# Zmeny: MCP pre začiatočníkov - učebný plán

Tento dokument slúži ako záznam všetkých významných zmien vykonaných v učebnom pláne Model Context Protocol (MCP) pre začiatočníkov. Zmeny sú zaznamenané v obrátenom chronologickom poradí (najnovšie zmeny ako prvé).

## 18. december 2025

### Aktualizácia bezpečnostnej dokumentácie - špecifikácia MCP 2025-11-25

#### Najlepšie bezpečnostné postupy MCP (02-Security/mcp-best-practices.md) - aktualizácia verzie špecifikácie
- **Aktualizácia verzie protokolu**: Aktualizované odkazy na najnovšiu špecifikáciu MCP 2025-11-25 (vydané 25. novembra 2025)
  - Aktualizované všetky odkazy na verziu špecifikácie z 18. júna 2025 na 25. novembra 2025
  - Aktualizované dátumy dokumentov z 18. augusta 2025 na 18. decembra 2025
  - Overené, že všetky URL špecifikácie smerujú na aktuálnu dokumentáciu
- **Validácia obsahu**: Komplexná validácia najlepších bezpečnostných postupov podľa najnovších štandardov
  - **Microsoft Security Solutions**: Overená aktuálna terminológia a odkazy pre Prompt Shields (predtým "detekcia rizika jailbreaku"), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 Security**: Potvrdená zhoda s najnovšími bezpečnostnými postupmi OAuth
  - **OWASP štandardy**: Overené, že odkazy na OWASP Top 10 pre LLM zostávajú aktuálne
  - **Azure služby**: Overené všetky odkazy na dokumentáciu Microsoft Azure a najlepšie postupy
- **Zladenie so štandardmi**: Všetky referencované bezpečnostné štandardy sú aktuálne
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Najlepšie bezpečnostné postupy OAuth 2.1
  - Azure bezpečnostné a súladové rámce
- **Implementačné zdroje**: Overené všetky odkazy na implementačné príručky a zdroje
  - Vzory autentifikácie Azure API Management
  - Príručky integrácie Microsoft Entra ID
  - Správa tajomstiev Azure Key Vault
  - DevSecOps pipeline a monitorovacie riešenia

### Kontrola kvality dokumentácie
- **Súlad so špecifikáciou**: Zabezpečené, že všetky povinné bezpečnostné požiadavky MCP (MUST/MUST NOT) sú v súlade s najnovšou špecifikáciou
- **Aktualizácia zdrojov**: Overené všetky externé odkazy na dokumentáciu Microsoft, bezpečnostné štandardy a implementačné príručky
- **Pokrytie najlepších postupov**: Potvrdené komplexné pokrytie autentifikácie, autorizácie, hrozieb špecifických pre AI, bezpečnosti dodávateľského reťazca a podnikových vzorov

## 6. október 2025

### Rozšírenie sekcie Začíname – Pokročilé použitie servera a jednoduchá autentifikácia

#### Pokročilé použitie servera (03-GettingStarted/10-advanced)
- **Pridaná nová kapitola**: Predstavený komplexný sprievodca pokročilým používaním MCP servera, pokrývajúci bežné aj nízkoúrovňové architektúry servera.
  - **Bežný vs. nízkoúrovňový server**: Podrobná komparácia a príklady kódu v Pythone a TypeScripte pre oba prístupy.
  - **Dizajn založený na handleroch**: Vysvetlenie správy nástrojov/zdrojov/promptov založené na handleroch pre škálovateľné a flexibilné implementácie servera.
  - **Praktické vzory**: Reálne scenáre, kde sú nízkoúrovňové vzory servera výhodné pre pokročilé funkcie a architektúru.

