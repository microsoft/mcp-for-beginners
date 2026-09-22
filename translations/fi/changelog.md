# Muutosloki: MCP aloittelijoille -opetusohjelma

Tämä dokumentti toimii merkintänä kaikista merkittävistä muutoksista, jotka on tehty Model Context Protocol (MCP) aloittelijoille -opetusohjelmaan. Muutokset on dokumentoitu käänteisessä kronologisessa järjestyksessä (uusimmat muutokset ensin).

## 9. syyskuuta 2026

### MCP 2026-07-28 lopullisen määritelmän yhdenmukaistus

Päivitettiin englanninkielinen opetusohjelma beta-versiosta ja `2025-11-25`
perussuuntaohjeista lopulliseen MCP `2026-07-28` määritykseen.

- **Päivitetty**: Nykyversion viitteet, määrityksen linkit, tilattoman
  pyynnön ohjeistus, `server/discover`, striimattavat HTTP-otsikot ja Tasks-laajennuksen
  elinkaari 38 englanninkielisessä dokumentaatiotiedostossa.
- **Korjattu**: Elicitation käyttää nyt `elicitation/create`, Sampling käyttää
  `sampling/createMessage` ja `InputRequiredResult.resultType` käyttää
  arvoa `"input_required"`.
- **Korvattu**: Epätarkka Root Contextin keskustelutilakappale on vaihdettu
  protokollan mukaisella Roots-opetuksella, joka kattaa informaatiojärjestelmän vihjeet,
  nykyisen monikierrosvirran, turvallisuusrajat ja migraatiovaihtoehdot.
- **Selkeytetty**: Roots, Sampling, Logging ja Dynamic Client Registration ovat
  vanhentuneita `2026-07-28`:ssa, ja niiden suositellut korvaajat sekä aikaisin
  poistopäivä on dokumentoitu.
- **Merkattu**: Näytteet, jotka edelleen riippuvat MCP `2025-11-25`:stä, HTTP+SSE:stä,
  aloituskättelyistä tai protokollasessioista on säilytetty perintöyhteensopivuusesimerkkeinä,
  eikä niitä esitetä nykyisinä toteutuksina.
- **Turvaohjeistus**: Päivitettiin itsenäiset turvaoppaat käyttämään
  pyynnön lupausta ja eksplisiittisiä sovellustilan käsittelytapoja poistettujen
  protokollasessio-ID:iden sijaan. Client ID Metadata Documents on nyt
  suositeltu rekisteröitymissuunta, ja DCR on dokumentoitu yhteensopivuusratkaisuna.
- **Tukimateriaali**: Päivitettiin opetusopas, kontribuuttorin tarkistuslista,
  Publora-tapaustutkimus ja APIM-tapaustutkimus. APIM-kävely suosittelee nyt
  nykyistä striimattavaa HTTP `/mcp` päätteensä deprecated `/sse`:n sijaan.
- **Kanonaaliset linkit**: Korvattiin eläkkeelle jääneet ja luonnosmääritysten
  URL-osoitteet englanninkielisessä lähdemarkdownissa versioituihin `2026-07-28`
  linkkeihin, samalla säilyttäen selkeät linkit perintöversioihin, joissa näyte on
  edelleen sidottu vanhempaan työkalupinoon.
- **Vakaat tiedostonimet**: Nimettiin lopullinen määritysohje ja kaksi turvaopasta
  uudelleen poistamalla beta-versioon ja vuosi-lisäys, ja päivitettiin kaikki englanninkieliset
  hyperlinkit vakaisiin polkuihin.
- **Uusi valtuutusesimerkki**: Lisättiin testattu
  [TypeScript MCP `2026-07-28` resurssipalvelin](./02-Security/samples/cimd-dcr-auth/README.md),
  joka vertailee suositeltuja Client ID Metadata Documents -lomakkeita poistettuun Dynamic
  Client Registration -varavertailuun. Esimerkissä on RFC 9728 -löytö, JWKS
  validointi, työkalukohtaiset scopet, kaksitoista testiä ja Auth0:n asetusopastus.
- **Käännösalue**: Muokattiin vain englanninkielisiä lähdetiedostoja; automaattisesti






Lisättiin toimittajariippumaton seuraluesimerkki MCP-työkaluille, jotka luovat todenmukaisia


- **Uusi**: [kestävyys-sivuvaunu seuralesson][reliability-sidecar]
  käyttää yhtä tukipyyntöä koskevaa tarinaa, kahta Mermaid-kaaviota ja uudelleenyritys-
  päätösprosessia selittääkseen vakaat toimintojen avaimet, atomisen kaksoiskäsittelyn,
  yhteen sovituksen, todisteet ja Tasks-laajennuksen rajapinnan.
- **Uusi**: Standardikirjaston Python- ja SQLite-vikainjektioharjoitus
  käyttää erillisiä operaatio- ja lähetysvarastoja havainnollistaen, kuinka vastaus menetetään
  ulkoisen vaikutuksen sitoutuessa. Kuusi determinististä testiä käsittelevät naïvia
  kopiointia, suojattua uudelleenkäynnistys-palautusta, kuormakonflikteja, välimuistissa olevia tuloksia,
  aktiivisia vaateita ja samanaikaista kaksoiskäsittelyä.
- **Päivitetty**: Moduuli 08 linkittää nyt seuraluokkauksen, tunnistaa
  lopullisen `2026-07-28` tilattoman pyynnön mallin, erottaa OpenTelemetry-observoinnin
  MCP:n vanhentuneesta kirjausominaisuudesta ja rajoittaa yleisen uudelleenyritys-
  esimerkkinsä vain lukuoperaatioihin.
- **Valinnainen**: Oppitunti yhdistää siirrettävät käsitteensä nimettyyn yhteisön
  toteutukseen ilman, että isännöity palvelu tai verkkokutsu olisi osa harjoitusta.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. heinäkuuta 2026

### Uusi oppitunti: 2026-07-28 MCP määrityksen beta-versio

Lisättiin kattavuus tulevasta `2026-07-28` MCP-määrityksen beta-versiosta (ilmoitettu 21. toukokuuta 2026; lopullinen julkaisu aikataulutettu 28. heinäkuuta 2026), tiivistettynä [virallisesta tiedoteblogista](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Opetusohjelman perusta pysyy **MCP Specification 2025-11-25** -versiossa uuden version julkaisuun asti, joten tätä esitetään eteenpäin katsovana ohjeistuksena, ei vanhojen oppituntien uudelleenkirjoituksena.

- **Uusi**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — täydellinen oppitunti, joka kattaa tilattoman protokollan ytimen (`initialize`-kättelyn ja `Mcp-Session-Id`:n poistamisen), uudet `Mcp-Method`/`Mcp-Name` reititysotsikot, `ttlMs`/`cacheScope` välimuistimetatiedot, W3C Trace Contextin `_meta`:ssa, muodollisen Extensions-kehyksen (MCP Apps ja uusi Tasks-laajennus), kuusi valtuutuksen tiukennuksen SEP:iä, Roots/Sampling/Logging-toimintojen käytöstä poistamisen ja siirtymisen täydelliseen JSON Schema 2020-12 -määrittelyyn työkalujen skeemoissa.
- **Päivitetty** eteenpäin suuntautuvilla huomioilla, jotka linkittävät uuteen oppituntiin:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokollaversion huomautus, Sampling/Roots/Logging/Tasks -osiot ja "Mitä seuraavaksi"
  - [02-Security/README.md](./02-Security/README.md): valtuutuksen tiukennuksen huomautus
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): tilattoman siirron huomautus
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Samplingin käytöstäpoiston huomautus
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Kirjauksen käytöstäpoiston ja Tasks-laajennuksen huomautus

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): tilaton/istunnonreititys maininta
  - [README.md](./README.md): "Katse tulevaisuuteen" -muistutus määrittelyosiossa ja uusi `1.1` merkintä opetussuunnitelmataulukossa
  - [study_guide.md](./study_guide.md): eteenpäin katsova kohta Ydinkäsitteet-yleiskatsauksessa ja päivämäärätty liite
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): maininta `mcp-session-id` siirtokartasta ennen tilatonta pyyntömallia
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduulin yleiskatsauksen maininta Juuriympäristöjen/Näytteiden vanhentumisista ja Tehtävät-lisäosasta
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): valtuutuksen tiukennuksen maininta

## 24. kesäkuuta 2026

### Uusi oppitunti: MCP:n käyttö Copilot-sovelluksessa

- [Työkalut-osio](./12-tooling/README.md) Lisätty työkalut-osio.
- [MCP Copilot-sovelluksessa](./12-tooling/01-copilot-app/README.md)

## 16. kesäkuuta 2026

