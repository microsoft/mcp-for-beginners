# Ανάπτυξη της εφαρμογής Spring AI MCP σε Azure Container Apps

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Εικόνα: Ο διακομιστής Spring AI MCP ασφαλισμένος με Spring Authorization Server. Ο διακομιστής εκδίδει access tokens στους πελάτες και τα επαληθεύει στα εισερχόμενα αιτήματα (πηγή: Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Για να αναπτύξετε τον διακομιστή Spring MCP, δημιουργήστε τον ως container και χρησιμοποιήστε τα Azure Container Apps με εξωτερική πρόσβαση (ingress). Για παράδειγμα, με το Azure CLI μπορείτε να εκτελέσετε:

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

Αυτό δημιουργεί μια δημόσια προσβάσιμη Container App με ενεργοποιημένο HTTPS (η Azure εκδίδει δωρεάν πιστοποιητικό TLS για το προεπιλεγμένο domain `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Η έξοδος της εντολής περιλαμβάνει το FQDN της εφαρμογής (π.χ. `my-mcp-app.eastus.azurecontainerapps.io`), το οποίο γίνεται η βάση του **issuer URL**. Βεβαιωθείτε ότι η HTTP πρόσβαση (ingress) είναι ενεργοποιημένη (όπως παραπάνω) ώστε το APIM να μπορεί να φτάσει την εφαρμογή. Σε περιβάλλον δοκιμών/ανάπτυξης, χρησιμοποιήστε την επιλογή `--ingress external` (ή συνδέστε ένα προσαρμοσμένο domain με TLS σύμφωνα με τα [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Αποθηκεύστε ευαίσθητες ιδιότητες (όπως τα OAuth client secrets) στα Container Apps secrets ή στο Azure Key Vault και αντιστοιχίστε τα στο container ως μεταβλητές περιβάλλοντος.

## Διαμόρφωση Spring Authorization Server

Στον κώδικα της εφαρμογής Spring Boot, συμπεριλάβετε τα starters για Spring Authorization Server και Resource Server. Διαμορφώστε έναν `RegisteredClient` (για το grant `client_credentials` σε dev/test) και μια πηγή κλειδιού JWT. Για παράδειγμα, στο `application.properties` μπορείτε να ορίσετε:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Ενεργοποιήστε τον Authorization Server και Resource Server ορίζοντας μια αλυσίδα φίλτρων ασφαλείας. Για παράδειγμα:

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

Αυτή η διαμόρφωση θα εκθέσει τα προεπιλεγμένα OAuth2 endpoints: `/oauth2/token` για tokens και `/oauth2/jwks` για το JSON Web Key Set. (Εξ ορισμού, το `AuthorizationServerSettings` του Spring αντιστοιχίζει τα `/oauth2/token` και `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Ο διακομιστής θα εκδίδει JWT access tokens υπογεγραμμένα με το παραπάνω RSA κλειδί και θα δημοσιεύει το δημόσιο κλειδί του στο `https://<your-app>:/oauth2/jwks`.

**Ενεργοποίηση OpenID Connect discovery:** Για να επιτρέψετε στο APIM να ανακτήσει αυτόματα τον issuer και το JWKS, ενεργοποιήστε το endpoint διαμόρφωσης παρόχου OIDC προσθέτοντας `.oidc(Customizer.withDefaults())` στη ρύθμιση ασφαλείας σας ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Για παράδειγμα:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Αυτό εκθέτει το `/.well-known/openid-configuration`, το οποίο μπορεί να χρησιμοποιήσει το APIM για μεταδεδομένα. Τέλος, ίσως θελήσετε να προσαρμόσετε το JWT **audience** claim ώστε ο έλεγχος `<audiences>` του APIM να περάσει. Για παράδειγμα, προσθέστε έναν token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Αυτό διασφαλίζει ότι τα tokens φέρουν `"aud": ["mcp-client"]`, ταιριάζοντας με το client ID ή το scope που αναμένει το APIM.

## Έκθεση των Token και JWKS Endpoints

Μετά την ανάπτυξη, το **issuer URL** της εφαρμογής σας θα είναι `https://<app-fqdn>`, π.χ. `https://my-mcp-app.eastus.azurecontainerapps.io`. Τα OAuth2 endpoints είναι:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – εδώ οι πελάτες λαμβάνουν tokens (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – επιστρέφει το σύνολο JWK (χρησιμοποιείται από το APIM για να πάρει τα κλειδιά υπογραφής).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON για OIDC discovery (περιέχει `issuer`, `token_endpoint`, `jwks_uri` κ.ά.).

Το APIM θα δείχνει στο **OpenID configuration URL**, από όπου ανακαλύπτει το `jwks_uri`. Για παράδειγμα, αν το FQDN της Container App είναι `my-mcp-app.eastus.azurecontainerapps.io`, τότε το `<openid-config url="...">` του APIM πρέπει να χρησιμοποιεί `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Εξ ορισμού, το Spring θα ορίσει το `issuer` στα μεταδεδομένα στο ίδιο βασικό URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Διαμόρφωση Azure API Management (`validate-jwt`)

Στο Azure APIM, προσθέστε μια inbound πολιτική που χρησιμοποιεί το `<validate-jwt>` για να ελέγξει τα εισερχόμενα JWTs έναντι του Spring Authorization Server σας. Για απλή διαμόρφωση, μπορείτε να χρησιμοποιήσετε το OpenID Connect metadata URL. Παράδειγμα αποσπάσματος πολιτικής:

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

Αυτή η πολιτική λέει στο APIM να πάρει τη διαμόρφωση OpenID από τον Spring Auth Server, να ανακτήσει το JWKS και να επαληθεύσει ότι κάθε token είναι υπογεγραμμένο από αξιόπιστο κλειδί και έχει το σωστό audience. (Αν παραλείψετε τα `<issuers>`, το APIM θα χρησιμοποιήσει αυτόματα το `issuer` claim από τα μεταδεδομένα.) Το `<audience>` πρέπει να ταιριάζει με το client ID ή το API resource identifier στο token (στο παράδειγμα παραπάνω το ορίσαμε σε `"mcp-client"`). Αυτό συμφωνεί με την τεκμηρίωση της Microsoft για τη χρήση του `validate-jwt` με `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Μετά την επαλήθευση, το APIM προωθεί το αίτημα (συμπεριλαμβανομένου του αρχικού header `Authorization`) στο backend. Επειδή η εφαρμογή Spring είναι επίσης resource server, θα επαληθεύσει ξανά το token, αλλά το APIM έχει ήδη διασφαλίσει την εγκυρότητά του. (Για ανάπτυξη, μπορείτε να βασιστείτε στον έλεγχο του APIM και να απενεργοποιήσετε επιπλέον ελέγχους στην εφαρμογή αν θέλετε, αλλά είναι πιο ασφαλές να διατηρήσετε και τους δύο.)

## Παραδείγματα Ρυθμίσεων

| Ρύθμιση           | Παράδειγμα Τιμής                                                   | Σημειώσεις                                  |
|-------------------|-------------------------------------------------------------------|---------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | Το URL της Container App (βασικό URI)       |
| **Token endpoint**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Προεπιλεγμένο token endpoint του Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Προεπιλεγμένο JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Έγγραφο ανακάλυψης OIDC (αυτοπαραγόμενο)    |
| **APIM audience** | `mcp-client`                                                      | OAuth client ID ή όνομα API resource        |
| **APIM policy**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | Το `<validate-jwt>` χρησιμοποιεί αυτό το URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Συνηθισμένα Σφάλματα

- **HTTPS/TLS:** Η πύλη APIM απαιτεί το OpenID/JWKS endpoint να είναι HTTPS με έγκυρο πιστοποιητικό. Εξ ορισμού, τα Azure Container Apps παρέχουν αξιόπιστο πιστοποιητικό TLS για το domain που διαχειρίζεται η Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Αν χρησιμοποιείτε προσαρμοσμένο domain, βεβαιωθείτε ότι έχετε συνδέσει πιστοποιητικό (μπορείτε να χρησιμοποιήσετε τη δωρεάν διαχείριση πιστοποιητικών της Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Αν το APIM δεν εμπιστεύεται το πιστοποιητικό του endpoint, το `<validate-jwt>` δεν θα καταφέρει να πάρει τα μεταδεδομένα.

- **Προσβασιμότητα Endpoints:** Βεβαιωθείτε ότι τα endpoints της εφαρμογής Spring είναι προσβάσιμα από το APIM. Η χρήση `--ingress external` (ή η ενεργοποίηση ingress από το portal) είναι η απλούστερη λύση. Αν έχετε επιλέξει εσωτερικό ή vNet-bound περιβάλλον, το APIM (που είναι δημόσιο εξ ορισμού) μπορεί να μην έχει πρόσβαση εκτός αν βρίσκεται στο ίδιο VNet. Σε περιβάλλον δοκιμών, προτιμήστε δημόσιο ingress ώστε το APIM να μπορεί να καλέσει τα URLs `.well-known` και `/jwks`.

- **Ενεργοποίηση OpenID Discovery:** Εξ ορισμού, ο Spring Authorization Server **δεν εκθέτει** το `/.well-known/openid-configuration` αν δεν είναι ενεργοποιημένο το OIDC. Βεβαιωθείτε ότι έχετε συμπεριλάβει `.oidc(Customizer.withDefaults())` στη ρύθμιση ασφαλείας (βλ. παραπάνω) ώστε το endpoint διαμόρφωσης παρόχου να είναι ενεργό ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Διαφορετικά, το κάλεσμα `<openid-config>` του APIM θα επιστρέψει 404.

- **Audience Claim:** Η προεπιλεγμένη συμπεριφορά του Spring είναι να ορίζει το `aud` claim στο client ID. Αν ο έλεγχος `<audience>` του APIM αποτύχει, ίσως χρειαστεί να προσαρμόσετε το token (όπως δείχθηκε παραπάνω) ή να τροποποιήσετε την πολιτική του APIM. Βεβαιωθείτε ότι το audience στο JWT ταιριάζει με αυτό που ορίζετε στο `<audience>`.

- **Ανάλυση JSON Μεταδεδομένων:** Το JSON διαμόρφωσης OpenID πρέπει να είναι έγκυρο. Η προεπιλεγμένη ρύθμιση του Spring θα παράγει ένα τυπικό έγγραφο μεταδεδομένων OIDC. Ελέγξτε ότι περιέχει το σωστό `issuer` και `jwks_uri`. Αν φιλοξενείτε τον Spring πίσω από proxy ή με διαδρομή βάσης (path-based route), ελέγξτε προσεκτικά τα URLs σε αυτά τα μεταδεδομένα. Το APIM θα τα χρησιμοποιήσει όπως είναι.

- **Σειρά Πολιτικών:** Στην πολιτική του APIM, τοποθετήστε το `<validate-jwt>` **πριν** από οποιαδήποτε δρομολόγηση προς το backend. Διαφορετικά, τα αιτήματα μπορεί να φτάσουν στην εφαρμογή χωρίς έγκυρο token. Επίσης, βεβαιωθείτε ότι το `<validate-jwt>` εμφανίζεται αμέσως κάτω από το `<inbound>` (όχι μέσα σε άλλη συνθήκη) ώστε το APIM να το εφαρμόζει.

Ακολουθώντας τα παραπάνω βήματα, μπορείτε να τρέξετε τον Spring AI MCP server σας σε Azure Container Apps και να έχετε το Azure API Management να επαληθεύει τα εισερχόμενα OAuth2 JWTs με μια ελάχιστη πολιτική. Τα βασικά σημεία είναι: εκθέστε δημόσια τα Spring Auth endpoints με TLS, ενεργοποιήστε το OIDC discovery και δείξτε το `validate-jwt` του APIM στο OpenID config URL (ώστε να παίρνει αυτόματα το JWKS). Αυτή η διαμόρφωση είναι κατάλληλη για περιβάλλον dev/test· για παραγωγή, σκεφτείτε σωστή διαχείριση μυστικών, διάρκεια ζωής tokens και περιστροφή κλειδιών στο JWKS όπως απαιτείται.
**Αναφορές:** Δείτε τα έγγραφα του Spring Authorization Server για τις προεπιλεγμένες τελικές σημεία ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) και τη ρύθμιση OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); δείτε τα έγγραφα Microsoft APIM για παραδείγματα `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); και τα έγγραφα Azure Container Apps για ανάπτυξη και πιστοποιητικά ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.