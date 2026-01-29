# Úvod do Model Context Protocol (MCP): Prečo je dôležitý pre škálovateľné AI aplikácie

[![Úvod do Model Context Protocol](../../../translated_images/sk/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

Generatívne AI aplikácie predstavujú veľký krok vpred, pretože často umožňujú používateľom interakciu s aplikáciou pomocou prirodzených jazykových príkazov. Avšak, keď sa do takýchto aplikácií investuje viac času a zdrojov, je dôležité zabezpečiť jednoduchú integráciu funkcií a zdrojov tak, aby bolo možné aplikáciu ľahko rozšíriť, podporovať viacero modelov a zvládnuť rôzne špecifiká modelov. Jednoducho povedané, vytváranie generatívnych AI aplikácií je na začiatku jednoduché, ale ako rastú a stávajú sa komplexnejšími, je potrebné začať definovať architektúru a pravdepodobne sa spoliehať na štandard, ktorý zabezpečí konzistentnú výstavbu aplikácií. Tu prichádza MCP, aby veci zorganizoval a poskytol štandard.

---

## **🔍 Čo je Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** je **otvorené, štandardizované rozhranie**, ktoré umožňuje veľkým jazykovým modelom (LLM) bezproblémovo komunikovať s externými nástrojmi, API a zdrojmi dát. Poskytuje konzistentnú architektúru na rozšírenie funkčnosti AI modelov nad rámec ich tréningových dát, čím umožňuje inteligentnejšie, škálovateľné a citlivejšie AI systémy.

---

## **🎯 Prečo je štandardizácia v AI dôležitá**

Ako sa generatívne AI aplikácie stávajú komplexnejšími, je nevyhnutné prijať štandardy, ktoré zabezpečia **škálovateľnosť, rozšíriteľnosť, udržateľnosť** a **vyhnutie sa závislosti na jednom dodávateľovi**. MCP rieši tieto potreby tým, že:

- Zjednocuje integrácie modelov s nástrojmi
- Znižuje krehké, jednorazové vlastné riešenia
- Umožňuje koexistenciu viacerých modelov od rôznych dodávateľov v jednom ekosystéme

**Poznámka:** Hoci sa MCP prezentuje ako otvorený štandard, neplánuje sa jeho štandardizácia prostredníctvom existujúcich štandardizačných orgánov, ako sú IEEE, IETF, W3C, ISO alebo iné.

---

## **📚 Ciele učenia**

Na konci tohto článku budete schopní:

- Definovať **Model Context Protocol (MCP)** a jeho použitie
- Pochopiť, ako MCP štandardizuje komunikáciu medzi modelmi a nástrojmi
- Identifikovať hlavné komponenty architektúry MCP
- Preskúmať reálne aplikácie MCP v podnikových a vývojových kontextoch

---

## **💡 Prečo je Model Context Protocol (MCP) prelomový**

### **🔗 MCP rieši fragmentáciu v AI interakciách**

Pred MCP integrácia modelov s nástrojmi vyžadovala:

- Vlastný kód pre každý pár nástroj-model
- Neštandardné API pre každého dodávateľa
- Časté problémy spôsobené aktualizáciami
- Slabú škálovateľnosť s rastúcim počtom nástrojov

### **✅ Výhody štandardizácie MCP**

| **Výhoda**              | **Popis**                                                                |
|--------------------------|-------------------------------------------------------------------------|
| Interoperabilita         | LLM bezproblémovo fungujú s nástrojmi od rôznych dodávateľov            |
| Konzistentnosť           | Jednotné správanie naprieč platformami a nástrojmi                     |
| Znovupoužiteľnosť        | Nástroje vytvorené raz môžu byť použité v rôznych projektoch a systémoch|
| Zrýchlený vývoj          | Skrátenie času vývoja vďaka štandardizovaným rozhraniam                |

---

## **🧱 Prehľad architektúry MCP na vysokej úrovni**

MCP nasleduje **klient-server model**, kde:

- **MCP Hostitelia** prevádzkujú AI modely
- **MCP Klienti** iniciujú požiadavky
- **MCP Servery** poskytujú kontext, nástroje a schopnosti

### **Kľúčové komponenty:**

- **Zdroje** – Statické alebo dynamické dáta pre modely  
- **Príkazy** – Preddefinované pracovné postupy pre riadenú generáciu  
- **Nástroje** – Vykonateľné funkcie ako vyhľadávanie, výpočty  
- **Sampling** – Agentické správanie prostredníctvom rekurzívnych interakcií

---

## Ako fungujú MCP servery

MCP servery fungujú nasledovne:

- **Tok požiadaviek**:
    1. Požiadavka je iniciovaná koncovým používateľom alebo softvérom, ktorý koná v jeho mene.
    2. **MCP Klient** pošle požiadavku **MCP Hostiteľovi**, ktorý spravuje runtime AI modelu.
    3. **AI Model** prijme používateľský príkaz a môže požiadať o prístup k externým nástrojom alebo dátam prostredníctvom jedného alebo viacerých volaní nástrojov.
    4. **MCP Hostiteľ**, nie model priamo, komunikuje s príslušným **MCP Serverom** pomocou štandardizovaného protokolu.
- **Funkcionalita MCP Hostiteľa**:
    - **Registrácia nástrojov**: Udržiava katalóg dostupných nástrojov a ich schopností.
    - **Autentifikácia**: Overuje povolenia na prístup k nástrojom.
    - **Spracovanie požiadaviek**: Spracováva prichádzajúce požiadavky nástrojov od modelu.
    - **Formátovanie odpovedí**: Štruktúruje výstupy nástrojov do formátu, ktorý model dokáže pochopiť.
- **Vykonanie MCP Servera**:
    - **MCP Hostiteľ** smeruje volania nástrojov na jeden alebo viac **MCP Serverov**, z ktorých každý poskytuje špecializované funkcie (napr. vyhľadávanie, výpočty, dotazy na databázu).
    - **MCP Servery** vykonávajú svoje operácie a vracajú výsledky **MCP Hostiteľovi** v konzistentnom formáte.
    - **MCP Hostiteľ** formátuje a odosiela tieto výsledky **AI Modelu**.
- **Dokončenie odpovede**:
    - **AI Model** začlení výstupy nástrojov do konečnej odpovede.
    - **MCP Hostiteľ** pošle túto odpoveď späť **MCP Klientovi**, ktorý ju doručí koncovému používateľovi alebo volajúcemu softvéru.

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

## 👨‍💻 Ako vytvoriť MCP server (s príkladmi)

MCP servery umožňujú rozšíriť schopnosti LLM poskytovaním dát a funkcií.

Pripravení vyskúšať? Tu sú SDK špecifické pre jazyk alebo stack s príkladmi vytvorenia jednoduchých MCP serverov v rôznych jazykoch/stackoch:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk

## 🌍 Reálne použitia MCP

MCP umožňuje širokú škálu aplikácií rozšírením schopností AI:

| **Aplikácia**              | **Popis**                                                                |
|----------------------------|-------------------------------------------------------------------------|
| Integrácia podnikových dát | Prepojenie LLM s databázami, CRM alebo internými nástrojmi              |
| Agentické AI systémy       | Umožnenie autonómnych agentov s prístupom k nástrojom a pracovným postupom|
| Multimodálne aplikácie     | Kombinácia textových, obrazových a zvukových nástrojov v jednej AI aplikácii|
| Integrácia reálnych dát    | Prinesenie živých dát do AI interakcií pre presnejšie a aktuálne výstupy |

### 🧠 MCP = Univerzálny štandard pre AI interakcie

Model Context Protocol (MCP) funguje ako univerzálny štandard pre AI interakcie, podobne ako USB-C štandardizoval fyzické pripojenia pre zariadenia. Vo svete AI poskytuje MCP konzistentné rozhranie, ktoré umožňuje modelom (klientom) bezproblémovo integrovať externé nástroje a poskytovateľov dát (servery). Tým eliminuje potrebu rôznych vlastných protokolov pre každé API alebo zdroj dát.

Pod MCP, nástroj kompatibilný s MCP (nazývaný MCP server) nasleduje jednotný štandard. Tieto servery môžu uvádzať zoznam nástrojov alebo akcií, ktoré ponúkajú, a vykonávať tieto akcie na požiadanie AI agenta. Platformy AI agentov, ktoré podporujú MCP, sú schopné objaviť dostupné nástroje zo serverov a vyvolať ich prostredníctvom tohto štandardného protokolu.

### 💡 Uľahčuje prístup k znalostiam

Okrem ponúkania nástrojov MCP tiež uľahčuje prístup k znalostiam. Umožňuje aplikáciám poskytovať kontext veľkým jazykovým modelom (LLM) tým, že ich prepojí s rôznymi zdrojmi dát. Napríklad MCP server môže reprezentovať dokumentové úložisko spoločnosti, čo umožňuje agentom na požiadanie získavať relevantné informácie. Iný server môže spracovávať špecifické akcie, ako je odosielanie e-mailov alebo aktualizácia záznamov. Z pohľadu agenta sú to jednoducho nástroje, ktoré môže použiť—niektoré nástroje vracajú dáta (kontext znalostí), zatiaľ čo iné vykonávajú akcie. MCP efektívne spravuje oboje.

Agent, ktorý sa pripája k MCP serveru, automaticky zistí dostupné schopnosti servera a prístupné dáta prostredníctvom štandardného formátu. Táto štandardizácia umožňuje dynamickú dostupnosť nástrojov. Napríklad pridanie nového MCP servera do systému agenta okamžite sprístupní jeho funkcie bez potreby ďalšej úpravy inštrukcií agenta.

Táto zjednodušená integrácia je v súlade s tokmi zobrazenými na nasledujúcom diagrame, kde servery poskytujú nástroje aj znalosti, čím zabezpečujú bezproblémovú spoluprácu naprieč systémami.

### 👉 Príklad: Škálovateľné riešenie pre agentov

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
Univerzálny konektor umožňuje MCP serverom komunikovať a zdieľať schopnosti medzi sebou, čo umožňuje ServerA delegovať úlohy na ServerB alebo pristupovať k jeho nástrojom a znalostiam. Tým sa federujú nástroje a dáta naprieč servermi, podporujúc škálovateľné a modulárne architektúry agentov. Pretože MCP štandardizuje expozíciu nástrojov, agenti môžu dynamicky objavovať a smerovať požiadavky medzi servermi bez pevne zakódovaných integrácií.

Federácia nástrojov a znalostí: Nástroje a dáta môžu byť prístupné naprieč servermi, čo umožňuje škálovateľnejšie a modulárnejšie agentické architektúry.

### 🔄 Pokročilé scenáre MCP s integráciou LLM na strane klienta

Okrem základnej architektúry MCP existujú pokročilé scenáre, kde klient aj server obsahujú LLM, čo umožňuje sofistikovanejšie interakcie. Na nasledujúcom diagrame môže byť **Klientská aplikácia** IDE s množstvom MCP nástrojov dostupných pre používateľa prostredníctvom LLM:

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

## 🔐 Praktické výhody MCP

Tu sú praktické výhody používania MCP:

- **Aktualizovanosť**: Modely môžu pristupovať k aktuálnym informáciám nad rámec ich tréningových dát
- **Rozšírenie schopností**: Modely môžu využívať špecializované nástroje na úlohy, na ktoré neboli trénované
- **Zníženie halucinácií**: Externé zdroje dát poskytujú faktické základy
- **Ochrana súkromia**: Citlivé dáta môžu zostať v bezpečnom prostredí namiesto ich vloženia do príkazov

## 📌 Kľúčové poznatky

Nasledujú kľúčové poznatky o používaní MCP:

- **MCP** štandardizuje, ako AI modely interagujú s nástrojmi a dátami
- Podporuje **rozšíriteľnosť, konzistentnosť a interoperabilitu**
- MCP pomáha **skrátiť čas vývoja, zlepšiť spoľahlivosť a rozšíriť schopnosti modelov**
- Architektúra klient-server **umožňuje flexibilné, rozšíriteľné AI aplikácie**

## 🧠 Cvičenie

Premýšľajte o AI aplikácii, ktorú by ste chceli vytvoriť.

- Ktoré **externé nástroje alebo dáta** by mohli zlepšiť jej schopnosti?
- Ako by MCP mohol urobiť integráciu **jednoduchšou a spoľahlivejšou?**

## Ďalšie zdroje

- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

## Čo ďalej

Ďalej: [Kapitola 1: Základné koncepty](../01-CoreConcepts/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.