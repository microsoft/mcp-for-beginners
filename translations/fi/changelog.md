# Muutosloki: MCP aloittelijoille -opetussuunnitelma

Tämä asiakirja toimii kirjana kaikista merkittävistä muutoksista, jotka on tehty Model Context Protocol (MCP) for Beginners -opetussuunnitelmaan. Muutokset on dokumentoitu käänteisessä kronologisessa järjestyksessä (uusimmat muutokset ensin).

## 18. joulukuuta 2025

### Turvallisuusdokumentaation päivitys - MCP-spesifikaatio 2025-11-25

#### MCP:n turvallisuuden parhaat käytännöt (02-Security/mcp-best-practices.md) - Spesifikaatioversion päivitys
- **Protokollaversion päivitys**: Päivitetty viittaukset uusimpaan MCP-spesifikaatioon 2025-11-25 (julkaistu 25. marraskuuta 2025)
  - Päivitetty kaikki spesifikaatioversion viittaukset 2025-06-18:sta 2025-11-25:een
  - Päivitetty asiakirjan päivämääräviittaukset 18. elokuuta 2025:stä 18. joulukuuta 2025:een
  - Varmistettu, että kaikki spesifikaatio-URL-osoitteet osoittavat nykyiseen dokumentaatioon
- **Sisällön validointi**: Kattava turvallisuuden parhaiden käytäntöjen validointi uusimpia standardeja vastaan
  - **Microsoftin turvallisuusratkaisut**: Varmistettu nykyiset termit ja linkit Prompt Shieldsille (aiemmin "Jailbreak risk detection"), Azure Content Safetylle, Microsoft Entra ID:lle ja Azure Key Vaultille
  - **OAuth 2.1 -turvallisuus**: Vahvistettu yhdenmukaisuus uusimpien OAuth-turvallisuuden parhaiden käytäntöjen kanssa
  - **OWASP-standardit**: Tarkistettu, että OWASP Top 10 LLM:ille -viittaukset ovat ajan tasalla
  - **Azure-palvelut**: Varmistettu kaikki Microsoft Azuren dokumentaatio- ja parhaiden käytäntöjen linkit
- **Standardien yhdenmukaisuus**: Kaikki viitatut turvallisuusstandardit vahvistettu ajantasaisiksi
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azuren turvallisuus- ja vaatimustenmukaisuuskehykset
- **Toteutusresurssit**: Varmistettu kaikki toteutusoppaiden linkit ja resurssit
  - Azure API Managementin todennuskuviot
  - Microsoft Entra ID:n integraatio-oppaat
  - Azure Key Vaultin salaisuuksien hallinta
  - DevSecOps-putket ja valvontaratkaisut

### Dokumentaation laadunvarmistus
- **Spesifikaation noudattaminen**: Varmistettu, että kaikki pakolliset MCP-turvavaatimukset (MUST/MUST NOT) vastaavat uusinta spesifikaatiota
- **Resurssien ajantasaisuus**: Tarkistettu kaikki ulkoiset linkit Microsoftin dokumentaatioon, turvallisuusstandardeihin ja toteutusoppaisiin
- **Parhaiden käytäntöjen kattavuus**: Vahvistettu kattava käsittely todennuksesta, valtuutuksesta, tekoälyyn liittyvistä uhkista, toimitusketjun turvallisuudesta ja yrityskuvioista

## 6. lokakuuta 2025

### Aloitusosion laajennus – Edistynyt palvelimen käyttö & yksinkertainen todennus

#### Edistynyt palvelimen käyttö (03-GettingStarted/10-advanced)
- **Uusi luku lisätty**: Esitelty kattava opas edistyneeseen MCP-palvelimen käyttöön, joka kattaa sekä tavalliset että matalan tason palvelinarkkitehtuurit.
  - **Tavallinen vs. matalan tason palvelin**: Yksityiskohtainen vertailu ja koodiesimerkit Pythonilla ja TypeScriptille molemmista lähestymistavoista.
  - **Handler-pohjainen suunnittelu**: Selitys handler-pohjaisesta työkalujen/resurssien/promptien hallinnasta skaalautuvia ja joustavia palvelinratkaisuja varten.
  - **Käytännön mallit**: Todelliset tilanteet, joissa matalan tason palvelinmallit ovat hyödyllisiä edistyneille ominaisuuksille ja arkkitehtuurille.

