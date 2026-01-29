# Introduktion til Model Context Protocol (MCP): Hvorfor det er vigtigt for skalerbare AI-applikationer

[![Introduktion til Model Context Protocol](../../../translated_images/da/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Klik på billedet ovenfor for at se videoen til denne lektion)_

Generative AI-applikationer er et stort skridt fremad, da de ofte giver brugeren mulighed for at interagere med appen ved hjælp af naturlige sprogprompter. Men efterhånden som der investeres mere tid og ressourcer i sådanne apps, vil du gerne sikre, at du nemt kan integrere funktionaliteter og ressourcer på en måde, der gør det let at udvide, at din app kan understøtte flere modeller, og håndtere forskellige modeldetaljer. Kort sagt, det er nemt at komme i gang med at bygge Gen AI-apps, men når de vokser og bliver mere komplekse, skal du begynde at definere en arkitektur og sandsynligvis bruge en standard for at sikre, at dine apps bygges på en konsistent måde. Her kommer MCP ind i billedet for at organisere tingene og give en standard.

---

## **🔍 Hvad er Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** er en **åben, standardiseret grænseflade**, der gør det muligt for Large Language Models (LLMs) at interagere problemfrit med eksterne værktøjer, API'er og datakilder. Det giver en konsistent arkitektur, der forbedrer AI-modellernes funktionalitet ud over deres træningsdata, hvilket muliggør smartere, skalerbare og mere responsive AI-systemer.

---

## **🎯 Hvorfor standardisering i AI er vigtigt**

Efterhånden som generative AI-applikationer bliver mere komplekse, er det afgørende at vedtage standarder, der sikrer **skalerbarhed, udvidelsesmuligheder, vedligeholdelse** og **undgåelse af leverandørbinding**. MCP adresserer disse behov ved at:

- Forene model-værktøjsintegrationer
- Reducere skrøbelige, engangs tilpassede løsninger
- Muliggøre, at flere modeller fra forskellige leverandører kan sameksistere i ét økosystem

**Note:** Selvom MCP præsenterer sig som en åben standard, er der ingen planer om at standardisere MCP gennem eksisterende standardiseringsorganer som IEEE, IETF, W3C, ISO eller andre.

---

## **📚 Læringsmål**

Ved slutningen af denne artikel vil du kunne:

- Definere **Model Context Protocol (MCP)** og dens anvendelsesområder
- Forstå, hvordan MCP standardiserer kommunikation mellem modeller og værktøjer
- Identificere de centrale komponenter i MCP-arkitekturen
- Udforske virkelige anvendelser af MCP i erhvervs- og udviklingskontekster

---

## **💡 Hvorfor Model Context Protocol (MCP) er en game-changer**

### **🔗 MCP løser fragmentering i AI-interaktioner**

Før MCP krævede integration af modeller med værktøjer:

- Tilpasset kode for hvert værktøjs-modelpar
- Ikke-standardiserede API'er for hver leverandør
- Hyppige fejl på grund af opdateringer
- Dårlig skalerbarhed med flere værktøjer

### **✅ Fordele ved MCP-standardisering**

| **Fordel**                | **Beskrivelse**                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Interoperabilitet         | LLM'er fungerer problemfrit med værktøjer fra forskellige leverandører         |
| Konsistens                | Ensartet adfærd på tværs af platforme og værktøjer                             |
| Genanvendelighed          | Værktøjer bygget én gang kan bruges på tværs af projekter og systemer          |
| Hurtigere udvikling       | Reducer udviklingstid ved at bruge standardiserede, plug-and-play-grænseflader |

---

## **🧱 Overblik over MCP-arkitektur på højt niveau**

MCP følger en **klient-server-model**, hvor:

- **MCP Hosts** kører AI-modellerne
- **MCP Clients** initierer forespørgsler
- **MCP Servers** leverer kontekst, værktøjer og funktioner

### **Nøglekomponenter:**

- **Ressourcer** – Statisk eller dynamisk data til modeller  
- **Prompter** – Foruddefinerede workflows til guidet generering  
- **Værktøjer** – Udførbare funktioner som søgning, beregninger  
- **Sampling** – Agentisk adfærd via rekursive interaktioner

---

## Hvordan MCP-servere fungerer

MCP-servere opererer på følgende måde:

- **Forespørgselsflow**:
    1. En forespørgsel initieres af en slutbruger eller software, der handler på deres vegne.
    2. **MCP Client** sender forespørgslen til en **MCP Host**, som administrerer AI-modelens runtime.
    3. **AI-modellen** modtager brugerens prompt og kan anmode om adgang til eksterne værktøjer eller data via en eller flere værktøjskald.
    4. **MCP Host**, ikke modellen direkte, kommunikerer med de relevante **MCP Server(e)** ved hjælp af den standardiserede protokol.
- **MCP Host-funktionalitet**:
    - **Værktøjsregister**: Vedligeholder en katalog over tilgængelige værktøjer og deres funktioner.
    - **Autentifikation**: Bekræfter tilladelser til værktøjsadgang.
    - **Forespørgselsbehandler**: Behandler indkommende værktøjsanmodninger fra modellen.
    - **Responsformatter**: Strukturerer værktøjsoutput i et format, modellen kan forstå.
- **MCP Server-udførelse**:
    - **MCP Host** videresender værktøjsanmodninger til en eller flere **MCP Servere**, som hver især eksponerer specialiserede funktioner (f.eks. søgning, beregninger, databaseforespørgsler).
    - **MCP Servere** udfører deres respektive operationer og returnerer resultater til **MCP Host** i et konsistent format.
    - **MCP Host** formaterer og videresender disse resultater til **AI-modellen**.
- **Responsafslutning**:
    - **AI-modellen** inkorporerer værktøjsoutput i en endelig respons.
    - **MCP Host** sender denne respons tilbage til **MCP Client**, som leverer den til slutbrugeren eller den kaldende software.

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Client/Application] -->|Sends Request| H[MCP Host]
    H -->|Invokes| A[AI Model]
    A -->|Tool Call Request| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Web Search]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Calculator tool]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Database Access tool]
    H -->|MCP Protocol| T4[MCP Server Tool 04: File System tool]
    H -->|Sends Response| Client

    subgraph "MCP Host Components"
        H
        G[Tool Registry]
        I[Authentication]
        J[Request Handler]
        K[Response Formatter]
    end

    H <--> G
    H <--> I
    H <--> J
    H <--> K

    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style H fill:#eeeeee,stroke:#333,stroke-width:2px
    style Client fill:#d5e8f9,stroke:#333,stroke-width:2px
    style G fill:#fffbe6,stroke:#333,stroke-width:1px
    style I fill:#fffbe6,stroke:#333,stroke-width:1px
    style J fill:#fffbe6,stroke:#333,stroke-width:1px
    style K fill:#fffbe6,stroke:#333,stroke-width:1px
    style T1 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T2 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T3 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T4 fill:#c2f0c2,stroke:#333,stroke-width:1px
