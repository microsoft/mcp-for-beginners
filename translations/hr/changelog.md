# Changelog: MCP za početnike kurikulum

Ovaj dokument služi kao zapis svih značajnih promjena napravljenih u Model Context Protocol (MCP) za početnike kurikulumu. Promjene su zabilježene u obrnutom kronološkom redoslijedu (najnovije promjene prve).

## 11. travnja 2026.

### Nova lekcija, popravci dokumentacije i ažuriranja ovisnosti

#### Dodan novi sadržaj kurikuluma

**Modul 05 - Napredne teme**
- **Lekcija 5.17: Adversarialno višagentno rezoniranje s MCP-om** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Novi sveobuhvatni vodič koji pokriva obrazac suprotstavljenih debata za višagentske sustave
  - Mermaid dijagram arhitekture: dva agenta → zajednički MCP poslužitelj → transkript debate → sudac → presuda
  - Zajednički MCP alat poslužitelj (`web_search` + `run_python`) implementiran u Pythonu i TypeScriptu
  - Suprotstavljeni sustavni promptovi (ZA / PROTIV / Sudac) s eksplicitnim zahtjevima za korištenje alata
  - Orkestrator debate u Pythonu, TypeScriptu i C# koji upravlja rundama i usmjeravanjem argumenata
  - MCP `ClientSession` povezivanje za orkestrator prema stvarnim pozivima alata
  - Tablica primjera upotrebe (detekcija halucinacija, modeliranje prijetnji, pregled dizajna API-ja, provjera činjenica, odabir tehnologije)
  - Sigurnosni aspekti: izvođenje u sandboxu, validacija poziva alata, ograničenje brzine, bilježenje revizije
  - Strukturirana vježba s tri praktična scenarija (pregled koda, odluka o arhitekturi, moderacija sadržaja)

#### Popravci dokumentacije

**Modul 03 - Uvod**
- **05-stdio-server/README.md**: Ispravljen nepotpuni primjer TypeScript stdio servera — dodana nedostajuća inicijalizacija transporta (`new StdioServerTransport()`) i poziv `server.connect(transport)` u skladu s Python i .NET primjerima u istom odjeljku
- **14-sampling/README.md**: Ispravka tipfelera — ispravljeno `"Sampling is an davanced features"` u `"Sampling is an advanced feature"`

#### Ažuriranja kurikuluma

**Glavni README.md**
- Dodana stavka 5.17 (Adversarialno višagentno rezoniranje s MCP-om) u tablicu kurikuluma s direktnom poveznicom na novu lekciju

**05-AdvancedTopics/README.md**
- Dodan redak Lekcije 5.17 u tablicu lekcija

**study_guide.md**
- Dodana tema Adversarialnog višagentnog rezoniranja u mentalnu mapu i opis u poglavlju Napredne teme

#### Popravci koda i sigurnosti

**Modul 05 - Adversarialni agenti (`mcp-adversarial-agents`)**
- **Popravak sigurnosti — injekcija naredbi**: Zamijenjen `execSync` shell interpolacija s `execFile` + `promisify` u TypeScript alatu `run_python`, uklonivši površinu za injekciju naredbi (LLM kontrolirani kod sada se prosljeđuje kao literalni argv element bez uključenja shell-a)
- **Povezivanje MCP petlje za alat**: Ažuriran Python orkestrator debate da koristi `AsyncAnthropic` klijent (zamjena za blokirajući sinkroni `Anthropic`), prosljeđuje live `ClientSession` izravno svakom agentu u rundi, dohvaća definicije alata preko `session.list_tools()` pri svakom okretu i šalje `tool_use` blokove preko `session.call_tool()` u petlji dok model ne emitira konačni tekstualni odgovor

#### Ažuriranja ovisnosti

- Nadograđen `hono` na 4.12.12 u više paketa (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Nadograđen `@hono/node-server` s 1.19.11 na 1.19.13 u TypeScript paketima
- Nadograđen `cryptography` s 46.0.5 na 46.0.7 u Python paketima (labovi 3 i 4 u 10-StreamliningAIWorkflows)
- Nadograđen `lodash` s 4.17.23 na 4.18.1 u inspektoru 10-StreamliningAIWorkflows

#### Prijevodi

- Sinkronizirani prijevodi za 48+ jezika s najnovijim izvorima (ažuriranje i18n)

---

## 5. veljače 2026.

### Univerzalna provjera i poboljšanja navigacije u repozitoriju

#### Dodan novi sadržaj kurikuluma

**Modul 03 - Uvod**
- **12-mcp-hosts/README.md**: Novi sveobuhvatan vodič za postavljanje MCP hostova
  - Primjeri konfiguracije Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON predlošci konfiguracije za sve glavne hostove
  - Tablica usporedbe tipova transporta (stdio, SSE/HTTP, WebSocket)
  - Rješavanje uobičajenih problema s povezivanjem
  - Najbolje sigurnosne prakse za konfiguraciju hosta

- **13-mcp-inspector/README.md**: Novi vodič za ispravljanje pogrešaka MCP Inspektora
  - Metode instalacije (npx, globalni npm, iz izvora)
  - Povezivanje na poslužitelje preko stdio i HTTP/SSE
  - Testni alati, resursi i radni tokovi promptova
  - Integracija VS Codea s MCP Inspektorom
  - Česti scenariji ispravljanja pogrešaka s rješenjima

**Modul 04 - Praktična primjena**
- **pagination/README.md**: Novi vodič za implementaciju paginacije
  - Obrasci paginacije temeljeni na kurzoru u Pythonu, TypeScriptu, Javi
  - Rukovanje paginacijom na strani klijenta
  - Strategije dizajna kurzora (neprozirni vs. strukturirani)
  - Preporuke za optimizaciju performansi

**Modul 05 - Napredne teme**
- **mcp-protocol-features/README.md**: Novi detaljni pregled značajki protokola
  - Implementacija obavijesti o napretku
  - Obrasci otkazivanja zahtjeva
  - Predlošci resursa s URI šablonama
  - Upravljanje životnim ciklusom poslužitelja
  - Kontrola razine zapisivanja
  - Obrasci rukovanja greškama s JSON-RPC kodovima

#### Popravci navigacije (ažurirano 24+ datoteka)

**Glavni modul README-ovi**
 Sada povezuje i na prvu lekciju I sljedeći modul

**Poddatoteke 02-Security**
- Sve 5 dodatnih sigurnosnih dokumenata sada imaju navigaciju "Što slijedi":

**Datoteke 09-CaseStudy**
- Sve datoteke studija slučaja sada imaju sekvencijalnu navigaciju:

**Labovi 10-StreamliningAI**
Dodana sekcija Što slijedi u pregled modula 10 i modul 11

#### Popravci koda i sadržaja

**Ažuriranja SDK-a i ovisnosti**
Popravljen prazan openai verzijski broj na `^4.95.0`
Ažuriran SDK s `^1.8.0` na `>=1.26.0`
Ažurirani MCP pinovi verzija na `>=1.26.0`

**Popravci koda**
Ispravljen nevažeći model `gpt-4o-mini` u `gpt-4.1-mini`

**Popravci sadržaja**
Ispravljen pokvareni link `READMEmd` → `README.md`, ispravljen naslov kurikuluma `Module 1-3` → `Module 0-3`, ispravljena osjetljivost na velika/mala slova u putu
Uklonjen korumpirani duplicirani sadržaj Studije slučaja 5

**Poboljšanja za početnike**
Dodani ispravni uvod, ciljevi učenja i preduvjeti za početnike

#### Ažuriranja kurikuluma

**Glavni README.md**
- Dodane stavke 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginacija), 5.16 (Značajke protokola) u tablicu kurikuluma