#### Yksinkertainen todennus (03-GettingStarted/11-simple-auth)
- **Uusi luku lisätty**: Vaiheittainen opas yksinkertaisen todennuksen toteuttamiseen MCP-palvelimissa.
  - **Todennuskonseptit**: Selkeä selitys todennuksen ja valtuutuksen eroista sekä tunnistetietojen käsittelystä.
  - **Perustason todennuksen toteutus**: Middleware-pohjaiset todennuskuviot Pythonilla (Starlette) ja TypeScriptille (Express), koodiesimerkkien kera.
  - **Eteneminen edistyneeseen turvallisuuteen**: Ohjeistus yksinkertaisesta todennuksesta OAuth 2.1:een ja RBAC:iin, viittauksilla edistyneisiin turvallisuusmoduuleihin.

Nämä lisäykset tarjoavat käytännönläheistä, käytännön opastusta vahvempien, turvallisempien ja joustavampien MCP-palvelinratkaisujen rakentamiseen, yhdistäen perustavanlaatuiset käsitteet edistyneisiin tuotantomalleihin.

## 29. syyskuuta 2025

### MCP-palvelimen tietokantaintegraatiolaboratoriot – Kattava käytännön oppimispolku

#### 11-MCPServerHandsOnLabs – Uusi täydellinen tietokantaintegraatio-opetussuunnitelma
- **Täydellinen 13-laboratoriopolku**: Lisätty kattava käytännön opetussuunnitelma tuotantovalmiiden MCP-palvelimien rakentamiseen PostgreSQL-tietokantaintegraatiolla
  - **Todellisen maailman toteutus**: Zava Retailin analytiikkatapaus, joka demonstroi yritystason malleja
  - **Rakenteellinen oppimisen eteneminen**:
    - **Laboratoriot 00-03: Perusteet** – Johdanto, ydinarkkitehtuuri, turvallisuus & monivuokraus, ympäristön asennus
    - **Laboratoriot 04-06: MCP-palvelimen rakentaminen** – Tietokannan suunnittelu & skeema, MCP-palvelimen toteutus, työkalujen kehitys  
    - **Laboratoriot 07-09: Edistyneet ominaisuudet** – Semanttinen haku, testaus & virheenkorjaus, VS Code -integraatio
    - **Laboratoriot 10-12: Tuotanto & parhaat käytännöt** – Julkaisustrategiat, valvonta & havaittavuus, parhaat käytännöt & optimointi
  - **Yritysteknologiat**: FastMCP-kehys, PostgreSQL pgvectorillä, Azure OpenAI -upotukset, Azure Container Apps, Application Insights
  - **Edistyneet ominaisuudet**: Rivitason turvallisuus (RLS), semanttinen haku, monivuokraajan datan käyttö, vektoriupotukset, reaaliaikainen valvonta

#### Terminologian yhdenmukaistus – Moduulista laboratorioon
- **Kattava dokumentaatiopäivitys**: Päivitetty systemaattisesti kaikki README-tiedostot 11-MCPServerHandsOnLabs-kansiossa käyttämään "Lab" -terminologiaa "Module" sijaan
  - **Osiootsikot**: Päivitetty "What This Module Covers" muotoon "What This Lab Covers" kaikissa 13 laboratoriossa
  - **Sisällön kuvaus**: Muutettu "This module provides..." muotoon "This lab provides..." dokumentaatiossa
  - **Oppimistavoitteet**: Päivitetty "By the end of this module..." muotoon "By the end of this lab..."
  - **Navigointilinkit**: Muutettu kaikki "Module XX:" -viittaukset muotoon "Lab XX:" ristiinviittauksissa ja navigoinnissa
  - **Suorituksen seuranta**: Päivitetty "After completing this module..." muotoon "After completing this lab..."
  - **Tekniset viittaukset säilytetty**: Python-moduuliviittaukset konfiguraatiotiedostoissa (esim. `"module": "mcp_server.main"`) säilytetty

#### Opasopiskelijan parannus (study_guide.md)
- **Visuaalinen opetussuunnitelmakartta**: Lisätty uusi "11. Database Integration Labs" -osio kattavalla laboratoriorakenteen visualisoinnilla
- **Repositorion rakenne**: Päivitetty kymmenestä yhdelletoista pääosioon, sisältäen yksityiskohtaisen kuvauksen 11-MCPServerHandsOnLabsista
- **Oppimispolun ohjeistus**: Parannettu navigointiohjeita kattamaan osiot 00-11
- **Teknologian kattavuus**: Lisätty FastMCP, PostgreSQL, Azure-palveluiden integraatiotiedot
- **Oppimistulokset**: Korostettu tuotantovalmiiden palvelimien kehitystä, tietokantaintegraatiomalleja ja yritysturvallisuutta

