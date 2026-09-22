# MCP Varnost: Celovita zaščita za AI sisteme

[![MCP Varnost najboljše prakse](../../../translated_images/sl/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Kliknite na zgornjo sliko za ogled videa te lekcije)_

Varnost je temelj oblikovanja AI sistemov, zato ji namenjamo prednost kot drugemu poglavju. To se ujema z Microsoftovim načelom **Secure by Design** iz [Iniciative za varno prihodnost](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Protokol konteksta modela (MCP) prinaša zmogljive nove funkcije za aplikacije, ki temeljijo na AI, hkrati pa uvaja edinstvene varnostne izzive, ki presegajo tradicionalna tveganja programske opreme. Sistemi MCP se soočajo tako z uveljavljenimi varnostnimi vprašanji (varno kodiranje, najmanjša privilegija, varnost dobavne verige) kot z novimi grožnjami, specifičnimi za AI, vključno z vbrizgavanjem usmeritev, zastrupitvijo orodij, prevzemom sej, napadi "zmedeni namestnik", ranljivostmi pri posredovanju žetonov in dinamičnimi spremembami zmogljivosti.

V tej lekciji raziskujemo najpomembnejša varnostna tveganja v implementacijah MCP — pokrivamo preverjanje pristnosti, pooblastila, prekomerne pravice, posredno vbrizgavanje usmeritev, varnost sej, težave z "zmedenim namestnikom", upravljanje žetonov in ranljivosti dobavne verige. Naučili se boste učinkovitih ukrepov in najboljših praks za zmanjšanje teh tveganj, hkrati pa boste izkoristili Microsoftove rešitve, kot so Prompt Shields, Azure Content Safety in GitHub Advanced Security, za krepitev vaše uspstave MCP.

## Cilji učenja

Do konca te lekcije boste lahko:

- **Prepoznati grožnje, specifične za MCP**: Prepoznati edinstvena varnostna tveganja v sistemih MCP, vključno z vbrizgavanjem usmeritev, zastrupitvijo orodij, prekomernimi dovoljenji, prevzemom sej, težavami z "zmedenim namestnikom", ranljivostmi pri posredovanju žetonov in tveganji dobavne verige
- **Uvesti varnostne ukrepe**: Izvesti učinkovite ukrepe, vključno z robustnim preverjanjem pristnosti, dostopom po načelu najmanjših privilegijev, varnim upravljanjem žetonov, varnostnimi kontrolami sej in preverjanjem dobavne verige
- **Izkoristiti Microsoftove varnostne rešitve**: Razumeti in uporabiti Microsoft Prompt Shields, Azure Content Safety in GitHub Advanced Security za zaščito delovnih obremenitev MCP
- **Preveriti varnost orodij**: Prepoznati pomembnost preverjanja metapodatkov orodij, spremljati dinamične spremembe in se braniti pred posrednimi napadi vbrizgavanja usmeritev
- **Integrirati najboljše prakse**: Združiti uveljavljene varnostne temelje (varno kodiranje, utrjevanje strežnika, zero trust) z MCP-specifičnimi ukrepi za celovito zaščito

# MCP Varnostna arhitektura in kontrole

Sodobne implementacije MCP zahtevajo večplastne varnostne pristope, ki naslovijo tradicionalno varnost programske opreme in specifične grožnje AI. Hitro razvijajoča se specifikacija MCP nadalje izboljšuje varnostne kontrole, omogoča boljšo integracijo z arhitekturami podjetij in uveljavljenimi najboljšimi praksami.

Raziskave iz [Microsoft Digital Defense Report](https://aka.ms/mddr) prikazujejo, da **bi bilo 98 % prijavljenih kršitev preprečenih z robustno varnostno higieno**. Najbolj učinkovita zaščitna strategija združuje temeljne varnostne prakse z MCP-specifičnimi kontrolami — preverjene varnostne osnove ostajajo najbolj pomembne za zmanjšanje skupnega varnostnega tveganja.

## Trenutno varnostno stanje

> **Opomba:** To poglavje združuje uveljavljene varnostne kontrole MCP s
> trenutno **MCP specifikacijo 2026-07-28** za pooblastila. Vedno se
> sklicujte na trenutno [MCP Specifikacijo](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub repozitorij](https://github.com/modelcontextprotocol) in
> [dokumentacijo najboljših varnostnih praks](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> pri implementaciji varnostno občutljive kode.

> **Posodobitev pooblastil:** MCP `2026-07-28` zahteva od odjemalcev, da preverijo
> parameter `iss` v odgovorih na pooblastila (RFC 9207) in povežejo registrirane
> poverilnice z izdajo strežnika pooblastil. Dinamična registracija odjemalcev
> je neveljavna; nove implementacije naj uporabljajo metapodatke o odjemalcu.
> Oglejte si [Kaj se je spremenilo v MCP: specifikacija 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> za celoten seznam sprememb pooblastil.

## 🏔️ MCP Varnostni vrh delavnica (Sherpa)

Za **praktično varnostno usposabljanje** močno priporočamo **MCP Varnostni vrh delavnico** (Sherpa) - celovito vodeno odpravo za zaščito MCP strežnikov v Microsoft Azure.

### Pregled delavnice

[MCP Varnostni vrh delavnica](https://azure-samples.github.io/sherpa/) ponuja praktično, uporabno varnostno usposabljanje preko preverjene metodologije "ranljivost → izkoriščenje → popravilo → preverjanje". Naučili se boste:

- **Učenje z razbijanjem stvari**: Izkušnje z ranljivostmi z izkoriščanjem namensko negotovih strežnikov
- **Uporaba Azure-nativne varnosti**: Uporaba Azure Entra ID, Key Vault, API Management in AI Content Safety
- **Sledenje obrambi v globino**: Napredovanje skozi tabore z gradnjo celovitih plasti varnosti
- **Uporaba OWASP standardov**: Vsaka tehnika je povezana z [OWASP MCP Azure Varnostnim vodnikom](https://microsoft.github.io/mcp-azure-security-guide/)
- **Pridobitev proizvodne kode**: Odhod z delujočimi, preizkušenimi implementacijami

### Pot odprave

| Tabor | Osredotočenost | Pokrita OWASP tveganja |
|------|-------------|---------------------|
| **Osnovni tabor** | Osnove MCP in ranljivosti preverjanja pristnosti | MCP01, MCP07 |
| **Tabor 1: Identiteta** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Tabor 2: Vhodna točka** | API Management, zasebni konektorji, upravljanje | MCP02, MCP06, MCP07, MCP09 |
| **Tabor 3: I/O varnost** | Vbrizgavanje usmeritev, zaščita PII, varnost vsebine | MCP03, MCP05, MCP06, MCP10 |
| **Tabor 4: Spremljanje** | Log Analytics, nadzorne plošče, zaznavanje groženj | MCP04, MCP08 |
| **Vrh** | Test integracije rdeče in modre ekipe | Vsa |

**Začni tukaj**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 varnostnih tveganj

[OWASP MCP Azure Varnostni vodnik](https://microsoft.github.io/mcp-azure-security-guide/) podrobno opisuje deset najpomembnejših varnostnih tveganj za implementacije MCP:

| Tveganje | Opis | Azure zaščita |
|---------|-------|---------------|
| **MCP01** | Nepravilno upravljanje žetonov in razkritje skrivnosti | Azure Key Vault, Managed Identity |
| **MCP02** | Eskalacija privilegijev preko naraščanja obsega | RBAC, pogojni dostop |
| **MCP03** | Zastrupitev orodij | Preverjanje orodij, potrjevanje integritete |
| **MCP04** | Napadi na dobavno verigo programske opreme & manipulacije odvisnosti | GitHub Advanced Security, skeniranje odvisnosti |
| **MCP05** | Vbrizgavanje in izvedba ukazov | Preverjanje vhodnih podatkov, peskovnik |
| **MCP06** | Podvajanje namena | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Nezadostno preverjanje pristnosti in pooblastil | Azure Entra ID, OAuth 2.1 z PKCE |
| **MCP08** | Pomanjkanje revizije in telemetrije | Azure Monitor, Application Insights |
| **MCP09** | Senci strežniki MCP | Urejanje API centra, mrežna izolacija |
| **MCP10** | Vbrizgavanje konteksta & prekomerna delitev | Klasifikacija podatkov, minimalna izpostavljenost |

### Razvoj preverjanja pristnosti MCP

Specifikacija MCP se je bistveno razvila v pristopu k preverjanju pristnosti in pooblastil:

- **Izvirni pristop**: Zgodnje specifikacije so zahtevale od razvijalcev implementacijo lastnih strežnikov za preverjanje pristnosti, pri čemer so MCP strežniki delovali kot strežniki za pooblastila OAuth 2.0 in upravljali preverjanje pristnosti uporabnikov neposredno
- **Trenutni standard (`2026-07-28`)**: MCP strežniki lahko delegirajo preverjanje pristnosti
  zunanjim ponudnikom identitete, kot je Microsoft Entra ID. Odjemalci morajo
  prav tako upoštevati trenutne zahteve za preverjanje izdajatelja in vezavo poverilnic.
- **Varnost sloja prenosa**: Izboljšana podpora za varne mehanizme prenosa s pravilnimi vzorci preverjanja pristnosti tako za lokalne (STDIO) kot oddaljene (Streamable HTTP) povezave

## Varnost preverjanja pristnosti in pooblastil

### Trenutni varnostni izzivi

Sodobne implementacije MCP se soočajo z več izzivi pri preverjanju pristnosti in pooblastilih:

### Tveganja in grožnje

- **Nepravilno konfigurirana logika pooblastil**: Napake v implementaciji pooblastil v MCP strežnikih lahko razkrijejo občutljive podatke in nepravilno uveljavljajo kontrole dostopa
- **Ogroženi OAuth žetoni**: Kraja žetonov lokalnega MCP strežnika omogoča napadalcem, da se predstavljajo kot strežniki in dostopajo do storitev
- **Ranljivosti pri posredovanju žetonov**: Nepravilno upravljanje žetonov omogoča obhod varnostnih kontrol in vrzeli v odgovornosti
- **Prekomerna dovoljenja**: MCP strežniki z več privilegiji kršijo načelo najmanjših privilegijev in povečujejo površino napada

#### Posredovanje žetonov: Kritičen anti-vzorac

**Posredovanje žetonov je izrecno prepovedano** v trenutni MCP specifikaciji pooblastil zaradi resnih varnostnih posledic:

##### Obhod varnostnih kontrol
- MCP strežniki in spodnje API-ji uporabljajo kritične varnostne kontrole (omejevanje hitrosti, preverjanje zahtev, spremljanje prometa), ki so odvisne od pravilne validacije žetonov
- Neposredna uporaba žetonov od stranke do API-ja obide te zaščite in podre varnostno arhitekturo

##### Izzivi odgovornosti in revizije  
- MCP strežniki ne morejo razlikovati strank, ki uporabljajo žetone, izdane zgoraj, kar ruši sledljivost
- Dnevniki strežnikov virov kažejo zavajajoče izvore zahtev namesto dejanske vloge MCP strežnikov
- Preiskave incidentov in skladnostne revizije postanejo bistveno težje

##### Tveganja odtujitve podatkov
- Nevalidirani trditve v žetonih omogočajo zlobnim akterjem z ukradenimi žetoni, da uporabljajo MCP strežnike kot posrednike za odtujitev podatkov
- Kršitve mej zaupanja omogočajo nepooblaščen dostop, ki obide namenjene varnostne kontrole

##### Večstoritevni vektorji napadov
- Izrabljeni žetoni, ki jih sprejema več storitev, omogočajo lateralno gibanje po povezanih sistemih
- Predpostavke zaupanja med storitvami so lahko kršene, če izvori žetonov niso preverljivi

### Varnostne kontrole in ublažitve

**Ključne varnostne zahteve:**

> **OBVEZNO**: MCP strežniki **NE SMEJO** sprejemati nobenih žetonov, ki niso izrecno izdani za MCP strežnik

#### Kontrole preverjanja pristnosti in pooblastil

- **Strog pregled pooblastil**: Izvedite celovite revizije pooblastil MCP strežnikov, da zagotovite, da lahko dostopajo samo predvideni uporabniki in odjemalci do občutljivih virov
  - **Vodnik za implementacijo**: [Azure API Management kot vhod za preverjanje pristnosti MCP strežnikov](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integracija identitete**: [Uporaba Microsoft Entra ID za preverjanje pristnosti MCP strežnikov](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Varno upravljanje žetonov**: Uporabite [Microsoftove najboljše prakse za validacijo žetonov in življenjski cikel](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Preverite, da trditve občinstva žetona ustrezajo identiteti MCP strežnika
  - Uvedite pravilno rotacijo in potek veljavnosti žetonov
  - Preprečite ponovne zlorabe in nepooblaščeno uporabo žetonov

- **Zaščiteno shranjevanje žetonov**: Varnostno shranjujte žetone z uporabo šifriranja tako v mirovanju kot med prenosom
  - **Najboljše prakse**: [Vodič za varno shranjevanje žetonov in šifriranje](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementacija kontrole dostopa

- **Načelo najmanjših privilegijev**: Dodelite MCP strežnikom samo minimalna dovoljenja, potrebna za predvidene funkcionalnosti
  - Redno pregledujte in posodabljajte dovoljenja za preprečitev naraščanja privilegijev
  - **Microsoftova dokumentacija**: [Varno najmanj privilegiran dostop](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Upravljanje dostopa na osnovi vlog (RBAC)**: Uvedite natančne dodelitve vlog
  - Natančno omejite vloge na specifične vire in dejanja
  - Izogibajte se širokim ali nepotrebnim dovoljenjem, ki povečujejo površino napada

- **Stalno spremljanje dovoljenj**: Vladajte stalno revizijo dostopa in spremljanje
  - Spremljate vzorce uporabe dovoljenj za odstopanja
  - Hitro odpravite prekomerna ali neuporabljena dovoljenja

## Grožnje, specifične za AI

### Napadi vbrizgavanja usmeritev in manipulacije orodij

Sodobne implementacije MCP se soočajo z izpopolnjenimi, specifičnimi AI vektorskimi napadi, ki jih tradicionalni varnostni ukrepi ne morejo popolnoma nasloviti:

#### **Posredno vbrizgavanje usmeritev (vbrizgavanje usmeritev med domenami)**

**Posredno vbrizgavanje usmeritev** predstavlja eno najpomembnejših ranljivosti v AI sistemih z omogočenim MCP. Napadalci vključujejo zlonamerna navodila znotraj zunanje vsebine — dokumentov, spletnih strani, e-pošte ali podatkovnih virov — ki jih AI sistemi nato obdelujejo kot legitimna navodila.

**Scenariji napada:**
- **Vbrizgavanje v dokumentih**: Zlonamerna navodila skrita v obdelanih dokumentih, ki sprožijo nezaželena AI dejanja
- **Izraba spletne vsebine**: Kompromitirane spletne strani z vgrajenimi usmeritvami, ki manipulirajo vedenje AI ob strganju
- **Napadi preko e-pošte**: Zlonamerna navodila v e-pošti, ki povzročijo, da AI asistenti razkrijejo informacije ali izvedejo nepooblaščena dejanja
- **Kontaminacija podatkovnih virov**: Kompromitirane baze podatkov ali API-ji, ki dobavljajo okuženo vsebino AI sistemom

**Vpliv v resničnem svetu**: Ti napadi lahko povzročijo odtujitev podatkov, kršitve zasebnosti, generiranje škodljive vsebine ter manipulacijo uporabniških interakcij. Za podrobno analizo glejte [Prompt Injection v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagram napada vbrizgavanja usmeritev](../../../translated_images/sl/prompt-injection.ed9fbfde297ca877.webp)

#### **Napadi zastrupitve orodij**

**Zastrupitev orodij** cilja na metapodatke, ki definirajo orodja MCP, izkorišča pa način, kako LLM-ji interpretirajo opise orodij in parametre za odločanje o izvedbi.

**Mehanizmi napada:**
- **Manipulacija metapodatkov**: Napadalci vbrizgajo zlonamerna navodila v opise orodij, definicije parametrov ali primere uporabe
- **Nevidna navodila**: Skrita usmeritev v metapodatkih orodij, ki jih AI modeli obdelujejo, vendar so nevidna človeškim uporabnikom
- **Dinamična sprememba orodij ("Rug Pulls")**: Orodja, odobrena s strani uporabnikov, so kasneje spremenjena za izvajanje zlonamernih dejanj brez vednosti uporabnika
- **Vbrizgavanje parametrov**: Zlonamerna vsebina v shemah parametrov orodij, ki vpliva na vedenje modela


**Tveganja gostovanih strežnikov**: Oddaljeni MCP strežniki predstavljajo povečana tveganja, saj je mogoče definicije orodij posodobiti po začetnem uporabniškem odobritvi, kar ustvarja scenarije, kjer prej varna orodja postanejo zlonamerna. Za celovito analizo glejte [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagram napada z injiciranjem orodja](../../../translated_images/sl/tool-injection.3b0b4a6b24de6bef.webp)

#### **Dodatni vektorji napadov AI**

- **Injiciranje pozivov med domenami (XPIA)**: Izpopolnjeni napadi, ki izkoriščajo vsebino iz več domen za obhod varnostnih kontrol
- **Dinamična sprememba zmogljivosti**: Spremembe zmogljivosti orodij v realnem času, ki uidejo začetnim varnostnim ocenam
- **Zastrupitev kontekstnega okna**: Napadi, ki manipulirajo z velikimi kontekstnimi okni za skrivanje zlonamernih navodil
- **Napadi zaradi zmede modela**: Izraba omejitev modela za ustvarjanje nepredvidljivih ali nevarnih vedenj


### Vpliv tveganj AI varnosti

**Visokovplivne posledice:**
- **Izpipanje podatkov**: Nepooblaščen dostop in kraja občutljivih podjetniških ali osebnih podatkov
- **Kršitve zasebnosti**: Razkritje osebnih podatkov (PII) in poslovnih skrivnosti  
- **Manipulacija sistemov**: Nenamerne spremembe kritičnih sistemov in delovnih tokov
- **Kraja poverilnic**: Kompromitacija avtorizacijskih žetonov in servisnih poverilnic
- **Stranski premik**: Uporaba kompromitiranih AI sistemov kot odskočnih desk za širše omrežne napade

### Microsoftove rešitve za varnost AI

#### **Ščiti pozivov AI: Napredna zaščita pred injiciranjem**

Microsoft **Ščiti pozivov AI** nudijo celovito obrambo pred neposrednimi in posrednimi napadi z injiciranjem pozivov preko več varnostnih plasti:

##### **Glavni mehanizmi zaščite:**

1. **Napredno zaznavanje in filtriranje**
   - Algoritmi strojnega učenja in NLP tehnike zaznavajo zlonamerna navodila v zunanji vsebini
   - Analiza dokumentov, spletnih strani, e-pošte in virov podatkov v realnem času za vgrajene grožnje
   - Kontekstualno razumevanje legitimnih proti zlonamernim vzorcem pozivov

2. **Tehnike poudarjanja**  
   - Razlikuje med zaupanja vrednimi sistemskimi navodili in potencianlo kompromitiranimi zunanjimi vhodi
   - Metode transformacije besedila, ki izboljšajo relevantnost modela in izolirajo zlonamerno vsebino
   - Pomaga AI sistemom ohraniti pravilno hierarhijo navodil in ignorirati injicirane ukaze

3. **Sistemi ločil in označevanja podatkov**
   - Izrecna definicija meja med zaupanja vredna sistemska sporočila in zunanji vhodni tekst
   - Posebni markerji poudarjajo meje med zaupanja vrednimi in nezaupnimi viri podatkov
   - Jasna ločitev preprečuje zmedo navodil in nepooblaščeno izvajanje ukazov

4. **Neprestano obveščanje o grožnjah**
   - Microsoft nenehno spremlja nastajajoče vzorce napadov in posodablja obrambe
   - Proaktivno iskanje groženj za nove tehnike injiciranja in vektorje napadov
   - Redne posodobitve varnostnih modelov za ohranjanje učinkovitosti proti razvijajočim se grožnjam

5. **Integracija Azure Content Safety**
   - Del celovitega paketa Azure AI Content Safety
   - Dodatna zaznava poskusov jailbreak, škodljive vsebine in kršitev varnostnih politik
   - Združene varnostne kontrole za vse komponente AI aplikacij

**Viri za implementacijo**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Zaščita Microsoft Prompt Shields](../../../translated_images/sl/prompt-shield.ff5b95be76e9c78c.webp)


## Napredne varnostne grožnje MCP

### Ranljivosti prevzema sej

**Prevzem sej** predstavlja kritični vektor napada v implementacijah stanja MCP, kjer nepooblaščene strani pridobijo in zlorabljajo legitimne identifikatorje sej za oponašanje strank in izvajanje nepooblaščenih dejanj.

#### **Scenariji napadov in tveganja**

- **Injiciranje poziva z ugrabitvijo seje**: Napadalci s ukradenimi ID sej vnašajo zlonamerne dogodke v strežnike, ki delijo stanje seje, kar lahko sproži škodljiva dejanja ali dostop do občutljivih podatkov
- **Neposredno oponašanje**: Ukradeni ID sej omogočajo neposredne klice MCP strežnika, ki obidejo avtorizacijo in obravnavajo napadalce kot legitimne uporabnike
- **Kompromitirani obnovljivi tokovi**: Napadalci lahko predčasno prekinejo zahteve, zaradi česar legitimne stranke nadaljujejo z morebitno zlonamerno vsebino

#### **Varnostne kontrole za upravljanje sej**

**Kritične zahteve:**
- **Preverjanje avtorizacije**: MCP strežniki, ki izvajajo avtorizacijo, **MORALI BI** preveriti VSE dohodne zahteve in **NE SMEJO** zanašati na seje za overjanje
- **Varna generacija sej**: Uporaba kriptografsko varnih, nedeterminističnih ID sej, ustvarjenih z varnimi generatorji naključnih števil
- **Povezava s specifičnim uporabnikom**: Povezava ID sej z informacijami specifičnimi za uporabnika z formati, kot je `<user_id>:<session_id>`, za preprečitev zlorabe sej med uporabniki
- **Upravljanje življenjskega cikla seje**: Uvedba pravilnih potekov, rotacije in ničenja za omejitev okna ranljivosti
- **Varnost prenosa**: Obvezno HTTPS za vso komunikacijo za preprečitev prestrezanja ID sej

### Problem zmedenega namestnika

**Problem zmedenega namestnika** se pojavi, ko MCP strežniki delujejo kot proxyji za overjanje med strankami in storitvami tretjih oseb, kar odpira možnosti za obhod avtorizacije z izkoriščanjem statičnih ID-jev strank.

#### **Mehanika napada in tveganja**

- **Obhod soglasja na osnovi piškotkov**: Prejšnja avtorizacija uporabnika ustvari soglasne piškotke, ki jih napadalci izkoriščajo preko zlonamernih zahtev z odobritvijo in skrojenimi URI za preusmeritev
- **Kraja avtorizacijskih kod**: Obstoječi soglasni piškotki lahko povzročijo, da avtorizacijski strežniki preskočijo zaslone soglasja in preusmerjajo kode na kontrolo napadalca  
- **Neavtoriziran dostop do API-jev**: Ukradene avtorizacijske kode omogočajo izmenjavo žetonov in oponašanje uporabnikov brez izrecne odobritve

#### **Strategije ublažitve**

**Obvezne kontrole:**
- **Izrecne zahteve soglasja**: MCP proxy strežniki, ki uporabljajo statične ID-je strank, **MORALI BI** pridobiti uporabniško soglasje za vsako dinamično registrirano stranko
- **Varnost za OAuth 2.1**: Slediti trenutnim najboljšim praksam varnosti OAuth, vključno s PKCE (Proof Key for Code Exchange) za vse avtorizacijske zahteve
- **Stroga validacija strank**: Izvajati rigorozno preverjanje URI za preusmeritev in identifikatorjev strank za preprečitev izkoriščanja

### Ranljivosti v prehodu žetonov  

**Prehod žetonov** predstavlja eksplicitno slabo prakso, kjer MCP strežniki sprejemajo žetone strank brez ustrezne validacije ter jih posredujejo navzdol usmerjenim API-jem, s čimer kršijo specifikacije avtorizacije MCP.

#### **Varnostni vplivi**

- **Obhod kontrol**: Neposredno uporabljanje žetonov stranke do API-ja zaobide kritične omejitve hitrosti, validacijo in nadzorne kontrole
- **Poškodba revizijske sledi**: Žetoni, izdani navzgor, onemogočajo identifikacijo stranke in motijo preiskave incidentov
- **Izpipanje podatkov preko proxy-ja**: Nevalidirani žetoni omogočajo zlonamernim akterjem uporabo strežnikov kot proxy za nepooblaščen dostop do podatkov
- **Kršitev meja zaupanja**: Predpostavke zaupanja servisa navzdol so lahko kršene, ko izvora žetona ni mogoče preveriti
- **Širjenje napadov prek več storitev**: Kompromitirani žetoni, sprejeti preko več služb, omogočajo stransko premikanje

#### **Zahtevane varnostne kontrole**

**Nepogrešljive zahteve:**
- **Validacija žetonov**: MCP strežniki **NE SMEJO** sprejemati žetonov, ki niso izrecno izdani za MCP strežnik
- **Preverjanje občinstva**: Vedno validirajte, da se trditve o občinstvu žetona ujemajo z identiteto MCP strežnika
- **Ustrezno življenjsko dobo žetona**: Uporabite kratkotrajne dostopne žetone z varnimi praksami rotacije


## Varnost oskrbovalne verige za AI sisteme

Varnost oskrbovalne verige je presegla tradicionalne programske odvisnosti in zajema celoten AI ekosistem. Sodobne implementacije MCP morajo strogo preverjati in spremljati vse AI povezane komponente, saj vsak vnaša morebitne ranljivosti, ki lahko ogrozijo integriteto sistema.

### Razširjene komponente oskrbovalne verige AI

**Tradicionalne programske odvisnosti:**
- Knjižnice odprte kode in ogrodja
- Kontajnerske slike in osnovni sistemi  
- Orodja za razvoj in gradbene verige
- Infrastrukturne komponente in storitve

**Posebni elementi oskrbovalne verige AI:**
- **Osnovni modeli**: Vnaprej trenirani modeli različnih ponudnikov, ki zahtevajo preverjanje izvora
- **Storitve vdelave**: Zunanje storitve vektorizacije in semantičnega iskanja
- **Ponudniki konteksta**: Viri podatkov, baze znanja in skladišča dokumentov  
- **API-ji tretjih oseb**: Zunanje AI storitve, ML cevovodi in končne točke za obdelavo podatkov
- **Modelski artefakti**: Teže, konfiguracije in fino nastavljene različice modelov
- **Viri učnih podatkov**: Nabore podatkov, uporabljene za usposabljanje in fino nastavljanje modelov

### Celovita varnostna strategija oskrbovalne verige

#### **Preverjanje komponent in zaupanje**
- **Validacija izvora**: Preverite izvor, licenciranje in integriteto vseh AI komponent pred integracijo
- **Varnostna ocena**: Izvedite preglede ranljivosti in varnostne preglede za modele, vire podatkov in AI storitve
- **Analiza ugleda**: Ocenite varnostno zgodovino in prakse ponudnikov AI storitev
- **Preverjanje skladnosti**: Zagotovite, da vse komponente izpolnjujejo varnostne in regulatorne zahteve organizacije

#### **Varnostne cevi za uvajanje**  
- **Avtomatizirano varnostno preverjanje CI/CD**: Vključite varnostno skeniranje v celotne avtomatizirane pipelines za uvajanje
- **Integriteta artefaktov**: Uvedite kriptografsko preverjanje za vse nameščene artefakte (koda, modeli, konfiguracije)
- **Fazno uvajanje**: Uporabljajte progresivne strategije uvajanja z varnostno validacijo v vsakem koraku
- **Zaupanja vredni repozitoriji artefaktov**: Namestitev samo iz preverjenih in varnih registrij ter skladišč artefaktov

#### **Neprestano spremljanje in odziv**
- **Skeniranje odvisnosti**: Neprestano spremljanje ranljivosti za vse programske in AI komponentne odvisnosti
- **Nadzor modela**: Neprestana ocena vedenja modela, drsenja zmogljivosti in varnostnih anomalij
- **Spremljanje zdravja storitev**: Nadzor zunanjih AI storitev glede razpoložljivosti, varnostnih incidentov in sprememb politik
- **Integracija obveščevalnih podatkov o grožnjah**: Vključitev virih podatkov o grožnjah specifičnih za AI in ML varnostna tveganja

#### **Nadzor dostopa in načelo najmanjših privilegijev**
- **Dovoljenja na ravni komponent**: Omejite dostop do modelov, podatkov in storitev glede na poslovno nujnost
- **Upravljanje servisnih računov**: Uvedite namenski servisni računi z minimalnimi potrebnimi dovoljenji
- **Segmentacija omrežja**: Izolacija AI komponent in omejevanje omrežnega dostopa med storitvami
- **Kontrole API vstopnih točk**: Uporaba centraliziranih API gateway-jev za nadzor in spremljanje dostopa do zunanjih AI storitev

#### **Odziv na incidente in okrevanje**
- **Hitri postopki odziva**: Uveljavljeni postopki za popravke ali zamenjavo kompromitiranih AI komponent
- **Rotacija poverilnic**: Avtomatizirani sistemi za rotiranje skrivnosti, API ključev in servisnih poverilnic
- **Možnosti povrnitve**: Zmožnost hitrega vračanja na prej znane dobre različice AI komponent
- **Okrevanje po vdoru v oskrbovalno verigo**: Specifični postopki za odziv na kompromitacije zunanjih AI storitev

### Microsoftova varnostna orodja in integracija

**GitHub Advanced Security** nudi celovito zaščito oskrbovalne verige, vključno z:
- **Skeniranjem skrivnosti**: Avtomatizirano zaznavanje poverilnic, API ključev in žetonov v repozitorijih
- **Skeniranje odvisnosti**: Ocena ranljivosti odprtokodnih odvisnosti in knjižnic
- **Analizo CodeQL**: Statična analiza kode za varnostne ranljivosti in težave pri programiranju
- **Vpogledi v oskrbovalno verigo**: Pregled zdravja odvisnosti in varnostnega stanja

**Integracija Azure DevOps in Azure Repos:**
- Brezhibna integracija varnostnega skeniranja na Microsoftovih razvojnih platformah
- Avtomatizirano varnostno preverjanje v Azure Pipelines za AI naloge
- Uveljavljanje politik za varno uvajanje AI komponent

**Notranje prakse Microsofta:**
Microsoft izvaja obsežne prakse varnosti oskrbovalne verige za vse izdelke. Spoznajte preizkušene pristope v [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Najboljše prakse za temeljno varnost

Implementacije MCP dedujejo in gradijo na obstoječem varnostnem položaju vaše organizacije. Krepitev temeljnih varnostnih praks bistveno izboljša celotno varnost AI sistemov in uvajanja MCP.

### Osnovna varnostna izhodišča

#### **Prakse varnega razvoja**
- **Skladnost z OWASP**: Zaščita pred ranljivostmi spletnih aplikacij [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **AI-specifične zaščite**: Uvedba kontrol za [OWASP Top 10 za LLM-je](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Varno upravljanje skrivnosti**: Uporaba namenskih trezorjev za žetone, API ključe in občutljive konfiguracijske podatke
- **Šifriranje od konca do konca**: Izvedba varnih komunikacij preko vseh komponent aplikacije in podatkovnih tokov
- **Validacija vhodov**: Stroga validacija vseh uporabniških vhodov, parametrov API in virov podatkov

#### **Utrjevanje infrastrukture**
- **Večfaktorska avtentikacija**: Obvezna MFA za vse administrativne in servisne račune
- **Upravljanje popravkov**: Avtomatizirano in pravočasno nameščanje popravkov operacijskih sistemov, ogrodij in odvisnosti  
- **Integracija ponudnikov identitete**: Centralizirano upravljanje identitet preko podjetniških ponudnikov (Microsoft Entra ID, Active Directory)
- **Segmentacija omrežja**: Logična izolacija komponent MCP za omejitev potenciala stranskega premikanja
- **Načelo najmanjših privilegijev**: Minimalna potrebna dovoljenja za vse sistemske komponente in račune

#### **Nadzor in zaznavanje varnosti**
- **Celovito beleženje**: Podrobno beleženje dejavnosti AI aplikacij, vključno z interakcijami MCP klient-strežnik
- **Integracija SIEM**: Centralizirano upravljanje varnostnih informacij in dogodkov za zaznavanje anomalij
- **Analitika vedenja**: AI-podprt nadzor za zaznavanje nenavadnih vzorcev v sistemskem in uporabniškem vedenju
- **Obveščevalne informacije o grožnjah**: Integracija zunanjih virov podatkov o grožnjah in indikatorjev kompromisa (IOC)
- **Odziv na incidente**: Dobro opredeljeni postopki za zaznavanje, odziv in okrevanje po varnostnih incidentih

#### **Arhitektura Zero Trust**
- **Nikoli ne zaupaj, vedno preverjaj**: Neprestano preverjanje uporabnikov, naprav in omrežnih povezav
- **Mikrosegmentacija**: Granularni omrežni nadzor, ki izolira posamezne delovne obremenitve in storitve
- **Varnost usmerjena na identiteto**: Varovalne politike, osnovane na preverjenih identitetah, ne na lokaciji omrežja
- **Neprestana ocena tveganja**: Dinamična ocena varnostnega položaja na podlagi trenutnega konteksta in vedenja
- **Pogojni dostop**: Kontrole dostopa, ki se prilagajajo glede na dejavnike tveganja, lokacijo in zaupanje naprave

### Vzorec integracije v podjetju

#### **Integracija v Microsoftov varnostni ekosistem**
- **Microsoft Defender za oblak**: Celovito upravljanje varnostnega položaja oblaka
- **Azure Sentinel**: Nativni SIEM in SOAR zmožnosti v oblaku za zaščito AI obremenitev
- **Microsoft Entra ID**: Upravljanje podjetniške identitete in dostopa z uporabo politik pogojnega dostopa
- **Azure Key Vault**: Centralizirano upravljanje skrivnosti z uporabo kriptografskih modulov (HSM)
- **Microsoft Purview**: Upravljanje podatkov in skladnosti za vire podatkov in delovne tokove AI

#### **Skladnost in upravljanje**
- **Usklajenost z regulativami**: Zagotovite, da implementacije MCP izpolnjujejo industrijske zahteve skladnosti (GDPR, HIPAA, SOC 2)

- **Klasifikacija podatkov**: Pravilna kategorizacija in obravnava občutljivih podatkov, ki jih obdelujejo sistemi AI
- **Revizijske sledi**: Celovito beleženje za skladnost z zakonodajo in forenzične preiskave
- **Nadzor zasebnosti**: Izvajanje načel zasebnosti po zasnovi v arhitekturi AI sistemov
- **Upravljanje sprememb**: Formalni postopki za varnostne preglede sprememb AI sistemov

Te temeljne prakse ustvarjajo robustno varnostno izhodišče, ki izboljšuje učinkovitost specifičnih varnostnih nadzorov MCP in zagotavlja celovito zaščito za aplikacije, ki temeljijo na AI.

## Ključne varnostne ugotovitve

- **Večplastni varnostni pristop**: Združite temeljne varnostne prakse (varno programiranje, najmanjše privilegije, preverjanje dobavne verige, kontinuirano spremljanje) z AI-spoškimi nadzori za celovito zaščito

- **Specifični grozljivi elementi za AI**: Sistemi MCP se soočajo z edinstvenimi tveganji, vključno z vnosom navodil, zastrupitvijo orodij, prevzemom sej, težavami z zmedenim pomočnikom, ranljivostmi prehoda žetonov in prekomernimi dovoljenji, ki zahtevajo posebne ukrepe za ublažitev

- **Odličnost overjanja in avtorizacije**: Uporabite robustno overjanje z zunanjimi ponudniki identitet (Microsoft Entra ID), dosledno preverjanje žetonov in nikoli ne sprejemajte žetonov, ki niso izrecno izdani za vaš MCP strežnik

- **Preprečevanje AI napadov**: Uporabite Microsoft Prompt Shields in Azure Content Safety za obrambo pred posrednimi napadi vnosov navodil in zastrupitvijo orodij, hkrati pa preverjajte metapodatke orodij in spremljajte dinamične spremembe

- **Varnost sej in prenosa**: Uporabite kriptografsko varne, nedeterministične ID-je sej, vezane na uporabniške identitete, izvedite pravilno upravljanje življenjskega cikla sej in nikoli ne uporabljajte sej za overjanje

- **Najboljše prakse varnosti OAuth**: Preprečite napade zmedenega pomočnika s eksplicitnim soglasjem uporabnika za dinamično registrirane odjemalce, pravilno implementacijo OAuth 2.1 s PKCE in strogim preverjanjem URI-jev za preusmeritev  

- **Načela varnosti žetonov**: Izogibajte se nepravilnim vzorcem prehoda žetonov, preverjajte trditve o občinstvu žetona, uvajajte kratkoročne žetone z varnim rotiranjem in vzdržujte jasne meje zaupanja

- **Celovita varnost dobavne verige**: Vse komponente AI ekosistema (modeli, vdelave, ponudniki konteksta, zunanji API-ji) obravnavajte z enako varnostno rigoroznostjo kot tradicionalne programske odvisnosti

- **Nenehen razvoj**: Bodite na tekočem z hitro spreminjajočimi se specifikacijami MCP, prispevajte k varnostnim standardom skupnosti in ohranjajte prilagodljive varnostne drže, ko protokol dozori

- **Integracija Microsoftove varnosti**: Izkoristite celoviti varnostni ekosistem Microsofta (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) za izboljšano zaščito implementacij MCP

## Celoviti viri

### **Uradna MCP varnostna dokumentacija**
- [Specifikacija MCP (Trenutno: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najboljše prakse varnosti MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specifikacija avtorizacije MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [GitHub repozitorij MCP](https://github.com/modelcontextprotocol)

### **OWASP MCP varnostni viri**
- [OWASP MCP Azure varnostni vodič](https://microsoft.github.io/mcp-azure-security-guide/) - Celovit OWASP MCP Top 10 z navodili za implementacijo v Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Uradna OWASP MCP varnostna tveganja
- [Delavnica MCP varnostnega vrha (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktična varnostna usposabljanja za MCP v Azure

### **Varnostni standardi in najboljše prakse**
- [Najboljše prakse varnosti OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 spletna varnost aplikacij](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 za velike jezikovne modele](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoftov poročilo o digitalni obrambi](https://aka.ms/mddr)

### **Raziskave in analize varnosti AI**
- [Vnos navodil v MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Napadi zastrupitve orodij (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Poročilo o raziskavah varnosti MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoftove varnostne rešitve**
- [Dokumentacija Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID varnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Najboljše prakse upravljanja žetonov Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Vodniki za implementacijo in vadnice**
- [Azure API Management kot avtentikacijski prehod MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID avtentikacija z MCP strežniki](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Varen shranjevanje in šifriranje žetonov (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps in varnost dobavne verige**
- [Azure DevOps varnost](https://azure.microsoft.com/products/devops)
- [Azure Repos varnost](https://azure.microsoft.com/products/devops/repos/)
- [Microsoftova pot do varne dobavne verige programske opreme](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dodatna varnostna dokumentacija**

Za celovita varnostna navodila si oglejte te specializirane dokumente v tem razdelku:

- **[Primer avtorizacije CIMD in DCR](./samples/cimd-dcr-auth/README.md)** - Izvedljiv TypeScript MCP `2026-07-28` strežnik virov, ki primerja želene Metapodatke ID odjemalca s potisnim padcem zastarelega dinamičnega registriranja odjemalcev
- **[Najboljše prakse varnosti MCP](./mcp-security-best-practices.md)** - Celovite najboljše varnostne prakse za implementacije MCP
- **[Implementacija Azure Content Safety](./azure-content-safety-implementation.md)** - Praktični primeri implementacije za integracijo Azure Content Safety  
- **[MCP varnostni nadzor](./mcp-security-controls.md)** - Najnovejši nadzor in tehnike varnosti za implementacije MCP
- **[Hitri pregled najboljših praks MCP](./mcp-best-practices.md)** - Hitri referenčni vodič za bistvene varnostne prakse MCP
- **[BlueHat 2026: Zavarovanje prihodnosti AI: varovanje MCP z obrambnimi vzorci](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Obrambni vzorci globinske varnosti iz Microsoft Security Response Center (MSRC)

### **Praktična varnostna usposabljanja**

- **[Delavnica varnostnega vrha MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - Celovita praktična delavnica za varovanje MCP strežnikov v Azure z naprednimi tabori od osnovnega tabora do vrha
- **[OWASP MCP Azure varnostni vodič](https://microsoft.github.io/mcp-azure-security-guide/)** - Referenčna arhitektura in navodila za implementacijo za vseh OWASP MCP Top 10 tveganj

---

## Kaj sledi

Naslednje: [Poglavje 3: Začetek](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->