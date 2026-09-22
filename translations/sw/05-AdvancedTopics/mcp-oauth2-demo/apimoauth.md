# Kuweka Programu ya Spring AI MCP kwenye Azure Container Apps

> [!WARNING]
> Huu mchanganyiko wa seva ya idhini/rasilimali umetengenezwa kwa ajili ya kujifunza na
> matumizi ya maendeleo/mtihani. Mifumo ya uzalishaji inapaswa kutumia mtoa utambulisho wa kipekee,
> funguo za kusaini zinazodumu, na nyaraka zilizohifadhiwa katika duka la siri lililotawala.

 ([Kuhifadhi seva za Spring AI MCP kwa OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Mchoro: Seva ya Spring AI MCP iliyohifadhiwa na Spring Authorization Server. Seva hutuma tokeni za kupata kwa wateja na kuzikagua kwenye maombi yanayoingia (chanzo: Spring blog) ([Kuhifadhi seva za Spring AI MCP kwa OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Ili kuweka seva ya Spring MCP, jenga kama kontena na tumia Azure Container Apps na ingizo la nje. Kwa mfano, ukitumia Azure CLI unaweza kuendesha:

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

Hii hutengeneza Container App inayopatikana kwa umma na HTTPS imewezeshwa (Azure hutuma cheti cha bure cha TLS kwa kikoa cha chaguo `*.azurecontainerapps.io` ([Majina ya kikoa maalum na vyeti vinavyosimamiwa vya bure katika Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Matokeo ya amri yanajumuisha FQDN ya programu (kwa mfano `my-mcp-app.eastus.azurecontainerapps.io`), ambayo huwa msingi wa **URL ya mtumaji**. Hakikisha ingizo la HTTP limewezeshwa (kama ilivyo hapo juu) ili APIM iweze kufikia programu. Katika mpangilio wa majaribio/maendeleo, tumia chaguo `--ingress external` (au uambatane na kikoa maalum chenye TLS kulingana na [nyaraka za Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Majina ya kikoa maalum na vyeti vinavyosimamiwa vya bure katika Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Hifadhi mali yoyote nyeti (kama siri za mteja za OAuth) katika vifaa vya siri vya Container Apps au Azure Key Vault, na ziweke kwenye kontena kama vigezo vya mazingira.

## Kusanidi Spring Authorization Server

Katika msimbo wa programu yako ya Spring Boot, jumuisha watangulizi wa Spring Authorization Server na Resource Server. Sanidi `RegisteredClient` (kwa ajili ya ruzuku ya `client_credentials` katika maendeleo/mtihani) na chanzo cha funguo za JWT. Kwa mfano, katika `application.properties` unaweza kuweka:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Wezesha Authorization Server na Resource Server kwa kufafanua mnyororo wa filteri za usalama. Kwa mfano:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Wezesha sehemu za seva ya Uidhinishaji
            .apply(authzServer.and())
            // Wezesha seva ya Rasilimali (hakiki JWT kwenye maombi yanayoingia)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Zima CSRF (seva ya MCP si ya kivinjari)
            .csrf(csrf -> csrf.disable())
            // Ruhusu CORS kwa zana za majaribio za wateja
            .cors(withDefaults());
        return http.build();
    }

    // Eleza mteja wa kumbukumbu ya ndani (RegisteredClient) na chanzo cha JWK:
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
        // Tengeneza funguo za RSA (kwa maendelezo/majibu, tengeneza upya wakati wa kuanzisha)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Mpangilio huu utaonyesha vituo vya msingi vya OAuth2: `/oauth2/token` kwa tokeni na `/oauth2/jwks` kwa Seti ya Funguo za Wavulana wa JSON. (Kwa kawaida, Spring `AuthorizationServerSettings` huoanisha `/oauth2/token` na `/oauth2/jwks` ([Mfano wa Usanidi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Seva itatuma tokeni za upatikanaji za JWT zilizosainiwa na funguo za RSA zilizo hapo juu, na kuchapisha funguo zake za umma katika `https://<your-app>:/oauth2/jwks`.

**Wezesha kugundua OpenID Connect:** Ili APIM ipate mtumaji na JWKS moja kwa moja, wezesha kiungo cha usanidi cha mtoa huduma wa OIDC kwa kuongeza `.oidc(Customizer.withDefaults())` katika usanidi wako wa usalama ([Mfano wa Usanidi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Kwa mfano:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– inaruhusu /.well-known/openid-configuration
```

Hii itaonyesha `/.well-known/openid-configuration`, ambayo APIM inaweza kutumia kwa metadata. Mwishowe, unaweza kutaka kubinafsisha dai la hadhira ya JWT ili ukaguzi wa APIM wa `<audiences>` upite. Kwa mfano, ongeza mabadiliko ya tokeni:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Weka hadhira maalum (km. kitambulisho cha mteja au kitambulisho cha API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Hii inahakikisha tokeni zinapeleka `"aud": ["mcp-client"]`, inayolingana na ID ya mteja au upeo unaotarajiwa na APIM.

## Kutoa Vituo vya Tokeni na JWKS

Baada ya kuweka, **URL ya mtumaji** wa programu yako itakuwa `https://<app-fqdn>`, kwa mfano, `https://my-mcp-app.eastus.azurecontainerapps.io`. Vituo vyake vya OAuth2 ni:

- **Kituo cha Tokeni:** `https://<app-fqdn>/oauth2/token` – wateja hupata tokeni hapa (mtiririko wa client_credentials).
- **Kituo cha JWKS:** `https://<app-fqdn>/oauth2/jwks` – hurudisha seti ya JWK (inayotumika na APIM kupata funguo za kusaini).
- **Usanidi wa OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC kugundua JSON (ina `issuer`, `token_endpoint`, `jwks_uri`, nk).

APIM itakuwa ikielekeza kwenye **URL ya usanidi wa OpenID**, ambacho hutambua `jwks_uri`. Kwa mfano, ikiwa FQDN ya Container App yako ni `my-mcp-app.eastus.azurecontainerapps.io`, basi `<openid-config url="...">` ya APIM inapaswa kutumia `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Kwa kawaida Spring itaweka `issuer` katika metadata hiyo kwa URL ile ile ya msingi ([Mfano wa Usanidi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Kusanidi Azure API Management (`validate-jwt`)

Katika Azure APIM, ongeza sera ya kuingiza ambayo inatumia sera ya `<validate-jwt>` kuangalia JWT zinazokuja dhidi ya Spring Authorization Server yako. Kwa mpangilio rahisi, unaweza kutumia URL ya metadata ya OpenID Connect. Mfano wa kipande cha sera:

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

Sera hii inamwambia APIM kupata usanidi wa OpenID kutoka kwa Spring Auth Server, kupakua JWKS yake, na kuthibitisha kuwa kila tokeni imesainiwa na funguo inayotegemewa na ina hadhira sahihi. (Ikiwa utaacha `<issuers>`, APIM itatumia dai la `issuer` kutoka metadata moja kwa moja.) `<audience>` inapaswa kulingana na ID yako ya mteja au kitambulisho cha rasilimali ya API katika tokeni (kama ilivyo mfano hapo juu, tumeiweka kuwa `"mcp-client"`). Hii ni sawa na nyaraka za Microsoft kuhusu kutumia `validate-jwt` na `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Baada ya uthibitishaji, APIM itapeleka ombi (ikiwa ni pamoja na kichwa cha asili cha `Authorization`) kwa backend. Kwa kuwa programu ya Spring pia ni seva ya rasilimali, itahakikisha tena tokeni, lakini APIM tayari imehakikisha halali yake. (Kwa maendeleo, unaweza kutegemea ukaguzi wa APIM na kuzima ukaguzi zaidi katika programu ikiwa unataka, lakini ni salama zaidi kuweka zote mbili.)

## Mipangilio ya Mfano

| Mpangilio         | Thamani ya Mfano                                                 | Maelezo                                  |
|--------------------|------------------------------------------------------------------|------------------------------------------|
| **Mtumaji**       | `https://my-mcp-app.eastus.azurecontainerapps.io`               | URL ya Container App yako (URI ya msingi) |
| **Kituo cha Tokeni** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`  | Kituo cha tokeni chaguo-msingi cha Spring ([Mfano wa Usanidi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **Kituo cha JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | Kituo chaguo-msingi cha Seti ya JWK ([Mfano wa Usanidi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **Usanidi wa OpenID** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Hati ya kugundua OIDC (inayotengenezwa moja kwa moja) |
| **Hadhira ya APIM** | `mcp-client`                                                     | ID ya mteja wa OAuth au jina la rasilimali ya API |
| **Sera ya APIM**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` inatumia URL hii ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Makosa Yanayojirudia Mara kwa Mara

- **HTTPS/TLS:** Mlango wa APIM unahitaji kuwa kituo cha OpenID/JWKS kuwa HTTPS na cheti halali. Kwa kawaida, Azure Container Apps hutoa cheti cha TLS kinachotegemewa kwa kikoa kinachosimamiwa na Azure ([Majina ya kikoa maalum na vyeti vinavyosimamiwa vya bure katika Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ikiwa unatumia kikoa maalum, hakikisha kuambatisha cheti (unaweza kutumia huduma ya vyeti inayoendeshwa bure na Azure) ([Majina ya kikoa maalum na vyeti vinavyosimamiwa vya bure katika Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ikiwa APIM haiwezi kuamini cheti cha kituo, `<validate-jwt>` itashindwa kupakua metadata.

- **Upatikana wa Kituo:** Hakikisha vituo vya programu ya Spring vinaweza kufikiwa kutoka APIM. Kutumia `--ingress external` (au kuamilisha ingizo kwenye lango) ni rahisi zaidi. Ikiwa umechagua mazingira ya ndani au yanayolengwa na vNet, APIM (kawaida ya umma) inaweza isifike kwenda hapo isipokuwa ikawekwa katika vNet ile ile. Katika mipango ya majaribio, upendeleo ingizo la umma ili APIM iweze kuita URL za `.well-known` na `/jwks`.

- **Kugundua OpenID Kumewezeshwa:** Kwa kawaida, Spring Authorization Server **hainaonyesha** `/.well-known/openid-configuration` isipokuwa OIDC iwe imewezeshwa. Hakikisha umejumuisha `.oidc(Customizer.withDefaults())` katika usanidi wako wa usalama (angalia hapo juu) ili kiungo cha usanidi wa mtoa huduma kiwe hai ([Mfano wa Usanidi :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Vinginevyo, mwito wa `<openid-config>` wa APIM utarudisha kosa 404.

- **Dai la Hadhira:** Tabia ya kawaida ya Spring ni kuweka dai la `aud` kuwa ID ya mteja. Ikiwa ukaguzi wa `<audience>` wa APIM utashindwa, huenda ukahitaji kubinafsisha tokeni (kama ilivyoonyeshwa hapo juu) au kurekebisha sera ya APIM. Hakikisha hadhira katika JWT yako inalingana na unavyoisanidi kwenye `<audience>`.

- **Uchambuzi wa Metadata ya JSON:** Metadata ya usanidi wa OpenID lazima iwe halali. Usanidi wa kawaida wa Spring utaonyesha hati ya kawaida ya metadata ya OIDC. Thibitisha kuwa ina `issuer` sahihi na `jwks_uri`. Ikiwa unaendesha Spring nyuma ya wakala au njia za msingi kwa njia, hakikisha URL katika metadata hii ni sahihi. APIM itatumia maadili haya kama yalivyo.

- **Mpangilio wa Sera:** Katika sera ya APIM, weka `<validate-jwt>` **kabla** ya mtu yeyote kupeleka kwenye backend. Vinginevyo, simu zinaweza kufikia programu yako bila tokeni halali. Pia hakikisha `<validate-jwt>` inaonekana mara moja chini ya `<inbound>` (si ndani ya hali nyingine) ili APIM itumie sera hii.

Kwa kufuata hatua zilizo hapo juu, unaweza kuendesha seva yako ya Spring AI MCP kwenye Azure Container Apps na kuweka Azure API Management ithibitishe JWT za OAuth2 zinazoingia kwa sera ndogo. Mambo muhimu ni: toa vituo vya Spring Auth hadharani na TLS, wezesha kugundua OIDC, na elekeza `validate-jwt` ya APIM kwenye URL ya usanidi wa OpenID (ili ipate JWKS moja kwa moja). Mpangilio huu unafaa kwa mazingira ya majaribio/maendeleo; kwa uzalishaji, fikiria usimamizi sahihi wa siri, muda wa tokeni, na mizunguko ya funguo katika JWKS kama inavyohitajika.


**Marejeleo:** Angalia nyaraka za Spring Authorization Server kwa vituo vya chaguo-msingi ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) na usanidi wa OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); angalia nyaraka za Microsoft APIM kwa mifano ya `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); na nyaraka za Azure Container Apps kwa uenezaji na vyeti ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->