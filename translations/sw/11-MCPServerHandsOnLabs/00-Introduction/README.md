# Utangulizi wa Uunganisho wa Hifadhidata wa MCP

> [!NOTE]
> Michoro au nambari katika njia hii ya kujifunza inayotumia HTTP/SSE au chaguzi za
> uanzishaji zinaonyesha utegemezi wa sampuli ya MCP `2025-11-25`. Kwa utekelezaji mpya,
> tumia ombi zisizo na hali ya `2026-07-28` na HTTP Inayoweza Kutiririsha.

## 🎯 Kinachofunikwa na Maabara Hii

Maabara hii ya utangulizi inatoa muhtasari mpana wa kujenga seva za Model Context Protocol (MCP) zenye uunganisho wa hifadhidata. Utaelewa kesi ya biashara, usanifu wa kiufundi, na matumizi halisi kupitia kesi ya uchambuzi ya Zava Retail katika https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Muhtasari

**Model Context Protocol (MCP)** inaruhusu wasaidizi wa AI kufikia na kuingiliana kwa usalama na vyanzo vya data vya nje kwa wakati halisi. Iwapo itachanganywa na uunganisho wa hifadhidata, MCP hutoa uwezo mkubwa kwa matumizi ya AI yanayotegemea data.

Njia hii ya kujifunza inakufundisha kujenga seva za MCP tayari kwa uzalishaji ambazo zinaunganisha wasaidizi wa AI na data za mauzo ya rejareja kupitia PostgreSQL, zikitekeleza mifumo ya biashara kama Usalama wa Ngazi ya Safu (Row Level Security), utafutaji wa maana, na upatikanaji wa data kwa wateja mbalimbali.

## Malengo ya Kujifunza

Mwisho wa maabara hii, utaweza:

- **Fafanua** Model Context Protocol na faida zake kuu kwa uunganisho wa hifadhidata
- **Tambua** vipengele muhimu vya usanifu wa seva ya MCP na hifadhidata
- **Elewa** kesi ya matumizi ya Zava Retail na mahitaji yake ya kibiashara
- **Tambua** mifumo ya biashara kwa upatikanaji wa hifadhidata wenye usalama na kupanuka
- **Orodhesha** zana na teknolojia zinazotumika katika njia hii ya kujifunza

## 🧭 Changamoto: AI Inakutana na Data Halisi

### Vizingiti vya AI vya Kawaida

Madai ya kisasa ya wasaidizi wa AI ni makubwa lakini wanakutana na vizingiti vikubwa wanaposhughulikia data halisi za biashara:

| **Changamoto** | **Maelezo** | **Madhara ya Biashara** |
|---------------|-----------------|-------------------|
| **Maarifa Yasiyotegemeza Mabadiliko** | Mifano ya AI iliyofundishwa kwa seti za data zisizobadilika haiwezi kufikia data za hivi sasa za biashara | Maarifa ya zamani, fursa zilizoachwa nyuma |
| **Hifadhidata Zilizozezewa** | Taarifa zilizofungwa katika hifadhidata, API, na mifumo AI haiwezi kufikia | Uchambuzi usio kamilifu, kazi za mkono zilizogawanyika |
| **Vizuiwa vya Usalama** | Ufikiaji wa moja kwa moja wa hifadhidata huleta wasiwasi wa usalama na utimilifu | Uwekaji wa mipaka, maandalizi ya data ya mikono |
| **Maswali Magumu** | Watumiaji wa biashara wanahitaji maarifa ya kiufundi kutambua maarifa ya data | Kupungua kwa matumizi, michakato isiyofaa |

### Suluhisho la MCP

Model Context Protocol inaondoa changamoto hizi kwa kutoa:

- **Ufikiaji wa Data kwa Wakati Halisi**: Wasaidizi wa AI hufanya maswali kwenye hifadhidata na API za moja kwa moja
- **Uunganisho wa Usalama**: Ufikiaji wa kudhibitiwa kwa uthibitisho na vibali
- **Kiolesura cha Lugha Asili**: Watumiaji wa biashara huuliza maswali kwa Kiingereza rahisi
- **Itifaki Sanifu**: Inafanya kazi kwenye majukwaa na zana mbalimbali za AI

