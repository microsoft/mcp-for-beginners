# AGENTS.md

## Aperçu du Projet

**MCP pour Débutants** est un programme éducatif open-source pour apprendre le Model Context Protocol (MCP) - un cadre standardisé pour les interactions entre les modèles d'IA et les applications clientes. Ce dépôt fournit des matériaux d'apprentissage complets avec des exemples pratiques de code dans plusieurs langages de programmation.

### Technologies Clés

- **Langages de Programmation** : C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks et SDK** : 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bases de Données** : PostgreSQL avec l'extension pgvector
- **Plateformes Cloud** : Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Outils de Build** : npm, Maven, pip, Cargo
- **Documentation** : Markdown avec traduction automatisée multilingue (plus de 48 langues)

### Architecture

- **11 Modules principaux (00-11)** : Parcours d'apprentissage séquentiel des bases aux sujets avancés
- **Ateliers pratiques** : Exercices pratiques avec code solution complet dans plusieurs langages
- **Projets d'exemple** : Implémentations fonctionnelles de serveurs et clients MCP
- **Système de traduction** : Workflow GitHub Actions automatisé pour support multilingue
- **Ressources d'images** : Dossier centralisé d'images avec versions traduites

## Commandes d'Installation

Ceci est un dépôt axé sur la documentation. La majeure partie de la configuration se fait au sein des projets d'exemple et ateliers.

### Configuration du Dépôt

```bash
# Clonez le dépôt
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Travailler avec les Projets d'Exemple

Les projets d'exemple sont situés dans :
- `03-GettingStarted/samples/` - Exemples spécifiques aux langages
- `03-GettingStarted/01-first-server/solution/` - Premières implémentations serveur
- `03-GettingStarted/02-client/solution/` - Implémentations client
- `11-MCPServerHandsOnLabs/` - Ateliers complets d'intégration base de données

Chaque projet exemple contient ses propres instructions d'installation :

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
# ou
pip install -e .
python main.py
```

#### Projets Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Flux de Développement

### Préparation MCP 7-28

#### Liste de vérification pour la préparation du dépôt

- [x] **Clarté pour les nouveaux contributeurs** : Ce fichier définit l'objectif du dépôt,
  la structure, les règles de contribution et les chemins d'installation des exemples.
- [x] **Commandes build/test/lint avec options exactes** :
  - Lint de la documentation du dépôt :
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit du modèle des liens dans la documentation du dépôt :
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validation des exemples TypeScript :
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validation des exemples Python :
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validation des exemples Java :
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Un workflow réaliste pouvant devenir un outil MCP** :
  `validate_curriculum_change`
- [x] **Entrées/sorties explicites** (voir spécification ci-dessous).
- [x] **Permissions et modes d'échec documentés** (voir spécification ci-dessous).
- [x] **Testabilité CI explicite** (commandes déterministes, codes de sortie explicites,
  et sorties lisibles par machine).

#### Workflow candidat pour outil MCP : `validate_curriculum_change`

##### Objectif

Valider les modifications de la documentation du curriculum et l'état de santé
du code exemple représentatif avant fusion.

##### Entrées

