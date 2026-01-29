# Změny: MCP pro začátečníky - osnovy

Tento dokument slouží jako záznam všech významných změn provedených v osnovách Model Context Protocol (MCP) pro začátečníky. Změny jsou zaznamenány v obráceném chronologickém pořadí (nejnovější změny první).

## 18. prosince 2025

### Aktualizace dokumentace zabezpečení - MCP specifikace 2025-11-25

#### MCP bezpečnostní osvědčené postupy (02-Security/mcp-best-practices.md) - aktualizace verze specifikace
- **Aktualizace verze protokolu**: Aktualizováno na odkaz na nejnovější MCP specifikaci 2025-11-25 (vydáno 25. listopadu 2025)
  - Aktualizovány všechny odkazy na verzi specifikace z 18. 6. 2025 na 25. 11. 2025
  - Aktualizovány datumové odkazy v dokumentu z 18. srpna 2025 na 18. prosince 2025
  - Ověřeno, že všechny URL specifikace směřují na aktuální dokumentaci
- **Validace obsahu**: Komplexní ověření bezpečnostních osvědčených postupů vůči nejnovějším standardům
  - **Microsoft Security Solutions**: Ověřena aktuální terminologie a odkazy pro Prompt Shields (dříve „detekce rizika jailbreaku“), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 zabezpečení**: Potvrzeno sladění s nejnovějšími bezpečnostními osvědčenými postupy OAuth
  - **OWASP standardy**: Validovány odkazy na OWASP Top 10 pro LLM, že jsou aktuální
  - **Azure služby**: Ověřeny všechny odkazy na dokumentaci Microsoft Azure a osvědčené postupy
- **Soulad se standardy**: Všechny odkazované bezpečnostní standardy potvrzeny jako aktuální
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 bezpečnostní osvědčené postupy
  - Azure bezpečnostní a shodné rámce
- **Implementační zdroje**: Ověřeny všechny odkazy na průvodce implementací a zdroje
  - Autentizační vzory Azure API Management
  - Průvodce integrací Microsoft Entra ID
  - Správa tajemství Azure Key Vault
  - DevSecOps pipeline a monitorovací řešení

### Zajištění kvality dokumentace
- **Soulad se specifikací**: Zajištěno, že všechny povinné bezpečnostní požadavky MCP (MUST/MUST NOT) odpovídají nejnovější specifikaci
- **Aktualizace zdrojů**: Ověřeny všechny externí odkazy na dokumentaci Microsoft, bezpečnostní standardy a průvodce implementací
- **Pokrytí osvědčených postupů**: Potvrzeno komplexní pokrytí autentizace, autorizace, AI-specifických hrozeb, zabezpečení dodavatelského řetězce a podnikových vzorů

## 6. října 2025

### Rozšíření sekce Začínáme – Pokročilé použití serveru a jednoduchá autentizace

#### Pokročilé použití serveru (03-GettingStarted/10-advanced)
- **Přidána nová kapitola**: Představen komplexní průvodce pokročilým použitím MCP serveru, pokrývající jak běžné, tak nízkoúrovňové serverové architektury.
  - **Běžný vs. nízkoúrovňový server**: Podrobná srovnání a ukázky kódu v Pythonu a TypeScriptu pro oba přístupy.
  - **Design založený na handlerech**: Vysvětlení správy nástrojů/zdrojů/promptů založené na handlerech pro škálovatelné a flexibilní implementace serveru.
  - **Praktické vzory**: Reálné scénáře, kde jsou nízkoúrovňové serverové vzory výhodné pro pokročilé funkce a architekturu.

#### Jednoduchá autentizace (03-GettingStarted/11-simple-auth)
- **Přidána nová kapitola**: Krok za krokem průvodce implementací jednoduché autentizace v MCP serverech.
  - **Koncepty autentizace**: Jasné vysvětlení rozdílu mezi autentizací a autorizací a práce s přihlašovacími údaji.
  - **Implementace základní autentizace**: Middleware vzory autentizace v Pythonu (Starlette) a TypeScriptu (Express) s ukázkami kódu.
  - **Postup k pokročilému zabezpečení**: Návod, jak začít s jednoduchou autentizací a postupovat k OAuth 2.1 a RBAC, s odkazy na pokročilé bezpečnostní moduly.

