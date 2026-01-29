# MCP stdio Strežniške Rešitve

> **⚠️ Pomembno**: Te rešitve so bile posodobljene za uporabo **stdio transporta**, kot je priporočeno v MCP Specifikaciji 2025-06-18. Prvotni SSE (Server-Sent Events) transport je bil ukinjen.

Tukaj so popolne rešitve za gradnjo MCP strežnikov z uporabo stdio transporta v vsakem okolju izvajanja:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Popolna implementacija stdio strežnika
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio strežnik z asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio strežnik z vbrizgavanjem odvisnosti

Vsaka rešitev prikazuje:
- Nastavitev stdio transporta
- Definiranje strežniških orodij
- Pravilno obravnavo JSON-RPC sporočil
- Integracijo z MCP odjemalci, kot je Claude

Vse rešitve sledijo trenutni MCP specifikaciji in uporabljajo priporočeni stdio transport za optimalno zmogljivost in varnost.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.