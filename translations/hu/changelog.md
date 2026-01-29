# Változásnapló: MCP kezdőknek tananyag

Ez a dokumentum a Model Context Protocol (MCP) kezdőknek szóló tananyagában történt jelentős változások nyilvántartására szolgál. A változások fordított időrendi sorrendben vannak dokumentálva (legújabb változások elöl).

## 2025. december 18.

### Biztonsági dokumentáció frissítése - MCP specifikáció 2025-11-25

#### MCP biztonsági legjobb gyakorlatok (02-Security/mcp-best-practices.md) - Specifikáció verzió frissítés
- **Protokoll verzió frissítés**: Frissítve a legújabb MCP specifikáció 2025-11-25 hivatkozására (2025. november 25-én kiadva)
  - Minden specifikáció verzió hivatkozás frissítve 2025-06-18-ról 2025-11-25-re
  - Dokumentum dátum hivatkozások frissítve 2025. augusztus 18-ról 2025. december 18-ra
  - Ellenőrizve, hogy minden specifikáció URL a jelenlegi dokumentációra mutat
- **Tartalom validálás**: Átfogó validálás a biztonsági legjobb gyakorlatokról a legújabb szabványok szerint
  - **Microsoft biztonsági megoldások**: Ellenőrizve a jelenlegi terminológia és linkek a Prompt Shields (korábban "Jailbreak kockázat észlelés"), Azure Content Safety, Microsoft Entra ID és Azure Key Vault esetében
  - **OAuth 2.1 biztonság**: Megerősítve az összhang a legújabb OAuth biztonsági legjobb gyakorlatokkal
  - **OWASP szabványok**: Validálva, hogy az OWASP Top 10 LLM-ekre vonatkozó hivatkozások naprakészek
  - **Azure szolgáltatások**: Ellenőrizve minden Microsoft Azure dokumentációs link és legjobb gyakorlat
- **Szabványoknak való megfelelés**: Minden hivatkozott biztonsági szabvány megerősítve, hogy aktuális
  - NIST AI Kockázatkezelési Keretrendszer
  - ISO 27001:2022
  - OAuth 2.1 biztonsági legjobb gyakorlatok
  - Azure biztonsági és megfelelőségi keretrendszerek
- **Megvalósítási források**: Ellenőrizve minden megvalósítási útmutató link és erőforrás
  - Azure API Management hitelesítési minták
  - Microsoft Entra ID integrációs útmutatók
  - Azure Key Vault titkok kezelése
  - DevSecOps pipeline-ok és megfigyelési megoldások

### Dokumentáció minőségbiztosítás
- **Specifikációnak való megfelelés**: Biztosítva, hogy minden kötelező MCP biztonsági követelmény (KELL/NEM KELL) összhangban legyen a legújabb specifikációval
- **Források naprakészsége**: Ellenőrizve minden külső link Microsoft dokumentációra, biztonsági szabványokra és megvalósítási útmutatókra
- **Legjobb gyakorlatok lefedettsége**: Megerősítve az átfogó lefedettség az autentikáció, autorizáció, AI-specifikus fenyegetések, ellátási lánc biztonság és vállalati minták terén

## 2025. október 6.

### Kezdő szakasz bővítése – Haladó szerverhasználat és egyszerű hitelesítés

#### Haladó szerverhasználat (03-GettingStarted/10-advanced)
- **Új fejezet hozzáadva**: Átfogó útmutató a haladó MCP szerverhasználathoz, beleértve a hagyományos és alacsony szintű szerverarchitektúrákat.
  - **Hagyományos vs. alacsony szintű szerver**: Részletes összehasonlítás és kódpéldák Pythonban és TypeScriptben mindkét megközelítéshez.
  - **Handler-alapú tervezés**: Magyarázat a handler-alapú eszköz/erőforrás/prompt kezelésről a skálázható, rugalmas szervermegvalósításokhoz.
  - **Gyakorlati minták**: Valós példák, ahol az alacsony szintű szerver minták előnyösek haladó funkciók és architektúra esetén.

