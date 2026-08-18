# Dnevnik promjena: MCP za početnike plan učenja

Ovaj dokument služi kao zapis svih značajnih promjena napravljenih u modelu nastave Model Context Protocol (MCP) za početnike. Promjene su dokumentirane u obrnutom kronološkom redoslijedu (najnovije promjene prve).

## 29. srpnja 2026.

### Novi modul 08 pratilac: Pouzdanost pomoćnih programa i sigurna ponovna pokušaja

Dodana je vendor-neutralna pratiteljska lekcija za MCP alate koji stvaraju stvarne
učinke, usklađena s konačnom specifikacijom `2026-07-28`.

- **Novo**: [pratiteljska lekcija o pouzdanosti pomoćnih programa][reliability-sidecar]
  koristi jednu priču o podršci, dva Mermaid dijagrama i tok
  odluke o ponovnom pokušaju za objašnjenje ključeva stabilnog rada, atomskog prihvata dupliciranih zahtjeva,
  usklađivanja, dokaza i granice proširenja Zadataka.
- **Novo**: Vježba umetanju grešaka u Pythonu i SQLite iz standardne biblioteke
  koristi odvojene trgovine operacija i zahtjeva da pokaže odgovor koji je izgubljen
  nakon što se vanjski učinak potvrdi. Šest determinističkih testova pokrivaju naivne
  duplikacije, zaštićeni oporavak od ponovnog pokretanja, sukobe podataka, keširane rezultate,
  aktivne zahtjeve i istovremene duplicirane prijeme.
- **Ažurirano**: Modul 08 sada povezuje pratiteljsku lekciju, identificira
  konačni model bezstanja zahtjeva `2026-07-28`, razlikuje OpenTelemetry
  promatranje od zastarjele MCP značajke zapisivanja i ograničava njegov
  generički primjer ponovnog pokušaja na operacije samo za čitanje.
- **Opcionalno**: Lekcija preslikava svoje prenosive koncepte na jednu označenu zajedničku
  implementaciju bez uključivanja hostirane usluge ili mrežnog poziva kao dijela
  vježbe.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. srpnja 2026.

### Nova lekcija: MCP specifikacija 2026-07-28 kandidat za izdanje

Dodano pokrivanje nadolazećeg kandidata za izdanje specifikacije MCP `2026-07-28` (najavljeno 21. svibnja 2026.; konačno izdanje zakazano za 28. srpnja 2026.), sažeto iz [službenog blog posta](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Osnovna verzija plana učenja ostaje **MCP Specifikacija 2025-11-25** dok nova verzija ne bude objavljena, stoga je ovo predstavljeno kao buduće usmjerenje, a ne prepisivanje postojećih lekcija.

- **Novo**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — cijela lekcija koja pokriva jezgru protokola bez stanja (uklanjanje rukovanja `initialize` i `Mcp-Session-Id`), nove zaglavlja za usmjeravanje `Mcp-Method`/`Mcp-Name`, metapodatke keširanja `ttlMs`/`cacheScope`, W3C Trace Context u `_meta`, formalni okvir proširenja (MCP aplikacije i novo proširenje Zadataka), šest SEP-ova za jačanje autorizacije, zastarijevanje Roots/Sampling/Logging i prelazak na potpuni JSON Schema 2020-12 za sheme alata.
- **Ažurirano** s budućim uputama koje vode do nove lekcije:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): bilješka o verziji protokola, odjeljci Sampling/Roots/Logging/Tasks i "Što slijedi"
  - [02-Security/README.md](./02-Security/README.md): napomena o jačanju autorizacije
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): napomena o transportu bez stanja
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): upozorenje o zastarijevanju uzorkovanja
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): upozorenje o zastarijevanju zapisivanja i o proširenju Zadataka
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): napomena o bezstanja/usmjeravanju sesije
  - [README.md](./README.md): bilješka "Gledajući unaprijed" u odjeljku specifikacije i novi unos `1.1` u tablici modula kurikuluma
  - [study_guide.md](./study_guide.md): buduća točka u pregledu osnovnih pojmova i datumirana bilješka dodatka
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): napomena o karti transporta `mcp-session-id` prije modela zahtjeva bez stanja
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): obrada modula s pregledom o zastarijevanju Root Contexts/Sampling i proširenju Zadataka
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): napomena o jačanju autorizacije

## 24. lipnja 2026.

### Nova lekcija: Korištenje MCP u aplikaciji Copilot

- [Odjeljak Alati](./12-tooling/README.md) Dodan odjeljak alata.
- [MCP u aplikaciji Copilot](./12-tooling/01-copilot-app/README.md)

## 16. lipnja 2026.

### Usklađivanje specifikacije MCP i validacija uzoraka

Validiran je kurikulum prema trenutnoj **MCP specifikaciji 2025-11-25** i najnovijim službenim SDK-ovima, zatim su ispravljene preostale zastarjele reference na specifikaciju i potvrđeno je da se osnovni uzorci još uvijek sastavljaju i izvršavaju.

#### Ispravci verzije specifikacije (2025-06-18 / 2025-03-26 → 2025-11-25)

Ažuriran je sadržaj na engleskom gdje je još tvrdio da je starija revizija specifikacije *trenutni/najnoviji* standard i linkovi su usmjereni na kanoničke specifikacijske putanje `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Ažuriran banner "Trenutni standard", uvod, odjeljak o osnovnim sigurnosnim principima, obavezni zahtjevi, dio o Microsoft Entra ID, linkovi na reference i resurse, te zaključna sigurnosna napomena (8 referenci) na 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Ažuriran link na dodatne resurse i banner "Trenutni standard" na 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Zamijenjen zastarjeli link sigurnosti i povjerenja `2025-03-26` s trenutačnom stranicom najboljih sigurnosnih praksi 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Ažuriran službeni link za uzorkovanje na 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Ažurirane reference o "trenutnoj MCP specifikaciji" u sadašnjem vremenu i link na dodatne resurse na 2025-11-25 (povijesne bilješke o zastarijevanju SSE ostavljene radi točnosti)

#### Validacija uzoraka prema aktualnim SDK-ovima

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` instalirao `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` prošao bez grešaka tipa — postojeći API-ji `McpServer`/`StdioServerTransport` ostaju valjani
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validirano u izoliranom `.venv` s `mcp[cli]` (1.27.2); `py_compile` prošao i `FastMCP.list_tools()` ispravno vratio alate `add` i `subtract`
- Potvrđeno da svi uzorci s deklariranim verzijama `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) uredno rješavaju trenutačni `1.29.0` bez prekida API-ja

#### Poravnanje pin-ova ovisnosti (zatvaranje verzijskih praznina)

Ažurirani su zastarjeli pinovi SDK-a tako da svaki uzorak prati trenutačno MCP izdanje, u skladu s konvencijom cijelog repozitorija:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Ažurirano `@modelcontextprotocol/sdk` s `^1.8.0` na `>=1.26.0` i opis paketa `"updated for MCP 2025-06-18"` zamijenjen s `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** i **lab4/code/github_mcp_server/pyproject.toml**: Ažuriran precizni pin `mcp==1.23.0` na `mcp>=1.26.0`; regenerirane su obje datoteke `uv.lock` (`uv lock`) kako bi se osiguralo da se datoteke zaključavanja rješavaju na trenutačni `mcp 1.27.2` i da ostanu sinkronizirane s manifestima

