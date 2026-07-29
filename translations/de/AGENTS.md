# AGENTS.md

## Projektübersicht

**MCP für Anfänger** ist ein Open-Source-Lerncurriculum zum Erlernen des Model Context Protocol (MCP) – einem standardisierten Rahmenwerk für die Interaktion zwischen KI-Modellen und Client-Anwendungen. Dieses Repository stellt umfassende Lernmaterialien mit praxisnahen Codebeispielen in mehreren Programmiersprachen bereit.

### Schlüsseltechnologien

- **Programmiersprachen**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Datenbanken**: PostgreSQL mit pgvector-Erweiterung
- **Cloud-Plattformen**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build-Tools**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown mit automatischer Mehrsprachübersetzung (48+ Sprachen)

### Architektur

- **11 Kernmodule (00-11)**: Sequenzieller Lernpfad von Grundlagen bis zu Fortgeschrittenen-Themen
- **Hands-on Labs**: Praktische Übungen mit vollständigem Lösungscode in mehreren Sprachen
- **Beispielfprojekte**: Funktionierende MCP-Server- und Client-Implementierungen
- **Übersetzungssystem**: Automatisierter GitHub Actions Workflow für Mehrsprachunterstützung
- **Bildressourcen**: Zentralisiertes Bilderverzeichnis mit übersetzten Versionen

## Einrichtungskommandos

Dies ist ein dokumentationsfokussiertes Repository. Die meisten Setups erfolgen in einzelnen Beispielprojekten und Labs.

### Repository-Einrichtung

```bash
# Klonen Sie das Repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbeiten mit Beispielprojekten

Beispielprojekte befinden sich in:
- `03-GettingStarted/samples/` - Sprachspezifische Beispiele
- `03-GettingStarted/01-first-server/solution/` - Erste Server-Implementierungen
- `03-GettingStarted/02-client/solution/` - Client-Implementierungen
- `11-MCPServerHandsOnLabs/` - Umfassende Labs zur Datenbank-Integration

Jedes Beispielprojekt enthält eigene Einrichtungsanweisungen:

#### TypeScript/JavaScript-Projekte
```bash
cd <project-directory>
npm install
npm start
```

#### Python-Projekte
```bash
cd <project-directory>
pip install -r requirements.txt
# oder
pip install -e .
python main.py
```

#### Java-Projekte
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Entwicklungs-Workflow

### MCP 7-28 Bereitschaft

#### Checkliste zur Repository-Bereitschaft

- [x] **Klarheit für neue Mitwirkende**: Diese Datei definiert Repository-Zweck,
  Struktur, Beitragsregeln und Beispiel-Setup-Pfade.
- [x] **Build-/Test-/Lint-Kommandos mit exakten Flags**:
  - Repository-Dokumentation Lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Prüfung des Linkmusters in der Repository-Dokumentation:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validierung von TypeScript-Beispielen:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validierung von Python-Beispielen:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validierung von Java-Beispielen:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Ein realistischer Workflow, der zu einem MCP-Tool werden kann**:
  `validate_curriculum_change`
- [x] **Eingaben/Ausgaben sind explizit** (siehe Spezifikation unten).
- [x] **Berechtigungen und Fehlerfälle sind dokumentiert** (siehe Spezifikation unten).
- [x] **CI-Testbarkeit ist explizit** (deterministische Kommandos, explizite
  Exit-Codes und maschinenlesbare Ausgaben).

#### Kandidat MCP-Tool-Workflow: `validate_curriculum_change`

##### Ziel

Validierung von Curriculum-Dokumentationsänderungen und repräsentativem Beispielcode
vor dem Merge.

##### Eingaben

- `changed_paths: string[]` (erforderlich) – relative Pfade, die im PR geändert wurden.
- `run_docs_lint: boolean` (Standard `true`)
- `run_links_audit: boolean` (Standard `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (Standard alle `false`)

