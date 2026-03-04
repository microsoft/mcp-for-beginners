# Exempel: Grundläggande värd

En referensimplementation som visar hur man bygger en MCP-värdsapplikation som ansluter till MCP-servrar och renderar verktygsgränssnitt i en säker sandbox.

Denna grundläggande värd kan också användas för att testa MCP-appar under lokal utveckling.

## Viktiga filer

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI-värd med verktygsval, parameterinmatning och iframe-hantering
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Yttre iframe-proxy med säkerhetsvalidering och tvåvägs meddelandeförmedling
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Kärnlogik: serveranslutning, verktygsanrop och AppBridge-uppsättning

## Kom igång

```bash
npm install
npm run start
# Öppna http://localhost:8080
```

Som standard försöker värdsapplikationen ansluta till en MCP-server på `http://localhost:3001/mcp`. Du kan konfigurera detta genom att sätta miljövariabeln `SERVERS` med en JSON-array av server-URL:er:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arkitektur

Detta exempel använder ett mönster med dubbel iframe-sandbox för säker UI-isolering:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Varför två iframes?**

- Den yttre iframen körs på ett separat ursprung (port 8081) vilket förhindrar direkt åtkomst till värden
- Den inre iframen tar emot HTML via `srcdoc` och begränsas av sandbox-attribut
- Meddelanden flödar genom den yttre iframen som validerar och förmedlar dem i två riktningar

Denna arkitektur säkerställer att även om verktygets UI-kod är skadlig kan den inte komma åt värdsapplikationens DOM, cookies eller JavaScript-kontext.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Trots att vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->