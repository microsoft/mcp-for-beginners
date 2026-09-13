# Einrichtung beliebter MCP-Host-Clients

> [!NOTE]
> Host-Konfigurationen, die auf `/sse` zeigen, sind Legacy-HTTP+SSE-Beispiele für
> MCP `2025-11-25`. Für MCP `2026-07-28` wählen Sie Streamable HTTP in Hosts, die
> dies unterstützen, und verwenden Sie den vom Server konfigurierten Endpunkt.

Dieser Leitfaden behandelt, wie man MCP-Server mit beliebten AI-Host-Anwendungen konfiguriert und verwendet. Jeder Host hat seinen eigenen Konfigurationsansatz, aber nach der Einrichtung kommunizieren sie alle mit MCP-Servern über das standardisierte Protokoll.

## Was ist ein MCP-Host?

Ein **MCP-Host** ist eine KI-Anwendung, die sich mit MCP-Servern verbinden kann, um ihre Fähigkeiten zu erweitern. Man kann es sich als „Frontend“ vorstellen, mit dem Benutzer interagieren, während MCP-Server die „Backend“-Werkzeuge und Daten bereitstellen.

```mermaid
flowchart LR
    User[👤 Benutzer] --> Host[🖥️ MCP-Host]
    Host --> S1[MCP-Server A]
    Host --> S2[MCP-Server B]
    Host --> S3[MCP-Server C]
    
    subgraph "Beliebte Hosts"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Voraussetzungen

- Ein MCP-Server, mit dem eine Verbindung hergestellt wird (siehe [Modul 3.1 - Erster Server](../01-first-server/README.md))
- Die Host-Anwendung auf Ihrem System installiert
- Grundkenntnisse in JSON-Konfigurationsdateien

---

## 1. Claude Desktop

**Claude Desktop** ist die offizielle Desktop-Anwendung von Anthropic, die MCP nativ unterstützt.

### Installation

1. Laden Sie Claude Desktop von [claude.ai/download](https://claude.ai/download) herunter
2. Installieren und melden Sie sich mit Ihrem Anthropic-Konto an

### Konfiguration

Claude Desktop verwendet eine JSON-Konfigurationsdatei zur Definition von MCP-Servern.

**Ort der Konfigurationsdatei:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Beispielkonfiguration:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Konfigurationsoptionen

| Feld | Beschreibung | Beispiel |
|-------|-------------|---------|
| `command` | Die auszuführende ausführbare Datei | `"python"`, `"node"`, `"npx"` |
| `args` | Kommandozeilenargumente | `["-m", "my_server"]` |
| `env` | Umgebungsvariablen | `{"API_KEY": "xxx"}` |
| `cwd` | Arbeitsverzeichnis | `"/path/to/server"` |

### Testen Ihrer Einrichtung

1. Speichern Sie die Konfigurationsdatei
2. Starten Sie Claude Desktop komplett neu (beenden und neu öffnen)
3. Öffnen Sie ein neues Gespräch
4. Achten Sie auf das 🔌-Symbol, das verbundene Server anzeigt
5. Versuchen Sie, Claude zu bitten, eines Ihrer Werkzeuge zu benutzen

### Fehlerbehebung bei Claude Desktop

**Server erscheint nicht:**
- Prüfen Sie die Syntax der Konfigurationsdatei mit einem JSON-Validator
- Stellen Sie sicher, dass der Befehls-Pfad korrekt ist
- Prüfen Sie die Claude Desktop-Protokolle: Hilfe → Protokolle anzeigen

**Server stürzt beim Start ab:**
- Testen Sie den Server zuerst manuell im Terminal
- Kontrollieren Sie, ob Umgebungsvariablen korrekt gesetzt sind
- Stellen Sie sicher, dass alle Abhängigkeiten installiert sind

---

## 2. VS Code mit GitHub Copilot

VS Code unterstützt MCP über GitHub Copilot Chat-Erweiterungen.

### Voraussetzungen

1. Installierter VS Code 1.99+
2. Installierte GitHub Copilot-Erweiterung
3. Installierte GitHub Copilot Chat-Erweiterung

### Konfiguration

VS Code verwendet `.vscode/mcp.json` in Ihren Arbeitsbereichs- oder Benutzereinstellungen.

**Arbeitsbereichskonfiguration** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Benutzereinstellungen** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Verwendung von MCP in VS Code

1. Öffnen Sie das Copilot Chat-Panel (Strg+Shift+I / Cmd+Shift+I)
2. Geben Sie `@` ein, um verfügbare MCP-Werkzeuge zu sehen
3. Verwenden Sie natürliche Sprache, um Werkzeuge aufzurufen: „Rechne 25 * 48 mit dem Taschenrechner“

### Fehlerbehebung VS Code

**MCP-Server werden nicht geladen:**
- Prüfen Sie das Ausgabefenster → „MCP“ auf Fehlermeldungen
- Fenster neu laden: Strg+Shift+P → „Developer: Reload Window“
- Vergewissern Sie sich, dass der Server zuerst eigenständig läuft

---

## 3. Cursor

**Cursor** ist ein AI-fokussierter Code-Editor mit integrierter MCP-Unterstützung.

### Installation

1. Laden Sie Cursor von [cursor.sh](https://cursor.sh) herunter
2. Installieren und melden Sie sich an

### Konfiguration

Cursor verwendet ein ähnliches Konfigurationsformat wie Claude Desktop.

**Ort der Konfigurationsdatei:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Beispielkonfiguration:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Verwendung von MCP in Cursor

1. Öffnen Sie den AI-Chat von Cursor (Strg+L / Cmd+L)
2. MCP-Werkzeuge werden automatisch in den Vorschlägen angezeigt
3. Bitten Sie die KI, Aufgaben mit verbundenen Servern auszuführen

---

## 4. Cline (Terminal-basiert)

**Cline** ist ein terminalbasierter MCP-Client, ideal für Kommandozeilen-Workflows.

### Installation

```bash
npm install -g @anthropic/cline
```

### Konfiguration

Cline verwendet Umgebungsvariablen und Kommandozeilenargumente.

**Verwendung von Umgebungsvariablen:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Verwendung von Kommandozeilenargumenten:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigurationsdatei** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Verwendung von Cline

```bash
# Starte eine interaktive Sitzung
cline

