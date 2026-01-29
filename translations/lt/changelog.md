# Pakeitimų žurnalas: MCP pradedantiesiems mokymo programa

Šis dokumentas fiksuoja visus reikšmingus Modelio konteksto protokolo (MCP) pradedantiesiems mokymo programos pakeitimus. Pakeitimai pateikiami atvirkštine chronologine tvarka (naujausi pakeitimai pirmiausia).

## 2025 m. gruodžio 18 d.

### Saugumo dokumentacijos atnaujinimas – MCP specifikacija 2025-11-25

#### MCP saugumo gerosios praktikos (02-Security/mcp-best-practices.md) – specifikacijos versijos atnaujinimas
- **Protokolo versijos atnaujinimas**: atnaujinta nuoroda į naujausią MCP specifikaciją 2025-11-25 (išleista 2025 m. lapkričio 25 d.)
  - Atnaujintos visos specifikacijos versijos nuorodos nuo 2025-06-18 iki 2025-11-25
  - Atnaujintos dokumento datos nuorodos nuo 2025 m. rugpjūčio 18 d. iki 2025 m. gruodžio 18 d.
  - Patikrinta, kad visos specifikacijos URL nuorodos veda į dabartinę dokumentaciją
- **Turinio patikra**: išsami saugumo gerųjų praktikų atitikties naujausiems standartams patikra
  - **Microsoft saugumo sprendimai**: patikrinta dabartinė terminologija ir nuorodos į Prompt Shields (anksčiau „Jailbreak rizikos aptikimas“), Azure Content Safety, Microsoft Entra ID ir Azure Key Vault
  - **OAuth 2.1 saugumas**: patvirtinta atitiktis naujausioms OAuth saugumo gerosioms praktikoms
  - **OWASP standartai**: patikrinta, kad OWASP Top 10 LLM nuorodos yra aktualios
  - **Azure paslaugos**: patikrintos visos Microsoft Azure dokumentacijos nuorodos ir gerosios praktikos
- **Standartų atitiktis**: patvirtinta, kad visi nurodyti saugumo standartai yra aktualūs
  - NIST AI rizikos valdymo sistema
  - ISO 27001:2022
  - OAuth 2.1 saugumo gerosios praktikos
  - Azure saugumo ir atitikties sistemos
- **Įgyvendinimo ištekliai**: patikrintos visos įgyvendinimo vadovų nuorodos ir ištekliai
  - Azure API valdymo autentifikavimo modeliai
  - Microsoft Entra ID integracijos vadovai
  - Azure Key Vault slaptųjų duomenų valdymas
  - DevSecOps vamzdynai ir stebėjimo sprendimai

### Dokumentacijos kokybės užtikrinimas
- **Specifikacijos atitiktis**: užtikrinta, kad visi privalomi MCP saugumo reikalavimai (PRIVALO/PRIVALO NE) atitinka naujausią specifikaciją
- **Išteklių aktualumas**: patikrintos visos išorinės nuorodos į Microsoft dokumentaciją, saugumo standartus ir įgyvendinimo vadovus
- **Geriausių praktikų aprėptis**: patvirtinta išsami autentifikavimo, autorizacijos, AI specifinių grėsmių, tiekimo grandinės saugumo ir įmonių modelių aprėptis

## 2025 m. spalio 6 d.

### Pradžios skyriaus išplėtimas – pažangus serverio naudojimas ir paprasta autentifikacija

#### Pažangus serverio naudojimas (03-GettingStarted/10-advanced)
- **Pridėtas naujas skyrius**: pateiktas išsamus vadovas apie pažangų MCP serverio naudojimą, apimantis tiek įprastą, tiek žemo lygio serverių architektūras.
  - **Įprastas vs žemo lygio serveris**: išsamus palyginimas ir kodo pavyzdžiai Python ir TypeScript abiem požiūriais.
  - **Handler pagrindu sukurta dizaino schema**: paaiškinimas apie įrankių/išteklių/promptų valdymą naudojant handlerius, skirtas mastelio keičiamoms ir lanksčioms serverių įgyvendinimo galimybėms.
  - **Praktiniai modeliai**: realūs scenarijai, kur žemo lygio serverio modeliai naudingi pažangioms funkcijoms ir architektūrai.

