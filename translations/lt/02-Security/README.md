# MCP saugumas: visapusiška AI sistemų apsauga

[![MCP Security Best Practices](../../../translated_images/lt/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Spustelėkite aukščiau esantį vaizdą, norėdami peržiūrėti pamokos vaizdo įrašą)_

Saugumas yra pagrindinis AI sistemų dizaino elementas, todėl mes jį prioritetizuojame kaip antrą skyrių. Tai atitinka Microsoft principą **Saugumas pagal dizainą** iš [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Modelio konteksto protokolas (MCP) suteikia galingų naujų galimybių AI varomoms programoms, tačiau įveda išskirtines saugumo problemas, kurios viršija tradicines programinės įrangos rizikas. MCP sistemos susiduria tiek su įprastomis saugumo problemomis (saugus kodavimas, mažiausios teisės, tiekimo grandinės saugumas), tiek su naujais AI specifiniais pavojais, įskaitant užklausų injekcijas, įrankių apsinuodijimą, sesijos užgrobimą, supainioto administratoriaus atakas, žetonų praeinamumo spragas ir dinaminio pajėgumo modifikavimą.

Ši pamoka nagrinėja svarbiausias MCP įgyvendinimo saugumo rizikas – apimančias autentifikaciją, autorizaciją, perteklines teises, netiesiogines užklausų injekcijas, sesijos saugumą, supainioto administratoriaus problemas, žetonų valdymą ir tiekimo grandinės pažeidžiamumus. Išmoksite veiksmingų kontrolės priemonių ir geriausių praktikų, kaip sumažinti šias rizikas, pasitelkdami Microsoft sprendimus, tokius kaip Prompt Shields, Azure Content Safety ir GitHub Advanced Security, kad sustiprintumėte savo MCP diegimą.

## Mokymosi tikslai

Iki šios pamokos pabaigos jūs gebėsite:

- **Atpažinti MCP specifines grėsmes**: atpažinti unikalius saugumo pavojus MCP sistemose, įskaitant užklausų injekciją, įrankių apsinuodijimą, perteklines teises, sesijos užgrobimą, supainioto administratoriaus problemas, žetonų praeinamumo trūkumus ir tiekimo grandinės rizikas
- **Taikyti saugumo kontrolę**: įgyvendinti veiksmingas priemones, tarp jų patikimą autentifikaciją, mažiausių teisių prieigą, saugų žetonų valdymą, sesijos saugumo kontrolę ir tiekimo grandinės patikrinimą
- **Pasitelkti Microsoft saugumo sprendimus**: suprasti ir diegti Microsoft Prompt Shields, Azure Content Safety ir GitHub Advanced Security MCP darbo krūvio apsaugai
- **Tikrinti įrankių saugumą**: pripažinti įrankių metaduomenų patikros svarbą, stebėti dinamiškus pakeitimus ir gintis nuo netiesioginių užklausų injekcijos atakų
- **Integruoti geriausias praktikas**: derinti patvirtintas saugumo pagrindus (saugus kodavimas, serverio tvirtinimas, zero trust) su MCP specifinėmis kontrolėmis visapusiškai apsaugai

# MCP saugumo architektūra ir kontrolės

Šiuolaikiniai MCP diegimai reikalauja sluoksniuotos saugumo strategijos, apimančios tiek tradicinį programinės įrangos saugumą, tiek AI specifines grėsmes. Greitai tobulėjanti MCP specifikacija toliau tobulina savo saugumo kontrolės priemones, leidžiančias geriau integruotis į įmonių saugumo architektūras ir patvirtintas geriausias praktikas.

Tyrimai iš [Microsoft Digital Defense Report](https://aka.ms/mddr) rodo, kad **98 % praneštų saugumo pažeidimų būtų užkirsti kelias taikant griežtą saugumo higieną**. Efektyviausia apsaugos strategija derina pagrindines saugumo praktikas su MCP specifinėmis kontrolėmis – patikrintos bazinės saugumo priemonės išlieka pagrindiniu rizikos mažinimo veiksniu.

## Dabartinė saugumo padėtis

> **Pastaba:** Šis skyrius jungia patvirtintas MCP saugumo kontrolės priemones su
> dabartinėmis **MCP specifikacijos 2026-07-28** autorizacijos gairėmis. Visada kreipkitės
> į dabartinę [MCP specifikaciją](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub saugyklą](https://github.com/modelcontextprotocol) ir
> [saugumo geriausių praktikų dokumentaciją](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> įgyvendinant saugumui jautrią kodą.

> **Autorizacijos atnaujinimas:** MCP `2026-07-28` reikalauja klientams patvirtinti
> `iss` parametrą autorizacijos atsakymuose (RFC 9207) ir susieti registruotus
> įgaliojimus su išduodančiu autorizacijos serveriu. Dinaminė kliento registracija
> yra pasenusi; nauji diegimai turėtų naudoti Kliento ID metaduomenų dokumentus.
> Žr. [Kas pasikeitė MCP: 2026-07-28 specifikacija](../01-CoreConcepts/mcp-2026-07-28.md)
> dėl pilno autorizacijos pakeitimų sąrašo.

## 🏔️ MCP Saugumo Viršūnių Seminare (Sherpa)

Rekomenduojame **praktinius saugumo mokymus** – **MCP Saugumo Viršūnių Seminarą (Sherpa)**, kuris yra išsamus vadovaujamas žygis MCP serverių saugumui Microsoft Azure aplinkoje užtikrinti.

### Seminaro apžvalga

[MCP Saugumo Viršūnių Seminaras](https://azure-samples.github.io/sherpa/) suteikia praktinius, veiksmingus saugumo mokymus per patvirtintą "pažeidžiamumas → pasinaudojimas → taisymas → patvirtinimas" metodiką. Jūs:

- **Mokysitės per klaidų paiešką**: patirsite pažeidžiamumus tiesiogiai, išnaudodami specialiai nesaugias serverių versijas
- **Naudosite vietinius Azure saugumo įrankius**: Azure Entra ID, Key Vault, API valdymą ir AI turinio saugumą
- **Seksite gynybos sluoksniuotumo principą**: žengsite per mokymosi etapus, kuriant išsamias saugumo sluoksnius
- **Taikysite OWASP standartus**: kiekviena technika atitinka [OWASP MCP Azure Saugumo Gairių](https://microsoft.github.io/mcp-azure-security-guide/) reikalavimus
- **Gausite gamybinius kodus**: išeisite su veikiamais, išbandytais sprendimais

### Ekspedicijos maršrutas

| Stovyklavietė | Fokusas | Apimtų OWASP rizikų kodai |
|------|-------|---------------------|
| **Pagrindinė stovykla** | MCP pagrindai ir autentifikacijos spragos | MCP01, MCP07 |
| **1-oji stovykla: Tapatybė** | OAuth 2.1, Azure valdomoji tapatybė, Key Vault | MCP01, MCP02, MCP07 |
| **2-oji stovykla: Vartai** | API valdymas, privatūs galiniai taškai, valdymas | MCP02, MCP06, MCP07, MCP09 |
| **3-oji stovykla: I/O saugumas** | Užklausų injekcija, asmeninės duomenų apsauga, turinio saugumas | MCP03, MCP05, MCP06, MCP10 |
| **4-oji stovykla: Stebėsena** | Žurnalų analizė, valdymo skydeliai, grėsmių aptikimas | MCP04, MCP08 |
| **Viršukalnė** | Raudonosios ir Mėlynosios komandos integracinis testas | Visos |

**Pradėti:** [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 saugumo rizikų

[OWASP MCP Azure Saugumo Gairės](https://microsoft.github.io/mcp-azure-security-guide/) aprašo dešimt svarbiausių MCP įgyvendinimo saugumo rizikų:

| Rizika | Aprašymas | Azure sumažinimo priemonės |
|------|-------------|------------------|
| **MCP01** | Žetonų nevaldymas ir slaptažodžių atskleidimas | Azure Key Vault, valdomoji tapatybė |
| **MCP02** | Teisių padidinimas per savo apimties išpuolį | RBAC, sąlyginė prieiga |
| **MCP03** | Įrankių apsinuodijimas | Įrankių patikra, vientisumo tikrinimas |
| **MCP04** | Programinės įrangos tiekimo grandinės atakos ir priklausomybių klastojimas | GitHub Advanced Security, priklausomybių skenavimas |
| **MCP05** | Komandų injekcija ir vykdymas | Įvesties tikrinimas, smėlio dėžės naudojimas |
| **MCP06** | Ketinimų srauto sutrikdymas | Azure AI turinio saugumas, Prompt Shields |
| **MCP07** | Nepakankama autentifikacija ir autorizacija | Azure Entra ID, OAuth 2.1 su PKCE |
| **MCP08** | Audito ir telemetrijos trūkumas | Azure Monitor, Application Insights |
| **MCP09** | Šešėliniai MCP serveriai | API centrinis valdymas, tinklo izoliacija |
| **MCP10** | Konteksto injekcija ir perteklinis dalinimasis | Duomenų klasifikacija, minimalus viešinimas |

### MCP autentifikacijos raida

MCP specifikacija smarkiai evoliucionavo autentifikacijos ir autorizacijos srityje:

- **Pirminis požiūris**: Ankstyvosios specifikacijos reikalavo, kad kūrėjai įgyvendintų individualius autentifikacijos serverius, o MCP serveriai vaidintų kaip OAuth 2.0 autorizacijos serveriai, tiesiogiai tvarkantys naudotojų autentifikaciją
- **Dabartinis standartas (`2026-07-28`)**: MCP serveriai gali deleguoti autentifikaciją
  išoriniams tapatybės teikėjams, tokiems kaip Microsoft Entra ID. Klientai taip pat
  privalo taikyti dabartinius leidėjo patvirtinimo ir įgaliojimų susiejimo reikalavimus.
- **Transporto sluoksnio saugumas**: Pagerintas saugių transporto mechanizmų palaikymas su tinkamais autentifikacijos modeliais tiek vietiniams (STDIO), tiek nuotoliniams (Streamable HTTP) ryšiams

## Autentifikacijos ir autorizacijos saugumas

### Dabartinės saugumo problemos

Šiuolaikiniai MCP diegimai susiduria su keliomis autentifikacijos ir autorizacijos iššūkiais:

### Rizikos ir grėsmių vektoriai

- **Neteisingai sukonfigūruota autorizacijos logika**: klaidingas autorizacijos įgyvendinimas MCP serveriuose gali atskleisti jautrius duomenis ir neteisingai taikyti prieigos kontrolę
- **OAuth žetonų kompromitavimas**: vietinio MCP serverio žetonų vagystė leidžia užpuolikams apsimesti serveriais ir pasiekti tolesnes paslaugas
- **Žetonų praeinamumo spragos**: netinkamas žetonų tvarkymas sukuria saugumo kontrolės apeigas ir atskaitomybės spragas
- **Perteklinės teisės**: per daug įgaliojimų turintys MCP serveriai pažeidžia mažiausių teisių principą ir išplečia atakų paviršių

#### Žetonų praeinamumas: kritinė klaida

**Žetonų praeinamumas yra griežtai draudžiamas** dabartinėje MCP autorizacijos specifikacijoje dėl rimtų saugumo pasekmių:

##### Saugumo kontrolės apeigos
- MCP serveriai ir tolimieji API įgyvendina svarbias saugumo priemones (vietos ribojimas, užklausų patikra, eismo stebėsena), kurios priklauso nuo tinkamo žetonų tikrinimo
- Tiesioginis kliento žetonų naudojimas tiesiogiai API apeina šias apsaugas, silpnindamas saugumo architektūrą

##### Atsakomybės ir audito problemos  
- MCP serveriai nesugeba atskirti tarp klientų, naudojančių iš anksto išduotus upstream žetonus, todėl nutrūksta audito grandinės
- Tolimosios išteklių serverio žurnalai rodo klaidinančius užklausų šaltinius, o ne faktinius MCP serverių tarpininkus
- Įvykio tyrimai ir atitikties auditai tampa ženkliai sudėtingesni

##### Duomenų nutekėjimo rizikos
- Nepatikrintos žetonų teiginių leidžia piktavaliams asmenims, turintiems pavogtus žetonus, naudoti MCP serverius kaip tarpininkus duomenų nutekinimui
- Pasitikėjimo ribų pažeidimai leidžia neteisėtą prieigą, apeinant numatytas saugumo kontrolės priemones

##### Daugelio paslaugų atakų vektoriai
- Priimti kompromituoti žetonai daugybėje paslaugų leidžia sklisti per sujungtas sistemas
- Pasitikėjimo prielaidos tarp paslaugų gali būti pažeistos, kai nėra galimybės patikrinti žetonų kilmę

### Saugumo kontrolės ir mažinimo priemonės

**Svarbiausi saugumo reikalavimai:**

> **PRIEVOLĖ:** MCP serveriai **NETURI PRIIMTI** jokių žetonų, kurie nėra aiškiai išduoti būtent tam MCP serveriui

#### Autentifikacijos ir autorizacijos kontrolės

- **Griežtas autorizacijos peržiūrėjimas**: atlikite išsamų MCP serverio autorizacijos logikos auditą, užtikrinant, kad prieigą prie jautrių išteklių turėtų tik numatytieji vartotojai ir klientai
  - **Įgyvendinimo gidas**: [Azure API valdymas kaip autentifikacijos vartų sprendimas MCP serveriams](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Tapatybės integracija**: [Microsoft Entra ID naudojimas MCP serverio autentifikacijai](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Saugus žetonų valdymas**: įgyvendinkite [Microsoft žetonų patikros ir gyvavimo ciklo geriausias praktikas](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Patikrinkite, ar žetonų auditorijos teiginiai atitinka MCP serverio tapatybę
  - Įgyvendinkite tinkamas žetonų rotacijos ir galiojimo pabaigos politiką
  - Užkirsti kelią žetonų pakartotinoms atakoms ir neteisėtam naudojimui

- **Apsaugotas žetonų saugojimas**: saugokite žetonus šifruotus tiek ramybėje, tiek perdavimo metu
  - **Geriausios praktikos**: [Saugus žetonų saugojimas ir šifravimo gairės](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Prieigos kontrolės įgyvendinimas

- **Mažiausių teisių principas**: suteikite MCP serveriams tik būtiniausias teises numatytoms funkcijoms atlikti
  - Reguliarūs teisių peržiūrimai ir atnaujinimai, kad būtų išvengta teisės išplėtimo
  - **Microsoft dokumentacija**: [Saugus mažiausių teisių suteikimas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Pritaikyta vaidmenų pagrindu veikianti prieigos kontrolė (RBAC)**: įgyvendinkite smulkiai valdomus vaidmenų priskyrimus
  - Tiksliai nustatykite vaidmenis konkretiems ištekliams ir veiksmams
  - Venkite plačių ar nereikalingų teisių, kurios padidina atakų paviršių

- **Nuolatinė teisių stebėsena**: įgyvendinkite nuolatinį prieigos audito ir stebėsena procesą
  - Stebėkite teisių naudojimo modelius dėl anomalijų
  - Greitai pašalinkite perteklines arba nenaudojamas teises

## AI specifinės saugumo grėsmės

### Užklausų injekcijos ir įrankių manipuliavimo atakos

Šiuolaikiniai MCP diegimai susiduria su rafinuotais AI specifiniais atakų vektoriais, kuriuos tradicinės saugumo priemonės negali visiškai pašalinti:

#### **Netiesioginė užklausų injekcija (tarpdomeninė užklausų injekcija)**

**Netiesioginė užklausų injekcija** yra viena iš kritiškiausių spragų MCP įgalintuose AI sistemose. Užpuolikai įterpia kenksmingas instrukcijas į išorinį turinį – dokumentus, interneto puslapius, el. laiškus ar duomenų šaltinius, kuriuos AI sistema vėliau interpretuoja kaip teisėtas komandas.

**Atakų scenarijai:**
- **Dokumentų pagrindu įterpta injekcija**: kenksmingos instrukcijos paslėptos apdorojamuose dokumentuose, sukeliantys nenumatytas AI veiklas
- **Interneto turinio išnaudojimas**: kompromituoti tinklapiai su įterptomis užklausomis, kurios manipuliuoja AI elgsena duomenims renkant
- **El. laiškų atakos**: kenksmingos užklausos el. laiškuose, verčiančios AI pagalbininkus nutekinti informaciją ar atlikti neteisėtas operacijas
- **Duomenų šaltinių užteršimas**: kompromituotos duomenų bazės ar API, tiekiantys užkrėstą turinį AI sistemoms

**Reali pasekmė:** šios atakos gali sukelti duomenų nutekėjimą, privatumo pažeidimus, žalingo turinio generavimą ir naudotojų sąveikų manipuliavimą. Išsamią analizę rasite [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/lt/prompt-injection.ed9fbfde297ca877.webp)

#### **Įrankių apsinuodijimo atakos**

**Įrankių apsinuodijimas** taikosi į metaduomenis, apibrėžiančius MCP įrankius, išnaudojant tai, kaip LLM interpretuoja įrankių aprašymus ir parametrus būsimiems veiksmams.

**Atakų mechanizmai:**
- **Metaduomenų manipulacija**: užpuolikai įterpia kenksmingas instrukcijas į įrankių aprašus, parametrų apibrėžimus ar naudojimo pavyzdžius
- **Nematomi nurodymai**: paslėptos užklausos įrankių metaduomenyse, kurias apdoroja AI modeliai, bet jų nemato žmonės
- **Dinaminiai įrankių pakeitimai („Kilimų traukymas“) (Rug Pulls)**: vartotojų patvirtinti įrankiai vėliau modifikuojami kenksmingoms veikloms be vartotojo žinios
- **Parametrų injekcija**: kenksmingas turinys integruotas į įrankio parametrų schemas, veikiantis modelio elgseną


**Priimamo serverio rizikos**: Nuotoliniai MCP serveriai kelia didesnę riziką, nes įrankių apibrėžimus galima atnaujinti po pradinio vartotojo patvirtinimo, sukuriant situacijas, kai anksčiau saugūs įrankiai tampa kenkėjiški. Išsamiai analizei žr. [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/lt/tool-injection.3b0b4a6b24de6bef.webp)

#### **Papildomi DI atakų vektoriai**

- **Kryžminės srities užklausų injekcija (XPIA)**: Sudėtingos atakos, kurios pasitelkia kelių sričių turinį siekiant apeiti saugumo kontrolę
- **Dinaminis funkcionalumo keitimas**: Įrankių galimybių realaus laiko keitimai, kurių pradinės saugumo apžvalgos nepastebi
- **Konteksto lango apnuodijimas**: Atakos, manipuliuojančios dideliais konteksto langais, kad paslėptų kenkėjiškas instrukcijas
- **Modelių painiavos atakos**: Modelių ribotumų išnaudojimas, sukuriant nenuspėjamą arba nesaugią elgseną


### DI saugumo rizikos poveikis

**Didelio poveikio pasekmės:**
- **Duomenų nutekėjimas**: Netinkamas prieigos gavimas ir jautrių įmonių ar asmeninių duomenų vagystė
- **Privatumo pažeidimai**: Asmens identifikavimo duomenų (PII) ir konfidencialios verslo informacijos atskleidimas  
- **Sistemų manipuliavimas**: Netikėti kritinių sistemų ir darbo procesų pakeitimai
- **Autentifikacijos duomenų vagystė**: Autentifikacijos žetonų ir paslaugų kredencialų kompromitavimas
- **Šoninė judėjimo galimybė**: Pažeistų DI sistemų naudojimas kaip atakos per tinklą pradininkai

### Microsoft DI saugumo sprendimai

#### **DI užklausų skydai: pažangi apsauga nuo injekcijos atakų**

Microsoft **DI užklausų skydai** suteikia išsamią gynybą tiek nuo tiesioginių, tiek netiesioginių užklausų injekcijų atakų per kelis saugumo sluoksnius:

##### **Pagrindiniai apsaugos mechanizmai:**

1. **Pažangi aptikimo ir filtravimo sistema**
   - Mašininio mokymosi algoritmai ir NLP technikos aptinka kenkėjiškas instrukcijas išoriniame turinyje
   - Dokumentų, tinklalapių, el. laiškų ir duomenų šaltinių grėsmių realaus laiko analizė
   - Kontekstinis supratimas, kas yra teisėta ir kas kenksminga užklausų formos

2. **Išryškinimo technikos**  
   - Skiria patikimas sistemos instrukcijas nuo galimai pažeisto išorinio įvesties turinio
   - Teksto transformavimo metodai, kurie didina modelio aktualumą ir izoliuoja kenkėjišką turinį
   - Padeda DI sistemoms išlaikyti tinkamą instrukcijų hierarchiją ir ignoruoti įterptas komandas

3. **Ribų ir duomenų žymėjimo sistemos**
   - Aiškus ribų apibrėžimas tarp patikimų sistemos pranešimų ir išorinės įvesties teksto
   - Specialūs žymekliai pabrėžia ribas tarp patikimų ir nepatikimų duomenų šaltinių
   - Aiški atskirtis apsaugo nuo instrukcijų painiavos ir neteisėto komandų vykdymo

4. **Nuolatinė grėsmių žvalgyba**
   - Microsoft nuolat stebi iškilusias atakų strategijas ir atnaujina gynybą
   - Proaktyvi grėsmių paieška naujoms injekcijos technikoms ir atakų vektoriams
   - Reguliarūs saugumo modelių atnaujinimai, siekiant išlaikyti efektyvumą prieš kintančias grėsmes

5. **Azure turinio saugos integracija**
   - Dalis išsamios Azure DI turinio saugos komplekto
   - Papildomas aptikimas bandymams „apgauti sistemą“, kenksmingam turiniui ir saugumo politikos pažeidimams
   - Vieningos saugumo kontrolės visoms DI programų sudedamosioms dalims

**Įgyvendinimo ištekliai**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/lt/prompt-shield.ff5b95be76e9c78c.webp)


## Pažangios MCP saugumo grėsmės

### Sesijos užgrobimo pažeidžiamumai

**Sesijos užgrobimas** yra kritinis atakos vektorius būseną saugančiose MCP įgyvendinimuose, kai neautorizuotos šalys gauna ir piktnaudžiauja teisėtais sesijos identifikatoriais, apsimesdamos klientais ir atliekamos neleistinos veiklos.

#### **Atakų scenarijai ir rizikos**

- **Sesijos užgrobimo užklausos injekcija**: Atakotojai su pavogtais sesijos ID įterpia kenkėjiškus įvykius į serverius, dalijančius sesijos būseną, galimai sukeliančius žalingas veiklas arba prieigą prie jautrios informacijos
- **Tiesioginė apsimetinėjimas**: Pavogti sesijos ID leidžia tiesioginius MCP serverio kvietimus, apeinant autentifikaciją ir elgiantis kaip teisėti vartotojai
- **Komprontuotų tęstinų srautų problemos**: Atakotojai gali iš anksto nutraukti užklausas, dėl ko teisėti klientai gali tęsti su galimai kenkėjišku turiniu

#### **Sesijos valdymo saugumo kontrolės**

**Kritiniai reikalavimai:**
- **Autorizacijos patikrinimas**: MCP serveriai, kurie įgyvendina autorizaciją, **TURI** patikrinti VISAS įeinančias užklausas ir **NETURI** naudoti sesijų autentifikacijai
- **Saugus sesijos generavimas**: Naudoti kriptografiškai saugius, nedeterministinius sesijos ID, generuojamus su saugiais atsitiktinių skaičių generatoriais
- **Vartotojui specifinis susiejimas**: Susieti sesijos ID su vartotojui priskirta informacija tokiu formatu kaip `<user_id>:<session_id>`, kad būtų išvengta sesijų piktnaudžiavimo tarp vartotojų
- **Sesijos gyvavimo ciklo valdymas**: Įgyvendinti tinkamą galiojimo laiko pabaigą, rotaciją ir nebegaliojimo mechanizmus, kad būtų sugriežtintos pažeidžiamumo ribos
- **Transporto saugumas**: Privalomas HTTPS visai komunikacijai, kad būtų užkirstas kelias sesijos ID pagrobimui

### Painaus tarpininko problema

**Painaus tarpininko problema** kyla, kai MCP serveriai veikia kaip autentifikacijos tarpininkai tarp klientų ir trečiųjų šalių paslaugų, leidžiant apeiti autorizaciją naudojant statinius kliento ID.

#### **Atakų mechanika ir rizikos**

- **Sutikimo apeinimas remiantis slapukais**: Ankstesnė vartotojo autentifikacija sukuria sutikimo slapukus, kuriuos atakotojai išnaudoja siunčiant kenkėjiškas autorizacijos užklausas su specialiai sukurtomis peradresavimo URI
- **Autorizacijos kodo vagystė**: Esami sutikimo slapukai gali leisti autorizacijos serveriams praleisti sutikimo ekranus ir peradresuoti kodus į atakoto kontroluojamus taškus  
- **Neautorizuota API prieiga**: Pavogti autorizacijos kodai leidžia apsikeisti žetonais ir apsimesti vartotojais be aiškaus vietinio patvirtinimo

#### **Sumažinimo strategijos**

**Privalomos kontrolės:**
- **Aiškūs sutikimo reikalavimai**: MCP tarpiniai serveriai, naudojantys statinius kliento ID, **TURI** gauti vartotojo sutikimą kiekvienam dinamiškai registruotam klientui
- **OAuth 2.1 saugumo įgyvendinimas**: Vadovautis dabartinėmis OAuth saugumo gerosios praktikos gairėmis, įskaitant PKCE (Proof Key for Code Exchange) visoms autorizacijos užklausoms
- **Griežtas kliento validavimas**: Įgyvendinti griežtą peradresavimo URI ir kliento identifikatorių validavimą, kad būtų išvengta neteisėto naudojimo

### Žetonų perleidimo pažeidžiamumai  

**Žetonų perleidimas** yra aiškus anti-patern’as, kai MCP serveriai priima kliento žetonus be tinkamo patvirtinimo ir perduoda juos žemyninis API, pažeisdami MCP autorizacijos specifikacijas.

#### **Saugumo pasekmės**

- **Kontrolės apeinimas**: Tiesioginis kliento į API žetono naudojimas aplenkia svarbias ribojimo, validavimo ir stebėjimo priemones
- **Auditavimo takelio sugadinimas**: Žetonai, išduoti aukščiau, neleidžia identifikuoti kliento, trukdant incidentų tyrimams
- **Proxy pagrindu vykdoma duomenų nutekėjimas**: Nepatikrinti žetonai leidžia kenkėjiškam subjektui naudoti serverius kaip proxy neautorizuotai prieigai prie duomenų
- **Pasitikėjimo ribų pažeidimai**: Žemyninių paslaugų pasitikėjimo nuostatos gali būti pažeistos, kai negalima patikrinti žetono kilmės
- **Daugiapaslaugės atakos plėtra**: Priimti kompromituoti žetonai keliuose paslaugose leidžia šoninį judėjimą

#### **Privalomos saugumo kontrolės**

**Neabejotini reikalavimai:**
- **Žetonų patikra**: MCP serveriai **NETURI** priimti žetonų, kurie nėra aiškiai išduoti būtent MCP serveriui
- **Publikumų patikrinimas**: Visada tikrinkite, ar žetono publiko pretenzijos atitinka MCP serverio tapatybę
- **Tinkamas žetono gyvavimo ciklas**: Įgyvendinti trumpalaikius prieigos žetonus su saugia rotacija


## Tiekimo grandinės saugumas DI sistemoms

Tiekimo grandinės saugumas išsiplėtė nuo tradicinių programinės įrangos priklausomybių iki visos DI ekosistemos. Šiuolaikiniai MCP įgyvendinimai privalo griežtai tikrinti ir stebėti visas su DI susijusias dalis, nes kiekviena gali turėti pažeidžiamumų, kompromituojančių sistemos vientisumą.

### Išplėstiniai DI tiekimo grandinės komponentai

**Tradicinės programinės įrangos priklausomybės:**
- Atvirojo kodo bibliotekos ir karkasai
- Konteinerių vaizdai ir bazinės sistemos  
- Kūrimo įrankiai ir statybos vamzdynai
- Infrastruktūros komponentai ir paslaugos

**DI specifiniai tiekimo grandinės elementai:**
- **Pagrindiniai modeliai**: Iš anksto apmokyti modeliai iš įvairių tiekėjų, reikalaujantys kilmės patikrinimo
- **Įterpimo paslaugos**: Išorinės vektorizacijos ir semantinės paieškos paslaugos
- **Konteksto tiekėjai**: Duomenų šaltiniai, žinių bazės ir dokumentų saugyklos  
- **Trečiųjų šalių API**: Išorinės DI paslaugos, ML vamzdynai ir duomenų apdorojimo galutiniai taškai
- **Modelių artefaktai**: Svoriai, konfigūracijos ir tiksliai sureguliuoti modelių variantai
- **Mokymo duomenų šaltiniai**: Duomenų rinkiniai, naudojami modelių mokymui ir tikslinimui

### Išsamios tiekimo grandinės saugumo strategija

#### **Komponentų patikra ir pasitikėjimas**
- **Kilmės patvirtinimas**: Patikrinti visų DI komponentų kilmę, licencijavimą ir vientisumą prieš integraciją
- **Saugumo vertinimas**: Atlikti pažeidžiamumo nuskaitymus ir saugumo apžvalgas modeliams, duomenų šaltiniams ir DI paslaugoms
- **Reputacijos analizė**: Įvertinti DI paslaugų tiekėjų saugumo rekordą ir praktiką
- **Atitikimo užtikrinimas**: Užtikrinti, kad visi komponentai atitiktų organizacijos saugumo ir reguliavimo reikalavimus

#### **Saugūs diegimo vamzdynai**  
- **Automatizuotas CI/CD saugumas**: Integruoti saugumo nuskaitymus visame automatizuotame diegimo procese
- **Artefaktų vientisumas**: Įgyvendinti kriptografinį patikrinimą visiems diegiamiems artefaktams (kodui, modeliams, konfigūracijoms)
- **Pakopinis diegimas**: Naudoti pažangias diegimo strategijas su saugumo patikrinimu kiekviename etape
- **Patikimos artefaktų saugyklos**: Diegti tik iš patikrintų, saugių artefaktų registrų ir saugyklų

#### **Nuolatinis stebėjimas ir reagavimas**
- **Priklausomybių nuskaitymas**: Nuolatinė pažeidžiamumų stebėsena visoms programinės įrangos ir DI komponentų priklausomybėms
- **Modelių stebėjimas**: Nuolatinis modelių elgsenos, našumo pokyčių ir saugumo anomalijų vertinimas
- **Paslaugų sveikatos sekimas**: Stebėti išorinių DI paslaugų prieinamumą, saugumo incidentus ir politikos pokyčius
- **Grėsmių žvalgybos integracija**: Integruoti grėsmių srautus, specifinius DI ir ML saugumo rizikoms

#### **Prieigos kontrolė ir minimalios privilegijos**
- **Komponentų lygių leidimai**: Riboti prieigą prie modelių, duomenų ir paslaugų pagal verslo poreikį
- **Paslaugų paskyrų valdymas**: Įgyvendinti specializuotas paslaugų paskyras su minimaliais reikalingais leidimais
- **Tinklo segmentavimas**: Izoliuoti DI komponentus ir riboti tinklo prieigą tarp paslaugų
- **API vartų kontrolė**: Naudoti centralizuotus API vartus prieigai prie išorinių DI paslaugų valdyti ir stebėti

#### **Incidentų valdymas ir atkūrimas**
- **Greitos reagavimo procedūros**: Nusistovėjusios taisyklės pažeistiems DI komponentams taisyti arba keisti
- **Kredencialų rotacija**: Automatizuotos sistemos slaptažodžiams, API raktams ir paslaugų kredencialams keisti
- **Atstatymo galimybės**: Greito sugrįžimo prie ankstesnių patikrintų DI komponentų versijų galimybė
- **Tiekimo grandinės pažeidimų atkūrimas**: Specialios procedūros reaguoti į aukštesnių lygių DI paslaugų kompromitavimą

### Microsoft saugumo įrankiai ir integracija

**GitHub Advanced Security** suteikia išsamią tiekimo grandinės apsaugą, įskaitant:
- **Slaptažodžių nuskaitymas**: Automatinis kredencialų, API raktų ir žetonų aptikimas saugyklose
- **Priklausomybių nuskaitymas**: Pažeidžiamumų vertinimas atvirojo kodo priklausomybėms ir bibliotekoms
- **CodeQL analizė**: Statinė kodo analizė dėl saugumo pažeidžiamumų ir programavimo klaidų
- **Tiekimo grandinės įžvalgos**: Matomumas į priklausomybių sveikatą ir saugumo būklę

**Azure DevOps ir Azure Repos integracija:**
- Sklandi saugumo nuskaitymo integracija per Microsoft kūrimo platformas
- Automatizuoti saugumo patikrinimai Azure vamzdynuose DI apkrovoms
- Politikos vykdymas saugiam DI komponentų diegimui

**Microsoft vidinės praktikos:**
Microsoft taiko plačias tiekimo grandinės saugumo praktikas visuose produktuose. Sužinokite apie patikrintas strategijas [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Pagrindinės saugumo gerosios praktikos

MCP įgyvendinimai paveldi ir papildo jūsų organizacijos esamą saugumo politiką. Pagrindinių saugumo praktikų stiprinimas ženkliai padidina bendrą DI sistemų ir MCP diegimų saugumą.

### Pagrindiniai saugumo pagrindai

#### **Saugios plėtros praktikos**
- **OWASP atitiktis**: Apsauga nuo [OWASP Top 10](https://owasp.org/www-project-top-ten/) žiniatinklio programų pažeidžiamumų
- **DI specifinės apsaugos**: Kontrolės įgyvendinimas pagal [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Saugus slaptažodžių valdymas**: Naudoti skirtas saugyklas žetonams, API raktams ir jautrioms konfigūracijos reikšmėms
- **End-to-End šifravimas**: Saugios komunikacijos įgyvendinimas visose programų sudedamosiose dalyse ir duomenų srautuose
- **Įvesties validavimas**: Griežta visų vartotojo įvesčių, API parametrų ir duomenų šaltinių validacija

#### **Infrastruktūros sutvirtinimas**
- **Daugelio veiksnių autentifikacija**: Privalomas MFA visoms administracinėms ir paslaugų paskyroms
- **Pleistrų valdymas**: Automatizuotas ir laiku atliekamas operacinių sistemų, karkasų ir priklausomybių atnaujinimas  
- **Tapatybės tiekėjo integracija**: Centralizuotas tapatybės valdymas per įmonių tapatybės tiekėjus (Microsoft Entra ID, Active Directory)
- **Tinklo segmentavimas**: Loginė MCP komponentų izoliacija siekiant riboti šoninį judėjimą
- **Mažiausių privilegijų principas**: Minimalūs reikalingi leidimai visiems sistemos komponentams ir paskyroms

#### **Saugumo stebėjimas ir aptikimas**
- **Išsami žurnalizacija**: Detalus DI programų veiklos, įskaitant MCP klientų-serverių sąveikas, žurnalas
- **SIEM integracija**: Centralizuota saugumo informacijos ir įvykių valdymo sistema anomalijoms aptikti
- **Elgsenos analizė**: DI varomas stebėjimas neįprastiems sistemų ir vartotojų elgesio modeliams aptikti
- **Grėsmių žvalgyba**: Išorinių grėsmių srautų ir kompromitavimo rodiklių (IOC) integracija
- **Incidentų reagavimas**: Aiškiai apibrėžtos procedūros saugumo incidentams aptikti, reaguoti ir atstatyti

#### **Nulinės pasitikėjimo architektūra**
- **Niekada nepasitikėti, visada patikrinkite**: Nuolatinis vartotojų, įrenginių ir tinklo jungčių patikrinimas
- **Mikrosegmentavimas**: Detalūs tinklo kontrolės mechanizmai, izoliuojantys atskirus darbo krūvius ir paslaugas
- **Tapatybės centriškas saugumas**: Saugumo politikos, pagrįstos patvirtintomis tapatybėmis, o ne tinklo vieta
- **Nuolatinis rizikos vertinimas**: Dinaminis saugumo pozicijos vertinimas pagal esamą kontekstą ir elgseną
- **Sąlyginė prieiga**: Prieigos kontrolės, kurios prisitaiko pagal rizikos veiksnius, vietą ir įrenginio patikimumą

### Įmonių integracijos modeliai

#### **Microsoft saugumo ekosistemos integracija**
- **Microsoft Defender for Cloud**: Išsami debesų saugumo būklės valdymo priemonė
- **Azure Sentinel**: Debesų pagrindu veikianti SIEM ir SOAR platforma DI apkrovų apsaugai
- **Microsoft Entra ID**: Įmonių tapatybės ir prieigos valdymas su sąlyginės prieigos politikomis
- **Azure Key Vault**: Centralizuotas slaptažodžių valdymas su aparatine saugumo modulių (HSM) parama
- **Microsoft Purview**: Duomenų valdymas ir atitiktis DI duomenų šaltiniams bei darbo srautams

#### **Atitiktis ir valdymas**
- **Reguliavimo laikymasis**: Užtikrinti, kad MCP įgyvendinimai atitiktų pramonės konkrečius atitikties reikalavimus (GDPR, HIPAA, SOC 2)

- **Duomenų klasifikavimas**: Tinkamas jautrių duomenų, tvarkomų dirbtinio intelekto sistemų, kategorizavimas ir tvarkymas
- **Auditavimo įrašai**: Išsamus registravimas reglamentiniam atitikties stebėjimui ir kriminalistinei analizei
- **Privatumo valdymas**: Privatumo pagal dizainą principų įgyvendinimas DI sistemos architektūroje
- **Pokyčių valdymas**: Formalūs procesai DI sistemos pakeitimų saugos peržiūroms

Šios pagrindinės praktikos sukuria tvirtą saugos bazę, kuri pagerina MCP specifinių saugumo priemonių efektyvumą ir užtikrina visapusišką apsaugą DI pagrindu veikiančioms programoms.

## Pagrindinės saugumo išvados

- **Sluoksniuota saugumo strategija**: Derinkite pagrindines saugumo praktikas (saugus kodavimas, mažiausios privilegijos, tiekimo grandinės patikra, nuolatinė stebėsena) su DI specifinėmis priemonėmis visapusiškai apsaugai

- **DI specifinė grėsmių aplinka**: MCP sistemos susiduria su unikaliomis rizikomis, tokiomis kaip užklausų injekcija, įrankių užnuodijimas, seansų pagrobimas, supainiotas tarpininkas, raktų perleidimo pažeidžiamumai ir per didelės teisės, kurios reikalauja specialių mažinimo priemonių

- **Autentifikacijos ir autorizacijos tobulumas**: Įgyvendinkite tvirtą autentifikaciją, naudojant išorinius tapatybės tiekėjus (Microsoft Entra ID), užtikrinkite tinkamą žetonų patvirtinimą ir niekada nepripažinkite žetonų, kurie aiškiai neišduoti jūsų MCP serveriui

- **DI atakų prevencija**: Naudokite Microsoft Prompt Shields ir Azure Content Safety, kad apsisaugotumėte nuo netiesioginės užklausų injekcijos ir įrankių užnuodijimo atakų, tuo pačiu tikrindami įrankių metaduomenis ir stebėdami dinamiškus pokyčius

- **Seansų ir transporto saugumas**: Naudokite kriptografiškai saugius, nenumatytus seansų ID, susietus su vartotojo tapatybėmis, įgyvendinkite tinkamą seansų gyvavimo ciklo valdymą ir niekada nenaudokite seansų autentifikacijai

- **OAuth saugos gerosios praktikos**: Užkirsti kelią supainioto tarpininko atakoms per aiškų vartotojo sutikimą dinamiškai registruotiems klientams, tinkamai įgyvendinti OAuth 2.1 su PKCE ir griežtai tikrinti persiuntimo URI  

- **Žetonų saugumo principai**: Venkite žetonų perleidimo antifunkcijų, tikrinkite žetonų auditorijos teiginius, naudokite trumpai galiojančius žetonus su saugiu rotavimu ir palaikykite aiškias pasitikėjimo ribas

- **Išsami tiekimo grandinės sauga**: Elkitės su visais DI ekosistemos komponentais (modeliais, įterpiniais, konteksto tiekėjais, išorinėmis API) taip pat atsargiai ir saugiai kaip su tradicinėmis programinės įrangos priklausomybėmis

- **Nuolatinė evoliucija**: Sekite MCP specifikacijų greitą kismą, prisidėkite prie saugumo bendruomenės standartų ir palaikykite adaptuojamas saugumo pozicijas protokolui bręstant

- **Microsoft saugumo integracija**: Naudokitės Microsoft išsamia saugumo ekosistema (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) MCP diegimo apsaugos stiprinimui

## Išsamūs ištekliai

### **Oficiali MCP saugumo dokumentacija**
- [MCP specifikacija (dabartinė: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP saugumo gerosios praktikos](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP autorizacijos specifikacija](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub saugykla](https://github.com/modelcontextprotocol)

### **OWASP MCP saugumo ištekliai**
- [OWASP MCP Azure saugumo vadovas](https://microsoft.github.io/mcp-azure-security-guide/) - Išsamios OWASP MCP Top 10 su Azure įgyvendinimo rekomendacijomis
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficialios OWASP MCP saugumo rizikos
- [MCP saugumo suvažiavimo dirbtuvės (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktiniai saugumo mokymai MCP Azure aplinkoje

### **Saugumo standartai ir gerosios praktikos**
- [OAuth 2.0 saugumo gerosios praktikos (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 interneto programų saugumas](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 dideliems kalbos modeliams](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft skaitmeninės gynybos ataskaita](https://aka.ms/mddr)

### **DI saugumo tyrimai ir analizė**
- [Užklausų injekcija MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Įrankių užnuodijimo atakos (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP saugumo tyrimų apžvalga (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft saugumo sprendimai**
- [Microsoft Prompt Shields dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety paslauga](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID sauga](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure žetonų valdymo gerosios praktikos](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Įgyvendinimo vadovai ir pamokos**
- [Azure API valdymas kaip MCP autentifikacijos vartai](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentifikacija MCP serveriuose](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Saugaus žetonų saugojimo ir šifravimo vaizdo įrašas](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps ir tiekimo grandinės saugumas**
- [Azure DevOps saugumas](https://azure.microsoft.com/products/devops)
- [Azure Repos saugumas](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft tiekimo grandinės saugumo kelionė](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Papildoma saugumo dokumentacija**

Išsamiam saugumo vadovui, žr. šiuos specializuotus dokumentus šiame skyriuje:

- **[CIMD ir DCR autorizacijos pavyzdys](./samples/cimd-dcr-auth/README.md)** - Veikiantis TypeScript MCP `2026-07-28` resursų serveris, lyginantis pageidaujamus Kliento ID metaduomenų dokumentus su pasenusiu dinaminės kliento registracijos pakaitalu
- **[MCP saugumo gerosios praktikos](./mcp-security-best-practices.md)** - Išsamios saugumo gerosios praktikos MCP įgyvendinimams
- **[Azure Content Safety įgyvendinimas](./azure-content-safety-implementation.md)** - Praktiniai Azure Content Safety integracijos pavyzdžiai  
- **[MCP saugumo kontrolių apžvalga](./mcp-security-controls.md)** - Naujausios saugumo kontrolės ir technikos MCP diegimams
- **[MCP gerųjų praktikų greitojo vadovo](./mcp-best-practices.md)** - Greitoji nuoroda esminėms MCP saugumo praktikoms
- **[BlueHat 2026: Ateities DI užtikrinimas: MCP apsauga daugiasluoksnėmis saugumo schemomis](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Gynybos daugelyje sluoksnių modeliai iš Microsoft Security Response Center (MSRC)

### **Praktiniai saugumo mokymai**

- **[MCP saugumo suvažiavimo dirbtuvės (Sherpa)](https://azure-samples.github.io/sherpa/)** - Išsamios praktinės dirbtuvės MCP serverių saugojimui Azure, su progresiniais mokymais nuo Bazinės stovyklos iki Suvažiavimo
- **[OWASP MCP Azure saugumo vadovas](https://microsoft.github.io/mcp-azure-security-guide/)** - Nuorodų architektūra ir įgyvendinimo gairės visoms OWASP MCP Top 10 rizikoms

---

## Kas toliau

Toliau: [3 skyrius: Pradžia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->