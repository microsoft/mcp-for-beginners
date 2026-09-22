# Postavljanje popularnih MCP klijentskih aplikacija

> [!NOTE]
> Konfiguracije hosta koje upućuju na `/sse` su naslijeđeni primjeri HTTP+SSE za
> MCP `2025-11-25`. Za MCP `2026-07-28`, odaberite Streamable HTTP kod hostova koji
> to podržavaju i koristite krajnu točku konfiguriranu od strane servera.

Ovaj vodič pokriva kako konfigurirati i koristiti MCP servere s popularnim AI host aplikacijama. Svaki host ima svoj način konfiguracije, ali jednom podeseni, svi komuniciraju s MCP serverima koristeći standardizirani protokol.

## Što je MCP Host?

**MCP Host** je AI aplikacija koja se može spojiti na MCP servere kako bi proširila svoje mogućnosti. Zamislite ga kao "prednji kraj" s kojim korisnici komuniciraju, dok MCP serveri pružaju "stražnji kraj" alate i podatke.

```mermaid
flowchart LR
    User[👤 Korisnik] --> Host[🖥️ MCP Poslužitelj]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Popularni Poslužitelji"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Preduvjeti

- MCP server na koji se treba spojiti (pogledajte [Modul 3.1 - Prvi server](../01-first-server/README.md))
- Host aplikacija instalirana na vašem sustavu
- Osnovno poznavanje JSON konfiguracijskih datoteka

---

## 1. Claude Desktop

**Claude Desktop** je službena desktop aplikacija Anthropic-a koja nativno podržava MCP.

### Instalacija

1. Preuzmite Claude Desktop s [claude.ai/download](https://claude.ai/download)
2. Instalirajte i prijavite se sa svojim Anthropic računom

### Konfiguracija

Claude Desktop koristi JSON konfiguracijsku datoteku za definiranje MCP servera.

**Lokacija konfiguracijske datoteke:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Primjer konfiguracije:**

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

### Opcije konfiguracije

| Polje | Opis | Primjer |
|-------|-------------|---------|
| `command` | Izvršna datoteka koja se pokreće | `"python"`, `"node"`, `"npx"` |
| `args` | Argumenti naredbenog retka | `["-m", "my_server"]` |
| `env` | Varijable okoline | `{"API_KEY": "xxx"}` |
| `cwd` | Radni direktorij | `"/path/to/server"` |

### Testiranje vaše postavke

1. Spremite konfiguracijsku datoteku
2. Potpuno ponovno pokrenite Claude Desktop (ugasi i ponovno otvori)
3. Otvorite novi razgovor
4. Potražite ikonu 🔌 koja označava povezane servere
5. Pokušajte pitati Claudea da koristi jedan od vaših alata

### Rješavanje problema s Claude Desktopom

**Server se ne pojavljuje:**
- Provjerite sintaksu konfiguracijske datoteke s JSON validatorom
- Provjerite je li putanja naredbe ispravna
- Provjerite logove Claude Desktop-a: Help → Show Logs

**Server se ruši prilikom pokretanja:**
- Prvo ručno testirajte svoj server u terminalu
- Provjerite jesu li varijable okoline ispravno postavljene
- Osigurajte da su sve ovisnosti instalirane

---

## 2. VS Code s GitHub Copilotom

VS Code podržava MCP putem proširenja GitHub Copilot Chat.

### Preduvjeti

1. Instaliran VS Code 1.99+
2. Instalirano GitHub Copilot proširenje
3. Instalirano GitHub Copilot Chat proširenje

### Konfiguracija

VS Code koristi `.vscode/mcp.json` u vašem radnom prostoru ili korisničkim postavkama.

**Konfiguracija radnog prostora** (`.vscode/mcp.json`):

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

**Korisničke postavke** (`settings.json`):

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

### Korištenje MCP-a u VS Code-u

1. Otvorite Copilot Chat panel (Ctrl+Shift+I / Cmd+Shift+I)
2. Upisujte `@` da vidite dostupne MCP alate
3. Koristite prirodni jezik za pozivanje alata: "Izračunaj 25 * 48 koristeći kalkulator"

### Rješavanje problema s VS Code-om

**MCP serveri se ne učitavaju:**
- Provjerite Output panel → "MCP" za zapis pogrešaka
- Ponovno učitajte prozor: Ctrl+Shift+P → "Developer: Reload Window"
- Provjerite prvo da se server može pokrenuti samostalno

---

## 3. Cursor

**Cursor** je AI-prvi uređivač koda s ugrađenom podrškom za MCP.

### Instalacija

1. Preuzmite Cursor s [cursor.sh](https://cursor.sh)
2. Instalirajte i prijavite se

### Konfiguracija

Cursor koristi sličan format konfiguracije kao Claude Desktop.

**Lokacija konfiguracijske datoteke:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Primjer konfiguracije:**

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

### Korištenje MCP-a u Cursoru

1. Otvorite AI chat u Cursoru (Ctrl+L / Cmd+L)
2. MCP alati se automatski pojavljuju u sugestijama
3. Pitajte AI da izvrši zadatke koristeći spojene servere

---

## 4. Cline (Terminal-Based)

**Cline** je MCP klijent baziran na terminalu, idealan za rad u komandnoj liniji.

### Instalacija

```bash
npm install -g @anthropic/cline
```

### Konfiguracija

Cline koristi varijable okoline i argumente komandne linije.

**Korištenje varijabli okoline:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Korištenje argumenata komandne linije:**

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

### Korištenje Cline-a

```bash
# Pokreni interaktivnu sesiju
cline

