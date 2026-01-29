# AGENTS.md

## Projektübersicht

**MCP für Anfänger** ist ein Open-Source-Bildungsprogramm zum Erlernen des Model Context Protocol (MCP) – ein standardisiertes Framework für die Interaktion zwischen KI-Modellen und Client-Anwendungen. Dieses Repository bietet umfassende Lernmaterialien mit praktischen Codebeispielen in mehreren Programmiersprachen.

### Wichtige Technologien

- **Programmiersprachen**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Datenbanken**: PostgreSQL mit pgvector-Erweiterung
- **Cloud-Plattformen**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build-Tools**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown mit automatisierter Übersetzung in mehrere Sprachen (48+ Sprachen)

### Architektur

- **11 Kernmodule (00-11)**: Schrittweiser Lernpfad von den Grundlagen bis zu fortgeschrittenen Themen
- **Praktische Übungen**: Praktische Aufgaben mit vollständigen Lösungscodes in mehreren Sprachen
- **Beispielprojekte**: Funktionierende MCP-Server- und Client-Implementierungen
- **Übersetzungssystem**: Automatisierter GitHub Actions-Workflow für mehrsprachige Unterstützung
- **Bildressourcen**: Zentrales Bildverzeichnis mit übersetzten Versionen

## Setup-Befehle

Dies ist ein dokumentationsorientiertes Repository. Die meisten Setups erfolgen innerhalb der einzelnen Beispielprojekte und Übungen.

### Repository-Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbeiten mit Beispielprojekten

Beispielprojekte befinden sich in:
- `03-GettingStarted/samples/` - Sprachspezifische Beispiele
- `03-GettingStarted/01-first-server/solution/` - Erste Server-Implementierungen
- `03-GettingStarted/02-client/solution/` - Client-Implementierungen
- `11-MCPServerHandsOnLabs/` - Umfassende Datenbankintegrationsübungen

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
# or
pip install -e .
python main.py
```

#### Java-Projekte
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Entwicklungsworkflow

### Dokumentationsstruktur

- **Module 00-11**: Kerncurriculum-Inhalte in chronologischer Reihenfolge
- **translations/**: Sprachspezifische Versionen (automatisch generiert, nicht direkt bearbeiten)
- **translated_images/**: Lokalisierte Bildversionen (automatisch generiert)
- **images/**: Quellbilder und Diagramme

### Änderungen an der Dokumentation vornehmen

1. Bearbeiten Sie nur die englischen Markdown-Dateien in den Hauptmodulverzeichnissen (00-11)
2. Aktualisieren Sie bei Bedarf Bilder im Verzeichnis `images/`
3. Der GitHub Action „co-op-translator“ generiert automatisch Übersetzungen
4. Übersetzungen werden bei jedem Push in den Hauptbranch neu erstellt

### Arbeiten mit Übersetzungen

- **Automatische Übersetzung**: Der GitHub Actions-Workflow übernimmt alle Übersetzungen
- **Bearbeiten Sie NIEMALS** Dateien im Verzeichnis `translations/`
- Übersetzungsmetadaten sind in jeder übersetzten Datei eingebettet
- Unterstützte Sprachen: 48+ Sprachen, darunter Arabisch, Chinesisch, Französisch, Deutsch, Hindi, Japanisch, Koreanisch, Portugiesisch, Russisch, Spanisch und viele mehr

## Testanweisungen

### Validierung der Dokumentation

Da dies hauptsächlich ein Dokumentations-Repository ist, konzentriert sich das Testen auf:

1. **Link-Validierung**: Sicherstellen, dass alle internen Links funktionieren
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validierung von Codebeispielen**: Testen, ob Codebeispiele kompiliert/ausgeführt werden
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown-Linting**: Überprüfung der Formatierungskonsistenz
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testen von Beispielprojekten

Jedes sprachspezifische Beispiel hat seinen eigenen Testansatz:

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
- Fügen Sie, wo möglich, Codebeispiele in mehreren Sprachen ein
- Befolgen Sie die besten Praktiken für Markdown:
  - Verwenden Sie ATX-Header (`#`-Syntax)
  - Verwenden Sie umschlossene Codeblöcke mit Sprachkennzeichnung
  - Fügen Sie beschreibende Alt-Texte für Bilder hinzu
  - Halten Sie die Zeilenlängen vernünftig (kein festes Limit, aber sinnvoll)

### Stil für Codebeispiele

#### TypeScript/JavaScript
- Verwenden Sie ES-Module (`import`/`export`)
- Befolgen Sie die Konventionen des TypeScript-Strict-Modus
- Fügen Sie Typannotationen hinzu
- Ziel: ES2022

#### Python
- Befolgen Sie die PEP 8-Stilrichtlinien
- Verwenden Sie, wo angebracht, Typ-Hinweise
- Fügen Sie Docstrings für Funktionen und Klassen hinzu
- Verwenden Sie moderne Python-Funktionen (3.8+)

#### Java
- Befolgen Sie die Konventionen von Spring Boot
- Verwenden Sie Java 21-Funktionen
- Befolgen Sie die Standard-Maven-Projektstruktur
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

### Deployment der Dokumentation

Das Repository verwendet GitHub Pages oder Ähnliches für das Hosting der Dokumentation (falls zutreffend). Änderungen am Hauptbranch lösen aus:

1. Übersetzungsworkflow (`.github/workflows/co-op-translator.yml`)
2. Automatische Übersetzung aller englischen Markdown-Dateien
3. Lokalisierung von Bildern bei Bedarf

