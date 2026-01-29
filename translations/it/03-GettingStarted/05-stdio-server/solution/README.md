# Soluzioni Server MCP stdio

> **⚠️ Importante**: Queste soluzioni sono state aggiornate per utilizzare il **trasporto stdio** come raccomandato dalla Specifica MCP 2025-06-18. Il trasporto originale SSE (Server-Sent Events) è stato deprecato.

Ecco le soluzioni complete per costruire server MCP utilizzando il trasporto stdio in ogni runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Implementazione completa del server stdio
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Server stdio in Python con asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Server stdio in .NET con dependency injection

Ogni soluzione dimostra:
- Configurazione del trasporto stdio
- Definizione degli strumenti del server
- Gestione corretta dei messaggi JSON-RPC
- Integrazione con client MCP come Claude

Tutte le soluzioni seguono la specifica MCP attuale e utilizzano il trasporto stdio raccomandato per garantire prestazioni e sicurezza ottimali.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.