#### Paprasta autentifikacija (03-GettingStarted/11-simple-auth)
- **Pridėtas naujas skyrius**: žingsnis po žingsnio vadovas, kaip įgyvendinti paprastą autentifikaciją MCP serveriuose.
  - **Autentifikacijos sąvokos**: aiškus autentifikacijos ir autorizacijos bei kredencialų tvarkymo paaiškinimas.
  - **Paprastos autentifikacijos įgyvendinimas**: tarpinio programinės įrangos (middleware) pagrindu sukurti autentifikacijos modeliai Python (Starlette) ir TypeScript (Express) su kodo pavyzdžiais.
  - **Pažanga į pažangų saugumą**: gairės, kaip pradėti nuo paprastos autentifikacijos ir pereiti prie OAuth 2.1 bei RBAC, su nuorodomis į pažangius saugumo modulius.

Šie papildymai suteikia praktinių, tiesioginių gairių, kaip kurti tvirtesnius, saugesnius ir lankstesnius MCP serverių įgyvendinimus, sujungiant pagrindines sąvokas su pažangiais gamybos modeliais.

## 2025 m. rugsėjo 29 d.

### MCP serverio duomenų bazės integracijos laboratorijos – išsamus praktinis mokymosi kelias

#### 11-MCPServerHandsOnLabs – nauja pilna duomenų bazės integracijos mokymo programa
- **Pilnas 13 laboratorijų mokymosi kelias**: pridėta išsami praktinė mokymo programa MCP serverių kūrimui su PostgreSQL duomenų bazės integracija
  - **Realus įgyvendinimas**: Zava Retail analizės atvejis, demonstruojantis įmonių lygio modelius
  - **Struktūruotas mokymosi progresas**:
    - **Laboratorijos 00-03: pagrindai** – įvadas, pagrindinė architektūra, saugumas ir daugiavartotojiškumas, aplinkos paruošimas
    - **Laboratorijos 04-06: MCP serverio kūrimas** – duomenų bazės dizainas ir schema, MCP serverio įgyvendinimas, įrankių kūrimas
    - **Laboratorijos 07-09: pažangios funkcijos** – semantinės paieškos integracija, testavimas ir derinimas, VS Code integracija
    - **Laboratorijos 10-12: gamyba ir gerosios praktikos** – diegimo strategijos, stebėjimas ir stebėsenos galimybės, gerosios praktikos ir optimizavimas
  - **Įmonių technologijos**: FastMCP karkasas, PostgreSQL su pgvector, Azure OpenAI įterpimai, Azure Container Apps, Application Insights
  - **Pažangios funkcijos**: eilutės lygio saugumas (RLS), semantinė paieška, daugiavartotojiškas duomenų prieigos valdymas, vektoriniai įterpimai, realaus laiko stebėjimas

#### Terminologijos standartizavimas – modulio keitimas į laboratoriją
- **Išsami dokumentacijos atnaujinimas**: sistemingai atnaujinti visi README failai 11-MCPServerHandsOnLabs, kad būtų naudojama „Laboratorija“ vietoje „Modulis“
  - **Skyriaus antraštės**: pakeista „What This Module Covers“ į „What This Lab Covers“ visuose 13 laboratorijų aprašymuose
  - **Turinio aprašymas**: pakeista „This module provides...“ į „This lab provides...“ visoje dokumentacijoje
  - **Mokymosi tikslai**: atnaujinta „By the end of this module...“ į „By the end of this lab...“
  - **Navigacijos nuorodos**: visos „Module XX:“ nuorodos pakeistos į „Lab XX:“ kryžminėse nuorodose ir navigacijoje
  - **Užbaigimo sekimas**: atnaujinta „After completing this module...“ į „After completing this lab...“
  - **Išsaugotos techninės nuorodos**: išlaikyti Python modulio pavadinimai konfigūracijos failuose (pvz., `"module": "mcp_server.main"`)