**Modulski README-ovi**
Dodane lekcije 12 i 13 u popis lekcija
Dodana sekcija Praktični vodiči s linkom za paginaciju
Dodane lekcije 5.15 (Prilagođeni transport) i 5.16 (Značajke protokola)

**study_guide.md**
- Ažurirana mentalna mapa sa svim novim temama: MCP Hosts postavljanje, MCP Inspector, strategije paginacije, detaljni pregled značajki protokola

## 28. siječnja 2026.

### Pregled usklađenosti MCP specifikacije 2025-11-25

#### Unapređenje osnovnih koncepata (01-CoreConcepts/)
- **Novi primitiv klijenta - Roots**: Dodana sveobuhvatna dokumentacija o primitivu Roots koji omogućuje poslužiteljima razumijevanje granica datotečnog sustava i pristupnih prava
- **Bilješke o alatima**: Dodana dokumentacija o bilješkama o ponašanju alata (`readOnlyHint`, `destructiveHint`) za bolje odluke o izvršavanju alata
- **Pozivanje alata u Sampling-u**: Ažurirana documentation za Sampling za uključivanje parametara `tools` i `toolChoice` za modelom upravljanu aktivaciju alata tijekom zahtjeva za Sampling
- **URL način poticanja**: Dodana dokumentacija o poticanju na vanjske mrežne interakcije inicirane od strane poslužitelja putem URL načina
- **Zadaci (eksperimentalno)**: Dodano novo poglavlje o značajci Zadaci za trajne wrapper-e izvršenja i odgođeno dohvaćanje rezultata
- **Podrška za ikone**: Zabilježeno da alati, resursi, predlošci resursa i promptovi sada mogu sadržavati ikone kao dodatne metapodatke

#### Ažuriranja dokumentacije
- **README.md**: Dodana referenca verzije MCP specifikacije 2025-11-25 i objašnjenje verzioniranja po datumu
- **study_guide.md**: Ažurirana karta kurikuluma da uključuje Zadatke i bilješke o alatima u odjeljak Osnovni koncepti; ažurirani vremenski žig dokumenta

#### Verifikacija usklađenosti sa specifikacijom
- **Verzija protokola**: Potvrđeno da sva dokumentacija referira trenutnu MCP specifikaciju 2025-11-25
- **Usuglašenost arhitekture**: Potvrđen dvoslajni arhitekturalni model (sloj podataka + sloj transporta)
- **Dokumentacija primitiva**: Provjereni primitivni objekti poslužitelja (Resursi, Promptovi, Alati) i primitivni objekti klijenta (Sampling, Poticanje, Dnevnici, Roots)
- **Transportni mehanizmi**: Provjereni opisi STDIO i streamabilnog HTTP transporta
- **Sigurnosne smjernice**: Potvrđena usklađenost s najnovijom MCP sigurnosnom praksom

#### Glavne značajke MCP 2025-11-25 dokumentirane
- **OpenID Connect otkrivanje**: Otkrivanje auth poslužitelja putem OIDC
- **Metapodaci OAuth Client ID-a**: Preporučeni mehanizam registracije klijenta
- **JSON Schema 2020-12**: Zadani dijalekt za MCP definicije shema
- **Sustav slojevanja SDK-a**: Formalizirani zahtjevi za podršku i održavanje SDK značajki
- **Struktura upravljanja**: Formalizirane radne i interesne skupine MCP upravljanja

### Veliko ažuriranje sigurnosne dokumentacije (02-Security/)

#### Integracija MCP Security Summit radionice (Sherpa)
- **Novi praktični izvor učenja**: Dodana sveobuhvatna integracija s [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) kroz cijelu sigurnosnu dokumentaciju
- **Pregled ekspedicijske rute**: Dokumentirano cjelokupno kretanje od Baznog kampa do Summita
- **Sinkronizacija s OWASP-om**: Svi sigurnosni savjeti sada su mapirani na OWASP MCP Azure Security Guide rizike

