# Postavljanje Spring AI MCP aplikacije na Azure Container Apps

> [!WARNING]
> Ovaj kombinirani server za autorizaciju/resurse namijenjen je učenju i
> razvoju/testiranju. Produkcijski sustavi trebaju koristiti namjenskog davatelja identiteta,
> trajne ključeve za potpisivanje i vjerodajnice pohranjene u upravljanom tajnom spremištu.

 ([Osiguravanje Spring AI MCP servera s OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Slika: Spring AI MCP server osiguran Spring Authorization Serverom. Server izdaje pristupne tokene klijentima i provjerava ih kod dolaznih zahtjeva (izvor: Spring blog) ([Osiguravanje Spring AI MCP servera s OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Za postavljanje Spring MCP servera, izgradite ga kao kontejner i koristite Azure Container Apps s vanjskim pristupom. Primjerice, pomoću Azure CLI možete pokrenuti:

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

Ovo stvara javno dostupan Container App s omogućеним HTTPS-om (Azure izdaje besplatni TLS certifikat za zadani `*.azurecontainerapps.io` domen) ([Prilagođeni nazivi domena i besplatni upravljani certifikati u Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Izlaz naredbe uključuje FQDN aplikacije (npr. `my-mcp-app.eastus.azurecontainerapps.io`), što postaje baza **issuer URL**-a. Osigurajte da je HTTP pristup omogućen (kao gore) kako bi APIM mogao dohvatiti aplikaciju. U testnom/razvojnog okruženju, koristite opciju `--ingress external` (ili povežite prilagođenu domenu s TLS-om prema [Microsoft dokumentaciji](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Prilagođeni nazivi domena i besplatni upravljani certifikati u Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Osjetljive postavke (kao što su OAuth klijentske tajne) pohranite u Container Apps secrets ili Azure Key Vault i mapirajte ih u kontejner kao varijable okoline.

## Konfiguriranje Spring Authorization Servera

U kodu svoje Spring Boot aplikacije uključite Spring Authorization Server i Resource Server startere. Konfigurirajte `RegisteredClient` (za `client_credentials` grant u razvoju/testiranju) i JWT izvor ključeva. Na primjer, u `application.properties` možete postaviti:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Omogućite Authorization Server i Resource Server definiranjem sigurnosnog filter lanca. Na primjer:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Omogući krajnje točke Poslužitelja za autorizaciju
            .apply(authzServer.and())
            // Omogući Poslužitelja resursa (provjeri JWT na dolaznim zahtjevima)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Onemogući CSRF (MCP poslužitelj nije baziran na pregledniku)
            .csrf(csrf -> csrf.disable())
            // Dozvoli CORS za klijentske alate za demonstraciju
            .cors(withDefaults());
        return http.build();
    }

    // Definiraj klijenta u memoriji (RegisteredClient) i JWK izvor:
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
        // Generiraj RSA ključ (za razvoj/test, generiraj iznova pri pokretanju)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ova konfiguracija će izložiti zadane OAuth2 krajnje točke: `/oauth2/token` za tokene i `/oauth2/jwks` za JSON Web Key Set. (Po zadanim postavkama Spring-ov `AuthorizationServerSettings` mapira `/oauth2/token` i `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server će izdavati JWT pristupne tokene potpisane RSA ključem iznad i objaviti svoj javni ključ na `https://<your-app>:/oauth2/jwks`.

**Omogućite OpenID Connect otkrivanje:** Da bi APIM automatski preuzeo issuer i JWKS, omogućite OIDC provider konfiguracijsku krajnju točku dodavanjem `.oidc(Customizer.withDefaults())` u vašu sigurnosnu konfiguraciju ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Na primjer:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– omogućuje /.well-known/openid-configuration
```

Ovo izlaže `/.well-known/openid-configuration`, što APIM može koristiti za metapodatke. Na kraju, možda ćete htjeti prilagoditi JWT **audience** claim tako da APIM-ov `<audiences>` prolaz bude uspješan. Na primjer, dodajte token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Postavite prilagođenu publiku (npr. ID klijenta ili API identifikator)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ovo osigurava da tokeni nose `"aud": ["mcp-client"]`, što odgovara ID-u klijenta ili očekivanom scopeu u APIM-u.

## Izlaganje Token i JWKS krajnjih točaka

Nakon postavljanja, **issuer URL** vaše aplikacije bit će `https://<app-fqdn>`, npr. `https://my-mcp-app.eastus.azurecontainerapps.io`. Njene OAuth2 krajnje točke su:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – klijenti ovdje dobivaju tokene (client_credentials tok).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – vraća JWK set (koji APIM koristi za dohvat ključeva za potpisivanje).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC otkriveni JSON (sadrži `issuer`, `token_endpoint`, `jwks_uri`, itd.).

APIM će koristiti **OpenID konfiguracijski URL** s kojeg otkriva `jwks_uri`. Na primjer, ako je FQDN vaše Container App `my-mcp-app.eastus.azurecontainerapps.io`, APIM-ov `<openid-config url="...">` treba koristiti `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Po zadanim postavkama Spring postavlja `issuer` u tim metapodacima na isti osnovni URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguriranje Azure API Managementa (`validate-jwt`)

U Azure APIM dodajte inbound politiku koja koristi `<validate-jwt>` politiku za provjeru dolaznih JWT-ova protiv vašeg Spring Authorization Servera. Za jednostavnu konfiguraciju, možete koristiti OpenID Connect URL za metapodatke. Primjer dijela politike:

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

Ova politika kaže APIM-u da dohvaća OpenID konfiguraciju iz Spring Auth Servera, preuzima njegov JWKS i provjerava je li svaki token potpisan pouzdanim ključem i ima li ispravan audience. (Ako izostavite `<issuers>`, APIM će automatski koristiti `issuer` claim iz metapodataka.) `<audience>` treba odgovarati ID-u vašeg klijenta ili identifikatoru API resursa u tokenu (u gornjem primjeru postavljeno na `"mcp-client"`). Ovo je u skladu s Microsoftovom dokumentacijom o korištenju `validate-jwt` s `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Nakon provjere, APIM će proslijediti zahtjev (uključujući originalni zaglavlje `Authorization`) backendu. Budući da je Spring aplikacija također resursni server, ponovno će provjeriti token, ali APIM je već osigurao njegovu valjanost. (Za razvoj možete se oslanjati na APIM provjeru i onemogućiti dodatne provjere u aplikaciji ako želite, ali sigurnije je imati oba.)

## Primjeri postavki

| Postavka          | Primjer vrijednosti                                              | Bilješke                                    |
|-------------------|-----------------------------------------------------------------|----------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`               | URL vaše Container aplikacije (osnovni URI) |
| **Token endpoint**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`  | Zadana Spring token krajnja točka ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`   | Zadana JWK Set krajnja točka ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC otkrivajući dokument (automatski generiran) |
| **APIM audience** | `mcp-client`                                                    | OAuth klijentski ID ili naziv API resursa    |
| **APIM policy**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` koristi ovaj URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Česte zamke

- **HTTPS/TLS:** APIM gateway zahtijeva da OpenID/JWKS krajnja točka bude HTTPS s valjanim certifikatom. Po zadanim postavkama, Azure Container Apps osigurava pouzdani TLS certifikat za Azure-om upravljanu domenu ([Prilagođeni nazivi domena i besplatni upravljani certifikati u Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ako koristite prilagođenu domenu, obvezno povežite certifikat (možete koristiti Azure-ovu besplatnu upravljanu značajku certifikata) ([Prilagođeni nazivi domena i besplatni upravljani certifikati u Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ako APIM ne može vjerovati certifikatu krajnje točke, `<validate-jwt>` neće moći dohvatiti metapodatke.

- **Dostupnost krajnjih točaka:** Provjerite da li su krajnje točke Spring aplikacije dostupne s APIM-a. Najjednostavnije je koristiti `--ingress external` (ili omogućiti ingress u portalu). Ako ste odabrali interno ili vNet povezano okruženje, APIM (koji je po zadanim postavkama javan) možda neće moći pristupiti osim ako nije u istom VNetu. U testnom okruženju preferirajte javni pristup da APIM može pozivati `.well-known` i `/jwks` URL-e.

- **Omogućeno OpenID otkrivanje:** Po zadanim postavkama, Spring Authorization Server **ne izlaže** `/.well-known/openid-configuration` osim ako OIDC nije omogućeno. Obavezno uključite `.oidc(Customizer.withDefaults())` u svoju sigurnosnu konfiguraciju (vidi gore) da bi konfiguracijska krajnja točka davatelja bila aktivna ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Inače će APIM-ov `<openid-config>` poziv vratiti 404.

- **Audience claim:** Zadano ponašanje Spring-a je postaviti `aud` claim na ID klijenta. Ako APIM-ova `<audience>` provjera ne prođe, možda ćete trebati prilagoditi token (kao što je gore prikazano) ili promijeniti APIM politiku. Osigurajte da audience u vašem JWT-u odgovara onome što konfigurirate u `<audience>`.

- **Parsiranje JSON metapodataka:** OpenID konfiguracijski JSON mora biti valjan. Zadana Spring konfiguracija emitira standardni OIDC metapodatkovni dokument. Provjerite da sadrži ispravan `issuer` i `jwks_uri`. Ako hvatate Spring iza proxyja ili konfigurirate rutu baziranu na putu, provjerite URL-ove u ovim metapodacima. APIM će koristiti te vrijednosti takve kakve jesu.

- **Redoslijed politika:** U APIM politici stavite `<validate-jwt>` **prije** bilo kakvog usmjeravanja prema backendu. Inače pozivi mogu doseći vašu aplikaciju bez valjanog tokena. Također osigurajte da `<validate-jwt>` stoji neposredno unutar `<inbound>` (ne ugniježđeno unutar drugog uvjeta) kako bi ga APIM primijenio.

Slijedeći gore navedene korake, možete pokrenuti svoj Spring AI MCP server u Azure Container Apps i imati Azure API Management koji provjerava dolazne OAuth2 JWT-ove s minimalnom politikom. Ključne točke su: javno izložite Spring Auth krajnje točke s TLS-om, omogućite OIDC otkrivanje i usmjerite APIM-ov `validate-jwt` prema OpenID config URL-u (da automatski može dohvatiti JWKS). Ova konfiguracija je prikladna za razvojno/testno okruženje; za produkciju razmotrite pravilno upravljanje tajnama, trajanje tokena i rotaciju ključeva u JWKS prema potrebi.


**Reference:** Pogledajte dokumentaciju Spring Authorization Servera za zadane krajnje točke ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) i OIDC konfiguraciju ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); pogledajte Microsoft APIM dokumentaciju za primjere `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); i Azure Container Apps dokumentaciju za implementaciju i certifikate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->