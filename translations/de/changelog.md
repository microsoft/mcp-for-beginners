# Changelog: MCP für Anfänger Lehrplan

Dieses Dokument dient als Aufzeichnung aller wichtigen Änderungen am Model Context Protocol (MCP) für Anfänger Lehrplan. Änderungen werden in umgekehrter chronologischer Reihenfolge dokumentiert (neueste Änderungen zuerst).

## 29. Juli 2026

### Neues Modul 08 Begleitmaterial: Zuverlässigkeits-Sidecars und sichere Wiederholungen

Ein herstellerneutrales Begleitmaterial für MCP-Tools hinzugefügt, die reale
Effekte erzeugen, abgestimmt auf die finale `2026-07-28` Spezifikation.

- **Neu**: Die [Reliability Sidecar Begleitlektion][reliability-sidecar]
  verwendet eine Support-Ticket-Geschichte, zwei Mermaid-Diagramme und einen Wiederholungs-Entscheidungs-
  Ablauf, um stabile Betriebsschlüssel, atomare Duplikatsannahme,
  Abgleich, Beweisführung und die Tasks-Erweiterungsgrenze zu erklären.
- **Neu**: Eine Standardbibliothek Python- und SQLite-Fehlerinjektionsübung
  verwendet separate Operation- und Ticket-Speicher, um eine Antwort zu demonstrieren, die nach
  Commit eines externen Effekts verloren geht. Sechs deterministische Tests decken naive
  Duplikation, gesicherte Neustart-Wiederherstellung, Payload-Konflikte, zwischengespeicherte Ergebnisse,
  aktive Ansprüche und gleichzeitige Duplikatsannahme ab.
- **Aktualisiert**: Modul 08 verlinkt jetzt die Begleitlektion, identifiziert das
  finale `2026-07-28` zustandslose Anfragemodell, unterscheidet OpenTelemetry
  Observability vom veralteten MCP-Logging-Feature und beschränkt sein
  generisches Wiederholungsbeispiel auf schreibgeschützte Operationen.
- **Optional**: Die Lektion ordnet ihre portablen Konzepte einer markierten Community-
  Implementierung zu, ohne den gehosteten Dienst oder einen Netzwerkanruf Teil der
  Übung zu machen.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. Juli 2026

### Neue Lektion: Der 2026-07-28 MCP Spezifikations-Release Candidate

Neuer Inhalt zum kommenden `2026-07-28` MCP Spezifikations-Release Candidate (angekündigt am 21. Mai 2026; finale Veröffentlichung geplant für 28. Juli 2026), zusammengefasst aus dem [offiziellen Ankündigungs-Blogbeitrag](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Die Basisversion des Lehrplans bleibt **MCP Spezifikation 2025-11-25**, bis die neue Version ausgeliefert wird, daher wird dies als zukunftsgerichtete Orientierung und nicht als Neuauflage bestehender Lektionen dargestellt.

- **Neu**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — eine vollständige Lektion, die den zustandslosen Protokollkern behandelt (Entfernung des `initialize` Handshakes und `Mcp-Session-Id`), die neuen `Mcp-Method`/`Mcp-Name` Routing-Header, `ttlMs`/`cacheScope` Cache-Metadaten, W3C Trace Context in `_meta`, das formale Erweiterungs-Framework (MCP Apps und die neue Tasks-Erweiterung), sechs SEPs zur Authentifizierungs-Härtung, die Abkehr von Roots/Sampling/Logging und den Umstieg auf JSON Schema 2020-12 für Tools-Schemas.
- **Aktualisiert** mit zukunftsgerichteten Hinweisen und Verlinkungen zur neuen Lektion:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): Protokollversion-Hinweis, Sampling/Roots/Logging/Tasks Abschnitte und "Was kommt als Nächstes"
  - [02-Security/README.md](./02-Security/README.md): Hinweis zur Authentifizierungs-Härtung
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): Hinweis zum zustandslosen Transport
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Hinweis zur Sampling-Abschaffung
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Hinweise zu Logging-Abschaffung und Tasks-Erweiterung
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): Hinweis zu zustandslosem/Session-Routing
  - [README.md](./README.md): "Ausblick" Hinweis im Spezifikationsabschnitt und neuer Eintrag `1.1` in der Lehrplan-Modultabelle
  - [study_guide.md](./study_guide.md): zukunftsgerichteter Punkt unter der Core Concepts Übersicht und ein datiertes Nachtragshinweis
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): Hinweis zur `mcp-session-id` Transportmap vor dem zustandslosen Anfragemodell
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): Modulübersicht Hinweis zu Root-Kontexten/Sampling Abschaffungen und der Tasks-Erweiterung
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): Hinweis zur Authentifizierungs-Härtung

## 24. Juni 2026

### Neue Lektion: Verwendung von MCP in der Copilot-App

- [Tooling Abschnitt](./12-tooling/README.md) Tooling Abschnitt hinzugefügt.
- [MCP in Copilot-App](./12-tooling/01-copilot-app/README.md)

## 16. Juni 2026

### MCP Spezifikationsabgleich & Beispielvalidierung

Lehrplan gegen die aktuelle **MCP Specification 2025-11-25** und die neuesten offiziellen SDKs validiert, verbleibende veraltete Spezifikationsverweise korrigiert und bestätigt, dass die Kernbeispiele weiterhin gebaut und ausgeführt werden.

#### Spezifikationsversion-Korrekturen (2025-06-18 / 2025-03-26 → 2025-11-25)

Englische Inhalte aktualisiert, in denen noch behauptet wurde, dass eine ältere Spezifikationsrevision der *aktuelle/neuste* Standard sei, und Links auf die kanonischen `modelcontextprotocol.io` Spezifikationspfade umgeleitet:
- **05-AdvancedTopics/mcp-security/README.md**: Banner "Current Standard", Einführung, Überschrift Kernprinzipien Sicherheit, Überschrift obligatorische Anforderungen, Microsoft Entra ID Abschnitt, Referenzen & Ressourcen Links und abschließender Sicherheitshinweis (8 Referenzen) auf 2025-11-25 aktualisiert
- **05-AdvancedTopics/mcp-transport/README.md**: Spezifikationslink für zusätzliche Ressourcen und Banner "Current Standard" auf 2025-11-25 aktualisiert
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Veralteten `2025-03-26` Sicherheits- und Vertrauenslink durch die aktuelle Seite zu Sicherheit Best Practices 2025-11-25 ersetzt
- **03-GettingStarted/14-sampling/README.md**: Offiziellen Sampling-Dokumentationslink auf 2025-11-25 aktualisiert
- **03-GettingStarted/05-stdio-server/README.md**: Gegenwärtige "aktuelle MCP Spezifikation" Referenz und Spezifikationslink für zusätzliche Ressourcen auf 2025-11-25 aktualisiert (historische SSE-Abschaffungsnotizen zur Genauigkeit belassen)

#### Beispielvalidierung gegen aktuelle SDKs

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` löste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` ohne Typfehler bestanden — bestehende `McpServer`/`StdioServerTransport` APIs bleiben gültig
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validiert in isoliertem `.venv` mit `mcp[cli]` (1.27.2); `py_compile` bestanden und `FastMCP.list_tools()` gab korrekt die `add` und `subtract` Tools zurück
- Bestätigt, dass alle Beispiel-`@modelcontextprotocol/sdk` Versionsbereiche (`>=1.26.0` / `^1.26.0` / `^1.27.0`) sauber auf die aktuelle `1.29.0` auflösen, ohne brechende API-Änderungen

#### Abhängigkeits-Pin-Ausrichtung (Schließen von Versionslücken)

