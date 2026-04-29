# Änderungsprotokoll: MCP für Anfänger Curriculum

Dieses Dokument dient als Aufzeichnung aller wesentlichen Änderungen am Model Context Protocol (MCP) für Anfänger Curriculum. Änderungen werden in umgekehrter chronologischer Reihenfolge dokumentiert (neueste Änderungen zuerst).

## 11. April 2026

### Neue Lektion, Dokumentationskorrekturen und Abhängigkeitsaktualisierungen

#### Neue Curriculuminhalte hinzugefügt

**Modul 05 - Fortgeschrittene Themen**  
- **Lektion 5.17: Adversarial Multi-Agent Reasoning mit MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Neuer ausführlicher Leitfaden, der das adversarielle Debattenmuster für Multi-Agenten-Systeme behandelt  
  - Mermaid-Architekturdiagramm: zwei Agenten → geteilter MCP-Server → Debattentranskript → Richter → Urteil  
  - Geteilter MCP-Tool-Server (`web_search` + `run_python`) implementiert in Python und TypeScript  
  - Gegensätzliche System-Prompts (FÜR / GEGEN / Richter) mit expliziten Tool-Nutzungsanforderungen  
  - Debatten-Orchestrator in Python, TypeScript und C#, der Runden verwaltet und Argumente weiterleitet  
  - MCP `ClientSession` Anbindung für den Orchestrator an echte Tool-Aufrufe  
  - Anwendungsfall-Tabelle (Halluzinations-Erkennung, Bedrohungsmodellierung, API-Design-Review, Faktenprüfung, Technologieauswahl)  
  - Sicherheitsüberlegungen: Sandbox-Ausführung, Tool-Aufruf Validierung, Ratenbegrenzung, Audit-Logging  
  - Strukturierte Übung mit drei praktischen Szenarien (Code-Review, Architekturentscheidung, Inhaltsmoderation)  

#### Dokumentationskorrekturen

