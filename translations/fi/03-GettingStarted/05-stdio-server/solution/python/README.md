# MCP stdio-palvelin - Python-ratkaisu

> **⚠️ Tärkeää**: Tämä ratkaisu on päivitetty käyttämään **stdio-kuljetusta**, kuten MCP-määrittelyssä 2025-06-18 suositellaan. Alkuperäinen SSE-kuljetus on poistettu käytöstä.

## Yleiskatsaus

Tämä Python-ratkaisu näyttää, kuinka rakentaa MCP-palvelin käyttäen nykyistä stdio-kuljetusta. Stdio-kuljetus on yksinkertaisempi, turvallisempi ja tarjoaa paremman suorituskyvyn kuin vanhentunut SSE-lähestymistapa.

## Esivaatimukset

- Python 3.8 tai uudempi
- Suositellaan asentamaan `uv` pakettien hallintaan, katso [ohjeet](https://docs.astral.sh/uv/#highlights)

## Asennusohjeet

### Vaihe 1: Luo virtuaaliympäristö

```bash
python -m venv venv
```

### Vaihe 2: Aktivoi virtuaaliympäristö

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Vaihe 3: Asenna riippuvuudet

```bash
pip install mcp
```

## Palvelimen käynnistäminen

Stdio-palvelin toimii eri tavalla kuin vanha SSE-palvelin. Sen sijaan, että se käynnistäisi verkkopalvelimen, se kommunikoi stdin/stdoutin kautta:

```bash
python server.py
```

**Tärkeää**: Palvelin näyttää jäätyvän - tämä on normaalia! Se odottaa JSON-RPC-viestejä stdinistä.

## Palvelimen testaaminen

### Menetelmä 1: MCP Inspectorin käyttö (suositeltu)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Tämä:
1. Käynnistää palvelimen aliprosessina
2. Avaa verkkokäyttöliittymän testausta varten
3. Mahdollistaa kaikkien palvelintyökalujen interaktiivisen testauksen

### Menetelmä 2: Suora JSON-RPC-testaus

Voit myös testata lähettämällä JSON-RPC-viestejä suoraan:

1. Käynnistä palvelin: `python server.py`
2. Lähetä JSON-RPC-viesti (esimerkki):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Palvelin vastaa käytettävissä olevilla työkaluilla

### Käytettävissä olevat työkalut

Palvelin tarjoaa seuraavat työkalut:

- **add(a, b)**: Laskee kahden luvun summan
- **multiply(a, b)**: Laskee kahden luvun tulon  
- **get_greeting(name)**: Luo henkilökohtaisen tervehdyksen
- **get_server_info()**: Antaa tietoja palvelimesta

### Testaus Claude Desktopilla

Jos haluat käyttää tätä palvelinta Claude Desktopin kanssa, lisää tämä konfiguraatio tiedostoon `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Keskeiset erot SSE:stä

**Stdio-kuljetus (Nykyinen):**
- ✅ Yksinkertaisempi asennus - ei tarvetta verkkopalvelimelle
- ✅ Parempi turvallisuus - ei HTTP-päätepisteitä
- ✅ Kommunikointi aliprosessien kautta
- ✅ JSON-RPC stdin/stdoutin kautta
- ✅ Parempi suorituskyky

**SSE-kuljetus (Poistettu käytöstä):**
- ❌ Vaati HTTP-palvelimen asennuksen
- ❌ Tarvitsi verkkokehyksen (Starlette/FastAPI)
- ❌ Monimutkaisempi reititys ja istunnonhallinta
- ❌ Lisäturvallisuushuomiot
- ❌ Poistettu käytöstä MCP:ssä 2025-06-18

## Vianetsintävinkit

- Käytä `stderr`-virtaa lokitukseen (älä koskaan `stdoutia`)
- Testaa Inspectorilla visuaalista vianetsintää varten
- Varmista, että kaikki JSON-viestit ovat rivinvaihdolla erotettuja
- Tarkista, että palvelin käynnistyy ilman virheitä

Tämä ratkaisu noudattaa nykyistä MCP-määrittelyä ja esittelee parhaat käytännöt stdio-kuljetuksen toteutukseen.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.