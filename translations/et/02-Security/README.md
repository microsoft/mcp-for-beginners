# MCP Turvalisus: Kõikehõlmav kaitse AI süsteemidele

[![MCP Turvalisuse Parimad Tavad](../../../translated_images/et/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klõpsa ülaloleval pildil selle õppetunni video vaatamiseks)_

Turvalisus on AI süsteemide kujunduse aluseks, mistõttu seame selle prioriteediks teises jaotises. See on kooskõlas Microsofti **Secure by Design** põhimõttega [Tuleviku Turvalisuse Algatusest](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Mudelikonteksti protokoll (MCP) toob AI-põhistele rakendustele võimsad uued võimalused, tuues samal ajal kaasa ainulaadsed turvaprobleemid, mis ulatuvad traditsiooniliste tarkvarariskide piiridest kaugemale. MCP süsteemid seisavad silmitsi nii väljakujunenud turvariskidega (turvaline kodeerimine, minimaalne ligipääs, tarneahela turvalisus) kui ka uute AI-spetsiifiliste ohtudega, sealhulgas päringu süstimine, tööriistamürgitus, sessiooni ülevõtmine, segadusse seotud volitused, tokeni läbilaske nõrkused ja dünaamilise võime muutmine.

See õppetund käsitleb kõige kriitilisemaid turvariske MCP rakendustes—sh autentimist, autoriseerimist, liigset õigust, kaudset päringu süstimist, sessiooni turvalisust, segadusse seotud volituste probleeme, tokenite haldamist ja tarneahela haavatavusi. Õpid rakendatavaid kontrolle ja parimaid tavasid nende riskide leevendamiseks, kasutades Microsofti lahendusi nagu Prompt Shields, Azure Content Safety ja GitHub Advanced Security oma MCP juurutamise tugevdamiseks.

## Õpieesmärgid

Selle õppetunni lõpuks oskad sa:

- **Tuvastada MCP-spetsiifilisi ohte**: Mõista MCP süsteemide ainulaadseid turvariske, sealhulgas päringu süstimist, tööriistamürgitust, liigseid õigusi, sessiooni ülevõtmist, segadusse seotud volituste probleeme, tokeni läbilaske nõrkusi ja tarneahela riske
- **Rakendada turvakontrulle**: Kasutada tõhusaid leevendusi, sh jõulist autentimist, minimaalset ligipääsu, turvalist tokenite haldamist, sessiooniturbe kontrolle ja tarneahela kontrolli
- **Kasutada Microsofti turvalahendusi**: Mõista ja rakendada Microsoft Prompt Shields, Azure Content Safety ja GitHub Advanced Security MCP töökoormuste kaitseks
- **Tööriistade turvalisuse valideerimine**: Mõista tööriista metainfo valideerimise tähtsust, dünaamiliste muudatuste jälgimist ja kaitset kaudsete päringu süstimise rünnakute vastu
- **Integreerida parimad tavad**: Ühendada väljakujunenud turvafundamendid (turvaline kodeerimine, serveri tugevdamine, null-usaldus) MCP-spetsiifiliste kontrollidega kõikehõlmava kaitse tagamiseks

# MCP turbe arhitektuur ja kontrollid

Kaasaegsed MCP rakendused nõuavad kihilisi turbelahendusi, mis käsitlevad nii traditsioonilist tarkvara turvalisust kui ka AI-spetsiifilisi ohte. Kiiresti arenev MCP spetsifikatsioon täiustab pidevalt oma turbekontrolle, võimaldades paremat integreerimist ettevõtete turbearhitektuuride ja parimate tavadega.

[Microsofti Digitaalse Kaitse Raport](https://aka.ms/mddr) uuringud näitavad, et **98% teatatud rikkumistest oleks saanud ära hoida tugeva turvahügieeni abil**. Kõige tõhusam kaitsestrateegia ühendab aluseks võetud turvatavad MCP-spetsiifiliste kontrollidega—proovitud baasjoone turvameetmed jäävad kõige mõjusamaks kogu turvariski vähendamisel.

## Praegune turvalisuse olukord

> **Märkus:** See peatükk ühendab väljakujunenud MCP turvakontrollid ja
> praegust **MCP Spetsifikatsioon 2026-07-28** autoriseerimise juhendit. Alati tutvu
> kehtiva [MCP Spetsifikatsiooniga](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHubi hoidla](https://github.com/modelcontextprotocol) ja
> [turvalisuse parimate tavade dokumentatsiooniga](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices),
> kui hakkad sisse viima turvatundlikku koodi.

> **Autoriseerimise uuendus:** MCP `2026-07-28` nõuab klientidelt, et nad valideeriksid
> `iss` parameetri autoriseerimisvastustes (RFC 9207) ning seoksid registreeritud
> volitused autoriseerimisserveriga. Dünaamiline kliendi registreerimine on aegunud;
> uued rakendused peaksid kasutama kliendi ID metaandmedokumente.
> Vaata [Mida MCP-s muudeti: 2026-07-28 spetsifikatsioon](../01-CoreConcepts/mcp-2026-07-28.md)
> autoriseerimise muudatuste täieliku nimekirja saamiseks.

## 🏔️ MCP Turbesummit Töötuba (Sherpa)

Tõhusa **praktikal põhineva turvakoolituse** jaoks soovitame soojalt **MCP Turbesummit Töötuba** (Sherpa) - põhjalik juhendatud ekspeditsioon MCP serverite turvamiseks Microsoft Azure keskkonnas.

### Töötuba ülevaade

[MCP Turbesummit Töötuba](https://azure-samples.github.io/sherpa/) pakub praktilist, rakendatavat turvakoolitust läbiproovitud "haavatav → ekspluateeri → parand → valideeri" metoodika kaudu. Sa:

- **Õpid vigade kaudu**: Koge haavatavusi otse, ärakasutades tahtlikult ebaturvalisi servereid
- **Kasutad Azure native turbet**: Rakendad Azure Entra ID, Key Vault, API Management ja AI Content Safety lahendusi
- **Järgid mitmekihilist kaitset**: Läbid laagrite kaupa kihilise turvasüsteemi ülesehituse
- **Rakendad OWASP standardeid**: Iga tehnika vastab [OWASP MCP Azure turbejuhisele](https://microsoft.github.io/mcp-azure-security-guide/)
- **Saad tootmiskoode**: Lahkud töökorras, testitud rakendustega

### Ekspeditsiooni marsruut

| Laager | Fookus | Kaetud OWASP riskid |
|------|-------|---------------------|
| **Baaskamp** | MCP põhialused & autentimishaavatavused | MCP01, MCP07 |
| **Laager 1: Identiteet** | OAuth 2.1, Azure hallatud identiteet, Key Vault | MCP01, MCP02, MCP07 |
| **Laager 2: Lüüsi** | API haldamine, privaatotsad, haldus | MCP02, MCP06, MCP07, MCP09 |
| **Laager 3: I/O Turvalisus** | Päringu süstimine, isikuandmete kaitse, sisuturvalisus | MCP03, MCP05, MCP06, MCP10 |
| **Laager 4: Jälgimine** | Logianalüütika, armatuurlaudad, ohtude tuvastamine | MCP04, MCP08 |
| **Tippkohtumine** | Punase ja sinise meeskonna integratsiooni test | Kõik |

**Alusta**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Turvariskid

[OWASP MCP Azure turbejuhend](https://microsoft.github.io/mcp-azure-security-guide/) kirjeldab kümmet kõige kriitilisemat turvariski MCP rakendustel:

| Risk | Kirjeldus | Azure leevendus |
|------|-------------|------------------|
| **MCP01** | Tokeni haldamise nõrkus ja saladuse lekkimine | Azure Key Vault, hallatud identiteet |
| **MCP02** | Õiguste eskaleerimine ulatusliku ligipääsuga | RBAC, tingimuslik juurdepääs |
| **MCP03** | Tööriistamürgitus | Tööriista valideerimine, terviklikkuse kontroll |
| **MCP04** | Tarkvara tarneahela rünnakud ja sõltuvuste rikkumised | GitHub Advanced Security, sõltuvuste skanneerimine |
| **MCP05** | Käskude süstimine ja käitamine | Sisendi valideerimine, liivakastimine |
| **MCP06** | Eesmärgipõhine voo alistamine | Azure AI Content Safety, Prompt Shields |

| **MCP07** | Ebapiisav autentimine ja volitamine | Azure Entra ID, OAuth 2.1 koos PKCE-ga |
| **MCP08** | Auditite ja telemeetria puudumine | Azure Monitor, Application Insights |
| **MCP09** | Varjatud MCP serverid | API Centeri haldus, võrgu isoleerimine |
| **MCP10** | Konteksti süstimine ja liigsed avaldamised | Andmeklassifikatsioon, minimaalne avalikustamine |

### MCP autentimise areng

MCP spetsifikatsioon on autentimise ja volitamise osas oluliselt arenenud:

- **Originaalne lähenemine**: Varasemad spetsifikatsioonid nõudsid arendajatelt kohandatud autentimisserverite loomist, kus MCP serverid tegid OAuth 2.0 volitamise serveritena kasutaja autentimise otse
- **Praegune standard (`2026-07-28`)**: MCP serverid võivad volitamise edasi anda
  välistele identiteediteenuse pakkujatele nagu Microsoft Entra ID. Kliendid peavad samuti
  rakendama käimasolevaid heakskiitja kinnitamise ning mandaadi sidumise nõudeid.
- **Transport Layer Security**: Täiustatud tugi turvalistele edastusmehhanismidele koos nõuetekohaste autentimismustritega nii kohapealsetele (STDIO) kui kaugühendustele (streamitav HTTP)

## Autentimise ja volitamise turvalisus

### Praegused turvalisuse väljakutsed

Moodsa MCP rakendused seisavad silmitsi mitmete autentimise ja volitamise probleemidega:

### Riskid ja ohugeneraatorid

- **Valesti konfigureeritud volitusloogika**: MCP serveri vigane volitusloogika võib paljastada tundlikke andmeid ja rakendada valesti juurdepääsukontrolli
- **OAuth tokeni kompromiteerimine**: Kohaliku MCP serveri tokeni vargus võimaldab ründajatel esineda serveri nime all ja pääseda alluvatele teenustele ligi
- **Tokeni edasiandmise haavatavused**: Ebaõige tokeni käsitlemine loob turvakontrollide möödaviimise ja vastutuse lüngad
- **Liigne õiguste andmine**: Üleõigustatud MCP serverid rikuvad vähemalt privileegi põhimõtet ja laiendavad rünnaku pindu

#### Tokeni edasiandmine: kriitiline anti-muster

**Tokeni edasiandmine on rangelt keelatud** praeguses MCP volitusspetsifikatsioonis tõsiste turvariskide tõttu:

##### Turvakontrollide möödaviimine
- MCP serverid ja alluvad API-d rakendavad kriitilisi turvakontrolle (kiiruse piiramine, päringute valideerimine, liikluse jälgimine), mis sõltuvad nõuetekohasest tokeni kontrollist
- Kliendi otsene tokeni kasutamine API puhul mööda neid kaitseid, alandades kogu turvaehitust

##### Vastutus ja auditeerimise väljakutsed  
- MCP serverid ei suuda teha vahet klientidel, kes kasutavad ülaltpoolt väljastatud tokeneid, seades auditid löögi alla
- Alluvate ressurssiserverite logid näitavad eksitavaid taotluse päritolukohti, mitte tegelikke MCP serveri vahendeid
- Intsidentide uurimine ja vastavuskontrollid muutuvad kordades keerulisemaks

##### Andmete väljaimemise riskid
- Kontrollimata tokeni nõuded võimaldavad varastatud tokenite väärkasutajatel kasutada MCP servereid vahendajatena andmete väljatõmbamiseks
- Usalduspiiri rikkumised lubavad volitamata juurdepääsumustreid, mis mööduvad kavandatud turvakontrollidest

##### Mitme teenuse rünnakusuunad
- Kompromiteeritud tokenid, mida aktsepteerivad mitmed teenused, võimaldavad lateraalset liikumist ühendatud süsteemides
- Teenustevahelised usaldusassumptsioonid võivad pettuda, kui tokeni päritolu ei ole tõendatav

### Turvakontrollid ja leevendused

**Olulised turvanõuded:**

> **KOHUSTUSLIK**: MCP serverid **EI TOHI** vastu võtta mingeid tokeneid, mis ei ole otseselt välja antud selle MCP serveri jaoks

#### Autentimise ja volitamise kontrollid

- **Range volituse ülevaatus**: Tõhusaid MCP serverite volitusloogikate auditsid, et tagada ainult ettenähtud kasutajate ja klientide juurdepääs tundlikele ressurssidele
  - **Rakendamisjuhend**: [Azure API Management kui MCP serverite autentimise värav](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identiteedi integratsioon**: [Microsoft Entra ID kasutamine MCP serveri autentimiseks](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Turvaline tokenihaldus**: Rakenda [Microsofti tokeni valideerimise ja elutsükli parimaid tavasid](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Kontrolli, et tokeni sihtkoht vastab MCP serveri identiteedile
  - Rakenda tokeni nõuetekohast pööramist ja aegumist
  - Ennetada tokeni replaysid ja volitamata kasutamist

- **Kaitstud tokeni salvestus**: Tokeni salvestus krüptimisega nii puhke- kui ülekandeajal
  - **Parimad praktikad**: [Turvaline tokeni salvestus ja krüpteerimise juhised](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Juurdepääsukontrolli rakendamine

- **Vähemate privileegide põhimõte**: Anna MCP serveritele ainult vajalikud minimaalset õigused kavandatud funktsionaalsuse jaoks
  - Regulaarne õiguste ülevaatus ja värskendus, et vältida privileegide laienemist
  - **Microsofti dokumentatsioon**: [Turvaline vähempõhiste õigustega juurdepääs](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rollipõhine juurdepääsukontroll (RBAC)**: Rakenda peenhäälestatud rollijaotusi
  - Kitsenda rolle spetsiifilistele ressurssidele ja toimingutele
  - Väldi laialdasi või mittevajalikke õigusi, mis suurendavad rünnaku pindu

- **Jätkuv õiguste jälgimine**: Rakenda pidevat juurdepääsu auditeerimist ja seiret
  - Jälgi õiguste kasutusmustreid kõrvalekallete suhtes
  - Kiirelt kõrvalda liigsed või kasutamata õigused

## Tehisintellekti spetsiifilised turvaohtud

### Käsu süstimise ja tööriistade manipuleerimise rünnakud

Moodsaid MCP rakendusi ähvardavad keerukad tehisintellekti-spetsiifilised rünnakusuunad, mida traditsioonilised turvameetmed ei suuda täielikult käsitleda:

#### **Kaudne käsu süstimine (ülaldomaini käsu süstimine)**

**Kaudne käsu süstimine** on üks kõige kriitilisemaid haavatavusi MCP-toega tehisintellekti süsteemides. Ründajad peidavad pahatahtlikke käske välises sisus – dokumentides, veebilehtedel, e-kirjades või andmeallikates –, mida tehisintellekt käsitleb hiljem legaalsete käskudena.

**Rünnakustsenaariumid:**
- **Dokumendipõhine süstimine**: Pahatahtlikud käsud peidetud töödeldavatesse dokumentidesse, mis vallandavad ettenägematud tehisintellekti toimingud
- **Veebisisu ärakasutamine**: Kompromiteeritud veebilehed, mis sisaldavad manustatud käske tehisintellekti käitumise mõjutamiseks, kui neid kraabitakse
- **E-kirjade baasil rünnakud**: Pahatahtlikud käsud e-kirjades, mis põhjustavad tehisabiliste informatsiooni lekkimist või volitamata toiminguid
- **Andmeallika reostus**: Kompromiteeritud andmebaasid või API-d, mis tarnivad reostunud sisu tehisintellektile

**Tegelik mõju**: Need rünnakud võivad viia andmete väljaimemiseni, privaatsusrikkumisteni, kahjuliku sisu genereerimiseni ja kasutajakogemuse manipuleerimiseni. Põhjalikuma analüüsi leiate siit: [Käsu süstimine MCP-s (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/et/prompt-injection.ed9fbfde297ca877.webp)

#### **Tööriistade mürgitamise rünnakud**

**Tööriistade mürgitamine** sihib MCP tööriistade metaandmeid, ärakasutades, kuidas LLM-id tõlgendavad tööriistakirjeldusi ja parameetreid täideviimist puudutavate otsustena.

**Rünnaku mehhanismid:**
- **Metaandmete manipuleerimine**: Ründajad süstivad pahatahtlikke käske tööriista kirjelduste, parameetri definitsioonide või kasutusnäidiste sisse
- **Nägematud juhised**: Peidetud käsud tööriista metaandmetes, mida tehisintellekt töötleb, kuid mis on inimestele nähtamatud
- **Dünaamiline tööriista muutmine („Rug Pulls“) **: Kasutajate poolt heakskiidetud tööriistad muudetakse hiljem pahatahtlikeks toiminguteks kasutaja teadmata
- **Parameetri süstimine**: Pahatahtlik sisu peidetakse tööriista parameetrite skeemidesse, mõjutades mudeli käitumist


**Hostitud serveri riskid**: Kaug-MCP serverid kujutavad endast tõstetud riske, kuna tööriistade määratlusi saab pärast kasutaja algset kinnitust uuendada, luues olukordi, kus varem ohutud tööriistad muutuvad pahatahtlikeks. Üksikasjalikuks analüüsiks vaadake [Tööriistamürgitusrünnakud (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tööriistasüsti rünnaku diagramm](../../../translated_images/et/tool-injection.3b0b4a6b24de6bef.webp)

#### **Täiendavad AI ründevektorid**

- **Ristdomeeni prompti süstimine (XPIA)**: Kvalifitseeritud rünnakud, mis kasutavad mitme domeeni sisu turvakontrollide läbimiseks
- **Dünaamiline võimekuse muutmine**: Tööriistade võimekuse reaalajas muutused, mis pääsevad esialgsest turvaanalüüsist
- **Kontekstuaalse akna mürgitamine**: Rünnakud, mis manipuleerivad suurte kontekstuaalsete akendega pahatahtlike juhiste peitmiseks
- **Mudeli segaduse rünnakud**: Mudeli piirangute ärakasutamine ettearvamatute või ebaturvaliste käitumiste loomiseks


### AI turvariskide mõju

**Kõrge mõjuga tagajärjed:**
- **Andmete väljapressimine**: Loata juurdepääs ja tundlike ettevõtte- või isikuandmete vargus
- **Privaatsusrikkumised**: Isikut tuvastava info (PII) ja konfidentsiaalsete ärandmete avalikustamine  
- **Süsteemi manipuleerimine**: Kriitiliste süsteemide ja töövoogude ettenägematud muudatused
- **Tuvastustunnuste vargus**: Autentimisvõtmete ja teenuse mandaadi kompromiteerimine
- **Lateral liikumine**: Rikutud AI süsteemide kasutamine võrgurünnakute laiemaks läbiviimiseks

### Microsoft AI turvalahendused

#### **AI prompt-kilbid: täiustatud kaitse süstimisrünnakute vastu**

Microsofti **AI prompt-kilbid** pakuvad kõikehõlmavat kaitset nii otseste kui ka kaudsete prompti süstimisrünnakute vastu mitmete turvakihte kaudu:

##### **Põhikaitse mehhanismid:**

1. **Täiustatud tuvastamine & filtreerimine**
   - Masinõppe algoritmid ja NLP tehnikad tuvastavad pahatahtlikud juhised välistes allikates
   - Reaalaegne dokumentide, veebilehtede, meilide ja andmeallikate analüüs sisse süstitud ohtude tuvastamiseks
   - Kontekstipõhine arusaam legitiimsete ja pahatahtlike promptimustrite vahel

2. **Valgustehnikad**  
   - Eristab usaldusväärseid süsteemijuhiseid võimalikult kompromiteeritud välissisestustest
   - Teksti teisendamise meetodid, mis parandavad mudeli asjakohasust samal ajal eraldades pahatahtliku sisu
   - Aitab AI süsteemidel hoida korrektset juhiste hierarhiat ja ignoreerida süstitud käske

3. **Piirajate ja andmemärgistus süsteemid**
   - Selge piiri määratlus usaldusväärsete süsteemiteadete ja välissisendi teksti vahel
   - Spetsiaalsed märgised rõhutavad piire usaldusväärsete ja mitteusaldusväärsete andmeallikate vahel
   - Selge eraldatus hoiab ära juhiste segaduse ja volitamata käskude täitmise

4. **Jätkuv ohuteave**
   - Microsoft jälgib pidevalt uusi ründemustreid ja uuendab kaitseid
   - Proaktiivne ohujaht uute süstimisrõhude ja ründevektorite leidmiseks
   - Regulaarne turvalahenduste täiendamine, et hoida kaitset arenevate ohtude vastu

5. **Azure sisuturve integratsioon**
   - Osa terviklikust Azure AI sisuturbe komplektist
   - Täiendav tuvastus purunemiskatsede, kahjuliku sisuga ja turvapoliitika rikkumiste jaoks
   - Ühtsed turvakontrollid AI rakenduse komponentide vahel

**Rakenduse ressursid**: [Microsoft Prompt Shields dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields kaitse](../../../translated_images/et/prompt-shield.ff5b95be76e9c78c.webp)


## Täiustatud MCP turvaohtud

### Seansi äravõtmise haavatavused

**Seansi äravõtmine** on kriitiline ründevektor seisundipõhistes MCP rakendustes, kus volitamata pooled saavad kätte ja kuritarvitavad legitiimseid seansi tunnuseid, et esineda klientidena ja teha volitamata toiminguid.

#### **Rünnakustsenaariumid & riskid**

- **Seansi äravõtu prompti süstimine**: Varastatud seansi ID-dega ründajad süstivad pahatahtlikke sündmusi serveritesse, mis jagavad seansiseisundit, potentsiaalselt vallandades kahjulikke tegevusi või pääsedes tundlikele andmetele ligi
- **Otse esinemine**: Varastatud seansi ID-d võimaldavad otse MCP serveri kõnesid, mis mööduvad autentimisest, käsitledes ründajaid kui legitiimseid kasutajaid
- **Kompromiteeritud taasalustatavad voogud**: Ründajad võivad päringuid ennetähtaegselt lõpetada, põhjustades legitiimsetel klientidel võimaliku pahatahtliku sisu taasalustamise

#### **Seansihalduse turvakontrollid**

**Kriitilised nõuded:**
- **Volituse kontroll**: MCP serverid, mis rakendavad volitust, PEAVAD kontrollima KÕIKI saabuvaid päringuid ja EI TOHI tugineda seanssidele autentimiseks
- **Turvalise seansi genereerimine**: Kasutada krüptograafiliselt turvalisi, mittetuvastatavaid seansi ID-sid, mis luuakse turvaliste juhuslike arvude generaatoritega
- **Kasutajapõhine sidumine**: Siduda seansi ID-d kasutajaspetsiifilise info külge vormingus `<user_id>:<session_id>` ristsessioonivarguse vältimiseks
- **Seansi elutsükli haldus**: Rakendada korralik aegumine, rotatsioon ja kehtetuks tegemine kitsendamaks haavatavusaknaid
- **Transporditurvalisus**: Kõigi sidekanalite jaoks kohustuslik HTTPS seansi IDde pealtkuulamise vältimiseks

### Segadusse aetud ametniku probleem

**Segadusse aetud ametniku probleem** tekib siis, kui MCP serverid toimivad autentimisproksidena klientide ja kolmandate osapoolte teenuste vahel, luues võimalused volituste möödapanemiseks staatiliste kliendi ID-de ärakasutamise kaudu.

#### **Rünnaku mehhanismid & riskid**

- **Cookie-põhine nõusoleku möödapääs**: Eelnev kasutajaautentimine loob nõusolekuküpsised, mida ründajad kasutavad pahatahtlike volituspäringute ja kavandatud ümbersuunamise URI-de abil
- **Volituskoodi vargus**: Olemasolevad nõusolekuküpsised võivad põhjustada volitusserverite nõusolekuekraani vahelejätmise, suunates koode ründajate kontrollitavatesse lõpp-punktidesse  
- **Loata API juurdepääs**: Varastatud volituskoodid võimaldavad tokenivahetust ja kasutaja esinemist ilma otsese heakskiiduta

#### **Leevendusstrateegiad**

**Kohustuslikud kontrollid:**
- **Selged nõusoleku nõuded**: MCP proksi serverid, mis kasutavad staatilisi kliendi ID-sid, PEAVAD saama iga dünaamiliselt registreeritud kliendi jaoks kasutaja nõusoleku
- **OAuth 2.1 turvalahenduste rakendamine**: Järgida praeguseid OAuth turbestandardeid, sealhulgas PKCE (Proof Key for Code Exchange) kõigi volituspäringute jaoks
- **Range kliendi valideerimine**: Rakendada ranget ümbersuunamise URI-de ja kliendi identifikaatorite valideerimist ekspluateerimise vältimiseks

### Tokeni läbipääsu haavatavused  

**Tokeni läbipääs** kujutab endast otsest anti-mustrit, kus MCP serverid võtavad vastu kliendi tokenid ilma korraliku valideerimiseta ja edastavad neid all-API-dele, rikkudes MCP volitusereegleid.

#### **Turvaimpakti**

- **Kontrollide möödapääs**: Otsene kliendi-API tokeni kasutamine möödub olulistest piiramis-, valideerimis- ja jälgimiskontrollidest
- **Auditirai jälje korruptsioon**: Ülaltpoolt väljastatud tokenid muudavad kliendi tuvastamise võimatuks, halvendades intsidentide uurimisvõimalusi
- **Proksipõhine andmete väljaandmine**: Mittevalideeritud tokenid lubavad pahatahtlikel osapooltel kasutada servereid proksidena loata andmetele juurdepääsuks
- **Usalduspiiri rikkumised**: Allteenuste usaldushoiakud võivad rikutud tokenite päritolu kontrollimisel
- **Mitme teenuse ründe laienemine**: Rikutud tokenite aktsepteerimine mitmetes teenustes võimaldab külgmist liikumist

#### **Nõutavad turvakontrollid**

**Läbirääkimisteta nõuded:**
- **Tokeni valideerimine**: MCP serverid EI TOHI vastu võtta tokeneid, mis pole selgesõnaliselt MCP serverile väljastatud
- **Sihtgrupi kontroll**: Alati kontrollida, et tokeni sihtrühmavaldised vastavad MCP serveri identiteedile
- **Õige tokeni elutsükkel**: Rakendada lühikese elueaga juurdepääsutokeneid koos turvalise rotatsioonipoliitikaga


## Tarneahela turvalisus AI süsteemidele

Tarneahela turvalisus on arenenud traditsioonilistest tarkvara sõltuvustest kogu AI ökosüsteemi hõlmavaks. Kaasaegsed MCP rakendused peavad rangelt kontrollima ja jälgima kõiki AI-komponente, kuna igaüks neist võib sisse tuua haavatavusi, mis ohustavad süsteemi terviklikkust.

### Laiendatud AI tarneahela komponendid

**Traditsioonilised tarkvara sõltuvused:**
- Avatud lähtekoodiga teegid ja raamistike
- Kasti-pildid ja baassüsteemid  
- Arendustööriistad ja ehitusliinid
- Taristu komponendid ja teenused

**AI-spetsiifilised tarneahela elemendid:**
- **Alusmudelid**: Erinevate pakkujate eelõpetatud mudelid, mis vajavad päritolu kontrolli
- **Embedimisteenused**: Väljaspool asuvad vektoritamis- ja semantilise otsingu teenused
- **Konteksti pakkujad**: Andmeallikad, teadmistebaasid ja dokumendirepositoriumid  
- **Kolmanda osapoole API-d**: Väline AI teenused, ML töövood ja andmetöötluse lõpp-punktid
- **Mudeli artefaktid**: Kaalud, konfiguratsioonid ja peenhäälestatud mudelivariandid
- **Õppematerjalide allikad**: Andmekogud mudelite treenimiseks ja peenhäälestamiseks

### Ülevaatav tarneahela turvastrateegia

#### **Komponendi kontroll ja usaldus**
- **Päritolu valideerimine**: Kontrollida kõigi AI komponentide päritolu, litsentsimist ja terviklikkust enne integreerimist
- **Turvaanalüüs**: Teostada haavatavuskontrolle ja turvakontrolli mudeleid, andmeallikaid ja AI teenuseid
- **Maine analüüs**: Hinnata AI teenuse pakkujate turvarekordeid ja -tavasid
- **Vastavuskontroll**: Veenduda, et kõik komponendid vastavad organisatsiooni turva- ja regulatiivsetele nõuetele

#### **Turvalised juurutusliinid**  
- **Automatiseeritud CI/CD turvakontrollid**: Integreerida turvaskaneerimine kogu automatiseeritud juurutusliinidesse
- **Artefakti terviklikkus**: Rakendada krüptograafiline kontroll kõigi juurutatud artefaktide (kood, mudelid, konfiguratsioonid) osas
- **Eraldatud juurutamine**: Kasutada progressiivseid juurutusstrateegiaid koos turvakontrolliga igal etapil
- **Usaldusväärsed artefaktiretseptorid**: Juurutada ainult kontrollitud ja turvalistest repositooriumitest

#### **Jätkuv jälgimine ja reageerimine**
- **Sõltuvuste skanneerimine**: Jätkuv haavatavuste jälgimine kõigi tarkvara- ja AI komponendide sõltuvuste osas
- **Mudelite monitooring**: Mudeli käitumise, jõudluse nihkete ja turvaveidete jätkuv hindamine
- **Teenuste tervise jälgimine**: Väliste AI teenuste saadavuse, turvaintsidentide ja poliitika muutuste jälgimine
- **Ohuteabe integratsioon**: Integreerida ohuteabe voo spetsiaalselt AI ja ML turvariskide jaoks

#### **Juurdepääsukontroll ja minimaalsete privileegide põhimõte**
- **Komponendipõhised õigused**: Piirata juurdepääsu mudelitele, andmetele ja teenustele vastavalt ärivajadusele
- **Teenusekonto haldus**: Rakendada pühendatud teenusekontosid minimaalse vajaliku õigusega
- **Võrgusegmentatsioon**: Isolatsioon AI komponentide ja teenuste vahel, piirates võrguvahelist ligipääsu
- **API värava kontrollid**: Kasutada tsentraliseeritud API väravaid väliste AI teenuste juurde pääsu kontrollimiseks ja jälgimiseks

#### **Intsidentidele reageerimine ja taastumine**
- **Kiired reageerimismenetlused**: Kehtestatud protsessid kompromiteeritud AI komponentide parandamiseks või asendamiseks
- **Tunnuste rotatsioon**: Automatiseeritud süsteemid saladuste, API võtmete ja teenuse mandaadi rotatsiooniks
- **Tagasi keeramise võimekus**: Võimalus kiiresti taastada eelnevalt teada-töökorras AI komponendi versioon
- **Tarneahela rikkumise taastamine**: Spetsiifilised protseduurid ülesvoolu AI teenuse kompromiteerimise korral reageerimiseks

### Microsofti turvatööriistad ja integratsioon

**GitHub Advanced Security** pakub kõikehõlmavat tarneahela kaitset, sh:
- **Saladuste skanneerimine**: Automatiseeritud autentimisandmete, API võtmete ja tokenite tuvastus repositooriumites
- **Sõltuvuste skanneerimine**: Haavatavuste hindamine avatud lähtekoodi sõltuvuste ja teekide jaoks
- **CodeQL analüüs**: Staatiline koodi analüüs turvaarkude ja kodeerimisvigade leidmiseks
- **Tarneahela ülevaated**: Nähtavus sõltuvuste tervise ja turvaseisu kohta

**Azure DevOpsi ja Azure Repos integratsioon:**
- Sujuv turvakontrollide integreerimine Microsofti arendusplatvormides
- Automatiseeritud turvakontrollid Azure Pipelines'is AI töökoormuste jaoks
- Poliitikate täitmine turvaliseks AI komponentide juurutamiseks

**Microsofti sisemised tavad:**
Microsoft rakendab põhjalikke tarneahela turvatavasid kõigis toodetes. Lisateavet tõestatud meetodite kohta leiate [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Turvalisuse aluspõhimõtted

MCP rakendused pärivad ja tugevdavad teie organisatsiooni olemasolevat turvastaatus. Aluspõhimõtete tugevdamine parandab märkimisväärselt AI süsteemide ja MCP juurutuste üldist turvalisust.

### Põhitõed turvalisuses

#### **Turvalised arendustavad**
- **OWASP nõuetele vastavus**: Kaitse [OWASP Top 10](https://owasp.org/www-project-top-ten/) veebirakenduste haavatavuste eest
- **AI-spetsiifilised kaitsed**: Rakendada [OWASP Top 10 LLMide jaoks](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Saladuste turvaline haldus**: Kasutada eraldi vault’e tokenite, API võtmete ja tundlike konfiguratsioonandmete jaoks
- **Lõpp-punkti krüptimine**: Rakendada turvaline side kõigis rakenduse komponentides ja andmevoogudes
- **Sisendi valideerimine**: Range kõigi kasutajasisestuste, API parameetrite ja andmeallikate valideerimine

#### **Taristu tugevdamine**
- **Mitmefaktoriline autentimine**: Kohustuslik MFA kõigi administraatori- ja teenusekontode jaoks
- **Paranduste haldus**: Automatiseeritud, õigel ajal tehtud parandused opsüsteemidele, raamistikutele ja sõltuvustele  
- **Identiteedipakkuja integratsioon**: Tsentraliseeritud identiteedihaldus ettevõtte identiteedipakkujate (Microsoft Entra ID, Active Directory) kaudu
- **Võrgusegmendid**: MCP komponentide loogiline isolatsioon külgsuunalise liikumise piiramiseks
- **Vähimate privileegide põhimõte**: Kõigi süsteemikomponentide ja kontode minimaalne vajalik õigus

#### **Turvalisuse jälgimine ja tuvastamine**
- **Kõikehõlmav logimine**: Detailne logimine AI rakenduse tegevustest, sealhulgas MCP kliendi-serveri suhtlusest
- **SIEM integratsioon**: Tsentraliseeritud turva-info ja sündmuste haldus anomaaliate tuvastamiseks
- **Käitumusanalüüs**: AI-põhine monitooring süsteemi ja kasutaja tavatu käitumise märkamiseks
- **Ohuteave**: Väliste ohuteabe voogude ja kompromissimismärkide (IOC) integreerimine
- **Intsidentidele reageerimine**: Hästi määratletud protseduurid turvaintsidentide tuvastamiseks, reageerimiseks ja taastumiseks

#### **Zero Trust arhitektuur**
- **Ära usalda kunagi, kontrolli alati**: Kasutajate, seadmete ja võrguliikluse pidev valideerimine
- **Mikrosegmentatsioon**: Peened võrguvaldkonnad, mis isoleerivad üksikuid töökoormusi ja teenuseid
- **Identiteedikeskne turvalisus**: Turvapoliitikad, mis põhinevad kontrollitud identiteetidel mitte võrgukohtadel
- **Jätkuv riskihindamine**: Dünaamiline turvastaatuse hindamine praeguse konteksti ja käitumise põhjal
- **Tingimustel juurdepääs**: Juurdepääsukontrollid, mis kohanduvad riskitegurite, asukoha ja seadme usaldusväärsuse alusel

### Ettevõtte integratsioonimudelid

#### **Microsofti turvaökosüsteemi integratsioon**
- **Microsoft Defender for Cloud**: Kõikehõlmav pilve turvastaatuse haldus
- **Azure Sentinel**: Pilvel põhinev SIEM ja SOAR võimekused AI töökoormuste kaitseks
- **Microsoft Entra ID**: Ettevõtte identiteedi- ja juurdepääsuhaldus tingimusjuurdepääsetega
- **Azure Key Vault**: Tsentraliseeritud saladuste haldus riistvaraturvalisusega (HSM)
- **Microsoft Purview**: Andmete valitsemine ja vastavus AI andmeallikate ja töövoogude jaoks

#### **Vastavus ja juhtimine**
- **Regulatiivne vastavus**: Veendumine, et MCP rakendused täidavad tööstusharu spetsiifilisi nõudeid (GDPR, HIPAA, SOC 2)

- **Andmete klassifitseerimine**: Tundlike andmete õige kategooriate määramine ja töötlemine, mida haldavad AI süsteemid  
- **Auditijäljed**: Üksikasjalik logimine regulatiivsete nõuete täitmiseks ja kohtuekspertiisi uurimiseks  
- **Privaatsuskontrollid**: Privaatsuse disainipõhimõtete rakendamine AI süsteemi arhitektuuris  
- **Muudatuste juhtimine**: Formaalsed protsessid AI süsteemi muudatuste turvakontrollide jaoks  

Need põhiharjumused loovad tugeva turvalisuse aluspinna, mis suurendab MCP-spetsiifiliste turvakontrollide efektiivsust ja tagab tervikliku kaitse AI-põhistele rakendustele.  

## Peamised turvalisuse võtmejäreldused  

- **Samm-sammult kihiline turvalisus**: Ühenda põhiturvapraktikad (turvaline kodeerimine, minimaalne õiguste tase, tarneahela kontroll, pidev järelevalve) AI-spetsiifiliste kontrolleritega tervikliku kaitse tagamiseks  

- **AI-spetsiifiline ohut maastik**: MCP süsteemidel on unikaalsed riskid nagu promptide süstimine, tööriistamürgitus, sessioonikaaperdamine, segaduses volinikuprobleemid, tokenite läbipääsu haavatavused ja liigne õiguste võtmine, mis vajavad spetsiaalseid leevendusi  

- **Autentimise ja autoriseerimise tipptase**: Rakenda tugevat autentimist väliste identiteedipakkujate (Microsoft Entra ID) abil, kehtesta korrektne tokeni valideerimine, ning ära kunagi aktsepteeri tokeneid, mis pole selgesõnaliselt välja antud sinu MCP serverile  

- **AI rünnakute ennetamine**: Kasuta Microsoft Prompt Shieldsi ja Azure Content Safety’d kaudsete promptide süstimiste ja tööriistamürgitusrünnakute vastu kaitsmiseks, kontrollides samal ajal tööriistade metadataid ja jälgides dünaamilisi muutusi  

- **Sessiooni ja transpordi turvalisus**: Kasuta krüptograafiliselt turvalisi, mitte-determineerivaid sessiooni ID-sid, mis on seotud kasutaja identiteediga, rakenda korralikku sessiooni elutsükli haldust ning ära kunagi kasuta sessioone autentimiseks  

- **OAuth turvalisuse parimad tavad**: Ennetage segaduses voliniku rünnakuid kasutajalt selgesõnalise nõusoleku saamisega dünaamiliselt registreeritud klientide puhul, korraliku OAuth 2.1 PKCE täitmisega ning ranged ümber suunamise (redirect URI) valideerimisega  

- **Tokeni turvalisuse põhimõtted**: Väldi tokeni läbipääsu antipatju, valideeri tokeni sihtrühma (audience) väited, rakenda lühikese elueaga tokeneid turvalise rotatsiooniga ning säilita selged usalduspiirid  

- **Tarneahela terviklik turvalisus**: Käsitle kõiki AI ökosüsteemi komponente (mudelid, manused, kontekstipakkujad, välised API-d) sama kõrge turvatasemega nagu traditsioonilisi tarkvarasõltuvusi  

- **Pidev areng**: Jälgi kiirelt arenevaid MCP spetsifikatsioone, panusta turvakeskonna standarditesse ning hoia turvapositsioon kohanduvana protokolli küpsemisega  

- **Microsofti turvaintegratsioon**: Kasuta Microsofti ulatuslikku turvaökosüsteemi (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) MCP paigalduse tugevdamiseks  

## Terviklikud ressursid  

### **Ametlik MCP turvadokumentatsioon**  
- [MCP Spetsifikatsioon (Praegune: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)  
- [MCP turvalisuse parimad tavad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)  
- [MCP autoriseerimise spetsifikatsioon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)  
- [MCP GitHub hoidla](https://github.com/modelcontextprotocol)  

### **OWASP MCP turvaressursid**  
- [OWASP MCP Azure turva juhend](https://microsoft.github.io/mcp-azure-security-guide/) - Üksikasjalik OWASP MCP Top 10 koos Azure’i rakenduse juhistega  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Ametlikud OWASP MCP turvariskid  
- [MCP turvasummiti töötuba (Sherpa)](https://azure-samples.github.io/sherpa/) - Käed-külge turvaõpe MCP jaoks Azure’is  

### **Turvastandardid ja parimad tavad**  
- [OAuth 2.0 turvapõhimõtted (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 veebi rakenduste turvalisus](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 suurte keelemudelite jaoks](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsofti digitaalse kaitse aruanne](https://aka.ms/mddr)  

### **AI turvauuringud ja analüüsid**  
- [Promptide süstimine MCP-s (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Tööriistamürgitusrünnakud (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [MCP turvauuringu kokkuvõte (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)  

### **Microsofti turvalahendused**  
- [Microsoft Prompt Shields dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety teenus](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Microsoft Entra ID turvalisus](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [Azure tokenihalduse parimad tavad](https://learn.microsoft.com/entra/identity-platform/access-tokens)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Rakendamise juhendid ja õpetused**  
- [Azure API Management MCP autentimise väravana](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Microsoft Entra ID autentimine MCP serveritega](https://den.dev/blog/mcp-server-auth-entra-id-session/)  
- [Turvalise tokenisalvestuse ja krüpteerimise video](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)  

### **DevOps ja tarneahela turvalisus**  
- [Azure DevOps turvalisus](https://azure.microsoft.com/products/devops)  
- [Azure Repos turvalisus](https://azure.microsoft.com/products/devops/repos/)  
- [Microsofti tarneahela turvamise teekond](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)  

## **Täiendav turvadokumentatsioon**  

Üksikasjaliku turvasuuna jaoks vaata selles oluliste dokumentide sektsioonis:  

- **[CIMD ja DCR autoriseerimise näide](./samples/cimd-dcr-auth/README.md)** - Käivitatav TypeScript MCP `2026-07-28` ressursserver, mis võrdleb eelistatud kliendi ID metadata dokumente aegunud dünaamilise kliendiregistreerimise tagavaraga  
- **[MCP turvalisuse parimad tavad](./mcp-security-best-practices.md)** - Täielikud turvapraktikad MCP rakenduste jaoks  
- **[Azure Content Safety rakendamine](./azure-content-safety-implementation.md)** - Praktilised rakendamise näited Azure Content Safety integreerimiseks  
- **[MCP turvakontrollerid](./mcp-security-controls.md)** - Uusimad turvakontrollerid ja tehnikad MCP paigaldiste jaoks  
- **[MCP parimate tavade kiire juhend](./mcp-best-practices.md)** - Kiire juhend oluliste MCP turvapraktikate kohta  
- **[BlueHat 2026: AI tuleviku kindlustamine: MCP kaitse defentsi kihistusega mustritega](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Defentsi kihistusega mustrid Microsoft Security Response Center’ilt (MSRC)  

### **Käed-külge turvakoolitus**  

- **[MCP turvasummiti töötuba (Sherpa)](https://azure-samples.github.io/sherpa/)** - Ulatuslik praktiline töötuba MCP serverite kindlustamiseks Azure’is koos järkjärguliste laagritega Baaskampist Summiti tasemele  
- **[OWASP MCP Azure turvajuhend](https://microsoft.github.io/mcp-azure-security-guide/)** - Viitearhitektuur ja rakendusjuhised kõigi OWASP MCP Top 10 riskide jaoks  

---

## Mis järgmiseks  

Järgmiseks: [3. peatükk: Alustamine](../03-GettingStarted/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->