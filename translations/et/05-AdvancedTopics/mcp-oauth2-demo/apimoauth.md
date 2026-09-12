# Spring AI MCP rakenduse juurutamine Azure Container Apps keskkonda

> [!WARNING]
> See kombineeritud autoriseerimis-/ressursiserver on mõeldud õppimiseks ja arendus-/testkasutuseks.
> Tootmiskeskkondades tuleks kasutada spetsiaalset identiteedipakkujat,
> püsivaid allkirjastamisvõtmeid ja volitusi, mis on hoitud hallatavas salajases poest.

 ([Spring AI MCP serverite turvamine OAuth2-ga](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Joonis: Spring AI MCP server, mis on kaitstud Spring Authorization Serveriga. Server väljastab kliendile ligipääsutokeneid ja kontrollib neid sissetulevatel päringutel (allikas: Spring blogi) ([Spring AI MCP serverite turvamine OAuth2-ga](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP serveri juurutamiseks ehitage see konteineriks ja kasutage Azure Container Appsi koos välise sisenemisega. Näiteks Azure CLI-ga saate käivitada:

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

See loob avalikult ligipääsetava Container App-i HTTPS-iga (Azure väljastab tasuta TLS-sertifikaadi vaikimisi `*.azurecontainerapps.io` domeeniks ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Appsis | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Käsu väljundis on rakenduse FQDN (nt `my-mcp-app.eastus.azurecontainerapps.io`), mis saab olema **väljastaja URL-i** alus. Veenduge, et HTTP sisenemine on lubatud (nagu eespool), et APIM saaks rakendusele ligi. Test-/arenduskeskkonnas kasutage `--ingress external` valikut (või siduge kohandatud domeen TLS-iga vastavalt [Microsofti dokumentatsioonile](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Appsis | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Hoidke kõik tundlikud omadused (nt OAuth kliendisaladused) Container Appsi saladustes või Azure Key Vaultis ning kaardistage need konteinerisse keskkonnamuutujatena.

## Spring Authorization Serveri konfigureerimine

Lisage oma Spring Boot rakenduse koodi Spring Authorization Serveri ja Resource Serveri starterid. Konfigureerige `RegisteredClient` (arendus-/testkeskkonnas `client_credentials` grant-tüüp) ja JWT võtmeallikas. Näiteks võite `application.properties` failis seada:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Lubage Authorization Server ja Resource Server, määrates turvafiltri ketti. Näiteks:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Luba autoriseerimiserveri lõpp-punktid
            .apply(authzServer.and())
            // Luba ressursiserver (kontrolli sissetulevaid päringuid JWT abil)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Keela CSRF (MCP server ei põhine brauseril)
            .csrf(csrf -> csrf.disable())
            // Luba CORS kliendi demo tööriistadele
            .cors(withDefaults());
        return http.build();
    }

    // Määra mälus olev klient (RegisteredClient) ja JWK allikas:
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
        // Genereeri RSA võti (arenduseks/testimiseks, genereeri iga käivitusega uus)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

See seadistus avab vaikimisi OAuth2 otspunktid: `/oauth2/token` tokenite saamiseks ja `/oauth2/jwks` JSON Web Key Seti pärimiseks. (Vaikimisi seab Spring `AuthorizationServerSettings` `/oauth2/token` ja `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server väljastab JWT ligipääsutokeneid, mis on allkirjastatud ülaltoodud RSA võtmega ja avaldab oma avaliku võtme aadressil `https://<your-app>:/oauth2/jwks`.

**Lubage OpenID Connecti avastamine:** Selleks, et APIM saaks automaatselt väljastajat ja JWKS-i hankida, lubage OIDC pakkuja konfigureerimise otspunkt, lisades `.oidc(Customizer.withDefaults())` oma turvakonfiguratsiooni ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Näiteks:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– lubab /.well-known/openid-configuration
```

See avab `/.well-known/openid-configuration`, mida APIM saab kasutada metaandmete jaoks. Lõpuks võite soovida kohandada JWT **audience** claim-i, et APIM-i `<audiences>` kontroll peaks läbi. Näiteks lisage tokeni kohandaja:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Määra kohandatud sihtgrupp (nt kliendi ID või API identifikaator)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

See tagab, et tokenid kannavad `"aud": ["mcp-client"]`, mis vastab kliendi ID-le või APIM-i oodatud õigustele.

## Tokeni ja JWKS otspunktide avalikustamine

Pärast juurutamist on teie rakenduse **väljastaja URL** `https://<app-fqdn>`, nt `https://my-mcp-app.eastus.azurecontainerapps.io`. Selle OAuth2 otspunktid on:

- **Tokeni otspunkt:** `https://<app-fqdn>/oauth2/token` – tokenite saamiseks klientide poolt (client_credentials voog).
- **JWKS otspunkt:** `https://<app-fqdn>/oauth2/jwks` – tagastab JWK komplekti (APIM kasutab allkirjavõtmete hankimiseks).
- **OpenID konfiguratsioon:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC avastus JSON (sisaldab `issuer`, `token_endpoint`, `jwks_uri` jne).  

APIM osutab **OpenID konfiguratsiooni URL-ile**, kust ta avastab `jwks_uri`. Näiteks kui teie Container Appi FQDN on `my-mcp-app.eastus.azurecontainerapps.io`, peaks APIM-i `<openid-config url="...">` kasutama `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Vaikimisi seab Spring selle metaandmete `issuer` samale baas-URL-ile ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Managementu konfigureerimine (`validate-jwt`)

Azure APIM-is lisage sissetulev poliitika, mis kasutab `<validate-jwt>` poliitikat, et kontrollida sissetulevaid JWT-sid teie Spring Authorization Serveri vastu. Lihtsaks seadistuseks võite kasutada OpenID Connect metaandmete URL-i. Näidis poliitika fragment:

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

See poliitika ütleb APIM-ile, et ta hangib Spring Authorization Serverist OpenID konfiguratsiooni, teeb JWKS päringu ja kontrollib, et iga token on allkirjastatud usaldusväärse võtmega ning tal on õige sihtrühm. (Kui `<issuers>` jäetakse välja, kasutab APIM automaatselt metaandmetest `issuer` claim-i.) `<audience>` peaks vastama teie kliendi ID-le või API ressurssi identifikaatorile tokenis (ülaltoodud näites on see `"mcp-client"`). See vastab Microsofti dokumentatsioonile `validate-jwt` kasutamise kohta koos `<openid-config>`-iga ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Pärast valideerimist edastab APIM päringu (sh originaalse `Authorization` päise) backendile. Kuna Spring rakendus on ka ressursiserver, valideerib see tokeni uuesti, kuid APIM on juba taganud selle kehtivuse. (Arenduses võite tugineda APIM-i kontrollile ja soovi korral rakenduses täiendavad kontrollid keelata, kuid turvalisem on säilitada mõlemad.)

## Näidis seaded

| Seade             | Näidisväärtus                                                     | Märkused                                   |
|--------------------|------------------------------------------------------------------|--------------------------------------------|
| **Väljastaja**     | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | Teie Container Appi URL (baas URI)          |
| **Tokeni otspunkt**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Vaikimisi Springi tokeni otspunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS otspunkt** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Vaikimisi JWK komplekti otspunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID konfiguratsioon** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC avastusdokument (automaatselt genereeritud)  |
| **APIM-i sihtrühm**  | `mcp-client`                                                      | OAuth kliendi ID või API ressurssi nimi     |
| **APIM poliitika**  | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` kasutab seda URL-i ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Levinud probleemid

- **HTTPS/TLS:** APIM värav nõuab, et OpenID/JWKS otspunkt oleks HTTPS-i ja kehtiva sertifikaadiga. Vaikimisi pakub Azure Container Apps usaldusväärset TLS sertifikaati Azure'i hallataval domeenil ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Appsis | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kui kasutate kohandatud domeeni, veenduge sertifikaadi sidumises (võite kasutada Azure tasuta hallatavat sertifikaadi teenust) ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Appsis | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kui APIM ei saa usaldada otspunkti sertifikaati, ebaõnnestub `<validate-jwt>` metaandmete hankimine.

- **Otspunkti ligipääsetavus:** Veenduge, et Spring rakenduse otspunktid oleksid APIM-ist ligipääsetavad. Lihtsaim on kasutada `--ingress external` (või sisenemise lubamine portaalis). Kui valisite sisemise või vNet piiritletud keskkonna, ei pruugi APIM (vaikimisi avalik) sinna ligi pääseda, kui see pole samas VNetis. Testimiskeskkonnas eelistage avalikku sisenemist, et APIM pääseks ligi `.well-known` ja `/jwks` URL-idele.

- **OpenID avastus on lubatud:** Vaikimisi ei avalda Spring Authorization Server `/.well-known/openid-configuration` väljaspool OIDC lubamist. Veenduge, et lisate `.oidc(Customizer.withDefaults())` oma turvakonfiguratsiooni (vt eespool), et pakkuja konfigureerimise otspunkt oleks aktiivne ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Vastasel korral tagastab APIM-i `<openid-config>` kõne 404.

- **Sihtrühma claim:** Spring vaikimisi seab `aud` claimiks kliendi ID. Kui APIM-i `<audience>` kontroll ebaõnnestub, peate võib-olla tokenit kohandama (nagu eespool näidatud) või APIM poliitikat muutma. Tagage, et JWT-s olev sihtrühm vastab teie `<audience>` seadele.

- **JSON metaandmete töötlemine:** OpenID konfiguratsiooni JSON peab olema kehtiv. Springi vaikimisi konfiguratsioon genereerib standardse OIDC metaandmete dokumendi. Kontrollige, et see sisaldab õiget `issuer` ja `jwks_uri`. Kui hostite Springi proxy või teepõhise marsruudi taga, kontrollige tähelepanelikult nende metaandmete URL-e. APIM kasutab neid väärtusi täpselt nii nagu on.

- **Poliitika järjekord:** APIM poliitikas paigutage `<validate-jwt>` **enne** kõiki taustateenuste marsruute. Vastasel korral võivad kõned ilma kehtiva tokenita teie rakendusse jõuda. Samuti veenduge, et `<validate-jwt>` oleks kõnealuse `<inbound>` sõlme all kohe (mitte mõne teise tingimuse sees), nii rakendab APIM seda korrektselt.

Järgides ülaltoodud samme, saate käivitada oma Spring AI MCP serveri Azure Container Appsis ning Azure API Management valideerib sisenevad OAuth2 JWT-d minimaalse poliitikaga. Peamised punktid on: avage Springi autentimisotspunktid avalikult TLS-iga, lubage OIDC avastus ja osutage APIM-i `validate-jwt` OpenID konfi URL-ile (et ta saaks JWKS-i automaatselt pärida). See seadistus sobib arendus-/testkeskkonnale; tootmises kaaluge sidebarimajandust, tokenite kestvust ja võtmete pööramist JWKS-is vastavalt vajadusele.


**Viited:** Vaadake Spring Authorization Serveri dokumentatsiooni vaikeotsapunktide kohta ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ja OIDC konfiguratsiooni kohta ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); vaadake Microsofti APIM dokumentatsiooni `validate-jwt` näidete jaoks ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ja Azure Container Appsi dokumentatsiooni juurutamise ja sertifikaatide kohta ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->