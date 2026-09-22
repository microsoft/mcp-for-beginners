# Änderungsprotokoll: MCP für Anfänger Curriculum

Dieses Dokument dient als Aufzeichnung aller wesentlichen Änderungen am Model Context Protocol (MCP) für Anfänger Curriculum. Änderungen werden in umgekehrter chronologischer Reihenfolge dokumentiert (neueste Änderungen zuerst).

## 9. September 2026

### MCP 2026-07-28 Finale Spezifikationsanpassung

Das englische Curriculum wurde vom Release-Kandidaten und der `2025-11-25`
Basis-Leitlinie zur finalen MCP `2026-07-28` Spezifikation aktualisiert.

- **Aktualisiert**: Referenzen auf die aktuelle Version, Spezifikationslinks, zustandslose
  Anforderungsrichtlinien, `server/discover`, Streamable HTTP-Headers und den Lifecycle
  der Tasks-Erweiterung in 38 englischen Dokumentationsdateien.
- **Korrigiert**: Elicitation verwendet jetzt `elicitation/create`, Sampling nutzt
  `sampling/createMessage`, und `InputRequiredResult.resultType` verwendet
  `"input_required"`.
- **Ersetzt**: Die ungenaue Root Context Konversationsstatus-Lektion wurde durch eine
  protokollgenaue Roots-Lektion ersetzt, die informative Dateisystem-Hinweise, den
  aktuellen Multi-Round-Trip-Fluss, Sicherheitsgrenzen und Migrationsoptionen behandelt.
- **Klärung**: Roots, Sampling, Logging und Dynamic Client Registration sind in
  `2026-07-28` veraltet, mit ihren empfohlenen Ersatzmethoden und dem frühestmöglichen
  Entfernungsdatum dokumentiert.
- **Markiert**: Beispiele, die noch vom MCP `2025-11-25`, HTTP+SSE,
  Initialisierungs-Handshakes oder Protokollsitzungen abhängen, werden als
  Legacy-Kompatibilitätsbeispiele beibehalten und nicht als aktuelle Implementierungen präsentiert.
- **Sicherheitshinweise**: Die eigenständigen Sicherheitsleitfäden wurden aktualisiert,
  um per-Anfrage-Autorisierung und explizite Anwendungsstatus-Handles statt
  entfernter Protokollsitzungs-IDs zu verwenden. Client ID Metadata Documents sind
  nun der bevorzugte Registrierungsweg, Dynamic Client Registration (DCR) wird
  als nur kompatibel dokumentiert.
- **Unterstützendes Material**: Aktualisierung des Studienleitfadens, der Mitwirkenden-Checkliste,
  der Publora Fallstudie und der APIM Fallstudie. Die APIM-Anleitung empfiehlt jetzt
  den aktuellen Streamable HTTP `/mcp` Endpunkt statt des veralteten `/sse`.
- **Kanonische Links**: Ersetzte ausgemusterte und Entwurfs-Spezifikations-URLs im englischen
  Quell-Markdown durch versionierte `2026-07-28` Links, wobei explizite Links zu
  Legacy-Versionen erhalten bleiben, wenn ein Beispiel an älteres Werkzeug gekoppelt ist.
- **Stabile Dateinamen**: Das finale Spezifikationshandbuch und zwei Sicherheitsleitfäden
  wurden umbenannt, um Release-Kandidaten- und Jahres-Suffixe zu entfernen, danach alle
  englischen Hyperlinks auf ihre stabilen Pfade aktualisiert.
- **Neues Autorisierungsbeispiel**: Hinzugefügt wurde ein getesteter
  [TypeScript MCP `2026-07-28` Ressourcenausführungsserver](./02-Security/samples/cimd-dcr-auth/README.md),
  der bevorzugte Client ID Metadata Documents mit veralteter Dynamic Client Registration
  als Fallback vergleicht. Das Beispiel enthält RFC 9728 Discovery, JWKS Validierung,
  Tool-spezifische Bereiche, zwölf Tests und eine Auth0-Einrichtungsanleitung.
- **Übersetzungsumfang**: Es wurden nur englische Quelldateien bearbeitet; generierte






Ein herstellerneutrales Begleitmaterial für MCP-Werkzeuge wurde hinzugefügt, die reale


- **Neu**: Die [Zuverlässigkeits-Sidecar Begleitlektion][reliability-sidecar]
  verwendet eine Support-Ticket-Geschichte, zwei Mermaid-Diagramme und einen Entscheidungsfluss
  für Wiederholungen zur Erklärung von stabilen Betriebsschlüsseln, atomarer
  Duplikatsannahme, Abgleich, Belegen und der Tasks-Erweiterungsgrenze.
- **Neu**: Eine Standardbibliothek Python und SQLite Fehlerinjektionsübung verwendet
  getrennte Operation- und Ticket-Datenbanken, um eine verlorene Antwort nach dem
  Abschluss eines externen Effekts zu demonstrieren. Sechs deterministische Tests
  decken naive Duplikate, geschützte Neustartwiederherstellung, Payload-Konflikte,
  zwischengespeicherte Ergebnisse, aktive Claims und gleichzeitige Duplikatsannahme ab.
- **Aktualisiert**: Modul 08 verlinkt nun die Begleitlektion, weist das finale `2026-07-28`
  zustandslose Anforderungsmodell aus, unterscheidet OpenTelemetry-Beobachtbarkeit
  vom veralteten MCP-Logging-Feature und beschränkt sein allgemeines Beispiel für
  Wiederholungen auf Leseoperationen.
- **Optional**: Die Lektion überträgt ihre portablen Konzepte auf eine markierte Community
  Implementierung, ohne dass der gehostete Service oder ein Netzwerkaufruf Teil der Übung sind.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. Juli 2026

### Neue Lektion: Der MCP Spezifikations-Release-Kandidat 2026-07-28

Aufnahme der kommenden `2026-07-28` MCP Spezifikations-Release-Kandidaten (angekündigt am 21. Mai 2026; finaler Release geplant für 28. Juli 2026), zusammengefasst aus dem [offiziellen Ankündigungs-Blogpost](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Die Basis des Curriculums bleibt **MCP Spezifikation 2025-11-25**, bis die neue Version veröffentlicht wird, daher wird dies als zukunftsgerichtete Anleitung und nicht als Umschreibung bestehender Lektionen präsentiert.

- **Neu**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — eine vollständige Lektion zum zustandslosen Protokollkern (Entfernung des `initialize` Handshakes und von `Mcp-Session-Id`), den neuen `Mcp-Method`/`Mcp-Name` Routing-Headern, `ttlMs`/`cacheScope` Caching-Metadaten, W3C Trace Context in `_meta`, dem formalen Erweiterungsrahmenwerk (MCP Apps und die neue Tasks-Erweiterung), sechs Autorisierungshärtungs-SEPs, der Verwahrung von Roots/Sampling/Logging und der Umstellung auf vollständiges JSON Schema 2020-12 für Werkzeugschemata.
- **Aktualisiert** mit zukunftsweisenden Verweisen auf die neue Lektion:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): Protokollversions-Hinweis, Sampling/Roots/Logging/Tasks Abschnitte und "Was kommt als Nächstes"
  - [02-Security/README.md](./02-Security/README.md): Autorisierungshärtungs-Hinweis
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): Hinweis zum zustandslosen Transport
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling-Verwahrungshinweis
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging-Verwahrung und Tasks-Erweiterungshinweis
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): Hinweis zum zustandslosen/sitzungsbasierten Routing
  - [README.md](./README.md): "Vorausschau" Hinweis im Spezifikationsabschnitt und neuer `1.1` Eintrag in der Curriculummodultabelle
  - [study_guide.md](./study_guide.md): zukunftsgerichteter Punkt unter der Core Concepts Übersicht und ein datierter Ergänzungshinweis
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): Hinweis zur `mcp-session-id` Transport-Karte vor dem zustandslosen Anforderungsmodell
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): Modulübersichtshinweis zu Root Contexts/Sampling-Verwahrungen und Tasks-Erweiterung
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): Autorisierungshärtungs-Hinweis

## 24. Juni 2026

### Neue Lektion: Verwendung von MCP in Copilot-App

- [Werkzeugabschnitt](./12-tooling/README.md) Werkzeugsabschnitt hinzugefügt.
- [MCP in Copilot-App](./12-tooling/01-copilot-app/README.md)

