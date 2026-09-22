# Dnevnik sprememb: MCP za začetnike kurikuluma

Ta dokument služi kot zapis vseh pomembnih sprememb, narejenih na kurikulumu Model Context Protocol (MCP) za začetnike. Spremembe so dokumentirane v obratnem kronološkem vrstnem redu (najnovejše spremembe prve).

## 9. september 2026

### MCP 2026-07-28 končna poravnava specifikacije

Posodobljen angleški kurikulum iz izdaje kandidata in referenčnih navodil `2025-11-25`
na končno MCP `2026-07-28` specifikacijo.

- **Posodobljeno**: reference na trenutno verzijo, povezave do specifikacije, navodila za brezdržavne
  zahtevke, `server/discover`, pretočne HTTP glave (Streamable HTTP headers) in življenjski cikel razširitve Tasks
  skozi 38 angleških dokumentacijskih datotek.
- **Popravljeno**: Elicitation zdaj uporablja `elicitation/create`, Sampling uporablja
  `sampling/createMessage`, in `InputRequiredResult.resultType` uporablja
  `"input_required"`.
- **Zamenjano**: Netočna lekcija o stanju pogovora Root Context z natančno lekcijo o koreninah,
  ki pokriva informativne namige datotečnega sistema, trenutni tok z več krogi,
  varnostne meje in možnosti migracije.
- **Poenostavljeno**: Roots, Sampling, Logging in Dynamic Client Registration so
  označeni kot zastareli v `2026-07-28`, s priporočenimi zamenjavami in najzgodnejšim
  datumom odstranitve dokumentirano.
- **Označeno**: Primeri, ki se še vedno zanašajo na MCP `2025-11-25`, HTTP+SSE,
  inicializacijske rokovanja ali protokolarne seje so ohranjeni kot primeri za
  združljivost z zapuščino, namesto da bi bili predstavljeni kot trenutne implementacije.
- **Varnostna navodila**: Posodobljeni samostojni varnostni vodiči za uporabo
  avtentikacije na zahtevek in eksplicitne ročaje stanja aplikacije namesto
  odstranjenih ID-jev sej protokola. Dokumenti metapodatkov ID stranke so zdaj
  prednostna pot registracije, DCR pa je dokumentiran kot samo za združljivost.
- **Podporni materiali**: Posodobljeni študijski vodič, kontrolni seznam prispevkov,
  študija primera Publora in študija primera APIM. Namigovanje APIM zdaj priporoča
  svojo trenutno pretočno HTTP `/mcp` končno točko namesto zastarelega `/sse`.
- **Kanonične povezave**: Zamenjane upokojene in osnutkovne URL-je specifikacij v angleškem
  izvoru Markdown z verziranimi povezavami `2026-07-28`, ob ohranitvi eksplicitnih
  povezav do starejših različic, kjer vzorec ostaja pritrjen na starejša orodja.
- **Stabilna imena datotek**: Preimenovan končni vodnik specifikacije in dva varnostna
  vodiča za odstranjevanje priponk kandidata za izdajo in letnic, nato pa posodobljene vse angleške
  hiperpovezave na njihove stabilne poti.
- **Nov avtentikacijski vzorec**: Dodan preizkušen
  [TypeScript MCP `2026-07-28` strežnik virov](./02-Security/samples/cimd-dcr-auth/README.md),
  ki primerja prednostne dokumente metapodatkov ID stranke z zastarelo
  dinamično registracijo strank (Dynamic Client Registration) kot rezervno možnostjo. Vzorec vključuje odkrivanje RFC 9728, preverjanje JWKS,
  območja za vsako orodje, dvanajst testov in vodnik nastavitve Auth0.
- **Obseg prevoda**: Urejene so bile le angleške izvorne datoteke; generirani
  prevodi in prevedene slike ostajajo nespremenjeni, saj so samodejno prevedeni.

## 29. julij 2026

### Novi modul 08 spremljevalec: Zanesljivi stranski avtomobili (reliability sidecars) in varni ponovni poskusi

Dodana nevtralna spremljevalna lekcija za orodja MCP, ki ustvarjajo učinke v realnem svetu,
usklajena s končno `2026-07-28` specifikacijo.

- **Novo**: [Spremljevalna lekcija zanesljivosti][reliability-sidecar]
  uporablja eno zgodbo o podporni vozovnici, dva Mermaid diagramov in tok odločanja
  pri ponovnem poskusu za razlago stabilnih ključev operacij, atomske podvojitve vstopa,
  usklajevanja, dokazov in meje razširitve Tasks.
- **Novo**: Vaja za vbrizgavanje napak v Python standardni knjižnici in SQLite
  uporablja ločene zbirk operacij in vozovnic, da prikaže primer izgubljenega odziva
  po potrditvi zunanjega učinka. Šest determinističnih testov pokriva naivno
  podvajanje, zaščiteno obnovo ponovnega zagona, konflikte s podatki, predpomnjene rezultate,
  aktivne zahtevke in konkurentno podvajanje vstopa.
- **Posodobljeno**: Modul 08 zdaj povezuje spremljevalno lekcijo, identificira
  končni `2026-07-28` model brezdržavnih zahtevkov, razlikuje OpenTelemetry
  opazljivost od zastarele funkcije beleženja MCP in omejuje svoj
  generični primer ponovnega poskusa na samo operacije za branje.
- **Neobvezno**: Lekcija preslika svoje prenosljive koncepte na eno označeno skupnostno
  implementacijo brez, da bi gostujočo storitev ali omrežni klic naredila del
  vaje.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. julij 2026

### Nova lekcija: Kandidat za izdajo MCP specifikacije 2026-07-28

Dodano pokrivanje prihajajočega kandidata za izdajo MCP specifikacije `2026-07-28` (objavljeno 21. maja 2026; končna izdaja predvidena za 28. julij 2026), povzeto iz [uradnega blog zapisa](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Osnovna raven kurikuluma ostaja **MCP specifikacija 2025-11-25** dokler nova verzija ne izide, zato je to predstavljeno kot napoved v prihodnost, ne kot prepis obstoječih lekcij.

- **Novo**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — celovita lekcija, ki pokriva brezdržavno jedro protokola (odstranitev rokovanja `initialize` in `Mcp-Session-Id`), nove glave za usmerjanje `Mcp-Method`/`Mcp-Name`, metapodatke predpomnjenja `ttlMs`/`cacheScope`, W3C Trace Context v `_meta`, formalni okvir razširitev (MCP aplikacije in nova razširitev Tasks), šest SEP-jev za utrjevanje avtentikacije, opustitev Roots/Sampling/Logging, ter prehod na polni JSON Schema 2020-12 za sheme orodij.
- **Posodobljeno** s klici usmerjenih naprej, ki povezujejo na novo lekcijo:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): opomba o različici protokola, poglavja Sampling/Roots/Logging/Tasks in "Kaj sledi"
  - [02-Security/README.md](./02-Security/README.md): opomba o utrjevanju avtentikacije
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): opomba o brezdržavnem prenosu
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): opomba o opustitvi Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): opustitev Logging in razširitev Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): opomba o brezdržavnem/usmerjanju sej
  - [README.md](./README.md): opomba "Gledanje naprej" v oddelku specifikacij in nova vnos `1.1` v tabeli modulov kurikuluma
  - [study_guide.md](./study_guide.md): naprek usmerjena pika v pregledu osnovnih konceptov in datirana dodatek opomba
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): opomba o `mcp-session-id` transportni mapi pred brezdržavnim modelom zahtevkov
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): klic modula o opustitvah Root Contexts/Sampling in razširitvi Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): opomba o utrjevanju avtentikacije

## 24. junij 2026

### Nova lekcija: Uporaba MCP v aplikaciji Copilot

