# Näide: Põhiline Host

Võrdlusrakendus, mis näitab, kuidas ehitada MCP hostrakendus, mis ühendub MCP serveritega ja kuvab turvalises liivakastis tööriistade kasutajaliideseid.

Seda põhilist hosti saab kasutada ka MCP rakenduste testimiseks kohalikus arenduses.

## Peamised Failid

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host tööriista valiku, parameetrite sisendi ja iframe haldusega
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Välimine iframe proxy turvalisuse valideerimise ja kahepoolselt sõnumite edastamisega
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Tuumikloogika: serveri ühendus, tööriista kutsumine ja AppBridge seadistus

## Alustamine

```bash
npm install
npm run start
# Ava http://localhost:8080
```

Vaikimisi proovib host-rakendus ühendada MCP serveriga aadressil `http://localhost:3001/mcp`. Seda käitumist saab seadistada, määrates keskkonnamuutujas `SERVERS` JSON-massiivi serveri URLidega:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arhitektuur

See näide kasutab turvaliseks kasutajaliidese isoleerimiseks topeltiframe liivakasti mustrit:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Miks kaks iframe'i?**

- Välimine iframe töötab eraldi päritoluga (port 8081), takistades otsest juurdepääsu hostile
- Siseiframe saab HTML-i `srcdoc` kaudu ja on piiratud liivakasti atribuudi poolt
- Sõnumid voolavad läbi välise iframe'i, mis valideerib ja edastab need kahepoolselt

See arhitektuur tagab, et ka siis, kui tööriista UI kood on pahatahtlik, ei pääse see ligi host-rakenduse DOM-ile, küpsistele ega JavaScripti kontekstile.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, on oluline arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->