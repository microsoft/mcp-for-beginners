<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "245b03ae1e7973094fe82b8051ae0939",
  "translation_date": "2025-08-26T16:02:34+00:00",
  "source_file": "changelog.md",
  "language_code": "lt"
}
-->
# Keitimo žurnalas: MCP pradedančiųjų mokymo programa

Šis dokumentas yra visų reikšmingų pakeitimų, atliktų Model Context Protocol (MCP) pradedančiųjų mokymo programoje, įrašas. Pakeitimai dokumentuojami atvirkštine chronologine tvarka (naujausi pakeitimai pirmiausia).

## 2025 m. rugpjūčio 18 d.

### Dokumentacijos išsamus atnaujinimas - MCP 2025-06-18 standartai

#### MCP saugumo geriausios praktikos (02-Security/) - visiška modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Visiškai perrašyta pagal MCP specifikaciją 2025-06-18
  - **Privalomi reikalavimai**: Pridėti aiškūs MUST/MUST NOT reikalavimai iš oficialios specifikacijos su vizualiais žymekliais
  - **12 pagrindinių saugumo praktikų**: Pertvarkyta iš 15 punktų sąrašo į išsamius saugumo domenus
    - Žetonų saugumas ir autentifikacija su išorinių tapatybės teikėjų integracija
    - Sesijų valdymas ir transporto saugumas su kriptografiniais reikalavimais
    - AI specifinė grėsmių apsauga su Microsoft Prompt Shields integracija
    - Prieigos kontrolė ir leidimai pagal mažiausios privilegijos principą
    - Turinys saugumas ir stebėjimas su Azure Content Safety integracija
    - Tiekimo grandinės saugumas su išsamia komponentų patikra
    - OAuth saugumas ir „Confused Deputy“ prevencija su PKCE įgyvendinimu
    - Incidentų valdymas ir atkūrimas su automatizuotomis galimybėmis
    - Atitiktis ir valdymas su reguliavimo suderinimu
    - Pažangios saugumo kontrolės su „zero trust“ architektūra
    - Microsoft saugumo ekosistemos integracija su išsamiais sprendimais
    - Nuolatinė saugumo evoliucija su adaptacinėmis praktikomis
  - **Microsoft saugumo sprendimai**: Patobulinta integracijos gairė Prompt Shields, Azure Content Safety, Entra ID ir GitHub Advanced Security
  - **Įgyvendinimo ištekliai**: Kategorizuotos išsamios nuorodos pagal oficialią MCP dokumentaciją, Microsoft saugumo sprendimus, saugumo standartus ir įgyvendinimo gaires

#### Pažangios saugumo kontrolės (02-Security/) - įmonių įgyvendinimas
- **MCP-SECURITY-CONTROLS-2025.md**: Visiškai pertvarkyta su įmonių lygio saugumo sistema
  - **9 išsamūs saugumo domenai**: Išplėsta nuo bazinių kontrolės priemonių iki detalių įmonių sistemų
    - Pažangi autentifikacija ir autorizacija su Microsoft Entra ID integracija
    - Žetonų saugumas ir anti-passthrough kontrolės su išsamia validacija
    - Sesijų saugumo kontrolės su užgrobimo prevencija
    - AI specifinės saugumo kontrolės su prompt injekcijos ir įrankių užnuodijimo prevencija
    - „Confused Deputy“ atakų prevencija su OAuth proxy saugumu
    - Įrankių vykdymo saugumas su smėlio dėžės ir izoliacijos mechanizmais
    - Tiekimo grandinės saugumo kontrolės su priklausomybių patikra
    - Stebėjimo ir aptikimo kontrolės su SIEM integracija
    - Incidentų valdymas ir atkūrimas su automatizuotomis galimybėmis
  - **Įgyvendinimo pavyzdžiai**: Pridėti detalūs YAML konfigūracijos blokai ir kodo pavyzdžiai
  - **Microsoft sprendimų integracija**: Išsamiai aptartos Azure saugumo paslaugos, GitHub Advanced Security ir įmonių tapatybės valdymas

