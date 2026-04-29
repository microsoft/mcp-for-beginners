# Záznam změn: MCP pro začátečníky – kurz

Tento dokument slouží jako záznam všech významných změn provedených v kurzu Model Context Protocol (MCP) pro začátečníky. Změny jsou zaznamenány v obráceném chronologickém pořadí (nejnovější změny nahoře).

## 11. dubna 2026

### Nové lekce, opravy dokumentace a aktualizace závislostí

#### Přidáno nové obsah kurikula

**Modul 05 - Pokročilá témata**
- **Lekce 5.17: Adversariální multi-agentní uvažování s MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nový komplexní průvodce pokrývající vzor adversariální debaty pro multi-agentní systémy
  - Mermaid architektonický diagram: dva agenti → sdílený MCP server → přepis debaty → rozhodčí → verdikt
  - Sdílený MCP server nástrojů (`web_search` + `run_python`) implementovaný v Pythonu a TypeScriptu
  - Protikladné systémové výzvy (PRO / PROTI / Rozhodčí) s explicitními požadavky na použití nástrojů
  - Orchestrátor debaty v Pythonu, TypeScriptu a C# řídící kola a směrování argumentů
  - Zapojení MCP `ClientSession` pro orchestrátora k reálným voláním nástrojů
  - Tabulka případů použití (detekce halucinací, modelování hrozeb, revize návrhu API, faktická verifikace, výběr technologie)
  - Bezpečnostní úvahy: sandboxované provádění, ověření volání nástrojů, omezení rychlosti, auditní záznamy
  - Strukturované cvičení se třemi praktickými scénáři (kontrola kódu, rozhodnutí o architektuře, moderování obsahu)

#### Opravy dokumentace

**Modul 03 - Začínáme**
- **05-stdio-server/README.md**: Opraven neúplný příklad TypeScript stdio serveru — přidána chybějící instance transportu (`new StdioServerTransport()`) a volání `server.connect(transport)`, aby odpovídalo příkladům v Pythonu a .NET ve stejné části
- **14-sampling/README.md**: Oprava překlepu — opraveno `"Sampling is an davanced features"` na `"Sampling is an advanced feature"`

#### Aktualizace kurikula

**Hlavní README.md**
- Přidán záznam 5.17 (Adversariální multi-agentní uvažování s MCP) do tabulky kurikula s přímým odkazem na novou lekci

**05-AdvancedTopics/README.md**
- Přidán řádek Lekce 5.17 do tabulky lekcí

**study_guide.md**
- Přidán tematický uzel Adversariální multi-agentní uvažování do myšlenkové mapy a textového popisu Pokročilých témat

#### Opravy kódu a zabezpečení

**Modul 05 - Adversariální agenti (`mcp-adversarial-agents`)**
- **Bezpečnostní oprava — příkazová injekce**: Nahrazeno shellové interpolování `execSync` funkcí `execFile` + `promisify` v TypeScript nástroji `run_python`, čímž byla eliminována možnost příkazové injekce (kód řízený LLM je nyní předáván jako doslovný argument argv bez zásahu shellu)
- **Zapojení smyčky MCP nástrojů**: Aktualizován orchestrátor debaty v Pythonu k použití asynchronního klienta `AsyncAnthropic` (nahrazující blokující synchronní `Anthropic`), předávání živé `ClientSession` přímo na každý tah agenta, načítání definic nástrojů přes `session.list_tools()` každé kolo a vysílání bloků `tool_use` přes `session.call_tool()` v cyklu, dokud model nevygeneruje finální textovou odpověď

#### Aktualizace závislostí

- Aktualizováno `hono` na verzi 4.12.12 napříč několika balíčky (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aktualizováno `@hono/node-server` z 1.19.11 na 1.19.13 v TypeScript balíčcích
- Aktualizováno `cryptography` z 46.0.5 na 46.0.7 v Python balíčcích (10-StreamliningAIWorkflows laboratoře 3 a 4)
- Aktualizováno `lodash` z 4.17.23 na 4.18.1 v inspektoru 10-StreamliningAIWorkflows

#### Překlady

- Synchronizovány překlady více než 48 jazyků s nejnovějšími změnami zdroje (aktualizace i18n)

---

## 5. února 2026

### Validace a vylepšení navigace napříč repozitářem

#### Přidáno nové obsah kurikula

**Modul 03 - Začínáme**
- **12-mcp-hosts/README.md**: Nový komplexní průvodce nastavením MCP hostů
  - Konfigurační příklady pro Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON konfigurační šablony pro všechny hlavní hosty
  - Tabulka porovnání typů transportu (stdio, SSE/HTTP, WebSocket)
  - Řešení běžných problémů s připojením
  - Zásady bezpečného nastavení hosta

- **13-mcp-inspector/README.md**: Nový průvodce laděním MCP Inspectoru
  - Způsoby instalace (npx, npm globálně, ze zdroje)
  - Připojení ke serverům přes stdio a HTTP/SSE
  - Testovací nástroje, zdroje a workflow s výzvami
  - Integrace s VS Code pro MCP Inspector
  - Časté scénáře ladění a řešení

**Modul 04 - Praktická implementace**
- **pagination/README.md**: Nový průvodce implementací stránkování
  - Vzory stránkování pomocí kurzoru v Pythonu, TypeScriptu, Javě
  - Řízení stránkování na straně klienta
  - Návrhové strategie kurzoru (neprůhledný vs. strukturovaný)
  - Doporučení pro optimalizaci výkonu

**Modul 05 - Pokročilá témata**
- **mcp-protocol-features/README.md**: Nový detailní přehled funkcí protokolu
  - Implementace oznámení o průběhu
  - Vzory rušení požadavků
  - Šablony zdrojů s URI vzory
  - Správa životního cyklu serveru
  - Řízení úrovně logování
  - Vzory zpracování chyb s JSON-RPC kódy

#### Opravy navigace (aktualizováno 24+ souborů)

**Hlavní moduly README**
 Nyní odkazují jak na první lekci TAK na další modul

**02-Security podřízené soubory**
- Všech 5 doplňkových bezpečnostních dokumentů má nyní sekci „Co dál“

**09-CaseStudy soubory**
- Všechny případové studie nyní mají sekvenční navigaci

**10-StreamliningAI laboratoře**
Přidána sekce „Co dál“ k přehledu modulu 10 a modulu 11

#### Opravy kódu a obsahu

**Aktualizace SDK a závislostí**
Opravená prázdná verze openai na `^4.95.0`
SDK aktualizováno z `^1.8.0` na `>=1.26.0`
Změněné verze mcp na `>=1.26.0`

**Opravy kódu**
Opraven neplatný model `gpt-4o-mini` na `gpt-4.1-mini`

**Opravy obsahu**
Oprava rozbitého odkazu `READMEmd` → `README.md`, oprava hlavičky kurikula `Modul 1-3` → `Modul 0-3`, oprava závislosti na velikosti písmen v cestě
Odstraněno poškozené duplikované znění případové studie 5

**Vylepšení pro začátečníky**
Přidán řádný úvod, výukové cíle a předpoklady pro začátečníky

#### Aktualizace kurikula

**Hlavní README.md**
- Přidány záznamy 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Stránkování), 5.16 (Funkce protokolu) do tabulky kurikula

