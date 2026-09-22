# Ανάπτυξη της Εφαρμογής Spring AI MCP σε Azure Container Apps

> [!WARNING]
> Αυτός ο συνδυασμός εξουσιοδότησης/διακομιστή πόρων προορίζεται για μάθηση και
> χρήση ανάπτυξης/δοκιμής. Τα συστήματα παραγωγής θα πρέπει να χρησιμοποιούν έναν αφιερωμένο πάροχο ταυτότητας,
> μόνιμα κλειδιά υπογραφής και διαπιστευτήρια αποθηκευμένα σε διαχειριζόμενο αποθηκευτικό μυστικών.

 ([Εξασφάλιση των διακομιστών Spring AI MCP με OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Εικόνα: Διακομιστής Spring AI MCP ασφαλισμένος με Spring Authorization Server. Ο διακομιστής εκδίδει διακριτικά πρόσβασης στους πελάτες και τα επικυρώνει στα εισερχόμενα αιτήματα (πηγή: Spring blog) ([Εξασφάλιση των διακομιστών Spring AI MCP με OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Για να αναπτύξετε τον διακομιστή Spring MCP, δημιουργήστε τον ως κοντέινερ και χρησιμοποιήστε τα Azure Container Apps με εξωτερική είσοδο. Για παράδειγμα, χρησιμοποιώντας το Azure CLI μπορείτε να εκτελέσετε:

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

Αυτό δημιουργεί μια δημόσια προσβάσιμη Εφαρμογή Container με ενεργοποιημένο HTTPS (η Azure εκδίδει δωρεάν πιστοποιητικό TLS για το προεπιλεγμένο domain `*.azurecontainerapps.io` ([Προσαρμοσμένα ονόματα τομέα και δωρεάν διαχειριζόμενα πιστοποιητικά σε Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Η έξοδος της εντολής περιλαμβάνει το FQDN της εφαρμογής (π.χ. `my-mcp-app.eastus.azurecontainerapps.io`), που γίνεται η βάση του **issuer URL**. Βεβαιωθείτε ότι η είσοδος HTTP είναι ενεργοποιημένη (όπως παραπάνω) ώστε το APIM να μπορεί να φτάσει στην εφαρμογή. Σε ρύθμιση δοκιμής/ανάπτυξης, χρησιμοποιήστε την επιλογή `--ingress external` (ή δεσμεύστε ένα προσαρμοσμένο domain με TLS σύμφωνα με τα [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Προσαρμοσμένα ονόματα τομέα και δωρεάν διαχειριζόμενα πιστοποιητικά σε Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Αποθηκεύστε τυχόν ευαίσθητες ιδιότητες (όπως μυστικά πελάτη OAuth) στα μυστικά των Container Apps ή στο Azure Key Vault και χαρτογραφήστε τα στο κοντέινερ ως μεταβλητές περιβάλλοντος. 

## Διαμόρφωση του Spring Authorization Server

Στον κώδικα της εφαρμογής Spring Boot, συμπεριλάβετε τους εκκινητές Spring Authorization Server και Resource Server. Ρυθμίστε ένα `RegisteredClient` (για το `client_credentials` grant σε dev/test) και μια πηγή κλειδιού JWT. Για παράδειγμα, στο `application.properties` ίσως ορίσετε:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Ενεργοποιήστε τον Authorization Server και τον Resource Server ορίζοντας μια αλυσίδα φίλτρων ασφαλείας. Για παράδειγμα:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Ενεργοποίηση των τελικών σημείων του Authorization Server
            .apply(authzServer.and())
            // Ενεργοποίηση του Resource Server (επικύρωση JWT σε εισερχόμενα αιτήματα)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Απενεργοποίηση CSRF (ο διακομιστής MCP δεν βασίζεται σε πρόγραμμα περιήγησης)
            .csrf(csrf -> csrf.disable())
            // Επιτρέψτε CORS για εργαλεία επίδειξης πελατών
            .cors(withDefaults());
        return http.build();
    }

    // Ορισμός ενός πελάτη στη μνήμη (RegisteredClient) και μιας πηγής JWK:
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
        // Δημιουργία ενός κλειδιού RSA (για ανάπτυξη/δοκιμή, δημιουργία νέου κατά την εκκίνηση)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Αυτή η διαμόρφωση θα εκθέσει τα προεπιλεγμένα endpoints OAuth2: `/oauth2/token` για διακριτικά και `/oauth2/jwks` για το JSON Web Key Set. (Η προεπιλογή Spring `AuthorizationServerSettings` αντιστοιχίζει `/oauth2/token` και `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Ο διακομιστής θα εκδώσει JWT access tokens υπογεγραμμένα με το παραπάνω κλειδί RSA και θα δημοσιεύσει το δημόσιο κλειδί στο `https://<your-app>:/oauth2/jwks`. 

**Ενεργοποίηση ανακάλυψης OpenID Connect:** Για να επιτρέψετε στο APIM να ανακτήσει αυτόματα τον issuer και το JWKS, ενεργοποιήστε το endpoint διαμόρφωσης παρόχου OIDC προσθέτοντας `.oidc(Customizer.withDefaults())` στη διαμόρφωση ασφαλείας σας ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Για παράδειγμα:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– ενεργοποιεί το /.well-known/openid-configuration
```

Αυτό εκθέτει το `/.well-known/openid-configuration`, το οποίο το APIM μπορεί να χρησιμοποιήσει για μεταδεδομένα. Τέλος, ίσως θέλετε να προσαρμόσετε το JWT **audience** το οποίο θα περάσει τον έλεγχο `<audiences>` του APIM. Για παράδειγμα, προσθέστε έναν token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Ορίστε ένα προσαρμοσμένο κοινό (π.χ. το αναγνωριστικό πελάτη ή το αναγνωριστικό API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Αυτό εξασφαλίζει ότι τα tokens φέρουν `"aud": ["mcp-client"]`, που ταιριάζει με το client ID ή το expected scope του APIM. 

## Έκθεση των Token και JWKS Endpoints

Μετά την ανάπτυξη, το **issuer URL** της εφαρμογής σας θα είναι `https://<app-fqdn>`, π.χ. `https://my-mcp-app.eastus.azurecontainerapps.io`. Τα OAuth2 endpoints είναι:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – οι πελάτες αποκτούν tokens εδώ (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – επιστρέφει το σετ JWK (χρησιμοποιείται από το APIM για να πάρει τα κλειδιά υπογραφής).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON ανακάλυψης OIDC (περιέχει `issuer`, `token_endpoint`, `jwks_uri` κ.ά.).  

Το APIM θα δείχνει στο **OpenID configuration URL**, από όπου ανακαλύπτει το `jwks_uri`. Για παράδειγμα, αν το FQDN της Container App είναι `my-mcp-app.eastus.azurecontainerapps.io`, τότε το `<openid-config url="...">` του APIM θα πρέπει να χρησιμοποιεί `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Η προεπιλογή Spring ορίζει το `issuer` σε αυτό το μεταδεδομένο στο ίδιο βασικό URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Διαμόρφωση Azure API Management (`validate-jwt`)

Στο Azure APIM, προσθέστε μια εισερχόμενη πολιτική που χρησιμοποιεί την πολιτική `<validate-jwt>` για να ελέγξει τα εισερχόμενα JWT έναντι του Spring Authorization Server σας. Για μια απλή ρύθμιση, μπορείτε να χρησιμοποιήσετε το URL μεταδεδομένων OpenID Connect. Παράδειγμα απόσπασμα πολιτικής:

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

Αυτή η πολιτική λέει στο APIM να πάρει τη διαμόρφωση OpenID από το Spring Auth Server, να ανακτήσει το JWKS και να επαληθεύσει ότι κάθε token υπογράφεται από ένα αξιόπιστο κλειδί και έχει το σωστό audience. (Αν παραλείψετε το `<issuers>`, το APIM θα χρησιμοποιήσει αυτόματα το `issuer` από τα μεταδεδομένα.) Το `<audience>` πρέπει να ταιριάζει με το client ID ή το API resource identifier στο token (στο παράδειγμα παραπάνω, το ορίσαμε σε `"mcp-client"`). Αυτό είναι σύμφωνο με την τεκμηρίωση της Microsoft για χρήση του `validate-jwt` με `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Μετά την επικύρωση, το APIM θα προωθήσει το αίτημα (συμπεριλαμβανομένης της αρχικής κεφαλίδας `Authorization`) στο backend. Επειδή η εφαρμογή Spring είναι επίσης διακομιστής πόρων, θα επικυρώσει ξανά το token, αλλά το APIM έχει ήδη διασφαλίσει την εγκυρότητά του. (Για ανάπτυξη, μπορείτε να βασιστείτε στον έλεγχο του APIM και να απενεργοποιήσετε πρόσθετους ελέγχους στην εφαρμογή αν το επιθυμείτε, αλλά είναι πιο ασφαλές να κρατήσετε και τα δύο.)

## Παραδείγματα Ρυθμίσεων

| Ρύθμιση            | Παράδειγμα Τιμής                                                     | Σημειώσεις                                |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Το URL της Container App (βασικό URI)   |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Προεπιλεγμένο endpoint token Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Προεπιλεγμένο endpoint JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Έγγραφο ανακάλυψης OIDC (αυτόματα δημιουργημένο)  |
| **APIM audience**  | `mcp-client`                                                         | Client ID OAuth ή όνομα πόρου API        |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | Το `<validate-jwt>` χρησιμοποιεί αυτό το URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Συνήθη Σφάλματα

- **HTTPS/TLS:** Η πύλη APIM απαιτεί το OpenID/JWKS endpoint να είναι HTTPS με έγκυρο πιστοποιητικό. Από προεπιλογή, τα Azure Container Apps παρέχουν έγκυρο πιστοποιητικό TLS για το διαχειριζόμενο domain Azure ([Προσαρμοσμένα ονόματα τομέα και δωρεάν διαχειριζόμενα πιστοποιητικά σε Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Αν χρησιμοποιείτε προσαρμοσμένο domain, βεβαιωθείτε ότι έχετε δεσμεύσει πιστοποιητικό (μπορείτε να χρησιμοποιήσετε τη δωρεάν διαχείριση πιστοποιητικών της Azure) ([Προσαρμοσμένα ονόματα τομέα και δωρεάν διαχειριζόμενα πιστοποιητικά σε Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Αν το APIM δεν εμπιστεύεται το πιστοποιητικό του endpoint, η πολιτική `<validate-jwt>` θα αποτύχει να τραβήξει τα μεταδεδομένα.  

- **Προσβασιμότητα Endpoints:** Βεβαιωθείτε ότι τα endpoints της Spring εφαρμογής είναι προσβάσιμα από το APIM. Η χρήση του `--ingress external` (ή η ενεργοποίηση εισόδου από το portal) είναι η απλούστερη λύση. Αν έχετε επιλέξει εσωτερικό ή δεσμευμένο σε vNet περιβάλλον, το APIM (δημόσιο από προεπιλογή) ίσως να μην έχει πρόσβαση εκτός αν βρίσκεται στο ίδιο VNet. Σε ρυθμίσεις δοκιμής, προτιμήστε δημόσια είσοδο ώστε το APIM να μπορεί να καλέσει τα URLs `.well-known` και `/jwks`. 

- **Ενεργοποιημένη Ανακάλυψη OpenID:** Από προεπιλογή, ο Spring Authorization Server **δεν εκθέτει** το `/.well-known/openid-configuration` αν το OIDC δεν είναι ενεργοποιημένο. Βεβαιωθείτε ότι έχετε συμπεριλάβει `.oidc(Customizer.withDefaults())` στη διαμόρφωση ασφαλείας σας (βλέπε παραπάνω) ώστε το endpoint διαμόρφωσης παρόχου να είναι ενεργό ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Αλλιώς, η κλήση `<openid-config>` του APIM θα επιστρέψει 404.

- **Απαίτηση Audience:** Η προεπιλεγμένη συμπεριφορά του Spring είναι να θέτει το claim `aud` στο client ID. Αν ο έλεγχος `<audience>` του APIM αποτύχει, ίσως χρειαστεί να προσαρμόσετε το token (όπως δείχθηκε παραπάνω) ή να τροποποιήσετε την πολιτική του APIM. Βεβαιωθείτε ότι το audience στο JWT σας ταιριάζει με την τιμή που έχετε ρυθμίσει στο `<audience>`. 

- **Ανάλυση JSON Μεταδεδομένων:** Το JSON διαμόρφωσης OpenID πρέπει να είναι έγκυρο. Η προεπιλεγμένη ρύθμιση του Spring παράγει ένα τυπικό έγγραφο OIDC μεταδεδομένων. Επαληθεύστε ότι περιέχει τα σωστά `issuer` και `jwks_uri`. Αν φιλοξενείτε το Spring πίσω από proxy ή διαδρομή βάσει διαδρομής, ελέγξτε προσεκτικά τα URLs σε αυτά τα μεταδεδομένα. Το APIM θα χρησιμοποιήσει αυτές τις τιμές όπως είναι. 

- **Σειρά Πολιτικών:** Στην πολιτική APIM, τοποθετήστε το `<validate-jwt>` **πριν** από οποιοδήποτε routing προς το backend. Διαφορετικά, οι κλήσεις μπορεί να φτάσουν στην εφαρμογή σας χωρίς έγκυρο token. Επίσης, βεβαιωθείτε ότι το `<validate-jwt>` εμφανίζεται αμέσως κάτω από το `<inbound>` (όχι μέσα σε άλλη συνθήκη) ώστε το APIM να το εφαρμόζει.

Ακολουθώντας τα παραπάνω βήματα, μπορείτε να εκτελέσετε τον Spring AI MCP server σας σε Azure Container Apps και να έχετε το Azure API Management να επικυρώνει τα εισερχόμενα OAuth2 JWTs με μια ελάχιστη πολιτική. Τα βασικά σημεία είναι: εκθέστε δημόσια τα Spring Auth endpoints με TLS, ενεργοποιήστε την ανακάλυψη OIDC και ορίστε το `validate-jwt` του APIM στο URL διαμόρφωσης OpenID (ώστε να μπορεί αυτόματα να παίρνει το JWKS). Αυτή η ρύθμιση είναι κατάλληλη για περιβάλλον ανάπτυξης/δοκιμής· για παραγωγή, σκεφτείτε σωστή διαχείριση μυστικών, διάρκεια ζωής token και περιστροφή κλειδιών στο JWKS όπως απαιτείται. 


**Αναφορές:** Δείτε τα έγγραφα του Spring Authorization Server για τις προεπιλεγμένες τελικές σημεία ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) και τη ρύθμιση OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); δείτε τα έγγραφα Microsoft APIM για παραδείγματα `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); και τα έγγραφα Azure Container Apps για ανάπτυξη και πιστοποιητικά ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->