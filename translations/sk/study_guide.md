# Protokol kontextu modelu (MCP) pre začiatočníkov - Študijný sprievodca

Tento študijný sprievodca poskytuje prehľad štruktúry a obsahu repozitára pre učebný plán "Protokol kontextu modelu (MCP) pre začiatočníkov". Použite tento sprievodca na efektívnu navigáciu v repozitári a maximálne využitie dostupných zdrojov.

## Prehľad repozitára

Protokol kontextu modelu (MCP) je štandardizovaný rámec pre interakcie medzi AI modelmi a klientskými aplikáciami. Pôvodne ho vytvorila spoločnosť Anthropic, no v súčasnosti ho spravuje širšia komunita MCP prostredníctvom oficiálnej organizácie na GitHube. Tento repozitár poskytuje komplexný učebný plán s praktickými príkladmi kódu v jazykoch C#, Java, JavaScript, Python a TypeScript, určený pre vývojárov AI, systémových architektov a softvérových inžinierov.

## Vizualizácia učebného plánu

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


## Štruktúra repozitára

Repozitár je organizovaný do jedenástich hlavných sekcií, z ktorých každá sa zameriava na rôzne aspekty MCP:

1. **Úvod (00-Introduction/)**
   - Prehľad protokolu kontextu modelu
   - Prečo je štandardizácia dôležitá v AI procesoch
   - Praktické prípady použitia a výhody

2. **Základné koncepty (01-CoreConcepts/)**
   - Architektúra klient-server
   - Kľúčové komponenty protokolu
   - Vzory správ v MCP

3. **Bezpečnosť (02-Security/)**
   - Bezpečnostné hrozby v systémoch založených na MCP
   - Najlepšie postupy na zabezpečenie implementácií
   - Stratégie autentifikácie a autorizácie
   - **Komplexná dokumentácia o bezpečnosti**:
     - Najlepšie bezpečnostné postupy MCP 2025
     - Príručka implementácie bezpečnosti obsahu Azure
     - Bezpečnostné kontroly a techniky MCP
     - Rýchly referenčný sprievodca najlepšími postupmi MCP
   - **Kľúčové bezpečnostné témy**:
     - Útoky na injekciu promptov a otravu nástrojov
     - Únos relácie a problémy s nejasným zástupcom
     - Zraniteľnosti pri prechode tokenov
     - Nadmerné oprávnenia a kontrola prístupu
     - Bezpečnosť dodávateľského reťazca pre AI komponenty
     - Integrácia Microsoft Prompt Shields

4. **Začíname (03-GettingStarted/)**
   - Nastavenie a konfigurácia prostredia
   - Vytváranie základných MCP serverov a klientov
   - Integrácia s existujúcimi aplikáciami
   - Obsahuje sekcie:
     - Prvá implementácia servera
     - Vývoj klienta
     - Integrácia LLM klienta
     - Integrácia VS Code
     - Server-Sent Events (SSE) server
     - Pokročilé používanie servera
     - HTTP streaming
     - Integrácia AI Toolkit
     - Testovacie stratégie
     - Pokyny na nasadenie

5. **Praktická implementácia (04-PracticalImplementation/)**
   - Používanie SDK v rôznych programovacích jazykoch
   - Techniky ladenia, testovania a validácie
   - Tvorba opakovane použiteľných šablón promptov a pracovných postupov
   - Ukážkové projekty s implementačnými príkladmi

6. **Pokročilé témy (05-AdvancedTopics/)**
   - Techniky inžinierstva kontextu
   - Integrácia Foundry agentov
   - Multimodálne AI pracovné postupy
   - Demos OAuth2 autentifikácie
   - Schopnosti reálneho vyhľadávania
   - Reálny streaming
   - Implementácia koreňových kontextov
   - Stratégie smerovania
   - Techniky vzorkovania
   - Prístupy k škálovaniu
   - Bezpečnostné úvahy
   - Integrácia bezpečnosti Entra ID
   - Integrácia webového vyhľadávania

7. **Príspevky komunity (06-CommunityContributions/)**
   - Ako prispievať kódom a dokumentáciou
   - Spolupráca cez GitHub
   - Vylepšenia a spätná väzba od komunity
   - Používanie rôznych MCP klientov (Claude Desktop, Cline, VSCode)
   - Práca s populárnymi MCP servermi vrátane generovania obrázkov

8. **Poučenia z raného prijatia (07-LessonsfromEarlyAdoption/)**
   - Implementácie v reálnom svete a úspešné príbehy
   - Budovanie a nasadzovanie riešení založených na MCP
   - Trendy a budúca cesta
   - **Príručka Microsoft MCP Servers**: Komplexná príručka k 10 produkčne pripraveným Microsoft MCP serverom vrátane:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (15+ špecializovaných konektorov)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **Najlepšie postupy (08-BestPractices/)**
   - Optimalizácia výkonu
   - Návrh odolných MCP systémov
   - Testovacie a odolnostné stratégie

