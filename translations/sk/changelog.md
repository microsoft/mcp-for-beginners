# Zmeny: MCP pre začiatočníkov - kurikulum

Tento dokument slúži ako záznam všetkých významných zmien vykonaných v kurikulu Model Context Protocol (MCP) pre začiatočníkov. Zmeny sú zaznamenané v obrátenom chronologickom poradí (najnovšie zmeny najskôr).

## 11. apríl 2026

### Nová lekcia, opravy dokumentácie a aktualizácie závislostí

#### Pridaný nový obsah kurikula

**Modul 05 - Pokročilé témy**
- **Lekcia 5.17: Adversariálne viac-agentové uvažovanie s MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nový komplexný sprievodca pokrývajúci vzor adversariálneho debatujúceho pre viac-agentové systémy
  - Mermaid diagram architektúry: dvaja agenti → zdieľaný MCP server → prepis debaty → sudca → rozsudok
  - Zdieľaný MCP nástrojový server (`web_search` + `run_python`) implementovaný v Pythone a TypeScripte
  - Protiľahlé systémové výzvy (ZA / PROTI / Sudca) s explicitnými požiadavkami na použitie nástrojov
  - Orchestrátor debaty v Pythone, TypeScripte a C# riadiaci kolá a smerovanie argumentov
  - Zapojenie MCP `ClientSession` pre orchestrátor na reálne volania nástrojov
  - Tabuľka prípadov použitia (detekcia halucinácií, hrozby, revízia návrhu API, overovanie faktov, výber technológií)
  - Bezpečnostné úvahy: spúšťanie v sandboxe, validácia volaní nástrojov, obmedzenie rýchlosti, auditné logy
  - Štruktúrované cvičenie s troma praktickými scénarami (prehľad kódu, rozhodnutie architektúry, moderovanie obsahu)

#### Opravy dokumentácie

