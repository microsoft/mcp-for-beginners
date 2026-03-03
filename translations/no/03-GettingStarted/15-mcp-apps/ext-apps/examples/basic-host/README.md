# Eksempel: Grunnleggende Host

En referanseimplementering som viser hvordan man bygger en MCP-hostapplikasjon som kobler til MCP-servere og gjengir verktøygrensesnitt i et sikkert sandkassemiljø.

Denne grunnleggende hosten kan også brukes til å teste MCP-apper under lokal utvikling.

## Nøkkelfiler

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI-host med verktøyvalg, parameterinndata og iframe-håndtering
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Ytre iframe-proxy med sikkerhetsvalidering og toveis meldingsoverføring
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Kjernelogikk: servertilkobling, verktøysamtaler og AppBridge-oppsett

## Komme i gang

```bash
npm install
npm run start
# Åpne http://localhost:8080
```

Som standard vil hostapplikasjonen forsøke å koble til en MCP-server på `http://localhost:3001/mcp`. Du kan konfigurere denne oppførselen ved å sette miljøvariabelen `SERVERS` med et JSON-array av server-URLer:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arkitektur

Dette eksemplet bruker et to-iframe-sandkasse-mønster for sikker UI-isolasjon:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Hvorfor to iframes?**

- Den ytre iframe kjører på et eget opprinnelsessted (port 8081) og forhindrer direkte tilgang til hosten
- Den indre iframe mottar HTML via `srcdoc` og er begrenset av sandbox-attributter
- Meldinger flyter gjennom den ytre iframe som validerer og videresender dem i to retninger

Denne arkitekturen sikrer at selv om verktøyets UI-kode er ondsinnet, kan den ikke få tilgang til hostapplikasjonens DOM, informasjonskapsler eller JavaScript-kontekst.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->