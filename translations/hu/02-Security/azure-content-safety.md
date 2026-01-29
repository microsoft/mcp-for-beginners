# Fejlett MCP biztonság az Azure Content Safety segítségével

Az Azure Content Safety számos hatékony eszközt kínál, amelyek növelhetik az MCP megvalósítások biztonságát:

## Prompt Shields

A Microsoft AI Prompt Shields erős védelmet nyújtanak mind közvetlen, mind közvetett prompt injekciós támadások ellen az alábbi módokon:

1. **Fejlett felismerés**: Gépi tanulást alkalmaz a tartalomba ágyazott rosszindulatú utasítások azonosítására.
2. **Kiemelés**: Átalakítja a bemeneti szöveget, hogy az AI rendszerek könnyebben megkülönböztessék a helyes utasításokat a külső bemenetektől.
3. **Elválasztók és adatjelölés**: Megjelöli a megbízható és nem megbízható adatok közötti határokat.
4. **Content Safety integráció**: Együttműködik az Azure AI Content Safety-vel a jailbreak kísérletek és káros tartalmak felismerésére.
5. **Folyamatos frissítések**: A Microsoft rendszeresen frissíti a védelmi mechanizmusokat az új fenyegetések ellen.

## Azure Content Safety megvalósítása MCP-vel

Ez a megközelítés többrétegű védelmet biztosít:
- Bemenetek átvizsgálása feldolgozás előtt
- Kimenetek ellenőrzése visszaadás előtt
- Tiltólisták használata ismert káros minták ellen
- Az Azure folyamatosan frissülő content safety modelljeinek kihasználása

## Azure Content Safety források

Ha többet szeretnél megtudni az Azure Content Safety MCP szerverekkel való megvalósításáról, nézd meg az alábbi hivatalos forrásokat:

1. [Azure AI Content Safety Dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/) - Az Azure Content Safety hivatalos dokumentációja.
2. [Prompt Shield Dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Útmutató a prompt injekciós támadások megelőzéséhez.
3. [Content Safety API Referencia](https://learn.microsoft.com/rest/api/contentsafety/) - Részletes API referencia a Content Safety megvalósításához.
4. [Gyors kezdés: Azure Content Safety C#-val](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Gyors útmutató C# használatával.
5. [Content Safety klienskönyvtárak](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klienskönyvtárak különböző programozási nyelvekhez.
6. [Jailbreak kísérletek felismerése](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Speciális útmutató a jailbreak kísérletek észlelésére és megelőzésére.
7. [Legjobb gyakorlatok a Content Safety-hez](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Hatékony content safety megvalósítás legjobb gyakorlatai.

Részletesebb megvalósításhoz lásd a [Azure Content Safety megvalósítási útmutatót](./azure-content-safety-implementation.md).

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.