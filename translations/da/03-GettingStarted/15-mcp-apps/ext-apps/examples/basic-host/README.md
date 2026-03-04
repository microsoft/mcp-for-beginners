# Example: Basic Host

En referenceimplementering, der viser, hvordan man bygger en MCP-hostapplikation, der forbinder til MCP-servere og renderer værktøjsbrugerflader i en sikker sandbox.

Denne basic host kan også bruges til at teste MCP Apps under lokal udvikling.

## Key Files

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI-host med værktøjsvalg, parameterinput og iframe-håndtering
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Ydre iframe-proxy med sikkerhedsvalidering og tovejskommunikation
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Kerne-logik: serverforbindelse, værktøjskald og AppBridge-opsætning

## Getting Started

```bash
npm install
npm run start
# Åbn http://localhost:8080
```

Som standard vil hostapplikationen forsøge at forbinde til en MCP-server på `http://localhost:3001/mcp`. Du kan konfigurere denne adfærd ved at sætte miljøvariablen `SERVERS` med et JSON-array af server-URLs:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

Dette eksempel bruger et dobbelt-iframe-sandbox-mønster for sikker UI-isolation:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Hvorfor to iframes?**

- Den ydre iframe kører på et separat oprindelsessted (port 8081), hvilket forhindrer direkte adgang til hosten
- Den indre iframe modtager HTML via `srcdoc` og er begrænset af sandbox-attributter
- Beskeder flyder gennem den ydre iframe, som validerer og videresender dem tovejs

Denne arkitektur sikrer, at selv hvis værktøjets UI-kode er ondsindet, kan den ikke få adgang til hostapplikationens DOM, cookies eller JavaScript-kontekst.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->