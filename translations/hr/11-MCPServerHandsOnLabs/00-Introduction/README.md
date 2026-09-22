# Uvod u integraciju baze podataka MCP

> [!NOTE]
> Dijagrami ili kod u ovom putu učenja koji koriste HTTP/SSE ili opcije inicijalizacije
> odražavaju uzorke MCP `2025-11-25` ovisnosti. Za nove
> implementacije koristite `2026-07-28` stateless zahtjeve i Streamable HTTP.

## 🎯 Što ovaj laboratorij pokriva

Ovaj uvodni laboratorij pruža sveobuhvatni pregled izgradnje Model Context Protocol (MCP) servera s integracijom baza podataka. Razumjet ćete poslovni slučaj, tehničku arhitekturu i stvarne primjene kroz Zava Retail analitiku na https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Pregled

**Model Context Protocol (MCP)** omogućuje AI asistentima siguran pristup i interakciju s vanjskim izvorima podataka u stvarnom vremenu. Kada se kombinira s integracijom baza podataka, MCP otključava moćne mogućnosti za AI aplikacije vođene podacima.

Ovaj put učenja vas uči kako izgraditi MCP servere spremne za proizvodnju koji povezuju AI asistente s podacima o maloprodajnoj prodaji putem PostgreSQL-a, implementirajući enterprise obrasce poput Row Level Security, semantičkog pretraživanja i višekorisničkog pristupa podacima.

## Ciljevi učenja

Do kraja ovog laboratorija moći ćete:

- **Definirati** Model Context Protocol i njegove ključne prednosti za integraciju baza podataka
- **Identificirati** ključne komponente MCP server arhitekture s bazama podataka
- **Razumjeti** Zava Retail slučaj i njegove poslovne zahtjeve
- **Prepoznati** enterprise obrasce za siguran, skalabilan pristup bazi podataka
- **Navesti** alate i tehnologije korištene kroz ovaj put učenja

## 🧭 Izazov: AI susreće stvarne podatke

### Ograničenja tradicionalnog AI

Moderni AI asistenti su nevjerojatno moćni, ali suočavaju se sa značajnim ograničenjima pri radu sa stvarnim poslovnim podacima:

| **Izazov** | **Opis** | **Poslovni učinak** |
|---------------|-----------------|-------------------|
| **Statističko znanje** | AI modeli trenirani na fiksnim skupovima podataka ne mogu pristupiti aktualnim poslovnim podacima | Zastarjeli uvidi, propuštene prilike |
| **Podatkovni silosi** | Informacije zaključane u bazama podataka, API-jima i sustavima do kojih AI ne može doći | Nepotpuna analiza, fragmentirani radni tokovi |
| **Sigurnosna ograničenja** | Direktni pristup bazama podataka podiže sigurnosna i usklađenostna pitanja | Ograničena primjena, ručna priprema podataka |
| **Složeni upiti** | Poslovni korisnici trebaju tehničko znanje za izvlačenje uvida iz podataka | Smanjena prihvaćenost, neefikasni procesi |

### MCP rješenje

Model Context Protocol rješava ove izazove pružajući:

- **Pristup podacima u stvarnom vremenu**: AI asistenti upitaju žive baze podataka i API-je
- **Sigurna integracija**: Kontrolirani pristup s autentifikacijom i dozvolama
- **Sučelje prirodnog jezika**: Poslovni korisnici postavljaju pitanja običnim jezikom
- **Standardizirani protokol**: Radi na različitim AI platformama i alatima

## 🏪 Upoznajte Zava Retail: Naš studijski slučaj https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Tijekom ovog puta učenja izgradit ćemo MCP server za **Zava Retail**, fiktivni DIY maloprodajni lanac s više prodajnih mjesta. Ovaj realističan scenarij demonstrira enterprise implementaciju MCP-a.

### Poslovni kontekst

**Zava Retail** posluje s:
- **8 fizičkih trgovina** diljem savezne države Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online trgovinom** za e-trgovinu
- **Raznolikim katalogom proizvoda** koji uključuje alate, hardver, vrtne potrepštine i građevinski materijal
- **Višerazinskim upravljanjem** s voditeljima trgovina, regionalnim menadžerima i izvršnim osobama

### Poslovni zahtjevi

Voditelji trgovina i izvršni menadžeri trebaju AI-pokretanu analitiku da:

1. **Analiziraju prodajne rezultate** kroz trgovine i vremenske periode
2. **Prate razine zaliha** i identificiraju potrebe za ponovnim naručivanjem
3. **Razumiju ponašanje kupaca** i obrasce kupovine
4. **Otkrivaju uvide o proizvodima** kroz semantičko pretraživanje
5. **Generiraju izvještaje** koristeći pitanja prirodnim jezikom
6. **Održavaju sigurnost podataka** s kontrolom pristupa temeljenu na ulogama

