## Početak  

[![Izgradite svoj prvi MCP poslužitelj](../../../translated_images/hr/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Kliknite na sliku iznad za pregled videa ove lekcije)_

Ovaj odjeljak sastoji se od nekoliko lekcija:

- **1 Vaš prvi poslužitelj**, u ovoj prvoj lekciji naučit ćete kako stvoriti svoj prvi poslužitelj i pregledati ga pomoću alata za inspekciju, vrijednog načina za testiranje i otklanjanje pogrešaka vašeg poslužitelja, [na lekciju](01-first-server/README.md)

- **2 Klijent**, u ovoj lekciji naučit ćete kako napisati klijent koji se može povezati s vašim poslužiteljem, [na lekciju](02-client/README.md)

- **3 Klijent s LLM-om**, još bolji način pisanja klijenta je dodavanje LLM-a kako bi mogao "pregovarati" s vašim poslužiteljem o tome što učiniti, [na lekciju](03-llm-client/README.md)

- **4 Korištenje poslužitelja u načinu GitHub Copilot Agent u Visual Studio Code-u**. Ovdje ćemo pogledati pokretanje našeg MCP poslužitelja unutar Visual Studio Code-a, [na lekciju](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport je preporučeni standard za komunikaciju između MCP poslužitelja i klijenta u trenutnoj specifikaciji, pružajući sigurnu komunikaciju temeljenu na podprocesima [na lekciju](05-stdio-server/README.md)

- **6 HTTP Streaming s MCP-om (Streamable HTTP)**. Naučite o modernom HTTP streamingu, obavijestima o napretku i kako implementirati skalabilne, real-time MCP poslužitelje i klijente koristeći Streamable HTTP. [na lekciju](06-http-streaming/README.md)

- **7 Korištenje AI alata za VSCode** za konzumaciju i testiranje vaših MCP klijenata i poslužitelja [na lekciju](07-aitk/README.md)

- **8 Testiranje**. Ovdje ćemo se posebno fokusirati na različite načine testiranja vašeg poslužitelja i klijenta, [na lekciju](08-testing/README.md)

- **9 Implementacija**. Ovaj poglavlje će istražiti različite načine implementacije vaših MCP rješenja, [na lekciju](09-deployment/README.md)

- **10 Napredno korištenje poslužitelja**. Ovo poglavlje pokriva napredne načine korištenja poslužitelja, [na lekciju](./10-advanced/README.md)

- **11 Autentifikacija**. Ovo poglavlje pokriva kako dodati jednostavnu autentifikaciju, od osnovne autentifikacije do korištenja JWT-a i RBAC-a. Preporučuje se započeti ovdje, a zatim pogledati napredne teme u poglavlju 5 i provesti dodatno osiguranje prema preporukama u poglavlju 2, [na lekciju](./11-simple-auth/README.md)

Model Context Protocol (MCP) je otvoreni protokol koji standardizira način na koji aplikacije pružaju kontekst LLM-ovima. Zamislite MCP kao USB-C priključak za AI aplikacije - pruža standardizirani način povezivanja AI modela s različitim izvorima podataka i alatima.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Postaviti razvojna okruženja za MCP u C#, Java, Python, TypeScript i JavaScript
- Izgraditi i implementirati osnovne MCP poslužitelje s prilagođenim značajkama (resursi, upiti i alati)
- Stvoriti host aplikacije koje se povezuju s MCP poslužiteljima
- Testirati i otkloniti pogreške MCP implementacija
- Razumjeti uobičajene izazove postavljanja i njihova rješenja
- Povezati svoje MCP implementacije s popularnim LLM uslugama

## Postavljanje MCP okruženja

Prije nego što započnete rad s MCP-om, važno je pripremiti razvojno okruženje i razumjeti osnovni tijek rada. Ovaj odjeljak će vas voditi kroz početne korake postavljanja kako biste osigurali nesmetan početak rada s MCP-om.

### Preduvjeti

Prije nego što se upustite u MCP razvoj, osigurajte da imate:

- **Razvojno okruženje**: Za odabrani jezik (C#, Java, Python, TypeScript ili JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm ili bilo koji moderni editor koda
- **Upravitelji paketa**: NuGet, Maven/Gradle, pip ili npm/yarn
- **API ključeve**: Za sve AI usluge koje planirate koristiti u svojim host aplikacijama

### Službeni SDK-ovi

U nadolazećim poglavljima vidjet ćete rješenja izgrađena koristeći Python, TypeScript, Java i .NET. Ovdje su svi službeno podržani SDK-ovi.

MCP pruža službene SDK-ove za više jezika:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Održava se u suradnji s Microsoftom
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Održava se u suradnji s Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Službena TypeScript implementacija
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Službena Python implementacija
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Službena Kotlin implementacija
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Održava se u suradnji s Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Službena Rust implementacija

## Ključne točke

- Postavljanje MCP razvojnog okruženja je jednostavno uz SDK-ove specifične za jezik
- Izgradnja MCP poslužitelja uključuje stvaranje i registraciju alata s jasnim shemama
- MCP klijenti se povezuju s poslužiteljima i modelima kako bi iskoristili proširene mogućnosti
- Testiranje i otklanjanje pogrešaka ključni su za pouzdane MCP implementacije
- Opcije implementacije kreću se od lokalnog razvoja do rješenja temeljenih na oblaku

## Vježbanje

Imamo set primjera koji nadopunjuju vježbe koje ćete vidjeti u svim poglavljima ovog odjeljka. Osim toga, svako poglavlje također ima svoje vježbe i zadatke.

- [Java Kalkulator](./samples/java/calculator/README.md)
- [.Net Kalkulator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](./samples/javascript/README.md)
- [TypeScript Kalkulator](./samples/typescript/README.md)
- [Python Kalkulator](../../../03-GettingStarted/samples/python)

## Dodatni resursi

- [Izgradnja agenata koristeći Model Context Protocol na Azureu](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP s Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Što slijedi

Sljedeće: [Stvaranje vašeg prvog MCP poslužitelja](01-first-server/README.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.