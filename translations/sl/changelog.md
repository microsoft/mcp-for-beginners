# Dnevnik sprememb: MCP za začetnike kurikulum

Ta dokument služi kot zapis vseh pomembnih sprememb, narejenih v kurikulumu Model Context Protocol (MCP) za začetnike. Spremembe so dokumentirane v obratnem kronološkem vrstnem redu (najnovejše spremembe najprej).

## 18. december 2025

### Posodobitev varnostne dokumentacije - MCP specifikacija 2025-11-25

#### Najboljše varnostne prakse MCP (02-Security/mcp-best-practices.md) - Posodobitev različice specifikacije
- **Posodobitev različice protokola**: Posodobljeno za sklicevanje na najnovejšo MCP specifikacijo 2025-11-25 (izdano 25. novembra 2025)
  - Posodobljene vse reference različice specifikacije iz 2025-06-18 na 2025-11-25
  - Posodobljene datumske reference dokumenta iz 18. avgusta 2025 na 18. december 2025
  - Preverjene vse URL-je specifikacije, da kažejo na trenutno dokumentacijo
- **Validacija vsebine**: Celovita validacija najboljših varnostnih praks glede na najnovejše standarde
  - **Microsoftove varnostne rešitve**: Preverjena trenutna terminologija in povezave za Prompt Shields (prej "odkrivanje tveganja jailbreak"), Azure Content Safety, Microsoft Entra ID in Azure Key Vault
  - **OAuth 2.1 varnost**: Potrjena usklajenost z najnovejšimi najboljšimi praksami varnosti OAuth
  - **OWASP standardi**: Validirane reference OWASP Top 10 za LLM-je ostajajo aktualne
  - **Azure storitve**: Preverjene vse povezave do Microsoft Azure dokumentacije in najboljših praks
- **Usklajenost s standardi**: Vsi navedeni varnostni standardi so potrjeni kot aktualni
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Najboljše varnostne prakse OAuth 2.1
  - Okviri za varnost in skladnost Azure
- **Viri za implementacijo**: Preverjene vse povezave do vodnikov in virov za implementacijo
  - Avtentikacijski vzorci Azure API Management
  - Vodniki za integracijo Microsoft Entra ID
  - Upravljanje skrivnosti Azure Key Vault
  - DevSecOps cevovodi in rešitve za nadzor

### Zagotavljanje kakovosti dokumentacije
- **Skladnost s specifikacijo**: Zagotovljena usklajenost vseh obveznih varnostnih zahtev MCP (MORA/MORA NE) z najnovejšo specifikacijo
- **Aktualnost virov**: Preverjene vse zunanje povezave do Microsoftove dokumentacije, varnostnih standardov in vodnikov za implementacijo
- **Pokritost najboljših praks**: Potrjena celovita pokritost avtentikacije, avtorizacije, AI-specifičnih groženj, varnosti dobavne verige in vzorcev za podjetja

## 6. oktober 2025

### Razširitev razdelka Začetek – Napredna uporaba strežnika in preprosta avtentikacija

#### Napredna uporaba strežnika (03-GettingStarted/10-advanced)
- **Dodano novo poglavje**: Predstavljen celovit vodič za napredno uporabo MCP strežnika, ki pokriva tako običajno kot nizkonivojsko strežniško arhitekturo.
  - **Običajen proti nizkonivojskemu strežniku**: Podrobna primerjava in primeri kode v Pythonu in TypeScript za oba pristopa.
  - **Oblikovanje na osnovi upravljalcev**: Razlaga upravljanja orodij/virov/promptov na osnovi upravljalcev za razširljive in prilagodljive strežniške implementacije.
  - **Praktični vzorci**: Resnični scenariji, kjer so vzorci nizkonivojskega strežnika koristni za napredne funkcije in arhitekturo.