**Modulové README**
Přidány lekce 12 a 13 do seznamu lekcí
Přidána sekce Praktické průvodce s odkazem na stránkování
Přidány lekce 5.15 (Vlastní transport) a 5.16 (Funkce protokolu)

**study_guide.md**
- Aktualizována myšlenková mapa se všemi novými tématy: Nastavení MCP Hosts, MCP Inspector, Stránkovací strategie, Hloubková analýza funkcí protokolu

## 28. ledna 2026

### Přezkum souladu s MCP specifikací 2025-11-25

#### Vylepšení základních konceptů (01-CoreConcepts/)
- **Nový primitiv klienta - Kořeny**: Přidána rozsáhlá dokumentace o primitivu klienta Roots, umožňující servery chápat hranice souborového systému a oprávnění k přístupu
- **Anotace nástrojů**: Přidána dokumentace anotací chování nástrojů (`readOnlyHint`, `destructiveHint`) pro lepší rozhodování o provedení nástroje
- **Volání nástrojů při Sampling**: Aktualizována dokumentace Sampling o parametry `tools` a `toolChoice` pro modelové řízené volání nástrojů během žádostí o sampling
- **URL mod vyvolávání**: Přidána dokumentace vyvolávání založeného na URL pro externí webové interakce iniciované serverem
- **Úkoly (experimentální)**: Přidána nová sekce popisující experimentální funkci Úkolů pro trvalé spouštění a odložené získání výsledku
- **Podpora ikon**: Poznámka, že nástroje, zdroje, šablony zdrojů a výzvy nyní mohou obsahovat ikony jako dodatečná metadata

#### Aktualizace dokumentace
- **README.md**: Přidána referenční verze MCP Specifikace 2025-11-25 a vysvětlení verzování podle data
- **study_guide.md**: Aktualizována mapa kurikula o Úkoly a Anotace nástrojů v sekci Základní koncepty; aktualizován časový údaj dokumentu

#### Verifikace souladu specifikace
- **Verze protokolu**: Ověřeno, že veškerá dokumentace odkazuje na aktuální MCP Specifikaci 2025-11-25
- **Architektonická shoda**: Potvrzen popis dvouvrstvé architektury (Data Layer + Transport Layer)
- **Dokumentace primitiv**: Validovány primitiva serveru (Zdroje, Výzvy, Nástroje) a klienta (Sampling, Elicitation, Logging, Roots)
- **Mechanismy transportu**: Ověřena přesnost dokumentace STDIO a Streamovatelného HTTP transportu
- **Bezpečnostní doporučení**: Potvrzen shodný obsah se současnými MCP Best Practices pro bezpečnost

#### Hlavní MCP 2025-11-25 funkce zdokumentovány
- **OpenID Connect Discovery**: Objevování autentizačního serveru přes OIDC
- **OAuth klientská ID metadata dokumenty**: Doporučený mechanismus registrace klienta
- **JSON Schema 2020-12**: Výchozí dialekt pro definice MCP schémat
- **Systém úrovní SDK**: Formalizované požadavky na podporu a údržbu funkcí SDK
- **Správa řízení**: Formalizované pracovní skupiny a zájmové skupiny v správě MCP

### Hlavní aktualizace bezpečnostní dokumentace (02-Security/)

#### Integrace MCP Security Summit Workshop (Sherpa)
- **Nový praktický školicí zdroj**: Přidána rozsáhlá integrace s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) do veškeré bezpečnostní dokumentace
- **Pokrytí trasy expedice**: Zdokumentovaný kompletní postup z tábora do tábora od Base Campu po Summit
- **Soulad s OWASP**: Veškeré bezpečnostní pokyny nyní mapují rizika dle OWASP MCP Azure Security Guide

