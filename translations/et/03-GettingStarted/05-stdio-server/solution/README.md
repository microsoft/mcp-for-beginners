# MCP stdio Serveri Lahendused

> **⚠️ Tähtis**: Need lahendused on uuendatud, et kasutada **stdio transporti**, nagu on soovitatud MCP spetsifikatsioonis 2025-06-18. Algne SSE (Server-Sent Events) transport on aegunud.

Siin on täielikud lahendused MCP serverite loomiseks stdio transpordi abil igas käituskeskkonnas:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Täielik stdio serveri teostus
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio server koos asyncio-ga
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio server koos sõltuvuste süstimisega

Iga lahendus näitab:
- Stdio transpordi seadistamist
- Serveri tööriistade määratlemist
- Õiget JSON-RPC sõnumite käsitlemist
- Integratsiooni MCP klientidega, nagu Claude

Kõik lahendused järgivad praegust MCP spetsifikatsiooni ja kasutavad soovitatud stdio transporti parima jõudluse ja turvalisuse tagamiseks.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.