# Muutosloki: MCP for Beginners -oppimateriaali

Tämä asiakirja toimii kirjanpitona kaikista merkittävistä Model Context Protocol (MCP) for Beginners -oppimateriaalin muutoksista. Muutokset on dokumentoitu käänteisessä kronologisessa järjestyksessä (uusimmat muutokset ensin).

## 29. heinäkuuta 2026

### Uusi moduulin 08 kumppani: Luotettavuuden sivuohjelmat ja turvalliset uudelleentoyritykset

Lisättiin toimittajariippumaton kumppanitunti MCP-työkaluille, jotka luovat todellisen maailman vaikutuksia, linjassa lopullisen `2026-07-28`-määrityksen kanssa.


  hyödyntää yhtä tukipyyntötarinaa, kahta Mermaid-kaaviota ja uudelleentoyrityspäätös-
  virtausta selittääkseen vakaan toiminnan avaimet, atomisen duplikaatti-
  sisäänpääsyn, sovituksen, todisteet ja Tasks-laajennuksen rajapinnan.
- **Uusi**: Standardikirjaston Python ja SQLite -virheenkorjausharjoitus
  käyttää erillisiä toiminto- ja lippukauppoja havainnollistaakseen vastauksen katoamista
  ulkoisen vaikutuksen sitouduttua. Kuusi determinististä testiä kattavat naiivin
  duplikaation, suojatun uudelleenkäynnistyksen palautuksen, hyötykuorman ristiriidat,
  välimuistissa olevat tulokset, aktiiviset vaatimukset ja samanaikaisen duplikaatti-
  sisäänpääsyn.
- **Päivitetty**: Moduuli 08 linkittää nyt kumppanitunnin, tunnistaa
  lopullisen `2026-07-28` tilattoman pyyntömallein, erottaa OpenTelemetrin
  observabiliteetin vanhentuneesta MCP-lokitustoiminnosta ja rajoittaa
  yleisen uudelleentoyritysesimerkkinsä vain lukuoperaatioihin.
- **Valinnainen**: Oppitunti kuvaa kannettavissa olevia käsitteitään yhdelle merkatulle
  yhteisön toteutukselle ilman, että isännöity palvelu tai verkkokutsu on osa
  harjoitusta.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. heinäkuuta 2026

### Uusi oppitunti: Vuoden 2026-07-28 MCP-määrityksen julkaisuvalmis versio

Lisättiin kattavuus tulevasta `2026-07-28` MCP-määrityksen julkaisuvalmiista versiosta (julkaistu 21. toukokuuta 2026; lopullinen julkaisu aikataulutettu heinäkuun 28. päivälle 2026), tiivistettynä [virallisesta ilmoitusblogipostauksesta](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Oppimateriaalin lähtötaso pysyy **MCP Specification 2025-11-25** -versiossa uuden version julkaisuun saakka, joten tätä esitetään eteenpäin katsovana ohjeistuksena eikä olemassa olevien oppituntien uudelleenkirjoituksena.

- **Uusi**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — täydellinen oppitunti koskien tilatonta protokollan ydintä (`initialize`-kättelyn ja `Mcp-Session-Id` poistaminen), uusia `Mcp-Method`/`Mcp-Name` reititysotsikoita, `ttlMs`/`cacheScope` välimuistitietoja, W3C Trace Context `_meta`-kentässä, virallista Extensions-kehystä (MCP Apps ja uusi Tasks-laajennus), kuusi valtuutuksen tiukennukseen liittyvää SEP:ä, Roots/Sampling/Logging -ominaisuuksien vanhentumisen ja siirtymisen täydelliseen JSON Schema 2020-12 -työkalumäärityksiin.
- **Päivitetty** eteenpäin katsovilla huomioilla, jotka linkittävät uuteen oppituntiin:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokollaversion huomautus, Sampling/Roots/Logging/Tasks-osioita sekä "Mitä seuraavaksi"
  - [02-Security/README.md](./02-Security/README.md): valtuutuksen tiukennuksen huomautus
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): tilattoman siirron huomautus
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Samplingin vanhentumisen huomautus
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Lokituksen vanhentuminen ja Tasks-laajennuksen huomautus
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): tilattoman/sessio-reitityksen huomautus
  - [README.md](./README.md): "Eteenpäin katsominen" -muistio määritysosassa ja uusi `1.1` merkintä oppimateriaalin moduulitaulukossa
  - [study_guide.md](./study_guide.md): eteenpäin katsova kohta Core Concepts -yhteenvetoon ja päivätty lisäys
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): huomautus `mcp-session-id`-siirtokartasta ennen tilatonta pyyntömallia
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduuliyhteenveto Root Contexts / Sampling -vanhentumisista ja Tasks-laajennuksesta
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): valtuutuksen tiukennuksen huomautus

## 24. kesäkuuta 2026

### Uusi oppitunti: MCP:n käyttäminen Copilot-sovelluksessa

- [Työkalut-osio](./12-tooling/README.md) Lisätty työkaluosio.
- [MCP Copilot-sovelluksessa](./12-tooling/01-copilot-app/README.md)

## 16. kesäkuuta 2026

### MCP-määrityksen yhteensopivuus ja esimerkkien validointi

Varmistettiin oppimateriaalin yhteensopivuus nykyisen **MCP Specification 2025-11-25** -version ja uusimpien virallisten SDK:iden kanssa, korjattiin vanhentuneet määritysviitteet ja varmistettiin ydinesimerkkien edelleen rakentaminen ja ajaminen.

#### Määritysversion korjaukset (2025-06-18 / 2025-03-26 → 2025-11-25)

Päivitettiin englanninkielisiä sisältöjä, joissa vielä väitettiin vanhemman määrityksen olevan *voimassa/vallitseva* standardi, ja korjattiin linkit kanonisiin `modelcontextprotocol.io` -määrityspolkuun:
- **05-AdvancedTopics/mcp-security/README.md**: Päivitetty "Current Standard" -banneri, johdanto, ydinturvaperiaatteet -otsikko, pakolliset vaatimukset -otsikko, Microsoft Entra ID -osio, Viitteet & Resurssit -linkit ja päättävä tietoturvaviesti (8 viitettä) versioon 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Päivitetty Lisäresurssit-määrityksen linkki ja "Current Standard" -banneri versioon 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Korvattu vanhentunut `2025-03-26` turva- ja luottamuskäytäntöjen linkki nykyisellä 2025-11-25 parhaiden käytäntöjen sivulla
- **03-GettingStarted/14-sampling/README.md**: Päivitetty virallisen Sampling-dokumentaation linkki versioon 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Päivitetty nykyhetken "nykyinen MCP-määritys" -viittaus ja Lisäresurssit-määrityksen linkki versioon 2025-11-25 (historialliset SSE-vanhentumishuomiot säilytetty oikeellisuuden vuoksi)

#### Esimerkkien validointi nykyisiin SDK:ihin

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` asensi `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` onnistui ilman tyyppivirheitä — olemassa olevat `McpServer`/`StdioServerTransport` API:t säilyivät voimassa
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validointi eristetyssä `.venv`-ympäristössä `mcp[cli]` (1.27.2); `py_compile` onnistui ja `FastMCP.list_tools()` palautti oikein `add` ja `subtract` työkalut
- Vahvistettu, että kaikki esimerkkien `@modelcontextprotocol/sdk` versiorajat (`>=1.26.0` / `^1.26.0` / `^1.27.0`) ratkeavat siististi nykyiseen `1.29.0` versioon ilman rikkovia API-muutoksia

#### Riippuvuuksien versiotasapainotus (suljetaan versioaukot)

Päivitettiin vanhentuneet SDK-versiot sovittamaan nykyistä MCP-julkaisua, yhtenäistäen koko repositorion käytännön kanssa:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Nostettu `@modelcontextprotocol/sdk` versiosta `^1.8.0` versioon `>=1.26.0` ja päivitetty vanhentunut `"updated for MCP 2025-06-18"` paketin kuvaus muotoon `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ja **lab4/code/github_mcp_server/pyproject.toml**: Nostettiin tarkka versio `mcp==1.23.0` versioon `mcp>=1.26.0`; generoitiin molemmat `uv.lock`-tiedostot uudelleen (`uv lock`), jotta lukitustiedostot ratkeavat nykyiseen `mcp 1.27.2`:een ja pysyvät synkronissa manifestien kanssa

