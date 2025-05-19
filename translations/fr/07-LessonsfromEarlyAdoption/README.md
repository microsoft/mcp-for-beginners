<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T17:42:26+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "fr"
}
-->
# Leçons des premiers adopteurs

## Aperçu

Cette leçon explore comment les premiers adopteurs ont utilisé le Model Context Protocol (MCP) pour résoudre des défis concrets et stimuler l'innovation dans divers secteurs. À travers des études de cas détaillées et des projets pratiques, vous découvrirez comment le MCP permet une intégration d’IA standardisée, sécurisée et évolutive — connectant les grands modèles de langage, les outils et les données d’entreprise dans un cadre unifié. Vous acquerrez une expérience concrète en concevant et construisant des solutions basées sur MCP, apprendrez des modèles d’implémentation éprouvés, et découvrirez les meilleures pratiques pour déployer MCP en environnement de production. La leçon met également en lumière les tendances émergentes, les orientations futures, ainsi que les ressources open source pour vous aider à rester à la pointe de la technologie MCP et de son écosystème en évolution.

## Objectifs d’apprentissage

- Analyser des implémentations réelles de MCP dans différents secteurs
- Concevoir et développer des applications complètes basées sur MCP
- Explorer les tendances émergentes et les perspectives futures de la technologie MCP
- Appliquer les meilleures pratiques dans des scénarios de développement concrets

## Implémentations réelles de MCP

### Étude de cas 1 : Automatisation du support client en entreprise

Une multinationale a mis en place une solution basée sur MCP pour standardiser les interactions IA dans ses systèmes de support client. Cela leur a permis de :

- Créer une interface unifiée pour plusieurs fournisseurs de LLM
- Maintenir une gestion cohérente des prompts entre les départements
- Mettre en œuvre des contrôles robustes de sécurité et conformité
- Basculer facilement entre différents modèles IA selon les besoins spécifiques

**Implémentation technique :**  
```python
# Python MCP server implementation for customer support
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# Configure logging
logging.basicConfig(level=logging.INFO)

async def main():
    # Create server configuration
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # Initialize MCP server
    server = create_server(config)
    
    # Register knowledge base resources
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # Register prompt templates
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # Register support tools
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # Start server with HTTP transport
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**Résultats :** Réduction de 30 % des coûts des modèles, amélioration de 45 % de la cohérence des réponses, et conformité renforcée à l’échelle mondiale.

### Étude de cas 2 : Assistant diagnostique en santé

Un fournisseur de soins de santé a développé une infrastructure MCP pour intégrer plusieurs modèles médicaux spécialisés tout en garantissant la protection des données sensibles des patients :

- Passage fluide entre modèles médicaux généralistes et spécialistes
- Contrôles stricts de confidentialité et pistes d’audit
- Intégration avec les systèmes existants de dossiers médicaux électroniques (DME)
- Ingénierie cohérente des prompts pour la terminologie médicale

**Implémentation technique :**  
```csharp
// C# MCP host application implementation in healthcare application
using Microsoft.Extensions.DependencyInjection;
using ModelContextProtocol.SDK.Client;
using ModelContextProtocol.SDK.Security;
using ModelContextProtocol.SDK.Resources;

public class DiagnosticAssistant
{
    private readonly MCPHostClient _mcpClient;
    private readonly PatientContext _patientContext;
    
    public DiagnosticAssistant(PatientContext patientContext)
    {
        _patientContext = patientContext;
        
        // Configure MCP client with healthcare-specific settings
        var clientOptions = new ClientOptions
        {
            Name = "Healthcare Diagnostic Assistant",
            Version = "1.0.0",
            Security = new SecurityOptions
            {
                Encryption = EncryptionLevel.Medical,
                AuditEnabled = true
            }
        };
        
        _mcpClient = new MCPHostClientBuilder()
            .WithOptions(clientOptions)
            .WithTransport(new HttpTransport("https://healthcare-mcp.example.org"))
            .WithAuthentication(new HIPAACompliantAuthProvider())
            .Build();
    }
    