## 16. Juni 2026

### MCP Spezifikationsanpassung & Mustervalidierung

Curriculum wurde gegen die aktuelle **MCP Spezifikation 2025-11-25** und die neuesten offiziellen SDKs validiert, danach verbliebene veraltete Spezifikationsreferenzen korrigiert und bestätigt, dass die Kernbeispiele weiterhin kompilieren und laufen.

#### Korrekturen der Spezifikationsversion (2025-06-18 / 2025-03-26 → 2025-11-25)

Englische Inhalte aktualisiert, die noch eine ältere Spezifikationsrevision als *aktuelle/neuste* Norm anführten, und Links zu den kanonischen `modelcontextprotocol.io` Spezifikationspfaden umgestellt:
- **05-AdvancedTopics/mcp-security/README.md**: Aktualisiert das Banner "Aktueller Standard", Einleitung, Überschrift über Kernprinzipien der Sicherheit, Überschrift über obligatorische Anforderungen, Microsoft Entra ID Abschnitt, Referenzen & Ressourcen-Links und abschließende Sicherheitsmitteilung (8 Referenzen) auf 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Aktualisiert den Link zu Zusatzressourcen in der Spezifikation und das Banner "Aktueller Standard" auf 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Ersetzte den veralteten `2025-03-26` Link zu Sicherheit und Vertrauen mit der aktuellen Seite zu Sicherheitspraktiken 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Aktualisierte den offiziellen Sampling-Dokumentationslink auf 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Aktualisierte den gegenwärtigen "aktuellen MCP Spezifikations"-Verweis und den Link zu Zusatzressourcen auf 2025-11-25 (historische SSE-Verwahrungshinweise aus Genauigkeitsgründen belassen)

#### Musterüberprüfung gegen aktuelle SDKs

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` löste `@modelcontextprotocol/sdk@1.29.0` auf; `tsc --noEmit` bestand ohne Typfehler — bestehende `McpServer`/`StdioServerTransport` APIs bleiben gültig
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validiert in isoliertem `.venv` mit `mcp[cli]` (1.27.2); `py_compile` bestanden und `FastMCP.list_tools()` gab korrekt die Werkzeuge `add` und `subtract` zurück
- Bestätigt, dass alle Beispiel-`@modelcontextprotocol/sdk` Versionsbereiche (`>=1.26.0` / `^1.26.0` / `^1.27.0`) sauber auf die aktuelle `1.29.0` auflösen ohne breaking API-Änderungen

#### Abhängigkeits-Pin-Anpassung (Schließen von Versionslücken)

Veraltete SDK-Pins erhöht, sodass jedes Beispiel die aktuelle MCP Version verwendet, entsprechend der Repo-weiten Konvention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` von `^1.8.0` → `>=1.26.0` angehoben und die veraltete Paketbeschreibung `"updated for MCP 2025-06-18"` auf `"aligned with MCP Specification 2025-11-25"` aktualisiert
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** und **lab4/code/github_mcp_server/pyproject.toml**: Exaktes Pin `mcp==1.23.0` → `mcp>=1.26.0` erhöht; beide `uv.lock` Dateien (`uv lock`) neu generiert, damit Lockfiles auf aktuelle `mcp 1.27.2` auflösen und mit den Manifesten synchron bleiben

#### Analyse der Curriculum-Lücken — Abdeckung neuester Spezifikationsfeatures

Bestätigt, dass das Curriculum bereits alle in MCP 2025-11-25 eingeführten/erweiterten Primitiven abdeckt, somit keine Inhaltslücken bestehen:
- **Sampling**: Lektion 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-Modus)**: Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumentiert in 00-Introduction, 01-CoreConcepts und 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentelle, langlaufende Operationen)**: Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features
- **Tool-Anmerkungen** (`readOnlyHint` / `destructiveHint`): Dokumentiert in 01-CoreConcepts und 05-AdvancedTopics/mcp-protocol-features

### Sicherheitshärtung & Behebung von Abhängigkeits-Schwachstellen

Ein vollständiger Sicherheitsscan aller Abhängigkeitsmanifestdateien und Quellcodes der Beispiele wurde durchgeführt, anschließend wurden alle gemeldeten npm-Warnungen und ein Code-Level-Fund behoben. Nach der Behebung meldet `npm audit` **0 Schwachstellen** in jedem überprüften Verzeichnis.

#### npm Abhängigkeits-Schwachstellen (transitiv) — Behoben

 Es wurden alle 15 eingereichten `package-lock.json` Dateien auditiert. Schwachstellen beschränkten sich auf transitive Abhängigkeiten, die durch das MCP Inspector Dev-Tool, den OpenAI Client und das MCP SDK eingebracht wurden; alle sind nun ohne Brüche der Beispiele behoben:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** und **lab3/code/weather_mcp/inspector**: Aktualisiert `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), was die gebündelten Sicherheitswarnungen von `ajv`, `brace-expansion`, `diff`, `path-to-regexp` und `ws` beseitigte. Ein npm `overrides`-Eintrag wurde hinzugefügt, der die gepatchte Version `shell-quote@1.8.4` erzwingt, um die verbleibende kritische Warnung von `concurrently` zu eliminieren; beide Lockfiles wurden neu generiert (jetzt 0 Schwachstellen)
- **03-GettingStarted/samples/typescript**: `npm audit fix` aktualisierte die transitive Abhängigkeit `qs` (mittel) auf eine gepatchte Version
- **03-GettingStarted/samples/javascript**: `npm audit fix` aktualisierte die transitive Abhängigkeit `hono` (mittel) auf eine gepatchte Version
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` aktualisierte die transitive Abhängigkeit `form-data` (hoch) auf eine gepatchte Version
- **03-GettingStarted/11-simple-auth/solution/typescript**: Das fehlende `package-lock.json` wurde generiert, sodass das Projekt reproduzierbar und auditierbar ist (0 Schwachstellen)

#### Sicherheitsfix auf Code-Ebene (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `shell=True` wurde aus dem `open_in_vscode`-Tool entfernt. Das vorherige `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` erlaubte, dass Shell-Metazeichen in einem Ordnerpfad von `cmd.exe` interpretiert wurden (Command Injection-Vektor). Es startet nun direkt das aufgelöste `Code.exe` mit dem Ordner als Argument — ohne Shell — was funktional äquivalent und sicher ist

#### Python-Abhängigkeitsprüfung