### MCP-määrityksen yhdenmukaistus ja näytteiden validointi

Validoin opetussuunnitelman nykyistä **MCP Specification 2025-11-25** -versiota ja uusimpia virallisia SDK:ita vasten, korjasin vanhentuneet määritysviitteet ja varmistin, että ydinnäytteet rakennetaan ja toimivat edelleen.

#### Määrityksen versiotarkistukset (2025-06-18 / 2025-03-26 → 2025-11-25)

Päivitin englanninkielisen sisällön, jossa vielä väitettiin vanhemman määrityksen olevan *nykyinen/viimeisin* standardi, ja ohjasin linkit kanonisiin `modelcontextprotocol.io` määritysreitteihin:
- **05-AdvancedTopics/mcp-security/README.md**: Päivitetty "Current Standard" banner, johdanto, ydinturvaperiaatteiden otsikko, pakollisvaatimukset-osio, Microsoft Entra ID -osio, Viitteet & Resurssit -linkit ja lopun turvahälytys (8 viitettä) versioon 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Päivitetty Lisäresurssit-määrityslinkki ja "Current Standard" banner versioon 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Korvattu vanhentunut `2025-03-26` turva- ja luottamuslinkki nykyisellä 2025-11-25 tietoturvakäytännöt-sivulla
- **03-GettingStarted/14-sampling/README.md**: Päivitetty virallinen otantadokumentaalilinkki versioon 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Päivitetty preesensissä oleva "nykyinen MCP-määritys" viittaus ja Lisäresurssit-määrityslinkki versioon 2025-11-25 (historialliset SSE-poistumismuistutukset säilytetty tarkkuuden vuoksi)

#### Näytteiden validointi nykyisillä SDK:illa

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` ratkaisi `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` ei tuottanut tyyppivirheitä — olemassa olevat `McpServer`/`StdioServerTransport` API:t pysyvät voimassa
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validointi eristetyssä `.venv`:ssä `mcp[cli]` (1.27.2) versioilla; `py_compile` suoritettu ja `FastMCP.list_tools()` palautti oikein `add` ja `subtract` työkalut
- Kaikki näytekohtaiset `@modelcontextprotocol/sdk` versioalueet (`>=1.26.0` / `^1.26.0` / `^1.27.0`) ratkaistaan puhtaasti nykyiseen `1.29.0`:aan ilman rikovia API-muutoksia

#### Riippuvuuden versiotäsmäys (kuiluversioiden sulkeminen)

Päivitettiin vanhentuneet SDK-versiot niin, että jokainen näyte seuraa ajankohtaista MCP-julkaisua, vastaavasti koko repositorion käytäntöön:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Päivitetty `@modelcontextprotocol/sdk` versiosta `^1.8.0` → `>=1.26.0` ja vanhentunut `"updated for MCP 2025-06-18"` paketin kuvaus muotoon `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ja **lab4/code/github_mcp_server/pyproject.toml**: Tarkka versiotäsmä `mcp==1.23.0` nostettu versioon `mcp>=1.26.0`; generoitu uudelleen molemmat `uv.lock` tiedostot (`uv lock`), jotta lukitustiedostot vastaavat nykyistä `mcp 1.27.2` ja pysyvät synkronoituina manifestien kanssa

#### Opetussuunnitelman aukkoanalyysi — Uusimman määrityksen ominaisuuksien kattavuus

Varmistettiin opetussuunnitelman kattavan jo kaikki MCP 2025-11-25 -versiossa lisätyt/laajennetut perusominaisuudet, joten sisältöaukkoja ei ole:
- **Otantat**: Oppitunnit 03-GettingStarted/14-sampling sekä 05-AdvancedTopics/mcp-sampling
- **Saaminen (sisältäen URL-tilan)**: Dokumentoitu 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features osioissa
- **Juuret**: Dokumentoitu 00-Introduction, 01-CoreConcepts ja 05-AdvancedTopics/mcp-root-contexts osioissa
- **Tehtävät (kokeelliset, pitkään kestävät toiminnot)**: Dokumentoitu 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features osioissa
- **Työkalujen annotaatiot** (`readOnlyHint` / `destructiveHint`): Dokumentoitu 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features osioissa

### Turvallisuuden tiukennus ja riippuvuuksien haavoittuvuuksien korjaus

Suoritettu täysi turvallisuustarkastus kaikissa riippuvuuksien manifesteissa ja esimerkkien lähdekoodissa, korjattu kaikki ilmoitetut npm-varoitukset ja yksi kooditasoinen löydös. Korjauksen jälkeen `npm audit` raportoi **0 haavoittuvuutta** kaikissa tarkastetuissa hakemistoissa.

#### npm-riippuvuuksien haavoittuvuudet (epäsuorat) — Korjattu

Tarkastettu kaikki 15 sitoutettua `package-lock.json` tiedostoa. Haavoittuvuudet rajoittuivat MCP Inspector kehitystyökaluun, OpenAI-asiakasohjelmaan ja MCP SDK:hon liittyviin epäsuoriin riippuvuuksiin; kaikki korjattu rikkoutumatta näytteitä:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ja **lab3/code/weather_mcp/inspector**: Korotettiin `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), mikä poisti mukana tulevat `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ja `ws` turvallisuusvaroitukset. Lisättiin npm:n `overrides`-merkintä, joka pakottaa korjatun `shell-quote@1.8.4` käytön eliminoidakseen jäljellä olevan kriittisen varoituksen, jonka aiheutti `concurrently`; generoitiin uudelleen molemmat lukituspaketit (nyt 0 haavoittuvuutta)
- **03-GettingStarted/samples/typescript**: `npm audit fix` päivitti transitiivisen `qs` (keskitaso) korjattuun julkaisuun
- **03-GettingStarted/samples/javascript**: `npm audit fix` päivitti transitiivisen `hono` (keskitaso) korjattuun julkaisuun
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` päivitti transitiivisen `form-data` (korkea) korjattuun julkaisuun
- **03-GettingStarted/11-simple-auth/solution/typescript**: Luotiin puuttuva `package-lock.json`, jotta projekti on toistettavissa ja auditoitavissa (0 haavoittuvuutta)

#### Kooditason tietoturvakorjaus (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Poistettu `shell=True` `open_in_vscode`-työkalusta. Aiempi `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` sallitsi shellin metamerkkien tulkinnan kansiopolussa `cmd.exe`:n toimesta (komentoinjektio-pinta). Nyt se käynnistää suoraan selvitetyn `Code.exe`-ohjelman kansiopolun argumenttina — ilman shelliä — mikä on toiminnallisesti vastaava ja turvallinen

#### Python-riippuvuuksien auditointi

- Auditoitu jokainen Python-vaatimuskokonaisuus `pip-audit`-työkalulla. `05-AdvancedTopics` ja `03-GettingStarted/samples/python` raportoivat **ei tunnettuja haavoittuvuuksia** (heidän `mcp` / `httpx` / `pydantic` / `python-dotenv` -versiot ratkeavat nykyisiin korjattuihin julkaisuihin)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` havaitsi transitiivisen riippuvuuden **`werkzeug` 3.1.1** kolmella `safe_join` Windows-laitteenimen DoS-varoituksella — `CVE-2025-66221`, `CVE-2026-21860`, ja `CVE-2026-27199` (kaikki korjattu versiossa 3.1.6). Lisätty eksplisiittinen turvallisuuspin `werkzeug>=3.1.6`, jotta korjattu julkaisu ratkeaa; varmistettu, että rajoite ratkeaa siististi `chainlit` / `mcp` / `semantic-kernel` -pinon kanssa

### Tuotemerkin uudelleenbrändäys

Päivitetty kaikki opetussisällöt heijastamaan Microsoftin tuotemerkin uudelleenbrändäystä:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Päivitetty Discord-yhteisön linkki
- **AGENTS.md**: Päivitetty Discord-palvelimen viittaus
- **README.md**: Päivitetty teknologiaekosysteemiviittaukset
- **study_guide.md**: Päivitetty tapaustutkimusviittauksia
- **05-AdvancedTopics/README.md**: Päivitetty Moduuli 5.13 otsikko ja kuvaus
- **05-AdvancedTopics/mcp-integration/README.md**: Päivitetty osaston otsikko ja kuvaus
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Täysi moduulin otsikon ja sisällön päivitys
- **05-AdvancedTopics/mcp-security-entra/README.md**: Päivitetty ristiviittauslinkki
- **07-LessonsfromEarlyAdoption/README.md**: Päivitetty tapaustutkimusviittauksia
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Päivitetty osio 9 otsikko, badge-tunnisteet ja ominaisuudet
- **08-BestPractices/README.md**: Päivitetty Discord-yhteisön linkki
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Päivitetty Discord-kanavan viittaus
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Päivitetty mallin käyttöönoton viittaus
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Päivitetty AI-palvelujen taulukko
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Päivitetty resurssiviittaukset

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Päivitetty pääopetussisällön viittaukset
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Päivitetty moduulin otsikko, yleiskuvaus ja kaikki moduulin otsikot
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Päivitetty otsikko, oppimistavoitteet, asennusohjeet ja resurssit
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Päivitetty otsikko, oppimistavoitteet, MCP-hostien taulukko ja ristiviittaukset
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Päivitetty otsikko, badge:t, esivaatimukset ja resurssit
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Päivitetty Agent Builder -viittaukset ja palautelinkki
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Päivitetty esivaatimukset ja lisäosien viittaukset