    public async Task<DiagnosticSuggestion> GetDiagnosticAssistance(
        string symptoms, string patientHistory)
    {
        // Create request with appropriate resources and tool access
        var resourceRequest = new ResourceRequest
        {
            Name = "patient_records",
            Parameters = new Dictionary<string, object>
            {
                ["patientId"] = _patientContext.PatientId,
                ["requestingProvider"] = _patientContext.ProviderId
            }
        };
        
        // Request diagnostic assistance using appropriate prompt
        var response = await _mcpClient.SendPromptRequestAsync(
            promptName: "diagnostic_assistance",
            parameters: new Dictionary<string, object>
            {
                ["symptoms"] = symptoms,
                patientHistory = patientHistory,
                relevantGuidelines = _patientContext.GetRelevantGuidelines()
            });
            
        return DiagnosticSuggestion.FromMCPResponse(response);
    }
}
```

**Résultats :** Suggestions diagnostiques améliorées pour les médecins, conformité totale avec la HIPAA, et réduction significative des changements de contexte entre systèmes.

### Étude de cas 3 : Analyse des risques dans les services financiers

Une institution financière a utilisé MCP pour standardiser ses processus d’analyse des risques à travers différents départements :

- Création d’une interface unifiée pour les modèles de risque crédit, détection de fraude et risque d’investissement
- Mise en place de contrôles d’accès stricts et versionnage des modèles
- Garantie de l’auditabilité de toutes les recommandations IA
- Maintien d’un formatage cohérent des données entre systèmes divers

**Implémentation technique :**  
```java
// Java MCP server for financial risk assessment
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // Create MCP server with financial compliance features
        MCPServer server = new MCPServerBuilder()
            .withModelProviders(
                new ModelProvider("risk-assessment-primary", new AzureOpenAIProvider()),
                new ModelProvider("risk-assessment-audit", new LocalLlamaProvider())
            )
            .withPromptTemplateDirectory("./compliance/templates")
            .withAccessControls(new SOCCompliantAccessControl())
            .withDataEncryption(EncryptionStandard.FINANCIAL_GRADE)
            .withVersionControl(true)
            .withAuditLogging(new DatabaseAuditLogger())
            .build();
            
        server.addRequestValidator(new FinancialDataValidator());
        server.addResponseFilter(new PII_RedactionFilter());
        
        server.start(9000);
        
        System.out.println("Financial Risk MCP Server running on port 9000");
    }
}
```

**Résultats :** Conformité réglementaire renforcée, cycles de déploiement des modèles 40 % plus rapides, et meilleure cohérence dans l’évaluation des risques.

### Étude de cas 4 : Serveur MCP Microsoft Playwright pour l’automatisation navigateur

Microsoft a développé le [serveur Playwright MCP](https://github.com/microsoft/playwright-mcp) pour permettre une automatisation navigateur sécurisée et standardisée via le Model Context Protocol. Cette solution permet aux agents IA et aux LLM d’interagir avec les navigateurs web de manière contrôlée, traçable et extensible — ouvrant la voie à des cas d’usage comme les tests web automatisés, l’extraction de données et les workflows de bout en bout.

- Expose les capacités d’automatisation navigateur (navigation, remplissage de formulaires, capture d’écran, etc.) en tant qu’outils MCP
- Met en œuvre des contrôles d’accès stricts et un sandboxing pour éviter les actions non autorisées
- Fournit des journaux d’audit détaillés pour toutes les interactions navigateur
- Supporte l’intégration avec Azure OpenAI et d’autres fournisseurs LLM pour l’automatisation pilotée par agents

**Implémentation technique :**  
```typescript
// TypeScript: Registering Playwright browser automation tools in an MCP server
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// Register a tool for navigating to a URL and capturing a screenshot
server.tools.register(
  new ToolDefinition({
    name: 'navigate_and_screenshot',
    description: 'Navigate to a URL and capture a screenshot',
    parameters: {
      url: { type: 'string', description: 'The URL to visit' }
    }
  }),
  async ({ url }) => {
    const browser = await launch();
    const page = await browser.newPage();
    await page.goto(url);
    const screenshot = await page.screenshot();
    await browser.close();
    return { screenshot };
  }
);