#### Oppimateriaalin aukkoanalyysi — Tuoreimman määrityksen ominaisuuskattavuus

Varmistettu, että oppimateriaali kattaa jo kaikki MCP 2025-11-25:ssä esitellyt tai laajennetut primitiivit, joten sisältöaukkoja ei ole:
- **Sampling**: Oppitunnit 03-GettingStarted/14-sampling sekä 05-AdvancedTopics/mcp-sampling
- **Elicitation (sis. URL-tila)**: Dokumentoitu 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumentoitu 00-Introduction, 01-CoreConcepts ja 05-AdvancedTopics/mcp-root-contexts
- **Tasks (kokeellinen, pitkään kestäviä operaatioita)**: Dokumentoitu 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Työkalujen annotaatiot** (`readOnlyHint` / `destructiveHint`): Dokumentoitu 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features

### Turvallisuuden tiukennus & riippuvuushaavoittuvuuksien korjaus

Tehtiin kattava turvallisuustarkastus jokaisessa riippuvuusmanifestissa ja esimerkkien lähdekoodissa, jonka jälkeen korjattiin kaikki havaitut npm-varoitukset ja yksi kooditason löydös. Korjausten jälkeen `npm audit` raportoikin **0 haavoittuvuutta** kaikissa tarkastetuissa hakemistoissa.

#### npm-riippuvuuksien haavoittuvuudet (transitiiviset) — Korjattu

Tarkastettiin kaikki 15 tallennettua `package-lock.json`-tiedostoa. Haavoittuvuudet rajoittuivat transitiivisiin riippuvuuksiin, jotka tulevat MCP Inspector -kehitystyökalusta, OpenAI-asiakasohjelmasta ja MCP SDK:sta; kaikki on nyt ratkaistu rikkovilta muutoksilta vapaasti:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ja **lab3/code/weather_mcp/inspector**: Nostettiin `@modelcontextprotocol/inspector` -versio (`0.16.6` / `0.14.1` → `0.22.0`), mikä poisti niputetut `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ja `ws` varoitukset. Lisättiin npm:n `overrides`-käsky pakottamaan korjattu `shell-quote@1.8.4`, joka poistaa jäljellä olevan kriittisen varoituksen `concurrently`-kirjastosta; generoitiin molemmat lukitustiedostot uudelleen (nyt 0 haavoittuvuutta)
- **03-GettingStarted/samples/typescript**: `npm audit fix` päivitti transitiivisen `qs`-kirjaston (keskivahva) korjattuun julkaisuun
- **03-GettingStarted/samples/javascript**: `npm audit fix` päivitti transitiivisen `hono`-kirjaston (keskivahva) korjattuun julkaisuun
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` päivitti transitiivisen `form-data`-kirjaston (korkea) korjattuun julkaisuun
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generoitiin puuttuva `package-lock.json`, jotta projekti on toistettavissa ja tarkastettavissa (0 haavoittuvuutta)

#### Kooditason tietoturvakorjaus (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Poistettu `shell=True` `open_in_vscode`-työkalusta. Aiempi `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` salli shellin metamerkkien tulkitsemisen kansiopolussa `cmd.exe`-ohjelmassa (komentoinjektio). Nyt se käynnistää suoraan selvitetyn `Code.exe`-ohjelman kansiopolkuargumentilla — ei shelliä — mikä on toiminnallisesti vastaava ja turvallinen.

#### Python-riippuvuuksien tarkastus

- Tarkastettu jokainen Python-vaatimuspaketti `pip-audit`-työkalulla. `05-AdvancedTopics` ja `03-GettingStarted/samples/python` raportoivat **ei tunnettua haavoittuvuutta** (niiden `mcp` / `httpx` / `pydantic` / `python-dotenv` versiot ratkeavat nykyisiin korjattuihin julkaisuihin)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` löysi transitiivisen riippuvuuden **`werkzeug` 3.1.1** jonka kolme `safe_join`-Windows-laitteenimen Denial-of-Service -varoitusta — `CVE-2025-66221`, `CVE-2026-21860` ja `CVE-2026-27199` (kaikki korjattu versiossa 3.1.6). Lisätty ilmeinen tietoturvan pinuus `werkzeug>=3.1.6`, jotta korjattu julkaisu ratkeaa; varmistettu, että tämä riippuvuus ratkeaa siististi `chainlit` / `mcp` / `semantic-kernel` pinossa

### Tuotteen nimen uudelleenbrändäys

Päivitetty kaikki oppimateriaalin sisällöt vastaamaan Microsoftin tuotemerkin uudelleenbrändäystä:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Päivitetty Discord-yhteisön linkki

- **AGENTS.md**: Päivitetty Discord-palvelinviite
- **README.md**: Päivitetyt teknologiaekosysteemiviitteet
- **study_guide.md**: Päivitetyt tapaustutkimusviitteet
- **05-AdvancedTopics/README.md**: Päivitetty moduulin 5.13 otsikko ja kuvaus
- **05-AdvancedTopics/mcp-integration/README.md**: Päivitetty osion otsikko ja kuvaus
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Kokonainen moduulin otsikko ja sisältö päivitetty
- **05-AdvancedTopics/mcp-security-entra/README.md**: Päivitetty ristiviittauslinkki
- **07-LessonsfromEarlyAdoption/README.md**: Päivitetyt tapaustutkimusviitteet
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Päivitetty osio 9 otsikko, merkit ja ominaisuudet
- **08-BestPractices/README.md**: Päivitetty Discord-yhteisölinkki
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Päivitetty Discord-kanaviite
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Päivitetty mallin käyttöönoton viite
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Päivitetty tekoälypalveluiden taulukko
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Päivitetyt resurssiviitteet

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension VS Codeen
- **README.md**: Päivitetyt pääoppimateriaalin viitteet
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Päivitetty moduulin otsikko, yleiskatsaus ja kaikki moduulin otsikot
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Päivitetty otsikko, oppimistavoitteet, asennusohjeet ja resurssit
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Päivitetty otsikko, oppimistavoitteet, MCP-isäntien taulukko ja ristiviitteet
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Päivitetty otsikko, merkit, ennakkovaatimukset ja resurssit
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Päivitetyt Agent Builder -viitteet ja palautelinkki
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Päivitetyt ennakkovaatimukset ja laajennusviitteet

---

## 11. huhtikuuta 2026

### Uusi oppitunti, dokumentaation korjaukset ja riippuvuuspäivitykset

#### Uutta oppimateriaalissa

**Moduuli 05 - Edistyneet aiheet**
- **Oppitunti 5.17: Vihamielinen moniedustajapäättely MCP:n kanssa** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Uusi kattava opas, joka käsittelee moniedustajajärjestelmien vihamielisen väittelyn mallia
  - Mermaid-arkkitehtuurikaavio: kaksi agenttia → jaettu MCP-palvelin → väittelypöytäkirja → tuomari → tuomio
  - Jaettu MCP-työkalupalvelin (`web_search` + `run_python`) toteutettu Pythonilla ja TypeScripillä
  - Vastaavat järjestelmäkehotteet (PUOLESTA / VASTAAN / Tuomari) eksplisiittisillä työkalujen käyttövaatimuksilla
  - Väittelyn orkestroija Pythonilla, TypeScripillä ja C#:lla, joka hallitsee kierroksia ja reitittää argumentteja
  - MCP `ClientSession` -liitäntä orkestroijalle todellisiin työkalukutsuihin
  - Käyttötapauksia taulukossa (harhaluulon tunnistus, uhkamallinnus, API-suunnittelun tarkistus, tosiasioiden varmistus, teknologian valinta)
  - Turvallisuusnäkökohtia: hiekkalaatikkoajo, työkalukutsujen validointi, nopeusrajoitus, tarkastuslokitus
  - Jäsennelty harjoitus kolmella käytännön skenaariolla (koodikatselmus, arkkitehtuuripäätös, sisällön valvonta)

#### Dokumentaation korjaukset

**Moduuli 03 - Aloittaminen**
- **05-stdio-server/README.md**: Korjattu keskeneräinen TypeScriptin stdio-palvelinesimerkki — lisätty puuttuva kuljetuksen luonti (`new StdioServerTransport()`) ja `server.connect(transport)`-kutsu vastaamaan Pythonin ja .NET:n esimerkkejä samassa osiossa
- **14-sampling/README.md**: Korjattu kirjoitusvirhe — korjattu `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Oppimateriaalipäivitykset