#### Pažangios temos saugumas (05-AdvancedTopics/mcp-security/) - paruošta gamybai
- **README.md**: Visiškai perrašyta įmonių saugumo įgyvendinimui
  - **Dabartinės specifikacijos suderinimas**: Atnaujinta pagal MCP specifikaciją 2025-06-18 su privalomais saugumo reikalavimais
  - **Patobulinta autentifikacija**: Microsoft Entra ID integracija su išsamiais .NET ir Java Spring Security pavyzdžiais
  - **AI saugumo integracija**: Microsoft Prompt Shields ir Azure Content Safety įgyvendinimas su detalizuotais Python pavyzdžiais
  - **Pažangi grėsmių mažinimas**: Išsamūs įgyvendinimo pavyzdžiai
    - „Confused Deputy“ atakų prevencija su PKCE ir vartotojo sutikimo validacija
    - Žetonų passthrough prevencija su auditorijos validacija ir saugiu žetonų valdymu
    - Sesijų užgrobimo prevencija su kriptografiniu susiejimu ir elgesio analize
  - **Įmonių saugumo integracija**: Azure Application Insights stebėjimas, grėsmių aptikimo kanalai ir tiekimo grandinės saugumas
  - **Įgyvendinimo kontrolinis sąrašas**: Aiškiai atskirti privalomi ir rekomenduojami saugumo kontrolės elementai su Microsoft saugumo ekosistemos privalumais

### Dokumentacijos kokybė ir standartų suderinimas
- **Specifikacijų nuorodos**: Atnaujintos visos nuorodos į dabartinę MCP specifikaciją 2025-06-18
- **Microsoft saugumo ekosistema**: Patobulintos integracijos gairės visoje saugumo dokumentacijoje
- **Praktinis įgyvendinimas**: Pridėti detalūs kodo pavyzdžiai .NET, Java ir Python su įmonių šablonais
- **Išteklių organizavimas**: Išsamiai kategorizuota oficiali dokumentacija, saugumo standartai ir įgyvendinimo gairės
- **Vizualūs žymekliai**: Aiškiai pažymėti privalomi reikalavimai ir rekomenduojamos praktikos

#### Pagrindinės sąvokos (01-CoreConcepts/) - visiška modernizacija
- **Protokolo versijos atnaujinimas**: Atnaujinta pagal dabartinę MCP specifikaciją 2025-06-18 su datos pagrindu versijavimu (YYYY-MM-DD formatas)
- **Architektūros patobulinimas**: Patobulinti aprašymai apie Host, Client ir Server, atspindintys dabartinius MCP architektūros modelius
  - Host aiškiai apibrėžti kaip AI programos, koordinuojančios kelis MCP klientų ryšius
  - Client aprašyti kaip protokolo jungtys, palaikančios vienas su vienu serverio ryšius
  - Server patobulinti su vietinio ir nuotolinio diegimo scenarijais
- **Primitivų pertvarkymas**: Visiškai pertvarkyti serverio ir kliento primityvai
  - Serverio primityvai: Ištekliai (duomenų šaltiniai), Šablonai (prompts), Įrankiai (vykdomos funkcijos) su detalizuotais paaiškinimais ir pavyzdžiais
  - Kliento primityvai: Mėginių ėmimas (LLM užbaigimai), Iškvietimas (vartotojo įvestis), Žurnalas (derinimas/stebėjimas)
  - Atnaujinta su dabartiniais atradimo (`*/list`), gavimo (`*/get`) ir vykdymo (`*/call`) metodų modeliais
- **Protokolo architektūra**: Pristatytas dviejų sluoksnių architektūros modelis
  - Duomenų sluoksnis: JSON-RPC 2.0 pagrindas su gyvavimo ciklo valdymu ir primityvais
  - Transporto sluoksnis: STDIO (vietinis) ir Streamable HTTP su SSE (nuotolinis) transporto mechanizmais
