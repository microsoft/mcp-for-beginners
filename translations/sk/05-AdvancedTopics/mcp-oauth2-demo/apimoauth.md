# Nasadenie aplikácie Spring AI MCP do Azure Container Apps

> [!WARNING]
> Tento kombinovaný server autorizácie/zdrojov je určený na vzdelávacie a
> vývojové/testovacie použitie. Produkčné systémy by mali používať vyhradeného poskytovateľa identity,
> trvalé podpisové kľúče a poverenia uložené v spravovanom úložisku tajomstiev.

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

Týmto sa vytvorí verejne prístupná Container App s povoleným HTTPS (Azure vydáva bezplatný TLS certifikát pre predvolenú doménu `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Výstup príkazu obsahuje FQDN aplikácie (napr. `my-mcp-app.eastus.azurecontainerapps.io`), ktorý sa stáva základom **issuer URL**. Uistite sa, že je povolený HTTP ingress (ako vyššie), aby APIM mala prístup k aplikácii. V testovacom/vývojovom prostredí použite možnosť `--ingress external` (alebo priraďte vlastnú doménu s TLS podľa [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Akékoľvek citlivé vlastnosti (ako tajomstvá OAuth klienta) uložte do tajomstiev Container Apps alebo Azure Key Vault a namapujte ich do kontajnera ako premenné prostredia. 

## Konfigurácia Spring Authorization Server

Vo vašom kóde Spring Boot aplikácie zahrňte štartéry Spring Authorization Server a Resource Server. Nakonfigurujte `RegisteredClient` (pre grant `client_credentials` vo vývojovom/testovacom režime) a zdroj kľúčov JWT. Napríklad v súbore `application.properties` môžete nastaviť:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Povoliť Authorization Server a Resource Server definovaním bezpečnostného filter reťazca. Napríklad:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Povoliť koncové body Autorizačného servera
            .apply(authzServer.and())
            // Povoliť server zdrojov (overovať JWT na prichádzajúcich požiadavkách)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Vypnúť CSRF (MCP server nie je založený na prehliadači)
            .csrf(csrf -> csrf.disable())
            // Povoliť CORS pre klientské demo nástroje
            .cors(withDefaults());
        return http.build();
    }

    // Definovať klienta v pamäti (RegisteredClient) a zdroj JWK:
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
        // Generovať RSA kľúč (pre vývoj/test, generovať znova pri spustení)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Táto konfigurácia sprístupní predvolené OAuth2 koncové body: `/oauth2/token` pre tokeny a `/oauth2/jwks` pre JSON Web Key Set. (Štandardne Spring `AuthorizationServerSettings` mapuje `/oauth2/token` a `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server bude vydávať JWT prístupové tokeny podpísané vyššie uvedeným RSA kľúčom a verejný kľúč zverejní na `https://<your-app>:/oauth2/jwks`. 

**Povoliť OpenID Connect discovery:** Aby APIM mohol automaticky získať issuer a JWKS, povoľte endpoint konfigurácie OIDC poskytovateľa pridaním `.oidc(Customizer.withDefaults())` do vašej bezpečnostnej konfigurácie ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Napríklad:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– povolí /.well-known/openid-configuration
```

Tým sa sprístupní `/.well-known/openid-configuration`, ktoré APIM môže využiť pre metadata. Nakoniec možno budete chcieť prispôsobiť JWT **audience** claim, aby splnil kontrolu `<audiences>` v APIM. Napríklad pridajte token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Nastavte vlastné publikum (napr. ID klienta alebo identifikátor API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Toto zabezpečí, že tokeny budú niesť `"aud": ["mcp-client"]`, čo zodpovedá ID klienta alebo očakávanému rozsahu APIM. 

## Sprístupnenie Token a JWKS Endpoints

Po nasadení bude **issuer URL** vašej aplikácie `https://<app-fqdn>`, napr. `https://my-mcp-app.eastus.azurecontainerapps.io`. Jej OAuth2 koncové body sú:

- **Koncový bod tokenu:** `https://<app-fqdn>/oauth2/token` – klienti tu získavajú tokeny (prúd klientských poverení).
- **Koncový bod JWKS:** `https://<app-fqdn>/oauth2/jwks` – vracia sadu JWK (APIM ju používa na získanie podpisových kľúčov).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (obsahuje `issuer`, `token_endpoint`, `jwks_uri` atď.).  

APIM bude smerovať na **OpenID konfiguračnú URL**, z ktorej zistí `jwks_uri`. Napríklad, ak FQDN vašej Container App je `my-mcp-app.eastus.azurecontainerapps.io`, potom by APIM `<openid-config url="...">` mal používať `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Štandardne Spring nastaví `issuer` v týchto metadátach na rovnakú základnú URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurácia Azure API Management (`validate-jwt`)

V Azure APIM pridajte inbound politiku, ktorá používa `<validate-jwt>` na overenie prichádzajúcich JWT voči Spring Authorization Server. Pre jednoduchú konfiguráciu môžete použiť OpenID Connect metadata URL. Príklad úryvku politiky:

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

Táto politika hovorí APIM, aby načítal OpenID konfiguráciu zo Spring Auth Server, získal jeho JWKS a validoval, či je každý token podpísaný dôveryhodným kľúčom a má správne publikum. (Ak vynecháte `<issuers>`, APIM automaticky použije `issuer` claim z metadát.) `<audience>` by malo zodpovedať ID klienta alebo identifikátoru API zdroja v tokene (v uvedenom príklade sme nastavili `"mcp-client"`). Toto je v súlade s dokumentáciou Microsoftu o používaní `validate-jwt` s `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po overení APIM presmeruje požiadavku (vrátane pôvodného `Authorization` hlavičky) na backend. Keďže Spring aplikácia je tiež resource server, token znovu overí, ale APIM už zabezpečil jeho platnosť. (Vo vývoji sa môžete spoľahnúť na kontrolu APIM a vypnúť ďalšie kontroly v aplikácii, ak chcete, ale bezpečnejšie je mať oboje.)

## Príklad nastavení

| Nastavenie         | Príklad hodnoty                                                      | Poznámky                                   |
|-------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL vašej Container App (základná URI)    |
| **Token endpoint**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Predvolený Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Predvolený JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Dokument OIDC discovery (automaticky generovaný)    |
| **APIM audience** | `mcp-client`                                                         | OAuth ID klienta alebo názov API zdroja   |
| **APIM policy**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` používa túto URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Bežné chyby

- **HTTPS/TLS:** Brána APIM vyžaduje, aby OpenID/JWKS endpoint bol HTTPS s platným certifikátom. Predvolene Azure Container Apps poskytuje dôveryhodný TLS certifikát pre Azure spravovanú doménu ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ak používate vlastnú doménu, uistite sa, že ste certifikát priradili (môžete použiť Azure free managed cert funkciu) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ak APIM nebude môcť dôverovať certifikátu endpointu, `<validate-jwt>` nezíska metadáta a zlyhá.  

- **Prístupnosť endpointu:** Uistite sa, že endpointy Spring aplikácie sú prístupné z APIM. Použitie `--ingress external` (alebo povolenie ingress v portáli) je najjednoduchšie. Ak ste zvolili interné alebo vNet-bound prostredie, APIM (štandardne verejné) nemusí mať k nemu prístup, pokiaľ nie je v tej istej VNet. V testovacom režime uprednostnite verejný ingress, aby APIM mohol volať `.well-known` a `/jwks` URL. 

- **Povolené OpenID Discovery:** Štandardne Spring Authorization Server **neposkytuje** `/.well-known/openid-configuration`, ak OIDC nie je povolené. Uistite sa, že v bezpečnostnej konfigurácii máte `.oidc(Customizer.withDefaults())` (viď vyššie), aby bol endpoint poskytovateľa aktívny ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Inak bude APIM `<openid-config>` volať 404.

- **Audience Claim:** Štandardné správanie Spring je nastaviť `aud` claim na ID klienta. Ak kontrola `<audience>` v APIM zlyhá, možno budete musieť token prispôsobiť (ako je uvedené vyššie) alebo upraviť politiku APIM. Uistite sa, že audience v JWT zodpovedá nastaveniu v `<audience>`. 

- **Parsovanie JSON Metadát:** OpenID konfiguračný JSON musí byť platný. Štandardná konfigurácia Spring vydáva štandardný OIDC metadata dokument. Overte, že obsahuje správne `issuer` a `jwks_uri`. Ak hosťujete Spring za proxy alebo so založením na ceste, dôkladne skontrolujte URL v týchto metadátach. APIM tieto hodnoty použije tak, ako sú. 

- **Poradie politík:** V politike APIM umiestnite `<validate-jwt>` **pred** akýmkoľvek routovaním na backend. Inak môžu požiadavky dosiahnuť vašu aplikáciu bez platného tokenu. Tiež zabezpečte, že `<validate-jwt>` je umiestnený hneď pod `<inbound>` (nie vnorený v inom podmienkovom bloku), aby ho APIM aplikoval.

Dodržaním vyššie uvedených krokov môžete prevádzkovať váš Spring AI MCP server v Azure Container Apps a nechať Azure API Management overovať prichádzajúce OAuth2 JWT pomocou minimálnej politiky. Kľúčové body sú: sprístupniť Spring Auth endpointy verejne cez TLS, povoliť OIDC discovery a nasmerovať APIM `validate-jwt` na OpenID konfiguračnú URL (aby mohol automaticky načítavať JWKS). Táto konfigurácia je vhodná pre vývojové/testovacie prostredie; na produkciu zvážte správu tajomstiev, životnosť tokenov a rotovanie kľúčov v JWKS podľa potreby. 


**Referencie:** Pozri dokumentáciu Spring Authorization Server pre predvolené koncové body ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) a konfiguráciu OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); pozri dokumentáciu Microsoft APIM pre príklady `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); a dokumentáciu Azure Container Apps pre nasadenie a certifikáty ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->