#### Preprosta avtentikacija (03-GettingStarted/11-simple-auth)
- **Dodano novo poglavje**: Korak za korakom vodič za implementacijo preproste avtentikacije v MCP strežnikih.
  - **Koncepti avtentikacije**: Jasna razlaga razlik med avtentikacijo in avtorizacijo ter ravnanja z poverilnicami.
  - **Implementacija osnovne avtentikacije**: Vzorci avtentikacije na osnovi middleware v Pythonu (Starlette) in TypeScriptu (Express) s primeri kode.
  - **Napredovanje do napredne varnosti**: Navodila za začetek s preprosto avtentikacijo in napredovanje do OAuth 2.1 in RBAC, z referencami na napredne varnostne module.

Te dodatke nudijo praktična, neposredna navodila za gradnjo bolj robustnih, varnih in prilagodljivih MCP strežniških implementacij, ki povezujejo temeljne koncepte z naprednimi produkcijskimi vzorci.

## 29. september 2025

### MCP strežniške laboratorijske vaje za integracijo podatkovnih baz - Celovit praktični učni načrt

#### 11-MCPServerHandsOnLabs - Nov celovit kurikulum integracije podatkovnih baz
- **Celovit 13-laboratorijski učni načrt**: Dodan celovit praktični kurikulum za gradnjo produkcijsko pripravljenih MCP strežnikov z integracijo PostgreSQL podatkovne baze
  - **Resnična implementacija**: Primer uporabe Zava Retail analitike, ki prikazuje vzorce na ravni podjetja
  - **Strukturiran učni napredek**:
    - **Laboratoriji 00-03: Osnove** - Uvod, osnovna arhitektura, varnost in večnajemništvo, nastavitev okolja
    - **Laboratoriji 04-06: Gradnja MCP strežnika** - Oblikovanje baze in sheme, implementacija MCP strežnika, razvoj orodij  
    - **Laboratoriji 07-09: Napredne funkcije** - Integracija semantičnega iskanja, testiranje in odpravljanje napak, integracija z VS Code
    - **Laboratoriji 10-12: Produkcija in najboljše prakse** - Strategije uvajanja, nadzor in opazovanje, najboljše prakse in optimizacija
  - **Tehnologije za podjetja**: Okvir FastMCP, PostgreSQL s pgvector, Azure OpenAI vdelave, Azure Container Apps, Application Insights
  - **Napredne funkcije**: Varnost na ravni vrstic (RLS), semantično iskanje, večnajemniški dostop do podatkov, vektorske vdelave, nadzor v realnem času

#### Standardizacija terminologije - pretvorba modulov v laboratorije
- **Celovita posodobitev dokumentacije**: Sistematično posodobljene vse datoteke README v 11-MCPServerHandsOnLabs za uporabo terminologije "Laboratorij" namesto "Modul"
  - **Naslovi razdelkov**: Posodobljeno "Kaj ta modul pokriva" v "Kaj ta laboratorij pokriva" v vseh 13 laboratorijih
  - **Opis vsebine**: Spremenjeno "Ta modul zagotavlja..." v "Ta laboratorij zagotavlja..." po celotni dokumentaciji
  - **Učni cilji**: Posodobljeno "Do konca tega modula..." v "Do konca tega laboratorija..."
  - **Navigacijske povezave**: Pretvorjene vse reference "Modul XX:" v "Laboratorij XX:" v križnih referencah in navigaciji
  - **Sledenje dokončanju**: Posodobljeno "Po zaključku tega modula..." v "Po zaključku tega laboratorija..."
  - **Ohranjene tehnične reference**: Ohranjene Python module reference v konfiguracijskih datotekah (npr. `"module": "mcp_server.main"`)

