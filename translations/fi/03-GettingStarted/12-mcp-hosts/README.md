# Suosittujen MCP-isäntäasiakkaiden asetukset

> [!NOTE]
> Isäntäkonfiguraatiot, jotka osoittavat `/sse`-polulle, ovat vanhentuneita HTTP+SSE-esimerkkejä
> MCP `2025-11-25` -versiolle. MCP `2026-07-28` -versiossa valitse Streamable HTTP isännissä, jotka
> tukevat sitä, ja käytä palvelimen määrittämää päätepistettä.

Tämä opas kattaa, kuinka konfiguroida ja käyttää MCP-palvelimia suosittujen tekoälyisäntäohjelmien kanssa. Jokaisella isännällä on oma konfiguraatiotapansa, mutta kun ne on asennettu, ne kaikki kommunikoivat MCP-palvelimien kanssa standardisoidun protokollan avulla.

## Mikä on MCP-isäntä?

**MCP-isäntä** on tekoälysovellus, joka voi muodostaa yhteyden MCP-palvelimiin laajentaakseen toiminnallisuuttaan. Ajattele sitä "käyttöliittymänä", jonka kanssa käyttäjät ovat tekemisissä, kun taas MCP-palvelimet tarjoavat "taustan" työkalut ja datan.

```mermaid
flowchart LR
    User[👤 Käyttäjä] --> Host[🖥️ MCP Isäntä]
    Host --> S1[MCP Palvelin A]
    Host --> S2[MCP Palvelin B]
    Host --> S3[MCP Palvelin C]
    
    subgraph "Suositut Isännät"
        H1[Claude Pöytäkone]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Vaatimukset

- MCP-palvelin, johon muodostetaan yhteys (katso [Moduuli 3.1 - Ensimmäinen palvelin](../01-first-server/README.md))
- Isäntäohjelma asennettuna järjestelmääsi
- Perustason tuttuus JSON-konfiguraatiotiedostojen kanssa

---

## 1. Claude Desktop

**Claude Desktop** on Anthropicin virallinen työpöytäsovellus, joka tukee MCP:tä natiivisti.

### Asennus

1. Lataa Claude Desktop osoitteesta [claude.ai/download](https://claude.ai/download)
2. Asenna ja kirjaudu sisään Anthropic-tililläsi

### Konfigurointi

Claude Desktop käyttää JSON-konfiguraatiotiedostoa MCP-palvelimien määrittämiseen.

**Konfiguraatiotiedoston sijainti:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Esimerkkikonfiguraatio:**

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

### Konfiguraatioasetukset

| Kenttä | Kuvaus | Esimerkki |
|-------|---------|----------|
| `command` | Suoritettava ohjelma | `"python"`, `"node"`, `"npx"` |
| `args` | Komentoriviparametrit | `["-m", "my_server"]` |
| `env` | Ympäristömuuttujat | `{"API_KEY": "xxx"}` |
| `cwd` | Työhakemisto | `"/path/to/server"` |

### Asetusten testaus

1. Tallenna konfiguraatiotiedosto
2. Käynnistä Claude Desktop täysin uudelleen (lopeta ja käynnistä uudelleen)
3. Avaa uusi keskustelu
4. Etsi 🔌-kuvake, joka näyttää yhdistetyt palvelimet
5. Kokeile pyytää Claudea käyttämään jotain työkalujasi

### Vianmääritys Claude Desktopissa

**Palvelin ei näy:**
- Tarkista konfiguraatiotiedoston syntaksi JSON-validointityökalulla
- Varmista, että komenton polku on oikea
- Tarkista Claude Desktopin lokit: Ohje → Näytä lokit

**Palvelin kaatuu käynnistyksessä:**
- Testaa palvelinta ensin manuaalisesti terminaalissa
- Tarkista, että ympäristömuuttujat on asetettu oikein
- Varmista, että kaikki riippuvuudet on asennettu

---

## 2. VS Code GitHub Copilotin kanssa

VS Code tukee MCP:tä GitHub Copilot Chat -laajennusten avulla.

### Vaatimukset

1. VS Code versio 1.99 tai uudempi asennettuna
2. GitHub Copilot -laajennus asennettuna
3. GitHub Copilot Chat -laajennus asennettuna

### Konfigurointi

VS Code käyttää `.vscode/mcp.json` -tiedostoa työtila- tai käyttäjäasetuksissa.

**Työtilan konfiguraatio** (`.vscode/mcp.json`):

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

**Käyttäjäasetukset** (`settings.json`):

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

### MCP:n käyttö VS Codessa

1. Avaa Copilot Chat -paneeli (Ctrl+Shift+I / Cmd+Shift+I)
2. Kirjoita `@` nähdäksesi käytettävissä olevat MCP-työkalut
3. Käytä luonnollista kieltä kutsuaksesi työkaluja: "Laske 25 * 48 laskimella"

### VS Coden vianmääritys

**MCP-palvelimet eivät lataudu:**
- Tarkista Tulostuspaneeli → "MCP" virhelokeista
- Lataa ikkuna uudelleen: Ctrl+Shift+P → "Developer: Reload Window"
- Varmista, että palvelin toimii itsenäisesti ensin

---

## 3. Cursor

**Cursor** on tekoälyyn perustuva koodieditori, jossa on sisäänrakennettu MCP-tuki.

### Asennus

1. Lataa Cursor osoitteesta [cursor.sh](https://cursor.sh)
2. Asenna ja kirjaudu sisään

### Konfigurointi

Cursor käyttää samankaltaista konfiguraatiomuotoa kuin Claude Desktop.

**Konfiguraatiotiedoston sijainti:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Esimerkkikonfiguraatio:**

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

### MCP:n käyttö Cursorissa

1. Avaa Cursorin tekoälykeskustelu (Ctrl+L / Cmd+L)
2. MCP-työkalut näkyvät automaattisesti ehdotuksissa
3. Pyydä tekoälyä suorittamaan tehtäviä yhdistettyjen palvelimien avulla

---

## 4. Cline (Pääteperustainen)

**Cline** on pääteperustainen MCP-asiakas, ihanteellinen komentorivityönkulkuun.

### Asennus

```bash
npm install -g @anthropic/cline
```

### Konfigurointi

Cline käyttää ympäristömuuttujia ja komentoriviparametreja.

**Ympäristömuuttujien käyttö:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Komentoriviparametrien käyttö:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfiguraatiotiedosto** (`~/.clinerc`):

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

### Clinén käyttö

```bash
# Aloita interaktiivinen istunto
cline

