# Nasadenie aplikácie Spring AI MCP do Azure Container Apps

 ([Zabezpečenie Spring AI MCP serverov pomocou OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Obrázok: Spring AI MCP server zabezpečený pomocou Spring Authorization Server. Server vydáva prístupové tokeny klientom a overuje ich pri prichádzajúcich požiadavkách (zdroj: Spring blog) ([Zabezpečenie Spring AI MCP serverov pomocou OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Na nasadenie Spring MCP servera ho zostavte ako kontajner a použite Azure Container Apps s externým prístupom. Napríklad pomocou Azure CLI môžete spustiť:

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

Týmto sa vytvorí verejne prístupná Container App s povoleným HTTPS (Azure vydáva bezplatný TLS certifikát pre predvolenú doménu `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Výstup príkazu obsahuje FQDN aplikácie (napr. `my-mcp-app.eastus.azurecontainerapps.io`), ktorý sa stáva základom **issuer URL**. Uistite sa, že je povolený HTTP ingress (ako vyššie), aby APIM mohol aplikáciu dosiahnuť. V testovacom alebo vývojovom prostredí použite možnosť `--ingress external` (alebo priraďte vlastnú doménu s TLS podľa [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Akékoľvek citlivé údaje (napr. OAuth client secrets) ukladajte do Container Apps secrets alebo Azure Key Vault a mapujte ich do kontajnera ako premenné prostredia.

## Konfigurácia Spring Authorization Servera

Vo vašom kóde Spring Boot aplikácie zahrňte Spring Authorization Server a Resource Server starters. Nakonfigurujte `RegisteredClient` (pre `client_credentials` grant v dev/test prostredí) a zdroj JWT kľúča. Napríklad v `application.properties` môžete nastaviť:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Povoľte Authorization Server a Resource Server definovaním bezpečnostného filter chainu. Napríklad:

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

Táto konfigurácia sprístupní predvolené OAuth2 endpointy: `/oauth2/token` pre tokeny a `/oauth2/jwks` pre JSON Web Key Set. (Predvolene Spring `AuthorizationServerSettings` mapuje `/oauth2/token` a `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server bude vydávať JWT prístupové tokeny podpísané RSA kľúčom vyššie a zverejní svoj verejný kľúč na `https://<your-app>:/oauth2/jwks`.

**Povoľte OpenID Connect discovery:** Aby APIM mohol automaticky získať issuer a JWKS, povoľte endpoint konfigurácie OIDC providera pridaním `.oidc(Customizer.withDefaults())` do vašej bezpečnostnej konfigurácie ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Napríklad:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Tým sa sprístupní `/.well-known/openid-configuration`, ktoré APIM môže použiť na získanie metadát. Nakoniec možno budete chcieť prispôsobiť JWT **audience** claim, aby APIM kontrola `<audiences>` prešla. Napríklad pridajte token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tým zabezpečíte, že tokeny budú obsahovať `"aud": ["mcp-client"]`, čo zodpovedá klientskemu ID alebo scope očakávanému APIM.

## Sprístupnenie Token a JWKS endpointov

Po nasadení bude **issuer URL** vašej aplikácie `https://<app-fqdn>`, napr. `https://my-mcp-app.eastus.azurecontainerapps.io`. Jej OAuth2 endpointy sú:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – tu klienti získavajú tokeny (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – vracia JWK set (APIM ho používa na získanie podpisových kľúčov).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (obsahuje `issuer`, `token_endpoint`, `jwks_uri` a ďalšie).

APIM bude smerovať na **OpenID configuration URL**, odkiaľ získa `jwks_uri`. Napríklad, ak je FQDN Container App `my-mcp-app.eastus.azurecontainerapps.io`, potom APIM `<openid-config url="...">` by mal používať `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Predvolene Spring nastaví `issuer` v týchto metadátach na rovnakú základnú URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurácia Azure API Management (`validate-jwt`)

V Azure APIM pridajte inbound policy, ktorá používa `<validate-jwt>` na overenie prichádzajúcich JWT proti vášmu Spring Authorization Serveru. Pre jednoduché nastavenie môžete použiť OpenID Connect metadata URL. Príklad útržku politiky:

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

Táto politika hovorí APIM, aby získal OpenID konfiguráciu zo Spring Auth Servera, načítal jeho JWKS a overil, že každý token je podpísaný dôveryhodným kľúčom a má správne audience. (Ak vynecháte `<issuers>`, APIM automaticky použije `issuer` claim z metadát.) `<audience>` by mala zodpovedať vášmu klientskemu ID alebo identifikátoru API zdroja v tokene (v príklade vyššie sme nastavili `"mcp-client"`). Toto je v súlade s dokumentáciou Microsoftu o používaní `validate-jwt` s `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po overení APIM presmeruje požiadavku (vrátane pôvodného hlavičky `Authorization`) na backend. Keďže Spring aplikácia je tiež resource server, token znova overí, ale APIM už zabezpečil jeho platnosť. (Pre vývoj môžete spoľahnúť na kontrolu APIM a prípadne vypnúť ďalšie kontroly v aplikácii, ale bezpečnejšie je mať obe.)

## Príklad nastavení

| Nastavenie         | Príklad hodnoty                                                    | Poznámky                                   |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL vašej Container App (základná URI)     |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Predvolený Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Predvolený JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery dokument (automaticky generovaný) |
| **APIM audience**  | `mcp-client`                                                      | OAuth client ID alebo názov API zdroja     |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` používa túto URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Bežné úskalia

- **HTTPS/TLS:** APIM gateway vyžaduje, aby OpenID/JWKS endpoint bol HTTPS s platným certifikátom. Predvolene Azure Container Apps poskytuje dôveryhodný TLS certifikát pre Azure spravovanú doménu ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ak používate vlastnú doménu, nezabudnite priradiť certifikát (môžete využiť bezplatnú spravovanú certifikáciu Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ak APIM nemôže dôverovať certifikátu endpointu, `<validate-jwt>` zlyhá pri načítaní metadát.

- **Dostupnosť endpointov:** Uistite sa, že endpointy Spring aplikácie sú dostupné z APIM. Použitie `--ingress external` (alebo povolenie ingress v portáli) je najjednoduchšie. Ak ste zvolili interné alebo vNet-bound prostredie, APIM (predvolene verejné) nemusí mať prístup, pokiaľ nie je v rovnakom VNet. V testovacom prostredí uprednostnite verejný ingress, aby APIM mohol volať `.well-known` a `/jwks` URL.

- **Povolené OpenID Discovery:** Predvolene Spring Authorization Server **neposkytuje** `/.well-known/openid-configuration`, pokiaľ nie je povolený OIDC. Nezabudnite zahrnúť `.oidc(Customizer.withDefaults())` do bezpečnostnej konfigurácie (viď vyššie), aby bol endpoint konfigurácie aktívny ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Inak APIM `<openid-config>` volanie skončí 404.

- **Audience Claim:** Predvolené správanie Spring je nastaviť `aud` claim na klientske ID. Ak APIM kontrola `<audience>` zlyhá, možno budete musieť token prispôsobiť (ako je uvedené vyššie) alebo upraviť APIM politiku. Uistite sa, že audience v JWT zodpovedá tomu, čo konfigurujete v `<audience>`.

- **Parsovanie JSON metadát:** OpenID konfiguračný JSON musí byť platný. Predvolená konfigurácia Spring vygeneruje štandardný OIDC metadata dokument. Overte, že obsahuje správne `issuer` a `jwks_uri`. Ak hostujete Spring za proxy alebo s path-based routou, dôkladne skontrolujte URL v týchto metadátach. APIM ich použije tak, ako sú.

- **Poradie politík:** V APIM politike umiestnite `<validate-jwt>` **pred** akýmkoľvek smerovaním na backend. Inak môžu požiadavky dosiahnuť aplikáciu bez platného tokenu. Tiež zabezpečte, aby `<validate-jwt>` bol umiestnený priamo pod `<inbound>` (nie vnorený v inom podmienkovom bloku), aby ho APIM aplikoval.

Dodržiavaním týchto krokov môžete spustiť svoj Spring AI MCP server v Azure Container Apps a nechať Azure API Management overovať prichádzajúce OAuth2 JWT s minimálnou politikou. Kľúčové body sú: sprístupniť Spring Auth endpointy verejne s TLS, povoliť OIDC discovery a nasmerovať APIM `validate-jwt` na OpenID config URL (aby mohol automaticky načítať JWKS). Toto nastavenie je vhodné pre dev/test prostredie; do produkcie zvážte správu tajomstiev, životnosť tokenov a rotáciu kľúčov v JWKS podľa potreby.
**Referencie:** Pozrite si dokumentáciu Spring Authorization Server pre predvolené koncové body ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) a konfiguráciu OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); pozrite si dokumentáciu Microsoft APIM pre príklady `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); a dokumentáciu Azure Container Apps pre nasadenie a certifikáty ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.