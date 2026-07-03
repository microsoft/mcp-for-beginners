# MCP turvalisus: põhjalik kaitse tehisintellekti süsteemidele

[![MCP turvalisuse parimad tavad](../../../translated_images/et/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klõpsake ülaltoodud pildil, et vaadata selle õppetunni videot)_

Turvalisus on AI süsteemide kujunduse aluseks, mistõttu on see meie teine peatükk ja eelistatud teema. See on kooskõlas Microsofti põhimõttega **Secure by Design** [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/) raames.

Model Context Protocol (MCP) pakub võimsaid uusi võimalusi AI-põhistele rakendustele, tuues samas kaasa unikaalseid turvalisuse väljakutseid, mis ulatuvad traditsioonilistest tarkvara riskidest kaugemale. MCP süsteemid seisavad silmitsi nii tuntud turvariskidega (ohutu kodeerimine, minimaalne õiguste tase, tarneahela turvalisus) kui ka uute AI-spetsiifiliste ohtudega, sealhulgas promptide süstimine, tööriistade mürgitamine, sessiooni kaaperdamine, segadusse sattunud asetäitjate rünnakud, märgiste edastamise haavatavused ja dünaamilised võimete muutmised.

See õppetund käsitleb kõige kriitilisemaid turvariske MCP rakendustes — hõlmates autentimist, autoriseerimist, liigselt laialdasi õigusi, kaudset promptide süstimist, sessiooni turvalisust, segadusse sattunud asetäitjate probleeme, märgihaldust ja tarneahela haavatavusi. Õpite rakendatavaid kontrollimeetmeid ja parimaid tavasid nende riskide maandamiseks samal ajal Microsofti lahenduste kasutamise kaudu, nagu Prompt Shields, Azure Content Safety ja GitHub Advanced Security, et tugevdada oma MCP juurutust.

## Õpieesmärgid

Selle õppetunni lõpuks suudate:

- **Tuua välja MCP-spetsiifilised ohud**: Tuvastada MCP süsteemidele omaseid turvariske, sealhulgas promptide süstimine, tööriistade mürgitamine, liigsed õigused, sessiooni kaaperdamine, segadusse sattunud asetäitjate probleemid, märgiste edastamise haavatavused ja tarneahela ohud
- **Rakendada turvakontrollid**: Kasutada tõhusaid leevendusmeetmeid, sealhulgas tugevat autentimist, minimaalset õiguste taset, turvalist märgihaldust, sessiooni turvaelemente ja tarneahela kontrolli
- **Kasutada Microsofti turvalahendusi**: Mõista ja paigaldada Microsoft Prompt Shields, Azure Content Safety ja GitHub Advanced Security MCP töökoormuse kaitseks
- **Valideerida tööriistade turvalisust**: Mõista tööriista metaandmete valideerimise tähtsust, jälgida dünaamilisi muudatusi ja kaitsta kaudsete promptide süstimise rünnakute eest
- **Integreerida parimad tavad**: Ühendada kehtivad turvalisuse aluspõhimõtted (ohutu kodeerimine, serveri tugevdamine, nullusaldusmudel) MCP-spetsiifiliste kontrollidega terviklikuks kaitseks

# MCP turvaarhitektuur ja kontrollid

Kaasaegsed MCP rakendused vajavad kihistatud turvalahendusi, mis katavad nii traditsioonilise tarkvara turvalisuse kui ka AI-spetsiifilised ohud. Kiiresti arenev MCP spetsifikatsioon arendab edasi oma turvakontrolle, võimaldades paremat integreerimist ettevõtte turvaarhitektuuridega ja kehtestatud parimate tavadega.

[Microsofti digitaalse kaitse aruande](https://aka.ms/mddr) uuringu kohaselt takistaks **98% teatatud rikkumistest tugev turvahügieen**. Kõige tõhusam kaitsestrateegia ühendab põhjalikud turvapraktikad MCP-spetsiifiliste kontrollidega — tõestatud baasjõudlusega turvameetmed jäävad kõige mõjusamaks turvariski vähendamisel.

## Praegune turvatäielikkuse maastik

> **Märkus:** See info kajastab MCP turvastandardeid seisuga **5. veebruar 2026**, kooskõlas **MCP spetsifikatsiooniga 2025-11-25**. MCP protokoll areneb kiiresti edasi ning tulevikus võidakse lisada uusi autentimisviise ja täiustatud kontrollimeetmeid. Viimase teabe saamiseks pöörduge alati praeguse [MCP spetsifikatsiooni](https://spec.modelcontextprotocol.io/), [MCP GitHub hoidla](https://github.com/modelcontextprotocol) ja [turvalisuse parimate tavade dokumentatsiooni](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) poole.

> **Tulevikku silmas pidades:** `2026-07-28` versiooni kandidaadiga tugevdatakse autoriseerimist — kliendid peavad valideerima autoriseerimiste vastuste `iss` parameetri (RFC 9207), deklareerima OpenID Connect `application_type` dünaamilisel kliendi registreerimisel ning siduma registreeritud mandaadid välja andva autoriseerimiste serveriga. Vaata [Mis MCP-s muutub: 2026-07-28 versiooni kandidaat](../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) autoriseerimise SEP-de täieliku nimekirja jaoks.

## 🏔️ MCP turvakonverentsi töötuba (Sherpa)

Praktiliste turvakoolituste jaoks soovitame tungivalt **MCP turvakonverentsi töötuba** (Sherpa) — põhjalikku juhitud ekspeditsiooni MCP serverite turvamiseks Microsoft Azure’i platvormil.

### Töötuba ülevaade

[MCP turvakonverentsi töötuba](https://azure-samples.github.io/sherpa/) pakub praktilist ja rakendatavat turvaõpet läbi katsetatud "õrnpunkt → ekspluateeri → paranda → valideeri" metoodika. Õpite:

- **Murrates asju**: Kogeda haavatavusi päriselust, kasutades tahtlikult ebaturvalisi servereid
- **Azure-i natiivset turvalisust**: Kasutada Azure Entra ID-d, Key Vaulti, API Managementi ja AI sisuturvalisust
- **Mitmekihist kaitset**: Liikuda järk-järgult laagrites, luues põhjalikud turvakihid
- **OWASP standardite rakendamist**: Iga tehnika on seotud [OWASP MCP Azure turvajuhendiga](https://microsoft.github.io/mcp-azure-security-guide/)
- **Tootmiskõlblikku koodi**: Saada toimivaid ja testitud lahendusi

### Ekspeditsiooni marsruut

| Laager | Fookus | Kattuvad OWASP ohud |
|--------|--------|---------------------|
| **Base Camp** | MCP alused ja autentimise haavatavused | MCP01, MCP07 |
| **Camp 1: Identity** | OAuth 2.1, Azure hallatud identiteet, Key Vault | MCP01, MCP02, MCP07 |
| **Camp 2: Gateway** | API haldus, privaatsete lõpp-punktide haldus, valitsemine | MCP02, MCP06, MCP07, MCP09 |
| **Camp 3: I/O Security** | Promptide süstimine, PII kaitse, sisu turvalisus | MCP03, MCP05, MCP06, MCP10 |
| **Camp 4: Monitoring** | Logianalüüs, juhtpaneelid, ohutuvastus | MCP04, MCP08 |
| **The Summit** | Punase ja sinise meeskonnaga integratsioonitest | Kõik |

**Alusta siit**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP TOP 10 turvariski

[OWASP MCP Azure turvajuhend](https://microsoft.github.io/mcp-azure-security-guide/) kirjeldab kümmet kõige kriitilisemat turvariski MCP rakendustes:

| Risk | Kirjeldus | Azure leevendus |
|-------|-----------|-----------------|
| **MCP01** | Märgihalduse eksitus ja saladuse lekkimine | Azure Key Vault, hallatud ID |
| **MCP02** | Õiguste eskaleerumine laiendamise kaudu | RBAC, tingimuslik ligipääs |
| **MCP03** | Tööriistade mürgitamine | Tööriistade valideerimine, terviklikkuse kontroll |
| **MCP04** | Tarkvaratarneahela rünnakud ja sõltuvuste manipuleerimine | GitHub Advanced Security, sõltuvuste skaneerimine |
| **MCP05** | Käskude süstimine ja täitmine | Sisendi valideerimine, sandboxing |
| **MCP06** | Intentsioonivoo alistamine | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Ebapiisav autentimine ja autoriseerimine | Azure Entra ID, OAuth 2.1 PKCE-ga |
| **MCP08** | Auditite ja telemeetria puudumine | Azure Monitor, Application Insights |
| **MCP09** | Varjatud MCP serverid | API keskuse valitsemine, võrgueraldus |
| **MCP10** | Konteksti süstimine ja liigne info jagamine | Andmete klassifikatsioon, minimaalne eksponeerimine |

### MCP autentimise areng

MCP spetsifikatsioon on oluliselt arenenud autentimise ja autoriseerimise alal:

- **Esialgne lähenemine**: Varased spetsifikatsioonid nõudsid arendajatelt kohandatud autentimisserverite loomist, kus MCP serverid toimisid OAuth 2.0 autoriseerimisserveritena, hallates kasutaja autentimist otse
- **Praegune standard (2025-11-25)**: Uuendatud spetsifikatsioon lubab MCP serveritel delegaadi kaudu autentida väliste identiteedipakkujate, nagu Microsoft Entra ID, kaudu, parandades turvaplaani ja vähendades juurutuse keerukust
- **Transpordikihi turvalisus**: Paranenud tugi turvalistele transpordimehhanismidele koos sobivate autentimismustritega nii lokaalsetel (STDIO) kui kaugsuhtluskanalitel (voogedastusega HTTP)

## Autentimise ja autoriseerimise turvalisus

### Praegused turvaeesmärgid ja probleemid

Kaasaegsed MCP rakendused seisavad silmitsi mitmete autentimise ja autoriseerimise väljakutsetega:

### Riskid ja ohtude allikad

- **Valesti konfigureeritud autoriseerimisloogika**: MCP serverite nõrk autoriseerimise rakendus võib paljastada tundlikke andmeid ja rakendada ligipääsuvalveid valesti
- **OAuth märgiste kompromiteerimine**: Kohaliku MCP serveri märgiste vargus võimaldab ründajatel servereid esitada ja ligipääsu teenustele edasi suunata
- **Märgiste edastamise haavatavused**: Märgiste ebakorrapärane käitlemine loob turvakontrollide mööda minemise ja vastutuse puudumise
- **Liigne õiguste andmine**: Üleolevad õigused rikuvad minimaalsete õiguste põhimõtet ja suurendavad rünnakupinda

#### Märgiste edastamine: kriitiline anti-muster

**Märgiste edastamine on MCP praeguses autoriseerimise spetsifikatsioonis selgesõnaliselt keelatud seetõttu, et sellel on tõsised turvakaalutlused:**

##### Turvakontrollide mööda minemine  
- MCP serverid ja nende taga olevad API-d rakendavad olulisi turvakontrolle (kiirusepiirangud, päringute valideerimine, liikluse jälgimine), mis tuginevad korrektsel märgiste valideerimisel  
- Otse kliendi poolt API-le märgiste saatmine mööda nimetatud kaitseid nõrgendab turvaarsenali

##### Vastutuse ja auditeerimise raskused  
- MCP serverid ei suuda eristada kliente, kes kasutavad ülaltpoolt väljastatud märgiseid, murdes auditeerimisjälgi  
- Järgneva ressursiserveri logid näitavad eksitavalt päringu algallikaid, mitte tegelikult MCP serveri vahendajaid  
- Juhtumite uurimine ja vastavusauditid raskenevad oluliselt

##### Andmete väljaviimise riskid  
- Kontrollimata märgiste nõuded võimaldavad pahatahtlikel isikutel varastatud märgistega kasutada MCP servereid andmete väljaviimiseks vahendina  
- Usalduspiiri rikkumised võimaldavad volitamata ligipääsu vorme, mis mööduvad turvameetme piiridest

##### Mitme teenuse rünnakud  
- Kompromiteeritud märgised, mida aktsepteerivad mitmed teenused, lubavad külgsuunalist liikumist ühendatud süsteemides  
- Teenuste vaheline usaldusmudel võib puruneda, kui märgise päritolu ei ole kontrollitav

### Turvakontrollid ja leevendused

**Kriitilised turvanõuded:**

> **KOHUSTUSLIK**: MCP serverid **EI TOHI** aktsepteerida ühtegi märgist, mis ei ole selgesõnaliselt MCP serveri jaoks väljastatud

#### Autentimise ja autoriseerimise kontrollid

- **Terviklik autoriseerimise ülevaatus**: Tehke põhjalikke auditite MCP serveri autoriseerimisloogika kohta, et tagada ainult ettenähtud kasutajate ja klientide ligipääs tundlikele ressurssidele  
  - **Juhend rakendamiseks**: [Azure API Management kui autentimisvärav MCP serveritele](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
  - **Identiteedi integreerimine**: [Microsoft Entra ID kasutamine MCP serveri autentimiseks](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Turvaline märgihaldus**: Kasuta [Microsofti juhendis soovitatud märgiste valideerimise ja elutsükli parimaid tavasid](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)  
  - Kontrolli, et märgiste sihtrühmad vastaks MCP serveri identiteedile  
  - Rakenda korralikku märgiste pööramist ja aegumist  
  - Tõkesta märgiste korduslöögi ja volitamata kasutamise ründed  

- **Märgiste kaitstud hoiustamine**: Hoia märgiseid krüpteeritult nii puhke- kui liikumisolekus  
  - **Parimad tavad**: [Turvaline märgihaldus ja krüpteerimise juhend](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Ligipääsuvalve rakendamine

- **Väikseimate õiguste põhimõte**: Anna MCP serveritele vaid minimaalne vajalik ligipääs  
  - Regulaarne õiguste ülevaatus ja uuendus privilegeerimise vältimiseks  
  - **Microsofti dokumentatsioon**: [Ohutu väikseimate õiguste ligipääs](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollipõhine ligipääsukontroll (RBAC)**: Rakenda peent rollide jaotust  
  - Kitsalt sihitud rollid kindlatele ressurssidele ja tegevustele  
  - Väldi laialdasi või mittevajalikke õigusi, mis suurendaksid rünnakupinda

- **Jätkuv õiguste jälgimine**: Teosta pidevat ligipääsukontrolli auditeerimist ja jälgimist  
  - Jälgi õiguste kasutusmustreid kõrvalekallete tuvastamiseks  
  - Paranda viivitamatult üleliigsed või kasutamata õigused

## AI-spetsiifilised turvaohtud

### Promptide süstimine ja tööriistade manipuleerimise rünnakud

Kaasaegsed MCP rakendused seisavad silmitsi keerukate AI-spetsiifiliste rünnakutega, mida traditsioonilised turvameetmed täielikult ei kata:

#### **Kaudne promptide süstimine (Cross-Domain Prompt Injection)**

**Kaudne promptide süstimine** on üks kriitilisemaid haavatavusi MCP toetatud AI süsteemides. Ründajad peidavad pahatahtlikke juhiseid välisesse sisusse — dokumentidesse, veebilehtedele, meilidele või andmeallikatesse — mida AI süsteemid hiljem töötlevad legaalsete käskudena.

**Rünnaku stsenaariumid:**  
- **Dokumendipõhine süstimine**: Pahatahtlikud juhised peidetud töödeldavatesse dokumentidesse, mis vallandavad ettenägematud AI toimingud  
- **Veebisisu ärakasutamine**: Kompromiteeritud veebilehed, mis sisaldavad manustatud promptisid, mis juhivad AI käitumist kaughaaval  
- **Meilil põhinevad rünnakud**: Pahatahtlikud promptid meilides, mis panevad AI assistendi lekkima infot või tegema volitamata toiminguid  
- **Andmeallikate saastamine**: Kompromiteeritud andmebaasid või API-d, mis edastavad saastatud sisu AI süsteemidele

**Reaalelu mõju**: Need rünnakud võivad põhjustada andmelekkeid, privaatsusintsidente, kahjuliku sisu loomist ja kasutajate manipuleerimist. Üksikasjaliku analüüsi leiad siit: [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/et/prompt-injection.ed9fbfde297ca877.webp)

#### **Tööriistade mürgitamise rünnakud**

**Tööriistade mürgitamine** on suunatud MCP tööriistade metaandmetele, ärakasutades seda, kuidas LLM-id tõlgendavad tööriistade kirjeldusi ja parameetreid täitemeetodite tegemiseks.

**Rünnaku mehhanismid:**  
- **Metaandmete manipuleerimine**: Ründajad süstivad pahatahtlikke juhiseid tööriistade kirjeldustesse, parameetrite määratlusse või kasutusnäidistesse  
- **Nähtamatud juhised**: Peidetud promptid tööriistade metaandmetes, mida AI mudelid töötlevad, kuid mis on inimestele nähtamatud  
- **Dünaamilised tööriistamuudatused ("Rug Pulls")**: Kasutajate poolt heaks kiidetud tööriistad muudetakse hiljem pahatahtlikeks ilma teadmiseta  
- **Parameetrite süstimine**: Pahatahtlik sisu tööriistade parameetrite skeemides, mis mõjutab mudelite käitumist
**Majutatud serveri riskid**: kaug-MCP serveritel on suuremad riskid, kuna tööriistade määratlusi saab värskendada pärast kasutaja esialgset nõusolekut, tekitades olukordi, kus varem ohutud tööriistad muutuvad pahatahtlikeks. Üldiseks analüüsiks vaadake [Tööriista mürgitamise rünnakuid (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/et/tool-injection.3b0b4a6b24de6bef.webp)

#### **Täiendavad tehisintellekti ründevektorid**

- **Ristdomeeni juhise süstimine (XPIA)**: keerukad rünnakud, mis kasutavad sisu mitmest domeenist turvakontrollidest möödumiseks
- **Dünaamiline võimekuse muutmine**: tööriistade võimekuse reaalajas muutmine, mis pääseb esialgsetest turvakontrollidest
- **Kontekstikasti mürgitamine**: rünnakud, mis manipuleerivad suurte kontekstikastidega, et peita pahatahtlikke juhiseid
- **Mudelipõhised segadusrünnakud**: mudeli piirangute ärakasutamine ettearvamatute või ohtlike käitumiste tekitamiseks


### Tehisintellekti turvariskide mõju

**Suure mõjuga tagajärjed:**
- **Andmete väljapressimine**: volitamata juurdepääs ja tundlike ettevõtte- või isikuandmete vargus
- **Privaatsusrikked**: isikut tuvastava teabe (PII) ja konfidentsiaalse äriteabe lekked  
- **Süsteemi manipuleerimine**: kriitiliste süsteemide ja tööprotsesside soovimatud muutmised
- **Tunnuste vargus**: autentimistokenite ja teenusetunnuste kompromiteerimine
- **Lateraalne liikumine**: kompromiteeritud tehisintellektisüsteemide kasutamine laiemate võrgurünnakute läbiviimiseks

### Microsofti tehisintellekti turvalahendused

#### **Tehisintellekti juhisesildid: täiustatud kaitse süstimisrünnakute vastu**

Microsofti **AI Prompt Shields** tagavad täieliku kaitse nii otseste kui ka kaudsete juhise süstimisrünnakute vastu mitme turvakihi kaudu:

##### **Põhikaitse mehhanismid:**

1. **Täiustatud tuvastamine ja filtreerimine**
   - Masinõppe algoritmid ja NLP tehnikad tuvastavad pahatahtlikud juhised välises sisus
   - Reaalajas analüüs dokumentide, veebilehtede, e-kirjade ja andmeallikate ohtudeks
   - Konteksti mõistmine legaalsetest vs pahatahtlikest juhiste mustritest

2. **Fookustehnikad**  
   - Eraldab usaldusväärsed süsteemijuhised ja potentsiaalselt kompromiteeritud välissisestuse
   - Teksti teisenduse meetodid, mis suurendavad mudeli asjakohasust, samal ajal isoleerides pahatahtliku sisu
   - Aitab tehisintellektil hoida juhiste õiget hierarhiat ja ignoreerida süstitud käsklusi

3. **Piiritlejate ja andmesildistamise süsteemid**
   - Selge piiri määratlus usaldusväärsete süsteemisõnumite ja välise sisuteksti vahel
   - Erilised märgistajad, mis toovad esile piire usaldusväärsete ja ebausaldusväärsete andmeallikate vahel
   - Selge eraldamine takistab juhiste segadust ja volitamata käskluste täitmist

4. **Pidev ohuintelligentsus**
   - Microsoft jälgib pidevalt uusi ründemustreid ja uuendab kaitseid
   - Proaktiivne ohujahindus uute süstimisvõtete ja ründevektorite jaoks
   - Regulaarne turvalisuse mudelite uuendamine ohutuse tagamiseks muutuva ohumaailma vastu

5. **Azure sisukaitse integreerimine**
   - Osana laiemast Azure AI sisukaitse komplektist
   - Täiendav tuvastus jailbreak-i katsetele, kahjulikule sisule ja turvapoliitikate rikkumistele
   - Ühtsed turvakontrollid AI rakenduste komponentide vahel

**Rakendamisressursid**: [Microsoft Prompt Shields dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/et/prompt-shield.ff5b95be76e9c78c.webp)


## Täiustatud MCP turvaohtud

### Sessiooni ülevõtmise haavatavused

**Sessiooni ülevõtmine** on kriitiline ründevektor olekupõhiste MCP rakenduste puhul, kus volitamata pooled saavad kätte ja kuritarvitavad kehtivaid sessiooni identifikaatoreid, et esineda klientidena ja läbi viia volitamata toiminguid.

#### **Rünnakustsenaariumid ja riskid**

- **Sessiooni ülevõtmise juhise süstimine**: varastatud sessioonituvastajatega ründajad süstivad serveritesse pahatahtlikke sündmusi, mis jagavad sessioone, potentsiaalselt käivitades kahjulikke toiminguid või pääsedes ligi tundlikele andmetele
- **Otsepärasus**: varastatud sessioonituvastajad võimaldavad MCP serveril teha otsekõnesid, mis mööduvad autentimisest ning käsitlevad ründajat legaalse kasutajana
- **Kompromiteeritud taasalustavad vood**: ründajad võivad taotlusi varakult lõpetada, põhjustades, et legitiimsed kliendid jätkavad potentsiaalselt pahatahtliku sisuga

#### **Sessioonihalduse turvakontrollid**

**Kriitilised nõuded:**
- **Volituse kontroll**: MCP serverid, mis teostavad volitusi, PEAVAD kontrollima KÕIKI sissetulevaid taotlusi ja EI TOHI tugineda sessioonidele autentimiseks
- **Turvaline sessiooni loomine**: kasutage krüptograafiliselt turvalisi, mittesihipäraseid sessioonituvastajaid, mis genereeritakse turvaliste juhuslike arvugeneraatoritega
- **Kasutajapõhine sidumine**: siduge sessioonituvastajad kasutajaspetsiifilise infoga, kasutades vormingut nagu `<user_id>:<session_id>`, et vältida sessioonide kuritarvitamist eri kasutajate vahel
- **Sessiooni elutsükli haldus**: rakendage nõuetekohast aegumist, rotatsiooni ja tühistamist, et piirata haavatavuste kordumist
- **Transportiurgutus**: kohustuslik HTTPS kogu suhtluseks, et vältida sessioonituvastajate pealtkuulamist

### Segaduses volitaja probleem

**Segaduses volitaja probleem** tekib siis, kui MCP serverid toimivad autentimisproksidena klientide ja kolmandate osapoolte teenuste vahel, võimaldades volituse möödumist staatiliste kliendi-ID-de ärakasutamise kaudu.

#### **Rünnakumehhanismid ja riskid**

- **Küpsistepõhine nõusoleku möödaviimine**: varem kasutaja autentimisel loodud nõusolekuküpsised, mida ründajad kuritarvitavad pahatahtlike volitustaotlustega, kasutades võltsitud ümbersuunamiste URI-sid
- **Volituskoode vargus**: olemasolevad nõusolekuküpsised võivad sundida volitusservereid nõusolekusid kasutamata jättes suunama koode ründaja kontrollitud lõpp-punktidesse  
- **Volitamata API juurdepääs**: varastatud volituskoode kasutatakse tokenite vahetamiseks ja kasutaja esindamiseks ilma selgesõnalise heakskiiduta

#### **Leevendusmeetmed**

**Kohustuslikud kontrollid:**
- **Eksplitseerunud nõusoleku nõuded**: MCP proksiserverid, kes kasutavad staatilisi kliendi-ID-sid, PEAVAD hankima kasutaja nõusoleku iga dünaamiliselt registreeritud kliendi jaoks
- **OAuth 2.1 turvalisuse rakendus**: järgige kehtivaid OAuth turvapraktikaid, sealhulgas PKCE (Proof Key for Code Exchange) kõigile volitusnõuetele
- **Range kliendi valideerimine**: rakendage ranget valideerimist ümbersuunamise URI-dele ja kliendi identifikaatoritele kuritarvituste vältimiseks

### Tokenite läbipääsu haavatavused  

**Tokenite läbipääs** on otsene anti-muster, kus MCP serverid võtavad vastu klientide tokenid ilma nõuetekohase valideerimiseta ning edastavad need alluvatele API-dele, rikkudes MCP volituse spetsifikatsioone.

#### **Turvapõhimõtted**

- **Kontrollide möödaviimine**: otsene klient-API tokenite kasutamine möödub kriitilistest kiirusepiirangutest, valideerimisest ja jälgimisest
- **Auditijälje rikkumine**: ülesvoolu väljastatud tokenid muudavad kliendi tuvastamise võimatuks, kahjustades intsidentide uurimise võimalusi
- **Proksipõhine andmete väljapressimine**: vältimatult valideerimata tokenid võimaldavad pahatahtlikel osapooltel kasutada servereid volitamata andmetele ligipääsuks
- **Usalduse piiri rikked**: alluvad teenused võivad eeldada usaldust tokeni päritolu suhtes, mis muutub kontrollimatuks
- **Mitmeteenuseline ründe laienemine**: kompromiteeritud tokenite aktsepteerimine mitmes teenuses võimaldab lateraalset liikumist

#### **Nõutavad turvakontrollid**

**Läbirääkimatu nõuded:**
- **Tokenite valideerimine**: MCP serverid EI TOHI vastu võtta tokenid, mis ei ole otseselt väljastatud MCP serverile
- **Publiku kontroll**: alati valideerige, et tokeni sihtrühm vastab MCP serveri identiteedile
- **Korralik tokeni elutsükkel**: kasutage lühikest kestvusega ligipääsutokenid koos turvalise rotatsiooniga


## Tarneahela turvalisus tehisintellektisüsteemidele

Tarneahela turvalisus on arenenud kaugemale traditsioonilistest tarkvarasõltuvustest ja hõlmab kogu tehisintellekti ökosüsteemi. Moodsad MCP rakendused peavad rangelt kontrollima ja jälgima kõiki tehisintellektiga seotud komponente, sest igaüks neist toob sisse võimalikke haavatavusi, mis võivad ohustada süsteemi terviklikkust.

### Laiendatud tehisintellekti tarneahela komponendid

**Traditsioonilised tarkvarasõltuvused:**
- Avatud lähtekoodiga raamistike ja teekide kasutamine
- Konteineripildid ja baasüsteemid  
- Arendustööriistad ja koostevood
- Infrastruktuuri komponendid ja teenused

**Tehisintellekti spetsiifilised tarneahela elemendid:**
- **Alusmudelid**: erinevatelt pakkujatelt eelõpetatud mudelid, mis vajavad päritolutõestust
- **Sissepakkimise teenused**: välised vektori- ja semantilise otsingu teenused
- **Konteksti pakkujad**: andmeallikad, teadmistebaasid ja dokumendirepositooriumid  
- **Kolmandate osapoolte API-d**: välised AI teenused, ML vood ja andmetöötluse lõpp-punktid
- **Mudeli artefaktid**: kaalud, konfiguratsioonid ja peenhäälestatud mudelivariandid
- **Treeningandmete allikad**: andmekogumid mudelite treenimiseks ja peenhäälestamiseks

### Üldine tarneahela turvastrateegia

#### **Komponentide kontroll ja usaldus**
- **Päritolu valideerimine**: kontrollige kõigi tehisintellekti komponentide päritolu, litsentseeringut ja terviklikkust enne integreerimist
- **Turvaanalüüs**: viige läbi haavatavuste skaneerimine ja turvaaudit mudelitele, andmeallikatele ja AI teenustele
- **Mainetulemuste analüüs**: hinnake AI teenusepakkujate turvarekordeid ja praktikaid
- **Nõuete täitmine**: veenduge, et kõik komponendid vastavad organisatsiooni turva- ja regulatiivsetele nõuetele

#### **Turvalised juurutusvood**  
- **Automatiseeritud CI/CD turvakontrollid**: integreerige turvaskaneerimine kogu juurutusvoo jooksul
- **Artefakti terviklikkus**: kasutage krüptograafilist valideerimist kõigi juurutatud artefaktide (kood, mudelid, konfiguratsioonid) puhul
- **Etagenev juurutus**: kasutage progressiivseid juurutusstrateegiaid turvakontrolliga igas etapis
- **Usaldusväärsed artefaktide repositooriumid**: juurutage ainult verifitseeritud ja turvalistest repositooriumitest

#### **Pidev jälgimine ja reageerimine**
- **Sõltuvuste skaneerimine**: pidev haavatavuste jälgimine kõigi tarkvara- ja AI-komponentide sõltuvuste puhul
- **Mudeli jälgimine**: mudeli käitumise, jõudluse nihkete ja turvaanomaliate pidev hindamine
- **Teenuse tervise jälgimine**: jälgige väliseid AI teenuseid nende kättesaadavuse, turvaintsidentide ja poliitika muudatuste osas
- **Ohuintelligentsuse integreerimine**: kaasake AI ja ML turvariskidega seotud ohuinfo voogusid

#### **Juurdepääsukontroll ja miinimumõigused**
- **Komponentide tasandi õigused**: piirake juurdepääsu mudelitele, andmetele ja teenustele ärivajaduse alusel
- **Teenuskontode haldus**: kasutage spetsiaalseid teenuskontosid minimaalsete vajalike õigustega
- **Võrgu segmentatsioon**: isoleerige AI komponendid ja piirake võrguliiklust teenuste vahel
- **API värava kontrollid**: kasutage tsentraliseeritud API väravaid välistele AI teenustele juurdepääsu kontrollimiseks ja jälgimiseks

#### **Intsidentide haldus ja taastumine**
- **Kiired reageerimisprotseduurid**: väljatöötatud protsessid kompromiteeritud AI komponentide parandamiseks või asendamiseks
- **Tunnuste rotatsioon**: automatiseeritud süsteemid saladuste, API võtmete ja teenusetunnuste vahetamiseks
- **Tagasipöördumise võimalused**: võimalus kiiresti taastada varasemad teada-tuntud toimivad AI komponendid
- **Tarneahela rikkumise taastumine**: spetsiifilised protseduurid ülesvoolu AI teenuse kompromiteerumise korral

### Microsofti turvatööriistad ja integreerimine

**GitHub Advanced Security** pakub kõikehõlmavat tarneahela kaitset, sealhulgas:
- **Saladuste skaneerimine**: automatiseeritud autentimisteabe, API võtmete ja tokenite tuvastus repositooriumites
- **Sõltuvuste skaneerimine**: haavatavuste hindamine avatud lähtekoodiga sõltuvuste ja teekide kohta
- **CodeQL analüüs**: staatiline koodi analüüs turvaaukude ja koodimisprobleemide jaoks
- **Tarneahela ülevaated**: nähtavus sõltuvuste tervisesse ja turvastatusse

**Azure DevOps ja Azure Repos integratsioon:**
- Kõrgtaseme turvaskaneeringute integreerimine Microsofti arendusplatvormidel
- Automatiseeritud turvakontrollid Azure Pipelines-is AI töökoormustele
- Poliitikate jõustamine turvalise AI komponendide juurutamise jaoks

**Microsofti sisemised praktikad:**
Microsoft rakendab ulatuslikke tarneahela turvapraktilisi viise kõigis toodetes. Õppige tõestatud lähenemisi [Tee tarneahela turvaks Microsoftis](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Põhitõed turvaluse parimates tavades

MCP rakendused pärivad ja arendavad teie organisatsiooni olemasolevat turvataset. Aluspõhimõtete tugevdamine parandab oluliselt tehisintellekti süsteemide ja MCP juurutuste üldist turvalisust.

### Turvalisuse põhialused

#### **Turvalise arenduse tavad**
- **OWASP vastavus**: kaitse [OWASP Top 10](https://owasp.org/www-project-top-ten/) veebirakenduste haavatavuste eest
- **Tehisintellekti spetsiifilised kaitsed**: rakendage meetmed [OWASP Top 10 LLM-idele](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Turvaline saladuste haldus**: kasutage spetsiaalseid sahtleid tokenite, API võtmete ja tundlike seadistusandmete jaoks
- **Lõpust-lõpuni krüpteerimine**: rakendage turvalist side kõigis rakenduse komponentides ja andmevoogudes
- **Sisendi valideerimine**: kõigi kasutajasisendite, API parameetrite ja andmeallikate range valideerimine

#### **Infrastruktuuri tugevdamine**
- **Mitmetasemeline autentimine**: kohustuslik MFA kõigile haldus- ja teenuskontodele
- **Plaasterihaldus**: automatiseeritud ja õigeaegne süsteemide, raamistikute ja sõltuvuste plaastrite paigaldus  
- **Identiteedipakkuja integratsioon**: tsentraliseeritud identiteedihaldus ettevõtte identiteedipakkujate (Microsoft Entra ID, Active Directory) kaudu
- **Võrgu segmentatsioon**: MCP komponentide loogiline eraldamine lateraalse liikumise piiramiseks
- **Väikseima volituse printsiip**: minimaalsete vajalike õiguste kasutamine kõikidel süsteemikomponentidel ja kontodel

#### **Turvamonitooring ja tuvastamine**
- **Üleüldine logimine**: detailsed logid AI rakenduste tegevusest, sealhulgas MCP kliendi-serveri vahelistest suhtlustest
- **SIEM integratsioon**: tsentraliseeritud turvainfo ja sündmuste haldus anomaaliate tuvastamiseks
- **Käitumusanalüüs**: AI-põhine jälgimine ebatavaliste mustrite avastamiseks süsteemi ja kasutajate käitumises
- **Ohuintelligentsus**: väliste ohuvoogude ja kompromissinäitajate (IOC) integreerimine
- **Intsidentide haldus**: hästi määratletud protseduurid turvaprobleemide avastamiseks, reageerimiseks ja taastumiseks

#### **Nullusaldus arhitektuur**
- **Ärge usaldage kunagi, kontrollige alati**: pidev kasutajate, seadmete ja võrguliideste valideerimine
- **Mikrosegmentatsioon**: peenekoelised võrgukontrollid, mis isoleerivad üksikud töökoormused ja teenused
- **Identiteedikeskne turvalisus**: turvapoliitikad, mis põhinevad valideeritud identiteetidel, mitte võrgukohtadel
- **Pidev riskihindamine**: dünaamiline turvastaatuse hindamine praeguse konteksti ja käitumise põhjal
- **Tingimuslik ligipääs**: juurdepääsukontrollid, mis kohanevad riskifaktorite, asukoha ja seadme usaldatavusega

### Ettevõtteintegratsiooni mustrid

#### **Microsofti turvakompleksi integreerimine**
- **Microsoft Defender for Cloud**: pilve turvatugipostatsiooni haldus
- **Azure Sentinel**: pilvepõhine SIEM ja SOAR võimekus AI töövoogude kaitseks
- **Microsoft Entra ID**: ettevõtte identiteedi- ja juurdepääsuhaldus tingimusliku ligipääsuga poliitikate abil
- **Azure Key Vault**: tsentraliseeritud saladuste haldus riistvarapõhise turbemooduliga (HSM)
- **Microsoft Purview**: andmevalitsemine ja vastavus AI andmeallikatele ja töövoogudele

#### **Vastavus ja haldus**
- **Regulatiivne kooskõla**: veenduge, et MCP rakendused vastavad tööstusharu spetsiifilistele nõuetele (GDPR, HIPAA, SOC 2)
- **Andmete klassifitseerimine**: AI-süsteemide poolt töödeldavate tundlike andmete nõuetekohane kategoriseerimine ja käsitlemine  
- **Auditijäljed**: Regulatiivse vastavuse ja kohtuekspertiisi uurimise jaoks põhjalik logimine  
- **Privaatsuse juhtimine**: Privaatsuspõhimõtete rakendamine „privaatsus disainis“ AI-süsteemide arhitektuuris  
- **Muutuste haldamine**: Formaalsed protsessid AI-süsteemi muudatuste turvakontrolliks  

Need aluspraktikad loovad tugeva turvalisuse aluse, mis tõhustab MCP-spetsiifiliste turvakontrollide tõhusust ja tagab põhjaliku kaitse AI-põhistele rakendustele.

## Olulised turbevõtmed

- **Kihiline turbe lähenemine**: Ühenda aluslikud turbepraktikad (turvaline kodeerimine, minimaalne privileeg, tarneahela verifitseerimine, pidev järelevalve) AI-spetsiifiliste kontrollidega põhjalikuks kaitseks

- **AI-spetsiifiline ohumaastik**: MCP süsteemid seisavad silmitsi unikaalsete riskidega nagu prompti süstimine, tööriistamürgitus, sessioonikaaperdamine, „segaduses esindaja“ probleemid, tokeni läbipääsu haavatavused ja liigne õiguste andmine, mis nõuavad spetsiaalseid leevendusi

- **Autentimise ja autoriseerimise tipptase**: Rakenda tugevat autentimist väliste identiteedipakkujate (Microsoft Entra ID) abil, kehtesta nõuetekohane tokeni valideerimine ja ära kunagi aktsepteeri tokeneid, mis pole selgelt välja antud sinu MCP serverile

- **AI rünnakute ennetamine**: Kasuta Microsoft Prompt Shields ja Azure Content Safety teenuseid, et kaitsta kaudse prompt-süstimise ja tööriistamürgituse rünnakute eest, valideeri tööriistade metaandmeid ja jälgi dünaamilisi muutusi

- **Sessiooni ja transpordi turvalisus**: Kasuta krüptograafiliselt turvalisi, mittedeterministlikke sessiooni ID-sid, mis on seotud kasutajatunnustega, rakenda nõuetekohane sessiooni elutsükli haldus ja ära kunagi kasuta sessioone autentimiseks

- **OAuth turbe parimad praktikad**: Väldi „segaduses esindaja“ rünnakuid, hankides kasutajalt selge nõusoleku dünaamiliselt registreeritud klientidele, rakenda nõuetekohaselt OAuth 2.1 PKCE-ga ning kehtesta rangelt redirect URI valideerimine  

- **Tokenite turbeprintsiibid**: Väldi tokeni läbipääsu anti-mustreid, valideeri tokeni vastuvõtja väited, kasuta lühiajalisi tokeneid turvalise rotatsiooniga ja säilita selged usalduspiirid

- **Põhjalik tarneahela turvalisus**: Käsitle kõiki AI ökosüsteemi komponente (mudelid, embedding'u pakkujad, konteksti pakkujad, välised APId) sama range turvasusega nagu traditsioonilisi tarkvarasõltuvusi

- **Pidev areng**: Hoia end kursis kiiresti arenevate MCP spetsifikatsioonidega, panusta turvakeskonna standarditesse ja säilita kohanev turbepostuur protokolli küpsemisel

- **Microsofti turbeintegreerimine**: Kasuta Microsofti ulatuslikku turbeökosüsteemi (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID), et suurendada MCP levitamise kaitset

## Põhjalikud ressursid

### **Ametlik MCP turbedokumentatsioon**
- [MCP spetsifikatsioon (Käivitus: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP turbe parimad praktikad](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP autoriseerimise spetsifikatsioon](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub hoidla](https://github.com/modelcontextprotocol)

### **OWASP MCP turberessursid**
- [OWASP MCP Azure turbejuhend](https://microsoft.github.io/mcp-azure-security-guide/) – Põhjalik OWASP MCP Top 10 koos Azure juurutusjuhistega  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) – Ametlik OWASP MCP turberiskid  
- [MCP turbe tippkohtumise töötuba (Sherpa)](https://azure-samples.github.io/sherpa/) – Käed-külge turbekoolitus MCP jaoks Azure'is  

### **Turbestandardid & parimad praktikad**
- [OAuth 2.0 turbe parimad praktikad (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 veebirakenduste turve](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 suurtel keelemudelitel](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsofti digitaalne kaitseraport](https://aka.ms/mddr)

### **AI turbeuuringud & analüüs**
- [Prompti süstimine MCP-s (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tööriistamürgituse rünnakud (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP turbeuuringu ülevaade (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsofti turbelahendused**
- [Microsoft Prompt Shields dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety teenus](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID turve](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure tokenite halduse parimad praktikad](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Juhendid & õppetunnid**
- [Azure API haldus MCP autentimise väravana](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentimine MCP serveritega](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Turvaline tokeni salvestamine ja krüpteerimine (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps ja tarneahela turvalisus**
- [Azure DevOps turve](https://azure.microsoft.com/products/devops)
- [Azure Repos turve](https://azure.microsoft.com/products/devops/repos/)
- [Microsofti tarneahela turvalisuse teekond](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Täiendavad turbedokumendid**

Põhjalikku turbesuuniseid leiad nende spetsialiseerunud dokumentide hulgast:

- **[MCP turbe parimad praktikad 2025](./mcp-security-best-practices-2025.md)** – Täielik turbepraktikate kogumik MCP rakendustele  
- **[Azure Content Safety juurutamine](./azure-content-safety-implementation.md)** – Praktilised näited Azure Content Safety integreerimiseks  
- **[MCP turbekontrollid 2025](./mcp-security-controls-2025.md)** – Viimased turbekontrollid ja meetodid MCP kasutuselevõtuks  
- **[MCP parimate praktikate kiire viide](./mcp-best-practices.md)** – Kiire visand olulistest MCP turbepraktikatest  
- **[BlueHat 2026: AI tuleviku turvamine – MCP kaitsmine süvakihtidega](https://www.youtube.com/watch?v=cVWB58kEt-Y)** – Kaitse süvakihtides mustrid Microsofti Turbe Reageerimiskeskuselt (MSRC)  

### **Praktilised turbekoolitused**

- **[MCP turbe tippkohtumise töötuba (Sherpa)](https://azure-samples.github.io/sherpa/)** – Põhjalik praktiline töötuba MCP serverite turvamiseks Azure'is, progresseeruvate laagrikoolitustega alates Baaslaagrist kuni Tippkohtumiseni  
- **[OWASP MCP Azure turbejuhend](https://microsoft.github.io/mcp-azure-security-guide/)** – Viitearhitektuur ja rakendusjuhised kõigi OWASP MCP Top 10 riskide jaoks  

---

## Järgmine

Järgmine: [3. peatükk: Algus](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->