Tyto doplňky poskytují praktické, prakticky orientované návody pro vytváření robustnějších, bezpečnějších a flexibilnějších implementací MCP serverů, propojující základní koncepty s pokročilými produkčními vzory.

## 29. září 2025

### MCP Server Database Integration Labs – komplexní praktická výuka

#### 11-MCPServerHandsOnLabs – nová kompletní osnova integrace databáze
- **Kompletní 13-laboratorní výuková cesta**: Přidána komplexní praktická osnova pro tvorbu produkčně připravených MCP serverů s integrací databáze PostgreSQL
  - **Reálná implementace**: Případová studie Zava Retail analytics demonstrující podnikové vzory
  - **Strukturovaný postup učení**:
    - **Lab 00-03: Základy** – Úvod, základní architektura, zabezpečení a multi-tenancy, nastavení prostředí
    - **Lab 04-06: Tvorba MCP serveru** – Návrh databáze a schéma, implementace MCP serveru, vývoj nástrojů
    - **Lab 07-09: Pokročilé funkce** – Integrace sémantického vyhledávání, testování a ladění, integrace s VS Code
    - **Lab 10-12: Produkce a osvědčené postupy** – Strategie nasazení, monitoring a observabilita, osvědčené postupy a optimalizace
  - **Podnikové technologie**: Framework FastMCP, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Pokročilé funkce**: Row Level Security (RLS), sémantické vyhledávání, přístup k datům více nájemců, vektorové embeddingy, monitorování v reálném čase

#### Standardizace terminologie – převod modulů na laby
- **Komplexní aktualizace dokumentace**: Systematicky aktualizovány všechny README soubory v 11-MCPServerHandsOnLabs pro použití termínu „Lab“ místo „Modul“
  - **Nadpisy sekcí**: Aktualizováno „Co tento modul pokrývá“ na „Co tento lab pokrývá“ ve všech 13 labech
  - **Popis obsahu**: Změněno „Tento modul poskytuje...“ na „Tento lab poskytuje...“ v celé dokumentaci
  - **Cíle učení**: Aktualizováno „Na konci tohoto modulu...“ na „Na konci tohoto labu...“
  - **Navigační odkazy**: Převod všech odkazů „Modul XX:“ na „Lab XX:“ v křížových odkazech a navigaci
  - **Sledování dokončení**: Aktualizováno „Po dokončení tohoto modulu...“ na „Po dokončení tohoto labu...“
  - **Zachování technických odkazů**: Zachovány odkazy na Python moduly v konfiguračních souborech (např. `"module": "mcp_server.main"`)

#### Vylepšení studijního průvodce (study_guide.md)
- **Vizualizace osnovy**: Přidána nová sekce „11. Database Integration Labs“ s komplexní vizualizací struktury labů
- **Struktura repozitáře**: Aktualizováno z deseti na jedenáct hlavních sekcí s podrobným popisem 11-MCPServerHandsOnLabs
- **Navigační pokyny**: Vylepšeny instrukce pro pokrytí sekcí 00-11
- **Pokrytí technologií**: Přidány detaily integrace FastMCP, PostgreSQL a Azure služeb
- **Výsledky učení**: Zdůrazněn vývoj produkčně připravených serverů, vzory integrace databáze a podnikové zabezpečení

#### Vylepšení struktury hlavního README
- **Terminologie založená na labech**: Aktualizováno hlavní README.md v 11-MCPServerHandsOnLabs pro konzistentní použití struktury „Lab“
- **Organizace výukové cesty**: Jasný postup od základních konceptů přes pokročilou implementaci až po produkční nasazení
- **Zaměření na praxi**: Důraz na praktické, laboratorní učení s podnikově orientovanými vzory a technologiemi

