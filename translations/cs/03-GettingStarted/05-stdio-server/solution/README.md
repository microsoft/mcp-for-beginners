# MCP stdio Server Solutions

> **⚠️ Důležité**: Tato řešení byla aktualizována tak, aby používala **stdio transport**, jak je doporučeno ve specifikaci MCP 2025-06-18. Původní transport SSE (Server-Sent Events) byl ukončen.

Zde jsou kompletní řešení pro vytváření MCP serverů s využitím stdio transportu v jednotlivých runtime prostředích:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Kompletní implementace stdio serveru
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio server s asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio server s dependency injection

Každé řešení ukazuje:
- Nastavení stdio transportu
- Definování serverových nástrojů
- Správné zpracování zpráv JSON-RPC
- Integraci s MCP klienty, jako je Claude

Všechna řešení odpovídají aktuální specifikaci MCP a využívají doporučený stdio transport pro optimální výkon a bezpečnost.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.