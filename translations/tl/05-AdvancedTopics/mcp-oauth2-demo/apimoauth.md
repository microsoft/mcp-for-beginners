# Pag-deploy ng Spring AI MCP App sa Azure Container Apps

> [!WARNING]
> Ang pinagsamang authorization/resource server na ito ay para sa pag-aaral at
> paggamit sa dev/test lamang. Para sa mga production system, dapat gumamit ng dedikadong identity provider,
> permanenteng signing keys, at mga kredensyal na nakaimbak sa isang managed secret store.

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Larawan: Spring AI MCP server na secured gamit ang Spring Authorization Server. Nagbibigay ang server ng access tokens sa mga kliyente at sinusuri ang mga ito sa mga papasok na kahilingan (pinagmulan: Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para ideploy ang Spring MCP server, i-build ito bilang isang container at gamitin ang Azure Container Apps na may external ingress. Halimbawa, gamit ang Azure CLI maaari mong patakbuhin:

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

Lumilikha ito ng pampublikong naa-access na Container App na may naka-enable na HTTPS (nagbibigay ang Azure ng libreng TLS certificate para sa default na `*.azurecontainerapps.io` domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kasama sa output ng utos ang FQDN ng app (hal. `my-mcp-app.eastus.azurecontainerapps.io`), na magiging base ng **issuer URL**. Siguraduhing naka-enable ang HTTP ingress (gaya ng nasa itaas) para maabot ng APIM ang app. Sa test/dev setup, gamitin ang `--ingress external` option (o mag-bind ng custom domain na may TLS ayon sa [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). I-imbak ang anumang sensitibong properties (tulad ng OAuth client secrets) sa Container Apps secrets o Azure Key Vault, at i-map ang mga ito sa container bilang environment variables. 

## Pag-configure ng Spring Authorization Server

Sa code ng iyong Spring Boot app, isama ang Spring Authorization Server at Resource Server starters. I-configure ang isang `RegisteredClient` (para sa `client_credentials` grant sa dev/test) at isang JWT key source. Halimbawa, sa `application.properties` maaari mong itakda:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

I-enable ang Authorization Server at Resource Server sa pamamagitan ng pagde-define ng security filter chain. Halimbawa:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Paganahin ang mga endpoint ng Authorization Server
            .apply(authzServer.and())
            // Paganahin ang Resource Server (beripikahin ang JWT sa mga papasok na kahilingan)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Huwag paganahin ang CSRF (ang MCP server ay hindi nakabase sa browser)
            .csrf(csrf -> csrf.disable())
            // Payagan ang CORS para sa mga demo tool ng client
            .cors(withDefaults());
        return http.build();
    }

    // Tukuyin ang isang in-memory client (RegisteredClient) at isang JWK source:
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
        // Bumuo ng isang RSA key (para sa dev/test, bumuo ng bago sa pagsisimula)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ipapakita ng setup na ito ang default na OAuth2 endpoints: `/oauth2/token` para sa mga token at `/oauth2/jwks` para sa JSON Web Key Set. (Sa default, Spring’s `AuthorizationServerSettings` ay nagmamapa ng `/oauth2/token` at `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Magbibigay ang server ng JWT access tokens na nilagdaan gamit ang RSA key sa itaas, at ipapublish ang public key nito sa `https://<your-app>:/oauth2/jwks`. 

**I-enable ang OpenID Connect discovery:** Para pahintulutan ang APIM na awtomatikong kunin ang issuer at JWKS, i-enable ang OIDC provider configuration endpoint sa pamamagitan ng pagdagdag ng `.oidc(Customizer.withDefaults())` sa iyong security configuration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Halimbawa:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– pinapagana ang /.well-known/openid-configuration
```

Ina-expose nito ang `/.well-known/openid-configuration`, na maaaring gamitin ng APIM para sa metadata. Sa huli, maaari mong i-customize ang JWT **audience** claim upang pumasa ang APIM’s `<audiences>` check. Halimbawa, magdagdag ng token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Magtakda ng sariling audience (hal. ang client ID o API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tinitiyak nito na ang mga token ay mayroong `"aud": ["mcp-client"]`, na tumutugma sa client ID o scope na inaasahan ng APIM. 

## Pagpapakita ng Token at JWKS Endpoints

Pagkatapos ma-deploy, ang iyong app’s **issuer URL** ay `https://<app-fqdn>`, hal. `https://my-mcp-app.eastus.azurecontainerapps.io`. Ang mga OAuth2 endpoints nito ay:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – dito kumukuha ng mga token ang mga kliyente (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – nagbabalik ng JWK set (ginagamit ng APIM upang makuha ang signing keys).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (naglalaman ng `issuer`, `token_endpoint`, `jwks_uri`, atbp.).  

Ituturo ng APIM ang **OpenID configuration URL**, kung saan nito nadidiskubre ang `jwks_uri`. Halimbawa, kung ang Container App FQDN mo ay `my-mcp-app.eastus.azurecontainerapps.io`, dapat gamitin ng APIM’s `<openid-config url="...">` ang `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Sa default, ise-set ng Spring ang `issuer` sa metadata na iyon bilang parehas na base URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Pag-configure ng Azure API Management (`validate-jwt`)

Sa Azure APIM, magdagdag ng inbound policy na gumagamit ng `<validate-jwt>` policy upang suriin ang mga papasok na JWT laban sa iyong Spring Authorization Server. Para sa simpleng setup, maaari mong gamitin ang OpenID Connect metadata URL. Halimbawa ng snippet ng policy:

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

Sinabi ng policy na ito sa APIM na kunin ang OpenID configuration mula sa Spring Auth Server, kunin ang JWKS nito, at suriin na bawat token ay nilagdaan ng isang pinagkakatiwalaang key at may tamang audience. (Kung hindi mo isama ang `<issuers>`, gagamitin ng APIM ang `issuer` claim mula sa metadata nang awtomatiko.) Dapat tumugma ang `<audience>` sa iyong client ID o API resource identifier sa token (sa halimbawa sa itaas, itinakda namin ito sa `"mcp-client"`). Ito ay alinsunod sa dokumentasyon ng Microsoft tungkol sa paggamit ng `validate-jwt` na may `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Pagkatapos ng validation, ipapasa ng APIM ang kahilingan (kasama ang orihinal na `Authorization` header) sa backend. Dahil ang Spring app ay isang resource server din, muling sasaliksikin nito ang token, ngunit tiniyak na ng APIM ang pagiging wasto nito. (Para sa development, maaari kang umasa sa check ng APIM at huwag paganahin ang karagdagang pagsusuri sa app kung nais, ngunit mas ligtas na panatilihin ang pareho.)

## Mga Halimbawa ng Setting

| Setting            | Halimbawa ng Halaga                                                   | Mga Tala                                  |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL ng Iyong Container App (base URI)     |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Default na Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Default na JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery document (awtomatikong-generated)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID o pangalan ng API resource |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | Ginagamit ng `<validate-jwt>` ang URL na ito ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Mga Karaniwang Kapahamakan

- **HTTPS/TLS:** Kinakailangan ng APIM gateway na ang OpenID/JWKS endpoint ay HTTPS na may wastong sertipiko. Sa default, nagbibigay ang Azure Container Apps ng pinagkakatiwalaang TLS cert para sa Azure-managed domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kung gumagamit ka ng custom domain, siguraduhing naka-bind ang isang sertipiko (maaaring gamitin ang libreng managed cert feature ng Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kung hindi mapagkakatiwalaan ng APIM ang sertipiko ng endpoint, mabibigo ang `<validate-jwt>` na kunin ang metadata.  

- **Endpoint Accessibility:** Siguraduhing maaabot ng APIM ang mga endpoint ng Spring app. Mas simple ang paggamit ng `--ingress external` (o pag-enable ng ingress sa portal). Kung pinili mo ang internal o vNet-bound na environment, maaaring hindi maabot ng APIM (na sa default ay public) ang app maliban kung nasa parehong VNet. Sa test setup, mas mainam ang public ingress para ma-access ng APIM ang `.well-known` at `/jwks` URLs. 

- **OpenID Discovery Enabled:** Sa default, hindi ina-expose ng Spring Authorization Server ang `/.well-known/openid-configuration` maliban kung naka-enable ang OIDC. Siguraduhing isama ang `.oidc(Customizer.withDefaults())` sa iyong security config (tingnan sa itaas) para maging aktibo ang provider configuration endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Kung hindi, magbabalik ng 404 ang tawag ng APIM’s `<openid-config>`.

- **Audience Claim:** Ang default na pag-uugali ng Spring ay itakda ang `aud` claim sa client ID. Kung mabigo ang APIM’s `<audience>` check, maaaring kailangan mong i-customize ang token (gaya ng ipinakita sa itaas) o ayusin ang policy ng APIM. Siguraduhing tumutugma ang audience sa iyong JWT sa nakasaad sa `<audience>`. 

- **JSON Metadata Parsing:** Kailangang valid ang OpenID configuration JSON. Maglalabas ang default config ng Spring ng karaniwang dokumento ng OIDC metadata. Tiyaking naglalaman ito ng tamang `issuer` at `jwks_uri`. Kung naka-host ang Spring sa likod ng proxy o path-based na ruta, i-double check ang mga URL sa metadata na ito. Gagamitin ng APIM ang mga halagang ito nang diretso. 

- **Policy Ordering:** Sa policy ng APIM, ilagay ang `<validate-jwt>` **bago** ang anumang routing papunta sa backend. Kung hindi, maaring marating ng mga tawag ang iyong app nang walang wastong token. Siguraduhing ang `<validate-jwt>` ay nasa ilalim agad ng `<inbound>` (hindi nested sa loob ng ibang kondisyon) upang maipatupad ito ng APIM.

Sa pagsunod sa mga hakbang sa itaas, maaari mong patakbuhin ang iyong Spring AI MCP server sa Azure Container Apps at hayaang i-validate ng Azure API Management ang mga papasok na OAuth2 JWT gamit ang minimal na policy. Ang mga susi ay: ipakita ang Spring Auth endpoints nang publiko na may TLS, i-enable ang OIDC discovery, at ituro ang `validate-jwt` ng APIM sa OpenID config URL (para awtomatikong makuha ang JWKS). Ang setup na ito ay angkop para sa dev/test environment; para sa production, isaalang-alang ang tamang pamamahala ng mga lihim, token lifetimes, at pagpapalit ng mga key sa JWKS kung kinakailangan. 


**Mga Sanggunian:** Tingnan ang mga dokumento ng Spring Authorization Server para sa mga default na endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) at OIDC na konfigurasyon ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); tingnan ang mga dokumento ng Microsoft APIM para sa mga halimbawa ng `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); at mga dokumento ng Azure Container Apps para sa deployment at mga sertipiko ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->