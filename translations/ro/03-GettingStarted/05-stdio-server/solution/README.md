# Soluții MCP stdio Server

> **⚠️ Important**: Aceste soluții au fost actualizate pentru a utiliza **transportul stdio**, conform recomandărilor din Specificația MCP 2025-06-18. Transportul original SSE (Server-Sent Events) a fost depreciat.

Iată soluțiile complete pentru construirea serverelor MCP folosind transportul stdio în fiecare mediu de execuție:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Implementare completă a serverului stdio
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Server stdio în Python cu asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Server stdio în .NET cu injecție de dependențe

Fiecare soluție demonstrează:
- Configurarea transportului stdio
- Definirea instrumentelor serverului
- Gestionarea corectă a mesajelor JSON-RPC
- Integrarea cu clienți MCP precum Claude

Toate soluțiile respectă specificația actuală MCP și utilizează transportul stdio recomandat pentru performanță și securitate optime.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.