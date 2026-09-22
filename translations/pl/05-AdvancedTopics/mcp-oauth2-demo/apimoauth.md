# Wdrażanie aplikacji Spring AI MCP na Azure Container Apps

> [!WARNING]
> Ten połączony serwer autoryzacji/zasobów jest przeznaczony do celów edukacyjnych oraz
> środowisk deweloperskich/testowych. Systemy produkcyjne powinny korzystać z dedykowanego dostawcy tożsamości,
> trwałych kluczy podpisujących oraz przechowywania poświadczeń w zarządzanym magazynie sekretów.

 ([Zabezpieczanie serwerów Spring AI MCP za pomocą OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Rysunek: Serwer Spring AI MCP zabezpieczony przez Spring Authorization Server. Serwer wydaje tokeny dostępu klientom i waliduje je przy nadchodzących żądaniach (źródło: Spring blog) ([Zabezpieczanie serwerów Spring AI MCP za pomocą OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Aby wdrożyć serwer Spring MCP, zbuduj go jako kontener i użyj Azure Container Apps z zewnętrznym dostępem. Na przykład, używając Azure CLI, możesz wykonać:

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

To tworzy publicznie dostępny Container App z włączonym HTTPS (Azure wydaje darmowy certyfikat TLS dla domyślnej domeny `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). W wyjściu polecenia znajduje się FQDN aplikacji (np. `my-mcp-app.eastus.azurecontainerapps.io`), który staje się bazą **issuer URL**. Upewnij się, że dostęp HTTP jest włączony (jak powyżej), aby APIM mógł dotrzeć do aplikacji. W środowisku testowym/dev użyj opcji `--ingress external` (lub powiąż własną domenę z TLS zgodnie z dokumentacją Microsoft ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Przechowuj wszelkie poufne właściwości (takie jak sekret klienta OAuth) w sekretach Container Apps lub Azure Key Vault i mapuj je do kontenera jako zmienne środowiskowe.

## Konfiguracja Spring Authorization Server

W kodzie aplikacji Spring Boot dołącz Spring Authorization Server oraz Resource Server starters. Skonfiguruj `RegisteredClient` (dla grant’u `client_credentials` w środowisku deweloperskim/testowym) oraz źródło klucza JWT. Na przykład, w `application.properties` możesz ustawić:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Włącz Authorization Server oraz Resource Server definiując łańcuch filtrów bezpieczeństwa. Na przykład:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Włącz punkty końcowe serwera autoryzacji
            .apply(authzServer.and())
            // Włącz serwer zasobów (weryfikuj JWT w nadchodzących żądaniach)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Wyłącz CSRF (serwer MCP nie jest oparty na przeglądarce)
            .csrf(csrf -> csrf.disable())
            // Zezwól na CORS dla narzędzi demo klienta
            .cors(withDefaults());
        return http.build();
    }

    // Zdefiniuj klienta w pamięci (RegisteredClient) i źródło JWK:
    @Bean
    public RegisteredClientRepository registeredClientRepository(
        @Value("${demo.oauth.client-id}") String clientId,
        @Value("${demo.oauth.client-secret}") String clientSecret) {
      PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
        RegisteredClient client = RegisteredClient.withId("1")
        .clientId(clientId)
        .clientSecret(encoder.encode(clientSecret))
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Wygeneruj klucz RSA (dla deweloperki/testów, generuj ponownie przy starcie)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ta konfiguracja udostępni domyślne endpointy OAuth2: `/oauth2/token` dla tokenów oraz `/oauth2/jwks` dla JSON Web Key Set. (Domyślnie `AuthorizationServerSettings` Springa mapuje `/oauth2/token` oraz `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serwer będzie wydawać tokeny dostępu JWT podpisane kluczem RSA powyżej oraz opublikuje swój klucz publiczny pod adresem `https://<twoja-aplikacja>:/oauth2/jwks`.

**Włącz odkrywanie OpenID Connect:** Aby pozwolić APIM automatycznie pobierać issuer oraz JWKS, włącz endpoint konfiguracyjny dostawcy OIDC dodając `.oidc(Customizer.withDefaults())` w konfiguracji bezpieczeństwa ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Na przykład:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– włącza /.well-known/openid-configuration
```

To udostępni `/.well-known/openid-configuration`, które APIM może użyć do metadanych. Na końcu możesz dostosować roszczenie JWT **audience**, tak aby sprawdzenie `<audiences>` APIM przeszło pomyślnie. Na przykład, dodaj customizer tokena:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Ustaw niestandardową grupę odbiorców (np. identyfikator klienta lub identyfikator API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

To zapewnia, że tokeny zawierają `"aud": ["mcp-client"]`, co odpowiada ID klienta lub scope oczekiwanemu przez APIM.

## Udostępnianie endpointów Token i JWKS

Po wdrożeniu, **issuer URL** Twojej aplikacji będzie `https://<app-fqdn>`, np. `https://my-mcp-app.eastus.azurecontainerapps.io`. Jej endpointy OAuth2 to:

- **Endpoint tokenów:** `https://<app-fqdn>/oauth2/token` – tutaj klienci pobierają tokeny (flow client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – zwraca zestaw JWK (używany przez APIM do pobierania kluczy podpisujących).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON do odkrywania OIDC (zawiera `issuer`, `token_endpoint`, `jwks_uri` itd.).

APIM będzie wskazywać na **OpenID configuration URL**, z którego odkrywa `jwks_uri`. Na przykład, jeśli FQDN Twojego Container App to `my-mcp-app.eastus.azurecontainerapps.io`, to `<openid-config url="...">` w APIM powinien używać `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Domyślnie Spring ustawia `issuer` w tych metadanych na ten sam bazowy URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguracja Azure API Management (`validate-jwt`)

W Azure APIM dodaj politykę przychodzącą, która używa polityki `<validate-jwt>` do weryfikacji nadchodzących JWT względem Twojego Spring Authorization Server. Dla prostego ustawienia możesz użyć URL-a metadanych OpenID Connect. Przykładowy fragment polityki:

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

Ta polityka nakazuje APIM pobrać konfigurację OpenID z serwera autoryzacji Spring, pobrać z niej JWKS i zweryfikować, że każdy token jest podpisany zaufanym kluczem oraz ma właściwe audience. (Jeśli pominięto `<issuers>`, APIM automatycznie użyje `issuer` z metadanych.) `<audience>` powinno odpowiadać ID klienta lub identyfikatorowi zasobu API w tokenie (w powyższym przykładzie ustawiono na `"mcp-client"`). Jest to zgodne z dokumentacją Microsoft dotyczącą użycia `validate-jwt` z `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po weryfikacji APIM przesyła żądanie (łącznie z oryginalnym nagłówkiem `Authorization`) do backendu. Ponieważ aplikacja Spring jest także serwerem zasobów, ponownie zweryfikuje token, ale APIM już zagwarantował jego ważność. (W środowisku developerskim można polegać na weryfikacji APIM i wyłączyć dodatkowe sprawdzenia w aplikacji, jeśli chcemy, ale bezpieczniej jest zachować oba.)

## Przykładowe ustawienia

| Ustawienie          | Przykładowa wartość                                                | Uwagi                                      |
|--------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | URL Twojej aplikacji Container App (bazowy URI)  |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Domyślny endpoint tokenów Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Domyślny endpoint JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Dokument do odkrywania OIDC (generowany automatycznie)    |
| **APIM audience**  | `mcp-client`                                                       | ID klienta OAuth lub nazwa zasobu API       |
| **Polityka APIM**  | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` używa tego URL-a ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Powszechne problemy

- **HTTPS/TLS:** Brama APIM wymaga, aby endpoint OpenID/JWKS był dostępny przez HTTPS z ważnym certyfikatem. Domyślnie Azure Container Apps dostarcza zaufany certyfikat TLS dla zarządzanej domeny Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jeśli używasz własnej domeny, pamiętaj, aby powiązać certyfikat (możesz skorzystać z darmowej funkcji certyfikatu zarządzanego Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jeśli APIM nie będzie ufał certyfikatowi endpointu, `<validate-jwt>` nie będzie mógł pobrać metadanych.

- **Dostępność endpointów:** Upewnij się, że endpointy aplikacji Spring są dostępne z APIM. Użycie `--ingress external` (lub włączenie ingress w portalu) jest najprostszym rozwiązaniem. Jeśli wybrałeś środowisko wewnętrzne lub powiązane z vNet, APIM (domyślnie publiczne) może nie mieć do niego dostępu, jeśli nie znajduje się w tym samym vNet. W środowisku testowym polecany jest publiczny ingress, aby APIM mógł wywołać adresy `.well-known` i `/jwks`.

- **Włączone odkrywanie OpenID:** Domyślnie Spring Authorization Server **nie udostępnia** `/.well-known/openid-configuration` jeśli OIDC nie jest włączony. Upewnij się, że w konfiguracji bezpieczeństwa dodałeś `.oidc(Customizer.withDefaults())` (patrz wyżej), żeby endpoint konfiguracji dostawcy był aktywny ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). W przeciwnym razie wywołanie `<openid-config>` w APIM zakończy się błędem 404.

- **Roszczenie Audience:** Domyślne zachowanie Springa to ustawienie `aud` na ID klienta. Jeśli weryfikacja `<audience>` APIM się nie powiedzie, może być konieczne dostosowanie tokena (jak pokazano powyżej) lub zmiana polityki APIM. Upewnij się, że audience w JWT odpowiada temu, co konfigurujesz w `<audience>`.

- **Parsowanie metadanych JSON:** JSON konfiguracyjny OpenID musi być poprawny. Domyślna konfiguracja Springa wygeneruje standardowy dokument metadanych OIDC. Sprawdź, czy zawiera poprawne `issuer` i `jwks_uri`. Jeśli hostujesz Spring za proxy lub ścieżką, dokładnie sprawdź URL-e w tych metadanych. APIM użyje ich bez zmian.

- **Porządek polityk:** W polityce APIM umieść `<validate-jwt>` **przed** routingiem do backendu. W przeciwnym razie żądania mogą trafić do Twojej aplikacji bez ważnego tokena. Upewnij się również, że `<validate-jwt>` znajduje się bezpośrednio pod `<inbound>` (nie zagnieżdżony w innym warunku), aby APIM go zastosował.

Postępując według powyższych kroków, możesz uruchomić serwer Spring AI MCP w Azure Container Apps i mieć Azure API Management weryfikujący przychodzące tokeny OAuth2 JWT przy minimalnej polityce. Kluczowe elementy to: udostępnianie publiczne endpointów Spring Auth z TLS, włączenie odkrywania OIDC oraz skonfigurowanie `validate-jwt` w APIM z URL-em konfiguracji OpenID (aby automatycznie pobierał JWKS). Ta konfiguracja nadaje się do środowiska deweloperskiego/testowego; do produkcji rozważ odpowiednie zarządzanie sekretami, czasy życia tokenów oraz rotację kluczy w JWKS według potrzeb.


**Źródła:** Zobacz dokumentację Spring Authorization Server dotyczącą domyślnych punktów końcowych ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) oraz konfiguracji OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); zobacz dokumentację Microsoft APIM dla przykładów `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); oraz dokumentację Azure Container Apps dotyczącą wdrożenia i certyfikatów ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->