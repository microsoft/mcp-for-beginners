# AGENTS.md

## Aperçu du projet

**MCP pour les débutants** est un programme éducatif open-source conçu pour apprendre le protocole Model Context Protocol (MCP) - un cadre standardisé pour les interactions entre modèles d'IA et applications clientes. Ce dépôt propose des supports d'apprentissage complets avec des exemples de code pratiques dans plusieurs langages de programmation.

### Technologies clés

- **Langages de programmation** : C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks et SDK** : 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bases de données** : PostgreSQL avec l'extension pgvector
- **Plateformes cloud** : Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Outils de build** : npm, Maven, pip, Cargo
- **Documentation** : Markdown avec traduction automatique en plusieurs langues (48+ langues)

### Architecture

- **11 modules principaux (00-11)** : Parcours d'apprentissage séquentiel des bases aux sujets avancés
- **Laboratoires pratiques** : Exercices pratiques avec code de solution complet dans plusieurs langages
- **Projets exemples** : Implémentations fonctionnelles de serveurs et clients MCP
- **Système de traduction** : Workflow automatisé GitHub Actions pour le support multilingue
- **Ressources graphiques** : Répertoire centralisé d'images avec versions traduites

## Commandes d'installation

Ce dépôt est principalement axé sur la documentation. La plupart des configurations se font dans les projets exemples et laboratoires individuels.

### Configuration du dépôt

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Travailler avec les projets exemples

Les projets exemples se trouvent dans :
- `03-GettingStarted/samples/` - Exemples spécifiques à chaque langage
- `03-GettingStarted/01-first-server/solution/` - Implémentations du premier serveur
- `03-GettingStarted/02-client/solution/` - Implémentations du client
- `11-MCPServerHandsOnLabs/` - Laboratoires complets d'intégration de bases de données

Chaque projet exemple contient ses propres instructions de configuration :

#### Projets TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projets Python
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Projets Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Workflow de développement

### Structure de la documentation