Veraltete SDK-Pins erhöht, sodass jedes Beispiel die aktuelle MCP-Version verfolgt, gemäß der repositoryweiten Konvention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` von `^1.8.0` auf `>=1.26.0` erhöht und die veraltete `"updated for MCP 2025-06-18"` Paketbeschreibung auf `"aligned with MCP Specification 2025-11-25"` aktualisiert
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** und **lab4/code/github_mcp_server/pyproject.toml**: Exakten Pin `mcp==1.23.0` auf `mcp>=1.26.0` erhöht; beide `uv.lock` Dateien neu generiert (`uv lock`), sodass die Lockfiles auf die aktuelle `mcp 1.27.2` auflösen und mit den Manifests synchron bleiben

#### Lehrplan-Lückenanalyse — Abdeckung neuester Spezifikationsfeatures

Verifiziert, dass der Lehrplan bereits alle in MCP 2025-11-25 eingeführten/erweiterten Primitiven abdeckt, somit keine Inhaltslücken bestehen:
- **Sampling**: Lektion 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-Modus)**: Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumentiert in 00-Introduction, 01-CoreConcepts und 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentell, langlaufende Operationen)**: Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features
- **Tool-Anmerkungen** (`readOnlyHint` / `destructiveHint`): Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features

### Sicherheitshärtung & Behebung von Abhängigkeitsverletzlichkeiten

Vollständigen Sicherheitsdurchlauf über alle Abhängigkeitsmanifeste und den Quellcode der Beispiele ausgeführt, anschließend alle gemeldeten npm-Warnungen und einen Fehler auf Codeebene behoben. Nach Behebung meldet `npm audit` **0 Sicherheitslücken** in jedem überprüften Verzeichnis.

#### npm-Abhängigkeitslücken (transitiv) — Gefixt

Alle 15 eingecheckten `package-lock.json` Dateien geprüft. Lücken betrafen nur transitive Abhängigkeiten, die vom MCP Inspector-Entwicklungstool, dem OpenAI-Client und dem MCP SDK eingebracht wurden; alle sind jetzt ohne Bruch von Beispielen behoben:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** und **lab3/code/weather_mcp/inspector**: `@modelcontextprotocol/inspector` von (`0.16.6` / `0.14.1` → `0.22.0`) erhöht, was die gebündelten Warnungen für `ajv`, `brace-expansion`, `diff`, `path-to-regexp` und `ws` beseitigte. npm `overrides` Eintrag hinzugefügt, der das gepatchte `shell-quote@1.8.4` erzwingt, um die verbleibende kritische Warnung durch `concurrently` zu eliminieren; beide Lockfiles neu generiert (jetzt 0 Lücken)
- **03-GettingStarted/samples/typescript**: `npm audit fix` aktualisierte transitives `qs` (moderat) auf gepatchte Version
- **03-GettingStarted/samples/javascript**: `npm audit fix` aktualisierte transitives `hono` (moderat) auf gepatchte Version
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` aktualisierte transitives `form-data` (hoch) auf gepatchte Version
- **03-GettingStarted/11-simple-auth/solution/typescript**: Fehlende `package-lock.json` erzeugt, sodass das Projekt reproduzierbar und überprüfbar ist (0 Lücken)

#### Sicherheitskorrektur auf Codeebene (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `shell=True` aus dem `open_in_vscode` Tool entfernt. Das vorherige `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` erlaubte Shell-Metazeichen in einem Ordnerpfad, die von `cmd.exe` interpretiert werden konnten (Angriffsvektor für Befehlsinjektion). Jetzt wird `Code.exe` direkt mit dem Ordner als Argument gestartet — ohne Shell — was funktional äquivalent und sicher ist

#### Python-Abhängigkeitsprüfung

