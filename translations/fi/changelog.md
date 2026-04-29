# Muutospäiväkirja: MCP aloittelijoille -opintokokonaisuus

Tämä dokumentti toimii tallennuksena kaikista merkittävistä Model Context Protocol (MCP) aloittelijoille -opintokokonaisuuden muutoksista. Muutokset on kirjattu käänteisessä kronologisessa järjestyksessä (uusimmat ensin).

## 11. huhtikuuta 2026

### Uusi oppitunti, dokumentaation korjauksia ja riippuvuuksien päivityksiä

#### Uutta opintosisältöä lisätty

**Moduuli 05 - Edistyneet aiheet**
- **Oppitunti 5.17: Vihamielinen moniajattelujärjestelmien päättely MCP:llä** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Uusi laaja opas, joka käsittelee vihamielistä väittelymallia moniajattelujärjestelmissä
  - Mermaid-arkkitehtuurikaavio: kaksi agenttia → yhteinen MCP-palvelin → väittelytallenne → tuomari → päätös
  - Yhteinen MCP-työkalupalvelin (`web_search` + `run_python`), toteutettu Pythonilla ja TypeScripillä
  - Vastakkaiset järjestelmäkehotteet (PUOLUSTAA / VASTUSTAA / Tuomari) eksplisiittisillä työkalujen käyttövaatimuksilla
  - Väittelyn orkestroija Pythonilla, TypeScripillä ja C#:lla, joka hallinnoi kierroksia ja ohjaa argumentteja
  - MCP `ClientSession` -kytkentä orkestroijalle oikeisiin työkalukutsuihin
  - Käyttötapataulukko (harhan tunnistus, uhkamallinnus, API-suunnittelun tarkistus, tosiasioiden varmistus, teknologian valinta)
  - Turvallisuusseikat: hiekkalaatikkokehitys, työkalukutsujen validointi, nopeuden rajoitus, lokitus
  - Rakenteellinen harjoitus kolmella käytännön skenaariolla (koodikatselmus, arkkitehtuuripäätös, sisällön moderointi)

#### Dokumentaation korjaukset

