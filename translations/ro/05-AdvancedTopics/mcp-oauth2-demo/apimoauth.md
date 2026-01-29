# Implementarea aplicației Spring AI MCP pe Azure Container Apps

([Securizarea serverelor Spring AI MCP cu OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figură: Server Spring AI MCP securizat cu Spring Authorization Server. Serverul emite tokenuri de acces către clienți și le validează la cererile primite (sursa: blog Spring) ([Securizarea serverelor Spring AI MCP cu OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Pentru a implementa serverul Spring MCP, construiți-l ca un container și folosiți Azure Container Apps cu ingress extern. De exemplu, folosind Azure CLI puteți rula:

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

Aceasta creează o aplicație Container accesibilă public, cu HTTPS activat (Azure emite un certificat TLS gratuit pentru domeniul implicit `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Ieșirea comenzii include FQDN-ul aplicației (ex. `my-mcp-app.eastus.azurecontainerapps.io`), care devine baza **issuer URL**. Asigurați-vă că ingress-ul HTTP este activat (așa cum este descris mai sus) pentru ca APIM să poată accesa aplicația. Într-un mediu de testare/dezvoltare, folosiți opțiunea `--ingress external` (sau legați un domeniu personalizat cu TLS conform [documentației Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Stocați orice proprietăți sensibile (cum ar fi secretele clientului OAuth) în secretele Container Apps sau în Azure Key Vault și mapați-le în container ca variabile de mediu.

## Configurarea Spring Authorization Server

În codul aplicației Spring Boot, includeți starter-ele Spring Authorization Server și Resource Server. Configurați un `RegisteredClient` (pentru grantul `client_credentials` în dev/test) și o sursă de chei JWT. De exemplu, în `application.properties` puteți seta:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Activați Authorization Server și Resource Server definind un lanț de filtre de securitate. De exemplu:

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

Această configurație va expune endpoint-urile OAuth2 implicite: `/oauth2/token` pentru tokenuri și `/oauth2/jwks` pentru JSON Web Key Set. (Implicit, `AuthorizationServerSettings` din Spring mapează `/oauth2/token` și `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serverul va emite tokenuri JWT semnate cu cheia RSA de mai sus și va publica cheia publică la `https://<your-app>:/oauth2/jwks`.

**Activați descoperirea OpenID Connect:** Pentru ca APIM să poată prelua automat issuer-ul și JWKS, activați endpoint-ul de configurare al provider-ului OIDC adăugând `.oidc(Customizer.withDefaults())` în configurația de securitate ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). De exemplu:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Aceasta expune `/.well-known/openid-configuration`, pe care APIM îl poate folosi pentru metadate. În final, este posibil să doriți să personalizați revendicarea JWT **audience** astfel încât verificarea `<audiences>` din APIM să treacă. De exemplu, adăugați un customizer pentru token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Astfel, tokenurile vor conține `"aud": ["mcp-client"]`, corespunzător ID-ului clientului sau scope-ului așteptat de APIM.

## Expunerea endpoint-urilor Token și JWKS

După implementare, **issuer URL** al aplicației va fi `https://<app-fqdn>`, de exemplu `https://my-mcp-app.eastus.azurecontainerapps.io`. Endpoint-urile OAuth2 sunt:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – aici clienții obțin tokenuri (flux client_credentials).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – returnează setul JWK (folosit de APIM pentru a obține cheile de semnare).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON pentru descoperirea OIDC (conține `issuer`, `token_endpoint`, `jwks_uri` etc.).

APIM va folosi **URL-ul de configurare OpenID**, de unde va descoperi `jwks_uri`. De exemplu, dacă FQDN-ul Container App este `my-mcp-app.eastus.azurecontainerapps.io`, atunci `<openid-config url="...">` din APIM trebuie să folosească `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Implicit, Spring setează `issuer` în acele metadate la aceeași adresă de bază ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurarea Azure API Management (`validate-jwt`)

În Azure APIM, adăugați o politică inbound care folosește `<validate-jwt>` pentru a verifica JWT-urile primite față de Spring Authorization Server. Pentru o configurare simplă, puteți folosi URL-ul de metadate OpenID Connect. Exemplu de fragment de politică:

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

Această politică spune APIM să preia configurația OpenID de la Spring Auth Server, să obțină JWKS și să valideze că fiecare token este semnat cu o cheie de încredere și are audiența corectă. (Dacă omiteți `<issuers>`, APIM va folosi automat valoarea `issuer` din metadate.) `<audience>` trebuie să corespundă ID-ului clientului sau identificatorului resursei API din token (în exemplul de mai sus, este setat la `"mcp-client"`). Aceasta este conformă cu documentația Microsoft privind folosirea `validate-jwt` cu `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

După validare, APIM va redirecționa cererea (inclusiv header-ul original `Authorization`) către backend. Deoarece aplicația Spring este și resource server, va revalida tokenul, dar APIM a asigurat deja validitatea acestuia. (Pentru dezvoltare, puteți să vă bazați pe verificarea APIM și să dezactivați verificările suplimentare în aplicație dacă doriți, dar este mai sigur să păstrați ambele.)

## Setări exemplu

| Setare             | Valoare exemplu                                                    | Note                                       |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL-ul aplicației Container App (URI de bază) |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Endpoint-ul implicit pentru token Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Endpoint-ul implicit pentru JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documentul de descoperire OIDC (generat automat) |
| **APIM audience**  | `mcp-client`                                                      | ID-ul clientului OAuth sau numele resursei API |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` folosește acest URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Capcane comune

- **HTTPS/TLS:** Gateway-ul APIM necesită ca endpoint-ul OpenID/JWKS să fie HTTPS cu un certificat valid. Implicit, Azure Container Apps oferă un certificat TLS de încredere pentru domeniul gestionat de Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Dacă folosiți un domeniu personalizat, asigurați-vă că legați un certificat (puteți folosi funcția gratuită de certificate gestionate Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Dacă APIM nu poate avea încredere în certificatul endpoint-ului, `<validate-jwt>` nu va putea prelua metadatele.

- **Accesibilitatea endpoint-urilor:** Asigurați-vă că endpoint-urile aplicației Spring sunt accesibile din APIM. Folosirea `--ingress external` (sau activarea ingress-ului în portal) este cea mai simplă soluție. Dacă ați ales un mediu intern sau legat de vNet, APIM (implicit public) s-ar putea să nu poată accesa aplicația decât dacă este în același VNet. Într-un mediu de testare, preferați ingress public pentru ca APIM să poată apela URL-urile `.well-known` și `/jwks`.

- **Descoperirea OpenID activată:** Implicit, Spring Authorization Server **nu expune** `/.well-known/openid-configuration` dacă OIDC nu este activat. Asigurați-vă că includeți `.oidc(Customizer.withDefaults())` în configurația de securitate (vezi mai sus) pentru ca endpoint-ul de configurare al provider-ului să fie activ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Altfel, apelul `<openid-config>` din APIM va returna 404.

- **Revendicarea Audience:** Comportamentul implicit al Spring este să seteze `aud` la ID-ul clientului. Dacă verificarea `<audience>` din APIM eșuează, poate fi necesar să personalizați tokenul (așa cum este arătat mai sus) sau să ajustați politica APIM. Asigurați-vă că audiența din JWT corespunde cu ce configurați în `<audience>`.

- **Parsarea metadatelor JSON:** JSON-ul de configurare OpenID trebuie să fie valid. Configurația implicită Spring va emite un document standard de metadate OIDC. Verificați că conține `issuer` și `jwks_uri` corecte. Dacă găzduiți Spring în spatele unui proxy sau rutare bazată pe cale, verificați cu atenție URL-urile din aceste metadate. APIM le va folosi exact așa cum sunt.

- **Ordinea politicilor:** În politica APIM, plasați `<validate-jwt>` **înainte** de orice rutare către backend. Altfel, cererile ar putea ajunge la aplicație fără un token valid. De asemenea, asigurați-vă că `<validate-jwt>` apare imediat sub `<inbound>` (nu este imbricat într-o altă condiție) pentru ca APIM să îl aplice.

Urmând pașii de mai sus, puteți rula serverul Spring AI MCP în Azure Container Apps și să permiteți Azure API Management să valideze JWT-urile OAuth2 primite cu o politică minimă. Punctele cheie sunt: expuneți endpoint-urile Spring Auth public cu TLS, activați descoperirea OIDC și indicați `validate-jwt` din APIM către URL-ul de configurare OpenID (pentru a prelua automat JWKS). Această configurație este potrivită pentru medii de dezvoltare/test; pentru producție, luați în considerare gestionarea corectă a secretelor, durata de viață a tokenurilor și rotația cheilor JWKS după necesitate.
**Referințe:** Consultați documentația Spring Authorization Server pentru endpoint-urile implicite ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) și configurarea OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consultați documentația Microsoft APIM pentru exemple `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); și documentația Azure Container Apps pentru implementare și certificate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.