#### Integrace OWASP MCP Top 10
- **Nová sekce**: Přidána tabulka OWASP MCP Top 10 bezpečnostních rizik s Azure mitigacemi do hlavního bezpečnostního README
- **Dokumentace založená na rizicích**: Aktualizace mcp-security-controls-2025.md s odkazy na rizika OWASP MCP pro každou oblast zabezpečení
- **Referenční architektura**: Odkaz na OWASP MCP Azure Security Guide referenční architekturu a implementační vzory

#### Aktualizované bezpečnostní soubory
- **README.md**: Přidán přehled Sherpa Workshopu, tabulka trasy expedice, shrnutí rizik OWASP MCP Top 10 a sekce praktického školení
- **mcp-security-controls-2025.md**: Aktualizována hlavička na únor 2026, přidány odkazy na OWASP rizika (MCP01-MCP08), oprava nejednotnosti verze specifikace
- **mcp-security-best-practices-2025.md**: Přidána sekce zdrojů Sherpa a OWASP, aktualizováno časové razítko
- **mcp-best-practices.md**: Přidána sekce praktického školení se Sherpa a OWASP odkazy
- **azure-content-safety-implementation.md**: Přidána reference OWASP MCP06, sladění s táborem 3 Sherpa a sekce dodatečných zdrojů

#### Přidány nové odkazy na zdroje
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Jednotlivé stránky rizik OWASP MCP (MCP01-MCP10)

### Zarovnání kurikula s MCP specifikací 2025-11-25

#### Modul 03 - Začínáme
- **Dokumentace SDK**: Přidáno Go SDK do oficiálního seznamu SDK; aktualizovány všechny odkazy na SDK dle MCP specifikace 2025-11-25
- **Upřesnění transportu**: Aktualizovány popisy STDIO a HTTP streaming transportu s explicitními odkazy na specifikaci

#### Modul 04 - Praktická implementace
- **Aktualizace SDK**: Přidáno Go SDK; aktualizován seznam SDK s referencí na verzi specifikace
- **Specifikace autorizace**: Aktualizován odkaz na MCP Authorization specifikaci na aktuální verzi 2025-11-25

#### Modul 05 - Pokročilá témata
- **Nové funkce**: Přidána poznámka o nových funkcích MCP Specifikace 2025-11-25 (Úkoly, Anotace nástrojů, URL mód vyvolávání, Kořeny)
- **Bezpečnostní zdroje**: Přidány odkazy na OWASP MCP Top 10 a Sherpa workshop do dodatkových odkazů

#### Modul 06 - Příspěvky komunity
- **Seznam SDK**: Přidány Swift a Rust SDK; aktualizován odkaz na specifikaci na verzi 2025-11-25
- **Reference specifikace**: Aktualizován odkaz na MCP Specifikaci na přímý URL specifikace

#### Modul 07 - Lekce z rané adopce
- **Aktualizace zdrojů**: Přidán odkaz na MCP Specifikaci 2025-11-25 a OWASP MCP Top 10 do dodatkových zdrojů

#### Modul 08 - Nejlepší praktiky
- **Verze specifikace**: Aktualizována reference na MCP Specifikaci 2025-11-25
- **Bezpečnostní zdroje**: Přidány OWASP MCP Top 10 a Sherpa workshop do dodatkových odkazů

#### Modul 10 - Zefektivnění AI pracovních toků
- **Aktualizace odznaku**: Změněn odznak verze MCP z verze SDK (1.9.3) na verzi specifikace (2025-11-25)
- **Odkazy na zdroje**: Aktualizován odkaz na MCP Specifikaci; přidán OWASP MCP Top 10

#### Modul 11 - MCP server hands-on laboratoře
- **Reference specifikace**: Aktualizován odkaz na MCP Specifikaci na verzi 2025-11-25
- **Bezpečnostní zdroje**: Přidán OWASP MCP Top 10 do oficiálních zdrojů

## 18. prosince 2025
### Aktualizace bezpečnostní dokumentace – Specifikace MCP 2025-11-25

#### Nejlepší bezpečnostní postupy MCP (02-Security/mcp-best-practices.md) – aktualizace verze specifikace
- **Aktualizace verze protokolu**: Aktualizováno pro referenci na nejnovější specifikaci MCP 2025-11-25 (vydáno 25. listopadu 2025)
  - Aktualizovány všechny odkazy na verzi specifikace z 2025-06-18 na 2025-11-25
  - Aktualizovány datumové odkazy v dokumentu z 18. srpna 2025 na 18. prosince 2025
  - Ověřeno, že všechny URL specifikace ukazují na aktuální dokumentaci
- **Validace obsahu**: Komplexní validace nejlepších bezpečnostních praktik vůči nejnovějším standardům
  - **Microsoft Security Solutions**: Ověřena aktuální terminologie a odkazy pro Prompt Shields (dříve "Detekce rizika jailbreaku"), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 Security**: Potvrzeno souladu s nejnovějšími nejlepšími bezpečnostními praktikami OAuth
  - **OWASP standardy**: Validovány odkazy na OWASP Top 10 pro LLM zůstávají aktuální
  - **Azure služby**: Ověřeny všechny odkazy na dokumentaci Microsoft Azure a nejlepší bezpečnostní postupy
