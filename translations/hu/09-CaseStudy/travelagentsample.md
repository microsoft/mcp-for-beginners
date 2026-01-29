# Esettanulmány: Azure AI Utazási Ügynökök – Referencia Implementáció

## Áttekintés

Az [Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) egy átfogó referencia megoldás, amelyet a Microsoft fejlesztett ki, és bemutatja, hogyan lehet több ügynökből álló, mesterséges intelligenciával támogatott utazástervező alkalmazást építeni a Model Context Protocol (MCP), az Azure OpenAI és az Azure AI Search használatával. Ez a projekt a legjobb gyakorlatokat szemlélteti a több AI ügynök összehangolására, vállalati adatok integrálására, valamint egy biztonságos és bővíthető platform biztosítására valós életbeli helyzetekhez.

## Főbb jellemzők
- **Több ügynök összehangolása:** Az MCP segítségével koordinálja a specializált ügynököket (pl. repülőjárat, szállás, útiterv ügynökök), amelyek együttműködve teljesítik a komplex utazástervezési feladatokat.
- **Vállalati adatok integrálása:** Csatlakozik az Azure AI Search-hoz és más vállalati adatforrásokhoz, hogy naprakész, releváns információkat nyújtson az utazási ajánlásokhoz.
- **Biztonságos, skálázható architektúra:** Az Azure szolgáltatásait használja hitelesítéshez, jogosultságkezeléshez és skálázható telepítéshez, követve a vállalati biztonsági legjobb gyakorlatokat.
- **Bővíthető eszköztár:** Újrahasznosítható MCP eszközöket és prompt sablonokat valósít meg, amelyek gyors alkalmazkodást tesznek lehetővé új területekhez vagy üzleti igényekhez.
- **Felhasználói élmény:** Beszélgetés-alapú felületet biztosít a felhasználók számára az utazási ügynökökkel való interakcióhoz, amelyet az Azure OpenAI és az MCP hajt.

## Architektúra
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Az architektúra diagram leírása

Az Azure AI Travel Agents megoldás moduláris, skálázható és biztonságos integrációra lett tervezve több AI ügynök és vállalati adatforrás között. A fő komponensek és az adatáramlás a következő:

- **Felhasználói felület:** A felhasználók egy beszélgetés-alapú UI-n (például webes chat vagy Teams bot) keresztül lépnek kapcsolatba a rendszerrel, ahol kérdéseket tesznek fel és utazási ajánlásokat kapnak.
- **MCP Server:** Központi koordinátorként működik, fogadja a felhasználói bemenetet, kezeli a kontextust, és összehangolja a specializált ügynökök (pl. FlightAgent, HotelAgent, ItineraryAgent) tevékenységét a Model Context Protocol segítségével.
- **AI ügynökök:** Minden ügynök egy adott területért felel (repülőjáratok, szállások, útiterv), és MCP eszközként van megvalósítva. Az ügynökök prompt sablonokat és logikát használnak a kérések feldolgozására és válaszok generálására.
- **Azure OpenAI Service:** Fejlett természetes nyelvi megértést és generálást biztosít, lehetővé téve az ügynökök számára a felhasználói szándék értelmezését és beszélgetés-alapú válaszok létrehozását.
- **Azure AI Search és vállalati adatok:** Az ügynökök lekérdezik az Azure AI Search-t és más vállalati adatforrásokat, hogy naprakész információkat szerezzenek a repülőjáratokról, szállásokról és utazási lehetőségekről.
- **Hitelesítés és biztonság:** Integrálódik a Microsoft Entra ID-vel a biztonságos hitelesítés érdekében, és a legkisebb jogosultság elvét alkalmazza az összes erőforrásra.
- **Telepítés:** Azure Container Apps-re tervezték a telepítést, biztosítva a skálázhatóságot, a monitorozást és az üzemeltetési hatékonyságot.

Ez az architektúra lehetővé teszi a több AI ügynök zökkenőmentes összehangolását, a vállalati adatok biztonságos integrációját, valamint egy robusztus, bővíthető platformot domain-specifikus AI megoldások építéséhez.

## Az architektúra diagram lépésről lépésre történő magyarázata
Képzeld el, hogy egy nagy utazást tervezel, és egy szakértő asszisztensekből álló csapat segít neked minden részletben. Az Azure AI Travel Agents rendszer hasonlóan működik, különböző részekből (mint a csapattagok) áll, amelyek mindegyike különleges feladatot lát el. Így illeszkedik össze az egész:

### Felhasználói felület (UI):
Gondolj erre úgy, mint az utazási ügynököd recepciójára. Itt teszed fel a kérdéseidet vagy adod meg a kéréseidet, például: „Találj nekem egy repülőjáratot Párizsba.” Ez lehet egy weboldalon lévő chat ablak vagy egy üzenetküldő alkalmazás.

### MCP Server (A koordinátor):
Az MCP Server olyan, mint a menedzser, aki a recepcióban meghallgatja a kérésedet, és eldönti, melyik szakértőnek kell foglalkoznia vele. Nyomon követi a beszélgetést, és gondoskodik arról, hogy minden zökkenőmentesen működjön.

### AI ügynökök (Szakértő asszisztensek):
Minden ügynök egy adott terület szakértője – az egyik mindent tud a repülőjáratokról, a másik a szállásokról, a harmadik az útiterv tervezéséről. Amikor utazást kérsz, az MCP Server elküldi a kérésedet a megfelelő ügynök(ök)nek. Ezek az ügynökök a tudásukat és eszközeiket használva keresik meg a legjobb lehetőségeket.

### Azure OpenAI Service (Nyelvi szakértő):
Ez olyan, mintha lenne egy nyelvi szakértőd, aki pontosan érti, mit kérsz, bármilyen formában is fogalmazod meg. Segít az ügynököknek megérteni a kéréseidet és természetes, beszélgetéshez hasonló válaszokat adni.

### Azure AI Search és vállalati adatok (Információs könyvtár):
Képzelj el egy hatalmas, naprakész könyvtárat, amelyben minden legfrissebb utazási információ megtalálható – repülőjárat menetrendek, szállás elérhetőség és még sok más. Az ügynökök ebben a könyvtárban keresik meg a legpontosabb válaszokat.

### Hitelesítés és biztonság (Biztonsági őr):
Ahogy egy biztonsági őr ellenőrzi, ki léphet be bizonyos területekre, ez a rész gondoskodik arról, hogy csak az arra jogosult személyek és ügynökök férhessenek hozzá érzékeny adatokhoz. Biztosítja az adataid védelmét és titkosságát.

### Telepítés Azure Container Apps-en (Az épület):
Minden asszisztens és eszköz együtt dolgozik egy biztonságos, skálázható épületben (a felhőben). Ez azt jelenti, hogy a rendszer egyszerre sok felhasználót képes kiszolgálni, és mindig elérhető, amikor szükséged van rá.

## Hogyan működik mindez együtt:

Először a recepcióban (UI) teszel fel egy kérdést.
A menedzser (MCP Server) eldönti, melyik szakértő (ügynök) segít neked.
A szakértő a nyelvi szakértőt (OpenAI) használja a kérésed megértéséhez, és a könyvtárat (AI Search) a legjobb válasz megtalálásához.
A biztonsági őr (Hitelesítés) gondoskodik arról, hogy minden biztonságos legyen.
Mindez egy megbízható, skálázható épületben (Azure Container Apps) történik, így az élmény gördülékeny és biztonságos.
Ez a csapatmunka lehetővé teszi, hogy a rendszer gyorsan és biztonságosan segítsen megtervezni az utazásodat, akár egy modern irodában dolgozó szakértő utazási ügynökök csapata!

## Műszaki megvalósítás
- **MCP Server:** A fő összehangoló logikát futtatja, elérhetővé teszi az ügynökök eszközeit, és kezeli a kontextust a többlépéses utazástervezési munkafolyamatokhoz.
- **Ügynökök:** Minden ügynök (pl. FlightAgent, HotelAgent) MCP eszközként van megvalósítva, saját prompt sablonokkal és logikával.
- **Azure integráció:** Az Azure OpenAI-t használja a természetes nyelvi megértéshez, és az Azure AI Search-t az adatok lekéréséhez.
- **Biztonság:** Integrálódik a Microsoft Entra ID-vel a hitelesítéshez, és a legkisebb jogosultság elvét alkalmazza az összes erőforrásra.
- **Telepítés:** Támogatja az Azure Container Apps-re történő telepítést a skálázhatóság és az üzemeltetési hatékonyság érdekében.

## Eredmények és hatás
- Bemutatja, hogyan használható az MCP több AI ügynök összehangolására valós, éles környezetben.
- Gyorsítja a megoldásfejlesztést újrahasznosítható minták biztosításával az ügynökök koordinációjához, adatintegrációhoz és biztonságos telepítéshez.
- Mintaként szolgál domain-specifikus, AI-alapú alkalmazások építéséhez MCP és Azure szolgáltatások használatával.

## Hivatkozások
- [Azure AI Travel Agents GitHub tárhely](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.