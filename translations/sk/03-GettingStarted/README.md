## Začíname  

[![Vytvorte svoj prvý MCP server](../../../translated_images/sk/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Kliknite na obrázok vyššie a pozrite si video k tejto lekcii)_

Táto sekcia obsahuje niekoľko lekcií:

- **1 Váš prvý server**, v tejto prvej lekcii sa naučíte, ako vytvoriť svoj prvý server a skontrolovať ho pomocou nástroja Inspector, čo je cenný spôsob testovania a ladenia vášho servera, [k lekcii](01-first-server/README.md)

- **2 Klient**, v tejto lekcii sa naučíte, ako napísať klienta, ktorý sa dokáže pripojiť k vášmu serveru, [k lekcii](02-client/README.md)

- **3 Klient s LLM**, ešte lepší spôsob, ako napísať klienta, je pridať do neho LLM, aby mohol „vyjednávať“ s vaším serverom o tom, čo robiť, [k lekcii](03-llm-client/README.md)

- **4 Spotrebovanie servera v režime GitHub Copilot Agent vo Visual Studio Code**. Tu sa pozrieme na spustenie nášho MCP servera priamo vo Visual Studio Code, [k lekcii](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport je odporúčaný štandard pre komunikáciu medzi MCP serverom a klientom v aktuálnej špecifikácii, poskytujúci bezpečnú komunikáciu založenú na podprocesoch [k lekcii](05-stdio-server/README.md)

- **6 HTTP Streaming s MCP (Streamable HTTP)**. Naučte sa o modernom HTTP streamingu, notifikáciách o pokroku a o tom, ako implementovať škálovateľné, real-time MCP servery a klientov pomocou Streamable HTTP. [k lekcii](06-http-streaming/README.md)

- **7 Využitie AI Toolkit pre VSCode** na spotrebovanie a testovanie vašich MCP klientov a serverov [k lekcii](07-aitk/README.md)

- **8 Testovanie**. Tu sa zameriame najmä na to, ako môžeme testovať náš server a klient rôznymi spôsobmi, [k lekcii](08-testing/README.md)

- **9 Nasadenie**. Táto kapitola sa zaoberá rôznymi spôsobmi nasadenia vašich MCP riešení, [k lekcii](09-deployment/README.md)

- **10 Pokročilé používanie servera**. Táto kapitola pokrýva pokročilé používanie servera, [k lekcii](./10-advanced/README.md)

- **11 Autentifikácia**. Táto kapitola sa zaoberá tým, ako pridať jednoduchú autentifikáciu, od Basic Auth po použitie JWT a RBAC. Odporúčame začať tu a potom sa pozrieť na pokročilé témy v kapitole 5 a vykonať ďalšie zabezpečenie podľa odporúčaní v kapitole 2, [k lekcii](./11-simple-auth/README.md)

Protokol Model Context Protocol (MCP) je otvorený protokol, ktorý štandardizuje, ako aplikácie poskytujú kontext LLM. MCP si môžete predstaviť ako USB-C port pre AI aplikácie - poskytuje štandardizovaný spôsob pripojenia AI modelov k rôznym zdrojom dát a nástrojom.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Nastaviť vývojové prostredie pre MCP v C#, Java, Python, TypeScript a JavaScript
- Vytvoriť a nasadiť základné MCP servery s vlastnými funkciami (zdroje, výzvy a nástroje)
- Vytvoriť hostiteľské aplikácie, ktoré sa pripájajú k MCP serverom
- Testovať a ladiť MCP implementácie
- Pochopiť bežné problémy pri nastavovaní a ich riešenia
- Pripojiť vaše MCP implementácie k populárnym LLM službám

## Nastavenie MCP prostredia

Predtým, než začnete pracovať s MCP, je dôležité pripraviť si vývojové prostredie a pochopiť základný pracovný postup. Táto sekcia vás prevedie počiatočnými krokmi nastavenia, aby ste mohli začať s MCP bez problémov.

### Predpoklady

Predtým, než sa pustíte do vývoja MCP, uistite sa, že máte:

- **Vývojové prostredie**: Pre váš zvolený jazyk (C#, Java, Python, TypeScript alebo JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm alebo akýkoľvek moderný editor kódu
- **Správcovia balíkov**: NuGet, Maven/Gradle, pip alebo npm/yarn
- **API kľúče**: Pre akékoľvek AI služby, ktoré plánujete použiť vo vašich hostiteľských aplikáciách

### Oficiálne SDK

V nasledujúcich kapitolách uvidíte riešenia postavené pomocou Pythonu, TypeScriptu, Javy a .NET. Tu sú všetky oficiálne podporované SDK.

MCP poskytuje oficiálne SDK pre viaceré jazyky:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Udržiavané v spolupráci s Microsoftom
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Udržiavané v spolupráci so Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Oficiálna implementácia TypeScriptu
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Oficiálna implementácia Pythonu
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Oficiálna implementácia Kotlinu
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Udržiavané v spolupráci s Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Oficiálna implementácia Rustu

## Hlavné poznatky

- Nastavenie vývojového prostredia MCP je jednoduché s jazykovo špecifickými SDK
- Budovanie MCP serverov zahŕňa vytváranie a registráciu nástrojov s jasnými schémami
- MCP klienti sa pripájajú k serverom a modelom, aby využívali rozšírené schopnosti
- Testovanie a ladenie sú nevyhnutné pre spoľahlivé MCP implementácie
- Možnosti nasadenia siahajú od lokálneho vývoja po cloudové riešenia

## Precvičovanie

Máme súbor vzorov, ktoré dopĺňajú cvičenia, ktoré uvidíte vo všetkých kapitolách tejto sekcie. Okrem toho má každá kapitola svoje vlastné cvičenia a úlohy.

- [Java Kalkulačka](./samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](./samples/javascript/README.md)
- [TypeScript Kalkulačka](./samples/typescript/README.md)
- [Python Kalkulačka](../../../03-GettingStarted/samples/python)

## Ďalšie zdroje

- [Vytváranie agentov pomocou Model Context Protocol na Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Vzdialený MCP s Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Čo ďalej

Ďalej: [Vytvorenie vášho prvého MCP servera](01-first-server/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.