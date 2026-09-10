# Déploiement de l’application Spring AI MCP sur Azure Container Apps

> [!WARNING]
> Ce serveur combiné d’autorisation/ressource est destiné à l’apprentissage et à un usage dev/test. Les systèmes de production doivent utiliser un fournisseur d’identité dédié, des clés de signature persistantes, et des identifiants stockés dans un magasin de secrets géré.
> 
> 

 ([Sécurisation des serveurs Spring AI MCP avec OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figure : Serveur Spring AI MCP sécurisé avec Spring Authorization Server. Le serveur émet des jetons d’accès aux clients et les valide lors des requêtes entrantes (source : blog Spring) ([Sécurisation des serveurs Spring AI MCP avec OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Pour déployer le serveur Spring MCP, construisez-le en tant que conteneur et utilisez Azure Container Apps avec un ingress externe. Par exemple, avec l’Azure CLI vous pouvez exécuter :

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

Cela crée une Container App accessible publiquement avec HTTPS activé (Azure émet un certificat TLS gratuit pour le domaine par défaut `*.azurecontainerapps.io` ([Noms de domaine personnalisés et certificats gérés gratuits dans Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). La sortie de la commande inclut le FQDN de l’application (ex. `my-mcp-app.eastus.azurecontainerapps.io`), qui devient la base de l’**URL de l’émetteur**. Assurez-vous que l’ingress HTTP est activé (comme ci-dessus) pour que APIM puisse atteindre l’application. Dans un environnement test/dev, utilisez l’option `--ingress external` (ou liez un domaine personnalisé avec TLS selon [docs Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Noms de domaine personnalisés et certificats gérés gratuits dans Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Stockez toute propriété sensible (comme les secrets clients OAuth) dans les secrets de Container Apps ou Azure Key Vault, et mappez-les dans le conteneur en variables d’environnement.

## Configuration de Spring Authorization Server

Dans le code de votre application Spring Boot, incluez les starters Spring Authorization Server et Resource Server. Configurez un `RegisteredClient` (pour la grant `client_credentials` en dev/test) et une source de clé JWT. Par exemple, dans `application.properties` vous pouvez définir :

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Activez Authorization Server et Resource Server en définissant une chaîne de filtres de sécurité. Par exemple :

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Activer les points de terminaison du serveur d'autorisation
            .apply(authzServer.and())
            // Activer le serveur de ressources (valider le JWT sur les requêtes entrantes)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Désactiver CSRF (le serveur MCP n'est pas basé sur un navigateur)
            .csrf(csrf -> csrf.disable())
            // Autoriser CORS pour les outils clients de démonstration
            .cors(withDefaults());
        return http.build();
    }

    // Définir un client en mémoire (RegisteredClient) et une source JWK :
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
        // Générer une clé RSA (pour dev/test, générer à nouveau au démarrage)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Cette configuration exposera les endpoints OAuth2 par défaut : `/oauth2/token` pour les jetons et `/oauth2/jwks` pour le JSON Web Key Set. (Par défaut `AuthorizationServerSettings` de Spring mappe `/oauth2/token` et `/oauth2/jwks` ([Modèle de configuration :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Le serveur émettra des jetons JWT signés par la clé RSA ci-dessus et publiera sa clé publique à l’URL `https://<votre-app>:/oauth2/jwks`.

**Activez la découverte OpenID Connect :** Pour permettre à APIM de récupérer automatiquement l’émetteur et le JWKS, activez le endpoint de configuration du fournisseur OIDC en ajoutant `.oidc(Customizer.withDefaults())` dans votre configuration de sécurité ([Modèle de configuration :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Par exemple :

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– active /.well-known/openid-configuration
```

Cela expose `/.well-known/openid-configuration`, que APIM peut utiliser pour les métadonnées. Enfin, vous pouvez souhaiter personnaliser la revendication JWT **audience** afin que la vérification `<audiences>` d’APIM soit validée. Par exemple, ajoutez un customizer de jeton :

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Définir une audience personnalisée (par exemple l'ID client ou l'identifiant de l'API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ceci garantit que les jetons portent `"aud": ["mcp-client"]`, correspondant à l’ID client ou au scope attendu par APIM.

## Exposition des endpoints Token et JWKS

Après déploiement, l’**URL de l’émetteur** de votre app sera `https://<app-fqdn>`, par exemple `https://my-mcp-app.eastus.azurecontainerapps.io`. Ses endpoints OAuth2 sont :

- **Endpoint Token :** `https://<app-fqdn>/oauth2/token` – les clients obtiennent les jetons ici (flux client_credentials).
- **Endpoint JWKS :** `https://<app-fqdn>/oauth2/jwks` – renvoie le jeu de clés JWK (utilisé par APIM pour obtenir les clés de signature).
- **Config OpenID :** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de découverte OIDC (contient `issuer`, `token_endpoint`, `jwks_uri`, etc.).  

APIM pointera sur l’**URL de configuration OpenID**, depuis laquelle il découvre le `jwks_uri`. Par exemple, si le FQDN de votre Container App est `my-mcp-app.eastus.azurecontainerapps.io`, alors le `<openid-config url="...">` d’APIM doit utiliser `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Par défaut Spring définira l’`issuer` dans ces métadonnées sur la même URL de base ([Modèle de configuration :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configuration d’Azure API Management (`validate-jwt`)

Dans Azure APIM, ajoutez une politique entrante utilisant la politique `<validate-jwt>` pour vérifier les JWT entrants contre votre Spring Authorization Server. Pour une configuration simple, vous pouvez utiliser l’URL de métadonnées OpenID Connect. Exemple d’extrait de politique :

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

Cette politique indique à APIM de récupérer la configuration OpenID depuis Spring Auth Server, d’obtenir son JWKS, et de valider que chaque jeton est signé par une clé de confiance et possède la bonne audience. (Si vous omettez `<issuers>`, APIM utilisera automatiquement la revendication `issuer` des métadonnées.) Le `<audience>` doit correspondre à votre ID client ou identifiant de ressource API dans le jeton (dans l’exemple ci-dessus, on l’a fixé à `"mcp-client"`). Ceci est conforme à la documentation Microsoft sur l’utilisation de `validate-jwt` avec `<openid-config>` ([Référence politique Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Après validation, APIM transmettra la requête (y compris l’en-tête `Authorization` original) au backend. Étant donné que l’app Spring est aussi un serveur de ressources, elle re-validera le jeton, mais APIM a déjà assuré sa validité. (Pour le développement, vous pouvez vous appuyer sur la vérification d’APIM et désactiver les vérifications supplémentaires dans l’application si vous le souhaitez, mais il est plus sûr de conserver les deux.)

## Exemples de paramètres

| Paramètre          | Valeur Exemple                                                     | Notes                                      |
|--------------------|------------------------------------------------------------------|--------------------------------------------|
| **Émetteur**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                | URL de base de votre Container App         |
| **Endpoint Token**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | Endpoint token Spring par défaut ([Modèle de configuration :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Endpoint JWKS**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | Endpoint JWK Set par défaut ([Modèle de configuration :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Config OpenID**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Document de découverte OIDC (généré automatiquement)  |
| **Audience APIM**   | `mcp-client`                                                     | ID client OAuth ou nom de ressource API     |
| **Politique APIM**  | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` utilise cette URL ([Référence politique Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Pièges courants

- **HTTPS/TLS :** La passerelle APIM exige que l’endpoint OpenID/JWKS soit en HTTPS avec un certificat valide. Par défaut, Azure Container Apps fournit un certificat TLS de confiance pour le domaine géré par Azure ([Noms de domaine personnalisés et certificats gérés gratuits dans Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si vous utilisez un domaine personnalisé, assurez-vous de lier un certificat (vous pouvez utiliser la fonctionnalité certifié managé gratuite d’Azure) ([Noms de domaine personnalisés et certificats gérés gratuits dans Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si APIM ne fait pas confiance au certificat de l’endpoint, `<validate-jwt>` échouera à récupérer les métadonnées.

- **Accessibilité de l’endpoint :** Assurez-vous que les endpoints de l’app Spring sont accessibles depuis APIM. Utiliser `--ingress external` (ou activer l’ingress dans le portail) est le plus simple. Si vous avez choisi un environnement interne ou lié à un vNet, APIM (par défaut public) pourrait ne pas y accéder sauf s’il est placé dans le même VNet. Dans un setup de test, préférez un ingress public pour que APIM puisse appeler les URLs `.well-known` et `/jwks`.

- **Découverte OpenID activée :** Par défaut, Spring Authorization Server **n’expose pas** `/.well-known/openid-configuration` à moins que OIDC soit activé. Assurez-vous d’inclure `.oidc(Customizer.withDefaults())` dans votre config de sécurité (voir ci-dessus) pour que l’endpoint de configuration du fournisseur soit actif ([Modèle de configuration :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Sinon, l’appel `<openid-config>` d’APIM renverra un 404.

- **Revendication Audience :** Le comportement par défaut de Spring est de mettre la revendication `aud` à l’ID client. Si la vérification `<audience>` d’APIM échoue, vous devrez peut-être personnaliser le jeton (comme montré ci-dessus) ou ajuster la politique APIM. Assurez-vous que l’audience dans votre JWT correspond à ce que vous configurez dans `<audience>`.

- **Analyse des métadonnées JSON :** Le JSON de configuration OpenID doit être valide. La config par défaut de Spring émettra un document standard de métadonnées OIDC. Vérifiez qu’il contient bien `issuer` et `jwks_uri`. Si vous hébergez Spring derrière un proxy ou un routage basé sur des chemins, vérifiez les URLs dans ces métadonnées. APIM utilisera ces valeurs telles quelles.

- **Ordonnancement des politiques :** Dans la politique APIM, placez `<validate-jwt>` **avant** tout routage vers le backend. Sinon, les appels pourraient atteindre votre app sans jeton valide. Assurez-vous aussi que `<validate-jwt>` apparaisse immédiatement sous `<inbound>` (pas imbriqué dans une autre condition) pour que APIM l’applique.

En suivant les étapes ci-dessus, vous pouvez exécuter votre serveur Spring AI MCP dans Azure Container Apps et faire valider les JWT OAuth2 entrants par Azure API Management avec une politique minimale. Les points clés sont : exposer publiquement les endpoints Spring Auth avec TLS, activer la découverte OIDC, et pointer `validate-jwt` d’APIM sur l’URL config OpenID (pour qu’il récupère automatiquement le JWKS). Cette configuration est adaptée à un environnement dev/test ; pour la production, envisagez une bonne gestion des secrets, des durées de vie de jeton, et la rotation des clés dans le JWKS selon les besoins.


**Références :** Voir la documentation de Spring Authorization Server pour les points de terminaison par défaut ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) et la configuration OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); voir la documentation Microsoft APIM pour des exemples `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); et la documentation Azure Container Apps pour le déploiement et les certificats ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->