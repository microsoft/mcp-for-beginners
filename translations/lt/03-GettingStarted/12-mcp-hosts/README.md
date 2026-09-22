# Populiariausių MCP serverio klientų nustatymas

> [!NOTE]
> Serverio konfigūracijos, nurodančios į `/sse`, yra senstelėję HTTP+SSE pavyzdžiai MCP `2025-11-25` versijai. MCP `2026-07-28` naudokite Streamable HTTP tais serveriuose, kurie tai palaiko, ir naudokite serverio nustatytą galinį tašką.
> 
> 

Šiame vadove aprašoma, kaip konfigūruoti ir naudoti MCP serverius su populiariomis AI serverio programomis. Kiekvienas serveris turi savitą konfigūracijos metodą, tačiau po nustatymo visi jie bendrauja su MCP serveriais naudodami standartizuotą protokolą.

## Kas yra MCP serveris?

**MCP serveris** yra AI programėlė, galinti prisijungti prie MCP serverių ir išplėsti savo funkcionalumą. Galvokite apie jį kaip apie „priekinę dalį“, su kuria sąveikauja vartotojai, o MCP serveriai teikia „galinę dalį“ - įrankius ir duomenis.

```mermaid
flowchart LR
    User[👤 Vartotojas] --> Host[🖥️ MCP serverio šeimininkas]
    Host --> S1[MCP serveris A]
    Host --> S2[MCP serveris B]
    Host --> S3[MCP serveris C]
    
    subgraph "Populiarūs serveriai"
        H1[Claude darbalaukis]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Reikalavimai

- MCP serveris, prie kurio bus jungiamasi (žiūrėti [3.1 modulis - Pirmasis serveris](../01-first-server/README.md))
- Serverio programa įdiegta jūsų sistemoje
- Pagrindinės JSON konfigūracijos failų žinios

---

## 1. Claude Desktop

**Claude Desktop** yra oficiali Anthropic darbalaukio programa, kuri natūraliai palaiko MCP.

### Įdiegimas

1. Atsisiųskite Claude Desktop iš [claude.ai/download](https://claude.ai/download)
2. Įdiekite ir prisijunkite naudodami savo Anthropic paskyrą

### Konfigūracija

Claude Desktop naudoja JSON konfigūracijos failą MCP serveriams apibrėžti.

**Konfigūracijos failo vieta:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Konfigūracijos pavyzdys:**

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

### Konfigūracijos parinktys

| Laukas | Aprašymas | Pavyzdys |
|-------|------------|----------|
| `command` | Vykdomoji programa | `"python"`, `"node"`, `"npx"` |
| `args` | Komandinės eilutės argumentai | `["-m", "my_server"]` |
| `env` | Aplinkos kintamieji | `{"API_KEY": "xxx"}` |
| `cwd` | Darbo katalogas | `"/path/to/server"` |

### Nustatymo testavimas

1. Išsaugokite konfigūracijos failą
2. Pilnai perkraukite Claude Desktop (uždarykite ir vėl atidarykite)
3. Atidarykite naują pokalbį
4. Ieškokite 🔌 ikonos, rodančios prisijungusius serverius
5. Išbandykite paprašyti Claude naudoti vieną iš jūsų įrankių

### Claude Desktop trikčių šalinimas

**Serveris nerodomas:**
- Patikrinkite konfigūracijos failo sintaksę su JSON tikrintuvu
- Įsitikinkite, kad kelias iki komandos yra teisingas
- Peržiūrėkite Claude Desktop žurnalus: Pagalba → Rodyti žurnalus

**Serveris užstringa paleidžiant:**
- Iš pradžių rankiniu būdu išbandykite serverį terminale
- Patikrinkite, ar aplinkos kintamieji nustatyti teisingai
- Įsitikinkite, kad įdiegti visi reikalingi priklausiniai

---

## 2. VS Code su GitHub Copilot

VS Code palaiko MCP per GitHub Copilot Chat plėtinius.

### Reikalavimai

1. Įdiegta VS Code 1.99 ar naujesnė versija
2. Įdiegtas GitHub Copilot plėtinys
3. Įdiegtas GitHub Copilot Chat plėtinys

### Konfigūracija

VS Code naudoja `.vscode/mcp.json` jūsų darbo aplanke arba naudotojo nustatymuose.

**Darbo aplanko konfigūracija** (`.vscode/mcp.json`):

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

**Naudotojo nustatymai** (`settings.json`):

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

### MCP naudojimas VS Code

1. Atidarykite Copilot Chat panelę (Ctrl+Shift+I / Cmd+Shift+I)
2. Įveskite `@`, kad pamatytumėte galimus MCP įrankius
3. Naudokite natūralią kalbą įrankiams iškviesti: „Calculate 25 * 48 using the calculator“

### VS Code trikčių šalinimas

**MCP serveriai nesikrauna:**
- Patikrinkite Išvesties panelę → „MCP“ dėl klaidų žurnalų
- Perkraukite langą: Ctrl+Shift+P → „Developer: Reload Window“
- Patikrinkite, ar serveris pirmiausia veikia savarankiškai

---

## 3. Cursor

**Cursor** yra AI pirmiausia orientuotas kodo redaktorius su įmontuota MCP palaikymu.

### Įdiegimas

1. Atsisiųskite Cursor iš [cursor.sh](https://cursor.sh)
2. Įdiekite ir prisijunkite

### Konfigūracija

Cursor naudoja panašų konfigūracijos formatą kaip Claude Desktop.

**Konfigūracijos failo vieta:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Konfigūracijos pavyzdys:**

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

### MCP naudojimas Cursor

1. Atidarykite Cursor AI pokalbį (Ctrl+L / Cmd+L)
2. MCP įrankiai automatiškai rodomi pasiūlymuose
3. Paprašykite AI atlikti užduotis naudodami prijungtus serverius

---

## 4. Cline (Terminalinis klientas)

**Cline** yra terminalinis MCP klientas, tinkamas komandų eilutės darbams.

### Įdiegimas

```bash
npm install -g @anthropic/cline
```

### Konfigūracija

Cline naudoja aplinkos kintamuosius ir komandų eilutės argumentus.

**Naudojant aplinkos kintamuosius:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Naudojant komandų eilutės argumentus:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigūracijos failas** (`~/.clinerc`):

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

### Cline naudojimas

```bash
# Paleiskite interaktyvią sesiją
cline

