# Änderungsprotokoll: MCP für Anfänger Curriculum

Dieses Dokument dient als Aufzeichnung aller bedeutenden Änderungen am Model Context Protocol (MCP) für Anfänger Curriculum. Änderungen werden in umgekehrter chronologischer Reihenfolge dokumentiert (neueste Änderungen zuerst).

## 18. Dezember 2025

### Sicherheitsdokumentation Update - MCP Spezifikation 2025-11-25

#### MCP Sicherheits-Best-Practices (02-Security/mcp-best-practices.md) - Spezifikationsversions-Update
- **Protokollversions-Update**: Aktualisiert auf die neueste MCP Spezifikation 2025-11-25 (veröffentlicht am 25. November 2025)
  - Alle Versionsverweise der Spezifikation von 2025-06-18 auf 2025-11-25 aktualisiert
  - Dokumentdatum-Verweise von 18. August 2025 auf 18. Dezember 2025 aktualisiert
  - Überprüft, dass alle Spezifikations-URLs auf die aktuelle Dokumentation verweisen
- **Inhaltsvalidierung**: Umfassende Validierung der Sicherheits-Best-Practices gegen aktuelle Standards
  - **Microsoft Sicherheitslösungen**: Überprüfung der aktuellen Terminologie und Links für Prompt Shields (früher "Jailbreak-Risikoerkennung"), Azure Content Safety, Microsoft Entra ID und Azure Key Vault
  - **OAuth 2.1 Sicherheit**: Bestätigung der Übereinstimmung mit den neuesten OAuth Sicherheits-Best-Practices
  - **OWASP Standards**: Validierung, dass die OWASP Top 10 für LLMs Referenzen aktuell sind
  - **Azure Dienste**: Überprüfung aller Microsoft Azure Dokumentationslinks und Best Practices
- **Standardausrichtung**: Alle referenzierten Sicherheitsstandards als aktuell bestätigt
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Sicherheits-Best-Practices
  - Azure Sicherheits- und Compliance-Frameworks
- **Implementierungsressourcen**: Validierung aller Links und Ressourcen zu Implementierungsleitfäden
  - Azure API Management Authentifizierungsmuster
  - Microsoft Entra ID Integrationsanleitungen
  - Azure Key Vault Geheimnisverwaltung
  - DevSecOps Pipelines und Überwachungslösungen

### Dokumentationsqualitätssicherung
- **Spezifikationskonformität**: Sicherstellung, dass alle verpflichtenden MCP Sicherheitsanforderungen (MUSS/MUSS NICHT) mit der neuesten Spezifikation übereinstimmen
- **Ressourcenaktualität**: Überprüfung aller externen Links zu Microsoft Dokumentation, Sicherheitsstandards und Implementierungsleitfäden
- **Best-Practices-Abdeckung**: Bestätigung der umfassenden Abdeckung von Authentifizierung, Autorisierung, KI-spezifischen Bedrohungen, Lieferkettensicherheit und Unternehmensmustern

## 6. Oktober 2025

### Erweiterung des Abschnitts „Erste Schritte“ – Erweiterte Servernutzung & Einfache Authentifizierung

#### Erweiterte Servernutzung (03-GettingStarted/10-advanced)
- **Neues Kapitel hinzugefügt**: Einführung eines umfassenden Leitfadens zur erweiterten MCP-Servernutzung, der sowohl reguläre als auch Low-Level-Serverarchitekturen abdeckt.
  - **Regulärer vs. Low-Level-Server**: Detaillierter Vergleich und Codebeispiele in Python und TypeScript für beide Ansätze.
  - **Handler-basierte Gestaltung**: Erklärung der handlerbasierten Verwaltung von Tools/Ressourcen/Prompts für skalierbare, flexible Serverimplementierungen.
  - **Praktische Muster**: Praxisnahe Szenarien, in denen Low-Level-Servermuster für erweiterte Funktionen und Architektur vorteilhaft sind.