#### Jednoduchá autentifikácia (03-GettingStarted/11-simple-auth)
- **Pridaná nová kapitola**: Krok za krokom sprievodca implementáciou jednoduchej autentifikácie v MCP serveroch.
  - **Koncepty autentifikácie**: Jasné vysvetlenie rozdielu medzi autentifikáciou a autorizáciou a správy poverení.
  - **Implementácia základnej autentifikácie**: Middleware vzory autentifikácie v Pythone (Starlette) a TypeScripte (Express) s ukážkami kódu.
  - **Postup k pokročilej bezpečnosti**: Návod na začatie s jednoduchou autentifikáciou a postup k OAuth 2.1 a RBAC, s odkazmi na pokročilé bezpečnostné moduly.

Tieto doplnky poskytujú praktické, praktické návody na vytváranie robustnejších, bezpečnejších a flexibilnejších implementácií MCP serverov, ktoré prepájajú základné koncepty s pokročilými produkčnými vzormi.

## 29. september 2025

### MCP Server Database Integration Labs – komplexná praktická učebná cesta

#### 11-MCPServerHandsOnLabs – nový kompletný učebný plán integrácie databázy
- **Kompletná 13-laboratórna učebná cesta**: Pridaný komplexný praktický učebný plán na tvorbu produkčne pripravených MCP serverov s integráciou PostgreSQL databázy
  - **Reálna implementácia**: Prípad použitia Zava Retail analytics demonštrujúci podnikové vzory
  - **Štruktúrovaný postup učenia**:
    - **Lab 00-03: Základy** – Úvod, jadrová architektúra, bezpečnosť a multi-tenancy, nastavenie prostredia
    - **Lab 04-06: Tvorba MCP servera** – Návrh databázy a schéma, implementácia MCP servera, vývoj nástrojov
    - **Lab 07-09: Pokročilé funkcie** – Integrácia sémantického vyhľadávania, testovanie a ladenie, integrácia VS Code
    - **Lab 10-12: Produkcia a najlepšie postupy** – Stratégie nasadenia, monitorovanie a pozorovateľnosť, najlepšie postupy a optimalizácia
  - **Podnikové technológie**: FastMCP framework, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Pokročilé funkcie**: Row Level Security (RLS), sémantické vyhľadávanie, multi-tenant prístup k dátam, vektorové embeddingy, monitorovanie v reálnom čase

#### Štandardizácia terminológie – konverzia modulu na laboratórium
- **Komplexná aktualizácia dokumentácie**: Systematicky aktualizované všetky README súbory v 11-MCPServerHandsOnLabs na používanie termínu "Lab" namiesto "Module"
  - **Nadpisy sekcií**: Aktualizované "What This Module Covers" na "What This Lab Covers" vo všetkých 13 laboratóriách
  - **Popis obsahu**: Zmenené "This module provides..." na "This lab provides..." v celej dokumentácii
  - **Ciele učenia**: Aktualizované "By the end of this module..." na "By the end of this lab..."
  - **Navigačné odkazy**: Prekonvertované všetky odkazy "Module XX:" na "Lab XX:" v krížových odkazoch a navigácii
  - **Sledovanie dokončenia**: Aktualizované "After completing this module..." na "After completing this lab..."
  - **Zachované technické odkazy**: Zachované odkazy na Python moduly v konfiguračných súboroch (napr. `"module": "mcp_server.main"`)

#### Vylepšenie študijného sprievodcu (study_guide.md)
- **Vizualizácia učebného plánu**: Pridaná nová sekcia "11. Database Integration Labs" s komplexnou vizualizáciou štruktúry laboratórií
- **Štruktúra repozitára**: Aktualizované z desiatich na jedenásť hlavných sekcií s podrobným popisom 11-MCPServerHandsOnLabs
- **Navigačné pokyny**: Vylepšené inštrukcie na prechádzanie sekciami 00-11
- **Pokrytie technológií**: Pridané detaily o FastMCP, PostgreSQL a integrácii Azure služieb
- **Výsledky učenia**: Zdôraznený vývoj produkčne pripravených serverov, vzory integrácie databázy a podniková bezpečnosť