### Zlepšení kvality a konzistence dokumentace
- **Důraz na praktické učení**: Posílen praktický, laboratorní přístup v celé dokumentaci
- **Zaměření na podnikové vzory**: Zvýrazněny produkčně připravené implementace a podnikové bezpečnostní aspekty
- **Integrace technologií**: Komplexní pokrytí moderních Azure služeb a AI integračních vzorů
- **Postup učení**: Jasná, strukturovaná cesta od základních konceptů k produkčnímu nasazení

## 26. září 2025

### Vylepšení případových studií – integrace GitHub MCP Registry

#### Případové studie (09-CaseStudy/) – zaměření na rozvoj ekosystému
- **README.md**: Významné rozšíření s komplexní případovou studií GitHub MCP Registry
  - **Případová studie GitHub MCP Registry**: Nová komplexní případová studie zkoumající spuštění GitHub MCP Registry v září 2025
    - **Analýza problému**: Podrobná analýza fragmentovaného objevování a nasazení MCP serverů
    - **Architektura řešení**: Centralizovaný přístup registru GitHub s instalací VS Code na jedno kliknutí
    - **Obchodní dopad**: Měřitelné zlepšení onboardingu vývojářů a produktivity
    - **Strategická hodnota**: Zaměření na modulární nasazení agentů a interoperabilitu nástrojů
    - **Rozvoj ekosystému**: Pozice jako základní platforma pro agentní integraci
  - **Vylepšená struktura případových studií**: Aktualizováno všech sedm případových studií s jednotným formátováním a komplexními popisy
    - Azure AI Travel Agents: důraz na orchestraci více agentů
    - Azure DevOps integrace: zaměření na automatizaci workflow
    - Real-time získávání dokumentace: implementace Python konzolového klienta
    - Interaktivní generátor studijního plánu: Chainlit konverzační webová aplikace
    - Dokumentace v editoru: integrace VS Code a GitHub Copilot
    - Azure API Management: podnikové integrační vzory API
    - GitHub MCP Registry: rozvoj ekosystému a komunitní platforma
  - **Komplexní závěr**: Přepsaná závěrečná sekce zdůrazňující sedm případových studií pokrývajících různé dimenze implementace MCP
    - Podniková integrace, orchestraci více agentů, produktivitu vývojářů
    - Rozvoj ekosystému, vzdělávací aplikace
    - Vylepšené poznatky o architektonických vzorech, implementačních strategiích a osvědčených postupech
    - Důraz na MCP jako zralý, produkčně připravený protokol

#### Aktualizace studijního průvodce (study_guide.md)
- **Vizualizace osnovy**: Aktualizována myšlenková mapa o zařazení GitHub MCP Registry do sekce případových studií
- **Popis případových studií**: Rozšířen z obecných popisů na detailní rozbor sedmi komplexních případových studií
- **Struktura repozitáře**: Aktualizována sekce 10 pro odraz komplexního pokrytí případových studií s konkrétními implementačními detaily
- **Integrace changelogu**: Přidán záznam ze 26. září 2025 dokumentující přidání GitHub MCP Registry a vylepšení případových studií
- **Aktualizace data**: Aktualizováno datum v patičce na nejnovější revizi (26. září 2025)

### Zlepšení kvality dokumentace
- **Zvýšení konzistence**: Standardizováno formátování a struktura případových studií ve všech sedmi příkladech
- **Komplexní pokrytí**: Případové studie nyní pokrývají scénáře podnikové integrace, produktivity vývojářů a rozvoje ekosystému
- **Strategické postavení**: Zvýrazněn důraz na MCP jako základní platformu pro nasazení agentních systémů
- **Integrace zdrojů**: Aktualizovány doplňkové zdroje o odkaz na GitHub MCP Registry

## 15. září 2025

### Rozšíření pokročilých témat – vlastní transporty a inženýrství kontextu

