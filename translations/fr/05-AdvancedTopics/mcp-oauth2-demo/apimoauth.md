# Déploiement de l’application Spring AI MCP sur Azure Container Apps

([Sécurisation des serveurs Spring AI MCP avec OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figure : Serveur Spring AI MCP sécurisé avec Spring Authorization Server. Le serveur délivre des tokens d’accès aux clients et les valide lors des requêtes entrantes (source : blog Spring) ([Sécurisation des serveurs Spring AI MCP avec OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Pour déployer le serveur Spring MCP, construisez-le en tant que conteneur et utilisez Azure Container Apps avec un ingress externe. Par exemple, avec l’Azure CLI, vous pouvez exécuter :

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

Cela crée une Container App accessible publiquement avec HTTPS activé (Azure délivre un certificat TLS gratuit pour le domaine par défaut `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). La sortie de la commande inclut le FQDN de l’application (ex. `my-mcp-app.eastus.azurecontainerapps.io`), qui devient la base de l’**URL de l’émetteur**. Assurez-vous que l’ingress HTTP est activé (comme ci-dessus) pour que APIM puisse atteindre l’application. En environnement test/dev, utilisez l’option `--ingress external` (ou liez un domaine personnalisé avec TLS selon la documentation Microsoft ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Stockez les propriétés sensibles (comme les secrets clients OAuth) dans les secrets de Container Apps ou Azure Key Vault, puis mappez-les dans le conteneur en variables d’environnement.

## Configuration de Spring Authorization Server

Dans le code de votre application Spring Boot, incluez les starters Spring Authorization Server et Resource Server. Configurez un `RegisteredClient` (pour le grant `client_credentials` en dev/test) ainsi qu’une source de clés JWT. Par exemple, dans `application.properties`, vous pouvez définir :

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Activez le serveur d’autorisation et le serveur de ressources en définissant une chaîne de filtres de sécurité. Par exemple :

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

Cette configuration exposera les endpoints OAuth2 par défaut : `/oauth2/token` pour les tokens et `/oauth2/jwks` pour le JSON Web Key Set. (Par défaut, `AuthorizationServerSettings` de Spring mappe `/oauth2/token` et `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Le serveur délivrera des tokens d’accès JWT signés par la clé RSA définie ci-dessus, et publiera sa clé publique à l’adresse `https://<votre-app>:/oauth2/jwks`.

**Activez la découverte OpenID Connect :** Pour permettre à APIM de récupérer automatiquement l’émetteur et le JWKS, activez le endpoint de configuration du fournisseur OIDC en ajoutant `.oidc(Customizer.withDefaults())` dans votre configuration de sécurité ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Par exemple :

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Cela expose `/.well-known/openid-configuration`, que APIM peut utiliser pour récupérer les métadonnées. Enfin, vous pouvez vouloir personnaliser la revendication **audience** du JWT afin que la vérification `<audiences>` d’APIM soit validée. Par exemple, ajoutez un customizer de token :

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Cela garantit que les tokens contiennent `"aud": ["mcp-client"]`, correspondant à l’ID client ou au scope attendu par APIM.

## Exposition des endpoints Token et JWKS

Après déploiement, l’**URL de l’émetteur** de votre application sera `https://<app-fqdn>`, par exemple `https://my-mcp-app.eastus.azurecontainerapps.io`. Ses endpoints OAuth2 sont :

- **Endpoint Token :** `https://<app-fqdn>/oauth2/token` – les clients obtiennent les tokens ici (flux client_credentials).
- **Endpoint JWKS :** `https://<app-fqdn>/oauth2/jwks` – retourne le jeu de clés JWK (utilisé par APIM pour récupérer les clés de signature).
- **Configuration OpenID :** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de découverte OIDC (contient `issuer`, `token_endpoint`, `jwks_uri`, etc.).

APIM pointera vers l’**URL de configuration OpenID**, à partir de laquelle il découvre le `jwks_uri`. Par exemple, si le FQDN de votre Container App est `my-mcp-app.eastus.azurecontainerapps.io`, alors le `<openid-config url="...">` d’APIM doit utiliser `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Par défaut, Spring définit l’`issuer` dans ces métadonnées à la même URL de base ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configuration d’Azure API Management (`validate-jwt`)

Dans Azure APIM, ajoutez une politique inbound qui utilise la politique `<validate-jwt>` pour vérifier les JWT entrants contre votre Spring Authorization Server. Pour une configuration simple, vous pouvez utiliser l’URL des métadonnées OpenID Connect. Exemple de snippet de politique :

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

Cette politique indique à APIM de récupérer la configuration OpenID depuis Spring Auth Server, d’obtenir son JWKS, et de valider que chaque token est signé par une clé de confiance et possède la bonne audience. (Si vous omettez `<issuers>`, APIM utilisera automatiquement la revendication `issuer` des métadonnées.) Le `<audience>` doit correspondre à votre ID client ou à l’identifiant de la ressource API dans le token (dans l’exemple ci-dessus, nous l’avons défini à `"mcp-client"`). Ceci est conforme à la documentation Microsoft sur l’utilisation de `validate-jwt` avec `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Après validation, APIM transmettra la requête (y compris l’en-tête `Authorization` original) au backend. Comme l’application Spring est aussi un serveur de ressources, elle revalidera le token, mais APIM aura déjà assuré sa validité. (En développement, vous pouvez vous reposer sur la vérification d’APIM et désactiver les contrôles supplémentaires dans l’application si vous le souhaitez, mais il est plus sûr de garder les deux.)

## Paramètres d’exemple

| Paramètre          | Valeur Exemple                                                     | Notes                                      |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL de votre Container App (URI de base)  |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Endpoint token Spring par défaut ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Endpoint JWK Set par défaut ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Document de découverte OIDC (généré automatiquement)    |
| **Audience APIM**  | `mcp-client`                                                      | ID client OAuth ou nom de ressource API    |
| **Politique APIM** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` utilise cette URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Pièges courants

- **HTTPS/TLS :** La passerelle APIM exige que les endpoints OpenID/JWKS soient en HTTPS avec un certificat valide. Par défaut, Azure Container Apps fournit un certificat TLS de confiance pour le domaine géré par Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si vous utilisez un domaine personnalisé, veillez à lier un certificat (vous pouvez utiliser la fonctionnalité de certificat géré gratuit d’Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si APIM ne peut pas faire confiance au certificat du endpoint, `<validate-jwt>` échouera à récupérer les métadonnées.

- **Accessibilité des endpoints :** Assurez-vous que les endpoints de l’application Spring sont accessibles depuis APIM. Utiliser `--ingress external` (ou activer l’ingress dans le portail) est la solution la plus simple. Si vous avez choisi un environnement interne ou lié à un vNet, APIM (par défaut public) pourrait ne pas y accéder sauf s’il est dans le même vNet. En test, privilégiez un ingress public pour que APIM puisse appeler les URLs `.well-known` et `/jwks`.

- **Découverte OpenID activée :** Par défaut, Spring Authorization Server **n’expose pas** `/.well-known/openid-configuration` sauf si OIDC est activé. Veillez à inclure `.oidc(Customizer.withDefaults())` dans votre configuration de sécurité (voir ci-dessus) pour activer le endpoint de configuration du fournisseur ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Sinon, l’appel `<openid-config>` d’APIM retournera une erreur 404.

- **Revendication Audience :** Le comportement par défaut de Spring est de définir la revendication `aud` sur l’ID client. Si la vérification `<audience>` d’APIM échoue, vous devrez peut-être personnaliser le token (comme montré ci-dessus) ou ajuster la politique APIM. Assurez-vous que l’audience dans votre JWT correspond à ce que vous configurez dans `<audience>`.

- **Parsing des métadonnées JSON :** Le JSON de configuration OpenID doit être valide. La configuration par défaut de Spring émet un document standard OIDC. Vérifiez qu’il contient les bonnes valeurs pour `issuer` et `jwks_uri`. Si vous hébergez Spring derrière un proxy ou une route basée sur un chemin, vérifiez bien les URLs dans ces métadonnées. APIM utilisera ces valeurs telles quelles.

- **Ordre des politiques :** Dans la politique APIM, placez `<validate-jwt>` **avant** tout routage vers le backend. Sinon, les appels pourraient atteindre votre application sans token valide. Assurez-vous aussi que `<validate-jwt>` se trouve directement sous `<inbound>` (pas imbriqué dans une autre condition) pour que APIM l’applique.

En suivant ces étapes, vous pouvez exécuter votre serveur Spring AI MCP dans Azure Container Apps et faire valider les JWT OAuth2 entrants par Azure API Management avec une politique minimale. Les points clés sont : exposer publiquement les endpoints Spring Auth avec TLS, activer la découverte OIDC, et pointer la validation `validate-jwt` d’APIM vers l’URL de configuration OpenID (pour qu’il récupère automatiquement le JWKS). Cette configuration convient pour un environnement dev/test ; en production, pensez à une gestion appropriée des secrets, à la durée de vie des tokens et à la rotation des clés JWKS selon les besoins.
**Références :** Consultez la documentation de Spring Authorization Server pour les points de terminaison par défaut ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) et la configuration OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consultez la documentation Microsoft APIM pour des exemples de `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) ; et la documentation Azure Container Apps pour le déploiement et les certificats ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.