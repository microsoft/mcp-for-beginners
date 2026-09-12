# Zoznam zmien: MCP pre Začiatočníkov Kurikulum

Tento dokument slúži ako záznam všetkých významných zmien vykonaných v kurikule Model Context Protocol (MCP) pre začiatočníkov. Zmeny sú zaznamenané v reverznom chronologickom poradí (najnovšie zmeny ako prvé).

## 9. september 2026

### Zarovnanie finálnej špecifikácie MCP 2026-07-28

Aktualizované anglické kurikulum z kandidátskej verzie a `2025-11-25`
základného návodu na finálnu MCP špecifikáciu `2026-07-28`.

- **Aktualizované**: Referencie na aktuálnu verziu, odkazy na špecifikácie, prevedenie bezstavových
  požiadaviek, `server/discover`, Streamovateľné HTTP hlavičky a životný cyklus rozšírenia Tasks
  vo 38 anglických dokumentačných súboroch.
- **Opravené**: Elicitácia teraz používa `elicitation/create`, Sampling používa
  `sampling/createMessage`, a `InputRequiredResult.resultType` používa
  `"input_required"`.
- **Nahradené**: Nepresná lekcia o stave rozhovoru Root Context bola nahradená
  lekciou presnou podľa protokolu o Rootse, pokrývajúcou informačné tipy na súborový systém,
  aktuálny viackolový tok, bezpečnostné hranice a možnosti migrácie.
- **Vysvetlené**: Roots, Sampling, Logging a Dynamická registrácia klienta sú
  označené ako zastarané v `2026-07-28`, s odporúčanými náhradami a
  dokumentovaným najskorším dátumom odstránenia.
- **Označené**: Ukážky, ktoré stále závisia od MCP `2025-11-25`, HTTP+SSE,
  inicializačných handshake alebo protokolových relácií sa ponechávajú ako príklady staršej
  kompatibility namiesto prezentovania ako aktuálne implementácie.
- **Bezpečnostné odporúčania**: Aktualizované samostatné bezpečnostné príručky na použitie
  autorizácie na úrovni požiadavky a explicitných rukovätí stavov aplikácie namiesto
  odstránených ID relácií protokolu. Dokumenty metadát Client ID sú teraz
  preferovanou cestou registrácie, pričom DCR je zdokumentované ako kompatibilita len.
- **Podporný materiál**: Aktualizovaný študijný sprievodca, kontrolný zoznam prispievateľov,
  prípadová štúdia Publory a prípadová štúdia APIM. Prechádzka APIM teraz odporúča
  svoj súčasný Streamable HTTP `/mcp` endpoint namiesto zastaraného `/sse`.
- **Kanonické odkazy**: Nahradené vyradené a návrhové URL špecifikácií v anglických
  zdrojových Markdown odkazoch verziami `2026-07-28`, pričom explicitné
  odkazy na staršie verzie sú zachované tam, kde je ukážka stále viazaná na staršie nástroje.
- **Stabilné názvy súborov**: Premenovaná finálna príručka špecifikácie a dve bezpečnostné
  príručky na odstránenie prípon kandidátskych verzií a rokov, potom aktualizované všetky anglické
  hypertextové odkazy na ich stabilné cesty.
- **Nová ukážka autorizácie**: Pridaný testovaný
  [TypeScript MCP `2026-07-28` resource server](./02-Security/samples/cimd-dcr-auth/README.md)
  ktorý porovnáva preferované dokumenty metadát Client ID s zastaranou dynamickou
  registráciou klienta ako záložnou možnosťou. Ukážka obsahuje objavovanie podľa RFC 9728, validáciu JWKS,
  rozsahy podľa nástroja, dvanásť testov a sprievodcu nastavením Auth0.
- **Rozsah prekladu**: Iba anglické zdrojové súbory boli upravené; generované
  preklady a preložené obrázky zostávajú nezmenené, pretože sú automaticky prekladané.

## 29. júl 2026

### Nový modul 08 sprievodca: Spoľahlivé sidecary a bezpečné opakovania

Pridaná neutrálnym dodávateľom sprievodná lekcia pre MCP nástroje vytvárajúce reálne
účinky, zosúladená s finálnou špecifikáciou `2026-07-28`.

- **Nové**: [sprievodná lekcia spoľahlivostného sidecaru][reliability-sidecar]
  používa jeden príbeh o podpore ticketov, dva Mermaid diagramy a rozhodovací
  tok opakovania na vysvetlenie stabilných kľúčov operácií, atómovej duplicitnej akceptácie,
  zladenia, dôkazov a hranice rozšírenia Tasks.
- **Nové**: Cvičenie s injekciou zlyhaní v štandardnej Python knižnici a SQLite
  používa samostatné obchodíky operácií a ticketov na demonštráciu straty odpovede
  po potvrdení externého efektu. Šesť deterministických testov pokrýva naivnú
  duplicitu, stráženú obnovu restartu, konflikty užitočného zaťaženia, uložené výsledky,
  aktívne nároky a súbežnú duplicitnú akceptáciu.
- **Aktualizované**: Modul 08 teraz obsahuje odkaz na sprievodnú lekciu, identifikuje
  finálny model bezstavovej požiadavky `2026-07-28`, rozlišuje OpenTelemetry
  sledovanie od zastaranej funkcie MCP logovania a obmedzuje jeho
  všeobecný príklad opakovania na operácie iba na čítanie.
- **Voliteľné**: Lekcia mapuje svoje prenosné koncepty na jednu označenú komunitnú
  implementáciu bez toho, aby bola hostovaná služba alebo sieťové volanie súčasťou
  cvičenia.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. júl 2026

### Nová lekcia: Kandidát finálnej špecifikácie MCP 2026-07-28

Pridané pokrytie nadchádzajúceho kandidáta finálnej špecifikácie MCP `2026-07-28` (oznámené 21. mája 2026; finálne vydanie plánované na 28. júla 2026), zhrnuté z [oficiálneho blogového oznámenia](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Základ kurikula zostáva **MCP Specification 2025-11-25** až do vydania novej verzie, takže je to prezentované ako výhľadové odporúčanie, nie ako prepísanie existujúcich lekcií.

- **Nové**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — úplná lekcia pokrývajúca bezstavové jadro protokolu (odstránenie handshake `initialize` a `Mcp-Session-Id`), nové smerovacie hlavičky `Mcp-Method`/`Mcp-Name`, metadata ukladaní do medzipamäte `ttlMs`/`cacheScope`, W3C Trace Context v `_meta`, formálny rámec rozšírení (MCP Apps a nové rozšírenie Tasks), šesť SEPs na spevnenie autorizácie, zastaranie Roots/Sampling/Logging a prechod na plnú schému JSON Schema 2020-12 pre nástrojové schémy.
- **Aktualizované** s výhľadovými upozorneniami s odkazmi na novú lekciu:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): poznámka o verzii protokolu, sekcie Sampling/Roots/Logging/Tasks, a „Čo bude ďalej“
  - [02-Security/README.md](./02-Security/README.md): upozornenie na spevnenie autorizácie
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): upozornenie na bezstavnú dopravu
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): upozornenie na zastaranie Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): upozornenie na zastaranie Logging a rozšírenia Tasks

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): výzva na stateless/session-routing
  - [README.md](./README.md): poznámka „Pozrite sa dopredu“ v časti špecifikácie a nová položka `1.1` v tabuľke modulu kurikula
  - [study_guide.md](./study_guide.md): výhľadový bod v prehľade základných konceptov a datovaná dodatková poznámka
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): upozornenie na mapu prenosu `mcp-session-id` pred modelom stateless požiadavky
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): upozornenie v prehľade modulu o zastarnutí Root Contexts/Sampling a rozšírení úloh
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): upozornenie na spevnenie autorizácie

## 24. júna 2026

### Nová lekcia: Použitie MCP v aplikácii Copilot

