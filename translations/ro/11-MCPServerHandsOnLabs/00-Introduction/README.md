# Introducere în Integrarea Bazei de Date MCP

## 🎯 Ce Acoperă Acest Laborator

Acest laborator introductiv oferă o privire de ansamblu asupra construirii serverelor Model Context Protocol (MCP) cu integrare în baze de date. Veți înțelege cazul de afaceri, arhitectura tehnică și aplicațiile reale prin exemplul de analiză Zava Retail disponibil la https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Prezentare Generală

**Model Context Protocol (MCP)** permite asistenților AI să acceseze și să interacționeze în siguranță cu surse de date externe în timp real. Când este combinat cu integrarea bazelor de date, MCP deblochează capabilități puternice pentru aplicațiile AI bazate pe date.

Acest parcurs de învățare vă învață să construiți servere MCP pregătite pentru producție, care conectează asistenții AI la datele de vânzări din retail prin PostgreSQL, implementând modele de întreprindere precum Row Level Security, căutare semantică și acces multi-tenant la date.

## Obiective de Învățare

Până la finalul acestui laborator, veți putea:

- **Defini** Protocolul Model Context și beneficiile sale principale pentru integrarea bazelor de date
- **Identifica** componentele cheie ale unei arhitecturi de server MCP cu baze de date
- **Înțelege** cazul de utilizare Zava Retail și cerințele sale de afaceri
- **Recunoaște** modele de întreprindere pentru acces sigur și scalabil la baze de date
- **Lista** instrumentele și tehnologiile utilizate pe parcursul acestui parcurs de învățare

## 🧭 Provocarea: AI Întâlnește Datele din Lumea Reală

### Limitările AI Tradițional

Asistenții AI moderni sunt extrem de puternici, dar se confruntă cu limitări semnificative atunci când lucrează cu datele de afaceri din lumea reală:

| **Provocare** | **Descriere** | **Impact asupra afacerii** |
|---------------|-----------------|-------------------|
| **Cunoștințe Statice** | Modelele AI antrenate pe seturi de date fixe nu pot accesa datele actuale de afaceri | Perspective depășite, oportunități ratate |
| **Insule de Date** | Informații blocate în baze de date, API-uri și sisteme inaccesibile AI | Analiză incompletă, fluxuri de lucru fragmentate |
| **Constrângeri de Securitate** | Accesul direct la baze de date ridică probleme de securitate și conformitate | Implementare limitată, pregătire manuală a datelor |
| **Interogări Complexe** | Utilizatorii de afaceri au nevoie de cunoștințe tehnice pentru a extrage perspective din date | Adoptare redusă, procese ineficiente |

### Soluția MCP

Protocolul Model Context abordează aceste provocări oferind:

- **Acces la Date în Timp Real**: Asistenții AI interoghează baze de date și API-uri live
- **Integrare Securizată**: Acces controlat cu autentificare și permisiuni
- **Interfață în Limbaj Natural**: Utilizatorii de afaceri pun întrebări în limbaj simplu
- **Protocol Standardizat**: Funcționează pe diverse platforme și instrumente AI

## 🏪 Cunoașteți Zava Retail: Studiul nostru de Caz https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Pe parcursul acestui parcurs de învățare, vom construi un server MCP pentru **Zava Retail**, un lanț fictiv de retail DIY cu mai multe locații. Acest scenariu realist demonstrează implementarea MCP la nivel de întreprindere.

### Contextul Afacerii

**Zava Retail** operează:
- **8 magazine fizice** în statul Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 magazin online** pentru vânzări e-commerce
- **Catalog divers de produse** incluzând unelte, hardware, materiale de grădină și construcții
- **Management pe mai multe niveluri** cu manageri de magazin, manageri regionali și executivi

### Cerințe de Afaceri

Managerii de magazin și executivii au nevoie de analize AI pentru:

1. **Analiza performanței vânzărilor** pe magazine și perioade de timp
2. **Monitorizarea nivelurilor de inventar** și identificarea necesităților de reaprovizionare
3. **Înțelegerea comportamentului clienților** și a modelelor de achiziție
4. **Descoperirea perspectivelor despre produse** prin căutare semantică
5. **Generarea de rapoarte** cu interogări în limbaj natural
6. **Menținerea securității datelor** prin controlul accesului bazat pe roluri

### Cerințe Tehnice

Serverul MCP trebuie să ofere:

- **Acces multi-tenant la date**, unde managerii de magazin văd doar datele magazinului lor
- **Interogare flexibilă** care suportă operațiuni SQL complexe
- **Căutare semantică** pentru descoperirea și recomandarea produselor
- **Date în timp real** care reflectă starea actuală a afacerii
- **Autentificare securizată** cu Row Level Security
- **Arhitectură scalabilă** care suportă utilizatori simultani multipli

## 🏗️ Prezentare Generală a Arhitecturii Serverului MCP

Serverul nostru MCP implementează o arhitectură stratificată optimizată pentru integrarea bazelor de date:

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

### Componente Cheie

#### **1. Strat Server MCP**
- **Framework FastMCP**: Implementare modernă de server MCP în Python
- **Înregistrarea Instrumentelor**: Definiții declarative ale instrumentelor cu siguranță tipurilor
- **Contextul Cererii**: Gestionarea identității utilizatorului și a sesiunii
- **Gestionarea Erorilor**: Management robust al erorilor și jurnalizare

#### **2. Strat de Integrare a Bazei de Date**
- **Pooling de Conexiuni**: Gestionarea eficientă a conexiunilor asyncpg
- **Furnizor de Scheme**: Descoperirea dinamică a schemelor de tabel
- **Executor de Interogări**: Execuție SQL securizată cu context RLS
- **Gestionarea Tranzacțiilor**: Conformitate ACID și gestionarea rollback-urilor

#### **3. Strat de Securitate**
- **Row Level Security**: RLS PostgreSQL pentru izolarea datelor multi-tenant
- **Identitatea Utilizatorului**: Autentificarea și autorizarea managerilor de magazin
- **Controlul Accesului**: Permisiuni detaliate și trasee de audit
- **Validarea Inputului**: Prevenirea injecțiilor SQL și validarea interogărilor

#### **4. Strat de Îmbunătățire AI**
- **Căutare Semantică**: Vector embeddings pentru descoperirea produselor
- **Integrare Azure OpenAI**: Generarea de embeddings textuale
- **Algoritmi de Similaritate**: Căutare de similaritate cosine pgvector
- **Optimizarea Căutării**: Indexare și ajustare a performanței

## 🔧 Tehnologii Utilizate

### Tehnologii de Bază

| **Componentă** | **Tehnologie** | **Scop** |
|----------------|----------------|----------|
| **Framework MCP** | FastMCP (Python) | Implementare modernă de server MCP |
| **Bază de Date** | PostgreSQL 17 + pgvector | Date relaționale cu căutare vectorială |
| **Servicii AI** | Azure OpenAI | Embeddings textuale și modele lingvistice |
| **Containerizare** | Docker + Docker Compose | Mediu de dezvoltare |
| **Platformă Cloud** | Microsoft Azure | Implementare în producție |
| **Integrare IDE** | VS Code | Chat AI și flux de lucru de dezvoltare |

### Instrumente de Dezvoltare

| **Instrument** | **Scop** |
|----------------|----------|
| **asyncpg** | Driver PostgreSQL de înaltă performanță |
| **Pydantic** | Validarea și serializarea datelor |
| **Azure SDK** | Integrarea serviciilor cloud |
| **pytest** | Framework de testare |
| **Docker** | Containerizare și implementare |

### Stack de Producție

| **Serviciu** | **Resursă Azure** | **Scop** |
|--------------|-------------------|----------|
| **Bază de Date** | Azure Database for PostgreSQL | Serviciu de bază de date gestionat |
| **Container** | Azure Container Apps | Găzduire serverless pentru containere |
| **Servicii AI** | Azure AI Foundry | Modele OpenAI și puncte de acces |
| **Monitorizare** | Application Insights | Observabilitate și diagnosticare |
| **Securitate** | Azure Key Vault | Gestionarea secretelor și configurațiilor |

## 🎬 Scenarii de Utilizare în Lumea Reală

Să explorăm cum interacționează diferiți utilizatori cu serverul nostru MCP:

### Scenariul 1: Revizuirea Performanței Managerului de Magazin

**Utilizator**: Sarah, Manager Magazin Seattle  
**Obiectiv**: Analiza performanței vânzărilor din ultimul trimestru

**Interogare în Limbaj Natural**:
> "Arată-mi primele 10 produse după venituri pentru magazinul meu în T4 2024"

**Ce Se Întâmplă**:
1. Chat-ul AI din VS Code trimite interogarea la serverul MCP
2. Serverul MCP identifică contextul magazinului lui Sarah (Seattle)
3. Politicile RLS filtrează datele doar pentru magazinul din Seattle
4. Interogarea SQL este generată și executată
5. Rezultatele sunt formatate și returnate către Chat-ul AI
6. AI oferă analize și perspective