- Dodan [oddelek za orodja](./12-tooling/README.md).
- [MCP v aplikaciji Copilot](./12-tooling/01-copilot-app/README.md)

## 16. junij 2026

### Poravnava MCP specifikacije in validacija vzorcev

Validiran kurikulum glede na trenutno **MCP specifikacijo 2025-11-25** in zadnje uradne SDK-je, nato popravljene ostale zastarele reference do specifikacije in potrjeno, da jedrni vzorci še vedno gradijo in delujejo.

#### Popravki različice specifikacije (2025-06-18 / 2025-03-26 → 2025-11-25)

Posodobljena angleška vsebina tam, kjer je še vedno trdila, da je starejša različica specifikacije aktualni/končni standard, in preusmerjene povezave na kanonične poti specifikacije `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Posodobljen trak "Trenutni standard", uvod, naslov jedrnih varnostnih načel, naslov obveznih zahtev, odsek Microsoft Entra ID, povezave do referenc in virov ter zaključna varnostna obvestila (8 referenc) na 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Posodobljena povezava do dodatnih virov in trak "Trenutni standard" na 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Zamenjana zastarela povezava o varnosti in zaupanju `2025-03-26` s trenutnim dokumentom najboljših varnostnih praks 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Posodobljena uradna povezava do dokumentacije Sampling na 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Posodobljena sklicevanja na "trenutno MCP specifikacijo" v sedanjiku in povezava do dodatnih virov na 2025-11-25 (zgodovinski zapiski o opuščanju SSE so ohranjeni zaradi natančnosti)

#### Validacija vzorcev na trenutnih SDK-jih

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` rešil `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` je uspel brez tipnih napak — obstoječi API-ji `McpServer`/`StdioServerTransport` ostajajo veljavni
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validirano v izoliranem `.venv` z `mcp[cli]` (1.27.2); `py_compile` je uspel in `FastMCP.list_tools()` je pravilno vrnil orodji `add` in `subtract`
- Potrjeno, da vsi vzorci `@modelcontextprotocol/sdk` različični razponi (`>=1.26.0` / `^1.26.0` / `^1.27.0`) brezhibno rešujejo na trenutno `1.29.0` brez sprememb v API, ki bi prekinile združljivost

#### Poravnava zaklepanja odvisnosti (zapiranje različičnih vrzeli)

Povišani zastareli SDK zaklepi, da vsak vzorec sledi trenutni izdaji MCP, kar sledi konvenciji celotnega repozitorija:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Povišan `@modelcontextprotocol/sdk` iz `^1.8.0` → `>=1.26.0` in posodobljen zastareli opis paketa `"updated for MCP 2025-06-18"` v `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** in **lab4/code/github_mcp_server/pyproject.toml**: Povišan točen zaklep `mcp==1.23.0` → `mcp>=1.26.0`; ponovno generirani oba datoteki `uv.lock` (`uv lock`), tako da zaklepi rešujejo na trenutno `mcp 1.27.2` in ostajajo usklajeni z manifesti

#### Analiza vrzeli kurikuluma — pokritost najnovejše funkcionalnosti specifikacije

Preverjeno, da kurikulum že pokriva vse primitive, uvedene ali razširjene v MCP 2025-11-25, zato ni vrzeli v vsebini:
- **Sampling**: lekcija 03-GettingStarted/14-sampling in 05-AdvancedTopics/mcp-sampling
- **Elicitation (vključno z načinom URL)**: dokumentirano v 01-CoreConcepts in 05-AdvancedTopics/mcp-protocol-features
- **Roots**: dokumentirano v 00-Introduction, 01-CoreConcepts in 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimentalne, dolgotrajne operacije)**: dokumentirano v 01-CoreConcepts in 05-AdvancedTopics/mcp-protocol-features
- **Oznake orodij** (`readOnlyHint` / `destructiveHint`): dokumentirano v 01-CoreConcepts in 05-AdvancedTopics/mcp-protocol-features

### Krepitev varnosti in odprava ranljivosti odvisnosti

Izveden je bil celovit varnostni pregled vseh manifestov odvisnosti in izvorne kode vzorcev, nato odpravljene vse prijavljene varnostne pomanjkljivosti npm in ena najdba na ravni kode. Po odpravi `npm audit` poroča o **0 ranljivostih** v vsakem pregledanem imeniku.

#### Ranljivosti odvisnosti npm (transitivne) — odpravljeno

Pregledanih vseh 15 predanih datotek `package-lock.json`. Ranljivosti so bile omejene na tranzitivne odvisnosti, pridobljene z razvojnih orodjem MCP Inspector, odjemalcem OpenAI in MCP SDK; vse so zdaj odpravljene brez prelomov pri vzorcih:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** in **lab3/code/weather_mcp/inspector**: Nadgradil `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), kar je odpravilo pripete varnostne težave `ajv`, `brace-expansion`, `diff`, `path-to-regexp` in `ws`. Dodan vnos npm `overrides`, ki prisili popravljeno različico `shell-quote@1.8.4` za odpravo preostale kritične varnostne opozorilne informacije pri `concurrently`; obe ključavnični datoteki ponovno generirani (zdaj 0 ranljivosti)
- **03-GettingStarted/samples/typescript**: `npm audit fix` je posodobil prehodno odvisnost `qs` (srednja resnost) na popravljeno izdajo
- **03-GettingStarted/samples/javascript**: `npm audit fix` je posodobil prehodno odvisnost `hono` (srednja resnost) na popravljeno izdajo
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` je posodobil prehodno odvisnost `form-data` (visoka resnost) na popravljeno izdajo
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generirana manjkajoča `package-lock.json`, da je projekt reproducibilen in preverljiv (0 ranljivosti)

#### Popravek varnosti na ravni kode (OWASP A03: Injekcija)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Odstranjen `shell=True` iz orodja `open_in_vscode`. Prejšnji `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` je dovoljeval interpretacijo lupinskih metaznakov v poti mape preko `cmd.exe` (vektor za vbrizgavanje ukazov). Zdaj se neposredno zažene rešena `Code.exe` z mapo kot argumentom — brez lupine — kar je funkcionalno enakovredno in varno

#### Python revizija odvisnosti

- Revidirani vsi Python zahtevi z `pip-audit`. `05-AdvancedTopics` in `03-GettingStarted/samples/python` nista poročala o **nobeni znani ranljivosti** (njihovi `mcp` / `httpx` / `pydantic` / `python-dotenv` različice kažejo na trenutno popravljene izdaje)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` je zaznal prehodno odvisnost **`werkzeug` 3.1.1** s tremi varnostnimi ranljivostmi DoS zaradi `safe_join` Windows naprav (ime naprave) — `CVE-2025-66221`, `CVE-2026-21860` in `CVE-2026-27199` (vse popravljeno v 3.1.6). Dodan ekspliciten varnostni pin `werkzeug>=3.1.6`, da se reši popravljena izdaja; preverjeno, da omejitev pravilno deluje z `chainlit` / `mcp` / `semantic-kernel` skladom

### Preimenovanje imena izdelka

