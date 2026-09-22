# Spring AI MCP programėlės diegimas į Azure Container Apps

> [!WARNING]
> Šis sujungtas autorizacijos/išteklių serveris skirtas mokymuisi ir
> vystymo/testavimo naudojimui. Produkcijos sistemos turėtų naudoti specialų tapatybės tiekėją,
> nuolatinius pasirašymo raktus ir kredencialus saugomus valdomame slaptajame saugykloje.

 ([Spring AI MCP serverių apsauga su OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Paveikslas: Spring AI MCP serveris apsaugotas su Spring Authorization Server. Serveris išduoda prieigos žetonus klientams ir tikrina juos gaunamuose užklausose (šaltinis: Spring tinklaraštis) ([Spring AI MCP serverių apsauga su OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Norint įdiegti Spring MCP serverį, sukurkite konteinerį ir naudokite Azure Container Apps su išoriniu prieigos tašku. Pavyzdžiui, naudojant Azure CLI, galite vykdyti:

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

Tai sukuria viešai prieinamą Container App su įjungtu HTTPS (Azure suteikia nemokamą TLS sertifikatą standartiniam `*.azurecontainerapps.io` domenui ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Komandos išvestyje yra programėlės FQDN (pvz., `my-mcp-app.eastus.azurecontainerapps.io`), kuris tampa **išdavėjo URL** pagrindu. Užtikrinkite, kad HTTP prieiga būtų įjungta (kaip aukščiau), kad APIM galėtų pasiekti programėlę. Testavimo/vystymo aplinkoje naudokite parinktį `--ingress external` (arba susiekite pasirinktą domeną su TLS pagal [Microsoft dokumentaciją](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Bet kokias jautrias savybes (pvz., OAuth kliento slaptus raktus) laikykite Container Apps slaptuose duomenyse arba Azure Key Vault ir susiekite jas su konteineriu kaip aplinkos kintamuosius.

## Spring Authorization Server konfigūravimas

Jūsų Spring Boot programėlės kode įtraukite Spring Authorization Server ir Resource Server pradmenis. Sukonfigūruokite `RegisteredClient` (dev/test aplinkoje naudojant `client_credentials` leidimą) ir JWT rakto šaltinį. Pavyzdžiui, `application.properties` faile galite nustatyti:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
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
            // Įjunkite autorizacijos serverio galinius taškus
            .apply(authzServer.and())
            // Įjunkite išteklių serverį (patikrinkite JWT gaunamuose užklausimuose)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Išjunkite CSRF (MCP serveris nėra naršyklės pagrindu)
            .csrf(csrf -> csrf.disable())
            // Leisti CORS klientų demonstravimo įrankiams
            .cors(withDefaults());
        return http.build();
    }

    // Apibrėžkite atmintyje esančią klientą (RegisteredClient) ir JWK šaltinį:
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
        // Sugeneruokite RSA raktą (kūrimui/testavimui, generuokite naują paleidžiant)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Šis nustatymas atvers numatytuosius OAuth2 galinius taškus: `/oauth2/token` žetonams ir `/oauth2/jwks` JSON Web Key rinkiniui. (Pagal numatytuosius Spring `AuthorizationServerSettings` susieja `/oauth2/token` ir `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serveris išduos JWT prieigos žetonus, pasirašytus aukščiau nurodytu RSA raktu, ir paskelbs savo viešąjį raktą adresu `https://<your-app>:/oauth2/jwks`.

**Įjungti OpenID Connect atradimą:** Kad APIM galėtų automatiškai gauti išdavėjo informaciją ir JWKS, įjunkite OIDC teikėjo konfigūracijos galinį tašką pridėdami `.oidc(Customizer.withDefaults())` savo saugumo konfigūracijoje ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Pavyzdžiui:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– įgalina /.well-known/openid-configuration
```

Tai atveria `/.well-known/openid-configuration`, kurį APIM gali naudoti metaduomenims. Galiausiai galite norėti pritaikyti JWT **audience** lauką, kad APIM `<audiences>` patikra praeitų. Pavyzdžiui, pridėkite žetono pritaikymo funkciją:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Nustatykite pasirinktą auditoriją (pvz., kliento ID arba API identifikatorių)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tai užtikrina, kad žetonai turės `"aud": ["mcp-client"]`, atitinkantį kliento ID ar APIM tikėtą sritį.

## Žetonų ir JWKS galinių taškų atvėrimas

Po diegimo jūsų programėlės **išdavėjo URL** bus `https://<app-fqdn>`, pvz., `https://my-mcp-app.eastus.azurecontainerapps.io`. Jo OAuth2 galiniai taškai yra:

- **Žetono galinis taškas:** `https://<app-fqdn>/oauth2/token` – čia klientai gauna žetonus (client_credentials srautas).
- **JWKS galinis taškas:** `https://<app-fqdn>/oauth2/jwks` – grąžina JWK rinkinį (naudojamas APIM pasirašymo raktams gauti).
- **OpenID Konfigūracija:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC atradimo JSON (kuriame yra `issuer`, `token_endpoint`, `jwks_uri` ir kt.).

APIM nukreips į **OpenID konfigūracijos URL**, iš kurio suras `jwks_uri`. Pavyzdžiui, jei jūsų Container App FQDN yra `my-mcp-app.eastus.azurecontainerapps.io`, tada APIM `<openid-config url="...">` turėtų naudoti `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Pagal numatytuosius nustatymus Spring į metadata bus nustatytas tas pats pagrindinis URL kaip `issuer` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) konfigūravimas

Azure APIM pridėkite įeinančios užklausos politiką, kuri naudoja `<validate-jwt>` politiką tikrinti gaunamus JWT pagal jūsų Spring Authorization Server. Paprastam nustatymui galite naudoti OpenID Connect metaduomenų URL. Pavyzdinis politikos fragmentas:

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

Ši politika liepia APIM gauti OpenID konfigūraciją iš Spring Auth Server, surasti jo JWKS ir patikrinti, ar kiekvienas žetonas pasirašytas patikimu raktu ir turi teisingą audience. (Jei nenurodote `<issuers>`, APIM automatiškai naudos `issuer` reikšmę iš metaduomenų.) `<audience>` turi atitikti jūsų kliento ID arba API resurso identifikatorių žetone (aukščiau pateiktame pavyzdyje nustatėme `"mcp-client"`). Tai atitinka Microsoft dokumentaciją apie `validate-jwt` naudojimą su `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po validacijos APIM persiųs užklausą (įskaitant originalų `Authorization` antraštę) į backendą. Kadangi Spring programėlė taip pat yra išteklių serveris, ji dar kartą patikrins žetoną, tačiau APIM jau užtikrino jo galiojimą. (Vystymo metu galite pasikliauti APIM patikra ir, jei norite, išjungti papildomas patikrintas programėlėje, bet saugiau palikti abi.)

## Pavyzdinės nuostatos

| Nuostata          | Pavyzdinė reikšmė                                                  | Pastabos                                  |
|-------------------|---------------------------------------------------------------------|-------------------------------------------|
| **Išdavėjas**     | `https://my-mcp-app.eastus.azurecontainerapps.io`                   | Jūsų Container App URL (pagrindinis URI)  |
| **Žetono galinis taškas** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Spring numatytasis žetono galinis taškas ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS galinis taškas** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`       | Numatytoji JWK rinkinio vieta ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID konfigūracija** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC atradimo dokumentas (automatiškai sugeneruotas)    |
| **APIM auditorija** | `mcp-client`                                                       | OAuth kliento ID arba API resurso pavadinimas              |
| **APIM politika** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` naudoja šį URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Dažni klaidų šaltiniai

- **HTTPS/TLS:** APIM vartų reikalavimas – OpenID/JWKS galiniai taškai turi būti HTTPS su galiojančiu sertifikatu. Pagal numatytuosius nustatymus Azure Container Apps suteikia patikimą TLS sertifikatą Azure valdomam domenui ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jei naudojate pasirinktą domeną, būtinai susiekite jį su sertifikatu (galite naudoti Azure nemokamą valdomą sertifikatų funkciją) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jei APIM negali pasitikėti galinio taško sertifikatu, `<validate-jwt>` nepavyks gauti metaduomenų.

- **Galiniai taškai pasiekiami:** Įsitikinkite, kad Spring programėlės galiniai taškai yra pasiekiami iš APIM. Naudojant parinktį `--ingress external` (arba įjungiant prieigą portale) yra paprasčiausia. Jei pasirinkote vidinę arba VNet ribojamą aplinką, APIM (pagal numatytuosius nustatymus viešas) jos gali nepasiekti, nebent yra tame pačiame VNet tinkle. Testavimo aplinkoje geriau naudoti viešą prieigą, kad APIM galėtų pasiekti `.well-known` ir `/jwks` URL.

- **OpenID atradimas įjungtas:** Pagal numatytuosius nustatymus Spring Authorization Server **neišduoda** `/.well-known/openid-configuration`, jei OIDC nėra įjungtas. Įsitikinkite, kad įtraukėte `.oidc(Customizer.withDefaults())` savo saugumo konfigūracijoje (žr. aukščiau), kad teikėjo konfigūracijos galinis taškas veiktų ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Priešingu atveju APIM `<openid-config>` kvietimas grąžins 404.

- **Audience teiginys:** Pagal nutylėjimą Spring nustato `aud` reikšmę kliento ID. Jei APIM `<audience>` patikra nepraeina, gali tekti pritaikyti žetoną (kaip parodyta aukščiau) arba keisti APIM politiką. Įsitikinkite, kad auditorija jūsų JWT atitinka tą, kurią nustatote `<audience>`.

- **JSON metaduomenų analizė:** OpenID konfigūracijos JSON turi būti galiojantis. Numatytoji Spring konfigūracija generuos standartinį OIDC metaduomenų dokumentą. Patikrinkite, ar jame yra teisingi `issuer` ir `jwks_uri`. Jei hostinate Spring už proxy ar naudodami kelių maršrutų kelią, kruopščiai patikrinkite URL šiame metaduomenų faile. APIM jį naudos tokiu pačiu pavidalu.

- **Politikos tvarka:** APIM politikoje `<validate-jwt>` turi būti dedamas **prieš** bet kokį maršrutavimą į backendą. Kitu atveju užklausos gali pasiekti jūsų programėlę be galiojančio žetono. Taip pat užtikrinkite, kad `<validate-jwt>` būtų tiesiogiai po `<inbound>` (nėra įdėtas į kitą sąlygą), kad APIM ją taikytų.

Laikantis aukščiau aprašytų žingsnių, galite paleisti Spring AI MCP serverį Azure Container Apps ir leisti Azure API Management tikrinti gaunamus OAuth2 JWT su minimaliomis politikų sąnaudomis. Svarbiausi dalykai: viešai atverti Spring Auth galinius taškus su TLS, įjungti OIDC atradimą ir nukreipti APIM `validate-jwt` į OpenID konfigūracijos URL (kad automatiškai gautų JWKS). Šis nustatymas tinkamas dev/test aplinkai; gamybai rekomenduojama tinkamai valdyti slaptus duomenis, žetonų galiojimo laikus ir raktų rotaciją JWKS rinkinyje pagal poreikį.


**Nuorodos:** Žr. Spring Authorization Server dokumentaciją dėl numatytųjų galinių taškų ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ir OIDC konfigūracijos ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); žr. Microsoft APIM dokumentaciją dėl `validate-jwt` pavyzdžių ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ir Azure Container Apps dokumentaciją dėl diegimo ir sertifikatų ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->