#### Pää-README-rakenteen parannus
- **Laboratoriopohjainen terminologia**: Päivitetty pää-README.md 11-MCPServerHandsOnLabsissa käyttämään johdonmukaisesti "Lab" -rakennetta
- **Oppimispolun organisointi**: Selkeä eteneminen perustavanlaatuisista käsitteistä edistyneeseen toteutukseen ja tuotantoon
- **Todellisen maailman painotus**: Korostettu käytännönläheistä, käytännön oppimista yritystason mallien ja teknologioiden kanssa

### Dokumentaation laadun ja johdonmukaisuuden parannukset
- **Käytännönläheinen oppiminen**: Vahvistettu käytännön, laboratorioihin perustuva lähestymistapa koko dokumentaatiossa
- **Yritysmallien painotus**: Korostettu tuotantovalmiita toteutuksia ja yritysturvallisuusnäkökohtia
- **Teknologian integrointi**: Kattava käsittely nykyaikaisista Azure-palveluista ja tekoälyintegraatiomalleista
- **Oppimisen eteneminen**: Selkeä, jäsennelty polku peruskäsitteistä tuotantoon

## 26. syyskuuta 2025

### Tapaustutkimusten parannus – GitHub MCP Registry -integraatio

#### Tapaustutkimukset (09-CaseStudy/) – Ekosysteemin kehityksen painotus
- **README.md**: Merkittävä laajennus kattavalla GitHub MCP Registry -tapaustutkimuksella
  - **GitHub MCP Registry -tapaustutkimus**: Uusi kattava tapaustutkimus, joka tarkastelee GitHubin MCP Registryn julkaisua syyskuussa 2025
    - **Ongelman analyysi**: Yksityiskohtainen tarkastelu hajanaisen MCP-palvelimen löytämisen ja käyttöönoton haasteista
    - **Ratkaisun arkkitehtuuri**: GitHubin keskitetty rekisteriratkaisu, jossa yhden klikkauksen VS Code -asennus
    - **Liiketoiminnan vaikutus**: Mitattavissa olevat parannukset kehittäjien perehdytyksessä ja tuottavuudessa
    - **Strateginen arvo**: Painotus modulaariseen agenttien käyttöönottoon ja työkalujen väliseen yhteentoimivuuteen
    - **Ekosysteemin kehitys**: Sijoittuminen perustavanlaatuiseksi alustaksi agenttipohjaiselle integraatiolle
  - **Parannettu tapaustutkimusten rakenne**: Päivitetty kaikki seitsemän tapaustutkimusta johdonmukaisella muotoilulla ja kattavilla kuvauksilla
    - Azure AI Travel Agents: Moniagenttien orkestroinnin painotus
    - Azure DevOps -integraatio: Työnkulun automaation painotus
    - Reaaliaikainen dokumenttien haku: Python-konsoliasiakas
    - Interaktiivinen opintosuunnitelman generaattori: Chainlit-keskustelusovellus
    - Editorin sisäinen dokumentaatio: VS Code ja GitHub Copilot -integraatio
    - Azure API Management: Yritystason API-integraatiomallit
    - GitHub MCP Registry: Ekosysteemin kehitys ja yhteisöalusta
  - **Kattava yhteenveto**: Uudelleenkirjoitettu yhteenveto-osio, joka korostaa seitsemää tapaustutkimusta eri MCP-toteutuksen ulottuvuuksilla
    - Yritysintegratio, moniagenttien orkestrointi, kehittäjien tuottavuus
    - Ekosysteemin kehitys, koulutussovellukset -luokittelu
    - Parannettu näkemyksiä arkkitehtuurimalleista, toteutusstrategioista ja parhaista käytännöistä
    - Korostus MCP:n kypsänä, tuotantovalmiina protokollana