# Einzelne Abfrage mit MCP
cline "Calculate the square root of 144 using the calculator"

# Verfügbare Werkzeuge auflisten
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** ist ein weiterer KI-gestützter Code-Editor mit MCP-Unterstützung.

### Installation

1. Laden Sie Windsurf von [codeium.com/windsurf](https://codeium.com/windsurf) herunter
2. Installieren und erstellen Sie ein Konto

### Konfiguration

Windsurf-Konfiguration wird über die Einstellungsoberfläche verwaltet:

1. Öffnen Sie die Einstellungen (Strg+, / Cmd+,)
2. Suchen Sie nach „MCP“
3. Klicken Sie auf „In settings.json bearbeiten“

**Beispielkonfiguration:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Vergleich der Transporttypen

Verschiedene Hosts unterstützen unterschiedliche Transportmechanismen:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (Standard Ein-/Ausgabe): Am besten für lokale Server, die vom Host gestartet werden
**SSE/HTTP**: Am besten für Remote-Server oder Server, die von mehreren Clients gemeinsam genutzt werden

---

## Häufige Fehlerbehebung

### Server startet nicht

1. **Testen Sie den Server zuerst manuell:**
   ```bash
   # Für Python
   python -m your_server_module
   
   # Für Node.js
   node /path/to/server/index.js
   ```

2. **Überprüfen Sie den Befehls-Pfad:**
   - Verwenden Sie wann immer möglich absolute Pfade
   - Stellen Sie sicher, dass die ausführbare Datei in Ihrem PATH ist

3. **Überprüfen Sie Abhängigkeiten:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server verbindet, aber Werkzeuge funktionieren nicht

1. **Prüfen Sie Serverprotokolle** – Die meisten Hosts haben Protokollierungsoptionen
2. **Überprüfen Sie die Werkzeugregistrierung** – Testen Sie mit MCP Inspector
3. **Prüfen Sie Berechtigungen** – Einige Werkzeuge benötigen Datei- oder Netzwerkzugriff

### Umgebungsvariablen werden nicht übergeben

- Einige Hosts filtern Umgebungsvariablen
- Verwenden Sie das Konfigurationsfeld `env` explizit
- Vermeiden Sie sensible Daten in Konfigurationsdateien (verwenden Sie Geheimnisverwaltung)

---

## Sicherheitsbest Practices

1. **API-Schlüssel niemals in Konfigurationsdateien festschreiben**
2. **Verwenden Sie Umgebungsvariablen für sensible Daten**
3. **Begrenzen Sie Serverberechtigungen nur auf das Notwendige**
4. **Überprüfen Sie Servercode, bevor Sie Zugriff auf Ihr System gewähren**
5. **Verwenden Sie Erlaubnislisten für Datei- und Netzwerkzugriffe**

---

## Was kommt als Nächstes

- [3.13 - Debugging mit MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Erstellen Ihres ersten MCP-Servers](../01-first-server/README.md)
- [Modul 5 - Fortgeschrittene Themen](../../05-AdvancedTopics/README.md)

---

## Zusätzliche Ressourcen

- [Claude Desktop MCP-Dokumentation](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP-Erweiterung](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP-Spezifikation - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Offizielles MCP-Server-Register](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->