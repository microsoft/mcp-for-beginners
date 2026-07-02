# Änderungsprotokoll: MCP für Anfänger Curriculum

Dieses Dokument dient als Aufzeichnung aller bedeutenden Änderungen am Model Context Protocol (MCP) für Anfänger Curriculum. Änderungen werden in umgekehrter chronologischer Reihenfolge dokumentiert (neueste Änderungen zuerst).

## 2. Juli 2026

### Neue Lektion: Der 2026-07-28 MCP Spezifikations-Release-Kandidat

Aufnahme der bald erscheinenden `2026-07-28` MCP Spezifikations-Release-Kandidaten (angekündigt am 21. Mai 2026; Endgültige Veröffentlichung geplant für den 28. Juli 2026), zusammengefasst aus dem [offiziellen Ankündigungs-Blogpost](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Die Basis des Curriculums bleibt bis zum Erscheinen der neuen Version **MCP Spezifikation 2025-11-25**, daher wird dies als zukunftsgerichtete Orientierung und nicht als Umschreibung bestehender Lektionen präsentiert.

- **Neu**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — eine vollständige Lektion, die den zustandslosen Protokollkern abdeckt (Entfernung des `initialize` Handshakes und des `Mcp-Session-Id`), die neuen `Mcp-Method`/`Mcp-Name` Routing-Header, `ttlMs`/`cacheScope` Caching-Metadaten, W3C Trace Context in `_meta`, das formale Erweiterungsframework (MCP Apps und die neue Tasks-Erweiterung), sechs autorisierungsverstärkende SEPs, die Ausphasung von Roots/Sampling/Logging sowie den Umstieg auf vollständig JSON Schema 2020-12 für Tool-Schemata.
- **Aktualisiert** mit zukunftsgerichteten Hinweisen mit Verlinkung zur neuen Lektion:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): Protokollversionshinweis, Abschnitte Sampling/Roots/Logging/Tasks und "Was kommt als Nächstes"
  - [02-Security/README.md](./02-Security/README.md): Hinweis zur Autorisierungsverstärkung
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): Hinweis zum zustandslosen Transport
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Hinweis zur Ausphasung von Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Hinweis zur Ausphasung von Logging und zur Tasks-Erweiterung
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): Hinweis zu zustandslosem/session-basiertem Routing
  - [README.md](./README.md): "Ausblick" Hinweis im Spezifikationsabschnitt und neuer Eintrag `1.1` in der Curriculum-Modultabelle
  - [study_guide.md](./study_guide.md): zukunftsgerichtete Aufzählung unter der Core Concepts Übersicht und eine datierte Nachtragsnotiz
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): Hinweis zur `mcp-session-id` Transportzuordnung vor dem zustandslosen Anfrage-Modell
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): Modulübersicht mit Hinweisen zu Root Contexts/Sampling-Ausphasungen und der Tasks-Erweiterung
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): Hinweis zur Autorisierungsverstärkung

## 24. Juni 2026

### Neue Lektion: Verwendung von MCP in der Copilot-App

- [Tooling Abschnitt](./12-tooling/README.md) Tooling-Abschnitt hinzugefügt.
- [MCP in der Copilot-App](./12-tooling/01-copilot-app/README.md)

## 16. Juni 2026

### MCP Spezifikationsanpassung & Musterüberprüfung

Das Curriculum wurde gegen die aktuelle **MCP Spezifikation 2025-11-25** und die neuesten offiziellen SDKs validiert, anschließend alle veralteten Spezifikationsreferenzen korrigiert und bestätigt, dass die Kernbeispiele weiterhin gebaut und ausgeführt werden können.

#### Korrekturen der Spezifikationsversion (2025-06-18 / 2025-03-26 → 2025-11-25)

Englische Inhalte, die noch eine ältere Spezifikationsrevision als *aktuelle/neuste* Norm angaben, wurden aktualisiert, ebenso wurden Links zu den kanonischen `modelcontextprotocol.io` Spezifikationspfaden angepasst:
- **05-AdvancedTopics/mcp-security/README.md**: Aktualisierung des Banners "Current Standard", Einleitung, Überschrift Kernsicherheitsprinzipien, Überschrift obligatorische Anforderungen, Microsoft Entra ID Abschnitt, Referenzen & Ressourcen-Links sowie Abschlusshinweis zur Sicherheit (8 Verweise) auf 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Aktualisierung des Links zu Zusätzlichen Ressourcen und Banner "Current Standard" auf 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Ersetzung des veralteten `2025-03-26` security-and-trust Links durch die aktuelle 2025-11-25 Seite zu Sicherheitsbest Practices
- **03-GettingStarted/14-sampling/README.md**: Aktualisierung des offiziellen Sampling-Dokumentationslinks zu 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Aktualisierung der Gegenwartsform "aktuelle MCP Spezifikation" Referenz und des Links zu Zusätzlichen Ressourcen auf 2025-11-25 (historische SSE-Ausphasungsnotizen aus Genauigkeitsgründen unverändert)

#### Validierung der Beispiele gegen aktuelle SDKs

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` löste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` erfolgreich ohne Typfehler — bestehende `McpServer`/`StdioServerTransport` APIs bleiben gültig
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validiert in isoliertem `.venv` mit `mcp[cli]` (1.27.2); `py_compile` erfolgreich, `FastMCP.list_tools()` gab korrekt die Tools `add` und `subtract` zurück
- Bestätigung, dass alle Beispielversionbereiche von `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) problemlos aktuell auf `1.29.0` aufgelöst werden ohne API-Breaks

#### Dependency Pin Angleichung (Schließung von Versionslücken)

Veraltete SDK Versionen erhöht, sodass jedes Beispiel der aktuellen MCP Version folgt und dem repoweiten Konventionsschema entspricht:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` von `^1.8.0` → `>=1.26.0` angehoben und veraltete Paketbeschreibung `"updated for MCP 2025-06-18"` zu `"aligned with MCP Specification 2025-11-25"` aktualisiert
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** und **lab4/code/github_mcp_server/pyproject.toml**: Genaue Pinnings `mcp==1.23.0` → `mcp>=1.26.0` angehoben; beide `uv.lock` Dateien neu generiert (`uv lock`), sodass Lockfiles auf aktuelle `mcp 1.27.2` weisen und mit Manifesten synchron bleiben

#### Curriculum-Lückenanalyse — Neue Spezifikationsfeatures abgedeckt

Überprüfung zeigt, dass alle im MCP 2025-11-25 eingeführten/ausgebauten Primitiven bereits im Curriculum behandelt werden, also keine Inhaltslücken bestehen:
- **Sampling**: Lektion 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-Modus)**: Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumentiert in 00-Introduction, 01-CoreConcepts und 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentell, langlaufende Operationen)**: Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features
- **Tool-Anmerkungen** (`readOnlyHint` / `destructiveHint`): Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features

### Sicherheitsverstärkung & Behebung von Abhängigkeits-Schwachstellen

Eine vollständige Sicherheitsüberprüfung aller Abhängigkeitsmanifeste und des Beispielquellcodes wurde durchgeführt, alle erkannten npm Advisories und ein Code-Level-Befund wurden behoben. Anschließend meldet `npm audit` in allen geprüften Verzeichnissen **0 Schwachstellen**.

#### npm Abhängigkeits-Schwachstellen (transitiv) — Behandelt

