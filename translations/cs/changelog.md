# Přehled změn: MCP pro začátečníky – učební plán

Tento dokument slouží jako záznam všech významných změn provedených v učebním plánu Model Context Protocol (MCP) pro začátečníky. Změny jsou dokumentovány v obráceném chronologickém pořadí (novější změny první).

## 29. července 2026

### Nový doprovodný modul 08: Spolehlivé sidecary a bezpečné opakování

Přidána neutrální doprovodná lekce pro nástroje MCP, které vytvářejí reálné
efekty, v souladu s finální specifikací `2026-07-28`.

- **Nové**: [doprovodná lekce o spolehlivých sidecarech][reliability-sidecar]
  využívá jeden příběh s tiketem podpory, dva Mermaid diagramy a tok rozhodování o opakování
  k vysvětlení klíčů stabilního provozu, atomického přijetí duplikátů,
  vyrovnávání, důkazů a hranice rozšíření Tasks.
- **Nové**: Cvičení na injektování chyb v Pythonu a SQLite ve standardní knihovně
  využívá oddělené ukládání operací a tiketů k demonstraci ztráty odpovědi
  po potvrzení externího efektu. Šest deterministických testů pokrývá naivní
  duplikaci, chráněné zotavení restartu, konflikty v nákladu, cache výsledků,
  aktivní nároky a souběžné přijetí duplikátů.
- **Aktualizováno**: Modul 08 nyní obsahuje odkaz na doprovodnou lekci, identifikuje
  finální model stateless požadavků `2026-07-28`, rozlišuje OpenTelemetry
  observabilitu od zastaralé funkce logování MCP a omezuje svůj
  obecný příklad opakování na operace pouze pro čtení.
- **Volitelné**: Lekce mapuje své přenosné koncepty na jednu označenou komunitní
  implementaci, aniž by činila hostovanou službu nebo síťový hovor součástí
  cvičení.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. července 2026

### Nová lekce: Kandidát na vydání specifikace MCP 2026-07-28

Přidáno pokrytí nadcházejícího kandidáta na vydání specifikace MCP `2026-07-28` (oznámáno 21. května 2026; konečné vydání plánováno na 28. července 2026), shrnuto z [oficiálního blogového příspěvku o oznámení](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Základ učebního plánu zůstává **MCP Specifikace 2025-11-25**, dokud nová verze nebude zveřejněna, takže toto je prezentováno jako výhled do budoucna, nikoli jako přepis stávajících lekcí.

- **Nové**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — plnohodnotná lekce pokrývající jádro bezstavového protokolu (odstranění úvodního handshake `initialize` a `Mcp-Session-Id`), nové směrovací hlavičky `Mcp-Method`/`Mcp-Name`, metadata ukládání do cache `ttlMs`/`cacheScope`, W3C Trace Context v `_meta`, formální rámec rozšíření (MCP Apps a nové rozšíření Tasks), šest bezpečnostních a autorizačních SEP, zastaralost Roots/Sampling/Logging a přechod na plný JSON Schema 2020-12 pro schémata nástrojů.
- **Aktualizováno** s výhledovými odkazy na novou lekci:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): poznámka o verzi protokolu, sekce Sampling/Roots/Logging/Tasks a "Co dál"
  - [02-Security/README.md](./02-Security/README.md): poznámka o posílení autorizace
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): upozornění na bezstavný transport
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): upozornění na ukončení Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): upozornění na ukončení Logging a rozšíření Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): upozornění na bezstavné/směrování relací
  - [README.md](./README.md): poznámka "Výhled do budoucna" v sekci specifikace a nová položka `1.1` v tabulce modulů učebního plánu
  - [study_guide.md](./study_guide.md): výhledový bod v přehledu základních konceptů a datumovaný dodatkový poznatek
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): upozornění na transportní mapu `mcp-session-id` před modelem bezstavných požadavků
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): upozornění v přehledu modulu na ukončení Root Contexts/Sampling a rozšíření Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): upozornění na posílení autorizace

## 24. června 2026

### Nová lekce: Použití MCP v aplikaci Copilot

- [Sekce Nástroje](./12-tooling/README.md) Přidána sekce nástrojů.
- [MCP v aplikaci Copilot](./12-tooling/01-copilot-app/README.md)

## 16. června 2026

### Zarovnání se specifikací MCP a validace vzorků

Validovali jsme učební plán proti aktuální **MCP Specifikaci 2025-11-25** a nejnovějším oficiálním SDK, poté jsme opravili zbývající zastaralé odkazy na specifikaci a potvrdili, že základní vzorky se stále staví a spouští.

#### Opravy verze specifikace (2025-06-18 / 2025-03-26 → 2025-11-25)

Aktualizovaný anglický obsah tam, kde stále uváděl starší revizi specifikace jako *aktuální/nejnovější* standard, a přesměrovány odkazy na kanonické cesty specifikace `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Aktualizován banner "Aktuální standard", úvod, nadpis principů zabezpečení, povinných požadavků, sekce Microsoft Entra ID, odkazy na Reference & zdroje a závěrečné bezpečnostní upozornění (8 odkazů) na 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Aktualizován odkaz na Specifikaci v sekci Další zdroje a banner "Aktuální standard" na 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Nahrazen zastaralý odkaz na bezpečnost a důvěru `2025-03-26` aktuální stránkou s nejlepšími postupy bezpečnosti 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Aktualizován oficiální odkaz na dokumentaci Sampling na 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Aktualizována současná referencia na "aktuální MCP specifikaci" a odkaz na Specifikaci v sekci Další zdroje na 2025-11-25 (historické poznámky o ukončení SSE ponechány pro přesnost)

#### Validace vzorků proti aktuálním SDK

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` nainstaloval `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` prošel bez chyb v typech — existující API `McpServer`/`StdioServerTransport` zůstávají platná
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validováno v izolovaném `.venv` s `mcp[cli]` (1.27.2); `py_compile` bez chyb a `FastMCP.list_tools()` správně vrátil nástroje `add` a `subtract`
- Potvrzeno, že všechny rozsahy verzí `@modelcontextprotocol/sdk` ve vzorcích (`>=1.26.0` / `^1.26.0` / `^1.27.0`) se čistě vyřeší na aktuální `1.29.0` bez nekompatibilních změn API

#### Zarovnání závislostí (uzavření mezer ve verzích)

