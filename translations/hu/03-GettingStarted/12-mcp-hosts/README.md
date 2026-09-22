# Népszerű MCP Host Kliensek Beállítása

> [!NOTE]
> A `/sse`-re mutató host konfigurációk a MCP `2025-11-25` verzióhoz tartozó hagyományos HTTP+SSE példák.
> Az MCP `2026-07-28` esetén válassza a Streamable HTTP-t azokban a hosztokban, amelyek támogatják,
> és használja a szerver által beállított végpontot.

Ez az útmutató arra tér ki, hogyan lehet népszerű AI host alkalmazásokkal MCP szervereket konfigurálni és használni. Minden hostnak megvan a saját konfigurációs módja, de ha egyszer beállították, mindegyik szabványosított protokoll segítségével kommunikál az MCP szerverekkel.

## Mi az az MCP Host?

Az **MCP Host** egy olyan AI alkalmazás, amely képes kapcsolódni MCP szerverekhez képességeinek kibővítése érdekében. Olyan, mint a "front end", amelyet a felhasználók használnak, míg az MCP szerverek a "back end" eszközöket és adatokat szolgáltatják.

```mermaid
flowchart LR
    User[👤 Felhasználó] --> Host[🖥️ MCP Gazdagép]
    Host --> S1[MCP Szerver A]
    Host --> S2[MCP Szerver B]
    Host --> S3[MCP Szerver C]
    
    subgraph "Népszerű gazdagépek"
        H1[Claude Asztali]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Előfeltételek

- Egy MCP szerver, amelyhez kapcsolódni lehet (lásd [Module 3.1 - First Server](../01-first-server/README.md))
- A host alkalmazás telepítve az Ön rendszerén
- Alapvető ismeretek a JSON konfigurációs fájlokról

---

## 1. Claude Desktop

A **Claude Desktop** az Anthropic hivatalos asztali alkalmazása, amely natívan támogatja az MCP-t.

### Telepítés

1. Töltse le a Claude Desktopot innen: [claude.ai/download](https://claude.ai/download)
2. Telepítse, és jelentkezzen be Anthropic fiókjával

### Konfiguráció

A Claude Desktop JSON konfigurációs fájlt használ az MCP szerverek definiálásához.

**Konfigurációs fájl helye:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Példa konfiguráció:**

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

### Konfigurációs Opciók

| Mező | Leírás | Példa |
|-------|-------------|---------|
| `command` | A futtatandó végrehajtható fájl | `"python"`, `"node"`, `"npx"` |
| `args` | Parancssori argumentumok | `["-m", "my_server"]` |
| `env` | Környezeti változók | `{"API_KEY": "xxx"}` |
| `cwd` | Munkakönyvtár | `"/path/to/server"` |

### A Beállítás Tesztelése

1. Mentse el a konfigurációs fájlt
2. Indítsa újra teljesen a Claude Desktopot (zárja be és nyissa meg újra)
3. Nyisson új beszélgetést
4. Keresse a 🔌 ikont, ami a kapcsolódó szervereket jelzi
5. Próbálja meg megkérni Claudet, hogy használjon egy eszközt

### Claude Desktop Hibakeresés

**Szerver nem jelenik meg:**
- Ellenőrizze a konfigurációs fájl szintaxisát JSON ellenőrzővel
- Győződjön meg a parancs elérési útjának helyességéről
- Ellenőrizze a Claude Desktop naplóit: Help → Show Logs

**Szerver induláskor összeomlik:**
- Először kézzel tesztelje a szervert terminálon
- Ellenőrizze, hogy helyesen vannak-e beállítva a környezeti változók
- Győződjön meg róla, hogy minden függőség telepítve van

---

## 2. VS Code GitHub Copilot-tal

A VS Code támogatja az MCP-t a GitHub Copilot Chat kiterjesztéseken keresztül.

### Előfeltételek

1. Telepített VS Code 1.99 vagy újabb
2. Telepített GitHub Copilot kiterjesztés
3. Telepített GitHub Copilot Chat kiterjesztés

### Konfiguráció

A VS Code `.vscode/mcp.json` fájlt használ a munkaterületen vagy a felhasználói beállításokban.

**Munkaterület konfiguráció** (`.vscode/mcp.json`):

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

**Felhasználói beállítások** (`settings.json`):

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

### MCP használata VS Code-ban

1. Nyissa meg a Copilot Chat panelt (Ctrl+Shift+I / Cmd+Shift+I)
2. Gépelje be az `@` jelet az elérhető MCP eszközök megjelenítéséhez
3. Használjon természetes nyelvet az eszközök meghívásához: "Számold ki 25 * 48 a számológép segítségével"

### VS Code Hibakeresés

**MCP szerverek nem töltődnek be:**
- Ellenőrizze a Kimenet panel → "MCP" hibalogjait
- Ablak újratöltése: Ctrl+Shift+P → "Developer: Reload Window"
- Először ellenőrizze, hogy a szerver önállóan fut-e

---

## 3. Cursor

A **Cursor** egy AI-központú kód-szerkesztő, beépített MCP támogatással.

### Telepítés

1. Töltse le a Cursor-t innen: [cursor.sh](https://cursor.sh)
2. Telepítse és jelentkezzen be

### Konfiguráció

A Cursor hasonló konfigurációs formátumot használ, mint a Claude Desktop.

**Konfigurációs fájl helye:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Példa konfiguráció:**

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

### MCP használata Cursorban

1. Nyissa meg Cursor AI csetjét (Ctrl+L / Cmd+L)
2. Az MCP eszközök automatikusan megjelennek a javaslatokban
3. Kérje meg az AI-t, hogy végezze el a feladatokat a kapcsolódó szerverek segítségével

---

## 4. Cline (Terminál alapú)

A **Cline** egy terminál alapú MCP kliens, ideális parancssori workflow-khoz.

### Telepítés

```bash
npm install -g @anthropic/cline
```

### Konfiguráció

A Cline környezeti változókat és parancssori argumentumokat használ.

**Környezeti változók használata:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Parancssori argumentumok használata:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigurációs fájl** (`~/.clinerc`):

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

### Cline használata

```bash
# Interaktív munkamenet indítása
cline