### Tehnički zahtjevi

MCP server mora pružiti:

- **Višekorisnički pristup podacima** gdje voditelji trgovina vide samo podatke svoje trgovine
- **Fleksibilno upitavanje** koje podržava složene SQL operacije
- **Semantičko pretraživanje** za otkrivanje proizvoda i preporuke
- **Podatke u stvarnom vremenu** koji odražavaju aktualno stanje poslovanja
- **Sigurnu autentifikaciju** s row-level security
- **Skalabilnu arhitekturu** koja podržava više istovremenih korisnika

## 🏗️ Pregled arhitekture MCP servera

Naš MCP server implementira slojevitu arhitekturu optimiziranu za integraciju baza podataka:

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

#### **1. MCP Server sloj**
- **FastMCP Framework**: Moderna Python implementacija MCP servera
- **Registracija alata**: Deklarativne definicije alata s tipnom sigurnošću
- **Kontekst zahtjeva**: Identitet korisnika i upravljanje sesijom
- **Rukovanje pogreškama**: Robusno upravljanje i zapisivanje pogrešaka

#### **2. Sloj integracije baze podataka**
- **Povezivanje putem pool-a**: Efikasno upravljanje asinhronim pg vezama
- **Pružatelj šeme**: Dinamičko otkrivanje šema tablica
- **Izvršitelj upita**: Sigurno izvođenje SQL-a s RLS kontekstom
- **Upravljanje transakcijama**: ACID usklađenost i obrada povrata

#### **3. Sigurnosni sloj**
- **Row Level Security**: PostgreSQL RLS za višekorisničku izolaciju podataka
- **Identitet korisnika**: Autentifikacija i autorizacija voditelja trgovine
- **Kontrola pristupa**: Detaljne dozvole i revizijski zapisi
- **Validacija unosa**: Prevencija SQL injekcija i validacija upita

#### **4. AI sloj za poboljšanja**
- **Semantičko pretraživanje**: Vektorski ugrađeni prikazi za otkrivanje proizvoda
- **Azure OpenAI integracija**: Generiranje tekstualnih ugrađivanja
- **Algoritmi sličnosti**: pgvector cosinusno pretraživanje sličnosti
- **Optimizacija pretraživanja**: Indeksiranje i podešavanje performansi

## 🔧 Tehnološki paket

### Osnovne tehnologije

| **Komponenta** | **Tehnologija** | **Namjena** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Moderna implementacija MCP servera |
| **Baza podataka** | PostgreSQL 17 + pgvector | Relacijski podaci s vektorskim pretraživanjem |
| **AI usluge** | Azure OpenAI | Tekstualna ugrađivanja i jezični modeli |
| **Kontejnerizacija** | Docker + Docker Compose | Razvojno okruženje |
| **Cloud platforma** | Microsoft Azure | Proizvodno okruženje |
| **IDE integracija** | VS Code | AI chat i razvojni tijek rada |

### Alati za razvoj

| **Alat** | **Namjena** |
|----------|-------------|
| **asyncpg** | Visokoperformansni PostgreSQL driver |
| **Pydantic** | Validacija i serijalizacija podataka |
| **Azure SDK** | Integracija cloud usluga |
| **pytest** | Okvir za testiranje |
| **Docker** | Kontejnerizacija i implementacija |

### Produkcijski paket

| **Usluga** | **Azure resurs** | **Namjena** |
|-------------|-------------------|-------------|
| **Baza podataka** | Azure Database for PostgreSQL | Upravljačka baza podataka |
| **Kontejner** | Azure Container Apps | Bezbrižno hostiranje kontejnera |
| **AI usluge** | Microsoft Foundry | OpenAI modeli i krajnje točke |
| **Nadzor** | Application Insights | Praćenje i dijagnostika |
| **Sigurnost** | Azure Key Vault | Upravljanje tajnama i konfiguracijom |

## 🎬 Stvarni scenariji korištenja

Pogledajmo kako različiti korisnici komuniciraju s našim MCP serverom:

### Scenarij 1: Pregled performansi voditelja trgovine

**Korisnik**: Sarah, voditeljica trgovine u Seattleu  
**Cilj**: Analizirati prodajne rezultate zadnjeg kvartala

**Upit prirodnim jezikom**:
> "Pokaži mi top 10 proizvoda po prihodima za moju trgovinu u četvrtom kvartalu 2024."

**Što se događa**:
1. VS Code AI Chat šalje upit MCP serveru
2. MCP server prepoznaje kontekst trgovine Sarah (Seattle)
3. RLS pravila filtriraju podatke samo za trgovinu Seattle
4. Generira se i izvršava SQL upit
5. Rezultati se formatiraju i vraćaju AI Chatu
6. AI pruža analizu i uvide

