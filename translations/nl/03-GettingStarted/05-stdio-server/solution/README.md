# MCP stdio Server-oplossingen

> **⚠️ Belangrijk**: Deze oplossingen zijn bijgewerkt om gebruik te maken van het **stdio-transport**, zoals aanbevolen in de MCP-specificatie van 2025-06-18. Het oorspronkelijke SSE (Server-Sent Events)-transport is verouderd.

Hier zijn de complete oplossingen voor het bouwen van MCP-servers met behulp van het stdio-transport in elke runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Complete stdio-serverimplementatie
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio-server met asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio-server met dependency injection

Elke oplossing demonstreert:
- Het opzetten van stdio-transport
- Het definiëren van servertools
- Correcte JSON-RPC-berichtafhandeling
- Integratie met MCP-clients zoals Claude

Alle oplossingen volgen de huidige MCP-specificatie en maken gebruik van het aanbevolen stdio-transport voor optimale prestaties en beveiliging.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen om nauwkeurigheid te garanderen, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.