#### Izboljšava učnega vodiča (study_guide.md)
- **Vizualna karta kurikuluma**: Dodan nov razdelek "11. Laboratoriji za integracijo podatkovnih baz" s celovito vizualizacijo strukture laboratorijev
- **Struktura repozitorija**: Posodobljeno z desetih na enajst glavnih razdelkov z podrobnim opisom 11-MCPServerHandsOnLabs
- **Navodila za učno pot**: Izboljšana navodila za navigacijo, ki pokrivajo razdelke 00-11
- **Pokritost tehnologij**: Dodani podrobnosti o integraciji FastMCP, PostgreSQL in Azure storitev
- **Učni rezultati**: Poudarek na razvoju produkcijsko pripravljenih strežnikov, vzorcih integracije podatkovnih baz in varnosti za podjetja

#### Izboljšava strukture glavnega README
- **Terminologija na osnovi laboratorijev**: Posodobljen glavni README.md v 11-MCPServerHandsOnLabs za dosledno uporabo strukture "Laboratorij"
- **Organizacija učne poti**: Jasna progresija od temeljnih konceptov preko napredne implementacije do produkcijskega uvajanja
- **Poudarek na resničnem svetu**: Poudarek na praktičnem, laboratorijskem učenju z vzorci in tehnologijami na ravni podjetja

### Izboljšave kakovosti in doslednosti dokumentacije
- **Poudarek na praktičnem učenju**: Okrepljen praktični, laboratorijski pristop skozi celotno dokumentacijo
- **Poudarek na vzorcih za podjetja**: Izpostavljene produkcijsko pripravljene implementacije in varnostne zahteve podjetij
- **Integracija tehnologij**: Celovita pokritost sodobnih Azure storitev in vzorcev integracije AI
- **Napredek učenja**: Jasna, strukturirana pot od osnovnih konceptov do produkcijskega uvajanja

## 26. september 2025

### Izboljšave študijskih primerov - Integracija GitHub MCP registra

#### Študijski primeri (09-CaseStudy/) - Poudarek na razvoju ekosistema
- **README.md**: Obsežna razširitev z obsežnim študijskim primerom GitHub MCP registra
  - **Študija primera GitHub MCP registra**: Nova obsežna študija primera, ki preučuje lansiranje GitHub MCP registra septembra 2025
    - **Analiza problema**: Podrobna analiza fragmentiranega odkrivanja in uvajanja MCP strežnikov
    - **Arhitektura rešitve**: Centraliziran pristop registra GitHub z namestitvijo z enim klikom v VS Code
    - **Poslovni vpliv**: Merljive izboljšave pri uvajanju razvijalcev in produktivnosti
    - **Strateška vrednost**: Poudarek na modularnem uvajanju agentov in interoperabilnosti med orodji
    - **Razvoj ekosistema**: Pozicioniranje kot temeljna platforma za agentno integracijo
  - **Izboljšana struktura študij primerov**: Posodobljeni vsi sedem študijskih primerov z doslednim formatiranjem in celovitimi opisi
    - Azure AI Travel Agents: Poudarek na večagentni orkestraciji
    - Azure DevOps integracija: Poudarek na avtomatizaciji delovnih tokov
    - Pridobivanje dokumentacije v realnem času: Implementacija Python konzolnega odjemalca
    - Interaktivni generator študijskega načrta: Chainlit pogovorna spletna aplikacija
    - Dokumentacija v urejevalniku: Integracija VS Code in GitHub Copilot
    - Azure API Management: Vzorci integracije API-jev za podjetja
    - GitHub MCP Registry: Razvoj ekosistema in skupnostna platforma
  - **Celovit zaključek**: Prepisan zaključni razdelek, ki poudarja sedem študij primerov, ki pokrivajo več dimenzij implementacije MCP
    - Integracija podjetij, večagentna orkestracija, produktivnost razvijalcev
    - Razvoj ekosistema, kategorizacija izobraževalnih aplikacij
    - Izboljšani vpogledi v arhitekturne vzorce, strategije implementacije in najboljše prakse
    - Poudarek na MCP kot zrelem, produkcijsko pripravljenem protokolu

