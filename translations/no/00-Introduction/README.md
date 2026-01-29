# Introduksjon til Model Context Protocol (MCP): Hvorfor det er viktig for skalerbare AI-applikasjoner

[![Introduksjon til Model Context Protocol](../../../translated_images/no/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Klikk på bildet over for å se videoen til denne leksjonen)_

Generative AI-applikasjoner er et stort fremskritt, da de ofte lar brukeren samhandle med appen ved hjelp av naturlige språkkommandoer. Men etter hvert som mer tid og ressurser investeres i slike apper, vil du sørge for at du enkelt kan integrere funksjonaliteter og ressurser på en måte som gjør det lett å utvide, at appen din kan støtte flere modeller samtidig, og håndtere ulike modellspesifikasjoner. Kort sagt, det er enkelt å starte med å bygge generative AI-apper, men etter hvert som de vokser og blir mer komplekse, må du begynne å definere en arkitektur og sannsynligvis bruke en standard for å sikre at appene dine bygges på en konsistent måte. Det er her MCP kommer inn for å organisere ting og tilby en standard.

---

## **🔍 Hva er Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** er et **åpent, standardisert grensesnitt** som lar store språkmodeller (LLMs) samhandle sømløst med eksterne verktøy, API-er og datakilder. Det gir en konsistent arkitektur for å forbedre AI-modellers funksjonalitet utover deres treningsdata, og muliggjør smartere, skalerbare og mer responsive AI-systemer.

---

## **🎯 Hvorfor standardisering i AI er viktig**

Etter hvert som generative AI-applikasjoner blir mer komplekse, er det avgjørende å ta i bruk standarder som sikrer **skalerbarhet, utvidbarhet, vedlikeholdbarhet** og **unngå leverandørbinding**. MCP adresserer disse behovene ved å:

- Forene integrasjoner mellom modeller og verktøy
- Redusere skjøre, engangsløsninger
- Tillate flere modeller fra ulike leverandører å eksistere innenfor ett økosystem

**Merk:** Selv om MCP markedsfører seg som en åpen standard, er det ingen planer om å standardisere MCP gjennom eksisterende standardiseringsorganer som IEEE, IETF, W3C, ISO eller andre.

---

## **📚 Læringsmål**

Ved slutten av denne artikkelen vil du kunne:

- Definere **Model Context Protocol (MCP)** og dens bruksområder
- Forstå hvordan MCP standardiserer kommunikasjon mellom modeller og verktøy
- Identifisere de viktigste komponentene i MCP-arkitekturen
- Utforske virkelige anvendelser av MCP i bedrifts- og utviklingskontekster

---

## **💡 Hvorfor Model Context Protocol (MCP) er en revolusjonerende løsning**

### **🔗 MCP løser fragmentering i AI-interaksjoner**

Før MCP krevde integrering av modeller med verktøy:

- Egendefinert kode for hvert verktøy-modell-par
- Ikke-standardiserte API-er for hver leverandør
- Hyppige feil på grunn av oppdateringer
- Dårlig skalerbarhet med flere verktøy

### **✅ Fordeler med MCP-standardisering**

| **Fordel**                | **Beskrivelse**                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Interoperabilitet         | LLMs fungerer sømløst med verktøy fra ulike leverandører                       |
| Konsistens                | Ensartet oppførsel på tvers av plattformer og verktøy                          |
| Gjenbrukbarhet            | Verktøy bygget én gang kan brukes på tvers av prosjekter og systemer           |
| Akselerert utvikling      | Reduser utviklingstid ved å bruke standardiserte, plug-and-play-grensesnitt    |

---

## **🧱 Oversikt over MCP-arkitektur på høyt nivå**

MCP følger en **klient-server-modell**, hvor:

- **MCP Hosts** kjører AI-modellene
- **MCP Clients** initierer forespørsler
- **MCP Servers** leverer kontekst, verktøy og funksjoner

### **Nøkkelkomponenter:**

- **Ressurser** – Statisk eller dynamisk data for modeller  
- **Prompter** – Forhåndsdefinerte arbeidsflyter for veiledet generering  
- **Verktøy** – Utførbare funksjoner som søk, beregninger  
- **Sampling** – Agentisk oppførsel via rekursive interaksjoner

---

## Hvordan MCP-servere fungerer

MCP-servere opererer på følgende måte:

- **Forespørselsflyt**:
    1. En forespørsel initieres av en sluttbruker eller programvare som handler på deres vegne.
    2. **MCP-klienten** sender forespørselen til en **MCP Host**, som administrerer AI-modellens runtime.
    3. **AI-modellen** mottar brukerens prompt og kan be om tilgang til eksterne verktøy eller data via ett eller flere verktøykall.
    4. **MCP Host**, ikke modellen direkte, kommuniserer med de relevante **MCP-serverne** ved hjelp av den standardiserte protokollen.
- **MCP Host-funksjonalitet**:
    - **Verktøyregister**: Opprettholder en katalog over tilgjengelige verktøy og deres funksjoner.
    - **Autentisering**: Verifiserer tillatelser for verktøytilgang.
    - **Forespørselshåndtering**: Behandler innkommende verktøykall fra modellen.
    - **Responsformatter**: Strukturerer verktøyutganger i et format modellen kan forstå.
- **MCP Server-utførelse**:
    - **MCP Host** ruter verktøykall til én eller flere **MCP-servere**, som hver eksponerer spesialiserte funksjoner (f.eks. søk, beregninger, databaseforespørsler).
    - **MCP-serverne** utfører sine respektive operasjoner og returnerer resultater til **MCP Host** i et konsistent format.
    - **MCP Host** formaterer og videresender disse resultatene til **AI-modellen**.
- **Responsfullføring**:
    - **AI-modellen** inkorporerer verktøyutgangene i en endelig respons.
    - **MCP Host** sender denne responsen tilbake til **MCP-klienten**, som leverer den til sluttbrukeren eller den kallende programvaren.

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

## 👨‍💻 Hvordan bygge en MCP-server (med eksempler)

MCP-servere lar deg utvide LLM-funksjonalitet ved å tilby data og funksjoner.

Klar til å prøve det? Her er språk- og/eller stack-spesifikke SDK-er med eksempler på hvordan du lager enkle MCP-servere i forskjellige språk/stakker:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk


## 🌍 Virkelige bruksområder for MCP

MCP muliggjør et bredt spekter av applikasjoner ved å utvide AI-funksjonalitet:

| **Applikasjon**             | **Beskrivelse**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| Integrasjon av bedriftsdata | Koble LLMs til databaser, CRM-er eller interne verktøy                         |
| Agentiske AI-systemer       | Muliggjør autonome agenter med verktøystilgang og beslutningsarbeidsflyter     |
| Multimodale applikasjoner   | Kombiner tekst-, bilde- og lydverktøy i én samlet AI-app                      |
| Sanntidsdataintegrasjon     | Bring live data inn i AI-interaksjoner for mer nøyaktige, oppdaterte resultater|

### 🧠 MCP = Universell standard for AI-interaksjoner

Model Context Protocol (MCP) fungerer som en universell standard for AI-interaksjoner, på samme måte som USB-C standardiserte fysiske tilkoblinger for enheter. I AI-verdenen gir MCP et konsistent grensesnitt som lar modeller (klienter) integrere sømløst med eksterne verktøy og dataleverandører (servere). Dette eliminerer behovet for diverse, egendefinerte protokoller for hver API eller datakilde.

Under MCP følger et MCP-kompatibelt verktøy (referert til som en MCP-server) en enhetlig standard. Disse serverne kan liste opp verktøyene eller handlingene de tilbyr og utføre disse handlingene når de blir bedt om det av en AI-agent. AI-agentplattformer som støtter MCP er i stand til å oppdage tilgjengelige verktøy fra serverne og bruke dem gjennom denne standardprotokollen.

### 💡 Tilrettelegger for tilgang til kunnskap

I tillegg til å tilby verktøy, tilrettelegger MCP også for tilgang til kunnskap. Det gjør det mulig for applikasjoner å gi kontekst til store språkmodeller (LLMs) ved å koble dem til ulike datakilder. For eksempel kan en MCP-server representere et selskaps dokumentarkiv, slik at agenter kan hente relevant informasjon på forespørsel. En annen server kan håndtere spesifikke handlinger som å sende e-poster eller oppdatere poster. Fra agentens perspektiv er dette bare verktøy den kan bruke—noen verktøy returnerer data (kunnskapskontekst), mens andre utfører handlinger. MCP administrerer begge effektivt.

En agent som kobler seg til en MCP-server lærer automatisk serverens tilgjengelige funksjoner og tilgjengelige data gjennom et standardformat. Denne standardiseringen muliggjør dynamisk verktøytilgjengelighet. For eksempel gjør det å legge til en ny MCP-server i agentens system dens funksjoner umiddelbart brukbare uten behov for ytterligere tilpasning av agentens instruksjoner.

Denne strømlinjeformede integrasjonen samsvarer med flyten som er avbildet i følgende diagram, der servere tilbyr både verktøy og kunnskap, og sikrer sømløst samarbeid på tvers av systemer.

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
Den universelle koblingen gjør det mulig for MCP-servere å kommunisere og dele funksjoner med hverandre, slik at ServerA kan delegere oppgaver til ServerB eller få tilgang til dens verktøy og kunnskap. Dette federerer verktøy og data på tvers av servere, og støtter skalerbare og modulære agentarkitekturer. Fordi MCP standardiserer verktøyeksponering, kan agenter dynamisk oppdage og rute forespørsler mellom servere uten hardkodede integrasjoner.

Federering av verktøy og kunnskap: Verktøy og data kan nås på tvers av servere, noe som muliggjør mer skalerbare og modulære agentiske arkitekturer.

### 🔄 Avanserte MCP-scenarier med klientbasert LLM-integrasjon

Utover den grunnleggende MCP-arkitekturen finnes det avanserte scenarier der både klient og server inneholder LLMs, noe som muliggjør mer sofistikerte interaksjoner. I følgende diagram kan **Client App** være en IDE med en rekke MCP-verktøy tilgjengelig for bruk av LLM:

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

## 🔐 Praktiske fordeler med MCP

Her er de praktiske fordelene ved å bruke MCP:

- **Oppdatert informasjon**: Modeller kan få tilgang til oppdatert informasjon utover deres treningsdata
- **Utvidet funksjonalitet**: Modeller kan bruke spesialiserte verktøy for oppgaver de ikke er trent for
- **Reduserte hallusinasjoner**: Eksterne datakilder gir faktagrunnlag
- **Personvern**: Sensitiv data kan forbli innenfor sikre miljøer i stedet for å bli innebygd i prompter

## 📌 Viktige punkter

Følgende er viktige punkter for bruk av MCP:

- **MCP** standardiserer hvordan AI-modeller samhandler med verktøy og data
- Fremmer **utvidbarhet, konsistens og interoperabilitet**
- MCP hjelper med **å redusere utviklingstid, forbedre pålitelighet og utvide modellens funksjonalitet**
- Klient-server-arkitekturen **muliggjør fleksible, utvidbare AI-applikasjoner**

## 🧠 Øvelse

Tenk på en AI-applikasjon du er interessert i å bygge.

- Hvilke **eksterne verktøy eller data** kan forbedre dens funksjonalitet?
- Hvordan kan MCP gjøre integrasjonen **enklere og mer pålitelig?**

## Tilleggsressurser

- [MCP GitHub Repository](https://github.com/modelcontextprotocol)


## Hva skjer videre

Neste: [Kapittel 1: Grunnleggende konsepter](../01-CoreConcepts/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.