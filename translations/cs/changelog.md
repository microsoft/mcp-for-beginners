# Přehled změn: MCP pro začátečníky - kurz

Tento dokument slouží jako záznam všech významných změn provedených v kurzu Model Context Protocol (MCP) pro začátečníky. Změny jsou zaznamenány v obráceném chronologickém pořadí (nejnovější změny první).

## 9. září 2026

### MCP 2026-07-28 Finální sladění specifikace

Aktualizovaný anglický kurz z release-kandidáta a základních pokynů `2025-11-25`
na finální specifikaci MCP `2026-07-28`.

- **Aktualizováno**: Odkazy na aktuální verzi, odkazy na specifikaci, vedení pro bezstavové
  požadavky, `server/discover`, streamovatelné HTTP hlavičky a životní cyklus rozšíření Tasks
  napříč 38 anglickými dokumentačními soubory.
- **Opraveno**: Elicitation nyní používá `elicitation/create`, Sampling používá
  `sampling/createMessage`, a `InputRequiredResult.resultType` nyní používá
  `"input_required"`.
- **Nahrazeno**: Nepřesná lekce o Root Context stavu konverzace byla nahrazena
  protokolem přesnou lekcí Roots pokrývající informativní souborové systémové tipy,
  aktuální vícerychlostní tok, bezpečnostní hranice a možnosti migrace.
- **Vyjasněno**: Roots, Sampling, Logging a Dynamická registrace klienta jsou
  v `2026-07-28` zastaralé, s doporučenými náhradami a zdokumentovaným
  nejranějším datem odstranění.
- **Označeno**: Vzorky, které stále závisí na MCP `2025-11-25`, HTTP+SSE,
  inicializačních handshakech, nebo protokolových relacích, jsou ponechány jako příklady
  pro starší kompatibilitu, nikoliv jako aktuální implementace.
- **Bezpečnostní vedení**: Aktualizovány samostatné bezpečnostní návody pro
  autorizaci na úrovni požadavku a explicitní stavové handlery aplikace místo
  odstraněných ID protokolových relací. Dokumenty Client ID Metadata jsou nyní
  preferovanou cestou registrace, s DCR zdokumentovaným pouze jako kompatibilita.
- **Doprovodný materiál**: Aktualizován studijní průvodce, kontrolní seznam přispěvatelů,
  případová studie Publora a případová studie APIM. Procházka APIM nyní doporučuje
  svůj aktuální streamovatelný HTTP `/mcp` endpoint místo zastaralého `/sse`.
- **Kanonické odkazy**: Nahrazeny vyřazené a konceptové URL specifikace v anglických
  zdrojových Markdown souborech verzovanými odkazy `2026-07-28`, přičemž explicitní
  odkazy na starší verze zůstaly, pokud vzorek zůstává připoután ke starším nástrojům.
- **Stabilní názvy souborů**: Přejmenován finální průvodce specifikací a dva bezpečnostní
  návody tak, aby odstranily přípony release-kandidáta a roku, a aktualizovány všechny anglické
  hypertextové odkazy na jejich stabilní cesty.
- **Nový vzorek autorizace**: Přidán testovaný
  [TypeScript MCP `2026-07-28` resource server](./02-Security/samples/cimd-dcr-auth/README.md),
  který porovnává preferované dokumenty Client ID Metadata s deprecated záložní Dynamic
  Client Registration. Vzorek zahrnuje RFC 9728 discovery, validaci JWKS,
  scope pro jednotlivé nástroje, dvanáct testů a průvodce nastavením Auth0.
- **Rozsah překladu**: Byly upraveny pouze anglické zdrojové soubory; generované
  překlady a přeložené obrázky zůstávají nezměněny, protože jsou automaticky překládány.

## 29. července 2026

### Nový doprovodný modul 08: Spolehlivé sidecary a bezpečné opakování

Přidána neutrální lekce pro MCP nástroje, které vytvářejí reálné
efekty, sladěná s finální specifikací `2026-07-28`.

- **Nové**: [doprovodná lekce o spolehlivostních sidecarech][reliability-sidecar]
  využívá jeden příběh o podpoře ticketu, dva Mermaid diagramy a rozhodovací tok
  pro opakování, aby vysvětlila stabilní klíče operací, atomické opakované přijetí,
  rekonsiliaci, důkazy a hranici rozšíření Tasks.
- **Nové**: Cvičení s injektáží selhání pomocí standardní knihovny Python a SQLite
  používá oddělené úložiště operací a tiketů, aby demonstrovalo ztrátu odpovědi
  po potvrzení vnějšího efektu. Šest deterministických testů pokrývá naivní
  duplikaci, chráněnou obnovu restartem, konflikty užitečného zatížení, 
  mezipaměť výsledků, aktivní nároky a souběžné duplikované přijetí.
- **Aktualizováno**: Modul 08 nyní odkazuje na doprovodnou lekci, identifikuje
  finální model bezstavového požadavku `2026-07-28`, rozlišuje OpenTelemetry
  sledovatelnost od zastaralé MCP funkce logování a omezuje svůj
  obecný příklad opakování pouze na operace pro čtení.
- **Volitelné**: Lekce mapuje své přenositelné koncepty k jedné označené komunitní
  implementaci, aniž by hostovaná služba nebo síťové volání byly součástí
  cvičení.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. července 2026

### Nová lekce: Release Candidate specifikace MCP 2026-07-28

Přidáno pokrytí nadcházející release candidate specifikace MCP `2026-07-28` (oznámeno 21. května 2026; finální vydání plánováno na 28. července 2026), shrnuto z [oficiálního oznámení na blogu](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Základ kurzu zůstává **MCP Specification 2025-11-25** až do vydání nové verze, proto je to prezentováno jako výhledové vedení spíše než přepsání stávajících lekcí.

- **Nové**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — plná lekce pokrývající bezstavové jádro protokolu (odstranění handshake `initialize` a `Mcp-Session-Id`), nové směrovací hlavičky `Mcp-Method`/`Mcp-Name`, `ttlMs`/`cacheScope` metadat ke kešování, W3C Trace Context v `_meta`, formální rámec rozšíření (MCP Apps a nové rozšíření Tasks), šest SEP k zesílení autorizace, zastarání Roots/Sampling/Logging a přechod na plný JSON Schema 2020-12 pro schémata nástrojů.
- **Aktualizováno** s výhledovými upozorněními odkazujícími na novou lekci:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): poznámka ke verzi protokolu, sekce Sampling/Roots/Logging/Tasks a "Co dál"
  - [02-Security/README.md](./02-Security/README.md): upozornění na zesílení autorizace
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): upozornění na bezstavný přenos
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): upozornění na zastarání Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): upozornění na zastarání Logging a rozšíření Tasks

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): bezstavové/relace-směrování zvýraznění
  - [README.md](./README.md): poznámka „Díváme se dopředu“ v části specifikace a nová položka `1.1` v tabulce modulu osnovy
  - [study_guide.md](./study_guide.md): výhledový bod v přehledu Jádrových konceptů a datumovaná poznámka dodatku
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): zvýraznění o mapě transportu `mcp-session-id` před modelem bezstavového požadavku
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): zvýraznění přehledu modulu o odstraňování Root Contexts/Sampling a rozšíření úkolů
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): zvýraznění zpevnění autorizace

