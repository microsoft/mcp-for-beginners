# Bevezetés az MCP Adatbázis Integrációba

> [!NOTE]
> A tanulási út ezen diagramjai vagy kódjai, amelyek HTTP/SSE vagy inicializációs
> opciókat használnak, a minta MCP `2025-11-25` függőségeit tükrözik. Új
> megvalósítások esetén használja a `2026-07-28` állapotmentes kéréseket és a Streamable HTTP-t.

## 🎯 Amit ez a laboratórium lefed

Ez a bevezető laboratórium átfogó áttekintést nyújt az Model Context Protocol (MCP) szerverek adatbázis-integrációval történő felépítéséről. Megértheti az üzleti esetet, a műszaki architektúrát, és a valós alkalmazási eseteket a Zava Retail elemzési példáján keresztül, amely megtalálható a https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail oldalon.

## Áttekintés

**A Model Context Protocol (MCP)** lehetővé teszi az AI asszisztensek számára, hogy valós időben biztonságosan hozzáférjenek és interakcióba lépjenek külső adatforrásokkal. Adatbázis-integrációval kombinálva az MCP erőteljes képességeket nyit meg az adatalapú AI alkalmazások számára.

Ez a tanulási út megtanítja, hogyan építsünk éles használatra kész MCP szervereket, amelyek PostgreSQL-en keresztül kapcsolják az AI asszisztenseket a kiskereskedelmi értékesítési adatokhoz, olyan vállalati minták megvalósításával, mint a sor szintű biztonság, szemantikus keresés és többbérlős adat-hozzáférés.

## Tanulási célok

A labor végére képes lesz:

- **Meghatározni** a Model Context Protocolt és annak alapvető előnyeit az adatbázis-integrációban
- **Azonosítani** egy MCP szerver architektúra kulcsfontosságú elemeit adatbázisokkal
- **Megérteni** a Zava Retail használati esetét és üzleti követelményeit
- **Fel-ismerni** az üzleti mintákat a biztonságos, skálázható adatbázis-hozzáféréshez
- **Felsorolni** azokat az eszközöket és technológiákat, amiket ezen a tanulási úton használunk

## 🧭 A kihívás: Az AI találkozik a valós üzleti adatokkal

### Hagyományos AI korlátok

A modern AI asszisztensek hihetetlenül erősek, de jelentős korlátokkal szembesülnek a valós üzleti adatokkal dolgozva:

| **Kihívás** | **Leírás** | **Üzleti hatás** |
|---------------|-----------------|-------------------|
| **Statikus tudás** | Az AI modellek fix adatkészleteken tanultak, nem férnek hozzá aktuális üzleti adatokhoz | Elavult betekintések, kihagyott lehetőségek |
| **Adatszigetek** | Információk zárva adatbázisokban, API-kban és rendszerekben, amiket az AI nem ér el | Hiányos elemzés, töredezett munkafolyamatok |
| **Biztonsági korlátok** | Közvetlen adatbázis hozzáférés biztonsági és megfelelőségi aggályokat vet fel | Korlátozott telepítés, manuális adat-előkészítés |
| **Bonyolult lekérdezések** | Az üzleti felhasználóknak technikai tudásra van szükségük az adatkinyeréshez | Csökkent elfogadás, nem hatékony folyamatok |

### Az MCP megoldás

A Model Context Protocol ezekre a kihívásokra ad választ az alábbiakkal:

- **Valós idejű adat-hozzáférés**: Az AI asszisztensek élő adatbázisokat és API-kat kérdeznek le
- **Biztonságos integráció**: Szabályozott hozzáférés hitelesítéssel és jogosultságokkal
- **Természetes nyelvű felület**: Az üzleti felhasználók egyszerű angol kérdéseket tesznek fel
- **Standardizált protokoll**: Különböző AI platformok és eszközök között működik

## 🏪 Ismerkedjünk meg a Zava Retail-lel: Tanulási esettanulmányunk https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Ezen a tanulási úton egy MCP szervert építünk a **Zava Retail** számára, egy fiktív barkács-áruházlánc több üzlethellyel. Ez a valósághű forgatókönyv bemutatja az üzleti szintű MCP megvalósítást.

### Üzleti kontextus

