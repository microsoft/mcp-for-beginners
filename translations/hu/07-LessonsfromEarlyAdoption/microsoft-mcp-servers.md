# 🚀 10 Microsoft MCP szerver, amely forradalmasítja a fejlesztők hatékonyságát

## 🎯 Mit tanulhatsz meg ebben az útmutatóban

Ez a gyakorlati útmutató tíz Microsoft MCP szervert mutat be, amelyek aktívan alakítják, hogyan dolgoznak a fejlesztők AI asszisztensekkel. Nem csak azt magyarázzuk el, hogy az MCP szerverek *mit tudnak*, hanem bemutatjuk azokat a szervereket, amelyek már most is valódi változást hoznak a Microsoftnál és azon túl a napi fejlesztési munkafolyamatokban.

Minden szervert valós használat és fejlesztői visszajelzések alapján választottunk ki. Megtudhatod, mit csinál egy-egy szerver, miért fontos, és hogyan hozhatod ki belőle a legtöbbet a saját projektjeidben. Akár teljesen új vagy az MCP-ben, akár bővíteni szeretnéd a meglévő rendszeredet, ezek a szerverek a Microsoft ökoszisztéma legpraktikusabb és legnagyobb hatású eszközeit képviselik.

> **💡 Gyors kezdő tipp**
> 
> Új vagy az MCP-ben? Ne aggódj! Ez az útmutató kezdőknek készült. Végigvezetünk a fogalmakon, és bármikor visszatérhetsz az [Introduction to MCP](../00-Introduction/README.md) és a [Core Concepts](../01-CoreConcepts/README.md) modulokhoz, ha mélyebb háttérre van szükséged.

## Áttekintés

Ez az átfogó útmutató tíz Microsoft MCP szervert vizsgál meg, amelyek forradalmasítják, hogyan lépnek kapcsolatba a fejlesztők AI asszisztensekkel és külső eszközökkel. Az Azure erőforráskezeléstől a dokumentumfeldolgozásig ezek a szerverek megmutatják, milyen erőt képvisel a Model Context Protocol a zökkenőmentes, hatékony fejlesztési munkafolyamatok létrehozásában.

## Tanulási célok

Az útmutató végére:
- Megérted, hogyan növelik az MCP szerverek a fejlesztők hatékonyságát
- Megismered a Microsoft legjelentősebb MCP szerver implementációit
- Felfedezed az egyes szerverek gyakorlati felhasználási eseteit
- Tudni fogod, hogyan állítsd be és konfiguráld ezeket a szervereket VS Code-ban és Visual Studio-ban
- Megismered az MCP ökoszisztéma szélesebb körét és jövőbeli irányait

## 🔧 MCP szerverek megértése: Kezdőknek

### Mik azok az MCP szerverek?

Ha kezdő vagy a Model Context Protocol (MCP) területén, talán az a kérdésed, hogy „Mi is pontosan az MCP szerver, és miért érdekeljen engem?” Kezdjük egy egyszerű hasonlattal.

Gondolj az MCP szerverekre úgy, mint speciális asszisztensekre, amelyek segítik az AI kódoló társadat (például a GitHub Copilotot), hogy kapcsolódjon külső eszközökhöz és szolgáltatásokhoz. Ahogy a telefonodon különböző alkalmazásokat használsz különböző feladatokra – egyet az időjárásra, egyet a navigációra, egyet a bankolásra –, az MCP szerverek lehetővé teszik az AI asszisztensed számára, hogy különféle fejlesztői eszközökkel és szolgáltatásokkal kommunikáljon.

### Milyen problémát oldanak meg az MCP szerverek?

Az MCP szerverek előtt, ha például:
- Meg akartad nézni az Azure erőforrásaidat
- Létrehozni egy GitHub issue-t
- Lekérdezni az adatbázisodat
- Dokumentációban keresni

Meg kellett szakítanod a kódolást, megnyitni a böngészőt, a megfelelő weboldalra navigálni, és manuálisan elvégezni ezeket a feladatokat. Ez az állandó kontextusváltás megtöri a munkafolyamatot és csökkenti a hatékonyságot.

### Hogyan változtatják meg az MCP szerverek a fejlesztési élményt?

Az MCP szerverekkel a fejlesztői környezetedben (VS Code, Visual Studio stb.) maradhatsz, és egyszerűen megkérheted az AI asszisztenst, hogy végezze el ezeket a feladatokat. Például:

**A hagyományos munkafolyamat helyett:**
1. Megállsz a kódolásban
2. Megnyitod a böngészőt
3. Az Azure portálra navigálsz
4. Megnézed a tárolófiók adatait
5. Visszatérsz a VS Code-ba
6. Folytatod a kódolást

**Most már ezt teheted:**
1. Megkérdezed az AI-t: „Mi a státusza az Azure tárolófiókjaimnak?”
2. A kapott információval folytatod a kódolást

### Fő előnyök kezdőknek

#### 1. 🔄 **Maradj a flow állapotban**
- Nem kell több alkalmazás között váltogatni
- A kódolásra koncentrálhatsz
- Csökken a különböző eszközök kezelése miatti mentális terhelés

#### 2. 🤖 **Használj természetes nyelvet a bonyolult parancsok helyett**
- Nem kell SQL szintaxist memorizálni, csak írd le, milyen adatot szeretnél
- Nem kell fejben tartani az Azure CLI parancsokat, csak mondd el, mit akarsz elérni
- Az AI intézi a technikai részleteket, te a logikára koncentrálhatsz