#### Egyszerű hitelesítés (03-GettingStarted/11-simple-auth)
- **Új fejezet hozzáadva**: Lépésről lépésre útmutató egyszerű hitelesítés megvalósításához MCP szervereken.
  - **Hitelesítési fogalmak**: Világos magyarázat az autentikáció és autorizáció közötti különbségről, valamint a hitelesítő adatok kezeléséről.
  - **Alapvető hitelesítés megvalósítása**: Middleware-alapú hitelesítési minták Pythonban (Starlette) és TypeScriptben (Express), kódpéldákkal.
  - **Haladó biztonság felé haladás**: Útmutatás az egyszerű hitelesítésről az OAuth 2.1 és RBAC felé, hivatkozásokkal a haladó biztonsági modulokra.

Ezek a kiegészítések gyakorlati, kézzelfogható útmutatást nyújtanak a robusztusabb, biztonságosabb és rugalmasabb MCP szervermegvalósítások építéséhez, hidat képezve az alapfogalmak és a haladó gyártási minták között.

## 2025. szeptember 29.

### MCP szerver adatbázis integrációs laborok – Átfogó gyakorlati tanulási út

#### 11-MCPServerHandsOnLabs – Új teljes adatbázis integrációs tananyag
- **Teljes 13 laboros tanulási út**: Átfogó gyakorlati tananyag hozzáadva gyártásra kész MCP szerverek építéséhez PostgreSQL adatbázis integrációval
  - **Valós megvalósítás**: Zava Retail elemzési esettanulmány vállalati szintű mintákkal
  - **Strukturált tanulási előrehaladás**:
    - **Laborok 00-03: Alapok** – Bevezetés, alap architektúra, biztonság és multi-tenancy, környezet beállítása
    - **Laborok 04-06: MCP szerver építése** – Adatbázis tervezés és séma, MCP szerver megvalósítás, eszközfejlesztés
    - **Laborok 07-09: Haladó funkciók** – Szemantikus keresés integráció, tesztelés és hibakeresés, VS Code integráció
    - **Laborok 10-12: Gyártás és legjobb gyakorlatok** – Telepítési stratégiák, megfigyelés és megfigyelhetőség, legjobb gyakorlatok és optimalizáció
  - **Vállalati technológiák**: FastMCP keretrendszer, PostgreSQL pgvector-rel, Azure OpenAI beágyazások, Azure Container Apps, Application Insights
  - **Haladó funkciók**: Sor szintű biztonság (RLS), szemantikus keresés, multi-tenant adat-hozzáférés, vektor beágyazások, valós idejű megfigyelés

#### Terminológia szabványosítás – Modulról laborra váltás
- **Átfogó dokumentáció frissítés**: Minden README fájl a 11-MCPServerHandsOnLabs könyvtárban rendszeresen frissítve, hogy a "Modul" helyett "Labor" terminológiát használjon
  - **Szakaszfejlécek**: "Mit fed le ez a modul" frissítve "Mit fed le ez a labor" minden 13 laborban
  - **Tartalom leírása**: "Ez a modul biztosítja..." módosítva "Ez a labor biztosítja..." mindenhol
  - **Tanulási célok**: "A modul végére..." frissítve "A labor végére..."
  - **Navigációs hivatkozások**: Minden "Modul XX:" hivatkozás "Labor XX:"-ra módosítva kereszt-hivatkozásokban és navigációban
  - **Teljesítési nyomon követés**: "A modul befejezése után..." frissítve "A labor befejezése után..."
  - **Megőrzött technikai hivatkozások**: Python modul hivatkozások megőrizve konfigurációs fájlokban (pl. `"module": "mcp_server.main"`)

