# Deployanje Spring AI MCP aplikacije na Azure Container Apps

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Slika: Spring AI MCP server zaštićen Spring Authorization Serverom. Server izdaje pristupne tokene klijentima i provjerava ih pri dolaznim zahtjevima (izvor: Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Za deploy Spring MCP servera, izgradite ga kao kontejner i koristite Azure Container Apps s vanjskim pristupom (ingress). Na primjer, pomoću Azure CLI-ja možete pokrenuti:

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

Ovim se kreira javno dostupna Container App s omogućenim HTTPS-om (Azure izdaje besplatni TLS certifikat za zadanu domenu `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Izlaz naredbe uključuje FQDN aplikacije (npr. `my-mcp-app.eastus.azurecontainerapps.io`), koji postaje baza za **issuer URL**. Provjerite je li omogućen HTTP ingress (kao gore) kako bi APIM mogao pristupiti aplikaciji. U testnom/razvojnom okruženju koristite opciju `--ingress external` (ili povežite prilagođenu domenu s TLS-om prema [Microsoft dokumentaciji](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Osjetljive postavke (poput OAuth client secret-a) spremite u Container Apps secrets ili Azure Key Vault i mapirajte ih u kontejner kao varijable okoline.

## Konfiguracija Spring Authorization Servera

U kodu vaše Spring Boot aplikacije uključite Spring Authorization Server i Resource Server startere. Konfigurirajte `RegisteredClient` (za `client_credentials` grant u dev/test okruženju) i izvor JWT ključeva. Na primjer, u `application.properties` možete postaviti:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Omogućite Authorization Server i Resource Server definiranjem security filter chain-a. Na primjer:

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

Ova konfiguracija će izložiti zadane OAuth2 endpoint-e: `/oauth2/token` za tokene i `/oauth2/jwks` za JSON Web Key Set. (Springova `AuthorizationServerSettings` prema zadanim postavkama mapira `/oauth2/token` i `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server će izdavati JWT pristupne tokene potpisane RSA ključem gore i objavljivati svoj javni ključ na `https://<your-app>:/oauth2/jwks`.

**Omogućite OpenID Connect discovery:** Da bi APIM automatski dohvaćao issuer i JWKS, omogućite OIDC provider konfiguracijski endpoint dodavanjem `.oidc(Customizer.withDefaults())` u vašu sigurnosnu konfiguraciju ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Na primjer:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Ovo izlaže `/.well-known/openid-configuration`, koji APIM može koristiti za dohvat metapodataka. Na kraju, možda ćete htjeti prilagoditi JWT **audience** claim kako bi APIM-ova provjera `<audiences>` prošla. Na primjer, dodajte token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ovo osigurava da tokeni sadrže `"aud": ["mcp-client"]`, što odgovara client ID-u ili scope-u koji APIM očekuje.

## Izlaganje Token i JWKS endpointa

Nakon deploya, **issuer URL** vaše aplikacije bit će `https://<app-fqdn>`, npr. `https://my-mcp-app.eastus.azurecontainerapps.io`. Njeni OAuth2 endpointi su:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – klijenti ovdje dobivaju tokene (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – vraća JWK set (koji APIM koristi za dohvat ključeva za potpisivanje).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (sadrži `issuer`, `token_endpoint`, `jwks_uri` itd.).

APIM će koristiti **OpenID configuration URL** s kojeg otkriva `jwks_uri`. Na primjer, ako je FQDN vaše Container App `my-mcp-app.eastus.azurecontainerapps.io`, APIM-ov `<openid-config url="...">` treba koristiti `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Spring prema zadanim postavkama postavlja `issuer` u tim metapodacima na istu baznu URL adresu ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguracija Azure API Managementa (`validate-jwt`)

U Azure APIM-u dodajte inbound policy koji koristi `<validate-jwt>` za provjeru dolaznih JWT-ova prema vašem Spring Authorization Serveru. Za jednostavnu konfiguraciju možete koristiti OpenID Connect metadata URL. Primjer policy snippet-a:

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

Ova politika govori APIM-u da dohvaća OpenID konfiguraciju sa Spring Auth Servera, preuzima njegov JWKS i provjerava da je svaki token potpisan pouzdanim ključem i da ima ispravnu publiku. (Ako izostavite `<issuers>`, APIM će automatski koristiti `issuer` claim iz metapodataka.) `<audience>` treba odgovarati vašem client ID-u ili identifikatoru API resursa u tokenu (u gornjem primjeru postavljeno na `"mcp-client"`). Ovo je u skladu s Microsoftovom dokumentacijom o korištenju `validate-jwt` s `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Nakon validacije, APIM prosljeđuje zahtjev (uključujući originalni `Authorization` header) backendu. Budući da je Spring aplikacija također resource server, ponovno će validirati token, ali APIM je već osigurao njegovu valjanost. (Za razvoj možete se osloniti na APIM-ovu provjeru i po želji onemogućiti dodatne provjere u aplikaciji, no sigurnije je zadržati obje.)

## Primjer postavki

| Postavka           | Primjer vrijednosti                                                  | Napomene                                   |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL vaše Container App (baza URI)          |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Zadani Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Zadani JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery dokument (automatski generiran) |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID ili naziv API resursa       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` koristi ovaj URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Česte zamke

- **HTTPS/TLS:** APIM gateway zahtijeva da OpenID/JWKS endpoint bude HTTPS s valjanim certifikatom. Prema zadanim postavkama, Azure Container Apps pruža pouzdani TLS certifikat za Azure-managed domenu ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ako koristite prilagođenu domenu, obavezno povežite certifikat (možete koristiti Azure-ovu besplatnu managed cert funkcionalnost) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ako APIM ne može vjerovati certifikatu endpointa, `<validate-jwt>` neće moći dohvatiti metapodatke.

- **Dostupnost endpointa:** Provjerite da su endpointi Spring aplikacije dostupni iz APIM-a. Korištenje `--ingress external` (ili omogućavanje ingresa u portalu) je najjednostavnije. Ako ste odabrali interno ili vNet-bound okruženje, APIM (koji je prema zadanim postavkama javan) možda neće moći pristupiti osim ako nije u istom VNet-u. U testnom okruženju preferirajte javni ingress kako bi APIM mogao dohvatiti `.well-known` i `/jwks` URL-ove.

- **Omogućen OpenID Discovery:** Prema zadanim postavkama, Spring Authorization Server **ne izlaže** `/.well-known/openid-configuration` ako OIDC nije omogućen. Obavezno uključite `.oidc(Customizer.withDefaults())` u sigurnosnu konfiguraciju (vidi gore) kako bi provider konfiguracijski endpoint bio aktivan ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Inače će APIM-ov poziv `<openid-config>` vratiti 404.

- **Audience claim:** Zadano ponašanje Springa je postaviti `aud` claim na client ID. Ako APIM-ova provjera `<audience>` ne uspije, možda ćete morati prilagoditi token (kao što je prikazano gore) ili podesiti APIM politiku. Provjerite da publika u vašem JWT-u odgovara onome što ste konfigurirali u `<audience>`.

- **Parsiranje JSON metapodataka:** OpenID konfiguracijski JSON mora biti valjan. Zadana Spring konfiguracija emitira standardni OIDC metadata dokument. Provjerite da sadrži ispravan `issuer` i `jwks_uri`. Ako hostate Spring iza proxyja ili s rutiranjem po putanji, dvaput provjerite URL-ove u metapodacima. APIM će koristiti te vrijednosti onakve kakve jesu.

- **Redoslijed politika:** U APIM politici, stavite `<validate-jwt>` **prije** bilo kakvog usmjeravanja prema backendu. Inače pozivi mogu doći do aplikacije bez valjanog tokena. Također, osigurajte da `<validate-jwt>` stoji odmah ispod `<inbound>` (ne unutar drugog uvjeta) kako bi APIM pravilno primijenio provjeru.

Slijedeći ove korake, možete pokrenuti svoj Spring AI MCP server u Azure Container Apps i omogućiti Azure API Managementu da validira dolazne OAuth2 JWT-ove s minimalnom politikom. Ključne točke su: javno izložiti Spring Auth endpoint-e s TLS-om, omogućiti OIDC discovery i usmjeriti APIM-ov `validate-jwt` na OpenID config URL (kako bi automatski dohvaćao JWKS). Ova konfiguracija je prikladna za razvojno/testno okruženje; za produkciju razmotrite pravilno upravljanje tajnama, trajanje tokena i rotaciju ključeva u JWKS-u prema potrebi.
**Reference:** Pogledajte dokumentaciju Spring Authorization Server za zadane krajnje točke ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) i OIDC konfiguraciju ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); pogledajte Microsoft APIM dokumentaciju za primjere `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); i Azure Container Apps dokumentaciju za implementaciju i certifikate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.