## 24. června 2026

### Nová lekce: Použití MCP v aplikaci Copilot

- [Sekce nástrojů](./12-tooling/README.md) Přidána sekce nástrojů.
- [MCP v aplikaci Copilot](./12-tooling/01-copilot-app/README.md)

## 16. června 2026

### Srovnání specifikace MCP a ověření ukázek

Ověřili jsme osnovu vůči aktuální **MCP specifikaci 2025-11-25** a nejnovějším oficiálním SDK a následně opravili zbývající neaktuální odkazy na specifikaci a potvrdili, že hlavní ukázky se stále sestavují a spouštějí.

#### Opravy verze specifikace (2025-06-18 / 2025-03-26 → 2025-11-25)

Aktualizovali jsme anglický obsah tam, kde stále tvrdil, že starší revize specifikace je *aktuální/nejnovější* standard, a přesměrovali odkazy na kanonické cesty specifikace `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: aktualizován banner „Current Standard“, úvod, nadpis základních bezpečnostních principů, nadpis povinných požadavků, sekce Microsoft Entra ID, odkazy na Reference a Zdrojové materiály a závěrečné bezpečnostní upozornění (8 odkazů) na 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: aktualizován odkaz na Specifikaci v části Další zdroje a banner „Current Standard“ na 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: nahrazen zastaralý odkaz `2025-03-26` na bezpečnost a důvěryhodnost za aktuální stránku bezpečnostních doporučení z 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: aktualizován odkaz na oficiální dokumentaci vzorkování na 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: aktualizována přítomná reference „aktuální specifikace MCP“ a odkaz na Specifikaci v části Další zdroje na 2025-11-25 (historické poznámky o zrušení SSE ponechány pro přesnost)

#### Ověření ukázek vůči aktuálním SDK

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` vyřešil `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` proběhl bez chyb typů — stávající API `McpServer`/`StdioServerTransport` jsou stále funkční
- **Python (03-GettingStarted/01-first-server/solution/python)**: ověřeno v izolovaném `.venv` s `mcp[cli]` (1.27.2); `py_compile` prošel a `FastMCP.list_tools()` správně vrátil nástroje `add` a `subtract`
- Potvrzeno, že všechny rozsahy verzí ukázek `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) se čistě vyřeší na aktuální `1.29.0` bez rozbití API

#### Vyrovnání pevné verze závislostí (uzavírání mezer ve verzích)

Zvýšili jsme zastaralé verze SDK, aby každý příklad sledoval aktuální vydání MCP, v souladu s konvencí celého repozitáře:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: zvýšeno `@modelcontextprotocol/sdk` z `^1.8.0` → `>=1.26.0` a aktualizován popis balíčku „updated for MCP 2025-06-18“ na „aligned with MCP Specification 2025-11-25“
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** a **lab4/code/github_mcp_server/pyproject.toml**: zvýšena přesná verze `mcp==1.23.0` → `mcp>=1.26.0`; regenerovány oba soubory `uv.lock` (`uv lock`), takže zámkové soubory odkazují na aktuální `mcp 1.27.2` a zůstávají synchronizované s manifesty

#### Analýza mezer v osnově — pokrytí funkcí nejnovější specifikace

Ověřili jsme, že osnova už pokrývá všechny primitivy zavedené/rozšířené v MCP 2025-11-25, takže již nezůstávají žádné mezerové obsahy:
- **Vzorování**: Lekce 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Získávání dat (včetně režimu URL)**: zdokumentováno v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Kořeny**: zdokumentováno v 00-Introduction, 01-CoreConcepts a 05-AdvancedTopics/mcp-root-contexts
- **Úkoly (experimentální, dlouhotrvající operace)**: zdokumentováno v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Anotace nástrojů** (`readOnlyHint` / `destructiveHint`): zdokumentováno v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features

### Zpevnění bezpečnosti a odstranění zranitelností závislostí

Provedli jsme kompletní bezpečnostní audit veškerých manifestů závislostí a zdrojového kódu ukázek, poté odstranili všechny hlášené bezpečnostní chyby npm a jednu chybu na úrovni kódu. Po opravě `npm audit` hlásí **0 zranitelností** ve všech auditovaných adresářích.

#### Zranitelnosti závislostí npm (přechodné) — Opraveno

Auditoval jsem všech 15 commitovaných souborů `package-lock.json`. Zranitelnosti byly omezeny na přechodné závislosti zavedené nástrojem MCP Inspector pro vývoj, klientem OpenAI a MCP SDK; všechny jsou nyní vyřešeny bez rozbití ukázek:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** a **lab3/code/weather_mcp/inspector**: Aktualizován `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), což odstranilo vázané advisory týkající se `ajv`, `brace-expansion`, `diff`, `path-to-regexp` a `ws`. Přidán záznam npm `overrides` vynucující opravený `shell-quote@1.8.4` k odstranění zbývajícího kritického advisories přenášeného `concurrently`; oba lock files regenerovány (nyní 0 zranitelností)
- **03-GettingStarted/samples/typescript**: `npm audit fix` aktualizoval tranzitivní `qs` (střední riziko) na opravenou verzi
- **03-GettingStarted/samples/javascript**: `npm audit fix` aktualizoval tranzitivní `hono` (střední riziko) na opravenou verzi
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` aktualizoval tranzitivní `form-data` (vysoké riziko) na opravenou verzi
- **03-GettingStarted/11-simple-auth/solution/typescript**: Vygenerován chybějící `package-lock.json`, aby byl projekt reprodukovatelný a auditovatelný (0 zranitelností)

#### Oprava zabezpečení na úrovni kódu (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Odstraněno `shell=True` z nástroje `open_in_vscode`. Předchozí `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` umožňovalo interpretaci metaznaků shellu v cestě složky přes `cmd.exe` (vektor útoku příkazovou injekcí). Nyní přímo spouští vyřešený `Code.exe` s cestou k složce jako argumentem – žádný shell – což je funkčně ekvivalentní a bezpečné

#### Audit Python závislostí

- Auditovány všechny sady požadavků Pythonu pomocí `pip-audit`. `05-AdvancedTopics` a `03-GettingStarted/samples/python` nahlásily **žádné známé zranitelnosti** (jejich rozsahy `mcp` / `httpx` / `pydantic` / `python-dotenv` řeší na aktuální opravené verze)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` označil tranzitivní závislost **`werkzeug` 3.1.1** s třemi advisory pro DoS zneužití jmen zařízení ve Windows v `safe_join` — `CVE-2025-66221`, `CVE-2026-21860` a `CVE-2026-27199` (vše opraveno ve verzi 3.1.6). Přidána explicitní bezpečnostní závislost `werkzeug>=3.1.6`, aby byla použita opravená verze; potvrzeno čisté vyřešení s `chainlit` / `mcp` / `semantic-kernel` stackem

### Přejmenování produktů