#### Tanulási útmutató fejlesztése (study_guide.md)
- **Vizualizált tananyag térkép**: Új "11. Adatbázis integrációs laborok" szakasz hozzáadva átfogó labor struktúra vizualizációval
- **Tároló struktúra**: Frissítve tízről tizenegy fő szakaszra, részletes 11-MCPServerHandsOnLabs leírással
- **Tanulási útmutatás**: Navigációs utasítások bővítve a 00-11 szakaszokra
- **Technológiai lefedettség**: FastMCP, PostgreSQL, Azure szolgáltatások integráció részletezve
- **Tanulási eredmények**: Kiemelve a gyártásra kész szerverfejlesztést, adatbázis integrációs mintákat és vállalati biztonságot

#### Fő README struktúra fejlesztése
- **Labor-alapú terminológia**: A 11-MCPServerHandsOnLabs fő README.md fájlja egységesen "Labor" struktúrát használ
- **Tanulási út szervezése**: Világos előrehaladás az alapfogalmaktól a haladó megvalósításon át a gyártásba helyezésig
- **Valós fókusz**: Gyakorlati, kézzelfogható tanulás vállalati szintű mintákkal és technológiákkal

### Dokumentáció minőség és konzisztencia javítások
- **Gyakorlati tanulás hangsúlyozása**: Erősített labor-alapú megközelítés az egész dokumentációban
- **Vállalati minták fókusza**: Kiemelt gyártásra kész megvalósítások és vállalati biztonsági szempontok
- **Technológiai integráció**: Átfogó lefedettség a modern Azure szolgáltatások és AI integrációs minták terén
- **Tanulási előrehaladás**: Világos, strukturált út az alapfogalmaktól a gyártásba helyezésig

## 2025. szeptember 26.

### Esettanulmányok bővítése – GitHub MCP Registry integráció

#### Esettanulmányok (09-CaseStudy/) – Ökoszisztéma fejlesztési fókusz
- **README.md**: Jelentős bővítés átfogó GitHub MCP Registry esettanulmánnyal
  - **GitHub MCP Registry esettanulmány**: Új átfogó esettanulmány a GitHub MCP Registry 2025 szeptemberi indításáról
    - **Probléma elemzés**: Részletes vizsgálat a fragmentált MCP szerver felfedezés és telepítés kihívásairól
    - **Megoldás architektúra**: GitHub központosított regisztrációs megközelítése egykattintásos VS Code telepítéssel
    - **Üzleti hatás**: Mérhető javulás a fejlesztői onboarding és termelékenység terén
    - **Stratégiai érték**: Moduláris ügynök telepítés és eszközök közötti interoperabilitás fókusz
    - **Ökoszisztéma fejlesztés**: Alapvető platformként pozícionálva az ügynöki integrációhoz
  - **Esettanulmány struktúra fejlesztése**: Minden hét esettanulmány egységes formázással és átfogó leírással frissítve
    - Azure AI utazási ügynökök: Több ügynök összehangolás hangsúlyozása
    - Azure DevOps integráció: Munkafolyamat automatizálás fókusz
    - Valós idejű dokumentáció lekérés: Python konzol kliens megvalósítás
    - Interaktív tanulási terv generátor: Chainlit beszélgetős webalkalmazás
    - Szerkesztőben dokumentáció: VS Code és GitHub Copilot integráció
    - Azure API Management: Vállalati API integrációs minták
    - GitHub MCP Registry: Ökoszisztéma fejlesztés és közösségi platform
  - **Átfogó összefoglaló**: Újraírt összefoglaló rész, amely kiemeli a hét esettanulmányt, amelyek több MCP megvalósítási dimenziót fednek le
    - Vállalati integráció, több ügynök összehangolás, fejlesztői termelékenység
    - Ökoszisztéma fejlesztés, oktatási alkalmazások kategorizálása
    - Mélyebb betekintés az architekturális mintákba, megvalósítási stratégiákba és legjobb gyakorlatokba
    - Kiemelve az MCP-t mint érett, gyártásra kész protokollt