- **Saugumo sistema**: Išsamūs saugumo principai, įskaitant aiškų vartotojo sutikimą, duomenų privatumo apsaugą, įrankių vykdymo saugumą ir transporto sluoksnio saugumą
- **Komunikacijos modeliai**: Atnaujinti protokolo pranešimai, rodantys inicijavimo, atradimo, vykdymo ir pranešimų srautus
- **Kodo pavyzdžiai**: Atnaujinti daugiakalbiai pavyzdžiai (.NET, Java, Python, JavaScript), atspindintys dabartinius MCP SDK modelius

#### Saugumas (02-Security/) - išsamus saugumo pertvarkymas  
- **Standartų suderinimas**: Visiškas suderinimas su MCP specifikacijos 2025-06-18 saugumo reikalavimais
- **Autentifikacijos evoliucija**: Dokumentuota evoliucija nuo individualių OAuth serverių iki išorinių tapatybės teikėjų delegavimo (Microsoft Entra ID)
- **AI specifinė grėsmių analizė**: Patobulinta šiuolaikinių AI atakų vektorių aprėptis
  - Detalizuoti prompt injekcijos atakų scenarijai su realiais pavyzdžiais
  - Įrankių užnuodijimo mechanizmai ir „rug pull“ atakų modeliai
  - Konteksto lango užnuodijimas ir modelio painiavos atakos
- **Microsoft AI saugumo sprendimai**: Išsamiai aptarta Microsoft saugumo ekosistema
  - AI Prompt Shields su pažangiu aptikimu, akcentavimu ir ribotuvų technikomis
  - Azure Content Safety integracijos modeliai
  - GitHub Advanced Security tiekimo grandinės apsaugai
- **Pažangi grėsmių mažinimas**: Detalizuotos saugumo kontrolės
  - Sesijų užgrobimas su MCP specifiniais atakų scenarijais ir kriptografiniais sesijos ID reikalavimais
  - „Confused Deputy“ problemos MCP proxy scenarijuose su aiškiais sutikimo reikalavimais
  - Žetonų passthrough pažeidžiamumai su privalomais validacijos kontrolės elementais
- **Tiekimo grandinės saugumas**: Išplėsta AI tiekimo grandinės aprėptis, įskaitant pagrindinius modelius, įterpimo paslaugas, konteksto teikėjus ir trečiųjų šalių API
- **Pagrindinis saugumas**: Patobulinta integracija su įmonių saugumo modeliais, įskaitant „zero trust“ architektūrą ir Microsoft saugumo ekosistemą
- **Išteklių organizavimas**: Kategorizuotos išsamios nuorodos pagal tipą (oficiali dokumentacija, standartai, tyrimai, Microsoft sprendimai, įgyvendinimo gairės)

### Dokumentacijos kokybės patobulinimai
- **Struktūruoti mokymosi tikslai**: Patobulinti mokymosi tikslai su konkrečiais, veiksmais pagrįstais rezultatais
- **Kryžminės nuorodos**: Pridėtos nuorodos tarp susijusių saugumo ir pagrindinių sąvokų temų
- **Dabartinė informacija**: Atnaujintos visos datos ir specifikacijų nuorodos pagal dabartinius standartus
- **Įgyvendinimo gairės**: Pridėtos konkrečios, veiksmais pagrįstos įgyvendinimo gairės abiejuose skyriuose

## 2025 m. liepos 16 d.

### README ir navigacijos patobulinimai
- Visiškai pertvarkyta mokymo programos navigacija README.md faile
- Pakeisti `<details>` žymekliai į labiau prieinamą lentelės formatą
- Sukurti alternatyvūs išdėstymo variantai naujame „alternative_layouts“ aplanke
- Pridėti kortelių, skirtukų ir akordeono stiliaus navigacijos pavyzdžiai
- Atnaujinta saugyklos struktūros dalis, įtraukiant visus naujausius failus
- Patobulinta „Kaip naudoti šią mokymo programą“ dalis su aiškiomis rekomendacijomis
- Atnaujintos MCP specifikacijų nuorodos, nukreipiančios į teisingus URL
- Pridėta konteksto inžinerijos dalis (5.14) į mokymo programos struktūrą