Posodobljena vsa učna vsebina za odraz preimenovanja izdelka podjetja Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Posodobljen povezava do skupnosti Discord
- **AGENTS.md**: Posodobljena referenca strežnika Discord
- **README.md**: Posodobljene reference tehnologijskega ekosistema
- **study_guide.md**: Posodobljene reference študije primera
- **05-AdvancedTopics/README.md**: Posodobljen naslov in opis modula 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Posodobljen naslov razdelka in opis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Popolna posodobitev naslova modula in vsebine
- **05-AdvancedTopics/mcp-security-entra/README.md**: Posodobljena navzkrižna povezava
- **07-LessonsfromEarlyAdoption/README.md**: Posodobljene reference študije primera
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Posodobljen naslov poglavja 9, značke in zmožnosti
- **08-BestPractices/README.md**: Posodobljen povezava do skupnosti Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Posodobljena referenca kanala Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Posodobljena referenca uvajanja modela
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Posodobljena tabela AI storitev
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Posodobljene reference virov

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension za VS Code
- **README.md**: Posodobljene glavne reference kurikuluma
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Posodobljen naslov modula, pregled in vsi naslovi modulov
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Posodobljen naslov, učni cilji, navodila za nastavitev in viri
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Posodobljen naslov, učni cilji, tabela gostiteljev MCP ter navzkrižne reference
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Posodobljen naslov, značke, predpogoji in viri
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Posodobljene reference Agent Builder in povezava za povratne informacije
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Posodobljeni predpogoji in reference razširitve

---

## 11. april 2026

### Nova lekcija, popravki dokumentacije in posodobitve odvisnosti

#### Dodana nova učna vsebina

**Modul 05 - Napredne teme**
- **Lekcija 5.17: Adverzarno večagentno sklepanje z MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nova celovita vodič, ki pokriva vzorec adverzarne debate za večagentne sisteme
  - Mermaid diagram arhitekture: dva agenta → skupni MCP strežnik → zapis debate → sodnik → razsodba
  - Skupni strežnik orodij MCP (`web_search` + `run_python`) izveden v Pythonu in TypeScriptu
  - Sistemski opozori nasprotnih strani (ZA / PROTI / Sodnik) z eksplicitnimi zahtevami po uporabi orodij
  - Orkestrator debate v Pythonu, TypeScriptu in C# za upravljanje rund in usmerjanje argumentov
  - MCP `ClientSession` povezava za orkestrator za pristne klice orodij
  - Tabela primerov uporabe (odkrivanje halucinacij, modeliranje groženj, pregled zasnove API, preverjanje dejstev, izbira tehnologije)
  - Varstvene premisleke: zagon v peskovniku, validacija klicev orodij, omejevanje hitrosti, zapisovanje revizije
  - Strukturirana vaja s tremi praktičnimi scenariji (pregled kode, arhitekturne odločitve, moderacija vsebin)

#### Popravki dokumentacije

