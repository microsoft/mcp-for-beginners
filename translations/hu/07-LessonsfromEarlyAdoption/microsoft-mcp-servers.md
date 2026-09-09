# 🚀 10 Microsoft MCP szerver, amely átalakítja a fejlesztők termelékenységét

## 🎯 Amit ebben az útmutatóban megtanulsz

Ez a gyakorlati útmutató tíz Microsoft MCP szervert mutat be, amelyek aktívan átalakítják, hogyan dolgoznak a fejlesztők az AI asszisztensekkel. Nemcsak azt magyarázzuk el, hogy az MCP szerverek *mit tudnak*, hanem bemutatjuk azokat a szervereket, amelyek már valódi változást hoznak a mindennapi fejlesztési munkafolyamatokban a Microsoftnál és azon túl.

Az útmutatóban szereplő szervereket a valós használat és fejlesztői visszajelzések alapján választottuk ki. Nemcsak azt fogod megtudni, hogy az egyes szerverek mit csinálnak, hanem azt is, hogy miért fontosak, és hogyan hozhatod ki belőlük a legtöbbet a saját projektjeidben. Akár teljesen új vagy az MCP-ben, akár bővíteni szeretnéd meglévő rendszereidet, ezek a szerverek a Microsoft ökoszisztéma leggyakorlatiasabb és legnagyobb hatású eszközeit képviselik.

> **💡 Gyors kezdő tipp**
> 
> Új vagy az MCP-ben? Ne aggódj! Ez az útmutató kezdők számára készült. Ahogy haladunk, elmagyarázzuk a fogalmakat, és bármikor visszatérhetsz a [Bevezetés az MCP-be](../00-Introduction/README.md) és az [Alapfogalmak](../01-CoreConcepts/README.md) modulokhoz mélyebb háttéranyagért.

## Áttekintés

Ez az átfogó útmutató tíz Microsoft MCP szervert vizsgál meg, amelyek forradalmasítják a fejlesztők AI asszisztensekkel és külső eszközökkel való interakcióját. Az Azure erőforráskezeléstől a dokumentumfeldolgozásig ezek a szerverek bemutatják, hogyan használható a Model Context Protocol a zökkenőmentes, hatékony fejlesztési munkafolyamatok létrehozására.

## Tanulási célok

Az útmutató végére:
- Megérted, hogyan növelik az MCP szerverek a fejlesztők termelékenységét
- Megismerkedsz a Microsoft legbefolyásosabb MCP szerver implementációival
- Gyakorlati felhasználási eseteket ismersz meg az egyes szerverekhez
- Tudni fogod, hogyan állítsd be és konfiguráld ezeket a szervereket VS Code-ban és Visual Studio-ban
- Felfedezed a szélesebb MCP ökoszisztémát és a jövőbeli irányokat

## 🔧 Az MCP szerverek megértése: kezdők útmutatója

### Mik azok az MCP szerverek?

Ha kezdő vagy a Model Context Protocol (MCP) terén, talán azt kérdezed: "Mi az az MCP szerver pontosan, és miért fontos ez nekem?" Kezdjük egy egyszerű hasonlattal.

Gondolj az MCP szerverekre úgy, mint speciális asszisztensekre, amelyek segítik az AI kódoló társadat (például a GitHub Copilotot), hogy kapcsolódni tudjon külső eszközökhöz és szolgáltatásokhoz. Ahogy különböző alkalmazásokat használsz a telefonodon különböző feladatokra – egyik az időjárásra, másik a navigációra, harmadik a bankolásra – úgy az MCP szerverek lehetővé teszik, hogy az AI asszisztensed különféle fejlesztői eszközökkel és szolgáltatásokkal kommunikáljon.

### Az MCP szerverek által megoldott probléma

Az MCP szerverek előtt, ha azt szeretted volna:
- Ellenőrizni az Azure erőforrásaidat
- GitHub hibajegyet létrehozni
- Lekérdezni az adatbázisodat
- Dokumentációt keresni

Ne kellett volna abbahagynod a kódolást, megnyitnod egy böngészőt, meglátogatnod a megfelelő weboldalt, és manuálisan elvégezni ezeket a feladatokat. Ez a folyamatos kontextusváltás megszakítja a munkafolyamatodat és csökkenti a termelékenységet.

### Hogyan alakítják át az MCP szerverek a fejlesztési élményt

Az MCP szerverek segítségével a fejlesztői környezetedben (VS Code, Visual Studio stb.) maradhatsz, és egyszerűen kérheted az AI asszisztensedet, hogy végezze el ezeket a feladatokat. Például:

**A hagyományos munkafolyamat helyett:**
1. Kódolás megállítása
2. Böngésző megnyitása
3. Azure portálra navigálás
4. Tárolófiók adatok lekérése
5. Visszatérés a VS Code-ba
6. Kódolás folytatása

**Mostantól ezt teheted:**
1. Megkérdezed az AI-t: "Mi az állapota az Azure tárolófiókjaimnak?"
2. A kapott információkkal folytatod a kódolást

### Fő előnyök kezdők számára

#### 1. 🔄 **Maradj a flow állapotban**
- Ne kelljen több alkalmazás között váltogatni
- Tartsd fókuszodat a kód írásán
- Csökkentsd azoknak az eszközöknek a mentális terhét a kezelésében, amelyekkel dolgozol

#### 2. 🤖 **Használj természetes nyelvet a bonyolult parancsok helyett**
- Ahelyett, hogy SQL szintaxist jegyeznél meg, írd le, milyen adatokat szeretnél
- Ahelyett, hogy az Azure CLI parancsokat tanulnád meg, magyarázd el, mit akarsz elérni
- Hagyd, hogy az AI kezelje a technikai részleteket, miközben te a logikára koncentrálsz

#### 3. 🔗 **Kapcsolj össze több eszközt**
- Hozz létre erős munkafolyamatokat különböző szolgáltatások kombinálásával
- Példa: "Szerezd meg az összes legutóbbi GitHub hibajegyet, és hozz létre hozzájuk tartozó Azure DevOps munkatételeket"
- Építs automatizációt bonyolult szkriptek írása nélkül

