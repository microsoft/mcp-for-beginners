# Démonstration de Streaming HTTP du Calculateur

Ce projet illustre le streaming HTTP en utilisant les Server-Sent Events (SSE) avec Spring Boot WebFlux. Il se compose de deux applications :

- **Calculator Server** : un service web réactif qui effectue des calculs et diffuse les résultats via SSE
- **Calculator Client** : une application cliente qui consomme le point de terminaison de streaming

## Prérequis

- Java 17 ou supérieur
- Maven 3.6 ou supérieur

## Structure du Projet

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Fonctionnement

1. Le **Calculator Server** expose un point de terminaison `/calculate` qui :
   - Accepte les paramètres de requête : `a` (nombre), `b` (nombre), `op` (opération)
   - Opérations supportées : `add`, `sub`, `mul`, `div`
   - Retourne des Server-Sent Events avec la progression du calcul et le résultat

2. Le **Calculator Client** se connecte au serveur et :
   - Effectue une requête pour calculer `7 * 5`
   - Consomme la réponse en streaming
   - Affiche chaque événement dans la console

## Lancement des Applications

### Option 1 : Utilisation de Maven (recommandé)

#### 1. Démarrer le Calculator Server

Ouvrez un terminal et placez-vous dans le répertoire du serveur :

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Le serveur démarrera sur `http://localhost:8080`

Vous devriez voir une sortie similaire à :
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Lancer le Calculator Client

Ouvrez un **nouveau terminal** et placez-vous dans le répertoire du client :

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Le client se connectera au serveur, effectuera le calcul et affichera les résultats en streaming.

### Option 2 : Utilisation directe de Java

#### 1. Compiler et lancer le serveur :

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compiler et lancer le client :

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Tester le Serveur Manuellement

Vous pouvez aussi tester le serveur via un navigateur web ou curl :

### Avec un navigateur web :
Visitez : `http://localhost:8080/calculate?a=10&b=5&op=add`

### Avec curl :
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Résultat Attendu

Lors de l’exécution du client, vous devriez voir un flux de sortie similaire à :

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Opérations Supportées

- `add` - Addition (a + b)
- `sub` - Soustraction (a - b)
- `mul` - Multiplication (a * b)
- `div` - Division (a / b, retourne NaN si b = 0)

## Référence API

### GET /calculate

**Paramètres :**
- `a` (obligatoire) : Premier nombre (double)
- `b` (obligatoire) : Second nombre (double)
- `op` (obligatoire) : Opération (`add`, `sub`, `mul`, `div`)

**Réponse :**
- Content-Type : `text/event-stream`
- Retourne des Server-Sent Events avec la progression du calcul et le résultat

**Exemple de requête :**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Exemple de réponse :**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Dépannage

### Problèmes Courants

1. **Port 8080 déjà utilisé**
   - Arrêtez toute autre application utilisant le port 8080
   - Ou modifiez le port du serveur dans `calculator-server/src/main/resources/application.yml`

2. **Connexion refusée**
   - Assurez-vous que le serveur est lancé avant de démarrer le client
   - Vérifiez que le serveur a bien démarré sur le port 8080

3. **Problèmes de nom de paramètre**
   - Ce projet inclut une configuration Maven du compilateur avec le flag `-parameters`
   - Si vous rencontrez des problèmes de liaison des paramètres, assurez-vous que le projet est construit avec cette configuration

### Arrêter les Applications

- Appuyez sur `Ctrl+C` dans le terminal où chaque application tourne
- Ou utilisez `mvn spring-boot:stop` si elles tournent en arrière-plan

## Stack Technologique

- **Spring Boot 3.3.1** - Framework d’application
- **Spring WebFlux** - Framework web réactif
- **Project Reactor** - Bibliothèque de flux réactifs
- **Netty** - Serveur I/O non bloquant
- **Maven** - Outil de build
- **Java 17+** - Langage de programmation

## Étapes Suivantes

Essayez de modifier le code pour :
- Ajouter plus d’opérations mathématiques
- Inclure la gestion des erreurs pour les opérations invalides
- Ajouter la journalisation des requêtes/réponses
- Implémenter l’authentification
- Ajouter des tests unitaires

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.