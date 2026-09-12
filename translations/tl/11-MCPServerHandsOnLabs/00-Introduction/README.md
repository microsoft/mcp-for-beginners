# Panimula sa MCP Database Integration

> [!NOTE]
> Ang mga diagram o code sa learning path na ito na gumagamit ng HTTP/SSE o mga opsyon sa pagpapatakbo
> ay nagrereflekta sa sample MCP `2025-11-25` dependencies. Para sa mga bagong
> implementasyon, gamitin ang `2026-07-28` stateless requests at Streamable HTTP.

## 🎯 Ano ang Saklaw ng Lab na Ito

Ang pambungad na lab na ito ay nagbibigay ng komprehensibong overview sa paggawa ng Model Context Protocol (MCP) servers na may database integration. Mauunawaan mo ang kaso ng negosyo, teknikal na arkitektura, at mga aplikasyon sa totoong mundo sa pamamagitan ng Zava Retail analytics use case sa https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Pangkalahatang-ideya

**Model Context Protocol (MCP)** ay nagbibigay-daan sa AI assistants na ligtas na ma-access at makipag-ugnayan sa mga external na data source nang real-time. Kapag pinagsama sa database integration, binubuksan ng MCP ang makapangyarihang kakayahan para sa data-driven na AI applications.

Itinuturo ng learning path na ito kung paano bumuo ng production-ready MCP servers na kumokonekta sa AI assistants sa retail sales data gamit ang PostgreSQL, na nagpapatupad ng mga enterprise pattern tulad ng Row Level Security, semantic search, at multi-tenant data access.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng lab na ito, magagawa mong:

- **Ibigay ang Kahulugan sa** Model Context Protocol at ang pangunahing benepisyo nito para sa database integration
- **Kilalanin** ang mga pangunahing bahagi ng isang MCP server architecture na may mga database
- **Unawain** ang Zava Retail use case at ang mga pangangailangan sa negosyo nito
- **Kilalanin** ang mga enterprise pattern para sa ligtas at scalable na database access
- **Ilista** ang mga tool at teknolohiya na ginamit sa learning path na ito

## 🧭 Ang Hamon: Pagsasanib ng AI at Totoong Mundo na Data

### Mga Limitasyon ng Tradisyonal na AI

Ang modernong AI assistants ay napakabisa ngunit nahaharap sa mga limitasyong malaki kapag nagtatrabaho sa totoong mundo ng data sa negosyo:

| **Hamon** | **Paglalarawan** | **Epekto sa Negosyo** |
|---------------|-----------------|-------------------|
| **Static Knowledge** | Ang mga AI model na tinrain sa fixed datasets ay hindi makaka-access ng kasalukuyang data ng negosyo | Mga luma na insight, mga na-miss na oportunidad |
| **Data Silos** | Mga impormasyon na nakakulong sa mga database, API, at sistema na di maabot ng AI | Hindi kompletong pagsusuri, pira-pirasong workflow |
| **Security Constraints** | Direktang access sa database ay nagdudulot ng mga isyu sa seguridad at pagsunod | Limitadong deployment, manu-manong paghahanda ng data |
| **Complex Queries** | Kailangan ng teknikal na kaalaman ng mga business user para makuha ang data insights | Mabagal na pagtanggap, hindi mahusay na mga proseso |

### Ang Solusyon ng MCP

Nilulutas ng Model Context Protocol ang mga hamon na ito sa pamamagitan ng pagbibigay:

- **Access sa Data ng Real-time**: Ang AI assistants ay nag-que-ry sa live databases at APIs
- **Ligtas na Integrasyon**: Kinokontrol na access gamit ang authentication at permissions
- **Natural Language Interface**: Ang mga business user ay nagtatanong gamit ang payak na Ingles
- **Standardized Protocol**: Gumagana sa iba't ibang AI platform at mga tool

## 🏪 Kilalanin ang Zava Retail: Ang Aming Learning Case Study https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Sa kabuuan ng learning path na ito, gagawa tayo ng MCP server para sa **Zava Retail**, isang kathang-isip na DIY retail chain na may maraming mga lokasyon ng tindahan. Ipinapakita ng realistic na scenario na ito ang enterprise-grade na implementasyon ng MCP.

### Konteksto ng Negosyo

Ang **Zava Retail** ay nagpapatakbo ng:
- **8 pisikal na tindahan** sa iba't ibang bahagi ng estado ng Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online store** para sa e-commerce na mga benta
- **Iba't ibang katalogo ng produkto** kabilang ang mga kasangkapan, hardware, mga gamit sa hardin, at mga materyales sa gusali
- **Multi-level na pamamahala** na may mga store manager, regional manager, at mga ehekutibo

### Mga Pangunahing Pangangailangan sa Negosyo

Kailangan ng mga store manager at mga ehekutibo ng AI-powered na analytics upang:

1. **Suriin ang performance ng benta** sa mga tindahan at mga period ng oras
2. **Subaybayan ang mga lebel ng imbentaryo** at tukuyin ang pangangailangan sa restocking
3. **Unawain ang ugali ng customer** at mga pattern ng pagbili
4. **Tuklasin ang mga insight tungkol sa produkto** sa pamamagitan ng semantic search
5. **Gumawa ng mga ulat** gamit ang natural language na mga query
6. **Panatilihin ang seguridad ng data** gamit ang role-based access control

### Mga Teknikal na Pangangailangan

Ang MCP server ay dapat magbigay ng:

- **Multi-tenant data access** kung saan ang mga store manager ay makakakita lamang ng data ng kanilang sariling tindahan
- **Flexible querying** na sumusuporta sa mga komplikadong operasyon ng SQL
- **Semantic search** para sa pagtuklas at rekomendasyon ng produkto
- **Real-time data** na nagrereflekta ng kasalukuyang estado ng negosyo
- **Ligtas na authentication** na may row-level security
- **Scalable architecture** na sumusuporta sa maraming sabay-sabay na gumagamit

## 🏗️ Pangkalahatang-ideya ng Arkitektura ng MCP Server

Isinasaayos ng aming MCP server ang layered architecture na optimized para sa database integration:

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

### Mga Pangunahing Bahagi

#### **1. MCP Server Layer**
- **FastMCP Framework**: Modernong implementasyon ng Python MCP server
- **Tool Registration**: Deklaratibong pagtatakda ng tool na may type safety
- **Request Context**: Pamamahala ng user identity at session
- **Error Handling**: Matatag na pamamahala ng error at pag-log

#### **2. Database Integration Layer**
- **Connection Pooling**: Mahusay na asyncpg connection management
- **Schema Provider**: Dinamikong pagtuklas ng schema ng table
- **Query Executor**: Ligtas na pagpapatupad ng SQL na may RLS context
- **Transaction Management**: ACID compliance at pamamahala ng rollback

#### **3. Security Layer**
- **Row Level Security**: PostgreSQL RLS para sa multi-tenant na pag-isolate ng data
- **User Identity**: Authentication at authorization ng store manager
- **Access Control**: Pinong detalye ng permissions at audit trails
- **Input Validation**: Pag-iwas sa SQL injection at pag-validate ng query

#### **4. AI Enhancement Layer**
- **Semantic Search**: Vector embeddings para sa pagtuklas ng produkto
- **Azure OpenAI Integration**: Pagbuo ng text embedding
- **Similarity Algorithms**: pgvector cosine similarity search
- **Search Optimization**: Pag-index at tuning para sa performance

## 🔧 Teknolohiyang Ginamit

### Pangunahing Teknolohiya

| **Bahagi** | **Teknolohiya** | **Layunin** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Modernong implementasyon ng MCP server |
| **Database** | PostgreSQL 17 + pgvector | Relational data na may vector search |
| **AI Services** | Azure OpenAI | Text embeddings at mga language model |
| **Containerization** | Docker + Docker Compose | Development environment |
| **Cloud Platform** | Microsoft Azure | Production deployment |
| **IDE Integration** | VS Code | AI Chat at development workflow |

### Mga Tool sa Pag-develop

| **Tool** | **Layunin** |
|----------|-------------|
| **asyncpg** | Mataas na performance na PostgreSQL driver |
| **Pydantic** | Pag-validate ng data at serialization |
| **Azure SDK** | Integrasyon ng cloud service |
| **pytest** | Testing framework |
| **Docker** | Containerization at deployment |

### Production Stack

| **Serbisyo** | **Azure Resource** | **Layunin** |
|-------------|-------------------|-------------|
| **Database** | Azure Database for PostgreSQL | Managed database service |
| **Container** | Azure Container Apps | Serverless container hosting |
| **AI Services** | Microsoft Foundry | OpenAI models at endpoints |
| **Monitoring** | Application Insights | Observability at diagnostics |
| **Seguridad** | Azure Key Vault | Secrets at configuration management |

## 🎬 Mga Sitwasyon sa Totoong Mundo ng Paggamit

Tuklasin natin kung paano nakikipag-ugnayan ang iba't ibang user sa aming MCP server:

### Scenario 1: Pagsusuri ng Performance ng Store Manager

**User**: Sarah, Seattle Store Manager  
**Layunin**: Suriin ang sales performance ng nakaraang quarter

**Natural Language Query**:
> "Ipakita sa akin ang top 10 produkto ayon sa kita para sa aking tindahan sa Q4 2024"