#### MCP vlastní transporty (05-AdvancedTopics/mcp-transport/) – nový pokročilý průvodce implementací
- **README.md**: Kompletní průvodce implementací vlastních MCP transportních mechanismů
  - **Azure Event Grid transport**: Komplexní serverless event-driven transportní implementace
    - Příklady v C#, TypeScriptu a Pythonu s integrací Azure Functions
    - Event-driven architektonické vzory pro škálovatelné MCP řešení
    - Příjemci webhooků a push-based zpracování zpráv
  - **Azure Event Hubs transport**: Implementace vysokopropustného streamovacího transportu
    - Schopnosti streamování v reálném čase pro scénáře s nízkou latencí
    - Strategie partitioningu a správa checkpointů
    - Seskupování zpráv a optimalizace výkonu
  - **Podnikové integrační vzory**: Produkčně připravené architektonické příklady
    - Distribuované MCP zpracování přes více Azure Functions
    - Hybridní transportní architektury kombinující různé typy transportů
    - Strategie trvanlivosti zpráv, spolehlivosti a zpracování chyb
  - **Zabezpečení a monitoring**: Integrace Azure Key Vault a vzory observability
    - Autentizace pomocí spravované identity a přístup s nejmenšími právy
    - Telemetrie Application Insights a monitorování výkonu
    - Circuit breakers a vzory odolnosti vůči chybám
  - **Testovací frameworky**: Komplexní testovací strategie pro vlastní transporty
    - Jednotkové testy s testovacími dubléry a mocking frameworky
    - Integrační testy s Azure Test Containers
    - Úvahy o testování výkonu a zátěže

#### Inženýrství kontextu (05-AdvancedTopics/mcp-contextengineering/) – vznikající disciplína AI
- **README.md**: Komplexní průzkum inženýrství kontextu jako vznikajícího oboru
  - **Základní principy**: Kompletní sdílení kontextu, povědomí o rozhodování akcí a správa kontextového okna
  - **Soulad s MCP protokolem**: Jak design MCP řeší výzvy inženýrství kontextu
    - Omezení kontextového okna a strategie postupného načítání
    - Určování relevance a dynamické získávání kontextu
    - Zpracování multimodálního kontextu a bezpečnostní aspekty
  - **Přístupy k implementaci**: Jednovláknové vs. víceagentní architektury
    - Techniky dělení a prioritizace kontextu
    - Postupné načítání a kompresní strategie kontextu
    - Vícevrstvé přístupy ke kontextu a optimalizace získávání
  - **Měřicí rámec**: Vznikající metriky pro hodnocení efektivity kontextu
    - Efektivita vstupu, výkon, kvalita a uživatelská zkušenost
    - Experimentální přístupy k optimalizaci kontextu
    - Analýza selhání a metodiky zlepšování

#### Aktualizace navigace osnovy (README.md)
- **Vylepšená struktura modulů**: Aktualizována tabulka osnovy o nové pokročilé témata
  - Přidány položky Context Engineering (5.14) a Custom Transport (5.15)
  - Konzistentní formátování a navigační odkazy ve všech modulech
  - Aktualizované popisy odrážející aktuální rozsah obsahu

### Vylepšení struktury adresářů
- **Standardizace pojmenování**: Přejmenováno „mcp transport“ na „mcp-transport“ pro konzistenci s ostatními složkami pokročilých témat
- **Organizace obsahu**: Všechny složky 05-AdvancedTopics nyní používají konzistentní pojmenování (mcp-[téma])

### Zlepšení kvality dokumentace
- **Soulad se specifikací MCP**: Veškerý nový obsah odkazuje na aktuální MCP specifikaci 2025-06-18
- **Příklady v několika jazycích**: Komplexní ukázky kódu v C#, TypeScriptu a Pythonu
- **Podnikové zaměření**: Produkčně připravené vzory a integrace s Azure cloudem
- **Vizualizace dokumentace**: Mermaid diagramy pro architekturu a vizualizaci toků

## 18. srpna 2025

### Komplexní aktualizace dokumentace – standardy MCP 2025-06-18

