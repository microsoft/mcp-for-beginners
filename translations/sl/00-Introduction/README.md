# Uvod v Model Context Protocol (MCP): Zakaj je pomemben za razširljive AI aplikacije

[![Uvod v Model Context Protocol](../../../translated_images/sl/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Kliknite na zgornjo sliko za ogled videa te lekcije)_

Generativne AI aplikacije so velik korak naprej, saj pogosto omogočajo uporabnikom interakcijo z aplikacijo prek naravnih jezikovnih pozivov. Vendar pa, ko se v takšne aplikacije vlaga več časa in virov, želite zagotoviti, da lahko enostavno integrirate funkcionalnosti in vire na način, ki omogoča enostavno razširitev, da vaša aplikacija podpira več kot en model in obvladuje različne posebnosti modelov. Skratka, gradnja Gen AI aplikacij je na začetku enostavna, vendar ko rastejo in postajajo bolj zapletene, morate začeti definirati arhitekturo in se verjetno zanašati na standard, da zagotovite, da so vaše aplikacije zgrajene na dosleden način. Tukaj pride MCP, da organizira stvari in zagotovi standard.

---

## **🔍 Kaj je Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** je **odprt, standardiziran vmesnik**, ki omogoča brezhibno interakcijo Velikih Jezikovnih Modelov (LLM) z zunanjimi orodji, API-ji in viri podatkov. Ponuja dosledno arhitekturo za izboljšanje funkcionalnosti AI modelov onkraj njihovih učnih podatkov, kar omogoča pametnejše, razširljive in bolj odzivne AI sisteme.

---

## **🎯 Zakaj je standardizacija v AI pomembna**

Ko generativne AI aplikacije postajajo bolj zapletene, je ključnega pomena sprejeti standarde, ki zagotavljajo **razširljivost, prilagodljivost, vzdržljivost** in **izogibanje odvisnosti od enega ponudnika**. MCP odgovarja na te potrebe z:

- Poenotenjem integracij model-orodje
- Zmanjšanjem krhkih, enkratnih prilagojenih rešitev
- Omogočanjem sobivanja več modelov različnih ponudnikov v enem ekosistemu

**Opomba:** Čeprav se MCP predstavlja kot odprt standard, ni načrtov za standardizacijo MCP prek obstoječih standardnih organizacij, kot so IEEE, IETF, W3C, ISO ali katera koli druga organizacija.

---

## **📚 Cilji učenja**

Do konca tega članka boste lahko:

- Definirali **Model Context Protocol (MCP)** in njegove primere uporabe
- Razumeli, kako MCP standardizira komunikacijo med modeli in orodji
- Prepoznali ključne komponente arhitekture MCP
- Raziskali resnične primere uporabe MCP v podjetniških in razvojnih kontekstih

---

## **💡 Zakaj je Model Context Protocol (MCP) prelomnica**

### **🔗 MCP rešuje fragmentacijo v AI interakcijah**

Pred MCP je integracija modelov z orodji zahtevala:

- Prilagojeno kodo za vsak par orodje-model
- Nestandardizirane API-je za vsakega ponudnika
- Pogoste prekinitve zaradi posodobitev
- Slabo razširljivost z več orodji

### **✅ Prednosti standardizacije MCP**

| **Prednost**              | **Opis**                                                                |
|---------------------------|-------------------------------------------------------------------------|
| Interoperabilnost         | LLM-ji brezhibno delujejo z orodji različnih ponudnikov                |
| Doslednost                | Enotno vedenje na različnih platformah in orodjih                      |
| Ponovna uporabnost        | Orodja, zgrajena enkrat, se lahko uporabljajo v različnih projektih     |
| Pospešen razvoj           | Skrajšanje časa razvoja z uporabo standardiziranih, plug-and-play vmesnikov |

---

## **🧱 Pregled arhitekture MCP na visoki ravni**

MCP sledi **modelu odjemalec-strežnik**, kjer:

- **MCP gostitelji** poganjajo AI modele
- **MCP odjemalci** sprožijo zahteve
- **MCP strežniki** zagotavljajo kontekst, orodja in zmogljivosti

### **Ključne komponente:**

- **Viri** – Statični ali dinamični podatki za modele  
- **Pozivi** – Vnaprej določeni poteki dela za usmerjeno generacijo  
- **Orodja** – Izvedljive funkcije, kot so iskanje, izračuni  
- **Vzorcevanje** – Agentično vedenje prek rekurzivnih interakcij

---

## Kako delujejo MCP strežniki

MCP strežniki delujejo na naslednji način:

- **Tok zahteve**:
    1. Zahtevo sproži končni uporabnik ali programska oprema, ki deluje v njegovem imenu.
    2. **MCP odjemalec** pošlje zahtevo **MCP gostitelju**, ki upravlja z AI modelom.
    3. **AI model** prejme uporabniški poziv in lahko zahteva dostop do zunanjih orodij ali podatkov prek enega ali več klicev orodij.
    4. **MCP gostitelj**, ne model neposredno, komunicira z ustreznim **MCP strežnikom(-i)** z uporabo standardiziranega protokola.
- **Funkcionalnost MCP gostitelja**:
    - **Register orodij**: Vzdržuje katalog razpoložljivih orodij in njihovih zmogljivosti.
    - **Avtentikacija**: Preverja dovoljenja za dostop do orodij.
    - **Upravljalnik zahtev**: Obdeluje dohodne zahteve za orodja od modela.
    - **Oblikovalec odgovorov**: Strukturira izhode orodij v formatu, ki ga model razume.
- **Izvedba MCP strežnika**:
    - **MCP gostitelj** usmerja klice orodij na enega ali več **MCP strežnikov**, ki izpostavljajo specializirane funkcije (npr. iskanje, izračuni, poizvedbe v bazi podatkov).
    - **MCP strežniki** izvajajo svoje operacije in rezultate vrnejo **MCP gostitelju** v doslednem formatu.
    - **MCP gostitelj** oblikuje in posreduje te rezultate **AI modelu**.
- **Dokončanje odgovora**:
    - **AI model** vključi izhode orodij v končni odgovor.
    - **MCP gostitelj** pošlje ta odgovor nazaj **MCP odjemalcu**, ki ga dostavi končnemu uporabniku ali programski opremi.

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

## 👨‍💻 Kako zgraditi MCP strežnik (z zgledi)

MCP strežniki omogočajo razširitev zmogljivosti LLM z zagotavljanjem podatkov in funkcionalnosti.

Pripravljeni, da poskusite? Tukaj so SDK-ji za določene jezike in/ali platforme z zgledi za ustvarjanje preprostih MCP strežnikov v različnih jezikih/platformah:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk


## 🌍 Resnični primeri uporabe MCP

MCP omogoča širok spekter aplikacij z razširitvijo AI zmogljivosti:

| **Aplikacija**              | **Opis**                                                                |
|-----------------------------|-------------------------------------------------------------------------|
| Integracija podatkov v podjetju | Povezovanje LLM-jev z bazami podatkov, CRM-ji ali internimi orodji       |
| Agentični AI sistemi         | Omogočanje avtonomnih agentov z dostopom do orodij in poteki odločanja |
| Večmodalne aplikacije        | Združevanje besedilnih, slikovnih in zvočnih orodij v eni AI aplikaciji |
| Integracija podatkov v realnem času | Prinašanje živih podatkov v AI interakcije za natančnejše, aktualne izhode |

### 🧠 MCP = Univerzalni standard za AI interakcije

Model Context Protocol (MCP) deluje kot univerzalni standard za AI interakcije, podobno kot je USB-C standardiziral fizične povezave za naprave. V svetu AI MCP zagotavlja dosleden vmesnik, ki omogoča modelom (odjemalcem), da se brezhibno integrirajo z zunanjimi orodji in ponudniki podatkov (strežniki). To odpravlja potrebo po raznolikih, prilagojenih protokolih za vsak API ali vir podatkov.

V okviru MCP orodje, združljivo z MCP (imenovano MCP strežnik), sledi enotnemu standardu. Ti strežniki lahko navedejo orodja ali dejanja, ki jih ponujajo, in ta dejanja izvedejo, ko jih zahteva AI agent. Platforme AI agentov, ki podpirajo MCP, so sposobne odkriti razpoložljiva orodja s strežnikov in jih uporabiti prek tega standardnega protokola.

### 💡 Omogoča dostop do znanja

Poleg ponujanja orodij MCP omogoča tudi dostop do znanja. Omogoča aplikacijam, da zagotavljajo kontekst velikim jezikovnim modelom (LLM) z njihovim povezovanjem z različnimi viri podatkov. Na primer, MCP strežnik lahko predstavlja dokumentni repozitorij podjetja, kar agentom omogoča, da po potrebi pridobijo ustrezne informacije. Drug strežnik lahko obravnava specifična dejanja, kot so pošiljanje e-pošte ali posodabljanje zapisov. Z vidika agenta so to preprosto orodja, ki jih lahko uporablja – nekatera orodja vračajo podatke (kontekst znanja), druga pa izvajajo dejanja. MCP učinkovito upravlja oboje.

Agent, ki se poveže z MCP strežnikom, samodejno spozna razpoložljive zmogljivosti strežnika in dostopne podatke prek standardnega formata. Ta standardizacija omogoča dinamično razpoložljivost orodij. Na primer, dodajanje novega MCP strežnika v sistem agenta omogoča takojšnjo uporabo njegovih funkcij brez dodatne prilagoditve navodil agenta.

Ta poenostavljena integracija je skladna s tokom, prikazanim na naslednjem diagramu, kjer strežniki zagotavljajo tako orodja kot znanje, kar omogoča brezhibno sodelovanje med sistemi.

### 👉 Primer: Razširljiva rešitev za agente

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
Univerzalni konektor omogoča MCP strežnikom, da komunicirajo in si delijo zmogljivosti med seboj, kar omogoča, da ServerA delegira naloge ServerB ali dostopa do njegovih orodij in znanja. To združuje orodja in podatke med strežniki ter podpira razširljive in modularne arhitekture agentov. Ker MCP standardizira izpostavljanje orodij, lahko agenti dinamično odkrivajo in usmerjajo zahteve med strežniki brez trdno kodiranih integracij.

Združevanje orodij in znanja: Orodja in podatki so dostopni med strežniki, kar omogoča bolj razširljive in modularne agencijske arhitekture.

### 🔄 Napredni scenariji MCP z integracijo LLM na strani odjemalca

Poleg osnovne arhitekture MCP obstajajo napredni scenariji, kjer tako odjemalec kot strežnik vsebujeta LLM-je, kar omogoča bolj prefinjene interakcije. Na naslednjem diagramu je **odjemalska aplikacija** lahko IDE z več MCP orodji, ki so na voljo za uporabo LLM:

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

## 🔐 Praktične prednosti MCP

Tukaj so praktične prednosti uporabe MCP:

- **Aktualnost**: Modeli lahko dostopajo do najnovejših informacij onkraj svojih učnih podatkov
- **Razširitev zmogljivosti**: Modeli lahko uporabljajo specializirana orodja za naloge, za katere niso bili usposobljeni
- **Zmanjšanje halucinacij**: Zunanji viri podatkov zagotavljajo dejansko osnovo
- **Zasebnost**: Občutljivi podatki lahko ostanejo v varnih okoljih, namesto da bi bili vključeni v pozive

## 📌 Ključne točke

Naslednje so ključne točke za uporabo MCP:

- **MCP** standardizira, kako AI modeli komunicirajo z orodji in podatki
- Spodbuja **razširljivost, doslednost in interoperabilnost**
- MCP pomaga **skrajšati čas razvoja, izboljšati zanesljivost in razširiti zmogljivosti modelov**
- Arhitektura odjemalec-strežnik omogoča **prilagodljive, razširljive AI aplikacije**

## 🧠 Vaja

Razmislite o AI aplikaciji, ki bi jo želeli zgraditi.

- Katera **zunanja orodja ali podatki** bi lahko izboljšali njene zmogljivosti?
- Kako bi MCP lahko poenostavil in naredil integracijo **bolj zanesljivo?**

## Dodatni viri

- [MCP GitHub repozitorij](https://github.com/modelcontextprotocol)


## Kaj sledi

Naprej: [Poglavje 1: Osnovni koncepti](../01-CoreConcepts/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.