#### Analiza praznina kurikuluma — pokrivenost najnovijih značajki specifikacije

Potvrđeno je da kurikulum već pokriva sve primitivne funkcije uvedene/razrađene u MCP 2025-11-25, tako da nema praznina u sadržaju:
- **Sampling (uzorkovanje)**: Lekcija 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (uključujući URL način rada)**: Dokumentirano u 01-CoreConcepts i 05-AdvancedTopics/mcp-protocol-features
- **Roots (Korijeni)**: Dokumentirano u 00-Introduction, 01-CoreConcepts i 05-AdvancedTopics/mcp-root-contexts
- **Tasks (zadatci; eksperimentalni, dugotrajni poslovi)**: Dokumentirano u 01-CoreConcepts i 05-AdvancedTopics/mcp-protocol-features
- **Bilješke o alatima** (`readOnlyHint` / `destructiveHint`): Dokumentirano u 01-CoreConcepts i 05-AdvancedTopics/mcp-protocol-features

### Pojačanje sigurnosti i otklanjanje ranjivosti ovisnosti

Proveden je potpuni sigurnosni pregled svih manifestnih datoteka ovisnosti i izvornog koda primjera, zatim su otklonjena sva prijavljena upozorenja iz npm-a i jedna sigurnosna pronađena ranjivost u kodu. Nakon ispravke, `npm audit` izvještava o **0 ranjivosti** u svim provjerenim mapama.

#### npm ranjivosti ovisnosti (prijenosne) — Ispravljeno

Pregledano svih 15 predanih `package-lock.json` datoteka. Ranjivosti su bile ograničene na prijenosne ovisnosti koje povlače alat za razvoj MCP Inspectora, OpenAI klijent i MCP SDK; svi su sada riješeni bez prekida uzoraka:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** i **lab3/code/weather_mcp/inspector**: Nadograđen `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), što je uklonilo sav bundlovani `ajv`, `brace-expansion`, `diff`, `path-to-regexp` i `ws` sigurnosni problemi. Dodan je npm unos `overrides` koji forsira popravljeni `shell-quote@1.8.4` da ukloni preostala kritična upozorenja koja je nosio `concurrently`; obje datoteke zaključavanja ponovno generirane (sada 0 ranjivosti)
- **03-GettingStarted/samples/typescript**: `npm audit fix` ažurirao prijenosni `qs` (umjerene) u popravljenu verziju
- **03-GettingStarted/samples/javascript**: `npm audit fix` ažurirao prijenosni `hono` (umjerene) u popravljenu verziju
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` ažurirao prijenosni `form-data` (visoke) u popravljenu verziju
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generirana nedostajuća `package-lock.json` datoteka za reproduktivnost i auditabilnost projekta (0 ranjivosti)

#### Sigurnosna ispravka na razini koda (OWASP A03: Umetanje)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Uklonjen `shell=True` iz alata `open_in_vscode`. Prethodni `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` dopuštao je da shell metaznakovi u putanji mape budu interpretirani od strane `cmd.exe` (vektor za injekciju naredbi). Sada se izravno pokreće razriješeni `Code.exe` s mapom kao argumentom — bez shellica — što je funkcionalno ekvivalentno i sigurno

#### Python sigurnosni pregled ovisnosti