## 🏪 Kutana na Zava Retail: Kesi Yetu ya Kujifunza https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Katika njia hii ya kujifunza, tutajenga seva ya MCP kwa **Zava Retail**, mnyororo wa rejareja wa DIY wa kubuniwa ambao una maeneo mengi ya duka. Hali halisi hii inaonyesha utekelezaji wa kiwango cha biashara cha MCP.

### Muktadha wa Biashara

**Zava Retail** inafanya kazi:
- **Maduka 8 ya mwili** katika jimbo la Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **Duka 1 la mtandaoni** kwa mauzo ya e-commerce
- **Orodha ya bidhaa mbalimbali** ikiwa ni pamoja na zana, vifaa, vifaa vya bustani, na vifaa vya ujenzi
- **Usimamizi wa ngazi nyingi** na wasimamizi wa duka, wasimamizi wa mikoa, na wakurugenzi

### Mahitaji ya Biashara

Wasimamizi wa duka na wakurugenzi wanahitaji uchambuzi unaotumia AI ili:

1. **Kuchambua utendaji wa mauzo** katika maduka na vipindi vya muda
2. **Kufuata viwango vya hesabu** na kubaini mahitaji ya upya bidhaa
3. **Kuelewa tabia za wateja** na mifumo ya ununuzi
4. **Gundua maarifa ya bidhaa** kupitia utafutaji wa maana
5. **Tengeneza ripoti** kwa maswali ya lugha asilia
6. **Dumisha usalama wa data** kwa udhibiti wa upatikanaji wa majukumu

### Mahitaji ya Kiufundi

Seva ya MCP lazima itoe:

- **Upatikanaji wa data kwa wateja wengi** ambapo wasimamizi wa duka wanaona data za duka lao pekee
- **Uwezo wa maswali yenye kubadilika** kuunga mkono shughuli ngumu za SQL
- **Utafutaji wa maana** kwa ugunduzi wa bidhaa na mapendekezo
- **Data ya wakati halisi** inayoakisi hali halisi ya biashara
- **Uthibitishaji salama** pamoja na usalama wa ngazi ya safu
- **Usanifu unaoweza kupanuka** unaomkubali mtumiaji wengi kwa wakati mmoja

## 🏗️ Muhtasari wa Usanifu wa Seva ya MCP

Seva yetu ya MCP inatekeleza usanifu wa tabaka ulioboreshwa kwa uunganisho wa hifadhidata:

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
- **Mfumo wa FastMCP**: Utekelezaji wa seva ya MCP ya kisasa kwa Python
- **Usajili wa Zana**: Maelezo ya zana kwa njia ya tamko yenye usalama wa aina
- **Muktadha wa Ombi**: Utambulisho wa mtumiaji na usimamizi wa kikao
- **Udhibiti wa Makosa**: Usimamizi imara wa makosa na uandishi wa kumbukumbu

#### **2. Tabaka la Uunganisho wa Hifadhidata**
- **Usimamizi wa Pool ya Muunganisho**: Usimamizi wa muunganisho wa asyncpg kwa ufanisi
- **Mtoaji wa Skima**: Ugunduzi wa skima ya meza kwa nguvu
- **Mtendaji wa Maswali**: Utekelezaji salama wa SQL kwa muktadha wa RLS
- **Usimamizi wa Muamala**: Utimilifu wa ACID na usimamizi wa kurudisha nyuma

#### **3. Tabaka la Usalama**
- **Usalama wa Ngazi ya Safu**: PostgreSQL RLS kwa kutenganisha data ya wengi
- **Utambulisho wa Mtumiaji**: Uthibitishaji na ruhusa za wasimamizi wa duka
- **Udhibiti wa Upatikanaji**: Vibali vyenye usahihi mkubwa na usisitizi wa rekodi
- **Uthibitishaji wa Ingizo**: Kuzuia sindano za SQL na uthibitishaji wa maswali