#### Posodobitve učnega vodiča (study_guide.md)
- **Vizualna karta kurikuluma**: Posodobljen miselni zemljevid za vključitev GitHub MCP registra v razdelek Študijski primeri
- **Opis študijskih primerov**: Izboljšan iz generičnih opisov v podroben razčlenitev sedmih obsežnih študij primerov
- **Struktura repozitorija**: Posodobljen razdelek 10 za odražanje celovite pokritosti študij primerov s specifičnimi podrobnostmi implementacije
- **Integracija dnevnika sprememb**: Dodan vnos 26. septembra 2025, ki dokumentira dodatek GitHub MCP registra in izboljšave študij primerov
- **Posodobitve datumov**: Posodobljen časovni žig v nogi za odražanje najnovejše revizije (26. september 2025)

### Izboljšave kakovosti dokumentacije
- **Izboljšanje doslednosti**: Standardizirano formatiranje in struktura študij primerov v vseh sedmih primerih
- **Celovita pokritost**: Študije primerov zdaj pokrivajo scenarije podjetij, produktivnosti razvijalcev in razvoja ekosistema
- **Strateško pozicioniranje**: Izboljšan poudarek na MCP kot temeljni platformi za uvajanje agentnih sistemov
- **Integracija virov**: Posodobljeni dodatni viri za vključitev povezave do GitHub MCP registra

## 15. september 2025

### Razširitev naprednih tem - Prilagojeni transporti in inženiring konteksta

#### Prilagojeni transporti MCP (05-AdvancedTopics/mcp-transport/) - Nov vodič za napredno implementacijo
- **README.md**: Celovit vodič za implementacijo prilagojenih transportnih mehanizmov MCP
  - **Azure Event Grid transport**: Celovita implementacija strežnika brez strežnika, ki temelji na dogodkih
    - Primeri v C#, TypeScript in Python z integracijo Azure Functions
    - Vzorci arhitekture, ki temelji na dogodkih za razširljive rešitve MCP
    - Sprejemniki webhook in obdelava sporočil na osnovi potiska
  - **Azure Event Hubs transport**: Implementacija transporta za pretočno visoko prepustnost
    - Zmožnosti pretočnega prenosa v realnem času za scenarije z nizko zakasnitvijo
    - Strategije particioniranja in upravljanje kontrolnih točk
    - Pakiranje sporočil in optimizacija zmogljivosti
  - **Vzorci integracije podjetij**: Produkcijsko pripravljeni arhitekturni primeri
    - Porazdeljena obdelava MCP preko več Azure Functions
    - Hibridne transportne arhitekture, ki združujejo več vrst transportov
    - Strategije vzdržljivosti, zanesljivosti in obravnave napak sporočil
  - **Varnost in nadzor**: Integracija Azure Key Vault in vzorci opazovanja
    - Avtentikacija z upravljano identiteto in dostop z najmanjšimi privilegiji
    - Telemetrija Application Insights in nadzor zmogljivosti
    - Prekinitveni mehanizmi in vzorci odpornosti na napake
  - **Okviri za testiranje**: Celovite strategije testiranja za prilagojene transporte
    - Enotsko testiranje z dvojniki in ogrodji za lažno testiranje
    - Integracijsko testiranje z Azure Test Containers
    - Premisleki o testiranju zmogljivosti in obremenitve

#### Inženiring konteksta (05-AdvancedTopics/mcp-contextengineering/) - Nastajajoča disciplina AI
- **README.md**: Celovita raziskava inženiringa konteksta kot nastajajočega področja
  - **Temeljna načela**: Popolno deljenje konteksta, zavedanje odločitev o dejanjih in upravljanje kontekstnega okna
  - **Usklajenost s protokolom MCP**: Kako zasnova MCP naslavlja izzive inženiringa konteksta
    - Omejitve kontekstnega okna in strategije progresivnega nalaganja
    - Določanje relevantnosti in dinamično pridobivanje konteksta
    - Upravljanje multimodalnega konteksta in varnostni vidiki
  - **Pristopi k implementaciji**: Enonitna proti večagentnim arhitekturam
    - Razdeljevanje konteksta in tehnike prioritizacije
    - Progresivno nalaganje in strategije stiskanja konteksta
    - Večplastni pristopi in optimizacija pridobivanja
  - **Okvir za merjenje**: Nastajajoče metrike za ocenjevanje učinkovitosti konteksta
    - Učinkovitost vnosa, zmogljivost, kakovost in uporabniška izkušnja
    - Eksperimentalni pristopi k optimizaciji konteksta
    - Analiza napak in metodologije izboljšav