#### Studijų vadovo patobulinimas (study_guide.md)
- **Vizualinė mokymo programos schema**: pridėtas naujas skyrius „11. Duomenų bazės integracijos laboratorijos“ su išsamia laboratorijų struktūros vizualizacija
- **Saugyklos struktūra**: atnaujinta nuo dešimties iki vienuolikos pagrindinių skyrių su detaliu 11-MCPServerHandsOnLabs aprašymu
- **Mokymosi kelio gairės**: patobulintos navigacijos instrukcijos, apimančios skyrius 00-11
- **Technologijų aprėptis**: pridėta FastMCP, PostgreSQL, Azure paslaugų integracijos informacija
- **Mokymosi rezultatai**: pabrėžtas gamybai paruošto serverio kūrimas, duomenų bazės integracijos modeliai ir įmonių saugumas

#### Pagrindinio README struktūros patobulinimas
- **Laboratorijų terminologija**: pagrindiniame 11-MCPServerHandsOnLabs README.md nuosekliai naudojama „Laboratorijos“ struktūra
- **Mokymosi kelio organizavimas**: aiškus progresas nuo pagrindinių sąvokų iki pažangaus įgyvendinimo ir gamybos diegimo
- **Realus dėmesys**: pabrėžiamas praktinis, tiesioginis mokymasis su įmonių lygio modeliais ir technologijomis

### Dokumentacijos kokybės ir nuoseklumo gerinimas
- **Praktinio mokymosi akcentas**: sustiprintas praktinis, laboratorijomis pagrįstas požiūris visoje dokumentacijoje
- **Įmonių modelių dėmesys**: pabrėžti gamybai paruošti įgyvendinimai ir įmonių saugumo aspektai
- **Technologijų integracija**: išsami šiuolaikinių Azure paslaugų ir AI integracijos modelių aprėptis
- **Mokymosi progresas**: aiškus, struktūruotas kelias nuo pagrindinių sąvokų iki gamybos diegimo

## 2025 m. rugsėjo 26 d.

### Atvejų studijų patobulinimas – GitHub MCP registro integracija

#### Atvejų studijos (09-CaseStudy/) – ekosistemos plėtros dėmesys
- **README.md**: didelis išplėtimas su išsamiu GitHub MCP registro atvejo studija
  - **GitHub MCP registro atvejo studija**: nauja išsami atvejo studija, nagrinėjanti GitHub MCP registro paleidimą 2025 m. rugsėjį
    - **Problemos analizė**: išsamus MCP serverių atradimo ir diegimo iššūkių nagrinėjimas
    - **Sprendimo architektūra**: GitHub centralizuoto registro požiūris su vieno spustelėjimo VS Code diegimu
    - **Verslo poveikis**: matomi pagerėjimai kūrėjų įsitraukime ir produktyvume
    - **Strateginė vertė**: dėmesys modulinei agentų diegimo sistemai ir įrankių tarpusavio sąveikai
    - **Ekosistemos plėtra**: pozicionavimas kaip pagrindinė platforma agentų integracijai
  - **Patobulinta atvejo studijų struktūra**: atnaujintos visos septynios atvejo studijos su nuoseklia formatu ir išsamiais aprašymais
    - Azure AI kelionių agentai: daugiaagentinė orkestracija
    - Azure DevOps integracija: darbo eigos automatizavimas
    - Realaus laiko dokumentacijos gavimas: Python konsolės klientas
    - Interaktyvus studijų plano generatorius: Chainlit pokalbių žiniatinklio programa
    - Redaktoriaus viduje esanti dokumentacija: VS Code ir GitHub Copilot integracija
    - Azure API valdymas: įmonių API integracijos modeliai
    - GitHub MCP registras: ekosistemos plėtra ir bendruomenės platforma
  - **Išsami išvada**: perrašyta išvados dalis, pabrėžianti septynias atvejo studijas, apimančias kelis MCP įgyvendinimo aspektus
    - Įmonių integracija, daugiaagentinė orkestracija, kūrėjų produktyvumas
    - Ekosistemos plėtra, švietimo taikymas
    - Patobulintos įžvalgos apie architektūrinius modelius, įgyvendinimo strategijas ir gerąsias praktikas
    - Pabrėžiamas MCP kaip brandus, gamybai paruoštas protokolas

