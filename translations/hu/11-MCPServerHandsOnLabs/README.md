# 🚀 MCP Server PostgreSQL-val - Teljes Tanulási Útmutató

## 🧠 Áttekintés az MCP adatbázis-integráció tanulási útjáról

Ez az átfogó tanulási útmutató megtanítja, hogyan építsünk gyártásra kész **Model Context Protocol (MCP) szervereket**, amelyek adatbázisokkal integrálódnak egy gyakorlati kiskereskedelmi analitikai megvalósításon keresztül. Megismerheted a vállalati szintű mintákat, mint például **soros szintű biztonság (RLS)**, **szemantikus keresés**, **Azure AI integráció**, és **több-bérlős adat-hozzáférés**.

Akár backend fejlesztő, AI mérnök, vagy adatarchitekt vagy, ez az útmutató strukturált tanulást kínál valós példákkal és gyakorlati feladatokkal, amelyek végigvezetnek az MCP szerveren: https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Hivatalos MCP Források

- 📘 [MCP Dokumentáció](https://modelcontextprotocol.io/) – Részletes oktatóanyagok és felhasználói útmutatók
- 📜 [MCP Specifikáció](https://modelcontextprotocol.io/docs/) – Protokoll architektúra és technikai referenciák
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – Nyílt forráskódú SDK-k, eszközök és kódminták
- 🌐 [MCP Közösség](https://github.com/orgs/modelcontextprotocol/discussions) – Csatlakozz a beszélgetésekhez és járulj hozzá a közösséghez

## 🧭 MCP Adatbázis-Integráció Tanulási Út

### 📚 Teljes Tanulási Struktúra a https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail számára

| Lab | Téma | Leírás | Link |
|--------|-------|-------------|------|
| **Lab 1-3: Alapok** | | | |
| 00 | [Bevezetés az MCP Adatbázis-Integrációba](./00-Introduction/README.md) | Áttekintés az MCP adatbázis-integrációról és a kiskereskedelmi analitikai esettanulmányról | [Kezdd itt](./00-Introduction/README.md) |
| 01 | [Alapvető Architektúra Fogalmak](./01-Architecture/README.md) | MCP szerver architektúra, adatbázis rétegek és biztonsági minták megértése | [Tanulj](./01-Architecture/README.md) |
| 02 | [Biztonság és Több-Bérlőség](./02-Security/README.md) | Soros szintű biztonság, hitelesítés és több-bérlős adat-hozzáférés | [Tanulj](./02-Security/README.md) |
| 03 | [Környezet Beállítása](./03-Setup/README.md) | Fejlesztési környezet beállítása, Docker, Azure erőforrások | [Beállítás](./03-Setup/README.md) |
| **Lab 4-6: MCP Szerver Építése** | | | |
| 04 | [Adatbázis Tervezés és Séma](./04-Database/README.md) | PostgreSQL beállítása, kiskereskedelmi séma tervezése és mintaadatok | [Építs](./04-Database/README.md) |
| 05 | [MCP Szerver Megvalósítása](./05-MCP-Server/README.md) | FastMCP szerver építése adatbázis-integrációval | [Építs](./05-MCP-Server/README.md) |
| 06 | [Eszközfejlesztés](./06-Tools/README.md) | Adatbázis-lekérdezési eszközök és séma introspekció létrehozása | [Építs](./06-Tools/README.md) |
| **Lab 7-9: Haladó Funkciók** | | | |
| 07 | [Szemantikus Keresés Integráció](./07-Semantic-Search/README.md) | Vektor beágyazások megvalósítása Azure OpenAI-val és pgvectorral | [Haladj tovább](./07-Semantic-Search/README.md) |
| 08 | [Tesztelés és Hibakeresés](./08-Testing/README.md) | Tesztelési stratégiák, hibakeresési eszközök és validációs megközelítések | [Tesztelj](./08-Testing/README.md) |
| 09 | [VS Code Integráció](./09-VS-Code/README.md) | VS Code MCP integráció és AI Chat használatának konfigurálása | [Integrálj](./09-VS-Code/README.md) |
| **Lab 10-12: Gyártás és Legjobb Gyakorlatok** | | | |
| 10 | [Telepítési Stratégiák](./10-Deployment/README.md) | Docker telepítés, Azure Container Apps és skálázási szempontok | [Telepíts](./10-Deployment/README.md) |
| 11 | [Felügyelet és Megfigyelhetőség](./11-Monitoring/README.md) | Application Insights, naplózás, teljesítményfigyelés | [Figyelj](./11-Monitoring/README.md) |
| 12 | [Legjobb Gyakorlatok és Optimalizálás](./12-Best-Practices/README.md) | Teljesítményoptimalizálás, biztonsági megerősítés és gyártási tippek | [Optimalizálj](./12-Best-Practices/README.md) |

### 💻 Amit Felépítesz

A tanulási út végére egy teljes **Zava Retail Analytics MCP Szervert** fogsz felépíteni, amely tartalmazza:

- **Több-táblás kiskereskedelmi adatbázis** ügyfélrendelésekkel, termékekkel és készlettel
- **Soros szintű biztonság** az üzlet-alapú adatizolációhoz
- **Szemantikus termékkeresés** Azure OpenAI beágyazásokkal
- **VS Code AI Chat integráció** természetes nyelvi lekérdezésekhez
- **Gyártásra kész telepítés** Dockerrel és Azure-val
- **Átfogó felügyelet** Application Insights segítségével

## 🎯 Tanulási Előfeltételek

Ahhoz, hogy a legtöbbet hozd ki ebből a tanulási útból, rendelkezned kell:

- **Programozási Tapasztalat**: Python (előnyben) vagy hasonló nyelvek ismerete
- **Adatbázis Ismeretek**: SQL és relációs adatbázisok alapvető megértése
- **API Fogalmak**: REST API-k és HTTP fogalmak ismerete
- **Fejlesztési Eszközök**: Parancssor, Git és kódszerkesztők használatának tapasztalata
- **Felhő Alapok**: (Opcionális) Azure vagy hasonló felhőplatformok alapvető ismerete
- **Docker Ismeretek**: (Opcionális) Konténerizációs fogalmak megértése

### Szükséges Eszközök

- **Docker Desktop** - PostgreSQL és MCP szerver futtatásához
- **Azure CLI** - Felhő erőforrások telepítéséhez
- **VS Code** - Fejlesztéshez és MCP integrációhoz
- **Git** - Verziókezeléshez
- **Python 3.8+** - MCP szerver fejlesztéséhez

## 📚 Tanulási Útmutató és Források

Ez a tanulási út átfogó forrásokat tartalmaz, amelyek segítenek hatékonyan navigálni:

### Tanulási Útmutató

Minden labor tartalmaz:
- **Világos tanulási célokat** - Amit elérsz
- **Lépésről-lépésre útmutatókat** - Részletes megvalósítási útmutatók
- **Kódmintákat** - Működő példák magyarázatokkal
- **Feladatokat** - Gyakorlati lehetőségek
- **Hibakeresési útmutatókat** - Gyakori problémák és megoldások
- **További forrásokat** - További olvasási és felfedezési lehetőségek

### Előfeltételek Ellenőrzése

Minden labor előtt megtalálod:
- **Szükséges ismeretek** - Amit előzetesen tudnod kell
- **Beállítás ellenőrzése** - Hogyan ellenőrizd a környezeted
- **Időbecslések** - Várható befejezési idő
- **Tanulási eredmények** - Amit a végén tudni fogsz

### Ajánlott Tanulási Útvonalak

Válassz útvonalat tapasztalati szinted alapján:

#### 🟢 **Kezdő Útvonal** (Új az MCP-ben)
1. Győződj meg róla, hogy elvégezted a [MCP Kezdőknek](https://aka.ms/mcp-for-beginners) 0-10 laborját
2. Végezd el a 00-03 laborokat az alapok megerősítéséhez
3. Kövesd a 04-06 laborokat gyakorlati építéshez
4. Próbáld ki a 07-09 laborokat gyakorlati használatra

#### 🟡 **Középhaladó Útvonal** (Némi MCP tapasztalat)
1. Tekintsd át a 00-01 laborokat az adatbázis-specifikus fogalmakért
2. Koncentrálj a 02-06 laborokra a megvalósításhoz
3. Mélyedj el a 07-12 laborokban a haladó funkciókért

#### 🔴 **Haladó Útvonal** (Tapasztalt MCP-ben)
1. Fusd át a 00-03 laborokat a kontextusért
2. Koncentrálj a 04-09 laborokra az adatbázis-integrációért
3. Összpontosíts a 10-12 laborokra a gyártási telepítésért

## 🛠️ Hogyan Használd Hatékonyan Ezt a Tanulási Utat

### Szekvenciális Tanulás (Ajánlott)

Haladj végig a laborokon sorrendben az átfogó megértés érdekében:

1. **Olvasd el az áttekintést** - Értsd meg, mit fogsz tanulni
2. **Ellenőrizd az előfeltételeket** - Győződj meg róla, hogy rendelkezel a szükséges ismeretekkel
3. **Kövesd a lépésről-lépésre útmutatókat** - Valósítsd meg, miközben tanulsz
4. **Teljesítsd a feladatokat** - Erősítsd meg a megértésed
5. **Tekintsd át a kulcsfontosságú tanulságokat** - Szilárdítsd meg a tanulási eredményeket

### Célzott Tanulás

Ha specifikus készségekre van szükséged:

- **Adatbázis-Integráció**: Koncentrálj a 04-06 laborokra
- **Biztonsági Megvalósítás**: Összpontosíts a 02, 08, 12 laborokra
- **AI/Szemantikus Keresés**: Mélyedj el a 07 laborban
- **Gyártási Telepítés**: Tanulmányozd a 10-12 laborokat

### Gyakorlati Tapasztalat

Minden labor tartalmaz:
- **Működő kódmintákat** - Másold, módosítsd és kísérletezz
- **Valós forgatókönyveket** - Gyakorlati kiskereskedelmi analitikai esettanulmányokat
- **Fokozatos komplexitást** - Egyszerűtől a haladóig építkezve
- **Validációs lépéseket** - Ellenőrizd, hogy a megvalósításod működik

## 🌟 Közösség és Támogatás

### Segítség Kérése

- **Azure AI Discord**: [Csatlakozz szakértői támogatásért](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Repo és Megvalósítási Minta**: [Telepítési Minta és Források](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Közösség**: [Csatlakozz szélesebb MCP beszélgetésekhez](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Készen Állsz a Kezdésre?

Kezdd el az utadat a **[Lab 00: Bevezetés az MCP Adatbázis-Integrációba](./00-Introduction/README.md)**

---

*Mesteri szinten építs gyártásra kész MCP szervereket adatbázis-integrációval ezen átfogó, gyakorlati tanulási élményen keresztül.*

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.