- **Soulad se standardy**: Potvrzeno, že všechny odkazované bezpečnostní standardy jsou aktuální
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Bezpečnostní a soulady rámce Azure
- **Implementační zdroje**: Ověřeny všechny odkazy a zdroje k implementačním průvodcům
  - Autentizační vzory Azure API Management
  - Průvodce integrací Microsoft Entra ID
  - Správa tajemství Azure Key Vault
  - DevSecOps pipeline a řešení monitoringu

### Zajištění kvality dokumentace
- **Soulad se specifikací**: Zajištěno, že všechny povinné bezpečnostní požadavky MCP (MUST/MUST NOT) odpovídají nejnovější specifikaci
- **Aktuálnost zdrojů**: Ověřeny všechny externí odkazy na dokumentaci Microsoftu, bezpečnostní standardy a implementační průvodce
- **Pokrytí nejlepších praktik**: Potvrzeno komplexní pokrytí autentizace, autorizace, AI-specifických hrozeb, zabezpečení dodavatelských řetězců a podnikových vzorů

## 6. října 2025

### Rozšíření sekce Začínáme – pokročilé používání serveru a jednoduchá autentizace

#### Pokročilé používání serveru (03-GettingStarted/10-advanced)
- **Přidána nová kapitola**: Představen podrobný průvodce pokročilým používáním MCP serveru, pokrývající běžné i nízkoúrovňové architektury serverů.
  - **Běžný vs. nízkoúrovňový server**: Podrobný rozbor a ukázky kódu v Pythonu a TypeScriptu pro oba přístupy.
  - **Design založený na handleru**: Vysvětlení správy nástrojů/zdrojů/promptů na základě handlerů pro škálovatelné a flexibilní implementace serveru.
  - **Praktické vzory**: Reálné scénáře, kde jsou nízkoúrovňové serverové vzory výhodné pro pokročilé funkce a architekturu.

#### Jednoduchá autentizace (03-GettingStarted/11-simple-auth)
- **Přidána nová kapitola**: Krok za krokem průvodce implementací jednoduché autentizace v MCP serverech.
  - **Koncepty autentizace**: Jasné vysvětlení rozdílu autentizace a autorizace a správy přihlašovacích údajů.
  - **Implementace základní autentizace**: Middleware-bázované vzory autentizace v Pythonu (Starlette) a TypeScriptu (Express) s ukázkami kódu.
  - **Pokrok ke složité bezpečnosti**: Návod, jak začít s jednoduchou autentizací a postupovat k OAuth 2.1 a RBAC, s odkazy na pokročilé bezpečnostní moduly.

Tyto dodatky poskytují praktické, hands-on návody pro vývoj robustnějších, bezpečnějších a flexibilnějších MCP serverových implementací, propojují základní koncepty s pokročilými výrobními vzory.

## 29. září 2025

### Laboratoře integrace databází MCP Serveru – komplexní praktická cesta učením

#### 11-MCPServerHandsOnLabs – nová kompletní kurikulum databázové integrace
- **Kompletní 13 laboratorní cesta učením**: Přidán obsáhlý praktický kurz pro tvorbu produkčně připravených MCP serverů s integrací databáze PostgreSQL
  - **Reálná implementace**: Příklad použití Zava Retail analytics demonstrující podnikové vzory
  - **Strukturovaný postup učení**:
    - **Lab 00-03: Základy** – Úvod, základní architektura, bezpečnost a multi-tenancy, nastavení prostředí
    - **Lab 04-06: Vývoj MCP serveru** – Návrh databáze a schéma, implementace MCP serveru, vývoj nástrojů  
    - **Lab 07-09: Pokročilé funkce** – Integrace sémantického vyhledávání, testování a debugování, integrace VS Code
    - **Lab 10-12: Produkce a nejlepší postupy** – Strategie nasazení, monitoring a sledovatelnost, osvědčené praktiky a optimalizace
  - **Podnikové technologie**: Framework FastMCP, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Pokročilé funkce**: Row Level Security (RLS), sémantické vyhledávání, více-nájemnický přístup k datům, vektorové embeddingy, monitorování v reálném čase

#### Standardizace terminologie – převod modulů na laboratoře
- **Komplexní aktualizace dokumentace**: Systematicky aktualizovány všechny README soubory v 11-MCPServerHandsOnLabs z používání termínu „Module“ na „Lab“
  - **Nadpisy sekcí**: Převzato „What This Module Covers“ na „What This Lab Covers“ ve všech 13 laboratořích
  - **Popisy obsahu**: Změněno „This module provides...“ na „This lab provides...“ v celém obsahu
  - **Cíle učení**: Aktualizováno „By the end of this module...“ na „By the end of this lab...“
  - **Navigační odkazy**: Převod všech „Module XX:“ referencí na „Lab XX:“ v křížových odkazech a navigaci
  - **Sledování dokončení**: Změněno „After completing this module...“ na „After completing this lab...“
  - **Technické reference zachovány**: Zachovány odkazy na Python moduly v konfiguračních souborech (např. `"module": "mcp_server.main"`)

#### Vylepšení studijního průvodce (study_guide.md)
- **Vizualizace kurikula**: Přidána nová sekce „11. Database Integration Labs“ s přehledným zobrazením struktury laboratoří
- **Struktura repozitáře**: Aktualizováno z deseti na jedenáct hlavních sekcí s podrobným popisem 11-MCPServerHandsOnLabs
- **Navigační pokyny**: Vylepšené instrukce k pokrytí sekcí 00-11
- **Pokrytí technologií**: Přidány detaily integrace FastMCP, PostgreSQL a Azure služeb
- **Výsledky učení**: Zdůrazněn vývoj produkčně připravených serverů, vzory integrace databází a podniková bezpečnost

