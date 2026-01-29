# Uvod v integracijo podatkovnih baz z MCP

## 🎯 Kaj zajema ta laboratorij

Ta uvodni laboratorij ponuja celovit pregled gradnje strežnikov Model Context Protocol (MCP) z integracijo podatkovnih baz. Spoznali boste poslovni primer, tehnično arhitekturo in resnične aplikacije skozi primer uporabe analitike Zava Retail na https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Pregled

**Model Context Protocol (MCP)** omogoča AI asistentom varno dostopanje in interakcijo z zunanjimi viri podatkov v realnem času. Ko je združen z integracijo podatkovnih baz, MCP odklene močne zmogljivosti za aplikacije umetne inteligence, ki temeljijo na podatkih.

Ta učna pot vas nauči, kako zgraditi produkcijsko pripravljene MCP strežnike, ki povezujejo AI asistente s podatki o prodaji na drobno prek PostgreSQL, pri čemer se uporabljajo vzorci za podjetja, kot so varnost na ravni vrstic, semantično iskanje in dostop do podatkov za več najemnikov.

## Cilji učenja

Do konca tega laboratorija boste lahko:

- **Definirali** Model Context Protocol in njegove ključne prednosti za integracijo podatkovnih baz
- **Prepoznali** ključne komponente arhitekture MCP strežnika z bazami podatkov
- **Razumeli** primer uporabe Zava Retail in njegove poslovne zahteve
- **Prepoznali** vzorce za varno in razširljivo dostopanje do podatkov
- **Našteli** orodja in tehnologije, uporabljene v tej učni poti

## 🧭 Izziv: AI in resnični podatki

### Omejitve tradicionalne umetne inteligence

Sodobni AI asistenti so izjemno zmogljivi, vendar se soočajo z velikimi omejitvami pri delu z resničnimi poslovnimi podatki:

| **Izziv** | **Opis** | **Poslovni vpliv** |
|-----------|----------|--------------------|
| **Statično znanje** | AI modeli, usposobljeni na fiksnih podatkovnih nizih, ne morejo dostopati do trenutnih poslovnih podatkov | Zastareli vpogledi, zamujene priložnosti |
| **Podatkovni silosi** | Informacije so zaklenjene v bazah podatkov, API-jih in sistemih, do katerih AI nima dostopa | Nepopolna analiza, razdrobljeni delovni tokovi |
| **Varnostne omejitve** | Neposreden dostop do baz podatkov povzroča varnostne in skladnostne težave | Omejena uporaba, ročna priprava podatkov |
| **Zapletene poizvedbe** | Poslovni uporabniki potrebujejo tehnično znanje za pridobivanje vpogledov iz podatkov | Manjša uporaba, neučinkoviti procesi |

### Rešitev MCP

Model Context Protocol rešuje te izzive z zagotavljanjem:

- **Dostopa do podatkov v realnem času**: AI asistenti poizvedujejo po živih bazah podatkov in API-jih
- **Varne integracije**: Nadzorovan dostop z avtentikacijo in dovoljenji
- **Vmesnika v naravnem jeziku**: Poslovni uporabniki postavljajo vprašanja v preprostem jeziku
- **Standardiziranega protokola**: Deluje na različnih AI platformah in orodjih

## 🏪 Spoznajte Zava Retail: Naša študija primera https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

V tej učni poti bomo zgradili MCP strežnik za **Zava Retail**, izmišljeno verigo trgovin za domače mojstre z več lokacijami. Ta realističen scenarij prikazuje implementacijo MCP na ravni podjetja.

### Poslovni kontekst

**Zava Retail** upravlja:
- **8 fizičnih trgovin** v zvezni državi Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 spletno trgovino** za e-prodajo
- **Raznolik katalog izdelkov**, ki vključuje orodja, strojno opremo, vrtnarske pripomočke in gradbene materiale
- **Večnivojsko upravljanje** z vodji trgovin, regionalnimi vodji in vodstvom podjetja

### Poslovne zahteve

Vodje trgovin in vodstvo potrebujejo analitiko, podprto z AI, za:

1. **Analizo prodajne uspešnosti** po trgovinah in časovnih obdobjih
2. **Sledenje zalogam** in prepoznavanje potreb po ponovnem naročanju
3. **Razumevanje vedenja strank** in nakupnih vzorcev
4. **Odkritje vpogledov o izdelkih** s semantičnim iskanjem
5. **Generiranje poročil** z naravnimi jezikovnimi poizvedbami
6. **Ohranjanje varnosti podatkov** z nadzorom dostopa na podlagi vlog

### Tehnične zahteve

MCP strežnik mora zagotavljati:

- **Dostop do podatkov za več najemnikov**, kjer vodje trgovin vidijo le podatke svoje trgovine
- **Prilagodljive poizvedbe**, ki podpirajo zapletene SQL operacije
- **Semantično iskanje** za odkrivanje izdelkov in priporočila
- **Podatke v realnem času**, ki odražajo trenutno stanje poslovanja
- **Varno avtentikacijo** z varnostjo na ravni vrstic
- **Razširljivo arhitekturo**, ki podpira več hkratnih uporabnikov

## 🏗️ Pregled arhitekture MCP strežnika

Naš MCP strežnik implementira slojno arhitekturo, optimizirano za integracijo podatkovnih baz:

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

#### **1. Sloj MCP strežnika**
- **FastMCP Framework**: Sodobna implementacija MCP strežnika v Pythonu
- **Registracija orodij**: Deklarativne definicije orodij z varnostjo tipov
- **Kontekst poizvedb**: Upravljanje identitete uporabnikov in sej
- **Obravnava napak**: Zanesljivo upravljanje napak in beleženje

#### **2. Sloj integracije podatkovnih baz**
- **Upravljanje povezav**: Učinkovito upravljanje povezav asyncpg
- **Ponudnik shem**: Dinamično odkrivanje shem tabel
- **Izvajalec poizvedb**: Varno izvajanje SQL poizvedb z RLS kontekstom
- **Upravljanje transakcij**: Skladnost z ACID in obravnava povratkov

#### **3. Varnostni sloj**
- **Varnost na ravni vrstic**: PostgreSQL RLS za izolacijo podatkov za več najemnikov
- **Identiteta uporabnikov**: Avtentikacija in avtorizacija vodij trgovin
- **Nadzor dostopa**: Dovoljenja na podlagi vlog in revizijske sledi
- **Validacija vnosa**: Preprečevanje SQL vbrizgavanja in validacija poizvedb

#### **4. Sloj izboljšanja AI**
- **Semantično iskanje**: Vektorske vdelave za odkrivanje izdelkov
- **Integracija Azure OpenAI**: Generiranje vdelav besedila
- **Algoritmi podobnosti**: pgvector iskanje s kosinusno podobnostjo
- **Optimizacija iskanja**: Indeksiranje in izboljšanje zmogljivosti

## 🔧 Tehnološki sklad

### Osnovne tehnologije

| **Komponenta** | **Tehnologija** | **Namen** |
|----------------|-----------------|-----------|
| **MCP Framework** | FastMCP (Python) | Sodobna implementacija MCP strežnika |
| **Podatkovna baza** | PostgreSQL 17 + pgvector | Relacijski podatki z vektorskim iskanjem |
| **AI storitve** | Azure OpenAI | Vdelave besedila in jezikovni modeli |
| **Kontejnerizacija** | Docker + Docker Compose | Razvojno okolje |
| **Oblak** | Microsoft Azure | Produkcijsko uvajanje |
| **Integracija IDE** | VS Code | AI Chat in razvojni potek dela |

### Razvojna orodja

| **Orodje** | **Namen** |
|------------|-----------|
| **asyncpg** | Visoko zmogljiv gonilnik za PostgreSQL |
| **Pydantic** | Validacija in serializacija podatkov |
| **Azure SDK** | Integracija oblačnih storitev |
| **pytest** | Okvir za testiranje |
| **Docker** | Kontejnerizacija in uvajanje |

### Produkcijski sklad

| **Storitev** | **Azure vir** | **Namen** |
|--------------|---------------|-----------|
| **Podatkovna baza** | Azure Database for PostgreSQL | Upravljana storitev podatkovne baze |
| **Kontejner** | Azure Container Apps | Gostovanje kontejnerjev brez strežnika |
| **AI storitve** | Azure AI Foundry | OpenAI modeli in končne točke |
| **Nadzor** | Application Insights | Opazovanje in diagnostika |
| **Varnost** | Azure Key Vault | Upravljanje skrivnosti in konfiguracij |

## 🎬 Scenariji uporabe v resničnem svetu

Poglejmo, kako različni uporabniki uporabljajo naš MCP strežnik:

### Scenarij 1: Pregled uspešnosti vodje trgovine

**Uporabnik**: Sarah, vodja trgovine v Seattlu  
**Cilj**: Analizirati prodajno uspešnost v zadnjem četrtletju

**Poizvedba v naravnem jeziku**:
> "Pokaži mi 10 najboljših izdelkov po prihodkih za mojo trgovino v Q4 2024"

**Kaj se zgodi**:
1. VS Code AI Chat pošlje poizvedbo MCP strežniku
2. MCP strežnik identificira kontekst trgovine Sarah (Seattle)
3. RLS politike filtrirajo podatke samo za trgovino v Seattlu
4. SQL poizvedba se generira in izvede
5. Rezultati se formatirajo in vrnejo AI Chatu
6. AI ponudi analizo in vpoglede