# Egyetlen lekérdezés MCP-vel
cline "Calculate the square root of 144 using the calculator"

# Elérhető eszközök listázása
cline --list-tools
```

---

## 5. Windsurf

A **Windsurf** egy másik AI-alapú kódszerkesztő, amely MCP támogatással rendelkezik.

### Telepítés

1. Töltse le a Windsurf-et innen: [codeium.com/windsurf](https://codeium.com/windsurf)
2. Telepítse és hozzon létre fiókot

### Konfiguráció

A Windsurf konfigurációját a beállítások felületen keresztül kezelheti:

1. Nyissa meg a Beállításokat (Ctrl+, / Cmd+,)
2. Keressen rá a "MCP" kifejezésre
3. Kattintson az "Edit in settings.json" gombra

**Példa konfiguráció:**

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

## Szállítási Típusok Összehasonlítása

Különböző hosztok különböző szállítási mechanizmusokat támogatnak:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard bemenet/kimenet): A legjobb helyi szerverekhez, amelyeket a host indít
**SSE/HTTP**: A legjobb távoli vagy több kliens között megosztott szerverekhez

---

## Gyakori Hibakeresés

### A szerver nem indul el

1. **Először kézzel tesztelje a szervert:**
   ```bash
   # Pythonhoz
   python -m your_server_module
   
   # Node.js-hez
   node /path/to/server/index.js
   ```

2. **Ellenőrizze a parancs elérési útját:**
   - Amennyiben lehetséges, használjon abszolút elérési utat
   - Győződjön meg arról, hogy a végrehajtható a PATH-ban van

3. **Ellenőrizze a függőségeket:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### A szerver kapcsolódik, de az eszközök nem működnek

1. **Ellenőrizze a szerver naplóit** - A legtöbb hoszt rendelkezik naplózási lehetőségekkel
2. **Ellenőrizze az eszköz regisztrációját** - Használja az MCP Inspectort a teszteléshez
3. **Ellenőrizze a jogosultságokat** - Néhány eszköznek szüksége van fájl vagy hálózati hozzáférésre

### A környezeti változók nem jutnak át

- Egyes hosztok megtisztítják a környezeti változókat
- Használja az `env` konfigurációs mezőt kifejezetten
- Kerülje az érzékeny adatok konfigurációs fájlokban való tárolását (használjon titkoskezelést)

---

## Biztonsági Legjobb Gyakorlatok

1. **Sose adjon hozzá API kulcsokat** konfigurációs fájlokhoz
2. **Használjon környezeti változókat** érzékeny adatokhoz
3. **Korlátozza a szerver jogosultságait** csak a szükségesre
4. **Nézze át a szerver kódját** mielőtt hozzáférést ad a rendszeréhez
5. **Használjon engedélyezőlistákat** fájlrendszer és hálózati hozzáférésekhez

---

## Mi a következő?

- [3.13 - Hibakeresés MCP Inspectorral](../13-mcp-inspector/README.md)
- [3.1 - Első MCP szerver létrehozása](../01-first-server/README.md)
- [Modul 5 - Haladó témák](../../05-AdvancedTopics/README.md)

---

## További Források

- [Claude Desktop MCP Dokumentáció](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Kiterjesztés](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specifikáció - Szállítások](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Hivatalos MCP Szerverek Regisztere](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->