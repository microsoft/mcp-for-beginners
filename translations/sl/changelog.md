# Zapis sprememb: MCP za začetnike učni načrt

Ta dokument služi kot zapis vseh pomembnih sprememb, narejenih v učnem načrtu Model Context Protocol (MCP) za začetnike. Spremembe so dokumentirane v obratnem kronološkem vrstnem redu (najnovejše spremembe najprej).

## 29. julij 2026

### Nov spremljevalec modula 08: Zanesljivostni priklopniki in varni ponovni poskusi

Dodana je nevtralna lekcija za MCP orodja, ki ustvarjajo učinke v resničnem svetu,
usklajena z dokončno specifikacijo `2026-07-28`.

- **Novo**: [lekcija spremljevalca zanesljivostnega priklopnika][reliability-sidecar]
  uporablja eno zgodbo o podporni vstopnici, dva Mermaid diagrama in tok odločanja o ponovnem poskusu,
  da pojasni ključe za stabilno delovanje, atomsko podvajanje vstopa,
  usklajevanje, dokaze in mejo razširitve Naloge.
- **Novo**: Vaja za injiciranje napak s standardno knjižnico Python in SQLite
  uporablja ločena skladišča operacij in vstopnic za demonstracijo izgubljenega odziva
  po potrditvi zunanjega učinka. Šest determinističnih testov pokriva nežno
  podvajanje, zaščiteno obnovitev ob zagonu, konflikte vsebine, predpomnjene rezultate,
  aktivne zahtevke in hkratni podvojeni vstop.
- **Posodobljeno**: Modul 08 zdaj povezuje lekcijo spremljevalca, identificira
  dokončni model brezstanjskega zahteva `2026-07-28`, razlikuje OpenTelemetry
  opazovanje od zastarele funkcije beleženja MCP in omejuje svoj
  generični primer ponovnega poskusa na samo operacije za branje.
- **Izbirno**: Lekcija preslika svoje prenosljive pojme na eno označeno skupnost
  implementacijo, ne da bi storitev gostiteljice ali omrežni klic vključila v
  vajo.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. julij 2026

### Nova lekcija: Kandidat za izdajo specifikacije MCP 2026-07-28

Dodano pokritje prihajajočega kandidata za izdajo specifikacije MCP `2026-07-28` (objavljeno 21. maja 2026; dokončna izdaja predvidena za 28. julij 2026), povzeto iz [uradne objave na blogu](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Osnova učnega načrta ostaja **MCP Specification 2025-11-25** do izdaje nove različice, zato je predstavljeno kot vnaprejšnje vodilo in ne prepis obstoječih lekcij.

- **Novo**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — celotna lekcija, ki pokriva brezstanje osnove protokola (odstranitev rokovanja `initialize` in `Mcp-Session-Id`), nove usmerjevalne glave `Mcp-Method`/`Mcp-Name`, predpomnilniške metapodatke `ttlMs`/`cacheScope`, W3C Trace Context v `_meta`, formalni okvir razširitev (MCP aplikacije in nova razširitev Naloge), šest SEP za utrditev pooblastil, zastaranje Roots/Sampling/Logging in prehod na polni JSON Schema 2020-12 za orodjske sheme.
- **Posodobljeno** z usmerjenimi opombami, ki povezujejo na novo lekcijo:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): opomba o verziji protokola, razdelki Sampling/Roots/Logging/Tasks, in "Kaj sledi"
  - [02-Security/README.md](./02-Security/README.md): opomba o utrjevanju pooblastil
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): opomba o brezstanjskem transportu
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): opomba o opustitvi Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): opomba o opustitvi beleženja in razširitvi Naloge
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): opomba o brezstanjskem/usmerjevalnem protokolu
  - [README.md](./README.md): opomba "Pogled v prihodnost" v razdelku specifikacije in nova vnos `1.1` v tabeli učnih modulov
  - [study_guide.md](./study_guide.md): usmerjen odstavek pod pregledom osnovnih konceptov in datumska pripomba
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): opomba o transportni karti `mcp-session-id` pred modelom brezstanjskega zahtevka
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): pregled modula z opombo o opustitvah Root Contexts/Sampling in razširitvi Naloge
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): opomba o utrjevanju pooblastil

## 24. junij 2026

### Nova lekcija: Uporaba MCP v aplikaciji Copilot

- [Odsek Orodja](./12-tooling/README.md) Dodan odsek o orodjih.
- [MCP v aplikaciji Copilot](./12-tooling/01-copilot-app/README.md)

## 16. junij 2026

### Uskladitev specifikacije MCP & validacija primerov

Učni načrt je bil preverjen glede na trenutno **MCP Specification 2025-11-25** in najnovejše uradne SDK-je, nato so bile popravljene preostale zastarele reference specifikacije in potrjeno, da jedrni primeri še vedno sestavijo in delujejo.

#### Popravki verzije specifikacije (2025-06-18 / 2025-03-26 → 2025-11-25)

Posodobljena angleška vsebina, kjer je še navajala starejšo revizijo specifikacije kot *trenutni/najnovejši* standard, in povezave so bile usmerjene na kanonične poti `modelcontextprotocol.io` specifikacije:
- **05-AdvancedTopics/mcp-security/README.md**: Posodobljen pas "Trenutni standard", uvod, naslov osnovnih varnostnih načel, naslov obveznih zahtev, razdelek Microsoft Entra ID, povezave do referenc in virov ter zaključna varnostna obvestila (8 referenc) na 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Posodobljena povezava do dodatnih virov specifikacije in pas "Trenutni standard" na 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Zamenjana zastarela povezava `2025-03-26` za varnost in zaupanje s trenutno stranjo najboljših varnostnih praks na 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Posodobljena uradna povezava do dokumentacije za Sampling na 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Posodobljena omemba "trenutne MCP specifikacije" v sedanjiku in povezava do dodatnih virov specifikacije na 2025-11-25 (zgodovinske opombe o opustitvi SSE so ohranjene zaradi natančnosti)

#### Validacija primerov glede na trenutne SDK-je

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` je namestil `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` je uspel brez tipnih napak — obstoječi API-ji `McpServer`/`StdioServerTransport` ostajajo veljavni
- **Python (03-GettingStarted/01-first-server/solution/python)**: Preverjen v izoliranem `.venv` z `mcp[cli]` (1.27.2); `py_compile` je uspel in `FastMCP.list_tools()` je pravilno vrnil orodji `add` in `subtract`
- Potrjeno je, da vsi primeri znotraj območij verzij `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) brezhibno rešujejo na trenutno `1.29.0` brez kršitve API-jev

#### Uskladitev odvisnosti (zapiranje vrzeli verzij)

