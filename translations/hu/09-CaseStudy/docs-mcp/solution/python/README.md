# Tanulási terv generátor Chainlit és Microsoft Learn Docs MCP segítségével

## Előfeltételek

- Python 3.8 vagy újabb
- pip (Python csomagkezelő)
- Internetkapcsolat a Microsoft Learn Docs MCP szerverhez való csatlakozáshoz

## Telepítés

1. Klónozd ezt a repót vagy töltsd le a projekt fájlokat.
2. Telepítsd a szükséges függőségeket:

   ```bash
   pip install -r requirements.txt
   ```

## Használat

### 1. Forgatókönyv: Egyszerű lekérdezés a Docs MCP-hez
Egy parancssoros kliens, amely csatlakozik a Docs MCP szerverhez, elküldi a lekérdezést, és megjeleníti az eredményt.

1. Futtasd a szkriptet:
   ```bash
   python scenario1.py
   ```
2. Írd be a dokumentációval kapcsolatos kérdésedet a promptba.

### 2. Forgatókönyv: Tanulási terv generátor (Chainlit webalkalmazás)
Egy webes felület (Chainlit segítségével), amely lehetővé teszi a felhasználók számára, hogy személyre szabott, heti bontású tanulási tervet készítsenek bármely technikai témához.

1. Indítsd el a Chainlit alkalmazást:
   ```bash
   chainlit run scenario2.py
   ```
2. Nyisd meg a terminálban megadott helyi URL-t (pl. http://localhost:8000) a böngésződben.
3. A chat ablakban írd be a tanulási témát és a tanulás időtartamát (pl. "AI-900 vizsga, 8 hét").
4. Az alkalmazás válaszol egy heti bontású tanulási tervvel, amely tartalmazza a releváns Microsoft Learn dokumentáció linkjeit.

**Szükséges környezeti változók:**

A 2. forgatókönyv (Chainlit webalkalmazás Azure OpenAI-val) használatához a következő környezeti változókat kell beállítanod egy `.env` fájlban a `python` könyvtárban:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Töltsd ki ezeket az értékeket az Azure OpenAI erőforrás részleteivel, mielőtt futtatnád az alkalmazást.

> [!TIP]
> Könnyen telepítheted saját modelljeidet az [Azure AI Foundry](https://ai.azure.com/) segítségével.

### 3. Forgatókönyv: Dokumentáció a szerkesztőben MCP szerverrel VS Code-ban

Ahelyett, hogy böngészőfülek között váltanál a dokumentáció kereséséhez, közvetlenül a Microsoft Learn Docs-t hozhatod be a VS Code-ba az MCP szerver segítségével. Ez lehetővé teszi, hogy:
- Dokumentációt keress és olvass közvetlenül a VS Code-ban anélkül, hogy elhagynád a kódolási környezetet.
- Dokumentációs hivatkozásokat adj hozzá, és linkeket illessz be közvetlenül a README vagy kurzus fájlokba.
- GitHub Copilotot és MCP-t együtt használj egy zökkenőmentes, AI-alapú dokumentációs munkafolyamathoz.

**Példa felhasználási esetek:**
- Gyorsan adj hozzá hivatkozásokat egy README-hez, miközben kurzus- vagy projekt-dokumentációt írsz.
- Használd a Copilotot kód generálására, és az MCP-t releváns dokumentáció keresésére és idézésére.
- Maradj fókuszált a szerkesztőben, és növeld a produktivitást.

> [!IMPORTANT]
> Győződj meg róla, hogy érvényes [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) konfigurációval rendelkezel a munkaterületedben (helye: `.vscode/mcp.json`).

## Miért Chainlit a 2. forgatókönyvhöz?

A Chainlit egy modern, nyílt forráskódú keretrendszer beszélgetés-alapú webalkalmazások építéséhez. Egyszerűvé teszi chat-alapú felhasználói felületek létrehozását, amelyek backend szolgáltatásokhoz, például a Microsoft Learn Docs MCP szerverhez csatlakoznak. Ez a projekt a Chainlit segítségével egy egyszerű, interaktív módot kínál személyre szabott tanulási tervek valós idejű generálására. A Chainlit használatával gyorsan építhetsz és telepíthetsz chat-alapú eszközöket, amelyek növelik a produktivitást és a tanulást.

## Mit csinál ez az alkalmazás?

Ez az alkalmazás lehetővé teszi a felhasználók számára, hogy személyre szabott tanulási tervet készítsenek egyszerűen egy téma és egy időtartam megadásával. Az alkalmazás elemzi a bevitt adatokat, lekérdezéseket küld a Microsoft Learn Docs MCP szervernek releváns tartalomért, és az eredményeket strukturált, heti bontású tervvé szervezi. Minden hét ajánlásai megjelennek a chatben, így könnyen követheted és nyomon követheted a haladásodat. Az integráció biztosítja, hogy mindig a legfrissebb, legrelevánsabb tanulási forrásokat kapd.

## Példa lekérdezések

Próbáld ki ezeket a lekérdezéseket a chat ablakban, hogy lásd, hogyan reagál az alkalmazás:

- `AI-900 vizsga, 8 hét`
- `Azure Functions tanulása, 4 hét`
- `Azure DevOps, 6 hét`
- `Adatmérnökség az Azure-on, 10 hét`
- `Microsoft biztonsági alapok, 5 hét`
- `Power Platform, 7 hét`
- `Azure AI szolgáltatások, 12 hét`
- `Felhőarchitektúra, 9 hét`

Ezek a példák bemutatják az alkalmazás rugalmasságát különböző tanulási célok és időkeretek esetén.

## Hivatkozások

- [Chainlit dokumentáció](https://docs.chainlit.io/)
- [MCP dokumentáció](https://github.com/MicrosoftDocs/mcp)

---

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.