Aktualizována zastaralá zafixovaná verze SDK tak, aby každý vzorek sledoval aktuální vydání MCP, v souladu s konvencí celého repo:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Zvýšena minimální verze `@modelcontextprotocol/sdk` z `^1.8.0` na `>=1.26.0` a aktualizován popis balíčku ze zastaralého `"updated for MCP 2025-06-18"` na `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** a **lab4/code/github_mcp_server/pyproject.toml**: Zvýšena přesná verze `mcp==1.23.0` na `mcp>=1.26.0`; regenerovány oba soubory `uv.lock` (`uv lock`), aby se lockfiles řešily na aktuální `mcp 1.27.2` a zůstaly synchronizovány s manifesty

#### Analýza mezer v učebním plánu — Pokrytí funkcí nejnovější specifikace

Ověřeno, že učební plán již pokrývá všechny primitivy zavedené/rozšířené v MCP 2025-11-25, takže žádné obsahové mezery nezůstávají:
- **Sampling**: Lekce 03-GettingStarted/14-sampling a 05-AdvancedTopics/mcp-sampling
- **Elicitation (včetně režimu URL)**: Zdokumentováno v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Zdokumentováno v 00-Introduction, 01-CoreConcepts a 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentální, dlouhotrvající operace)**: Zdokumentováno v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features
- **Anotace nástrojů** (`readOnlyHint` / `destructiveHint`): Zdokumentováno v 01-CoreConcepts a 05-AdvancedTopics/mcp-protocol-features

### Posílení bezpečnosti a odstranění zranitelností závislostí

Proveden úplný bezpečnostní audit všech manifestů závislostí a zdrojového kódu vzorků, poté odstraněny všechny nahlášené npm upozornění a jedna nálezová chyba v kódu. Po opravě hlásí `npm audit` **0 zranitelností** ve všech kontrolovaných adresářích.

#### Zranitelnosti závislostí npm (transitivní) — Opraveno

Zkontrolováno všech 15 souborů `package-lock.json`. Zranitelnosti byly omezeny na tranzitivní závislosti vyvolané nástrojem MCP Inspector, klientem OpenAI a MCP SDK; všechny nyní vyřešeny bez porušení funkčnosti vzorků:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** a **lab3/code/weather_mcp/inspector**: Zvýšena verze `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), čímž byly vyčištěny nahlášené problémy u zabalených `ajv`, `brace-expansion`, `diff`, `path-to-regexp` a `ws`. Přidán vstup `overrides` v npm nutící opravený `shell-quote@1.8.4` pro odstranění zbývajícího kritického upozornění na `concurrently`; oba lockfile regenerovány (nyní 0 zranitelností)
- **03-GettingStarted/samples/typescript**: `npm audit fix` aktualizoval tranzitivní `qs` (střední riziko) na opravenou verzi
- **03-GettingStarted/samples/javascript**: `npm audit fix` aktualizoval tranzitivní `hono` (střední riziko) na opravenou verzi
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` aktualizoval tranzitivní `form-data` (vysoké riziko) na opravenou verzi
- **03-GettingStarted/11-simple-auth/solution/typescript**: Vygenerován chybějící `package-lock.json`, takže projekt je reprodukovatelný a auditovatelný (0 zranitelností)

#### Oprava bezpečnosti na úrovni kódu (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Odebráno `shell=True` z nástroje `open_in_vscode`. Předchozí `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` umožňoval interpretaci metaznaků shellu v cestě ke složce prostřednictvím `cmd.exe` (vektor příkazové injekce). Nyní spouští přímo vyřešený `Code.exe` se složkou jako argumentem — bez shellu — což je funkčně ekvivalentní a bezpečné

#### Audit závislostí Pythonu

- Proveden audit všech Python requirements s `pip-audit`. `05-AdvancedTopics` a `03-GettingStarted/samples/python` nehlásily žádné známé zranitelnosti (jejich rozsahy `mcp` / `httpx` / `pydantic` / `python-dotenv` směřují na aktuální opravné verze)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` označil tranzitivní závislost **`werkzeug` 3.1.1** s třemi nahlášenými zranitelnostmi DoS jménem zařízení ve Windows při použití `safe_join` — `CVE-2025-66221`, `CVE-2026-21860` a `CVE-2026-27199` (vše vyřešeno ve verzi 3.1.6). Přidán explicitní bezpečnostní pin `werkzeug>=3.1.6`, aby se vyřešila opravená verze; ověřeno čisté vyřešení omezení v rámci stacku `chainlit` / `mcp` / `semantic-kernel`

### Přejmenování produktů

Aktualizován veškerý obsah učebního plánu, aby reflektoval přejmenování produktů Microsoftu:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Aktualizován odkaz na komunitu Discord

- **AGENTS.md**: Aktualizována reference Discord serveru
- **README.md**: Aktualizovány reference technologického ekosystému
- **study_guide.md**: Aktualizovány reference případových studií
- **05-AdvancedTopics/README.md**: Aktualizován název a popis modulu 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Aktualizován záhlaví sekce a popis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Kompletní aktualizace názvu modulu a obsahu
- **05-AdvancedTopics/mcp-security-entra/README.md**: Aktualizován odkaz na křížové reference
- **07-LessonsfromEarlyAdoption/README.md**: Aktualizovány reference případových studií
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Aktualizováno záhlaví sekce 9, odznaky a schopnosti
- **08-BestPractices/README.md**: Aktualizován odkaz na Discord komunitu
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Aktualizována reference kanálu Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Aktualizována reference nasazení modelu
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Aktualizována tabulka AI služeb
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Aktualizovány reference zdrojů

#### AI Toolkit / AITK → Rozšíření Microsoft Foundry Toolkit pro VS Code
- **README.md**: Aktualizovány hlavní reference kurikula
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Aktualizován název modulu, přehled a všechny nadpisy modulů
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Aktualizován název, cíle učení, instrukce nastavení a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Aktualizován název, cíle učení, tabulka MCP hostů a křížové reference
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Aktualizován název, odznaky, předpoklady a zdroje
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Aktualizovány reference Agent Builderu a odkaz na zpětnou vazbu
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Aktualizovány předpoklady a reference rozšíření

---

## 11. dubna 2026

### Nová lekce, opravy dokumentace a aktualizace závislostí

#### Přidán nový obsah kurikula

**Modul 05 - Pokročilá témata**
- **Lekce 5.17: Adversariální multiagentní uvažování s MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nový komplexní průvodce pokrývající vzor adversariálních debat pro multiagentní systémy
  - Mermaid diagram architektury: dva agenti → sdílený MCP server → přepis debaty → soudce → verdikt
  - Sdílený MCP nástrojový server (`web_search` + `run_python`) implementovaný v Pythonu a TypeScriptu
  - Protikladné systémové výzvy (PROTI / ZASTÁVACÍ / Soudce) s explicitními požadavky na použití nástrojů
  - Orchestrátor debaty v Pythonu, TypeScriptu a C# spravující kola a směrování argumentů
  - MCP `ClientSession` propojení pro orchestrátora k volání skutečných nástrojů
  - Tabulka použití (detekce halucinací, modelování hrozeb, revize návrhu API, ověřování faktů, výběr technologií)
  - Bezpečnostní aspekty: sandboxované provádění, validace volání nástrojů, omezení rychlosti, auditní protokolování
  - Strukturované cvičení se třemi praktickými scénáři (revize kódu, rozhodnutí o architektuře, moderace obsahu)

#### Opravy dokumentace