#### Einfache Authentifizierung (03-GettingStarted/11-simple-auth)
- **Neues Kapitel hinzugefügt**: Schritt-für-Schritt-Anleitung zur Implementierung einfacher Authentifizierung in MCP-Servern.
  - **Auth-Konzepte**: Klare Erklärung von Authentifizierung vs. Autorisierung und Umgang mit Zugangsdaten.
  - **Grundlegende Auth-Implementierung**: Middleware-basierte Authentifizierungsmuster in Python (Starlette) und TypeScript (Express) mit Codebeispielen.
  - **Fortschritt zu erweiterter Sicherheit**: Anleitung zum Einstieg mit einfacher Auth und Weiterentwicklung zu OAuth 2.1 und RBAC, mit Verweisen auf erweiterte Sicherheitsmodule.

Diese Ergänzungen bieten praktische, praxisnahe Anleitungen zum Aufbau robusterer, sichererer und flexiblerer MCP-Serverimplementierungen und verbinden grundlegende Konzepte mit fortgeschrittenen Produktionsmustern.

## 29. September 2025

### MCP Server Datenbank-Integrations-Labs – Umfassender praktischer Lernpfad

#### 11-MCPServerHandsOnLabs – Neues vollständiges Curriculum zur Datenbankintegration
- **Vollständiger 13-Lab Lernpfad**: Hinzugefügt wurde ein umfassendes praktisches Curriculum zum Aufbau produktionsreifer MCP-Server mit PostgreSQL-Datenbankintegration
  - **Praxisnahe Implementierung**: Zava Retail Analytics Anwendungsfall mit Unternehmensmustern
  - **Strukturierter Lernfortschritt**:
    - **Labs 00-03: Grundlagen** – Einführung, Kernarchitektur, Sicherheit & Multi-Tenancy, Umgebungseinrichtung
    - **Labs 04-06: Aufbau des MCP Servers** – Datenbankdesign & Schema, MCP Server Implementierung, Tool-Entwicklung  
    - **Labs 07-09: Erweiterte Funktionen** – Semantische Suche Integration, Testen & Debugging, VS Code Integration
    - **Labs 10-12: Produktion & Best Practices** – Deployment-Strategien, Monitoring & Observability, Best Practices & Optimierung
  - **Enterprise-Technologien**: FastMCP Framework, PostgreSQL mit pgvector, Azure OpenAI Embeddings, Azure Container Apps, Application Insights
  - **Erweiterte Funktionen**: Row Level Security (RLS), semantische Suche, Multi-Tenant-Datenzugriff, Vektor-Embeddings, Echtzeit-Monitoring

#### Terminologiestandardisierung – Modul-zu-Lab-Konvertierung
- **Umfassendes Dokumentationsupdate**: Systematische Aktualisierung aller README-Dateien in 11-MCPServerHandsOnLabs zur Verwendung des Begriffs „Lab“ anstelle von „Modul“
  - **Abschnittsüberschriften**: „Was dieses Modul abdeckt“ wurde in allen 13 Labs zu „Was dieses Lab abdeckt“ geändert
  - **Inhaltsbeschreibung**: „Dieses Modul bietet...“ wurde durchgehend zu „Dieses Lab bietet...“ geändert
  - **Lernziele**: „Am Ende dieses Moduls...“ wurde zu „Am Ende dieses Labs...“ aktualisiert
  - **Navigationslinks**: Alle „Modul XX:“ Verweise wurden in „Lab XX:“ umgewandelt in Querverweisen und Navigation
  - **Abschlussverfolgung**: „Nach Abschluss dieses Moduls...“ wurde zu „Nach Abschluss dieses Labs...“ geändert
  - **Technische Referenzen erhalten**: Python-Modulreferenzen in Konfigurationsdateien (z. B. `"module": "mcp_server.main"`) wurden beibehalten

#### Studienleitfaden-Erweiterung (study_guide.md)
- **Visuelle Curriculum-Karte**: Neuer Abschnitt „11. Database Integration Labs“ mit umfassender Visualisierung der Lab-Struktur hinzugefügt
- **Repository-Struktur**: Aktualisierung von zehn auf elf Hauptabschnitte mit detaillierter Beschreibung von 11-MCPServerHandsOnLabs
- **Lernpfad-Anleitung**: Verbesserte Navigationsanweisungen für die Abschnitte 00-11
- **Technologieabdeckung**: Hinzugefügt FastMCP, PostgreSQL, Azure-Dienste Integrationsdetails
- **Lernergebnisse**: Betonung der Entwicklung produktionsreifer Server, Datenbankintegrationsmuster und Unternehmenssicherheit