#### MCP bezpečnostní osvědčené postupy (02-Security/) – kompletní modernizace
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletní přepsání sladěné s MCP specifikací 2025-06-18
  - **Povinné požadavky**: Přidány explicitní požadavky MUSÍ/MUSÍ NE z oficiální specifikace s jasnými vizuálními indikátory
  - **12 základních bezpečnostních praktik**: Přestrukturováno z 15 položkového seznamu na komplexní bezpečnostní domény
    - Bezpečnost tokenů a autentizace s integrací externího poskytovatele identity
    - Správa relací a bezpečnost přenosu s kryptografickými požadavky
    - Ochrana proti hrozbám specifickým pro AI s integrací Microsoft Prompt Shields
    - Řízení přístupu a oprávnění s principem nejmenších oprávnění
    - Bezpečnost obsahu a monitorování s integrací Azure Content Safety
    - Bezpečnost dodavatelského řetězce s komplexní verifikací komponent
    - Bezpečnost OAuth a prevence útoku zmateného zástupce s implementací PKCE
    - Reakce na incidenty a zotavení s automatizovanými schopnostmi
    - Soulad a správa s regulatorními požadavky
    - Pokročilé bezpečnostní kontroly s architekturou zero trust
    - Integrace Microsoft bezpečnostního ekosystému s komplexními řešeními
    - Neustálý vývoj bezpečnosti s adaptivními praktikami
  - **Microsoft bezpečnostní řešení**: Vylepšené pokyny pro integraci Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security
  - **Implementační zdroje**: Kategorizované komplexní odkazy na zdroje podle Oficiální dokumentace MCP, Microsoft bezpečnostních řešení, bezpečnostních standardů a implementačních průvodců

#### Pokročilé bezpečnostní kontroly (02-Security/) - Podniková implementace
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletní přepracování s podnikových bezpečnostním rámcem
  - **9 komplexních bezpečnostních domén**: Rozšířeno z základních kontrol na detailní podnikový rámec
    - Pokročilá autentizace a autorizace s integrací Microsoft Entra ID
    - Bezpečnost tokenů a kontroly proti průchodu s komplexní validací
    - Kontroly bezpečnosti relací s prevencí únosu
    - AI-specifické bezpečnostní kontroly s prevencí injekce promptů a otravy nástrojů
    - Prevence útoku zmateného zástupce s bezpečností OAuth proxy
    - Bezpečnost spouštění nástrojů s sandboxingem a izolací
    - Kontroly bezpečnosti dodavatelského řetězce s ověřováním závislostí
    - Kontroly monitorování a detekce s integrací SIEM
    - Reakce na incidenty a zotavení s automatizovanými schopnostmi
  - **Implementační příklady**: Přidány detailní YAML konfigurační bloky a ukázky kódu
  - **Integrace Microsoft řešení**: Komplexní pokrytí Azure bezpečnostních služeb, GitHub Advanced Security a podnikového řízení identity

#### Pokročilá témata bezpečnosti (05-AdvancedTopics/mcp-security/) - Produkčně připravená implementace
- **README.md**: Kompletní přepis pro podnikovou bezpečnostní implementaci
  - **Soulad s aktuální specifikací**: Aktualizováno na MCP Specification 2025-06-18 s povinnými bezpečnostními požadavky
  - **Vylepšená autentizace**: Integrace Microsoft Entra ID s komplexními příklady v .NET a Java Spring Security
  - **Integrace AI bezpečnosti**: Implementace Microsoft Prompt Shields a Azure Content Safety s detailními příklady v Pythonu
  - **Pokročilá mitigace hrozeb**: Komplexní implementační příklady pro
    - Prevence útoku zmateného zástupce s PKCE a validací uživatelského souhlasu
    - Prevence průchodu tokenů s validací publika a bezpečnou správou tokenů
    - Prevence únosu relace s kryptografickým vázáním a behaviorální analýzou
  - **Podniková bezpečnostní integrace**: Monitorování Azure Application Insights, pipeline detekce hrozeb a bezpečnost dodavatelského řetězce
  - **Implementační kontrolní seznam**: Jasné rozlišení povinných a doporučených bezpečnostních kontrol s výhodami Microsoft bezpečnostního ekosystému

### Kvalita dokumentace a soulad se standardy
- **Odkazy na specifikace**: Aktualizovány všechny odkazy na aktuální MCP Specification 2025-06-18
- **Microsoft bezpečnostní ekosystém**: Vylepšené pokyny pro integraci v celé bezpečnostní dokumentaci
- **Praktická implementace**: Přidány detailní příklady kódu v .NET, Java a Python s podnikatelskými vzory
- **Organizace zdrojů**: Komplexní kategorizace oficiální dokumentace, bezpečnostních standardů a implementačních průvodců
- **Vizuální indikátory**: Jasné označení povinných požadavků vs. doporučených praktik