#### Vylepšenie štruktúry hlavného README
- **Terminológia založená na laboratóriách**: Aktualizovaný hlavný README.md v 11-MCPServerHandsOnLabs na konzistentné používanie štruktúry "Lab"
- **Organizácia učebnej cesty**: Jasný postup od základných konceptov cez pokročilú implementáciu až po produkčné nasadenie
- **Zameranie na reálny svet**: Dôraz na praktické, praktické učenie s podnikových vzormi a technológiami

### Zlepšenia kvality a konzistencie dokumentácie
- **Dôraz na praktické učenie**: Posilnený praktický, laboratórny prístup v celej dokumentácii
- **Zameranie na podnikové vzory**: Zvýraznené produkčne pripravené implementácie a podnikové bezpečnostné aspekty
- **Integrácia technológií**: Komplexné pokrytie moderných Azure služieb a vzorov integrácie AI
- **Postup učenia**: Jasná, štruktúrovaná cesta od základných konceptov po produkčné nasadenie

## 26. september 2025

### Vylepšenie prípadových štúdií – integrácia GitHub MCP Registry

#### Prípadové štúdie (09-CaseStudy/) – zameranie na rozvoj ekosystému
- **README.md**: Významné rozšírenie s komplexnou prípadovou štúdiou GitHub MCP Registry
  - **Prípadová štúdia GitHub MCP Registry**: Nová komplexná prípadová štúdia skúmajúca spustenie GitHub MCP Registry v septembri 2025
    - **Analýza problému**: Podrobná analýza fragmentovaného objavovania a nasadzovania MCP serverov
    - **Architektúra riešenia**: Centralizovaný prístup registru GitHub s inštaláciou VS Code na jedno kliknutie
    - **Obchodný dopad**: Merateľné zlepšenia v onboardingu vývojárov a produktivite
    - **Strategická hodnota**: Zameranie na modulárne nasadenie agentov a interoperabilitu medzi nástrojmi
    - **Rozvoj ekosystému**: Pozicionovanie ako základná platforma pre agentickú integráciu
  - **Vylepšená štruktúra prípadových štúdií**: Aktualizované všetky sedem prípadových štúdií s konzistentným formátovaním a komplexnými popismi
    - Azure AI Travel Agents: dôraz na multi-agentnú orchestráciu
    - Azure DevOps Integration: zameranie na automatizáciu workflow
    - Real-Time Documentation Retrieval: implementácia Python konzolového klienta
    - Interactive Study Plan Generator: Chainlit konverzačná webová aplikácia
    - In-Editor Documentation: integrácia VS Code a GitHub Copilot
    - Azure API Management: podnikové vzory integrácie API
    - GitHub MCP Registry: rozvoj ekosystému a komunitná platforma
  - **Komplexný záver**: Prepracovaná záverečná sekcia zdôrazňujúca sedem prípadových štúdií pokrývajúcich viacero dimenzií implementácie MCP
    - Podniková integrácia, multi-agentná orchestrácia, produktivita vývojárov
    - Rozvoj ekosystému, kategorizácia vzdelávacích aplikácií
    - Vylepšené poznatky o architektonických vzoroch, implementačných stratégiách a najlepších postupoch
    - Dôraz na MCP ako zrelý, produkčne pripravený protokol

#### Aktualizácie študijného sprievodcu (study_guide.md)
- **Vizualizácia učebného plánu**: Aktualizovaná myšlienková mapa s pridaním GitHub MCP Registry v sekcii Prípadové štúdie
- **Popis prípadových štúdií**: Vylepšený z generických popisov na podrobný rozpis siedmich komplexných prípadových štúdií
- **Štruktúra repozitára**: Aktualizovaná sekcia 10 na odraz komplexného pokrytia prípadových štúdií so špecifickými implementačnými detailmi
- **Integrácia changelogu**: Pridaný záznam z 26. septembra 2025 dokumentujúci pridanie GitHub MCP Registry a vylepšenia prípadových štúdií
- **Aktualizácia dátumu**: Aktualizovaný časový údaj v pätičke na najnovšiu revíziu (26. september 2025)

