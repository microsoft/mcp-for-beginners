# Configurarea clienților populari MCP Host

> [!NOTE]
> Configurațiile host care indică către `/sse` sunt exemple vechi HTTP+SSE pentru
> MCP `2025-11-25`. Pentru MCP `2026-07-28`, selectați Streamable HTTP în hosturile care
> îl suportă și folosiți endpoint-ul configurat de server.

Acest ghid acoperă modul de configurare și utilizare a serverelor MCP cu aplicații host AI populare. Fiecare host are propria sa abordare de configurare, dar odată configurate, toate comunică cu serverele MCP folosind protocolul standardizat.

## Ce este un MCP Host?

Un **MCP Host** este o aplicație AI care poate să se conecteze la serverele MCP pentru a-și extinde capacitățile. Gândiți-vă la el ca la "frontend-ul" cu care utilizatorii interacționează, în timp ce serverele MCP oferă uneltele și datele "backend".

```mermaid
flowchart LR
    User[👤 Utilizator] --> Host[🖥️ Gazdă MCP]
    Host --> S1[Server MCP A]
    Host --> S2[Server MCP B]
    Host --> S3[Server MCP C]
    
    subgraph "Gazde Populare"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Cerințe preliminare

- Un server MCP la care să vă conectați (vezi [Modul 3.1 - Primul Server](../01-first-server/README.md))
- Aplicația host instalată pe sistemul dumneavoastră
- Familiaritate de bază cu fișierele de configurare JSON

---

## 1. Claude Desktop

**Claude Desktop** este aplicația desktop oficială a Anthropic care suportă nativ MCP.

### Instalare

1. Descărcați Claude Desktop de la [claude.ai/download](https://claude.ai/download)
2. Instalați și conectați-vă cu contul dumneavoastră Anthropic

### Configurare

Claude Desktop utilizează un fișier de configurare JSON pentru a defini serverele MCP.

**Locația fișierului de configurare:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Exemplu de configurare:**

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

### Opțiuni de configurare

| Câmp | Descriere | Exemplu |
|-------|-------------|---------|
| `command` | Executabilul de rulat | `"python"`, `"node"`, `"npx"` |
| `args` | Argumente linie de comandă | `["-m", "my_server"]` |
| `env` | Variabile de mediu | `{"API_KEY": "xxx"}` |
| `cwd` | Director de lucru | `"/path/to/server"` |

### Testarea configurării

1. Salvați fișierul de configurare
2. Repornirea completă a Claude Desktop (închideți și redeschideți)
3. Deschideți o conversație nouă
4. Căutați pictograma 🔌 care indică servere conectate
5. Încercați să îi cereți lui Claude să folosească unul dintre instrumentele dumneavoastră

### Depanare Claude Desktop

**Serverul nu apare:**
- Verificați sintaxa fișierului de configurare cu un validator JSON
- Asigurați-vă că calea către comandă este corectă
- Verificați jurnalele Claude Desktop: Ajutor → Afișare jurnale

**Serverul se prăbușește la pornire:**
- Testați serverul manual în terminal mai întâi
- Verificați dacă variabilele de mediu sunt setate corect
- Asigurați-vă că toate dependențele sunt instalate

---

## 2. VS Code cu GitHub Copilot

VS Code suportă MCP prin extensiile GitHub Copilot Chat.

### Cerințe preliminare

1. VS Code 1.99+ instalat
2. Extensia GitHub Copilot instalată
3. Extensia GitHub Copilot Chat instalată

### Configurare

VS Code folosește `.vscode/mcp.json` în spațiul de lucru sau în setările utilizatorului.

**Configurarea spațiului de lucru** (`.vscode/mcp.json`):

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

**Setările utilizatorului** (`settings.json`):

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

### Utilizarea MCP în VS Code

1. Deschideți panoul Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Tastați `@` pentru a vedea uneltele MCP disponibile
3. Folosiți limbaj natural pentru a invoca uneltele: „Calculează 25 * 48 folosind calculatorul”

### Depanare VS Code

**Serverele MCP nu se încarcă:**
- Verificați panoul Output → „MCP” pentru jurnale de erori
- Reîncărcați fereastra: Ctrl+Shift+P → „Developer: Reload Window”
- Verificați dacă serverul rulează independent mai întâi

---

## 3. Cursor

**Cursor** este un editor de cod orientat AI cu suport integrat MCP.

### Instalare

1. Descărcați Cursor de la [cursor.sh](https://cursor.sh)
2. Instalați și conectați-vă

### Configurare

Cursor utilizează un format de configurare similar cu Claude Desktop.

**Locația fișierului de configurare:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Exemplu de configurare:**

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

### Utilizarea MCP în Cursor

1. Deschideți chatul AI al lui Cursor (Ctrl+L / Cmd+L)
2. Uneltele MCP apar automat în sugestii
3. Cereți AI-ului să efectueze sarcini folosind serverele conectate

---

## 4. Cline (bazat pe terminal)

**Cline** este un client MCP bazat pe terminal, ideal pentru fluxuri de lucru în linie de comandă.

### Instalare

```bash
npm install -g @anthropic/cline
```

### Configurare

Cline utilizează variabile de mediu și argumente în linia de comandă.

**Folosind variabile de mediu:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Folosind argumente în linia de comandă:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Fișier de configurare** (`~/.clinerc`):

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

### Utilizarea Cline

```bash
# Începe o sesiune interactivă
cline

