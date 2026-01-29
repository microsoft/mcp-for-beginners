# Bevezetés a Model Context Protocol (MCP) protokollba: Miért fontos a skálázható AI alkalmazásokhoz?

[![Bevezetés a Model Context Protocol protokollba](../../../translated_images/hu/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

A generatív AI alkalmazások nagy előrelépést jelentenek, mivel gyakran lehetővé teszik, hogy a felhasználó természetes nyelvi utasításokkal lépjen kapcsolatba az alkalmazással. Azonban, ahogy egyre több időt és erőforrást fektetünk ezekbe az alkalmazásokba, fontos biztosítani, hogy könnyen integrálhatóak legyenek a funkciók és erőforrások, hogy az alkalmazás könnyen bővíthető legyen, több modell használatát is támogassa, és kezelje a különböző modellek sajátosságait. Röviden, a generatív AI alkalmazások építése kezdetben egyszerű, de ahogy növekednek és bonyolultabbá válnak, szükségessé válik egy architektúra meghatározása, és valószínűleg egy szabványra lesz szükség, hogy az alkalmazások következetesen épüljenek. Itt lép be az MCP, hogy rendszert teremtsen és szabványt biztosítson.

---

## **🔍 Mi az a Model Context Protocol (MCP)?**

A **Model Context Protocol (MCP)** egy **nyílt, szabványosított interfész**, amely lehetővé teszi, hogy a nagy nyelvi modellek (LLM-ek) zökkenőmentesen lépjenek kapcsolatba külső eszközökkel, API-kkal és adatforrásokkal. Egy következetes architektúrát biztosít, amely javítja az AI modellek funkcionalitását a tanítási adataikon túl, lehetővé téve okosabb, skálázhatóbb és érzékenyebb AI rendszerek létrehozását.

---

## **🎯 Miért fontos a szabványosítás az AI területén?**

Ahogy a generatív AI alkalmazások egyre bonyolultabbá válnak, elengedhetetlen olyan szabványok elfogadása, amelyek biztosítják a **skálázhatóságot, bővíthetőséget, karbantarthatóságot**, és **elkerülik a gyártói függőséget**. Az MCP ezekre az igényekre ad választ az alábbiak révén:

- Modellek és eszközök integrációjának egységesítése
- Törékeny, egyedi megoldások csökkentése
- Több különböző gyártótól származó modellek egyetlen ökoszisztémában való együttműködésének lehetővé tétele

**Megjegyzés:** Bár az MCP nyílt szabványként hirdeti magát, nincs terv arra, hogy az MCP-t bármely meglévő szabványosító testület, például IEEE, IETF, W3C, ISO vagy más testület által szabványosítsák.

---

## **📚 Tanulási célok**

A cikk végére képes leszel:

- Meghatározni a **Model Context Protocol (MCP)** fogalmát és felhasználási területeit
- Megérteni, hogyan szabványosítja az MCP a modellek és eszközök közötti kommunikációt
- Azonosítani az MCP architektúra alapvető elemeit
- Felfedezni az MCP valós alkalmazásait vállalati és fejlesztési környezetben

---

## **💡 Miért számít áttörésnek a Model Context Protocol (MCP)?**

### **🔗 Az MCP megoldja az AI interakciók széttöredezettségét**

Az MCP előtt a modellek és eszközök integrációja az alábbiakat igényelte:

- Egyedi kód minden eszköz-modell párosra
- Nem szabványos API-k minden gyártóhoz
- Gyakori hibák frissítések miatt
- Rossz skálázhatóság több eszköz esetén

### **✅ Az MCP szabványosítás előnyei**

| **Előny**                  | **Leírás**                                                                     |
|----------------------------|-------------------------------------------------------------------------------|
| Interoperabilitás          | Az LLM-ek zökkenőmentesen működnek különböző gyártók eszközeivel              |
| Következetesség            | Egységes viselkedés platformok és eszközök között                            |
| Újrafelhasználhatóság      | Egyszer létrehozott eszközök több projektben és rendszerben is használhatók  |
| Gyorsabb fejlesztés        | Csökkenti a fejlesztési időt szabványos, plug-and-play interfészek révén     |

---

## **🧱 Az MCP architektúra magas szintű áttekintése**

Az MCP egy **kliens-szerver modellt** követ, ahol:

- **MCP Hostok** futtatják az AI modelleket
- **MCP Kliensek** kezdeményezik a kéréseket
- **MCP Szerverek** biztosítják a kontextust, eszközöket és képességeket

### **Főbb elemek:**

- **Erőforrások** – Statikus vagy dinamikus adatok a modellek számára  
- **Utasítások** – Előre meghatározott munkafolyamatok irányított generáláshoz  
- **Eszközök** – Végrehajtható funkciók, mint keresés, számítások  
- **Mintavétel** – Ügynöki viselkedés rekurzív interakciók révén  

---

## Hogyan működnek az MCP szerverek?

Az MCP szerverek az alábbi módon működnek:

- **Kérés folyamata**:
    1. Egy végfelhasználó vagy az ő nevében működő szoftver kezdeményezi a kérést.
    2. Az **MCP Kliens** elküldi a kérést egy **MCP Hostnak**, amely kezeli az AI modell futtatását.
    3. Az **AI Modell** megkapja a felhasználói utasítást, és szükség esetén külső eszközökhöz vagy adatokhoz fordulhat egy vagy több eszközhívás révén.
    4. Az **MCP Host**, nem közvetlenül a modell, kommunikál a megfelelő **MCP Szerver(ekkel)** a szabványos protokoll használatával.
- **MCP Host funkciói**:
    - **Eszközregiszter**: Katalógust tart fenn az elérhető eszközökről és képességeikről.
    - **Hitelesítés**: Ellenőrzi az eszközök eléréséhez szükséges jogosultságokat.
    - **Kéréskezelő**: Feldolgozza a modell által érkező eszközkéréseket.
    - **Válaszformázó**: Az eszközök kimenetét olyan formátumba alakítja, amelyet a modell megért.
- **MCP Szerver végrehajtás**:
    - Az **MCP Host** az eszközhívásokat egy vagy több **MCP Szerverhez** irányítja, amelyek speciális funkciókat kínálnak (pl. keresés, számítások, adatbázis-lekérdezések).
    - Az **MCP Szerverek** végrehajtják a műveleteiket, és az eredményeket következetes formátumban visszaküldik az **MCP Hostnak**.
    - Az **MCP Host** formázza és továbbítja ezeket az eredményeket az **AI Modellnek**.
- **Válasz befejezése**:
    - Az **AI Modell** beépíti az eszközök kimenetét a végső válaszba.
    - Az **MCP Host** visszaküldi ezt a választ az **MCP Kliensnek**, amely eljuttatja azt a végfelhasználóhoz vagy a hívó szoftverhez.

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

## 👨‍💻 Hogyan építsünk MCP szervert (példákkal)

Az MCP szerverek lehetővé teszik az LLM képességek bővítését adatok és funkcionalitás biztosításával.

Készen állsz kipróbálni? Íme nyelv- és/vagy stack-specifikus SDK-k példákkal, amelyek bemutatják egyszerű MCP szerverek létrehozását különböző nyelveken/stackekben:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk

## 🌍 Valós alkalmazási példák az MCP-re

Az MCP számos alkalmazást tesz lehetővé az AI képességek bővítésével:

| **Alkalmazás**              | **Leírás**                                                                     |
|-----------------------------|-------------------------------------------------------------------------------|
| Vállalati adatintegráció    | LLM-ek összekapcsolása adatbázisokkal, CRM-ekkel vagy belső eszközökkel       |
| Ügynöki AI rendszerek       | Autonóm ügynökök eszközhozzáféréssel és döntéshozatali munkafolyamatokkal     |
| Multimodális alkalmazások   | Szöveg, kép és hang eszközök kombinálása egyetlen AI alkalmazásban            |
| Valós idejű adatintegráció  | Élő adatok bevonása az AI interakciókba pontosabb, aktuális kimenetekért      |

### 🧠 MCP = Univerzális szabvány az AI interakciókhoz

A Model Context Protocol (MCP) univerzális szabványként működik az AI interakciókhoz, hasonlóan ahhoz, ahogy a USB-C szabványosította az eszközök fizikai csatlakozását. Az AI világában az MCP egy következetes interfészt biztosít, amely lehetővé teszi, hogy a modellek (kliensek) zökkenőmentesen integrálódjanak külső eszközökkel és adatforrásokkal (szerverekkel). Ez megszünteti az egyedi protokollok szükségességét minden API-hoz vagy adatforráshoz.

Az MCP alatt egy MCP-kompatibilis eszköz (MCP szerverként említve) egy egységes szabványt követ. Ezek a szerverek felsorolhatják az általuk kínált eszközöket vagy műveleteket, és végrehajthatják ezeket a műveleteket, amikor egy AI ügynök kéri. Az MCP-t támogató AI ügynök platformok képesek felfedezni a szerverek által kínált eszközöket, és szabványos protokollon keresztül meghívni azokat.

### 💡 Tudáshozzáférés megkönnyítése

Az eszközök biztosításán túl az MCP megkönnyíti a tudáshozzáférést is. Lehetővé teszi, hogy az alkalmazások kontextust biztosítsanak a nagy nyelvi modelleknek (LLM-eknek) különböző adatforrásokhoz való kapcsolódás révén. Például egy MCP szerver képviselheti egy vállalat dokumentumtárát, lehetővé téve az ügynökök számára, hogy releváns információkat kérjenek le igény szerint. Egy másik szerver kezelhet specifikus műveleteket, mint például e-mailek küldése vagy rekordok frissítése. Az ügynök szempontjából ezek egyszerűen eszközök, amelyeket használhat—egyes eszközök adatokat adnak vissza (tudáskontextus), míg mások műveleteket hajtanak végre. Az MCP hatékonyan kezeli mindkettőt.

Egy ügynök, amely csatlakozik egy MCP szerverhez, automatikusan megtanulja a szerver elérhető képességeit és hozzáférhető adatait egy szabványos formátumon keresztül. Ez a szabványosítás lehetővé teszi a dinamikus eszközhozzáférést. Például egy új MCP szerver hozzáadása egy ügynök rendszeréhez azonnal használhatóvá teszi annak funkcióit anélkül, hogy további testreszabásra lenne szükség az ügynök utasításaiban.

Ez az egyszerűsített integráció összhangban van az alábbi diagrammal, ahol a szerverek eszközöket és tudást biztosítanak, biztosítva a rendszerek közötti zökkenőmentes együttműködést.

### 👉 Példa: Skálázható ügynöki megoldás

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
Az Univerzális Csatlakozó lehetővé teszi, hogy az MCP szerverek kommunikáljanak és megosszák képességeiket egymással, lehetővé téve, hogy ServerA feladatokat delegáljon ServerB-nek, vagy hozzáférjen annak eszközeihez és tudásához. Ez az eszközök és adatok szerverek közötti szövetségét támogatja, skálázható és moduláris ügynöki architektúrákat biztosítva. Mivel az MCP szabványosítja az eszközök bemutatását, az ügynökök dinamikusan felfedezhetik és irányíthatják a kéréseket a szerverek között anélkül, hogy keményen kódolt integrációkra lenne szükség.

Eszköz- és tudásszövetség: Az eszközök és adatok hozzáférhetők a szerverek között, lehetővé téve skálázhatóbb és modulárisabb ügynöki architektúrákat.

### 🔄 Fejlett MCP forgatókönyvek kliensoldali LLM integrációval

Az alapvető MCP architektúrán túl vannak fejlett forgatókönyvek, ahol mind a kliens, mind a szerver tartalmaz LLM-eket, lehetővé téve kifinomultabb interakciókat. Az alábbi diagramon a **Kliensalkalmazás** lehet egy IDE, amely számos MCP eszközt kínál az LLM számára:

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

## 🔐 Az MCP gyakorlati előnyei

Az MCP használatának gyakorlati előnyei:

- **Frissesség**: A modellek hozzáférhetnek naprakész információkhoz a tanítási adataikon túl
- **Képességbővítés**: A modellek speciális eszközöket használhatnak olyan feladatokhoz, amelyekre nem lettek kiképezve
- **Csökkentett hallucinációk**: Külső adatforrások biztosítják a tényeken alapuló alapozást
- **Adatvédelem**: Érzékeny adatok biztonságos környezetben maradhatnak, ahelyett, hogy utasításokba ágyazódnának

## 📌 Főbb tanulságok

Az MCP használatának főbb tanulságai:

- Az **MCP** szabványosítja, hogyan lépnek kapcsolatba az AI modellek az eszközökkel és adatokkal
- Elősegíti a **bővíthetőséget, következetességet és interoperabilitást**
- Az MCP segít **csökkenteni a fejlesztési időt, javítani a megbízhatóságot és bővíteni a modell képességeit**
- A kliens-szerver architektúra **rugalmas, bővíthető AI alkalmazásokat tesz lehetővé**

## 🧠 Gyakorlat

Gondolj egy AI alkalmazásra, amelyet szeretnél létrehozni.

- Milyen **külső eszközök vagy adatok** javíthatnák a képességeit?
- Hogyan tehetné az MCP az integrációt **egyszerűbbé és megbízhatóbbá**?

## További források

- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

## Mi következik?

Következő: [1. fejezet: Alapfogalmak](../01-CoreConcepts/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.