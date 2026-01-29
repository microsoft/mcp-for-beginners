# MCP Saugumas: Išsamus AI sistemų apsaugos sprendimas

[![MCP Security Best Practices](../../../translated_images/lt/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Saugumas yra pagrindinis AI sistemų projektavimo aspektas, todėl mes jam skiriame antrąją skyriaus vietą. Tai atitinka Microsoft principą **Saugumas pagal dizainą** iš [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Modelio konteksto protokolas (MCP) suteikia galingas naujas galimybes AI pagrįstoms programoms, tačiau kartu kelia unikalius saugumo iššūkius, kurie viršija tradicines programinės įrangos rizikas. MCP sistemos susiduria tiek su įprastomis saugumo problemomis (saugus kodavimas, mažiausių privilegijų principas, tiekimo grandinės saugumas), tiek su naujomis AI specifinėmis grėsmėmis, įskaitant užklausų injekciją, įrankių užnuodijimą, sesijų užgrobimą, painių tarpininkų atakas, žetonų perleidimo pažeidžiamumus ir dinaminį galimybių keitimą.

Šioje pamokoje nagrinėjamos svarbiausios saugumo rizikos MCP įgyvendinimuose – apimant autentifikaciją, autorizaciją, perteklines teises, netiesioginę užklausų injekciją, sesijų saugumą, painių tarpininkų problemas, žetonų valdymą ir tiekimo grandinės pažeidžiamumus. Sužinosite veiksmingas kontrolės priemones ir geriausias praktikas, kaip sumažinti šias rizikas, pasitelkdami Microsoft sprendimus, tokius kaip Prompt Shields, Azure Content Safety ir GitHub Advanced Security, stiprinant MCP diegimą.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- **Nustatyti MCP specifines grėsmes**: Atpažinti unikalius saugumo pavojus MCP sistemose, įskaitant užklausų injekciją, įrankių užnuodijimą, perteklines teises, sesijų užgrobimą, painių tarpininkų problemas, žetonų perleidimo pažeidžiamumus ir tiekimo grandinės rizikas
- **Taikyti saugumo kontrolę**: Įgyvendinti veiksmingas priemones, įskaitant tvirtą autentifikaciją, mažiausių privilegijų prieigą, saugų žetonų valdymą, sesijų saugumo kontrolę ir tiekimo grandinės patikrinimą
- **Pasinaudoti Microsoft saugumo sprendimais**: Suprasti ir diegti Microsoft Prompt Shields, Azure Content Safety ir GitHub Advanced Security MCP darbo krūvio apsaugai
- **Patvirtinti įrankių saugumą**: Suprasti įrankių metaduomenų patikros svarbą, stebėti dinamiškus pokyčius ir ginti nuo netiesioginės užklausų injekcijos atakų
- **Integruoti geriausias praktikas**: Derinti įprastus saugumo pagrindus (saugus kodavimas, serverių stiprinimas, nulinės pasitikėjimo modelis) su MCP specifinėmis kontrolėmis visapusiškai apsaugai

# MCP saugumo architektūra ir kontrolės

Šiuolaikiniai MCP įgyvendinimai reikalauja sluoksniuotos saugumo strategijos, apimančios tiek tradicinį programinės įrangos saugumą, tiek AI specifines grėsmes. Greitai besivystanti MCP specifikacija toliau tobulina saugumo kontrolę, leidžiančią geriau integruotis į įmonių saugumo architektūras ir įtvirtintas geriausias praktikas.

[Microsoft Digital Defense Report](https://aka.ms/mddr) tyrimai rodo, kad **98 % praneštų pažeidimų būtų užkirsti keliai taikant tvirtą saugumo higieną**. Efektyviausia apsaugos strategija derina pagrindines saugumo praktikas su MCP specifinėmis kontrolėmis – patikrintos bazinės saugumo priemonės išlieka svarbiausios bendros rizikos mažinimui.

## Dabartinė saugumo situacija

> **Pastaba:** Ši informacija atspindi MCP saugumo standartus nuo **2025 m. gruodžio 18 d.** MCP protokolas sparčiai vystosi, o būsimuose įgyvendinimuose gali atsirasti naujų autentifikacijos modelių ir patobulintų kontrolės priemonių. Visada kreipkitės į naujausią [MCP specifikaciją](https://spec.modelcontextprotocol.io/), [MCP GitHub saugyklą](https://github.com/modelcontextprotocol) ir [saugumo geriausių praktikų dokumentaciją](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) dėl naujausių nurodymų.

### MCP autentifikacijos evoliucija

MCP specifikacija reikšmingai pasikeitė autentifikacijos ir autorizacijos srityje:

- **Pradinis požiūris**: Ankstyvosios specifikacijos reikalavo kūrėjams įgyvendinti individualius autentifikacijos serverius, o MCP serveriai veikė kaip OAuth 2.0 autorizacijos serveriai, tiesiogiai valdantys vartotojų autentifikaciją
- **Dabartinis standartas (2025-11-25)**: Atnaujinta specifikacija leidžia MCP serveriams deleguoti autentifikaciją išoriniams tapatybės tiekėjams (pvz., Microsoft Entra ID), gerinant saugumo lygį ir mažinant įgyvendinimo sudėtingumą
- **Transporto sluoksnio saugumas**: Patobulinta saugaus transporto palaikymas su tinkamais autentifikacijos modeliais tiek vietiniams (STDIO), tiek nuotoliniams (Streamable HTTP) ryšiams

## Autentifikacijos ir autorizacijos saugumas

### Dabartiniai saugumo iššūkiai

Šiuolaikiniai MCP įgyvendinimai susiduria su keliomis autentifikacijos ir autorizacijos problemomis:

### Rizikos ir grėsmių vektoriai

- **Neteisingai sukonfigūruota autorizacijos logika**: Klaidinga autorizacijos įgyvendinimo MCP serveriuose gali atskleisti jautrius duomenis ir neteisingai taikyti prieigos kontrolę
- **OAuth žetonų kompromitavimas**: Vietinio MCP serverio žetonų vagystė leidžia užpuolikams apsimesti serveriais ir pasiekti tolesnes paslaugas
- **Žetonų perleidimo pažeidžiamumai**: Netinkamas žetonų tvarkymas sukuria saugumo kontrolės apeigas ir atsakomybės spragas
- **Perteklinės teisės**: Pernelyg plačios MCP serverių teisės pažeidžia mažiausių privilegijų principą ir plečia atakos paviršių

#### Žetonų perleidimas: kritinis anti-modelis

**Žetonų perleidimas yra griežtai draudžiamas** dabartinėje MCP autorizacijos specifikacijoje dėl rimtų saugumo pasekmių:

##### Saugumo kontrolės apeigos
- MCP serveriai ir tolesni API įgyvendina svarbias saugumo priemones (užklausų ribojimą, užklausų patikrinimą, srauto stebėjimą), kurios priklauso nuo tinkamo žetonų patvirtinimo
- Tiesioginis kliento žetonų naudojimas API apeina šias esmines apsaugas, silpnindamas saugumo architektūrą

##### Atsakomybės ir audito iššūkiai  
- MCP serveriai negali atskirti klientų, naudojančių aukštesnės grandies išduotus žetonus, todėl nutrūksta audito grandinės
- Tolesnių išteklių serverių žurnalai rodo klaidinančius užklausų šaltinius, o ne tikruosius MCP serverių tarpininkus
- Incidentų tyrimas ir atitikties auditas tampa žymiai sudėtingesni

##### Duomenų nutekėjimo rizikos
- Nepatikrinti žetonų teiginiai leidžia piktavaliams su pavogtais žetonais naudoti MCP serverius kaip tarpininkus duomenų nutekėjimui
- Pasitikėjimo ribų pažeidimai leidžia neautorizuotą prieigą, apeinant numatytas saugumo priemones

##### Daugiapaslauginių atakų vektoriai
- Kompromituoti žetonai, priimami kelių paslaugų, leidžia judėti šonine kryptimi per susietas sistemas
- Pasitikėjimo prielaidos tarp paslaugų gali būti pažeistos, kai žetonų kilmė negali būti patvirtinta

### Saugumo kontrolės ir rizikos mažinimas

**Svarbiausi saugumo reikalavimai:**

> **PRIVALOMA**: MCP serveriai **NETURI** priimti jokių žetonų, kurie nebuvo aiškiai išduoti MCP serveriui

#### Autentifikacijos ir autorizacijos kontrolės

- **Griežtas autorizacijos peržiūrėjimas**: Atlikti išsamius MCP serverių autorizacijos logikos auditą, kad tik numatyti vartotojai ir klientai galėtų pasiekti jautrius išteklius
  - **Įgyvendinimo vadovas**: [Azure API Management kaip autentifikacijos vartai MCP serveriams](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Tapatybės integracija**: [Microsoft Entra ID naudojimas MCP serverių autentifikacijai](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Saugus žetonų valdymas**: Įgyvendinti [Microsoft žetonų patvirtinimo ir gyvavimo ciklo geriausias praktikas](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Patikrinti, ar žetonų auditorijos teiginiai atitinka MCP serverio tapatybę
  - Įgyvendinti tinkamą žetonų rotaciją ir galiojimo laiką
  - Užkirsti kelią žetonų pakartotiniam naudojimui ir neautorizuotam naudojimui

- **Apsaugotas žetonų saugojimas**: Užtikrinti žetonų saugojimą su šifravimu tiek ramybės būsenoje, tiek perdavimo metu
  - **Geriausios praktikos**: [Saugus žetonų saugojimas ir šifravimo gairės](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Prieigos kontrolės įgyvendinimas

- **Mažiausių privilegijų principas**: Suteikti MCP serveriams tik minimalias teises, reikalingas numatytai funkcijai
  - Reguliarūs teisių peržiūros ir atnaujinimai, siekiant išvengti privilegijų plėtros
  - **Microsoft dokumentacija**: [Saugus mažiausių privilegijų prieigos valdymas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rolėmis pagrįsta prieigos kontrolė (RBAC)**: Įgyvendinti smulkiai sukonstruotas rolės priskyrimo taisykles
  - Riboti roles konkretiems ištekliams ir veiksmams
  - Vengti plačių ar nereikalingų teisių, kurios plečia atakos paviršių

- **Nuolatinis teisių stebėjimas**: Įgyvendinti nuolatinį prieigos auditą ir stebėjimą
  - Stebėti teisių naudojimo modelius dėl anomalijų
  - Greitai šalinti perteklines ar nenaudojamas teises

## AI specifinės saugumo grėsmės

### Užklausų injekcija ir įrankių manipuliavimo atakos

Šiuolaikiniai MCP įgyvendinimai susiduria su sudėtingais AI specifiniais atakų vektoriais, kurių tradicinės saugumo priemonės negali visiškai užkirsti kelio:

#### **Netiesioginė užklausų injekcija (tarpdomeninė užklausų injekcija)**

**Netiesioginė užklausų injekcija** yra viena iš kritiškiausių pažeidžiamybių MCP palaikomose AI sistemose. Užpuolikai įterpia piktavališkas instrukcijas į išorinį turinį – dokumentus, tinklalapius, el. laiškus ar duomenų šaltinius, kuriuos AI sistemos vėliau apdoroja kaip teisėtas komandas.

**Atakų scenarijai:**
- **Dokumentų pagrindu atliekama injekcija**: Piktavališkos instrukcijos paslėptos apdorojamuose dokumentuose, kurios sukelia nepageidaujamas AI veiklas
- **Interneto turinio išnaudojimas**: Pažeisti tinklalapiai su įterptomis užklausomis, kurios manipuliuoja AI elgsena, kai jos yra nuskaitytos
- **El. pašto atakos**: Piktavališkos užklausos el. laiškuose, kurios verčia AI asistentus nutekinti informaciją arba atlikti neautorizuotas veiklas
- **Duomenų šaltinių užteršimas**: Pažeistos duomenų bazės ar API, tiekiantys užterštą turinį AI sistemoms

**Reali įtaka**: Šios atakos gali sukelti duomenų nutekėjimą, privatumo pažeidimus, žalingo turinio generavimą ir vartotojų sąveikos manipuliavimą. Išsamiai analizuokite [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/lt/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Įrankių užnuodijimo atakos**

**Įrankių užnuodijimas** taikosi į MCP įrankių metaduomenis, išnaudodamas, kaip LLM interpretuoja įrankių aprašymus ir parametrus priimant vykdymo sprendimus.

**Atakų mechanizmai:**
- **Metaduomenų manipuliavimas**: Užpuolikai įterpia piktavališkas instrukcijas į įrankių aprašymus, parametrų apibrėžimus ar naudojimo pavyzdžius
- **Nematomi nurodymai**: Paslėptos užklausos įrankių metaduomenyse, kurias apdoroja AI modeliai, bet jų nemato žmonės
- **Dinaminis įrankių keitimas („Rug Pulls“) **: Vartotojų patvirtinti įrankiai vėliau modifikuojami vykdyti piktavališkas veiklas be vartotojų žinios
- **Parametrų injekcija**: Piktavališkas turinys įterpiamas į įrankių parametrų schemas, paveikiant modelio elgseną

**Nuotolinių serverių rizikos**: Nuotoliniai MCP serveriai kelia didesnę riziką, nes įrankių apibrėžimai gali būti atnaujinami po pradinio vartotojo patvirtinimo, sukuriant situacijas, kai anksčiau saugūs įrankiai tampa piktavališki. Išsamiai analizuokite [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/lt/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Papildomi AI atakų vektoriai**

- **Tarpdomeninė užklausų injekcija (XPIA)**: Sudėtingos atakos, kurios naudoja turinį iš kelių domenų, kad apeitų saugumo kontrolę
- **Dinaminis galimybių keitimas**: Realaus laiko įrankių galimybių pokyčiai, kurie išvengia pradinės saugumo analizės
- **Konteksto lango užnuodijimas**: Atakos, manipuliuojančios dideliais konteksto langais, kad paslėptų piktavališkas instrukcijas
- **Modelio painiavos atakos**: Išnaudojant modelio ribotumus kuriant nenuspėjamą ar nesaugų elgesį

### AI saugumo rizikos poveikis

**Didelės įtakos pasekmės:**
- **Duomenų nutekėjimas**: Neautorizuota prieiga ir jautrių įmonių ar asmeninių duomenų vagystė
- **Privatumo pažeidimai**: Asmens identifikuojamos informacijos (PII) ir konfidencialių verslo duomenų atskleidimas  
- **Sistemų manipuliavimas**: Netikėti kritinių sistemų ir darbo procesų pakeitimai
- **Prisijungimo duomenų vagystė**: Autentifikacijos žetonų ir paslaugų kredencialų kompromitavimas
- **Šoninė judėjimo galimybė**: Kompromituotų AI sistemų naudojimas platesnėms tinklo atakoms

### Microsoft AI saugumo sprendimai

#### **AI Prompt Shields: pažangi apsauga nuo injekcijos atakų**

Microsoft **AI Prompt Shields** suteikia išsamią apsaugą nuo tiesioginių ir netiesioginių užklausų injekcijos atakų per kelis saugumo sluoksnius:

##### **Pagrindiniai apsaugos mechanizmai:**

1. **Pažangi aptikimo ir filtravimo sistema**
   - Mašininio mokymosi algoritmai ir NLP metodai aptinka piktavališkas instrukcijas išoriniame turinyje
   - Realaus laiko dokumentų, tinklalapių, el. laiškų ir duomenų šaltinių analizė dėl įterptų grėsmių
   - Kontekstinis teisėtų ir piktavališkų užklausų modelių supratimas

2. **Išskyrimo technikos**  
   - Skiria patikimas sistemos instrukcijas nuo galimai pažeistų išorinių įvesties duomenų
   - Teksto transformavimo metodai, kurie pagerina modelio aktualumą ir izoliuoja piktavališką turinį
   - Padeda AI sistemoms išlaikyti tinkamą instrukcijų hierarchiją ir ignoruoti įterptas komandas

3. **Ribų ir duomenų žymėjimo sistemos**
   - Aiškus ribų apibrėžimas tarp patikimų sistemos pranešimų ir išorinio įvesties teksto
   - Specialūs žymekliai, paryškinantys ribas tarp patikimų ir nepatikimų duomenų šaltinių
   - Aiškus atskyrimas neleidžia painiavos instrukcijose ir neautorizuotam komandų vykdymui

4. **Nuolatinė grėsmių žvalgyba**
   - Microsoft nuolat stebi naujus atakų modelius ir atnaujina apsaugas
   - Proaktyvus grėsmių paieškos darbas dėl naujų injekcijos technikų ir atakų vektorių
   - Reguliarūs saugumo modelių atnaujinimai, siekiant išlaikyti efektyvumą prieš kintančias grėsmes

5. **Azure Content Safety integracija**
   - Dalis išsamios Azure AI turinio saugumo rinkinio
   - Papildomas aptikimas dėl jailbreak bandymų, žalingo turinio ir saugumo politikos pažeidimų
   - Vieningos saugumo kontrolės per AI programų komponentus

**Įgyvendinimo ištekliai**: [Microsoft Prompt Shields dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/lt/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Pažangios MCP saugumo grėsmės

### Sesijų užgrobimo pažeidžiamumai

**Sesijų užgrobimas** yra kritinis atakos vektorius būseną palaikančiuose MCP įgyvendinimuose, kai neautorizuotos šalys įgyja ir piktnaudžiauja teisėtais sesijos identifikatoriais, apsimesdamos klientais ir vykdydamos neautorizuotas veiklas.

#### **Atakų scenarijai ir rizikos**

- **Sesijos užgrobimo užklausų injekcija**: Užpuolikai su pavogtais sesijos ID įterpia piktavališkus įvykius į serverius, dalijančius sesijos būseną, galimai sukeldami žalingas veiklas arba pasiekiant jautrius duomenis
- **Tiesioginė apsimetimo ataka**: Pavogti sesijos ID leidžia tiesioginius MCP serverio kvietimus, apeinant autentifikaciją ir traktuojant užpuolikus kaip teisėtus vartotojus
- **Kompromituoti tęstinių srautų nutraukimai**: Užpuolikai gali anksti nutraukti užklausas, priversdami teisėtus klientus tęsti su galimai piktavališku turiniu

#### **Sesijų valdymo saugumo kontrolės**

**Svarbūs reikalavimai:**
- **Autorizacijos patikra**: MCP serveriai, įgyvendinantys autorizaciją, **PRIVALO** patikrinti VISUS įeinančius užklausimus ir **NETURI** pasikliauti sesijomis autentifikacijai
- **Saugus sesijos generavimas**: Naudokite kriptografiškai saugius, nedeterministinius sesijos ID, sugeneruotus naudojant saugius atsitiktinių skaičių generatorius
- **Vartotojui specifinis susiejimas**: Susiekite sesijos ID su vartotojui specifine informacija, naudodami formatus, tokius kaip `<user_id>:<session_id>`, kad būtų išvengta sesijų piktnaudžiavimo tarp vartotojų
- **Sesijos gyvavimo ciklo valdymas**: Įgyvendinkite tinkamą galiojimo pabaigą, rotaciją ir nebegaliojimą, kad sumažintumėte pažeidžiamumo langus
- **Transporto saugumas**: Privalomas HTTPS visai komunikacijai, kad būtų išvengta sesijos ID perėmimo

### Supainioto įgaliotojo problema

**Supainioto įgaliotojo problema** kyla, kai MCP serveriai veikia kaip autentifikacijos tarpininkai tarp klientų ir trečiųjų šalių paslaugų, sukurdami galimybes apeiti autorizaciją naudojant statinius kliento ID.

#### **Atakos mechanika ir rizikos**

- **Sutikimo apeinimas naudojant slapukus**: Ankstesnė vartotojo autentifikacija sukuria sutikimo slapukus, kuriuos užpuolikai išnaudoja siunčiant kenkėjiškus autorizacijos užklausimus su sukonstruotais peradresavimo URI
- **Autorizacijos kodo vagystė**: Esami sutikimo slapukai gali priversti autorizacijos serverius praleisti sutikimo ekranus ir nukreipti kodus į užpuoliko valdomus galinius taškus  
- **Neautorizuotas API prieigos gavimas**: Pavogti autorizacijos kodai leidžia keistis žetonais ir apsimesti vartotoju be aiškaus leidimo

#### **Sumažinimo strategijos**

**Privalomi valdikliai:**
- **Aiškus sutikimo reikalavimas**: MCP tarpiniai serveriai, naudojantys statinius kliento ID, **PRIVALO** gauti vartotojo sutikimą kiekvienam dinamiškai registruotam klientui
- **OAuth 2.1 saugumo įgyvendinimas**: Laikytis dabartinių OAuth saugumo geriausių praktikų, įskaitant PKCE (Proof Key for Code Exchange) visoms autorizacijos užklausoms
- **Griežta kliento patikra**: Įgyvendinti griežtą peradresavimo URI ir kliento identifikatorių patikrą, kad būtų išvengta piktnaudžiavimo

### Žetonų praleidimo pažeidžiamumai  

**Žetonų praleidimas** yra aiškus anti-pavyzdys, kai MCP serveriai priima kliento žetonus be tinkamos patikros ir perduoda juos žemyn srautui API, pažeisdami MCP autorizacijos specifikacijas.

#### **Saugumo pasekmės**

- **Kontrolės apeinimas**: Tiesioginis kliento žetonų naudojimas API apeina svarbius ribojimus, patikras ir stebėjimo valdiklius
- **Auditavimo takų sugadinimas**: Iš viršaus išduoti žetonai neleidžia identifikuoti kliento, todėl neįmanoma tirti incidentų
- **Tarpinio serverio duomenų nutekėjimas**: Nepatikrinti žetonai leidžia kenkėjiškiems veikėjams naudoti serverius kaip tarpininkus neautorizuotam duomenų prieinamumui
- **Pasitikėjimo ribų pažeidimai**: Žemyn srauto paslaugų pasitikėjimo prielaidos gali būti pažeistos, kai negalima patvirtinti žetono kilmės
- **Daugiapaslaugės atakos plėtra**: Kompromituoti žetonai, priimami keliuose paslaugų taškuose, leidžia judėti šonine kryptimi

#### **Reikalaujami saugumo valdikliai**

**Nesuderinami reikalavimai:**
- **Žetonų patikra**: MCP serveriai **NETURI** priimti žetonų, kurie nėra aiškiai išduoti MCP serveriui
- **Auditorijos patikra**: Visada tikrinkite, ar žetono auditorijos teiginiai atitinka MCP serverio tapatybę
- **Tinkamas žetono gyvavimo ciklas**: Įgyvendinkite trumpalaikius prieigos žetonus su saugia rotacija


## Tiekimo grandinės saugumas AI sistemoms

Tiekimo grandinės saugumas išsiplėtė nuo tradicinių programinės įrangos priklausomybių iki visos AI ekosistemos. Šiuolaikiniai MCP įgyvendinimai privalo griežtai tikrinti ir stebėti visas su AI susijusias sudedamąsias dalis, nes kiekviena gali įvesti pažeidžiamumų, galinčių pakenkti sistemos vientisumui.

### Išplėstiniai AI tiekimo grandinės komponentai

**Tradicinės programinės įrangos priklausomybės:**
- Atvirojo kodo bibliotekos ir karkasai
- Konteinerių vaizdai ir bazinės sistemos  
- Kūrimo įrankiai ir kūrimo vamzdynai
- Infrastruktūros komponentai ir paslaugos

**AI specifiniai tiekimo grandinės elementai:**
- **Pagrindiniai modeliai**: Iš anksto apmokyti modeliai iš įvairių tiekėjų, kuriems reikalinga kilmės patikra
- **Įterpimo paslaugos**: Išorinės vektorizacijos ir semantinio paieškos paslaugos
- **Konteksto tiekėjai**: Duomenų šaltiniai, žinių bazės ir dokumentų saugyklos  
- **Trečiųjų šalių API**: Išorinės AI paslaugos, ML vamzdynai ir duomenų apdorojimo galiniai taškai
- **Modelių artefaktai**: Svoriai, konfigūracijos ir smulkiai pritaikyti modelių variantai
- **Mokymo duomenų šaltiniai**: Duomenų rinkiniai, naudojami modelių mokymui ir pritaikymui

### Išsami tiekimo grandinės saugumo strategija

#### **Komponentų patikra ir pasitikėjimas**
- **Kilmės patikra**: Patikrinkite visų AI komponentų kilmę, licencijavimą ir vientisumą prieš integraciją
- **Saugumo vertinimas**: Atlikite pažeidžiamumo skenavimą ir saugumo peržiūras modeliams, duomenų šaltiniams ir AI paslaugoms
- **Reputacijos analizė**: Įvertinkite AI paslaugų tiekėjų saugumo istoriją ir praktiką
- **Atitikties patikra**: Užtikrinkite, kad visi komponentai atitiktų organizacijos saugumo ir reguliavimo reikalavimus

#### **Saugūs diegimo vamzdynai**  
- **Automatizuotas CI/CD saugumas**: Integruokite saugumo skenavimą visame automatizuotame diegimo vamzdyne
- **Artefaktų vientisumas**: Įgyvendinkite kriptografinę patikrą visiems diegiamiems artefaktams (kodas, modeliai, konfigūracijos)
- **Pakopinis diegimas**: Naudokite progresyvias diegimo strategijas su saugumo patikra kiekviename etape
- **Patikimos artefaktų saugyklos**: Diegti tik iš patikrintų, saugių artefaktų registrų ir saugyklų

#### **Nuolatinis stebėjimas ir reagavimas**
- **Priklausomybių skenavimas**: Nuolatinis pažeidžiamumo stebėjimas visoms programinės įrangos ir AI komponentų priklausomybėms
- **Modelių stebėjimas**: Nuolatinis modelių elgesio, našumo svyravimų ir saugumo anomalijų vertinimas
- **Paslaugų sveikatos stebėjimas**: Stebėkite išorines AI paslaugas dėl prieinamumo, saugumo incidentų ir politikos pokyčių
- **Grėsmių žvalgybos integracija**: Įtraukite grėsmių srautus, specifinius AI ir ML saugumo rizikoms

#### **Prieigos kontrolė ir mažiausios privilegijos principas**
- **Komponentų lygmens leidimai**: Ribokite prieigą prie modelių, duomenų ir paslaugų pagal verslo poreikį
- **Paslaugų paskyrų valdymas**: Įgyvendinkite specialias paslaugų paskyras su minimaliais reikalingais leidimais
- **Tinklo segmentavimas**: Izoliuokite AI komponentus ir ribokite tinklo prieigą tarp paslaugų
- **API vartų kontrolė**: Naudokite centralizuotus API vartus prieigos prie išorinių AI paslaugų kontrolei ir stebėjimui

#### **Incidentų valdymas ir atkūrimas**
- **Greito reagavimo procedūros**: Nustatytos procedūros pažeistų AI komponentų taisymui ar keitimui
- **Prisijungimo duomenų rotacija**: Automatizuotos sistemos slaptumams, API raktams ir paslaugų kredencialams keisti
- **Atstatymo galimybės**: Galimybė greitai grįžti prie ankstesnių patikrintų AI komponentų versijų
- **Tiekimo grandinės pažeidimų atkūrimas**: Specifinės procedūros reagavimui į aukštesnio lygio AI paslaugų kompromitavimą

### Microsoft saugumo įrankiai ir integracija

**GitHub Advanced Security** suteikia išsamų tiekimo grandinės apsaugą, įskaitant:
- **Slaptumų skenavimas**: Automatizuotas kredencialų, API raktų ir žetonų aptikimas saugyklose
- **Priklausomybių skenavimas**: Pažeidžiamumo vertinimas atvirojo kodo priklausomybėms ir bibliotekoms
- **CodeQL analizė**: Statinė kodo analizė saugumo pažeidžiamumams ir programavimo klaidoms
- **Tiekimo grandinės įžvalgos**: Matomumas priklausomybių sveikatai ir saugumo būklei

**Azure DevOps ir Azure Repos integracija:**
- Sklandi saugumo skenavimo integracija Microsoft kūrimo platformose
- Automatizuotos saugumo patikros Azure vamzdynuose AI darbo krūviams
- Politikos vykdymas saugiam AI komponentų diegimui

**Microsoft vidinės praktikos:**
Microsoft įgyvendina plačias tiekimo grandinės saugumo praktikas visuose produktuose. Sužinokite apie patikrintus metodus [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Pagrindinės saugumo gerosios praktikos

MCP įgyvendinimai paveldi ir plečia jūsų organizacijos esamą saugumo poziciją. Pagrindinių saugumo praktikų stiprinimas žymiai pagerina bendrą AI sistemų ir MCP diegimų saugumą.

### Pagrindiniai saugumo principai

#### **Saugus kūrimas**
- **OWASP atitiktis**: Apsauga nuo [OWASP Top 10](https://owasp.org/www-project-top-ten/) žiniatinklio programų pažeidžiamumų
- **AI specifinės apsaugos**: Įgyvendinkite valdiklius pagal [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Saugus slaptumų valdymas**: Naudokite specialias saugyklas žetonams, API raktams ir jautriems konfigūracijos duomenims
- **End-to-end šifravimas**: Įgyvendinkite saugią komunikaciją visuose programos komponentuose ir duomenų srautuose
- **Įvesties patikra**: Griežta visų vartotojo įvesties, API parametrų ir duomenų šaltinių patikra

#### **Infrastruktūros stiprinimas**
- **Daugiaveiksmė autentifikacija**: Privaloma MFA visoms administravimo ir paslaugų paskyroms
- **Atnaujinimų valdymas**: Automatizuotas, laiku atliekamas operacinių sistemų, karkasų ir priklausomybių atnaujinimas  
- **Tapatybės tiekėjo integracija**: Centralizuotas tapatybės valdymas per įmonių tapatybės tiekėjus (Microsoft Entra ID, Active Directory)
- **Tinklo segmentavimas**: Logiška MCP komponentų izoliacija, ribojanti šoninį judėjimą
- **Mažiausių privilegijų principas**: Minimalūs reikalingi leidimai visiems sistemos komponentams ir paskyroms

#### **Saugumo stebėjimas ir aptikimas**
- **Išsamus žurnalas**: Detalus AI programų veiklos žurnalas, įskaitant MCP klientų-serverių sąveikas
- **SIEM integracija**: Centralizuota saugumo informacijos ir įvykių valdymo sistema anomalijų aptikimui
- **Elgesio analizė**: AI pagrįstas stebėjimas neįprastų sistemų ir vartotojų elgesio modelių aptikimui
- **Grėsmių žvalgyba**: Išorinių grėsmių srautų ir kompromitavimo indikatorių (IOC) integracija
- **Incidentų valdymas**: Aiškiai apibrėžtos procedūros saugumo incidentų aptikimui, reagavimui ir atkūrimui

#### **Nulinės pasitikėjimo architektūra**
- **Niekada nepasitikėk, visada tikrink**: Nuolatinis vartotojų, įrenginių ir tinklo ryšių patikrinimas
- **Mikrosegmentacija**: Smulkūs tinklo valdikliai, izoliuojantys atskirus darbo krūvius ir paslaugas
- **Tapatybe pagrįstas saugumas**: Saugumo politikos, pagrįstos patvirtintomis tapatybėmis, o ne tinklo vieta
- **Nuolatinė rizikos vertinimas**: Dinaminis saugumo pozicijos vertinimas pagal esamą kontekstą ir elgesį
- **Sąlyginė prieiga**: Prieigos valdikliai, prisitaikantys pagal rizikos veiksnius, vietą ir įrenginio pasitikėjimą

### Įmonių integracijos modeliai

#### **Microsoft saugumo ekosistemos integracija**
- **Microsoft Defender for Cloud**: Išsamus debesų saugumo pozicijos valdymas
- **Azure Sentinel**: Debesų gimtoji SIEM ir SOAR galimybės AI darbo krūvių apsaugai
- **Microsoft Entra ID**: Įmonių tapatybės ir prieigos valdymas su sąlyginės prieigos politikomis
- **Azure Key Vault**: Centralizuotas slaptumų valdymas su aparatine saugumo modulių (HSM) parama
- **Microsoft Purview**: Duomenų valdymas ir atitiktis AI duomenų šaltiniams ir darbo srautams

#### **Atitiktis ir valdymas**
- **Reguliavimo atitikimas**: Užtikrinkite, kad MCP įgyvendinimai atitiktų pramonės specifinius atitikties reikalavimus (GDPR, HIPAA, SOC 2)
- **Duomenų klasifikavimas**: Tinkama jautrių duomenų, apdorojamų AI sistemose, kategorizacija ir tvarkymas
- **Auditavimo takai**: Išsamus žurnalas reguliavimo atitikčiai ir teismo tyrimams
- **Privatumo valdikliai**: Privatumo pagal dizainą principų įgyvendinimas AI sistemos architektūroje
- **Pokyčių valdymas**: Formalios saugumo peržiūros procedūros AI sistemos pakeitimams

Šios pagrindinės praktikos sukuria tvirtą saugumo pagrindą, kuris pagerina MCP specifinių saugumo valdiklių efektyvumą ir suteikia išsamią apsaugą AI pagrįstoms programoms.

## Pagrindinės saugumo išvados

- **Sluoksniuota saugumo strategija**: Derinkite pagrindines saugumo praktikas (saugus kodavimas, mažiausios privilegijos, tiekimo grandinės patikra, nuolatinis stebėjimas) su AI specifiniais valdikliais visapusiškai apsaugai

- **AI specifinė grėsmių aplinka**: MCP sistemos susiduria su unikaliomis rizikomis, įskaitant užklausų injekciją, įrankių užnuodijimą, sesijų užgrobimą, supainioto įgaliotojo problemas, žetonų praleidimo pažeidžiamumus ir perteklines teises, kurioms reikalingos specializuotos mažinimo priemonės

- **Autentifikacijos ir autorizacijos meistriškumas**: Įgyvendinkite tvirtą autentifikaciją naudojant išorinius tapatybės tiekėjus (Microsoft Entra ID), užtikrinkite tinkamą žetonų patikrą ir niekada nepriimkite žetonų, kurie nėra aiškiai išduoti jūsų MCP serveriui

- **AI atakų prevencija**: Diegkite Microsoft Prompt Shields ir Azure Content Safety, kad apsisaugotumėte nuo netiesioginės užklausų injekcijos ir įrankių užnuodijimo atakų, kartu tikrindami įrankių metaduomenis ir stebėdami dinamiškus pokyčius

- **Sesijų ir transporto saugumas**: Naudokite kriptografiškai saugius, nedeterministinius sesijos ID, susietus su vartotojo tapatybėmis, įgyvendinkite tinkamą sesijos gyvavimo ciklo valdymą ir niekada nenaudokite sesijų autentifikacijai

- **OAuth saugumo gerosios praktikos**: Užkirsti kelią supainioto įgaliotojo atakoms per aiškų vartotojo sutikimą dinamiškai registruotiems klientams, tinkamą OAuth 2.1 įgyvendinimą su PKCE ir griežtą peradresavimo URI patikrą  

- **Žetonų saugumo principai**: Venkite žetonų praleidimo anti-pavyzdžių, tikrinkite žetono auditorijos teiginius, įgyvendinkite trumpalaikius žetonus su saugia rotacija ir palaikykite aiškias pasitikėjimo ribas

- **Išsamus tiekimo grandinės saugumas**: Visus AI ekosistemos komponentus (modelius, įterpimus, konteksto tiekėjus, išorinius API) vertinkite su tokia pačia saugumo griežtimi kaip tradicines programinės įrangos priklausomybes

- **Nuolatinė evoliucija**: Sekite sparčiai besivystančias MCP specifikacijas, prisidėkite prie saugumo bendruomenės standartų ir palaikykite adaptuotą saugumo poziciją, kai protokolas bręsta

- **Microsoft saugumo integracija**: Pasinaudokite Microsoft išsamia saugumo ekosistema (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) geresnei MCP diegimo apsaugai

## Išsamūs ištekliai

### **Oficiali MCP saugumo dokumentacija**
- [MCP specifikacija (dabartinė: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP saugumo gerosios praktikos](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP autorizacijos specifikacija](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub saugykla](https://github.com/modelcontextprotocol)

### **Saugumo standartai ir gerosios praktikos**
- [OAuth 2.0 saugumo gerosios praktikos (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 žiniatinklio programų saugumas](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 dideliems kalbos modeliams](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft skaitmeninės gynybos ataskaita](https://aka.ms/mddr)

### **AI saugumo tyrimai ir analizė**
- [Užklausų injekcija MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Įrankių užnuodijimo atakos (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP saugumo tyrimų apžvalga (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft saugumo sprendimai**
- [Microsoft Prompt Shields dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure turinio saugos paslauga](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID saugumas](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure žetonų valdymo geriausios praktikos](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub pažangus saugumas](https://github.com/security/advanced-security)

### **Įgyvendinimo vadovai ir pamokos**
- [Azure API valdymas kaip MCP autentifikacijos vartai](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentifikacija su MCP serveriais](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Saugus žetonų saugojimas ir šifravimas (vaizdo įrašas)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps ir tiekimo grandinės saugumas**
- [Azure DevOps saugumas](https://azure.microsoft.com/products/devops)
- [Azure Repos saugumas](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft tiekimo grandinės saugumo kelionė](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Papildoma saugumo dokumentacija**

Išsamiai saugumo gairėms žr. šiuos specializuotus dokumentus šiame skyriuje:

- **[MCP saugumo geriausios praktikos 2025](./mcp-security-best-practices-2025.md)** - Išsamios MCP įgyvendinimo saugumo geriausios praktikos
- **[Azure turinio saugos įgyvendinimas](./azure-content-safety-implementation.md)** - Praktiniai Azure turinio saugos integracijos pavyzdžiai  
- **[MCP saugumo kontrolės 2025](./mcp-security-controls-2025.md)** - Naujausios MCP diegimo saugumo kontrolės ir metodai
- **[MCP geriausių praktikų greita nuoroda](./mcp-best-practices.md)** - Greitos nuorodos vadovas esminėms MCP saugumo praktikoms

---

## Kas toliau

Toliau: [3 skyrius: Pradžia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->