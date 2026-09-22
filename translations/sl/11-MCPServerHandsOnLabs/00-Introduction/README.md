# Uvod v integracijo baze podatkov MCP

> [!NOTE]
> Diagrami ali koda v tej učni poti, ki uporabljajo HTTP/SSE ali možnosti inicializacije,
> odražajo vzorčne odvisnosti MCP različice `2025-11-25`. Za nove
> izvedbe uporabljajte brezstanjskih zahtevkov `2026-07-28` in Streamable HTTP.

## 🎯 Kaj zajema ta laboratorij

Ta uvodni laboratorij ponuja celovit pregled gradnje strežnikov Model Context Protocol (MCP) z integracijo baz podatkov. Spoznali boste poslovni primer, tehnično arhitekturo in primere iz resničnega sveta preko analitičnega primera Zava Retail na https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Pregled

**Model Context Protocol (MCP)** omogoča AI asistentom varen dostop in interakcijo z zunanjimi viri podatkov v realnem času. V kombinaciji z integracijo baz podatkov MCP omogoča močne zmožnosti za aplikacije AI, ki temeljijo na podatkih.

Ta učna pot vas nauči graditi MCP strežnike, pripravljene za produkcijo, ki povezujejo AI asistente s podatki o prodaji v trgovinah preko PostgreSQL, pri čemer uporabljajo poslovne vzorce kot so Row Level Security, semantično iskanje in večnajemniški dostop do podatkov.

## Cilji učenja

Ob koncu tega laboratorija boste sposobni:

- **Opredeliti** Model Context Protocol in njegove ključne prednosti za integracijo baz podatkov
- **Prepoznati** ključne komponente arhitekture MCP strežnika z bazami podatkov
- **Razumeti** poslovni primer Zava Retail in njegove poslovne zahteve
- **Prepoznati** poslovne vzorce za varen in razširljiv dostop do baz podatkov
- **Našteti** orodja in tehnologije, uporabljene v tej učni poti

## 🧭 Izziv: AI sreča podatke iz resničnega sveta

### Tradicionalne omejitve AI

Sodobni AI asistenti so izredno zmogljivi, vendar se soočajo z velikimi omejitvami pri delu z resničnimi poslovnimi podatki:

| **Izziv** | **Opis** | **Poslovni vpliv** |
|---------------|-----------------|-------------------|
| **Statično znanje** | AI modeli, usposobljeni na fiksnih podatkovnih nizih, nimajo dostopa do trenutnih poslovnih podatkov | Zastarela spoznanja, zamujene priložnosti |
| **Podatkovni silosi** | Informacije so zaklenjene v bazah podatkov, API-jih in sistemih, do katerih AI nima dostopa | Nepopolna analiza, razdrobljeni delovni procesi |
| **Varnostne omejitve** | Neposreden dostop do baz podatkov povzroča varnostne in skladnostne težave | Omejena uvedba, ročna priprava podatkov |
| **Kompleksna poizvedovanja** | Poslovni uporabniki potrebujejo tehnično znanje za pridobivanje podatkovnih vpogledov | Zmanjšana uporaba, neučinkoviti procesi |

### Rešitev MCP

Model Context Protocol rešuje te izzive z zagotavljanjem:

- **Dostop v realnem času**: AI asistenti poizvedujejo aktivne baze podatkov in API-je
- **Varna integracija**: Kontroliran dostop z avtentikacijo in dovoljenji
- **Vmesnik v naravnem jeziku**: Poslovni uporabniki postavljajo vprašanja v običajni angleščini
- **Standardiziran protokol**: Deluje na različnih AI platformah in orodjih

## 🏪 Spoznajte Zava Retail: Naš študijski primer https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

V tej učni poti bomo zgradili MCP strežnik za **Zava Retail**, fiktivno DIY maloprodajno verigo z več fizičnimi lokacijami trgovin. Ta realistični scenarij prikazuje implementacijo MCP na ravni podjetja.

### Poslovni kontekst

**Zava Retail** posluje:
- **8 fizičnih trgovin** po državi Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 spletna trgovina** za e-trgovino
- **Raznolik katalog izdelkov**, vključno z orodji, strojno opremo, vrtnim materialom in gradbenim materialom
- **Večnivojsko vodstvo** z vodji trgovin, regionalnimi vodji in direktorji

### Poslovne zahteve

Vodje trgovin in direktorji potrebujejo analitiko na osnovi AI za:

1. **Analizo uspešnosti prodaje** po trgovinah in časovnih obdobjih
2. **Spremljanje zalog** in identifikacijo potreb po dopolnitvi
3. **Razumevanje vedenja strank** in vzorcev nakupovanja
4. **Odkritje vpogledov v izdelke** preko semantičnega iskanja
5. **Generiranje poročil** z vprašanji v naravnem jeziku
6. **Vzdrževanje varnosti podatkov** z nadzorom dostopa glede na vloge