#### Tanulási útmutató frissítések (study_guide.md)
- **Vizualizált tananyag térkép**: Frissítve a gondolattérkép, hogy tartalmazza a GitHub MCP Registry-t az Esettanulmányok szakaszban
- **Esettanulmányok leírása**: Általános leírásokról részletes bontásra bővítve a hét átfogó esettanulmányról
- **Tároló struktúra**: Frissítve a 10. szakasz, hogy tükrözze az átfogó esettanulmány lefedettséget konkrét megvalósítási részletekkel
- **Változásnapló integráció**: Hozzáadva 2025. szeptember 26-i bejegyzés a GitHub MCP Registry hozzáadásáról és esettanulmány fejlesztésekről
- **Dátum frissítések**: Lábléc időbélyeg frissítve a legutóbbi felülvizsgálatra (2025. szeptember 26.)

### Dokumentáció minőség javítások
- **Konzisztencia javítása**: Esettanulmány formázás és struktúra egységesítve mind a hét példánál
- **Átfogó lefedettség**: Esettanulmányok lefedik a vállalati, fejlesztői termelékenységi és ökoszisztéma fejlesztési forgatókönyveket
- **Stratégiai pozicionálás**: Fókuszáltabb MCP mint alapvető platform az ügynöki rendszer telepítéshez
- **Forrás integráció**: Frissített további források között a GitHub MCP Registry link

## 2025. szeptember 15.

### Haladó témák bővítése – Egyedi transzportok és kontextus mérnökség

#### MCP egyedi transzportok (05-AdvancedTopics/mcp-transport/) – Új haladó megvalósítási útmutató
- **README.md**: Teljes megvalósítási útmutató egyedi MCP transzport mechanizmusokhoz
  - **Azure Event Grid transzport**: Átfogó szerver nélküli eseményvezérelt transzport megvalósítás
    - C#, TypeScript és Python példák Azure Functions integrációval
    - Eseményvezérelt architektúra minták skálázható MCP megoldásokhoz
    - Webhook fogadók és push-alapú üzenetkezelés
  - **Azure Event Hubs transzport**: Nagy áteresztőképességű streaming transzport megvalósítás
    - Valós idejű streaming képességek alacsony késleltetésű forgatókönyvekhez
    - Particionálási stratégiák és checkpoint kezelés
    - Üzenetcsomagolás és teljesítmény optimalizáció
  - **Vállalati integrációs minták**: Gyártásra kész architekturális példák
    - Elosztott MCP feldolgozás több Azure Functions között
    - Hibrid transzport architektúrák több transzport típus kombinálásával
    - Üzenet tartósság, megbízhatóság és hibakezelési stratégiák
  - **Biztonság és megfigyelés**: Azure Key Vault integráció és megfigyelhetőségi minták
    - Kezelt identitás alapú hitelesítés és legkisebb jogosultság elve
    - Application Insights telemetria és teljesítmény megfigyelés
    - Áramkör megszakítók és hibabiztos minták
  - **Tesztelési keretrendszerek**: Átfogó tesztelési stratégiák egyedi transzportokhoz
    - Egységtesztelés teszt duplikátumokkal és mock keretrendszerekkel
    - Integrációs tesztelés Azure Test Containers használatával
    - Teljesítmény- és terheléses tesztelési szempontok

#### Kontextus mérnökség (05-AdvancedTopics/mcp-contextengineering/) – Felmerülő AI tudományág
- **README.md**: Átfogó feltárás a kontextus mérnökségről mint felmerülő területről
  - **Alapelvek**: Teljes kontextus megosztás, cselekvési döntés tudatosság, kontextus ablak kezelése
  - **MCP protokoll összhang**: Hogyan kezeli az MCP a kontextus mérnökség kihívásait
    - Kontextus ablak korlátok és progresszív betöltési stratégiák
    - Relevancia meghatározás és dinamikus kontextus lekérés
    - Többmodalitású kontextus kezelés és biztonsági szempontok
  - **Megvalósítási megközelítések**: Egyszálú vs. több ügynök architektúrák
    - Kontextus darabolás és prioritizálási technikák
    - Progresszív kontextus betöltés és tömörítési stratégiák
    - Rétegzett kontextus megközelítések és lekérdezés optimalizáció
  - **Mérési keretrendszer**: Felmerülő metrikák a kontextus hatékonyság értékelésére
    - Bemeneti hatékonyság, teljesítmény, minőség és felhasználói élmény szempontok
    - Kísérleti megközelítések a kontextus optimalizációhoz
    - Hibaanalízis és fejlesztési módszertanok