Povišani so bili zastareli SDK pini, tako da vsak primer sledi trenutni izdaji MCP, skladno s konvencijo celotnega repozitorija:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Povišan `@modelcontextprotocol/sdk` iz `^1.8.0` na `>=1.26.0` in posodobljen zastareli opis paketa `"updated for MCP 2025-06-18"` na `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** in **lab4/code/github_mcp_server/pyproject.toml**: Povišan točen pin `mcp==1.23.0` na `mcp>=1.26.0`; obe datoteki `uv.lock` sta bili ponovno ustvarjeni (`uv lock`), da se zakleni datoteki uskladita z trenutno `mcp 1.27.2`

#### Analiza vrzeli v učnem načrtu — Pokritost najnovejših lastnosti specifikacije

Preverjeno je bilo, da učni načrt že pokriva vse primitive, uvedene ali razširjene v MCP 2025-11-25, zato vrzeli vsebine ni:
- **Sampling**: Lekcija 03-GettingStarted/14-sampling in 05-AdvancedTopics/mcp-sampling
- **Elicitation (vključujoč način URL)**: Dokumentirano v 01-CoreConcepts in 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumentirano v 00-Introduction, 01-CoreConcepts in 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimentalno, dolgotrajne operacije)**: Dokumentirano v 01-CoreConcepts in 05-AdvancedTopics/mcp-protocol-features
- **Oznake orodij** (`readOnlyHint` / `destructiveHint`): Dokumentirano v 01-CoreConcepts in 05-AdvancedTopics/mcp-protocol-features

### Krepitev varnosti & odprava ranljivosti v odvisnostih

Izveden je bil popoln varnostni pregled vseh manifestov odvisnosti in izvorne kode primerov, nato so bile odpravljene vse prijavljene npm varnostne napake in ena ugotovitev na ravni kode. Po odpravi `npm audit` ne kaže nobenih ranljivosti v nobeni pregledani map.

#### Ranljivosti v npm odvisnostih (transitivne) — Odpravljeno

Pregledanih je bilo vseh 15 predanih `package-lock.json` datotek. Ranljivosti so bile omejene na transitivne odvisnosti orodja MCP Inspector za razvoj, OpenAI klienta in MCP SDK; vse so sedaj odpravljene brez prekinitve primerov:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** in **lab3/code/weather_mcp/inspector**: Povišan paket `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), kar je odstranilo združene varnostne napotke za `ajv`, `brace-expansion`, `diff`, `path-to-regexp` in `ws`. Dodan je bil npm `overrides` vnos, ki sili popravljen `shell-quote@1.8.4` za odpravo preostale kritične napake v paketu `concurrently`; obe zakleni datoteki sta bili ponovno generirani (zdaj brez ranljivosti)
- **03-GettingStarted/samples/typescript**: `npm audit fix` je posodobil tranzitivni `qs` (zmerno) na popravljeno izdajo
- **03-GettingStarted/samples/javascript**: `npm audit fix` je posodobil tranzitivni `hono` (zmerno) na popravljeno izdajo
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` je posodobil tranzitivni `form-data` (visoko) na popravljeno izdajo
- **03-GettingStarted/11-simple-auth/solution/typescript**: Ustvarjen je bil manjkajoči `package-lock.json`, da je projekt reproducibilen in preverljiv (0 ranljivosti)

#### Popravek varnosti na ravni kode (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Iz alata `open_in_vscode` odstranjen parameter `shell=True`. Predhodni `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` je omogočal interpretacijo lupinskih metaznakov v poti mape s strani `cmd.exe` (vektor za vbrizg ukazov). Zdaj neposredno zažene odločeno `Code.exe` z mapo kot argumentom — brez lupine — kar je funkcionalno enakovredno in varno.

#### Pregled odvisnosti za Python

- Pregledani so bili vsi nabori zahtev za Python z `pip-audit`. `05-AdvancedTopics` in `03-GettingStarted/samples/python` nista pokazala **nihče znanih ranljivosti** (njihova območja `mcp` / `httpx` / `pydantic` / `python-dotenv` se rešujejo na trenutne popravljene izdaje)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` je opozoril na tranzitivno odvisnost **`werkzeug` 3.1.1** s tremi napotki za DoS preko Windows imen naprav v `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, in `CVE-2026-27199` (vse popravljeno v 3.1.6). Dodan je bil ekspliciten varnostni pin `werkzeug>=3.1.6`, da se rešitev popravljene izdaje; potrjeno je, da se omejitev brezhibno rešuje v skladnosti s skladom `chainlit` / `mcp` / `semantic-kernel`

### Preimenovanje blagovne znamke izdelka

Posodobljena je bila vsa vsebina učnega načrta, da odraža preimenovanje izdelka Pri Microsoftu:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Posodobljena povezava na Discord skupnost

- **AGENTS.md**: Posodobljena referenca Discord strežnika
- **README.md**: Posodobljene reference tehnološkega ekosistema
- **study_guide.md**: Posodobljene reference študije primera
- **05-AdvancedTopics/README.md**: Posodobljen naslov in opis modula 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Posodobljen naslov razdelka in opis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Popolna posodobitev naslova in vsebine modula
- **05-AdvancedTopics/mcp-security-entra/README.md**: Posodobljena povezava medreferenc
- **07-LessonsfromEarlyAdoption/README.md**: Posodobljene reference študije primera
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Posodobljen naslov razdelka 9, značke in zmogljivosti
- **08-BestPractices/README.md**: Posodobljena povezava Discord skupnosti
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Posodobljena referenca kanala Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Posodobljena referenca za uvajanje modela
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Posodobljena tabela AI storitev
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Posodobljene reference virov

#### AI Toolkit / AITK → Razširitev Microsoft Foundry Toolkit za VS Code
- **README.md**: Posodobljene glavne reference kurikuluma
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Posodobljen naslov modula, pregled in vsi naslovi modulov
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Posodobljen naslov, cilji učenja, navodila za nastavitev in viri
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Posodobljen naslov, cilji učenja, tabela gostiteljev MCP in medreferenc
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Posodobljen naslov, značke, predpogoji in viri
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Posodobljene reference Agent Builder in povezava za povratne informacije
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Posodobljeni predpogoji in reference razširitev

---

## 11. april 2026

### Nova lekcija, popravki dokumentacije in posodobitve odvisnosti

#### Dodana nova vsebina kurikuluma

**Modul 05 - Napredne teme**
- **Lekcija 5.17: Nasprotno večagentno razmišljanje z MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Novi obsežni vodič, ki pokriva vzorec nasprotnega razpravljanja za več agenteske sisteme
  - Mermaid diagram arhitekture: dva agenta → skupni MCP strežnik → prepis razprave → sodnik → sodba
  - Skupni strežnik orodij MCP (`web_search` + `run_python`) implementiran v Pythonu in TypeScriptu
  - Protipostavljeni sistemski pozivi (ZA / PROTI / Sodnik) z izrecnimi zahtevami za uporabo orodij
  - Orkestrator razprave v Pythonu, TypeScriptu in C#, ki upravlja kroge in usmerja argumente
  - MCP `ClientSession` povezava za orkestrator do dejanskih klicev orodij
  - Tabela uporabnih primerov (odkrivanje halucinacij, modeliranje groženj, pregled zasnove API, preverjanje dejstev, izbira tehnologije)
  - Varnostne razmisleke: zavarovana izvedba, potrjevanje klicev orodij, omejitev hitrosti, beleženje revizij
  - Strukturirana vaja s tremi praktičnimi scenariji (pregled kode, arhitekturna odločitev, moderacija vsebine)

#### Popravki dokumentacije

**Modul 03 - Začetek**
- **05-stdio-server/README.md**: Popravljena nepopolna TypeScript stdio strežniška koda — dodana manjkajoča instanciacija transporta (`new StdioServerTransport()`) in klic `server.connect(transport)` za uskladitev s Python in .NET primeri v istem razdelku
- **14-sampling/README.md**: Popravljena tipkarska napaka — popravljeno `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Posodobitve kurikuluma

