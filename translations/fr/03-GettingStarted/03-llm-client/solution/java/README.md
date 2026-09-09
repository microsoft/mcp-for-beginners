# Client Calculatrice LLM

Une application Java qui démontre comment utiliser LangChain4j pour se connecter à un service calculatrice MCP (Model Context Protocol) via l'API MiniMax compatible OpenAI.

## Prérequis

- Java 21 ou supérieur
- Maven 3.6+ (ou utilisez le wrapper Maven inclus)
- Une clé API MiniMax
- Un service calculatrice MCP fonctionnant à `http://localhost:8080`

## Obtention de la clé API

Cette application utilise l'API MiniMax compatible OpenAI. Suivez ces étapes pour obtenir votre clé et votre endpoint :

### 1. Choisir un endpoint
1. Utilisez `https://api.minimax.io/v1` pour l'endpoint global
2. Utilisez `https://api.minimaxi.com/v1` pour l'endpoint Chine

### 2. Créer une clé API
1. Créez une clé API MiniMax depuis votre compte MiniMax
2. Conservez la clé en lieu sûr

### 3. Configurer les variables d'environnement

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

1. **Clonez ou accédez au répertoire du projet**

2. **Installez les dépendances** :
   ```cmd
   mvnw clean install
   ```
   Ou si Maven est installé globalement :
   ```cmd
   mvn clean install
   ```

3. **Configurez les variables d'environnement** (voir la section "Obtention de la clé API" ci-dessus)

4. **Démarrez le service calculatrice MCP** :
   Assurez-vous que le service calculatrice MCP du chapitre 1 est en fonctionnement sur `http://localhost:8080/sse`. Il doit être en marche avant de démarrer le client.

## Exécution de l'application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ce que fait l'application

L'application démontre trois interactions principales avec le service calculatrice :

1. **Addition** : Calcule la somme de 24.5 et 17.3
2. **Racine carrée** : Calcule la racine carrée de 144
3. **Aide** : Affiche les fonctions disponibles de la calculatrice

## Résultat attendu

Lorsque l'exécution réussit, vous devriez voir une sortie similaire à :

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Dépannage

### Problèmes courants

1. **"La variable d'environnement OPENAI_API_KEY n'est pas définie"**
   - Assurez-vous d'avoir défini la variable d'environnement `OPENAI_API_KEY`
   - Redémarrez votre terminal/invite de commandes après avoir défini la variable

2. **"Connexion refusée à localhost:8080"**
   - Vérifiez que le service calculatrice MCP fonctionne sur le port 8080
   - Vérifiez si un autre service utilise le port 8080

3. **"Échec de l'authentification"**
   - Vérifiez que votre clé API est valide
   - Vérifiez que `OPENAI_BASE_URL` correspond à l'endpoint que vous souhaitez utiliser

4. **Erreurs de compilation Maven**
   - Assurez-vous d'utiliser Java 21 ou supérieur : `java -version`
   - Essayez de nettoyer la compilation : `mvnw clean`

### Débogage

Pour activer les logs de débogage, ajoutez l'argument JVM suivant lors de l'exécution :
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

L'application est configurée pour :
- Utiliser MiniMax-M3 par défaut, ou MiniMax-M2.7 lorsque `MINIMAX_MODEL_ID` est défini
- Se connecter à `OPENAI_BASE_URL` lorsqu'il est défini ; sinon utiliser `https://api.minimaxi.com/v1` lorsque `MINIMAX_REGION=cn_zh`, ou `https://api.minimax.io/v1` par défaut
- Se connecter au service MCP à `http://localhost:8080/sse`
- Utiliser un timeout de 60 secondes pour les requêtes

## Dépendances

Dépendances clés utilisées dans ce projet :
- **LangChain4j** : Pour l'intégration IA et la gestion des outils
- **LangChain4j MCP** : Pour la prise en charge du Model Context Protocol
- **LangChain4j OpenAI officiel** : Pour l'intégration de l'API MiniMax compatible OpenAI
- **Spring Boot** : Pour le framework d'application et l'injection de dépendances

## Licence

Ce projet est sous licence Apache 2.0 - voir le fichier [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) pour plus de détails.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->