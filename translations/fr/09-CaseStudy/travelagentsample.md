# Étude de cas : Agents de voyage Azure AI – Implémentation de référence

## Vue d’ensemble

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) est une solution de référence complète développée par Microsoft qui montre comment créer une application de planification de voyage multi-agents alimentée par l’IA, en utilisant le Model Context Protocol (MCP), Azure OpenAI et Azure AI Search. Ce projet illustre les meilleures pratiques pour orchestrer plusieurs agents IA, intégrer des données d’entreprise et offrir une plateforme sécurisée et extensible pour des scénarios réels.

## Fonctionnalités clés
- **Orchestration multi-agents :** Utilise MCP pour coordonner des agents spécialisés (par exemple, agents vols, hôtels et itinéraires) qui collaborent pour accomplir des tâches complexes de planification de voyage.
- **Intégration des données d’entreprise :** Se connecte à Azure AI Search et à d’autres sources de données d’entreprise pour fournir des informations à jour et pertinentes pour les recommandations de voyage.
- **Architecture sécurisée et évolutive :** Exploite les services Azure pour l’authentification, l’autorisation et le déploiement scalable, en suivant les meilleures pratiques de sécurité en entreprise.
- **Outils extensibles :** Implémente des outils MCP réutilisables et des modèles de prompts, permettant une adaptation rapide à de nouveaux domaines ou besoins métier.
- **Expérience utilisateur :** Offre une interface conversationnelle permettant aux utilisateurs d’interagir avec les agents de voyage, propulsée par Azure OpenAI et MCP.

## Architecture
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Description du diagramme d’architecture

La solution Azure AI Travel Agents est conçue pour la modularité, l’évolutivité et l’intégration sécurisée de plusieurs agents IA et sources de données d’entreprise. Les principaux composants et le flux de données sont les suivants :

- **Interface utilisateur :** Les utilisateurs interagissent avec le système via une interface conversationnelle (comme un chat web ou un bot Teams), qui envoie les requêtes utilisateur et reçoit les recommandations de voyage.
- **Serveur MCP :** Sert d’orchestrateur central, recevant les entrées utilisateur, gérant le contexte et coordonnant les actions des agents spécialisés (par exemple FlightAgent, HotelAgent, ItineraryAgent) via le Model Context Protocol.
- **Agents IA :** Chaque agent est responsable d’un domaine spécifique (vols, hôtels, itinéraires) et est implémenté comme un outil MCP. Les agents utilisent des modèles de prompts et une logique propre pour traiter les demandes et générer des réponses.
- **Service Azure OpenAI :** Fournit une compréhension et une génération avancées du langage naturel, permettant aux agents d’interpréter l’intention utilisateur et de produire des réponses conversationnelles.
- **Azure AI Search & données d’entreprise :** Les agents interrogent Azure AI Search et d’autres sources de données d’entreprise pour récupérer des informations à jour sur les vols, hôtels et options de voyage.
- **Authentification & sécurité :** S’intègre à Microsoft Entra ID pour une authentification sécurisée et applique des contrôles d’accès au moindre privilège sur toutes les ressources.
- **Déploiement :** Conçu pour un déploiement sur Azure Container Apps, garantissant évolutivité, supervision et efficacité opérationnelle.

Cette architecture permet une orchestration fluide de plusieurs agents IA, une intégration sécurisée des données d’entreprise et une plateforme robuste et extensible pour construire des solutions IA spécifiques à un domaine.

## Explication pas à pas du diagramme d’architecture
Imaginez que vous planifiez un grand voyage et que vous avez une équipe d’assistants experts qui vous aident pour chaque détail. Le système Azure AI Travel Agents fonctionne de manière similaire, en utilisant différentes parties (comme des membres d’une équipe) qui ont chacune un rôle spécifique. Voici comment tout cela s’assemble :

