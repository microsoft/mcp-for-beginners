# Fejlett témák az MCP-ben

[![Fejlett MCP: Biztonságos, skálázható és multimodális MI ügynökök](../../../translated_images/hu/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

Ez a fejezet a Model Context Protocol (MCP) implementációjának számos fejlett témáját tárgyalja, beleértve a multimodális integrációt, a skálázhatóságot, a biztonsági legjobb gyakorlatokat és a vállalati integrációt. Ezek a témák létfontosságúak robusztus és éles rendszerekhez alkalmas MCP alkalmazások építéséhez, amelyek képesek megfelelni a modern MI rendszerek elvárásainak.

## Áttekintés

Ez a lecke az MCP megvalósításának fejlett fogalmait tárgyalja, hangsúlyt fektetve a multimodális integrációra, a skálázhatóságra, a biztonsági legjobb gyakorlatokra és a vállalati integrációra. Ezek a témák nélkülözhetetlenek éles, termelési környezetben alkalmazható MCP alkalmazások fejlesztéséhez, amelyek képesek kezelni a komplex követelményeket vállalati környezetben.

## Tanulási célok

A lecke végére képes lesz:

- Megvalósítani multimodális képességeket MCP keretrendszerekben
- Tervezni skálázható MCP architektúrákat magas igényű helyzetekhez
- Alkalmazni az MCP biztonsági elveivel összhangban álló biztonsági legjobb gyakorlatokat
- Integrálni az MCP-t vállalati MI rendszerekkel és keretrendszerekkel
- Optimalizálni a teljesítményt és megbízhatóságot éles környezetben

## Leckék és mintaprojektek

| Link | Cím | Leírás |
|------|-------|-------------|
| [5.1 Integráció Azure-rel](./mcp-integration/README.md) | Integráció Azure-rel | Tanulja meg, hogyan integrálhatja MCP szerverét Azure felületen |
| [5.2 Multimodális minta](./mcp-multi-modality/README.md) | MCP multimodális minták | Minták hang, kép és multimodális válaszokhoz |
| [5.3 MCP OAuth2 minta](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimális Spring Boot alkalmazás, amely bemutatja az OAuth2 használatát MCP-vel, mint jogosítási és erőforrás szerver. Biztonságos tokenkiadást, védett végpontokat, Azure Container Apps telepítést és API Management integrációt szemléltet. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Gyökérkörnyezetek | További tudnivalók a gyökérkörnyezetről és annak megvalósításáról |
| [5.5 Útválasztás](./mcp-routing/README.md) | Útválasztás | Ismerje meg az útválasztás különböző típusait |
| [5.6 Mintavétel](./mcp-sampling/README.md) | Mintavétel | Tanulja meg, hogyan kell dolgozni mintavétellel |
| [5.7 Skálázás](./mcp-scaling/README.md) | Skálázás | Ismerje meg a skálázást |
| [5.8 Biztonság](./mcp-security/README.md) | Biztonság | Biztosítsa MCP szerverét |
| [5.9 Webes keresés minta](./web-search-mcp/README.md) | Web Search MCP | Python MCP szerver és kliens, amely integrálja a SerpAPI-t valós idejű webes, hírek, termékkereséshez és kérdés-válasz funkcióhoz. Több eszköz összehangolását, külső API integrációt és robusztus hibakezelést mutat be. |
| [5.10 Valós idejű adatfolyam](./mcp-realtimestreaming/README.md) | Streaming | A valós idejű adatfolyam alapvetővé vált a mai adatközpontú világban, ahol a vállalkozásoknak és alkalmazásoknak azonnali hozzáférésre van szükségük az információkhoz a gyors döntéshozatal érdekében. |
| [5.11 Valós idejű webes keresés](./mcp-realtimesearch/README.md) | Web Search | Hogyan alakítja át az MCP a valós idejű webes keresést egy szabványosított kontextuskezelési megközelítéssel MI modellek, keresőmotorok és alkalmazások között. |
| [5.12 Entra ID hitelesítés MCP szerverekhez](./mcp-security-entra/README.md) | Entra ID hitelesítés | A Microsoft Entra ID egy robusztus, felhőalapú azonosítási és hozzáférés-kezelési megoldás, amely biztosítja, hogy csak jogosult felhasználók és alkalmazások férhessenek hozzá az MCP szerveréhez. |
| [5.13 Azure AI Foundry ügynök integráció](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integráció | Tanulja meg, hogyan integrálhatja az MCP szervereket Azure AI Foundry ügynökökkel, lehetővé téve erőteljes eszközösszehangolást és vállalati MI képességeket szabványosított külső adatforrás csatlakozásokkal. |
| [5.14 Kontextus mérnöki tudomány](./mcp-contextengineering/README.md) | Kontextus mérnökség | A jövő lehetőségei a kontextus mérnöki technikák alkalmazásában MCP szervereknél, beleértve a kontextus optimalizálást, dinamikus kontextuskezelést és hatékony prompt tervezési stratégiákat MCP keretrendszerekben. |
| [5.15 Egyedi átvitel MCP-hez](./mcp-transport/README.md) | Egyedi átvitel | Tanulja meg, hogyan valósíthat meg egyedi átvitelmechanizmusokat speciális MCP kommunikációs esetekben. |
| [5.16 Protokoll jellemzők mélyreható bemutatása](./mcp-protocol-features/README.md) | Protokoll jellemzők | Sajátítsa el a fejlett protokoll funkciókat, mint előrehaladási értesítések, kérés törlése, erőforrás sablonok és hibakezelési minták. |
| [5.17 Adverzári többügynökös érvelés](./mcp-adversarial-agents/README.md) | Adverzári ügynökök | Két egymással szemben álló állásponttal rendelkező ügynök egyetlen MCP eszközkészlet megosztásával, hogy kiszűrjék a hallucinációkat, felüljáró eseteket tárjanak fel, és jobb kalibrált kimeneteket hozzanak létre strukturált vita révén. |

> **Újdonság az MCP specifikációban 2025-11-25:** A specifikáció most kísérleti támogatást tartalmaz a **Feladatok** (hosszú lefutású műveletek előrehaladás követéssel), **Eszköz annotációk** (metadata az eszköz viselkedéséről a biztonság érdekében), **URL mód előhívás** (kliens által megadott konkrét URL tartalom kérése), és továbbfejlesztett **Gyökerek** (munkaterület kontextuskezeléshez). Részletekért lásd a [MCP specifikáció változásnaplóját](https://spec.modelcontextprotocol.io/).

## További hivatkozások

A legfrissebb információkért fejlett MCP témákban hivatkozzon a következőkre:
- [MCP dokumentáció](https://modelcontextprotocol.io/)
- [MCP specifikáció (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub tárház](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Biztonsági kockázatok és enyhítések
- [MCP Biztonsági Csúcsmunka (Sherpa)](https://azure-samples.github.io/sherpa/) - Gyakorlati biztonsági képzés

## Legfontosabb tanulságok

- A multimodális MCP megoldások túlmutatnak a puszta szövegfeldolgozáson, és kibővítik az MI képességeit
- A skálázhatóság elengedhetetlen vállalati telepítésekhez, amely vízszintes és függőleges skálázással kezelhető
- Átfogó biztonsági intézkedések védik az adatokat és biztosítják a megfelelő hozzáférés-ellenőrzést
- A vállalati integráció olyan platformokkal, mint az Azure OpenAI és Microsoft AI Foundry, növeli az MCP képességeit
- A fejlett MCP megvalósítások profitálnak az optimalizált architektúrákból és a gondos erőforrás-kezelésből

## Gyakorlat

Tervezzen vállalati szintű MCP megvalósítást egy adott felhasználási esethez:

1. Azonosítsa a multimodális követelményeket az adott esethez
2. Vázolja fel a szükséges biztonsági kontrollokat az érzékeny adatok védelmére
3. Tervezzen skálázható architektúrát a változó terhelés kezeléséhez
4. Tervezze meg az integrációs pontokat vállalati MI rendszerekkel
5. Dokumentálja a potenciális teljesítménybottleneckeket és enyhítési stratégiákat

## További források

- [Azure OpenAI dokumentáció](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry dokumentáció](https://learn.microsoft.com/en-us/ai-services/)

---

## Mi következik

Fedezze fel a modul leckéit az alábbi kezdő leckével: [5.1 MCP integráció](./mcp-integration/README.md)

Miután befejezte ezt a modult, folytassa a következővel: [6. modul: Közösségi hozzájárulások](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértések vagy félreértelmezések miatt.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->