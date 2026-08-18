# Zoznam zmien: Kurikulum MCP pre začiatočníkov

Tento dokument slúži ako záznam všetkých významných zmien vykonaných v kurikule Model Context Protocol (MCP) pre začiatočníkov. Zmeny sú zaznamenané v obrátenom chronologickom poradí (najnovšie zmeny prvé).

## 29. júla 2026

### Nový modul 08 doplnok: Spoľahlivé sidecary a bezpečné opakovania

Pridaná nezávislá doprovodná lekcia k nástrojom MCP, ktoré vytvárajú reálne
efekty, zosúladená s konečnou špecifikáciou `2026-07-28`.

- **Nové**: [doprovodná lekcia o spoľahlivostných sidecaroch][reliability-sidecar]
  používa jeden príbeh o podpore lístkov, dva Mermaid diagramy a rozhodovací tok opakovaní
  na vysvetlenie kľúčov stabilnej prevádzky, atómovej duplicitnej admisie,
  zosúladzovania, dôkazov a hranice rozšírenia úloh (Tasks).
- **Nové**: Cvičenie so zlyhaním pomocou štandardnej knižnice Python a SQLite
  používa oddelené obchody operácií a lístkov na demonštráciu odpovede, ktorá sa stratila
  po spustení externého efektu. Šesť deterministických testov pokrýva naivnú
  duplicitu, zabezpečené obnovenie reštartu, konflikty nákladu, uložené výsledky,
  aktívne nároky a paralelnú duplicitnú admisiu.
- **Aktualizované**: Modul 08 teraz odkazuje na doprovodnú lekciu, identifikuje
  konečný stavový model požiadavky `2026-07-28`, rozlišuje OpenTelemetry
  pozorovateľnosť od zastaranej funkcie protokolovania MCP a obmedzuje svoj
  generický príklad opakovaní na operácie iba na čítanie.
- **Voliteľné**: Lekcia mapuje svoje prenosné koncepty na jednu označenú komunitnú
  implementáciu bez toho, aby zahrnula hosťovanú službu alebo sieťové volanie
  ako súčasť cvičenia.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. júla 2026

### Nová lekcia: Kandidát na vydanie špecifikácie MCP 2026-07-28

Pridané pokrytie nadchádzajúceho kandidáta na vydanie špecifikácie MCP `2026-07-28` (oznámené 21. mája 2026; konečné vydanie plánované na 28. júl 2026), zhrnuté z [oficiálneho blogového príspevku oznámenia](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Základom kurikula zostáva **MCP Špecifikácia 2025-11-25**, kým nebude nová verzia vydaná, takže je to prezentované ako výhľadové usmernenie a nie prepis existujúcich lekcií.

- **Nové**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — plná lekcia pokrývajúca jadro bezstavového protokolu (odstránenie úvodného handshaku `initialize` a `Mcp-Session-Id`), nové smerovacie hlavičky `Mcp-Method`/`Mcp-Name`, metadata cachovania `ttlMs`/`cacheScope`, W3C Trace Context v `_meta`, formálny rámec rozšírení (MCP Apps a nové rozšírenie Tasks), šesť SEP na zosilnenie autorizácie, vysadenie Roots/Sampling/Logging a prechod na plný JSON Schema 2020-12 pre schémy nástrojov.
- **Aktualizované** s výhľadovými odkazmi na novú lekciu:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): poznámka o verzii protokolu, sekcie Sampling/Roots/Logging/Tasks a "Čo ďalej"
  - [02-Security/README.md](./02-Security/README.md): upozornenie na zosilnenie autorizácie
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): upozornenie na bezstavový transport
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): upozornenie na vysadenie Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): upozornenie na vysadenie Logging a rozšírenie Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): upozornenie na bezstavové/smerovanie relácií
  - [README.md](./README.md): poznámka "Pohľad do budúcnosti" v sekcii špecifikácie a nová položka `1.1` v tabuľke modulov kurikula
  - [study_guide.md](./study_guide.md): výhľadový bod v prehľade základných konceptov a datovaná dodatková poznámka
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): upozornenie na mapu transportu `mcp-session-id` pred modelom bezstavovej požiadavky
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): prehľad modulu o vysadení Root Contexts/Sampling a o rozšírení Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): upozornenie na zosilnenie autorizácie

## 24. júna 2026

### Nová lekcia: Použitie MCP v aplikácii Copilot

- [Sekcia nástrojov](./12-tooling/README.md) Pridaná sekcia nástrojov.
- [MCP v aplikácii Copilot](./12-tooling/01-copilot-app/README.md)

## 16. júna 2026

### Zladenie so špecifikáciou MCP & validácia príkladov

Overili sme kurz podľa aktuálnej **MCP Špecifikácie 2025-11-25** a najnovších oficiálnych SDK, potom sme opravili zvyšné zastaralé odkazy na špecifikácie a potvrdili, že základné príklady sa stále kompilujú a spúšťajú.

#### Opravy verzie špecifikácie (2025-06-18 / 2025-03-26 → 2025-11-25)

Aktualizovaný anglický obsah, kde sa stále uvádzalo, že staršia revízia špecifikácie je *aktuálny/najnovší* štandard, a presmerované odkazy na kanonické cesty špecifikácií `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Aktualizovaný banner "Aktuálny štandard", úvod, nadpis hlavnej bezpečnostnej politiky, nadpis povinných požiadaviek, sekcia Microsoft Entra ID, odkazy s referenciami a zdrojmi a záverečné bezpečnostné upozornenie (8 odkazov) na 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Aktualizovaný odkaz na pomôcky a banner "Aktuálny štandard" na 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Nahradený zastaralý odkaz na bezpečnosť `2025-03-26` aktuálnou stránkou najlepších bezpečnostných postupov pre 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Aktualizovaný oficiálny odkaz na Sampling na 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Aktualizovaný súčasný odkaz na "aktuálnu špecifikáciu MCP" a odkaz na pomôcky na 2025-11-25 (historické poznámky k deprekácii SSE zostali pre presnosť)

#### Validácia príkladov s aktuálnymi SDK

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` vyriešil `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` prešlo bez chýb typov — existujúce API `McpServer`/`StdioServerTransport` sú stále platné
- **Python (03-GettingStarted/01-first-server/solution/python)**: Overené v izolovanom `.venv` s `mcp[cli]` (1.27.2); `py_compile` prešlo a `FastMCP.list_tools()` správne vrátil nástroje `add` a `subtract`
- Potvrdené, že všetky rozsahy verzií `@modelcontextprotocol/sdk` v príkladoch (`>=1.26.0` / `^1.26.0` / `^1.27.0`) sa čistotne vyriešia na aktuálnu `1.29.0` bez prerušenia API

#### Zladenie závislostí (uzatváranie medzier vo verziách)