#### Posodobitve navigacije kurikuluma (README.md)
- **Izboljšana struktura modulov**: Posodobljena tabela kurikuluma za vključitev novih naprednih tem
  - Dodani vnosi Inženiring konteksta (5.14) in Prilagojeni transport (5.15)
  - Dosledno formatiranje in navigacijske povezave v vseh modulih
  - Posodobljeni opisi za odražanje trenutnega obsega vsebine

### Izboljšave strukture imenikov
- **Standardizacija imen**: Preimenovan "mcp transport" v "mcp-transport" za skladnost z ostalimi mapami naprednih tem
- **Organizacija vsebine**: Vse mape 05-AdvancedTopics zdaj sledijo doslednemu vzorcu imen (mcp-[tema])

### Izboljšave kakovosti dokumentacije
- **Usklajenost s specifikacijo MCP**: Vsa nova vsebina se sklicuje na trenutno MCP specifikacijo 2025-06-18
- **Primeri v več jezikih**: Celoviti primeri kode v C#, TypeScript in Python
- **Poudarek na podjetjih**: Produkcijsko pripravljeni vzorci in integracija Azure oblaka skozi celotno vsebino
- **Vizualna dokumentacija**: Diagrami Mermaid za vizualizacijo arhitekture in poteka

## 18. avgust 2025

### Celovita posodobitev dokumentacije - Standardi MCP 2025-06-18

#### Najboljše varnostne prakse MCP (02-Security/) - Popolna modernizacija
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Popolna predelava usklajena z MCP specifikacijo 2025-06-18
  - **Obvezne zahteve**: Dodane eksplicitne zahteve MORA/MORA NE iz uradne specifikacije z jasnimi vizualnimi indikatorji
  - **12 osnovnih varnostnih praks**: Prestrukturirano s seznama 15 elementov v celovite varnostne domene
    - Varnost žetonov in avtentikacija z integracijo zunanjega ponudnika identitete
    - Upravljanje sej in varnost prenosa s kriptografskimi zahtevami
    - Zaščita pred grožnjami, specifičnimi za AI, z integracijo Microsoft Prompt Shields
    - Nadzor dostopa in dovoljenja s principom najmanjših privilegijev
    - Varnost vsebine in nadzor z integracijo Azure Content Safety
    - Varnost dobavne verige s celovito verifikacijo komponent
    - Varnost OAuth in preprečevanje zmede zastopnika z implementacijo PKCE
    - Odziv na incidente in okrevanje z avtomatiziranimi zmogljivostmi
    - Skladnost in upravljanje z usklajenostjo z regulativami
    - Napredni varnostni nadzor z arhitekturo ničelnega zaupanja
    - Integracija Microsoftovega varnostnega ekosistema s celovitimi rešitvami
    - Neprestana varnostna evolucija z adaptivnimi praksami
  - **Microsoftove varnostne rešitve**: Izboljšana navodila za integracijo Prompt Shields, Azure Content Safety, Entra ID in GitHub Advanced Security
  - **Viri za implementacijo**: Kategorizirani celoviti povezavi do virov po uradni MCP dokumentaciji, Microsoftovih varnostnih rešitvah, varnostnih standardih in vodičih za implementacijo