#### 3. 🔗 **Kapcsold össze az eszközöket**
- Hozz létre hatékony munkafolyamatokat különböző szolgáltatások kombinálásával
- Példa: „Szerezz be minden friss GitHub issue-t, és hozz létre hozzájuk megfelelő Azure DevOps munkafolyamatokat”
- Automatizálj bonyolult szkriptek írása nélkül

#### 4. 🌐 **Használj egy folyamatosan bővülő ökoszisztémát**
- Használj Microsoft, GitHub és más cégek által fejlesztett szervereket
- Különböző gyártók eszközeit keverd össze zökkenőmentesen
- Csatlakozz egy szabványosított ökoszisztémához, amely több AI asszisztenssel is működik

#### 5. 🛠️ **Tanulj a gyakorlatban**
- Kezdd előre elkészített szerverekkel, hogy megértsd az alapokat
- Fokozatosan építsd fel a saját szervereidet, ahogy egyre magabiztosabb leszel
- Használd az elérhető SDK-kat és dokumentációkat a tanuláshoz

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

### Az Enterprise szabvány előnyei

Az MCP iparági szabvánnyá válik, ami azt jelenti:
- **Konzisztencia**: Hasonló élmény különböző eszközök és cégek között
- **Interoperabilitás**: Különböző gyártók szerverei együttműködnek
- **Jövőbiztosság**: Készségek és beállítások átvihetők különböző AI asszisztensek között
- **Közösség**: Nagy, megosztott tudás- és erőforrásbázis

### Kezdés: Mit tanulsz meg

Ebben az útmutatóban 10 Microsoft MCP szervert mutatunk be, amelyek különösen hasznosak minden szintű fejlesztő számára. Minden szerver arra lett tervezve, hogy:
- Megoldja a gyakori fejlesztési kihívásokat
- Csökkentse az ismétlődő feladatokat
- Javítsa a kód minőségét
- Növelje a tanulási lehetőségeket

> **💡 Tanulási tipp**
> 
> Ha teljesen új vagy az MCP-ben, először nézd meg az [Introduction to MCP](../00-Introduction/README.md) és a [Core Concepts](../01-CoreConcepts/README.md) modulokat. Ezután térj vissza ide, hogy lásd, hogyan működnek ezek a fogalmak a valós Microsoft eszközökkel.
>
> Az MCP fontosságáról további háttérért olvasd el Maria Naggaga bejegyzését: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## MCP szerverek beállítása VS Code-ban és Visual Studio-ban 🚀

Ezeknek az MCP szervereknek a beállítása egyszerű, ha Visual Studio Code-ot vagy Visual Studio 2022-t használsz GitHub Copilottal.

### VS Code beállítás

A VS Code esetén az alapfolyamat:

1. **Agent mód engedélyezése**: A Copilot Chat ablakban válts Agent módra
2. **MCP szerverek konfigurálása**: Add hozzá a szerver konfigurációkat a VS Code settings.json fájlodhoz
3. **Szerverek indítása**: Kattints a „Start” gombra az egyes használni kívánt szervereknél
4. **Eszközök kiválasztása**: Válaszd ki, mely MCP szervereket engedélyezed az aktuális munkamenethez

