# 🚀 MCP szerver PostgreSQL-lel – Teljes tanulási útmutató

## 🧠 Áttekintés az MCP adatbázis-integráció tanulási útról

Ez az átfogó tanulási útmutató megtanítja, hogyan építs előállításra kész **Model Context Protocol (MCP) szervereket**, amelyek adatbázisokkal integrálódnak egy gyakorlati kiskereskedelmi elemzési megvalósításon keresztül. Megismerheted a vállalati szintű mintákat, többek között a **Soros szintű biztonságot (RLS)**, a **szemantikus keresést**, az **Azure AI integrációt** és a **többbérlős adat-hozzáférést**.

Legyél akár backend fejlesztő, AI mérnök vagy adatarchitekt, ez az útmutató strukturált tanulást nyújt valós példákkal és gyakorlati feladatokkal, amely végigvezet a következő MCP szerver https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail használatán.

## 🔗 Hivatalos MCP források

- 📘 [MCP dokumentáció](https://modelcontextprotocol.io/) – Részletes oktatóanyagok és felhasználói útmutatók
- 📜 [MCP specifikáció (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protokoll architektúra és műszaki hivatkozások
- 🧑‍💻 [MCP GitHub tárhely](https://github.com/modelcontextprotocol) – Nyílt forráskódú SDK-k, eszközök és kódminták
- 🌐 [MCP közösség](https://github.com/orgs/modelcontextprotocol/discussions) – Vegyél részt a beszélgetésekben és járulj hozzá a közösséghez
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Biztonsági bevált gyakorlatok és kockázatcsökkentés


## 🧭 MCP adatbázis-integráció tanulási útvonal

### 📚 Teljes tanulási struktúra a https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail projekthez

| Labor | Téma | Leírás | Link |
|--------|-------|-------------|------|
| **1-3. labor: Alapok** | | | |
| 00 | [Bevezetés az MCP adatbázis-integrációba](./00-Introduction/README.md) | Áttekintés az MCP-ről adatbázis-integrációval és kiskereskedelmi elemzési esettel | [Itt kezd](./00-Introduction/README.md) |
| 01 | [Alap architektúra fogalmak](./01-Architecture/README.md) | MCP szerver architektúra, adatbázis rétegek és biztonsági minták megértése | [Tanulás](./01-Architecture/README.md) |
| 02 | [Biztonság és többbérlőség](./02-Security/README.md) | Soros szintű biztonság, hitelesítés és többbérlős adat-hozzáférés | [Tanulás](./02-Security/README.md) |
| 03 | [Környezet beállítása](./03-Setup/README.md) | Fejlesztői környezet, Docker, Azure erőforrások beállítása | [Beállítás](./03-Setup/README.md) |
| **4-6. labor: MCP szerver építése** | | | |
| 04 | [Adatbázis tervezés és séma](./04-Database/README.md) | PostgreSQL beállítás, kiskereskedelmi séma tervezés és mintaadatok | [Építés](./04-Database/README.md) |
| 05 | [MCP szerver megvalósítása](./05-MCP-Server/README.md) | FastMCP szerver építése adatbázis-integrációval | [Építés](./05-MCP-Server/README.md) |
| 06 | [Eszközfejlesztés](./06-Tools/README.md) | Adatbázis lekérdező eszközök és séma introspekció készítése | [Építés](./06-Tools/README.md) |
| **7-9. labor: Haladó funkciók** | | | |
| 07 | [Szemantikus keresés integráció](./07-Semantic-Search/README.md) | Vektorbeágyazások megvalósítása Azure OpenAI-val és pgvectorral | [Haladás](./07-Semantic-Search/README.md) |
| 08 | [Tesztelés és hibakeresés](./08-Testing/README.md) | Tesztelési stratégiák, hibakereső eszközök és validációs megközelítések | [Tesztelés](./08-Testing/README.md) |
| 09 | [VS Code integráció](./09-VS-Code/README.md) | VS Code MCP integráció és AI Chat használat konfigurálása | [Integráció](./09-VS-Code/README.md) |
| **10-12. labor: Üzembe helyezés és bevált gyakorlatok** | | | |
| 10 | [Telepítési stratégiák](./10-Deployment/README.md) | Docker telepítés, Azure Container Apps és skálázási megfontolások | [Telepítés](./10-Deployment/README.md) |
| 11 | [Monitoring és megfigyelés](./11-Monitoring/README.md) | Application Insights, naplózás, teljesítmény monitorozás | [Monitoring](./11-Monitoring/README.md) |
| 12 | [Bevált gyakorlatok és optimalizálás](./12-Best-Practices/README.md) | Teljesítmény-optimalizálás, biztonsági megerősítés és üzemeltetési tippek | [Optimalizálás](./12-Best-Practices/README.md) |

### 💻 Amit építeni fogsz

A tanulási út végére elkészíted a teljes **Zava Kiskereskedelmi Elemző MCP Szervert**, amely tartalmazza:

- **Többtáblás kiskereskedelmi adatbázis** ügyfélrendelésekkel, termékekkel és készlettel
- **Soros szintű biztonság** üzlet-alapú adatizolációhoz
- **Szemantikus termékkutatás** Azure OpenAI beágyazásokkal
- **VS Code AI Chat integráció** természetes nyelvű lekérdezésekhez
- **Üzemeltetésre kész telepítés** Dockeren és Azure-on keresztül
- **Átfogó monitoring** az Application Insights segítségével

## 🎯 Tanulási előfeltételek

A legtöbbet hozhatod ki ebből az útból, ha rendelkezel:

- **Programozási tapasztalat**: Előny a Python ismerete, vagy hasonló nyelvek
- **Adatbázis ismeretek**: SQL és relációs adatbázisok alapvető megértése
- **API fogalmak**: REST API-k és HTTP alapelvek ismerete
- **Fejlesztői eszközök**: Parancssor, Git és kódszerkesztők tapasztalat
- **Felhőalapok**: (Opcionális) Azure vagy hasonló felhőplatformok alapismerete
- **Docker ismeretek**: (Opcionális) Konténerizációs fogalmak ismerete

### Szükséges eszközök

- **Docker Desktop** - PostgreSQL és MCP szerver futtatásához
- **Azure CLI** - Felhő erőforrások telepítéséhez
- **VS Code** - Fejlesztéshez és MCP integrációhoz
- **Git** - Verziókezeléshez
- **Python 3.8+** - MCP szerver fejlesztéshez

## 📚 Tanulási útmutató és források

Ez a tanulási út átfogó forrásokat tartalmaz, amelyek segítenek hatékonyan navigálni:

### Tanulási útmutató

Minden labor tartalmaz:
- **Világos tanulási célokat** – Mit fogsz elérni
- **Lépésről lépésre útmutatókat** – Részletes megvalósítási útmutatókat
- **Kódpéldákat** – Működő példákat magyarázatokkal
- **Gyakorlatokat** – Kézzelfogható gyakorlási lehetőségeket
- **Hibakeresési útmutatókat** – Gyakori problémák és megoldások
- **További forrásokat** – További olvasmányok és kutatások

### Előfeltételek ellenőrzése

Minden labor indulása előtt:
- **Szükséges tudás** – Mit kell előzetesen tudnod
- **Beállítás ellenőrzése** – Hogyan validáld a környezetedet
- **Időbecslések** – A várható befejezési idő
- **Tanulási eredmények** – Mit fogsz tudni a végére

### Ajánlott tanulási útvonalak

Válaszd az utat tapasztalati szinted szerint:

#### 🟢 **Kezdő útvonal** (Új az MCP-ben)
1. Győződj meg róla, hogy elvégezted a 0-10. pontokat az [MCP kezdőknek](https://aka.ms/mcp-for-beginners) tananyagból
2. Teljesítsd a 00-03 laborokat az alapok megerősítéséhez
3. Kövesd a 04-06 laborokat gyakorlati építéshez
4. Próbáld ki a 07-09 laborokat a gyakorlati használathoz

#### 🟡 **Középhaladó útvonal** (Némi MCP tapasztalat)
1. Tekintsd át a 00-01 laborokat adatbázis-specifikus fogalmakért
2. Fókuszálj a 02-06 laborokra a megvalósításhoz
3. Mélyedj el a 07-12 laborokban haladó funkciókhoz

#### 🔴 **Haladó útvonal** (Tapasztalt MCP felhasználó)
1. Átfuttasd a 00-03 laborokat kontextus miatt
2. Fókuszálj a 04-09 laborokra az adatbázis integrációért
3. Koncentrálj a 10-12 laborokra az üzembe helyezéshez

## 🛠️ Hogyan használd hatékonyan ezt a tanulási utat

### Sorrendben történő tanulás (Ajánlott)

Kövesd a laborokat sorrendben az átfogó megértésért:

1. **Olvasd el az áttekintést** – Értsd meg, mit fogsz tanulni
2. **Ellenőrizd az előfeltételeket** – Bizonyosodj meg a szükséges tudásodról
3. **Kövess lépésről lépésre útmutatókat** – Valósítsd meg tanulás közben
4. **Teljesítsd a gyakorlatokat** – Mélyítsd el a megértést
5. **Nézd át a főbb tanulságokat** – Szilárdítsd meg az eredményeket

### Célzott tanulás

Ha speciális képességekre van szükséged:

- **Adatbázis-integráció**: Fókuszálj a 04-06 laborokra
- **Biztonság megvalósítás**: Koncentrálj a 02, 08, 12 laborokra
- **AI/Szemantikus keresés**: Mélyedj el a 07 laborban
- **Üzembe helyezés**: Tanulmányozd a 10-12 laborokat

### Gyakorlati tapasztalat

Minden labor tartalmaz:
- **Működő kódpéldákat** – Másold, módosítsd és kísérletezz vele
- **Valós helyzeteket** – Gyakorlati kiskereskedelmi elemzési eseteket
- **Fokozatos összetettséget** – Egyszerűtől a haladóig építve
- **Érvényesítési lépéseket** – Ellenőrizd, hogy működik-e a megvalósításod

## 🌟 Közösség és támogatás

### Kérj segítséget

- **Azure AI Discord**: [Csatlakozz szakértői támogatásért](https://discord.com/invite/ByRwuEEgH4)
- **GitHub tárhely és megvalósítási minta**: [Telepítési minta és források](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP közösség**: [Csatlakozz a kiterjedt MCP beszélgetésekhez](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Készen állsz a kezdésre?

Indítsd el utadat a **[00. labor: Bevezetés az MCP adatbázis-integrációba](./00-Introduction/README.md)** anyaggal

---

*Mesteri szintre emelheted az előállításra kész MCP szerverek építését adatbázis-integrációval ezen az átfogó, gyakorlati tanulási élményen keresztül.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->