- `changed_paths: string[]` (requis) - chemins relatifs modifiés dans la PR.
- `run_docs_lint: boolean` (par défaut `true`)
- `run_links_audit: boolean` (par défaut `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (par défaut tous `false`)

##### Sorties

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permissions

- Lire les fichiers de l'espace de travail et écrire uniquement les artefacts générés par l'outil (ex. rapports de lint,
  journaux de test) ; pas d'écriture dans `translations/` ou
  `translated_images/`.
- Exécuter des commandes shell locales.
- Accès réseau optionnel uniquement pour la restauration de paquets (`npm ci`,
  `python -m pip install`, résolution des dépendances `mvn`).
- Pas de permission pour pousser, fusionner ou modifier `translations/` ou
  `translated_images/`.

##### Modes d'échec

- `E_NO_INPUT_PATHS` : `changed_paths` est vide.
- `E_INVALID_PATH` : chemin d'entrée sort de la racine du dépôt.
- `E_LINT_FAILED` : lint markdown retourne un code non nul.
- `E_LINK_AUDIT_FAILED` : commande d'audit des liens retourne un code non nul.
- `E_SAMPLE_TEST_FAILED` : test/build d'exemple retourne un code non nul.
- `E_TIMEOUT` : commande a dépassé le délai configuré.

##### Contrat CI recommandé

Pour automatiser la validation, configurez un job CI qui :

- Se déclenche sur les pull requests touchant `*.md`, le code d'exemple, ou ce fichier.
- Exécute les commandes exactes listées ci-dessus.
- Persiste les journaux comme artefacts.
- Échoue le job dès qu'un code de sortie non nul est retourné.

#### Si vous déployez un serveur MCP à partir de ce dépôt

- [ ] Lisez le changelog provisoire pour MCP 7-28 :
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Testez votre serveur avec les bêta SDK :
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Supprimez les hypothèses de session et de poignée de main ; traitez chaque requête comme
  autonome :
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Envoyez les en-têtes `Mcp-Method` et `Mcp-Name` pour les requêtes HTTP brutes :
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Auditez les codes d'erreur codés en dur (`missing resource` déplacé de `-32002` à `-32602`).

- [ ] Marquer et planifier la migration des racines, échantillonnage et
  journalisation dépréciés :
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrer de l'API expérimentale `2025-11-25` des Tâches :
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Revoir l'autorisation pour le renforcement OAuth et OpenID Connect :
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Structure de la documentation

- **Modules 00-11** : Contenu principal du cursus dans l'ordre séquentiel
- **translations/** : Versions spécifiques à chaque langue (auto-générées, ne pas éditer directement)
- **translated_images/** : Versions localisées des images (auto-générées)
- **images/** : Images et diagrammes sources

### Modification de la documentation

1. Modifier uniquement les fichiers markdown en anglais dans les répertoires racines des modules (00-11)
2. Mettre à jour les images dans le répertoire `images/` si nécessaire
3. L'action GitHub co-op-translator génère automatiquement les traductions
4. Les traductions sont régénérées lors d'un push sur la branche principale

### Travailler avec les traductions

- **Traduction automatisée** : Le workflow GitHub Actions gère toutes les traductions
- **Ne pas éditer manuellement** les fichiers dans le répertoire `translations/`
- Les métadonnées de traduction sont intégrées dans chaque fichier traduit
- Langues supportées : plus de 48 langues dont arabe, chinois, français, allemand, hindi, japonais, coréen, portugais, russe, espagnol, et bien d'autres

## Instructions de test

### Validation de la documentation

Comme il s'agit principalement d'un dépôt de documentation, les tests portent sur :

1. **Audit des liens** : Lister les liens Markdown pour revue

   ```bash
   # Liste des liens Markdown (audit de modèle)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validation des exemples de code** : Tester que les exemples compilent/s'exécutent

   ```bash
   # Naviguer vers un échantillon spécifique et exécuter ses tests
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown** : Vérifier la cohérence du formatage

   ```bash
   # Utilisez markdownlint si nécessaire
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Test des projets d'exemple

Chaque exemple spécifique à une langue inclut sa propre approche de test :

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

- Utiliser un langage clair et accessible aux débutants
- Inclure des exemples de code en plusieurs langues lorsque c’est approprié
- Suivre les bonnes pratiques Markdown :
  - Utiliser des en-têtes style ATX (syntaxe `#`)
  - Utiliser des blocs de code délimités avec identificateurs de langue
  - Inclure un texte alternatif descriptif pour les images
  - Garder des longueurs de lignes raisonnables (pas de limite stricte, mais faire preuve de bon sens)

### Style des exemples de code

#### TypeScript/JavaScript
- Utiliser les modules ES (`import`/`export`)
- Suivre les conventions du mode strict TypeScript
- Inclure des annotations de type
- Cibler ES2022

#### Python
- Suivre les directives PEP 8
- Utiliser les suggestions de type quand approprié
- Inclure des docstrings pour fonctions et classes
- Utiliser des fonctionnalités modernes de Python (3.8+)

#### Java
- Suivre les conventions Spring Boot
- Utiliser les fonctionnalités Java 21
- Suivre la structure standard des projets Maven
- Inclure des commentaires Javadoc

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

## Compilation et déploiement

### Déploiement de la documentation

Le dépôt utilise GitHub Pages ou similaire pour l'hébergement de documentation (si applicable). Les modifications sur la branche principale déclenchent :

1. Workflow de traduction (`.github/workflows/co-op-translator.yml`)
2. Traduction automatisée de tous les fichiers markdown anglais
3. Localisation des images selon les besoins

### Pas de processus de build requis

Ce dépôt contient principalement de la documentation markdown. Aucune compilation ou étape de build n’est nécessaire pour le contenu principal du cursus.

### Déploiement des projets d’exemple

Les projets exemples individuels peuvent disposer d’instructions de déploiement :
- Voir `03-GettingStarted/09-deployment/` pour les instructions de déploiement du serveur MCP
- Exemples de déploiement Azure Container Apps dans `11-MCPServerHandsOnLabs/`

## Directives de contribution

### Processus de Pull Request

1. **Forker et cloner** : Faire un fork du dépôt et cloner votre fork localement
2. **Créer une branche** : Utiliser des noms de branche descriptifs (ex. `fix/typo-module-3`, `add/python-example`)
3. **Faire les modifications** : Modifier uniquement les fichiers markdown en anglais (pas les traductions)
4. **Tester localement** : Vérifier que le markdown s’affiche correctement
5. **Soumettre la PR** : Utiliser des titres et descriptions de PR clairs
6. **CLA** : Signer le Microsoft Contributor License Agreement lorsqu’invité

### Format du titre de PR

Utiliser des titres clairs et descriptifs :
- `[Module XX] Brève description` pour les modifications spécifiques aux modules
- `[Samples] Description` pour les changements dans les exemples de code
- `[Docs] Description` pour les mises à jour générales de la documentation

### Que contribuer

- Corrections de bugs dans la documentation ou les exemples de code
- Nouveaux exemples de code dans d’autres langues
- Clarifications et améliorations du contenu existant
- Nouvelles études de cas ou exemples pratiques
- Rapports de problèmes pour contenus peu clairs ou incorrects

### Ce qu’il NE FAUT PAS faire

- Ne pas éditer directement les fichiers dans `translations/`
- Ne pas éditer le répertoire `translated_images/`
- Ne pas ajouter de gros fichiers binaires sans discussion préalable
- Ne pas modifier les fichiers du workflow de traduction sans coordination

## Notes supplémentaires

### Maintenance du dépôt

- **Journal des modifications** : Tous les changements importants sont documentés dans `changelog.md`
- **Guide d’étude** : Utiliser `study_guide.md` pour la navigation dans le cursus
- **Modèles de problèmes** : Utiliser les modèles GitHub pour rapports de bugs et demandes de fonctionnalités
- **Code de conduite** : Tous les contributeurs doivent respecter le Code de conduite open source de Microsoft

### Parcours d’apprentissage

Suivre les modules dans l’ordre séquentiel (00-11) pour un apprentissage optimal :
1. **00-02** : Fondamentaux (Introduction, Concepts clés, Sécurité)
2. **03** : Premiers pas avec mise en œuvre pratique
3. **04-05** : Mise en œuvre pratique et sujets avancés
4. **06-10** : Communauté, bonnes pratiques et applications réelles
5. **11** : Ateliers d’intégration complète de bases de données (13 ateliers consécutifs)

### Ressources de support

- **Documentation** : https://modelcontextprotocol.io/
- **Spécification** : https://spec.modelcontextprotocol.io/
- **Communauté** : https://github.com/orgs/modelcontextprotocol/discussions
- **Discord** : serveur Microsoft Foundry Discord
- **Cours associés** : Voir README.md pour d’autres parcours d’apprentissage Microsoft

### Dépannage courant

**Q : Ma PR échoue la vérification de traduction**
R : Assurez-vous d'avoir modifié uniquement les fichiers markdown anglais des modules racines, pas les versions traduites.

**Q : Comment ajouter une nouvelle langue ?**
R : Le support linguistique est géré via le workflow co-op-translator. Ouvrez un ticket pour discuter de l'ajout de nouvelles langues.

**Q : Les exemples de code ne fonctionnent pas**

R : Assurez-vous d'avoir suivi les instructions d'installation dans le README de l'exemple spécifique. Vérifiez que vous avez les bonnes versions des dépendances installées.

**Q : Les images ne s'affichent pas**
R : Vérifiez que les chemins des images sont relatifs et utilisent des barres obliques. Les images doivent se trouver dans le répertoire `images/` ou `translated_images/` pour les versions localisées.

### Considérations sur la performance

- Le flux de traduction peut prendre plusieurs minutes à se compléter
- Les images volumineuses doivent être optimisées avant validation
- Gardez les fichiers markdown individuels ciblés et de taille raisonnable
- Utilisez des liens relatifs pour une meilleure portabilité

### Gouvernance du projet

Ce projet suit les pratiques open source de Microsoft :
- Licence MIT pour le code et la documentation
- Code de conduite Microsoft Open Source
- CLA requis pour les contributions
- Problèmes de sécurité : Suivez les directives de SECURITY.md
- Support : Consultez SUPPORT.md pour les ressources d'aide

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->