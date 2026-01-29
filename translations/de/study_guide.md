# Model Context Protocol (MCP) für Anfänger - Lernleitfaden

Dieser Lernleitfaden bietet einen Überblick über die Struktur und Inhalte des Repositorys für das Curriculum "Model Context Protocol (MCP) für Anfänger". Nutzen Sie diesen Leitfaden, um das Repository effizient zu navigieren und die verfügbaren Ressourcen optimal zu nutzen.

## Überblick über das Repository

Das Model Context Protocol (MCP) ist ein standardisiertes Framework für die Interaktion zwischen KI-Modellen und Client-Anwendungen. Ursprünglich von Anthropic entwickelt, wird MCP nun von der breiteren MCP-Community über die offizielle GitHub-Organisation gepflegt. Dieses Repository bietet ein umfassendes Curriculum mit praktischen Codebeispielen in C#, Java, JavaScript, Python und TypeScript, das sich an KI-Entwickler, Systemarchitekten und Softwareingenieure richtet.

## Visuelle Curriculum-Karte

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```

## Struktur des Repositorys

Das Repository ist in elf Hauptabschnitte unterteilt, die jeweils verschiedene Aspekte von MCP behandeln:

1. **Einführung (00-Introduction/)**
   - Überblick über das Model Context Protocol
   - Warum Standardisierung in KI-Pipelines wichtig ist
   - Praktische Anwendungsfälle und Vorteile

2. **Kernkonzepte (01-CoreConcepts/)**
   - Client-Server-Architektur
   - Wichtige Protokollkomponenten
   - Nachrichtenmuster in MCP

3. **Sicherheit (02-Security/)**
   - Sicherheitsbedrohungen in MCP-basierten Systemen
   - Best Practices zur Sicherung von Implementierungen
   - Strategien für Authentifizierung und Autorisierung
   - **Umfassende Sicherheitsdokumentation**:
     - MCP Sicherheits-Best Practices 2025
     - Azure Content Safety Implementierungsleitfaden
     - MCP Sicherheitskontrollen und Techniken
     - MCP Best Practices Schnellreferenz
   - **Wichtige Sicherheitsthemen**:
     - Prompt Injection und Tool Poisoning Angriffe
     - Session Hijacking und Confused Deputy Probleme
     - Token-Passthrough-Schwachstellen
     - Übermäßige Berechtigungen und Zugriffskontrolle
     - Lieferkettensicherheit für KI-Komponenten
     - Integration von Microsoft Prompt Shields

4. **Erste Schritte (03-GettingStarted/)**
   - Einrichtung und Konfiguration der Umgebung
   - Erstellung grundlegender MCP-Server und -Clients
   - Integration in bestehende Anwendungen
   - Enthält Abschnitte zu:
     - Erste Server-Implementierung
     - Client-Entwicklung
     - LLM-Client-Integration
     - VS Code-Integration
     - Server-Sent Events (SSE) Server
     - Erweiterte Servernutzung
     - HTTP-Streaming
     - AI Toolkit-Integration
     - Teststrategien
     - Bereitstellungsrichtlinien

5. **Praktische Implementierung (04-PracticalImplementation/)**
   - Verwendung von SDKs in verschiedenen Programmiersprachen
   - Debugging-, Test- und Validierungstechniken
   - Erstellung wiederverwendbarer Prompt-Vorlagen und Workflows
   - Beispielprojekte mit Implementierungsbeispielen

6. **Fortgeschrittene Themen (05-AdvancedTopics/)**
   - Techniken des Kontext-Engineerings
   - Integration von Foundry-Agenten
   - Multi-modale KI-Workflows
   - OAuth2-Authentifizierungsdemos
   - Echtzeitsuchfunktionen
   - Echtzeit-Streaming
   - Implementierung von Root-Kontexten
   - Routing-Strategien
   - Sampling-Techniken
   - Skalierungsansätze
   - Sicherheitsüberlegungen
   - Entra ID Sicherheitsintegration
   - Web-Suchintegration

7. **Community-Beiträge (06-CommunityContributions/)**
   - Wie man Code und Dokumentation beiträgt
   - Zusammenarbeit über GitHub
   - Community-getriebene Verbesserungen und Feedback
   - Verwendung verschiedener MCP-Clients (Claude Desktop, Cline, VSCode)
   - Arbeit mit beliebten MCP-Servern einschließlich Bildgenerierung

8. **Lektionen aus der frühen Einführung (07-LessonsfromEarlyAdoption/)**
   - Implementierungen und Erfolgsgeschichten aus der Praxis
   - Aufbau und Bereitstellung von MCP-basierten Lösungen
   - Trends und zukünftige Roadmap
   - **Microsoft MCP Servers Guide**: Umfassender Leitfaden zu 10 produktionsreifen Microsoft MCP-Servern, darunter:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (15+ spezialisierte Konnektoren)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **Best Practices (08-BestPractices/)**
   - Leistungsoptimierung und -tuning
   - Gestaltung fehlertoleranter MCP-Systeme
   - Test- und Resilienzstrategien

10. **Fallstudien (09-CaseStudy/)**
    - **Sieben umfassende Fallstudien**, die die Vielseitigkeit von MCP in verschiedenen Szenarien demonstrieren:
    - **Azure AI Travel Agents**: Multi-Agenten-Orchestrierung mit Azure OpenAI und AI Search
    - **Azure DevOps Integration**: Automatisierung von Workflow-Prozessen mit YouTube-Datenaktualisierungen
    - **Echtzeit-Dokumentationsabruf**: Python-Konsolenclient mit HTTP-Streaming
    - **Interaktiver Studienplan-Generator**: Chainlit-Web-App mit konversationeller KI
    - **In-Editor-Dokumentation**: VS Code-Integration mit GitHub Copilot-Workflows
    - **Azure API Management**: Unternehmens-API-Integration mit MCP-Server-Erstellung
    - **GitHub MCP Registry**: Ökosystementwicklung und agentische Integrationsplattform
    - Implementierungsbeispiele, die Unternehmensintegration, Entwicklerproduktivität und Ökosystementwicklung umfassen

11. **Praktischer Workshop (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Umfassender praktischer Workshop, der MCP mit AI Toolkit kombiniert
    - Aufbau intelligenter Anwendungen, die KI-Modelle mit realen Tools verbinden
    - Praktische Module, die Grundlagen, benutzerdefinierte Serverentwicklung und Produktionsbereitstellungsstrategien abdecken
    - **Lab-Struktur**:
      - Lab 1: Grundlagen des MCP-Servers
      - Lab 2: Erweiterte MCP-Serverentwicklung
      - Lab 3: AI Toolkit-Integration
      - Lab 4: Produktionsbereitstellung und Skalierung
    - Lab-basiertes Lernansatz mit Schritt-für-Schritt-Anleitungen

12. **MCP Server Datenbank-Integrations-Labs (11-MCPServerHandsOnLabs/)**
    - **Umfassender 13-Lab-Lernpfad** für den Aufbau produktionsreifer MCP-Server mit PostgreSQL-Integration
    - **Implementierung von Echtzeit-Retail-Analysen** anhand des Zava Retail Use Case
    - **Unternehmensgerechte Muster** einschließlich Row Level Security (RLS), semantischer Suche und Multi-Tenant-Datenzugriff
    - **Komplette Lab-Struktur**:
      - **Labs 00-03: Grundlagen** - Einführung, Architektur, Sicherheit, Einrichtung der Umgebung
      - **Labs 04-06: Aufbau des MCP-Servers** - Datenbankdesign, MCP-Server-Implementierung, Tool-Entwicklung
      - **Labs 07-09: Erweiterte Funktionen** - Semantische Suche, Testen & Debugging, VS Code-Integration
      - **Labs 10-12: Produktion & Best Practices** - Bereitstellung, Überwachung, Optimierung
    - **Abgedeckte Technologien**: FastMCP-Framework, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Lernziele**: Produktionsreife MCP-Server, Datenbank-Integrationsmuster, KI-gestützte Analysen, Unternehmenssicherheit

## Zusätzliche Ressourcen

Das Repository enthält unterstützende Ressourcen:

- **Bilder-Ordner**: Enthält Diagramme und Illustrationen, die im gesamten Curriculum verwendet werden
- **Übersetzungen**: Mehrsprachige Unterstützung mit automatisierten Übersetzungen der Dokumentation
- **Offizielle MCP-Ressourcen**:
  - [MCP Dokumentation](https://modelcontextprotocol.io/)
  - [MCP Spezifikation](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub Repository](https://github.com/modelcontextprotocol)

## So nutzen Sie dieses Repository

1. **Sequenzielles Lernen**: Folgen Sie den Kapiteln in der Reihenfolge (00 bis 11) für ein strukturiertes Lernerlebnis.
2. **Sprachspezifischer Fokus**: Wenn Sie sich für eine bestimmte Programmiersprache interessieren, erkunden Sie die Sample-Verzeichnisse für Implementierungen in Ihrer bevorzugten Sprache.
3. **Praktische Implementierung**: Beginnen Sie mit dem Abschnitt "Erste Schritte", um Ihre Umgebung einzurichten und Ihren ersten MCP-Server und -Client zu erstellen.
4. **Erweiterte Erkundung**: Sobald Sie mit den Grundlagen vertraut sind, tauchen Sie in die fortgeschrittenen Themen ein, um Ihr Wissen zu erweitern.
5. **Community-Engagement**: Treten Sie der MCP-Community über GitHub-Diskussionen und Discord-Kanäle bei, um sich mit Experten und anderen Entwicklern zu vernetzen.

## MCP-Clients und Tools

Das Curriculum behandelt verschiedene MCP-Clients und Tools:

1. **Offizielle Clients**:
   - Visual Studio Code 
   - MCP in Visual Studio Code
   - Claude Desktop
   - Claude in VSCode 
   - Claude API

2. **Community-Clients**:
   - Cline (terminalbasiert)
   - Cursor (Code-Editor)
   - ChatMCP
   - Windsurf

3. **MCP-Verwaltungstools**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Beliebte MCP-Server

Das Repository stellt verschiedene MCP-Server vor, darunter:

1. **Offizielle Microsoft MCP-Server**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (15+ spezialisierte Konnektoren)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **Offizielle Referenz-Server**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **Bildgenerierung**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Entwicklungstools**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **Spezialisierte Server**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Mitwirken

Dieses Repository begrüßt Beiträge aus der Community. Siehe den Abschnitt Community-Beiträge für Anleitungen, wie Sie effektiv zum MCP-Ökosystem beitragen können.

----

*Dieser Lernleitfaden wurde am 6. Oktober 2025 aktualisiert und bietet einen Überblick über das Repository zu diesem Datum. Der Inhalt des Repositorys kann nach diesem Datum aktualisiert werden.*

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.