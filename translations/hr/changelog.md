# Dnevnik promjena: MCP za početnike kurikulum

Ovaj dokument služi kao zapis svih značajnih promjena napravljenih u Model Context Protocol (MCP) za početnike kurikulumu. Promjene su dokumentirane u obrnutom kronološkom redoslijedu (najnovije promjene prve).

## 18. prosinca 2025.

### Ažuriranje sigurnosne dokumentacije - MCP specifikacija 2025-11-25

#### Najbolje sigurnosne prakse MCP-a (02-Security/mcp-best-practices.md) - Ažuriranje verzije specifikacije
- **Ažuriranje verzije protokola**: Ažurirano na najnoviju MCP specifikaciju 2025-11-25 (objavljeno 25. studenog 2025.)
  - Ažurirani svi referentni brojevi verzija specifikacije s 2025-06-18 na 2025-11-25
  - Ažurirani datumski referenti u dokumentu s 18. kolovoza 2025. na 18. prosinca 2025.
  - Provjereno da svi URL-ovi specifikacije upućuju na trenutnu dokumentaciju
- **Validacija sadržaja**: Sveobuhvatna validacija sigurnosnih najboljih praksi prema najnovijim standardima
  - **Microsoft sigurnosna rješenja**: Provjereni aktualni termini i poveznice za Prompt Shields (ranije "detekcija rizika jailbreaka"), Azure Content Safety, Microsoft Entra ID i Azure Key Vault
  - **OAuth 2.1 sigurnost**: Potvrđena usklađenost s najnovijim sigurnosnim najboljim praksama OAuth-a
  - **OWASP standardi**: Validirani OWASP Top 10 za LLM-ove ostaju aktualni
  - **Azure usluge**: Provjereni svi Microsoft Azure dokumentacijski linkovi i najbolje prakse
- **Usklađenost sa standardima**: Sve referentne sigurnosne norme potvrđene kao aktualne
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 sigurnosne najbolje prakse
  - Azure sigurnosni i usklađenostni okviri
- **Resursi za implementaciju**: Validirani svi linkovi i resursi za vodiče implementacije
  - Azure API Management obrasci autentikacije
  - Microsoft Entra ID integracijski vodiči
  - Upravljanje tajnama u Azure Key Vaultu
  - DevSecOps pipeline-i i rješenja za nadzor

### Osiguranje kvalitete dokumentacije
- **Usklađenost sa specifikacijom**: Osigurano da svi obavezni MCP sigurnosni zahtjevi (MORA/MORA NE) budu usklađeni s najnovijom specifikacijom
- **Aktualnost resursa**: Provjereni svi vanjski linkovi na Microsoft dokumentaciju, sigurnosne standarde i vodiče za implementaciju
- **Pokriće najboljih praksi**: Potvrđeno sveobuhvatno pokriće autentikacije, autorizacije, prijetnji specifičnih za AI, sigurnosti lanca opskrbe i enterprise obrazaca

## 6. listopada 2025.

### Proširenje odjeljka Početak rada – Napredna upotreba servera i jednostavna autentikacija

#### Napredna upotreba servera (03-GettingStarted/10-advanced)
- **Dodano novo poglavlje**: Uveden sveobuhvatan vodič za naprednu upotrebu MCP servera, pokrivajući redovnu i niskorazinsku arhitekturu servera.
  - **Redovni vs. niskorazinski server**: Detaljna usporedba i primjeri koda u Pythonu i TypeScriptu za oba pristupa.
  - **Dizajn temeljen na handlerima**: Objašnjenje upravljanja alatima/resursima/promptima putem handlera za skalabilne i fleksibilne implementacije servera.
  - **Praktični obrasci**: Stvarni scenariji gdje su niskorazinski obrasci servera korisni za napredne značajke i arhitekturu.