**Pää-README.md**
- Lisätty merkintä 5.17 (Vihamielinen moniedustajapäättely MCP:n kanssa) oppimateriaalitaulukkoon uudella oppitunnilla suoraan linkitettynä

**05-AdvancedTopics/README.md**
- Lisätty oppitunti 5.17 riveihin

**study_guide.md**
- Lisätty Vihamielinen moniedustajapäättely -aihe miellekarttaan ja Advanced Topics -kohdan tekstikuvaan

#### Koodin ja turvallisuuden korjaukset

**Moduuli 05 - Vihamieliset agentit (`mcp-adversarial-agents`)**
- **Turvallisuuskorjaus — komentoinjektio**: Vaihdettu `execSync`-kuoren interpolaatio `execFile` + `promisify` -käyttöön TypeScriptin `run_python` -työkalussa, poistaen komentoinjektion hyökkäyspintaa (LLM-ohjattu koodi välitetään nyt kirjainarvojana ilman kuoren osallisuutta)
- **MCP-työkalusilmukan kytkennät**: Päivitetty Python-kielinen väittelyn orkestroija käyttämään `AsyncAnthropic`-asiakasta (korvaten synkronisen `Anthropic`-estämisen), välittämään live-`ClientSession` suoraan kunkin agenttikierroksen käyttöön, hakemaan työkalumääritykset `session.list_tools()`-kutsulla jokaisella kierroksella, ja suorittamaan `tool_use`-lohkot `session.call_tool()` -kutsun silmukassa, kunnes malli antaa lopullisen tekstivastauksen

#### Riippuvuuspäivitykset

- Korotettu `hono` versioon 4.12.12 useissa paketeissa (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Korotettu `@hono/node-server` versiosta 1.19.11 versioon 1.19.13 TypeScript-paketeissa
- Korotettu `cryptography` versiosta 46.0.5 versioon 46.0.7 Python-paketeissa (10-StreamliningAIWorkflows labrat 3 ja 4)
- Korotettu `lodash` versiosta 4.17.23 versioon 4.18.1 10-StreamliningAIWorkflows-inspektorissa

#### Käännökset

- Synkronoitu yli 48 kielen käännökset uusimpien lähdemuutosten kanssa (i18n-päivitys)

---

## 5. helmikuuta 2026

### Koko arkiston validointi- ja navigointiparannukset

#### Uutta oppimateriaalissa

**Moduuli 03 - Aloittaminen**
- **12-mcp-hosts/README.md**: Uusi kattava opas MCP-isäntien asennukseen
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf -konfigurointiesimerkkejä
  - JSON-konfigurointimallit kaikille isoille isännille
  - Kuljetustyyppien vertailutaulukko (stdio, SSE/HTTP, WebSocket)
  - Yleisimpien yhteysongelmien vianmääritys
  - Turvallisuus parhaat käytännöt isäntäkonfiguraatiossa

- **13-mcp-inspector/README.md**: Uusi vianetsintäopas MCP Inspectorille
  - Asennustavat (npx, npm global, lähdekoodista)
  - Palvelimiin yhdistäminen stdio- ja HTTP/SSE -protokollilla
  - Testityökalut, resurssit ja kehotteiden työnkulut
  - VS Code -integraatio MCP Inspectoriin
  - Yleiset vianetsintätilanteet ja ratkaisut

**Moduuli 04 - Käytännön toteutus**
- **pagination/README.md**: Uusi sivutuksen toteutusopas
  - Kursori-pohjaiset sivutusmallit Pythonissa, TypeScriptissä, Javassa
  - Asiakaspuolen sivutuksen käsittely
  - Kurssorin suunnittelustrategiat (läpinäkymätön vs. jäsennelty)
  - Suorituskyvyn optimointisuositukset

**Moduuli 05 - Edistyneet aiheet**
- **mcp-protocol-features/README.md**: Uusi syväsukellus protokollan ominaisuuksiin
  - Edistymisilmoitusten toteutus
  - Pyynnön peruutusmallit
  - Resurssimallit URI-malleilla
  - Palvelimen elinkaaren hallinta
  - Lokitason ohjaus
  - Virheenkäsittelymallit JSON-RPC-koodeilla

#### Navigointikorjaukset (päivitetty yli 24 tiedostoa)

**Päämoduulin README-tiedostot**
 Linkit nyt sekä ensimmäiseen oppituntiin ETTÄ seuraavaan moduuliin

**02-Security alitiedostot**
- Kaikilla 5 lisätyllä turvallisuusasiakirjalla nyt "Mitä seuraavaksi" -navigointi:

**09-CaseStudy -tiedostot**
- Kaikissa tapaustutkimustiedostoissa on nyt peräkkäinen navigointi:

**10-StreamliningAI Labrat**
Lisätty Mitä seuraavaksi -osio Moduuli 10 yleiskatsaukseen ja Moduuli 11:een

#### Koodin ja sisällön korjaukset

**SDK- ja riippuvuuspäivitykset**
Korjattu avoimen openai-version versio `^4.95.0`
Päivitetty SDK versiosta `^1.8.0` versioon `>=1.26.0`
Päivitetty mcp-version kiinnitykset versioon `>=1.26.0`

**Koodikorjaukset**
Korjattu virheellinen malli `gpt-4o-mini` → `gpt-4.1-mini`

**Sisällön korjaukset**
Korjattu rikki mennyt linkki `READMEmd` → `README.md`, korjattu oppimateriaalin otsikko `Module 1-3` → `Module 0-3`, korjattu kirjainkokoherkkä polku
Poistettu vahingoittunut päällekkäinen Case Study 5 -sisältö

**Aloittelijaohjeiden parannukset**
Lisätty asianmukainen johdanto, oppimistavoitteet ja ennakkovaatimukset aloittelijoille

#### Oppimateriaalipäivitykset

**Pää-README.md**
- Lisätty merkinnät 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) oppimateriaalitaulukkoon

**Moduulien READMEt**
Lisätty oppitunnit 12 ja 13 oppituntilistaan
Lisätty Practical Guides -osio sivutuksen linkillä
Lisätty oppitunnit 5.15 (Custom Transport) ja 5.16 (Protocol Features)

**study_guide.md**
- Päivitetty miellekartta kaikilla uusilla aiheilla: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## 28. tammikuuta 2026

### MCP-spesifikaation 2025-11-25 vaatimustenmukaisuustarkastus

#### Ydinperiaatteiden parannukset (01-CoreConcepts/)
- **Uusi asiakasprimiitti - Roots**: Lisätty kattava dokumentaatio Roots-asiakasprimiitistä, joka mahdollistaa palvelinten ymmärtää tiedostojärjestelmän rajat ja käyttöoikeudet
- **Työkalujen annotaatiot**: Lisätty dokumentaatio työkalujen käyttäytymistietueista (`readOnlyHint`, `destructiveHint`) paremman työkalujen suorituspäätöksen tueksi
- **Työkalukutsut näytteistyksessä**: Päivitetty Näytteistys-dokumentaatio sisältämään `tools` ja `toolChoice` -parametrit malliohjattua työkalukutsua varten näytteistyspyynnöissä
- **URL-tilan kysely**: Lisätty dokumentaatio URL-pohjaisesta ulkoisten verkkovuorovaikutusten aloituksesta palvelimen toimesta
- **Tehtävät (kokeellinen)**: Lisätty uusi osio, joka dokumentoi kokeellisen Tehtävät-ominaisuuden kestäville suorituksen kääreille ja viivevastuiden hakemiselle
- **Ikonien tuki**: Todettu, että työkalut, resurssit, resurssimallit ja kehotteet voivat nyt sisältää ikoneja lisätietona

