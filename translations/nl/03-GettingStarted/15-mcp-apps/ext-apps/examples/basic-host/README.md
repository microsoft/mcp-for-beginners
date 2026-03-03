# Voorbeeld: Basis Host

Een referentie-implementatie die laat zien hoe je een MCP host-applicatie bouwt die verbinding maakt met MCP-servers en tool-UI's rendert in een beveiligde sandbox.

Deze basis host kan ook worden gebruikt om MCP Apps te testen tijdens lokale ontwikkeling.

## Belangrijke Bestanden

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host met toolselectie, parameterinvoer en iframebeheer
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Buitenste iframe-proxy met beveiligingsvalidatie en bidirectionele berichtdoorvoer
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Kernlogica: serververbinding, tool-aanroepen en AppBridge-instelling

## Aan de Slag

```bash
npm install
npm run start
# Open http://localhost:8080
```

Standaard probeert de host-applicatie verbinding te maken met een MCP-server op `http://localhost:3001/mcp`. Je kunt dit gedrag configureren door de omgevingsvariabele `SERVERS` in te stellen met een JSON-array van server-URL's:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architectuur

Dit voorbeeld gebruikt een double-iframe sandbox-patroon voor veilige UI-isolatie:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Waarom twee iframes?**

- Het buitenste iframe draait op een apart domein (poort 8081), waardoor directe toegang tot de host wordt voorkomen
- Het binnenste iframe ontvangt HTML via `srcdoc` en wordt beperkt door sandbox-attributen
- Berichten verlopen via het buitenste iframe dat ze valideert en bidirectioneel doorgeeft

Deze architectuur zorgt ervoor dat zelfs als tool-UI-code kwaadaardig is, deze geen toegang kan krijgen tot de DOM, cookies of JavaScript-context van de host-applicatie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Ondanks onze inspanningen voor nauwkeurigheid, dient rekening gehouden te worden met het feit dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal wordt beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->