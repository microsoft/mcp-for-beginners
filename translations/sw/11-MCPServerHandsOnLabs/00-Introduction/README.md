# Utangulizi wa Muunganisho wa Hifadhidata ya MCP

## 🎯 Yaliyomo Katika Maabara Hii

Maabara hii ya utangulizi inatoa muhtasari wa kina wa jinsi ya kujenga seva za Model Context Protocol (MCP) zilizounganishwa na hifadhidata. Utajifunza kuhusu kesi ya kibiashara, usanifu wa kiufundi, na matumizi halisi kupitia mfano wa uchanganuzi wa Zava Retail kwenye https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Muhtasari

**Model Context Protocol (MCP)** inawezesha wasaidizi wa AI kufikia na kuingiliana na vyanzo vya data vya nje kwa usalama na kwa muda halisi. Ikichanganywa na muunganisho wa hifadhidata, MCP hufungua uwezo mkubwa kwa programu za AI zinazotegemea data.

Njia hii ya kujifunza inakufundisha jinsi ya kujenga seva za MCP zilizo tayari kwa uzalishaji ambazo zinaunganisha wasaidizi wa AI na data ya mauzo ya rejareja kupitia PostgreSQL, kwa kutumia mifumo ya biashara kama Usalama wa Kiwango cha Safu (Row Level Security), utafutaji wa semantiki, na ufikiaji wa data wa wateja wengi.

## Malengo ya Kujifunza

Mwisho wa maabara hii, utaweza:

- **Kuelezea** Model Context Protocol na faida zake kuu kwa muunganisho wa hifadhidata  
- **Kutambua** vipengele muhimu vya usanifu wa seva ya MCP na hifadhidata  
- **Kuelewa** kesi ya matumizi ya Zava Retail na mahitaji yake ya kibiashara  
- **Kutambua** mifumo ya biashara kwa ufikiaji wa hifadhidata salama na inayoweza kupanuka  
- **Kuweka orodha** ya zana na teknolojia zinazotumika katika njia hii ya kujifunza  

## 🧭 Changamoto: AI Kukutana na Data Halisi ya Kibiashara

### Mapungufu ya Kawaida ya AI

Wasaidizi wa kisasa wa AI wana nguvu sana lakini wanakabiliwa na changamoto kubwa wanapofanya kazi na data halisi ya kibiashara:

| **Changamoto** | **Maelezo** | **Athari za Kibiashara** |
|----------------|-------------|--------------------------|
| **Maarifa ya Kawaida** | Miundo ya AI iliyofunzwa kwenye seti za data zisizobadilika haiwezi kufikia data ya sasa ya kibiashara | Maarifa yaliyopitwa na wakati, fursa zilizokosa |
| **Vizuizi vya Data** | Taarifa zilizofungwa kwenye hifadhidata, API, na mifumo ambayo AI haiwezi kufikia | Uchambuzi usio kamili, mtiririko wa kazi ulio na mapengo |
| **Vizuizi vya Usalama** | Ufikiaji wa moja kwa moja wa hifadhidata huleta wasiwasi wa usalama na uzingatiaji | Utekelezaji mdogo, maandalizi ya data ya mwongozo |
| **Maswali Magumu** | Watumiaji wa biashara wanahitaji ujuzi wa kiufundi ili kutoa maarifa ya data | Kupungua kwa matumizi, michakato isiyo na ufanisi |

### Suluhisho la MCP

Model Context Protocol inashughulikia changamoto hizi kwa kutoa:

- **Ufikiaji wa Data wa Muda Halisi**: Wasaidizi wa AI huuliza hifadhidata na API moja kwa moja  
- **Muunganisho Salama**: Ufikiaji unaodhibitiwa na uthibitishaji na ruhusa  
- **Kiolesura cha Lugha Asilia**: Watumiaji wa biashara huuliza maswali kwa Kiingereza rahisi  
- **Itifaki Iliyosanifishwa**: Inafanya kazi kwenye majukwaa na zana tofauti za AI  