#### Integracija OWASP MCP Top 10
- **Novi odjeljak**: Dodana tablica OWASP MCP Top 10 sigurnosnih rizika sa Azure mitigacijama u glavnom sigurnosnom README-u
- **Rizično bazirana dokumentacija**: Ažuriran dokument mcp-security-controls-2025.md s referencama na OWASP MCP rizike za svaki sigurnosni domen
- **Referentna arhitektura**: Povezan s OWASP MCP Azure Security Guide referentnom arhitekturom i implementacijskim obrascima

#### Ažurirane sigurnosne datoteke
- **README.md**: Dodan pregled radonice Sherpa, tablica rute ekspedicije, sažetak rizika OWASP MCP Top 10 i sekcija praktične obuke
- **mcp-security-controls-2025.md**: Ažuriran zaglavlje na veljaču 2026., dodane OWASP referentne oznake rizika (MCP01-MCP08), ispravljena nesukladnost verzije specifikacije
- **mcp-security-best-practices-2025.md**: Dodana sekcija Sherpa i OWASP resursa, ažuriran vremenski žig
- **mcp-best-practices.md**: Dodana sekcija praktične obuke s Sherpa i OWASP linkovima
- **azure-content-safety-implementation.md**: Dodana OWASP MCP06 referenca, usklađenost s Sherpa Kampom 3 i dodatna sekcija resursa

#### Dodani novi resursi
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pojedinačne stranice rizika OWASP MCP (MCP01-MCP10)

### Usklađenost kurikuluma sa MCP specifikacijom 2025-11-25

#### Modul 03 - Uvod
- **Dokumentacija SDK-a**: Dodan Go SDK na službenu listu SDK-a; ažurirani svi SDK linkovi da odgovaraju MCP specifikaciji 2025-11-25
- **Pojašnjenje transporta**: Ažurirani opisi STDIO i HTTP streaming transporta s eksplicitnim referencama na specifikaciju

#### Modul 04 - Praktična primjena
- **Ažuriranja SDK-a**: Dodan Go SDK; ažurirana lista SDK-a s referencom na verziju specifikacije
- **Specifikacija autorizacije**: Ažurirana MCP specifikacija autorizacije na trenutačnu verziju 2025-11-25

#### Modul 05 - Napredne teme
- **Nove značajke**: Dodana napomena o novim značajkama MCP specifikacije 2025-11-25 (Zadaci, bilješke o alatima, URL način poticanja, Roots)
- **Sigurnosni resursi**: Dodani linkovi na OWASP MCP Top 10 i Sherpa radionicu kao dodatne reference

#### Modul 06 - Doprinosi zajednice
- **Lista SDK-a**: Dodani Swift i Rust SDK; ažurirani link specifikacije na verziju 2025-11-25
- **Referenca specifikacije**: Ažurirana MCP specifikacija na direktni URL verzije

#### Modul 07 - Lekcije ranog usvajanja
- **Ažuriranja resursa**: Dodan link MCP specifikacije 2025-11-25 i OWASP MCP Top 10 u dodatne resurse

#### Modul 08 - Najbolje prakse
- **Verzija specifikacije**: Ažurirana referenca MCP specifikacije na 2025-11-25
- **Sigurnosni resursi**: Dodani OWASP MCP Top 10 i Sherpa radionica u dodatne reference

#### Modul 10 - Optimizacija AI tokova rada
- **Ažuriranje značke**: MCP verzija oznaka promijenjena s verzije SDK-a (1.9.3) na verziju specifikacije (2025-11-25)
- **Linkovi resursa**: Ažuriran MCP specifikacija link; dodan OWASP MCP Top 10

#### Modul 11 - MCP Server praktični labovi
- **Referenca specifikacije**: Ažurirana MCP specifikacija na verziju 2025-11-25
- **Sigurnosni resursi**: Dodan OWASP MCP Top 10 u službene resurse

## 18. prosinca 2025.
### Ažuriranje sigurnosne dokumentacije - MCP specifikacija 2025-11-25

#### Najbolje sigurnosne prakse MCP-a (02-Security/mcp-best-practices.md) - Ažuriranje verzije specifikacije
- **Ažuriranje verzije protokola**: Ažurirano za referencu najnovije MCP specifikacije 2025-11-25 (objavljeno 25. studenog 2025.)
  - Ažurirane sve reference verzije specifikacije sa 2025-06-18 na 2025-11-25
  - Ažurirani datumi u dokumentu sa 18. kolovoza 2025. na 18. prosinca 2025.
  - Provjerene sve URL-ove specifikacija da upućuju na aktualnu dokumentaciju
- **Provjera sadržaja**: Sveobuhvatna provjera sigurnosnih najboljih praksi u skladu s najnovijim standardima
  - **Microsoft sigurnosna rješenja**: Provjerena trenutna terminologija i linkovi za Prompt Shields (ranije "detekcija rizika jailbreaka"), Azure Content Safety, Microsoft Entra ID i Azure Key Vault
  - **OAuth 2.1 sigurnost**: Potvrđena usklađenost s najnovijim sigurnosnim praksama OAuth-a
  - **OWASP standardi**: Validirane OWASP Top 10 reference za LLM modele ostaju ažurirane
  - **Azure usluge**: Provjereni svi Microsoft Azure dokumentacijski linkovi i najbolje prakse
- **Usuglašavanje standarda**: Sve referencirane sigurnosne norme potvrđene kao aktualne
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Najbolje sigurnosne prakse
  - Azure sigurnosni i usklađenostni okviri
- **Resursi za implementaciju**: Provjereni svi linkovi za vodiče za implementaciju i resurse
  - Autentikacijski obrasci Azure API Managementa
  - Vodiči za integraciju Microsoft Entra ID-ja
  - Upravljanje tajnama Azure Key Vaulta
  - DevSecOps pipeline-i i rješenja za nadzor

