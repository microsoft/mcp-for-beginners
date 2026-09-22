# Introduktion till Model Context Protocol (MCP): Varför det är viktigt för skalbara AI-applikationer

[![Introduction to Model Context Protocol](../../../translated_images/sv/01.a467036d886b5fb5.webp)](https://youtu.be/agBbdiOPLQA)

_(Klicka på bilden ovan för att se videon för denna lektion)_

Generativa AI-applikationer är ett stort steg framåt eftersom de ofta låter användaren interagera med appen via naturliga språkpromptar. Men när mer tid och resurser investeras i sådana appar vill du säkerställa att du enkelt kan integrera funktioner och resurser på ett sådant sätt att det är lätt att utöka, att din app kan hantera mer än en modell samtidigt, och hantera olika modellkomplexiteter. Kort sagt, att bygga Gen AI-appar är enkelt i början, men när de växer och blir mer komplexa behöver du börja definiera en arkitektur och kommer sannolikt behöva förlita dig på en standard för att säkerställa att dina appar byggs på ett konsekvent sätt. Här kommer MCP in för att organisera och tillhandahålla en standard.

---

## **🔍 Vad är Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** är ett **öppet, standardiserat gränssnitt** som låter stora språkmodeller (LLMs) interagera sömlöst med externa verktyg, API:er och datakällor. Det tillhandahåller en konsekvent arkitektur för att förbättra AI-modellers funktionalitet bortom deras träningsdata, vilket möjliggör smartare, skalbara och mer responsiva AI-system.

---

## **🎯 Varför standardisering inom AI är viktigt**

När generativa AI-applikationer blir mer komplexa är det viktigt att anta standarder som säkerställer **skalbarhet, utbyggbarhet, underhållbarhet** och **att undvika leverantörslåsningar**. MCP adresserar dessa behov genom att:

- Förenhetliga integrationer mellan modeller och verktyg
- Minska ömtåliga, skräddarsydda engångslösningar
- Tillåta flera modeller från olika leverantörer att samexistera inom ett ekosystem

**Notera:** Även om MCP kallar sig en öppen standard, finns inga planer på att standardisera MCP genom några befintliga standardiseringsorgan som IEEE, IETF, W3C, ISO eller något annat standardorgan.

---

## **📚 Läromål**

I slutet av denna artikel kommer du att kunna:

- Definiera **Model Context Protocol (MCP)** och dess användningsområden
- Förstå hur MCP standardiserar kommunikationen mellan modeller och verktyg
- Identifiera de centrala komponenterna i MCP-arkitekturen
- Utforska verkliga användningsfall för MCP i företags- och utvecklingssammanhang

---

## **💡 Varför Model Context Protocol (MCP) är en revolutionerande förändring**

### **🔗 MCP löser fragmentering i AI-interaktioner**

Före MCP krävde integration av modeller med verktyg:

- Egengjord kod för varje verktygs- och modellpar
- Icke-standardiserade API:er för varje leverantör
- Frekventa avbrott vid uppdateringar
- Dålig skalbarhet när fler verktyg tillkommer

### **✅ Fördelar med MCP-standardisering**

| **Fördel**               | **Beskrivning**                                                                |
|--------------------------|--------------------------------------------------------------------------------|
| Interoperabilitet        | LLM:er fungerar sömlöst med verktyg från olika leverantörer                    |
| Konsekvens               | Enhetligt beteende över plattformar och verktyg                               |
| Återanvändbarhet         | Verktyg byggda en gång kan användas i olika projekt och system                |
| Accelererad utveckling   | Minska utvecklingstid genom användning av standardiserade, plug-and-play-gränssnitt |

---

## **🧱 Översikt av MCP-arkitektur på hög nivå**

MCP följer en **klient-server-modell**, där:

- **MCP Hosts** kör AI-modellerna
- **MCP Clients** initierar förfrågningar
- **MCP Servers** tillhandahåller kontext, verktyg och kapabiliteter

### **Nyckelkomponenter:**

- **Resurser** – Statisk eller dynamisk data för modeller  
- **Prompter** – Fördefinierade arbetsflöden för styrd generering  
- **Verktyg** – Körbara funktioner som sökning, beräkningar  
- **Sampling** – Agentlikt beteende via rekursiva interaktioner (föråldrat i
    MCP `2026-07-28`; nya implementationer bör integrera direkt med en LLM-
    leverantör)
- **Elicitation** – Serverinitierade förfrågningar om användarinmatning
- **Roots** – Informationsfilsystemslägen relevanta för en server
    (föråldrat i MCP `2026-07-28`; föredra verktygsparametrar, resurs-URIs eller
    serverkonfiguration)

### **Protokollarkitektur:**

MCP använder en tvålagersarkitektur:
- **Datalager**: JSON-RPC 2.0-meddelanden, metadata per förfrågan, upptäckt och
    protokollprimitive
- **Transportlager**: stdio för lokala underprocesser och Streamable HTTP för
    fjärrservrar. Streamable HTTP kan använda SSE-ramverk för strömmade svar,
    men den äldre HTTP+SSE-transporten är föråldrad.

---

## Hur MCP-servrar fungerar

MCP-servrar fungerar på följande sätt:

- **Förfrågningsflöde**:
    1. En förfrågan initieras av en slutanvändare eller programvara som agerar på deras vägnar.
    2. **MCP-klienten** skickar förfrågan till en **MCP Host**, som hanterar AI-modellens runtime.
    3. **AI-modellen** tar emot användarens prompt och kan begära tillgång till externa verktyg eller data via en eller flera verktygsanrop.
    4. **MCP Host**, inte modellen direkt, kommunicerar med lämpliga **MCP Server(s)** med hjälp av det standardiserade protokollet.
- **MCP Host-funktionalitet**:
    - **Verktygsregister**: Underhåller en katalog över tillgängliga verktyg och deras kapabiliteter.
    - **Autentisering**: Verifierar behörighet för verktygsåtkomst.
    - **Förfrågningshanterare**: Bearbetar inkommande verktygsförfrågningar från modellen.
    - **Svarformatterare**: Strukturerar verktygsutdata i ett format som modellen kan förstå.
- **MCP Server-exekvering**:
    - **MCP Host** dirigerar verktygsanrop till en eller flera **MCP Servers**, som vardera exponerar specialiserade funktioner (t.ex. sökning, beräkningar, databasfrågor).
    - **MCP Servers** utför sina respektive operationer och returnerar resultat till **MCP Host** i ett konsekvent format.
    - **MCP Host** formaterar och vidarebefordrar dessa resultat till **AI-modellen**.
- **Slutförande av svar**:
    - **AI-modellen** integrerar verktygsutdata i ett slutgiltigt svar.
    - **MCP Host** skickar tillbaka detta svar till **MCP Client**, som levererar det till slutanvändaren eller anropande programvara.
    

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Klient/Applikation] -->|Skickar Förfrågan| H[MCP Värd]
    H -->|Anropar| A[AI Modell]
    A -->|Verktygsanropsförfrågan| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Webbsökning]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Kalkylatorverktyg]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Databasåtkomstverktyg]
    H -->|MCP Protocol| T4[MCP Server Tool 04: Filsystemverktyg]
    H -->|Skickar Svar| Client

    subgraph "MCP Värdkomponenter"
        H
        G[Verktygsregister]
        I[Autentisering]
        J[Förfrågningshanterare]
        K[Svarformaterare]
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

