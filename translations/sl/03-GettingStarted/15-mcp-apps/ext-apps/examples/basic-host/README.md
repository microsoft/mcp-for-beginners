# Primer: Osnovni gostitelj

Referenčna implementacija, ki prikazuje, kako zgraditi gostiteljsko aplikacijo MCP, ki se poveže s strežniki MCP in upodobi orodja UI v varnem peskovniku.

Ta osnovni gostitelj se lahko uporablja tudi za testiranje MCP aplikacij med lokalnim razvojem.

## Ključne datoteke

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React gostitelj UI z izbiro orodij, vnosom parametrov in upravljanjem iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Zunanji iframe proxy z varnostno validacijo in dvosmernim posredovanjem sporočil
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Jedrna logika: povezava s strežnikom, klic orodij in nastavitev AppBridge

## Začetek

```bash
npm install
npm run start
# Odprite http://localhost:8080
```

Privzeto bo gostiteljska aplikacija poskušala vzpostaviti povezavo s strežnikom MCP na `http://localhost:3001/mcp`. To vedenje lahko konfigurirate z nastavitvijo okoljske spremenljivke `SERVERS` z JSON poljem URL-jev strežnikov:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arhitektura

Ta primer uporablja vzorec dvo-iframe peskovnika za varno izolacijo UI:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Zakaj dva iframe-a?**

- Zunanji iframe teče na ločenem izvoru (vrata 8081), kar preprečuje neposreden dostop do gostitelja
- Notranji iframe prejme HTML preko `srcdoc` in je omejen z atributi peskovnika
- Sporočila potujejo skozi zunanji iframe, ki jih validira in posreduje v obe smeri

Ta arhitektura zagotavlja, da tudi če je koda orodja UI zlonamerna, ne more dostopati do DOM gostiteljske aplikacije, piškotkov ali JavaScript konteksta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve umetne inteligence za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorno jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za kakršnekoli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->