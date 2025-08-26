<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c767a35642f753127dc08545c25a290",
  "translation_date": "2025-08-26T16:40:09+00:00",
  "source_file": "02-Security/README.md",
  "language_code": "lt"
}
-->
# MCP Saugumas: Išsamus AI sistemų apsaugos vadovas

[![MCP Saugumo Geriausios Praktikos](../../../translated_images/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.lt.png)](https://youtu.be/88No8pw706o)

_(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Saugumas yra esminis AI sistemų projektavimo elementas, todėl mes jį laikome prioritetu antrame skyriuje. Tai atitinka „Microsoft“ **Saugumo pagal dizainą** principą iš [Saugios ateities iniciatyvos](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Modelio Konteksto Protokolas (MCP) suteikia galingas naujas galimybes AI pagrįstoms programoms, tačiau kartu kelia unikalius saugumo iššūkius, kurie viršija tradicinės programinės įrangos rizikas. MCP sistemos susiduria tiek su įprastais saugumo klausimais (saugus kodavimas, minimalūs leidimai, tiekimo grandinės saugumas), tiek su naujomis AI specifinėmis grėsmėmis, tokiomis kaip komandų injekcija, įrankių užnuodijimas, sesijos užgrobimas, supainioto tarpininko atakos, žetonų perdavimo pažeidžiamumai ir dinaminis galimybių keitimas.

Šioje pamokoje nagrinėjamos svarbiausios MCP įgyvendinimo saugumo rizikos – nuo autentifikavimo, autorizacijos, perteklinių leidimų iki netiesioginės komandų injekcijos, sesijos saugumo, supainioto tarpininko problemų, žetonų valdymo ir tiekimo grandinės pažeidžiamumų. Sužinosite praktinius valdymo būdus ir geriausias praktikas, kaip sumažinti šias rizikas, pasitelkiant „Microsoft“ sprendimus, tokius kaip „Prompt Shields“, „Azure Content Safety“ ir „GitHub Advanced Security“, siekiant sustiprinti jūsų MCP diegimą.

## Mokymosi tikslai

Šios pamokos pabaigoje galėsite:

- **Atpažinti MCP specifines grėsmes**: Suprasti unikalius MCP sistemų saugumo pavojus, įskaitant komandų injekciją, įrankių užnuodijimą, perteklinius leidimus, sesijos užgrobimą, supainioto tarpininko problemas, žetonų perdavimo pažeidžiamumus ir tiekimo grandinės rizikas
- **Taikyti saugumo kontrolės priemones**: Įgyvendinti veiksmingas priemones, tokias kaip patikimas autentifikavimas, minimalūs leidimai, saugus žetonų valdymas, sesijos saugumo kontrolė ir tiekimo grandinės patikrinimas
- **Naudoti „Microsoft“ saugumo sprendimus**: Suprasti ir diegti „Microsoft Prompt Shields“, „Azure Content Safety“ ir „GitHub Advanced Security“ MCP darbo krūvio apsaugai
- **Patikrinti įrankių saugumą**: Suprasti įrankių metaduomenų patikrinimo, dinaminių pokyčių stebėjimo ir apsaugos nuo netiesioginės komandų injekcijos svarbą
- **Integruoti geriausias praktikas**: Derinti nusistovėjusius saugumo pagrindus (saugus kodavimas, serverių stiprinimas, nulinio pasitikėjimo principas) su MCP specifinėmis kontrolės priemonėmis, siekiant visapusiškos apsaugos

# MCP Saugumo Architektūra ir Kontrolė

Šiuolaikinės MCP įgyvendinimo sistemos reikalauja sluoksniuoto saugumo požiūrio, kuris apimtų tiek tradicinės programinės įrangos saugumą, tiek AI specifines grėsmes. Greitai besivystanti MCP specifikacija tobulina savo saugumo kontrolės priemones, leidžiančias geriau integruotis su įmonių saugumo architektūromis ir nusistovėjusiomis geriausiomis praktikomis.

Tyrimai iš [Microsoft Digital Defense Report](https://aka.ms/mddr) rodo, kad **98% praneštų pažeidimų būtų galima išvengti taikant tinkamą saugumo higieną**. Veiksmingiausia apsaugos strategija derina pagrindines saugumo praktikas su MCP specifinėmis kontrolės priemonėmis – įrodyta, kad bazinės saugumo priemonės yra labiausiai veiksmingos mažinant bendrą saugumo riziką.

## Dabartinė saugumo situacija

> **Pastaba:** Ši informacija atspindi MCP saugumo standartus, galiojančius **2025 m. rugpjūčio 18 d.** MCP protokolas sparčiai vystosi, o ateities įgyvendinimai gali pristatyti naujus autentifikavimo modelius ir patobulintas kontrolės priemones. Visada remkitės dabartine [MCP specifikacija](https://spec.modelcontextprotocol.io/), [MCP GitHub saugykla](https://github.com/modelcontextprotocol) ir [saugumo geriausių praktikų dokumentacija](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) dėl naujausių gairių.

### MCP autentifikavimo evoliucija

MCP specifikacija reikšmingai patobulino savo požiūrį į autentifikavimą ir autorizaciją:

- **Pradinis požiūris**: Ankstyvosiose specifikacijose kūrėjai turėjo įgyvendinti individualius autentifikavimo serverius, o MCP serveriai veikė kaip OAuth 2.0 autorizacijos serveriai, tiesiogiai valdantys naudotojų autentifikavimą
- **Dabartinis standartas (2025-06-18)**: Atnaujinta specifikacija leidžia MCP serveriams deleguoti autentifikavimą išoriniams tapatybės tiekėjams (pvz., „Microsoft Entra ID“), pagerinant saugumo lygį ir sumažinant įgyvendinimo sudėtingumą
- **Transporto sluoksnio saugumas**: Patobulinta saugių transporto mechanizmų parama su tinkamais autentifikavimo modeliais tiek vietiniams (STDIO), tiek nuotoliniams (Streamable HTTP) ryšiams

## Autentifikavimo ir autorizacijos saugumas

### Dabartiniai saugumo iššūkiai

Šiuolaikinės MCP įgyvendinimo sistemos susiduria su keliais autentifikavimo ir autorizacijos iššūkiais:

### Rizikos ir grėsmių vektoriai

- **Neteisingai sukonfigūruota autorizacijos logika**: Klaidingas autorizacijos įgyvendinimas MCP serveriuose gali atskleisti jautrius duomenis ir netinkamai taikyti prieigos kontrolę
- **OAuth žetonų kompromitavimas**: Vietinio MCP serverio žetonų vagystė leidžia užpuolikams apsimesti serveriais ir pasiekti paslaugas
- **Žetonų perdavimo pažeidžiamumai**: Netinkamas žetonų tvarkymas sukuria saugumo kontrolės apėjimus ir atsakomybės spragas
- **Pertekliniai leidimai**: Per dideli MCP serverių leidimai pažeidžia minimalių leidimų principą ir padidina atakos paviršių

#### Žetonų perdavimas: Kritinis anti-modelis

**Žetonų perdavimas yra griežtai draudžiamas** dabartinėje MCP autorizacijos specifikacijoje dėl rimtų saugumo pasekmių:

##### Saugumo kontrolės apėjimas
- MCP serveriai ir žemyn srauto API įgyvendina svarbias saugumo kontrolės priemones (užklausų ribojimas, užklausų tikrinimas, srauto stebėjimas), kurios priklauso nuo tinkamo žetonų tikrinimo
- Tiesioginis kliento ir API žetonų naudojimas apeina šias esmines apsaugos priemones, silpnindamas saugumo architektūrą

##### Atsakomybės ir audito iššūkiai  
- MCP serveriai negali atskirti klientų, naudojančių aukštyn srauto išduotus žetonus, taip pažeidžiant audito pėdsakus
- Žemyn srauto resursų serverių žurnaluose rodomi klaidinantys užklausų šaltiniai, o ne tikrieji MCP serverių tarpininkai
- Incidentų tyrimas ir atitikties auditas tampa žymiai sudėtingesni

##### Duomenų nutekėjimo rizika
- Nepatikrinti žetonų teiginiai leidžia piktavaliams veikėjams su pavogtais žetonais naudoti MCP serverius kaip tarpininkus duomenų nutekėjimui
- Pasitikėjimo ribų pažeidimai leidžia neautorizuotus prieigos modelius, kurie apeina numatytas saugumo kontrolės priemones

##### Daugiapaslaugės atakos vektoriai
- Kompromituoti žetonai, priimami keliose paslaugose, leidžia šoninius judesius tarp susijusių sistemų
- Pasitikėjimo prielaidos tarp paslaugų gali būti pažeistos, kai žetonų kilmė negali būti patikrinta

### Saugumo kontrolės priemonės ir mažinimo strategijos

**Kritiniai saugumo reikalavimai:**

> **PRIVALOMA**: MCP serveriai **NETURI** priimti jokių žetonų, kurie nebuvo aiškiai išduoti MCP serveriui

#### Autentifikavimo ir autorizacijos kontrolės priemonės

- **Griežta autorizacijos peržiūra**: Atlikite išsamias MCP serverio autorizacijos logikos peržiūras, kad įsitikintumėte, jog tik numatyti naudotojai ir klientai gali pasiekti jautrius resursus
  - **Įgyvendinimo vadovas**: [Azure API valdymas kaip autentifikavimo vartai MCP serveriams](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Tapatybės integracija**: [Microsoft Entra ID naudojimas MCP serverio autentifikavimui](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Saugus žetonų valdymas**: Įgyvendinkite [Microsoft žetonų tikrinimo ir gyvavimo ciklo geriausias praktikas](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Patikrinkite, ar žetonų auditorijos teiginiai atitinka MCP serverio tapatybę
  - Įgyvendinkite tinkamą žetonų rotaciją ir galiojimo politiką
  - Užkirsti kelią žetonų pakartotiniam naudojimui ir neautorizuotam naudojimui

- **Apsaugotas žetonų saugojimas**: Užtikrinkite žetonų saugojimą su šifravimu tiek ramybės būsenoje, tiek perduodant
  - **Geriausios praktikos**: [Saugus žetonų saugojimas ir šifravimo gairės](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Prieigos kontrolės įgyvendinimas

- **Minimalūs leidimai**: Suteikite MCP serveriams tik minimalius leidimus, reikalingus numatytai funkcijai
  - Reguliariai peržiūrėkite ir atnaujinkite leidimus, kad išvengtumėte leidimų kaupimosi
  - **Microsoft dokumentacija**: [Saugus minimalios prieigos principas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rolėmis pagrįsta prieigos kontrolė (RBAC)**: Įgyvendinkite smulkiai apibrėžtus vaidmenų priskyrimus
  - Apribokite vaidmenis tik konkretiems resursams ir veiksmams
  - Venkite plačių ar nereikalingų leidimų, kurie padidina atakos paviršių

- **Nuolatinis leidimų stebėjimas**: Įgyvendinkite nuolatinį prieigos auditą ir stebėjimą
  - Stebėkite leidimų naudojimo modelius dėl anomalijų
  - Nedelsiant pašalinkite perteklinius ar nenaudojamus leidimus
- **Saugus sesijos generavimas**: Naudokite kriptografiškai saugius, nedeterministinius sesijos ID, generuojamus su saugiais atsitiktinių skaičių generatoriais  
- **Vartotojui pritaikytas susiejimas**: Susiekite sesijos ID su vartotojo specifine informacija, naudodami formatus, pvz., `<user_id>:<session_id>`, kad išvengtumėte sesijų piktnaudžiavimo tarp vartotojų  
- **Sesijos gyvavimo ciklo valdymas**: Įgyvendinkite tinkamą galiojimo pabaigą, rotaciją ir anuliavimą, kad sumažintumėte pažeidžiamumo langus  
- **Transporto saugumas**: Privalomas HTTPS visai komunikacijai, kad būtų išvengta sesijos ID perėmimo  

### Supainioto tarpininko problema  

**Supainioto tarpininko problema** atsiranda, kai MCP serveriai veikia kaip autentifikavimo tarpininkai tarp klientų ir trečiųjų šalių paslaugų, sudarydami galimybes apeiti autorizaciją, naudojant statinius kliento ID.  

#### **Atakos mechanizmai ir rizikos**  

- **Slapukais pagrįsto sutikimo apeitis**: Ankstesnis vartotojo autentifikavimas sukuria sutikimo slapukus, kuriuos užpuolikai išnaudoja, pateikdami kenkėjiškus autorizacijos užklausas su suklastotais peradresavimo URI  
- **Autorizacijos kodo vagystė**: Esami sutikimo slapukai gali priversti autorizacijos serverius praleisti sutikimo ekranus, nukreipiant kodus į užpuoliko valdomus galinius taškus  
- **Neleistina API prieiga**: Pavogti autorizacijos kodai leidžia keistis žetonais ir apsimesti vartotoju be aiškaus patvirtinimo  

#### **Švelninimo strategijos**  

**Privalomos kontrolės:**  
- **Aiškūs sutikimo reikalavimai**: MCP tarpiniai serveriai, naudojantys statinius kliento ID, **PRIVALĖTŲ** gauti vartotojo sutikimą kiekvienam dinamiškai registruotam klientui  
- **OAuth 2.1 saugumo įgyvendinimas**: Laikykitės dabartinių OAuth saugumo geriausių praktikų, įskaitant PKCE (Proof Key for Code Exchange) visoms autorizacijos užklausoms  
- **Griežtas kliento tikrinimas**: Įgyvendinkite griežtą peradresavimo URI ir kliento identifikatorių tikrinimą, kad išvengtumėte išnaudojimo  

### Žetonų perdavimo pažeidžiamumai  

**Žetonų perdavimas** yra aiškus antipattern'as, kai MCP serveriai priima kliento žetonus be tinkamo patikrinimo ir perduoda juos žemyn esančioms API, pažeisdami MCP autorizacijos specifikacijas.  

#### **Saugumo pasekmės**  

- **Kontrolės apeitis**: Tiesioginis kliento ir API žetonų naudojimas apeina svarbias greičio ribojimo, tikrinimo ir stebėjimo kontrolės priemones  
- **Audito pėdsakų sugadinimas**: Aukštesnio lygio išduoti žetonai neleidžia identifikuoti kliento, trukdydami incidentų tyrimams  
- **Tarpinio serverio duomenų nutekėjimas**: Nepatikrinti žetonai leidžia kenkėjiškiems veikėjams naudoti serverius kaip tarpininkus neleistinai prieigai prie duomenų  
- **Pasitikėjimo ribų pažeidimai**: Žemyn esančių paslaugų pasitikėjimo prielaidos gali būti pažeistos, kai žetonų kilmė negali būti patvirtinta  
- **Daugiapaslaugės atakos plėtra**: Kompromituoti žetonai, priimami keliose paslaugose, leidžia judėti šoniniu būdu  

#### **Reikalingos saugumo kontrolės**  

**Nesiderėtini reikalavimai:**  
- **Žetonų tikrinimas**: MCP serveriai **NETURI** priimti žetonų, kurie nėra aiškiai išduoti MCP serveriui  
- **Auditorijos patikrinimas**: Visada tikrinkite, ar žetono auditorijos teiginiai atitinka MCP serverio tapatybę  
- **Tinkamas žetonų gyvavimo ciklas**: Įgyvendinkite trumpalaikius prieigos žetonus su saugiomis rotacijos praktikomis  

## Tiekimo grandinės saugumas AI sistemoms  

Tiekimo grandinės saugumas išsiplėtė už tradicinių programinės įrangos priklausomybių ribų, apimdamas visą AI ekosistemą. Modernios MCP įgyvendinimo priemonės turi griežtai tikrinti ir stebėti visus su AI susijusius komponentus, nes kiekvienas iš jų gali sukelti pažeidžiamumų, galinčių pakenkti sistemos vientisumui.  

### Išplėstiniai AI tiekimo grandinės komponentai  

**Tradicinės programinės įrangos priklausomybės:**  
- Atvirojo kodo bibliotekos ir karkasai  
- Konteinerių atvaizdai ir bazinės sistemos  
- Kūrimo įrankiai ir kūrimo vamzdynai  
- Infrastruktūros komponentai ir paslaugos  

**AI specifiniai tiekimo grandinės elementai:**  
- **Pagrindiniai modeliai**: Iš anksto apmokyti modeliai iš įvairių tiekėjų, kuriems reikalingas kilmės patikrinimas  
- **Įterpimo paslaugos**: Išorinės vektorizacijos ir semantinės paieškos paslaugos  
- **Konteksto teikėjai**: Duomenų šaltiniai, žinių bazės ir dokumentų saugyklos  
- **Trečiųjų šalių API**: Išorinės AI paslaugos, ML vamzdynai ir duomenų apdorojimo galiniai taškai  
- **Modelio artefaktai**: Svoris, konfigūracijos ir pritaikyti modelio variantai  
- **Mokymo duomenų šaltiniai**: Duomenų rinkiniai, naudojami modelio mokymui ir pritaikymui  

### Išsami tiekimo grandinės saugumo strategija  

#### **Komponentų tikrinimas ir pasitikėjimas**  
- **Kilmės patikrinimas**: Patikrinkite visų AI komponentų kilmę, licencijavimą ir vientisumą prieš integraciją  
- **Saugumo vertinimas**: Atlikite pažeidžiamumo skenavimus ir saugumo peržiūras modeliams, duomenų šaltiniams ir AI paslaugoms  
- **Reputacijos analizė**: Įvertinkite AI paslaugų teikėjų saugumo istoriją ir praktiką  
- **Atitikties patikrinimas**: Užtikrinkite, kad visi komponentai atitiktų organizacijos saugumo ir reguliavimo reikalavimus  

#### **Saugios diegimo linijos**  
- **Automatizuotas CI/CD saugumas**: Integruokite saugumo skenavimą visose automatizuotose diegimo linijose  
- **Artefaktų vientisumas**: Įgyvendinkite kriptografinį visų diegiamų artefaktų (kodo, modelių, konfigūracijų) patikrinimą  
- **Etapinis diegimas**: Naudokite progresyvaus diegimo strategijas su saugumo patikrinimu kiekviename etape  
- **Patikimos artefaktų saugyklos**: Diekite tik iš patikrintų, saugių artefaktų registrų ir saugyklų  

#### **Nuolatinis stebėjimas ir reagavimas**  
- **Priklausomybių skenavimas**: Nuolatinis pažeidžiamumo stebėjimas visoms programinės įrangos ir AI komponentų priklausomybėms  
- **Modelio stebėjimas**: Nuolatinis modelio elgsenos, našumo nukrypimų ir saugumo anomalijų vertinimas  
- **Paslaugų sveikatos stebėjimas**: Stebėkite išorines AI paslaugas dėl prieinamumo, saugumo incidentų ir politikos pokyčių  
- **Grėsmių žvalgybos integracija**: Įtraukite grėsmių srautus, susijusius su AI ir ML saugumo rizikomis  

#### **Prieigos kontrolė ir minimalus privilegijų principas**  
- **Komponentų lygio leidimai**: Apribokite prieigą prie modelių, duomenų ir paslaugų pagal verslo poreikį  
- **Paslaugų paskyrų valdymas**: Įgyvendinkite specialias paslaugų paskyras su minimaliomis reikalingomis teisėmis  
- **Tinklo segmentacija**: Izoliuokite AI komponentus ir apribokite tinklo prieigą tarp paslaugų  
- **API vartų kontrolė**: Naudokite centralizuotus API vartus, kad kontroliuotumėte ir stebėtumėte prieigą prie išorinių AI paslaugų  

#### **Incidentų reagavimas ir atkūrimas**  
- **Greito reagavimo procedūros**: Nustatytos procedūros, skirtos pataisyti arba pakeisti pažeistus AI komponentus  
- **Kredencialų rotacija**: Automatizuotos sistemos, skirtos paslapčių, API raktų ir paslaugų kredencialų rotacijai  
- **Atstatymo galimybės**: Galimybė greitai grįžti prie ankstesnių, patikrintų AI komponentų versijų  
- **Tiekimo grandinės pažeidimų atkūrimas**: Konkretūs veiksmai, skirti reaguoti į aukštesnio lygio AI paslaugų kompromisus  


### **Microsoft saugumo sprendimai**
- [Microsoft Prompt Shields dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure turinio saugos paslauga](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID saugumas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure žetonų valdymo geriausios praktikos](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub pažangus saugumas](https://github.com/security/advanced-security)

### **Įgyvendinimo vadovai ir mokymai**
- [Azure API valdymas kaip MCP autentifikavimo vartai](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentifikavimas su MCP serveriais](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Saugus žetonų saugojimas ir šifravimas (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps ir tiekimo grandinės saugumas**
- [Azure DevOps saugumas](https://azure.microsoft.com/products/devops)
- [Azure Repos saugumas](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft tiekimo grandinės saugumo kelionė](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Papildoma saugumo dokumentacija**

Norėdami gauti išsamias saugumo rekomendacijas, peržiūrėkite šiuos specializuotus dokumentus šiame skyriuje:

- **[MCP saugumo geriausios praktikos 2025](./mcp-security-best-practices-2025.md)** - Išsamios saugumo geriausios praktikos MCP įgyvendinimui
- **[Azure turinio saugos įgyvendinimas](./azure-content-safety-implementation.md)** - Praktiniai pavyzdžiai, kaip integruoti Azure turinio saugą  
- **[MCP saugumo kontrolės 2025](./mcp-security-controls-2025.md)** - Naujausios saugumo kontrolės ir technikos MCP diegimui
- **[MCP geriausių praktikų greita nuoroda](./mcp-best-practices.md)** - Greita nuoroda į esmines MCP saugumo praktikas

---

## Kas toliau

Toliau: [3 skyrius: Pradžia](../03-GettingStarted/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, kylančius dėl šio vertimo naudojimo.