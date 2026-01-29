# MCP turvalisus: põhjalik kaitse tehisintellekti süsteemidele

[![MCP turvalisuse parimad tavad](../../../translated_images/et/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

Turvalisus on tehisintellekti süsteemide disaini aluseks, mistõttu oleme selle teise sektsiooni prioriteediks seadnud. See vastab Microsofti **Secure by Design** põhimõttele [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/) raames.

Model Context Protocol (MCP) toob AI-põhistele rakendustele võimsad uued võimalused, tuues samal ajal kaasa unikaalsed turvalisuse väljakutsed, mis ulatuvad kaugemale traditsioonilistest tarkvarariskidest. MCP süsteemid seisavad silmitsi nii väljakujunenud turvariskidega (turvaline kodeerimine, minimaalne privileeg, tarneahela turvalisus) kui ka uute AI-spetsiifiliste ohtudega, sealhulgas promptide süstimine, tööriistade mürgitamine, sessiooni kaaperdamine, segaduses esindaja rünnakud, tokenite läbipääsu haavatavused ja dünaamiline võimekuse muutmine.

See õppetund uurib kõige kriitilisemaid turvariske MCP rakendustes — hõlmates autentimist, autoriseerimist, liigselt laialdasi õigusi, kaudset promptide süstimist, sessiooni turvalisust, segaduses esindaja probleeme, tokenite haldust ja tarneahela haavatavusi. Õpite rakendatavaid kontrollimeetmeid ja parimaid tavasid nende riskide vähendamiseks, kasutades Microsofti lahendusi nagu Prompt Shields, Azure Content Safety ja GitHub Advanced Security, et tugevdada oma MCP juurutust.

## Õpieesmärgid

Selle õppetunni lõpuks oskate:

- **Tuvastada MCP-spetsiifilisi ohte**: Tuvastada MCP süsteemide unikaalsed turvariskid, sealhulgas promptide süstimine, tööriistade mürgitamine, liigsed õigused, sessiooni kaaperdamine, segaduses esindaja probleemid, tokenite läbipääsu haavatavused ja tarneahela riskid
- **Rakendada turvakontrolle**: Rakendada tõhusaid leevendusmeetmeid, sealhulgas tugevat autentimist, minimaalset privileegi juurdepääsu, turvalist tokenite haldust, sessiooni turvakontrolle ja tarneahela kontrolli
- **Kasutada Microsofti turvalahendusi**: Mõista ja juurutada Microsoft Prompt Shields, Azure Content Safety ja GitHub Advanced Security MCP töökoormuste kaitseks
- **Valideerida tööriistade turvalisust**: Mõista tööriistade metaandmete valideerimise tähtsust, dünaamiliste muudatuste jälgimist ja kaitset kaudsete promptide süstimise rünnakute vastu
- **Integreerida parimaid tavasid**: Ühendada väljakujunenud turvalisuse aluspõhimõtted (turvaline kodeerimine, serverite tugevdamine, nullusaldus) MCP-spetsiifiliste kontrollidega põhjalikuks kaitseks

# MCP turvalisuse arhitektuur ja kontrollid

Kaasaegsed MCP rakendused nõuavad kihilisi turvalahendusi, mis käsitlevad nii traditsioonilist tarkvara turvalisust kui ka AI-spetsiifilisi ohte. Kiiresti arenev MCP spetsifikatsioon täiustab pidevalt oma turvakontrolle, võimaldades paremat integreerimist ettevõtte turvarhitektuuridega ja väljakujunenud parimate tavadega.

[Microsoft Digital Defense Report](https://aka.ms/mddr) uuring näitab, et **98% teatatud rikkumistest oleks takistatud tugeva turvahügieeni abil**. Kõige tõhusam kaitsestrateegia ühendab aluspõhised turvapraktikad MCP-spetsiifiliste kontrollidega — tõestatud baasjoonel põhinevad turvameetmed on endiselt kõige mõjusamad üldise turvariski vähendamisel.

## Praegune turvamaastik

> **Märkus:** See teave kajastab MCP turvastandardeid seisuga **18. detsember 2025**. MCP protokoll areneb kiiresti ning tulevased rakendused võivad tuua uusi autentimis- ja täiustatud kontrollimustreid. Järgige alati kehtivat [MCP spetsifikatsiooni](https://spec.modelcontextprotocol.io/), [MCP GitHubi hoidlat](https://github.com/modelcontextprotocol) ja [turvalisuse parimate tavade dokumentatsiooni](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) viimast juhendit.

### MCP autentimise areng

MCP spetsifikatsioon on autentimise ja autoriseerimise lähenemist oluliselt arendanud:

- **Algne lähenemine**: Varased spetsifikatsioonid nõudsid arendajatelt kohandatud autentimisteenuste loomist, kus MCP serverid tegid OAuth 2.0 autoriseerimisteenuste rolli, haldades kasutaja autentimist otse
- **Praegune standard (2025-11-25)**: Uuendatud spetsifikatsioon lubab MCP serveritel delegeerida autentimine välistele identiteedipakkujatele (nt Microsoft Entra ID), parandades turvalisust ja vähendades rakenduse keerukust
- **Transpordikihi turvalisus**: Täiustatud tugi turvalistele transpordimehhanismidele koos sobivate autentimismustritega nii lokaalsete (STDIO) kui ka kaugühenduste (Streamable HTTP) jaoks

## Autentimise ja autoriseerimise turvalisus

### Praegused turvaprobleemid

Kaasaegsed MCP rakendused seisavad silmitsi mitmete autentimise ja autoriseerimise väljakutsetega:

### Riskid ja ohutegurid

- **Valesti konfigureeritud autoriseerimisloogika**: MCP serverite vigane autoriseerimise rakendus võib avaldada tundlikku teavet ja rakendada juurdepääsukontrolle valesti
- **OAuth tokeni kompromiteerimine**: Kohaliku MCP serveri tokeni vargus võimaldab ründajatel esineda serveritena ja pääseda alluvatesse teenustesse
- **Tokenite läbipääsu haavatavused**: Tokenite väär käsitlemine loob turvakontrollide möödaviigu ja vastutuse lüngad
- **Liigsed õigused**: Üleprivileegitud MCP serverid rikuvad minimaalsete privileegide põhimõtet ja suurendavad ründepinda

#### Tokenite läbipääs: kriitiline anti-muster

**Tokenite läbipääs on praeguse MCP autoriseerimise spetsifikatsiooni järgi selgesõnaliselt keelatud** tõsiste turvariskide tõttu:

##### Turvakontrollide möödaviimine
- MCP serverid ja alluvad API-d rakendavad kriitilisi turvakontrolle (nt päringute piiramist, päringute valideerimist, liikluse jälgimist), mis sõltuvad tokenite nõuetekohasest valideerimisest
- Otsene kliendi ja API tokeni kasutamine möödub neist olulistest kaitsetest, nõrgestades turvarhitektuuri

##### Vastutuse ja auditeerimise raskused  
- MCP serverid ei suuda eristada kliente, kes kasutavad ülemjooksu väljastatud tokeneid, mis rikub auditeerimisteed
- Alluvate ressurssiserverite logid näitavad eksitavalt päringute päritolu, mitte tegelikke MCP serveri vahendajaid
- Juhtumite uurimine ja vastavusauditid muutuvad oluliselt keerulisemaks

##### Andmete väljaviimise riskid
- Valideerimata tokeni nõuded võimaldavad pahatahtlikel isikutel varastatud tokenitega kasutada MCP servereid andmete väljaviimiseks
- Usalduspiiri rikkumised lubavad volitamata juurdepääsu mustreid, mis mööduvad kavandatud turvakontrollidest

##### Mitme teenuse ründeteed
- Kompromiteeritud tokenid, mida aktsepteerivad mitmed teenused, võimaldavad külgsuunalist liikumist ühendatud süsteemides
- Teenustevahelised usaldusassumptsioonid võivad rikkuda, kui tokenite päritolu ei saa kontrollida

### Turvakontrollid ja leevendused

**Kriitilised turvanõuded:**

> **KOHUSTUSLIK**: MCP serverid **EI TOHI** vastu võtta ühtegi tokenit, mis ei ole selgesõnaliselt MCP serverile väljastatud

#### Autentimise ja autoriseerimise kontrollid

- **Range autoriseerimise ülevaatus**: Viia läbi põhjalikke auditeid MCP serveri autoriseerimisloogika kohta, et tagada juurdepääs tundlikele ressurssidele ainult kavandatud kasutajatele ja klientidele
  - **Rakendamise juhend**: [Azure API Management kui autentimislüüsi MCP serveritele](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identiteedi integratsioon**: [Microsoft Entra ID kasutamine MCP serveri autentimiseks](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Turvaline tokenite haldus**: Rakendada [Microsofti tokenite valideerimise ja elutsükli parimaid tavasid](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Kontrollida, et tokeni sihtrühma nõuded vastaksid MCP serveri identiteedile
  - Rakendada nõuetekohast tokenite rotatsiooni ja aegumispoliitikaid
  - Ennetada tokenite korduskasutamise rünnakuid ja volitamata kasutust

- **Kaitstud tokenite salvestus**: Turvaline tokenite salvestus krüpteerimisega nii puhke- kui ka ülekandeseisundis
  - **Parimad tavad**: [Turvalise tokenite salvestamise ja krüpteerimise juhised](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Juurdepääsukontrolli rakendamine

- **Minimaalse privileegi põhimõte**: Anda MCP serveritele ainult minimaalne vajalik juurdepääs kavandatud funktsionaalsuse jaoks
  - Regulaarne õiguste ülevaatus ja uuendamine, et vältida privileegide laienemist
  - **Microsofti dokumentatsioon**: [Turvaline minimaalsete privileegidega juurdepääs](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollipõhine juurdepääsukontroll (RBAC)**: Rakendada peenhäälestatud rollijaotusi
  - Kitsendada rolle konkreetsetele ressurssidele ja tegevustele
  - Vältida laialdasi või mittevajalikke õigusi, mis suurendavad ründepinda

- **Jätkuv õiguste jälgimine**: Rakendada pidevat juurdepääsu auditeerimist ja jälgimist
  - Jälgida õiguste kasutusmustreid anomaaliate tuvastamiseks
  - Kiirelt kõrvaldada liigsed või kasutamata privileegid

## AI-spetsiifilised turvaohtud

### Promptide süstimine ja tööriistade manipuleerimise rünnakud

Kaasaegsed MCP rakendused seisavad silmitsi keerukate AI-spetsiifiliste ründeteedega, mida traditsioonilised turvameetmed ei suuda täielikult käsitleda:

#### **Kaudne promptide süstimine (ristdomeeni promptide süstimine)**

**Kaudne promptide süstimine** on üks kriitilisemaid haavatavusi MCP-ga lubatud AI süsteemides. Ründajad peidavad pahatahtlikke juhiseid välises sisus — dokumentides, veebilehtedel, e-kirjades või andmeallikates — mida AI süsteemid seejärel töötlevad kui legitiimseid käske.

**Ründestseenid:**
- **Dokumendipõhine süstimine**: Pahatahtlikud juhised peidetud töödeldavatesse dokumentidesse, mis vallandavad soovimatuid AI toiminguid
- **Veebisisu ärakasutamine**: Kompromiteeritud veebilehed, mis sisaldavad manustatud promptisid, mis manipuleerivad AI käitumist kraapimisel
- **E-kirjade rünnakud**: Pahatahtlikud promptid e-kirjades, mis panevad AI assistendid lekkima infot või tegema volitamata toiminguid
- **Andmeallika saastamine**: Kompromiteeritud andmebaasid või API-d, mis pakuvad AI süsteemidele saastatud sisu

**Reaalne mõju**: Need rünnakud võivad põhjustada andmete väljaviimist, privaatsusrikkumisi, kahjuliku sisu genereerimist ja kasutajate interaktsioonide manipuleerimist. Üksikasjaliku analüüsi leiab [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Promptide süstimise rünnaku skeem](../../../translated_images/et/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Tööriistade mürgitamise rünnakud**

**Tööriistade mürgitamine** sihib MCP tööriistade metaandmeid, ärakasutades seda, kuidas LLM-id tõlgendavad tööriistade kirjeldusi ja parameetreid täitmisotsuste tegemiseks.

**Ründemehhanismid:**
- **Metaandmete manipuleerimine**: Ründajad süstivad pahatahtlikke juhiseid tööriistade kirjeldustesse, parameetrite määratlusse või kasutusnäidistesse
- **Nähtamatud juhised**: Peidetud promptid tööriistade metaandmetes, mida AI mudelid töötlevad, kuid mis on inimkasutajatele nähtamatud
- **Dünaamiline tööriistade muutmine ("Rug Pulls")**: Kasutajate poolt heaks kiidetud tööriistad muudetakse hiljem pahatahtlikeks ilma kasutaja teadmiseta
- **Parameetrite süstimine**: Pahatahtlik sisu tööriistade parameetrite skeemides, mis mõjutab mudeli käitumist

**Hostitud serverite riskid**: Kaug-MCP serverid kujutavad endast kõrgendatud riske, kuna tööriistade definitsioone saab pärast kasutaja esmast heakskiitu uuendada, luues olukordi, kus varem ohutud tööriistad muutuvad pahatahtlikeks. Üksikasjaliku analüüsi leiab [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tööriistade süstimise rünnaku skeem](../../../translated_images/et/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Täiendavad AI ründeteed**

- **Ristdomeeni promptide süstimine (XPIA)**: Keerukad rünnakud, mis kasutavad sisu mitmest domeenist turvakontrollide möödahiilimiseks
- **Dünaamiline võimekuse muutmine**: Reaalajas tööriistade võimekuse muutused, mis pääsevad esialgsetest turvaanalüüsidest mööda
- **Kontekstakna mürgitamine**: Rünnakud, mis manipuleerivad suurte kontekstakendega, et peita pahatahtlikke juhiseid
- **Mudeli segaduse rünnakud**: Mudeli piirangute ärakasutamine et luua ettearvamatuid või ebaturvalisi käitumisi

### AI turvariski mõju

**Kõrge mõjuga tagajärjed:**
- **Andmete väljaviimine**: Volitamata juurdepääs ja tundlike ettevõtte- või isikuandmete vargus
- **Privaatsusrikkumised**: Isikuandmete (PII) ja konfidentsiaalse ärilise teabe avalikustamine  
- **Süsteemi manipuleerimine**: Soovimatud muudatused kriitilistes süsteemides ja töövoogudes
- **Tunnuste vargus**: Autentimistokenite ja teenusetunnuste kompromiteerimine
- **Külgsuunaline liikumine**: Kompromiteeritud AI süsteemide kasutamine laiemate võrgurünnakute läbiviimiseks

### Microsofti AI turvalahendused

#### **AI Prompt Shields: täiustatud kaitse süstimisrünnakute vastu**

Microsofti **AI Prompt Shields** pakuvad põhjalikku kaitset nii otseste kui ka kaudsete promptide süstimisrünnakute vastu mitme turvakihi kaudu:

##### **Põhikaitse mehhanismid:**

1. **Täiustatud tuvastamine ja filtreerimine**
   - Masinõppe algoritmid ja NLP tehnikad tuvastavad pahatahtlikud juhised välises sisus
   - Reaalajas analüüs dokumentide, veebilehtede, e-kirjade ja andmeallikate manustatud ohtude jaoks
   - Kontekstuaalne arusaam legitiimsetest vs pahatahtlikest promptimustritest

2. **Valgustamise tehnikad**  
   - Eraldab usaldusväärsed süsteemijuhised potentsiaalselt kompromiteeritud välisest sisendist
   - Teksti transformeerimise meetodid, mis suurendavad mudeli asjakohasust ja isoleerivad pahatahtliku sisu
   - Aitab AI süsteemidel säilitada õiget juhiste hierarhiat ja ignoreerida süstitud käske

3. **Piiritleja ja andmemärgistussüsteemid**
   - Selge piiri määratlemine usaldusväärsete süsteemiteadete ja välise sisendi vahel
   - Erilised märgised, mis rõhutavad usaldusväärsete ja mitteusaldusväärsete andmeallikate piire
   - Selge eraldus takistab juhiste segadust ja volitamata käskude täitmist

4. **Jätkuv ohuteave**
   - Microsoft jälgib pidevalt uusi ründemustreid ja uuendab kaitseid
   - Proaktiivne ohuotsing uute süstimisvõtete ja ründeteede jaoks
   - Regulaarne turvamudelite uuendamine, et säilitada tõhusus arenevate ohtude vastu

5. **Azure Content Safety integratsioon**
   - Osa Azure AI Content Safety terviklikust paketist
   - Täiendav tuvastus jailbreaki katsete, kahjuliku sisu ja turvapoliitika rikkumiste jaoks
   - Ühtsed turvakontrollid AI rakenduse komponentide vahel

**Rakendamise ressursid**: [Microsoft Prompt Shields dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields kaitse](../../../translated_images/et/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Täiustatud MCP turvaohtud

### Sessiooni kaaperdamise haavatavused

**Sessiooni kaaperdamine** on kriitiline ründeteekond olelusessioonidega MCP rakendustes, kus volitamata isikud saavad kätte ja kuritarvitavad legitiimseid sessiooni identifikaatoreid, et esineda klientidena ja teha volitamata toiminguid.

#### **Ründestseenid ja riskid**

- **Sessiooni kaaperdamise promptide süstimine**: Ründajad varastatud sessiooni ID-dega süstivad pahatahtlikke sündmusi serveritesse, mis jagavad sessiooni olekut, mis võib vallandada kahjulikke toiminguid või pääseda tundlikele andmetele
- **Otsene esinemine**: Varastatud sessiooni ID-d võimaldavad otse MCP serveri kõnesid, mis mööduvad autentimisest, käsitledes ründajaid legitiimsete kasutajatena
- **Kompromiteeritud jätkusuutlikud vood**: Ründajad võivad päringuid enneaegselt lõpetada, põhjustades legitiimsete klientide jätkamise potentsiaalselt pahatahtliku sisuga

#### **Sessioonihalduse turvakontrollid**

**Kriitilised nõuded:**
- **Autoriseerimise kontroll**: MCP serverid, mis rakendavad autoriseerimist, **PEAVAD** kontrollima KÕIKI sissetulevaid päringuid ja **EI TOHI** tugineda autentimiseks sessioonidele
- **Turvaline sessiooni loomine**: Kasutage krüptograafiliselt turvalisi, mittedeterministlikke sessiooni-ID-sid, mis on genereeritud turvaliste juhuslike arvude generaatoritega
- **Kasutajaspetsiifiline sidumine**: Siduge sessiooni-ID-d kasutajaspetsiifilise infoga, kasutades vormingut nagu `<user_id>:<session_id>`, et vältida sessioonide väärkasutust kasutajate vahel
- **Sessiooni elutsükli haldus**: Rakendage nõuetekohane aegumine, rotatsioon ja tühistamine, et piirata haavatavuse aken
- **Transporditurve**: Kõigi sidekanalite puhul on HTTPS kohustuslik, et vältida sessiooni-ID vargust

### Segaduses esindaja probleem

**Segaduses esindaja probleem** tekib siis, kui MCP serverid toimivad autentimisproksidena klientide ja kolmandate osapoolte teenuste vahel, luues võimalusi autoriseerimise möödaviimiseks staatiliste kliendi-ID-de ärakasutamise kaudu.

#### **Rünnaku mehhanismid ja riskid**

- **Küpsisepõhine nõusoleku möödaviimine**: Varasem kasutaja autentimine loob nõusolekuküpsised, mida ründajad kasutavad pahatahtlike autoriseerimispäringute ja manipuleeritud suunamis-URI-de kaudu
- **Autoriseerimiskoodi vargus**: Olemasolevad nõusolekuküpsised võivad põhjustada, et autoriseerimisserverid vahele jätavad nõusoleku ekraanid ja suunavad koodid ründaja kontrollitud lõpp-punktidele  
- **Luba mittevajalik API ligipääs**: Varastatud autoriseerimiskoodid võimaldavad tokeni vahetust ja kasutaja identiteedi varjamist ilma selge heakskiiduta

#### **Leevendusstrateegiad**

**Kohustuslikud kontrollid:**
- **Selge nõusoleku nõue**: MCP proksiserverid, mis kasutavad staatilisi kliendi-ID-sid, **PEAVAD** saama kasutajalt nõusoleku iga dünaamiliselt registreeritud kliendi puhul
- **OAuth 2.1 turvalisuse rakendamine**: Järgige kehtivaid OAuth turvapraktikaid, sealhulgas PKCE (Proof Key for Code Exchange) kõigi autoriseerimispäringute puhul
- **Range kliendi valideerimine**: Rakendage ranget suunamis-URI-de ja kliendi identifikaatorite valideerimist, et vältida ärakasutamist

### Tokeni edasiandmise haavatavused  

**Tokeni edasiandmine** on selge anti-muster, kus MCP serverid aktsepteerivad kliendi tokeneid ilma nõuetekohase valideerimiseta ja edastavad need alluvatele API-dele, rikkudes MCP autoriseerimise spetsifikatsioone.

#### **Turvariskid**

- **Kontrolli möödaviimine**: Otsene kliendi ja API vaheline tokeni kasutamine möödub kriitilistest kiirusepiirangutest, valideerimisest ja jälgimisest
- **Auditijälje rikkumine**: Ülevalt väljastatud tokenid muudavad kliendi tuvastamise võimatuks, takistades intsidentide uurimist
- **Proksi kaudu andmete väljapressimine**: Valideerimata tokenid võimaldavad pahatahtlikel osapooltel kasutada servereid volitamata andmetele ligipääsuks
- **Usalduspiiri rikkumine**: Alluvad teenused võivad rikkuda usalduspiire, kui tokeni päritolu ei ole kontrollitav
- **Mitme teenuse rünnaku laienemine**: Kompromiteeritud tokenite aktsepteerimine mitmes teenuses võimaldab külgsuunalist liikumist

#### **Nõutavad turvakontrollid**

**Läbirääkimisteta nõuded:**
- **Tokeni valideerimine**: MCP serverid **EI TOHI** aktsepteerida tokeneid, mis ei ole selgesõnaliselt MCP serverile väljastatud
- **Sihtgrupi kontroll**: Alati valideerige, et tokeni sihtgrupi väited vastavad MCP serveri identiteedile
- **Õige tokeni elutsükkel**: Rakendage lühiajalisi ligipääsutokeneid koos turvalise rotatsioonipraktikaga


## Tarneahela turvalisus AI süsteemidele

Tarneahela turvalisus on arenenud traditsioonilistest tarkvarasõltuvustest kaugemale, hõlmates kogu AI ökosüsteemi. Kaasaegsed MCP rakendused peavad rangelt kontrollima ja jälgima kõiki AI-ga seotud komponente, kuna igaüks neist võib tuua sisse haavatavusi, mis ohustavad süsteemi terviklikkust.

### Laiendatud AI tarneahela komponendid

**Traditsioonilised tarkvarasõltuvused:**
- Avatud lähtekoodiga teegid ja raamistikud
- Konteineripildid ja baasüsteemid  
- Arendusvahendid ja ehitusliinid
- Infrastruktuuri komponendid ja teenused

**AI-spetsiifilised tarneahela elemendid:**
- **Põhimudelid**: Eeltreenitud mudelid erinevatelt pakkujatelt, mis vajavad päritolu kontrolli
- **Embedingu teenused**: Välised vektoriseerimise ja semantilise otsingu teenused
- **Konteksti pakkujad**: Andmeallikad, teadmistebaasid ja dokumendikogud  
- **Kolmandate osapoolte API-d**: Välised AI teenused, ML liinid ja andmetöötluse lõpp-punktid
- **Mudeli artefaktid**: Kaalud, konfiguratsioonid ja peenhäälestatud mudelivariandid
- **Treeningandmete allikad**: Andmekogud mudelite treenimiseks ja peenhäälestamiseks

### Kõikehõlmav tarneahela turvastrateegia

#### **Komponentide kontroll ja usaldus**
- **Päritolu valideerimine**: Kontrollige kõigi AI komponentide päritolu, litsentsi ja terviklikkust enne integreerimist
- **Turva hindamine**: Tehke haavatavuste skaneerimist ja turvaülevaateid mudelitele, andmeallikatele ja AI teenustele
- **Maine analüüs**: Hinnake AI teenusepakkujate turvatrükki ja praktikaid
- **Vastavuse kontroll**: Veenduge, et kõik komponendid vastavad organisatsiooni turva- ja regulatiivsetele nõuetele

#### **Turvalised juurutusliinid**  
- **Automatiseeritud CI/CD turvalisus**: Integreerige turvaskaneerimine kogu automatiseeritud juurutusliinidesse
- **Artefaktide terviklikkus**: Rakendage krüptograafilist valideerimist kõigi juurutatud artefaktide (kood, mudelid, konfiguratsioonid) puhul
- **Järkjärguline juurutus**: Kasutage progressiivseid juurutusstrateegiaid koos turvakontrolliga igas etapis
- **Usaldusväärsed artefaktide hoidlad**: Juurutage ainult kontrollitud ja turvalistest hoidlatest

#### **Jätkuv jälgimine ja reageerimine**
- **Sõltuvuste skaneerimine**: Jätkuv haavatavuste jälgimine kõigi tarkvara ja AI komponentide sõltuvuste puhul
- **Mudelite jälgimine**: Mudeli käitumise, jõudluse kõikumise ja turvaanomaliate pidev hindamine
- **Teenuste tervise jälgimine**: Väliste AI teenuste kättesaadavuse, turvaintsidentide ja poliitikamuudatuste jälgimine
- **Ohuteabe integreerimine**: AI ja ML turvariskidele spetsiifiliste ohuteabe voogude kaasamine

#### **Ligipääsukontroll ja minimaalne privileeg**
- **Komponentide tasandi õigused**: Piirake ligipääsu mudelitele, andmetele ja teenustele ärivajaduse alusel
- **Teenusekonto haldus**: Rakendage pühendatud teenusekontosid minimaalsete vajalike õigustega
- **Võrgu segmentatsioon**: Isolatsioon AI komponentide vahel ja piirake võrguliiklust teenuste vahel
- **API värava kontrollid**: Kasutage tsentraliseeritud API väravaid väliste AI teenuste ligipääsu kontrollimiseks ja jälgimiseks

#### **Intsidentidele reageerimine ja taastumine**
- **Kiired reageerimisprotseduurid**: Kehtestatud protsessid kompromiteeritud AI komponentide parandamiseks või asendamiseks
- **Tunnuste rotatsioon**: Automatiseeritud süsteemid saladuste, API võtmete ja teenuse mandaadi rotatsiooniks
- **Tagasikerimise võimalused**: Võime kiiresti taastada varasemad teada-töökorras AI komponendid
- **Tarneahela rikkumise taastumine**: Spetsiifilised protseduurid ülemiste AI teenuste kompromiteerimise korral

### Microsofti turvatööriistad ja integratsioon

**GitHub Advanced Security** pakub kõikehõlmavat tarneahela kaitset, sealhulgas:
- **Saladuste skaneerimine**: Automatiseeritud mandaadi, API võtmete ja tokenite tuvastamine hoidlates
- **Sõltuvuste skaneerimine**: Haavatavuste hindamine avatud lähtekoodiga sõltuvustele ja teekidele
- **CodeQL analüüs**: Staatiline koodi analüüs turvaaukude ja kodeerimisvigade leidmiseks
- **Tarneahela ülevaated**: Sõltuvuste tervise ja turvaseisundi nähtavus

**Azure DevOps ja Azure Repos integratsioon:**
- Sujuv turvaskaneerimise integreerimine Microsofti arendusplatvormidel
- Automatiseeritud turvakontrollid Azure Pipelines AI töökoormuste jaoks
- Poliitikate jõustamine turvaliseks AI komponentide juurutamiseks

**Microsofti sisemised praktikad:**
Microsoft rakendab ulatuslikke tarneahela turvapraktikaid kõigis toodetes. Tutvu tõestatud lähenemistega aadressil [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Põhiturvalisuse parimad praktikad

MCP rakendused pärivad ja arendavad teie organisatsiooni olemasolevat turvapositsiooni. Põhiturvalisuse tugevdamine parandab oluliselt AI süsteemide ja MCP juurutuste üldist turvalisust.

### Turvalisuse põhialused

#### **Turvalised arenduspraktikad**
- **OWASP vastavus**: Kaitse [OWASP Top 10](https://owasp.org/www-project-top-ten/) veebirakenduste haavatavuste vastu
- **AI-spetsiifilised kaitsed**: Rakendage kontrollid [OWASP Top 10 LLM-idele](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Turvaline saladuste haldus**: Kasutage pühendatud salvestusruume tokenite, API võtmete ja tundlike konfiguratsioonide jaoks
- **Lõpp-punkti krüpteerimine**: Rakendage turvaline side kõigi rakenduse komponentide ja andmevoogude vahel
- **Sisendi valideerimine**: Range valideerimine kõigi kasutajasisendite, API parameetrite ja andmeallikate puhul

#### **Infrastruktuuri tugevdamine**
- **Mitmefaktoriline autentimine**: Kohustuslik MFA kõigile administraatori- ja teenusekontodele
- **Paranduste haldus**: Automatiseeritud ja õigeaegne operatsioonisüsteemide, raamistikute ja sõltuvuste parandamine  
- **Identiteedipakkuja integratsioon**: Keskne identiteedihaldus ettevõtte identiteedipakkujate kaudu (Microsoft Entra ID, Active Directory)
- **Võrgu segmentatsioon**: MCP komponentide loogiline isoleerimine külgsuunalise liikumise piiramiseks
- **Vähemõiguste põhimõte**: Kõigi süsteemikomponentide ja kontode minimaalsete vajalike õiguste rakendamine

#### **Turvamonitooring ja avastamine**
- **Kõikehõlmav logimine**: Detailne logimine AI rakenduste tegevustest, sealhulgas MCP kliendi-serveri suhtlusest
- **SIEM integratsioon**: Keskne turvateabe ja sündmuste haldus anomaaliate avastamiseks
- **Käitumisanalüütika**: AI-põhine jälgimine süsteemi ja kasutajate ebatavaliste mustrite tuvastamiseks
- **Ohuteave**: Väliste ohuteabe voogude ja kompromiteerimise näitajate (IOC) kaasamine
- **Intsidentidele reageerimine**: Selgelt määratletud protseduurid turvaintsidentide avastamiseks, reageerimiseks ja taastumiseks

#### **Nullusaldus arhitektuur**
- **Ära usalda kunagi, kontrolli alati**: Kasutajate, seadmete ja võrguliideste pidev valideerimine
- **Mikrosegmentatsioon**: Täpsed võrgukontrollid, mis isoleerivad üksikuid töökoormusi ja teenuseid
- **Identiteedikeskne turvalisus**: Turvapoliitikad, mis põhinevad kontrollitud identiteetidel, mitte võrgu asukohal
- **Jätkuv riskihindamine**: Dünaamiline turvapositsiooni hindamine vastavalt kontekstile ja käitumisele
- **Tingimuslik ligipääs**: Ligipääsukontrollid, mis kohanduvad riskitegurite, asukoha ja seadme usaldusväärsuse põhjal

### Ettevõtte integratsioonimustrid

#### **Microsofti turvaökosüsteemi integratsioon**
- **Microsoft Defender for Cloud**: Kõikehõlmav pilve turvapositsiooni haldus
- **Azure Sentinel**: Pilvepõhine SIEM ja SOAR AI töökoormuste kaitseks
- **Microsoft Entra ID**: Ettevõtte identiteedi- ja ligipääsuhaldus tingimusliku ligipääsuga
- **Azure Key Vault**: Keskne saladuste haldus riistvaraturvalisuse mooduliga (HSM)
- **Microsoft Purview**: Andmehaldus ja vastavus AI andmeallikate ja töövoogude jaoks

#### **Vastavus ja haldus**
- **Regulatiivne kooskõla**: Veenduge, et MCP rakendused vastavad tööstusharu spetsiifilistele nõuetele (GDPR, HIPAA, SOC 2)
- **Andmete klassifitseerimine**: Tundlike andmete nõuetekohane kategoriseerimine ja käsitlemine AI süsteemides
- **Auditijäljed**: Kõikehõlmav logimine regulatiivseks vastavuseks ja kohtuekspertiisiks
- **Privaatsuskontrollid**: Privaatsus disainist lähtudes AI süsteemi arhitektuuris
- **Muudatuste haldus**: Formaalsed protsessid AI süsteemi muudatuste turvakontrolliks

Need põhiharjumused loovad tugeva turvapõhja, mis suurendab MCP-spetsiifiliste turvakontrollide tõhusust ja pakub kõikehõlmavat kaitset AI-põhiste rakenduste jaoks.

## Peamised turvakokkuvõtted

- **Kihiline turvalisus**: Kombineerige põhiturvalisuse praktikad (turvaline kodeerimine, minimaalne privileeg, tarneahela kontroll, pidev jälgimine) AI-spetsiifiliste kontrollidega kõikehõlmavaks kaitseks

- **AI-spetsiifiline ohumaastik**: MCP süsteemid seisavad silmitsi unikaalsete riskidega nagu promptide süstimine, tööriistamürgitus, sessioonikaaperdamine, segaduses esindaja probleemid, tokeni edasiandmise haavatavused ja liigne õiguste andmine, mis nõuavad spetsiaalseid leevendusi

- **Autentimise ja autoriseerimise tipptase**: Rakendage tugevat autentimist väliste identiteedipakkujate (Microsoft Entra ID) abil, jõustage nõuetekohane tokeni valideerimine ja ärge kunagi aktsepteerige tokeneid, mis ei ole selgesõnaliselt MCP serverile väljastatud

- **AI rünnakute ennetamine**: Kasutage Microsoft Prompt Shieldsi ja Azure Content Safetyt kaudsete promptide süstimise ja tööriistamürgituse rünnakute vastu kaitsmiseks, valideerides tööriistade metaandmeid ja jälgides dünaamilisi muutusi

- **Sessiooni ja transporditurve**: Kasutage krüptograafiliselt turvalisi, mittedeterministlikke sessiooni-ID-sid, mis on seotud kasutaja identiteediga, rakendage nõuetekohast sessiooni elutsükli haldust ja ärge kunagi kasutage sessioone autentimiseks

- **OAuth turvalisuse parimad praktikad**: Takistage segaduses esindaja rünnakuid selge kasutajanõusoleku kaudu dünaamiliselt registreeritud klientide puhul, nõuetekohase OAuth 2.1 rakendamisega PKCE-ga ja rangete suunamis-URI valideerimisega  

- **Tokeni turvapõhimõtted**: Vältige tokeni edasiandmise anti-mustreid, valideerige tokeni sihtgrupi väited, rakendage lühiajalisi tokeneid turvalise rotatsiooniga ja hoidke selgeid usalduspiire

- **Kõikehõlmav tarneahela turvalisus**: Kohtlege kõiki AI ökosüsteemi komponente (mudelid, embedud, konteksti pakkujad, välised API-d) sama rangusega nagu traditsioonilisi tarkvarasõltuvusi

- **Jätkuv areng**: Hoidke end kursis kiiresti arenevate MCP spetsifikatsioonidega, panustage turvakogukonna standarditesse ja säilitage kohanduv turvapositsioon protokolli küpsemisel

- **Microsofti turvaintegratsioon**: Kasutage Microsofti kõikehõlmavat turvaökosüsteemi (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) MCP juurutuse kaitseks

## Kõikehõlmavad ressursid

### **Ametlik MCP turvadokumentatsioon**
- [MCP spetsifikatsioon (kehtiv: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP turvalisuse parimad praktikad](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP autoriseerimise spetsifikatsioon](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub hoidla](https://github.com/modelcontextprotocol)

### **Turvastandardid ja parimad praktikad**
- [OAuth 2.0 turvalisuse parimad praktikad (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 veebirakenduste turvalisus](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 suurtele keelemudelitele](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **AI turvauuringud ja analüüs**
- [Promptide süstimine MCP-s (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tööriistamürgituse rünnakud (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP turvauuringu kokkuvõte (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsofti turvalahendused**
- [Microsoft Prompt Shields dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety teenus](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID turvalisus](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management parimad tavad](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Rakendamise juhendid ja õpetused**
- [Azure API Management kui MCP autentimislüüsi](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentimine MCP serveritega](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Turvaline tokeni salvestamine ja krüpteerimine (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps ja tarneahela turvalisus**
- [Azure DevOps turvalisus](https://azure.microsoft.com/products/devops)
- [Azure Repos turvalisus](https://azure.microsoft.com/products/devops/repos/)
- [Microsofti tarneahela turvalisuse teekond](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Täiendav turvadokumentatsioon**

Üldise turvajuhise saamiseks vaadake selles jaotises olevaid spetsialiseeritud dokumente:

- **[MCP turvalisuse parimad tavad 2025](./mcp-security-best-practices-2025.md)** - Täielik turvalisuse parimate tavade kogumik MCP rakendustele
- **[Azure Content Safety rakendamine](./azure-content-safety-implementation.md)** - Praktilised näited Azure Content Safety integreerimiseks  
- **[MCP turvakontrollid 2025](./mcp-security-controls-2025.md)** - Uusimad turvakontrollid ja tehnikad MCP juurutusteks
- **[MCP parimate tavade kiire viide](./mcp-best-practices.md)** - Kiire viide olulistele MCP turvapraktikatele

---

## Mis järgmiseks

Järgmine: [3. peatükk: Alustamine](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->