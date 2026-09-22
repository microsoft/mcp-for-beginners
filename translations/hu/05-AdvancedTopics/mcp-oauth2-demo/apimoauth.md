# Spring AI MCP App telepítése az Azure Container Apps-be

> [!WARNING]
> Ez az egyesített autorizációs/erőforrás szerver tanulási és fejlesztési/tesztelési célokra készült. A gyártási rendszereknek különálló identitásszolgáltatót, állandó aláírási kulcsokat és kezelt titoktárolóban tárolt hitelesítő adatokat kell használniuk.
>  
> 

 ([Spring AI MCP szerverek OAuth2-vel történő biztonságossá tétele](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Ábra: Spring AI MCP szerver a Spring Authorization Server-rel védve. A szerver hozzáférési tokeneket állít ki az ügyfeleknek és azokat a bejövő kérések során érvényesíti (forrás: Spring blog) ([Spring AI MCP szerverek OAuth2-vel történő biztonságossá tétele](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* A Spring MCP szerver telepítéséhez építsd meg konténerként, és használd az Azure Container Apps-t külső bejárattal. Például az Azure CLI segítségével futtathatod:

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

Ez létrehoz egy nyilvánosan elérhető Container Appet HTTPS engedélyezéssel (az Azure ingyenes TLS tanúsítványt biztosít az alapértelmezett `*.azurecontainerapps.io` domainhez ([Egyéni domain nevek és ingyenes kezelt tanúsítványok az Azure Container Apps-ben | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). A parancs kimenete tartalmazza az alkalmazás FQDN-jét (pl. `my-mcp-app.eastus.azurecontainerapps.io`), amely az **issuer URL** alapjává válik. Győződj meg róla, hogy az HTTP ingress engedélyezve van (mint fent), hogy az APIM elérhesse az appot. Teszt/fejlesztési környezetben használd a `--ingress external` opciót (vagy kösd be a saját domained TLS-sel a [Microsoft dokumentáció] alapján ([Egyéni domain nevek és ingyenes kezelt tanúsítványok az Azure Container Apps-ben | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). A titkos adatokat (pl. OAuth kliens titkokat) tárold Container Apps titkokban vagy Azure Key Vault-ban, és térképezd be a konténer környezeti változóiként.

## Spring Authorization Server konfigurálása

A Spring Boot alkalmazásod kódjában add hozzá a Spring Authorization Server és Resource Server startereket. Konfigurálj egy `RegisteredClient`-et (fejlesztési/teszt környezetben `client_credentials` engedéllyel) és egy JWT kulcsforrást. Például az `application.properties` fájlban állíthatod be:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Engedélyezd az Authorization Server és Resource Server funkciókat egy biztonsági szűrőlánc definiálásával. Például:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Engedélyezze az Authorization Server végpontokat
            .apply(authzServer.and())
            // Engedélyezze a Resource Server-t (érkező kéréseken JWT érvényesítése)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Tiltsa le a CSRF-t (az MCP szerver nem böngésző alapú)
            .csrf(csrf -> csrf.disable())
            // Engedélyezze a CORS-t az ügyfél demo eszközök számára
            .cors(withDefaults());
        return http.build();
    }

    // Határozzon meg egy memóriában tárolt klienst (RegisteredClient) és egy JWK forrást:
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
        // Generáljon RSA kulcsot (fejlesztés/teszt esetén az indításkor újat generáljon)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ez a konfiguráció alapértelmezett OAuth2 végpontokat nyit: `/oauth2/token` a tokenek lekérésére és `/oauth2/jwks` a JSON Web Key Set lekérésére. (Alapértelmezés szerint a Spring `AuthorizationServerSettings` leképezi az `/oauth2/token` és `/oauth2/jwks` végpontokat ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) A szerver RSA kulccsal aláírt JWT hozzáférési tokeneket bocsát ki, és az nyilvános kulcsát elérhetővé teszi a `https://<your-app>:/oauth2/jwks` címen.

**OpenID Connect felfedezés engedélyezése:** Ahhoz, hogy az APIM automatikusan lekérhesse az issuer és JWKS adatokat, engedélyezni kell az OIDC szolgáltató konfigurációs végpontját azzal, hogy a biztonsági konfigurációban hozzáadod a `.oidc(Customizer.withDefaults())` elemet ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Például:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– engedélyezi a /.well-known/openid-configuration-t
```

Ez elérhetővé teszi a `/.well-known/openid-configuration` végpontot, amit az APIM metadata lekérésére használhat. Végül érdemes lehet testre szabni a JWT **audience** mezőt, hogy az APIM `<audiences>` ellenőrzése sikeres legyen. Például adj hozzá egy token testreszabót:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Állíts be egy egyedi közönséget (pl. az ügyfél azonosítója vagy az API azonosítója)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ez biztosítja, hogy a tokenek `"aud": ["mcp-client"]` értéket tartalmazzanak, ami megegyezik az APIM által elvárt kliensazonosítóval vagy jogosultsággal.

## Token és JWKS végpontok elérhetővé tétele

A telepítés után az alkalmazásod **issuer URL-je** a `https://<app-fqdn>`, például `https://my-mcp-app.eastus.azurecontainerapps.io`. OAuth2 végpontjai:

- **Token végpont:** `https://<app-fqdn>/oauth2/token` – itt kapnak tokeneket az ügyfelek (client_credentials folyamat).
- **JWKS végpont:** `https://<app-fqdn>/oauth2/jwks` – a JWK készletet szolgáltatja (amit az APIM használ az aláíró kulcsok lekérésére).
- **OpenID Konfiguráció:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC felfedező JSON (tartalmazza az `issuer`, `token_endpoint`, `jwks_uri` mezőket stb.).

Az APIM az **OpenID konfiguráció URL-re** mutat, amelyből felfedezi a `jwks_uri`-t. Például, ha a Container App FQDN-je `my-mcp-app.eastus.azurecontainerapps.io`, akkor APIM `<openid-config url="...">` elemében használja a `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` címet. (Alapértelmezés szerint a Spring az issuer-t is erre az alap URL-re állítja be ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management konfigurálása (`validate-jwt`)

Az Azure APIM-ben adj hozzá egy bejövő szabályt, amely `<validate-jwt>` elemet használ az érkező JWT-k ellenőrzésére a Spring Authorization Server alapján. Egy egyszerű beállításhoz használhatod az OpenID Connect metadata URL-t. Példa szabályrészlet:

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

Ez a szabály arra utasítja az APIM-et, hogy töltse le a Spring Auth Server OpenID konfigurációját, szerezze be a JWKS-t, és ellenőrizze, hogy minden token aláírása megbízható kulccsal történt-e, valamint hogy a célközönség helyes-e. (Ha kihagyod az `<issuers>` elemet, az APIM automatikusan a metadata `issuer` mezőjét fogja használni.) Az `<audience>` értékének meg kell egyeznie a tokenben lévő kliensazonosítóval vagy az API erőforrásával (példánkban `"mcp-client"`). Ez megfelel a Microsoft dokumentációjának arra a részére, amely a `<validate-jwt>` és `<openid-config>` használatát ismerteti ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Az érvényesítés után az APIM továbbítja a kérést (a eredeti `Authorization` fejlécet is beleértve) a háttérrendszernek. Mivel a Spring alkalmazás is erőforrás szerver, újra érvényesíti a tokent, de az APIM már biztosította annak érvényességét. (Fejlesztés alatt támaszkodhatsz az APIM ellenőrzésére és kikapcsolhatod az app további ellenőrzéseit, de biztonságosabb mindkettőt megtartani.)

## Példa beállítások

| Beállítás           | Példa érték                                                         | Megjegyzések                               |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | A Container App URL-je (alap URI)          |
| **Token végpont**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Alapértelmezett Spring token végpont ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS végpont**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Alapértelmezett JWK készlet végpont ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))     |
| **OpenID Konfig**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC felfedező dokumentum (automatikusan generált) |
| **APIM célközönség** | `mcp-client`                                                         | OAuth kliensazonosító vagy API név        |
| **APIM szabály**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | Ezt használja a `<validate-jwt>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Gyakori hibák

- **HTTPS/TLS:** Az APIM átjárónak HTTPS végpont szükséges érvényes tanúsítvánnyal az OpenID/JWKS eléréséhez. Alapértelmezésben az Azure Container Apps megbízható TLS tanúsítványt ad az Azure által kezelt domainhez ([Egyéni domain nevek és ingyenes kezelt tanúsítványok az Azure Container Apps-ben | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Egyéni domain használata esetén mindenképp kösd be a tanúsítványt (az Azure ingyenes kezelt tanúsítvány funkciója használható) ([Egyéni domain nevek és ingyenes kezelt tanúsítványok az Azure Container Apps-ben | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ha APIM nem bízik meg a végpont tanúsítványában, a `<validate-jwt>` sikertelen lesz a metadata lekérésében.

- **Végpont elérhetősége:** Győződj meg róla, hogy az APIM eléri a Spring alkalmazás végpontjait. A `--ingress external` opció (vagy portalon keresztüli ingress engedélyezése) a legegyszerűbb. Ha belső hálózaton vagy vNet-hez kötve telepíted, az APIM (alapértelmezett nyilvános) esetleg nem fogja elérni az appot, hacsak nem ugyanabban a VNet-ben található. Teszt környezetben érdemes nyilvános ingress-t használni, hogy az APIM elérje a `.well-known` és `/jwks` URL-eket.

- **OpenID Felfedezés engedélyezve:** Alapértelmezésben a Spring Authorization Server **nem teszi elérhetővé** a `/.well-known/openid-configuration` végpontot, hacsak nem engedélyezed az OIDC-t. Biztosítsd, hogy a biztonsági konfigurációban szerepel a `.oidc(Customizer.withDefaults())` (lásd fent), hogy a szolgáltató beállítási végpont aktív legyen ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ellenkező esetben az APIM `<openid-config>` hívás 404-es hibát ad.

- **Audience Claim:** A Spring alapértelmezett viselkedése, hogy az `aud` mezőt a kliensazonosítóra állítja. Ha az APIM `<audience>` ellenőrzése sikertelen, lehet, hogy testreszabni kell a tokent (ahogy fent mutattuk), vagy módosítani kell az APIM szabályt. Győződj meg róla, hogy a JWT audience megegyezik a `<audience>` konfigurációval.

- **JSON Metadata elemzés:** Az OpenID konfiguráció JSON-nek érvényesnek kell lennie. A Spring alapértelmezett konfigurációja szabványos OIDC metadata dokumentumot generál. Ellenőrizd, hogy tartalmazza a helyes `issuer` és `jwks_uri` mezőket. Ha proxy vagy útvonal alapú elérés mögé helyezed a Spring-et, ellenőrizd a metadata URL-eket. Az APIM ezeket használja változtatás nélkül.

- **Szabály sorrend:** Az APIM szabályban helyezd el a `<validate-jwt>` elemet **mielőtt** az átirányítás a backend felé megtörténik. Ellenkező esetben előfordulhat, hogy hívások érvényes token nélkül jutnak el az alkalmazáshoz. Továbbá győződj meg róla, hogy a `<validate-jwt>` közvetlenül az `<inbound>` alatt van (nem egy másik feltételben), hogy az APIM alkalmazni tudja.

A fenti lépések követésével futtathatod a Spring AI MCP szerveredet Azure Container Apps-ben, és az Azure API Management minimalista szabályokkal validálhatja a bejövő OAuth2 JWT-ket. A kulcsfontosságú pontok: a Spring Auth végpontok nyilvános elérése TLS-sel, az OIDC felfedezés engedélyezése, valamint az APIM `validate-jwt` irányítása az OpenID konfiguráció URL-je felé (hogy automatikusan lekérhesse a JWKS-t). Ez a konfiguráció fejlesztési/tesztelési környezethez alkalmas; éles használathoz fontold meg a titkok megfelelő kezelését, a token élettartamokat és a JWKS kulcsok rotációját szükség szerint.


**Hivatkozások:** Lásd a Spring Authorization Server dokumentációt az alapértelmezett végpontokhoz ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) és az OIDC konfigurációhoz ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); lásd a Microsoft APIM dokumentációt a `validate-jwt` példákhoz ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); valamint az Azure Container Apps dokumentációt a telepítéshez és tanúsítványokhoz ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->