#### Haupt-README-Strukturverbesserung
- **Lab-basierte Terminologie**: Haupt-README.md in 11-MCPServerHandsOnLabs auf konsistente Verwendung der „Lab“-Struktur aktualisiert
- **Lernpfad-Organisation**: Klarer Fortschritt von Grundlagen über erweiterte Implementierung bis hin zum Produktions-Deployment
- **Praxisorientierung**: Fokus auf praktisches, hands-on Lernen mit Unternehmensmustern und Technologien

### Verbesserungen der Dokumentationsqualität & Konsistenz
- **Betonung praktischen Lernens**: Verstärkung des praktischen, lab-basierten Ansatzes in der gesamten Dokumentation
- **Enterprise-Muster-Fokus**: Hervorhebung produktionsreifer Implementierungen und Unternehmenssicherheitsaspekte
- **Technologieintegration**: Umfassende Abdeckung moderner Azure-Dienste und KI-Integrationsmuster
- **Lernfortschritt**: Klarer, strukturierter Pfad von Grundkonzepten bis zum Produktions-Deployment

## 26. September 2025

### Case Studies Erweiterung – GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) – Fokus auf Ökosystementwicklung
- **README.md**: Umfangreiche Erweiterung mit umfassender GitHub MCP Registry Case Study
  - **GitHub MCP Registry Case Study**: Neue umfassende Fallstudie zur Einführung der GitHub MCP Registry im September 2025
    - **Problemanalyse**: Detaillierte Untersuchung fragmentierter MCP-Server-Discovery- und Deployment-Herausforderungen
    - **Lösungsarchitektur**: GitHubs zentraler Registry-Ansatz mit One-Click VS Code Installation
    - **Geschäftlicher Einfluss**: Messbare Verbesserungen bei Entwickler-Onboarding und Produktivität
    - **Strategischer Wert**: Fokus auf modulare Agentenbereitstellung und Tool-übergreifende Interoperabilität
    - **Ökosystementwicklung**: Positionierung als grundlegende Plattform für agentische Integration
  - **Verbesserte Case Study Struktur**: Alle sieben Fallstudien mit konsistenter Formatierung und umfassenden Beschreibungen aktualisiert
    - Azure AI Travel Agents: Schwerpunkt Multi-Agenten-Orchestrierung
    - Azure DevOps Integration: Fokus Workflow-Automatisierung
    - Echtzeit-Dokumentenabruf: Python-Konsolenclient-Implementierung
    - Interaktiver Studienplan-Generator: Chainlit Konversations-Web-App
    - In-Editor Dokumentation: VS Code und GitHub Copilot Integration
    - Azure API Management: Unternehmens-API-Integrationsmuster
    - GitHub MCP Registry: Ökosystementwicklung und Community-Plattform
  - **Umfassendes Fazit**: Überarbeiteter Abschlussabschnitt mit Hervorhebung der sieben Fallstudien, die mehrere MCP-Implementierungsdimensionen abdecken
    - Unternehmensintegration, Multi-Agenten-Orchestrierung, Entwicklerproduktivität
    - Ökosystementwicklung, Bildungsanwendungen Kategorisierung
    - Vertiefte Einblicke in Architektur-Muster, Implementierungsstrategien und Best Practices
    - Betonung von MCP als ausgereiftes, produktionsreifes Protokoll

#### Studienleitfaden-Updates (study_guide.md)
- **Visuelle Curriculum-Karte**: Aktualisierte Mindmap zur Einbeziehung der GitHub MCP Registry im Abschnitt Case Studies
- **Case Studies Beschreibung**: Erweiterung von generischen Beschreibungen zu detaillierter Aufschlüsselung der sieben umfassenden Fallstudien
- **Repository-Struktur**: Aktualisierung von Abschnitt 10 zur Abbildung der umfassenden Case Study Abdeckung mit spezifischen Implementierungsdetails
- **Changelog-Integration**: Hinzugefügt Eintrag vom 26. September 2025 zur Dokumentation der GitHub MCP Registry Ergänzung und Case Study Erweiterungen
- **Datumsaktualisierungen**: Aktualisierung des Fußzeilen-Zeitstempels auf die neueste Revision (26. September 2025)