#### Napredni varnostni nadzor (02-Security/) - Implementacija za podjetja
- **MCP-SECURITY-CONTROLS-2025.md**: Popolna prenova z varnostnim okvirom za podjetja
  - **9 celovitih varnostnih domen**: Razširjeno iz osnovnih nadzorov v podroben okvir za podjetja
    - Napredna avtentikacija in avtorizacija z integracijo Microsoft Entra ID
    - Varnost žetonov in nadzor proti prehodu z obsežno validacijo
    - Nadzor varnosti sej s preprečevanjem prevzema
    - AI-specifični varnostni nadzori s preprečevanjem vbrizgavanja pozivov in zastrupitve orodij
    - Preprečevanje napadov z zmedenim zastopnikom z varnostjo OAuth proxyja
    - Varnost izvajanja orodij s peskovnikom in izolacijo
    - Nadzor varnosti dobavne verige z verifikacijo odvisnosti
    - Nadzor in zaznavanje z integracijo SIEM
    - Odziv na incidente in okrevanje z avtomatiziranimi zmogljivostmi
  - **Primeri implementacije**: Dodani podrobni YAML konfiguracijski bloki in primeri kode
  - **Integracija Microsoftovih rešitev**: Celovito pokritje Azure varnostnih storitev, GitHub Advanced Security in upravljanja identitet za podjetja

#### Napredne varnostne teme (05-AdvancedTopics/mcp-security/) - Implementacija pripravljena za produkcijo
- **README.md**: Popolna predelava za implementacijo varnosti v podjetjih
  - **Usklajenost s trenutno specifikacijo**: Posodobljeno na MCP Specifikacijo 2025-06-18 z obveznimi varnostnimi zahtevami
  - **Izboljšana avtentikacija**: Integracija Microsoft Entra ID z obsežnimi primeri za .NET in Java Spring Security
  - **Integracija AI varnosti**: Implementacija Microsoft Prompt Shields in Azure Content Safety z podrobnimi primeri v Pythonu
  - **Napredna ublažitev groženj**: Celoviti primeri implementacije za
    - Preprečevanje napadov z zmedenim zastopnikom z PKCE in validacijo uporabniškega soglasja
    - Preprečevanje prehoda žetonov z validacijo občinstva in varnim upravljanjem žetonov
    - Preprečevanje prevzema sej s kriptografskim vezanjem in vedenjsko analizo
  - **Integracija varnosti za podjetja**: Nadzor z Azure Application Insights, cevovodi za zaznavanje groženj in varnost dobavne verige
  - **Kontrolni seznam implementacije**: Jasna ločitev obveznih in priporočenih varnostnih nadzorov z ugodnostmi Microsoftovega varnostnega ekosistema

### Kakovost dokumentacije in usklajenost s standardi
- **Reference specifikacij**: Posodobljene vse reference na trenutno MCP Specifikacijo 2025-06-18
- **Microsoftov varnostni ekosistem**: Izboljšana navodila za integracijo v celotni varnostni dokumentaciji
- **Praktična implementacija**: Dodani podrobni primeri kode v .NET, Java in Python z vzorci za podjetja
- **Organizacija virov**: Celovita kategorizacija uradne dokumentacije, varnostnih standardov in vodičev za implementacijo
- **Vizualni indikatorji**: Jasno označevanje obveznih zahtev v primerjavi s priporočenimi praksami


#### Osnovni koncepti (01-CoreConcepts/) - Popolna modernizacija
- **Posodobitev različice protokola**: Posodobljeno za referenco na trenutno MCP Specifikacijo 2025-06-18 z datumskim verzioniranjem (format LLLL-MM-DD)
- **Izboljšava arhitekture**: Izboljšani opisi gostiteljev, odjemalcev in strežnikov za odsev trenutnih arhitekturnih vzorcev MCP
  - Gostitelji so zdaj jasno definirani kot AI aplikacije, ki usklajujejo več MCP odjemalskih povezav
  - Odjemalci opisani kot protokolarni priključki, ki vzdržujejo en-na-en strežniške povezave
  - Strežniki izboljšani z lokalnimi in oddaljenimi scenariji nameščanja