- [Sekcia nástrojov](./12-tooling/README.md) Pridaná sekcia nástrojov.
- [MCP v aplikácii Copilot](./12-tooling/01-copilot-app/README.md)

## 16. júna 2026

### Zladenie špecifikácie MCP a validácia ukážok

Overili sme kurikulum podľa aktuálnej **MCP špecifikácie 2025-11-25** a najnovších oficiálnych SDK, potom sme opravili zostávajúce neaktuálne odkazy vo špecifikácii a potvrdili, že jadrové ukážky sa stále zostavujú a spúšťajú.

#### Opravy verzie špecifikácie (2025-06-18 / 2025-03-26 → 2025-11-25)

Aktualizovali sme anglický obsah tam, kde sa stále tvrdilo, že staršia revízia špecifikácie je *aktuálnym/najnovším* štandardom, a prešli sme na kanonické cesty k špecifikáciám na `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Aktualizovali sme banner „Current Standard“, úvod, nadpisy jadrových bezpečnostných princípov, povinných požiadaviek, sekciu Microsoft Entra ID, odkazy na Referential & Resources a záverečné bezpečnostné upozornenie (8 odkazov) na 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Aktualizovali sme odkaz na špecifikáciu dodatočných zdrojov a banner „Current Standard“ na 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Nahradili sme zastaraný odkaz `2025-03-26` na bezpečnosť a dôveru aktuálnou stránkou o najlepších bezpečnostných praktikách z 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Aktualizovali sme odkaz na oficiálnu dokumentáciu vzorkovania na 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Aktualizovali sme odkaz na súčasnú, prítomnou časť „aktuálnej MCP špecifikácie“ a odkaz na dodatočné zdroje na 2025-11-25 (historické poznámky o zastaraní SSE ponechané pre presnosť)

#### Validácia ukážok voči aktuálnym SDK

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` úspešne vyriešil `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` prešlo bez typových chýb — existujúce API `McpServer`/`StdioServerTransport` sú stále platné
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validované v izolovanom prostredí `.venv` s `mcp[cli]` (1.27.2); `py_compile` prešlo a `FastMCP.list_tools()` správne vrátil nástroje `add` a `subtract`
- Potvrdili sme, že všetky verziové rozsahy `@modelcontextprotocol/sdk` vo vzorkách (`>=1.26.0` / `^1.26.0` / `^1.27.0`) sa hladko vyriešia na aktuálnu `1.29.0` bez prerušenia API

#### Zladenie závislostí verzií (uzavretie medzier vo verziách)

Zvýšili sme zastarané SDK závislosti, aby každá ukážka sledovala aktuálne vydanie MCP, podľa konvencie celého repozitára:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Zvýšenie `@modelcontextprotocol/sdk` z `^1.8.0` → `>=1.26.0` a aktualizácia zastaraného popisu balíka „updated for MCP 2025-06-18“ na „aligned with MCP Specification 2025-11-25“
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** a **lab4/code/github_mcp_server/pyproject.toml**: Zvýšenie presnej verzie `mcp==1.23.0` → `mcp>=1.26.0`; regenerované zámkové súbory `uv.lock` (`uv lock`), aby sa zámky vyriešili na aktuálnu verziu `mcp 1.27.2` a boli synchronizované s manifestami

#### Analýza medzier v kurikule — Krytie najnovších funkcií špecifikácie

Overili sme, že kurikulum už pokrýva všetky primitivá zavedené/rozšírené v MCP 2025-11-25, takže žiadne obsahové medzery nezostávajú:
- **Sampling (vzorkovanie)**: Lekcia 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (vrátane režimu URL)**: Dokumentované v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Roots (koreňové kontexty)**: Dokumentované v 00-Introduction, 01-CoreConcepts a 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentálne, dlhodobé operácie)**: Dokumentované v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Anotácie nástrojov** (`readOnlyHint` / `destructiveHint`): Dokumentované v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features

### Spevnenie bezpečnosti & odstránenie zraniteľností v závislostiach

Prešiel som kompletne bezpečnostnú kontrolu každého manifestu závislostí a zdrojového kódu ukážok, potom som opravil všetky hlásené npm varovania a jednu zistenú chybu na úrovni kódu. Po oprave `npm audit` hlási **0 zraniteľností** v každom kontrolovanom adresári.

#### Zraniteľnosti závislostí npm (prenesené) — Opravené

Kontrolovali sme všetkých 15 potvrdených súborov `package-lock.json`. Zraniteľnosti boli limitované na prenesené závislosti vyvolané vývojárskym nástrojom MCP Inspector, klientom OpenAI a MCP SDK; všetky sú teraz vyriešené bez prerušenia ukážok:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** a **lab3/code/weather_mcp/inspector**: Aktualizovaný `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), čo vyriešilo bezpečnostné upozornenia vo zabalených balíčkoch `ajv`, `brace-expansion`, `diff`, `path-to-regexp` a `ws`. Pridaný vstup npm `overrides` vynucujúci opravený balíček `shell-quote@1.8.4` na eliminovanie zostávajúceho kritického upozornenia neseného `concurrently`; pregenerované obe uzamykacie súbory balíčkov (teraz 0 zraniteľností)
- **03-GettingStarted/samples/typescript**: `npm audit fix` aktualizoval tranzitný balíček `qs` (mierna závažnosť) na opravenú verziu
- **03-GettingStarted/samples/javascript**: `npm audit fix` aktualizoval tranzitný balíček `hono` (mierna závažnosť) na opravenú verziu
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` aktualizoval tranzitný balíček `form-data` (vysoká závažnosť) na opravenú verziu
- **03-GettingStarted/11-simple-auth/solution/typescript**: Vygenerovaný chýbajúci súbor `package-lock.json`, tak aby projekt bol reprodukovateľný a auditovateľný (0 zraniteľností)

#### Oprava bezpečnosti na úrovni kódu (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Odstránené `shell=True` z nástroja `open_in_vscode`. Predchádzajúci `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` umožňoval, že shell metaznaky v ceste k priečinku boli interpretované `cmd.exe` (vektor injekcie príkazu). Teraz sa priamo spustí vyriešený `Code.exe` s priečinkom ako argumentom — žiadny shell — čo je funkčne ekvivalentné a bezpečné

#### Python Audit Závislostí

- Auditované všetky sady požiadaviek Python pomocou `pip-audit`. `05-AdvancedTopics` a `03-GettingStarted/samples/python` nehlásia **žiadne známe zraniteľnosti** (ich rozsahy `mcp` / `httpx` / `pydantic` / `python-dotenv` vedú k aktuálnym opravneným vydaniam)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` označil tranzitnú závislosť **`werkzeug` 3.1.1** s tromi upozorneniami DoS na Windows zariadenia `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, a `CVE-2026-27199` (všetky opravené v 3.1.6). Pridaný explicitný bezpečnostný pin `werkzeug>=3.1.6`, aby sa vyriešilo na opravené vydanie; overené, že obmedzenie sa čistým spôsobom vyrieši so stackom `chainlit` / `mcp` / `semantic-kernel`

### Prebranding Produktu

