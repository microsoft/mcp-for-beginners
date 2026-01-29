# MCP stdio Server - TypeScript-ratkaisu

> **⚠️ Tärkeää**: Tämä ratkaisu on päivitetty käyttämään **stdio-kuljetusta**, kuten MCP-määrittelyssä 2025-06-18 suositellaan. Alkuperäinen SSE-kuljetus on poistettu käytöstä.

## Yleiskatsaus

Tämä TypeScript-ratkaisu näyttää, kuinka rakentaa MCP-palvelin käyttäen nykyistä stdio-kuljetusta. Stdio-kuljetus on yksinkertaisempi, turvallisempi ja tarjoaa paremman suorituskyvyn kuin vanhentunut SSE-lähestymistapa.

## Esivaatimukset

- Node.js 18+ tai uudempi
- npm- tai yarn-pakettienhallinta

## Asennusohjeet

### Vaihe 1: Asenna riippuvuudet

```bash
npm install
```

### Vaihe 2: Rakenna projekti

```bash
npm run build
```

## Palvelimen käynnistäminen

Stdio-palvelin toimii eri tavalla kuin vanha SSE-palvelin. Sen sijaan, että se käynnistäisi verkkopalvelimen, se kommunikoi stdin/stdoutin kautta:

```bash
npm start
```

**Tärkeää**: Palvelin näyttää jäätyvän - tämä on normaalia! Se odottaa JSON-RPC-viestejä stdinistä.

## Palvelimen testaaminen

### Menetelmä 1: MCP Inspectorin käyttö (suositeltu)

```bash
npm run inspector
```

Tämä tekee seuraavaa:
1. Käynnistää palvelimesi aliprosessina
2. Avaa verkkokäyttöliittymän testausta varten
3. Mahdollistaa kaikkien palvelintyökalujen interaktiivisen testauksen

### Menetelmä 2: Suora komentorivitestaus

Voit myös testata käynnistämällä Inspectorin suoraan:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Käytettävissä olevat työkalut

Palvelin tarjoaa seuraavat työkalut:

- **add(a, b)**: Laskee kahden luvun summan
- **multiply(a, b)**: Kertoo kaksi lukua keskenään  
- **get_greeting(name)**: Luo henkilökohtaisen tervehdyksen
- **get_server_info()**: Antaa tietoja palvelimesta

### Testaus Claude Desktopilla

Käyttääksesi tätä palvelinta Claude Desktopin kanssa, lisää tämä konfiguraatio tiedostoon `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Projektin rakenne

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Keskeiset erot SSE:stä

**stdio-kuljetus (Nykyinen):**
- ✅ Yksinkertaisempi asennus - ei tarvetta HTTP-palvelimelle
- ✅ Parempi turvallisuus - ei HTTP-päätepisteitä
- ✅ Kommunikointi aliprosessien kautta
- ✅ JSON-RPC stdin/stdoutin kautta
- ✅ Parempi suorituskyky

**SSE-kuljetus (Poistettu käytöstä):**
- ❌ Vaati Express-palvelimen asennuksen
- ❌ Tarvitsi monimutkaista reititystä ja istunnonhallintaa
- ❌ Enemmän riippuvuuksia (Express, HTTP-käsittely)
- ❌ Lisäturvallisuushuomioita
- ❌ Poistettu käytöstä MCP:ssä 2025-06-18

## Kehitysvinkit

- Käytä `console.error()` lokitukseen (älä koskaan `console.log()`, koska se kirjoittaa stdoutiin)
- Rakenna komennolla `npm run build` ennen testausta
- Testaa Inspectorilla visuaalista virheenkorjausta varten
- Varmista, että kaikki JSON-viestit on muotoiltu oikein
- Palvelin käsittelee automaattisesti siistin sammutuksen SIGINT/SIGTERM-signaaleilla

Tämä ratkaisu noudattaa nykyistä MCP-määrittelyä ja esittelee parhaat käytännöt stdio-kuljetuksen toteuttamiseen TypeScriptillä.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.