# Nastavitev priljubljenih MCP gostiteljskih odjemalcev

> [!NOTE]
> Nastavitve gostiteljev, ki kažejo na `/sse`, so zastareli primeri HTTP+SSE za
> MCP `2025-11-25`. Za MCP `2026-07-28` izberite Streamable HTTP pri gostiteljih, ki 
> to podpirajo, in uporabite konec točke, ki jo nastavi strežnik.

Ta vodič pokriva, kako konfigurirati in uporabljati MCP strežnike s priljubljenimi aplikacijami za gostitelje AI. Vsak gostitelj ima svoj pristop konfiguracije, a ko so nastavljeni, vsi komunicirajo z MCP strežniki s standardiziranim protokolom.

## Kaj je MCP gostitelj?

**MCP gostitelj** je AI aplikacija, ki se lahko poveže z MCP strežniki za razširitev svojih zmogljivosti. Predstavljajte si ga kot "sprednji del", s katerim uporabniki upravljajo, medtem ko MCP strežniki nudijo "zadnji del" orodij in podatkov.

```mermaid
flowchart LR
    User[👤 Uporabnik] --> Host[🖥️ MCP Gostitelj]
    Host --> S1[MCP Strežnik A]
    Host --> S2[MCP Strežnik B]
    Host --> S3[MCP Strežnik C]
    
    subgraph "Priljubljeni gostitelji"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Predpogoji

- MCP strežnik, s katerim se boste povezali (glej [Modul 3.1 - Prvi strežnik](../01-first-server/README.md))
- Gostiteljska aplikacija nameščena na vašem sistemu
- Osnovno poznavanje JSON konfiguracijskih datotek

---

## 1. Claude Desktop

**Claude Desktop** je uradna namizna aplikacija podjetja Anthropic, ki izvorno podpira MCP.

### Namestitev

1. Prenesite Claude Desktop s [claude.ai/download](https://claude.ai/download)
2. Namestite in se prijavite z vašim Anthropic računom

### Konfiguracija

Claude Desktop uporablja JSON konfiguracijsko datoteko za določanje MCP strežnikov.

**Lokacija konfiguracijske datoteke:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Primer konfiguracije:**

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

### Možnosti konfiguracije

| Polje | Opis | Primer |
|-------|-------------|---------|
| `command` | Izvedljiva datoteka za zagon | `"python"`, `"node"`, `"npx"` |
| `args` | Argumenti ukazne vrstice | `["-m", "my_server"]` |
| `env` | Spremeljivke okolja | `{"API_KEY": "xxx"}` |
| `cwd` | Delovni imenik | `"/path/to/server"` |

### Preizkus vaše nastavitve

1. Shrani konfiguracijsko datoteko
2. Povsem ponovno zaženi Claude Desktop (izhod in ponovno odpri)
3. Odpri nov pogovor
4. Poišči ikono 🔌, ki označuje povezane strežnike
5. Poskusi vprašati Claude, naj uporabi eno od tvojih orodij

### Odpravljanje težav pri Claude Desktop

**Strežnik se ne prikaže:**
- Preveri sintakso konfiguracijske datoteke z JSON validatorjem
- Prepričaj se, da je pot do ukaza pravilna
- Preveri dnevnike Claude Desktop: Pomoč → Prikaži dnevnike

**Strežnik se zruši ob zagonu:**
- Najprej ročno preizkusi strežnik v terminalu
- Preveri, da so okoljske spremenljivke pravilno nastavljene
- Prepričaj se, da so vse odvisnosti nameščene

---

## 2. VS Code z GitHub Copilot

VS Code podpira MCP preko razširitev GitHub Copilot Chat.

### Predpogoji

1. Nameščen VS Code verzije 1.99 ali višje
2. Nameščena GitHub Copilot razširitev
3. Nameščena GitHub Copilot Chat razširitev

### Konfiguracija

VS Code uporablja `.vscode/mcp.json` v vašem delovnem prostoru ali uporabniških nastavitvah.

**Konfiguracija delovnega prostora** (`.vscode/mcp.json`):

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

**Uporabniške nastavitve** (`settings.json`):

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

### Uporaba MCP v VS Code

1. Odpri ploščo Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Vnesi `@` za prikaz razpoložljivih MCP orodij
3. Uporabi naravni jezik za klicanje orodij: "Izračunaj 25 * 48 z uporabo kalkulatorja"

### Odpravljanje težav v VS Code

**MCP strežniki se ne nalagajo:**
- Preveri zavihek Izhod → "MCP" za zaznamke o napakah
- Osveži okno: Ctrl+Shift+P → "Developer: Reload Window"
- Najprej preveri, ali strežnik deluje samostojno

---

## 3. Cursor

**Cursor** je kodni urejevalnik, zasnovan za AI, z vgrajeno podporo MCP.

### Namestitev

1. Prenesite Cursor s [cursor.sh](https://cursor.sh)
2. Namestite in se prijavite

### Konfiguracija

Cursor uporablja podoben format konfiguracije kot Claude Desktop.

**Lokacija konfiguracijske datoteke:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Primer konfiguracije:**

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

### Uporaba MCP v Cursor

1. Odpri AI klepet Cursorja (Ctrl+L / Cmd+L)
2. Orodja MCP se samodejno pojavijo v predlogah
3. Prosi AI, da opravi naloge z uporabo povezanih strežnikov

---

## 4. Cline (na osnovi terminala)

**Cline** je MCP odjemalec, ki temelji na terminalu, idealen za ukazne tokove.

### Namestitev

```bash
npm install -g @anthropic/cline
```

### Konfiguracija

Cline uporablja okoljske spremenljivke in argumente ukazne vrstice.

**Uporaba okoljskih spremenljivk:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Uporaba argumentov ukazne vrstice:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfiguracijska datoteka** (`~/.clinerc`):

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

### Uporaba Cline

```bash
# Začni interaktivno sejo
cline