- Jede Python-Anforderungssatz wurde mit `pip-audit` geprüft. `05-AdvancedTopics` und `03-GettingStarted/samples/python` meldeten **keine bekannten Schwachstellen** (deren Bereiche für `mcp` / `httpx` / `pydantic` / `python-dotenv` führen zu aktuellen gepatchten Versionen)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` meldete für die transitive Abhängigkeit **`werkzeug` 3.1.1** drei `safe_join` DoS-Warnungen durch Windows-Gerätenamen — `CVE-2025-66221`, `CVE-2026-21860` und `CVE-2026-27199` (alle behoben in 3.1.6). Ein expliziter Sicherheitspin `werkzeug>=3.1.6` wurde hinzugefügt, damit die gepatchte Version genutzt wird; bestätigt, dass die Einschränkung mit dem `chainlit` / `mcp` / `semantic-kernel` Stack sauber aufgelöst wird

### Produktnamens-Rebranding

Aktualisierte alle Kursinhalte, um die Produkt-Umbenennung von Microsoft widerzuspiegeln:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Aktualisierter Discord-Community-Link
- **AGENTS.md**: Aktualisierter Discord-Server-Verweis
- **README.md**: Aktualisierte Verweise auf Technologie-Ökosysteme
- **study_guide.md**: Aktualisierte Fallstudien-Verweise
- **05-AdvancedTopics/README.md**: Aktualisierter Titel und Beschreibung des Moduls 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Aktualisierte Abschnittsüberschrift und Beschreibung
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Vollständige Aktualisierung des Modultitels und Inhalts
- **05-AdvancedTopics/mcp-security-entra/README.md**: Aktualisierter Querverweis-Link
- **07-LessonsfromEarlyAdoption/README.md**: Aktualisierte Fallstudien-Verweise
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Aktualisierter Abschnitt 9 Überschrift, Badges und Fähigkeiten
- **08-BestPractices/README.md**: Aktualisierter Discord-Community-Link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Aktualisierter Discord-Kanal-Verweis
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Aktualisierter Modell-Deployment-Verweis
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Aktualisierte Tabelle der KI-Dienste
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Aktualisierte Ressourcen-Verweise

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension für VS Code
- **README.md**: Aktualisierte Hauptverweise im Curriculum
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Aktualisierter Modultitel, Übersicht und alle Modulüberschriften
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Aktualisierter Titel, Lernziele, Einrichtungshinweise und Ressourcen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Aktualisierter Titel, Lernziele, MCP-Hosts-Tabelle und Querverweise
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Aktualisierter Titel, Badges, Voraussetzungen und Ressourcen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Aktualisierte Verweise auf Agent Builder und Feedback-Link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Aktualisierte Voraussetzungen und Erweiterungsverweise

---

## 11. April 2026

### Neue Lektion, Dokumentationskorrekturen und Abhängigkeitsupdates

#### Neue Kursinhalte hinzugefügt

**Modul 05 - Fortgeschrittene Themen**
- **Lektion 5.17: Gegenseitiges Multi-Agenten-Denken mit MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Neuer umfassender Leitfaden zum adversarial debate Muster für Multi-Agenten-Systeme
  - Mermaid Architekturdiagramm: zwei Agenten → gemeinsamer MCP-Server → Debattentranskript → Richter → Urteil
  - Gemeinsamer MCP-Tool-Server (`web_search` + `run_python`) in Python und TypeScript implementiert
  - Gegensätzliche System-Prompts (FÜR / GEGEN / Richter) mit expliziten Werkzeugnutzungsanforderungen
  - Debatten-Orchestrator in Python, TypeScript und C#, der Runden verwaltet und Argumente routet
  - MCP `ClientSession`-Anbindung für den Orchestrator zu tatsächlichen Werkzeugaufrufen
  - Anwendungsbeispieltabelle (Halluzinationserkennung, Bedrohungsmodellierung, API-Design-Review, Faktenprüfung, Technologiewahl)
  - Sicherheitsüberlegungen: Sandbox-Ausführung, Werkzeugaufrufvalidierung, Ratenbegrenzung, Prüfprotokollierung
  - Strukturierte Übung mit drei praktischen Szenarien (Code Review, Architekturentscheidung, Inhaltsmoderation)

#### Dokumentationskorrekturen

**Modul 03 - Erste Schritte**
- **05-stdio-server/README.md**: Korrigiertes unvollständiges TypeScript stdio-server Beispiel – fehlende Transport-Instanziierung (`new StdioServerTransport()`) und `server.connect(transport)`-Aufruf ergänzt, um den Python- und .NET-Beispielen im selben Abschnitt zu entsprechen
- **14-sampling/README.md**: Tippfehler korrigiert — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kursaktualisierungen

**Haupt-README.md**
- Eintrag 5.17 (Gegenseitiges Multi-Agenten-Denken mit MCP) in die Curriculum-Tabelle mit Direktlink zur neuen Lektion hinzugefügt

**05-AdvancedTopics/README.md**
- Lektion 5.17 Zeile in der Unterrichtsliste hinzugefügt

**study_guide.md**
- Thema Gegenseitiges Multi-Agenten-Denken zur Mindmap und Fließtextbeschreibung der fortgeschrittenen Themen hinzugefügt

#### Code- und Sicherheitskorrekturen

**Modul 05 - Gegnerschaftliche Agenten (`mcp-adversarial-agents`)**
- **Sicherheitsfix — Kommandoinjektion**: Ersetzte Shell-Interpolation mit `execSync` durch `execFile` + `promisify` im TypeScript `run_python`-Tool, wodurch die Kommandoinjektionsfläche entfällt (LLM-gesteuerter Code wird jetzt als Literal-argv-Element ohne Shell-Beteiligung übergeben)
- **MCP-Tool-Loop-Anbindung**: Aktualisierte den Python-Debatten-Orchestrator zur Nutzung des `AsyncAnthropic`-Client (ersetzt blockierenden synchronen `Anthropic`), übergibt eine live `ClientSession` direkt bei jedem Agentenwechsel, ruft Werkzeugdefinitionen via `session.list_tools()` jeden Durchlauf ab und verschickt `tool_use` Blocks via `session.call_tool()` in einer Schleife, bis das Modell eine finale Textantwort abgibt

#### Abhängigkeitsupdates

- Aktualisierte `hono` auf 4.12.12 in mehreren Paketen (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aktualisierte `@hono/node-server` von 1.19.11 auf 1.19.13 in TypeScript-Paketen
- Aktualisierte `cryptography` von 46.0.5 auf 46.0.7 in Python-Paketen (10-StreamliningAIWorkflows Labs 3 und 4)
- Aktualisierte `lodash` von 4.17.23 auf 4.18.1 im 10-StreamliningAIWorkflows inspector

#### Übersetzungen

- Synchronisierte Übersetzungen für 48+ Sprachen mit den neuesten Quelländerungen (i18n-Update)

---

## 5. Februar 2026

### Repositoryweite Validierungs- und Navigationsverbesserungen

#### Neue Kursinhalte hinzugefügt

**Modul 03 - Erste Schritte**
- **12-mcp-hosts/README.md**: Neuer umfassender Leitfaden zur Einrichtung von MCP-Hosts
  - Konfigurationsbeispiele für Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-Konfigurationsvorlagen für alle wichtigen Hosts
  - Vergleichstabelle der Transporttypen (stdio, SSE/HTTP, WebSocket)
  - Fehlerbehebung bei häufigen Verbindungsproblemen
  - Sicherheits-Best Practices für Host-Konfiguration

- **13-mcp-inspector/README.md**: Neuer Debugging-Leitfaden für MCP Inspector
  - Installationsmethoden (npx, globales npm, aus dem Quellcode)
  - Verbindung zu Servern via stdio und HTTP/SSE
  - Testwerkzeuge, Ressourcen und Prompt-Workflows
  - VS Code-Integration mit MCP Inspector
  - Häufige Debugging-Szenarien mit Lösungen

**Modul 04 - Praktische Implementierung**
- **pagination/README.md**: Neuer Leitfaden zur Pagination-Implementierung
  - Cursor-basierte Pagination-Muster in Python, TypeScript, Java
  - Clientseitige Pagination-Handhabung
  - Cursor-Designstrategien (opak vs. strukturiert)
  - Empfehlungen zur Leistungsoptimierung

**Modul 05 - Fortgeschrittene Themen**
- **mcp-protocol-features/README.md**: Neuer Deep-Dive in Protokollfunktionen
  - Implementierung von Fortschritts-Benachrichtigungen
  - Muster für Anforderungssabbrüche
  - Ressourcenvorlagen mit URI-Mustern
  - Server-Lebenszyklusmanagement
  - Steuerung des Log-Level
  - Fehlerbehandlungsmuster mit JSON-RPC-Codes

#### Navigationskorrekturen (24+ Dateien aktualisiert)

**README-Dateien der Hauptmodule**
 Nun Verlinkungen zu erstem Unterricht UND nächstem Modul

**02-Security Unterdateien**
- Alle 5 ergänzenden Sicherheitsdokumente haben jetzt eine "What's Next"-Navigation:

**09-CaseStudy Dateien**
- Alle Fallstudien-Dateien besitzen nun eine sequenzielle Navigation:

**10-StreamliningAI Labs**
Dem Modul 10 Überblick und Modul 11 wurden What's Next-Abschnitte hinzugefügt

#### Code- und Inhaltskorrekturen

**SDK- und Abhängigkeitsupdates**
Leere `openai`-Version auf `^4.95.0` gesetzt
SDK von `^1.8.0` auf `>=1.26.0` aktualisiert
MCP-Version-Pins auf `>=1.26.0` aktualisiert

**Codekorrekturen**
Ungültiges Modell `gpt-4o-mini` zu `gpt-4.1-mini` korrigiert

**Inhaltskorrekturen**
Defekten Link `READMEmd` → `README.md` repariert, Kursüberschrift `Module 1-3` → `Module 0-3` korrigiert, Groß-/Kleinschreibungsfehler im Pfad behoben
Beschädigten doppelten Inhalt von Fallstudie 5 entfernt

**Verbesserungen für Einsteiger**
Richtige Einführung, Lernziele und Voraussetzungen für Einsteiger hinzugefügt

#### Kursupdates

**Haupt-README.md**
- Einträge 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protokollfunktionen) zur Curriculum-Tabelle hinzugefügt

**Modul README-Dateien**
Lektionen 12 und 13 zur Unterrichtsliste hinzugefügt
Abschnitt Praktische Leitfäden mit Pagination-Link hinzugefügt
Lektionen 5.15 (Custom Transport) und 5.16 (Protocol Features) hinzugefügt

**study_guide.md**
- Mindmap um alle neuen Themen erweitert: MCP Hosts Setup, MCP Inspector, Pagination-Strategien, Deep Dive zu Protokollfunktionen

## 28. Januar 2026

### MCP-Spezifikation 2025-11-25 Compliance-Prüfung

#### Kernkonzepte-Erweiterung (01-CoreConcepts/)
- **Neue Client-Primitiv - Roots**: Hinzugefügte umfassende Dokumentation zur Roots Client-Primitiv, die es Servern ermöglicht, Dateisystem-Grenzen und Zugriffsrechte zu verstehen
- **Tool-Anmerkungen**: Dokumentation zu Tool-Verhaltensanmerkungen (`readOnlyHint`, `destructiveHint`) für bessere Entscheidungen bei Tool-Ausführungen hinzugefügt
- **Tool-Aufrufe beim Sampling**: Sampling-Dokumentation aktualisiert, um `tools` und `toolChoice` Parameter für modellgesteuerte Toolaufrufe während Sampling-Anfragen einzubeziehen
- **URL Mode Elicitation**: Dokumentation zur URL-basierten Auslösung für serverinitiierte externe Webinteraktionen hinzugefügt
- **Tasks (experimentell)**: Neuer Abschnitt zur experimentellen Tasks-Funktion für dauerhafte Ausführungs-Wrapper und verzögerte Ergebnisabfrage hinzugefügt

- **Icons Unterstützung**: Es wurde vermerkt, dass Tools, Ressourcen, Ressourcenvorlagen und Prompts jetzt Symbole als zusätzliche Metadaten enthalten können

#### Aktualisierungen der Dokumentation
- **README.md**: MCP-Spezifikation 2025-11-25 Versionsreferenz und erklärung der datumsbasierten Versionierung hinzugefügt
- **study_guide.md**: Aktualisierte Lehrplanübersicht zur Einbeziehung von Aufgaben und Tool-Anmerkungen im Abschnitt Kernkonzepte; aktualisierter Dokumentzeitstempel

#### Überprüfung der Spezifikationskonformität
- **Protokollversion**: Alle Dokumentationsnachweise wurden mit der aktuellen MCP-Spezifikation 2025-11-25 abgeglichen
- **Architekturausrichtung**: Bestätigung der Genauigkeit der Dokumentation der Zwei-Schichten-Architektur (Daten-Schicht + Transport-Schicht)
- **Primitiven Dokumentation**: Validierung der Server-Primitiven (Ressourcen, Prompts, Tools) und Client-Primitiven (Sampling, Elicitation, Logging, Roots)
- **Transportmechanismen**: Verifizierung der Genauigkeit der Dokumentation zu STDIO- und streambarem HTTP-Transport
- **Sicherheitshinweise**: Bestätigung der Übereinstimmung mit der aktuellen MCP Security Best Practices-Dokumentation

#### Wichtigste dokumentierte MCP-Features 2025-11-25
- **OpenID Connect Discovery**: Auth-Server-Erkennung über OIDC
- **OAuth Client ID Metadokumente**: Empfohlenes Client-Registrierungsverfahren
- **JSON Schema 2020-12**: Standarddialekt für MCP-Schemadefinitionen
- **SDK-Stufensystem**: Formalisierte Anforderungen für SDK-Feature-Support und Wartung
- **Governance-Struktur**: Formalisierte Arbeitsgruppen und Interessengruppen in der MCP-Governance

### Großes Update der Sicherheitsdokumentation (02-Security/)

#### Integration des MCP Security Summit Workshops (Sherpa)
- **Neue praktische Schulungsressource**: Umfassende Integration mit dem [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in sämtlicher Sicherheitsdokumentation hinzugefügt
- **Expeditionsroutenabdeckung**: Dokumentiert den vollständigen Fortschritt von Camp zu Camp von Basislager bis Gipfel
- **OWASP-Ausrichtung**: Alle Sicherheitshinweise beziehen sich jetzt auf die Risiken des OWASP MCP Azure Security Guide

#### OWASP MCP Top 10 Integration
- **Neuer Abschnitt**: Tabelle zu den OWASP MCP Top 10 Sicherheitsrisiken mit Azure-Minderungen zur Hauptsicherheits-README hinzugefügt
- **Risikobasierte Dokumentation**: Aktualisierung von mcp-security-controls-2025.md mit OWASP MCP Risiko-Verweisen zu jedem Sicherheitsbereich
- **Referenzarchitektur**: Verlinkung auf OWASP MCP Azure Security Guide Referenzarchitektur und Implementierungsmuster

#### Aktualisierte Sicherheitsdateien
- **README.md**: Sherpa Workshop Übersicht, Expeditionsroutentabelle, Zusammenfassung der OWASP MCP Top 10 Risiken und Abschnitt für praktische Schulungen hinzugefügt
- **mcp-security-controls-2025.md**: Header auf Februar 2026 aktualisiert, OWASP-Risikoverweise (MCP01-MCP08) hinzugefügt, Versionsinkonsistenz behoben
- **mcp-security-best-practices-2025.md**: Sherpa- und OWASP-Ressourcenabschnitt hinzugefügt, Zeitstempel aktualisiert
- **mcp-best-practices.md**: Abschnitt für praktische Schulungen mit Sherpa- und OWASP-Links hinzugefügt
- **azure-content-safety-implementation.md**: OWASP MCP06-Bezug, Sherpa Camp 3 Ausrichtung und zusätzlicher Ressourcenabschnitt hinzugefügt

#### Neue Ressourcen-Links hinzugefügt
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Einzelne OWASP MCP-Risikoseiten (MCP01-MCP10)

### Lehrplanweite MCP Spezifikation 2025-11-25 Ausrichtung

#### Modul 03 - Erste Schritte
- **SDK-Dokumentation**: Go SDK zur offiziellen SDK-Liste hinzugefügt; alle SDK-Verweise auf MCP-Spezifikation 2025-11-25 abgestimmt
- **Transporterklärung**: Beschreibungen zu STDIO- und HTTP-Streaming-Transport mit expliziten Spezifikationsverweisen aktualisiert

#### Modul 04 - Praktische Umsetzung
- **SDK Updates**: Go SDK hinzugefügt; SDK-Liste mit Spezifikationsversionsverweis aktualisiert
- **Autorisierungsspezifikation**: Link zur MCP Authorization Spezifikation auf aktuelle Version 2025-11-25 aktualisiert

#### Modul 05 - Fortgeschrittene Themen
- **Neue Features**: Hinweis zu neuen MCP Specification 2025-11-25 Features (Aufgaben, Tool-Anmerkungen, URL-Modus Elicitation, Roots) hinzugefügt
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa Workshop Links zu zusätzlichen Referenzen hinzugefügt

#### Modul 06 - Community Beiträge
- **SDK-Liste**: Swift- und Rust-SDKs hinzugefügt; Spezifikationslink auf Version 2025-11-25 aktualisiert
- **Spezifikationsverweis**: MCP Spezifikationslink auf direkte Spezifikations-URL aktualisiert

#### Modul 07 - Erfahrungen aus der frühen Nutzung
- **Ressourcen-Updates**: MCP Specification 2025-11-25 Link und OWASP MCP Top 10 zu zusätzlichen Ressourcen hinzugefügt

#### Modul 08 - Best Practices
- **Versionsangabe**: MCP Spezifikationsverweis auf 2025-11-25 aktualisiert
- **Sicherheitsressourcen**: OWASP MCP Top 10 und Sherpa Workshop zu zusätzlichen Referenzen hinzugefügt

#### Modul 10 - KI-Workflows optimieren
- **Badge-Update**: MCP-Versions-Badge von SDK-Version (1.9.3) auf Spezifikationsversion (2025-11-25) geändert
- **Ressourcenlinks**: MCP Spezifikationslink aktualisiert; OWASP MCP Top 10 hinzugefügt

#### Modul 11 - MCP Server Hands-On Labs
- **Spezifikationsverweis**: MCP Spezifikationslink auf Version 2025-11-25 aktualisiert
- **Sicherheitsressourcen**: OWASP MCP Top 10 zu offiziellen Ressourcen hinzugefügt

## 18. Dezember 2025

### Sicherheitsdokumentations-Update - MCP Spezifikation 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Versionsupdate der Spezifikation
- **Protokollversions-Update**: Aktualisiert zur Bezugnahme auf die neueste MCP Spezifikation 2025-11-25 (veröffentlicht am 25. November 2025)
  - Alle Versionsverweise von 2025-06-18 auf 2025-11-25 aktualisiert
  - Aktualisierung der Dokumentdatum-Verweise von 18. August 2025 auf 18. Dezember 2025
  - Überprüfung, dass alle Spezifikations-URLs auf aktuelle Dokumentation verweisen
- **Inhaltsvalidierung**: Umfassende Validierung der Sicherheits-Best-Practices gegen neueste Standards
  - **Microsoft-Sicherheitslösungen**: Überprüft aktuelle Terminologie und Links für Prompt Shields (früher "Jailbreak Risikoerkennung"), Azure Content Safety, Microsoft Entra ID und Azure Key Vault
  - **OAuth 2.1 Sicherheit**: Bestätigung der Übereinstimmung mit aktuellen OAuth Sicherheits-Best-Practices
  - **OWASP Standards**: Validierung, dass die OWASP Top 10 für LLMs aktuell sind
  - **Azure-Dienste**: Überprüfung aller Microsoft Azure Dokumentations-Links und Best Practices
- **Standardausrichtung**: Alle referenzierten Sicherheitsstandards als aktuell bestätigt
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure Sicherheits- und Compliance-Frameworks
- **Implementierungsressourcen**: Validierung aller Links und Ressourcen zu Implementierungsanleitungen
  - Azure API Management Authentifizierungsmuster
  - Microsoft Entra ID Integrationsanleitungen
  - Azure Key Vault Geheimnisverwaltung
  - DevSecOps-Pipelines und Überwachungslösungen

### Qualitätssicherung der Dokumentation
- **Spezifikationskonformität**: Sicherstellung, dass alle obligatorischen MCP-Sicherheitsanforderungen (MUST/MUST NOT) mit der neuesten Spezifikation übereinstimmen
- **Aktualität der Ressourcen**: Überprüfung aller externen Links zu Microsoft-Dokumentationen, Sicherheitsstandards und Implementierungsanleitungen
- **Best-Practices-Abdeckung**: Bestätigung einer umfassenden Abdeckung zu Authentifizierung, Autorisierung, KI-spezifischen Bedrohungen, Lieferkettensicherheit und Unternehmensmustern

## 6. Oktober 2025

### Erweiterung des Abschnitts "Erste Schritte" – Fortgeschrittene Servernutzung & einfache Authentifizierung

#### Fortgeschrittene Servernutzung (03-GettingStarted/10-advanced)
- **Neues Kapitel hinzugefügt**: Einführung eines umfassenden Leitfadens zur fortgeschrittenen MCP-Servernutzung, der sowohl reguläre als auch Low-Level Server-Architekturen abdeckt.
  - **Regulärer vs. Low-Level Server**: Detaillierter Vergleich und Codebeispiele in Python und TypeScript für beide Ansätze.
  - **Handler-basierte Gestaltung**: Erklärung des handler-basierten Tool-/Ressourcen-/Prompt-Managements für skalierbare, flexible Serverimplementierungen.
  - **Praktische Muster**: Praxisbeispiele, bei denen Low-Level-Server-Muster für erweiterte Features und Architekturen von Vorteil sind.

#### Einfache Authentifizierung (03-GettingStarted/11-simple-auth)
- **Neues Kapitel hinzugefügt**: Schritt-für-Schritt-Anleitung zur Implementierung einfacher Authentifizierung in MCP-Servern.
  - **Auth-Konzepte**: Klare Erklärung von Authentifizierung vs. Autorisierung und Umgang mit Zugangsdaten.
  - **Basic Auth Implementierung**: Middleware-basierte Authentifizierungsmuster in Python (Starlette) und TypeScript (Express), mit Codebeispielen.
  - **Fortschritt zur erweiterten Sicherheit**: Anleitung für den Übergang von einfacher Authentifizierung zu OAuth 2.1 und RBAC, mit Verweisen auf fortgeschrittene Sicherheitsmodule.

Diese Ergänzungen bieten praktische, praxisnahe Orientierung zum Aufbau robusterer, sicherer und flexibler MCP-Serverimplementierungen, die Grundlagenkonzepte mit fortgeschrittenen Produktionsmustern verbinden.

## 29. September 2025

### MCP Server-Datenbankintegrations-Labs – Umfassender praxisnaher Lernpfad

#### 11-MCPServerHandsOnLabs – Neuer kompletter Lehrplan zur Datenbankintegration
- **Vollständiger 13-Lab Lernpfad**: Umfassender praxisnaher Lehrplan zum Aufbau produktionsbereiter MCP-Server mit PostgreSQL-Datenbankintegration hinzugefügt
  - **Praxisbeispiel**: Use Case Zava Retail Analytics mit Enterprise-Grade-Mustern
  - **Strukturierter Lernfortschritt**:
    - **Labs 00-03: Grundlagen** – Einführung, Kernarchitektur, Sicherheit & Multi-Tenancy, Einrichtung der Umgebung
    - **Labs 04-06: Aufbau des MCP Servers** – Datenbankdesign & Schema, MCP Server Implementierung, Toolentwicklung  
    - **Labs 07-09: Erweiterte Funktionen** – Semantische Suche Integration, Testen & Debugging, VS Code Integration
    - **Labs 10-12: Produktion & Best Practices** – Bereitstellungsstrategien, Überwachung & Beobachtbarkeit, Best Practices & Optimierung
  - **Enterprise-Technologien**: FastMCP Framework, PostgreSQL mit pgvector, Azure OpenAI Embeddings, Azure Container Apps, Application Insights
  - **Erweiterte Features**: Row Level Security (RLS), semantische Suche, Multi-Tenant Datenzugriff, Vektor-Embeddings, Echtzeit-Monitoring

#### Standardisierung der Terminologie – Umwandlung von Modulen in Labs
- **Umfassendes Update der Dokumentation**: Systematische Aktualisierung aller README-Dateien in 11-MCPServerHandsOnLabs zur Verwendung des Begriffs "Lab" anstelle von "Modul"
  - **Abschnittsüberschriften**: Aktualisierung von "Was dieses Modul abdeckt" zu "Was dieses Lab abdeckt" in allen 13 Labs
  - **Inhaltsbeschreibung**: Änderung von "Dieses Modul bietet..." zu "Dieses Lab bietet..." im gesamten Dokument
  - **Lernziele**: Aktualisierung von "Am Ende dieses Moduls..." zu "Am Ende dieses Labs..."
  - **Navigationslinks**: Alle Verweise "Modul XX:" in Querverweisen und Navigation zu "Lab XX:" geändert
  - **Abschlussverfolgung**: Änderung von "Nach Abschluss dieses Moduls..." zu "Nach Abschluss dieses Labs..."
  - **Technische Verweise erhalten**: Python-Modulverweise in Konfigurationsdateien (z.B. `"module": "mcp_server.main"`) beibehalten

#### Erweiterung des Study Guide (study_guide.md)
- **Visuelle Lehrplanübersicht**: Neuer Abschnitt "11. Database Integration Labs" mit umfassender Visualisierung der Lab-Struktur hinzugefügt
- **Repository-Übersicht**: Von zehn auf elf Hauptabschnitte erweitert mit detaillierter Beschreibung von 11-MCPServerHandsOnLabs
- **Navigationshilfe**: Verbesserte Navigationsanweisungen für Abschnitte 00-11
- **Technologie-Abdeckung**: Details zu FastMCP, PostgreSQL, Azure-Diensteintegration hinzugefügt
- **Lernergebnisse**: Betonung der Entwicklung produktionsbereiter Server, Datenbankintegrationsmuster und Unternehmenssicherheit

#### Verbesserung der Haupt-README-Struktur
- **Lab-basierte Terminologie**: Haupt-README.md in 11-MCPServerHandsOnLabs aktualisiert zur konsequenten Verwendung der "Lab"-Struktur
- **Organisation des Lernpfads**: Klare Abfolge von Grundlagen über fortgeschrittene Umsetzung bis zur Produktionsbereitstellung
- **Praxisorientierung**: Betonung praktischen, praxisnahen Lernens mit Enterprise-Mustern und Technologien

### Qualitäts- und Konsistenzverbesserungen der Dokumentation
- **Praxisorientierung hervorgehoben**: Verstärkte Betonung des praktischen, lab-basierten Ansatzes
- **Fokus auf Unternehmungsmuster**: Hervorhebung produktionsbereiter Implementationen und Unternehmenssicherheitsaspekte
- **Technologie-Integration**: Umfassende Abdeckung moderner Azure-Dienste und KI-Integrationsmuster
- **Lernfortschritt**: Klar strukturierter Pfad von Basiskenntnissen bis zur Produktion

## 26. September 2025

### Erweiterung der Fallstudien – GitHub MCP Registry Integration

#### Fallstudien (09-CaseStudy/) – Fokus auf Ökosystementwicklung
- **README.md**: Große Erweiterung mit umfassender Fallstudie zur GitHub MCP Registry
  - **GitHub MCP Registry Fallstudie**: Neue ausführliche Fallstudie zur Einführung der GitHub MCP Registry im September 2025
    - **Problemanalyse**: Detaillierte Untersuchung fragmentierter MCP-Servererkennung und Deployment-Herausforderungen
    - **Lösungsarchitektur**: GitHubs zentraler Registry-Ansatz mit Ein-Klick VS Code Installation
    - **Geschäftlicher Einfluss**: Messbare Verbesserungen bei Entwickler-Onboarding und Produktivität
    - **Strategischer Wert**: Fokus auf modulare Agent-Bereitstellung und Tool-übergreifende Interoperabilität
    - **Ökosystem-Entwicklung**: Positionierung als grundlegende Plattform für agentenbasierte Integration
  - **Verbesserte Fallstudienstruktur**: Alle sieben Fallstudien mit einheitlichem Format und umfassenden Beschreibungen aktualisiert
    - Azure AI Travel Agents: Schwerpunkt Multi-Agenten-Orchestrierung
    - Azure DevOps Integration: Fokus auf Workflow-Automatisierung
    - Echtzeit-Dokumentenabruf: Python-Konsolenclient-Implementierung
    - Interaktiver Studienplan-Generator: Chainlit konversationelle Web-App

    - Dokumentation im Editor: VS Code- und GitHub Copilot-Integration
    - Azure API Management: Muster für Unternehmens-API-Integration
    - GitHub MCP-Registry: Ökosystementwicklung und Community-Plattform
  - **Umfassendes Fazit**: Neu geschriebener Abschlussteil mit sieben Fallstudien, die mehrere MCP-Implementierungsdimensionen abdecken
    - Unternehmensintegration, Multi-Agenten-Orchestrierung, Entwicklerproduktivität
    - Ökosystementwicklung, Kategorisierung von Bildungsanwendungen
    - Verbesserte Einblicke in Architekturpatterns, Implementierungsstrategien und bewährte Verfahren
    - Betonung von MCP als ausgereiftes, produktionsreifes Protokoll

#### Aktualisierungen des Studienleitfadens (study_guide.md)
- **Visuelle Curriculum-Karte**: Aktualisierte Mindmap zur Aufnahme der GitHub MCP-Registry im Abschnitt Fallstudien
- **Fallstudienbeschreibung**: Von generischen Beschreibungen zu detaillierter Aufschlüsselung von sieben umfassenden Fallstudien verbessert
- **Repository-Struktur**: Aktualisierter Abschnitt 10 zur umfassenden Abdeckung der Fallstudien mit spezifischen Implementierungsdetails
- **Changelog-Integration**: Eintrag vom 26. September 2025 hinzugefügt, der die Aufnahme der GitHub MCP-Registry und Verbesserungen der Fallstudien dokumentiert
- **Datumsaktualisierungen**: Fußzeilentimestamp auf die neueste Überarbeitung (26. September 2025) aktualisiert

### Verbesserungen der Dokumentationsqualität
- **Konsistenzsteigerung**: Standardisierte Formatierung und Struktur der Fallstudien über alle sieben Beispiele hinweg
- **Umfassende Abdeckung**: Fallstudien umfassen nun Unternehmens-, Entwicklerproduktivitäts- und Ökosystementwicklungsszenarien
- **Strategische Positionierung**: Verstärkter Fokus auf MCP als Grundlage für die Bereitstellung agentischer Systeme
- **Ressourcenintegration**: Aktualisierte zusätzliche Ressourcen zur Einbindung des Links zur GitHub MCP-Registry

## 15. September 2025

### Erweiterung fortgeschrittener Themen – Benutzerdefinierte Transports & Kontext-Engineering

#### MCP-Benutzerdefinierte Transports (05-AdvancedTopics/mcp-transport/) – Neuer fortgeschrittener Implementierungsleitfaden
- **README.md**: Vollständiger Implementierungsleitfaden für benutzerdefinierte MCP-Transportmechanismen
  - **Azure Event Grid Transport**: Umfassende serverlose ereignisgesteuerte Transportimplementierung
    - C#, TypeScript- und Python-Beispiele mit Integration von Azure Functions
    - Ereignisgesteuerte Architekturpatterns für skalierbare MCP-Lösungen
    - Webhook-Empfänger und Push-basierte Nachrichtenverarbeitung
  - **Azure Event Hubs Transport**: Hochdurchsatz-Streaming-Transportimplementierung
    - Echtzeit-Streaming-Fähigkeiten für latenzarme Szenarien
    - Partitionierungsstrategien und Checkpoint-Verwaltung
    - Nachrichtenbündelung und Leistungsoptimierung
  - **Enterprise-Integrationsmuster**: Produktionsreife Architekturbeispiele
    - Verteilte MCP-Verarbeitung über mehrere Azure Functions
    - Hybride Transportarchitekturen, die mehrere Transporttypen kombinieren
    - Nachrichtenhaltbarkeit, Zuverlässigkeit und Fehlerbehandlungsstrategien
  - **Sicherheit & Überwachung**: Azure Key Vault-Integration und Observability-Patterns
    - Authentifizierung mit Managed Identity und Zugriffsrechte nach dem Prinzip der geringsten Berechtigung
    - Application Insights-Telemetrie und Leistungsüberwachung
    - Circuit-Breaker- und Fehlertoleranz-Patterns
  - **Testframeworks**: Umfassende Teststrategien für benutzerdefinierte Transports
    - Unit-Tests mit Test-Doubles und Mocking-Frameworks
    - Integrationstests mit Azure Test Containers
    - Überlegungen zu Leistungs- und Lasttests

#### Kontext-Engineering (05-AdvancedTopics/mcp-contextengineering/) – Aufkommende KI-Disziplin
- **README.md**: Umfassende Erkundung von Kontext-Engineering als aufstrebendes Feld
  - **Kernprinzipien**: Vollständiges Teilen von Kontext, Bewusstsein für Handlungsentscheidungen und Verwaltung des Kontextfensters
  - **MCP-Protokollabgleich**: Wie das MCP-Design Herausforderungen des Kontext-Engineerings adressiert
    - Kontextfensterbeschränkungen und progressive Ladestrategien
    - Relevanzbestimmung und dynamische Kontextabrufe
    - Multimodale Kontextbehandlung und Sicherheitsüberlegungen
  - **Implementierungsansätze**: Ein-Thread- vs. Multi-Agenten-Architekturen
    - Techniken zur Kontextzerlegung (Chunking) und Priorisierung
    - Progressive Kontextladung und Kompressionsstrategien
    - Schichtweise Kontextansätze und Abrufoptimierung
  - **Messrahmen**: Aufkommende Metriken zur Bewertung der Kontexteffektivität
    - Eingabeeffizienz, Leistung, Qualität und Nutzererfahrungsüberlegungen
    - Experimentelle Ansätze zur Kontextoptimierung
    - Ausfallanalyse und Verbesserungsmethoden

#### Updates zur Curriculum-Navigation (README.md)
- **Verbesserte Modulstruktur**: aktualisierte Curriculum-Tabelle zur Einbindung neuer fortgeschrittener Themen
  - Hinzugefügt: Kontext-Engineering (5.14) und Benutzerdefinierter Transport (5.15)
  - Einheitliche Formatierung und Navigationslinks über alle Module hinweg
  - Aktualisierte Beschreibungen zur Wiedergabe des aktuellen Inhaltsumfangs

### Verbesserungen der Verzeichnisstruktur
- **Namensstandardisierung**: Umbenennung von „mcp transport“ zu „mcp-transport“ für Konsistenz mit anderen Ordnern fortgeschrittener Themen
- **Inhaltsorganisation**: Alle 05-AdvancedTopics-Ordner folgen jetzt dem einheitlichen Namensmuster (mcp-[Thema])

### Verbesserungen der Dokumentationsqualität
- **Ausrichtung an MCP-Spezifikation**: Alle neuen Inhalte verweisen auf die aktuelle MCP-Spezifikation 2025-06-18
- **Mehrsprachige Beispiele**: Umfassende Codebeispiele in C#, TypeScript und Python
- **Unternehmensfokus**: Produktionsreife Muster und Azure-Cloud-Integration durchgehend
- **Visuelle Dokumentation**: Mermaid-Diagramme zur Architektur- und Ablaufvisualisierung

## 18. August 2025

### Umfassendes Update der Dokumentation – MCP-Standards 2025-06-18

#### MCP-Sicherheitsbest Practices (02-Security/) – Komplette Modernisierung
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Komplettüberarbeitung im Einklang mit MCP-Spezifikation 2025-06-18
  - **Verbindliche Anforderungen**: Hinzufügen expliziter MUSS / DARF NICHT Anforderungen aus offizieller Spezifikation mit klaren visuellen Markierungen
  - **12 Kern-Sicherheitspraktiken**: Umstrukturierung von 15-Punkte-Liste zu umfassenden Sicherheitsdomänen
    - Token-Sicherheit & Authentifizierung mit Integration externer Identitätsanbieter
    - Sitzungsverwaltung & Transportsicherheit mit kryptographischen Anforderungen
    - KI-spezifischer Bedrohungsschutz mit Microsoft Prompt Shields-Integration
    - Zugriffskontrolle & Berechtigungen mit Prinzip der geringsten Berechtigung
    - Inhaltssicherheit & Überwachung mit Azure Content Safety-Integration
    - Lieferkettensicherheit mit umfassender Komponentenverifikation
    - OAuth-Sicherheit & Schutz vor Confused-Deputy-Angriffen mit PKCE-Implementierung
    - Vorfallreaktion & Wiederherstellung mit automatisierten Fähigkeiten
    - Compliance & Governance mit regulatorischer Ausrichtung
    - Fortschrittliche Sicherheitskontrollen mit Zero-Trust-Architektur
    - Integration des Microsoft-Sicherheits-Ökosystems mit umfassenden Lösungen
    - Kontinuierliche Sicherheitsevolution mit adaptiven Praktiken
  - **Microsoft-Sicherheitslösungen**: Verbesserte Integrationsanleitungen für Prompt Shields, Azure Content Safety, Entra ID und GitHub Advanced Security
  - **Implementierungsressourcen**: Kategorisierte umfassende Ressourcenlinks nach Offizieller MCP-Dokumentation, Microsoft-Sicherheitslösungen, Sicherheitsstandards und Implementierungsleitfäden

#### Fortgeschrittene Sicherheitskontrollen (02-Security/) – Unternehmensimplementierung
- **MCP-SECURITY-CONTROLS-2025.md**: Komplette Überarbeitung mit sicherheitsrahmen für Unternehmen
  - **9 umfassende Sicherheitsdomänen**: Erweiterung von Basis-Steuerungen zum detaillierten Unternehmensrahmen
    - Erweiterte Authentifizierung & Autorisierung mit Microsoft Entra ID-Integration
    - Token-Sicherheit & Anti-Passthrough-Steuerungen mit umfassender Validierung
    - Sitzungssicherheitskontrollen mit Schutz vor Hijacking
    - KI-spezifische Sicherheitskontrollen mit Schutz vor Prompt-Injection und Tool-Vergiftung
    - Confused-Deputy-Angriffsschutz mit OAuth-Proxy-Sicherheit
    - Sicherheit bei der Werkzeugaussführung mit Sandboxing und Isolation
    - Lieferkettensicherheitskontrollen mit Abhängigkeitsprüfung
    - Überwachungs- & Detektionssteuerungen mit SIEM-Integration
    - Vorfallreaktion & Wiederherstellung mit automatisierten Fähigkeiten
  - **Implementierungsbeispiele**: Hinzugefügte detaillierte YAML-Konfigurationsblöcke und Codebeispiele
  - **Integration von Microsoft-Lösungen**: Umfassende Abdeckung von Azure-Sicherheitsdiensten, GitHub Advanced Security und Unternehmensidentitätsverwaltung

#### Sicherheit fortgeschrittener Themen (05-AdvancedTopics/mcp-security/) – Produktionsreife Implementierung
- **README.md**: Komplette Neufassung für unternehmensweite Sicherheitsimplementierung
  - **Aktueller Spezifikationsabgleich**: Aktualisiert auf MCP-Spezifikation 2025-06-18 mit verbindlichen Sicherheitsanforderungen
  - **Erweiterte Authentifizierung**: Microsoft Entra ID-Integration mit umfangreichen .NET- und Java Spring Security-Beispielen
  - **KI-Sicherheitsintegration**: Microsoft Prompt Shields- und Azure Content Safety-Implementierung mit detaillierten Python-Beispielen
  - **Erweiterte Bedrohungsminderung**: Umfassende Implementierungsbeispiele für
    - Schutz vor Confused-Deputy-Angriffen mit PKCE und Benutzerzustimmungsvalidierung
    - Verhinderung von Token-Passthrough mit Audience-Validierung und sicherem Token-Management
    - Verhinderung von Sitzungs-Hijacking mit kryptographischer Bindung und Verhaltensanalyse
  - **Unternehmenssicherheit-Integration**: Azure Application Insights-Überwachung, Bedrohungserkennungs-Pipelines und Lieferkettensicherheit
  - **Implementierungs-Checkliste**: Klare verbindliche vs. empfohlene Sicherheitskontrollen mit Vorteilen durch Microsoft-Sicherheits-Ökosystem

### Dokumentationsqualität & Standardsausrichtung
- **Spezifikationsverweise**: Alle Verweise auf aktuelle MCP-Spezifikation 2025-06-18 aktualisiert
- **Microsoft-Sicherheits-Ökosystem**: Verbesserte Integrationsanleitungen in allen Sicherheitsdokumentationen
- **Praktische Implementierung**: Hinzugefügte detaillierte Codebeispiele in .NET, Java und Python mit Unternehmensmustern
- **Ressourcenorganisation**: Umfassende Kategorisierung offizieller Dokumentationen, Sicherheitsstandards und Implementierungsleitfäden
- **Visuelle Indikatoren**: Klare Kennzeichnung verpflichtender Anforderungen gegenüber empfohlenen Praktiken


#### Kernkonzepte (01-CoreConcepts/) – Komplette Modernisierung
- **Protokollversion-Update**: Aktualisierung auf Referenz der aktuellen MCP-Spezifikation 2025-06-18 mit datumsbasierter Versionierung (YYYY-MM-DD-Format)
- **Architekturverfeinerung**: Verbesserte Beschreibungen von Hosts, Clients und Servern zur Darstellung aktueller MCP-Architekturpatterns
  - Hosts jetzt klar definiert als KI-Anwendungen, die mehrere MCP-Clientverbindungen koordinieren
  - Clients beschrieben als Protokollanschlüsse mit Ein-zu-eins-Serverbeziehungen
  - Server weiterentwickelt mit lokalen vs. Remote-Bereitstellungsszenarien
- **Primitive Umstrukturierung**: Komplette Überarbeitung der Server- und Client-Primitives
  - Server-Primitives: Ressourcen (Datenquellen), Prompts (Vorlagen), Werkzeuge (ausführbare Funktionen) mit detaillierten Erklärungen und Beispielen
  - Client-Primitives: Sampling (LLM-Vervollständigungen), Elicitation (Benutzereingabe), Logging (Debugging/Überwachung)
  - Aktualisiert mit aktuellen Entdeckungs- (`*/list`), Abruf- (`*/get`) und Ausführungs- (`*/call`) Methoden-Patterns
- **Protokollarchitektur**: Einführung eines Zwei-Schichten-Architekturmodells
  - Datenschicht: JSON-RPC 2.0-Grundlage mit Lebenszyklusverwaltung und Primitives
  - Transportschicht: STDIO (lokal) und Streamable HTTP mit SSE (remote) Transportmechanismen
- **Sicherheitsrahmen**: Umfassende Sicherheitsprinzipien einschließlich expliziter Benutzerzustimmung, Datenschutz, Ausführungssicherheit von Werkzeugen und Transportschichtsicherheit
- **Kommunikationsmuster**: Aktuelle Protokollnachrichten zeigen Initialisierung-, Entdeckungs-, Ausführungs- und Benachrichtigungsabläufe
- **Codebeispiele**: Auffrischung der mehrsprachigen Beispiele (.NET, Java, Python, JavaScript), um aktuelle MCP SDK-Patterns widerzuspiegeln

#### Sicherheit (02-Security/) – Umfassende Sicherheitsüberarbeitung  
- **Standardausrichtung**: Vollständige Ausrichtung an den Sicherheitsanforderungen der MCP-Spezifikation 2025-06-18
- **Authentifizierungsevolution**: Dokumentierte Entwicklung von eigenen OAuth-Servern zur Delegation an externe Identitätsanbieter (Microsoft Entra ID)
- **KI-spezifische Bedrohungsanalyse**: Verbesserte Abdeckung moderner KI-Angriffsvektoren
  - Detaillierte Angriffsszenarien für Prompt Injection mit realen Beispielen
  - Mechanismen der Werkzeugvergiftung und „Rug Pull“-Angriffsmuster
  - Kontextfenstervergiftung und Modellverwirrungsangriffe
- **Microsoft KI-Sicherheitslösungen**: Umfassende Abdeckung des Microsoft-Sicherheits-Ökosystems
  - AI Prompt Shields mit fortschrittlicher Erkennung, Hervorhebung und Begrenzungstechniken
  - Azure Content Safety-Integrationsmuster
  - GitHub Advanced Security zum Schutz der Lieferkette
- **Erweiterte Bedrohungsminderung**: Detaillierte Sicherheitskontrollen für
  - Sitzungs-Hijacking mit MCP-spezifischen Angriffsszenarien und kryptographischen Sitzungs-ID-Anforderungen
  - Confused-Deputy-Probleme in MCP-Proxy-Szenarien mit expliziten Zustimmungserfordernissen
  - Token-Passthrough-Schwachstellen mit obligatorischen Validierungskontrollen
- **Lieferkettensicherheit**: Erweiterte KI-Lieferkettenabdeckung einschließlich Foundation-Modellen, Embeddings-Diensten, Kontextanbietern und Drittanbieter-APIs
- **Foundation-Sicherheit**: Verbesserte Integration mit Unternehmenssicherheitsmustern einschließlich Zero-Trust-Architektur und Microsoft-Sicherheits-Ökosystem
- **Ressourcenorganisation**: Kategorisierte umfassende Ressourcenlinks nach Typ (Offizielle Docs, Standards, Forschung, Microsoft-Lösungen, Implementierungsleitfäden)

### Verbesserungen der Dokumentationsqualität
- **Strukturierte Lernziele**: Verbesserte Lernziele mit spezifischen, umsetzbaren Ergebnissen
- **Querverweise**: Hinzugefügte Links zwischen verwandten Sicherheits- und Kernkonzeptthemen
- **Aktuelle Informationen**: Alle Datumsverweise und Spezifikationslinks auf aktuelle Standards aktualisiert
- **Implementierungsanleitungen**: Hinzugefügte spezifische, umsetzbare Implementierungsleitlinien in beiden Abschnitten

## 16. Juli 2025

### README und Navigationsverbesserungen
- Curriculum-Navigation in README.md komplett neu gestaltet
- `<details>`-Tags wurden durch ein zugänglicheres tabellenbasiertes Format ersetzt
- Alternative Layoutoptionen im neuen Ordner „alternative_layouts“ erstellt
- Beispiele für kartenbasiertes, registerkarten-artiges und Akkordeon-navigationsdesign hinzugefügt
- Aktualisierung des Repository-Strukturabschnitts zur Aufnahme aller neuesten Dateien
- Verbesserung des Abschnitts „Wie man dieses Curriculum verwendet“ mit klaren Empfehlungen
- Aktualisierte MCP-Spezifikationslinks zeigen auf korrekte URLs
- Kontext-Engineering-Abschnitt (5.14) zur Curriculum-Struktur hinzugefügt

### Aktualisierungen des Studienleitfadens
- Studienleitfaden komplett überarbeitet, um mit aktueller Repository-Struktur übereinzustimmen
- Neue Abschnitte für MCP-Clients und Tools sowie populäre MCP-Server hinzugefügt
- Visuelle Curriculum-Karte aktualisiert, um alle Themen genau widerzuspiegeln
- Beschreibungen fortgeschrittener Themen erweitert, um alle Spezialgebiete abzudecken
- Abschnitt Fallstudien aktualisiert, um tatsächliche Beispiele darzustellen
- Dieses umfassende Changelog hinzugefügt

### Community-Beiträge (06-CommunityContributions/)
- Ausführliche Informationen zu MCP-Servern für Bildgenerierung hinzugefügt
- Umfassender Abschnitt zur Nutzung von Claude in VSCode hinzugefügt
- Anweisungen zur Einrichtung und Nutzung des Cline-Terminalclients hinzugefügt
- MCP-Client-Abschnitt aktualisiert, um alle populären Clientoptionen einzubeziehen
- Beitragende Beispiele mit genaueren Codesamples verbessert

### Fortgeschrittene Themen (05-AdvancedTopics/)
- Alle spezialisierten Themenordner mit einheitlicher Namensgebung organisiert
- Materialien und Beispiele zum Kontext-Engineering hinzugefügt
- Dokumentation zur Integration von Foundry-Agent hinzugefügt
- Verbesserte Dokumentation zur Sicherheitsintegration von Entra ID

## 11. Juni 2025

### Erste Erstellung
- Erste Version des MCP für Anfänger-Curriculums veröffentlicht

- Grundstruktur für alle 10 Hauptabschnitte erstellt
- Visuelle Lehrplanübersicht für die Navigation implementiert
- Erste Beispielprojekte in mehreren Programmiersprachen hinzugefügt

### Erste Schritte (03-GettingStarted/)
- Erste Server-Implementierungsbeispiele erstellt
- Anleitung zur Client-Entwicklung hinzugefügt
- Anweisungen zur Integration von LLM-Clients eingefügt
- Dokumentation zur VS Code-Integration hinzugefügt
- Beispiele für Server-Sent Events (SSE) Server implementiert

### Kernkonzepte (01-CoreConcepts/)
- Detaillierte Erklärung der Client-Server-Architektur hinzugefügt
- Dokumentation zu wichtigen Protokollkomponenten erstellt
- Nachrichtenmuster im MCP dokumentiert

## 23. Mai 2025

### Repository-Struktur
- Repository mit grundlegender Ordnerstruktur initialisiert
- README-Dateien für jeden Hauptabschnitt erstellt
- Übersetzungsinfrastruktur eingerichtet
- Bildressourcen und Diagramme hinzugefügt

### Dokumentation
- Erste README.md mit Lehrplanübersicht erstellt
- CODE_OF_CONDUCT.md und SECURITY.md hinzugefügt
- SUPPORT.md mit Hilfestellungen eingerichtet
- Vorläufige Struktur für Studienleitfaden erstellt

## 15. April 2025

### Planung und Rahmenwerk
- Erste Planung für den MCP für Anfänger Lehrplan
- Lernziele und Zielgruppe definiert
- 10-Abschnitte-Struktur des Lehrplans skizziert
- Konzeptuelles Rahmenwerk für Beispiele und Fallstudien entwickelt
- Erste Prototyp-Beispiele für Schlüsselkonzepte erstellt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->