Alle 15 eingescheckten `package-lock.json` Dateien auditiert. Schwachstellen beschränkten sich auf transitive Dependencies, die durch das MCP Inspector Dev-Tool, den OpenAI Client und das MCP SDK eingebunden wurden; alle nun ohne Beeinträchtigung der Beispiele behoben:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** und **lab3/code/weather_mcp/inspector**: `@modelcontextprotocol/inspector` aktualisiert (`0.16.6` / `0.14.1` → `0.22.0`), damit wurden die gebündelten Advisories für `ajv`, `brace-expansion`, `diff`, `path-to-regexp` und `ws` entfernt. Ein npm `overrides` Eintrag wurde hinzugefügt, der die gepatchte `shell-quote@1.8.4` erzwingt und den verbliebenen kritischen Advisory von `concurrently` beseitigt; beide Lockfiles neu generiert (jetzt 0 Schwachstellen)
- **03-GettingStarted/samples/typescript**: `npm audit fix` aktualisierte die transitive `qs` (mittel) auf eine gepatchte Version
- **03-GettingStarted/samples/javascript**: `npm audit fix` aktualisierte die transitive `hono` (mittel) auf eine gepatchte Version
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` aktualisierte die transitive `form-data` (hoch) auf eine gepatchte Version
- **03-GettingStarted/11-simple-auth/solution/typescript**: Fehlende `package-lock.json` generiert, nun reproduzierbar und prüfbar (0 Schwachstellen)

#### Code-Level Sicherheitsfix (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Entfernte `shell=True` aus dem `open_in_vscode` Tool. Das vorherige `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` erlaubte Shell-Metazeichen im Ordnerpfad, die von `cmd.exe` interpretiert wurden (Command-Injection Vektor). Jetzt wird das aufgelöste `Code.exe` direkt mit dem Ordner als Argument gestartet — ohne Shell — funktional äquivalent und sicher

#### Python-Abhängigkeits-Audit

- Alle Python-Anforderungssets mit `pip-audit` geprüft. `05-AdvancedTopics` und `03-GettingStarted/samples/python` meldeten **keine bekannten Schwachstellen** (deren `mcp` / `httpx` / `pydantic` / `python-dotenv` Bereiche lösen auf aktuelle gepatchte Releases auf)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` meldete die transitive Abhängigkeit **`werkzeug` 3.1.1** mit drei `safe_join` Windows-Gerätenamen DoS Advisories — `CVE-2025-66221`, `CVE-2026-21860`, und `CVE-2026-27199` (alle in 3.1.6 behoben). Ein expliziter Sicherheitspin `werkzeug>=3.1.6` wurde hinzugefügt, um die gepatchte Version aufzulösen; es wurde überprüft, dass die Einschränkung sauber mit `chainlit` / `mcp` / `semantic-kernel` Stack aufgelöst wird

### Produkt-Umbenennung

Alle Curriculum-Inhalte wurden aktualisiert, um die Produkt-Umbenennung von Microsoft widerzuspiegeln:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord Community Link aktualisiert
- **AGENTS.md**: Discord Server Verweis aktualisiert
- **README.md**: Referenzen zum Technologie-Ökosystem aktualisiert
- **study_guide.md**: Fallstudienverweise aktualisiert
- **05-AdvancedTopics/README.md**: Modul 5.13 Titel und Beschreibung aktualisiert
- **05-AdvancedTopics/mcp-integration/README.md**: Abschnittsüberschrift und Beschreibung aktualisiert
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Kompletter Modul-Titel und Inhaltsaktualisierung
- **05-AdvancedTopics/mcp-security-entra/README.md**: Querverweis Link aktualisiert
- **07-LessonsfromEarlyAdoption/README.md**: Fallstudienverweise aktualisiert
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Abschnitt 9 Überschrift, Badges und Fähigkeiten aktualisiert
- **08-BestPractices/README.md**: Discord Community Link aktualisiert
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Discord Channel Verweis aktualisiert
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Modell-Deployment Verweis aktualisiert
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: AI Services Tabelle aktualisiert
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Ressourcenverweise aktualisiert

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension für VS Code
- **README.md**: Aktualisierte Hauptcurriculum-Verweise  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Aktualisierter Modultitel, Übersicht und alle Modulüberschriften  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Aktualisierter Titel, Lernziele, Einrichtungshinweise und Ressourcen  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Aktualisierter Titel, Lernziele, MCP-Hosts-Tabelle und Querverweise  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Aktualisierter Titel, Abzeichen, Voraussetzungen und Ressourcen  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Aktualisierte Agent Builder-Verweise und Feedback-Link  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Aktualisierte Voraussetzungen und Verweise auf Erweiterungen  

---

## 11. April 2026

### Neue Lektion, Dokumentationskorrekturen und Abhängigkeits-Updates

#### Neue Curriculum-Inhalte Hinzugefügt

**Modul 05 - Fortgeschrittene Themen**  
- **Lektion 5.17: Adversariales Multi-Agenten-Denken mit MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Neuer umfassender Leitfaden zum adversarial debate Muster für Multi-Agenten-Systeme  
  - Mermaid-Architekturdiagramm: zwei Agenten → gemeinsamer MCP-Server → Debattenprotokoll → Richter → Urteil  
  - Gemeinsamer MCP-Tool-Server (`web_search` + `run_python`), implementiert in Python und TypeScript  
  - Gegensätzliche System-Prompts (FÜR / GEGEN / Richter) mit expliziten Werkzeug-Nutzungsanforderungen  
  - Debatten-Orchestrator in Python, TypeScript und C#, verwaltet Runden und leitet Argumente weiter  
  - MCP `ClientSession`-Vernetzung für den Orchestrator zu echten Werkzeugaufrufen  
  - Anwendungsfall-Tabelle (Halluzinations-Erkennung, Bedrohungsmodellierung, API-Design-Review, Faktenprüfung, Technologiewahl)  
  - Sicherheitsaspekte: Sandbox-Ausführung, Werkzeugaufrufvalidierung, Rate-Limiting, Auditing-Logging  
  - Strukturierte Übung mit drei praktischen Szenarien (Code-Review, Architekturentscheidung, Inhaltsmoderation)  

#### Dokumentationskorrekturen

**Modul 03 - Einstieg**  
- **05-stdio-server/README.md**: Behebung unvollständigen TypeScript stdio Server-Beispiels — Hinzufügen der fehlenden Transport-Instanziierung (`new StdioServerTransport()`) und `server.connect(transport)` Aufruf entsprechend der Python- und .NET-Beispiele im gleichen Abschnitt  
- **14-sampling/README.md**: Tippfehlerbehebung — korrigiert `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`  

#### Curriculum-Aktualisierungen

**Haupt-README.md**  
- Eintrag 5.17 (Adversariales Multi-Agenten-Denken mit MCP) zur Curriculum-Tabelle mit direktem Link zur neuen Lektion hinzugefügt  

**05-AdvancedTopics/README.md**  
- Zeile für Lektion 5.17 in die Lektionentabelle aufgenommen  

**study_guide.md**  
- Adversariales Multi-Agenten-Thema zur Mind-Map und Fließtextbeschreibung der Fortgeschrittenen Themen ergänzt  

#### Code- und Sicherheitskorrekturen

