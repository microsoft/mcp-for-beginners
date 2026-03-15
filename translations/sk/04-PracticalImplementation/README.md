# Praktická implementácia

[![Ako vytvoriť, testovať a nasadiť MCP aplikácie pomocou reálnych nástrojov a pracovných tokov](../../../translated_images/sk/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

Praktická implementácia je miesto, kde sa sila Model Context Protocolu (MCP) stáva hmatateľnou. Kým pochopenie teórie a architektúry za MCP je dôležité, skutočná hodnota sa ukazuje, keď tieto koncepty využijete na tvorbu, testovanie a nasadenie riešení, ktoré riešia reálne problémy. Táto kapitola premostí priepasť medzi konceptuálnymi znalosťami a praktickým vývojom a prevedie vás procesom oživenia aplikácií založených na MCP.

Či už vyvíjate inteligentných asistentov, integrujete AI do podnikových pracovných tokov alebo tvoríte vlastné nástroje na spracovanie dát, MCP poskytuje flexibilný základ. Jeho jazykovo nezávislý dizajn a oficiálne SDK pre populárne programovacie jazyky ho sprístupňujú širokému spektru vývojárov. Využitím týchto SDK môžete rýchlo prototypovať, iterovať a škálovať svoje riešenia na rôznych platformách a prostrediach.

V nasledujúcich častiach nájdete praktické príklady, ukážkový kód a stratégie nasadenia, ktoré demonštrujú, ako implementovať MCP v C#, Java so Spring, TypeScript, JavaScript a Pythone. Naučíte sa tiež, ako ladit a testovať svoje MCP servery, spravovať API a nasadzovať riešenia do cloudu pomocou Azure. Tieto praktické zdroje sú navrhnuté tak, aby urýchlili vaše učenie a pomohli vám s istotou vytvárať robustné produkčné MCP aplikácie.

## Prehľad

Táto lekcia sa zameriava na praktické aspekty implementácie MCP v rôznych programovacích jazykoch. Preskúmame, ako používať MCP SDK v C#, Java so Spring, TypeScript, JavaScript a Pythone na tvorbu robustných aplikácií, ladenie a testovanie MCP serverov a tvorbu znovupoužiteľných zdrojov, promptov a nástrojov.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Implementovať MCP riešenia pomocou oficiálnych SDK v rôznych programovacích jazykoch
- Systematicky ladiť a testovať MCP servery
- Vytvárať a používať funkcie servera (Zdroje, Prompt a Nástroje)
- Navrhovať efektívne MCP pracovné toky pre komplexné úlohy
- Optimalizovať MCP implementácie pre výkon a spoľahlivosť

## Oficiálne SDK zdroje

Model Context Protocol ponúka oficiálne SDK pre viaceré jazyky (v súlade s [MCP Špecifikáciou 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java so Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Poznámka:** vyžaduje závislosť na [Project Reactor](https://projectreactor.io). (Pozri [diskusný issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Práca s MCP SDK

Táto sekcia poskytuje praktické príklady implementácie MCP v rôznych programovacích jazykoch. Ukážkový kód nájdete v adresári `samples` zoradený podľa jazyka.

### Dostupné ukážky

Repozitár obsahuje [ukážkové implementácie](../../../04-PracticalImplementation/samples) v nasledujúcich jazykoch:

- [C#](./samples/csharp/README.md)
- [Java so Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Každá ukážka demonštruje kľúčové MCP koncepty a vzory implementácie pre daný jazyk a ekosystém.

### Praktické návody

Ďalšie návody pre praktickú implementáciu MCP:

- [Paginácia a veľké výsledkové sady](./pagination/README.md) – Správa stránkovania pomocou kurzorov pre nástroje, zdroje a veľké množiny dát

## Hlavné funkcie servera

MCP servery môžu implementovať ľubovoľnú kombináciu týchto funkcií:

### Zdroje

Zdroje poskytujú kontext a dáta pre používateľa alebo AI model:

- Úložiská dokumentov
- Znalostné bázy
- Štruktúrované dátové zdroje
- Súborové systémy

### Prompt (výzvy)

Prompt sú šablónované správy a pracovné toky pre používateľov:

- Preddefinované konverzačné šablóny
- Usmernené vzory interakcie
- Špecializované dialógové štruktúry

### Nástroje

Nástroje sú funkcie, ktoré môže AI model vykonávať:

- Nástroje na spracovanie dát
- Integrácie s externými API
- Výpočtové schopnosti
- Funkcionalita vyhľadávania

## Ukážkové implementácie: C# implementácia

Oficiálny C# SDK repozitár obsahuje niekoľko ukážkových implementácií demonštrujúcich rôzne aspekty MCP:

- **Základný MCP klient**: Jednoduchý príklad, ako vytvoriť MCP klienta a volať nástroje
- **Základný MCP server**: Minimálna implementácia servera so základnou registráciou nástrojov
- **Pokročilý MCP server**: Plnofunkčný server s registráciou nástrojov, autentifikáciou a ošetrením chýb
- **Integrácia ASP.NET**: Príklady integrácie s ASP.NET Core
- **Vzory implementácie nástrojov**: Rôzne vzory implementácie nástrojov s rôznou mierou zložitosti

MCP C# SDK je vo verzii preview a API sa môžu meniť. Tento blog budeme priebežne aktualizovať podľa vývoja SDK.

### Kľúčové funkcie

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Stavba vášho [prvého MCP servera](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Pre kompletné ukážky implementácie v C# navštívte [oficiálny repozitár s ukážkami C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Ukážková implementácia: Java so Spring implementácia

Java so Spring SDK ponúka robustné možnosti implementácie MCP s funkcionalitami na úrovni enterprise.

### Kľúčové funkcie

- Integrácia so Spring Frameworkom
- Silná typová bezpečnosť
- Podpora reaktívneho programovania
- Komplexné ošetrovanie chýb

Pre kompletnú ukážku implementácie Java so Spring pozrite [Java so Spring ukážku](samples/java/containerapp/README.md) v adresári samples.

## Ukážková implementácia: JavaScript implementácia

JavaScript SDK poskytuje ľahký a flexibilný prístup k implementácii MCP.

### Kľúčové funkcie

- Podpora Node.js a prehliadača
- API založené na Promise
- Jednoduchá integrácia s Express a ďalšími frameworkmi
- Podpora WebSocket pre streamovanie

Pre kompletnú JavaScript ukážku implementácie pozrite [JavaScript ukážku](samples/javascript/README.md) v adresári samples.

## Ukážková implementácia: Python implementácia

Python SDK ponúka pythonický prístup k implementácii MCP s vynikajúcou integráciou ML frameworkov.

### Kľúčové funkcie

- Podpora async/await s asyncio
- Integrácia s FastAPI``
- Jednoduchá registrácia nástrojov
- Nativna integrácia s populárnymi ML knižnicami

Pre kompletnú Python implementáciu pozrite [Python ukážku](samples/python/README.md) v adresári samples.

## Správa API

Azure API Management je skvelým riešením na zabezpečenie MCP serverov. Myšlienka je umiestniť Azure API Management inštanciu pred váš MCP server a nechať ju spravovať funkcie, ktoré pravdepodobne budete chcieť, ako napríklad:

- obmedzovanie rýchlosti
- správa tokenov
- monitorovanie
- vyvažovanie záťaže
- bezpečnosť

### Príklad Azure

Tu je Azure ukážka, ktorá robí presne to, teda [vytvára MCP server a zabezpečuje ho pomocou Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Pozrite sa, ako prebieha autorizačný tok na obrázku nižšie:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na predchádzajúcom obrázku prebieha:

- Autentifikácia/autorizácia pomocou Microsoft Entra.
- Azure API Management funguje ako brána a používa politiky na smerovanie a správu prevádzky.
- Azure Monitor zapisuje všetky požiadavky pre ďalšiu analýzu.

#### Autorizačný tok

Pozrime sa bližšie na autorizačný tok:

![Sekvenčný diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Špecifikácia autorizácie MCP

Viac sa dozviete o [MCP špecifikácii autorizácie](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Nasadenie vzdialeného MCP servera do Azure

Pozrime sa, či môžeme nasadiť ukážku, ktorú sme spomenuli vyššie:

1. Klonujte repozitár

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Zaregistrujte poskytovateľa zdrojov `Microsoft.App`.

   - Ak používate Azure CLI, spustite `az provider register --namespace Microsoft.App --wait`.
   - Ak používate Azure PowerShell, spustite `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Následne po nejakej dobe skontrolujte `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`, či je registrácia dokončená.

1. Spustite tento [azd](https://aka.ms/azd) príkaz na provisionovanie služby správy API, funkčnej aplikácie (s kódom) a všetkých ostatných potrebných Azure zdrojov

    ```shell
    azd up
    ```

    Tento príkaz by mal nasadiť všetky cloudové zdroje na Azure

### Testovanie vášho servera pomocou MCP Inspector

1. V **novom terminálovom okne** nainštalujte a spustite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Mali by ste vidieť rozhranie podobné:

    ![Pripojenie k Node inspector](../../../translated_images/sk/connect.141db0b2bd05f096.webp)

1. CTRL kliknite pre načítanie MCP Inspector webovej aplikácie z URL zobrazenej aplikáciou (napr. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Nastavte typ transportu na `SSE`
1. Nastavte URL na bežiaci API Management SSE endpoint, ktorý sa zobrazil po `azd up` a **Pripojte sa**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Zoznam nástrojov**. Kliknite na nástroj a **Spustite nástroj**.

Ak všetky kroky prebehli správne, teraz by ste mali byť pripojení k MCP serveru a úspešne zavolali nástroj.

## MCP servery pre Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Táto skupina repozitárov je rýchly štartovací šablónový projekt na tvorbu a nasadenie vlastných vzdialených MCP (Model Context Protocol) serverov pomocou Azure Functions v Pythone, C# .NET alebo Node/TypeScript.

Ukážky poskytujú kompletné riešenie, ktoré umožňuje vývojárom:

- Vytvárať a spúšťať lokálne: Vyvíjať a ladiť MCP server na lokálnom počítači
- Nasadzovať do Azure: Jednoducho nasadiť do cloudu príkazom azd up
- Pripojiť sa z klientov: Pripojiť sa k MCP serveru z rôznych klientov vrátane režimu agenta Copilot vo VS Code a nástroja MCP Inspector

### Kľúčové funkcie

- Bezpečnosť podľa dizajnu: MCP server je zabezpečený pomocou kľúčov a HTTPS
- Možnosti autentifikácie: Podporuje OAuth s integrovanou autentifikáciou a/alebo API Management
- Izolácia siete: Umožňuje sieťovú izoláciu pomocou Azure Virtual Networks (VNET)
- Serverless architektúra: Využíva Azure Functions pre škálovateľnú event-driven exekúciu
- Lokálny vývoj: Komplexná podpora pre lokálny vývoj a ladenie
- Jednoduché nasadenie: Zjednodušený proces nasadenia do Azure

Repozitár obsahuje všetky potrebné konfiguračné súbory, zdrojový kód a definície infraštruktúry na rýchly štart s produkčnou MCP serverovou implementáciou.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Ukážková implementácia MCP pomocou Azure Functions v Pythone

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Ukážková implementácia MCP pomocou Azure Functions v C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Ukážková implementácia MCP pomocou Azure Functions v Node/TypeScript.

## Kľúčové poznatky

- MCP SDK poskytujú nástroje špecifické pre jazyky na implementáciu robustných MCP riešení
- Proces ladenia a testovania je kritický pre spoľahlivé MCP aplikácie
- Znovupoužiteľné šablóny promptov umožňujú konzistentnú AI interakciu
- Dobre navrhnuté pracovné toky dokážu zorganizovať komplexné úlohy s viacerými nástrojmi
- Implementácia MCP riešení si vyžaduje zváženie bezpečnosti, výkonu a ošetrenia chýb

## Cvičenie

Navrhnite praktický MCP pracovný tok, ktorý rieši reálny problém vo vašej oblasti:

1. Identifikujte 3-4 nástroje, ktoré by boli užitočné na riešenie tohto problému
2. Vytvorte diagram pracovného toku ukazujúci, ako tieto nástroje spolupracujú
3. Implementujte základnú verziu jedného z nástrojov vo vašom preferovanom jazyku
4. Vytvorte šablónu promptu, ktorá by pomohla modelu efektívne používať váš nástroj

## Dodatočné zdroje

---

## Čo nasleduje

Nasleduje: [Pokročilé témy](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o vylúčení zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, uvedomte si, prosím, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->