#### Jednostavna autentikacija (03-GettingStarted/11-simple-auth)
- **Dodano novo poglavlje**: Korak-po-korak vodič za implementaciju jednostavne autentikacije u MCP serverima.
  - **Koncepti autentikacije**: Jasno objašnjenje razlike između autentikacije i autorizacije te rukovanja vjerodajnicama.
  - **Implementacija osnovne autentikacije**: Obrasci autentikacije temeljeni na middleware-u u Pythonu (Starlette) i TypeScriptu (Express), s primjerima koda.
  - **Napredak prema naprednoj sigurnosti**: Smjernice za početak s jednostavnom autentikacijom i napredovanje prema OAuth 2.1 i RBAC-u, s referencama na napredne sigurnosne module.

Ova proširenja pružaju praktične, hands-on smjernice za izgradnju robusnijih, sigurnijih i fleksibilnijih MCP server implementacija, povezujući temeljne koncepte s naprednim proizvodnim obrascima.

## 29. rujna 2025.

### MCP Server integracija baze podataka laboratoriji - Sveobuhvatan praktični put učenja

#### 11-MCPServerHandsOnLabs - Novi kompletan kurikulum integracije baze podataka
- **Potpuni put učenja od 13 laboratorija**: Dodan sveobuhvatan praktični kurikulum za izgradnju MCP servera spremnih za produkciju s integracijom PostgreSQL baze podataka
  - **Primjer iz stvarnog svijeta**: Zava Retail analitika kao primjer enterprise obrazaca
  - **Strukturirani napredak u učenju**:
    - **Laboratoriji 00-03: Osnove** - Uvod, osnovna arhitektura, sigurnost i multi-tenancy, postavljanje okruženja
    - **Laboratoriji 04-06: Izgradnja MCP servera** - Dizajn baze podataka i shema, implementacija MCP servera, razvoj alata
    - **Laboratoriji 07-09: Napredne značajke** - Integracija semantičkog pretraživanja, testiranje i otklanjanje pogrešaka, integracija s VS Code-om
    - **Laboratoriji 10-12: Produkcija i najbolje prakse** - Strategije implementacije, nadzor i promatranje, najbolje prakse i optimizacija
  - **Enterprise tehnologije**: FastMCP framework, PostgreSQL s pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Napredne značajke**: Row Level Security (RLS), semantičko pretraživanje, višekorisnički pristup podacima, vektorski embeddings, nadzor u stvarnom vremenu

#### Standardizacija terminologije - Pretvorba modula u laboratorije
- **Sveobuhvatno ažuriranje dokumentacije**: Sustavno ažurirani svi README fajlovi u 11-MCPServerHandsOnLabs da koriste termin "Laboratorij" umjesto "Modul"
  - **Naslovi odjeljaka**: Ažurirano "Što ovaj modul pokriva" u "Što ovaj laboratorij pokriva" u svih 13 laboratorija
  - **Opis sadržaja**: Promijenjeno "Ovaj modul pruža..." u "Ovaj laboratorij pruža..." kroz cijelu dokumentaciju
  - **Ciljevi učenja**: Ažurirano "Na kraju ovog modula..." u "Na kraju ovog laboratorija..."
  - **Navigacijski linkovi**: Pretvoreni svi referenti "Modul XX:" u "Laboratorij XX:" u međureferencama i navigaciji
  - **Praćenje završetka**: Ažurirano "Nakon završetka ovog modula..." u "Nakon završetka ovog laboratorija..."
  - **Sačuvane tehničke reference**: Očuvane Python module reference u konfiguracijskim datotekama (npr. `"module": "mcp_server.main"`)

#### Poboljšanje vodiča za učenje (study_guide.md)
- **Vizualna karta kurikuluma**: Dodan novi odjeljak "11. Laboratoriji integracije baze podataka" sa sveobuhvatnom vizualizacijom strukture laboratorija
- **Struktura repozitorija**: Ažurirano s deset na jedanaest glavnih odjeljaka s detaljnim opisom 11-MCPServerHandsOnLabs
- **Smjernice za put učenja**: Poboljšane upute za navigaciju koje pokrivaju odjeljke 00-11
- **Pokriće tehnologija**: Dodani detalji o integraciji FastMCP, PostgreSQL i Azure usluga
- **Ishodi učenja**: Naglašena izrada servera spremnih za produkciju, obrasci integracije baze podataka i enterprise sigurnost