#### Studijų vadovo atnaujinimai (study_guide.md)
- **Vizualinė mokymo programos schema**: atnaujintas minčių žemėlapis, įtraukiant GitHub MCP registrą į atvejo studijų skyrių
- **Atvejo studijų aprašymas**: patobulintas nuo bendrų aprašymų iki detalaus septynių išsamių atvejo studijų suskirstymo
- **Saugyklos struktūra**: atnaujintas skyrius 10, atspindintis išsamią atvejo studijų aprėptį su konkrečiomis įgyvendinimo detalėmis
- **Pakeitimų žurnalo integracija**: pridėtas 2025 m. rugsėjo 26 d. įrašas, dokumentuojantis GitHub MCP registro pridėjimą ir atvejo studijų patobulinimus
- **Datos atnaujinimai**: atnaujintas poraštės laiko žymėjimas, atspindintis naujausią peržiūrą (2025 m. rugsėjo 26 d.)

### Dokumentacijos kokybės gerinimas
- **Nuoseklumo stiprinimas**: standartizuotas atvejo studijų formatas ir struktūra visuose septyniuose pavyzdžiuose
- **Išsami aprėptis**: atvejo studijos apima įmonių, kūrėjų produktyvumo ir ekosistemos plėtros scenarijus
- **Strateginis pozicionavimas**: sustiprintas dėmesys MCP kaip pagrindinei agentinių sistemų diegimo platformai
- **Išteklių integracija**: atnaujinti papildomi ištekliai, įtraukiant GitHub MCP registro nuorodą

## 2025 m. rugsėjo 15 d.

### Pažangių temų išplėtimas – individualūs transportai ir konteksto inžinerija

#### MCP individualūs transportai (05-AdvancedTopics/mcp-transport/) – naujas pažangus įgyvendinimo vadovas
- **README.md**: pilnas individualių MCP transporto mechanizmų įgyvendinimo vadovas
  - **Azure Event Grid transportas**: išsamus serverless įvykių valdomo transporto įgyvendinimas
    - C#, TypeScript ir Python pavyzdžiai su Azure Functions integracija
    - Įvykių valdomos architektūros modeliai mastelio keičiamoms MCP sprendimams
    - Webhook gavėjai ir pranešimų siuntimo mechanizmai
  - **Azure Event Hubs transportas**: didelio pralaidumo srautinio transporto įgyvendinimas
    - Realaus laiko srautinės perdavimo galimybės mažo delsos scenarijams
    - Skirsnių valdymo strategijos ir kontrolinių taškų valdymas
    - Pranešimų grupavimas ir našumo optimizavimas
  - **Įmonių integracijos modeliai**: gamybai paruošti architektūriniai pavyzdžiai
    - Paskirstytas MCP apdorojimas per kelias Azure Functions
    - Hibridinės transporto architektūros, derinančios kelis transporto tipus
    - Pranešimų patvarumo, patikimumo ir klaidų valdymo strategijos
  - **Saugumas ir stebėjimas**: Azure Key Vault integracija ir stebėjimo modeliai
    - Valdomos tapatybės autentifikacija ir mažiausių privilegijų prieiga
    - Application Insights telemetrija ir našumo stebėjimas
    - Grandinės pertraukikliai ir gedimų tolerancijos modeliai
  - **Testavimo sistemos**: išsamios testavimo strategijos individualiems transportams
    - Vienetinis testavimas su testų dubleriais ir imitavimo sistemomis
    - Integracinis testavimas su Azure Test Containers
    - Našumo ir apkrovos testavimo aspektai

#### Konteksto inžinerija (05-AdvancedTopics/mcp-contextengineering/) – nauja besiformuojanti AI disciplina
- **README.md**: išsami konteksto inžinerijos kaip besiformuojančios srities apžvalga
  - **Pagrindinės principai**: pilnas konteksto dalijimasis, veiksmų sprendimų suvokimas ir konteksto lango valdymas
  - **MCP protokolo atitiktis**: kaip MCP dizainas sprendžia konteksto inžinerijos iššūkius
    - Konteksto lango apribojimai ir progresyvaus užkrovimo strategijos
    - Reikšmingumo nustatymas ir dinaminis konteksto gavimas
    - Daugiarūšio konteksto valdymas ir saugumo aspektai
  - **Įgyvendinimo metodai**: vienos gijos prieš daugiaagentines architektūras
    - Konteksto dalijimas į dalis ir prioritetų nustatymo technikos
    - Progresyvus konteksto užkrovimas ir suspaudimo strategijos
    - Sluoksniuoto konteksto metodai ir gavimo optimizavimas
  - **Matuoklių sistema**: nauji metrikos rodikliai konteksto efektyvumo vertinimui
    - Įvesties efektyvumas, našumas, kokybė ir naudotojo patirtis
    - Eksperimentiniai konteksto optimizavimo metodai
    - Gedimų analizė ir tobulinimo metodologijos