### Interface utilisateur (UI) :
Considérez cela comme la réception de votre agent de voyage. C’est là que vous (l’utilisateur) posez des questions ou faites des demandes, par exemple « Trouve-moi un vol pour Paris ». Cela peut être une fenêtre de chat sur un site web ou une application de messagerie.

### Serveur MCP (Le coordinateur) :
Le serveur MCP est comme le responsable qui écoute votre demande à la réception et décide quel spécialiste doit s’en charger. Il garde la trace de votre conversation et veille à ce que tout se passe bien.

### Agents IA (Assistants spécialistes) :
Chaque agent est un expert dans un domaine spécifique — l’un connaît tout sur les vols, un autre sur les hôtels, un autre sur la planification d’itinéraires. Quand vous demandez un voyage, le serveur MCP envoie votre requête au(x) agent(s) approprié(s). Ces agents utilisent leurs connaissances et outils pour trouver les meilleures options pour vous.

### Service Azure OpenAI (Expert linguistique) :
C’est comme avoir un expert en langue qui comprend exactement ce que vous demandez, peu importe la façon dont vous le formulez. Il aide les agents à comprendre vos demandes et à répondre dans un langage naturel et conversationnel.

### Azure AI Search & données d’entreprise (Bibliothèque d’informations) :
Imaginez une immense bibliothèque à jour avec toutes les dernières infos de voyage — horaires de vols, disponibilités d’hôtels, et plus encore. Les agents consultent cette bibliothèque pour obtenir les réponses les plus précises pour vous.

### Authentification & sécurité (Agent de sécurité) :
Tout comme un agent de sécurité vérifie qui peut entrer dans certaines zones, cette partie s’assure que seules les personnes et agents autorisés peuvent accéder aux informations sensibles. Elle protège vos données et votre vie privée.

### Déploiement sur Azure Container Apps (Le bâtiment) :
Tous ces assistants et outils travaillent ensemble à l’intérieur d’un bâtiment sécurisé et évolutif (le cloud). Cela signifie que le système peut gérer de nombreux utilisateurs simultanément et est toujours disponible quand vous en avez besoin.

## Comment tout cela fonctionne ensemble :

Vous commencez par poser une question à la réception (UI).  
Le responsable (Serveur MCP) détermine quel spécialiste (agent) doit vous aider.  
Le spécialiste utilise l’expert linguistique (OpenAI) pour comprendre votre demande et la bibliothèque (AI Search) pour trouver la meilleure réponse.  
L’agent de sécurité (Authentification) s’assure que tout est sécurisé.  
Tout cela se passe dans un bâtiment fiable et évolutif (Azure Container Apps), pour que votre expérience soit fluide et sécurisée.  
Cette collaboration permet au système de vous aider rapidement et en toute sécurité à planifier votre voyage, comme une équipe d’agents de voyage experts travaillant ensemble dans un bureau moderne !

## Implémentation technique
- **Serveur MCP :** Héberge la logique centrale d’orchestration, expose les outils des agents et gère le contexte pour les workflows de planification de voyage en plusieurs étapes.
- **Agents :** Chaque agent (par exemple FlightAgent, HotelAgent) est implémenté comme un outil MCP avec ses propres modèles de prompts et sa logique.
- **Intégration Azure :** Utilise Azure OpenAI pour la compréhension du langage naturel et Azure AI Search pour la récupération des données.
- **Sécurité :** S’intègre à Microsoft Entra ID pour l’authentification et applique des contrôles d’accès au moindre privilège sur toutes les ressources.
- **Déploiement :** Supporte le déploiement sur Azure Container Apps pour l’évolutivité et l’efficacité opérationnelle.

## Résultats et impact
- Montre comment MCP peut être utilisé pour orchestrer plusieurs agents IA dans un scénario réel et de qualité production.
- Accélère le développement de solutions en fournissant des modèles réutilisables pour la coordination des agents, l’intégration des données et le déploiement sécurisé.
- Sert de modèle pour construire des applications spécifiques à un domaine, alimentées par l’IA, en utilisant MCP et les services Azure.

## Références
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)  
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)  
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)  
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.