## 🏪 Kutana na Zava Retail: Kesi Yetu ya Kujifunza https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Katika njia hii ya kujifunza, tutajenga seva ya MCP kwa **Zava Retail**, mnyororo wa rejareja wa DIY wa kubuniwa wenye maeneo mengi ya maduka. Hali hii halisi inaonyesha utekelezaji wa MCP wa kiwango cha biashara.

### Muktadha wa Kibiashara

**Zava Retail** inaendesha:
- **Maduka 8 ya kimwili** katika jimbo la Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)  
- **Duka 1 la mtandaoni** kwa mauzo ya e-commerce  
- **Katalogi ya bidhaa mbalimbali** ikijumuisha zana, vifaa vya ujenzi, vifaa vya bustani, na vifaa vya ujenzi  
- **Usimamizi wa viwango vingi** na mameneja wa maduka, mameneja wa kanda, na watendaji  

### Mahitaji ya Kibiashara

Mameneja wa maduka na watendaji wanahitaji uchanganuzi unaotumia AI ili:

1. **Kuchambua utendaji wa mauzo** katika maduka na vipindi vya muda  
2. **Kufuatilia viwango vya hesabu** na kutambua mahitaji ya kuongeza bidhaa  
3. **Kuelewa tabia ya wateja** na mifumo ya ununuzi  
4. **Kugundua maarifa ya bidhaa** kupitia utafutaji wa semantiki  
5. **Kuzalisha ripoti** kwa maswali ya lugha asilia  
6. **Kudumisha usalama wa data** kwa udhibiti wa ufikiaji kulingana na majukumu  

### Mahitaji ya Kiufundi

Seva ya MCP inapaswa kutoa:

- **Ufikiaji wa data wa wateja wengi** ambapo mameneja wa maduka wanaona data ya maduka yao pekee  
- **Uwezo wa kuuliza maswali kwa urahisi** unaounga mkono operesheni ngumu za SQL  
- **Utafutaji wa semantiki** kwa ugunduzi wa bidhaa na mapendekezo  
- **Data ya muda halisi** inayoonyesha hali ya sasa ya biashara  
- **Uthibitishaji salama** na usalama wa kiwango cha safu (RLS)  
- **Usanifu unaoweza kupanuka** unaounga mkono watumiaji wengi kwa wakati mmoja  

## 🏗️ Muhtasari wa Usanifu wa Seva ya MCP

Seva yetu ya MCP inatekeleza usanifu wa tabaka ulioimarishwa kwa muunganisho wa hifadhidata:

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

### Vipengele Muhimu

#### **1. Tabaka la Seva ya MCP**
- **FastMCP Framework**: Utekelezaji wa kisasa wa seva ya MCP kwa Python  
- **Usajili wa Zana**: Ufafanuzi wa zana kwa njia ya tamko na usalama wa aina  
- **Muktadha wa Ombi**: Utambulisho wa mtumiaji na usimamizi wa kikao  
- **Ushughulikiaji wa Makosa**: Usimamizi wa makosa thabiti na ufuatiliaji  

#### **2. Tabaka la Muunganisho wa Hifadhidata**
- **Usimamizi wa Muunganisho**: Usimamizi wa muunganisho wa asyncpg kwa ufanisi  
- **Mtoa Schema**: Ugunduzi wa schema ya jedwali kwa njia ya nguvu  
- **Mtekelezaji wa Maswali**: Utekelezaji salama wa SQL na muktadha wa RLS  
- **Usimamizi wa Muamala**: Uzingatiaji wa ACID na usimamizi wa kurudisha nyuma  

#### **3. Tabaka la Usalama**
- **Usalama wa Kiwango cha Safu**: RLS ya PostgreSQL kwa kutenganisha data ya wateja wengi  
- **Utambulisho wa Mtumiaji**: Uthibitishaji na ruhusa za mameneja wa maduka  
- **Udhibiti wa Ufikiaji**: Ruhusa za kina na rekodi za ukaguzi  
- **Uthibitishaji wa Ingizo**: Kuzuia sindikizo la SQL na uthibitishaji wa maswali  

#### **4. Tabaka la Uboreshaji wa AI**
- **Utafutaji wa Semantiki**: Uwekaji wa vector kwa ugunduzi wa bidhaa  
- **Muunganisho wa Azure OpenAI**: Uzalishaji wa uwekaji wa maandishi  
- **Algorithimu za Ulinganisho**: Utafutaji wa ulinganisho wa cosine wa pgvector  
- **Uboreshaji wa Utafutaji**: Uwekaji wa faharasa na uboreshaji wa utendaji  