#### Dokumentaatiopäivitykset
- **README.md**: Lisätty MCP-spesifikaation 2025-11-25 versio- ja päivämääräpohjainen versiointi selitys
- **study_guide.md**: Päivitetty oppimateriaalikartta sisältämään Tehtävät ja Työkaluannotaatiot Ydinperiaatteet-osiossa; päivitetty asiakirjan aikaleima

#### Spesifikaation vaatimustenmukaisuuden varmennus
- **Protokollan versio**: Varmennettu, että kaikki dokumentaatioviitteet vastaavat nykyistä MCP-spesifikaatiota 2025-11-25
- **Arkkitehtuurin yhdenmukaisuus**: Vahvistettu kahden kerroksen arkkitehtuurin (Datalayer + Transportlayer) dokumentaation oikeellisuus
- **Primiittien dokumentaatio**: Tarkistettu palvelimen primiitit (Resurssit, Kehotteet, Työkalut) ja asiakkaan primiitit (Näytteistys, Kysely, Lokitus, Roots)
- **Kuljetusmekanismit**: Varmennettu STDIO- ja Streamable HTTP -kuljetuksen dokumentaation tarkkuus
- **Turvallisuusohjeistus**: Vahvistettu vastaavuus nykyisiin MCP Turvallisuuden parhaiden käytäntöjen dokumentaatioon

#### Keskeiset MCP 2025-11-25 ominaisuudet dokumentoituna
- **OpenID Connectin löytyminen**: Tunnistuspalvelimen löytyminen OIDC:n kautta
- **OAuth Client ID:n metatietodokumentit**: Suositeltu asiakasrekisteröintimekanismi
- **JSON Schema 2020-12**: MCP-skeemojen oletustulkki
- **SDK-kerrosjärjestelmä**: Virallistettu vaatimukset SDK-ominaisuuksien tuelle ja ylläpidolle
- **Hallintorakenne**: Virallistettu MCP:n hallinnassa työryhmät ja intressiryhmät

### Turvallisuudendokumentaation suuri päivitys (02-Security/)

#### MCP Security Summit Workshop (Sherpa) -integraatio
- **Uusi käytännön koulutusresurssi**: Lisätty kattava integraatio [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) -materiaalin kanssa koko turvadokumentaatioon
- **Retkireitin kattavuus**: Dokumentoitu kokonainen leiri-leiriltä kestävään huippusuoritukseen reitti Base Campista Summitille
- **OWASP-vastaavuus**: Kaikki turvallisuusohjeistukset kartoittuvat OWASP MCP Azure -turvaoppaassa määriteltyihin riskeihin

#### OWASP MCP Top 10 -integraatio
- **Uusi osio**: Lisätty OWASP MCP Top 10 -turvariskitaulukko ja Azure-suojaustoimenpiteet pääasialliseen Security README:hen
- **Riskiin perustuva dokumentaatio**: Päivitetty mcp-security-controls-2025.md OWASP MCP -riskiviitteillä jokaisessa turva-alueessa
- **Viitetarkitekturilinkitys**: Linkitetty OWASP MCP Azure Security Guide -viitetarkoitusrakenteeseen ja toteutusmalleihin

#### Päivitetyt turvatiedostot
- **README.md**: Lisätty Sherpa-työpajan yleiskatsaus, retkireittitaulukko, OWASP MCP Top 10 -riskien tiivistelmä ja käytännön harjoittelun osio
- **mcp-security-controls-2025.md**: Päivitetty otsikko helmikuuhun 2026, lisätty OWASP-riskiviitteet (MCP01-MCP08), korjattu spesifikaatioversion epätasaisuus
- **mcp-security-best-practices-2025.md**: Lisätty Sherpa- ja OWASP-resurssit -osio, päivitetty aikaleima
- **mcp-best-practices.md**: Lisätty käytännön harjoitteluosio Sherpa- ja OWASP-linkeillä
- **azure-content-safety-implementation.md**: Lisätty OWASP MCP06 -viite, Sherpa 3. leirille yhdenmukaistus ja lisäresurssiosio

#### Uudet resurssilinkit lisätty
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Yksittäiset OWASP MCP riskisivut (MCP01-MCP10)

### Opetussuunnitelman laajuinen MCP-määrittely 2025-11-25 -linjaus

#### Moduuli 03 - Aloittaminen
- **SDK-dokumentaatio**: Lisätty Go SDK viralliseen SDK-listaan; päivitetty kaikki SDK-viitteet vastaamaan MCP-määrittelyä 2025-11-25
- **Siirtokelpoisuuden tarkennus**: Päivitetty STDIO- ja HTTP-lähdönkuljetuksen kuvaukset sisältämään selkeät määrittelyviitteet

#### Moduuli 04 - Käytännön toteutus
- **SDK-päivitykset**: Lisätty Go SDK; päivitetty SDK-lista sisältämään määrittelyversion viite
- **Valtuutuksen määrittely**: Päivitetty MCP-valtuutusmäärittelyn linkki nykyiseen versioon 2025-11-25

#### Moduuli 05 - Edistyneet aiheet
- **Uudet ominaisuudet**: Lisätty huomautus uusista MCP-määrittelyn 2025-11-25 ominaisuuksista (Tehtävät, Työkalujen annotaatiot, URL-tilan selvitteleminen, Juuret)
- **Turvallisuusresurssit**: Lisätty OWASP MCP Top 10 ja Sherpa-työpajojen linkit lisäviitteisiin

#### Moduuli 06 - Yhteisön panokset
- **SDK-lista**: Lisätty Swift- ja Rust-SDK:t; päivitetty määrittelylinkki versioon 2025-11-25
- **Määrittelyviite**: Päivitetty MCP-määrittelylinkki suoraan määrittelyosoitteeseen

#### Moduuli 07 - Varhaisen käytön opit
- **Resurssipäivitykset**: Lisätty MCP-määrittely 2025-11-25 -linkki ja OWASP MCP Top 10 lisäresursseihin

#### Moduuli 08 - Parhaat käytännöt
- **Määrittelyversion päivitys**: Päivitetty MCP-määrittelyviite versioon 2025-11-25
- **Turvallisuusresurssit**: Lisätty OWASP MCP Top 10 ja Sherpa-työpaja lisäviitteisiin

#### Moduuli 10 - AI-työnkulkujen virtaviivaistaminen
- **Merkintäpäivitys**: Vaihdettu MCP-version merkki SDK-version (1.9.3) sijasta määrittelyversion (2025-11-25) mukaiseksi
- **Resurssilinkit**: Päivitetty MCP-määrittelylinkki; lisätty OWASP MCP Top 10

#### Moduuli 11 - MCP-palvelimen käytännön laboratoriot
- **Määrittelyviite**: Päivitetty MCP-määrittelylinkki versioon 2025-11-25
- **Turvallisuusresurssit**: Lisätty OWASP MCP Top 10 virallisiin resursseihin

## 18. joulukuuta 2025

### Turvallisuusdokumentaation päivitys - MCP-määrittely 2025-11-25

#### MCP:n turvallisuuden parhaat käytännöt (02-Security/mcp-best-practices.md) – Määrittelyversion päivitys
- **Protokollaversion päivitys**: Päivitetty viittaus uusimpaan MCP-määrittelyyn 2025-11-25 (julkaistu 25. marraskuuta 2025)
  - Päivitetty kaikki määrittelyversion viittaukset versiosta 2025-06-18 versioon 2025-11-25
  - Päivitetty asiakirjan päivämääräviitteet 18. elokuuta 2025:stä 18. joulukuuta 2025:een
  - Varmistettu että kaikki määrittelylinkit osoittavat nykyiseen dokumentaatioon
- **Sisällön validointi**: Laaja turvallisuuden parhaiden käytäntöjen tarkistus viimeisimpien standardien mukaisesti
  - **Microsoft Security Solutions**: Tarkistettu nykyiset termit ja linkit Prompt Shieldsille (aiemmin "Jailbreak riskin havaitseminen"), Azure Content Safetylle, Microsoft Entra ID:lle ja Azure Key Vaultille
  - **OAuth 2.1 turvallisuus**: Vahvistettu linjaus uusimpiin OAuth-turvallisuuden parhaisiin käytäntöihin
  - **OWASP-standardit**: Tarkistettu OWASP Top 10 LLM-viitteiden ajantasaisuus
  - **Azure-palvelut**: Varmistettu kaikkien Microsoft Azure -dokumentaatiolinkkien ja parhaiden käytäntöjen ajantasaisuus