### Zlepšenia kvality dokumentácie
- **Zvýšenie konzistencie**: Štandardizované formátovanie a štruktúra prípadových štúdií vo všetkých siedmich príkladoch
- **Komplexné pokrytie**: Prípadové štúdie teraz pokrývajú podnikové, produktivitu vývojárov a scenáre rozvoja ekosystému
- **Strategické pozicionovanie**: Zvýraznený dôraz na MCP ako základnú platformu pre nasadenie agentických systémov
- **Integrácia zdrojov**: Aktualizované doplnkové zdroje o odkaz na GitHub MCP Registry

## 15. september 2025

### Rozšírenie pokročilých tém – vlastné transporty a inžinierstvo kontextu

#### Vlastné transporty MCP (05-AdvancedTopics/mcp-transport/) – nový sprievodca pokročilou implementáciou
- **README.md**: Kompletný sprievodca implementáciou vlastných transportných mechanizmov MCP
  - **Azure Event Grid Transport**: Komplexná implementácia serverless event-driven transportu
    - Príklady v C#, TypeScript a Pythone s integráciou Azure Functions
    - Vzory event-driven architektúry pre škálovateľné MCP riešenia
    - Príjemcovia webhookov a push-based spracovanie správ
  - **Azure Event Hubs Transport**: Implementácia vysoko priepustného streaming transportu
    - Schopnosti streamovania v reálnom čase pre nízku latenciu
    - Stratégiá partitioningu a správa checkpointov
    - Batching správ a optimalizácia výkonu
  - **Podnikové integračné vzory**: Produkčne pripravené architektonické príklady
    - Distribuované spracovanie MCP cez viaceré Azure Functions
    - Hybridné transportné architektúry kombinujúce viacero typov transportu
    - Trvácnosť správ, spoľahlivosť a stratégie spracovania chýb
  - **Bezpečnosť a monitorovanie**: Integrácia Azure Key Vault a vzory pozorovateľnosti
    - Autentifikácia spravovanou identitou a prístup s najmenšími právami
    - Telemetria Application Insights a monitorovanie výkonu
    - Circuit breakers a vzory odolnosti voči chybám
  - **Testovacie rámce**: Komplexné testovacie stratégie pre vlastné transporty
    - Jednotkové testovanie s testovacími dablami a mocking frameworkmi
    - Integračné testovanie s Azure Test Containers
    - Úvahy o výkonnostnom a záťažovom testovaní

#### Inžinierstvo kontextu (05-AdvancedTopics/mcp-contextengineering/) – vznikajúca disciplína AI
- **README.md**: Komplexné preskúmanie inžinierstva kontextu ako vznikajúceho odboru
  - **Základné princípy**: Kompletné zdieľanie kontextu, uvedomenie rozhodovania o akciách a správa kontextového okna
  - **Zladenie s protokolom MCP**: Ako dizajn MCP rieši výzvy inžinierstva kontextu
    - Obmedzenia kontextového okna a stratégie progresívneho načítania
    - Určovanie relevantnosti a dynamické získavanie kontextu
    - Spracovanie multimodálneho kontextu a bezpečnostné aspekty
  - **Prístupy k implementácii**: Jednovláknové vs. multi-agentné architektúry
    - Techniky rozdeľovania a prioritizácie kontextových blokov
    - Progresívne načítanie a kompresné stratégie kontextu
    - Viacvrstvové prístupy ku kontextu a optimalizácia získavania
  - **Merací rámec**: Vznikajúce metriky na hodnotenie efektívnosti kontextu
    - Efektivita vstupu, výkon, kvalita a používateľská skúsenosť
    - Experimentálne prístupy k optimalizácii kontextu
    - Analýza zlyhaní a metodiky zlepšovania

