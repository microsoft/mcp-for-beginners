# Nameščanje aplikacije Spring AI MCP v Azure Container Apps

> [!WARNING]
> Ta združeni avtentikacijski/strežnik virov je namenjen za učenje in
> razvojno/testno rabo. Produkcijski sistemi naj uporabljajo namenski ponudnik identitete,
> trajne podpise in poverilnice, shranjene v upravljanem skrivnem skladišču.

 ([Zavarovanje Spring AI MCP strežnikov z OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Slika: Spring AI MCP strežnik zavarovan s Spring Authorization Server. Strežnik izda dostopne žetone odjemalcem in jih potrdi pri dohodnih zahtevah (vir: Spring blog) ([Zavarovanje Spring AI MCP strežnikov z OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Za nameščanje Spring MCP strežnika ga zgradite kot vsebnik in uporabite Azure Container Apps z zunanjim vhodom. Na primer, z uporabo Azure CLI lahko zaženete:

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

Ta ukaz ustvari javno dostopno Container App z omogočenim HTTPS (Azure izda brezplačen TLS certifikat za privzeto domeno `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Izpis ukaza vključuje FQDN aplikacije (npr. `my-mcp-app.eastus.azurecontainerapps.io`), ki postane osnovni **URL izdajatelja**. Poskrbite, da je omogočen HTTP vhod (kot zgoraj), da lahko APIM dostopa do aplikacije. V testnem/razvojnem okolju uporabite možnost `--ingress external` (ali vežite lastno domeno s TLS po [Microsoft dokumentaciji](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Občutljive lastnosti (kot so OAuth skrivnosti odjemalcev) shranjujte v Container Apps skrivnosti ali Azure Key Vault in jih preslikajte v vsebnik kot okoljske spremenljivke.

## Konfiguracija Spring Authorization Serverja

V kodi vaše Spring Boot aplikacije vključite Spring Authorization Server in Resource Server starterje. Konfigurirajte `RegisteredClient` (za `client_credentials` grant v razvoju/testiranju) in vir JWT ključev. Na primer, v `application.properties` lahko nastavite:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Omogočite Authorization Server in Resource Server z definiranjem varnostne verige filtrov. Na primer:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Omogoči točke končne avtorizacijskega strežnika
            .apply(authzServer.and())
            // Omogoči strežnik virov (preveri JWT v dohodnih zahtevah)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Onemogoči CSRF (MCP strežnik ni spletni brskalnik)
            .csrf(csrf -> csrf.disable())
            // Dovoli CORS za orodja demo odjemalca
            .cors(withDefaults());
        return http.build();
    }

    // Določi odjemalca v pomnilniku (RegisteredClient) in vir JWK:
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
        // Ustvari RSA ključ (za razvoj/test, ustvari novega ob zagonu)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ta nastavitev bo razkrila privzete OAuth2 končne točke: `/oauth2/token` za žetone in `/oauth2/jwks` za JSON Web Key Set. (Privzeto Springjeva `AuthorizationServerSettings` preslika `/oauth2/token` in `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Strežnik bo izdal JWT dostopne žetone, podpisane z RSA ključem zgoraj, in objavil javni ključ na `https://<your-app>:/oauth2/jwks`.

**Omogočite OpenID Connect odkrivanje:** Da lahko APIM samodejno pridobi izdajatelja in JWKS, omogočite OIDC ponudnik konfiguracijsko končno točko z dodajanjem `.oidc(Customizer.withDefaults())` v vašo varnostno konfiguracijo ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Na primer:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– omogoči /.well-known/openid-configuration
```

To razkrije `/.well-known/openid-configuration`, ki ga APIM lahko uporabi za metapodatke. Nazadnje boste morda želeli prilagoditi JWT **audience** trditev, da bo APIM-jeva preverba `<audiences>` uspešna. Na primer, dodajte prilagoditelj žetona:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Nastavite prilagojeno občinstvo (npr. ID stranke ali identifikator API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

To zagotavlja, da žetoni nosijo `"aud": ["mcp-client"]`, kar ustreza ID-ju odjemalca ali obsegu, ki ga pričakuje APIM.

## Razkritje žetonov in JWKS končnih točk

Po nameščanju bo **izdajateljev URL** vaše aplikacije `https://<app-fqdn>`, npr. `https://my-mcp-app.eastus.azurecontainerapps.io`. Njene OAuth2 končne točke so:

- **Končna točka za žetone:** `https://<app-fqdn>/oauth2/token` – odjemalci tukaj pridobivajo žetone (tok client_credentials).
- **JWKS končna točka:** `https://<app-fqdn>/oauth2/jwks` – vrne JWK set (APIM ga uporablja za pridobivanje podpisnih ključev).
- **OpenID konfiguracija:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC odkrivanje JSON (vsebuje `issuer`, `token_endpoint`, `jwks_uri`, itd.).  

APIM bo kazal na **OpenID konfiguracijski URL**, od koder odkrije `jwks_uri`. Na primer, če je FQDN vaše Container App `my-mcp-app.eastus.azurecontainerapps.io`, potem naj APIM-jeva `<openid-config url="...">` uporablja `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Privzeto bo Spring nastavil `issuer` v teh metapodatkih na isti osnovni URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguracija Azure API Management (`validate-jwt`)

V Azure APIM dodajte vhodno pravilo, ki uporablja `<validate-jwt>` pravilo za preverjanje vhodnih JWT-jev v primerjavi z vašim Spring Authorization Serverjem. Za preprosto nastavitev lahko uporabite OpenID Connect metapodatkovni URL. Primer odseka pravil:

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

To pravilo pove APIM, naj pridobi OpenID konfiguracijo iz Spring Auth Serverja, prevzame njegov JWKS in pregleda, da je vsak žeton podpisan s zaupanja vrednim ključem in ima pravilen audience. (Če izpustite `<issuers>`, bo APIM samodejno uporabljal `issuer` trditev iz metapodatkov.) `<audience>` naj ustreza ID-ju vašega odjemalca ali identifikatorju API vira v žetonu (v zgornjem primeru smo jo nastavili na `"mcp-client"`). To je skladno z Microsoftovo dokumentacijo o uporabi `validate-jwt` s `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po potrditvi bo APIM posredoval zahtevek (vključno z originalno glavo `Authorization`) v ozadje. Ker je Spring aplikacija tudi strežnik virov, bo ponovno preverila veljavnost žetona, a APIM je že zagotovil njegovo veljavnost. (Za razvoj se lahko zanesete na APIM-jevo preverjanje in po potrebi onemogočite dodatne kontrole v aplikaciji, a varneje je imeti obe.)

## Primer nastavitev

| Nastavitev         | Primer vrednosti                                                   | Opombe                                       |
|-------------------|------------------------------------------------------------------|----------------------------------------------|
| **Izdajatelj**    | `https://my-mcp-app.eastus.azurecontainerapps.io`                | URL vaše Container App (osnovni URI)          |
| **Končna točka za žetone** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | Privzeta Spring končna točka za žetone ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS končna točka** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks` | Privzeta končna točka za JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC odkrit dokument (samodejno generiran)    |
| **APIM občinstvo** | `mcp-client`                                                     | ID OAuth odjemalca ali ime API vira          |
| **APIM pravilo** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` uporablja ta URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Pogoste pasti

- **HTTPS/TLS:** Prehod APIM zahteva, da sta OpenID/JWKS končni točki na HTTPS z veljavnim certifikatom. Privzeto Azure Container Apps zagotavlja zanesljiv TLS certifikat za Azure-upravljano domeno ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Če uporabljate lastno domeno, jo obvezno povežite s certifikatom (lahko uporabite Azure-ovo brezplačno upravljano funkcijo certifikatov) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Če APIM ne zaupa certifikatu končne točke, `<validate-jwt>` ne bo uspel pridobiti metapodatkov.

- **Dostopnost končnih točk:** Poskrbite, da so strežniške končne točke Spring aplikacije dosegljive iz APIM. Uporaba `--ingress external` (ali omogočanje vhoda v portalu) je najpreprostejša. Če ste izbrali notranje ali vNet vezano okolje, APIM (privzeto javno) morda ne bo dosegel aplikacije, razen če je v isti VNet. V testnem okolju je bolje uporabiti javni vhod, da lahko APIM pokliče `.well-known` in `/jwks` URL-je.

- **Omogočeno odkrivanje OpenID:** Privzeto Spring Authorization Server **ne izpostavi** `/.well-known/openid-configuration`, če OIDC ni omogočen. Prepričajte se, da ste v varnostni konfiguraciji vključili `.oidc(Customizer.withDefaults())` (glejte zgoraj), da je končna točka ponudnika aktivna ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). V nasprotnem primeru bo APIM-jevo klicanje `<openid-config>` dalo 404.

- **Trditev audience:** Springova privzeta nastavitev je nastaviti `aud` trditev na ID odjemalca. Če APIM-jeva preverba `<audience>` ne uspe, boste morda morali prilagoditi žeton (kot je prikazano zgoraj) ali spremeniti APIM pravilo. Prepričajte se, da se občinstvo v vašem JWT ujema s tistim, kar nastavite v `<audience>`.

- **Analiza JSON metapodatkov:** OpenID konfiguracijski JSON mora biti veljaven. Springova privzeta konfiguracija izda standardni OIDC metapodatkovni dokument. Preverite, da vsebuje pravilni `issuer` in `jwks_uri`. Če gostite Spring za proxyjem ali potjo, dvojno preverite URL-je v teh metapodatkih. APIM bo uporabljal te vrednosti nespremenjene.

- **Urejanje pravil:** V APIM pravilu postavite `<validate-jwt>` **pred** katerim koli preusmerjanjem na ozadje. V nasprotnem primeru lahko klici dosežejo vašo aplikacijo brez veljavnega žetona. Prav tako zagotovite, da je `<validate-jwt>` neposredno pod `<inbound>` (ne gnezden v drugem pogoju), da ga APIM uveljavlja.

Z upoštevanjem zgornjih korakov lahko v Azure Container Apps zaženete svoj Spring AI MCP strežnik in imate Azure API Management, ki ob minimalnem pravilu preverja vhodne OAuth2 JWT-je. Ključne točke so: javno razkriti Spring Auth končne točke s TLS, omogočiti OIDC odkrivanje in usmeriti APIM-jevo `validate-jwt` na OpenID konfiguracijski URL (da lahko samodejno pridobi JWKS). Ta nastavitev ustreza razvojno/testnemu okolju; za produkcijo razmislite o ustreznem upravljanju skrivnosti, življenjski dobi žetonov in rotaciji ključev v JWKS po potrebi.


**Reference:** Glejte dokumentacijo Spring Authorization Server za privzete končne točke ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) in OIDC konfiguracijo ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); glejte Microsoft APIM dokumentacijo za primere `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); in Azure Container Apps dokumentacijo za namestitev in certifikate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->