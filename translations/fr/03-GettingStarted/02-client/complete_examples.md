# Exemples Complets de Clients MCP

Ce répertoire contient des exemples complets et fonctionnels de clients MCP dans différents langages de programmation. Chaque client illustre l'ensemble des fonctionnalités décrites dans le tutoriel principal README.md.

## Clients Disponibles

### 1. Client Java (`client_example_java.java`)

- **Transport** : SSE (Server-Sent Events) via HTTP
- **Serveur Cible** : `http://localhost:8080`
- **Fonctionnalités** :
  - Établissement de la connexion et ping
  - Liste des outils
  - Opérations de calculatrice (addition, soustraction, multiplication, division, aide)
  - Gestion des erreurs et extraction des résultats

**Pour exécuter :**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. Client C# (`client_example_csharp.cs`)

- **Transport** : Stdio (Entrée/Sortie Standard)
- **Serveur Cible** : Serveur MCP local .NET via dotnet run
- **Fonctionnalités** :
  - Démarrage automatique du serveur via le transport stdio
  - Liste des outils et des ressources
  - Opérations de calculatrice
  - Analyse des résultats JSON
  - Gestion complète des erreurs

**Pour exécuter :**

```bash
dotnet run
```

### 3. Client TypeScript (`client_example_typescript.ts`)

- **Transport** : Stdio (Entrée/Sortie Standard)
- **Serveur Cible** : Serveur MCP local Node.js
- **Fonctionnalités** :
  - Support complet du protocole MCP
  - Opérations sur les outils, ressources et invites
  - Opérations de calculatrice
  - Lecture des ressources et exécution des invites
  - Gestion robuste des erreurs

**Pour exécuter :**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Client Python (`client_example_python.py`)

- **Transport** : Stdio (Entrée/Sortie Standard)  
- **Serveur Cible** : Serveur MCP local Python
- **Fonctionnalités** :
  - Modèle async/await pour les opérations
  - Découverte des outils et des ressources
  - Test des opérations de calculatrice
  - Lecture du contenu des ressources
  - Organisation basée sur les classes

**Pour exécuter :**

```bash
python client_example_python.py
```

## Fonctionnalités Communes à Tous les Clients

Chaque implémentation de client illustre :

1. **Gestion de la Connexion**
   - Établissement de la connexion au serveur MCP
   - Gestion des erreurs de connexion
   - Nettoyage approprié et gestion des ressources

2. **Découverte du Serveur**
   - Liste des outils disponibles
   - Liste des ressources disponibles (si pris en charge)
   - Liste des invites disponibles (si pris en charge)

3. **Invocation des Outils**
   - Opérations de calculatrice de base (addition, soustraction, multiplication, division)
   - Commande d'aide pour les informations sur le serveur
   - Passage correct des arguments et gestion des résultats

4. **Gestion des Erreurs**
   - Erreurs de connexion
   - Erreurs d'exécution des outils
   - Échecs gracieux et retour d'information à l'utilisateur

5. **Traitement des Résultats**
   - Extraction du contenu textuel des réponses
   - Formatage des résultats pour une meilleure lisibilité
   - Gestion des différents formats de réponse

## Prérequis

Avant d'exécuter ces clients, assurez-vous d'avoir :

1. **Le serveur MCP correspondant en cours d'exécution** (depuis `../01-first-server/`)
2. **Les dépendances nécessaires installées** pour le langage choisi
3. **Une connectivité réseau appropriée** (pour les transports basés sur HTTP)

## Différences Clés Entre les Implémentations

| Langage    | Transport | Démarrage Serveur | Modèle Async | Bibliothèques Clés       |
|------------|-----------|-------------------|--------------|--------------------------|
| Java       | SSE/HTTP  | Externe           | Synchrone    | WebFlux, MCP SDK         |
| C#         | Stdio     | Automatique       | Async/Await  | .NET MCP SDK             |
| TypeScript | Stdio     | Automatique       | Async/Await  | Node MCP SDK             |
| Python     | Stdio     | Automatique       | AsyncIO      | Python MCP SDK           |
| Rust       | Stdio     | Automatique       | Async/Await  | Rust MCP SDK, Tokio      |

## Prochaines Étapes

Après avoir exploré ces exemples de clients :

1. **Modifiez les clients** pour ajouter de nouvelles fonctionnalités ou opérations
2. **Créez votre propre serveur** et testez-le avec ces clients
3. **Expérimentez avec différents transports** (SSE vs. Stdio)
4. **Construisez une application plus complexe** intégrant les fonctionnalités MCP

## Résolution de Problèmes

### Problèmes Courants

1. **Connexion refusée** : Assurez-vous que le serveur MCP est en cours d'exécution sur le port/chemin attendu
2. **Module introuvable** : Installez le SDK MCP requis pour votre langage
3. **Permission refusée** : Vérifiez les permissions des fichiers pour le transport stdio
4. **Outil introuvable** : Vérifiez que le serveur implémente les outils attendus

### Conseils de Débogage

1. **Activez la journalisation détaillée** dans votre SDK MCP
2. **Consultez les journaux du serveur** pour les messages d'erreur
3. **Vérifiez les noms et signatures des outils** entre le client et le serveur
4. **Testez avec MCP Inspector** pour valider la fonctionnalité du serveur

## Documentation Connexe

- [Tutoriel Principal du Client](./README.md)
- [Exemples de Serveurs MCP](../../../../03-GettingStarted/01-first-server)
- [MCP avec Intégration LLM](../../../../03-GettingStarted/03-llm-client)
- [Documentation Officielle MCP](https://modelcontextprotocol.io/)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.