#### Mokymo programos navigacijos atnaujinimai (README.md)
- **Patobulinta modulio struktūra**: atnaujinta mokymo programos lentelė, įtraukiant naujas pažangias temas
  - Pridėti įrašai apie Konteksto inžineriją (5.14) ir Individualų transportą (5.15)
  - Nuoseklus formatavimas ir navigacijos nuorodos visuose moduliuose
  - Atnaujinti aprašymai, atspindintys dabartinį turinio apimtį

### Aplanko struktūros patobulinimai
- **Pavadinimų standartizavimas**: „mcp transport“ pervadintas į „mcp-transport“ siekiant nuoseklumo su kitais pažangių temų aplankais
- **Turinio organizavimas**: visi 05-AdvancedTopics aplankai dabar laikosi nuoseklaus pavadinimų modelio (mcp-[tema])

### Dokumentacijos kokybės gerinimas
- **MCP specifikacijos atitiktis**: visas naujas turinys nurodo dabartinę MCP specifikaciją 2025-06-18
- **Daugiakalbiai pavyzdžiai**: išsamūs kodo pavyzdžiai C#, TypeScript ir Python kalbomis
- **Įmonių dėmesys**: gamybai paruošti modeliai ir Azure debesų integracija visame turinyje
- **Vizualinė dokumentacija**: Mermaid diagramos architektūros ir srautų vizualizacijai

## 2025 m. rugpjūčio 18 d.

### Dokumentacijos išsamus atnaujinimas – MCP 2025-06-18 standartai

#### MCP saugumo gerosios praktikos (02-Security/) – visiškas modernizavimas
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: visiškas perrašymas, suderintas su MCP specifikacija 2025-06-18
  - **Privalomi reikalavimai**: Pridėti aiškūs PRIVALOMA/NEPRIVALOMA reikalavimai iš oficialios specifikacijos su aiškiais vizualiniais indikatoriais
  - **12 pagrindinių saugumo praktikų**: Pertvarkyta iš 15 punktų sąrašo į išsamias saugumo sritis
    - Žetonų saugumas ir autentifikacija su išorinio tapatybės teikėjo integracija
    - Sesijos valdymas ir transporto saugumas su kriptografiniais reikalavimais
    - AI specifinė grėsmių apsauga su Microsoft Prompt Shields integracija
    - Prieigos kontrolė ir leidimai pagal mažiausios privilegijos principą
    - Turinys saugumas ir stebėsena su Azure Content Safety integracija
    - Tiekimo grandinės saugumas su išsamiu komponentų patikrinimu
    - OAuth saugumas ir painiavos prevencija su PKCE įgyvendinimu
    - Incidentų valdymas ir atkūrimas su automatizuotomis galimybėmis
    - Atitiktis ir valdymas su reguliavimo reikalavimų suderinamumu
    - Pažangios saugumo kontrolės su zero trust architektūra
    - Microsoft saugumo ekosistemos integracija su išsamiais sprendimais
    - Nuolatinė saugumo evoliucija su adaptuojamomis praktikomis
  - **Microsoft saugumo sprendimai**: Patobulintos integracijos gairės Prompt Shields, Azure Content Safety, Entra ID ir GitHub Advanced Security
  - **Įgyvendinimo ištekliai**: Išsamūs išteklių nuorodų kategorijų suskirstymai pagal oficialią MCP dokumentaciją, Microsoft saugumo sprendimus, saugumo standartus ir įgyvendinimo vadovus