**Modul 05 - Adversariale Agenten (`mcp-adversarial-agents`)**  
- **Sicherheitsfix — Kommandoinjektion**: Ersetzung der shell-Interpolation `execSync` durch `execFile` + `promisify` im TypeScript `run_python` Werkzeug, wodurch die Angriffsfläche für Kommandoinjektionen entfällt (LLM-gesteuerter Code wird nun als literal argv-Element ohne Shell-Verarbeitung übergeben)  
- **MCP-Werkzeugschleifen-Vernetzung**: Aktualisierung des Python Debatten-Orchestrators zur Nutzung des asynchronen `AsyncAnthropic` Clients (ersetzt blockierenden synchronen `Anthropic`), Übergabe einer lebenden `ClientSession` direkt an jede Agentenrunde, Abruf der Werkzeugdefinitionen via `session.list_tools()` in jeder Runde und Ausführen von `tool_use` Blöcken per `session.call_tool()` in einer Schleife bis zur finalen Textantwort des Modells  

#### Abhängigkeitsaktualisierungen

- `hono` auf Version 4.12.12 in mehreren Paketen erhöht (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- `@hono/node-server` von 1.19.11 auf 1.19.13 in TypeScript-Paketen aktualisiert  
- `cryptography` von 46.0.5 auf 46.0.7 in Python-Paketen (Labs 3 und 4 von 10-StreamliningAIWorkflows) aktualisiert  
- `lodash` von 4.17.23 auf 4.18.1 im 10-StreamliningAIWorkflows Inspector aktualisiert  

#### Übersetzungen

- Übersetzungen für über 48 Sprachen mit den neuesten Quelländerungen synchronisiert (i18n-Update)  

---

## 5. Februar 2026

### Repository-weite Validierung und Verbesserungen der Navigation

#### Neue Curriculum-Inhalte Hinzugefügt

**Modul 03 - Einstieg**  
- **12-mcp-hosts/README.md**: Neuer umfassender Leitfaden zum Einrichten von MCP-Hosts  
  - Konfigurationsbeispiele für Claude Desktop, VS Code, Cursor, Cline, Windsurf  
  - JSON-Konfigurationsvorlagen für alle großen Hosts  
  - Vergleichstabelle der Transporttypen (stdio, SSE/HTTP, WebSocket)  
  - Fehlerbehebung bei häufigen Verbindungsproblemen  
  - Sicherheitsbest Practices für Host-Konfiguration  

- **13-mcp-inspector/README.md**: Neuer Debugging-Leitfaden für MCP Inspector  
  - Installationsmethoden (npx, globales npm, aus Quellcode)  
  - Verbindung zu Servern via stdio und HTTP/SSE  
  - Testwerkzeuge, Ressourcen und Prompts Workflows  
  - VS Code Integration mit MCP Inspector  
  - Häufige Debugging-Szenarien mit Lösungen  

**Modul 04 - Praktische Umsetzung**  
- **pagination/README.md**: Neuer Leitfaden zur Paginierungs-Implementierung  
  - Cursor-basierte Paginierungsmuster in Python, TypeScript, Java  
  - Client-seitige Paginierungsbehandlung  
  - Cursor-Design-Strategien (opaque vs. structured)  
  - Empfehlungen zur Performance-Optimierung  

**Modul 05 - Fortgeschrittene Themen**  
- **mcp-protocol-features/README.md**: Neue detaillierte Beschreibung von Protokoll-Features  
  - Umsetzung von Fortschrittsbenachrichtigungen  
  - Muster für Anforderungsabbrüche  
  - Ressourcenvorlagen mit URI-Mustern  
  - Server-Lifecycle-Management  
  - Steuerung von Logging-Leveln  
  - Fehlerbehandlungsmuster mit JSON-RPC-Codes  

#### Navigationskorrekturen (über 24 Dateien aktualisiert)

**Hauptmodul-READMEs**  
- Verlinken nun sowohl zur ersten Lektion als auch zum nächsten Modul  

**02-Security Unterdateien**  
- Alle 5 ergänzenden Sicherheitsdokumente besitzen jetzt eine „Was folgt“-Navigation  

**09-CaseStudy Dateien**  
- Alle Fallstudien-Dateien haben jetzt sequentielle Navigation  

**10-StreamliningAI Labs**  
- „Was folgt“-Abschnitt zu Modul 10 Übersicht und Modul 11 hinzugefügt  

#### Code- und Inhaltskorrekturen

**SDK- und Abhängigkeitsupdates**  
- Leere openai-Version auf `^4.95.0` gesetzt  
- SDK von `^1.8.0` auf `>=1.26.0` aktualisiert  
- MCP-Version-Pins auf `>=1.26.0` aktualisiert  

**Codekorrekturen**  
- Ungültiges Modell `gpt-4o-mini` zu `gpt-4.1-mini` korrigiert  

**Inhaltskorrekturen**  
- Defekten Link `READMEmd` → `README.md` korrigiert, Curriculum-Überschrift `Module 1-3` → `Module 0-3` angepasst, case-sensitive Pfad korrigiert  
- Beschädigte doppelte Inhalte von Case Study 5 entfernt  

**Verbesserungen für Anfänger**  
- Einführung, Lernziele und Voraussetzungen für Anfänger ergänzt  

#### Curriculum-Aktualisierungen

**Haupt-README.md**  
- Einträge 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protokoll-Features) zur Curriculum-Tabelle hinzugefügt  

**Modul-READMEs**  
- Lektionen 12 und 13 in Lektionenliste aufgenommen  
- Abschnitt Praktische Anleitungen mit Paginierungslink hinzugefügt  
- Lektionen 5.15 (Custom Transport) und 5.16 (Protocol Features) ergänzt  

**study_guide.md**  
- Mindmap mit allen neuen Themen aktualisiert: MCP Hosts Setup, MCP Inspector, Pagination-Strategien, Protokoll-Features im Detail  

---

## 28. Januar 2026

### MCP Specification 2025-11-25 Compliance Review

#### Kernkonzepte Erweiterung (01-CoreConcepts/)  
- **Neues Client-Primitiv – Roots**: Umfassende Dokumentation zum Roots Client-Primitiv hinzugefügt, das Servern das Verstehen von Dateisystemgrenzen und Zugriffsrechten ermöglicht  
- **Werkzeug-Anmerkungen**: Dokumentation von Verhaltensanmerkungen für Werkzeuge (`readOnlyHint`, `destructiveHint`) für verbesserte Ausführungsentscheidungen hinzugefügt  
- **Werkzeugaufruf beim Sampling**: Sampling-Dokumentation um Parameter `tools` und `toolChoice` für modell-gesteuerte Werkzeugaufrufe während Sampling-Anfragen erweitert  
- **URL-Modus-Auslösung**: Dokumentation der URL-basierten Auslösung für serverinitiierte externe Webinteraktionen hinzugefügt  
- **Tasks (experimentell)**: Neuer Abschnitt dokumentiert experimentelles Tasks-Feature für dauerhafte Ausführungs-wrapper und verzögerten Ergebnisabruf  
- **Icons-Unterstützung**: Hinweis, dass Werkzeuge, Ressourcen, Ressourcenvorlagen und Prompts nun Symbole als zusätzliche Metadaten enthalten können  

#### Dokumentations-Updates  
- **README.md**: MCP Specification 2025-11-25 Versionsverweis und datumsbasierte Versionierungserklärung hinzugefügt  
- **study_guide.md**: Curriculum-Karte mit Tasks und Werkzeug-Anmerkungen im Kernkonzepte-Abschnitt aktualisiert; Dokumentzeitstempel angepasst  