#### Vylepšení hlavní struktury README
- **Terminologie založená na laboratořích**: Aktualizováno hlavní README.md v 11-MCPServerHandsOnLabs na jednotné užívání struktury „Lab“
- **Organizace učební cesty**: Jasná posloupnost od základních konceptů přes pokročilou implementaci až po produkční nasazení
- **Důraz na reálné použití**: Zaměření na praktické, hands-on učení s podnikovými vzory a technologiemi

### Zlepšení kvality a konzistence dokumentace
- **Důraz na praktické učení**: Posílena labově orientovaná metoda veškeré dokumentace
- **Zaměření na podnikové vzory**: Zvýrazněny produkčně připravené implementace a aspekty podnikové bezpečnosti
- **Integrace technologií**: Komplexní pokrytí moderních služeb Azure a IA integračních vzorů
- **Postup učení**: Jasná, strukturovaná cesta od základů k produkčnímu nasazení

## 26. září 2025

### Vylepšení případových studií – Integrace GitHub MCP registru

#### Případové studie (09-CaseStudy/) – Zaměření na rozvoj ekosystému
- **README.md**: Výrazné rozšíření s komplexní případovou studií GitHub MCP Registry
  - **Případová studie GitHub MCP Registry**: Nová podrobná analýza spuštění GitHub MCP Registry v září 2025
    - **Analýza problémů**: Detailní pohled na fragmentované objevení a nasazení MCP serverů
    - **Architektura řešení**: Centralizovaný registr GitHubu s instalací VS Code na jedno kliknutí
    - **Obchodní dopad**: Měřitelné zlepšení onboarding procesů a produktivity vývojářů
    - **Strategická hodnota**: Zaměření na modulární nasazení agentů a interoperabilitu nástrojů
    - **Rozvoj ekosystému**: Pozice jako základní platforma pro agentickou integraci
  - **Zdokonalená struktura případových studií**: Aktualizace všech sedmi studií s jednotným formátováním a komplexním popisem
    - Azure AI Travel Agents: důraz na multi-agentní orchestraci
    - Azure DevOps Integration: zaměření na automatizace workflow
    - Real-Time Documentation Retrieval: implementace Python konzolového klienta
    - Interactive Study Plan Generator: Chainlit konverzační webová aplikace
    - In-Editor Documentation: integrace VS Code a GitHub Copilot
    - Azure API Management: podnikové API integrační vzory
    - GitHub MCP Registry: rozvoj ekosystému a komunitní platforma
  - **Komplexní závěr**: Přepsaná závěrečná sekce zdůrazňující sedm případových studií pokrývajících různé dimenze MCP implementací
    - Podniková integrace, multi-agentní orchestraci, produktivitu vývojářů
    - Rozvoj ekosystému, vzdělávací aplikace
    - Vylepšené vhledy do architektonických vzorů, implementačních strategií a osvědčených postupů
    - Důraz na MCP jako vyspělý, produkčně připravený protokol

#### Aktualizace studijního průvodce (study_guide.md)
- **Vizualizace kurikula**: Aktualizována myšlenková mapa k začlenění GitHub MCP Registry v sekci případových studií
- **Popis případových studií**: Rozvinut z obecného na detailní přehled sedmi komplexních studií
- **Struktura repozitáře**: Aktualizována sekce 10 pro zobrazení komplexního pokrytí případových studií s konkrétními implementačními detaily
- **Integrace changelogu**: Přidán záznam ze 26. září 2025 dokumentující přidání GitHub MCP Registry a rozšíření případových studií
- **Aktualizace datumu**: Aktualizován časový razítko patičky na nejnovější revizi (26. září 2025)

### Zlepšení kvality dokumentace
- **Zvýšení konzistence**: Standardizováno formátování a struktura případových studií u všech sedmi příkladů
- **Komplexní pokrytí**: Případové studie nyní pokrývají podniková, vývojářská a ekosystémová prostředí
- **Strategické umístění**: Zvýrazněno MCP jako základní platforma pro nasazení agentických systémů
- **Integrace zdrojů**: Aktualizovány doplňkové zdroje, aby zahrnovaly odkaz na GitHub MCP Registry

## 15. září 2025

### Rozšíření pokročilých témat – Vlastní transporty a kontextové inženýrství

#### Vlastní MCP transporty (05-AdvancedTopics/mcp-transport/) – nový pokročilý implementační průvodce
- **README.md**: Kompletní průvodce implementací vlastních MCP transportních mechanismů
  - **Azure Event Grid Transport**: Komplexní implementace serverless event-driven transportu
    - Příklady v C#, TypeScriptu a Pythonu s integrací Azure Functions
    - Vzory event-driven architektury pro škálovatelná MCP řešení
    - Příjemci webhooků a zpracování zpráv na základě push
  - **Azure Event Hubs Transport**: Implementace vysokopropustného streamingového transportu
    - Možnosti real-time streamingu pro scénáře s nízkou latencí
    - Strategie partitioningu a správa checkpointů
    - Batching zpráv a optimalizace výkonu
  - **Podnikové integrační vzory**: Produkčně připravené architektonické příklady
    - Distribuované MCP zpracování přes více Azure Functions
    - Hybridní transportní architektury kombinující více typů transportů
    - Strategie odolnosti, spolehlivosti a chybové zacházení
  - **Bezpečnost a monitoring**: Integrace Azure Key Vault a vzory observability
    - Autentizace s managed identity a přístup na principu nejmenšího oprávnění
    - Telemetrie Application Insights a monitoring výkonu
    - Obvodové přerušovače a vzory pro odolnost vůči chybám
  - **Testovací frameworky**: Kompletní strategie testování vlastních transportů
    - Jednotkové testy s pomocí test double a mocking frameworků
    - Integrační testování s Azure Test Containers
    - Úvahy o testování výkonu a zátěže

