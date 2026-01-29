## Začínáme  

[![Vytvořte svůj první MCP server](../../../translated_images/cs/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

Tato sekce obsahuje několik lekcí:

- **1 Váš první server**, v této první lekci se naučíte, jak vytvořit svůj první server a prozkoumat ho pomocí inspektorového nástroje, což je cenný způsob testování a ladění serveru, [k lekci](01-first-server/README.md)

- **2 Klient**, v této lekci se naučíte, jak napsat klienta, který se může připojit k vašemu serveru, [k lekci](02-client/README.md)

- **3 Klient s LLM**, ještě lepší způsob psaní klienta je přidání LLM, aby mohl „vyjednávat“ s vaším serverem o tom, co dělat, [k lekci](03-llm-client/README.md)

- **4 Spotřebování serveru v režimu GitHub Copilot Agent ve Visual Studio Code**. Zde se podíváme na spuštění našeho MCP serveru přímo z Visual Studio Code, [k lekci](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport je doporučený standard pro komunikaci mezi MCP serverem a klientem v aktuální specifikaci, poskytující bezpečnou komunikaci založenou na podprocesech [k lekci](05-stdio-server/README.md)

- **6 HTTP Streaming s MCP (Streamable HTTP)**. Naučte se o moderním HTTP streamování, notifikacích o průběhu a jak implementovat škálovatelné, real-time MCP servery a klienty pomocí Streamable HTTP. [k lekci](06-http-streaming/README.md)

- **7 Využití AI Toolkit pro VSCode** k testování a spotřebování vašich MCP klientů a serverů [k lekci](07-aitk/README.md)

- **8 Testování**. Zde se zaměříme zejména na to, jak můžeme testovat náš server a klient různými způsoby, [k lekci](08-testing/README.md)

- **9 Nasazení**. Tato kapitola se zaměří na různé způsoby nasazení vašich MCP řešení, [k lekci](09-deployment/README.md)

- **10 Pokročilé použití serveru**. Tato kapitola pokrývá pokročilé použití serveru, [k lekci](./10-advanced/README.md)

- **11 Autentizace**. Tato kapitola se zabývá tím, jak přidat jednoduchou autentizaci, od Basic Auth po použití JWT a RBAC. Doporučujeme začít zde a poté se podívat na pokročilá témata v kapitole 5 a provést další zabezpečení podle doporučení v kapitole 2, [k lekci](./11-simple-auth/README.md)

Model Context Protocol (MCP) je otevřený protokol, který standardizuje způsob, jakým aplikace poskytují kontext LLM. MCP si můžete představit jako USB-C port pro AI aplikace - poskytuje standardizovaný způsob připojení AI modelů k různým datovým zdrojům a nástrojům.

## Cíle učení

Na konci této lekce budete schopni:

- Nastavit vývojová prostředí pro MCP v C#, Java, Python, TypeScript a JavaScript
- Vytvořit a nasadit základní MCP servery s vlastními funkcemi (zdroje, výzvy a nástroje)
- Vytvořit hostitelské aplikace, které se připojují k MCP serverům
- Testovat a ladit implementace MCP
- Porozumět běžným problémům při nastavení a jejich řešením
- Připojit vaše implementace MCP k populárním LLM službám

## Nastavení vašeho MCP prostředí

Než začnete pracovat s MCP, je důležité připravit vaše vývojové prostředí a pochopit základní pracovní postup. Tato sekce vás provede počátečními kroky nastavení, aby byl váš start s MCP hladký.

### Předpoklady

Než se pustíte do vývoje MCP, ujistěte se, že máte:

- **Vývojové prostředí**: Pro vámi zvolený jazyk (C#, Java, Python, TypeScript nebo JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm nebo jakýkoli moderní editor kódu
- **Správce balíčků**: NuGet, Maven/Gradle, pip nebo npm/yarn
- **API klíče**: Pro jakékoli AI služby, které plánujete použít ve vašich hostitelských aplikacích

### Oficiální SDK

V nadcházejících kapitolách uvidíte řešení postavená pomocí Pythonu, TypeScriptu, Javy a .NET. Zde jsou všechny oficiálně podporované SDK.

MCP poskytuje oficiální SDK pro více jazyků:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Udržováno ve spolupráci s Microsoftem
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Udržováno ve spolupráci se Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Oficiální implementace TypeScriptu
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Oficiální implementace Pythonu
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Oficiální implementace Kotlinu
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Udržováno ve spolupráci s Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Oficiální implementace Rustu

## Klíčové poznatky

- Nastavení vývojového prostředí MCP je jednoduché díky SDK specifickým pro jazyk
- Vytváření MCP serverů zahrnuje tvorbu a registraci nástrojů s jasnými schématy
- MCP klienti se připojují k serverům a modelům, aby využili rozšířené schopnosti
- Testování a ladění jsou nezbytné pro spolehlivé implementace MCP
- Možnosti nasazení sahají od lokálního vývoje po cloudová řešení

## Procvičování

Máme sadu ukázek, které doplňují cvičení, jež uvidíte ve všech kapitolách této sekce. Navíc každá kapitola má své vlastní cvičení a úkoly.

- [Java Kalkulačka](./samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](./samples/javascript/README.md)
- [TypeScript Kalkulačka](./samples/typescript/README.md)
- [Python Kalkulačka](../../../03-GettingStarted/samples/python)

## Další zdroje

- [Vytváření agentů pomocí Model Context Protocol na Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Vzdálený MCP s Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Co dál

Další: [Vytvoření vašeho prvního MCP serveru](01-first-server/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.