### Osiguranje kvalitete dokumentacije
- **Usklađenost sa specifikacijom**: Osigurano da svi obavezni sigurnosni zahtjevi MCP-a (MORA/MORA NE) budu usklađeni s najnovijom specifikacijom
- **Ažurnost resursa**: Provjereni svi vanjski linkovi na Microsoftovu dokumentaciju, sigurnosne standarde i vodiče za implementaciju
- **Obuhvat najboljih praksi**: Potvrđena sveobuhvatnost pokrivenosti autentikacije, autorizacije, prijetnji specifičnih za AI, sigurnosti opskrbnog lanca i obrasca za poduzeća

## 6. listopada 2025.

### Proširenje odjeljka Početak – Napredno korištenje servera i jednostavna autentikacija

#### Napredno korištenje servera (03-GettingStarted/10-advanced)
- **Novi poglavlje Dodano**: Uveden sveobuhvatan vodič za napredno korištenje MCP servera, koji pokriva i redovnu i niskorazinsku arhitekturu servera.
  - **Redovni vs. niskorazinski server**: Detaljna usporedba i primjeri koda u Pythonu i TypeScriptu za oba pristupa.
  - **Dizajn baziran na handlerima**: Objašnjenje upravljanja alatima/resursima/promptima bazirano na handlerima za skalabilne, fleksibilne implementacije servera.
  - **Praktični obrasci**: Stvarni scenariji u kojima su niskorazinski obrasci servera korisni za napredne značajke i arhitekturu.

#### Jednostavna autentikacija (03-GettingStarted/11-simple-auth)
- **Novi poglavlje Dodano**: Korak-po-korak vodič za implementaciju jednostavne autentikacije u MCP serverima.
  - **Koncepti autentikacije**: Jasno objašnjenje razlike između autentikacije i autorizacije, te rukovanje vjerodajnicama.
  - **Implementacija osnovne autentikacije**: Obrasci autentikacije temeljeni na middlewareu u Pythonu (Starlette) i TypeScriptu (Express) s primjerima koda.
  - **Progresija prema naprednoj sigurnosti**: Upute za početak sa jednostavnom autentikacijom i napredovanje prema OAuth 2.1 i RBAC-u, s referencama na module napredne sigurnosti.

Ova proširenja pružaju praktične, praktične smjernice za izgradnju robusnijih, sigurnijih i fleksibilnijih MCP server implementacija, povezivanjem temeljnih koncepata s naprednim proizvodnim obrascima.

## 29. rujna 2025.

### Laboratoriji integracije baze podataka MCP servera - Sveobuhvatan praktični obrazovni put

#### 11-MCPServerHandsOnLabs - Novi potpuni tečaj za integraciju baze podataka
- **Potpuni put učenja od 13 laboratorija**: Dodan sveobuhvatan praktični tečaj za izgradnju proizvodno spremnih MCP servera s PostgreSQL integracijom baze podataka
  - **Primjer stvarnog svijeta**: Analitika Zava Retail koja demonstrira obrasce razine poduzeća
  - **Strukturirana progresija učenja**:
    - **Laboratoriji 00-03: Osnove** - Uvod, osnovna arhitektura, sigurnost i višekorisnički način, postavljanje okruženja
    - **Laboratoriji 04-06: Izgradnja MCP servera** - Dizajn baze podataka i shema, implementacija MCP servera, razvoj alata
    - **Laboratoriji 07-09: Napredne značajke** - Integracija semantičkog pretraživanja, testiranje i otklanjanje pogrešaka, integracija s VS Code
    - **Laboratoriji 10-12: Proizvodnja i najbolje prakse** - Strategije za proizvodnju, nadzor i promatranje, najbolje prakse i optimizacija
  - **Tehnologije razine poduzeća**: FastMCP framework, PostgreSQL s pgvectorom, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Napredne značajke**: Sigurnost na razini redaka (RLS), semantičko pretraživanje, višekorisnički pristup podacima, vektorske embeddings, praćenje u stvarnom vremenu

#### Standardizacija terminologije - Pretvorba modula u laboratoriju
- **Sveobuhvatno ažuriranje dokumentacije**: Sistematski ažurirani svi README-ovi u 11-MCPServerHandsOnLabs za korištenje termina "Laboratorij" umjesto "Modul"
  - **Naslovi odjeljaka**: Promijenjeno "Što ovaj modul pokriva" u "Što ovaj laboratorij pokriva" u svih 13 laboratorija
  - **Opis sadržaja**: Promijenjeno "Ovaj modul pruža..." u "Ovaj laboratorij pruža..." kroz dokumentaciju
  - **Ciljevi učenja**: Ažurirano "Na kraju ovog modula..." u "Na kraju ovog laboratorija..."
  - **Navigacijski linkovi**: Pretvorene sve reference "Modul XX:" u "Laboratorij XX:" u međureferencama i navigaciji
  - **Praćenje završetka**: Ažurirano "Nakon završetka ovog modula..." u "Nakon završetka ovog laboratorija..."
  - **Sačuvane tehničke reference**: Očuvane reference na Python module u konfiguracijskim datotekama (npr. `"module": "mcp_server.main"`)

#### Poboljšanje vodiča za učenje (study_guide.md)
- **Vizualna karta kurikuluma**: Dodan novi odjeljak "11. Laboratoriji integracije baza podataka" sa sveobuhvatnom vizualizacijom strukture laboratorija
- **Struktura repozitorija**: Ažurirano s deset na jedanaest glavnih odjeljaka sa detaljnim opisom 11-MCPServerHandsOnLabs
- **Upute za navigaciju**: Poboljšane upute za navigaciju pokrivajući odjeljke 00-11
- **Pokriće tehnologije**: Dodan opis integracije FastMCP-a, PostgreSQL-a i Azure usluga
- **Ishodi učenja**: Naglašena izrada proizvodno spremnih servera, obrasci integracije baze podataka i sigurnost za poduzeća

