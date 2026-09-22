# Virheenkorjaus MCP Inspectorilla

> [!NOTE]
> Komennot, jotka käyttävät `--sse` ja URL-osoitteet, jotka päättyvät `/sse`, testaavat perinteistä HTTP+SSE
> -siirtoa. Uudelle MCP `2026-07-28` -palvelimelle käytä Inspectorin versiota, joka
> tukee suoritettavaa HTTP:ta ja valitse se siirtotapa sen sijaan.

**MCP Inspector** on olennainen virheenkorjaustyökalu, joka antaa sinun testata ja korjata MCP-palvelimiasi vuorovaikutteisesti ilman täyttä tekoälysovellusta. Ajattele sitä kuin "Postman MCP:lle" - se tarjoaa visuaalisen käyttöliittymän pyyntöjen lähettämiseen, vastausten katseluun ja palvelimesi käyttäytymisen ymmärtämiseen.

## Miksi käyttää MCP Inspectoria?

MCP-palvelimia rakentaessasi kohtaat usein seuraavat haasteet:

- **"Onko palvelimeni edes käynnissä?"** - Inspector näyttää yhteyden tilan
- **"Ovatko työkaluni rekisteröity oikein?"** - Inspector listaa kaikki saatavilla olevat työkalut
- **"Millainen vastausmuoto on?"** - Inspector näyttää täydet JSON-vastaukset
- **"Miksi tämä työkalu ei toimi?"** - Inspector näyttää yksityiskohtaiset virheilmoitukset

## Esivaatimukset

- Node.js 18+ asennettuna
- npm (sisältyy Node.js:ään)
- MCP-palvelin testattavaksi (katso [Module 3.1 - Ensimmäinen palvelin](../01-first-server/README.md))

## Asennus

### Vaihtoehto 1: Aja npx:llä (suositeltu nopeaan testaukseen)

```bash
npx @modelcontextprotocol/inspector
```

### Vaihtoehto 2: Asenna globaalisti

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Vaihtoehto 3: Lisää projektiisi

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Lisää `package.json`-tiedostoon:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Yhteyden muodostaminen palvelimeesi

### stdio-palvelimet (paikallinen prosessi)

Palvelimille, jotka kommunikoivat standard input/output -kanavien kautta:

```bash
# Python-palvelin
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js-palvelin
npx @modelcontextprotocol/inspector node ./build/index.js

# Ympäristömuuttujien kanssa
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP-palvelimet (verkko)

Palvelimille, jotka toimivat HTTP-palveluina:

1. Käynnistä ensin palvelimesi:
   ```bash
   python server.py  # Palvelin käynnissä osoitteessa http://localhost:8080
   ```

2. Käynnistä Inspector ja muodosta yhteys:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspectorin käyttöliittymän yleiskatsaus

Kun Inspector käynnistyy, näet web-käyttöliittymän (tyypillisesti osoitteessa `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Työkalujen testaaminen

### Saatavilla olevien työkalujen listaaminen

1. Klikkaa **Tools**-välilehteä
2. Inspector kutsuu automaattisesti `tools/list`
3. Näet kaikki rekisteröidyt työkalut:
   - Työkalun nimi
   - Kuvaus
   - Syötteen skeema (parametrit)

### Työkalun kutsuminen

1. Valitse työkalu listasta
2. Täytä lomakkeeseen vaaditut parametrit
3. Klikkaa **Run Tool**
4. Katso vastaus tulosruudussa

**Esimerkki: laskutyökalun testaus**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Työkalun virheiden vianmääritys

Kun työkalu epäonnistuu, Inspector näyttää:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Yleisiä virhekoodistoja:
| Koodi | Merkitys |
|------|----------|
| -32700 | Jäsentämisvirhe (virheellinen JSON) |
| -32600 | Virheellinen pyyntö |
| -32601 | Metodia ei löydy |
| -32602 | Virheelliset parametrit |
| -32603 | Sisäinen virhe |

---

## Resurssien testaaminen

### Resurssien listaaminen

1. Klikkaa **Resources**-välilehteä
2. Inspector kutsuu `resources/list`
3. Näet:
   - Resurssien URI:t
   - Nimet ja kuvaukset
   - MIME-tyypit

### Resurssin lukeminen

1. Valitse resurssi
2. Klikkaa **Read Resource**
3. Katso palautettu sisältö

**Esimerkkivastaus:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Kehoteiden testaaminen

### Kehoteiden listaaminen

1. Klikkaa **Prompts**-välilehteä
2. Inspector kutsuu `prompts/list`
3. Näytä saatavilla olevat kehotepohjat

### Kehotteen hakeminen

1. Valitse kehotepohja
2. Täytä vaadittavat argumentit
3. Klikkaa **Get Prompt**
4. Näytä tuotetut kehotteet

---

## Viestilokin analysointi

