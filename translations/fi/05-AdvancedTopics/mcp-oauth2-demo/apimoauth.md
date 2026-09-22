# Spring AI MCP -sovelluksen käyttöönotto Azure Container Apps -palvelussa

> [!WARNING]
> Tämä yhdistetty valtuutus-/resurssipalvelin on tarkoitettu oppimista ja
> kehitys-/testikäyttöä varten. Tuotantojärjestelmien tulisi käyttää omistettua identiteetin tarjoajaa,
> pysyviä allekirjoitusavaimia ja tunnistetietoja, jotka on tallennettu hallittuun salaisuuksien säilytykseen.

 ([Spring AI MCP -palvelimien suojaaminen OAuth2:lla](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Kuvassa: Spring AI MCP -palvelin suojattuna Spring Authorization Serverilla. Palvelin myöntää käyttöoikeustunnuksia asiakkaille ja validoi ne saapuvissa pyynnöissä (lähde: Spring blogi) ([Spring AI MCP -palvelimien suojaaminen OAuth2:lla](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP -palvelimen käyttöönottoa varten rakenna se kontiksi ja käytä Azure Container Appsia ulkoisella sisääntulolla. Esimerkiksi Azure CLI:llä voit ajaa:

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

Tämä luo julkisesti saavutettavan Container App -sovelluksen, jossa HTTPS on käytössä (Azure myöntää ilmaisen TLS-varmenteen oletusverkkotunnukselle `*.azurecontainerapps.io` ([Raikkaat verkkotunnukset ja ilmaiset hallitut varmenteet Azure Container Appsissa | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Komentotuloste sisältää sovelluksen FQDN:n (esim. `my-mcp-app.eastus.azurecontainerapps.io`), joka toimii **myöntäjän URL-pohjana**. Varmista, että HTTP-sisääntulo on käytössä (kuten yllä) jotta APIM pääsee sovellukseen. Testi-/kehitysympäristössä käytä `--ingress external` -vaihtoehtoa (tai määritä mukautettu verkkotunnus TLS:llä Microsoftin ohjeiden mukaan ([Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Raikkaat verkkotunnukset ja ilmaiset hallitut varmenteet Azure Container Appsissa | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Tallenna herkät tiedot (kuten OAuth-asiakassalaisuudet) Container Apps -salaisuuksiin tai Azure Key Vaultiin, ja map-paa ne konttiin ympäristömuuttujina.

## Spring Authorization Serverin määritys

Lisää Spring Boot -sovelluksesi koodiin Spring Authorization Server ja Resource Server -aloituspaketit. Määritä `RegisteredClient` (käyttämällä `client_credentials` -valtuutusta kehitys/testikäytössä) sekä JWT-avaimen lähde. Esimerkiksi `application.properties` tiedostossa voit asettaa:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Ota Authorization Server ja Resource Server käyttöön määrittämällä turvallisuusketju (security filter chain). Esimerkki:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Ota käyttöön valtuutuspalvelimen päätepisteet
            .apply(authzServer.and())
            // Ota käyttöön resurssipalvelin (vahvista JWT saapuvissa pyynnöissä)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Poista CSRF käytöstä (MCP-palvelin ei perustu selaimeen)
            .csrf(csrf -> csrf.disable())
            // Salli CORS asiakasdemotyökaluille
            .cors(withDefaults());
        return http.build();
    }

    // Määrittele muistissa oleva asiakas (RegisteredClient) ja JWK-lähde:
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
        // Luo RSA-avain (kehitys/testi, luo uudelleen käynnistyksessä)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Tämä kokoonpano paljastaa oletusarvoiset OAuth2-päätepisteet: `/oauth2/token` tunnuksia varten ja `/oauth2/jwks` JSON Web Key Setia varten. (Springin `AuthorizationServerSettings` mapittaa oletuksena `/oauth2/token` ja `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Palvelin myöntää RSA-avaimella allekirjoitettuja JWT-hyväksyntätunnuksia ja julkaisee julkisen avaimensa osoitteessa `https://<your-app>:/oauth2/jwks`.

**Ota käyttöön OpenID Connect -löytö:** Jotta APIM voi automaattisesti hakea myöntäjän ja JWKS:n, ota käyttöön OIDC-tarjoajan kokoonpano lisäämällä `.oidc(Customizer.withDefaults())` turvallisuusasetuksiin ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Esimerkiksi:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– ottaa käyttöön /.well-known/openid-configuration
```

Tämä julkaisee osoitteessa `/.well-known/openid-configuration`, jota APIM voi käyttää metatietojen hakemiseen. Lopuksi saatat haluta mukauttaa JWT:n **audience**-väitettä, jotta APIM:n `<audiences>`-tarkistus läpäisee. Lisää esimerkiksi tokenin muokkaaja:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Aseta mukautettu yleisö (esim. asiakas-ID tai API-tunniste)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tämä varmistaa, että tunnukset sisältävät `"aud": ["mcp-client"]`, joka vastaa APIM:n odottamaa asiakastunnusta tai laajuutta.

## Token- ja JWKS-päätepisteiden julkaiseminen

Käyttöönoton jälkeen sovelluksesi **myöntäjän URL** on `https://<app-fqdn>`, esim. `https://my-mcp-app.eastus.azurecontainerapps.io`. OAuth2-päätepisteet ovat:

- **Token-päätepiste:** `https://<app-fqdn>/oauth2/token` – asiakkaat hakevat tunnuksia täältä (client_credentials-flown yhteydessä).
- **JWKS-päätepiste:** `https://<app-fqdn>/oauth2/jwks` – palauttaa JWK-setin (käytetään APIM:ssä allekirjoitusavaimien hakemiseen).
- **OpenID-asetukset:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC-löytö JSON (sisältää `issuer`, `token_endpoint`, `jwks_uri` jne.).

APIM osoittaa **OpenID-konfiguraatio-URL:**iin, josta se löytää `jwks_uri`:n. Esimerkiksi, jos Container App FQDN on `my-mcp-app.eastus.azurecontainerapps.io`, APIM:n `<openid-config url="...">` tulisi käyttää `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Spring asettaa oletuksena `issuer`-kentän samaan perus-URL:iin ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Managementin määritys (`validate-jwt`)

Lisää Azure APIM:iin saapuva politiikka, joka käyttää `<validate-jwt>` -politiikkaa tarkistamaan saapuvat JWT:t Spring Authorization Serveriasi vastaan. Yksinkertaisessa asennossa voit käyttää OpenID Connect -metatietojen URL:ia. Esimerkki politiikan osasta:

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

Tämä politiikka käskee APIM:iä hakemaan OpenID-konfiguraation Spring Auth Serverilta, hakemaan JWKS:n ja validoimaan, että jokainen tunnus on allekirjoitettu luotetulla avaimella ja että sillä on oikea tuotejoukko. (Jos jätät `<issuers>` pois, APIM käyttää automaattisesti metadatan `issuer`-väitettä.) `<audience>` tulisi vastata asiakastunnustasi tai API-resurssin tunnistetta tunnuksessa (esimerkissämme asetimme sen `"mcp-client"`). Tämä on linjassa Microsoftin dokumentaation kanssa `validate-jwt`-käytöstä `<openid-config>` kanssa ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Vahvistuksen jälkeen APIM välittää pyynnön edelleen (sisältäen alkuperäisen `Authorization`-otsikon) backendille. Koska Spring-sovellus on myös resurssipalvelin, se validoi tunnuksen uudelleen, mutta APIM on jo varmistanut sen kelvollisuuden. (Kehityksessä voit luottaa APIM:n tarkistukseen ja poistaa lisätarkistukset sovelluksesta, mutta molempien pitäminen on turvallisempaa.)

## Esimerkkiasetukset

| Asetus             | Esimerkkiarvo                                                      | Huomautuksia                                 |
|--------------------|--------------------------------------------------------------------|---------------------------------------------|
| **Myöntäjä**       | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | Container Appisi URL (perus-URI)             |
| **Token-päätepiste** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Oletus Springin token-päätepiste ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS-päätepiste** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Oletus JWK Set -päätepiste ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **OpenID-config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC-löytödokumentti (automaattisesti luotu)  |
| **APIM audience**  | `mcp-client`                                                       | OAuth-asiakastunnus tai API-resurssin nimi  |
| **APIM-politiikka** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` käyttää tätä URL:ia ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Yleiset sudenkuopat

- **HTTPS/TLS:** APIM-portaali vaatii, että OpenID/JWKS-päätepiste käyttää HTTPS:ää kelvollisella varmenteella. Oletuksena Azure Container Apps tarjoaa luotettavan TLS-varmenteen Azure-hallinnoidulle verkkotunnukselle ([Raikkaat verkkotunnukset ja ilmaiset hallitut varmenteet Azure Container Appsissa | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jos käytät mukautettua verkkotunnusta, varmista että varmenne on sidottu oikein (voit käyttää Azuren ilmaista hallittua varmennetta) ([Raikkaat verkkotunnukset ja ilmaiset hallitut varmenteet Azure Container Appsissa | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jos APIM ei voi luottaa päätepisteen varmenteeseen, `<validate-jwt>` epäonnistuu metadatan haussa.

- **Päätepisteiden saatavuus:** Varmista, että Spring-sovelluksen päätepisteet ovat APIM:stä saavutettavissa. `--ingress external`-vaihtoehdon käyttö (tai sisääntulon aktivointi portaalissa) on helpoin tapa. Jos käytät sisäistä tai vNetiin sidottua ympäristöä, APIM (joka on oletuksena julkinen) ei välttämättä pääse siihen, ellei se ole samassa VNetissä. Testikäytössä suositaan julkista sisääntuloa, jotta APIM voi kutsua `.well-known` ja `/jwks` URL-osoitteita.

- **OpenID-löytö käytössä:** Oletuksena Spring Authorization Server **ei julkaise** `/.well-known/openid-configuration` -polkua, ellei OIDC-ominaisuus ole käytössä. Muista sisällyttää `.oidc(Customizer.withDefaults())` turva-asetuksiin (ks. yllä), jotta tarjoajan kokoonpano on käytössä ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Muuten APIM:n `<openid-config>` kutsu palauttaa 404:n.

- **Audience-väite:** Springin oletuskäyttäytyminen on asettaa `aud`-väite asiakastunnukseksi. Jos APIM:n `<audience>` tarkistus epäonnistuu, sinun saattaa olla tarpeen mukauttaa tokenia (kuten yllä) tai säätää APIM-politiikkaa. Varmista, että tokenin audience vastaa sitä, minkä määrität `<audience>`-kentässä.

- **JSON-metadatan jäsentäminen:** OpenID-konfiguraation JSON:n tulee olla kelvollinen. Springin oletusasetukset tuottavat standardin OIDC-metadokumentin. Tarkista, että se sisältää oikeat arvot `issuer` ja `jwks_uri`. Jos isännöit Springiä proxyn tai polkuperusteisen reitin takana, tarkista URL:t tässä metadatassa. APIM käyttää arvoja sellaisenaan.

- **Politiikan järjestys:** APIM-politiikassa sijoita `<validate-jwt>` **ennen** mitään reititystä backendille. Muuten kutsut voivat saavuttaa sovelluksen ilman kelvollista tunnusta. Varmista lisäksi, että `<validate-jwt>` on heti `<inbound>`-lohkon alla (ei toisten ehtojen sisällä), jotta APIM soveltaa sitä.

Noudattamalla yllä olevia ohjeita voit ajaa Spring AI MCP -palvelimesi Azure Container Appsissa ja antaa Azure API Managementin validoida saapuvat OAuth2 JWT -tunnukset minimipolitiikalla. Keskeiset kohdat ovat: paljasta Spring Auth -päätepisteet julkisesti TLS:llä, ota käyttöön OIDC-löytö ja suuntaa APIM:n `validate-jwt` OpenID-konfiguraatio-URL:iin (jotta se voi hakea JWKS:n automaattisesti). Tämä kokoonpano sopii kehitys-/testiympäristöön; tuotantoon harkitse asianmukaista salaisuudenhallintaa, tunnusten elinaikoja ja JWKS-avainten kierrätystä tarpeen mukaan.


**Viitteet:** Katso Spring Authorization Server -dokumentaatio oletuspäätteistä ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ja OIDC-konfiguraatiosta ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); katso Microsoft APIM -dokumentaatio `validate-jwt` -esimerkeistä ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ja Azure Container Apps -dokumentaatio käyttöönotosta ja sertifikaateista ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->