#### Poboljšanje strukture glavnog README-a
- **Terminologija bazirana na laboratorijima**: Ažuriran glavni README.md u 11-MCPServerHandsOnLabs za konzistentnu upotrebu strukture "Laboratorija"
- **Organizacija puta učenja**: Jasna progresija od temeljnih koncepata preko napredne implementacije do proizvodnog postavljanja
- **Fokus na stvarni svijet**: Naglasak na praktično, laboratorijsko učenje s obrascima i tehnologijama razine poduzeća

### Poboljšanja kvalitete i dosljednosti dokumentacije
- **Naglasak na praktičnom učenju**: Ojačani pristup zasnovan na laboratorijima kroz cijelu dokumentaciju
- **Fokus na obrasce za poduzeća**: Istaknute proizvodno spremne implementacije i sigurnosni aspekti za poduzeća
- **Integracija tehnologije**: Sveobuhvatno pokriće modernih Azure usluga i AI obrazaca integracije
- **Progresija učenja**: Jasan, strukturiran put od osnovnih koncepata do proizvodnog postavljanja

## 26. rujna 2025.

### Proširenje studija slučaja - Integracija GitHub MCP registra

#### Studije slučaja (09-CaseStudy/) - Fokus na razvoj ekosustava
- **README.md**: Veliko proširenje s opsežnim studijem slučaja o GitHub MCP registru
  - **Studija slučaja GitHub MCP registra**: Novi detaljni studij koji pregledava lansiranje GitHub MCP registra u rujnu 2025.
    - **Analiza problema**: Detaljna analiza fragmentiranog otkrivanja i postavljanja MCP servera
    - **Arhitektura rješenja**: GitHubov pristup centraliziranog registra s instalacijom jednim klikom u VS Code
    - **Poslovni utjecaj**: Mjerljiva poboljšanja u onboardingu i produktivnosti developera
    - **Strateška vrijednost**: Fokus na modularno postavljanje agenata i interoperabilnost alata
    - **Razvoj ekosustava**: Pozicioniranje kao temeljna platforma za integraciju agenata
  - **Poboljšana struktura studija slučaja**: Ažurirane sve sedam studija slučaja sa konzistentnim formatom i opširnim opisima
    - Azure AI Travel Agents: Naglasak na orkestraciju više agenata
    - Azure DevOps integracija: Fokus na automatizaciju tijeka rada
    - Dohvat dokumenata u stvarnom vremenu: Implementacija Python konzolnog klijenta
    - Interaktivni generator plana učenja: Chainlit konverzacijska web aplikacija
    - Dokumentacija u editoru: Integracija VS Code i GitHub Copilota
    - Azure API Management: Obrasci integracije poduzeća za API-je
    - GitHub MCP Registry: Razvoj ekosustava i platforma zajednice
  - **Sveobuhvatan zaključak**: Prepisan završni odjeljak ističući sedam studija slučaja koje pokrivaju više dimenzija MCP implementacije
    - Integracija poduzeća, orkestracija više agenata, produktivnost developera
    - Razvoj ekosustava, obrazovne primjene
    - Poboljšani uvidi u arhitektonske obrasce, strategije implementacije i najbolje prakse
    - Naglasak na MCP kao zrelom, proizvodno spremnom protokolu

#### Ažuriranja vodiča za učenje (study_guide.md)
- **Vizualna karta kurikuluma**: Ažuriran mindmap za uključivanje GitHub MCP registra u odjeljak studija slučaja
- **Opis studija slučaja**: Poboljšano sa generičkih opisa na detaljan pregled sedam opsežnih studija slučaja
- **Struktura repozitorija**: Ažuriran odjeljak 10 da odražava opsežno pokriće studija slučaja sa specifičnim pojedinostima implementacije
- **Integracija promjena u dnevnik promjena**: Dodan unos od 26. rujna 2025. s dokumentiranjem dodavanja GitHub MCP registra i poboljšanja studija slučaja
- **Ažuriranje datuma**: Ažuriran podnožje s vremenskim pečatom na najnoviju reviziju (26. rujna 2025.)

### Poboljšanja kvalitete dokumentacije
- **Poboljšanja dosljednosti**: Standardiziran format i struktura studija slučaja u svih sedam primjera
- **Sveobuhvatno pokriće**: Studije slučaja sada pokrivaju poduzeće, produktivnost developera i razvoj ekosustava
- **Strateško pozicioniranje**: Povećani fokus na MCP kao temeljnu platformu za postavljanje sustava agenata
- **Integracija resursa**: Ažurirani dodatni resursi za uključivanje linka na GitHub MCP registar

## 15. rujna 2025.

### Proširenje naprednih tema - Prilagođeni transporti i inženjering konteksta

#### MCP prilagođeni transporti (05-AdvancedTopics/mcp-transport/) - Novi vodič za naprednu implementaciju
- **README.md**: Potpuni vodič za implementaciju prilagođenih MCP transportnih mehanizama
  - **Azure Event Grid transport**: Sveobuhvatna implementacija serverless transporta pokretanog događajima
    - Primjeri u C#, TypeScriptu i Pythonu s integracijom Azure Functions
    - Obrasci arhitekture pokretane događajima za skalabilna MCP rješenja
    - Primatelji webhooka i push-based rukovanje porukama
  - **Azure Event Hubs transport**: Implementacija visoke propusnosti streaming transporta
    - Mogućnosti striminga u stvarnom vremenu za nisko kašnjenje scenarije
    - Strategije particioniranja i upravljanja kontrolnim točkama
    - Grupiranje poruka i optimizacija performansi
  - **Obrasci integracije poduzeća**: Proizvodno spremni arhitektonski primjeri
    - Raspodijeljena MCP obrada preko više Azure Functions
    - Hibridne transportne arhitekture koje kombiniraju više tipova transporta
    - Strategije izdržljivosti poruka, pouzdanosti i rukovanja pogreškama
  - **Sigurnost i nadzor**: Integracija Azure Key Vaulta i obrasci za promatranje
    - Autentikacija upravljanim identitetom i pristup s najmanjim privilegijama
    - Telemetrija Application Insights i nadzor performansi
    - Prekidači kruga i obrasci otpornosti na pogreške
  - **Okviri za testiranje**: Sveobuhvatne strategije testiranja prilagođenih transporta
    - Jedinično testiranje s test-doublima i mocking frameworkima
    - Integracijsko testiranje s Azure Test Containers
    - Razmatranja performansi i opterećenja

