# Spring AI MCP rakenduse juurutamine Azure Container Apps keskkonda

([Spring AI MCP serverite turvamine OAuth2-ga](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Joonis: Spring AI MCP server, mis on turvatud Spring Authorization Serveriga. Server väljastab klientidele juurdepääsutokenid ja valideerib neid sissetulevate päringute korral (allikas: Spring blogi) ([Spring AI MCP serverite turvamine OAuth2-ga](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP serveri juurutamiseks ehitage see konteinerina ja kasutage Azure Container Apps koos välise ingressiga. Näiteks Azure CLI abil saate käivitada:

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

See loob avalikult ligipääsetava Container Appi, millel on HTTPS lubatud (Azure väljastab tasuta TLS-sertifikaadi vaikimisi `*.azurecontainerapps.io` domeenile ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Apps keskkonnas | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Käskluse väljund sisaldab rakenduse FQDN-i (nt `my-mcp-app.eastus.azurecontainerapps.io`), mis muutub **issuer URL** baasiks. Veenduge, et HTTP ingress on lubatud (nagu eespool), et APIM saaks rakendusele ligi. Testi/arenduse seadistuses kasutage `--ingress external` valikut (või siduge kohandatud domeen TLS-iga vastavalt [Microsofti dokumentatsioonile](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Apps keskkonnas | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Salvestage kõik tundlikud omadused (nagu OAuth kliendi saladused) Container Apps salajastesse või Azure Key Vaulti ja kaardistage need konteinerisse keskkonnamuutujatena.

## Spring Authorization Serveri konfigureerimine

Lisage oma Spring Boot rakenduse koodi Spring Authorization Serveri ja Resource Serveri starterid. Konfigureerige `RegisteredClient` (arenduse/testi jaoks `client_credentials` grant) ja JWT võtmeallikas. Näiteks `application.properties` failis võite määrata:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Lubage Authorization Server ja Resource Server, määratledes turvafiltri ahela. Näiteks:

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

See seadistus avab vaikimisi OAuth2 lõpp-punktid: `/oauth2/token` tokenite jaoks ja `/oauth2/jwks` JSON Web Key Set jaoks. (Vaikimisi Springi `AuthorizationServerSettings` kaardistab `/oauth2/token` ja `/oauth2/jwks` ([Konfiguratsioonimudel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server väljastab JWT juurdepääsutokenid, mis on allkirjastatud ülaltoodud RSA võtmega, ja avaldab oma avaliku võtme aadressil `https://<your-app>:/oauth2/jwks`.

**Lubage OpenID Connect avastamine:** Et APIM saaks automaatselt hankida issueri ja JWKS-i, lubage OIDC pakkuja konfiguratsioonilõpp-punkt, lisades `.oidc(Customizer.withDefaults())` oma turvakonfiguratsiooni ([Konfiguratsioonimudel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Näiteks:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

See avab `/.well-known/openid-configuration`, mida APIM saab kasutada metaandmete jaoks. Lõpuks võite kohandada JWT **audience** väidet, et APIM-i `<audiences>` kontroll õnnestuks. Näiteks lisage tokeni kohandaja:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

See tagab, et tokenid sisaldavad `"aud": ["mcp-client"]`, mis vastab kliendi ID-le või ulatusele, mida APIM ootab.

## Tokeni ja JWKS lõpp-punktide avaldamine

Pärast juurutamist on teie rakenduse **issuer URL** `https://<app-fqdn>`, näiteks `https://my-mcp-app.eastus.azurecontainerapps.io`. Selle OAuth2 lõpp-punktid on:

- **Tokeni lõpp-punkt:** `https://<app-fqdn>/oauth2/token` – kliendid saavad siin tokenid (client_credentials voog).
- **JWKS lõpp-punkt:** `https://<app-fqdn>/oauth2/jwks` – tagastab JWK komplekti (APIM kasutab seda allkirjastusvõtmete hankimiseks).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC avastamise JSON (sisaldab `issuer`, `token_endpoint`, `jwks_uri` jne).

APIM osutab **OpenID konfiguratsiooni URL-ile**, kust see avastab `jwks_uri`. Näiteks, kui teie Container App FQDN on `my-mcp-app.eastus.azurecontainerapps.io`, siis APIM-i `<openid-config url="...">` peaks kasutama `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Vaikimisi määrab Spring selle metaandmetes `issuer` sama baas-URL-iga ([Konfiguratsioonimudel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Managementi konfigureerimine (`validate-jwt`)

Azure APIM-is lisage sissetulev poliitika, mis kasutab `<validate-jwt>` poliitikat sissetulevate JWT-de kontrollimiseks teie Spring Authorization Serveri vastu. Lihtsa seadistuse jaoks saate kasutada OpenID Connect metaandmete URL-i. Näide poliitika lõigust:

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

See poliitika ütleb APIM-ile, et see hangiks OpenID konfiguratsiooni Spring Auth Serverist, hangiks selle JWKS-i ja valideeriks, et iga token on allkirjastatud usaldusväärse võtmega ja omab õiget audience'i. (Kui jätate `<issuers>` välja, kasutab APIM metaandmetest automaatselt `issuer` väidet.) `<audience>` peaks vastama teie kliendi ID-le või API ressursi identifikaatorile tokenis (näites määrasime selle `"mcp-client"`). See on kooskõlas Microsofti dokumentatsiooniga `validate-jwt` kasutamise kohta `<openid-config>`-iga ([Azure API Management poliitika viide - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Pärast valideerimist edastab APIM päringu (sealhulgas algse `Authorization` päise) backendile. Kuna Springi rakendus on samuti ressursiserver, valideerib see tokeni uuesti, kuid APIM on juba taganud selle kehtivuse. (Arenduse jaoks võite tugineda APIM-i kontrollile ja keelata täiendavad kontrollid rakenduses, kui soovite, kuid turvalisem on mõlemad säilitada.)

## Näidisseaded

| Seade              | Näidisväärtus                                                       | Märkused                                   |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Teie Container Appi URL (baas-URI)         |
| **Tokeni lõpp-punkt** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Vaikimisi Springi tokeni lõpp-punkt ([Konfiguratsioonimudel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS lõpp-punkt**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Vaikimisi JWK komplekti lõpp-punkt ([Konfiguratsioonimudel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC avastamise dokument (automaatselt genereeritud)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth kliendi ID või API ressursi nimi     |
| **APIM poliitika**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` kasutab seda URL-i ([Azure API Management poliitika viide - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Levinud vead

- **HTTPS/TLS:** APIM gateway nõuab, et OpenID/JWKS lõpp-punkt oleks HTTPS-iga ja kehtiva sertifikaadiga. Vaikimisi pakub Azure Container Apps usaldusväärset TLS-sertifikaati Azure hallatud domeeni jaoks ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Apps keskkonnas | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kui kasutate kohandatud domeeni, veenduge, et sertifikaat on seotud (võite kasutada Azure'i tasuta hallatud sertifikaadi funktsiooni) ([Kohandatud domeeninimed ja tasuta hallatud sertifikaadid Azure Container Apps keskkonnas | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Kui APIM ei saa usaldada lõpp-punkti sertifikaati, ebaõnnestub `<validate-jwt>` metaandmete hankimine.

- **Lõpp-punkti ligipääsetavus:** Veenduge, et Springi rakenduse lõpp-punktid on APIM-ile ligipääsetavad. Kasutades `--ingress external` (või lubades ingressi portaalis) on kõige lihtsam. Kui valisite sisemise või vNet-põhise keskkonna, ei pruugi APIM (vaikimisi avalik) sellele ligi pääseda, kui see pole samas vNetis. Testi seadistuses eelistage avalikku ingressi, et APIM saaks kutsuda `.well-known` ja `/jwks` URL-e.

- **OpenID avastamine lubatud:** Vaikimisi ei **ava** Spring Authorization Server `/.well-known/openid-configuration`, kui OIDC pole lubatud. Veenduge, et lisate `.oidc(Customizer.withDefaults())` oma turvakonfiguratsiooni (vt eespool), et pakkuja konfiguratsioonilõpp-punkt oleks aktiivne ([Konfiguratsioonimudel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Vastasel juhul APIM-i `<openid-config>` kutse annab 404.

- **Audience väide:** Springi vaikimisi käitumine on määrata `aud` väide kliendi ID-le. Kui APIM-i `<audience>` kontroll ebaõnnestub, peate võib-olla kohandama tokenit (nagu eespool näidatud) või kohandama APIM-i poliitikat. Veenduge, et teie JWT audience vastab sellele, mida `<audience>`-is konfigureerite.

- **JSON metaandmete parsimine:** OpenID konfiguratsiooni JSON peab olema kehtiv. Springi vaikimisi konfiguratsioon väljastab standardse OIDC metaandmete dokumendi. Kontrollige, et see sisaldab õigeid `issuer` ja `jwks_uri` väärtusi. Kui hostite Springi proxy või teepõhise marsruudi taga, kontrollige metaandmetes olevaid URL-e. APIM kasutab neid väärtusi muutmata kujul.

- **Poliitika järjestus:** APIM-i poliitikas asetage `<validate-jwt>` **enne** mis tahes marsruutimist backendile. Vastasel juhul võivad kõned jõuda teie rakenduseni ilma kehtiva tokenita. Veenduge ka, et `<validate-jwt>` ilmub kohe `<inbound>` all (mitte pesastatud teise tingimuse sees), et APIM seda rakendaks.

Järgides ülaltoodud samme, saate käivitada oma Spring AI MCP serveri Azure Container Apps keskkonnas ja lasta Azure API Managementil valideerida sissetulevaid OAuth2 JWT-sid minimaalse poliitikaga. Olulised punktid on: avaldage Spring Auth lõpp-punktid avalikult TLS-iga, lubage OIDC avastamine ja suunake APIM-i `validate-jwt` OpenID konfiguratsiooni URL-ile (et see saaks JWKS-i automaatselt hankida). See seadistus sobib arenduse/testi keskkonnale; tootmises kaaluge korralikku saladuste haldamist, tokenite eluaegu ja JWKS-i võtmete pööramist vastavalt vajadusele.
**Viited:** Vaata Spring Authorization Server dokumentatsiooni vaikimisi lõpp-punktide kohta ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ja OIDC konfiguratsiooni kohta ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); vaata Microsoft APIM dokumentatsiooni `validate-jwt` näidete kohta ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ja Azure Container Apps dokumentatsiooni juurutamise ja sertifikaatide kohta ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.