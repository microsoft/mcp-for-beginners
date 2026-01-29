# Protokol konteksta modela (MCP) za začetnike - Vodnik za študij

Ta vodnik za študij ponuja pregled strukture in vsebine repozitorija za učni načrt "Protokol konteksta modela (MCP) za začetnike". Uporabite ta vodnik za učinkovito navigacijo po repozitoriju in kar najboljši izkoristek razpoložljivih virov.

## Pregled repozitorija

Protokol konteksta modela (MCP) je standardiziran okvir za interakcije med modeli umetne inteligence in odjemalskimi aplikacijami. MCP je bil sprva ustvarjen pri Anthropic, zdaj pa ga vzdržuje širša skupnost MCP prek uradne organizacije na GitHubu. Ta repozitorij ponuja celovit učni načrt s praktičnimi primeri kode v C#, Java, JavaScript, Python in TypeScript, zasnovan za razvijalce umetne inteligence, sistemske arhitekte in programske inženirje.

## Vizualni zemljevid učnega načrta

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

Repozitorij je organiziran v enajst glavnih razdelkov, od katerih se vsak osredotoča na različne vidike MCP:

1. **Uvod (00-Introduction/)**
   - Pregled protokola konteksta modela
   - Zakaj je standardizacija pomembna v procesih umetne inteligence
   - Praktični primeri uporabe in koristi

2. **Osnovni koncepti (01-CoreConcepts/)**
   - Arhitektura odjemalec-strežnik
   - Ključne komponente protokola
   - Vzorci sporočanja v MCP

3. **Varnost (02-Security/)**
   - Grožnje varnosti v sistemih, ki temeljijo na MCP
   - Najboljše prakse za varne implementacije
   - Strategije za avtentikacijo in avtorizacijo
   - **Celovita varnostna dokumentacija**:
     - Najboljše prakse za varnost MCP 2025
     - Vodnik za implementacijo varnosti vsebin Azure
     - Nadzor in tehnike varnosti MCP
     - Hitri referenčni priročnik za najboljše prakse MCP
   - **Ključne teme varnosti**:
     - Napadi z vbrizgavanjem pozivov in zastrupitev orodij
     - Ugrabitev sej in težave z zmedenim namestnikom
     - Ranljivosti pri prenosu žetonov
     - Prekomerne pravice in nadzor dostopa
     - Varnost dobavne verige za komponente umetne inteligence
     - Integracija Microsoft Prompt Shields

4. **Začetek (03-GettingStarted/)**
   - Nastavitev okolja in konfiguracija
   - Ustvarjanje osnovnih MCP strežnikov in odjemalcev
   - Integracija z obstoječimi aplikacijami
   - Vključuje razdelke za:
     - Prvo implementacijo strežnika
     - Razvoj odjemalca
     - Integracijo odjemalca LLM
     - Integracijo z VS Code
     - Strežnik za dogodke, poslane s strežnika (SSE)
     - Napredno uporabo strežnika
     - HTTP pretakanje
     - Integracijo AI Toolkit
     - Strategije testiranja
     - Smernice za uvajanje

5. **Praktična implementacija (04-PracticalImplementation/)**
   - Uporaba SDK-jev v različnih programskih jezikih
   - Tehnike za odpravljanje napak, testiranje in validacijo
   - Oblikovanje predlog pozivov in delovnih tokov za ponovno uporabo
   - Vzorčni projekti s primeri implementacije

6. **Napredne teme (05-AdvancedTopics/)**
   - Tehnike inženiringa konteksta
   - Integracija agentov Foundry
   - Delovni tokovi večmodalne umetne inteligence
   - Demosi avtentikacije OAuth2
   - Zmožnosti iskanja v realnem času
   - Pretakanje v realnem času
   - Implementacija osnovnih kontekstov
   - Strategije usmerjanja
   - Tehnike vzorčenja
   - Pristopi k skaliranju
   - Varnostni vidiki
   - Integracija varnosti Entra ID
   - Integracija spletnega iskanja

