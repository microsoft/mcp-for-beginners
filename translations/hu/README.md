![MCP-for-beginners](../../translated_images/hu/mcp-beginners.2ce2b317996369ff.webp) 

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/mcp-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/mcp-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/mcp-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kövesd ezeket a lépéseket, hogy elkezdhess dolgozni ezekkel az erőforrásokkal:
1. **Törzs tároló fork-olása**: Kattints ide [![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
2. **Törzs tároló klónozása**:   `git clone https://github.com/microsoft/mcp-for-beginners.git`
3. **Csatlakozz a** [![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


### 🌐 Többnyelvű támogatás

#### GitHub Action által támogatott (Automatikus és mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Mianmar)](../my/README.md) | [Kínai (Egyszerűsített)](../zh-CN/README.md) | [Kínai (Hagyományos, Hongkong)](../zh-HK/README.md) | [Kínai (Hagyományos, Makaó)](../zh-MO/README.md) | [Kínai (Hagyományos, Tajvan)](../zh-TW/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Hollandi](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigeriái pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Fársi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../pt-BR/README.md) | [Portugál (Portugália)](../pt-PT/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (Cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (Filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnámi](../vi/README.md)

> **Inkább helyben szeretnéd klónozni?**
>
> Ez a tároló több mint 50 nyelvi fordítást tartalmaz, ami jelentősen megnöveli a letöltés méretét. Ha fordítások nélkül szeretnéd klónozni, használd a sparse checkout-ot:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Így mindent megkapsz, amire szükséged van a tanfolyam befejezéséhez, sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

# 🚀 Model Context Protocol (MCP) tananyag kezdőknek

## **Tanulj MCP-t kézzel fogható kódpéldákon keresztül C#, Java, JavaScript, Rust, Python, és TypeScript nyelveken**

## 🧠 A Model Context Protocol tananyag áttekintése
Üdvözlünk a Model Context Protocol felfedezésének útján! Ha valaha is kíváncsi voltál, hogyan kommunikálnak az AI alkalmazások különböző eszközökkel és szolgáltatásokkal, most megismerheted azt az elegáns megoldást, amely átalakítja a fejlesztők intelligens rendszerek építését.

Gondolj az MCP-re úgy, mint az AI alkalmazások univerzális fordítójára – ahogy az USB portok lehetővé teszik, hogy bármilyen eszközt csatlakoztass számítógépedhez, az MCP lehetővé teszi, hogy az AI modellek egységes módon kapcsolódjanak bármely eszközhöz vagy szolgáltatáshoz. Akár az első chatbotodat építed, akár bonyolult AI munkafolyamatokon dolgozol, az MCP megértése erőt ad arra, hogy képesebb és rugalmasabb alkalmazásokat hozz létre.

Ez a tananyag türelemmel és gondossággal készült a tanulási utadhoz. Egyszerű koncepciókkal kezdünk, amiket már értesz, majd fokozatosan fejlesztjük a tudásod gyakorlati példákon keresztül a kedvenc programozási nyelveden. Minden lépésben világos magyarázatokat, gyakorlati példákat és sok bátorítást kapsz.

A tananyag befejeztével magabiztos leszel saját MCP szerverek létrehozásában, integrálod őket népszerű AI platformokkal, és megérted, hogyan formálja át ez a technológia az AI fejlesztés jövőjét. Kezdjük el együtt ezt az izgalmas kalandot!

### Hivatalos dokumentáció és specifikációk

Ez a tananyag összhangban van a **MCP Specification 2025-11-25** verzióval (a legfrissebb stabil kiadás). Az MCP specifikáció dátumalapú verziózást használ (ÉÉÉÉ-HH-NN formátumban), hogy biztosítsa a protokoll verziójának követhetőségét.

Ezek az erőforrások értékesebbek lesznek a megértésed növekedésével, de ne érezd kötelezőnek, hogy azonnal mindent elolvass! Kezdd azzal, ami a legérdekesebb számodra!
- 📘 [MCP Dokumentáció](https://modelcontextprotocol.io/) – Ez az alapvető erőforrásod lépésről lépésre bemutatókkal és használati útmutatókkal. A dokumentáció kezdők számára készült világos példákkal, amelyekhez saját tempódban tudsz csatlakozni.
- 📜 [MCP Specifikáció](https://modelcontextprotocol.io/specification/2025-11-25) – Tekintsd ezt átfogó referencia kézikönyvnek. Ahogy haladsz a tananyagban, gyakran visszatérsz ide, hogy részleteket nézz meg és bővebben megismerd az előrehaladott funkciókat.
- 📜 [MCP Specifikáció verziózás](https://modelcontextprotocol.io/specification/versioning) – Ez tartalmazza a protokoll verziótörténetét és az MCP dátumalapú verziózását (ÉÉÉÉ-HH-NN formátumban).
- 🧑‍💻 [MCP GitHub tároló](https://github.com/modelcontextprotocol) – Itt SDK-kat, eszközöket és kódmintákat találsz több programozási nyelven. Olyan, mint egy kincsestár gyakorlati példákkal és készen használható komponensekkel.
- 🌐 [MCP Közösség](https://github.com/orgs/modelcontextprotocol/discussions) – Csatlakozz a tanulók és tapasztalt fejlesztők közösségéhez, ahol az MCP-ről folytatott megbeszélések zajlanak. Ez egy támogató közösség, ahol kérdések megengedettek és a tudás szabadon megosztott.

## Tanulási célok

A tananyag végére magabiztos és lelkes leszel az új képességeiddel kapcsolatban. Íme, mit érsz el:

• **Megérted az MCP alapjait**: Átlátod, mi az a Model Context Protocol, és miért forradalmasítja az AI alkalmazások együttműködését, érthető hasonlatokkal és példákkal.

• **Megépíted az első MCP szerveredet**: Elkészítesz egy működő MCP szervert a választott programozási nyelveden, egyszerű példákkal indulva és lépésről lépésre fejlesztve a készségeidet.

• **Kapcsolatot teremtesz AI modellek és valós eszközök között**: Megtanulod, hogyan építs hidat az AI modellek és az igazi szolgáltatások között, így erőteljes új funkciókat adhatsz alkalmazásaidhoz.

• **Biztonsági legjobb gyakorlatok alkalmazása**: Megérted, hogyan tartsd biztonságban az MCP megvalósításaidat, védve az alkalmazásokat és a felhasználókat.

• **Magabiztos telepítés**: Tudni fogod, hogyan juttasd el az MCP projektjeidet a fejlesztéstől a termelésig, gyakorlati telepítési stratégiákkal, amelyek a valóságban is működnek.

• **Csatlakozol az MCP közösséghez**: Része leszel egy növekvő fejlesztői közösségnek, amely az AI alkalmazásfejlesztés jövőjét formálja.

## Alapvető háttér

Mielőtt belevágunk az MCP részleteibe, győződjünk meg róla, hogy kényelmesen mozogsz néhány alapvető fogalomban. Ne aggódj, ha nem vagy szakértő ezeken a területeken - mindent elmagyarázunk menet közben!

### Protokollok megértése (Az alapok)

Gondolj a protokollra úgy, mint egy beszélgetés szabályaira. Amikor felhívsz egy barátot, mindketten tudjátok, hogy „szia”-t mondotok a fogadáskor, felváltva beszéltek, és a végén elköszöntek. A programoknak hasonló szabályokra van szükségük, hogy hatékonyan kommunikáljanak.

Az MCP egy protokoll – egy megállapodott szabálykészlet, amely segít az AI modelleknek és alkalmazásoknak, hogy „értelmes” beszélgetést folytassanak eszközökkel és szolgáltatásokkal. Ahogy az emberi kommunikáció gördülékenyebb a szabályokkal, az MCP megbízhatóbbá és hatékonyabbá teszi az AI alkalmazások közötti kommunikációt.

### Ügyfél-szerver kapcsolatok (Hogyan működnek együtt a programok)

Nap mint nap használod az ügyfél-szerver kapcsolatokat! Amikor böngészőt (ügyfél) használsz egy weboldal elérésére, kapcsolódsz egy web szerverhez, ami elküldi az oldal tartalmát. A böngésző tudja, hogyan kérjen információt, a szerver pedig hogyan válaszoljon.

Az MCP-ben is hasonló kapcsolat van: az AI modellek ügyfelekként kérnek adatokat vagy műveleteket, míg az MCP szerverek ezeket a szolgáltatásokat nyújtják. Olyan, mintha az AI egy segítő asszisztenssel (a szerverrel) beszélgetne, amely elvégzi a kért feladatokat.

### Miért fontos a szabványosítás (Együttműködésre hangolás)

Képzeld el, ha minden autógyártó más alakú benzinpumpa-csatlakozót használna – minden autóhoz külön adapter kellene! A szabványosítás azt jelenti, hogy közös megközelítésben állapodunk meg, hogy minden zökkenőmentesen működjön.

Az MCP ezt a szabványosítást nyújtja az AI alkalmazások számára. Nem kell mindegyik AI modellnek egyedi kód arra, hogy minden eszközzel együttműködjön, hanem az MCP univerzális kommunikációs módot teremt. Így a fejlesztők egyszer építik meg az eszközöket, amelyek sokféle AI rendszerrel működnek együtt.

## 🧭 A tanulási utad áttekintése

Az MCP utad gondosan felépített, hogy fokozatosan növelje a magabiztosságot és a képességeidet. Minden fázis új fogalmakat mutat be, miközben megerősíti, amit már tanultál.

### 🌱 Alapozó fázis: Az alapok megértése (0-2. modulok)

Itt kezdődik a kaland! Megismertetünk az MCP fogalmával ismerős hasonlatokkal és egyszerű példákkal. Megérted, mi az az MCP, miért létezik, és hogyan illeszkedik az AI fejlesztés nagyobb világába.

• **0. modul - Bevezetés az MCP-be**: Megvizsgáljuk, mi az MCP és miért fontos a modern AI alkalmazások számára. Valós példákon keresztül megérted, hogyan oldja meg a fejlesztők által gyakran tapasztalt problémákat.

• **1. modul - Alapfogalmak magyarázata**: Itt megismered az MCP lényeges építőköveit. Sok hasonlattal és vizuális példával dolgozunk, hogy ezek a fogalmak természetesnek és könnyen érthetőnek hassanak.

• **2. modul - Biztonság az MCP-ben**: A biztonság talán ijesztőnek hangzik, de megmutatjuk, hogyan tartalmaz az MCP beépített védelmi funkciókat, és megtanítjuk a legjobb gyakorlatokat, amelyek az alkalmazásaid védelmét szolgálják.

### 🔨 Építő fázis: Az első megvalósítások elkészítése (3. modul)
Most kezdődik az igazi móka! Gyakorlati tapasztalatot szerezhetsz valódi MCP szerverek és kliensek építésében. Ne aggódj – egyszerűen kezdünk, és végigvezetünk minden lépésen.

Ez a modul több gyakorlati útmutatót tartalmaz, amelyek lehetővé teszik, hogy a kiválasztott programozási nyelvedben gyakorolj. Elkészíted az első szerveredet, építesz egy klienst, ami kapcsolódik hozzá, és akár népszerű fejlesztői eszközökkel, mint a VS Code, is integrálod.

Minden útmutató teljes kódpéldákat, hibaelhárítási tippeket és magyarázatokat tartalmaz arról, hogy miért hoztunk meg bizonyos tervezési döntéseket. Ennek a fázisnak a végére működő MCP megvalósításokkal rendelkezel, amikre büszke lehetsz!

### 🚀 Növekedési fázis: Fejlett koncepciók és valós alkalmazások (4-5. modulok)

Az alapok elsajátítása után készen állsz, hogy felfedezz fejlettebb MCP funkciókat. Megvizsgáljuk a gyakorlati megvalósítási stratégiákat, hibakeresési technikákat, valamint fejlett témákat, mint a multimodális MI integrációja.

Megtanulod azt is, hogyan skálázd az MCP megvalósításokat a gyártási felhasználáshoz, és hogyan integrálj felhőplatformokkal, mint az Azure. Ezek a modulok felkészítenek arra, hogy MCP megoldásokat építs, amelyek képesek megbirkózni a valós világ követelményeivel.

### 🌟 Mesterfázis: Közösség és specializáció (6-11. modulok)

Az utolsó fázis az MCP közösséghez való csatlakozásra és az érdeklődési területek szerinti specializációra fókuszál. Megtanulod, hogyan járulj hozzá nyílt forráskódú MCP projektekhez, valósíts meg fejlett hitelesítési mintákat, és építs átfogó, adatbázissal integrált megoldásokat.

A 11. modul külön említést érdemel – egy teljes, 13 laborból álló gyakorlati tanulási út, amely megtanít arra, hogyan építs gyártásra kész MCP szervereket PostgreSQL integrációval. Olyan, mint egy összefoglaló projekt, ami összehozza mindazt, amit tanultál!

### 📚 Teljes tanterv struktúra

| Modul | Téma | Leírás | Link |
|--------|-------|-------------|------|
| **0-3. modulok: Alapok** | | | |
| 00 | Bevezetés az MCP-be | Áttekintés a Model Context Protocolról és annak jelentőségéről az MI pipeline-okban | [Bővebben](./00-Introduction/README.md) |
| 01 | Alapfogalmak magyarázata | Mélyreható vizsgálat az MCP alapfogalmairól | [Bővebben](./01-CoreConcepts/README.md) |
| 02 | Biztonság az MCP-ben | Biztonsági fenyegetések és legjobb gyakorlatok | [Bővebben](./02-Security/README.md) |
| 03 | MCP használatának megkezdése | Környezet beállítása, alap szerverek/kliensek, integráció | [Bővebben](./03-GettingStarted/README.md) |
| **3. Modul: Első szervered és kliensed építése** | | | |
| 3.1 | Első szerver | Készítsd el első MCP szerveredet | [Útmutató](./03-GettingStarted/01-first-server/README.md) |
| 3.2 | Első kliens | Fejlessz alap MCP klienst | [Útmutató](./03-GettingStarted/02-client/README.md) |
| 3.3 | Kliens LLM-mel | Integrálj nagy nyelvi modelleket | [Útmutató](./03-GettingStarted/03-llm-client/README.md) |
| 3.4 | VS Code integráció | Használd az MCP szervereket VS Code-ban | [Útmutató](./03-GettingStarted/04-vscode/README.md) |
| 3.5 | stdio szerver | Készíts szervereket stdio protokollal | [Útmutató](./03-GettingStarted/05-stdio-server/README.md) |
| 3.6 | HTTP streaming | Valósíts meg HTTP streaminget MCP-ben | [Útmutató](./03-GettingStarted/06-http-streaming/README.md) |
| 3.7 | AI Toolkit | Használd az AI Toolkitet MCP-vel | [Útmutató](./03-GettingStarted/07-aitk/README.md) |
| 3.8 | Tesztelés | Teszteld az MCP szerver megvalósításodat | [Útmutató](./03-GettingStarted/08-testing/README.md) |
| 3.9 | Telepítés | Telepítsd az MCP szervereket éles környezetbe | [Útmutató](./03-GettingStarted/09-deployment/README.md) |
| 3.10 | Fejlett szerverhasználat | Használj fejlett szervereket fejlettebb funkciókhoz és jobb architektúrához | [Útmutató](./03-GettingStarted/10-advanced/README.md) |
| 3.11 | Egyszerű hitelesítés | Egy fejezet arról, hogyan működik a hitelesítés az elejétől és RBAC | [Útmutató](./03-GettingStarted/11-simple-auth/README.md) |
| 3.12 | MCP hosztok | Claude Desktop, Cursor, Cline és más MCP hosztok konfigurálása | [Útmutató](./03-GettingStarted/12-mcp-hosts/README.md) |
| 3.13 | MCP Inspector | Hibakeresés és tesztelés az Inspector eszközzel | [Útmutató](./03-GettingStarted/13-mcp-inspector/README.md) |
| 3.14 | Mintavételezés | Használd a mintavételezést a klienssel való együttműködéshez | [Útmutató](./03-GettingStarted/14-sampling/README.md) |
| 3.15 | MCP alkalmazások | Készíts MCP alkalmazásokat | [Útmutató](./03-GettingStarted/15-mcp-apps/README.md) |
| **4-5. modulok: Gyakorlati és fejlett témák** | | | |
| 04 | Gyakorlati megvalósítás | SDK-k, hibakeresés, tesztelés, újrahasznosítható prompt sablonok | [Bővebben](./04-PracticalImplementation/README.md) |
| 4.1 | Lapozás | Nagy eredményhalmazok kezelése kurzoros lapozással | [Útmutató](./04-PracticalImplementation/pagination/README.md) |
| 05 | Fejlett MCP témák | Multimodális MI, skálázás, vállalati használat | [Bővebben](./05-AdvancedTopics/README.md) |
| 5.1 | Azure integráció | MCP integráció Azure-ral | [Útmutató](./05-AdvancedTopics/mcp-integration/README.md) |
| 5.2 | Multimodalitás | Több modalitással való munka | [Útmutató](./05-AdvancedTopics/mcp-multi-modality/README.md) |
| 5.3 | OAuth2 bemutató | OAuth2 hitelesítés megvalósítása | [Útmutató](./05-AdvancedTopics/mcp-oauth2-demo/README.md) |
| 5.4 | Root környezetek | Root kontextusok megértése és implementálása | [Útmutató](./05-AdvancedTopics/mcp-root-contexts/README.md) |
| 5.5 | Routing | MCP routing stratégiák | [Útmutató](./05-AdvancedTopics/mcp-routing/README.md) |
| 5.6 | Mintavételezés | Mintavételezési technikák MCP-ben | [Útmutató](./05-AdvancedTopics/mcp-sampling/README.md) |
| 5.7 | Skálázás | MCP megvalósítások skálázása | [Útmutató](./05-AdvancedTopics/mcp-scaling/README.md) |
| 5.8 | Biztonság | Fejlett biztonsági szempontok | [Útmutató](./05-AdvancedTopics/mcp-security/README.md) |
| 5.9 | Web keresés | Web keresési képességek megvalósítása | [Útmutató](./05-AdvancedTopics/web-search-mcp/README.md) |
| 5.10 | Valós idejű streaming | Valós idejű streaming funkció építése | [Útmutató](./05-AdvancedTopics/mcp-realtimestreaming/README.md) |
| 5.11 | Valós idejű keresés | Valós idejű keresés megvalósítása | [Útmutató](./05-AdvancedTopics/mcp-realtimesearch/README.md) |
| 5.12 | Entra ID hitelesítés | Hitelesítés Microsoft Entra ID-vel | [Útmutató](./05-AdvancedTopics/mcp-security-entra/README.md) |
| 5.13 | Foundry integráció | Integráció Azure AI Foundry-val | [Útmutató](./05-AdvancedTopics/mcp-foundry-agent-integration/README.md) |
| 5.14 | Kontextervezés | Hatékony kontextus tervezési technikák | [Útmutató](./05-AdvancedTopics/mcp-contextengineering/README.md) |
| 5.15 | Egyedi MCP transport | Egyedi transport megvalósítások | [Útmutató](./05-AdvancedTopics/mcp-transport/README.md) |
| 5.16 | Protokoll funkciók | Előrehaladási értesítések, megszakítás, erőforrás sablonok | [Útmutató](./05-AdvancedTopics/mcp-protocol-features/README.md) |
| 5.17 | Ellentétes többügynökös érvelés | Két ügynök ellentétes álláspontokat képvisel megosztott MCP eszközökkel, bíráló ügynök értékeli | [Útmutató](./05-AdvancedTopics/mcp-adversarial-agents/README.md) |
| **6-10. modulok: Közösség és legjobb gyakorlatok** | | | |
| 06 | Közösségi hozzájárulások | Hogyan járulj hozzá az MCP ökoszisztémához | [Útmutató](./06-CommunityContributions/README.md) |
| 07 | Korai tapasztalatok tanulságai | Valós megvalósítási történetek | [Útmutató](./07-LessonsfromEarlyAdoption/README.md) |
| 08 | Legjobb gyakorlatok MCP-ben | Teljesítmény, hibabiztosság, ellenállóság | [Útmutató](./08-BestPractices/README.md) |
| 09 | MCP esettanulmányok | Gyakorlati megvalósítási példák | [Útmutató](./09-CaseStudy/README.md) |
| 10 | Gyakorlati workshop | MCP szerver építése AI Toolkittel | [Labor](./10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) |
| **11. Modul: MCP szerver gyakorlati labor** | | | |
| 11 | MCP szerver adatbázis integráció | Teljes, 13 laborból álló gyakorlati tanulási út PostgreSQL integrációval | [Laborok](./11-MCPServerHandsOnLabs/README.md) |
| 11.1 | Bevezetés | Áttekintés az MCP-ről adatbázis integrációval és kiskereskedelmi elemzési esettel | [Labor 00](./11-MCPServerHandsOnLabs/00-Introduction/README.md) |
| 11.2 | Alap architektúra | MCP szerver architektúra, adatbázis rétegek és biztonsági minták megértése | [Labor 01](./11-MCPServerHandsOnLabs/01-Architecture/README.md) |
| 11.3 | Biztonság és multi-tenancy | Sor szintű biztonság, hitelesítés, multi-tenant adat hozzáférés | [Labor 02](./11-MCPServerHandsOnLabs/02-Security/README.md) |
| 11.4 | Környezet beállítása | Fejlesztői környezet, Docker, Azure erőforrások beállítása | [Labor 03](./11-MCPServerHandsOnLabs/03-Setup/README.md) |
| 11.5 | Adatbázis tervezés | PostgreSQL beállítása, kiskereskedelmi séma tervezése, mintaadatok | [Labor 04](./11-MCPServerHandsOnLabs/04-Database/README.md) |
| 11.6 | MCP szerver megvalósítása | FastMCP szerver építése adatbázis integrációval | [Labor 05](./11-MCPServerHandsOnLabs/05-MCP-Server/README.md) |
| 11.7 | Eszközfejlesztés | Adatbázis lekérdező eszközök és séma introspekció készítése | [Labor 06](./11-MCPServerHandsOnLabs/06-Tools/README.md) |
| 11.8 | Szemantikus keresés | Vektoros beágyazások megvalósítása Azure OpenAI-vel és pgvectorral | [Labor 07](./11-MCPServerHandsOnLabs/07-Semantic-Search/README.md) |
| 11.9 | Tesztelés és hibakeresés | Tesztelési stratégiák, hibakereső eszközök és validációs megközelítések | [Labor 08](./11-MCPServerHandsOnLabs/08-Testing/README.md) |
| 11.10 | VS Code integráció | VS Code MCP integráció konfigurálása és AI chat használat | [Labor 09](./11-MCPServerHandsOnLabs/09-VS-Code/README.md) |
| 11.11 | Telepítési stratégiák | Docker telepítés, Azure Container Apps és skálázási megfontolások | [Labor 10](./11-MCPServerHandsOnLabs/10-Deployment/README.md) |
| 11.12 | Monitoring | Application Insights, naplózás, teljesítményfigyelés | [Labor 11](./11-MCPServerHandsOnLabs/11-Monitoring/README.md) |
| 11.13 | Legjobb gyakorlatok | Teljesítmény optimalizálás, biztonsági megerősítés és éles tippek | [Labor 12](./11-MCPServerHandsOnLabs/12-Best-Practices/README.md) |

### 💻 Minta kód projektek

Az egyik legizgalmasabb része az MCP tanulásának, hogy láthatod, ahogy a kód tudásod fokozatosan fejlődik. A kódpéldáink úgy vannak kialakítva, hogy egyszerűtől induljanak, és egyre kifinomultabbá váljanak, ahogy mélyül a megértésed. Így vezetjük be a koncepciókat – olyan kód, amit könnyű megérteni, de valódi MCP elveket demonstrál, így nemcsak azt fogod érteni, hogy mit csinál a kód, hanem azt is, hogy miért így van felépítve, és hogyan illeszkedik nagyobb MCP alkalmazásokba.

#### Alap MCP számológép minták

| Nyelv | Leírás | Link |
|----------|-------------|------|
| C# | MCP szerver példa | [Kód megtekintése](./03-GettingStarted/samples/csharp/README.md) |
| Java | MCP számológép | [Kód megtekintése](./03-GettingStarted/samples/java/calculator/README.md) |
| JavaScript | MCP demó | [Kód megtekintése](./03-GettingStarted/samples/javascript/README.md) |
| Python | MCP szerver | [Kód megtekintése](../../03-GettingStarted/samples/python/mcp_calculator_server.py) |
| TypeScript | MCP példa | [Kód megtekintése](./03-GettingStarted/samples/typescript/README.md) |
| Rust | MCP példa | [Kód megtekintése](./03-GettingStarted/samples/rust/README.md) |

#### Fejlett MCP megvalósítások

| Nyelv | Leírás | Link |
|----------|-------------|------|
| C# | Fejlett minta | [Kód megtekintése](./04-PracticalImplementation/samples/csharp/README.md) |
| Java Spring-mel | Konténeres alkalmazás példa | [Kód megtekintése](./04-PracticalImplementation/samples/java/containerapp/README.md) |
| JavaScript | Fejlett minta | [Kód megtekintése](./04-PracticalImplementation/samples/javascript/README.md) |
| Python | Összetett megvalósítás | [Kód megtekintése](./04-PracticalImplementation/samples/python/README.md) |
| TypeScript | Konténer Példa | [Kód megtekintése](./04-PracticalImplementation/samples/typescript/README.md) |


## 🎯 Az MCP tanulásának előfeltételei

Ahhoz, hogy a legtöbbet hozd ki ebből a tananyagból, rendelkezned kell:

- Alapvető programozási ismeretekkel legalább az alábbi nyelvek egyikén: C#, Java, JavaScript, Python vagy TypeScript
- Megértéssel a kliens-szerver modell és az API-k működéséről
- Ismeretekkel a REST és HTTP fogalmakról
- (Opcionális) Háttérismeretek az AI/ML fogalmakból

- Közösségi beszélgetéseinkhez való csatlakozás támogatásért

## 📚 Tanulási Útmutató & Források

Ez a tároló több forrást is tartalmaz, hogy segítsen hatékonyan eligazodni és tanulni:

### Tanulási Útmutató

Egy átfogó [Tanulási Útmutató](./study_guide.md) érhető el, amely segít hatékonyan navigálni ebben a tárolóban. Ez a vizuális tantervtérkép megmutatja, hogyan kapcsolódnak egymáshoz a témák, és útmutatást ad arra, hogyan használd a mintaprojekteket hatékonyan. Különösen hasznos, ha vizuális típusú tanuló vagy, aki szereti látni az egész képet.

Az útmutató tartalmazza:
- Egy vizuális tantervtérkép, amely az összes lefedett témát bemutatja
- A tároló egyes részeinek részletes bontását
- Útmutatást a mintaprojektek használatához
- Ajánlott tanulási útvonalakat különböző készségszintekhez
- További forrásokat, amelyek kiegészítik a tanulási utadat

### Változások Naplója

Részletes [Változások Naplót](./changelog.md) vezetünk, amely nyomon követi a tananyagelemek fontosabb frissítéseit, hogy mindig naprakész legyél a legújabb fejlesztésekkel és bővítésekkel.
- Új tartalom hozzáadások
- Strukturális változtatások
- Funkciófejlesztések
- Dokumentáció frissítések

## 🛠️ Hogyan Használjuk Hatékonyan Ezt a Tananyagot

Az útmutatóban minden lecke tartalmaz:

1. Az MCP koncepcióinak világos magyarázatát  
2. Élő kódpéldákat több nyelven  
3. Gyakorlatokat valódi MCP alkalmazások építéséhez  
4. Extra forrásokat haladó tanulók számára

### Tanuljuk Meg az MCP-t C#-szal – Oktatási Sorozat
Ismerkedj meg a Model Context Protocol-lal (MCP), egy élvonalbeli keretrendszerrel, amely az AI modellek és kliensalkalmazások közötti interakciók szabványosítására szolgál. Ebben a kezdőbarát gyakorlati foglalkozásban bemutatjuk az MCP-t, és végigvezetünk az első MCP szervered elkészítésén.
#### C#: [https://aka.ms/letslearnmcp-csharp](https://aka.ms/letslearnmcp-csharp)
#### Java: [https://aka.ms/letslearnmcp-java](https://aka.ms/letslearnmcp-java)
#### JavaScript: [https://aka.ms/letslearnmcp-javascript](https://aka.ms/letslearnmcp-javascript)
#### Python: [https://aka.ms/letslearnmcp-python](https://aka.ms/letslearnmcp-python)

## 🎓 Az MCP Utad Kezdete

Gratulálunk! Most tetted meg az első lépést egy izgalmas úton, amely bővíti programozói képességeidet és összeköt a mesterséges intelligencia fejlesztésének élvonalával.

### Amit Már Elértél

Ebbe az bevezető olvasásával már megkezdted az MCP tudásalapod építését. Érted, mi az MCP, miért fontos, és hogyan támogat téged ez a tananyag a tanulási utadon. Ez nagy eredmény, és a szakértelmed kezdete ebben a fontos technológiában.

### A Kaland Előtted

Ahogy haladsz a modulokon keresztül, ne feledd, hogy minden szakértő egyszer kezdő volt. Azok a fogalmak, amelyek most bonyolultnak tűnnek, rutinná válnak, ahogy gyakorolsz és alkalmazod őket. Minden apró lépés egy erőteljes képesség felé vezet, amely végigkíséri fejlesztői pályafutásodat.

### A Támogatói Hálózatod

Csatlakozol egy olyan tanulókból és szakértőkből álló közösséghez, akik szenvedélyesen érdeklődnek az MCP iránt, és szívesen segítenek másoknak sikeresnek lenni. Legyen szó kódolási kihívásról vagy áttörés megosztásáról, a közösség itt van, hogy támogassa az utadat.

Ha elakadsz vagy kérdésed van az AI alkalmazások építésével kapcsolatban, csatlakozz a többi tanulóhoz és tapasztalt fejlesztőkhöz az MCP témájú beszélgetésekben. Ez egy támogató közösség, ahol a kérdések szívesen fogadottak, és a tudás szabadon megosztott.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termékvisszajelzésed vagy hibákba ütközöl az építés közben, látogasd meg:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

### Készen Állsz Kezdeni?

Most indul az MCP kalandod! Kezdd a 0. Modulnál, hogy belemerülj az első gyakorlati MCP élményekbe, vagy fedezd fel a mintaprojekteket, hogy lásd, mit fogsz építeni. Ne feledd – minden szakértő pontosan ott kezdte, ahol most vagy, és türelemmel, gyakorlással csodálatos dolgokat érhetsz el.

Üdvözöljük a Model Context Protocol fejlesztés világában. Építsünk együtt valami csodálatost!

## 🤝 Hozzájárulás a Tanulóközösséghez

Ez a tananyag a hozzájáruló tanulók által egyre erősebb! Akár elgépelést javítasz, világosabb magyarázatot javasolsz, vagy új példát adsz hozzá, hozzájárulásaid segítik, hogy más kezdők is sikeresek legyenek.

Köszönet a Microsoft Értékelt Szakembernek [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) a kódmintákért.

A hozzájárulási folyamat barátságos és támogató jellegű. A legtöbb hozzájáruláshoz szükséges a Contributor License Agreement (CLA), de az automatizált eszközök zökkenőmentesen végigvezetnek a folyamaton.

## 📜 Nyílt Forráskódú Tanulás

Ez az egész tananyag az MIT [LICENSE](../../LICENSE) alatt érhető el, ami azt jelenti, hogy szabadon használhatod, módosíthatod és megoszthatod. Ez támogatja küldetésünket, hogy az MCP tudás minden fejlesztő számára hozzáférhető legyen.
## 🤝 Hozzájárulási Irányelvek

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. A legtöbb hozzájáruláshoz el kell fogadnod egy
Contributor License Agreement (CLA) megállapodást, amelyben kijelented, hogy jogod van arra, és ténylegesen megadod nekünk
a jogokat a hozzájárulásod használatára. Részletekért látogass el a <https://cla.opensource.microsoft.com> oldalra.

Amikor pull request-et küldesz be, egy CLA bot automatikusan megállapítja, hogy szükséges-e CLA-t benyújtanod,
és ennek megfelelően jelöli meg a PR-t (pl. állapot ellenőrzés, komment). Egyszerűen kövesd a bot által adott
utasításokat. Ezt csak egyszer kell megtenned az összes olyan tároló esetén, amely a CLA-nkat használja.

Ez a projekt elfogadta a [Microsoft Nyílt Forráskódú Magatartási Szabályzatát](https://opensource.microsoft.com/codeofconduct/).
További információért lásd a [Magatartási Szabályzat GYIK](https://opensource.microsoft.com/codeofconduct/faq/) részt, vagy
kapcsolatfelvétel az [opencode@microsoft.com](mailto:opencode@microsoft.com) címen bármilyen további kérdés vagy észrevétel esetén.

---

*Készen állsz az MCP utad megkezdésére? Kezdd a [00. Modul – Bevezetés az MCP-be](./00-Introduction/README.md) anyagot és tedd meg az első lépéseket a Model Context Protocol fejlesztés világában!*



## 🎒 Egyéb kurzusok
Csapatunk más kurzusokat is készít! Nézd meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j kezdőknek](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js kezdőknek](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain kezdőknek](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Ügynökök
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatív AI sorozat
[![Generatív AI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Alapvető tanulás
[![ML kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webfejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Fejlesztés Kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Sorozat
[![Copilot az AI Páros Programozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-hez](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Kaland](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősségkizárás**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) nevű AI fordítási szolgáltatás segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum, annak anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértések vagy félreértelmezések miatt.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->