#### Spezifikationskonformität Verifikation  
- **Protokollversion**: Alle Dokumente referenzieren die aktuelle MCP Specification 2025-11-25  
- **Architekturausrichtung**: Bestätigung der Dokumentationskorrektheit zur zweischichtigen Architektur (Daten- und Transportebene)  
- **Primitive Dokumentation**: Validierung von Server-Primitiven (Ressourcen, Prompts, Werkzeuge) und Client-Primitiven (Sampling, Elicitation, Logging, Roots)  
- **Transportmechanismen**: Bestätigung der Richtigkeit der STDIO- und Streamable HTTP-Transport-Dokumentation  
- **Sicherheitsleitlinien**: Abstimmung auf aktuelle MCP Sicherheits-Best Practices Dokumentation bestätigt  

#### Wichtige MCP 2025-11-25 Features Dokumentiert  
- **OpenID Connect Discovery**: Auth-Server-Erkennung über OIDC  
- **OAuth Client ID Metadaten-Dokumente**: Empfohlenes Client-Registrierungsverfahren  
- **JSON Schema 2020-12**: Standarddialekt für MCP-Schema-Definitionen  
- **SDK-Schichten-System**: Formale Anforderungen für SDK-Feature-Unterstützung und Wartung  
- **Governance-Struktur**: Formalisierte Arbeitsgruppen und Interessengruppen in der MCP-Governance  

### Große Sicherheits-Dokumentationsaktualisierung (02-Security/)