##### Ausgaben

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Berechtigungen

- Lesen von Arbeitsbereichsdateien und Schreiben von werkzeuggenerierten Artefakten (z.B. Lint-
  Berichten, Test-Logs) nur; kein Schreiben in `translations/` oder
  `translated_images/`.
- Ausführen von lokalen Shell-Kommandos.
- Optionaler Netzwerkzugriff nur für Paket-Wiederherstellung (`npm ci`,
  `python -m pip install`, `mvn` Abhängigkeitsauflösung).
- Keine Berechtigung zum Pushen, Mergen oder Ändern von `translations/` oder
  `translated_images/`.

##### Fehlerfälle

- `E_NO_INPUT_PATHS`: `changed_paths` ist leer.
- `E_INVALID_PATH`: Eingabepfad verlässt das Repository-Root.
- `E_LINT_FAILED`: Markdown-Lint endet mit Fehlercode.
- `E_LINK_AUDIT_FAILED`: Link-Audit-Befehl endet mit Fehlercode.
- `E_SAMPLE_TEST_FAILED`: Beispiel-Test/Build endet mit Fehlercode.
- `E_TIMEOUT`: Befehl hat die konfigurierte Zeitüberschreitung überschritten.

##### Empfohlener CI-Vertrag

Zur Automatisierung der Validierung konfiguriere einen CI-Job, der:

- Bei Pull Requests auslöst, die `*.md`, Beispielcode oder diese Datei berühren.
- Die oben aufgeführten exakten Kommandos ausführt.
- Logs als Artefakte speichert.
- Den Job bei jedem Nicht-Null-Exit-Code fehlschlagen lässt.

#### Wenn du einen MCP-Server aus diesem Repo bereitstellst

- [ ] Lies das Entwurf-Changelog für MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Teste deinen Server gegen SDK-Betas:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Entferne Annahmen zu Sessions und Handshakes; behandle jede Anfrage als
  eigenständig:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Sende `Mcp-Method`- und `Mcp-Name`-Header für rohe HTTP-Anfragen:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Prüfe fest codierte Fehlercodes (`missing resource` wurde von `-32002` auf `-32602` verschoben).

- [ ] Migration für veraltete Roots, Sampling und
  Logging markieren und planen:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migration von der experimentellen `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Überprüfung der Autorisierung für OAuth und OpenID Connect Härtung:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentationsstruktur

- **Module 00-11**: Kerncurriculum-Inhalte in sequentieller Reihenfolge
- **translations/**: Sprachspezifische Versionen (automatisch generiert, nicht direkt bearbeiten)
- **translated_images/**: Lokalisierte Bildversionen (automatisch generiert)
- **images/**: Quellbilder und Diagramme

### Änderungen an der Dokumentation vornehmen

1. Bearbeiten Sie nur die englischen Markdown-Dateien in den Root-Modulverzeichnissen (00-11)
2. Aktualisieren Sie bei Bedarf die Bilder im Verzeichnis `images/`
3. Der GitHub Action co-op-translator generiert automatisch Übersetzungen
4. Übersetzungen werden bei Push auf den Hauptbranch neu generiert

### Arbeiten mit Übersetzungen

- **Automatisierte Übersetzung**: GitHub Actions Workflow übernimmt alle Übersetzungen
- **Nicht manuell bearbeiten** von Dateien im Verzeichnis `translations/`
- Übersetzungs-Metadaten sind in jeder übersetzten Datei eingebettet
- Unterstützte Sprachen: 48+ Sprachen einschließlich Arabisch, Chinesisch, Französisch, Deutsch, Hindi, Japanisch, Koreanisch, Portugiesisch, Russisch, Spanisch und viele mehr

## Testanweisungen

### Dokumentationsvalidierung

Da es sich hauptsächlich um ein Dokumentations-Repository handelt, konzentrieren sich die Tests auf:

1. **Link-Musterprüfung**: Markdown-Links auflisten zur Überprüfung

   ```bash
   # Markdown-Links auflisten (Musterüberprüfung)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Codebeispielvalidierung**: Testen, dass Codebeispiele kompilieren/laufen

   ```bash
   # Zum bestimmten Beispiel navigieren und dessen Tests ausführen
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Überprüfung der Formatierungs-Konsistenz

   ```bash
   # Verwenden Sie bei Bedarf markdownlint
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testen von Beispielprojekten

