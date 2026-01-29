# Client Calculator LLM

Une application Java qui montre comment utiliser LangChain4j pour se connecter à un service de calculateur MCP (Model Context Protocol) avec intégration des GitHub Models.

## Prérequis

- Java 21 ou supérieur
- Maven 3.6+ (ou utilisez le wrapper Maven inclus)
- Un compte GitHub avec accès aux GitHub Models
- Un service de calculateur MCP en fonctionnement sur `http://localhost:8080`

## Obtention du Token GitHub

Cette application utilise les GitHub Models, ce qui nécessite un token d'accès personnel GitHub. Suivez ces étapes pour obtenir votre token :

### 1. Accéder aux GitHub Models
1. Rendez-vous sur [GitHub Models](https://github.com/marketplace/models)
2. Connectez-vous avec votre compte GitHub
3. Demandez l'accès aux GitHub Models si ce n'est pas déjà fait

### 2. Créer un Token d'Accès Personnel
1. Allez dans [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Cliquez sur "Generate new token" → "Generate new token (classic)"
3. Donnez un nom descriptif à votre token (par exemple, "MCP Calculator Client")
4. Définissez la durée d'expiration selon vos besoins
5. Sélectionnez les scopes suivants :
   - `repo` (si vous accédez à des dépôts privés)
   - `user:email`
6. Cliquez sur "Generate token"
7. **Important** : Copiez immédiatement le token - vous ne pourrez plus le voir par la suite !

### 3. Configurer la Variable d’Environnement

#### Sur Windows (Invite de commandes) :
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Sur Windows (PowerShell) :
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Sur macOS/Linux :
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Installation et Configuration

1. **Cloner ou naviguer vers le répertoire du projet**

2. **Installer les dépendances** :
   ```cmd
   mvnw clean install
   ```
   Ou si Maven est installé globalement :
   ```cmd
   mvn clean install
   ```

3. **Configurer la variable d’environnement** (voir la section "Obtention du Token GitHub" ci-dessus)

4. **Démarrer le service MCP Calculator** :
   Assurez-vous que le service MCP calculator du chapitre 1 fonctionne sur `http://localhost:8080/sse`. Il doit être lancé avant de démarrer le client.

## Exécution de l’Application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Fonctionnalités de l’Application

L’application illustre trois interactions principales avec le service de calcul :

1. **Addition** : Calcule la somme de 24,5 et 17,3
2. **Racine carrée** : Calcule la racine carrée de 144
3. **Aide** : Affiche les fonctions disponibles du calculateur

## Résultat Attendu

En cas de succès, vous devriez voir une sortie similaire à :

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Dépannage

### Problèmes Courants

1. **"GITHUB_TOKEN environment variable not set"**
   - Vérifiez que la variable d’environnement `GITHUB_TOKEN` est bien définie
   - Redémarrez votre terminal/invite de commandes après avoir configuré la variable

2. **"Connection refused to localhost:8080"**
   - Assurez-vous que le service MCP calculator tourne bien sur le port 8080
   - Vérifiez qu’aucun autre service n’utilise le port 8080

3. **"Authentication failed"**
   - Vérifiez que votre token GitHub est valide et possède les permissions nécessaires
   - Assurez-vous d’avoir accès aux GitHub Models

4. **Erreurs de build Maven**
   - Vérifiez que vous utilisez Java 21 ou supérieur : `java -version`
   - Essayez de nettoyer la build : `mvnw clean`

### Débogage

Pour activer les logs de débogage, ajoutez l’argument JVM suivant lors de l’exécution :
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

L’application est configurée pour :
- Utiliser les GitHub Models avec le modèle `gpt-4.1-nano`
- Se connecter au service MCP à l’adresse `http://localhost:8080/sse`
- Utiliser un timeout de 60 secondes pour les requêtes
- Activer la journalisation des requêtes/réponses pour le débogage

## Dépendances

Principales dépendances utilisées dans ce projet :
- **LangChain4j** : pour l’intégration IA et la gestion des outils
- **LangChain4j MCP** : pour le support du Model Context Protocol
- **LangChain4j GitHub Models** : pour l’intégration des GitHub Models
- **Spring Boot** : pour le framework applicatif et l’injection de dépendances

## Licence

Ce projet est sous licence Apache 2.0 - voir le fichier [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) pour plus de détails.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.