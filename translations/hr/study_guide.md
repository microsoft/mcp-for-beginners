# Protokol konteksta modela (MCP) za početnike - Vodič za učenje

Ovaj vodič pruža pregled strukture i sadržaja repozitorija za kurikulum "Protokol konteksta modela (MCP) za početnike". Koristite ovaj vodič kako biste učinkovito navigirali repozitorijem i maksimalno iskoristili dostupne resurse.

## Pregled repozitorija

Protokol konteksta modela (MCP) je standardizirani okvir za interakcije između AI modela i klijentskih aplikacija. Prvotno ga je kreirao Anthropic, a MCP sada održava šira MCP zajednica putem službene GitHub organizacije. Ovaj repozitorij pruža sveobuhvatan kurikulum s praktičnim primjerima koda u C#, Java, JavaScript, Python i TypeScript, namijenjen AI programerima, sistemskim arhitektima i softverskim inženjerima.

## Vizualna karta kurikuluma

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```

## Struktura repozitorija

Repozitorij je organiziran u jedanaest glavnih sekcija, od kojih svaka pokriva različite aspekte MCP-a:

1. **Uvod (00-Introduction/)**
   - Pregled Protokola konteksta modela
   - Zašto je standardizacija važna u AI procesima
   - Praktični primjeri korištenja i prednosti

2. **Osnovni koncepti (01-CoreConcepts/)**
   - Klijent-server arhitektura
   - Ključne komponente protokola
   - Obrasci razmjene poruka u MCP-u

3. **Sigurnost (02-Security/)**
   - Sigurnosne prijetnje u sustavima temeljenim na MCP-u
   - Najbolje prakse za osiguranje implementacija
   - Strategije autentifikacije i autorizacije
   - **Sveobuhvatna dokumentacija o sigurnosti**:
     - MCP najbolje prakse za sigurnost 2025
     - Vodič za implementaciju sigurnosti sadržaja na Azureu
     - Kontrole i tehnike sigurnosti MCP-a
     - Brzi referentni vodič za najbolje prakse MCP-a
   - **Ključne teme sigurnosti**:
     - Napadi ubrizgavanjem prompta i trovanje alata
     - Otimanje sesije i problemi s zbunjenim zamjenikom
     - Ranljivosti prijenosa tokena
     - Pretjerane dozvole i kontrola pristupa
     - Sigurnost opskrbnog lanca za AI komponente
     - Integracija Microsoft Prompt Shields

4. **Početak rada (03-GettingStarted/)**
   - Postavljanje i konfiguracija okruženja
   - Kreiranje osnovnih MCP servera i klijenata
   - Integracija s postojećim aplikacijama
   - Uključuje sekcije za:
     - Prvu implementaciju servera
     - Razvoj klijenta
     - Integraciju LLM klijenta
     - Integraciju s VS Codeom
     - Server-Sent Events (SSE) server
     - Napredno korištenje servera
     - HTTP streaming
     - Integraciju AI alata
     - Strategije testiranja
     - Smjernice za implementaciju

5. **Praktična implementacija (04-PracticalImplementation/)**
   - Korištenje SDK-ova u različitim programskim jezicima
   - Tehnike otklanjanja grešaka, testiranja i validacije
   - Izrada predložaka prompta i radnih tijekova koji se mogu ponovno koristiti
   - Primjeri projekata s implementacijom

6. **Napredne teme (05-AdvancedTopics/)**
   - Tehnike inženjeringa konteksta
   - Integracija Foundry agenta
   - Multimodalni AI radni tijekovi
   - Demonstracije autentifikacije putem OAuth2
   - Sposobnosti pretraživanja u stvarnom vremenu
   - Streaming u stvarnom vremenu
   - Implementacija osnovnih konteksta
   - Strategije usmjeravanja
   - Tehnike uzorkovanja
   - Pristupi skaliranju
   - Sigurnosna razmatranja
   - Integracija sigurnosti Entra ID-a
   - Integracija web pretraživanja

7. **Doprinosi zajednice (06-CommunityContributions/)**
   - Kako doprinijeti kodu i dokumentaciji
   - Suradnja putem GitHuba
   - Poboljšanja i povratne informacije vođene zajednicom
   - Korištenje različitih MCP klijenata (Claude Desktop, Cline, VSCode)
   - Rad s popularnim MCP serverima uključujući generiranje slika

8. **Lekcije iz ranog usvajanja (07-LessonsfromEarlyAdoption/)**
   - Implementacije iz stvarnog svijeta i priče o uspjehu
   - Izrada i implementacija rješenja temeljenih na MCP-u
   - Trendovi i buduća mapa puta
   - **Vodič za Microsoft MCP servere**: Sveobuhvatan vodič za 10 Microsoft MCP servera spremnih za produkciju, uključujući:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (15+ specijaliziranih konektora)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **Najbolje prakse (08-BestPractices/)**
   - Podešavanje performansi i optimizacija
   - Dizajniranje sustava MCP otpornog na greške
   - Strategije testiranja i otpornosti

10. **Studije slučaja (09-CaseStudy/)**
    - **Sedam sveobuhvatnih studija slučaja** koje demonstriraju svestranost MCP-a u raznim scenarijima:
    - **Azure AI putnički agenti**: Orkestracija više agenata s Azure OpenAI i AI pretraživanjem
    - **Integracija s Azure DevOpsom**: Automatizacija radnih procesa s ažuriranjima podataka s YouTubea
    - **Dohvaćanje dokumentacije u stvarnom vremenu**: Python konzolni klijent sa streamingom putem HTTP-a
    - **Interaktivni generator plana učenja**: Chainlit web aplikacija s konverzacijskim AI-jem
    - **Dokumentacija unutar uređivača**: Integracija s VS Codeom i GitHub Copilot radnim tijekovima
    - **Upravljanje API-jem na Azureu**: Integracija API-ja za poduzeća s kreiranjem MCP servera
    - **GitHub MCP Registry**: Razvoj ekosustava i platforma za agentičku integraciju
    - Primjeri implementacije koji obuhvaćaju integraciju u poduzeću, produktivnost programera i razvoj ekosustava

11. **Praktična radionica (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Sveobuhvatna praktična radionica koja kombinira MCP s AI Toolkitom
    - Izrada inteligentnih aplikacija koje povezuju AI modele s alatima iz stvarnog svijeta
    - Praktični moduli koji pokrivaju osnove, razvoj prilagođenih servera i strategije implementacije u produkciji
    - **Struktura laboratorija**:
      - Laboratorij 1: Osnove MCP servera
      - Laboratorij 2: Napredni razvoj MCP servera
      - Laboratorij 3: Integracija AI Toolkita
      - Laboratorij 4: Implementacija u produkciji i skaliranje
    - Pristup učenju temeljen na laboratorijima s korak-po-korak uputama

12. **Laboratoriji za integraciju MCP servera s bazom podataka (11-MCPServerHandsOnLabs/)**
    - **Sveobuhvatan put učenja kroz 13 laboratorija** za izradu MCP servera spremnih za produkciju s integracijom PostgreSQL-a
    - **Implementacija analitike maloprodaje iz stvarnog svijeta** koristeći Zava Retail slučaj
    - **Obrasci na razini poduzeća** uključujući sigurnost na razini redaka (RLS), semantičko pretraživanje i pristup podacima za više korisnika
    - **Kompletna struktura laboratorija**:
      - **Laboratoriji 00-03: Osnove** - Uvod, Arhitektura, Sigurnost, Postavljanje okruženja
      - **Laboratoriji 04-06: Izrada MCP servera** - Dizajn baze podataka, Implementacija MCP servera, Razvoj alata
      - **Laboratoriji 07-09: Napredne značajke** - Semantičko pretraživanje, Testiranje i otklanjanje grešaka, Integracija s VS Codeom
      - **Laboratoriji 10-12: Produkcija i najbolje prakse** - Implementacija, Praćenje, Optimizacija
    - **Obuhvaćene tehnologije**: FastMCP okvir, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Rezultati učenja**: MCP serveri spremni za produkciju, obrasci integracije baza podataka, analitika temeljena na AI-ju, sigurnost na razini poduzeća

## Dodatni resursi

Repozitorij uključuje podržavajuće resurse:

- **Mapa slika**: Sadrži dijagrame i ilustracije korištene u cijelom kurikulumu
- **Prijevodi**: Podrška za više jezika s automatskim prijevodima dokumentacije
- **Službeni MCP resursi**:
  - [MCP Dokumentacija](https://modelcontextprotocol.io/)
  - [MCP Specifikacija](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub Repozitorij](https://github.com/modelcontextprotocol)

## Kako koristiti ovaj repozitorij

1. **Sekvencijalno učenje**: Slijedite poglavlja redom (00 do 11) za strukturirano iskustvo učenja.
2. **Fokus na specifične jezike**: Ako vas zanima određeni programski jezik, istražite direktorije s primjerima implementacije u željenom jeziku.
3. **Praktična implementacija**: Započnite s odjeljkom "Početak rada" kako biste postavili svoje okruženje i kreirali svoj prvi MCP server i klijent.
4. **Napredno istraživanje**: Kada se upoznate s osnovama, zaronite u napredne teme kako biste proširili svoje znanje.
5. **Angažman zajednice**: Pridružite se MCP zajednici putem GitHub rasprava i Discord kanala kako biste se povezali s stručnjacima i kolegama programerima.

## MCP klijenti i alati

Kurikulum pokriva različite MCP klijente i alate:

1. **Službeni klijenti**:
   - Visual Studio Code 
   - MCP u Visual Studio Codeu
   - Claude Desktop
   - Claude u VSCodeu 
   - Claude API

2. **Klijenti zajednice**:
   - Cline (temeljen na terminalu)
   - Cursor (uređivač koda)
   - ChatMCP
   - Windsurf

3. **Alati za upravljanje MCP-om**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Popularni MCP serveri

Repozitorij uvodi različite MCP servere, uključujući:

1. **Službeni Microsoft MCP serveri**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (15+ specijaliziranih konektora)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **Službeni referentni serveri**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **Generiranje slika**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Alati za razvoj**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **Specijalizirani serveri**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Doprinosi

Ovaj repozitorij pozdravlja doprinose zajednice. Pogledajte odjeljak Doprinosi zajednice za smjernice o tome kako učinkovito doprinijeti MCP ekosustavu.

----

*Ovaj vodič za učenje ažuriran je 6. listopada 2025. i pruža pregled repozitorija na taj datum. Sadržaj repozitorija može biti ažuriran nakon ovog datuma.*

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.