---

## 11. huhtikuuta 2026

### Uusi oppitunti, dokumentaation korjauksia ja riippuvuuspäivityksiä

#### Uutta opetussisältöä lisätty

**Moduuli 05 - Edistyneet aiheet**
- **Oppitunti 5.17: Vihamielinen moniedustelijoiden päättely MCP:llä** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Uusi kattava opas moniedustelijajärjestelmien vihamieliseen väittelymalliin
  - Mermaid-arkkitehtuuridiagrammi: kaksi agenttia → jaettu MCP-palvelin → väittelytallenne → tuomari → ratkaisu
  - Jaettu MCP-työkalupalvelin (`web_search` + `run_python`) toteutettu Pythonilla ja TypeScriptillä
  - Vastakkaiset järjestelmäkehotteet (PUOLESTA / VASTAAN / Tuomari) eksplisiittisillä työkalujen käyttövaatimuksilla
  - Väittelyn orkestroija Pythonilla, TypeScriptillä ja C#:lla, joka hallinnoi kierroksia ja argumenttien reititystä
  - MCP:n `ClientSession`-kytkentä orkestroijalle todellisiin työkalukutsuihin
  - Käyttötapaustaulukko (harhakuvien tunnistus, uhkamallinnus, API-suunnittelun tarkistus, tosiasioiden varmistus, teknologian valinta)
  - Turvallisuusnäkökohdat: hiekkalaatikkosuoritus, työkalukutsujen vahvistus, nopeuden rajoitus, auditointilokit
  - Rakenteellinen harjoitus kolmella käytännön skenaariolla (koodikatselmointi, arkkitehtuuripäätös, sisällön valvonta)

#### Dokumentaation korjauksia