#### Opasopiskelijan päivitykset (study_guide.md)
- **Visuaalinen opetussuunnitelmakartta**: Päivitetty miellekartta sisältämään GitHub MCP Registry tapaustutkimusosiossa
- **Tapaustutkimusten kuvaus**: Parannettu geneerisistä kuvauksista yksityiskohtaiseen seitsemän tapaustutkimuksen erittelyyn
- **Repositorion rakenne**: Päivitetty osio 10 kattamaan kattava tapaustutkimusten sisältö ja toteutustiedot
- **Muutoslokin integrointi**: Lisätty 26. syyskuuta 2025 merkintä, joka dokumentoi GitHub MCP Registryn lisäyksen ja tapaustutkimusten parannukset
- **Päivämääräpäivitykset**: Päivitetty alatunnisteen aikaleima vastaamaan viimeisintä versiota (26. syyskuuta 2025)

### Dokumentaation laadun parannukset
- **Johdonmukaisuuden parannus**: Standardoitu tapaustutkimusten muotoilu ja rakenne kaikissa seitsemässä esimerkissä
- **Kattava käsittely**: Tapaustutkimukset kattavat nyt yritys-, kehittäjien tuottavuus- ja ekosysteemikehitystilanteet
- **Strateginen asema**: Parannettu painotus MCP:hen perustavana alustana agenttipohjaiselle järjestelmäkäyttöönotolle
- **Resurssien integrointi**: Päivitetty lisäresurssit sisältämään GitHub MCP Registry -linkki

## 15. syyskuuta 2025

### Edistyneet aiheet laajennus – Mukautetut siirrot & kontekstisuunnittelu

#### MCP:n mukautetut siirrot (05-AdvancedTopics/mcp-transport/) – Uusi edistynyt toteutusopas
- **README.md**: Täydellinen toteutusopas mukautetuille MCP-siirtomekanismeille
  - **Azure Event Grid -siirto**: Kattava palvelimeton tapahtumapohjainen siirtototeutus
    - C#, TypeScript ja Python -esimerkit Azure Functions -integraatiolla
    - Tapahtumapohjaiset arkkitehtuurimallit skaalautuville MCP-ratkaisuille
    - Webhook-vastaanottimet ja push-pohjainen viestinkäsittely
  - **Azure Event Hubs -siirto**: Suurivirtainen suoratoistosiirto
    - Reaaliaikaiset suoratoistomahdollisuudet matalan viiveen tilanteisiin
    - Osiointistrategiat ja checkpoint-hallinta
    - Viestien ryhmittely ja suorituskyvyn optimointi
  - **Yritysintegratiomallit**: Tuotantovalmiit arkkitehtuuriesimerkit
    - Hajautettu MCP-käsittely useiden Azure Functions -instanssien välillä
    - Hybridisiirtoarkkitehtuurit, jotka yhdistävät useita siirtotyyppejä
    - Viestien kestävyys, luotettavuus ja virheenkäsittelystrategiat
  - **Turvallisuus & valvonta**: Azure Key Vault -integraatio ja havaittavuusmallit
    - Hallitun identiteetin todennus ja vähimmän oikeuden periaate
    - Application Insights -telemetria ja suorituskyvyn valvonta
    - Piirikytkimet ja vikasietoisuusmallit
  - **Testauskehykset**: Kattavat testausstrategiat mukautetuille siirroille
    - Yksikkötestaus testidubletteineen ja mockauskehyksineen
    - Integraatiotestaus Azure Test Containers -ympäristössä
    - Suorituskyky- ja kuormitustestausnäkökohdat

#### Kontekstisuunnittelu (05-AdvancedTopics/mcp-contextengineering/) – Nouseva tekoälyn ala
- **README.md**: Kattava tutkimus kontekstisuunnittelusta nousevana alana
  - **Periaatteet**: Täydellinen kontekstin jakaminen, toimintapäätösten tietoisuus ja kontekstin ikkunanhallinta
  - **MCP-protokollan yhdenmukaisuus**: Kuinka MCP-suunnittelu vastaa kontekstisuunnittelun haasteisiin
    - Kontekstin ikkunan rajoitukset ja progressiivisen latauksen strategiat
    - Merkityksellisyyden määrittäminen ja dynaaminen kontekstin haku
    - Monimodaalinen kontekstin käsittely ja turvallisuusnäkökohdat
  - **Toteutuslähestymistavat**: Yksisäikeiset vs. moniagenttijärjestelmät
    - Kontekstin pilkkominen ja priorisointitekniikat
    - Progressiivinen kontekstin lataus ja pakkausstrategiat
    - Kerroksellinen kontekstin käsittely ja hakun optimointi
  - **Mittauskehys**: Nousevat mittarit kontekstin tehokkuuden arviointiin
    - Syötteen tehokkuus, suorituskyky, laatu ja käyttäjäkokemus
    - Kokeelliset lähestymistavat kontekstin optimointiin
    - Virheanalyysi ja parannusmenetelmät