```

## 👨‍💻 Sådan bygger du en MCP-server (med eksempler)

MCP-servere giver dig mulighed for at udvide LLM-funktioner ved at levere data og funktionalitet.

Klar til at prøve det? Her er sprog- og/eller stack-specifikke SDK'er med eksempler på oprettelse af simple MCP-servere i forskellige sprog/stacks:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk

## 🌍 Virkelige anvendelser af MCP

MCP muliggør en bred vifte af applikationer ved at udvide AI-funktioner:

| **Applikation**            | **Beskrivelse**                                                                |
|----------------------------|--------------------------------------------------------------------------------|
| Integration af virksomhedsdata | Forbind LLM'er til databaser, CRM'er eller interne værktøjer                  |
| Agentiske AI-systemer       | Muliggør autonome agenter med værktøjsadgang og beslutningsarbejdsflows         |
| Multimodale applikationer   | Kombiner tekst-, billede- og lydværktøjer i én samlet AI-app                    |
| Integration af realtidsdata | Bring live data ind i AI-interaktioner for mere præcise, aktuelle outputs       |

### 🧠 MCP = Universel standard for AI-interaktioner

Model Context Protocol (MCP) fungerer som en universel standard for AI-interaktioner, ligesom USB-C standardiserede fysiske forbindelser for enheder. I AI-verdenen giver MCP en konsistent grænseflade, der gør det muligt for modeller (klienter) at integrere problemfrit med eksterne værktøjer og dataleverandører (servere). Dette eliminerer behovet for diverse, tilpassede protokoller for hver API eller datakilde.

Under MCP følger et MCP-kompatibelt værktøj (kaldet en MCP-server) en ensartet standard. Disse servere kan liste de værktøjer eller handlinger, de tilbyder, og udføre disse handlinger, når de anmodes af en AI-agent. AI-agentplatforme, der understøtter MCP, er i stand til at opdage tilgængelige værktøjer fra serverne og kalde dem via denne standardprotokol.

### 💡 Muliggør adgang til viden

Ud over at tilbyde værktøjer muliggør MCP også adgang til viden. Det gør det muligt for applikationer at give kontekst til store sprogmodeller (LLMs) ved at forbinde dem til forskellige datakilder. For eksempel kan en MCP-server repræsentere en virksomheds dokumentarkiv, hvilket gør det muligt for agenter at hente relevant information efter behov. En anden server kunne håndtere specifikke handlinger som at sende e-mails eller opdatere poster. Fra agentens perspektiv er disse blot værktøjer, den kan bruge—nogle værktøjer returnerer data (videnskontekst), mens andre udfører handlinger. MCP administrerer begge dele effektivt.

En agent, der forbinder til en MCP-server, lærer automatisk serverens tilgængelige funktioner og tilgængelige data gennem et standardformat. Denne standardisering muliggør dynamisk værktøjstilgængelighed. For eksempel gør tilføjelsen af en ny MCP-server til en agents system dens funktioner straks anvendelige uden behov for yderligere tilpasning af agentens instruktioner.

Denne strømlinede integration stemmer overens med flowet vist i det følgende diagram, hvor servere leverer både værktøjer og viden, hvilket sikrer problemfri samarbejde på tværs af systemer.

### 👉 Eksempel: Skalerbar agentløsning

```mermaid
---
title: Scalable Agent Solution with MCP
description: A diagram illustrating how a user interacts with an LLM that connects to multiple MCP servers, with each server providing both knowledge and tools, creating a scalable AI system architecture
---
graph TD
    User -->|Prompt| LLM
    LLM -->|Response| User
    LLM -->|MCP| ServerA
    LLM -->|MCP| ServerB
    ServerA -->|Universal connector| ServerB
    ServerA --> KnowledgeA
    ServerA --> ToolsA
    ServerB --> KnowledgeB
    ServerB --> ToolsB

    subgraph Server A
        KnowledgeA[Knowledge]
        ToolsA[Tools]
    end

    subgraph Server B
        KnowledgeB[Knowledge]
        ToolsB[Tools]
    end