**Modul 03 - Začíname**
- **05-stdio-server/README.md**: Opravený neúplný príklad TypeScript stdio servera — doplnená chýbajúca inštancia transportu (`new StdioServerTransport()`) a volanie `server.connect(transport)` pre zhodu s príkladmi v Pythone a .NET v rovnakej sekcii
- **14-sampling/README.md**: Opravená preklep — upravené `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aktualizácie kurikula

**Hlavný README.md**
- Pridaný záznam 5.17 (Adversariálne viac-agentové uvažovanie s MCP) do tabuľky kurikula s priamym odkazom na novú lekciu

**05-AdvancedTopics/README.md**
- Pridaný riadok Lekcie 5.17 do tabuľky lekcií

**study_guide.md**
- Pridaná téma Adversariálne viac-agentové uvažovanie do myšlienkovej mapy a popisu pokročilých tém

#### Opravy kódu a bezpečnosti

**Modul 05 - Adversariálni agenti (`mcp-adversarial-agents`)**
- **Bezpečnostná oprava — injekcia príkazov**: Nahradené interpolovanie shellu `execSync` pomocou `execFile` + `promisify` v TypeScript nástroji `run_python`, čo odstránilo možnosť injekcie príkazov (kód riadený LLM sa teraz posiela ako doslovný prvok argv bez zapojenia shellu)
- **Zapojenie slučky MCP nástrojov**: Aktualizovaný Python orchestrátor debaty na použitie klienta `AsyncAnthropic` (nahrádzajúceho blokujúci sync `Anthropic`), prenos aktívnej `ClientSession` priamo do každého kola agenta, získavanie definícií nástrojov cez `session.list_tools()` v každom kole a odosielanie blokov `tool_use` cez `session.call_tool()` v slučke až do konečného textového výstupu modelu

#### Aktualizácie závislostí

- Aktualizovaný `hono` na 4.12.12 vo viacerých balíkoch (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aktualizovaný `@hono/node-server` z 1.19.11 na 1.19.13 v TypeScript balíkoch
- Aktualizovaný `cryptography` z 46.0.5 na 46.0.7 v Python balíkoch (10-StreamliningAIWorkflows laby 3 a 4)
- Aktualizovaný `lodash` z 4.17.23 na 4.18.1 v inšpektore 10-StreamliningAIWorkflows

#### Preklady

- Synchronizované preklady pre 48+ jazykov s najnovšími zdrojovými zmenami (i18n aktualizácia)

---

## 5. február 2026

### Validácia a zlepšenia navigácie v celom repozitári

#### Pridaný nový obsah kurikula

**Modul 03 - Začíname**
- **12-mcp-hosts/README.md**: Nový komplexný sprievodca nastavením MCP hostiteľov
  - Konfiguračné príklady pre Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Šablóny JSON konfigurácie pre všetkých hlavných hostiteľov
  - Porovnávacia tabuľka typov transportu (stdio, SSE/HTTP, WebSocket)
  - Riešenie bežných problémov s pripojením
  - Bezpečnostné najlepšie praktiky pre konfiguráciu hostiteľa

- **13-mcp-inspector/README.md**: Nový sprievodca ladením pre MCP Inspector
  - Spôsoby inštalácie (npx, globálny npm, zo zdroja)
  - Pripojenie k serverom cez stdio a HTTP/SSE
  - Testovacie nástroje, zdroje a workflowy výziev
  - Integrácia MCP Inspector v VS Code
  - Bežné scenáre ladenia s riešeniami

**Modul 04 - Praktická implementácia**
- **pagination/README.md**: Nový sprievodca implementáciou stránkovania
  - Vzory stránkovania na základe kurzora v Pythone, TypeScripte, Jave
  - Spracovanie stránkovania na klientskej strane
  - Stratégie návrhu kurzora (nepriehľadný vs. štruktúrovaný)
  - Odporúčania na optimalizáciu výkonu

**Modul 05 - Pokročilé témy**
- **mcp-protocol-features/README.md**: Nový podrobný pohľad na funkcie protokolu
  - Implementácia notifikácií o pokroku
  - Vzory rušenia požiadaviek
  - Šablóny zdrojov s vzormi URI
  - Správa životného cyklu servera
  - Riadenie úrovne logovania
  - Vzory spracovania chýb s JSON-RPC kódmi

#### Opravy navigácie (aktualizovaných 24+ súborov)

**Hlavné README modulov**
 Odkazuje teraz na prvú lekciu AJ ďalší modul

**Podské súbory 02-Security**
- Všetky 5 doplnkových bezpečnostných dokumentov majú teraz navigáciu „Čo je ďalej“:

**Súbory 09-CaseStudy**
- Všetky súbory prípadových štúdií majú teraz sekvenčnú navigáciu:

**Laby 10-StreamliningAI**
Pridaná časť Čo je ďalej k prehľadu Modulu 10 a modulu 11

#### Opravy kódu a obsahu

**Aktualizácie SDK a závislostí**
Opravená prázdna verzia openai na `^4.95.0`
Aktualizované SDK z `^1.8.0` na `>=1.26.0`
Aktualizované verzie mcp na `>=1.26.0`

**Opravy kódu**
Opravený neplatný model `gpt-4o-mini` na `gpt-4.1-mini`

**Opravy obsahu**
Opravený zlomený odkaz `READMEmd` → `README.md`, opravený nadpis kurikula `Module 1-3` → `Module 0-3`, opravená veľkosť písmen v ceste
Odstránený poškodený duplicitný obsah Prípadu štúdie 5

**Zlepšenia pre začiatočníkov**
Pridaný správny úvod, učebné ciele a predpoklady pre začiatočníkov

#### Aktualizácie kurikula

**Hlavný README.md**
- Pridané záznamy 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Stránkovanie), 5.16 (Funkcie protokolu) do tabuľky kurikula

**Modulové README**
Pridané lekcie 12 a 13 do zoznamu lekcií
Pridaná sekcia Praktické príručky so stránkovaním
Pridané lekcie 5.15 (Vlastný transport) a 5.16 (Funkcie protokolu)

**study_guide.md**
- Aktualizovaná myšlienková mapa o všetky nové témy: nastavenie MCP Hostov, MCP Inspector, stratégie stránkovania, podrobný pohľad na funkcie protokolu

## 28. január 2026

### Preskúmanie súladu špecifikácie MCP 2025-11-25

#### Vylepšenie základných konceptov (01-CoreConcepts/)
- **Nová klientská primitiva - Roots**: Pridaná obsiahla dokumentácia na primitivum klienta Roots, umožňujúca serverom chápať hranice súborového systému a prístupové práva
- **Anotácie nástrojov**: Pridaná dokumentácia na behaviorálne anotácie nástrojov (`readOnlyHint`, `destructiveHint`) pre lepšie rozhodovanie pri spúšťaní nástrojov
- **Volanie nástrojov pri vzorkovaní**: Aktualizovaná dokumentácia vzorkovania o parametre `tools` a `toolChoice` pre volanie nástrojov riadené modelom počas požiadaviek vzorkovania
- **URL Mode Elicitation**: Pridaná dokumentácia o vyvolávaní na báze URL pre externé webové interakcie iniciované serverom
- **Úlohy (experimentálne)**: Pridaná nová sekcia dokumentujúca experimentálnu funkciu Úloh pre trvalé vykonávacie obaly a odložené získavanie výsledkov
- **Podpora ikon**: Poznamenané, že nástroje, zdroje, šablóny zdrojov a výzvy môžu teraz obsahovať ikony ako ďalšie metaúdaje

#### Aktualizácie dokumentácie
- **README.md**: Pridaná referencia na verziu špecifikácie MCP 2025-11-25 a vysvetlenie verziovania podľa dátumu
- **study_guide.md**: Aktualizovaná mapa kurikula o Úlohy a Anotácie nástrojov v sekcii Základné koncepty; aktualizovaný časový údaj dokumentu

#### Overenie súladu so špecifikáciou
- **Verzia protokolu**: Overené, že všetka dokumentácia odkazuje na aktuálnu špecifikáciu MCP 2025-11-25
- **Zladenie architektúry**: Potvrdená presnosť dokumentácie dvojvrstvovej architektúry (Dátová vrstva + Transportná vrstva)
- **Dokumentácia primítív**: Validované serverové primitivá (Zdroje, Výzvy, Nástroje) a klientské primitivá (Vzorkovanie, Elicitation, Logging, Roots)
- **Mechanizmy transportu**: Overená presnosť dokumentácie STDIO a Streamable HTTP transportu
- **Bezpečnostné usmernenia**: Potvrdené zladenie so súčasnými bezpečnostnými najlepšími praktikami MCP

#### Kľúčové funkcie MCP 2025-11-25 zdokumentované
- **OpenID Connect Discovery**: Objev autentifikačného servera cez OIDC
- **OAuth Client ID Metadata Dokumenty**: Odporúčaný mechanizmus registrácie klienta
- **JSON Schema 2020-12**: Predvolený dialekt pre definície MCP schém
- **SDK Tiering System**: Formalizované požiadavky na podporu a údržbu funkcií SDK
- **Štruktúra správy**: Formalizované pracovné skupiny a záujmové skupiny v MCP správe

### Veľká aktualizácia dokumentácie bezpečnosti (02-Security/)

#### Integrácia workshopu MCP Security Summit (Sherpa)
- **Nový praktický tréningový zdroj**: Pridaná komplexná integrácia s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) v celej bezpečnostnej dokumentácii
- **Pokrytie trasy expedície**: Zdokumentovaný kompletný postup camp-to-camp od základného tábora po vrchol
- **Zladenie s OWASP**: Všetky bezpečnostné odporúčania mapované na riziká OWASP MCP Azure Security Guide

#### Integrácia OWASP MCP Top 10
- **Nová sekcia**: Pridaná tabuľka OWASP MCP Top 10 bezpečnostných rizík s Azure mitigáciami v hlavnom bezpečnostnom README
- **Dokumentácia založená na rizikách**: Aktualizovaný súbor mcp-security-controls-2025.md o odkazy na OWASP MCP riziká pre každú bezpečnostnú doménu
- **Referenčná architektúra**: Linky na referenčnú architektúru a implementačné vzory OWASP MCP Azure Security Guide

#### Aktualizované bezpečnostné súbory
- **README.md**: Pridaný prehľad workshopu Sherpa, tabuľka trasy expedície, súhrn rizík OWASP MCP Top 10 a časť o praktickom tréningu
- **mcp-security-controls-2025.md**: Aktualizovaný nadpis na február 2026, pridané odkazy na OWASP riziká (MCP01-MCP08), opravená nejednotnosť verzie špecifikácie
- **mcp-security-best-practices-2025.md**: Pridaná sekcia zdrojov Sherpa a OWASP, aktualizovaný časový údaj
- **mcp-best-practices.md**: Pridaná sekcia praktického tréningu so Sherpa a OWASP odkazmi
- **azure-content-safety-implementation.md**: Pridaný odkaz na OWASP MCP06, zladenie s táborom Sherpa 3 a sekcia ďalších zdrojov

#### Pridané nové odkazy na zdroje
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Jednotlivé stránky rizík OWASP MCP (MCP01-MCP10)

### Zladenie celého kurikula so špecifikáciou MCP 2025-11-25

#### Modul 03 - Začíname
- **Dokumentácia SDK**: Pridané Go SDK do oficiálneho zoznamu SDK; aktualizované všetky odkazy SDK na zladenie so špecifikáciou MCP 2025-11-25
- **Vysvetlenie transportu**: Aktualizované popisy protokolu STDIO a HTTP Streaming s explicitnými odkazmi na špecifikáciu

#### Modul 04 - Praktická implementácia
- **Aktualizácie SDK**: Pridané Go SDK; aktualizovaný zoznam SDK s referenciou na verziu špecifikácie
- **Špecifikácia autorizácie**: Aktualizovaný odkaz na MCP Authorization špecifikáciu na aktuálnu verziu 2025-11-25

#### Modul 05 - Pokročilé témy
- **Nové funkcie**: Pridaná poznámka o nových funkciách MCP Špecifikácie 2025-11-25 (Úlohy, Anotácie nástrojov, URL Mode Elicitation, Roots)
- **Bezpečnostné zdroje**: Pridané odkazy na OWASP MCP Top 10 a workshop Sherpa do doplnkových referencií

#### Modul 06 - Príspevky komunity
- **Zoznam SDK**: Pridané Swift a Rust SDK; aktualizovaný odkaz na špecifikáciu na 2025-11-25

#### Modul 07 - Lekcie z prvého nasadenia
- **Aktualizácie zdrojov**: Pridaný odkaz na MCP Špecifikáciu 2025-11-25 a OWASP MCP Top 10 do doplnkových zdrojov

#### Modul 08 - Najlepšie praktiky
- **Verzia špecifikácie**: Aktualizovaný odkaz na MCP Špecifikáciu 2025-11-25
- **Bezpečnostné zdroje**: Pridané OWASP MCP Top 10 a workshop Sherpa do doplnkových referencií

#### Modul 10 - Zjednodušovanie AI workflowov
- **Aktualizácia odznaku**: Zmenený odznak verzie MCP z verzie SDK (1.9.3) na verziu špecifikácie (2025-11-25)
- **Odkazy na zdroje**: Aktualizovaný odkaz na MCP Špecifikáciu; pridaný OWASP MCP Top 10

#### Modul 11 - MCP Server Hands-On laby
- **Odkaz na špecifikáciu**: Aktualizovaný odkaz na verziu 2025-11-25
- **Bezpečnostné zdroje**: Pridaný OWASP MCP Top 10 do oficiálnych zdrojov

## 18. december 2025
### Aktualizácia bezpečnostnej dokumentácie - špecifikácia MCP 2025-11-25

#### Najlepšie bezpečnostné postupy MCP (02-Security/mcp-best-practices.md) - aktualizácia verzie špecifikácie
- **Aktualizácia verzie protokolu**: Aktualizované odkazy na najnovšiu špecifikáciu MCP 2025-11-25 (uvoľnenú 25. novembra 2025)
  - Aktualizované všetky odkazy na verziu špecifikácie z 18.06.2025 na 25.11.2025
  - Aktualizované dátumy v dokumente z 18. augusta 2025 na 18. decembra 2025
  - Overené, že všetky URL špecifikácie smerujú na aktuálnu dokumentáciu
- **Validácia obsahu**: Komplexná kontrola najlepších bezpečnostných postupov podľa najnovších štandardov
  - **Microsoft bezpečnostné riešenia**: Overená aktuálna terminológia a odkazy pre Prompt Shields (predtým "detekcia rizika jailbreaku"), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 bezpečnosť**: Potvrdená zhoda s najnovšími bezpečnostnými postupmi OAuth
  - **OWASP štandardy**: Overené, že odkazy na OWASP Top 10 pre LLM zostávajú aktuálne
  - **Azure služby**: Overené všetky dokumentačné odkazy Microsoft Azure a najlepšie postupy
- **Zladenie so štandardmi**: Všetky referencované bezpečnostné štandardy sú aktuálne
  - NIST Rámec riadenia rizík AI
  - ISO 27001:2022
  - Najlepšie bezpečnostné postupy OAuth 2.1
  - Azure bezpečnostné a súladové rámce
- **Implementačné zdroje**: Overené všetky odkazy na implementačné príručky a zdroje
  - Overovanie Azure API Management vzory
  - Integrácie Microsoft Entra ID
  - Správa tajomstiev Azure Key Vault
  - DevSecOps pipeliny a monitorovacie riešenia

### Kontrola kvality dokumentácie
- **Súlad so špecifikáciou**: Overené, že všetky povinné bezpečnostné požiadavky MCP (MUST/MUST NOT) sú v súlade s najnovšou špecifikáciou
- **Aktualitu zdrojov**: Overené všetky externé odkazy na dokumentáciu Microsoft, bezpečnostné štandardy a implementačné príručky
- **Pokrytie najlepších postupov**: Potvrdené komplexné pokrytie autentifikácie, autorizácie, AI-špecifických hrozieb, bezpečnosti dodávateľského reťazca a podnikových vzorov

## 6. október 2025

### Rozšírenie sekcie Začíname – Pokročilé použitie servera a jednoduchá autentifikácia

#### Pokročilé použitie servera (03-GettingStarted/10-advanced)
- **Pridaná nová kapitola**: Predstavený komplexný návod na pokročilé použitie MCP servera, zahŕňajúci štandardnú aj nízkoúrovňovú serverovú architektúru.
  - **Štandardný vs. nízkoúrovňový server**: Podrobná komparácia a ukážky kódu v Pythone a TypeScripte pre oba prístupy.
  - **Dizajn založený na handleroch**: Vysvetlenie manažmentu nástrojov/zdrojov/promptov založeného na handleroch pre škálovateľné a flexibilné serverové implementácie.
  - **Praktické vzory**: Reálne scenáre, kde sú nízkoúrovňové serverové vzory užitočné pre pokročilé funkcie a architektúru.

#### Jednoduchá autentifikácia (03-GettingStarted/11-simple-auth)
- **Pridaná nová kapitola**: Krok za krokom návod na implementáciu jednoduchej autentifikácie v MCP serveroch.
  - **Koncepty autentifikácie**: Jasné vysvetlenie rozdielu medzi autentifikáciou a autorizáciou, a spracovania prihlasovacích údajov.
  - **Implementácia základnej autentifikácie**: Vzory autentifikácie s middleware v Pythone (Starlette) a TypeScripte (Express) s príkladmi kódu.
  - **Pokrok ku pokročilej bezpečnosti**: Návod na začatie s jednoduchou autentifikáciou a prechod na OAuth 2.1 a RBAC, s odkazmi na pokročilé bezpečnostné moduly.

Tieto prídavky poskytujú praktické a aplikované návody pre vývoj robustnejších, bezpečnejších a flexibilnejších MCP serverových implementácií, prepájajúc základné koncepty s pokročilými produkčnými vzormi.

## 29. september 2025

### MCP Server Database Integration Labs – komplexné praktické učebné cesty

#### 11-MCPServerHandsOnLabs – nový kompletný kurz integrácie databázy
- **Kompletná 13-dielna úroveň laboratórií**: Pridaný komplexný praktický kurz na výstavbu produkčne pripravených MCP serverov s integráciou PostgreSQL databázy
  - **Reálny prípad použitia**: Analytika Zava Retail pre demonštráciu podnikových vzorov
  - **Štruktúrovaný progres učím sa**:
    - **Laboratóriá 00-03: Základy** - Úvod, jadrová architektúra, bezpečnosť a multi-tenancy, nastavenie prostredia
    - **Laboratóriá 04-06: Výstavba MCP servera** - Návrh databázy a schéma, implementácia MCP servera, vývoj nástrojov
    - **Laboratóriá 07-09: Pokročilé funkcie** - Integrácia sémantického vyhľadávania, testovanie a ladenie, integrácia do VS Code
    - **Laboratóriá 10-12: Produkcia a najlepšie postupy** - Nasadzovacie stratégie, monitoring a pozorovateľnosť, najlepšie postupy a optimalizácia
  - **Podnikové technológie**: Rámec FastMCP, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Pokročilé funkcie**: Row Level Security (RLS), sémantické vyhľadávanie, viaceré nájomnícke prístupy k dátam, vektorové embeddings, real-time monitoring

#### Štandardizácia terminológie – konverzia modulov na laboratóriá
- **Komplexná aktualizácia dokumentácie**: Systematická aktualizácia všetkých README súborov v 11-MCPServerHandsOnLabs na používanie termínu "Laboratórium" namiesto "Modul"
  - **Nadpisy sekcií**: Aktualizované "Čo tento modul pokrýva" na "Čo toto laboratórium pokrýva" naprieč všetkými 13 laboratóriami
  - **Popis obsahu**: Zmenené "Tento modul poskytuje..." na "Toto laboratórium poskytuje..." v celej dokumentácii
  - **Vzdelávacie ciele**: Aktualizované "Na konci tohto modulu..." na "Na konci tohto laboratória..."
  - **Navigačné odkazy**: Prevedené všetky odkazy "Modul XX:" na "Laboratórium XX:" v krížových odkazoch a navigácii
  - **Sledovanie dokončenia**: Aktualizované "Po dokončení tohto modulu..." na "Po dokončení tohto laboratória..."
  - **Zachované technické odkazy**: Udržiavané referencie na Python moduly v konfiguračných súboroch (napr. `"module": "mcp_server.main"`)

#### Vylepšenie študijného návodu (study_guide.md)
- **Vizualizácia kurikula**: Pridaná nová sekcia "11. Laboratóriá integrácie databáz" s detailnou štruktúrou laboratórií
- **Štruktúra repozitára**: Aktualizované z desiatich na jedenásť hlavných sekcií s podrobným popisom 11-MCPServerHandsOnLabs
- **Návod na učebnú cestu**: Vylepšené inštrukcie na prehliadanie sekcií 00-11
- **Pokrytie technológií**: Pridané detaily integrácie FastMCP, PostgreSQL a Azure služieb
- **Vzdelávacie výstupy**: Zdôraznený vývoj produkčne pripravených serverov, vzory integrácie databáz a podniková bezpečnosť

#### Vylepšenie hlavnej README štruktúry
- **Terminológia založená na laboratóriách**: Aktualizovaný hlavný README.md v 11-MCPServerHandsOnLabs s konzistentným používaním štruktúry "Laboratórium"
- **Organizácia učebnej cesty**: Jasný progres od základných konceptov cez pokročilú implementáciu až k produkčnému nasadeniu
- **Zameranie na reálny svet**: Dôraz na praktické, skúsenostné učenie s podnikových vzorov a technológií

### Zlepšenia kvality a konzistencie dokumentácie
- **Dôraz na praktické učenie**: Posilnený prístup založený na laboratórnej výučbe v celej dokumentácii
- **Zameranie na podnikové vzory**: Zvýraznené produkčne pripravené implementácie a podnikové bezpečnostné aspekty
- **Integrácia technológií**: Komplexné pokrytie moderných Azure služieb a AI integračných vzorov
- **Progres učebnej cesty**: Jasná a štruktúrovaná cesta od základných konceptov po produkčné nasadenie

## 26. september 2025

### Vylepšenie prípadových štúdií – Integrácia GitHub MCP Registry

#### Prípadové štúdie (09-CaseStudy/) - zameranie na rozvoj ekosystému
- **README.md**: Významné rozšírenie s komplexnou prípadovou štúdiou GitHub MCP Registry
  - **Prípadová štúdia GitHub MCP Registry**: Nová komplexná prípadová štúdia skúmajúca spustenie GitHub MCP Registry v septembri 2025
    - **Analýza problému**: Podrobná analýza fragmentácie objavovania a nasadenia MCP serverov
    - **Architektúra riešenia**: Centralizovaný prístup GitHub registry s inštaláciou VS Code na jeden klik
    - **Obchodný dopad**: Merateľné zlepšenia onboardingového procesu vývojárov a produktivity
    - **Strategická hodnota**: Zameranie na modulárne nasadenie agentov a interoperabilitu medzi nástrojmi
    - **Vývoj ekosystému**: Postavenie ako základnej platformy pre agentickú integráciu
  - **Vylepšená štruktúra prípadových štúdií**: Aktualizované všetkých sedem prípadových štúdií so štandardizovaným formátovaním a komplexným popisom
    - Azure AI Travel Agents: dôraz na viacagentúrsku orchestráciu
    - Azure DevOps integrácia: zameranie na automatizáciu pracovných tokov
    - Zber dokumentácie v reálnom čase: implementácia Python konzolového klienta
    - Interaktívny generátor študijných plánov: Chainlit konverzačná webová aplikácia
    - Dokumentácia v editore: integrácia VS Code a GitHub Copilot
    - Azure API Management: podnikové API integračné vzory
    - GitHub MCP Registry: rozvoj ekosystému a komunítna platforma
  - **Komplexné záverečné zhrnutie**: Prepracovaná záverečná sekcia zvýrazňujúca sedem prípadových štúdií pokrývajúcich rôzne MCP implementačné dimenzie
    - Podniková integrácia, viacagentúrska orchestrácia, produktivita vývojárov
    - Vývoj ekosystému, kategorizácia vzdelávacích aplikácií
    - Zdokonalené poznatky o architektonických vzoroch, implementačných stratégiách a najlepších praktikách
    - Dôraz na MCP ako zrelý, produkčne pripravený protokol

#### Aktualizácie študijného sprievodcu (study_guide.md)
- **Vizualizácia kurikula**: Aktualizovaná myšlienková mapa vrátane GitHub MCP Registry v sekcii Prípadové štúdie
- **Popis prípadových štúdií**: Vylepšené z generických popisov na podrobný rozbor siedmich komplexných prípadových štúdií
- **Štruktúra repozitára**: Aktualizovaná sekcia 10, aby odrážala komplexné pokrytie prípadových štúdií so špecifickými detailmi implementácie
- **Integrácia changelog**: Pridaný záznam 26. septembra 2025 dokumentujúci pridanie GitHub MCP Registry a vylepšenia prípadových štúdií
- **Aktualizácia dátumu**: Aktualizovaný časový údaj v pätičke reflektujúci najnovšiu revíziu (26. september 2025)

### Zlepšenia kvality dokumentácie
- **Zlepšenie konzistencie**: Štandardizované formátovanie a štruktúra prípadových štúdií naprieč všetkými siedmymi príkladmi
- **Komplexné pokrytie**: Prípadové štúdie teraz pokrývajú podnikové, produktivitu vývojárov a rozvoj ekosystému
- **Strategické postavenie**: Zvýraznený dôraz na MCP ako základnú platformu pre nasadenie agentných systémov
- **Integrácia zdrojov**: Aktualizované doplnkové zdroje vrátane odkazu na GitHub MCP Registry

## 15. september 2025

### Rozšírenie pokročilých tém – Vlastné transporty a inžinierstvo kontextu

#### Vlastné MCP transporty (05-AdvancedTopics/mcp-transport/) – nový pokročilý implementačný sprievodca
- **README.md**: Kompletný návod na implementáciu vlastných MCP transportných mechanizmov
  - **Azure Event Grid transport**: Komplexná implementácia bezserverového event-driven transportu
    - Príklady v C#, TypeScript a Pythone s integráciou Azure Functions
    - Event-driven architektonické vzory pre škálovateľné MCP riešenia
    - Príjemcovia webhookov a pushová správa správ
  - **Azure Event Hubs transport**: Implementácia streaming transportu s vysokou priepustnosťou
    - Realtime streamingové schopnosti pre nízku latenciu
    - Stratégií partitioningu a správy checkpointov
    - Zhlukovanie správ a optimalizácia výkonu
  - **Podnikové integračné vzory**: Produkčne pripravené architektonické príklady
    - Distribuované MCP spracovanie cez viaceré Azure Functions
    - Hybridné transportné architektúry kombinujúce viaceré transportné typy
    - Trvanlivosť správ, spoľahlivosť a stratégie pre spracovanie chýb
  - **Bezpečnosť a monitoring**: Integrácia Azure Key Vault a vzory pozorovateľnosti
    - Overovanie spravovaných identít a princíp najmenších privilégií
    - Telemetria Application Insights a monitoring výkonu
    - Circuit breakery a vzory odolnosti voči chybám
  - **Testovacie rámce**: Komplexné testovacie stratégie pre vlastné transporty
    - Jednotkové testovanie s testovacími náhradami a mocking rámcami
    - Integračné testovanie s Azure Test Containers
    - Zváženia výkonového a záťažového testovania

#### Inžinierstvo kontextu (05-AdvancedTopics/mcp-contextengineering/) – vznikajúca AI disciplína
- **README.md**: Komplexná explózia inžinierstva kontextu ako vznikajúceho odboru
  - **Základné princípy**: Kompletné zdieľanie kontextu, povedomie o rozhodovaní o krokoch, a manažment kontextového okna
  - **Zladenie s MCP protokolom**: Ako dizajn MCP rieši výzvy inžinierstva kontextu
    - Obmedzenia kontextového okna a progresívne načítavanie
    - Určenie relevancie a dynamické získavanie kontextu
    - Multimodálne spracovanie kontextu a bezpečnostné ohľady
  - **Implementačné prístupy**: Jednovláknové vs. viacagentúrne architektúry
    - Rozdeľovanie kontextu na kúsky a techniky prioritizácie
    - Progresívne načítavanie a kompresné stratégie kontextu
    - Vrstvené prístupy ku kontextu a optimalizácia získavania
  - **Rámec merania**: Vznikajúce metriky pre hodnotenie efektívnosti kontextu
    - Efektívnosť vstupov, výkon, kvalita a užívateľské skúsenosti
    - Experimentálne prístupy k optimalizácii kontextu
    - Analýza zlyhaní a metodiky zlepšenia

#### Aktualizácie navigácie kurikula (README.md)
- **Vylepšená štruktúra modulov**: Aktualizovaná tabulka kurikula o nové pokročilé témy
  - Pridané položky Context Engineering (5.14) a Custom Transport (5.15)
  - Konzistentné formátovanie a navigačné odkazy vo všetkých moduloch
  - Aktualizované popisy odrážajú rozsah aktuálneho obsahu

### Zlepšenia adresárovej štruktúry
- **Štandardizácia názvov**: Premenovaný "mcp transport" na "mcp-transport" pre konzistentnosť s ostatnými priečinkami pokročilých tém
- **Organizácia obsahu**: Všetky priečinky 05-AdvancedTopics teraz používajú konzistentný názvový vzor (mcp-[téma])

### Vylepšenia kvality dokumentácie
- **Zladenie so špecifikáciou MCP**: Všetok nový obsah odkazuje na aktuálnu špecifikáciu MCP 2025-06-18
- **Príklady vo viacerých jazykoch**: Komplexné ukážky v C#, TypeScript a Python
- **Podnikové zameranie**: Produkčne pripravené vzory a integrácia Azure cloud služieb v celom obsahu
- **Vizualizácia dokumentácie**: Mermaid diagramy pre architektúru a vizualizáciu tokov

## 18. august 2025

### Komplexná aktualizácia dokumentácie – štandardy MCP 2025-06-18

#### Najlepšie bezpečnostné postupy MCP (02-Security/) – kompletná modernizácia
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletná prepísaná verzia v súlade so špecifikáciou MCP 2025-06-18  
  - **Povinné požiadavky**: Pridané explicitné požiadavky MUSÍ/NESMIE z oficiálnej špecifikácie s jasnými vizuálnymi indikátormi  
  - **12 základných bezpečnostných praktík**: Preštruktúrované z 15-položkového zoznamu na komplexné bezpečnostné domény  
    - Bezpečnosť tokenov a autentifikácia s integráciou externého poskytovateľa identity  
    - Správa relácií a zabezpečenie prenosu s kryptografickými požiadavkami  
    - Ochrana proti hrozbám špecifickým pre AI s integráciou Microsoft Prompt Shields  
    - Riadenie prístupu a oprávnení podľa princípu minimálnych práv  
    - Bezpečnosť obsahu a monitorovanie s integráciou Azure Content Safety  
    - Zabezpečenie dodávateľského reťazca s komplexnou verifikáciou komponentov  
    - OAuth bezpečnosť a prevencia zameneného zástupcu s implementáciou PKCE  
    - Reakcia na incidenty a obnova so zabudovanými automatizovanými možnosťami  
    - Súlad a správa s regulačnou harmonizáciou  
    - Pokročilé bezpečnostné kontroly s architektúrou nulovej dôvery  
    - Integrácia ekosystému Microsoft Security s komplexnými riešeniami  
    - Neustály vývoj bezpečnosti s adaptívnymi praktikami  
  - **Microsoft Security Solutions**: Vylepšené pokyny na integráciu Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security  
  - **Implementačné zdroje**: Kategorizované komplexné odkazy na zdroje podľa Oficiálnej MCP dokumentácie, Microsoft Security Solutions, bezpečnostných štandardov a implementačných príručiek  

#### Pokročilé bezpečnostné kontroly (02-Security/) - Implementácia pre podniky  
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletný prepracovanie na podnikový bezpečnostný rámec  
  - **9 komplexných bezpečnostných domén**: Rozšírené z základných kontrol na detailný podnikový rámec  
    - Pokročilá autentifikácia a autorizácia s integráciou Microsoft Entra ID  
    - Bezpečnosť tokenov a kontroly proti presmerovaniu s komplexnou validáciou  
    - Bezpečnostné kontroly relácií s prevenciou únosu relácie  
    - Bezpečnostné kontroly špecifické pre AI s prevenciou injekcie promptu a otravy nástrojov  
    - Prevencia útokov zameneného zástupcu s OAuth proxy zabezpečením  
    - Bezpečnosť vykonávania nástrojov so sandboxingom a izoláciou  
    - Kontroly bezpečnosti dodávateľského reťazca s overovaním závislostí  
    - Kontroly monitorovania a detekcie s integráciou SIEM  
    - Reakcia na incidenty a obnova s automatizovanými možnosťami  
  - **Implementačné príklady**: Pridané podrobné YAML bloky konfigurácie a ukážky kódu  
  - **Integrácia Microsoft riešení**: Komplexný prehľad Azure bezpečnostných služieb, GitHub Advanced Security a správy podnikových identít  

#### Pokročilé bezpečnostné témy (05-AdvancedTopics/mcp-security/) - Produkčne pripravená implementácia  
- **README.md**: Kompletný prepísaný text pre implementáciu podnikovej bezpečnosti  
  - **Súlad s aktuálnou špecifikáciou**: Aktualizované na MCP špecifikáciu 2025-06-18 s povinnými bezpečnostnými požiadavkami  
  - **Vylepšená autentifikácia**: Integrácia Microsoft Entra ID s komplexnými príkladmi .NET a Java Spring Security  
  - **Integrácia AI bezpečnosti**: Implementácia Microsoft Prompt Shields a Azure Content Safety s podrobnými príkladmi v Pythone  
  - **Pokročilá mitigácia hrozieb**: Komplexné implementačné príklady pre  
    - Prevenciu útokov zameneného zástupcu s PKCE a validáciou súhlasu používateľa  
    - Prevenciu presmerovania tokenov s validáciou publika a bezpečnou správou tokenov  
    - Prevenciu únosov relácií s kryptografickým viazaním a behaviorálnou analýzou  
  - **Integrácia podnikového zabezpečenia**: Monitorovanie cez Azure Application Insights, pipeline detekcie hrozieb a zabezpečenie dodávateľského reťazca  
  - **Implementačný kontrolný zoznam**: Jasné rozlíšenie povinných a odporúčaných bezpečnostných kontrol s výhodami Microsoft bezpečnostného ekosystému  

### Kvalita dokumentácie a súlad so štandardmi  
- **Odkazy na špecifikácie**: Aktualizované všetky odkazy na aktuálnu MCP špecifikáciu 2025-06-18  
- **Ekosystém Microsoft Security**: Vylepšené odporúčania na integráciu v celej bezpečnostnej dokumentácii  
- **Praktická implementácia**: Pridané detailné príklady kódu v .NET, Java a Python s podnikateľskými vzormi  
- **Organizácia zdrojov**: Komplexná kategorizácia oficiálnych dokumentov, bezpečnostných štandardov a implementačných príručiek  
- **Vizuálne indikátory**: Jasné označenie povinných požiadaviek vs. odporúčaných praktík  


#### Základné koncepty (01-CoreConcepts/) - Kompletná modernizácia  
- **Aktualizácia verzie protokolu**: Aktualizované na referenciu aktuálnej MCP špecifikácie 2025-06-18 s dátumovým formátom (RRRR-MM-DD)  
- **Zlepšenie architektúry**: Vylepšené opisy Hostiteľov, Klientov a Serverov odrážajúce aktuálne vzory architektúry MCP  
  - Hostitelia teraz jasne definovaní ako AI aplikácie koordinujúce viaceré MCP klientské pripojenia  
  - Klienti popísaní ako protokolové konektory udržiavajúce vzťah 1:1 so serverom  
  - Servery rozšírené o scenáre lokálneho a vzdialeného nasadenia  
- **Prepracovanie primitív**: Kompletné prepracovanie serverových a klientskych primitív  
  - Serverové primitíva: Zdroje (datové zdroje), Prompty (šablóny), Nástroje (spustiteľné funkcie) s detailnými vysvetleniami a príkladmi  
  - Klientské primitíva: Sampling (dokončenia LLM), Elicitation (zadávanie používateľa), Logging (ladenie/monitorovanie)  
  - Aktualizované s aktuálnymi vzormi metód pre objavovanie (`*/list`), získavanie (`*/get`) a vykonávanie (`*/call`)  
- **Architektúra protokolu**: Zavedený dvojvrstvový architektonický model  
  - Úroveň dát: základy JSON-RPC 2.0 s riadením životného cyklu a primitívami  
  - Úroveň prenosu: STDIO (lokálny) a Streamable HTTP s SSE (vzdialený) ako prenosové mechanizmy  
- **Bezpečnostný rámec**: Komplexné bezpečnostné princípy vrátane explicitného súhlasu používateľa, ochrany súkromia dát, bezpečnosti vykonávania nástrojov a bezpečnosti prenosovej vrstvy  
- **Komunikačné vzory**: Aktualizované protokolové správy zobrazujúce inicializáciu, objavovanie, vykonávanie a notifikácie  
- **Príklady kódu**: Osviežené viacjazyčné príklady (.NET, Java, Python, JavaScript) odrážajúce aktuálne MCP SDK vzory  

#### Bezpečnosť (02-Security/) - Komplexné prepracovanie bezpečnosti  
- **Súlad so štandardmi**: Plný súlad s bezpečnostnými požiadavkami MCP špecifikácie 2025-06-18  
- **Vývoj autentifikácie**: Zdokumentovaný vývoj od vlastných OAuth serverov po delegovanie externému poskytovateľovi identity (Microsoft Entra ID)  
- **Analýza hrozieb špecifických pre AI**: Vylepšené pokrytie moderných AI útokových vektorov  
  - Detailné scenáre útokov injekcie promptov s reálnymi príkladmi  
  - Mechanizmy otravy nástrojov a vzory útokov „rug pull“  
  - Otrava kontextového okna a útoky spôsobujúce zmätok modelu  
- **Bezpečnostné riešenia Microsoft AI**: Komplexné pokrytie Microsoft bezpečnostného ekosystému  
  - AI Prompt Shields s pokročilou detekciou, zvýrazňovaním a technikami oddeľovačov  
  - Vzory integrácie Azure Content Safety  
  - GitHub Advanced Security pre ochranu dodávateľského reťazca  
- **Pokročilá mitigácia hrozieb**: Detailné bezpečnostné kontroly pre  
  - Únosi relácií s MCP-špecifickými scenármi útokov a požiadavkami na kryptografické ID relácie  
  - Problémy so zameneným zástupcom v MCP proxy scenároch s explicitnými požiadavkami na súhlas  
  - Zraniteľnosti presmerovania tokenov s povinnými kontrolami validácie  
- **Zabezpečenie dodávateľského reťazca**: Rozšírené pokrytie AI dodávateľského reťazca vrátane základných modelov, embedding služieb, poskytovateľov kontextu a third-party API  
- **Zabezpečenie základov**: Vylepšená integrácia podnikového bezpečnostného vzoru vrátane architektúry nulovej dôvery a Microsoft bezpečnostného ekosystému  
- **Organizácia zdrojov**: Kategorizované komplexné odkazy na zdroje podľa typu (Oficiálne dokumenty, Štandardy, Výskum, Microsoft riešenia, Implementačné návody)  

### Zlepšenia kvality dokumentácie  
- **Štruktúrované učebné ciele**: Vylepšené učebné ciele s konkrétnymi, použiteľnými výsledkami  
- **Krosové odkazy**: Pridané odkazy medzi súvisiacimi témami bezpečnosti a základných konceptov  
- **Aktuálne informácie**: Aktualizované všetky dátumové odkazy a odkazy na špecifikácie na súčasné štandardy  
- **Pokyny na implementáciu**: Pridané konkrétne, použiteľné implementačné pokyny v obidvoch sekciách  

## 16. júl 2025

### README a navigačné vylepšenia  
- Kompletné prepracovanie navigácie kurikula v README.md  
- Nahradené `<details>` značky dostupnejším tabuľkovým formátom  
- Vytvorené alternatívne rozloženia v novom priečinku "alternative_layouts"  
- Pridané príklady navigácie s kartami, záložkami a harmonikou  
- Aktualizovaná časť štruktúry repozitára vrátane všetkých najnovších súborov  
- Vylepšená sekcia „Ako používať toto kurikulum“ s jasnými odporúčaniami  
- Aktualizované odkazy na MCP špecifikáciu smerujúce na správne URL  
- Pridaná sekcia Kontextového inžinierstva (5.14) do štruktúry kurikula  

### Aktualizácie študijného sprievodcu  
- Kompletné prepracovanie študijného sprievodcu podľa aktuálnej štruktúry repozitára  
- Pridané nové sekcie pre MCP klientov a nástroje, a populárne MCP servery  
- Aktualizovaná vizuálna mapa kurikula presne zobrazujúca všetky témy  
- Vylepšené opisy pokročilých tém pokrývajúce všetky špecializované oblasti  
- Aktualizovaná sekcia prípadových štúdií s reálnymi príkladmi  
- Pridaný tento komplexný changelog  

### Príspevky komunity (06-CommunityContributions/)  
- Pridané detailné informácie o MCP serveroch pre generovanie obrazov  
- Rozšírená sekcia o používaní Claude vo VSCode  
- Pridané nastavenie a použitie terminálového klienta Cline  
- Aktualizovaná sekcia MCP klientov so všetkými populárnymi klientskymi možnosťami  
- Vylepšené príklady príspevkov s presnejšími vzorkami kódu  

### Pokročilé témy (05-AdvancedTopics/)  
- Organizované všetky špecializované témy v súlade s jednotným pomenovaním  
- Pridané materiály a príklady Kontextového inžinierstva  
- Pridaná dokumentácia integrácie Foundry agenta  
- Vylepšená dokumentácia integrácie bezpečnosti Entra ID  

## 11. jún 2025

### Počiatočné vytvorenie  
- Uvoľnená prvá verzia kurikula MCP pre začiatočníkov  
- Vytvorená základná štruktúra všetkých 10 hlavných sekcií  
- Implementovaná vizuálna mapa kurikula na navigáciu  
- Pridané počiatočné ukážkové projekty v niekoľkých programovacích jazykoch  

### Začíname (03-GettingStarted/)  
- Vytvorené prvé príklady implementácie servera  
- Pridané návody na vývoj klienta  
- Zahrnuté pokyny na integráciu LLM klienta  
- Pridaná dokumentácia integrácie VS Code  
- Implementované príklady servera so Server-Sent Events (SSE)  

### Základné koncepty (01-CoreConcepts/)  
- Pridané detailné vysvetlenie klient-server architektúry  
- Vytvorená dokumentácia k hlavným komponentom protokolu  
- Zdokumentované komunikačné vzory v MCP  

## 23. máj 2025

### Štruktúra repozitára  
- Inicializovaný repozitár so základnou štruktúrou priečinkov  
- Vytvorené README súbory pre každú hlavnú sekciu  
- Nastavená infraštruktúra pre preklady  
- Pridané grafické zdroje a diagramy  

### Dokumentácia  
- Vytvorený počiatočný README.md so súhrnom kurikula  
- Pridané súbory CODE_OF_CONDUCT.md a SECURITY.md  
- Nastavený SUPPORT.md s pokynmi na získanie pomoci  
- Vytvorená predbežná štruktúra študijného sprievodcu  

## 15. apríl 2025

### Plánovanie a rámec  
- Počiatočné plánovanie kurikula MCP pre začiatočníkov  
- Definované učebné ciele a cieľová skupina  
- Načrtnutá štruktúra kurikula so 10 sekciami  
- Vyvinutý konceptuálny rámec pre príklady a prípadové štúdie  
- Vytvorené počiatočné prototypové príklady kľúčových konceptov

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->