#### **4. Tabaka la Uboreshaji wa AI**
- **Utafutaji wa Maana**: Uingizaji wa vekta kwa ugunduzi wa bidhaa
- **Uunganisho wa Azure OpenAI**: Uundaji wa uingizaji wa maandishi
- **Algoriti za Ulinganifu**: Utafutaji wa ulinganifu wa cosini wa pgvector
- **Uboreshaji wa Utafutaji**: Uainishaji na usanidi wa utendaji

## 🔧 Stack ya Teknolojia

### Teknolojia Muhimu

| **Sehemu** | **Teknolojia** | **Madhumuni** |
|---------------|----------------|-------------|
| **Mfumo wa MCP** | FastMCP (Python) | Utekelezaji wa seva ya MCP wa kisasa |
| **Hifadhidata** | PostgreSQL 17 + pgvector | Data ya uhusiano na utafutaji wa vekta |
| **Huduma za AI** | Azure OpenAI | Uingizaji wa maandishi na mifano ya lugha |
| **Ufungashaji** | Docker + Docker Compose | Mazingira ya maendeleo |
| **Jukwaa la Wingu** | Microsoft Azure | Uwekaji uzalishaji |
| **Uunganisho wa IDE** | VS Code | Mazungumzo ya AI na mtiririko wa maendeleo |

### Zana za Maendeleo

| **Zana** | **Madhumuni** |
|----------|-------------|
| **asyncpg** | Dereva wa PostgreSQL yenye ufanisi wa juu |
| **Pydantic** | Uthibitishaji na serialization ya data |
| **Azure SDK** | Uunganisho wa huduma za wingu |
| **pytest** | Mfumo wa upimaji |
| **Docker** | Ufungashaji na uwekeaji |

### Stack ya Uzalishaji

| **Huduma** | **Rasilimali ya Azure** | **Madhumuni** |
|-------------|-------------------|-------------|
| **Hifadhidata** | Azure Database for PostgreSQL | Huduma ya hifadhidata inayosimamiwa |
| **Kontena** | Azure Container Apps | Uendeshaji wa kontena bila seva |
| **Huduma za AI** | Microsoft Foundry | Mifano na vituo vya OpenAI |
| **Ufuatiliaji** | Application Insights | Uwezo wa kuona na uchunguzi |
| **Usalama** | Azure Key Vault | Usimamizi wa siri na usanidi |

## 🎬 Matukio Halisi ya Matumizi

Tuchunguze jinsi watumiaji tofauti wanavyoshirikiana na seva yetu ya MCP:

### Tukio la 1: Ukaguzi wa Utendaji wa Msimamizi wa Duka

**Mtumiaji**: Sarah, Msimamizi wa Duka la Seattle  
**Lengo**: Kuchambua utendaji wa mauzo wa robo iliyopita

**Swali la Lugha Asilia**:
> "Nionyeshe bidhaa 10 za juu kwa mapato kwa duka langu katika Robo ya 4 ya 2024"

**Kinachotokea**:
1. Mazungumzo ya AI ya VS Code yanatuma swali kwa seva ya MCP
2. Seva ya MCP inatambua muktadha wa duka la Sarah (Seattle)
3. Sera za RLS zinachuja data kwa duka la Seattle pekee
4. Swali la SQL linatengenezwa na kutekelezwa
5. Matokeo yanapangwa na kurudiwa kwa Mazungumzo ya AI
6. AI hutoa uchambuzi na maarifa

### Tukio la 2: Ugunduzi wa Bidhaa kwa Utafutaji wa Maana

**Mtumiaji**: Mike, Msimamizi wa Hesabu  
**Lengo**: Kutafuta bidhaa zinazofanana na ombi la mteja

**Swali la Lugha Asilia**:
> "Ni bidhaa gani tunazouza zinazofanana na 'viunganishi wa umeme wa maji yanayostahimili matumizi ya nje'?"

**Kinachotokea**:
1. Swali linaendeshwa na zana ya utafutaji wa maana
2. Azure OpenAI hutengeneza wigo wa uingizaji
3. pgvector hufanya utafutaji wa ulinganifu
4. Bidhaa zinazohusiana zinapangwa kwa umuhimu
5. Matokeo yanajumuisha maelezo ya bidhaa na upatikanaji
6. AI inapendekeza mbadala na fursa za kuunganisha