Zvyšovanie zastaralých pripnutých verzií SDK, takže každý príklad sleduje aktuálne vydanie MCP, v súlade s konvenciou celého repo:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Zvýšený `@modelcontextprotocol/sdk` z `^1.8.0` na `>=1.26.0` a aktualizovaný zastaralý popis balíka `"updated for MCP 2025-06-18"` na `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** a **lab4/code/github_mcp_server/pyproject.toml**: Zvýšený presný pin `mcp==1.23.0` na `mcp>=1.26.0`; obnovené oba lock súbory `uv.lock` (`uv lock`), aby lock súbory smerovali na aktuálny `mcp 1.27.2` a boli synchronizované s manifestami

#### Analýza medzier v kurikule — pokrytie najnovších funkcií špecifikácie

Overené, že kurikulum už pokrýva všetky primitíva zavedené/rozšírené v MCP 2025-11-25, takže nezostali žiadne obsahové medzery:
- **Sampling**: Lekcia 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (vrátane URL režimu)**: Zdokumentované v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Zdokumentované v 00-Introduction, 01-CoreConcepts a 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentálne, dlhodobé operácie)**: Zdokumentované v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Anotácie nástrojov** (`readOnlyHint` / `destructiveHint`): Zdokumentované v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features

### Zosilnenie bezpečnosti a oprava zraniteľností závislostí

Prebehla kompletná bezpečnostná kontrola všetkých manifestov závislostí a zdrojového kódu príkladov a následne boli opravené všetky hlásené npm upozornenia a jedna zistená bezpečnostná chyba v kóde. Po oprave hlásenie `npm audit` uvádza **0 zraniteľností** vo všetkých kontrolovaných adresároch.

#### npm zraniteľnosti závislostí (prenosné) — Opravené

Skontrolovaných všetkých 15 publikovaných súborov `package-lock.json`. Zraniteľnosti boli obmedzené na prenosné závislosti prichádzajúce z vývojárskeho nástroja MCP Inspector, OpenAI klienta a MCP SDK; všetky sú teraz vyriešené bez prerušenia príkladov:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** a **lab3/code/weather_mcp/inspector**: Zvýšený `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), čo vyriešilo nahlásenia `ajv`, `brace-expansion`, `diff`, `path-to-regexp` a `ws`. Pridaný záznam npm `overrides` nútiaci opravený `shell-quote@1.8.4` na odstránenie pretrvávajúceho kritického varovania v rámci `concurrently`; obnovené oba lock súbory (teraz 0 zraniteľností)
- **03-GettingStarted/samples/typescript**: `npm audit fix` aktualizoval prenosný `qs` (mierna zraniteľnosť) na opravené vydanie
- **03-GettingStarted/samples/javascript**: `npm audit fix` aktualizoval prenosný `hono` (mierna zraniteľnosť) na opravené vydanie
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` aktualizoval prenosný `form-data` (vysoká zraniteľnosť) na opravené vydanie
- **03-GettingStarted/11-simple-auth/solution/typescript**: Vygenerovaný chýbajúci `package-lock.json`, aby bol projekt reprodukovateľný a kontrolovateľný (0 zraniteľností)

#### Bezpečnostná oprava na úrovni kódu (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Odstránený parameter `shell=True` z nástroja `open_in_vscode`. Predchádzajúci príkaz `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` umožňoval interpretáciu shell metaznakov v ceste k adresáru cez `cmd.exe` (vektor injekcie príkazov). Teraz spúšťa priamo vyriešený `Code.exe` s adresárom ako argumentom — bez shellu — čo je funkčne rovnaké a bezpečné

#### Python audit závislostí

- Kontrolované všetky Python požiadavky pomocou `pip-audit`. `05-AdvancedTopics` a `03-GettingStarted/samples/python` nezaznamenali **žiadne známe zraniteľnosti** (ich rozsahy `mcp` / `httpx` / `pydantic` / `python-dotenv` sa vyriešia na aktuálne pevné vydania)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` označil prenosnú závislosť **`werkzeug` 3.1.1** s tromi upozorneniami na DoS cez `safe_join` v systéme Windows — `CVE-2025-66221`, `CVE-2026-21860` a `CVE-2026-27199` (všetky opravené v 3.1.6). Pridaný explicitný bezpečnostný pin `werkzeug>=3.1.6`, aby sa vyriešilo opravené vydanie; overené, že obmedzenie sa čisto vyrieši s `chainlit` / `mcp` / `semantic-kernel` stack

### Rebranding názvu produktu

Aktualizovaný celý obsah kurikula, aby odrážal rebranding produktov Microsoftu:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Aktualizovaný odkaz na Discord komunitu

- **AGENTS.md**: Aktualizovaný odkaz na Discord server
- **README.md**: Aktualizované odkazy na technologický ekosystém
- **study_guide.md**: Aktualizované odkazy na prípadové štúdie
- **05-AdvancedTopics/README.md**: Aktualizovaný názov a opis modulu 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Aktualizovaný nadpis sekcie a popis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Kompletná aktualizácia názvu modulu a obsahu
- **05-AdvancedTopics/mcp-security-entra/README.md**: Aktualizovaný odkaz na krížovú referenciu
- **07-LessonsfromEarlyAdoption/README.md**: Aktualizované odkazy na prípadové štúdie
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Aktualizovaný nadpis sekcie 9, odznaky a možnosti
- **08-BestPractices/README.md**: Aktualizovaný odkaz na Discord komunitu
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Aktualizovaný odkaz na Discord kanál
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Aktualizovaný odkaz na nasadenie modelu
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Aktualizovaná tabuľka služieb AI
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Aktualizované odkazy na zdroje

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension pre VS Code
- **README.md**: Aktualizované hlavné odkazy v učebnom pláne
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Aktualizovaný názov modulu, prehľad a všetky nadpisy modulov
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Aktualizovaný názov, ciele učenia, inštrukcie nastavenia a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Aktualizovaný názov, ciele učenia, tabuľka hostiteľov MCP a krížové odkazy
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Aktualizovaný názov, odznaky, predpoklady a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Aktualizované odkazy na Agent Builder a odkaz na spätnú väzbu
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Aktualizované predpoklady a odkazy na rozšírenia

---

## 11. apríl 2026

### Nová lekcia, opravy dokumentácie a aktualizácie závislostí

#### Pridaný nový obsah učebného plánu

**Modul 05 - Pokročilé témy**
- **Lekcia 5.17: Adversariálne viacagentné uvažovanie s MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nový komplexný sprievodca pokrývajúci vzor sporu viacagentných systémov
  - Diagram architektúry Mermaid: dvaja agenti → zdieľaný MCP server → prepis sporu → rozhodca → verdikt
  - Zdieľaný MCP nástrojový server (`web_search` + `run_python`) implementovaný v Pythone a TypeScripte
  - Protiľahlé systémové výzvy (PRE / PROTI / Rozhodca) s explicitnými požiadavkami na použitie nástrojov
  - Orchester sporu v Pythone, TypeScripte a C# spravujúci kolá a smerovanie argumentov
  - Prepojenie MCP `ClientSession` pre orchestrátora na reálne volania nástrojov
  - Tabuľka prípadov použitia (detekcia halucinácií, modelovanie hrozieb, revízia návrhu API, faktická overiteľnosť, výber technológií)
  - Bezpečnostné úvahy: spustenie v pieskovisku, validácia volaní nástroja, obmedzenie rýchlosti, auditovanie
  - Štruktúrované cvičenie s tromi praktickými situáciami (kontrola kódu, rozhodovanie o architektúre, moderovanie obsahu)

#### Opravy dokumentácie