// Start the MCP server
server.listen(8080);
```

**Résultats :**  
- Automatisation navigateur sécurisée et programmatique pour agents IA et LLM  
- Réduction des efforts de tests manuels et meilleure couverture des tests web  
- Cadre réutilisable et extensible pour l’intégration d’outils basés sur navigateur en entreprise

**Références :**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### Étude de cas 5 : Azure MCP – Model Context Protocol de niveau entreprise en tant que service

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) est l’implémentation managée de Microsoft du Model Context Protocol de niveau entreprise, conçue pour offrir des capacités serveur MCP évolutives, sécurisées et conformes sous forme de service cloud. Azure MCP permet aux organisations de déployer, gérer et intégrer rapidement des serveurs MCP avec Azure AI, les données et les services de sécurité, réduisant ainsi la charge opérationnelle et accélérant l’adoption de l’IA.

- Hébergement serveur MCP entièrement managé avec montée en charge, supervision et sécurité intégrées
- Intégration native avec Azure OpenAI, Azure AI Search et autres services Azure
- Authentification et autorisation d’entreprise via Microsoft Entra ID
- Support des outils personnalisés, modèles de prompts et connecteurs de ressources
- Conformité aux exigences de sécurité et réglementaires des entreprises

**Implémentation technique :**  
```yaml
# Example: Azure MCP server deployment configuration (YAML)
apiVersion: mcp.microsoft.com/v1
kind: McpServer
metadata:
  name: enterprise-mcp-server
spec:
  modelProviders:
    - name: azure-openai
      type: AzureOpenAI
      endpoint: https://<your-openai-resource>.openai.azure.com/
      apiKeySecret: <your-azure-keyvault-secret>
  tools:
    - name: document_search
      type: AzureAISearch
      endpoint: https://<your-search-resource>.search.windows.net/
      apiKeySecret: <your-azure-keyvault-secret>
  authentication:
    type: EntraID
    tenantId: <your-tenant-id>
  monitoring:
    enabled: true
    logAnalyticsWorkspace: <your-log-analytics-id>