#### Aktualizácie navigácie učebného plánu (README.md)
- **Vylepšená štruktúra modulu**: Aktualizovaná tabuľka učebného plánu o nové pokročilé témy
  - Pridané položky Context Engineering (5.14) a Custom Transport (5.15)
  - Konzistentné formátovanie a navigačné odkazy vo všetkých moduloch
  - Aktualizované popisy odrážajúce aktuálny rozsah obsahu

### Vylepšenia štruktúry adresárov
- **Štandardizácia názvov**: Premenovaný "mcp transport" na "mcp-transport" pre konzistenciu s ostatnými priečinkami pokročilých tém
- **Organizácia obsahu**: Všetky priečinky 05-AdvancedTopics teraz používajú konzistentný názvový vzor (mcp-[téma])

### Vylepšenia kvality dokumentácie
- **Zladenie so špecifikáciou MCP**: Všetok nový obsah odkazuje na aktuálnu špecifikáciu MCP 2025-06-18
- **Príklady v rôznych jazykoch**: Komplexné príklady kódu v C#, TypeScript a Pythone
- **Zameranie na podnikanie**: Produkčne pripravené vzory a integrácia Azure cloudu v celom obsahu
- **Vizualizácia dokumentácie**: Mermaid diagramy pre architektúru a vizualizáciu tokov

## 18. august 2025

### Komplexná aktualizácia dokumentácie – štandardy MCP 2025-06-18

#### Najlepšie bezpečnostné postupy MCP (02-Security/) – kompletná modernizácia
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletné prepracovanie zosúladené so špecifikáciou MCP 2025-06-18
  - **Povinné požiadavky**: Pridané explicitné požiadavky MUSÍ/MUSÍ NESMIE podľa oficiálnej špecifikácie s jasnými vizuálnymi indikátormi
  - **12 základných bezpečnostných praktík**: Preštruktúrované z 15-položkového zoznamu na komplexné bezpečnostné domény
    - Bezpečnosť tokenov a autentifikácia s integráciou externého poskytovateľa identity
    - Správa relácií a bezpečnosť prenosu s kryptografickými požiadavkami
    - Ochrana proti hrozbám špecifickým pre AI s integráciou Microsoft Prompt Shields
    - Riadenie prístupu a oprávnení s princípom najmenších privilégií
    - Bezpečnosť obsahu a monitorovanie s integráciou Azure Content Safety
    - Bezpečnosť dodávateľského reťazca s komplexnou verifikáciou komponentov
    - Bezpečnosť OAuth a prevencia útokov typu confused deputy s implementáciou PKCE
    - Reakcia na incidenty a obnova s automatizovanými schopnosťami
    - Súlad a správa s regulatórnym zosúladením
    - Pokročilé bezpečnostné kontroly s architektúrou zero trust
    - Integrácia Microsoft bezpečnostného ekosystému s komplexnými riešeniami
    - Neustály vývoj bezpečnosti s adaptívnymi praktikami
  - **Microsoft bezpečnostné riešenia**: Vylepšené pokyny pre integráciu Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security
  - **Implementačné zdroje**: Kategorizované komplexné odkazy na zdroje podľa Oficiálnej MCP dokumentácie, Microsoft bezpečnostných riešení, bezpečnostných štandardov a implementačných príručiek