MCP-servrar låter dig utöka LLM-funktionaliteter genom att tillhandahålla data och funktionalitet.

Redo att testa? Här är språk- och/eller stack-specifika SDK:er med exempel på att skapa enkla MCP-servrar i olika språk/stackar:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk


## 🌍 Verkliga användningsfall för MCP

MCP möjliggör en rad applikationer genom att utöka AI-kapabiliteter:

| **Applikation**               | **Beskrivning**                                                                |
|------------------------------|--------------------------------------------------------------------------------|
| Företagsdataintegration      | Koppla LLM:er till databaser, CRM-system eller interna verktyg                  |
| Agentlika AI-system          | Möjliggör autonoma agenter med verktygstillgång och arbetsflöden för beslutsfattande |
| Multimodala applikationer    | Kombinera text-, bild- och ljudverktyg inom en enda enhetlig AI-app             |
| Realtidsdataintegration      | Ta in live-data i AI-interaktioner för mer exakta, aktuella resultat           |


### 🧠 MCP = Universell standard för AI-interaktioner

Model Context Protocol (MCP) fungerar som en universell standard för AI-interaktioner, precis som USB-C standardiserade fysiska anslutningar för enheter. Inom AI-världen tillhandahåller MCP ett konsekvent gränssnitt som låter modeller (klienter) integreras sömlöst med externa verktyg och dataleverantörer (servrar). Detta eliminerar behovet av olika, skräddarsydda protokoll för varje API eller datakälla.