**Modul 03 - Začínáme**
- **05-stdio-server/README.md**: Opraven neúplný příklad TypeScript stdio serveru — doplněna chybějící instance transportu (`new StdioServerTransport()`) a volání `server.connect(transport)` v souladu s příklady v Pythonu a .NET v téže sekci
- **14-sampling/README.md**: Opraven překlep — oprava `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Aktualizace kurikula

**Hlavní README.md**
- Přidána položka 5.17 (Adversariální multiagentní uvažování s MCP) do tabulky kurikula s přímým odkazem na novou lekci

**05-AdvancedTopics/README.md**
- Přidán řádek Lekce 5.17 do tabulky lekcí

**study_guide.md**
- Přidáno téma Adversariální multiagentní uvažování do myšlenkové mapy a textového popisu Pokročilých témat

#### Opravy kódu a bezpečnosti

**Modul 05 - Adversariální agenti (`mcp-adversarial-agents`)**
- **Bezpečnostní oprava — injekce příkazů**: Nahrazení shell interpolace `execSync` za `execFile` + `promisify` v TypeScript nástroji `run_python`, čímž je odstraněna plocha pro injekci příkazů (kód řízený LLM je nyní předáván jako doslovný argv prvek bez zapojení shellu)
- **Propojení smyčky nástrojů MCP**: Aktualizován orchestrátor debaty v Pythonu k použití klienta `AsyncAnthropic` (nahrazení blokujícího synchronního `Anthropic`), předávání živé `ClientSession` přímo do každého tahu agenta, získávání definice nástrojů pomocí `session.list_tools()` v každém tahu a odesílání bloků `tool_use` pomocí `session.call_tool()` v cyklu, dokud model nevygeneruje finální textovou odpověď

#### Aktualizace závislostí

- Aktualizováno `hono` na 4.12.12 napříč více balíčky (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Aktualizováno `@hono/node-server` z 1.19.11 na 1.19.13 v TypeScript balíčcích
- Aktualizováno `cryptography` z 46.0.5 na 46.0.7 v Python balíčcích (laboratoře 3 a 4 z 10-StreamliningAIWorkflows)
- Aktualizováno `lodash` z 4.17.23 na 4.18.1 v inspektoru 10-StreamliningAIWorkflows

#### Překlady

- Synchronizovány překlady pro více než 48 jazyků s nejnovějšími změnami zdroje (aktualizace i18n)

---

## 5. února 2026

### Zlepšení validace a navigace v celém repozitáři

#### Přidán nový obsah kurikula

**Modul 03 - Začínáme**
- **12-mcp-hosts/README.md**: Nový komplexní průvodce nastavením MCP hostitelů
  - Příklady konfigurace Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Šablony konfigurace JSON pro všechny hlavní hostitele
  - Tabulka porovnání typů transportů (stdio, SSE/HTTP, WebSocket)
  - Řešení běžných problémů s připojením
  - Bezpečnostní osvědčené postupy konfigurace hostitelů

- **13-mcp-inspector/README.md**: Nový průvodce laděním pro MCP Inspector
  - Způsoby instalace (npx, globální npm, ze zdroje)
  - Připojení k serverům přes stdio a HTTP/SSE
  - Testovací nástroje, zdroje a pracovní postupy s výzvami
  - Integrace VS Code s MCP Inspectorem
  - Běžné ladicí scénáře a řešení

**Modul 04 - Praktická implementace**
- **pagination/README.md**: Nový průvodce implementací stránkování
  - Vzory stránkování založené na kurzoru v Pythonu, TypeScriptu, Javě
  - Zacházení se stránkováním na straně klienta
  - Strategie návrhu kurzoru (neprůhledný vs. strukturovaný)
  - Doporučení pro optimalizaci výkonu

**Modul 05 - Pokročilá témata**
- **mcp-protocol-features/README.md**: Nový podrobný průzkum funkcí protokolu
  - Implementace notifikací postupu
  - Vzory zrušení požadavků
  - Šablony zdrojů s URI vzory
  - Správa životního cyklu serveru
  - Řízení úrovně logování
  - Vzory zpracování chyb s JSON-RPC kódy

#### Opravy navigace (aktualizováno 24+ souborů)

**Hlavní moduly README**
 Nyní s odkazy na první lekci I další modul

**Podřízené soubory 02-Security**
- Všech 5 doplňujících dokumentů bezpečnosti nyní obsahuje navigaci "Co dál"

**Soubory 09-CaseStudy**
- Všechny soubory případových studií nyní mají sekvenční navigaci

**Laboratoře 10-StreamliningAI**
Přidána sekce Co dál k přehledu Modulu 10 a Modulu 11

#### Opravy kódu a obsahu

**Aktualizace SDK a závislostí**
Opravená prázdná verze openai na `^4.95.0`
Aktualizováno SDK z `^1.8.0` na `>=1.26.0`
Aktualizovány mcp verze zámků na `>=1.26.0`

**Opravy kódu**
Opraven neplatný model `gpt-4o-mini` na `gpt-4.1-mini`

**Opravy obsahu**
Opraven nefunkční odkaz `READMEmd` → `README.md`, opraven záhlaví kurikula `Module 1-3` → `Module 0-3`, opraveno velikostní rozlišování cesty
Odstraněn poškozený duplicitní obsah případové studie 5

**Zlepšení vedení pro začátečníky**
Přidán správný úvod, cíle učení a předpoklady pro začátečníky

#### Aktualizace kurikula

**Hlavní README.md**
- Přidány položky 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Stránkování), 5.16 (Funkce protokolu) do tabulky kurikula

**Modulové README**
Přidány lekce 12 a 13 do seznamu lekcí
Přidána sekce Praktické průvodce s odkazem na stránkování
Přidány lekce 5.15 (Vlastní Transport) a 5.16 (Funkce protokolu)

**study_guide.md**
- Aktualizována myšlenková mapa o všech nových tématech: Nastavení MCP Hosts, MCP Inspector, Strategie stránkování, Podrobný průzkum funkcí protokolu

## 28. ledna 2026

### Revize shody se specifikací MCP 2025-11-25

#### Rozšíření základních konceptů (01-CoreConcepts/)
- **Nový klientský primitiv - Roots**: Přidána komplexní dokumentace ke klientskému primitivu Roots, umožňující serverům rozumět hranicím systémů souborů a oprávněním přístupu
- **Anotace nástrojů**: Přidána dokumentace k behaviorálním anotacím nástrojů (`readOnlyHint`, `destructiveHint`) pro lepší rozhodování o vykonávání nástrojů
- **Volání nástrojů při Sampling**: Aktualizována dokumentace Sampling o parametry `tools` a `toolChoice` pro modelem řízené volání nástrojů během požadavků na Sampling
- **Elicitation režim URL**: Přidána dokumentace k elicitation založenému na URL pro serverem iniciované externí webové interakce
- **Tasks (experimentální)**: Přidána nová sekce dokumentující experimentální funkci Tasks pro trvalé obaly provádění a odložené získávání výsledků
- **Podpora ikon**: Uvedeno, že nástroje, zdroje, šablony zdrojů a výzvy nyní mohou obsahovat ikony jako dodatečná metadata

#### Aktualizace dokumentace
- **README.md**: Přidána reference verze MCP Specification 2025-11-25 a vysvětlení verzování podle data
- **study_guide.md**: Aktualizována mapa kurikula o Tasks a Tool Annotations v sekci Core Concepts; aktualizováno datum dokumentu

#### Ověření shody se specifikací
- **Verze protokolu**: Ověřeno, že veškerá dokumentace odkazuje na aktuální MCP Specification 2025-11-25
- **Srovnání architektury**: Potvrzena správnost dokumentace dvouvrstvé architektury (Data Layer + Transport Layer)
- **Dokumentace primitiv**: Validována serverová primitiva (Resources, Prompts, Tools) a klientská primitiva (Sampling, Elicitation, Logging, Roots)
- **Mechanismy přenosu**: Ověřena správnost dokumentace STDIO a Streamable HTTP transportu
- **Bezpečnostní pokyny**: Potvrzena shoda s aktuální dokumentací osvědčených bezpečnostních postupů MCP

#### Klíčové vlastnosti MCP 2025-11-25 zdokumentovány
- **OpenID Connect Discovery**: Objevování autentizačního serveru přes OIDC
- **OAuth Client ID Metadata dokumenty**: Doporučený mechanismus registrace klienta
- **JSON Schema 2020-12**: Výchozí dialekt pro definice schémat MCP
- **Systém třídění SDK**: Formalizované požadavky na podporu a údržbu funkcí SDK
- **Struktura správy**: Formalizovány pracovní skupiny a zájmové skupiny v řízení MCP

### Hlavní aktualizace bezpečnostní dokumentace (02-Security/)

#### Integrace MCP Security Summit Workshop (Sherpa)
- **Nový interaktivní tréninkový zdroj**: Přidána komplexní integrace s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) ve všech bezpečnostních dokumentech
- **Pokrytí trasy expedice**: Zdokumentováno kompletní přesouvání z tábora do tábora od Base Campu po Summit
- **Soulad s OWASP**: Veškeré bezpečnostní pokyny nyní odpovídají rizikům z OWASP MCP Azure Security Guide

#### Integrace OWASP MCP Top 10
- **Nová sekce**: Přidána tabulka OWASP MCP Top 10 bezpečnostních rizik s mitigacemi Azure do hlavního Security README
- **Dokumentace založená na rizicích**: Aktualizován soubor mcp-security-controls-2025.md s odkazy na OWASP MCP rizika pro každou bezpečnostní doménu
- **Referenční architektura**: Propojeno s referenční architekturou a implementačními vzory OWASP MCP Azure Security Guide

#### Aktualizované bezpečnostní soubory
- **README.md**: Přidány přehled Sherpa Workshopu, tabulka trasy expedice, shrnutí OWASP MCP Top 10 rizik a sekce interaktivního tréninku
- **mcp-security-controls-2025.md**: Aktualizován nadpis na únor 2026, přidány OWASP rizikové reference (MCP01-MCP08), opravena nekonzistence ve verzi specifikace
- **mcp-security-best-practices-2025.md**: Přidána sekce zdrojů Sherpa a OWASP, aktualizováno datum
- **mcp-best-practices.md**: Přidána sekce interaktivního tréninku s odkazy na Sherpa a OWASP
- **azure-content-safety-implementation.md**: Přidána reference OWASP MCP06, sladění s Sherpa Camp 3 a dodatečná sekce zdrojů

#### Přidány nové odkazy na zdroje
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuální stránky rizik OWASP MCP (MCP01-MCP10)

### Zarovnání s celkovou specifikací MCP kurikula 2025-11-25

#### Modul 03 - Začínáme
- **Dokumentace SDK**: Přidáno Go SDK do oficiálního seznamu SDK; aktualizovány všechny odkazy na SDK pro sladění se specifikací MCP 2025-11-25
- **Upřesnění přenosu**: Aktualizovány popisy přenosů STDIO a HTTP Streaming s explicitními odkazy na specifikaci

#### Modul 04 - Praktická implementace
- **Aktualizace SDK**: Přidáno Go SDK; aktualizován seznam SDK s odkazem na verzi specifikace
- **Specifikace autorizace**: Aktualizován odkaz na MCP specifikaci autorizace na aktuální verzi 2025-11-25

#### Modul 05 - Pokročilá témata
- **Nové funkce**: Přidána poznámka o nových prvcích MCP specifikace 2025-11-25 (Úkoly, Anotace nástrojů, Elicitation režim URL, Kořeny)
- **Bezpečnostní zdroje**: Přidány odkazy na OWASP MCP Top 10 a Sherpa workshop do doplňkových referencí

#### Modul 06 - Příspěvky komunity
- **Seznam SDK**: Přidány Swift a Rust SDK; aktualizován odkaz na specifikaci na 2025-11-25
- **Odkaz na specifikaci**: Aktualizován odkaz MCP specifikace na přímou URL specifikace

#### Modul 07 - Zkušenosti z raného adopce
- **Aktualizace zdrojů**: Přidán odkaz MCP specifikace 2025-11-25 a OWASP MCP Top 10 do doplňkových zdrojů

#### Modul 08 - Nejlepší praktiky
- **Verze specifikace**: Aktualizován odkaz MCP specifikace na 2025-11-25
- **Bezpečnostní zdroje**: Přidáno OWASP MCP Top 10 a Sherpa workshop do doplňkových referencí

#### Modul 10 - Zefektivnění AI pracovních postupů
- **Aktualizace odznaku**: Změněn odznak verze MCP ze verze SDK (1.9.3) na verzi specifikace (2025-11-25)
- **Odkazy na zdroje**: Aktualizován odkaz MCP specifikace; přidán OWASP MCP Top 10

#### Modul 11 - MCP Server Hands-On Laboratoře
- **Odkaz na specifikaci**: Aktualizován odkaz MCP specifikace na verzi 2025-11-25
- **Bezpečnostní zdroje**: Přidán OWASP MCP Top 10 do oficiálních zdrojů

## 18. prosince 2025

### Aktualizace bezpečnostní dokumentace - MCP specifikace 2025-11-25

#### MCP Bezpečnostní nejlepší praktiky (02-Security/mcp-best-practices.md) - Aktualizace verze specifikace
- **Aktualizace verze protokolu**: Aktualizováno na odkaz na nejnovější MCP specifikaci 2025-11-25 (vydáno 25. listopadu 2025)
  - Aktualizovány všechny odkazy na verzi specifikace z 2025-06-18 na 2025-11-25
  - Aktualizovány datumové odkazy dokumentu z 18. srpna 2025 na 18. prosince 2025
  - Ověřeno, že všechny URL specifikací vedou na aktuální dokumentaci
- **Validace obsahu**: Kompletní validace bezpečnostních nejlepších praktik podle nejnovějších standardů
  - **Microsoft Security Solutions**: Ověřena aktuální terminologie a odkazy pro Prompt Shields (dříve "detekce rizika jailbreaku"), Azure Content Safety, Microsoft Entra ID a Azure Key Vault
  - **OAuth 2.1 bezpečnost**: Potvrzená shoda s nejnovějšími bezpečnostními praktikami OAuth
  - **OWASP standardy**: Ověřeny aktuální odkazy na OWASP Top 10 pro LLM
  - **Azure služby**: Ověřeny všechny odkazy a nejlepší praktiky Microsoft Azure dokumentace
- **Soulad se standardy**: Všechny odkazované bezpečnostní standardy potvrzeny jako aktuální
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 bezpečnostní nejlepší praktiky
  - Bezpečnostní a souladové rámce Azure
- **Implementační zdroje**: Ověřeny všechny odkazy a zdroje implementačních průvodců
  - Autentifikační vzory Azure API Management
  - Průvodce integrací Microsoft Entra ID
  - Správa tajemství v Azure Key Vault
  - DevSecOps pipeline a monitorovací řešení

### Zajištění kvality dokumentace
- **Soulad se specifikací**: Zajištěno, že všechny povinné bezpečnostní požadavky MCP (MUSÍ/MUSÍ NE) jsou v souladu s nejnovější specifikací
- **Aktuálnost zdrojů**: Ověřeny všechny vnější odkazy na Microsoft dokumentaci, bezpečnostní standardy a implementační průvodce
- **Pokrytí nejlepších praktik**: Potvrzeno komplexní pokrytí autentizace, autorizace, AI-specifických hrozeb, bezpečnosti dodavatelského řetězce a podnikových vzorů

## 6. října 2025

### Rozšíření sekce Začínáme – Pokročilé použití serveru & jednoduchá autentizace

#### Pokročilé použití serveru (03-GettingStarted/10-advanced)
- **Přidána nová kapitola**: Představen komplexní průvodce pokročilým použitím MCP serveru, pokrývající pravidelné i nízkoúrovňové architektury serveru.
  - **Pravidelný vs. nízkoúrovňový server**: Podrobná srovnání a příklady kódu v Python a TypeScript pro oba přístupy.
  - **Návrh založený na handleru**: Vysvětlení správy nástrojů/zdrojů/promptů založené na handlerech pro škálovatelné a flexibilní implementace serveru.
  - **Praktické vzory**: Reálné scénáře, kde jsou vzory nízkoúrovňového serveru prospěšné pro pokročilé funkce a architekturu.

#### Jednoduchá autentizace (03-GettingStarted/11-simple-auth)
- **Přidána nová kapitola**: Kroky pro implementaci jednoduché autentizace v MCP serverech.
  - **Koncepty autentizace**: Jasné vysvětlení rozdílu mezi autentizací a autorizací, a zacházení s přihlašovacími údaji.
  - **Implementace základní autentizace**: Middleware vzory autentizace v Python (Starlette) a TypeScript (Express) s ukázkami kódu.
  - **Pokrok k pokročilé bezpečnosti**: Návod pro začátek s jednoduchou autentizací a postup k OAuth 2.1 a RBAC, s odkazy na pokročilé moduly bezpečnosti.

Tyto doplňky poskytují praktické, praktické návody pro vytváření robustnějších, bezpečnějších a flexibilnějších implementací MCP serverů, spojující základní koncepty s pokročilými výrobními vzory.

## 29. září 2025

### MCP Server databázová integrace – Komplexní praktická cesta

#### 11-MCPServerHandsOnLabs - Nové kompletní kurikulum databázové integrace
- **Kompletní 13-laboratorní učební cesta**: Přidán komplexní praktický kurz pro budování produktových MCP serverů s integrací databáze PostgreSQL
  - **Reálná implementace**: Zava Retail analytický případ využití demonstrující podnikovou úroveň vzorů
  - **Strukturovaný postup učení**:
    - **Lab 00-03: Základy** - Úvod, jádrová architektura, bezpečnost a multi-tenancy, nastavení prostředí
    - **Lab 04-06: Stavba MCP serveru** - Návrh databáze a schéma, implementace MCP serveru, vývoj nástrojů  
    - **Lab 07-09: Pokročilé funkce** - Integrace sémantického vyhledávání, testování a ladění, integrace s VS Code
    - **Lab 10-12: Produkce a nejlepší praktiky** - Nasazovací strategie, monitoring a pozorovatelnost, nejlepší praktiky a optimalizace
  - **Podnikové technologie**: FastMCP framework, PostgreSQL s pgvector, Azure OpenAI embeddingy, Azure Container Apps, Application Insights
  - **Pokročilé funkce**: Ochrana na úrovni řádků (RLS), sémantické vyhledávání, multi-tenant přístup k datům, vektorové embeddingy, monitoring v reálném čase

#### Standardizace terminologie - Převod modulu na lab
- **Komplexní aktualizace dokumentace**: Systematicky aktualizovány všechny README soubory v 11-MCPServerHandsOnLabs na používání termínu „Lab“ místo „Modul“
  - **Nadpisy sekcí**: Aktualizováno „Co tento modul pokrývá“ na „Co tento lab pokrývá“ napříč všemi 13 laby
  - **Popis obsahu**: Změněno „Tento modul poskytuje...“ na „Tento lab poskytuje...“ v celé dokumentaci
  - **Výukové cíle**: Aktualizováno „Na konci tohoto modulu...“ na „Na konci tohoto labu...“ 
  - **Navigační odkazy**: Převod všech odkazů typu „Modul XX:“ na „Lab XX:“ v křížových referencích a navigaci
  - **Sledování dokončení**: Aktualizováno „Po dokončení tohoto modulu...“ na „Po dokončení tohoto labu...“
  - **Zachovány technické odkazy**: Zachovány odkazy na Python moduly v konfiguračních souborech (např. `"module": "mcp_server.main"`)

#### Vylepšení studijní příručky (study_guide.md)
- **Vizualizace kurikula**: Přidána nová sekce „11. Databázová integrační laboratoř“ s kompletní strukturou labů
- **Struktura repozitáře**: Aktualizováno z deseti na jedenáct hlavních sekcí s podrobným popisem 11-MCPServerHandsOnLabs
- **Pokyny pro učební cestu**: Vylepšená navigace pokrývající sekce 00-11
- **Technologická působnost**: Přidány detaily integrace FastMCP, PostgreSQL, Azure služeb
- **Výsledky učení**: Zdůrazněno vytváření produkčně připravených serverů, vzory databázové integrace a podniková bezpečnost

#### Vylepšení hlavní struktury README
- **Terminologie založená na labech**: Aktualizováno hlavní README.md v 11-MCPServerHandsOnLabs pro jednotné používání struktury „Lab“
- **Organizace učební cesty**: Jasný postup od základních konceptů přes pokročilou implementaci po produkční nasazení
- **Zaměření na praxi**: Důraz na praktické, laboratorní učení s podnikovýma vzorama a technologiemi

### Zlepšení kvality a konzistence dokumentace
- **Důraz na praktické učení**: Posílený laboratorní přístup v celé dokumentaci
- **Zaměření na podnikové vzory**: Zvýrazněny produkčně připravené implementace a podnikové bezpečnostní aspekty
- **Integrace technologií**: Kompletní pokrytí moderních Azure služeb a AI integračních vzorů
- **Postup učení**: Jasná, strukturovaná cesta od základních konceptů po produkční nasazení

## 26. září 2025

### Rozšíření případových studií - Integrace GitHub MCP Registry

#### Případové studie (09-CaseStudy/) - Zaměření na rozvoj ekosystému
- **README.md**: Výrazné rozšíření s komplexní případovou studií GitHub MCP Registry
  - **Případová studie GitHub MCP Registry**: Nová komplexní případová studie zkoumající uvedení GitHub MCP Registry v září 2025
    - **Analýza problémů**: Podrobné zpracování fragmentovaného objevování a nasazení MCP serverů
    - **Architektura řešení**: Centralizovaný přístup GitHub registry s jedním kliknutím instalace do VS Code
    - **Obchodní dopad**: Měřitelné zlepšení onboardingu vývojářů a produktivity
    - **Strategická hodnota**: Zaměření na modulární nasazení agentů a interoperabilitu nástrojů
    - **Rozvoj ekosystému**: Pozice jako základní platforma pro agentickou integraci
  - **Vylepšená struktura případových studií**: Aktualizovány všechny sedm případových studií s jednotným formátováním a komplexními popisy
    - Azure AI Travel Agents: Důraz na orchestraci multi-agentů
    - Azure DevOps Integrace: Zaměření na automatizaci pracovních postupů
    - Reálné načítání dokumentace v reálném čase: Implementace Python konzolového klienta
    - Interaktivní generátor studijního plánu: Konverzační webová aplikace Chainlit
    - Dokumentace v editoru: Integrace VS Code a GitHub Copilot
    - Azure API Management: Podnikové integrační vzory API
    - GitHub MCP Registry: Rozvoj ekosystému a komunitní platforma
  - **Komplexní závěr**: Přepsaná závěrečná sekce zdůrazňující sedm případových studií pokrývajících několik dimenzí implementace MCP
    - Podniková integrace, multi-agent orchestraci, produktivitu vývojářů
    - Rozvoj ekosystému, kategorizaci vzdělávacích aplikací
    - Rozšířené poznatky o architektonických vzorech, implementačních strategiích a nejlepších praktikách
    - Důraz na MCP jako zralý, produkčně připravený protokol

#### Aktualizace studijní příručky (study_guide.md)
- **Vizualizace kurikula**: Aktualizovaný myšlenkový mapa s začleněním GitHub MCP Registry do sekce případových studií
- **Popis případových studií**: Vylepšeno z obecného na detailní rozbor sedmi komplexních případových studií
- **Struktura repozitáře**: Aktualizována sekce 10 pro odrážení podrobného pokrytí případových studií s konkrétními implementačními detaily
- **Integrace změnového deníku**: Přidána záznamová položka 26. září 2025 dokumentující přidání GitHub MCP Registry a vylepšení případových studií
- **Aktualizace datumů**: Aktualizován časový štítek zápatí pro odraz poslední revize (26. září 2025)

### Zlepšení kvality dokumentace
- **Zvýšení konzistence**: Standardizováno formátování a struktura případových studií ve všech sedmi příkladech
- **Komplexní pokrytí**: Případové studie nyní pokrývají scénáře podnikové integrace, produktivity vývojářů a rozvoje ekosystému
- **Strategické umístění**: Zvýšený důraz na MCP jako základní platformu pro nasazení agentních systémů
- **Integrace zdrojů**: Aktualizovány doplňkové zdroje o odkaz na GitHub MCP Registry

## 15. září 2025

### Rozšíření pokročilých témat - Vlastní přenosy & kontextové inženýrství

#### Vlastní přenosy MCP (05-AdvancedTopics/mcp-transport/) - Nový pokročilý průvodce implementací
- **README.md**: Kompletní průvodce implementací vlastních přenosových mechanismů MCP
  - **Azure Event Grid přenos**: Komplexní implementace serverless event-driven přenosu
    - Příklady v C#, TypeScript a Python s integrací Azure Functions
    - Vzory event-driven architektury pro škálovatelná MCP řešení
    - Příjemci webhooků a push založená správa zpráv
  - **Azure Event Hubs přenos**: Implementace přenosu s vysokou propustností pro streamování
    - Real-time streamovací kapacity pro scénáře s nízkou latencí
    - Strategie partitioningu a správa checkpointů
    - Batching zpráv a optimalizace výkonu
  - **Podnikové integrační vzory**: Produkčně připravené architektonické příklady
    - Distribuované zpracování MCP přes více Azure Functions
    - Hybridní přenosové architektury kombinující více typů přenosů
    - Strategie trvanlivosti, spolehlivosti zpráv a zvládání chyb
  - **Bezpečnost a monitoring**: Integrace Azure Key Vault a vzory observability
    - Autentizace spravované identity a přístup s nejmenšími právy
    - Telemetrie Application Insights a monitoring výkonu
    - Circuit breakers a vzory odolnosti vůči chybám
  - **Testovací frameworky**: Kompletní testovací strategie pro vlastní přenosy
    - Jednotkové testování s testovacími dvojičkami a mocking frameworky
    - Integrační testování s Azure Test Containers
    - Úvahy o testování výkonu a zatížení

#### Kontextové inženýrství (05-AdvancedTopics/mcp-contextengineering/) - Nově vznikající disciplína AI
- **README.md**: Komplexní průzkum kontextového inženýrství jako nově vznikající oblasti
  - **Jádrové principy**: Kompletní sdílení kontextu, vědomí rozhodování akcí a správa kontextového okna

  - **Soulad protokolu MCP**: Jak návrh MCP řeší výzvy inženýrství kontextu
    - Omezení kontextového okna a strategie postupného načítání
    - Určení relevance a dynamické získávání kontextu
    - Zpracování multimodálního kontextu a bezpečnostní aspekty
  - **Implementační přístupy**: Jednovláknové vs. víceagentní architektury
    - Techniky dělení a prioritizace kontextových bloků
    - Strategie postupného načítání a komprese kontextu
    - Vícevrstvé přístupy ke kontextu a optimalizace získávání
  - **Měřicí rámec**: Nově vznikající metriky pro hodnocení efektivity kontextu
    - Úvahy o efektivitě vstupů, výkonu, kvalitě a uživatelském zážitku
    - Experimentální přístupy k optimalizaci kontextu
    - Analýza selhání a metodiky zlepšování

#### Aktualizace navigace kurikula (README.md)
- **Vylepšená struktura modulů**: Aktualizovaná tabulka kurikula o nové pokročilé témata
  - Přidány položky Inženýrství kontextu (5.14) a Vlastní transport (5.15)
  - Konzistentní formátování a odkazy na navigaci napříč všemi moduly
  - Aktualizované popisy odpovídající aktuálnímu rozsahu obsahu

### Vylepšení struktury adresářů
- **Standardizace názvů**: Přejmenování "mcp transport" na "mcp-transport" pro konzistenci s dalšími složkami pokročilých témat
- **Organizace obsahu**: Všechny složky 05-AdvancedTopics nyní dodržují konzistentní vzor pojmenování (mcp-[téma])

### Vylepšení kvality dokumentace
- **Soulad s MCP specifikací**: Veškerý nový obsah odkazuje na aktuální MCP Specifikaci 2025-06-18
- **Příklady v několika jazycích**: Kompletní ukázky kódu v C#, TypeScript a Pythonu
- **Zaměření na podnikové prostředí**: Produkčně připravené vzory a integrace Azure cloudu napříč celým obsahem
- **Vizualizace dokumentace**: Mermaid diagramy pro vizualizaci architektury a toků

## 18. srpna 2025

### Komplexní aktualizace dokumentace – standardy MCP 2025-06-18

#### Nejlepší bezpečnostní postupy MCP (02-Security/) – Kompletní modernizace
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kompletní přepsání v souladu se specifikací MCP 2025-06-18
  - **Povinné požadavky**: Přidány explicitní požadavky MUSÍ / NESMÍ dle oficiální specifikace s jasnými vizuálními indikátory
  - **12 hlavních bezpečnostních praktik**: Přestavěno z 15 položek na komplexní bezpečnostní domény
    - Bezpečnost tokenů a autentizace s integrací externího poskytovatele identity
    - Správa relací a bezpečnost transportu s kryptografickými požadavky
    - Ochrana specifická pro AI s integrací Microsoft Prompt Shields
    - Řízení přístupu a oprávnění s principem nejmenších privilegií
    - Bezpečnost obsahu a monitorování s integrací Azure Content Safety
    - Bezpečnost dodavatelského řetězce s komplexní verifikací komponent
    - OAuth bezpečnost a prevence zneužití zprostředkovatele s implementací PKCE
    - Reakce na incidenty a obnovy s automatizovanými možnostmi
    - Soulad a správa s regulativním sladěním
    - Pokročilá bezpečnostní opatření s architekturou zero trust
    - Integrace Microsoft bezpečnostního ekosystému s komplexními řešeními
    - Neustálý vývoj bezpečnosti s adaptivními praktikami
  - **Microsoft bezpečnostní řešení**: Vylepšené integrační pokyny pro Prompt Shields, Azure Content Safety, Entra ID a GitHub Advanced Security
  - **Implementační zdroje**: Kategorizované komplexní odkazy podle oficiální MCP dokumentace, Microsoft bezpečnostních řešení, bezpečnostních standardů a implementačních průvodců

#### Pokročilá bezpečnostní opatření (02-Security/) – Podniková implementace
- **MCP-SECURITY-CONTROLS-2025.md**: Kompletní restrukturalizace s podnikově orientovaným bezpečnostním rámcem
  - **9 komplexních bezpečnostních domén**: Rozšířeno z základních opatření na detailní podnikový rámec
    - Pokročilá autentizace a autorizace s integrací Microsoft Entra ID
    - Bezpečnost tokenů a kontrol proti průchodu s komplexní validací
    - Kontroly bezpečnosti relací s prevencí únosů
    - Bezpečnostní kontroly specifické pro AI s prevencí injekcí promptů a kontaminace nástrojů
    - Prevence útoku „confused deputy“ s bezpečností proxy OAuth
    - Bezpečnost spouštění nástrojů s sandboxingem a izolací
    - Kontroly dodavatelského řetězce s verifikací závislostí
    - Kontroly monitorování a detekce s integrací SIEM
    - Reakce na incidenty a obnovy s automatizovanými možnostmi
  - **Příklady implementace**: Přidány detailní YAML konfigurační bloky a ukázky kódu
  - **Integrace Microsoft řešení**: Kompletní pokrytí bezpečnostních služeb Azure, GitHub Advanced Security a správy podnikové identity

#### Pokročilá témata – bezpečnost (05-AdvancedTopics/mcp-security/) – Produkčně připravená implementace
- **README.md**: Kompletní přepsání pro podnikovou bezpečnostní implementaci
  - **Soulad s aktuální specifikací**: Aktualizováno na MCP Specifikaci 2025-06-18 s povinnými bezpečnostními požadavky
  - **Vylepšená autentizace**: Integrace Microsoft Entra ID s komplexními příklady .NET a Java Spring Security
  - **Integrace AI bezpečnosti**: Implementace Microsoft Prompt Shields a Azure Content Safety s detailními příklady v Pythonu
  - **Pokročilé zmírnění hrozeb**: Komplexní příklady implementace pro
    - Prevence útoků „confused deputy“ s PKCE a validací uživatelského souhlasu
    - Prevence průchodu tokenů s validací publika a bezpečnou správou tokenů
    - Prevence únosu relace s kryptografickým vázáním a behaviorální analýzou
  - **Integrace podnikové bezpečnosti**: Monitoring Azure Application Insights, pipeline detekce hrozeb a bezpečnost dodavatelského řetězce
  - **Implementační kontrolní seznam**: Jasné rozlišení povinných vs. doporučených bezpečnostních opatření s výhodami Microsoft bezpečnostního ekosystému

### Kvalita dokumentace a soulad se standardy
- **Odkazy na specifikace**: Aktualizovány všechny odkazy na aktuální MCP Specifikaci 2025-06-18
- **Microsoft bezpečnostní ekosystém**: Vylepšené pokyny pro integraci napříč celou bezpečnostní dokumentací
- **Praktická implementace**: Přidány detailní příklady kódu v .NET, Java a Python s podnikatelskými vzory
- **Organizace zdrojů**: Komplexní kategorizace oficiální dokumentace, bezpečnostních standardů a implementačních průvodců
- **Vizualní indikátory**: Jasné označení povinných požadavků vůči doporučeným praktikám


#### Základní koncepty (01-CoreConcepts/) – Kompletní modernizace
- **Aktualizace verze protokolu**: Aktualizováno na odkazování na aktuální MCP Specifikaci 2025-06-18 s verzováním podle data (formát RRRR-MM-DD)
- **Upřesnění architektury**: Vylepšené popisy Hostitelů, Klientů a Serverů pro odraz aktuálních vzorů architektury MCP
  - Hostitelé nyní jasně definováni jako AI aplikace koordinující více uživatelských klientských připojení MCP
  - Klienti popisováni jako protokolové konektory udržující vztahy jeden na jednoho se servery
  - Servery vylepšeny o scénáře lokálního vs. vzdáleného nasazení
- **Přestavba primitiv**: Kompletní restrukturalizace serverových a klientských primitiv
  - Serverové primitivy: Zdroje (datové zdroje), Prompt (šablony), Nástroje (spustitelné funkce) s detailními vysvětleními a příklady
  - Klientské primitivy: Vzorkování (dokončení LLM), Vytváření (uživatelský vstup), Protokolování (debugování/monitorování)
  - Aktualizace s aktuálními vzory metod pro vyhledávání (`*/list`), získávání (`*/get`) a vykonávání (`*/call`)
- **Architektura protokolu**: Zaveden dvouvrstvý model architektury
  - Datová vrstva: Základ JSON-RPC 2.0 s řízením životního cyklu a primitivy
  - Transportní vrstva: STDIO (lokální) a Streamable HTTP s SSE (vzdálený) transportní mechanismy
- **Bezpečnostní rámec**: Komplexní bezpečnostní principy včetně explicitního uživatelského souhlasu, ochrany soukromí dat, bezpečnosti spuštění nástrojů a bezpečnosti transportní vrstvy
- **Komunikační vzory**: Aktualizované zprávy protokolu ukazující inicializační, vyhledávací, vykonávací a notifikační toky
- **Ukázky kódu**: Oživení příkladů pro více jazyků (.NET, Java, Python, JavaScript) odrážející aktuální vzory MCP SDK

#### Bezpečnost (02-Security/) – Kompletní bezpečnostní restrukturalizace  
- **Soulad se standardy**: Plný soulad s bezpečnostními požadavky MCP Specifikace 2025-06-18
- **Vývoj autentizace**: Zdokumentovaná evoluce od vlastních OAuth serverů k delegaci externímu poskytovateli identity (Microsoft Entra ID)
- **Analýza hrozeb specifických pro AI**: Rozšířené pokrytí moderních AI útoků
  - Detailní scénáře útoků injekce promptů s reálnými příklady
  - Mechanismy kontaminace nástrojů a vzory útoků typu "rug pull"
  - Poškození kontextového okna a útoky záměny modelu
- **Microsoft AI bezpečnostní řešení**: Komplexní pokrytí Microsoft bezpečnostního ekosystému
  - AI Prompt Shields s pokročilou detekcí, zvýrazňováním a technikami oddělování
  - Vzory integrace Azure Content Safety
  - GitHub Advanced Security pro ochranu dodavatelského řetězce
- **Pokročilé zmírnění hrozeb**: Podrobné bezpečnostní kontroly pro
  - Únos relace s MCP-specifickými scénáři útoků a požadavky na kryptografické ID relace
  - Problémy „confused deputy“ v MCP proxy scénářích s explicitními požadavky na souhlas
  - Zranitelnosti průchodu tokenů s povinnými validačními kontrolami
- **Bezpečnost dodavatelského řetězce**: Rozšířené pokrytí AI dodavatelského řetězce včetně základních modelů, embedding služeb, poskytovatelů kontextu a třetích stran API
- **Základní bezpečnost**: Vylepšená integrace s podnikatelskými bezpečnostními vzory včetně architektury zero trust a Microsoft bezpečnostního ekosystému
- **Organizace zdrojů**: Kategorie komplexních odkazů podle typu (Oficiální dokumenty, standardy, výzkum, Microsoft řešení, implementační průvodce)

### Vylepšení kvality dokumentace
- **Strukturované vzdělávací cíle**: Vylepšené vzdělávací cíle se specifickými a akčními výsledky
- **Křížové odkazy**: Přidány odkazy mezi souvisejícími tématy bezpečnosti a základních konceptů
- **Aktuální informace**: Aktualizovány všechny datové odkazy a odkazy na specifikace na současné standardy
- **Pokyny k implementaci**: Přidány specifické a akční implementační směrnice v obou sekcích

## 16. července 2025

### Vylepšení README a navigace
- Kompletně přepracována navigace kurikula v README.md
- Nahrazeny značky `<details>` přístupnějším formátem založeným na tabulkách
- Vytvořeny alternativní možnosti rozložení ve složce "alternative_layouts"
- Přidány příklady navigace založené na kartách, záložkách a akordeonu
- Aktualizována sekce struktury repozitáře o všechny nejnovější soubory
- Vylepšena sekce „Jak používat toto kurikulum“ s jasnými doporučeními
- Aktualizovány odkazy na specifikaci MCP tak, aby směřovaly na správné URL
- Přidána sekce Inženýrství kontextu (5.14) do struktury kurikula

### Aktualizace studijní příručky
- Kompletně přepracována studijní příručka pro sladění s aktuální strukturou repozitáře
- Přidány nové sekce pro MCP klienty a nástroje a populární MCP servery
- Aktualizována vizuální mapa kurikula pro přesné zobrazení všech témat
- Vylepšeny popisy pokročilých témat pro pokrytí všech specializovaných oblastí
- Aktualizována sekce případových studií, aby reflektovala aktuální příklady
- Přidán tento komplexní changelog

### Příspěvky komunity (06-CommunityContributions/)
- Přidány detailní informace o MCP serverech pro generování obrázků
- Přidána komplexní sekce o použití Claude ve VSCode
- Přidány pokyny pro nastavení a používání klienta terminálu Cline
- Aktualizována sekce MCP klientů zahrnující všechny populární klientské možnosti
- Vylepšeny příklady příspěvků s přesnějšími ukázkami kódu

### Pokročilá témata (05-AdvancedTopics/)
- Organizovány všechny specializované tématické složky s konzistentním pojmenováním
- Přidány materiály a příklady inženýrství kontextu
- Přidána dokumentace integrace agenta Foundry
- Vylepšena dokumentace integrace bezpečnosti Entra ID

## 11. června 2025

### První vytvoření
- Vydána první verze kurikula MCP pro začátečníky
- Vytvořena základní struktura pro všech 10 hlavních sekcí
- Implementována vizuální mapa kurikula pro navigaci
- Přidány úvodní ukázkové projekty v několika programovacích jazycích

### Začínáme (03-GettingStarted/)
- Vytvořeny první příklady implementace serveru
- Přidány pokyny k vývoji klienta
- Zahrnuty instrukce integrace klienta LLM
- Přidána dokumentace integrace VS Code
- Implementovány příklady serveru podporujícího Server-Sent Events (SSE)

### Základní koncepty (01-CoreConcepts/)
- Přidán detailní popis architektury klient-server
- Vytvořena dokumentace klíčových komponent protokolu
- Zdokumentovány vzory zpráv v MCP

## 23. května 2025

### Struktura repozitáře
- Inicializováno repozitář se základní strukturou složek
- Vytvořeny README soubory pro každou hlavní sekci
- Nastavena infrastruktura pro překlady
- Přidány obrazové assety a diagramy

### Dokumentace
- Vytvořen počáteční README.md s přehledem kurikula
- Přidány soubory CODE_OF_CONDUCT.md a SECURITY.md
- Nastaven SUPPORT.md s návody na získání pomoci
- Vytvořena předběžná struktura studijní příručky

## 15. dubna 2025

### Plánování a rámec
- Počáteční plánování kurikula MCP pro začátečníky
- Definovány vzdělávací cíle a cílové publikum
- Nastíněna struktura kurikula v 10 sekcích
- Vyvinut konceptuální rámec pro příklady a případové studie
- Vytvořeny první prototypové příklady klíčových konceptů

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->