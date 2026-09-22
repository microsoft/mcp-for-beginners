# Distribuire l’app Spring AI MCP in Azure Container Apps

> [!WARNING]
> Questo server combinato di autorizzazione/risorse è destinato ad uso didattico e
> di sviluppo/test. I sistemi di produzione dovrebbero usare un provider di identità dedicato,
> chiavi di firma persistenti e credenziali conservate in un archivio di segreti gestito.

 ([Proteggere i server Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Server Spring AI MCP protetto con Spring Authorization Server. Il server emette token di accesso ai client e li convalida sulle richieste in ingresso (fonte: blog Spring) ([Proteggere i server Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Per distribuire il server Spring MCP, costruiscilo come contenitore e usa Azure Container Apps con ingress esterno. Ad esempio, usando la CLI di Azure puoi eseguire:

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

Questo crea un Container App accessibile pubblicamente con HTTPS abilitato (Azure emette un certificato TLS gratuito per il dominio predefinito `*.azurecontainerapps.io` ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). L'output del comando include il FQDN dell’app (es. `my-mcp-app.eastus.azurecontainerapps.io`), che diventa la base dell’**URL dell’emittente**. Assicurati che l’ingresso HTTP sia abilitato (come sopra) affinché APIM possa raggiungere l’app. In un ambiente di test/sviluppo, usa l’opzione `--ingress external` (o associa un dominio personalizzato con TLS come da [documentazione Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Archivia eventuali proprietà sensibili (come i segreti client OAuth) nei segreti di Container Apps o in Azure Key Vault, e mappale nel contenitore come variabili d’ambiente.

## Configurare Spring Authorization Server

Nel codice della tua app Spring Boot, includi gli starter Spring Authorization Server e Resource Server. Configura un `RegisteredClient` (per la concessione `client_credentials` in dev/test) e una sorgente chiavi JWT. Ad esempio, in `application.properties` potresti impostare:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Abilita il Authorization Server e Resource Server definendo una catena di filtri di sicurezza. Ad esempio:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Abilita gli endpoint del Authorization Server
            .apply(authzServer.and())
            // Abilita il Resource Server (valida JWT sulle richieste in entrata)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Disabilita CSRF (il server MCP non è basato su browser)
            .csrf(csrf -> csrf.disable())
            // Consenti CORS per gli strumenti demo del client
            .cors(withDefaults());
        return http.build();
    }

    // Definisci un client in memoria (RegisteredClient) e una sorgente JWK:
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
        // Genera una chiave RSA (per dev/test, genera una nuova ad ogni avvio)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Questa configurazione espone gli endpoint OAuth2 predefiniti: `/oauth2/token` per i token e `/oauth2/jwks` per il JSON Web Key Set. (Per impostazione predefinita Spring `AuthorizationServerSettings` associa `/oauth2/token` e `/oauth2/jwks` ([Modello di configurazione :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Il server emetterà token di accesso JWT firmati con la chiave RSA sopra e pubblicherà la sua chiave pubblica su `https://<your-app>:/oauth2/jwks`.

**Abilitare la scoperta OpenID Connect:** Per consentire ad APIM di recuperare automaticamente l’emittente e JWKS, abilita l’endpoint di configurazione del provider OIDC aggiungendo `.oidc(Customizer.withDefaults())` nella configurazione di sicurezza ([Modello di configurazione :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ad esempio:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– abilita /.well-known/openid-configuration
```

Questo espone `/.well-known/openid-configuration`, che APIM può usare per i metadati. Infine, potresti voler personalizzare la rivendicazione JWT **audience** affinché il controllo `<audiences>` di APIM venga superato. Ad esempio, aggiungi un personalizzatore di token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Imposta un pubblico personalizzato (ad es. l'ID del cliente o l'identificatore API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Questo garantisce che i token contengano `"aud": ["mcp-client"]`, corrispondente all’ID client o allo scope atteso da APIM.

## Esporre gli endpoint Token e JWKS

Dopo la distribuzione, l’**URL dell’emittente** della tua app sarà `https://<app-fqdn>`, ad es. `https://my-mcp-app.eastus.azurecontainerapps.io`. I suoi endpoint OAuth2 sono:

- **Endpoint Token:** `https://<app-fqdn>/oauth2/token` – i client ottengono token qui (flusso client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – restituisce il set JWK (usato da APIM per ottenere le chiavi di firma).
- **Configurazione OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON di scoperta OIDC (contiene `issuer`, `token_endpoint`, `jwks_uri`, ecc.).

APIM punta all’**URL di configurazione OpenID**, da cui scopre il `jwks_uri`. Ad esempio, se il FQDN del tuo Container App è `my-mcp-app.eastus.azurecontainerapps.io`, allora il `<openid-config url="...">` di APIM dovrebbe usare `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Per impostazione predefinita Spring imposta l’`issuer` in questi metadati allo stesso URL base ([Modello di configurazione :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurare Azure API Management (`validate-jwt`)

In Azure APIM, aggiungi una policy in ingresso che utilizzi la policy `<validate-jwt>` per controllare i JWT in arrivo rispetto al tuo Spring Authorization Server. Per una configurazione semplice, puoi usare l’URL dei metadati OpenID Connect. Ecco un esempio di snippet policy:

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

Questa policy dice ad APIM di recuperare la configurazione OpenID dal server Spring Auth, ottenere il suo JWKS e convalidare che ogni token sia firmato da una chiave attendibile e abbia il pubblico corretto. (Se ometti `<issuers>`, APIM userà automaticamente il valore `issuer` dalla metadata.) Il `<audience>` deve corrispondere al tuo ID client o identificatore risorsa API nel token (nell’esempio sopra, l’abbiamo impostato su `"mcp-client"`). Questo è coerente con la documentazione Microsoft sull’uso di `validate-jwt` con `<openid-config>` ([Riferimento policy Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Dopo la convalida, APIM inoltrerà la richiesta (inclusa l’originale intestazione `Authorization`) al backend. Poiché l’app Spring è anche un resource server, convaliderà nuovamente il token, ma APIM avrà già garantito la sua validità. (Per sviluppo, puoi fare affidamento sul controllo APIM e disabilitare eventuali controlli aggiuntivi nell’app, se desideri, ma è più sicuro mantenere entrambi.)

## Impostazioni Esempio

| Impostazione        | Valore Esempio                                                       | Note                                       |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Emittente**      | `https://my-mcp-app.eastus.azurecontainerapps.io`                   | L’URL del tuo Container App (URI base)    |
| **Endpoint Token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`      | Endpoint token predefinito di Spring ([Modello di configurazione :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **Endpoint JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`       | Endpoint set JWK predefinito ([Modello di configurazione :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **Config OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento di scoperta OIDC (generato automaticamente) |
| **Audience APIM**  | `mcp-client`                                                        | ID client OAuth o nome risorsa API         |
| **Policy APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa questo URL ([Riferimento policy Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Errori Comuni

- **HTTPS/TLS:** Il gateway APIM richiede che l’endpoint OpenID/JWKS sia HTTPS con un certificato valido. Per impostazione predefinita, Azure Container Apps fornisce un certificato TLS attendibile per il dominio gestito da Azure ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se usi un dominio personalizzato, assicurati di associare un certificato (puoi usare la funzionalità di certificato gestito gratuito di Azure) ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se APIM non può fidarsi del certificato dell’endpoint, `<validate-jwt>` non riuscirà a ottenere i metadati.

- **Accessibilità dell’endpoint:** Assicurati che gli endpoint dell’app Spring siano raggiungibili da APIM. Usare `--ingress external` (o abilitare l’ingresso nel portale) è la soluzione più semplice. Se hai scelto un ambiente interno o vincolato a vNet, APIM (predefinito pubblico) potrebbe non raggiungerlo a meno che non sia posizionato nella stessa vNet. In un ambiente di test, preferisci ingress pubblico così APIM può chiamare le URL `.well-known` e `/jwks`.

- **Scoperta OpenID abilitata:** Di default, Spring Authorization Server **non espone** `/.well-known/openid-configuration` a meno che OIDC non sia abilitato. Assicurati di includere `.oidc(Customizer.withDefaults())` nella configurazione di sicurezza (vedi sopra) in modo che l’endpoint di configurazione provider sia attivo ([Modello di configurazione :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Altrimenti la chiamata `<openid-config>` di APIM restituirà 404.

- **Claim Audience:** Il comportamento predefinito di Spring è impostare il claim `aud` sull’ID client. Se il controllo `<audience>` di APIM fallisce, potresti dover personalizzare il token (come mostrato sopra) o modificare la policy APIM. Assicurati che l’audience nel tuo JWT corrisponda a quanto configurato in `<audience>`.

- **Parsing JSON metadati:** Il JSON di configurazione OpenID deve essere valido. La configurazione predefinita di Spring emetterà un documento standard dei metadati OIDC. Verifica che contenga `issuer` e `jwks_uri` corretti. Se ospiti Spring dietro un proxy o una rotta basata su path, verifica attentamente gli URL in questi metadati. APIM userà questi valori così come sono.

- **Ordinamento della policy:** Nella policy APIM, posiziona `<validate-jwt>` **prima** di qualsiasi routing al backend. Altrimenti, le chiamate possono raggiungere la tua app senza token valido. Assicurati inoltre che `<validate-jwt>` sia immediatamente sotto `<inbound>` (non annidato in un’altra condizione) così che APIM la applichi.

Seguendo questi passaggi, potrai eseguire il tuo server Spring AI MCP in Azure Container Apps e far convalidare da Azure API Management i JWT OAuth2 in ingresso con una policy minima. I punti chiave sono: esporre pubblicamente gli endpoint Spring Auth con TLS, abilitare la scoperta OIDC, e puntare `validate-jwt` di APIM all’URL di configurazione OpenID (per poter recuperare automaticamente il JWKS). Questa configurazione è adatta per un ambiente di test/sviluppo; per la produzione, considera una corretta gestione dei segreti, i tempi di validità dei token e la rotazione delle chiavi nel JWKS secondo necessità.


**Riferimenti:** Vedi la documentazione di Spring Authorization Server per gli endpoint predefiniti ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) e per la configurazione OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); vedi la documentazione Microsoft APIM per esempi di `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); e la documentazione di Azure Container Apps per il deployment e i certificati ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->