#### Poboljšanje strukture glavnog README-a
- **Terminologija temeljena na laboratorijima**: Ažuriran glavni README.md u 11-MCPServerHandsOnLabs za dosljednu upotrebu strukture "Laboratorij"
- **Organizacija puta učenja**: Jasna progresija od temeljnih koncepata preko napredne implementacije do produkcijske implementacije
- **Fokus na stvarni svijet**: Naglasak na praktično, hands-on učenje s enterprise obrascima i tehnologijama

### Poboljšanja kvalitete i dosljednosti dokumentacije
- **Naglasak na praktično učenje**: Ojačan praktični, laboratorijski pristup kroz cijelu dokumentaciju
- **Fokus na enterprise obrasce**: Istaknute produkcijski spremne implementacije i razmatranja enterprise sigurnosti
- **Integracija tehnologija**: Sveobuhvatno pokriće modernih Azure usluga i AI integracijskih obrazaca
- **Napredak u učenju**: Jasan, strukturirani put od osnovnih koncepata do produkcijske implementacije

## 26. rujna 2025.

### Poboljšanje studija slučaja - Integracija GitHub MCP registra

#### Studije slučaja (09-CaseStudy/) - Fokus na razvoj ekosustava
- **README.md**: Veliko proširenje s opsežnim studijom slučaja GitHub MCP registra
  - **Studija slučaja GitHub MCP registra**: Nova opsežna studija slučaja koja analizira lansiranje GitHub MCP registra u rujnu 2025.
    - **Analiza problema**: Detaljna analiza fragmentiranog otkrivanja i implementacije MCP servera
    - **Arhitektura rješenja**: GitHubov pristup centraliziranom registru s instalacijom jednim klikom u VS Code
    - **Poslovni utjecaj**: Mjerljiva poboljšanja u onboardingu i produktivnosti developera
    - **Strateška vrijednost**: Fokus na modularnu implementaciju agenata i interoperabilnost među alatima
    - **Razvoj ekosustava**: Pozicioniranje kao temeljna platforma za agentnu integraciju
  - **Poboljšana struktura studija slučaja**: Ažurirane sve sedam studija slučaja s dosljednim formatiranjem i sveobuhvatnim opisima
    - Azure AI Travel Agents: Naglasak na orkestraciju više agenata
    - Azure DevOps integracija: Fokus na automatizaciju tijeka rada
    - Dohvat dokumentacije u stvarnom vremenu: Implementacija Python konzolnog klijenta
    - Interaktivni generator plana učenja: Chainlit konverzacijska web aplikacija
    - Dokumentacija u editoru: Integracija VS Code i GitHub Copilot
    - Azure API Management: Enterprise obrasci integracije API-ja
    - GitHub MCP Registry: Razvoj ekosustava i platforma zajednice
  - **Sveobuhvatan zaključak**: Prepisan zaključni odjeljak koji ističe sedam studija slučaja koje pokrivaju različite dimenzije MCP implementacije
    - Enterprise integracija, orkestracija više agenata, produktivnost developera
    - Razvoj ekosustava, obrazovne primjene
    - Poboljšani uvidi u arhitektonske obrasce, strategije implementacije i najbolje prakse
    - Naglasak na MCP kao zreli, produkcijski spremni protokol

#### Ažuriranja vodiča za učenje (study_guide.md)
- **Vizualna karta kurikuluma**: Ažurirana mentalna mapa da uključi GitHub MCP Registry u odjeljak Studije slučaja
- **Opis studija slučaja**: Proširen s generičkih opisa na detaljnu razradu sedam opsežnih studija slučaja
- **Struktura repozitorija**: Ažuriran odjeljak 10 da odražava sveobuhvatno pokriće studija slučaja s konkretnim detaljima implementacije
- **Integracija dnevnika promjena**: Dodan unos za 26. rujna 2025. koji dokumentira dodavanje GitHub MCP registra i poboljšanja studija slučaja
- **Ažuriranje datuma**: Ažuriran vremenski žig u podnožju da odražava najnoviju reviziju (26. rujna 2025.)

