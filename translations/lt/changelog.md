# Pakeitimų žurnalas: MCP pradedantiesiems mokymo programa

Šis dokumentas pateikia visų reikšmingų pakeitimų Model Context Protocol (MCP) pradedantiesiems mokymo programoje įrašus. Pakeitimai dokumentuojami atvirkštine chronologine tvarka (naujausi pakeitimai pirmieji).

## 2026 m. balandžio 11 d.

### Nauja pamoka, dokumentacijos pataisymai ir priklausomybių atnaujinimai

#### Pridėta nauja mokymo programos medžiaga

**Modulis 05 - Pažangios temos**  
- **Pamoka 5.17: Priešinga daugiapakopių agentų samprotavimas su MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Naujas išsamus vadovas apie priešingos diskusijos modelį daugiapakopių agentų sistemoms  
  - Mermaid architektūros diagrama: du agentai → bendras MCP serveris → diskusijos transkripcija → teisėjas → nuosprendis  
  - Bendras MCP įrankių serveris (`web_search` + `run_python`), įgyvendintas Python ir TypeScript kalbomis  
  - Priešinės sistemos pateiktys (UŽ / PRIEŠ / Teisėjas) su aiškiomis įrankių naudojimo sąlygomis  
  - Diskusijų organizatorius Python, TypeScript ir C# kalbomis, valdomas raundų ir argumentų maršrutizavimas  
  - MCP `ClientSession` prijungimas organizatoriaus gyviems įrankių kvietimams  
  - Naudojimo atvejų lentelė (haliucinacijų aptikimas, grėsmių modeliavimas, API dizaino peržiūra, faktų tikrinimas, technologijų pasirinkimas)  
  - Saugumo aspektai: izoliuota vykdymo aplinka, įrankių kvietimų patikra, greičio ribojimas, registravimo auditas  
  - Struktūruota užduotis su trim praktiniais scenarijais (kodo peržiūra, architektūros sprendimai, turinio moderavimas)

#### Dokumentacijos pataisymai

**Modulis 03 - Pradžia**  
- **05-stdio-server/README.md**: Ištaisyta nepilna TypeScript stdio serverio pavyzdžio dalis — pridėtas trūkstamas transporto sukūrimas (`new StdioServerTransport()`) ir `server.connect(transport)` kvietimas, atitinkantis Python ir .NET pavyzdžius toje pačioje dalyje  
- **14-sampling/README.md**: Ištaisyta rašybos klaida — pataisyta `"Sampling is an davanced features"` į `"Sampling is an advanced feature"`

#### Mokymo programos atnaujinimai

**Pagrindinis README.md**  
- Pridėta įrašo 5.17 (Priešinga daugiapakopių agentų samprotavimas su MCP) eilutė su tiesiogine nuoroda į naują pamoką mokymo programos lentelei

**05-AdvancedTopics/README.md**  
- Pridėta pamokos 5.17 eilutė pamokų lentelėje

**study_guide.md**  
- Pridėta Tema „Priešinga daugiapakopių agentų samprotavimas“ į protą žemėlapį ir pažangių temų aprašymą

#### Kodo ir saugumo pataisymai

**Modulis 05 - Priešingi agentai (`mcp-adversarial-agents`)**  
- **Saugumo pataisa – komandų įpurškimo išvengimas**: TypeScript `run_python` įrankyje pakeista `execSync` apvalkalo interpolacija į `execFile` + `promisify`, pašalinant komandų įpurškimo paviršių (dabar LLM valdomas kodas perduodamas kaip tiesioginis argv elementas be apvalkalo)  
- **MCP įrankių ciklo prijungimas**: Atnaujintas Python diskusijų organizatorius, kad naudotų `AsyncAnthropic` klientą (pakeitus sinchroninį `Anthropic`), perduodamas tiesiogiai gyvą `ClientSession` kiekvienam agentei, kiekvieno raundo metu gaunamos įrankių apibrėžtys per `session.list_tools()`, ir vykdomi `tool_use` blokai per `session.call_tool()` ciklą, kol modelis pateikia galutinį tekstinį atsakymą

#### Priklausomybių atnaujinimai