### Kein Build-Prozess erforderlich

Dieses Repository enthält hauptsächlich Markdown-Dokumentation. Für die Kerncurriculum-Inhalte ist keine Kompilierung oder ein Build-Schritt erforderlich.

### Deployment von Beispielprojekten

Einzelne Beispielprojekte können Deployment-Anweisungen enthalten:
- Siehe `03-GettingStarted/09-deployment/` für Anleitungen zur MCP-Server-Bereitstellung
- Beispiele für Azure Container Apps-Bereitstellungen in `11-MCPServerHandsOnLabs/`

## Richtlinien für Beiträge

### Pull-Request-Prozess

1. **Fork und Klonen**: Forken Sie das Repository und klonen Sie Ihren Fork lokal
2. **Erstellen Sie einen Branch**: Verwenden Sie beschreibende Branch-Namen (z. B. `fix/typo-module-3`, `add/python-example`)
3. **Änderungen vornehmen**: Bearbeiten Sie nur englische Markdown-Dateien (keine Übersetzungen)
4. **Lokal testen**: Überprüfen Sie, ob Markdown korrekt gerendert wird
5. **PR einreichen**: Verwenden Sie klare PR-Titel und Beschreibungen
6. **CLA**: Unterzeichnen Sie die Microsoft Contributor License Agreement, wenn Sie dazu aufgefordert werden

### Format für PR-Titel

Verwenden Sie klare, beschreibende Titel:
- `[Module XX] Kurze Beschreibung` für modulspezifische Änderungen
- `[Samples] Beschreibung` für Änderungen an Beispielcodes
- `[Docs] Beschreibung` für allgemeine Dokumentationsaktualisierungen

### Was Sie beitragen können

- Fehlerbehebungen in der Dokumentation oder in Codebeispielen
- Neue Codebeispiele in zusätzlichen Sprachen
- Klarstellungen und Verbesserungen bestehender Inhalte
- Neue Fallstudien oder praktische Beispiele
- Problemberichte für unklare oder fehlerhafte Inhalte

### Was Sie NICHT tun sollten

- Bearbeiten Sie keine Dateien im Verzeichnis `translations/` direkt
- Bearbeiten Sie nicht das Verzeichnis `translated_images/`
- Fügen Sie keine großen Binärdateien ohne Absprache hinzu
- Ändern Sie keine Übersetzungsworkflow-Dateien ohne Abstimmung

## Zusätzliche Hinweise

### Repository-Wartung

- **Changelog**: Alle wesentlichen Änderungen sind in `changelog.md` dokumentiert
- **Lernleitfaden**: Verwenden Sie `study_guide.md` für eine Übersicht über die Navigation im Curriculum
- **Issue-Vorlagen**: Verwenden Sie GitHub-Issue-Vorlagen für Fehlerberichte und Funktionsanfragen
- **Verhaltenskodex**: Alle Mitwirkenden müssen den Microsoft Open Source Code of Conduct einhalten

### Lernpfad

Folgen Sie den Modulen in chronologischer Reihenfolge (00-11) für ein optimales Lernerlebnis:
1. **00-02**: Grundlagen (Einführung, Kernkonzepte, Sicherheit)
2. **03**: Einstieg mit praktischer Implementierung
3. **04-05**: Praktische Implementierung und fortgeschrittene Themen
4. **06-10**: Community, Best Practices und reale Anwendungen
5. **11**: Umfassende Datenbankintegrationsübungen (13 aufeinanderfolgende Übungen)

### Unterstützungsressourcen

- **Dokumentation**: https://modelcontextprotocol.io/
- **Spezifikation**: https://spec.modelcontextprotocol.io/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord-Server
- **Verwandte Kurse**: Siehe README.md für weitere Microsoft-Lernpfade

### Häufige Probleme

**F: Mein PR schlägt bei der Übersetzungsprüfung fehl**  
A: Stellen Sie sicher, dass Sie nur englische Markdown-Dateien in den Hauptmodulverzeichnissen bearbeitet haben, nicht die übersetzten Versionen.

**F: Wie füge ich eine neue Sprache hinzu?**  
A: Die Sprachunterstützung wird über den co-op-translator-Workflow verwaltet. Öffnen Sie ein Issue, um die Hinzufügung neuer Sprachen zu besprechen.

**F: Codebeispiele funktionieren nicht**  
A: Stellen Sie sicher, dass Sie die Setup-Anweisungen in der README des jeweiligen Beispiels befolgt haben. Überprüfen Sie, ob Sie die richtigen Versionen der Abhängigkeiten installiert haben.

**F: Bilder werden nicht angezeigt**  
A: Überprüfen Sie, ob die Bildpfade relativ sind und Schrägstriche verwenden. Bilder sollten sich im Verzeichnis `images/` oder `translated_images/` für lokalisierte Versionen befinden.

### Leistungsüberlegungen

- Der Übersetzungsworkflow kann mehrere Minuten dauern
- Große Bilder sollten vor dem Commit optimiert werden
- Halten Sie einzelne Markdown-Dateien fokussiert und in einer angemessenen Größe
- Verwenden Sie relative Links für bessere Portabilität

### Projektführung

Dieses Projekt folgt den Open-Source-Praktiken von Microsoft:
- MIT-Lizenz für Code und Dokumentation
- Microsoft Open Source Code of Conduct
- CLA erforderlich für Beiträge
- Sicherheitsprobleme: Befolgen Sie die Richtlinien in SECURITY.md
- Unterstützung: Siehe SUPPORT.md für Hilfsressourcen

---

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.