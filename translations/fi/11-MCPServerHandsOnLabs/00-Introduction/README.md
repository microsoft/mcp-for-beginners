# Johdanto MCP-tietokantaintegraatioon

> [!NOTE]
> Tämän oppimispolun kaaviot tai koodi, jotka käyttävät HTTP/SSE:tä tai alustamisvaihtoehtoja,
> heijastavat esimerkin MCP `2025-11-25` riippuvuuksia. Uusissa toteutuksissa käytä
> `2026-07-28` tilattomia pyyntöjä ja Streamable HTTP:tä.

## 🎯 Mitä tämä labra kattaa

Tämä johdantolabra tarjoaa kattavan yleiskatsauksen Model Context Protocol (MCP) -palvelinten rakentamisesta tietokantaintegraation kanssa. Ymmärrät liiketoiminnan taustan, teknisen arkkitehtuurin ja käytännön sovellukset Zava Retailin analytiikkatapausesimerkin kautta osoitteessa https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Yleiskatsaus

**Model Context Protocol (MCP)** mahdollistaa tekoälyavustajien turvallisen pääsyn ja vuorovaikutuksen ulkoisten tietolähteiden kanssa reaaliajassa. Yhdistettynä tietokantaintegraatioon MCP avaa tehokkaita mahdollisuuksia datavetoisille tekoälysovelluksille.

Tämä oppimispolku opettaa sinut rakentamaan tuotantovalmiita MCP-palvelimia, jotka yhdistävät tekoälyavustajat vähittäiskaupan myyntitietoihin PostgreSQL:n kautta toteuttaen yritysratkaisuja, kuten rivitason suojaus, semanttinen haku ja monivuokraajainen datan käyttö.

## Oppimistavoitteet

Tämän labran lopuksi osaat:

- **Määritellä** Model Context Protocolin ja sen keskeiset hyödyt tietokantaintegraatiossa
- **Tunnistaa** MCP-palvelinarkkitehtuurin keskeiset komponentit tietokantojen kanssa
- **Ymmärtää** Zava Retailin käyttötapauksen ja sen liiketoiminnalliset vaatimukset
- **Tunnistaa** yrityksen mallit turvalliseen ja skaalautuvaan tietokantakäyttöön
- **Luetella** tämän oppimispolun käyttämät työkalut ja teknologiat

## 🧭 Haaste: Tekoäly kohtaa todellisuuden tiedot

### Perinteiset tekoälyn rajoitukset

Nykyaikaiset tekoälyavustajat ovat erittäin tehokkaita, mutta kohtaavat merkittäviä rajoituksia työskennellessään todellisen maailman liiketoimintadatan kanssa:

| **Haaste** | **Kuvaus** | **Liiketoiminnan vaikutus** |
|---------------|-----------------|-------------------|
| **Staattinen tieto** | Tekoälymallit, jotka on koulutettu kiinteillä aineistoilla, eivät pääse käsiksi ajantasaisiin tietoihin | Vanhentuneet havainnot, menetetyt mahdollisuudet |
| **Datasaarekkeet** | Tieto lukittuna tietokantoihin, rajapintoihin ja järjestelmiin, joihin tekoäly ei pääse | Epätäydelliset analyysit, pirstaloituneet työnkulut |
| **Turvavaatimukset** | Suora tietokantayhteys aiheuttaa turvallisuus- ja vaatimustenmukaisuushuolia | Rajoitettu käyttöönotto, manuaalinen datan valmistelu |
| **Monimutkaiset kyselyt** | Liiketoimintakäyttäjien tulee hallita teknistä osaamista tiedon louhintaan | Heikentynyt käyttöönotto, tehottomat prosessit |

### MCP-ratkaisu

Model Context Protocol vastaa näihin haasteisiin tarjoamalla:

- **Reaaliaikainen datan käyttö**: Tekoälyavustajat voivat kysellä suoria tietokantoja ja rajapintoja
- **Turvallinen integraatio**: Hallittu pääsy autentikoinnilla ja käyttöoikeuksilla
- **Luonnollisen kielen käyttöliittymä**: Liiketoimintakäyttäjät voivat esittää kysymyksiä tavallisella englannilla
- **Standardoitu protokolla**: Toimii eri tekoälyalustojen ja työkalujen välillä