## 🔧 Teknolojia Zinazotumika

### Teknolojia za Msingi

| **Kipengele** | **Teknolojia** | **Madhumuni** |
|---------------|----------------|---------------|
| **MCP Framework** | FastMCP (Python) | Utekelezaji wa kisasa wa seva ya MCP |
| **Hifadhidata** | PostgreSQL 17 + pgvector | Data ya uhusiano na utafutaji wa vector |
| **Huduma za AI** | Azure OpenAI | Uwekaji wa maandishi na mifano ya lugha |
| **Uwekaji wa Kontena** | Docker + Docker Compose | Mazingira ya maendeleo |
| **Jukwaa la Wingu** | Microsoft Azure | Utekelezaji wa uzalishaji |
| **Muunganisho wa IDE** | VS Code | AI Chat na mtiririko wa kazi wa maendeleo |

### Zana za Maendeleo

| **Zana** | **Madhumuni** |
|----------|--------------|
| **asyncpg** | Dereva wa PostgreSQL wa utendaji wa juu |
| **Pydantic** | Uthibitishaji wa data na usawazishaji |
| **Azure SDK** | Muunganisho wa huduma za wingu |
| **pytest** | Mfumo wa majaribio |
| **Docker** | Uwekaji wa kontena na utekelezaji |

### Stack ya Uzalishaji

| **Huduma** | **Rasilimali ya Azure** | **Madhumuni** |
|------------|-------------------------|---------------|
| **Hifadhidata** | Azure Database for PostgreSQL | Huduma ya hifadhidata inayosimamiwa |
| **Kontena** | Azure Container Apps | Ukaribishaji wa kontena bila seva |
| **Huduma za AI** | Azure AI Foundry | Mifano ya OpenAI na ncha za mwisho |
| **Ufuatiliaji** | Application Insights | Ufuatiliaji na uchunguzi |
| **Usalama** | Azure Key Vault | Usiri na usimamizi wa usanidi |

## 🎬 Matumizi Halisi ya Kesi

Hebu tuchunguze jinsi watumiaji tofauti wanavyotumia seva yetu ya MCP:

### Kisa 1: Mapitio ya Utendaji wa Meneja wa Duka

**Mtumiaji**: Sarah, Meneja wa Duka la Seattle  
**Lengo**: Kuchambua utendaji wa mauzo ya robo ya mwisho

**Swali la Lugha Asilia**:  
> "Nionyeshe bidhaa 10 bora kwa mapato kwa duka langu katika robo ya nne ya 2024"

**Kinachotokea**:
1. VS Code AI Chat inatuma swali kwa seva ya MCP  
2. Seva ya MCP inatambua muktadha wa duka la Sarah (Seattle)  
3. Sera za RLS huchuja data kwa duka la Seattle pekee  
4. Swali la SQL linazalishwa na kutekelezwa  
5. Matokeo yanapangwa na kurudishwa kwa AI Chat  
6. AI inatoa uchanganuzi na maarifa  

### Kisa 2: Ugunduzi wa Bidhaa kwa Utafutaji wa Semantiki

**Mtumiaji**: Mike, Meneja wa Hesabu  
**Lengo**: Kupata bidhaa zinazofanana na ombi la mteja

**Swali la Lugha Asilia**:  
> "Ni bidhaa gani tunazouza zinazofanana na 'viunganishi vya umeme visivyo na maji kwa matumizi ya nje'?"

**Kinachotokea**:
1. Swali linashughulikiwa na zana ya utafutaji wa semantiki  
2. Azure OpenAI inazalisha vector ya uwekaji  
3. pgvector inafanya utafutaji wa ulinganisho  
4. Bidhaa zinazohusiana zinapangwa kulingana na umuhimu  
5. Matokeo yanajumuisha maelezo ya bidhaa na upatikanaji  
6. AI inapendekeza mbadala na fursa za kuunganisha bidhaa  

### Kisa 3: Uchambuzi wa Maduka Mbalimbali

