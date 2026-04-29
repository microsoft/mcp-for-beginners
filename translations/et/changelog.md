# Muudatuste logi: MCP algajatele programmiõppekava

See dokument toimib kõigi Model Context Protocoli (MCP) algajatele programmiõppekava oluliste muudatuste kirjeldusena. Muudatused on dokumenteeritud pöördselt kronoloogilises järjekorras (uusimad muudatused ees).

## 11. aprill 2026

### Uus õppetund, dokumentatsiooni parandused ja sõltuvuste uuendused

#### Lisatud uus õppekava sisu

**Moodul 05 - Täiustatud teemad**
- **Õppetund 5.17: Vastandlik mitmeagendi järeldamine MCP-ga** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Uus põhjalik juhend, mis käsitleb vastandliku debati mustrit mitmeagendi süsteemide jaoks
  - Mermaid arhitektuuri diagramm: kaks agenti → ühine MCP server → debati transkriptsioon → kohtunik → otsus
  - Ühine MCP tööriistade server (`web_search` + `run_python`) rakendatud Pythonis ja TypeScriptis
  - Vastaspoole süsteemipromptid (NÕUAVAD / VASTUVÄITES / Kohtunik) koos selgete tööriista kasutamise nõuetega
  - Debati korraldaja Pythonis, TypeScriptis ja C#-s, juhib voorusid ja argumentide suunamist
  - MCP `ClientSession` ühendus korraldajaga päris tööriistakõnede jaoks
  - Kasutusjuhtumite tabel (hallutsinatsioonide tuvastamine, ohu modelleerimine, API-disaini ülevaatus, faktide kontrollimine, tehnoloogia valik)
  - Turvalisuse kaalutlused: sandboxitud täitmine, tööriistakõnede valideerimine, kiirusepiirang, auditeerimislogi
  - Struktureeritud harjutus kolme praktilise stsenaariumiga (koodikontroll, arhitektuuri otsus, sisu modereerimine)

#### Dokumentatsiooni parandused