### Poboljšanja kvalitete dokumentacije
- **Poboljšanje dosljednosti**: Standardizirano formatiranje i struktura studija slučaja u svih sedam primjera
- **Sveobuhvatno pokriće**: Studije slučaja sada pokrivaju enterprise, produktivnost developera i scenarije razvoja ekosustava
- **Strateško pozicioniranje**: Pojačan fokus na MCP kao temeljnu platformu za implementaciju agentnih sustava
- **Integracija resursa**: Ažurirani dodatni resursi da uključe link na GitHub MCP Registry

## 15. rujna 2025.

### Proširenje naprednih tema - Prilagođeni transporti i inženjering konteksta

#### Prilagođeni MCP transporti (05-AdvancedTopics/mcp-transport/) - Novi vodič za naprednu implementaciju
- **README.md**: Potpuni vodič za implementaciju prilagođenih MCP transportnih mehanizama
  - **Azure Event Grid transport**: Sveobuhvatna implementacija serverless event-driven transporta
    - Primjeri u C#, TypeScriptu i Pythonu s integracijom Azure Functions
    - Obrasci event-driven arhitekture za skalabilna MCP rješenja
    - Primatelji webhookova i push-based rukovanje porukama
  - **Azure Event Hubs transport**: Implementacija transporta visokog protoka streaminga
    - Mogućnosti streaminga u stvarnom vremenu za scenarije niske latencije
    - Strategije particioniranja i upravljanje checkpointovima
    - Grupiranje poruka i optimizacija performansi
  - **Enterprise obrasci integracije**: Produkcijski spremni arhitektonski primjeri
    - Distribuirana MCP obrada preko više Azure Functions
    - Hibridne transportne arhitekture koje kombiniraju više tipova transporta
    - Strategije trajnosti poruka, pouzdanosti i upravljanja pogreškama
  - **Sigurnost i nadzor**: Integracija Azure Key Vaulta i obrasci promatranja
    - Autentikacija upravljanim identitetom i pristup s najmanjim privilegijama
    - Telemetrija Application Insights i nadzor performansi
    - Circuit breaker-i i obrasci otpornosti na pogreške
  - **Okviri za testiranje**: Sveobuhvatne strategije testiranja prilagođenih transporta
    - Jedinično testiranje s test dablovima i mocking framework-ima
    - Integracijsko testiranje s Azure Test Containers
    - Razmatranja performansi i testiranja opterećenja

#### Inženjering konteksta (05-AdvancedTopics/mcp-contextengineering/) - Nova AI disciplina
- **README.md**: Sveobuhvatno istraživanje inženjeringa konteksta kao rastućeg područja
  - **Temeljna načela**: Potpuno dijeljenje konteksta, svijest o donošenju odluka i upravljanje kontekstnim prozorom
  - **Usklađenost s MCP protokolom**: Kako dizajn MCP-a rješava izazove inženjeringa konteksta
    - Ograničenja kontekstnog prozora i strategije progresivnog učitavanja
    - Određivanje relevantnosti i dinamičko dohvaćanje konteksta
    - Rukovanje multimodalnim kontekstom i sigurnosna razmatranja
  - **Pristupi implementaciji**: Jednothread vs. višestruki agenti
    - Tehnike segmentacije i prioritizacije konteksta
    - Progresivno učitavanje i strategije kompresije konteksta
    - Slojeviti pristupi kontekstu i optimizacija dohvaćanja
  - **Okvir za mjerenje**: Novi metrički sustavi za evaluaciju učinkovitosti konteksta
    - Učinkovitost unosa, performanse, kvaliteta i korisničko iskustvo
    - Eksperimentalni pristupi optimizaciji konteksta
    - Analiza neuspjeha i metodologije poboljšanja