- **Standardien noudattaminen**: Kaikki mainitut turvallisuusstandardit vahvistettu ajantasaisiksi
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 turvallisuuden parhaat käytännöt
  - Azure-turvallisuus- ja vaatimustenmukaisuuskehykset
- **Toteutusresurssit**: Tarkistettu kaikki toteutusoppaiden linkit ja resurssit
  - Azure API Management -todennuskuviot
  - Microsoft Entra ID -integraatio-oppaat
  - Azure Key Vault -salaisuuksien hallinta
  - DevSecOps-putket ja valvontaratkaisut

### Dokumentaation laadunvarmistus
- **Määrittelyn noudattaminen**: Varmistettu että kaikki pakolliset MCP-turvavaatimukset (MUST/MUST NOT) ovat linjassa uusimman määrittelyn kanssa
- **Resurssien ajantasaisuus**: Tarkistettu kaikki ulkoiset linkit Microsoftin dokumentaatioon, turvallisuusstandardeihin ja toteutusoppaisiin
- **Parhaiden käytäntöjen kattavuus**: Vahvistettu kattava käsittely todennuksesta, valtuutuksesta, AI-spesifisistä uhkista, toimitusketjun turvallisuudesta ja yritysmallien osalta

## 6. lokakuuta 2025

### Aloitusosion laajennus – Edistynyt palvelimen käyttö ja yksinkertainen todennus

#### Edistynyt palvelimen käyttö (03-GettingStarted/10-advanced)
- **Uusi luku lisätty**: Tarjotaan kattava opas edistyneeseen MCP-palvelimen käyttöön, sisältäen sekä tavallisen että alhaisen tason palvelinarkkitehtuurit.
  - **Tavallinen vs. alhainen taso**: Yksityiskohtainen vertailu ja koodiesimerkit Pythonilla ja TypeScriptilä molemmista lähestymistavoista.
  - **Handler-pohjainen suunnittelu**: Selitys työkalu-/resurssi-/kehotehallinnasta handler-pohjaisissa toteutuksissa, jotka tukevat skaalautuvia, joustavia palvelinratkaisuja.
  - **Käytännön mallit**: Todellisia tilanteita, joissa alhaisen tason palvelinmallit tarjoavat etuja edistyneille ominaisuuksille ja arkkitehtuurille.

#### Yksinkertainen todennus (03-GettingStarted/11-simple-auth)
- **Uusi luku lisätty**: Askelen-askelelta opas yksinkertaisen todennuksen toteuttamiseen MCP-palvelimissa.
  - **Todennus- ja valtuutuskonseptit**: Selkeä erittely todennuksen ja valtuutuksen eroista sekä tunnistetietojen käsittelystä.
  - **Perustodennuksen toteutus**: Middleware-pohjaiset todennuskuviot Pythonilla (Starlette) ja TypeScriptilä (Express), koodiesimerkkien kanssa.
  - **Edistyneen turvallisuuden eteneminen**: Ohjeistus siirtymiseen yksinkertaisesta todennuksesta OAuth 2.1:een ja RBAC:iin, viitteineen edistyneisiin turvaluokkiin.

Nämä lisäykset tarjoavat käytännönläheisen, käsillä olevan ohjauksen vahvempien, turvallisempien ja joustavampien MCP-palvelintoteutusten rakentamiseen yhdistäen perustekijät edistyneisiin tuotantomalleihin.

## 29. syyskuuta 2025

### MCP-palvelimen tietokantaintegraation laboratoriot – Kattava käytännön oppimispolku

#### 11-MCPServerHandsOnLabs – Uusi täydellinen tietokantaintegraatio-opetussuunnitelma
- **Täydellinen 13-laboratoriopolku**: Lisätty kattava käytännön opetussuunnitelma tuotantovalmiiden MCP-palvelimien rakentamiseen PostgreSQL-tietokantaintegraatiolla
  - **Todellinen käyttötapaus**: Zava Retail -analytiikka osoituksena yritystason malleista
  - **Rakenteellinen oppimisjärjestys**:
    - **Laboratoriot 00-03: Perusteet** – Johdanto, ydinarkkitehtuuri, turvallisuus & monivuokraisuus, ympäristön pystytys
    - **Laboratoriot 04-06: MCP-palvelimen rakentaminen** – Tietokantasunnittelu & skeema, MCP-palvelimen toteutus, työkalujen kehitys  
    - **Laboratoriot 07-09: Edistyneet ominaisuudet** – Semanttinen haku, testaus & virheenkorjaus, VS Coden integrointi
    - **Laboratoriot 10-12: Tuotanto & parhaat käytännöt** – Julkaisustrategiat, valvonta & havainnointi, parhaat käytännöt & optimointi
  - **Yritysteknologiat**: FastMCP-kehys, PostgreSQL pgvectorillä, Azure OpenAI Embeddit, Azure Container Apps, Application Insights
  - **Edistyneet ominaisuudet**: Rivitason turvallisuus (RLS), semanttinen haku, monivuokraajan datan käyttö, vektoriembeddit, reaaliaikainen valvonta

#### Terminologian yhdenmukaistaminen – Moduulista laboratorioksi
- **Kattava dokumentaatiopäivitys**: Käyty läpi kaikki 11-MCPServerHandsOnLabsin README-tiedostot ja vaihdettu "Module"-terminologia "Lab"-terminologiaan
  - **Otsikot**: Päivitetty "What This Module Covers" muotoon "What This Lab Covers" kaikissa 13 laboratoriossa
  - **Sisällön kuvaukset**: Muutettu "This module provides..." muotoon "This lab provides..." dokumentaatiossa
  - **Oppimistavoitteet**: Päivitetty "By the end of this module..." muotoon "By the end of this lab..."
  - **Navigointilinkit**: Muutettu kaikki "Module XX:" -viittaukset muotoon "Lab XX:" ristiinviittauksissa ja navigoinnissa
  - **Suorituksen seuranta**: Päivitetty "After completing this module..." muotoon "After completing this lab..."
  - **Tekniset viitteet säilytetty**: Säilytetty Python-moduuliviitteet kokoonpanotiedostoissa (esim. `"module": "mcp_server.main"`)

#### Opasparannus (study_guide.md)
- **Visuaalinen opetussuunnitelmakartta**: Lisätty uusi osio "11. Database Integration Labs" sisältäen kattavan visualisoinnin laboratoriorakenteesta
- **Repositorion rakenne**: Päivitetty kymmenestä yhdentoista pääosioon, lisäten yksityiskohtaisen kuvauksen 11-MCPServerHandsOnLabsistä
- **Oppimispolun ohjaus**: Parannettu navigointiohjeita kattamaan osiot 00-11
- **Teknologian kattavuus**: Lisätty FastMCP, PostgreSQL ja Azure-palvelujen integraatiotiedot
- **Oppimistulokset**: Korostettu tuotantovalmiiden palvelinten kehitystä, tietokantaintegraatiomalleja ja yritysturvallisuutta

#### Pää-README-rakenteen parannus
- **Laboratoriopohjainen terminologia**: Päivitetty 11-MCPServerHandsOnLabsin pää-README.md käyttämään johdonmukaisesti "Lab" -rakennetta
- **Oppimispolun organisointi**: Selkeä eteneminen perusteista edistyneeseen toteutukseen ja tuotantojulkaisuihin
- **Todellisiin tarpeisiin perustuva fokus**: Korostettu käytännönläheistä, lab-pohjaista oppimista yritystason malleilla ja teknologioilla

### Dokumentaation laatu ja johdonmukaisuuden parannukset
- **Käytännönläheinen oppiminen**: Vahvistettu lab-pohjainen lähestymistapa koko dokumentaatiossa
- **Yritysarkkitehtuurimallit**: Korostettu tuotantovalmiita toteutuksia ja yritysturvallisuusnäkökohtia
- **Teknologian integrointi**: Kattava käsittely moderneista Azure-palveluista ja AI-integraatiomalleista
- **Oppimisen eteneminen**: Selkeä, strukturoitu polku perusteista tuotantokäyttöön

## 26. syyskuuta 2025