7. **Prispevki skupnosti (06-CommunityContributions/)**
   - Kako prispevati kodo in dokumentacijo
   - Sodelovanje prek GitHuba
   - Izboljšave in povratne informacije, ki jih vodi skupnost
   - Uporaba različnih MCP odjemalcev (Claude Desktop, Cline, VSCode)
   - Delo z priljubljenimi MCP strežniki, vključno z generiranjem slik

8. **Lekcije iz zgodnje uporabe (07-LessonsfromEarlyAdoption/)**
   - Implementacije v resničnem svetu in zgodbe o uspehu
   - Gradnja in uvajanje rešitev, ki temeljijo na MCP
   - Trendi in prihodnja načrtovanja
   - **Vodnik za Microsoft MCP strežnike**: Celovit vodnik za 10 produkcijsko pripravljenih Microsoft MCP strežnikov, vključno z:
     - Microsoft Learn Docs MCP strežnik
     - Azure MCP strežnik (15+ specializiranih konektorjev)
     - GitHub MCP strežnik
     - Azure DevOps MCP strežnik
     - MarkItDown MCP strežnik
     - SQL Server MCP strežnik
     - Playwright MCP strežnik
     - Dev Box MCP strežnik
     - Azure AI Foundry MCP strežnik
     - Microsoft 365 Agents Toolkit MCP strežnik

9. **Najboljše prakse (08-BestPractices/)**
   - Izboljšanje zmogljivosti in optimizacija
   - Oblikovanje sistemov MCP, odpornih na napake
   - Strategije testiranja in odpornosti

10. **Študije primerov (09-CaseStudy/)**
    - **Sedem celovitih študij primerov**, ki prikazujejo vsestranskost MCP v različnih scenarijih:
    - **Azure AI potovalni agenti**: Orkestracija več agentov z Azure OpenAI in AI Search
    - **Integracija Azure DevOps**: Avtomatizacija procesov delovnih tokov z YouTube posodobitvami podatkov
    - **Pridobivanje dokumentacije v realnem času**: Python konzolni odjemalec s pretakanjem HTTP
    - **Interaktivni generator študijskega načrta**: Chainlit spletna aplikacija s pogovorno umetno inteligenco
    - **Dokumentacija v urejevalniku**: Integracija VS Code z delovnimi tokovi GitHub Copilot
    - **Upravljanje API-jev Azure**: Integracija podjetniških API-jev z ustvarjanjem MCP strežnika
    - **GitHub MCP Register**: Razvoj ekosistema in platforma za integracijo agentov
    - Primeri implementacije, ki zajemajo integracijo v podjetjih, produktivnost razvijalcev in razvoj ekosistema