- Pregledani su svi Python skupovi zahtjeva s `pip-audit`. `05-AdvancedTopics` i `03-GettingStarted/samples/python` nisu prijavili niti jednu ranjivost (njihovi rasponi `mcp` / `httpx` / `pydantic` / `python-dotenv` rješavaju se trenutačnim popravljajućim izdanjima)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` je označio transivnu ovisnost **`werkzeug` 3.1.1** s tri prijave DoS zlonamjernih naziva uređaja na Windows-u za funkciju `safe_join` — `CVE-2025-66221`, `CVE-2026-21860` i `CVE-2026-27199` (sve ispravljeno u 3.1.6). Dodan je eksplicitni sigurnosni pin `werkzeug>=3.1.6` radi priznavanja popravljene verzije; potvrđeno je da se ograničenje uredno rješava s `chainlit` / `mcp` / `semantic-kernel` stogom

### Rebranding naziva proizvoda

Ažuriran je sav sadržaj kurikuluma da odražava rebranding proizvoda Microsofta:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Ažuriran link zajednice Discord

- **AGENTS.md**: Ažuriran referenca na Discord server
- **README.md**: Ažurirane reference ekosustava tehnologije
- **study_guide.md**: Ažurirane reference slučaja studije
- **05-AdvancedTopics/README.md**: Ažuriran naslov i opis Modula 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Ažuriran naslov odjeljka i opis
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Potpuno ažuriranje naslova modula i sadržaja
- **05-AdvancedTopics/mcp-security-entra/README.md**: Ažurirana poveznica međureferenciranja
- **07-LessonsfromEarlyAdoption/README.md**: Ažurirane reference slučaja studije
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Ažuriran naslov odjeljka 9, značke i mogućnosti
- **08-BestPractices/README.md**: Ažurirana poveznica Discord zajednice
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Ažurirana referenca Discord kanala
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Ažurirana referenca implementacije modela
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Ažurirana tablica AI usluga
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Ažurirane reference resursa

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension za VS Code
- **README.md**: Ažurirane glavne reference nastavnog programa
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Ažurirani naslov modula, pregled i svi naslovi modula
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Ažurirani naslov, ciljevi učenja, upute za postavljanje i resursi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Ažurirani naslov, ciljevi učenja, tablica MCP hostova i međureferenciranja
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Ažurirani naslov, značke, preduvjeti i resursi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Ažurirane reference Agent Buildera i poveznica za povratne informacije
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Ažurirani preduvjeti i reference proširenja

---

## 11. travnja 2026.

### Nova lekcija, ispravci dokumentacije i ažuriranja ovisnosti

#### Dodan novi sadržaj nastavnog programa

**Modul 05 - Napredne Tematike**
- **Lekcija 5.17: Protivničko višeglavno rezoniranje s MCP-om** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Novi sveobuhvatni vodič koji pokriva uzorak protivničke debate za višeglave sustave
  - Mermaid dijagram arhitekture: dva agenta → zajednički MCP poslužitelj → transkript debate → sudac → presuda
  - Zajednički MCP alatni poslužitelj (`web_search` + `run_python`) implementiran u Pythonu i TypeScriptu
  - Protivnički sistemski upiti (ZA / PROTIV / Sudac) s eksplicitnim zahtjevima za korištenje alata
  - Orkestrator debate u Pythonu, TypeScriptu i C# koji upravlja rundama i usmjeravanjem argumenata
  - MCP `ClientSession` povezivanje za orkestrator za stvarne pozive alata
  - Tablica slučajeva korištenja (detekcija halucinacija, modeliranje prijetnji, revizija dizajna API-ja, provjera činjenica, odabir tehnologije)
  - Sigurnosne mjere: izvršavanje u sandboxu, provjera poziva alata, ograničenje brzine, audit logiranje
  - Strukturirana vježba s tri praktična scenarija (revizija koda, odluka o arhitekturi, moderacija sadržaja)

#### Ispravci dokumentacije

**Modul 03 - Početak rada**
- **05-stdio-server/README.md**: Popravljen nepotpuni primjer TypeScript stdio poslužitelja — dodana nedostajuća instancija transporta (`new StdioServerTransport()`) i poziv `server.connect(transport)` u skladu s Python i .NET primjerima u istom odjeljku
- **14-sampling/README.md**: Ispravljen tipografska pogreška — ispravljeno `"Sampling is an davanced features"` u `"Sampling is an advanced feature"`

#### Ažuriranja nastavnog programa

**Glavni README.md**
- Dodan unos 5.17 (Protivničko višeglavo rezoniranje s MCP-om) u tablicu nastavnog programa s izravnom poveznicom na novu lekciju

**05-AdvancedTopics/README.md**
- Dodan redak Lekcije 5.17 u tablicu lekcija

**study_guide.md**
- Dodana tema protivničkog višeglava rezoniranja u mentalnu mapu i opis Naprednih Tematika

#### Ispravci koda i sigurnosti

**Modul 05 - Protivnički agenti (`mcp-adversarial-agents`)**
- **Sigurnosni popravak — injekcija naredbi**: Zamijenjeno `execSync` skaliranje ljuske s `execFile` + `promisify` u TypeScript alatu `run_python`, čime je eliminirana površina za injekciju naredbi (kôd kojim upravlja LLM sada se prosljeđuje kao literalni argv element bez sudjelovanja ljuske)
- **Povezivanje petlje MCP alata**: Ažuriran Python orkestrator debate da koristi `AsyncAnthropic` klijent (zamjena blokirajućeg sinkronog `Anthropic`), prosljeđuje živu `ClientSession` izravno svakom agentu u rundi, dohvaća definicije alata putem `session.list_tools()` svake runde i šalje blokove `tool_use` putem `session.call_tool()` u petlji dok model ne izda završni tekstualni odgovor

#### Ažuriranja ovisnosti

- Nadograđen `hono` na 4.12.12 u više paketa (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Nadograđen `@hono/node-server` sa 1.19.11 na 1.19.13 u TypeScript paketima
- Nadograđen `cryptography` sa 46.0.5 na 46.0.7 u Python paketima (laboratoriji 3 i 4 u 10-StreamliningAIWorkflows)
- Nadograđen `lodash` sa 4.17.23 na 4.18.1 u inspektoru 10-StreamliningAIWorkflows

#### Prijevodi

- Sinkronizirani prijevodi za 48+ jezika s najnovijim promjenama izvora (ažuriranje i18n)

---

## 5. veljače 2026.

### Poboljšanja potvrde i navigacije u cijelom spremištu

#### Dodan novi sadržaj nastavnog programa

**Modul 03 - Početak rada**
- **12-mcp-hosts/README.md**: Novi sveobuhvatni vodič za postavljanje MCP hostova
  - Primjeri konfiguracije Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON predlošci konfiguracije za sve glavne hostove
  - Usporedna tablica tipova transporta (stdio, SSE/HTTP, WebSocket)
  - Rješavanje uobičajenih problema s vezom
  - Najbolje sigurnosne prakse za konfiguraciju hosta

- **13-mcp-inspector/README.md**: Novi vodič za otklanjanje grešaka MCP Inspectora
  - Metode instalacije (npx, globalni npm, iz izvora)
  - Povezivanje s poslužiteljima putem stdio i HTTP/SSE
  - Alati za testiranje, resursi i tijekovi rada prompta
  - Integracija VS Code-a s MCP Inspectorom
  - Uobičajeni scenariji otklanjanja grešaka s rješenjima

**Modul 04 - Praktična implementacija**
- **pagination/README.md**: Novi vodič za implementaciju paginacije
  - Obrasci paginacije temeljeni na pokazivaču u Pythonu, TypeScriptu, Javi
  - Rukovanje paginacijom na strani klijenta
  - Strategije dizajna pokazivača (neprozirni vs. strukturirani)
  - Preporuke za optimizaciju performansi

**Modul 05 - Napredne tematike**
- **mcp-protocol-features/README.md**: Dubinska analiza novih značajki protokola
  - Implementacija notifikacija o napretku
  - Obrasci za otkazivanje zahtjeva
  - Predlošci resursa sa uzorcima URI-ja
  - Upravljanje životnim ciklusom poslužitelja
  - Kontrola razine zapisivanja
  - Obrasci za rukovanje greškama s JSON-RPC kodovima

#### Ispravci navigacije (ažurirano 24+ datoteke)

**Glavni modul README-ovi**
 Sada s poveznicama na prvu lekciju I sljedeći modul

**Poddatoteke 02-Security**
- Sve 5 prateće sigurnosne datoteke sada imaju navigaciju "Što slijedi":

**Datoteke 09-CaseStudy**
- Sve datoteke studije slučaja sada imaju sekvencijalnu navigaciju:

**Laboratoriji 10-StreamliningAI**
Dodana sekcija Što slijedi za pregled Modula 10 i Modul 11

#### Ispravci koda i sadržaja

**Ažuriranja SDK-a i ovisnosti**
Ispravljena prazna verzija openai na `^4.95.0`
SDK nadograđen s `^1.8.0` na `>=1.26.0`
Nadograđene verzije mcp na `>=1.26.0`

**Ispravci koda**
Ispravljen nevažeći model `gpt-4o-mini` u `gpt-4.1-mini`

**Ispravci sadržaja**
Ispravljena pokvarena poveznica `READMEmd` → `README.md`, ispravljen naslov nastavnog programa `Module 1-3` → `Module 0-3`, ispravljena velika/mala slova u putu
Uklonjen oštećeni duplicirani sadržaj Studije slučaja 5

**Poboljšanja vodstva za početnike**
Dodan odgovarajući uvod, ciljevi učenja i preduvjeti za početnike

#### Ažuriranja nastavnog programa

**Glavni README.md**
- Dodani su unosi 3.12 (MCP hostovi), 3.13 (MCP inspector), 4.1 (Paginacija), 5.16 (Značajke protokola) u tablicu nastavnog programa

**Modul README-ovi**
Dodane lekcije 12 i 13 u popis lekcija
Dodan odjeljak Praktični vodiči s poveznicom na paginaciju
Dodane lekcije 5.15 (Prilagođeni transport) i 5.16 (Značajke protokola)

**study_guide.md**
- Ažurirana mentalna mapa sa svim novim temama: postavljanje MCP hostova, MCP inspektor, strategije paginacije, dubinska analiza značajki protokola

## 28. siječnja 2026.

### Pregled usklađenosti sa specifikacijom MCP 2025-11-25

#### Poboljšanje osnovnih koncepata (01-CoreConcepts/)
- **Novi klijentski primitiv - Roots**: Dodana opširna dokumentacija o Roots klijentskom primitivu, omogućavajući poslužiteljima razumijevanje granica datotečnog sustava i prava pristupa
- **Bilješke o alatima**: Dodana dokumentacija o bilješkama ponašanja alata (`readOnlyHint`, `destructiveHint`) za bolje odluke o izvršavanju alata
- **Pozivanje alata u Sampling-u**: Ažurirana dokumentacija Sampling-a za uključivanje parametara `tools` i `toolChoice` za pozivanje alata vođeno modelom tijekom zahtjeva za uzorkovanjem
- **Elicitacija putem URL moda**: Dodana dokumentacija o elicitanju baziranom na URL-u za vanjske web interakcije inicirane s poslužitelja
- **Zadaci (eksperimentalno)**: Dodan novi odjeljak koji dokumentira eksperimentalnu značajku Zadaci za izdržljive omotače izvršavanja i odgođeno dohvaćanje rezultata
- **Podrška za ikone**: Napomenuto da alati, resursi, predlošci resursa i promptovi sada mogu uključivati ikone kao dodatne metapodatke

#### Ažuriranja dokumentacije
- **README.md**: Dodan referentni broj specifikacije MCP 2025-11-25 i objašnjenje verzioniranja po datumu
- **study_guide.md**: Ažurirana karta nastavnog programa da uključi Zadatke i bilješke o alatima u odjeljku Osnovni koncepti; ažuriran vremenski pečat dokumenta

#### Provjera usklađenosti sa specifikacijom
- **Verzija protokola**: Potvrđene sve dokumentacijske reference na tekuću MCP specifikaciju 2025-11-25
- **Usklađenost arhitekture**: Potvrđena točnost dokumentacije dvoslojne arhitekture (Sloj podataka + sloj transporta)
- **Dokumentacija primitiva**: Validirani primitivni objekti poslužitelja (Resursi, Prompti, Alati) i klijenta (Sampling, Elicitation, Logging, Roots)
- **Mehanizmi transporta**: Potvrđena točnost dokumentacije STDIO i Streamable HTTP transporta
- **Sigurnosne upute**: Potvrđena usklađenost s trenutnom dokumentacijom MCP Sigurnosnih najboljih praksi

#### Glavne značajke MCP 2025-11-25 dokumentirane
- **OpenID Connect Discovery**: Otkrivanje autentifikacijskog poslužitelja putem OIDC-a
- **OAuth Client ID metapodaci**: Preporučeni mehanizam registracije klijenta
- **JSON Schema 2020-12**: Zadani dijalekt za definicije MCP sheme
- **Sustav nivoa SDK-a**: Formalizirani zahtjevi za podršku i održavanje značajki SDK-a
- **Upravljačka struktura**: Formalizirane radne i interesne grupe u MCP upravljanju

### Veliko ažuriranje dokumentacije o sigurnosti (02-Security/)

#### Integracija MCP Security Summit Workshop (Sherpa)
- **Novi resurs za praktičnu obuku**: Dodana sveobuhvatna integracija s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) kroz cijelu sigurnosnu dokumentaciju
- **Pokriće rute ekspedicije**: Dokumentiran kompletan tijek od kamp do kampa, od osnovnog do vrha
- **Usklađenost s OWASP-om**: Svi sigurnosni vodiči sada su povezani s rizicima prema OWASP MCP Azure Security Guide

#### Integracija OWASP MCP Top 10
- **Novi odjeljak**: Dodana tablica OWASP MCP Top 10 sigurnosnih rizika s Azure ublaženjima u glavni sigurnosni README
- **Dokumentacija zasnovana na rizicima**: Ažuriran mcp-security-controls-2025.md s OWASP MCP referencama rizika za svako sigurnosno područje
- **Referentna arhitektura**: Povezan s referentnom arhitekturom i obrascima implementacije OWASP MCP Azure Security Guide

#### Ažurirane sigurnosne datoteke
- **README.md**: Dodan pregled Sherpa radionice, tablica ruta ekspedicije, sažetak OWASP MCP Top 10 rizika i odjeljak za praktičnu obuku
- **mcp-security-controls-2025.md**: Ažuriran zaglavlje na veljaču 2026., dodane OWASP referenca rizika (MCP01-MCP08), ispravljena nekonzistentnost verzije specifikacije
- **mcp-security-best-practices-2025.md**: Dodan odjeljak resursa za Sherpa i OWASP, ažuriran vremenski pečat
- **mcp-best-practices.md**: Dodan odjeljak za praktičnu obuku s poveznicama na Sherpa i OWASP
- **azure-content-safety-implementation.md**: Dodana OWASP MCP06 referenca, usklađenost Sherpa kampa 3 i dodatni odjeljak resursa

#### Dodane nove poveznice resursa
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Sigurnosni Vodič](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pojedinačne OWASP MCP stranice rizika (MCP01-MCP10)

### Poravnanje s MCP specifikacijom opsega kurikuluma 2025-11-25

#### Modul 03 - Početak rada
- **SDK dokumentacija**: Dodan Go SDK na službeni popis SDK-ova; ažurirane sve reference SDK-a u skladu s MCP specifikacijom 2025-11-25
- **Pojašnjenje transporta**: Ažurirani opisi STDIO i HTTP Streaming transporta s eksplicitnim referencama specifikacije

#### Modul 04 - Praktična implementacija
- **Ažuriranja SDK-a**: Dodan Go SDK; ažuriran popis SDK-ova s referencom verzije specifikacije
- **Specifikacija autorizacije**: Ažurirana veza na MCP specifikaciju autorizacije na trenutnu verziju 2025-11-25

#### Modul 05 - Napredne teme
- **Nove značajke**: Dodana napomena o novim značajkama MCP specifikacije 2025-11-25 (Zadaci, Anotacije alata, URL Mode Elicitation, Korijeni)
- **Sigurnosni resursi**: Dodane veze na OWASP MCP Top 10 i Sherpa radionicu u dodatne reference

#### Modul 06 - Zajednički doprinosi
- **Popis SDK-a**: Dodani Swift i Rust SDK-ovi; ažurirana veza specifikacije na 2025-11-25
- **Referenca specifikacije**: Ažurirana veza na MCP specifikaciju na direktni URL specifikacije

#### Modul 07 - Lekcije iz ranog usvajanja
- **Ažuriranja resursa**: Dodana veza na MCP specifikaciju 2025-11-25 i OWASP MCP Top 10 u dodatne resurse

#### Modul 08 - Najbolje prakse
- **Verzija specifikacije**: Ažurirana referenca MCP specifikacije na 2025-11-25
- **Sigurnosni resursi**: Dodani OWASP MCP Top 10 i Sherpa radionica u dodatne reference

#### Modul 10 - Optimizacija AI radnih procesa
- **Ažuriranje značke**: Promijenjena oznaka verzije MCP-a sa verzije SDK-a (1.9.3) na verziju specifikacije (2025-11-25)
- **Veze resursa**: Ažurirana veza na MCP specifikaciju; dodan OWASP MCP Top 10

#### Modul 11 - MCP Server praktične radionice
- **Referenca specifikacije**: Ažurirana veza na MCP specifikaciju na verziju 2025-11-25
- **Sigurnosni resursi**: Dodan OWASP MCP Top 10 u službene resurse

## 18. prosinca 2025.

### Ažuriranje sigurnosne dokumentacije - MCP specifikacija 2025-11-25

#### MCP sigurnosne najbolje prakse (02-Security/mcp-best-practices.md) - Ažuriranje verzije specifikacije
- **Ažuriranje verzije protokola**: Ažurirano na referencu najnovije MCP specifikacije 2025-11-25 (izdana 25. studenog 2025.)
  - Ažurirane sve reference verzije specifikacije s 2025-06-18 na 2025-11-25
  - Ažurirani datumski podaci dokumenta s 18. kolovoza 2025. na 18. prosinca 2025.
  - Provjereno da sve URL adrese specifikacije vode na trenutnu dokumentaciju
- **Validacija sadržaja**: Sveobuhvatna provjera sigurnosnih najboljih praksi u skladu s najnovijim standardima
  - **Microsoft Security Solutions**: Provjerena trenutna terminologija i veze za Prompt Shields (prije "detekcija rizika jailbreaka"), Azure Content Safety, Microsoft Entra ID i Azure Key Vault
  - **OAuth 2.1 sigurnost**: Potvrđena usklađenost s najnovijim sigurnosnim najboljim praksama OAuth-a
  - **OWASP standardi**: Validirane su referenca OWASP Top 10 za LLM-ove i dalje aktualne
  - **Azure usluge**: Provjereni svi Microsoft Azure dokumentacijski linkovi i najbolje prakse
- **Usklađenost standarda**: Potvrđeni su svi referencirani sigurnosni standardi
  - NIST AI Okvir upravljanja rizikom
  - ISO 27001:2022
  - OAuth 2.1 Najbolje prakse sigurnosti
  - Azure sigurnosni i usklađenosni okviri
- **Resursi za implementaciju**: Provjereni svi linkovi vodiča za implementaciju i resursi
  - Autentikacijski obrasci upravljanja Azure API-jem
  - Vodiči za integraciju Microsoft Entra ID-a
  - Upravljanje tajnama u Azure Key Vault-u
  - DevSecOps pipeline-ovi i rješenja za nadzor

### Osiguranje kvalitete dokumentacije
- **Usuglašenost sa specifikacijama**: Osigurano usklađivanje svih obaveznih MCP sigurnosnih zahtjeva (MORA/MORA NE) s najnovijom specifikacijom
- **Aktualnost resursa**: Provjereni svi vanjski linkovi na Microsoft dokumentaciju, sigurnosne standarde i vodiče za implementaciju
- **Pokriće najboljih praksi**: Potvrđeno sveobuhvatno pokriće autentikacije, autorizacije, AI-specifičnih prijetnji, sigurnosti opskrbnog lanca i enterprise obrazaca

## 6. listopada 2025.

### Proširenje odjeljka Početak rada – Napredno korištenje servera i jednostavna autentikacija

#### Napredno korištenje servera (03-GettingStarted/10-advanced)
- **Dodano novo poglavlje**: Predstavljen sveobuhvatan vodič za napredno korištenje MCP servera, obuhvaćajući redovnu i niskorazinsku server arhitekturu.
  - **Redovni vs. Niskorazinski server**: Detaljna usporedba i primjeri koda u Pythonu i TypeScriptu za oba pristupa.
  - **Dizajn temeljen na handlerima**: Objašnjenje upravljanja alatima/resursima/promptima bazirano na handlerima za skalabilne i fleksibilne server implementacije.
  - **Praktični obrasci**: Stvarni scenariji gdje su korisni obrasci niskorazinskog servera za napredne značajke i arhitekturu.

#### Jednostavna autentikacija (03-GettingStarted/11-simple-auth)
- **Dodano novo poglavlje**: Korak-po-korak vodič za implementaciju jednostavne autentikacije na MCP serverima.
  - **Pojmovi autentikacije**: Jasno objašnjenje razlike između autentikacije i autorizacije te rukovanja vjerodajnicama.
  - **Implementacija osnovne autentikacije**: Uzorci autentikacijskih middleware-a u Pythonu (Starlette) i TypeScriptu (Express), s prikazom koda.
  - **Napredak prema sigurnosti**: Smjernice za početak s jednostavnom autentikacijom i napredak do OAuth 2.1 i RBAC-a, uz reference na napredne sigurnosne module.

Ova proširenja pružaju praktične, hands-on upute za izgradnju robusnijih, sigurnijih i fleksibilnijih MCP server implementacija, povezujući temeljne koncepte s naprednim produkcijskim obrascima.

## 29. rujna 2025.

### MCP Server integracija baze podataka - Sveobuhvatan hands-on put učenja

#### 11-MCPServerHandsOnLabs - Novi potpuni kurikulum integracije baze podataka
- **Potpuni put učenja s 13 radionica**: Dodan sveobuhvatan hands-on kurikulum za izgradnju produkcijski spremnih MCP servera s PostgreSQL bazom podataka
  - **Implementacija iz stvarnog svijeta**: Zava Retail analitika demonstrira enterprise razinu obrazaca
  - **Strukturirani progres učenja**:
    - **Radionice 00-03: Temelji** - Uvod, osnovna arhitektura, sigurnost i multi-tenant, konfiguracija okoline
    - **Radionice 04-06: Izgradnja MCP servera** - Dizajn baze podataka i shema, implementacija MCP servera, razvoj alata  
    - **Radionice 07-09: Napredne značajke** - Integracija semantičkog pretraživanja, testiranje i otklanjanje pogrešaka, VS Code integracija
    - **Radionice 10-12: Produkcija i najbolje prakse** - Strategije implementacije, nadzor i opažanje, najbolje prakse i optimizacija
  - **Enterprise tehnologije**: FastMCP framework, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Napredne značajke**: RLS (Row Level Security), semantičko pretraživanje, višekorisnički pristup podacima, vektorski embeddingi, nadzor u stvarnom vremenu

#### Standardizacija terminologije - pretvorba modula u radionicu
- **Sveobuhvatno ažuriranje dokumentacije**: Sistematski ažurirani svi README fajlovi u 11-MCPServerHandsOnLabs da koriste terminologiju "Radionica" umjesto "Modul"
  - **Naslovi odjeljaka**: Ažurirano "Što ovaj modul pokriva" u "Što ova radionica pokriva" u svih 13 radionica
  - **Opis sadržaja**: Promijenjeno "Ovaj modul pruža..." u "Ova radionica pruža..." kroz cijelu dokumentaciju
  - **Ciljevi učenja**: Ažurirano "Do kraja ovog modula..." u "Do kraja ove radionice..."
  - **Navigacijske veze**: Pretvorene sve reference "Modul XX:" u "Radionica XX:" u međuvezama i navigaciji
  - **Praćenje završetka**: Ažurirano "Nakon završetka ovog modula..." u "Nakon završetka ove radionice..."
  - **Sačuvane tehničke reference**: Očuvane Python module reference u konfiguracijskim fajlovima (npr. `"module": "mcp_server.main"`)

#### Poboljšanje vodiča za učenje (study_guide.md)
- **Vizualna karta kurikuluma**: Dodan novi odjeljak "11. Radionice integracije baza podataka" s vizualizacijom strukture radionica
- **Struktura repozitorija**: Ažurirano s deset na jedanaest glavnih odjeljaka s detaljnim opisom 11-MCPServerHandsOnLabs
- **Smjernice za put učenja**: Poboljšane navigacijske upute za odlazak kroz odjeljke 00-11
- **Pokriće tehnologije**: Dodani detalji o FastMCP, PostgreSQL i integraciji Azure usluga
- **Ishodi učenja**: Naglasak na razvoj produkcijski spremnih servera, obrasci integracije baza podataka i enterprise sigurnost

#### Poboljšanje strukture glavnog README-a
- **Terminologija zasnovana na radionicama**: Ažuriran glavni README.md u 11-MCPServerHandsOnLabs da dosljedno koristi strukturu "Radionice"
- **Organizacija puta učenja**: Jasna progresija od temeljnih koncepta preko napredne implementacije do produkcijske implementacije
- **Fokus na stvarni svijet**: Naglasak na praktično hands-on učenje s enterprise obrascima i tehnologijama

### Poboljšanja kvalitete i dosljednosti dokumentacije
- **Naglasak na hands-on učenje**: Pojačan praktični pristup zasnovan na radionicama kroz svu dokumentaciju
- **Fokus na enterprise obrasce**: Istaknute produkcijski spremne implementacije i sigurnosni aspekti enterprise razine
- **Integracija tehnologije**: Sveobuhvatno pokriće modernih Azure usluga i AI integracijskih obrazaca
- **Progresija učenja**: Jasan, strukturirani put od osnovnih koncepata do produkcijske upotrebe

## 26. rujna 2025.

### Proširenje studija slučaja - Integracija GitHub MCP registra

#### Studije slučaja (09-CaseStudy/) - Fokus na razvoj ekosustava
- **README.md**: Veliko proširenje s detaljnom studijom slučaja GitHub MCP registra
  - **Studija slučaja GitHub MCP registra**: Nova sveobuhvatna studija slučaja koja ispituje lansiranje GitHub MCP registra u rujnu 2025.
    - **Analiza problema**: Detaljno ispitivanje fragmentiranog otkrivanja i implementacije MCP servera
    - **Arhitektura rješenja**: GitHub-ov centralizirani pristup registru s instalacijom jednim klikom u VS Code
    - **Poslovni utjecaj**: Mjerljive poboljšanja u onboarding-u developera i produktivnosti
    - **Strateška vrijednost**: Fokus na modularnu implementaciju agenata i interoperabilnost između alata
    - **Razvoj ekosustava**: Pozicioniranje kao temeljna platforma za agentsku integraciju
  - **Poboljšana struktura studija slučaja**: Ažurirane sve sedam studija slučaja s dosljednim formatiranjem i iscrpnim opisima
    - Azure AI Travel Agents: Naglasak na orkestraciju više agenata
    - Integracija Azure DevOps: Fokus na automatizaciju radnih procesa
    - Dohvaćanje dokumentacije u stvarnom vremenu: Implementacija Python konzolnog klijenta
    - Interaktivni generator planova učenja: Chainlit konverzacijska web aplikacija
    - Dokumentacija unutar editora: Integracija VS Code-a i GitHub Copilota
    - Azure API Management: Enterprise obrasci integracije API-ja
    - GitHub MCP Registar: Razvoj ekosustava i zajednice
  - **Sveobuhvatni zaključak**: Prepravljena zaključna sekcija s naglaskom na sedam studija slučaja koje pokrivaju različite dimenzije MCP implementacije
    - Enterprise integracija, orkestracija više agenata, produktivnost developera
    - Razvoj ekosustava, kategorizacija edukacijskih primjena
    - Poboljšani uvidi u arhitektonske obrasce, strategije implementacije i najbolje prakse
    - Naglasak na MCP kao zrelu, produkcijski spremnu specifikaciju

#### Ažuriranja vodiča za učenje (study_guide.md)
- **Vizualna karta kurikuluma**: Ažurirana mentalna mapa za uključivanje GitHub MCP registra u odjeljak studija slučaja
- **Opis studija slučaja**: Prošireno s generičkih opisa na detaljnu razradu sedam sveobuhvatnih studija slučaja
- **Struktura repozitorija**: Ažuriran odjeljak 10 radi pokrića sveobuhvatnih studija slučaja sa specifičnim implementacijskim detaljima
- **Integracija promjena**: Dodan unos od 26. rujna 2025. dokumentirajući dodatak GitHub MCP registra i proširenja studija slučaja
- **Ažuriranja datuma**: Ažuriran vremenski zapis u podnožju na najnoviju reviziju (26. rujna 2025.)

### Poboljšanja kvalitete dokumentacije
- **Poboljšanje dosljednosti**: Standardizirano formatiranje i struktura studija slučaja kroz svih sedam primjera
- **Sveobuhvatno pokriće**: Studije slučaja sada pokrivaju scenarije enterprise integracije, produktivnosti developera i razvoja ekosustava
- **Strateško pozicioniranje**: Pojačan fokus na MCP kao temeljnu platformu za implementaciju agentskih sustava
- **Integracija resursa**: Ažurirani dodatni resursi s uključenom vezom na GitHub MCP registar

## 15. rujna 2025.

### Proširenje naprednih tema - Prilagođeni transporti i kontekstualno inženjerstvo

#### MCP prilagođeni transporti (05-AdvancedTopics/mcp-transport/) - Novi vodič za naprednu implementaciju
- **README.md**: Potpuni vodič za implementaciju prilagođenih MCP transportnih mehanizama
  - **Transport Azure Event Grid**: Sveobuhvatna implementacija serverless event-driven transporta
    - Primjeri u C#, TypeScriptu i Pythonu s integracijom Azure Functions
    - Obrasci arhitekture vođene događajima za skalabilna MCP rješenja
    - Primatelji webhookova i push-based upravljanje porukama
  - **Transport Azure Event Hubs**: Implementacija high-throughput streaming transporta
    - Streaming u stvarnom vremenu za scenarije niske latencije
    - Strategije particioniranja i upravljanje checkpointovima
    - Grupiranje poruka i optimizacija performansi
  - **Enterprise obrasci integracije**: Produkcijski spremni arhitektonski primjeri
    - Distribuirana MCP obrada preko više Azure Functions
    - Hibridne transportne arhitekture koje kombiniraju više tipova transporta
    - Strategije trajnosti, pouzdanosti i upravljanja pogreškama poruka
  - **Sigurnost i nadzor**: Integracija Azure Key Vault-a i obrasci opažanja
    - Autentikacija upravljanom identitetu i princip najmanjih privilegija
    - Telemetrija i nadzor performansi putem Application Insights
    - Obratnici i obrasci otpornosti na greške
  - **Okviri za testiranje**: Sveobuhvatne strategije testiranja prilagođenih transporta
    - Jedinično testiranje s test dvojancima i mocking framework-ima
    - Integracijsko testiranje s Azure Test Containers
    - Razmatranja za testiranje performansi i opterećenja

#### Kontekstualno inženjerstvo (05-AdvancedTopics/mcp-contextengineering/) - Nova disciplina u AI
- **README.md**: Sveobuhvatan pregled kontekstualnog inženjerstva kao rastućeg područja
  - **Temeljna načela**: Potpuno dijeljenje konteksta, osviještenost o donošenju odluka i upravljanje kontekstualnim prozorom

  - **Usklađivanje MCP protokola**: Kako dizajn MCP-a rješava izazove inženjerstva konteksta
    - Ograničenja prozora konteksta i strategije progresivnog učitavanja
    - Određivanje relevantnosti i dinamičko dohvaćanje konteksta
    - Višemodalno rukovanje kontekstom i sigurnosna razmatranja
  - **Pristupi implementaciji**: Jednoprocesne vs. višestruke arhitekture agenata
    - Tehnike segmentacije i prioritizacije konteksta
    - Strategije progresivnog učitavanja i kompresije konteksta
    - Slojeviti pristupi kontekstu i optimizacija dohvaćanja
  - **Okvir za mjerenje**: Novi metrički pokazatelji za evaluaciju učinkovitosti konteksta
    - Učinkovitost unosa, izvedba, kvaliteta i razmatranja korisničkog iskustva
    - Eksperimentalni pristupi optimizaciji konteksta
    - Analiza neuspjeha i metodologije poboljšanja

#### Ažuriranja navigacije nastavnog plana (README.md)
- **Poboljšana struktura modula**: Ažurirana tablica nastavnog plana s novim naprednim temama
  - Dodani unosi Context Engineering (5.14) i Custom Transport (5.15)
  - Dosljedno formatiranje i navigacijski linkovi kroz sve module
  - Ažurirani opisi za odražavanje trenutačnog opsega sadržaja

### Poboljšanja strukture direktorija
- **Standardizacija imenovanja**: Preimenovan "mcp transport" u "mcp-transport" radi dosljednosti s ostalim mapama naprednih tema
- **Organizacija sadržaja**: Sve mape 05-AdvancedTopics sada slijede dosljedni obrazac imenovanja (mcp-[tema])

### Poboljšanja kvalitete dokumentacije
- **Usklađivanje specifikacije MCP-a**: Sav novi sadržaj referira se na trenutačnu MCP specifikaciju 2025-06-18
- **Primjeri na više jezika**: Sveobuhvatni primjeri koda u C#, TypeScriptu i Pythonu
- **Enterprise fokus**: Obrasci spremni za produkciju i integracija sa Azure cloudom kroz cijeli sadržaj
- **Vizualna dokumentacija**: Mermaid dijagrami za vizualizaciju arhitekture i tokova

## 18. kolovoza 2025.

### Sveobuhvatno ažuriranje dokumentacije - MCP standardi 2025-06-18

#### Najbolje sigurnosne prakse MCP-a (02-Security/) - Potpuna modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Potpuni preradak usklađen s MCP specifikacijom 2025-06-18
  - **Obavezni zahtjevi**: Dodani eksplicitni MUST/MUST NOT zahtjevi iz službene specifikacije s jasnim vizualnim oznakama
  - **12 osnovnih sigurnosnih praksi**: Prestrukturirano s popisa od 15 stavki u sveobuhvatna sigurnosna područja
    - Sigurnost tokena i autentifikacija s integracijom eksternog pružatelja identiteta
    - Upravljanje sesijama i sigurnost prijenosa s kriptografskim zahtjevima
    - Zaštita specifična za AI uz integraciju Microsoft Prompt Shields
    - Kontrola pristupa i dozvole s principom najmanjih privilegija
    - Sigurnost sadržaja i nadzor s integracijom Azure Content Safety
    - Sigurnost lanceva opskrbe s opsežnom provjerom komponenti
    - Sigurnost OAuth-a i sprječavanje "confused deputy" problema uz implementaciju PKCE
    - Odgovor na incidente i oporavak s automatiziranim mogućnostima
    - Usklađenost i upravljanje s regulatornim zahtjevima
    - Napredne sigurnosne kontrole s arhitekturom zero trust
    - Integracija Microsoft sigurnosnog ekosustava s opsežnim rješenjima
    - Kontinuirani razvoj sigurnosti s adaptivnim praksama
  - **Microsoft sigurnosna rješenja**: Proširene smjernice za integraciju Prompt Shields, Azure Content Safety, Entra ID i GitHub Advanced Security
  - **Resursi za implementaciju**: Kategorizirani sveobuhvatni izvori po službenoj MCP dokumentaciji, Microsoft sigurnosnim rješenjima, sigurnosnim standardima i vodičima za implementaciju

#### Napredne sigurnosne kontrole (02-Security/) - Enterprise implementacija
- **MCP-SECURITY-CONTROLS-2025.md**: Potpuni preobražaj s enterprise razinom sigurnosnog okvira
  - **9 obuhvatnih sigurnosnih područja**: Proširenih od osnovnih kontrola do detaljnog enterprise okvira
    - Napredna autentifikacija i autorizacija s integracijom Microsoft Entra ID
    - Sigurnost tokena i anti-passthrough kontrole s opsežnom validacijom
    - Sigurnosne kontrole sesija sa sprječavanjem otmice
    - AI-specifične sigurnosne kontrole sa sprječavanjem umetanja promptova i trovanja alata
    - Sprječavanje napade "confused deputy" s OAuth proxy sigurnošću
    - Sigurnost izvršenja alata s sandboxingom i izolacijom
    - Sigurnosne kontrole lanceva opskrbe s provjerom ovisnosti
    - Kontrole nadzora i detekcije s integracijom SIEM-a
    - Odgovor na incidente i oporavak s automatiziranim mogućnostima
  - **Primjeri implementacije**: Dodani detaljni YAML konfiguracijski blokovi i primjeri koda
  - **Integracija Microsoft rješenja**: Sveobuhvatno pokrivanje Azure sigurnosnih usluga, GitHub Advanced Security i upravljanja enterprise identitetom

#### Sigurnost naprednih tema (05-AdvancedTopics/mcp-security/) - Produkcijska implementacija
- **README.md**: Potpuni preradak za enterprise sigurnosnu implementaciju
  - **Usklađenost s trenutačnom specifikacijom**: Ažurirano prema MCP specifikaciji 2025-06-18 s obaveznim sigurnosnim zahtjevima
  - **Poboljšana autentifikacija**: Integracija Microsoft Entra ID s opsežnim primjerima u .NET i Java Spring Security
  - **Integracija AI sigurnosti**: Implementacija Microsoft Prompt Shields i Azure Content Safety s detaljnim primjerima u Pythonu
  - **Napredna mitigacija prijetnji**: Sveobuhvatni primjeri implementacije za
    - Sprječavanje napada "confused deputy" s PKCE i validacijom korisničkog pristanka
    - Sprječavanje passthrough tokena s validacijom publike i sigurnim upravljanjem tokenima
    - Sprječavanje otmice sesije s kriptografskim vezanjem i analizom ponašanja
  - **Enterprise integracija sigurnosti**: Azure Application Insights nadzor, pipelineovi za detekciju prijetnji i sigurnost lanceva opskrbe
  - **Popis za implementaciju**: Jasne obavezne naspram preporučenih sigurnosnih kontrola s prednostima Microsoft sigurnosnog ekosustava

### Kvaliteta dokumentacije i usklađenost sa standardima
- **Reference specifikacije**: Ažurirani svi linkovi na trenutačnu MCP specifikaciju 2025-06-18
- **Microsoft sigurnosni ekosustav**: Proširene smjernice za integraciju kroz cijelu sigurnosnu dokumentaciju
- **Praktična implementacija**: Dodani detaljni primjeri koda u .NET, Javi i Pythonu s enterprise obrascima
- **Organizacija resursa**: Sveobuhvatna kategorizacija službene dokumentacije, sigurnosnih standarda i vodiča za implementaciju
- **Vizualne oznake**: Jasno označavanje obaveznih zahtjeva naspram preporučenih praksi


#### Osnovni pojmovi (01-CoreConcepts/) - Potpuna modernizacija
- **Ažuriranje verzije protokola**: Ažurirano za referencu trenutačne MCP specifikacije 2025-06-18 s verzioniranjem po datumu (format GGGG-MM-DD)
- **Fina dorada arhitekture**: Poboljšani opisi domaćina, klijenata i servera za odražavanje aktualnih MCP obrazaca arhitekture
  - Domaćini sada jasno definirani kao AI aplikacije koje koordiniraju višestruke MCP klijentske veze
  - Klijenti opisani kao protokoli povezivači s održavanjem odnosa jedan-na-jedan sa serverima
  - Serveri prošireni s lokalnim i udaljenim scenarijima implementacije
- **Preustroj primitiva**: Potpuni preobražaj server i klijentskih primitiva
  - Server primitiv: Resursi (izvori podataka), Prompts (predlošci), Alati (izvršne funkcije) s detaljnim objašnjenjima i primjerima
  - Klijentski primitiv: Uzorkovanje (LLM završetci), Poticanje (korisnički unos), Logiranje (debugging/nadzor)
  - Ažurirano s aktualnim obrascima metoda za otkrivanje (`*/list`), dohvaćanje (`*/get`) i izvršavanje (`*/call`)
- **Arhitektura protokola**: Uvođenje dvostrukog sloja arhitekture
  - Sloj podataka: JSON-RPC 2.0 temelj s upravljanjem životnim ciklusom i primitivima
  - Transportni sloj: STDIO (lokalni) i Streamable HTTP sa SSE (udaljeni) transportni mehanizmi
- **Sigurnosni okvir**: Sveobuhvatna sigurnosna načela uključujući eksplicitni korisnički pristanak, zaštitu privatnosti podataka, sigurnost izvršenja alata i sigurnost transportnog sloja
- **Obrasci komunikacije**: Ažurirane protokolarne poruke za prikaz inicijalizacije, otkrivanja, izvršavanja i tijek obavijesti
- **Primjeri koda**: Osvježeni primjeri na više jezika (.NET, Java, Python, JavaScript) za odražavanje aktualnih MCP SDK obrazaca

#### Sigurnost (02-Security/) - Sveobuhvatni sigurnosni preuredaj  
- **Usklađivanje sa standardima**: Puna usklađenost s MCP zahtjevima sigurnosti 2025-06-18
- **Evolucija autentifikacije**: Dokumentirana evolucija od prilagođenih OAuth servera do delegacije eksternim pružateljima identiteta (Microsoft Entra ID)
- **AI-specifična analiza prijetnji**: Prošireni pregled modernih AI vektora napada
  - Detaljni scenariji napada ubrizgavanjem prompta s realnim primjerima
  - Mehanizmi trovanja alata i obrasci "rug pull" napada
  - Trovanje prozora konteksta i napadi zbunjivanja modela
- **Microsoft AI sigurnosna rješenja**: Sveobuhvatno pokrivanje Microsoft sigurnosnog ekosustava
  - AI Prompt Shields s naprednom detekcijom, isticanjem i tehnikama za razgraničenje
  - Azure Content Safety obrasci integracije
  - GitHub Advanced Security za zaštitu lanceva opskrbe
- **Napredna mitigacija prijetnji**: Detaljne sigurnosne kontrole za
  - Otimanje sesije s MCP-specifičnim scenarijima napada i zahtjevima kriptografskog ID-a sesije
  - Problemi "confused deputy" u MCP proxy scenarijima s eksplicitnim zahtjevima pristanka
  - Ranljivosti propuštanja tokena s obaveznim kontrolama validacije
- **Sigurnost lanceva opskrbe**: Prošireno pokrivanje AI lanceva opskrbe uključujući temeljne modele, usluge ugradnji, davatelje konteksta i vanjske API-je
- **Sigurnost temelja**: Poboljšana integracija s enterprise sigurnosnim obrascima uključujući zero trust arhitekturu i Microsoft sigurnosni ekosustav
- **Organizacija resursa**: Kategorizirani sveobuhvatni izvori po tipu (Službena dok., standardi, istraživanja, Microsoft rješenja, vodiči za implementaciju)

### Poboljšanja kvalitete dokumentacije
- **Strukturirani ciljevi učenja**: Poboljšani ciljevi učenja sa specifičnim, provedivim rezultatima
- **Unakrsne reference**: Dodani linkovi između povezanih tema o sigurnosti i osnovnim konceptima
- **Trenutačne informacije**: Ažurirani svi datumski linkovi i reference na specifikacije prema aktualnim standardima
- **Smjernice za implementaciju**: Dodane specifične, provedive implementacijske upute kroz oba dijela

## 16. srpnja 2025.

### Poboljšanja README-a i navigacije
- Potpuno redizajnirana navigacija nastavnog plana u README.md
- Zamijenjeni `<details>` tagovi pristupačnijim tabličnim formatom
- Kreirane alternativne opcije izgleda u novoj mapi "alternative_layouts"
- Dodani primjeri navigacije u obliku kartica, kartica sa tabovima i akordeona
- Ažuriran odjeljak strukture repozitorija da uključi sve najnovije datoteke
- Poboljšan odjeljak "Kako koristiti ovaj nastavni plan" s jasnim preporukama
- Ažurirani linkovi na MCP specifikacije prema točnim URL-ovima
- Dodan odjeljak Context Engineering (5.14) u strukturu nastavnog plana

### Ažuriranja vodiča za učenje
- Potpuno revidiran vodič za učenje kako bi se uskladio s aktualnom strukturom repozitorija
- Dodani novi odjeljci za MCP klijente i alate, te popularne MCP servere
- Ažurirana Vizualna karta nastavnog plana za točan prikaz svih tema
- Poboljšani opisi naprednih tema da pokrivaju sva specijalizirana područja
- Ažuriran odjeljak Studije slučaja da odražava stvarne primjere
- Dodan ovaj sveobuhvatni zapis promjena

### Doprinosi zajednice (06-CommunityContributions/)
- Dodane detaljne informacije o MCP serverima za generiranje slika
- Dodan opsežan odjeljak o korištenju Claude-a u VSCode
- Dodane upute za postavljanje i korištenje terminal klijenta Cline
- Ažuriran odjeljak MCP klijenta da uključi sve popularne opcije klijenata
- Poboljšani primjeri doprinosa s točnijim uzorcima koda

### Napredne teme (05-AdvancedTopics/)
- Organizirane sve specijalizirane mape tema s dosljednim imenovanjem
- Dodani materijali i primjerci za inženjering konteksta
- Dodana dokumentacija za integraciju Foundry agenta
- Poboljšana dokumentacija integracije sigurnosti Entra ID-a

## 11. lipnja 2025.

### Početno kreiranje
- Objavljena prva verzija nastavnog plana MCP za početnike
- Kreirana osnovna struktura za svih 10 glavnih sekcija
- Implementirana Vizualna karta nastavnog plana za navigaciju
- Dodani početni probni projekti na više programskih jezika

### Početak rada (03-GettingStarted/)
- Kreirani prvi primjeri implementacije servera
- Dodane smjernice za razvoj klijenta
- Uključene upute za integraciju LLM klijenta
- Dodana dokumentacija za integraciju u VS Code
- Implementirani primjeri servera sa Server-Sent Events (SSE)

### Osnovni pojmovi (01-CoreConcepts/)
- Dodano detaljno objašnjenje arhitekture klijent-server
- Kreirana dokumentacija ključnih protokolnih komponenti
- Dokumentirani obrasci poruka u MCP-u

## 23. svibnja 2025.

### Struktura repozitorija
- Inicijaliziran repozitorij s osnovnom strukturom mapa
- Kreirane README datoteke za svaku glavnu sekciju
- Postavljena infrastruktura za prijevod
- Dodani slikovni resursi i dijagrami

### Dokumentacija
- Kreiran početni README.md s pregledom nastavnog plana
- Dodani CODE_OF_CONDUCT.md i SECURITY.md
- Postavljen SUPPORT.md s uputama za traženje pomoći
- Kreirana preliminarna struktura vodiča za učenje

## 15. travnja 2025.

### Planiranje i okvir
- Početno planiranje nastavnog plana MCP za početnike
- Definirani ciljevi učenja i ciljana publika
- Nacrtana struktura od 10 sekcija nastavnog plana
- Razvijen konceptualni okvir za primjere i studije slučajeva
- Kreirani početni prototipni primjeri ključnih pojmova

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->