#### Opetussuunnitelman navigointipäivitykset (README.md)
- **Parannettu moduulirakenne**: Päivitetty opetussuunnitelman taulukko sisältämään uudet edistyneet aiheet
  - Lisätty Context Engineering (5.14) ja Custom Transport (5.15) -kohdat
  - Johdonmukainen muotoilu ja navigointilinkit kaikissa moduuleissa
  - Päivitetyt kuvaukset vastaamaan nykyistä sisältöä

### Hakemistorakenteen parannukset
- **Nimien yhdenmukaistus**: Nimetty "mcp transport" uudelleen muotoon "mcp-transport" yhdenmukaisuuden vuoksi muiden edistyneiden aiheiden kansioiden kanssa
- **Sisällön organisointi**: Kaikki 05-AdvancedTopics-kansiot noudattavat nyt johdonmukaista nimikäytäntöä (mcp-[aihe])

### Dokumentaation laadun parannukset
- **MCP-spesifikaation yhdenmukaisuus**: Kaikki uusi sisältö viittaa nykyiseen MCP-spesifikaatioon 2025-06-18
- **Monikieliset esimerkit**: Kattavat koodiesimerkit C#:lla, TypeScriptille ja Pythonilla
- **Yrityspainotus**: Tuotantovalmiit mallit ja Azure-pilvi-integraatio kauttaaltaan
- **Visuaalinen dokumentaatio**: Mermaid-kaaviot arkkitehtuurin ja työnkulun visualisointiin

## 18. elokuuta 2025

### Dokumentaation kattava päivitys – MCP 2025-06-18 -standardit

#### MCP:n turvallisuuden parhaat käytännöt (02-Security/) – Täydellinen modernisointi
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täydellinen uudelleenkirjoitus MCP-spesifikaation 2025-06-18 mukaisesti
  - **Pakolliset vaatimukset**: Lisätty virallisesta spesifikaatiosta eksplisiittiset PAKKO/ EI SAA -vaatimukset selkeillä visuaalisilla indikaattoreilla
  - **12 ydinturvakäytäntöä**: Järjestelty uudelleen 15 kohdan listasta kattaviksi turvallisuusalueiksi
    - Tokenin turvallisuus ja todennus ulkoisen identiteettipalveluntarjoajan integraatiolla
    - Istunnon hallinta ja siirtoturvallisuus kryptografisilla vaatimuksilla
    - AI-spesifinen uhkasuojaus Microsoft Prompt Shields -integraatiolla
    - Pääsynvalvonta ja käyttöoikeudet vähimmän etuoikeuden periaatteella
    - Sisällön turvallisuus ja valvonta Azure Content Safety -integraatiolla
    - Toimitusketjun turvallisuus kattavalla komponenttien varmennuksella
    - OAuth-turvallisuus ja Confused Deputy -hyökkäyksen estäminen PKCE-toteutuksella
    - Tapahtumavaste ja palautuminen automatisoiduilla ominaisuuksilla
    - Säädösten noudattaminen ja hallinto sääntelyvaatimusten mukaisesti
    - Edistyneet turvakontrollit zero trust -arkkitehtuurilla
    - Microsoftin turvallisuus-ekosysteemin integraatio kattavilla ratkaisuilla
    - Jatkuva turvallisuuden kehitys mukautuvilla käytännöillä
  - **Microsoftin turvallisuusratkaisut**: Parannettu integraatio-ohjeistus Prompt Shieldsille, Azure Content Safetylle, Entra ID:lle ja GitHub Advanced Securitylle
  - **Toteutusresurssit**: Luokiteltu kattavat resurssilinkit virallisen MCP-dokumentaation, Microsoftin turvallisuusratkaisujen, turvallisuusstandardien ja toteutusoppaiden mukaan