#### Tananyag navigáció frissítések (README.md)
- **Fejlesztett modul struktúra**: Tananyag táblázat frissítve az új haladó témákkal
  - Hozzáadva Kontextus mérnökség (5.14) és Egyedi transzport (5.15) bejegyzések
  - Egységes formázás és navigációs linkek minden modulban
  - Leírások frissítve a jelenlegi tartalomkörnek megfelelően

### Könyvtár struktúra fejlesztések
- **Név szabványosítás**: Az "mcp transport" átnevezve "mcp-transport"-ra az egységesség érdekében a többi haladó téma mappával
- **Tartalom szervezés**: Minden 05-AdvancedTopics mappa most egységes névformátumot követ (mcp-[téma])

### Dokumentáció minőség fejlesztések
- **MCP specifikáció összhang**: Minden új tartalom a jelenlegi MCP specifikáció 2025-06-18 hivatkozásával
- **Többnyelvű példák**: Átfogó kódpéldák C#, TypeScript és Python nyelveken
- **Vállalati fókusz**: Gyártásra kész minták és Azure felhő integráció mindenütt
- **Vizualizált dokumentáció**: Mermaid diagramok az architektúra és folyamatok szemléltetésére

## 2025. augusztus 18.

### Dokumentáció átfogó frissítése – MCP 2025-06-18 szabványok

#### MCP biztonsági legjobb gyakorlatok (02-Security/) – Teljes modernizáció
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Teljes átírás az MCP specifikáció 2025-06-18 összhangjában
  - **Kötelező követelmények**: Hivatalos specifikációból származó egyértelműen jelzett KELL/NEM KELL követelmények hozzáadva
  - **12 alapvető biztonsági gyakorlat**: 15 elemes listából átalakítva átfogó biztonsági területekre
    - Token biztonság és hitelesítés külső identitásszolgáltató integrációval
    - Munkamenet-kezelés és szállítási biztonság kriptográfiai követelményekkel
    - AI-specifikus fenyegetésvédelem Microsoft Prompt Shields integrációval
    - Hozzáférés-vezérlés és jogosultságok a legkisebb jogosultság elvével
    - Tartalombiztonság és megfigyelés Azure Content Safety integrációval
    - Ellátási lánc biztonság átfogó komponens-ellenőrzéssel
    - OAuth biztonság és Confused Deputy megelőzés PKCE megvalósítással
    - Incidens válasz és helyreállítás automatizált képességekkel
    - Megfelelőség és irányítás szabályozási összhanggal
    - Fejlett biztonsági vezérlők zéró bizalom architektúrával
    - Microsoft biztonsági ökoszisztéma integráció átfogó megoldásokkal
    - Folyamatos biztonsági fejlődés adaptív gyakorlatokkal
  - **Microsoft biztonsági megoldások**: Fejlesztett integrációs útmutató Prompt Shields, Azure Content Safety, Entra ID és GitHub Advanced Security számára
  - **Megvalósítási források**: Átfogó forráslinkek kategorizálva Hivatalos MCP dokumentáció, Microsoft biztonsági megoldások, biztonsági szabványok és megvalósítási útmutatók szerint

