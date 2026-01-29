# Mise en œuvre d’Azure Content Safety avec MCP

Pour renforcer la sécurité de MCP contre les injections de prompt, l’empoisonnement d’outils et d’autres vulnérabilités spécifiques à l’IA, il est fortement recommandé d’intégrer Azure Content Safety.

## Intégration avec le serveur MCP

Pour intégrer Azure Content Safety à votre serveur MCP, ajoutez le filtre de sécurité de contenu en tant que middleware dans votre pipeline de traitement des requêtes :

1. Initialisez le filtre au démarrage du serveur  
2. Validez toutes les requêtes d’outils entrantes avant traitement  
3. Vérifiez toutes les réponses sortantes avant de les renvoyer aux clients  
4. Enregistrez et alertez en cas de violations de sécurité  
5. Mettez en place une gestion d’erreurs appropriée pour les contrôles de sécurité de contenu échoués  

Cela offre une défense solide contre :  
- Les attaques par injection de prompt  
- Les tentatives d’empoisonnement d’outils  
- L’exfiltration de données via des entrées malveillantes  
- La génération de contenu nuisible  

## Bonnes pratiques pour l’intégration d’Azure Content Safety

1. **Listes de blocage personnalisées** : Créez des listes de blocage spécifiques aux schémas d’injection MCP  
2. **Ajustement de la gravité** : Adaptez les seuils de gravité selon votre cas d’usage et votre tolérance au risque  
3. **Couverture complète** : Appliquez les contrôles de sécurité de contenu à toutes les entrées et sorties  
4. **Optimisation des performances** : Envisagez la mise en cache pour les contrôles de sécurité de contenu répétés  
5. **Mécanismes de secours** : Définissez des comportements de repli clairs lorsque les services de sécurité de contenu ne sont pas disponibles  
6. **Retour utilisateur** : Fournissez un retour clair aux utilisateurs lorsque du contenu est bloqué pour des raisons de sécurité  
7. **Amélioration continue** : Mettez régulièrement à jour les listes de blocage et les schémas en fonction des menaces émergentes

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.