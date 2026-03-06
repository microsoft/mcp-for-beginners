# Gyakorlati megvalósítás

[![Hogyan építsünk, teszteljünk és telepítsünk MCP alkalmazásokat valódi eszközökkel és munkafolyamatokkal](../../../translated_images/hu/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Kattints a fenti képre a lecke videójának megtekintéséhez)_

A gyakorlati megvalósítás az a pont, ahol a Model Context Protocol (MCP) ereje kézzelfoghatóvá válik. Bár fontos megérteni az MCP mögötti elméletet és architektúrát, az igazi érték akkor jelenik meg, amikor ezeket a fogalmakat alkalmazod, hogy valós problémákat megoldó megoldásokat építs, tesztelj és telepíts. Ez a fejezet áthidalja a szakadékot a fogalmi tudás és a gyakorlati fejlesztés között, és végigvezet a MCP alapú alkalmazások megvalósításának folyamatán.

Legyen szó intelligens asszisztensek fejlesztéséről, mesterséges intelligencia vállalati munkafolyamatokba integrálásáról vagy egyedi eszközök építéséről adatfeldolgozáshoz, az MCP rugalmas alapot nyújt. Nyelvfüggetlen kialakítása és a népszerű programozási nyelvek hivatalos SDK-i széles fejlesztői kör számára hozzáférhetővé teszik. Ezeknek az SDK-knak a kihasználásával gyorsan prototípuskészítés, ismétlés és skálázás végezhető különböző platformokon és környezetekben.

A következő szakaszok gyakorlati példákat, mintakódokat és telepítési stratégiákat tartalmaznak, amelyek bemutatják az MCP implementációját C#, Java Springgel, TypeScript, JavaScript és Python nyelveken. Megtanulhatod továbbá, hogyan lehet hibakeresni és tesztelni az MCP szervereket, kezelni az API-kat, valamint hogyan lehet megoldásokat telepíteni az Azure felhőjébe. Ezek a gyakorlati források felgyorsítják a tanulási folyamatot és támogatnak a megbízható, éles használatra kész MCP alkalmazások készítésében.

## Áttekintés

Ez a lecke az MCP megvalósítás gyakorlati aspektusaira fókuszál több programozási nyelven át. Megvizsgáljuk, hogyan használhatók az MCP SDK-k C#, Java Spring, TypeScript, JavaScript és Python környezetekben robosztus alkalmazások építéséhez, az MCP szerverek hibakereséséhez és teszteléséhez, valamint újrahasznosítható erőforrások, promptok és eszközök létrehozásához.

## Tanulási célok

A lecke végére képes leszel:

- MCP megoldásokat implementálni hivatalos SDK-kkal különböző programozási nyelveken
- Rendszeresen hibakeresni és tesztelni MCP szervereket
- Szerverfunkciókat létrehozni és használni (erőforrások, promptok és eszközök)
- Hatékony MCP munkafolyamatokat tervezni összetett feladatokhoz
- Optimalizálni az MCP megvalósításokat teljesítmény és megbízhatóság szempontjából

## Hivatalos SDK erőforrások

A Model Context Protocol hivatalos SDK-kkal rendelkezik több nyelven (összhangban az [MCP specifikáció 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) verzióval):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Megjegyzés:** szükséges a [Project Reactor](https://projectreactor.io) függőség. (Lásd a [246. számú vitát](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## MCP SDK-k használata

Ez a szakasz gyakorlati példákat mutat be MCP implementációra több programozási nyelven. Példakódokat találsz a `samples` könyvtárban nyelv szerint rendezve.

### Elérhető minták

A tároló [mintamegoldásokat](../../../04-PracticalImplementation/samples) tartalmaz az alábbi nyelveken:

- [C#](./samples/csharp/README.md)
- [Java Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Minden minta bemutatja az adott nyelv és ökoszisztéma MCP kulcsfogalmait és implementációs mintáit.

### Gyakorlati útmutatók

További útmutatók a gyakorlati MCP megvalósításhoz:

- [Lapozás és nagy eredményhalmazok kezelése](./pagination/README.md) – Kurzor alapú lapozás kezelése eszközöknél, erőforrásoknál és nagy adatbázisoknál

## Alapszerver funkciók

Az MCP szerverek az alábbi funkciók tetszőleges kombinációját valósíthatják meg:

### Erőforrások

Az erőforrások kontextust és adatot biztosítanak a felhasználó vagy az MI modell számára:

- Dokumentumtárak
- Tudásbázisok
- Strukturált adatok forrásai
- Fájlrendszerek

### Promptok

Promptok előre meghatározott sablonok és munkafolyamatok a felhasználóknak:

- Előre definiált beszélgetési sablonok
- Vezérelt interakciós minták
- Speciális párbeszédstruktúrák

### Eszközök

Eszközök olyan függvények, melyeket az MI modell hajt végre:

- Adatfeldolgozó segédprogramok
- Külső API integrációk
- Számítási képességek
- Keresési funkciók

## Mintapéldák: C# megvalósítás

A hivatalos C# SDK tároló több mintamegoldást tartalmaz, amelyek az MCP különböző aspektusait mutatják be:

- **Alap MCP kliens**: Egyszerű példa az MCP kliens létrehozására és eszközök hívására
- **Alap MCP szerver**: Minimális szerver implementáció alap eszközregisztrációval
- **Fejlett MCP szerver**: Teljes funkcionalitású szerver eszközregisztrációval, hitelesítéssel és hiba kezeléssel
- **ASP.NET integráció**: Példák az ASP.NET Core integrációjára
- **Eszköz megvalósítási minták**: Különböző minták eszközök megvalósításához különböző komplexitási szintekkel

Az MCP C# SDK előzetes verzióban van, az API-k változhatnak. Ez a blog folyamatosan frissül majd, ahogy az SDK fejlődik.

### Főbb jellemzők

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Az [első MCP szervered építése](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

A teljes C# implementációs mintákért látogass el a [hivatalos C# SDK minták tárolójába](https://github.com/modelcontextprotocol/csharp-sdk)

## Mintapélda: Java Spring megvalósítás

A Java Spring SDK vállalati szintű funkciókat kínál robosztus MCP megvalósításhoz.

### Főbb jellemzők

- Spring Framework integráció
- Erős típusbiztonság
- Reaktív programozás támogatás
- Átfogó hiba kezelés

A teljes Java Spring megvalósítás mintáért lásd a [Java Spring mintát](samples/java/containerapp/README.md) a minta könyvtárban.

## Mintapélda: JavaScript megvalósítás

A JavaScript SDK könnyű és rugalmas megközelítést kínál az MCP megvalósításhoz.

### Főbb jellemzők

- Node.js és böngésző támogatás
- Promise alapú API
- Egyszerű integráció Express és más keretrendszerekkel
- WebSocket támogatás streaminghez

A teljes JavaScript megvalósítás mintáért lásd a [JavaScript mintát](samples/javascript/README.md) a minta könyvtárban.

## Mintapélda: Python megvalósítás

A Python SDK pythonos megközelítést kínál az MCP megvalósításhoz, kiváló ML könyvtár integrációkkal.

### Főbb jellemzők

- Async/await támogatás asyncio-val
- FastAPI integráció
- Egyszerű eszközregisztráció
- Natív integráció a népszerű ML könyvtárakkal

A teljes Python megvalósítás mintáért lásd a [Python mintát](samples/python/README.md) a minta könyvtárban.

## API menedzsment

Az Azure API Management kitűnő megoldás az MCP szerverek biztonságossá tételére. Az ötlet, hogy egy Azure API Management példányt helyezel az MCP szervered elé, amely kezeli az olyan funkciókat, amikre valószínűleg szükséged lesz, például:

- lekérések számlálása (rate limiting)
- token kezelése
- monitorozás
- terheléselosztás
- biztonság

### Azure minta

Itt egy Azure minta, amely pontosan ezt valósítja meg, azaz [MCP szerver létrehozása és biztonságossá tétele Azure API Managementtel](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Lásd az engedélyezési folyamatot a következő képen:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

A fenti képen a következők történnek:

- Hitelesítés/engedélyezés történik a Microsoft Entra használatával.
- Az Azure API Management kapuként működik, és szabályzatokkal irányítja és kezeli a forgalmat.
- Az Azure Monitor minden kérést naplóz további elemzéshez.

#### Engedélyezési folyamat

Nézzük meg részletesebben az engedélyezési folyamatot:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP engedélyezési specifikáció

Tudj meg többet az [MCP engedélyezési specifikációról](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Távoli MCP szerver telepítése Azure-ra

Nézzük meg, hogyan telepíthetjük az előbb említett mintát:

1. Klónozd a tárolót

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Regisztráld a `Microsoft.App` erőforrás szolgáltatót.

   - Ha Azure CLI-t használsz, futtasd: `az provider register --namespace Microsoft.App --wait`.
   - Ha Azure PowerShell-t használsz, futtasd: `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Ezután várj egy kicsit, majd futtasd `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`, hogy ellenőrizd a regisztráció állapotát.

1. Futtasd ezt az [azd](https://aka.ms/azd) parancsot az API menedzsment szolgáltatás, függvényalkalmazás (kóddal) és minden egyéb szükséges Azure erőforrás előkészítéséhez

    ```shell
    azd up
    ```

    Ez a parancs telepíti az összes felhő erőforrást Azure-on

### Szerver tesztelése MCP Inspectorral

1. Egy **új terminál ablakban** telepítsd és futtasd az MCP Inspectort

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Az alábbihoz hasonló felületet kell látnod:

    ![Connect to Node inspector](../../../translated_images/hu/connect.141db0b2bd05f096.webp)

1. CTRL kattintással töltsd be az MCP Inspector webalkalmazást az alkalmazás által mutatott URL-ről (pl. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Állítsd a szállítási típust `SSE`-re
1. Állítsd be az URL-t az `azd up` után megjelenő API Menedzsment SSE végpontra, majd **Kapcsolódás**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Eszközök listázása**. Kattints egy eszközre, majd **Eszköz futtatása**.

Ha minden lépés sikeres volt, most csatlakoztál az MCP szerverhez és sikerült egy eszközt meghívnod.

## MCP szerverek Azure-hoz

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ezek a tárolók gyors kezdő sablonokat biztosítanak egyedi távoli MCP (Model Context Protocol) szerverek építéséhez és telepítéséhez Azure Functions segítségével Python, C# .NET vagy Node/TypeScript nyelveken.

A minták teljes megoldást kínálnak, amely lehetővé teszi a fejlesztők számára, hogy:

- Helyben építsenek és futtassanak: MCP szerver fejlesztése és hibakeresése helyi gépen
- Azure-ra telepítsenek: Egyszerűen telepíthető felhőbe egyetlen azd up paranccsal
- Kliensekről csatlakozzanak: Csatlakozás az MCP szerverhez különböző kliensekről, például a VS Code Copilot ügynök módjából vagy az MCP Inspector eszközzel

### Főbb jellemzők

- Biztonság tervezés szerint: Az MCP szerver kulcsokkal és HTTPS-sel biztosított
- Hitelesítési opciók: OAuth támogatás beépített autentikációval és/vagy API Menedzsmenttel
- Hálózati izoláció: Hálózati izoláció engedélyezése Azure Virtuális Hálózatok (VNET) használatával
- Serverless architektúra: Él az Azure Functions eseményvezérelt, skálázható futtatási modelljeivel
- Helyi fejlesztés: Átfogó helyi fejlesztési és hibakeresési támogatás
- Egyszerű telepítés: Egyszerűsített telepítési folyamat Azure-ra

A tároló tartalmazza az összes szükséges konfigurációs fájlt, forráskódot és infrastruktúra definíciót a gyors induláshoz és éles MCP szerver implementációhoz.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) – MCP minta megvalósítás Azure Functions és Python használatával

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – MCP minta megvalósítás Azure Functions és C# .NET használatával

- [Azure Remote MCP Functions Node/TypeScript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – MCP minta megvalósítás Azure Functions és Node/TypeScript használatával

## Főbb tanulságok

- Az MCP SDK-k nyelvspecifikus eszközöket biztosítanak robosztus MCP megoldások implementálásához
- A hibakeresés és tesztelés kritikus a megbízható MCP alkalmazásokhoz
- Az újrahasznosítható prompt sablonok biztosítják az AI konzisztens interakcióit
- Jól megtervezett munkafolyamatok összetett feladatokat képesek vezényelni több eszköz használatával
- MCP megoldások implementálásakor figyelembe kell venni a biztonságot, a teljesítményt és a hibakezelést

## Gyakorlat

Tervezzen egy gyakorlati MCP munkafolyamatot, amely a szakmai területén egy valós problémát old meg:

1. Határozz meg 3-4 olyan eszközt, amelyek hasznosak lennének a probléma megoldásához
2. Készíts munkafolyamat ábrát, amely megmutatja, hogyan lépnek kölcsönhatásba ezek az eszközök
3. Valósíts meg egy alap verziót az egyik eszközből a preferált programnyelveden
4. Készíts egy prompt sablont, amely segíti a modellt az eszköz hatékony használatában

## További források

---

## Mi jön ezután

Következő: [Haladó témakörök](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:
Ezt a dokumentumot az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvű dokumentum tekinthető hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást ajánlunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->