Aktualizován veškerý obsah kurikula tak, aby odrážel přejmenování produktů společnosti Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Aktualizován odkaz na Discord komunitu
- **AGENTS.md**: Aktualizována reference na Discord server
- **README.md**: Aktualizovány odkazy na technologický ekosystém
- **study_guide.md**: Aktualizovány reference na případové studie
- **05-AdvancedTopics/README.md**: Aktualizován název a popis Modulu 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Aktualizován nadpis sekce a popis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Kompletní aktualizace názvu modulu a obsahu
- **05-AdvancedTopics/mcp-security-entra/README.md**: Aktualizován křížový odkaz
- **07-LessonsfromEarlyAdoption/README.md**: Aktualizovány reference na případové studie
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Aktualizován nadpis sekce 9, odznaky a schopnosti
- **08-BestPractices/README.md**: Aktualizován odkaz na Discord komunitu
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Aktualizován odkaz na Discord kanál
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Aktualizován odkaz na nasazení modelu
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Aktualizována tabulka AI služeb
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Aktualizovány odkazy na zdroje

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Aktualizovány hlavní kurikulární odkazy
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Aktualizován název modulu, přehled a všechny nadpisy modulů
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Aktualizován název, vzdělávací cíle, instrukce nastavení a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Aktualizován název, vzdělávací cíle, tabulka hostitelů MCP a křížové odkazy
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Aktualizován název, odznaky, předpoklady a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Aktualizovány odkazy na Agent Builder a odkaz na zpětnou vazbu
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Aktualizovány předpoklady a odkazy na rozšíření

---

## 11. dubna 2026

### Nová lekce, opravy dokumentace a aktualizace závislostí

#### Přidán nový obsah kurikula

**Modul 05 - Pokročilá témata**
- **Lekce 5.17: Adversariální víceagentní uvažování s MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nová komplexní příručka pokrývající vzor adversariální debaty pro multiagentní systémy
  - Diagram architektury v Mermaid: dva agenti → sdílený MCP server → přepis debaty → rozhodčí → verdikt
  - Sdílený MCP server nástrojů (`web_search` + `run_python`) implementovaný v Pythonu a TypeScriptu
  - Protikladné systémové výzvy (PRO / PROTI / Rozhodčí) s explicitními požadavky na použití nástrojů
  - Orchestrátor debaty v Pythonu, TypeScriptu a C#, spravující kola a směrování argumentů
  - Zapojení MCP `ClientSession` v orchestrátoru pro reálné volání nástrojů
  - Tabulka případů použití (detekce halucinací, modelování hrozeb, revize návrhu API, ověřování faktů, výběr technologií)
  - Bezpečnostní aspekty: sandboxované vykonávání, validace volání nástrojů, omezení rychlosti, auditní záznamy
  - Strukturované cvičení se třemi praktickými scénáři (revize kódu, rozhodování o architektuře, moderování obsahu)

#### Opravy dokumentace