Viestiloki näyttää kaikki MCP-protokollaviestit. Alla oleva keskustelu on peräisin
perinteiseltä `2025-11-25` -palvelimelta, ja sisältää poistetun `initialize`-kättelyn. 
`2026-07-28` -palvelin käyttää itsenäistä pyyntömeta-dataa ja kutsua `server/discover`
sen sijaan.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Mitä tarkastella

- **Pyyntö/vastaus-parit**: Jokaisella `→`-merkillä pitäisi olla vastaava `←`
- **Virheilmoitukset**: Tarkista vastausten `"error"`-osat
- **Ajastus**: Suuret aukot voivat viitata suorituskykyongelmiin
- **Protokollan versio**: Varmista, että palvelin ja asiakas ovat samassa versiossa

---

## VS Code -integraatio

Voit käyttää Inspectoria suoraan VS Codesta:

### Käyttäen launch.json-tiedostoa

Lisää `.vscode/launch.json`-tiedostoon:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Käyttäen tehtäviä (Tasks)

Lisää `.vscode/tasks.json`-tiedostoon:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Yleisiä virheenkorjaustilanteita

### Tilanne 1: Palvelin ei yhdistä

**Oireet:** Inspector näyttää "Disconnected" tai jumittuu "Connecting..."-tilaan

**Tarkistuslista:**
1. ✅ Onko palvelimen komento oikein?
2. ✅ Onko kaikki riippuvuudet asennettu?
3. ✅ Onko palvelimen polku absoluuttinen tai suhteessa nykyiseen hakemistoon?
4. ✅ Onko tarvittavat ympäristömuuttujat asetettu?

**Virheen selvitys:**
```bash
# Testaa palvelin manuaalisesti ensin
python -c "import your_server_module; print('OK')"

# Tarkista tuontivirheet
python -m your_server_module 2>&1 | head -20

# Varmista, että MCP SDK on asennettu
pip show mcp
```

### Tilanne 2: Työkalut eivät näy

**Oireet:** Tools-välilehti näyttää tyhjän listan

**Mahdolliset syyt:**
1. Työkaluja ei rekisteröity palvelimen käynnistyessä
2. Palvelin kaatui käynnistyksen jälkeen
3. `tools/list`-käsittelijä palauttaa tyhjän taulukon

**Virheen selvitys:**
1. Tarkista viestiloki `tools/list`-vastauksesta
2. Lisää lokitus työkalujen rekisteröintikoodiin
3. Varmista, että `@mcp.tool()`-koristeet ovat paikallaan (Python)

### Tilanne 3: Työkalu palauttaa virheen

**Oireet:** Työkalun kutsu palauttaa virhevastauksen

**Virheen selvitystapa:**
1. Lue virheilmoitus huolellisesti
2. Tarkista, että parametrityypit vastaavat skeemaa
3. Lisää try/catch-yksityiskohdilla virheilmoituksista
4. Tarkista palvelimen lokit jäljityksiä varten

**Parannettu virheenkäsittelyn esimerkki:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Työkalun logiikka tässä
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Tilanne 4: Resurssin sisältö tyhjä

**Oireet:** Resurssi palautuu, mutta sisältö on tyhjä tai null

**Tarkistuslista:**
1. ✅ Tiedostopolku tai URI on oikea
2. ✅ Palvelimella on lupa lukea resurssi
3. ✅ Resurssin sisältö palautuu oikein

---

## Kehittyneet Inspector-ominaisuudet

### Mukautetut otsikot (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Yksityiskohtainen lokitus

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Istuntojen tallentaminen

Inspector voi viedä viestilokit myöhempää analyysia varten:
1. Klikkaa **Export Log** viestipaneelissa
2. Tallenna JSON-tiedosto
3. Jaa tiimin jäsenten kanssa virheenkorjausta varten

---

## Parhaat käytännöt

1. **Testaa ajoissa ja usein** - Käytä Inspectoria kehityksen aikana, ei vain virhetilanteissa
2. **Aloita yksinkertaisesti** - Testaa yhteydet ennen monimutkaisia työkalukutsuja
3. **Tarkista skeema** - Monet virheet johtuvat parametrityyppien ristiriidoista
4. **Lue virheilmoitukset** - MCP-virheet ovat yleensä kuvaavia
5. **Pidä Inspector auki** - Se auttaa havaitsemaan ongelmat kehityksen aikana

---

## Seuraavat askeleet

Olet suorittanut Moduulin 3: Aloittelijan opas! Jatka oppimista:

- [Moduuli 4: Käytännön toteutus](../../04-PracticalImplementation/README.md)

---

## Lisäresurssit

- [MCP Inspector GitHub -varasto](https://github.com/modelcontextprotocol/inspector)
- [MCP Spesifikaatio - Protokollaviestit](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Spesifikaatio](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->