Aktualizovaný celý obsah kurikula tak, aby odrážal prebranding produktov Microsoftu:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Aktualizovaný odkaz na Discord komunitu
- **AGENTS.md**: Aktualizovaný odkaz na Discord server
- **README.md**: Aktualizované odkazy na technologický ekosystém
- **study_guide.md**: Aktualizované odkazy v prípadovej štúdii
- **05-AdvancedTopics/README.md**: Aktualizovaný názov a popis modulu 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Aktualizovaný nadpis sekcie a popis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Kompletná aktualizácia názvu a obsahu modulu
- **05-AdvancedTopics/mcp-security-entra/README.md**: Aktualizovaný odkazovanie
- **07-LessonsfromEarlyAdoption/README.md**: Aktualizované odkazy v prípadovej štúdii
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Aktualizovaný nadpis sekcie 9, odznaky a schopnosti
- **08-BestPractices/README.md**: Aktualizovaný odkaz na Discord komunitu
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Aktualizovaný odkaz na Discord kanál
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Aktualizovaný odkaz nasadenia modelu
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Aktualizovaná tabuľka AI služieb
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Aktualizované odkazy na zdroje

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension pre VS Code
- **README.md**: Aktualizované hlavné odkazy v kurikule
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Aktualizovaný názov modulu, prehľad a všetky nadpisy modulu
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Aktualizovaný názov, ciele učenia, inštrukcie nastavenia a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Aktualizovaný názov, ciele učenia, tabuľka MCP hostov a medziodkazy
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Aktualizovaný názov, odznaky, predpoklady a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Aktualizované odkazy Agent Buildera a odkaz na spätnú väzbu
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Aktualizované predpoklady a odkazy na rozšírenie

---

## 11. apríla 2026

### Nová lekcia, opravy dokumentácie a aktualizácie závislostí

#### Pridaný nový obsah kurikula

**Modul 05 - Pokročilé témy**
- **Lekcia 5.17: Adversariálne multi-agentné uvažovanie s MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nový komplexný sprievodca pokrývajúci vzor adversariálneho debaty pre multi-agentné systémy
  - Diagram architektúry Mermaid: dvaja agenti → zdieľaný MCP server → prepis debaty → sudca → verdikt
  - Zdieľaný MCP nástrojový server (`web_search` + `run_python`) implementovaný v Pythone a TypeScripte
  - Protichodné systémové výzvy (ZA / PROTI / Sudca) s explicitnými požiadavkami na použitie nástrojov
  - Orchestrátor debaty v Python, TypeScript a C# riadiaci kolá a smerovanie argumentov
  - Wiring MCP `ClientSession` pre orchestrátor na reálne volania nástrojov
  - Tabuľka použitia (detekcia halucinácií, príprava hrozieb, revízia návrhu API, overovanie faktov, výber technológií)
  - Bezpečnostné úvahy: spustené v sandboxe, validácia volaní nástrojov, limitovanie rýchlosti, auditovanie záznamov
  - Štruktúrované cvičenie s tromi praktickými scenármi (revízia kódu, rozhodnutia v architektúre, moderovanie obsahu)

#### Opravy Dokumentácie