- **Prenova primitivov**: Popolna prenova strežniških in odjemalskih primitivov
  - Strežniški primitiv: Viri (viri podatkov), Pozivi (predloge), Orodja (izvedljive funkcije) z podrobnimi razlagami in primeri
  - Odjemalski primitiv: Vzorcevanje (LLM zaključki), Izvabljanje (uporabniški vnos), Beleženje (razhroščevanje/nadzor)
  - Posodobljeno z aktualnimi vzorci metod za odkrivanje (`*/list`), pridobivanje (`*/get`) in izvajanje (`*/call`)
- **Arhitektura protokola**: Uveden dvoplastni arhitekturni model
  - Podatkovna plast: Temelj JSON-RPC 2.0 z upravljanjem življenjskega cikla in primitivov
  - Transportna plast: STDIO (lokalno) in Streamable HTTP s SSE (oddaljeno) transportnimi mehanizmi
- **Varnostni okvir**: Celoviti varnostni principi, vključno z eksplicitnim uporabniškim soglasjem, zaščito zasebnosti podatkov, varnostjo izvajanja orodij in varnostjo transportne plasti
- **Vzorce komunikacije**: Posodobljena protokolarna sporočila za prikaz inicializacije, odkrivanja, izvajanja in obveščanja
- **Primeri kode**: Osveženi večjezični primeri (.NET, Java, Python, JavaScript) za odsev trenutnih vzorcev MCP SDK

#### Varnost (02-Security/) - Celovita prenova varnosti  
- **Usklajenost s standardi**: Popolna uskladitev z varnostnimi zahtevami MCP Specifikacije 2025-06-18
- **Evolucija avtentikacije**: Dokumentirana evolucija od lastnih OAuth strežnikov do delegacije zunanjega ponudnika identitete (Microsoft Entra ID)
- **Analiza groženj, specifičnih za AI**: Izboljšano pokrivanje sodobnih AI napadov
  - Podrobni scenariji napadov z vbrizgavanjem pozivov z resničnimi primeri
  - Mehanizmi zastrupitve orodij in vzorci napadov "rug pull"
  - Zastrupitev kontekstnega okna in napadi z zmedo modela
- **Microsoftove AI varnostne rešitve**: Celovito pokritje Microsoftovega varnostnega ekosistema
  - AI Prompt Shields z napredno detekcijo, osvetlitvijo in tehnikami ločil
  - Vzorci integracije Azure Content Safety
  - GitHub Advanced Security za zaščito dobavne verige
- **Napredna ublažitev groženj**: Podrobni varnostni nadzori za
  - Prevzem sej z MCP-specifičnimi scenariji napadov in kriptografskimi zahtevami za ID seje
  - Težave z zmedenim zastopnikom v MCP proxy scenarijih z eksplicitnimi zahtevami za soglasje
  - Ranljivosti prehoda žetonov z obveznimi validacijskimi nadzori
- **Varnost dobavne verige**: Razširjeno pokrivanje AI dobavne verige, vključno z osnovnimi modeli, storitvami vdelav, ponudniki konteksta in API-ji tretjih oseb
- **Varnost temeljev**: Izboljšana integracija z varnostnimi vzorci za podjetja, vključno z arhitekturo ničelnega zaupanja in Microsoftovim varnostnim ekosistemom
- **Organizacija virov**: Kategorizirane celovite povezave do virov po tipu (uradna dokumentacija, standardi, raziskave, Microsoftove rešitve, vodiči za implementacijo)

### Izboljšave kakovosti dokumentacije
- **Strukturirani učni cilji**: Izboljšani učni cilji s specifičnimi, izvedljivimi rezultati
- **Medsebojne reference**: Dodane povezave med povezanimi varnostnimi in osnovnimi temami
- **Aktualne informacije**: Posodobljene vse datumske reference in povezave na specifikacije za trenutne standarde
- **Navodila za implementacijo**: Dodana specifična, izvedljiva navodila za implementacijo v obeh razdelkih