```
Den universelle connector gør det muligt for MCP-servere at kommunikere og dele funktioner med hinanden, hvilket gør det muligt for ServerA at delegere opgaver til ServerB eller få adgang til dens værktøjer og viden. Dette federerer værktøjer og data på tværs af servere og understøtter skalerbare og modulære agentarkitekturer. Fordi MCP standardiserer værktøjseksponering, kan agenter dynamisk opdage og dirigere forespørgsler mellem servere uden hårdkodede integrationer.

Værktøjs- og vidensfederation: Værktøjer og data kan tilgås på tværs af servere, hvilket muliggør mere skalerbare og modulære agentiske arkitekturer.

### 🔄 Avancerede MCP-scenarier med klient-side LLM-integration

Ud over den grundlæggende MCP-arkitektur er der avancerede scenarier, hvor både klient og server indeholder LLM'er, hvilket muliggør mere sofistikerede interaktioner. I det følgende diagram kunne **Client App** være en IDE med en række MCP-værktøjer tilgængelige for brug af LLM:

```mermaid
---
title: Advanced MCP Scenarios with Client-Server LLM Integration
description: A sequence diagram showing the detailed interaction flow between user, client application, client LLM, multiple MCP servers, and server LLM, illustrating tool discovery, user interaction, direct tool calling, and feature negotiation phases
---
sequenceDiagram
    autonumber
    actor User as 👤 User
    participant ClientApp as 🖥️ Client App
    participant ClientLLM as 🧠 Client LLM
    participant Server1 as 🔧 MCP Server 1
    participant Server2 as 📚 MCP Server 2
    participant ServerLLM as 🤖 Server LLM
    
    %% Discovery Phase
    rect rgb(220, 240, 255)
        Note over ClientApp, Server2: TOOL DISCOVERY PHASE
        ClientApp->>+Server1: Request available tools/resources
        Server1-->>-ClientApp: Return tool list (JSON)
        ClientApp->>+Server2: Request available tools/resources
        Server2-->>-ClientApp: Return tool list (JSON)
        Note right of ClientApp: Store combined tool<br/>catalog locally
    end
    
    %% User Interaction
    rect rgb(255, 240, 220)
        Note over User, ClientLLM: USER INTERACTION PHASE
        User->>+ClientApp: Enter natural language prompt
        ClientApp->>+ClientLLM: Forward prompt + tool catalog
        ClientLLM->>-ClientLLM: Analyze prompt & select tools
    end
    
    %% Scenario A: Direct Tool Calling
    alt Direct Tool Calling
        rect rgb(220, 255, 220)
            Note over ClientApp, Server1: SCENARIO A: DIRECT TOOL CALLING
            ClientLLM->>+ClientApp: Request tool execution
            ClientApp->>+Server1: Execute specific tool
            Server1-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    
    %% Scenario B: Feature Negotiation (VS Code style)
    else Feature Negotiation (VS Code style)
        rect rgb(255, 220, 220)
            Note over ClientApp, ServerLLM: SCENARIO B: FEATURE NEGOTIATION
            ClientLLM->>+ClientApp: Identify needed capabilities
            ClientApp->>+Server2: Negotiate features/capabilities
            Server2->>+ServerLLM: Request additional context
            ServerLLM-->>-Server2: Provide context
            Server2-->>-ClientApp: Return available features
            ClientApp->>+Server2: Call negotiated tools
            Server2-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    end
