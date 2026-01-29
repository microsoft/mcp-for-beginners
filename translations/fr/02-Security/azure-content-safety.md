# Sécurité avancée MCP avec Azure Content Safety

Azure Content Safety offre plusieurs outils puissants qui peuvent renforcer la sécurité de vos implémentations MCP :

## Prompt Shields

Les AI Prompt Shields de Microsoft fournissent une protection solide contre les attaques d'injection de prompt, qu'elles soient directes ou indirectes, grâce à :

1. **Détection avancée** : Utilise le machine learning pour identifier les instructions malveillantes intégrées dans le contenu.
2. **Mise en lumière** : Transforme le texte d'entrée pour aider les systèmes d'IA à distinguer les instructions valides des entrées externes.
3. **Délimiteurs et marquage des données** : Marque les frontières entre les données fiables et non fiables.
4. **Intégration Content Safety** : Fonctionne avec Azure AI Content Safety pour détecter les tentatives de jailbreak et les contenus nuisibles.
5. **Mises à jour continues** : Microsoft met régulièrement à jour les mécanismes de protection contre les menaces émergentes.

## Mise en œuvre d’Azure Content Safety avec MCP

Cette approche offre une protection à plusieurs niveaux :
- Analyse des entrées avant traitement
- Validation des sorties avant retour
- Utilisation de listes noires pour les motifs nuisibles connus
- Exploitation des modèles de sécurité de contenu d’Azure, constamment mis à jour

## Ressources Azure Content Safety

Pour en savoir plus sur la mise en œuvre d’Azure Content Safety avec vos serveurs MCP, consultez ces ressources officielles :

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Documentation officielle d’Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Apprenez à prévenir les attaques d’injection de prompt.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Référence API détaillée pour implémenter Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Guide rapide d’implémentation en C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Bibliothèques clientes pour divers langages de programmation.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Conseils spécifiques pour détecter et prévenir les tentatives de jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Bonnes pratiques pour une mise en œuvre efficace de la sécurité du contenu.

Pour une mise en œuvre plus approfondie, consultez notre [guide d’implémentation Azure Content Safety](./azure-content-safety-implementation.md).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.