```

**Résultats :**  
- Réduction du délai de mise en valeur des projets IA d’entreprise grâce à une plateforme serveur MCP prête à l’emploi et conforme  
- Intégration simplifiée des LLM, outils et sources de données d’entreprise  
- Sécurité, observabilité et efficacité opérationnelle améliorées pour les charges MCP  

**Références :**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## Étude de cas 6 : NLWeb  
MCP (Model Context Protocol) est un protocole émergent permettant aux chatbots et assistants IA d’interagir avec des outils. Chaque instance NLWeb est aussi un serveur MCP, supportant une méthode principale, ask, utilisée pour poser une question en langage naturel à un site web. La réponse renvoyée exploite schema.org, un vocabulaire largement utilisé pour décrire les données web. En termes simples, MCP est à NLWeb ce que Http est à HTML. NLWeb combine protocoles, formats Schema.org et exemples de code pour aider les sites à créer rapidement ces points d’accès, au bénéfice des humains via des interfaces conversationnelles et des machines via une interaction naturelle agent-à-agent.

NLWeb se compose de deux éléments distincts :  
- Un protocole, très simple au départ, pour interagir en langage naturel avec un site et un format utilisant json et schema.org pour la réponse. Voir la documentation sur l’API REST pour plus de détails.  
- Une implémentation simple de (1) qui exploite le balisage existant, pour les sites pouvant être abstraits en listes d’éléments (produits, recettes, attractions, avis, etc.). Avec un ensemble de widgets d’interface utilisateur, les sites peuvent facilement offrir des interfaces conversationnelles à leur contenu. Voir la documentation sur Life of a chat query pour plus d’informations sur le fonctionnement.

**Références :**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## Projets pratiques

### Projet 1 : Construire un serveur MCP multi-fournisseurs

**Objectif :** Créer un serveur MCP capable de router les requêtes vers plusieurs fournisseurs de modèles IA selon des critères spécifiques.

**Exigences :**  
- Supporter au moins trois fournisseurs de modèles différents (ex. OpenAI, Anthropic, modèles locaux)  
- Implémenter un mécanisme de routage basé sur les métadonnées des requêtes  
- Créer un système de configuration pour gérer les identifiants des fournisseurs  
- Ajouter un cache pour optimiser performances et coûts  
- Construire un tableau de bord simple pour le suivi de l’utilisation

**Étapes d’implémentation :**  
1. Mettre en place l’infrastructure de base du serveur MCP  
2. Implémenter les adaptateurs fournisseurs pour chaque service de modèle IA  
3. Créer la logique de routage basée sur les attributs des requêtes  
4. Ajouter des mécanismes de cache pour les requêtes fréquentes  
5. Développer le tableau de bord de monitoring  
6. Tester avec différents scénarios de requêtes

**Technologies :** Choix entre Python (.NET/Java/Python selon préférence), Redis pour le cache, et un framework web simple pour le tableau de bord.

### Projet 2 : Système d’administration des prompts en entreprise

**Objectif :** Développer un système basé sur MCP pour gérer, versionner et déployer des modèles de prompts à l’échelle d’une organisation.

**Exigences :**  
- Créer un dépôt centralisé pour les modèles de prompts  
- Implémenter le versionnage et des workflows d’approbation  
- Construire des capacités de test des modèles avec des entrées exemples  
- Développer des contrôles d’accès basés sur les rôles  
- Créer une API pour la récupération et le déploiement des modèles

**Étapes d’implémentation :**  
1. Concevoir le schéma de base de données pour le stockage des modèles  
2. Créer l’API principale pour les opérations CRUD sur les modèles  
3. Implémenter le système de versionnage  
4. Construire le workflow d’approbation  
5. Développer le cadre de test  
6. Créer une interface web simple pour la gestion  
7. Intégrer avec un serveur MCP

**Technologies :** Framework backend au choix, base de données SQL ou NoSQL, framework frontend pour l’interface de gestion.

### Projet 3 : Plateforme de génération de contenu basée sur MCP

**Objectif :** Construire une plateforme de génération de contenu qui utilise MCP pour garantir des résultats cohérents sur différents types de contenu.

**Exigences :**  
- Supporter plusieurs formats de contenu (articles de blog, réseaux sociaux, textes marketing)  
- Implémenter une génération basée sur des modèles avec options de personnalisation  
- Créer un système de revue et de feedback sur le contenu  
- Suivre les métriques de performance du contenu  
- Supporter le versionnage et l’itération du contenu

**Étapes d’implémentation :**  
1. Mettre en place l’infrastructure cliente MCP  
2. Créer des modèles pour les différents types de contenu  
3. Construire la chaîne de génération de contenu  
4. Implémenter le système de revue  
5. Développer le système de suivi des métriques  
6. Créer une interface utilisateur pour la gestion des modèles et la génération

**Technologies :** Langage de programmation préféré, framework web, système de base de données.

## Perspectives futures pour la technologie MCP

### Tendances émergentes

1. **MCP multimodal**  
   - Extension de MCP pour standardiser les interactions avec des modèles d’image, audio et vidéo  
   - Développement de capacités de raisonnement intermodal  
   - Formats de prompt standardisés pour différentes modalités

2. **Infrastructure MCP fédérée**  
   - Réseaux MCP distribués pouvant partager des ressources entre organisations  
   - Protocoles standardisés pour le partage sécurisé de modèles  
   - Techniques de calcul préservant la confidentialité

3. **Places de marché MCP**  
   - Écosystèmes pour partager et monétiser modèles MCP et plugins  
   - Processus d’assurance qualité et de certification  
   - Intégration avec les places de marché de modèles

4. **MCP pour edge computing**  
   - Adaptation des standards MCP aux appareils edge à ressources limitées  
   - Protocoles optimisés pour les environnements à faible bande passante  
   - Implémentations MCP spécialisées pour les écosystèmes IoT

5. **Cadres réglementaires**  
   - Développement d’extensions MCP pour la conformité réglementaire  
   - Pistes d’audit standardisées et interfaces d’explicabilité  
   - Intégration avec les cadres émergents de gouvernance de l’IA

### Solutions MCP de Microsoft

Microsoft et Azure ont développé plusieurs dépôts open source pour aider les développeurs à implémenter MCP dans divers scénarios :

#### Organisation Microsoft  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) – Serveur Playwright MCP pour l’automatisation et les tests navigateur  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) – Implémentation serveur MCP OneDrive pour tests locaux et contributions communautaires  
3. [NLWeb](https://github.com/microsoft/NlWeb) – Collection de protocoles ouverts et outils open source associés, visant à établir une couche fondamentale pour le Web IA

#### Organisation Azure-Samples  
1. [mcp](https://github.com/Azure-Samples/mcp) – Liens vers exemples, outils et ressources pour construire et intégrer des serveurs MCP sur Azure avec plusieurs langages  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) – Serveurs MCP de référence démontrant l’authentification selon la spécification actuelle du Model Context Protocol  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) – Page d’accueil pour les implémentations Remote MCP Server dans Azure Functions avec liens vers dépôts spécifiques aux langages  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) – Template de démarrage rapide pour créer et déployer des serveurs MCP distants personnalisés avec Azure Functions en Python  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – Template de démarrage rapide pour créer et déployer des serveurs MCP distants personnalisés avec Azure Functions en .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – Template de démarrage rapide pour créer et déployer des serveurs MCP distants personnalisés avec Azure Functions en TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) – Azure API Management comme passerelle IA vers des serveurs MCP distants en Python  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) – Expériences APIM ❤️ IA incluant les capacités MCP, intégration avec Azure OpenAI et AI Foundry

Ces dépôts offrent diverses implémentations, modèles et ressources pour travailler avec le Model Context Protocol dans plusieurs langages de programmation et services Azure. Ils couvrent un large éventail de cas d’usage, de l’implémentation basique à l’authentification, au déploiement cloud et à l’intégration en entreprise.

#### Répertoire des ressources MCP

Le [répertoire MCP Resources](https://github.com/microsoft/mcp/tree/main/Resources) dans le dépôt officiel Microsoft MCP propose une collection organisée de ressources exemples, modèles de prompts et définitions d’outils pour les serveurs Model Context Protocol. Ce répertoire vise à aider les développeurs à démarrer rapidement avec MCP en offrant des blocs réutilisables et des exemples de bonnes pratiques pour :

- **Modèles de prompts :** Modèles prêts à l’emploi pour tâches et scénarios IA courants, adaptables à vos propres implémentations serveur MCP  
- **Définitions d’outils :** Schémas et métadonnées d’outils types pour standardiser l’intégration et l’appel des outils entre différents serveurs MCP  
- **Exemples de ressources :** Définitions de ressources pour connecter des sources de données, API et services externes dans le cadre MCP  
- **Implémentations de référence :** Exemples pratiques montrant comment structurer et organiser ressources, prompts et outils dans des projets MCP réels

Ces ressources accélèrent le développement, favorisent la standardisation et contribuent à garantir les meilleures pratiques lors de la construction et du déploiement de solutions basées sur MCP.

#### Répertoire des ressources MCP  
- [MCP Resources (exemples de prompts, outils et définitions de ressources)](https://github.com/microsoft/mcp/tree/main/Resources)

### Opportunités de recherche

- Techniques efficaces d’optimisation des prompts dans les frameworks MCP  
- Modèles de sécurité pour déploiements MCP multi-locataires  
- Évaluation des performances entre différentes implémentations MCP  
- Méthodes de vérification formelle des serveurs MCP

## Conclusion

Le Model Context Protocol (MCP) façonne rapidement l’avenir de l’intégration IA standardisée, sécurisée et interopérable dans tous les secteurs. À travers les études de cas et projets pratiques de cette leçon, vous avez vu comment les premiers adopteurs — notamment Microsoft et Azure — exploitent MCP pour relever des défis concrets, accélérer l’adoption de l’IA, et garantir conformité, sécurité et évolutivité. L’approche modulaire de MCP permet aux organisations de connecter grands modèles de langage, outils et données d’entreprise dans un cadre unifié et traçable. Alors que MCP continue d’évoluer, rester engagé avec la communauté, explorer les ressources open source et appliquer les meilleures pratiques seront essentiels pour construire des solutions IA robustes et prêtes pour l’avenir.

## Ressources supplémentaires

- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)  
- [MCP Resources Directory (exemples de prompts, outils et définitions de ressources)](https://github.com/microsoft/mcp/tree/main/Resources)  
- [Communauté et documentation MCP](https://modelcontextprotocol.io/introduction)  
- [Documentation Azure MCP](https://aka.ms/azmcp)  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Files MCP Server (OneDrive)](https://github.com/microsoft/files-mcp-server)  
- [Azure-Samples MCP](https://github.com/Azure-Samples/mcp)  
- [MCP Auth Servers (Azure-Samples)](
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Exercices

1. Analysez une des études de cas et proposez une approche alternative d’implémentation.
2. Choisissez une des idées de projet et rédigez un cahier des charges technique détaillé.
3. Recherchez un secteur non couvert par les études de cas et décrivez comment MCP pourrait répondre à ses défis spécifiques.
4. Explorez une des pistes d’évolution et créez un concept pour une nouvelle extension MCP afin de la soutenir.

Suivant : [Bonnes Pratiques](../08-BestPractices/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.