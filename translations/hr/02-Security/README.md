# MCP Sigurnost: Sveobuhvatna Zaštita za AI Sustave

[![MCP Sigurnost Najbolje Prakse](../../../translated_images/hr/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Kliknite na sliku iznad za prikaz videa ove lekcije)_

Sigurnost je temeljni dio dizajna AI sustava, zbog čega joj dajemo prioritet kao našoj drugoj sekciji. Ovo se slaže s Microsoftovim načelom **Sigurno po Dizajnu** iz [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) donosi moćne nove mogućnosti AI-pokretanim aplikacijama, dok uvodi jedinstvene sigurnosne izazove koji nadilaze tradicionalne softverske rizike. MCP sustavi se suočavaju i s postojećim sigurnosnim problemima (sigurno programiranje, najmanje ovlasti, sigurnost opskrbnog lanca) kao i s novim AI-specifičnim prijetnjama uključujući ubrizgavanje upita, trovanje alata, preuzimanje sesije, napade zbrkanog zamjenika, ranjivosti prolaza tokena i dinamične izmjene mogućnosti.

Ova lekcija istražuje najkritičnije sigurnosne rizike u MCP implementacijama—obuhvaćajući autentikaciju, autorizaciju, prekomjerne dozvole, indirektno ubrizgavanje upita, sigurnost sesije, probleme zbrkanog zamjenika, upravljanje tokenima i ranjivosti opskrbnog lanca. Naučit ćete provedive kontrole i najbolje prakse za ublažavanje ovih rizika koristeći Microsoftova rješenja kao što su Prompt Shields, Azure Content Safety i GitHub Advanced Security za ojačavanje vaše MCP implementacije.

## Ciljevi Učenja

Do kraja ove lekcije, moći ćete:

- **Prepoznati MCP-Specifične Prijetnje**: Prepoznati jedinstvene sigurnosne rizike u MCP sustavima uključujući ubrizgavanje upita, trovanje alata, prekomjerne dozvole, preuzimanje sesije, probleme zbrkanog zamjenika, ranjivosti prolaza tokena i rizike opskrbnog lanca
- **Primijeniti Sigurnosne Kontrole**: Implementirati učinkovite mjere ublažavanja uključujući robusnu autentikaciju, pristup s najmanje ovlasti, sigurno upravljanje tokenima, kontrole sigurnosti sesije i verifikaciju opskrbnog lanca
- **Iskoristiti Microsoftova Sigurnosna Rješenja**: Razumjeti i implementirati Microsoft Prompt Shields, Azure Content Safety i GitHub Advanced Security za zaštitu MCP radnih opterećenja
- **Validirati Sigurnost Alata**: Prepoznati važnost validacije metapodataka alata, nadgledanja dinamičkih promjena i obrane od indirektnih napada ubrizgavanja upita
- **Integrirati Najbolje Prakse**: Kombinirati uspostavljene sigurnosne temelje (sigurno programiranje, učvršćivanje poslužitelja, zero trust) s MCP-specifičnim kontrolama za sveobuhvatnu zaštitu

# MCP Sigurnosna Arhitektura i Kontrole

Moderni MCP implementacije zahtijevaju složene sigurnosne pristupe koji rješavaju i tradicionalne softverske sigurnosne prijetnje i AI-specifične prijetnje. Brzo razvijajuća MCP specifikacija nastavlja sazrijevati svoje sigurnosne kontrole, omogućujući bolju integraciju s arhitekturama sigurnosti poduzeća i uspostavljenim najboljim praksama.

Istraživanje iz [Microsoft Digital Defense Report](https://aka.ms/mddr) pokazuje da bi **98% prijavljenih proboja bilo spriječeno jakom sigurnosnom higijenom**. Najefektivnija strategija zaštite kombinira osnovne sigurnosne prakse s MCP-specifičnim kontrolama—dokazano temeljne sigurnosne mjere ostaju najutjecajnije za smanjenje ukupnog sigurnosnog rizika.

## Trenutni Sigurnosni Pejzaž

> **Napomena:** Ovo poglavlje kombinira uspostavljene MCP sigurnosne kontrole s
> trenutnim **MCP Specification 2026-07-28** smjernicama za autorizaciju. Uvijek se
> pozivajte na aktualni [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub repozitorij](https://github.com/modelcontextprotocol) i
> [dokumentaciju najboljih sigurnosnih praksi](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> pri implementaciji koda osjetljivog na sigurnost.

> **Ažuriranje autorizacije:** MCP `2026-07-28` zahtijeva od klijenata da validiraju
> `iss` parametar u autorizacijskim odgovorima (RFC 9207) i vežu registrirane
> vjerodajnice uz izdavački autorizacijski server. Dinamička registracija klijenta
> se ukida; nove implementacije trebaju koristiti Client ID Metadata Dokumente.
> Pogledajte [Što se Promijenilo u MCP: Specifikacija 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> za potpuni popis promjena u autorizaciji.

## 🏔️ MCP Sigurnosni Summit Radionica (Sherpa)

Za **praktičnu sigurnosnu obuku** toplo preporučujemo **MCP Sigurnosnu Summit Radionicu** (Sherpa) - sveobuhvatnu vođenu ekspediciju za osiguranje MCP poslužitelja u Microsoft Azure-u.

### Pregled radionice

[MCP Sigurnosna Summit Radionica](https://azure-samples.github.io/sherpa/) pruža praktičnu, provedivu sigurnosnu obuku kroz dokazan metodologiju "ranjiv → iskorišten → popravljen → potvrđeno". Vi ćete:

- **Učiti Razbijanjem Stvari**: Iskusiti ranjivosti iz prve ruke iskorištavanjem namjerno nesigurnih poslužitelja
- **Koristiti Azure-nativnu Sigurnost**: Iskoristiti Azure Entra ID, Key Vault, API Management i AI Content Safety
- **Slijediti Obranu-u-Dubinu**: Napredovati kroz kampove gradeći slojevite sigurnosne barijere
- **Primijeniti OWASP Standarde**: Svaka tehnika mapira se na [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Dobiti Kôd za Proizvodnju**: Odlazite s funkcionalnim, testiranim implementacijama

### Ruta ekspedicije

| Kamp | Fokus | OWASP Rizici Pokriveni |
|------|-------|---------------------|
| **Osnovni Kamp** | MCP temelji & ranjivosti autentikacije | MCP01, MCP07 |
| **Kamp 1: Identitet** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Kamp 2: Gateway** | API Management, Privatni Endpointi, upravljanje | MCP02, MCP06, MCP07, MCP09 |
| **Kamp 3: I/O Sigurnost** | Ubrizgavanje upita, zaštita PII, sigurnost sadržaja | MCP03, MCP05, MCP06, MCP10 |
| **Kamp 4: Nadgledanje** | Log Analytics, nadzorne ploče, detekcija prijetnji | MCP04, MCP08 |
| **Summit** | Integracijski test Red Team / Blue Team | Svi |

**Započni**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Sigurnosnih Rizika

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) detaljno opisuje deset najkritičnijih sigurnosnih rizika za MCP implementacije:

| Rizik | Opis | Azure Ublažavanje |
|------|-------------|------------------|
| **MCP01** | Pogrešno upravljanje tokenima & izlaganje tajni | Azure Key Vault, Managed Identity |
| **MCP02** | Eskalacija privilegija putem nepotrebnih dozvola | RBAC, Conditional Access |
| **MCP03** | Trovanje alata | Validacija alata, provjera integriteta |
| **MCP04** | Napadi na softverski opskrbni lanac & manipulacija ovisnostima | GitHub Advanced Security, skeniranje ovisnosti |
| **MCP05** | Ubrizgavanje i izvršenje naredbi | Validacija unosa, sandboxing |
| **MCP06** | Subverzija protoka namjere | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Nedostatna autentikacija & autorizacija | Azure Entra ID, OAuth 2.1 s PKCE |
| **MCP08** | Nedostatak revizije i telemetrije | Azure Monitor, Application Insights |
| **MCP09** | Sjenoviti MCP poslužitelji | Upravljanje API Centerom, mrežna izolacija |
| **MCP10** | Ubrizgavanje konteksta & prekomjerno dijeljenje | Klasifikacija podataka, minimalna izloženost |

### Evolucija MCP Autentikacije

MCP specifikacija značajno se razvila u pristupu autentikaciji i autorizaciji:

- **Izvorni Pristup**: Rane specifikacije zahtijevale su da programeri implementiraju prilagođene autorizacijske poslužitelje, pri čemu MCP poslužitelji djeluju kao OAuth 2.0 autorizacijski poslužitelji koji upravljaju autentikacijom korisnika izravno
- **Trenutni Standard (`2026-07-28`)**: MCP poslužitelji mogu delegirati autentikaciju
  vanjskim pružateljima identiteta poput Microsoft Entra ID-a. Klijenti također
  moraju primijeniti zahtjeve za provjeru izdavača i povezivanje vjerodajnica.
- **Sigurnost sloja prijenosa (TLS)**: Poboljšana podrška za sigurne mehanizme prijenosa s ispravnim obrascima autentikacije za lokalne (STDIO) i udaljene (Streamable HTTP) veze

## Sigurnost Autentikacije & Autorizacije

### Trenutni Sigurnosni Izazovi

Moderni MCP implementacije suočavaju se s nekoliko izazova u autentikaciji i autorizaciji:

### Rizici & Vektori Prijetnji

- **Pogrešno Konfigurirana Logika Autorizacije**: Manjkava implementacija autorizacije u MCP poslužiteljima može izložiti osjetljive podatke i nepravilno primijeniti kontrole pristupa
- **Kompromitacija OAuth Tokena**: Krađa tokena lokalnog MCP poslužitelja omogućuje napadačima da se predstavljaju kao poslužitelji i pristupe niže ležećim uslugama
- **Ranjivosti Prolaza Tokena**: Nepravilno rukovanje tokenima stvara zaobilaženje sigurnosnih kontrola i praznine u odgovornosti
- **Prekomjerne Dozvole**: MCP poslužitelji s prevelikim ovlastima krše načelo najmanje povlastice i šire površine napada

#### Prolaz Tokena: Kritičan Anti-Obrazac

**Prolaz tokena je izričito zabranjen** u trenutnoj MCP specifikaciji autorizacije zbog ozbiljnih sigurnosnih posljedica:

##### Zaobilaženje Sigurnosnih Kontrola
- MCP poslužitelji i API-ji nižeg sloja implementiraju ključne sigurnosne kontrole (ograničenje brzine, validaciju zahtjeva, nadzor prometa) koje ovise o ispravnoj provjeri tokena
- Izravna upotreba tokena između klijenta i API-ja zaobilazi ove ključne zaštite, podrivajući sigurnosnu arhitekturu

##### Izazovi Odgovornosti & Revizije  
- MCP poslužitelji ne mogu razlikovati klijente koji koriste tokene izdane na višem sloju, čime se narušavaju revizijski tragovi
- Dnevnici poslužitelja resursa nižeg sloja prikazuju varljive izvore zahtjeva umjesto stvarnih MCP poslužiteljskih posrednika
- Istrage incidenata i usklađenost postaju znatno teže

##### Rizici Ekfiltracije Podataka
- Nevalidirane tvrdnje tokena omogućuju zlonamjernim akterima s ukradenim tokenima korištenje MCP poslužitelja kao proxyja za iznošenje podataka
- Kršenje granice povjerenja omogućuje neovlaštene obrasce pristupa koji zaobilaze namijenjene sigurnosne kontrole

##### Vektori Napada Višestrukih Usluga
- Kompromitirani tokeni prihvaćeni od strane više usluga omogućuju lateralno kretanje kroz povezane sustave
- Pretpostavke povjerenja između usluga mogu biti prekršene ako se ne može potvrditi podrijetlo tokena

### Sigurnosne Kontrole & Ublažavanja

**Ključni Sigurnosni Zahtjevi:**

> **OBAVEZNO**: MCP poslužitelji **NE SMIJU** prihvaćati tokene koji nisu eksplicitno izdani za MCP poslužitelj

#### Kontrole Autentikacije & Autorizacije

- **Temeljita Revizija Autorizacije**: Provesti sveobuhvatne revizije logike autorizacije MCP poslužitelja kako bi se osiguralo da samo namijenjeni korisnici i klijenti imaju pristup osjetljivim resursima
  - **Vodič za implementaciju**: [Azure API Management kao Gateway za Autentikaciju MCP Poslužitelja](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integracija Identiteta**: [Korištenje Microsoft Entra ID za MCP Autentikaciju Poslužitelja](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Sigurno Upravljanje Tokenima**: Implementirati [Microsoftove najbolje prakse validacije tokena i životnog ciklusa](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validirati da tvrdnje publike tokena odgovaraju identitetu MCP poslužitelja
  - Implementirati ispravne politike rotacije i isteka tokena
  - Spriječiti ponovnu upotrebu tokena i neovlaštenu uporabu

- **Zaštićeno Pohranjivanje Tokena**: Sigurno pohranjivanje tokena uz enkripciju u stanju mirovanja i tijekom prijenosa
  - **Najbolje Prakse**: [Vodič za Sigurno Pohranjivanje i Enkripciju Tokena](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementacija Kontrole Pristupa

- **Načelo Najmanje Povlastice**: Dodijeliti MCP poslužiteljima samo minimalna dopuštenja potrebna za predviđenu funkcionalnost
  - Redovite revizije i ažuriranja dozvola radi sprječavanja širenja privilegija
  - **Microsoft Dokumentacija**: [Siguran Pristup s Najmanje Povlastica](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kontrola Pristupa Temeljena na Ulogama (RBAC)**: Implementirati fino podešene dodjele uloga
  - Usko definirati uloge prema specifičnim resursima i radnjama
  - Izbjegavati široke ili nepotrebne dozvole koje povećavaju površinu napada

- **Kontinuirano Praćenje Dozvola**: Implementirati stalnu reviziju i nadzor pristupa
  - Nadzirati obrasce korištenja dozvola radi anomalija
  - Brzo uklanjati prekomjerne ili neiskorištene privilegije

## AI-Specifične Sigurnosne Prijetnje

### Napadi na Ubrizgavanje Upita & Manipulaciju Alata

Moderni MCP implementacije suočavaju se sa sofisticiranim AI-specifičnim vektorima napada koje tradicionalne sigurnosne mjere ne mogu u potpunosti adresirati:

#### **Indirektno Ubrizgavanje Upita (Ubrizgavanje Upita Preko Domeni)**

**Indirektno ubrizgavanje upita** predstavlja jednu od najozbiljnijih ranjivosti u AI sustavima opremljenim MCP-om. Napadači ugrađuju zlonamjerne upute u vanjski sadržaj—dokumente, web stranice, e-mailove ili izvore podataka—koje AI sustavi potom obrađuju kao legitimne naredbe.

**Scenariji napada:**
- **Ubrizgavanje u Dokumente**: Zlonamjerne upute skrivene u obrađenim dokumentima koje pokreću neželjene AI akcije
- **Eksploatacija Web Sadržaja**: Kompromitirane web stranice koje sadrže ugrađene upite za manipulaciju AI ponašanjem pri dohvaćanju podataka
- **Napadi putem E-maila**: Zlonamjerni upiti u e-mailovima koji uzrokuju curenje informacija ili neovlaštene akcije AI asistenata
- **Kontaminacija Izvora Podataka**: Kompromitirane baze podataka ili API-ji koji poslužuju onečišćeni sadržaj AI sustavima

**Stvarna Posljedica**: Ovi napadi mogu rezultirati ekfiltracijom podataka, povredama privatnosti, generiranjem štetnog sadržaja i manipulacijom korisničkih interakcija. Za detaljnu analizu pogledajte [Prompt Injection u MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Dijagram napada ubrizgavanja upita](../../../translated_images/hr/prompt-injection.ed9fbfde297ca877.webp)

#### **Napadi Trovanja Alata**

**Trovanje alata** cilja metapodatke koji definiraju MCP alate, iskorištavajući način na koji LLM-ovi tumače opise i parametre alata za donošenje odluka o izvršenju.

**Mehanizmi napada:**
- **Manipulacija Metapodacima**: Napadači ubrizgavaju zlonamjerne upute u opise alata, definicije parametara ili primjere korištenja
- **Nevidljive Upute**: Sakriveni upiti u metapodacima alata koje obrađuju AI modeli, ali su nevidljivi ljudskim korisnicima
- **Dinamična Modifikacija Alata ("Rug Pulls")**: Alati koje su korisnici odobrili kasnije se mijenjaju da bi se izvršavale zlonamjerne radnje bez korisnikove svijesti
- **Ubrizgavanje Parametara**: Zlonamjerni sadržaj ugrađen u sheme parametara alata koji utječe na ponašanje modela


**Rizici hostanih poslužitelja**: Remote MCP poslužitelji predstavljaju povišene rizike jer se definicije alata mogu ažurirati nakon početnog odobrenja korisnika, stvarajući scenarije u kojima alati koji su prije bili sigurni postaju zlonamjerni. Za sveobuhvatnu analizu pogledajte [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Shema napada ubacivanjem alata](../../../translated_images/hr/tool-injection.3b0b4a6b24de6bef.webp)

#### **Dodatni vektori napada s AI**

- **Ubaci upute preko domena (XPIA)**: Sofisticirani napadi koji koriste sadržaj iz više domena zaobilaženje sigurnosnih kontrola
- **Dinamička modifikacija mogućnosti**: Promjene sposobnosti alata u stvarnom vremenu koje zaobilaze početne sigurnosne procjene
- **Zagađenje kontekstnog prozora**: Napadi koji manipuliraju velikim kontekstnim prozorima kako bi sakrili zlonamjerne upute
- **Napadi stvaranja zabune modela**: Iskorištavanje ograničenja modela za stvaranje nepredvidivog ili nesigurnog ponašanja


### Utjecaj rizika na sigurnost AI

**Posljedice velikog utjecaja:**
- **Eksfiltracija podataka**: Neovlašteni pristup i krađa osjetljivih podataka poduzeća ili osobnih podataka
- **Povrede privatnosti**: Izlaganje osobno identificirajućih podataka (PII) i povjerljivih poslovnih informacija  
- **Manipulacija sustavom**: Nezadane izmjene kritičnih sustava i tokova rada
- **Krađa vjerodajnica**: Kompromitiranje autentikacijskih tokena i vjerodajnica za usluge
- **Lateralno kretanje**: Korištenje kompromitiranih AI sustava kao polazišta za šire napade na mrežu

### Microsoft AI sigurnosna rješenja

#### **AI Prompt Shields: Napredna zaštita od napada ubacivanjem uputa**

Microsoft **AI Prompt Shields** nude sveobuhvatnu obranu od izravnih i neizravnih napada ubacivanja uputa kroz višeslojne sigurnosne mehanizme:

##### **Osnovni mehanizmi zaštite:**

1. **Napredno otkrivanje i filtriranje**
   - Algoritmi strojnog učenja i tehnike NLP-a koji otkrivaju zlonamjerne instrukcije u vanjskom sadržaju
   - Analiza u stvarnom vremenu dokumenata, web stranica, e-mailova i izvora podataka za ugrađene prijetnje
   - Kontekstualno razumijevanje legitimnih nasuprot zlonamjernim obrascima uputa

2. **Tehnike isticanja**  
   - Razlikuje pouzdane sistemske upute od potencijalno kompromitiranih vanjskih unosa
   - Metode transformacije teksta koje pojačavaju relevantnost modela dok izoliraju zlonamjerni sadržaj
   - Pomaže AI sustavima održati ispravan hijerarhijski redoslijed uputa i ignorirati ubačene naredbe

3. **Sustavi ograničavanja i označavanja podataka**
   - Izričito definiranje granica između pouzdanih sistemskih poruka i vanjskog teksta unosa
   - Posebni markeri ističu granice između pouzdanih i nepouzdanih izvora podataka
   - Jasna separacija sprječava zbunjivanje uputa i neovlaštenu izvršnu naredbu

4. **Neprekidni nadzor prijetnji**
   - Microsoft kontinuirano prati nove obrasce napada i ažurira obrane
   - Proaktivno traženje prijetnji za nove tehnike ubrizgavanja i vektore napada
   - Redovita ažuriranja sigurnosnih modela održavaju učinkovitost protiv evoluirajućih prijetnji

5. **Integracija Azure Content Safety**
   - Dio sveobuhvatnog Azure AI sigurnosnog paketa za sadržaj
   - Dodatno otkrivanje pokušaja jailbreaka, štetnog sadržaja i kršenja sigurnosnih politika
   - Jedinstvene sigurnosne kontrole u svim komponentama AI aplikacija

**Resursi za implementaciju**: [Microsoft Prompt Shields Dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Zaštita Microsoft Prompt Shields](../../../translated_images/hr/prompt-shield.ff5b95be76e9c78c.webp)


## Napredne prijetnje sigurnosti MCP-a

### Ranljivosti preuzimanja sesije

**Preuzimanje sesije** predstavlja kritični vektor napada u implementacijama MCP-a sa stanjem gdje neautorizirane strane pribavljaju i zloupotrebljavaju legitimne identifikatore sesija da bi se predstavljale kao klijenti i izvršavale neovlaštene radnje.

#### **Scenariji napada i rizici**

- **Ubacivanje uputa preuzimanjem sesije**: Napadači s ukradenim ID-jevima sesija ubacuju zlonamjerne događaje u poslužitelje koji dijele stanje sesije, potencijalno pokrećući štetne akcije ili pristup osjetljivim podacima
- **Izravno predstavljanja**: Ukradeni ID-ovi sesija omogućuju izravne pozive MCP poslužitelju koji zaobilaze autentikaciju tretirajući napadače kao legitimne korisnike
- **Kompromitirani nastavci tokova**: Napadači mogu prerano prekinuti zahtjeve, prisiljavajući legitimne klijente da nastave s potencijalno zlonamjernim sadržajem

#### **Sigurnosne kontrole za upravljanje sesijama**

**Kritični zahtjevi:**
- **Verifikacija autorizacije**: MCP poslužitelji koji implementiraju autorizaciju **MORAJU** provjeriti SVE dolazne zahtjeve i **NE SMIJU** se oslanjati na sesije za autentikaciju
- **Sigurna generacija sesija**: Koristiti kriptografski sigurne, nedeterminističke ID-jeve sesija generirane pomoću sigurnih generatora slučajnih brojeva
- **Povezivanje sa specifičnim korisnikom**: Povezati ID-jeve sesije s korisničkim podacima koristeći formate poput `<user_id>:<session_id>` kako bi se spriječila zloupotreba sesija između korisnika
- **Upravljanje životnim ciklusom sesije**: Implementirati pravilno istecanje, rotaciju i nevaljanost za ograničavanje ranjivosti
- **Sigurnost prijenosa**: Obavezni HTTPS za svu komunikaciju kako bi se spriječilo presretanje ID-ja sesije

### Problem zbunjenog zastupnika

**Problem zbunjenog zastupnika** nastaje kada MCP poslužitelji djeluju kao proxy autentikacije između klijenata i usluga trećih strana, stvarajući mogućnosti za zaobilaženje autorizacije iskorištavanjem statičkih ID-eva klijenata.

#### **Mehanika napada i rizici**

- **Zaobilaženje pristanka na temelju kolačića**: Prethodna autentikacija korisnika stvara kolačiće pristanka koje napadači iskorištavaju zlonamjernim zahtjevima autorizacije s izrađenim URI-jevima za preusmjeravanje
- **Krađa autorizacijskog koda**: Postojeći kolačići pristanka mogu uzrokovati da autorizacijski poslužitelji preskoče zaslone pristanka, preusmjeravajući kodove na krajnje točke pod kontrolom napadača  
- **Neovlašteni pristup API-ju**: Ukradeni autorizacijski kodovi omogućuju zamjenu tokena i predstavljanje korisnika bez eksplicitnog odobrenja

#### **Strategije ublažavanja**

**Obavezne kontrole:**
- **Izričite obaveze pristanka**: MCP proxy poslužitelji koji koriste statičke ID-jeve klijenata **MORAJU** dobiti korisnički pristanak za svakog dinamički registriranog klijenta
- **Implementacija OAuth 2.1 sigurnosti**: Slijediti trenutne najbolje prakse OAuth sigurnosti uključujući PKCE (Proof Key for Code Exchange) za sve zahtjeve autorizacije
- **Stroga validacija klijenta**: Implementirati rigoroznu validaciju URI-jeva za preusmjeravanje i identifikatora klijenta kako bi se spriječila zloupotreba

### Ranljivosti prosljeđivanja tokena  

**Prosljeđivanje tokena** predstavlja eksplicitni anti-obrazac gdje MCP poslužitelji prihvaćaju klijentske tokene bez pravilne verifikacije i prosljeđuju ih API-jima nižeg sloja, kršeći MCP specifikacije autorizacije.

#### **Sigurnosni učinci**

- **Zaobilaženje kontrole**: Izravna uporaba tokena klijent-API zaobilazi kritične kontrole ograničenja brzine, validacije i nadzora
- **Krađa tragova revizije**: Tokeni izdani gore čine identifikaciju klijenta nemogućom, remeteći mogućnosti istrage incidenata
- **Eksfiltracija podataka posredstvom proxyja**: Nevalidirani tokeni omogućuju zlonamjernim akterima korištenje poslužitelja kao proxyja za neovlašteni pristup podacima
- **Kršenje granica povjerenja**: Usluge niže razine mogu prekršiti povjerenje ako se ne može verificirati izvor tokena
- **Proširenje napada na više usluga**: Kompromitirani tokeni prihvaćeni u više usluga omogućuju lateralna kretanja

#### **Potrebne sigurnosne kontrole**

**Neophodni uvjeti:**
- **Validacija tokena**: MCP poslužitelji **NE SMIJU** prihvatiti tokene koji nisu izričito izdani za MCP poslužitelj
- **Provjera publike tokena**: Uvijek potvrditi da se tvrdnje o publici u tokenu podudaraju s identitetom MCP poslužitelja
- **Ispravan životni ciklus tokena**: Implementirati kratkotrajne pristupne tokene s sigurnim praksama rotacije


## Sigurnost opskrbnog lanca za AI sustave

Sigurnost opskrbnog lanca se razvila izvan tradicionalnih softverskih ovisnosti i obuhvaća cijeli AI ekosustav. Moderne MCP implementacije moraju rigorozno provjeravati i pratiti sve AI povezane komponente jer svaka unosi potencijalne ranjivosti koje mogu kompromitirati integritet sustava.

### Proširene AI komponente opskrbnog lanca

**Tradicionalne softverske ovisnosti:**
- Open-source biblioteke i okviri
- Container slike i temeljni sustavi  
- Razvojni alati i build pipeline-i
- Komponente infrastrukture i usluge

**Specifični AI elementi opskrbnog lanca:**
- **Temeljni modeli**: Predtrenirani modeli od različitih dobavljača koji zahtijevaju provjeru izvora
- **Usluge ugrađivanja**: Vanjske usluge vektorizacije i semantičkog pretraživanja
- **Pružatelji konteksta**: Izvori podataka, baze znanja i repozitoriji dokumenata  
- **API-ji trećih strana**: Vanjske AI usluge, ML pipeline-i i krajnje točke obrade podataka
- **Artefakti modela**: Težine, konfiguracije i fino ugađane varijante modela
- **Izvori podataka za treniranje**: Skupovi podataka korišteni za treniranje i fino podešavanje modela

### Sveobuhvatna strategija sigurnosti opskrbnog lanca

#### **Verifikacija komponenti i povjerenje**
- **Provjera izvora**: Provjeriti podrijetlo, licencu i integritet svih AI komponenti prije integracije
- **Sigurnosna procjena**: Provoditi skeniranje ranjivosti i sigurnosne preglede modela, izvora podataka i AI usluga
- **Analiza reputacije**: Procijeniti sigurnosni zapis i prakse dobavljača AI usluga
- **Provjera usklađenosti**: Osigurati da sve komponente zadovoljavaju organizacijske sigurnosne i regulatorne zahtjeve

#### **Sigurni pipeline-i za implementaciju**  
- **Automatizirano CI/CD skeniranje**: Integrirati sigurnosno skeniranje kroz automatizirane pipeline-e implementacije
- **Integritet artefakata**: Implementirati kriptografske provjere za sve implementirane artefakte (kod, modeli, konfiguracije)
- **Postepena implementacija**: Koristiti progresivne strategije implementacije sa sigurnosnom validacijom na svakoj fazi
- **Pouzdani repozitoriji artefakata**: Implementirati samo iz verificiranih, sigurnih registara i repozitorija artefakata

#### **Neprekidni nadzor i odgovor**
- **Skeniranje ovisnosti**: Stalni nadzor ranjivosti za sve softverske i AI komponente ovisnosti
- **Praćenje modela**: Kontinuirana procjena ponašanja modela, drift performansi i sigurnosnih anomalija
- **Praćenje stanja usluge**: Nadzirati vanjske AI usluge za dostupnost, sigurnosne incidente i promjene politika
- **Integracija obavještavanja o prijetnjama**: Uključivanje feedova prijetnji specifičnih za AI i ML sigurnosne rizike

#### **Kontrola pristupa i minimalna privilegija**
- **Dozvole na razini komponenti**: Ograničiti pristup modelima, podacima i uslugama prema poslovnoj potrebi
- **Upravljanje računima usluga**: Implementirati zasebne račune usluga s minimalnom potrebnom dozvolom
- **Segmentacija mreže**: Izolirati AI komponente i ograničiti mrežni pristup između usluga
- **Kontrole API Gateway-a**: Koristiti centralizirane API gateway-e za kontrolu i nadzor pristupa vanjskim AI uslugama

#### **Odgovor na incidente i oporavak**
- **Postupci brzog odgovora**: Uspostavljeni procesi za zakrpu ili zamjenu kompromitiranih AI komponenti
- **Rotacija vjerodajnica**: Automatizirani sustavi za rotaciju tajni, API ključeva i vjerodajnica usluga
- **Mogućnosti povratka**: Sposobnost brzog vraćanja na prethodne poznate dobre verzije AI komponenti
- **Oporavak od proboja opskrbnog lanca**: Specifični postupci za reagiranje na kompromitiranje AI usluga višeg sloja

### Microsoft sigurnosni alati i integracija

**GitHub Advanced Security** pruža sveobuhvatnu zaštitu opskrbnog lanca uključujući:
- **Skeniranje tajni**: Automatizirano otkrivanje vjerodajnica, API ključeva i tokena u repozitorijima
- **Skeniranje ovisnosti**: Procjena ranjivosti open-source ovisnosti i biblioteka
- **CodeQL analiza**: Statička analiza koda za sigurnosne ranjivosti i kodne probleme
- **Uvidi u opskrbni lanac**: Vidljivost u zdravlje ovisnosti i status sigurnosti

**Integracija Azure DevOps & Azure Repos:**
- Bešavna integracija sigurnosnog skeniranja kroz Microsoft razvojne platforme
- Automatizirane sigurnosne provjere u Azure pipeline-ima za AI radna opterećenja
- Provedba politika za sigurnu implementaciju AI komponenti

**Microsoft interne prakse:**
Microsoft provodi opsežne prakse sigurnosti opskrbnog lanca u svim proizvodima. Saznajte o dokazanim pristupima u [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Najbolje prakse osnovne sigurnosti

MCP implementacije nasljeđuju i nadograđuju postojeće sigurnosno stanje vaše organizacije. Jačanje osnovnih sigurnosnih praksi značajno povećava ukupnu sigurnost AI sustava i MCP implementacija.

### Osnovni sigurnosni temelji

#### **Sigurne razvojne prakse**
- **Usklađenost s OWASP-om**: Zaštita od [OWASP Top 10](https://owasp.org/www-project-top-ten/) ranjivosti web aplikacija
- **AI specifične zaštite**: Provesti kontrole za [OWASP Top 10 za LLM-ove](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Sigurno upravljanje tajnama**: Koristiti posvećene trezore za tokene, API ključeve i osjetljive konfiguracijske podatke
- **End-to-End šifriranje**: Implementirati sigurne komunikacije u svim komponentama aplikacije i tokovima podataka
- **Validacija unosa**: Stroga validacija svih korisničkih unosa, API parametara i izvora podataka

#### **Ojačavanje infrastrukture**
- **Višefaktorska autentikacija**: Obavezni MFA za sve administrativne i servisne račune
- **Upravljanje zakrpama**: Automatizirano, pravovremeno zakrpanje operativnih sustava, okvira i ovisnosti  
- **Integracija pružatelja identiteta**: Centralizirano upravljanje identitetima kroz enterprise identity providere (Microsoft Entra ID, Active Directory)
- **Segmentacija mreže**: Logička izolacija MCP komponenti radi ograničavanja potencijala lateralnog kretanja
- **Načelo najmanjeg privilegija**: Minimalne potrebne dozvole za sve komponente sustava i račune

#### **Praćenje i otkrivanje sigurnosti**
- **Sveobuhvatno zapisivanje**: Detaljno zapisivanje aktivnosti AI aplikacija, uključujući interakcije MCP klijent-poslužitelj
- **Integracija SIEM-a**: Centralizirano upravljanje sigurnosnim informacijama i događajima za otkrivanje anomalija
- **Behavioralna analitika**: AI-pokretani nadzor za otkrivanje neuobičajenih obrazaca u ponašanju sustava i korisnika
- **Obavještavanje o prijetnjama**: Integracija vanjskih izvora prijetnji i indikatora kompromisa (IOC)
- **Odgovor na incidente**: Dobro definirani postupci za otkrivanje, odgovor i oporavak od sigurnosnih incidenata

#### **Zero Trust arhitektura**
- **Nikad ne vjeruj, uvijek potvrdi**: Kontinuirana provjera korisnika, uređaja i mrežnih veza
- **Mikrosegmentacija**: Granularne mrežne kontrole koje izoliraju pojedinačna radna opterećenja i usluge
- **Sigurnost usmjerena na identitet**: Sigurnosne politike temeljene na verificiranim identitetima umjesto na mrežnoj lokaciji
- **Kontinuirana procjena rizika**: Dinamička procjena sigurnosnog stanja temeljena na trenutnom kontekstu i ponašanju
- **Uvjetni pristup**: Kontrole pristupa koje se prilagođavaju na temelju faktora rizika, lokacije i povjerenja uređaja

### Obrasci integracije u poduzeću

#### **Integracija Microsoft sigurnosnog ekosustava**
- **Microsoft Defender za Cloud**: Sveobuhvatno upravljanje sigurnosnim stanjem oblaka
- **Azure Sentinel**: Izvorni SIEM i SOAR u oblaku za zaštitu AI radnih opterećenja
- **Microsoft Entra ID**: Upravljanje identitetom i pristupom u poduzeću s uvjetnim pristupnim politikama
- **Azure Key Vault**: Centralizirano upravljanje tajnama uz podršku sigurnosnog hardverskog modula (HSM)
- **Microsoft Purview**: Upravljanje podacima i usklađenost za izvore podataka i tokove rada AI-ja

#### **Usklađenost i upravljanje**
- **Regulatorno usklađivanje**: Osigurati da MCP implementacije zadovoljavaju industrijske zahtjeve usklađenosti (GDPR, HIPAA, SOC 2)

- **Klasifikacija podataka**: Ispravna kategorizacija i rukovanje osjetljivim podacima obrađenim od strane AI sustava
- **Revizijske evidencije**: Sveobuhvatno bilježenje za usklađenost s propisima i forenzičku istragu
- **Kontrole privatnosti**: Implementacija načela privatnosti po dizajnu u arhitekturi AI sustava
- **Upravljanje promjenama**: Formalni procesi za sigurnosne preglede modifikacija AI sustava

Ove temeljne prakse stvaraju čvrstu sigurnosnu osnovu koja poboljšava učinkovitost sigurnosnih kontrola specifičnih za MCP i pruža sveobuhvatnu zaštitu AI-pokretanih aplikacija.

## Ključni sigurnosni zaključci

- **Slojeviti pristup sigurnosti**: Kombinirajte temeljne sigurnosne prakse (sigurno kodiranje, najmanje privilegije, provjera lanca opskrbe, kontinuirano nadgledanje) sa kontrolama specifičnim za AI za sveobuhvatnu zaštitu

- **Prijetnje specifične za AI**: MCP sustavi suočavaju se s jedinstvenim rizicima kao što su ubacivanje prompta, trovanje alata, preuzimanje sesija, problemi zbunjenog zamjenika, ranjivosti prosljeđivanja tokena i pretjerane dozvole koje zahtijevaju specijalizirane mjere ublažavanja

- **Izvrsnost u autentikaciji i autorizaciji**: Implementirajte robusnu autentikaciju koristeći vanjske pružatelje identiteta (Microsoft Entra ID), nametnite pravilnu validaciju tokena i nikada ne prihvaćajte tokene koji nisu eksplicitno izdani za vaš MCP poslužitelj

- **Prevencija AI napada**: Postavite Microsoft Prompt Shields i Azure Content Safety za obranu od neizravnog ubacivanja prompta i trovanja alata, dok istovremeno validirate metapodatke alata i pratite dinamičke promjene

- **Sigurnost sesija i prijenosa**: Koristite kriptografski sigurne, nedeterminističke ID-jeve sesija povezane s identitetom korisnika, implementirajte pravilno upravljanje životnim ciklusom sesije i nikada nemojte koristiti sesije za autentikaciju

- **Najbolje prakse sigurnosti OAuth**: Spriječite napade zbunjenog zamjenika kroz eksplicitan pristanak korisnika za dinamički registrirane klijente, pravilnu implementaciju OAuth 2.1 s PKCE i strogu validaciju URI-ja za preusmjeravanje  

- **Principi sigurnosti tokena**: Izbjegavajte anti-obrasce prosljeđivanja tokena, validirajte tvrdnje o publici tokena, implementirajte kratkotrajne tokene sa sigurnom rotacijom i održavajte jasne granice povjerenja

- **Sveobuhvatna sigurnost lanca opskrbe**: Postupajte sa svim komponentama AI ekosustava (modeli, ugradnje, davatelji konteksta, vanjski API-ji) s istim stupnjem sigurnosne rigoroznosti kao tradicionalne softverske ovisnosti

- **Kontinuirani razvoj**: Budite u tijeku s brzo razvijajućim specifikacijama MCP-a, doprinosite sigurnosnim zajedničkim standardima i održavajte prilagodljive sigurnosne posture kako se protokol razvija

- **Integracija sigurnosti Microsofta**: Iskoristite sveobuhvatan sigurnosni ekosustav Microsofta (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) za poboljšanu zaštitu MCP implementacija

## Sveobuhvatni resursi

### **Službena MCP sigurnosna dokumentacija**
- [MCP specifikacija (trenutno: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP sigurnosne najbolje prakse](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP specifikacija autorizacije](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub repozitorij](https://github.com/modelcontextprotocol)

### **OWASP MCP sigurnosni resursi**
- [OWASP MCP Azure sigurnosni vodič](https://microsoft.github.io/mcp-azure-security-guide/) - Sveobuhvatni OWASP MCP Top 10 s uputama za implementaciju u Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Službene OWASP MCP sigurnosne ranjivosti
- [MCP Security Summit radionica (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktična obuka iz sigurnosti za MCP na Azureu

### **Sigurnosni standardi i najbolje prakse**
- [OAuth 2.0 sigurnosne najbolje prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 sigurnost web aplikacija](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 za velike jezične modele](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Istraživanje i analiza sigurnosti AI**
- [Ubacivanje prompta u MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Napadi trovanjem alata (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP sigurnosno istraživanje (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft sigurnosna rješenja**
- [Microsoft Prompt Shields dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety usluga](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID sigurnost](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Najbolje prakse upravljanja tokenima u Azureu](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Vodiči za implementaciju i tutorijali**
- [Azure API Management kao MCP autentikacijski gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID autentikacija s MCP poslužiteljima](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Sigurno pohranjivanje i enkripcija tokena (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps i sigurnost lanca opskrbe**
- [Azure DevOps sigurnost](https://azure.microsoft.com/products/devops)
- [Azure Repos sigurnost](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft put sigurnosti lanca opskrbe](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dodatna sigurnosna dokumentacija**

Za sveobuhvatne sigurnosne smjernice, pogledajte ove specijalizirane dokumente u ovom odjeljku:

- **[CIMD i DCR uzorak autorizacije](./samples/cimd-dcr-auth/README.md)** - Izvedivi TypeScript MCP `2026-07-28` resursni poslužitelj koji uspoređuje preferirane dokumente meta-podataka klijenata s zastarjelim mehanizmom dinamičke registracije klijenta kao rezervom
- **[MCP sigurnosne najbolje prakse](./mcp-security-best-practices.md)** - Potpune sigurnosne najbolje prakse za MCP implementacije
- **[Implementacija Azure Content Safety](./azure-content-safety-implementation.md)** - Praktični primjeri implementacije za integraciju Azure Content Safety  
- **[MCP sigurnosne kontrole](./mcp-security-controls.md)** - Najnovije sigurnosne kontrole i tehnike za MCP implementacije
- **[MCP brzi vodič najboljih praksi](./mcp-best-practices.md)** - Brzi referentni vodič za ključne MCP sigurnosne prakse
- **[BlueHat 2026: Osiguravanje budućnosti AI: Sigurnost MCP-a uz obranu u dubinu](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Obrasci obrane u dubinu iz Microsoft Security Response Centera (MSRC)

### **Praktična sigurnosna obuka**

- **[MCP Security Summit radionica (Sherpa)](https://azure-samples.github.io/sherpa/)** - Sveobuhvatna praktična radionica za osiguravanje MCP poslužitelja u Azureu s progresivnim kampovima od Base Camp do Summita
- **[OWASP MCP Azure sigurnosni vodič](https://microsoft.github.io/mcp-azure-security-guide/)** - Referentna arhitektura i upute za implementaciju za sve OWASP MCP Top 10 rizike

---

## Što slijedi

Sljedeće: [Poglavlje 3: Početak](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->