### Scenarij 2: Otkrivanje proizvoda s semantičkim pretraživanjem

**Korisnik**: Mike, voditelj zaliha  
**Cilj**: Pronaći proizvode slične zahtjevu kupca

**Upit prirodnim jezikom**:
> "Koje proizvode prodajemo slične 'vodootpornim električnim konektorima za vanjsku upotrebu'?"

**Što se događa**:
1. Upit obrađuje alat za semantičko pretraživanje
2. Azure OpenAI generira vektorski prikaz
3. pgvector izvršava pretraživanje po sličnosti
4. Povezani proizvodi rangiraju se po relevantnosti
5. Rezultati uključuju detalje i dostupnost proizvoda
6. AI predlaže alternative i mogućnosti pakiranja

### Scenarij 3: Analitika preko više trgovina

**Korisnik**: Jennifer, regionalna menadžerica  
**Cilj**: Usporediti performanse svih trgovina

**Upit prirodnim jezikom**:
> "Usporedi prodaju po kategorijama za sve trgovine u zadnjih 6 mjeseci"

**Što se događa**:
1. RLS kontekst postavlja se za pristup regionalne menadžerice
2. Generira se složeni upit za više trgovina
3. Podaci se agregiraju preko lokacija trgovina
4. Rezultati uključuju trendove i usporedbe
5. AI identificira uvide i preporuke

## 🔒 Detaljni pregled sigurnosti i višekorisničkog pristupa

Naša implementacija stavlja naglasak na sigurnost razine enterprise:

### Row Level Security (RLS)

PostgreSQL RLS osigurava izolaciju podataka:

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

### Upravljanje identitetom korisnika

Svaka MCP veza uključuje:
- **ID voditelja trgovine**: Jedinstveni identifikator za RLS kontekst
- **Dodjela uloga**: Dozvole i razine pristupa
- **Upravljanje sesijom**: Sigurnosni tokeni za autentifikaciju
- **Audit zapisivanje**: Potpuna povijest pristupa

### Zaštita podataka

Višeslojna sigurnost:
- **Šifriranje veza**: TLS za sve veze prema bazi podataka
- **Prevencija SQL injekcija**: Isključivo parametarski upiti
- **Validacija unosa**: Sveobuhvatna validacija zahtjeva
- **Upravljanje pogreškama**: Bez osjetljivih podataka u porukama greške

## 🎯 Ključni zaključci

Nakon završetka ovog uvoda trebali biste razumjeti:

✅ **Vrijednost MCP-a**: Kako MCP povezuje AI asistente i stvarne podatke  
✅ **Poslovni kontekst**: Zahtjeve i izazove Zava Retaila  
✅ **Pregled arhitekture**: Ključne komponente i njihove interakcije  
✅ **Tehnološki paket**: Alate i okvire korištene kroz cijeli put  
✅ **Sigurnosni model**: Višekorisnički pristup podacima i zaštita  
✅ **Obrasci korištenja**: Stvarni scenariji upita i radnih tijekova  

## 🚀 Što slijedi

Spremni za dublje uranjanje? Nastavite s:

**[Laboratorij 01: Osnovni pojmovi arhitekture](../01-Architecture/README.md)**

Naučite o MCP arhitektonskim obrascima servera, principima dizajna baza podataka i detaljnoj tehničkoj implementaciji koja pokreće naše maloprodajne analitičke rješenje.

## 📚 Dodatni resursi

### MCP dokumentacija
- [MCP specifikacija](https://modelcontextprotocol.io/docs/) - Službena dokumentacija protokola
- [MCP za početnike](https://aka.ms/mcp-for-beginners) - Sveobuhvatan vodič za učenje MCP-a
- [FastMCP dokumentacija](https://github.com/modelcontextprotocol/python-sdk) - Dokumentacija Python SDK-a

### Integracija baze podataka
- [PostgreSQL dokumentacija](https://www.postgresql.org/docs/) - Kompletna referenca PostgreSQL-a
- [pgvector vodič](https://github.com/pgvector/pgvector) - Dokumentacija za vektorski dodatak
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Vodič za PostgreSQL RLS

### Azure usluge
- [Azure OpenAI dokumentacija](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integracija AI usluga
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Upravljačka baza podataka
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Bezbrižni kontejneri

---

**Odricanje od odgovornosti**: Ovo je vježba učenja koja koristi fiktivne maloprodajne podatke. Uvijek slijedite politike upravljanja podacima i sigurnosti vaše organizacije prilikom implementacije sličnih rješenja u produkcijskim okruženjima.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->