#### 4. 🌐 **Hozzáférés egy növekvő ökoszisztémához**
- Használj Microsoft, GitHub és más cégek által fejlesztett szervereket
- Különböző szállítók eszközeit zökkenőmentesen kombináld
- Csatlakozz egy szabványosított ökoszisztémához, amely különféle AI asszisztensekkel működik

#### 5. 🛠️ **Tanulj a gyakorlatból**
- Kezdj előre elkészített szerverekkel az alapok megértéséhez
- Fokozatosan építsd fel saját szervereidet, ahogy egyre magabiztosabb leszel
- Használd a rendelkezésre álló SDK-kat és dokumentációkat, hogy vezessenek a tanulásban

### Valós példa kezdőknek

Tegyük fel, hogy új vagy a webfejlesztésben, és az első projekteden dolgozol. Így segíthetnek az MCP szerverek:

**Hagyományos megközelítés:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP szerverekkel:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Az üzleti szabvány előnye

Az MCP iparági szabvánnyá válik, ami azt jelenti:
- **Következetesség**: hasonló élmény különböző eszközök és cégek között
- **Interoperabilitás**: különböző szállítók szerverei együttműködnek
- **Jövőbiztosság**: a készségek és beállítások átválthatók különböző AI asszisztensek között
- **Közösség**: nagy ökoszisztéma megosztott tudással és erőforrásokkal

### Kezdés: Amit megtanulsz

Ebben az útmutatóban tíz Microsoft MCP szervert vizsgálunk meg, amelyek különösen hasznosak minden szintű fejlesztő számára. Minden szerver tervezték arra, hogy:
- Megoldja a gyakori fejlesztési kihívásokat
- Csökkentse az ismétlődő feladatokat
- Javítsa a kód minőségét
- Növelje a tanulási lehetőségeket