#### Edistyneet turvakontrollit (02-Security/) - Yritystason toteutus
- **MCP-SECURITY-CONTROLS-2025.md**: Täydellinen uudistus yritystason turvallisuuskehykseksi
  - **9 kattavaa turvallisuusaluetta**: Laajennettu peruskontrolleista yksityiskohtaiseen yrityskehykseen
    - Edistynyt todennus ja valtuutus Microsoft Entra ID -integraatiolla
    - Tokenin turvallisuus ja anti-passthrough-kontrollit kattavalla validoinnilla
    - Istunnon turvakontrollit kaappauksen estolla
    - AI-spesifiset turvakontrollit prompt-injektion ja työkalumyrkytyksen estolla
    - Confused Deputy -hyökkäyksen estäminen OAuth-välityspalvelimen turvallisuudella
    - Työkalujen suoritusturvallisuus hiekkalaatikoilla ja eristyksellä
    - Toimitusketjun turvakontrollit riippuvuuksien varmennuksella
    - Valvonta- ja havaitsemiskontrollit SIEM-integraatiolla
    - Tapahtumavaste ja palautuminen automatisoiduilla ominaisuuksilla
  - **Toteutusesimerkit**: Lisätty yksityiskohtaiset YAML-konfiguraatiolohkot ja koodiesimerkit
  - **Microsoft-ratkaisujen integraatio**: Kattava Azure-turvapalveluiden, GitHub Advanced Securityn ja yrityksen identiteetinhallinnan kattavuus

#### Edistyneet aiheet turvallisuus (05-AdvancedTopics/mcp-security/) - Tuotantovalmiit toteutukset
- **README.md**: Täydellinen uudelleenkirjoitus yritysturvallisuuden toteutukseen
  - **Nykyisen spesifikaation mukaisuus**: Päivitetty MCP Specification 2025-06-18 mukaiseksi pakollisine turvallisuusvaatimuksineen
  - **Parannettu todennus**: Microsoft Entra ID -integraatio kattavilla .NET- ja Java Spring Security -esimerkeillä
  - **AI-turvallisuusintegraatio**: Microsoft Prompt Shieldsin ja Azure Content Safetyn toteutus yksityiskohtaisilla Python-esimerkeillä
  - **Edistynyt uhkien lieventäminen**: Kattavat toteutusesimerkit
    - Confused Deputy -hyökkäyksen estäminen PKCE:llä ja käyttäjän suostumuksen validoinnilla
    - Tokenin passthrough-estäminen yleisövalidoinnilla ja turvallisella token-hallinnalla
    - Istunnon kaappauksen estäminen kryptografisella sidonnalla ja käyttäytymisanalyysillä
  - **Yritysturvallisuuden integraatio**: Azure Application Insights -valvonta, uhkien havaitsemisputket ja toimitusketjun turvallisuus
  - **Toteutuschecklist**: Selkeä pakollisten ja suositeltujen turvakontrollien erottelu Microsoftin turvallisuus-ekosysteemin hyödyillä

### Dokumentaation laatu ja standardien mukaisuus
- **Spesifikaatioviitteet**: Päivitetty kaikki viitteet nykyiseen MCP Specification 2025-06-18
- **Microsoftin turvallisuus-ekosysteemi**: Parannettu integraatio-ohjeistus kaikissa turvallisuusdokumentaatioissa
- **Käytännön toteutus**: Lisätty yksityiskohtaisia koodiesimerkkejä .NET:ssä, Javassa ja Pythonissa yritysmallien mukaisesti
- **Resurssien organisointi**: Kattava virallisen dokumentaation, turvallisuusstandardien ja toteutusoppaiden luokittelu
- **Visuaaliset indikaattorit**: Selkeä merkintä pakollisille vaatimuksille ja suositelluille käytännöille


#### Ydinkäsitteet (01-CoreConcepts/) - Täydellinen modernisointi
- **Protokollaversion päivitys**: Päivitetty viittaukset nykyiseen MCP Specification 2025-06-18 päivämääräpohjaisella versioinnilla (VVVV-KK-PP-muoto)
- **Arkkitehtuurin tarkennus**: Parannettu kuvaukset Hosteista, Clienteista ja Serveista nykyisten MCP-arkkitehtuurimallien mukaisesti
  - Hostit määritelty selkeästi AI-sovelluksiksi, jotka koordinoivat useita MCP-asiakasliitäntöjä
  - Clientit kuvattu protokollaliittiminä, jotka ylläpitävät yksittäisiä palvelinsuhteita
  - Serverit parannettu paikallisen ja etäkäyttöönoton skenaarioilla