#### Pažangios saugumo kontrolės (02-Security/) - Įmonių įgyvendinimas
- **MCP-SECURITY-CONTROLS-2025.md**: Viso perrašymo versija su įmonių lygio saugumo sistema
  - **9 išsamios saugumo sritys**: Išplėsta nuo pagrindinių kontrolės priemonių iki detalaus įmonių lygio sistemos
    - Pažangi autentifikacija ir autorizacija su Microsoft Entra ID integracija
    - Žetonų saugumas ir anti-praėjimo kontrolės su išsamia validacija
    - Sesijos saugumo kontrolės su užgrobimo prevencija
    - AI specifinės saugumo kontrolės su promptų injekcijos ir įrankių užnuodijimo prevencija
    - Painiavos prevencija su OAuth proxy saugumu
    - Įrankių vykdymo saugumas su sandbox ir izoliacija
    - Tiekimo grandinės saugumo kontrolės su priklausomybių patikrinimu
    - Stebėjimo ir aptikimo kontrolės su SIEM integracija
    - Incidentų valdymas ir atkūrimas su automatizuotomis galimybėmis
  - **Įgyvendinimo pavyzdžiai**: Pridėti išsamūs YAML konfigūracijos blokai ir kodo pavyzdžiai
  - **Microsoft sprendimų integracija**: Išsamus Azure saugumo paslaugų, GitHub Advanced Security ir įmonių tapatybės valdymo aprėptis

#### Pažangios temos saugumas (05-AdvancedTopics/mcp-security/) - Produkcijai paruoštas įgyvendinimas
- **README.md**: Viso perrašymo versija įmonių saugumo įgyvendinimui
  - **Dabartinės specifikacijos suderinamumas**: Atnaujinta pagal MCP specifikaciją 2025-06-18 su privalomais saugumo reikalavimais
  - **Patobulinta autentifikacija**: Microsoft Entra ID integracija su išsamiais .NET ir Java Spring Security pavyzdžiais
  - **AI saugumo integracija**: Microsoft Prompt Shields ir Azure Content Safety įgyvendinimas su išsamiais Python pavyzdžiais
  - **Pažangi grėsmių mažinimo priemonė**: Išsamūs įgyvendinimo pavyzdžiai
    - Painiavos prevencija su PKCE ir vartotojo sutikimo validacija
    - Žetonų praėjimo prevencija su auditorijos validacija ir saugiu žetonų valdymu
    - Sesijos užgrobimo prevencija su kriptografiniu susiejimu ir elgsenos analize
  - **Įmonių saugumo integracija**: Azure Application Insights stebėsena, grėsmių aptikimo vamzdynai ir tiekimo grandinės saugumas
  - **Įgyvendinimo kontrolinis sąrašas**: Aiškus privalomų ir rekomenduojamų saugumo kontrolės priemonių atskyrimas su Microsoft saugumo ekosistemos privalumais

### Dokumentacijos kokybė ir standartų suderinamumas
- **Specifikacijos nuorodos**: Atnaujintos visos nuorodos į dabartinę MCP specifikaciją 2025-06-18
- **Microsoft saugumo ekosistema**: Patobulintos integracijos gairės visoje saugumo dokumentacijoje
- **Praktinis įgyvendinimas**: Pridėti išsamūs kodo pavyzdžiai .NET, Java ir Python su įmonių modeliais
- **Išteklių organizavimas**: Išsamus oficialios dokumentacijos, saugumo standartų ir įgyvendinimo vadovų suskirstymas
- **Vizualiniai indikatoriai**: Aiškus privalomų reikalavimų ir rekomenduojamų praktikų žymėjimas


#### Pagrindinės sąvokos (01-CoreConcepts/) - Viso modernizavimo versija
- **Protokolo versijos atnaujinimas**: Atnaujinta nuoroda į dabartinę MCP specifikaciją 2025-06-18 su datos formatu (YYYY-MM-DD)
- **Architektūros patobulinimas**: Patobulinti aprašymai apie šeimininkus, klientus ir serverius, atspindintys dabartinius MCP architektūros modelius
  - Šeimininkai dabar aiškiai apibrėžti kaip AI programos, koordinuojančios kelis MCP klientų ryšius
  - Klientai aprašyti kaip protokolo jungtys, palaikančios vienas prie vieno serverio ryšius
  - Serveriai patobulinti su vietinio ir nuotolinio diegimo scenarijais