#### Pokročilé bezpečnostné kontroly (02-Security/) - Podniková implementácia
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletná revízia s podnikovo orientovaným bezpečnostným rámcom
  - **9 komplexných bezpečnostných domén**: Rozšírené z základných kontrol na detailný podnikový rámec
    - Pokročilá autentifikácia a autorizácia s integráciou Microsoft Entra ID
    - Bezpečnosť tokenov a kontroly proti passthrough s komplexnou validáciou
    - Kontroly bezpečnosti relácií s prevenciou únosu
    - AI-špecifické bezpečnostné kontroly s prevenciou prompt injection a otravy nástrojov
    - Prevencia útokov typu confused deputy s OAuth proxy bezpečnosťou
    - Bezpečnosť vykonávania nástrojov s sandboxingom a izoláciou
    - Kontroly bezpečnosti dodávateľského reťazca s overovaním závislostí
    - Kontroly monitorovania a detekcie s integráciou SIEM
    - Reakcia na incidenty a obnova s automatizovanými schopnosťami
  - **Implementačné príklady**: Pridané detailné YAML konfiguračné bloky a príklady kódu
  - **Integrácia Microsoft riešení**: Komplexné pokrytie Azure bezpečnostných služieb, GitHub Advanced Security a podnikového manažmentu identity

#### Pokročilé bezpečnostné témy (05-AdvancedTopics/mcp-security/) - Produkčne pripravená implementácia
- **README.md**: Kompletné prepísanie pre podnikovú bezpečnostnú implementáciu
  - **Zosúladenie s aktuálnou špecifikáciou**: Aktualizované na MCP špecifikáciu 2025-06-18 s povinnými bezpečnostnými požiadavkami
  - **Vylepšená autentifikácia**: Integrácia Microsoft Entra ID s komplexnými príkladmi v .NET a Java Spring Security
  - **Integrácia AI bezpečnosti**: Implementácia Microsoft Prompt Shields a Azure Content Safety s detailnými príkladmi v Pythone
  - **Pokročilá mitigácia hrozieb**: Komplexné implementačné príklady pre
    - Prevenciu útokov typu confused deputy s PKCE a validáciou súhlasu používateľa
    - Prevenciu token passthrough s validáciou publika a bezpečným manažmentom tokenov
    - Prevenciu únosu relácie s kryptografickým viazaním a behaviorálnou analýzou
  - **Podniková bezpečnostná integrácia**: Monitorovanie Azure Application Insights, pipeline detekcie hrozieb a bezpečnosť dodávateľského reťazca
  - **Implementačný kontrolný zoznam**: Jasné rozlíšenie povinných a odporúčaných bezpečnostných kontrol s výhodami Microsoft bezpečnostného ekosystému

### Kvalita dokumentácie a zosúladenie so štandardmi
- **Odkazy na špecifikácie**: Aktualizované všetky odkazy na aktuálnu MCP špecifikáciu 2025-06-18
- **Microsoft bezpečnostný ekosystém**: Vylepšené pokyny pre integráciu v celej bezpečnostnej dokumentácii
- **Praktická implementácia**: Pridané detailné príklady kódu v .NET, Java a Pythone s podnikateľskými vzormi
- **Organizácia zdrojov**: Komplexná kategorizácia oficiálnej dokumentácie, bezpečnostných štandardov a implementačných príručiek
- **Vizuálne indikátory**: Jasné označenie povinných požiadaviek vs. odporúčaných praktík


#### Základné koncepty (01-CoreConcepts/) - Kompletná modernizácia
- **Aktualizácia verzie protokolu**: Aktualizované na odkazovanie na aktuálnu MCP špecifikáciu 2025-06-18 s dátumovým formátom (RRRR-MM-DD)
- **Vylepšenie architektúry**: Rozšírené popisy Hostiteľov, Klientov a Serverov pre odraz aktuálnych MCP architektonických vzorov
  - Hostitelia teraz jasne definovaní ako AI aplikácie koordinujúce viacero MCP klientskych pripojení
  - Klienti popísaní ako protokoloví konektory udržiavajúce vzťahy jeden na jedného so servermi
  - Servery rozšírené o lokálne vs. vzdialené nasadenie
