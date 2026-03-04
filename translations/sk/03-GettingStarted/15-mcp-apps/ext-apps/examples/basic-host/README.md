# Príklad: Základný hostiteľ

Referenčná implementácia ukazujúca, ako vytvoriť MCP hostiteľskú aplikáciu, ktorá sa pripája k MCP serverom a zobrazuje používateľské rozhrania nástrojov v bezpečnom sandboxe.

Tento základný hostiteľ možno tiež použiť na testovanie MCP aplikácií počas lokálneho vývoja.

## Kľúčové súbory

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI hostiteľ s výberom nástroja, zadávaním parametrov a správou iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Vonkajší iframe proxy s bezpečnostnou validáciou a obojsmerným prenášaním správ
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Hlavná logika: pripojenie k serveru, volanie nástroja a nastavenie AppBridge

## Začíname

```bash
npm install
npm run start
# Otvorte http://localhost:8080
```

Predvolene sa hostiteľská aplikácia pokúsi pripojiť k MCP serveru na adrese `http://localhost:3001/mcp`. Toto správanie môžete nakonfigurovať nastavením premenej prostredia `SERVERS` s JSON poľom URL serverov:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architektúra

Tento príklad používa vzor dvojitého iframe sandboxu pre bezpečnú izoláciu používateľského rozhrania:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Prečo dva iframy?**

- Vonkajší iframe beží na samostatnom pôvode (port 8081), čím zabraňuje priamemu prístupu k hostiteľovi
- Vnútorný iframe prijíma HTML cez `srcdoc` a je obmedzený atribútmi sandboxu
- Správy prechádzajú cez vonkajší iframe, ktorý ich overuje a zároveň ich obojsmerne prenáša

Táto architektúra zabezpečuje, že aj keď je kód používateľského rozhrania nástroja škodlivý, nemôže pristupovať k DOM hostiteľskej aplikácie, cookies ani JavaScriptovému kontextu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->