# Yksittäinen kysely MCP:llä
cline "Calculate the square root of 144 using the calculator"

# Lista käytettävissä olevista työkaluista
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** on toinen MCP:tä tukeva tekoälyllä varustettu koodieditori.

### Asennus

1. Lataa Windsurf osoitteesta [codeium.com/windsurf](https://codeium.com/windsurf)
2. Asenna ja luo tili

### Konfigurointi

Windsurfin konfigurointi tapahtuu asetusten käyttöliittymän kautta:

1. Avaa asetukset (Ctrl+, / Cmd+,)
2. Etsi "MCP"
3. Klikkaa "Muokkaa tiedostossa settings.json"

**Esimerkkikonfiguraatio:**

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

## Kuljetustyyppien vertailu

Eri isännät tukevat eri kuljetusmekanismeja:

| Isäntä | stdio | SSE/HTTP | WebSocket |
|--------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard input/output): Paras tapa paikallisille palvelimille, jotka isäntä käynnistää
**SSE/HTTP**: Paras tapa etäpalvelimille tai palvelimille, joita jaetaan useiden asiakkaiden kesken

---

## Yleiset vianmääritykset

### Palvelin ei käynnisty

1. **Testaa palvelin ensin manuaalisesti:**
   ```bash
   # Pythonille
   python -m your_server_module
   
   # Node.js:lle
   node /path/to/server/index.js
   ```

2. **Tarkista komennon polku:**
   - Käytä absoluuttisia polkuja mahdollisuuksien mukaan
   - Varmista, että suoritettava ohjelma on PATH:ssa

3. **Vahvista riippuvuudet:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Palvelin yhdistyy, mutta työkalut eivät toimi

1. **Tarkista palvelimen lokit** - Useimmissa isännissä on lokitusvaihtoehdot
2. **Vahvista työkalujen rekisteröinti** - Käytä MCP Inspector -työkalua testaukseen
3. **Tarkista käyttöoikeudet** - Joillakin työkaluilla on tiedosto- tai verkkoyhteyden vaatimukset

### Ympäristömuuttujia ei välitetä

- Joissain isännissä ympäristömuuttujat puhdistetaan
- Käytä `env` konfiguraatiokenttää eksplisiittisesti
- Vältä arkaluonteisen tiedon säilyttämistä konfiguraatiotiedostoissa (käytä salaisuuksien hallintaa)

---

## Turvallisuuden parhaat käytännöt

1. **Älä koskaan tallenna API-avaimia konfiguraatiotiedostoihin**
2. **Käytä ympäristömuuttujia arkaluontoisille tiedoille**
3. **Rajoita palvelimen oikeudet vain tarpeelliseen**
4. **Tarkista palvelinratkaisut ennen pääsyn myöntämistä järjestelmääsi**
5. **Käytä hyväksymislistoja tiedosto- ja verkkoyhteyksien käyttöön**

---

## Mitä seuraavaksi

- [3.13 - Vianmääritys MCP Inspectorilla](../13-mcp-inspector/README.md)
- [3.1 - Luo ensimmäinen MCP-palvelimesi](../01-first-server/README.md)
- [Moduuli 5 - Edistyneet aiheet](../../05-AdvancedTopics/README.md)

---

## Lisäresurssit

- [Claude Desktop MCP -dokumentaatio](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP -laajennus](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP-spesifikaatio - Kuljetustavat](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Virallinen MCP-palvelinrekisteri](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->