### Tapaustutkimusten laajennus – GitHub MCP Registry integraatio

#### Tapaustutkimukset (09-CaseStudy/) – Ekosysteemin kehityksen painopiste
- **README.md**: Suuri laajennus, sisältäen kattavan GitHub MCP Registry -tapaustutkimuksen
 - **GitHub MCP Registry -tapaustutkimus**: Uusi kattava tapaustutkimus GitHubin MCP Registryn lanseerauksesta syyskuussa 2025
   - **Ongelman analyysi**: Yksityiskohtainen tarkastelu pirstaloituneiden MCP-palvelinten löytämisen ja käyttöönoton haasteista
   - **Ratkaisuarkkitehtuuri**: GitHubin keskitetty rekisterimalli ja yhden klikkauksen VS Code -asennus
   - **Liiketoimintavaikutukset**: Mitattavissa olevat parannukset kehittäjien käyttöönotossa ja tuottavuudessa
   - **Strateginen arvo**: Painotus modulaarisessa agenttien käyttöönotossa ja työkalujen yhteentoimivuudessa
   - **Ekosysteemin kehitys**: Sijoittuminen perustavanlaatuiseksi alustaksi agenttipohjaiselle integraatiolle
 - **Parannettu tapaustutkimusten rakenne**: Päivitetty kaikki seitsemän tapaustutkimusta yhtenäisellä muotoilulla ja kattavilla kuvauksilla
   - Azure AI Travel Agents: Moni-agenttien orkestroinnin painotus
   - Azure DevOps Integration: Työnkulkujen automaatioon keskittyvä
   - Reaaliaikainen dokumenttien haku: Python-konsoliasiakas
   - Interaktiivinen opintosuunnitelman generaattori: Chainlit-keskusteleva web-sovellus
   - Sisäeditorin dokumentaatio: VS Code ja GitHub Copilot -integraatio
   - Azure API Management: Yritys-API-integraatiomallit
   - GitHub MCP Registry: Ekosysteemin kehitys- ja yhteisöalusta
 - **Kattava yhteenveto**: Uudelleen kirjoitettu päätösosa, joka korostaa seitsemää tapaustutkimusta useissa MCP-toteutuksen ulottuvuuksissa
   - Yrityskiinnitys, moni-agenttien orkestrointi, kehittäjien tuottavuus
   - Ekosysteemin kehitys, koulutussovellusten luokittelu
   - Syventävät näkemykset arkkitehtuurimalleista, toteutusstrategioista ja parhaista käytännöistä
   - Korostus MCP:stä kypsänä, tuotantovalmiina protokollana

#### Opasparannukset (study_guide.md)
- **Visuaalinen opetussuunnitelmakartta**: Päivitetty miellekartta sisältämään GitHub MCP Registry tapaustutkimuksissa
- **Tapaustutkimusten kuvaus**: Parannettu geneerisen kuvauksen korvaamiseksi seitsemän kattavan tapaustutkimuksen yksityiskohdat
- **Repositorion rakenne**: Päivitetty osio 10 heijastamaan laajaa tapaustutkimuskattavuutta ja erityisiä toteutustietoja
- **Muutostenhallinnan integrointi**: Lisätty 26. syyskuuta 2025 merkintä, jossa dokumentoidaan GitHub MCP Registryn lisääminen ja tapaustutkimusten parannukset
- **Päivämääräpäivitykset**: Päivitetty alaviitetunniste vastaamaan uusinta versiota (26. syyskuuta 2025)

### Dokumentaation laadun parannukset
- **Johdonmukaisuuden vahvistus**: Standardoitu tapaustutkimusten muotoilu ja rakenne kaikissa seitsemässä esimerkissä
- **Kattava kattavuus**: Tapaustutkimukset kattavat nyt yritys-, kehittäjien tuottavuuden ja ekosysteemin kehittämistilanteet
- **Strateginen asemoituminen**: Korostettu MCP:n roolia perustavana alustana agenttipohjaisten järjestelmien käyttöönotossa
- **Resurssien integrointi**: Päivitetty lisäresurssit sisältämään GitHub MCP Registry -linkki

## 15. syyskuuta 2025

### Edistyneiden aiheiden laajennus – Mukautetut siirrot ja kontekstisuunnittelu

#### MCP:n mukautetut siirrot (05-AdvancedTopics/mcp-transport/) – Uusi edistyneen toteutuksen opas
- **README.md**: Täydellinen opas mukautettujen MCP-siirtomekanismien toteutukseen
 - **Azure Event Grid -siirto**: Kattava palvelinlainen tapahtumapohjainen siirtototeutus
   - Esimerkit C#:lla, TypeScriptillä ja Pythonilla Azure Functions -integraatiolla
   - Tapahtumapohjaisen arkkitehtuurin mallit skaalautuville MCP-ratkaisuille
   - Webhook-vastaanottajat ja push-viestien käsittely
 - **Azure Event Hubs -siirto**: Korkean läpimenon suoratoistosiirtototeutus
   - Reaaliaikaiset suoratoisto-ominaisuudet matalan viiveen tilanteissa
   - Jakelustrategiat ja checkpoint-hallinta
   - Viestien ryhmittely ja suorituskyvyn optimointi
 - **Yrityksen integraatiomallit**: Tuotantovalmiit arkkitehtuuriesimerkit
   - Hajautettu MCP-käsittely useiden Azure Functionien välillä
   - Hybridisiirtoarkkitehtuurit yhdistäen useita siirtotyyppejä
   - Viestien kestävyyden, luotettavuuden ja virheenkäsittelyn strategiat
 - **Turvallisuus ja valvonta**: Azure Key Vaultin integraatio ja havainnointimallit
   - Hallittu identiteetin todennus ja vähimmän oikeuden periaate
   - Application Insights -telemetria ja suorituskyvyn valvonta
   - Virtakatkaisijat ja vikasietoisuusmallit
 - **Testauskehykset**: Kattavat testaustrategiat mukautetuille siirroille
   - Yksikkötestaus testidobleilla ja mockauskehityksillä
   - Integraatiotestaus Azure Test Containersilla
   - Suorituskyky- ja kuormitustestausnäkökulmat

#### Kontextisuunnittelu (05-AdvancedTopics/mcp-contextengineering/) – Nouseva AI-ala
- **README.md**: Kattava selvitys kontekstisuunnittelusta nousevana alana
 - **Keskeiset periaatteet**: Täydellinen kontekstin jakaminen, toiminnan päätöksentekotietoisuus ja kontekstin ikkunanhallinta

  - **MCP-protokollan linjaus**: Kuinka MCP-muotoilu ratkaisee kontekstitekniikan haasteita
    - Kontekstin ikkunan rajoitukset ja progressiivisen latauksen strategiat
    - Merkityksellisyyden määrittäminen ja dynaaminen kontekstin haku
    - Monimuotoisen kontekstin käsittely ja turvallisuuteen liittyvät näkökohdat
  - **Toteutusmenetelmät**: Yksisäikeiset vs. moniedustaja-arkkitehtuurit
    - Kontekstimurun pilkkomis- ja priorisointitekniikat
    - Progressiivinen kontekstin lataus ja pakkausstrategiat
    - Kerrostetut kontekstimenetelmät ja haun optimointi
  - **Mittauskehys**: Nousevat mittarit kontekstin tehokkuuden arviointiin
    - Syötteen tehokkuus, suorituskyky, laatu ja käyttökokemusnäkökulmat
    - Kokeelliset lähestymistavat kontekstin optimointiin
    - Virheanalyysi ja parannusmenetelmät

#### Opintosuunnitelman navigointipäivitykset (README.md)
- **Parannettu moduulirakenne**: Päivitetty opintosuunnitelman taulukko sisältämään uusia edistyneitä aiheita
  - Lisätty Context Engineering (5.14) ja Custom Transport (5.15) kohteet
  - Johdonmukainen muotoilu ja navigointilinkit kaikissa moduuleissa
  - Päivitetyt kuvaukset vastaamaan nykyistä sisältökattavuutta

### Hakemistorakenteen parannukset
- **Nimien yhdenmukaistus**: Nimetty uudelleen "mcp transport" -> "mcp-transport" yhdenmukaisuuden vuoksi muiden edistyneiden aiheiden kansioiden kanssa
- **Sisällön organisointi**: Kaikki 05-AdvancedTopics-kansiot noudattavat nyt johdonmukaista nimeämiskaavaa (mcp-[aihe])

