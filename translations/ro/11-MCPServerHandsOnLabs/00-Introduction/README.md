# Introducere în Integrarea Bazei de Date MCP

> [!NOTE]
> Diagramele sau codul din acest traseu de învățare care utilizează HTTP/SSE sau opțiuni de inițializare reflectă dependențele de MCP `2025-11-25` ale exemplului. Pentru implementările noi, utilizați cererile stateless `2026-07-28` și HTTP Streamable.
> 


## 🎯 Ce acoperă acest laborator

Acest laborator introductiv oferă o prezentare cuprinzătoare pentru construirea serverelor Model Context Protocol (MCP) cu integrare în baze de date. Veți înțelege cazul de afaceri, arhitectura tehnică și aplicații reale prin exemplul de analiză Zava Retail la https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Prezentare generală

**Model Context Protocol (MCP)** permite asistenților AI să acceseze și să interacționeze în siguranță cu surse externe de date în timp real. Combinat cu integrarea bazei de date, MCP oferă capabilități puternice pentru aplicații AI bazate pe date.

Acest traseu de învățare vă învață să construiți servere MCP gata de producție care conectează asistenții AI la date de vânzări retail prin PostgreSQL, implementând modele enterprise precum Row Level Security, căutare semantică și acces multi-tenant la date.

## Obiectivele de învățare

La finalul acestui laborator, veți putea:

- **Definiți** Model Context Protocol și beneficiile sale cheie pentru integrarea bazelor de date
- **Identificați** componentele principale ale arhitecturii serverului MCP cu baze de date
- **Înțelegeți** cazul de utilizare Zava Retail și cerințele sale de afaceri
- **Recunoașteți** modelele enterprise pentru acces securizat și scalabil la baze de date
- **Enumerați** instrumentele și tehnologiile folosite pe parcursul acestui traseu de învățare

## 🧭 Provocarea: AI se întâlnește cu date reale

### Limitările tradiționale ale AI

Asistenții AI moderni sunt incredibil de puternici, dar se confruntă cu limitări serioase când lucrează cu date reale de afaceri:

| **Provocare** | **Descriere** | **Impact de afaceri** |
|---------------|-----------------|-------------------|
| **Cunoștințe statice** | Modelele AI antrenate pe seturi fixe de date nu pot accesa datele curente de afaceri | Informații depășite, oportunități ratate |
| **Silo-uri de date** | Informații blocate în baze de date, API-uri și sisteme inaccesibile AI | Analize incomplete, fluxuri de lucru fragmentate |
| **Constrângeri de securitate** | Accesul direct la bază de date ridică probleme de securitate și conformitate | Implementare limitată, pregătire manuală a datelor |
| **Interogări complexe** | Utilizatorii de business au nevoie de cunoștințe tehnice pentru a extrage perspectivele datelor | Adoptare redusă, procese ineficiente |

### Soluția MCP

Model Context Protocol abordează aceste provocări oferind:

- **Acces în timp real la date**: Asistenții AI interoghează baze de date și API-uri live
- **Integrare securizată**: Acces controlat cu autentificare și permisiuni
- **Interfață în limbaj natural**: Utilizatorii de business pun întrebări în limba engleză comună
- **Protocol standardizat**: Funcționează pe diverse platforme și instrumente AI

## 🏪 Faceți cunoștință cu Zava Retail: Studiul nostru de caz https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Pe parcursul acestui traseu de învățare, vom construi un server MCP pentru **Zava Retail**, un lanț de retail DIY fictiv cu locații multiple. Acest scenariu realist demonstrează implementarea MCP la nivel enterprise.

### Context de afaceri

**Zava Retail** operează:
- **8 magazine fizice** în statul Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 magazin online** pentru vânzări e-commerce
- **Catalog diversificat de produse** incluzând unelte, materiale hardware, produse pentru grădină și materiale de construcții
- **Management pe mai multe niveluri** cu manageri de magazin, manageri regionali și executivi

### Cerințe de afaceri

Managerii de magazin și executivii au nevoie de analize alimentate de AI pentru a:

1. **Analiza performanței vânzărilor** în toate magazinele și perioadele de timp
2. **Urmărirea nivelului de inventar** și identificarea necesarului de reaprovizionare
3. **Înțelegerea comportamentului clienților** și a tiparelor de cumpărare
4. **Descoperirea perspectivelor produselor** prin căutare semantică
5. **Generarea rapoartelor** cu interogări în limbaj natural
6. **Menținerea securității datelor** prin controlul accesului bazat pe roluri