- **Preštruktúrovanie primitív**: Kompletná revízia serverových a klientskych primitív
  - Serverové primitíva: Zdroje (dátové zdroje), Prompty (šablóny), Nástroje (vykonávateľné funkcie) s detailnými vysvetleniami a príkladmi
  - Klientské primitíva: Sampling (LLM dokončenia), Elicitation (vstup používateľa), Logging (ladenie/monitorovanie)
  - Aktualizované s aktuálnymi vzormi metód discovery (`*/list`), retrieval (`*/get`) a execution (`*/call`)
- **Architektúra protokolu**: Zavedený dvojvrstvový architektonický model
  - Dátová vrstva: Základ JSON-RPC 2.0 s manažmentom životného cyklu a primitívami
  - Prenosová vrstva: STDIO (lokálna) a Streamable HTTP s SSE (vzdialený) prenosové mechanizmy
- **Bezpečnostný rámec**: Komplexné bezpečnostné princípy vrátane explicitného súhlasu používateľa, ochrany súkromia dát, bezpečnosti vykonávania nástrojov a bezpečnosti prenosovej vrstvy
- **Komunikačné vzory**: Aktualizované protokolové správy zobrazujúce inicializáciu, discovery, vykonávanie a notifikačné toky
- **Príklady kódu**: Obnovené viacjazyčné príklady (.NET, Java, Python, JavaScript) odrážajúce aktuálne MCP SDK vzory

#### Bezpečnosť (02-Security/) - Komplexná bezpečnostná revízia  
- **Zosúladenie so štandardmi**: Plné zosúladenie s bezpečnostnými požiadavkami MCP špecifikácie 2025-06-18
- **Vývoj autentifikácie**: Zdokumentovaný vývoj od vlastných OAuth serverov k delegácii externého poskytovateľa identity (Microsoft Entra ID)
- **Analýza AI-špecifických hrozieb**: Rozšírené pokrytie moderných AI útokových vektorov
  - Detailné scenáre útokov prompt injection s reálnymi príkladmi
  - Mechanizmy otravy nástrojov a vzory útokov "rug pull"
  - Otrava kontextového okna a útoky na zmätok modelu
- **Microsoft AI bezpečnostné riešenia**: Komplexné pokrytie Microsoft bezpečnostného ekosystému
  - AI Prompt Shields s pokročilou detekciou, zvýrazňovaním a technikami delimiterov
  - Vzory integrácie Azure Content Safety
  - GitHub Advanced Security pre ochranu dodávateľského reťazca
- **Pokročilá mitigácia hrozieb**: Detailné bezpečnostné kontroly pre
  - Únos relácie s MCP-špecifickými scenármi útokov a kryptografickými požiadavkami na session ID
  - Problémy confused deputy v MCP proxy scenároch s explicitnými požiadavkami na súhlas
  - Zraniteľnosti token passthrough s povinnými validačnými kontrolami
- **Bezpečnosť dodávateľského reťazca**: Rozšírené pokrytie AI dodávateľského reťazca vrátane základných modelov, embedding služieb, poskytovateľov kontextu a API tretích strán
- **Základná bezpečnosť**: Vylepšená integrácia s podnikateľskými bezpečnostnými vzormi vrátane architektúry zero trust a Microsoft bezpečnostného ekosystému
- **Organizácia zdrojov**: Kategorizované komplexné odkazy na zdroje podľa typu (Oficiálna dokumentácia, Štandardy, Výskum, Microsoft riešenia, Implementačné príručky)

### Zlepšenia kvality dokumentácie
- **Štruktúrované vzdelávacie ciele**: Vylepšené vzdelávacie ciele so špecifickými, akčnými výsledkami
- **Krížové odkazy**: Pridané odkazy medzi súvisiacimi bezpečnostnými a základnými konceptmi
- **Aktuálne informácie**: Aktualizované všetky dátumové odkazy a odkazy na špecifikácie podľa aktuálnych štandardov
- **Pokyny na implementáciu**: Pridané špecifické, akčné implementačné pokyny v oboch sekciách

## 16. júla 2025