**Ano ang Nangyayari**:
1. Nagpapadala ng query ang VS Code AI Chat sa MCP server
2. Tinutukoy ng MCP server ang konteksto ng tindahan ni Sarah (Seattle)
3. Pinipili ng RLS policies ang data ng Seattle store lamang
4. Binubuo at pinapatupad ang SQL query
5. Inaayos at ibinabalik ang mga resulta sa AI Chat
6. Nagbibigay ang AI ng pagsusuri at mga insight

### Scenario 2: Pagtuklas ng Produkto gamit ang Semantic Search

**User**: Mike, Inventory Manager  
**Layunin**: Maghanap ng mga produktong kahawig ng hiling ng customer

**Natural Language Query**:
> "Anong mga produkto ang binebenta namin na kahawig ng 'waterproof electrical connectors para sa panlabas na gamit'?"

**Ano ang Nangyayari**:
1. Pinoproseso ng semantic search tool ang query
2. Bumubuo ang Azure OpenAI ng embedding vector
3. Nagsasagawa ng similarity search ang pgvector
4. Niraranggo ang mga kaugnay na produkto ayon sa relevance
5. Kasama sa resulta ang detalye ng produkto at availability
6. Nagmumungkahi ang AI ng mga alternatibo at bundling opportunities

### Scenario 3: Cross-Store Analytics

**User**: Jennifer, Regional Manager  
**Layunin**: Ihambing ang performance sa lahat ng mga tindahan

**Natural Language Query**:
> "Ihambing ang benta ayon sa kategorya para sa lahat ng tindahan sa nakaraang 6 na buwan"

**Ano ang Nangyayari**:
1. Itinatakda ang RLS context para sa access ng regional manager
2. Binubuo ang komplikadong multi-store query
3. Pinagsasama ang data mula sa iba't ibang lokasyon ng tindahan
4. Kasama sa resulta ang mga trend at paghahambing
5. Nakikilala ng AI ang mga insight at rekomendasyon

## 🔒 Malalim na Pagsusuri sa Seguridad at Multi-Tenancy

Binibigyang-priyoridad ng aming implementasyon ang enterprise-grade na seguridad:

### Row Level Security (RLS)

Tinitiyak ng PostgreSQL RLS ang isolation ng data:

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

### Pamamahala ng User Identity

Kasama sa bawat koneksyon sa MCP:
- **Store Manager ID**: Natatanging identifier para sa RLS context
- **Role Assignment**: Mga permiso at antas ng access
- **Session Management**: Ligtas na authentication tokens
- **Audit Logging**: Kumpletong kasaysayan ng access

### Proteksyon ng Data

Maramihang layer ng seguridad:
- **Connection Encryption**: TLS para sa lahat ng koneksyon sa database
- **SQL Injection Prevention**: Parameterized queries lamang
- **Input Validation**: Komprehensibong validation ng request
- **Error Handling**: Walang sensitibong data sa mga mensahe ng error

## 🎯 Mga Pangunahing Aral

Matapos makumpleto ang panimulang ito, dapat mong maunawaan ang:

✅ **MCP Value Proposition**: Paano pinagdurugtong ng MCP ang AI assistants at totoong mundo na data  
✅ **Konteksto ng Negosyo**: Mga pangangailangan at hamon ng Zava Retail  
✅ **Pangkalahatang-ideya ng Arkitektura**: Mga pangunahing bahagi at ang kanilang interaksyon  
✅ **Teknolohiyang Ginamit**: Mga tool at framework na ginamit sa kabuuan  
✅ **Modelo ng Seguridad**: Multi-tenant data access at proteksyon  
✅ **Mga Pattern ng Paggamit**: Mga scenario ng real-world query at workflow  

## 🚀 Ano ang Susunod

Handa ka na bang sumisid ng mas malalim? Magpatuloy sa:

**[Lab 01: Core Architecture Concepts](../01-Architecture/README.md)**

Alamin ang mga pattern ng arkitektura ng MCP server, prinsipyo ng database design, at detalyadong teknikal na implementasyon na nagpapagana sa aming retail analytics solution.

## 📚 Karagdagang Mga Mapagkukunan

### Dokumentasyon ng MCP
- [MCP Specification](https://modelcontextprotocol.io/docs/) - Opisyal na dokumentasyon ng protocol
- [MCP for Beginners](https://aka.ms/mcp-for-beginners) - Komprehensibong gabay sa pag-aaral ng MCP
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk) - Dokumentasyon ng Python SDK

### Database Integration
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - Kumpletong sanggunian ng PostgreSQL
- [pgvector Guide](https://github.com/pgvector/pgvector) - Dokumentasyon ng vector extension
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Gabay sa PostgreSQL RLS

### Azure Services
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrasyon ng AI service
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Managed database service
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless containers

---

**Paunawa**: Ito ay isang pagsasanay na gumagamit ng kathang-isip na retail data. Laging sundin ang mga patakaran sa pamahalaan ng data at seguridad ng iyong organisasyon kapag nag-iimplementa ng katulad na mga solusyon sa production environment.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->