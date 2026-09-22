# AGENTS.md

## Projektübersicht

**MCP für Anfänger** ist ein Open-Source-Bildungsprogramm zum Erlernen des Model Context Protocol (MCP) – ein standardisiertes Framework für Interaktionen zwischen KI-Modellen und Client-Anwendungen. Dieses Repository bietet umfassende Lernmaterialien mit praktischen Codebeispielen in mehreren Programmiersprachen.

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
- **Dokumentation**: Markdown mit automatischer Übersetzung in über 48 Sprachen

### Architektur

- **11 Kernmodule (00-11)**: Sequenzieller Lernpfad von Grundlagen zu fortgeschrittenen Themen
- **Hands-on Labs**: Praktische Übungen mit vollständigem Lösungscode in mehreren Sprachen
- **Beispielprojekte**: Funktionierende MCP-Server- und Client-Implementierungen
- **Übersetzungssystem**: Automatisierter GitHub Actions Workflow für Mehrsprachigkeit
- **Bildmaterialien**: Zentraler Bild-Ordner mit übersetzten Versionen

## Setup-Befehle

Dies ist ein dokumentationsorientiertes Repository. Das meiste Setup erfolgt innerhalb der einzelnen Beispielprojekte und Labs.

### Repository Setup

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
- `11-MCPServerHandsOnLabs/` - Umfassende Datenbankintegrations-Labs

Jedes Beispielprojekt enthält eigene Setup-Anweisungen:

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

## Entwicklungsablauf

### MCP 7-28 Bereitschaft

#### Checkliste für Repository-Bereitschaft

- [x] **Klarheit für neue Mitwirkende**: Diese Datei definiert Zweck des Repositories,
  Struktur, Beitragsregeln und Setup-Pfade für Beispiele.
- [x] **Build/Test/Lint-Befehle mit exakten Flags**:
  - Repository-Dokumentations-Lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit der Link-Muster in der Dokumentation:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validierung TypeScript-Beispiele:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validierung Python-Beispiele:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validierung Java-Beispiele:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Einen realistischen Workflow, der zu einem MCP-Tool werden kann**:
  `validate_curriculum_change`
- [x] **Eingaben/Ausgaben sind explizit** (siehe Spezifikation weiter unten).
- [x] **Berechtigungen und Fehlermodi sind dokumentiert** (siehe Spezifikation weiter unten).
- [x] **CI-Testbarkeit ist explizit** (deterministische Befehle, eindeutige
  Exit-Codes und maschinenlesbare Ausgaben).

#### Vorschlag für MCP-Tool-Workflow: `validate_curriculum_change`

##### Ziel

Validierung von Änderungen an Curriculum-Dokumentation und repräsentativem Beispielcode
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

- Nur Lesen von Arbeitsbereichsdateien und Schreiben von Tool-generierten Artefakten (z. B. Lint-Berichte,
  Test-Logs); keine Schreibzugriffe auf `translations/` oder
  `translated_images/`.
- Ausführung lokaler Shell-Befehle.
- Optionaler Netzwerkzugriff nur für Paketwiederherstellung (`npm ci`,
  `python -m pip install`, `mvn` Abhängigkeitsauflösung).
- Keine Berechtigung zum Pushen, Mergen oder Ändern von `translations/` oder
  `translated_images/`.

##### Fehlermodi

- `E_NO_INPUT_PATHS`: `changed_paths` ist leer.
- `E_INVALID_PATH`: Eingabepfad verlässt den Repository-Stamm.
- `E_LINT_FAILED`: markdown lint endet mit Fehlercode ungleich null.
- `E_LINK_AUDIT_FAILED`: Link-Audit-Befehl endet mit Fehlercode ungleich null.
- `E_SAMPLE_TEST_FAILED`: Beispiel-Test/Build endet mit Fehlercode ungleich null.
- `E_TIMEOUT`: Befehl überschritt die konfigurierte Zeitüberschreitung.

##### Empfohlener CI-Vertrag

Um die Validierung zu automatisieren, richten Sie einen CI-Job ein, der:

- Bei Pull Requests ausgelöst wird, die `*.md`, Beispielcode oder diese Datei berühren.
- Die oben genannten exakten Befehle ausführt.
- Logs als Artefakte speichert.
- Den Job bei jedem Fehlercode ungleich null als fehlgeschlagen markiert.

#### Wenn Sie einen MCP-Server aus diesem Repo bereitstellen

- [ ] Lesen Sie das finale MCP-`2026-07-28` Changelog:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Vergewissern Sie sich, dass die ausgewählte SDK-Version MCP `2026-07-28` unterstützt:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Entfernen Sie Sitzungs- und Handshake-Annahmen; behandeln Sie jede Anfrage als
  eigenständige Einheit:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Senden Sie `Mcp-Method` und `Mcp-Name` Header für rohe HTTP-Anfragen:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Prüfen Sie hartkodierte Fehlercodes (`missing resource` wurde von `-32002` auf `-32602` verschoben).