## 🏪 Tapaa Zava Retail: Oppimistapaus https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Tämän oppimispolun aikana rakennamme MCP-palvelimen **Zava Retail** -nimiselle kuvitteelliselle tee-se-itse-vähittäisketjulle, jolla on useita myymälöitä. Tämä realistinen skenaario havainnollistaa yritystason MCP-toteutusta.

### Liiketoimintaympäristö

**Zava Retail** toimii:
- **8 fyysisessä myymälässä** Washingtonin osavaltiossa (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 verkkokaupassa** sähköisen kaupankäynnin myyntiin
- **Monipuolisessa tuotekatalogissa**, joka sisältää työkaluja, rautatarvikkeita, puutarhatarvikkeita ja rakennusmateriaaleja
- **Monitasoisessa johdossa** myymäläpäälliköistä aluepäälliköihin ja johtajiin

### Liiketoimintavaatimukset

Myymäläpäälliköt ja johtajat tarvitsevat tekoälypohjaista analytiikkaa seuraaviin tehtäviin:

1. **Analysoida myyntisuorituskykyä** myymälöittäin ja ajanjaksoittain
2. **Seurata varastotasoja** ja tunnistaa täydennystarpeet
3. **Ymmärtää asiakaskäyttäytymistä** ja ostomalleja
4. **Löytää tuotehavaintoja** semanttisen haun avulla
5. **Tuottaa raportteja** luonnollisen kielen kyselyillä
6. **Ylläpitää tietoturvaa** roolipohjaisella pääsynhallinnalla

### Teknisiä vaatimuksia

MCP-palvelimen on tarjottava:

- **Monivuokraajainen datan käyttö**, jossa myymäläpäälliköt näkevät vain oman myymälänsä tiedot
- **Joustavat kyselymahdollisuudet**, jotka tukevat monimutkaisia SQL-operaatioita
- **Semanttinen haku** tuotehavaintoon ja suosituksiin
- **Reaaliaikainen data**, joka heijastaa nykyistä liiketoimintatilannetta
- **Turvallinen autentikointi** rivitason suojauksella
- **Skaalautuva arkkitehtuuri**, joka tukee useita samanaikaisia käyttäjiä

## 🏗️ MCP-palvelimen arkkitehtuurin yleiskuva

MCP-palvelimemme toteuttaa kerrosrakenteen, joka on optimoitu tietokantaintegraatiota varten:

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

### Keskeiset komponentit

#### **1. MCP-palvelinkerros**
- **FastMCP Framework**: Moderni Python-pohjainen MCP-palvelinimplementaatio
- **Työkalujen rekisteröinti**: Deklaratiiviset työkalumääritelmät tyyppiturvallisuudella
- **Pyyntöyhteys**: Käyttäjäidentiteetin ja istunnon hallinta
- **Virheenkäsittely**: Vankka virheiden hallinta ja lokitus

#### **2. Tietokantaintegraatiokerros**
- **Yhteysaltaan hallinta**: Tehokas asyncpg-yhteyksien hallinta
- **Skeeman tarjoaja**: Dynaaminen taulun skeeman tunnistus
- **Kyselyjen suorittaja**: Turvallinen SQL:n suoritus RLS-kontekstissa
- **Transaktioiden hallinta**: ACID-vaatimustenmukaisuus ja peruutusten käsittely

#### **3. Turvakerros**
- **Rivitason suojaus (RLS)**: PostgreSQL:n RLS monivuokraajaisen datan eristämiseen
- **Käyttäjäidentiteetti**: Myymäläpäällikön autentikointi ja valtuutus
- **Käyttöoikeuksien hallinta**: Tarkoin määritellyt oikeudet ja auditointilokit
- **Syötteen validointi**: SQL-injektioiden esto ja kyselyjen validointi

#### **4. Tekoälyä parantava kerros**
- **Semanttinen haku**: Vektoriesitykset tuotehavaintoon
- **Azure OpenAI -integraatio**: Tekstiembeddingien generointi
- **Samanlaisuusalgoritmit**: pgvector kosinisen samankaltaisuuden haku
- **Haun optimointi**: Indeksointi ja suorituskyvyn viritys

## 🔧 Teknologiapino

### Ydinteknologiat

| **Komponentti** | **Teknologia** | **Tarkoitus** |
|---------------|----------------|-------------|
| **MCP-kehys** | FastMCP (Python) | Moderni MCP-palvelinimplementaatio |
| **Tietokanta** | PostgreSQL 17 + pgvector | Relaatiotietokanta vektoriahulla |
| **Tekoälypalvelut** | Azure OpenAI | Tekstiembeddingit ja kielimallit |
| **Konttiteknologia** | Docker + Docker Compose | Kehitysympäristö |
| **Pilvialustat** | Microsoft Azure | Tuotantoympäristö |
| **IDE-integraatio** | VS Code | Tekoälychat ja kehitysprosessi |

### Kehitystyökalut

| **Työkalu** | **Tarkoitus** |
|----------|-------------|
| **asyncpg** | Suorituskykyinen PostgreSQL-kirjasto |
| **Pydantic** | Datan validointi ja serialisointi |
| **Azure SDK** | Pilvipalveluintegrointi |
| **pytest** | Testauskehys |
| **Docker** | Kontittaminen ja käyttöönotto |

### Tuotantopino

| **Palvelu** | **Azure-resurssi** | **Tarkoitus** |
|-------------|-------------------|-------------|
| **Tietokanta** | Azure Database for PostgreSQL | Hallittu tietokantapalvelu |
| **Kontti** | Azure Container Apps | Serverless-konttien hosting |
| **Tekoälypalvelut** | Microsoft Foundry | OpenAI-mallit ja -rajapinnat |
| **Seuranta** | Application Insights | Havainnointi ja diagnostiikka |
| **Turvallisuus** | Azure Key Vault | Salaisuuksien ja konfiguraation hallinta |

## 🎬 Käytännön käyttötapaukset

Tutkitaan, miten eri käyttäjät käyttävät MCP-palvelintamme:

### Skenaario 1: Myymäläpäällikön suorituskyvyn tarkastelu

**Käyttäjä**: Sarah, Seattlen myymäläpäällikkö  
**Tavoite**: Analysoida viimeisen vuosineljänneksen myynti

**Luonnollisen kielen kysely**:
> "Näytä myymäläni top 10 tuotetta liikevaihdon mukaan Q4 2024"

**Mitä tapahtuu**:
1. VS Code AI Chat lähettää kyselyn MCP-palvelimelle
2. MCP-palvelin tunnistaa Sarah'n myymäläyhteyden (Seattle)
3. RLS-politiikat suodattavat datan vain Seattle-myymälään
4. SQL-kysely generoidaan ja suoritetaan
5. Tulokset muotoillaan ja lähetetään AI Chatille
6. Tekoäly tarjoaa analyysit ja oivallukset

### Skenaario 2: Tuotehaku semanttisen haun avulla

**Käyttäjä**: Mike, Varastopäällikkö  
**Tavoite**: Löytää asiakkaan pyynnöstä samankaltaisia tuotteita

**Luonnollisen kielen kysely**:
> "Mitä tuotteita myymme, jotka ovat samanlaisia kuin 'vedenkestävät ulkokäyttöön tarkoitetut sähkörasiat'?"

**Mitä tapahtuu**:
1. Kysely käsitellään semanttisen haun työkalulla
2. Azure OpenAI generoi vektoriesityksen
3. pgvector suorittaa samankaltaisuushaku
4. Samankaltaiset tuotteet järjestetään relevanssin mukaan
5. Tulokset sisältävät tuotetiedot ja saatavuuden
6. Tekoäly ehdottaa vaihtoehtoja ja paketoimismahdollisuuksia

### Skenaario 3: Usean myymälän analytiikka

**Käyttäjä**: Jennifer, Aluepäällikkö  
**Tavoite**: Verrata suorituskykyä kaikissa myymälöissä

**Luonnollisen kielen kysely**:
> "Vertaile myyntiä kategorioittain kaikissa myymälöissä viimeisen 6 kuukauden aikana"

**Mitä tapahtuu**:
1. RLS-konteksti asetetaan aluepäällikön käyttöoikeuksilla
2. Monimutkainen usean myymälän kysely luodaan
3. Data yhdistellään eri myymäläsijainneista
4. Tulokset sisältävät trendit ja vertailut
5. Tekoäly tunnistaa oivallukset ja suositukset

## 🔒 Turvallisuus ja monivuokraajaisuus syvemmässä tarkastelussa

Toteutuksemme painottaa yritystason turvallisuutta:

### Rivikohtainen suojaus (RLS)

PostgreSQL:n RLS varmistaa datan eristyksen:

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

### Käyttäjäidentiteetin hallinta

Jokainen MCP-yhteys sisältää:
- **Myymäläpäällikön tunniste**: Yksilöllinen tunniste RLS-kontekstille
- **Roolin määrittely**: Käyttöoikeudet ja pääsytasot
- **Istunnon hallinta**: Turvalliset autentikointitunnukset
- **Auditointilokitus**: Täydellinen pääsyloki

### Datan suojaus

Useita suojakerroksia:
- **Yhteyden salaus**: TLS kaikissa tietokantayhteyksissä
- **SQL-injektion esto**: Vain parametrisoidut kyselyt
- **Syötteen validointi**: Laaja pyyntöjen validointi
- **Virheenkäsittely**: Ei arkaluonteista dataa virheilmoituksissa

## 🎯 Keskeiset opit

Johdannon suorittamisen jälkeen sinun tulisi ymmärtää:

✅ **MCP:n arvolupaus**: Miten MCP yhdistää tekoälyavustajat ja todellisuuden data  
✅ **Liiketoimintaympäristö**: Zava Retailin vaatimukset ja haasteet  
✅ **Arkkitehtuurin yleiskuva**: Keskeiset komponentit ja niiden vuorovaikutus  
✅ **Teknologiapino**: Tämän oppimispolun työkalut ja kehykset  
✅ **Turvamalli**: Monivuokraajainen datan käyttö ja suojaus  
✅ **Käyttömallit**: Käytännön kyselytilanteet ja työnkulut  

## 🚀 Mitä seuraavaksi

Valmiina sukeltamaan syvemmälle? Jatka:

**[Lab 01: Ydinarkkitehtuurin käsitteet](../01-Architecture/README.md)**

Opi MCP-palvelinarkkitehtuurin malleista, tietokantojen suunnitteluperiaatteista ja yksityiskohtaisesta teknisestä toteutuksesta, joka pyörittää vähittäiskaupan analytiikkaratkaisuamme.

## 📚 Lisäresurssit

### MCP-dokumentaatio
- [MCP-määritys](https://modelcontextprotocol.io/docs/) - Virallinen protokolladokumentaatio
- [MCP aloittelijoille](https://aka.ms/mcp-for-beginners) - Kattava MCP-opas
- [FastMCP-dokumentaatio](https://github.com/modelcontextprotocol/python-sdk) - Python SDK -dokumentaatio

### Tietokantaintegraatio
- [PostgreSQL-dokumentaatio](https://www.postgresql.org/docs/) - Täydellinen PostgreSQL-viite
- [pgvector-opas](https://github.com/pgvector/pgvector) - Vektori-laajennuksen dokumentaatio
- [Rivitason suojaus](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL:n RLS-opas

### Azure-palvelut
- [Azure OpenAI-dokumentaatio](https://docs.microsoft.com/azure/cognitive-services/openai/) - Tekoälypalvelujen integrointi
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Hallittu tietokantapalvelu
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless-kontit

---

**Vastuuvapauslauseke**: Tämä on oppimisharjoitus, jossa käytetään kuvitteellista vähittäistietoa. Noudata aina organisaatiosi tietohallinta- ja turvallisuusohjeita toteuttaessasi vastaavia ratkaisuja tuotantoympäristössä.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->