Jedes sprachspezifische Beispiel enthält seinen eigenen Testansatz:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Code-Stilrichtlinien

### Dokumentationsstil

- Verwenden Sie klare, anfängerfreundliche Sprache
- Fügen Sie Codebeispiele in mehreren Sprachen hinzu, wo zutreffend
- Folgen Sie den besten Markdown-Praktiken:
  - Verwenden Sie ATX-Style-Überschriften (`#` Syntax)
  - Verwenden Sie umgrenzte Codeblöcke mit Sprachkennzeichnung
  - Fügen Sie beschreibenden Alt-Text für Bilder ein
  - Halten Sie die Zeilenlängen vernünftig (kein harter Grenzwert, aber sinnvoll)

### Stil für Codebeispiele

#### TypeScript/JavaScript
- Verwenden Sie ES-Module (`import`/`export`)
- Folgen Sie den TypeScript-Stilregeln für strict mode
- Fügen Sie Typannotationen hinzu
- Ziel-Standard ES2022

#### Python
- Folgen Sie den PEP 8-Stilrichtlinien
- Verwenden Sie Typ-Hinweise wo angemessen
- Fügen Sie Docstrings für Funktionen und Klassen hinzu
- Verwenden Sie moderne Python-Features (3.8+)

#### Java
- Folgen Sie den Spring Boot-Konventionen
- Verwenden Sie Java 21-Features
- Folgen Sie der Standard-Maven-Projektstruktur
- Fügen Sie Javadoc-Kommentare hinzu

### Dateiorganisation

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Build und Deployment

### Dokumentations-Deployment


Das Repository verwendet GitHub Pages oder ähnliches für das Hosting der Dokumentation (falls zutreffend). Änderungen am main-Branch lösen aus:

1. Übersetzungsworkflow (`.github/workflows/co-op-translator.yml`)
2. Automatisierte Übersetzung aller englischen Markdown-Dateien
3. Lokalisierung von Bildern nach Bedarf

### Kein Build-Prozess erforderlich

Dieses Repository enthält hauptsächlich Markdown-Dokumentation. Für den Kerncurriculum-Inhalt ist kein Kompilierungs- oder Build-Schritt erforderlich.

### Bereitstellung von Beispielprojekten

Einzelne Beispielprojekte können Bereitstellungsanweisungen enthalten:
- Siehe `03-GettingStarted/09-deployment/` für Anleitung zur MCP-Server-Bereitstellung
- Beispiele zur Bereitstellung von Azure Container Apps in `11-MCPServerHandsOnLabs/`

## Richtlinien für Beiträge

### Pull-Request-Prozess

1. **Fork und Klonen**: Forke das Repository und klone deinen Fork lokal
2. **Erstelle einen Branch**: Verwende aussagekräftige Branch-Namen (z. B. `fix/typo-module-3`, `add/python-example`)
3. **Nimm Änderungen vor**: Bearbeite nur englische Markdown-Dateien (keine Übersetzungen)
4. **Lokal testen**: Überprüfe, ob Markdown korrekt dargestellt wird
5. **Reiche PR ein**: Verwende klare PR-Titel und Beschreibungen
6. **CLA**: Unterzeichne die Microsoft Contributor License Agreement bei Aufforderung

### PR-Titelformat

Verwende klare, beschreibende Titel:
- `[Module XX] Kurze Beschreibung` für modul-spezifische Änderungen
- `[Samples] Beschreibung` für Änderungen an Beispielcode
- `[Docs] Beschreibung` für allgemeine Dokumentationsupdates