- **Primitivien uudelleenjärjestely**: Täydellinen uudistus palvelin- ja asiakasprimitivien osalta
  - Palvelinprimitivit: Resurssit (tietolähteet), Promptit (mallipohjat), Työkalut (suoritettavat funktiot) yksityiskohtaisilla selityksillä ja esimerkeillä
  - Asiakasprimitivit: Näytteenotto (LLM-vastaukset), Elicitaatio (käyttäjän syöte), Lokitus (debuggaus/valvonta)
  - Päivitetty nykyisillä discovery (`*/list`), retrieval (`*/get`) ja execution (`*/call`) -menetelmillä
- **Protokollan arkkitehtuuri**: Esitelty kaksikerroksinen arkkitehtuurimalli
  - Datalayer: JSON-RPC 2.0 -perusta elinkaaren hallinnalla ja primitiiveillä
  - Transportlayer: STDIO (paikallinen) ja Streamable HTTP SSE:llä (etäkuljetusmekanismit)
- **Turvakehys**: Kattavat turvallisuusperiaatteet, mukaan lukien eksplisiittinen käyttäjän suostumus, tietosuojan suojaus, työkalujen suoritusturvallisuus ja siirtokerroksen turvallisuus
- **Viestintämallit**: Päivitetyt protokollaviestit näyttämään alustuksen, löydön, suorituksen ja ilmoitusvirrat
- **Koodiesimerkit**: Päivitetyt monikieliset esimerkit (.NET, Java, Python, JavaScript) nykyisten MCP SDK -mallien mukaisesti

#### Turvallisuus (02-Security/) - Kattava turvallisuuden uudistus  
- **Standardien mukaisuus**: Täysi yhdenmukaisuus MCP Specification 2025-06-18 turvallisuusvaatimusten kanssa
- **Todennuksen kehitys**: Dokumentoitu kehitys räätälöidyistä OAuth-palvelimista ulkoisen identiteettipalveluntarjoajan delegointiin (Microsoft Entra ID)
- **AI-spesifinen uhka-analyysi**: Parannettu kattavuus nykyaikaisista AI-hyökkäysvektoreista
  - Yksityiskohtaiset prompt-injektion hyökkäysskenaariot todellisilla esimerkeillä
  - Työkalujen myrkytysmenetelmät ja "rug pull" -hyökkäysmallit
  - Kontekstin myrkytys ja mallin sekoittumishyökkäykset
- **Microsoftin AI-turvaratkaisut**: Kattava Microsoftin turvallisuus-ekosysteemin kuvaus
  - AI Prompt Shields edistyneellä havaitsemisella, korostuksilla ja erottelutekniikoilla
  - Azure Content Safety -integraatiomallit
  - GitHub Advanced Security toimitusketjun suojaukseen
- **Edistynyt uhkien lieventäminen**: Yksityiskohtaiset turvakontrollit
  - Istunnon kaappaus MCP-spesifisillä hyökkäysskenaarioilla ja kryptografisilla istuntotunnusvaatimuksilla
  - Confused Deputy -ongelmat MCP-välityspalvelimen skenaarioissa eksplisiittisillä suostumusvaatimuksilla
  - Tokenin passthrough-haavoittuvuudet pakollisilla validointikontrolleilla
- **Toimitusketjun turvallisuus**: Laajennettu AI-toimitusketjun kattavuus sisältäen perustamallit, upotepalvelut, kontekstin tarjoajat ja kolmannen osapuolen API:t
- **Perusturvallisuus**: Parannettu integraatio yritysturvallisuusmalleihin, mukaan lukien zero trust -arkkitehtuuri ja Microsoftin turvallisuus-ekosysteemi
- **Resurssien organisointi**: Luokiteltu kattavat resurssilinkit tyypin mukaan (viralliset dokumentit, standardit, tutkimus, Microsoft-ratkaisut, toteutusoppaat)

### Dokumentaation laadun parannukset
- **Rakenteelliset oppimistavoitteet**: Parannetut oppimistavoitteet konkreettisilla, toteuttamiskelpoisilla tuloksilla
- **Ristiinviittaukset**: Lisätty linkkejä liittyvien turvallisuus- ja ydinkäsitteen aiheiden välillä
- **Ajantasainen tieto**: Päivitetty kaikki päivämääräviitteet ja spesifikaatiolinkit nykyisiin standardeihin
- **Toteutusohjeistus**: Lisätty konkreettisia, toteuttamiskelpoisia ohjeita molempiin osioihin

## 16. heinäkuuta 2025