**Moodul 03 - Algus**
- **05-stdio-server/README.md**: Parandatud puudulik TypeScripti stdio serveri näide — lisatud puuduv transpordi instants (`new StdioServerTransport()`) ja `server.connect(transport)` kõne, et vastata Python ja .NET näidetele samas sektsioonis
- **14-sampling/README.md**: Parandatud trükkviga — parandatud `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Õppekava uuendused

**Peamine README.md**
- Lisatud 5.17. kirje (Vastandlik mitmeagendi järeldamine MCP-ga) õppekava tabelisse koos otselinkiga uude õppetundi

**05-AdvancedTopics/README.md**
- Lisatud õppetunni 5.17 rida õppetundide tabelisse

**study_guide.md**
- Lisatud Vastandliku mitmeagendi järeldamise teema mõttekaardile ja proosa kirjeldusele Täiustatud teemade sektsioonis

#### Koodi ja turvalisuse parandused

**Moodul 05 - Vastandlikud agendid (`mcp-adversarial-agents`)**
- **Turvalisuse parandus — käsu süstimine**: Asendatud TypeScripti `run_python` tööriista `execSync` käsu interpolatsioon `execFile` + `promisify` kasutusega, likvideerides käsu süstimise võimaluse (LLM-i kontrollitud kood edastatakse nüüd sõnasõnaliselt argv elemendina ilma shelli sekkumiseta)
- **MCP tööriista tsükli juhtimine**: Uuendatud Python debati korraldaja kasutama `AsyncAnthropic` klienti (asendab takistavat sünkroonset `Anthropic`-ut), edastab iga agendi käigu jaoks live `ClientSession` otse, hangib tööriistade definitsioonid igas voorus `session.list_tools()` abil ja edastab `tool_use` plokid `session.call_tool()` meetodiga tsükliliselt kuni mudel edastab lõpliku teksti vastuse

#### Sõltuvuste uuendused

- Uuendatud `hono` versioon 4.12.12 mitmes paketis (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Uuendatud `@hono/node-server` versioon 1.19.11-st 1.19.13-ni TypeScripti paketis
- Uuendatud `cryptography` versioon 46.0.5-lt 46.0.7-ni Python paketis (10-StreamliningAIWorkflows laborid 3 ja 4)
- Uuendatud `lodash` versioon 4.17.23-st 4.18.1-ni 10-StreamliningAIWorkflows inspekteerijas

#### Tõlked

- Sünkroonitud tõlked 48+ keeles vastavalt uusimatele lähtekoodimuudatustele (i18n uuendus)

---

## 5. veebruar 2026

### Aruandelaia valideerimine ja navigeerimise parandused

#### Lisatud uus õppekava sisu

**Moodul 03 - Algus**
- **12-mcp-hosts/README.md**: Uus põhjalik juhend MCP hostide seadistamiseks
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfiguratsiooni näited
  - Kõigi peamiste hostide JSON konfiguratsiooni mallid
  - Transpordi tüüpide võrdlustabel (stdio, SSE/HTTP, WebSocket)
  - Levinumate ühendusprobleemide tõrkeotsingu juhend
  - Hostide konfiguratsiooni turvalisuse parimad tavad

- **13-mcp-inspector/README.md**: Uus silumine MCP Inspectoriga
  - Paigaldusmeetodid (npx, npm globaalne, lähtekoodist)
  - Ühendamine serveritega stdio ja HTTP/SSE kaudu
  - Testimisvahendid, ressursid ja promptide töövood
  - VS Code integreerimine MCP Inspectoriga
  - Levinumad silumisstsenaariumid lahendustega

**Moodul 04 - Praktiline rakendamine**
- **pagination/README.md**: Uus leheküpitusjuhtide juhend
  - Kursoripõhised leheküpitusmustrid Pythonis, TypeScriptis, Javas
  - Kliendipoolne leheküptuse käsitlemine
  - Kursori disaini strateegiad (opak vs struktureeritud)
  - Jõudluse optimeerimise soovitused

**Moodul 05 - Täiustatud teemad**
- **mcp-protocol-features/README.md**: Uued protokolli funktsioonide põhjalik ülevaade
  - Edusammude teavitamise rakendus
  - Päringu tühistamise mustrid
  - Ressursside mallid URI mustritega
  - Serveri elutsükli haldus
  - Logitaseme juhtimine
  - Vea käsitlemise mustrid JSON-RPC koodidega

#### Navigeerimise parandused (24+ faili uuendatud)

**Põhimooduli README failid**
 Nüüd lingivad nii esimesele õppetunnile KUI ka järgmisele moodulile

**02-Security alamfailid**
- Kõigil 5 lisaturvalisuse dokumendil on nüüd "Mis edasi" navigeerimine:

**09-CaseStudy failid**
- Kõigil juhtumiuuringu failidel on nüüd järjestikulise navigeerimise võimalus:

**10-StreamliningAI Laborid**
Lisatud "Mis edasi" sektsioon Moodul 10 ülevaatesse ja Moodul 11-le

#### Koodi ja sisu parandused

**SDK ja sõltuvuste uuendused**
Parandatud tühi openai versioon `^4.95.0`
Uuendatud SDK versioonilt `^1.8.0` kuni `>=1.26.0`
Uuendatud mcp versioonide piirangud `>=1.26.0`

**Koodi parandused**
Parandatud vale mudel `gpt-4o-mini` → `gpt-4.1-mini`

**Sisu parandused**
Parandatud katkine link `READMEmd` → `README.md`, parandatud õppekava päise nimetus `Module 1-3` → `Module 0-3`, parandatud suurtähega tee
Eemaldatud rikutud dubleeritud Juhtumiuuring 5 sisu

**Algajate juhised**
Lisatud korralik sissejuhatus, õpieesmärgid ja eeltingimused algajatele

#### Õppekava uuendused

**Peamine README.md**
- Lisatud kirjed 3.12 (MCP majutajad), 3.13 (MCP Inspector), 4.1 (Leheküpitus), 5.16 (Protokolli funktsioonid) õppekava tabelisse

**Mooduli README-d**
Lisatud õppetunnid 12 ja 13 õppetundide nimekirja
Lisatud praktiliste juhendite sektsioon leheküpituselinkiga
Lisatud õppetunnid 5.15 (Kohandatud transpordi) ja 5.16 (Protokolli funktsioonid)

**study_guide.md**
- Uuendatud mõttekaart kõigi uute teemadega: MCP majutajate seadistus, MCP Inspector, leheküpituse strateegiad, protokolli süvitsi ülevaade

## 28. jaanuar 2026

### MCP Spetsifikatsiooni 2025-11-25 vastavuse ülevaade

#### Põhimõistete täiustamine (01-CoreConcepts/)
- **Uus kliendi primitiiv - Roots**: Lisatud põhjalik dokumentatsioon Roots kliendi primitiivi kohta, võimaldades serveritel mõista failisüsteemi piire ja juurdepääsuõigusi
- **Tööriista annotatsioonid**: Lisatud dokumentatsioon tööriista käitumise annotatsioonide (`readOnlyHint`, `destructiveHint`) kohta paremate tööriistade täitmise otsuste tegemiseks
- **Tööriistade kutsumine proovimisel**: Uuendatud Proovimise dokumentatsiooni, lisades parameetrid `tools` ja `toolChoice` mudelipõhiseks tööriistade kutseks proovipäringute ajal
- **URL režiimi esiletoomine**: Lisatud dokumentatsioon URL-põhise esiletoomise kohta serveri algatatud väliste veebitegevuste jaoks
- **Ülesanded (katsefaas)**: Lisatud uus sektsioon, mis dokumenteerib katsetamise faasis oleva Ülesannete funktsiooni vastupidavate täitmiskestade ja tulemustooste edasilükkamiseks
- **Ikoonide tugi**: Märgitud, et tööriistad, ressursid, ressursmallid ja promptid võivad nüüd sisaldada ikoone lisametainfona

#### Dokumentatsiooni uuendused
- **README.md**: Lisatud MCP Spetsifikatsiooni 2025-11-25 versiooni viide ja kuupõhine versioneerimise selgitus
- **study_guide.md**: Uuendatud õppekava kaarti, lisades Ülesanded ja Tööriista annotatsioonid põhikontseptsioonide sektsiooni; uuendatud dokumendi ajatemplit

#### Spetsifikatsiooni vastavuse kontroll
- **Protokolli versioon**: Kinnitused, et kogu dokumentatsioon viitab MCP Spetsifikatsioonile 2025-11-25
- **Arhitektuuri vastavus**: Kinnitatud kahekihilise arhitektuuri (Andmekiht + Transpordikiht) dokumentatsiooni täpsus
- **Primitiivide dokumentatsioon**: Kontrollitud serveri primitiive (ressursid, promptid, tööriistad) ja kliendi primitiive (proovimine, esiletoomine, logimine, Roots)
- **Transpordimehhanismid**: Kontrollitud STDIO ja voogedastatava HTTP transpordi dokumentatsiooni täpsust
- **Turvalisuse juhised**: Kinnitatud kooskõla praeguste MCP turvalisuse parimate tavade dokumentatsiooniga

#### Põhifunktsioonid MCP 2025-11-25 spetsifikatsioonist dokumenteeritud
- **OpenID Connect avastamine**: Autentimisserveri avastamine OIDC kaudu
- **OAuth kliendi ID metaandmete dokumendid**: Soovitatav kliendi registreerimise mehhanism
- **JSON Schema 2020-12**: MCP skeemi definitsioonide vaikekeel
- **SDK kihistussüsteem**: Ametlik SDK funktsioonide toe ja hoolduse nõuded
- **Valitsemise struktuur**: Ametlikud töörühmad ja huvirühmad MCP valitsemises

### Turvamistiku suured uuendused (02-Security/)

#### MCP Security Summit töötoa (Sherpa) integratsioon
- **Uus praktiline koolitusressurss**: Lisatud põhjalik integratsioon [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) kogu turvadokumentatsiooni ulatuses
- **Ekspeditsiooni marsruudi kajastus**: Dokumenteeritud täielik laagrilt laagrile liikumise progresioon Base Camp-ist Summit-ini
- **OWASP kooskõla**: Kõik turvajuhised nüüd kaardistatud OWASP MCP Azure Security Guide riskidega

#### OWASP MCP Top 10 integreerimine
- **Uus sektsioon**: Lisatud OWASP MCP Top 10 turvariskide tabel koos Azure leevendustega peamise turvalisuse README-sse
- **Risikipõhine dokumentatsioon**: Uuendatud mcp-security-controls-2025.md OWASP MCP riskiviidetega iga turvalisuse domeeni kohta
- **Viitearhitektuur**: Lingitud OWASP MCP Azure Security Guide viitearhitektuuri ja rakendusmustritega

#### Uuendatud turvafailid
- **README.md**: Lisatud Sherpa töötoa ülevaade, ekspeditsiooniraja tabel, OWASP MCP Top 10 riskide kokkuvõte ja praktiline koolitussektsioon
- **mcp-security-controls-2025.md**: Uuendatud päis veebruar 2026, lisatud OWASP riskiviited (MCP01-MCP08), parandatud spetsifikatsiooni versiooni ebajärjekindlus
- **mcp-security-best-practices-2025.md**: Lisatud Sherpa ja OWASP ressursside sektsioon, uuendatud ajatemplit
- **mcp-best-practices.md**: Lisatud praktilise koolituse sektsioon Sherpa ja OWASP linkidega
- **azure-content-safety-implementation.md**: Lisatud OWASP MCP06 viide, Sherpa Camp 3 kooskõla ja lisanduvad ressursid

#### Lisatud uued ressursside lingid
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuaalsed OWASP MCP riski lehed (MCP01-MCP10)

### Õppekava MCP Spetsifikatsiooni 2025-11-25 ühtlustamine

#### Moodul 03 - Algus
- **SDK dokumentatsioon**: Lisatud Go SDK ametliku SDK nimekirja; uuendatud kõik SDK viited MCP Spetsifikatsioon 2025-11-25-ga kooskõlla
- **Transpordi täpsustus**: Uuendatud STDIO ja HTTP voogedastuse transpordi kirjeldused koos selgete spetsifikatsiooni viidetega

#### Moodul 04 - Praktiline rakendamine
- **SDK uuendused**: Lisatud Go SDK; uuendatud SDK nimekiri koos spetsifikatsiooni versiooni viitega
- **Autoriseerimise spetsifikatsioon**: Uuendatud MCP Autoriseerimise spetsifikatsiooni link praegusele 2025-11-25 versioonile

#### Moodul 05 - Täiustatud teemad
- **Uued funktsioonid**: Lisatud märkus MCP Spetsifikatsiooni 2025-11-25 uutest funktsioonidest (Ülesanded, Tööriista annotatsioonid, URL režiimi esiletoomine, Roots)
- **Turvaressursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötoa lingid lisamaterjalidesse

#### Moodul 06 - Kogukonna panused
- **SDK nimekiri**: Lisatud Swift ja Rust SDK-d; uuendatud spetsifikatsiooni link 2025-11-25 versioonile
- **Spetsifikatsiooni viide**: Uuendatud MCP Spetsifikatsiooni link otse spetsifikatsiooni URL-ile

#### Moodul 07 - Varajase kasutuse õppetunnid
- **Ressursi uuendused**: Lisatud MCP Spetsifikatsiooni 2025-11-25 link ja OWASP MCP Top 10 lisamaterjalidesse

#### Moodul 08 - Head tavad
- **Spetsifikatsiooni versioon**: Uuendatud MCP Spetsifikatsiooni viide 2025-11-25 versioonile
- **Turvaressursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötoa lingid lisamaterjalidesse

#### Moodul 10 - AI töövoogude sujuvamaks muutmine
- **Märgi uuendus**: Muudetud MCP versioonimärgis SDK versioonilt (1.9.3) spetsifikatsiooni versioonile (2025-11-25)
- **Ressursside lingid**: Uuendatud MCP Spetsifikatsiooni link; lisatud OWASP MCP Top 10

#### Moodul 11 - MCP serveri praktilised laborid
- **Spetsifikatsiooni viide**: Uuendatud MCP Spetsifikatsiooni link 2025-11-25 versioonile
- **Turvaressursid**: Lisatud OWASP MCP Top 10 ametlikesse ressurssidesse

## 18. detsember 2025
### Turvadokumentatsiooni uuendus – MCP spetsifikatsioon 2025-11-25

#### MCP turvaparemad tavad (02-Security/mcp-best-practices.md) – spetsifikatsiooni versiooni uuendus
- **Protokolli versiooni uuendus**: uuendatud viide uusimale MCP spetsifikatsioonile 2025-11-25 (välja antud 25. novembril 2025)
  - uuendatud kõik spetsifikatsiooni versiooni viited 2025-06-18 pealt 2025-11-25 peale
  - uuendatud dokumendi kuupäeva viited 18. augustilt 2025 18. detsembrile 2025
  - kontrollitud, et kõik spetsifikatsiooni URL-id viitavad praegusele dokumentatsioonile
- **Sisu valideerimine**: turvaparemate tavade põhjalik valideerimine vastavalt uusimatele standarditele
  - **Microsofti turvalahendused**: kontrollitud praeguseid termineid ja linke Prompt Shields’ile (varem "Jailbreak risk detection"), Azure Content Safety’le, Microsoft Entra ID-le ja Azure Key Vaultile
  - **OAuth 2.1 turvalisus**: kinnitatud järjepidevus uusimate OAuth turva parimate tavadega
  - **OWASP standardid**: valideeritud, et OWASP Top 10 LLM-ide kohta viited on endiselt aktuaalsed
  - **Azure teenused**: kontrollitud kõiki Microsoft Azure dokumendi linke ja parimaid tavasid
- **Standardite järgimine**: kõik viidatud turvastandardid on kinnitatud olevat ajakohased
  - NIST AI riskijuhtimise raamistik
  - ISO 27001:2022
  - OAuth 2.1 turvaparemad tavad
  - Azure turva- ja vastavusraamistikud
- **Rakendamise ressursid**: kinnitatud kõik rakendamisjuhiste lingid ja ressursid
  - Azure API Management autentimise mustrid
  - Microsoft Entra ID integratsioonijuhendid
  - Azure Key Vault saladuste haldamine
  - DevSecOps torud ja monitooringulahendused

### Dokumentatsiooni kvaliteedi tagamine
- **Spetsifikatsiooni järgimine**: tagatud, et kõik MCP turvanõuded (PEAB/PEAB MITTE) vastavad uusimale spetsifikatsioonile
- **Ressursside ajakohasus**: kontrollitud kõiki väliseid linke Microsofti dokumentatsioonile, turvastandarditele ja rakendamisjuhistele
- **Parimate tavade katvus**: kinnitatud täielik katvus autentimise, autoriseerimise, AI-spetsiifiliste ohtude, tarneahela turvalisuse ja ettevõtte mustrite osas

## 6. oktoober 2025

### Algaja juhendi jaotise laiendus – täiustatud serveri kasutamine ja lihtne autentimine

#### Täiustatud serveri kasutamine (03-GettingStarted/10-advanced)
- **Lisatud uus peatükk**: detailne juhend täiustatud MCP serveri kasutamise kohta, hõlmates nii tavalist kui madala taseme serveri arhitektuuri.
  - **Tavaline vs madala taseme server**: üksikasjalik võrdlus ja koodinäited Pythonis ja TypeScriptis mõlema lähenemise jaoks.
  - **Handler-põhine disain**: selgitus handler-põhisest tööriista/resurssi/käsu haldusest skaala- ja paindlike serverite rakendustes.
  - **Praktilised mustrid**: reaalsed stsenaariumid, kus madala taseme serveri mustrid võimaldavad täiustatud funktsioone ja arhitektuuri.

#### Lihtne autentimine (03-GettingStarted/11-simple-auth)
- **Lisatud uus peatükk**: samm-sammuline juhend lihtsa autentimise rakendamiseks MCP serverites.
  - **Autentimise mõisted**: selge selgitus autentimise ja autoriseerimise erinevusest ning mandaadihaldusest.
  - **Basic Auth rakendus**: middleware-põhised autentimismustrid Pythonis (Starlette) ja TypeScriptis (Express) koos koodinäidetega.
  - **Tee edasi täiustatud turvalisusse**: juhised lihtsast autentimisest alustamiseks ja edasi liikumiseks OAuth 2.1 ja RBAC kasutusele võtmise suunas, koos viidetega täiendavatele turvalisuse moodulitele.

Need lisad pakuvad praktilisi ja käsikäes juhendeid tugevamate, turvalisemate ja paindlikumate MCP serverite loomisel, ühendades põhikontseptsioonid kõrgema taseme tootmismustritega.

## 29. september 2025

### MCP serveri andmebaasi integreerimise laborid – põhjalik praktiline õppeprogramm

#### 11-MCPServerHandsOnLabs – uus täielik andmebaasi integreerimise õppekava
- **Täielik 13-laboriline õppeprogramm**: lisatud põhjalik praktiline õppekava tootmisvalmis MCP serverite loomise kohta PostgreSQL andmebaasi integratsiooniga
  - **Reaaleluline rakendus**: Zava Retaili analüütika kasutusjuhtum, mis demonstreerib ettevõtte taseme mustreid
  - **Struktureeritud õppeprotsess**:
    - **Laborid 00-03: Alused** – sissejuhatus, tuumikarhitektuur, turvalisus ja mitmeüürlus, keskkonna seadistus
    - **Laborid 04-06: MCP serveri ehitus** – andmebaasi disain ja skeem, MCP serveri rakendamine, tööriistade arendus
    - **Laborid 07-09: Täiustatud funktsioonid** – semantiline otsing, testimine ja silumine, VS Code integratsioon
    - **Laborid 10-12: Tootmine ja parimad tavad** – juurutamisstrateegiad, monitooring ja jälgitavus, parimad tavad ja optimeerimine
  - **Ettevõtte tehnoloogiad**: FastMCP raamistik, PostgreSQL koos pgvectoriga, Azure OpenAI sõnastused, Azure Container Apps, Application Insights
  - **Täiustatud funktsioonid**: reataseme turvalisus (RLS), semantiline otsing, mitme kliendi andmejuurdepääs, vektorsõnastused, reaalajas monitooring

#### Terminoloogia standardiseerimine – mooduli asendamine laboriga
- **Dokumentatsiooni ulatuslik uuendus**: süsteemselt uuendatud kõik 11-MCPServerHandsOnLabs README failid kasutama "Labor" terminoloogiat "Mooduli" asemel
  - **Sektsiooni päised**: uuendatud "What This Module Covers" formaadist "What This Lab Covers" kõigis 13 laboris
  - **Sisu kirjeldus**: muudetud "This module provides..." kujule "This lab provides..." kogu dokumentatsioonis
  - **Õpieesmärgid**: uuendatud "By the end of this module..." kujule "By the end of this lab..."
  - **Navigatsioonilingid**: kõik "Module XX:" viited muudetud kujule "Lab XX:" ristviidetes ja navigeerimises
  - **Lõpetamise jälgimine**: uuendatud "After completing this module..." kujule "After completing this lab..."
  - **Tehnilised viited säilitatud**: Python moodulite viited konfiguratsioonifailides jäävad muutmata (nt `"module": "mcp_server.main"`)

#### Õppejuhendi täiustamine (study_guide.md)
- **Visuaalne õppekava kaart**: lisatud uus sektsioon "11. Database Integration Labs" koos täieliku labori struktuuriga visualiseerituna
- **Varahoidla struktuur**: uuendatud kümnest üheteistkümnele põhiosale koos 11-MCPServerHandsOnLabs põhjaliku kirjeldusega
- **Õppeteekonna juhised**: täiustatud navigeerimise juhised sektsioonide 00-11 katmiseks
- **Tehnoloogia katvus**: lisatud FastMCP, PostgreSQL ja Azure teenuste integratsioonide üksikasjad
- **Õpitulemused**: rõhutatud tootmisvalmis serveri arendus, andmebaasi integreerimise mustrid ja ettevõtte turvalisus

#### Põhidokumentide struktuuri täiustamine
- **Laboripõhine terminoloogia**: uuendatud põhilist README.md faili 11-MCPServerHandsOnLabs kaustas kasutamaks järjepidevalt "Labor" struktuuri
- **Õppeteekonna organiseerimine**: selge edenemine alustaladest täiustatud rakenduste ja tootmistööde suunas
- **Reaalelu rõhuasetus**: rõhutatud praktilist ja käed-külge õppimist ettevõtte taseme mustrite ja tehnoloogiatega

### Dokumentatsiooni kvaliteedi ja järjepidevuse täiustused
- **Praktilise õppimise rõhutamine**: tugevdati praktilist ja laboripõhist lähenemist kogu dokumentatsioonis
- **Ettevõtte mustrite fookus**: esiletõstetud tootmisvalmis rakendused ja ettevõtte turvakaalutlused
- **Tehnoloogia integratsioon**: terviklik katvus kaasaegsete Azure teenuste ja AI integratsioonimustritega
- **Õppeprotsessi edenemine**: selge ja struktureeritud tee alustaladest tootmiseni

## 26. september 2025

### Juhtumiuuringute täiustamine – GitHub MCP registri integratsioon

#### Juhtumiuuringud (09-CaseStudy/) – ökosüsteemi arendamise fookus
- **README.md**: oluline laiendus koos põhjaliku GitHub MCP registri juhtumiuuringuga
  - **GitHub MCP registri juhtumiuuring**: uus põhjalik juhtum, mis analüüsib GitHub MCP registri käivitamist 2025. aasta septembris
    - **Probleemi analüüs**: üksikasjalik ülevaade killustatud MCP serverite avastamise ja juurutamise väljakutsetest
    - **Lahenduse arhitektuur**: GitHubi tsentraliseeritud registri lähenemine ühe klõpsuga VS Code installatsiooniga
    - **Äriline mõju**: mõõdetavad parendused arendajate onboardimisel ja tootlikkuses
    - **Strateegiline väärtus**: rõhuasetus modulaarsele agente juurutamisele ja tööriistadevahelisele koostalitlusele
    - **Ökosüsteemi arendus**: positsioneerimine agentkesksust toetava platvormina
  - **Juhtumiuuringute struktuuri täiustus**: kõik seitse juhtumiuuringut uuendatud järjepideva vormingu ja põhjalike kirjeldustega
    - Azure AI reisiagendid: mitme agendi orkestreerimise fookus
    - Azure DevOps integratsioon: töövoo automatiseerimise rõhuasetus
    - Reaalajas dokumentide päring: Python konsoolikliendi rakendus
    - Interaktiivne õppekava generaator: Chainlit konversatsiooniline veebiäpp
    - Redaktori sees dokumentatsioon: VS Code ja GitHub Copiloti integratsioon
    - Azure API Management: ettevõtte API integratsiooni mustrid
    - GitHub MCP registri ökosüsteemi arendus ja kogukonnaplatform
  - **Põhjalik kokkuvõte**: ümberkirjutatud kokkuvõtte sektsioon, mis rõhutab seitset juhtumiuuringut, mis hõlmavad mitut MCP rakenduse dimensiooni
    - Ettevõtte integratsioon, mitme agendi orkestreerimine, arendaja tootlikkus
    - Ökosüsteemi arendus, hariduslikud rakendused
    - Täiustatud ülevaated arhitektuurimustritest, rakendusstrateegiatest ja tavadest
    - Rõhuasetus MCP-le valminud ja tootmisvalmis protokollina

#### Õppejuhendi uuendused (study_guide.md)
- **Visuaalne õppekava kaart**: uuendatud mõttekaart, millele lisatud GitHub MCP register juhtumiuuringute sektsiooni
- **Juhtumiuuringute kirjeldus**: täiendatud üldistest kirjeldustest üksikasjalikuks seitsme põhjaliku juhtumiuuringu lagundamiseks
- **Varahoidla struktuur**: uuendatud 10. sektsiooni, et kajastada põhjalikku juhtumiuuringute katvust koos konkreetsete rakendusdetailidega
- **Muudatuste nimekiri**: lisatud 26. septembri 2025 sissekanne GitHub MCP registri lisamise ja juhtumiuuringute täiustuste kohta
- **Kuupäeva uuendused**: uuendatud alumise serva ajatempel, et näidata uusimat redaktsiooni (26. september 2025)

### Dokumentatsiooni kvaliteedi täiustused
- **Järjepidevuse tugevdamine**: standardiseeritud juhtumiuuringute vormindus ja struktuur kõigi seitsme näite puhul
- **Põhjalik katvus**: juhtumiuuringud hõlmavad nüüd ettevõtte, arendaja tootlikkuse ja ökosüsteemi arendamise stsenaariume
- **Strateegiline positsioneerimine**: keskendumine MCP-le kui agentkesksuse põhiplatvormile
- **Ressursside integreerimine**: täiendatud lisandväärtusega ressursid, mis sisaldavad GitHub MCP registri linki

## 15. september 2025

### Täiustatud teemade laiendus – kohandatud transpordid ja konteksti inseneriteadus

#### MCP kohandatud transpordid (05-AdvancedTopics/mcp-transport/) – uus täiustatud rakendusjuhend
- **README.md**: täielik juhend kohandatud MCP transpordimehhanismide rakendamiseks
  - **Azure Event Gridi transport**: põhjalik serveriteta sündmustepõhine transpordirakendus
    - näited C#, TypeScript ja Python keeles koos Azure Functionsiga integratsiooniga
    - sündmustepõhised arhitektuurimustrid skaleeritavate MCP lahenduste jaoks
    - webhooki vastuvõtjad ja push-põhine sõnumite töötlemine
  - **Azure Event Hubsi transport**: suure mahutavusega voogedastuse transport
    - reaalaja voogedastuse võimalused madala latentsusega stsenaariumites
    - jaotamise strateegiad ja kontrollpunktide haldamine
    - sõnumite grupeerimine ja jõudluse optimeerimine
  - **Ettevõtte integratsioonimustrid**: tootmisvalmis arhitektuurinäited
    - jaotatud MCP töötlemine mitme Azure Functioni vahel
    - hübriidtransportide arhitektuurid, mis ühendavad mitut transporditüüpi
    - sõnumite vastupidavus, töökindlus ja veahaldusstrateegiad
  - **Turvalisus ja monitooring**: Azure Key Vaulti integratsioon ja jälgitavuse mustrid
    - hallatava identiteedi autentimine ja vähima privileegi juurdepääs
    - Application Insights telemeetria ja jõudluse jälgimine
    - katkestusskeemid (circuit breakers) ja tõrketaluvuse mustrid
  - **Testimismeetodid**: põhjalikud testistrateegiad kohandatud transpordite jaoks
    - üksustestimine testduplikaatide ja mockimise raamistikuga
    - integreerimistestimine Azure Test Containers abil
    - jõudluse ja koormustestimise kaalutlused

#### Konteksti inseneriteadus (05-AdvancedTopics/mcp-contextengineering/) – tekkiv AI eriala
- **README.md**: põhjalik uurimus konteksti inseneriteadusest kui tekkivast valdkonnast
  - **Põhiprintsiibid**: täielik konteksti jagamine, tegevuseotsuste teadlikkus ja konteksti akna haldus
  - **MCP protokolli vastavus**: kuidas MCP disain lahendab konteksti inseneri väljakutseid
    - konteksti akna piirangud ja järkjärguline laadimise strateegiad
    - asjakohasuse hindamine ja dünaamiline konteksti päring
    - multimodaalse konteksti käsitlemine ja turvakaalutlused
  - **Rakenduslähenemised**: üheteljelised vs mitmeagendi arhitektuurid
    - konteksti tükkideks jagamine ja prioriseerimistehnikad
    - järkjärguline konteksti laadimine ja kompresseerimise strateegiad
    - kihiline konteksti käsitlus ja päringu optimeerimine
  - **Mõõtmisk raamistik**: uued mõõdikud konteksti tõhususe hindamiseks
    - sisendi efektiivsus, jõudlus, kvaliteet ja kasutajakogemuse kaalutlused
    - eksperimenti lähenemised konteksti optimeerimiseks
    - läbikukkumise analüüs ja täiustamise metoodikad

#### Õppekava navigeerimise uuendused (README.md)
- **Täiustatud moodulistruktuur**: uuendatud õppekava tabel, lisades uued täiustatud teemad
  - lisatud Context Engineering (5.14) ja Custom Transport (5.15)
  - ühtlane vormistus ja navigeerimislingid kõigis moodulites
  - uuendatud kirjeldused, mis kajastavad hetke sisusisaldust

### Kausta struktuuri täiustused
- **Nime standardiseerimine**: muudetud "mcp transport" nimeks "mcp-transport", et olla ühtlane teiste täiustatud teemade kaustadega
- **Sisu korraldus**: kõik 05-AdvancedTopics kaustad järgivad nüüd vormingut mcp-[teema]

### Dokumentatsiooni kvaliteedi täiustused
- **MCP spetsifikatsiooni vastavus**: kogu uus sisu viitab MCP spetsifikatsioonile 2025-06-18
- **Mitmekeelne näide**: põhjalikud koodinäited C#, TypeScripti ja Pythoni keeltes
- **Ettevõtte fookus**: tootmisvalmis mustrid ja Azure pilveintegreerimine kogu ulatuses
- **Visuaalne dokumentatsioon**: mermaid diagrammid arhitektuuri ja voo visualiseerimiseks

## 18. august 2025

### Dokumentatsiooni põhjalik uuendus – MCP 2025-06-18 standardite järgi

#### MCP turvaparemad tavad (02-Security/) – täielik moderniseerimine
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täielik ümberkirjutus kooskõlas MCP spetsifikatsiooniga 2025-06-18
  - **Kohustuslikud nõuded**: Lisatud selged PEAB/PEAB MITTE nõuded ametlikust spetsifikatsioonist koos visuaalsete indikaatoritega
  - **12 põhiturvalisuse praktikat**: Ümber struktureeritud 15-punktilisest loendist põhjalikeks turva valdkondadeks
    - Määratud turvalisus ja autentimine välishalduse identiteediteenuse integratsiooniga
    - Sessiooni haldus ja transporditurvalisus koos krüptograafiliste nõuetega
    - Tehisintellekti spetsiifiline ohutõrje Microsoft Prompt Shieldsi integreerimisega
    - Juurdepääsukontroll ja õigused põhimõttele "vähima õigusega"
    - Sisu turvalisus ja järelvalve Azure Content Safety integreerimisega
    - Tarneahela turvalisus kõikehõlmava komponentide valideerimisega
    - OAuth turvalisus ja Confused Deputy rünnete tõrje PKCE rakendusega
    - Juhtumite haldus ja taastumine automatiseeritud võimete abil
    - Vastavus ja haldus regulatiivse nõuetega kaasas
    - Täiustatud turvakontrollid nullusaldus arhitektuuriga
    - Microsofti turvasüsteemide integratsioon kõikehõlmavate lahendustega
    - Jätkuv turvalisuse arendus kohanduvate praktikatega
  - **Microsoft turvalahendused**: Täiustatud integratsioonijuhised Prompt Shields, Azure Content Safety, Entra ID ja GitHub Advanced Security jaoks
  - **Rakendamise ressursid**: Kategooriad ametlike MCP dokumentide, Microsoft turvalahenduste, turvastandardite ja rakendamisjuhendite jaoks

#### Täiustatud turvakontrollid (02-Security/) - Ettevõtte rakendamine
- **MCP-SECURITY-CONTROLS-2025.md**: Täielik ümberkujundus ettevõtte taseme turvakontseptsiooniga
  - **9 põhjalikku turva valdkonda**: Laiendatud aluskontrollidest detailse ettevõtte raamistikuni
    - Täiustatud autentimine ja autoriseerimine Microsoft Entra ID integratsiooniga
    - Määratud turvalisus ja anti-passthrough kontrollid põhjaliku valideerimisega
    - Sessiooniturvakontrollid hõivamise tõrjega
    - Tehisintellekti spetsiifilised turvakontrollid prompti süstimise ja tööriistamürgituse vältimiseks
    - Confused Deputy rünnetõrje OAuth proksi turvameetmetega
    - Tööriistade täitmise turvalisus sandboxingu ja isolatsiooniga
    - Tarneahela turvakontrollid sõltuvuste valideerimisega
    - Järelvalve ja tuvastamise kontrollid SIEM integratsiooniga
    - Juhtumite haldus ja taastumine automatiseeritud võimetega
  - **Rakenduse näited**: Lisatud detailseid YAML konfiguratsiooniplokke ja koodinäiteid
  - **Microsofti lahenduste integratsioon**: Kõikehõlmav ülevaade Azure turvateenustest, GitHub Advanced Security'st ja ettevõtte identideedi haldusest

#### Täiustatud teemade turvalisus (05-AdvancedTopics/mcp-security/) - Tootmiskõlblik rakendus
- **README.md**: Täielik ümberkirjutus ettevõtte taseme turvalisuse rakendamiseks
  - **Hetkeseisuga kooskõlas spetsifikatsiooniga**: Uuendatud MCP spetsifikatsioonile 2025-06-18 kohandatud kohustuslike turvanõuetega
  - **Täiustatud autentimine**: Microsoft Entra ID integratsioon koos põhjalike .NET ja Java Spring Security näidetega
  - **Tehisintellekti turbe integratsioon**: Microsoft Prompt Shields ja Azure Content Safety rakendamine detaileeritud Python näidetega
  - **Täiustatud ohtude vähendamine**: Põhjalikud rakendamise näited
    - Confused Deputy rünnete tõrje PKCE ja kasutaja nõusoleku valideerimisega
    - Token passtrough tõkestamine sihtgrupi valideerimise ja turvalise tokeni haldusega
    - Sessioonirünnete tõkestus krüptograafilise sidumise ja käitumusanalüüsiga
  - **Ettevõtte turbe integratsioon**: Azure Application Insights järelvalve, ohtude tuvastamise torustikud ja tarneahela turvalisus
  - **Rakendamise kontrollnimekiri**: Selged kohustuslikud ja soovitatavad turvakontrollid Microsofti turvasüsteemi kasudega

### Dokumentatsiooni kvaliteet ja standardite järgimine
- **Spetsifikatsiooni viited**: Kõik viited ajakohastatud MCP spetsifikatsioonile 2025-06-18
- **Microsofti turvasüsteem**: Täiustatud integreerimisjuhised kõigis turvadokumentides
- **Praktiline rakendamine**: Lisatud üksikasjalikud koodinäited .NET, Java ja Python keeles koos ettevõttelistest mustritest
- **Ressursside organiseerimine**: Põhjalik ametlike dokumentide, turvastandardite ja rakendamisjuhendite kategooria
- **Visuaalsed indikaatorid**: Selge märgistamine kohustuslike nõuete ja soovitatud praktikate vahel


#### Põhikontseptsioonid (01-CoreConcepts/) - Täielik moderniseerimine
- **Protokolli versiooni uuendus**: Uuendatud viited MCP spetsifikatsioonile 2025-06-18 kuupõhise versiooninumbriga (AAAA-KK-PP formaat)
- **Arhitektuuri täpsustus**: Täiustatud selgitused Hostide, Klientide ja Serverite kohta MCP arhitektuuri mustritele vastavalt
  - Hostid nüüd selgelt määratletud kui AI rakendused mitme MCP kliendikonnektsiooni koordineerimiseks
  - Kliendid kirjeldatud protokolli ühendajatena, hoides üks-ühele serveri suhteid
  - Serverid täiustatud lokaalse ja kaugjärgija kasutusstsenaariumite osas
- **Primitiivide ümberkorraldus**: Täielik ülevaatus serveri ja kliendi primitiividest
  - Serveri primitiivid: Ressursid (andmeallikad), Promptid (mallid), Tööriistad (käivitatavad funktsioonid) koos detailsete selgituste ja näidetega
  - Kliendi primitiivid: Valik (LLM täitmised), Esitamine (kasutaja sisend), Logimine (silumine/jälgimine)
  - Uuendatud avastamise (`*/list`), päringu (`*/get`) ja käivituse (`*/call`) meetoditega
- **Protokolli arhitektuur**: Sissejuhatus kahekihilisse arhitektuuri mudelisse
  - Andmekiht: JSON-RPC 2.0 alus koos elutsükli halduse ja primitiividega
  - Transpordikiht: STDIO (kohalik) ja voogedastusega HTTP SSE-ga (kaug) transpordimehhanismid
- **Turvaraamistik**: Põhjalikud turvapõhimõtted, sealhulgas selge kasutaja nõusolek, andmete privaatsuskaitse, tööriistade täitmise ohutus ja transpordikihi turvalisus
- **Kommunikatsioonimustrid**: Uuendatud protokolli sõnumid näitavad initsialiseerimist, avastamist, täitmist ja teavitusi
- **Koodinäited**: Värskendatud mitme keele näited (.NET, Java, Python, JavaScript) vastavalt MCP SDK mustritele

#### Turvalisus (02-Security/) - Kõikehõlmav turva uuendus  
- **Standardite järgimine**: Täielik kooskõla MCP spetsifikatsiooni 2025-06-18 turvanõuetega
- **Autentimise areng**: Dokumenteeritud areng kohandatud OAuth serveritest välishalduse identiteediteenuse delegeerimiseni (Microsoft Entra ID)
- **Tehisintellekti spetsiifiline ohtude analüüs**: Täiustatud kaasaegsete AI rünnakuvektorite käsitlus
  - Detailitud prompti süstimise rünnete stsenaariumid koos rea maailmast pärinevate näidetega
  - Tööriistamürgituse mehhanismid ja "rug pull" rünnakumustrid
  - Konteksti akna mürgitamine ja mudeli segaduse rünnakud
- **Microsoft AI turvalahendused**: Kõikehõlmav ülevaade Microsofti turvasüsteemist
  - AI Prompt Shields koos täiustatud tuvastuse, esiletõstmise ja piiritlejate tehnikatega
  - Azure Content Safety integreerimismustrid
  - GitHub Advanced Security tarneahela kaitseks
- **Täiustatud rünnetõrje**: Detailitud turvakontrollid
  - Sessiooni üle võtmise tõrje MCP-spetsiifiliste stsenaariumitega ja krüptograafilise sessiooni ID nõuetega
  - Confused deputy probleemid MCP proksi stsenaariumides ja selgete nõusolekunõuetega
  - Tokeni passtrough haavatavused kohustuslike valideerimiskontrollidega
- **Tarneahela turvalisus**: Laiendatud AI tarneahela hõlmamine, sealhulgas algmudelid, upseeringuteenused, kontekstipakkujad ja kolmanda osapoole API-d
- **Aluspõhimõtete turvalisus**: Täiustatud integratsioon ettevõtte turvatavadega, sealhulgas nullusaldus arhitektuur ja Microsoft turvasüsteem
- **Ressursside organiseerimine**: Kategooriline kõikehõlmavate ressursilinkide rühmitus (ametlik dokumentatsioon, standardid, teadusuuringud, Microsoft lahendused, rakendamisjuhendid)

### Dokumentatsiooni kvaliteedi parandused
- **Struktureeritud õpieesmärgid**: Täiustatud õppimiseesmärgid konkreetsete ja rakendatavate tulemustega
- **Ristviited**: Lisatud lingid seotud turva ja põhikontseptsioonide teemade vahel
- **Ajakohasus**: Kõik kuupäevad ja spetsifikatsiooni lingid uuendatud vastavalt kaasaegsetele standarditele
- **Rakendamisjuhised**: Lisatud konkreetseid, rakendust toetavaid juhiseid mõlemas osas

## 16. juuli 2025

### README ja navigeerimise täiustused
- Täielikult ümber kujundatud õppekava navigeerimine README.md failis
- Asendatud `<details>` sildid paremini ligipääsetava tabelipõhise vorminguga
- Loodud alternatiivseid paigutusvalikuid uues "alternative_layouts" kaustas
- Lisatud kaardipõhised, tab-stiilis ja akordionilaadsed navigeerimisnäited
- Uuendatud hoidla struktuuri osa viidete lisamisega kõigile viimastele failidele
- Täiustatud "Kuidas seda õppekava kasutada" jaotis selgete soovitustega
- Värskendatud MCP spetsifikatsiooni lingid õigele URL-ile
- Lisatud õppekavasse konteksti inseneringu sektsioon (5.14)

### Õppekava uuendused
- Täielikult ümber kirjutatud õppekava, et sobituda värske hoidla struktuuriga
- Lisatud uued jaotised MCP klientide ja tööriistade kohta ning populaarsetest MCP serveritest
- Uuendatud visuaalne õppekava kaart, mis kajastab ühtselt kõiki teemasid
- Täiustatud täiendavate teemade kirjeldused kõikide spetsialiseeritud valdkondade jaoks
- Värskendatud juhtumiuuringud, mis kajastavad tegelikke näiteid
- Lisatud see põhjalik muudatuste logi

### Kogukonna panused (06-CommunityContributions/)
- Lisatud põhjalikud andmed pildigeneratsiooni MCP serverite kohta
- Lisatud ulatuslik section Claude kasutamisest VSCode'is
- Lisatud Cline terminali kliendi seadistamise ja kasutamise juhised
- Uuendatud MCP kliendiosa, et hõlmata kõiki populaarseid kliendivalikuid
- Täiustatud panusunäited täpsemate koodinäidetega

### Täiustatud teemad (05-AdvancedTopics/)
- Kõigi spetsialiseeritud teema kaustade organiseerimine kooskõlas ühtlase nimetusega
- Lisatud konteksti inseneringu materjalid ja näited
- Lisatud Foundry agent integreerimise dokumentatsioon
- Täiustatud Entra ID turvaintegratsiooni dokumentatsioon

## 11. juuni 2025

### Algne loomine
- Välja antud MCP algajatele õppekava esimene versioon
- Loodud põhiline struktuur kõigile 10 peamisele sektsioonile
- Rakendatud visuaalne õppekava kaart navigeerimiseks
- Lisatud algsed prooviprojektid mitmes programmeerimiskeeles

### Algus (03-GettingStarted/)
- Loodud esimesed serverite rakendamise näited
- Lisatud kliendi arendamise juhised
- Lisatud LLM kliendi integreerimisjuhised
- Lisatud VS Code integreerimisdokumentatsioon
- Rakendatud Server-Sent Events (SSE) serveri näited

### Põhikontseptsioonid (01-CoreConcepts/)
- Lisatud detailne kliendi-serveri arhitektuuri selgitus
- Loodud dokumentatsioon peamistest protokolli komponentidest
- Dokumenteeritud MCP sõnumimustrid

## 23. mai 2025

### Hoidla struktuur
- Algatatud hoidla põhiline kaustastruktuur
- Loodud README failid iga suurema sektsiooni jaoks
- Seadistatud tõlkimise infrastruktuur
- Lisatud pildifailid ja skeemid

### Dokumentatsioon
- Loodud esmane README.md koos õppekava ülevaatega
- Lisatud CODE_OF_CONDUCT.md ja SECURITY.md
- Seadistatud SUPPORT.md juhistega abi saamiseks
- Koostatud esialgne õppejuhend struktuur

## 15. aprill 2025

### Planeerimine ja raamistik
- Esmane planeerimine MCP algajatele õppekava jaoks
- Määratletud õppimiseesmärgid ja sihtrühm
- Kirjeldatud õppekava 10-sektsiooniline struktuur
- Arendatud kontseptuaalne raamistik näidete ja juhtumiuuringute jaoks
- Loodud esialgsed prototüübi näited põhikontseptsioonidest

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada ametlikuks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->