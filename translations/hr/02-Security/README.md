# MCP Sigurnost: Sveobuhvatna Zaštita za AI Sustave

[![MCP Security Best Practices](../../../translated_images/hr/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Kliknite na gornju sliku za pregled videa ove lekcije)_

Sigurnost je temelj dizajna AI sustava, zbog čega joj dajemo prioritet kao drugom dijelu. Ovo je u skladu s Microsoftovim principom **Secure by Design** iz [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) donosi moćne nove mogućnosti AI-pokretanih aplikacija, istovremeno uvodeći jedinstvene sigurnosne izazove koji nadilaze tradicionalne softverske rizike. MCP sustavi suočavaju se s etabliranim sigurnosnim problemima (sigurno kodiranje, načelo najmanjih privilegija, sigurnost opskrbnog lanca) kao i novim AI-specifičnim prijetnjama uključujući prompt injection, trovanje alata, preuzimanje sesije, napade zbunjenog zamjenika, ranjivosti token passthrough i dinamičke izmjene sposobnosti.

Ova lekcija istražuje najkritičnije sigurnosne rizike u MCP implementacijama—obuhvaćajući autentikaciju, autorizaciju, pretjerane dozvole, indirektni prompt injection, sigurnost sesije, probleme zbunjenog zamjenika, upravljanje tokenima i ranjivosti opskrbnog lanca. Naučit ćete primjenjive kontrole i najbolje prakse za ublažavanje ovih rizika koristeći Microsoftova rješenja poput Prompt Shields, Azure Content Safety i GitHub Advanced Security za jačanje vaše MCP implementacije.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- **Prepoznati MCP-specifične prijetnje**: Uočiti jedinstvene sigurnosne rizike u MCP sustavima uključujući prompt injection, trovanje alata, pretjerane dozvole, preuzimanje sesije, probleme zbunjenog zamjenika, ranjivosti token passthrough i rizike opskrbnog lanca
- **Primijeniti sigurnosne kontrole**: Implementirati učinkovite mjere ublažavanja uključujući robusnu autentikaciju, pristup temeljen na načelu najmanjih privilegija, sigurno upravljanje tokenima, kontrole sigurnosti sesije i verifikaciju opskrbnog lanca
- **Iskoristiti Microsoftova sigurnosna rješenja**: Razumjeti i primijeniti Microsoft Prompt Shields, Azure Content Safety i GitHub Advanced Security za zaštitu MCP radnih opterećenja
- **Validirati sigurnost alata**: Prepoznati važnost validacije metapodataka alata, nadzora dinamičkih promjena i obrane od indirektnih prompt injection napada
- **Integrirati najbolje prakse**: Kombinirati uspostavljene sigurnosne temelje (sigurno kodiranje, učvršćivanje poslužitelja, zero trust) s MCP-specifičnim kontrolama za sveobuhvatnu zaštitu

# MCP Sigurnosna arhitektura i kontrole

Moderne MCP implementacije zahtijevaju slojevite sigurnosne pristupe koji adresiraju i tradicionalnu softversku sigurnost i AI-specifične prijetnje. Brzo razvijajuća MCP specifikacija nastavlja usavršavati svoje sigurnosne kontrole, omogućujući bolju integraciju s arhitekturama sigurnosti poduzeća i etabliranim najboljim praksama.

Istraživanje iz [Microsoft Digital Defense Report](https://aka.ms/mddr) pokazuje da bi **98% prijavljenih proboja bilo spriječeno robusnom sigurnosnom higijenom**. Najefikasnija strategija zaštite kombinira temeljne sigurnosne prakse s MCP-specifičnim kontrolama—dokazane osnovne sigurnosne mjere ostaju najutjecajnije u smanjenju ukupnog sigurnosnog rizika.

## Trenutni sigurnosni pejzaž

> **Napomena:** Ove informacije odražavaju MCP sigurnosne standarde na dan **18. prosinca 2025.** MCP protokol se brzo razvija, a buduće implementacije mogu uvesti nove obrasce autentikacije i poboljšane kontrole. Uvijek se referirajte na aktualnu [MCP specifikaciju](https://spec.modelcontextprotocol.io/), [MCP GitHub repozitorij](https://github.com/modelcontextprotocol) i [dokumentaciju najboljih sigurnosnih praksi](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) za najnovije smjernice.

### Evolucija MCP autentikacije

MCP specifikacija značajno je evoluirala u pristupu autentikaciji i autorizaciji:

- **Izvorni pristup**: Rane specifikacije zahtijevale su od programera implementaciju prilagođenih autentikacijskih poslužitelja, pri čemu su MCP poslužitelji djelovali kao OAuth 2.0 Authorization Servers koji izravno upravljaju autentikacijom korisnika
- **Trenutni standard (2025-11-25)**: Ažurirana specifikacija dopušta MCP poslužiteljima delegiranje autentikacije vanjskim pružateljima identiteta (kao što je Microsoft Entra ID), poboljšavajući sigurnosni položaj i smanjujući složenost implementacije
- **Transport Layer Security**: Poboljšana podrška za sigurne transportne mehanizme s odgovarajućim obrascima autentikacije za lokalne (STDIO) i udaljene (Streamable HTTP) veze

## Sigurnost autentikacije i autorizacije

### Trenutni sigurnosni izazovi

Moderne MCP implementacije suočavaju se s nekoliko izazova u autentikaciji i autorizaciji:

### Rizici i vektori prijetnji

- **Pogrešno konfigurirana autorizacijska logika**: Neispravna implementacija autorizacije u MCP poslužiteljima može izložiti osjetljive podatke i nepravilno primijeniti kontrole pristupa
- **Kompromitacija OAuth tokena**: Krađa tokena lokalnog MCP poslužitelja omogućuje napadačima da se lažno predstavljaju kao poslužitelji i pristupe downstream uslugama
- **Ranjivosti token passthrough**: Neispravno rukovanje tokenima stvara zaobilaženje sigurnosnih kontrola i praznine u odgovornosti
- **Pretjerane dozvole**: MCP poslužitelji s prevelikim privilegijama krše načelo najmanjih privilegija i proširuju površinu napada

#### Token passthrough: Kritični anti-obrazac

**Token passthrough je izričito zabranjen** u trenutnoj MCP autorizacijskoj specifikaciji zbog ozbiljnih sigurnosnih posljedica:

##### Zaobilaženje sigurnosnih kontrola
- MCP poslužitelji i downstream API-ji implementiraju ključne sigurnosne kontrole (ograničenje brzine, validacija zahtjeva, nadzor prometa) koje ovise o ispravnoj validaciji tokena
- Izravna upotreba tokena klijenta prema API-ju zaobilazi ove ključne zaštite, narušavajući sigurnosnu arhitekturu

##### Izazovi u odgovornosti i reviziji  
- MCP poslužitelji ne mogu razlikovati klijente koji koriste tokene izdane upstream, što prekida revizijske tragove
- Zapisi downstream poslužitelja resursa prikazuju zavaravajuće izvore zahtjeva umjesto stvarnih MCP poslužiteljskih posrednika
- Istrage incidenata i revizije usklađenosti postaju znatno teže

##### Rizici od izvlačenja podataka
- Nevalidirani token zahtjevi omogućuju zlonamjernim akterima s ukradenim tokenima da koriste MCP poslužitelje kao proxy za izvlačenje podataka
- Kršenja granica povjerenja dopuštaju neovlaštene obrasce pristupa koji zaobilaze namjeravane sigurnosne kontrole

##### Vektori napada na više usluga
- Kompromitirani tokeni prihvaćeni od strane više usluga omogućuju lateralno kretanje kroz povezane sustave
- Pretpostavke povjerenja između usluga mogu biti prekršene kada se ne može potvrditi podrijetlo tokena

### Sigurnosne kontrole i mjere ublažavanja

**Kritični sigurnosni zahtjevi:**

> **OBAVEZNO**: MCP poslužitelji **NE SMIJU** prihvaćati bilo kakve tokene koji nisu izričito izdani za MCP poslužitelj

#### Kontrole autentikacije i autorizacije

- **Temeljita revizija autorizacije**: Provedite sveobuhvatne revizije autorizacijske logike MCP poslužitelja kako biste osigurali da samo namijenjeni korisnici i klijenti mogu pristupiti osjetljivim resursima
  - **Vodič za implementaciju**: [Azure API Management kao autentikacijski gateway za MCP poslužitelje](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integracija identiteta**: [Korištenje Microsoft Entra ID za autentikaciju MCP poslužitelja](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sigurno upravljanje tokenima**: Implementirajte [Microsoftove najbolje prakse za validaciju i životni ciklus tokena](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validirajte da audience tokena odgovara identitetu MCP poslužitelja
  - Implementirajte pravilnu rotaciju i politike isteka tokena
  - Spriječite ponovnu upotrebu tokena i neovlaštenu upotrebu

- **Zaštićeno pohranjivanje tokena**: Sigurno pohranjivanje tokena s enkripcijom u mirovanju i u prijenosu
  - **Najbolje prakse**: [Sigurno pohranjivanje i smjernice za enkripciju tokena](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementacija kontrole pristupa

- **Načelo najmanjih privilegija**: Dodijelite MCP poslužiteljima samo minimalne dozvole potrebne za namjeravanu funkcionalnost
  - Redovite revizije i ažuriranja dozvola za sprječavanje nakupljanja privilegija
  - **Microsoftova dokumentacija**: [Siguran pristup s najmanjim privilegijama](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kontrola pristupa temeljena na ulogama (RBAC)**: Implementirajte detaljne dodjele uloga
  - Usko definirajte uloge za specifične resurse i radnje
  - Izbjegavajte široke ili nepotrebne dozvole koje proširuju površinu napada

- **Kontinuirani nadzor dozvola**: Provedite stalnu reviziju i nadzor pristupa
  - Pratite obrasce korištenja dozvola radi otkrivanja anomalija
  - Pravovremeno uklonite pretjerane ili neiskorištene privilegije

## AI-specifične sigurnosne prijetnje

### Prompt Injection i napadi manipulacije alatima

Moderne MCP implementacije suočavaju se sa sofisticiranim AI-specifičnim vektorima napada koje tradicionalne sigurnosne mjere ne mogu u potpunosti adresirati:

#### **Indirektni Prompt Injection (Cross-Domain Prompt Injection)**

**Indirektni Prompt Injection** predstavlja jednu od najkritičnijih ranjivosti u AI sustavima s MCP-om. Napadači ugrađuju zlonamjerne upute unutar vanjskog sadržaja—dokumenata, web stranica, e-pošte ili izvora podataka—koje AI sustavi potom obrađuju kao legitimne naredbe.

**Scenariji napada:**
- **Injekcija u dokumentima**: Zlonamjerne upute skrivene u obrađenim dokumentima koje pokreću neželjene AI akcije
- **Eksploatacija web sadržaja**: Kompromitirane web stranice s ugrađenim promptovima koji manipuliraju AI ponašanjem prilikom prikupljanja podataka
- **Napadi putem e-pošte**: Zlonamjerni promptovi u e-porukama koji uzrokuju da AI asistenti otkrivaju informacije ili izvode neovlaštene radnje
- **Kontaminacija izvora podataka**: Kompromitirane baze podataka ili API-ji koji poslužuju zagađeni sadržaj AI sustavima

**Stvarni utjecaj**: Ovi napadi mogu rezultirati izvlačenjem podataka, kršenjem privatnosti, generiranjem štetnog sadržaja i manipulacijom korisničkim interakcijama. Za detaljnu analizu pogledajte [Prompt Injection u MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/hr/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Napadi trovanja alata**

**Trovanje alata** cilja na metapodatke koji definiraju MCP alate, iskorištavajući način na koji LLM modeli interpretiraju opise alata i parametre za donošenje odluka o izvršavanju.

**Mehanizmi napada:**
- **Manipulacija metapodacima**: Napadači ubacuju zlonamjerne upute u opise alata, definicije parametara ili primjere korištenja
- **Nevidljive upute**: Skriveni promptovi u metapodacima alata koje AI modeli obrađuju, ali su nevidljivi ljudskim korisnicima
- **Dinamičke izmjene alata ("Rug Pulls")**: Alati koje su korisnici odobrili kasnije se mijenjaju da izvode zlonamjerne radnje bez znanja korisnika
- **Injekcija parametara**: Zlonamjerni sadržaj ugrađen u sheme parametara alata koji utječu na ponašanje modela

**Rizici hostanih poslužitelja**: Udaljeni MCP poslužitelji predstavljaju povećane rizike jer se definicije alata mogu ažurirati nakon početnog odobrenja korisnika, stvarajući scenarije u kojima prethodno sigurni alati postaju zlonamjerni. Za sveobuhvatnu analizu pogledajte [Napadi trovanja alata (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/hr/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Dodatni AI vektori napada**

- **Cross-Domain Prompt Injection (XPIA)**: Sofisticirani napadi koji koriste sadržaj iz više domena zaobilaženjem sigurnosnih kontrola
- **Dinamičke izmjene sposobnosti**: Promjene u stvarnom vremenu u sposobnostima alata koje izbjegavaju početne sigurnosne procjene
- **Trovanje kontekstnog prozora**: Napadi koji manipuliraju velikim kontekstnim prozorima kako bi sakrili zlonamjerne upute
- **Napadi zbunjivanja modela**: Iskorištavanje ograničenja modela za stvaranje nepredvidivog ili nesigurnog ponašanja

### Utjecaj AI sigurnosnih rizika

**Posljedice visokog utjecaja:**
- **Izvlačenje podataka**: Neovlašteni pristup i krađa osjetljivih podataka poduzeća ili osobnih podataka
- **Kršenja privatnosti**: Izlaganje osobnih identifikacijskih podataka (PII) i povjerljivih poslovnih podataka  
- **Manipulacija sustavima**: Neželjene izmjene kritičnih sustava i radnih tokova
- **Krađa vjerodajnica**: Kompromitacija autentikacijskih tokena i vjerodajnica usluga
- **Lateralno kretanje**: Korištenje kompromitiranih AI sustava kao polazišta za šire mrežne napade

### Microsoftova AI sigurnosna rješenja

#### **AI Prompt Shields: Napredna zaštita od injekcijskih napada**

Microsoft **AI Prompt Shields** pružaju sveobuhvatnu obranu od izravnih i neizravnih prompt injection napada kroz višeslojne sigurnosne mehanizme:

##### **Ključni mehanizmi zaštite:**

1. **Napredno otkrivanje i filtriranje**
   - Algoritmi strojnog učenja i NLP tehnike otkrivaju zlonamjerne upute u vanjskom sadržaju
   - Analiza u stvarnom vremenu dokumenata, web stranica, e-pošte i izvora podataka za ugrađene prijetnje
   - Kontekstualno razumijevanje legitimnih naspram zlonamjernih obrazaca promptova

2. **Tehnike isticanja**  
   - Razlikuje pouzdane sistemske upute od potencijalno kompromitiranih vanjskih ulaza
   - Metode transformacije teksta koje poboljšavaju relevantnost modela dok izoliraju zlonamjerni sadržaj
   - Pomaže AI sustavima održati pravilnu hijerarhiju uputa i ignorirati ubačene naredbe

3. **Sustavi razdjelnika i označavanja podataka**
   - Izričito definiranje granica između pouzdanih sistemskih poruka i vanjskog ulaznog teksta
   - Posebni markeri ističu granice između pouzdanih i nepouzdanih izvora podataka
   - Jasna separacija sprječava zbunjenost uputa i neovlašteno izvršavanje naredbi

4. **Kontinuirana obavještajna sigurnosna analiza**
   - Microsoft kontinuirano prati nove obrasce napada i ažurira obrane
   - Proaktivno traženje prijetnji za nove tehnike injekcija i vektore napada
   - Redovita ažuriranja sigurnosnih modela za održavanje učinkovitosti protiv evoluirajućih prijetnji

5. **Integracija Azure Content Safety**
   - Dio sveobuhvatnog Azure AI Content Safety paketa
   - Dodatno otkrivanje pokušaja jailbreaka, štetnog sadržaja i kršenja sigurnosnih politika
   - Jedinstvene sigurnosne kontrole kroz komponente AI aplikacija

**Resursi za implementaciju**: [Microsoft Prompt Shields Dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/hr/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Napredne MCP sigurnosne prijetnje

### Ranjivosti preuzimanja sesije

**Preuzimanje sesije** predstavlja kritični vektor napada u stateful MCP implementacijama gdje neovlaštene strane dobivaju i zloupotrebljavaju legitimne identifikatore sesije za lažno predstavljanje klijenata i izvođenje neovlaštenih radnji.

#### **Scenariji napada i rizici**

- **Prompt injection preuzimanja sesije**: Napadači s ukradenim ID-jevima sesije ubacuju zlonamjerne događaje u poslužitelje koji dijele stanje sesije, potencijalno pokrećući štetne radnje ili pristupajući osjetljivim podacima
- **Izravno lažno predstavljanje**: Ukradeni ID-jevi sesije omogućuju izravne pozive MCP poslužitelju koji zaobilaze autentikaciju, tretirajući napadače kao legitimne korisnike
- **Kompromitirani nastavci streamova**: Napadači mogu prerano prekinuti zahtjeve, uzrokujući da legitimni klijenti nastave s potencijalno zlonamjernim sadržajem

#### **Sigurnosne kontrole za upravljanje sesijama**

**Kritični zahtjevi:**
- **Provjera autorizacije**: MCP poslužitelji koji implementiraju autorizaciju **MORAJU** provjeriti SVE dolazne zahtjeve i **NE SMIJU** se oslanjati na sesije za autentifikaciju
- **Sigurna generacija sesija**: Koristite kriptografski sigurne, nedeterminističke ID-eve sesija generirane sigurnim generatorima slučajnih brojeva
- **Povezivanje sa specifičnim korisnikom**: Povežite ID-eve sesija s informacijama specifičnim za korisnika koristeći formate poput `<user_id>:<session_id>` kako biste spriječili zloupotrebu sesija između korisnika
- **Upravljanje životnim ciklusom sesije**: Implementirajte pravilno isteka, rotaciju i poništavanje kako biste ograničili ranjivosti
- **Sigurnost prijenosa**: Obavezni HTTPS za svu komunikaciju kako bi se spriječilo presretanje ID-eva sesija

### Problem zbunjenog zamjenika

**Problem zbunjenog zamjenika** nastaje kada MCP poslužitelji djeluju kao proxyji za autentifikaciju između klijenata i usluga trećih strana, stvarajući prilike za zaobilaženje autorizacije kroz iskorištavanje statičkih ID-eva klijenata.

#### **Mehanika napada i rizici**

- **Zaobilaženje pristanka temeljeno na kolačićima**: Prethodna autentifikacija korisnika stvara kolačiće pristanka koje napadači iskorištavaju putem zlonamjernih zahtjeva za autorizaciju s izrađenim URI-jevima za preusmjeravanje
- **Krađa autorizacijskog koda**: Postojeći kolačići pristanka mogu uzrokovati da autorizacijski poslužitelji preskoče zaslone pristanka, preusmjeravajući kodove na krajnje točke pod kontrolom napadača  
- **Neovlašteni pristup API-ju**: Ukradeni autorizacijski kodovi omogućuju razmjenu tokena i lažno predstavljanje korisnika bez izričitog odobrenja

#### **Strategije ublažavanja**

**Obavezne kontrole:**
- **Zahtjevi za izričitim pristankom**: MCP proxy poslužitelji koji koriste statičke ID-eve klijenata **MORAJU** dobiti korisnički pristanak za svakog dinamički registriranog klijenta
- **Implementacija sigurnosti OAuth 2.1**: Slijedite trenutne najbolje sigurnosne prakse OAuth-a uključujući PKCE (Proof Key for Code Exchange) za sve zahtjeve za autorizaciju
- **Stroga validacija klijenata**: Implementirajte rigoroznu validaciju URI-jeva za preusmjeravanje i identifikatora klijenata kako biste spriječili iskorištavanje

### Ranjivosti prosljeđivanja tokena  

**Prosljeđivanje tokena** predstavlja eksplicitni anti-uzorak gdje MCP poslužitelji prihvaćaju tokene klijenata bez odgovarajuće validacije i prosljeđuju ih prema nižim API-jima, kršeći MCP specifikacije autorizacije.

#### **Sigurnosne implikacije**

- **Zaobilaženje kontrole**: Izravna upotreba tokena klijenta prema API-ju zaobilazi ključne kontrole ograničenja brzine, validacije i nadzora
- **Kvar tragova revizije**: Tokeni izdani uzvodno onemogućuju identifikaciju klijenta, što narušava mogućnosti istrage incidenata
- **Eksfiltracija podataka putem proxyja**: Nevalidirani tokeni omogućuju zlonamjernim akterima korištenje poslužitelja kao proxyja za neovlašteni pristup podacima
- **Kršenje granica povjerenja**: Pretpostavke povjerenja usluga nižeg sloja mogu biti narušene kada se ne može potvrditi podrijetlo tokena
- **Širenje napada na više usluga**: Kompromitirani tokeni prihvaćeni u više usluga omogućuju lateralno kretanje

#### **Potrebne sigurnosne kontrole**

**Nezaobilazni zahtjevi:**
- **Validacija tokena**: MCP poslužitelji **NE SMIJU** prihvaćati tokene koji nisu izričito izdani za MCP poslužitelj
- **Provjera publike**: Uvijek validirajte da tvrdnje o publici tokena odgovaraju identitetu MCP poslužitelja
- **Ispravan životni ciklus tokena**: Implementirajte kratkotrajne pristupne tokene s praksama sigurne rotacije


## Sigurnost lanca opskrbe za AI sustave

Sigurnost lanca opskrbe evoluirala je izvan tradicionalnih softverskih ovisnosti i obuhvaća cijeli AI ekosustav. Moderni MCP implementacije moraju rigorozno provjeravati i nadzirati sve AI povezane komponente, jer svaka uvodi potencijalne ranjivosti koje mogu ugroziti integritet sustava.

### Proširene komponente AI lanca opskrbe

**Tradicionalne softverske ovisnosti:**
- Open-source biblioteke i okviri
- Slike kontejnera i osnovni sustavi  
- Alati za razvoj i build pipelineovi
- Infrastrukturne komponente i usluge

**AI-specifični elementi lanca opskrbe:**
- **Temeljni modeli**: Predtrenirani modeli od različitih pružatelja koji zahtijevaju provjeru podrijetla
- **Usluge ugradnje (embedding)**: Vanjske usluge vektorizacije i semantičkog pretraživanja
- **Pružatelji konteksta**: Izvori podataka, baze znanja i spremišta dokumenata  
- **API-ji trećih strana**: Vanjske AI usluge, ML pipelineovi i krajnje točke za obradu podataka
- **Artefakti modela**: Težine, konfiguracije i fino podešene varijante modela
- **Izvori podataka za treniranje**: Skupovi podataka korišteni za treniranje i fino podešavanje modela

### Sveobuhvatna strategija sigurnosti lanca opskrbe

#### **Verifikacija komponenti i povjerenje**
- **Provjera podrijetla**: Provjerite podrijetlo, licencu i integritet svih AI komponenti prije integracije
- **Sigurnosna procjena**: Provedite skeniranje ranjivosti i sigurnosne preglede za modele, izvore podataka i AI usluge
- **Analiza reputacije**: Procijenite sigurnosnu povijest i prakse pružatelja AI usluga
- **Provjera usklađenosti**: Osigurajte da sve komponente zadovoljavaju organizacijske sigurnosne i regulatorne zahtjeve

#### **Sigurni pipelineovi za implementaciju**  
- **Automatizirana CI/CD sigurnost**: Integrirajte sigurnosno skeniranje kroz automatizirane pipelineove za implementaciju
- **Integritet artefakata**: Implementirajte kriptografsku verifikaciju za sve implementirane artefakte (kod, modeli, konfiguracije)
- **Postepena implementacija**: Koristite progresivne strategije implementacije sa sigurnosnom validacijom u svakoj fazi
- **Pouzdana spremišta artefakata**: Implementirajte samo iz verificiranih, sigurnih spremišta i registara artefakata

#### **Kontinuirani nadzor i odgovor**
- **Skeniranje ovisnosti**: Stalni nadzor ranjivosti za sve softverske i AI komponente
- **Nadzor modela**: Kontinuirana procjena ponašanja modela, promjena performansi i sigurnosnih anomalija
- **Praćenje zdravlja usluga**: Nadzor vanjskih AI usluga za dostupnost, sigurnosne incidente i promjene politika
- **Integracija obavještajnih podataka o prijetnjama**: Uključivanje feedova prijetnji specifičnih za AI i ML sigurnosne rizike

#### **Kontrola pristupa i načelo najmanjih privilegija**
- **Dozvole na razini komponenti**: Ograničite pristup modelima, podacima i uslugama prema poslovnoj potrebi
- **Upravljanje servisnim računima**: Implementirajte posvećene servisne račune s minimalnim potrebnim dozvolama
- **Segmentacija mreže**: Izolirajte AI komponente i ograničite mrežni pristup između usluga
- **Kontrole API gatewaya**: Koristite centralizirane API gateway-e za kontrolu i nadzor pristupa vanjskim AI uslugama

#### **Odgovor na incidente i oporavak**
- **Postupci brzog odgovora**: Uspostavljeni procesi za zakrpu ili zamjenu kompromitiranih AI komponenti
- **Rotacija vjerodajnica**: Automatizirani sustavi za rotaciju tajni, API ključeva i servisnih vjerodajnica
- **Mogućnosti povrata**: Sposobnost brzog vraćanja na prethodne poznate dobre verzije AI komponenti
- **Oporavak od proboja lanca opskrbe**: Specifični postupci za reagiranje na kompromitacije uzvodnih AI usluga

### Microsoft alati za sigurnost i integraciju

**GitHub Advanced Security** pruža sveobuhvatnu zaštitu lanca opskrbe uključujući:
- **Skeniranje tajni**: Automatsko otkrivanje vjerodajnica, API ključeva i tokena u repozitorijima
- **Skeniranje ovisnosti**: Procjena ranjivosti za open-source ovisnosti i biblioteke
- **CodeQL analiza**: Statička analiza koda za sigurnosne ranjivosti i probleme u kodiranju
- **Uvidi u lanac opskrbe**: Vidljivost u zdravlje i sigurnosni status ovisnosti

**Integracija s Azure DevOps i Azure Repos:**
- Besprijekorna integracija sigurnosnog skeniranja kroz Microsoft razvojne platforme
- Automatizirane sigurnosne provjere u Azure Pipelines za AI radna opterećenja
- Provedba politika za sigurnu implementaciju AI komponenti

**Microsoft interne prakse:**
Microsoft provodi opsežne prakse sigurnosti lanca opskrbe u svim proizvodima. Saznajte o provjerenim pristupima u [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Najbolje prakse temeljne sigurnosti

MCP implementacije nasljeđuju i nadograđuju postojeći sigurnosni položaj vaše organizacije. Jačanje temeljnih sigurnosnih praksi značajno poboljšava ukupnu sigurnost AI sustava i MCP implementacija.

### Osnovni sigurnosni temelji

#### **Sigurne razvojne prakse**
- **Usklađenost s OWASP-om**: Zaštita od [OWASP Top 10](https://owasp.org/www-project-top-ten/) ranjivosti web aplikacija
- **AI-specifične zaštite**: Implementacija kontrola za [OWASP Top 10 za LLM-ove](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Sigurno upravljanje tajnama**: Korištenje posvećenih spremišta za tokene, API ključeve i osjetljive konfiguracijske podatke
- **End-to-end enkripcija**: Implementacija sigurnih komunikacija kroz sve komponente aplikacije i tokove podataka
- **Validacija unosa**: Rigorozna validacija svih korisničkih unosa, API parametara i izvora podataka

#### **Ojačavanje infrastrukture**
- **Višefaktorska autentifikacija**: Obavezni MFA za sve administrativne i servisne račune
- **Upravljanje zakrpama**: Automatizirano, pravovremeno zakrpanje operativnih sustava, okvira i ovisnosti  
- **Integracija pružatelja identiteta**: Centralizirano upravljanje identitetima putem enterprise pružatelja identiteta (Microsoft Entra ID, Active Directory)
- **Segmentacija mreže**: Logička izolacija MCP komponenti za ograničavanje lateralnog kretanja
- **Načelo najmanjih privilegija**: Minimalne potrebne dozvole za sve sustavne komponente i račune

#### **Sigurnosni nadzor i detekcija**
- **Sveobuhvatno evidentiranje**: Detaljno evidentiranje aktivnosti AI aplikacija, uključujući interakcije MCP klijent-poslužitelj
- **Integracija SIEM-a**: Centralizirano upravljanje sigurnosnim informacijama i događajima za detekciju anomalija
- **Analitika ponašanja**: AI-pokretan nadzor za otkrivanje neuobičajenih obrazaca u sustavu i ponašanju korisnika
- **Obavještajni podaci o prijetnjama**: Integracija vanjskih feedova prijetnji i indikatora kompromitacije (IOC)
- **Odgovor na incidente**: Dobro definirani postupci za detekciju, odgovor i oporavak od sigurnosnih incidenata

#### **Arhitektura nulte povjerenja**
- **Nikad ne vjeruj, uvijek provjeri**: Kontinuirana provjera korisnika, uređaja i mrežnih veza
- **Mikrosegmentacija**: Granularne mrežne kontrole koje izoliraju pojedinačne radne zadatke i usluge
- **Sigurnost usredotočena na identitet**: Sigurnosne politike temeljene na verificiranim identitetima, a ne na mrežnoj lokaciji
- **Kontinuirana procjena rizika**: Dinamička evaluacija sigurnosnog položaja na temelju trenutnog konteksta i ponašanja
- **Uvjetni pristup**: Kontrole pristupa koje se prilagođavaju na temelju faktora rizika, lokacije i povjerenja uređaja

### Obrasci integracije u poduzeću

#### **Integracija Microsoft sigurnosnog ekosustava**
- **Microsoft Defender for Cloud**: Sveobuhvatno upravljanje sigurnosnim položajem u oblaku
- **Azure Sentinel**: Cloud-native SIEM i SOAR mogućnosti za zaštitu AI radnih opterećenja
- **Microsoft Entra ID**: Enterprise upravljanje identitetom i pristupom s politikama uvjetnog pristupa
- **Azure Key Vault**: Centralizirano upravljanje tajnama s podrškom hardverskog sigurnosnog modula (HSM)
- **Microsoft Purview**: Upravljanje podacima i usklađenost za AI izvore podataka i tokove rada

#### **Usklađenost i upravljanje**
- **Regulatorna usklađenost**: Osigurajte da MCP implementacije zadovoljavaju industrijske zahtjeve usklađenosti (GDPR, HIPAA, SOC 2)
- **Klasifikacija podataka**: Ispravna kategorizacija i rukovanje osjetljivim podacima obrađenim u AI sustavima
- **Tragovi revizije**: Sveobuhvatno evidentiranje za regulatornu usklađenost i forenzičku istragu
- **Kontrole privatnosti**: Implementacija principa privatnosti po dizajnu u arhitekturi AI sustava
- **Upravljanje promjenama**: Formalni procesi za sigurnosne preglede izmjena AI sustava

Ove temeljne prakse stvaraju snažnu sigurnosnu osnovu koja povećava učinkovitost MCP-specifičnih sigurnosnih kontrola i pruža sveobuhvatnu zaštitu AI aplikacija.

## Ključni sigurnosni zaključci

- **Slojeviti sigurnosni pristup**: Kombinirajte temeljne sigurnosne prakse (sigurno kodiranje, načelo najmanjih privilegija, verifikaciju lanca opskrbe, kontinuirani nadzor) s AI-specifičnim kontrolama za sveobuhvatnu zaštitu

- **AI-specifični sigurnosni pejzaž**: MCP sustavi suočavaju se s jedinstvenim rizicima uključujući injekciju prompta, trovanje alata, otmicu sesija, problem zbunjenog zamjenika, ranjivosti prosljeđivanja tokena i pretjerane dozvole koje zahtijevaju specijalizirane mjere ublažavanja

- **Izvrsnost u autentifikaciji i autorizaciji**: Implementirajte robusnu autentifikaciju koristeći vanjske pružatelje identiteta (Microsoft Entra ID), provodite pravilnu validaciju tokena i nikada ne prihvaćajte tokene koji nisu izričito izdani za vaš MCP poslužitelj

- **Prevencija AI napada**: Implementirajte Microsoft Prompt Shields i Azure Content Safety za obranu od indirektne injekcije prompta i trovanja alata, dok validirate metapodatke alata i nadzirete dinamičke promjene

- **Sigurnost sesija i prijenosa**: Koristite kriptografski sigurne, nedeterminističke ID-eve sesija povezane s identitetima korisnika, implementirajte pravilno upravljanje životnim ciklusom sesije i nikada ne koristite sesije za autentifikaciju

- **Najbolje prakse OAuth sigurnosti**: Spriječite napade zbunjenog zamjenika kroz izričiti korisnički pristanak za dinamički registrirane klijente, pravilnu implementaciju OAuth 2.1 s PKCE i strogu validaciju URI-ja za preusmjeravanje  

- **Principi sigurnosti tokena**: Izbjegavajte anti-uzorak prosljeđivanja tokena, validirajte tvrdnje o publici tokena, implementirajte kratkotrajne tokene sa sigurnom rotacijom i održavajte jasne granice povjerenja

- **Sveobuhvatna sigurnost lanca opskrbe**: Postupajte sa svim AI komponentama ekosustava (modeli, embedding, pružatelji konteksta, vanjski API-ji) s istom sigurnosnom rigoroznošću kao i s tradicionalnim softverskim ovisnostima

- **Kontinuirana evolucija**: Budite u toku s brzo mijenjajućim MCP specifikacijama, doprinosite sigurnosnim standardima zajednice i održavajte prilagodljive sigurnosne položaje kako protokol sazrijeva

- **Microsoft sigurnosna integracija**: Iskoristite Microsoftov sveobuhvatni sigurnosni ekosustav (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) za poboljšanu zaštitu MCP implementacija

## Sveobuhvatni resursi

### **Službena MCP sigurnosna dokumentacija**
- [MCP specifikacija (trenutno: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP najbolje sigurnosne prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP specifikacija autorizacije](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub repozitorij](https://github.com/modelcontextprotocol)

### **Sigurnosni standardi i najbolje prakse**
- [OAuth 2.0 najbolje sigurnosne prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 sigurnost web aplikacija](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 za velike jezične modele](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Istraživanje i analiza AI sigurnosti**
- [Injekcija prompta u MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Napadi trovanja alata (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Sigurnosni istraživački izvještaj (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Sigurnosna rješenja**
- [Microsoft Prompt Shields Dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Usluga](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Sigurnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Najbolje prakse](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Vodiči za implementaciju i tutorijali**
- [Azure API Management kao MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentikacija s MCP serverima](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Sigurno pohranjivanje tokena i enkripcija (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps i sigurnost lanca opskrbe**
- [Azure DevOps Sigurnost](https://azure.microsoft.com/products/devops)
- [Azure Repos Sigurnost](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Put prema sigurnosti lanca opskrbe](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dodatna sigurnosna dokumentacija**

Za sveobuhvatne sigurnosne smjernice, pogledajte ove specijalizirane dokumente u ovom odjeljku:

- **[MCP Sigurnosne najbolje prakse 2025](./mcp-security-best-practices-2025.md)** - Potpune sigurnosne najbolje prakse za MCP implementacije
- **[Azure Content Safety Implementacija](./azure-content-safety-implementation.md)** - Praktični primjeri implementacije za integraciju Azure Content Safety  
- **[MCP Sigurnosne kontrole 2025](./mcp-security-controls-2025.md)** - Najnovije sigurnosne kontrole i tehnike za MCP implementacije
- **[MCP Najbolje prakse Brzi vodič](./mcp-best-practices.md)** - Brzi vodič za osnovne MCP sigurnosne prakse

---

## Što slijedi

Sljedeće: [Poglavlje 3: Početak](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->