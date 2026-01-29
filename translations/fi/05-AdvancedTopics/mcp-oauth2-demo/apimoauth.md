# Spring AI MCP -sovelluksen käyttöönotto Azure Container Appsissa

 ([Spring AI MCP -palvelimien suojaaminen OAuth2:lla](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Kuva: Spring AI MCP -palvelin suojattuna Spring Authorization Serverilla. Palvelin myöntää käyttöoikeustunnuksia asiakkaille ja validoi ne saapuvissa pyynnöissä (lähde: Spring blogi) ([Spring AI MCP -palvelimien suojaaminen OAuth2:lla](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP -palvelimen käyttöönottoa varten rakenna se kontiksi ja käytä Azure Container Appsia ulkoisella ingressillä. Esimerkiksi Azure CLI:llä voit ajaa:

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

Tämä luo julkisesti saavutettavan Container Appin, jossa HTTPS on käytössä (Azure myöntää ilmaisen TLS-varmenteen oletusalueelle `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Komennon tuloste sisältää sovelluksen FQDN:n (esim. `my-mcp-app.eastus.azurecontainerapps.io`), joka toimii **issuer URL** -perusosoitteena. Varmista, että HTTP-ingress on käytössä (kuten yllä), jotta APIM pääsee sovellukseen käsiksi. Testi- tai kehitysympäristössä käytä `--ingress external` -valitsinta (tai sido mukautettu domain TLS:llä Microsoftin ohjeiden mukaan ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Tallenna kaikki arkaluontoiset tiedot (kuten OAuth-asiakassalaisuudet) Container Appsin salaisuuksiin tai Azure Key Vaultiin ja liitä ne konttiin ympäristömuuttujina.

## Spring Authorization Serverin konfigurointi

Spring Boot -sovelluksesi koodissa lisää Spring Authorization Serverin ja Resource Serverin starterit. Määritä `RegisteredClient` (kehitys/testiympäristössä `client_credentials` -myöntämiselle) ja JWT-avaimen lähde. Esimerkiksi `application.properties` -tiedostossa voit asettaa:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Ota Authorization Server ja Resource Server käyttöön määrittelemällä security filter chain. Esimerkiksi:

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

Tämä kokoonpano paljastaa oletusarvoiset OAuth2-päätepisteet: `/oauth2/token` tunnuksia varten ja `/oauth2/jwks` JSON Web Key Setiä varten. (Springin `AuthorizationServerSettings` oletuksena kartoittaa `/oauth2/token` ja `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Palvelin myöntää RSA-avaimella allekirjoitettuja JWT-käyttöoikeustunnuksia ja julkaisee julkisen avaimesi osoitteessa `https://<your-app>:/oauth2/jwks`.

**Ota OpenID Connect -löytö käyttöön:** Jotta APIM voi automaattisesti hakea issuerin ja JWKS:n, ota OIDC-providerin konfigurointipäätepiste käyttöön lisäämällä `.oidc(Customizer.withDefaults())` turva-asetuksiin ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Esimerkiksi:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Tämä paljastaa `/.well-known/openid-configuration` -polun, jota APIM voi käyttää metatietojen hakemiseen. Lopuksi voit halutessasi mukauttaa JWT:n **audience**-väitettä, jotta APIM:n `<audiences>`-tarkistus menee läpi. Lisää esimerkiksi tokenin mukauttaja:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tämä varmistaa, että tunnukset sisältävät `"aud": ["mcp-client"]`, joka vastaa APIM:n odottamaa asiakastunnusta tai scopea.

## Token- ja JWKS-päätepisteiden paljastaminen

Käyttöönoton jälkeen sovelluksesi **issuer URL** on `https://<app-fqdn>`, esim. `https://my-mcp-app.eastus.azurecontainerapps.io`. Sen OAuth2-päätepisteet ovat:

- **Token-päätepiste:** `https://<app-fqdn>/oauth2/token` – asiakkaat hakevat tunnuksia tästä (client_credentials -virtaus).
- **JWKS-päätepiste:** `https://<app-fqdn>/oauth2/jwks` – palauttaa JWK-setin (APIM käyttää tätä allekirjoitusavainten hakemiseen).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC-löytödokumentti JSON-muodossa (sisältää `issuer`, `token_endpoint`, `jwks_uri` jne.).

APIM osoittaa **OpenID-konfiguraatio-URL:iin**, josta se löytää `jwks_uri`:n. Esimerkiksi, jos Container Appin FQDN on `my-mcp-app.eastus.azurecontainerapps.io`, APIM:n `<openid-config url="...">` tulisi käyttää `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Spring asettaa oletuksena `issuer`-kentän samaan perusosoitteeseen ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Managementin (`validate-jwt`) konfigurointi

Azure APIM:ssä lisää inbound-politiikka, joka käyttää `<validate-jwt>` -politiikkaa tarkistamaan saapuvat JWT:t Spring Authorization Serveriasi vastaan. Yksinkertaisessa kokoonpanossa voit käyttää OpenID Connect -metatietojen URL:ia. Esimerkkipolitiikka:

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

Tämä politiikka ohjeistaa APIM:ää hakemaan OpenID-konfiguraation Spring Auth Serverilta, noutamaan sen JWKS:n ja validoimaan, että jokainen tunnus on allekirjoitettu luotetulla avaimella ja että sillä on oikea audience. (Jos jätät pois `<issuers>`, APIM käyttää automaattisesti metatiedoista löytyvää `issuer`-väitettä.) `<audience>` tulisi vastata asiakastunnustasi tai API-resurssin tunnistetta tokenissa (esimerkissä asetimme sen arvoon `"mcp-client"`). Tämä on yhdenmukaista Microsoftin dokumentaation kanssa `validate-jwt`-käytöstä `<openid-config>` kanssa ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Validoinnin jälkeen APIM välittää pyynnön (mukaan lukien alkuperäisen `Authorization`-otsikon) backendille. Koska Spring-sovellus toimii myös resurssipalvelimena, se validoi tunnuksen uudelleen, mutta APIM on jo varmistanut sen pätevyyden. (Kehityksessä voit luottaa APIM:n tarkistukseen ja poistaa sovelluksen lisätarkistukset, mutta turvallisempaa on pitää molemmat käytössä.)

## Esimerkkiasetukset

| Asetus             | Esimerkkiarvo                                                      | Huomautukset                                |
|--------------------|-------------------------------------------------------------------|---------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | Container Appin URL (perus-URI)             |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Oletusarvoinen Spring token-päätepiste ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Oletusarvoinen JWK Set -päätepiste ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC-löytödokumentti (automaattisesti luotu) |
| **APIM audience**  | `mcp-client`                                                      | OAuth-asiakastunnus tai API-resurssin nimi |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` käyttää tätä URL:ia ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Yleisiä sudenkuoppia

- **HTTPS/TLS:** APIM-portaali vaatii, että OpenID/JWKS-päätepiste on HTTPS:llä ja sillä on voimassa oleva varmenne. Azure Container Apps tarjoaa oletuksena luotettavan TLS-varmenteen Azure-hallinnoidulle domainille ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jos käytät omaa domainia, muista sitoa varmenne (voit käyttää Azuren ilmaista hallittua varmenteen ominaisuutta) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Jos APIM ei voi luottaa päätepisteen varmenteeseen, `<validate-jwt>` epäonnistuu metatietojen hakemisessa.

- **Päätepisteiden saavutettavuus:** Varmista, että Spring-sovelluksen päätepisteet ovat APIM:n saavutettavissa. `--ingress external` (tai ingressin aktivointi portaalissa) on helpoin tapa. Jos valitsit sisäisen tai vNet-rajatun ympäristön, APIM (joka on oletuksena julkinen) ei välttämättä pääse siihen käsiksi, ellei se ole samassa vNetissä. Testiympäristössä suositaan julkista ingressiä, jotta APIM voi kutsua `.well-known` ja `/jwks` -URL-osoitteita.

- **OpenID-löytö käytössä:** Spring Authorization Server **ei oletuksena paljasta** `/.well-known/openid-configuration` -polkua, ellei OIDC ole otettu käyttöön. Muista lisätä `.oidc(Customizer.withDefaults())` turva-asetuksiin (ks. yllä), jotta providerin konfigurointipäätepiste aktivoituu ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Muuten APIM:n `<openid-config>`-kutsu palauttaa 404:n.

- **Audience-väite:** Spring asettaa oletuksena `aud`-väitteen asiakastunnukseksi. Jos APIM:n `<audience>`-tarkistus epäonnistuu, sinun täytyy mukauttaa tokenia (kuten yllä) tai säätää APIM-politiikkaa. Varmista, että JWT:n audience vastaa sitä, mitä määrittelet `<audience>`-kentässä.

- **JSON-metatietojen jäsentäminen:** OpenID-konfiguraation JSON:n tulee olla kelvollinen. Springin oletuskonfiguraatio tuottaa standardin OIDC-metatietodokumentin. Tarkista, että se sisältää oikeat `issuer` ja `jwks_uri` -arvot. Jos isännöit Springiä proxyn tai polkuun perustuvan reitityksen takana, tarkista URL-osoitteet huolellisesti. APIM käyttää näitä arvoja sellaisenaan.

- **Politiikan järjestys:** APIM-politiikassa sijoita `<validate-jwt>` **ennen** backendille reititystä. Muuten kutsut voivat tavoittaa sovelluksen ilman voimassa olevaa tunnusta. Varmista myös, että `<validate-jwt>` on heti `<inbound>`-elementin alla (ei sisäkkäin toisen ehdon kanssa), jotta APIM soveltaa sitä oikein.

Noudattamalla yllä olevia ohjeita voit ajaa Spring AI MCP -palvelimesi Azure Container Appsissa ja antaa Azure API Managementin validoida saapuvat OAuth2 JWT:t minimipolitiikalla. Keskeiset asiat ovat: paljasta Spring Auth -päätepisteet julkisesti TLS:llä, ota OIDC-löytö käyttöön ja osoita APIM:n `validate-jwt` OpenID-konfiguraatio-URL:iin (jotta se voi hakea JWKS:n automaattisesti). Tämä kokoonpano sopii kehitys- ja testausympäristöön; tuotantoon kannattaa harkita asianmukaista salaisuuksien hallintaa, tokenien elinaikoja ja avainten kierrätystä JWKS:ssä tarpeen mukaan.
**Viitteet:** Katso Spring Authorization Server -dokumentaatiosta oletuspäätepisteet ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ja OIDC-konfiguraatio ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); katso Microsoft APIM -dokumentaatiosta `validate-jwt`-esimerkkejä ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); sekä Azure Container Apps -dokumentaatiosta käyttöönotto ja sertifikaatit ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.