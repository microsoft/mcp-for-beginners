# MCP Java Client - Démonstration Calculatrice

Ce projet montre comment créer un client Java qui se connecte à un serveur MCP (Model Context Protocol) et interagit avec lui. Dans cet exemple, nous allons nous connecter au serveur calculatrice du Chapitre 01 et effectuer diverses opérations mathématiques.

## Prérequis

Avant d’exécuter ce client, vous devez :

1. **Démarrer le serveur Calculatrice** du Chapitre 01 :
   - Rendez-vous dans le répertoire du serveur calculatrice : `03-GettingStarted/01-first-server/solution/java/`
   - Construisez et lancez le serveur calculatrice :
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Le serveur doit être accessible à l’adresse `http://localhost:8080`

2. **Java 21 ou version supérieure** installé sur votre système  
3. **Maven** (inclus via Maven Wrapper)

## Qu’est-ce que le SDKClient ?

Le `SDKClient` est une application Java qui montre comment :
- Se connecter à un serveur MCP en utilisant le transport Server-Sent Events (SSE)
- Lister les outils disponibles sur le serveur
- Appeler à distance différentes fonctions de la calculatrice
- Gérer les réponses et afficher les résultats

## Comment ça fonctionne

Le client utilise le framework Spring AI MCP pour :

1. **Établir la connexion** : crée un client WebFlux SSE pour se connecter au serveur calculatrice  
2. **Initialiser le client** : configure le client MCP et établit la connexion  
3. **Découvrir les outils** : liste toutes les opérations de la calculatrice disponibles  
4. **Exécuter les opérations** : appelle différentes fonctions mathématiques avec des données d’exemple  
5. **Afficher les résultats** : présente les résultats de chaque calcul

## Structure du projet

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Dépendances principales

Le projet utilise les dépendances clés suivantes :

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Cette dépendance fournit :  
- `McpClient` - L’interface principale du client  
- `WebFluxSseClientTransport` - Transport SSE pour la communication web  
- Les schémas du protocole MCP ainsi que les types de requêtes/réponses

## Compilation du projet

Compilez le projet en utilisant le wrapper Maven :

```cmd
.\mvnw clean install
```

## Exécution du client

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note** : Assurez-vous que le serveur calculatrice est bien lancé sur `http://localhost:8080` avant d’exécuter ces commandes.

## Ce que fait le client

Lorsque vous lancez le client, il va :

1. **Se connecter** au serveur calculatrice à l’adresse `http://localhost:8080`  
2. **Lister les outils** - Affiche toutes les opérations disponibles de la calculatrice  
3. **Effectuer des calculs** :  
   - Addition : 5 + 3 = 8  
   - Soustraction : 10 - 4 = 6  
   - Multiplication : 6 × 7 = 42  
   - Division : 20 ÷ 4 = 5  
   - Puissance : 2^8 = 256  
   - Racine carrée : √16 = 4  
   - Valeur absolue : |-5.5| = 5.5  
   - Aide : Affiche les opérations disponibles

## Résultat attendu

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Note** : Vous pouvez voir des avertissements Maven concernant des threads persistants à la fin - c’est normal pour les applications réactives et cela ne signifie pas une erreur.

## Comprendre le code

### 1. Configuration du transport  
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```  
Cela crée un transport SSE (Server-Sent Events) qui se connecte au serveur calculatrice.

### 2. Création du client  
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```  
Crée un client MCP synchrone et initialise la connexion.

### 3. Appel des outils  
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```  
Appelle l’outil "add" avec les paramètres a=5.0 et b=3.0.

## Dépannage

### Serveur non démarré  
Si vous obtenez des erreurs de connexion, assurez-vous que le serveur calculatrice du Chapitre 01 est bien lancé :  
```
Error: Connection refused
```  
**Solution** : Démarrez d’abord le serveur calculatrice.

### Port déjà utilisé  
Si le port 8080 est occupé :  
```
Error: Address already in use
```  
**Solution** : Arrêtez les autres applications utilisant le port 8080 ou modifiez le serveur pour utiliser un autre port.

### Erreurs de compilation  
Si vous rencontrez des erreurs lors de la compilation :  
```cmd
.\mvnw clean install -DskipTests
```

## Pour en savoir plus

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)  
- [Spécification Model Context Protocol](https://modelcontextprotocol.io/)  
- [Documentation Spring WebFlux](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.