### Tehnične zahteve

MCP strežnik mora zagotoviti:

- **Večnajemniški dostop do podatkov**, kjer vodje trgovin vidijo le podatke svoje trgovine
- **Fleksibilne poizvedbe** z podporo za kompleksne SQL operacije
- **Semantično iskanje** za odkrivanje izdelkov in priporočila
- **Podatke v realnem času**, ki odražajo trenutno stanje poslovanja
- **Varno avtentikacijo** z nadzorom na ravni vrstic (RLS)
- **Razširljivo arhitekturo** z zmogljivostjo za več sočasnih uporabnikov

## 🏗️ Pregled arhitekture MCP strežnika

Naš MCP strežnik izvaja slojevito arhitekturo, optimizirano za integracijo baz podatkov:

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

### Ključne komponente

#### **1. MCP sloj strežnika**
- **FastMCP Framework**: Moderna Python implementacija MCP strežnika
- **Registracija orodij**: Deklarativne definicije orodij z varnostjo tipov
- **Kontekst zahtevkov**: Identiteta uporabnika in upravljanje sej
- **Obdelava napak**: Zanesljivo upravljanje napak in beleženje

#### **2. Sloj integracije baze podatkov**
- **Upravljanje povezav**: Učinkovito upravljanje povezav asyncpg
- **Ponudnik shem**: Dinamično odkrivanje shem tabel
- **Izvajalec poizvedb**: Varen SQL z izvajanjem v RLS kontekstu
- **Upravljanje transakcij**: ACID skladnost in obdelava preklicev

#### **3. Varnostni sloj**
- **Row Level Security**: PostgreSQL RLS za izolacijo podatkov večnajemniške uporabe
- **Identiteta uporabnika**: Avtentikacija in avtorizacija vodij trgovin
- **Nadzor dostopa**: Podrobna dovoljenja in revizijske sledi
- **Validacija vhodov**: Preprečevanje SQL injekcij in validacija poizvedb

#### **4. Sloj izboljšav AI**
- **Semantično iskanje**: Vektorski vdelki za odkrivanje izdelkov
- **Azure OpenAI integracija**: Generiranje tekstovnih vdelkov
- **Algoritmi podobnosti**: pgvector iskanje po kosinusni podobnosti
- **Optimizacija iskanja**: Indeksiranje in optimizacija zmogljivosti

## 🔧 Tehnološki sklad

### Osnovne tehnologije

| **Komponenta** | **Tehnologija** | **Namen** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Moderna implementacija MCP strežnika |
| **Baza podatkov** | PostgreSQL 17 + pgvector | Relacijski podatki z vektorskim iskanjem |
| **AI storitve** | Azure OpenAI | Tekstovni vdelki in jezikovni modeli |
| **Kontejnerizacija** | Docker + Docker Compose | Razvojno okolje |
| **Oblačna platforma** | Microsoft Azure | Produkcijska namestitev |
| **Integracija IDE** | VS Code | AI klepet in razvojni tok dela |

### Orodja za razvoj

| **Orodje** | **Namen** |
|----------|-------------|
| **asyncpg** | Visoko zmogljiv PostgreSQL gonilnik |
| **Pydantic** | Validacija in serijalizacija podatkov |
| **Azure SDK** | Integracija oblačnih storitev |
| **pytest** | Testni okvir |
| **Docker** | Kontejnerizacija in namestitev |

### Produkcijski sklad

| **Storitev** | **Azure vir** | **Namen** |
|-------------|-------------------|-------------|
| **Baza podatkov** | Azure Database for PostgreSQL | Upravljana storitev baze podatkov |
| **Kontejner** | Azure Container Apps | Brezstrežni hosting kontejnerjev |
| **AI storitve** | Microsoft Foundry | OpenAI modeli in končne točke |
| **Nadzor** | Application Insights | Opazovanje in diagnostika |
| **Varnost** | Azure Key Vault | Upravljanje skrivnosti in konfiguracij |

## 🎬 Scenariji uporabe iz resničnega sveta

Raziščimo, kako različni uporabniki sodelujejo z našim MCP strežnikom:

### Scenarij 1: Pregled zmogljivosti vodje trgovine

**Uporabnik**: Sarah, vodja trgovine Seattle  
**Cilj**: Analizirati uspešnost prodaje v zadnjem četrtletju

**Poizvedba v naravnem jeziku**:
> "Pokaži mi top 10 izdelkov po prihodku v moji trgovini v 4. četrtletju 2024"

**Kaj se zgodi**:
1. VS Code AI Chat pošlje poizvedbo MCP strežniku
2. MCP strežnik prepozna kontekst trgovine Sarah (Seattle)
3. RLS politike filtrirajo podatke samo za trgovino Seattle
4. SQL poizvedba je generirana in izvedena
5. Rezultati so formatirani in poslani nazaj AI Chat-u
6. AI zagotovi analizo in vpoglede