#### Integration MCP Security Summit Workshop (Sherpa)  
- **Neue praktische Trainingsressource**: Umfassende Integration mit dem [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in allen Sicherheitsdokumenten  
- **Expeditionsrouten-Abdeckung**: Dokumentation des gesamten Lager-zu-Lager-Fortschritts vom Base Camp bis zum Summit  
- **OWASP-Abstimmung**: Sämtliche Sicherheitshinweise sind nun OWASP MCP Azure Security Guide Risiken zugeordnet  

#### OWASP MCP Top 10 Integration  
- **Neuer Abschnitt**: Hinzufügen der OWASP MCP Top 10 Sicherheitsrisiken-Tabelle mit Azure-Minderungen im Haupt-Security-README  
- **Risiko-basierte Dokumentation**: Ergänzung von mcp-security-controls-2025.md um OWASP MCP Risiko-Verweise (MCP01-MCP08) für jeden Sicherheitsbereich  
- **Referenzarchitektur**: Verlinkungen zur OWASP MCP Azure Security Guide Referenzarchitektur und Implementierungsmustern  

#### Aktualisierte Sicherheitsdateien  
- **README.md**: Sherpa Workshop Übersicht, Expeditionsrouten-Tabelle, OWASP MCP Top 10 Risikoübersicht und Hands-on Trainingsabschnitt hinzugefügt  
- **mcp-security-controls-2025.md**: Header auf Februar 2026 aktualisiert, OWASP Risiko-Verweise (MCP01-MCP08) ergänzt, Versionsinkonsistenz behoben  
- **mcp-security-best-practices-2025.md**: Sherpa und OWASP-Ressourcenabschnitt sowie Zeitstempel aktualisiert  
- **mcp-best-practices.md**: Hands-on Trainingsabschnitt mit Sherpa- und OWASP-Links ergänzt  
- **azure-content-safety-implementation.md**: OWASP MCP06-Verweis, Sherpa Camp 3-Abstimmung und zusätzlichen Ressourcenabschnitt ergänzt  

#### Neue Ressourcenslinks Hinzugefügt  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Einzelne OWASP MCP Risiko-Seiten (MCP01-MCP10)  

### Curriculum-weite MCP Specification 2025-11-25 Ausrichtung

#### Modul 03 - Einstieg  
- **SDK-Dokumentation**: Go SDK zur offiziellen SDK-Liste hinzugefügt; alle SDK-Verweise mit MCP Specification 2025-11-25 abgeglichen  
- **Transportklärung**: STDIO und HTTP Streaming Transportbeschreibungen mit expliziten Spezifikationsverweisen aktualisiert  

#### Modul 04 - Praktische Umsetzung  
- **SDK-Updates**: Go SDK ergänzt; SDK-Liste mit Spezifikationsreferenz aktualisiert  
- **Autorisierung Spezifikation**: MCP Autorisierungsspezifikation auf aktuelle 2025-11-25 Version aktualisiert  

#### Modul 05 - Fortgeschrittene Themen  
- **Neue Features**: Hinweis auf neue MCP Specification 2025-11-25 Features (Tasks, Werkzeug-Anmerkungen, URL Modus-Auslösung, Roots) ergänzt  
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa Workshop Links zu weiterführenden Referenzen hinzugefügt  

#### Modul 06 - Community-Beiträge  
- **SDK-Liste**: Swift- und Rust-SDKs ergänzt; Spezifikationslink auf 2025-11-25 aktualisiert  
- **Spezifikationsreferenz**: Direkter MCP Spezifikationslink ergänzt  

#### Modul 07 - Erkenntnisse aus früher Nutzung
- **Ressourcenaktualisierungen**: Hinzugefügt MCP-Spezifikation 2025-11-25 Link und OWASP MCP Top 10 zu zusätzlichen Ressourcen

#### Modul 08 - Best Practices
- **Spezifikationsversion**: MCP-Spezifikationsreferenz auf 2025-11-25 aktualisiert
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa-Workshop zu zusätzlichen Referenzen hinzugefügt

#### Modul 10 - Optimierung von KI-Workflows
- **Abzeichen-Aktualisierung**: MCP-Version-Abzeichen von SDK-Version (1.9.3) auf Spezifikationsversion (2025-11-25) geändert
- **Ressourcenlinks**: MCP-Spezifikationslink aktualisiert; OWASP MCP Top 10 hinzugefügt

#### Modul 11 - MCP Server Hands-On Labs
- **Spezifikationsreferenz**: MCP-Spezifikationslink auf Version 2025-11-25 aktualisiert
- **Sicherheitsressourcen**: OWASP MCP Top 10 zu offiziellen Ressourcen hinzugefügt

## 18. Dezember 2025

### Sicherheitsdokumentationsupdate - MCP-Spezifikation 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Versionsaktualisierung der Spezifikation
- **Protokollversionsupdate**: Aktualisiert zur Referenz der neuesten MCP-Spezifikation 2025-11-25 (veröffentlicht am 25. November 2025)
  - Alle Spezifikationsversionsreferenzen von 2025-06-18 auf 2025-11-25 aktualisiert
  - Dokumentdatumverweise von 18. August 2025 auf 18. Dezember 2025 aktualisiert
  - Überprüft, dass alle Spezifikations-URLs auf die aktuelle Dokumentation verweisen
- **Inhaltsvalidierung**: Umfassende Validierung der Sicherheits-Best-Practices gemäß neuesten Standards
  - **Microsoft-Sicherheitslösungen**: Verifizierte aktuelle Terminologie und Links für Prompt Shields (früher "Jailbreak-Risikoerkennung"), Azure Content Safety, Microsoft Entra ID und Azure Key Vault
  - **OAuth 2.1 Sicherheit**: Bestätigung der Übereinstimmung mit den neuesten OAuth-Sicherheitsbest-Practices
  - **OWASP-Standards**: Validierung, dass die OWASP Top 10 für LLMs aktuell bleiben
  - **Azure-Dienste**: Überprüfung aller Microsoft Azure-Dokumentationslinks und Best Practices
- **Standards-Ausrichtung**: Alle referenzierten Sicherheitsstandards als aktuell bestätigt
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Sicherheits-Best-Practices
  - Azure Sicherheits- und Compliance-Frameworks
- **Implementierungsressourcen**: Validierte alle Links und Ressourcen für Implementierungsanleitungen
  - Azure API Management Authentifizierungsmuster
  - Microsoft Entra ID Integrationsanleitungen
  - Azure Key Vault Geheimnisverwaltung
  - DevSecOps-Pipelines und Monitoring-Lösungen

### Dokumentationsqualitätssicherung
- **Spezifikationskonformität**: Sicherstellung, dass alle verpflichtenden MCP-Sicherheitsanforderungen (MUSS/NICHT MUSS) mit der neuesten Spezifikation übereinstimmen
- **Aktualität der Ressourcen**: Überprüfung aller externen Links zu Microsoft-Dokumentationen, Sicherheitsstandards und Implementierungshandbüchern
- **Abdeckung von Best Practices**: Bestätigung der umfassenden Abdeckung von Authentifizierung, Autorisierung, KI-spezifischen Bedrohungen, Lieferkettensicherheit und Enterprise-Mustern

## 6. Oktober 2025

### Erweiterung des Bereichs Erste Schritte – Erweiterte Servernutzung & einfache Authentifizierung

#### Erweiterte Servernutzung (03-GettingStarted/10-advanced)
- **Neues Kapitel hinzugefügt**: Einführung eines umfassenden Leitfadens zur erweiterten MCP-Servernutzung, der sowohl reguläre als auch Low-Level-Server-Architekturen behandelt.
  - **Regulärer vs. Low-Level-Server**: Detaillierter Vergleich und Codebeispiele in Python und TypeScript für beide Ansätze.
  - **Handler-basierte Gestaltung**: Erklärung des handlerbasierten Tool-/Ressourcen-/Prompt-Managements für skalierbare, flexible Serverimplementierungen.
  - **Praktische Muster**: Praxisnahe Szenarien, in denen Low-Level-Server-Muster für erweiterte Funktionen und Architektur vorteilhaft sind.

#### Einfache Authentifizierung (03-GettingStarted/11-simple-auth)
- **Neues Kapitel hinzugefügt**: Schritt-für-Schritt-Anleitung zur Implementierung einfacher Authentifizierung in MCP-Servern.
  - **Auth-Konzepte**: Klare Erklärung von Authentifizierung vs. Autorisierung und Umgang mit Zugangsdaten.
  - **Implementierung von Basic Auth**: Middleware-basierte Authentifizierungsmuster in Python (Starlette) und TypeScript (Express) mit Codebeispielen.
  - **Übergang zur fortgeschrittenen Sicherheit**: Anleitung zum Einstieg mit einfacher Authentifizierung und Weiterentwicklung zu OAuth 2.1 und RBAC mit Verweisen auf fortgeschrittene Sicherheitsmodule.

Diese Ergänzungen bieten praktische, hands-on Anleitungen zum Aufbau robuster, sicherer und flexibler MCP-Serverimplementierungen, die grundlegende Konzepte mit fortgeschrittenen Produktionsmustern verbinden.

## 29. September 2025

### MCP Server Datenbank-Integrationslabs – Umfassender praktischer Lernpfad

#### 11-MCPServerHandsOnLabs – Neuer kompletter Datenbank-Integrationslehrplan
- **Vollständiger 13-Lab-Lernpfad**: Ergänzt um umfassenden praktischen Lehrplan zum Aufbau produktionsbereiter MCP-Server mit PostgreSQL-Datenbankintegration
  - **Praxisnahe Implementierung**: Zava Retail Analytics Use Case zur Demonstration von Enterprise-Grade-Mustern
  - **Strukturierter Lernfortschritt**:
    - **Labs 00-03: Grundlagen** – Einführung, Kernarchitektur, Sicherheit & Multi-Tenancy, Umgebungseinrichtung
    - **Labs 04-06: Aufbau des MCP Servers** – Datenbankdesign & Schema, MCP Server Implementierung, Tool-Entwicklung  
    - **Labs 07-09: Erweiterte Funktionen** – Semantische Suche Integration, Testen & Debugging, VS Code Integration
    - **Labs 10-12: Produktion & Best Practices** – Bereitstellungsstrategien, Monitoring & Observability, Best Practices & Optimierung
  - **Enterprise-Technologien**: FastMCP-Framework, PostgreSQL mit pgvector, Azure OpenAI Embeddings, Azure Container Apps, Application Insights
  - **Erweiterte Features**: Row Level Security (RLS), semantische Suche, Multi-Tenant-Datenzugriff, Vektor-Embeddings, Echtzeit-Monitoring

#### Terminologie-Standardisierung – Modulumwandlung zu Labs
- **Umfassendes Dokumentationsupdate**: Systematische Aktualisierung aller README-Dateien in 11-MCPServerHandsOnLabs zur Verwendung des Begriffs "Lab" anstelle von "Modul"
  - **Abschnittsüberschriften**: "What This Module Covers" in allen 13 Labs zu "What This Lab Covers" geändert
  - **Inhaltsbeschreibungen**: "This module provides..." zu "This lab provides..." geändert
  - **Lernziele**: "By the end of this module..." zu "By the end of this lab..." angepasst
  - **Navigationslinks**: Alle Verweise "Module XX:" in "Lab XX:" umgewandelt
  - **Abschlussverfolgung**: "After completing this module..." zu "After completing this lab..." geändert
  - **Technische Referenzen beibehalten**: Python-Modulreferenzen in Konfigurationsdateien erhalten (z.B. `"module": "mcp_server.main"`)

#### Studienführer-Erweiterung (study_guide.md)
- **Visuelle Lehrplanübersicht**: Neuer Abschnitt "11. Database Integration Labs" mit umfassender Visualisierung der Lab-Struktur hinzugefügt
- **Repository-Struktur**: Von zehn auf elf Hauptabschnitte erweitert, detaillierte Beschreibung von 11-MCPServerHandsOnLabs ergänzt
- **Lernpfad-Anleitung**: Navigationshinweise erweitert auf Bereiche 00–11
- **Technology-Coverage**: FastMCP, PostgreSQL und Azure-Dienste-Integrationsdetails ergänzt
- **Lernziele**: Betonung auf produktionsreife Serverentwicklung, Datenbankintegrationsmuster und Unternehmenssicherheit

#### Verbesserte Haupt-README-Struktur
- **Lab-basierte Terminologie**: Haupt-README.md in 11-MCPServerHandsOnLabs auf konsequente "Lab"-Struktur aktualisiert
- **Lernpfadorganisation**: Klarer Fortschritt von Grundlagen über fortgeschrittene Implementierung bis zur Produktionseinführung
- **Praxisbezogener Fokus**: Betonung praktischem, hands-on Lernen mit Enterprise-Grade-Mustern und Technologien

### Verbesserungen der Dokumentationsqualität & Konsistenz
- **Praktische Lernbetonung**: Verstärkte Betonung des lab-basierten, praktischen Ansatzes in der gesamten Dokumentation
- **Enterprise-Musterfokus**: Hervorhebung produktionsreifer Implementierungen und Sicherheitsaspekte für Unternehmen
- **Technologieintegration**: Umfassende Abdeckung moderner Azure-Dienste und KI-Integrationsmuster
- **Lernfortschritt**: Klar strukturierter Pfad von grundlegenden Konzepten zu Produktionseinführungen

## 26. September 2025

### Case Studies Erweiterung – GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) – Fokus auf Ökosystem-Entwicklung
- **README.md**: Umfangreiche Erweiterung mit umfassender GitHub MCP Registry Case Study
  - **GitHub MCP Registry Case Study**: Neue umfassende Fallstudie zur Einführung der GitHub MCP Registry im September 2025
    - **Problem-Analyse**: Detaillierte Untersuchung fragmentierter MCP-Server-Discovery- und Bereitstellungsprobleme
    - **Lösungsarchitektur**: GitHubs zentraler Registry-Ansatz mit Ein-Klick-VS-Code-Installation
    - **Geschäftlicher Nutzen**: Messbare Verbesserungen bei Entwickler-Onboarding und Produktivität
    - **Strategischer Wert**: Fokus auf modulare Agenten-Bereitstellung und Werkzeug-übergreifende Interoperabilität
    - **Ökosystementwicklung**: Positionierung als grundlegende Plattform für agentische Integration
  - **Erweiterte Case-Study-Struktur**: Alle sieben Fallstudien mit konsistenter Formatierung und umfassenden Beschreibungen aktualisiert
    - Azure AI Travel Agents: Betonung Multi-Agent-Orchestrierung
    - Azure DevOps Integration: Fokus auf Workflow-Automatisierung
    - Real-Time Documentation Retrieval: Python-Konsolen-Client-Implementierung
    - Interactive Study Plan Generator: Chainlit konversationelle Web-App
    - In-Editor Documentation: VS Code und GitHub Copilot Integration
    - Azure API Management: Enterprise API-Integrationsmuster
    - GitHub MCP Registry: Ökosystementwicklung und Community-Plattform
  - **Umfassendes Fazit**: Überarbeiteter Schlussabschnitt mit Hervorhebung der sieben Fallstudien über mehrere MCP-Implementierungsdimensionen
    - Unternehmensintegration, Multi-Agent-Orchestrierung, Entwicklerproduktivität
    - Ökosystementwicklung, Bildungsanwendungs-Kategorisierung
    - Vertiefte Einblicke in Architektur-Muster, Implementierungsstrategien und Best Practices
    - Betonung von MCP als ausgereiftes, produktionsreifes Protokoll

#### Studienführer-Updates (study_guide.md)
- **Visuelle Lehrplanübersicht**: Mindmap aktualisiert zur Aufnahme der GitHub MCP Registry im Abschnitt Case Studies
- **Case Studies Beschreibung**: Von generischen Beschreibungen zu detaillierter Aufschlüsselung der sieben umfassenden Fallstudien erweitert
- **Repository-Struktur**: Abschnitt 10 zur umfassenden Fallstudienabdeckung mit spezifischen Implementierungsdetails aktualisiert
- **Changelog-Integration**: Eintrag vom 26. September 2025 ergänzt zur Dokumentation der GitHub MCP Registry Ergänzung und Case Study Erweiterungen
- **Datum-Aktualisierungen**: Fußzeilen-Zeitstempel auf neueste Revision (26. September 2025) aktualisiert

### Verbesserungen der Dokumentationsqualität
- **Konsistenzsteigerung**: Einheitliche Fallstudienformatierung und Struktur über alle sieben Beispiele hinweg standardisiert
- **Umfassende Abdeckung**: Fallstudien beleuchten nun Unternehmens-, Entwicklerproduktivitäts- und Ökosystem-Szenarien
- **Strategische Positionierung**: Verstärkter Fokus auf MCP als grundlegende Plattform für agentische Systembereitstellung
- **Ressourcenintegration**: Aktualisierung zusätzlicher Ressourcen um GitHub MCP Registry Link

## 15. September 2025

### Erweiterung der Fortgeschrittenenthemen – Benutzerdefinierte Transporte & Kontext-Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) – Neuer Leitfaden zur fortgeschrittenen Implementierung
- **README.md**: Vollständiger Implementierungsleitfaden für benutzerdefinierte MCP-Transportmechanismen
  - **Azure Event Grid Transport**: Umfassende serverlose, ereignisgesteuerte Transportimplementierung
    - Beispiele in C#, TypeScript und Python mit Azure Functions Integration
    - Ereignisgesteuerte Architektur-Pattern für skalierbare MCP-Lösungen
    - Webhook-Empfänger und push-basierte Nachrichtenverarbeitung
  - **Azure Event Hubs Transport**: Hochdurchsatz-Streaming-Transportimplementierung
    - Echtzeit-Streaming für latenzarme Szenarien
    - Partitionierungsstrategien und Checkpoint-Verwaltung
    - Nachrichten-Batching und Leistungsoptimierung
  - **Enterprise-Integrationsmuster**: Produktionsreife Architekturbeispiele
    - Verteilte MCP-Verarbeitung über mehrere Azure Functions
    - Hybride Transportarchitekturen mit Kombination mehrerer Transportsysteme
    - Nachrichten-Dauerhaftigkeit, Zuverlässigkeit und Fehlerbehandlung
  - **Sicherheit & Monitoring**: Azure Key Vault Integration und Beobachtbarkeitsmuster
    - Verwaltete Identitätsauthentifizierung und Prinzip der geringsten Privilegien
    - Application Insights Telemetrie und Leistungsüberwachung
    - Circuit Breaker und Fehlertoleranzmuster
  - **Testframeworks**: Umfassende Teststrategien für benutzerdefinierte Transporte
    - Unittests mit Testdoubles und Mocking-Frameworks
    - Integrationstests mit Azure Test Containers
    - Leistungstests und Lasttests

#### Kontext-Engineering (05-AdvancedTopics/mcp-contextengineering/) – Aufkommende KI-Disziplin
- **README.md**: Umfassende Erkundung von Kontext-Engineering als aufkommendes Fachgebiet
  - **Kernprinzipien**: Vollständiges Teilen von Kontext, Bewusstsein für Handlungsentscheidungen und Kontextfenster-Management
  - **MCP-Protokoll-Ausrichtung**: Wie das MCP-Design Herausforderungen des Kontext-Engineerings adressiert
    - Begrenzungen des Kontextfensters und progressive Lade-Strategien
    - Relevanzbestimmung und dynamische Kontextabrufe
    - Multimodale Kontextverarbeitung und Sicherheitsaspekte
  - **Implementierungsansätze**: Single-Thread- vs. Multi-Agent-Architekturen
    - Kontext-Chunking und Priorisierungstechniken
    - Progressives Kontextladen und Komprimierungsstrategien
    - Geschichtete Kontextansätze und Abruffoptimierung
  - **Messrahmen**: Aufkommende Metriken zur Bewertung der Kontextwirksamkeit
    - Eingabeeffizienz, Leistung, Qualität und Nutzererfahrungen
    - Experimentelle Ansätze zur Kontextoptimierung
    - Fehlermusteranalyse und Verbesserungstechniken

#### Lehrplan-Navigationsupdates (README.md)
- **Erweiterte Modulstruktur**: Lehrplantabelle aktualisiert zur Aufnahme neuer Fortgeschrittenenthemen
  - Eingefügt Context Engineering (5.14) und Custom Transport (5.15)
  - Einheitliche Formatierung und Navigationslinks über alle Module hinweg
  - Aktualisierte Beschreibungen zur Darstellung des aktuellen Inhaltsumfangs

### Verbesserungen der Verzeichnisstruktur
- **Namensstandardisierung**: "mcp transport" zu "mcp-transport" umbenannt für Konsistenz mit anderen Fortgeschrittenenkapiteln
- **Inhaltsorganisation**: Alle 05-AdvancedTopics-Ordner folgen nun dem Namensmuster mcp-[thema]

### Verbesserungen der Dokumentationsqualität
- **MCP-Spezifikationsausrichtung**: Alle neuen Inhalte referenzieren die aktuelle MCP-Spezifikation 2025-06-18
- **Mehrsprachige Beispiele**: Umfassende Codebeispiele in C#, TypeScript und Python
- **Enterprise-Fokus**: Produktionsreife Muster und Azure-Cloud-Integration durchgehend
- **Visuelle Dokumentation**: Mermaid-Diagramme zur Architektur- und Ablaufvisualisierung

## 18. August 2025

### Umfassende Dokumentationsaktualisierung – MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) – Komplette Modernisierung
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Vollständige Neufassung gemäß MCP Spezifikation 2025-06-18
  - **Verbindliche Anforderungen**: Explizite MUST/MUST NOT Anforderungen aus der offiziellen Spezifikation mit klaren visuellen Hinweisen hinzugefügt
  - **12 Kern-Sicherheitspraktiken**: Umstrukturierung von einer 15-Punkte-Liste zu umfassenden Sicherheitsdomänen
    - Token-Sicherheit & Authentifizierung mit Integration von externen Identitätsanbietern
    - Sitzungsverwaltung & Transportsicherheit mit kryptografischen Anforderungen
    - KI-spezifischer Bedrohungsschutz mit Microsoft Prompt Shields Integration
    - Zugriffskontrolle & Berechtigungen mit Minimalprivilegienprinzip
    - Inhalts-Sicherheit & Überwachung mit Azure Content Safety Integration
    - Lieferkettensicherheit mit umfassender Komponentenüberprüfung
    - OAuth-Sicherheit & Vermeidung des Confused Deputy-Problems mit PKCE-Implementierung
    - Vorfallsreaktion & Wiederherstellung mit automatisierten Kapazitäten
    - Compliance & Governance mit regulatorischer Ausrichtung
    - Erweiterte Sicherheitskontrollen mit Zero-Trust-Architektur
    - Integration des Microsoft Security Ökosystems mit umfassenden Lösungen
    - Kontinuierliche Sicherheitsentwicklung mit adaptiven Praktiken
  - **Microsoft Security Lösungen**: Verbesserte Integrationsanleitung für Prompt Shields, Azure Content Safety, Entra ID und GitHub Advanced Security
  - **Implementierungsressourcen**: Kategorisierte umfassende Ressourcenlinks nach Offizieller MCP-Dokumentation, Microsoft Security Lösungen, Sicherheitsstandards und Implementierungsleitfäden

#### Erweiterte Sicherheitskontrollen (02-Security/) – Enterprise-Implementierung
- **MCP-SECURITY-CONTROLS-2025.md**: Komplettes Rework mit Enterprise-Sicherheitsrahmenwerk
  - **9 Umfassende Sicherheitsdomänen**: Ausbau von Basis-Kontrollen zu detailliertem Enterprise-Framework
    - Erweiterte Authentifizierung & Autorisierung mit Microsoft Entra ID Integration
    - Token-Sicherheit & Anti-Passthrough-Kontrollen mit umfassender Validierung
    - Sitzungssicherheitskontrollen mit Schutz vor Hijacking
    - KI-spezifische Sicherheitskontrollen mit Schutz vor Prompt-Injektion und Tool-Vergiftung
    - Schutz vor Confused Deputy Attacken mit OAuth-Proxy-Sicherheit
    - Sicherheit bei Tool-Ausführung mit Sandboxing und Isolation
    - Kontrolle der Lieferkettensicherheit mit Abhängigkeitsprüfung
    - Monitoring- & Erkennungskontrollen mit SIEM-Integration
    - Vorfallsreaktion & Wiederherstellung mit automatisierten Fähigkeiten
  - **Implementierungsbeispiele**: Detaillierte YAML-Konfigurationsblöcke und Codebeispiele hinzugefügt
  - **Integration von Microsoft-Lösungen**: Umfassende Abdeckung von Azure-Sicherheitsdiensten, GitHub Advanced Security und Enterprise-Identitätsmanagement

#### Erweiterte Sicherheitsthemen (05-AdvancedTopics/mcp-security/) – Produktionsreife Implementierung
- **README.md**: Vollständige Neufassung für Enterprise-Sicherheitsimplementierung
  - **Aktuelle Spezifikationsausrichtung**: Aktualisiert auf MCP Spezifikation 2025-06-18 mit verbindlichen Sicherheitsanforderungen
  - **Verbesserte Authentifizierung**: Microsoft Entra ID Integration mit umfangreichen .NET- und Java Spring Security-Beispielen
  - **KI-Sicherheitsintegration**: Microsoft Prompt Shields und Azure Content Safety Implementierung mit detaillierten Python-Beispielen
  - **Erweiterte Bedrohungsminderung**: Umfassende Implementierungsbeispiele für
    - Schutz vor Confused Deputy Attacken mit PKCE und Benutzerzustimmungsvalidierung
    - Verhinderung von Token-Passthrough mit Audience-Validierung und sicherem Token-Management
    - Schutz vor Session Hijacking mit kryptografischer Bindung und Verhaltensanalyse
  - **Enterprise Security Integration**: Azure Application Insights Monitoring, Bedrohungserkennungspipelines und Lieferkettensicherheit
  - **Implementierungscheckliste**: Klare Unterscheidung verbindlicher gegenüber empfohlenen Sicherheitskontrollen mit Vorteilen des Microsoft Security Ökosystems

### Dokumentationsqualität & Standardausrichtung
- **Spezifikationsreferenzen**: Alle Verweise auf aktuelle MCP Spezifikation 2025-06-18 aktualisiert
- **Microsoft Security Ökosystem**: Verbesserte Integrationsanleitungen in sämtlichen Sicherheitsdokumentationen
- **Praktische Implementierung**: Erweiterte detaillierte Codebeispiele in .NET, Java und Python mit Enterprise-Mustern
- **Ressourcenorganisation**: Umfassende Kategorisierung offizieller Dokumentation, Sicherheitsstandards und Implementierungsanleitungen
- **Visuelle Indikatoren**: Klare Markierung verbindlicher Anforderungen gegenüber empfohlenen Praktiken

#### Kernkonzepte (01-CoreConcepts/) – Komplette Modernisierung
- **Protokollversions-Update**: Aktualisiert auf Referenz der aktuellen MCP Spezifikation 2025-06-18 mit datumsbasierter Versionierung (YYYY-MM-DD Format)
- **Architekturverfeinerung**: Verbesserte Beschreibungen von Hosts, Clients und Servern zur Abbildung aktueller MCP-Architekturmuster
  - Hosts nun klar definiert als KI-Anwendungen zur Koordination mehrerer MCP-Client-Verbindungen
  - Clients beschrieben als Protokollverbindungen mit eins-zu-eins Server-Beziehungen
  - Server erweitert mit Szenarien für lokale vs. remote Bereitstellung
- **Primitive Umstrukturierung**: Vollständige Überarbeitung von Server- und Client-Primitiven
  - Server-Primitives: Ressourcen (Datenquellen), Prompts (Vorlagen), Tools (ausführbare Funktionen) mit detaillierten Erklärungen und Beispielen
  - Client-Primitives: Sampling (LLM-Vervollständigungen), Elicitation (Benutzereingaben), Logging (Debugging/Monitoring)
  - Aktualisiert mit aktuellen Discover- (`*/list`), Abruf- (`*/get`) und Ausführungs- (`*/call`) Methodenmustern
- **Protokollarchitektur**: Einführung eines Zwei-Schichten-Architekturmodells
  - Datenschicht: JSON-RPC 2.0 Basis mit Lifecycle-Management und Primitiven
  - Transportschicht: STDIO (lokal) und Streamable HTTP mit SSE (remote) Transportmechanismen
- **Sicherheitsrahmenwerk**: Umfassende Sicherheitsprinzipien inklusive expliziter Nutzerzustimmung, Datenschutz, Sicherheit bei Tool-Ausführung und Transportschicht-Sicherheit
- **Kommunikationsmuster**: Protokollnachrichten aktualisiert zur Darstellung von Initialisierung, Entdeckung, Ausführung und Benachrichtigungsabläufen
- **Codebeispiele**: Überarbeitete mehrsprachige Beispiele (.NET, Java, Python, JavaScript) zur Abbildung aktueller MCP SDK-Muster

#### Sicherheit (02-Security/) – Umfassende Sicherheitsüberarbeitung  
- **Standards-Ausrichtung**: Volle Ausrichtung an MCP Spezifikation 2025-06-18 Sicherheitsanforderungen
- **Evolution der Authentifizierung**: Dokumentierte Entwicklung von eigenständigen OAuth-Servern hin zu Delegation an externe Identitätsanbieter (Microsoft Entra ID)
- **KI-spezifische Bedrohungsanalyse**: Erweiterte Abdeckung moderner KI-Angriffsvektoren
  - Detaillierte Prompt-Injektion Angriffsszenarien mit Praxisbeispielen
  - Mechanismen der Tool-Vergiftung und "Rug Pull" Angriffsmuster
  - Kontextsfenstervergiftung und Modellverwirrungsangriffe
- **Microsoft AI-Sicherheitslösungen**: Umfassende Abdeckung des Microsoft Security Ökosystems
  - AI Prompt Shields mit fortgeschrittener Erkennung, Hervorhebung und Delimiter-Techniken
  - Azure Content Safety Integrationsmuster
  - GitHub Advanced Security für Lieferkettenschutz
- **Erweiterte Bedrohungsminderung**: Detaillierte Sicherheitskontrollen für
  - Session Hijacking mit MCP-spezifischen Angriffsszenarien und kryptografischen Session-ID Anforderungen
  - Confused Deputy Probleme in MCP Proxy-Szenarien mit expliziten Zustimmungsanfordungen
  - Token-Passthrough-Schwachstellen mit obligatorischen Validierungskontrollen
- **Lieferkettensicherheit**: Erweiterte Abdeckung der KI-Lieferkette einschließlich Foundation Models, Embeddings Services, Context Provider und Drittanbieter-APIs
- **Foundation Security**: Verbesserte Integration mit Enterprise-Sicherheitsmustern inklusive Zero Trust Architektur und Microsoft Security Ökosystem
- **Ressourcenorganisation**: Kategorisierte umfassende Ressourcenlinks nach Typ (Offizielle Docs, Standards, Forschung, Microsoft Lösungen, Implementierungsleitfäden)

### Verbesserungen in der Dokumentationsqualität
- **Strukturierte Lernziele**: Verbesserte Lernziele mit spezifischen, umsetzbaren Ergebnissen
- **Querverweise**: Hinzugefügte Verlinkungen zwischen verwandten Sicherheits- und Kernkonzept-Themen
- **Aktuelle Informationen**: Alle Datumsreferenzen und Spezifikationslinks auf aktuelle Standards aktualisiert
- **Implementierungsanleitungen**: Ergänzung spezifischer, umsetzbarer Implementierungsleitlinien in beiden Abschnitten

## 16. Juli 2025

### README und Navigationsverbesserungen
- Gesamtüberarbeitung der Curriculum-Navigation in README.md
- Ersetzung der `<details>`-Tags durch zugänglicheres tabellarisches Format
- Erstellung alternativer Layoutoptionen im neuen Ordner „alternative_layouts“
- Hinzugefügt Kartenbasierte, tabbed-Style- und Akkordeon-Stil Navigationsbeispiele
- Aktualisierung des Repository-Struktur-Abschnitts zur Aufnahme aller neuesten Dateien
- Verbesserung der Sektion „Wie man dieses Curriculum verwendet“ mit klaren Empfehlungen
- Aktualisierung der MCP Spezifikations-Links auf korrekte URLs
- Ergänzung des Abschnitts Kontext-Engineering (5.14) in der Curriculum-Struktur

### Aktualisierungen im Lernleitfaden
- Vollständige Überarbeitung des Lernleitfadens zur Ausrichtung an der aktuellen Repository-Struktur
- Neue Sektionen für MCP Clients und Tools sowie populäre MCP Server hinzugefügt
- Aktualisierung der Visual Curriculum Map zur korrekten Darstellung aller Themen
- Verbesserte Beschreibungen der Advanced Topics zur Abdeckung aller spezialisierten Bereiche
- Aktualisierung der Fallstudien-Sektion mit echten Beispielen
- Hinzufügen dieses umfassenden Changelogs

### Community-Beiträge (06-CommunityContributions/)
- Detaillierte Informationen zu MCP Servern für die Bilderzeugung hinzugefügt
- Umfassende Sektion zum Einsatz von Claude in VSCode ergänzt
- Einrichtung und Nutzung des Cline Terminal Clients beschrieben
- MCP Client Sektion aktualisiert zur Aufnahme aller populären Client-Optionen
- Beitragende Beispiele mit präziseren Codebeispielen erweitert

### Erweiterte Themen (05-AdvancedTopics/)
- Alle spezialisierten Themenordner konsistent benannt und organisiert
- Material und Beispiele zu Kontext-Engineering hinzugefügt
- Dokumentation zur Foundry Agent Integration erstellt
- Entra ID Sicherheitsintegration erweitert dokumentiert

## 11. Juni 2025

### Erste Erstellung
- Erste Version des MCP für Anfänger Curriculums veröffentlicht
- Grundstruktur für alle 10 Hauptabschnitte erstellt
- Visuelle Curriculum-Karte für Navigation implementiert
- Erste Beispielprojekte in mehreren Programmiersprachen hinzugefügt

### Erste Schritte (03-GettingStarted/)
- Erste Server-Implementierungsbeispiele erstellt
- Anleitung zur Client-Entwicklung hinzugefügt
- Anweisungen zur LLM Client-Integration aufgenommen
- Dokumentation zur VS Code Integration eingefügt
- Server-Sent Events (SSE) Server-Beispiele implementiert

### Kernkonzepte (01-CoreConcepts/)
- Detaillierte Erklärung der Client-Server-Architektur hinzugefügt
- Dokumentation zentraler Protokoll-Komponenten erstellt
- Messaging-Muster im MCP dokumentiert

## 23. Mai 2025

### Repository-Struktur
- Repository mit grundlegender Ordnerstruktur initialisiert
- README-Dateien für jeden Hauptabschnitt erstellt
- Übersetzungsinfrastruktur aufgesetzt
- Bildmaterial und Diagramme hinzugefügt

### Dokumentation
- Erste README.md mit Curriculum-Übersicht erstellt
- CODE_OF_CONDUCT.md und SECURITY.md hinzugefügt
- SUPPORT.md mit Hilfsanleitungen eingerichtet
- Vorläufige Struktur des Lernleitfadens erstellt

## 15. April 2025

### Planung und Rahmenwerk
- Erste Planung des Curriculums MCP für Anfänger
- Lernziele und Zielgruppen definiert
- 10-Abschnitts-Struktur des Curriculums skizziert
- Konzeptueller Rahmen für Beispiele und Fallstudien entwickelt
- Erste Prototyp-Beispiele für Schlüsselkonzepte erstellt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->