**Modul 03 - Začíname**
- **05-stdio-server/README.md**: Opravený neúplný príklad TypeScript stdio servera — pridaná chýbajúca inštancia transportu (`new StdioServerTransport()`) a volanie `server.connect(transport)` pre zhodu s príkladmi Pythonu a .NET v rovnakej sekcii
- **14-sampling/README.md**: Opravená chyba — opravené `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aktualizácie učebného plánu

**Hlavný README.md**
- Pridaný záznam 5.17 (Adversariálne viacagentné uvažovanie s MCP) do tabuľky učebného plánu s priamym odkazom na novú lekciu

**05-AdvancedTopics/README.md**
- Pridaný riadok lekcie 5.17 do tabuľky lekcií

**study_guide.md**
- Pridaná téma Adversariálne viacagentné uvažovanie do myšlienkovej mapy a popisu pokročilých tém

#### Opravy kódu a bezpečnosti

**Modul 05 - Adversariálni agenti (`mcp-adversarial-agents`)**
- **Bezpečnostná oprava — injekcia príkazu**: Nahradené interpolovanie shellu `execSync` kombináciou `execFile` + `promisify` v TypeScript nástroji `run_python`, čím sa eliminuje povrch pre injekciu príkazov (kód riadený LLM sa teraz odovzdáva ako doslovný prvok argv bez zapojenia shellu)
- **Prepojenie slučky MCP nástroja**: Aktualizovaný orchestrátor sporu v Pythone na použitie klienta `AsyncAnthropic` (nahrádza blokujúci synchronný `Anthropic`), priamo odovzdáva živú `ClientSession` každej agentovej otočke, načítava definície nástrojov cez `session.list_tools()` každé kolo a posiela bloky `tool_use` cez `session.call_tool()` v slučke až do vydania finálnej textovej odpovede modelom

#### Aktualizácie závislostí

- Zvýšenie verzie `hono` na 4.12.12 naprieč viacerými balíčkami (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Zvýšenie verzie `@hono/node-server` z 1.19.11 na 1.19.13 v balíčkoch TypeScript
- Zvýšenie verzie `cryptography` z 46.0.5 na 46.0.7 v Python balíčkoch (laboratória 3 a 4 v 10-StreamliningAIWorkflows)
- Zvýšenie verzie `lodash` z 4.17.23 na 4.18.1 v inspektore 10-StreamliningAIWorkflows

#### Preklady

- Synchronizované preklady pre 48+ jazykov s najnovšími zdrojovými zmenami (i18n aktualizácia)

---

## 5. február 2026

### Validácia a vylepšenia navigácie v celom repozitári

#### Pridaný nový obsah učebného plánu

**Modul 03 - Začíname**
- **12-mcp-hosts/README.md**: Nový komplexný sprievodca nastavením hostiteľov MCP
  - Príklady konfigurácií pre Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Šablóny JSON konfigurácií pre všetkých hlavných hostiteľov
  - Tabuľka porovnania typov transportu (stdio, SSE/HTTP, WebSocket)
  - Riešenie bežných problémov s pripojením
  - Najlepšie praktiky zabezpečenia konfigurácie hostiteľa

- **13-mcp-inspector/README.md**: Nový sprievodca ladením pre MCP Inspector
  - Spôsoby inštalácie (npx, globálne npm, zo zdroja)
  - Pripojenie k serverom cez stdio a HTTP/SSE
  - Testovacie nástroje, zdroje a pracovné postupy promptov
  - Integrácia s VS Code cez MCP Inspector
  - Bežné scenáre ladenia s riešeniami

**Modul 04 - Praktická implementácia**
- **pagination/README.md**: Nový sprievodca implementáciou stránkovania
  - Vzory stránkovania založené na kurzore v Pythone, TypeScripte, Jave
  - Spracovanie stránkovania na strane klienta
  - Stratégie návrhu kurzora (nepriehľadný vs. štruktúrovaný)
  - Odporúčania na optimalizáciu výkonu

**Modul 05 - Pokročilé témy**
- **mcp-protocol-features/README.md**: Hĺbkový rozbor noviniek protokolu
  - Implementácia notifikácií o priebehu
  - Vzory rušenia požiadaviek
  - Šablóny zdrojov s URI vzormi
  - Správa životného cyklu servera
  - Riadenie úrovne logovania
  - Vzory spracovania chýb s JSON-RPC kódmi

#### Opravy navigácie (aktualizácia 24+ súborov)

**Hlavné moduly README**
 Teraz odkazuje na súčasne prvú lekciu AJ nasledujúci modul

**Podadresáre 02-Security**
- Všetkých 5 doplnkových bezpečnostných dokumentov má teraz navigáciu "Čo ďalej":

**Súbory 09-CaseStudy**
- Všetky súbory prípadových štúdií majú sekvenčnú navigáciu:

**Laboratória 10-StreamliningAI**
Pridaná sekcia Čo ďalej do prehľadu modulu 10 a do modulu 11

#### Opravy kódu a obsahu

**Aktualizácie SDK a závislostí**
Opravená prázdna verzia openai na `^4.95.0`
Aktualizovaný SDK z `^1.8.0` na `>=1.26.0`
Aktualizované pripnutia verzie mcp na `>=1.26.0`

**Opravy kódu**
Opravený neplatný model `gpt-4o-mini` na `gpt-4.1-mini`

**Opravy obsahu**
Opravený chybný odkaz `READMEmd` → `README.md`, opravený nadpis učebného plánu `Module 1-3` → `Module 0-3`, opravená citlivosť na veľkosť písmen v cestách
Odstránený poškodený duplicitný obsah Prípadovej štúdie 5

**Vylepšenia pre začiatočníkov**
Pridaný riadny úvod, ciele učenia a predpoklady pre začiatočníkov

#### Aktualizácie učebného plánu

**Hlavný README.md**
- Pridané položky 3.12 (MCP hostitelia), 3.13 (MCP Inspector), 4.1 (Stránkovanie), 5.16 (Funkcie protokolu) do tabuľky učebného plánu

**README moduly**
Pridané lekcie 12 a 13 do zoznamu lekcií
Pridaná sekcia Praktické príručky s odkazom na stránkovanie
Pridané lekcie 5.15 (Vlastný transport) a 5.16 (Funkcie protokolu)

**study_guide.md**
- Aktualizovaná myšlienková mapa so všetkými novými témami: Nastavenie MCP hostiteľov, MCP Inspector, stratégie stránkovania, hĺbkový rozbor funkcií protokolu

## 28. január 2026

### Preskúmanie zhody so špecifikáciou MCP 2025-11-25

#### Vylepšenie základných konceptov (01-CoreConcepts/)
- **Nová klientská primitíva - Roots**: Pridaná komplexná dokumentácia ku klientovej primitíve Roots umožňujúca serverom porozumieť hraniciam súborového systému a povoleniam prístupu
- **Anotácie nástrojov**: Pridaná dokumentácia o behaviorálnych anotáciách nástrojov (`readOnlyHint`, `destructiveHint`) na lepšie rozhodovanie pri ich vykonávaní
- **Volanie nástrojov pri Sampling**: Aktualizovaná dokumentácia Sampling o parametroch `tools` a `toolChoice` pre volanie nástrojov riadené modelom počas žiadostí o sampling
- **URL režim vyvolania**: Pridaná dokumentácia o URL-založenom vyvolávaní pre serverom iniciované externé webové interakcie
- **Úlohy (experimentálne)**: Pridaná nová sekcia dokumentujúca experimentálnu funkciu úloh pre trvalé obaly vykonávania a odložené získavanie výsledkov
- **Podpora ikon**: Uvedené, že nástroje, zdroje, šablóny zdrojov a prompt môžu teraz obsahovať ikony ako doplnkové metaúdaje

#### Aktualizácie dokumentácie
- **README.md**: Pridaná referenciu na verziu špecifikácie MCP 2025-11-25 a vysvetlenie verziovania podľa dátumu
- **study_guide.md**: Aktualizovaná mapa učebného plánu o Úlohy a Anotácie nástrojov v sekcii základných konceptov; aktualizovaný časový údaj dokumentu

#### Overenie zhody so špecifikáciou
- **Verzia protokolu**: Overené, že všetka dokumentácia odkazuje na aktuálnu špecifikáciu MCP 2025-11-25
- **Zladenie architektúry**: Potvrdená správnosť dokumentácie dvojvrstvovej architektúry (vrstva dát + vrstva transportu)
- **Dokumentácia primitív**: Validované primitívy servera (zdroje, prompt, nástroje) a primitívy klienta (Sampling, Elicitation, Logging, Roots)
- **Transportné mechanizmy**: Overená správnosť dokumentácie STDIO a Streamable HTTP transportu
- **Bezpečnostné odporúčania**: Potvrdené zladenie s aktuálnymi najlepšími bezpečnostnými praktikami MCP

#### Kľúčové funkcie MCP 2025-11-25 zdokumentované
- **OpenID Connect Discovery**: Objavovanie autentifikačných serverov cez OIDC
- **Metadáta OAuth Client ID dokumentov**: Odporúčaný mechanizmus registrácie klienta
- **JSON Schema 2020-12**: Predvolený dialekt pre definície MCP schém
- **Systém vrstvenia SDK**: Formalizované požiadavky na podporu a údržbu funkcií SDK
- **Štruktúra správy**: Formalizované pracovné skupiny a záujmové skupiny v správe MCP

### Hlavná aktualizácia bezpečnostnej dokumentácie (02-Security/)

#### Integrácia MCP Security Summit Workshop (Sherpa)
- **Nový praktický tréningový zdroj**: Pridaná komplexná integrácia s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) vo všetkej bezpečnostnej dokumentácii
- **Pokrytie trasy expedície**: Zdokumentovaný kompletný postup z tábora do tábora od základného tábora po vrchol
- **Zladenie s OWASP**: Všetky bezpečnostné odporúčania teraz mapujú riziká OWASP MCP Azure Security Guide

#### Integrácia OWASP MCP Top 10
- **Nová sekcia**: Pridaná tabuľka rizík OWASP MCP Top 10 s mitigáciami pre Azure do hlavného bezpečnostného README
- **Dokumentácia založená na rizikách**: Aktualizovaný súbor mcp-security-controls-2025.md s referenciami na riziká OWASP MCP pre každú bezpečnostnú doménu
- **Referenčná architektúra**: Prepojenie na referenčnú architektúru a vzory implementácie OWASP MCP Azure Security Guide

#### Aktualizované bezpečnostné súbory
- **README.md**: Pridaný prehľad Sherpa Workshopu, tabuľka trasy expedície, súhrn rizík OWASP MCP Top 10 a sekcia praktického školenia
- **mcp-security-controls-2025.md**: Aktualizovaný nadpis na február 2026, pridané referencie OWASP rizík (MCP01-MCP08), opravená nezhoda verzií
- **mcp-security-best-practices-2025.md**: Pridaná sekcia zdrojov Sherpa a OWASP, aktualizovaný časový údaj
- **mcp-best-practices.md**: Pridaná sekcia praktického školenia s odkazmi na Sherpa a OWASP
- **azure-content-safety-implementation.md**: Pridaná referencia OWASP MCP06, zladenie s Camp 3 Sherpa a sekcia dodatočných zdrojov

#### Pridané nové odkazy na zdroje
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuálne OWASP MCP stránky rizík (MCP01-MCP10)

### Zarovnanie špecifikácie MCP pre celú osnovu 2025-11-25

#### Modul 03 - Začíname
- **Dokumentácia SDK**: Pridané Go SDK do oficiálneho zoznamu SDK; aktualizované všetky odkazy na SDK podľa špecifikácie MCP 2025-11-25
- **Vysvetlenie transportu**: Aktualizované popisy transportov STDIO a HTTP Streaming s explicitnými odkazmi na špecifikáciu

#### Modul 04 - Praktická implementácia
- **Aktualizácie SDK**: Pridané Go SDK; aktualizovaný zoznam SDK s odkazom na verziu špecifikácie
- **Špecifikácia autorizácie**: Aktualizovaný odkaz na MCP Authorization špecifikáciu na aktuálnu verziu 2025-11-25

#### Modul 05 - Pokročilé témy
- **Nové funkcie**: Pridaná poznámka o nových funkciách MCP špecifikácie 2025-11-25 (Úlohy, Anotácie nástrojov, URL mód vyvolávania, Korene)
- **Bezpečnostné zdroje**: Pridané odkazy na OWASP MCP Top 10 a Sherpa workshop do ďalších referencií

#### Modul 06 - Príspevky komunity
- **Zoznam SDK**: Pridané Swift a Rust SDK; aktualizovaný odkaz na špecifikáciu na 2025-11-25
- **Odkaz na špecifikáciu**: Aktualizovaný odkaz na MCP špecifikáciu priamo na URL špecifikácie

#### Modul 07 - Lekcie z prvotného nasadenia
- **Aktualizácie zdrojov**: Pridaný odkaz na MCP špecifikáciu 2025-11-25 a OWASP MCP Top 10 do ďalších zdrojov

#### Modul 08 - Najlepšie postupy
- **Verzia špecifikácie**: Aktualizovaný odkaz na MCP špecifikáciu na 2025-11-25
- **Bezpečnostné zdroje**: Pridaný OWASP MCP Top 10 a Sherpa workshop do ďalších referencií

#### Modul 10 - Optimalizácia AI pracovných tokov
- **Aktualizácia odznaku**: Zmenený odznak verzie MCP z verzie SDK (1.9.3) na verziu špecifikácie (2025-11-25)
- **Odkazy na zdroje**: Aktualizovaný odkaz na MCP špecifikáciu; pridaný OWASP MCP Top 10

#### Modul 11 - Praktické laboratóriá MCP servera
- **Odkaz na špecifikáciu**: Aktualizovaný odkaz na MCP špecifikáciu na verziu 2025-11-25
- **Bezpečnostné zdroje**: Pridaný OWASP MCP Top 10 do oficiálnych zdrojov

## 18. december 2025

### Aktualizácia bezpečnostnej dokumentácie - MCP Špecifikácia 2025-11-25

#### Najlepšie bezpečnostné praktiky MCP (02-Security/mcp-best-practices.md) - Aktualizácia verzie špecifikácie
- **Aktualizácia verzie protokolu**: Aktualizované odkazy na najnovšiu MCP špecifikáciu 2025-11-25 (uvedenú 25. novembra 2025)
  - Aktualizované všetky odkazy na verziu špecifikácie zo 2025-06-18 na 2025-11-25
  - Aktualizované dátumy v dokumente z 18. augusta 2025 na 18. decembra 2025
  - Overené, že všetky URL špecifikácie odkazujú na aktuálnu dokumentáciu
- **Validácia obsahu**: Komplexná validácia najlepších bezpečnostných praktík vzhľadom na najnovšie štandardy
  - **Microsoft Security Solutions**: Overená aktuálna terminológia a odkazy na Prompt Shields (predtým "detekcia rizika jailbreaku"), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 bezpečnosť**: Potvrdená zhoda s najnovšími bezpečnostnými praktikami OAuth
  - **OWASP štandardy**: Overené, že odkazy na OWASP Top 10 pre LLM zostávajú aktuálne
  - **Azure služby**: Overené všetky odkazy na dokumentáciu Microsoft Azure a najlepšie praktiky
- **Zladenie so štandardmi**: Všetky referencované bezpečnostné štandardy potvrdené ako aktuálne
  - NIST Rámec pre správu rizík AI
  - ISO 27001:2022
  - Najlepšie bezpečnostné praktiky OAuth 2.1
  - Bezpečnostné a súladové rámce Azure
- **Zdroje implementácie**: Overené všetky odkazy na implementačné príručky a zdroje
  - Vzory autentifikácie pre Azure API Management
  - Príručky integrácie Microsoft Entra ID
  - Správa tajomstiev Azure Key Vault
  - DevSecOps pipeline a monitorovacie riešenia

### Kontrola kvality dokumentácie
- **Zladenie so špecifikáciou**: Zabezpečené, že všetky povinné bezpečnostné požiadavky MCP (MUST/MUST NOT) zodpovedajú najnovšej špecifikácii
- **Aktuálnosť zdrojov**: Overené všetky externé odkazy na Microsoft dokumentáciu, bezpečnostné štandardy a príručky implementácie
- **Pokrytie najlepších praktík**: Potvrdené komplexné pokrytie autentifikácie, autorizácie, špecifických hrozieb AI, bezpečnosti dodávateľského reťazca a podnikových vzorov

## 6. október 2025

### Rozšírenie sekcie Začíname – Pokročilé používanie servera & Jednoduchá autentifikácia

#### Pokročilé používanie servera (03-GettingStarted/10-advanced)
- **Pridaná nová kapitola**: Predstavený komplexný sprievodca pokročilým používaním MCP servera, pokrývajúci bežné a nízkoúrovňové architektúry servera.
  - **Bežný vs. nízkoúrovňový server**: Podrobná komparácia a príklady kódu v Pythone a TypeScripte pre oba prístupy.
  - **Handler-based dizajn**: Vysvetlenie správy nástrojov/zdrojov/promptov založenej na handleroch pre škálovateľné a flexibilné implementácie servera.
  - **Praktické vzory**: Reálne scenáre, v ktorých sú nízkoúrovňové vzory servera výhodné pre pokročilé funkcie a architektúru.

#### Jednoduchá autentifikácia (03-GettingStarted/11-simple-auth)
- **Pridaná nová kapitola**: Krok za krokom sprievodca implementáciou jednoduchej autentifikácie v MCP serveroch.
  - **Koncepty autentifikácie**: Jasné vysvetlenie rozdielu medzi autentifikáciou a autorizáciou a správy poverení.
  - **Implementácia základnej autentifikácie**: Vzory autentifikácie založené na middleware v Pythone (Starlette) a TypeScripte (Express) s ukážkami kódu.
  - **Pokrok k pokročilej bezpečnosti**: Návod začať s jednoduchou auth a rozvíjať na OAuth 2.1 a RBAC s odkazmi na pokročilé bezpečnostné moduly.

Tieto doplnky poskytujú praktické, prakticky orientované usmernenie na budovanie robustnejších, bezpečnejších a flexibilnejších implementácií MCP serverov, ktoré prepájajú základné koncepty s pokročilými produkčnými vzormi.

## 29. september 2025

### MCP Server Database Integration Labs - Kompletná praktická vzdelávacia cesta

#### 11-MCPServerHandsOnLabs - Nová kompletná osnovná databázová integrácia
- **Komplexná 13-laboratórna vzdelávacia cesta**: Pridaná komplexná praktická osnova na budovanie produkčne pripravených MCP serverov s integráciou PostgreSQL databázy
  - **Praktická implementácia**: Use case Zava Retail analytiky demonštrujúci podnikové vzory
  - **Štruktúrovaná výučba**:
    - **Labs 00-03: Základy** - Úvod, základná architektúra, bezpečnosť a multi-tenancita, nastavenie prostredia
    - **Labs 04-06: Budovanie MCP servera** - Návrh databázy a schéma, implementácia MCP servera, vývoj nástrojov  
    - **Labs 07-09: Pokročilé funkcie** - Integrácia sámantického vyhľadávania, testovanie a ladenie, VS Code integrácia
    - **Labs 10-12: Produkcia & najlepšie praktiky** - Stratégie nasadenia, monitorovanie a pozorovateľnosť, najlepšie praktiky a optimalizácia
  - **Podnikové technológie**: FastMCP framework, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Pokročilé funkcie**: Row Level Security (RLS), sémantické vyhľadávanie, multi-tenantný prístup k dátam, vektorové embeddings, monitorovanie v reálnom čase

#### Štandardizácia terminológie - konverzia modulov na laby
- **Komplexná aktualizácia dokumentácie**: Systematicky aktualizované všetky README súbory v 11-MCPServerHandsOnLabs na používanie terminológie "Lab" namiesto "Modul"
  - **Nadpisy sekcií**: Aktualizované "Čo tento modul obsahuje" na "Čo tento lab obsahuje" vo všetkých 13 laboratóriách
  - **Popis obsahu**: Zmenené "Tento modul poskytuje..." na "Tento lab poskytuje..." v celej dokumentácii
  - **Vzdelávacie ciele**: Aktualizované "Na konci tohto modulu..." na "Na konci tohto labu..."
  - **Navigačné odkazy**: Konvertované všetky odkazy "Modul XX:" na "Lab XX:" v priechodoch a navigáciách
  - **Sledovanie dokončenia**: Aktualizované "Po dokončení tohto modulu..." na "Po dokončení tohto labu..."
  - **Zachované technické odkazy**: Zachované odkazy na Python moduly vo konfiguračných súboroch (napr. `"module": "mcp_server.main"`)

#### Vylepšenie študijného sprievodcu (study_guide.md)
- **Vizuálna mapa osnovy**: Pridaná nová sekcia "11. Database Integration Labs" s komplexnou vizualizáciou štruktúry labov
- **Štruktúra repozitára**: Aktualizovaná z desiatich na jedenásť hlavných sekcií so detailným popisom 11-MCPServerHandsOnLabs
- **Navigačné usmernenie**: Vylepšené navigačné pokyny pokrývajúce sekcie 00-11
- **Pokrytie technológií**: Pridané detaily integrácie FastMCP, PostgreSQL, Azure služieb
- **Výsledky štúdia**: Zdôraznený vývoj produkčne pripravených serverov, vzory integrácie databáz a podniková bezpečnosť

#### Vylepšenie hlavnej štruktúry README
- **Terminológia založená na laboch**: Aktualizovaný hlavný README.md v 11-MCPServerHandsOnLabs na konzistentné používanie štruktúry "Lab"
- **Organizácia vzdelávacej cesty**: Jasný postup od základných konceptov cez pokročilú implementáciu až po produkčné nasadenie
- **Zameranie na prax**: Dôraz na praktické, praktické učenie s podnikovo orientovanými vzormi a technológiami

### Zlepšenia kvality a konzistencie dokumentácie
- **Dôraz na prax**: Posilnený praktický prístup založený na laboch v celej dokumentácii
- **Zameranie na podnikové vzory**: Zdôraznené produkčne pripravené implementácie a podnikové bezpečnostné úvahy
- **Integrácia technológií**: Komplexné pokrytie moderných Azure služieb a vzorov AI integrácie
- **Postup výučby**: Jasná, štruktúrovaná cesta od základných konceptov k produkčnému nasadeniu

## 26. september 2025

### Rozšírenie prípadových štúdií - Integrácia GitHub MCP Registry

#### Prípadové štúdie (09-CaseStudy/) - Zameranie na rozvoj ekosystému
- **README.md**: Významné rozšírenie s komplexnou prípadovou štúdiou GitHub MCP Registry
  - **GitHub MCP Registry Prípadová štúdia**: Nová komplexná štúdia skúmajúca spustenie GitHub MCP Registry v septembri 2025
    - **Analýza problému**: Podrobná analýza fragmentácie discovery a deploy MCP serverov
    - **Architektúra riešenia**: Centralizovaný registr GitHub s inštaláciou VS Code na jedno kliknutie
    - **Obchodný dopad**: Merateľné zlepšenie onboardingu vývojárov a produktivity
    - **Strategická hodnota**: Zameranie na modulárne nasadenie agentov a interoperabilitu medzi nástrojmi
    - **Rozvoj ekosystému**: Pozicionovanie ako základná platforma pre agentickú integráciu
  - **Vylepšená štruktúra prípadovej štúdie**: Aktualizované všetkých sedem prípadových štúdií s konzistentným formátovaním a komplexnými popismi
    - Azure AI Travel Agents: Dôraz na viacerých agentov a ich orchestráciu
    - Azure DevOps integrácia: Zameranie na automatizáciu pracovných tokov
    - Real-Time Documentation Retrieval: Implementácia Python konzolového klienta
    - Interactive Study Plan Generator: Chainlit konverzačná webová aplikácia
    - Dokumentácia v editore: Integrácia VS Code a GitHub Copilot
    - Azure API Management: Podnikové vzory API integrácie
    - GitHub MCP Registry: Rozvoj ekosystémovej a komunitnej platformy
  - **Komplexný záver**: Prepracovaná záverečná sekcia zdôrazňujúca sedem prípadových štúdií pokrývajúcich viaceré dimenzie implementácie MCP
    - Podniková integrácia, viac-agentová orchestrácia, produktivita vývojárov
    - Rozvoj ekosystému, klasifikácia vzdelávacích aplikácií
    - Vylepšený pohľad na architektonické vzory, stratégie implementácie a najlepšie praktiky
    - Dôraz na MCP ako zrelý, produkčne pripravený protokol

#### Aktualizácie študijného sprievodcu (study_guide.md)
- **Vizuálna mapa osnovy**: Aktualizovaný myšlienkový map s pridaním GitHub MCP Registry v sekcii Prípadové štúdie
- **Popis prípadových štúdií**: Vylepšený z generických opisov na podrobný rozpis siedmich komplexných prípadových štúdií
- **Štruktúra repozitára**: Aktualizovaná sekcia 10 reflektujúca komplexné pokrytie prípadových štúdií so špecifickými implementačnými detailmi
- **Integrácia changelogu**: Pridaný záznam z 26. septembra 2025 dokumentujúci pridanie GitHub MCP Registry a rozšírenia prípadových štúdií
- **Aktualizácia dátumu**: Aktualizovaný časový údaj v päte dokumentu pre odraz najnovšej revízie (26. september 2025)

### Zlepšenia kvality dokumentácie
- **Zlepšenie konzistencie**: Štandardizované formátovanie a štruktúra prípadových štúdií vo všetkých siedmich príkladoch
- **Komplexné pokrytie**: Prípadové štúdie teraz pokrývajú scenáre podnikovej, vývojárskej produktivity a rozvoja ekosystému
- **Strategické pozicionovanie**: Zdôraznený MCP ako základná platforma pre nasadenie agentických systémov
- **Integrácia zdrojov**: Aktualizované ďalšie zdroje o zahrnutie odkazu GitHub MCP Registry

## 15. september 2025

### Rozšírenie pokročilých tém - Vlastné transporty & Context Engineering

#### Vlastné MCP transporty (05-AdvancedTopics/mcp-transport/) - Nový sprievodca pokročilou implementáciou
- **README.md**: Kompletný sprievodca implementáciou vlastných MCP transportných mechanizmov
  - **Azure Event Grid Transport**: Komplexná implementácia serverless event-driven transportu
    - Príklady v C#, TypeScript a Pythone s integráciou Azure Functions
    - Vzory event-driven architektúry pre škálovateľné MCP riešenia
    - Príjemcovia webhookov a spracovanie správ založených na push notifikáciách
  - **Azure Event Hubs Transport**: Implementácia high-throughput streaming transportu
    - Real-time streaming schopnosti pre nízku latenciu
    - Stratégie partií a správa checkpointov
    - Zhlukovanie správ a optimalizácia výkonu
  - **Podnikové integračné vzory**: Produkčne pripravené príklady architektúr
    - Distribuované MCP spracovanie cez viacero Azure Functions
    - Hybridné transportné architektúry kombinujúce viacero typov transportu
    - Trvácnosť správ, spoľahlivosť a stratégie spracovania chýb
  - **Bezpečnosť a monitorovanie**: Integrácia Azure Key Vault a vzory pozorovateľnosti
    - Autentifikácia spravovanou identitou a princíp najmenšieho oprávnenia
    - Telemetria a monitorovanie výkonu Application Insights
    - Circuit breakers a vzory odolnosti voči chybám
  - **Testovacie rámce**: Komplexné testovacie stratégie pre vlastné transporty
    - Jednotkové testovanie s testovacími dvojitkami a mocking rámcami
    - Integračné testovanie s Azure Test Containers
    - Úvahy o výkone a záťaži počas testovania

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Nová disciplína AI
- **README.md**: Komplexná explorácia context engineering ako vyvíjajúcej sa oblasti
  - **Základné princípy**: Kompletné zdieľanie kontextu, vedomosť rozhodovania o akciách a správa kontextového okna

  - **Zladenie protokolu MCP**: Ako dizajn MCP rieši výzvy kontextového inžinierstva
    - Obmedzenia okna kontextu a stratégie postupného načítania
    - Určovanie relevantnosti a dynamický výber kontextu
    - Spracovanie multimodálneho kontextu a bezpečnostné úvahy
  - **Prístupy k implementácii**: Jednovláknové vs. viacagentové architektúry
    - Techniky delenia a priorizácie kontextuálnych blokov
    - Stratégie postupného načítania a kompresie kontextu
    - Viacvrstvové prístupy ku kontextu a optimalizácia získavania
  - **Meračský rámec**: Nové metriky na hodnotenie efektívnosti kontextu
    - Úvahy o efektívnosti vstupu, výkonnosti, kvalite a používateľskom zážitku
    - Experimentálne prístupy k optimalizácii kontextu
    - Analýza neúspechov a metodiky zlepšovania

#### Aktualizácie navigácie kurikula (README.md)
- **Vylepšená štruktúra modulu**: Aktualizovaná tabuľka kurikula obsahujúca nové pokročilé témy
  - Pridané položky Context Engineering (5.14) a Custom Transport (5.15)
  - Konzistentné formátovanie a navigačné odkazy vo všetkých moduloch
  - Aktualizované popisy odrážajúce aktuálny rozsah obsahu

### Vylepšenia štruktúry adresárov
- **Štandardizácia názvov**: Premenované "mcp transport" na "mcp-transport" pre konzistentnosť s inými zložkami pokročilých tém
- **Organizácia obsahu**: Všetky priečinky 05-AdvancedTopics teraz používajú jednotný vzor názvov (mcp-[topic])

### Vylepšenia kvality dokumentácie
- **Zladenie so špecifikáciou MCP**: Všetok nový obsah odkazuje na aktuálnu špecifikáciu MCP 2025-06-18
- **Príklady v rôznych jazykoch**: Komplexné ukážky kódu v C#, TypeScript a Pythone
- **Zameranie na podnikové prostredie**: Vzory pripravené na produkciu a integrácia s Azure cloudom naprieč dokumentáciou
- **Vizualizácia dokumentácie**: Mermaid diagramy pre architektúru a vizualizáciu tokov

## 18. august 2025

### Kompletná aktualizácia dokumentácie - štandardy MCP 2025-06-18

#### Najlepšie bezpečnostné postupy MCP (02-Security/) - Kompletná modernizácia
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Úplné prepísanie zosúladené s MCP špecifikáciou 2025-06-18
  - **Povinné požiadavky**: Pridané explicitné požiadavky MUSÍ/MUSÍ NE, podľa oficiálnej špecifikácie s jasnými vizuálnymi indikátormi
  - **12 základných bezpečnostných praktík**: Reštrukturalizované z 15-položkového zoznamu na komplexné bezpečnostné domény
    - Bezpečnosť tokenov a autentifikácia s integráciou externého poskytovateľa identity
    - Správa relácií a bezpečnosť prenosu s kryptografickými požiadavkami
    - Ochrana špecifická pre AI s integráciou Microsoft Prompt Shields
    - Kontrola prístupu a povolenia s princípom minimálnych oprávnení
    - Bezpečnosť obsahu a monitorovanie s integráciou Azure Content Safety
    - Bezpečnosť dodávateľského reťazca s komplexnou verifikáciou komponentov
    - Bezpečnosť OAuth a prevencia útokov confused deputy s implementáciou PKCE
    - Reakcia na incidenty a obnova s automatizovanými schopnosťami
    - Súlad a správa s legislatívnym zaradením
    - Pokročilá bezpečnostná kontrola s architektúrou nulovej dôvery
    - Integrácia v Microsoft bezpečnostnom ekosystéme s komplexnými riešeniami
    - Neustály vývoj bezpečnosti s adaptívnymi praktikami
  - **Microsoft bezpečnostné riešenia**: Vylepšené návody na integráciu Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security
  - **Implementačné zdroje**: Kategorizované komplexné odkazy na zdroje podľa Oficiálnej dokumentácie MCP, Microsoft bezpečnostných riešení, bezpečnostných štandardov a implementačných príručiek

#### Pokročilé bezpečnostné kontroly (02-Security/) - Podniková implementácia
- **MCP-SECURITY-CONTROLS-2025.md**: Úplný prepracovaný podnikový bezpečnostný rámec
  - **9 komplexných bezpečnostných domén**: Rozšírené z základných kontrol na podrobný podnikový rámec
    - Pokročilá autentifikácia a autorizácia s integráciou Microsoft Entra ID
    - Bezpečnosť tokenov a kontroly proti presmerovaniu s komplexnou validáciou
    - Kontroly bezpečnosti relácií s prevenciou unesenia
    - AI-špecifické bezpečnostné kontroly s prevenciou vloženia promptov a otrávených nástrojov
    - Prevencia útokov confused deputy s OAuth proxy bezpečnosťou
    - Bezpečnosť vykonávania nástrojov s pieskoviskom a izoláciou
    - Kontroly bezpečnosti dodávateľského reťazca s overovaním závislostí
    - Kontroly monitorovania a detekcie s integráciou SIEM
    - Reakcia na incidenty a obnova s automatizovanými schopnosťami
  - **Implementačné príklady**: Pridané podrobné YAML konfiguračné bloky a príklady kódu
  - **Integrácia Microsoft riešení**: Komplexné pokrytie služieb Azure bezpečnosti, GitHub Advanced Security a podnikovej správy identity

#### Bezpečnosť pokročilých tém (05-AdvancedTopics/mcp-security/) - Produkčne pripravená implementácia
- **README.md**: Kompletné prepísanie pre podnikové bezpečnostné implementácie
  - **Zladenie s aktuálnou špecifikáciou**: Aktualizované podľa MCP špecifikácie 2025-06-18 s povinnými bezpečnostnými požiadavkami
  - **Vylepšená autentifikácia**: Integrácia Microsoft Entra ID s komplexnými príkladmi v .NET a Java Spring Security
  - **AI bezpečnostná integrácia**: Implementácia Microsoft Prompt Shields a Azure Content Safety s podrobnými príkladmi v Pythone
  - **Pokročilá mitigácia hrozieb**: Komplexné implementačné príklady pre
    - Prevenciu útokov confused deputy s PKCE a validáciou súhlasu používateľa
    - Prevenciu token passthrough s validáciou publika a bezpečnou správou tokenov
    - Prevenciu unesenia relácie s kryptografickým viazaním a behaviorálnou analýzou
  - **Integrácia podnikovej bezpečnosti**: Monitorovanie Azure Application Insights, pipeline detekcie hrozieb a bezpečnosť dodávateľského reťazca
  - **Kontrolný zoznam implementácie**: Jasné označenie povinných vs. odporúčaných bezpečnostných kontrol s výhodami Microsoft bezpečnostného ekosystému

### Kvalita dokumentácie a zladenie so štandardmi
- **Odkazy na špecifikácie**: Aktualizované všetky odkazy na aktuálnu MCP špecifikáciu 2025-06-18
- **Microsoft bezpečnostný ekosystém**: Vylepšené návody na integráciu v celej bezpečnostnej dokumentácii
- **Praktická implementácia**: Pridané podrobné príklady kódu v .NET, Java a Python s podnikateľskými vzormi
- **Organizácia zdrojov**: Komplexná kategorizácia oficiálnej dokumentácie, bezpečnostných štandardov a implementačných príručiek
- **Vizualne indikátory**: Jasné označenie povinných požiadaviek vs. odporúčaných praktík


#### Základné koncepty (01-CoreConcepts/) - Kompletná modernizácia
- **Aktualizácia verzie protokolu**: Aktualizované odkazy na aktuálnu MCP špecifikáciu 2025-06-18 s verziou vo formáte YYYY-MM-DD
- **Vylepšenie architektúry**: Rozšírené popisy Hostiteľov, Klientov a Serverov pre zosúladenie s aktuálnymi vzormi MCP architektúr
  - Hostitelia sú teraz jasne definovaní ako AI aplikácie koordinujúce viacnásobné klientské pripojenia MCP
  - Klienti popísaní ako protokolové konektory udržiavajúce vzťah jeden-na-jedného so serverom
  - Servery rozšírené o scenáre lokálneho a vzdialeného nasadenia
- **Reštrukturalizácia primitív**: Kompletné prepracovanie serverových a klientske primitív
  - Serverové primitíva: Zdroje (zdroje dát), Prompty (šablóny), Nástroje (vykonávateľné funkcie) s detailnými vysvetleniami a príkladmi
  - Klientské primitíva: Sampling (dokončenia LLM), Elicitation (vstup používateľa), Logging (ladenie/monitorovanie)
  - Aktualizované s aktuálnymi vzormi metód objavovania (`*/list`), získavania (`*/get`) a vykonávania (`*/call`)
- **Architektúra protokolu**: Zavedený model architektúry so dvoma vrstvami
  - Dátová vrstva: Základ JSON-RPC 2.0 s manažmentom životného cyklu a primitívami
  - Transportná vrstva: STDIO (lokálny) a Streamable HTTP s SSE (vzdialený) transportné mechanizmy
- **Bezpečnostný rámec**: Komplexné bezpečnostné princípy vrátane explicitného súhlasu používateľa, ochrany dátového súkromia, bezpečného vykonávania nástrojov a bezpečnosti transportnej vrstvy
- **Komunikačné vzory**: Aktualizované protokolové správy zobrazujúce inicializáciu, objavovanie, vykonávanie a notifikačné toky
- **Príklady kódu**: Obnovené príklady v rôznych jazykoch (.NET, Java, Python, JavaScript) reflektujúce aktuálne vzory SDK MCP

#### Bezpečnosť (02-Security/) - Komplexné prepracovanie bezpečnosti  
- **Zladenie so štandardmi**: Plné zosúladenie s bezpečnostnými požiadavkami MCP špecifikácie 2025-06-18
- **Evolúcia autentifikácie**: Zdokumentovaná evolúcia od vlastných OAuth serverov k delegácii externého poskytovateľa identity (Microsoft Entra ID)
- **Analýza hrozieb špecifických pre AI**: Rozšírené pokrytie moderných útokov na AI
  - Detailné scenáre útokov typu prompt injection s reálnymi príkladmi
  - Mechanizmy otrávenia nástrojov a vzory útokov "rug pull"
  - Otrávenie okna kontextu a útoky zameniteľnosti modelu
- **Microsoft AI bezpečnostné riešenia**: Komplexné pokrytie Microsoft bezpečnostného ekosystému
  - AI Prompt Shields s pokročilou detekciou, zdôrazňovaním a technikami delimitácie
  - Vzory integrácie Azure Content Safety
  - GitHub Advanced Security pre ochranu dodávateľského reťazca
- **Pokročilá mitigácia hrozieb**: Detailné bezpečnostné kontroly pre
  - Unesenie relácie s MCP-špecifickými scenármi a kryptografickými požiadavkami na ID relácie
  - Problémy confused deputy v MCP proxy scenároch s explicitnými požiadavkami na súhlas
  - Zraniteľnosti token passthrough s povinnými validačnými kontrolami
- **Bezpečnosť dodávateľského reťazca**: Rozšírené pokrytie AI dodávateľského reťazca vrátane základných modelov, embedding služieb, poskytovateľov kontextu a API tretích strán
- **Základná bezpečnosť**: Vylepšená integrácia s podnikateľskými bezpečnostnými vzormi vrátane architektúry nulovej dôvery a Microsoft bezpečnostného ekosystému
- **Organizácia zdrojov**: Kategorizované komplexné odkazy na zdroje podľa typu (Oficiálna dokumentácia, štandardy, výskum, Microsoft riešenia, implementačné príručky)

### Vylepšenia kvality dokumentácie
- **Štruktúrované vzdelávacie ciele**: Vylepšené vzdelávacie ciele so špecifickými, akčnými výsledkami 
- **Krížové odkazy**: Pridané odkazy medzi súvisiacimi bezpečnostnými a základnými témami
- **Aktuálne informácie**: Aktualizované všetky dátumové odkazy a odkazy na špecifikácie podľa aktuálnych štandardov
- **Návody na implementáciu**: Pridané špecifické, akčné implementačné usmernenia v oboch sekciách

## 16. júl 2025

### Vylepšenia README a navigácie
- Kompletná prepracovaná navigácia kurikula v README.md
- Nahradené značky `<details>` prístupnejším formátom založeným na tabuľkách
- Vytvorené alternatívne rozloženia v novom priečinku "alternative_layouts"
- Pridané príklady navigácií na báze kariet, záložiek a akordeónu
- Aktualizovaná sekcia štruktúry repozitára, ktorá obsahuje všetky najnovšie súbory
- Vylepšená sekcia "Ako používať toto kurikulum" s jasnými odporúčaniami
- Aktualizované odkazy na MCP špecifikácie ukazujúce na správne URL
- Pridaná sekcia Context Engineering (5.14) do štruktúry kurikula

### Aktualizácie študijného sprievodcu
- Kompletné prepracovanie študijného sprievodcu na zosúladenie s aktuálnou štruktúrou repozitára
- Pridané nové sekcie pre MCP klientov a nástroje a populárne MCP servery
- Aktualizovaná vizuálna mapa kurikula pre presné zobrazenie všetkých tém
- Vylepšené popisy pokročilých tém zahŕňajúce všetky špecializované oblasti
- Aktualizovaná sekcia prípadových štúdií reflektujúca reálne príklady
- Pridaný tento komplexný zoznam zmien

### Príspevky komunity (06-CommunityContributions/)
- Pridané podrobné informácie o MCP serveroch pre generovanie obrázkov
- Pridaná komplexná sekcia o používaní Clauda vo VSCode
- Pridaná inštalácia a pokyny na použitie terminálového klienta Cline
- Aktualizovaná sekcia MCP klient zohľadňujúca všetky populárne klientské možnosti
- Vylepšené príklady príspevkov presnejšími ukážkami kódu

### Pokročilé témy (05-AdvancedTopics/)
- Zorganizované všetky špecializované témy so jednotným pomenovaním
- Pridané materiály a príklady kontextového inžinierstva
- Pridaná dokumentácia o integrácii agenta Foundry
- Vylepšená dokumentácia o integrácii bezpečnosti Entra ID

## 11. jún 2025

### Počiatočné vytvorenie
- Vydaná prvá verzia kurikula MCP pre začiatočníkov
- Vytvorená základná štruktúra pre všetkých 10 hlavných sekcií
- Implementovaná vizuálna mapa kurikula pre navigáciu
- Pridané počiatočné ukážkové projekty v rôznych programovacích jazykoch

### Začiatok práce (03-GettingStarted/)
- Vytvorené prvé príklady implementácie servera
- Pridané návody pre vývoj klienta
- Zahrnuté inštrukcie pre integráciu LLM klienta
- Pridaná dokumentácia integrácie VS Code
- Implementované príklady serverov posielajúcich udalosti (SSE)

### Základné koncepty (01-CoreConcepts/)
- Pridané detailné vysvetlenie architektúry klient-server
- Vytvorená dokumentácia kľúčových komponentov protokolu
- Zdokumentované komunikačné vzory v MCP

## 23. máj 2025

### Štruktúra repozitára
- Inicializovaný repozitár so základnou štruktúrou priečinkov
- Vytvorené README súbory pre každú hlavnú sekciu
- Nastavená prekladateľská infraštruktúra
- Pridané obrázky a diagramy

### Dokumentácia
- Vytvorený počiatočný README.md s prehľadom kurikula
- Pridané súbory CODE_OF_CONDUCT.md a SECURITY.md
- Nastavený SUPPORT.md s návodmi ako získať pomoc
- Vytvorená predbežná štruktúra študijného sprievodcu

## 15. apríl 2025

### Plánovanie a rámec
- Počiatočné plánovanie kurikula MCP pre začiatočníkov
- Definované vzdelávacie ciele a cieľová skupina
- Načrtnutá štruktúra kurikula s 10 sekciami
- Vyvinutý konceptuálny rámec pre príklady a prípadové štúdie
- Vytvorené počiatočné prototypové príklady kľúčových konceptov

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->