- Alle Python-Anforderungssätze mit `pip-audit` geprüft. `05-AdvancedTopics` und `03-GettingStarted/samples/python` meldeten **keine bekannten Schwachstellen** (deren `mcp` / `httpx` / `pydantic` / `python-dotenv` Bereiche lösen sich zu aktuellen gepatchten Releases auf)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` meldete für die transitive Abhängigkeit **`werkzeug` 3.1.1** drei `safe_join` Windows Geräte-Namen DoS Warnungen — `CVE-2025-66221`, `CVE-2026-21860` und `CVE-2026-27199` (alle gefixt in 3.1.6). Expliziten Sicherheitspin `werkzeug>=3.1.6` hinzugefügt, sodass das gepatchte Release aufgelöst wird; Überprüft, dass die Einschränkung sauber mit dem `chainlit` / `mcp` / `semantic-kernel` Stack aufgelöst wird

### Produktnamen-Rebranding

Alle Lehrplaninhalte aktualisiert, um Microsofts Produkt-Umbenennung widerzuspiegeln:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord-Community-Link aktualisiert

- **AGENTS.md**: Aktualisierte Discord-Server-Referenz
- **README.md**: Aktualisierte Verweise auf das Technologie-Ökosystem
- **study_guide.md**: Aktualisierte Fallstudien-Referenzen
- **05-AdvancedTopics/README.md**: Aktualisierter Titel und Beschreibung von Modul 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Aktualisierte Abschnittsüberschrift und Beschreibung
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Vollständige Aktualisierung des Modultitels und -inhalts
- **05-AdvancedTopics/mcp-security-entra/README.md**: Aktualisierter Querverweis-Link
- **07-LessonsfromEarlyAdoption/README.md**: Aktualisierte Fallstudien-Referenzen
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Aktualisierte Überschrift von Abschnitt 9, Badges und Fähigkeiten
- **08-BestPractices/README.md**: Aktualisierter Discord-Community-Link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Aktualisierte Discord-Kanal-Referenz
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Aktualisierte Referenz zur Modellbereitstellung
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Aktualisierte Tabelle der KI-Dienste
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Aktualisierte Ressourcenreferenzen

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension für VS Code
- **README.md**: Aktualisierte Hauptcurriculum-Referenzen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Aktualisierter Modultitel, Übersicht und alle Modulüberschriften
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Aktualisierter Titel, Lernziele, Einrichtungsanweisungen und Ressourcen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Aktualisierter Titel, Lernziele, Tabelle der MCP-Hosts und Querverweise
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Aktualisierte Titel, Badges, Voraussetzungen und Ressourcen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Aktualisierte Agent Builder-Verweise und Feedback-Link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Aktualisierte Voraussetzungen und Erweiterungsreferenzen

---

## 11. April 2026

### Neue Lektion, Dokumentationskorrekturen und Abhängigkeitsaktualisierungen

#### Neues Curriculum hinzugefügt

**Modul 05 - Fortgeschrittene Themen**
- **Lektion 5.17: Adversarial Multi-Agent Reasoning mit MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Neue umfassende Anleitung, die das adversariale Debattenmuster für Multi-Agenten-Systeme behandelt
  - Mermaid-Architekturdiagramm: zwei Agenten → gemeinsamer MCP-Server → Debattenprotokoll → Richter → Urteil
  - Gemeinsamer MCP-Werkzeugserver (`web_search` + `run_python`), implementiert in Python und TypeScript
  - Gegensätzliche System-Prompts (FÜR / GEGEN / Richter) mit expliziten Werkzeug-Nutzungsvorgaben
  - Debatten-Orchestrator in Python, TypeScript und C#, der Runden verwaltet und Argumente leitet
  - MCP `ClientSession` Anbindung für den Orchestrator zu realen Werkzeugaufrufen
  - Anwendungsfalldarstellung (Erkennung von Halluzinationen, Bedrohungsmodellierung, API-Design-Review, Faktenprüfung, Technik-Auswahl)
  - Sicherheitsaspekte: Sandbox-Ausführung, Werkzeugaufruf-Validierung, Ratenbegrenzung, Audit-Protokollierung
  - Strukturierte Übung mit drei praktischen Szenarien (Code-Review, Architekturentscheidung, Inhaltsmoderation)

#### Dokumentationskorrekturen

**Modul 03 - Einstieg**
- **05-stdio-server/README.md**: Behobenes unvollständiges TypeScript-Stdio-Server-Beispiel — fehlende Transportinstanziierung (`new StdioServerTransport()`) und `server.connect(transport)`-Aufruf ergänzt, passend zu den Python- und .NET-Beispielen im selben Abschnitt
- **14-sampling/README.md**: Rechtschreibfehler korrigiert — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Curriculum-Updates

**Haupt README.md**
- Neuer Eintrag 5.17 (Adversarial Multi-Agent Reasoning with MCP) in der Curriculum-Tabelle mit Direktlink zur neuen Lektion

**05-AdvancedTopics/README.md**
- Lektion 5.17 als Zeile zur Lektionentabelle hinzugefügt

**study_guide.md**
- Thema Adversarial Multi-Agent Reasoning zur Mindmap und zur Fließtextbeschreibung der Fortgeschrittenen Themen hinzugefügt

#### Code- und Sicherheitskorrekturen

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Sicherheitsfix — Kommandoinjektion**: Ersetzte Shell-Interpolation mit `execSync` durch `execFile` + `promisify` im TypeScript-Tool `run_python`, womit die Angriffsmöglichkeit durch Kommandoinjektion entfällt (vom LLM gesteuerter Code wird jetzt wörtlich als argv-Element übergeben, ohne Shell-Beteiligung)
- **MCP Werkzeug-Schleifenanbindung**: Aktualisierte den Python-Debatten-Orchestrator auf Nutzung des `AsyncAnthropic` Clients (ersetzt blockierenden Sync `Anthropic`), Übergabe einer Live-`ClientSession` direkt an jeden Agenten-Zug, Abruf der Werkzeugdefinitionen über `session.list_tools()` pro Durchlauf und Versand von `tool_use`-Blöcken über `session.call_tool()` in einer Schleife, bis das Modell eine finale Textantwort liefert

#### Abhängigkeitsaktualisierungen

- `hono` auf Version 4.12.12 in mehreren Paketen erhöht (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- `@hono/node-server` von 1.19.11 auf 1.19.13 in TypeScript-Paketen aktualisiert
- `cryptography` von 46.0.5 auf 46.0.7 in Python-Paketen (Labs 3 und 4 von 10-StreamliningAIWorkflows) erhöht
- `lodash` von 4.17.23 auf 4.18.1 im 10-StreamliningAIWorkflows-Inspector erhöht

#### Übersetzungen

- Übersetzungen für 48+ Sprachen mit den neuesten Quelländerungen synchronisiert (i18n-Update)

---

## 5. Februar 2026

### Repository-weite Validierungs- und Navigationsverbesserungen

#### Neues Curriculum hinzugefügt

**Modul 03 - Einstieg**
- **12-mcp-hosts/README.md**: Neue umfassende Anleitung zur Einrichtung von MCP-Hosts
  - Konfigurationsbeispiele für Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-Konfigurationsvorlagen für alle wichtigen Hosts
  - Vergleichstabelle der Transporttypen (stdio, SSE/HTTP, WebSocket)
  - Fehlerbehebung bei häufigen Verbindungsproblemen
  - Sicherheitsempfehlungen für Host-Konfiguration

- **13-mcp-inspector/README.md**: Neue Debugging-Anleitung für MCP Inspector
  - Installationsmethoden (npx, npm global, aus dem Quellcode)
  - Verbindung zu Servern über stdio und HTTP/SSE
  - Testwerkzeuge, Ressourcen und Prompts-Workflows
  - VS Code-Integration mit MCP Inspector
  - Häufige Debugging-Szenarien mit Lösungen

**Modul 04 - Praktische Umsetzung**
- **pagination/README.md**: Neue Anleitung zur Implementierung von Pagination
  - Cursor-basierte Pagination-Muster in Python, TypeScript, Java
  - Client-seitige Pagination-Handhabung
  - Strategien für Cursor-Design (opak vs. strukturiert)
  - Empfehlungen zur Leistungsoptimierung

**Modul 05 - Fortgeschrittene Themen**
- **mcp-protocol-features/README.md**: Neue ausführliche Betrachtung der Protokollfunktionen
  - Umsetzung von Fortschrittsbenachrichtigungen
  - Muster zur Anfragestornierung
  - Ressourcenvorlagen mit URI-Mustern
  - Verwaltung des Server-Lebenszyklus
  - Steuerung der Protokollierungsstufen
  - Fehlerbehandlungsmuster mit JSON-RPC-Codes

#### Navigationskorrekturen (24+ Dateien aktualisiert)

**Hauptmodul-READMEs**
 Jetzt Verlinkung sowohl zur ersten Lektion ALS AUCH zum nächsten Modul

**02-Sicherheits-Unterdateien**
- Alle 5 ergänzenden Sicherheitsdokumente haben nun "Was kommt als Nächstes"-Navigation:

**09-Fallstudien-Dateien**
- Alle Fallstudien-Dateien haben nun sequentielle Navigation:

**10-StreamliningAI Labs**
Hinzugefügt: Abschnitt „Was kommt als Nächstes“ zur Modul-10-Übersicht und Modul 11

#### Code- und Inhaltskorrekturen

**SDK- und Abhängigkeitsupdates**
Leere openai-Version auf `^4.95.0` korrigiert
SDK von `^1.8.0` auf `>=1.26.0` aktualisiert
MCP-Versionspins auf `>=1.26.0` aktualisiert

**Code-Korrekturen**
Ungültiges Modell `gpt-4o-mini` auf `gpt-4.1-mini` korrigiert

**Inhaltskorrekturen**
defekten Link `READMEmd` → `README.md` korrigiert, Header im Curriculum `Module 1-3` → `Module 0-3` korrigiert, Fallunterscheidung im Pfad behoben
beschädigten doppelten Fallstudien-5-Inhalt entfernt

**Verbesserungen der Anfängeranleitung**
Einführung, Lernziele und Voraussetzungen für Anfänger hinzugefügt

#### Curriculum-Updates

**Haupt README.md**
- Einträge 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protokollfunktionen) zur Curriculum-Tabelle hinzugefügt

**Modul-READMEs**
Lektionen 12 und 13 zur Lektionenliste hinzugefügt
Praktische Anleitungen-Sektion mit Pagination-Link hinzugefügt
Lektionen 5.15 (Benutzerdefinierte Transportmittel) und 5.16 (Protokollfunktionen) hinzugefügt

**study_guide.md**
- Aktualisierte Mindmap mit allen neuen Themen: MCP Hosts Setup, MCP Inspector, Pagination Strategien, Protokollfunktionen im Detail

## 28. Januar 2026

### Überprüfung der MCP-Spezifikation 2025-11-25-Konformität

#### Verbesserungen der Kernkonzepte (01-CoreConcepts/)
- **Neue Client-Primitiven - Roots**: Umfassende Dokumentation der Roots-Client-Primitiven hinzugefügt, die es Servern ermöglicht, Dateisystemgrenzen und Zugriffsrechte zu verstehen
- **Werkzeugannotationen**: Dokumentation zu Verhaltensannotationen von Werkzeugen (`readOnlyHint`, `destructiveHint`) für bessere Entscheidungen der Werkzeugausführung ergänzt
- **Werkzeugaufruf in Sampling**: Sampling-Dokumentation aktualisiert, um `tools` und `toolChoice` Parameter für modellgesteuerte Werkzeuginvokation während der Sampling-Anfragen einzubeziehen
- **URL-Modus-Erzeugung**: Dokumentation zur URL-basierten Erzeugung für serverinitiierte externe Webinteraktionen ergänzt
- **Tasks (Experimentell)**: Neuer Abschnitt zur Dokumentation der experimentellen Tasks-Funktion für dauerhafte Ausführungs-Wrapper und verzögerten Ergebnisabruf hinzugefügt
- **Icon-Unterstützung**: Vermerkt, dass Werkzeuge, Ressourcen, Ressourcenvorlagen und Prompts jetzt Icons als zusätzliche Metadaten enthalten können

#### Dokumentationsupdates
- **README.md**: MCP-Spezifikation 2025-11-25 Versionsreferenz und datumsbasierte Versionierungserklärung hinzugefügt
- **study_guide.md**: Curriculum-Karte aktualisiert, um Tasks und Werkzeugannotationen im Abschnitt Kernkonzepte einzubeziehen; Dokument-Zeitstempel aktualisiert

#### Überprüfung der Spezifikationskonformität
- **Protokollversion**: Alle Dokumentationsverweise auf die aktuelle MCP-Spezifikation 2025-11-25 überprüft
- **Architekturausrichtung**: Zwei-Schichten-Architektur (Datenschicht + Transportschicht) Dokumentationsgenauigkeit bestätigt
- **Primitiven-Dokumentation**: Server-Primitiven (Ressourcen, Prompts, Werkzeuge) und Client-Primitiven (Sampling, Elicitation, Logging, Roots) validiert
- **Transportmechanismen**: STDIO- und Streamable HTTP-Transportdokumentation auf Genauigkeit überprüft
- **Sicherheitsanleitungen**: Übereinstimmung mit aktuellen MCP Sicherheits-Best-Practices bestätigt

#### Wichtige dokumentierte MCP 2025-11-25 Funktionen
- **OpenID Connect Discovery**: Auth-Server-Erkennung mittels OIDC
- **OAuth Client-ID-Metadatendokumente**: Empfohlener Mechanismus zur Client-Registrierung
- **JSON Schema 2020-12**: Standard-Dialekt für MCP-Schemadefinitionen
- **SDK-Tiering-System**: Formalisierte Anforderungen für SDK-Funktionsunterstützung und Wartung
- **Governance-Struktur**: Formalisierte Arbeitsgruppen und Interessengruppen in der MCP-Governance

### Wesentliche Aktualisierung der Sicherheitsdokumentation (02-Security/)

#### Integration des MCP Security Summit Workshop (Sherpa)
- **Neue praktische Schulungsressource**: Umfassende Integration mit dem [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in sämtlichen Sicherheitsdokumentationen hinzugefügt
- **Abdeckung der Expeditionsroute**: Dokumentation des kompletten Camp-zu-Camp Fortschritts vom Basislager bis zum Gipfel
- **OWASP-Ausrichtung**: Alle Sicherheitshinweise jetzt auf OWASP MCP Azure Security Guide Risiken abgestimmt

#### OWASP MCP Top 10 Integration
- **Neuer Abschnitt**: Tabelle der OWASP MCP Top 10 Sicherheitsrisiken mit Azure-Minderungen zum Haupt-Security-README hinzugefügt
- **Risikobasierte Dokumentation**: mcp-security-controls-2025.md mit OWASP MCP Risiko-Verweisen für jede Sicherheitsdomäne aktualisiert
- **Referenzarchitektur**: Verlinkung zur OWASP MCP Azure Security Guide Referenzarchitektur und Implementierungsmuster

#### Aktualisierte Sicherheitsdateien
- **README.md**: Sherpa Workshop Übersicht, Expeditionsroutentabelle, OWASP MCP Top 10 Risikoübersicht und praktischer Schulungsabschnitt hinzugefügt
- **mcp-security-controls-2025.md**: Header auf Februar 2026 aktualisiert, OWASP Risiko-Verweise (MCP01-MCP08) hinzugefügt, Versionsinkonsistenz der Spezifikation behoben
- **mcp-security-best-practices-2025.md**: Sherpa- und OWASP-Ressourcenbereich hinzugefügt, Zeitstempel aktualisiert
- **mcp-best-practices.md**: Praktischer Schulungsabschnitt mit Sherpa- und OWASP-Links hinzugefügt
- **azure-content-safety-implementation.md**: OWASP MCP06-Verweis, Sherpa Camp 3-Ausrichtung und zusätzliche Ressourcen-Sektion ergänzt

#### Neue Ressourcen-Links hinzugefügt
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuelle OWASP MCP Risiko-Seiten (MCP01-MCP10)

### Lehrplanweite MCP-Spezifikation 2025-11-25 Ausrichtung

#### Modul 03 - Einstieg
- **SDK-Dokumentation**: Go SDK zur offiziellen SDK-Liste hinzugefügt; alle SDK-Verweise zur Abstimmung auf MCP-Spezifikation 2025-11-25 aktualisiert
- **Transportklarstellung**: STDIO- und HTTP-Streaming-Transportbeschreibungen mit expliziten Spezifikationsverweisen aktualisiert

#### Modul 04 - Praktische Umsetzung
- **SDK-Aktualisierungen**: Go SDK hinzugefügt; SDK-Liste mit Spezifikationsversionsverweis aktualisiert
- **Autorisierungsspezifikation**: MCP-Autorisierungsspezifikationslink auf aktuelle Version 2025-11-25 aktualisiert

#### Modul 05 - Erweiterte Themen
- **Neue Funktionen**: Hinweis zu neuen MCP-Spezifikationsfunktionen 2025-11-25 (Aufgaben, Tool-Anmerkungen, URL-Modus-Erfassung, Wurzeln) hinzugefügt
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa-Workshop-Links zu zusätzlichen Verweisen hinzugefügt

#### Modul 06 - Community-Beiträge
- **SDK-Liste**: Swift- und Rust-SDKs hinzugefügt; Spezifikationslink auf 2025-11-25 aktualisiert
- **Spezifikationsverweis**: MCP-Spezifikationslink auf direkte Spezifikations-URL aktualisiert

#### Modul 07 - Erkenntnisse aus früher Einführung
- **Ressourcenaktualisierungen**: MCP-Spezifikation 2025-11-25 Link und OWASP MCP Top 10 zu zusätzlichen Ressourcen hinzugefügt

#### Modul 08 - Best Practices
- **Spezifikationsversion**: MCP-Spezifikationsverweis auf 2025-11-25 aktualisiert
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa-Workshop zu zusätzlichen Verweisen hinzugefügt

#### Modul 10 - Optimierung von KI-Workflows
- **Abzeichen-Update**: MCP-Versionsbadge von SDK-Version (1.9.3) auf Spezifikationsversion (2025-11-25) geändert
- **Ressourcenlinks**: MCP-Spezifikationslink aktualisiert; OWASP MCP Top 10 hinzugefügt

#### Modul 11 - MCP Server Hands-On Labs
- **Spezifikationsverweis**: MCP-Spezifikationslink auf Version 2025-11-25 aktualisiert
- **Sicherheitsressourcen**: OWASP MCP Top 10 zu offiziellen Ressourcen hinzugefügt

## 18. Dezember 2025

### Sicherheitsdokumentations-Update - MCP Spezifikation 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Versionsupdate der Spezifikation
- **Protokollversions-Update**: Verweis auf neueste MCP Spezifikation 2025-11-25 (veröffentlicht am 25. November 2025) aktualisiert
  - Alle Spezifikationsversionsverweise von 2025-06-18 auf 2025-11-25 aktualisiert
  - Dokumentdatum-Verweise von 18. August 2025 auf 18. Dezember 2025 aktualisiert
  - Alle Spezifikations-URLs auf aktuelle Dokumentation überprüft
- **Inhaltsvalidierung**: Umfassende Validierung der Sicherheits-Best Practices gegen neueste Standards
  - **Microsoft Security Solutions**: Aktuelle Terminologie und Links für Prompt Shields (früher „Jailbreak-Risikodetektion“), Azure Content Safety, Microsoft Entra ID und Azure Key Vault geprüft
  - **OAuth 2.1 Sicherheit**: Übereinstimmung mit neuesten OAuth Sicherheitsbestimmungen bestätigt
  - **OWASP Standards**: OWASP Top 10 für LLMs Referenzen als aktuell bestätigt
  - **Azure Dienste**: Alle Microsoft Azure Dokumentationslinks und Best Practices überprüft
- **Standards-Ausrichtung**: Alle referenzierten Sicherheitsstandards als aktuell bestätigt
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure Sicherheits- und Compliance-Frameworks
- **Implementierungs-Ressourcen**: Alle Implementierungsleitfäden und Ressourcen überprüft
  - Authentifizierungsmuster für Azure API Management
  - Microsoft Entra ID Integrationsleitfäden
  - Azure Key Vault Geheimnisverwaltung
  - DevSecOps-Pipelines und Überwachungslösungen

### Dokumentations-Qualitätssicherung
- **Spezifikationskonformität**: Sicherstellung, dass alle obligatorischen MCP-Sicherheitsanforderungen (MUSS/MUSS NICHT) mit der neuesten Spezifikation übereinstimmen
- **Aktualität der Ressourcen**: Alle externen Links zu Microsoft-Dokumentationen, Sicherheitsstandards und Implementierungsleitfäden überprüft
- **Abdeckung der Best Practices**: Umfassende Abdeckung von Authentifizierung, Autorisierung, KI-spezifischen Bedrohungen, Lieferkettensicherheit und Enterprise-Mustern bestätigt

## 6. Oktober 2025

### Erweiterung des Einstiegsbereichs – Fortgeschrittene Servernutzung & einfache Authentifizierung

#### Fortgeschrittene Servernutzung (03-GettingStarted/10-advanced)
- **Neues Kapitel hinzugefügt**: Umfassender Leitfaden zur fortgeschrittenen MCP-Servernutzung, der sowohl reguläre als auch Low-Level-Serverarchitekturen behandelt
  - **Regulärer vs. Low-Level-Server**: Detaillierter Vergleich und Codebeispiele in Python und TypeScript für beide Ansätze
  - **Handler-basierte Gestaltung**: Erklärung des handlerbasierten Tool-/Ressource-/Prompt-Managements für skalierbare und flexible Serverimplementierungen
  - **Praktische Muster**: Praxisnahe Szenarien, in denen Low-Level-Servermuster für fortgeschrittene Features und Architektur vorteilhaft sind

#### Einfache Authentifizierung (03-GettingStarted/11-simple-auth)
- **Neues Kapitel hinzugefügt**: Schritt-für-Schritt-Anleitung zur Implementierung einer einfachen Authentifizierung in MCP-Servern
  - **Auth-Konzepte**: Klare Erklärung von Authentifizierung vs. Autorisierung und Umgang mit Zugangsdaten
  - **Basis-Auth-Implementierung**: Middleware-basierte Authentifizierungsmuster in Python (Starlette) und TypeScript (Express) mit Codebeispielen
  - **Weiterentwicklung zur erweiterten Sicherheit**: Anleitung zum Einstieg mit einfacher Auth und Weiterentwicklung zu OAuth 2.1 und RBAC, mit Verweisen auf erweiterte Sicherheitsmodule

Diese Ergänzungen bieten praktische, praxisnahe Anleitung zum Aufbau robuster, sicherer und flexibler MCP-Serverimplementierungen und schlagen die Brücke zwischen Grundlagen und fortgeschrittenen Produktionsmustern.

## 29. September 2025

### MCP Server Datenbank-Integrations-Labs – Umfassender Hands-On-Lernpfad

#### 11-MCPServerHandsOnLabs - Neues vollständiges Datenbank-Integrationscurriculum
- **Vollständiger 13-Labs Lernpfad**: Umfassender praxisorientierter Lehrplan zum Aufbau produktionsfertiger MCP-Server mit PostgreSQL-Datenbankintegration hinzugefügt
  - **Praxisanwendung**: Zava Retail Analytics Anwendungsfall mit Unternehmensmustern
  - **Strukturierter Lernfortschritt**:
    - **Labs 00-03: Grundlagen** - Einführung, Kernarchitektur, Sicherheit & Multi-Tenancy, Umgebungseinrichtung
    - **Labs 04-06: Aufbau des MCP Servers** - Datenbankdesign & Schema, MCP-Server-Implementierung, Tool-Entwicklung  
    - **Labs 07-09: Erweiterte Funktionen** - Semantische Suche Integration, Testen & Debugging, VS Code Integration
    - **Labs 10-12: Produktion & Best Practices** - Deployment-Strategien, Überwachung & Beobachtbarkeit, Best Practices & Optimierung
  - **Enterprise-Technologien**: FastMCP Framework, PostgreSQL mit pgvector, Azure OpenAI Einbettungen, Azure Container Apps, Application Insights
  - **Erweiterte Funktionen**: Row Level Security (RLS), semantische Suche, Mandantendatenzugriff, Vektor-Einbettungen, Echtzeit-Überwachung

#### Terminologie-Standardisierung – Modul-zu-Lab-Umstellung
- **Umfassendes Dokumentationsupdate**: Systematische Aktualisierung aller README-Dateien in 11-MCPServerHandsOnLabs auf „Lab“ Terminologie statt „Modul“
  - **Abschnittsüberschriften**: „What This Module Covers“ zu „What This Lab Covers“ in allen 13 Labs geändert
  - **Inhaltsbeschreibung**: „This module provides...“ zu „This lab provides...“ in der gesamten Dokumentation geändert
  - **Lernziele**: „By the end of this module...“ zu „By the end of this lab...“ aktualisiert
  - **Navigationslinks**: Alle „Modul XX:“ Verweise zu „Lab XX:“ in Querverweisen und Navigation geändert
  - **Abschlussverfolgung**: „After completing this module...“ zu „After completing this lab...“ aktualisiert
  - **Technische Verweise erhalten**: Python-Modulverweise in Konfigurationsdateien (z.B. `"module": "mcp_server.main"`) beibehalten

#### Lernleitfaden-Erweiterung (study_guide.md)
- **Visuelle Lehrplanübersicht**: Neuer Abschnitt „11. Database Integration Labs“ mit umfassender Lab-Strukturvisualisierung hinzugefügt
- **Repository-Struktur**: Von zehn auf elf Hauptabschnitte mit detaillierter Beschreibung von 11-MCPServerHandsOnLabs aktualisiert
- **Lernpfad-Anleitung**: Navigationsanweisungen für Abschnitte 00-11 verbessert
- **Technologieabdeckung**: FastMCP, PostgreSQL, Azure-Dienste-Integrationsdetails ergänzt
- **Lernergebnisse**: Fokus auf produktionsfertige Serverentwicklung, Datenbank-Integrationsmuster und Unternehmenssicherheit gesetzt

#### Haupt-README-Struktur-Erweiterung
- **Lab-basierte Terminologie**: Haupt-README.md in 11-MCPServerHandsOnLabs konsequent auf „Lab“-Struktur aktualisiert
- **Lernpfad-Organisation**: Klarer Fortschritt von Grundlagen über fortgeschrittene Implementierung bis Produktion-Deployment
- **Praxisfokus**: Betonung praxisnahen Hands-on-Lernens mit Unternehmensmustern und Technologien

### Verbesserungen der Dokumentationsqualität & Konsistenz
- **Hands-On-Lernansatz**: Praxisorientierten Lab-Ansatz in der gesamten Dokumentation verstärkt
- **Enterprise-Musterfokus**: Produktionsfertige Implementierungen und Unternehmenssicherheitsaspekte hervorgehoben
- **Technologieintegration**: Umfassende Behandlung moderner Azure-Dienste und KI-Integrationsmuster
- **Lernfortschritt**: Klar strukturierter Weg von Grundkonzepten bis zum Produktions-Deployment

## 26. September 2025

### Case Studies Erweiterung - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Fokus auf Ökosystementwicklung
- **README.md**: Große Erweiterung mit umfassender GitHub MCP Registry Fallstudie
  - **GitHub MCP Registry Fallstudie**: Neue umfassende Fallstudie zur Einführung des GitHub MCP Registry im September 2025
    - **Problemanalyse**: Detaillierte Betrachtung fragmentierter MCP-Server-Discovery- und Deployment-Herausforderungen
    - **Lösungsarchitektur**: Zentralisierte Registry-Ansatz von GitHub mit Ein-Klick-VS-Code-Installation
    - **Geschäftliche Auswirkungen**: Messbare Verbesserungen bei Entwickler-Onboarding und Produktivität
    - **Strategischer Wert**: Fokus auf modulare Agent-Deployment und Tool-übergreifende Interoperabilität
    - **Ökosystementwicklung**: Positionierung als grundlegende Plattform für agentenbasierte Integration
  - **Erweiterte Fallstudienstruktur**: Alle sieben Fallstudien mit einheitlichem Format und umfassenden Beschreibungen aktualisiert
    - Azure AI Reiseagenten: Betonung Multi-Agenten-Orchestrierung
    - Azure DevOps Integration: Fokus auf Workflow-Automatisierung
    - Echtzeit-Dokumentenabruf: Python-Konsolenclient-Implementierung
    - Interaktiver Studienplan-Generator: Chainlit konversationsfähige Web-App
    - In-Editor-Dokumentation: VS Code und GitHub Copilot Integration
    - Azure API Management: Unternehmens-API-Integrationsmuster
    - GitHub MCP Registry: Ökosystementwicklung und Community-Plattform
  - **Umfassender Abschluss**: Neugeschriebener Abschnitt zur Zusammenfassung mit sieben Fallstudien, die mehrere MCP-Implementierungsdimensionen abdecken
    - Unternehmensintegration, Multi-Agent-Orchestrierung, Entwicklerproduktivität
    - Ökosystementwicklung, Kategorisierung Bildungsanwendungen
    - Erweiterte Einblicke in Architekturmustern, Implementierungsstrategien und Best Practices
    - Betonung MCP als ausgereiftes, produktionsbereites Protokoll

#### Studienführer-Updates (study_guide.md)
- **Visuelle Lehrplanübersicht**: Mindmap aktualisiert, um GitHub MCP Registry im Abschnitt Case Studies einzuschließen
- **Fallstudienbeschreibung**: Von generischen Beschreibungen zu detaillierter Aufteilung von sieben umfassenden Fallstudien erweitert
- **Repository-Struktur**: Abschnitt 10 zur umfassenden Fallstudienabdeckung mit spezifischen Implementierungsdetails aktualisiert
- **Changelog-Integration**: Eintrag vom 26. September 2025 hinzugefügt, der GitHub MCP Registry Ergänzung und Fallstudienerweiterungen dokumentiert
- **Datum-Updates**: Fußzeilen-Zeitstempel wurde auf die letzte Revision (26. September 2025) aktualisiert

### Verbesserungen der Dokumentationsqualität
- **Konsistenzsteigerung**: Standardisiertes Fallstudienformat und Struktur über alle sieben Beispiele hinweg
- **Umfassende Abdeckung**: Fallstudien decken nun Unternehmens-, Entwicklerproduktivitäts- und Ökosystementwicklungszenarien ab
- **Strategische Positionierung**: Verstärkter Fokus auf MCP als grundlegende Plattform für agentenbasierte Systembereitstellung
- **Ressourceneinbindung**: Zusätzliche Ressourcen um GitHub MCP Registry-Link aktualisiert

## 15. September 2025

### Erweiterung der erweiterten Themen – Benutzerdefinierte Transporte & Kontext-Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Neuer Leitfaden zur fortgeschrittenen Implementierung
- **README.md**: Vollständiger Implementierungsleitfaden für benutzerdefinierte MCP-Transportmechanismen
  - **Azure Event Grid Transport**: Umfassende serverlose, ereignisgesteuerte Transportimplementierung
    - C#, TypeScript und Python Beispiele mit Azure Functions Integration
    - Ereignisgesteuerte Architektur-Muster für skalierbare MCP-Lösungen
    - Webhook-Empfänger und Push-basierte Nachrichtenverarbeitung
  - **Azure Event Hubs Transport**: Hochdurchsatz-Streaming-Transportimplementierung
    - Echtzeit-Streaming-Fähigkeiten für latenzarme Szenarien
    - Partitionierungsstrategien und Checkpoint-Management
    - Nachrichtenbündelung und Leistungsoptimierung
  - **Enterprise-Integrationsmuster**: Produktionsreife Architekturbeispiele
    - Verteilte MCP-Verarbeitung über mehrere Azure Functions
    - Hybride Transportarchitekturen, die mehrere Transporttypen kombinieren
    - Nachrichtenhaltbarkeit, Zuverlässigkeit und Fehlerbehandlungsstrategien
  - **Sicherheit & Überwachung**: Azure Key Vault Integration und Beobachtbarkeitsmuster
    - Authentifizierung mit verwalteter Identität und Prinzip der minimalen Rechtevergabe
    - Application Insights Telemetrie und Leistungsüberwachung
    - Circuit Breaker und Fehlertoleranzmuster
  - **Testframeworks**: Umfassende Teststrategien für benutzerdefinierte Transporte
    - Unit-Tests mit Test-Doubles und Mocking-Frameworks
    - Integrationstests mit Azure Test Containers
    - Leistungs- und Lasttestsüberlegungen

#### Kontext-Engineering (05-AdvancedTopics/mcp-contextengineering/) - Aufkommende KI-Disziplin
- **README.md**: Umfassende Untersuchung des Kontext-Engineerings als aufkommendes Fachgebiet
  - **Kernprinzipien**: Vollständiges Kontext-Sharing, Bewusstsein für Handlungsentscheidungen und Verwaltung des Kontextfensters

  - **MCP-Protokollausrichtung**: Wie das MCP-Design Herausforderungen im Context Engineering adressiert
    - Begrenzungen von Kontextfenstern und progressive Ladeverfahren
    - Relevanzbestimmung und dynamische Kontextabfrage
    - Multimodale Kontextverarbeitung und Sicherheitsaspekte
  - **Implementierungsansätze**: Einzelthread- vs. Multi-Agent-Architekturen
    - Techniken zur Kontext-Segmentierung und Priorisierung
    - Progressive Kontextlade- und Komprimierungsstrategien
    - Geschichtete Kontextansätze und Abrufoptimierung
  - **Messrahmen**: Neue Metriken zur Bewertung der Kontextwirksamkeit
    - Eingabeeffizienz, Leistung, Qualität und Nutzererfahrungsaspekte
    - Experimentelle Ansätze zur Kontextoptimierung
    - Fehleranalyse und Verbesserungsmethoden

#### Aktualisierungen der Kursnavigation (README.md)
- **Verbesserte Modulstruktur**: Aktualisierte Kursübersichtstabelle mit neuen fortgeschrittenen Themen
  - Hinzugefügt Context Engineering (5.14) und Custom Transport (5.15)
  - Einheitliche Formatierung und Navigationslinks in allen Modulen
  - Aktualisierte Beschreibungen zur Abbildung des aktuellen Inhaltsumfangs

### Verbesserungen der Verzeichnisstruktur
- **Namensstandardisierung**: Umbenennung von "mcp transport" in "mcp-transport" zur Konsistenz mit anderen fortgeschrittenen Themenordnern
- **Inhaltsorganisation**: Alle 05-AdvancedTopics-Ordner folgen nun einem konsistenten Namensmuster (mcp-[thema])

### Verbesserungen der Dokumentationsqualität
- **MCP-Spezifikationsanpassung**: Neuer Inhalt verweist auf aktuelle MCP-Spezifikation 2025-06-18
- **Mehrsprachige Beispiele**: Umfassende Codebeispiele in C#, TypeScript und Python
- **Enterprise-Fokus**: Produktionsreife Muster und Azure-Cloud-Integration durchgängig
- **Visuelle Dokumentation**: Mermaid-Diagramme für Architektur- und Ablaufvisualisierung

## 18. August 2025

### Umfassendes Dokumentationsupdate - MCP 2025-06-18 Standards

#### MCP Sicherheit Best Practices (02-Security/) – Komplette Modernisierung
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Vollständige Überarbeitung gemäß MCP-Spezifikation 2025-06-18
  - **Verpflichtende Anforderungen**: Explizite MUST/MUST NOT-Anforderungen aus der offiziellen Spezifikation mit klaren visuellen Indikatoren ergänzt
  - **12 Kernsicherheitspraktiken**: Umstrukturierung von 15-Punkte-Liste zu umfassenden Sicherheitsdomänen
    - Token-Sicherheit & Authentifizierung mit Integration externer Identitätsanbieter
    - Sitzungsmanagement & Transportsicherheit mit kryptografischen Anforderungen
    - KI-spezifischer Bedrohungsschutz mit Microsoft Prompt Shields-Integration
    - Zugriffskontrolle & Berechtigungen mit Prinzip der minimalen Rechtevergabe
    - Inhaltsicherheit & Überwachung mit Azure Content Safety-Integration
    - Lieferkettensicherheit mit umfassender Komponentenüberprüfung
    - OAuth-Sicherheit & Vermeidung von Confused Deputy mit PKCE-Implementierung
    - Vorfallreaktion & Wiederherstellung mit automatisierten Funktionen
    - Compliance & Governance mit regulatorischer Übereinstimmung
    - Erweiterte Sicherheitskontrollen mit Zero-Trust-Architektur
    - Integration des Microsoft-Sicherheitsökosystems mit umfassenden Lösungen
    - Kontinuierliche Sicherheitsevolution mit adaptiven Praktiken
  - **Microsoft-Sicherheitslösungen**: Verbesserte Integrationsanleitungen für Prompt Shields, Azure Content Safety, Entra ID und GitHub Advanced Security
  - **Implementierungsressourcen**: Kategorisierte umfassende Linksammlung nach offizieller MCP-Dokumentation, Microsoft-Sicherheitslösungen, Sicherheitsstandards und Implementierungsanleitungen

#### Erweiterte Sicherheitskontrollen (02-Security/) – Unternehmensimplementierung
- **MCP-SECURITY-CONTROLS-2025.md**: Komplettes Überarbeitung mit Enterprise-Sicherheitsrahmenwerk
  - **9 Umfassende Sicherheitsdomänen**: Erweiterung von Basiskontrollen zu detailliertem Unternehmensrahmen
    - Erweiterte Authentifizierung & Autorisierung mit Microsoft Entra ID-Integration
    - Token-Sicherheit & Anti-Passthrough-Kontrollen mit umfassender Validierung
    - Sitzungs-Sicherheitskontrollen mit Hijacking-Prävention
    - KI-spezifische Sicherheitskontrollen mit Prompt Injection und Tool Poisoning-Prävention
    - Vermeidung von Confused Deputy-Angriffen mit OAuth-Proxy-Sicherheit
    - Tools-Ausführungssicherheit mit Sandboxing und Isolation
    - Lieferkettensicherheitskontrollen mit Abhängigkeitsprüfung
    - Überwachungs- & Erkennungskontrollen mit SIEM-Integration
    - Vorfallreaktion & Wiederherstellung mit automatisierten Funktionen
  - **Implementierungsbeispiele**: Detaillierte YAML-Konfigurationsblöcke und Codebeispiele hinzugefügt
  - **Microsoft-Lösungsintegration**: Umfassende Abdeckung von Azure-Sicherheitsdiensten, GitHub Advanced Security und Unternehmens-Identitätsmanagement

#### Fortgeschrittene Themen Sicherheit (05-AdvancedTopics/mcp-security/) – Produktionsreife Implementierung
- **README.md**: Vollständige Überarbeitung für Unternehmenssicherheit
  - **Aktuelle Spezifikationsanpassung**: Aktualisiert auf MCP Spezifikation 2025-06-18 mit verpflichtenden Sicherheitsanforderungen
  - **Erweiterte Authentifizierung**: Microsoft Entra ID-Integration mit umfassenden .NET- und Java Spring Security-Beispielen
  - **KI-Sicherheitsintegration**: Microsoft Prompt Shields und Azure Content Safety-Implementierung mit detaillierten Python-Beispielen
  - **Erweiterte Bedrohungsminderung**: Umfassende Implementierungsbeispiele für
    - Vermeidung von Confused Deputy-Angriffen mit PKCE und Benutzerzustimmungsvalidierung
    - Token-Passthrough-Vermeidung mit Audience-Validierung und sicherem Token-Management
    - Sitzungs-Hijacking-Prävention mit kryptografischer Bindung und Verhaltensanalyse
  - **Unternehmenssicherheitsintegration**: Azure Application Insights-Monitoring, Bedrohungserkennungs-Pipelines und Lieferkettensicherheit
  - **Implementierungscheckliste**: Klare Unterscheidung verpflichtender vs. empfohlener Sicherheitskontrollen mit Vorteilen des Microsoft-Sicherheitsökosystems

### Dokumentationsqualität & Standardanpassung
- **Spezifikationsverweise**: Alle Verweise auf aktuelle MCP Spezifikation 2025-06-18 aktualisiert
- **Microsoft-Sicherheitsökosystem**: Verbesserte Integrationsanleitungen in allen Sicherheitsdokumentationen
- **Praktische Implementierung**: Detaillierte Codebeispiele in .NET, Java und Python mit Enterprise-Mustern hinzugefügt
- **Ressourcenorganisation**: Umfassende Kategorisierung offizieller Dokumentationen, Sicherheitsstandards und Implementierungsanleitungen
- **Visuelle Indikatoren**: Klare Markierung verpflichtender Anforderungen vs. empfohlener Praktiken


#### Kernkonzepte (01-CoreConcepts/) – Komplette Modernisierung
- **Protokollversionsupdate**: Aktualisiert mit Verweis auf aktuelle MCP Spezifikation 2025-06-18 mit datumsbasierter Versionierung (JJJJ-MM-TT-Format)
- **Architekturverfeinerung**: Verbesserte Beschreibung von Hosts, Clients und Servern entsprechend aktueller MCP-Architekturmuster
  - Hosts jetzt klar definiert als KI-Anwendungen zur Koordination mehrerer MCP-Client-Verbindungen
  - Clients als Protokollverbindungen mit Eins-zu-eins-Serverbeziehungen beschrieben
  - Server erweitert mit lokalen vs. Remote-Bereitstellungsszenarien
- **Primitive Umstrukturierung**: Vollständige Überarbeitung der Server- und Client-Primitives
  - Server-Primitives: Ressourcen (Datenquellen), Prompts (Vorlagen), Tools (ausführbare Funktionen) mit detaillierten Erklärungen und Beispielen
  - Client-Primitives: Sampling (LLM-Completion), Elicitation (Benutzereingabe), Logging (Debugging/Monitoring)
  - Aktualisiert mit aktuellen Discovery- (`*/list`), Retrieval- (`*/get`) und Ausführungs- (`*/call`) Methodentypen
- **Protokollarchitektur**: Einführung eines zweischichtigen Architekturmodells
  - Datenschicht: JSON-RPC 2.0-Grundlage mit Lifecycle-Management und Primitives
  - Transportschicht: STDIO (lokal) und Streambarer HTTP mit SSE (remote) Transportmechanismen
- **Sicherheitsrahmenwerk**: Umfassende Sicherheitsprinzipien inklusive expliziter Nutzereinwilligungen, Datenschutz, Tool-Ausführungssicherheit und Transportschichtsicherheit
- **Kommunikationsmuster**: Aktualisierte Protokollnachrichten mit Initialisierungs-, Entdeckungs-, Ausführungs- und Benachrichtigungsabläufen
- **Codebeispiele**: Erneuerte mehrsprachige Beispiele (.NET, Java, Python, JavaScript) entsprechend aktuellen MCP SDK-Mustern

#### Sicherheit (02-Security/) – Umfassende Sicherheitsüberarbeitung  
- **Standardausrichtung**: Vollständige Übereinstimmung mit Sicherheitsanforderungen der MCP Spezifikation 2025-06-18
- **Authentifizierungsevolution**: Dokumentation der Entwicklung von benutzerdefinierten OAuth-Servern zur Delegation an externe Identitätsanbieter (Microsoft Entra ID)
- **KI-spezifische Bedrohungsanalyse**: Verbesserte Abdeckung moderner KI-Angriffsvektoren
  - Detaillierte Prompt-Injection-Angriffsszenarien mit Praxisbeispielen
  - Mechanismen des Tool-Poisoning und "Rug Pull"-Angriffsmuster
  - Kontextfenster-Vergiftung und Modellverwirrungsangriffe
- **Microsoft KI-Sicherheitslösungen**: Umfassende Abdeckung des Microsoft-Sicherheitsökosystems
  - KI Prompt Shields mit fortschrittlicher Erkennung, Spotlights und Trenntechniken
  - Azure Content Safety-Integrationsmuster
  - GitHub Advanced Security zum Schutz der Lieferkette
- **Erweiterte Bedrohungsminderung**: Detaillierte Sicherheitskontrollen für
  - Sitzungshijacking mit MCP-spezifischen Angriffsszenarien und kryptografischen Sitzungs-ID-Anforderungen
  - Probleme mit Confused Deputy in MCP-Proxy-Szenarien mit expliziten Zustimmungsanforderungen
  - Token-Passthrough-Schwachstellen mit verpflichtenden Validierungskontrollen
- **Lieferkettensicherheit**: Erweiterte KI-Lieferkettendeckung einschl. Foundation Models, Embeddings-Dienste, Kontextanbieter und Drittanbieter-APIs
- **Foundation-Sicherheit**: Verbesserte Integration mit Unternehmenssicherheitsmustern einschließlich Zero-Trust-Architektur und Microsoft-Sicherheitsökosystem
- **Ressourcenorganisation**: Kategorisierte umfassende Ressourcensammlung nach Typ (Offizielle Dokumente, Standards, Forschung, Microsoft-Lösungen, Implementierungsanleitungen)

### Verbesserungen der Dokumentationsqualität
- **Strukturierte Lernziele**: Verbesserte Lernziele mit spezifischen, umsetzbaren Ergebnissen
- **Querverweise**: Links zwischen verwandten Sicherheits- und Kernkonzeptthemen ergänzt
- **Aktuelle Informationen**: Alle Datumsangaben und Spezifikationsverweise auf aktuelle Standards aktualisiert
- **Implementierungsanleitungen**: Spezifische und praxisnahe Implementierungsrichtlinien in beiden Abschnitten ergänzt

## 16. Juli 2025

### README- und Navigationsverbesserungen
- Komplette Neugestaltung der Kursnavigation in README.md
- Ersetzung der `<details>`-Tags durch zugänglicheres tabellenbasiertes Format
- Erstellung alternativer Layoutoptionen im neuen Ordner "alternative_layouts"
- Hinzugefügt Beispiele für kartenbasierte, Registerkarten- und Akkordeon-Navigation
- Aktualisierung des Repository-Strukturabschnitts zur Einbeziehung aller neuesten Dateien
- Verbessertes „Wie man diesen Kurs verwendet“ mit klaren Empfehlungen
- Aktualisierte MCP-Spezifikationslinks mit korrekten URLs
- Hinzugefügt Abschnitt Context Engineering (5.14) zur Kursstruktur

### Aktualisierungen des Studienleitfadens
- Vollständige Überarbeitung des Studienleitfadens zur Angleichung an aktuelle Repository-Struktur
- Neue Abschnitte für MCP-Clients und Tools sowie beliebte MCP-Server hinzugefügt
- Aktualisierte visuelle Kursübersicht zur genauen Abbildung aller Themen
- Verbesserte Beschreibungen der Fortgeschrittenenthemen zur Abdeckung aller Spezialgebiete
- Aktualisierte Abschnitt Fallstudien zur Darstellung tatsächlicher Beispiele
- Dieser umfassende Änderungsverlauf hinzugefügt

### Community-Beiträge (06-CommunityContributions/)
- Detaillierte Informationen zu MCP-Servern für Bildgenerierung hinzugefügt
- Umfassender Abschnitt zur Nutzung von Claude in VSCode hinzugefügt
- Cline-Terminal-Client-Setup und Nutzungshinweise hinzugefügt
- MCP-Client-Abschnitt mit allen beliebten Client-Optionen aktualisiert
- Erweiterte Beitragsbeispiele mit genaueren Codebeispielen

### Fortgeschrittene Themen (05-AdvancedTopics/)
- Alle spezialisierten Themenordner konsistent benannt organisiert
- Context Engineering Materialien und Beispiele hinzugefügt
- Dokumentation zur Foundry-Agentenintegration hinzugefügt
- Verbesserte Dokumentation zur Entra ID-Sicherheitsintegration

## 11. Juni 2025

### Erste Erstellung
- Veröffentlichung der ersten Version des MCP für Anfänger-Kurses
- Grundstruktur aller 10 Hauptabschnitte erstellt
- Visual Curriculum Map zur Navigation implementiert
- Erste Beispielprojekte in mehreren Programmiersprachen hinzugefügt

### Erste Schritte (03-GettingStarted/)
- Erste Server-Implementierungsbeispiele erstellt
- Anleitung zur Client-Entwicklung hinzugefügt
- Integrierte LLM-Client-Anweisungen beigefügt
- Dokumentation zur VS Code-Integration hinzugefügt
- Server-Sent Events (SSE) Server-Beispiele implementiert

### Kernkonzepte (01-CoreConcepts/)
- Detaillierte Erklärung der Client-Server-Architektur ergänzt
- Dokumentation zu wichtigen Protokollkomponenten erstellt
- Dokumentierte Messaging-Muster in MCP

## 23. Mai 2025

### Repository-Struktur
- Initialisierung des Repositories mit grundlegender Ordnerstruktur
- README-Dateien für jede Hauptsektion erstellt
- Übersetzungsinfrastruktur eingerichtet
- Bildmaterialien und Diagramme hinzugefügt

### Dokumentation
- Erste README.md mit Kursübersicht erstellt
- CODE_OF_CONDUCT.md und SECURITY.md hinzugefügt
- SUPPORT.md mit Hilfeführung eingerichtet
- Vorläufige Studienleitfaden-Struktur erstellt

## 15. April 2025

### Planung und Rahmenwerk
- Erste Planungen für MCP für Anfänger-Kurs
- Lernziele und Zielgruppe definiert
- Zehn-Abschnitt-Struktur des Kurses skizziert
- Konzeptueller Rahmen für Beispiele und Fallstudien entwickelt
- Erste Prototypenbeispiele für Hauptkonzepte erstellt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->