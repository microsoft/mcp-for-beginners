# MCP Biztonság: Átfogó védelem az AI rendszerek számára

[![MCP Biztonság Legjobb Gyakorlatai](../../../translated_images/hu/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Kattintson a fenti képre a tananyag videójának megtekintéséhez)_

A biztonság alapvető fontosságú az AI rendszerek tervezésében, ezért kiemelt helyen kezeljük a második szakaszunkban. Ez összhangban áll a Microsoft **Secure by Design** elvével a [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/) részeként.

A Model Context Protocol (MCP) új, erőteljes képességeket hoz az AI által vezérelt alkalmazásokhoz, miközben egyedi biztonsági kihívásokat is felvet, amelyek túlmutatnak a hagyományos szoftverkockázatokon. Az MCP rendszereknek szembe kell nézniük mind a bevett biztonsági kérdésekkel (biztonságos programozás, legkisebb jogosultság elve, ellátási lánc biztonság), mind az új AI-specifikus fenyegetésekkel, mint a prompt injekció, eszköz mérgezés, munkamenet eltérítés, összezavart helyettesítő támadások, token átviteli sérülékenységek és dinamikus képesség módosítás.

Ez a tananyag feltárja az MCP megvalósítások legkritikusabb biztonsági kockázatait — beleértve a hitelesítést, engedélyezést, túlzott jogosultságokat, közvetett prompt injekciót, munkamenet biztonságot, összezavart helyettesítő problémákat, token kezelést és ellátási lánc sebezhetőségeket. Megtanulhatja a kockázatok mérséklésére alkalmas irányítási intézkedéseket és legjobb gyakorlatokat, miközben kihasználja a Microsoft megoldásait, mint a Prompt Shields, Azure Content Safety és GitHub Advanced Security, hogy megerősítse MCP telepítését.

## Tanulási célok

A tananyag végére képes lesz:

- **Az MCP-specifikus fenyegetések azonosítása**: Felismerni az MCP rendszerek egyedi biztonsági kockázatait, beleértve a prompt injekciót, eszköz mérgezést, túlzott jogosultságokat, munkamenet eltérítést, összezavart helyettesítő problémákat, token átviteli sérülékenységeket és ellátási lánc kockázatokat
- **Biztonsági kontrollok alkalmazása**: Hatékony enyhítések végrehajtása, beleértve a szilárd hitelesítést, legkisebb jogosultság hozzáférést, biztonságos token kezelést, munkamenet biztonsági ellenőrzéseket és ellátási lánc ellenőrzést
- **Microsoft biztonsági megoldások kihasználása**: Megérteni és telepíteni a Microsoft Prompt Shields, Azure Content Safety és GitHub Advanced Security megoldásokat az MCP munkaterhelés védelmére
- **Eszköz biztonságának érvényesítése**: Felismerni az eszköz metaadat érvényesítés fontosságát, a dinamikus változások figyelemmel kísérését és a közvetett prompt injekciós támadások elleni védelmet
- **Legjobb gyakorlatok integrálása**: Összekapcsolni a bevett biztonsági alapelveket (biztonságos kódolás, szerver megerősítés, nulla bizalom) az MCP-specifikus kontrollokkal az átfogó védelem érdekében

# MCP Biztonsági Architektúra és Kontrollok

A modern MCP megvalósítások több rétegű biztonsági megközelítést igényelnek, amelyek egyszerre kezelik a hagyományos szoftverbiztonsági és AI-specifikus fenyegetéseket. A gyorsan fejlődő MCP specifikáció folyamatosan éretté teszi biztonsági kontrolljait, lehetővé téve a jobb integrációt a vállalati biztonsági architektúrákkal és a bevett legjobb gyakorlatokkal.

A [Microsoft Digital Defense Report](https://aka.ms/mddr) kutatása kimutatja, hogy a **jelentett támadások 98%-a elkerülhető lenne szilárd biztonsági higiéniával**. A leghatékonyabb védekezési stratégia az alapvető biztonsági gyakorlatokat és az MCP-specifikus kontrollokat ötvözi — a bizonyított alapbiztonsági intézkedések a legnagyobb hatást gyakorolják az átfogó biztonsági kockázat csökkentésében.

## Jelenlegi Biztonsági Helyzet

> **Megjegyzés:** Ez a fejezet ötvözi a bevett MCP biztonsági kontrollokat a
> jelenlegi **MCP Specifikáció 2026-07-28** engedélyezési iránymutatással. Mindig hivatkozzon
> a jelenlegi [MCP Specifikációra](https://modelcontextprotocol.io/specification/2026-07-28/),
> az [MCP GitHub tárházára](https://github.com/modelcontextprotocol), és a
> [biztonsági legjobb gyakorlatok dokumentációjára](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> biztonságérzékeny kód megvalósításakor.

> **Engedélyezés frissítés:** Az MCP `2026-07-28` követeli meg az ügyfelektől, hogy ellenőrizzék az
> `iss` paramétert az engedélyezési válaszokban (RFC 9207) és kössék a regisztrált
> hitelesítő adatokat a kibocsátó engedélyező szerverhez. A Dinamikus Ügyfél Regisztráció
> elavult; az új megvalósításoknak az Ügyfélazonosító Metaadat dokumentumokat kell használniuk.
> Lásd: [Mi változott az MCP-ben: 2026-07-28 Specifikáció](../01-CoreConcepts/mcp-2026-07-28.md)
> az engedélyezési változtatások teljes listájáért.

## 🏔️ MCP Biztonsági Csúcstalálkozó Műhely (Sherpa)

A **gyakorlati biztonsági képzéshez** erősen ajánljuk az **MCP Biztonsági Csúcstalálkozó Műhelyt** (Sherpa) - egy átfogó, vezetett expedíciót az MCP szerverek Microsoft Azure-ban történő biztosítására.

### Műhely Áttekintése

A [MCP Biztonsági Csúcstalálkozó Műhely](https://azure-samples.github.io/sherpa/) gyakorlati, megvalósítható biztonsági képzést nyújt bizonyított "sebezhető → kihasználás → javítás → ellenőrzés" módszeren keresztül. A következőket teheti:

- **Tanuljon a hibákból**: Tapasztalja meg a sebezhetőségeket személyesen, véletlenül sebezhető szerverek kihasználásával
- **Használja az Azure-natív biztonságot**: Kihasználja az Azure Entra ID, Key Vault, API Management és AI Content Safety szolgáltatásokat
- **Kövesse a mélységi védelem elvét**: Haladjon előre táborok között, átfogó biztonsági rétegek kiépítésével
- **Alkalmazza az OWASP szabványokat**: Minden technika megfelel az [OWASP MCP Azure Biztonsági Útmutatónak](https://microsoft.github.io/mcp-azure-security-guide/)
- **Szerezzen működő kódot**: Hazavihet működő, tesztelt megvalósításokat

### Az expedíció útvonala

| Tábor | Fókusz | Lefedett OWASP kockázatok |
|------|-------|---------------------|
| **Alaptábor** | MCP alapok és hitelesítési sebezhetőségek | MCP01, MCP07 |
| **1. Tábor: Identitás** | OAuth 2.1, Azure Kezelt Identitás, Key Vault | MCP01, MCP02, MCP07 |
| **2. Tábor: Átjáró** | API Management, privát végpontok, irányítás | MCP02, MCP06, MCP07, MCP09 |
| **3. Tábor: Bemenet/Kimenet Biztonság** | Prompt injekció, PII védelem, tartalombiztonság | MCP03, MCP05, MCP06, MCP10 |
| **4. Tábor: Megfigyelés** | Log Analytics, műszerfalak, fenyegetésészlelés | MCP04, MCP08 |
| **A Csúcs** | Red Team / Blue Team integrációs teszt | Minden |

**Kezdje el itt**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Biztonsági Kockázat

A [OWASP MCP Azure Biztonsági Útmutató](https://microsoft.github.io/mcp-azure-security-guide/) részletezi az MCP megvalósítások tíz legkritikusabb biztonsági kockázatát:

| Kockázat | Leírás | Azure Megelőzés |
|------|-------------|------------------|
| **MCP01** | Token Kezelési Hibák és Titkok Szivárgása | Azure Key Vault, Kezelt Identitás |
| **MCP02** | Jogosultság Növelés a Scope Creep által | RBAC, Feltételes Hozzáférés |
| **MCP03** | Eszköz mérgezés | Eszköz érvényesítés, integritás ellenőrzés |
| **MCP04** | Szoftver ellátási lánc támadások és függőség manipulálás | GitHub Advanced Security, függőség szkennelés |
| **MCP05** | Parancs injekció és végrehajtás | Bemeneti érvényesítés, sandboxing |
| **MCP06** | Szándék áramló aláásás | Azure AI Content Safety, Prompt Shields |

| **MCP07** | Nem megfelelő hitelesítés és engedélyezés | Azure Entra ID, OAuth 2.1 PKCE-vel |
| **MCP08** | Auditálás és telemetria hiánya | Azure Monitor, Application Insights |
| **MCP09** | Árnyék MCP szerverek | API Center irányítás, hálózati izoláció |
| **MCP10** | Kontextus injekció és túlzott megosztás | Adatok osztályozása, minimális kitettség |

### Az MCP hitelesítés fejlődése

Az MCP specifikáció jelentősen fejlődött a hitelesítés és engedélyezés megközelítésében:

- **Eredeti megközelítés**: Korai specifikációk megkövetelték a fejlesztőktől egyedi hitelesítő szerverek megvalósítását, ahol az MCP szerverek OAuth 2.0 engedélyező szerverként közvetlenül kezelték a felhasználói hitelesítést
- **Jelenlegi szabvány (`2026-07-28`)**: Az MCP szerverek átruházhatják a hitelesítést külső identitásszolgáltatókra, például a Microsoft Entra ID-re. Az ügyfeleknek szintén alkalmazniuk kell az aktuális kibocsátó-ellenőrzési és hitelesítő adat-kötési követelményeket.
 
 
- **Átvitelréteg biztonság**: Fokozott támogatás a biztonságos átvitelhez megfelelő hitelesítési mintákkal mind helyi (STDIO), mind távoli (Streamable HTTP) kapcsolatok esetén

## Hitelesítés és engedélyezés biztonsága

### Jelenlegi biztonsági kihívások

A modern MCP implementációk több hitelesítési és engedélyezési kihívással néznek szembe:

### Kockázatok és fenyegetési vektorok

- **Hibásan konfigurált engedélyezési logika**: Az MCP szerverek hibás engedélyezési megvalósítása érzékeny adatok kiszivárgását és helytelen hozzáférés-vezérlést eredményezhet
- **OAuth token kompromittálás**: A helyi MCP szerver token lopása lehetővé teszi a támadók számára a szerverek megszemélyesítését és a további szolgáltatásokhoz való hozzáférést
- **Token továbbítási sérülékenységek**: A helytelen tokenkezelés biztonsági ellenőrzések megkerüléséhez és elszámoltathatósági hiányosságokhoz vezet
- **Túlzott jogosultságok**: A túljogosított MCP szerverek sértik a legkisebb jogosultság elvét és növelik a támadási felületet

#### Token továbbítás: Kritikus anti-minta

**A token továbbítás kifejezetten tilos** a jelenlegi MCP engedélyezési specifikációban súlyos biztonsági következményei miatt:

##### Biztonsági ellenőrzések megkerülése
- Az MCP szerverek és a downstream API-k kritikus biztonsági ellenőrzéseket (sebességkorlátozás, kérés-ellenőrzés, forgalomfigyelés) valósítanak meg, amelyek a megfelelő token érvényesítésen alapulnak
- A közvetlen kliens-API token használat megkerüli ezeket az alapvető védelmi mechanizmusokat, aláaknázva a biztonsági architektúrát

##### Elszámoltathatóság és auditálás kihívások  
- Az MCP szerverek nem tudják megkülönböztetni az upstream által kibocsátott tokeneket használó ügyfeleket, megszakítva az audit nyomvonalakat
- A downstream erőforrásszerver naplók félrevezető kérés-eredetet mutatnak az MCP szerver közvetítők helyett
- Az incidens kivizsgálás és megfelelőségi audit jelentősen megnehezedik

##### Adat kimeneti kockázatok
- Az érvénytelenített token állítások lehetővé teszik rosszindulatú szereplők számára, hogy ellopott tokenekkel MCP szervereket használjanak adatok kiszivárogtatására
- A bizalmi határok megszegése nem jogosított hozzáférési mintákat hoz létre, amelyek megkerülik a tervezett biztonsági ellenőrzéseket

##### Több szolgáltatás elleni támadási vektorok
- A kompromittált tokeneket több szolgáltatás elfogadja, lehetővé téve a rendszeroldali oldalirányú mozgást összekapcsolt rendszerek között
- A token eredetét igazolni nem tudó szolgáltatások közötti bizalmi feltevések sérülhetnek

### Biztonsági ellenőrzések és mérséklések

**Kritikus biztonsági követelmények:**

> **KÖTELEZŐ**: Az MCP szerverek **NEM FOGADHATNAK EL** olyan tokeneket, amelyeket nem kifejezetten az adott MCP szerver számára bocsátottak ki

#### Hitelesítési és engedélyezési ellenőrzések

- **Alapos engedélyezési átvizsgálás**: Teljes körű auditok az MCP szerver engedélyezési logikáján, hogy biztosítsák, hogy csak a szándékolt felhasználók és kliensek férjenek hozzá érzékeny erőforrásokhoz
  - **Megvalósítási útmutató**: [Azure API Management mint hitelesítési átjáró MCP szerverekhez](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitás integráció**: [Microsoft Entra ID használata MCP szerver hitelesítéshez](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Biztonságos token kezelés**: Megvalósítani a [Microsoft token érvényesítés és életciklus legjobb gyakorlatokat](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Érvényesíteni, hogy a token célozottsági állítások megfeleljenek az MCP szerver identitásának
  - Megvalósítani megfelelő token forgatási és lejárati szabályzatokat
  - Megelőzni a token újrajátszást és jogosulatlan használatot

- **Védett token tárolás**: Titkosított token tárolás mind nyugalmi, mind átvitel közbeni állapotban
  - **Legjobb gyakorlatok**: [Biztonságos token tárolás és titkosítási irányelvek](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Hozzáférés-vezérlés megvalósítása

- **Legkisebb jogosultság elve**: Az MCP szervereknek csak a rendelt funkcióhoz szükséges minimális jogosultságokat adni
  - Rendszeres jogosultság-átvizsgálatok és frissítések a privilégium-növekedés megelőzésére
  - **Microsoft dokumentáció**: [Biztonságos legkisebb jogosultságú hozzáférés](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Szerepalapú hozzáférés-vezérlés (RBAC)**: Finomhangolt szerepkör hozzárendelések megvalósítása
  - A szerepköröket szűken egy-egy erőforráshoz és művelethez kötni
  - Kerülni a széles vagy szükségtelen jogosultságokat, amelyek növelik a támadási felületet

- **Folyamatos jogosultság-figyelés**: Megvalósítani a folyamatos hozzáférés auditálást és monitorozást
  - Figyelni a jogosultság használati mintákat rendellenességek után kutatva
  - Azonnal kezelni a túlzott vagy fel nem használt jogosultságokat

## Mesterséges Intelligencia specifikus biztonsági fenyegetések

### Prompt injekció és eszközmanipulációs támadások

A modern MCP implementációk kifinomult, MI-specifikus támadási vektorokkal néznek szembe, amelyeket a hagyományos biztonsági intézkedések nem fednek le teljes mértékben:

#### **Közvetett prompt injekció (kereszt-domain prompt injekció)**

A **közvetett prompt injekció** az egyik legsúlyosabb sérülékenység az MCP-t támogató MI rendszerekben. A támadók rosszindulatú utasításokat rejtenek el külső tartalmakban – dokumentumokban, weboldalakon, e-mailekben vagy adatforrásokban –, amelyeket az MI rendszerek később legitim parancsként dolgoznak fel.

**Támadási forgatókönyvek:**
- **Dokumentumalapú injekció**: Rosszindulatú utasítások rejtve a feldolgozott dokumentumokban, amelyek nemkívánatos MI műveleteket váltanak ki
- **Webtartalom kihasználása**: Megfertőzött weboldalak beágyazott promptokkal, amelyek manipulálják az MI viselkedését, amikor azokat lekérik
- **E-mail alapú támadások**: Rosszindulatú promptok az e-mailekben, amelyek MI asszisztensek által információszivárgást vagy jogosulatlan műveleteket idéznek elő
- **Adatforrás szennyeződés**: Megfertőzött adatbázisok vagy API-k, amelyek szennyezett tartalmat szolgáltatnak az MI rendszereknek

**Valós hatás**: Ezek a támadások adatkiszivárgáshoz, adatvédelmi incidensekhez, ártalmas tartalmak generálásához és a felhasználói interakciók manipulációjához vezethetnek. Részletes elemzésért lásd [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/hu/prompt-injection.ed9fbfde297ca877.webp)

#### **Eszközmérgezéses támadások**

Az **eszközmérgezés** az MCP eszközök metaadataira irányul, kihasználva, hogy az LLM-ek hogyan értelmezik az eszközleírásokat és paramétereket a végrehajtási döntések meghozatalához.

**Támadási mechanizmusok:**
- **Metaadat manipuláció**: Támadók rosszindulatú utasításokat fecskendeznek be az eszközleírásokba, paraméterdefiníciókba vagy használati példákba
- **Láthatatlan utasítások**: Rejtett promptok az eszköz metaadataiban, amelyeket az MI modellek feldolgoznak, de emberi felhasználók nem látnak
- **Dinamikus eszköz módosítások ("Rug Pulls")**: A felhasználók által jóváhagyott eszközök később módosulnak, hogy rosszindulatú műveleteket hajtsanak végre felhasználói tudta nélkül
- **Paraméter injekció**: Rosszindulatú tartalom eszközparaméter sémákba ágyazva, amely befolyásolja a modell viselkedését


**Tárhelyen üzemeltetett szerverek kockázatai**: A távoli MCP szerverek fokozott kockázatot jelentenek, mivel az eszközdefiníciók a felhasználó első jóváhagyása után frissíthetők, ami olyan helyzeteket hozhat létre, ahol korábban biztonságos eszközök rosszindulatúvá válhatnak. Az alapos elemzésért lásd: [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/hu/tool-injection.3b0b4a6b24de6bef.webp)

#### **További AI támadási vektorok**

- **Domainok közötti prompt injektálás (XPIA)**: Megbízható biztonsági mechanizmusokat megkerülő, több domaint érintő kifinomult támadások
- **Dinamikus képesség módosítás**: Az eszközök képességeinek valós idejű változtatásai, amelyek elkerülik a kezdeti biztonsági értékeléseket
- **Kontextus ablak mérgezés**: Nagy kontextusablakokat manipuláló támadások, amelyek elrejtik a rosszindulatú utasításokat
- **Modell összezavarásos támadások**: A modell korlátait kihasználó, kiszámíthatatlan vagy veszélyes viselkedéseket előidéző támadások


### AI Biztonsági kockázatok hatásai

**Magas hatású következmények:**
- **Adatkiszivárgás**: Jogosulatlan hozzáférés és érzékeny vállalati vagy személyes adatok ellopása
- **Adatvédelmi incidensek**: Személyes azonosításra alkalmas információk (PII) és bizalmas üzleti adatok kiszivárogtatása  
- **Rendszermanipuláció**: Kritikus rendszerek és munkafolyamatok nem szándékolt módosítása
- **Hitelesítő adatok ellopása**: Hitelesítési tokenek és szolgáltatási hitelesítő adatok kompromittálása
- **Oldallépéses mozgás**: Megtámadott AI rendszerek támadási kiindulópontként való felhasználása szélesebb körű hálózati támadásokhoz

### Microsoft AI biztonsági megoldások

#### **AI Prompt Shields: Fejlett védelem az injektálásos támadások ellen**

A Microsoft **AI Prompt Shields** átfogó védelmet nyújt közvetlen és közvetett prompt injektálásos támadások ellen több biztonsági rétegen keresztül:

##### **Alapvető védelmi mechanizmusok:**

1. **Fejlett felismerés és szűrés**
   - Gépi tanulási algoritmusok és NLP technikák azonosítják a rosszindulatú utasításokat a külső tartalmakban
   - Dokumentumok, weboldalak, emailek és adatforrások valós idejű elemzése a beágyazott fenyegetések detektálásához
   - Kontextuális megértés a jogos és rosszindulatú promptminták között

2. **Kiemelési technikák**  
   - Megkülönbözteti a megbízható rendszerutasításokat a potenciálisan kompromittált külső bemenetektől
   - Szövegátalakítási módszerek, amelyek növelik a modell relevanciáját, miközben izolálják a rosszindulatú tartalmat
   - Segít az AI rendszereknek megőrizni a megfelelő utasítási hierarchiát és figyelmen kívül hagyni az injektált parancsokat

3. **Elválasztó és adatjelölő rendszerek**
   - Kifejezett határ meghatározása a megbízható rendszerüzenetek és külső bemeneti szöveg között
   - Speciális jelölők kiemelik a megbízható és nem megbízható adatforrások közötti határokat
   - Az egyértelmű elválasztás megelőzi az utasítási összetévesztéseket és a jogosulatlan parancsvégrehajtást

4. **Folyamatos fenyegetésinformáció**
   - A Microsoft folyamatosan figyeli a felmerülő támadási mintákat és frissíti a védelmi mechanizmusokat
   - Proaktív fenyegetésfelderítés új injektáló technikák és támadási vektorok után kutatva
   - Rendszeres biztonsági modellfrissítések az egyre változó fenyegetések elleni hatékonyság fenntartására

5. **Azure Content Safety integráció**
   - Az átfogó Azure AI Content Safety csomag része
   - Kiegészítő észlelés jailbreak-kísérletekre, káros tartalmakra és biztonsági előírások megsértésére
   - Egységes biztonsági vezérlők az AI alkalmazási komponensei között

**Megvalósítási források**: [Microsoft Prompt Shields Dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/hu/prompt-shield.ff5b95be76e9c78c.webp)


## Fejlett MCP Biztonsági Fenyegetések

### Munkamenet-eltérítési sebezhetőségek

A **munkamenet eltérítés** kritikus támadási vektort jelent állapotot tároló MCP implementációkban, ahol jogosulatlan felek jogos munkamenet-azonosítókat szereznek meg és visszaélnek velük, ügyfelek személyének eltulajdonítása és jogosulatlan műveletek végrehajtása céljából.

#### **Támadási forgatókönyvek és kockázatok**

- **Munkamenet-eltérítéses prompt injektálás**: Lopott munkamenet azonosítóval rendelkező támadók rosszindulatú eseményeket injektálnak olyan szerverekbe, amelyek megosztják a munkamenet állapotot, potenciálisan káros műveleteket indítva el vagy érzékeny adatokhoz férve hozzá
- **Közvetlen személyesítés**: Lopott munkamenet azonosítók lehetővé teszik a közvetlen MCP szerver hívásokat hitelesítés megkerülésével, a támadókat jogos felhasználóként kezelve
- **Kompromittált folytatható adatfolyamok**: A támadók idő előtt megszakíthatják a kéréseket, így a jogos ügyfelek potenciálisan rosszindulatú tartalommal folytathatják

#### **Munkamenet-kezelési biztonsági intézkedések**

**Kritikus követelmények:**
- **Engedélyezés ellenőrzése**: Az engedélyezést megvalósító MCP szerverek **MINDEN** bejövő kérést ellenőrizni **KELL**, és nem támaszkodhatnak munkamenetekre hitelesítés céljából
- **Biztonságos munkamenet-generálás**: Kriptográfiailag biztonságos, nem-determinisztikus munkamenet azonosítók használata, biztonságos véletlenszám generátorokkal
- **Felhasználóhoz kötés**: Munkamenet azonosítók kötése felhasználó-specifikus információkhoz `<user_id>:<session_id>` formában a felhasználók közötti munkamenet-visszaélések megakadályozására
- **Munkamenet életciklus kezelése**: Megfelelő lejárat, forgatás és érvénytelenítés megvalósítása a sebezhetőségi időablakok korlátozására
- **Szállítási biztonság**: Kötelező HTTPS minden kommunikációra a munkamenet azonosítók elfogása elleni védelemért

### Összezavart megbízott probléma

Az **összezavart megbízott probléma** akkor fordul elő, amikor az MCP szerverek hitelesítési proxyként működnek kliens és harmadik fél szolgáltatások között, engedélyezési kikerülési lehetőséget teremtve statikus kliens-azonosítók kihasználásával.

#### **Támadási mechanizmusok és kockázatok**

- **Cookie alapú hozzájárulás kikerülés**: Korábbi felhasználói hitelesítés hozzájárulási cookie-kat hoz létre, amelyeket a támadók rosszindulatú engedélyezési kérelmekkel, elkészített átirányítási URI-kkal kihasználnak
- **Engedélyezési kód lopás**: A meglévő hozzájárulási cookie-k miatt az engedélyezési szerverek kihagyhatják a hozzájárulási képernyőket, és a kódokat támadó által irányított végpontokra irányíthatják  
- **Jogosulatlan API hozzáférés**: Ellopott engedélyezési kódok token cserét és felhasználó személyének eltulajdonítását teszik lehetővé explicite jóváhagyás nélkül

#### **Megelőzési stratégiák**

**Kötelező vezérlések:**
- **Explicit hozzájárulási követelmények**: Az MCP proxy szerverek statikus kliens azonosítókkal **KELL**, hogy minden dinamikus regisztrációjú kliens esetében felhasználói hozzájárulást szerezzenek
- **OAuth 2.1 biztonsági megvalósítás**: Az aktuális OAuth biztonsági legjobb gyakorlatok követése, beleértve a PKCE-t (Proof Key for Code Exchange) minden engedélyezési kérelemhez
- **Szigorú kliens validálás**: Kemény validáció az átirányítási URI-k és kliens-azonosítók esetén a kihasználás megelőzése érdekében

### Token átvivő sebezhetőségek  

A **token átvivés** kifejezetten nem ajánlott gyakorlatot jelent, ahol az MCP szerverek érvényesítés nélkül fogadnak el kliens tokeneket és továbbítják őket alá-folyó API-k felé, megsértve az MCP engedélyezési specifikációit.

#### **Biztonsági következmények**

- **Szabályozás megkerülése**: A kliens közvetlen API token használata megkerüli a kritikus sebességkorlátozást, érvényesítést és felügyeleti vezérlőket
- **Audit nyomvonal sérülése**: Felülről kiadott tokenek megakadályozzák a kliensazonosítást, megnehezítve az incidenst kivizsgálását
- **Proxy alapú adatkiszivárgás**: Érvénytelenített tokenek lehetővé teszik rosszindulatú szereplőknek, hogy szervereket használjanak jogosulatlan adat-hozzáféréshez
- **Bizalmi határ átlépések**: Az aláfolyó szolgáltatások bizalmi feltevéseit megsértheti, ha a tokenek eredete nem igazolható
- **Többszolgáltatásos támadás kiterjesztés**: Széles körben elfogadott kompromittált tokenek lehetővé teszik oldallépést

#### **Szükséges biztonsági vezérlések**

**Nem tárgyalható követelmények:**
- **Token érvényesítés**: Az MCP szerverek nem fogadhatnak el kifejezetten nem nekik kiadott tokeneket
- **Célközönség ellenőrzése**: Mindig ellenőrizze, hogy a token célközönség állítása megegyezik-e az MCP szerver azonosítójával
- **Megfelelő token életciklus kezelés**: Rövid élettartamú hozzáférési tokenek és biztonságos forgatási gyakorlatok alkalmazása


## Ellátási lánc biztonság AI rendszerek számára

Az ellátási lánc biztonság a hagyományos szoftver-függőségeken túlterjedve magában foglalja az egész AI ökoszisztémát. A modern MCP implementációknak szigorúan ellenőrizniük és felügyelniük kell minden AI-rel kapcsolatos komponenst, mivel mindegyik bevezethet olyan sebezhetőségeket, amelyek veszélyeztethetik a rendszer integritását.

### Kibővített AI ellátási lánc komponensek

**Hagyományos szoftverfüggőségek:**
- Nyílt forráskódú könyvtárak és keretrendszerek
- Konténer képek és alap rendszerek  
- Fejlesztői eszközök és build pipeline-ok
- Infrastruktúra komponensek és szolgáltatások

**AI-specifikus ellátási lánc elemek:**
- **Alapmodellek**: Különféle szolgáltatóktól származó előre betanított modellek, melyek eredete igazolandó
- **Beágyazási szolgáltatások**: Külső vektorosítási és szemantikus keresési szolgáltatások
- **Kontextus szolgáltatók**: Adatforrások, tudásbázisok és dokumentumtárak  
- **Harmadik féltől származó API-k**: Külső AI szolgáltatások, gépi tanulási pipeline-ok és adatfeldolgozó végpontok
- **Modell artefaktumok**: Súlyok, konfigurációk és finomhangolt modell változatok
- **Tanító adatforrások**: Modell tanításához és finomhangolásához használt adatkészletek

### Átfogó ellátási lánc biztonsági stratégia

#### **Komponens ellenőrzés és megbízhatóság**
- **Eredet ellenőrzése**: Ellenőrizze az AI komponensek származását, licencelését és sértetlenségét az integráció előtt
- **Biztonsági értékelés**: Sebezhetőség vizsgálatok és biztonsági áttekintések modellek, adatforrások és AI szolgáltatások esetén
- **Hírnév elemzés**: Az AI szolgáltatók biztonsági múljának és gyakorlatainak értékelése
- **Megfelelőség igazolása**: Biztosítsa, hogy minden komponens megfelel a szervezeti biztonsági és szabályozási követelményeknek

#### **Biztonságos telepítési pipeline-ok**  
- **Automatizált CI/CD biztonság**: Biztonsági szkennelést építsen be az automatizált telepítési folyamatokba
- **Artefaktum sértetlenség**: Minden telepített artefaktum (kód, modellek, konfigurációk) kriptográfiai igazolása
- **Fokozatos telepítés**: Lépésenkénti telepítési stratégiák alkalmazása biztonsági ellenőrzéssel minden szakaszban
- **Megbízható artefakt tárolók**: Csak ellenőrzött, biztonságos regisztrált könyvtárakból telepítsen

#### **Folyamatos megfigyelés és reagálás**
- **Függőség szkennelés**: Folytatólagos sebezhetőség monitorozás minden szoftver és AI komponens függőségre
- **Modell monitorozás**: Folyamatos értékelése a modell viselkedésének, teljesítmény-ingadozásának és biztonsági anomáliáinak
- **Szolgáltatás egészség követés**: Külső AI szolgáltatások elérhetőségének, biztonsági incidenseknek és szabályzatváltozásoknak megfigyelése
- **Fenyegetés információ integráció**: Az AI és gépi tanulás biztonsági kockázataira specializált fenyegetésfeedek beépítése

#### **Hozzáférés-vezérlés és legkisebb jogosultság elve**
- **Komponens szintű engedélyek**: Hozzáférés korlátozása modellekhez, adatokhoz és szolgáltatásokhoz üzleti szükséglet alapján
- **Szolgáltatói fiók menedzsment**: Dedikált szolgáltatói fiókok minimális jogosultságokkal
- **Hálózati szeparáció**: AI komponensek elkülönítése és hálózati hozzáférések korlátozása a szolgáltatások között
- **API Gateway vezérlések**: Központosított API gatewayek alkalmazása a külső AI szolgáltatások hozzáférésének ellenőrzésére és monitorozására

#### **Incidens reagálás és helyreállítás**
- **Gyors reagálási eljárások**: Meghatározott folyamatok sérült AI komponensek javítására vagy cseréjére
- **Hitelesítő adatok forgatása**: Automatikus rendszerek titkok, API kulcsok és szolgáltatói hitelesítők forgatására
- **Visszaállítási képességek**: Gyors visszatérés korábbi megbízható AI komponens verziókra
- **Ellátási lánc incidens helyreállítás**: Konkrét eljárások felsőbb szintű AI szolgáltatás kompromittálások kezelésére

### Microsoft biztonsági eszközök és integráció

A **GitHub Advanced Security** átfogó ellátási lánc védelmet nyújt, többek között:
- **Titok szkennelés**: Automatizált hitelesítő adatok, API kulcsok és tokenek detektálása a tárolókban
- **Függőség szkennelés**: Nyílt forráskódú függőségek és könyvtárak sebezhetőség értékelése
- **CodeQL elemzés**: Statisztikai kódelemzés biztonsági sebezhetőségek és kódolási hibák felderítésére
- **Ellátási lánc betekintések**: Láthatóság a függőségek egészségi és biztonsági állapotára

**Azure DevOps és Azure Repos integráció:**
- Zökkenőmentes biztonsági szkennelés integráció a Microsoft fejlesztési platformjain
- Automatizált biztonsági ellenőrzések AI munkaterhelések Azure Pipelines-ban
- Szabályzati végrehajtás az AI komponensek biztonságos telepítéséhez

**Microsoft belső gyakorlatok:**
A Microsoft kiterjedt ellátási lánc biztonsági gyakorlatokat valósít meg minden termékénél. Tudjon meg többet a bevált módszerekről a [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/) oldalon.


## Alapvető Biztonsági Legjobb Gyakorlatok

Az MCP implementációk öröklik és tovább építik szervezete meglévő biztonsági helyzetét. Az alapvető biztonsági gyakorlatok megerősítése jelentősen növeli az AI rendszerek és MCP telepítések összbiztonságát.

### Alapvető biztonsági alapelvek

#### **Biztonságos fejlesztési gyakorlatok**
- **OWASP megfelelés**: Védje webalkalmazásait az [OWASP Top 10](https://owasp.org/www-project-top-ten/) sebezhetőségek ellen
- **AI-specifikus védelem**: Alkalmazzon kontrollokat az [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) szerint
- **Biztonságos titokkezelés**: Dedikált tárhelyek használata tokenek, API kulcsok és érzékeny konfigurációs adatok számára
- **Végpontok közötti titkosítás**: Biztonságos kommunikáció megvalósítása minden alkalmazás komponens és adatáramlás között
- **Bemenet-ellenőrzés**: Minden felhasználói bevitel, API paraméter és adatforrás szigorú ellenőrzése

#### **Infrastruktúra megerősítése**
- **Többlépcsős hitelesítés**: Kötelező MFA minden adminisztratív és szolgáltatói fiók számára
- **Frissítés-kezelés**: Automatizált, időben történő javítások operációs rendszerekre, keretrendszerekre és függőségekre  
- **Identitásszolgáltató integráció**: Központosított identitáskezelés vállalati identitásszolgáltatókon keresztül (Microsoft Entra ID, Active Directory)
- **Hálózati szeparáció**: MCP komponensek logikai elkülönítése az oldallépési potenciál korlátozására
- **Legkisebb jogosultság elve**: Minimális szükséges jogosultság minden rendszerkomponens és fiók számára

#### **Biztonsági monitorozás és észlelés**
- **Átfogó naplózás**: Részletes naplózás az AI alkalmazás tevékenységeiről, beleértve az MCP kliens-szerver interakciókat
- **SIEM integráció**: Központosított biztonsági információ- és eseménykezelés anomáliák észlelésére
- **Viselkedési elemzés**: AI által támogatott megfigyelés szokatlan rendszer- és felhasználói viselkedési minták felismerésére
- **Fenyegetés információ**: Külső fenyegetési feedek és kompromittálódás indikátorok (IOC) integrációja
- **Incidens reagálás**: Jól definiált eljárások a biztonsági incidensek észlelésére, kezelésére és helyreállítására

#### **Zero Trust architektúra**
- **Soha ne bízz, mindig ellenőrizz**: Folyamatos ellenőrzése a felhasználóknak, eszközöknek és hálózati kapcsolatoknak
- **Mikro-szegmentáció**: Részletes hálózati vezérlések, amelyek izolálják az egyes munkaterheléseket és szolgáltatásokat
- **Identitás-központú biztonság**: Biztonsági irányelvek ellenőrzött identitások alapján a hálózati helyett
- **Folyamatos kockázatértékelés**: Dinamikus biztonsági helyzet értékelése az aktuális kontextus és viselkedés alapján
- **Feltételes hozzáférés**: Kockázati tényezők, helyszín és eszköz megbízhatóság szerint alkalmazkodó hozzáférés-vezérlés

### Vállalati integrációs minták

#### **Microsoft biztonsági ökoszisztéma integráció**
- **Microsoft Defender for Cloud**: Átfogó felhőbiztonsági helyzetkezelés
- **Azure Sentinel**: Felhő-alapú SIEM és SOAR képességek AI munkaterhelés védelemre
- **Microsoft Entra ID**: Vállalati identitás- és hozzáférés-kezelés feltételes hozzáférési szabályokkal
- **Azure Key Vault**: Központosított titokkezelés hardveres biztonsági modullal (HSM)
- **Microsoft Purview**: Adatkezelés és megfelelőség AI adatforrások és munkafolyamatok számára

#### **Megfelelőség és irányítás**
- **Szabályozási megfelelés**: Biztosítsa, hogy az MCP implementációk megfelelnek az iparági szabályozási követelményeknek (GDPR, HIPAA, SOC 2)

- **Adatosztályozás**: Az AI rendszerek által feldolgozott érzékeny adatok megfelelő kategorizálása és kezelése
- **Ellenőrzési naplók**: Átfogó naplózás a szabályozási megfelelés és a kriminalisztikai vizsgálat érdekében
- **Adatvédelmi vezérlők**: Az adatvédelem tervezésbe építésének elveinek megvalósítása az AI rendszer architektúrájában
- **Változáskezelés**: Formális folyamatok az AI rendszer módosításainak biztonsági áttekintéséhez

Ezek az alapvető gyakorlatok stabil biztonsági alapot teremtenek, amelyek növelik az MCP-specifikus biztonsági vezérlők hatékonyságát és átfogó védelmet nyújtanak az AI-alapú alkalmazások számára.

## Fő biztonsági tanulságok

- **Többrétegű biztonsági megközelítés**: Alapvető biztonsági gyakorlatok (biztonságos kódolás, legkisebb jogosultság elve, ellátási lánc ellenőrzése, folyamatos megfigyelés) egyesítése az AI-specifikus vezérlőkkel átfogó védelem érdekében

- **AI-specifikus fenyegetettségi környezet**: Az MCP rendszerek egyedi kockázatokkal szembesülnek, mint például a prompt injekció, eszközmérgezés, munkamenet eltérítés, zavaros helyettes problémák, token átengedési sérülékenységek és túlzott jogosultságok, amelyek speciális ellenszabályokat igényelnek

- **Kiváló hitelesítés és engedélyezés**: Robusztus hitelesítés megvalósítása külső identitásszolgáltatók (Microsoft Entra ID) használatával, a tokenek megfelelő érvényesítésének betartása, és soha nem fogadni el olyan tokeneket, amelyeket nem kifejezetten az MCP szerver számára bocsátottak ki

- **AI támadások megelőzése**: Microsoft Prompt Shields és Azure Content Safety használata a közvetett prompt injekció és eszközmérgezés elleni védelemhez, miközben ellenőrzik az eszköz metaadatait és figyelik az dinamikus változásokat

- **Munkamenet- és átvitelbiztonság**: Kriptográfiailag biztonságos, nem determinisztikus munkamenet-azonosítók használata, amelyek a felhasználói identitásokhoz kötöttek, a munkamenet életciklusának megfelelő kezelése, és munkamenetek használatának mellőzése hitelesítésre

- **OAuth biztonsági legjobb gyakorlatok**: Zavaros helyettes támadások megakadályozása a dinamikusan regisztrált kliensek esetén a felhasználói nyílt beleegyezés által, az OAuth 2.1 megfelelő megvalósítása PKCE-vel, és a redirect URI szigorú ellenőrzése  

- **Token biztonsági alapelvek**: Token átengedési anti-minták kerülése, a token célközönségének érvényesítése, rövid élettartamú tokenek biztonságos forgatással, és tiszta bizalmi határok fenntartása

- **Átfogó ellátási lánc biztonság**: Minden AI ökoszisztéma komponens kezelése (modellek, beágyazások, kontextusszolgáltatók, külső API-k) ugyanazzal a biztonsági szigorral, mint a hagyományos szoftver-függőségek esetében

- **Folyamatos fejlődés**: Naprakészség megtartása a gyorsan fejlődő MCP szabványokkal, hozzájárulás a biztonsági közösségi szabványokhoz, és adaptív biztonsági megközelítések fenntartása a protokoll érésével párhuzamosan

- **Microsoft biztonsági integráció**: A Microsoft átfogó biztonsági ökoszisztémájának (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) kihasználása az MCP telepítések fokozott védelme érdekében

## Átfogó források

### **Hivatalos MCP biztonsági dokumentáció**
- [MCP specifikáció (Aktuális: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP biztonsági legjobb gyakorlatok](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP engedélyezési specifikáció](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub tárhely](https://github.com/modelcontextprotocol)

### **OWASP MCP biztonsági források**
- [OWASP MCP Azure biztonsági útmutató](https://microsoft.github.io/mcp-azure-security-guide/) - Átfogó OWASP MCP Top 10 Azure megvalósítási útmutatóval
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Hivatalos OWASP MCP biztonsági kockázatok
- [MCP biztonsági csúcstalálkozó workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Gyakorlati biztonsági tréning MCP Azure rendszerekhez

### **Biztonsági szabványok és legjobb gyakorlatok**
- [OAuth 2.0 biztonsági legjobb gyakorlatok (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 webalkalmazás-biztonság](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 nagyméretű nyelvi modellekhez](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digitális Védelem Jelentés](https://aka.ms/mddr)

### **AI biztonsági kutatás és elemzés**
- [Prompt Injekció az MCP-ben (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Eszközmérgezési támadások (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP biztonsági kutatási összefoglaló (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft biztonsági megoldások**
- [Microsoft Prompt Shields dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety szolgáltatás](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID biztonság](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure token kezelési legjobb gyakorlatok](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Megvalósítási útmutatók és oktatóanyagok**
- [Azure API Management mint MCP hitelesítési átjáró](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID hitelesítés MCP szerverekhez](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Biztonságos token tárolás és titkosítás (videó)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps és ellátási lánc biztonság**
- [Azure DevOps biztonság](https://azure.microsoft.com/products/devops)
- [Azure Repos biztonság](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft ellátási lánc biztonsági útja](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **További biztonsági dokumentáció**

Átfogó biztonsági útmutatásért olvassa el az ebben a szakaszban található speciális dokumentumokat:

- **[CIMD és DCR engedélyezési minta](./samples/cimd-dcr-auth/README.md)** - Futtatható TypeScript MCP `2026-07-28` erőforrás szerver, amely összehasonlítja a preferált Client ID Metadata Documents dokumentumokat a megszűnő Dynamic Client Registration visszalépéssel
- **[MCP biztonsági legjobb gyakorlatok](./mcp-security-best-practices.md)** - Teljes biztonsági legjobb gyakorlatok MCP megvalósításokhoz
- **[Azure Content Safety megvalósítás](./azure-content-safety-implementation.md)** - Gyakorlati megvalósítási példák az Azure Content Safety integrációhoz  
- **[MCP biztonsági vezérlők](./mcp-security-controls.md)** - Legfrissebb biztonsági vezérlők és technikák MCP telepítésekhez
- **[MCP legjobb gyakorlatok gyors referencia](./mcp-best-practices.md)** - Gyors referencia útmutató az alapvető MCP biztonsági gyakorlatokhoz
- **[BlueHat 2026: Az AI jövőjének védelme: MCP védelme több rétegű védelemmel](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Többrétegű védelem minták a Microsoft Biztonsági Reagálási Központjától (MSRC)

### **Gyakorlati biztonsági képzés**

- **[MCP biztonsági csúcstalálkozó workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Átfogó, gyakorlati workshop az MCP Azure szerverek védelméhez alapozó tábortól a csúcstalálkozóig
- **[OWASP MCP Azure biztonsági útmutató](https://microsoft.github.io/mcp-azure-security-guide/)** - Referencia architektúra és megvalósítási útmutató minden OWASP MCP Top 10 kockázathoz

---

## Mi következik

Következő: [3. fejezet: Első lépések](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->