**Modul 03 - Začíname**
- **05-stdio-server/README.md**: Opravený neúplný príklad TypeScript stdio servera — pridaná chýbajúca inštanciácia transportu (`new StdioServerTransport()`) a volanie `server.connect(transport)` aby sa zhodovalo s príkladmi v jazykoch Python a .NET v rovnakej sekcii
- **14-sampling/README.md**: Opravená preklep — opravené `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aktualizácie kurikula

**Hlavný README.md**
- Pridaný záznam 5.17 (Adversariálne multi-agentné uvažovanie s MCP) do tabuľky kurikula s priamym odkazom na novú lekciu

**05-AdvancedTopics/README.md**
- Pridaný riadok lekcie 5.17 do tabuľky lekcií

**study_guide.md**
- Pridaná téma Adversariálneho multi-agentného uvažovania do myšlienkovej mapy a opis pokročilých tém

#### Opravy kódu a bezpečnosti

**Modul 05 - Adversariálni agenti (`mcp-adversarial-agents`)**
- **Bezpečnostná oprava — injekcia príkazu**: Nahradená shell interpolácia `execSync` použitím `execFile` + `promisify` v TypeScript nástroji `run_python`, čím sa odstránilo riziko injekcie príkazu (kód riadený LLM sa teraz odovzdáva ako doslovný prvok argv bez zapojenia shellu)
- **Zapojenie smyčky MCP nástroja**: Aktualizovaný Python orchestrátor debaty na použitie klienta `AsyncAnthropic` (nahrádzajúci blokujúce sync `Anthropic`), priamym predaním live `ClientSession` na každý ťah agenta, získavaním definícií nástrojov cez `session.list_tools()` na každý ťah a odosielaním blokov `tool_use` cez `session.call_tool()` v slučke až do vygenerovania konečnej textovej odpovede modelom

#### Aktualizácie závislostí

- Aktualizovaný `hono` na verziu 4.12.12 v rôznych balíčkoch (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aktualizovaný `@hono/node-server` z verzie 1.19.11 na 1.19.13 v TypeScript balíčkoch
- Aktualizovaný `cryptography` z verzie 46.0.5 na 46.0.7 v Python balíčkoch (10-StreamliningAIWorkflows laby 3 a 4)
- Aktualizovaný `lodash` z verzie 4.17.23 na 4.18.1 v inšpektore 10-StreamliningAIWorkflows

#### Preklady

- Synchronizované preklady pre viac ako 48 jazykov s najnovšími zdrojovými zmenami (i18n aktualizácia)

---

## 5. februára 2026

### Zdokonalenia validácie a navigácie v repozitári

#### Pridaný nový obsah kurikula

**Modul 03 - Začíname**
- **12-mcp-hosts/README.md**: Nový komplexný sprievodca nastavením MCP hostov
  - Príklady konfigurácií Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Šablóny konfigurácie JSON pre všetky hlavné hosty
  - Porovnávacia tabuľka typov transportov (stdio, SSE/HTTP, WebSocket)
  - Riešenie bežných problémov s pripojením
  - Najlepšie bezpečnostné postupy pre konfiguráciu hosta

- **13-mcp-inspector/README.md**: Nový sprievodca ladením pre MCP Inspector
  - Spôsoby inštalácie (npx, globálne npm, zo zdroja)
  - Pripojenie k serverom cez stdio a HTTP/SSE
  - Testovacie nástroje, zdroje a pracovné postupy promptov
  - Integrácia MCP Inspector s VS Code
  - Bežné scenáre ladenia s riešeniami

**Modul 04 - Praktická implementácia**
- **pagination/README.md**: Nový sprievodca implementáciou stránkovania
  - Vzory stránkovania založené na kurzore v Pythone, Typescripte, Jave
  - Zvládanie stránkovania na strane klienta
  - Stratégie návrhu kurzora (nepriehľadný vs. štruktúrovaný)
  - Odporúčania pre optimalizáciu výkonu

**Modul 05 - Pokročilé témy**
- **mcp-protocol-features/README.md**: Nový podrobný prehľad funkcií protokolu
  - Implementácia notifikácií o pokroku
  - Vzory rušenia požiadaviek
  - Šablóny zdrojov s URI vzormi
  - Správa životného cyklu servera
  - Ovládanie úrovne logovania
  - Vzory spracovania chýb s JSON-RPC kódmi

#### Opravy navigácie (aktualizovaných viac ako 24 súborov)

**Hlavné moduly README**
 Teraz odkazy na prvú lekciu AJ nasledujúci modul

**Pod-súbory 02-Security**
- Všetkých 5 doplnkových bezpečnostných dokumentov teraz obsahuje navigáciu "Čo ďalej"

**Súbory 09-CaseStudy**
- Všetky súbory prípadových štúdií teraz obsahujú sekvenčnú navigáciu

**Laboratóriá 10-StreamliningAI**
Pridaná sekcia Čo ďalej do prehľadu modulu 10 a modulu 11

#### Opravy kódu a obsahu

**Aktualizácie SDK a závislostí**
Opravená prázdna verzia openai na `^4.95.0`
Aktualizované SDK z `^1.8.0` na `>=1.26.0`
Aktualizované pinovanie verzií mcp na `>=1.26.0`

**Opravy kódu**
Opravený neplatný model `gpt-4o-mini` na `gpt-4.1-mini`

**Opravy obsahu**
Opravený nefunkčný odkaz z `READMEmd` na `README.md`, opravený nadpis kurikula z `Module 1-3` na `Module 0-3`, opravená cestová citlivosť na veľkosť písmen
Odstránený poškodený duplicitný obsah Prípadovej štúdie 5

**Zlepšenia pre začiatočníkov**
Pridaný správny úvod, ciele učenia a predpoklady pre začiatočníkov

#### Aktualizácie kurikula

**Hlavný README.md**
- Pridané záznamy 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagestránkovanie), 5.16 (Funkcie protokolu) do tabuľky kurikula

**Moduly README**
Pridané lekcie 12 a 13 do zoznamu lekcií
Pridaná sekcia Praktické príručky s odkazom na stránkovanie
Pridané lekcie 5.15 (Vlastný Transport) a 5.16 (Funkcie protokolu)

**study_guide.md**
- Aktualizovaná myšlienková mapa so všetkými novými témami: Nastavenie MCP hostiteľov, MCP Inspector, stratégie stránkovania, podrobný prehľad funkcií protokolu

## 28. januára 2026

### Revizia zhody so špecifikáciou MCP 2025-11-25

#### Vylepšenie jadrových konceptov (01-CoreConcepts/)
- **Nová primitívna entita klienta - Roots**: Pridaná komplexná dokumentácia o primitíve Roots pre klienta, umožňujúca serverom pochopiť hranice súborového systému a prístupové oprávnenia
- **Anotácie nástrojov**: Pridaná dokumentácia o anotáciách správania nástrojov (`readOnlyHint`, `destructiveHint`) pre lepšie rozhodovanie o vykonávaní nástrojov
- **Volanie nástrojov pri Sampling**: Aktualizovaná dokumentácia Sampling na zahŕňanie parametrov `tools` a `toolChoice` pre modelom riadené volanie nástrojov počas žiadostí o sampling
- **URL mód vyvolávania**: Pridaná dokumentácia o vyvolávaní na základe URL pre externé webové interakcie iniciované serverom
- **Úlohy (Experimentálne)**: Pridaná nová sekcia dokumentujúca experimentálnu funkciu Úlohy pre perzistentné obaly vykonávania a odložené získavanie výsledkov

- **Podpora ikon**: Všimnuté, že nástroje, zdroje, šablóny zdrojov a výzvy môžu teraz obsahovať ikony ako dodatočné metaúdaje

#### Aktualizácie dokumentácie
- **README.md**: Pridané odkazy na špecifikáciu MCP 2025-11-25 a vysvetlenie verziovania podľa dátumu
- **study_guide.md**: Aktualizovaná mapa osnovy na zahrnutie úloh a anotácií nástrojov v sekcii Základné pojmy; aktualizovaný časový údaj dokumentu

#### Overenie zhody so špecifikáciou
- **Verzia protokolu**: Overené, že všetky dokumenty odkazujú na aktuálnu špecifikáciu MCP 2025-11-25
- **Zladenie architektúry**: Potvrdená správnosť dokumentácie dvojvrstvovej architektúry (Dátová vrstva + Prenosová vrstva)
- **Dokumentácia primitívov**: Overené primitíva servera (Zdroje, Výzvy, Nástroje) a primitíva klienta (Vzorkovanie, Elicitačné mechanizmy, Zaznamenávanie, Koreňové prvky)
- **Prenosové mechanizmy**: Skontrolovaná správnosť dokumentácie pre STDIO a Streamable HTTP prenosy
- **Bezpečnostné pokyny**: Potvrdená zhoda so súčasnou dokumentáciou bezpečnostných najlepších praktík MCP

#### Kľúčové vlastnosti MCP 2025-11-25 zdokumentované
- **OpenID Connect Discovery**: Objavovanie autentifikačného servera cez OIDC
- **Metadokumenty OAuth Client ID**: Odporúčaný mechanizmus registrácie klienta
- **JSON Schema 2020-12**: Predvolený dialekt pre definície schém MCP
- **SDK Tiering System**: Formalizované požiadavky na podporu a údržbu funkcií SDK
- **Štruktúra riadenia**: Formalizované pracovné skupiny a záujmové skupiny v správe MCP

### Hlavná aktualizácia bezpečnostnej dokumentácie (02-Security/)

#### Integrácia MCP Security Summit Workshop (Sherpa)
- **Nový praktický školiaci zdroj**: Pridaná komplexná integrácia s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) vo všetkej bezpečnostnej dokumentácii
- **Pokrytie trasy expedície**: Zdokumentovaný kompletný postup od základného tábora po vrchol Summitu
- **Zladenie s OWASP**: Všetky bezpečnostné pokyny teraz mapované na riziká OWASP MCP Azure Security Guide

#### Integrácia OWASP MCP Top 10
- **Nová sekcia**: Pridaná tabuľka OWASP MCP Top 10 bezpečnostných rizík s mitigáciami Azure do hlavného súboru README pre bezpečnosť
- **Dokumentácia založená na rizikách**: Aktualizovaný súbor mcp-security-controls-2025.md s referenciami na riziká OWASP MCP pre každú bezpečnostnú doménu
- **Referenčná architektúra**: Odkaz na OWASP MCP Azure Security Guide referenčnú architektúru a implementačné vzory

#### Aktualizované bezpečnostné súbory
- **README.md**: Pridaný prehľad Sherpa Workshop, tabuľka trasy expedície, zhrnutie OWASP MCP Top 10 rizík a sekcia praktického školenia
- **mcp-security-controls-2025.md**: Aktualizovaný záhlavie na február 2026, pridané referencie na riziká OWASP (MCP01-MCP08), opravená nezhoda verzie špecifikácie
- **mcp-security-best-practices-2025.md**: Pridaná sekcia zdrojov Sherpa a OWASP, aktualizovaný časový údaj
- **mcp-best-practices.md**: Pridaná sekcia praktického školenia s odkazmi na Sherpa a OWASP
- **azure-content-safety-implementation.md**: Pridaná referencia OWASP MCP06, zosúladenie s Sherpa táborom 3 a sekcia ďalších zdrojov

#### Pridané nové zdroje odkazov
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Jednotlivé stránky rizík OWASP MCP (MCP01-MCP10)

### Celková zhoda osnovy so špecifikáciou MCP 2025-11-25

#### Modul 03 - Začíname
- **Dokumentácia SDK**: Pridané Go SDK do oficiálneho zoznamu SDK; aktualizované všetky odkazy na SDK zhoda so špecifikáciou MCP 2025-11-25
- **Vysvetlenie prenosu**: Aktualizované popisy prenosov STDIO a HTTP Streaming s explicitnými odkazmi na špecifikáciu

#### Modul 04 - Praktická implementácia
- **Aktualizácie SDK**: Pridané Go SDK; aktualizovaný zoznam SDK s odkazom na verziu špecifikácie
- **Specifikácia autorizácie**: Aktualizovaný odkaz na MCP autorizáciu na aktuálnu verziu 2025-11-25

#### Modul 05 - Pokročilé témy
- **Nové funkcie**: Pridaná poznámka o nových vlastnostiach MCP špecifikácie 2025-11-25 (Úlohy, anotácie nástrojov, URL mód elicitačných mechanizmov, koreňové prvky)
- **Bezpečnostné zdroje**: Pridané odkazy na OWASP MCP Top 10 a Sherpa workshop do ďalších referencií

#### Modul 06 - Príspevky komunity
- **Zoznam SDK**: Pridané Swift a Rust SDK; aktualizovaný odkaz na špecifikáciu na 2025-11-25
- **Odkaz na špecifikáciu**: Aktualizovaný odkaz MCP špecifikácie na priamu URL špecifikácie

#### Modul 07 - Lekcie z raného zavedenia
- **Aktualizácie zdrojov**: Pridané odkazy na MCP špecifikáciu 2025-11-25 a OWASP MCP Top 10 do ďalších zdrojov

#### Modul 08 - Najlepšie praktiky
- **Verzia špecifikácie**: Aktualizovaný odkaz na MCP špecifikáciu na verziu 2025-11-25
- **Bezpečnostné zdroje**: Pridané odkazy na OWASP MCP Top 10 a Sherpa workshop do ďalších referencií

#### Modul 10 - Zjednodušovanie AI pracovných postupov
- **Aktualizácia odznaku**: Zmena MCP odznaku verzie zo SDK verzie (1.9.3) na verziu špecifikácie (2025-11-25)
- **Odkazy na zdroje**: Aktualizovaný odkaz MCP špecifikácie; pridané OWASP MCP Top 10

#### Modul 11 - MCP server praktické laboratóriá
- **Odkaz na špecifikáciu**: Aktualizovaný odkaz na MCP špecifikáciu na verziu 2025-11-25
- **Bezpečnostné zdroje**: Pridané OWASP MCP Top 10 do oficiálnych zdrojov

## 18. december 2025

### Aktualizácia bezpečnostnej dokumentácie - MCP špecifikácia 2025-11-25

#### Najlepšie bezpečnostné praktiky MCP (02-Security/mcp-best-practices.md) - Aktualizácia verzie špecifikácie
- **Aktualizácia verzie protokolu**: Aktualizovaný odkaz na najnovšiu verziu MCP špecifikácie 2025-11-25 (vydané 25. novembra 2025)
  - Aktualizované všetky odkazy na verziu špecifikácie z 2025-06-18 na 2025-11-25
  - Aktualizované dátumy v dokumentoch z 18. augusta 2025 na 18. decembra 2025
  - Overené, že všetky URL špecifikácie smerujú na aktuálnu dokumentáciu
- **Overenie obsahu**: Komplexné overenie najlepších bezpečnostných praktík podľa najnovších štandardov
  - **Microsoft Security Solutions**: Overené aktuálne pojmy a odkazy pre Prompt Shields (predtým "detekcia rizika jailbreak"), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 bezpečnosť**: Potvrdené zosúladenie s najnovšími bezpečnostnými praktikami OAuth
  - **OWASP štandardy**: Validované, že odkazy na OWASP Top 10 pre LLM zostávajú aktuálne
  - **Služby Azure**: Overené všetky odkazy na dokumentáciu Microsoft Azure a bezpečnostné postupy
- **Zladenie so štandardmi**: Potvrdené, že všetky citované bezpečnostné štandardy sú aktuálne
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 bezpečnostné najlepšie praktiky
  - Azure bezpečnostné a súladové rámce
- **Implementačné zdroje**: Overené všetky odkazy na príručky implementácie a zdroje
  - Overovacie vzory Azure API Management autentifikácie
  - Príručky integrácie Microsoft Entra ID
  - Správa tajomstiev Azure Key Vault
  - DevSecOps pipeline a monitorovacie riešenia

### Zabezpečenie kvality dokumentácie
- **Zhoda so špecifikáciou**: Zabezpečené, že všetky povinné bezpečnostné požiadavky MCP (MUST/MUST NOT) sú v súlade s najnovšou špecifikáciou
- **Aktuálnosť zdrojov**: Overené všetky externé odkazy na Microsoft dokumentáciu, bezpečnostné štandardy a príručky implementácie
- **Pokrytie najlepších praktík**: Potvrdené komplexné pokrytie autentifikácie, autorizácie, AI špecifických hrozieb, bezpečnosti dodávateľského reťazca a podnikových vzorov

## 6. október 2025

### Rozšírenie sekcie Začíname – Pokročilé používanie servera a jednoduchá autentifikácia

#### Pokročilé používanie servera (03-GettingStarted/10-advanced)
- **Pridaná nová kapitola**: Zavedený komplexný návod na pokročilé používanie MCP servera, pokrývajúci bežné aj nízkoúrovňové architektúry servera.
  - **Bežný vs. nízkoúrovňový server**: Detailné porovnanie a ukážky kódu v Pythone a TypeScripte pre obe prístupy.
  - **Návrh založený na handleroch**: Vysvetlenie správy nástrojov/zdrojov/výziev prostredníctvom handlerov pre škálovateľné a flexibilné implementácie servera.
  - **Praktické vzory**: Reálne scenáre, kde sú nízkoúrovňové serverové vzory výhodné pre pokročilé funkcie a architektúru.

#### Jednoduchá autentifikácia (03-GettingStarted/11-simple-auth)
- **Pridaná nová kapitola**: Krok za krokom návod na implementáciu jednoduchej autentifikácie v MCP serveroch.
  - **Koncepty autentifikácie**: Jasné vysvetlenie autentifikácie vs. autorizácie a správa poverení.
  - **Implementácia základnej autentifikácie**: Middleware vzory autentifikácie v Pythone (Starlette) a TypeScript (Express), s ukážkami kódu.
  - **Postup k pokročilej bezpečnosti**: Pokyny na začiatok s jednoduchou autentifikáciou a postup k OAuth 2.1 a RBAC, s odkazmi na pokročilé bezpečnostné moduly.

Tieto doplnky poskytujú praktické, prakticky orientované usmernenia na vytváranie robustnejších, bezpečnejších a flexibilnejších implementácií MCP servera, premostenie základných konceptov s pokročilými produkčnými vzormi.

## 29. september 2025

### MCP Server databázová integrácia - komplexná praktická vzdelávacia cesta

#### 11-MCPServerHandsOnLabs - Nová úplná osnova na integráciu databázy
- **Úplná 13-laboratórna vzdelávacia cesta**: Pridaná komplexná praktická osnova na vytváranie produkčne pripravených MCP serverov s integráciou PostgreSQL databázy
  - **Reálny prípad použitia**: Zava Retail analytický prípad demonštrujúci podnikové vzory
  - **Štruktúrovaný vzdelávací postup**:
    - **Lab 00-03: Základy** - Úvod, základná architektúra, bezpečnosť a multitenancia, nastavenie prostredia
    - **Lab 04-06: Budovanie MCP servera** - Návrh databázy a schéma, implementácia MCP servera, vývoj nástroja
    - **Lab 07-09: Pokročilé funkcie** - Integrácia semantického vyhľadávania, testovanie a ladenie, integrácia VS Code
    - **Lab 10-12: Produkcia a najlepšie praktiky** - Stratégie nasadenia, monitorovanie a observabilita, najlepšie praktiky a optimalizácia
  - **Podnikové technológie**: FastMCP framework, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Pokročilé funkcie**: Bezpečnosť na úrovni riadkov (RLS), semantické vyhľadávanie, prístup k dátam s viacerými nájomníkmi, vektorové embeddingy, monitorovanie v reálnom čase

#### Štandardizácia terminológie - prechod z modulu na lab
- **Komplexná aktualizácia dokumentácie**: Systematicky aktualizované všetky README súbory v 11-MCPServerHandsOnLabs na použitie termínu "Lab" namiesto "Modul"
  - **Hlavičky sekcií**: Aktualizované "Čo tento modul pokrýva" na "Čo tento lab pokrýva" vo všetkých 13 laboratóriách
  - **Popis obsahu**: Zmena "Tento modul poskytuje..." na "Tento lab poskytuje..." v celej dokumentácii
  - **Vzdelávacie ciele**: Aktualizované "Na konci tohto modulu..." na "Na konci tohto labu..."
  - **Navigačné odkazy**: Prevedené všetky odkazy "Modul XX:" na "Lab XX:" v krížových odkazoch a navigácii
  - **Sledovanie dokončenia**: Aktualizované "Po dokončení tohto modulu..." na "Po dokončení tohto labu..."
  - **Zachované technické odkazy**: Zachované odkazy na Python modul v konfiguračných súboroch (napr. `"module": "mcp_server.main"`)

#### Vylepšenie študijného sprievodcu (study_guide.md)
- **Vizualizovaná mapa osnovy**: Pridaná nová sekcia "11. Database Integration Labs" s komplexnou vizualizáciou štruktúry laboratórií
- **Štruktúra repozitára**: Aktualizovaná z desať na jedenásť hlavných sekcií s podrobným popisom 11-MCPServerHandsOnLabs
- **Pokyny pre vzdelávaciu cestu**: Vylepšené navigačné inštrukcie pre sekcie 00-11
- **Pokrytie technológií**: Pridané detaily o FastMCP, PostgreSQL, a integrácii služieb Azure
- **Výsledky učenia**: Zdôraznený vývoj produkčne pripravených serverov, vzory integrácie databáz a podniková bezpečnosť

#### Vylepšenie hlavnej štruktúry README
- **Terminológia založená na laboratóriách**: Aktualizovaný hlavný README.md v 11-MCPServerHandsOnLabs na konzistentné používanie štruktúry "Lab"
- **Organizácia vzdelávacej cesty**: Jasný postup od základných konceptov cez pokročilú implementáciu po produkčné nasadenie
- **Zameranie na reálny svet**: Zdôraznenie praktického, prakticky orientovaného učenia s podnikových vzormi a technológiami

### Zlepšenie kvality a konzistencie dokumentácie
- **Dôraz na praktické učenie**: Posilnený praktický prístup založený na laboratóriách v celej dokumentácii
- **Zameranie na podnikové vzory**: Zvýraznené produkčne pripravené implementácie a podnikové bezpečnostné úvahy
- **Integrácia technológií**: Komplexné pokrytie moderných Azure služieb a AI integračných vzorov
- **Postup vzdelávania**: Jasná, štruktúrovaná cesta od základných konceptov po produkčné nasadenie

## 26. september 2025

### Vylepšenie prípadových štúdií - integrácia s GitHub MCP Registry

#### Prípadové štúdie (09-CaseStudy/) - Zameranie na rozvoj ekosystému
- **README.md**: Rozsiahle rozšírenie s komplexnou prípadovou štúdiou GitHub MCP Registry
  - **Prípadová štúdia GitHub MCP Registry**: Nová komplexná prípadová štúdia skúmajúca uvedenie GitHub MCP Registry v septembri 2025
    - **Analýza problému**: Detailné preskúmanie fragmentovaných výziev v objavovaní a nasadení MCP serverov
    - **Architektúra riešenia**: Centralizovaný registr GitHub s inštaláciou VS Code jedným kliknutím
    - **Obchodný dopad**: Merateľné zlepšenia onboardingu a produktivity vývojárov
    - **Strategická hodnota**: Zameranie na modulárne nasadenie agentov a interoperabilitu nástrojov
    - **Rozvoj ekosystému**: Pozicionovanie ako základná platforma pre agentnú integráciu
  - **Vylepšená štruktúra prípadových štúdií**: Aktualizované všetkých sedem prípadových štúdií so konzistentným formátovaním a komplexnými popismi
    - Azure AI Travel Agents: Dôraz na koordináciu viacerých agentov
    - Azure DevOps Integration: Fokus na automatizáciu pracovných tokov
    - Real-Time Documentation Retrieval: Implementácia klienta v konzole Python
    - Interaktívny generátor študijného plánu: Konverzačná webová aplikácia Chainlit

    - Dokumentácia priamo v editore: Integrácia VS Code a GitHub Copilot
    - Azure API Management: Vzory integrácie podnikových API
    - GitHub MCP Registry: Vývoj ekosystému a komunitná platforma
  - **Komplexné záverečné zhrnutie**: Prepracovaná záverečná časť zdôrazňujúca sedem prípadových štúdií pokrývajúcich viacero dimenzií implementácie MCP
    - Podniková integrácia, orchestrácia viacerých agentov, produktivita vývojára
    - Rozvoj ekosystému, kategorizácia vzdelávacích aplikácií
    - Vylepšené poznatky o architektonických vzorcoch, stratégiách implementácie a najlepších praktík
    - Dôraz na MCP ako zrelý protokol pripravený na produkciu

#### Aktualizácie študijného sprievodcu (study_guide.md)
- **Vizuálna mapa kurikula**: Aktualizovaný myšlienkový map pre zaradenie GitHub MCP Registry v sekcii prípadových štúdií
- **Popis prípadových štúdií**: Vylepšený z všeobecných popisov na podrobný rozbor siedmich komplexných prípadových štúdií
- **Štruktúra repozitára**: Aktualizovaná sekcia 10 reflektujúca komplexné pokrytie prípadových štúdií s konkrétnymi detailmi implementácie
- **Integrácia changelogu**: Pridaný zápis zo 26. septembra 2025 dokumentujúci pridanie GitHub MCP Registry a zlepšenia prípadových štúdií
- **Aktualizácia dátumu**: Aktualizovaný časový údaj v pätičke pre najnovšiu revíziu (26. september 2025)

### Zlepšenia kvality dokumentácie
- **Zlepšenie konzistencie**: Štandardizované formátovanie a štruktúra prípadových štúdií vo všetkých siedmich príkladoch
- **Komplexné pokrytie**: Prípadové štúdie teraz pokrývajú scenáre podnikovej integrácie, produktivity vývojára a rozvoja ekosystému
- **Strategické zameranie**: Zvýraznenie MCP ako základnej platformy pre nasadenie agentných systémov
- **Integrácia zdrojov**: Aktualizované doplnkové zdroje o odkaz na GitHub MCP Registry

## 15. september 2025

### Rozšírenie pokročilých tém - Vlastné transporty a Inžinierstvo kontextu

#### Vlastné MCP transporty (05-AdvancedTopics/mcp-transport/) - Nový sprievodca pokročilou implementáciou
- **README.md**: Kompletný sprievodca implementáciou vlastných transportných mechanizmov MCP
  - **Transport Azure Event Grid**: Komplexná serverless implementácia event-driven transportu
    - Príklady v C#, TypeScript a Pythone s integráciou Azure Functions
    - Vzory architektúry založenej na udalostiach pre škálovateľné MCP riešenia
    - Príjemcovia webhookov a spracovanie správ na báze push notifikácií
  - **Transport Azure Event Hubs**: Implementácia vysoko výkonného streamingového transportu
    - Možnosti streamovania v reálnom čase pre scenáre s nízkou latenciou
    - Stratégie partitioningu a správa checkpointov
    - Zoskupovanie správ a optimalizácia výkonu
  - **Podnikové integračné vzory**: Produkčne pripravené architektonické príklady
    - Distribuované spracovanie MCP naprieč viacerými Azure Functions
    - Hybridné transportné architektúry kombinujúce viacero typov transportov
    - Stratégie odolnosti správ, spoľahlivosti a spracovania chýb
  - **Bezpečnosť a monitorovanie**: Integrácia Azure Key Vault a vzory pozorovateľnosti
    - Overovanie pomocou spravovanej identity a princíp minimálnych práv
    - Telemetria Application Insights a monitorovanie výkonu
    - Vzory circuit breakerov a tolerancia voči chybám
  - **Testovacie rámce**: Komplexné stratégie testovania vlastných transportov
    - Jednotkové testovanie s použitím testovacích náhrad a mocking frameworkov
    - Integračné testovanie s Azure Test Containers
    - Úvahy o výkonovom a záťažovom testovaní

#### Inžinierstvo kontextu (05-AdvancedTopics/mcp-contextengineering/) - Vznikajúca disciplína AI
- **README.md**: Komplexné preskúmanie inžinierstva kontextu ako vznikajúcej oblasti
  - **Základné princípy**: Úplné zdieľanie kontextu, uvedomelosť rozhodnutí akcií a riadenie kontextového okna
  - **Zladenie s protokolom MCP**: Ako dizajn MCP rieši výzvy inžinierstva kontextu
    - Limity kontextového okna a stratégie postupného načítavania
    - Určenie relevantnosti a dynamické získavanie kontextu
    - Multimodálne spracovanie kontextu a bezpečnostné aspekty
  - **Prístupy k implementácii**: Jednovláknové vs. multi-agentové architektúry
    - Techniky delenia na časti a prioritizácie kontextu
    - Strategické postupné načítavanie a kompresia kontextu
    - Viacvrstvové prístupy ku kontextu a optimalizácia získavania informácií
  - **Merací rámec**: Vznikajúce metriky na hodnotenie efektívnosti kontextu
    - Účinnosť vstupu, výkon, kvalita a používateľský zážitok
    - Experimentálne prístupy k optimalizácii kontextu
    - Analýza zlyhaní a metodológie zlepšovania

#### Aktualizácie navigácie kurikula (README.md)
- **Vylepšená štruktúra modulov**: Aktualizovaná tabuľka kurikula o nové pokročilé témy
  - Pridané záznamy Inžinierstvo kontextu (5.14) a Vlastný transport (5.15)
  - Konzistentné formátovanie a navigačné odkazy vo všetkých moduloch
  - Aktualizované popisy odrážajúce súčasný rozsah obsahu

### Vylepšenia štruktúry adresárov
- **Štandardizácia názvov**: Premenovanie "mcp transport" na "mcp-transport" v súlade s ostatnými priečinkami pokročilých tém
- **Organizácia obsahu**: Všetky priečinky 05-AdvancedTopics teraz dodržiavajú konzistentný názvový vzor (mcp-[téma])

### Vylepšenia kvality dokumentácie
- **Zladenie so špecifikáciou MCP**: Všetok nový obsah referuje aktuálnu špecifikáciu MCP 2025-06-18
- **Príklady v viacerých jazykoch**: Komplexné kódové príklady v C#, TypeScript a Python
- **Zameranie na podnikové použitie**: Produkčne pripravené vzory a integrácia s Azure cloudom
- **Vizuálna dokumentácia**: Mermaid diagramy pre vizualizáciu architektúry a tokov

## 18. august 2025

### Komplexná aktualizácia dokumentácie - štandardy MCP 2025-06-18

#### Najlepšie bezpečnostné praktiky MCP (02-Security/) - Kompletná modernizácia
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletné prepracovanie v súlade so špecifikáciou MCP 2025-06-18
  - **Povinné požiadavky**: Pridané explicitné požiadavky MUSÍ/MUSÍ NIE z oficiálnej špecifikácie s jasnými vizuálnymi indikátormi
  - **12 základných bezpečnostných praktík**: Preusporiadané z 15-položkového zoznamu na komplexné bezpečnostné domény
    - Bezpečnosť tokenov a overovanie s integráciou externého poskytovateľa identity
    - Správa relácií a bezpečnosť transportu s kryptografickými požiadavkami
    - Ochrana proti hrozbám špecifickým pre AI s integráciou Microsoft Prompt Shields
    - Kontrola prístupu a oprávnení s princípom minimálnych práv
    - Bezpečnosť obsahu a monitorovanie s integráciou Azure Content Safety
    - Bezpečnosť dodávateľského reťazca s komplexnou verifikáciou komponentov
    - OAuth bezpečnosť a prevencia útokov confundovaného zástupcu s implementáciou PKCE
    - Reakcia na incidenty a zotavenie s automatizovanými schopnosťami
    - Súlad s predpismi a riadenie s reguláciou
    - Pokročilé bezpečnostné kontroly s architektúrou zero trust
    - Integrácia Microsoft bezpečnostného ekosystému s komplexnými riešeniami
    - Neustály vývoj bezpečnosti s adaptívnymi postupmi
  - **Microsoft bezpečnostné riešenia**: Vylepšené pokyny k integrácii Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security
  - **Zdroje implementácie**: Kategorizované komplexné odkazy na zdroje podľa oficiálnej dokumentácie MCP, Microsoft bezpečnostných riešení, bezpečnostných štandardov a sprievodcov implementáciou

#### Pokročilé bezpečnostné kontroly (02-Security/) - Podniková implementácia
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletné prepracovanie s bezpečnostným rámcom na úrovni podniku
  - **9 komplexných bezpečnostných domén**: Rozšírené z základných kontrol na podrobný podnikový rámec
    - Pokročilé overovanie a autorizácia s integráciou Microsoft Entra ID
    - Bezpečnosť tokenov a kontroly proti priechodu s komplexnou validáciou
    - Bezpečnostné kontroly relácií s prevenciou unesenia
    - AI-špecifické bezpečnostné kontroly s prevenciou vstreku promptov a otrávenia nástrojov
    - Prevenzia útokov confundovaného zástupcu s bezpečnosťou proxy OAuth
    - Bezpečnosť spúšťania nástrojov s použitím sandboxingu a izolácie
    - Kontroly bezpečnosti dodávateľského reťazca s verifikáciou závislostí
    - Kontroly monitorovania a detekcie s integráciou SIEM
    - Reakcia na incidenty a zotavenie s automatizovanými schopnosťami
  - **Príklady implementácie**: Pridané detailné YAML konfiguračné bloky a kódové príklady
  - **Integrácia Microsoft riešení**: Komplexné pokrytie bezpečnostných služieb Azure, GitHub Advanced Security a podnikovej správy identity

#### Bezpečnosť pokročilých tém (05-AdvancedTopics/mcp-security/) - Produkčne pripravená implementácia
- **README.md**: Kompletné prepracovanie pre podnikovú bezpečnostnú implementáciu
  - **Zladenie so súčasnou špecifikáciou**: Aktualizované na MCP špecifikáciu 2025-06-18 s povinnými bezpečnostnými požiadavkami
  - **Vylepšené overovanie**: Integrácia Microsoft Entra ID s komplexnými príkladmi v .NET a Java Spring Security
  - **Integrácia bezpečnosti AI**: Implementácia Microsoft Prompt Shields a Azure Content Safety s detailnými príkladmi v Pythone
  - **Pokročilá mitigácia hrozieb**: Komplexné príklady implementácie pre
    - Prevenziu útokov confundovaného zástupcu s PKCE a validáciou súhlasu používateľa
    - Prevenziu priechodu tokenov s overovaním publika a bezpečnou správou tokenov
    - Prevenciu unesenia relácie s kryptografickým viazaním a behaviorálnou analýzou
  - **Integrácia podnikovej bezpečnosti**: Monitorovanie Azure Application Insights, pipeline detekcie hrozieb a bezpečnosť dodávateľského reťazca
  - **Kontrolný zoznam implementácie**: Jasné povinné vs. odporúčané bezpečnostné kontroly s výhodami Microsoft bezpečnostného ekosystému

### Kvalita dokumentácie a zladenie štandardov
- **Odkazy na špecifikáciu**: Aktualizované všetky odkazy na súčasnú špecifikáciu MCP 2025-06-18
- **Microsoft bezpečnostný ekosystém**: Vylepšené pokyny k integrácii v celej dokumentácii bezpečnosti
- **Praktická implementácia**: Pridané detailné kódové príklady v .NET, Java a Python s podnikateľskými vzormi
- **Organizácia zdrojov**: Komplexná kategorizácia oficiálnej dokumentácie, bezpečnostných štandardov a sprievodcov implementácie
- **Vizuálne indikátory**: Jasné označenie povinných požiadaviek vs. odporúčaných praktík


#### Základné koncepcie (01-CoreConcepts/) - Kompletná modernizácia
- **Aktualizácia verzie protokolu**: Aktualizované odkazy na aktuálnu špecifikáciu MCP 2025-06-18 s dátumovou verziou (formát RRRR-MM-DD)
- **Vylepšenie architektúry**: Rozšírené popisy Hostiteľov, Klientov a Serverov reflektujúce súčasné architektonické vzory MCP
  - Hostitelia teraz jasne definovaní ako AI aplikácie koordinujúce viacnásobné MCP klientske spojenia
  - Klienti popísaní ako protokolové konektory udržiavajúce vzťahy jeden na jedného so servermi
  - Servery rozšírené o lokálne vs. vzdialené nasadenie scenáre
- **Prepracovanie primitívnych prvkov**: Kompletné prepracovanie serverových a klientskych primitív
  - Serverové primitíva: Zdroje (dátové zdroje), Prompt-ly (šablóny), Nástroje (vykonateľné funkcie) s detailnými vysvetleniami a príkladmi
  - Klientské primitíva: Odber (LLM dokončenia), Získavanie (užívateľské vstupy), Protokolovanie (ladenie/monitoring)
  - Aktualizované metódy objavovania (`*/list`), získavania (`*/get`) a vykonávania (`*/call`)
- **Architektúra protokolu**: Zavedený model dvojvrstvovej architektúry
  - Dátová vrstva: základy JSON-RPC 2.0 s riadením životného cyklu a primitívmi
  - Transportná vrstva: STDIO (lokálny) a streamovateľný HTTP so SSE (vzdialený) transportné mechanizmy
- **Bezpečnostný rámec**: Komplexné bezpečnostné princípy vrátane explicitného súhlasu používateľa, ochrany súkromia dát, bezpečnosti vykonávania nástrojov a bezpečnosti transportnej vrstvy
- **Komunikačné vzory**: Aktualizované správy protokolu zobrazujúce inicializáciu, objavovanie, vykonávanie a notifikačné toky
- **Kódové príklady**: Obnovené príklady v mnohých jazykoch (.NET, Java, Python, JavaScript) reflektujúce aktuálne vzory MCP SDK

#### Bezpečnosť (02-Security/) - Komplexná bezpečnostná obnova  
- **Zladenie so štandardmi**: Plné zladenie s bezpečnostnými požiadavkami MCP špecifikácie 2025-06-18
- **Vývoj overovania**: Zdokumentovaný vývoj od vlastných OAuth serverov po delegovanie externým poskytovateľom identity (Microsoft Entra ID)
- **AI-špecifická analýza hrozieb**: Rozšírené pokrytie moderných útokov na AI
  - Podrobné scenáre útokov na vstreku promptov s reálnymi príkladmi
  - Mechanizmy otrávenia nástrojov a vzory útokov "rug pull"
  - Otrávenie kontextového okna a útoky spôsobiace zmätok modelu
- **Microsoft AI bezpečnostné riešenia**: Komplexné pokrytie bezpečnostného ekosystému Microsoft
  - AI Prompt Shields s pokročilou detekciou, zvýrazňovaním a technikami oddeľovania
  - Vzory integrácie Azure Content Safety
  - GitHub Advanced Security pre ochranu dodávateľského reťazca
- **Mitigácia pokročilých hrozieb**: Detailné bezpečnostné kontroly pre
  - Unesenie relácie so scénarmi útokov špecifickými pre MCP a kryptografickými požiadavkami na session ID
  - Problémy confundovaného zástupcu v MCP proxy scenároch s explicitnými požiadavkami na súhlas
  - Zraniteľnosti priechodu tokenov s povinnými validačnými kontrolami
- **Bezpečnosť dodávateľského reťazca**: Rozšírené pokrytie AI dodávateľského reťazca vrátane základných modelov, embeddingových služieb, poskytovateľov kontextu a API tretích strán
- **Základná bezpečnosť**: Vylepšená integrácia s podnikový bezpečnostnými vzormi vrátane architektúry zero trust a Microsoft bezpečnostného ekosystému
- **Organizácia zdrojov**: Kategorizovali sa komplexné odkazy na zdroje podľa typu (Oficiálna dokumentácia, štandardy, výskum, Microsoft riešenia, sprievodcovia implementácie)

### Zlepšenia kvality dokumentácie
- **Štruktúrované učebné ciele**: Vylepšené učebné ciele so špecifickými, akčnými výsledkami 
- **Krížové odkazy**: Pridané odkazy medzi súvisiacimi témami bezpečnosti a základných koncepcií
- **Aktuálne informácie**: Aktualizované všetky dátumy a odkazy na štandardy na súčasné verzie
- **Pokyny k implementácii**: Pridané špecifické, akčné implementačné pokyny v oboch sekciách

## 16. júl 2025

### Vylepšenia README a navigácie
- Kompletná prepracovanie navigácie kurikula v README.md
- Nahradené značky `<details>` prístupnejším formátom tabuľky
- Vytvorené alternatívne rozloženia v novom priečinku "alternative_layouts"
- Pridané príklady navigácie založenej na kartách, záložkách a akordeóne
- Aktualizovaná sekcia štruktúry repozitára o všetky najnovšie súbory
- Vylepšená sekcia "Ako používať toto kurikulum" s jasnými odporúčaniami
- Aktualizované odkazy na špecifikácie MCP smerujúce na správne URL
- Pridaná sekcia Inžinierstvo kontextu (5.14) do štruktúry kurikula

### Aktualizácie študijného sprievodcu
- Kompletná revízia študijného sprievodcu pre zosúladenie so súčasnou štruktúrou repozitára
- Pridané nové sekcie pre MCP Klientov a Nástroje a Populárne MCP Servery
- Aktualizovaná Vizuálna mapa kurikula presne odrážajúca všetky témy
- Vylepšené popisy pokročilých tém na pokrytie všetkých špecializovaných oblastí
- Aktualizovaná sekcia Prípadové štúdie reflektujúca aktuálne príklady
- Pridaný tento komplexný changelog

### Príspevky komunity (06-CommunityContributions/)
- Pridané detailné informácie o MCP serveroch pre generovanie obrázkov
- Pridaná rozsiahla sekcia o používaní Claude vo VSCode
- Pridané inštrukcie na nastavenie a používanie terminálového klienta Cline
- Aktualizovaná sekcia MCP klientov o všetky populárne klientské možnosti
- Vylepšené príklady príspevkov s presnejšími vzorkami kódu

### Pokročilé témy (05-AdvancedTopics/)
- Organizované všetky špecializované priečinky tém s konzistentným pomenovaním
- Pridaný materiál a príklady inžinierstva kontextu
- Pridaná dokumentácia integrácie Foundry agenta
- Vylepšená dokumentácia bezpečnostnej integrácie Entra ID

## 11. jún 2025

### Počiatočné vytvorenie
- Vydaná prvá verzia kurikula MCP pre začiatočníkov

- Vytvorená základná štruktúra pre všetkých 10 hlavných sekcií
- Implementovaná vizuálna mapa kurikula pre navigáciu
- Pridané počiatočné ukážkové projekty v rôznych programovacích jazykoch

### Začíname (03-GettingStarted/)
- Vytvorené prvé príklady implementácie servera
- Pridané pokyny na vývoj klienta
- Zahrnuté inštrukcie na integráciu LLM klienta
- Pridaná dokumentácia integrácie VS Code
- Implementované príklady serverov s Server-Sent Events (SSE)

### Základné koncepty (01-CoreConcepts/)
- Pridané podrobné vysvetlenie klient-server architektúry
- Vytvorená dokumentácia o kľúčových komponentech protokolu
- Dokumentované vzory správ v MCP

## 23. mája 2025

### Štruktúra repozitára
- Inicializovaný repozitár so základnou štruktúrou priečinkov
- Vytvorené README súbory pre každú hlavnú sekciu
- Nastavená infraštruktúra pre preklady
- Pridané obrazové zdroje a diagramy

### Dokumentácia
- Vytvorený počiatočný README.md s prehľadom kurikula
- Pridané CODE_OF_CONDUCT.md a SECURITY.md
- Nastavený SUPPORT.md s pokynmi na získanie pomoci
- Vytvorená predbežná štruktúra študijného sprievodcu

## 15. apríla 2025

### Plánovanie a rámec
- Počiatočné plánovanie kurikula MCP pre začiatočníkov
- Definované učebné ciele a cieľová skupina
- Načrtnutá štruktúra kurikula s 10 sekciami
- Vyvinutý konceptuálny rámec pre príklady a prípadové štúdie
- Vytvorené počiatočné prototypové príklady kľúčových konceptov

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->