#### Fejlett biztonsági vezérlők (02-Security/) - Vállalati megvalósítás
- **MCP-SECURITY-CONTROLS-2025.md**: Teljes átdolgozás vállalati szintű biztonsági keretrendszerrel
  - **9 átfogó biztonsági terület**: Alapvető vezérlőkből kibővítve részletes vállalati keretrendszerre
    - Fejlett hitelesítés és engedélyezés Microsoft Entra ID integrációval
    - Token biztonság és anti-passthrough vezérlők átfogó érvényesítéssel
    - Munkamenet biztonsági vezérlők eltérítés elleni védelemmel
    - AI-specifikus biztonsági vezérlők prompt injekció és eszközmérgezés elleni védelemmel
    - Confused Deputy támadás megelőzés OAuth proxy biztonsággal
    - Eszköz végrehajtási biztonság sandboxinggal és izolációval
    - Ellátási lánc biztonsági vezérlők függőségellenőrzéssel
    - Megfigyelési és észlelési vezérlők SIEM integrációval
    - Incidens válasz és helyreállítás automatizált képességekkel
  - **Megvalósítási példák**: Részletes YAML konfigurációs blokkok és kódpéldák hozzáadva
  - **Microsoft megoldások integrációja**: Átfogó lefedettség Azure biztonsági szolgáltatásokkal, GitHub Advanced Security-vel és vállalati identitáskezeléssel

#### Fejlett témák biztonsága (05-AdvancedTopics/mcp-security/) - Termelésre kész megvalósítás
- **README.md**: Teljes átírás vállalati biztonsági megvalósításhoz
  - **Aktuális specifikáció szerinti összhang**: Frissítve MCP Specifikáció 2025-06-18 szerint kötelező biztonsági követelményekkel
  - **Fejlesztett hitelesítés**: Microsoft Entra ID integráció átfogó .NET és Java Spring Security példákkal
  - **AI biztonsági integráció**: Microsoft Prompt Shields és Azure Content Safety megvalósítás részletes Python példákkal
  - **Fejlett fenyegetéscsökkentés**: Átfogó megvalósítási példák
    - Confused Deputy támadás megelőzés PKCE és felhasználói hozzájárulás érvényesítéssel
    - Token passthrough megelőzés audience érvényesítéssel és biztonságos token kezeléssel
    - Munkamenet eltérítés megelőzés kriptográfiai kötés és viselkedéselemzés segítségével
  - **Vállalati biztonsági integráció**: Azure Application Insights megfigyelés, fenyegetésészlelési folyamatok és ellátási lánc biztonság
  - **Megvalósítási ellenőrzőlista**: Egyértelmű kötelező és ajánlott biztonsági vezérlők Microsoft biztonsági ökoszisztéma előnyeivel

### Dokumentáció minősége és szabványoknak való megfelelés
- **Specifikáció hivatkozások**: Minden hivatkozás frissítve az aktuális MCP Specifikáció 2025-06-18-ra
- **Microsoft biztonsági ökoszisztéma**: Fejlesztett integrációs útmutatás minden biztonsági dokumentációban
- **Gyakorlati megvalósítás**: Részletes kódpéldák hozzáadva .NET, Java és Python nyelveken vállalati mintákkal
- **Források rendszerezése**: Átfogó kategorizálás hivatalos dokumentáció, biztonsági szabványok és megvalósítási útmutatók szerint
- **Vizuális jelölések**: Egyértelmű jelölés kötelező követelmények és ajánlott gyakorlatok között


#### Alapfogalmak (01-CoreConcepts/) - Teljes modernizáció
- **Protokoll verzió frissítés**: Frissítve az aktuális MCP Specifikáció 2025-06-18 dátumalapú verziózásával (ÉÉÉÉ-HH-NN formátum)
- **Architektúra finomítás**: Fejlesztett leírások a Hostokról, Kliensekről és Szerverekről az aktuális MCP architektúra minták szerint
  - Hostok most egyértelműen AI alkalmazásokként definiálva, amelyek több MCP kliens kapcsolatot koordinálnak
  - Kliensek protokoll csatlakozóként leírva, egy-egy szerver kapcsolatot fenntartva
  - Szerverek fejlesztve helyi és távoli telepítési forgatókönyvekkel