- **Primitivų pertvarkymas**: Viso perrašymo versija serverio ir kliento primityvų
  - Serverio primityvai: Ištekliai (duomenų šaltiniai), Promptai (šablonai), Įrankiai (vykdomos funkcijos) su išsamiais paaiškinimais ir pavyzdžiais
  - Kliento primityvai: Atranka (LLM užbaigimai), Išgavimas (vartotojo įvestis), Registravimas (derinimas/stebėsena)
  - Atnaujinta su dabartiniais atradimo (`*/list`), gavimo (`*/get`) ir vykdymo (`*/call`) metodų modeliais
- **Protokolo architektūra**: Įvesta dviejų sluoksnių architektūros modelis
  - Duomenų sluoksnis: JSON-RPC 2.0 pagrindas su gyvavimo ciklo valdymu ir primityvais
  - Transporto sluoksnis: STDIO (vietinis) ir Streamable HTTP su SSE (nuotolinis) transporto mechanizmai
- **Saugumo sistema**: Išsamūs saugumo principai, įskaitant aiškų vartotojo sutikimą, duomenų privatumo apsaugą, įrankių vykdymo saugumą ir transporto sluoksnio saugumą
- **Komunikacijos modeliai**: Atnaujinti protokolo pranešimai, rodantys inicializavimo, atradimo, vykdymo ir pranešimų srautus
- **Kodo pavyzdžiai**: Atnaujinti daugiakalbiai pavyzdžiai (.NET, Java, Python, JavaScript), atspindintys dabartinius MCP SDK modelius

#### Saugumas (02-Security/) - Išsamus saugumo perrašymas  
- **Standartų suderinamumas**: Pilnas suderinamumas su MCP specifikacijos 2025-06-18 saugumo reikalavimais
- **Autentifikacijos evoliucija**: Dokumentuota evoliucija nuo pasirinktinių OAuth serverių iki išorinio tapatybės teikėjo delegavimo (Microsoft Entra ID)
- **AI specifinė grėsmių analizė**: Patobulintas šiuolaikinių AI atakų vektorių aprėptis
  - Išsamios promptų injekcijos atakų scenarijai su realiais pavyzdžiais
  - Įrankių užnuodijimo mechanizmai ir „rug pull“ atakų modeliai
  - Konteksto lango užnuodijimas ir modelio painiavos atakos
- **Microsoft AI saugumo sprendimai**: Išsamus Microsoft saugumo ekosistemos aprėptis
  - AI Prompt Shields su pažangia aptikimo, išryškinimo ir ribojimo technikomis
  - Azure Content Safety integracijos modeliai
  - GitHub Advanced Security tiekimo grandinės apsaugai
- **Pažangi grėsmių mažinimo priemonė**: Išsamios saugumo kontrolės
  - Sesijos užgrobimas su MCP specifiniais atakų scenarijais ir kriptografiniais sesijos ID reikalavimais
  - Painiavos problemos MCP proxy scenarijuose su aiškiais sutikimo reikalavimais
  - Žetonų praėjimo pažeidžiamumai su privalomomis validacijos kontrolėmis
- **Tiekimo grandinės saugumas**: Išplėsta AI tiekimo grandinės aprėptis, įskaitant pagrindinius modelius, įterpimo paslaugas, konteksto tiekėjus ir trečiųjų šalių API
- **Pagrindų saugumas**: Patobulinta integracija su įmonių saugumo modeliais, įskaitant zero trust architektūrą ir Microsoft saugumo ekosistemą
- **Išteklių organizavimas**: Išsamus išteklių nuorodų suskirstymas pagal tipą (Oficiali dokumentacija, standartai, tyrimai, Microsoft sprendimai, įgyvendinimo vadovai)

### Dokumentacijos kokybės patobulinimai
- **Struktūruoti mokymosi tikslai**: Patobulinti mokymosi tikslai su konkrečiais, veiksmingais rezultatais
- **Kryžminės nuorodos**: Pridėtos nuorodos tarp susijusių saugumo ir pagrindinių sąvokų temų
- **Dabartinė informacija**: Atnaujintos visos datos nuorodos ir specifikacijų saitai į dabartinius standartus
- **Įgyvendinimo gairės**: Pridėtos konkrečios, veiksmingos įgyvendinimo rekomendacijos abiejose skiltyse

## 2025 m. liepos 16 d.