11. **Praktična delavnica (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Celovita praktična delavnica, ki združuje MCP z AI Toolkit
    - Gradnja inteligentnih aplikacij, ki povezujejo modele umetne inteligence z orodji iz resničnega sveta
    - Praktični moduli, ki pokrivajo osnove, razvoj prilagojenega strežnika in strategije uvajanja v produkcijo
    - **Struktura laboratorija**:
      - Laboratorij 1: Osnove MCP strežnika
      - Laboratorij 2: Napredni razvoj MCP strežnika
      - Laboratorij 3: Integracija AI Toolkit
      - Laboratorij 4: Uvajanje v produkcijo in skaliranje
    - Učenje na podlagi laboratorijev s korak-po-korak navodili

12. **Laboratoriji za integracijo MCP strežnika z bazo podatkov (11-MCPServerHandsOnLabs/)**
    - **Celovita učna pot s 13 laboratoriji** za gradnjo produkcijsko pripravljenih MCP strežnikov z integracijo PostgreSQL
    - **Implementacija analitike maloprodaje v resničnem svetu** z uporabo primera Zava Retail
    - **Vzorce na ravni podjetja**, vključno z varnostjo na ravni vrstic (RLS), semantičnim iskanjem in dostopom do podatkov za več najemnikov
    - **Celotna struktura laboratorija**:
      - **Laboratoriji 00-03: Osnove** - Uvod, Arhitektura, Varnost, Nastavitev okolja
      - **Laboratoriji 04-06: Gradnja MCP strežnika** - Oblikovanje baze podatkov, Implementacija MCP strežnika, Razvoj orodij
      - **Laboratoriji 07-09: Napredne funkcije** - Semantično iskanje, Testiranje in odpravljanje napak, Integracija z VS Code
      - **Laboratoriji 10-12: Produkcija in najboljše prakse** - Uvajanje, Spremljanje, Optimizacija
    - **Pokrite tehnologije**: FastMCP okvir, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Rezultati učenja**: Produkcijsko pripravljeni MCP strežniki, vzorci integracije baze podatkov, analitika, ki jo poganja umetna inteligenca, varnost na ravni podjetja

## Dodatni viri

Repozitorij vključuje podporne vire:

- **Mapa slik**: Vsebuje diagrame in ilustracije, uporabljene v učnem načrtu
- **Prevodi**: Podpora za več jezikov z avtomatiziranimi prevodi dokumentacije
- **Uradni viri MCP**:
  - [Dokumentacija MCP](https://modelcontextprotocol.io/)
  - [Specifikacija MCP](https://spec.modelcontextprotocol.io/)
  - [GitHub repozitorij MCP](https://github.com/modelcontextprotocol)

## Kako uporabljati ta repozitorij

1. **Zaporedno učenje**: Sledite poglavjem po vrsti (00 do 11) za strukturirano učno izkušnjo.
2. **Osredotočenost na specifičen jezik**: Če vas zanima določen programski jezik, raziščite mape z vzorci za implementacije v vašem priljubljenem jeziku.
3. **Praktična implementacija**: Začnite z razdelkom "Začetek", da nastavite svoje okolje in ustvarite svoj prvi MCP strežnik in odjemalec.
4. **Napredno raziskovanje**: Ko se seznanite z osnovami, se poglobite v napredne teme za širjenje znanja.
5. **Sodelovanje skupnosti**: Pridružite se skupnosti MCP prek razprav na GitHubu in kanalov Discord za povezovanje s strokovnjaki in drugimi razvijalci.

## MCP odjemalci in orodja

Učni načrt pokriva različne MCP odjemalce in orodja:

1. **Uradni odjemalci**:
   - Visual Studio Code 
   - MCP v Visual Studio Code
   - Claude Desktop
   - Claude v VSCode 
   - Claude API

2. **Odjemalci skupnosti**:
   - Cline (na osnovi terminala)
   - Cursor (urejevalnik kode)
   - ChatMCP
   - Windsurf

3. **Orodja za upravljanje MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Priljubljeni MCP strežniki

Repozitorij predstavlja različne MCP strežnike, vključno z:

1. **Uradni Microsoft MCP strežniki**:
   - Microsoft Learn Docs MCP strežnik
   - Azure MCP strežnik (15+ specializiranih konektorjev)
   - GitHub MCP strežnik
   - Azure DevOps MCP strežnik
   - MarkItDown MCP strežnik
   - SQL Server MCP strežnik
   - Playwright MCP strežnik
   - Dev Box MCP strežnik
   - Azure AI Foundry MCP strežnik
   - Microsoft 365 Agents Toolkit MCP strežnik

2. **Uradni referenčni strežniki**:
   - Datotečni sistem
   - Fetch
   - Pomnilnik
   - Sekvenčno razmišljanje

3. **Generiranje slik**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Razvojna orodja**:
   - Git MCP
   - Nadzor terminala
   - Pomočnik za kodo

5. **Specializirani strežniki**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Prispevanje

Ta repozitorij pozdravlja prispevke skupnosti. Oglejte si razdelek Prispevki skupnosti za smernice o tem, kako učinkovito prispevati k ekosistemu MCP.

----

*Ta vodnik za študij je bil posodobljen 6. oktobra 2025 in ponuja pregled repozitorija na ta datum. Vsebina repozitorija se lahko po tem datumu posodobi.*

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.