### Verbesserungen der Dokumentationsqualität
- **Konsistenzsteigerung**: Standardisierung der Case Study Formatierung und Struktur über alle sieben Beispiele hinweg
- **Umfassende Abdeckung**: Fallstudien umfassen nun Unternehmens-, Entwicklerproduktivitäts- und Ökosystementwicklungsszenarien
- **Strategische Positionierung**: Verstärkter Fokus auf MCP als grundlegende Plattform für agentische Systembereitstellung
- **Ressourcenintegration**: Aktualisierung zusätzlicher Ressourcen um Link zur GitHub MCP Registry

## 15. September 2025

### Erweiterung fortgeschrittener Themen – Benutzerdefinierte Transports & Kontext-Engineering

#### MCP Benutzerdefinierte Transports (05-AdvancedTopics/mcp-transport/) – Neuer fortgeschrittener Implementierungsleitfaden
- **README.md**: Vollständiger Implementierungsleitfaden für benutzerdefinierte MCP-Transportmechanismen
  - **Azure Event Grid Transport**: Umfassende serverlose ereignisgesteuerte Transportimplementierung
    - C#, TypeScript und Python Beispiele mit Azure Functions Integration
    - Ereignisgesteuerte Architektur-Muster für skalierbare MCP-Lösungen
    - Webhook-Empfänger und Push-basierte Nachrichtenverarbeitung
  - **Azure Event Hubs Transport**: Hochdurchsatz-Streaming-Transportimplementierung
    - Echtzeit-Streaming-Fähigkeiten für latenzarme Szenarien
    - Partitionierungsstrategien und Checkpoint-Management
    - Nachrichten-Batching und Leistungsoptimierung
  - **Enterprise-Integrationsmuster**: Produktionsreife Architekturbeispiele
    - Verteilte MCP-Verarbeitung über mehrere Azure Functions
    - Hybride Transportarchitekturen, die mehrere Transporttypen kombinieren
    - Nachrichtenhaltbarkeit, Zuverlässigkeit und Fehlerbehandlungsstrategien
  - **Sicherheit & Überwachung**: Azure Key Vault Integration und Observability-Muster
    - Managed Identity Authentifizierung und Least Privilege Zugriff
    - Application Insights Telemetrie und Leistungsüberwachung
    - Circuit Breaker und Fehlertoleranzmuster
  - **Testframeworks**: Umfassende Teststrategien für benutzerdefinierte Transports
    - Unit-Tests mit Testdoubles und Mocking-Frameworks
    - Integrationstests mit Azure Test Containers
    - Leistungs- und Lasttests Überlegungen

#### Kontext-Engineering (05-AdvancedTopics/mcp-contextengineering/) – Aufkommende KI-Disziplin
- **README.md**: Umfassende Erkundung von Kontext-Engineering als aufstrebendes Fachgebiet
  - **Kernprinzipien**: Vollständiges Kontextteilen, Handlungsentscheidungsbewusstsein und Kontextfensterverwaltung
  - **MCP Protokollausrichtung**: Wie das MCP-Design Herausforderungen des Kontext-Engineerings adressiert
    - Kontextfensterbegrenzungen und progressive Lade-Strategien
    - Relevanzbestimmung und dynamische Kontextabfrage
    - Multimodale Kontextverarbeitung und Sicherheitsaspekte
  - **Implementierungsansätze**: Single-Threaded vs. Multi-Agenten-Architekturen
    - Kontext-Chunking und Priorisierungstechniken
    - Progressives Kontextladen und Komprimierungsstrategien
    - Geschichtete Kontextansätze und Abrufoptimierung
  - **Messrahmen**: Aufkommende Metriken zur Bewertung der Kontextwirksamkeit
    - Eingabeeffizienz, Leistung, Qualität und Nutzererfahrungsaspekte
    - Experimentelle Ansätze zur Kontextoptimierung
    - Fehleranalyse und Verbesserungsmethoden