**Mtumiaji**: Jennifer, Meneja wa Kanda  
**Lengo**: Kulinganisha utendaji katika maduka yote

**Swali la Lugha Asilia**:  
> "Linganisha mauzo kwa kategoria kwa maduka yote katika miezi 6 iliyopita"

**Kinachotokea**:
1. Muktadha wa RLS unasanidiwa kwa ufikiaji wa meneja wa kanda  
2. Swali ngumu la maduka mengi linazalishwa  
3. Data inakusanywa katika maeneo ya maduka  
4. Matokeo yanajumuisha mitindo na kulinganisha  
5. AI inatambua maarifa na mapendekezo  

## 🔒 Uchambuzi wa Usalama na Ufikiaji wa Wateja Wengi

Utekelezaji wetu unazingatia usalama wa kiwango cha biashara:

### Usalama wa Kiwango cha Safu (RLS)

RLS ya PostgreSQL inahakikisha kutenganisha data:

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

### Usimamizi wa Utambulisho wa Mtumiaji

Kila muunganisho wa MCP unajumuisha:
- **Kitambulisho cha Meneja wa Duka**: Kitambulisho cha kipekee kwa muktadha wa RLS  
- **Uteuzi wa Majukumu**: Ruhusa na viwango vya ufikiaji  
- **Usimamizi wa Kikao**: Tokeni za uthibitishaji salama  
- **Ufuatiliaji wa Ukaguzi**: Historia kamili ya ufikiaji  

### Ulinzi wa Data

Tabaka nyingi za usalama:
- **Usimbaji wa Muunganisho**: TLS kwa muunganisho wote wa hifadhidata  
- **Kuzuia Sindikizo la SQL**: Maswali yaliyo na vigezo pekee  
- **Uthibitishaji wa Ingizo**: Uthibitishaji wa maombi kwa kina  
- **Ushughulikiaji wa Makosa**: Hakuna data nyeti katika ujumbe wa makosa  

## 🎯 Mambo Muhimu ya Kujifunza

Baada ya kukamilisha utangulizi huu, unapaswa kuelewa:

✅ **Thamani ya MCP**: Jinsi MCP inavyounganisha wasaidizi wa AI na data halisi  
✅ **Muktadha wa Kibiashara**: Mahitaji na changamoto za Zava Retail  
✅ **Muhtasari wa Usanifu**: Vipengele muhimu na mwingiliano wake  
✅ **Teknolojia Zinazotumika**: Zana na mifumo inayotumika  
✅ **Mfumo wa Usalama**: Ufikiaji wa data wa wateja wengi na ulinzi  
✅ **Mifumo ya Matumizi**: Kesi halisi za maswali na mtiririko wa kazi  

## 🚀 Hatua Inayofuata

Tayari kuendelea? Endelea na:

**[Maabara 01: Dhana za Msingi za Usanifu](../01-Architecture/README.md)**

Jifunze kuhusu mifumo ya usanifu wa seva ya MCP, kanuni za muundo wa hifadhidata, na utekelezaji wa kiufundi wa kina unaoendesha suluhisho letu la uchanganuzi wa rejareja.

## 📚 Rasilimali za Ziada

### Nyaraka za MCP
- [MCP Specification](https://modelcontextprotocol.io/docs/) - Nyaraka rasmi za itifaki  
- [MCP for Beginners](https://aka.ms/mcp-for-beginners) - Mwongozo wa kujifunza MCP kwa kina  
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk) - Nyaraka za SDK ya Python  

### Muunganisho wa Hifadhidata
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - Marejeleo kamili ya PostgreSQL  
- [pgvector Guide](https://github.com/pgvector/pgvector) - Nyaraka za kiendelezi cha vector  
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Mwongozo wa RLS wa PostgreSQL  

### Huduma za Azure
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - Muunganisho wa huduma za AI  
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Huduma ya hifadhidata inayosimamiwa  
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontena bila seva  

---

**Kanusho**: Hii ni zoezi la kujifunza linalotumia data ya rejareja ya kubuniwa. Daima fuata sera za usimamizi wa data na usalama za shirika lako unapotekeleza suluhisho kama hili katika mazingira ya uzalishaji.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.