### Dokumentaation laadun parannukset
- **MCP-määrityksen noudattaminen**: Kaikki uudet sisällöt viittaavat MCP Specification 2025-06-18 -versioon
- **Monikieliset esimerkit**: Laaja valikoima koodiesimerkkejä C#:ssa, TypeScriptissä ja Pythonissa
- **Yrityskeskeisyys**: Tuotantovalmiita malleja ja Azure-pilvipalveluiden integrointia kauttaaltaan
- **Visuaalinen dokumentaatio**: Mermaid-kaaviot arkkitehtuurin ja prosessien visualisointiin

## 18. elokuuta 2025

### Dokumentaation kattava päivitys - MCP 2025-06-18 -standardit

#### MCP:n tietoturvan parhaat käytännöt (02-Security/) - Täydellinen uudistus
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täysi uudelleenkirjoitus MCP Specification 2025-06-18 mukaisesti
  - **Pakolliset vaatimukset**: Lisätyt selkeät PAKOLLISTA/PÄÄLLEMERKIT vaatimukset virallisesta määritelmästä selkein visuaalisin tunnuksin
  - **12 ydintietoturvakäytäntöä**: Järjestelty 15 kohteen listasta kattaviin turvallisuusalueisiin
    - Token-turva ja tunnistautuminen ulkoisen identiteetin tarjoajan integraatiolla
    - Istunnon hallinta ja tiedonsiirron turvallisuus kryptografisin vaatimuksin
    - AI-spesifinen uhkasuojaus Microsoft Prompt Shields -integraatiolla
    - Pääsynhallinta ja oikeudet vähimmäisprivilege-periaatteella
    - Sisällön turvallisuus ja valvonta Azure Content Safety -integraatiolla
    - Toimitusketjun turvallisuus laajan komponenttien tarkistuksen avulla
    - OAuth-turva ja Confused Deputy -hyökkäyksen ehkäisy PKCE-toteutuksella
    - Poikkeaman hallinta ja palautuminen automaattisilla toiminnoilla
    - Säännösten noudattaminen ja hallinto säädösten mukaisesti
    - Edistyneet turvakontrollit zero trust -arkkitehtuurilla
    - Microsoftin tietoturvaekosysteemin integrointi kattavilla ratkaisuilla
    - Jatkuva tietoturvan kehitys adaptiivisten käytäntöjen avulla
  - **Microsoftin tietoturvaratkaisut**: Parannettu ohjeistus Prompt Shieldsin, Azure Content Safetyn, Entra ID:n ja GitHub Advanced Securityn integraatioon
  - **Toteutusresurssit**: Kattavat linkit viralliseen MCP-dokumentaatioon, Microsoftin tietoturvaratkaisuihin, turvallisuusstandardeihin ja toteutusoppaisiin luokiteltuna

#### Edistyneet turvakontrollit (02-Security/) - Yritystason toteutus
- **MCP-SECURITY-CONTROLS-2025.md**: Täysi uudistus yritystason tietoturvakehyksellä
  - **9 laajaa turvallisuusaluetta**: Laajennettu perustason kontrollista yksityiskohtaiseen yrityskehykseen
    - Edistynyt tunnistautuminen ja valtuutus Microsoft Entra ID -integraatiolla
    - Token-turva ja Anti-Passthrough-kontrollit kattavalla validoimisella
    - Istunnon turvallisuuden kontrollit kaappausten estoon
    - AI-spesifiset turvakontrollit kehotteiden injektioiden ja työkalumyrkytyksen estämiseen
    - Confused Deputy -hyökkäyksen ehkäisy OAuth-välityspalvelimen tietoturvalla
    - Työkalujen suorityksen turvallisuus hiekkalaatikkorajausten ja eristyksen avulla
    - Toimitusketjun turvallisuuskontrollit riippuvuustarkistuksilla
    - Valvonta- ja tunnistuskontrollit SIEM-integraatiolla
    - Poikkeamatilanteiden hallinta ja palautuminen automaattisilla toiminnoilla
  - **Toteutusesimerkit**: Lisätty yksityiskohtaisia YAML-konfiguraatiolohkoja ja koodiesimerkkejä
  - **Microsoftin ratkaisujen integrointi**: Kattava Azure-tietoturvapalveluiden, GitHub Advanced Securityn ja yritysten identiteetinhallinnan esittely

#### Edistyneiden aiheiden tietoturva (05-AdvancedTopics/mcp-security/) - Tuotantovalmiit toteutukset
- **README.md**: Täydellinen uudelleenkirjoitus yritysturvallisuuden toteutuksesta
  - **Nykyisen määritelmän mukaisuus**: Päivitetty MCP Specification 2025-06-18 mukaiseksi pakollisine turvallisuusvaatimuksineen
  - **Parannettu tunnistautuminen**: Microsoft Entra ID -integraatio kattavilla .NET- ja Java Spring Security -esimerkeillä
  - **AI-tietoturva-integraatio**: Microsoft Prompt Shieldsin ja Azure Content Safetyn toteutus yksityiskohtaisilla Python-esimerkeillä
  - **Edistynyt uhkien lieventäminen**: Kattavat toteutusesimerkit
    - Confused Deputy -hyökkäyksen ehkäisy PKCE:llä ja käyttäjän suostumuksen validoinnilla
    - Tokenin läpikulkumisen estäminen yleisötarkistuksella ja turvallisella tokenin hallinnalla
    - Istunnon kaappauksen estäminen kryptografisella sidonnalla ja käyttäytymisanalyysillä
  - **Yritysturvallisuuden integraatio**: Azure Application Insights -valvonta, uhkien havainnointiputket ja toimitusketjun turvallisuus
  - **Toteutuschecklistat**: Selkeä pakollisten ja suositeltujen turvakontrollien erottelu Microsoftin tietoturvaekosysteemin eduilla

### Dokumentaation laatu ja standardien mukaisuus
- **Määritysviitteet**: Päivitetty kaikki viitteet MCP Specification 2025-06-18 -versioon
- **Microsoftin tietoturvaekosysteemi**: Parannettu integraatio-ohjeistus koko turvallisuusdokumentaatiossa
- **Käytännön toteutus**: Lisätty yksityiskohtaisia koodiesimerkkejä .NET:ssä, Javassa ja Pythonissa yritysmallien kanssa
- **Resurssien organisointi**: Kattava virallisen dokumentaation, turvallisuusstandardien ja toteutusoppaiden luokittelu
- **Visuaaliset indikaattorit**: Selkeä merkintä pakollisten vaatimusten ja suositeltujen käytäntöjen välillä


#### Peruskäsitteet (01-CoreConcepts/) - Täydellinen uudistus
- **Protokollaversion päivitys**: Päivitetty viittauksia nykyiseen MCP Specification 2025-06-18 versioon, päivämääräpohjaisella versionumeroinnilla (VVVV-KK-PP)
- **Arkkitehtuurin tarkennus**: Parannettu kuvauksia Hosts-, Clients- ja Servers-komponenteista vastaamaan nykyisiä MCP-arkkitehtuurimalleja
  - Hosts nyt selkeästi määritelty tekoälysovelluksiksi, jotka koordinoivat useita MCP-asiakasliityntöjä
  - Clients kuvattu protokollayhteyksinä, jotka ylläpitävät yksi-yhteen palvelin-suhteita
  - Servers päivitetty tukemaan paikallista ja etäasennusta
- **Primitiivien uudelleenjärjestely**: Täydellinen uudistus palvelin- ja asiakasprimitiiveissä
  - Palvelinprimitiivit: Resurssit (datalähteet), Kehotteet (mallit), Työkalut (suoritettavat funktiot) yksityiskohtineen ja esimerkkien kera
  - Asiakasprimitiivit: Otanta (LLM-vastausten luonti), Kysely (käyttäjän syöte), Lokitus (debug- ja valvontatiedot)
  - Päivitetty nykyisiin löytö (`*/list`), haku (`*/get`) ja suoritus (`*/call`) -menetelmiin