**Glavni README.md**
- Dodan vnos 5.17 (Nasprotno večagentno razmišljanje z MCP) v preglednico kurikuluma z neposredno povezavo do nove lekcije

**05-AdvancedTopics/README.md**
- Dodana vrstica lekcije 5.17 v tabelo lekcij

**study_guide.md**
- Dodana tema Nasprotno večagentno razmišljanje v mentalno karto in opis Naprednih tem

#### Popravki kode in varnosti

**Modul 05 - Nasprotni agenti (`mcp-adversarial-agents`)**
- **Varnostni popravek — vbrizgavanje ukazov**: Zamenjana uporaba `execSync` z `execFile` + `promisify` v orodju 'run_python' TypeScripta, s čimer je odstranjen vektor vbrizgavanja ukazov (koda, ki jo nadzoruje LLM, se zdaj posreduje kot dobesedni element argv brez vključenosti lupine)
- **Zanka orodij MCP**: Posodobljen Python orkestrator razprave za uporabo `AsyncAnthropic` klienta (namesto blokirajočega synchornous `Anthropic`), posredovanje žive `ClientSession` neposredno vsakemu agentovemu koraku, pridobivanje definicij orodij z `session.list_tools()` vsak korak, in pošiljanje `tool_use` blokov preko `session.call_tool()` v zanki, dokler model ne odda končnega besedilnega odziva

#### Posodobitve odvisnosti

