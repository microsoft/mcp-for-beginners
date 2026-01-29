# MCP Biztonság: Átfogó védelem az MI rendszerek számára

[![MCP Security Best Practices](../../../translated_images/hu/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

A biztonság alapvető az MI rendszerek tervezésében, ezért második szekciónkban kiemelten foglalkozunk vele. Ez összhangban áll a Microsoft **Secure by Design** elvével a [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/) keretében.

A Model Context Protocol (MCP) erőteljes új képességeket hoz az MI-vezérelt alkalmazásokba, miközben egyedi biztonsági kihívásokat is felvet, amelyek túlmutatnak a hagyományos szoftverkockázatokon. Az MCP rendszerek mind a bevett biztonsági kérdésekkel (biztonságos kódolás, legkisebb jogosultság elve, ellátási lánc biztonság), mind az új MI-specifikus fenyegetésekkel szembesülnek, beleértve a prompt injekciót, eszközmérgezést, munkamenet eltérítést, confused deputy támadásokat, token átengedési sérülékenységeket és dinamikus képességmódosítást.

Ez a lecke az MCP megvalósítások legkritikusabb biztonsági kockázatait vizsgálja — beleértve az autentikációt, autorizációt, túlzott jogosultságokat, közvetett prompt injekciót, munkamenet biztonságot, confused deputy problémákat, token kezelést és ellátási lánc sérülékenységeket. Gyakorlati vezérlőket és bevált gyakorlatokat tanulhat meg ezek kockázatainak mérséklésére, miközben kihasználja a Microsoft megoldásait, mint a Prompt Shields, Azure Content Safety és GitHub Advanced Security az MCP telepítésének megerősítésére.

## Tanulási célok

A lecke végére képes lesz:

- **MCP-specifikus fenyegetések azonosítása**: Felismerni az MCP rendszerek egyedi biztonsági kockázatait, beleértve a prompt injekciót, eszközmérgezést, túlzott jogosultságokat, munkamenet eltérítést, confused deputy problémákat, token átengedési sérülékenységeket és ellátási lánc kockázatokat
- **Biztonsági vezérlők alkalmazása**: Hatékony mérséklések bevezetése, beleértve a robusztus autentikációt, legkisebb jogosultság elvét, biztonságos token kezelést, munkamenet biztonsági vezérlőket és ellátási lánc ellenőrzést
- **Microsoft biztonsági megoldások kihasználása**: A Microsoft Prompt Shields, Azure Content Safety és GitHub Advanced Security megértése és telepítése az MCP munkaterhelés védelmére
- **Eszközbiztonság validálása**: Az eszköz metaadatainak validálásának fontosságának felismerése, a dinamikus változások figyelése és a közvetett prompt injekciós támadások elleni védelem
- **Bevált gyakorlatok integrálása**: A bevett biztonsági alapelvek (biztonságos kódolás, szerver megerősítés, zero trust) és az MCP-specifikus vezérlők kombinálása az átfogó védelem érdekében

# MCP Biztonsági architektúra és vezérlők

A modern MCP megvalósítások rétegzett biztonsági megközelítéseket igényelnek, amelyek mind a hagyományos szoftverbiztonságot, mind az MI-specifikus fenyegetéseket kezelik. Az MCP specifikáció gyorsan fejlődik, folyamatosan érik biztonsági vezérlői, lehetővé téve a jobb integrációt a vállalati biztonsági architektúrákkal és a bevált gyakorlatokkal.

A [Microsoft Digital Defense Report](https://aka.ms/mddr) kutatása szerint a **jelentett incidensek 98%-a megelőzhető lenne robusztus biztonsági higiéniával**. A leghatékonyabb védekezési stratégia az alapvető biztonsági gyakorlatok és az MCP-specifikus vezérlők kombinációja — a bizonyított alapbiztonsági intézkedések a legnagyobb hatással vannak az összesített biztonsági kockázat csökkentésére.

## Jelenlegi biztonsági helyzet

> **Megjegyzés:** Ez az információ az MCP biztonsági szabványokat tükrözi **2025. december 18-án**. Az MCP protokoll gyorsan fejlődik, és a jövőbeni megvalósítások új autentikációs mintákat és továbbfejlesztett vezérlőket vezethetnek be. Mindig hivatkozzon a jelenlegi [MCP specifikációra](https://spec.modelcontextprotocol.io/), [MCP GitHub tárházra](https://github.com/modelcontextprotocol) és a [biztonsági bevált gyakorlatok dokumentációjára](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) a legfrissebb útmutatásért.

### Az MCP autentikáció fejlődése

Az MCP specifikáció jelentősen fejlődött az autentikáció és autorizáció megközelítésében:

- **Eredeti megközelítés**: Korai specifikációk megkövetelték, hogy a fejlesztők egyedi autentikációs szervereket valósítsanak meg, az MCP szerverek pedig OAuth 2.0 autorizációs szerverként működtek, közvetlenül kezelve a felhasználói autentikációt
- **Jelenlegi szabvány (2025-11-25)**: A frissített specifikáció lehetővé teszi, hogy az MCP szerverek külső identitásszolgáltatókra (például Microsoft Entra ID) delegálják az autentikációt, javítva a biztonsági helyzetet és csökkentve a megvalósítási komplexitást
- **Transzport réteg biztonság**: Fejlesztett támogatás a biztonságos transzport mechanizmusokhoz, megfelelő autentikációs mintákkal mind helyi (STDIO), mind távoli (Streamable HTTP) kapcsolatokhoz

## Autentikáció és autorizáció biztonsága

### Jelenlegi biztonsági kihívások

A modern MCP megvalósítások több autentikációs és autorizációs kihívással néznek szembe:

### Kockázatok és fenyegetési vektorok

- **Helytelenül konfigurált autorizációs logika**: Hibás autorizációs megvalósítás az MCP szervereken érzékeny adatok kiszivárgását és helytelen hozzáférés-ellenőrzést eredményezhet
- **OAuth token kompromittálás**: A helyi MCP szerver token lopása lehetővé teszi a támadók számára a szerverek megszemélyesítését és downstream szolgáltatások elérését
- **Token átengedési sérülékenységek**: Hibás token kezelés biztonsági vezérlők megkerülését és elszámoltathatósági hiányosságokat okoz
- **Túlzott jogosultságok**: Túljogosított MCP szerverek megsértik a legkisebb jogosultság elvét és növelik a támadási felületet

#### Token átengedés: Kritikus anti-minta

A **token átengedés kifejezetten tilos** a jelenlegi MCP autorizációs specifikációban súlyos biztonsági következményei miatt:

##### Biztonsági vezérlők megkerülése
- Az MCP szerverek és downstream API-k kritikus biztonsági vezérlőket valósítanak meg (sebességkorlátozás, kérés validáció, forgalomfigyelés), amelyek a megfelelő token érvényesítésen alapulnak
- A közvetlen kliens-API token használat megkerüli ezeket az alapvető védelmeket, aláássa a biztonsági architektúrát

##### Elsámoltathatósági és auditálási kihívások  
- Az MCP szerverek nem tudják megkülönböztetni az upstream által kibocsátott tokeneket használó klienseket, megszakítva az audit nyomvonalakat
- A downstream erőforrás szerver naplók félrevezető kérés eredeteket mutatnak az MCP szerver közvetítők helyett
- Az incidens kivizsgálás és megfelelőségi auditálás jelentősen nehezebbé válik

##### Adatkiszivárgási kockázatok
- Az érvénytelenített token állítások lehetővé teszik a rosszindulatú szereplők számára, hogy ellopott tokenekkel MCP szervereket proxyként használjanak adatkiszivárgáshoz
- A bizalmi határok megsértése jogosulatlan hozzáférési mintákat enged meg, amelyek megkerülik a tervezett biztonsági vezérlőket

##### Több szolgáltatás elleni támadási vektorok
- A kompromittált tokenek több szolgáltatás által történő elfogadása lehetővé teszi a laterális mozgást a kapcsolódó rendszerek között
- A szolgáltatások közötti bizalmi feltételezések sérülhetnek, ha a token eredete nem ellenőrizhető

### Biztonsági vezérlők és mérséklések

**Kritikus biztonsági követelmények:**

> **KÖTELEZŐ**: Az MCP szerverek **NEM FOGADHATNAK EL** olyan tokeneket, amelyeket nem kifejezetten az MCP szerver számára bocsátottak ki

#### Autentikációs és autorizációs vezérlők

- **Alapos autorizációs felülvizsgálat**: Átfogó auditok végrehajtása az MCP szerver autorizációs logikáján, hogy csak a szándékolt felhasználók és kliensek férhessenek hozzá érzékeny erőforrásokhoz
  - **Megvalósítási útmutató**: [Azure API Management mint autentikációs átjáró MCP szerverekhez](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identitás integráció**: [Microsoft Entra ID használata MCP szerver autentikációhoz](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Biztonságos token kezelés**: A [Microsoft token validációs és életciklus bevált gyakorlatai](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) alkalmazása
  - Token audience állítások validálása, hogy megfeleljenek az MCP szerver identitásának
  - Megfelelő token forgatási és lejárati szabályzatok bevezetése
  - Token replay támadások és jogosulatlan használat megelőzése

- **Védett token tárolás**: Tokenek titkosított tárolása mind nyugalmi, mind átvitel közbeni állapotban
  - **Bevált gyakorlatok**: [Biztonságos token tárolás és titkosítási irányelvek](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Hozzáférés-vezérlés megvalósítása

- **Legkisebb jogosultság elve**: Csak a szükséges minimális jogosultságok megadása az MCP szervereknek a kívánt funkciókhoz
  - Rendszeres jogosultság felülvizsgálatok és frissítések a jogosultság növekedés megelőzésére
  - **Microsoft dokumentáció**: [Biztonságos legkisebb jogosultságú hozzáférés](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Szerepkör alapú hozzáférés-vezérlés (RBAC)**: Finomhangolt szerepkör hozzárendelések megvalósítása
  - Szerepkörök szoros korlátozása konkrét erőforrásokra és műveletekre
  - Kerülje a széles vagy szükségtelen jogosultságokat, amelyek növelik a támadási felületet

- **Folyamatos jogosultságfigyelés**: Folyamatos hozzáférési auditálás és monitorozás bevezetése
  - Jogosultság használati minták figyelése anomáliákra
  - Túlzott vagy nem használt jogosultságok gyors javítása

## MI-specifikus biztonsági fenyegetések

### Prompt injekció és eszközmanipulációs támadások

A modern MCP megvalósítások kifinomult MI-specifikus támadási vektorokkal néznek szembe, amelyeket a hagyományos biztonsági intézkedések nem képesek teljes mértékben kezelni:

#### **Közvetett prompt injekció (tartományok közötti prompt injekció)**

A **közvetett prompt injekció** az egyik legkritikusabb sérülékenység az MCP-vel engedélyezett MI rendszerekben. A támadók rosszindulatú utasításokat ágyaznak be külső tartalmakba — dokumentumokba, weboldalakba, e-mailekbe vagy adatforrásokba — amelyeket az MI rendszerek később legitim parancsként dolgoznak fel.

**Támadási forgatókönyvek:**
- **Dokumentum alapú injekció**: Rosszindulatú utasítások rejtve a feldolgozott dokumentumokban, amelyek nem kívánt MI műveleteket váltanak ki
- **Webtartalom kihasználása**: Megfertőzött weboldalak beágyazott promptokkal, amelyek az MI viselkedését manipulálják, amikor azokat lekérik
- **E-mail alapú támadások**: Rosszindulatú promptok e-mailekben, amelyek MI asszisztenseket késztetnek információszivárgásra vagy jogosulatlan műveletekre
- **Adatforrás szennyezés**: Megfertőzött adatbázisok vagy API-k, amelyek szennyezett tartalmat szolgáltatnak az MI rendszereknek

**Valós hatás**: Ezek a támadások adatkiszivárgáshoz, adatvédelmi incidensekhez, káros tartalom generálásához és felhasználói interakciók manipulálásához vezethetnek. Részletes elemzésért lásd: [Prompt Injection az MCP-ben (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/hu/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Eszközmérgezéses támadások**

Az **eszközmérgezés** az MCP eszközöket definiáló metaadatokat célozza meg, kihasználva, hogy a nagy nyelvi modellek hogyan értelmezik az eszközleírásokat és paramétereket a végrehajtási döntésekhez.

**Támadási mechanizmusok:**
- **Metaadat manipuláció**: Támadók rosszindulatú utasításokat injektálnak az eszközleírásokba, paraméterdefiníciókba vagy használati példákba
- **Láthatatlan utasítások**: Rejtett promptok az eszköz metaadatokban, amelyeket az MI modellek feldolgoznak, de az emberi felhasználók nem látnak
- **Dinamikus eszköz módosítás ("Rug Pulls")**: Felhasználók által jóváhagyott eszközök később módosulnak rosszindulatú műveletek végrehajtására a felhasználó tudta nélkül
- **Paraméter injekció**: Rosszindulatú tartalom beágyazása az eszköz paraméter sémákba, amely befolyásolja a modell viselkedését

**Hosztolt szerver kockázatok**: A távoli MCP szerverek fokozott kockázatot jelentenek, mivel az eszközdefiníciók a felhasználói jóváhagyás után is frissíthetők, olyan helyzeteket teremtve, ahol korábban biztonságos eszközök rosszindulatúvá válhatnak. Átfogó elemzésért lásd: [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/hu/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **További MI támadási vektorok**

- **Tartományok közötti prompt injekció (XPIA)**: Kifinomult támadások, amelyek több tartomány tartalmát használják fel a biztonsági vezérlők megkerülésére
- **Dinamikus képességmódosítás**: Valós idejű változtatások az eszköz képességein, amelyek elkerülik a kezdeti biztonsági értékeléseket
- **Kontextusablak mérgezés**: Támadások, amelyek nagy kontextusablakokat manipulálnak rosszindulatú utasítások elrejtésére
- **Modell zavar támadások**: A modell korlátainak kihasználása kiszámíthatatlan vagy nem biztonságos viselkedések létrehozására

### MI biztonsági kockázatok hatása

**Magas hatású következmények:**
- **Adatkiszivárgás**: Jogosulatlan hozzáférés és érzékeny vállalati vagy személyes adatok ellopása
- **Adatvédelmi incidensek**: Személyes azonosításra alkalmas adatok (PII) és bizalmas üzleti adatok kiszivárgása  
- **Rendszermanipuláció**: Kritikus rendszerek és munkafolyamatok nem kívánt módosítása
- **Hitelesítő adatok lopása**: Autentikációs tokenek és szolgáltatási hitelesítő adatok kompromittálása
- **Laterális mozgás**: Kompromittált MI rendszerek használata szélesebb hálózati támadások pivot pontjaként

### Microsoft MI biztonsági megoldások

#### **AI Prompt Shields: Fejlett védelem injekciós támadások ellen**

A Microsoft **AI Prompt Shields** átfogó védelmet nyújtanak mind közvetlen, mind közvetett prompt injekciós támadások ellen több biztonsági rétegen keresztül:

##### **Alapvető védelmi mechanizmusok:**

1. **Fejlett észlelés és szűrés**
   - Gépi tanulási algoritmusok és NLP technikák felismerik a rosszindulatú utasításokat a külső tartalmakban
   - Valós idejű elemzés dokumentumok, weboldalak, e-mailek és adatforrások beágyazott fenyegetéseire
   - Kontextuális megértés a legitim és rosszindulatú prompt minták között

2. **Kiemelési technikák**  
   - Megkülönbözteti a megbízható rendszerutasításokat a potenciálisan kompromittált külső bemenetektől
   - Szövegtranszformációs módszerek, amelyek növelik a modell relevanciáját, miközben izolálják a rosszindulatú tartalmat
   - Segíti az MI rendszereket a megfelelő utasítás hierarchia fenntartásában és az injektált parancsok figyelmen kívül hagyásában

3. **Elválasztó és adatjelölő rendszerek**
   - Kifejezett határvonal meghatározása a megbízható rendszerüzenetek és a külső bemeneti szöveg között
   - Különleges jelölők kiemelik a határokat a megbízható és nem megbízható adatforrások között
   - Egyértelmű elkülönítés megakadályozza az utasítások összekeveredését és a jogosulatlan parancsvégrehajtást

4. **Folyamatos fenyegetés intelligencia**
   - A Microsoft folyamatosan figyeli a felmerülő támadási mintákat és frissíti a védelmi mechanizmusokat
   - Proaktív fenyegetéskutatás új injekciós technikák és támadási vektorok ellen
   - Rendszeres biztonsági modell frissítések az evolúciós fenyegetések elleni hatékonyság fenntartására

5. **Azure Content Safety integráció**
   - Az átfogó Azure AI Content Safety csomag része
   - További észlelés jailbreak kísérletekre, káros tartalmakra és biztonsági szabályzat megsértésekre
   - Egységes biztonsági vezérlők az MI alkalmazás komponensei között

**Megvalósítási források**: [Microsoft Prompt Shields dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/hu/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Fejlett MCP biztonsági fenyegetések

### Munkamenet eltérítési sérülékenységek

A **munkamenet eltérítés** kritikus támadási vektor az állapotmegőrző MCP megvalósításokban, ahol jogosulatlan felek megszerzik és visszaélnek a legitim munkamenet-azonosítókkal, hogy klienseket megszemélyesítve jogosulatlan műveleteket hajtsanak végre.

#### **Támadási forgatókönyvek és kockázatok**

- **Munkamenet eltérítéses prompt injekció**: A lopott munkamenetazonosítóval rendelkező támadók rosszindulatú eseményeket injektálnak olyan szerverekbe, amelyek megosztják a munkamenet állapotot, potenciálisan káros műveleteket váltva ki vagy érzékeny adatokhoz férve hozzá
- **Közvetlen megszemélyesítés**: A lopott munkamenetazonosítók lehetővé teszik a közvetlen MCP szerver hívásokat, amelyek megkerülik az autentikációt, a támadókat legitim felhasználóként kezelve
- **Kompromittált folytatható adatfolyamok**: A támadók idő előtt megszakíthatják a kéréseket, ami miatt a legitim kliensek potenciálisan rosszindulatú tartalommal folytatják a munkamenetet

#### **Munkamenet-kezelés biztonsági vezérlői**

**Kritikus követelmények:**
- **Hitelesítés ellenőrzése**: Az MCP szerverek, amelyek hitelesítést valósítanak meg, **MINDEN** bejövő kérést ellenőrizniuk kell, és **NEM SZABAD** munkamenetekre támaszkodniuk az azonosításhoz
- **Biztonságos munkamenet-generálás**: Kriptográfiailag biztonságos, nem determinisztikus munkamenet-azonosítókat kell használni, amelyeket biztonságos véletlenszám-generátorokkal hoznak létre
- **Felhasználó-specifikus kötés**: A munkamenet-azonosítókat felhasználó-specifikus információkhoz kell kötni olyan formátumokkal, mint `<user_id>:<session_id>`, hogy megakadályozzák a munkamenet visszaéléseket felhasználók között
- **Munkamenet életciklus-kezelés**: Megfelelő lejáratot, forgatást és érvénytelenítést kell megvalósítani a sérülékenységi ablakok korlátozására
- **Átvitel biztonsága**: Kötelező HTTPS minden kommunikációhoz a munkamenet-azonosítók elfogásának megakadályozására

### Zavarodott helyettes probléma

A **zavarodott helyettes probléma** akkor fordul elő, amikor az MCP szerverek hitelesítési proxyként működnek az ügyfelek és harmadik fél szolgáltatások között, lehetőséget teremtve az engedélyezés megkerülésére statikus kliensazonosító kihasználásával.

#### **Támadási mechanizmusok és kockázatok**

- **Cookie-alapú hozzájárulás megkerülés**: Korábbi felhasználói hitelesítés hozzájárulási cookie-kat hoz létre, amelyeket a támadók rosszindulatú engedélyezési kérésekkel, előre elkészített átirányítási URI-kkal kihasználnak
- **Engedélyezési kód lopás**: A meglévő hozzájárulási cookie-k miatt az engedélyező szerverek kihagyhatják a hozzájárulási képernyőket, és a kódokat támadó által ellenőrzött végpontokra irányítják  
- **Jogosulatlan API-hozzáférés**: A lopott engedélyezési kódok lehetővé teszik a tokencserét és a felhasználó megszemélyesítését jóváhagyás nélkül

#### **Megelőzési stratégiák**

**Kötelező ellenőrzések:**
- **Explicit hozzájárulás követelmények**: Az MCP proxy szerverek, amelyek statikus kliensazonosítókat használnak, **KÖTELESEK** minden dinamikusan regisztrált kliens esetén felhasználói hozzájárulást kérni
- **OAuth 2.1 biztonsági megvalósítás**: Kövesse az aktuális OAuth biztonsági legjobb gyakorlatokat, beleértve a PKCE-t (Proof Key for Code Exchange) minden engedélyezési kérésnél
- **Szigorú kliens-ellenőrzés**: Alapos ellenőrzést kell végezni az átirányítási URI-kon és kliensazonosítókon a kihasználás megakadályozására

### Token átengedési sérülékenységek  

A **token átengedés** egy kifejezett anti-minta, ahol az MCP szerverek kliens tokeneket fogadnak el megfelelő ellenőrzés nélkül, és továbbítják azokat a downstream API-k felé, megsértve az MCP engedélyezési előírásokat.

#### **Biztonsági következmények**

- **Ellenőrzés megkerülése**: A közvetlen kliens-API token használat megkerüli a kritikus sebességkorlátozást, ellenőrzést és monitorozást
- **Audit nyomvonal sérülése**: A felülről kiadott tokenek miatt lehetetlen azonosítani a klienst, ami megakadályozza az incidensek vizsgálatát
- **Proxy alapú adatkivitel**: Az ellenőrizetlen tokenek lehetővé teszik rosszindulatú szereplők számára, hogy a szervereket proxyként használják jogosulatlan adat-hozzáféréshez
- **Bizalmi határ megsértése**: A downstream szolgáltatások bizalmi feltételezései sérülhetnek, ha a token eredete nem ellenőrizhető
- **Több szolgáltatás elleni támadás kiterjesztése**: A kompromittált tokenek több szolgáltatásban elfogadva oldalirányú mozgást tesznek lehetővé

#### **Szükséges biztonsági ellenőrzések**

**Nem tárgyalható követelmények:**
- **Token ellenőrzés**: Az MCP szerverek **NEM FOGLALHATNAK EL** olyan tokeneket, amelyeket nem kifejezetten az MCP szerver számára bocsátottak ki
- **Célközönség ellenőrzése**: Mindig ellenőrizze, hogy a token célközönségi állításai megfelelnek-e az MCP szerver azonosítójának
- **Megfelelő token életciklus**: Rövid élettartamú hozzáférési tokeneket kell alkalmazni biztonságos forgatási gyakorlatokkal


## Ellátási lánc biztonság AI rendszerekhez

Az ellátási lánc biztonság túllépett a hagyományos szoftverfüggőségeken, és magában foglalja az egész AI ökoszisztémát. A modern MCP megvalósításoknak szigorúan ellenőrizniük és monitorozniuk kell minden AI-hoz kapcsolódó komponenst, mivel mindegyik potenciális sérülékenységet jelenthet, amely veszélyeztetheti a rendszer integritását.

### Kiterjesztett AI ellátási lánc komponensek

**Hagyományos szoftverfüggőségek:**
- Nyílt forráskódú könyvtárak és keretrendszerek
- Konténer képek és alap rendszerek  
- Fejlesztői eszközök és build pipeline-ok
- Infrastruktúra komponensek és szolgáltatások

**AI-specifikus ellátási lánc elemek:**
- **Alapmodellek**: Különböző szolgáltatóktól származó előre betanított modellek, amelyek eredetiség-ellenőrzést igényelnek
- **Beágyazási szolgáltatások**: Külső vektorizációs és szemantikus keresési szolgáltatások
- **Kontekstus szolgáltatók**: Adatforrások, tudásbázisok és dokumentumtárak  
- **Harmadik fél API-k**: Külső AI szolgáltatások, ML pipeline-ok és adatfeldolgozó végpontok
- **Modell artefaktumok**: Súlyok, konfigurációk és finomhangolt modellváltozatok
- **Képzési adatforrások**: A modell tanításához és finomhangolásához használt adatkészletek

### Átfogó ellátási lánc biztonsági stratégia

#### **Komponens ellenőrzés és bizalom**
- **Eredetiség ellenőrzés**: Ellenőrizze az összes AI komponens eredetét, licencelését és integritását az integráció előtt
- **Biztonsági értékelés**: Végezzen sérülékenységvizsgálatot és biztonsági áttekintést modelleken, adatforrásokon és AI szolgáltatásokon
- **Hírnév elemzés**: Értékelje az AI szolgáltatók biztonsági múltját és gyakorlatait
- **Megfelelőség ellenőrzés**: Biztosítsa, hogy minden komponens megfeleljen a szervezeti biztonsági és szabályozási követelményeknek

#### **Biztonságos telepítési pipeline-ok**  
- **Automatizált CI/CD biztonság**: Integrálja a biztonsági vizsgálatokat az automatizált telepítési pipeline-okba
- **Artefaktum integritás**: Kriptográfiai ellenőrzést alkalmazzon minden telepített artefaktumra (kód, modellek, konfigurációk)
- **Fokozatos telepítés**: Használjon progresszív telepítési stratégiákat biztonsági ellenőrzéssel minden lépésben
- **Megbízható artefaktum tárolók**: Csak ellenőrzött, biztonságos artefaktum regisztrációkból és tárolókból telepítsen

#### **Folyamatos monitorozás és reagálás**
- **Függőség vizsgálat**: Folyamatos sérülékenységfigyelés minden szoftver- és AI komponens függőségre
- **Modell monitorozás**: Folyamatos értékelés a modell viselkedéséről, teljesítmény eltérésről és biztonsági anomáliákról
- **Szolgáltatás egészség követés**: Külső AI szolgáltatások elérhetőségének, biztonsági eseményeinek és szabályzatváltozásainak monitorozása
- **Fenyegetés intelligencia integráció**: AI és ML biztonsági kockázatokra vonatkozó fenyegetés adatfolyamok beépítése

#### **Hozzáférés-vezérlés és legkisebb jogosultság**
- **Komponens szintű jogosultságok**: Korlátozza a hozzáférést modellekhez, adatokhoz és szolgáltatásokhoz üzleti szükséglet alapján
- **Szolgáltatás fiók kezelése**: Dedikált szolgáltatásfiókok alkalmazása minimális szükséges jogosultságokkal
- **Hálózati szegmentáció**: AI komponensek izolálása és hálózati hozzáférés korlátozása a szolgáltatások között
- **API kapu vezérlés**: Központosított API kapuk használata a külső AI szolgáltatásokhoz való hozzáférés szabályozására és monitorozására

#### **Incidens válasz és helyreállítás**
- **Gyors reagálási eljárások**: Meglévő folyamatok a kompromittált AI komponensek javítására vagy cseréjére
- **Hitelesítő adatok forgatása**: Automatikus rendszerek titkok, API kulcsok és szolgáltatás hitelesítő adatok forgatására
- **Visszaállítási képességek**: Gyors visszatérés korábban ismert jó AI komponens verziókra
- **Ellátási lánc sérülés helyreállítás**: Specifikus eljárások a felülről érkező AI szolgáltatás kompromittálására adott válaszra

### Microsoft biztonsági eszközök és integráció

A **GitHub Advanced Security** átfogó ellátási lánc védelmet nyújt, beleértve:
- **Titok keresés**: Automatikus hitelesítő adatok, API kulcsok és tokenek felismerése a tárolókban
- **Függőség vizsgálat**: Sérülékenység értékelés nyílt forráskódú függőségekre és könyvtárakra
- **CodeQL elemzés**: Statikus kódelemzés biztonsági sérülékenységek és kódolási hibák felderítésére
- **Ellátási lánc betekintés**: Láthatóság a függőségek egészségére és biztonsági állapotára

**Azure DevOps és Azure Repos integráció:**
- Zökkenőmentes biztonsági vizsgálat integráció a Microsoft fejlesztői platformokon
- Automatizált biztonsági ellenőrzések Azure Pipeline-okban AI munkaterhelésekhez
- Szabályzat érvényesítés biztonságos AI komponens telepítéshez

**Microsoft belső gyakorlatok:**
A Microsoft kiterjedt ellátási lánc biztonsági gyakorlatokat alkalmaz minden termékében. Ismerje meg a bevált megközelítéseket a [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/) oldalon.


## Alapvető biztonsági legjobb gyakorlatok

Az MCP megvalósítások öröklik és továbbépítik a szervezet meglévő biztonsági helyzetét. Az alapvető biztonsági gyakorlatok megerősítése jelentősen növeli az AI rendszerek és MCP telepítések általános biztonságát.

### Alapvető biztonsági alapelvek

#### **Biztonságos fejlesztési gyakorlatok**
- **OWASP megfelelés**: Védelem az [OWASP Top 10](https://owasp.org/www-project-top-ten/) webalkalmazás sérülékenységek ellen
- **AI-specifikus védelem**: Intézkedések megvalósítása az [OWASP Top 10 LLM-ekhez](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Biztonságos titokkezelés**: Dedikált tárolók használata tokenek, API kulcsok és érzékeny konfigurációs adatok számára
- **Végpontok közötti titkosítás**: Biztonságos kommunikáció megvalósítása az összes alkalmazás komponens és adatfolyam között
- **Bemenet ellenőrzés**: Minden felhasználói bemenet, API paraméter és adatforrás szigorú ellenőrzése

#### **Infrastruktúra megerősítése**
- **Többfaktoros hitelesítés**: Kötelező MFA minden adminisztratív és szolgáltatásfiókhoz
- **Javításkezelés**: Automatikus, időben történő javítás operációs rendszerekre, keretrendszerekre és függőségekre  
- **Identitásszolgáltató integráció**: Központosított identitáskezelés vállalati identitásszolgáltatókon keresztül (Microsoft Entra ID, Active Directory)
- **Hálózati szegmentáció**: MCP komponensek logikai izolálása az oldalirányú mozgás korlátozására
- **Legkisebb jogosultság elve**: Minimális szükséges jogosultságok minden rendszerkomponens és fiók számára

#### **Biztonsági monitorozás és észlelés**
- **Átfogó naplózás**: Részletes naplózás AI alkalmazás tevékenységekről, beleértve az MCP kliens-szerver interakciókat
- **SIEM integráció**: Központosított biztonsági információ- és eseménykezelés anomáliák észlelésére
- **Viselkedéselemzés**: AI-alapú monitorozás a szokatlan rendszer- és felhasználói minták felismerésére
- **Fenyegetés intelligencia**: Külső fenyegetés adatfolyamok és kompromittálódási indikátorok (IOC) integrálása
- **Incidens válasz**: Jól definiált eljárások biztonsági incidensek észlelésére, reagálásra és helyreállításra

#### **Zero Trust architektúra**
- **Soha ne bízz, mindig ellenőrizz**: Folyamatos felhasználó-, eszköz- és hálózati kapcsolat ellenőrzés
- **Mikroszegmentáció**: Részletes hálózati szabályozás, amely izolálja az egyes munkaterheléseket és szolgáltatásokat
- **Identitás-központú biztonság**: Biztonsági szabályzatok ellenőrzött identitások alapján, nem hálózati hely szerint
- **Folyamatos kockázatértékelés**: Dinamikus biztonsági helyzet értékelés a jelenlegi kontextus és viselkedés alapján
- **Feltételes hozzáférés**: Hozzáférés-vezérlés, amely alkalmazkodik a kockázati tényezőkhöz, helyhez és eszköz megbízhatósághoz

### Vállalati integrációs minták

#### **Microsoft biztonsági ökoszisztéma integráció**
- **Microsoft Defender for Cloud**: Átfogó felhőbiztonsági helyzetkezelés
- **Azure Sentinel**: Felhőalapú SIEM és SOAR képességek AI munkaterhelések védelmére
- **Microsoft Entra ID**: Vállalati identitás- és hozzáféréskezelés feltételes hozzáférési szabályzatokkal
- **Azure Key Vault**: Központosított titokkezelés hardveres biztonsági modul (HSM) támogatással
- **Microsoft Purview**: Adatkezelés és megfelelőség AI adatforrások és munkafolyamatok számára

#### **Megfelelőség és irányítás**
- **Szabályozási megfelelés**: Biztosítsa, hogy az MCP megvalósítások megfeleljenek az iparági megfelelőségi követelményeknek (GDPR, HIPAA, SOC 2)
- **Adatosztályozás**: Az AI rendszerek által feldolgozott érzékeny adatok megfelelő kategorizálása és kezelése
- **Audit nyomvonalak**: Átfogó naplózás szabályozási megfelelőség és igazságügyi vizsgálat céljából
- **Adatvédelmi szabályozások**: Adatvédelmi tervezési elvek megvalósítása az AI rendszer architektúrában
- **Változáskezelés**: Formális folyamatok az AI rendszer módosításainak biztonsági áttekintésére

Ezek az alapvető gyakorlatok erős biztonsági alapot teremtenek, amely növeli az MCP-specifikus biztonsági ellenőrzések hatékonyságát és átfogó védelmet nyújtanak AI-alapú alkalmazások számára.

## Fő biztonsági tanulságok

- **Rétegezett biztonsági megközelítés**: Kombinálja az alapvető biztonsági gyakorlatokat (biztonságos kódolás, legkisebb jogosultság, ellátási lánc ellenőrzés, folyamatos monitorozás) AI-specifikus ellenőrzésekkel az átfogó védelem érdekében

- **AI-specifikus fenyegetési környezet**: Az MCP rendszerek egyedi kockázatokkal néznek szembe, beleértve a prompt injekciót, eszközmérgezést, munkamenet eltérítést, zavarodott helyettes problémákat, token átengedési sérülékenységeket és túlzott jogosultságokat, amelyek speciális enyhítéseket igényelnek

- **Hitelesítés és engedélyezés kiválósága**: Erős hitelesítést valósítson meg külső identitásszolgáltatókkal (Microsoft Entra ID), érvényesítse megfelelően a tokeneket, és soha ne fogadjon el olyan tokeneket, amelyeket nem kifejezetten az MCP szerver számára bocsátottak ki

- **AI támadások megelőzése**: Telepítse a Microsoft Prompt Shields és Azure Content Safety megoldásokat az indirekt prompt injekció és eszközmérgezés elleni védelemhez, miközben ellenőrzi az eszköz metaadatait és monitorozza a dinamikus változásokat

- **Munkamenet és átvitel biztonság**: Használjon kriptográfiailag biztonságos, nem determinisztikus, felhasználói identitáshoz kötött munkamenet-azonosítókat, valósítson meg megfelelő munkamenet életciklus-kezelést, és soha ne használjon munkameneteket hitelesítésre

- **OAuth biztonsági legjobb gyakorlatok**: Megelőzze a zavarodott helyettes támadásokat explicit felhasználói hozzájárulással dinamikusan regisztrált kliensek esetén, megfelelő OAuth 2.1 megvalósítással PKCE-vel, és szigorú átirányítási URI ellenőrzéssel  

- **Token biztonsági elvek**: Kerülje a token átengedési anti-mintákat, ellenőrizze a token célközönségi állításokat, alkalmazzon rövid élettartamú tokeneket biztonságos forgatással, és tartsa fenn a világos bizalmi határokat

- **Átfogó ellátási lánc biztonság**: Az AI ökoszisztéma összes komponensét (modellek, beágyazások, kontextus szolgáltatók, külső API-k) ugyanolyan szigorral kezelje, mint a hagyományos szoftverfüggőségeket

- **Folyamatos fejlődés**: Tartsa naprakészen az MCP specifikációkat, járuljon hozzá a biztonsági közösségi szabványokhoz, és tartson fenn adaptív biztonsági helyzetet a protokoll fejlődésével

- **Microsoft biztonsági integráció**: Használja ki a Microsoft átfogó biztonsági ökoszisztémáját (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) az MCP telepítések fokozott védelméhez

## Átfogó források

### **Hivatalos MCP biztonsági dokumentáció**
- [MCP specifikáció (aktuális: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP biztonsági legjobb gyakorlatok](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP engedélyezési specifikáció](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub tároló](https://github.com/modelcontextprotocol)

### **Biztonsági szabványok és legjobb gyakorlatok**
- [OAuth 2.0 biztonsági legjobb gyakorlatok (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 webalkalmazás biztonság](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 nagy nyelvi modellekhez](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digitális Védelem Jelentés](https://aka.ms/mddr)

### **AI biztonsági kutatás és elemzés**
- [Prompt injekció az MCP-ben (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Eszközmérgezés támadások (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Biztonsági Kutatási Tájékoztató (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Biztonsági Megoldások**
- [Microsoft Prompt Shields Dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Szolgáltatás](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Biztonság](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Kezelési Legjobb Gyakorlatok](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Megvalósítási Útmutatók & Oktatóanyagok**
- [Azure API Management mint MCP Hitelesítési Kapu](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Hitelesítés MCP Szerverekkel](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Biztonságos Token Tárolás és Titkosítás (Videó)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Ellátási Lánc Biztonság**
- [Azure DevOps Biztonság](https://azure.microsoft.com/products/devops)
- [Azure Repos Biztonság](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Ellátási Lánc Biztonsági Útja](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **További Biztonsági Dokumentáció**

Átfogó biztonsági útmutatásért tekintse meg az ebben a szakaszban található speciális dokumentumokat:

- **[MCP Biztonsági Legjobb Gyakorlatok 2025](./mcp-security-best-practices-2025.md)** - Teljes körű biztonsági legjobb gyakorlatok MCP megvalósításokhoz
- **[Azure Content Safety Megvalósítás](./azure-content-safety-implementation.md)** - Gyakorlati megvalósítási példák az Azure Content Safety integrációhoz  
- **[MCP Biztonsági Ellenőrzések 2025](./mcp-security-controls-2025.md)** - Legújabb biztonsági ellenőrzések és technikák MCP telepítésekhez
- **[MCP Legjobb Gyakorlatok Gyors Referencia](./mcp-best-practices.md)** - Gyors referencia útmutató az alapvető MCP biztonsági gyakorlatokhoz

---

## Mi következik

Következő: [3. fejezet: Kezdés](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->