### Was beigetragen werden sollte

- Fehlerbehebungen in Dokumentation oder Codebeispielen
- Neue Codebeispiele in weiteren Sprachen
- Klarstellungen und Verbesserungen bestehender Inhalte
- Neue Fallstudien oder praktische Beispiele
- Fehlerberichte für unklare oder falsche Inhalte

### Was NICHT gemacht werden sollte

- Bearbeite Dateien im `translations/`-Verzeichnis nicht direkt
- Bearbeite das Verzeichnis `translated_images/` nicht
- Füge keine großen Binärdateien ohne Absprache hinzu
- Ändere Übersetzungsworkflow-Dateien nicht ohne Koordination

## Zusätzliche Hinweise

### Repository-Pflege

- **Changelog**: Alle wesentlichen Änderungen sind in `changelog.md` dokumentiert
- **Study Guide**: Verwende `study_guide.md` für einen Überblick zur Curriculum-Navigation
- **Issue-Vorlagen**: Nutze GitHub-Issue-Vorlagen für Fehlerberichte und Feature-Anfragen
- **Code of Conduct**: Alle Mitwirkenden müssen dem Microsoft Open Source Code of Conduct folgen

### Lernpfad

Folge den Modulen in der Reihenfolge (00-11) für optimales Lernen:
1. **00-02**: Grundlagen (Einführung, Kernkonzepte, Sicherheit)
2. **03**: Einstieg mit praktischer Umsetzung
3. **04-05**: Praktische Umsetzung und fortgeschrittene Themen
4. **06-10**: Community, bewährte Verfahren und reale Anwendungen
5. **11**: Umfangreiche Datenbank-Integrationslabore (13 aufeinanderfolgende Labs)

### Unterstützungsressourcen

- **Dokumentation**: https://modelcontextprotocol.io/
- **Spezifikation**: https://spec.modelcontextprotocol.io/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-Server
- **Verwandte Kurse**: Siehe README.md für weitere Microsoft-Lernpfade

### Häufige Problembehebung

**F: Mein PR besteht die Übersetzungsprüfung nicht**
A: Stelle sicher, dass du nur englische Markdown-Dateien in den Root-Modulverzeichnissen bearbeitet hast, nicht übersetzte Versionen.

**F: Wie füge ich eine neue Sprache hinzu?**

A: Die Sprachunterstützung wird über den Co-op-Translator-Workflow verwaltet. Öffnen Sie ein Issue, um das Hinzufügen neuer Sprachen zu besprechen.

**F: Codebeispiele funktionieren nicht**

A: Stellen Sie sicher, dass Sie die Einrichtungshinweise im README der jeweiligen Beispielanwendung befolgt haben. Überprüfen Sie, ob die korrekten Versionen der Abhängigkeiten installiert sind.

**F: Bilder werden nicht angezeigt**
A: Überprüfen Sie, ob die Bildpfade relativ sind und Vorwärtsschläge verwenden. Bilder sollten sich im Verzeichnis `images/` oder in `translated_images/` für lokalisierte Versionen befinden.

### Leistungsüberlegungen

- Der Übersetzungsworkflow kann mehrere Minuten in Anspruch nehmen
- Große Bilder sollten vor dem Commit optimiert werden
- Halten Sie einzelne Markdown-Dateien fokussiert und vernünftig groß
- Verwenden Sie relative Links für bessere Portabilität

### Projekt-Governance

Dieses Projekt folgt den Open-Source-Praktiken von Microsoft:
- MIT-Lizenz für Code und Dokumentation
- Microsoft Open Source Code of Conduct
- CLA ist für Beiträge erforderlich
- Sicherheitsprobleme: Befolgen Sie die Richtlinien in SECURITY.md
- Support: Siehe SUPPORT.md für Hilfsressourcen

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->