# Diegimas Spring AI MCP programos Azure Container Apps

([Spring AI MCP serverių apsauga naudojant OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Paveikslas: Spring AI MCP serveris apsaugotas Spring Authorization Server. Serveris išduoda prieigos žetonus klientams ir tikrina juos gaunamuose užklausose (šaltinis: Spring tinklaraštis) ([Spring AI MCP serverių apsauga naudojant OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Norėdami diegti Spring MCP serverį, sukurkite jį kaip konteinerį ir naudokite Azure Container Apps su išoriniu įėjimu. Pavyzdžiui, naudodami Azure CLI galite paleisti:

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

Tai sukuria viešai prieinamą konteinerio programą su įjungtu HTTPS (Azure išduoda nemokamą TLS sertifikatą numatytajam `*.azurecontainerapps.io` domenui ([Pasirinktiniai domenų vardai ir nemokami valdomi sertifikatai Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Komandos rezultatuose pateikiamas programos FQDN (pvz., `my-mcp-app.eastus.azurecontainerapps.io`), kuris tampa **issuer URL** pagrindu. Įsitikinkite, kad HTTP įėjimas yra įjungtas (kaip aukščiau), kad APIM galėtų pasiekti programą. Testavimo/kūrimo aplinkoje naudokite `--ingress external` parinktį (arba priskirkite pasirinktinį domeną su TLS pagal [Microsoft dokumentaciją](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Pasirinktiniai domenų vardai ir nemokami valdomi sertifikatai Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Bet kokias jautrias savybes (pvz., OAuth klientų slaptažodžius) saugokite Container Apps paslaptyse arba Azure Key Vault ir susiekite jas su konteineriu kaip aplinkos kintamuosius.

## Spring Authorization Server konfigūravimas

Savo Spring Boot programos kode įtraukite Spring Authorization Server ir Resource Server starterius. Konfigūruokite `RegisteredClient` (dev/test aplinkoje naudojant `client_credentials` grant) ir JWT raktų šaltinį. Pavyzdžiui, `application.properties` galite nustatyti:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Įjunkite Authorization Server ir Resource Server apibrėždami saugumo filtrų grandinę. Pavyzdžiui:

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

Ši konfigūracija atskleis numatytuosius OAuth2 galinius taškus: `/oauth2/token` žetonams ir `/oauth2/jwks` JSON Web Key Set. (Pagal numatytuosius nustatymus Spring `AuthorizationServerSettings` susieja `/oauth2/token` ir `/oauth2/jwks` ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serveris išduos JWT prieigos žetonus, pasirašytus aukščiau nurodytu RSA raktu, ir paskelbs savo viešąjį raktą adresu `https://<your-app>:/oauth2/jwks`.

**Įjunkite OpenID Connect atradimą:** Kad APIM automatiškai gautų issuer ir JWKS, įjunkite OIDC teikėjo konfigūracijos galinį tašką pridėdami `.oidc(Customizer.withDefaults())` savo saugumo konfigūracijoje ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Pavyzdžiui:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Tai atskleis `/.well-known/openid-configuration`, kurį APIM gali naudoti metaduomenims. Galiausiai, galbūt norėsite pritaikyti JWT **audience** claim, kad APIM `<audiences>` patikrinimas būtų sėkmingas. Pavyzdžiui, pridėkite žetono pritaikymo funkciją:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tai užtikrina, kad žetonai turėtų `"aud": ["mcp-client"]`, atitinkantį klientų ID arba scope, kurį tikisi APIM.

## Žetonų ir JWKS galinių taškų atskleidimas

Po diegimo jūsų programos **issuer URL** bus `https://<app-fqdn>`, pvz., `https://my-mcp-app.eastus.azurecontainerapps.io`. Jos OAuth2 galiniai taškai yra:

- **Žetono galinis taškas:** `https://<app-fqdn>/oauth2/token` – klientai čia gauna žetonus (client_credentials flow).
- **JWKS galinis taškas:** `https://<app-fqdn>/oauth2/jwks` – grąžina JWK rinkinį (naudojamas APIM pasirašymo raktams gauti).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC atradimo JSON (yra `issuer`, `token_endpoint`, `jwks_uri` ir kt.).

APIM nukreips į **OpenID konfigūracijos URL**, iš kurio jis atranda `jwks_uri`. Pavyzdžiui, jei jūsų Container App FQDN yra `my-mcp-app.eastus.azurecontainerapps.io`, tada APIM `<openid-config url="...">` turėtų naudoti `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Pagal numatytuosius nustatymus Spring nustatys `issuer` šiuose metaduomenyse kaip tą patį bazinį URL ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management konfigūravimas (`validate-jwt`)

Azure APIM pridėkite įeinančią politiką, kuri naudoja `<validate-jwt>` politiką, kad patikrintų gaunamus JWT pagal jūsų Spring Authorization Server. Paprasto nustatymo atveju galite naudoti OpenID Connect metaduomenų URL. Politikos fragmento pavyzdys:

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

Ši politika nurodo APIM gauti OpenID konfigūraciją iš Spring Auth Server, gauti jo JWKS ir patikrinti, kad kiekvienas žetonas būtų pasirašytas patikimu raktu ir turėtų tinkamą audience. (Jei praleisite `<issuers>`, APIM automatiškai naudos `issuer` claim iš metaduomenų.) `<audience>` turėtų atitikti jūsų klientų ID arba API resurso identifikatorių žetone (aukščiau pateiktame pavyzdyje mes nustatėme `"mcp-client"`). Tai atitinka Microsoft dokumentaciją apie `validate-jwt` naudojimą su `<openid-config>` ([Azure API Management politikos nuoroda - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po patikrinimo APIM persiųs užklausą (įskaitant originalų `Authorization` antraštę) į backend. Kadangi Spring programa taip pat yra resurso serveris, ji dar kartą patikrins žetoną, tačiau APIM jau užtikrino jo galiojimą. (Kūrimo metu galite pasikliauti APIM patikrinimu ir išjungti papildomus patikrinimus programoje, jei norite, tačiau saugiau palikti abu.)

## Pavyzdiniai nustatymai

| Nustatymas         | Pavyzdinė vertė                                                     | Pastabos                                   |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Jūsų Container App URL (bazinis URI)       |
| **Žetono galinis taškas** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Numatytoji Spring žetono galinio taško vieta ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS galinis taškas**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Numatytoji JWK Set galinio taško vieta ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC atradimo dokumentas (automatiškai sugeneruotas)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth klientų ID arba API resurso pavadinimas |
| **APIM politika**  | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` naudoja šį URL ([Azure API Management politikos nuoroda - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Dažnos klaidos

- **HTTPS/TLS:** APIM vartai reikalauja, kad OpenID/JWKS galinis taškas būtų HTTPS su galiojančiu sertifikatu. Pagal numatytuosius nustatymus Azure Container Apps pateikia patikimą TLS sertifikatą Azure valdomam domenui ([Pasirinktiniai domenų vardai ir nemokami valdomi sertifikatai Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jei naudojate pasirinktinį domeną, būtinai priskirkite sertifikatą (galite naudoti Azure nemokamą valdomą sertifikatų funkciją) ([Pasirinktiniai domenų vardai ir nemokami valdomi sertifikatai Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jei APIM negali pasitikėti galinio taško sertifikatu, `<validate-jwt>` nepavyks gauti metaduomenų.

- **Galinių taškų prieinamumas:** Įsitikinkite, kad Spring programos galiniai taškai yra pasiekiami iš APIM. Naudojant `--ingress external` (arba įjungiant įėjimą portale) yra paprasčiausia. Jei pasirinkote vidinę arba vNet susietą aplinką, APIM (pagal numatytuosius nustatymus viešas) gali nepasiekti jos, nebent būtų patalpintas tame pačiame VNet. Testavimo aplinkoje geriau naudoti viešą įėjimą, kad APIM galėtų pasiekti `.well-known` ir `/jwks` URL.

- **OpenID atradimas įjungtas:** Pagal numatytuosius nustatymus Spring Authorization Server **neatskleidžia** `/.well-known/openid-configuration`, nebent OIDC yra įjungtas. Įsitikinkite, kad įtraukėte `.oidc(Customizer.withDefaults())` savo saugumo konfigūracijoje (žr. aukščiau), kad teikėjo konfigūracijos galinis taškas būtų aktyvus ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Priešingu atveju APIM `<openid-config>` užklausa grąžins 404.

- **Audience claim:** Spring numatytasis elgesys yra nustatyti `aud` claim kaip klientų ID. Jei APIM `<audience>` patikrinimas nepavyksta, gali tekti pritaikyti žetoną (kaip parodyta aukščiau) arba koreguoti APIM politiką. Įsitikinkite, kad audience jūsų JWT atitinka tai, ką konfigūruojate `<audience>`.

- **JSON metaduomenų analizė:** OpenID konfigūracijos JSON turi būti galiojantis. Spring numatytoji konfigūracija išduos standartinį OIDC metaduomenų dokumentą. Patikrinkite, ar jame yra teisingas `issuer` ir `jwks_uri`. Jei Spring yra talpinamas už proxy arba maršruto pagrindu, dar kartą patikrinkite URL šiuose metaduomenyse. APIM naudos šias vertes kaip yra.

- **Politikos tvarka:** APIM politikoje `<validate-jwt>` turi būti **prieš** bet kokį maršrutizavimą į backend. Priešingu atveju užklausos gali pasiekti jūsų programą be galiojančio žetono. Taip pat įsitikinkite, kad `<validate-jwt>` yra iškart po `<inbound>` (ne įdėta į kitą sąlygą), kad APIM ją taikytų.

Laikydamiesi aukščiau pateiktų žingsnių, galite paleisti savo Spring AI MCP serverį Azure Container Apps ir leisti Azure API Management patikrinti gaunamus OAuth2 JWT su minimalia politika. Pagrindiniai punktai yra: viešai atskleisti Spring Auth galinius taškus su TLS, įjungti OIDC atradimą ir nukreipti APIM `validate-jwt` į OpenID konfigūracijos URL (kad jis galėtų automatiškai gauti JWKS). Ši konfigūracija tinka kūrimo/testavimo aplinkai; gamybai apsvarstykite tinkamą paslapčių valdymą, žetonų galiojimo laiką ir raktų rotaciją JWKS, jei reikia.
**Nuorodos:** Žr. Spring Authorization Server dokumentaciją dėl numatytųjų galinių taškų ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ir OIDC konfigūracijos ([Konfigūracijos modelis :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); žr. Microsoft APIM dokumentaciją dėl `validate-jwt` pavyzdžių ([Azure API Management politikos nuoroda - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ir Azure Container Apps dokumentaciją dėl diegimo ir sertifikatų ([Diegti Java Spring Boot programas į Azure Container Apps - Java ant Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Pasirinktiniai domenų vardai ir nemokami valdomi sertifikatai Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.