- **Primitívek átalakítása**: Teljes átdolgozás szerver és kliens primitívekből
  - Szerver primitívek: Erőforrások (adatforrások), Promptok (sablonok), Eszközök (végrehajtható funkciók) részletes magyarázatokkal és példákkal
  - Kliens primitívek: Mintavételezés (LLM kimenetek), Kiváltás (felhasználói bemenet), Naplózás (hibakeresés/megfigyelés)
  - Frissítve az aktuális felfedezési (`*/list`), lekérési (`*/get`) és végrehajtási (`*/call`) metódusmintákkal
- **Protokoll architektúra**: Bevezetve kétszintű architektúra modell
  - Adat réteg: JSON-RPC 2.0 alapok életciklus-kezeléssel és primitívekkel
  - Szállítási réteg: STDIO (helyi) és Streamable HTTP SSE-vel (távoli) szállítási mechanizmusok
- **Biztonsági keretrendszer**: Átfogó biztonsági elvek, beleértve egyértelmű felhasználói hozzájárulást, adatvédelmet, eszköz végrehajtási biztonságot és szállítási réteg biztonságot
- **Kommunikációs minták**: Frissített protokoll üzenetek inicializáció, felfedezés, végrehajtás és értesítés folyamatokkal
- **Kódpéldák**: Frissített többnyelvű példák (.NET, Java, Python, JavaScript) az aktuális MCP SDK minták szerint

#### Biztonság (02-Security/) - Átfogó biztonsági átdolgozás  
- **Szabványoknak való megfelelés**: Teljes összhang az MCP Specifikáció 2025-06-18 biztonsági követelményeivel
- **Hitelesítés fejlődése**: Dokumentált fejlődés egyedi OAuth szerverektől külső identitásszolgáltató delegációig (Microsoft Entra ID)
- **AI-specifikus fenyegetéselemzés**: Fejlesztett lefedettség a modern AI támadási vektorokra
  - Részletes prompt injekció támadási forgatókönyvek valós példákkal
  - Eszközmérgezési mechanizmusok és "rug pull" támadási minták
  - Kontextusablak mérgezés és modellzavar támadások
- **Microsoft AI biztonsági megoldások**: Átfogó lefedettség a Microsoft biztonsági ökoszisztémában
  - AI Prompt Shields fejlett észlelési, kiemelési és elválasztó technikákkal
  - Azure Content Safety integrációs minták
  - GitHub Advanced Security az ellátási lánc védelmére
- **Fejlett fenyegetéscsökkentés**: Részletes biztonsági vezérlők
  - Munkamenet eltérítés MCP-specifikus támadási forgatókönyvekkel és kriptográfiai munkamenet azonosító követelményekkel
  - Confused Deputy problémák MCP proxy forgatókönyvekben egyértelmű hozzájárulási követelményekkel
  - Token passthrough sérülékenységek kötelező érvényesítési vezérlőkkel
- **Ellátási lánc biztonság**: Kibővített AI ellátási lánc lefedettség alapmodellekkel, beágyazási szolgáltatásokkal, kontextus szolgáltatókkal és harmadik féltől származó API-kkal
- **Alapbiztonság**: Fejlesztett integráció vállalati biztonsági mintákkal, beleértve zéró bizalom architektúrát és Microsoft biztonsági ökoszisztémát
- **Források rendszerezése**: Átfogó forráslinkek kategorizálva típus szerint (Hivatalos dokumentumok, szabványok, kutatás, Microsoft megoldások, megvalósítási útmutatók)

### Dokumentáció minőségjavítások
- **Strukturált tanulási célok**: Fejlesztett tanulási célok specifikus, végrehajtható eredményekkel
- **Kereszthivatkozások**: Kapcsolódó biztonsági és alapfogalmi témák közötti linkek hozzáadva
- **Aktuális információk**: Minden dátumhivatkozás és specifikációs link frissítve az aktuális szabványokra
- **Megvalósítási útmutatás**: Specifikus, végrehajtható megvalósítási iránymutatások hozzáadva mindkét szakaszban

