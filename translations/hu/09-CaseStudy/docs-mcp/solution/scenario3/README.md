# 3. Forgatókönyv: Szerkesztőn belüli dokumentáció MCP szerverrel VS Code-ban

## Áttekintés

Ebben a forgatókönyvben megtanulod, hogyan hozhatod be a Microsoft Learn dokumentációt közvetlenül a Visual Studio Code környezetedbe az MCP szerver segítségével. Ahelyett, hogy folyamatosan böngészőfüleket váltogatnál a dokumentáció kereséséhez, közvetlenül a szerkesztődben érheted el, keresheted és hivatkozhatsz a hivatalos anyagokra. Ez a megközelítés egyszerűsíti a munkafolyamatodat, segít fókuszált maradni, és zökkenőmentes integrációt tesz lehetővé olyan eszközökkel, mint a GitHub Copilot.

- Keresd és olvasd a dokumentációt VS Code-on belül, anélkül, hogy elhagynád a kódolási környezetet.
- Hivatkozz dokumentációra, és illessz be linkeket közvetlenül a README vagy tananyag fájljaidba.
- Használd együtt a GitHub Copilotot és az MCP-t egy gördülékeny, mesterséges intelligencia által támogatott dokumentációs munkafolyamathoz.

## Tanulási célok

A fejezet végére megérted, hogyan állítsd be és használd az MCP szervert a VS Code-ban a dokumentációs és fejlesztési munkafolyamatod javítására. Képes leszel:

- Beállítani a munkakörnyezetedet az MCP szerver használatára dokumentáció kereséséhez.
- Keresni és beszúrni dokumentációt közvetlenül a VS Code-ból.
- Ötvözni a GitHub Copilot és az MCP erejét egy hatékonyabb, mesterséges intelligenciával támogatott munkafolyamathoz.

Ezek a képességek segítenek fókuszált maradni, javítani a dokumentáció minőségét, és növelni a termelékenységedet fejlesztőként vagy technikai íróként.

## Megoldás

A szerkesztőn belüli dokumentáció eléréséhez egy lépésről lépésre követhető folyamatot fogsz követni, amely integrálja az MCP szervert a VS Code-dal és a GitHub Copilottal. Ez a megoldás ideális tananyagírók, dokumentációs szakemberek és fejlesztők számára, akik szeretnék megtartani a fókuszt a szerkesztőben, miközben dolgoznak a dokumentációval és a Copilottal.

- Gyorsan adj hozzá hivatkozásokat egy README-hez tananyag vagy projekt dokumentáció írása közben.
- Használd a Copilotot kód generálására, és az MCP-t a releváns dokumentáció azonnali megtalálására és idézésére.
- Maradj fókuszált a szerkesztődben, és növeld a termelékenységedet.

### Lépésről lépésre útmutató

A kezdéshez kövesd az alábbi lépéseket. Minden lépéshez hozzáadhatsz egy képernyőképet az assets mappából, hogy vizuálisan is illusztráld a folyamatot.

1. **Add hozzá az MCP konfigurációt:**
   A projekt gyökérkönyvtárában hozz létre egy `.vscode/mcp.json` fájlt, és illeszd be a következő konfigurációt:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Ez a konfiguráció megmondja a VS Code-nak, hogyan csatlakozzon a [`Microsoft Learn Docs MCP szerverhez`](https://github.com/MicrosoftDocs/mcp).
   
   ![1. lépés: mcp.json hozzáadása a .vscode mappához](../../../../../../translated_images/hu/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.png)
    
2. **Nyisd meg a GitHub Copilot Chat panelt:**
   Ha még nincs telepítve a GitHub Copilot bővítményed, menj a VS Code Extensions nézetébe, és telepítsd. Közvetlenül letöltheted a [Visual Studio Code Marketplace-ről](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Ezután nyisd meg a Copilot Chat panelt az oldalsávból.

   ![2. lépés: Copilot Chat panel megnyitása](../../../../../../translated_images/hu/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.png)

3. **Kapcsold be az agent módot és ellenőrizd az eszközöket:**
   A Copilot Chat panelen kapcsold be az agent módot.

   ![3. lépés: Agent mód bekapcsolása és eszközök ellenőrzése](../../../../../../translated_images/hu/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.png)

   Az agent mód bekapcsolása után ellenőrizd, hogy az MCP szerver szerepel-e az elérhető eszközök között. Ez biztosítja, hogy a Copilot agent hozzáférjen a dokumentációs szerverhez a releváns információk lekéréséhez.
   
   ![3. lépés: MCP szerver eszköz ellenőrzése](../../../../../../translated_images/hu/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.png)

4. **Indíts új chatet és kérdezd az agentet:**
   Nyiss egy új chatet a Copilot Chat panelen. Most már kérdezheted az agentet a dokumentációs kérdéseiddel. Az agent az MCP szervert használja, hogy közvetlenül a szerkesztődben megjelenítse a releváns Microsoft Learn dokumentációt.

   - *„Tanulmányi tervet szeretnék írni az X témához. 8 héten át fogom tanulni, minden hétre javasolj tartalmat.”*

   ![4. lépés: Kérdezd az agentet a chatben](../../../../../../translated_images/hu/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.png)

5. **Élő lekérdezés:**

   > Vegyünk egy élő lekérdezést az Azure AI Foundry Discord [#get-help](https://discord.gg/D6cRhjHWSC) szekcióból ([eredeti üzenet megtekintése](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *„Válaszokat keresek arra, hogyan lehet többagentű megoldást telepíteni az Azure AI Foundry-n fejlesztett AI agentekkel. Látom, hogy nincs közvetlen telepítési mód, mint például a Copilot Studio csatornák. Milyen különböző módjai vannak ennek a telepítésnek, hogy vállalati felhasználók tudjanak együttműködni és elvégezni a feladatot?
Számos cikk/blog állítja, hogy az Azure Bot szolgáltatás használható erre a célra, amely hidat képezhet az MS Teams és az Azure AI Foundry agentek között. Vajon működik-e, ha beállítok egy Azure botot, amely az Azure AI Foundry Orchestrator Agentjéhez kapcsolódik Azure functionön keresztül az orchestration végrehajtásához, vagy minden AI agenthez külön Azure functiont kell létrehoznom a Bot framework orchestrationhöz? Egyéb javaslatokat is szívesen fogadok.”*

   ![5. lépés: Élő lekérdezések](../../../../../../translated_images/hu/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.png)

   Az agent releváns dokumentációs linkekkel és összefoglalókkal válaszol, amelyeket közvetlenül beilleszthetsz markdown fájljaidba vagy hivatkozásként használhatsz a kódodban.

### Minta lekérdezések

Íme néhány példa lekérdezés, amelyeket kipróbálhatsz. Ezek megmutatják, hogyan működhet együtt az MCP szerver és a Copilot, hogy azonnali, kontextusérzékeny dokumentációt és hivatkozásokat biztosítsanak anélkül, hogy elhagynád a VS Code-ot:

- „Mutasd meg, hogyan használhatók az Azure Functions trigger-ek.”
- „Illessz be egy linket az Azure Key Vault hivatalos dokumentációjához.”
- „Mik az Azure erőforrások biztonságos kezelésének legjobb gyakorlatai?”
- „Keress egy gyors kezdő útmutatót az Azure AI szolgáltatásokhoz.”

Ezek a lekérdezések bemutatják, hogyan tud együttműködni az MCP szerver és a Copilot, hogy azonnali, kontextusérzékeny dokumentációt és hivatkozásokat nyújtsanak anélkül, hogy elhagynád a VS Code-ot.

---

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.