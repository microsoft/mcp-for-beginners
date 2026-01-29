# Sissejuhatus mudeli kontekstiprotokolli (MCP): Miks see on oluline skaleeritavate AI-rakenduste jaoks

[![Sissejuhatus mudeli kontekstiprotokolli](../../../translated_images/et/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

Generatiivsed AI-rakendused on suur edasiminek, kuna need võimaldavad kasutajal sageli suhelda rakendusega loomuliku keele kaudu. Kuid mida rohkem aega ja ressursse sellistesse rakendustesse investeeritakse, seda olulisem on tagada, et funktsionaalsusi ja ressursse oleks lihtne integreerida, rakendust oleks lihtne laiendada, see toetaks mitut mudelit ja suudaks toime tulla erinevate mudelite keerukustega. Lühidalt öeldes on generatiivsete AI-rakenduste loomine alguses lihtne, kuid nende kasvades ja keerukamaks muutudes tuleb hakata määratlema arhitektuuri ning tõenäoliselt on vaja standardit, et tagada rakenduste järjepidev ülesehitus. Siin tulebki MCP mängu, et asju organiseerida ja pakkuda standardit.

---

## **🔍 Mis on mudeli kontekstiprotokoll (MCP)?**

**Mudeli kontekstiprotokoll (MCP)** on **avatud ja standardiseeritud liides**, mis võimaldab suurte keelemudelite (LLM-id) sujuvat suhtlust väliste tööriistade, API-de ja andmeallikatega. See pakub järjepidevat arhitektuuri, et laiendada AI-mudelite funktsionaalsust väljapoole nende treeningandmeid, võimaldades targemaid, skaleeritavamaid ja reageerivamaid AI-süsteeme.

---

## **🎯 Miks on standardiseerimine AI-s oluline**

Generatiivsete AI-rakenduste keerukuse kasvades on oluline võtta kasutusele standardid, mis tagavad **skaleeritavuse, laiendatavuse, hooldatavuse** ja **vältida sõltuvust konkreetsetest tarnijatest**. MCP vastab nendele vajadustele, pakkudes:

- Mudelite ja tööriistade integreerimise ühtlustamist
- Vähem hapraid ja ühekordseid kohandatud lahendusi
- Võimalust mitme erineva tarnija mudelite kooseksisteerimiseks ühes ökosüsteemis

**Märkus:** Kuigi MCP esitleb end avatud standardina, ei ole plaanis MCP-d standardiseerida ühegi olemasoleva standardiorganisatsiooni, nagu IEEE, IETF, W3C, ISO või mõne muu kaudu.

---

## **📚 Õpieesmärgid**

Selle artikli lõpuks suudate:

- Defineerida **mudeli kontekstiprotokolli (MCP)** ja selle kasutusjuhtumid
- Mõista, kuidas MCP standardiseerib mudelite ja tööriistade vahelist suhtlust
- Tuvastada MCP arhitektuuri põhikomponendid
- Uurida MCP reaalseid rakendusi ettevõtete ja arenduskontekstides

---

## **💡 Miks mudeli kontekstiprotokoll (MCP) on murranguline**

### **🔗 MCP lahendab AI-interaktsioonide killustatuse**

Enne MCP-d nõudis mudelite integreerimine tööriistadega:

- Kohandatud koodi iga tööriista-mudeli paari jaoks
- Iga tarnija jaoks mittestandardseid API-sid
- Sagedasi katkestusi uuenduste tõttu
- Kehva skaleeritavust suurema tööriistade arvu korral

### **✅ MCP standardiseerimise eelised**

| **Eelis**                 | **Kirjeldus**                                                                  |
|---------------------------|-------------------------------------------------------------------------------|
| Interoperatiivsus         | LLM-id töötavad sujuvalt tööriistadega erinevatelt tarnijatelt               |
| Järjepidevus              | Ühtne käitumine platvormide ja tööriistade vahel                              |
| Taaskasutatavus           | Üks kord loodud tööriistu saab kasutada erinevates projektides ja süsteemides |
| Kiirendatud arendus       | Vähendab arendusaega, kasutades standardiseeritud, plug-and-play liideseid    |

---

## **🧱 MCP arhitektuuri ülevaade kõrgel tasemel**

MCP järgib **klient-serveri mudelit**, kus:

- **MCP Hostid** käitavad AI-mudeleid
- **MCP Kliendid** algatavad päringuid
- **MCP Serverid** pakuvad konteksti, tööriistu ja võimekusi

### **Põhikomponendid:**

- **Ressursid** – Staatilised või dünaamilised andmed mudelite jaoks  
- **Küsimused** – Eelmääratletud töövood juhendatud generatsiooniks  
- **Tööriistad** – Käivitatavad funktsioonid nagu otsing, arvutused  
- **Proovivõtmine** – Agentlik käitumine rekursiivsete interaktsioonide kaudu

---

## Kuidas MCP serverid töötavad

MCP serverid toimivad järgmiselt:

- **Päringuvoog**:
    1. Päringu algatab lõppkasutaja või tarkvara, mis tegutseb tema nimel.
    2. **MCP Klient** saadab päringu **MCP Hostile**, mis haldab AI-mudeli käitusaega.
    3. **AI Mudel** võtab vastu kasutaja küsimuse ja võib taotleda juurdepääsu välistele tööriistadele või andmetele ühe või mitme tööriistakõne kaudu.
    4. **MCP Host**, mitte mudel ise, suhtleb vastavate **MCP Serveritega** kasutades standardiseeritud protokolli.
- **MCP Host funktsionaalsus**:
    - **Tööriistade register**: Hoiab kataloogi saadaolevatest tööriistadest ja nende võimekustest.
    - **Autentimine**: Kontrollib tööriistadele juurdepääsu õigusi.
    - **Päringute haldur**: Töötleb mudelilt tulevaid tööriistapäringuid.
    - **Vastuse vormindaja**: Struktureerib tööriistade väljundid mudeli jaoks arusaadavasse vormingusse.
- **MCP Serveri täitmine**:
    - **MCP Host** suunab tööriistakõned ühele või mitmele **MCP Serverile**, millest igaüks pakub spetsialiseeritud funktsioone (nt otsing, arvutused, andmebaasi päringud).
    - **MCP Serverid** täidavad oma vastavad operatsioonid ja tagastavad tulemused **MCP Hostile** ühtses vormingus.
    - **MCP Host** vormindab ja edastab need tulemused **AI Mudelile**.
- **Vastuse lõpetamine**:
    - **AI Mudel** integreerib tööriistade väljundid lõplikku vastusesse.
    - **MCP Host** saadab selle vastuse tagasi **MCP Kliendile**, kes edastab selle lõppkasutajale või päringut teinud tarkvarale.

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

## 👨‍💻 Kuidas ehitada MCP serverit (koos näidetega)

MCP serverid võimaldavad laiendada LLM-i võimekusi, pakkudes andmeid ja funktsionaalsust.

Valmis proovima? Siin on keele- ja/või stack-spetsiifilised SDK-d koos näidetega lihtsate MCP serverite loomiseks erinevates keeltes/stackides:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk


## 🌍 MCP reaalsed kasutusjuhtumid

MCP võimaldab laia valikut rakendusi, laiendades AI võimekusi:

| **Rakendus**               | **Kirjeldus**                                                                  |
|----------------------------|-------------------------------------------------------------------------------|
| Ettevõtte andmete integreerimine | Ühendage LLM-id andmebaaside, CRM-ide või sisemiste tööriistadega          |
| Agentlikud AI-süsteemid    | Võimaldage autonoomseid agente tööriistade juurdepääsu ja otsustusprotsessidega |
| Multimodaalsed rakendused  | Kombineerige teksti-, pildi- ja helitööriistad ühes ühtses AI-rakenduses       |
| Reaalajas andmete integreerimine | Tooge AI-interaktsioonidesse reaalajas andmeid täpsemate ja ajakohasemate väljundite jaoks |

### 🧠 MCP = universaalne standard AI-interaktsioonide jaoks

Mudeli kontekstiprotokoll (MCP) toimib universaalse standardina AI-interaktsioonide jaoks, sarnaselt sellele, kuidas USB-C standardiseeris füüsilised ühendused seadmete jaoks. AI maailmas pakub MCP järjepidevat liidest, võimaldades mudelitel (kliendid) integreeruda sujuvalt väliste tööriistade ja andmeallikatega (serverid). See kõrvaldab vajaduse mitmekesiste, kohandatud protokollide järele iga API või andmeallika jaoks.

MCP raames järgib MCP-ühilduv tööriist (nimetatakse MCP serveriks) ühtset standardit. Need serverid saavad loetleda pakutavaid tööriistu või toiminguid ja täita neid toiminguid, kui AI-agent neid taotleb. MCP-d toetavad AI-agentide platvormid suudavad avastada serverite pakutavaid tööriistu ja neid standardprotokolli kaudu kasutada.

### 💡 Hõlbustab juurdepääsu teadmistele

Lisaks tööriistade pakkumisele hõlbustab MCP ka juurdepääsu teadmistele. See võimaldab rakendustel pakkuda suurtele keelemudelitele (LLM-id) konteksti, ühendades need erinevate andmeallikatega. Näiteks võib MCP server esindada ettevõtte dokumendirepositooriumi, võimaldades agentidel nõudmisel asjakohast teavet hankida. Teine server võib hallata konkreetseid toiminguid, nagu e-kirjade saatmine või kirjete uuendamine. Agendi vaatenurgast on need lihtsalt tööriistad, mida ta saab kasutada—mõned tööriistad tagastavad andmeid (teadmiste kontekst), teised teostavad toiminguid. MCP haldab mõlemat tõhusalt.

Agent, kes ühendub MCP serveriga, õpib automaatselt serveri saadaolevaid võimekusi ja juurdepääsetavaid andmeid standardvormingus. See standardiseerimine võimaldab dünaamilist tööriistade kättesaadavust. Näiteks uue MCP serveri lisamine agendi süsteemi muudab selle funktsioonid kohe kasutatavaks, ilma et oleks vaja agendi juhiseid täiendavalt kohandada.

See sujuv integreerimine vastab allpool kujutatud voole, kus serverid pakuvad nii tööriistu kui ka teadmisi, tagades süsteemide vahelise sujuva koostöö.

### 👉 Näide: skaleeritav agendilahendus

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
Universaalne ühendaja võimaldab MCP serveritel omavahel suhelda ja võimekusi jagada, võimaldades ServerA-l delegeerida ülesandeid ServerB-le või kasutada selle tööriistu ja teadmisi. See ühendab tööriistad ja andmed serverite vahel, toetades skaleeritavaid ja modulaarseid agendi arhitektuure. Kuna MCP standardiseerib tööriistade eksponeerimist, saavad agendid dünaamiliselt avastada ja suunata päringuid serverite vahel ilma kõvakoodiga integreerimisteta.

Tööriistade ja teadmiste ühendamine: Tööriistad ja andmed on kättesaadavad serverite vahel, võimaldades skaleeritavamaid ja modulaarsemaid agentlikke arhitektuure.

### 🔄 Täiustatud MCP stsenaariumid kliendipoolse LLM-i integreerimisega

Lisaks MCP põhiarhitektuurile on olemas täiustatud stsenaariumid, kus nii klient kui ka server sisaldavad LLM-e, võimaldades keerukamaid interaktsioone. Järgnevas diagrammis võib **Kliendirakendus** olla IDE, millel on mitmeid MCP tööriistu, mida LLM saab kasutada:

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

## 🔐 MCP praktilised eelised

Siin on MCP kasutamise praktilised eelised:

- **Värskus**: Mudelid saavad juurdepääsu ajakohasele teabele väljaspool nende treeningandmeid
- **Võimekuse laiendamine**: Mudelid saavad kasutada spetsialiseeritud tööriistu ülesannete jaoks, milleks neid ei ole treenitud
- **Vähem hallutsinatsioone**: Välised andmeallikad pakuvad faktipõhist alust
- **Privaatsus**: Tundlikud andmed võivad jääda turvalistesse keskkondadesse, mitte olla sisestatud küsimustesse

## 📌 Olulised punktid

Järgnevad on MCP kasutamise olulised punktid:

- **MCP** standardiseerib, kuidas AI-mudelid suhtlevad tööriistade ja andmetega
- Edendab **laiendatavust, järjepidevust ja koostalitlusvõimet**
- MCP aitab **vähendada arendusaega, parandada töökindlust ja laiendada mudeli võimekusi**
- Kliendi-serveri arhitektuur **võimaldab paindlikke ja laiendatavaid AI-rakendusi**

## 🧠 Harjutus

Mõelge AI-rakendusele, mida soovite luua.

- Millised **välised tööriistad või andmed** võiksid selle võimekust parandada?
- Kuidas võiks MCP muuta integreerimise **lihtsamaks ja usaldusväärsemaks?**

## Täiendavad ressursid

- [MCP GitHubi repositoorium](https://github.com/modelcontextprotocol)


## Mis edasi

Järgmine: [1. peatükk: Põhimõisted](../01-CoreConcepts/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.