**Moduuli 03 - Aloittaminen**
- **05-stdio-server/README.md**: Korjattu keskeneräinen TypeScript stdio -palvelin esimerkki — lisätty puuttuva siirtoyhteyden luonti (`new StdioServerTransport()`) ja `server.connect(transport)`-kutsu Python- ja .NET-esimerkkien mukaisesti samassa osiossa
- **14-sampling/README.md**: Korjattu kirjoitusvirhe — korjattu `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Opintokokonaisuuden päivitykset

**Pää-README.md**
- Lisätty oppitunti 5.17 (Vihamielinen moniajattelujärjestelmien päättely MCP:llä) opintotaulukkoon suoran linkin kanssa

**05-AdvancedTopics/README.md**
- Lisätty rivi oppitunnille 5.17 oppituntitaulukkoon

**study_guide.md**
- Lisätty Vihamielinen moniajattelujärjestelmien päättely -aihe miellekarttaan ja edistyneiden aiheiden tekstikuvaukseen

#### Koodin ja tietoturvan korjaukset

**Moduuli 05 - Vihamieliset agentit (`mcp-adversarial-agents`)**
- **Tietoturvakorjaus — komentoinjektio**: Vaihdettu TypeScriptin `run_python`-työkalussa `execSync`-kuorikomento interpolaatio käyttöön `execFile` + `promisify` -ratkaisuun, poistaen komentoinjektion haavoittuvuuden (LLM-ohjattu koodi välitetään nyt kirjaimellisena argv-elementtinä ilman kuoren osuutta)
- **MCP-työkalusilmukan kytkentä**: Päivitetty Pythonin väittely-orkestroija käyttämään `AsyncAnthropic`-asiakasta (korvaten synkronisen `Anthropic`), välittämään live-`ClientSession` jokaiselle agenttikierrokselle, hakemaan työkalumäärittelyt `session.list_tools()`-kutsulla kullekin kierrokselle, sekä lähettämään `tool_use`-lohkoja `session.call_tool()`-kutsun kautta silmukassa, kunnes malli tuottaa lopullisen tekstivastauksen

#### Riippuvuuspäivitykset

- Päivitetty `hono` versioon 4.12.12 useissa paketeissa (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Päivitetty `@hono/node-server` versiosta 1.19.11 versioon 1.19.13 TypeScript-paketeissa
- Päivitetty `cryptography` versiosta 46.0.5 versioon 46.0.7 Python-paketeissa (10-StreamliningAIWorkflows labrat 3 ja 4)
- Päivitetty `lodash` versiosta 4.17.23 versioon 4.18.1 10-StreamliningAIWorkflows tarkastajassa

#### Käännökset

- Synkronoitu käännökset 48+ kielelle viimeisimpien lähdemuutosten mukaisesti (i18n-päivitys)

---

## 5. helmikuuta 2026

### Koko repositorion validointi ja navigointiparannukset

#### Uutta opintosisältöä lisätty

**Moduuli 03 - Aloittaminen**
- **12-mcp-hosts/README.md**: Uusi kattava opas MCP-hostien määrittämiseen
  - Claude Desktopin, VS Coden, Cursorin, Clinen, Windsurfin konfiguraatioesimerkit
  - JSON-konfiguraatiomallit kaikille merkittäville hosteille
  - Kuljetustyyppien vertailutaulukko (stdio, SSE/HTTP, WebSocket)
  - Yleiset yhdistämisongelmat ja niiden ratkaisut
  - Turvallista hostikonfiguraatiota koskevat parhaat käytännöt

- **13-mcp-inspector/README.md**: Uusi virheenkorjausopas MCP Inspectorille
  - Asennusmenetelmät (npx, npm globaalisti, lähdekoodista)
  - Yhteydet palvelimiin stdio:n ja HTTP/SSE:n kautta
  - Työkalujen, resurssien ja kehotteiden testaaminen
  - VS Coden integrointi MCP Inspectoriin
  - Yleisiä virheenkorjaustilanteita ja ratkaisuja

**Moduuli 04 - Käytännön toteutus**
- **pagination/README.md**: Uusi sivutuksen toteutusopas
  - Cursor-pohjaiset sivutusmallit Pythonissa, TypeScriptissä, Javassa
  - Client-puolen sivutuksen käsittely
  - Cursorin suunnittelustrategiat (läpinäkymätön vs. jäsennelty)
  - Suorituskyvyn optimointisuositukset

**Moduuli 05 - Edistyneet aiheet**
- **mcp-protocol-features/README.md**: Uusi protokollan ominaisuuksien syväluotaus
  - Edistymisilmoitusten toteutus
  - Pyyntöjen peruutusmallit
  - Resurssimallit URI-kaavioilla
  - Palvelimen elinkaaren hallinta
  - Lokitasojen säätö
  - Virheenkäsittelymallit JSON-RPC-koodien kanssa

#### Navigointikorjaukset (24+ tiedostoa päivitetty)

**Päämoduulien README:t**
 Nyt osoitetaan linkit sekä ensimmäiseen oppituntiin että seuraavaan moduuliin

**02-Security Alitiedostot**
- Kaikilla 5 lisäturvallisuusasiakirjalla nyt "Mitä seuraavaksi" -navigointi:

**09-CaseStudy Tiedostot**
- Kaikilla tapaustutkimustiedostoilla nyt peräkkäinen navigointi:

**10-StreamliningAI Labrat**
Lisätty "Mitä seuraavaksi" -osio moduulin 10 yleiskatsaukseen ja moduuliin 11

#### Koodin ja sisällön korjaukset

**SDK ja riippuvuuspäivitykset**
Korjattu tyhjä openai-versio kohtaan `^4.95.0`
Päivitetty SDK versiosta `^1.8.0` versioon `>=1.26.0`
Päivitetty MCP versiotunnisteet kohtaan `>=1.26.0`

**Koodikorjaukset**
Korjattu virheellinen malli `gpt-4o-mini` muotoon `gpt-4.1-mini`

**Sisältökorjaukset**
Korjattu rikkinäinen linkki `READMEmd` → `README.md`, korjattu oppimateriaalin otsikko `Module 1-3` → `Module 0-3`, korjattu kirjainkoolla herkkä polku
Poistettu korruptoitunut päällekkäinen Case Study 5 -sisältö

**Aloittelijoiden ohjausparannukset**
Lisätty asianmukaiset esittelyt, oppimistavoitteet ja edellytykset aloittelijoille

#### Opintokokonaisuuden päivitykset

**Pää-README.md**
- Lisätty merkinnät 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Sivutus), 5.16 (Protokollan ominaisuudet) opintotaulukkoon

**Moduulien README:t**
Lisätty oppitunnit 12 ja 13 oppituntilistaan
Lisätty käytännön oppaat -osio sivutuslinkillä
Lisätty oppitunnit 5.15 (Mukautettu kuljetus) ja 5.16 (Protokollan ominaisuudet)

**study_guide.md**
- Päivitetty miellekarttaa kaikilla uusilla aiheilla: MCP Hosts -asetukset, MCP Inspector, Sivutusstrategiat, Protokollan ominaisuudet syväluotaus

## 28. tammikuuta 2026

### MCP-määrittelyn 2025-11-25 vaatimustenmukaisuus tarkistus

#### Keskeisten käsitteiden parannukset (01-CoreConcepts/)
- **Uusi Client-alkio - Roots**: Lisätty laaja dokumentaatio Roots-asiakasalkiosta, joka mahdollistaa palvelimille tiedostojärjestelmän rajojen ja käyttöoikeuksien ymmärtämisen
- **Työkalujen merkinnät**: Lisätty dokumentaatio työkalujen käyttäytymismerkinnöistä (`readOnlyHint`, `destructiveHint`) parempaan työkalusuorituksen päätöksentekoon
- **Työkalukutsut näytteistämisessä**: Päivitetty Näytteistys-dokumentaatio sisällyttämään `tools`- ja `toolChoice`-parametrit mallipohjaiseen työkalujen kutsumiseen näytteistysvaatimuksissa
- **URL-tilan käynnistys**: Lisätty dokumentaatio URI-pohjaisesta käynnistyksestä, jolla palvelin voi aloittaa ulkoiset web-interaktiot
- **Tehtävät (kokeellinen)**: Lisätty uusi osio, joka dokumentoi kokeellisen Tasks-ominaisuuden kestävälle suorituksen kääreenä ja tulosten viivehaulle
- **Kuvakkeiden tuki**: Huomattu, että työkalut, resurssit, resurssimallit ja kehotteet voivat sisältää kuvakkeita lisämetatietona

#### Dokumentaatiopäivitykset
- **README.md**: Lisätty MCP-määrittelyn 2025-11-25 versio ja päiväysperusteinen versiointi selitys
- **study_guide.md**: Päivitetty opintokokonaisuuskartta sisältämään Tasks ja Työkalumerkinnät Keskeisten käsitteiden osiossa; päivitetty dokumentin aikaleima

#### Määrittelyvaatimusten tarkistus
- **Protokollaversio**: Varmistettu, että kaikki dokumentaatioviitteet vastaavat MCP-määrittelyä 2025-11-25
- **Arkkitehtuurin yhdenmukaisuus**: Varmistettu kahden kerroksen arkkitehtuurin (Data Layer + Transport Layer) dokumentaation oikeellisuus
- **Primiittien dokumentaatio**: Varmistettu palvelimen primitiivien (Resurssit, Kehotteet, Työkalut) ja asiakkaan primitiivien (Näytteistys, Käynnistys, Lokitus, Roots) dokumentaatio
- **Kuljetusmekanismit**: Varmistettu STDIO- ja Streamable HTTP -kuljetuksen dokumentaation oikeellisuus
- **Tietoturvaohjeistuksen yhdenmukaisuus**: Vahvistettu nykyisen MCP-tietoturvan parhaiden käytäntöjen dokumentaation mukaisuus

#### Tärkeitä MCP 2025-11-25 -ominaisuuksia dokumentoitu
- **OpenID Connect -löytäminen**: Tunnistuspalvelimen löytäminen OIDC:n kautta
- **OAuth-asiakas-ID:n metadokumentit**: Suositeltu asiakasrekisteröintimekanismi
- **JSON Schema 2020-12**: MCP-skeemamääritelmien oletusdialekti
- **SDK-tasojärjestelmä**: Viralliset vaatimukset SDK:n ominaisuustuen ja ylläpidon tasoille
- **Hallintorakenne**: Virallistettu MCP:n hallinnan työryhmät ja kiinnostusryhmät

### Turvallisuusdokumentaation laaja päivitys (02-Security/)

#### MCP Security Summit Workshop (Sherpa) -integraatio
- **Uusi käytännön koulutusmateriaali**: Lisätty kattava integrointi [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) -materiaalin kanssa kaikkiin tietoturvadokumentteihin
- **Retkeilyreitin kattavuus**: Dokumentoitu koko leiristä leiriin eteneminen perusleiristä huipulle
- **OWASP:n yhdenmukaisuus**: Kaikki tietoturvaohjeistukset vastaavat OWASP MCP Azure Security Guide -riskiluokituksia

#### OWASP MCP Top 10 -integraatio
- **Uusi osio**: Lisätty OWASP MCP Top 10 -tietoturvariskitaulukko Azure:n lievennyksillä pääasialliseen Turvallisuus-README:hen
- **Riskipohjainen dokumentaatio**: Päivitetty mcp-security-controls-2025.md sisältämään OWASP MCP -riskiviitteet (MCP01-MCP08) jokaiseen turvallisuusalueeseen
- **Viitearkkitehtuuri**: Linkitetty OWASP MCP Azure Security Guide -viitearkkitehtuuriin ja toteutusmalleihin

#### Päivitetyt tietoturvatiedostot
- **README.md**: Lisätty Sherpa Workshop -yhteenveto, retkeilyreittitaulukko, OWASP MCP Top 10 -riskien yhteenveto ja käytännön koulutusosio
- **mcp-security-controls-2025.md**: Päivitetty otsikko helmikuuhun 2026, lisätty OWASP-riskiviitteet (MCP01-MCP08), korjattu määrittelyversion epäjohdonmukaisuus
- **mcp-security-best-practices-2025.md**: Lisätty Sherpa- ja OWASP-resurssit-osio, päivitetty aikaleima
- **mcp-best-practices.md**: Lisätty käytännön koulutusosio Sherpa- ja OWASP-linkkien kanssa
- **azure-content-safety-implementation.md**: Lisätty OWASP MCP06-viite, Sherpa Leiri 3 -yhteensopivuus ja lisäresurssit

#### Uudet resurssilinkit lisätty
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Yksittäiset OWASP MCP riskisivut (MCP01-MCP10)

### Opintokokonaisuuden laajuinen MCP-määrittelyn 2025-11-25 yhdenmukaisuus

#### Moduuli 03 - Aloittaminen
- **SDK-dokumentaatio**: Lisätty Go SDK viralliseksi SDK-listaksi; päivitetty kaikki SDK-viitteet vastaamaan MCP-määrittelyä 2025-11-25
- **Kuljetusten selvennys**: Päivitetty STDIO- ja HTTP Streaming -kuljetuksen kuvaukset eksplisiittisillä määrittelyviitteillä

#### Moduuli 04 - Käytännön toteutus
- **SDK-päivitykset**: Lisätty Go SDK; päivitetty SDK-lista sisältämään määrittelyversion
- **Valtuutusmäärittely**: Päivitetty MCP Authorization -määrittelylinkki nykyiseen 2025-11-25 versioon

#### Moduuli 05 - Edistyneet aiheet
- **Uudet ominaisuudet**: Lisätty huomautus MCP-määrittelyn 2025-11-25 uusista ominaisuuksista (Tasks, Työkalumerkinnät, URL-tilan käynnistys, Roots)
- **Turvallisuusresurssit**: Lisätty OWASP MCP Top 10 ja Sherpa workshop -linkit lisäviitteisiin

#### Moduuli 06 - Yhteisön panokset
- **SDK-lista**: Lisätty Swift- ja Rust-SDK:t; päivitetty määrittelylinkki 2025-11-25
- **Määrittelyviite**: Päivitetty MCP-määrittelylinkki suoraan määrittelyn URL-osoitteeseen

#### Moduuli 07 - Varhaisen käyttöönoton opit
- **Resurssipäivitykset**: Lisätty MCP-määrittely 2025-11-25 linkki ja OWASP MCP Top 10 lisäresursseihin

#### Moduuli 08 - Parhaat käytännöt
- **Määrittelyversio**: Päivitetty MCP-määrittelyreferenssi versioon 2025-11-25
- **Turvallisuusresurssit**: Lisätty OWASP MCP Top 10 ja Sherpa workshop lisäviitteisiin

#### Moduuli 10 - AI-työnkulkujen virtaviivaistaminen
- **Merkki päivitys**: Vaihdettu MCP-version merkki SDK-version (1.9.3) sijaan määrittelyversion (2025-11-25) mukaiseksi
- **Resurssilinkit**: Päivitetty MCP-määrittelylinkki; lisätty OWASP MCP Top 10

#### Moduuli 11 - MCP-palvelimen käytännön labrat
- **Määrittelyviite**: Päivitetty MCP-määrittelylinkki versioon 2025-11-25
- **Turvallisuusresurssit**: Lisätty OWASP MCP Top 10 virallisiksi resursseiksi

## 18. joulukuuta 2025
### Turvallisuusdokumentaation päivitys - MCP-spesifikaatio 2025-11-25

#### MCP:n turvallisuuden parhaat käytännöt (02-Security/mcp-best-practices.md) - spesifikaatioversion päivitys
- **Protokollaversion päivitys**: Päivitetty viittaus uusimpaan MCP-spesifikaatioon 2025-11-25 (julkaistu 25. marraskuuta 2025)
  - Päivitetty kaikki spesifikaatioversion viittaukset 2025-06-18:sta 2025-11-25:een
  - Päivitetty dokumentin päivämääräviittaukset 18. elokuuta 2025:stä 18. joulukuuta 2025:een
  - Varmistettu, että kaikki spesifikaation URL-osoitteet osoittavat nykyiseen dokumentaatioon
- **Sisällön validointi**: Kattava validointi turvallisuuden parhaista käytännöistä uusimpia standardeja vasten
  - **Microsoftin turvallisuusratkaisut**: Varmistettu nykyiset termit ja linkit Prompt Shields -ominaisuudelle (entinen "Jailbreak risk detection"), Azure Content Safetylle, Microsoft Entra ID:lle ja Azure Key Vaultille
  - **OAuth 2.1:n turvallisuus**: Vahvistettu yhdenmukaisuus uusimpien OAuth-turvallisuuden parhaiden käytäntöjen kanssa
  - **OWASP-standardit**: Tarkistettu, että OWASP Top 10 for LLMs -viittaukset ovat ajan tasalla
  - **Azure-palvelut**: Varmistettu kaikkien Microsoft Azure -dokumentaatioiden linkkien ja parhaiden käytäntöjen ajantasaisuus
- **Standardien yhdenmukaisuus**: Kaikki viitatut turvallisuusstandardit vahvistettu ajan tasalle
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure-turvallisuus- ja vaatimustenmukaisuuskehykset
- **Toteutusresurssit**: Vahvistettu kaikkien toteutusoppaiden linkkien ja resurssien ajantasaisuus
  - Azure API Managementin todennustavat
  - Microsoft Entra ID:n integraatio-oppaat
  - Azure Key Vaultin salaisuuksien hallinta
  - DevSecOps-putket ja monitorointiratkaisut

### Dokumentaation laadunvarmistus
- **Spesifikaation noudattaminen**: Varmistettu, että kaikki pakolliset MCP:n turvallisuusvaatimukset (MUST/MUST NOT) ovat yhdenmukaisia uusimman spesifikaation kanssa
- **Resurssien ajantasaisuus**: Tarkistettu kaikkien ulkoisten linkkien toimivuus Microsoftin dokumentaatioihin, turvallisuusstandardeihin ja toteutusoppaisiin
- **Parhaiden käytäntöjen kattavuus**: Vahvistettu kattava käsittely todennuksesta, valtuutuksesta, tekoälyyn liittyvistä uhista, toimitusketjun turvallisuudesta ja yrityskäytön malleista

## 6. lokakuuta 2025

### Aloitusosion laajennus – Edistynyt palvelimen käyttö ja yksinkertainen todennus

#### Edistynyt palvelimen käyttö (03-GettingStarted/10-advanced)
- **Uusi luku lisätty**: Laaja opas edistyneeseen MCP-palvelimien käyttöön, kattaen sekä tavanomaiset että matalan tason palvelinarkkitehtuurit.
  - **Tavanomainen vs. matalan tason palvelin**: Yksityiskohtainen vertailu sekä koodiesimerkit Pythonilla ja TypeScriptilä molemmille lähestymistavoille.
  - **Handler-pohjainen suunnittelu**: Selitys handler-pohjaisesta työkalujen/resurssien/kehotteiden hallinnasta skaalautuvien ja joustavien palvelinratkaisujen toteutuksessa.
  - **Käytännön mallit**: Todelliset käyttötapaukset, joissa matalan tason palvelinmallit tarjoavat hyötyä edistyneiden ominaisuuksien ja arkkitehtuurien rakentamisessa.

#### Yksinkertainen todennus (03-GettingStarted/11-simple-auth)
- **Uusi luku lisätty**: Askeltainen opas yksinkertaisen todennuksen toteuttamiseen MCP-palvelimissa.
  - **Todennuskonseptit**: Selkeä selitys todennuksen ja valtuutuksen eroista sekä tunnistetietojen käsittelystä.
  - **Perustason todennuksen toteutus**: Middleware-pohjaiset todennuskäytännöt Pythonissa (Starlette) ja TypeScriptissä (Express) koodiesimerkkien kera.
  - **Eteneminen kehittyneempään turvallisuuteen**: Ohjeet aloittamiseen yksinkertaisella todennuksella ja etenemiseen OAuth 2.1:een ja RBAC:iin, viittauksilla edistyneisiin turvallisuusmoduuleihin.

Nämä lisäykset tarjoavat käytännönläheistä opastusta MCP-palvelintoteutusten vahvistamiseksi, turvallisuuden ja joustavuuden lisäämiseksi yhdistäen perustavanlaatuiset konseptit edistyneisiin tuotantomalleihin.

## 29. syyskuuta 2025

### MCP-palvelimen tietokantaintegrointilaboratoriot – Kattava käytännön oppimispolku

#### 11-MCPServerHandsOnLabs – uusi täydellinen tietokantaintegrointikurssi
- **Täydellinen 13-laboratoriokurssi**: Laajennettu kattava käytännön kurssi tuotantovalmiiden MCP-palvelimien rakentamiseen PostgreSQL-tietokantaintegroinnilla
  - **Todellisen maailman toteutus**: Zava Retail -analytiikkatapaus, joka demonstroi yritystason malleja
  - **Rakenteellinen oppimisen eteneminen**:
    - **Laboratoriot 00-03: Perusteet** – Johdanto, ydinar­kitehtuuri, turvallisuus ja moni-asiakkuus, ympäristön asennus
    - **Laboratoriot 04-06: MCP-palvelimen rakentaminen** – Tietokannan suunnittelu ja skeema, MCP-palvelimen toteutus, työkalujen kehitys
    - **Laboratoriot 07-09: Edistyneet ominaisuudet** – Semanttinen haku, testaus ja virheenetsintä, VS Coden integrointi
    - **Laboratoriot 10-12: Tuotanto ja parhaat käytännöt** – Julkaisu­strategiat, monitorointi ja havaittavuus, parhaat käytännöt ja optimointi
  - **Yritysteknologiat**: FastMCP-framework, PostgreSQL pgvectorillä, Azure OpenAI upotukset, Azure Container Apps, Application Insights
  - **Edistyneet ominaisuudet**: Platautasolla tietoturva (RLS), semanttinen haku, moni-asiakkaan tietojen käyttö, vektoriupotukset, reaaliaikainen monitorointi

#### Terminologian yhtenäistäminen – moduulista laboratorioon
- **Kattava dokumentaatiopäivitys**: Järjestelmällisesti päivitetty kaikki README-tiedostot 11-MCPServerHandsOnLabs-kansiossa korvaamaan "Module" sanalla "Lab"
  - **Otsikkotasot**: Päivitetty "What This Module Covers" muotoon "What This Lab Covers" kaikissa 13 laboratoriossa
  - **Sisältökuvaus**: Muutettu "This module provides..." muotoon "This lab provides..." koko dokumentaatiossa
  - **Oppimistavoitteet**: Päivitetty "By the end of this module..." muotoon "By the end of this lab..."
  - **Navigointilinkit**: Muutettu kaikki "Module XX:" viitteet muotoon "Lab XX:" ristiinviittauksissa ja navigaatiossa
  - **Suorituksen seuranta**: Päivitetty "After completing this module..." muotoon "After completing this lab..."
  - **Teknisten viitteiden säilyttäminen**: Säilytetty Python-moduuliviittaukset konfiguraatiotiedostoissa (esim. `"module": "mcp_server.main"`)

#### Opasopintojen parannus (study_guide.md)
- **Visuaalinen kurssikartta**: Lisätty uusi "11. Database Integration Labs" -osio sisältäen kattavan laboratoriorakenteen visualisoinnin
- **Repositorion rakenne**: Päivitetty kymmenestä yhdelletoista pääosioon yksityiskohtaisella 11-MCPServerHandsOnLabs-kuvauksella
- **Oppimispolun ohjeistus**: Parannettu navigointi kattamaan osiot 00-11
- **Teknologian kattavuus**: Lisätty FastMCP, PostgreSQL, Azure-palveluiden integraatioiden tiedot
- **Oppimistulokset**: Korostettu tuotantovalmiiden palvelimien kehittämistä, tietokantaintegroinnin malleja ja yritysturvallisuutta

#### Pää-README-rakenteen parannus
- **Laboratoriopohjainen terminologia**: Päivitetty pää-README.md tiedosto 11-MCPServerHandsOnLabs-kansiossa käyttämään johdonmukaisesti "Lab"-rakennetta
- **Oppimispolun organisointi**: Selkeä eteneminen perustavanlaatuisista konsepteista edistyneeseen toteutukseen ja tuotantoon julkaisuun
- **Todellisen maailman painotus**: Korostus käytännön, laboratorioon perustuvan oppimisen, yritystason mallien ja teknologioiden hyödyntämiseen

### Dokumentaation laadun ja yhdenmukaisuuden parannukset
- **Käytännönläheinen oppiminen**: Vahvistettu laboratoriopohjaista lähestymistapaa dokumentaation kaikissa osissa
- **Yritysmallit**: Korostettu tuotantovalmiita toteutuksia ja yritysturvallisuusnäkökulmia
- **Teknologian integrointi**: Kattava käsittely modernien Azure-palveluiden ja tekoälyintegraatiomallien osalta
- **Oppimisen eteneminen**: Selkeät, rakenteelliset polut peruskonsepteista tuotantoon asti

## 26. syyskuuta 2025

### Case-tutkimusten laajennus – GitHub MCP Registry -integraatio

#### Case Studies (09-CaseStudy/) – Ekosysteemin kehityksen painopiste
- **README.md**: Merkittävä laajennus kattavalla GitHub MCP Registry -case-tutkimuksella
  - **GitHub MCP Registry -case-tutkimus**: Uusi kattava case-tutkimus syventäen GitHubin MCP Registry -käyttöönottoa syyskuussa 2025
    - **Ongelman analyysi**: Yksityiskohtainen tarkastelu hajautetun MCP-palvelimen löytämisen ja käyttöönoton haasteista
    - **Ratkaisuarkkitehtuuri**: GitHubin keskitetty rekisteriratkaisu yhdellä klikkauksella tehtävään VS Code -asennukseen
    - **Liiketoiminnan vaikutus**: Mitattavissa olevat parannukset kehittäjien perehdytyksessä ja tuottavuudessa
    - **Strateginen arvo**: Painotus modulaaristen agenttien käyttöönotossa ja työkalujen välisessä yhteentoimivuudessa
    - **Ekosysteemin kehitys**: Siirtyminen perustavanlaatuiseksi alustaksi agenttipohjaisille integraatioille
  - **Parannettu case-tutkimusten rakenne**: Kaikkien seitsemän case-tutkimuksen yhtenäistetty muotoilu ja kattavat kuvaukset
    - Azure AI Travel Agents: Moni-agenttiorkestroinnin painotus
    - Azure DevOps -integraatio: Työnkulkujen automatisointi
    - Reaaliaikainen dokumenttien haku: Python-konsolisovellus
    - Interaktiivinen opintosuunnitelman generaattori: Chainlit-keskusteleva web-sovellus
    - Editorin sisäinen dokumentaatio: VS Code ja GitHub Copilot -integraatio
    - Azure API Management: Yrityksen API-integraatiomallit
    - GitHub MCP Registry: Ekosysteemin kehitys ja yhteisöalusta
  - **Kattava yhteenveto**: Kirjoitettu uudelleen yhteenveto-osio, joka korostaa seitsemää eri MCP-toteutusten ulottuvuutta käsittävää case-tutkimusta
    - Yritysintegraatio, moni-agenttiorcestrointi, kehittäjien tuottavuus
    - Ekosysteemin kehitys, opetussovellusten luokittelu
    - Syvälliset näkemykset arkkitehtonisista malleista, toteutusstrategioista ja parhaista käytännöistä
    - Painotus MCP:n kypsyyteen, tuotantovalmiuteen protokollana

#### Opasopinto-päivitykset (study_guide.md)
- **Visuaalinen kurssikartta**: Päivitetty miellekartta sisältämään GitHub MCP Registry Case Studies -osiossa
- **Case-tutkimusten kuvaus**: Laajennettu geneerisistä kuvauksista seitsemän kattavan tapaustutkimuksen yksityiskohtiin
- **Repositorion rakenne**: Päivitetty osio 10 heijastamaan kattavaa case-tutkimusten sisältöä ja yksittäisiä toteutustietoja
- **Muutoslokikirjan integrointi**: Lisätty 26.9.2025 merkintä dokumentoimaan GitHub MCP Registry -lisäys ja case-tutkimusten parannukset
- **Päivämääräpäivitykset**: Päivitetty alaviitteen aikaleima vastaamaan viimeisintä versiota (26. syyskuuta 2025)

### Dokumentaation laadun parannukset
- **Yhdenmukaisuuden vahvistus**: Case-tutkimusten yhtenäinen muotoilu ja rakenne kaikissa seitsemässä esimerkissä
- **Kattava käsittely**: Case-tutkimukset kattavat nyt yritys-, kehittäjätuottavuus- ja ekosysteemin kehitystilanteet
- **Strateginen asema**: Korostettu MCP:n roolia perustavana agenttipohjaisten järjestelmien alustana
- **Resurssien integrointi**: Päivitetty lisäresurssit sisältämään GitHub MCP Registry -linkin

## 15. syyskuuta 2025

### Edistyneet aiheet laajennus – Räätälöidyt kuljetukset ja kontekstitekniikka

#### MCP räätälöidyt kuljetukset (05-AdvancedTopics/mcp-transport/) – uusi edistynyt toteutusopas
- **README.md**: Täydellinen toteutusopas custom MCP -kuljetusmekanismeihin
  - **Azure Event Grid -kuljetus**: Kattava palvelimettoman tapahtumaohjatun kuljetuksen toteutus
    - C#, TypeScript ja Python -esimerkit Azure Functions -integraatiolla
    - Tapahtumaohjatun arkkitehtuurin mallit skaalautuviin MCP-ratkaisuihin
    - Webhook-vastaanottimet ja push-pohjainen viestien käsittely
  - **Azure Event Hubs -kuljetus**: Korkean läpimenon suoratoistokuljetuksen toteutus
    - Reaaliaikaisen suoratoiston mahdollisuudet matalan viiveen tilanteisiin
    - Osiointistrategiat ja checkpoint-hallinta
    - Viestien ryhmittely ja suorituskyvyn optimointi
  - **Yritysintegraation mallit**: Tuotantovalmiit arkkitehtuuriesimerkit
    - Hajautettu MCP-käsittely useissa Azure Functions -instansseissa
    - Hybridikuljetusarkkitehtuurit, jotka yhdistävät useita kuljetustyyppejä
    - Viestien kestävyys-, luotettavuus- ja virheenkäsittelystrategiat
  - **Turvallisuus ja monitorointi**: Azure Key Vault -integraatio ja havaittavuuden mallit
    - Hallinnoidun identiteetin todennus ja vähimmän etuoikeuden käyttöoikeudet
    - Application Insights -telemetria ja suorituskyvyn monitorointi
    - Virtapiirikatkaisijat ja vikasietoisuusmallit
  - **Testauskehykset**: Kattavat testausstrategiat räätälöidyille kuljetuksille
    - Yksikkötestaus testinkopioilla ja mockauskehyksillä
    - Integraatiotestaus Azure Test Containers -työkaluilla
    - Suorituskyky- ja kuormitustestausnäkökohdat

#### Kontekstitekniikka (05-AdvancedTopics/mcp-contextengineering/) – Nouseva tekoälyn ala
- **README.md**: Kattava katsaus kontekstitekniikkaan nousevana alana
  - **Periaatteet**: Kattava kontekstin jakaminen, toimintapäätösten tietoisuus ja kontekstikehyksen hallinta
  - **MCP-protokollan yhdenmukaisuus**: Kuinka MCP-malli käsittelee kontekstitekniikan haasteita
    - Kontekstikehyksen rajoitukset ja progressiivisen latauksen strategiat
    - Relevanssin määritys ja dynaaminen kontekstin haku
    - Monimodaalinen kontekstin käsittely ja turvallisuusnäkökohdat
  - **Toteutusmenetelmät**: Yhden säikeen vs. moni-agenttiarkkitehtuurit
    - Konstekstikappaleistus ja priorisointitekniikat
    - Progressiivinen kontekstin lataaminen ja pakkausstrategiat
    - Kerroksittainen kontekstin käsittely ja hakun optimointi
  - **Mittauskehys**: Nousevat mittarit kontekstin tehokkuuden arviointiin
    - Syötön tehokkuus, suorituskyky, laatu ja käyttäjäkokemus
    - Kokeelliset lähestymistavat kontekstin optimointiin
    - Virheanalyysi ja parannusmenetelmät

#### Kurssin navigoinnin päivitykset (README.md)
- **Parannettu moduulirakenne**: Päivitetty kurssin taulukko sisältämään uudet edistyneet aiheet
  - Lisätty kontekstitekniikka (5.14) ja räätälöity kuljetus (5.15)
  - Yhdenmukainen muotoilu ja navigointilinkit kaikissa moduuleissa
  - Päivitetyt kuvaukset vastaamaan nykyistä sisältöä

### Hakemistorakenteen parannukset
- **Nimeämisen yhdenmukaisuus**: Nimetty "mcp transport" uudelleen muotoon "mcp-transport" muiden edistynyt-aiheiden kansioiden mukaisesti
- **Sisällön järjestely**: Kaikki 05-AdvancedTopics -kansiot noudattavat nyt yhtenäistä nimeämiskäytäntöä (mcp-[aihe])

### Dokumentaation laadun parannukset
- **MCP-spesifikaation yhdenmukaisuus**: Kaikki uudet sisällöt viittaavat nykyiseen MCP-spesifikaatioon 2025-06-18
- **Monikieliset esimerkit**: Kattavat koodiesimerkit C#, TypeScript- ja Python-kielillä
- **Yrityspainotus**: Tuotantovalmiit mallit ja Azure-pilvi-integraatio koko materiaalissa
- **Visuaalinen dokumentaatio**: Mermaid-kaaviot arkkitehtuurista ja työnkulkujen visualisoinnit

## 18. elokuuta 2025

### Dokumentaation kattava päivitys – MCP 2025-06-18 standardit

#### MCP:n turvallisuuden parhaat käytännöt (02-Security/) – täysi modernisointi
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täydellinen uudelleenkirjoitus, joka on linjassa MCP Specification 2025-06-18 -version kanssa
  - **Pakolliset vaatimukset**: Lisätty eksplisiittiset ONTEHTÄVÄ/ONKIELLETTY-vaatimukset virallisesta spesifikaatiosta selkeillä visuaalisilla merkinnöillä
  - **12 keskeistä turvallisuuskäytäntöä**: Uudelleenjärjestely 15 kohdan listasta kattaviksi turvallisuusalueiksi
    - Token-turvallisuus ja tunnistautuminen ulkoisen identiteettipalveluntarjoajan integraatiolla
    - Istunnon hallinta ja siirtoturvallisuus kryptografisilla vaatimuksilla
    - AI-spesifinen uhkasuojelu Microsoft Prompt Shields -integraatiolla
    - Käyttöoikeuksien hallinta ja oikeudet vähimmän etuoikeuden periaatteella
    - Sisällön turvallisuus ja valvonta Azure Content Safety -integraatiolla
    - Toimitusketjun turvallisuus kattavalla komponenttien tarkistuksella
    - OAuth-turvallisuus ja Confused Deputy -hyökkäyksen estäminen PKCE:n toteutuksella
    - Tapahtumien hallinta ja palautuminen automaattisilla kyvyillä
    - Noudattaminen ja hallinto säädösten mukaisesti
    - Kehittyneet turvallisuusohjaimet nollaluottamusarkkitehtuurilla
    - Microsoftin turvallisuus ekosysteemin integraatio kokonaisvaltaisilla ratkaisuilla
    - Jatkuva turvallisuuden kehitys adaptiivisilla käytännöillä
  - **Microsoftin turvallisuusratkaisut**: Parannettu integraatio-ohjeistus Prompt Shieldsille, Azure Content Safetylle, Entra ID:lle ja GitHub Advanced Securitylle
  - **Toteutusresurssit**: Resurssilinkit järjestetty viralliseen MCP-dokumentaatioon, Microsoftin turvallisuusratkaisuihin, turvallisuusstandardeihin ja toteutusoppaisiin

#### Kehittyneet turvallisuusohjaimet (02-Security/) - Yritystason toteutus
- **MCP-SECURITY-CONTROLS-2025.md**: Täydellinen uudistus yritystason turvallisuuskehikon mukaisesti
  - **9 kattavaa turvallisuusaluetta**: Laajennettu perusohjaimista yksityiskohtaiseen yrityskehikoon
    - Kehittynyt tunnistautuminen ja valtuutus Microsoft Entra ID -integraatiolla
    - Token-turvallisuus ja anti-passthrough-ohjaimet kattavalla validoinnilla
    - Istuntoturvaohjaimet kaappauksen estolla
    - AI-spesifiset turvallisuusohjaimet kehotteen injektiota ja työkalumyrkytyksen estoa varten
    - Confused Deputy -hyökkäyksen estäminen OAuth-välityksen turvaominaisuuksilla
    - Työkalujen suoritusturvallisuus hiekkalaatikoinnilla ja eristyksellä
    - Toimitusketjun turvallisuusohjaimet riippuvuuksien tarkistuksella
    - Valvonta- ja havaitsemisohjaimet SIEM-integraatiolla
    - Tapahtumien hallinta ja palautuminen automaattisilla kyvyillä
  - **Toteutusesimerkit**: Lisätty yksityiskohtaiset YAML-konfiguraatiolohkot ja koodiesimerkit
  - **Microsoft-ratkaisujen integraatio**: Kattava käsittely Azure-turvapalveluille, GitHub Advanced Securitylle ja yritysidentiteetin hallinnalle

#### Edistyneet aihealueet turvallisuus (05-AdvancedTopics/mcp-security/) - Tuotantovalmiit toteutukset
- **README.md**: Täydellinen uudelleenkirjoitus yritysturvallisuuden toteutukseen
  - **Ajantasainen spesifikaatio**: Päivitetty MCP Specification 2025-06-18 mukaiseksi pakollisine turvallisuusvaatimuksineen
  - **Parannettu tunnistautuminen**: Microsoft Entra ID -integraatio, kattavat .NET- ja Java Spring Security -esimerkit
  - **AI-turvallisuusintegraatio**: Microsoft Prompt Shields ja Azure Content Safety yksityiskohtaisilla Python-esimerkeillä
  - **Kehittynyt uhkien lieventäminen**: Kattavat toteutusesimerkit
    - Confused Deputy -hyökkäyksen estäminen PKCE:llä ja käyttäjän suostumuksen validoinnilla
    - Tokenin passthrough’n estäminen kohderyhmän validoinnilla ja turvallisella tokenin hallinnalla
    - Istunnon kaappauksen estäminen kryptografisella sidonnalla ja käyttäytymisanalyysilla
  - **Yritysturvallisuuden integraatio**: Azure Application Insights -valvonta, uhkien havainnointi putket ja toimitusketjun turvallisuus
  - **Toteutuschecklista**: Selkeä erottelu pakollisten ja suositeltujen turvallisuusohjaimien välillä Microsoftin turvallisuus ekosysteemin hyötyineen

### Dokumentaation laatu ja standardien mukaisuus
- **Spesifikaatioviitteet**: Päivitetty kaikki viittaukset MCP Specification 2025-06-18 -versioon
- **Microsoftin turvallisuusekosysteemi**: Parannettu integraatio-ohjeistus kaikissa turvallisuusdokumenteissa
- **Käytännön toteutus**: Lisätty yksityiskohtaiset koodiesimerkit .NET:lle, Javalle ja Pythonille yritysmallien mukaisesti
- **Resurssien organisointi**: Kattava luokittelu viralliselle dokumentaatiolle, turvallisuusstandardeille ja toteutusoppailla
- **Visuaaliset merkinnät**: Selkeät merkinnät pakollisista vaatimuksista ja suositelluista käytännöistä


#### Keskeiset käsitteet (01-CoreConcepts/) - Täysi modernisointi
- **Protokollaversion päivitys**: Päivitetty viittaukset nykyiseen MCP Specification 2025-06-18 -versioon päivämääräpohjaisella versionumerolla (VVVV-KK-PP)
- **Arkkitehtuurin tarkennus**: Parannettu määrittelyjä Hosteista, Clienteista ja Serveista ajantasaisen MCP-arkkitehtuurin mukaisesti
  - Hostit määritelty selkeästi AI-sovelluksiksi, jotka koordinoivat useita MCP-client-yhteyksiä
  - Clientit kuvattu protokollan liitännöiksi, jotka ylläpitävät yksittäisiä serverisuhteita
  - Serverit laajennettu paikalliseen ja etäkäyttöönottoon
- **Primiittien uudelleenjärjestely**: Täydellinen uudistus server- ja client-primiiteistä
  - Server-primiitit: Resurssit (tietolähteet), Promptit (mallipohjat), Työkalut (suoritettavat toiminnot) detaljoituna ja esimerkein
  - Client-primiitit: Otanta (LLM-valmiudet), Tiedon keruu (käyttäjäsyöte), Lokitus (vikadiagnostiikka/valvonta)
  - Päivitetty käyttäen nykyisiä metodimalleja: löytö (`*/list`), haku (`*/get`), suoritukset (`*/call`)
- **Protokollan arkkitehtuuri**: Kahden kerroksen arkkitehtuurimalli
  - Datakerros: JSON-RPC 2.0 pohja elinkaaren hallinnalla ja primitiiveillä
  - Siirtokerros: STDIO (paikallinen) ja Streamable HTTP SSE:llä (etäyhteydet)
- **Turvakehikko**: Kattavat turvallisuusperiaatteet, kuten eksplisiittinen käyttäjän suostumus, tietosuoja, työkalujen turvallinen suoritus ja siirtokerroksen suojaus
- **Kommunikaatiomallit**: Päivitetyt protokollaviestit alustus-, löytö-, suoritus- ja ilmoitusvaiheista
- **Koodiesimerkit**: Päivitetyt monikieliset esimerkit (.NET, Java, Python, JavaScript) nykyisen MCP SDK:n mukaisesti

#### Turvallisuus (02-Security/) - Kattava turvallisuuden uudistus  
- **Standardien mukaisuus**: Täysi yhdenmukaisuus MCP Specification 2025-06-18 mukaisiin turvallisuusvaatimuksiin
- **Tunnistautumisen kehitys**: Dokumentoitu siirtymä räätälöidyistä OAuth-servereistä ulkoisen identiteettipalveluntarjoajan delegointiin (Microsoft Entra ID)
- **AI-spesifinen uhka-analyysi**: Parannettu kattavuus modernien AI-hyökkäysvektorien osalta
  - Yksityiskohtaiset kehotteen injektion hyökkäysskenaariot todellisilla esimerkeillä
  - Työkalujen myrkytysmenetelmät ja "rug pull" -hyökkäysmallit
  - Kontekstikehysmyrkytys ja mallin sekoittumishyökkäykset
- **Microsoftin AI-turvaratkaisut**: Kattava läpikäynti Microsoftin turvallisuus ekosysteemistä
  - AI Prompt Shields kehittyneillä havaitsemis-, valokeilaja ja erotinmenetelmillä
  - Azure Content Safety -integraatiomallit
  - GitHub Advanced Security toimitusketjun suojaukseen
- **Kehittynyt uhkien lieventäminen**: Yksityiskohtaiset turvallisuusohjaimet
  - Istuntojen kaappauksen estäminen MCP-spesifisillä hyökkäysskenaarioilla ja kryptografisilla istunto-ID-vaatimuksilla
  - Confused deputy -ongelmat MCP-proxy-skenaarioissa eksplisiittisillä suostumusvaatimuksilla
  - Token passthrough -haavoittuvuudet pakollisilla validointiohjaimilla
- **Toimitusketjun turvallisuus**: Laajennettu AI-toimitusketjun käsittely, mukaan lukien perustamismallit, upotupalvelut, kontekstin tarjoajat ja kolmannen osapuolen API:t
- **Perusturunneistus**: Parannettu integraatio yritysturvallisuusmallien, kuten nollaluottamuksen arkkitehtuurin ja Microsoftin turvallisuus ekosysteemin kanssa
- **Resurssien organisointi**: Kattava resurssilinkkien luokittelu tyypin mukaan (viralliset dokumentit, standardit, tutkimus, Microsoftin ratkaisut, toteutusoppaat)

### Dokumentaation laadun parannukset
- **Rakenteelliset oppimistavoitteet**: Parannetut oppimistavoitteet konkreettisilla, toteutettavissa olevilla tuloksilla
- **Ristiinlinkitykset**: Lisätty linkityksiä liittyvien turvallisuus- ja ydinkäsitteleiden sisältöjen välillä
- **Ajantasaisuus**: Päivitetty kaikki päivämääräviitteet ja spesifikaatiolinkit nykystandardeihin
- **Toteutusohjeistus**: Lisätty konkreettisia ja toteuttamiskelpoisia ohjeita molempiin osioihin

## 16. heinäkuuta 2025

### README ja navigaation parannukset
- Täydellinen uudelleensuunnittelu oppimateriaalin navigaatioon README.md:ssä
- `<details>`-tunnisteet korvattu saavutettavammilla taulukkopohjaisilla malleilla
- Luotu vaihtoehtoisia ulkoasuvaihtoehtoja uuteen "alternative_layouts" -kansioon
- Lisätty korttipohjaisia, välilehtityylisiä ja harmonikkatyylisiä navigointiesimerkkejä
- Päivitetty repositorion rakenne-osio sisältämään kaikki uusimmat tiedostot
- Parannettu "Miten käyttää tätä oppimateriaalia" -osiota selkeillä suosituksilla
- Päivitetty MCP-spesifikaatiolinkit osoittamaan oikeisiin URL-osoitteisiin
- Lisätty Context Engineering -osio (5.14) oppimateriaalin rakenteeseen

### Opas päivitykset
- Täysin uudistettu opas vastaamaan nykyistä repositorion rakennetta
- Lisätty uudet osiot MCP Klienteille ja Työkaluille sekä Suosituimmat MCP Serverit
- Päivitetty visuaalinen oppimateriaalikartta sisältämään kaikki aiheet tarkasti
- Parannettu edistyneiden aihealueiden kuvauksia kattamaan kaikki erikoistuneet osa-alueet
- Päivitetty tapaustutkimukset vastaamaan todellisia esimerkkejä
- Lisätty tämä kattava muutosten loki

### Yhteisön panokset (06-CommunityContributions/)
- Lisätty yksityiskohtaista tietoa MCP-servereistä kuvan generointiin
- Lisätty kattava osio Clawden käytöstä VSCodessa
- Lisätty Cline-päätelmäasiakkaan asennus- ja käyttöohjeet
- Päivitetty MCP-client-osio sisältämään kaikki suosituimmat asiakasvaihtoehdot
- Parannettu kontribuutiotesimerkit entistä tarkemmilla koodinäytteillä

### Edistyneet aiheet (05-AdvancedTopics/)
- Järjestetty kaikki erikoistuneet aihealuekansiot yhtenäisellä nimityksellä
- Lisätty konteksti-insinöörityön materiaaleja ja esimerkkejä
- Lisätty Foundry-agentin integraatiodokumentaatio
- Parannettu Entra ID -turvallisuusintegraation dokumentaatiota

## 11. kesäkuuta 2025

### Alkuperäinen julkaisu
- Julkaistu ensimmäinen versio MCP for Beginners -oppimateriaalista
- Luotu perusrakenne kaikille 10 pääosalle
- Toteutettu visuaalinen oppimateriaalikartta navigointia varten
- Lisätty aloitusprojektiesimerkit useilla ohjelmointikielillä

### Aloittaminen (03-GettingStarted/)
- Luotu ensimmäiset serverin toteutusesimerkit
- Lisätty ohjeistusta client-kehitykseen
- Sisällytetty ohjeet LLM client -integraatioon
- Lisätty VS Code -integraatiodokumentaatio
- Toteutettu Server-Sent Events (SSE) -serveriesimerkit

### Keskeiset käsitteet (01-CoreConcepts/)
- Lisätty yksityiskohtaista selitystä client-server-arkkitehtuurista
- Luotu dokumentaatio keskeisistä protokollakomponenteista
- Dokumentoitu MCP-viestintämallit

## 23. toukokuuta 2025

### Repositorion rakenne
- Alustettu repositorio perusrakenteella
- Luotu README-tiedostot jokaiselle pääosiolle
- Perustettu käännösinfrastruktuuri
- Lisätty kuvia ja kaavioita

### Dokumentaatio
- Luotu alkuperäinen README.md oppimateriaalin yleiskatsauksella
- Lisätty CODE_OF_CONDUCT.md ja SECURITY.md
- Perustettu SUPPORT.md ohjeilla avun saamiseen
- Luotu alustava opaskirjan rakenne

## 15. huhtikuuta 2025

### Suunnittelu ja kehys
- MCP for Beginners -oppimateriaalin alkuperäinen suunnittelu
- Määritelty oppimistavoitteet ja kohderyhmä
- Luotu 10-osainen oppimateriaalin rakenne
- Kehitetty konseptuaalinen kehys esimerkeille ja tapaustutkimuksille
- Luotu alkuperäiset prototyyppiesimerkit keskeisistä käsitteistä

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattikäännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammatillista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->