#### Kontextové inženýrství (05-AdvancedTopics/mcp-contextengineering/) – vznikající AI disciplína
- **README.md**: Komplexní průzkum kontextového inženýrství jako nového oboru
  - **Základní principy**: Kompletní sdílení kontextu, povědomí o rozhodování akcí a správa okna kontextu
  - **Soulad s MCP protokolem**: Jak design MCP řeší výzvy kontextového inženýrství
    - Omezení velikosti okna kontextu a strategie postupného načítání
    - Určování relevance a dynamické načítání kontextu
    - Multi-modální zpracování kontextu a bezpečnostní aspekty
  - **Přístupy k implementaci**: Jednomístný vs. multi-agentní architektury
    - Techniky rozdělení kontextu na části a jejich prioritizace
    - Postupné načítání a kompresní strategie kontextu
    - Vícevrstvé přístupy ke kontextu a optimalizace jeho načítání
  - **Rámec měření**: Vznikající metriky pro hodnocení efektivity kontextu
    - Efektivita vstupu, výkon, kvalita a uživatelská zkušenost
    - Experimentální přístupy k optimalizaci kontextu
    - Analýza selhání a metodologie zlepšení

#### Aktualizace navigace kurikulem (README.md)
- **Vylepšená struktura modulů**: Aktualizována tabulka kurikula pro zahrnutí nových pokročilých témat
  - Přidány položky Kontextové inženýrství (5.14) a Vlastní transport (5.15)
  - Konzistentní formátování a navigační odkazy ve všech modulech
  - Aktualizované popisy reflektující aktuální rozsah obsahu

### Vylepšení struktury adresářů
- **Standardizace názvů**: Přejmenováno „mcp transport“ na „mcp-transport“ pro konzistenci s ostatními složkami pokročilých témat
- **Organizace obsahu**: Všechny složky 05-AdvancedTopics nyní následují jednotný vzor názvů (mcp-[téma])

### Zlepšení kvality dokumentace
- **Soulad se specifikací MCP**: Veškerý nový obsah odkazuje na aktuální specifikaci MCP 2025-06-18
- **Vícejazyčné příklady**: Komplexní ukázky kódu v C#, TypeScriptu a Pythonu
- **Zaměření na podniky**: Produkčně připravené vzory a integrace Azure cloudu napříč celým obsahem
- **Vizualizace dokumentace**: Mermaid diagramy pro architekturu a vizualizaci toku

## 18. srpna 2025

### Komplexní aktualizace dokumentace – standardy MCP 2025-06-18

#### Nejlepší bezpečnostní postupy MCP (02-Security/) – kompletní modernizace
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletní přepis v souladu se specifikací MCP 2025-06-18  
  - **Povinné požadavky**: Přidány explicitní požadavky MUSÍ/MUSÍ NE z oficiální specifikace s jasnými vizuálními indikátory  
  - **12 základních bezpečnostních praktik**: Přeskupeny z 15 položkového seznamu na komplexní bezpečnostní domény  
    - Bezpečnost tokenů a autentizace s integrací externího poskytovatele identity  
    - Správa relací a zabezpečení přenosu s kryptografickými požadavky  
    - Ochrana před AI-specifickými hrozbami s integrací Microsoft Prompt Shields  
    - Řízení přístupu a oprávnění s principem nejmenších práv  
    - Bezpečnost obsahu a monitoring s integrací Azure Content Safety  
    - Bezpečnost dodavatelského řetězce s komplexní ověřovací praxí komponent  
    - OAuth bezpečnost a prevence záměny zprostředkovatele s implementací PKCE  
    - Reakce na incidenty a zotavení s automatizovanými schopnostmi  
    - Soulad s předpisy a správa s regulatorní integrací  
    - Pokročilé bezpečnostní kontroly s architekturou zero trust  
    - Integrace bezpečnostního ekosystému Microsoft s komplexními řešeními  
    - Neustálý vývoj bezpečnosti s adaptivními praktikami  
  - **Microsoft bezpečnostní řešení**: Vylepšené pokyny pro integraci Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security  
  - **Implementační zdroje**: Kategorizované komplexní odkazy na zdroje podle oficiální dokumentace MCP, Microsoft bezpečnostních řešení, bezpečnostních standardů a implementačních průvodců  

