# Générateur de Plan d'Étude avec Chainlit & Microsoft Learn Docs MCP

## Prérequis

- Python 3.8 ou version ultérieure
- pip (gestionnaire de paquets Python)
- Accès Internet pour se connecter au serveur Microsoft Learn Docs MCP

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers du projet.
2. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Scénario 1 : Requête Simple vers Docs MCP
Un client en ligne de commande qui se connecte au serveur Docs MCP, envoie une requête et affiche le résultat.

1. Exécutez le script :
   ```bash
   python scenario1.py
   ```
2. Entrez votre question sur la documentation dans l'invite.

### Scénario 2 : Générateur de Plan d'Étude (Application Web Chainlit)
Une interface web (utilisant Chainlit) qui permet aux utilisateurs de générer un plan d'étude personnalisé, semaine par semaine, pour tout sujet technique.

1. Lancez l'application Chainlit :
   ```bash
   chainlit run scenario2.py
   ```
2. Ouvrez l'URL locale fournie dans votre terminal (par exemple, http://localhost:8000) dans votre navigateur.
3. Dans la fenêtre de chat, entrez votre sujet d'étude et le nombre de semaines souhaité (par exemple, "Certification AI-900, 8 semaines").
4. L'application répondra avec un plan d'étude semaine par semaine, incluant des liens vers la documentation pertinente de Microsoft Learn.

**Variables d'Environnement Requises :**

Pour utiliser le Scénario 2 (l'application web Chainlit avec Azure OpenAI), vous devez définir les variables d'environnement suivantes dans un fichier `.env` situé dans le répertoire `python` :

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Renseignez ces valeurs avec les détails de votre ressource Azure OpenAI avant de lancer l'application.

> [!TIP]
> Vous pouvez facilement déployer vos propres modèles en utilisant [Azure AI Foundry](https://ai.azure.com/).

### Scénario 3 : Documentation Intégrée avec le Serveur MCP dans VS Code

Au lieu de basculer entre les onglets du navigateur pour rechercher de la documentation, vous pouvez intégrer Microsoft Learn Docs directement dans votre VS Code en utilisant le serveur MCP. Cela vous permet de :
- Rechercher et lire la documentation directement dans VS Code sans quitter votre environnement de développement.
- Référencer la documentation et insérer des liens directement dans votre README ou vos fichiers de cours.
- Utiliser GitHub Copilot et MCP ensemble pour un workflow de documentation fluide et optimisé par l'IA.

**Exemples d'Utilisation :**
- Ajouter rapidement des liens de référence à un README tout en rédigeant une documentation de cours ou de projet.
- Utiliser Copilot pour générer du code et MCP pour trouver et citer instantanément la documentation pertinente.
- Rester concentré dans votre éditeur et améliorer votre productivité.

> [!IMPORTANT]
> Assurez-vous d'avoir une configuration valide [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) dans votre espace de travail (emplacement : `.vscode/mcp.json`).

## Pourquoi utiliser Chainlit pour le Scénario 2 ?

Chainlit est un framework open-source moderne pour créer des applications web conversationnelles. Il simplifie la création d'interfaces utilisateur basées sur le chat qui se connectent à des services backend comme le serveur Microsoft Learn Docs MCP. Ce projet utilise Chainlit pour offrir un moyen simple et interactif de générer des plans d'étude personnalisés en temps réel. En exploitant Chainlit, vous pouvez rapidement créer et déployer des outils basés sur le chat qui améliorent la productivité et l'apprentissage.

## Ce que fait cette application

Cette application permet aux utilisateurs de créer un plan d'étude personnalisé en entrant simplement un sujet et une durée. L'application analyse votre saisie, interroge le serveur Microsoft Learn Docs MCP pour obtenir du contenu pertinent, et organise les résultats dans un plan structuré semaine par semaine. Les recommandations de chaque semaine sont affichées dans le chat, ce qui facilite le suivi et la progression. L'intégration garantit que vous obtenez toujours les ressources d'apprentissage les plus récentes et pertinentes.

## Exemples de Requêtes

Essayez ces requêtes dans la fenêtre de chat pour voir comment l'application répond :

- `Certification AI-900, 8 semaines`
- `Apprendre Azure Functions, 4 semaines`
- `Azure DevOps, 6 semaines`
- `Ingénierie des données sur Azure, 10 semaines`
- `Fondamentaux de la sécurité Microsoft, 5 semaines`
- `Power Platform, 7 semaines`
- `Services Azure AI, 12 semaines`
- `Architecture cloud, 9 semaines`

Ces exemples montrent la flexibilité de l'application pour différents objectifs d'apprentissage et durées.

## Références

- [Documentation Chainlit](https://docs.chainlit.io/)
- [Documentation MCP](https://github.com/MicrosoftDocs/mcp)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.