> **💡 Tanulási tipp**
> 
> Ha teljesen új vagy az MCP-ben, először kezd a [Bevezetés az MCP-be](../00-Introduction/README.md) és [Alapfogalmak](../01-CoreConcepts/README.md) modulokkal. Ezután térj vissza ide, hogy lásd ezeknek a fogalmaknak a gyakorlati megvalósítását valós Microsoft eszközökkel.
>
> Az MCP fontosságával kapcsolatos további háttérért olvasd el Maria Naggaga cikkét: [Csatlakozz egyszer, integrálódj bárhol az MCP-vel](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Az MCP használatának megkezdése VS Code-ban és Visual Studio-ban 🚀

Ezeknek az MCP szervereknek a beállítása egyszerű, ha Visual Studio Code-ot vagy Visual Studio 2022-t használsz GitHub Copilottal.

### VS Code beállítás

Itt van az alapvető folyamat VS Code-hoz:

1. **Agent mód engedélyezése**: A VS Code-ban válts Agent módra a Copilot Chat ablakban
2. **MCP szerverek konfigurációja**: Add hozzá a szerverkonfigurációkat a settings.json fájlodhoz
3. **Szerverek indítása**: Kattints az „Indítás” gombra minden használni kívánt szervernél
4. **Eszközök kiválasztása**: Válaszd ki, mely MCP szervereket engedélyezed az aktuális munkamenetben

Részletes beállítási útmutatóért lásd a [VS Code MCP dokumentációját](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profi tipp: Kezeld az MCP szervereket profiként!**
> 
> A VS Code Extensions nézet most egy [kényelmes új felhasználói felületet tartalmaz az MCP szerverek kezeléséhez](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Gyors hozzáférést kapsz az MCP szerverek indításához, leállításához és kezeléséhez tiszta, egyszerű felületen. Próbáld ki!

### Visual Studio 2022 beállítás

Visual Studio 2022 (17.14-es vagy újabb verzió) esetén:

1. **Agent mód engedélyezése**: Kattints az „Ask” legördülő menüre a GitHub Copilot Chat ablakban, és válaszd az „Agent” opciót
2. **Konfigurációs fájl létrehozása**: Hozz létre egy `.mcp.json` fájlt a megoldásod könyvtárában (ajánlott hely: `<SOLUTIONDIR>\.mcp.json`)
3. **Szerverek konfigurálása**: Add hozzá MCP szerver konfigurációidat a szabványos MCP formátum szerint
4. **Eszközjóváhagyás**: Amikor kéri, hagyd jóvá a használni kívánt eszközöket a megfelelő jogosultsági tartományokkal

Részletes Visual Studio beállítási útmutatóért lásd a [Visual Studio MCP dokumentációját](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Minden MCP szerver saját konfigurációs igényekkel rendelkezik (kapcsolati karakterláncok, hitelesítés stb.), de a beállítási minta mindkét IDE-ben következetes.

## Tanulságok a Microsoft MCP szerverekből 🛠️

### 1. 📚 Microsoft Learn Docs MCP szerver

[![Telepítés VS Code-ban](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Telepítés VS Code Insiders-ben](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mit csinál**: A Microsoft Learn Docs MCP szerver egy felhőalapú szolgáltatás, amely valós idejű hozzáférést biztosít az AI asszisztensek számára a hivatalos Microsoft dokumentációkhoz a Model Context Protocolon keresztül. Csatlakozik a `https://learn.microsoft.com/api/mcp` címhez, és szemantikus keresést tesz lehetővé a Microsoft Learn, az Azure dokumentáció, a Microsoft 365 dokumentáció és egyéb hivatalos Microsoft források között.

**Miért hasznos**: Bár elsőre "csak dokumentációnak" tűnhet, ez a szerver valójában kulcsfontosságú minden Microsoft technológiát használó fejlesztő számára. Az egyik legnagyobb panasz a .NET fejlesztők részéről az AI kódoló asszisztensekkel kapcsolatban az, hogy nem naprakészek a legújabb .NET és C# kiadásokkal. A Microsoft Learn Docs MCP szerver ezt oldja meg azzal, hogy valós idejű hozzáférést biztosít a legfrissebb dokumentációkhoz, API hivatkozásokhoz és bevált gyakorlatokhoz. Legyen szó a legújabb Azure SDK-król, a C# 13 új funkcióiról vagy a legmodernebb Aspire minták alkalmazásáról, ez a szerver biztosítja, hogy az AI asszisztensed hozzáférjen a hiteles, naprakész információkhoz a pontos, modern kód generálásához.

**Valós használat**: „Melyek az az cli parancsok egy Azure konténeralkalmazás létrehozásához a hivatalos Microsoft Learn dokumentáció szerint?” vagy „Hogyan konfiguráljam az Entity Frameworköt függőséginjektálással ASP.NET Core-ban?” Vagy például „Ellenőrizd ezt a kódot, hogy megfelel-e a Microsoft Learn dokumentációban szereplő teljesítményre vonatkozó ajánlásoknak.” A szerver átfogó lefedettséget nyújt a Microsoft Learn, az Azure dokumentáció és a Microsoft 365 dokumentáció területén, fejlett szemantikus keresést használva a leginkább kontextusban releváns információk megtalálásához. Legfeljebb 10 magas minőségű tartalmi részt ad vissza cikkcímekkel és URL-ekkel, mindig a legfrissebb Microsoft dokumentációt elérve az aktuális publikálás szerint.

**Kiemelt példa**: A szerver elérhetővé teszi a `microsoft_docs_search` eszközt, amely szemantikus keresést végez a Microsoft hivatalos technikai dokumentációjában. Miután beállítottad, kérhetsz például olyan kérdéseket, hogy „Hogyan valósítsam meg a JWT hitelesítést ASP.NET Core-ban?” és részletes, hivatalos válaszokat kapsz forráshivatkozásokkal. A keresés minősége kiváló, mert érti a kontextust – az „konténerek” kifejezés Azure kontextusban az Azure Container Instances dokumentációját hozza vissza, míg ugyanaz a kifejezés .NET kontextusban releváns C# gyűjteményekkel kapcsolatos információkat ad.

Ez különösen hasznos a gyorsan változó vagy nemrég frissült könyvtárak és használati esetek esetén. Például egy nemrégiben végzett kódolási projektem során az Aspire és a Microsoft.Extensions.AI legújabb kiadásainak funkcióit szerettem volna kihasználni. A Microsoft Learn Docs MCP szerver bevonásával nem csak az API dokumentációkat, hanem a nemrég megjelent útmutatókat és iránymutatásokat is használni tudtam.

> **💡 Profi tipp**
> 
> A még eszközbarátabb modelleket is bíztatni kell az MCP eszközök használatára! Fontold meg egy rendszerüzenet vagy a [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) hozzáadását, például: "Hozzáférésed van a `microsoft.docs.mcp` eszközhöz – használd ezt a kereséshez a Microsoft legfrissebb hivatalos dokumentációjában, amikor Microsoft technológiákról kérdeznek, mint a C#, Azure, ASP.NET Core vagy Entity Framework."
>
> Ennek nagyszerű példája megtalálható a [C# .NET Janitor chat mód](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) repóban az Awesome GitHub Copilot gyűjteményben. Ez az üzemmód kifejezetten a Microsoft Learn Docs MCP szervert használja, hogy segítsen megtisztítani és modernizálni a C# kódot a legújabb minták és bevált gyakorlatok szerint.
### 2. ☁️ Azure MCP szerver


[![Telepítés VS Code-ban](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Telepítés VS Code Insiders-ben](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mit csinál**: Az Azure MCP Server egy átfogó csomag több mint 15 speciális Azure szolgáltatás csatlakozóval, amely az egész Azure ökoszisztémát beemeli az AI munkafolyamatodba. Ez nem egy egyszerű szerver – ez egy erőteljes gyűjtemény, amely magában foglalja az erőforrás-kezelést, adatbázis csatlakozást (PostgreSQL, SQL Server), Azure Monitor naplóelemzést KQL-lel, Cosmos DB integrációt és még sok mást.

**Miért hasznos**: Az Azure erőforrások kezelésén túl ez a szerver drámaian javítja a kód minőségét, amikor Azure SDK-kkal dolgozol. Amikor az Azure MCP-t Agent módban használod, nem csak segít kódot írni – segít *jobb* Azure kódot írni, amely követi a jelenlegi hitelesítési mintákat, a hibakezelés legjobb gyakorlatait, és kihasználja az SDK legújabb funkcióit. Ahelyett, hogy általános, működő kódot kapnál, olyan kódot kapsz, amely az Azure ajánlott mintáit követi a termelési terhelésekhez.

**Fő modulok közé tartozik**:
- **🗄️ Adatbázis csatlakozók**: Közvetlen természetes nyelvű hozzáférés az Azure Database for PostgreSQL és SQL Server adatbázisokhoz
- **📊 Azure Monitor**: KQL-alapú naplóelemzés és működési betekintések
- **🌐 Erőforrás-kezelés**: Teljes Azure erőforrás életciklus-kezelés
- **🔐 Hitelesítés**: DefaultAzureCredential és kezelt identitás minták
- **📦 Tárolási szolgáltatások**: Blob Storage, Queue Storage és Table Storage műveletek
- **🚀 Konténer szolgáltatások**: Azure Container Apps, Container Instances és AKS kezelés
- **És sok más speciális csatlakozó**

**Valós használat**: „Sorold fel az Azure tárolási fiókjaimat”, „Kérdezd le a Log Analytics munkaterületem hibáit az elmúlt órában”, vagy „Segíts egy Azure alkalmazás építésében Node.js használatával megfelelő hitelesítéssel”

**Teljes demó forgatókönyv**: Íme egy teljes áttekintés, amely bemutatja az Azure MCP és a GitHub Copilot for Azure bővítmény kombinálásának erejét VS Code-ban. Amikor mindkettő telepítve van és megadod az alábbi promptot:

> "Készíts egy Python szkriptet, amely fájlt tölt fel az Azure Blob Storage-ba a DefaultAzureCredential hitelesítés használatával. A szkript kapcsolódjon a 'mycompanystorage' nevű Azure tárolási fiókomhoz, töltsön fel egy 'documents' nevű konténerbe, hozzon létre egy tesztfájlt az aktuális időbélyeggel az feltöltéshez, kezelje a hibákat elegánsan és nyújtson tájékoztató kimenetet, kövesse az Azure legjobb gyakorlatait a hitelesítés és hibakezelés terén, tartalmazzon megjegyzéseket a DefaultAzureCredential hitelesítés működéséről, és legyen jól strukturált megfelelő funkciókkal és dokumentációval."

Az Azure MCP Server generál egy teljes, termelésre kész Python szkriptet, amely:
- Az Azure Blob Storage legújabb SDK-ját használja helyes async mintákkal
- Megvalósítja a DefaultAzureCredential-t átfogó visszaesési lánc magyarázattal
- Robusztus hibakezelést tartalmaz specifikus Azure hibakezelési típusokkal
- Az Azure SDK legjobb gyakorlatait követi az erőforrás-kezelés és kapcsolatkezelés terén
- Részletes naplózást és informatív konzol kimenetet biztosít
- Megfelelően strukturált szkriptet hoz létre funkciókkal, dokumentációval és típusjelzésekkel

Ami különlegessé teszi, hogy az Azure MCP nélkül csak egy általános blob storage kódot kaphatnál, ami működik, de nem követi a jelenlegi Azure mintákat. Az Azure MCP-vel olyan kódot kapsz, amely a legújabb hitelesítési módszereket használja, kezeli az Azure-specifikus hibaszituációkat, és követi a Microsoft által javasolt termelési alkalmazási gyakorlatokat.

**Kiemelt példa**: Nekem nehéz volt mindig emlékezni az `az` és `azd` CLI specifikus parancsaira ad-hoc használat esetén. Ez nekem mindig egy kétszakaszos folyamat: először utána kell keresni a szintaxisnak, majd lefuttatni a parancsot. Gyakran egyszerűen csak beugrok a portálra és ott kattintgatom, mert nem akarom bevallani, hogy nem emlékszem a CLI szintaxisra. Az, hogy csak le tudom írni, mit akarok, csodálatos, és még jobb, ha ezt az IDE-emből sem kell elhagynom!

Van egy nagyszerű lista a [Azure MCP tárolóban](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server), amely segít elindulni. Átfogó beállítási útmutatókért és fejlett konfigurációs lehetőségekért nézd meg a [hivatalos Azure MCP dokumentációt](https://learn.microsoft.com/azure/developer/azure-mcp-server/)!

### 3. 🐙 GitHub MCP Server

[![Telepítés VS Code-ban](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Telepítés VS Code Insiders-ben](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mit csinál**: A hivatalos GitHub MCP Server zökkenőmentes integrációt biztosít a GitHub teljes ökoszisztémájával, mind hosztolt távoli elérés, mind helyi Docker telepítési lehetőségekkel. Ez nem csupán alapvető tároló műveletekről szól – egy átfogó eszköztárat kínál, beleértve a GitHub Actions menedzsmentet, pull request munkafolyamatokat, probléma követést, biztonsági vizsgálatot, értesítéseket és fejlett automatizációs képességeket.

**Miért hasznos**: Ez a szerver átalakítja, hogyan lépsz kapcsolatba a GitHub-bal azzal, hogy a teljes platform élményét közvetlenül a fejlesztési környezetedbe hozza. Ahelyett, hogy folyton váltogatnál a VS Code és a GitHub.com között projektmenedzsmenthez, kódáttekintéshez és CI/CD megfigyeléshez, mindent természetes nyelvű parancsokkal kezelhetsz, miközben a kódodra koncentrálsz.

> **ℹ️ Megjegyzés: Különböző 'Agent' típusok**
> 
> Ne keverd össze ezt a GitHub MCP Servert a GitHub Kodoló Agentjével (azzal az AI agente-vel, amelyhez meghatározhatsz feladatokat automatikus kódoláshoz). A GitHub MCP Server a VS Code Agent módban működik a GitHub API integráció érdekében, míg a GitHub Kodoló Agent egy külön funkció, amely pull requesteket hoz létre, amikor GitHub issue-khoz van rendelve.

**Fő képességek közé tartozik**:
- **⚙️ GitHub Actions**: Teljes CI/CD pipeline menedzsment, munkafolyamat megfigyelés és artefakt kezelés
- **🔀 Pull Requestek**: PR-k létrehozása, átnézése, egyesítése és kezelése átfogó állapotkövetéssel
- **🐛 Problémák**: Teljes probléma életciklus kezelés, kommentelés, címkézés és hozzárendelés
- **🔒 Biztonság**: Kód szkennelési figyelmeztetések, titok észlelés, valamint Dependabot integráció
- **🔔 Értesítések**: Intelligens értesítés-kezelés és tároló feliratkozás vezérlés
- **📁 Tárolókezelés**: Fájlműveletek, ágkezelés és tárolóadminisztráció
- **👥 Együttműködés**: Felhasználó- és szervezetkeresés, csapatkezelés és hozzáférés vezérlés

**Valós használat**: „Hozz létre egy pull requestet a feature ágamból”, „Mutasd meg az összes sikertelen CI futást ezen a héten”, „Sorold fel a nyitott biztonsági figyelmeztetéseket a tárolóimban”, vagy „Keress meg minden rám kiosztott problémát a szervezeteimben”

**Teljes demó forgatókönyv**: Íme egy hatékony munkafolyamat, amely bemutatja a GitHub MCP Server képességeit:

> "El kell készülnöm a sprint értékelésünkre. Mutasd meg az összes pull requestet, amit ezen a héten készítettem, ellenőrizd a CI/CD pipeline-ok állapotát, készíts egy összefoglalót a megoldandó biztonsági figyelmeztetésekről, és segíts megírni a kiadási megjegyzéseket a 'feature' címkével ellátott egyesített PR-ek alapján."

A GitHub MCP Server:
- Lekérdezi a legutóbbi pull requesteket részletes állapotinformációkkal
- Elemezi a munkafolyamat futásokat és kiemeli az esetleges hibákat vagy teljesítmény problémákat
- Összeállítja a biztonsági szkennelési eredményeket és priorizálja a kritikus figyelmeztetéseket
- Átfogó kiadási megjegyzéseket generál az egyesített PR-ek adatai alapján
- Cselekvési javaslatokat biztosít a sprint tervezéshez és a kiadás előkészítéséhez

**Kiemelt példa**: Imádom használni kódellenőrzési munkafolyamatokhoz. Ahelyett, hogy ugrálnék a VS Code, GitHub értesítések és pull request oldalak között, csak azt mondom: „Mutasd meg az összes PR-t, amely az én átnézésemre vár” majd "Adj egy megjegyzést a #123 PR-hez a hitelesítési módszer hibakezelésével kapcsolatban." A szerver kezeli a GitHub API hívásokat, megőrzi a párbeszéd kontextusát, és még abban is segít, hogy konstruktívabb átnézési megjegyzéseket fogalmazzak meg.

**Hitelesítési lehetőségek**: A szerver támogatja az OAuth-ot (zökkenőmentesen VS Code-ban) és a Személyes Hozzáférési Tokeneket is, konfigurálható eszközkészletekkel, hogy csak a szükséges GitHub funkciókat engedélyezze. Futtathatod távoli hosztolt szolgáltatásként az azonnali beállítás érdekében vagy helyben Docker segítségével teljes ellenőrzésért.

> **💡 Profi tipp**
> 
> Engedélyezd csak a szükséges eszközkészleteket az MCP szerver beállításaiban a `--toolsets` paraméterrel, hogy csökkentsd a kontextus méretét és javítsd az AI eszközválasztást. Például adj hozzá `"--toolsets", "repos,issues,pull_requests,actions"` az MCP konfigurációs argumentumokhoz az alap fejlesztési munkafolyamatokhoz, vagy használd `"--toolsets", "notifications, security"` ha elsősorban GitHub megfigyelési képességeket szeretnél.
### 4. 🔄 Azure DevOps MCP Server

[![Telepítés VS Code-ban](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Telepítés VS Code Insiders-ben](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mit csinál**: Kapcsolódik az Azure DevOps szolgáltatásokhoz átfogó projektmenedzsment, munkatétel követés, build pipeline menedzsment és tároló műveletek érdekében.

**Miért hasznos**: Azoknak a csapatoknak, akik az Azure DevOps-t használják elsődleges DevOps platformként, ez az MCP szerver megszünteti a fejlesztési környezet és az Azure DevOps webes felülete közti állandó böngészőfül-váltogatást. Közvetlenül az AI asszisztenseden keresztül kezelheted a munkatételeket, ellenőrizheted a build állapotokat, lekérdezheted a tárolókat és kezelheted a projektmenedzsment feladatokat.

**Valós használat**: „Mutasd meg az összes aktív munkatételt a jelenlegi sprintben a WebApp projekthez”, „Hozz létre egy hibajelentést a most talált bejelentkezési problémáról”, vagy „Ellenőrizd a build pipeline-ok állapotát és mutass be minden legutóbbi hibát”

**Kiemelt példa**: Egyszerű lekérdezéssel könnyen ellenőrizheted a csapat aktuális sprintjének állapotát, például „Mutasd meg az összes aktív munkatételt a jelenlegi sprintben a WebApp projekthez”, vagy „Hozz létre egy hibajelentést a most talált bejelentkezési problémáról” anélkül, hogy elhagynád a fejlesztési környezetet.

### 5. 📝 MarkItDown MCP Server


[![Telepítés a VS Code-ba](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Telepítés a VS Code Insidersbe](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mit csinál**: A MarkItDown egy átfogó dokumentumkonverziós szerver, amely különböző fájlformátumokat alakít át kiváló minőségű Markdown formátumba, optimalizálva LLM feldolgozáshoz és szövegelemzési munkafolyamatokhoz.

**Miért hasznos**: Elengedhetetlen a modern dokumentációs munkafolyamatokhoz! A MarkItDown lenyűgöző mennyiségű fájlformátumot kezel miközben megőrzi a kritikus dokumentumszerkezetet, mint a címsorok, listák, táblázatok és linkek. Ellentétben az egyszerű szövegkinyerő eszközökkel, az értelmi jelentés és formázás megtartására koncentrál, ami értékes mind az MI feldolgozás, mind az emberi olvashatóság szempontjából.

**Támogatott fájlformátumok**:
- **Office dokumentumok**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Médiafájlok**: Képek (EXIF metaadatokkal és OCR-rel), Hangfájlok (EXIF metaadatokkal és beszédfelismeréssel)
- **Webtartalom**: HTML, RSS feedek, YouTube URL-ek, Wikipédia oldalak
- **Adatformátumok**: CSV, JSON, XML, ZIP fájlok (rekurzívan feldolgozza a tartalom)
- **Kiadói formátumok**: EPub, Jupyter notebookok (.ipynb)
- **E-mail**: Outlook üzenetek (.msg)
- **Fejlett**: Azure Document Intelligence integráció fejlettebb PDF feldolgozásért

**Fejlett képességek**: A MarkItDown támogatja az LLM által vezérelt kép leírásokat (OpenAI kliens esetén), az Azure Document Intelligence-t a fejlettebb PDF feldolgozáshoz, hangátírást a beszéd tartalmakhoz, valamint bővítmény rendszert további fájlformátumok kezeléséhez.

**Valós használat**: „Alakítsd át ezt a PowerPoint bemutatót Markdown formátumba a dokumentációs oldalunkhoz”, „Kinyerni a szöveget ebből a PDF-ből megfelelő címsor szerkezettel”, vagy „Alakítsd át ezt az Excel táblázatot olvasható táblázatformátumba”

**Kiemelt példa**: Idézve a [MarkItDown dokumentációból](https://github.com/microsoft/markitdown#why-markdown):

> A Markdown nagyon közel áll a sima szöveghez, minimális jelöléssel vagy formázással, de mégis lehetőséget ad fontos dokumentumszerkezet megjelenítésére. A főbb LLM-ek, mint az OpenAI GPT-4o, natívan "beszélnek" Markdownul, és gyakran beépítik azt válaszaikba önkéntelenül. Ez arra utal, hogy hatalmas mennyiségű Markdown formátumú szövegen tanultak, és jól értik azt. Mellékes előnye, hogy a Markdown konvenciók rendkívül tokenhatékonyak is.

A MarkItDown igazán jól megőrzi a dokumentumszerkezetet, ami fontos az MI munkafolyamatokban. Például egy PowerPoint prezentáció konvertálásakor megőrzi a diák szerkezetét a megfelelő címsorokkal, kinyeri a táblázatokat Markdown táblázatokként, tartalmazza a képek alternatív szövegét, és még a szónoki jegyzeteket is feldolgozza. A diagramokat olvasható adattáblázatokra alakítja, és az eredményként kapott Markdown megőrzi az eredeti bemutató logikai folyamatát. Ez tökéletessé teszi a prezentációs tartalom MI rendszerekbe való betáplálásához vagy létező diákról készülő dokumentációhoz.
### 6. 🗃️ SQL Server MCP szerver

[![Telepítés a VS Code-ba](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Telepítés a VS Code Insidersbe](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mit csinál**: Beszélgetéses hozzáférést biztosít SQL Server adatbázisokhoz (helyszíni, Azure SQL vagy Fabric)

**Miért hasznos**: Hasonló a PostgreSQL szerverhez, de a Microsoft SQL ökoszisztémához. Egyszerű kapcsolati lánccal csatlakozhatsz és természetes nyelven kezdhetsz lekérdezéseket futtatni – nincs többé kontextus váltás!

**Valós használat**: „Találd meg azokat a megrendeléseket, amelyeket az elmúlt 30 napban nem teljesítettek” lekérdezése átalakul a megfelelő SQL lekérdezésekre és formázott eredményt ad vissza

**Kiemelt példa**: Miután beállítottad az adatbázis kapcsolatot, azonnal elkezdhetsz beszélgetni az adataiddal. A blogbejegyzés ezt egy egyszerű kérdéssel mutatja be: „Melyik adatbázishoz vagy csatlakozva?” Az MCP szerver erre meghívja a megfelelő adatbázis eszközt, csatlakozik az SQL Server példányodhoz, és visszaadja a jelenlegi adatbázis kapcsolat részleteit – mindezt egyetlen SQL sor írása nélkül. A szerver támogatja az átfogó adatbázis műveleteket a sémamenedzsmenttől az adatmódosításig, mindezt természetes nyelvi utasításokon keresztül. Teljes beállítási lépésekért és VS Code illetve Claude Desktop konfigurációs példákért lásd: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP szerver

[![Telepítés a VS Code-ba](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Telepítés a VS Code Insidersbe](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mit csinál**: Lehetővé teszi MI ügynökök számára, hogy weboldalakkal interaktáljanak tesztelés és automatizálás céljából

> **ℹ️ A GitHub Copilot motorja**
> 
> A Playwright MCP szerver működteti a GitHub Copilot kódoló ügynökét, ami web böngészési képességekkel ruházza fel őt! [Tudj meg többet erről a funkcióról](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miért hasznos**: Tökéletes a természetes nyelvi leírásokon alapuló automatizált teszteléshez. Az MI képes weboldalakat böngészni, űrlapokat kitölteni és strukturált hozzáférhetőségi pillanatképek alapján adatokat kinyerni – ez hihetetlenül erős!

**Valós használat**: „Teszteld a bejelentkezési folyamatot és ellenőrizd, hogy a műszerfal megfelelően töltődik be” vagy „Generálj egy tesztet, ami termékeket keres és ellenőrzi az eredményoldalt” – mindezt forráskód nélkül

**Kiemelt példa**: Debbie O'Brien kolléganőm mostanában fantasztikus munkát végez a Playwright MCP szerverrel! Például nemrég megmutatta, hogyan lehet teljes Playwright teszteket generálni úgy, hogy még csak nem is volt hozzáférése az alkalmazás forráskódjához. Az ő példájában a Copilotnak adott egy teszt kérdést egy filmkereső alkalmazáshoz: navigálj az oldalra, keress rá a „Garfield” kifejezésre, és ellenőrizd, hogy a film megjelenik az eredmények között. Az MCP elindított egy böngésző munkamenetet, feltérképezte az oldal szerkezetét DOM pillanatképek segítségével, megtalálta a megfelelő szelektorokat, és generált egy teljesen működő TypeScript tesztet, ami első futásra sikeres volt.

Ami igazán erőssé teszi ezt, hogy áthidalja a természetes nyelvű utasítások és a végrehajtható tesztkód közötti szakadékot. A hagyományos megközelítések vagy kézi tesztírást, vagy a kód bázishoz való hozzáférést igényelnek kontextus miatt. De a Playwright MCP-vel külső oldalakat, kliensalkalmazásokat vagy fekete dobozos tesztelési helyzeteket is tesztelhetsz, ahol nincs kódhozzáférés.


### 8. 💻 Dev Box MCP szerver

[![Telepítés a VS Code-ba](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Telepítés a VS Code Insidersbe](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mit csinál**: Természetes nyelven kezeli a Microsoft Dev Box környezeteket

**Miért hasznos**: Nagyon leegyszerűsíti a fejlesztői környezetek kezelését! Hozd létre, konfiguráld és kezeld a fejlesztői környezeteket anélkül, hogy meg kéne jegyezned konkrét parancsokat.

**Valós használat**: „Állíts be egy új Dev Boxot a legfrissebb .NET SDK-val és konfiguráld a projektünkhöz”, „Ellenőrizd az összes fejlesztői környezetem állapotát”, vagy „Hozz létre egy szabványosított demo környezetet a csapat bemutatóihoz”

**Kiemelt példa**: Nagy rajongója vagyok a Dev Box személyes fejlesztésre való használatának. A fény az alagút végén akkor gyúlt fel, amikor James Montemagno elmagyarázta, milyen nagyszerű a Dev Box konferencia demo-khoz, mert villámgyors ethernet kapcsolatot biztosít függetlenül attól, hogy éppen milyen konferencia, szálloda vagy repülőgépes wifi-t használok. Valójában nemrég csináltam egy konferencia demo gyakorlást, miközben a laptopom a telefonom hotspotjához volt kapcsolva és egy buszon utaztam Brugesből Antwerpenbe! A következő lépés nálam az, hogy elmélyedjek a több fejlesztői környezetet kezelő csapatok támogatásában és szabványosított demo környezetek létrehozásában. Egy másik nagy felhasználási terület, amit ügyfelektől és kollégáktól hallok, természetesen a Dev Box előre konfigurált fejlesztői környezeteinek használata. Mindkét esetben az MCP segítségével konfigurálhatod és kezelheted a Dev Boxokat természetes nyelvű interakcióval, miközben a fejlesztői környezetedben maradsz.

### 9. 🤖 Microsoft Foundry MCP szerver


[![Telepítés VS Code-ban](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Telepítés VS Code Insiders-ben](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Mit csinál**: A Microsoft Foundry MCP Server átfogó hozzáférést biztosít a fejlesztőknek az Azure AI ökoszisztémához, beleértve a modellkatalógusokat, a telepítéskezelést, a tudásindexelést az Azure AI Search segítségével, és az értékelési eszközöket. Ez a kísérleti szerver hidat képez az AI fejlesztés és az Azure erőteljes AI infrastruktúrája között, megkönnyítve az AI alkalmazások építését, telepítését és értékelését.

**Miért hasznos**: Ez a szerver átalakítja az Azure AI szolgáltatásokkal való munkát azáltal, hogy vállalati szintű AI képességeket hoz közvetlenül a fejlesztési munkafolyamatba. Az Azure portál, a dokumentáció és az IDE közötti váltogatás helyett felfedezheted a modelleket, telepítheted a szolgáltatásokat, kezelheted a tudásbázisokat, és természtes nyelvű parancsokkal értékelheted az AI teljesítményt. Különösen hasznos fejlesztőknek, akik RAG (Retrieval-Augmented Generation) alkalmazásokat építenek, többmodelles telepítéseket kezelnek, vagy átfogó AI értékelési folyamatokat valósítanak meg.

**Főbb fejlesztői képességek**:
- **🔍 Modell felfedezés és telepítés**: Böngészd a Microsoft Foundry modellkatalógusát, kapj részletes modellinformációkat kódmintákkal, és telepíts modelleket az Azure AI szolgáltatásokra
- **📚 Tudáskezelés**: Hozz létre és kezelj Azure AI Search indexeket, adj hozzá dokumentumokat, konfigurálj indexelőket, és építs kifinomult RAG rendszereket
- **⚡ AI ügynök integráció**: Csatlakozz az Azure AI ügynökökhöz, kérdezd le meglévő ügynököket, és értékeld az ügynök teljesítményt éles környezetben
- **📊 Értékelési keretrendszer**: Futtass átfogó szöveges és ügynöki értékeléseket, generálj markdown jelentéseket, és valósíts meg minőségbiztosítást AI alkalmazásokhoz
- **🚀 Prototípus-készítő eszközök**: Szerezz beállítási utasításokat GitHub-alapú prototípus készítéséhez, és férj hozzá a Microsoft Foundry Labs legújabb kutatási modelljeihez

**Valós fejlesztői használat**: "Telepíts egy Phi-4 modellt az Azure AI szolgáltatásokra az alkalmazásomhoz", "Hozz létre egy új keresési indexet a dokumentációm RAG rendszeréhez", "Értékeld az ügynököm válaszait minőségi mutatók alapján", vagy "Találd meg a legjobb érvelő modellt a komplex elemzési feladataimhoz"

**Teljes demó forgatókönyv**: Íme egy erőteljes AI fejlesztési munkafolyamat:

> "Ügyféltámogató ügynököt építek. Segíts, hogy találjak egy jó érvelő modellt a katalógusból, telepítsem az Azure AI szolgáltatásokra, hozzak létre egy tudásbázist a dokumentációnkból, állítsak be egy értékelési keretrendszert a válaszok minőségének tesztelésére, majd segíts a GitHub tokenes integráció prototípusának elkészítésében tesztelés céljából."

A Microsoft Foundry MCP Server a következőket fogja tenni:
- Lekérdezi a modellkatalógust, hogy ajánljon optimális érvelő modelleket az igényeid alapján
- Biztosítja a telepítési parancsokat és kvóta információkat az általad preferált Azure régióra
- Beállítja az Azure AI Search indexeket a dokumentációd megfelelő sémával
- Konfigurálja az értékelési folyamatokat minőségi mutatókkal és biztonsági ellenőrzésekkel
- Elkészíti a prototípus kódját GitHub hitelesítéssel az azonnali teszteléshez
- Átfogó beállítási útmutatókat nyújt a specifikus technológiai környezetedhez igazítva

**Kiemelt példa**: Fejlesztőként nehéz volt lépést tartanom a különböző LLM modellekkel. Néhány főbb modellt ismerek, de úgy éreztem, mintha lemaradnék bizonyos termelékenység- és hatékonyságjavulásokról. A tokenek és kvóták kezelése is stresszes és nehéz — sosem tudom, hogy a megfelelő modellt választom-e a megfelelő feladathoz, vagy épp hatékonytalanul égetem a költségvetésemet. Most hallottam erről az MCP Serverről James Montemagno-tól, amikor a csapattársaimnál érdeklődtem MCP szerver ajánlások után ehhez a bejegyzéshez, és alig várom, hogy kipróbáljam! A modell felfedező képességek különösen lenyűgözőek azok számára, mint én, akik az általános modelleken túl akarnak kutatni és speciális feladatokra optimalizált modelleket találni. Az értékelési keretrendszer pedig segít biztosítani, hogy tényleg jobb eredményeket kapjak, ne csak új dolgot próbáljak ki a sora miatt.

> **ℹ️ Kísérleti állapot**
> 
> Ez az MCP szerver kísérleti állapotban van, aktív fejlesztés alatt. A funkciók és API-k változhatnak. Kiváló az Azure AI képességek felfedezéséhez és prototípusok építéséhez, de a stabilitás igényeit győződj meg, ha éles környezetben akarod használni.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Telepítés VS Code-ban](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Telepítés VS Code Insiders-ben](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Mit csinál**: Alapvető eszközöket biztosít fejlesztőknek AI ügynökök és alkalmazások építéséhez, amelyek integrálódnak a Microsoft 365-tel és a Microsoft 365 Copilot-tal, beleértve a sémaellenőrzést, kódminták lekérését és hibakeresési segítséget.

**Miért hasznos**: A Microsoft 365 és Copilot fejlesztése komplex manifest sémákat és specifikus fejlesztési mintákat igényel. Ez az MCP szerver alapvető fejlesztői erőforrásokat hoz közvetlenül a kódolási környezetedbe, segítve a sémák validálását, kódminták megtalálását és a gyakori hibák elhárítását anélkül, hogy folyamatosan a dokumentációra kellene hivatkozni.

**Valós használat**: "Érvényesítsd a deklaratív ügynök manifestemet és javítsd a sémaháztó hibákat", "Mutass példakódot Microsoft Graph API plugin megvalósításához", vagy "Segíts hibakeresni a Teams alkalmazásom hitelesítési problémáit"

**Kiemelt példa**: Felvettem a kapcsolatot a barátommal, John Millerrel, miután a Build konferencián beszélgettünk az M365 ügynökökről, és ő ezt az MCP-t ajánlotta. Ez nagyszerű lehet azoknak a fejlesztőknek, akik újak az M365 ügynökök világában, hiszen sablonokat, kódmintákat és keretrendszert biztosít, hogy dokumentációba fulladás nélkül kezdjenek. A sémaellenőrző funkciók különösen hasznosak az olyan manifest szerkezeti hibák elkerülésére, amelyek több órányi hibakeresést okozhatnak.

> **💡 Profi tipp**
> 
> Használd ezt a szervert együtt a Microsoft Learn Docs MCP Serverrel a teljes körű M365 fejlesztési támogatásért — az egyik a hivatalos dokumentációt szolgáltatja, míg ez gyakorlati fejlesztői eszközöket és hibakeresési segítséget nyújt.


## Mi következik? 🔮

## 📋 Összefoglalás

A Model Context Protocol (MCP) átalakítja, ahogyan a fejlesztők AI asszisztensekkel és külső eszközökkel kommunikálnak. Ezek a 10 Microsoft MCP szerver bemutatják a szabványosított AI integráció erejét, lehetővé téve zökkenőmentes munkafolyamatokat, amelyek fejlesztőként a flow állapotban tartanak miközben erőteljes külső képességekhez férsz hozzá.

Az átfogó Azure ökoszisztéma integrációjától kezdve specializált eszközökig, mint a Playwright böngésző automatizáláshoz és a MarkItDown dokumentum feldolgozáshoz, ezek a szerverek megmutatják, hogyan fokozhatja az MCP a termelékenységet sokféle fejlesztési forgatókönyvben. A szabványosított protokoll biztosítja, hogy ezek az eszközök zökkenőmentesen működjenek együtt, egy összefüggő fejlesztői élményt teremtve.

Ahogy az MCP ökoszisztéma folyamatosan fejlődik, a közösséggel való kapcsolat fenntartása, új szerverek felfedezése és egyedi megoldások építése lesz a kulcs a fejlesztési hatékonyság maximalizálásához. Az MCP nyílt szabvány jellege lehetővé teszi, hogy különböző szolgáltatók eszközeit kombináld, és létrehozd a tökéletes munkafolyamatot az egyéni igényeidhez.

## 🔗 További források

- [Hivatalos Microsoft MCP Tároló](https://github.com/microsoft/mcp)
- [MCP Közösség és Dokumentáció](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Dokumentáció](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Dokumentáció](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Dokumentáció](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Tanuljunk – MCP Események](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Szuper GitHub Copilot Testreszabások](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days élőben július 29-30 vagy igény szerint](https://aka.ms/mcpdevdays)

## 🎯 Gyakorlatok

1. **Telepítés és konfiguráció**: Állíts be egy MCP szervert a VS Code környezetedben, és teszteld az alapvető funkciókat.
2. **Munkafolyamat integráció**: Tervezzen egy fejlesztési munkafolyamatot, amely legalább három különböző MCP szervert kombinál.
3. **Egyedi szerver tervezése**: Azonosíts egy feladatot a napi fejlesztési rutinodban, amely hasznát vehetné egy egyedi MCP szervernek, és készíts hozzá specifikációt.
4. **Teljesítmény elemzés**: Hasonlítsd össze az MCP szerverek használatának hatékonyságát a hagyományos megközelítésekkel a gyakori fejlesztési feladatok esetén.
5. **Biztonsági értékelés**: Vizsgáld meg az MCP szerverek fejlesztési környezetben való használatának biztonsági vonatkozásait, és javasolj legjobb gyakorlatokat.


Következő:[Legjobb gyakorlatok](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->