#### Základní koncepty (01-CoreConcepts/) - Kompletní modernizace
- **Aktualizace verze protokolu**: Aktualizováno na odkaz na aktuální MCP Specification 2025-06-18 s verzováním podle data (formát RRRR-MM-DD)
- **Vylepšení architektury**: Vylepšené popisy Hostitelů, Klientů a Serverů pro odraz aktuálních architektonických vzorů MCP
  - Hostitelé nyní jasně definováni jako AI aplikace koordinující více MCP klientských připojení
  - Klienti popsáni jako protokoloví konektory udržující vztahy jeden na jednoho se servery
  - Servery rozšířeny o scénáře lokálního vs. vzdáleného nasazení
- **Přepracování primitiv**: Kompletní přepracování serverových a klientských primitiv
  - Serverové primitivy: Zdroje (datové zdroje), Prompty (šablony), Nástroje (spustitelné funkce) s detailními vysvětleními a příklady
  - Klientské primitivy: Sampling (dokončení LLM), Elicitation (uživatelský vstup), Logging (ladění/monitorování)
  - Aktualizováno s aktuálními vzory metod discovery (`*/list`), retrieval (`*/get`) a execution (`*/call`)
- **Architektura protokolu**: Zaveden dvouvrstvý architektonický model
  - Datová vrstva: Základ JSON-RPC 2.0 s řízením životního cyklu a primitivy
  - Transportní vrstva: STDIO (lokální) a Streamable HTTP s SSE (vzdálený) transportními mechanismy
- **Bezpečnostní rámec**: Komplexní bezpečnostní principy včetně explicitního uživatelského souhlasu, ochrany soukromí dat, bezpečnosti spouštění nástrojů a bezpečnosti transportní vrstvy
- **Komunikační vzory**: Aktualizované protokolové zprávy ukazující inicializaci, discovery, exekuci a notifikační toky
- **Příklady kódu**: Obnovené vícejazyčné příklady (.NET, Java, Python, JavaScript) odrážející aktuální vzory MCP SDK

#### Bezpečnost (02-Security/) - Komplexní bezpečnostní přepracování  
- **Soulad se standardy**: Plný souladu s bezpečnostními požadavky MCP Specification 2025-06-18
- **Vývoj autentizace**: Dokumentován vývoj od vlastních OAuth serverů k delegaci externím poskytovatelům identity (Microsoft Entra ID)
- **Analýza hrozeb specifických pro AI**: Rozšířené pokrytí moderních AI útoků
  - Detailní scénáře útoků injekce promptů s reálnými příklady
  - Mechanismy otravy nástrojů a vzory útoků "rug pull"
  - Otrava kontextového okna a útoky na zmatení modelu
- **Microsoft AI bezpečnostní řešení**: Komplexní pokrytí Microsoft bezpečnostního ekosystému
  - AI Prompt Shields s pokročilou detekcí, zvýrazňováním a technikami oddělovačů
  - Vzory integrace Azure Content Safety
  - GitHub Advanced Security pro ochranu dodavatelského řetězce
- **Pokročilá mitigace hrozeb**: Detailní bezpečnostní kontroly pro
  - Únos relace s MCP-specifickými scénáři útoků a kryptografickými požadavky na ID relace
  - Problémy zmateného zástupce v MCP proxy scénářích s explicitními požadavky na souhlas
  - Zranitelnosti průchodu tokenů s povinnými validačními kontrolami
- **Bezpečnost dodavatelského řetězce**: Rozšířené pokrytí AI dodavatelského řetězce včetně základních modelů, embedding služeb, poskytovatelů kontextu a API třetích stran
- **Základní bezpečnost**: Vylepšená integrace s podnikatelskými bezpečnostními vzory včetně architektury zero trust a Microsoft bezpečnostního ekosystému
- **Organizace zdrojů**: Kategorizované komplexní odkazy na zdroje podle typu (Oficiální dokumentace, Standardy, Výzkum, Microsoft řešení, Implementační průvodce)