- [ ] Migrieren Sie die veralteten Roots, Sampling, Logging und Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrieren Sie weg von der experimentellen `2025-11-25` Tasks API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Überprüfen Sie die Autorisierung für OAuth und OpenID Connect Härtungen:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Dokumentationsstruktur

- **Module 00-11**: Kerninhalt des Curriculums in sequenzieller Reihenfolge
- **translations/**: Sprachspezifische Versionen (automatisch generiert, nicht direkt bearbeiten)
- **translated_images/**: Lokalisierte Bildversionen (automatisch generiert)
- **images/**: Quellbilder und Diagramme

### Änderungen an der Dokumentation vornehmen

1. Bearbeiten Sie nur die englischen Markdown-Dateien in den Stammverzeichnissen der Module (00-11)
2. Aktualisieren Sie bei Bedarf Bilder im Verzeichnis `images/`
3. Der GitHub Action co-op-translator generiert automatisch Übersetzungen
4. Übersetzungen werden bei Push auf den main-Branch neu generiert

### Arbeiten mit Übersetzungen

- **Automatisierte Übersetzung**: GitHub Actions Workflow verwaltet alle Übersetzungen
- Bearbeiten Sie Dateien im Verzeichnis `translations/` **NICHT** manuell
- Übersetzungs-Metadaten sind in jede übersetzte Datei eingebettet
- Unterstützte Sprachen: Über 48 Sprachen, darunter Arabisch, Chinesisch, Französisch, Deutsch, Hindi, Japanisch, Koreanisch, Portugiesisch, Russisch, Spanisch und viele mehr

## Testanweisungen

### Dokumentationsvalidierung

Da dies hauptsächlich ein Dokumentations-Repository ist, konzentrieren sich Tests auf:

1. **Link-Muster-Audit**: Markdown-Links zur Überprüfung auflisten

   ```bash
   # Markdown-Links auflisten (Musterüberprüfung)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Code-Beispiele validieren**: Testen, dass Code-Beispiele kompilieren/ausgeführt werden können

   ```bash
   # Navigiere zu einem bestimmten Beispiel und führe dessen Tests aus
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Prüfen der Formatierungskonsistenz

   ```bash
   # Verwenden Sie markdownlint, falls erforderlich
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Tests von Beispielprojekten

Jede sprachspezifische Beispielprojekt hat seine eigene Testmethode:

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

## Richtlinien für den Code-Stil

### Dokumentationsstil

- Verwenden Sie klare, anfängerfreundliche Sprache
- Fügen Sie bei Bedarf Codebeispiele in mehreren Sprachen ein
- Beachten Sie Markdown Best Practices:
  - Verwenden Sie ATX-Style-Überschriften (`#` Syntax)
  - Verwenden Sie umgrenzte Codeblöcke mit Sprachkennzeichnungen
  - Fügen Sie beschreibenden Alt-Text für Bilder hinzu
  - Halten Sie Zeilenlängen angemessen (keine harte Grenze, aber sinnvoll)

### Stil von Codebeispielen

#### TypeScript/JavaScript
- Verwenden Sie ES-Module (`import`/`export`)
- Befolgen Sie die TypeScript-Strict-Mode-Konventionen
- Fügen Sie Typannotationen hinzu
- Zielplattform ES2022

#### Python
- Beachten Sie PEP 8 Stilrichtlinien
- Verwenden Sie Typ-Hinweise wo angebracht
- Fügen Sie Docstrings für Funktionen und Klassen hinzu
- Nutzen Sie moderne Python-Funktionen (3.8+)

#### Java
- Folgen Sie Spring Boot Konventionen
- Verwenden Sie Java 21 Features
- Befolgen Sie die Standard Maven-Projektstruktur
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

## Build- und Deployment-Prozesse

### Deployment der Dokumentation

Das Repository verwendet GitHub Pages oder ähnliche Systeme zum Hosting der Dokumentation (falls zutreffend). Änderungen am main-Branch triggern:

1. Übersetzungsworkflow (`.github/workflows/co-op-translator.yml`)
2. Automatische Übersetzung aller englischen Markdown-Dateien
3. Bildlokalisierung nach Bedarf

### Kein Build-Prozess erforderlich

Dieses Repository enthält hauptsächlich Markdown-Dokumentation. Für den Kerncurriculum-Inhalt ist kein Kompilations- oder Build-Schritt erforderlich.

### Deployment von Beispielprojekten

Einzelne Beispielprojekte können Deployment-Anweisungen enthalten:
- Siehe `03-GettingStarted/09-deployment/` für MCP-Server-Deployment-Anleitungen
- Azure Container Apps Deployment-Beispiele in `11-MCPServerHandsOnLabs/`

## Beitragsrichtlinien

### Pull Request Prozess

1. **Forken und Klonen**: Forken Sie das Repository und klonen Sie Ihren Fork lokal
2. **Erstellen Sie einen Branch**: Verwenden Sie beschreibende Branch-Namen (z. B. `fix/typo-module-3`, `add/python-example`)
3. **Nehmen Sie Änderungen vor**: Bearbeiten Sie nur die englischen Markdown-Dateien (nicht die Übersetzungen)
4. **Testen Sie lokal**: Überprüfen Sie, ob Markdown korrekt gerendert wird
5. **Reichen Sie PR ein**: Verwenden Sie klare PR-Titel und Beschreibungen
6. **CLA**: Unterzeichnen Sie die Microsoft Contributor License Agreement, wenn Sie dazu aufgefordert werden

### PR-Titel-Format

Verwenden Sie klare, beschreibende Titel:
- `[Module XX] Kurze Beschreibung` für modulspezifische Änderungen
- `[Samples] Beschreibung` für Änderungen am Beispielcode
- `[Docs] Beschreibung` für allgemeine Dokumentationsupdates

### Was beitragen

- Fehlerbehebungen in Dokumentation oder Codebeispielen
- Neue Codebeispiele in weiteren Sprachen
- Klarstellungen und Verbesserungen bestehender Inhalte
- Neue Fallstudien oder praxisnahe Beispiele
- Fehlermeldungen bei unklaren oder fehlerhaften Inhalten

### Was NICHT tun

- Bearbeiten Sie Dateien im Verzeichnis `translations/` nicht direkt
- Bearbeiten Sie das Verzeichnis `translated_images/` nicht
- Fügen Sie keine großen Binärdateien ohne Absprache hinzu
- Ändern Sie keine Übersetzungs-Workflow-Dateien ohne Abstimmung

## Zusätzliche Hinweise

### Repository-Wartung

- **Changelog**: Alle bedeutenden Änderungen sind in `changelog.md` dokumentiert
- **Studienführer**: Verwenden Sie `study_guide.md` für eine Übersicht zur Navigation im Curriculum
- **Issue-Vorlagen**: Nutzen Sie GitHub-Issue-Vorlagen für Fehlerberichte und Funktionswünsche
- **Verhaltenskodex**: Alle Mitwirkenden müssen den Microsoft Open Source Code of Conduct einhalten

### Lernpfad

Folgen Sie den Modulen in sequenzieller Reihenfolge (00-11) für optimales Lernen:
1. **00-02**: Grundlagen (Einführung, Kernkonzepte, Sicherheit)
2. **03**: Einstieg mit praktischen Implementierungen
3. **04-05**: Praktische Umsetzung und fortgeschrittene Themen
4. **06-10**: Community, Best Practices und Anwendungen aus der Praxis
5. **11**: Umfassende Datenbankintegrations-Labs (13 aufeinanderfolgende Labs)

### Unterstützende Ressourcen

- **Dokumentation**: https://modelcontextprotocol.io/
- **Spezifikation**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-Server
- **Verwandte Kurse**: Siehe README.md für weitere Microsoft-Lernpfade

### Häufige Probleme und Lösungen

**F: Mein PR schlägt bei der Übersetzungsprüfung fehl**
A: Stellen Sie sicher, dass Sie nur die englischen Markdown-Dateien in den Stamm-Modulverzeichnissen bearbeitet haben, nicht die übersetzten Versionen.

**F: Wie füge ich eine neue Sprache hinzu?**
A: Die Sprachunterstützung wird durch den co-op-translator Workflow verwaltet. Öffnen Sie ein Issue, um das Hinzufügen neuer Sprachen zu besprechen.

**F: Codebeispiele funktionieren nicht**
A: Stellen Sie sicher, dass Sie die Setup-Anweisungen in der README des jeweiligen Beispiels befolgt haben. Prüfen Sie, ob Sie die korrekten Versionsstände der Abhängigkeiten installiert haben.

**F: Bilder werden nicht angezeigt**

A: Vergewissern Sie sich, dass Bildpfade relativ sind und Vorwärtsschrägstriche verwenden. Bilder sollten im Verzeichnis `images/` oder `translated_images/` für lokalisierte Versionen liegen.

### Leistungsaspekte

- Der Übersetzungsprozess kann mehrere Minuten dauern
- Große Bilder sollten vor dem Commit optimiert werden
- Halten Sie einzelne Markdown-Dateien fokussiert und vernünftig groß
- Verwenden Sie relative Links für bessere Portabilität

### Projektverwaltung

Dieses Projekt folgt den Open-Source-Praktiken von Microsoft:
- MIT-Lizenz für Code und Dokumentation
- Microsoft Open Source Verhaltenskodex
- CLA erforderlich für Beiträge
- Sicherheitsprobleme: Folgen Sie den Richtlinien in SECURITY.md
- Unterstützung: Siehe SUPPORT.md für Hilfsressourcen

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->