# Interogare unică cu MCP
cline "Calculate the square root of 144 using the calculator"

# Listează uneltele disponibile
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** este un alt editor de cod cu suport AI și MCP.

### Instalare

1. Descărcați Windsurf de la [codeium.com/windsurf](https://codeium.com/windsurf)
2. Instalați și creați un cont

### Configurare

Configurarea Windsurf se gestionează prin interfața grafică de setări:

1. Deschideți Setările (Ctrl+, / Cmd+,)
2. Căutați „MCP”
3. Dați click pe „Edit in settings.json”

**Exemplu de configurare:**

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

## Compararea tipurilor de transport

Hosturi diferite susțin mecanisme diferite de transport:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (intrare/ieșire standard): Cel mai bun pentru servere locale pornite de host
**SSE/HTTP**: Cel mai bun pentru servere remote sau servere partajate între mai mulți clienți

---

## Probleme comune de depanare

### Serverul nu pornește

1. **Testați serverul manual mai întâi:**
   ```bash
   # Pentru Python
   python -m your_server_module
   
   # Pentru Node.js
   node /path/to/server/index.js
   ```

2. **Verificați calea către comandă:**
   - Folosiți căi absolute când este posibil
   - Asigurați-vă că executabilul este în PATH

3. **Verificați dependențele:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Serverul se conectează, dar instrumentele nu funcționează

1. **Verificați jurnalele serverului** - Majoritatea hosturilor au opțiuni de logging
2. **Verificați înregistrarea uneltelor** - Folosiți MCP Inspector pentru testare
3. **Verificați permisiunile** - Unele unelte necesită acces la fișiere/rețea

### Variabilele de mediu nu sunt transmise

- Unele hosturi sanitizează variabilele de mediu
- Folosiți explicit câmpul de configurare `env`
- Evitați datele sensibile în fișierele de configurare (folosiți managementul secretelor)

---

## Cele mai bune practici de securitate

1. **Nu comiteți niciodată cheile API** în fișierele de configurare
2. **Folosiți variabile de mediu** pentru date sensibile
3. **Limitați permisiunile serverului** doar la ce este necesar
4. **Revizuiți codul serverului** înainte de a acorda acces la sistemul dumneavoastră
5. **Folosiți liste de permisiuni** pentru accesul la sistemul de fișiere și rețea

---

## Ce urmează

- [3.13 - Depanare cu MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Creați primul server MCP](../01-first-server/README.md)
- [Modul 5 - Subiecte Avansate](../../05-AdvancedTopics/README.md)

---

## Resurse suplimentare

- [Documentația Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Extensia VS Code MCP](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Specificația MCP - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Registrul oficial al serverelor MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->