#### Curriculum-Navigationsupdates (README.md)
- **Erweiterte Modulstruktur**: Aktualisierte Curriculum-Tabelle zur Aufnahme neuer fortgeschrittener Themen
  - Hinzugefügt Context Engineering (5.14) und Custom Transport (5.15)
  - Konsistente Formatierung und Navigationslinks über alle Module
  - Aktualisierte Beschreibungen zur Abbildung des aktuellen Inhaltsumfangs

### Verbesserungen der Verzeichnisstruktur
- **Namensstandardisierung**: Umbenennung von „mcp transport“ zu „mcp-transport“ zur Konsistenz mit anderen Ordnern für fortgeschrittene Themen
- **Inhaltsorganisation**: Alle 05-AdvancedTopics Ordner folgen nun einem konsistenten Namensmuster (mcp-[thema])

### Verbesserungen der Dokumentationsqualität
- **MCP Spezifikationsausrichtung**: Alle neuen Inhalte verweisen auf die aktuelle MCP Spezifikation 2025-06-18
- **Mehrsprachige Beispiele**: Umfassende Codebeispiele in C#, TypeScript und Python
- **Enterprise-Fokus**: Produktionsreife Muster und Azure Cloud Integration durchgängig
- **Visuelle Dokumentation**: Mermaid-Diagramme zur Architektur- und Ablaufvisualisierung

## 18. August 2025

### Umfassendes Dokumentationsupdate – MCP 2025-06-18 Standards

#### MCP Sicherheits-Best-Practices (02-Security/) – Vollständige Modernisierung
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Vollständige Neufassung im Einklang mit MCP Spezifikation 2025-06-18
  - **Verpflichtende Anforderungen**: Hinzugefügte explizite MUSS/MUSS NICHT Anforderungen aus der offiziellen Spezifikation mit klaren visuellen Indikatoren
  - **12 Kern-Sicherheitspraktiken**: Umstrukturiert von einer 15-Punkte-Liste zu umfassenden Sicherheitsdomänen
    - Token-Sicherheit & Authentifizierung mit Integration externer Identitätsanbieter
    - Sitzungsmanagement & Transportsicherheit mit kryptografischen Anforderungen
    - KI-spezifischer Bedrohungsschutz mit Microsoft Prompt Shields Integration
    - Zugriffskontrolle & Berechtigungen mit dem Prinzip der geringsten Privilegien
    - Inhaltsicherheit & Überwachung mit Azure Content Safety Integration
    - Lieferkettensicherheit mit umfassender Komponentenverifizierung
    - OAuth-Sicherheit & Verhinderung von Confused Deputy mit PKCE-Implementierung
    - Vorfallreaktion & Wiederherstellung mit automatisierten Fähigkeiten
    - Compliance & Governance mit regulatorischer Ausrichtung
    - Erweiterte Sicherheitskontrollen mit Zero-Trust-Architektur
    - Integration des Microsoft-Sicherheitsökosystems mit umfassenden Lösungen
    - Kontinuierliche Sicherheitsevolution mit adaptiven Praktiken
  - **Microsoft-Sicherheitslösungen**: Verbesserte Integrationsanleitungen für Prompt Shields, Azure Content Safety, Entra ID und GitHub Advanced Security
  - **Implementierungsressourcen**: Kategorisierte umfassende Ressourcenlinks nach offizieller MCP-Dokumentation, Microsoft-Sicherheitslösungen, Sicherheitsstandards und Implementierungsleitfäden