### Zlepšení kvality dokumentace
- **Strukturované učební cíle**: Vylepšené učební cíle s konkrétními, akčními výsledky
- **Křížové odkazy**: Přidány odkazy mezi souvisejícími tématy bezpečnosti a základních konceptů
- **Aktuální informace**: Aktualizovány všechny datumové odkazy a odkazy na specifikace na aktuální standardy
- **Pokyny k implementaci**: Přidány konkrétní, akční implementační pokyny v obou sekcích

## 16. července 2025

### README a vylepšení navigace
- Kompletně přepracovaná navigace kurikula v README.md
- Nahrazeny tagy `<details>` přístupnějším formátem založeným na tabulkách
- Vytvořeny alternativní rozložení v nové složce "alternative_layouts"
- Přidány příklady navigace založené na kartách, záložkách a akordeonu
- Aktualizována sekce struktury repozitáře o všechny nejnovější soubory
- Vylepšena sekce "Jak používat toto kurikulum" s jasnými doporučeními
- Aktualizovány odkazy na specifikaci MCP na správné URL
- Přidána sekce Context Engineering (5.14) do struktury kurikula

### Aktualizace studijního průvodce
- Kompletně přepracován studijní průvodce pro soulad s aktuální strukturou repozitáře
- Přidány nové sekce pro MCP klienty a nástroje a populární MCP servery
- Aktualizována vizuální mapa kurikula pro přesné zobrazení všech témat
- Vylepšeny popisy pokročilých témat pro pokrytí všech specializovaných oblastí
- Aktualizována sekce případových studií s reálnými příklady
- Přidán tento komplexní changelog

### Příspěvky komunity (06-CommunityContributions/)
- Přidány detailní informace o MCP serverech pro generování obrázků
- Přidána komplexní sekce o používání Claude ve VSCode
- Přidány instrukce pro nastavení a používání terminálového klienta Cline
- Aktualizována sekce MCP klientů o všechny populární klientské možnosti
- Vylepšeny příklady příspěvků s přesnějšími ukázkami kódu

### Pokročilá témata (05-AdvancedTopics/)
- Organizovány všechny specializované složky témat s konzistentním pojmenováním
- Přidány materiály a příklady pro context engineering
- Přidána dokumentace integrace agenta Foundry
- Vylepšena dokumentace integrace bezpečnosti Entra ID

## 11. června 2025

### První vytvoření
- Vydána první verze kurikula MCP pro začátečníky
- Vytvořena základní struktura všech 10 hlavních sekcí
- Implementována vizuální mapa kurikula pro navigaci
- Přidány počáteční ukázkové projekty v několika programovacích jazycích

### Začínáme (03-GettingStarted/)
- Vytvořeny první příklady implementace serveru
- Přidány pokyny pro vývoj klienta
- Zahrnuty instrukce pro integraci LLM klienta
- Přidána dokumentace integrace VS Code
- Implementovány příklady serveru s Server-Sent Events (SSE)

### Základní koncepty (01-CoreConcepts/)
- Přidáno detailní vysvětlení klient-server architektury
- Vytvořena dokumentace klíčových komponent protokolu
- Zdokumentovány vzory zpráv v MCP

## 23. května 2025

### Struktura repozitáře
- Inicializována struktura repozitáře se základními složkami
- Vytvořeny README soubory pro každou hlavní sekci
- Nastavena infrastruktura pro překlady
- Přidány obrazové zdroje a diagramy

### Dokumentace
- Vytvořen počáteční README.md s přehledem kurikula
- Přidány soubory CODE_OF_CONDUCT.md a SECURITY.md
- Nastaven SUPPORT.md s pokyny pro získání pomoci
- Vytvořena předběžná struktura studijního průvodce

## 15. dubna 2025

### Plánování a rámec
- Počáteční plánování kurikula MCP pro začátečníky
- Definovány učební cíle a cílové publikum
- Nastavena struktura kurikula o 10 sekcích
- Vyvinut konceptuální rámec pro příklady a případové studie
- Vytvořeny počáteční prototypové příklady klíčových konceptů

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->