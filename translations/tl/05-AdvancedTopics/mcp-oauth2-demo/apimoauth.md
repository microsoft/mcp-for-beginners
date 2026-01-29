# Pag-deploy ng Spring AI MCP App sa Azure Container Apps

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Larawan: Spring AI MCP server na naka-secure gamit ang Spring Authorization Server. Nagbibigay ang server ng access tokens sa mga kliyente at sinusuri ang mga ito sa mga papasok na request (pinagmulan: Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para i-deploy ang Spring MCP server, i-build ito bilang container at gamitin ang Azure Container Apps na may external ingress. Halimbawa, gamit ang Azure CLI maaari mong patakbuhin:

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

Lumilikha ito ng isang publicly-accessible Container App na may naka-enable na HTTPS (nagbibigay ang Azure ng libreng TLS certificate para sa default na `*.azurecontainerapps.io` domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kasama sa output ng command ang FQDN ng app (hal. `my-mcp-app.eastus.azurecontainerapps.io`), na nagsisilbing base ng **issuer URL**. Siguraduhing naka-enable ang HTTP ingress (gaya ng nasa itaas) para maabot ng APIM ang app. Sa test/dev setup, gamitin ang `--ingress external` option (o mag-bind ng custom domain na may TLS ayon sa [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Itago ang mga sensitibong property (tulad ng OAuth client secrets) sa Container Apps secrets o Azure Key Vault, at i-map ang mga ito sa container bilang environment variables.

## Pag-configure ng Spring Authorization Server

Sa code ng iyong Spring Boot app, isama ang Spring Authorization Server at Resource Server starters. I-configure ang isang `RegisteredClient` (para sa `client_credentials` grant sa dev/test) at isang JWT key source. Halimbawa, sa `application.properties` maaari mong itakda:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

I-enable ang Authorization Server at Resource Server sa pamamagitan ng pag-define ng security filter chain. Halimbawa:

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

Ipapakita ng setup na ito ang default na OAuth2 endpoints: `/oauth2/token` para sa mga token at `/oauth2/jwks` para sa JSON Web Key Set. (Sa default, ang Spring `AuthorizationServerSettings` ay nagma-map ng `/oauth2/token` at `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Magbibigay ang server ng JWT access tokens na pinirmahan gamit ang RSA key sa itaas, at ipapublish ang public key nito sa `https://<your-app>:/oauth2/jwks`.

**I-enable ang OpenID Connect discovery:** Para awtomatikong makuha ng APIM ang issuer at JWKS, i-enable ang OIDC provider configuration endpoint sa pamamagitan ng pagdagdag ng `.oidc(Customizer.withDefaults())` sa iyong security configuration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Halimbawa:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Ipinapakita nito ang `/.well-known/openid-configuration`, na maaaring gamitin ng APIM para sa metadata. Sa huli, maaaring gusto mong i-customize ang JWT **audience** claim upang pumasa ang APIM sa `<audiences>` check nito. Halimbawa, magdagdag ng token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tinitiyak nito na ang mga token ay may `"aud": ["mcp-client"]`, na tumutugma sa client ID o scope na inaasahan ng APIM.

## Pagpapakita ng Token at JWKS Endpoints

Pagkatapos i-deploy, ang **issuer URL** ng iyong app ay magiging `https://<app-fqdn>`, hal. `https://my-mcp-app.eastus.azurecontainerapps.io`. Ang mga OAuth2 endpoints nito ay:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – dito kumukuha ng token ang mga kliyente (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – nagbabalik ng JWK set (ginagamit ng APIM para makuha ang signing keys).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (naglalaman ng `issuer`, `token_endpoint`, `jwks_uri`, atbp.).

Ituturo ng APIM ang **OpenID configuration URL**, kung saan nito madidiskubre ang `jwks_uri`. Halimbawa, kung ang FQDN ng iyong Container App ay `my-mcp-app.eastus.azurecontainerapps.io`, dapat gamitin ng APIM ang `<openid-config url="...">` na `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Sa default, itinatakda ng Spring ang `issuer` sa metadata na iyon sa parehong base URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Pag-configure ng Azure API Management (`validate-jwt`)

Sa Azure APIM, magdagdag ng inbound policy na gumagamit ng `<validate-jwt>` policy para suriin ang mga papasok na JWT laban sa iyong Spring Authorization Server. Para sa simpleng setup, maaari mong gamitin ang OpenID Connect metadata URL. Halimbawa ng policy snippet:

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

Sinasabi ng policy na ito sa APIM na kunin ang OpenID configuration mula sa Spring Auth Server, kunin ang JWKS nito, at i-validate na ang bawat token ay pinirmahan ng isang pinagkakatiwalaang key at may tamang audience. (Kung hindi mo isasama ang `<issuers>`, awtomatikong gagamitin ng APIM ang `issuer` claim mula sa metadata.) Dapat tumugma ang `<audience>` sa iyong client ID o API resource identifier sa token (sa halimbawa sa itaas, itinakda namin ito sa `"mcp-client"`). Ito ay naaayon sa dokumentasyon ng Microsoft tungkol sa paggamit ng `validate-jwt` kasama ang `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Pagkatapos ng validation, ipapasa ng APIM ang request (kasama ang orihinal na `Authorization` header) sa backend. Dahil ang Spring app ay isang resource server din, muling susuriin nito ang token, ngunit nasiguro na ng APIM ang bisa nito. (Para sa development, maaari kang umasa sa check ng APIM at i-disable ang karagdagang pagsusuri sa app kung nais, ngunit mas ligtas na panatilihin ang pareho.)

## Halimbawa ng Mga Setting

| Setting            | Halimbawa ng Halaga                                                  | Mga Tala                                   |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL ng iyong Container App (base URI)      |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Default na Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Default na JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery document (awtomatikong ginawa)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID o pangalan ng API resource |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | Ginagamit ng `<validate-jwt>` ang URL na ito ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Mga Karaniwang Problema

- **HTTPS/TLS:** Kinakailangan ng APIM gateway na ang OpenID/JWKS endpoint ay HTTPS na may valid na certificate. Sa default, nagbibigay ang Azure Container Apps ng pinagkakatiwalaang TLS cert para sa Azure-managed domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kung gagamit ka ng custom domain, siguraduhing mag-bind ng certificate (maaari mong gamitin ang libreng managed cert feature ng Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kapag hindi mapagkakatiwalaan ng APIM ang certificate ng endpoint, mabibigo ang `<validate-jwt>` na kunin ang metadata.

- **Accessibility ng Endpoint:** Siguraduhing maabot ng APIM ang mga endpoint ng Spring app. Pinakamadali ang paggamit ng `--ingress external` (o pag-enable ng ingress sa portal). Kung pinili mo ang internal o vNet-bound na environment, maaaring hindi maabot ng APIM (na default ay public) ang app maliban kung nasa parehong VNet. Sa test setup, mas mainam ang public ingress para ma-access ng APIM ang `.well-known` at `/jwks` URLs.

- **OpenID Discovery Enabled:** Sa default, hindi ipinapakita ng Spring Authorization Server ang `/.well-known/openid-configuration` maliban kung naka-enable ang OIDC. Siguraduhing isama ang `.oidc(Customizer.withDefaults())` sa iyong security config (tingnan sa itaas) para maging aktibo ang provider configuration endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Kung hindi, magreresulta sa 404 ang tawag ng APIM sa `<openid-config>`.

- **Audience Claim:** Sa default, itinatakda ng Spring ang `aud` claim sa client ID. Kung hindi pumasa ang APIM sa `<audience>` check, maaaring kailanganin mong i-customize ang token (gaya ng ipinakita sa itaas) o baguhin ang APIM policy. Siguraduhing tumutugma ang audience sa JWT sa iyong configuration sa `<audience>`.

- **JSON Metadata Parsing:** Dapat valid ang OpenID configuration JSON. Naglalabas ang default config ng Spring ng standard na OIDC metadata document. Siguraduhing tama ang `issuer` at `jwks_uri` na nilalaman nito. Kung naka-host ang Spring sa likod ng proxy o path-based route, i-double check ang mga URL sa metadata na ito. Gagamitin ng APIM ang mga halagang ito nang walang pagbabago.

- **Pagkakasunod-sunod ng Policy:** Sa APIM policy, ilagay ang `<validate-jwt>` **bago** ang anumang routing papunta sa backend. Kung hindi, maaaring maabot ng mga tawag ang iyong app nang walang valid na token. Siguraduhing ang `<validate-jwt>` ay nasa ilalim ng `<inbound>` (hindi naka-nest sa ibang kondisyon) para maipatupad ito ng APIM.

Sa pagsunod sa mga hakbang na ito, maaari mong patakbuhin ang iyong Spring AI MCP server sa Azure Container Apps at hayaang i-validate ng Azure API Management ang mga papasok na OAuth2 JWT gamit ang minimal na policy. Ang mga pangunahing punto ay: ipakita ang Spring Auth endpoints nang publiko gamit ang TLS, i-enable ang OIDC discovery, at ituro ang `validate-jwt` ng APIM sa OpenID config URL (para awtomatikong makuha ang JWKS). Ang setup na ito ay angkop para sa dev/test environment; para sa production, isaalang-alang ang tamang pamamahala ng mga secret, token lifetimes, at pag-ikot ng mga key sa JWKS kung kinakailangan.
**References:** Tingnan ang Spring Authorization Server docs para sa mga default na endpoints ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) at OIDC configuration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); tingnan ang Microsoft APIM docs para sa mga halimbawa ng `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); at Azure Container Apps docs para sa deployment at mga sertipiko ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.