#### Ažuriranja navigacije kurikulumom (README.md)
- **Proširena struktura modula**: Ažurirana tablica kurikuluma da uključi nove napredne teme
  - Dodani unosi Inženjering konteksta (5.14) i Prilagođeni transport (5.15)
  - Dosljedno formatiranje i navigacijski linkovi kroz sve module
  - Ažurirani opisi da odražavaju trenutačni opseg sadržaja

### Poboljšanja strukture direktorija
- **Standardizacija naziva**: Preimenovan "mcp transport" u "mcp-transport" radi dosljednosti s ostalim mapama naprednih tema
- **Organizacija sadržaja**: Sve mape 05-AdvancedTopics sada slijede dosljedan obrazac naziva (mcp-[tema])

### Poboljšanja kvalitete dokumentacije
- **Usklađenost s MCP specifikacijom**: Sav novi sadržaj referira trenutnu MCP specifikaciju 2025-06-18
- **Primjeri na više jezika**: Sveobuhvatni primjeri koda u C#, TypeScriptu i Pythonu
- **Enterprise fokus**: Produkcijski spremni obrasci i integracija Azure clouda kroz cijeli sadržaj
- **Vizualna dokumentacija**: Mermaid dijagrami za arhitekturu i vizualizaciju toka

## 18. kolovoza 2025.

### Sveobuhvatno ažuriranje dokumentacije - MCP standardi 2025-06-18

#### Najbolje sigurnosne prakse MCP-a (02-Security/) - Potpuna modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Potpuni prepis usklađen s MCP specifikacijom 2025-06-18
  - **Obavezni Zahtjevi**: Dodani eksplicitni ZAHTJEVA/NE ZAHTJEVA iz službene specifikacije s jasnim vizualnim indikatorima
  - **12 Temeljnih Sigurnosnih Praksi**: Prestrukturirano s liste od 15 stavki u sveobuhvatne sigurnosne domene
    - Sigurnost tokena i autentikacija s integracijom vanjskog pružatelja identiteta
    - Upravljanje sesijama i sigurnost prijenosa s kriptografskim zahtjevima
    - Zaštita specifična za AI s integracijom Microsoft Prompt Shields
    - Kontrola pristupa i dozvole s principom najmanjih privilegija
    - Sigurnost sadržaja i nadzor s integracijom Azure Content Safety
    - Sigurnost lanca opskrbe s opsežnom verifikacijom komponenti
    - Sigurnost OAuth-a i sprječavanje Confused Deputy napada s implementacijom PKCE
    - Odgovor na incidente i oporavak s automatiziranim mogućnostima
    - Usklađenost i upravljanje s regulatornim usklađivanjem
    - Napredne sigurnosne kontrole s arhitekturom nulte povjerenja
    - Integracija Microsoft sigurnosnog ekosustava s opsežnim rješenjima
    - Kontinuirani razvoj sigurnosti s adaptivnim praksama
  - **Microsoft Sigurnosna Rješenja**: Poboljšane smjernice za integraciju Prompt Shields, Azure Content Safety, Entra ID i GitHub Advanced Security
  - **Resursi za Implementaciju**: Kategorizirani opsežni linkovi resursa po službenoj MCP dokumentaciji, Microsoft sigurnosnim rješenjima, sigurnosnim standardima i vodičima za implementaciju

