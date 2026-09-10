# Client Calculatrice LLM

Une application Java qui démontre comment utiliser LangChain4j pour se connecter à un service de calculatrice MCP (Model Context Protocol) via l'API MiniMax compatible OpenAI.

## Prérequis

- Java 21 ou supérieur
- Maven 3.6+ (ou utilisez le wrapper Maven fourni)
- Une clé API MiniMax
- Un service de calculatrice MCP en fonctionnement sur `http://localhost:8080`

## Obtention de la clé API

Cette application utilise l'API MiniMax compatible OpenAI. Suivez ces étapes pour obtenir votre clé et point de terminaison :

### 1. Choisissez un point de terminaison
1. Utilisez `https://api.minimax.io/v1` pour le point de terminaison global
2. Utilisez `https://api.minimaxi.com/v1` pour le point de terminaison Chine

### 2. Créez une clé API
1. Créez une clé API MiniMax depuis votre compte MiniMax
2. Conservez la clé en lieu sûr

### 3. Configurez les variables d’environnement

#### Sous Windows (Invite de commandes) :
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Sous Windows (PowerShell) :
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Sous macOS/Linux :
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Configuration et Installation

1. **Clonez ou allez dans le répertoire du projet**

2. **Installez les dépendances** :
   ```cmd
   mvnw clean install
   ```
   Ou si Maven est installé globalement :
   ```cmd
   mvn clean install
   ```

3. **Configurez les variables d’environnement** (voir la section "Obtention de la clé API" ci-dessus)

4. **Démarrez le Service Calculatrice MCP** :
   Assurez-vous que le service calculatrice MCP du chapitre 1 fonctionne sur `http://localhost:8080/sse`. Il doit être lancé avant de démarrer le client.

## Exécution de l’application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ce que fait l’application

L’application démontre trois interactions principales avec le service calculatrice :

1. **Addition** : Calcule la somme de 24,5 et 17,3
2. **Racine carrée** : Calcule la racine carrée de 144
3. **Aide** : Affiche les fonctions disponibles de la calculatrice

## Résultat attendu

En cas d’exécution réussie, vous devriez voir une sortie similaire à :

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Résolution des problèmes

### Problèmes courants

1. **"La variable d’environnement OPENAI_API_KEY n’est pas définie"**
   - Assurez-vous d’avoir défini la variable d’environnement `OPENAI_API_KEY`
   - Redémarrez votre terminal/invite de commandes après avoir défini la variable

2. **"Connexion refusée à localhost:8080"**
   - Vérifiez que le service calculatrice MCP fonctionne sur le port 8080
   - Vérifiez qu’aucun autre service n’utilise le port 8080

3. **"Échec d’authentification"**
   - Vérifiez que votre clé API est valide
   - Vérifiez que `OPENAI_BASE_URL` correspond bien au point de terminaison que vous souhaitez utiliser

4. **Erreurs de compilation Maven**
   - Assurez-vous d’utiliser Java 21 ou supérieur : `java -version`
   - Essayez de nettoyer la compilation : `mvnw clean`

### Débogage

Pour activer la journalisation debug, ajoutez l’argument JVM suivant lors de l’exécution :
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

L’application est configurée pour :
- Utiliser MiniMax-M3 par défaut ; régler `MINIMAX_MODEL_ID` pour choisir entre `MiniMax-M3` ou `MiniMax-M2.7`
- Se connecter à `OPENAI_BASE_URL` si défini ; sinon utiliser `https://api.minimaxi.com/v1` si `MINIMAX_REGION=cn_zh`, ou `https://api.minimax.io/v1` par défaut
- Se connecter au service MCP à `http://localhost:8080/sse`
- Utiliser un délai d’attente de 60 secondes pour les requêtes

## Dépendances

Dépendances clés utilisées dans ce projet :
- **LangChain4j** : Pour l’intégration IA et la gestion des outils
- **LangChain4j MCP** : Pour le support du Model Context Protocol
- **LangChain4j OpenAI officiel** : Pour l’intégration de l’API MiniMax compatible OpenAI
- **Spring Boot** : Pour le cadre applicatif et l’injection de dépendances

## Licence

Ce projet est sous licence Apache 2.0 - voir le fichier [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) pour les détails.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->