- `hono` atnaujintas iki 4.12.12 daugelyje paketų (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- `@hono/node-server` TypeScript paketuose atnaujintas nuo 1.19.11 iki 1.19.13  
- `cryptography` Python paketuose (10-StreamliningAIWorkflows laboratorijos 3 ir 4) atnaujintas nuo 46.0.5 iki 46.0.7  
- `lodash` atnaujintas nuo 4.17.23 iki 4.18.1 10-StreamliningAIWorkflows inspektoriuje

#### Vertimai

- Sinchronizuoti vertimai daugiau nei 48 kalbomis su naujausiais šaltinio pakeitimais (i18n atnaujinimas)

---

## 2026 m. vasario 5 d.

### Visos saugyklos patikrinimai ir navigacijos patobulinimai

#### Pridėta nauja mokymo programos medžiaga

**Modulis 03 - Pradžia**  
- **12-mcp-hosts/README.md**: Naujas išsamus vadovas apie MCP serverių nustatymą  
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfigūracijos pavyzdžiai  
  - JSON konfigūracijos šablonai visiems pagrindiniams serveriams  
  - Transporto tipų palyginimo lentelė (stdio, SSE/HTTP, WebSocket)  
  - Dažniausiai pasitaikančių ryšio problemų sprendimas  
  - Saugumo geriausios praktikos serverių konfigūracijoje

- **13-mcp-inspector/README.md**: Naujas MCP Inspector derinimo vadovas  
  - Įdiegimo būdai (npx, npm global, iš šaltinio)  
  - Ryšys su serveriais per stdio ir HTTP/SSE  
  - Įrankių, išteklių ir pateikčių testavimo darbo eiga  
  - VS Code integracija su MCP Inspector  
  - Dažniausiai pasitaikančios derinimo situacijos su sprendimais

**Modulis 04 - Praktinis įgyvendinimas**  
- **pagination/README.md**: Naujas vadovas apie puslapiavimą  
  - Žymeklio pagrindu veikiančio puslapiavimo modeliai Python, TypeScript, Java kalbomis  
  - Klientinės puslapiavimo apdorojimas  
  - Žymeklio dizaino strategijos (nepermatomas vs. struktūruotas)  
  - Veikimo optimizavimo rekomendacijos

**Modulis 05 - Pažangios temos**  
- **mcp-protocol-features/README.md**: Nauja protokolo funkcijų išsami analizė  
  - Progreso pranešimų įgyvendinimas  
  - Užklausų atšaukimo modeliai  
  - Išteklių šablonai su URI modeliais  
  - Serverio gyvavimo ciklo valdymas  
  - Registravimo lygių kontrolė  
  - Klaidos apdorojimo modeliai su JSON-RPC kodais

#### Navigacijos pataisymai (atnaujinta 24+ failai)

**Pagrindinių modulių README failai**  
Dabar turi nuorodas tiek į pirmą pamoką, tiek į kitą modulį

**02-Security poskyrio failai**  
Visi 5 papildomi saugumo dokumentai dabar turi „Kas toliau“ navigaciją

**09-CaseStudy failai**  
Visi atvejo tyrimų failai dabar turi sekančią seką navigacijai

**10-StreamliningAI laboratorijos**  
Pridėta „Kas toliau“ skiltis Modulyje 10 ir Module 11 apžvalgose

#### Kodo ir turinio pataisymai

**SDK ir priklausomybių atnaujinimai**  
Ištaisyta tuščia openai versija į `^4.95.0`  
SDK atnaujintas nuo `^1.8.0` iki `>=1.26.0`  
MCP versijos šablonų atnaujinimas iki `>=1.26.0`

**Kodo pataisymai**  
Ištaisyta neteisinga modelio reikšmė `gpt-4o-mini` į `gpt-4.1-mini`

**Turinio pataisymai**  
Ištaisyta sugadinta nuoroda `READMEmd` į `README.md`, pataisytas mokymo programos pavadinimas `Module 1-3` į `Module 0-3`, ištaisyta kelių skirtumo problema  
Pašalinta sugadinta dubliuota Atvejo tyrimo 5 turinio dalis

**Pradedančiųjų gairių patobulinimai**  
Pridėta tinkama įžanga, mokymosi tikslai ir išankstinės žinios pradedantiesiems

#### Mokymo programos atnaujinimai

**Pagrindinis README.md**  
- Pridėti įrašai 3.12 (MCP serveriai), 3.13 (MCP Inspector), 4.1 (Puslapiavimas), 5.16 (Protokolo funkcijos) mokymo programos lentelei

**Modulio README failai**  
Pridėtos pamokos 12 ir 13 pamokų sąraše  
Pridėta skyrius „Praktiniai vadovai“ su nuoroda į puslapiavimą  
Pridėtos pamokos 5.15 (Pasirinktinis transportas) ir 5.16 (Protokolo funkcijos)

**study_guide.md**  
- Atnaujintas protų žemėlapis su visomis naujomis temomis: MCP serverių nustatymas, MCP Inspector, Puslapiavimo strategijos, Protokolo funkcijų išsamus apžvalga

## 2026 m. sausio 28 d.

### MCP specifikacijos 2025-11-25 atitikties peržiūra

#### Pagrindinių sąvokų patobulinimai (01-CoreConcepts/)  
- **Naujas kliento primityvas – Roots**: Pridėta išsami dokumentacija apie Roots kliento primityvą, leidžiantį serveriams suprasti failų sistemos ribas ir prieigos teises  
- **Įrankių anotacijos**: Pridėta dokumentacija apie įrankių elgesio anotacijas (`readOnlyHint`, `destructiveHint`) geresniam įrankių vykdymo sprendimų priėmimui  
- **Įrankių kvietimas atrankoje**: Sampling dokumentacijoje pridėta informacija apie `tools` ir `toolChoice` parametrus modelio paleidžiamų įrankių kvietimui per samplingo užklausas  
- **URL režimo suaktyvinimas**: Pridėta dokumentacija apie URL pagrindu vykdomą serverio inicijuojamą išorinę interneto sąveiką  
- **Užduotys (eksperimentinė funkcija)**: Pridėtas naujas skyrius apie eksperimentinę Užduočių funkciją, skirtą ilgesnio vykdymo apvalkalams ir atidėto rezultato paieškai  
- **Piktogramų palaikymas**: Pažymėta, kad įrankiai, ištekliai, išteklių šablonai ir pateiktinės gali turėti piktogramas kaip papildomą metaduomenį

#### Dokumentacijos atnaujinimai  
- **README.md**: Pridėtas MCP specifikacijos 2025-11-25 versijos nuoroda ir paaiškinimas apie versijavimą pagal datą  
- **study_guide.md**: Atnaujintas mokymo programos žemėlapis, įtraukiantis Užduotis ir Įrankių anotacijas Pagrindinių sąvokų skyriuje; atnaujintas dokumento laiko žymėjimas

#### Specifikacijos atitikties patikra  
- **Protokolo versija**: Patikrinta, kad visa dokumentacija atitinka MCP specifikaciją 2025-11-25  
- **Architektūros suderinamumas**: Patvirtinta, kad dokumentacija tiksliai aprašo dviejų sluoksnių architektūrą (Duomenų sluoksnis + Transporto sluoksnis)  
- **Primityvų dokumentacija**: Patvirtinta serverio primityvų (Ištekliai, Pateiktinės, Įrankiai) ir kliento primityvų (Sampling, Elicitation, Logging, Roots) aprašymo teisingumas  
- **Transporto mechanizmai**: Patikrinta STDIO ir srautinio HTTP transporto dokumentacijos tikslumas  
- **Saugumo gairės**: Patvirtintas atitikimas dabartinėms MCP saugumo gerosioms praktikoms

#### Svarbiausios MCP 2025-11-25 funkcijos dokumentacijoje  
- **OpenID Connect aptikimas**: Autentifikacijos serverio aptikimas per OIDC  
- **OAuth kliento ID metaduomenų dokumentai**: Rekomenduojamas kliento registracijos mechanizmas  
- **JSON Schema 2020-12**: Numatytoji MCP schemų kalba  
- **SDK sluoksnių sistema**: Formalizuoti reikalavimai SDK funkcijų palaikymui ir palaikymui  
- **Valdymo struktūra**: Formalizuoti MCP valdymo darbo grupės ir interesų grupės

### Saugumo dokumentacijos didelis atnaujinimas (02-Security/)

#### MCP saugumo viršūnių konferencijos dirbtuvės (Sherpa) integracija  
- **Naujas praktinis mokymo išteklius**: Pridėta išsami integracija su [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) visuose saugumo dokumentuose  
- **Expedicijos maršruto aprašymas**: Dokumentuotas visas kemperių lauko kampų maršrutas nuo Bazinio stovyklos iki viršūnės  
- **OWASP suderinamumas**: Visa saugumo informacija dabar susieta su OWASP MCP Azure saugumo vadovo rizikomis

#### OWASP MCP Top 10 integracija  
- **Naujasis skyrius**: Pridėta OWASP MCP Top 10 saugumo rizikų lentelė su Azure sprendimų pavyzdžiais pagrindiniame Saugumo README  
- **Rizikomis pagrįsta dokumentacija**: Atnaujinta `mcp-security-controls-2025.md` su OWASP MCP rizikų nuorodomis kiekvienoje saugumo srityje  
- **Nuoroda į architektūrą**: Susieta su OWASP MCP Azure saugumo vadovo atitinkamu architektūros aprašu ir įgyvendinimo modeliais

#### Atnaujinti saugumo failai  
- **README.md**: Pridėta Sherpa dirbtuvių apžvalga, ekspedicijos maršruto lentelė, OWASP MCP Top 10 rizikų santrauka ir praktinio mokymo skyrius  
- **mcp-security-controls-2025.md**: Atnaujintas antraštės datos žymuo į 2026 m. vasarį, pridėtos OWASP rizikų nuorodos (MCP01-MCP08), ištaisyta specifikacijos versijos neatitikimo klaida  
- **mcp-security-best-practices-2025.md**: Pridėtas Sherpa ir OWASP išteklių skyrius, atnaujintas laiko žymėjimas  
- **mcp-best-practices.md**: Pridėtas praktinio mokymo skyrius su Sherpa ir OWASP nuorodomis  
- **azure-content-safety-implementation.md**: Pridėta OWASP MCP06 nuoroda, Sherpa 3 stovyklos suderinamumas ir papildomi ištekliai

#### Pridėtos naujos išteklių nuorodos  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Atskiri OWASP MCP rizikų puslapiai (MCP01-MCP10)

### Visos mokymo programos MCP specifikacijos 2025-11-25 suderinamumas

#### Modulis 03 - Pradžia  
- **SDK dokumentacija**: Pridėta Go SDK į oficialų SDK sąrašą; atnaujintos visos SDK nuorodos, atitinkančios MCP specifikaciją 2025-11-25  
- **Transporto paaiškinimas**: Atnaujinti STDIO ir HTTP srautinio transporto aprašymai su aiškiomis nuorodomis į specifikaciją

#### Modulis 04 - Praktinis įgyvendinimas  
- **SDK atnaujinimai**: Pridėtas Go SDK; SDK sąraše pridėtas specifikacijos versijos nurodymas  
- **Autorizacijos specifikacija**: MCP autorizacijos specifikacijos nuoroda atnaujinta į dabartinę 2025-11-25 versiją

#### Modulis 05 - Pažangios temos  
- **Naujos funkcijos**: Pridėta pastaba apie naujas MCP specifikacijos 2025-11-25 funkcijas (Užduotys, Įrankių anotacijos, URL režimo suaktyvinimas, Roots)  
- **Saugumo ištekliai**: Pridėtos nuorodos į OWASP MCP Top 10 ir Sherpa dirbtuves kaip papildomi ištekliai

#### Modulis 06 - Bendruomenės indėliai  
- **SDK sąrašas**: Pridėti Swift ir Rust SDK; atnaujinta specifikacijos nuoroda į 2025-11-25  
- **Specifikacijos nuoroda**: Atnaujinta MCP specifikacijos nuoroda į tiesioginį specifikacijos URL

#### Modulis 07 - Ankstyvosios diegimo patirtys  
- **Išteklių atnaujinimai**: Pridėta MCP specifikacijos 2025-11-25 ir OWASP MCP Top 10 nuoroda į papildomus išteklius

#### Modulis 08 - Geriausios praktikos  
- **Specifikacijos versija**: Atnaujintas MCP specifikacijos nuorodos numeris į 2025-11-25  
- **Saugumo ištekliai**: Pridėtos nuorodos į OWASP MCP Top 10 ir Sherpa dirbtuves į papildomas nuorodas

#### Modulis 10 - Dirbtinio intelekto darbo srautų supaprastinimas  
- **Ženklo atnaujinimas**: MCP versijos ženklo pakeitimas nuo SDK versijos (1.9.3) į specifikacijos versiją (2025-11-25)  
- **Išteklių nuorodos**: Atnaujinta MCP specifikacijos nuoroda; pridėta OWASP MCP Top 10

#### Modulis 11 - MCP serverio praktinės laboratorijos  
- **Specifikacijos nuoroda**: Atnaujinta MCP specifikacijos nuoroda į 2025-11-25 versiją  
- **Saugumo ištekliai**: Pridėta OWASP MCP Top 10 į oficialius išteklius

## 2025 m. gruodžio 18 d.
### Saugumo dokumentacijos atnaujinimas – MCP specifikacija 2025-11-25

#### MCP saugumo gerosios praktikos (02-Security/mcp-best-practices.md) – specifikacijos versijos atnaujinimas
- **Protokolo versijos atnaujinimas**: atnaujinta nuoroda į naujausią MCP specifikaciją 2025-11-25 (išleista 2025 m. lapkričio 25 d.)
  - Atitinkamai atnaujinti visi specifikacijos versijų nurodymai nuo 2025-06-18 iki 2025-11-25
  - Dokumento datų nuorodos atnaujintos nuo 2025 m. rugpjūčio 18 d. iki 2025 m. gruodžio 18 d.
  - Patikrinta, kad visi specifikacijos URL nuorodos veda į dabartinę dokumentaciją
- **Turinio patvirtinimas**: išsami saugumo gerųjų praktikų patikra pagal naujausius standartus
  - **Microsoft saugumo sprendimai**: patvirtinta dabartinė terminologija ir nuorodos į Prompt Shields (anksčiau „Jailbreak rizikos aptikimas“), Azure Content Safety, Microsoft Entra ID ir Azure Key Vault
  - **OAuth 2.1 saugumas**: patikrinimas, kad atitinka naujausias OAuth saugumo gerąsias praktikas
  - **OWASP standartai**: patvirtinta, kad OWASP Top 10 LLM ataskaitos yra aktualios
  - **Azure paslaugos**: patikrintos visos Microsoft Azure dokumentacijos nuorodos ir gerosios praktikos
- **Standartų atitikimas**: visi nurodyti saugumo standartai patvirtinti kaip galiojantys
  - NIST AI rizikos valdymo karkasas
  - ISO 27001:2022
  - OAuth 2.1 saugumo gerosios praktikos
  - Azure saugumo ir atitikties karkasai
- **Įgyvendinimo ištekliai**: patikrinti visi įgyvendinimo vadovų nuorodos ir ištekliai
  - Azure API valdymo autentifikacijos modeliai
  - Microsoft Entra ID integracijos vadovai
  - Azure Key Vault slaptų duomenų valdymas
  - DevSecOps CI/CD vamzdynai ir monitoringo sprendimai

### Dokumentacijos kokybės užtikrinimas
- **Specifikacijos atitikimas**: užtikrinta, kad visi privalomi MCP saugumo reikalavimai (BŪTINA/NEGALIMA) atitinka naujausią specifikaciją
- **Išteklių aktualumas**: patikrintos visos išorinės nuorodos į Microsoft dokumentaciją, saugumo standartus ir įgyvendinimo vadovus
- **Geriausios praktikos aprėptis**: patvirtintas išsamus autentiškumo, autorizacijos, AI grėsmių, tiekimo grandinės saugumo ir įmonių modelių aprėptis

## 2025 m. spalio 6 d.

### Pradžios skyriaus išplėtimas – pažangus serverio naudojimas ir paprastas autentifikavimas

#### Pažangus serverio naudojimas (03-GettingStarted/10-advanced)
- **Pridėtas naujas skyrius**: pateiktas išsamus vadovas apie pažangų MCP serverio naudojimą, apimantis įprastą ir žemo lygio serverio architektūrą.
  - **Įprastas vs žemo lygio serveris**: išsamus palyginimas ir kodo pavyzdžiai Python ir TypeScript kalbomis abiem metodais.
  - **Handlerio pagrindu grįstas dizainas**: paaiškinimas apie handlerio pagrindu valdomus įrankius/ištekliai/užklausas, leidžiančius kurti skalę ir lanksčius serverius.
  - **Praktinės schemos**: realūs scenarijai, kuriuose žemo lygio serverio modeliai yra naudingi pažangioms funkcijoms ir architektūrai.

#### Paprastas autentifikavimas (03-GettingStarted/11-simple-auth)
- **Pridėtas naujas skyrius**: žingsnis po žingsnio vadovas, kaip įgyvendinti paprastą autentifikavimą MCP serveriuose.
  - **Autentifikacijos sąvokos**: aiškus skirtumas tarp autentifikacijos ir autorizacijos, bei kredencialų valdymas.
  - **Paprastos autentifikacijos įgyvendinimas**: tarpinės programinės įrangos autentifikacijos modeliai Python (Starlette) ir TypeScript (Express) su kodo pavyzdžiais.
  - **Pažangus saugumas**: nurodymai, kaip pradėti nuo paprasto autentifikavimo ir pereiti prie OAuth 2.1 ir RBAC, su nuorodomis į pažangius saugumo modulius.

Šie papildymai suteikia praktiškų, tiesioginių patarimų, kaip sukurti stabilesnius, saugesnius ir lankstesnius MCP serverius, jungiant pagrindines sąvokas su pažangiais gamybos modeliais.

## 2025 m. rugsėjo 29 d.

### MCP serverio duomenų bazės integracijos laboratorijos – išsamus praktinis mokymosi kelias

#### 11-MCPServerHandsOnLabs – nauja išsami duomenų bazės integracijos programa
- **Išsamus 13 laboratorijų mokymosi kelias**: pridėtas išsamus praktinis kursas, skirtas gamybai pasiruošusiems MCP serveriams su PostgreSQL duomenų bazės integracija
  - **Realus įgyvendinimas**: Zava Retail analizės atvejis, demonstruojantis įmonių lygio modelius
  - **Struktūruotas mokymosi progresas**:
    - **Lab 00-03: pagrindai** – įvadas, pagrindinė architektūra, saugumas ir kelių klientų valdymas, aplinkos konfigūravimas
    - **Lab 04-06: MCP serverio kūrimas** – duomenų bazės dizainas ir schema, MCP serverio įgyvendinimas, įrankių kūrimas
    - **Lab 07-09: pažangios funkcijos** – semantinio paieškos integracija, testavimas ir derinimas, VS Code integracija
    - **Lab 10-12: gamyba ir gerosios praktikos** – diegimo strategijos, monitoringo ir stebėjimo sprendimai, geros praktikos ir optimizavimas
  - **Įmonių technologijos**: FastMCP karkasas, PostgreSQL su pgvector, Azure OpenAI įterpimai, Azure konteinerių programėlės, Application Insights
  - **Pažangios funkcijos**: eilučių lygio saugumas (RLS), semantinė paieška, kelių klientų duomenų prieiga, vektoriniai įterpimai, realaus laiko monitoringo sprendimai

#### Terminologijos standartizavimas – modulio keitimas į laboratoriją
- **Išsami dokumentacijos atnaujinimas**: sistemingai atnaujintos visos README bylos 11-MCPServerHandsOnLabs, pakeičiant terminą „Modulis“ į „Laboratorija“
  - **Skyriaus pavadinimai**: „What This Module Covers“ pakeista į „What This Lab Covers“ visuose 13 laboratorijų skyriuose
  - **Turinio aprašymai**: „This module provides...“ pakeista į „This lab provides...“ dokumentacijoje
  - **Mokymosi tikslai**: „By the end of this module...“ pakeista į „By the end of this lab...“
  - **Naršymo nuorodos**: visos „Module XX:“ nuorodos pakeistos į „Lab XX:“ kryžminėse nuorodose ir navigacijoje
  - **Užbaigimo sekimas**: „After completing this module...“ pakeista į „After completing this lab...“
  - **Techniniai terminai išsaugoti**: Python modulio nuorodos konfigūracijos failuose (pvz., `"module": "mcp_server.main"`) nepakitusios

#### Mokymosi vadovo papildymas (study_guide.md)
- **Vizualinė mokymo programa**: pridėtas naujas skyrius „11. Duomenų bazės integracijos laboratorijos“ su išsamia laboratorijų struktūros vizualizacija
- **Saugyklos struktūra**: atnaujinta iš dešimties į vienuolika pagrindinių skyrių su detaliu 11-MCPServerHandsOnLabs aprašymu
- **Mokymosi kelio gairės**: patobulintos naršymo instrukcijos skyriams 00-11
- **Technologijų aprėptis**: pridėta informacija apie FastMCP, PostgreSQL, Azure paslaugų integraciją
- **Mokymosi rezultatai**: pabrėžiamas gamybai pasiruošęs serverių kūrimas, duomenų bazės integracijos modeliai ir įmonių saugumas

#### Pagrindinės README struktūros tobulinimas
- **Laboratorijomis grįsta terminologija**: pagrindinis README.md faile 11-MCPServerHandsOnLabs naudojama nuosekli „Laboratorija“ terminologija
- **Mokymosi kelio organizavimas**: aiškus perėjimas nuo pagrindinių sąvokų iki pažangių įgyvendinimų ir gamybos diegimo
- **Realūs pavyzdžiai**: pabrėžiamas praktinis, rankose atliktamas mokymasis su įmonių lygio modeliais ir technologijomis

### Dokumentacijos kokybės ir nuoseklumo gerinimas
- **Praktinis mokymasis**: sustiprintas laboratorijų pagrindu vykdomas mokymasis visoje dokumentacijoje
- **Įmonių modelių dėmesys**: pabrėžtos gamybai pasiruošusios įgyvendinimo praktikos ir įmonių saugumo aspektai
- **Technologijų integracija**: išsami modernių Azure paslaugų bei AI integracijos modelių aprėptis
- **Mokymosi kelio progresas**: aiškus, struktūruotas kelias nuo pagrindų iki gamybos diegimo

## 2025 m. rugsėjo 26 d.

### Atvejų studijų papildymas – GitHub MCP registrų integracija

#### Atvejų studijos (09-CaseStudy/) – ekosistemos plėtros akcentas
- **README.md**: didelis išplėtimas su išsamiu GitHub MCP registrų atvejo tyrimu
  - **GitHub MCP registrų atvejo tyrimas**: nauja išsami studija apie GitHub MCP registrų paleidimą 2025 m. rugsėjo mėn.
    - **Problemos analizė**: detali išskaidytų MCP serverių aptikimo ir diegimo iššūkių analizė
    - **Sprendimo architektūra**: GitHub centralizuotos registrų sistemos požiūris su vieno paspaudimo VS Code instaliacija
    - **Verslo poveikis**: išmatuojami pagerinimai programuotojų integracijoje ir produktyvume
    - **Strateginė vertė**: dėmesys modulinei agentų diegimo ir tarpįrankių suderinamumo sistemai
    - **Ekosistemos plėtra**: pozicionavimas kaip pagrindinė agentinės integracijos platforma
  - **Išplėsta atvejo studijų struktūra**: atnaujintos visos septynios atvejų studijos su nuosekliais formatavimais ir išsamiais aprašymais
    - Azure AI kelionių agentai: daugiaagentės koordinavimo akcentas
    - Azure DevOps integracija: darbų srautų automatizavimas
    - Realiojo laiko dokumentacijos gavimas: Python konsolės kliento įgyvendinimas
    - Interaktyvus studijų plano generatorius: Chainlit pokalbių žiniatinklio programa
    - Dokumentacija redaktoriuje: VS Code ir GitHub Copilot integracija
    - Azure API valdymas: įmonių API integracijos modeliai
    - GitHub MCP registras: ekosistemos plėtra ir bendruomenės platforma
  - **Išsami išvada**: perrašyta išvada, kuri pabrėžia septynias atvejų studijas, apimančias įvairias MCP įgyvendinimo dimensijas
    - Įmonių integracija, daugiaagentinė koordinacija, programuotojų produktyvumas
    - Ekosistemos plėtra, švietimo taikymas
    - Pagerintos įžvalgos apie architektūros modelius, įgyvendinimo strategijas ir gerąsias praktikas
    - Pabrėžiamas MCP kaip brandžios, gamybai pasiruošusios protokolo reikšmė

#### Mokymosi vadovo atnaujinimai (study_guide.md)
- **Vizualinė mokymo programa**: atnaujintas protmūšio žemėlapis su GitHub MCP registru Atvejų studijų skyriuje
- **Atvejų studijų aprašymai**: patobulinta nuo bendrų iki detalių septynių atvejų studijų apžvalgų
- **Saugyklos struktūra**: atnaujintas 10 skyrius, rodantis išsamią atvejų studijų aprėptį su specifiniais įgyvendinimo detalėmis
- **Pakeitimų žurnalas**: pridėta 2025 m. rugsėjo 26 d. įrašo, apimančio GitHub MCP registrų pridėjimą ir atvejų studijų papildymus
- **Datos atnaujinimai**: apatinio skyriaus laiko žyma atnaujinta į naujausią datą (2025 m. rugsėjo 26 d.)

### Dokumentacijos kokybės gerinimas
- **Nuoseklumo stiprinimas**: standartizuotas atvejų studijų formatas ir struktūra visuose septyniuose pavyzdžiuose
- **Išsami aprėptis**: atvejų studijos apima įmonių, programuotojų produktyvumo ir ekosistemos plėtros scenarijus
- **Strateginis pozicionavimas**: pabrėžta MCP kaip pagrindinė agentinių sistemų diegimo platforma
- **Ištekliai**: papildomi ištekliai atnaujinti su GitHub MCP registrų nuoroda

## 2025 m. rugsėjo 15 d.

### Pažangių temų išplėtimas – pasirinktine transporto ir konteksto inžinerija

#### MCP pasirinktini transportai (05-AdvancedTopics/mcp-transport/) – naujas pažangios įgyvendinimo vadovas
- **README.md**: pilnas pasirinktinių MCP transporto mechanizmų įgyvendinimo vadovas
  - **Azure Event Grid transportas**: išsamus serverless, įvykių pagrindu veikiantis transporto įgyvendinimas
    - C#, TypeScript ir Python pavyzdžiai su Azure Functions integracija
    - Įvykių architektūros modeliai skalėms MCP sprendimams
    - Webhook imtuvai ir įvykių pranešimų tvarkymas push metodu
  - **Azure Event Hubs transportas**: aukšto pralaidumo srautinio perdavimo įgyvendinimas
    - Realios laiko srauto galimybės žemo delsos scenarijams
    - Skirsniavimo strategijos ir kontrolinių taškų valdymas
    - Žinučių paketavimas ir našumo optimizavimas
  - **Įmonių integracijos modeliai**: gamybai pasiruošę architektūriniai pavyzdžiai
    - Paskirstytas MCP apdorojimas per kelias Azure Functions funkcijas
    - Hibridinės transporto architektūros, jungiančios kelis transporto tipus
    - Žinučių patvarumas, patikimumas ir klaidų valdymo strategijos
  - **Saugumas ir monitoringo priemonės**: Azure Key Vault integracija ir stebėjimo modeliai
    - Valdomo identiteto autentifikacija ir mažiausios privilegijos prieiga
    - Application Insights telemetrija ir veikimo monitoringo priemonės
    - Grandinės pertraukikliai ir patvarumo modeliai
  - **Testavimo karkasai**: išsamios pasirinktinių transportų testavimo strategijos
    - Vienetinis testavimas su testiniais dubleriais ir maketavimo karkasais
    - Integracijos testavimas su Azure Test Containers
    - Našumo ir apkrovos testavimo aspektai

#### Konteksto inžinerija (05-AdvancedTopics/mcp-contextengineering/) – nauja atsirandanti AI disciplina
- **README.md**: išsamus konteksto inžinerijos kaip naujos disciplinos tyrimas
  - **Pagrindiniai principai**: visiškas konteksto dalijimasis, veiksmų sprendimų suvokimas ir konteksto lango valdymas
  - **MCP protokolo atitikimas**: kaip MCP dizainas sprendžia konteksto inžinerijos iššūkius
    - Konteksto lango apribojimai ir progresyvaus užkrovimo strategijos
    - Aktualumo nustatymas ir dinaminis konteksto gavimas
    - Daugiamodalinio konteksto tvarkymas ir saugumo aspektai
  - **Įgyvendinimo būdai**: vienos gijos prieš daugiaagentines architektūras
    - Konteksto dalijimosi fragmentavimas ir prioritetizavimo technikos
    - Progresyvus konteksto užkrovimas ir suspaudimo strategijos
    - Sluoksniuotas konteksto požiūris ir optimizavimas gavimui
  - **Matavimo karkasas**: atsirandančios metrikos konteksto efektyvumo vertinimui
    - Įvesties efektyvumas, veikimas, kokybė ir naudotojo patirtis
    - Eksperimentiniai konteksto optimizavimo metodai
    - Nepavykimo analizė ir tobulinimo metodikos

#### Mokymo programos naršymo atnaujinimai (README.md)
- **Patobulinta modulio struktūra**: atnaujinta mokymo programos lentelė, įtraukianti naujas pažangias temas
  - Pridėti įrašai Konteksto inžinerija (5.14) ir Pasirinktinis transportas (5.15)
  - Nuoseklus formatavimas ir navigacijos nuorodos visuose moduliuose
  - Atnaujinti aprašymai, atspindintys dabartinį turinio apimtį

### Katalogo struktūros patobulinimai
- **Pavadinimų standartizavimas**: „mcp transport“ pervadinta į „mcp-transport“ siekiant atitikti kitų pažangių temų aplankų struktūrą
- **Turinio organizavimas**: visi 05-AdvancedTopics aplankai dabar laikosi vienodos pavadinimų schemos (mcp-[tema])

### Dokumentacijos kokybės patobulinimai
- **MCP specifikacijos atitikimas**: visi nauji turiniai nuorodo į dabartinę MCP specifikaciją 2025-06-18
- **Daugiakalbiai pavyzdžiai**: išsamūs kodo pavyzdžiai C#, TypeScript ir Python kalbomis
- **Įmonių dėmesys**: gamybai pasiruošę modeliai ir Azure debesijos integracija visoje dokumentacijoje
- **Vizualinė dokumentacija**: Mermaid diagramos architektūros ir proceso vizualizacijai

## 2025 m. rugpjūčio 18 d.

### Dokumentacijos išsamus atnaujinimas – MCP 2025-06-18 standartai

#### MCP saugumo gerosios praktikos (02-Security/) – visiškas modernizavimas
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Pilnas perrašymas suderintas su MCP Specifikacija 2025-06-18
  - **Privalomi reikalavimai**: Įtraukti aiškūs BŪTINA / NEREIKIA reikalavimai iš oficialios specifikacijos su aiškiais vizualiniais indikatoriais
  - **12 pagrindinių saugumo praktikų**: Pertvarkyta iš 15 punktų sąrašo į išsamias saugumo sritis
    - Žetonų saugumas ir autentifikacija su išorinio tapatybės tiekėjo integracija
    - Seansų valdymas ir transporto saugumas su kriptografiniais reikalavimais
    - AI specifinė grėsmių apsauga su Microsoft Prompt Shields integracija
    - Prieigos kontrolė ir leidimai su principu „mažiausių privilegijų“
    - Turinio sauga ir stebėsena su Azure Content Safety integracija
    - Tiekimo grandinės saugumas su išsamia komponentų patikra
    - OAuth saugumas ir „Confused Deputy“ prevencija su PKCE įgyvendinimu
    - Incidentų valdymas ir atkūrimas su automatizuotomis galimybėmis
    - Atitiktis ir valdymas su reguliavimo reikalavimų laikymusi
    - Išplėstiniai saugumo valdikliai su nulinio pasitikėjimo architektūra
    - Microsoft saugumo ekosistemos integracija su išsamiais sprendimais
    - Nuolatinė saugumo evoliucija su adaptuojamomis praktikomis
  - **Microsoft saugumo sprendimai**: Pagerintos integracijos gairės Prompt Shields, Azure Content Safety, Entra ID ir GitHub Advanced Security
  - **Įgyvendinimo ištekliai**: Išsamiai suskirstyti ištekliai pagal oficialią MCP dokumentaciją, Microsoft saugumo sprendimus, saugumo standartus ir įgyvendinimo gidus

#### Išplėstiniai saugumo valdikliai (02-Security/) - Įmonės lygio įgyvendinimas
- **MCP-SECURITY-CONTROLS-2025.md**: Pilnas perrašymas su įmonės lygio saugumo sistema
  - **9 išsamios saugumo sritys**: Išplėstos iš pagrindinių valdiklių į detalią įmonės saugumo sistemą
    - Išplėstinė autentifikacija ir autorizacija su Microsoft Entra ID integracija
    - Žetonų saugumas ir anti-perdavimo valdikliai su išsamia validacija
    - Seanso saugumo valdikliai su užgrobimo prevencija
    - AI specifiniai saugumo valdikliai su promptų injekcijos ir įrankių apnuodijimo prevencija
    - „Confused Deputy“ atakos prevencija su OAuth tarpinio serverio saugumu
    - Įrankių vykdymo saugumas su izoliacija ir saugiu vykdymu smėlio dėžėje
    - Tiekimo grandinės saugumo valdikliai su priklausomybių tikrinimu
    - Stebėjimo ir aptikimo valdikliai su SIEM integracija
    - Incidentų valdymas ir atkūrimas su automatizuotomis galimybėmis
  - **Įgyvendinimo pavyzdžiai**: Įtraukti išsamūs YAML konfigūracijos blokai ir kodo pavyzdžiai
  - **Microsoft sprendimų integracija**: Išsamus Azure saugumo paslaugų, GitHub Advanced Security ir įmonės tapatybės valdymo aprėptis

#### Išplėtros temos saugumas (05-AdvancedTopics/mcp-security/) - Gamyklinei aplinkai paruoštas įgyvendinimas
- **README.md**: Pilnas perrašymas įmonės lygio saugumo įgyvendinimui
  - **Dabartinės specifikacijos suderinamumas**: Atnaujinta pagal MCP Specifikaciją 2025-06-18 su privalomais saugumo reikalavimais
  - **Patobulinta autentifikacija**: Microsoft Entra ID integracija su išsamiais .NET ir Java Spring Security pavyzdžiais
  - **AI saugumo integracija**: Microsoft Prompt Shields ir Azure Content Safety įgyvendinimas su išsamiais Python pavyzdžiais
  - **Išplėstinė grėsmių mažinimo strategija**: Išsamūs įgyvendinimo pavyzdžiai
    - „Confused Deputy“ atakos prevencija su PKCE ir vartotojo sutikimo validacija
    - Žetonų perdavimo prevencija su auditorijos patikrinimu ir saugiu žetonų valdymu
    - Seanso užgrobimo prevencija su kriptografiniu susiejimu ir elgsenos analize
  - **Įmonės saugumo integracija**: Azure Application Insights stebėsena, grėsmių aptikimo srautai ir tiekimo grandinės saugumas
  - **Įgyvendinimo kontrolinis sąrašas**: Aiškiai nurodomi privalomi ir rekomenduotini saugumo valdikliai su Microsoft saugumo ekosistemos privalumais

### Dokumentacijos kokybė ir standartų suderinamumas
- **Specifikacijų nuorodos**: Atnaujintos visos nuorodos į dabartinę MCP Specifikaciją 2025-06-18
- **Microsoft saugumo ekosistema**: Pagerintos integracijos gairės visoje saugumo dokumentacijoje
- **Praktinis įgyvendinimas**: Įtraukti išsamūs kodo pavyzdžiai .NET, Java ir Python su įmonių modeliais
- **Ištekliai organizacija**: Išsami oficialios dokumentacijos, saugumo standartų ir įgyvendinimo gidų kategorizacija
- **Vizualiniai indikatoriai**: Aiški privalomų reikalavimų ir rekomenduojamų praktikų žyma

#### Pagrindinės sąvokos (01-CoreConcepts/) - Pilnas modernizavimas
- **Protokolo versijos atnaujinimas**: Atnaujinta nuoroda į dabartinę MCP Specifikaciją 2025-06-18 su datos formatu YYYY-MM-DD
- **Architektūros patobulinimai**: Pagerinti aprašymai apie Hosts, Clients ir Servers, atspindintys dabartinius MCP architektūros modelius
  - Hosts dabar aiškiai apibrėžti kaip AI programos, koordinuojančios kelis MCP kliento ryšius
  - Clients aprašyti kaip protokolo jungtys palaikančios vienas prie vieno serverių ryšius
  - Servers patobulinti su vietinės ir nuotolinės diegimo scenarijomis
- **Primitivų pertvarkymas**: Pilnas serverių ir klientų primityvų perrašymas
  - Serverių primityvai: Ištekliai (duomenų šaltiniai), Promptai (šablonai), Įrankiai (vykdomos funkcijos) su išsamiais paaiškinimais ir pavyzdžiais
  - Klientų primityvai: Imtinė analizė (LLM baigtys), Duomenų rinkimas (vartotojo įvestis), Registravimas (naudojimosi ir derinimo stebėsena)
  - Atnaujinti šiuolaikiniai atradimo (`*/list`), gavimo (`*/get`) ir vykdymo (`*/call`) metodų modeliai
- **Protokolo architektūra**: Įvesta dviejų sluoksnių architektūros modelis
  - Duomenų sluoksnis: JSON-RPC 2.0 pagrindas su gyvenimo ciklo valdymu ir primityvais
  - Transporto sluoksnis: STDIO (vietinis) ir streaminamas HTTP su SSE (nuotolinis) transporto mechanizmai
- **Saugumo sistema**: Išsamūs saugumo principai įskaitant aiškų vartotojo sutikimą, duomenų privatumo apsaugą, įrankių vykdymo saugumą ir transporto sluoksnio saugumą
- **Komunikacijos modeliai**: Atnaujinti protokolo pranešimai rodo inicijavimo, atradimo, vykdymo ir pranešimų srautus
- **Kodo pavyzdžiai**: Atjauninti daugialypiai pavyzdžiai (.NET, Java, Python, JavaScript), atspindintys šiuolaikinius MCP SDK modelius

#### Saugumas (02-Security/) - Išsamus saugumo perrašymas
- **Standartų suderinamumas**: Visiškai suderinta su MCP Specifikacijos 2025-06-18 saugumo reikalavimais
- **Autentifikacijos evoliucija**: Dokumentuota evoliucija nuo užsakytinių OAuth serverių iki išorinio tapatybės tiekėjo delegavimo (Microsoft Entra ID)
- **AI specifinė grėsmių analizė**: Pagerintas moderno AI atakų vektorių aprėptis
  - Išsamios promptų injekcijos atakos scenarijos su realiais pavyzdžiais
  - Įrankių apnuodijimo mechanizmai ir „rug pull“ atakų modeliai
  - Konteksto lango apnuodijimas ir modelio painiavos atakos
- **Microsoft AI saugumo sprendimai**: Išsamus Microsoft saugumo ekosistemos aprašymas
  - AI Prompt Shields su pažangiomis aptikimo, pabrėžimo ir delimitavimo technikomis
  - Azure Content Safety integracijos modeliai
  - GitHub Advanced Security tiekimo grandinės apsaugai
- **Išplėstinė grėsmių mažinimo strategija**: Išsamūs saugumo valdikliai
  - Seansų užgrobimo prevencija su MCP specifinėmis atakų situacijomis ir kriptografiniais sesijos ID reikalavimais
  - „Confused Deputy“ problemos MCP tarpininkavimo scenarijuose su aiškiu sutikimu
  - Žetonų perdavimo spragos su privaloma validacija
- **Tiekimo grandinės saugumas**: Išplėstas AI tiekimo grandinės aprėpties aprašymas apimantis pamatines modelių bazes, embeddingų paslaugas, konteksto tiekėjus ir trečiųjų šalių API
- **Pamatinė sauga**: Pagerinta integracija su įmonių saugumo modeliais įskaitant nulinio pasitikėjimo architektūrą ir Microsoft saugumo ekosistemą
- **Ištekliai organizacija**: Išsami išteklių nuorodų kategorizacija pagal tipą (Oficiali dokumentacija, Standartai, Tyrimai, Microsoft sprendimai, Įgyvendinimo gidai)

### Dokumentacijos kokybės patobulinimai
- **Struktūruoti mokymosi tikslai**: Pagerinti mokymosi tikslai su specifiniais ir vykdomais rezultatais
- **Kryžminės nuorodos**: Įtrauktos nuorodos tarp susijusių saugumo ir pagrindinių sąvokų temų
- **Aktuali informacija**: Atnaujintos visos datos ir specifikacijų nuorodos pagal dabartinius standartus
- **Įgyvendinimo gairės**: Įtrauktos konkrečios ir vykdomos įgyvendinimo rekomendacijos abiejuose skirsniuose

## 2025 m. liepos 16 d.

### README ir naršymo patobulinimai
- Pilnai perprojektuotas mokymo programos naršymas README.md faile
- Pakeisti `<details>` žymos į labiau prieinamą lentelės formatą
- Sukurti alternatyvūs išdėstymai naujame „alternative_layouts“ kataloge
- Pridėti kortelių pagrindu, skirtukų ir akordeono tipo naršymo pavyzdžiai
- Atnaujintas saugyklos struktūros skyrius įtraukiant visas naujausias bylas
- Pagerintas skyrius „Kaip naudotis šia mokymo programa“ su aiškiomis rekomendacijomis
- Atnaujintos MCP specifikacijos nuorodos su teisingais URL adresais
- Pridėtas konteksto inžinerijos skyrius (5.14) į mokymo programos struktūrą

### Studijų gidų atnaujinimai
- Pilnai peržiūrėtas studijų gidas sutelkiant dėmesį į dabartinę saugyklos struktūrą
- Pridėti nauji skyriai apie MCP klientus ir įrankius bei populiarius MCP serverius
- Atnaujinta vizualinė mokymo programa atspindinti visas temas
- Papildyta išplėstinių temų aprašymai apimantys visas specializuotas sritis
- Atnaujinta atvejų analizės skyrius su realiais pavyzdžiais
- Pridėtas šis išsamus pakeitimų sąrašas

### Bendruomenės įnašai (06-CommunityContributions/)
- Pridėta išsami informacija apie MCP serverius vaizdų generavimui
- Papildytas skyrius apie Claude naudojimą VSCode aplinkoje
- Pridėti Cline terminalo kliento diegimo ir naudojimo nurodymai
- Atnaujintas MCP klientų skyrius su visomis populiariomis klientų parinktimis
- Pagerinti indėlio pavyzdžiai su tikslesniais kodo šablonais

### Išplėstinės temos (05-AdvancedTopics/)
- Suorganizuotos visos specializuotos temų bylos su nuosekliais pavadinimais
- Pridėti konteksto inžinerijos medžiaga ir pavyzdžiai
- Įtraukta Foundry agentūros integracijos dokumentacija
- Pagerinta Entra ID saugumo integracijos dokumentacija

## 2025 m. birželio 11 d.

### Pradinis sukūrimas
- Išleista pirmoji MCP pradedančiųjų mokymo programos versija
- Sukurta pagrindinė struktūra visiems 10 pagrindiniams skyriams
- Įdiegta vizualinė mokymo programos schema navigacijai
- Įtraukti pradinių pavyzdinių projektų kodai keliomis programavimo kalbomis

### Pradžia (03-GettingStarted/)
- Sukurti pirmieji serverio įgyvendinimo pavyzdžiai
- Pridėtos gairės klientų kūrimui
- Įtraukta LLM kliento integracijos instrukcijos
- Pridėta VS Code integracijos dokumentacija
- Įgyvendinti Server-Sent Events (SSE) serverio pavyzdžiai

### Pagrindinės sąvokos (01-CoreConcepts/)
- Papildyta išsami kliento-serverio architektūros paaiškinimą
- Sukurta dokumentacija apie pagrindinius protokolo komponentus
- Dokumentuoti MCP pranešimų modeliai

## 2025 m. gegužės 23 d.

### Saugyklos struktūra
- Inicializuota saugykla su pagrindine katalogų struktūra
- Sukurtos README bylos kiekvienam svarbiam skyriui
- Įdiegta vertimų infrastruktūra
- Pridėti vaizdų ištekliai ir diagramos

### Dokumentacija
- Sukurtas pradinis README.md su mokymo programos apžvalga
- Įtraukti CODE_OF_CONDUCT.md ir SECURITY.md failai
- Įdiegta SUPPORT.md su pagalbos gavimo gairėmis
- Sukurta preliminari studijų gido struktūra

## 2025 m. balandžio 15 d.

### Planavimas ir sistema
- Pradinis planavimas MCP pradedančiųjų mokymo programai
- Apibrėžti mokymosi tikslai ir tiksline auditorija
- Nubrėžta 10 dalių mokymo programos struktūra
- Sukurtas koncepcinis pagrindas pavyzdžiams ir atvejų analizėms
- Sukurti pradiniai prototipiniai pavyzdžiai pagrindinėms sąvokoms

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ragina**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatizuotos vertimų gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritiniais atvejais rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->