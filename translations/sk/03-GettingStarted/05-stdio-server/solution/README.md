# MCP stdio Server Riešenia

> **⚠️ Dôležité**: Tieto riešenia boli aktualizované na používanie **stdio transportu** podľa odporúčaní MCP Špecifikácie z 18. júna 2025. Pôvodný transport SSE (Server-Sent Events) bol vyradený.

Tu sú kompletné riešenia na vytvorenie MCP serverov s použitím stdio transportu pre jednotlivé runtime prostredia:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Kompletná implementácia stdio servera
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio server s asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio server s dependency injection

Každé riešenie demonštruje:
- Nastavenie stdio transportu
- Definovanie nástrojov servera
- Správne spracovanie JSON-RPC správ
- Integráciu s MCP klientmi, ako je Claude

Všetky riešenia dodržiavajú aktuálnu MCP špecifikáciu a používajú odporúčaný stdio transport pre optimálny výkon a bezpečnosť.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.