#### Inženjering konteksta (05-AdvancedTopics/mcp-contextengineering/) - Nova AI disciplina
- **README.md**: Sveobuhvatno istraživanje inženjeringa konteksta kao nove discipline
  - **Osnovni principi**: Potpuno dijeljenje konteksta, svijest o odlukama akcije i upravljanje kontekstnim prozorima
  - **Usuglašavanje s MCP protokolom**: Kako dizajn MCP-a adresira izazove inženjeringa konteksta
    - Ograničenja kontekstnih prozora i progresivne strategije učitavanja
    - Određivanje relevantnosti i dinamičko dohvaćanje konteksta
    - Višemode rukovanje kontekstom i sigurnosne razmatranja
  - **Pristupi implementaciji**: Jednoprocesna vs. arhitekture s više agenata
    - Tehnike segmentiranja i prioritizacije konteksta
    - Progresivno učitavanje i strategije kompresije konteksta
    - Slojeviti pristupi kontekstu i optimizacija dohvaćanja
  - **Okvir za mjerenje**: Nove metrike za evaluaciju učinkovitosti konteksta
    - Učinkovitost unosa, performanse, kvaliteta i korisničko iskustvo
    - Eksperimentalni pristupi optimizaciji konteksta
    - Analiza pogrešaka i metode poboljšanja

#### Ažuriranja navigacije kurikulumom (README.md)
- **Poboljšana struktura modula**: Ažuriran tablicu kurikuluma za uključivanje novih naprednih tema
  - Dodani Context Engineering (5.14) i Custom Transport (5.15)
  - Konzistentno formatiranje i navigacijski linkovi kroz sve module
  - Ažurirani opisi koji odražavaju trenutni sadržaj

### Poboljšanja strukture direktorija
- **Standardizacija naziva**: "mcp transport" preimenovan u "mcp-transport" radi konzistentnosti s ostalim mapama naprednih tema
- **Organizacija sadržaja**: Sve mape u 05-AdvancedTopics sada prate uniformni obrazac naziva (mcp-[tema])

### Poboljšanja kvalitete dokumentacije
- **Usklađenost s MCP specifikacijom**: Svi novi sadržaji referenciraju aktualnu MCP specifikaciju 2025-06-18
- **Primjeri u više jezika**: Sveobuhvatni primjeri koda u C#, TypeScriptu i Pythonu
- **Fokus na poduzeća**: Proizvodno spremni obrasci i Azure cloud integracija
- **Vizualna dokumentacija**: Mermaid dijagrami za arhitekturu i prikaz toka

## 18. kolovoza 2025.

### Sveobuhvatno ažuriranje dokumentacije - standardi MCP 2025-06-18

#### Najbolje sigurnosne prakse MCP-a (02-Security/) - Potpuna modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Potpuno prepravljanje usklađeno s MCP specifikacijom 2025-06-18
  - **Obavezni Zahtjevi**: Dodani eksplicitni ZAHTJEVAM / ZABRANAMA iz službene specifikacije s jasnim vizualnim indikatorima
  - **12 Temeljnih Sigurnosnih Praksi**: Preuređeno s popisa od 15 stavki u sveobuhvatna sigurnosna područja
    - Sigurnost žetona i autentikacija s integracijom vanjskog pružatelja identiteta
    - Upravljanje sesijama i sigurnost prijenosa s kriptografskim zahtjevima
    - Zaštita specifična za AI s integracijom Microsoft Prompt Shields
    - Kontrola pristupa i dopuštenja s načelom najmanjih privilegija
    - Sigurnost sadržaja i nadzor s integracijom Azure Content Safety
    - Sigurnost lanca opskrbe s detaljnom verifikacijom komponenti
    - Sigurnost OAuth i prevencija „zbunjenog zamjenika“ s implementacijom PKCE
    - Odgovor na incidente i oporavak s automatiziranim mogućnostima
    - Sukladnost i upravljanje usklađeno s regulatornim zahtjevima
    - Napredne sigurnosne kontrole s arhitekturom zero trust
    - Integracija Microsoft sigurnosnog ekosustava sa sveobuhvatnim rješenjima
    - Kontinuirani razvoj sigurnosti s prilagodljivim praksama
  - **Microsoft sigurnosna rješenja**: Poboljšane smjernice za integraciju Prompt Shields, Azure Content Safety, Entra ID i GitHub Advanced Security
  - **Resursi za implementaciju**: Kategorizirani opsežni poveznici resursa po službenoj MCP dokumentaciji, Microsoft sigurnosnim rješenjima, sigurnosnim standardima i vodičima za implementaciju