#### Napredne Sigurnosne Kontrole (02-Security/) - Implementacija za Poduzeća
- **MCP-SECURITY-CONTROLS-2025.md**: Potpuna prerada s sigurnosnim okvirom razine poduzeća
  - **9 Sveobuhvatnih Sigurnosnih Domena**: Prošireno s osnovnih kontrola na detaljni okvir za poduzeća
    - Napredna autentikacija i autorizacija s integracijom Microsoft Entra ID
    - Sigurnost tokena i kontrole protiv prosljeđivanja s opsežnom validacijom
    - Sigurnosne kontrole sesija s prevencijom otmice
    - Sigurnosne kontrole specifične za AI s prevencijom ubrizgavanja prompta i trovanja alata
    - Prevencija Confused Deputy napada s OAuth proxy sigurnošću
    - Sigurnost izvršavanja alata s sandboxingom i izolacijom
    - Sigurnosne kontrole lanca opskrbe s verifikacijom ovisnosti
    - Kontrole nadzora i detekcije s integracijom SIEM-a
    - Odgovor na incidente i oporavak s automatiziranim mogućnostima
  - **Primjeri Implementacije**: Dodani detaljni YAML konfiguracijski blokovi i primjeri koda
  - **Integracija Microsoft Rješenja**: Sveobuhvatno pokrivanje Azure sigurnosnih usluga, GitHub Advanced Security i upravljanja identitetom za poduzeća

#### Napredne Sigurnosne Teme (05-AdvancedTopics/mcp-security/) - Implementacija Spremna za Proizvodnju
- **README.md**: Potpuna prerada za implementaciju sigurnosti u poduzećima
  - **Usklađenost s Trenutnom Specifikacijom**: Ažurirano na MCP Specifikaciju 2025-06-18 s obaveznim sigurnosnim zahtjevima
  - **Poboljšana Autentikacija**: Integracija Microsoft Entra ID s opsežnim primjerima u .NET i Java Spring Security
  - **Integracija AI Sigurnosti**: Implementacija Microsoft Prompt Shields i Azure Content Safety s detaljnim Python primjerima
  - **Napredna Ublažavanja Prijetnji**: Sveobuhvatni primjeri implementacije za
    - Prevenciju Confused Deputy napada s PKCE i validacijom korisničkog pristanka
    - Prevenciju prosljeđivanja tokena s validacijom publike i sigurnim upravljanjem tokenima
    - Prevenciju otmice sesije s kriptografskim povezivanjem i analizom ponašanja
  - **Integracija Sigurnosti u Poduzeću**: Nadzor Azure Application Insights, pipelineovi za detekciju prijetnji i sigurnost lanca opskrbe
  - **Kontrolni Popis Implementacije**: Jasne obavezne naspram preporučenih sigurnosnih kontrola s prednostima Microsoft sigurnosnog ekosustava

### Kvaliteta Dokumentacije i Usklađenost sa Standardima
- **Reference Specifikacije**: Ažurirane sve reference na trenutnu MCP Specifikaciju 2025-06-18
- **Microsoft Sigurnosni Ekosustav**: Poboljšane smjernice za integraciju kroz svu sigurnosnu dokumentaciju
- **Praktična Implementacija**: Dodani detaljni primjeri koda u .NET, Java i Python s obrascima za poduzeća
- **Organizacija Resursa**: Sveobuhvatna kategorizacija službene dokumentacije, sigurnosnih standarda i vodiča za implementaciju
- **Vizualni Indikatori**: Jasno označavanje obaveznih zahtjeva naspram preporučenih praksi


#### Temeljni Koncepti (01-CoreConcepts/) - Potpuna Modernizacija
- **Ažuriranje Verzije Protokola**: Ažurirano za referencu na trenutnu MCP Specifikaciju 2025-06-18 s verzioniranjem po datumu (format GGGG-MM-DD)
- **Dorada Arhitekture**: Poboljšani opisi Hostova, Klijenata i Servera za odražavanje trenutnih MCP arhitektonskih obrazaca
  - Hostovi sada jasno definirani kao AI aplikacije koje koordiniraju više MCP klijentskih veza
  - Klijenti opisani kao protokolarni konektori koji održavaju odnos jedan-na-jedan sa serverom
  - Serveri poboljšani s lokalnim i udaljenim scenarijima implementacije