#### Erweiterte Sicherheitskontrollen (02-Security/) - Unternehmensimplementierung
- **MCP-SECURITY-CONTROLS-2025.md**: Komplettüberarbeitung mit Sicherheitsrahmenwerk auf Unternehmensniveau
  - **9 Umfassende Sicherheitsdomänen**: Erweiterung von Basis-Kontrollen zu detailliertem Unternehmensrahmenwerk
    - Erweiterte Authentifizierung & Autorisierung mit Microsoft Entra ID Integration
    - Token-Sicherheit & Anti-Passthrough-Kontrollen mit umfassender Validierung
    - Sitzungs-Sicherheitskontrollen mit Hijacking-Prävention
    - KI-spezifische Sicherheitskontrollen mit Schutz vor Prompt Injection und Tool-Vergiftung
    - Verhinderung von Confused Deputy Angriffen mit OAuth-Proxy-Sicherheit
    - Tool-Ausführungs-Sicherheit mit Sandboxing und Isolation
    - Lieferkettensicherheitskontrollen mit Abhängigkeitsverifizierung
    - Überwachungs- & Erkennungskontrollen mit SIEM-Integration
    - Vorfallreaktion & Wiederherstellung mit automatisierten Fähigkeiten
  - **Implementierungsbeispiele**: Hinzugefügte detaillierte YAML-Konfigurationsblöcke und Codebeispiele
  - **Microsoft-Lösungsintegration**: Umfassende Abdeckung von Azure-Sicherheitsdiensten, GitHub Advanced Security und Unternehmens-Identitätsmanagement

#### Erweiterte Sicherheitsthemen (05-AdvancedTopics/mcp-security/) - Produktionsreife Implementierung
- **README.md**: Komplettüberarbeitung für Unternehmenssicherheitsimplementierung
  - **Aktuelle Spezifikationsausrichtung**: Aktualisiert auf MCP-Spezifikation 2025-06-18 mit verpflichtenden Sicherheitsanforderungen
  - **Erweiterte Authentifizierung**: Microsoft Entra ID Integration mit umfassenden .NET- und Java Spring Security-Beispielen
  - **KI-Sicherheitsintegration**: Microsoft Prompt Shields und Azure Content Safety Implementierung mit detaillierten Python-Beispielen
  - **Erweiterte Bedrohungsminderung**: Umfassende Implementierungsbeispiele für
    - Verhinderung von Confused Deputy Angriffen mit PKCE und Benutzerzustimmungsvalidierung
    - Verhinderung von Token-Passthrough mit Audience-Validierung und sicherem Token-Management
    - Verhinderung von Sitzungs-Hijacking mit kryptografischer Bindung und Verhaltensanalyse
  - **Unternehmenssicherheitsintegration**: Azure Application Insights Überwachung, Bedrohungserkennungs-Pipelines und Lieferkettensicherheit
  - **Implementierungs-Checkliste**: Klare Unterscheidung zwischen verpflichtenden und empfohlenen Sicherheitskontrollen mit Vorteilen des Microsoft-Sicherheitsökosystems

### Dokumentationsqualität & Standardausrichtung
- **Spezifikationsreferenzen**: Alle Verweise auf aktuelle MCP-Spezifikation 2025-06-18 aktualisiert
- **Microsoft-Sicherheitsökosystem**: Verbesserte Integrationsanleitungen in der gesamten Sicherheitsdokumentation
- **Praktische Implementierung**: Hinzugefügte detaillierte Codebeispiele in .NET, Java und Python mit Unternehmensmustern
- **Ressourcenorganisation**: Umfassende Kategorisierung offizieller Dokumentation, Sicherheitsstandards und Implementierungsleitfäden
- **Visuelle Indikatoren**: Klare Markierung verpflichtender Anforderungen vs. empfohlener Praktiken


#### Kernkonzepte (01-CoreConcepts/) - Komplette Modernisierung
- **Protokollversions-Update**: Aktualisiert auf Verweis der aktuellen MCP-Spezifikation 2025-06-18 mit datumsbasierter Versionierung (JJJJ-MM-TT-Format)
- **Architekturverfeinerung**: Verbesserte Beschreibungen von Hosts, Clients und Servern zur Abbildung aktueller MCP-Architekturpatterns
  - Hosts nun klar definiert als KI-Anwendungen, die mehrere MCP-Client-Verbindungen koordinieren
  - Clients beschrieben als Protokoll-Connectoren mit Eins-zu-eins-Serverbeziehungen
  - Server erweitert mit lokalen vs. entfernten Bereitstellungsszenarien