### Mokymosi vadovo atnaujinimai
- Visiškai peržiūrėtas mokymosi vadovas, suderintas su dabartine saugyklos struktūra
- Pridėtos naujos dalys apie MCP klientus ir įrankius bei populiarius MCP serverius
- Atnaujintas vizualus mokymo programos žemėlapis, tiksliai atspindintis visas temas
- Patobulinti pažangių temų aprašymai, apimantys visas specializuotas sritis
- Atnaujinta atvejų analizės dalis, atspindinti realius pavyzdžius
- Pridėtas šis išsamus keitimo žurnalas

### Bendruomenės indėliai (06-CommunityContributions/)
- Pridėta išsami informacija apie MCP serverius vaizdų generavimui
- Pridėta išsami dalis apie Claude naudojimą VSCode
- Pridėtos Cline terminalo kliento nustatymo ir naudojimo instrukcijos
- Atnaujinta MCP klientų dalis, įtraukiant visus populiarius klientų variantus
- Patobulinti indėlių pavyzdžiai su tikslesniais kodo pavyzdžiais

### Pažangios temos (05-AdvancedTopics/)
- Organizuoti visi specializuotų temų aplankai su nuosekliais pavadinimais
- Pridėta konteksto inžinerijos medžiaga ir pavyzdžiai
- Pridėta Foundry agento integracijos dokumentacija
- Patobulinta Entra ID saugumo integracijos dokumentacija

## 2025 m. birželio 11 d.

### Pradinis sukūrimas
- Išleista pirmoji MCP pradedančiųjų mokymo programos versija
- Sukurta pagrindinė struktūra visiems 10 pagrindinių skyrių
- Įgyvendintas vizualus mokymo programos žemėlapis navigacijai
- Pridėti pradiniai pavyzdiniai projektai keliomis programavimo kalbomis

### Pradžia (03-GettingStarted/)
- Sukurti pirmieji serverio įgyvendinimo pavyzdžiai
- Pridėtos kliento kūrimo gairės
- Įtrauktos LLM kliento integracijos instrukcijos
- Pridėta VS Code integracijos dokumentacija
- Įgyvendinti Server-Sent Events (SSE) serverio pavyzdžiai

### Pagrindinės sąvokos (01-CoreConcepts/)
- Pridėtas išsamus kliento-serverio architektūros paaiškinimas
- Sukurta dokumentacija apie pagrindinius protokolo komponentus
- Dokumentuoti MCP pranešimų modeliai

## 2025 m. gegužės 23 d.

### Saugyklos struktūra
- Inicializuota saugykla su pagrindine aplankų struktūra
- Sukurti README failai kiekvienam pagrindiniam skyriui
- Sukurta vertimo infrastruktūra
- Pridėti vaizdo ištekliai ir diagramos

### Dokumentacija
- Sukurtas pradinis README.md su mokymo programos apžvalga
- Pridėti CODE_OF_CONDUCT.md ir SECURITY.md
- Sukurtas SUPPORT.md su pagalbos gavimo gairėmis
- Sukurta preliminari mokymosi vadovo struktūra

## 2025 m. balandžio 15 d.

### Planavimas ir struktūra
- Pradinis MCP pradedančiųjų mokymo programos planavimas
- Apibrėžti mokymosi tikslai ir tikslinė auditorija
- Nubrėžta 10 skyrių mokymo programos struktūra
- Sukurtas konceptualus pagrindas pavyzdžiams ir atvejų analizėms
- Sukurti pradiniai prototipiniai pavyzdžiai pagrindinėms sąvokoms

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.