### README ir navigacijos patobulinimai
- Viso perprojektuota mokymo plano navigacija README.md faile
- Pakeisti `<details>` žymės į labiau prieinamą lentelės formatą
- Sukurtos alternatyvios išdėstymo parinktys naujame „alternative_layouts“ kataloge
- Pridėti kortelių, skirtukų ir akordeono stiliaus navigacijos pavyzdžiai
- Atnaujinta saugyklos struktūros dalis, įtraukiant visus naujausius failus
- Patobulinta „Kaip naudotis šiuo mokymo planu“ dalis su aiškiomis rekomendacijomis
- Atnaujintos MCP specifikacijos nuorodos į teisingus URL
- Pridėta konteksto inžinerijos dalis (5.14) mokymo plano struktūroje

### Studijų vadovo atnaujinimai
- Viso perrašytas studijų vadovas, suderintas su dabartine saugyklos struktūra
- Pridėtos naujos skiltys MCP klientams ir įrankiams bei populiariems MCP serveriams
- Atnaujinta vizualinė mokymo plano schema, tiksliai atspindinti visas temas
- Patobulinti pažangių temų aprašymai, apimantys visas specializuotas sritis
- Atnaujinta atvejų studijų dalis, atspindinti tikrus pavyzdžius
- Pridėtas šis išsamus pakeitimų žurnalas

### Bendruomenės indėliai (06-CommunityContributions/)
- Pridėta išsami informacija apie MCP serverius vaizdų generavimui
- Pridėta išsami skiltis apie Claude naudojimą VSCode aplinkoje
- Pridėta Cline terminalo kliento nustatymo ir naudojimo instrukcijos
- Atnaujinta MCP klientų skiltis, įtraukiant visas populiarias klientų parinktis
- Patobulinti indėlių pavyzdžiai su tikslesniais kodo pavyzdžiais

### Pažangios temos (05-AdvancedTopics/)
- Suorganizuoti visi specializuoti temų katalogai su nuosekliais pavadinimais
- Pridėti konteksto inžinerijos medžiaga ir pavyzdžiai
- Pridėta Foundry agento integracijos dokumentacija
- Patobulinta Entra ID saugumo integracijos dokumentacija

## 2025 m. birželio 11 d.

### Pradinis sukūrimas
- Išleista pirmoji MCP pradedantiesiems mokymo plano versija
- Sukurta pagrindinė visų 10 pagrindinių skyrių struktūra
- Įgyvendinta vizualinė mokymo plano schema navigacijai
- Pridėti pradiniai pavyzdiniai projektai keliomis programavimo kalbomis

### Pradžia (03-GettingStarted/)
- Sukurti pirmieji serverio įgyvendinimo pavyzdžiai
- Pridėtos klientų kūrimo gairės
- Įtraukta LLM klientų integracijos instrukcijos
- Pridėta VS Code integracijos dokumentacija
- Įgyvendinti Server-Sent Events (SSE) serverio pavyzdžiai

### Pagrindinės sąvokos (01-CoreConcepts/)
- Pridėtas išsamus kliento-serverio architektūros paaiškinimas
- Sukurta dokumentacija apie pagrindinius protokolo komponentus
- Dokumentuoti MCP žinučių modeliai

## 2025 m. gegužės 23 d.

### Saugyklos struktūra
- Inicializuota saugykla su pagrindine katalogų struktūra
- Sukurti README failai kiekvienam pagrindiniam skyriui
- Įdiegta vertimo infrastruktūra
- Pridėti vaizdų ištekliai ir diagramos

### Dokumentacija
- Sukurtas pradinio README.md su mokymo plano apžvalga
- Pridėti CODE_OF_CONDUCT.md ir SECURITY.md failai
- Įdiegta SUPPORT.md su pagalbos gavimo gairėmis
- Sukurta preliminari studijų vadovo struktūra

## 2025 m. balandžio 15 d.

### Planavimas ir sistema
- Pradinis MCP pradedantiesiems mokymo plano planavimas
- Apibrėžti mokymosi tikslai ir tikslinė auditorija
- Apibrėžta 10 skyrių mokymo plano struktūra
- Sukurtas konceptualus pavyzdžių ir atvejų studijų pagrindas
- Sukurti pradiniai pavyzdžiai pagrindinėms sąvokoms

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->