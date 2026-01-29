# Introduktion till Model Context Protocol (MCP): Varför det är viktigt för skalbara AI-applikationer

[![Introduktion till Model Context Protocol](../../../translated_images/sv/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Klicka på bilden ovan för att se videon för denna lektion)_

Generativa AI-applikationer är ett stort framsteg eftersom de ofta låter användaren interagera med appen genom naturliga språkkommandon. Men när mer tid och resurser investeras i sådana appar vill du säkerställa att du enkelt kan integrera funktioner och resurser på ett sätt som gör det enkelt att utöka, att din app kan hantera mer än en modell och hantera olika modellkomplexiteter. Kort sagt, att bygga generativa AI-appar är enkelt att börja med, men när de växer och blir mer komplexa behöver du börja definiera en arkitektur och kommer sannolikt att behöva förlita dig på en standard för att säkerställa att dina appar byggs på ett konsekvent sätt. Här kommer MCP in för att organisera saker och tillhandahålla en standard.

---

## **🔍 Vad är Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** är ett **öppet, standardiserat gränssnitt** som gör det möjligt för stora språkmodeller (LLMs) att interagera smidigt med externa verktyg, API:er och datakällor. Det erbjuder en konsekvent arkitektur för att förbättra AI-modellens funktionalitet bortom dess träningsdata, vilket möjliggör smartare, skalbara och mer responsiva AI-system.

---

## **🎯 Varför standardisering inom AI är viktigt**

När generativa AI-applikationer blir mer komplexa är det avgörande att anta standarder som säkerställer **skalbarhet, utbyggbarhet, underhållbarhet** och **undvikande av leverantörsinlåsning**. MCP adresserar dessa behov genom att:

- Enhetliggöra integrationer mellan modeller och verktyg
- Minska sköra, engångslösningar
- Tillåta flera modeller från olika leverantörer att samexistera inom ett ekosystem

**Note:** Även om MCP marknadsför sig som en öppen standard finns det inga planer på att standardisera MCP genom befintliga standardiseringsorgan som IEEE, IETF, W3C, ISO eller något annat standardiseringsorgan.

---

## **📚 Lärandemål**

Efter att ha läst denna artikel kommer du att kunna:

- Definiera **Model Context Protocol (MCP)** och dess användningsområden
- Förstå hur MCP standardiserar kommunikation mellan modeller och verktyg
- Identifiera kärnkomponenterna i MCP-arkitekturen
- Utforska verkliga tillämpningar av MCP inom företag och utvecklingssammanhang

---

## **💡 Varför Model Context Protocol (MCP) är en spelväxlare**

### **🔗 MCP löser fragmentering i AI-interaktioner**

Innan MCP krävde integrering av modeller med verktyg:

- Anpassad kod för varje verktyg-modellpar
- Icke-standardiserade API:er för varje leverantör
- Frekventa avbrott på grund av uppdateringar
- Dålig skalbarhet med fler verktyg

### **✅ Fördelar med MCP-standardisering**

| **Fördel**                 | **Beskrivning**                                                                |
|----------------------------|--------------------------------------------------------------------------------|
| Interoperabilitet          | LLMs fungerar smidigt med verktyg från olika leverantörer                      |
| Konsekvens                 | Enhetligt beteende över plattformar och verktyg                                |
| Återanvändbarhet           | Verktyg byggda en gång kan användas över projekt och system                    |
| Accelererad utveckling     | Minska utvecklingstid genom att använda standardiserade, plug-and-play-gränssnitt |

---

## **🧱 Översikt över MCP-arkitektur på hög nivå**

MCP följer en **klient-server-modell**, där:

- **MCP Hosts** kör AI-modellerna
- **MCP Clients** initierar förfrågningar
- **MCP Servers** tillhandahåller kontext, verktyg och funktioner

### **Nyckelkomponenter:**

- **Resurser** – Statisk eller dynamisk data för modeller  
- **Prompter** – Fördefinierade arbetsflöden för styrd generering  
- **Verktyg** – Exekverbara funktioner som sökning, beräkningar  
- **Sampling** – Agentiskt beteende via rekursiva interaktioner

---

## Hur MCP-servrar fungerar

MCP-servrar fungerar på följande sätt:

- **Förfrågningsflöde**:
    1. En förfrågan initieras av en slutanvändare eller mjukvara som agerar på deras vägnar.
    2. **MCP Client** skickar förfrågan till en **MCP Host**, som hanterar AI-modellens runtime.
    3. **AI-modellen** tar emot användarens prompt och kan begära åtkomst till externa verktyg eller data via ett eller flera verktygsanrop.
    4. **MCP Host**, inte modellen direkt, kommunicerar med lämpliga **MCP Server(s)** via det standardiserade protokollet.
- **MCP Hosts funktionalitet**:
    - **Verktygsregister**: Håller en katalog över tillgängliga verktyg och deras funktioner.
    - **Autentisering**: Verifierar behörigheter för verktygsåtkomst.
    - **Förfrågningshanterare**: Bearbetar inkommande verktygsförfrågningar från modellen.
    - **Svarformatterare**: Strukturerar verktygsutdata i ett format som modellen kan förstå.
- **MCP Server-exekvering**:
    - **MCP Host** dirigerar verktygsanrop till en eller flera **MCP Servers**, som var och en exponerar specialiserade funktioner (t.ex. sökning, beräkningar, databasfrågor).
    - **MCP Servers** utför sina respektive operationer och returnerar resultat till **MCP Host** i ett konsekvent format.
    - **MCP Host** formaterar och vidarebefordrar dessa resultat till **AI-modellen**.
- **Slutförande av svar**:
    - **AI-modellen** integrerar verktygsutdata i ett slutgiltigt svar.
    - **MCP Host** skickar detta svar tillbaka till **MCP Client**, som levererar det till slutanvändaren eller den anropande mjukvaran.

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

## 👨‍💻 Hur man bygger en MCP-server (med exempel)

MCP-servrar gör det möjligt att utöka LLM-funktioner genom att tillhandahålla data och funktionalitet.

Redo att prova? Här är språk- och/eller stack-specifika SDK:er med exempel på hur man skapar enkla MCP-servrar i olika språk/stacks:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk

## 🌍 Verkliga användningsområden för MCP

MCP möjliggör en mängd olika applikationer genom att utöka AI-funktioner:

| **Applikation**             | **Beskrivning**                                                                |
|-----------------------------|--------------------------------------------------------------------------------|
| Företagsdataintegration     | Koppla LLMs till databaser, CRM-system eller interna verktyg                   |
| Agentiska AI-system         | Möjliggör autonoma agenter med verktygsåtkomst och beslutsarbetsflöden         |
| Multimodala applikationer   | Kombinera text-, bild- och ljudverktyg inom en enda enhetlig AI-app             |
| Realtidsdataintegration     | Ta in live-data i AI-interaktioner för mer exakta, aktuella resultat            |

### 🧠 MCP = Universell standard för AI-interaktioner

Model Context Protocol (MCP) fungerar som en universell standard för AI-interaktioner, ungefär som USB-C standardiserade fysiska anslutningar för enheter. I AI-världen tillhandahåller MCP ett konsekvent gränssnitt som gör det möjligt för modeller (klienter) att integrera smidigt med externa verktyg och dataleverantörer (servrar). Detta eliminerar behovet av olika, anpassade protokoll för varje API eller datakälla.

Under MCP följer ett MCP-kompatibelt verktyg (kallat MCP-server) en enhetlig standard. Dessa servrar kan lista de verktyg eller åtgärder de erbjuder och utföra dessa åtgärder när de begärs av en AI-agent. AI-agentplattformar som stöder MCP kan upptäcka tillgängliga verktyg från servrarna och anropa dem via detta standardprotokoll.

### 💡 Underlättar åtkomst till kunskap

Utöver att erbjuda verktyg underlättar MCP också åtkomst till kunskap. Det gör det möjligt för applikationer att tillhandahålla kontext till stora språkmodeller (LLMs) genom att länka dem till olika datakällor. Till exempel kan en MCP-server representera ett företags dokumentarkiv, vilket gör det möjligt för agenter att hämta relevant information vid behov. En annan server kan hantera specifika åtgärder som att skicka e-post eller uppdatera register. För agenten är dessa helt enkelt verktyg den kan använda—vissa verktyg returnerar data (kunskapskontext), medan andra utför åtgärder. MCP hanterar båda effektivt.

En agent som ansluter till en MCP-server lär sig automatiskt serverns tillgängliga funktioner och åtkomliga data genom ett standardformat. Denna standardisering möjliggör dynamisk verktygstillgänglighet. Till exempel gör tillägget av en ny MCP-server till en agents system dess funktioner omedelbart användbara utan att kräva ytterligare anpassning av agentens instruktioner.

Denna strömlinjeformade integration överensstämmer med flödet som visas i följande diagram, där servrar tillhandahåller både verktyg och kunskap, vilket säkerställer smidigt samarbete över system.

### 👉 Exempel: Skalbar agentlösning

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
Den universella anslutaren gör det möjligt för MCP-servrar att kommunicera och dela funktioner med varandra, vilket gör att ServerA kan delegera uppgifter till ServerB eller få åtkomst till dess verktyg och kunskap. Detta federerar verktyg och data över servrar, vilket stödjer skalbara och modulära agentarkitekturer. Eftersom MCP standardiserar verktygsexponering kan agenter dynamiskt upptäcka och dirigera förfrågningar mellan servrar utan hårdkodade integrationer.

Federering av verktyg och kunskap: Verktyg och data kan nås över servrar, vilket möjliggör mer skalbara och modulära agentiska arkitekturer.

### 🔄 Avancerade MCP-scenarier med klientbaserad LLM-integration

Utöver den grundläggande MCP-arkitekturen finns det avancerade scenarier där både klient och server innehåller LLMs, vilket möjliggör mer sofistikerade interaktioner. I följande diagram kan **Client App** vara en IDE med ett antal MCP-verktyg tillgängliga för användning av LLM:

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

## 🔐 Praktiska fördelar med MCP

Här är de praktiska fördelarna med att använda MCP:

- **Aktualitet**: Modeller kan få tillgång till aktuell information bortom deras träningsdata
- **Kapacitetsutvidgning**: Modeller kan använda specialiserade verktyg för uppgifter de inte tränats för
- **Minskade hallucinationer**: Externa datakällor ger faktagrund
- **Integritet**: Känslig data kan förbli inom säkra miljöer istället för att integreras i prompts

## 📌 Viktiga insikter

Följande är viktiga insikter för att använda MCP:

- **MCP** standardiserar hur AI-modeller interagerar med verktyg och data
- Främjar **utbyggbarhet, konsekvens och interoperabilitet**
- MCP hjälper till att **minska utvecklingstid, förbättra tillförlitlighet och utöka modellens kapaciteter**
- Klient-server-arkitekturen **möjliggör flexibla, utbyggbara AI-applikationer**

## 🧠 Övning

Tänk på en AI-applikation du är intresserad av att bygga.

- Vilka **externa verktyg eller data** skulle kunna förbättra dess kapaciteter?
- Hur kan MCP göra integrationen **enklare och mer tillförlitlig?**

## Ytterligare resurser

- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

## Vad händer härnäst

Nästa: [Kapitel 1: Kärnkoncept](../01-CoreConcepts/README.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.