### Vylepšenia README a navigácie
- Kompletné prepracovanie navigácie kurikula v README.md
- Nahradenie tagov `<details>` prístupnejším formátom založeným na tabuľkách
- Vytvorenie alternatívnych rozložení v novej zložke "alternative_layouts"
- Pridané príklady navigácie založenej na kartách, záložkách a akordeóne
- Aktualizovaná sekcia štruktúry repozitára s najnovšími súbormi
- Vylepšená sekcia "Ako používať toto kurikulum" s jasnými odporúčaniami
- Aktualizované odkazy na MCP špecifikácie smerujúce na správne URL
- Pridaná sekcia Context Engineering (5.14) do štruktúry kurikula

### Aktualizácie študijného sprievodcu
- Kompletné prepracovanie študijného sprievodcu pre zosúladenie s aktuálnou štruktúrou repozitára
- Pridané nové sekcie pre MCP klientov a nástroje, a populárne MCP servery
- Aktualizovaná vizuálna mapa kurikula presne zobrazujúca všetky témy
- Vylepšené popisy pokročilých tém pokrývajúcich všetky špecializované oblasti
- Aktualizovaná sekcia prípadových štúdií s reálnymi príkladmi
- Pridaný tento komplexný changelog

### Príspevky komunity (06-CommunityContributions/)
- Pridané detailné informácie o MCP serveroch pre generovanie obrázkov
- Pridaná komplexná sekcia o používaní Claude vo VSCode
- Pridané inštrukcie na nastavenie a používanie terminálového klienta Cline
- Aktualizovaná sekcia MCP klientov s kompletným zoznamom populárnych klientov
- Vylepšené príklady príspevkov s presnejšími ukážkami kódu

### Pokročilé témy (05-AdvancedTopics/)
- Organizované všetky špecializované témy so konzistentným pomenovaním
- Pridané materiály a príklady pre context engineering
- Pridaná dokumentácia integrácie agenta Foundry
- Vylepšená dokumentácia integrácie bezpečnosti Entra ID

## 11. júna 2025

### Počiatočné vytvorenie
- Vydaná prvá verzia kurikula MCP pre začiatočníkov
- Vytvorená základná štruktúra pre všetkých 10 hlavných sekcií
- Implementovaná vizuálna mapa kurikula pre navigáciu
- Pridané počiatočné ukážkové projekty v rôznych programovacích jazykoch

### Začíname (03-GettingStarted/)
- Vytvorené prvé príklady implementácie servera
- Pridané pokyny pre vývoj klienta
- Zahrnuté inštrukcie pre integráciu LLM klienta
- Pridaná dokumentácia integrácie VS Code
- Implementované príklady serverov s Server-Sent Events (SSE)

### Základné koncepty (01-CoreConcepts/)
- Pridané detailné vysvetlenie klient-server architektúry
- Vytvorená dokumentácia k hlavným komponentom protokolu
- Zdokumentované vzory správ v MCP

## 23. mája 2025

### Štruktúra repozitára
- Inicializovaný repozitár so základnou štruktúrou priečinkov
- Vytvorené README súbory pre každú hlavnú sekciu
- Nastavená infraštruktúra pre preklady
- Pridané obrazové zdroje a diagramy

### Dokumentácia
- Vytvorený počiatočný README.md s prehľadom kurikula
- Pridané súbory CODE_OF_CONDUCT.md a SECURITY.md
- Nastavený SUPPORT.md s pokynmi na získanie pomoci
- Vytvorená predbežná štruktúra študijného sprievodcu

## 15. apríla 2025

### Plánovanie a rámec
- Počiatočné plánovanie kurikula MCP pre začiatočníkov
- Definované vzdelávacie ciele a cieľové publikum
- Načrtnutá 10-článková štruktúra kurikula
- Vyvinutý konceptuálny rámec pre príklady a prípadové štúdie
- Vytvorené počiatočné prototypové príklady kľúčových konceptov

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->