- **Modules 00-11** : Contenu du programme principal dans un ordre séquentiel
- **translations/** : Versions spécifiques à chaque langue (générées automatiquement, ne pas modifier directement)
- **translated_images/** : Versions localisées des images (générées automatiquement)
- **images/** : Images et diagrammes sources

### Modifier la documentation

1. Modifiez uniquement les fichiers markdown en anglais dans les répertoires des modules racine (00-11)
2. Mettez à jour les images dans le répertoire `images/` si nécessaire
3. L'action GitHub co-op-translator générera automatiquement les traductions
4. Les traductions sont régénérées lors des pushs vers la branche principale

### Travailler avec les traductions

- **Traduction automatisée** : Le workflow GitHub Actions gère toutes les traductions
- **Ne modifiez PAS manuellement** les fichiers dans le répertoire `translations/`
- Les métadonnées de traduction sont intégrées dans chaque fichier traduit
- Langues prises en charge : 48+ langues, y compris l'arabe, le chinois, le français, l'allemand, l'hindi, le japonais, le coréen, le portugais, le russe, l'espagnol, et bien d'autres

## Instructions de test

### Validation de la documentation

Étant donné que ce dépôt est principalement axé sur la documentation, les tests se concentrent sur :

1. **Validation des liens** : Vérifiez que tous les liens internes fonctionnent
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validation des exemples de code** : Testez que les exemples de code se compilent/s'exécutent
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdown** : Vérifiez la cohérence du formatage
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Test des projets exemples

Chaque projet exemple spécifique à un langage inclut sa propre approche de test :

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Directives de style de code

### Style de documentation

- Utilisez un langage clair et adapté aux débutants
- Incluez des exemples de code dans plusieurs langages lorsque cela est pertinent
- Suivez les bonnes pratiques Markdown :
  - Utilisez des en-têtes de style ATX (`#` syntaxe)
  - Utilisez des blocs de code délimités avec des identifiants de langage
  - Ajoutez un texte alternatif descriptif pour les images
  - Gardez des longueurs de ligne raisonnables (pas de limite stricte, mais soyez sensé)

### Style des exemples de code

#### TypeScript/JavaScript
- Utilisez les modules ES (`import`/`export`)
- Suivez les conventions strictes de TypeScript
- Incluez des annotations de type
- Ciblez ES2022

#### Python
- Suivez les directives de style PEP 8
- Utilisez des annotations de type lorsque cela est approprié
- Ajoutez des docstrings pour les fonctions et les classes
- Utilisez les fonctionnalités modernes de Python (3.8+)

#### Java
- Suivez les conventions Spring Boot
- Utilisez les fonctionnalités de Java 21
- Respectez la structure standard des projets Maven
- Ajoutez des commentaires Javadoc

### Organisation des fichiers

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Build et déploiement

### Déploiement de la documentation

Le dépôt utilise GitHub Pages ou un service similaire pour l'hébergement de la documentation (si applicable). Les modifications apportées à la branche principale déclenchent :

1. Workflow de traduction (`.github/workflows/co-op-translator.yml`)
2. Traduction automatique de tous les fichiers markdown en anglais
3. Localisation des images si nécessaire

### Aucun processus de build requis

Ce dépôt contient principalement de la documentation Markdown. Aucun processus de compilation ou de build n'est nécessaire pour le contenu du programme principal.

### Déploiement des projets exemples

Les projets exemples individuels peuvent avoir des instructions de déploiement :
- Consultez `03-GettingStarted/09-deployment/` pour les conseils de déploiement du serveur MCP
- Exemples de déploiement Azure Container Apps dans `11-MCPServerHandsOnLabs/`

## Directives de contribution

### Processus de pull request

1. **Fork et clone** : Forkez le dépôt et clonez votre fork localement
2. **Créez une branche** : Utilisez des noms de branche descriptifs (ex. : `fix/typo-module-3`, `add/python-example`)
3. **Apportez des modifications** : Modifiez uniquement les fichiers markdown en anglais (pas les traductions)
4. **Testez localement** : Vérifiez que le markdown s'affiche correctement
5. **Soumettez une PR** : Utilisez des titres et descriptions de PR clairs
6. **CLA** : Signez l'accord de licence de contributeur Microsoft lorsque cela est demandé

### Format des titres de PR

Utilisez des titres clairs et descriptifs :
- `[Module XX] Brève description` pour les modifications spécifiques aux modules
- `[Samples] Description` pour les modifications des exemples de code
- `[Docs] Description` pour les mises à jour générales de la documentation

### Ce que vous pouvez contribuer

- Corrections de bugs dans la documentation ou les exemples de code
- Nouveaux exemples de code dans des langages supplémentaires
- Clarifications et améliorations du contenu existant
- Nouveaux cas d'étude ou exemples pratiques
- Signalement de problèmes pour du contenu peu clair ou incorrect

### Ce qu'il ne faut PAS faire

- Ne modifiez pas directement les fichiers dans le répertoire `translations/`
- Ne modifiez pas le répertoire `translated_images/`
- N'ajoutez pas de fichiers binaires volumineux sans discussion préalable
- Ne modifiez pas les fichiers de workflow de traduction sans coordination

## Notes supplémentaires

### Maintenance du dépôt

- **Changelog** : Tous les changements significatifs sont documentés dans `changelog.md`
- **Guide d'étude** : Utilisez `study_guide.md` pour un aperçu de navigation du programme
- **Modèles de problèmes** : Utilisez les modèles de problèmes GitHub pour les rapports de bugs et les demandes de fonctionnalités
- **Code de conduite** : Tous les contributeurs doivent suivre le code de conduite open source de Microsoft

### Parcours d'apprentissage

Suivez les modules dans l'ordre séquentiel (00-11) pour un apprentissage optimal :
1. **00-02** : Bases (Introduction, Concepts fondamentaux, Sécurité)
2. **03** : Premiers pas avec une implémentation pratique
3. **04-05** : Implémentation pratique et sujets avancés
4. **06-10** : Communauté, bonnes pratiques et applications réelles
5. **11** : Laboratoires complets d'intégration de bases de données (13 laboratoires séquentiels)

### Ressources de support

- **Documentation** : https://modelcontextprotocol.io/
- **Spécification** : https://spec.modelcontextprotocol.io/
- **Communauté** : https://github.com/orgs/modelcontextprotocol/discussions
- **Discord** : Serveur Discord Microsoft Azure AI Foundry
- **Cours associés** : Consultez README.md pour d'autres parcours d'apprentissage Microsoft

### Résolution des problèmes courants

**Q : Ma PR échoue au contrôle de traduction**
R : Assurez-vous d'avoir uniquement modifié les fichiers markdown en anglais dans les répertoires des modules racine, et non les versions traduites.

**Q : Comment ajouter une nouvelle langue ?**
R : Le support linguistique est géré via le workflow co-op-translator. Ouvrez un problème pour discuter de l'ajout de nouvelles langues.

**Q : Les exemples de code ne fonctionnent pas**
R : Assurez-vous d'avoir suivi les instructions de configuration dans le README spécifique à l'exemple. Vérifiez que vous avez installé les bonnes versions des dépendances.

**Q : Les images ne s'affichent pas**
R : Vérifiez que les chemins des images sont relatifs et utilisent des barres obliques. Les images doivent se trouver dans le répertoire `images/` ou `translated_images/` pour les versions localisées.

### Considérations de performance

- Le workflow de traduction peut prendre plusieurs minutes pour se terminer
- Les grandes images doivent être optimisées avant d'être commises
- Gardez les fichiers markdown individuels ciblés et de taille raisonnable
- Utilisez des liens relatifs pour une meilleure portabilité

### Gouvernance du projet

Ce projet suit les pratiques open source de Microsoft :
- Licence MIT pour le code et la documentation
- Code de conduite open source de Microsoft
- CLA requis pour les contributions
- Problèmes de sécurité : Suivez les directives de SECURITY.md
- Support : Consultez SUPPORT.md pour les ressources d'aide

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.