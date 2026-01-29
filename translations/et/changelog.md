# Muudatuste logi: MCP algajatele õppekava

See dokument toimib kõigi Model Context Protocol (MCP) algajatele õppekava oluliste muudatuste registrina. Muudatused on dokumenteeritud pööratud kronoloogilises järjekorras (uusimad muudatused ees).

## 18. detsember 2025

### Turvalisuse dokumentatsiooni uuendus - MCP spetsifikatsioon 2025-11-25

#### MCP turvalisuse parimad tavad (02-Security/mcp-best-practices.md) - spetsifikatsiooni versiooni uuendus
- **Protokolli versiooni uuendus**: Uuendatud viited uusimale MCP spetsifikatsioonile 2025-11-25 (välja antud 25. novembril 2025)
  - Uuendatud kõik spetsifikatsiooni versiooni viited 2025-06-18 pealt 2025-11-25 peale
  - Uuendatud dokumendi kuupäeva viited 18. august 2025 pealt 18. detsember 2025 peale
  - Kontrollitud, et kõik spetsifikatsiooni URL-id osutavad kehtivale dokumentatsioonile
- **Sisu valideerimine**: Turvalisuse parimate tavade põhjalik valideerimine vastavalt uusimatele standarditele
  - **Microsofti turvalahendused**: Kontrollitud kehtivad terminid ja lingid Prompt Shields (varem "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID ja Azure Key Vaulti kohta
  - **OAuth 2.1 turvalisus**: Kinnitatud vastavus uusimatele OAuth turvalisuse parimatele tavadele
  - **OWASP standardid**: Kontrollitud, et OWASP Top 10 LLM-ide jaoks on ajakohane
  - **Azure teenused**: Kontrollitud kõik Microsoft Azure dokumentatsiooni lingid ja parimad tavad
- **Standardite vastavus**: Kõik viidatud turvastandardid on ajakohased
  - NIST AI riskijuhtimise raamistik
  - ISO 27001:2022
  - OAuth 2.1 turvalisuse parimad tavad
  - Azure turva- ja vastavusraamistikud
- **Rakendamise ressursid**: Kontrollitud kõik rakendamisjuhiste lingid ja ressursid
  - Azure API halduse autentimismustrid
  - Microsoft Entra ID integratsiooni juhendid
  - Azure Key Vaulti saladuste haldus
  - DevSecOps torujuhtmed ja jälgimislahendused

### Dokumentatsiooni kvaliteedi tagamine
- **Spetsifikatsiooni nõuete täitmine**: Tagatud, et kõik kohustuslikud MCP turvanõuded (PEAB/PEAB MITTE) vastavad uusimale spetsifikatsioonile
- **Ressursside ajakohasus**: Kontrollitud kõik välised lingid Microsofti dokumentatsiooni, turvastandardite ja rakendamisjuhiste juurde
- **Parimate tavade katvus**: Kinnitatud autentimise, autoriseerimise, AI-spetsiifiliste ohtude, tarneahela turvalisuse ja ettevõtte mustrite põhjalik käsitlus

## 6. oktoober 2025

### Alustamise jaotise laiendus – Täiustatud serverikasutus ja lihtne autentimine

#### Täiustatud serverikasutus (03-GettingStarted/10-advanced)
- **Uus peatükk lisatud**: Esitatud põhjalik juhend täiustatud MCP serveri kasutamiseks, hõlmates nii tavalist kui madala taseme serveri arhitektuuri.
  - **Tavaline vs madala taseme server**: Üksikasjalik võrdlus ja koodinäited Pythonis ja TypeScriptis mõlema lähenemise kohta.
  - **Handler-põhine disain**: Selgitus tööriistade/resursside/käskude haldamisest handlerite kaudu skaleeritavate ja paindlike serverite rakendamiseks.
  - **Praktilised mustrid**: Reaalmaailma stsenaariumid, kus madala taseme serveri mustrid on kasulikud täiustatud funktsioonide ja arhitektuuri jaoks.

#### Lihtne autentimine (03-GettingStarted/11-simple-auth)
- **Uus peatükk lisatud**: Samm-sammuline juhend lihtsa autentimise rakendamiseks MCP serverites.
  - **Autentimise kontseptsioonid**: Selge selgitus autentimise ja autoriseerimise erinevusest ning volituste käsitlemisest.
  - **Põhilise autentimise rakendamine**: Middleware-põhised autentimismustrid Pythonis (Starlette) ja TypeScriptis (Express), koos koodinäidetega.
  - **Edasijõudmine täiustatud turvalisusse**: Juhised lihtsast autentimisest alustamiseks ja edasi liikumiseks OAuth 2.1 ja RBAC suunas, viidetega täiustatud turvamoodulitele.

Need lisad pakuvad praktilist, käed-külge juhendit tugevamate, turvalisemate ja paindlikumate MCP serverite ehitamiseks, ühendades põhikontseptsioonid täiustatud tootmismustritega.

## 29. september 2025

### MCP serveri andmebaasi integratsiooni laborid – põhjalik praktiline õppeprogramm

#### 11-MCPServerHandsOnLabs – uus täielik andmebaasi integratsiooni õppekava
- **Täielik 13-labori õppeprogramm**: Lisatud põhjalik praktiline õppekava tootmisvalmis MCP serverite ehitamiseks PostgreSQL andmebaasi integratsiooniga
  - **Reaalmaailma rakendus**: Zava Retail analüütika kasutusjuht, mis demonstreerib ettevõtte taseme mustreid
  - **Struktureeritud õppeprotsess**:
    - **Laborid 00-03: Alused** – Sissejuhatus, põhiarhitektuur, turvalisus ja mitmekasutajalisus, keskkonna seadistamine
    - **Laborid 04-06: MCP serveri ehitamine** – Andmebaasi disain ja skeem, MCP serveri rakendamine, tööriistade arendus
    - **Laborid 07-09: Täiustatud funktsioonid** – Semantiline otsing, testimine ja silumine, VS Code integratsioon
    - **Laborid 10-12: Tootmine ja parimad tavad** – Paigaldusstrateegiad, jälgimine ja vaatlus, parimad tavad ja optimeerimine
  - **Ettevõtte tehnoloogiad**: FastMCP raamistik, PostgreSQL koos pgvectoriga, Azure OpenAI manused, Azure Container Apps, Application Insights
  - **Täiustatud funktsioonid**: Rea taseme turvalisus (RLS), semantiline otsing, mitmekasutajaliidesega andmejuurdepääs, vektormanused, reaalajas jälgimine

#### Terminoloogia standardiseerimine – mooduli asendamine laboriga
- **Põhjalik dokumentatsiooni uuendus**: Süsteemne kõigi README failide uuendamine 11-MCPServerHandsOnLabs kaustas, kasutades "Labor" terminoloogiat "Mooduli" asemel
  - **Jaotise päised**: Muudetud "What This Module Covers" pealkirjadeks "What This Lab Covers" kõigis 13 laboris
  - **Sisu kirjeldus**: Muudetud "This module provides..." vormingus "This lab provides..." kogu dokumentatsioonis
  - **Õpieesmärgid**: Uuendatud "By the end of this module..." vormingus "By the end of this lab..."
  - **Navigatsioonilingid**: Kõik "Module XX:" viited muudetud "Lab XX:" vormingusse ristviidetes ja navigeerimises
  - **Lõpetamise jälgimine**: Uuendatud "After completing this module..." vormingus "After completing this lab..."
  - **Tehniliste viidete säilitamine**: Säilitatud Python mooduli viited konfiguratsioonifailides (nt `"module": "mcp_server.main"`)

#### Õppejuhendi täiustamine (study_guide.md)
- **Visuaalne õppekava kaart**: Lisatud uus jaotis "11. Andmebaasi integratsiooni laborid" koos põhjaliku laboristruktuuri visualiseeringuga
- **Repositooriumi struktuur**: Uuendatud kümnest üheteistkümneks põhijaotuseks koos detailse 11-MCPServerHandsOnLabs kirjeldusega
- **Õpperaja juhised**: Täiustatud navigeerimisjuhised jaotiste 00-11 katmiseks
- **Tehnoloogiate katvus**: Lisatud FastMCP, PostgreSQL ja Azure teenuste integratsiooni detailid
- **Õpitulemused**: Rõhutatud tootmisvalmis serveri arendamist, andmebaasi integratsiooni mustreid ja ettevõtte turvalisust

#### Peamise README struktuuri täiustamine
- **Laboripõhine terminoloogia**: Uuendatud 11-MCPServerHandsOnLabs peamist README.md faili järjepidevalt kasutama "Labor" struktuuri
- **Õpperaja organiseerimine**: Selge edenemine aluspõhimõtetest läbi täiustatud rakenduse tootmisse viimiseni
- **Reaalmaailma fookus**: Rõhk praktilisel, käed-külge õppel koos ettevõtte taseme mustrite ja tehnoloogiatega

### Dokumentatsiooni kvaliteedi ja järjepidevuse parandused
- **Praktilise õppe rõhutamine**: Tugevdatud praktiline, laboripõhine lähenemine kogu dokumentatsioonis
- **Ettevõtte mustrite fookus**: Esile toodud tootmisvalmis rakendused ja ettevõtte turvalisuse kaalutlused
- **Tehnoloogia integratsioon**: Põhjalik kaasaegsete Azure teenuste ja AI integratsioonimustrite katvus
- **Õppeprotsessi edenemine**: Selge, struktureeritud tee aluspõhimõtetest tootmisse viimiseni

## 26. september 2025

### Juhtumiuuringute täiustamine – GitHub MCP registri integratsioon

#### Juhtumiuuringud (09-CaseStudy/) – ökosüsteemi arenduse fookus
- **README.md**: Suur laiendus põhjaliku GitHub MCP registri juhtumiuuringuga
  - **GitHub MCP registri juhtumiuuring**: Uus põhjalik juhtumiuuring, mis käsitleb GitHubi MCP registri käivitamist 2025. aasta septembris
    - **Probleemi analüüs**: Üksikasjalik ülevaade killustatud MCP serverite avastamise ja juurutamise väljakutsetest
    - **Lahenduse arhitektuur**: GitHubi tsentraliseeritud registri lähenemine ühe klõpsuga VS Code installatsiooniga
    - **Äriline mõju**: Mõõdetavad parendused arendajate sisseelamisel ja tootlikkuses
    - **Strateegiline väärtus**: Fookus modulaarsele agendi juurutamisele ja tööriistadevahelisele koostalitlusvõimele
    - **Ökosüsteemi areng**: Positsioneerimine agentuurse integratsiooni aluseks platvormiks
  - **Täiendatud juhtumiuuringute struktuur**: Uuendatud kõik seitse juhtumiuuringut järjepideva vormingu ja põhjalike kirjeldustega
    - Azure AI reisibüroo agendid: mitme agendi orkestreerimise rõhutamine
    - Azure DevOps integratsioon: töövoo automatiseerimise fookus
    - Reaalajas dokumentatsiooni päring: Python konsooliklient
    - Interaktiivne õppekava generaator: Chainlit vestlusveebirakendus
    - Redaktori sees dokumentatsioon: VS Code ja GitHub Copilot integratsioon
    - Azure API haldus: ettevõtte API integratsiooni mustrid
    - GitHub MCP registri ökosüsteemi areng ja kogukonna platvorm
  - **Põhjalik kokkuvõte**: Ümber kirjutatud kokkuvõtte jaotis, mis rõhutab seitset juhtumiuuringut, mis hõlmavad mitmeid MCP rakenduse aspekte
    - Ettevõtte integratsioon, mitme agendi orkestreerimine, arendajate tootlikkus
    - Ökosüsteemi areng, hariduslikud rakendused
    - Täiustatud ülevaated arhitektuurimustritest, rakendamisstrateegiatest ja parimatest tavadest
    - Rõhk MCP-le kui küpselt tootmisvalmis protokollile

#### Õppejuhendi uuendused (study_guide.md)
- **Visuaalne õppekava kaart**: Uuendatud mõttekaart, lisades GitHub MCP registri juhtumiuuringute jaotisesse
- **Juhtumiuuringute kirjeldus**: Täiustatud üldistest kirjeldustest detailseks seitsme põhjaliku juhtumiuuringu jaotuseks
- **Repositooriumi struktuur**: Uuendatud jaotis 10, et kajastada põhjalikku juhtumiuuringute katvust koos spetsiifiliste rakendusdetailidega
- **Muudatuste logi integreerimine**: Lisatud 26. septembri 2025 sissekanne, mis dokumenteerib GitHub MCP registri lisamise ja juhtumiuuringute täiustused
- **Kuupäeva uuendused**: Uuendatud jaluse ajatemplit, et kajastada viimast revisjoni (26. september 2025)

### Dokumentatsiooni kvaliteedi parandused
- **Järjepidevuse tugevdamine**: Standardiseeritud juhtumiuuringute vorming ja struktuur kõigi seitsme näite puhul
- **Põhjalik katvus**: Juhtumiuuringud hõlmavad nüüd ettevõtte, arendajate tootlikkuse ja ökosüsteemi arenduse stsenaariume
- **Strateegiline positsioneerimine**: Täiustatud fookus MCP-le kui agentuurse süsteemi juurutamise aluseks platvormile
- **Ressursside integreerimine**: Uuendatud täiendavad ressursid, lisades GitHub MCP registri lingi

## 15. september 2025

### Täiustatud teemade laiendus – kohandatud transpordid ja konteksti inseneriteadus

#### MCP kohandatud transpordid (05-AdvancedTopics/mcp-transport/) – uus täiustatud rakendamisjuhend
- **README.md**: Täielik juhend kohandatud MCP transpordimehhanismide rakendamiseks
  - **Azure Event Grid transpordi**: Põhjalik serverivaba sündmuspõhise transpordi rakendus
    - C#, TypeScript ja Python näited Azure Functions integratsiooniga
    - Sündmuspõhised arhitektuurimustrid skaleeritavate MCP lahenduste jaoks
    - Webhook vastuvõtjad ja push-põhine sõnumite käsitlemine
  - **Azure Event Hubs transpordi**: Kõrge läbilaskevõimega voogedastuse transpordi rakendus
    - Reaalajas voogedastuse võimalused madala latentsusega stsenaariumides
    - Partitsioneerimise strateegiad ja kontrollpunktide haldus
    - Sõnumite partiide töötlemine ja jõudluse optimeerimine
  - **Ettevõtte integratsiooni mustrid**: Tootmisvalmis arhitektuuri näited
    - Hajutatud MCP töötlemine mitme Azure Functioni vahel
    - Hübriidtranspordi arhitektuurid, mis ühendavad mitut transporditüüpi
    - Sõnumite vastupidavus, usaldusväärsus ja veakäsitluse strateegiad
  - **Turvalisus ja jälgimine**: Azure Key Vault integratsioon ja vaatlusmustrid
    - Halduse identiteedi autentimine ja minimaalsete õiguste juurdepääs
    - Application Insights telemeetria ja jõudluse jälgimine
    - Lülitite ja tõrketaluvuse mustrid
  - **Testimisraamistikud**: Põhjalikud testimisstrateegiad kohandatud transpordile
    - Ühiktestimine testtopside ja mockimise raamistikuga
    - Integratsioonitestimine Azure Test Containers abil
    - Jõudluse ja koormustestimise kaalutlused

#### Konteksti inseneriteadus (05-AdvancedTopics/mcp-contextengineering/) – tekkiv AI distsipliin
- **README.md**: Põhjalik uurimus konteksti inseneriteadusest kui tekkivast valdkonnast
  - **Põhiprintsiibid**: Täielik konteksti jagamine, tegevuse otsustamise teadlikkus ja konteksti akna haldus
  - **MCP protokolli vastavus**: Kuidas MCP disain lahendab konteksti inseneriteaduse väljakutseid
    - Konteksti akna piirangud ja progressiivse laadimise strateegiad
    - Asjakohasuse määramine ja dünaamiline konteksti päring
    - Mitmemodaalne konteksti käsitlemine ja turvaküsimused
  - **Rakendamisviisid**: Ühe lõime vs mitme agendi arhitektuurid
    - Konteksti tükkideks jagamine ja prioriseerimise tehnikad
    - Progressiivne konteksti laadimine ja kokkusurumise strateegiad
    - Kihtidepõhised konteksti lähenemised ja päringu optimeerimine
  - **Mõõtmise raamistik**: Tekkivad mõõdikud konteksti tõhususe hindamiseks
    - Sisendi efektiivsus, jõudlus, kvaliteet ja kasutajakogemuse kaalutlused
    - Eksperimentaalsed lähenemised konteksti optimeerimiseks
    - Ebaõnnestumiste analüüs ja parendusmeetodid

#### Õppekava navigeerimise uuendused (README.md)
- **Täiustatud moodulistruktuur**: Uuendatud õppekava tabel, lisades uued täiustatud teemad
  - Lisatud Konteksti inseneriteadus (5.14) ja Kohandatud transpordi (5.15) kirjed
  - Järjepidev vormindus ja navigeerimislingid kõigis moodulites
  - Uuendatud kirjeldused, mis kajastavad praegust sisuala

### Kaustastruktuuri parandused
- **Nimede standardiseerimine**: Muudetud "mcp transport" kausta nimi "mcp-transport" vormingusse, et olla kooskõlas teiste täiustatud teemade kaustadega
- **Sisu organiseerimine**: Kõik 05-AdvancedTopics kaustad järgivad nüüd järjepidevat nimetamisstiili (mcp-[teema])

### Dokumentatsiooni kvaliteedi täiustused
- **MCP spetsifikatsiooni vastavus**: Kõik uus sisu viitab MCP spetsifikatsioonile 2025-06-18
- **Mitmekeelsete näidete kaasamine**: Põhjalikud koodinäited C#, TypeScripti ja Pythoni keeltes
- **Ettevõtte fookus**: Tootmisvalmis mustrid ja Azure pilve integratsioon kogu ulatuses
- **Visuaalne dokumentatsioon**: Mermaid diagrammid arhitektuuri ja voogude visualiseerimiseks

## 18. august 2025

### Dokumentatsiooni põhjalik uuendus – MCP 2025-06-18 standardid

#### MCP turvalisuse parimad tavad (02-Security/) – täielik moderniseerimine
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täielik ümberkirjutus, mis vastab MCP spetsifikatsioonile 2025-06-18
  - **Kohustuslikud nõuded**: Lisatud ametlikust spetsifikatsioonist selged PEAB/PEAB MITTE nõuded koos visuaalsete indikaatoritega
  - **12 põhiturvalisuse tava**: Ümber korraldatud 15-punktilisest loendist põhjalikeks turvalisuse valdkondadeks
    - Tokeni turvalisus ja autentimine välise identiteedipakkuja integratsiooniga
    - Sessioonihaldus ja transporditurvalisus krüptograafiliste nõuetega
    - AI-spetsiifiline ohtude kaitse Microsoft Prompt Shieldsi integratsiooniga
    - Juurdepääsukontroll ja õigused põhimõttega minimaalsetest privileegidest
    - Sisu turvalisus ja jälgimine Azure Content Safety integratsiooniga
    - Tarneahela turvalisus põhjaliku komponentide kontrolliga
    - OAuth turvalisus ja Confused Deputy ennetus PKCE rakendusega
    - Intsidendihaldus ja taastumine automatiseeritud võimekusega
    - Vastavus ja haldus regulatiivse kooskõla tagamiseks
    - Täiustatud turvakontrollid null usalduse arhitektuuriga
    - Microsofti turvalisuse ökosüsteemi integratsioon põhjalike lahendustega
    - Jätkuv turvalisuse areng kohanduvate tavadega
  - **Microsofti turvalahendused**: Täiustatud integratsioonijuhised Prompt Shieldsi, Azure Content Safety, Entra ID ja GitHub Advanced Security jaoks
  - **Rakendamise ressursid**: Kategooriate kaupa põhjalikud ressursilingid ametliku MCP dokumentatsiooni, Microsofti turvalahenduste, turvastandardite ja rakendamisjuhendite alla

#### Täiustatud turvakontrollid (02-Security/) - Ettevõtte rakendus
- **MCP-SECURITY-CONTROLS-2025.md**: Täielik ümberkujundus ettevõtte taseme turvaraamistikuga
  - **9 põhjalikku turvalisuse valdkonda**: Laiendatud põhilistest kontrollidest detailse ettevõtte raamistikuni
    - Täiustatud autentimine ja autoriseerimine Microsoft Entra ID integratsiooniga
    - Tokeni turvalisus ja anti-passthrough kontrollid põhjaliku valideerimisega
    - Sessiooniturbe kontrollid kaaperdamise ennetamiseks
    - AI-spetsiifilised turbekontrollid prompt süstimise ja tööriistamürgituse ennetamiseks
    - Confused Deputy rünnaku ennetus OAuth-proxy turvalisusega
    - Tööriistade täitmise turvalisus liivakasti ja isoleerimisega
    - Tarneahela turbekontrollid sõltuvuste kontrolliga
    - Jälgimise ja avastamise kontrollid SIEM integratsiooniga
    - Intsidendihaldus ja taastumine automatiseeritud võimekusega
  - **Rakendamise näited**: Lisatud detailseid YAML konfiguratsiooniplokke ja koodinäiteid
  - **Microsofti lahenduste integratsioon**: Põhjalik ülevaade Azure turvateenustest, GitHub Advanced Securityst ja ettevõtte identiteedihaldusest

#### Täiustatud teemade turvalisus (05-AdvancedTopics/mcp-security/) - Tootmiseks valmis rakendus
- **README.md**: Täielik ümberkirjutus ettevõtte turvalisuse rakendamiseks
  - **Praeguse spetsifikatsiooni kooskõla**: Uuendatud MCP spetsifikatsioonile 2025-06-18 koos kohustuslike turvanõuetega
  - **Täiustatud autentimine**: Microsoft Entra ID integratsioon koos põhjalike .NET ja Java Spring Security näidetega
  - **AI turvalisuse integratsioon**: Microsoft Prompt Shieldsi ja Azure Content Safety rakendamine detailsete Python näidetega
  - **Täiustatud ohtude leevendus**: Põhjalikud rakendamisnäited
    - Confused Deputy rünnaku ennetus PKCE ja kasutaja nõusoleku valideerimisega
    - Tokeni läbipääsu ennetus sihtrühma valideerimise ja turvalise tokenihaldusega
    - Sessiooni kaaperdamise ennetus krüptograafilise sidumise ja käitumusanalüüsiga
  - **Ettevõtte turvalisuse integratsioon**: Azure Application Insights jälgimine, ohu avastamise torujuhtmed ja tarneahela turvalisus
  - **Rakendamise kontrollnimekiri**: Selged kohustuslikud vs soovituslikud turvakontrollid Microsofti turvaökosüsteemi eelistega

### Dokumentatsiooni kvaliteet ja standardite kooskõla
- **Spetsifikatsiooni viited**: Uuendatud kõik viited praegusele MCP spetsifikatsioonile 2025-06-18
- **Microsofti turvaökosüsteem**: Täiustatud integratsioonijuhised kogu turvadokumentatsioonis
- **Praktiline rakendamine**: Lisatud detailseid koodinäiteid .NET, Java ja Python keeles ettevõtte mustritega
- **Ressursside organiseerimine**: Põhjalik ametliku dokumentatsiooni, turvastandardite ja rakendamisjuhendite kategooriate kaupa
- **Visuaalsed indikaatorid**: Selge märgistamine kohustuslike nõuete ja soovitatud tavade vahel


#### Põhikontseptsioonid (01-CoreConcepts/) - Täielik moderniseerimine
- **Protokolli versiooni uuendus**: Uuendatud viitamiseks praegusele MCP spetsifikatsioonile 2025-06-18 kuupõhise versiooniga (AAAA-KK-PP formaat)
- **Arhitektuuri täpsustus**: Täiustatud kirjeldused hostidest, klientidest ja serveritest, et kajastada praeguseid MCP arhitektuurimustreid
  - Hostid nüüd selgelt määratletud kui AI rakendused, mis koordineerivad mitut MCP kliendiühendust
  - Kliendid kirjeldatud kui protokolli ühendajad, kes hoiavad ühe-ühele serveri suhteid
  - Serverid täiustatud kohaliku ja kaugjuhtimise juurutamise stsenaariumitega
- **Primitiivide ümberkorraldus**: Täielik ümberkujundus serveri ja kliendi primitiivides
  - Serveri primitiivid: Ressursid (andmeallikad), Prompts (mallid), Tööriistad (täidetavad funktsioonid) koos detailsete selgituste ja näidetega
  - Kliendi primitiivid: Proovivõtt (LLM täitmised), Elicitation (kasutaja sisend), Logimine (silumine/jälgimine)
  - Uuendatud praeguste avastamise (`*/list`), päringu (`*/get`) ja täitmise (`*/call`) meetodimustritega
- **Protokolli arhitektuur**: Sisse juhitud kahekihiline arhitektuurimudel
  - Andmekiht: JSON-RPC 2.0 alus koos elutsükli halduse ja primitiividega
  - Transpordikiht: STDIO (kohalik) ja voogedastatav HTTP koos SSE (kaug) transpordimehhanismidega
- **Turvafraamistik**: Põhjalikud turvapõhimõtted, sealhulgas selge kasutaja nõusolek, andmete privaatsuskaitse, tööriistade täitmise turvalisus ja transpordikihi turvalisus
- **Kommunikatsioonimustrid**: Uuendatud protokollisõnumid, mis näitavad initsialiseerimist, avastamist, täitmist ja teavituste vooge
- **Koodinäited**: Värskendatud mitmekeelsed näited (.NET, Java, Python, JavaScript), et kajastada praeguseid MCP SDK mustreid

#### Turvalisus (02-Security/) - Põhjalik turvalisuse ümberkujundus  
- **Standardite kooskõla**: Täielik kooskõla MCP spetsifikatsiooni 2025-06-18 turvanõuetega
- **Autentimise areng**: Dokumenteeritud areng kohandatud OAuth serveritest välise identiteedipakkuja delegatsioonini (Microsoft Entra ID)
- **AI-spetsiifiline ohtude analüüs**: Täiustatud kaetus kaasaegsetest AI ründevektoritest
  - Detailne prompt süstimise rünnakute stsenaariumid reaalse maailma näidetega
  - Tööriistamürgituse mehhanismid ja "rug pull" ründemustrid
  - Kontekstiakna mürgitus ja mudeli segaduse rünnakud
- **Microsofti AI turvalahendused**: Põhjalik ülevaade Microsofti turvaökosüsteemist
  - AI Prompt Shieldsid täiustatud avastamise, esiletõstmise ja eraldusmeetoditega
  - Azure Content Safety integratsioonimustrid
  - GitHub Advanced Security tarneahela kaitseks
- **Täiustatud ohtude leevendus**: Detailne turvakontroll sessiooni kaaperdamise, MCP-spetsiifiliste ründe stsenaariumite ja krüptograafiliste sessiooni ID nõuetega
  - Confused Deputy probleemid MCP proxy stsenaariumites koos selgete nõusoleku nõuetega
  - Tokeni läbipääsu haavatavused kohustuslike valideerimiskontrollidega
- **Tarneahela turvalisus**: Laiendatud AI tarneahela kaetus, sealhulgas baasmudelid, manustusteenused, konteksti pakkujad ja kolmanda osapoole API-d
- **Põhiturvalisus**: Täiustatud integratsioon ettevõtte turvamustritega, sealhulgas null usalduse arhitektuur ja Microsofti turvaökosüsteem
- **Ressursside organiseerimine**: Kategooriate kaupa põhjalikud ressursilingid tüübi järgi (ametlikud dokumendid, standardid, uurimistöö, Microsofti lahendused, rakendamisjuhendid)

### Dokumentatsiooni kvaliteedi parandused
- **Struktureeritud õpieesmärgid**: Täiustatud õpieesmärgid konkreetsete, teostatavate tulemustega
- **Ristviited**: Lisatud lingid seotud turva- ja põhikontseptsioonide teemade vahel
- **Praegune info**: Uuendatud kõik kuupäevaviited ja spetsifikatsiooni lingid praegustele standarditele
- **Rakendamisjuhised**: Lisatud spetsiifilised, teostatavad rakendamisjuhised mõlemas jaotises

## 16. juuli 2025

### README ja navigeerimise täiustused
- Täielikult ümber kujundatud õppekava navigeerimine README.md-s
- Asendatud `<details>` sildid ligipääsetavama tabelipõhise vorminguga
- Loodud alternatiivsed paigutuse valikud uues "alternative_layouts" kaustas
- Lisatud kaardipõhised, vahekaartide stiilis ja akordionstiilis navigeerimise näited
- Uuendatud hoidla struktuuri jaotis, mis sisaldab kõiki uusimaid faile
- Täiustatud "Kuidas seda õppekava kasutada" jaotis selgete soovitustega
- Uuendatud MCP spetsifikatsiooni lingid, mis osutavad õigetele URL-idele
- Lisatud kontekstitöötluse jaotis (5.14) õppekava struktuuri

### Õpiku uuendused
- Täielikult ümber kirjutatud õpiku juhend vastavalt praegusele hoidla struktuurile
- Lisatud uued jaotised MCP klientide ja tööriistade ning populaarsete MCP serverite kohta
- Uuendatud visuaalne õppekava kaart, mis kajastab täpselt kõiki teemasid
- Täiustatud täiustatud teemade kirjeldused, mis hõlmavad kõiki spetsialiseeritud valdkondi
- Uuendatud juhtumiuuringute jaotis, mis kajastab tegelikke näiteid
- Lisatud see põhjalik muudatuste logi

### Kogukonna panused (06-CommunityContributions/)
- Lisatud detailne info MCP serverite kohta pildigeneratsiooni jaoks
- Lisatud põhjalik jaotis Claude kasutamisest VSCode’is
- Lisatud Cline terminalikliendi seadistamise ja kasutamise juhised
- Uuendatud MCP kliendi jaotis, mis sisaldab kõiki populaarseid kliendivalikuid
- Täiustatud panuse näited täpsemate koodinäidetega

### Täiustatud teemad (05-AdvancedTopics/)
- Korraldatud kõik spetsialiseeritud teema kaustad järjepideva nimetamisega
- Lisatud kontekstitöötluse materjalid ja näited
- Lisatud Foundry agendi integratsiooni dokumentatsioon
- Täiustatud Entra ID turvalisuse integratsiooni dokumentatsioon

## 11. juuni 2025

### Esialgne loomine
- Välja antud MCP for Beginners õppekava esimene versioon
- Loodud põhiline struktuur kõigi 10 põhijaotise jaoks
- Rakendatud visuaalne õppekava kaart navigeerimiseks
- Lisatud esialgsed näidisprojektid mitmes programmeerimiskeeles

### Alustamine (03-GettingStarted/)
- Loodud esimesed serveri rakendamise näited
- Lisatud kliendi arendamise juhised
- Lisatud LLM kliendi integratsiooni juhised
- Lisatud VS Code integratsiooni dokumentatsioon
- Rakendatud Server-Sent Events (SSE) serveri näited

### Põhikontseptsioonid (01-CoreConcepts/)
- Lisatud detailne kliendi-serveri arhitektuuri selgitus
- Loodud dokumentatsioon protokolli põhikomponentide kohta
- Dokumenteeritud sõnumimustrid MCP-s

## 23. mai 2025

### Hoidla struktuur
- Initsialiseeritud hoidla põhilise kaustastruktuuriga
- Loodud README failid iga suurema jaotise jaoks
- Seadistatud tõlke infrastruktuur
- Lisatud pildifailid ja skeemid

### Dokumentatsioon
- Loodud esialgne README.md õppekava ülevaatega
- Lisatud CODE_OF_CONDUCT.md ja SECURITY.md
- Seadistatud SUPPORT.md juhistega abi saamiseks
- Loodud esialgne õpiku juhendi struktuur

## 15. aprill 2025

### Planeerimine ja raamistik
- Esialgne planeerimine MCP for Beginners õppekava jaoks
- Määratletud õpieesmärgid ja sihtrühm
- Kirjeldatud õppekava 10 jaotise struktuur
- Töötatud välja kontseptuaalne raamistik näidete ja juhtumiuuringute jaoks
- Loodud esialgsed prototüübi näited põhikontseptsioonide kohta

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->