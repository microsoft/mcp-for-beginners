# Kuweka Spring AI MCP App kwenye Azure Container Apps

 ([Kuhakikisha seva za Spring AI MCP kwa OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Mchoro: Seva ya Spring AI MCP iliyo salama kwa kutumia Spring Authorization Server. Seva hutoa tokeni za ufikiaji kwa wateja na kuzikagua kwenye maombi yanayoingia (chanzo: Spring blog) ([Kuhakikisha seva za Spring AI MCP kwa OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Ili kuweka seva ya Spring MCP, jenge kama kontena na tumia Azure Container Apps na ingress ya nje. Kwa mfano, kwa kutumia Azure CLI unaweza kuendesha:

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

Hii inaunda Container App inayopatikana hadharani na HTTPS imewezeshwa (Azure hutoa cheti cha bure cha TLS kwa kikoa cha chaguo `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Matokeo ya amri yanajumuisha FQDN ya app (mfano `my-mcp-app.eastus.azurecontainerapps.io`), ambayo hutumika kama msingi wa **issuer URL**. Hakikisha ingress ya HTTP imewezeshwa (kama ilivyo hapo juu) ili APIM iweze kufikia app. Katika mazingira ya majaribio/maendeleo, tumia chaguo `--ingress external` (au weka kikoa maalum na TLS kulingana na [nyaraka za Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Hifadhi mali nyeti yoyote (kama siri za mteja wa OAuth) katika siri za Container Apps au Azure Key Vault, na ziweke ndani ya kontena kama mabadiliko ya mazingira.

## Kusanidi Spring Authorization Server

Katika msimbo wa app yako ya Spring Boot, jumuisha Spring Authorization Server na Resource Server starters. Sanidi `RegisteredClient` (kwa ajili ya ruhusa ya `client_credentials` katika mazingira ya majaribio/maendeleo) na chanzo cha funguo za JWT. Kwa mfano, katika `application.properties` unaweza kuweka:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Wezesha Authorization Server na Resource Server kwa kufafanua mnyororo wa kichujio cha usalama. Kwa mfano:

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

Mpangilio huu utaonyesha vituo vya msingi vya OAuth2: `/oauth2/token` kwa tokeni na `/oauth2/jwks` kwa Seti ya Funguo za JSON Web. (Kwa kawaida Spring `AuthorizationServerSettings` huoanisha `/oauth2/token` na `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Seva itatoa tokeni za ufikiaji za JWT zilizosainiwa na funguo za RSA zilizo hapo juu, na kuchapisha funguo zake za umma kwenye `https://<your-app>:/oauth2/jwks`.

**Wezesha ugunduzi wa OpenID Connect:** Ili APIM ipate moja kwa moja issuer na JWKS, wezesha kituo cha usanidi wa mtoa huduma wa OIDC kwa kuongeza `.oidc(Customizer.withDefaults())` katika usanidi wako wa usalama ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Kwa mfano:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Hii itaonyesha `/.well-known/openid-configuration`, ambayo APIM inaweza kutumia kwa metadata. Mwishowe, unaweza kutaka kubinafsisha dai la **audience** la JWT ili ukaguzi wa `<audiences>` wa APIM upite. Kwa mfano, ongeza mabadiliko ya tokeni:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Hii inahakikisha tokeni zina `"aud": ["mcp-client"]`, inayolingana na ID ya mteja au upeo unaotarajiwa na APIM.

## Kuweka Vituo vya Token na JWKS wazi

Baada ya kuweka, **issuer URL** ya app yako itakuwa `https://<app-fqdn>`, mfano `https://my-mcp-app.eastus.azurecontainerapps.io`. Vituo vyake vya OAuth2 ni:

- **Kituo cha Token:** `https://<app-fqdn>/oauth2/token` – wateja hupata tokeni hapa (mtiririko wa client_credentials).
- **Kituo cha JWKS:** `https://<app-fqdn>/oauth2/jwks` – hurudisha seti ya JWK (inayotumika na APIM kupata funguo za kusaini).
- **Usanidi wa OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON ya ugunduzi wa OIDC (ina `issuer`, `token_endpoint`, `jwks_uri`, n.k.).

APIM itatumia **URL ya usanidi wa OpenID**, ambapo itagundua `jwks_uri`. Kwa mfano, ikiwa FQDN ya Container App ni `my-mcp-app.eastus.azurecontainerapps.io`, basi `<openid-config url="...">` ya APIM itumie `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Kwa kawaida Spring itaweka `issuer` katika metadata hiyo kwa URL hiyo hiyo ya msingi ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Kusanidi Azure API Management (`validate-jwt`)

Katika Azure APIM, ongeza sera ya kuingia inayotumia sera ya `<validate-jwt>` kukagua JWT zinazokuja dhidi ya Spring Authorization Server yako. Kwa usanidi rahisi, unaweza kutumia URL ya metadata ya OpenID Connect. Mfano wa kipande cha sera:

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

Sera hii inaeleza APIM ipate usanidi wa OpenID kutoka Spring Auth Server, ipate JWKS yake, na ikague kuwa kila tokeni imesainiwa na funguo inayotegemewa na ina audience sahihi. (Kama utaacha `<issuers>`, APIM itatumia dai la `issuer` kutoka metadata moja kwa moja.) `<audience>` inapaswa kuendana na ID ya mteja wako au kitambulisho cha rasilimali ya API katika tokeni (kama ilivyo kwenye mfano hapo juu, tumeiweka kuwa `"mcp-client"`). Hii ni sawa na nyaraka za Microsoft kuhusu kutumia `validate-jwt` na `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Baada ya ukaguzi, APIM itapeleka ombi (ikiwa ni pamoja na kichwa cha `Authorization` cha awali) kwa backend. Kwa kuwa app ya Spring pia ni seva ya rasilimali, itakagua tokeni tena, lakini APIM tayari imehakikisha uhalali wake. (Kwa maendeleo, unaweza kutegemea ukaguzi wa APIM na kuzima ukaguzi wa ziada katika app ikiwa unataka, lakini ni salama zaidi kuweka zote mbili.)

## Mipangilio ya Mfano

| Mpangilio          | Thamani ya Mfano                                                   | Maelezo                                   |
|--------------------|-------------------------------------------------------------------|-------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL ya Container App yako (URI ya msingi) |
| **Kituo cha Token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Kituo cha tokeni cha Spring (chaguo-msingi) ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **Kituo cha JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Kituo cha Seti ya JWK (chaguo-msingi) ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **Usanidi wa OpenID** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Hati ya ugunduzi wa OIDC (inayotengenezwa moja kwa moja) |
| **Audience ya APIM** | `mcp-client`                                                     | ID ya mteja wa OAuth au jina la rasilimali ya API |
| **Sera ya APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` hutumia URL hii ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Makosa Yanayojirudia Mara kwa Mara

- **HTTPS/TLS:** Lango la APIM linahitaji kituo cha OpenID/JWKS kiwe na HTTPS na cheti halali. Kwa kawaida, Azure Container Apps hutoa cheti cha TLS kinachotegemewa kwa kikoa kinachosimamiwa na Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ikiwa unatumia kikoa maalum, hakikisha umeambatanisha cheti (unaweza kutumia huduma ya cheti ya bure ya Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ikiwa APIM haiwezi kuamini cheti cha kituo, `<validate-jwt>` itashindwa kupata metadata.

- **Upatikanaji wa Vituo:** Hakikisha vituo vya app ya Spring vinaweza kufikiwa kutoka APIM. Kutumia `--ingress external` (au kuwezesha ingress kwenye portal) ni rahisi zaidi. Ikiwa umechagua mazingira ya ndani au yanayohusishwa na vNet, APIM (kwa kawaida ni ya umma) huenda isiweze kufikia isipokuwa ikiwa ipo katika vNet ile ile. Katika mazingira ya majaribio, tumia ingress ya umma ili APIM iweze kuita URL za `.well-known` na `/jwks`.

- **Ugunduzi wa OpenID Umewezeshwa:** Kwa kawaida, Spring Authorization Server **haitoi** `/.well-known/openid-configuration` isipokuwa OIDC iwe imewezeshwa. Hakikisha umejumuisha `.oidc(Customizer.withDefaults())` katika usanidi wako wa usalama (tazama hapo juu) ili kituo cha usanidi wa mtoa huduma kiwe hai ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Vinginevyo, wito wa `<openid-config>` wa APIM utarudisha 404.

- **Dai la Audience:** Tabia ya kawaida ya Spring ni kuweka dai la `aud` kwa ID ya mteja. Ikiwa ukaguzi wa `<audience>` wa APIM utashindwa, unaweza kuhitaji kubinafsisha tokeni (kama ilivyoonyeshwa hapo juu) au kurekebisha sera ya APIM. Hakikisha audience katika JWT yako inalingana na ile unayoainisha katika `<audience>`.

- **Uchambuzi wa Metadata ya JSON:** Metadata ya usanidi wa OpenID lazima iwe halali. Usanidi wa kawaida wa Spring utatengeneza hati ya kawaida ya metadata ya OIDC. Hakikisha ina `issuer` na `jwks_uri` sahihi. Ikiwa unahudumia Spring nyuma ya proxy au njia ya msingi, hakikisha URL hizi ni sahihi katika metadata hii. APIM itazitumia kama zilivyo.

- **Mpangilio wa Sera:** Katika sera ya APIM, weka `<validate-jwt>` **kabla** ya routing yoyote kwenda backend. Vinginevyo, maombi yanaweza kufika kwenye app bila tokeni halali. Pia hakikisha `<validate-jwt>` ipo moja kwa moja chini ya `<inbound>` (si ndani ya hali nyingine) ili APIM itumie sera hii.

Kwa kufuata hatua zilizo hapo juu, unaweza kuendesha seva yako ya Spring AI MCP katika Azure Container Apps na kuruhusu Azure API Management ikague JWT za OAuth2 zinazokuja kwa sera rahisi. Mambo muhimu ni: kufungua vituo vya Spring Auth kwa umma kwa TLS, kuwezesha ugunduzi wa OIDC, na kuelekeza `validate-jwt` ya APIM kwenye URL ya usanidi wa OpenID (ili ipate JWKS moja kwa moja). Mpangilio huu unafaa kwa mazingira ya majaribio/maendeleo; kwa uzalishaji, zingatia usimamizi sahihi wa siri, muda wa tokeni, na mzunguko wa funguo katika JWKS kama inavyohitajika.
**Marejeleo:** Angalia nyaraka za Spring Authorization Server kwa vituo vya chaguo-msingi ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) na usanidi wa OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); angalia nyaraka za Microsoft APIM kwa mifano ya `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); na nyaraka za Azure Container Apps kwa usambazaji na vyeti ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.