#### Napredne sigurnosne kontrole (02-Security/) - Implementacija u poduzećima
- **MCP-SECURITY-CONTROLS-2025.md**: Potpuna izmjena sa sigurnosnim okvirom razine poduzeća
  - **9 Sveobuhvatnih sigurnosnih područja**: Prošireno od osnovnih kontrola do detaljnog okvira za poduzeća
    - Napredna autentikacija i autorizacija s integracijom Microsoft Entra ID
    - Sigurnost žetona i kontrole protiv propuštanja s detaljnom validacijom
    - Kontrole sigurnosti sesija s prevencijom otmice
    - Sigurnosne kontrole specifične za AI s prevencijom ubrizgavanja u upite i trovanja alata
    - Prevencija napada „zbunjenog zamjenika“ s OAuth proxy sigurnošću
    - Sigurnost izvršenja alata kroz sandboxing i izolaciju
    - Kontrole sigurnosti lanca opskrbe s verifikacijom ovisnosti
    - Kontrole nadzora i detekcije s integracijom SIEM-a
    - Odgovor na incidente i oporavak s automatiziranim mogućnostima
  - **Primjeri implementacije**: Dodani detaljni YAML konfiguracijski blokovi i primjeri koda
  - **Integracija Microsoft rješenja**: Sveobuhvatno pokrivanje Azure sigurnosnih usluga, GitHub Advanced Security i upravljanja identitetom za poduzeća

#### Napredne sigurnosne teme (05-AdvancedTopics/mcp-security/) - Implementacija spremna za produkciju
- **README.md**: Potpuno prepravljanje za sigurnosnu implementaciju u poduzećima
  - **Usklađenost s trenutnom specifikacijom**: Ažurirano na MCP specifikaciju 2025-06-18 s obaveznim sigurnosnim zahtjevima
  - **Poboljšana autentikacija**: Integracija Microsoft Entra ID s opsežnim primjerima u .NET i Java Spring Security
  - **Integracija AI sigurnosti**: Implementacija Microsoft Prompt Shields i Azure Content Safety s detaljnim primjerima u Pythonu
  - **Napredna zaštita od prijetnji**: Sveobuhvatni primjeri implementacije za
    - Prevenciju napada „zbunjenog zamjenika“ s PKCE i validacijom korisničkog pristanka
    - Prevenciju propuštanja žetona s validacijom publike i sigurnim upravljanjem žetonima
    - Prevenciju otmice sesije s kriptografskim povezivanjem i analizom ponašanja
  - **Integracija sigurnosti u poduzeću**: Nadzor putem Azure Application Insights, pipelineovi za detekciju prijetnji i sigurnost lanca opskrbe
  - **Kontrolni popis implementacije**: Jasna podjela obaveznih i preporučenih sigurnosnih kontrola s prednostima Microsoft sigurnosnog ekosustava

### Kvaliteta dokumentacije i usklađenost sa standardima
- **Reference specifikacija**: Ažurirani svi linkovi na trenutnu MCP specifikaciju 2025-06-18
- **Microsoft sigurnosni ekosustav**: Poboljšane smjernice za integraciju u sve sigurnosne dokumente
- **Praktična implementacija**: Dodani detaljni primjeri koda u .NET, Java i Python s obrascima za poduzeća
- **Organizacija resursa**: Sveobuhvatna kategorizacija službene dokumentacije, sigurnosnih standarda i vodiča za implementaciju
- **Vizualni indikatori**: Jasna oznaka obaveznih zahtjeva u odnosu na preporučene prakse


#### Temeljni pojmovi (01-CoreConcepts/) - Potpuna modernizacija
- **Ažuriranje verzije protokola**: Referenca na trenutnu MCP specifikaciju 2025-06-18 s verzioniranjem temeljenim na datumu (format GGGG-MM-DD)
- **Dorada arhitekture**: Poboljšani opisi hostova, klijenata i servera za odražavanje trenutnih MCP arhitektonskih uzoraka
  - Hostovi sada jasno definirani kao AI aplikacije koje koordiniraju više MCP client konekcija
  - Klijenti opisani kao konektori protokola održavajući jedno-na-jedan odnose sa serverom
  - Serveri poboljšani s lokalnim i udaljenim scenarijima postavljanja
- **Restrukturiranje primitiva**: Potpuno preuređenje server i client primitiva
  - Server primitivni elementi: Resursi (izvori podataka), Upiti (predlošci), Alati (izvršne funkcije) s detaljnim objašnjenjima i primjerima
  - Klijentski primitivni elementi: Uzorkovanje (LLM završeci), Izdvajanje (korisnički unosi), Evidencija (debugiranje/nadzor)
  - Ažurirano s aktualnim obrascima metoda za otkrivanje (`*/list`), dohvat (`*/get`) i izvršenje (`*/call`)
- **Arhitektura protokola**: Uvedeni dvostruki slojevi arhitekture
  - Podatkovni sloj: Temelj JSON-RPC 2.0 s upravljanjem životnim ciklusom i primitivima
  - Transportni sloj: STDIO (lokalni) i Streamable HTTP sa SSE (udaljeni) transportnim mehanizmima
- **Sigurnosni okvir**: Sveobuhvatna sigurnosna načela uključujući eksplicitni pristanak korisnika, zaštitu privatnosti podataka, sigurnost izvršenja alata i sigurnost transportnog sloja
- **Obrasci komunikacije**: Ažurirane poruke protokola za prikaz inicijalizacije, otkrivanja, izvršenja i tokova obavijesti
- **Primjeri koda**: Osvježeni višestruki jezični primjeri (.NET, Java, Python, JavaScript) za odraz aktualnih MCP SDK obrazaca

#### Sigurnost (02-Security/) - Sveobuhvatna sigurnosna revizija  
- **Usklađenost sa standardima**: Potpuna usklađenost sa zahtjevima MCP specifikacije 2025-06-18 za sigurnost
- **Evolucija autentikacije**: Dokumentiran razvoj od prilagođenih OAuth servera do delegacije vanjskom pružatelju identiteta (Microsoft Entra ID)
- **Analiza prijetnji specifičnih za AI**: Poboljšano pokriće suvremenih AI vektora napada
  - Detaljni scenariji napada ubrizgavanjem upita s primjerima iz stvarnog svijeta
  - Mehanizmi trovanja alata i obrasci napada „rug pull“
  - Trovanje kontekstnog okna i napadi zabune modela