#### Pokročilé bezpečnostní kontroly (02-Security/) - Podniková implementace  
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletní přestavba s bezpečnostním rámcem na podnikové úrovni  
  - **9 komplexních bezpečnostních domén**: Rozšířeno z základních kontrol na detailní podnikový rámec  
    - Pokročilá autentizace a autorizace s integrací Microsoft Entra ID  
    - Bezpečnost tokenů a kontroly před předáváním s komplexní validací  
    - Bezpečnost relací s prevencí únosu relace  
    - AI-specifické bezpečnostní kontroly s prevencí injektáže příkazů a otravy nástrojů  
    - Prevence záměny zprostředkovatele s OAuth proxy zabezpečením  
    - Zabezpečení spouštění nástrojů s izolací a sandboxingem  
    - Kontroly bezpečnosti dodavatelského řetězce s ověřováním závislostí  
    - Kontroly monitorování a detekce s integrací SIEM  
    - Reakce na incidenty a zotavení s automatizovanými funkcemi  
  - **Ukázky implementace**: Přidány podrobné YAML konfigurační bloky a ukázky kódu  
  - **Integrace Microsoft řešení**: Komplexní pokrytí Azure bezpečnostních služeb, GitHub Advanced Security a správy podnikové identity  

#### Pokročilá témata bezpečnosti (05-AdvancedTopics/mcp-security/) - Produkční implementace  
- **README.md**: Kompletní přepis pro podnikovou implementaci bezpečnosti  
  - **Soulad s aktuální specifikací**: Aktualizováno podle MCP Specification 2025-06-18 s povinnými bezpečnostními požadavky  
  - **Vylepšená autentizace**: Integrace Microsoft Entra ID s komplexními příklady v .NET a Java Spring Security  
  - **Integrace AI bezpečnosti**: Implementace Microsoft Prompt Shields a Azure Content Safety s podrobnými Python příklady  
  - **Pokročilá mitigace hrozeb**: Komplexní implementační příklady  
    - Prevence záměny zprostředkovatele s PKCE a validací uživatelského souhlasu  
    - Prevence předávání tokenu s validací publika a bezpečnou správou tokenů  
    - Prevence únosu relace s kryptografickým vázáním a behaviorální analýzou  
  - **Integrace podnikové bezpečnosti**: Monitorování Azure Application Insights, pipeline detekce hrozeb a bezpečnost dodavatelského řetězce  
  - **Kontrolní seznam implementace**: Jasné rozlišení povinných a doporučených bezpečnostních kontrol s výhodami Microsoft bezpečnostního ekosystému  

### Kvalita dokumentace a soulad se standardy  
- **Odkazy na specifikace**: Aktualizovány všechny odkazy na aktuální MCP Specification 2025-06-18  
- **Microsoft bezpečnostní ekosystém**: Vylepšené pokyny pro integraci ve všech bezpečnostních dokumentech  
- **Praktická implementace**: Přidány podrobné příklady kódu v .NET, Java a Python s podnikatelskými vzory  
- **Organizace zdrojů**: Komplexní kategorizace oficiální dokumentace, bezpečnostních standardů a implementačních průvodců  
- **Vizuální indikátory**: Jasné označení povinných požadavků versus doporučených praktik  

#### Základní koncepty (01-CoreConcepts/) - Kompletní modernizace  
- **Aktualizace verze protokolu**: Aktualizováno na aktuální MCP Specification 2025-06-18 s verzováním na základě data (formát RRRR-MM-DD)  
- **Zpřesnění architektury**: Vylepšené popisy hostitelů, klientů a serverů odpovídající aktuálním MCP vzorům  
  - Hostitelé nyní jasně definování jako AI aplikace koordinující více připojení MCP klientů  
  - Klienti popsáni jako protokoloví konektory udržující vztahy jeden-na-jednoho se servery  
  - Servery rozšířeny o scénáře místního a vzdáleného nasazení  
- **Přestavba primitiv**: Kompletní přestavba serverových a klientských primitiv  
  - Serverové primitivy: Zdroje (datové zdroje), Výzvy (šablony), Nástroje (spustitelné funkce) s podrobnými vysvětleními a příklady  
  - Klientské primitivy: Vzorkování (ukončení LLM), Vyvolání (uživatelský vstup), Logování (ladění/monitoring)  
  - Aktualizováno podle současných vzorů metod discovery (`*/list`), retrieval (`*/get`) a execution (`*/call`)  
- **Architektura protokolu**: Zaveden dvouvrstvý architektonický model  
  - Vrstva dat: Základ JSON-RPC 2.0 s řízením životního cyklu a primitivy  
  - Vrstva přenosu: STDIO (místní) a Streamable HTTP s SSE (vzdálený) přenosové mechanismy  
- **Bezpečnostní rámec**: Komplexní bezpečnostní principy včetně explicitního souhlasu uživatele, ochrany dat, bezpečného spouštění nástrojů a zabezpečení přenosové vrstvy  
- **Komunikační vzory**: Aktualizované protokolové zprávy ukazující inicializaci, discovery, provedení a notifikační toky  
- **Ukázky kódu**: Obnovené příklady pro více jazyků (.NET, Java, Python, JavaScript) odpovídající aktuálním vzorům MCP SDK  

#### Bezpečnost (02-Security/) - Komplexní bezpečnostní přestavba  
- **Soulad se standardy**: Plný soulad s bezpečnostními požadavky MCP Specification 2025-06-18  
- **Vývoj autentizace**: Dokumentována evoluce od vlastních OAuth serverů k delegaci na externí poskytovatele identity (Microsoft Entra ID)  
- **Analýza AI-specifických hrozeb**: Rozšířené pokrytí moderních AI útoků  
  - Detailní scénáře útoků injektáží příkazů s reálnými příklady  
  - Mechanismy otravy nástrojů a vzory útoku „rug pull“  
  - Otrava kontextového okna a útoky na zmatení modelu  
