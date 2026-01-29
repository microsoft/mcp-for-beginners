# Wdrażanie aplikacji Spring AI MCP na Azure Container Apps

 ([Zabezpieczanie serwerów Spring AI MCP za pomocą OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Rysunek: Serwer Spring AI MCP zabezpieczony za pomocą Spring Authorization Server. Serwer wydaje tokeny dostępu klientom i weryfikuje je przy nadchodzących żądaniach (źródło: blog Spring) ([Zabezpieczanie serwerów Spring AI MCP za pomocą OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Aby wdrożyć serwer Spring MCP, zbuduj go jako kontener i użyj Azure Container Apps z zewnętrznym dostępem (ingress). Na przykład, korzystając z Azure CLI, możesz uruchomić:

```bash
az containerapp up \
  --name my-mcp-app \
  --resource-group MyResourceGroup \
  --location eastus \
  --environment MyContainerEnv \
  --image myregistry.azurecr.io/my-mcp-server:latest \
  --ingress external \
  --target-port 8080 \
  --query properties.configuration.ingress.fqdn
```

To tworzy publicznie dostępny Container App z włączonym HTTPS (Azure wydaje darmowy certyfikat TLS dla domyślnej domeny `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). W wyniku polecenia otrzymasz FQDN aplikacji (np. `my-mcp-app.eastus.azurecontainerapps.io`), który stanie się bazowym **issuer URL**. Upewnij się, że włączony jest dostęp HTTP (ingress) (jak powyżej), aby APIM mógł się połączyć z aplikacją. W środowisku testowym/deweloperskim użyj opcji `--ingress external` (lub powiąż niestandardową domenę z TLS zgodnie z [dokumentacją Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Przechowuj wszelkie poufne dane (np. sekrety klienta OAuth) w sekretach Container Apps lub Azure Key Vault i mapuj je do kontenera jako zmienne środowiskowe.

## Konfiguracja Spring Authorization Server

W kodzie aplikacji Spring Boot dołącz startery Spring Authorization Server i Resource Server. Skonfiguruj `RegisteredClient` (dla grant typu `client_credentials` w środowisku dev/test) oraz źródło klucza JWT. Na przykład, w `application.properties` możesz ustawić:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Włącz Authorization Server i Resource Server definiując security filter chain. Przykład:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Enable the Authorization Server endpoints
            .apply(authzServer.and())
            // Enable the Resource Server (validate JWT on incoming requests)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Disable CSRF (MCP server is not browser-based)
            .csrf(csrf -> csrf.disable())
            // Allow CORS for client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Define an in-memory client (RegisteredClient) and a JWK source:
    @Bean
    public RegisteredClientRepository registeredClientRepository() {
        RegisteredClient client = RegisteredClient.withId("1")
            .clientId("mcp-client")
            .clientSecret("{noop}secret")
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Generate an RSA key (for dev/test, generate anew at startup)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ta konfiguracja udostępni domyślne endpointy OAuth2: `/oauth2/token` do pobierania tokenów oraz `/oauth2/jwks` do JSON Web Key Set. (Domyślnie `AuthorizationServerSettings` Springa mapuje `/oauth2/token` i `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serwer będzie wydawał tokeny JWT podpisane kluczem RSA powyżej i udostępni swój klucz publiczny pod adresem `https://<twoja-aplikacja>:/oauth2/jwks`.

**Włącz odkrywanie OpenID Connect:** Aby APIM mógł automatycznie pobrać issuer i JWKS, włącz endpoint konfiguracji dostawcy OIDC, dodając `.oidc(Customizer.withDefaults())` w konfiguracji zabezpieczeń ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Przykład:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

To udostępni `/.well-known/openid-configuration`, z którego APIM może pobrać metadane. Na koniec możesz chcieć dostosować polecenie JWT **audience**, aby APIM przeszedł sprawdzenie `<audiences>`. Na przykład, dodaj customizer tokena:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dzięki temu tokeny będą zawierać `"aud": ["mcp-client"]`, co odpowiada ID klienta lub oczekiwanemu zakresowi przez APIM.

## Udostępnianie endpointów Token i JWKS

Po wdrożeniu, **issuer URL** Twojej aplikacji będzie `https://<app-fqdn>`, np. `https://my-mcp-app.eastus.azurecontainerapps.io`. Jej endpointy OAuth2 to:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – tutaj klienci pobierają tokeny (flow client_credentials).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – zwraca zestaw JWK (używany przez APIM do pobierania kluczy podpisujących).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON odkrywania OIDC (zawiera `issuer`, `token_endpoint`, `jwks_uri` itd.).

APIM będzie wskazywał na **URL konfiguracji OpenID**, z którego pobierze `jwks_uri`. Na przykład, jeśli FQDN Twojej Container App to `my-mcp-app.eastus.azurecontainerapps.io`, to `<openid-config url="...">` w APIM powinno używać `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Domyślnie Spring ustawi `issuer` w tych metadanych na ten sam bazowy URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguracja Azure API Management (`validate-jwt`)

W Azure APIM dodaj politykę inbound, która używa `<validate-jwt>` do weryfikacji nadchodzących JWT względem Twojego Spring Authorization Server. Dla prostego setupu możesz użyć URL metadanych OpenID Connect. Przykładowy fragment polityki:

```xml
<inbound>
  <validate-jwt header-name="Authorization" require-scheme="Bearer">
    <openid-config url="https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration" />
    <audiences>
      <audience>mcp-client</audience>  <!-- Expected audience in the JWT -->
    </audiences>
    <issuers>
      <issuer>https://my-mcp-app.eastus.azurecontainerapps.io</issuer>
    </issuers>
  </validate-jwt>
  <!-- (optional) other policies -->
</inbound>
```

Ta polityka nakazuje APIM pobrać konfigurację OpenID z serwera Spring Auth, pobrać jego JWKS i zweryfikować, że każdy token jest podpisany zaufanym kluczem oraz ma poprawne audience. (Jeśli pominiesz `<issuers>`, APIM automatycznie użyje `issuer` z metadanych.) `<audience>` powinno odpowiadać ID klienta lub identyfikatorowi zasobu API w tokenie (w powyższym przykładzie ustawiliśmy `"mcp-client"`). To zgodne z dokumentacją Microsoft dotyczącą użycia `validate-jwt` z `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po weryfikacji APIM przekaże żądanie (łącznie z oryginalnym nagłówkiem `Authorization`) do backendu. Ponieważ aplikacja Spring jest również resource serverem, ponownie zweryfikuje token, ale APIM już potwierdził jego ważność. (W środowisku deweloperskim możesz polegać na weryfikacji APIM i wyłączyć dodatkowe sprawdzenia w aplikacji, ale bezpieczniej jest mieć oba.)

## Przykładowe ustawienia

| Ustawienie         | Przykładowa wartość                                                | Uwagi                                      |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL Twojej Container App (bazowy URI)      |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Domyślny endpoint tokenów Springa ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Domyślny endpoint JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Dokument odkrywania OIDC (generowany automatycznie)    |
| **APIM audience**  | `mcp-client`                                                      | ID klienta OAuth lub nazwa zasobu API      |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` używa tego URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Typowe pułapki

- **HTTPS/TLS:** Brama APIM wymaga, aby endpoint OpenID/JWKS był dostępny przez HTTPS z ważnym certyfikatem. Domyślnie Azure Container Apps zapewnia zaufany certyfikat TLS dla domeny zarządzanej przez Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jeśli używasz niestandardowej domeny, pamiętaj o powiązaniu certyfikatu (możesz skorzystać z darmowego certyfikatu zarządzanego przez Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jeśli APIM nie zaufa certyfikatowi endpointu, `<validate-jwt>` nie pobierze metadanych.

- **Dostępność endpointów:** Upewnij się, że endpointy aplikacji Spring są dostępne z APIM. Najprościej jest użyć `--ingress external` (lub włączyć ingress w portalu). Jeśli wybrałeś środowisko wewnętrzne lub powiązane z vNet, APIM (domyślnie publiczne) może nie mieć do nich dostępu, chyba że znajduje się w tym samym VNet. W środowisku testowym preferuj publiczny ingress, aby APIM mógł wywołać `.well-known` i `/jwks`.

- **Włączone odkrywanie OpenID:** Domyślnie Spring Authorization Server **nie udostępnia** `/.well-known/openid-configuration`, jeśli OIDC nie jest włączone. Upewnij się, że w konfiguracji zabezpieczeń dodałeś `.oidc(Customizer.withDefaults())` (patrz wyżej), aby endpoint konfiguracji dostawcy był aktywny ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). W przeciwnym razie wywołanie `<openid-config>` w APIM zwróci 404.

- **Polecenie Audience:** Domyślnie Spring ustawia `aud` na ID klienta. Jeśli sprawdzenie `<audience>` w APIM nie przejdzie, może być konieczne dostosowanie tokena (jak pokazano powyżej) lub zmiana polityki APIM. Upewnij się, że audience w JWT odpowiada temu, co konfigurujesz w `<audience>`.

- **Parsowanie metadanych JSON:** JSON konfiguracji OpenID musi być poprawny. Domyślna konfiguracja Springa wygeneruje standardowy dokument metadanych OIDC. Sprawdź, czy zawiera poprawne `issuer` i `jwks_uri`. Jeśli hostujesz Spring za proxy lub trasą opartą na ścieżce, dokładnie zweryfikuj URL-e w tych metadanych. APIM użyje ich bez zmian.

- **Kolejność polityk:** W polityce APIM umieść `<validate-jwt>` **przed** jakimkolwiek routingiem do backendu. W przeciwnym razie żądania mogą dotrzeć do aplikacji bez ważnego tokena. Upewnij się też, że `<validate-jwt>` znajduje się bezpośrednio pod `<inbound>` (nie zagnieżdżony w innym warunku), aby APIM go zastosował.

Postępując zgodnie z powyższymi krokami, możesz uruchomić serwer Spring AI MCP w Azure Container Apps i pozwolić Azure API Management na weryfikację nadchodzących tokenów OAuth2 JWT za pomocą minimalnej polityki. Kluczowe elementy to: udostępnienie endpointów Spring Auth publicznie z TLS, włączenie odkrywania OIDC oraz skierowanie `validate-jwt` APIM na URL konfiguracji OpenID (aby automatycznie pobierać JWKS). To rozwiązanie nadaje się do środowisk deweloperskich/testowych; w produkcji warto zadbać o odpowiednie zarządzanie sekretami, czas życia tokenów oraz rotację kluczy w JWKS.
**Referencje:** Zobacz dokumentację Spring Authorization Server dotyczącą domyślnych punktów końcowych ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) oraz konfiguracji OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); zobacz dokumentację Microsoft APIM dla przykładów `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); oraz dokumentację Azure Container Apps dotyczącą wdrożenia i certyfikatów ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.