# Vienas užklausimas su MCP
cline "Calculate the square root of 144 using the calculator"

# Išvardinkite turimus įrankius
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** yra dar vienas AI pagrindu veikiantis kodo redaktorius su MCP palaikymu.

### Įdiegimas

1. Atsisiųskite Windsurf iš [codeium.com/windsurf](https://codeium.com/windsurf)
2. Įdiekite ir susikurkite paskyrą

### Konfigūracija

Windsurf konfigūracijos valdomos per nustatymų naudotojo sąsają:

1. Atidarykite Nustatymus (Ctrl+, / Cmd+,)
2. Ieškokite „MCP“
3. Spauskite „Redaguoti settings.json faile“

**Konfigūracijos pavyzdys:**

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

## Transporto tipų palyginimas

Skirtingi serveriai palaiko skirtingus perdavimo mechanizmus:

| Serveris | stdio | SSE/HTTP | WebSocket |
|---------|--------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standartinis įvesties/išvesties srautas): Geriausias vietiniams serveriams, paleistiems prijungto serverio programos.
**SSE/HTTP**: Geriausias nuotoliniams serveriams arba serveriams, dalijamiems tarp kelių klientų.

---

## Dažnos problemos ir jų sprendimai

### Serveris nepaleidžiamas

1. **Pirmiausia rankiniu būdu išbandykite serverį:**
   ```bash
   # Skirta Python
   python -m your_server_module
   
   # Skirta Node.js
   node /path/to/server/index.js
   ```

2. **Patikrinkite komandos kelią:**

   - Naudokite absoliučius kelius, kai įmanoma
   - Užtikrinkite, kad vykdomasis failas būtų jūsų PATH

3. **Patikrinkite priklausomybes:**
   ```bash
   # Pythonas
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Serveris prisijungia, bet įrankiai neveikia

1. **Patikrinkite serverio žurnalus** – dauguma prieglobų turi žurnalų parinktis
2. **Patikrinkite įrankių registraciją** – naudokite MCP Inspector testavimui
3. **Patikrinkite leidimus** – kai kuriems įrankiams reikalingas prieigos prie failų/tinklo leidimas

### Aplinka kintamieji neperduodami

- Kai kurie prieglobos išvalo aplinkos kintamuosius
- Naudokite `env` konfigūracijos lauką aiškiai
- Venkite jautrių duomenų konfigūracijos failuose (naudokite slaptų duomenų valdymą)

---

## Saugumo geros praktikos

1. **Niekada nekelkite API raktų** į konfigūracijos failus
2. **Naudokite aplinkos kintamuosius** jautriems duomenims
3. **Apribokite serverio leidimus** tik tai, kas būtina
4. **Peržiūrėkite serverio kodą** prieš suteikdami prieigą prie savo sistemos
5. **Naudokite leidimų sąrašus** prieigai prie failų sistemos ir tinklo

---

## Kas toliau

- [3.13 - Trikčių šalinimas naudojant MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Sukurkite savo pirmąjį MCP serverį](../01-first-server/README.md)
- [5 modulis - Pažangios temos](../../05-AdvancedTopics/README.md)

---

## Papildomi ištekliai

- [Claude Desktop MCP dokumentacija](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP plėtinys](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP specifikacija - Transportai](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Oficialus MCP serverių registras](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->