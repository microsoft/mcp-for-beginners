# Distribuire l'app Spring AI MCP su Azure Container Apps

 ([Proteggere i server Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Server Spring AI MCP protetto con Spring Authorization Server. Il server emette token di accesso ai client e li convalida sulle richieste in ingresso (fonte: Spring blog) ([Proteggere i server Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Per distribuire il server Spring MCP, costruiscilo come container e usa Azure Container Apps con ingress esterno. Ad esempio, usando Azure CLI puoi eseguire:

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

Questo crea un Container App accessibile pubblicamente con HTTPS abilitato (Azure emette un certificato TLS gratuito per il dominio predefinito `*.azurecontainerapps.io` ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). L'output del comando include il FQDN dell'app (es. `my-mcp-app.eastus.azurecontainerapps.io`), che diventa la base dell'**issuer URL**. Assicurati che l'ingress HTTP sia abilitato (come sopra) in modo che APIM possa raggiungere l'app. In un ambiente di test/sviluppo, usa l'opzione `--ingress external` (o associa un dominio personalizzato con TLS secondo la documentazione Microsoft ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Conserva eventuali proprietà sensibili (come i segreti client OAuth) nei segreti di Container Apps o in Azure Key Vault, e mappale nel container come variabili d'ambiente.

## Configurare Spring Authorization Server

Nel codice della tua app Spring Boot, includi gli starter Spring Authorization Server e Resource Server. Configura un `RegisteredClient` (per il grant `client_credentials` in dev/test) e una sorgente chiave JWT. Ad esempio, in `application.properties` potresti impostare:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Abilita l'Authorization Server e il Resource Server definendo una security filter chain. Per esempio:

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

Questa configurazione esporrà gli endpoint OAuth2 predefiniti: `/oauth2/token` per i token e `/oauth2/jwks` per il JSON Web Key Set. (Per impostazione predefinita, `AuthorizationServerSettings` di Spring mappa `/oauth2/token` e `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Il server emetterà token di accesso JWT firmati con la chiave RSA sopra indicata e pubblicherà la chiave pubblica su `https://<your-app>:/oauth2/jwks`.

**Abilita la scoperta OpenID Connect:** Per permettere ad APIM di recuperare automaticamente l’issuer e il JWKS, abilita l’endpoint di configurazione del provider OIDC aggiungendo `.oidc(Customizer.withDefaults())` nella configurazione di sicurezza ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Per esempio:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Questo espone `/.well-known/openid-configuration`, che APIM può usare per i metadati. Infine, potresti voler personalizzare la claim **audience** del JWT affinché il controllo `<audiences>` di APIM venga superato. Ad esempio, aggiungi un token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Questo garantisce che i token contengano `"aud": ["mcp-client"]`, corrispondente all’ID client o allo scope atteso da APIM.

## Esporre gli endpoint Token e JWKS

Dopo la distribuzione, l’**issuer URL** della tua app sarà `https://<app-fqdn>`, es. `https://my-mcp-app.eastus.azurecontainerapps.io`. I suoi endpoint OAuth2 sono:

- **Endpoint token:** `https://<app-fqdn>/oauth2/token` – i client ottengono i token qui (flusso client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – restituisce il set di chiavi JWK (usato da APIM per ottenere le chiavi di firma).
- **Configurazione OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON di scoperta OIDC (contiene `issuer`, `token_endpoint`, `jwks_uri`, ecc.).

APIM punterà all’**URL di configurazione OpenID**, da cui scoprirà il `jwks_uri`. Ad esempio, se il FQDN del Container App è `my-mcp-app.eastus.azurecontainerapps.io`, allora il `<openid-config url="...">` di APIM dovrebbe usare `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Per impostazione predefinita, Spring imposta l’`issuer` in quei metadati allo stesso URL base ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurare Azure API Management (`validate-jwt`)

In Azure APIM, aggiungi una policy inbound che utilizzi la policy `<validate-jwt>` per verificare i JWT in ingresso contro il tuo Spring Authorization Server. Per una configurazione semplice, puoi usare l’URL dei metadati OpenID Connect. Esempio di snippet di policy:

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

Questa policy indica ad APIM di recuperare la configurazione OpenID dal server Spring Auth, ottenere il JWKS e convalidare che ogni token sia firmato da una chiave attendibile e abbia il pubblico corretto. (Se ometti `<issuers>`, APIM userà automaticamente la claim `issuer` dai metadati.) Il `<audience>` deve corrispondere al tuo client ID o all’identificatore della risorsa API nel token (nell’esempio sopra, lo abbiamo impostato su `"mcp-client"`). Questo è coerente con la documentazione Microsoft sull’uso di `validate-jwt` con `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Dopo la validazione, APIM inoltrerà la richiesta (inclusa l’intestazione `Authorization` originale) al backend. Poiché l’app Spring è anche un resource server, convaliderà nuovamente il token, ma APIM ha già garantito la sua validità. (Per lo sviluppo, puoi fare affidamento sul controllo di APIM e disabilitare ulteriori controlli nell’app se vuoi, ma è più sicuro mantenere entrambi.)

## Esempio di impostazioni

| Impostazione        | Valore di esempio                                                   | Note                                       |
|---------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | URL del tuo Container App (URI base)       |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Endpoint token Spring predefinito ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | Endpoint JWK Set predefinito ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento di scoperta OIDC (generato automaticamente) |
| **APIM audience**   | `mcp-client`                                                       | ID client OAuth o nome risorsa API          |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa questo URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Errori comuni

- **HTTPS/TLS:** Il gateway APIM richiede che l’endpoint OpenID/JWKS sia HTTPS con un certificato valido. Per impostazione predefinita, Azure Container Apps fornisce un certificato TLS attendibile per il dominio gestito da Azure ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se usi un dominio personalizzato, assicurati di associare un certificato (puoi usare la funzionalità di certificato gestito gratuito di Azure) ([Nomi di dominio personalizzati e certificati gestiti gratuiti in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se APIM non può fidarsi del certificato dell’endpoint, `<validate-jwt>` non riuscirà a recuperare i metadati.

- **Accessibilità degli endpoint:** Assicurati che gli endpoint dell’app Spring siano raggiungibili da APIM. Usare `--ingress external` (o abilitare l’ingress dal portale) è la soluzione più semplice. Se hai scelto un ambiente interno o vincolato a una vNet, APIM (che di default è pubblico) potrebbe non raggiungerlo a meno che non sia nella stessa vNet. In un ambiente di test, preferisci ingress pubblico così APIM può chiamare gli URL `.well-known` e `/jwks`.

- **OpenID Discovery abilitato:** Per impostazione predefinita, Spring Authorization Server **non espone** `/.well-known/openid-configuration` a meno che OIDC non sia abilitato. Assicurati di includere `.oidc(Customizer.withDefaults())` nella configurazione di sicurezza (vedi sopra) affinché l’endpoint di configurazione del provider sia attivo ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Altrimenti la chiamata `<openid-config>` di APIM restituirà un errore 404.

- **Claim Audience:** Il comportamento predefinito di Spring è impostare la claim `aud` sull’ID client. Se il controllo `<audience>` di APIM fallisce, potresti dover personalizzare il token (come mostrato sopra) o modificare la policy APIM. Assicurati che l’audience nel JWT corrisponda a quanto configurato in `<audience>`.

- **Parsing dei metadati JSON:** Il JSON di configurazione OpenID deve essere valido. La configurazione predefinita di Spring emette un documento standard di metadati OIDC. Verifica che contenga l’`issuer` e il `jwks_uri` corretti. Se ospiti Spring dietro un proxy o un percorso basato su path, ricontrolla gli URL in questi metadati. APIM userà questi valori così come sono.

- **Ordine delle policy:** Nella policy APIM, posiziona `<validate-jwt>` **prima** di qualsiasi routing verso il backend. Altrimenti, le chiamate potrebbero raggiungere la tua app senza un token valido. Assicurati inoltre che `<validate-jwt>` sia immediatamente sotto `<inbound>` (non annidato in un’altra condizione) affinché APIM lo applichi.

Seguendo questi passaggi, puoi eseguire il tuo server Spring AI MCP in Azure Container Apps e far sì che Azure API Management convalidi i JWT OAuth2 in ingresso con una policy minima. I punti chiave sono: esporre pubblicamente gli endpoint Spring Auth con TLS, abilitare la scoperta OIDC e puntare `validate-jwt` di APIM all’URL di configurazione OpenID (così da recuperare automaticamente il JWKS). Questa configurazione è adatta per ambienti di sviluppo/test; per la produzione, considera una gestione adeguata dei segreti, la durata dei token e la rotazione delle chiavi JWKS secondo necessità.
**Riferimenti:** Consulta la documentazione di Spring Authorization Server per gli endpoint predefiniti ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) e la configurazione OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consulta la documentazione Microsoft APIM per esempi di `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); e la documentazione di Azure Container Apps per il deployment e i certificati ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.