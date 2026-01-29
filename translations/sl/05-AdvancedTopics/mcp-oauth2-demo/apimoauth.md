# Namestitev aplikacije Spring AI MCP na Azure Container Apps

([Zavarovanje Spring AI MCP strežnikov z OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Slika: Spring AI MCP strežnik zavarovan s Spring Authorization Server. Strežnik izdaja dostopne žetone strankam in jih preverja pri dohodnih zahtevah (vir: Spring blog) ([Zavarovanje Spring AI MCP strežnikov z OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Za namestitev Spring MCP strežnika ga zgradite kot vsebnik in uporabite Azure Container Apps z zunanjim dostopom. Na primer, z uporabo Azure CLI lahko zaženete:

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

S tem ustvarite javno dostopno Container App z omogočenim HTTPS (Azure izda brezplačen TLS certifikat za privzeto domeno `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Izhod ukaza vključuje FQDN aplikacije (npr. `my-mcp-app.eastus.azurecontainerapps.io`), ki postane osnova za **issuer URL**. Poskrbite, da je omogočen HTTP ingress (kot zgoraj), da lahko APIM dostopa do aplikacije. V testnem/razvojnem okolju uporabite možnost `--ingress external` (ali povežite lastno domeno z TLS po [Microsoft dokumentaciji](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Vse občutljive lastnosti (kot so skrivnosti OAuth klienta) shranjujte v Container Apps secrets ali Azure Key Vault in jih preslikajte v vsebnik kot okoljske spremenljivke.

## Konfiguracija Spring Authorization Server

V kodi vaše Spring Boot aplikacije vključite Spring Authorization Server in Resource Server starterje. Konfigurirajte `RegisteredClient` (za `client_credentials` grant v razvoju/testiranju) in vir ključev JWT. Na primer, v `application.properties` lahko nastavite:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Omogočite Authorization Server in Resource Server z definiranjem varnostnega filtra. Na primer:

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

Ta nastavitev bo izpostavila privzete OAuth2 končne točke: `/oauth2/token` za žetone in `/oauth2/jwks` za JSON Web Key Set. (Privzeto Springjeva `AuthorizationServerSettings` preslika `/oauth2/token` in `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Strežnik bo izdajal JWT dostopne žetone, podpisane z zgoraj navedenim RSA ključem, in objavil svoj javni ključ na `https://<your-app>:/oauth2/jwks`.

**Omogočite OpenID Connect odkrivanje:** Da lahko APIM samodejno pridobi issuer in JWKS, omogočite OIDC provider konfiguracijsko končno točko z dodajanjem `.oidc(Customizer.withDefaults())` v vašo varnostno konfiguracijo ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Na primer:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

To izpostavi `/.well-known/openid-configuration`, ki ga APIM lahko uporabi za metapodatke. Nazadnje boste morda želeli prilagoditi JWT **audience** claim, da bo APIM-ov `<audiences>` preverjanje uspešno. Na primer, dodajte prilagoditev žetona:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

S tem zagotovite, da žetoni vsebujejo `"aud": ["mcp-client"]`, kar ustreza ID-ju klienta ali obsegu, ki ga APIM pričakuje.

## Izpostavitev Token in JWKS končnih točk

Po namestitvi bo vaš aplikacijski **issuer URL** `https://<app-fqdn>`, npr. `https://my-mcp-app.eastus.azurecontainerapps.io`. Njegove OAuth2 končne točke so:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – tukaj stranke pridobijo žetone (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – vrne JWK set (APIM ga uporablja za pridobivanje podpisnih ključev).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC odkrivanje v JSON obliki (vsebuje `issuer`, `token_endpoint`, `jwks_uri` itd.).

APIM bo usmeril na **OpenID configuration URL**, od koder bo odkril `jwks_uri`. Na primer, če je FQDN vaše Container App `my-mcp-app.eastus.azurecontainerapps.io`, potem naj APIM-ov `<openid-config url="...">` uporablja `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Privzeto bo Spring v teh metapodatkih nastavil `issuer` na isto osnovno URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguracija Azure API Management (`validate-jwt`)

V Azure APIM dodajte vhodno politiko, ki uporablja `<validate-jwt>` za preverjanje dohodnih JWT-jev proti vašemu Spring Authorization Serverju. Za preprosto nastavitev lahko uporabite OpenID Connect metapodatkovni URL. Primer odseka politike:

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

Ta politika pove APIM, naj pridobi OpenID konfiguracijo iz Spring Auth Serverja, pridobi njegov JWKS in preveri, da je vsak žeton podpisan z zaupanja vrednim ključem ter ima pravilen audience. (Če izpustite `<issuers>`, bo APIM samodejno uporabil `issuer` claim iz metapodatkov.) `<audience>` naj ustreza vašemu ID-ju klienta ali identifikatorju API vira v žetonu (v zgornjem primeru smo ga nastavili na `"mcp-client"`). To je skladno z Microsoftovo dokumentacijo o uporabi `validate-jwt` z `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po preverjanju bo APIM posredoval zahtevo (vključno z originalnim `Authorization` headerjem) v backend. Ker je Spring aplikacija tudi resource server, bo žeton ponovno preverila, vendar je APIM že zagotovil njegovo veljavnost. (Za razvoj lahko zaupate APIM-ovemu preverjanju in po želji onemogočite dodatne kontrole v aplikaciji, vendar je varneje imeti obe.)

## Primer nastavitve

| Nastavitev          | Primer vrednosti                                                   | Opombe                                     |
|---------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL vaše Container App (osnovni URI)       |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Privzeta Spring token končna točka ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Privzeta JWK Set končna točka ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC odkrivanje dokument (samodejno generiran) |
| **APIM audience**   | `mcp-client`                                                      | OAuth ID klienta ali ime API vira           |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` uporablja ta URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Pogoste težave

- **HTTPS/TLS:** APIM gateway zahteva, da sta OpenID/JWKS končni točki HTTPS z veljavnim certifikatom. Privzeto Azure Container Apps zagotavlja zaupanja vreden TLS certifikat za Azure upravljano domeno ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Če uporabljate lastno domeno, poskrbite za vezavo certifikata (lahko uporabite Azure funkcijo brezplačnega upravljanega certifikata) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Če APIM ne zaupa certifikatu končne točke, bo `<validate-jwt>` spodletel pri pridobivanju metapodatkov.

- **Dostopnost končnih točk:** Poskrbite, da so končne točke Spring aplikacije dosegljive iz APIM. Najlažje je uporabiti `--ingress external` (ali omogočiti ingress v portalu). Če ste izbrali interno ali vNet vezano okolje, APIM (privzeto javno) morda ne bo mogel dostopati, razen če je v istem VNetu. V testnem okolju raje uporabite javni ingress, da lahko APIM kliče `.well-known` in `/jwks` URL-je.

- **Omogočeno OpenID odkrivanje:** Privzeto Spring Authorization Server **ne izpostavlja** `/.well-known/openid-configuration`, razen če je omogočen OIDC. Poskrbite, da vključite `.oidc(Customizer.withDefaults())` v vašo varnostno konfiguracijo (glej zgoraj), da bo aktivna konfiguracijska končna točka ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). V nasprotnem primeru bo APIM-ov klic `<openid-config>` vrnil 404.

- **Audience claim:** Privzeto Spring nastavi `aud` claim na ID klienta. Če APIM-ov `<audience>` check ne uspe, boste morda morali prilagoditi žeton (kot je prikazano zgoraj) ali spremeniti APIM politiko. Poskrbite, da se audience v vašem JWT ujema s tistim, kar konfigurirate v `<audience>`.

- **Parsiranje JSON metapodatkov:** OpenID konfiguracijski JSON mora biti veljaven. Privzeta Spring konfiguracija bo izdala standardni OIDC metapodatkovni dokument. Preverite, da vsebuje pravilne vrednosti `issuer` in `jwks_uri`. Če gostite Spring za proxyjem ali potno usmeritvijo, natančno preverite URL-je v teh metapodatkih. APIM bo uporabil te vrednosti takšne, kot so.

- **Vrstni red politik:** V APIM politiki postavite `<validate-jwt>` **pred** kakršnim koli usmerjanjem v backend. V nasprotnem primeru lahko klici dosežejo vašo aplikacijo brez veljavnega žetona. Prav tako zagotovite, da je `<validate-jwt>` neposredno pod `<inbound>` (ne znotraj drugega pogoja), da ga APIM pravilno uporabi.

Z upoštevanjem zgornjih korakov lahko zaženete svoj Spring AI MCP strežnik v Azure Container Apps in omogočite Azure API Management, da preverja dohodne OAuth2 JWT-je z minimalno politiko. Ključne točke so: javno izpostaviti Spring Auth končne točke z TLS, omogočiti OIDC odkrivanje in usmeriti APIM-ov `validate-jwt` na OpenID config URL (da lahko samodejno pridobi JWKS). Ta nastavitev je primerna za razvojno/testno okolje; za produkcijo razmislite o ustreznem upravljanju skrivnosti, življenjski dobi žetonov in rotaciji ključev v JWKS po potrebi.
**Reference:** Oglejte si dokumentacijo Spring Authorization Server za privzete končne točke ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) in konfiguracijo OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); oglejte si Microsoft APIM dokumentacijo za primere `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); in dokumentacijo Azure Container Apps za nameščanje in certifikate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.