# Posamezen poizvedba z MCP
cline "Calculate the square root of 144 using the calculator"

# Naštej razpoložljiva orodja
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** je še en urejevalnik kode, ki ga poganja AI, z MCP podporo.

### Namestitev

1. Prenesite Windsurf s [codeium.com/windsurf](https://codeium.com/windsurf)
2. Namestite in ustvarite račun

### Konfiguracija

Konfiguracija Windsurfa se upravlja preko uporabniškega vmesnika nastavitev:

1. Odpri Nastavitve (Ctrl+, / Cmd+,)
2. Poišči "MCP"
3. Klikni "Uredi v settings.json"

**Primer konfiguracije:**

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

## Primerjava vrst prenosov

Različni gostitelji podpirajo različne transportne mehanizme:

| Gostitelj | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standardni vhod/izhod): Najboljše za lokalne strežnike, ki jih zažene gostitelj
**SSE/HTTP**: Najboljše za oddaljene strežnike ali strežnike, ki jih uporablja več odjemalcev

---

## Pogoste težave pri odpravljanju

### Strežnik se ne zažene

1. **Najprej ročno testirajte strežnik:**
   ```bash
   # Za Python
   python -m your_server_module
   
   # Za Node.js
   node /path/to/server/index.js
   ```

2. **Preverite pot ukaza:**
   - Po potrebi uporabljajte absolutne poti
   - Prepričajte se, da je izvršljiva datoteka v vaši poti PATH

3. **Preverite odvisnosti:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Strežnik se poveže, ampak orodja ne delujejo

1. **Preverite dnevnike strežnika** - Večina gostiteljev ima možnosti beleženja
2. **Preverite registracijo orodij** - Uporabite MCP Inspector za testiranje
3. **Preverite dovoljenja** - Nekatera orodja potrebujejo dostop do datotek/omrežja

### Okoljske spremenljivke niso posredovane

- Nekateri gostitelji očistijo okoljske spremenljivke
- Izrecno uporabite polje za okolje `env` v konfiguraciji
- Izogibajte se občutljivim podatkom v konfiguracijskih datotekah (uporabite upravljanje skrivnosti)

---

## Najboljše prakse varnosti

1. **Nikoli ne vključujte API ključev** v konfiguracijske datoteke
2. **Uporabljajte okoljske spremenljivke** za občutljive podatke
3. **Omejite dovoljenja strežnika** samo na potrebno
4. **Preglejte strežniško kodo** pred podelitvijo dostopa do vašega sistema
5. **Uporabite sezname dovoljenih** za dostop do datotečnega sistema in omrežja

---

## Kaj sledi

- [3.13 - Razhroščevanje z MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Ustvarite svoj prvi MCP strežnik](../01-first-server/README.md)
- [Modul 5 - Napredne teme](../../05-AdvancedTopics/README.md)

---

## Dodatni viri

- [Dokumentacija Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Razširitev](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP specifikacija - Prenosi](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Uradni register MCP strežnikov](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->