### README ja navigoinnin parannukset
- Täysin uudistettu opetussuunnitelman navigointi README.md:ssä
- Korvattu `<details>`-tagit helpommin saavutettavalla taulukkomuodolla
- Luotu vaihtoehtoisia asetteluvaihtoehtoja uuteen "alternative_layouts" -kansioon
- Lisätty korttipohjaisia, välilehtityylisiä ja harmonikkatyylisiä navigointiesimerkkejä
- Päivitetty repositorion rakenneosio sisältämään kaikki uusimmat tiedostot
- Parannettu "Kuinka käyttää tätä opetussuunnitelmaa" -osio selkeillä suosituksilla
- Päivitetty MCP-spesifikaatiolinkit osoittamaan oikeisiin URL-osoitteisiin
- Lisätty Context Engineering -osio (5.14) opetussuunnitelman rakenteeseen

### Opas päivitykset
- Täysin uudistettu opas vastaamaan nykyistä repositorion rakennetta
- Lisätty uudet osiot MCP-asiakkaille ja -työkaluille sekä suosituimmille MCP-palvelimille
- Päivitetty Visual Curriculum Map heijastamaan tarkasti kaikkia aiheita
- Parannettu Edistyneet aiheet -kuvauksia kattamaan kaikki erikoisalat
- Päivitetty Case Studies -osio vastaamaan todellisia esimerkkejä
- Lisätty tämä kattava muutosloki

### Yhteisön panokset (06-CommunityContributions/)
- Lisätty yksityiskohtaista tietoa MCP-palvelimista kuvageneraatiota varten
- Lisätty kattava osio Clauden käytöstä VSCodessa
- Lisätty Cline-päätelmäasiakkaan asennus- ja käyttöohjeet
- Päivitetty MCP-asiakasosio sisältämään kaikki suosituimmat asiakasvaihtoehdot
- Parannettu kontribuutioesimerkkejä tarkemmilla koodinäytteillä

### Edistyneet aiheet (05-AdvancedTopics/)
- Järjestetty kaikki erikoistuneet aihealuekansiot yhdenmukaisin nimillä
- Lisätty kontekstisuunnittelumateriaaleja ja esimerkkejä
- Lisätty Foundry-agentin integraatiodokumentaatio
- Parannettu Entra ID:n turvallisuusintegraatiodokumentaatiota

## 11. kesäkuuta 2025

### Alkuperäinen luonti
- Julkaistu ensimmäinen versio MCP for Beginners -opetussuunnitelmasta
- Luotu perusrakenne kaikille 10 pääosiolle
- Toteutettu Visual Curriculum Map navigointia varten
- Lisätty alkuperäiset esimerkkiprojektit useilla ohjelmointikielillä

### Aloittaminen (03-GettingStarted/)
- Luotu ensimmäiset palvelintoteutusesimerkit
- Lisätty asiakaskehitysohjeet
- Sisällytetty LLM-asiakasintegraatio-ohjeet
- Lisätty VS Code -integraatiodokumentaatio
- Toteutettu Server-Sent Events (SSE) -palvelinesimerkit

### Ydinkäsitteet (01-CoreConcepts/)
- Lisätty yksityiskohtainen selitys asiakas-palvelinarkkitehtuurista
- Luotu dokumentaatio keskeisistä protokollakomponenteista
- Dokumentoitu viestintämallit MCP:ssä

## 23. toukokuuta 2025

### Repositorion rakenne
- Alustettu repositorio perusrakenteella
- Luotu README-tiedostot jokaiselle pääosalle
- Perustettu käännösinfrastruktuuri
- Lisätty kuvat ja kaaviot

### Dokumentaatio
- Luotu alkuperäinen README.md opetussuunnitelman yleiskatsauksella
- Lisätty CODE_OF_CONDUCT.md ja SECURITY.md
- Perustettu SUPPORT.md ohjeilla avun saamiseksi
- Luotu alustava opasrakenteen runko

## 15. huhtikuuta 2025

### Suunnittelu ja kehys
- Alustava suunnittelu MCP for Beginners -opetussuunnitelmalle
- Määritelty oppimistavoitteet ja kohdeyleisö
- Luotu 10-osainen rakenne opetussuunnitelmalle
- Kehitetty konseptuaalinen kehys esimerkeille ja tapaustutkimuksille
- Luotu alkuperäiset prototyyppiesimerkit keskeisistä käsitteistä

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->