- **Primitive Umstrukturierung**: Komplette Überarbeitung der Server- und Client-Primitives
  - Server-Primitives: Ressourcen (Datenquellen), Prompts (Vorlagen), Tools (ausführbare Funktionen) mit detaillierten Erklärungen und Beispielen
  - Client-Primitives: Sampling (LLM-Vervollständigungen), Elicitation (Benutzereingabe), Logging (Debugging/Überwachung)
  - Aktualisiert mit aktuellen Discovery- (`*/list`), Abruf- (`*/get`) und Ausführungs- (`*/call`) Methodenmustern
- **Protokollarchitektur**: Einführung eines zweischichtigen Architekturmodells
  - Datenschicht: JSON-RPC 2.0 Basis mit Lifecycle-Management und Primitives
  - Transportschicht: STDIO (lokal) und Streamable HTTP mit SSE (remote) Transportmechanismen
- **Sicherheitsrahmenwerk**: Umfassende Sicherheitsprinzipien einschließlich expliziter Benutzerzustimmung, Datenschutz, Tool-Ausführungssicherheit und Transportschichtsicherheit
- **Kommunikationsmuster**: Aktualisierte Protokollnachrichten zur Darstellung von Initialisierung, Discovery, Ausführung und Benachrichtigungsabläufen
- **Codebeispiele**: Aktualisierte mehrsprachige Beispiele (.NET, Java, Python, JavaScript) zur Abbildung aktueller MCP SDK-Patterns

#### Sicherheit (02-Security/) - Umfassende Sicherheitsüberarbeitung  
- **Standardausrichtung**: Vollständige Ausrichtung an den Sicherheitsanforderungen der MCP-Spezifikation 2025-06-18
- **Authentifizierungsevolution**: Dokumentierte Entwicklung von benutzerdefinierten OAuth-Servern zur Delegation an externe Identitätsanbieter (Microsoft Entra ID)
- **KI-spezifische Bedrohungsanalyse**: Erweiterte Abdeckung moderner KI-Angriffsvektoren
  - Detaillierte Szenarien zu Prompt Injection Angriffen mit realen Beispielen
  - Mechanismen der Tool-Vergiftung und "Rug Pull" Angriffsmuster
  - Kontextfenstervergiftung und Modellverwirrungsangriffe
- **Microsoft KI-Sicherheitslösungen**: Umfassende Abdeckung des Microsoft-Sicherheitsökosystems
  - AI Prompt Shields mit fortschrittlicher Erkennung, Hervorhebung und Trennzeichen-Techniken
  - Azure Content Safety Integrationsmuster
  - GitHub Advanced Security zum Schutz der Lieferkette
- **Erweiterte Bedrohungsminderung**: Detaillierte Sicherheitskontrollen für
  - Sitzungs-Hijacking mit MCP-spezifischen Angriffsszenarien und kryptografischen Sitzungs-ID-Anforderungen
  - Confused Deputy Probleme in MCP-Proxy-Szenarien mit expliziten Zustimmungsanforderungen
  - Token-Passthrough-Schwachstellen mit verpflichtenden Validierungskontrollen
- **Lieferkettensicherheit**: Erweiterte KI-Lieferkettendeckung einschließlich Foundation Models, Embeddings-Services, Kontextanbietern und Drittanbieter-APIs
- **Foundation Security**: Verbesserte Integration mit Unternehmenssicherheitsmustern einschließlich Zero-Trust-Architektur und Microsoft-Sicherheitsökosystem
- **Ressourcenorganisation**: Kategorisierte umfassende Ressourcenlinks nach Typ (Offizielle Docs, Standards, Forschung, Microsoft-Lösungen, Implementierungsleitfäden)

### Verbesserungen der Dokumentationsqualität
- **Strukturierte Lernziele**: Verbesserte Lernziele mit spezifischen, umsetzbaren Ergebnissen
- **Querverweise**: Hinzugefügte Links zwischen verwandten Sicherheits- und Kernkonzeptthemen
- **Aktuelle Informationen**: Alle Datumsangaben und Spezifikationslinks auf aktuelle Standards aktualisiert
- **Implementierungsanleitungen**: Hinzugefügte spezifische, umsetzbare Implementierungsrichtlinien in beiden Abschnitten

## 16. Juli 2025