### Scenarij 2: Odkritje izdelkov s semantičnim iskanjem

**Uporabnik**: Mike, upravitelj zalog  
**Cilj**: Najti izdelke, podobne zahtevam stranke

**Poizvedba v naravnem jeziku**:
> "Katere izdelke prodajamo, ki so podobni 'vodoodpornim električnim konektorjem za zunanjo uporabo'?"

**Kaj se zgodi**:
1. Poizvedba se obdela z orodjem za semantično iskanje
2. Azure OpenAI generira vektorsko vdelavo
3. pgvector izvede iskanje podobnosti
4. Sorodni izdelki so razvrščeni po ustreznosti
5. Rezultati vključujejo podrobnosti o izdelkih in razpoložljivost
6. AI predlaga alternative in možnosti združevanja

### Scenarij 3: Analitika med trgovinami

**Uporabnik**: Jennifer, regionalna vodja  
**Cilj**: Primerjati uspešnost med vsemi trgovinami

**Poizvedba v naravnem jeziku**:
> "Primerjaj prodajo po kategorijah za vse trgovine v zadnjih 6 mesecih"

**Kaj se zgodi**:
1. RLS kontekst je nastavljen za dostop regionalne vodje
2. Generira se zapletena poizvedba za več trgovin
3. Podatki se združijo po lokacijah trgovin
4. Rezultati vključujejo trende in primerjave
5. AI identificira vpoglede in priporočila

## 🔒 Poglobljen pogled na varnost in večnajemništvo

Naša implementacija daje prednost varnosti na ravni podjetja:

### Varnost na ravni vrstic (RLS)

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

### Upravljanje identitete uporabnikov

Vsaka povezava MCP vključuje:
- **ID vodje trgovine**: Edinstven identifikator za RLS kontekst
- **Dodelitev vlog**: Dovoljenja in ravni dostopa
- **Upravljanje sej**: Varni avtentikacijski žetoni
- **Revizijsko beleženje**: Popolna zgodovina dostopa

### Zaščita podatkov

Več plasti varnosti:
- **Šifriranje povezav**: TLS za vse povezave z bazo podatkov
- **Preprečevanje SQL vbrizgavanja**: Samo parametizirane poizvedbe
- **Validacija vnosa**: Celovita validacija zahtevkov
- **Obravnava napak**: Brez občutljivih podatkov v sporočilih o napakah

## 🎯 Ključni poudarki

Po zaključku tega uvoda bi morali razumeti:

✅ **Vrednost MCP**: Kako MCP povezuje AI asistente in resnične podatke  
✅ **Poslovni kontekst**: Zahteve in izzivi Zava Retail  
✅ **Pregled arhitekture**: Ključne komponente in njihove interakcije  
✅ **Tehnološki sklad**: Orodja in okvirji, uporabljeni skozi celotno pot  
✅ **Varnostni model**: Dostop do podatkov za več najemnikov in zaščita  
✅ **Vzorce uporabe**: Resnični scenariji poizvedb in delovni tokovi  

## 🚀 Kaj sledi

Pripravljeni na poglobitev? Nadaljujte z:

**[Laboratorij 01: Osnovni koncepti arhitekture](../01-Architecture/README.md)**

Spoznajte vzorce arhitekture MCP strežnika, načela oblikovanja podatkovnih baz in podrobno tehnično implementacijo, ki poganja našo rešitev za analitiko na drobno.

## 📚 Dodatni viri

### Dokumentacija MCP
- [Specifikacija MCP](https://modelcontextprotocol.io/docs/) - Uradna dokumentacija protokola
- [MCP za začetnike](https://aka.ms/mcp-for-beginners) - Celovit vodnik za učenje MCP
- [Dokumentacija FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentacija za Python SDK

### Integracija podatkovnih baz
- [Dokumentacija PostgreSQL](https://www.postgresql.org/docs/) - Celoten referenčni priročnik za PostgreSQL
- [Vodič za pgvector](https://github.com/pgvector/pgvector) - Dokumentacija za razširitev vektorjev
- [Varnost na ravni vrstic](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Vodič za PostgreSQL RLS

### Azure storitve
- [Dokumentacija Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integracija AI storitev
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Upravljana storitev podatkovne baze
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontejnerji brez strežnika

---

**Omejitev odgovornosti**: To je učna vaja z uporabo izmišljenih podatkov o prodaji na drobno. Vedno upoštevajte politike upravljanja podatkov in varnosti vaše organizacije pri implementaciji podobnih rešitev v produkcijskih okoljih.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.