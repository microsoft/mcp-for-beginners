# MCP stdio Server - TypeScript sprendimas

> **⚠️ Svarbu**: Šis sprendimas buvo atnaujintas, kad naudotų **stdio transportą**, kaip rekomenduojama MCP specifikacijoje 2025-06-18. Originalus SSE transportas yra nebenaudojamas.

## Apžvalga

Šis TypeScript sprendimas parodo, kaip sukurti MCP serverį naudojant dabartinį stdio transportą. Stdio transportas yra paprastesnis, saugesnis ir užtikrina geresnį našumą nei nebenaudojamas SSE metodas.

## Reikalavimai

- Node.js 18+ arba naujesnė versija
- npm arba yarn paketų tvarkyklė

## Nustatymo instrukcijos

### 1 žingsnis: Įdiekite priklausomybes

```bash
npm install
```

### 2 žingsnis: Sukurkite projektą

```bash
npm run build
```

## Serverio paleidimas

Stdio serveris veikia kitaip nei senasis SSE serveris. Vietoj internetinio serverio paleidimo jis komunikuoja per stdin/stdout:

```bash
npm start
```

**Svarbu**: Serveris gali atrodyti, kad „užstrigo“ – tai normalu! Jis laukia JSON-RPC pranešimų iš stdin.

## Serverio testavimas

### 1 metodas: Naudojant MCP Inspector (Rekomenduojama)

```bash
npm run inspector
```

Tai atliks:
1. Paleis jūsų serverį kaip subprocesą
2. Atidarys internetinę sąsają testavimui
3. Leis interaktyviai testuoti visus serverio įrankius

### 2 metodas: Tiesioginis testavimas komandinėje eilutėje

Taip pat galite testuoti paleisdami Inspector tiesiogiai:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Galimi įrankiai

Serveris siūlo šiuos įrankius:

- **add(a, b)**: Sudėti du skaičius
- **multiply(a, b)**: Padauginti du skaičius  
- **get_greeting(name)**: Sukurti asmeninį pasveikinimą
- **get_server_info()**: Gauti informaciją apie serverį

### Testavimas su Claude Desktop

Norėdami naudoti šį serverį su Claude Desktop, pridėkite šią konfigūraciją į savo `claude_desktop_config.json`:

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

## Projekto struktūra

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Pagrindiniai skirtumai nuo SSE

**stdio transportas (Dabartinis):**
- ✅ Paprastesnis nustatymas – nereikia HTTP serverio
- ✅ Geresnis saugumas – nėra HTTP galinių taškų
- ✅ Komunikacija per subprocesus
- ✅ JSON-RPC per stdin/stdout
- ✅ Geresnis našumas

**SSE transportas (Nebenaudojamas):**
- ❌ Reikėjo Express serverio nustatymo
- ❌ Reikėjo sudėtingo maršrutų ir sesijų valdymo
- ❌ Daugiau priklausomybių (Express, HTTP tvarkymas)
- ❌ Papildomi saugumo aspektai
- ❌ Nebenaudojamas MCP 2025-06-18 specifikacijoje

## Patarimai kūrimui

- Naudokite `console.error()` žurnalavimui (niekada `console.log()`, nes jis rašo į stdout)
- Prieš testavimą sukurkite projektą naudodami `npm run build`
- Testuokite su Inspector vizualiam derinimui
- Įsitikinkite, kad visi JSON pranešimai yra tinkamai suformatuoti
- Serveris automatiškai tvarko sklandų uždarymą gavus SIGINT/SIGTERM signalus

Šis sprendimas atitinka dabartinę MCP specifikaciją ir demonstruoja geriausią praktiką stdio transporto įgyvendinimui naudojant TypeScript.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.