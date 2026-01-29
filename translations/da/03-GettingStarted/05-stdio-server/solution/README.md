# MCP stdio Server-løsninger

> **⚠️ Vigtigt**: Disse løsninger er blevet opdateret til at bruge **stdio-transport**, som anbefalet i MCP-specifikationen 2025-06-18. Den oprindelige SSE (Server-Sent Events)-transport er blevet udfaset.

Her er de komplette løsninger til at bygge MCP-servere ved hjælp af stdio-transport i hver runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Komplet stdio-serverimplementering
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio-server med asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio-server med dependency injection

Hver løsning demonstrerer:
- Opsætning af stdio-transport
- Definition af serverværktøjer
- Korrekt håndtering af JSON-RPC-beskeder
- Integration med MCP-klienter som Claude

Alle løsninger følger den aktuelle MCP-specifikation og bruger den anbefalede stdio-transport for optimal ydeevne og sikkerhed.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.