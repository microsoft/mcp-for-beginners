# Démo MCP OAuth2

> [!WARNING]
> Ceci est un exemple local d’apprentissage, pas un service d'autorisation en production. Il
> utilise un client en mémoire et génère une nouvelle clé de signature au démarrage. Ne
> le déployez jamais avec un secret client partagé, par défaut ou contrôlé par source.

## Introduction

OAuth2 est le protocole standard industriel pour l'autorisation, permettant un accès sécurisé aux ressources sans partager les identifiants. Dans les implémentations MCP (Model Context Protocol), OAuth2 fournit un moyen robuste d'authentifier et d’autoriser les clients (comme les agents IA) à accéder aux serveurs MCP et à leurs outils.

Cette leçon montre comment implémenter l’authentification OAuth2 pour les serveurs MCP en utilisant Spring Boot, un schéma courant pour les déploiements en entreprise et en production.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :
- Comprendre comment OAuth2 s’intègre aux serveurs MCP
- Implémenter un serveur d’autorisation Spring pour la délivrance de jetons
- Protéger les points de terminaison MCP avec une authentification JWT
- Configurer le flux client credentials pour la communication machine-à-machine

## Pré-requis

- Connaissances de base en Java et Spring Boot
- Familiarité avec les concepts MCP des modules précédents
- Maven ou Gradle installés

---

## Aperçu du projet

Ce projet est une **application minimaliste Spring Boot** qui agit à la fois comme :

* un **Serveur d’autorisation Spring** (délivrant des jetons d’accès JWT via le flux `client_credentials`), et  
* un **Serveur de ressources** (protégeant son propre point de terminaison `/hello`).

Il reflète la configuration présentée dans le [article de blog Spring (2 avril 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Démarrage rapide (local)

```bash
# Utilisez une valeur locale unique et évitez de la laisser dans l'historique du shell autant que possible.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# obtenir un jeton
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# appeler le point de terminaison protégé
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Tester la configuration OAuth2

Vous pouvez tester la configuration de sécurité OAuth2 en suivant ces étapes :

### 1. Vérifier que le serveur fonctionne et est sécurisé

```bash
# Cela devrait renvoyer 401 Non autorisé, confirmant que la sécurité OAuth2 est active
curl -v http://localhost:8081/
```

### 2. Obtenir un jeton d’accès avec les identifiants client

```bash
# Obtenir et extraire la réponse complète du jeton
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Ou pour extraire uniquement le jeton (requiert jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Sur PowerShell, définissez le secret local avant d’exécuter Maven :

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Accéder au point de terminaison protégé avec le jeton

```bash
# Utilisation du jeton enregistré
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Ou directement avec la valeur du jeton
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Une réponse réussie avec "Hello from MCP OAuth2 Demo!" confirme que la configuration OAuth2 fonctionne correctement.

---

## Construction du conteneur

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Sécurité en production

Pour un déploiement en production, utilisez un fournisseur d'identité dédié plutôt que
ce serveur d'autorisation de démonstration en processus. Stockez les identifiants dans un
magasin de secrets géré, faites-les tourner, utilisez des clés de signature persistantes, restreignez les scopes, et
définissez un émetteur explicite. Ne placez jamais un secret client dans le code source, les images de conteneurs,
les manifests de déploiement ou la sortie en ligne de commande.

Pour Azure Container Apps, stockez la valeur en tant que secret Container Apps soutenu par
Key Vault si possible, puis exposez seulement une référence secrète via la
variable d’environnement `OAUTH_CLIENT_SECRET`.

---

## Déployer sur **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Le FQDN d’entrée devient votre **émetteur** (`https://<fqdn>`).  
Azure fournit automatiquement un certificat TLS de confiance pour `*.azurecontainerapps.io`.

---

## Intégrer à **Azure API Management**

Ajoutez cette politique entrante à votre API :

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

APIM récupérera le JWKS et validera chaque requête.

---

## Et ensuite

- [5.4 Contextes racines](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->