Under MCP följer ett MCP-kompatibelt verktyg (kallat en MCP-server) en enhetlig standard. Dessa servrar kan lista de verktyg eller åtgärder de erbjuder och utföra dessa när de efterfrågas av en AI-agent. AI-agentplattformar som stödjer MCP kan upptäcka tillgängliga verktyg från servrarna och anropa dem via detta standardprotokoll.

### 💡 Underlättar tillgång till kunskap

Utöver att erbjuda verktyg underlättar MCP även tillgång till kunskap. Det möjliggör för applikationer att ge kontext till stora språkmodeller (LLMs) genom att länka dem till olika datakällor. Till exempel kan en MCP-server representera ett företags dokumentarkiv, vilket tillåter agenter att hämta relevant information vid behov. En annan server kan hantera specifika åtgärder som att skicka e-post eller uppdatera register. Ur agentens perspektiv är detta helt enkelt verktyg den kan använda – vissa verktyg returnerar data (kunskapskontext), medan andra utför handlingar. MCP hanterar båda effektivt.

En agent som ansluter till en MCP-server lär automatiskt sig serverns tillgängliga kapabiliteter och åtkomliga data via ett standardiserat format. Denna standardisering möjliggör dynamisk verktygstillgänglighet. Till exempel gör tillägg av en ny MCP-server till en agents system dess funktioner omedelbart användbara utan att kräva ytterligare anpassning av agentens instruktioner.

Denna strömlinjeformade integration stämmer överens med flödet som visas i följande diagram, där servrar tillhandahåller både verktyg och kunskap, vilket säkerställer sömlöst samarbete mellan system.

### 👉 Exempel: Skalbar agentslösning

```mermaid
---
title: Scalable Agent Solution with MCP
description: A diagram illustrating how a user interacts with an LLM that connects to multiple MCP servers, with each server providing both knowledge and tools, creating a scalable AI system architecture
---
graph TD
    User -->|Fråga| LLM
    LLM -->|Svar| User
    LLM -->|MCP| ServerA
    LLM -->|MCP| ServerB
    ServerA -->|Universell kontakt| ServerB
    ServerA --> KnowledgeA
    ServerA --> ToolsA
    ServerB --> KnowledgeB
    ServerB --> ToolsB

    subgraph Server A
        KnowledgeA[Kunskap]
        ToolsA[Verktyg]
    end

    subgraph Server B
        KnowledgeB[Kunskap]
        ToolsB[Verktyg]
    end
```
Den universella connectorn möjliggör att MCP-servrar kommunicerar och delar kapabiliteter med varandra, vilket tillåter ServerA att delegera uppgifter till ServerB eller få tillgång till dess verktyg och kunskap. Detta federerar verktyg och data över servrar, vilket stödjer skalbara och modulära agentarkitekturer. Eftersom MCP standardiserar exponering av verktyg kan agenter dynamiskt upptäcka och dirigera förfrågningar mellan servrar utan hårdkodade integrationer.


Verktygs- och kunskapsfederation: Verktyg och data kan nås över servrar, vilket möjliggör mer skalbara och modulära agentlika arkitekturer.

### 🔄 Avancerade MCP-scenarier med klientbaserad LLM-integration

Utöver den grundläggande MCP-arkitekturen finns avancerade scenarier där både klient och server innehåller LLM:er, vilket möjliggör mer sofistikerade interaktioner. I följande diagram kan **Client App** vara en IDE med ett antal MCP-verktyg tillgängliga för användning av LLM:

```mermaid
---
title: Advanced MCP Scenarios with Client-Server LLM Integration
description: A sequence diagram showing the detailed interaction flow between user, client application, client LLM, multiple MCP servers, and server LLM, illustrating tool discovery, user interaction, direct tool calling, and feature negotiation phases
---
sequenceDiagram
    autonumber
    actor User as 👤 Användare
    participant ClientApp as 🖥️ Klientapp
    participant ClientLLM as 🧠 Klient LLM
    participant Server1 as 🔧 MCP Server 1
    participant Server2 as 📚 MCP Server 2
    participant ServerLLM as 🤖 Server LLM
    
    %% Upptäcktsfas
    rect rgb(220, 240, 255)
        Note over ClientApp, Server2: UPPTÄCKTSFAS FÖR VERKTYG
        ClientApp->>+Server1: Begär tillgängliga verktyg/resurser
        Server1-->>-ClientApp: Returnera verktygslista (JSON)
        ClientApp->>+Server2: Begär tillgängliga verktyg/resurser
        Server2-->>-ClientApp: Returnera verktygslista (JSON)
        Note right of ClientApp: Spara kombinerad verktygskatalog<br/>lokalt
    end
    
    %% Användarinteraktion
    rect rgb(255, 240, 220)
        Note over User, ClientLLM: ANVÄNDARINTERAKTIONSFAS
        User->>+ClientApp: Ange prompt på naturligt språk
        ClientApp->>+ClientLLM: Skicka vidare prompt + verktygskatalog
        ClientLLM->>-ClientLLM: Analysera prompt & välj verktyg
    end
    
    %% Scenario A: Direkt verktygsanrop
    alt Direkt verktygsanrop
        rect rgb(220, 255, 220)
            Note over ClientApp, Server1: SCENARIO A: DIREKT VERKTYGSANROP
            ClientLLM->>+ClientApp: Begär verktygsexekvering
            ClientApp->>+Server1: Kör specifikt verktyg
            Server1-->>-ClientApp: Returnera resultat
            ClientApp->>+ClientLLM: Bearbeta resultat
            ClientLLM-->>-ClientApp: Generera svar
            ClientApp-->>-User: Visa slutligt svar
        end
    
    %% Scenario B: Funktionsförhandling (VS Code-stil)
    else Funktionsförhandling (VS Code-stil)
        rect rgb(255, 220, 220)
            Note over ClientApp, ServerLLM: SCENARIO B: FUNKTIONSFÖRHANDLING
            ClientLLM->>+ClientApp: Identifiera behövda kapabiliteter
            ClientApp->>+Server2: Förhandla funktioner/kapabiliteter
            Server2->>+ServerLLM: Begär ytterligare kontext
            ServerLLM-->>-Server2: Tillhandahåll kontext
            Server2-->>-ClientApp: Returnera tillgängliga funktioner
            ClientApp->>+Server2: Anropa förhandlade verktyg
            Server2-->>-ClientApp: Returnera resultat
            ClientApp->>+ClientLLM: Bearbeta resultat
            ClientLLM-->>-ClientApp: Generera svar
            ClientApp-->>-User: Visa slutligt svar
        end
    end
```

## 🔐 Praktiska fördelar med MCP

Här är de praktiska fördelarna med att använda MCP:

- **Aktualitet**: Modeller kan komma åt uppdaterad information utöver sin träningsdata
- **Kapabilitetsutökning**: Modeller kan använda specialiserade verktyg för uppgifter de inte tränades för
- **Minskade hallucinationer**: Externa datakällor ger faktabaserad grund
- **Sekretess**: Känslig data kan stanna inom säkra miljöer istället för att bäddas in i promptar

## 📌 Viktiga slutsatser

Följande är viktiga slutsatser för användning av MCP:

- **MCP** standardiserar hur AI-modeller interagerar med verktyg och data
- Främjar **utbyggbarhet, konsekvens och interoperabilitet**
- MCP hjälper till att **minska utvecklingstid, förbättra tillförlitlighet och utöka modelleffektivitet**
- Klient-server-arkitekturen **möjliggör flexibla, utbyggbara AI-applikationer**

## 🧠 Övning

Fundera på en AI-applikation du är intresserad av att bygga.

- Vilka **externa verktyg eller data** skulle kunna förbättra dess kapaciteter?
- Hur skulle MCP göra integrationen **enklare och mer pålitlig?**

## Ytterligare resurser

- [MCP GitHub Repository](https://github.com/modelcontextprotocol)


## Vad som kommer härnäst

Nästa: [Kapitel 1: Grundläggande begrepp](../01-CoreConcepts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->