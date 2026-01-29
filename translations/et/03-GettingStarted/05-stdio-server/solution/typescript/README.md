# MCP stdio Server - TypeScript Lahendus

> **⚠️ Tähtis**: See lahendus on uuendatud kasutama **stdio transporti**, nagu on soovitatud MCP spetsifikatsioonis 2025-06-18. Algne SSE transport on aegunud.

## Ülevaade

See TypeScripti lahendus näitab, kuidas luua MCP serverit, kasutades praegust stdio transporti. Stdio transport on lihtsam, turvalisem ja pakub paremat jõudlust kui aegunud SSE lähenemine.

## Eeltingimused

- Node.js 18+ või uuem
- npm või yarn paketihaldur

## Seadistamise juhised

### Samm 1: Paigalda sõltuvused

```bash
npm install
```

### Samm 2: Ehita projekt

```bash
npm run build
```

## Serveri käivitamine

Stdio server töötab erinevalt vanast SSE serverist. Veebiserveri käivitamise asemel suhtleb see stdin/stdout kaudu:

```bash
npm start
```

**Tähtis**: Server näib justkui "hangunud" - see on normaalne! See ootab JSON-RPC sõnumeid stdin kaudu.

## Serveri testimine

### Meetod 1: MCP Inspectori kasutamine (soovitatav)

```bash
npm run inspector
```

See teeb järgmist:
1. Käivitab teie serveri alamprotsessina
2. Avab veebiliidese testimiseks
3. Võimaldab teil kõiki serveri tööriistu interaktiivselt testida

### Meetod 2: Testimine otse käsurealt

Võite testida ka Inspectori otse käivitamisega:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Saadaval olevad tööriistad

Server pakub järgmisi tööriistu:

- **add(a, b)**: Liidab kaks arvu
- **multiply(a, b)**: Korrutab kaks arvu  
- **get_greeting(name)**: Loob isikupärastatud tervituse
- **get_server_info()**: Annab teavet serveri kohta

### Testimine Claude Desktopiga

Selle serveri kasutamiseks Claude Desktopiga lisage see konfiguratsioon oma faili `claude_desktop_config.json`:

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

## Projekti struktuur

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Peamised erinevused SSE-st

**stdio transport (Praegune):**
- ✅ Lihtsam seadistamine - HTTP serverit pole vaja
- ✅ Parem turvalisus - HTTP lõpp-punkte pole
- ✅ Suhtlus põhineb alamprotsessidel
- ✅ JSON-RPC stdin/stdout kaudu
- ✅ Parem jõudlus

**SSE transport (Aegunud):**
- ❌ Vajas Express serveri seadistamist
- ❌ Nõudis keerulist marsruutimist ja sessioonihaldust
- ❌ Rohkem sõltuvusi (Express, HTTP haldus)
- ❌ Lisaturvalisuse kaalutlused
- ❌ Nüüd aegunud MCP 2025-06-18 järgi

## Arendamise näpunäited

- Kasutage logimiseks `console.error()` (mitte kunagi `console.log()`, kuna see kirjutab stdout-i)
- Enne testimist ehitage projekt käsuga `npm run build`
- Testige Inspectoriga visuaalseks silumiseks
- Veenduge, et kõik JSON sõnumid oleksid õigesti vormindatud
- Server käsitleb automaatselt sujuvat sulgemist SIGINT/SIGTERM korral

See lahendus järgib praegust MCP spetsifikatsiooni ja demonstreerib parimaid tavasid stdio transpordi rakendamiseks TypeScripti abil.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.