### Cerințe tehnice

Serverul MCP trebuie să ofere:

- **Acces multi-tenant la date** unde managerii de magazin văd doar datele magazinului lor
- **Interogare flexibilă** suportând operațiuni SQL complexe
- **Căutare semantică** pentru descoperirea produselor și recomandări
- **Date în timp real** reflectând starea curentă a afacerii
- **Autentificare securizată** cu Row Level Security
- **Arhitectură scalabilă** ce suportă mulți utilizatori concurenți

## 🏗️ Prezentare arhitectură server MCP

Serverul nostru MCP implementează o arhitectură stratificată optimizată pentru integrarea bazei de date:

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

### Componente esențiale

#### **1. Strat server MCP**
- **FastMCP Framework**: Implementare modernă a serverului MCP în Python
- **Înregistrare unelte**: Definiții declarative ale uneltelor cu tipuri sigure
- **Context cerere**: Identitatea utilizatorului și gestionarea sesiunii
- **Gestionare erori**: Management robust al erorilor și logare

#### **2. Strat integrare bază de date**
- **Pooling conexiuni**: Administrare eficientă a conexiunilor asyncpg
- **Furnizor schemă**: Descoperirea dinamică a schemei tabelelor
- **Executor interogări**: Execuție SQL securizată cu context RLS
- **Gestionare tranzacții**: Conformitate ACID și rollback

#### **3. Strat de securitate**
- **Row Level Security**: Izolare multi-tenant a datelor cu RLS în PostgreSQL
- **Identitate utilizator**: Autentificare și autorizare manager magazin
- **Control acces**: Permisiuni fine-grained și audit
- **Validare input**: Prevenție SQL injection și validare interogări

#### **4. Strat de îmbunătățire AI**
- **Căutare semantică**: Vector embeddings pentru descoperirea produselor
- **Integrare Azure OpenAI**: Generarea embedărilor textuale
- **Algoritmi de similaritate**: Căutare similitudine cosine cu pgvector
- **Optimizare căutare**: Indexare și tuning performanță

## 🔧 Stack tehnologic

### Tehnologii de bază

| **Componentă** | **Tehnologie** | **Scop** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Implementare modernă server MCP |
| **Bază de date** | PostgreSQL 17 + pgvector | Date relaționale cu căutare vectorială |
| **Servicii AI** | Azure OpenAI | Embedări text și modele de limbaj |
| **Containerizare** | Docker + Docker Compose | Mediu de dezvoltare |
| **Platformă cloud** | Microsoft Azure | Deploy în producție |
| **Integrare IDE** | VS Code | Chat AI și flux dezvoltare |

### Unelte de dezvoltare

| **Unealtă** | **Scop** |
|----------|-------------|
| **asyncpg** | Driver performant PostgreSQL |
| **Pydantic** | Validare și serializare date |
| **Azure SDK** | Integrare servicii cloud |
| **pytest** | Framework testare |
| **Docker** | Containerizare și deployment |

### Stack pentru producție

| **Serviciu** | **Resursă Azure** | **Scop** |
|-------------|-------------------|-------------|
| **Bază de date** | Azure Database for PostgreSQL | Serviciu gestionat de baze de date |
| **Container** | Azure Container Apps | Gazduire containere fără server |
| **Servicii AI** | Microsoft Foundry | Modele și endpoint-uri OpenAI |
| **Monitorizare** | Application Insights | Observabilitate și diagnostic |
| **Securitate** | Azure Key Vault | Gestionare secrete și configurare |

## 🎬 Scenarii de utilizare reale

Să explorăm cum interacționează diferiți utilizatori cu serverul nostru MCP:

### Scenariul 1: Evaluarea performanței managerului de magazin

**Utilizator**: Sarah, manager magazin Seattle  
**Obiectiv**: Analiza performanței vânzărilor din ultimul trimestru

**Interogare în limbaj natural**:
> "Arată-mi top 10 produse după venit pentru magazinul meu în T4 2024"