**Modul 03 - Einstieg**  
- **05-stdio-server/README.md**: Unvollständiges TypeScript-stdio-Server-Beispiel korrigiert — fehlende Transport-Instanziierung (`new StdioServerTransport()`) und `server.connect(transport)`-Aufruf hinzugefügt, passend zu den Python- und .NET-Beispielen im gleichen Abschnitt  
- **14-sampling/README.md**: Tippfehler korrigiert — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`  

#### Curriculum Updates

**Haupt-README.md**  
- Eintrag 5.17 (Adversarial Multi-Agent Reasoning mit MCP) zur Curriculum-Tabelle mit Direktlink zur neuen Lektion hinzugefügt  

**05-AdvancedTopics/README.md**  
- Zeile für Lektion 5.17 zur Lektionentabelle hinzugefügt  

**study_guide.md**  
- Thema Adversarial Multi-Agent Reasoning zur Mind-Map und Fließtext-Beschreibung der Fortgeschrittenen Themen hinzugefügt  

#### Code- und Sicherheitsfixes

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**  
- **Sicherheitsfix — Command Injection**: `execSync` Shell-Interpolation durch `execFile` + `promisify` im TypeScript `run_python` Tool ersetzt, wodurch die Angriffsfläche für Kommando-Injektion entfällt (LLM-gesteuerter Code wird jetzt als Literal-argv-Element ohne Shell-Einbindung übergeben)  
- **MCP-Tool-Loop-Anbindung**: Python-Debatten-Orchestrator aktualisiert, um den `AsyncAnthropic` Client (statt blockierendem Sync `Anthropic`) zu verwenden, eine live `ClientSession` direkt an jeden Agenten-Turn zu übergeben, Tool-Definitionen über `session.list_tools()` in jeder Runde abzurufen sowie `tool_use` Blöcke über `session.call_tool()` in einer Schleife auszulösen, bis das Modell eine finale Textantwort ausgibt  

#### Abhängigkeitsaktualisierungen

- `hono` auf Version 4.12.12 in mehreren Paketen aktualisiert (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- `@hono/node-server` von 1.19.11 auf 1.19.13 in TypeScript-Paketen aktualisiert  
- `cryptography` von 46.0.5 auf 46.0.7 in Python-Paketen (10-StreamliningAIWorkflows Labs 3 und 4) aktualisiert  
- `lodash` von 4.17.23 auf 4.18.1 im 10-StreamliningAIWorkflows Inspector aktualisiert  

#### Übersetzungen

- Übersetzungen für 48+ Sprachen mit den neuesten Quelländerungen synchronisiert (i18n Update)  

---

## 5. Februar 2026

### Repository-weiter Validierungs- und Navigationsverbesserungen

#### Neue Curriculuminhalte hinzugefügt

**Modul 03 - Einstieg**  
- **12-mcp-hosts/README.md**: Neuer umfassender Leitfaden zur Einrichtung von MCP-Hosts  
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf Konfigurationsbeispiele  
  - JSON Konfigurationsvorlagen für alle wichtigen Hosts  
  - Vergleichstabelle der Transporttypen (stdio, SSE/HTTP, WebSocket)  
  - Fehlerbehebung bei typischen Verbindungsproblemen  
  - Sicherheitsempfehlungen für Host-Konfiguration  

- **13-mcp-inspector/README.md**: Neuer Debugging-Leitfaden für den MCP Inspector  
  - Installationsmethoden (npx, npm global, aus dem Quellcode)  
  - Verbindung zu Servern via stdio und HTTP/SSE  
  - Test-Tools, Ressourcen und Prompt-Workflows  
  - VS Code Integration mit MCP Inspector  
  - Häufige Debugging-Szenarien mit Lösungsvorschlägen  

**Modul 04 - Praktische Implementierung**  
- **pagination/README.md**: Neuer Leitfaden zur Paginierungs-Implementierung  
  - Cursor-basierte Paginierungsmuster in Python, TypeScript, Java  
  - Client-seitige Paginierungsbehandlung  
  - Cursor-Design-Strategien (opaque vs. structured)  
  - Performance-Optimierungsempfehlungen  

**Modul 05 - Fortgeschrittene Themen**  
- **mcp-protocol-features/README.md**: Neuer Look-Through zu Protokollfunktionen  
  - Fortschrittsbenachrichtigungen implementiert  
  - Request-Abbruchmuster  
  - Ressourcentemplates mit URI-Mustern  
  - Server-Lifecycle Management  
  - Steuerung von Log-Leveln  
  - Fehlerbehandlungsmuster mit JSON-RPC-Codes  

#### Navigationskorrekturen (24+ Dateien aktualisiert)

**Hauptmodul READMEs**  
 Verweisen nun auf sowohl die erste Lektion ALS AUCH das nächste Modul  

**02-Security Unterdateien**  
- Alle fünf ergänzenden Sicherheitsdokumente verfügen jetzt über "What's Next" Navigation:  

**09-Fallstudien Dateien**  
- Alle Fallstudien-Dateien haben jetzt sequentielle Navigation:  

**10-StreamliningAI Labs**  
"What's Next"-Abschnitt zu Modul 10 Übersicht und Modul 11 hinzugefügt  

#### Code- und Inhaltskorrekturen

**SDK- und Abhängigkeitsupdates**  
Leere openai-Version auf `^4.95.0` gesetzt  
SDK von `^1.8.0` auf `>=1.26.0` aktualisiert  
MCP Version-Pins auf `>=1.26.0` aktualisiert  

**Code-Korrekturen**  
Ungültiges Modell `gpt-4o-mini` auf `gpt-4.1-mini` korrigiert  

**Inhaltskorrekturen**  
Defekten Link `READMEmd` → `README.md` korrigiert, Curriculum-Überschrift `Module 1-3` → `Module 0-3` korrigiert, Case-sensitive Pfad richtiggestellt  
Beschädigten doppelten Inhalt von Fallstudie 5 entfernt  

**Anfänger-Leitfaden Verbesserungen**  
Einführung, Lernziele und Voraussetzungen für Anfänger hinzugefügt  

#### Curriculum Updates

**Haupt-README.md**  
- Einträge 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protokollfunktionen) zur Curriculum-Tabelle hinzugefügt  

**Modul-READMEs**  
Lektionen 12 und 13 zur Lektionenliste hinzugefügt  
Abschnitt Praktische Leitfäden mit Pagination-Link hinzugefügt  
Lektionen 5.15 (Custom Transport) und 5.16 (Protokollfunktionen) hinzugefügt  

**study_guide.md**  
- Mindmap mit allen neuen Themen aktualisiert: MCP Hosts Einrichtung, MCP Inspector, Pagination-Strategien, Protokoll-Funktions-Durchblick  

## 28. Januar 2026

### MCP Spezifikation 2025-11-25 Compliance-Überprüfung

#### Erweiterung der Kernkonzepte (01-CoreConcepts/)  
- **Neue Client-Primitiv - Roots**: Umfangreiche Dokumentation zum Roots Client-Primitiv hinzugefügt, das Server befähigt, Dateisystem-Grenzen und Zugriffsrechte zu verstehen  
- **Tool-Anmerkungen**: Dokumentation zu Tool-Verhaltensanmerkungen (`readOnlyHint`, `destructiveHint`) für bessere Tool-Ausführungsentscheidungen ergänzt  
- **Toolaufruf in Sampling**: Sampling-Dokumentation aktualisiert, um `tools` und `toolChoice` Parameter für modellgesteuerte Tool-Aufrufe während Sampling-Anfragen einzubeziehen  
- **URL-Modus Auslösung**: Dokumentation zur URL-basierten Auslösung für serverinitiierte externe Webinteraktionen hinzugefügt  
- **Tasks (Experimentell)**: Neuer Abschnitt dokumentiert die experimentelle Tasks-Funktion für dauerhafte Ausführungs-Wrapper und verzögerte Ergebnisabfrage  
- **Icons Unterstützung**: Vermerkt, dass Tools, Ressourcen, Ressourcentemplates und Prompts jetzt Icons als zusätzliche Metadaten enthalten können  

#### Dokumentationsupdates  
- **README.md**: Bezug auf MCP Spezifikation 2025-11-25 Version und Datum-basierte Versionssteuerung hinzugefügt  
- **study_guide.md**: Curriculum-Karte um Tasks und Tool-Anmerkungen im Abschnitt Kernkonzepte ergänzt; Dokument-Zeitstempel aktualisiert  

#### Spezifikations-Compliance-Verifizierung  
- **Protokollversion**: Bestätigung, dass alle Dokumentationen die aktuelle MCP Spezifikation 2025-11-25 referenzieren  
- **Architekturausrichtung**: Bestätigung der Genauigkeit der Dokumentation zur zweischichtigen Architektur (Datenebene + Transporteebene)  
- **Primitiven-Dokumentation**: Server-Primitiven (Ressourcen, Prompts, Tools) und Client-Primitiven (Sampling, Auslösung, Logging, Roots) validiert  
- **Transportmechanismen**: STDIO- und Streamable HTTP-Transport-Dokumentation bestätigt  
- **Sicherheitsleitlinien**: Übereinstimmung mit aktuellen MCP Sicherheitsbest-Practices-Dokumentationen bestätigt  

#### Wichtige MCP 2025-11-25 Funktionen dokumentiert  
- **OpenID Connect Discovery**: Auth-Server-Erkennung über OIDC  
- **OAuth Client-ID Metadokumente**: Empfohlenes Client-Registrierungsverfahren  
- **JSON Schema 2020-12**: Standarddialekt für MCP Schema-Definitionen  
- **SDK Stufensystem**: Formalisierte Anforderungen für SDK Feature-Unterstützung und Wartung  
- **Governance-Struktur**: Formalisierte Arbeitsgruppen und Interessensgruppen in MCP Governance  

### Größtes Update der Sicherheitsdokumentation (02-Security/)

#### Integration des MCP Security Summit Workshops (Sherpa)  
- **Neue Hands-on Trainingsressource**: Umfassende Integration mit dem [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in allen Sicherheitsdokumentationen  
- **Expeditionsweg-Abdeckung**: Dokumentierte komplette Camp-zu-Camp-Reise vom Basislager bis zum Gipfel  
- **OWASP-Ausrichtung**: Sämtliche Sicherheitsanleitungen nun auf OWASP MCP Azure Security Guide Risiken gemappt  

#### OWASP MCP Top 10 Integration  
- **Neuer Abschnitt**: OWASP MCP Top 10 Sicherheitsrisiken-Tabelle mit Azure-Minderungen zum Haupt-Security-README hinzugefügt  
- **Risikobasierte Dokumentation**: Aktualisierung des mcp-security-controls-2025.md mit OWASP MCP Risiko-Verweisen für jeden Sicherheitsbereich  
- **Referenzarchitektur**: Verlinkung auf OWASP MCP Azure Security Guide Referenzarchitektur und Implementierungsmuster  

#### Aktualisierte Sicherheitsdateien  
- **README.md**: Sherpa Workshop Übersicht, Expeditionswegen-Tabelle, OWASP MCP Top 10 Risiko-Zusammenfassung und Hands-on Training Abschnitt ergänzt  
- **mcp-security-controls-2025.md**: Header auf Februar 2026 aktualisiert, OWASP Risiko-Verweise (MCP01-MCP08) hinzugefügt, Inkonsistenz der Spezifikationsversion korrigiert  
- **mcp-security-best-practices-2025.md**: Sherpa- und OWASP-Ressourcen Abschnitt hinzugefügt, Zeitstempel aktualisiert  
- **mcp-best-practices.md**: Hands-on Training Abschnitt mit Sherpa- und OWASP Links ergänzt  
- **azure-content-safety-implementation.md**: Verweis auf OWASP MCP06, Sherpa Camp 3 Ausrichtung und zusätzliche Ressourcen-Sektion hinzugefügt  

#### Neue Ressourcenlinks hinzugefügt  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Einzelne OWASP MCP Risiko-Seiten (MCP01-MCP10)  

### Curriculum-weite MCP Spezifikation 2025-11-25 Ausrichtung

#### Modul 03 - Einstieg  
- **SDK-Dokumentation**: Go SDK zur offiziellen SDK-Liste hinzugefügt; alle SDK-Bezüge an MCP Spezifikation 2025-11-25 angepasst  
- **Transport-Klarstellung**: STDIO- und HTTP Streaming Transportbeschreibungen mit expliziten Spezifikationsverweisen aktualisiert  

#### Modul 04 - Praktische Implementierung  
- **SDK Updates**: Go SDK hinzugefügt; SDK-Liste mit Spezifikationsversionsverweis aktualisiert  
- **Autorisierungsspezifikation**: MCP Autorisierungsspezifikation-Link auf aktuelle 2025-11-25 Version aktualisiert  

#### Modul 05 - Fortgeschrittene Themen  
- **Neue Funktionen**: Hinweis zu neuen MCP Spezifikation 2025-11-25 Features (Tasks, Tool-Anmerkungen, URL-Modus Auslösung, Roots) hinzugefügt  
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa Workshop Links zu Zusatzreferenzen hinzugefügt  

#### Modul 06 - Gemeinschaftsbeiträge  
- **SDK-Liste**: Swift und Rust SDKs hinzugefügt; Spezifikations-Link auf 2025-11-25 aktualisiert  
- **Spezifikationsverweis**: MCP Spezifikation Link auf direkte Spezifikations-URL aktualisiert  

#### Modul 07 - Lektionen aus früher Einführung  
- **Ressourcen-Updates**: MCP Spezifikation 2025-11-25 Link und OWASP MCP Top 10 zu Zusatzressourcen hinzugefügt  

#### Modul 08 - Best Practices  
- **Spezifikationsversion**: MCP Spezifikation Verweis auf 2025-11-25 aktualisiert  
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa Workshop zu Zusatzreferenzen hinzugefügt  

#### Modul 10 - KI-Workflows optimieren  
- **Abzeichen-Update**: MCP Version Badge von SDK-Version (1.9.3) auf Spezifikationsversion (2025-11-25) geändert  
- **Ressourcenlinks**: MCP Spezifikation Link aktualisiert; OWASP MCP Top 10 hinzugefügt  

#### Modul 11 - MCP Server Hands-on Labs  
- **Spezifikationsverweis**: MCP Spezifikation Link auf Version 2025-11-25 aktualisiert  
- **Sicherheitsressourcen**: OWASP MCP Top 10 in offiziellen Ressourcen ergänzt  

## 18. Dezember 2025
### Sicherheitsdokumentations-Update - MCP-Spezifikation 2025-11-25

#### MCP Sicherheits-Best Practices (02-Security/mcp-best-practices.md) - Versions-Update der Spezifikation
- **Protokollversions-Update**: Aktualisiert auf die neueste MCP-Spezifikation 2025-11-25 (veröffentlicht am 25. November 2025)
  - Alle Versionsverweise der Spezifikation von 2025-06-18 auf 2025-11-25 aktualisiert
  - Dokumentdatumsverweise von 18. August 2025 auf 18. Dezember 2025 aktualisiert
  - Überprüft, dass alle Spezifikations-URLs auf die aktuelle Dokumentation verweisen
- **Inhaltsvalidierung**: Umfassende Validierung der Sicherheits-Best Practices gegen neueste Standards
  - **Microsoft Security Solutions**: Überprüft aktuelle Terminologie und Links für Prompt Shields (vormals „Jailbreak-Risikodetektion“), Azure Content Safety, Microsoft Entra ID und Azure Key Vault
  - **OAuth 2.1 Sicherheit**: Bestätigung der Übereinstimmung mit den neuesten OAuth-Sicherheits-Best Practices
  - **OWASP-Standards**: Validierung, dass die OWASP Top 10 für LLMs weiterhin aktuell sind
  - **Azure Services**: Überprüft alle Microsoft Azure-Dokumentationslinks und Best Practices
- **Standards-Ausrichtung**: Alle referenzierten Sicherheitsstandards als aktuell bestätigt
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Sicherheits-Best Practices
  - Azure Sicherheits- und Compliance-Frameworks
- **Implementierungsressourcen**: Überprüft alle Links zu Implementierungsanleitungen und Ressourcen
  - Azure API Management Authentifizierungsmuster
  - Microsoft Entra ID Integrationsanleitungen
  - Azure Key Vault Geheimnisverwaltung
  - DevSecOps Pipelines und Monitoring-Lösungen

### Dokumentationsqualitätssicherung
- **Spezifikationskonformität**: Sicherstellung, dass alle verpflichtenden MCP-Sicherheitsanforderungen (MUST/MUST NOT) mit der neuesten Spezifikation übereinstimmen
- **Ressourcenaktualität**: Überprüfung aller externen Links zu Microsoft-Dokumentation, Sicherheitsstandards und Implementierungsanleitungen
- **Best Practices Abdeckung**: Bestätigung einer umfassenden Abdeckung von Authentifizierung, Autorisierung, KI-spezifischen Bedrohungen, Lieferkettensicherheit und Unternehmensmustern

## 6. Oktober 2025

### Erweiterung des Einführungsabschnitts – Fortgeschrittene Servernutzung & Einfache Authentifizierung

#### Fortgeschrittene Servernutzung (03-GettingStarted/10-advanced)
- **Neues Kapitel hinzugefügt**: Einführung eines umfassenden Leitfadens zur fortgeschrittenen MCP-Servernutzung, der sowohl reguläre als auch Low-Level-Serverarchitekturen abdeckt.
  - **Regulärer vs. Low-Level-Server**: Detaillierter Vergleich und Codebeispiele in Python und TypeScript für beide Ansätze.
  - **Handler-basierte Architektur**: Erklärung der handlerbasierten Verwaltung von Werkzeugen/Ressourcen/Prompts für skalierbare und flexible Serverimplementierungen.
  - **Praxisnahe Muster**: Szenarien aus der Praxis, bei denen Low-Level-Servermuster für fortgeschrittene Features und Architektur von Vorteil sind.

#### Einfache Authentifizierung (03-GettingStarted/11-simple-auth)
- **Neues Kapitel hinzugefügt**: Schritt-für-Schritt-Anleitung zur Implementierung einfacher Authentifizierung in MCP-Servern.
  - **Auth-Konzepte**: Klare Erklärung von Authentifizierung vs. Autorisierung und Umgang mit Anmeldeinformationen.
  - **Einfaches Authentifizierungs-Implementierung**: Middlewarebasierte Authentifizierungsmuster in Python (Starlette) und TypeScript (Express) mit Codebeispielen.
  - **Fortschritt zu fortgeschrittener Sicherheit**: Leitfaden vom Beginn mit einfacher Authentifizierung bis zur Nutzung von OAuth 2.1 und RBAC mit Verweisen auf fortgeschrittene Sicherheitsmodule.

Diese Ergänzungen bieten praxisorientierte, handlungsfähige Anleitungen zum Aufbau robuster, sicherer und flexibler MCP-Serverimplementierungen und verbinden grundlegende Konzepte mit fortgeschrittenen Produktionsmustern.

## 29. September 2025

### MCP Server-Datenbank-Integrations-Labs – Umfassender praxisorientierter Lernpfad

#### 11-MCPServerHandsOnLabs – Neue vollständige Datenbank-Integrationscurriculum
- **Vollständiger 13-Labs-Lernpfad**: Hinzugefügt ein umfassendes praxisorientiertes Curriculum für den Aufbau produktionsreifer MCP-Server mit PostgreSQL-Datenbankintegration  
  - **Praxisbeispiel**: Zava Retail Analytics Anwendungsfall mit Enterprise-Mustern  
  - **Strukturierter Lernfortschritt**:
    - **Labs 00-03: Grundlagen** – Einführung, Kernarchitektur, Sicherheit & Multi-Tenant, Umgebungseinrichtung  
    - **Labs 04-06: Aufbau des MCP-Servers** – Datenbankdesign & Schema, MCP-Server-Implementierung, Tool-Entwicklung  
    - **Labs 07-09: Erweiterte Funktionen** – Semantische Suche Integration, Tests & Debugging, VS Code Integration  
    - **Labs 10-12: Produktion & Best Practices** – Bereitstellungsstrategien, Monitoring & Beobachtbarkeit, Best Practices & Optimierung  
  - **Enterprise-Technologien**: FastMCP Framework, PostgreSQL mit pgvector, Azure OpenAI Embeddings, Azure Container Apps, Application Insights  
  - **Erweiterte Features**: Row Level Security (RLS), semantische Suche, Mandantenfähiger Datenzugriff, Vektor-Embeddings, Echtzeit-Überwachung

#### Terminologie-Standardisierung – Modul-zu-Lab-Umbenennung
- **Umfassendes Dokumentations-Update**: Systematische Aktualisierung sämtlicher README-Dateien in 11-MCPServerHandsOnLabs auf den Begriff „Lab“ statt „Modul“
  - **Abschnittsüberschriften**: „Was dieses Modul abdeckt“ wurde in allen 13 Labs zu „Was dieses Lab abdeckt“ geändert
  - **Inhaltsbeschreibung**: „Dieses Modul bietet...“ wurde in „Dieses Lab bietet...“ geändert
  - **Lernziele**: „Am Ende dieses Moduls...“ wurde zu „Am Ende dieses Labs...“ aktualisiert
  - **Navigationslinks**: Alle „Modul XX:“-Verweise in Querverweisen und Navigation wurden zu „Lab XX:“ geändert
  - **Abschlussverfolgung**: „Nach Abschluss dieses Moduls...“ nun „Nach Abschluss dieses Labs...“
  - **Technische Referenzen erhalten**: Python-Modulreferenzen in Konfigurationsdateien (z. B. `"module": "mcp_server.main"`) unverändert beibehalten

#### Studienführer-Erweiterung (study_guide.md)
- **Visuelle Curriculum-Karte**: Neuer Abschnitt „11. Datenbank-Integrations-Labs“ mit detailliertem Lab-Struktur-Diagramm ergänzt
- **Repository-Struktur**: Von zehn auf elf Hauptabschnitte mit ausführlicher Beschreibung von 11-MCPServerHandsOnLabs erweitert
- **Lernpfad-Anleitung**: Navigationsanweisungen auf Abschnitte 00-11 erweitert
- **Technologieabdeckung**: FastMCP, PostgreSQL, Azure-Services-Integrationsdetails hinzugefügt
- **Lernergebnisse**: Fokus auf produktionsreife Serverentwicklung, Datenbank-Integrationsmuster und Unternehmenssicherheit

#### Haupt-README-Struktur-Verbesserung
- **Lab-basierte Terminologie**: Haupt-README.md von 11-MCPServerHandsOnLabs auf durchgängig „Lab“-Struktur aktualisiert
- **Lernpfad-Organisation**: Klare Progression von Grundlagen über fortgeschrittene Implementierung bis Produktionseinführung
- **Praxisorientierung**: Betonung praktischer, hands-on Lernansätze mit Enterprise-Mustern und Technologien

### Verbesserungen der Dokumentationsqualität & Konsistenz
- **Hands-On Lernfokus**: Stärkung des praktischen, lab-basierten Ansatzes in der gesamten Dokumentation
- **Enterprise Muster Fokus**: Betonung produktionsreifer Implementierungen und Unternehmenssicherheit
- **Technologieintegration**: Umfassende Abdeckung moderner Azure-Dienste und KI-Integrationsmuster
- **Lernfortschritt**: Klar strukturierter Pfad von Grundlagen bis Produktion

## 26. September 2025

### Erweiterung Case Studies – GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) – Fokus auf Ecosystem-Entwicklung
- **README.md**: Großes Update mit umfassender Case Study zur GitHub MCP Registry
  - **GitHub MCP Registry Case Study**: Neue ausführliche Fallstudie zur Einführung der GitHub MCP Registry im September 2025
    - **Problem-Analyse**: Detaillierte Untersuchung fragmentierter MCP-Server-Erkennung und Bereitstellungsherausforderungen
    - **Lösungsarchitektur**: GitHubs zentralisierte Registry-Lösung mit Ein-Klick-VS-Code-Installation
    - **Geschäftlicher Nutzen**: Messbare Verbesserungen bei Entwickler-Onboarding und Produktivität
    - **Strategischer Wert**: Fokus auf modulare Agent-Bereitstellung und Tool-übergreifende Interoperabilität
    - **Ecosystem-Entwicklung**: Positionierung als grundlegende Plattform für agentenbasierte Integration
  - **Verbesserte Case Study-Struktur**: Einheitliche Formatierung und umfassende Beschreibung sämtlicher sieben Fallstudien
    - Azure AI Travel Agents: Schwerpunkt Multi-Agenten-Orchestrierung
    - Azure DevOps Integration: Fokus Workflow-Automatisierung
    - Realtime Documentation Retrieval: Python Konsolenclient-Implementierung
    - Interaktiver Studienplan-Generator: Chainlit Conversational Web App
    - In-Editor Dokumentation: VS Code und GitHub Copilot Integration
    - Azure API Management: Enterprise API-Integrationsmuster
    - GitHub MCP Registry: Ecosystem-Entwicklung und Community-Plattform  
  - **Umfassender Abschluss**: Neuformulierter Fazitabschnitt mit Hervorhebung der sieben Case Studies über verschiedene MCP-Implementierungsdimensionen
    - Unternehmensintegration, Multi-Agenten-Orchestrierung, Entwicklerproduktivität
    - Ecosystem-Entwicklung, Bildungsanwendungen Kategorisierung
    - Verbesserte Einblicke in Architektur-, Implementierungsstrategien und Best Practices
    - Betonung von MCP als ausgereiftes, produktionsbereites Protokoll

#### Updates Study Guide (study_guide.md)
- **Visuelle Curriculum-Karte**: Mindmap um GitHub MCP Registry im Abschnitt Case Studies erweitert
- **Case Studies Beschreibung**: Verallgemeinerte Beschreibungen durch detaillierte Aufschlüsselung der sieben umfassenden Case Studies ersetzt
- **Repository-Struktur**: Abschnitt 10 mit umfassender Case Study-Abdeckung und spezifischen Implementierungsdetails aktualisiert
- **Changelog-Integration**: Eintrag vom 26. September 2025 hinzugefügt, der GitHub MCP Registry und Case Study-Erweiterungen dokumentiert
- **Datumsaktualisierung**: Fußzeile auf letzte Überarbeitung (26. September 2025) gesetzt

### Verbesserungen der Dokumentationsqualität
- **Konsistenzsteigerung**: Einheitliche Formatierung und Strukturierung der sieben Fallstudien
- **Umfassende Abdeckung**: Case Studies decken nun Unternehmens-, Entwicklerproduktivitäts- und Ecosystem-Entwicklungsszenarien ab
- **Strategische Positionierung**: Verstärkter Fokus auf MCP als grundlegende Plattform für Agentensystem-Bereitstellung
- **Ressourcenintegration**: Aktualisierung zusätzlicher Ressourcen um den Link zur GitHub MCP Registry

## 15. September 2025

### Erweiterung Fortgeschrittener Themen – Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) – Neuer fortgeschrittener Implementierungsleitfaden
- **README.md**: Vollständiger Implementierungsleitfaden für benutzerdefinierte MCP-Transportmechanismen
  - **Azure Event Grid Transport**: Umfassende serverlose ereignisgesteuerte Transportimplementierung
    - C#, TypeScript und Python Beispiele mit Azure Functions Integration
    - Event-getriebene Architektur-Muster für skalierbare MCP-Lösungen
    - Webhook-Receiver und Push-Nachrichtenverarbeitung
  - **Azure Event Hubs Transport**: Hochdurchsatz-Streaming-Transportimplementierung
    - Echtzeit-Streaming für latenzarme Szenarien
    - Partitionierungsstrategien und Checkpoint-Management
    - Nachrichten-Batching und Leistungsoptimierung
  - **Enterprise Integrationsmuster**: Produktionsfertige Architekturbeispiele
    - Verteilte MCP-Verarbeitung über mehrere Azure Functions
    - Hybride Transportarchitekturen mit mehreren Transporttypen
    - Nachrichtenverlässlichkeit, Fehlerbehandlung und Haltbarkeitsstrategien
  - **Sicherheit & Monitoring**: Azure Key Vault Integration und Beobachtbarkeitsmuster
    - Managed Identity Authentifizierung und Prinzip der geringsten Rechte
    - Application Insights Telemetrie und Performance-Monitoring
    - Circuit Breaker und Fehlertoleranzmuster
  - **Testframeworks**: Umfassende Teststrategien für Custom Transports
    - Unit Tests mit Testdoubles und Mocking-Frameworks
    - Integrationstests mit Azure Test Containers
    - Performance- und Lasttests

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) – Emerging AI Discipline
- **README.md**: Umfassende Erkundung von Context Engineering als aufstrebendes Fachgebiet
  - **Kernprinzipien**: Vollständiges Context Sharing, Entscheidungsbewusstsein bei Aktionen, Kontextfenster-Verwaltung
  - **MCP-Protokollausrichtung**: Wie das MCP-Design Herausforderungen des Context Engineerings adressiert
    - Einschränkungen des Kontextfensters und progressive Lade-Strategien
    - Relevanzbestimmung und dynamische Kontextabfrage
    - Multimodale Kontextverarbeitung und Sicherheitsaspekte
  - **Implementierungsansätze**: Single-Threaded vs. Multi-Agent-Architekturen
    - Kontext-Chunking und Priorisierungstechniken
    - Progressives Laden und Kompressionsstrategien
    - Schichtbasierte Kontextansätze und Optimierung der Abrufmechanismen
  - **Messframework**: Neue Metriken zur Bewertung der Kontextwirksamkeit
    - Eingabeeffizienz, Performance, Qualität und Nutzererfahrung
    - Experimentelle Ansätze zur Kontextoptimierung
    - Fehleranalyse und Verbesserungsmethoden

#### Curriculum Navigation Updates (README.md)
- **Erweiterte Modulstruktur**: Aktuelle Curriculums-Tabelle um neue fortgeschrittene Themen ergänzt
  - Hinzugefügt Context Engineering (5.14) und Custom Transport (5.15)
  - Einheitliche Formatierung und Navigationslinks über alle Module
  - Beschreibungen an aktuellen Inhalt angepasst

### Verbesserungen der Verzeichnisstruktur
- **Namensstandardisierung**: „mcp transport“ in „mcp-transport“ umbenannt für Konsistenz mit anderen Advanced-Topic-Ordnern
- **Inhaltsorganisation**: Alle 05-AdvancedTopics-Ordner folgen nun dem einheitlichen Namensmuster (mcp-[topic])

### Verbesserungen der Dokumentationsqualität
- **Abstimmung auf MCP-Spezifikation**: Alle neuen Inhalte verweisen auf aktuelle MCP-Spezifikation 2025-06-18
- **Mehrsprachige Beispiele**: Umfassende Codebeispiele in C#, TypeScript und Python
- **Enterprise Fokus**: Produktionstaugliche Muster und Azure Cloud-Integration durchgehend
- **Visuelle Dokumentation**: Mermaid-Diagramme zur Architektur- und Ablaufvisualisierung

## 18. August 2025

### Umfassendes Dokumentationsupdate – MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) – Vollständige Modernisierung
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Vollständige Neufassung abgestimmt auf MCP-Spezifikation 2025-06-18  
  - **Verpflichtende Anforderungen**: Hinzugefügte explizite MUSS/MUSS NICHT-Anforderungen aus offizieller Spezifikation mit klaren visuellen Indikatoren  
  - **12 Kern-Sicherheitspraktiken**: Umstrukturierung von einer 15-Punkte-Liste zu umfassenden Sicherheitsdomänen  
    - Tokensicherheit & Authentifizierung mit Integration externer Identitätsanbieter  
    - Sitzungsverwaltung & Transportsicherheit mit kryptographischen Anforderungen  
    - KI-spezifischer Bedrohungsschutz mit Microsoft Prompt Shields-Integration  
    - Zugriffskontrolle & Berechtigungen mit dem Prinzip der geringsten Privilegien  
    - Inhaltssicherheit & Überwachung mit Azure Content Safety-Integration  
    - Lieferkettensicherheit mit umfassender Komponentenverifikation  
    - OAuth-Sicherheit & Vermeidung von Confused Deputy mit PKCE-Implementierung  
    - Vorfallsreaktion & Wiederherstellung mit automatisierten Fähigkeiten  
    - Compliance & Governance mit regulatorischer Ausrichtung  
    - Erweiterte Sicherheitskontrollen mit Zero Trust-Architektur  
    - Integration des Microsoft-Sicherheitsökosystems mit umfassenden Lösungen  
    - Kontinuierliche Sicherheitsevolution mit adaptiven Praktiken  
  - **Microsoft Sicherheitslösungen**: Verbesserte Integrationsanleitung für Prompt Shields, Azure Content Safety, Entra ID und GitHub Advanced Security  
  - **Implementierungsressourcen**: Kategorisierte umfassende Ressourcenlinks unter Offizielle MCP-Dokumentation, Microsoft Sicherheitslösungen, Sicherheitsstandards und Implementierungsleitfäden  

#### Erweiterte Sicherheitskontrollen (02-Security/) - Unternehmensimplementierung  
- **MCP-SECURITY-CONTROLS-2025.md**: Vollständige Neugestaltung mit unternehmensgerechtem Sicherheitsrahmen  
  - **9 umfassende Sicherheitsdomänen**: Erweiterung von Basissteuerungen zu detailliertem Unternehmensrahmen  
    - Erweiterte Authentifizierung & Autorisierung mit Microsoft Entra ID-Integration  
    - Tokensicherheit & Anti-Passthrough-Kontrollen mit umfassender Validierung  
    - Sitzungs-Sicherheitskontrollen mit Hijacking-Prävention  
    - KI-spezifische Sicherheitskontrollen mit Schutz gegen Prompt Injection und Tool-Poisoning  
    - Vermeidung von Confused Deputy-Angriffen mit OAuth-Proxy-Sicherheit  
    - Tool-Ausführungs-Sicherheit mit Sandboxing und Isolation  
    - Lieferkettensicherheitskontrollen mit Abhängigkeitsverifizierung  
    - Überwachungs- & Erkennungssteuerungen mit SIEM-Integration  
    - Vorfallsreaktion & Wiederherstellung mit automatisierten Fähigkeiten  
  - **Implementierungsbeispiele**: Hinzugefügte detaillierte YAML-Konfigurationsblöcke und Codebeispiele  
  - **Integration Microsoft Lösungen**: Umfassende Abdeckung von Azure-Sicherheitsdiensten, GitHub Advanced Security und Unternehmens-Identitätsmanagement  

#### Erweiterte Themen Sicherheit (05-AdvancedTopics/mcp-security/) - Produktionsreife Implementierung  
- **README.md**: Vollständige Neufassung für Unternehmenssicherheitsimplementierung  
  - **Aktuelle Spezifikationsausrichtung**: Aktualisiert auf MCP-Spezifikation 2025-06-18 mit verpflichtenden Sicherheitsanforderungen  
  - **Erweiterte Authentifizierung**: Microsoft Entra ID-Integration mit umfangreichen .NET- und Java Spring Security-Beispielen  
  - **KI-Sicherheitsintegration**: Microsoft Prompt Shields- und Azure Content Safety-Implementierung mit detaillierten Python-Beispielen  
  - **Erweiterte Bedrohungsminderung**: Umfassende Implementierungsbeispiele für  
    - Vermeidung von Confused Deputy-Angriffen mit PKCE und Benutzerzustimmungsverifikation  
    - Verhinderung von Token-Passthrough mit Audience-Validierung und sicherer Tokenverwaltung  
    - Sitzungsentführungssicherung mit kryptographischer Bindung und Verhaltensanalyse  
  - **Integration Unternehmenssicherheit**: Azure Application Insights-Überwachung, Bedrohungserkennungs-Pipelines und Lieferkettensicherheit  
  - **Implementierungs-Checkliste**: Klare Trennung obligatorischer vs. empfohlenen Sicherheitskontrollen mit Vorteilen des Microsoft-Sicherheitsökosystems  

### Dokumentationsqualität & Standardausrichtung  
- **Spezifikationsverweise**: Alle Verweise auf aktuelle MCP-Spezifikation 2025-06-18 aktualisiert  
- **Microsoft-Sicherheitsökosystem**: Verbesserte Integrationsanleitungen in allen Sicherheitsdokumentationen  
- **Praxisnahe Implementierung**: Detaillierte Codebeispiele in .NET, Java und Python mit Unternehmensmustern hinzugefügt  
- **Ressourcenorganisation**: Umfassende Kategorisierung offizieller Dokumentationen, Sicherheitsstandards und Implementierungsleitfäden  
- **Visuelle Indikatoren**: Klare Markierung verpflichtender Anforderungen vs. empfohlener Praktiken  

#### Kernkonzepte (01-CoreConcepts/) - Vollständige Modernisierung  
- **Protokollversions-Update**: Auf Referenz der aktuellen MCP-Spezifikation 2025-06-18 mit datumsbasierter Versionierung (YYYY-MM-DD Format) aktualisiert  
- **Architekturverfeinerung**: Verbesserte Beschreibungen von Hosts, Clients und Servern zur Abbildung aktueller MCP-Architekturpattern  
  - Hosts nun klar definiert als KI-Anwendungen, die mehrere MCP-Client-Verbindungen koordinieren  
  - Clients beschrieben als Protokoll-Connectoren mit Eins-zu-eins-Serverbeziehungen  
  - Server mit Szenarien für lokale vs. remote Bereitstellung erweitert  
- **Primitive Umgestaltung**: Vollständige Überarbeitung der Server- und Client-Primitives  
  - Server-Primitives: Ressourcen (Datenquellen), Prompts (Vorlagen), Tools (ausführbare Funktionen) mit detaillierten Erklärungen und Beispielen  
  - Client-Primitives: Sampling (LLM-Ergebnisse), Elicitierung (Benutzereingabe), Logging (Debugging/Überwachung)  
  - Aktualisiert mit aktuellen Discovery- (`*/list`), Abruf- (`*/get`) und Ausführungs- (`*/call`) Methodenpatterns  
- **Protokollarchitektur**: Einführung eines zwei-schichtigen Architekturmodells  
  - Datenschicht: JSON-RPC 2.0-Grundlage mit Lebenszyklusmanagement und Primitives  
  - Transportschicht: STDIO (lokal) und Streamable HTTP mit SSE (remote) Transportmechanismen  
- **Sicherheitsrahmen**: Umfassende Sicherheitsprinzipien einschließlich expliziter Benutzerzustimmung, Datenschutz, Tool-Ausführungssicherheit und Transportschichtsicherheit  
- **Kommunikationsmuster**: Aktualisierte Protokollnachrichten zur Darstellung von Initialisierung, Discovery, Ausführung und Benachrichtigungen  
- **Codebeispiele**: Überarbeitete Mehrsprachbeispiele (.NET, Java, Python, JavaScript) zur Abbildung aktueller MCP SDK-Patterns  

#### Sicherheit (02-Security/) - Umfassende Sicherheitsüberarbeitung  
- **Standards-Ausrichtung**: Vollständige Ausrichtung an MCP-Spezifikation 2025-06-18 Sicherheitsanforderungen  
- **Authentifizierungsentwicklung**: Dokumentierte Entwicklung von kundenspezifischen OAuth-Servern hin zu externer Identitätsanbieter-Delegierung (Microsoft Entra ID)  
- **KI-spezifische Bedrohungsanalyse**: Verbesserte Abdeckung moderner KI-Angriffsvektoren  
  - Detaillierte Szenarien zu Prompt Injection-Angriffen mit Praxisbeispielen  
  - Mechanismen von Tool-Poisoning und "Rug Pull"-Angriffsmustern  
  - Kontextfenster-Poisoning und Modellverwirrungsangriffe  
- **Microsoft AI Sicherheitslösungen**: Umfassende Abdeckung des Microsoft Sicherheitsökosystems  
  - AI Prompt Shields mit fortgeschrittenen Erkennungs-, Highlighting- und Trennertechniken  
  - Azure Content Safety-Integrationsmuster  
  - GitHub Advanced Security für Lieferkettenschutz  
- **Erweiterte Bedrohungsminderung**: Detaillierte Sicherheitskontrollen für  
  - Sitzungsentführung mit MCP-spezifischen Angriffsszenarien und kryptographischen Sessions-ID-Anforderungen  
  - Confused Deputy-Probleme in MCP-Proxy-Szenarien mit expliziten Zustimmungsanforderungen  
  - Token-Passthrough-Schwachstellen mit verpflichtenden Validierungskontrollen  
- **Lieferkettensicherheit**: Erweiterte KI-Lieferkettensicherheit inklusive Foundation-Modellen, Embeddings-Diensten, Kontextanbietern und Drittanbieter-APIs  
- **Foundation-Sicherheit**: Verbesserte Integration mit Unternehmenssicherheitsmustern einschließlich Zero Trust-Architektur und Microsoft Sicherheitsökosystem  
- **Ressourcenorganisation**: Kategorisierte umfassende Ressourcenlinks nach Typ (Offizielle Docs, Standards, Forschung, Microsoft Lösungen, Implementierungsleitfäden)  

### Verbesserungen der Dokumentationsqualität  
- **Strukturierte Lernziele**: Verbessertes Lernziel-Set mit spezifischen, umsetzbaren Ergebnissen  
- **Querverweise**: Hinzugefügte Links zwischen verwandten Sicherheits- und Kernkonzept-Themen  
- **Aktuelle Informationen**: Alle Datumsangaben und Spezifikationslinks auf aktuelle Standards aktualisiert  
- **Implementierungsanleitung**: Spezifische, umsetzbare Implementierungsleitlinien in beiden Sektionen erweitert  

## 16. Juli 2025  

### README- und Navigationsverbesserungen  
- Vollständig neu gestaltete Curriculum-Navigation in README.md  
- Ersetzung der `<details>`-Tags durch besser zugängliches tabellenbasiertes Format  
- Alternative Layoutoptionen im neuen Ordner "alternative_layouts" erstellt  
- Hinzugefügte Beispiele für Karten-basierte, tabulatorische und Akkordeon-Navigation  
- Aktualisierter Abschnitte zur Repository-Struktur mit allen neuesten Dateien  
- Verbesserter Abschnitt "Wie man dieses Curriculum nutzt" mit klaren Empfehlungen  
- Aktualisierte MCP-Spezifikationslinks mit korrekten URLs  
- Hinzugefügt Context Engineering Abschnitt (5.14) zur Curriculum-Struktur  

### Aktualisierungen des Studienleitfadens  
- Vollständige Überarbeitung des Studienleitfadens zur Ausrichtung an aktueller Repository-Struktur  
- Neue Abschnitte zu MCP-Clients und Tools sowie populären MCP-Servern hinzugefügt  
- Aktualisierte Visual Curriculum Map zur genauen Abbildung aller Themen  
- Verfeinerte Beschreibungen der erweiterten Themen zur Abdeckung aller spezialisierten Bereiche  
- Aktualisierter Case Studies Abschnitt zur Abbildung realer Beispiele  
- Hinzugefügt dieses umfassende Änderungsprotokoll  

### Community-Beiträge (06-CommunityContributions/)  
- Detaillierte Informationen zu MCP-Servern für Bildgenerierung hinzugefügt  
- Umfangreicher Abschnitt zur Nutzung von Claude in VSCode  
- Einrichtung und Nutzung des Cline-Terminalclients dokumentiert  
- MCP-Client-Sektion aktualisiert mit allen populären Client-Optionen  
- Verbesserte Beitragsbeispiele mit präziseren Codebeispielen  

### Erweiterte Themen (05-AdvancedTopics/)  
- Alle spezialisierten Themenordner konsistent benannt und organisiert  
- Materialien und Beispiele zu Kontext-Engineering hinzugefügt  
- Dokumentation zur Foundry Agent Integration hinzugefügt  
- Verbesserte Dokumentation zur Entra ID Sicherheitsintegration  

## 11. Juni 2025  

### Erste Erstellung  
- Erste Version des MCP for Beginners Curriculums veröffentlicht  
- Grundstruktur für alle 10 Hauptabschnitte erstellt  
- Visual Curriculum Map für Navigation implementiert  
- Erste Beispielprojekte in mehreren Programmiersprachen hinzugefügt  

### Einstieg (03-GettingStarted/)  
- Erste Server-Implementierungsbeispiele erstellt  
- Anleitung zur Client-Entwicklung hinzugefügt  
- Integration von LLM-Clients dokumentiert  
- Dokumentation für VS Code-Integration beigefügt  
- Beispiele für Server-Sent Events (SSE) Server implementiert  

### Kernkonzepte (01-CoreConcepts/)  
- Detaillierte Erklärung der Client-Server-Architektur hinzugefügt  
- Dokumentation zu Schlüsselkomponenten des Protokolls erstellt  
- Nachrichtenmuster im MCP dokumentiert  

## 23. Mai 2025  

### Repository-Struktur  
- Repository mit Basisordnerstruktur initialisiert  
- README-Dateien für alle Hauptabschnitte erstellt  
- Übersetzungsinfrastruktur eingerichtet  
- Bild-Assets und Diagramme hinzugefügt  

### Dokumentation  
- Erste README.md mit Curriculum-Übersicht erstellt  
- CODE_OF_CONDUCT.md und SECURITY.md hinzugefügt  
- SUPPORT.md mit Hilfestellungen eingerichtet  
- Vorläufige Struktur des Studienleitfadens erstellt  

## 15. April 2025  

### Planung und Rahmenwerk  
- Erste Planungen für MCP for Beginners Curriculum  
- Lernziele und Zielpublikum definiert  
- Struktureller Rahmen mit 10 Abschnitten skizziert  
- Konzeptuelles Rahmenwerk für Beispiele und Fallstudien entwickelt  
- Erste Prototyp-Beispiele für Schlüsselkonzepte erstellt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->