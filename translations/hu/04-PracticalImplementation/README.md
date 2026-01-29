# Gyakorlati Megvalósítás

[![Hogyan építsünk, teszteljünk és telepítsünk MCP alkalmazásokat valós eszközökkel és munkafolyamatokkal](../../../translated_images/hu/05.64bea204e25ca891e3dd8b8f960d2170b9a000d8364305f57db3ec4a2c049a9a.png)](https://youtu.be/vCN9-mKBDfQ)

_(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

A gyakorlati megvalósítás az a pont, ahol a Model Context Protocol (MCP) ereje kézzelfoghatóvá válik. Bár az MCP mögötti elmélet és architektúra megértése fontos, az igazi érték akkor jelenik meg, amikor ezeket a koncepciókat alkalmazva olyan megoldásokat hozunk létre, amelyek valós problémákat oldanak meg. Ez a fejezet áthidalja az elméleti tudás és a gyakorlati fejlesztés közötti szakadékot, és végigvezet az MCP-alapú alkalmazások életre keltésének folyamatán.

Akár intelligens asszisztenseket fejlesztesz, mesterséges intelligenciát integrálsz üzleti munkafolyamatokba, vagy egyedi adatfeldolgozó eszközöket építesz, az MCP rugalmas alapot biztosít. Nyelvfüggetlen kialakítása és a népszerű programozási nyelvekhez készült hivatalos SDK-k révén széles fejlesztői kör számára elérhető. Ezeket az SDK-kat használva gyorsan prototípusokat készíthetsz, iterálhatsz, és méretezheted megoldásaidat különböző platformokon és környezetekben.

A következő szakaszokban gyakorlati példákat, mintakódokat és telepítési stratégiákat találsz, amelyek bemutatják, hogyan valósítható meg az MCP C#, Java Spring, TypeScript, JavaScript és Python nyelveken. Megtanulod továbbá, hogyan hibakeresd és teszteld az MCP szervereket, kezeld az API-kat, és telepítsd a megoldásokat a felhőbe az Azure segítségével. Ezek a gyakorlati források célja, hogy felgyorsítsák a tanulási folyamatot, és magabiztossá tegyenek a robusztus, éles környezetre kész MCP alkalmazások építésében.

## Áttekintés

Ez a lecke az MCP megvalósításának gyakorlati aspektusaira összpontosít több programozási nyelven. Megvizsgáljuk, hogyan használhatók az MCP SDK-k C#, Java Spring, TypeScript, JavaScript és Python nyelveken robusztus alkalmazások építésére, MCP szerverek hibakeresésére és tesztelésére, valamint újrahasznosítható erőforrások, promptok és eszközök létrehozására.

## Tanulási Célok

A lecke végére képes leszel:

- MCP megoldásokat megvalósítani hivatalos SDK-k segítségével különböző programozási nyelveken
- MCP szervereket rendszerszerűen hibakeresni és tesztelni
- Szerverfunkciókat (Erőforrások, Promptok és Eszközök) létrehozni és használni
- Hatékony MCP munkafolyamatokat tervezni összetett feladatokhoz
- MCP megvalósításokat optimalizálni teljesítmény és megbízhatóság szempontjából

## Hivatalos SDK Források

A Model Context Protocol több nyelvhez is kínál hivatalos SDK-kat:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Megjegyzés:** függ a [Project Reactor](https://projectreactor.io) projekttől. (Lásd: [246-os vita](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## MCP SDK-k Használata

Ez a szakasz gyakorlati példákat nyújt az MCP több programozási nyelven történő megvalósítására. A `samples` könyvtárban nyelvenként rendezett mintakódokat találhatsz.

### Elérhető Minták

A repó a következő nyelveken tartalmaz [minta megvalósításokat](../../../04-PracticalImplementation/samples):

- [C#](./samples/csharp/README.md)
- [Java Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Minden minta bemutatja az adott nyelvhez és ökoszisztémához kapcsolódó kulcsfontosságú MCP koncepciókat és megvalósítási mintákat.

## Alapvető Szerverfunkciók

Az MCP szerverek az alábbi funkciók bármely kombinációját megvalósíthatják:

### Erőforrások

Az erőforrások kontextust és adatokat biztosítanak a felhasználó vagy az AI modell számára:

- Dokumentumtárak
- Tudásbázisok
- Strukturált adatforrások
- Fájlrendszerek

### Promptok

A promptok sablonüzenetek és munkafolyamatok a felhasználók számára:

- Előre definiált beszélgetési sablonok
- Irányított interakciós minták
- Speciális párbeszédstruktúrák

### Eszközök

Az eszközök olyan funkciók, amelyeket az AI modell végrehajthat:

- Adatfeldolgozó segédprogramok
- Külső API integrációk
- Számítási képességek
- Keresési funkciók

## Minta Megvalósítások: C# Megvalósítás

A hivatalos C# SDK repó több minta megvalósítást tartalmaz, amelyek az MCP különböző aspektusait mutatják be:

- **Alapvető MCP kliens**: Egyszerű példa egy MCP kliens létrehozására és eszközök meghívására
- **Alapvető MCP szerver**: Minimális szervermegvalósítás alapvető eszközregisztrációval
- **Haladó MCP szerver**: Teljes funkcionalitású szerver eszközregisztrációval, hitelesítéssel és hibakezeléssel
- **ASP.NET integráció**: Példák az ASP.NET Core-ral való integrációra
- **Eszközmegvalósítási minták**: Különböző minták eszközök különböző összetettségi szinteken történő megvalósítására

A C# MCP SDK előzetes verzióban van, és az API-k változhatnak. A blogot folyamatosan frissítjük az SDK fejlődésével.

### Főbb Jellemzők

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- [Első MCP szervered építése](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

A teljes C# megvalósítási mintákért látogasd meg a [hivatalos C# SDK minták repóját](https://github.com/modelcontextprotocol/csharp-sdk).

## Minta Megvalósítás: Java Spring Megvalósítás

A Java Spring SDK robusztus MCP megvalósítási lehetőségeket kínál vállalati szintű funkciókkal.

### Főbb Jellemzők

- Spring Framework integráció
- Erős típusbiztonság
- Reaktív programozási támogatás
- Átfogó hibakezelés

A teljes Java Spring megvalósítási mintáért lásd a [Java Spring mintát](samples/java/containerapp/README.md) a minták könyvtárában.

## Minta Megvalósítás: JavaScript Megvalósítás

A JavaScript SDK könnyű és rugalmas megközelítést kínál az MCP megvalósításához.

### Főbb Jellemzők

- Node.js és böngésző támogatás
- Promise-alapú API
- Könnyű integráció az Express-szel és más keretrendszerekkel
- WebSocket támogatás streaminghez

A teljes JavaScript megvalósítási mintáért lásd a [JavaScript mintát](samples/javascript/README.md) a minták könyvtárában.

## Minta Megvalósítás: Python Megvalósítás

A Python SDK Python-barát megközelítést kínál az MCP megvalósításához, kiváló ML keretrendszer-integrációkkal.

### Főbb Jellemzők

- Async/await támogatás asyncio-val
- FastAPI integráció
- Egyszerű eszközregisztráció
- Natív integráció népszerű ML könyvtárakkal

A teljes Python megvalósítási mintáért lásd a [Python mintát](samples/python/README.md) a minták könyvtárában.

## API Kezelés

Az Azure API Management kiváló megoldás az MCP szerverek biztonságossá tételére. Az ötlet az, hogy egy Azure API Management példányt helyezünk az MCP szerver elé, és hagyjuk, hogy az kezelje azokat a funkciókat, amelyeket valószínűleg szeretnénk, például:

- sebességkorlátozás
- tokenkezelés
- monitorozás
- terheléselosztás
- biztonság

### Azure Példa

Itt egy Azure példa, amely pontosan ezt teszi, azaz [MCP szerver létrehozása és biztosítása Azure API Management segítségével](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Lásd az alábbi képen, hogyan zajlik az autorizációs folyamat:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

A fenti képen a következő történik:

- Azonosítás/hitelesítés a Microsoft Entra segítségével történik.
- Az Azure API Management átjáróként működik, és szabályzatokat használ a forgalom irányítására és kezelésére.
- Az Azure Monitor naplózza az összes kérést további elemzés céljából.

#### Autorizációs Folyamat

Nézzük meg részletesebben az autorizációs folyamatot:

![Szekvencia Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autorizációs specifikáció

További információ az [MCP autorizációs specifikációról](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow).

## Távoli MCP Szerver Telepítése Azure-ra

Nézzük meg, hogyan telepíthetjük a korábban említett mintát:

1. Klónozd a repót

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Regisztráld a `Microsoft.App` erőforrás-szolgáltatót.

   - Ha az Azure CLI-t használod, futtasd: `az provider register --namespace Microsoft.App --wait`.
   - Ha az Azure PowerShell-t használod, futtasd: `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Ezután futtasd: `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`, hogy ellenőrizd, befejeződött-e a regisztráció.

1. Futtasd ezt az [azd](https://aka.ms/azd) parancsot az API-kezelési szolgáltatás, a funkcióalkalmazás (kóddal) és az összes szükséges Azure-erőforrás telepítéséhez:

    ```shell
    azd up
    ```

    Ez a parancs telepíti az összes felhőalapú erőforrást az Azure-ra.

### Szerver Tesztelése MCP Inspectorral

1. Egy **új terminálablakban** telepítsd és futtasd az MCP Inspectort:

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Egy hasonló felületet kell látnod:

    ![Node Inspectorhoz csatlakozás](../../../translated_images/hu/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

1. CTRL kattintással töltsd be az MCP Inspector webalkalmazást az alkalmazás által megjelenített URL-ről (pl. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)).
1. Állítsd be a szállítási típust `SSE`-re.
1. Állítsd be az URL-t a futó API Management SSE végpontra, amely az `azd up` után jelenik meg, majd **Csatlakozz**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Eszközök listázása**. Kattints egy eszközre, majd **Eszköz futtatása**.

Ha minden lépés sikeres volt, most csatlakozva kell lenned az MCP szerverhez, és képesnek kell lenned egy eszköz meghívására.

## MCP Szerverek Azure-hoz

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ez a repósorozat gyorsindítási sablonokat kínál egyedi távoli MCP (Model Context Protocol) szerverek építéséhez és telepítéséhez Azure Functions segítségével Python, C# .NET vagy Node/TypeScript nyelveken.

A minták teljes megoldást nyújtanak, amely lehetővé teszi a fejlesztők számára:

- Helyi futtatás: MCP szerver fejlesztése és hibakeresése helyi gépen
- Azure-ra telepítés: Egyszerűen telepíthető a felhőbe egy egyszerű `azd up` paranccsal
- Kapcsolódás kliensekről: Kapcsolódás az MCP szerverhez különböző kliensekről, beleértve a VS Code Copilot ügynök módját és az MCP Inspector eszközt

### Főbb Jellemzők

- Biztonságos kialakítás: Az MCP szerver kulcsokkal és HTTPS-sel van biztosítva
- Hitelesítési lehetőségek: Támogatja az OAuth-ot beépített hitelesítéssel és/vagy API Managementtel
- Hálózati izoláció: Hálózati izolációt tesz lehetővé Azure Virtual Networks (VNET) használatával
- Szerver nélküli architektúra: Az Azure Functions-t használja skálázható, eseményvezérelt végrehajtáshoz
- Helyi fejlesztés: Átfogó helyi fejlesztési és hibakeresési támogatás
- Egyszerű telepítés: Egyszerűsített telepítési folyamat Azure-ra

A repó tartalmazza az összes szükséges konfigurációs fájlt, forráskódot és infrastruktúra-definíciót, hogy gyorsan elkezdhesd egy éles környezetre kész MCP szerver megvalósítását.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - MCP minta megvalósítása Azure Functions segítségével Pythonban
- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - MCP minta megvalósítása Azure Functions segítségével C# .NET-ben
- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - MCP minta megvalósítása Azure Functions segítségével Node/TypeScript-ben.

## Főbb Tanulságok

- Az MCP SDK-k nyelvspecifikus eszközöket biztosítanak robusztus MCP megoldások megvalósításához
- A hibakeresési és tesztelési folyamat kritikus a megbízható MCP alkalmazásokhoz
- Az újrahasznosítható prompt sablonok következetes AI interakciókat tesznek lehetővé
- A jól megtervezett munkafolyamatok összetett feladatokat képesek koordinálni több eszköz használatával
- Az MCP megoldások megvalósítása során figyelembe kell venni a biztonságot, a teljesítményt és a hibakezelést

## Gyakorlat

Tervezd meg egy gyakorlati MCP munkafolyamatot, amely egy valós problémát old meg a saját területeden:

1. Azonosíts 3-4 eszközt, amelyek hasznosak lennének a probléma megoldásához
2. Készíts egy munkafolyamat-diagramot, amely bemutatja, hogyan működnek együtt ezek az eszközök
3. Valósítsd meg az egyik eszköz alapverzióját a preferált nyelveden
4. Hozz létre egy prompt sablont, amely segíti a modellt az eszköz hatékony használatában

## További Források

---

Következő: [Haladó T

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.