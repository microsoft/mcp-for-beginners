# A Spring AI MCP alkalmazás telepítése Azure Container Apps-re

 ([A Spring AI MCP szerverek OAuth2-vel történő védelme](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Ábra: Spring AI MCP szerver Spring Authorization Server-rel védve. A szerver hozzáférési tokeneket bocsát ki a klienseknek, és ellenőrzi azokat a bejövő kéréseknél (forrás: Spring blog) ([A Spring AI MCP szerverek OAuth2-vel történő védelme](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* A Spring MCP szerver telepítéséhez készítsd el konténerként, majd használd az Azure Container Apps szolgáltatást külső bejárattal. Például az Azure CLI segítségével futtathatod:

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

Ez létrehoz egy nyilvánosan elérhető Container App-et HTTPS engedélyezéssel (az Azure ingyenes TLS tanúsítványt ad az alapértelmezett `*.azurecontainerapps.io` domainhez ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). A parancs kimenete tartalmazza az alkalmazás teljesen minősített domain nevét (pl. `my-mcp-app.eastus.azurecontainerapps.io`), amely lesz az **issuer URL** alapja. Győződj meg róla, hogy az HTTP bejárat engedélyezve van (ahogy fent), hogy az APIM elérhesse az alkalmazást. Teszt/fejlesztési környezetben használd a `--ingress external` opciót (vagy köss egy egyedi domaint TLS-sel a [Microsoft dokumentáció](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) szerint ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Bármilyen érzékeny beállítást (például OAuth kliens titkokat) tárolj Container Apps titkokban vagy Azure Key Vault-ban, és térképezd be őket környezeti változóként a konténerbe.

## Spring Authorization Server konfigurálása

A Spring Boot alkalmazásod kódjában add hozzá a Spring Authorization Server és Resource Server startereket. Konfigurálj egy `RegisteredClient`-et (a `client_credentials` grant típushoz fejlesztési/tesztelési környezetben) és egy JWT kulcsforrást. Például az `application.properties`-ben beállíthatod:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Engedélyezd az Authorization Server és Resource Server működését egy biztonsági szűrőlánc definiálásával. Például:

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

Ez a beállítás elérhetővé teszi az alapértelmezett OAuth2 végpontokat: `/oauth2/token` a tokenekhez és `/oauth2/jwks` a JSON Web Key Set-hez. (Alapértelmezés szerint a Spring `AuthorizationServerSettings` leképezi a `/oauth2/token` és `/oauth2/jwks` végpontokat ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) A szerver JWT hozzáférési tokeneket bocsát ki, amelyeket az előzőleg definiált RSA kulccsal ír alá, és közzéteszi a nyilvános kulcsát a `https://<your-app>:/oauth2/jwks` címen.

**Engedélyezd az OpenID Connect felfedezést:** Ahhoz, hogy az APIM automatikusan lekérhesse az issuer és JWKS adatokat, engedélyezd az OIDC szolgáltató konfigurációs végpontját azzal, hogy a biztonsági konfigurációdban hozzáadod a `.oidc(Customizer.withDefaults())` hívást ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Például:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Ez elérhetővé teszi a `/.well-known/openid-configuration` végpontot, amelyet az APIM metadata lekérésére használhat. Végül érdemes lehet testreszabni a JWT **audience** mezőt, hogy az APIM `<audiences>` ellenőrzése sikeres legyen. Például adj hozzá egy token testreszabót:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ez biztosítja, hogy a tokenek tartalmazzák az `"aud": ["mcp-client"]` értéket, amely megfelel az APIM által elvárt kliensazonosítónak vagy scope-nak.

## Token és JWKS végpontok elérhetővé tétele

A telepítés után az alkalmazásod **issuer URL-je** `https://<app-fqdn>` lesz, például `https://my-mcp-app.eastus.azurecontainerapps.io`. Az OAuth2 végpontok:

- **Token végpont:** `https://<app-fqdn>/oauth2/token` – itt kérhetnek a kliensek tokeneket (client_credentials folyamat).
- **JWKS végpont:** `https://<app-fqdn>/oauth2/jwks` – visszaadja a JWK készletet (amit az APIM a kulcsok lekérésére használ).
- **OpenID konfiguráció:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC felfedezési JSON (tartalmazza az `issuer`, `token_endpoint`, `jwks_uri` stb. mezőket).

Az APIM az **OpenID konfiguráció URL-re** mutat, ahonnan lekéri a `jwks_uri`-t. Például, ha a Container App FQDN-je `my-mcp-app.eastus.azurecontainerapps.io`, akkor az APIM `<openid-config url="...">` beállítása legyen `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Alapértelmezés szerint a Spring ugyanazt az alap URL-t állítja be az `issuer` mezőben ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management konfigurálása (`validate-jwt`)

Az Azure APIM-ben adj hozzá egy bejövő szabályt, amely a `<validate-jwt>` szabályt használja a bejövő JWT-k ellenőrzésére a Spring Authorization Server alapján. Egyszerű beállításhoz használhatod az OpenID Connect metadata URL-t. Példa szabályrészlet:

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

Ez a szabály megmondja az APIM-nek, hogy töltse le a Spring Auth Server OpenID konfigurációját, szerezze be a JWKS-t, és ellenőrizze, hogy minden token megbízható kulccsal van aláírva, valamint a megfelelő audience értékkel rendelkezik. (Ha kihagyod az `<issuers>` elemet, az APIM automatikusan a metadata `issuer` mezőjét használja.) Az `<audience>` értékének meg kell egyeznie a kliensazonosítóval vagy az API erőforrás nevével a tokenben (a fenti példában `"mcp-client"`). Ez összhangban van a Microsoft dokumentációjával a `validate-jwt` és `<openid-config>` használatáról ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Az ellenőrzés után az APIM továbbítja a kérést (beleértve az eredeti `Authorization` fejlécet) a háttérrendszer felé. Mivel a Spring alkalmazás is resource server, újra ellenőrzi a tokent, de az APIM már biztosította annak érvényességét. (Fejlesztés alatt támaszkodhatsz az APIM ellenőrzésére és kikapcsolhatod az alkalmazásban az extra ellenőrzéseket, de biztonságosabb mindkettőt megtartani.)

## Példa beállítások

| Beállítás          | Példa érték                                                        | Megjegyzések                               |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | A Container App URL-je (alap URI)          |
| **Token végpont**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Alapértelmezett Spring token végpont ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS végpont**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Alapértelmezett JWK készlet végpont ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID konfiguráció** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC felfedezési dokumentum (automatikusan generált) |
| **APIM audience**  | `mcp-client`                                                      | OAuth kliensazonosító vagy API erőforrás neve |
| **APIM szabály**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ezt az URL-t használja ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Gyakori buktatók

- **HTTPS/TLS:** Az APIM átjárónak HTTPS és érvényes tanúsítvány szükséges az OpenID/JWKS végpont eléréséhez. Alapértelmezés szerint az Azure Container Apps megbízható TLS tanúsítványt biztosít az Azure által kezelt domainhez ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Egyedi domain használata esetén mindenképp köss tanúsítványt (az Azure ingyenes kezelt tanúsítvány funkcióját is használhatod) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ha az APIM nem bízik a végpont tanúsítványában, a `<validate-jwt>` nem tudja lekérni a metadata-t.

- **Végpont elérhetőség:** Biztosítsd, hogy a Spring alkalmazás végpontjai elérhetők legyenek az APIM számára. A legegyszerűbb a `--ingress external` használata (vagy a portálon az ingress engedélyezése). Ha belső vagy vNet-hez kötött környezetet választasz, az APIM (alapértelmezés szerint publikus) nem biztos, hogy eléri, hacsak nem ugyanabban a vNet-ben van. Teszteléshez inkább publikus ingress ajánlott, hogy az APIM elérje a `.well-known` és `/jwks` URL-eket.

- **OpenID felfedezés engedélyezve:** Alapértelmezés szerint a Spring Authorization Server **nem teszi elérhetővé** a `/.well-known/openid-configuration` végpontot, ha az OIDC nincs engedélyezve. Győződj meg róla, hogy a biztonsági konfigurációban szerepel a `.oidc(Customizer.withDefaults())` (lásd fent), hogy a szolgáltató konfigurációs végpont aktív legyen ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ellenkező esetben az APIM `<openid-config>` hívása 404-et fog kapni.

- **Audience mező:** A Spring alapértelmezett viselkedése, hogy az `aud` mezőt a kliensazonosítóra állítja. Ha az APIM `<audience>` ellenőrzése nem sikerül, szükség lehet a token testreszabására (ahogy fent bemutatva) vagy az APIM szabály módosítására. Győződj meg róla, hogy a JWT-ben szereplő audience megegyezik az `<audience>` beállítással.

- **JSON metadata elemzés:** Az OpenID konfiguráció JSON-nak érvényesnek kell lennie. A Spring alapértelmezett konfigurációja szabványos OIDC metadata dokumentumot ad ki. Ellenőrizd, hogy tartalmazza a helyes `issuer` és `jwks_uri` értékeket. Ha a Spring proxyn vagy útvonal alapú routing mögött fut, ellenőrizd a metadata URL-eket. Az APIM ezeket az értékeket változtatás nélkül használja.

- **Szabályok sorrendje:** Az APIM szabályban a `<validate-jwt>`-t **mielőtt** bármilyen backend felé irányítás történik, helyezd el. Ellenkező esetben a hívások eljuthatnak az alkalmazáshoz érvényes token nélkül. Továbbá ügyelj arra, hogy a `<validate-jwt>` közvetlenül az `<inbound>` alatt legyen (ne legyen más feltételbe ágyazva), hogy az APIM alkalmazni tudja.

A fenti lépések követésével futtathatod a Spring AI MCP szervert Azure Container Apps-ben, és az Azure API Management minimális szabállyal ellenőrzi a bejövő OAuth2 JWT-ket. A legfontosabbak: tedd nyilvánosan elérhetővé a Spring Auth végpontokat TLS-sel, engedélyezd az OIDC felfedezést, és állítsd be az APIM `validate-jwt` szabályát az OpenID konfiguráció URL-jére (így automatikusan lekéri a JWKS-t). Ez a beállítás fejlesztési/tesztelési környezethez ideális; éles környezetben gondoskodj a titkok megfelelő kezeléséről, a tokenek élettartamáról és a JWKS kulcsok forgatásáról.
**Hivatkozások:** Lásd a Spring Authorization Server dokumentációját az alapértelmezett végpontokhoz ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) és az OIDC konfigurációhoz ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); lásd a Microsoft APIM dokumentációját a `validate-jwt` példákért ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); valamint az Azure Container Apps dokumentációját a telepítésről és tanúsítványokról ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.