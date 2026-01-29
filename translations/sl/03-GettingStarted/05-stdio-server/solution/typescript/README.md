# MCP stdio strežnik - TypeScript rešitev

> **⚠️ Pomembno**: Ta rešitev je bila posodobljena za uporabo **stdio transporta**, kot je priporočeno v MCP specifikaciji 2025-06-18. Prvotni SSE transport je bil ukinjen.

## Pregled

Ta TypeScript rešitev prikazuje, kako zgraditi MCP strežnik z uporabo trenutnega stdio transporta. Stdio transport je enostavnejši, varnejši in zagotavlja boljšo zmogljivost kot ukinjeni pristop SSE.

## Predpogoji

- Node.js 18+ ali novejši
- Upravitelj paketov npm ali yarn

## Navodila za nastavitev

### Korak 1: Namestite odvisnosti

```bash
npm install
```

### Korak 2: Zgradite projekt

```bash
npm run build
```

## Zagon strežnika

Stdio strežnik deluje drugače kot stari SSE strežnik. Namesto zagona spletnega strežnika komunicira prek stdin/stdout:

```bash
npm start
```

**Pomembno**: Strežnik se bo zdel, kot da "visi" - to je normalno! Čaka na JSON-RPC sporočila iz stdin.

## Testiranje strežnika

### Metoda 1: Uporaba MCP Inspectorja (Priporočeno)

```bash
npm run inspector
```

To bo:
1. Zagnalo vaš strežnik kot podproces
2. Odprlo spletni vmesnik za testiranje
3. Omogočilo interaktivno testiranje vseh orodij strežnika

### Metoda 2: Neposredno testiranje prek ukazne vrstice

Lahko testirate tudi z neposrednim zagonom Inspectorja:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Razpoložljiva orodja

Strežnik ponuja naslednja orodja:

- **add(a, b)**: Sešteje dve števili
- **multiply(a, b)**: Pomnoži dve števili  
- **get_greeting(name)**: Ustvari personaliziran pozdrav
- **get_server_info()**: Pridobi informacije o strežniku

### Testiranje z Claude Desktop

Za uporabo tega strežnika z Claude Desktop dodajte to konfiguracijo v vaš `claude_desktop_config.json`:

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

## Struktura projekta

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Ključne razlike od SSE

**stdio transport (trenutni):**
- ✅ Enostavnejša nastavitev - ni potreben HTTP strežnik
- ✅ Boljša varnost - ni HTTP končnih točk
- ✅ Komunikacija na osnovi podprocesov
- ✅ JSON-RPC prek stdin/stdout
- ✅ Boljša zmogljivost

**SSE transport (ukinjen):**
- ❌ Zahteval nastavitev Express strežnika
- ❌ Potreboval kompleksno usmerjanje in upravljanje sej
- ❌ Več odvisnosti (Express, HTTP obdelava)
- ❌ Dodatni varnostni premisleki
- ❌ Zdaj ukinjen v MCP 2025-06-18

## Nasveti za razvoj

- Uporabite `console.error()` za beleženje (nikoli `console.log()`, saj piše v stdout)
- Pred testiranjem zgradite z `npm run build`
- Testirajte z Inspectorjem za vizualno odpravljanje napak
- Prepričajte se, da so vsa JSON sporočila pravilno oblikovana
- Strežnik samodejno obravnava pravilno zaustavitev ob SIGINT/SIGTERM

Ta rešitev sledi trenutni MCP specifikaciji in prikazuje najboljše prakse za implementacijo stdio transporta z uporabo TypeScripta.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.