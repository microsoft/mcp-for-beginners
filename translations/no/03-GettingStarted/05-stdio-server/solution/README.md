# MCP stdio Server-løsninger

> **⚠️ Viktig**: Disse løsningene har blitt oppdatert til å bruke **stdio transport** som anbefalt i MCP-spesifikasjonen 2025-06-18. Den opprinnelige SSE (Server-Sent Events) transporten er avviklet.

Her er komplette løsninger for å bygge MCP-servere ved bruk av stdio transport i hver runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Komplett stdio serverimplementasjon
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio server med asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio server med avhengighetsinjeksjon

Hver løsning demonstrerer:
- Oppsett av stdio transport
- Definering av serververktøy
- Riktig håndtering av JSON-RPC-meldinger
- Integrasjon med MCP-klienter som Claude

Alle løsninger følger den gjeldende MCP-spesifikasjonen og bruker den anbefalte stdio transporten for optimal ytelse og sikkerhet.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.