- Posodobljen paket `hono` na različico 4.12.12 v več pakietih (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Posodobljen paket `@hono/node-server` iz 1.19.11 na 1.19.13 v TypeScript paketih
- Posodobljen paket `cryptography` iz 46.0.5 na 46.0.7 v Python paketih (laboratorija 3 in 4 modula 10-StreamliningAIWorkflows)
- Posodobljen paket `lodash` iz 4.17.23 na 4.18.1 v inšpektorju 10-StreamliningAIWorkflows

#### Prevedbe

- Sinhronizirane prevode za več kot 48 jezikov z najnovejšimi spremembami izvirnika (posodobitev i18n)

---

## 5. februar 2026

### Izboljšave preverjanja in navigacije v repozitoriju

#### Dodana nova vsebina kurikuluma

**Modul 03 - Začetek**
- **12-mcp-hosts/README.md**: Novi obsežni vodič za nastavitev gostiteljev MCP
  - Primeri konfiguracije Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Predloge konfiguracij JSON za vse glavne gostitelje
  - Primerjalna tabela tipov transporta (stdio, SSE/HTTP, WebSocket)
  - Odpravljanje pogostih težav s povezovanjem
  - Najboljše prakse varnosti za konfiguracijo gostiteljev

- **13-mcp-inspector/README.md**: Novi vodič za razhroščevanje z MCP Inspector
  - Metode namestitve (npx, globalni npm, iz izvorne kodi)
  - Povezovanje do strežnikov preko stdio in HTTP/SSE
  - Preizkušanje orodij, virov in potekov pozivov
  - Integracija VS Code z MCP Inspector
  - Pogoste situacije razhroščevanja s rešitvami

**Modul 04 - Praktična implementacija**
- **pagination/README.md**: Novi vodič za implementacijo paginacije
  - Vzorci paginacije na osnovi kazalcev v Pythonu, TypeScriptu, Javi
  - Upravljanje paginacije na strani odjemalca
  - Strategije oblikovanja kazalcev (neprosojni vs. strukturirani)
  - Priporočila za optimizacijo zmogljivosti

**Modul 05 - Napredne teme**
- **mcp-protocol-features/README.md**: Poglobljen pregled novih protokolnih funkcij
  - Implementacija obvestil o napredku
  - Vzorci preklica zahtev
  - Predloge virov s vzorci URI
  - Upravljanje življenjskega cikla strežnika
  - Nadzor nivoja beleženja
  - Vzorci ravnanja z napakami s kode JSON-RPC

#### Popravki navigacije (posodobljenih več kot 24 datotek)

**Glavni moduli README**
 Zdaj vsebuje povezave do prve lekcije IN naslednjega modula

**02-Security poddatoteke**
- Vseh 5 dopolnilnih varnostnih dokumentov ima del navigacije "Kaj sledi"

**09-CaseStudy datoteke**
- Vse datoteke študije primera imajo zaporedno navigacijo

**10-StreamliningAI Laboratoriji**
Dodan razdelek Kaj sledi v pregled modula 10 in modul 11

#### Popravki kode in vsebine

**Posodobitve SDK in odvisnosti**
Popravljena prazna verzija openai na `^4.95.0`
Posodobljen SDK iz `^1.8.0` na `>=1.26.0`
Posodobljeni MCP verzijski pini na `>=1.26.0`

**Popravki kode**
Popravljena neveljavna različica modela `gpt-4o-mini` na `gpt-4.1-mini`

**Popravki vsebine**
Popravljena prekinjena povezava `READMEmd` → `README.md`, popravljena glava kurikuluma `Module 1-3` → `Module 0-3`, popravljena natančnost velike/male črke v poti
Odstranjena poškodovana podvojena vsebina študije primera 5

**Izboljšave za začetnike**
Dodan ustrezen uvod, cilji učenja in predpogoji za začetnike

#### Posodobitve kurikuluma

**Glavni README.md**
- Dodani vnosi 3.12 (MCP gostitelji), 3.13 (MCP inšpektor), 4.1 (paginacija), 5.16 (protokolne funkcije) v preglednico kurikuluma

**README-i modulov**
Dodani lekciji 12 in 13 v seznam lekcij
Dodan razdelek Praktični vodiči s povezavo do paginacije
Dodani lekciji 5.15 (Prilagojen transport) in 5.16 (Protokolne funkcije)

**study_guide.md**
- Posodobljena mentalna karta z vsemi novimi temami: nastavitev MCP gostiteljev, MCP inšpektor, strategije paginacije, poglobljen pregled protokolnih funkcij

## 28. januar 2026

### Pregled skladnosti specifikacije MCP 2025-11-25

#### Izboljšave osnovnih konceptov (01-CoreConcepts/)
- **Nov primitiv klienta - Roots**: Dodana obsežna dokumentacija o primitivu klienta Roots, ki omogoča strežnikom razumevanje meja datotečnega sistema in dostopnih pravic
- **Oznake orodij**: Dodana dokumentacija o vedenjskih oznakah orodij (`readOnlyHint`, `destructiveHint`) za boljše odločitve o izvajanju orodij
- **Klic orodij pri Sampling-u**: Posodobljena dokumentacija Sampling za vključitev parametrov `tools` in `toolChoice` za modelovno vodene klice orodij med zahtevki vzorčenja
- **Elicitation način URL**: Dodana dokumentacija o URL-zasnovani elicitation za zunanje spletne interakcije, ki jih sproži strežnik
- **Naloge (eksperimentalno)**: Dodan nov razdelek s dokumentacijo za eksperimentalno funkcijo nalog za trajne ovojnice izvajanja in odloženo pridobivanje rezultatov
- **Podpora ikon**: Omenjeno, da lahko orodja, viri, predloge virov in pozivi zdaj vključujejo ikone kot dodatne metapodatke

#### Posodobitve dokumentacije
- **README.md**: Dodana referenca na različico MCP specifikacije 2025-11-25 in razlaga različic na podlagi datuma
- **study_guide.md**: Posodobljen zemljevid kurikuluma za vključitev Nalog in Oznak orodij v razdelek Osnovni koncepti; posodobljen časovni žig dokumenta

#### Preverjanje skladnosti specifikacije
- **Različica protokola**: Preverjene vse dokumentacijske reference na trenutno MCP specifikacijo 2025-11-25
- **Usklajenost arhitekture**: Potrjena natančnost dokumentacije dvoplastne arhitekture (plasti podatkov + plasti transporta)
- **Dokumentacija primitivov**: Preverjeni strežniški primitiv (viri, pozivi, orodja) in odjemalski primitiv (Sampling, Elicitation, Logging, Roots)
- **Transportni mehanizmi**: Preverjena točnost dokumentacije STDIO in pretočnega HTTP transporta
- **Varnostna navodila**: Potrjena skladnost z aktualno MCP varnostno dokumentacijo najboljših praks

#### Ključne funkcije MCP 2025-11-25 dokumentirane
- **Discovery OpenID Connect**: Odkritje avtentikacijskega strežnika preko OIDC
- **Dokumenti metapodatkov OAuth Client ID**: Priporočeni mehanizem registracije klienta
- **JSON Schema 2020-12**: Privzeta dialekta za MCP definicije shem
- **Sistem ravni SDK**: Formalizirane zahteve za podporo in vzdrževanje SDK funkcij
- **Struktura upravljanja**: Formalizirane delovne in interesne skupine znotraj MCP upravljanja

### Glavna posodobitev varnostne dokumentacije (02-Security/)

#### Integracija delavnice MCP Security Summit (Sherpa)
- **Nov praktičen vir usposabljanja**: Dodana obsežna integracija z [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) v vse varnostne dokumente
- **Pokrivanje poti ekspedicije**: Dokumentiran celoten napredek od osnovnega tabora do vrha
- **Usklajenost z OWASP**: Vse varnostne smernice zdaj ustrezajo tveganjem iz OWASP MCP Azure Security Guide

#### Integracija OWASP MCP Top 10
- **Nov razdelek**: Dodana tabela OWASP MCP Top 10 varnostnih tveganj z mitigacijami Azure v glavni varnostni README
- **Tveganja na osnovi dokumentacije**: Posodobljen mcp-security-controls-2025.md z OWASP MCP sklici tveganj za vsako varnostno področje
- **Referenčna arhitektura**: Povezava do referenčne arhitekture OWASP MCP Azure Security Guide in vzorcev implementacije

#### Posodobljene varnostne datoteke
- **README.md**: Dodan pregled delavnice Sherpa, tabela poti ekspedicije, povzetek OWASP MCP Top 10 tveganj in razdelek praktičnega usposabljanja
- **mcp-security-controls-2025.md**: Posodobljen naslov na februar 2026, dodani OWASP MCP sklici tveganj (MCP01-MCP08), popravljena neusklajenost različice specifikacije
- **mcp-security-best-practices-2025.md**: Dodan razdelek virov Sherpa in OWASP, posodobljen časovni žig
- **mcp-best-practices.md**: Dodan razdelek praktičnega usposabljanja z povezavami na Sherpa in OWASP
- **azure-content-safety-implementation.md**: Dodan OWASP MCP06 sklic, usklajenost s Sherpa Kamp 3 in dodaten razdelek virov

#### Dodane nove povezave do virov
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [Vodič za varnost OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Posamezne strani z OWASP MCP tveganji (MCP01-MCP10)

### Usklajevanje s specifikacijo MCP za celotno učni načrt 2025-11-25

#### Modul 03 - Začetek
- **SDK dokumentacija**: Dodan Go SDK na uradni seznam SDK; posodobljeni vsi SDK sklici za uskladitev s specifikacijo MCP 2025-11-25
- **Razjasnitev transporta**: Posodobljeni opisi transporta STDIO in HTTP Streaming z eksplicitnimi sklici na specifikacijo

#### Modul 04 - Praktična implementacija
- **Posodobitve SDK**: Dodan Go SDK; posodobljen seznam SDK s sklicem na verzijo specifikacije
- **Specifikacija avtentikacije**: Posodobljena povezava na MCP specifikacijo avtentikacije na sedanjo različico 2025-11-25

#### Modul 05 - Napredne teme
- **Nove funkcije**: Dodani opombe o novih funkcijah MCP specifikacije 2025-11-25 (Naloge, Oznake orodij, Način izluščanja URL, Koreni)
- **Viri za varnost**: Dodane povezave do OWASP MCP Top 10 in Sherpa delavnice v dodatne vire

#### Modul 06 - Prispevki skupnosti
- **Seznam SDK**: Dodana Swift in Rust SDK; posodobljen sklic na specifikacijo 2025-11-25
- **Sklic na specifikacijo**: Posodobljena povezava MCP specifikacije na neposredno URL specifikacije

#### Modul 07 - Lekcije iz zgodnje uporabe
- **Posodobitve virov**: Dodana povezava na MCP specifikacijo 2025-11-25 in OWASP MCP Top 10 v dodatne vire

#### Modul 08 - Najboljše prakse
- **Verzija specifikacije**: Posodobljen sklic na MCP specifikacijo na 2025-11-25
- **Viri za varnost**: Dodan OWASP MCP Top 10 in Sherpa delavnica med dodatne vire

#### Modul 10 - Poenostavitev AI delovnih tokov
- **Posodobitev značke**: Spremenjena različica značke MCP iz SDK verzije (1.9.3) na verzijo specifikacije (2025-11-25)
- **Povezave do virov**: Posodobljena povezava MCP specifikacije; dodan OWASP MCP Top 10

#### Modul 11 - MCP strežniški praktični laboratoriji
- **Sklic na specifikacijo**: Posodobljena povezava MCP specifikacije na verzijo 2025-11-25
- **Viri za varnost**: Dodan OWASP MCP Top 10 med uradne vire

## 18. december 2025

### Posodobitev varnostne dokumentacije - MCP specifikacija 2025-11-25

#### MCP Varnostne najboljše prakse (02-Security/mcp-best-practices.md) - Posodobitev verzije specifikacije
- **Posodobitev verzije protokola**: Posodobljen sklic na najnovejšo MCP specifikacijo 2025-11-25 (izdana 25. novembra 2025)
  - Posodobljeni vsi sklici na verzijo specifikacije iz 2025-06-18 na 2025-11-25
  - Posodobljeni datumski sklici dokumenta iz 18. avgusta 2025 na 18. december 2025
  - Preverjene vse URL povezave na specifikacije za trenutno dokumentacijo
- **Validacija vsebine**: Celovita validacija varnostnih najboljših praks glede na najnovejše standarde
  - **Microsoft Security Solutions**: Preverjena trenutna terminologija in povezave za Prompt Shields (prej "odkrivanje tveganja jailbreak"), Azure Content Safety, Microsoft Entra ID in Azure Key Vault
  - **OAuth 2.1 varnost**: Potrjena usklajenost z najnovejšimi varnostnimi najboljšimi praksami za OAuth
  - **OWASP standardi**: Preverjeni sklici na OWASP Top 10 za LLM ostajajo aktualni
  - **Azure storitve**: Preverjene vse povezave do Microsoft Azure dokumentacije in varnostnih najboljših praks
- **Standardi usklajenosti**: Vsi sklicani varnostni standardi so potrjeni kot aktualni
  - NIST okvir za upravljanje tveganj AI
  - ISO 27001:2022
  - OAuth 2.1 varnostne najboljše prakse
  - Okviri za varnost in skladnost Azure
- **Viri za implementacijo**: Preverjeni vsi vodiči in viri za implementacijo
  - Avtentikacijski vzorci upravljanja API Azure
  - Vodiči za integracijo Microsoft Entra ID
  - Upravljanje skrivnosti Azure Key Vault
  - DevSecOps cevovodi in rešitve za nadzor

### Zagotavljanje kakovosti dokumentacije
- **Skladnost s specifikacijo**: Zagotovljena usklajenost vseh obveznih MCP varnostnih zahtev (MORA/MORA NE) z najnovejšo specifikacijo
- **Aktualnost virov**: Preverjene vse zunanje povezave do Microsoft dokumentacije, varnostnih standardov in vodičev za implementacijo
- **Pokritost najboljših praks**: Potrjena celovita pokritost avtentikacije, avtorizacije, AI-specifičnih groženj, varnosti dobavne verige in enterprise vzorcev

## 6. oktober 2025

### Razširitev začetnega razdelka – Napredna uporaba strežnika & preprosta avtentikacija

#### Napredna uporaba strežnika (03-GettingStarted/10-advanced)
- **Dodano novo poglavje**: Predstavljen celovit vodič za napredno uporabo MCP strežnika, ki zajema redne in nizkonivojske strežniške arhitekture.
  - **Redni vs. nizkonivojski strežnik**: Podrobna primerjava in primeri kode v Python in TypeScript za oba pristopa.
  - **Oblikovanje na osnovi upravljavcev**: Pojasnilo upravljanja orodij/virov/pozivov z upravljavci za razširljive in prilagodljive strežniške implementacije.
  - **Praktični vzorci**: Resnični scenariji, kjer so vzorci nizkonivojskega strežnika koristni za napredne funkcije in arhitekturo.

#### Preprosta avtentikacija (03-GettingStarted/11-simple-auth)
- **Dodano novo poglavje**: Vodič po korakih za implementacijo preproste avtentikacije v MCP strežnikih.
  - **Koncepti avtentikacije**: Jasno pojasnilo avtentikacije v primerjavi z avtorizacijo in obravnavo poverilnic.
  - **Implementacija osnovne avtentikacije**: Vzorec middleware avtentikacije v Python (Starlette) in TypeScript (Express) s primeri kode.
  - **Napredovanje k napredni varnosti**: Navodila za začetek s preprosto avtentikacijo in nadaljevanje na OAuth 2.1 ter RBAC, s sklici na napredne varnostne module.

Te dodatke ponujajo praktična, izkušena navodila za gradnjo bolj robustnih, varnih in prilagodljivih MCP strežniških implementacij, ki povezujejo osnovne koncepte z naprednimi proizvodnimi vzorci.

## 29. september 2025

### Laboratoriji za integracijo MCP strežnika z bazami podatkov - celovit praktični učni načrt

#### 11-MCPServerHandsOnLabs - nov celovit učni načrt za integracijo baz podatkov
- **Celovit učni niz 13 laboratorijev**: Dodan celovit praktični učni načrt za gradnjo MCP strežnikov primeren za produkcijo z integracijo PostgreSQL baze podatkov
  - **Resnične primere uporabe**: Primer analitike Zava Retail kot vzorec enterprise razredov vzorcev
  - **Strukturiran potek učenja**:
    - **Laboratoriji 00-03: Osnove** - Uvod, osnovna arhitektura, varnost in multi-tenancy, nastavitve okolja
    - **Laboratoriji 04-06: Gradnja MCP strežnika** - Oblikovanje baze podatkov in sheme, implementacija MCP strežnika, razvoj orodij  
    - **Laboratoriji 07-09: Napredne funkcije** - Integracija semantičnega iskanja, testiranje in odpravljanje napak, integracija z VS Code
    - **Laboratoriji 10-12: Produkcija in najboljše prakse** - Strategije nameščanja, nadzor in opazovanje, najboljše prakse in optimizacija
  - **Enterprise tehnologije**: Okvir FastMCP, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Napredne funkcije**: Varnost na ravni vrstic (RLS), semantično iskanje, dostop do podatkov za več najemnikov, vektorske upodobitve, nadzor v realnem času

#### Standardizacija terminologije - pretvorba modulov v laboratorije
- **Celovita posodobitev dokumentacije**: Sistematsko posodobljeni vsi README-ji v 11-MCPServerHandsOnLabs z uporabo terminologije "Laboratorij" namesto "Modul"
  - **Naslovi odsekov**: Posodobljeno "Kaj zajema ta modul" v "Kaj zajema ta laboratorij" v vseh 13 laboratorijih
  - **Opis vsebine**: Spremenjeno z "Ta modul ponuja..." v "Ta laboratorij ponuja..." v celotni dokumentaciji
  - **Učne cilje**: Posodobljeno "Ob koncu tega modula..." v "Ob koncu tega laboratorija..."
  - **Navigacijske povezave**: Vse reference "Modul XX:" spremenjene v "Laboratorij XX:" v prekrižnih sklicih in navigaciji
  - **Sledenje dokončanju**: Posodobljeno "Po zaključku tega modula..." v "Po zaključku tega laboratorija..."
  - **Ohranjeni tehnični sklici**: Ohranili sklice na Python module v konfiguracijskih datotekah (npr. `"module": "mcp_server.main"`)

#### Izboljšave učnega vodiča (study_guide.md)
- **Vizualna karta učnega načrta**: Dodan nov razdelek "11. Laboratoriji za integracijo baz podatkov" s celovito vizualizacijo strukture laboratorijev
- **Struktura repozitorija**: Posodobljeno z deset na enajst glavnih razdelkov z podrobnim opisom 11-MCPServerHandsOnLabs
- **Navodila za učno pot**: Izboljšane navigacijske smernice za razdelke 00-11
- **Pokritost tehnologije**: Dodani podatki o FastMCP, PostgreSQL in integraciji Azure storitev
- **Izidi učenja**: Poudarjena pripravljenost na produkcijsko razvoj strežnika, vzorci integracije baz podatkov in enterprise varnost

#### Izboljšave strukture glavnega README
- **Terminologija na osnovi laboratorijev**: Posodobljen glavni README.md v 11-MCPServerHandsOnLabs za dosledno uporabo strukture "Laboratorij"
- **Organizacija učne poti**: Jasna progresija od osnovnih konceptov do napredne implementacije in produkcijskega nameščanja
- **Usmerjenost k resničnemu svetu**: Poudarek na praktičnem, izkustvenem učenju z vzorci in tehnologijami enterprise razreda

### Izboljšave kakovosti in doslednosti dokumentacije
- **Poudarek na praktičnem učenju**: Okrepljen praktičen, laboratorijski pristop skozi vso dokumentacijo
- **Fokus na enterprise vzorce**: Izpostavljene produkcijsko pripravljene implementacije in varnostne zahteve za podjetja
- **Integracija tehnologije**: Celovita pokritost modernih Azure storitev in AI integracijskih vzorcev
- **Progresija učenja**: Jasna, strukturirana pot od osnovnih konceptov do produkcijskega nameščanja

## 26. september 2025

### Izboljšave primerov uporabe - integracija GitHub MCP Registry

#### Primeri uporabe (09-CaseStudy/) - fokus na razvoj ekosistema
- **README.md**: Obsežna razširitev z izčrpnim študijem primera GitHub MCP Registry
  - **Študija primera GitHub MCP Registry**: Novi celovit študij primera, ki pregleduje lansiranje GitHubove MCP Registry septembra 2025
    - **Analiza problema**: Podrobna obravnava fragmentiranega odkrivanja in nameščanja MCP strežnikov
    - **Arhitektura rešitve**: Centraliziran pristop z registracijo GitHub z namestitvijo VS Code z enim klikom
    - **Poslovni vpliv**: Merljive izboljšave uvajanja razvijalcev in produktivnosti
    - **Strateška vrednost**: Fokus na modularno nameščanje agentov in interoperabilnost med orodji
    - **Razvoj ekosistema**: Pozicioniranje kot temeljna platforma za agentno integracijo
  - **Izboljšana struktura študije primera**: Posodobljeni vsi sedem študij primerov z doslednim formatiranjem in celovitimi opisi
    - Azure AI Travel Agents: Poudarek na orkestraciji več agentov
    - Integracija Azure DevOps: Poudarek na avtomatizaciji delovnih tokov
    - Pridobivanje dokumentacije v realnem času: Implementacija Python konzolnega odjemalca
    - Interaktivni generator študijskih načrtov: Pogovorna spletna aplikacija Chainlit
    - Dokumentacija znotraj urejevalnika: Integracija VS Code in GitHub Copilot
    - Azure API Management: Vzorci integracije enterprise API
    - GitHub MCP Registry: Razvoj ekosistema in skupnostna platforma
  - **Celovit zaključek**: Predelani zaključni del, ki poudarja sedem študij primerov, ki zajemajo različne dimenzije MCP implementacije
    - Integracija v podjetju, orkestracija več agentov, produktivnost razvijalcev
    - Razvoj ekosistema, kategorizacija izobraževalnih aplikacij
    - Izboljšani vpogledi v arhitekturne vzorce, strategije implementacije in najboljše prakse
    - Poudarek na MCP kot zrelem, proizvodno pripravljenem protokolu

#### Posodobitve učnega vodiča (study_guide.md)
- **Vizualna karta učnega načrta**: Posodobljen miselni zemljevid za vključitev GitHub MCP Registry v razdelek primerov uporabe
- **Opis primerov uporabe**: Izboljšan iz generičnih opisov v podrobno razčlenitev sedmih celovitih študij primerov
- **Struktura repozitorija**: Posodobljen razdelek 10 za odražanje celovite pokritosti študij primerov s specifičnimi podrobnostmi implementacije
- **Integracija dnevnika sprememb**: Dodan zapis 26. septembra 2025, ki dokumentira dodatek GitHub MCP Registry in izboljšave študij primerov
- **Posodobitve datumov**: Posodobljen časovni žig v nogi dokumenta za prikaz najnovejše revizije (26. september 2025)

### Izboljšave kakovosti dokumentacije
- **Izboljšanje doslednosti**: Standardizirano formatiranje in strukturo študij primerov v vseh sedmih primerih
- **Celovita pokritost**: Študije primerov zdaj zajemajo scenarije za podjetja, produktivnost razvijalcev in razvoj ekosistema
- **Strateško pozicioniranje**: Izboljšan fokus na MCP kot temeljno platformo za implementacijo sistemov z agenti
- **Integracija virov**: Posodobljeni dodatni viri za vključitev povezave do GitHub MCP Registry

## 15. september 2025

### Razširitev naprednih tem - prilagojeni transporti in inženiring konteksta

#### Prilagojeni MCP transporti (05-AdvancedTopics/mcp-transport/) - Nov vodič za napredno implementacijo
- **README.md**: Celovit vodič za implementacijo prilagojenih transportnih mehanizmov MCP
  - **Azure Event Grid transport**: Celovita implementacija transporta, temelječega na dogodkih brez strežnika
    - Primeri C#, TypeScript in Python z integracijo Azure Functions
    - Vzorci arhitekture, vodene z dogodki, za razširljive rešitve MCP
    - Sprejemniki webhookov in push obdelava sporočil
  - **Azure Event Hubs transport**: Implementacija transporta s pretočnim prenosom velike prepustnosti
    - Zmožnosti pretočnega prenosa za scenarije z nizko latenco v realnem času
    - Strategije particioniranja in upravljanje kontrolnih točk
    - Paketizacija sporočil in optimizacija zmogljivosti
  - **Vzorec integracije v podjetjih**: Primeri arhitekture pripravljeni za produkcijo
    - Distribuirano MCP procesiranje preko več Azure Functions
    - Hibridne arhitekture transporta, ki kombinirajo več vrst transporta
    - Strategije trajnosti sporočil, zanesljivosti in obdelave napak
  - **Varnost in nadzor**: Integracija z Azure Key Vault in vzorci opazovanja
    - Avtentikacija z upravljano identiteto in najmanjše pravice dostopa
    - Telemetrija Application Insights in nadzor zmogljivosti
    - Vzorci odklopnikov in toleranca na napake
  - **Testni okvirji**: Celovite testne strategije za prilagojene transporte
    - Enotni testi z uporabo dvojnikov in orodij za ponarejanje
    - Integracijski testi z Azure Test Containers
    - Premisleki glede zmogljivosti in testiranja obremenitve

#### Inženiring konteksta (05-AdvancedTopics/mcp-contextengineering/) - Rastoča AI disciplina
- **README.md**: Celovita raziskava inženiringa konteksta kot rastočega področja
  - **Temeljna načela**: Popolno deljenje konteksta, zavedanje odločanja o akcijah in upravljanje okna konteksta

  - **Usklajenost protokola MCP**: Kako načrt MCP naslavlja izzive inženiringa konteksta
    - Omejitve kontekstnega okna in strategije progresivnega nalaganja
    - Določanje pomembnosti in dinamično pridobivanje konteksta
    - Upravljanje multimodalnega konteksta in varnostni vidiki
  - **Pristopi k implementaciji**: Enonitni proti večagentnim arhitekturam
    - Tehnike razdelitve in prioritizacije kontekstnih odsekov
    - Strategije progresivnega nalaganja in stiskanja konteksta
    - Plastni pristopi h kontekstu in optimizacija pridobivanja
  - **Merilni okvir**: Nastajajoče metrike za ocenjevanje učinkovitosti konteksta
    - Učinkovitost vnosa, zmogljivost, kakovost in uporabniška izkušnja
    - Eksperimentalni pristopi k optimizaciji konteksta
    - Analiza napak in metodologije izboljšav

#### Posodobitve navigacije kurikula (README.md)
- **Izboljšana struktura modulov**: Posodobljena tabela kurikula za vključitev novih naprednih tem
  - Dodani vnosi za Inženiring konteksta (5.14) in Prilagojeni transport (5.15)
  - Konsistentna oblika in navigacijske povezave v vseh modulih
  - Posodobljeni opisi za odražanje trenutnega obsega vsebine

### Izboljšave strukture imenika
- **Standardizacija poimenovanja**: Preimenovan "mcp transport" v "mcp-transport" za usklajenost z ostalimi mapami naprednih tem
- **Organizacija vsebine**: Vsi imeniki 05-AdvancedTopics sedaj sledijo doslednemu vzorcu imenovanja (mcp-[tema])

### Izboljšave kakovosti dokumentacije
- **Usklajenost specifikacije MCP**: Vsa nova vsebina se sklicuje na trenutno specifikacijo MCP 2025-06-18
- **Primeri v več jezikih**: Celoviti primeri kode v C#, TypeScript in Python
- **Poudarek na podjetjih**: Vzorce pripravljene za produkcijo in integracijo Azure oblaka povsod
- **Vizualna dokumentacija**: Mermaid diagrami za vizualizacijo arhitekture in tokov

## 18. avgust 2025

### Celovita posodobitev dokumentacije - standardi MCP 2025-06-18

#### Najboljše varnostne prakse MCP (02-Security/) - Popolna modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Popolno prepisovanje usklajeno s specifikacijo MCP 2025-06-18
  - **Obvezne zahteve**: Dodane eksplicitne zahteve MORATE/NIKOLI ne smete iz uradne specifikacije z jasnimi vizualnimi indikatorji
  - **12 osnovnih varnostnih praks**: Prenovljeno iz 15 elementov v celovita varnostna področja
    - Varnost žetonov in overjanje z integracijo zunanjega ponudnika identitete
    - Upravljanje sej in varnost transporta s kriptografskimi zahtevami
    - Zaščita pred napadi, specifičnimi za AI, z integracijo Microsoft Prompt Shields
    - Upravljanje dostopa in dovoljenj s principom najmanjše privilegije
    - Varnost vsebine in nadzor z integracijo Azure Content Safety
    - Varnost dobavne verige s celovito verifikacijo komponent
    - Varnost OAuth in preprečevanje napadov "Confused Deputy" z izvedbo PKCE
    - Odziv na incident in okrevanje z avtomatiziranimi zmogljivostmi
    - Skladnost in upravljanje z usklajenostjo z regulativami
    - Napredni varnostni nadzori z arhitekturo ničelnega zaupanja
    - Integracija Microsoftovega varnostnega ekosistema s celovitimi rešitvami
    - Neprestan razvoj varnosti z adaptivnimi praksami
  - **Microsoftove varnostne rešitve**: Izboljšana navodila za integracijo Prompt Shields, Azure Content Safety, Entra ID in GitHub Advanced Security
  - **Viri za implementacijo**: Kategorizirane celovite povezave do virov med uradno MCP dokumentacijo, Microsoftovimi varnostnimi rešitvami, varnostnimi standardi in vodniki za implementacijo

#### Napredni varnostni nadzori (02-Security/) - Podjetniška implementacija
- **MCP-SECURITY-CONTROLS-2025.md**: Popolna prenova s podjetniškim varnostnim okvirom
  - **9 celovitih varnostnih področij**: Razširjena iz osnovnih nadzorov v podrobnejši okvir za podjetja
    - Napredno overjanje in avtorizacija z integracijo Microsoft Entra ID
    - Varnost žetonov in nadzori proti passtrough z obsežno validacijo
    - Nadzori varnosti sej s preprečevanjem zasedbe
    - Specifični varnostni nadzori za AI s preprečevanjem vbrizgavanja pozivov in zastrupljanja orodij
    - Preprečevanje napadov "Confused Deputy" z varnostjo OAuth proxyja
    - Varnost izvajanja orodij s peskovnikom in izolacijo
    - Varnostni nadzori dobavne verige z verifikacijo odvisnosti
    - Nadzorni in zaznavni nadzori z integracijo SIEM
    - Odziv na incidente in okrevanje z avtomatiziranimi zmogljivostmi
  - **Primeri implementacije**: Dodani podrobni blok YAML konfiguracij in primeri kode
  - **Integracija Microsoftovih rešitev**: Celovito pokritje Azure varnostnih storitev, GitHub Advanced Security in upravljanje identitete podjetja

#### Varnost naprednih tem (05-AdvancedTopics/mcp-security/) - Implementacija pripravljenja za produkcijo
- **README.md**: Popoln prepis za implementacijo varnosti v podjetjih
  - **Usklajenost s trenutno specifikacijo**: Posodobljeno na MCP specifikacijo 2025-06-18 z obveznimi varnostnimi zahtevami
  - **Izboljšano overjanje**: Integracija Microsoft Entra ID z obsežnimi primeri za .NET in Java Spring Security
  - **Integracija varnosti AI**: Izvedba Microsoft Prompt Shields in Azure Content Safety z podrobnimi primeri v Pythonu
  - **Napredna mitigacija groženj**: Celoviti primeri implementacije za
    - Preprečevanje napadov "Confused Deputy" z PKCE in validacijo uporabniškega soglasja
    - Preprečevanje prehoda žetonov z validacijo občinstva in varnim upravljanjem žetonov
    - Preprečevanje zasedbe sej z uporabo kriptografske vezave in vedenjske analize
  - **Integracija varnosti podjetja**: Nadzor z Azure Application Insights, detekcijski kanali za grožnje in varnost dobavne verige
  - **Kontrolni seznam za implementacijo**: Jasni obvezni in priporočeni varnostni nadzori z ugodnostmi Microsoftovega varnostnega ekosistema

### Kakovost dokumentacije in usklajenost standardov
- **Reference specifikacij**: Posodobljene vse reference na trenutno MCP specifikacijo 2025-06-18
- **Microsoftov varnostni ekosistem**: Izboljšana navodila za integracijo skozi celotno varnostno dokumentacijo
- **Praktična implementacija**: Dodani podrobni primeri kode v .NET, Java in Python z vzorci za podjetja
- **Organizacija virov**: Celovita kategorizacija uradne dokumentacije, varnostnih standardov in vodnikov za implementacijo
- **Vizualni indikatorji**: Jasna označitev obveznih zahtev v primerjavi s priporočanimi praksami


#### Temeljni koncepti (01-CoreConcepts/) - Popolna modernizacija
- **Posodobitev različice protokola**: Posodobljena za sklicevanje na trenutno MCP specifikacijo 2025-06-18 z datumskim verzioniranjem (format LLLL-MM-DD)
- **Izpopolnitev arhitekture**: Izboljšani opisi gostiteljev, odjemalcev in strežnikov za prikaz trenutnih vzorcev MCP arhitekture
  - Gostitelji so zdaj jasno definirani kot AI aplikacije, ki koordinirajo več MCP odjemalskih povezav
  - Odjemalci opisani kot protokolarni konektorji vzdržujejo ena-na-ena odnos s strežniki
  - Strežniki izboljšani z lokalnimi in oddaljenimi scenariji razmestitve
- **Prenova primitivov**: Popolna prenova strežniških in odjemalskih primitivov
  - Strežniški primitiv: Viri (viri podatkov), Pozivi (predloge), Orodja (izvedljive funkcije) z podrobnimi razlagami in primeri
  - Odjemalski primitiv: Vzorcevanje (LLM dokončanja), Pridobivanje (uporabniški vnos), Beleženje (razhroščevanje/nadzor)
  - Posodobljeno z aktualnimi vzorci metod za iskanje (`*/list`), pridobivanje (`*/get`) in izvrševanje (`*/call`)
- **Arhitektura protokola**: Predstavljen dvoplastni arhitekturni model
  - Plasti podatkov: osnova JSON-RPC 2.0 z upravljanjem življenjskega cikla in primitivov
  - Transportna plast: STDIO (lokalni) in HTTP z možnostjo pretočnega SSE (oddaljeni) transportni mehanizmi
- **Varnostni okvir**: Celoviti varnostni principi, vključno z eksplicitnim uporabniškim soglasjem, varstvom zasebnosti podatkov, varnostjo izvajanja orodij in varnostjo transportne plasti
- **Vzorci komunikacije**: Posodobljena sporočila protokola za prikaz inicializacije, iskanja, izvrševanja in obveščanja
- **Primeri kode**: Osveženi primeri v več jezikih (.NET, Java, Python, JavaScript) za odražanje aktualnih vzorcev MCP SDK

#### Varnost (02-Security/) - Celovita prenova varnosti  
- **Usklajenost standardov**: Polna uskladitev z varnostnimi zahtevami MCP specifikacije 2025-06-18
- **Evolucija overjanja**: Dokumentirana evolucija od lastnih OAuth strežnikov do delegacije zunanjega ponudnika identitete (Microsoft Entra ID)
- **Analiza groženj, specifičnih za AI**: Izboljšano pokritje sodobnih AI načinov napadov
  - Podrobni scenariji napadov z vbrizgavanjem pozivov s praktičnimi primeri
  - Mehanizmi zastrupljanja orodij in vzorci napadov »rug pull«
  - Zastrupljanje kontekstnih oken in zmeda modela
- **Microsoftove varnostne rešitve za AI**: Celovita pokritost Microsoftovega varnostnega ekosistema
  - AI Prompt Shields z naprednim zaznavanjem, poudarjanjem in tehnikami ločilcev
  - Vzorci integracije Azure Content Safety
  - GitHub Advanced Security za zaščito dobavne verige
- **Napredna mitigacija groženj**: Podrobni varnostni nadzori za
  - Zasedbe sej s posebnimi MCP napadi in kriptografskimi zahtevami za ID sej
  - Težave z "Confused Deputy" v MCP proxy scenarijih z eksplicitnimi zahtevami za soglasje
  - Ranljivosti prehoda žetonov z obveznimi kontrolami validacije
- **Varnost dobavne verige**: Razširjeno pokritje obstoječih AI dobavnih verig, vključno z osnovnimi modeli, storitvami vdelav, ponudniki konteksta in API-ji tretjih oseb
- **Varnost temeljev**: Izboljšana integracija s podjetniškimi varnostnimi vzorci, vključno z arhitekturo ničelnega zaupanja in Microsoftovim varnostnim ekosistemom
- **Organizacija virov**: Kategorizirane celovite povezave do virov glede na vrsto (uradni dokumenti, standardi, raziskave, Microsoftove rešitve, implementacijski vodniki)

### Izboljšave kakovosti dokumentacije
- **Strukturirani učni cilji**: Izboljšani učni cilji z jasnimi, izvedljivimi rezultati
- **Navzkrižne reference**: Dodane povezave med sorodnimi varnostnimi in temeljnimi temami
- **Posodobljene informacije**: Posodobljene vse datumske reference in povezave na standarde
- **Smernice za implementacijo**: Dodane specifične, izvedljive smernice za implementacijo v obeh sekcijah

## 16. julij 2025

### Posodobitve README in navigacije
- Popolnoma prenovljena navigacija kurikula v README.md
- Zamenjani `<details>` oznake z bolj dostopno obliko v tabeli
- Ustvarjene alternativne možnosti postavitve v novi mapi "alternative_layouts"
- Dodani primeri navigacije z karticami, zavihki in harmoniko
- Posodobljen odsek strukture repozitorija za vključitev vseh najnovejših datotek
- Izboljšan odsek "Kako uporabljati ta kurikul" z jasnimi priporočili
- Posodobljene povezave do specifikacij MCP, ki kažejo na pravilne URL-je
- Dodan odsek Inženiring konteksta (5.14) v strukturo kurikula

### Posodobitve študijskega vodnika
- Popolnoma prenovljen študijski vodnik za usklajenost s trenutno strukturo repozitorija
- Dodani novi odseki za MCP odjemalce in orodja ter priljubljene MCP strežnike
- Posodobljena vizualna karta kurikula za natančno odražanje vseh tem
- Izboljšani opisi naprednih tem za pokrivanje vseh specializiranih področij
- Posodobljen odsek študij primerov za odražanje dejanskih primerov
- Dodan ta celovit dnevnik sprememb

### Prispevki skupnosti (06-CommunityContributions/)
- Dodane podrobne informacije o MCP strežnikih za generiranje slik
- Dodan celovit odsek o uporabi Claude v VSCode
- Dodana navodila za nastavitev in uporabo Cline terminalskega odjemalca
- Posodobljen oddelek MCP odjemalcev za vključitev vseh priljubljenih odjemalcev
- Izboljšani primeri prispevkov z natančnejšimi primeri kode

### Napredne teme (05-AdvancedTopics/)
- Organizirane vse specializirane mape tem z doslednim poimenovanjem
- Dodano gradivo in primeri za inženiring konteksta
- Dodana dokumentacija za integracijo agenta Foundry
- Izboljšana dokumentacija integracije varnosti Entra ID

## 11. junij 2025

### Začetna ustvaritev
- Izšla prva različica kurikula MCP za začetnike
- Ustvarjena osnovna struktura za vseh 10 glavnih sklopov
- Izvedena vizualna karta kurikula za navigacijo
- Dodani začetni primeri projektov v več programskih jezikih

### Začetek (03-GettingStarted/)
- Ustvarjeni prvi primeri implementacije strežnika
- Dodana navodila za razvoj odjemalcev
- Vključena navodila za integracijo LLM odjemalcev
- Dodana dokumentacija integracije v VS Code
- Izvedeni primeri strežnikov s strežbenimi dogodki (SSE)

### Temeljni koncepti (01-CoreConcepts/)
- Dodano podrobno pojasnilo arhitekture odjemalec-strežnik
- Ustvarjena dokumentacija o ključnih komponentah protokola
- Dokumentirani vzorci sporočanja v MCP

## 23. maj 2025

### Struktura repozitorija
- Iniciran repozitorij z osnovno mapno strukturo
- Ustvarjene datoteke README za vsak večji odsek
- Nastavljena infrastruktura za prevajanje
- Dodana slikovna gradiva in diagrami

### Dokumentacija
- Ustvarjen začetni README.md s pregledom kurikula
- Dodana datoteka CODE_OF_CONDUCT.md in SECURITY.md
- Nastavljen SUPPORT.md z navodili za pomoč
- Ustvarjena preliminarna struktura študijskega vodnika

## 15. april 2025

### Načrtovanje in okvir
- Začetno načrtovanje kurikula MCP za začetnike
- Določeni učni cilji in ciljna publika
- Načrtovana struktura z 10 sklopi kurikula
- Razvit konceptualni okvir za primere in študije primerov
- Ustvarjeni začetni prototipni primeri ključnih konceptov

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->