## 2025. július 16.

### README és navigációs fejlesztések
- Teljesen áttervezett tananyag navigáció a README.md-ben
- `<details>` tagek helyett könnyebben hozzáférhető táblázatos formátum
- Alternatív elrendezési lehetőségek létrehozása az új "alternative_layouts" mappában
- Kártya-alapú, fülös és harmonika stílusú navigációs példák hozzáadva
- A tárház struktúra szakasz frissítve az összes legújabb fájlra
- A "Hogyan használd ezt a tananyagot" szakasz fejlesztve egyértelmű ajánlásokkal
- MCP specifikáció linkek frissítve a helyes URL-ekre
- Kontextus mérnökség szakasz (5.14) hozzáadva a tananyag struktúrához

### Tanulmányi útmutató frissítések
- Teljesen átdolgozott tanulmányi útmutató az aktuális tárház struktúrához igazítva
- Új szakaszok hozzáadva MCP kliensek és eszközök, valamint népszerű MCP szerverek témakörében
- Vizualizált tananyag térkép frissítve az összes témakör pontos megjelenítéséhez
- Fejlett témák leírásainak fejlesztése az összes speciális terület lefedésére
- Esettanulmányok szakasz frissítve valós példák alapján
- Ez az átfogó változásnapló hozzáadva

### Közösségi hozzájárulások (06-CommunityContributions/)
- Részletes információk hozzáadva MCP szerverekről képgeneráláshoz
- Átfogó szakasz Claude használatáról VSCode-ban
- Cline terminál kliens beállítási és használati útmutató hozzáadva
- MCP kliens szakasz frissítve az összes népszerű kliens opcióval
- Hozzájárulási példák fejlesztve pontosabb kódmintákkal

### Fejlett témák (05-AdvancedTopics/)
- Minden speciális témakönyvtár egységes névhasználattal rendszerezve
- Kontextus mérnökségi anyagok és példák hozzáadva
- Foundry ügynök integráció dokumentáció hozzáadva
- Entra ID biztonsági integráció dokumentáció fejlesztve

## 2025. június 11.

### Kezdeti létrehozás
- Megjelent az MCP kezdőknek tananyag első verziója
- Alapstruktúra létrehozva a 10 fő szakaszhoz
- Vizualizált tananyag térkép megvalósítva a navigációhoz
- Kezdeti mintaprojektek hozzáadva több programozási nyelven

### Első lépések (03-GettingStarted/)
- Első szerver megvalósítási példák létrehozva
- Kliens fejlesztési útmutató hozzáadva
- LLM kliens integrációs utasítások beillesztve
- VS Code integráció dokumentáció hozzáadva
- Server-Sent Events (SSE) szerver példák megvalósítva

### Alapfogalmak (01-CoreConcepts/)
- Részletes kliens-szerver architektúra magyarázat hozzáadva
- Dokumentáció a kulcs protokoll komponensekről
- MCP üzenetküldési minták dokumentálva

## 2025. május 23.

### Tárház struktúra
- Tárház inicializálva alap mappastruktúrával
- README fájlok létrehozva minden fő szakaszhoz
- Fordítási infrastruktúra beállítva
- Képanyagok és diagramok hozzáadva

### Dokumentáció
- Kezdeti README.md létrehozva a tananyag áttekintésével
- CODE_OF_CONDUCT.md és SECURITY.md hozzáadva
- SUPPORT.md beállítva segítségkéréshez
- Előzetes tanulmányi útmutató struktúra létrehozva

## 2025. április 15.

### Tervezés és keretrendszer
- MCP kezdőknek tananyag kezdeti tervezése
- Tanulási célok és célközönség meghatározása
- A tananyag 10 szakaszos struktúrájának vázlata
- Fogalmi keretrendszer kidolgozása példákhoz és esettanulmányokhoz
- Kezdeti prototípus példák létrehozása kulcsfogalmakhoz

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->