Részletes beállítási útmutatóért lásd a [VS Code MCP dokumentációt](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profi tipp: Kezeld az MCP szervereket profiként!**
> 
> A VS Code Extensions nézetében most már elérhető egy [kényelmes új felület az MCP szerverek kezeléséhez](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Gyorsan indíthatod, leállíthatod és kezelheted az összes telepített MCP szervert egy átlátható, egyszerű felületen. Próbáld ki!

### Visual Studio 2022 beállítás

Visual Studio 2022 (17.14-es vagy újabb verzió) esetén:

1. **Agent mód engedélyezése**: A GitHub Copilot Chat ablak „Ask” legördülő menüjében válaszd az „Agent” opciót
2. **Konfigurációs fájl létrehozása**: Hozz létre egy `.mcp.json` fájlt a megoldás könyvtárában (ajánlott hely: `<SOLUTIONDIR>\.mcp.json`)
3. **Szerverek konfigurálása**: Add hozzá az MCP szerver konfigurációkat a szabványos MCP formátumban
4. **Eszköz jóváhagyása**: Amikor kéri, engedélyezd a használni kívánt eszközöket a megfelelő jogosultságokkal

Részletes Visual Studio beállítási útmutatóért lásd a [Visual Studio MCP dokumentációt](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Minden MCP szervernek megvannak a saját konfigurációs igényei (kapcsolati adatok, hitelesítés stb.), de a beállítási minta mindkét IDE-ben következetes.

## Tanulságok a Microsoft MCP szerverekből 🛠️

### 1. 📚 Microsoft Learn Docs MCP szerver

[![Telepítés VS Code-ban](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Telepítés VS Code Insiders-ben](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mit csinál**: A Microsoft Learn Docs MCP szerver egy felhőalapú szolgáltatás, amely valós idejű hozzáférést biztosít az AI asszisztenseknek a hivatalos Microsoft dokumentációkhoz a Model Context Protocolon keresztül. Csatlakozik a `https://learn.microsoft.com/api/mcp` végponthoz, és lehetővé teszi a szemantikus keresést a Microsoft Learn, az Azure dokumentáció, a Microsoft 365 dokumentáció és más hivatalos Microsoft források között.

**Miért hasznos**: Bár elsőre „csak dokumentációnak” tűnhet, ez a szerver kulcsfontosságú minden Microsoft technológiát használó fejlesztő számára. Az egyik leggyakoribb panasz a .NET fejlesztők részéről az AI kódoló asszisztensekkel kapcsolatban, hogy nem naprakészek a legújabb .NET és C# kiadásokkal. A Microsoft Learn Docs MCP szerver ezt oldja meg azzal, hogy valós idejű hozzáférést biztosít a legfrissebb dokumentációkhoz, API referenciákhoz és bevált gyakorlatokhoz. Akár a legújabb Azure SDK-kkal dolgozol, akár a C# 13 új funkcióit fedezed fel, vagy a legmodernebb .NET Aspire mintákat valósítod meg, ez a szerver biztosítja, hogy az AI asszisztensed hozzáférjen a hiteles, naprakész információkhoz, amelyekkel pontos, korszerű kódot generálhat.

**Valós használat**: „Mik az az CLI parancsok egy Azure container app létrehozásához a hivatalos Microsoft Learn dokumentáció szerint?” vagy „Hogyan konfiguráljam az Entity Framework-öt dependency injection-nel ASP.NET Core-ban?” Vagy „Nézd át ezt a kódot, hogy megfelel-e a Microsoft Learn dokumentáció teljesítményre vonatkozó ajánlásainak.” A szerver átfogó lefedettséget nyújt a Microsoft Learn, az Azure dokumentáció és a Microsoft 365 dokumentáció között fejlett szemantikus kereséssel, hogy megtalálja a leginkább releváns információkat. Legfeljebb 10 magas minőségű tartalmi egységet ad vissza cikkcímekkel és URL-ekkel, mindig a legfrissebb Microsoft dokumentációt használva.

**Kiemelt példa**: A szerver elérhetővé teszi a `microsoft_docs_search` eszközt, amely szemantikus keresést végez a Microsoft hivatalos technikai dokumentációjában. A konfiguráció után kérdezhetsz például: „Hogyan valósítsak meg JWT hitelesítést ASP.NET Core-ban?” és részletes, hivatalos válaszokat kapsz forráslinkekkel. A keresés minősége kiváló, mert érti a kontextust – ha „konténerek” kifejezést Azure környezetben kérdezed, az Azure Container Instances dokumentációját adja vissza, míg .NET kontextusban a C# gyűjteményekhez kapcsolódó információkat.

Ez különösen hasznos gyorsan változó vagy nemrég frissített könyvtárak és felhasználási esetek esetén. Például néhány friss kódolási projektben a legújabb .NET Aspire és Microsoft.Extensions.AI kiadások funkcióit akartam kihasználni. A Microsoft Learn Docs MCP szerver bevonásával nem csak API dokumentációkat, hanem frissen megjelent útmutatókat és példákat is tudtam használni.
> **💡 Profi tipp**
> 
> Még az eszközbarát modelleket is ösztönözni kell az MCP eszközök használatára! Érdemes hozzáadni egy rendszerüzenetet vagy a [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) fájlt, például: „Hozzáférésed van a `microsoft.docs.mcp`-hez – használd ezt az eszközt, hogy a Microsoft legfrissebb hivatalos dokumentációjában keress, amikor Microsoft technológiákkal kapcsolatos kérdéseket kezelsz, mint például C#, Azure, ASP.NET Core vagy Entity Framework.”
>
> Egy remek példa erre a gyakorlatban a [C# .NET Janitor chat mód](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) az Awesome GitHub Copilot tárolóból. Ez a mód kifejezetten a Microsoft Learn Docs MCP szervert használja, hogy segítsen megtisztítani és modernizálni a C# kódot a legújabb minták és bevált gyakorlatok alkalmazásával.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mit csinál**: Az Azure MCP Server egy átfogó csomag több mint 15 speciális Azure szolgáltatás-kapcsolóval, amely az egész Azure ökoszisztémát beemeli az AI munkafolyamatodba. Ez nem csupán egyetlen szerver – egy erőteljes gyűjtemény, amely tartalmaz erőforrás-kezelést, adatbázis-kapcsolatokat (PostgreSQL, SQL Server), Azure Monitor naplóelemzést KQL-lel, Cosmos DB integrációt és még sok mást.

**Miért hasznos**: Az Azure erőforrások kezelésén túl ez a szerver jelentősen javítja a kód minőségét az Azure SDK-k használata során. Ha az Azure MCP-t Agent módban használod, nem csak segít kódot írni – hanem *jobb* Azure kódot írni, amely követi a jelenlegi hitelesítési mintákat, a hibakezelés legjobb gyakorlatait, és kihasználja a legújabb SDK funkciókat. Ahelyett, hogy csak egy általános, működő kódot kapnál, olyan kódot kapsz, amely az Azure ajánlott mintáit követi éles környezetekhez.

**Főbb modulok**:
- **🗄️ Adatbázis-kapcsolók**: Természetes nyelvű közvetlen hozzáférés az Azure Database for PostgreSQL és SQL Server adatbázisokhoz
- **📊 Azure Monitor**: KQL-alapú naplóelemzés és működési betekintések
- **🌐 Erőforrás-kezelés**: Teljes Azure erőforrás életciklus-kezelés
- **🔐 Hitelesítés**: DefaultAzureCredential és managed identity minták
- **📦 Tárolási szolgáltatások**: Blob Storage, Queue Storage és Table Storage műveletek
- **🚀 Konténer szolgáltatások**: Azure Container Apps, Container Instances és AKS kezelése
- **És még sok más speciális kapcsoló**

**Valós használat**: „Listázd az Azure tárolófiókjaimat”, „Kérdezd le a Log Analytics munkaterületem hibáit az elmúlt órából”, vagy „Segíts egy Azure alkalmazás építésében Node.js-ben megfelelő hitelesítéssel”

**Teljes demó forgatókönyv**: Itt egy teljes bemutató, amely megmutatja, milyen erős az Azure MCP és a GitHub Copilot for Azure kiterjesztés kombinációja VS Code-ban. Ha mindkettő telepítve van, és ezt írod be:

> „Készíts egy Python szkriptet, amely fájlt tölt fel az Azure Blob Storage-ba DefaultAzureCredential hitelesítéssel. A szkript csatlakozzon az 'mycompanystorage' nevű Azure tárolófiókomhoz, töltsön fel egy 'documents' nevű konténerbe, hozzon létre egy tesztfájlt az aktuális időbélyeggel, kezelje a hibákat elegánsan és adjon informatív visszajelzést, kövesse az Azure hitelesítési és hibakezelési legjobb gyakorlatait, tartalmazzon kommentárokat a DefaultAzureCredential működéséről, és legyen jól strukturált, megfelelő függvényekkel és dokumentációval.”

Az Azure MCP Server egy teljes, éles környezetbe alkalmas Python szkriptet generál, amely:
- A legújabb Azure Blob Storage SDK-t használja megfelelő aszinkron mintákkal
- Megvalósítja a DefaultAzureCredential-t átfogó fallback lánc magyarázattal
- Robusztus hibakezelést tartalmaz specifikus Azure kivételtípusokkal
- Követi az Azure SDK legjobb gyakorlatait erőforrás-kezelés és kapcsolatkezelés terén
- Részletes naplózást és informatív konzol kimenetet biztosít
- Jól strukturált szkriptet hoz létre függvényekkel, dokumentációval és típusjelzésekkel

A különlegessége, hogy Azure MCP nélkül csak egy általános blob storage kódot kaphatnál, ami működik, de nem követi a jelenlegi Azure mintákat. Az Azure MCP-vel olyan kódot kapsz, amely a legújabb hitelesítési módszereket használja, kezeli az Azure-specifikus hibákat, és követi a Microsoft ajánlásait éles alkalmazásokhoz.

**Kiemelt példa**: Nekem mindig gondot okozott az `az` és `azd` CLI parancsok pontos megjegyzése ad-hoc használathoz. Mindig két lépés: először megnézem a szintaxist, aztán futtatom a parancsot. Gyakran inkább csak belépek a portálra és kattintgatok, mert nem akarom bevallani, hogy nem emlékszem a CLI szintaxisra. Az, hogy egyszerűen le tudom írni, mit szeretnék, fantasztikus, és még jobb, hogy ezt az IDE-ből ki sem lépve megtehetem!

A [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) remek listát tartalmaz a kezdéshez. A részletes telepítési útmutatókért és haladó beállítási lehetőségekért nézd meg a [hivatalos Azure MCP dokumentációt](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mit csinál**: A hivatalos GitHub MCP Server zökkenőmentes integrációt biztosít a GitHub teljes ökoszisztémájával, mind távoli hosztolt hozzáféréssel, mind helyi Docker telepítési lehetőséggel. Ez nem csak alapvető repository műveletekről szól – egy átfogó eszköztár, amely magában foglalja a GitHub Actions kezelését, pull request munkafolyamatokat, issue követést, biztonsági szkennelést, értesítéseket és fejlett automatizálási funkciókat.

**Miért hasznos**: Ez a szerver átalakítja a GitHubbal való interakciódat azáltal, hogy a teljes platformélményt közvetlenül a fejlesztői környezetedbe hozza. Ahelyett, hogy folyton váltogatnál VS Code és GitHub.com között projektmenedzsment, kódáttekintés és CI/CD figyelés miatt, mindent természetes nyelvű parancsokkal intézhetsz, miközben a kódodra koncentrálsz.

> **ℹ️ Megjegyzés: Különböző típusú 'Agentek'**
> 
> Ne keverd össze ezt a GitHub MCP Servert a GitHub Coding Agenttel (az AI ágenssel, amelyhez GitHub issue-kat rendelhetsz automatikus kódolási feladatokhoz). A GitHub MCP Server a VS Code Agent módban működik, hogy GitHub API integrációt biztosítson, míg a GitHub Coding Agent egy külön funkció, amely pull requesteket hoz létre, ha GitHub issue-khoz van rendelve.

**Főbb képességek**:
- **⚙️ GitHub Actions**: Teljes CI/CD pipeline kezelés, munkafolyamat figyelés és artifact kezelés
- **🔀 Pull Requestek**: PR-k létrehozása, átnézése, egyesítése és kezelése átfogó státusz követéssel
- **🐛 Issue-k**: Teljes issue életciklus-kezelés, kommentelés, címkézés és hozzárendelés
- **🔒 Biztonság**: Kód szkennelési riasztások, titokfelismerés és Dependabot integráció
- **🔔 Értesítések**: Okos értesítéskezelés és repository feliratkozás vezérlés
- **📁 Repository kezelés**: Fájlműveletek, ágkezelés és repository adminisztráció
- **👥 Együttműködés**: Felhasználó- és szervezetkeresés, csapatkezelés és hozzáférés-vezérlés

**Valós használat**: „Hozz létre egy pull requestet a feature branch-emből”, „Mutasd meg az összes sikertelen CI futást ezen a héten”, „Listázd az összes nyitott biztonsági riasztást a repository-jaimban”, vagy „Találd meg az összes hozzám rendelt issue-t a szervezeteimben”

**Teljes demó forgatókönyv**: Íme egy erőteljes munkafolyamat, amely bemutatja a GitHub MCP Server képességeit:

> „Készülnöm kell a sprint áttekintésre. Mutasd meg az összes pull requestet, amit ezen a héten készítettem, ellenőrizd a CI/CD pipeline-ok állapotát, készíts összefoglalót a megoldandó biztonsági riasztásokról, és segíts megírni a kiadási megjegyzéseket a 'feature' címkével ellátott egyesített PR-ek alapján.”

A GitHub MCP Server:
- Lekérdezi a legutóbbi pull requesteket részletes státusz információkkal
- Elemzi a munkafolyamat futásokat, kiemelve a hibákat vagy teljesítményproblémákat
- Összegyűjti a biztonsági szkennelési eredményeket és priorizálja a kritikus riasztásokat
- Átfogó kiadási megjegyzéseket generál az egyesített PR-ekből kinyert információk alapján
- Akcióképes lépéseket javasol a sprint tervezéshez és kiadás előkészítéshez

**Kiemelt példa**: Imádom ezt használni kódáttekintési munkafolyamatokhoz. Ahelyett, hogy ugrálnék VS Code, GitHub értesítések és pull request oldalak között, csak annyit mondok: „Mutasd meg az összes PR-t, ami az én átnézésemre vár”, majd „Adj egy kommentet a #123 PR-hez, hogy kérdezd meg a hibakezelést a hitelesítési metódusban.” A szerver kezeli a GitHub API hívásokat, megőrzi a beszélgetés kontextusát, és még segít konstruktívabb átnézési kommenteket írni.

**Hitelesítési lehetőségek**: A szerver támogatja az OAuth-ot (zökkenőmentesen VS Code-ban) és a Personal Access Tokeneket, konfigurálható eszközkészletekkel, hogy csak a szükséges GitHub funkciókat engedélyezd. Futtathatod távoli hosztolt szolgáltatásként az azonnali beállításhoz, vagy helyben Dockerrel a teljes kontrollért.

> **💡 Profi tipp**
> 
> Engedélyezd csak a szükséges eszközkészleteket a `--toolsets` paraméterrel az MCP szerver beállításaiban, hogy csökkentsd a kontextus méretét és javítsd az AI eszközök kiválasztását. Például add hozzá a `"--toolsets", "repos,issues,pull_requests,actions"` paramétert az MCP konfigurációs argumentumaihoz az alap fejlesztési munkafolyamatokhoz, vagy használd a `"--toolsets", "notifications, security"` beállítást, ha főként GitHub figyelési funkciókra van szükséged.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mit csinál**: Csatlakozik az Azure DevOps szolgáltatásokhoz átfogó projektmenedzsment, munkatétel követés, build pipeline kezelés és repository műveletek érdekében.

**Miért hasznos**: Azoknak a csapatoknak, akik az Azure DevOps-t használják elsődleges DevOps platformként, ez az MCP szerver megszünteti a folyamatos böngészőfül váltogatást a fejlesztői környezet és az Azure DevOps webes felülete között. Munkatételeket kezelhetsz, build állapotokat ellenőrizhetsz, repository-kat kérdezhetsz le, és projektmenedzsment feladatokat végezhetsz közvetlenül az AI asszisztensed segítségével.

**Valós használat**: „Mutasd meg az összes aktív munkatételt a jelenlegi sprintben a WebApp projekthez”, „Hozz létre hibajegyet a most talált bejelentkezési problémához”, vagy „Ellenőrizd a build pipeline-ok állapotát és mutasd meg a legutóbbi hibákat”

**Kiemelt példa**: Egyszerűen ellenőrizheted a csapatod aktuális sprintjének állapotát egy egyszerű lekérdezéssel, mint például „Mutasd meg az összes aktív munkatételt a jelenlegi sprintben a WebApp projekthez” vagy „Hozz létre hibajegyet a most talált bejelentkezési problémához” anélkül, hogy elhagynád a fejlesztői környezetedet.

### 
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mit csinál**: A MarkItDown egy átfogó dokumentumkonvertáló szerver, amely különféle fájlformátumokat alakít át magas minőségű Markdown formátumba, optimalizálva LLM-fogyasztásra és szövegelemzési munkafolyamatokra.

**Miért hasznos**: Elengedhetetlen a modern dokumentációs munkafolyamatokhoz! A MarkItDown lenyűgöző mennyiségű fájlformátumot kezel, miközben megőrzi a dokumentum kritikus szerkezetét, mint például a címsorokat, listákat, táblázatokat és linkeket. Ellentétben az egyszerű szövegkinyerő eszközökkel, a hangsúlyt a szemantikai jelentés és a formázás megőrzésére helyezi, ami értékes mind az AI feldolgozás, mind az emberi olvashatóság szempontjából.

**Támogatott fájlformátumok**:
- **Office dokumentumok**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Médiafájlok**: Képek (EXIF metaadatokkal és OCR-rel), Hangfájlok (EXIF metaadatokkal és beszédfelismeréssel)
- **Webtartalom**: HTML, RSS feedek, YouTube URL-ek, Wikipédia oldalak
- **Adatformátumok**: CSV, JSON, XML, ZIP fájlok (rekurzívan feldolgozza a tartalmat)
- **Kiadói formátumok**: EPub, Jupyter jegyzetfüzetek (.ipynb)
- **E-mail**: Outlook üzenetek (.msg)
- **Fejlett**: Azure Document Intelligence integráció a PDF-ek fejlettebb feldolgozásához

**Fejlett képességek**: A MarkItDown támogatja az LLM által vezérelt képleírásokat (OpenAI kliens megléte esetén), az Azure Document Intelligence-t a fejlettebb PDF feldolgozáshoz, hangátiratot beszédtartalomhoz, valamint egy bővítményrendszert további fájlformátumok támogatására.

**Valós használat**: „Alakítsd át ezt a PowerPoint prezentációt Markdown formátumba a dokumentációs oldalunkhoz”, „Nyerd ki a szöveget ebből a PDF-ből a megfelelő címsorszerkezettel”, vagy „Alakítsd át ezt az Excel táblázatot olvasható táblázatformátumba”.

**Kiemelt példa**: A [MarkItDown dokumentációból](https://github.com/microsoft/markitdown#why-markdown) idézve:


> A Markdown rendkívül közel áll a sima szöveghez, minimális jelöléssel vagy formázással, mégis lehetőséget ad a fontos dokumentumszerkezet megjelenítésére. A főbb LLM-ek, mint például az OpenAI GPT-4o, natívan „beszélnek” Markdownul, és gyakran beépítik a Markdown-t válaszaikba ösztönzés nélkül. Ez arra utal, hogy hatalmas mennyiségű Markdown formátumú szövegen tanultak, és jól értik azt. Mellékes előnyként a Markdown konvenciók nagyon tokenhatékonyak is.

A MarkItDown igazán jól megőrzi a dokumentumszerkezetet, ami fontos az AI munkafolyamatokhoz. Például egy PowerPoint prezentáció átalakításakor megőrzi a diák szerkezetét a megfelelő címsorokkal, a táblázatokat Markdown táblázatként emeli ki, a képekhez alt szöveget ad, és még a jegyzeteket is feldolgozza. A diagramok olvasható adattáblákká alakulnak, és a végeredmény Markdown megőrzi az eredeti prezentáció logikai folyamatát. Ez tökéletessé teszi a prezentációs tartalom AI rendszerekbe való betáplálásához vagy meglévő diákról dokumentáció készítéséhez.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mit csinál**: Beszélgetés-alapú hozzáférést biztosít SQL Server adatbázisokhoz (helyi, Azure SQL vagy Fabric)

**Miért hasznos**: Hasonló a PostgreSQL szerverhez, de a Microsoft SQL ökoszisztémához. Egyszerű kapcsolati karakterlánccal csatlakozhatsz, és természetes nyelven kezdhetsz lekérdezéseket futtatni – nincs több kontextusváltás!

**Valós használat**: „Találd meg az összes megrendelést, amelyet az elmúlt 30 napban nem teljesítettek” lekérdezéseket megfelelő SQL lekérdezésekké alakítja, és formázott eredményeket ad vissza.

**Kiemelt példa**: Miután beállítottad az adatbázis-kapcsolatot, azonnal elkezdhetsz beszélgetni az adataiddal. A blogbejegyzés ezt egy egyszerű kérdéssel mutatja be: „Melyik adatbázishoz vagy csatlakozva?” Az MCP szerver a megfelelő adatbázis eszközt hívja meg, csatlakozik az SQL Server példányodhoz, és visszaadja az aktuális adatbázis-kapcsolat részleteit – mindezt egyetlen SQL sor írása nélkül. A szerver támogatja az átfogó adatbázis-műveleteket a sémakezeléstől az adatmódosításig, mindezt természetes nyelvű utasításokon keresztül. A teljes beállítási útmutatóért és konfigurációs példákért VS Code-dal és Claude Desktopdal lásd: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mit csinál**: Lehetővé teszi AI ügynökök számára, hogy weboldalakkal lépjenek interakcióba tesztelés és automatizálás céljából

> **ℹ️ A GitHub Copilot hajtómotorja**
> 
> A Playwright MCP Server hajtja a GitHub Copilot Coding Agent-jét, amely így webes böngészési képességekkel rendelkezik! [Tudj meg többet erről a funkcióról](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miért hasznos**: Tökéletes az automatizált teszteléshez, amelyet természetes nyelvű leírások vezérelnek. Az AI képes weboldalakon navigálni, űrlapokat kitölteni, és adatokat kinyerni strukturált akadálymentességi pillanatképek segítségével – ez hihetetlenül erős funkció!

**Valós használat**: „Teszteld a bejelentkezési folyamatot, és ellenőrizd, hogy a műszerfal helyesen töltődik-e be” vagy „Generálj egy tesztet, amely termékeket keres és ellenőrzi az eredményoldalt” – mindez az alkalmazás forráskódja nélkül.

**Kiemelt példa**: A csapattársam, Debbie O'Brien fantasztikus munkát végzett mostanában a Playwright MCP Serverrel! Például nemrég bemutatta, hogyan lehet teljes Playwright teszteket generálni anélkül, hogy hozzáférne az alkalmazás forráskódjához. Az ő esetében azt kérte a Copilottól, hogy készítsen egy tesztet egy filmkereső alkalmazáshoz: navigáljon az oldalra, keressen rá a „Garfield” kifejezésre, és ellenőrizze, hogy a film megjelenik-e az eredmények között. Az MCP elindított egy böngésző munkamenetet, feltérképezte az oldal szerkezetét DOM pillanatképek segítségével, megtalálta a megfelelő szelektorokat, és generált egy teljesen működő TypeScript tesztet, amely első futásra sikeres volt.

Ami igazán erőssé teszi ezt, hogy áthidalja a természetes nyelvű utasítások és a végrehajtható tesztkód közötti szakadékot. A hagyományos megközelítések vagy kézi tesztírást, vagy a kódbázishoz való hozzáférést igényelnek a kontextus miatt. A Playwright MCP-vel azonban külső oldalakat, kliensalkalmazásokat vagy feketedobozos tesztelési forgatókönyveket is tesztelhetsz, ahol nincs hozzáférés a kódhoz.

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mit csinál**: Természetes nyelven kezeli a Microsoft Dev Box környezeteket

**Miért hasznos**: Nagyon leegyszerűsíti a fejlesztői környezetek kezelését! Fejlesztői környezeteket hozhatsz létre, konfigurálhatsz és kezelhetsz anélkül, hogy meg kellene jegyezned a konkrét parancsokat.

**Valós használat**: „Állíts be egy új Dev Boxot a legfrissebb .NET SDK-val, és konfiguráld a projektünkhöz”, „Ellenőrizd az összes fejlesztői környezetem állapotát”, vagy „Hozz létre egy szabványosított demó környezetet a csapatunk bemutatóihoz”.

**Kiemelt példa**: Nagy rajongója vagyok a Dev Box személyes fejlesztésre való használatának. A „villanykörte” pillanatom akkor jött el, amikor James Montemagno elmagyarázta, milyen nagyszerű a Dev Box konferencia demókhoz, mivel szupergyors ethernet kapcsolatot biztosít, függetlenül attól, hogy milyen konferencián, szállodában vagy repülőgépen vagyok éppen wifi-n. Valójában nemrég konferencia demó gyakorlást tartottam, miközben a laptopom a telefonom hotspotjához volt csatlakoztatva, és busszal utaztam Bruges-ből Antwerpenbe! A következő lépésem az, hogy mélyebben beleássam magam a több fejlesztői környezetet kezelő csapatokba és a szabványosított demó környezetekbe. Egy másik nagy felhasználási eset, amit ügyfelektől és kollégáktól hallottam, természetesen a Dev Box előre konfigurált fejlesztői környezetként való használata. Mindkét esetben az MCP használata a Dev Boxok konfigurálásához és kezeléséhez lehetővé teszi a természetes nyelvű interakciót, miközben a fejlesztői környezetben maradsz.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Mit csinál**: Az Azure AI Foundry MCP Server átfogó hozzáférést biztosít a fejlesztők számára az Azure AI ökoszisztémájához, beleértve a modellkatalógusokat, a telepítéskezelést, a tudásindexelést az Azure AI Search segítségével, valamint az értékelő eszközöket. Ez a kísérleti szerver hidat képez az AI fejlesztés és az Azure erőteljes AI infrastruktúrája között, megkönnyítve az AI alkalmazások építését, telepítését és értékelését.

**Miért hasznos**: Ez a szerver átalakítja az Azure AI szolgáltatásokkal való munkát azáltal, hogy vállalati szintű AI képességeket hoz közvetlenül a fejlesztési munkafolyamatba. Ahelyett, hogy az Azure portál, a dokumentáció és az IDE között váltogatnál, felfedezheted a modelleket, telepíthetsz szolgáltatásokat, kezelheted a tudásbázisokat, és értékelheted az AI teljesítményét természetes nyelvű parancsok segítségével. Különösen hasznos fejlesztőknek, akik RAG (Retrieval-Augmented Generation) alkalmazásokat építenek, többmodell telepítést kezelnek, vagy átfogó AI értékelési folyamatokat valósítanak meg.

**Fő fejlesztői képességek**:
- **🔍 Modellfelfedezés és telepítés**: Böngészd az Azure AI Foundry modellkatalógusát, kapj részletes modellinformációkat kódpéldákkal, és telepíts modelleket az Azure AI szolgáltatásokra
- **📚 Tudáskezelés**: Hozz létre és kezelj Azure AI Search indexeket, adj hozzá dokumentumokat, konfiguráld az indexelőket, és építs kifinomult RAG rendszereket
- **⚡ AI ügynök integráció**: Kapcsolódj Azure AI ügynökökhöz, kérdezd le a meglévő ügynököket, és értékeld az ügynökök teljesítményét éles környezetben
- **📊 Értékelési keretrendszer**: Futtass átfogó szöveg- és ügynökértékeléseket, generálj markdown jelentéseket, és valósíts meg minőségbiztosítást AI alkalmazásokhoz
- **🚀 Prototípus-készítő eszközök**: Szerezz beállítási útmutatókat GitHub-alapú prototípusokhoz, és férj hozzá az Azure AI Foundry Labs legújabb kutatási modelljeihez

**Valós fejlesztői használat**: „Telepíts egy Phi-4 modellt az Azure AI Services-re az alkalmazásomhoz”, „Hozz létre egy új keresési indexet a dokumentációm RAG rendszeréhez”, „Értékeld az ügynököm válaszait minőségi mutatók alapján”, vagy „Találd meg a legjobb érvelő modellt a komplex elemzési feladataimhoz”

**Teljes demó forgatókönyv**: Íme egy hatékony AI fejlesztési munkafolyamat:


> „Ügyfélszolgálati ügynököt építek. Segíts találni egy jó érvelő modellt a katalógusból, telepítsd az Azure AI Services-re, hozz létre egy tudásbázist a dokumentációból, állíts be egy értékelési keretrendszert a válaszok minőségének tesztelésére, majd segíts a GitHub tokenes integráció prototípusának elkészítésében a teszteléshez.”

Az Azure AI Foundry MCP Server:
- Lekérdezi a modellkatalógust, hogy az igényeid alapján ajánljon optimális érvelő modelleket
- Megadja a telepítési parancsokat és kvóta-információkat a preferált Azure régióhoz
- Beállítja az Azure AI Search indexeket a dokumentációd megfelelő sémájával
- Konfigurálja az értékelési folyamatokat minőségi mutatókkal és biztonsági ellenőrzésekkel
- Generál prototípus kódot GitHub hitelesítéssel az azonnali teszteléshez
- Átfogó beállítási útmutatókat nyújt a technológiai környezetedhez igazítva

**Kiemelt példa**: Fejlesztőként nehezen tartottam lépést a különböző LLM modellekkel. Ismerek néhány fő modellt, de úgy éreztem, hogy kimaradok bizonyos termelékenységi és hatékonysági előnyökből. A tokenek és kvóták kezelése stresszes és bonyolult – sosem tudom, hogy a megfelelő modellt választom-e a megfelelő feladathoz, vagy csak pazarlom a költségvetésemet. Most hallottam erről az MCP Serverről James Montemagnótól, miközben a csapattársaimmal beszélgettem MCP Server ajánlásokról, és izgatott vagyok, hogy kipróbáljam! A modellfelfedezési képességek különösen lenyűgözőek számomra, aki szeretnék a szokásos modelleken túl is felfedezni, és olyan modelleket találni, amelyek adott feladatokra optimalizáltak. Az értékelési keretrendszer segíthet megerősíteni, hogy valóban jobb eredményeket érek el, nem csak azért próbálok ki valamit, mert új.

> **ℹ️ Kísérleti állapot**
> 
> Ez az MCP szerver kísérleti jellegű és aktív fejlesztés alatt áll. A funkciók és API-k változhatnak. Kiváló az Azure AI képességek felfedezésére és prototípusok építésére, de a stabilitási követelményeket érdemes ellenőrizni éles használat előtt.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Mit csinál**: Alapvető eszközöket biztosít fejlesztőknek AI ügynökök és alkalmazások építéséhez, amelyek integrálódnak a Microsoft 365-tel és a Microsoft 365 Copilottal, beleértve a sémaellenőrzést, kódpéldák lekérését és hibakeresési segítséget.

**Miért hasznos**: A Microsoft 365 és Copilot fejlesztése összetett manifest sémákat és speciális fejlesztési mintákat igényel. Ez az MCP szerver közvetlenül a fejlesztési környezetedbe hozza az alapvető fejlesztői erőforrásokat, segítve a sémák ellenőrzését, kódpéldák megtalálását és a gyakori problémák hibakeresését anélkül, hogy folyamatosan a dokumentációt kellene böngészned.

**Valós használat**: „Ellenőrizd a deklaratív ügynök manifestemet, és javítsd a sémahíreket”, „Mutass példakódot Microsoft Graph API plugin megvalósításához”, vagy „Segíts a Teams alkalmazás hitelesítési problémáinak hibakeresésében”

**Kiemelt példa**: Felvettem a kapcsolatot a barátommal, John Millerrel, miután a Build konferencián beszélgettünk az M365 ügynökökről, és ő ezt az MCP-t ajánlotta. Ez nagyszerű lehet azoknak a fejlesztőknek, akik újak az M365 ügynökök világában, mert sablonokat, példakódokat és keretrendszert kínál, hogy elinduljanak anélkül, hogy elmerülnének a dokumentációban. A sémaellenőrző funkciók különösen hasznosak a manifest struktúra hibák elkerülésére, amelyek órákig tartó hibakeresést okozhatnak.

> **💡 Pro Tipp**
> 
> Használd ezt a szervert együtt a Microsoft Learn Docs MCP Serverrel a teljes körű M365 fejlesztői támogatásért – az egyik az hivatalos dokumentációt nyújtja, míg ez a gyakorlati fejlesztői eszközöket és hibakeresési segítséget kínál.

## Mi következik? 🔮

## 📋 Összefoglalás

A Model Context Protocol (MCP) átalakítja, hogyan lépnek kapcsolatba a fejlesztők AI asszisztensekkel és külső eszközökkel. Ezek a 10 Microsoft MCP szerver bemutatják a szabványosított AI integráció erejét, lehetővé téve zökkenőmentes munkafolyamatokat, amelyek fenntartják a fejlesztők fókuszát, miközben hozzáférnek erőteljes külső képességekhez.

Az átfogó Azure ökoszisztéma integrációtól kezdve a speciális eszközökig, mint a Playwright böngésző automatizáláshoz vagy a MarkItDown dokumentumfeldolgozáshoz, ezek a szerverek megmutatják, hogyan növelheti az MCP a termelékenységet különféle fejlesztési helyzetekben. A szabványosított protokoll biztosítja, hogy ezek az eszközök zökkenőmentesen működjenek együtt, egységes fejlesztői élményt teremtve.

Ahogy az MCP ökoszisztéma fejlődik, a közösséggel való aktív részvétel, az új szerverek felfedezése és egyedi megoldások építése kulcsfontosságú lesz a fejlesztői termelékenység maximalizálásához. Az MCP nyílt szabvány jellege lehetővé teszi, hogy különböző gyártók eszközeit kombináld, és megalkosd a számodra tökéletes munkafolyamatot.

## 🔗 További források

- [Hivatalos Microsoft MCP tárhely](https://github.com/microsoft/mcp)
- [MCP közösség és dokumentáció](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentáció](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentáció](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentáció](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP események](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot testreszabások](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days élőben július 29-30 vagy visszanézhető](https://aka.ms/mcpdevdays)

## 🎯 Gyakorlatok

1. **Telepítés és konfiguráció**: Állíts be egy MCP szervert a VS Code környezetedben, és teszteld az alapfunkciókat.
2. **Munkafolyamat integráció**: Tervezd meg egy fejlesztési munkafolyamatot, amely legalább három különböző MCP szervert kombinál.
3. **Egyedi szerver tervezés**: Azonosíts egy feladatot a napi fejlesztési rutinodban, amely profitálhatna egy egyedi MCP szerverből, és készíts hozzá specifikációt.
4. **Teljesítmény elemzés**: Hasonlítsd össze az MCP szerverek használatának hatékonyságát a hagyományos megközelítésekkel a gyakori fejlesztési feladatok esetén.
5. **Biztonsági értékelés**: Értékeld az MCP szerverek használatának biztonsági vonatkozásait a fejlesztési környezetedben, és javasolj legjobb gyakorlatokat.

Következő: [Best Practices](../08-BestPractices/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.