- **Microsoft AI bezpečnostní řešení**: Komplexní pokrytí Microsoft bezpečnostního ekosystému  
  - AI Prompt Shields s pokročilou detekcí, zdůrazňováním a metodami oddělovačů  
  - Vzory integrace Azure Content Safety  
  - GitHub Advanced Security pro ochranu dodavatelského řetězce  
- **Pokročilá mitigace hrozeb**: Detailní bezpečnostní kontroly pro  
  - Únos relace s MCP-specifickými scénáři útoků a kryptografickými požadavky na session ID  
  - Problémy záměny zprostředkovatele v MCP proxy scénářích s explicitními požadavky na souhlas  
  - Zranitelnosti předávání tokenů s povinnými kontrolami validace  
- **Bezpečnost dodavatelského řetězce**: Rozšířené pokrytí AI dodavatelského řetězce včetně základních modelů, embedding služeb, poskytovatelů kontextu a třetích stran API  
- **Základní bezpečnost**: Vylepšená integrace s podnikatelskými bezpečnostními vzory včetně architektury zero trust a Microsoft bezpečnostního ekosystému  
- **Organizace zdrojů**: Kategorizované komplexní odkazy na zdroje podle typu (Oficiální dokumentace, Standardy, Výzkum, Microsoft řešení, Implementační průvodci)  

### Zlepšení kvality dokumentace  
- **Strukturované učební cíle**: Vylepšené učební cíle se specifickými a akčními výsledky  
- **Křížové odkazy**: Přidány odkazy mezi souvisejícími tématy bezpečnosti a základních konceptů  
- **Aktuální informace**: Aktualizovány všechny datumové odkazy a odkazy na specifikace na aktuální standardy  
- **Pokyny k implementaci**: Přidány konkrétní a akční pokyny k implementaci v obou částech  

## 16. července 2025

### README a vylepšení navigace  
- Kompletně přepracována navigace osnovy v README.md  
- Nahrazeny značky `<details>` přístupnějším formátem založeným na tabulkách  
- Vytvořeny alternativní rozložení ve složce "alternative_layouts"  
- Přidány příklady navigace v kartách, záložkách a stylu harmoniky  
- Aktualizována sekce struktury repozitáře zahrnující všechny nejnovější soubory  
- Vylepšená sekce "Jak používat tuto osnovu" s jasnými doporučeními  
- Aktualizovány odkazy na MCP specifikace na správné URL  
- Přidána sekce Kontextové inženýrství (5.14) do struktury osnovy  

### Aktualizace studijního průvodce  
- Kompletně přepracován studijní průvodce v souladu s aktuální strukturou repozitáře  
- Přidány nové sekce o MCP klientech a nástrojích a populárních MCP serverech  
- Aktualizována vizuální mapa osnovy přesně odrážející všechna témata  
- Vylepšeny popisy pokročilých témat pro pokrytí všech specializovaných oblastí  
- Aktualizována sekce případových studií reflektující skutečné příklady  
- Přidán tento komplexní seznam změn  

### Příspěvky komunity (06-CommunityContributions/)  
- Přidány podrobné informace o MCP serverech pro generování obrázků  
- Přidána komplexní sekce o používání Claude ve VSCode  
- Přidány instrukce pro nastavení a používání terminálového klienta Cline  
- Aktualizována sekce MCP klientů o všechny populární klientské možnosti  
- Vylepšeny příklady příspěvků s přesnějšími ukázkami kódu  

### Pokročilá témata (05-AdvancedTopics/)  
- Organizovány všechny speciální složky témat s konzistentním pojmenováním  
- Přidány materiály a příklady kontextového inženýrství  
- Přidána dokumentace integrace Foundry agenta  
- Vylepšena dokumentace integrace bezpečnosti Entra ID  

## 11. června 2025

### První vytvoření  
- Vydána první verze osnovy MCP pro začátečníky  
- Vytvořena základní struktura pro všech 10 hlavních sekcí  
- Implementována vizuální mapa osnovy pro navigaci  
- Přidány počáteční ukázkové projekty v několika programovacích jazycích  

### Začínáme (03-GettingStarted/)  
- Vytvořeny první příklady implementace serveru  
- Přidány pokyny pro vývoj klienta  
- Zahrnuty instrukce pro integraci LLM klienta  
- Přidána dokumentace integrace do VS Code  
- Implementovány serverové příklady Server-Sent Events (SSE)  

### Základní koncepty (01-CoreConcepts/)  
- Přidáno podrobné vysvětlení klient-server architektury  
- Vytvořena dokumentace klíčových komponent protokolu  
- Dokumentovány vzory zpráv v MCP  

## 23. května 2025

### Struktura repozitáře  
- Inicializován repozitář se základní strukturou složek  
- Vytvořeny README soubory pro každou hlavní sekci  
- Nastavena infrastruktura pro překlady  
- Přidány obrazové zdroje a diagramy  

### Dokumentace  
- Vytvořen základní README.md s přehledem osnovy  
- Přidány soubory CODE_OF_CONDUCT.md a SECURITY.md  
- Nastaven SUPPORT.md s pokyny jak získat pomoc  
- Vytvořena předběžná struktura studijního průvodce  

## 15. dubna 2025

### Plánování a rámec  
- Počáteční plánování osnovy MCP pro začátečníky  
- Definovány učební cíle a cílová skupina  
- Návrh struktury osnovy v 10 sekcích  
- Vypracován koncepční rámec pro příklady a případové studie  
- Vytvořeny první prototypové příklady klíčových konceptů

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, uvědomte si prosím, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->