- **Prestrukturiranje Primitiva**: Potpuna prerada server i klijentskih primitiva
  - Server Primitivi: Resursi (izvori podataka), Prompts (predlošci), Alati (izvršne funkcije) s detaljnim objašnjenjima i primjerima
  - Klijent Primitivi: Uzorkovanje (LLM dovršetci), Elicitation (korisnički unos), Logiranje (debugging/nadzor)
  - Ažurirano s trenutnim obrascima metoda za otkrivanje (`*/list`), dohvat (`*/get`) i izvršavanje (`*/call`)
- **Arhitektura Protokola**: Uveden model arhitekture s dva sloja
  - Sloj podataka: Temelj JSON-RPC 2.0 s upravljanjem životnim ciklusom i primitivima
  - Transportni sloj: STDIO (lokalni) i Streamable HTTP s SSE (udaljeni) transportni mehanizmi
- **Sigurnosni Okvir**: Sveobuhvatni sigurnosni principi uključujući eksplicitan korisnički pristanak, zaštitu privatnosti podataka, sigurnost izvršavanja alata i sigurnost transportnog sloja
- **Obrasci Komunikacije**: Ažurirane protokolarne poruke za prikaz inicijalizacije, otkrivanja, izvršavanja i tokova obavijesti
- **Primjeri Koda**: Osvježeni primjeri u više jezika (.NET, Java, Python, JavaScript) za odražavanje trenutnih MCP SDK obrazaca

#### Sigurnost (02-Security/) - Sveobuhvatna Sigurnosna Prerada  
- **Usklađenost sa Standardima**: Potpuna usklađenost sa sigurnosnim zahtjevima MCP Specifikacije 2025-06-18
- **Evolucija Autentikacije**: Dokumentirana evolucija od prilagođenih OAuth servera do delegacije vanjskog pružatelja identiteta (Microsoft Entra ID)
- **Analiza Prijetnji Specifičnih za AI**: Poboljšano pokrivanje modernih AI vektora napada
  - Detaljni scenariji napada ubrizgavanjem prompta s primjerima iz stvarnog svijeta
  - Mehanizmi trovanja alata i obrasci napada "rug pull"
  - Trovanje kontekstnog prozora i napadi zbunjivanja modela
- **Microsoft AI Sigurnosna Rješenja**: Sveobuhvatno pokrivanje Microsoft sigurnosnog ekosustava
  - AI Prompt Shields s naprednom detekcijom, isticanjem i tehnikama razdjelnika
  - Obrasci integracije Azure Content Safety
  - GitHub Advanced Security za zaštitu lanca opskrbe
- **Napredna Ublažavanja Prijetnji**: Detaljne sigurnosne kontrole za
  - Otmicu sesije s MCP-specifičnim scenarijima napada i kriptografskim zahtjevima za ID sesije
  - Problemi Confused Deputy u MCP proxy scenarijima s eksplicitnim zahtjevima za pristanak
  - Ranljivosti prosljeđivanja tokena s obaveznim kontrolama validacije
- **Sigurnost Lanca Opskrbe**: Prošireno pokrivanje AI lanca opskrbe uključujući temeljne modele, usluge ugradnje, pružatelje konteksta i API-je trećih strana
- **Sigurnost Temelja**: Poboljšana integracija s obrascima sigurnosti za poduzeća uključujući arhitekturu nulte povjerenja i Microsoft sigurnosni ekosustav
- **Organizacija Resursa**: Kategorizirani opsežni linkovi resursa po tipu (Službena Dokumentacija, Standardi, Istraživanja, Microsoft Rješenja, Vodiči za Implementaciju)

### Poboljšanja Kvalitete Dokumentacije
- **Strukturirani Ciljevi Učenja**: Poboljšani ciljevi učenja sa specifičnim, izvedivim ishodima
- **Međureferenciranje**: Dodani linkovi između povezanih sigurnosnih i temeljnih koncepata
- **Ažurirane Informacije**: Ažurirani svi datumski i specifikacijski linkovi na trenutne standarde
- **Smjernice za Implementaciju**: Dodane specifične, izvedive smjernice za implementaciju kroz oba dijela