10. **Prípadové štúdie (09-CaseStudy/)**
    - **Sedem komplexných prípadových štúdií** demonštrujúcich všestrannosť MCP v rôznych scenároch:
    - **Azure AI Travel Agents**: Orchestrácia viacerých agentov s Azure OpenAI a AI Search
    - **Integrácia Azure DevOps**: Automatizácia pracovných procesov s aktualizáciami údajov z YouTube
    - **Reálne načítanie dokumentácie**: Python konzolový klient s HTTP streamingom
    - **Interaktívny generátor študijných plánov**: Chainlit webová aplikácia s konverzačnou AI
    - **Dokumentácia v editore**: Integrácia VS Code s pracovnými postupmi GitHub Copilot
    - **Správa API Azure**: Integrácia podnikových API s vytváraním MCP serverov
    - **GitHub MCP Registry**: Vývoj ekosystému a platforma pre agentickú integráciu
    - Implementačné príklady pokrývajúce podnikové integrácie, produktivitu vývojárov a vývoj ekosystému

11. **Praktický workshop (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Komplexný praktický workshop kombinujúci MCP s AI Toolkit
    - Budovanie inteligentných aplikácií spájajúcich AI modely s reálnymi nástrojmi
    - Praktické moduly pokrývajúce základy, vývoj vlastného servera a stratégie nasadenia do produkcie
    - **Štruktúra laboratórií**:
      - Laboratórium 1: Základy MCP servera
      - Laboratórium 2: Pokročilý vývoj MCP servera
      - Laboratórium 3: Integrácia AI Toolkit
      - Laboratórium 4: Nasadenie do produkcie a škálovanie
    - Učenie založené na laboratóriách s podrobnými pokynmi

12. **Laboratóriá integrácie databázy MCP servera (11-MCPServerHandsOnLabs/)**
    - **Komplexná 13-laboratórna vzdelávacia cesta** pre budovanie produkčne pripravených MCP serverov s integráciou PostgreSQL
    - **Implementácia analýzy maloobchodných údajov v reálnom svete** pomocou prípadu použitia Zava Retail
    - **Vzory na podnikovej úrovni** vrátane Row Level Security (RLS), sémantického vyhľadávania a prístupu k údajom pre viacerých nájomcov
    - **Kompletná štruktúra laboratórií**:
      - **Laboratóriá 00-03: Základy** - Úvod, Architektúra, Bezpečnosť, Nastavenie prostredia
      - **Laboratóriá 04-06: Budovanie MCP servera** - Návrh databázy, Implementácia MCP servera, Vývoj nástrojov
      - **Laboratóriá 07-09: Pokročilé funkcie** - Sémantické vyhľadávanie, Testovanie a ladenie, Integrácia VS Code
      - **Laboratóriá 10-12: Produkcia a najlepšie postupy** - Nasadenie, Monitorovanie, Optimalizácia
    - **Pokryté technológie**: FastMCP framework, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Výsledky učenia**: Produkčne pripravené MCP servery, vzory integrácie databáz, analýza údajov poháňaná AI, podniková bezpečnosť

## Dodatočné zdroje

Repozitár obsahuje podporné zdroje:

- **Priečinok s obrázkami**: Obsahuje diagramy a ilustrácie použité v celom učebnom pláne
- **Preklady**: Podpora viacerých jazykov s automatickými prekladmi dokumentácie
- **Oficiálne zdroje MCP**:
  - [Dokumentácia MCP](https://modelcontextprotocol.io/)
  - [Špecifikácia MCP](https://spec.modelcontextprotocol.io/)
  - [GitHub repozitár MCP](https://github.com/modelcontextprotocol)

## Ako používať tento repozitár

1. **Sekvenčné učenie**: Sledujte kapitoly v poradí (00 až 11) pre štruktúrovaný zážitok z učenia.
2. **Zameranie na konkrétny jazyk**: Ak vás zaujíma konkrétny programovací jazyk, preskúmajte adresáre so vzorkami implementácií vo vašom preferovanom jazyku.
3. **Praktická implementácia**: Začnite sekciou "Začíname", aby ste nastavili svoje prostredie a vytvorili svoj prvý MCP server a klienta.
4. **Pokročilé skúmanie**: Keď sa oboznámite so základmi, ponorte sa do pokročilých tém na rozšírenie svojich vedomostí.
5. **Zapojenie komunity**: Pripojte sa ku komunite MCP prostredníctvom diskusií na GitHube a kanálov na Discorde, aby ste sa spojili s odborníkmi a ostatnými vývojármi.

## MCP klienti a nástroje

Učebný plán pokrýva rôznych MCP klientov a nástroje:

1. **Oficiálni klienti**:
   - Visual Studio Code 
   - MCP vo Visual Studio Code
   - Claude Desktop
   - Claude vo VSCode 
   - Claude API

2. **Klienti komunity**:
   - Cline (založený na termináli)
   - Cursor (editor kódu)
   - ChatMCP
   - Windsurf

3. **Nástroje na správu MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Populárne MCP servery

Repozitár predstavuje rôzne MCP servery, vrátane:

1. **Oficiálne Microsoft MCP servery**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (15+ špecializovaných konektorov)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **Oficiálne referenčné servery**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **Generovanie obrázkov**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Nástroje pre vývoj**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **Špecializované servery**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Príspevky

Tento repozitár víta príspevky od komunity. Pozrite si sekciu Príspevky komunity pre pokyny, ako efektívne prispieť do ekosystému MCP.

----

*Tento študijný sprievodca bol aktualizovaný 6. októbra 2025 a poskytuje prehľad repozitára k tomuto dátumu. Obsah repozitára môže byť aktualizovaný po tomto dátume.*

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.