# Dnevnik sprememb: MCP za začetnike - učni načrt

Ta dokument služi kot zapis vseh pomembnih sprememb, narejenih v učnem načrtu Model Context Protocol (MCP) za začetnike. Spremembe so dokumentirane v obratnem kronološkem vrstnem redu (najnovejše spremembe prvi).

## 11. april 2026

### Nova lekcija, popravki dokumentacije in posodobitve odvisnosti

#### Dodana nova vsebina učnega načrta

**Modul 05 - Napredne teme**  
- **Lekcija 5.17: Adversarial Multi-Agent Reasoning z MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nov obsežen vodič o vzorcu nasprotujoče se debate za sisteme z več agenti  
  - Mermaid diagram arhitekture: dva agenta → skupni MCP strežnik → zapis debate → sodnik → razsodba  
  - Skupni MCP strežnik orodij (`web_search` + `run_python`) implementiran v Pythonu in TypeScriptu  
  - Nasprotujoči sistemski pozivi (ZA / PROTI / Sodnik) z eksplicitnimi zahtevami glede uporabe orodij  
  - Orkestrator debate v Pythonu, TypeScriptu in C#, ki upravlja runde in usmerjanje argumentov  
  - MCP `ClientSession` povezava orkestratorja z resničnimi klici orodij  
  - Tabela uporabe (odkrivanje halucinacij, modeliranje groženj, pregled oblikovanja API-jev, preverjanje dejstev, izbira tehnologije)  
  - Varnostni premisleki: izvajanje v peskovniku, preverjanje klicev orodij, omejevanje hitrosti, beleženje revizije  
  - Strukturirana vaja s tremi praktičnimi scenariji (pregled kode, odločanje o arhitekturi, moderacija vsebin)

#### Popravki dokumentacije

