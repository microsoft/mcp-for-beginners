# MCP stdio Server - TypeScript Rješenje

> **⚠️ Važno**: Ovo rješenje je ažurirano kako bi koristilo **stdio transport** prema preporuci MCP Specifikacije 2025-06-18. Izvorni SSE transport je ukinut.

## Pregled

Ovo TypeScript rješenje pokazuje kako izraditi MCP poslužitelj koristeći trenutni stdio transport. Stdio transport je jednostavniji, sigurniji i pruža bolje performanse u usporedbi s ukinutim SSE pristupom.

## Preduvjeti

- Node.js 18+ ili noviji
- npm ili yarn upravitelj paketa

## Upute za postavljanje

### Korak 1: Instalirajte ovisnosti

```bash
npm install
```

### Korak 2: Izgradite projekt

```bash
npm run build
```

## Pokretanje poslužitelja

Stdio poslužitelj radi drugačije od starog SSE poslužitelja. Umjesto pokretanja web poslužitelja, komunicira putem stdin/stdout:

```bash
npm start
```

**Važno**: Poslužitelj će izgledati kao da "visi" - to je normalno! Čeka JSON-RPC poruke putem stdin-a.

## Testiranje poslužitelja

### Metoda 1: Korištenje MCP Inspectora (Preporučeno)

```bash
npm run inspector
```

Ovo će:
1. Pokrenuti vaš poslužitelj kao podproces
2. Otvoriti web sučelje za testiranje
3. Omogućiti interaktivno testiranje svih alata poslužitelja

### Metoda 2: Testiranje putem naredbenog retka

Također možete testirati pokretanjem Inspectora izravno:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Dostupni alati

Poslužitelj pruža sljedeće alate:

- **add(a, b)**: Zbraja dva broja
- **multiply(a, b)**: Množi dva broja  
- **get_greeting(name)**: Generira personalizirani pozdrav
- **get_server_info()**: Dohvaća informacije o poslužitelju

### Testiranje s Claude Desktopom

Za korištenje ovog poslužitelja s Claude Desktopom, dodajte ovu konfiguraciju u vaš `claude_desktop_config.json`:

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

## Ključne razlike u odnosu na SSE

**stdio transport (Trenutni):**
- ✅ Jednostavnije postavljanje - nije potreban HTTP poslužitelj
- ✅ Bolja sigurnost - nema HTTP krajnjih točaka
- ✅ Komunikacija temeljena na podprocesima
- ✅ JSON-RPC putem stdin/stdout
- ✅ Bolje performanse

**SSE transport (Ukinut):**
- ❌ Zahtijevao postavljanje Express poslužitelja
- ❌ Potrebno složeno usmjeravanje i upravljanje sesijama
- ❌ Više ovisnosti (Express, HTTP obrada)
- ❌ Dodatni sigurnosni izazovi
- ❌ Sada ukinut u MCP 2025-06-18

## Savjeti za razvoj

- Koristite `console.error()` za zapisivanje logova (nikada `console.log()` jer piše u stdout)
- Izgradite projekt s `npm run build` prije testiranja
- Testirajte s Inspectorom za vizualno otklanjanje pogrešaka
- Osigurajte da su sve JSON poruke ispravno formatirane
- Poslužitelj automatski upravlja urednim gašenjem na SIGINT/SIGTERM

Ovo rješenje slijedi trenutnu MCP specifikaciju i demonstrira najbolje prakse za implementaciju stdio transporta koristeći TypeScript.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.