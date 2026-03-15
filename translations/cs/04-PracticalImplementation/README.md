# Praktická implementace

[![Jak sestavit, otestovat a nasadit aplikace MCP s reálnými nástroji a pracovními postupy](../../../translated_images/cs/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Kliknutím na obrázek výše zobrazíte video této lekce)_

Praktická implementace je místem, kde se síla Model Context Protocolu (MCP) stává hmatatelnou. Zatímco porozumění teorii a architektuře MCP je důležité, skutečná hodnota se ukáže, když tyto koncepty aplikujete k vytváření, testování a nasazování řešení, která řeší reálné problémy. Tato kapitola překlene propast mezi konceptuálními znalostmi a praktickým vývojem a provede vás procesem oživení aplikací založených na MCP.

Ať už vyvíjíte inteligentní asistenty, integrujete AI do podnikových pracovních postupů, nebo vytváříte vlastní nástroje pro zpracování dat, MCP poskytuje flexibilní základ. Jeho jazykově nezávislý návrh a oficiální SDK pro populární programovací jazyky jej činí přístupným širokému spektru vývojářů. Využitím těchto SDK můžete rychle prototypovat, iterovat a škálovat svá řešení napříč různými platformami a prostředími.

V následujících sekcích najdete praktické příklady, ukázkové kódy a strategie nasazení, které demonstrují, jak implementovat MCP v C#, Javu se Springem, TypeScriptu, JavaScriptu a Pythonu. Naučíte se také, jak ladit a testovat své MCP servery, spravovat API a nasazovat řešení do cloudu pomocí Azure. Tyto praktické zdroje jsou navrženy tak, aby urychlily vaše učení a pomohly vám s jistotou vytvářet robustní aplikace MCP připravené do produkce.

## Přehled

Tato lekce se zaměřuje na praktické aspekty implementace MCP napříč několika programovacími jazyky. Prozkoumáme, jak používat MCP SDK v C#, Javu se Springem, TypeScript, JavaScriptu a Pythonu k vytváření robustních aplikací, ladění a testování MCP serverů a vytváření znovupoužitelných zdrojů, promptů a nástrojů.

## Cíle učení

Na konci této lekce budete schopni:

- Implementovat MCP řešení pomocí oficiálních SDK v různých programovacích jazycích
- Systematicky ladit a testovat MCP servery
- Vytvářet a používat funkce serveru (zdroje, prompty a nástroje)
- Navrhnout efektivní pracovní postupy MCP pro složité úkoly
- Optimalizovat implementace MCP pro výkon a spolehlivost

## Oficiální zdroje SDK

Model Context Protocol nabízí oficiální SDK pro více jazyků (v souladu s [MCP Specifikací 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java se Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Poznámka:** vyžaduje závislost na [Project Reactor](https://projectreactor.io). (Viz [diskusní téma 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Práce s MCP SDK

Tato sekce poskytuje praktické příklady implementace MCP v několika programovacích jazycích. Ukázkové kódy najdete ve složce `samples` organizované podle jazyka.

### Dostupné ukázky

Repositář obsahuje [ukázkové implementace](../../../04-PracticalImplementation/samples) v následujících jazycích:

- [C#](./samples/csharp/README.md)
- [Java se Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Každá ukázka demonstruje klíčové koncepty MCP a vzory implementace pro konkrétní jazyk a ekosystém.

### Praktické průvodce

Další průvodce pro praktickou implementaci MCP:

- [Stránkování a velké množiny výsledků](./pagination/README.md) – Zpracování stránkování založeného na kurzoru pro nástroje, zdroje a velká data

## Hlavní funkce serveru

MCP servery mohou implementovat libovolnou kombinaci těchto funkcí:

### Zdroje

Zdroje poskytují kontext a data pro uživatele nebo AI model k použití:

- Repozitáře dokumentů
- Báze znalostí
- Strukturované zdroje dat
- Souborové systémy

### Prompty

Prompty jsou šablonované zprávy a pracovní postupy pro uživatele:

- Předdefinované šablony konverzací
- Řízené vzory interakcí
- Specializované struktury dialogu

### Nástroje

Nástroje jsou funkce, které může AI model spouštět:

- Utility pro zpracování dat
- Integrace externích API
- Výpočetní možnosti
- Vyhledávací funkce

## Ukázkové implementace: Implementace v C#

Oficiální repozitář C# SDK obsahuje několik ukázkových implementací, které demonstrují různé aspekty MCP:

- **Základní MCP klient**: Jednoduchý příklad, jak vytvořit MCP klienta a volat nástroje
- **Základní MCP server**: Minimální implementace serveru se základní registrací nástrojů
- **Pokročilý MCP server**: Plnohodnotný server s registrací nástrojů, ověřováním a zpracováním chyb
- **Integrace ASP.NET**: Příklady demonstrující integraci s ASP.NET Core
- **Vzory implementace nástrojů**: Různé vzory pro implementaci nástrojů s různou úrovní složitosti

MCP C# SDK je ve fázi preview a API se může měnit. Tento blog budeme průběžně aktualizovat s vývojem SDK.

### Klíčové funkce

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Vytvoření vašeho [prvního MCP serveru](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Pro úplné ukázky implementace v C# navštivte [oficiální repozitář C# SDK ukázek](https://github.com/modelcontextprotocol/csharp-sdk)

## Ukázková implementace: Implementace Java se Spring

Java se Spring SDK nabízí robustní možnosti implementace MCP s funkcemi na úrovni podnikových aplikací.

### Klíčové vlastnosti

- Integrace rámce Spring
- Silná typová bezpečnost
- Podpora reaktivního programování
- Komplexní zpracování chyb

Pro úplnou ukázkovou implementaci Java se Spring viz [ukázka Java se Spring](samples/java/containerapp/README.md) v adresáři ukázek.

## Ukázková implementace: Implementace JavaScript

JavaScript SDK poskytuje lehký a flexibilní přístup k implementaci MCP.

### Klíčové vlastnosti

- Podpora Node.js a prohlížečů
- API založené na Promise
- Snadná integrace s Express a dalšími frameworky
- Podpora WebSocket pro streamování

Pro úplnou ukázkovou implementaci JavaScriptu viz [ukázka JavaScript](samples/javascript/README.md) v adresáři ukázek.

## Ukázková implementace: Implementace Python

Python SDK nabízí pythonický přístup k implementaci MCP s vynikající integrací ML frameworků.

### Klíčové vlastnosti

- Podpora async/await s asyncio
- Integrace FastAPI
- Jednoduchá registrace nástrojů
- Nativní integrace s populárními ML knihovnami

Pro úplnou ukázkovou implementaci Pythonu viz [ukázka Python](samples/python/README.md) v adresáři ukázek.

## Správa API

Azure API Management je skvělou odpovědí na to, jak můžeme zabezpečit MCP servery. Myšlenka je umístit instanci Azure API Management před váš MCP server a nechat jí řešit funkce, které budete pravděpodobně chtít, jako:

- omezení rychlosti (rate limiting)
- správa tokenů
- monitorování
- vyvažování zátěže
- zabezpečení

### Azure ukázka

Zde je Azure ukázka, která dělá přesně to, tj. [vytváří MCP server a zabezpečuje ho pomocí Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Jak probíhá autorizační tok je znázorněno na obrázku níže:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na předchozím obrázku probíhá:

- Ověření/Autorizace probíhá pomocí Microsoft Entra.
- Azure API Management funguje jako brána a využívá zásady k řízení a správě provozu.
- Azure Monitor zaznamenává všechny požadavky pro další analýzu.

#### Autorizační tok

Podívejme se podrobněji na autorizační tok:

![Sekvenční diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specifikace autorizačního procesu MCP

Dozvíte se více o [specifikaci autorizačního procesu MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Nasazení vzdáleného MCP serveru do Azure

Podívejme se, jestli můžeme nasadit dříve zmíněný příklad:

1. Naklonujte repozitář

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Zaregistrujte poskytovatele zdrojů `Microsoft.App`.

   - Pokud používáte Azure CLI, spusťte `az provider register --namespace Microsoft.App --wait`.
   - Pokud používáte Azure PowerShell, spusťte `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Poté spusťte `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` po chvíli pro ověření dokončení registrace.

1. Spusťte tento příkaz [azd](https://aka.ms/azd) pro vytvoření služby správy API, funkční aplikace (s kódem) a všech dalších požadovaných zdrojů Azure

    ```shell
    azd up
    ```

    Tento příkaz by měl nasadit všechny cloudové zdroje na Azure

### Testování vašeho serveru pomocí MCP Inspector

1. V **novém okně terminálu** nainstalujte a spusťte MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Měli byste vidět rozhraní podobné:

    ![Připojení k Node inspector](../../../translated_images/cs/connect.141db0b2bd05f096.webp)

1. CTRL kliknutím načtěte webovou aplikaci MCP Inspector z URL zobrazené v aplikaci (např. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Nastavte typ přenosu na `SSE`
1. Nastavte URL na vaši běžící koncovku správy API typu SSE zobrazenou po `azd up` a **Připojte se**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Seznam nástrojů**. Klikněte na nástroj a **Spusťte nástroj**.

Pokud vše fungovalo, měli byste být nyní připojeni k MCP serveru a podařilo se vám zavolat nástroj.

## MCP servery pro Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Tento soubor repozitářů je rychlý start šablony pro vytváření a nasazení vlastních vzdálených MCP (Model Context Protocol) serverů používajících Azure Functions s Pythonem, C# .NET nebo Node/TypeScript.

Ukázky poskytují kompletní řešení, které umožňuje vývojářům:

- Stavět a spouštět lokálně: Vyvíjet a ladit MCP server na místním počítači
- Nasadit do Azure: Snadné nasazení do cloudu pomocí jednoduchého příkazu azd up
- Připojit klienty: Připojit se k MCP serveru z různých klientů včetně režimu agenta VS Code Copilot a nástroje MCP Inspector

### Klíčové vlastnosti

- Bezpečnost jako součást návrhu: MCP server je zabezpečen pomocí klíčů a HTTPS
- Možnosti autentifikace: Podpora OAuth pomocí vestavěného ověřování a/nebo správy API
- Izolace sítě: Umožňuje izolaci sítě pomocí Azure Virtual Networks (VNET)
- Serverless architektura: Využívá Azure Functions pro škálovatelné a událostmi řízené zpracování
- Lokální vývoj: Komplexní podpora lokálního vývoje a ladění
- Jednoduché nasazení: Zjednodušený proces nasazení do Azure

Repozitář zahrnuje všechny potřebné konfigurační soubory, zdrojový kód a definice infrastruktury pro rychlý start s produkčně připravenou implementací MCP serveru.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Ukázková implementace MCP používající Azure Functions s Pythonem

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Ukázková implementace MCP používající Azure Functions s C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Ukázková implementace MCP používající Azure Functions s Node/TypeScript.

## Hlavní závěry

- SDK MCP poskytují jazykově specifické nástroje pro implementaci robustních MCP řešení
- Proces ladění a testování je klíčový pro spolehlivé MCP aplikace
- Znovupoužitelné šablony promptů umožňují konzistentní interakce s AI
- Dobře navržené pracovní postupy dokážou orchestraci složitých úkolů využívajících více nástrojů
- Implementace MCP řešení vyžaduje zvážení bezpečnosti, výkonu a zpracování chyb

## Cvičení

Navrhněte praktický pracovní postup MCP, který řeší reálný problém ve vašem oboru:

1. Identifikujte 3-4 nástroje, které by byly užitečné pro řešení tohoto problému
2. Vytvořte diagram pracovního postupu ukazující, jak tyto nástroje spolupracují
3. Implementujte základní verzi jednoho z nástrojů ve vašem preferovaném jazyce
4. Vytvořte šablonu promptu, která by pomohla modelu efektivně používat váš nástroj

## Další zdroje

---

## Co dál

Další: [Pokročilá témata](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace je doporučován profesionální lidský překlad. Nejsme odpovědní za jakákoliv nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->