## 16. srpnja 2025.

### README i Poboljšanja Navigacije
- Potpuno redizajnirana navigacija kurikuluma u README.md
- Zamijenjeni `<details>` tagovi pristupačnijim formatom temeljenim na tablicama
- Kreirane alternativne opcije izgleda u novom folderu "alternative_layouts"
- Dodani primjeri navigacije u obliku kartica, tabova i akordeona
- Ažuriran odjeljak strukture repozitorija da uključi sve najnovije datoteke
- Poboljšan odjeljak "Kako koristiti ovaj kurikulum" s jasnim preporukama
- Ažurirani MCP specifikacijski linkovi da upućuju na ispravne URL-ove
- Dodan odjeljak Context Engineering (5.14) u strukturu kurikuluma

### Ažuriranja Studijskog Vodiča
- Potpuno revidiran studijski vodič za usklađenost s trenutnom strukturom repozitorija
- Dodani novi odjeljci za MCP klijente i alate, te popularne MCP servere
- Ažurirana Vizualna Mapa Kurikuluma za točno prikazivanje svih tema
- Poboljšani opisi Naprednih Tema za pokrivanje svih specijaliziranih područja
- Ažuriran odjeljak Studije Slučaja za prikaz stvarnih primjera
- Dodan ovaj sveobuhvatni dnevnik promjena

### Doprinosi Zajednice (06-CommunityContributions/)
- Dodane detaljne informacije o MCP serverima za generiranje slika
- Dodan opsežan odjeljak o korištenju Claude u VSCode-u
- Dodane upute za postavljanje i korištenje Cline terminalnog klijenta
- Ažuriran odjeljak MCP klijenata da uključi sve popularne opcije klijenata
- Poboljšani primjeri doprinosa s točnijim uzorcima koda

### Napredne Teme (05-AdvancedTopics/)
- Organizirani svi specijalizirani folderi s dosljednim imenovanjem
- Dodani materijali i primjeri za context engineering
- Dodana dokumentacija za integraciju Foundry agenta
- Poboljšana dokumentacija integracije sigurnosti Entra ID

## 11. lipnja 2025.

### Početno Kreiranje
- Objavljena prva verzija MCP za Početnike kurikuluma
- Kreirana osnovna struktura za svih 10 glavnih sekcija
- Implementirana Vizualna Mapa Kurikuluma za navigaciju
- Dodani početni uzorci projekata u više programskih jezika

### Početak Rada (03-GettingStarted/)
- Kreirani prvi primjeri implementacije servera
- Dodane smjernice za razvoj klijenata
- Uključene upute za integraciju LLM klijenta
- Dodana dokumentacija za integraciju u VS Code
- Implementirani primjeri servera s Server-Sent Events (SSE)

### Temeljni Koncepti (01-CoreConcepts/)
- Dodano detaljno objašnjenje klijent-server arhitekture
- Kreirana dokumentacija o ključnim protokolnim komponentama
- Dokumentirani obrasci poruka u MCP

## 23. svibnja 2025.

### Struktura Repozitorija
- Inicijaliziran repozitorij s osnovnom strukturom foldera
- Kreirani README fajlovi za svaku glavnu sekciju
- Postavljena infrastruktura za prijevod
- Dodani slikovni materijali i dijagrami

### Dokumentacija
- Kreiran početni README.md s pregledom kurikuluma
- Dodani CODE_OF_CONDUCT.md i SECURITY.md
- Postavljen SUPPORT.md s uputama za dobivanje pomoći
- Kreirana preliminarna struktura studijskog vodiča

## 15. travnja 2025.

### Planiranje i Okvir
- Početno planiranje MCP za Početnike kurikuluma
- Definirani ciljevi učenja i ciljana publika
- Nacrtana struktura kurikuluma s 10 sekcija
- Razvijen konceptualni okvir za primjere i studije slučaja
- Kreirani početni prototipni primjeri za ključne koncepte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->