A **Zava Retail** működteti:
- **8 fizikai üzletet** Washington államban (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online áruházat** e-kereskedelmi értékesítésre
- **Sokszínű termékkatalógust**, beleértve szerszámokat, hardvert, kertészeti kellékeket és építőanyagokat
- **Többszintű menedzsmentet** üzletvezetőkkel, régiós vezetőkkel és vezetőséggel

### Üzleti követelmények

Az üzletvezetőknek és vezetőknek AI-alapú elemzésekre van szükségük, hogy:

1. **Elemezzék az értékesítési teljesítményt** az üzletek és időszakok szerint
2. **Nyomon kövessék a készletszinteket** és az újratöltés szükségességét
3. **Megértsék a vásárlói viselkedést** és a vásárlási mintázatokat
4. **Fedezzenek fel termék-információkat** szemantikus kereséssel
5. **Készítsenek jelentéseket** természetes nyelvű lekérdezésekkel
6. **Fenntartsák az adatbiztonságot** szerepalapú hozzáférés-vezérléssel

### Műszaki követelmények

Az MCP szervernek biztosítania kell:

- **Többszintű adat-hozzáférést**, ahol az üzletvezetők csak saját üzletük adatait látják
- **Rugalmas lekérdezést**, amely támogatja a bonyolult SQL műveleteket
- **Szemantikus keresést** a termékfeltáráshoz és ajánlásokhoz
- **Valós idejű adatokat**, amelyek tükrözik az aktuális üzleti állapotot
- **Biztonságos hitelesítést** sor szintű biztonsággal
- **Skálázható architektúrát**, amely több párhuzamos felhasználót támogat

## 🏗️ MCP szerver architektúra áttekintése

MCP szerverünk rétegzett architektúrát valósít meg, optimalizálva az adatbázis-integrációhoz:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Kulcs komponensek

#### **1. MCP szerver réteg**
- **FastMCP keretrendszer**: Modern Python MCP szerver implementáció
- **Eszközregisztráció**: Deklaratív eszközdefiníciók típusbiztonsággal
- **Kéréstörténet**: Felhasználói azonosítás és munkamenet-kezelés
- **Hiba kezelés**: Robusztus hibakezelés és naplózás

#### **2. Adatbázis integrációs réteg**
- **Kapcsolat pool-ozás**: Hatékony asyncpg kapcsolatkezelés
- **Séma szolgáltató**: Dinamikus táblaséma-felderítés
- **Lekérdezés végrehajtó**: Biztonságos SQL végrehajtás RLS kontextussal
- **Tranzakció kezelés**: ACID kompatibilitás és visszagörgetés

#### **3. Biztonsági réteg**
- **Sor szintű biztonság (RLS)**: PostgreSQL RLS a többbérlős adat izolációhoz
- **Felhasználói azonosítás**: Üzletvezető hitelesítés és engedélyezés
- **Hozzáférés-vezérlés**: Finomhangolt jogosultságok és audit naplók
- **Bemeneti érvényesítés**: SQL befecskendezés elleni védelem és lekérdezés validálás

#### **4. AI fejlesztő réteg**
- **Szemantikus keresés**: Vektor beágyazások a termékfeltáráshoz
- **Azure OpenAI integráció**: Szöveg beágyazó generálás
- **Hasonlósági algoritmusok**: pgvector koszinusz hasonlósági keresés
- **Keresés optimalizáció**: Indexelés és teljesítményhangolás

## 🔧 Technológiai stack

### Alap technológiák

| **Komponens** | **Technológia** | **Cél** |
|---------------|----------------|-------------|
| **MCP keretrendszer** | FastMCP (Python) | Modern MCP szerver implementáció |
| **Adatbázis** | PostgreSQL 17 + pgvector | Relációs adat vektoros kereséssel |
| **AI szolgáltatások** | Azure OpenAI | Szövegbeágyazás és nyelvi modellek |
| **Konténerizáció** | Docker + Docker Compose | Fejlesztési környezet |
| **Felhő platform** | Microsoft Azure | Éles telepítés |
| **IDE integráció** | VS Code | AI Chat és fejlesztési munkafolyamat |

### Fejlesztői eszközök

| **Eszköz** | **Cél** |
|----------|-------------|
| **asyncpg** | Nagy teljesítményű PostgreSQL driver |
| **Pydantic** | Adat érvényesítés és sorosítás |
| **Azure SDK** | Felhő szolgáltatás integráció |
| **pytest** | Tesztelési keretrendszer |
| **Docker** | Konténerizáció és telepítés |

### Éles környezet stack

| **Szolgáltatás** | **Azure erőforrás** | **Cél** |
|-------------|-------------------|-------------|
| **Adatbázis** | Azure Database for PostgreSQL | Kezelt adatbázis szolgáltatás |
| **Konténer** | Azure Container Apps | Szerver nélküli konténer hoszting |
| **AI szolgáltatások** | Microsoft Foundry | OpenAI modellek és végpontok |
| **Monitoring** | Application Insights | Megfigyelhetőség és diagnosztika |
| **Biztonság** | Azure Key Vault | Titkok és konfiguráció kezelése |

## 🎬 Valós használati esetek

Nézzük meg, hogyan lépnek kapcsolatba különböző felhasználók az MCP szerverrel:

### Forgatókönyv 1: Üzletvezető teljesítmény értékelés

**Felhasználó**: Sarah, Seattle üzletvezető  
**Cél**: Elemzi az elmúlt negyedév értékesítési teljesítményét

**Természetes nyelvű lekérdezés**:
> "Mutasd meg az én üzletem top 10 bevételtermelő termékét a 2024 Q4-ben"

**A történés menete**:
1. A VS Code AI Chat lekérdezést küld az MCP szervernek
2. Az MCP szerver azonosítja Sarah üzletének kontextusát (Seattle)
3. Az RLS irányelvek csak Seattle üzlet adatait engedik át
4. Az SQL lekérdezés létrejön és végrehajtódik
5. Az eredmény formázva visszakerül az AI Chathez
6. Az AI elemzést és betekintést ad

### Forgatókönyv 2: Termékfeltárás szemantikus kereséssel

**Felhasználó**: Mike, Készletkezelő  
**Cél**: Olyan termékek megtalálása, amelyek hasonlóak egy vásárlói kéréshez

**Természetes nyelvű lekérdezés**:
> "Milyen termékeket árulunk, amelyek hasonlítanak a 'kültéri vízálló elektromos csatlakozók'-ra?"

**A történés menete**:
1. A lekérdezés feldolgozása a szemantikus kereső eszköz által
2. Az Azure OpenAI generálja a beágyazási vektort
3. A pgvector kivégzi a hasonlósági keresést
4. A kapcsolódó termékeket relevancia szerint rangsorolják
5. Eredmények tartalmazzák a termék részleteit és elérhetőségét
6. Az AI alternatívákat és csomagolási lehetőségeket javasol

### Forgatókönyv 3: Több üzlet elemzése

**Felhasználó**: Jennifer, Régiós menedzser  
**Cél**: Az összes üzlet teljesítményének összehasonlítása

**Természetes nyelvű lekérdezés**:
> "Hasonlítsuk össze az értékesítést kategóriánként az összes üzletben az elmúlt 6 hónapban"

**A történés menete**:
1. Az RLS kontextus beállítása a régiós menedzser hozzáféréséhez
2. Bonyolult több üzlet lekérdezés generálása
3. Adatok aggregálása az üzlethelyszínek között
4. Eredmények tartalmazzák a trendeket és összehasonlításokat
5. Az AI felismeri a betekintéseket és ajánlásokat

## 🔒 Biztonság és többbérlős mélyreható elemzés

Megvalósításunk az üzleti szintű biztonságot helyezi előtérbe:

### Sor szintű biztonság (RLS)

A PostgreSQL RLS biztosítja az adat izolációt:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Felhasználói azonosítás kezelése

Minden MCP kapcsolat tartalmazza:
- **Üzletvezető azonosítót**: Egyedi azonosító az RLS kontextushoz
- **Szerepkör hozzárendelést**: Jogosultságok és hozzáférési szintek
- **Munkamenet kezelést**: Biztonságos hitelesítési tokenek
- **Audit naplózást**: Teljes hozzáférési előzmények

### Adatvédelem

Többrétegű biztonság:
- **Kapcsolat titkosítás**: TLS minden adatbázis kapcsolatnál
- **SQL befecskendezés elleni védelem**: Csak paraméterezett lekérdezések
- **Bemenet érvényesítés**: Átfogó kérés validálás
- **Hiba kezelés**: Nincs érzékeny adat a hibaüzenetekben

## 🎯 Legfontosabb tanulságok

A bevezető elvégzése után meg kell értenie:

✅ **MCP értékajánlat**: Hogyan köti össze az MCP az AI asszisztenseket és a valós adatokat  
✅ **Üzleti környezet**: Zava Retail követelményei és kihívásai  
✅ **Architektúra áttekintés**: Kulcs komponensek és azok kölcsönhatásai  
✅ **Technológiai stack**: Az egész tanulási út során használt eszközök és keretrendszerek  
✅ **Biztonsági modell**: Többbérlős adat-hozzáférés és védelem  
✅ **Használati minták**: Valós lekérdezési forgatókönyvek és munkafolyamatok  

## 🚀 Mi következik

Készen áll a mélyebb merülésre? Folytassa a következővel:

**[Labor 01: Alapvető architektúra fogalmak](../01-Architecture/README.md)**

Ismerje meg az MCP szerver architektúra mintákat, az adatbázis tervezési elveket, és a részletes műszaki megvalósítást, ami működteti kiskereskedelmi elemzési megoldásunkat.

## 📚 További források

### MCP dokumentáció
- [MCP specifikáció](https://modelcontextprotocol.io/docs/) - Hivatalos protokoll dokumentáció
- [MCP kezdőknek](https://aka.ms/mcp-for-beginners) - Átfogó MCP tanulási útmutató
- [FastMCP dokumentáció](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokumentáció

### Adatbázis integráció
- [PostgreSQL dokumentáció](https://www.postgresql.org/docs/) - Teljes PostgreSQL referencia
- [pgvector útmutató](https://github.com/pgvector/pgvector) - Vektor kiterjesztés dokumentáció
- [Sor szintű biztonság](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS útmutató

### Azure szolgáltatások
- [Azure OpenAI dokumentáció](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI szolgáltatás integráció
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Kezelt adatbázis szolgáltatás
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Szerver nélküli konténerek

---

**Felelősség kizárása**: Ez egy tanulási gyakorlat fiktív kiskereskedelmi adatokkal. Mindig kövesse a szervezete adatkezelési és biztonsági szabályzatait hasonló megoldások éles környezetben történő megvalósításakor.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->