### README- und Navigationsverbesserungen
- Komplett neu gestaltete Curriculum-Navigation in README.md
- Ersetzte `<details>`-Tags durch zugänglicheres tabellenbasiertes Format
- Erstellte alternative Layoutoptionen im neuen Ordner "alternative_layouts"
- Hinzugefügte kartenbasierte, tabbed- und Akkordeon-Navigationsbeispiele
- Aktualisierte Repository-Strukturabschnitt zur Aufnahme aller neuesten Dateien
- Verbesserter Abschnitt "Wie man dieses Curriculum verwendet" mit klaren Empfehlungen
- Aktualisierte MCP-Spezifikationslinks auf korrekte URLs
- Hinzugefügter Abschnitt Context Engineering (5.14) zur Curriculum-Struktur

### Aktualisierungen des Studienleitfadens
- Komplett überarbeiteter Studienleitfaden zur Angleichung an aktuelle Repository-Struktur
- Neue Abschnitte für MCP Clients und Tools sowie populäre MCP Server hinzugefügt
- Aktualisierte Visual Curriculum Map zur genauen Abbildung aller Themen
- Verbesserte Beschreibungen der Advanced Topics zur Abdeckung aller Spezialgebiete
- Aktualisierter Abschnitt Fallstudien zur Abbildung tatsächlicher Beispiele
- Hinzugefügtes umfassendes Änderungsprotokoll

### Community-Beiträge (06-CommunityContributions/)
- Detaillierte Informationen zu MCP-Servern für Bildgenerierung hinzugefügt
- Umfassender Abschnitt zur Nutzung von Claude in VSCode hinzugefügt
- Cline Terminal-Client Setup- und Nutzungsanleitungen hinzugefügt
- MCP-Client-Abschnitt aktualisiert, um alle populären Client-Optionen einzuschließen
- Verbesserte Beitragsbeispiele mit genaueren Codebeispielen

### Erweiterte Themen (05-AdvancedTopics/)
- Alle spezialisierten Themenordner mit konsistenter Benennung organisiert
- Materialien und Beispiele zum Context Engineering hinzugefügt
- Dokumentation zur Foundry Agent Integration hinzugefügt
- Verbesserte Dokumentation zur Entra ID Sicherheitsintegration

## 11. Juni 2025

### Erste Erstellung
- Erste Version des MCP for Beginners Curriculums veröffentlicht
- Grundstruktur für alle 10 Hauptabschnitte erstellt
- Visual Curriculum Map für Navigation implementiert
- Erste Beispielprojekte in mehreren Programmiersprachen hinzugefügt

### Erste Schritte (03-GettingStarted/)
- Erste Server-Implementierungsbeispiele erstellt
- Anleitung zur Client-Entwicklung hinzugefügt
- Integration von LLM-Clients dokumentiert
- VS Code Integrationsdokumentation hinzugefügt
- Server-Sent Events (SSE) Server-Beispiele implementiert

### Kernkonzepte (01-CoreConcepts/)
- Detaillierte Erklärung der Client-Server-Architektur hinzugefügt
- Dokumentation zu Schlüsselkomponenten des Protokolls erstellt
- Messaging-Muster im MCP dokumentiert

## 23. Mai 2025

### Repository-Struktur
- Repository mit grundlegender Ordnerstruktur initialisiert
- README-Dateien für jeden Hauptabschnitt erstellt
- Übersetzungsinfrastruktur eingerichtet
- Bildmaterialien und Diagramme hinzugefügt

### Dokumentation
- Erste README.md mit Curriculum-Übersicht erstellt
- CODE_OF_CONDUCT.md und SECURITY.md hinzugefügt
- SUPPORT.md mit Hilfestellungen eingerichtet
- Vorläufige Struktur des Studienleitfadens erstellt

## 15. April 2025

### Planung und Rahmenwerk
- Erste Planung für MCP for Beginners Curriculum
- Lernziele und Zielgruppe definiert
- 10-Abschnitt-Struktur des Curriculums skizziert
- Konzeptuelles Rahmenwerk für Beispiele und Fallstudien entwickelt
- Erste Prototyp-Beispiele für Schlüsselkonzepte erstellt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->