**Moduuli 03 - Aloittaminen**
- **05-stdio-server/README.md**: Korjattu puutteellinen TypeScript stdio -palvelinohje — lisätty puuttuva kuljetuksen ilmentäminen (`new StdioServerTransport()`) ja `server.connect(transport)`-kutsu vastaamaan Python- ja .NET-esimerkkejä samassa osiossa
- **14-sampling/README.md**: Korjattu kirjoitusvirhe — korjattu `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Opetussisältöpäivitykset

**Pää-README.md**
- Lisätty kohta 5.17 (Vihamielinen moniedustelijoiden päättely MCP:llä) opetuksen taulukkoon suoraan linkitettynä uuteen oppituntiin

**05-AdvancedTopics/README.md**
- Lisätty oppitunti 5.17 rivinä oppituntien taulukkoon

**study_guide.md**
- Lisätty Vihamielisen moniedustelijoiden päättelyn aihe mielenkarttaan ja edistyneiden aiheiden kuvaukseen

#### Koodi- ja tietoturvakorjauksia

**Moduuli 05 - Vihamieliset agentit (`mcp-adversarial-agents`)**
- **Turvallisuuskorjaus — komento-injektio**: Vaihdettu `execSync`-shellinterpolaatio `execFile` + `promisify` -yhdistelmään TypeScript `run_python` -työkalussa, poistaen komentoinjektio-altaan (LLM-ohjattu koodi välitetään nyt kirjaimellisena argv-elementtinä ilman shellin väliintuloa)
- **MCP-työkalusilmukan kytkennät**: Päivitetty Python-väittelyn orkestroija käyttämään `AsyncAnthropic`-asiakasta (korvaten synkronisen estävän `Anthropic`in), välittämään live-`ClientSession`-objekti suoraan jokaiselle agentin vuorolle, hakemaan työkalu-definedit `session.list_tools()`-kutsulla joka vuorolla, ja välittämään `tool_use`-lohkoja `session.call_tool()`-kutsulla silmukassa, kunnes malli antaa lopullisen tekstivastauksen

#### Riippuvuuspäivitykset

- Korotettu `hono` versioon 4.12.12 useassa paketissa (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Korotettu `@hono/node-server` versiosta 1.19.11 versioon 1.19.13 TypeScript-paketeissa
- Korotettu `cryptography` versiosta 46.0.5 versioon 46.0.7 Python-paketeissa (10-StreamliningAIWorkflows lab3 ja lab4)
- Korotettu `lodash` versiosta 4.17.23 versioon 4.18.1 10-StreamliningAIWorkflows inspectorissa

#### Käännökset

- Synkronoitu yli 48 kielen käännökset viimeisimpien lähdemuutosten kanssa (i18n-päivitys)

---

## 5. helmikuuta 2026

### Repositorion laajuinen validointi- ja navigointiparannuksia

#### Uutta opetussisältöä lisätty

**Moduuli 03 - Aloittaminen**
- **12-mcp-hosts/README.md**: Uusi kattava opas MCP-hostien asettamiseen
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf -konfiguraatioesitykset
  - JSON-konfiguraatiomallit kaikille suurimmille hosteille
  - Kuljetustyyppien vertailutaulukko (stdio, SSE/HTTP, WebSocket)
  - Yleisten yhteysongelmien vianmääritys
  - Turvallisuuden parhaat käytännöt hostin konfiguroinnissa

- **13-mcp-inspector/README.md**: Uusi vianmääritysopas MCP Inspectorille
  - Asennusmenetelmät (npx, npm globaali, lähdekoodi)
  - Yhteydet palvelimiin stdio ja HTTP/SSE:n kautta
  - Testausvälineet, resurssit ja kehotteiden työnkulut
  - VS Code -integraatio MCP Inspectoriin
  - Tavalliset vianmääritystilanteet ja ratkaisut

**Moduuli 04 - Käytännön toteutus**
- **pagination/README.md**: Uusi sivutuksen toteutusopas
  - Kurssipohjaiset sivutuskäytännöt Pythonilla, TypeScriptillä, Javalla
  - Asiakaspään sivutuksen käsittely
  - Kurssisuunnittelustrategiat (läpinäkymätön vs. jäsennelty)
  - Suorituskyvyn optimointisuositukset

**Moduuli 05 - Edistyneet aiheet**
- **mcp-protocol-features/README.md**: Uudet protokollan ominaisuudet perusteellisesti
  - Edistymisilmoitusten toteutus
  - Pyyntöjen peruutusmallit
  - Resurssipohjat URI-kaavioilla
  - Palvelimen elinkaaren hallinta
  - Lokitustason hallinta
  - Virheenkäsittelymallit JSON-RPC-koodeilla

#### Navigointikorjauksia (päivitetty 24+ tiedostoa)

**Päämoduulin README:t**
 Nyt linkit sekä ensimmäiseen oppituntiin ETTÄ seuraavaan moduuliin

**02-Security alikansion tiedostot**
- Kaikissa viidessä lisäturvallisuusdokumentissa nyt "Mitä seuraavaksi" -navigointi:

**09-CaseStudy tiedostot**
- Kaikissa tapaustutkimustiedostoissa nyt sekventiaalinen navigointi:

**10-StreamliningAI Labit**
Lisätty "Mitä seuraavaksi" -osio Moduuli 10 yleiskuvaan ja Moduuli 11:een

#### Koodi- ja sisällön korjauksia

**SDK- ja riippuvuuspäivitykset**
Korjattu tyhjä openai-versio `^4.95.0`-muotoon
Päivitetty SDK versiosta `^1.8.0` versioon `>=1.26.0`
Päivitetty mcp-version pinnaus `>=1.26.0`

**Koodikorjaukset**
Korjattu virheellinen malli `gpt-4o-mini` muotoon `gpt-4.1-mini`

**Sisällön korjaukset**
Korjattu rikkinäinen linkki `READMEmd` → `README.md`, korjattu opetuksen otsikko `Module 1-3` → `Module 0-3`, korjattu kirjainkoolla eroteltu polku
Poistettu vioittunut päällekkäinen Tapaustutkimus 5:n sisältö

**Aloittelijoiden ohjeistuksen parannukset**
Lisätty asianmukainen johdanto, oppimistavoitteet ja esivaatimukset aloittelijoille

#### Oppimateriaalin päivitykset

**Pää-README.md**
- Lisätty kohdat 3.12 (MCP-hostit), 3.13 (MCP Inspector), 4.1 (Sivutus), 5.16 (Protokollaominaisuudet) opetustaulukkoon

**Moduulien README:t**
Lisätty oppitunnit 12 ja 13 oppituntilistaan
Lisätty Käytännön oppaat -osio sivutuslinkillä
Lisätty oppitunnit 5.15 (Mukautettu kuljetus) ja 5.16 (Protokollaominaisuudet)

**study_guide.md**
- Päivitetty mielenkartta kaikilla uusilla aiheilla: MCP-hostien määritys, MCP Inspector, Sivutusstrategiat, Protokollaominaisuuksien perusteellinen katsaus

## 28. tammikuuta 2026

### MCP-specifikaation 25.11.2025 vaatimustenmukaisuuden tarkastus

#### Peruskäsitteiden parannukset (01-CoreConcepts/)
- **Uusi client-primitiivi - Roots**: Lisätty kattava dokumentaatio Roots-asiakasprimitiivistä, joka auttaa palvelimia ymmärtämään tiedostojärjestelmän rajat ja käyttöoikeudet
- **Työkalujen annotaatiot**: Lisätty dokumentaatio työkalujen käyttäytymisen annotaatioista (`readOnlyHint`, `destructiveHint`) parempien työkalusuorituspäätösten tekemiseksi
- **Työkalujen kutsuminen näytteenotossa**: Päivitetty Näytteenoton dokumentaatio sisältämään `tools` ja `toolChoice` -parametrit mallin ohjattuun työkalukutsuun näytteenoton aikana
- **URL-tilan herättäminen**: Lisätty dokumentaatio URL-pohjaisesta herättämisestä palvelimen käynnistämille ulkoisille web-interaktioille
- **Tehtävät (kokeellinen)**: Lisätty uusi osio kuvaamaan kokeellista Tehtävät-ominaisuutta kestävän suorituksen kääreille ja viivästyneelle tuloksen hakemiselle

- **Kuvakkeiden tuki**: Työkalut, resurssit, resurssipohjat ja kehotteet voivat nyt sisältää kuvakkeita lisämetatietona

#### Dokumentaatiopäivitykset
- **README.md**: Lisätty MCP Specification 2025-11-25 version viittaus ja versionhallinnan selitys päivämäärän perusteella
- **study_guide.md**: Päivitetty opetussuunnitelmakartta sisällyttämään tehtävät ja työkalumuistiinpanot ydinajatusosioon; päivitetty asiakirjan aikaleima

#### Määrityksen vaatimustenmukaisuuden varmistus
- **Protokollaversio**: Varmistettu, että kaikki dokumentaatioviittaukset ovat nykyiseen MCP Specification 2025-11-25 mukaisia
- **Arkkitehtuurin yhteensopivuus**: Varmistettu kahden tason arkkitehtuurin (Tietokerros + Kuljetuskerros) dokumentaation tarkkuus
- **Primitivien dokumentaatio**: Tarkistettu palvelimen primitiivejä (Resurssit, Kehotteet, Työkalut) ja asiakkaan primitiivejä (Näytteenotto, Pyytely, Lokitus, Juuret)
- **Kuljetusmekanismit**: Varmistettu STDIO- ja suoratoistettavan HTTP-kuljetuksen dokumentaation tarkkuus
- **Turvaohjeistus**: Vahvistettu yhteensopivuus nykyisen MCP Security Best Practices -dokumentaation kanssa

#### Keskeiset MCP 2025-11-25 ominaisuudet dokumentoitu
- **OpenID Connect Discovery**: Todennuspalvelimen löytäminen OIDC:n kautta
- **OAuth-asiakas-ID-metadokumentit**: Suositeltu asiakasrekisteröintimekanismi
- **JSON Schema 2020-12**: Oletusdialliekieli MCP skeemamäärittelyille
- **SDK-tasoittelujärjestelmä**: Formalisoitu vaatimukset SDK-ominaisuuksien tuelle ja ylläpidolle
- **Hallinnon rakenne**: Formalisoidut työryhmät ja intressiryhmät MCP hallinnossa

### Turvadokumentaation merkittävä päivitys (02-Security/)

#### MCP Security Summit Workshop (Sherpa) integraatio
- **Uusi käytännön koulutusmateriaali**: Lisätty kattava integraatio [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) -materiaalin kautta kaikkeen turvadokumentaatioon
- **Retkireitin kattavuus**: Dokumentoitu kokonainen leiriltä leirille etenemismatka Base Campista Summitille
- **OWASP-yhteensopivuus**: Kaikki turvaohjeistukset vastaavat nyt OWASP MCP Azure Security Guide riskejä

#### OWASP MCP Top 10 integrointi
- **Uusi osio**: Lisätty OWASP MCP Top 10 -turvariskit taulukko Azure-mitigointien kanssa turvan pää-READMEen
- **Riskiin perustuva dokumentaatio**: Päivitetty mcp-security-controls-2025.md käyttämään OWASP MCP riskiviitteitä joka turvallisuusalueelle
- **Viitearkkitehtuuri**: Linkitetty OWASP MCP Azure Security Guide viitearkkitehtuuriin ja toteutuskuvioihin

#### Päivitetyt turvatiedostot
- **README.md**: Lisätty Sherpa-työpajan yleiskatsaus, retkireittitaulukko, OWASP MCP Top 10 riskikatsaus ja käytännön koulutusosio
- **mcp-security-controls-2025.md**: Päivitetty otsikko helmikuulle 2026, lisätty OWASP riskiviitteet (MCP01-MCP08), korjattu version epätarkkuus
- **mcp-security-best-practices-2025.md**: Lisätty Sherpa- ja OWASP-resurssi osio, päivitetty aikaleima
- **mcp-best-practices.md**: Lisätty käytännön koulutusosio Sherpa- ja OWASP-linkeillä
- **azure-content-safety-implementation.md**: Lisätty OWASP MCP06 -viite, Sherpa Camp 3 -yhteensopivuus ja lisäresurssit

#### Uudet resurssilinkit lisätty
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Yksittäiset OWASP MCP riskisivut (MCP01-MCP10)

### Kokonaisvaltainen opetussuunnitelman MCP Specification 2025-11-25 mukautus

#### Moduuli 03 - Aloittaminen
- **SDK-dokumentaatio**: Lisätty Go SDK viralliselle SDK-listalle; päivitetty kaikki SDK-viitteet vastaamaan MCP Specification 2025-11-25 -versiota
- **Kuljetuksen täsmennys**: Päivitetty STDIO- ja HTTP-suoratoistokuljetusten kuvauksia selkein spesifikaatioviittauksin

#### Moduuli 04 - Käytännön toteutus
- **SDK-päivitykset**: Lisätty Go SDK; päivitetty SDK-lista spesifikaatioversion viittauksella
- **Valtuutusmäärittely**: Päivitetty MCP Authorization -määrittelyn linkki nykyiseen 2025-11-25 versioon

#### Moduuli 05 - Edistyneet aiheet
- **Uudet ominaisuudet**: Lisätty maininta uusista MCP Specification 2025-11-25 ominaisuuksista (Tehtävät, Työkalumuistiinpanot, URL-tilan pyytely, Juuret)
- **Turvaresurssit**: Lisätty OWASP MCP Top 10 ja Sherpa-työpajan linkit lisäviitteisiin

#### Moduuli 06 - Yhteisön panokset
- **SDK-lista**: Lisätty Swift- ja Rust-SDK:t; päivitetty spesifikaatiolinkki 2025-11-25 -versioon
- **Spesifikaatioviite**: Päivitetty MCP Specification linkki suoraan spesifikaation URL-osoitteeseen

#### Moduuli 07 - Varhaisen käyttöönoton opit
- **Resurssipäivitykset**: Lisätty MCP Specification 2025-11-25 -linkki ja OWASP MCP Top 10 lisäresursseihin

#### Moduuli 08 - Parhaat käytännöt
- **Spesifikaatioversion päivitys**: Päivitetty MCP Specification viite versioon 2025-11-25
- **Turvaresurssit**: Lisätty OWASP MCP Top 10 ja Sherpa-työpajan linkit lisäviitteisiin

#### Moduuli 10 - Tehostettu tekoälytyönkulkujen hallinta
- **Merkkipäivitys**: Vaihdettu MCP-version merkki SDK-version (1.9.3) sijaan spesifikaatioversion (2025-11-25) käyttämiseksi
- **Resurssilinkit**: Päivitetty MCP Specification -linkki; lisätty OWASP MCP Top 10

#### Moduuli 11 - MCP-palvelimen käytännön labrat
- **Spesifikaatioviite**: Päivitetty MCP Specification -linkki versioon 2025-11-25
- **Turvaresurssit**: Lisätty OWASP MCP Top 10 virallisiin resursseihin

## 18. joulukuuta 2025

### Turvadokumentaation päivitys - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Määritysversion päivitys
- **Protokollaversion päivitys**: Päivitetty viittaus uusimpaan MCP Specification 2025-11-25 (julkaistu 25. marraskuuta 2025)
  - Päivitetty kaikki spesifikaatioversion viittaukset 2025-06-18:sta 2025-11-25:een
  - Päivitetty asiakirjan päivämääräviittaukset 18. elokuuta 2025:stä 18. joulukuuta 2025:een
  - Varmistettu että kaikki spesifikaatio-URL:t osoittavat nykyiseen dokumentaatioon
- **Sisällön validointi**: Kattava validointi turvallisuusparhaiden käytäntöjen osalta uusimpien standardien pohjalta
  - **Microsoftin turvallisuusratkaisut**: Tarkistettu nykyiset termit ja linkit Prompt Shieldsille (aiemmin "Jailbreak risk detection"), Azure Content Safetylle, Microsoft Entra ID:lle ja Azure Key Vaultille
  - **OAuth 2.1 -turvallisuus**: Varmistettu yhteensopivuus uusimpien OAuth-turvallisuusparhaiden käytäntöjen kanssa
  - **OWASP-standardit**: Validointi, että OWASP Top 10 LLM:ille -viitteet ovat ajan tasalla
  - **Azure-palvelut**: Tarkistettu kaikki Microsoft Azure -dokumentaatiolinkit ja parhaat käytännöt
- **Standardien täsmäytys**: Kaikki viitatut turvallisuusstandardit vahvistettu ajantasaisiksi
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure turvallisuus- ja vaatimustenmukaisuuskehykset
- **Toteutusresurssit**: Tarkistettu kaikki toteutusoppaiden linkit ja resurssit
  - Azure API Managementin autentikointikuvioita
  - Microsoft Entra ID:n integraatio-oppaat
  - Azure Key Vaultin salaisuuksien hallinta
  - DevSecOps-putket ja valvontaratkaisut

### Dokumentaation laadunvarmistus
- **Määrityksen noudattaminen**: Varmistettu, että kaikki pakolliset MCP-turvavaatimukset (MUST/MUST NOT) ovat yhdenmukaisia uusimman spesifikaation kanssa
- **Resurssien ajantasaisuus**: Tarkistettu kaikki ulkoiset linkit Microsoftin dokumentaatioon, turvallisuusstandardeihin ja toteutusoppaisiin
- **Parhaiden käytäntöjen kattavuus**: Varmistettu kattava käsittely autentikoinnista, valtuutuksesta, tekoälyyn liittyvistä uhkista, toimitusketjun turvallisuudesta ja yrityskuvioista

## 6. lokakuuta 2025

### Aloitusosion laajennus – Kehittynyt palvelimen käyttö & yksinkertainen autentikointi

#### Kehittynyt palvelimen käyttö (03-GettingStarted/10-advanced)
- **Uusi luku lisätty**: Esitelty kattava opas kehittyneestä MCP-palvelimen käytöstä, kattaen sekä tavalliset että matalan tason palvelinarkkitehtuurit.
  - **Tavallinen vs. matalan tason palvelin**: Yksityiskohtainen vertailu ja koodiesimerkit Pythonilla ja TypeScriptille molempiin malleihin.
  - **Handler-pohjainen suunnittelu**: Selitys handler-pohjaisesta työkalujen/resurssien/kehotteiden hallinnasta skaalautuville ja joustaville palvelintoteutuksille.
  - **Käytännön mallit**: Todelliset skenaariot, joissa matalan tason palvelinmallit tukevat edistyneitä ominaisuuksia ja arkkitehtuuria.

#### Yksinkertainen autentikointi (03-GettingStarted/11-simple-auth)
- **Uusi luku lisätty**: Vaiheittainen opas yksinkertaisen autentikoinnin toteuttamiseen MCP-palvelimissa.
  - **Tunnistus- ja valtuutuskonseptit**: Selkeä selitys autentikoinnin vs. valtuutuksen eroista ja tunnistetietojen käsittelystä.
  - **Perusautentikoinnin toteutus**: Middleware-pohjaiset autentikointimallit Pythonilla (Starlette) ja TypeScriptillä (Express), koodiesimerkit mukana.
  - **Eteneminen kehittyneeseen turvallisuuteen**: Ohjeet aloittaa yksinkertaisella autentikoinnilla ja edetä OAuth 2.1:een ja RBAC:iin, viitteet kehittyneisiin turvamoduuleihin.

Nämä lisäykset tarjoavat käytännönläheistä ohjausta tukevampien, turvallisempien ja joustavampien MCP-palvelintoteutusten rakentamiseen, yhdistäen perustavanlaatuiset käsitteet edistyneisiin tuotantokuvioihin.

## 29. syyskuuta 2025

### MCP-palvelimen tietokantaintegraation labrat – Kattava käytännön oppimispolku

#### 11-MCPServerHandsOnLabs – Uusi täysi tietokantaintegraatio-opetussuunnitelma
- **Täysi 13-labran oppimispolku**: Lisätty kattava käytännön opetussuunnitelma tuotantovalmiiden MCP-palvelimien rakentamiseen PostgreSQL-tietokantaintegraatiolla
  - **Todellisen maailman toteutus**: Zava Retail -analytiikkaesimerkki, joka demonstroi yritystason kuvioita
  - **Jäsennelty oppimisjärjestys**:
    - **Labrat 00-03: Perusteet** - Johdanto, ydinar­kitehtuuri, turvallisuus & monivuokraus, ympäristön asennus
    - **Labrat 04-06: MCP-palvelimen rakentaminen** - Tietokantasunnittelu & skeema, MCP-palvelimen toteutus, työkalun kehitys  
    - **Labrat 07-09: Edistyneet ominaisuudet** - Semanttinen haku-integraatio, testaus & virheenkorjaus, VS Code -integraatio
    - **Labrat 10-12: Tuotanto & parhaat käytännöt** - Julkaisustrategiat, valvonta & havaittavuus, parhaat käytännöt & optimointi
  - **Yritysteknologiat**: FastMCP-kehys, PostgreSQL pgvectorillä, Azure OpenAI upotukset, Azure Container Apps, Application Insights
  - **Edistyneet ominaisuudet**: Rivitason suojaus (RLS), semanttinen haku, monivuokraajien tiedon käyttö, vektoriesitykset, reaaliaikainen valvonta

#### Terminologian yhdenmukaistus – moduulista labraksi
- **Kattava dokumentaatiopäivitys**: Päivitetty järjestelmällisesti kaikki README-tiedostot 11-MCPServerHandsOnLabs -kansiossa käyttämään "Lab" terminologiaa "Module" sijaan
  - **Otsikot**: Päivitetty "What This Module Covers" muotoon "What This Lab Covers" kaikissa 13 labrassa 
  - **Sisällön kuvaus**: Muutettu "This module provides..." muotoon "This lab provides..." dokumentaatiossa
  - **Oppimistavoitteet**: Päivitetty "By the end of this module..." muotoon "By the end of this lab..." 
  - **Navigointilinkit**: Muutettu kaikki "Module XX:" viittaukset "Lab XX:" muotoon kaikissa ristiinviittauksissa ja navigaatiossa
  - **Suorituksen seuranta**: Muutettu "After completing this module..." muotoon "After completing this lab..."
  - **Tekniset viittaukset säilytetty**: Python-moduuliviittaukset säilytetty konfiguraatiotiedostoissa (esim. `"module": "mcp_server.main"`)

#### Opasparannus (study_guide.md)
- **Visuaalinen opetussuunnitelmakartta**: Lisätty uusi "11. Database Integration Labs" osio kattavalla labrakas rakenteen visualisoinnilla
- **Repositorion rakenne**: Päivitetty kymmenestä yhdelletoista pääosiolle, lisäten tarkan 11-MCPServerHandsOnLabs kuvauksen
- **Oppimispolun ohjeistus**: Parannettu navigointiohjeita kattamaan osiot 00-11
- **Teknologian kattavuus**: Lisätty FastMCP, PostgreSQL, Azure-palveluiden integraatiotiedot
- **Oppimistulokset**: Korostettu tuotantovalmiin palvelinkehityksen, tietokantaintegraatiokuvioiden ja yrityksen turvallisuuden merkitystä

#### Pää-README rakenteen parannus
- **Labrakeskeinen terminologia**: Päivitetty pää-README.md 11-MCPServerHandsOnLabs kansiossa käyttämään johdonmukaisesti "Lab" rakennetta
- **Oppimispolun järjestys**: Selkeä eteneminen perusteista edistyneeseen toteutukseen ja tuotantoon julkaisussa
- **Todellisen maailman painotus**: Korostettu käytännönläheistä, labripohjaista oppimista yritystason kuvioin ja teknologioin

### Dokumentaation laadun ja johdonmukaisuuden parantaminen
- **Käytännönläheinen oppiminen**: Vahvistettu käytännön labripohjaista lähestymistä dokumentaation kaikissa osissa
- **Yrityskuvioiden painottaminen**: Korostettu tuotantovalmiita toteutuksia ja yritysturvallisuutta
- **Teknologian integrointi**: Kattava Azure-palveluiden ja tekoälyintegraatiokuvioiden käsittely
- **Oppimisen eteneminen**: Selkeä, jäsennelty polku peruskäsitteistä tuotannon julkaisuun

## 26. syyskuuta 2025

### Tapaustutkimusten parannus – GitHub MCP Registry integraatio

#### Tapaustutkimukset (09-CaseStudy/) – Ekosysteemin kehityksen painotus
- **README.md**: Merkittävä laajennus kattavalla GitHub MCP Registry tapaustutkimuksella
  - **GitHub MCP Registry tapaustutkimus**: Uusi kattava tapaustutkimus GitHubin MCP Registry -lanseerauksesta syyskuussa 2025
    - **Ongelman analyysi**: Yksityiskohtainen tarkastelu sirpaloituneista MCP-palvelimen löytämisen ja käyttöönoton haasteista
    - **Ratkaisun arkkitehtuuri**: GitHubin keskitetty rekisteriratkaisu yhden klikkauksen VS Code -asennuksella
    - **Liiketoiminnan vaikutus**: Mitattavat parannukset kehittäjien käyttöönotossa ja tuottavuudessa
    - **Strateginen arvo**: Painotus modulaariseen agentin käyttöönottoon ja työkalujen välisten yhteentoimivuuteen
    - **Ekosysteemin kehitys**: Asemointi perustavanlaatuiseksi alustaksi agenttipohjaiselle integraatiolle
  - **Parannettu tapaustutkimusrakenne**: Päivitetty kaikki seitsemän tapaustutkimusta yhdenmukaisella muotoilulla ja kattavilla kuvauksilla
    - Azure AI Travel Agents: Moni-agenttien orkestrointiin keskittyminen
    - Azure DevOps Integration: Työnkulkujen automaation painotus
    - Reaaliaikainen dokumentaation haku: Python-konsoliasiakas toteutus
    - Interaktiivinen opintosuunnitelman generaattori: Chainlit-keskustelupohjainen web-sovellus

    - Editorin Sisällä Dokumentaatio: VS Code ja GitHub Copilot -integraatio
    - Azure API Management: Yritystason API-integraatiomallit
    - GitHub MCP Rekisteri: Ekosysteemin kehitys ja yhteisöalusta
  - **Kattava Yhteenveto**: Uudelleenkirjoitettu yhteenvetoluku, jossa korostetaan seitsemää tapaustutkimusta, jotka kattavat useita MCP:n toteutusulottuvuuksia
    - Yritysintegrointi, monitoimijaorchestrointi, kehittäjän tuottavuus
    - Ekosysteemin kehitys, koulutussovellusten luokittelu
    - Parannetut näkemykset arkkitehtuurimalleista, toteutusstrategioista ja hyvistä käytännöistä
    - Painotus MCP:hen kypsänä, tuotantovalmiina protokollana

#### Opas Päivitykset (study_guide.md)
- **Visuaalinen Opintosuunnitelmakartta**: Päivitetty miellekartta sisältämään GitHub MCP Rekisterin tapaustutkimukset-osioon
- **Tapaustutkimusten Kuvaus**: Täydennetty geneerisistä kuvauksista seitsemän kattavan tapaustutkimuksen yksityiskohtaiseen erittelyyn
- **Rekisterirakenne**: Päivitetty luku 10 kuvaamaan kattavaa tapaustutkimusten kattavuutta spesifisillä toteutustiedoilla
- **Muutosloki Integraatio**: Lisätty 26. syyskuuta 2025 merkintä, joka dokumentoi GitHub MCP Rekisterin lisäämisen ja tapaustutkimusten parannukset
- **Päivämääräpäivitykset**: Päivitetty alatunnisteen aikaleima heijastamaan viimeisintä versiota (26. syyskuuta 2025)

### Dokumentaation Laadun Parannukset
- **Yhtenäisyyden Parannus**: Yhtenäistetty tapaustutkimusten muotoilu ja rakenne kaikissa seitsemässä esimerkissä
- **Kattava Kattavuus**: Tapaustutkimukset kattavat nyt yrityksen, kehittäjän tuottavuuden ja ekosysteemin kehitys -tilanteet
- **Strateginen Sijoittelu**: Parannettu fokus MCP:hen perustavanlaatuisena alustana agenttipohjaisten järjestelmien käyttöönotolle
- **Resurssien Integraatio**: Päivitetty lisäresurssit sisältämään GitHub MCP Rekisterin linkki

## 15. syyskuuta 2025

### Edistyneet Aiheet Laajennus - Mukautetut Kuljetukset & Kontekstisuunnittelu

#### MCP Mukautetut Kuljetukset (05-AdvancedTopics/mcp-transport/) - Uusi Edistynyt Toteutusopas
- **README.md**: Täydellinen toteutusopas mukautetuille MCP-kuljetusmekanismeille
  - **Azure Event Grid Kuljetus**: Kattava palvelimeton tapahtumapohjainen kuljetustoteutus
    - C#, TypeScript ja Python esimerkit Azure Functions -integraatiolla
    - Tapahtumapohjaiset arkkitehtuurimallit skaalautuville MCP-ratkaisuille
    - Webhook-vastaanottajat ja push-pohjainen viestien käsittely
  - **Azure Event Hubs Kuljetus**: Suurivirtainen suoratoistokuljetustoteutus
    - Reaaliaikaiset suoratoistomahdollisuudet matalan viiveen tilanteissa
    - Osiointistrategiat ja tarkistuspisteiden hallinta
    - Viestien eräajo ja suorituskyvyn optimointi
  - **Yritysintegrointimallit**: Tuotantovalmiit arkkitehtuuriesimerkit
    - Hajautettu MCP-käsittely useiden Azure Functions -instanssien välillä
    - Hybridikuljetusarkkitehtuurit, jotka yhdistävät useita kuljetustyyppejä
    - Viestien pysyvyys, luotettavuus ja virheenkäsittelystrategiat
  - **Turvallisuus & Valvonta**: Azure Key Vault -integraatio ja havainnointimallit
    - Hallinnoitu identiteettitodennus ja vähimmän oikeuden pääsy
    - Application Insights -telemetria ja suorituskyvyn valvonta
    - Sulku- ja vikasietoisuusmallit
  - **Testauskehykset**: Kattavat testausstrategiat mukautetuille kuljetuksille
    - Yksikkötestaus testiparien ja mokkauskehysten avulla
    - Integraatiotestaus Azure Test Containers -ympäristössä
    - Suorituskyky- ja kuormitustestauksen näkökulmat

#### Kontekstisuunnittelu (05-AdvancedTopics/mcp-contextengineering/) - Nouseva AI-ala
- **README.md**: Kattava tutkimus kontekstisuunnittelusta nousevana alanaan
  - **Perusperiaatteet**: Täydellinen kontekstin jakaminen, toimintapäätösten tietoisuus ja kontekstin ikkunan hallinta
  - **MCP-protokollan Yhteensopivuus**: Miten MCP-suunnittelu käsittelee kontekstisuunnittelun haasteet
    - Kontekstin ikkunan rajoitukset ja asteittaisen latauksen strategiat
    - Merkityksellisyyden määrittäminen ja dynaaminen kontekstin nouto
    - Monimuotoinen kontekstin käsittely ja turvallisuuskysymykset
  - **Toteutusmenetelmät**: Yksisäikeiset vs. monitoimija-arkkitehtuurit
    - Kontekstin paloittelu ja priorisointitekniikat
    - Asteittainen kontekstin lataus ja pakkausstrategiat
    - Kerrostetut kontekstimenetelmät ja hakemisen optimointi
  - **Mittauskehys**: Nousevat mittarit kontekstitehokkuuden arviointiin
    - Syötteen tehokkuus, suorituskyky, laatu ja käyttäjäkokemusnäkökulmat
    - Kokeelliset lähestymistavat kontekstin optimointiin
    - Virheanalyysi ja parannusmenetelmät

#### Opintosuunnitelman Navigointipäivitykset (README.md)
- **Parannettu moduulirakenne**: Päivitetty opintosuunnitelmakaavio sisältämään uudet edistyneet aiheet
  - Lisätty Kontekstisuunnittelu (5.14) ja Mukautettu Kuljetus (5.15) merkinnät
  - Johdonmukainen muotoilu ja navigointilinkit kaikissa moduuleissa
  - Päivitetyt kuvaukset vastaamaan nykyisen sisällön laajuutta

### Hakemistorakenteen Parannukset
- **Nimeämisen Yhtenäistäminen**: Uudelleennimetty "mcp transport" muotoon "mcp-transport" yhtenäisyyden takaamiseksi muiden edistyneiden aiheiden kansioiden kanssa
- **Sisällön Järjestely**: Kaikki 05-AdvancedTopics-kansiot noudattavat nyt yhdenmukaista nimeämiskäytäntöä (mcp-[aihe])

### Dokumentaation Laadun Parannukset
- **MCP-spesifikaatioiden Yhteensopivuus**: Kaikki uudet sisällöt viittaavat nykyiseen MCP-spesifikaatioon 2025-06-18
- **Monikieliset Esimerkit**: Kattavat koodiesimerkit C#:ssa, TypeScriptissä ja Pythonissa
- **Yrityslähtöisyys**: Tuotantovalmiit mallit ja Azure-pilviyhteydet läpi koko dokumentaation
- **Visuaalinen Dokumentaatio**: Mermaid-kaaviot arkkitehtuurin ja prosessivirtojen visualisointiin

## 18. elokuuta 2025

### Dokumentaation Kattava Päivitys - MCP 2025-06-18 Standardit

#### MCP:n Turvallisuuden Parhaat Käytännöt (02-Security/) - Täysi Modernisointi
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täysin uudelleenkirjoitettu ja MCP-spesifikaatio 2025-06-18 mukainen
  - **Pakolliset Vaatimukset**: Lisätty selkeät PAKKO/ei saa -vaatimukset virallisesta spesifikaatiosta visuaalisesti selkein merkinnöin
  - **12 Keskeistä Turvakäytäntöä**: Muokattu 15-kohdan listasta kattaviksi turvallisuusalueiksi
    - Token-turva ja todennus ulkoisen identiteettipalvelun integroinnilla
    - Istunnon hallinta ja kuljetusturvallisuus kryptografisilla vaatimuksilla
    - AI-kohtainen uhkasuojaus Microsoft Prompt Shields -integraatiolla
    - Käyttöoikeuksien hallinta ja vähimmän oikeuden periaate
    - Sisällön turvallisuus ja valvonta Azure Content Safetyn avulla
    - Toimitusketjun turvallisuus kattavalla komponenttien tarkistuksella
    - OAuth-turva ja Confused Deputy -estot PKCE-toteutuksella
    - Vikatilanteisiin reagointi ja toipuminen automatisoiduilla keinoilla
    - Säädösten noudattaminen ja hallinnointi
    - Edistyneet turvakontrollit nollaluottamusarkkitehtuurilla
    - Microsoftin turvaekosysteemin integrointi kattavien ratkaisujen avulla
    - Jatkuva turvallisuuden kehitys mukautuvien käytäntöjen myötä
  - **Microsoftin Turvaratkaisut**: Parannettu ohjeistus Prompt Shieldsin, Azure Content Safetyn, Entra ID:n ja GitHub Advanced Securityn integroinnista
  - **Toteutusresurssit**: Kattavat resurssilinkit luokiteltuina virallisesta MCP-dokumentaatiosta, Microsoftin turvaratkaisuista, turvallisuusstandardeista ja toteutusoppaista

#### Edistyneet Turvakontrollit (02-Security/) - Yritysasteen Toteutus
- **MCP-SECURITY-CONTROLS-2025.md**: Täysi uudistus yritystason turvallisuuskehyksen mukaiseksi
  - **9 Kattavaa Turva-aluetta**: Laajennettu peruskontrolleista yksityiskohtaisiksi yritysratkaisuiksi
    - Kehittynyt todennus ja valtuutus Microsoft Entra ID -integraatiolla
    - Token-turva ja läpivienninvastaiset kontrollit kattavalla validoinnilla
    - Istunnon turvallisuus kontrollit sieppauksen estämiseen
    - AI-kohtaiset turvallisuuskontrollit kehotteiden injektiota ja työkalumyrkytyksiä vastaan
    - Confused Deputy -hyökkäysten esto OAuth-proxyn turvatoiminnoilla
    - Työkalujen suoritusturva hiekkalaatikkoratkaisuilla ja eristyksellä
    - Toimitusketjun turvallisuuskontrollit riippuvuuksien tarkistuksella
    - Valvonta ja havaitsemiskontrollit SIEM-integraatiolla
    - Vikatilanteisiin reagointi ja toipuminen automatisoiduilla prosesseilla
  - **Toteutusesimerkit**: Lisätty yksityiskohtaiset YAML-konfiguraatiolohkot ja koodiesimerkit
  - **Microsoftin Ratkaisujen Integrointi**: Kattava Azure-turvapalveluiden, GitHub Advanced Securityn ja yritysten identiteetinhallinnan tuki

#### Edistyneen Tason Turvallisuus (05-AdvancedTopics/mcp-security/) - Tuotantovalmiit Toteutukset
- **README.md**: Täysin uudelleenkirjoitettu yritysturvallisuuden toteutukseen
  - **Nykyinen Spesifikaatio**: Päivitetty MCP-spesifikaatio 2025-06-18 mukaisesti pakollisten turvallisuusvaatimusten osalta
  - **Parannettu Todennus**: Microsoft Entra ID -integraatio laajoine .NET ja Java Spring Security -esimerkkien kera
  - **AI-turva Integraatio**: Microsoft Prompt Shields ja Azure Content Safety toteutukset yksityiskohtaisilla Python-esimerkeillä
  - **Edistynyt Uhka- ehkäisy**: Kattavat toteutusesimerkit
    - Confused Deputy -hyökkäysten esto PKCE:llä ja käyttäjän suostumuksen validoinnilla
    - Token-läpiviennin estäminen kohdevalidoinnilla ja turvallisella token-hallinnalla
    - Istunnon kaappauksen esto kryptografisella sidonnalla ja käyttäytymisanalyysillä
  - **Yritysturvallisuuden Integrointi**: Azure Application Insights -valvonta, uhkien havaitsemisputket ja toimitusketjun turvallisuus
  - **Toteutuksen Tarkistustaulukko**: Selkeä pakollisten ja suositeltujen turvakontrollien erittely Microsoftin turvallisuus-ekosysteemietujen kera

### Dokumentaation Laatu & Standardien Yhteensopivuus
- **Spesifikaatioviitteet**: Päivitetty kaikki viitteet nykyiseen MCP-spesifikaatioon 2025-06-18
- **Microsoftin Turvaekosysteemi**: Parannettu integraatio-ohjeistus kaikkiin turvallisuusdokumentteihin
- **Käytännön Toteutus**: Lisätty yksityiskohtaiset koodiesimerkit .NETissä, Javassa ja Pythonissa yritysmallien kanssa
- **Resurssien Järjestely**: Kattava virallisen dokumentaation, turvallisuusstandardien ja toteutusoppaiden luokittelu
- **Visuaaliset Merkinnät**: Selkeä pakollisten vaatimusten ja suositeltujen käytäntöjen merkintä


#### Keskeiset Käsitteet (01-CoreConcepts/) - Täysi Modernisointi
- **Protokollaversion Päivitys**: Päivitetty viittaamaan nykyiseen MCP-spesifikaatioon 2025-06-18 päivämääräpohjaisella versiointityylillä (VVVV-KK-PP)
- **Arkkitehtuurin Tarkennus**: Parannetut kuvaukset Hosteista, Asiakkaista ja Palvelimista, jotta ne vastaavat MCP:n nykyisiä arkkitehtuurimalleja
  - Hostit nyt selkeästi määritelty AI-sovelluksina, jotka koordinoivat useita MCP-asiakasliitäntöjä
  - Asiakkaat kuvattu protokollaliittiminä, jotka ylläpitävät yhden suhteen yhteen palvelimen kanssa
  - Palvelimia parannettu paikallisen ja etäkäytön skenaarioilla
- **Primitiivien Rakenteen Uudistus**: Täysi uudistus palvelin- ja asiakasprimitiiveissä
  - Palvelinprimitiivit: Resurssit (datallähteet), Kehotteet (mallipohjat), Työkalut (suoritettavat funktiot) yksityiskohtineen ja esimerkein
  - Asiakasprimitiivit: Näytteenotto (LLM-suoritukset), Tiedonkeruu (käyttäjäsyöte), Lokitus (debuggaus/monitorointi)
  - Päivitetty nykyisiin löytö (`*/lista`), haku (`*/hanki`) ja suoritustapoihin (`*/kutsu`) malleihin
- **Protokollan Arkkitehtuuri**: Esitelty kaksikerroksinen arkkitehtuurimalli
  - Datan kerros: JSON-RPC 2.0 -pohja, elinkaaren hallinta ja primitiivit
  - Kuljetuskerros: STDIO (paikallinen) ja Streamable HTTP with SSE (etä) kuljetusmekanismit
- **Turvakehys**: Kattavat turvallisuusperiaatteet mukaan lukien eksplisiittinen käyttäjän suostumus, tietosuoja, työkalujen suoritusturva ja kuljetuskerroksen turvallisuus
- **Viestintämallit**: Päivitetyt protokollaviestit näyttävät alustuksen, löytymisen, suorituksen ja ilmoitusvirrat
- **Koodiesimerkit**: Päivitetyt monikieliset esimerkit (.NET, Java, Python, JavaScript) nykyisten MCP SDK -mallien mukaisiksi

#### Turvallisuus (02-Security/) - Kattava Turvallisuuden Uudistus  
- **Standardien Yhteensopivuus**: Täysi yhteensopivuus MCP-spesifikaation 2025-06-18 turvallisuusvaatimusten kanssa
- **Todennuksen Kehitys**: Dokumentoitu kehitys räätälöidyistä OAuth-palvelimista ulkoisiin identiteettipalvelun valtuutuksiin (Microsoft Entra ID)
- **AI-kohtainen Uhkanalyysi**: Parannettu nykyaikaisten AI-hyökkäysvektorien käsittely
  - Yksityiskohtaiset kehotteiden injektiohyökkäys-skenaariot todellisten esimerkkien kera
  - Työkalujen myrkytysmekanismit ja "rug pull" -hyökkäysmallit
  - Kontekstin ikkunan myrkytys ja mallin sekaannushyökkäykset
- **Microsoftin AI-Turvaratkaisut**: Kattava Microsoftin turvallisuus-ekosysteemin kuvaus
  - AI Prompt Shields kehittyneellä havaitsemisella, esille tuomisella ja erotinmenetelmillä
  - Azure Content Safetyn integrointimallit
  - GitHub Advanced Security toimitusketjun suojaamiseen
- **Edistynyt Uhkan Ehkäisy**: Yksityiskohtaiset turvakontrollit
  - Istunnon sieppaus MCP-spesifisillä hyökkäysskenaarioilla ja kryptografisilla istuntotunnusvaatimuksilla
  - Confused deputy -ongelmat MCP proxy -skenaarioissa eksplisiittisillä suostumusvaatimuksilla
  - Token-läpiviennin haavoittuvuudet pakollisilla validointikontrolleilla
- **Toimitusketjun Turvallisuus**: Laajennettu AI-toimitusketjun kattavuus perustavaan malliin, upotuksiin, kontekstin tarjoajiin ja kolmannen osapuolen API:hin
- **Perusturvallisuus**: Parannettu integraatio yritysturvallisuusmalleihin, mukaan lukien nollaluottamusarkkitehtuuri ja Microsoftin turvallisuus-ekosysteemi
- **Resurssien Järjestely**: Kattavat resurssilinkit luokiteltuina tyypin mukaan (viralliset dokumentit, standardit, tutkimus, Microsoft-ratkaisut, toteutusoppaat)

### Dokumentaation Laadun Parannukset
- **Rakenteelliset Oppimistavoitteet**: Parannetut oppimistavoitteet, joissa spesifisiä ja toteutettavia tuloksia
- **Ristiinviittaukset**: Lisätty linkkejä liittyvien turvallisuus- ja ydinkäsitteiden aiheiden välillä
- **Ajantasaiset Tiedot**: Päivitetty kaikki päivämääräviitteet ja spesifikaatiolinkit nykyisiin standardeihin
- **Toteutusohjeet**: Lisätty konkreettisia ja toteuttamiskelpoisia ohjeita molempiin osioihin

## 16. heinäkuuta 2025

### README ja Navigointiparannukset
- Täysin uudistettu opintosuunnitelman navigointi README.md:ssä
- Vaihdettu `<details>`-tagit saavutettavampaan taulukkomuotoon
- Luotu vaihtoehtoisia asetteluvaihtoehtoja uuteen "alternative_layouts" -kansioon
- Lisätty korttityyliset, välilehtityyliset ja harmonikkatyyliset navigointiesimerkit
- Päivitetty rekisterirakenne -osio sisältämään kaikki viimeisimmät tiedostot
- Parannettu "Kuinka Käyttää Tätä Opintosuunnitelmaa" -osio selkeillä suosituksilla
- Päivitetty MCP-spesifikaatiolinkit osoittamaan oikeisiin URL-osoitteisiin
- Lisätty Kontekstisuunnittelu -osio (5.14) opintosuunnitelmarakenteeseen

### Opas Päivitykset
- Täysin uudistettu opas vastaamaan nykyistä rekisterirakennetta
- Lisätty uusia osioita MCP-asiakkaille ja työkaluista sekä suosituista MCP-palvelimista
- Päivitetty visuaalinen opintosuunnitelmakartta kuvastamaan kaikkia aiheita tarkasti
- Parannettu edistyneiden aiheiden kuvauksia kattamaan kaikki erikoistuneet alueet
- Päivitetty tapaustutkimukset-osio vastaamaan todellisia esimerkkejä
- Lisätty tämä kattava muutosloki

### Yhteisön Panokset (06-CommunityContributions/)
- Lisätty yksityiskohtainen tieto MCP-palvelimista kuvan generointiin
- Lisätty kattava osio Clauden käytöstä VSCode:ssa
- Lisätty Cline terminaaliasiakkaan asennus- ja käyttöohjeet
- Päivitetty MCP-asiakasosio sisältämään kaikki suosituimmat asiakasvaihtoehdot
- Parannettu panosesimerkkejä tarkemmilla koodinäytteillä

### Edistyneet Aiheet (05-AdvancedTopics/)
- Järjestetty kaikki erikoistuneet aiheiden kansiot yhdenmukaisin nimikkein
- Lisätty kontekstisuunnittelumateriaaleja ja esimerkkejä
- Lisätty Foundry-agentin integraatiodokumentaatio
- Parannettu Entra ID -turvallisuusintegraatiodokumentaatiota

## 11. kesäkuuta 2025

### Alkuperäinen Luonti
- Julkaistu ensimmäinen versio MCP for Beginners -opintosuunnitelmasta

- Luotu perusrakenne kymmenelle pääosalle
- Toteutettu visuaalinen opetussuunnitelmakartta navigointia varten
- Lisätty alkuperäisiä esimerkkiprojekteja useilla ohjelmointikielillä

### Aloittaminen (03-GettingStarted/)
- Luotu ensimmäiset palvelinimplmentointiesimerkit
- Lisätty opastusta asiakasohjelmistokehitykseen
- Sisällytetty LLM-asiakasintegrointiohjeet
- Lisätty VS Code -integrointidokumentaatio
- Toteutettu Server-Sent Events (SSE) -palvelinesimerkit

### Peruskäsitteet (01-CoreConcepts/)
- Lisätty yksityiskohtainen selitys asiakas-palvelinarkkitehtuurista
- Luotu dokumentaatio keskeisistä protokollakomponenteista
- Dokumentoitu MCP:n viestintäkuviot

## 23. toukokuuta 2025

### Repositorion rakenne
- Alustettu repositorio peruskansiorakenteella
- Luotu README-tiedostot jokaiselle pääosiolle
- Määritelty käännösinfrastruktuuri
- Lisätty kuva-aineistot ja kaaviot

### Dokumentaatio
- Luotu alkuperäinen README.md opetussuunnitelman yleiskatsauksella
- Lisätty CODE_OF_CONDUCT.md ja SECURITY.md
- Määritelty SUPPORT.md ohjeineen avun saamiseksi
- Luotu alustava opiskeluopasrakenne

## 15. huhtikuuta 2025

### Suunnittelu ja kehys
- Ensimmäinen suunnittelu MCP for Beginners -opetussuunnitelmalle
- Määritelty oppimistavoitteet ja kohdeyleisö
- Luotu 10-osainen rakenne opetussuunnitelmalle
- Kehitetty käsitteellinen kehys esimerkeille ja tapaustutkimuksille
- Luotu alkuperäiset prototyyppiesimerkit keskeisille käsitteille

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->