**Modul 03 - Začínáme**
- **05-stdio-server/README.md**: Opraven neúplný příklad TypeScript stdio serveru — přidána chybějící instance transportu (`new StdioServerTransport()`) a volání `server.connect(transport)` odpovídající příkladům v Pythonu a .NET ve stejné sekci
- **14-sampling/README.md**: Oprava překlepu — opraveno `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aktualizace kurikula

**Hlavní README.md**
- Přidán záznam 5.17 (Adversariální víceagentní uvažování s MCP) do tabulky kurikula s přímým odkazem na novou lekci

**05-AdvancedTopics/README.md**
- Přidán řádek Lekce 5.17 do tabulky lekcí

**study_guide.md**
- Přidáno téma Adversariální víceagentní uvažování do myšlenkové mapy a popisu Pokročilých témat

#### Opravy kódu a zabezpečení

**Modul 05 - Adversariální agenti (`mcp-adversarial-agents`)**
- **Oprava zabezpečení — příkazová injekce**: Nahrazen interpolace shellem `execSync` funkcí `execFile` + `promisify` v TypeScript nástroji `run_python`, čímž se odstranila plocha příkazové injekce (kód řízený LLM je nyní předáván jako doslovný prvek argv bez zapojení shellu)
- **Zapojení smyčky MCP nástroje**: Aktualizován Python orchestrátor debaty pro použití klienta `AsyncAnthropic` (nahrazuje blokující synchronní `Anthropic`), předávání živé `ClientSession` přímo každému agentovi na tahu, získávání definic nástrojů přes `session.list_tools()` při každém tahu a vysílání bloků `tool_use` přes `session.call_tool()` ve smyčce, dokud model nevygeneruje konečnou textovou odpověď

#### Aktualizace závislostí

- Aktualizace `hono` na 4.12.12 v několika balíčcích (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aktualizace `@hono/node-server` z 1.19.11 na 1.19.13 v balíčcích TypeScript
- Aktualizace `cryptography` z 46.0.5 na 46.0.7 v Python balíčcích (10-StreamliningAIWorkflows laboratoře 3 a 4)
- Aktualizace `lodash` z 4.17.23 na 4.18.1 v inspektoru 10-StreamliningAIWorkflows

#### Překlady

- Synchronizace překladů pro 48+ jazyků s posledními zdrojovými změnami (aktualizace i18n)

---

## 5. února 2026

### Vylepšení ověřování a navigace v celém repozitáři

#### Přidán nový obsah kurikula

**Modul 03 - Začínáme**
- **12-mcp-hosts/README.md**: Nová komplexní příručka pro nastavení MCP hostů
  - Konfigurační příklady Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Šablony JSON konfigurací pro všechny hlavní hosty
  - Tabulka porovnání typů transportů (stdio, SSE/HTTP, WebSocket)
  - Řešení běžných problémů s připojením
  - Bezpečnostní osvědčené praktiky pro konfiguraci hostitelů

- **13-mcp-inspector/README.md**: Nová příručka pro ladění MCP Inspector
  - Metody instalace (npx, npm globálně, ze zdrojů)
  - Připojování k serverům přes stdio a HTTP/SSE
  - Nástroje na testování, zdroje a pracovní postupy promptů
  - Integrace VS Code s MCP Inspectorem
  - Běžné scénáře ladění s řešeními

**Modul 04 - Praktická implementace**
- **pagination/README.md**: Nová příručka pro implementaci stránkování
  - Vzory stránkování založené na kurzoru v Pythonu, TypeScriptu, Javě
  - Zpracování stránkování na straně klienta
  - Strategie návrhu kurzoru (neprůhledný vs. strukturovaný)
  - Doporučení pro optimalizaci výkonu

**Modul 05 - Pokročilá témata**
- **mcp-protocol-features/README.md**: Hloubková analýza nových funkcí protokolu
  - Implementace oznámení o pokroku
  - Vzory pro zrušení požadavků
  - Šablony zdrojů s URI vzory
  - Správa životního cyklu serveru
  - Řízení úrovně logování
  - Vzory zpracování chyb s JSON-RPC kódy

#### Opravy navigace (aktualizováno 24+ souborů)

**Hlavní moduly READMEs**
 Nyní odkazy jak na první lekci, tak i na další modul

**Podřízené soubory 02-Security**
- Všech 5 doplňkových dokumentů zabezpečení nyní obsahuje sekci "Co dál" pro navigaci:

**Soubory případu studie 09-CaseStudy**
- Všechny soubory případových studií nyní podporují sekvenční navigaci:

**Laboratoře 10-StreamliningAI**
Přidána sekce Co dál do přehledu Modulu 10 a do Modulu 11

#### Opravy kódu a obsahu

**Aktualizace SDK a závislostí**
Opravená prázdná verze openai na `^4.95.0`
SDK aktualizováno z `^1.8.0` na `>=1.26.0`
Závislosti mcp aktualizovány na `>=1.26.0`

**Opravy kódu**
Opraven neplatný model `gpt-4o-mini` na `gpt-4.1-mini`

**Opravy obsahu**
Opraven rozbitý odkaz `READMEmd` → `README.md`, opraven záhlaví kurikula `Module 1-3` → `Module 0-3`, opraven případ citlivosti na malá/velká písmena v cestě
Odstraněn poškozený duplicitní obsah případové studie 5

**Vylepšení pro začátečníky**
Přidán správný úvod, vzdělávací cíle a předpoklady pro začátečníky

#### Aktualizace kurikula

**Hlavní README.md**
- Přidány záznamy 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Stránkování), 5.16 (Funkce protokolu) do tabulky kurikula

**Modulové READMEs**
Přidány lekce 12 a 13 do seznamu lekcí
Přidána sekce Praktické příručky s odkazem na stránkování
Přidány lekce 5.15 (Vlastní transport) a 5.16 (Funkce protokolu)

**study_guide.md**
- Aktualizována myšlenková mapa o všechna nová témata: nastavení MCP hostů, MCP Inspector, strategie stránkování, hloubková analýza funkcí protokolu

## 28. ledna 2026

### Přezkoumání souladu se specifikací MCP 2025-11-25

#### Vylepšení základních konceptů (01-CoreConcepts/)
- **Nový klientský primitiv - Roots**: Přidána obsáhlá dokumentace k roots klientskému primitivu, který umožňuje serverům rozpoznat hranice souborového systému a přístupová oprávnění
- **Anotace nástrojů**: Přidána dokumentace k behaviorálním anotacím nástrojů (`readOnlyHint`, `destructiveHint`) pro lepší rozhodování o používání nástrojů
- **Volání nástrojů při Sampling**: Aktualizována dokumentace Sampling o parametry `tools` a `toolChoice` pro vyvolání modelové podpory nástrojů během požadavků Sampling
- **Elicitace režimu URL**: Přidána dokumentace k vyvolání externích webových interakcí iniciovaných serverem přes URL
- **Úlohy (experimentální)**: Přidána nová sekce k experimentální funkci Úloh pro trvalé vykonávací obálky a odložené získávání výsledků

- **Podpora ikon**: Zaznamenáno, že nástroje, zdroje, šablony zdrojů a promptů nyní mohou obsahovat ikony jako další metadata

#### Aktualizace dokumentace
- **README.md**: Přidána reference na MCP Specification verze 2025-11-25 a vysvětlení verzování podle data
- **study_guide.md**: Aktualizována mapa učebního plánu o úkoly a anotace nástrojů v sekci Základní koncepty; aktualizován časový údaj dokumentu

#### Ověření souladu se specifikací
- **Verze protokolu**: Ověřeno, že veškerá dokumentace odkazuje na aktuální MCP Specification 2025-11-25
- **Soulad architektury**: Potvrzena správnost dokumentace dvouvrstvé architektury (Datová vrstva + Transportní vrstva)
- **Dokumentace primitiv**: Ověřeny serverové primitivy (Zdroje, Prompt, Nástroje) a klientské primitivy (Sampling, Elicitation, Logging, Roots)
- **Přenosové mechanismy**: Ověřena správnost dokumentace STDIO a Streamable HTTP transportu
- **Bezpečnostní doporučení**: Potvrzena shoda s aktuální dokumentací MCP Security Best Practices

#### Hlavní funkce MCP 2025-11-25 zdokumentovány
- **OpenID Connect Discovery**: Objevování autentizačního serveru přes OIDC
- **Dokumenty metadat OAuth Client ID**: Doporučený mechanismus registrace klienta
- **JSON Schema 2020-12**: Výchozí dialekt pro definice MCP schémat
- **Systém úrovní SDK**: Formalizované požadavky na podporu a údržbu funkcí SDK
- **Struktura řízení**: Formalizované pracovní skupiny a zájmové skupiny ve správě MCP

### Velká aktualizace bezpečnostní dokumentace (02-Security/)

#### Integrace MCP Security Summit Workshop (Sherpa)
- **Nový zdroj praktického školení**: Přidána komplexní integrace s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) v celé bezpečnostní dokumentaci
- **Pokrytí trasy expedice**: Zdokumentovaný kompletní průchod od Base Camp po Summit
- **Soulad s OWASP**: Veškerá bezpečnostní doporučení nyní mapují rizika podle OWASP MCP Azure Security Guide

#### Integrace OWASP MCP Top 10
- **Nová sekce**: Přidána tabulka OWASP MCP Top 10 bezpečnostních rizik s mitigacemi Azure do hlavního Security README
- **Dokumentace na základě rizik**: Aktualizován soubor mcp-security-controls-2025.md s odkazy na rizika OWASP MCP pro každou bezpečnostní doménu
- **Referenční architektura**: Propojeno s referenční architekturou OWASP MCP Azure Security Guide a implementačními vzory

#### Aktualizované bezpečnostní soubory
- **README.md**: Přidán přehled Sherpa Workshopu, tabulka trasy expedice, shrnutí OWASP MCP Top 10 rizik a sekce praktického školení
- **mcp-security-controls-2025.md**: Aktualizován nadpis na únor 2026, přidány odkazy na rizika OWASP (MCP01-MCP08), opraveno nesoulad verze specifikace
- **mcp-security-best-practices-2025.md**: Přidána sekce zdrojů Sherpa a OWASP, aktualizován časový údaj
- **mcp-best-practices.md**: Přidána sekce praktického školení s odkazy na Sherpa a OWASP
- **azure-content-safety-implementation.md**: Přidán odkaz na OWASP MCP06, zarovnání s Purpzs Camp 3 a sekce dalších zdrojů

#### Přidány nové odkazy na zdroje
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuální stránky rizik OWASP MCP (MCP01-MCP10)

### Soulad učebního plánu se specifikací MCP 2025-11-25

#### Modul 03 - Začínáme
- **Dokumentace SDK**: Přidán Go SDK do oficiálního seznamu SDK; aktualizovány všechny odkazy SDK pro soulad s MCP Specification 2025-11-25
- **Upřesnění transportu**: Aktualizovány popisy transportu STDIO a HTTP Streaming s explicitními odkazy na specifikaci

#### Modul 04 - Praktická implementace
- **Aktualizace SDK**: Přidán Go SDK; aktualizován seznam SDK s referencí na verzi specifikace
- **Specifikace autorizace**: Aktualizován odkaz na MCP Authorization specifikaci na aktuální verzi 2025-11-25

#### Modul 05 - Pokročilá témata
- **Nové funkce**: Přidána poznámka o nových funkcích MCP Specification 2025-11-25 (Úkoly, Anotace nástrojů, Elicitace režimu URL, Roots)
- **Bezpečnostní zdroje**: Přidány odkazy OWASP MCP Top 10 a Sherpa workshop do doplňkových referencí

#### Modul 06 - Příspevky komunity
- **Seznam SDK**: Přidány Swift a Rust SDK; aktualizován odkaz na specifikaci na 2025-11-25
- **Reference specifikace**: Aktualizován odkaz MCP Specification na přímou URL specifikace

#### Modul 07 - Lekce z rané adopce
- **Aktualizace zdrojů**: Přidán odkaz MCP Specification 2025-11-25 a OWASP MCP Top 10 do doplňkových zdrojů

#### Modul 08 - Nejlepší praktiky
- **Verze specifikace**: Aktualizována reference MCP Specification na 2025-11-25
- **Bezpečnostní zdroje**: Přidány OWASP MCP Top 10 a Sherpa workshop do doplňkových referencí

#### Modul 10 - Zjednodušení AI pracovních toků
- **Aktualizace odznaku**: Změna odznaku verze MCP z verze SDK (1.9.3) na verzi specifikace (2025-11-25)
- **Odkazy na zdroje**: Aktualizován odkaz na MCP Specification; přidán OWASP MCP Top 10

#### Modul 11 - MCP Server Hands-On Labs
- **Reference specifikace**: Aktualizován odkaz MCP Specification na verzi 2025-11-25
- **Bezpečnostní zdroje**: Přidány OWASP MCP Top 10 do oficiálních zdrojů

## 18. prosince 2025

### Aktualizace bezpečnostní dokumentace - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Aktualizace verze specifikace
- **Aktualizace verze protokolu**: Aktualizováno pro referenci na nejnovější MCP Specification 2025-11-25 (vydáno 25. listopadu 2025)
  - Aktualizovány všechny reference na verzi specifikace z 2025-06-18 na 2025-11-25
  - Aktualizovány datumové reference dokumentu z 18. srpna 2025 na 18. prosince 2025
  - Ověřeno, že všechny URL specifikace ukazují na aktuální dokumentaci
- **Validace obsahu**: Komplexní validace bezpečnostních nejlepších praktik podle nejnovějších standardů
  - **Microsoft Security Solutions**: Ověřena aktuální terminologie a odkazy pro Prompt Shields (dříve "detekce rizika jailbreaku"), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 Security**: Potvrzen soulad s nejnovějšími bezpečnostními doporučeními OAuth
  - **OWASP Standards**: Validovány odkazy na OWASP Top 10 pro LLMs jako aktuální
  - **Azure Services**: Ověřeny všechny odkazy na dokumentaci a nejlepší praktiky Microsoft Azure
- **Soulad se standardy**: Potvrzen aktuální stav všech odkazovaných bezpečnostních standardů
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure bezpečnostní a souladu rámce
- **Zdroje implementace**: Ověřeny všechny odkazy na implementační příručky a zdroje
  - Vzory autentizace Azure API Management
  - Průvodci integrací Microsoft Entra ID
  - Správa tajemství Azure Key Vault
  - DevSecOps pipelines a monitoring řešení

### Zajištění kvality dokumentace
- **Soulad se specifikací**: Zajištěno, že všechny povinné bezpečnostní požadavky MCP (MUST/MUST NOT) odpovídají nejnovější specifikaci
- **Aktuálnost zdrojů**: Ověřeny všechny externí odkazy na dokumentaci Microsoft, bezpečnostní standardy a průvodce implementací
- **Pokrytí nejlepších praktik**: Potvrzeno komplexní pokrytí autentizace, autorizace, AI specifických hrozeb, zabezpečení dodavatelského řetězce a podnikových vzorů

## 6. října 2025

### Rozšíření sekce Začínáme – Pokročilé použití serveru a jednoduchá autentizace

#### Pokročilé použití serveru (03-GettingStarted/10-advanced)
- **Přidaná nová kapitola**: Zaveden komplexní průvodce pokročilým používáním MCP serveru pokrývající běžnou i nízkoúrovňovou serverovou architekturu.
  - **Běžný vs. nízkoúrovňový server**: Detailní srovnání a příklady kódu v Pythonu a TypeScriptu pro oba přístupy.
  - **Design založený na handleru**: Vysvětlení správy nástrojů/zdrojů/promptů založené na handlerech pro škálovatelné a flexibilní implementace serveru.
  - **Praktické vzory**: Reálné scénáře, kde jsou nízkoúrovňové serverové vzory prospěšné pro pokročilé funkce a architekturu.

#### Jednoduchá autentizace (03-GettingStarted/11-simple-auth)
- **Přidaná nová kapitola**: Krok za krokem průvodce implementací jednoduché autentizace na MCP serverech.
  - **Koncepty autentizace**: Jasné vysvětlení rozdílu mezi autentizací a autorizací, a manipulace s přihlašovacími údaji.
  - **Implementace základní autentizace**: Middleware vzory autentizace v Pythonu (Starlette) a TypeScriptu (Express), s ukázkami kódu.
  - **Progres k pokročilé bezpečnosti**: Návod, jak začít s jednoduchou autentizací a přejít k OAuth 2.1 a RBAC, s odkazy na pokročilé bezpečnostní moduly.

Tyto doplňky poskytují praktické, hands-on návody pro budování robustnějších, bezpečnějších a flexibilnějších implementací MCP serverů, spojující základní koncepty s pokročilými produkčními vzory.

## 29. září 2025

### MCP Server Database Integration Labs - Komplexní praktická výuka

#### 11-MCPServerHandsOnLabs – Nový kompletní učební plán integrace databází
- **Kompletní učební cesta s 13 laby**: Přidán komplexní praktický kurz pro budování produkčně připravených MCP serverů s integrací PostgreSQL databáze
  - **Reálná implementace**: Příklad analytics Zava Retail demonstrující podnikové vzory
  - **Strukturovaný postup učení**:
    - **Laby 00-03: Základy** - Úvod, Jádrová architektura, Bezpečnost a multi-tenancy, Nastavení prostředí
    - **Laby 04-06: Budování MCP serveru** - Návrh databáze a schéma, Implementace MCP serveru, Vývoj nástrojů
    - **Laby 07-09: Pokročilé funkce** - Integrace sémantického hledání, Testování a ladění, Integrace VS Code
    - **Laby 10-12: Produkce a nejlepší praktiky** - Strategie nasazení, Monitorování a observabilita, Nejlepší praktiky a optimalizace
  - **Podnikové technologie**: Rámec FastMCP, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Pokročilé funkce**: Bezpečnost na úrovni řádku (RLS), sémantické vyhledávání, multitenantní přístup k datům, vektorové embeddingy, monitoring v reálném čase

#### Standardizace terminologie - převod modulů na laby
- **Komplexní aktualizace dokumentace**: Systematická aktualizace všech README souborů v 11-MCPServerHandsOnLabs k používání termínu "Lab" namísto "Modul"
  - **Názvy sekcí**: Aktualizováno "Co tento modul pokrývá" na "Co tento lab pokrývá" ve všech 13 labech
  - **Popis obsahu**: Změněno "Tento modul poskytuje..." na "Tento lab poskytuje..." napříč dokumentací
  - **Vzdělávací cíle**: Aktualizováno "Na konci tohoto modulu..." na "Na konci tohoto labu..."
  - **Navigační odkazy**: Převedeny všechny reference "Modul XX:" na "Lab XX:" v křížových odkazech a navigaci
  - **Sledování dokončení**: Aktualizováno "Po dokončení tohoto modulu..." na "Po dokončení tohoto labu..."
  - **Zachované technické reference**: Uchovány odkazy na Python moduly v konfiguračních souborech (např. `"module": "mcp_server.main"`)

#### Vylepšení studijního průvodce (study_guide.md)
- **Vizualizovaná mapa učebního plánu**: Přidána nová sekce "11. Database Integration Labs" s komplexní strukturou labů
- **Struktura repozitáře**: Změněno z deseti na jedenáct hlavních sekcí s podrobným popisem 11-MCPServerHandsOnLabs
- **Navigační pokyny**: Vylepšeny instrukce pro pokrytí sekcí 00-11
- **Pokrytí technologií**: Přidány podrobnosti o FastMCP, PostgreSQL, integraci Azure služeb
- **Výsledky učení**: Zdůrazněno budování produkčně připravených serverů, vzory integrace databází a podniková bezpečnost

#### Vylepšení hlavní struktury README
- **Terminologie založená na labech**: Hlavní README.md v 11-MCPServerHandsOnLabs aktualizováno k důslednému používání struktury "Lab"
- **Organizace vzdělávací cesty**: Jasný postup od základních konceptů přes pokročilou implementaci k nasazení do produkce
- **Zaměření na reálný svět**: Důraz na praktické, hands-on učení s podnikovými vzory a technologiemi

### Zlepšení kvality a konzistence dokumentace
- **Důraz na praktické učení**: Posílen praktický, labově založený přístup v celé dokumentaci
- **Zaměření na podnikové vzory**: Zvýrazněny produkčně připravené implementace a bezpečnost podnikové úrovně
- **Integrace technologií**: Komplexní pokrytí moderních Azure služeb a AI integračních vzorů
- **Postup učení**: Jasná, strukturovaná cesta od základních konceptů po produkční nasazení

## 26. září 2025

### Vylepšení případových studií - integrace GitHub MCP Registry

#### Případové studie (09-CaseStudy/) - Zaměření na rozvoj ekosystému
- **README.md**: Velké rozšíření s komplexní případovou studií GitHub MCP Registry
  - **Případová studie GitHub MCP Registry**: Nová komplexní případová studie zkoumající spuštění GitHub MCP Registry v září 2025
    - **Analýza problému**: Detailní zkoumání fragmentovaných výzev při objevení a nasazení MCP serverů
    - **Architektura řešení**: Centralizovaný registr GitHub s instalací VS Code na jeden klik
    - **Obchodní dopad**: Měřitelné zlepšení onboardingu vývojářů a produktivity
    - **Strategická hodnota**: Zaměření na modulární nasazení agentů a interoperabilitu mezi nástroji
    - **Rozvoj ekosystému**: Pozicování jako základní platforma pro agentické integrace
  - **Vylepšená struktura případových studií**: Aktualizováno všech sedm případových studií se sjednoceným formátováním a komplexními popisy
    - Azure AI Travel Agents: Důraz na orchestraci více agentů
    - Integrace Azure DevOps: Fokus na automatizaci workflow
    - Dokumentace v reálném čase: Implementace Python konzolového klienta
    - Interaktivní generátor studijních plánů: Řetězcová webová aplikace Chainlit

    - Dokumentace v editoru: Integrace VS Code a GitHub Copilot
    - Azure API Management: Vzory integrace podnikových API
    - GitHub MCP Registry: Vývoj ekosystému a platforma pro komunitu
  - **Komplexní závěr**: Přepracovaná závěrečná část zdůrazňující sedm případových studií pokrývajících více rozměrů implementace MCP
    - Podniková integrace, víceagentová orchestrácia, produktivita vývojářů
    - Vývoj ekosystému, kategorizace vzdělávacích aplikací
    - Rozšířené pohledy na architektonické vzory, strategie implementace a osvědčené postupy
    - Důraz na MCP jako zralý, produkčně připravený protokol

#### Aktualizace studijního průvodce (study_guide.md)
- **Vizualizace osnovy**: Aktualizovaná myšlenková mapa zahrnující GitHub MCP Registry v sekci případových studií
- **Popis případových studií**: Vylepšeno z obecných popisů na podrobný rozbor sedmi komplexních případových studií
- **Struktura repozitáře**: Aktualizována část 10, aby odrážela komplexní pokrytí případových studií s konkrétními detaily implementace
- **Integrace changelogu**: Přidán zápis z 26. září 2025 dokumentující přidání GitHub MCP Registry a vylepšení případových studií
- **Aktualizace dat**: Aktualizovaný časový údaj v zápatí reflektující poslední revizi (26. září 2025)

### Zlepšení kvality dokumentace
- **Zvýšení konzistence**: Standardizované formátování a struktura případových studií napříč všemi sedmi příklady
- **Komplexní pokrytí**: Případové studie nyní zahrnují scénáře podnikové integrace, produktivity vývojářů a rozvoje ekosystému
- **Strategické umístění**: Posílený důraz na MCP jako základní platformu pro nasazení agentních systémů
- **Integrace zdrojů**: Aktualizovány doplňkové materiály o odkaz na GitHub MCP Registry

## 15. září 2025

### Rozšíření pokročilých témat – vlastní transporty a inženýrství kontextu

#### Vlastní transporty MCP (05-AdvancedTopics/mcp-transport/) – Nový průvodce pokročilou implementací
- **README.md**: Kompletní průvodce implementací vlastních transportních mechanismů MCP
  - **Azure Event Grid Transport**: Komplexní serverless implementace událostmi řízeného transportu
    - Příklady v C#, TypeScript a Python s integrací Azure Functions
    - Vzory architektury řízené událostmi pro škálovatelné MCP řešení
    - Příjemci webhooků a zpracování zpráv založené na push mechanismu
  - **Azure Event Hubs Transport**: Implementace transportu pro streamování s vysokou propustností
    - Schopnosti pro streamování v reálném čase s nízkou latencí
    - Strategie dělení na části a správa checkpointů
    - Seskupování zpráv a optimalizace výkonu
  - **Vzory podnikové integrace**: Produkčně připravené příklady architektury
    - Distribuované zpracování MCP přes více Azure Functions
    - Hybridní transportní architektury kombinující více typů transportů
    - Strategie odolnosti zpráv, spolehlivosti a zpracování chyb
  - **Bezpečnost a monitoring**: Integrace Azure Key Vault a vzory observability
    - Autentizace spravované identity a princip minimálních oprávnění
    - Telemetrie Application Insights a monitorování výkonu
    - Vzory pro circuit breakers a odolnost vůči chybám
  - **Testovací rámce**: Komplexní strategie testování vlastních transportů
    - Jednotkové testy s testovacími nahradami a mocking rámci
    - Integrační testování s Azure Test Containers
    - Úvahy o testování výkonu a zatížení

#### Inženýrství kontextu (05-AdvancedTopics/mcp-contextengineering/) – Vznikající disciplína AI
- **README.md**: Komplexní průzkum inženýrství kontextu jako vznikajícího oboru
  - **Základní principy**: Kompletní sdílení kontextu, povědomí o rozhodování akcí a správa kontextového okna
  - **Soulad s protokolem MCP**: Jak design MCP řeší výzvy inženýrství kontextu
    - Omezení velikosti kontextového okna a strategie postupného načítání
    - Určování relevance a dynamické získávání kontextu
    - Zpracování multimodálního kontextu a bezpečnostní aspekty
  - **Přístupy k implementaci**: Jednovláknová vs. víceagentní architektura
    - Techniky dělení kontextu na části a prioritizace
    - Postupné načítání kontextu a kompresní strategie
    - Vícevrstvé přístupy ke kontextu a optimalizace získávání
  - **Měřicí rámec**: Vznikající metriky pro hodnocení efektivity kontextu
    - Účinnost vstupu, výkon, kvalita a úvahy o uživatelském zážitku
    - Experimentální přístupy k optimalizaci kontextu
    - Analýza chyb a metodiky zlepšování

#### Aktualizace navigace osnovy (README.md)
- **Vylepšená struktura modulů**: Aktualizovaná tabulka osnovy zahrnující nová pokročilá témata
  - Přidány položky Inženýrství kontextu (5.14) a Vlastní transport (5.15)
  - Konzistentní formátování a navigační odkazy napříč všemi moduly
  - Aktualizované popisy odrážející aktuální rozsah obsahu

### Zlepšení struktury adresářů
- **Standardizace pojmenování**: Přejmenováno "mcp transport" na "mcp-transport" pro konzistenci s ostatními složkami pokročilých témat
- **Organizace obsahu**: Všechny složky 05-AdvancedTopics nyní následují konzistentní vzor pojmenování (mcp-[téma])

### Vylepšení kvality dokumentace
- **Soulad se specifikací MCP**: Veškerý nový obsah odkazuje na aktuální MCP Specification 2025-06-18
- **Příklady v několika jazycích**: Komplexní ukázky kódu v C#, TypeScriptu a Pythonu
- **Podnikový důraz**: Produkčně připravené vzory a integrace s Azure cloudem napříč dokumentací
- **Vizualizace dokumentace**: Diagramy Mermaid pro vizualizaci architektury a toků

## 18. srpna 2025

### Komplexní aktualizace dokumentace – standardy MCP 2025-06-18

#### Nejlepší bezpečnostní praktiky MCP (02-Security/) – Kompletní modernizace
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletní přepis sladěný s MCP Specification 2025-06-18
  - **Povinné požadavky**: Přidány explicitní požadavky MUSÍ / NESMÍ z oficiální specifikace s jasnými vizuálními ukazateli
  - **12 klíčových bezpečnostních praktik**: Restrukturalizováno z 15 položek na komplexní bezpečnostní domény
    - Zabezpečení tokenů & autentizace s integrací externího poskytovatele identity
    - Správa relací & bezpečnost transportu s kryptografickými požadavky
    - Ochrana proti AI-specifickým hrozbám s integrací Microsoft Prompt Shields
    - Řízení přístupu & oprávnění s principem minimálních oprávnění
    - Bezpečnost obsahu & monitoring s integrací Azure Content Safety
    - Bezpečnost dodavatelského řetězce s komplexní verifikací komponent
    - Bezpečnost OAuth & prevence Confused Deputy s implementací PKCE
    - Incident response & obnova s automatizovanými schopnostmi
    - Soulad & řízení s regulačním sladěním
    - Pokročilé bezpečnostní kontroly se zero trust architekturou
    - Integrace Microsoft bezpečnostního ekosystému s komplexními řešeními
    - Neustálý vývoj bezpečnosti s adaptivními praktikami
  - **Microsoft bezpečnostní řešení**: Vylepšené pokyny k integraci Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security
  - **Implementační zdroje**: Kategorizované komplexní odkazy na zdroje dle Oficiální dokumentace MCP, Microsoft bezpečnostních řešení, bezpečnostních standardů a průvodců implementací

#### Pokročilé bezpečnostní kontroly (02-Security/) – Podniková implementace
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletní revize s podnikově-grade bezpečnostním rámcem
  - **9 komplexních bezpečnostních domén**: Rozšířeno z základních kontrol na detailní podnikový rámec
    - Pokročilá autentizace & autorizace s integrací Microsoft Entra ID
    - Zabezpečení tokenů & kontroly proti průchodu s důkladnou validací
    - Kontroly bezpečnosti relací s prevencí hijackingu
    - AI-specifické bezpečnostní kontroly s prevencí vkládání promptů a otravy nástrojů
    - Prevence Confused Deputy útoků s OAuth proxy bezpečností
    - Bezpečnost spouštění nástrojů s využitím sandboxingu a izolace
    - Kontroly bezpečnosti dodavatelského řetězce s ověřováním závislostí
    - Kontroly monitoringu & detekce s integrací SIEM
    - Incident response & obnova s automatizovanými schopnostmi
  - **Příklady implementace**: Přidány detailní YAML konfigurační bloky a ukázky kódu
  - **Integrace Microsoft řešení**: Komplexní pokrytí bezpečnostních služeb Azure, GitHub Advanced Security a podnikového řízení identity

#### Bezpečnost pokročilých témat (05-AdvancedTopics/mcp-security/) – Produkčně připravená implementace
- **README.md**: Kompletní přepis pro podnikovou implementaci bezpečnosti
  - **Soulad s aktuální specifikací**: Aktualizace na MCP Specification 2025-06-18 s povinnými bezpečnostními požadavky
  - **Vylepšená autentizace**: Integrace Microsoft Entra ID s komplexními příklady pro .NET a Java Spring Security
  - **Integrace AI bezpečnosti**: Implementace Microsoft Prompt Shields a Azure Content Safety s detailními příklady v Pythonu
  - **Pokročilá mitigace hrozeb**: Komplexní implementační příklady pro
    - Prevence Confused Deputy útoků s PKCE a ověřováním uživatelského souhlasu
    - Prevence průchodu tokenů s validací audience a bezpečnou správou tokenů
    - Prevence hijackingu relací s kryptografickým vázáním a behaviorální analýzou
  - **Integrace podnikové bezpečnosti**: Monitorování Azure Application Insights, pipeline detekce hrozeb a bezpečnost dodavatelského řetězce
  - **Kontrolní seznam implementace**: Jasné rozlišení povinných a doporučených bezpečnostních kontrol s výhodami Microsoft bezpečnostního ekosystému

### Kvalita dokumentace a sladění se standardy
- **Odkazy na specifikace**: Aktualizovány všechny odkazy na aktuální MCP Specification 2025-06-18
- **Microsoft bezpečnostní ekosystém**: Vylepšené pokyny k integraci napříč veškerou bezpečnostní dokumentací
- **Praktická implementace**: Přidány detailní příklady kódu v .NET, Javě a Pythonu s podnikatelskými vzory
- **Organizace zdrojů**: Komplexní kategorizace oficiální dokumentace, bezpečnostních standardů a průvodců implementací
- **Vizuální indikátory**: Jasné označení povinných požadavků oproti doporučeným praktikám


#### Základní koncepty (01-CoreConcepts/) – Kompletní modernizace
- **Aktualizace verze protokolu**: Aktualizováno tak, aby odkazovalo na aktuální MCP Specification 2025-06-18 s verzováním založeným na datumu (formát RRRR-MM-DD)
- **Vylepšení architektury**: Rozšířené popisy Hosts, Clients a Servers tak, aby odrážely aktuální architektonické vzory MCP
  - Hosts nyní jasně definovány jako AI aplikace koordinující více klientských připojení MCP
  - Clients popsáni jako protokoloví konektoři udržující vztahy server-jedna-ku-jedné
  - Servers rozšířeny s lokálními vs. vzdálenými scénáři nasazení
- **Přepracování primitiv**: Kompletní revize serverových a klientských primitiv
  - Serverové primitivy: Zdroje (data), Prompty (šablony), Nástroje (spustitelné funkce) s detailními vysvětleními a příklady
  - Klientské primitivy: Sampling (doplnění LLM), Elicitation (uživatelský vstup), Logging (debugging/monitoring)
  - Aktualizováno podle aktuálních vzorů metod discovery (`*/list`), retrieval (`*/get`) a execution (`*/call`)
- **Architektura protokolu**: Zaveden dvouvrstvý architektonický model
  - Datová vrstva: Základ JSON-RPC 2.0 s životním cyklem a primitivy
  - Transportní vrstva: STDIO (lokální) a Streamable HTTP s SSE (vzdálený) transportní mechanismus
- **Bezpečnostní rámec**: Komplexní bezpečnostní principy včetně explicitního souhlasu uživatele, ochrany soukromí dat, bezpečnosti spouštění nástrojů a bezpečnosti transportní vrstvy
- **Komunikační vzory**: Aktualizována protokolová zpráva ukazující inicializaci, objevování, vykonávání a notifikační toky
- **Příklady kódu**: Osvěženy vícejazyčné příklady (.NET, Java, Python, JavaScript) aby odrážely aktuální vzory SDK MCP

#### Bezpečnost (02-Security/) – Komplexní revize bezpečnosti  
- **Soulad se standardy**: Plné sladění s bezpečnostními požadavky MCP Specification 2025-06-18
- **Evoluce autentizace**: Zdokumentován vývoj od vlastních OAuth serverů k delegaci externím poskytovatelům identity (Microsoft Entra ID)
- **AI-specifická analýza hrozeb**: Rozšířený přehled moderních AI vektorů útoků
  - Detailní scénáře útoků prompt injection s reálnými příklady
  - Mechanismy otravy nástrojů a vzory útoků typu "rug pull"
  - Otrava kontextového okna a útoky zmatení modelu
- **Microsoft AI bezpečnostní řešení**: Komplexní pokrytí Microsoft bezpečnostního ekosystému
  - AI Prompt Shields s pokročilou detekcí, spotlightingem a technikami delimiterů
  - Vzory integrace Azure Content Safety
  - GitHub Advanced Security pro ochranu dodavatelského řetězce
- **Pokročilá mitigace hrozeb**: Detailní bezpečnostní kontroly pro
  - Hijacking relace s MCP-specifickými scénáři útoků a kryptografickými požadavky na identifikaci relace
  - Confused deputy problémy v scénářích MCP proxy s explicitními požadavky na souhlas
  - Zranitelnosti token passthrough s povinnými kontrolami validace
- **Bezpečnost dodavatelského řetězce**: Rozšířeno pokrytí AI dodavatelského řetězce včetně základních modelů, embedding služeb, poskytovatelů kontextu a třetích stran API
- **Základní bezpečnost**: Vylepšená integrace s podnikatelskými bezpečnostními vzory včetně zero trust architektury a Microsoft bezpečnostního ekosystému
- **Organizace zdrojů**: Kategorizace komplexních odkazů na zdroje podle typu (Oficiální dokumentace, standardy, výzkum, Microsoft řešení, průvodce implementacemi)

### Zlepšení kvality dokumentace
- **Strukturované výukové cíle**: Vylepšené učební cíle s konkrétními, akčními výsledky
- **Křížové odkazy**: Přidány odkazy mezi souvisejícími bezpečnostními a základními koncepty
- **Aktuální informace**: Aktualizovány všechny datové reference a odkazy na specifikace dle aktuálních standardů
- **Implementační pokyny**: Přidány konkrétní, akční pokyny pro implementaci napříč oběma sekcemi

## 16. července 2025

### Vylepšení README a navigace
- Kompletně přepracovaná navigace osnovy v README.md
- Nahrazeny tagy `<details>` přístupnějším formátem založeným na tabulkách
- Vytvořeny alternativní rozložení v nové složce "alternative_layouts"
- Přidány příklady navigace založené na kartách, záložkách a akordeonovém stylu
- Aktualizována sekce se strukturou repozitáře o veškeré nejnovější soubory
- Vylepšena sekce "Jak používat tuto osnovu" s jasnými doporučeními
- Aktualizovány odkazy na specifikaci MCP, aby směřovaly ke správným URL
- Přidána sekce Inženýrství kontextu (5.14) do struktury osnovy

### Aktualizace studijního průvodce
- Kompletně přepracován studijní průvodce, aby odpovídal aktuální struktuře repozitáře
- Přidány nové sekce pro MCP klienty a nástroje a populární MCP servery
- Aktualizována vizuální mapa osnovy pro přesné zobrazení všech témat
- Vylepšeny popisy pokročilých témat tak, aby pokrývaly všechna specializovaná témata
- Aktualizována sekce případových studií, aby odrážela skutečné příklady
- Přidán tento komplexní changelog

### Příspěvky komunity (06-CommunityContributions/)
- Přidány detailní informace o MCP serverech pro generování obrázků
- Přidána komplexní sekce o použití Claude ve VSCode
- Přidány instrukce pro nastavení a používání Cline terminálového klienta
- Aktualizována sekce MCP klientů tak, aby zahrnovala všechny populární možnosti klientů
- Vylepšeny příklady příspěvků o přesnější ukázky kódu

### Pokročilá témata (05-AdvancedTopics/)
- Organizované všechny specializované složky témat s konzistentním pojmenováním
- Přidány materiály a příklady inženýrství kontextu
- Přidána dokumentace integrace Foundry agenta
- Vylepšena dokumentace integrace bezpečnosti Entra ID

## 11. června 2025

### Počáteční vytvoření
- Uvolněna první verze osnovy MCP pro začátečníky

- Vytvořena základní struktura pro všech 10 hlavních sekcí
- Implementována vizuální mapa kurikula pro navigaci
- Přidány úvodní ukázkové projekty v několika programovacích jazycích

### Začínáme (03-GettingStarted/)
- Vytvořeny první příklady implementace serveru
- Přidány pokyny pro vývoj klienta
- Zahrnuty instrukce pro integraci klienta LLM
- Přidána dokumentace integrace VS Code
- Implementovány příklady serveru využívajícího Server-Sent Events (SSE)

### Základní koncepty (01-CoreConcepts/)
- Přidáno podrobné vysvětlení architektury klient-server
- Vytvořena dokumentace o klíčových prvcích protokolu
- Dokumentovány vzory zasílání zpráv v MCP

## 23. května 2025

### Struktura repozitáře
- Inicializován repozitář se základní strukturou složek
- Vytvořeny README soubory pro každou hlavní sekci
- Nastavena infrastruktura pro překlady
- Přidány obrazové zdroje a diagramy

### Dokumentace
- Vytvořen počáteční README.md s přehledem kurikula
- Přidány soubory CODE_OF_CONDUCT.md a SECURITY.md
- Nastaven SUPPORT.md s pokyny pro získání pomoci
- Vytvořena předběžná struktura studijní příručky

## 15. dubna 2025

### Plánování a rámec
- Úvodní plánování kurikula MCP pro začátečníky
- Definovány cíle učení a cílová skupina
- Načrtnuta struktura kurikula v 10 sekcích
- Vyvinut konceptuální rámec pro příklady a případové studie
- Vytvořeny počáteční prototypové příklady klíčových konceptů

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->