- **Microsoft AI sigurnosna rješenja**: Sveobuhvatna pokrivenost Microsoft sigurnosnog ekosustava
  - AI Prompt Shields s naprednom detekcijom, isticanjem i tehnikama razdjelnika
  - Obrasci integracije Azure Content Safety
  - GitHub Advanced Security za zaštitu lanca opskrbe
- **Napredna mitigacija prijetnji**: Detaljne sigurnosne kontrole za
  - Otmicu sesije s MCP-specifičnim scenarijima napada i zahtjevima za kriptografski identitet sesije
  - Problem zbunjenog zamjenika u MCP proxy scenarijima s eksplicitnim zahtjevima pristanka
  - Ranljivosti propuštanja žetona s obaveznim kontrolama validacije
- **Sigurnost lanca opskrbe**: Prošireno pokriće AI lanca opskrbe uključujući temeljne modele, usluge ugradnji, pružatelje konteksta i API-je trećih strana
- **Sigurnost temelja**: Poboljšana integracija s obrascima sigurnosti poduzeća uključujući arhitekturu zero trust i Microsoft sigurnosni ekosustav
- **Organizacija resursa**: Kategorizirani opsežni poveznici resursa po tipu (Službena dokumentacija, Standardi, Istraživanja, Microsoft rješenja, Vodiči za implementaciju)

### Poboljšanja kvalitete dokumentacije
- **Strukturirani ciljevi učenja**: Poboljšani ciljevi učenja s konkretnim, provedivim ishodima
- **Križne reference**: Dodani linkovi između povezanih tema o sigurnosti i temeljnih pojmova
- **Aktualne informacije**: Ažurirani svi datumski referentni podaci i linkovi na specifikacije prema važećim standardima
- **Smjernice za implementaciju**: Dodane konkretne, provedive smjernice za implementaciju kroz oba segmenta

## 16. srpnja 2025.

### README i poboljšanja navigacije
- Potpuno redizajniran izgled navigacije u README.md
- Zamijenjeni `<details>` tagovi pristupačnijim tabelarnim formatom
- Izrađene alternativne opcije izgleda u novom folderu "alternative_layouts"
- Dodani primjeri navigacije u obliku kartica, kartica s karticama i akordeonskog stila
- Ažuriran odjeljak strukture repozitorija za uključenje svih najnovijih datoteka
- Poboljšan odjeljak "Kako koristiti ovaj kurikulum" s jasnim preporukama
- Ažurirani MCP specifikacijski linkovi za ispravno usmjeravanje na URL-ove
- Dodan odjeljak o inženjerstvu konteksta (5.14) u strukturu kurikuluma

### Ažuriranja vodiča za učenje
- Potpuno revidiran vodič za usklađivanje s trenutnom strukturom repozitorija
- Dodani novi odjeljci za MCP klijente i alate, te popularne MCP servere
- Ažurirana Vizualna karta kurikuluma za točan prikaz svih tema
- Poboljšani opisi naprednih tema za pokrivanje svih specijaliziranih područja
- Ažuriran odjeljak Studije slučaja za prikaz stvarnih primjera
- Dodan ovaj opsežni dnevnik promjena

### Doprinosi zajednice (06-CommunityContributions/)
- Dodane detaljne informacije o MCP serverima za generiranje slika
- Dodan opsežni odjeljak o korištenju Claude u VSCode-u
- Dodane upute za postavljanje i korištenje Cline terminal klijenta
- Ažuriran odjeljak MCP klijenata za uključivanje svih popularnih opcija
- Poboljšani primjeri doprinosa s preciznijim uzorcima koda

### Napredne teme (05-AdvancedTopics/)
- Organizirani svi folderi specijaliziranih tema s konzistentnim imenovanjem
- Dodani materijali i primjeri iz inženjerstva konteksta
- Dodana dokumentacija za integraciju Foundry agenta
- Poboljšana dokumentacija integracije sigurnosti Entra ID-a

## 11. lipnja 2025.

### Početno kreiranje
- Objavljena prva verzija MCP za početnike
- Stvorena osnovna struktura za svih 10 glavnih sekcija
- Implementirana Vizualna karta kurikuluma za navigaciju
- Dodani početni uzorci projekata u više programska jezika

### Početak rada (03-GettingStarted/)
- Kreirani prvi primjeri implementacije servera
- Dodane smjernice za razvoj klijenata
- Uključene upute za integraciju LLM klijenata
- Dodana dokumentacija za integraciju u VS Code
- Implementirani primjeri servera sa Server-Sent Events (SSE)

### Temeljni pojmovi (01-CoreConcepts/)
- Dodano detaljno objašnjenje klijent-server arhitekture
- Kreirana dokumentacija ključnih protokol komponenti
- Dokumentirani obrasci poruka u MCP

## 23. svibnja 2025.

### Struktura repozitorija
- Inicijaliziran repozitorij s osnovnom strukturom foldera
- Kreirani README dokumenti za svaku glavnu sekciju
- Postavljena infrastruktura za prevođenje
- Dodani slikovni materijali i dijagrami

### Dokumentacija
- Kreiran početni README.md s pregledom kurikuluma
- Dodani CODE_OF_CONDUCT.md i SECURITY.md
- Postavljen SUPPORT.md s uputama za pomoć
- Kreirana preliminarna struktura vodiča za učenje

## 15. travnja 2025.

### Planiranje i okvir
- Početno planiranje MCP za početnike
- Definirani ciljevi učenja i ciljana publika
- Skicirana struktura kurikuluma od 10 sekcija
- Razvijen konceptualni okvir za primjere i studije slučaja
- Kreirani prvi prototipovi primjera za ključne pojmove

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI usluge prijevoda [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili kriva tumačenja proizašla iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->