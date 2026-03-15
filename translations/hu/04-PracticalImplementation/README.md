# Gyakorlati megvalósítás

[![Hogyan építsünk, teszteljünk és telepítsünk MCP alkalmazásokat valós eszközökkel és munkafolyamatokkal](../../../translated_images/hu/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Kattints a fenti képre a lecke videójának megtekintéséhez)_

A gyakorlati megvalósítás az, ahol a Model Context Protocol (MCP) ereje kézzelfoghatóvá válik. Bár fontos megérteni az MCP mögötti elméletet és architektúrát, az igazi érték akkor születik, amikor ezeket a koncepciókat alkalmazod megoldások építésére, tesztelésére és telepítésére, amelyek valós problémákat oldanak meg. Ez a fejezet hidat képez a fogalmi tudás és a gyakorlati fejlesztés között, útmutatást nyújtva az MCP alapú alkalmazások megvalósításának folyamatához.

Akár intelligens asszisztenseket fejlesztesz, AI-t integrálsz üzleti munkafolyamatokba, vagy egyedi eszközöket építesz adatfeldolgozáshoz, az MCP rugalmas alapot nyújt. Nyelvfüggetlen tervezése és a népszerű programozási nyelvekhez elérhető hivatalos SDK-k széles fejlesztői kör számára hozzáférhetővé teszik. Ezeknek az SDK-knak a kihasználásával gyorsan prototípust készíthetsz, iterálhatsz és skálázhatod megoldásaidat különböző platformokon és környezetekben.

A következő szakaszok gyakorlati példákat, mintakódokat és telepítési stratégiákat mutatnak be, amelyek demonstrálják az MCP megvalósítását C#, Java Spring, TypeScript, JavaScript és Python nyelveken. Megtanulhatod azt is, hogyan lehet hibakeresni és tesztelni az MCP szervereket, menedzselni az API-kat, és megoldásokat felhőbe telepíteni Azure használatával. Ezek a gyakorlati erőforrások arra szolgálnak, hogy felgyorsítsák a tanulásodat és magabiztosan építhess megbízható, éles használatra kész MCP alkalmazásokat.

## Áttekintés

Ez a lecke az MCP megvalósítás gyakorlati aspektusaira fókuszál több programozási nyelven keresztül. Megvizsgáljuk, hogyan használhatók az MCP SDK-k C#, Java Spring, TypeScript, JavaScript és Python nyelveken stabil alkalmazások építésére, MCP szerverek hibakeresésére és tesztelésére, valamint újrahasznosítható erőforrások, promptok és eszközök készítésére.

## Tanulási célok

A lecke végére képes leszel:

- MCP megoldásokat megvalósítani hivatalos SDK-k használatával különböző programozási nyelveken
- Rendszeresen hibakeresni és tesztelni MCP szervereket
- Szerverfunkciókat (Erőforrások, Promptonk, Eszközök) létrehozni és használni
- Hatékony MCP munkafolyamatokat tervezni összetett feladatokhoz
- Optimalizálni az MCP megvalósításokat teljesítményre és megbízhatóságra

## Hivatalos SDK erőforrások

A Model Context Protocol több nyelvhez kínál hivatalos SDK-kat (összhangban az [MCP Specifikáció 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) verzióval):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Megjegyzés:** a Project Reactor függőség szükséges ([https://projectreactor.io](https://projectreactor.io)). (Lásd [vitadokumentum 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## MCP SDK-k használata

Ez a szakasz gyakorlati példákat nyújt MCP megvalósításra több programozási nyelven keresztül. Mintakódokat a `samples` könyvtárban találhatsz, nyelv szerint rendezve.

### Elérhető minták

A tárház tartalmaz [mintaimplementációkat](../../../04-PracticalImplementation/samples) a következő nyelveken:

- [C#](./samples/csharp/README.md)
- [Java Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Minden minta bemutatja az adott nyelv és ökoszisztéma MCP kulcsfogalmait és megvalósítási mintáit.

### Gyakorlati útmutatók

További útmutatók a gyakorlati MCP megvalósításhoz:

- [Lapozás és nagy eredményhalmazok kezelése](./pagination/README.md) - Kurszor-alapú lapozás kezelése eszközökhöz, erőforrásokhoz és nagy adatkészletekhez

## Alapszerver funkciók

Az MCP szerverek bármilyen kombinációját megvalósíthatják az alábbi funkcióknak:

### Erőforrások

Az erőforrások kontextust és adatokat szolgáltatnak a felhasználó vagy AI modell számára:

- Dokumentumtárak
- Tudásbázisok
- Strukturált adatforrások
- Fájlrendszerek

### Promptonk

A promptok sablonos üzenetek és munkafolyamatok a felhasználók számára:

- Előre definiált beszélgetési sablonok
- Vezérelt interakciós minták
- Specializált párbeszéd struktúrák

### Eszközök

Az eszközök olyan függvények, amelyeket az AI modell futtat:

- Adatfeldolgozó segédprogramok
- Külső API integrációk
- Számítási képességek
- Keresési funkciók

## Mintaimplementációk: C# megvalósítás

A hivatalos C# SDK tárház számos példa implementációt tartalmaz, amelyek az MCP különböző aspektusait demonstrálják:

- **Alap MCP kliens**: Egyszerű példa arra, hogyan kell létrehozni egy MCP klienst és meghívni eszközöket
- **Alap MCP szerver**: Minimális szerver megvalósítás alapvető eszközregisztrációval
- **Haladó MCP szerver**: Teljes funkcionalitású szerver eszközregisztrációval, hitelesítéssel és hibakezeléssel
- **ASP.NET integráció**: Példák az ASP.NET Core integrációjára
- **Eszközmegvalósítási minták**: Különböző minták eszközök implementálására különböző komplexitási szinteken

Az MCP C# SDK jelenleg előnézeti (preview) állapotban van, és az API-k változhatnak. Folyamatosan frissítjük ezt a blogot az SDK fejlődésével.

### Kulcsfunkciók

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Az [első MCP szervered építése](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Teljes C# minta megvalósításokért látogasd meg a [hivatalos C# SDK mintatárat](https://github.com/modelcontextprotocol/csharp-sdk)

## Minta megvalósítás: Java Spring megvalósítás

A Java Spring SDK robosztus MCP megvalósítási lehetőségeket kínál vállalati szintű funkciókkal.

### Kulcsfunkciók

- Spring Framework integráció
- Erős típusbiztonság
- Reaktív programozás támogatása
- Átfogó hibakezelés

Teljes Java Spring mintaért lásd a [Java Spring mintát](samples/java/containerapp/README.md) a mintakönyvtárban.

## Minta megvalósítás: JavaScript megvalósítás

A JavaScript SDK könnyű és rugalmas megközelítést nyújt az MCP megvalósításhoz.

### Kulcsfunkciók

- Node.js és böngésző támogatás
- Promise-alapú API
- Egyszerű integráció Express és más keretrendszerekkel
- WebSocket streaming támogatás

Teljes JavaScript megvalósítási minta a [JavaScript mintában](samples/javascript/README.md) található a minták között.

## Minta megvalósítás: Python megvalósítás

A Python SDK Pythonos megközelítést kínál az MCP megvalósításhoz kitűnő ML keretrendszer integrációkkal.

### Kulcsfunkciók

- Async/await támogatás asyncio-val
- FastAPI integráció
- Egyszerű eszközregisztráció
- Natív integráció népszerű ML könyvtárakkal

Teljes Python megvalósítási minta a [Python mintában](samples/python/README.md) található a minták között.

## API menedzsment

Az Azure API Management nagyszerű megoldás arra, hogyan tudjuk biztonságossá tenni az MCP szervereket. Az ötlet, hogy egy Azure API Management példányt helyezünk az MCP szerver elé, és hagyjuk, hogy kezelje az olyan funkciókat, amikre szükséged lehet:

- sebességkorlát beállítása
- token menedzsment
- monitorozás
- terheléselosztás
- biztonság

### Azure minta

Itt egy Azure minta, ami pontosan ezt valósítja meg, azaz [MCP szerver létrehozása és Azure API Managementtel való védelme](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Nézd meg az engedélyezési folyamatot az alábbi képen:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

A fenti képen a következők történnek:

- Hitelesítés/Engedélyezés Microsoft Entra segítségével zajlik.
- Az Azure API Management átjáróként működik, és szabályzatokkal irányítja és kezeli a forgalmat.
- Az Azure Monitor naplózza az összes kérést további elemzésre.

#### Engedélyezési folyamat

Nézzük meg az engedélyezési folyamatot részletesebben:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP engedélyezési specifikáció

További információk az [MCP engedélyezési specifikációról](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Távoli MCP szerver Azure-ba telepítése

Nézzük meg, hogyan telepíthetjük a fent említett mintát:

1. Klónozd a tárolót

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Regisztráld a `Microsoft.App` erőforrás szolgáltatót.

   - Ha Azure CLI-t használsz, futtasd az `az provider register --namespace Microsoft.App --wait` parancsot.
   - Ha Azure PowerShell-t használsz, futtasd a `Register-AzResourceProvider -ProviderNamespace Microsoft.App` parancsot. Ezután egy idő múlva ellenőrizd a `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` lefuttatásával, hogy a regisztráció befejeződött-e.

1. Futtasd ezt az [azd](https://aka.ms/azd) parancsot az API menedzsment szolgáltatás, a funkcióalkalmazás (kóddal) és az összes többi szükséges Azure erőforrás létrehozásához

    ```shell
    azd up
    ```

    Ez a parancs telepíti az összes felhő erőforrást az Azure-ra

### Szerver tesztelése MCP Inspectorral

1. Egy **új terminálablakban** telepítsd és futtasd az MCP Inspectort

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Egy hasonló felület fog megjelenni:

    ![Connect to Node inspector](../../../translated_images/hu/connect.141db0b2bd05f096.webp)

1. CTRL kattintással töltsd be az MCP Inspector webalkalmazást a megjelenített URL-ről (pl. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Állítsd a szállítási típust `SSE`-re
1. Állítsd be az URL-t a futó API Menedzsment SSE végpontjára, amely az `azd up` parancs után jelenik meg, majd **Kapcsolódás**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Eszközök listázása**. Kattints egy eszközre és **Eszköz futtatása**.  

Ha minden lépés sikeresen végződött, most csatlakoztál az MCP szerverhez és sikerült meghívnod egy eszközt.

## MCP szerverek Azure-hoz

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ezek a tárak gyorsindító sablonok egyedi távoli MCP (Model Context Protocol) szerverek építéséhez és telepítéséhez Azure Functions segítségével Python, C# .NET vagy Node/TypeScript nyelveken.

A minták teljes megoldást nyújtanak, lehetővé téve a fejlesztőknek, hogy:

- Helyileg építsenek és futtassanak: MCP szerver fejlesztése és hibakeresése helyi gépen
- Telepítsenek Azure-ba: Egyszerűen telepítsenek a felhőbe egyetlen azd up paranccsal
- Kliensről kapcsolódjanak: Csatlakozzanak az MCP szerverhez különböző kliensekről, például a VS Code Copilot ügynök módból és az MCP Inspector eszközzel

### Kulcsfunkciók

- Biztonság tervezésből: az MCP szerver kulcsokkal és HTTPS használatával védett
- Hitelesítési lehetőségek: OAuth támogatás beépített hitelesítéssel és/vagy API Managementtel
- Hálózati izoláció: lehetőség hálózati elkülönítésre Azure Virtual Networks (VNET) használatával
- Serverless architektúra: skalázható, eseményvezérelt végrehajtás Azure Functions segítségével
- Helyi fejlesztés: átfogó helyi fejlesztési és hibakeresési támogatás
- Egyszerű telepítés: egyszerűsített telepítési folyamat Azure-ra

A tár tartalmaz minden szükséges konfigurációs fájlt, forráskódot és infrastruktúra definíciót a gyors induláshoz egy éles használatra kész MCP szerver megvalósításhoz.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - MCP minta megvalósítás Azure Functions Python-nal

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - MCP minta megvalósítás Azure Functions C# .NET nyelven

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - MCP minta megvalósítás Azure Functions Node/TypeScript nyelven.

## Főbb tanulságok

- Az MCP SDK-k nyelvspecifikus eszközöket nyújtanak robosztus MCP megoldásokhoz
- A hibakeresési és tesztelési folyamat kritikus a megbízható MCP alkalmazásokhoz
- Az újrahasználható prompt sablonok következetes AI interakciókat tesznek lehetővé
- A jól megtervezett munkafolyamatok képesek összetett feladatokat megszervezni több eszköz használatával
- MCP megoldások megvalósítása során figyelembe kell venni a biztonságot, teljesítményt és hibakezelést

## Gyakorlat

Tervezd meg egy gyakorlati MCP munkafolyamatot, amely valós problémát old meg az adott területedhez:

1. Azonosíts 3-4 eszközt, amelyek hasznosak lennének a probléma megoldásához
2. Készíts munkafolyamat diagramot, amely bemutatja, hogyan lépnek kapcsolatba ezek az eszközök
3. Készíts el egy egyszerű verziót az egyik eszközből a preferált nyelveden
4. Készíts egy prompt sablont, amely segítené a modellt az eszköz hatékony használatában

## További erőforrások

---

## Mi következik

Következő: [Haladó témák](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->