**Modul 03 - Začetek**
- **05-stdio-server/README.md**: Popravljena nepopolna primer TypeScript stdio strežnika — dodan manjkajoči transport (`new StdioServerTransport()`) in klic `server.connect(transport)`, da se ujema s primeri v Pythonu in .NET v istem poglavju
- **14-sampling/README.md**: Popravljena tipkarska napaka — popravljeno `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Posodobitve kurikuluma

**Glavni README.md**
- Dodan vnos 5.17 (Adverzarno večagentno sklepanje z MCP) v tabelo kurikuluma s direktno povezavo do nove lekcije

**05-AdvancedTopics/README.md**
- Dodana vrstica lekcije 5.17 v tabelo lekcij

**study_guide.md**
- Dodana tema Adverzarno večagentno sklepanje na miselni zemljevid in opis proze Naprednih tem

#### Popravki kode in varnosti

**Modul 05 - Adverzarni agenti (`mcp-adversarial-agents`)**
- **Varnostni popravek — vbrizgavanje ukazov**: Nadomeščen `execSync` shell interpolacija z `execFile` + `promisify` v TypeScript orodju `run_python`, s čimer je odstranjen vektor za vbrizgavanje ukazov (koda, ki jo upravlja LLM, je zdaj posredovana kot dobesedni argv element brez sodelovanja lupine)
- **Ožičenje zanke MCP orodij**: Posodobljen Python orkestrator debate za uporabo `AsyncAnthropic` klienta (namesto blokirajočega sinhronega `Anthropic`), neposredno posredovanje žive `ClientSession` za vsak obrat agenta, pridobivanje definicij orodij preko `session.list_tools()` vsak obrat, in pošiljanje blokov `tool_use` preko `session.call_tool()` v zanki, dokler model ne odda končnega besedilnega odziva

#### Posodobitve odvisnosti

- Nadgrajen `hono` na 4.12.12 v več paketih (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Nadgrajen `@hono/node-server` iz 1.19.11 na 1.19.13 v TypeScript paketih
- Nadgrajen `cryptography` iz 46.0.5 na 46.0.7 v Python paketih (10-StreamliningAIWorkflows laboratoriji 3 in 4)
- Nadgrajen `lodash` iz 4.17.23 na 4.18.1 v 10-StreamliningAIWorkflows inspector

#### Prevodi

- Sinhronizirani prevodi za 48+ jezikov z najnovejšimi spremembami vira (i18n posodobitev)

---

## 5. februar 2026

### Izboljšave validacije in navigacije celotnega skladišča

#### Dodana nova učna vsebina

**Modul 03 - Začetek**
- **12-mcp-hosts/README.md**: Nov obsežen vodič za nastavitev gostiteljev MCP
  - Konfiguracijski primeri za Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON konfiguracijske predloge za vse glavne gostitelje
  - Primerjalna tabela vrst prevozov (stdio, SSE/HTTP, WebSocket)
  - Reševanje pogostih težav z povezavo
  - Najboljše varnostne prakse za nastavitve gostiteljev

- **13-mcp-inspector/README.md**: Novi vodič za odpravljanje napak MCP Inspectorja
  - Metode namestitve (npx, globalni npm, iz vira)
  - Povezovanje do strežnikov preko stdio in HTTP/SSE
  - Orodja za testiranje, viri in poteki pozivov
  - Integracija VS Code z MCP Inspectorjem
  - Pogosti scenariji odpravljanja napak z rešitvami

**Modul 04 - Praktična implementacija**
- **pagination/README.md**: Novi vodič za paginacijo
  - Vzorec paginacije na osnovi kurzorja v Pythonu, TypeScriptu, Javi
  - Upravljanje paginacije na odjemalcu
  - Strategije oblikovanja kurzorja (neprozoren vs. strukturiran)
  - Priporočila za optimizacijo zmogljivosti

**Modul 05 - Napredne teme**
- **mcp-protocol-features/README.md**: Globinski vpogled v funkcije protokola
  - Implementacija obvestil o napredku
  - Vzorec preklica zahtevkov
  - Predloge virov z vzorci URI
  - Upravljanje življenjskega cikla strežnika
  - Nadzor nivoja beleženja
  - Vzorec ravnanja z napakami z JSON-RPC kodami

#### Popravki navigacije (posodobljenih 24+ datotek)

**Glavni Module README-ji**
 Zdaj povezave na prvo lekcijo IN naslednji modul

**02-Security pod-datoteke**
- Vseh 5 dopolnilnih varnostnih dokumentov ima zdaj navigacijo "Kaj sledi":

**09-CaseStudy datoteke**
- Vse datoteke študije primera imajo zdaj zaporedno navigacijo:

**10-StreamliningAI laboratoriji**
Dodan odsek "Kaj sledi" v pregleda Modula 10 in Modul 11

#### Popravki kode in vsebine

**Posodobitve SDK in odvisnosti**
Popravljena prazna različica openai na `^4.95.0`
Nadgrajen SDK iz `^1.8.0` na `>=1.26.0`
Posodobljene različice MCP pinov na `>=1.26.0`

**Popravki kode**
Popravljena neveljavna različica modela `gpt-4o-mini` v `gpt-4.1-mini`

**Popravki vsebine**
Popravljena pokvarjena povezava `READMEmd` → `README.md`, popravljena glava kurikuluma `Module 1-3` → `Module 0-3`, popravljena pot, občutljiva na velike in male črke
Odstranjena poškodovana podvojena vsebina študije primera 5

**Izboljšave za začetnike**
Dodani pravi uvod, učni cilji in predpogoji za začetnike

#### Posodobitve kurikuluma

**Glavni README.md**
- Dodani vnosi 3.12 (MCP Gostitelji), 3.13 (MCP Inspector), 4.1 (Paginacija), 5.16 (Funkcije protokola) v tabelo kurikuluma

**README-ji modulov**
Dodani lekciji 12 in 13 na seznam lekcij
Dodan odsek Praktični vodiči s povezavo do paginacije
Dodani lekciji 5.15 (Prilagojen transport) in 5.16 (Funkcije protokola)

**study_guide.md**
- Posodobljen miselni zemljevid z vsemi novimi temami: nastavitev MCP gostiteljev, MCP inspector, strategije paginacije, globinski vpogled v funkcije protokola

## 28. januar 2026

### Pregled skladnosti specifikacije MCP 2025-11-25

#### Izboljšave osnovnih konceptov (01-CoreConcepts/)
- **Nova primitivna funkcija odjemalca - Roots**: Dodana obsežna dokumentacija o primitivni funkciji Roots za odjemalce, ki omogoča strežnikom razumevanje meja datotečnega sistema in dovoljenj dostopa
- **Orodne anotacije**: Dodana dokumentacija o obnašanju orodij (napotki `readOnlyHint`, `destructiveHint`) za boljše odločitve pri izvajanju orodij
- **Klic orodij pri vzorčenju**: Posodobljena dokumentacija za Sampling, ki vključuje parametra `tools` in `toolChoice` za modelom vodene klice orodij med zahtevki vzorčenja
- **Eliciation URL načina**: Dodana dokumentacija za sprožanje zunanjih spletnih interakcij, ki jih začne strežnik, preko URL načinov
- **Naloge (eksperimentalno)**: Dodan nov odsek z dokumentacijo eksperimentalne funkcije Naloge za žive ovojnice izvajanja in odloženo pridobivanje rezultatov

- **Podpora za ikone**: Opaženo, da orodja, viri, predloge virov in pozivi zdaj lahko vključujejo ikone kot dodatne metapodatke

#### Posodobitve dokumentacije
- **README.md**: Dodana referenca verzije MCP specifikacije 2025-11-25 in razlaga verzioniranja na podlagi datuma
- **study_guide.md**: Posodobljen zemljevid učnega načrta za vključitev Opravkov in Oznak orodij v razdelek Temeljni koncepti; posodobljen časovni žig dokumenta

#### Preverjanje skladnosti s specifikacijo
- **Verzija protokola**: Preverjeno, da vsa dokumentacija sklicuje na trenutno MCP specifikacijo 2025-11-25
- **Usklajenost arhitekture**: Potrjena točnost dokumentacije dvoslojne arhitekture (Plast podatkov + Plast transporta)
- **Dokumentacija primitivov**: Validirani strežniški primitiv (Viri, Pozivi, Orodja) in odjemalski primitiv (Vzorčenje, Izvleček, Beleženje, Korenine)
- **Transportni mehanizmi**: Preverjena točnost dokumentacije STDIO in poenostavljenih HTTP transportov
- **Varnostna navodila**: Potrjena usklajenost s trenutno dokumentacijo najboljših praks za MCP varnost

#### Ključne značilnosti MCP 2025-11-25 dokumentirane
- **OpenID Connect odkrivanje**: Odkritje avtentikacijskega strežnika preko OIDC
- **OAuth Client ID metapodatkovni dokumenti**: Priporočeni mehanizem registracije odjemalca
- **JSON Shema 2020-12**: Privzeti dialekt za MCP definicije shem
- **Sistem razredčkov SDK**: Formalizirane zahteve za podporo in vzdrževanje funkcij SDK
- **Struktura upravljanja**: Formalizirane delovne skupine in interesne skupine v upravljanju MCP

### Glavna posodobitev varnostne dokumentacije (02-Security/)

#### Integracija MCP Security Summit Workshop (Sherpa)
- **Nov praktični učni vir**: Dodana obsežna integracija z [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) po celotni varnostni dokumentaciji
- **Zajetje poti ekspedicije**: Dokumentiran celoten potek od osnovnega tabora do vrha
- **Usklajenost z OWASP**: Vsa varnostna navodila sedaj ustrezajo tveganjem v OWASP MCP Azure Security Guide

#### Integracija OWASP MCP Top 10
- **Nov razdelek**: Dodana tabela OWASP MCP Top 10 varnostnih tveganj z Azure mitigacijami v glavni Security README
- **Dokumentacija na podlagi tveganj**: Posodobljen mcp-security-controls-2025.md z referencami OWASP MCP tveganj za vsako varnostno domeno
- **Referenčna arhitektura**: Povezava do referenčne arhitekture in vzorcev implementacije v OWASP MCP Azure Security Guide

#### Posodobljene varnostne datoteke
- **README.md**: Dodan pregled warsztata Sherpa, tabela poti ekspedicije, povzetek OWASP MCP Top 10 tveganj in odsek za praktične vaje
- **mcp-security-controls-2025.md**: Posodobljen naslov na februar 2026, dodane OWASP referenčne nevarnosti (MCP01-MCP08), popravljena neskladnost verzije specifikacije
- **mcp-security-best-practices-2025.md**: Dodan odsek virov Sherpa in OWASP, posodobljen časovni žig
- **mcp-best-practices.md**: Dodan odsek praktičnih vaj s povezavami Sherpa in OWASP
- **azure-content-safety-implementation.md**: Dodan OWASP MCP06 pokazatelj, usklajenost Sherpa Camp 3 in dodaten odsek virov

#### Dodane nove povezave do virov
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Posamezne OWASP MCP strani tveganj (MCP01-MCP10)

### Skladnost MCP specifikacije 2025-11-25 po celotnem učnem načrtu

#### Modul 03 - Začetek
- **Dokumentacija SDK**: Dodan Go SDK na uradni seznam SDK; posodobljene vse SDK reference, usklajene z MCP specifikacijo 2025-11-25
- **Poenostavitev transporta**: Posodobljeni opisi transportov STDIO in HTTP Streaming z eksplicitnimi sklici na specifikacijo

#### Modul 04 - Praktična implementacija
- **Posodobitve SDK**: Dodan Go SDK; posodobljen seznam SDK z referenco verzije specifikacije
- **Specifikacija avtorizacije**: Posodobljena povezava MCP autorizacijske specifikacije na trenutno verzijo 2025-11-25

#### Modul 05 - Napredne teme
- **Nove funkcije**: Dodano opozorilo o novih funkcijah MCP specifikacije 2025-11-25 (Opravila, Oznake orodij, Izvleček URL načina, Korenine)
- **Varnostni viri**: Dodane povezave do OWASP MCP Top 10 in Sherpa delavnice v dodatne reference

#### Modul 06 - Prispevki skupnosti
- **Seznam SDK**: Dodana Swift in Rust SDK; posodobljena povezava specifikacije na 2025-11-25
- **Referenca specifikacije**: Posodobljena povezava do MCP specifikacije na neposredno URL specifikacije

#### Modul 07 - Lekcije iz zgodnje uporabe
- **Posodobitve virov**: Dodana povezava do MCP specifikacije 2025-11-25 in OWASP MCP Top 10 v dodatne vire

#### Modul 08 - Najboljše prakse
- **Verzija specifikacije**: Posodobljena referenca MCP specifikacije na 2025-11-25
- **Varnostni viri**: Dodani OWASP MCP Top 10 in Sherpa delavnica med dodatnimi referencami

#### Modul 10 - Poenostavitev AI delovnih tokov
- **Posodobitev značke**: Spremenjena značkica verzije MCP z verzije SDK (1.9.3) na verzijo specifikacije (2025-11-25)
- **Povezave virov**: Posodobljena povezava do MCP specifikacije; dodan OWASP MCP Top 10

#### Modul 11 - MCP strežniške praktične vaje
- **Referenca specifikacije**: Posodobljena povezava MCP specifikacije na verzijo 2025-11-25
- **Varnostni viri**: Dodan OWASP MCP Top 10 med uradne vire

## 18. december 2025

### Posodobitev varnostne dokumentacije - MCP specifikacija 2025-11-25

#### Najboljše praksa varnosti MCP (02-Security/mcp-best-practices.md) - posodobitev verzije specifikacije
- **Posodobitev verzije protokola**: Posodobitev na najnovejšo MCP specifikacijo 2025-11-25 (izdano 25. novembra 2025)
  - Posodobljene vse reference verzij specifikacije z 2025-06-18 na 2025-11-25
  - Posodobljene časovne reference dokumenta z 18. avgusta 2025 na 18. december 2025
  - Preverjeno, da vse URL specifikacij kažejo na trenutno dokumentacijo
- **Validacija vsebine**: Celovita validacija najboljših varnostnih praks glede na najnovejše standarde
  - **Microsoft varnostne rešitve**: Preverjena trenutna terminologija in povezave za Prompt Shields (prej "Odkritje tveganja jailbreak"), Azure Content Safety, Microsoft Entra ID in Azure Key Vault
  - **OAuth 2.1 varnost**: Potrjena usklajenost z najnovejšimi OAuth varnostnimi praksami
  - **OWASP standardi**: Validirani ostanki referenc OWASP Top 10 za LLM-je
  - **Azure storitve**: Preverjene vse Microsoft Azure dokumentacijske povezave in najboljše prakse
- **Uskladitev standardov**: Vsi referencirani varnostni standardi so potrjeni kot aktualni
  - Okvir za upravljanje tveganj AI NIST
  - ISO 27001:2022
  - Najboljše prakse varnosti OAuth 2.1
  - Okviri varnosti in skladnosti Azure
- **Viri za implementacijo**: Preverjene vse povezave do vodnikov za implementacijo in vire
  - Vzorci avtentikacije Azure API Management
  - Vodniki za integracijo Microsoft Entra ID
  - Upravljanje skrivnosti Azure Key Vault
  - DevSecOps cevovodi in rešitve za spremljanje

### Zagotovilo kakovosti dokumentacije
- **Skladnost s specifikacijo**: Zagotovljena usklajenost vseh obveznih MCP varnostnih zahtev (MORA/MORA NE) z najnovejšo specifikacijo
- **Sodobnost virov**: Preverjene vse zunanje povezave do Microsoft dokumentacije, varnostnih standardov in vodnikov za implementacijo
- **Zajetje najboljših praks**: Potrjena celovita pokritost avtentikacije, avtorizacije, AI specifičnih groženj, varnosti dobavne verige in poslovnih vzorcev

## 6. oktober 2025

### Razširitev razdelka Začetek - Napredna uporaba strežnika in preprosta avtentikacija

#### Napredna uporaba strežnika (03-GettingStarted/10-advanced)
- **Dodano novo poglavje**: Predstavljen celovit vodič za napredno uporabo MCP strežnikov, ki zajema tako redno kot nizkonivojsko strežniško arhitekturo.
  - **Redni proti nizkonivojskemu strežniku**: Podrobna primerjava in primeri kode v Python in TypeScript za oba pristopa.
  - **Obvladovanje preko upravljalcev**: Razlaga upravljanja orodij/virov/pozivov na osnovi handlerjev za prilagodljive in razširljive strežniške implementacije.
  - **Praktični vzorci**: Resnični primeri, kjer so nizkonivojski strežniški vzorci koristni za napredne funkcije in arhitekturo.

#### Preprosta avtentikacija (03-GettingStarted/11-simple-auth)
- **Dodano novo poglavje**: Korak-po-korak vodič za implementacijo preproste avtentikacije v MCP strežnikih.
  - **Koncepti avtentikacije**: Jasna razlaga razlik med avtentikacijo in avtorizacijo ter rokovanjem z overitvenimi podatki.
  - **Osnovna implementacija avtentikacije**: Vzorci avtentikacije na osnovi middleware v Python (Starlette) in TypeScript (Express) s primeri kode.
  - **Napredovanje k varnosti**: Navodila za začetek s preprosto avtentikacijo in napredovanje do OAuth 2.1 ter RBAC, z referencami na napredne varnostne module.

Te dodatke nudijo praktična, ročna navodila za gradnjo robustnih, varnih in prilagodljivih implementacij MCP strežnikov, povezujoč temeljne koncepte z naprednimi vzorci produkcije.

## 29. september 2025

### Laboratorijske vaje za integracijo MCP strežnika z bazo podatkov - Celovit praktični učni načrt

#### 11-MCPServerHandsOnLabs - Novi celovit učni načrt integracije baze podatkov
- **Celovit 13-laboratorijski učni načrt**: Dodan praktičen učni načrt za gradnjo MCP strežnikov pripravljenih za produkcijsko uporabo z integracijo PostgreSQL baze podatkov
  - **Praktična implementacija**: Primer uporabe analitike Zava Retail, ki prikazuje poslovno-tehnološke vzorce
  - **Strukturiran potek učenja**:
    - **Laboratoriji 00-03: Osnove** - Uvod, temeljna arhitektura, varnost in večstrankarskost, nastavitev okolja
    - **Laboratoriji 04-06: Gradnja MCP strežnika** - Oblikovanje baze podatkov in sheme, implementacija MCP strežnika, razvoj orodij  
    - **Laboratoriji 07-09: Napredne funkcije** - Integracija semantičnega iskanja, testiranje in odpravljanje napak, integracija z VS Code
    - **Laboratoriji 10-12: Produkcija in najboljše prakse** - Strategije uvajanja, spremljanje in vidnost, najboljše prakse in optimizacija
  - **Podjetniške tehnologije**: FastMCP okvir, PostgreSQL z pgvector, Azure OpenAI vdelave, Azure Container Apps, Application Insights
  - **Napredne funkcije**: Varnost na ravni vrstic (RLS), semantično iskanje, večstrankarski dostop do podatkov, vektorske vdelave, spremljanje v realnem času

#### Standardizacija terminologije - pretvorba modula v laboratorij
- **Celovita posodobitev dokumentacije**: Sistemsko posodobljene vse datoteke README v 11-MCPServerHandsOnLabs, da uporabljajo terminologijo "Laboratorij" namesto "Modul"
  - **Naslovi razdelkov**: Posodobljeno "Kaj ta modul zajema" v "Kaj ta laboratorij zajema" v vseh 13 laboratorijih
  - **Opis vsebine**: Spremenjeno "Ta modul nudi..." v "Ta laboratorij nudi..." po celotni dokumentaciji
  - **Cilji učenja**: Posodobljeno "Ob koncu tega modula..." v "Ob koncu tega laboratorija..." 
  - **Navigacijske povezave**: Preoblikovane vse reference "Modul XX:" v "Laboratorij XX:" v vseh navzkrižnih sklicih in navigacijah
  - **Sledenje dokončanju**: Posodobljeno "Po dokončanju tega modula..." v "Po dokončanju tega laboratorija..."
  - **Ohranitev tehničnih referenc**: Ohranjene Python module reference v konfiguracijskih datotekah (npr. `"module": "mcp_server.main"`)

#### Izboljšava študijskega vodiča (study_guide.md)
- **Vizualni zemljevid učnega načrta**: Dodan nov razdelek "11. Laboratorijske vaje za integracijo baze podatkov" s celovito vizualizacijo strukture laboratorijev
- **Struktura repozitorija**: Posodobljeno iz desetih na enajst glavnih razdelkov z podrobnim opisom 11-MCPServerHandsOnLabs
- **Navodila za učno pot**: Izboljšane navigacijske smernice za razdelke 00-11
- **Tehnološko pokritje**: Dodani detajli integracije FastMCP, PostgreSQL in Azure storitev
- **Učni rezultati**: Poudarek na strežniškem razvoju pripravljeni za produkcijo, vzorci integracije baze podatkov in podjetniška varnost

#### Izboljšava glavne strukture README
- **Terminologija na osnovi laboratorijev**: Posodobljen glavni README.md v 11-MCPServerHandsOnLabs za dosledno uporabo strukture "Laboratorij"
- **Organizacija učne poti**: Jasno razhajanje od temeljnih konceptov, prek naprednih implementacij do uvajanja v produkcijsko okolje
- **Fokus na resnični svet**: Poudarek na praktičnem, ročnem učenju s poslovnimi vzorci in tehnologijami

### Izboljšave kakovosti in doslednosti dokumentacije
- **Poudarek na praktičnem učenju**: Okrepljen praktični pristop z laboratorijskimi vajami skozi celotno dokumentacijo
- **Fokus na poslovne vzorce**: Izpostavljene produkcijsko pripravljene implementacije in premisleki o varnosti v podjetju
- **Tehnološka integracija**: Celovito pokritje sodobnih Azure storitev in AI integracijskih vzorcev
- **Napredovanje učenja**: Jasna, strukturirana pot od osnovnih konceptov do uvajanja v produkcijo

## 26. september 2025

### Izboljšave primerov rabe - integracija GitHub MCP registra

#### Primeri rabe (09-CaseStudy/) - osredotočenost na razvoj ekosistema
- **README.md**: Obsežna razširitev z obsežnim primerom rabe GitHub MCP registra
  - **Primer rabe GitHub MCP registra**: Novi obsežni primer rabe, ki preučuje lansiranje MCP registra na GitHubu septembra 2025
    - **Analiza problema**: Podrobno preučevanje razdrobljene MCP strežniške odkrivanja in izzivov uvajanja
    - **Arhitektura rešitve**: Centraliziran pristop registra GitHub s inštalacijo VS Code z enim klikom
    - **Poslovni vpliv**: Merljive izboljšave uvajanja razvijalcev in produktivnosti
    - **Strateška vrednost**: Poudarek na modularni namestitvi agentov in medorodnih interoperabilnostih
    - **Razvoj ekosistema**: Pozicioniranje kot temeljna platforma za agentno integracijo
  - **Izboljšana struktura primerov rabe**: Posodobljeni vsi sedem primerov z doslednim formatiranjem in obsežnimi opisi
    - Azure AI Travel Agents: Poudarek na multi-agentni orkestraciji
    - Azure DevOps integracija: Poudarek na avtomatizaciji delovnih tokov
    - Pridobivanje dokumentacije v realnem času: Implementacija odjemalca konzole Python
    - Interaktivni generator učnega načrta: Verižni klepetalni spletni app Chainlit

    - Dokumentacija v urejevalniku: integracija VS Code in GitHub Copilot
    - Azure API Management: vzorci integracije podjetniškega API-ja
    - GitHub MCP Registry: razvoj ekosistema in platforma skupnosti
  - **Celoviti zaključek**: Prepisan zaključni del, ki poudarja sedem študij primerov, ki zajemajo več dimenzij implementacije MCP
    - Podjetniška integracija, več-agentska orkestracija, produktivnost razvijalcev
    - Razvoj ekosistema, razvrstitev izobraževalnih aplikacij
    - Izboljšani vpogledi v arhitekturne vzorce, strategije implementacije in najboljše prakse
    - Poudarek na MCP kot zrelem, proizvodno pripravljenem protokolu

#### Posodobitve učnega načrta (study_guide.md)
- **Vizualni zemljevid kurikuluma**: Posodobljen miselni zemljevid, ki vključuje GitHub MCP Registry v razdelku Študije primerov
- **Opis študij primerov**: Izboljšan iz generičnih opisov v podrobno razčlenitev sedmih celovitih študij primerov
- **Struktura repozitorija**: Posodobljen 10. razdelek, ki prikazuje celovito pokritost študij primerov z določenimi podrobnostmi implementacije
- **Integracija dnevnika sprememb**: Dodan zapis z dne 26. septembra 2025, ki dokumentira dodatek GitHub MCP Registry in izboljšave študij primerov
- **Posodobitve datumov**: Posodobljen časovni žig v nogi strani, ki odraža najnovejšo revizijo (26. september 2025)

### Izboljšave kakovosti dokumentacije
- **Izboljšanje skladnosti**: Standardizirana oblika in struktura študij primerov v vseh sedmih primerih
- **Celovita pokritost**: Študije primerov zdaj zajemajo podjetniške, produktivnosti razvijalcev in scenarije razvoja ekosistema
- **Strateški položaj**: Izboljšan poudarek na MCP kot temeljni platformi za uvajanje agentnih sistemov
- **Integracija virov**: Posodobljeni dodatni viri, ki vključujejo povezavo do GitHub MCP Registry

## 15. september 2025

### Razširitev naprednih tem – prilagojeni transporti in inženiring konteksta

#### MCP prilagojeni transporti (05-AdvancedTopics/mcp-transport/) – Novi vodič za napredno implementacijo
- **README.md**: Popoln vodič za implementacijo prilagojenih mehanizmov MCP transporta
  - **Azure Event Grid Transport**: Celovita implementacija brezstrežniškega dogodkovno vodene transportne rešitve
    - Primeri v C#, TypeScript in Python z integracijo Azure Functions
    - Vzorci arhitekture, ki so vodeni z dogodki za razširljive rešitve MCP
    - Sprejemniki webhookov in upravljanje sporočil na osnovi push obvestil
  - **Azure Event Hubs Transport**: Implementacija transporta z visokoprepustnim pretokom
    - Zmožnosti pretakanja v realnem času za scenarije z nizko zakasnitvijo
    - Strategije particioniranja in upravljanje kontrolnih točk
    - Pakiranje sporočil in optimizacija zmogljivosti
  - **Vzorec podjetniške integracije**: Produktivni arhitekturni primeri
    - Distribuirano procesiranje MCP prek več Azure Functions
    - Hibridne transportne arhitekture, ki združujejo več vrst transporta
    - Strategije trajnosti sporočil, zanesljivosti in obravnave napak
  - **Varnost in nadzor**: Integracija Azure Key Vault in vzorci opazovanja
    - Avtentikacija z upravljano identiteto in dostop po načelu najmanjših privilegijev
    - Telemetrija Application Insights in spremljanje zmogljivosti
    - Prekinjevalniki in vzorci odpornosti na napake
  - **Okvirji za testiranje**: Celovite strategije testiranja za prilagojene transporte
    - Enotsko testiranje z nadomestnimi objekti in ogrodji za ponarejanje
    - Integracijsko testiranje z Azure Test Containers
    - Razmisleki o testiranju zmogljivosti in obremenitve

#### Inženiring konteksta (05-AdvancedTopics/mcp-contextengineering/) – Rastoča disciplina umetne inteligence
- **README.md**: Celovita raziskava inženiringa konteksta kot rastočega področja
  - **Temeljna načela**: Popolno deljenje konteksta, zavedanje odločitev dejanj in upravljanje oken konteksta
  - **Usmerjenost MCP protokola**: Kako zasnova MCP naslavlja izzive inženiringa konteksta
    - Omejitve okna konteksta in progresivne strategije nalaganja
    - Določanje relevantnosti in dinamično pridobivanje konteksta
    - Večmodalno upravljanje konteksta in varnostni premisleki
  - **Pristopi k implementaciji**: Enonitne proti več-agentskim arhitekturam
    - Tehnike razdeljevanja in prednostne obravnave kontekstnih kosov
    - Progresivno nalaganje in stiskanje konteksta
    - Večplastni pristopi h kontekstu in optimizacija pridobivanja
  - **Okvir za merjenje**: Nastajajoče metrike za ocenjevanje učinkovitosti konteksta
    - Učinkovitost vhodnih podatkov, zmogljivost, kakovost in uporabniška izkušnja
    - Eksperimentalni pristopi k optimizaciji konteksta
    - Analiza napak in metodologije izboljševanja

#### Posodobitve navigacije kurikuluma (README.md)
- **Izboljšana struktura modulov**: Posodobljena tabela kurikuluma, ki vključuje nove napredne teme
  - Dodani vnosi Inženiring konteksta (5.14) in Prilagojen transport (5.15)
  - Dosledno oblikovanje in navigacijske povezave v vseh modulih
  - Posodobljeni opisi, ki odražajo obseg trenutne vsebine

### Izboljšave strukture imenikov
- **Standardizacija imen**: Ime "mcp transport" preimenovano v "mcp-transport" za skladnost z drugimi mapami naprednih tem
- **Organizacija vsebine**: Vse mape 05-AdvancedTopics sedaj sledijo doslednemu vzorcu imenovanja (mcp-[tema])

### Izboljšave kakovosti dokumentacije
- **Usklajenost z MCP specifikacijo**: Vse nove vsebine sklicujejo na trenutno MCP specifikacijo 2025-06-18
- **Primeri v več jezikih**: Celoviti primeri kode v C#, TypeScript in Python
- **Podjetniški poudarek**: Vzorce, pripravljene za produkcijsko rabo, in integracija z Azure oblakom povsod
- **Vizualna dokumentacija**: Mermaid diagrami za vizualizacijo arhitekture in tokov

## 18. avgust 2025

### Celovita posodobitev dokumentacije – standardi MCP 2025-06-18

#### Najboljše varnostne prakse MCP (02-Security/) – popolna modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Popoln prepis, usklajen z MCP specifikacijo 2025-06-18
  - **Obvezni zahtevki**: Dodani eksplicitni zahtevi MORA / NE SME iz uradne specifikacije z jasnimi vizualnimi indikatorji
  - **12 temeljnih varnostnih praks**: Prestrukturirano iz 15-postavk v celovita varnostna področja
    - Varnost žetonov in avtentikacija z integracijo zunanjega ponudnika identitete
    - Upravljanje sej in varnost prenosa z zahtevami kriptografije
    - Zaščita pred grožnjami, specifičnimi za umetno inteligenco, z integracijo Microsoft Prompt Shields
    - Nadzor dostopa in dovoljenj po načelu najmanjših privilegijev
    - Varnost vsebine in nadzor z integracijo Azure Content Safety
    - Varnost dobavne verige s celovito preveritvijo komponent
    - Varnost OAuth in preprečevanje zmede delegata z implementacijo PKCE
    - Odziv na incidente in okrevanje z avtomatiziranimi zmožnostmi
    - Skladnost in upravljanje z uskladitvijo z regulativnimi zahtevami
    - Napredni varnostni nadzor z arhitekturo ničelnega zaupanja
    - Integracija Microsoft varnostnega ekosistema s celovitimi rešitvami
    - Neprestani razvoj varnosti z adaptivnimi praksami
  - **Microsoft varnostne rešitve**: Izboljšana integracijska navodila za Prompt Shields, Azure Content Safety, Entra ID in GitHub Advanced Security
  - **Viri za implementacijo**: Kategorizirane celovite povezave po uradni MCP dokumentaciji, Microsoft varnostnih rešitvah, varnostnih standardih in vodičih za implementacijo

#### Napredni varnostni nadzor (02-Security/) – implementacija na ravni podjetja
- **MCP-SECURITY-CONTROLS-2025.md**: Popolna prenova s podjetniškim varnostnim okvirom
  - **9 celovitih varnostnih področij**: Razširjeno iz osnovnih kontrol v podrobni podjetniški okvir
    - Napredna avtentikacija in avtorizacija z integracijo Microsoft Entra ID
    - Varnost žetonov in kontrole proti posredovanju s celovito preveritvijo
    - Kontrole varnosti sej z preprečevanjem prevzemov
    - Varnostne kontrole specifične za AI z zaščito pred injekcijo v pozive in strupenjem orodij
    - Preprečevanje napadov z zmedo delegata z varnostjo OAuth proxyja
    - Varnost izvajanja orodij z uporabo varnega okolja in izolacije
    - Kontrole varnosti dobavne verige s preverjanjem odvisnosti
    - Kontrole nadzora in zaznavanja z integracijo SIEM
    - Odziv na incidente in okrevanje z avtomatiziranimi zmožnostmi
  - **Primeri implementacije**: Dodani podrobni YAML konfiguracijski bloki in primeri kode
  - **Integracija rešitve Microsoft**: Celovita pokritost varnostnih storitev Azure, GitHub Advanced Security in upravljanja identitete podjetja

#### Varnost naprednih tem (05-AdvancedTopics/mcp-security/) – implementacija pripravljena za produkcijo
- **README.md**: Popoln prepis za implementacijo varnosti na ravni podjetja
  - **Usklajenost s trenutno specifikacijo**: Posodobljeno na MCP specifikacijo 2025-06-18 z obveznimi varnostnimi zahtevami
  - **Izboljšana avtentikacija**: Integracija Microsoft Entra ID z obsežnimi primeri za .NET in Java Spring Security
  - **Integracija varnosti za AI**: Implementacija Microsoft Prompt Shields in Azure Content Safety z detaljnimi primeri v Pythonu
  - **Napredna mitigacija groženj**: Celoviti primeri implementacije za
    - Preprečevanje napadov z zmedo delegata z validacijo PKCE in uporabniškim soglasjem
    - Preprečevanje prenosa žetonov z validacijo občinstva in varnim upravljanjem žetonov
    - Preprečevanje prevzemov sej s kriptografskim vezanjem in vedenjsko analizo
  - **Integracija varnosti podjetja**: Spremljanje Azure Application Insights, cevovodi za zaznavanje groženj in varnost dobavne verige
  - **Kontrolni seznam implementacije**: Jasna razmejitev med obveznimi in priporočenimi varnostnimi kontrolami z ugodnostmi Microsoft varnostnega ekosistema

### Kakovost dokumentacije in usklajenost s standardi
- **Reference specifikacij**: Posodobljene vse reference na trenutno MCP specifikacijo 2025-06-18
- **Microsoftov varnostni ekosistem**: Izboljšana integracijska navodila skozi vse varnostne dokumentacije
- **Praktična implementacija**: Dodani podrobni primeri kode v .NET, Javi in Pythonu z vzorci za podjetja
- **Organizacija virov**: Celovita kategorizacija uradne dokumentacije, varnostnih standardov in vodičev za implementacijo
- **Vizualni indikatorji**: Jasna označitev obveznih zahtev in priporočenih praks


#### Temeljni pojmi (01-CoreConcepts/) – popolna modernizacija
- **Posodobitev različice protokola**: Posodobljeno s sklicem na trenutno MCP specifikacijo 2025-06-18 z datumskim označevanjem (format LLLL-MM-DD)
- **Izboljšava arhitekture**: Izboljšani opisi gostiteljev, odjemalcev in strežnikov za prikaz trenutnih arhitekturnih vzorcev MCP
  - Gostitelji so zdaj jasno opredeljeni kot AI aplikacije, ki usklajujejo več povezav MCP odjemalcev
  - Odjemalci opisani kot protokolarni povezovalniki, ki vzdržujejo enon eno razmerje s strežniki
  - Strežniki so izboljšani z lokalnimi proti oddaljenim scenarijem uvajanja
- **Prenova primitivov**: Popolna prenova strežniških in odjemalskih primitivov
  - Strežniški primitiv: Viri (viri podatkov), Pozivi (predloge), Orodja (izvedljive funkcije) z podrobnimi razlagami in primeri
  - Odjemalski primitiv: Vzorcevanje (LLM zaključki), Vpraševanje (uporabniški vnos), Beleženje (razhroščevanje/nadzor)
  - Posodobljeno z aktualnimi vzorci metod za odkrivanje (`*/list`), pridobivanje (`*/get`) in izvajanje (`*/call`)
- **Arhitektura protokola**: Uveden model z dvojnim plasti arhitekture
  - Plasti podatkov: osnova JSON-RPC 2.0 z upravljanjem življenjskega cikla in primitivov
  - Plasti transporta: STDIO (lokalno) in Streamable HTTP z SSE (oddaljeno) transportnimi mehanizmi
- **Varnostni okvir**: Celovita varnostna načela, vključno z eksplicitnim soglasjem uporabnika, varstvom zasebnosti podatkov, varnostjo izvajanja orodij in varnostjo plasti transporta
- **Vzorec komunikacije**: Posodobljena protokolarna sporočila za prikaz inicializacije, odkrivanja, izvajanja in potekov obveščanja
- **Primeri kode**: Osveženi večjezični primeri (.NET, Java, Python, JavaScript) za prikaz trenutnih vzorcev MCP SDK

#### Varnost (02-Security/) – celovita prenova varnosti  
- **Usklajenost s standardi**: Popolna uskladitev z varnostnimi zahtevami MCP specifikacije 2025-06-18
- **Razvoj avtentikacije**: Dokumentiran razvoj od prilagojenih OAuth strežnikov do delegiranja zunanjim ponudnikom identitete (Microsoft Entra ID)
- **Analiza groženj za AI**: Izboljšana pokritost sodobnih AI napadov
  - Podrobni scenariji napadov z injekcijo pozivov z resničnimi primeri
  - Mehanizmi zastrupitve orodij in vzorci napadov "rug pull"
  - Zastrupitve oken konteksta in napadi z zmedo modela
- **Microsoft AI varnostne rešitve**: Celovita pokritost varnostnega ekosistema Microsoft
  - AI Prompt Shields z naprednim zaznavanjem, izpostavitvijo in tehniko delimiterjev
  - Vzorci integracije Azure Content Safety
  - GitHub Advanced Security za zaščito dobavne verige
- **Napredna zaščita pred grožnjami**: Podrobne varnostne kontrole za
  - Prevzeme sej z MCP-specifičnimi scenariji napadov in zahtevami kriptografskega ID sej
  - Težave z zmedo delegata v scenarijih MCP proxy z eksplicitnimi zahtevami za soglasje
  - Ranljivosti pri prenašanju žetonov z obveznimi validacijskimi kontrolami
- **Varnost dobavne verige**: Razširjena pokritost AI dobavne verige, vključno z osnovnimi modeli, storitvami vgradnje, ponudniki konteksta in API-ji tretjih oseb
- **Temeljna varnost**: Izboljšana integracija z varnostnimi vzorci podjetja, vključno z arhitekturo ničelnega zaupanja in Microsoftovim varnostnim ekosistemom
- **Organizacija virov**: Kategorizirane celovite povezave virov po vrstah (uradna dokumentacija, standardi, raziskave, Microsoft rešitve, vodiči za implementacijo)

### Izboljšave kakovosti dokumentacije
- **Strukturirani učni cilji**: Izboljšani učni cilji s specifičnimi, izvedljivimi izidi 
- **Preklici med temami**: Dodane povezave med sorodnimi temami na področju varnosti in temeljnih konceptov
- **Aktualne informacije**: Posodobljene vse datumske reference in povezave na specifikacije v skladu s trenutnimi standardi
- **Navodila za implementacijo**: Dodana specifična, izvedljiva navodila za implementacijo skozi oba razdelka

## 16. julij 2025

### Izboljšave README in navigacije
- Popolnoma prenovljena navigacija kurikuluma v datoteki README.md
- `<details>` oznake nadomeščene z bolj dostopno obliko, temelječo na tabeli
- Ustvarjene alternativne možnosti postavitve v novi mapi "alternative_layouts"
- Dodani primeri navigacije v obliki kartic, zavihkov in harmonike
- Posodobljen razdelek o strukturi repozitorija, ki sedaj vključuje vse najnovejše datoteke
- Izboljšan razdelek "Kako uporabljati ta kurikulum" z jasnimi priporočili
- Posodobljene povezave do specifikacij MCP, da kažejo na pravilne URL-je
- Dodan razdelek Inženiring konteksta (5.14) v strukturo kurikuluma

### Posodobitve učnega načrta
- Popolnoma prenovljen učni načrt v skladu s trenutno strukturo repozitorija
- Dodani novi razdelki za MCP odjemalce in orodja ter priljubljene MCP strežnike
- Posodobljen vizualni zemljevid kurikuluma za natančen prikaz vseh tem
- Izboljšani opisi naprednih tem za pokritje vseh specializiranih področij
- Posodobljen razdelek študij primerov za odražanje dejanskih primerov
- Dodan ta celovit dnevnik sprememb

### Prispevki skupnosti (06-CommunityContributions/)
- Dodane podrobne informacije o MCP strežnikih za generiranje slik
- Dodan celovit razdelek o uporabi Claude v VSCode
- Dodani navodila za nastavitev in uporabo terminalskega odjemalca Cline
- Posodobljen razdelek odjemalcev MCP, da vključuje vse priljubljene možnosti
- Izboljšani primeri prispevkov z bolj natančnimi vzorci kode

### Napredne teme (05-AdvancedTopics/)
- Organizirane vse specializirane mape tem z doslednim poimenovanjem
- Dodani materiali in primeri za inženiring konteksta
- Dodana dokumentacija integracije Foundry agenta
- Izboljšana dokumentacija integracije varnosti Entra ID

## 11. junij 2025

### Prvotna kreacija
- Izdana prva različica kurikuluma MCP za začetnike

- Ustvarjena osnovna struktura za vseh 10 glavnih poglavij
- Implementirana Vizualna učna karta za navigacijo
- Dodani začetni vzorčni projekti v več programskih jezikih

### Začetek (03-GettingStarted/)
- Ustvarjeni prvi primeri implementacije strežnika
- Dodana navodila za razvoj klienta
- Vključena navodila za integracijo LLM klienta
- Dodana dokumentacija za integracijo VS Code
- Implementirani primeri strežnika za Server-Sent Events (SSE)

### Osnovni koncepti (01-CoreConcepts/)
- Dodan podroben opis arhitekture klient-strežnik
- Ustvarjena dokumentacija o ključnih komponentah protokola
- Dokumentirani vzorci sporočanja v MCP

## 23. maj 2025

### Struktura repozitorija
- Inicializiran repozitorij z osnovno strukturo map
- Ustvarjene datoteke README za vsako glavno poglavje
- Nastavljena infrastruktura za prevajanje
- Dodane slikovne vsebine in diagrami

### Dokumentacija
- Ustvarjen začetni README.md s pregledom učnega načrta
- Dodana CODE_OF_CONDUCT.md in SECURITY.md
- Nastavljen SUPPORT.md z navodili za pomoč
- Ustvarjena preliminarna struktura študijskega vodiča

## 15. april 2025

### Načrtovanje in okvir
- Začetno načrtovanje učnega načrta MCP za začetnike
- Določeni učni cilji in ciljna publika
- Opisana struktura kurikuluma z 10 poglavji
- Razvit konceptualni okvir za primere in študije primerov
- Ustvarjeni začetni prototipni primeri za ključne koncepte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->