## 16. julij 2025

### Izboljšave README in navigacije
- Popolnoma prenovljena navigacija kurikuluma v README.md
- Zamenjani `<details>` oznake z bolj dostopnim tabelaričnim formatom
- Ustvarjene alternativne postavitve v novi mapi "alternative_layouts"
- Dodani primeri navigacije v obliki kartic, zavihkov in harmonike
- Posodobljen razdelek o strukturi repozitorija z vsemi najnovejšimi datotekami
- Izboljšan razdelek "Kako uporabljati ta kurikulum" z jasnimi priporočili
- Posodobljene povezave do MCP specifikacij na pravilne URL-je
- Dodan razdelek o inženiringu konteksta (5.14) v strukturo kurikuluma

### Posodobitve študijskega vodiča
- Popolnoma prenovljen študijski vodič za uskladitev s trenutno strukturo repozitorija
- Dodani novi razdelki za MCP odjemalce in orodja ter priljubljene MCP strežnike
- Posodobljena vizualna karta kurikuluma za natančen prikaz vseh tem
- Izboljšani opisi naprednih tem za pokritje vseh specializiranih področij
- Posodobljen razdelek študijskih primerov za odsev dejanskih primerov
- Dodan ta celovit dnevnik sprememb

### Prispevki skupnosti (06-CommunityContributions/)
- Dodane podrobne informacije o MCP strežnikih za generiranje slik
- Dodan celovit razdelek o uporabi Claude v VSCode
- Dodana navodila za nastavitev in uporabo terminalskega odjemalca Cline
- Posodobljen razdelek MCP odjemalcev z vsemi priljubljenimi možnostmi
- Izboljšani primeri prispevkov z natančnejšimi vzorci kode

### Napredne teme (05-AdvancedTopics/)
- Organizirane vse specializirane mape tem z doslednim poimenovanjem
- Dodani materiali in primeri za inženiring konteksta
- Dodana dokumentacija za integracijo agenta Foundry
- Izboljšana dokumentacija integracije varnosti Entra ID

## 11. junij 2025

### Začetna ustvaritev
- Izšla prva različica kurikuluma MCP za začetnike
- Ustvarjena osnovna struktura za vseh 10 glavnih razdelkov
- Implementirana vizualna karta kurikuluma za navigacijo
- Dodani začetni vzorčni projekti v več programskih jezikih

### Začetek dela (03-GettingStarted/)
- Ustvarjeni prvi primeri implementacije strežnika
- Dodana navodila za razvoj odjemalcev
- Vključena navodila za integracijo LLM odjemalcev
- Dodana dokumentacija za integracijo VS Code
- Implementirani primeri strežnikov z dogodki, ki jih pošilja strežnik (SSE)

### Osnovni koncepti (01-CoreConcepts/)
- Dodan podroben opis arhitekture odjemalec-strežnik
- Ustvarjena dokumentacija o ključnih komponentah protokola
- Dokumentirani vzorci sporočil v MCP

## 23. maj 2025

### Struktura repozitorija
- Inicializiran repozitorij z osnovno strukturo map
- Ustvarjene README datoteke za vsak glavni razdelek
- Nastavljena infrastruktura za prevajanje
- Dodani slikovni viri in diagrami

### Dokumentacija
- Ustvarjen začetni README.md s pregledom kurikuluma
- Dodani CODE_OF_CONDUCT.md in SECURITY.md
- Nastavljen SUPPORT.md z navodili za pomoč
- Ustvarjena preliminarna struktura študijskega vodiča

## 15. april 2025

### Načrtovanje in okvir
- Začetno načrtovanje kurikuluma MCP za začetnike
- Določeni učni cilji in ciljna publika
- Opisana struktura kurikuluma v 10 razdelkih
- Razvit konceptualni okvir za primere in študije primerov
- Ustvarjeni začetni prototipni primeri za ključne koncepte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->