**Ce se întâmplă**:
1. VS Code AI Chat trimite interogarea către serverul MCP
2. Serverul MCP identifică contextul magazinului lui Sarah (Seattle)
3. Politicile RLS filtrează datele doar pentru magazinul Seattle
4. Interogarea SQL este generată și executată
5. Rezultatele sunt formatate și returnate AI Chat
6. AI oferă analiză și perspective

### Scenariul 2: Descoperirea produselor prin căutare semantică

**Utilizator**: Mike, manager inventar  
**Obiectiv**: Găsirea produselor similare unui cereri a clientului

**Interogare în limbaj natural**:
> "Ce produse vindem care sunt similare cu 'conectori electrici impermeabili pentru utilizare în exterior'?"

**Ce se întâmplă**:
1. Interogarea este procesată de unealta de căutare semantică
2. Azure OpenAI generează vectorul embedding
3. pgvector realizează căutarea de similaritate
4. Produsele conexe sunt clasificate după relevanță
5. Rezultatele includ detalii și disponibilitate produse
6. AI sugerează alternative și oportunități de pachete

### Scenariul 3: Analize cross-store

**Utilizator**: Jennifer, manager regional  
**Obiectiv**: Compararea performanței între toate magazinele

**Interogare în limbaj natural**:
> "Compară vânzările pe categorii pentru toate magazinele în ultimele 6 luni"

**Ce se întâmplă**:
1. Contextul RLS este setat pentru accesul managerului regional
2. Este generată o interogare complexă multi-magazin
3. Datele sunt agregate pe locațiile magazinelor
4. Rezultatele includ trenduri și comparații
5. AI identifică perspective și recomandări

## 🔒 Securitate și Multi-Tenancy în detaliu

Implementarea noastră prioritizează securitatea la nivel enterprise:

### Row Level Security (RLS)

PostgreSQL RLS asigură izolare a datelor:

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

### Gestionarea identității utilizatorului

Fiecare conexiune MCP include:
- **ID manager magazin**: Identificator unic pentru contextul RLS
- **Asignare roluri**: Permisiuni și niveluri de acces
- **Gestionare sesiune**: Tokenuri de autentificare securizate
- **Logare audit**: Istoric complet de acces

### Protecția datelor

Mai multe straturi de securitate:
- **Criptare conexiune**: TLS pentru toate conexiunile la baza de date
- **Prevenție SQL injection**: Doar interogări parametrizate
- **Validare input**: Validare completă a cererilor
- **Gestionare erori**: Fără date sensibile în mesajele de eroare

## 🎯 Concluzii cheie

După finalizarea acestei introduceri, ar trebui să înțelegeți:

✅ **Propoziția de valoare MCP**: Cum MCP face legătura între asistenții AI și datele reale  
✅ **Contextul de afaceri**: Cerințele și provocările Zava Retail  
✅ **Prezentare arhitectură**: Componentele cheie și interacțiunile lor  
✅ **Stack tehnologic**: Instrumentele și framework-urile utilizate  
✅ **Model de securitate**: Acces și protecție multi-tenant la date  
✅ **Modele de utilizare**: Scenarii reale de interogare și fluxuri de lucru  

## 🚀 Ce urmează

Sunteți gata să aprofundați? Continuați cu:

**[Laboratorul 01: Concepte de arhitectură de bază](../01-Architecture/README.md)**

Aflați despre modelele arhitecturale ale serverelor MCP, principiile de design ale bazelor de date și implementarea tehnică detaliată care susține soluția noastră de analiză retail.

## 📚 Resurse suplimentare

### Documentație MCP
- [Specificația MCP](https://modelcontextprotocol.io/docs/) - Documentație oficială a protocolului
- [MCP pentru începători](https://aka.ms/mcp-for-beginners) - Ghid cuprinzător de învățare MCP
- [Documentație FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentație SDK Python

### Integrarea bazelor de date
- [Documentație PostgreSQL](https://www.postgresql.org/docs/) - Referință completă PostgreSQL
- [Ghid pgvector](https://github.com/pgvector/pgvector) - Documentația extensiei vectoriale
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Ghid RLS PostgreSQL

### Servicii Azure
- [Documentație Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrare servicii AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Serviciu gestionat de baze de date
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Containere fără server

---

**Declinarea responsabilității**: Acesta este un exercițiu de învățare folosind date fictive de retail. Urmați întotdeauna politicile organizației privind guvernanța și securitatea datelor la implementarea unor soluții similare în medii de producție.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->