### Scenarij 2: Odkritje izdelkov s semantičnim iskanjem

**Uporabnik**: Mike, upravitelj zalog  
**Cilj**: Najti izdelke podobne zahtevku stranke

**Poizvedba v naravnem jeziku**:
> "Katero električno vodoodporno priključke za zunanje uporabo prodajamo, ki so podobni temu?"

**Kaj se zgodi**:
1. Poizvedba je obdelana s semantičnim iskalnikom
2. Azure OpenAI generira vektorski vdelki
3. pgvector opravi iskanje po podobnosti
4. Sorodni izdelki so razvrščeni po relevantnosti
5. Rezultati vključujejo podrobnosti izdelkov in razpoložljivost
6. AI predlaga alternative in možnosti pakiranja

### Scenarij 3: Analitika čez več trgovin

**Uporabnik**: Jennifer, regionalna vodja  
**Cilj**: Primerjati uspešnost vseh trgovin

**Poizvedba v naravnem jeziku**:
> "Primerjaj prodajo po kategorijah za vse trgovine v zadnjih 6 mesecih"

**Kaj se zgodi**:
1. RLS kontekst nastavi dostop regionalnemu vodji
2. Generirana je kompleksna poizvedba za več trgovin
3. Podatki so agregirani po vseh lokacijah trgovin
4. Rezultati vključujejo trende in primerjave
5. AI izlušči vpoglede in priporočila

## 🔒 Varnost in poglobljen vpogled v večnajemniško delovanje

Naša implementacija daje prednost varnosti na ravni podjetja:

### Row Level Security (RLS)

PostgreSQL RLS zagotavlja izolacijo podatkov:

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

### Upravljanje identitete uporabnika

Vsaka MCP povezava vključuje:
- **ID vodje trgovine**: Edinstveni identifikator za RLS kontekst
- **Dodelitev vlog**: Dovoljenja in ravni dostopa
- **Upravljanje sej**: Varni avtentikacijski žetoni
- **Revizijsko beleženje**: Popolna zgodovina dostopa

### Zaščita podatkov

Več slojev varnosti:
- **Šifriranje povezav**: TLS za vse povezave z bazo podatkov
- **Preprečevanje SQL injekcij**: Le parametrične poizvedbe
- **Validacija vhodov**: Obsežna validacija zahtev
- **Obdelava napak**: Brez občutljivih podatkov v sporočilih o napaki

## 🎯 Ključne ugotovitve

Po zaključku tega uvoda boste razumeli:

✅ **Vrednost MCP**: Kako MCP povezuje AI asistente in podatke iz resničnega sveta  
✅ **Poslovni kontekst**: Zahteve in izzivi Zava Retail  
✅ **Pregled arhitekture**: Ključne komponente in njihove interakcije  
✅ **Tehnološki sklad**: Orodja in ogrodja uporabljena skozi celotno učno pot  
✅ **Varnostni model**: Večnajemniški dostop do podatkov in zaščita  
✅ **Vzorce uporabe**: Scenariji poizvedb in poteki dela iz resničnega sveta  

## 🚀 Kaj sledi

Pripravljen na poglobitev? Nadaljujte z:

**[Lab 01: Koncepti osnovne arhitekture](../01-Architecture/README.md)**

Spoznajte vzorce arhitekture MCP strežnika, načela oblikovanja baz podatkov in podrobno tehnično izvedbo, ki poganja našo rešitev za maloprodajno analitiko.

## 📚 Dodatni viri

### Dokumentacija MCP
- [MCP Specifikacija](https://modelcontextprotocol.io/docs/) - Uradna dokumentacija protokola
- [MCP za začetnike](https://aka.ms/mcp-for-beginners) - Celovit vodič po MCP
- [FastMCP Dokumentacija](https://github.com/modelcontextprotocol/python-sdk) - Dokumentacija Python SDKja

### Integracija baz podatkov
- [PostgreSQL Dokumentacija](https://www.postgresql.org/docs/) - Celovit referenčni vodič PostgreSQL
- [pgvector Vodič](https://github.com/pgvector/pgvector) - Dokumentacija razširitve vektorjev
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Vodič za PostgreSQL RLS

### Azure storitve
- [Azure OpenAI Dokumentacija](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integracija AI storitev
- [Azure Database za PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Upravljana baza podatkov
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Brezstrežni kontejnerji

---

**Omejitev odgovornosti**: To je učna vaja z uporabo fiktivnih maloprodajnih podatkov. Vedno upoštevajte politike upravljanja podatkov in varnosti vaše organizacije pri izvajanju podobnih rešitev v produkcijskih okoljih.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->