```

## 🔐 Praktiske fordele ved MCP

Her er de praktiske fordele ved at bruge MCP:

- **Aktualitet**: Modeller kan få adgang til opdateret information ud over deres træningsdata
- **Udvidelse af kapabiliteter**: Modeller kan udnytte specialiserede værktøjer til opgaver, de ikke er trænet til
- **Reducerede hallucinationer**: Eksterne datakilder giver faktuel forankring
- **Privatliv**: Følsomme data kan forblive inden for sikre miljøer i stedet for at blive indlejret i prompter

## 📌 Nøglepunkter

Følgende er nøglepunkter for brug af MCP:

- **MCP** standardiserer, hvordan AI-modeller interagerer med værktøjer og data
- Fremmer **udvidelsesmuligheder, konsistens og interoperabilitet**
- MCP hjælper med at **reducere udviklingstid, forbedre pålidelighed og udvide modelkapabiliteter**
- Klient-server-arkitekturen **muliggør fleksible, udvidelige AI-applikationer**

## 🧠 Øvelse

Tænk på en AI-applikation, du er interesseret i at bygge.

- Hvilke **eksterne værktøjer eller data** kunne forbedre dens kapabiliteter?
- Hvordan kunne MCP gøre integrationen **simplere og mere pålidelig?**

## Yderligere ressourcer

- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

## Hvad er næste skridt

Næste: [Kapitel 1: Kernekoncepter](../01-CoreConcepts/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.