- **Protokollan arkkitehtuuri**: Esitelty kaksikerroksinen arkkitehtuurimalli
  - Datakerros: JSON-RPC 2.0 pohja elinkaaren hallinnalla ja primitiiveillä
  - Siirtokerros: STDIO (paikallinen) ja muunnettava HTTP SSE:n kanssa (etäkuljetusmekanismit)
- **Turvakehys**: Kattavat tietoturvaperiaatteet, sisältäen eksplisiittisen käyttäjälupauksen, tietosuojan, työkalujen suojauksen ja siirtotason turvan
- **Viestintämallit**: Päivitetyt protokollaviestit näyttämään alustuksen, löydön, suorituksen ja ilmoitusvirrat
- **Koodiesimerkit**: Päivitetyt monikieliset esimerkit (.NET, Java, Python, JavaScript) vastaamaan nykyisiä MCP SDK -käytäntöjä

#### Turvallisuus (02-Security/) - Kattava tietoturvan uudistus  
- **Standardien mukaisuus**: Täysi linjaus MCP Specification 2025-06-18:n turvallisuusvaatimuksiin
- **Tunnistautumisen kehitys**: Dokumentoitu siirtyminen räätälöidyistä OAuth-palvelimista ulkoisten identiteetin tarjoajien delegointiin (Microsoft Entra ID)
- **AI-spesifinen uhkanalyysi**: Parannettu nykyaikaisten AI-hyökkäysvektorien kattavuus
  - Yksityiskohtaiset vinkkeihin kohdistuvat hyökkäysskenaariot todellisilla esimerkeillä
  - Työkalumyrkytysmenetelmät ja "rug pull" -hyökkäysmallit
  - Kontekstin ikkunan myrkytys ja mallin väärintulkinta hyökkäykset
- **Microsoftin AI-tietoturvaratkaisut**: Kattava esittely Microsoftin tietoturvaekosysteemistä
  - AI Prompt Shields kehittyneellä havaitsemisella, valaisulla ja erottelutekniikoilla
  - Azure Content Safety -integraatiomallit
  - GitHub Advanced Security toimitusketjun suojeluun
- **Edistynyt uhkien lieventäminen**: Yksityiskohtaiset turvakontrollit
  - Istunnon kaappauksen estäminen MCP-spesifisillä uhkaskenaarioilla ja kryptografisilla istuntotunnistevaatimuksilla
  - Confused Deputy -ongelmat MCP-välityspalvelinnäkymissä eksplisiittisillä suostumusvaatimuksilla
  - Token-läpikulkuhaavoittuvuudet pakollisilla validointikontrolleilla
- **Toimitusketjun turvallisuus**: Laajennettu AI-toimitusketjun kattavuus mm. perustamismallit, upotepalvelut, kontekstin tarjoajat ja kolmannen osapuolen rajapinnat
- **Perustietoturva**: Parannettu integraatio yritystason turvallisuusmalleihin kuten zero trust -arkkitehtuuriin ja Microsoftin tietoturvaekosysteemiin
- **Resurssien organisointi**: Luokitellut kattavat resurssilinkit tyypin mukaan (Viralliset dokumentit, standardit, tutkimus, Microsoftin ratkaisut, toteutusoppaat)

### Dokumentaation laadun parannukset
- **Rakenteelliset oppimistavoitteet**: Parannettu oppimistavoitteita spesifisillä, toteutettavilla tuloksilla 
- **Ristiinviittaukset**: Lisätty linkkejä liittyvien turvallisuus- ja peruskäsiteaiheiden välillä
- **Ajantasaiset tiedot**: Päivitetty kaikki päivämääräviitteet ja määritykset vastaamaan nykyisiä standardeja
- **Toteutusohjeistukset**: Lisätty spesifisiä, toteutettavia ohjeita molempiin osioihin

## 16. heinäkuuta 2025

### README ja navigointiparannukset
- Täysin uudistettu opintosuunnitelman navigointi README.md-tiedostossa
- Vaihdettu `<details>`-tagit paremmin saavutettavaan taulukkopohjaiseen muotoon
- Luotu vaihtoehtoisia asetteluvaihtoehtoja uuteen "alternative_layouts" -kansioon
- Lisätty korttipohjaisia, välilehtityylisiä ja harmonikkatyylisiä navigointiesimerkkejä
- Päivitetty repository-rakenteen osio sisältämään kaikki uusimmat tiedostot
- Parannettu "Kuinka käyttää tätä opintosuunnitelmaa" -osiota selkeillä suosituksilla
- Päivitetty MCP-määritysten linkit osoittamaan oikeisiin URL-osoitteisiin
- Lisätty Context Engineering -osio (5.14) opintosuunnitelman rakenteeseen

### Opintovinkkien päivitykset
- Täysin uudistettu opintovihko vastaamaan nykyistä repository-rakennetta
- Lisätty uusia osioita MCP-asiakkaille ja työkaluilla, sekä suosituimmille MCP-palvelimille
- Päivitetty Visuaalinen opintosuunnitelmakartta vastaamaan kaikkia aiheita tarkasti
- Parannettu kuvaus edistyneistä aiheista kattamaan kaikki erikoisalat
- Päivitetty tapaustutkimusosio vastaamaan todellisia esimerkkejä
- Lisätty tämä kattava muutosloki

### Yhteisön panokset (06-CommunityContributions/)
- Lisätty yksityiskohtaiset tiedot MCP-palvelimista kuvantuotantoon
- Lisätty kattava osio Clauden käytöstä VSCode:ssa
- Lisätty Cline-päätelmäasiakkaan asennus- ja käyttöohjeet
- Päivitetty MCP-asiakasosio sisältämään kaikki suositut asiakasvaihtoehdot
- Parannettu kontribuutiokohteiden esimerkit tarkemmilla koodinäytteillä

### Edistyneet aiheet (05-AdvancedTopics/)
- Järjestetty kaikki erikoistuneet aiheiden kansiot yhdenmukaisin nimityksin
- Lisätty kontekstitekniikan materiaaleja ja esimerkkejä
- Lisätty Foundry-agentin integraatiodokumentaatio
- Parannettu Entra ID -turvallisuusintegraatiodokumentaatiota

## 11. kesäkuuta 2025

### Alkuperäinen luonti
- Julkaistu ensimmäinen versio MCP for Beginners -opintosuunnitelmasta
- Luotu perusrakenne kaikille 10 pääosalle
- Toteutettu visuaalinen opintosuunnitelmakartta navigointiin
- Lisätty aloittelevat esimerkkiprojektit useilla ohjelmointikielillä

### Aloitus (03-GettingStarted/)
- Luotu ensimmäiset palvelintoteutusesimerkit
- Lisätty asiakkaan kehitysohjeistus
- Sisällytetty LLM-asiakkaan integraatio-ohjeet
- Lisätty VS Code -integraatiodokumentaatio
- Toteutettu Server-Sent Events (SSE) palvelinesimerkit

### Peruskäsitteet (01-CoreConcepts/)
- Lisätty yksityiskohtainen selitys asiakas-palvelinarkkitehtuurista
- Luotu dokumentaatio keskeisistä protokollan komponenteista
- Dokumentoitu viestintämallit MCP:ssä

## 23. toukokuuta 2025

### Repository-rakenne
- Aloitettu repository perusrakenteella
- Luotu README-tiedostot jokaiselle pääosalle
- Perustettu käännösinfrastruktuuri
- Lisätty kuvia ja kaavioita

### Dokumentaatio
- Luotu aloitteellinen README.md opintosuunnitelman yleiskatsauksella
- Lisätty CODE_OF_CONDUCT.md ja SECURITY.md
- Perustettu SUPPORT.md ohjeistuksella avun saamiseksi
- Luotu alustava opintovihkon rakenne

## 15. huhtikuuta 2025

### Suunnittelu ja kehys
- Ensimmäinen suunnittelu MCP for Beginners -opintosuunnitelmalle
- Määritelty oppimistavoitteet ja kohderyhmä
- Piirretty 10-osainen rakenne opintosuunnitelmalle
- Kehitetty konseptuaalinen kehys esimerkeille ja tapaustutkimuksille
- Luotu ensimmäiset prototyypin esimerkit keskeisistä käsitteistä

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->