# Jednostavni upit s MCP-om
cline "Calculate the square root of 144 using the calculator"

# Nabroj dostupne alate
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** je još jedan uređivač koda s podrškom za MCP pokretan AI-jem.

### Instalacija

1. Preuzmite Windsurf s [codeium.com/windsurf](https://codeium.com/windsurf)
2. Instalirajte i kreirajte račun

### Konfiguracija

Windsurf konfiguracija se upravlja kroz UI postavki:

1. Otvorite Postavke (Ctrl+, / Cmd+,)
2. Potražite "MCP"
3. Kliknite "Uredi u settings.json"

**Primjer konfiguracije:**

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

## Usporedba tipova transporta

Različiti hostovi podržavaju različite mehanizme transporta:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standardni ulaz/izlaz): Najbolje za lokalne servere koje host pokreće
**SSE/HTTP**: Najbolje za udaljene servere ili servere zajednički korištene među više klijenata

---

## Uobičajeno rješavanje problema

### Server se neće pokrenuti

1. **Prvo ručno testirajte server:**
   ```bash
   # Za Python
   python -m your_server_module
   
   # Za Node.js
   node /path/to/server/index.js
   ```

2. **Provjerite putanju naredbe:**
   - Koristite apsolutne putanje kad je moguće
   - Provjerite je li izvršna datoteka u vašem PATH-u

3. **Provjerite ovisnosti:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server se spoji, ali alati ne rade

1. **Provjerite logove servera** - Većina hostova ima opcije bilježenja
2. **Provjerite registraciju alata** - Koristite MCP Inspector za testiranje
3. **Provjerite dozvole** - Neki alati zahtijevaju pristup datotekama/mreži

### Varijable okoline se ne prenose

- Neki hostovi pročišćavaju varijable okoline
- Izričito koristite `env` polje u konfiguraciji
- Izbjegavajte osjetljive podatke u konfiguracijskim datotekama (koristite upravljanje tajnama)

---

## Najbolje sigurnosne prakse

1. **Nikada ne pohranjujte API ključeve** u konfiguracijske datoteke
2. **Koristite varijable okoline** za osjetljive podatke
3. **Ograničite dozvole servera** samo na potrebne
4. **Pregledajte kod servera** prije nego što mu dopustite pristup vašem sustavu
5. **Koristite liste dopuštenih** za pristup datotečnom sustavu i mreži

---

## Što slijedi

- [3.13 - Debugging with MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Kreirajte svoj prvi MCP server](../01-first-server/README.md)
- [Modul 5 - Napredne teme](../../05-AdvancedTopics/README.md)

---

## Dodatni resursi

- [Claude Desktop MCP dokumentacija](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP proširenje](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP specifikacija - Transporti](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Službeni registar MCP servera](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->