### Scenariul 2: Descoperirea Produselor prin Căutare Semantică

**Utilizator**: Mike, Manager Inventar  
**Obiectiv**: Găsirea produselor similare unei cereri a clientului

**Interogare în Limbaj Natural**:
> "Ce produse vindem care sunt similare cu 'conectori electrici impermeabili pentru utilizare în exterior'?"

**Ce Se Întâmplă**:
1. Interogarea este procesată de instrumentul de căutare semantică
2. Azure OpenAI generează vectorul embedding
3. pgvector efectuează căutarea de similaritate
4. Produsele relevante sunt clasificate după relevanță
5. Rezultatele includ detalii despre produse și disponibilitate
6. AI sugerează alternative și oportunități de pachete

### Scenariul 3: Analiza Performanței între Magazine

**Utilizator**: Jennifer, Manager Regional  
**Obiectiv**: Compararea performanței între toate magazinele

**Interogare în Limbaj Natural**:
> "Compară vânzările pe categorii pentru toate magazinele în ultimele 6 luni"

**Ce Se Întâmplă**:
1. Contextul RLS este setat pentru accesul managerului regional
2. Interogarea complexă multi-magazin este generată
3. Datele sunt agregate între locațiile magazinelor
4. Rezultatele includ tendințe și comparații
5. AI identifică perspective și recomandări

## 🔒 Detalii despre Securitate și Multi-Tenancy

Implementarea noastră prioritizează securitatea la nivel de întreprindere:

### Row Level Security (RLS)

RLS PostgreSQL asigură izolarea datelor:

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

### Gestionarea Identității Utilizatorului

Fiecare conexiune MCP include:
- **ID Manager Magazin**: Identificator unic pentru contextul RLS
- **Atribuirea Rolurilor**: Permisiuni și niveluri de acces
- **Gestionarea Sesiunii**: Token-uri de autentificare securizate
- **Jurnalizare Audit**: Istoric complet al accesului

### Protecția Datelor

Mai multe straturi de securitate:
- **Criptarea Conexiunilor**: TLS pentru toate conexiunile la bazele de date
- **Prevenirea Injecțiilor SQL**: Doar interogări parametrizate
- **Validarea Inputului**: Validare cuprinzătoare a cererilor
- **Gestionarea Erorilor**: Fără date sensibile în mesajele de eroare

## 🎯 Concluzii Cheie

După finalizarea acestei introduceri, ar trebui să înțelegeți:

✅ **Propunerea de Valoare MCP**: Cum MCP conectează asistenții AI la datele din lumea reală  
✅ **Contextul Afacerii**: Cerințele și provocările Zava Retail  
✅ **Prezentare Generală a Arhitecturii**: Componentele cheie și interacțiunile lor  
✅ **Tehnologii Utilizate**: Instrumentele și framework-urile utilizate pe parcurs  
✅ **Modelul de Securitate**: Acces multi-tenant la date și protecție  
✅ **Modele de Utilizare**: Scenarii reale de interogare și fluxuri de lucru  

## 🚀 Ce Urmează

Gata să aprofundați? Continuați cu:

**[Laborator 01: Concepte de Arhitectură de Bază](../01-Architecture/README.md)**

Aflați despre modelele de arhitectură ale serverului MCP, principiile de proiectare ale bazelor de date și implementarea tehnică detaliată care alimentează soluția noastră de analiză în retail.

## 📚 Resurse Suplimentare

### Documentație MCP
- [Specificația MCP](https://modelcontextprotocol.io/docs/) - Documentația oficială a protocolului
- [MCP pentru Începători](https://aka.ms/mcp-for-beginners) - Ghid complet de învățare MCP
- [Documentația FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Documentația SDK Python

### Integrarea Bazelor de Date
- [Documentația PostgreSQL](https://www.postgresql.org/docs/) - Referință completă PostgreSQL
- [Ghid pgvector](https://github.com/pgvector/pgvector) - Documentația extensiei vectoriale
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Ghid RLS PostgreSQL

### Servicii Azure
- [Documentația Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrarea serviciilor AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Serviciu de bază de date gestionat
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Containere serverless

---

**Disclaimer**: Acesta este un exercițiu de învățare utilizând date fictive de retail. Urmați întotdeauna politicile de guvernanță și securitate ale organizației dvs. atunci când implementați soluții similare în medii de producție.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.