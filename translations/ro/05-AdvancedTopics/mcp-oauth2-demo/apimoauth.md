# Implementarea aplicației Spring AI MCP pe Azure Container Apps

> [!WARNING]
> Acest server combinat de autorizare/resurse este destinat pentru învățare și
> utilizare în dev/test. Sistemele de producție ar trebui să folosească un furnizor de identitate dedicat,
> chei de semnare persistente și acreditări stocate într-un magazin de secrete gestionat.

 ([Securizarea serverelor Spring AI MCP cu OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Server Spring AI MCP securizat cu Spring Authorization Server. Serverul emite tokenuri de acces către clienți și le validează la cererile primite (sursa: blog Spring) ([Securizarea serverelor Spring AI MCP cu OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Pentru a implementa serverul Spring MCP, îl construiți ca un container și folosiți Azure Container Apps cu acces extern. De exemplu, folosind CLI-ul Azure puteți rula:

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

Acest lucru creează o aplicație Container accesibilă public cu HTTPS activat (Azure emite un certificat TLS gratuit pentru domeniul implicit `*.azurecontainerapps.io` ([Nume domenii personalizate și certificate gestionate gratuite în Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Ieșirea comenzii include FQDN-ul aplicației (de ex. `my-mcp-app.eastus.azurecontainerapps.io`), care devine baza **URL-ului emitent**. Asigurați-vă că accesul HTTP este activat (ca mai sus) pentru ca APIM să poată accesa aplicația. Într-un setup test/dev, folosiți opțiunea `--ingress external` (sau legați un domeniu personalizat cu TLS conform [documentației Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nume domenii personalizate și certificate gestionate gratuite în Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Stocați orice proprietăți sensibile (precum secrete OAuth client) în secretele Container Apps sau Azure Key Vault și mapați-le în container ca variabile de mediu. 

## Configurarea Spring Authorization Server

În codul aplicației Spring Boot, includeți starterele Spring Authorization Server și Resource Server. Configurați un `RegisteredClient` (pentru grantul `client_credentials` în dev/test) și o sursă de chei JWT. De exemplu, în `application.properties` puteți seta:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
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
            // Activează punctele finale ale serverului de autorizare
            .apply(authzServer.and())
            // Activează serverul de resurse (validare JWT pentru cererile primite)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Dezactivează CSRF (serverul MCP nu este bazat pe browser)
            .csrf(csrf -> csrf.disable())
            // Permite CORS pentru uneltele demo ale clientului
            .cors(withDefaults());
        return http.build();
    }

    // Definește un client în memorie (RegisteredClient) și o sursă JWK:
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
        // Generează o cheie RSA (pentru dezvoltare/test, generează una nouă la pornire)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Această configurare va expune endpoint-urile OAuth2 implicite: `/oauth2/token` pentru tokenuri și `/oauth2/jwks` pentru JSON Web Key Set. (Implicit, `AuthorizationServerSettings` Spring mapează `/oauth2/token` și `/oauth2/jwks` ([Model de Configurație :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serverul va emite tokenuri JWT de acces semnate cu cheia RSA de mai sus și va publica cheia publică la `https://<your-app>:/oauth2/jwks`. 

**Activați descoperirea OpenID Connect:** Pentru ca APIM să poată prelua automat issuerul și JWKS, activați endpointul de configurare a furnizorului OIDC adăugând `.oidc(Customizer.withDefaults())` în configurația de securitate ([Model de Configurație :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). De exemplu:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– activează /.well-known/openid-configuration
```

Acesta expune `/.well-known/openid-configuration`, pe care APIM îl poate folosi pentru metadate. În final, s-ar putea să doriți să personalizați afirmația JWT **audience** pentru ca verificarea APIM `<audiences>` să treacă. De exemplu, adăugați un customizer pentru token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Setează o audiență personalizată (de exemplu, ID-ul clientului sau identificatorul API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Aceasta se asigură că tokenurile poartă `"aud": ["mcp-client"]`, corespunzător ID-ului client sau scopului așteptat de APIM. 

## Expunerea endpoint-urilor Token și JWKS

După implementare, **URL-ul emitent** al aplicației va fi `https://<app-fqdn>`, ex. `https://my-mcp-app.eastus.azurecontainerapps.io`. Endpoint-urile sale OAuth2 sunt:

- **Endpoint token:** `https://<app-fqdn>/oauth2/token` – aici clienții obțin tokenuri (flux client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – returnează setul JWK (folosit de APIM pentru a obține cheile de semnare).
- **Config OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON pentru descoperire OIDC (conține `issuer`, `token_endpoint`, `jwks_uri` etc.).  

APIM va indica către **URL-ul de configurație OpenID**, de unde va descoperi `jwks_uri`. De exemplu, dacă FQDN-ul Container App este `my-mcp-app.eastus.azurecontainerapps.io`, atunci `<openid-config url="...">` din APIM ar trebui să folosească `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Implicit, Spring setează `issuer` în acele metadate la aceeași adresă de bază ([Model de Configurație :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurarea Azure API Management (`validate-jwt`)

În Azure APIM, adăugați o politică inbound care folosește politica `<validate-jwt>` pentru a verifica JWT-urile primite față de Spring Authorization Server. Pentru o configurare simplă, puteți utiliza URL-ul pentru metadatele OpenID Connect. Exemplu de fragment de politică:

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

Această politică spune APIM să preia configurația OpenID de la Spring Auth Server, să obțină JWKS și să valideze că fiecare token este semnat cu o cheie de încredere și are audiența corectă. (Dacă omiteți `<issuers>`, APIM va folosi automat afirmația `issuer` din metadate.) `<audience>` trebuie să corespundă ID-ului clientului sau identificatorului resursei API din token (în exemplul de mai sus, am setat `"mcp-client"`). Acest lucru este conform documentației Microsoft privind utilizarea `validate-jwt` cu `<openid-config>` ([Referință politică Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

După validare, APIM va transmite cererea (inclusiv header-ul `Authorization` original) către backend. Deoarece aplicația Spring este și server de resurse, va revalida tokenul, dar APIM deja i-a verificat validitatea. (Pentru dezvoltare, puteți să vă bazați pe verificarea APIM și să dezactivați verificări suplimentare în aplicație, dacă doriți, însă este mai sigur să păstrați ambele.)

## Setări de exemplu

| Setare            | Valoare exemplu                                                   | Note                                      |
|-------------------|-----------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`               | URL-ul aplicației Container App (URI de bază)       |
| **Endpoint token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`  | Endpoint token Spring implicit ([Model de Configurație :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Endpoint JWKS** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`   | Endpoint JWK Set implicit ([Model de Configurație :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Config OpenID** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Document de descoperire OIDC (generat automat)     |
| **Audiență APIM** | `mcp-client`                                                    | ID client OAuth sau numele resursei API        |
| **Politică APIM** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` folosește acest URL ([Referință politică Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Capcane comune

- **HTTPS/TLS:** Gateway-ul APIM necesită ca endpointul OpenID/JWKS să fie HTTPS cu un certificat valid. Implicit, Azure Container Apps oferă un certificat TLS de încredere pentru domeniul gestionat de Azure ([Nume domenii personalizate și certificate gestionate gratuite în Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Dacă folosiți un domeniu personalizat, asigurați-vă că legați un certificat (puteți folosi funcția Azure de certificat gestionat gratuit) ([Nume domenii personalizate și certificate gestionate gratuite în Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Dacă APIM nu poate avea încredere în certificatul endpointului, `<validate-jwt>` va eșua la preluarea metadatelor.  

- **Accesibilitatea endpointului:** Asigurați-vă că endpointurile aplicației Spring sunt accesibile din APIM. Folosind `--ingress external` (sau activând accesul în portal) este cea mai simplă variantă. Dacă ați ales un mediu intern sau legat de vNet, APIM (implicat public) s-ar putea să nu poată ajunge aici decât dacă este plasat în același vNet. Într-un mediu de test, preferați accesul public astfel încât APIM să poată apela URL-urile `.well-known` și `/jwks`. 

- **Descoperirea OpenID activată:** Implicit, Spring Authorization Server **nu expune** `/.well-known/openid-configuration` decât dacă OIDC este activat. Asigurați-vă că includeți `.oidc(Customizer.withDefaults())` în configurația dvs. de securitate (vezi mai sus) astfel încât endpointul de configurare al furnizorului să fie activ ([Model de Configurație :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). În caz contrar, apelul APIM `<openid-config>` va genera 404.

- **Afirmația Audience:** Comportamentul implicit Spring este să seteze afirmația `aud` la ID-ul clientului. Dacă verificarea `<audience>` APIM eșuează, poate fi nevoie să personalizați tokenul (așa cum s-a arătat mai sus) sau să ajustați politica APIM. Asigurați-vă că audiența din JWT corespunde cu ce configurați în `<audience>`. 

- **Parcurgerea metadatelor JSON:** Documentul JSON de configurare OpenID trebuie să fie valid. Configurația implicită Spring va emite un document standard de metadate OIDC. Verificați că conține corect `issuer` și `jwks_uri`. Dacă găzduiți Spring în spatele unui proxy sau rutare pe bază de cale, verificați URL-urile din aceste metadate. APIM va folosi aceste valori ca atare. 

- **Ordinea politicilor:** În politica APIM, plasați `<validate-jwt>` **înainte** de orice rutare către backend. Altfel, apelurile ar putea ajunge la aplicația dvs. fără token valid. De asemenea, asigurați-vă că `<validate-jwt>` apare imediat sub `<inbound>` (nu este în interiorul unei alte condiții) pentru ca APIM să o aplice.

Urmând pașii de mai sus, puteți rula serverul Spring AI MCP în Azure Container Apps și să aveți Azure API Management care validează JWT-urile OAuth2 primite cu o politică minimă. Punctele cheie sunt: expuneți endpoint-urile Spring Auth public cu TLS, activați descoperirea OIDC și direcționați `validate-jwt` APIM către URL-ul de configurare OpenID (pentru a putea prelua JWKS automat). Această configurație este potrivită pentru medii dev/test; pentru producție, luați în considerare o gestionare adecvată a secretelor, duratele tokenurilor și rotația cheilor în JWKS după necesitate. 


**Referințe:** Consultați documentația Spring Authorization Server pentru endpoint-urile implicite ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) și configurarea OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consultați documentația Microsoft APIM pentru exemple `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); și documentația Azure Container Apps pentru implementare și certificate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->