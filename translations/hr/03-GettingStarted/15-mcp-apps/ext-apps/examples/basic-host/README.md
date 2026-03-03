# Primjer: Osnovni Host

Referentna implementacija koja pokazuje kako izgraditi MCP host aplikaciju koja se povezuje na MCP poslužitelje i prikazuje sučelja alata u sigurnom pješčaniku.

Ovaj osnovni host također se može koristiti za testiranje MCP aplikacija tijekom lokalnog razvoja.

## Ključne datoteke

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host s izborom alata, unosom parametara i upravljanjem iframeovima
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Vanjski iframe proxy sa sigurnosnom provjerom i dvosmjernim prosljeđivanjem poruka
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Osnovna logika: veza s poslužiteljem, pozivanje alata i postavljanje AppBridgea

## Početak rada

```bash
npm install
npm run start
# Otvorite http://localhost:8080
```

Prema zadanim postavkama, host aplikacija će pokušati uspostaviti vezu s MCP poslužiteljem na `http://localhost:3001/mcp`. Ovo ponašanje možete konfigurirati postavljanjem varijable okoline `SERVERS` s JSON nizom URL-ova poslužitelja:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arhitektura

Ovaj primjer koristi obrazac dvostrukog iframe pješčanika za sigurnu izolaciju sučelja:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Zašto dva iframea?**

- Vanjski iframe radi na zasebnoj domeni (port 8081) sprječavajući izravan pristup hostu
- Unutarnji iframe prima HTML preko `srcdoc` i ograničen je atributima pješčanika
- Poruke prolaze kroz vanjski iframe koji ih provjerava i dvosmjerno prosljeđuje

Ova arhitektura osigurava da čak i ako je kod sučelja alata zlonamjeran, ne može pristupiti DOM-u host aplikacije, kolačićima ili JavaScript kontekstu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:  
Ovaj je dokument preveden korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporuča se stručni prijevod od strane profesionalnog prevoditelja. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->