**Modul 03 - Začetek**  
- **05-stdio-server/README.md**: Popravljen nepopoln primer TypeScript stdio strežnika — dodana manjkajoča inicializacija transporta (`new StdioServerTransport()`) in klic `server.connect(transport)` za skladnost s primeri v Pythonu in .NET v istem razdelku  
- **14-sampling/README.md**: Popravljena tipkarska napaka — popravljeno `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Posodobitve učnega načrta

**Glavni README.md**  
- Dodan vnos 5.17 (Adversarial Multi-Agent Reasoning z MCP) v tabelo učnega načrta z neposredno povezavo do nove lekcije

**05-AdvancedTopics/README.md**  
- Dodana vrstica Lekcije 5.17 v tabelo lekcij

**study_guide.md**  
- Dodana tema Adversarial Multi-Agent Reasoning v miselni zemljevid in opis naprednih tem

#### Popravki kode in varnosti

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**  
- **Varnostni popravek — vbrizgavanje ukazov**: Nadomeščena shell interpolacija `execSync` z `execFile` + `promisify` v orodju `run_python` v TypeScriptu, kar odpravi površino za vbrizgavanje ukazov (koda, ki jo nadzira LLM, je zdaj posredovana kot dobesedni element argv brez vključenosti shell-a)  
- **Povezava zanko orodij MCP**: Posodobljen Python orkestrator debate za uporabo odjemalca `AsyncAnthropic` (zamenjava sinhrone blokirajoče različice `Anthropic`), posredovanje žive `ClientSession` neposredno vsakemu agentu, pridobivanje definicij orodij prek `session.list_tools()` v vsakem krogu ter pošiljanje blokov `tool_use` preko `session.call_tool()` v zanki, dokler model ne odda končnega besedilnega odgovora

#### Posodobitve odvisnosti

- Posodobljen `hono` na različico 4.12.12 v več paketih (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- Posodobljen `@hono/node-server` iz 1.19.11 na 1.19.13 v paketih TypeScript  
- Posodobljen `cryptography` iz 46.0.5 na 46.0.7 v Python paketih (labosi 3 in 4 pri 10-StreamliningAIWorkflows)  
- Posodobljen `lodash` iz 4.17.23 na 4.18.1 v inšpektorju 10-StreamliningAIWorkflows

#### Prevodi

- Sinhronizirani prevodi za več kot 48 jezikov z najnovejšimi spremembami vira (posodobitev i18n)

---

## 5. februar 2026

### Preverjanje celotnega repozitorija in izboljšave navigacije

#### Dodana nova vsebina učnega načrta

**Modul 03 - Začetek**  
- **12-mcp-hosts/README.md**: Nov obsežen vodič za nastavitev MCP gostiteljev  
  - Primeri konfiguracij za Claude Desktop, VS Code, Cursor, Cline, Windsurf  
  - Predloge JSON konfiguracij za vse glavne gostitelje  
  - Tabela primerjav vrst transporta (stdio, SSE/HTTP, WebSocket)  
  - Reševanje pogostih težav s povezavami  
  - Najboljše varnostne prakse za konfiguracijo gostitelja

- **13-mcp-inspector/README.md**: Nov vodič za razhroščevanje MCP Inspectorja  
  - Metode namestitve (npx, globalni npm, iz vira)  
  - Povezovanje do strežnikov preko stdio in HTTP/SSE  
  - Orodja za testiranje, viri in delovni tokovi pozivov  
  - Integracija v VS Code z MCP Inspectorjem  
  - Pogoste situacije za razhroščevanje z rešitvami

**Modul 04 - Praktična izvedba**  
- **pagination/README.md**: Nov vodič za implementacijo paginacije  
  - Vzorce paginacije na osnovi kurzorjev v Pythonu, TypeScriptu, Javi  
  - Upravljanje paginacije na odjemalski strani  
  - Strategije oblikovanja kurzorjev (neprosojni proti strukturiranim)  
  - Priporočila za optimizacijo zmogljivosti

**Modul 05 - Napredne teme**  
- **mcp-protocol-features/README.md**: Novi poglobljeni vpogled v funkcije protokola  
  - Implementacija obvestil o napredku  
  - Vzorci preklica zahtev  
  - Predloge virov z vzorci URI-jev  
  - Upravljanje življenjskega cikla strežnika  
  - Nadzor ravni beleženja  
  - Vzorci ravnanja z napakami z uporabo kod JSON-RPC

#### Popravki navigacije (posodobljenih več kot 24 datotek)

**Glavni modulni README-ji**  
- Zdaj vsebujejo povezavi tako do prve lekcije KOT naslednjega modula

**Poddatoteke 02-Security**  
- Vseh 5 dodatnih varnostnih dokumentov ima sedaj navigacijo "Kaj sledi":

**Datoteke 09-CaseStudy**  
- Vseh študijskih primerov je sedaj sekvenčna navigacija:

**Labosi 10-StreamliningAI**  
Dodana sekcija Kaj sledi v pregledu Modula 10 in Modula 11

#### Popravki kode in vsebine

**Posodobitve SDK in odvisnosti**  
Popravljen prazen odprt openai paket na `^4.95.0`  
Posodobljen SDK iz `^1.8.0` na `>=1.26.0`  
Posodobljeni MCP verzijski pini na `>=1.26.0`

**Popravki kode**  
Popravljena neveljavna različica modela `gpt-4o-mini` na `gpt-4.1-mini`

**Popravki vsebine**  
Popravljena pokvarjena povezava `READMEmd` → `README.md`, popravljena naslovna vrstica učnega načrta `Module 1-3` → `Module 0-3`, popravljena občutljivost poti na velike/male črke  
Odstranjena pokvarjena duplicirana vsebina Študije primera 5

**Izboljšave za začetnike**  
Dodano ustrezno uvodno besedilo, učni cilji in predpogojni pogoji za začetnike

#### Posodobitve učnega načrta

**Glavni README.md**  
- Dodani vnosi 3.12 (MCP gostitelji), 3.13 (MCP inšpektor), 4.1 (Paginacija), 5.16 (Funkcije protokola) v tabelo učnega načrta

**Modulni README-ji**  
Dodani lekciji 12 in 13 na seznam lekcij  
Dodana sekcija Praktični vodiči s povezavo do paginacije  
Dodani lekciji 5.15 (Custom Transport) in 5.16 (Funkcije protokola)

**study_guide.md**  
- Posodobljen miselni zemljevid z vsemi novimi temami: Nastavitev MCP gostiteljev, MCP inšpektor, Strategije paginacije, Poglobljen vpogled v funkcije protokola

## 28. januar 2026

### Pregled skladnosti s specifikacijo MCP 2025-11-25

#### Izboljšave osnovnih konceptov (01-CoreConcepts/)  
- **Nova strukturna primitiva odjemalca - Roots**: Dodana obsežna dokumentacija o roots primitivah odjemalca, ki omogoča strežnikom razumevanje meja datotečnega sistema in dovoljenj za dostop  
- **Oznake orodij**: Dodana dokumentacija o vedenjskih oznakah orodij (`readOnlyHint`, `destructiveHint`) za boljše odločitve izvajanja orodij  
- **Klic orodij pri Sampling-u**: Posodobljena dokumentacija Sampling za vključitev parametrov `tools` in `toolChoice` za modelom voden klic orodij med zahtevki vzorčenja  
- **Eliciranje načina URL**: Dodana dokumentacija o eliciranju na osnovi URL za zunanjo spletno interakcijo, ki jo sproži strežnik  
- **Naloge (eksperimentalno)**: Dodan nov razdelek, ki dokumentira eksperimentalno funkcijo Tasks za trajne ovojnike izvajanja in odloženo pridobivanje rezultatov  
- **Podpora ikonam**: Zabeleženo, da orodja, viri, predloge virov in pozivi zdaj lahko vključujejo ikone kot dodatne metapodatke

#### Posodobitve dokumentacije  
- **README.md**: Dodan referenčni zapis različice MCP Specifikacije 2025-11-25 in pojasnilo verzioniranja po datumu  
- **study_guide.md**: Posodobljen zemljevid učnega načrta z vključitvijo Tasks in Tool Annotations v razdelek osnovnih konceptov; posodobljen časovni žig dokumenta

#### Preverjanje skladnosti specifikacije  
- **Različica protokola**: Preverjeno, da vsa dokumentacija sklicuje na aktualno MCP Specifikacijo 2025-11-25  
- **Usklajenost arhitekture**: Potrjena točnost dokumentacije o dvoplastni arhitekturi (plasti podatkov + transportne plasti)  
- **Dokumentacija primitiv**: Validirani strežniške primitive (Viri, Pozivi, Orodja) in primitiv odjemalca (Sampling, Elicitation, Logging, Roots)  
- **Transportni mehanizmi**: Preverjena točnost dokumentacije o STDIO in Streamable HTTP transportu  
- **Varnostna navodila**: Potrjena usklajenost s trenutno MCP dokumentacijo najboljših varnostnih praks

#### Ključne dokumentirane funkcije MCP 2025-11-25  
- **OpenID Connect Discovery**: Odkritje strežnika za avtentikacijo preko OIDC  
- **Dokumenti o metapodatkih OAuth Client ID**: Priporočeni mehanizem registracije odjemalca  
- **JSON Schema 2020-12**: Privzeti dialekt za definicije MCP shem  
- **Sistem nivojev SDK**: Formalizirane zahteve za podporo in vzdrževanje funkcij SDK  
- **Struktura upravljanja**: Formalizirane delovne skupine in interesne skupine v upravljanju MCP

### Velika varnostna posodobitev dokumentacije (02-Security/)

#### Integracija MCP Security Summit Workshop (Sherpa)  
- **Novi praktični viri usposabljanja**: Obsežna integracija z [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) skozi celotno varnostno dokumentacijo  
- **Pokritost poti ekspedicije**: Dokumentiran celoten potek od Baznega tabora do vrha  
- **Usklajenost z OWASP**: Vsa varnostna navodila so zdaj vezana na tveganja vodnika OWASP MCP Azure Security Guide

#### Integracija OWASP MCP Top 10  
- **Nov razdelek**: Dodana tabela OWASP MCP Top 10 varnostnih tveganj z mitigacijami Azure v glavni varnostni README  
- **Dokumentacija na osnovi tveganj**: Posodobljen `mcp-security-controls-2025.md` z referencami na OWASP MCP tveganja za vsako varnostno področje  
- **Referenčna arhitektura**: Povezava do referenčne arhitekture OWASP MCP Azure Security Guide in vzorcev izvajanja

#### Posodobljene varnostne datoteke  
- **README.md**: Dodan pregled Sherpa delavnice, tabela poti ekspedicije, povzetek OWASP MCP Top 10 tveganj in sekcija za praktično usposabljanje  
- **mcp-security-controls-2025.md**: Posodobljen naslov na februar 2026, dodane OWASP reference tveganj (MCP01-MCP08), popravljena neskladnost verzije specifikacije  
- **mcp-security-best-practices-2025.md**: Dodana sekcija virov Sherpa in OWASP, posodobljen časovni žig  
- **mcp-best-practices.md**: Dodana sekcija za praktično usposabljanje s povezavami na Sherpa in OWASP  
- **azure-content-safety-implementation.md**: Dodana OWASP MCP06 referenca, usklajenost s Sherpa taborom 3 in dodatna sekcija virov

#### Dodane nove povezave do virov  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Posamezne OWASP MCP strani tveganj (MCP01-MCP10)

### Skladnost učnega načrta s MCP specifikacijo 2025-11-25

#### Modul 03 - Začetek  
- **Dokumentacija SDK**: Dodan Go SDK v uradni seznam SDK; posodobljene vse reference SDK za skladnost z MCP Specifikacijo 2025-11-25  
- **Poenostavitve transporta**: Posodobljeni opisi transporta STDIO in HTTP Streaming z eksplicitnimi sklici na specifikacijo

#### Modul 04 - Praktična izvedba  
- **Posodobitve SDK**: Dodan Go SDK; posodobljen seznam SDK z referenco na različico specifikacije  
- **Specifikacija avtorizacije**: Posodobljena povezava na MCP Authorization specifikacijo na trenutno verzijo 2025-11-25

#### Modul 05 - Napredne teme  
- **Nove funkcije**: Dodana opomba o novih funkcijah MCP Specifikacije 2025-11-25 (Tasks, Tool Annotations, URL Mode Elicitation, Roots)  
- **Varnostni viri**: Dodane povezave na OWASP MCP Top 10 in Sherpa delavnico kot dodatni viri

#### Modul 06 - Prispevki skupnosti  
- **Seznam SDK**: Dodana Swift in Rust SDK; posodobljena povezava na različico specifikacije 2025-11-25  
- **Specifikacijska referenca**: Posodobljena povezava na uradni URL specifikacije MCP

#### Modul 07 - Lekcije zgodnje uporabe  
- **Posodobitve virov**: Dodana povezava MCP Specifikacije 2025-11-25 in OWASP MCP Top 10 v dodatne vire

#### Modul 08 - Najboljše prakse  
- **Različica specifikacije**: Posodobljen referenčni zapis MCP Specifikacije na 2025-11-25  
- **Varnostni viri**: Dodani OWASP MCP Top 10 in Sherpa delavnica k dodatnim virom

#### Modul 10 - Poenostavitev AI delovnih tokov  
- **Posodobitev značke**: Zamenjana MCP verzijska značka iz verzije SDK (1.9.3) na različico specifikacije (2025-11-25)  
- **Povezave do virov**: Posodobljena MCP Specifikacija; dodan OWASP MCP Top 10

#### Modul 11 - MCP strežnik – praktični labosi  
- **Specifikacijska referenca**: Posodobljen povezava MCP Specifikacije na različico 2025-11-25  
- **Varnostni viri**: Dodan OWASP MCP Top 10 med uradne vire

## 18. december 2025
### Posodobitev varnostne dokumentacije - MCP specifikacija 2025-11-25

#### Najboljše varnostne prakse MCP (02-Security/mcp-best-practices.md) - Posodobitev različice specifikacije
- **Posodobitev različice protokola**: Posodobljeno na najnovejšo MCP specifikacijo 2025-11-25 (izdano 25. novembra 2025)
  - Posodobljene vse reference različic specifikacije s 2025-06-18 na 2025-11-25
  - Posodobljene datumske reference dokumentov z 18. avgusta 2025 na 18. decembra 2025
  - Preverjene vse URL-je specifikacij, da kažejo na trenutno dokumentacijo
- **Preverjanje vsebine**: Celovita validacija najboljših varnostnih praks glede na najnovejše standarde
  - **Microsoftove varnostne rešitve**: Preverjena trenutna terminologija in povezave za Prompt Shields (prej "odkrivanje tveganja jailbreakanja"), Azure Content Safety, Microsoft Entra ID in Azure Key Vault
  - **Varnost OAuth 2.1**: Potrjeno usklajevanje z najnovejšimi najboljšimi praksami varnosti OAuth
  - **OWASP standardi**: Validirane ostajajo trenutne reference OWASP Top 10 za LLM-je
  - **Azure storitve**: Preverjene vse povezave do Microsoft Azure dokumentacije in najboljših praks
- **Usklajenost s standardi**: Vsi navedeni varnostni standardi so potrjeni kot trenutni
  - Okvir za upravljanje tveganja NIST AI
  - ISO 27001:2022
  - Najboljše varnostne prakse OAuth 2.1
  - Okviri za varnost in skladnost Azure
- **Viri za implementacijo**: Preverjene vse povezave do vodnikov za implementacijo in vire
  - Avtentikacijski vzorci Azure API Management
  - Vodniki za integracijo Microsoft Entra ID
  - Upravljanje skrivnosti Azure Key Vault
  - DevSecOps cevovodi in rešitve za spremljanje

### Zagotavljanje kakovosti dokumentacije
- **Skladnost s specifikacijo**: Zagotovljena uskladitev vseh obveznih varnostnih zahtev MCP (MORA/MORA NE) z najnovejšo specifikacijo
- **Posodobljenost virov**: Preverjene vse zunanje povezave do Microsoftove dokumentacije, varnostnih standardov in implementacijskih vodnikov
- **Pokritost najboljših praks**: Potrjena celovita pokritost avtentikacije, avtorizacije, AI-specifičnih groženj, varnosti dobavne verige in podjetniških vzorcev

## 6. oktober 2025

### Razširitev razdelka Začetek – napredna raba strežnika in enostavna avtentikacija

#### Napredna raba strežnika (03-GettingStarted/10-advanced)
- **Dodano novo poglavje**: Predstavljen celovit vodnik za napredno rabo MCP strežnika, ki zajema tako običajno kot nizkonivojsko strežniško arhitekturo.
  - **Običajni proti nizkonivojskemu strežniku**: Podroben pregled in primeri kode v Pythonu in TypeScript za oba pristopa.
  - **Oblikovanje na osnovi upravljavca (handler)**: Pojasnilo upravljanja orodij/virov/promptov preko upravljavcev za skalabilne in prilagodljive implementacije strežnikov.
  - **Praktični vzorci**: Realni primeri, kjer so vzorci nizkonivojskih strežnikov koristni za napredne funkcionalnosti in arhitekturo.

#### Enostavna avtentikacija (03-GettingStarted/11-simple-auth)
- **Dodano novo poglavje**: Vodnik korak za korakom za implementacijo preproste avtentikacije v MCP strežnikih.
  - **Pojmi avtentikacije**: Jasno pojasnilo razlik med avtentikacijo in avtorizacijo ter ravnanja z poverilnicami.
  - **Implementacija osnovne avtentikacije**: Vzorci avtentikacije na ravni middleware v Pythonu (Starlette) in TypeScriptu (Express), s primeri kode.
  - **Napredovanje proti napredni varnosti**: Smernice za začetek z enostavno avtentikacijo in nadaljevanje proti OAuth 2.1 in RBAC, z referencami na napredne varnostne module.

Te dodatke nudijo praktične, praktične smernice za izdelavo robustnih, varnih in prilagodljivih MCP strežnikov, ki povezujejo temeljne koncepte z naprednimi produkcijskimi vzorci.

## 29. september 2025

### MCP Server Database Integration Labs – celovit praktični učni načrt

#### 11-MCPServerHandsOnLabs - nov celovit kurikulum integracije podatkovnih baz
- **Popolna 13-laboratorijska učna pot**: Dodan celovit praktični kurikulum za izdelavo produkcijsko pripravljenih MCP strežnikov z integracijo PostgreSQL baze podatkov
  - **Realni primer uporabe**: primer Zava Retail Analytics demonstrira vzorce podjetniške ravni
  - **Strukturiran potek učenja**:
    - **Lab 00-03: Temelji** – Uvod, jedrna arhitektura, varnost in večnajemništvo, nastavitev okolja
    - **Lab 04-06: Izgradnja MCP strežnika** – Oblikovanje baze podatkov in sheme, implementacija MCP strežnika, razvoj orodij
    - **Lab 07-09: Napredne funkcije** – Semantična integracija iskanja, testiranje in odpravljanje napak, integracija VS Code
    - **Lab 10-12: Produkcija in najboljše prakse** – Strategije namestitve, spremljanje in opazovanje, najboljše prakse in optimizacija
  - **Podjetniške tehnologije**: ogrodje FastMCP, PostgreSQL s pgvector, Azure OpenAI embedngi, Azure Container Apps, Application Insights
  - **Napredne funkcije**: Varovanje vrstic (RLS), semantično iskanje, dostop do podatkov za več najemnikov, vektorske vključitve, spremljanje v realnem času

#### Standardizacija terminologije – pretvorba modulov v laboratorije
- **Celovita posodobitev dokumentacije**: Sistematično posodobljene vse datoteke README v 11-MCPServerHandsOnLabs za uporabo termina "Lab" namesto "Module"
  - **Naslovi oddelkov**: Posodobljeno "Kaj ta modul pokriva" v "Kaj ta lab pokriva" v vseh 13 laboratorijih
  - **Opis vsebine**: Spremenjeno "Ta modul zagotavlja..." v "Ta lab zagotavlja..." po celotni dokumentaciji
  - **Cilji učenja**: Posodobljeno "Na koncu tega modula..." v "Na koncu tega lab-a..."
  - **Navigacijske povezave**: Pretvorjene vse reference "Modul XX:" v "Lab XX:" v prečnih povezavah in navigaciji
  - **Sledenje dokončanju**: Posodobljeno "Po zaključku tega modula..." v "Po zaključku tega lab-a..."
  - **Ohranjene tehnične reference**: Ohranjene Pythonove reference na module v konfiguracijskih datotekah (npr. `"module": "mcp_server.main"`)

#### Izboljšava učnega vodiča (study_guide.md)
- **Vizualni zemljevid kurikuluma**: Dodan nov odsek "11. Database Integration Labs" s celovito vizualizacijo strukture laboratov
- **Struktura repozitorija**: Posodobljeno iz deset na enajst glavnih odsekov z podrobnim opisom 11-MCPServerHandsOnLabs
- **Usmeritve učenja**: Izboljšana navodila za navigacijo odsekov 00-11
- **Pokritost tehnologij**: Dodane podrobnosti o FastMCP, PostgreSQL in integraciji Azure storitev
- **Izhodi učenja**: Poudarjena izdelava produkcijsko pripravljenih strežnikov, vzorci integracije baz podatkov in varnost podjetja

#### Izboljšava glavne strukture README
- **Terminologija na osnovi laboratorijev**: Posodobljen glavni README.md v 11-MCPServerHandsOnLabs za konsistentno uporabo strukture "Lab"
- **Organizacija učne poti**: Jasna pot od temeljnih konceptov do napredne implementacije in produkcijske namestitve
- **Osredotočenost na prakso**: Poudarek na praktičnem učenju z vzorci podjetniške ravni in tehnologijami

### Izboljšave kakovosti in skladnosti dokumentacije
- **Poudarek na praktičnem učenju**: Okrepljen praktičen, laboratorijsko usmerjen pristop po celotni dokumentaciji
- **Poudarek na podjetniških vzorcih**: Izpostavljena produkcijsko pripravljene implementacije in podjetniške varnosti
- **Integracija tehnologij**: Celovita pokritost sodobnih Azure storitev in vzorcev AI integracije
- **Napredovanje učenja**: Jasna in strukturirana pot od osnovnih konceptov do produkcijske namestitve

## 26. september 2025

### Izboljšave študij primerov – integracija GitHub MCP registre

#### Študije primerov (09-CaseStudy/) – Osredotočenost na razvoj ekosistema
- **README.md**: Obsežna razširitev z obsežno študijo primera GitHub MCP registre
  - **Študija primera GitHub MCP registre**: Nova celovita študija primera, ki preučuje lansiranje MCP registre GitHub septembra 2025
    - **Analiza problema**: Podroben pregled fragmentiranega odkrivanja in nameščanja MCP strežnikov
    - **Arhitektura rešitve**: GitHubov centraliziran register z enostavno namestitvijo preko VS Code z enim klikom
    - **Poslovni učinek**: Merljive izboljšave onboardinga in produktivnosti razvijalcev
    - **Strateška vrednost**: Fokus na modularni namestitvi agentov in medorodjni interoperabilnosti orodij
    - **Razvoj ekosistema**: Pozicioniranje kot osnovna platforma za agencijsko integracijo
  - **Izboljšana struktura študij primerov**: Posodobljenih vseh sedem študij primerov s konsistentnim formatom in podrobnimi opisi
    - Azure AI Travel Agents: poudarek na večagentorski orkestraciji
    - Azure DevOps integracija: osredotočenost na avtomatizacijo potekov dela
    - Pridobivanje dokumentacije v realnem času: implementacija Python konzolnega odjemalca
    - Interaktivni generator učnih načrtov: spletna aplikacija Chainlit za pogovore
    - Dokumentacija v urejevalniku: integracija VS Code in GitHub Copilot
    - Azure API Management: vzorci integracije API podjetja
    - GitHub MCP Registry: razvoj ekosistema in skupnostna platforma
  - **Celovit zaključek**: Predelana zaključna sekcija, ki izpostavlja sedem študij primerov, ki zajemajo različne dimenzije implementacije MCP
    - Podjetniška integracija, večagentorska orkestracija, produktivnost razvijalcev
    - Razvoj ekosistema, kategorizacija izobraževalnih aplikacij
    - Izboljšani vpogledi v arhitekturne vzorce, strategije implementacije in najboljše prakse
    - Poudarek na MCP kot zrelem, produkcijsko pripravljenem protokolu

#### Posodobitve učnega vodiča (study_guide.md)
- **Vizualni zemljevid kurikuluma**: Posodobljen mindmap za vključitev GitHub MCP registre v razdelek Študije primerov
- **Opis študij primerov**: Izboljšan iz splošnih opisov v podrobno razčlenitev sedmih celovitih študij primerov
- **Struktura repozitorija**: Posodobljen odsek 10 za odsev celovite pokritosti študij primerov s specifičnimi podrobnostmi implementacije
- **Integracija changeloga**: Dodan vnos za 26. september 2025, ki dokumentira dodatek GitHub MCP registre in izboljšave študij primerov
- **Posodobitev datuma**: Posodobljen spodnji časovni žig na zadnjo revizijo (26. september 2025)

### Izboljšave kakovosti dokumentacije
- **Izboljšanje skladnosti**: Standardiziran format in struktura študij primerov po vseh sedmih primerih
- **Celovita pokritost**: Študije primerov zdaj zajemajo scenarije podjetniške rabe, produktivnosti razvijalcev in razvoja ekosistema
- **Strateško pozicioniranje**: Okrepčen fokus na MCP kot temeljno platformo za agencijski sistem in namestitev
- **Integracija virov**: Posodobljeni dodatni viri z vključitvijo povezave GitHub MCP registre

## 15. september 2025

### Razširitev naprednih tem – prilagojeni transporti in kontekstno inženirstvo

#### Prilagojeni transporti MCP (05-AdvancedTopics/mcp-transport/) – nov vodnik za napredno implementacijo
- **README.md**: Popoln vodnik za implementacijo prilagojenih transportnih mehanizmov MCP
  - **Azure Event Grid transport**: Celovita implementacija strežnika brez strežnika na osnovi dogodkov
    - Primeri v C#, TypeScript in Python z integracijo Azure Functions
    - Arhitekturni vzorci na osnovi dogodkov za skalabilne MCP rešitve
    - Sprejemniki webhookov in upravljanje sporočil na osnovi push
  - **Azure Event Hubs transport**: Implementacija pretočnega transporta z visoko prepustnostjo
    - Zmožnosti pretočnega prenosa v realnem času za nizko zakasnitev
    - Strategije particioniranja in upravljanje kontrolnih točk
    - Pakiranje sporočil in optimizacija zmogljivosti
  - **Podjetniški vzorci integracije**: Produkcijsko pripravljeni arhitekturni primeri
    - Distribuirana MCP obdelava preko več Azure Functions
    - Hibridne arhitekture transportov z združitvijo več tipov transporta
    - Strategije vzdržljivosti, zanesljivosti in upravljanja napak sporočil
  - **Varnost in spremljanje**: Integracija Azure Key Vault in vzorci opazovanja
    - Avtentikacija upravljane identitete in dostop po načelu najmanjše privilegije
    - Telemetrija Application Insights in spremljanje zmogljivosti
    - Prekinitveni vzorci in vzorci odpornosti na napake
  - **Testna orodja**: Celovite testne strategije za prilagojene transporte
    - Enotsko testiranje s testnimi dvojčki in ogrodji za posnemanje
    - Integracijsko testiranje z Azure Test Containers
    - Ohranjanje zmogljivosti in obremenitveno testiranje

#### Kontekstno inženirstvo (05-AdvancedTopics/mcp-contextengineering/) – nastajajoča disciplina AI
- **README.md**: Celovita raziskava kontekstnega inženirstva kot nastajajočega področja
  - **Osnovna načela**: Popolno deljenje konteksta, zavedanje odločitev ukrepov in upravljanje kontekstnega okna
  - **Usklajenost z MCP protokolom**: Kako dizajn MCP rešuje izzive kontekstnega inženirstva
    - Omejitve kontekstnih oken in strategije progresivnega nalaganja
    - Določanje relevantnosti in dinamično pridobivanje konteksta
    - Upravljanje multimodalnega konteksta in varnostne zahteve
  - **Pristopi implementacije**: Enoniti proti večagentorskim arhitekturam
    - Tehnike razdeljevanja konteksta in prioritizacije
    - Progresivno nalaganje konteksta in strategije stiskanja
    - Večplastni pristopi in optimizacija pridobivanja
  - **Merilni okvir**: Nastajajoče metrike za ocenjevanje učinkovitosti konteksta
    - Učinkovitost vnosa, zmogljivost, kvaliteta in uporabniška izkušnja
    - Eksperimentalne metode za optimizacijo konteksta
    - Analiza napak in metode izboljšav

#### Posodobitve navigacije kurikuluma (README.md)
- **Izboljšana struktura modulov**: Posodobljena tabela kurikuluma za vključitev novih naprednih tem
  - Dodani vnosi za Kontekstno inženirstvo (5.14) in Prilagojeni transport (5.15)
  - Konsistentno oblikovanje in navigacijske povezave čez vse module
  - Posodobljeni opisi za odsev trenutnega obsega vsebine

### Izboljšave strukture imenikov
- **Standardizacija imen**: Preimenovan "mcp transport" v "mcp-transport" za skladnost z drugimi mapami naprednih tem
- **Organizacija vsebine**: Vse mape 05-AdvancedTopics sledijo doslednemu vzorcu imen (mcp-[tema])

### Izboljšave kakovosti dokumentacije
- **Usklajenost MCP specifikacije**: Vsa nova vsebina navaja trenutno MCP specifikacijo 2025-06-18
- **Vzorci kode v več jezikih**: Celoviti primeri kode v C#, TypeScript in Python
- **Poudarek na podjetništvu**: Produkcijsko pripravljeni vzorci in integracija Azure oblaka
- **Vizualna dokumentacija**: Mermaid diagrami za vizualizacijo arhitekture in poteka

## 18. avgust 2025

### Celovita posodobitev dokumentacije - MCP standardi 2025-06-18

#### Najboljše varnostne prakse MCP (02-Security/) – popolna modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Popolna predelava usklajena s specifikacijo MCP 2025-06-18  
  - **Obvezne zahteve**: Dodane eksplicitne zahteve MORATE/MORATE NE iz uradne specifikacije z jasnimi vizualnimi indikatorji  
  - **12 osnovnih varnostnih praks**: Prestrukturirano s seznama 15 elementov v obsežne varnostne domene  
    - Varnost žetonov in avtentikacija z integracijo zunanjega ponudnika identitete  
    - Upravljanje sej in varnost prenosa s kriptografskimi zahtevami  
    - Zavarovanje pred grožnjami specifičnimi za AI z integracijo Microsoft Prompt Shields  
    - Dostopno upravljanje in dovoljenja s principom najmanjših privilegijev  
    - Varnost vsebin in nadzor z integracijo Azure Content Safety  
    - Varnost dobavne verige s celovito verifikacijo komponent  
    - Varnost OAuth in preprečevanje Confused Deputy z implementacijo PKCE  
    - Odziv na incidente in obnova z avtomatiziranimi zmogljivostmi  
    - Skladnost in upravljanje z usklajenostjo z regulacijo  
    - Napredni varnostni nadzori z arhitekturo ničelnega zaupanja  
    - Integracija Microsoftovega varnostnega ekosistema s celovitimi rešitvami  
    - Neprestani razvoj varnosti z adaptivnimi praksami  
  - **Microsoftove varnostne rešitve**: Izboljšana navodila za integracijo Prompt Shields, Azure Content Safety, Entra ID in GitHub Advanced Security  
  - **Implementacijski viri**: Kategorizirani celoviti povezovalniki virov po uradni MCP dokumentaciji, Microsoftovih varnostnih rešitvah, varnostnih standardih in implementacijskih vodičih  

#### Napredni varnostni nadzori (02-Security/) - Izvedba za podjetja  
- **MCP-SECURITY-CONTROLS-2025.md**: Popolna prenova z varnostnim ogrodjem za podjetja  
  - **9 celovitih varnostnih domen**: Razširjene iz osnovnih nadzorov v podrobno ogrodje za podjetja  
    - Napredna avtorizacija in avtentičnost z integracijo Microsoft Entra ID  
    - Varnost žetonov in nadzori proti nepooblaščenemu prehajanju s celovito validacijo  
    - Nadzor varnosti sej s preprečevanjem ugrabitve  
    - Varnostni nadzori specifični za AI s preprečevanjem vbrizgavanja zahtev in zastrupitve orodij  
    - Preprečevanje Confused Deputy napadov z varnostjo OAuth proxyja  
    - Varnost zagona orodij s peskovnikom in izolacijo  
    - Varnostni nadzori dobavne verige z verifikacijo odvisnosti  
    - Nadzor in detekcija z integracijo SIEM  
    - Odziv na incidente in obnova z avtomatiziranimi zmožnostmi  
  - **Primeri izvedbe**: Dodani podrobni YAML konfiguracijski bloki in primeri kode  
  - **Integracija Microsoftovih rešitev**: Celovita pokritost Azure varnostnih storitev, GitHub Advanced Security in upravljanja identitete za podjetja  

#### Napredne varnostne teme (05-AdvancedTopics/mcp-security/) - Izvedba pripravljena za produkcijo  
- **README.md**: Popolna predelava za varnostno izvedbo v podjetjih  
  - **Uskladitev z aktualno specifikacijo**: Posodobljeno skladno s MCP specifikacijo 2025-06-18 z obveznimi varnostnimi zahtevami  
  - **Izboljšana avtorizacija**: Integracija Microsoft Entra ID z celovitimi primeri v .NET in Java Spring Security  
  - **Integracija varnosti AI**: Implementacija Microsoft Prompt Shields in Azure Content Safety z podrobnimi primeri v Pythonu  
  - **Napredno blaženje groženj**: Celoviti primeri izvedbe za  
    - Preprečevanje Confused Deputy napadov z PKCE in validacijo uporabniškega soglasja  
    - Preprečevanje prehoda žetona z validacijo občinstva in varnim upravljanjem žetonov  
    - Preprečevanje ugrabitve seje z kriptografskim povezovanjem in analizo vedenja  
  - **Integracija varnosti podjetja**: Nadzor z Azure Application Insights, cevovodi za odkrivanje groženj in varnost dobavne verige  
  - **Kontrolni seznam za izvedbo**: Jasna razdelitev obveznih in priporočljivih varnostnih nadzorov z dobrobitmi Microsoftovega varnostnega ekosistema  

### Kakovost dokumentacije in usklajevanje s standardi  
- **Reference specifikacij**: Posodobljene vse reference na trenutno MCP specifikacijo 2025-06-18  
- **Microsoftov varnostni ekosistem**: Izboljšana integracijska navodila v vsej varnostni dokumentaciji  
- **Praktična izvedba**: Dodani podrobni primeri kode v .NET, Java in Python z vzorci za podjetja  
- **Organizacija virov**: Celovita kategorizacija uradnih dokumentov, varnostnih standardov in implementacijskih vodičev  
- **Vizualni indikatorji**: Jasna označitev obveznih zahtev rispetto priporočenim praksam  

#### Osnovni koncepti (01-CoreConcepts/) - Popolna modernizacija  
- **Posodobitev verzije protokola**: Posodobljeno na referenco trenutne MCP specifikacije 2025-06-18 z letno-mesečno-dnevno oznako (YYYY-MM-DD)  
- **Izboljšave arhitekture**: Izpopolnjeni opisi gostiteljev, odjemalcev in strežnikov za odražanje trenutnih MCP arhitekturnih vzorcev  
  - Gostitelji so sedaj jasno definirani kot AI aplikacije, ki koordinirajo več povezav MCP odjemalcev  
  - Odjemalci opisani kot protokolni povezovalci, ki vzdržujejo ena-na-ena razmerje s strežnikom  
  - Strežniki izpopolnjeni z lokalnimi naspram oddaljenim scenariji nameščanja  
- **Prenova primitov**: Popolna prenova strežniških in odjemalskih primitov  
  - Strežniški primiti: Viri (viri podatkov), Zahteve (predloge), Orodja (izvedljive funkcije) z podrobnimi pojasnili in primeri  
  - Odjemalski primiti: Vzorečenje (LLM zaključki), Povpraševanje (vnos uporabnika), Beleženje (debugging/nadzor)  
  - Posodobljeni s trenutnimi vzorci metod odkrivanja (`*/list`), pridobivanja (`*/get`) in izvedbe (`*/call`)  
- **Arhitektura protokola**: Uveden model dvoslojne arhitekture  
  - Podatkovni sloj: Oprti na JSON-RPC 2.0 s upravljanjem življenjskega cikla in primitivov  
  - Transportni sloj: STDIO (lokalni) in Streamable HTTP s SSE (oddaljeni) transportni mehanizmi  
- **Varnostno ogrodje**: Celoviti varnostni principi, vključno z eksplicitnim uporabniškim soglasjem, varovanjem zasebnosti podatkov, varnostjo zagona orodij in varnostjo transportnega sloja  
- **Vzorce komunikacije**: Posodobljena protokolna sporočila za inicializacijo, odkrivanje, izvedbo in obvestila  
- **Primeri kode**: Osveženi primeri v več jezikih (.NET, Java, Python, JavaScript) za odražanje trenutnih MCP SDK vzorcev  

#### Varnost (02-Security/) - Celovita prenova varnosti  
- **Uskladitev s standardi**: Popolna uskladitev z varnostnimi zahtevami MCP Specifikacije 2025-06-18  
- **Evolucija avtentičnosti**: Dokumentirana evolucija od lastnih OAuth strežnikov do delegacije zunanjim ponudnikom identitete (Microsoft Entra ID)  
- **Analiza groženj specifičnih za AI**: Izboljšana pokritost sodobnih AI napadalnih vektorjev  
  - Podrobni scenariji napadov z vbrizgavanjem zahtev z realnimi primeri  
  - Mehanizmi zastrupitve orodij in vzorci "rug pull" napadov  
  - Zastrupitev kontekstnega okna in zmedeni modeli napadov  
- **Microsoftove AI varnostne rešitve**: Celovita pokritost Microsoftovega varnostnega ekosistema  
  - AI Prompt Shields z napredno detekcijo, označevanjem in tehnikami ločevanja  
  - Vzorce integracije Azure Content Safety  
  - GitHub Advanced Security za zaščito dobavne verige  
- **Napredni ukrepi proti grožnjam**: Podrobni varnostni nadzori za  
  - Ugrabitev seje s MCP-specifičnimi scenariji napadov in kriptografskimi zahtevami za ID seje  
  - Problemi Confused Deputy v MCP proxy scenarijih z eksplicitnimi zahtevami soglasja  
  - Ranljivosti pri prehodu žetonov z obveznimi validacijskimi kontrolami  
- **Varnost dobavne verige**: Razširjena pokritost dobavne verige AI vključno z osnovnimi modeli, storitvami vdelav, ponudniki konteksta in API-ji tretjih oseb  
- **Osnovna varnost**: Izboljšana integracija z varnostnimi vzorci za podjetja, vključno z arhitekturo ničelnega zaupanja in Microsoftovim varnostnim ekosistemom  
- **Organizacija virov**: Kategorizirani celoviti povezovalniki virov po tipu (Uradni dokumenti, standardi, raziskave, Microsoftove rešitve, implementacijski vodiči)  

### Izboljšave kakovosti dokumentacije  
- **Strukturirani učni cilji**: Izboljšani učni cilji z jasnimi, izvedljivimi rezultati  
- **Medsebojne reference**: Dodane povezave med povezanimi varnostnimi in osnovnimi temami  
- **Aktualne informacije**: Posodobljene vse datumske reference in povezave na aktualne standarde  
- **Navodila za izvedbo**: Dodana specifična navodila za izvedbo skozi obe sekciji  

## 16. julij 2025  

### Izboljšave README in navigacije  
- Popolnoma prenovljena struktura navigacije v README.md  
- Nadomestitev `<details>` oznak z bolj dostopno tabelarično postavitvijo  
- Ustvarjene alternativne postavitve v novi mapi "alternative_layouts"  
- Dodani primeri navigacije s karticami, zavihki in akordeoni  
- Posodobljen odsek o strukturi repozitorija z vključitvijo vseh najnovejših datotek  
- Izboljšan odsek "Kako uporabljati ta kurikulum" z jasnimi priporočili  
- Posodobljene povezave na MCP specifikacijo, ki kažejo na pravilne URL-je  
- Dodan odsek o kontekstnem inženirstvu (5.14) v strukturo kurikuluma  

### Posodobitve učnega vodiča  
- Popolnoma prenovljen učni vodič v skladu s trenutno strukturo repozitorija  
- Dodani novi razdelki za MCP odjemalce in orodja ter priljubljene MCP strežnike  
- Posodobljen Vizualni zemljevid kurikuluma za natančno prikazovanje vseh tem  
- Izboljšani opisi naprednih tem, da pokrivajo vse specializirane področja  
- Posodobljen odsek primerov uporabe z dejanskimi primeri  
- Dodan ta podroben dnevnik sprememb  

### Prispevki skupnosti (06-CommunityContributions/)  
- Dodane podrobne informacije o MCP strežnikih za generiranje slik  
- Dodan celovit odsek o uporabi Claude v VSCode  
- Dodani navodila za nastavitev in uporabo terminalskega odjemalca Cline  
- Posodobljen razdelek MCP odjemalcev z vsemi priljubljenimi možnostmi  
- Izboljšani primeri prispevkov z natančnejšimi vzorci kode  

### Napredne teme (05-AdvancedTopics/)  
- Organizirane vse specializirane teme s konsistentnim poimenovanjem  
- Dodani materiali in primeri za kontekstno inženirstvo  
- Dodana dokumentacija za integracijo Foundry agenta  
- Izboljšana dokumentacija za integracijo varnosti Entra ID  

## 11. junij 2025  

### Prva izdaja  
- Izdan prvi verzijski MCP za začetnike  
- Ustvarjena osnovna struktura vseh 10 glavnih sekcij  
- Implementiran Vizualni zemljevid kurikuluma za navigacijo  
- Dodani začetni vzorčni projekti v več programskih jezikih  

### Začetek (03-GettingStarted/)  
- Prvi primeri izvajanja strežnika  
- Dodani vodniki za razvoj odjemalcev  
- Vključene navodila za integracijo LLM odjemalcev  
- Dodana dokumentacija za integracijo VS Code  
- Implementirani primeri Server-Sent Events (SSE) strežnika  

### Osnovni koncepti (01-CoreConcepts/)  
- Dodan podroben opis odjemalec-strežnik arhitekture  
- Ustvarjena dokumentacija ključnih protokolnih komponent  
- Dokumentirani vzorci sporočil v MCP  

## 23. maj 2025  

### Struktura repozitorija  
- Inicializirana struktura repozitorija z osnovno razporeditvijo map  
- Ustvarjene README datoteke za vsako glavno sekcijo  
- Nastavljena infrastruktura za prevode  
- Dodani slikovni viri in diagrami  

### Dokumentacija  
- Ustvarjen začetni README.md z pregledom kurikuluma  
- Dodana datoteka CODE_OF_CONDUCT.md in SECURITY.md  
- Nastavljen SUPPORT.md z usmeritvami za pomoč  
- Ustvarjena začetna struktura učnega vodiča  

## 15. april 2025  

### Načrtovanje in ogrodje  
- Začetno načrtovanje MCP za začetnike kurikula  
- Določeni učni cilji in ciljna publika  
- Osnutek strukture kurikuluma z 10 sekcijami  
- Razvit konceptualni okvir za primere in študije primerov  
- Ustvarjeni začetni prototipni primeri za ključne koncepte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvor nem jeziku velja kot avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne napačne razlage ali zgrešene pomene, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->