### Tukio la 3: Uchambuzi wa Maduka Mengi

**Mtumiaji**: Jennifer, Msimamizi wa Mkoa  
**Lengo**: Kulinganisha utendaji katika maduka yote

**Swali la Lugha Asilia**:
> "Linganisheni mauzo kwa kategoria kwa maduka yote katika miezi 6 iliyopita"

**Kinachotokea**:
1. Muktadha wa RLS unawekwa kwa upatikanaji wa msimamizi wa mkoa
2. Swali tata la maduka mengi linatengenezwa
3. Data zinakusanywa kutoka maeneo ya maduka
4. Matokeo yanajumuisha mwenendo na kulinganisha
5. AI inatambua maarifa na mapendekezo

## 🔒 Usalama na Uchambuzi wa Multi-Tenancy

Utekelezaji wetu unazingatia usalama wa kiwango cha biashara:

### Usalama wa Ngazi ya Safu (RLS)

PostgreSQL RLS huhakikisha kutengwa kwa data:

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

Kila muunganisho wa MCP una:
- **Utambulisho wa Msimamizi wa Duka**: Kitambulisho cha kipekee kwa muktadha wa RLS
- **Uteuzi wa Nafasi**: Vibali na viwango vya upatikanaji
- **Usimamizi wa Kikao**: Tokeni salama za uthibitishaji
- **Kumbukumbu za Ukaguzi**: Historia kamili ya ufikiaji

### Ulinzi wa Data

Tabaka nyingi za usalama:
- **Usimbaji wa Muunganisho**: TLS kwa muunganisho wote wa hifadhidata
- **Kuzuia Sindano za SQL**: Maswali yenye vigezo tu
- **Uthibitishaji wa Ingizo**: Uthibitisho kamili wa maombi
- **Udhibiti wa Makosa**: Hakuna data nyeti katika ujumbe wa makosa

## 🎯 Muhimu wa Mambo Muhimu

Baada ya kumaliza utangulizi huu, unapaswa kuelewa:

✅ **Thamani ya MCP**: Jinsi MCP inavyounganisha wasaidizi wa AI na data halisi  
✅ **Muktadha wa Biashara**: Mahitaji na changamoto za Zava Retail  
✅ **Muhtasari wa Usanifu**: Vipengele muhimu na mwingiliano wake  
✅ **Stack ya Teknolojia**: Zana na mifumo inayotumika  
✅ **Mfano wa Usalama**: Upatikanaji wa data wa wateja wengi na ulinzi  
✅ **Mifumo ya Matumizi**: Matukio ya maswali halisi na mtiririko wa kazi  

## 🚀 Nini Kifuatacho

Tayari kuingia zaidi? Endelea na:

**[Lab 01: Mifumo ya Msingi ya Usanifu](../01-Architecture/README.md)**

Jifunze kuhusu mifumo ya usanifu wa seva ya MCP, kanuni za usanifu wa hifadhidata, na utekelezaji wa kina wa kiufundi unaounga mkono suluhisho letu la uchambuzi wa rejareja.

## 📚 Vyanzo Zaidi

### Nyaraka za MCP
- [MCP Specification](https://modelcontextprotocol.io/docs/) - Nyaraka rasmi za itifaki
- [MCP for Beginners](https://aka.ms/mcp-for-beginners) - Mwongozo mpana wa kujifunza MCP
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk) - Nyaraka za SDK ya Python

### Uunganisho wa Hifadhidata
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - Marejeleo kamilifu ya PostgreSQL
- [pgvector Guide](https://github.com/pgvector/pgvector) - Nyaraka za ugani wa vekta
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Mwongozo wa PostgreSQL RLS

### Huduma za Azure
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - Uunganisho wa huduma za AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Huduma ya hifadhidata iliyosimamiwa
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontena zisizo na seva

---

**Kifungu cha Hukumu**: Hii ni mazoezi ya kujifunza kwa kutumia data za rejareja za kubuniwa. Fuata sera za usimamizi wa data na usalama za shirika lako kila wakati unapotekeleza suluhisho kama hizi katika mazingira ya uzalishaji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->