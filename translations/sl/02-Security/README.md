# MCP Varnost: Celovita zaščita za AI sisteme

[![MCP Security Best Practices](../../../translated_images/sl/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Kliknite na zgornjo sliko za ogled videa te lekcije)_

Varnost je temeljna za oblikovanje AI sistemov, zato ji namenjamo posebno pozornost kot drugi del vsebine. To je v skladu s Microsoftovim načelom **Secure by Design** iz [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) prinaša močne nove zmogljivosti za aplikacije, ki temeljijo na AI, hkrati pa uvaja edinstvene varnostne izzive, ki presegajo tradicionalna tveganja programske opreme. Sistemi MCP se soočajo tako z uveljavljenimi varnostnimi vprašanji (varno kodiranje, najmanjše privilegije, varnost dobavne verige) kot z novimi grožnjami, specifičnimi za AI, vključno z injiciranjem pozivov, zastrupljanjem orodij, prevzemom sej, napadi z zmedenim pooblaščencem, ranljivostmi pri prenosu žetonov in dinamičnimi spremembami zmogljivosti.

Ta lekcija raziskuje najpomembnejša varnostna tveganja pri implementacijah MCP — pokriva preverjanje pristnosti, avtorizacijo, prekomerne pravice, posredno injiciranje pozivov, varnost sej, težave z zmedenim pooblaščencem, upravljanje žetonov in ranljivosti dobavne verige. Naučili se boste izvedljivih kontrol in najboljših praks za ublažitev teh tveganj ter uporabe Microsoftovih rešitev, kot so Prompt Shields, Azure Content Safety in GitHub Advanced Security, za krepitev vaše MCP namestitve.

## Cilji učenja

Do konca te lekcije boste znali:

- **Prepoznati grožnje specifične za MCP**: Prepoznati edinstvena varnostna tveganja v MCP sistemih, vključno z injiciranjem pozivov, zastrupljanjem orodij, prekomernimi dovoljenji, prevzemom sej, težavami z zmedenim pooblaščencem, ranljivostmi pri prenosu žetonov in tveganji dobavne verige
- **Uporabiti varnostne kontrole**: Izvesti učinkovite ukrepe, vključno z robustnim preverjanjem pristnosti, dostopom z najmanjšimi privilegiji, varnim upravljanjem žetonov, kontrolami varnosti sej in preverjanjem dobavne verige
- **Izkoristiti Microsoftove varnostne rešitve**: Razumeti in implementirati Microsoft Prompt Shields, Azure Content Safety in GitHub Advanced Security za zaščito delovnih obremenitev MCP
- **Preveriti varnost orodij**: Prepoznati pomen validacije metapodatkov orodij, spremljanja dinamičnih sprememb in obrambe pred posrednimi napadi injiciranja pozivov
- **Integrirati najboljše prakse**: Združiti uveljavljene varnostne temelje (varno kodiranje, utrjevanje strežnika, zero trust) z MCP-specifičnimi kontrolami za celovito zaščito

# Arhitektura in kontrole MCP varnosti

Sodobne implementacije MCP zahtevajo večplastne varnostne pristope, ki naslovijo tako tradicionalno varnost programske opreme kot tudi grožnje, specifične za AI. Hitro razvijajoča se specifikacija MCP še naprej zori v svojih varnostnih kontrolah, kar omogoča boljšo integracijo z varnostnimi arhitekturami podjetij in uveljavljenimi najboljšimi praksami.

Raziskave iz [Microsoft Digital Defense Report](https://aka.ms/mddr) kažejo, da bi **98 % prijavljenih kršitev preprečila robustna varnostna higiena**. Najbolj učinkovita strategija zaščite združuje temeljne varnostne prakse z MCP-specifičnimi kontrolami — preverjene osnovne varnostne ukrepe ostajajo najpomembnejši za zmanjšanje skupnega varnostnega tveganja.

## Trenutno varnostno stanje

> **Opomba:** Te informacije odražajo varnostne standarde MCP stanja na dan **18. december 2025**. Protokol MCP se hitro razvija, prihodnje implementacije lahko uvedejo nove vzorce preverjanja pristnosti in izboljšane kontrole. Vedno se sklicujte na aktualno [MCP specifikacijo](https://spec.modelcontextprotocol.io/), [MCP GitHub repozitorij](https://github.com/modelcontextprotocol) in [dokumentacijo najboljših varnostnih praks](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) za najnovejša navodila.

### Evolucija preverjanja pristnosti MCP

Specifikacija MCP se je bistveno razvila v pristopu k preverjanju pristnosti in avtorizaciji:

- **Izvirni pristop**: Zgodnje specifikacije so zahtevale, da razvijalci implementirajo lastne strežnike za preverjanje pristnosti, pri čemer so MCP strežniki delovali kot OAuth 2.0 avtorizacijski strežniki, ki so neposredno upravljali preverjanje pristnosti uporabnikov
- **Trenutni standard (2025-11-25)**: Posodobljena specifikacija omogoča MCP strežnikom delegiranje preverjanja pristnosti zunanjim ponudnikom identitete (kot je Microsoft Entra ID), kar izboljšuje varnostni položaj in zmanjšuje kompleksnost implementacije
- **Varnost transportne plasti**: Izboljšana podpora za varne transportne mehanizme z ustreznimi vzorci preverjanja pristnosti za lokalne (STDIO) in oddaljene (Streamable HTTP) povezave

## Varnost preverjanja pristnosti in avtorizacije

### Trenutni varnostni izzivi

Sodobne implementacije MCP se soočajo z več izzivi pri preverjanju pristnosti in avtorizaciji:

### Tveganja in vektorji napadov

- **Napačno konfigurirana avtorizacijska logika**: Napake v implementaciji avtorizacije v MCP strežnikih lahko razkrijejo občutljive podatke in nepravilno uporabijo kontrole dostopa
- **Kompromitacija OAuth žetonov**: Kraja žetonov lokalnih MCP strežnikov omogoča napadalcem, da se predstavljajo kot strežniki in dostopajo do nadaljnjih storitev
- **Ranljivosti pri prenosu žetonov**: Nepravilno ravnanje z žetoni ustvarja obvoze varnostnih kontrol in vrzeli v odgovornosti
- **Prekomerne pravice**: MCP strežniki z več privilegiji kot je potrebno kršijo načelo najmanjših privilegijev in povečujejo površino napada

#### Prenos žetonov: kritičen anti-vzorec

**Prenos žetonov je izrecno prepovedan** v trenutni MCP specifikaciji avtorizacije zaradi hudih varnostnih posledic:

##### Obhod varnostnih kontrol
- MCP strežniki in nadaljnji API-ji izvajajo ključne varnostne kontrole (omejevanje hitrosti, validacija zahtev, spremljanje prometa), ki so odvisne od pravilne validacije žetonov
- Neposredna uporaba žetonov od odjemalca do API-ja obide te bistvene zaščite in podira varnostno arhitekturo

##### Izzivi odgovornosti in revizije  
- MCP strežniki ne morejo razlikovati med odjemalci, ki uporabljajo žetone, izdane zgoraj, kar podira revizijske sledi
- Dnevniki strežnikov virov prikazujejo zavajajoče izvore zahtev namesto dejanskih MCP strežnikov kot posrednikov
- Preiskave incidentov in revizije skladnosti postanejo bistveno težje

##### Tveganja iztoka podatkov
- Nevalidirani zahtevki žetonov omogočajo zlonamernim akterjem s ukradenimi žetoni uporabo MCP strežnikov kot proxyjev za iztok podatkov
- Kršitve mej zaupanja omogočajo nepooblaščen dostop, ki obide predvidene varnostne kontrole

##### Večstoritevni vektorji napadov
- Kompromitirani žetoni, sprejeti pri več storitvah, omogočajo lateralno gibanje po povezanih sistemih
- Predpostavke zaupanja med storitvami so lahko kršene, če izvora žetonov ni mogoče preveriti

### Varnostne kontrole in ublažitve

**Ključne varnostne zahteve:**

> **OBVEZNO**: MCP strežniki **NE SMEJO** sprejemati nobenih žetonov, ki niso izrecno izdani za MCP strežnik

#### Kontrole preverjanja pristnosti in avtorizacije

- **Stroga revizija avtorizacije**: Izvedite celovite preglede avtorizacijske logike MCP strežnikov, da zagotovite, da do občutljivih virov dostopajo le predvideni uporabniki in odjemalci
  - **Vodnik za implementacijo**: [Azure API Management kot avtorizacijski prehod za MCP strežnike](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integracija identitete**: [Uporaba Microsoft Entra ID za preverjanje pristnosti MCP strežnikov](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Varno upravljanje žetonov**: Uporabite [Microsoftove najboljše prakse za validacijo in življenjski cikel žetonov](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validirajte zahtevke občinstva žetona, da se ujemajo z identiteto MCP strežnika
  - Uvedite pravilno rotacijo in potek žetonov
  - Preprečite ponovne napade z žetoni in nepooblaščeno uporabo

- **Zaščiteno shranjevanje žetonov**: Varno shranjujte žetone z uporabo šifriranja tako v mirovanju kot med prenosom
  - **Najboljše prakse**: [Varnostno shranjevanje in smernice za šifriranje žetonov](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementacija kontrole dostopa

- **Načelo najmanjših privilegijev**: MCP strežnikom dodelite le minimalna dovoljenja, potrebna za predvideno funkcionalnost
  - Redni pregledi in posodobitve dovoljenj za preprečevanje kopičenja privilegijev
  - **Microsoftova dokumentacija**: [Varni dostop z najmanjšimi privilegiji](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Dostop na osnovi vlog (RBAC)**: Implementirajte natančne dodelitve vlog
  - Omejite vloge na specifične vire in dejanja
  - Izogibajte se širokim ali nepotrebnim dovoljenjem, ki povečujejo površino napada

- **Neprestano spremljanje dovoljenj**: Izvedite stalno revizijo in spremljanje dostopa
  - Spremljajte vzorce uporabe dovoljenj za odstopanja
  - Hitro odpravite prekomerne ali neuporabljene privilegije

## Grožnje, specifične za AI

### Napadi injiciranja pozivov in manipulacije orodij

Sodobne implementacije MCP se soočajo z zapletenimi AI-specifičnimi vektorji napadov, ki jih tradicionalni varnostni ukrepi ne morejo v celoti nasloviti:

#### **Posredno injiciranje pozivov (Cross-Domain Prompt Injection)**

**Posredno injiciranje pozivov** predstavlja eno najpomembnejših ranljivosti v AI sistemih, omogočenih z MCP. Napadalci vstavijo zlonamerna navodila v zunanje vsebine — dokumente, spletne strani, e-pošto ali podatkovne vire — ki jih AI sistemi nato obdelajo kot legitimna ukaza.

**Scenariji napadov:**
- **Injiciranje v dokumentih**: Zlonamerna navodila skrita v obdelanih dokumentih, ki sprožijo neželena AI dejanja
- **Izkoriščanje spletnih vsebin**: Kompromitirane spletne strani z vgrajenimi pozivi, ki manipulirajo vedenje AI ob strganju vsebine
- **Napadi preko e-pošte**: Zlonamerni pozivi v e-pošti, ki povzročijo, da AI asistenti razkrijejo informacije ali izvajajo nepooblaščena dejanja
- **Kontaminacija podatkovnih virov**: Kompromitirane baze podatkov ali API-ji, ki AI sistemom servirajo okuženo vsebino

**Dejanski vpliv**: Ti napadi lahko povzročijo iztok podatkov, kršitve zasebnosti, generiranje škodljive vsebine in manipulacijo uporabniških interakcij. Za podrobno analizo glejte [Prompt Injection v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/sl/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Napadi z zastrupljanjem orodij**

**Zastrupljanje orodij** cilja na metapodatke, ki definirajo MCP orodja, z izkoriščanjem načina, kako LLM-ji interpretirajo opise orodij in parametre za odločanje o izvajanju.

**Mehanizmi napadov:**
- **Manipulacija metapodatkov**: Napadalci vstavijo zlonamerna navodila v opise orodij, definicije parametrov ali primere uporabe
- **Nevidna navodila**: Skriti pozivi v metapodatkih orodij, ki jih AI modeli obdelajo, a so nevidni človeškim uporabnikom
- **Dinamične spremembe orodij ("Rug Pulls")**: Orodja, ki jih uporabniki odobrijo, so kasneje spremenjena za izvajanje zlonamernih dejanj brez vednosti uporabnika
- **Injiciranje parametrov**: Zlonamerna vsebina v shemah parametrov orodij, ki vpliva na vedenje modela

**Tveganja gostujočih strežnikov**: Oddaljeni MCP strežniki predstavljajo povečana tveganja, saj se definicije orodij lahko posodobijo po začetnem odobritvi uporabnika, kar ustvarja scenarije, kjer prej varna orodja postanejo zlonamerna. Za celovito analizo glejte [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/sl/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Dodatni AI vektorji napadov**

- **Cross-Domain Prompt Injection (XPIA)**: Zapleteni napadi, ki izkoriščajo vsebino iz več domen za obhod varnostnih kontrol
- **Dinamične spremembe zmogljivosti**: Spremembe zmogljivosti orodij v realnem času, ki uidejo začetnim varnostnim ocenam
- **Zastrupljanje kontekstnega okna**: Napadi, ki manipulirajo velika kontekstna okna za skrivanje zlonamernih navodil
- **Napadi z zmedo modela**: Izkoriščanje omejitev modela za ustvarjanje nepredvidljivih ali nevarnih vedenj

### Vpliv varnostnih tveganj AI

**Posledice z visokim vplivom:**
- **Iztok podatkov**: Nepooblaščen dostop in kraja občutljivih podatkov podjetja ali osebnih podatkov
- **Kršitve zasebnosti**: Razkritje osebnih identifikacijskih podatkov (PII) in zaupnih poslovnih informacij  
- **Manipulacija sistemov**: Neželjene spremembe kritičnih sistemov in delovnih tokov
- **Kraja poverilnic**: Kompromitacija žetonov za preverjanje pristnosti in poverilnic storitev
- **Lateralno gibanje**: Uporaba kompromitiranih AI sistemov kot odskočnih desk za širše omrežne napade

### Microsoftove rešitve za varnost AI

#### **AI Prompt Shields: Napredna zaščita pred injiciranjem pozivov**

Microsoft **AI Prompt Shields** nudijo celovito obrambo pred neposrednimi in posrednimi napadi injiciranja pozivov z več varnostnimi plastmi:

##### **Glavni zaščitni mehanizmi:**

1. **Napredno zaznavanje in filtriranje**
   - Algoritmi strojnega učenja in tehnike NLP zaznavajo zlonamerna navodila v zunanji vsebini
   - Analiza v realnem času dokumentov, spletnih strani, e-pošte in podatkovnih virov za vgrajene grožnje
   - Kontekstualno razumevanje legitimnih proti zlonamernim vzorcem pozivov

2. **Tehnike osvetlitve**  
   - Ločuje zaupanja vredna sistemska navodila od potencialno kompromitiranih zunanjih vhodov
   - Metode transformacije besedila, ki izboljšajo relevantnost modela in izolirajo zlonamerno vsebino
   - Pomaga AI sistemom ohranjati pravilno hierarhijo navodil in ignorirati vbrizgane ukaze

3. **Sistemi ločil in označevanja podatkov**
   - Izrecna opredelitev meja med zaupanja vrednimi sistemskimi sporočili in zunanjim vhodnim besedilom
   - Posebni markerji poudarjajo meje med zaupanja vrednimi in nezaupanja vrednimi viri podatkov
   - Jasna ločitev preprečuje zmedo navodil in nepooblaščeno izvajanje ukazov

4. **Neprestano obveščanje o grožnjah**
   - Microsoft stalno spremlja nove vzorce napadov in posodablja obrambe
   - Proaktivno iskanje groženj za nove tehnike injiciranja in vektorje napadov
   - Redne posodobitve varnostnih modelov za ohranjanje učinkovitosti proti razvijajočim se grožnjam

5. **Integracija Azure Content Safety**
   - Del celovitega paketa Azure AI Content Safety
   - Dodatno zaznavanje poskusov jailbreaka, škodljive vsebine in kršitev varnostnih politik
   - Enotne varnostne kontrole čez komponente AI aplikacij

**Viri za implementacijo**: [Microsoft Prompt Shields Dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/sl/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Napredne grožnje MCP varnosti

### Ranljivosti prevzema sej

**Prevzem sej** predstavlja kritični vektor napada v stanjevnih implementacijah MCP, kjer nepooblaščene osebe pridobijo in zlorabijo legitimne identifikatorje sej za predstavljanja odjemalcev in izvajanje nepooblaščenih dejanj.

#### **Scenariji napadov in tveganja**

- **Injiciranje pozivov z zlorabo seje**: Napadalci z ukradenimi ID-ji sej vnašajo zlonamerne dogodke v strežnike, ki delijo stanje sej, kar lahko sproži škodljiva dejanja ali dostop do občutljivih podatkov
- **Neposredna ponarejanja**: Ukradeni ID-ji sej omogočajo neposredne klice MCP strežnikov, ki obidejo preverjanje pristnosti in obravnavajo napadalce kot legitimne uporabnike
- **Kompromitirani obnovljivi tokovi**: Napadalci lahko predčasno prekinejo zahteve, kar povzroči, da legitimni odjemalci nadaljujejo z morebitno zlonamerno vsebino

#### **Varnostne kontrole za upravljanje sej**

**Ključne zahteve:**
- **Preverjanje avtorizacije**: MCP strežniki, ki izvajajo avtorizacijo, **MORAJO** preveriti VSE dohodne zahteve in **NE SMEJO** uporabljati sej za preverjanje pristnosti
- **Varnostna generacija sej**: Uporabite kriptografsko varne, nedeterministične ID-je sej, ustvarjene z varnimi generatorji naključnih števil
- **Povezava z uporabnikom**: Povežite ID-je sej z informacijami, specifičnimi za uporabnika, z uporabo formatov, kot je `<user_id>:<session_id>`, da preprečite zlorabo sej med uporabniki
- **Upravljanje življenjskega cikla seje**: Uvedite pravilno potekanje, rotacijo in razveljavitev za omejitev ranljivosti
- **Varnost prenosa**: Obvezna uporaba HTTPS za vso komunikacijo, da preprečite prestrezanje ID-jev sej

### Problem zmedene pooblaščenke

**Problem zmedene pooblaščenke** nastane, ko MCP strežniki delujejo kot preverjevalci pristnosti med odjemalci in storitvami tretjih oseb, kar ustvarja priložnosti za obhod avtorizacije z izkoriščanjem statičnih ID-jev odjemalcev.

#### **Mehanika napada in tveganja**

- **Obhod soglasja na podlagi piškotkov**: Prejšnja uporabniška avtentikacija ustvari piškotke soglasja, ki jih napadalci izkoriščajo z zlonamernimi zahtevki za avtorizacijo z izdelanimi URI-ji za preusmeritev
- **Kraja avtorizacijskih kod**: Obstoječi piškotki soglasja lahko povzročijo, da avtorizacijski strežniki preskočijo zaslone za soglasje in kode preusmerijo na napadalcem nadzorovane končne točke  
- **Neavtoriziran dostop do API-jev**: Ukradene avtorizacijske kode omogočajo izmenjavo žetonov in ponarejanje uporabnikov brez izrecnega dovoljenja

#### **Strategije ublažitve**

**Obvezni ukrepi:**
- **Izrecna zahteva po soglasju**: MCP proxy strežniki, ki uporabljajo statične ID-je odjemalcev, **MORAJO** pridobiti uporabnikovo soglasje za vsakega dinamično registriranega odjemalca
- **Varnostna implementacija OAuth 2.1**: Upoštevajte trenutne varnostne prakse OAuth, vključno s PKCE (Proof Key for Code Exchange) za vse zahteve za avtorizacijo
- **Stroga validacija odjemalcev**: Uvedite strogo preverjanje URI-jev za preusmeritev in identifikatorjev odjemalcev, da preprečite zlorabe

### Ranljivosti pri posredovanju žetonov  

**Posredovanje žetonov** predstavlja eksplicitno anti-vzorec, kjer MCP strežniki sprejemajo žetone odjemalcev brez ustrezne validacije in jih posredujejo navzdol do API-jev, kar krši specifikacije avtorizacije MCP.

#### **Varnostne posledice**

- **Obhod nadzora**: Neposredna uporaba žetonov odjemalcev do API-jev obide ključne omejitve hitrosti, validacijo in nadzorne ukrepe
- **Poškodba revizijske sledi**: Žetoni, izdani zgoraj, onemogočajo identifikacijo odjemalca, kar ovira preiskave incidentov
- **Izsiljevanje podatkov prek proxyja**: Nevalidirani žetoni omogočajo zlonamernim akterjem uporabo strežnikov kot proxyjev za nepooblaščen dostop do podatkov
- **Kršenje meja zaupanja**: Predpostavke zaupanja storitev navzdol lahko kršijo, če izvora žetonov ni mogoče preveriti
- **Širjenje napadov na več storitev**: Sprejeti kompromitirani žetoni na več storitvah omogočajo lateralno gibanje

#### **Zahtevani varnostni ukrepi**

**Neprenosljive zahteve:**
- **Validacija žetonov**: MCP strežniki **NE SMEJO** sprejemati žetonov, ki niso izrecno izdani za MCP strežnik
- **Preverjanje občinstva**: Vedno preverite, da trditve o občinstvu žetona ustrezajo identiteti MCP strežnika
- **Pravilno upravljanje življenjskega cikla žetona**: Uvedite kratkotrajne dostopne žetone z varnimi praksami rotacije


## Varnost dobavne verige za AI sisteme

Varnost dobavne verige se je razvila onkraj tradicionalnih odvisnosti programske opreme in zajema celoten AI ekosistem. Sodobne implementacije MCP morajo strogo preverjati in nadzorovati vse komponente, povezane z AI, saj vsaka prinaša potencialne ranljivosti, ki lahko ogrozijo integriteto sistema.

### Razširjene komponente dobavne verige AI

**Tradicionalne programske odvisnosti:**
- Knjižnice in ogrodja odprte kode
- Slike kontejnerjev in osnovni sistemi  
- Orodja za razvoj in gradnjo
- Infrastrukturne komponente in storitve

**Elementi dobavne verige specifični za AI:**
- **Temeljni modeli**: Vnaprej usposobljeni modeli različnih ponudnikov, ki zahtevajo preverjanje izvora
- **Storitve vdelave**: Zunanje storitve za vektorizacijo in semantično iskanje
- **Ponudniki konteksta**: Viri podatkov, baze znanja in repozitoriji dokumentov  
- **API-ji tretjih oseb**: Zunanje AI storitve, ML cevovodi in končne točke za obdelavo podatkov
- **Artefakti modelov**: Teže, konfiguracije in fino nastavljene različice modelov
- **Viri podatkov za usposabljanje**: Nabori podatkov, uporabljeni za usposabljanje in fino nastavitev modelov

### Celovita strategija varnosti dobavne verige

#### **Preverjanje komponent in zaupanje**
- **Preverjanje izvora**: Preverite izvor, licenciranje in integriteto vseh AI komponent pred integracijo
- **Varnostna ocena**: Izvedite preglede ranljivosti in varnostne preglede modelov, virov podatkov in AI storitev
- **Analiza ugleda**: Ocenite varnostno zgodovino in prakse ponudnikov AI storitev
- **Preverjanje skladnosti**: Zagotovite, da vse komponente izpolnjujejo varnostne in regulativne zahteve organizacije

#### **Varnostni cevovodi za uvajanje**  
- **Avtomatizirano varnostno skeniranje CI/CD**: Vključite varnostno skeniranje v celoten avtomatiziran cevovod uvajanja
- **Integriteta artefaktov**: Uvedite kriptografsko preverjanje vseh uvajanih artefaktov (koda, modeli, konfiguracije)
- **Postopno uvajanje**: Uporabljajte progresivne strategije uvajanja z varnostno validacijo na vsaki stopnji
- **Zanesljivi repozitoriji artefaktov**: Uvajajte samo iz preverjenih, varnih registrijev in repozitorijev artefaktov

#### **Neprestano spremljanje in odziv**
- **Skeniranje odvisnosti**: Neprestano spremljanje ranljivosti vseh programsko in AI komponent
- **Spremljanje modelov**: Neprestana ocena vedenja modelov, odstopanja zmogljivosti in varnostnih anomalij
- **Spremljanje zdravja storitev**: Nadzor zunanjih AI storitev glede razpoložljivosti, varnostnih incidentov in sprememb politik
- **Integracija obveščanja o grožnjah**: Vključevanje virov groženj, specifičnih za varnost AI in ML

#### **Nadzor dostopa in najmanjše privilegije**
- **Dovoljenja na ravni komponent**: Omejite dostop do modelov, podatkov in storitev glede na poslovno potrebo
- **Upravljanje servisnih računov**: Uvedite namenski servisni računi z minimalnimi potrebnimi dovoljenji
- **Segmentacija omrežja**: Izolirajte AI komponente in omejite omrežni dostop med storitvami
- **Nadzor API prehodov**: Uporabljajte centralizirane API prehode za nadzor in spremljanje dostopa do zunanjih AI storitev

#### **Odziv na incidente in okrevanje**
- **Postopki hitrega odziva**: Vzpostavljeni postopki za popravke ali zamenjavo kompromitiranih AI komponent
- **Rotacija poverilnic**: Avtomatizirani sistemi za rotacijo skrivnosti, API ključev in servisnih poverilnic
- **Možnosti povrnitve**: Zmožnost hitrega vračanja na prejšnje znane dobre različice AI komponent
- **Okrevanje po kršitvah dobavne verige**: Posebni postopki za odziv na kompromitacije zgornjih AI storitev

### Microsoftova varnostna orodja in integracija

**GitHub Advanced Security** nudi celovito zaščito dobavne verige, vključno z:
- **Skeniranjem skrivnosti**: Avtomatizirano odkrivanje poverilnic, API ključev in žetonov v repozitorijih
- **Skeniranjem odvisnosti**: Ocena ranljivosti odprtokodnih odvisnosti in knjižnic
- **Analizo CodeQL**: Statična analiza kode za varnostne ranljivosti in težave pri kodiranju
- **Vpogled v dobavno verigo**: Pregled stanja odvisnosti in varnostnega statusa

**Integracija Azure DevOps & Azure Repos:**
- Brezhibna integracija varnostnega skeniranja na Microsoftovih razvojnih platformah
- Avtomatizirani varnostni pregledi v Azure Pipelines za AI delovne obremenitve
- Uveljavljanje politik za varno uvajanje AI komponent

**Microsoftove notranje prakse:**
Microsoft izvaja obsežne prakse varnosti dobavne verige v vseh svojih izdelkih. Več o preverjenih pristopih si preberite v [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Najboljše prakse temeljne varnosti

Implementacije MCP dedujejo in gradijo na obstoječem varnostnem položaju vaše organizacije. Krepitev temeljnih varnostnih praks znatno izboljša celotno varnost AI sistemov in uvajanja MCP.

### Osnove varnosti

#### **Varnostne prakse razvoja**
- **Skladnost z OWASP**: Zaščita pred [OWASP Top 10](https://owasp.org/www-project-top-ten/) ranljivostmi spletnih aplikacij
- **Zaščite specifične za AI**: Uvedba kontrol za [OWASP Top 10 za LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Varnostno upravljanje skrivnosti**: Uporaba namenskih trezorjev za žetone, API ključe in občutljive konfiguracijske podatke
- **End-to-end šifriranje**: Uvedba varne komunikacije v vseh komponentah aplikacije in podatkovnih tokovih
- **Validacija vhodov**: Stroga validacija vseh uporabniških vhodov, API parametrov in virov podatkov

#### **Ojačitev infrastrukture**
- **Večfaktorska avtentikacija**: Obvezna MFA za vse administrativne in servisne račune
- **Upravljanje popravkov**: Avtomatizirano, pravočasno nameščanje popravkov za operacijske sisteme, ogrodja in odvisnosti  
- **Integracija ponudnikov identitete**: Centralizirano upravljanje identitet preko podjetniških ponudnikov identitete (Microsoft Entra ID, Active Directory)
- **Segmentacija omrežja**: Logična izolacija MCP komponent za omejitev lateralnega gibanja
- **Načelo najmanjših privilegijev**: Minimalna potrebna dovoljenja za vse sistemske komponente in račune

#### **Spremljanje in zaznavanje varnosti**
- **Celovito beleženje**: Podrobno beleženje aktivnosti AI aplikacij, vključno z interakcijami MCP odjemalcev in strežnikov
- **Integracija SIEM**: Centralizirano upravljanje varnostnih informacij in dogodkov za zaznavanje anomalij
- **Analitika vedenja**: AI-podprto spremljanje za odkrivanje nenavadnih vzorcev v sistemskem in uporabniškem vedenju
- **Obveščanje o grožnjah**: Vključevanje zunanjih virov groženj in indikatorjev kompromisa (IOC)
- **Odziv na incidente**: Dobro definirani postopki za zaznavanje, odziv in okrevanje po varnostnih incidentih

#### **Arhitektura ničelnega zaupanja**
- **Nikoli ne zaupaj, vedno preverjaj**: Neprestano preverjanje uporabnikov, naprav in omrežnih povezav
- **Mikrosegmentacija**: Granularni omrežni nadzor, ki izolira posamezne delovne obremenitve in storitve
- **Varnost, osredotočena na identiteto**: Varnostne politike, ki temeljijo na preverjenih identitetah namesto na lokaciji omrežja
- **Neprestana ocena tveganja**: Dinamična ocena varnostnega položaja glede na trenutni kontekst in vedenje
- **Pogojni dostop**: Nadzor dostopa, ki se prilagaja glede na dejavnike tveganja, lokacijo in zaupanje naprave

### Vzorce integracije v podjetju

#### **Integracija Microsoftovega varnostnega ekosistema**
- **Microsoft Defender for Cloud**: Celovito upravljanje varnostnega položaja v oblaku
- **Azure Sentinel**: Nativni SIEM in SOAR zmogljivosti za zaščito AI delovnih obremenitev
- **Microsoft Entra ID**: Upravljanje identitet in dostopa v podjetju s politikami pogojnega dostopa
- **Azure Key Vault**: Centralizirano upravljanje skrivnosti z podporo strojne varnostne enote (HSM)
- **Microsoft Purview**: Upravljanje podatkov in skladnosti za vire podatkov in delovne tokove AI

#### **Skladnost in upravljanje**
- **Usklajenost z regulativami**: Zagotovite, da implementacije MCP izpolnjujejo industrijske zahteve skladnosti (GDPR, HIPAA, SOC 2)
- **Klasifikacija podatkov**: Pravilna kategorizacija in ravnanje z občutljivimi podatki, ki jih obdelujejo AI sistemi
- **Revizijske sledi**: Celovito beleženje za skladnost z regulativami in forenzične preiskave
- **Kontrole zasebnosti**: Uvedba načel zasebnosti po zasnovi v arhitekturi AI sistemov
- **Upravljanje sprememb**: Formalni postopki za varnostne preglede sprememb AI sistemov

Te temeljne prakse ustvarjajo robustno varnostno osnovo, ki izboljša učinkovitost varnostnih kontrol, specifičnih za MCP, in zagotavlja celovito zaščito AI aplikacij.

## Ključne varnostne ugotovitve

- **Večplastni varnostni pristop**: Združite temeljne varnostne prakse (varno kodiranje, najmanjše privilegije, preverjanje dobavne verige, neprekinjeno spremljanje) z AI-specifičnimi kontrolami za celovito zaščito

- **Specifičen varnostni prostor AI**: MCP sistemi se soočajo z edinstvenimi tveganji, vključno z injiciranjem pozivov, zastrupljanjem orodij, prevzemom sej, problemom zmedene pooblaščenke, ranljivostmi pri posredovanju žetonov in prekomernimi dovoljenji, ki zahtevajo specializirane ukrepe

- **Odličnost pri avtentikaciji in avtorizaciji**: Uvedite robustno avtentikacijo z zunanjimi ponudniki identitete (Microsoft Entra ID), uveljavljajte pravilno validacijo žetonov in nikoli ne sprejemajte žetonov, ki niso izrecno izdani za vaš MCP strežnik

- **Preprečevanje AI napadov**: Uporabite Microsoft Prompt Shields in Azure Content Safety za obrambo pred posrednim injiciranjem pozivov in zastrupljanjem orodij, hkrati pa validirajte metapodatke orodij in spremljajte dinamične spremembe

- **Varnost sej in prenosa**: Uporabljajte kriptografsko varne, nedeterministične ID-je sej, povezane z identitetami uporabnikov, uvedite pravilno upravljanje življenjskega cikla sej in nikoli ne uporabljajte sej za avtentikacijo

- **Najboljše prakse OAuth**: Preprečite napade zmedene pooblaščenke z izrecnim soglasjem uporabnika za dinamično registrirane odjemalce, pravilno implementacijo OAuth 2.1 s PKCE in strogo validacijo URI-jev za preusmeritev  

- **Načela varnosti žetonov**: Izogibajte se anti-vzorcem posredovanja žetonov, validirajte trditve o občinstvu žetonov, uvedite kratkotrajne žetone z varno rotacijo in ohranjajte jasne meje zaupanja

- **Celovita varnost dobavne verige**: Vse komponente AI ekosistema (modeli, vdelave, ponudniki konteksta, zunanji API-ji) obravnavajte z enako varnostno rigoroznostjo kot tradicionalne programske odvisnosti

- **Neprestan razvoj**: Bodite na tekočem z hitro razvijajočimi se specifikacijami MCP, prispevajte k varnostnim standardom skupnosti in vzdržujte prilagodljive varnostne položaje, ko protokol dozoreva

- **Integracija Microsoftove varnosti**: Izkoristite Microsoftov celovit varnostni ekosistem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) za izboljšano zaščito uvajanja MCP

## Celoviti viri

### **Uradna MCP varnostna dokumentacija**
- [MCP specifikacija (trenutno: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Najboljše varnostne prakse MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP specifikacija avtorizacije](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub repozitorij](https://github.com/modelcontextprotocol)

### **Varnostni standardi in najboljše prakse**
- [OAuth 2.0 najboljše varnostne prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 varnost spletnih aplikacij](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 za velike jezikovne modele](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Raziskave in analize varnosti AI**
- [Injiciranje pozivov v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Napadi z zastrupljanjem orodij (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Poročilo o varnostnih raziskavah MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoftove varnostne rešitve**
- [Dokumentacija Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Storitev Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Varnost Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Najboljše prakse upravljanja žetonov Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Napredna varnost GitHub](https://github.com/security/advanced-security)

### **Vodniki za implementacijo in vadnice**
- [Upravljanje API Azure kot MCP avtentikacijska prehodna točka](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Avtentikacija Microsoft Entra ID z MCP strežniki](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Varnostno shranjevanje in šifriranje žetonov (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Varnost DevOps in dobavne verige**
- [Varnost Azure DevOps](https://azure.microsoft.com/products/devops)
- [Varnost Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Pot Microsofta do varnosti dobavne verige](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dodatna varnostna dokumentacija**

Za celovita varnostna navodila si oglejte te specializirane dokumente v tem razdelku:

- **[Najboljše varnostne prakse MCP 2025](./mcp-security-best-practices-2025.md)** - Celovite najboljše varnostne prakse za implementacije MCP
- **[Implementacija Azure Content Safety](./azure-content-safety-implementation.md)** - Praktični primeri implementacije za integracijo Azure Content Safety  
- **[Varnostni nadzor MCP 2025](./mcp-security-controls-2025.md)** - Najnovejši varnostni nadzori in tehnike za nameščanje MCP
- **[Hiter pregled najboljših praks MCP](./mcp-best-practices.md)** - Hiter referenčni vodič za ključne varnostne prakse MCP

---

## Kaj sledi

Naslednje: [Poglavje 3: Začetek](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->