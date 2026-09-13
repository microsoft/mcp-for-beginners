# MCP-tietoturva: Kattava suojaus AI-järjestelmille

[![MCP-tietoturvan parhaat käytännöt](../../../translated_images/fi/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Turvallisuus on perustavanlaatuista AI-järjestelmien suunnittelussa, minkä vuoksi asetamme sen toiseen osioon. Tämä on linjassa Microsoftin **Secure by Design** -periaatteen kanssa [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/)-ohjelmasta.

Model Context Protocol (MCP) tuo voimakkaita uusia mahdollisuuksia AI-pohjaisiin sovelluksiin samalla kun se tuo mukanaan ainutlaatuisia tietoturhahaasteita, jotka ylittävät perinteisen ohjelmistoriskit. MCP-järjestelmät kohtaavat sekä vakiintuneita tietoturvakysymyksiä (turvallinen koodaus, vähiten oikeuksia, toimitusketjun turvallisuus) että uusia AI-spesifisiä uhkia, kuten kehotteiden injektiot, työkalumyrkytys, istunnonkaappaukset, sekaantuneet valtuutuksen ongelmat, tunnisteiden läpikulkuhaavoittuvuudet ja dynaaminen kyvykkyyksien muokkaus.

Tässä oppitunnissa käydään läpi tärkeimmät tietoturvariskit MCP-toteutuksissa—sisältäen todennuksen, valtuutuksen, liiallisen käyttöoikeuden, epäsuoran kehotteen injektion, istuntojen turvallisuuden, sekaantuneen valtuutetun ongelmat, tunnisteiden hallinnan ja toimitusketjun haavoittuvuudet. Opit käytännöllisiä ohjaimia ja parhaita käytäntöjä riskien lieventämiseksi hyödyntäen Microsoftin ratkaisuja, kuten Prompt Shields, Azure Content Safety ja GitHub Advanced Security, vahvistaaksesi MCP-järjestelmääsi.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- **Tunnistaa MCP-Spesifiset Uhat**: Tunnistaa MCP-järjestelmille ominaiset tietoturvariskit, mukaan lukien kehotteen injektio, työkalumyrkytys, liialliset käyttöoikeudet, istunnon kaappaus, sekaantuneet valtuutetut, tunnisteiden läpikulkuhaavoittuvuudet ja toimitusketjun riskit
- **Soveltaa Turvallisuusohjaimia**: Toteuttaa tehokkaita lieventäviä toimia, kuten vahva tunnistus, vähimmäisoikeudet, turvallinen tunnisteiden hallinta, istuntojen turvallisuus ja toimitusketjun varmistus
- **Hyödyntää Microsoftin Tietoturvaratkaisuja**: Ymmärtää ja ottaa käyttöön Microsoft Prompt Shields, Azure Content Safety ja GitHub Advanced Security MCP-kuormituksen suojaamiseen
- **Varmistaa Työkalujen Turvallisuus**: Tunnistaa työkalujen metatietojen validoinnin, dynaamisten muutosten seurannan ja epäsuorien kehotteiden injektiohyökkäysten puolustuksen merkityksen
- **Yhdistää Parhaat Käytännöt**: Yhdistää vakiintuneet tietoturvan perusteet (turvallinen koodaus, palvelimen koventaminen, zero trust) MCP-spesifisiin ohjaimiin kattavaa suojaa varten

# MCP-tietoturva-arkkitehtuuri ja ohjaimet

Nykyiset MCP-toteutukset vaativat kerroksellisia turvallisuuslähestymistapoja, jotka käsittelevät sekä perinteistä ohjelmistoturvallisuutta että AI-spesifisiä uhkia. Nopeasti kehittyvä MCP-spesifikaatio jatkaa tietoturvaohjaimiensa kypsyttämistä, mahdollistaen paremman integraation yritysturvallisuusarkkitehtuureihin ja vakiintuneisiin parhaisiin käytäntöihin.

[Microsoft Digital Defense Report](https://aka.ms/mddr) -tutkimus osoittaa, että **98 % raportoituja tietomurtoja voitaisiin estää vahvalla tietoturvahyveellisyydellä**. Tehokkain suojausstrategia yhdistää perusturvallisuuskäytännöt MCP-spesifisiin ohjaimiin—todistetut perussuojaukset ovat kaikkein vaikuttavimpia vähentämään kokonaisriskiä.

## Nykyinen tietoturvatilanne

> **Huom:** Tässä luvussa yhdistetään vakiintuneet MCP-tietoturvaohjaimet ja
> ajantasainen **MCP Specification 2026-07-28** -valtuutusopastus. Viittaa aina
> nykyiseen [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub -varastoon](https://github.com/modelcontextprotocol) ja
> [tietoturvan parhaat käytännöt -dokumentaatioon](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> kun toteutat tietoturvakriittistä koodia.

> **Valtuutuksen päivitys:** MCP `2026-07-28` edellyttää, että asiakkaat tarkistavat
> `iss`-parametrin valtuutusvastauksissa (RFC 9207) ja sitovat rekisteröidyt
> tunnistetiedot valtuuttavaan valtuutuspalvelimeen. Dynaaminen asiakasrekisteröinti
> on poistettu käytöstä; uudet toteutukset käyttävät Client ID Metadata -dokumentteja.
> Katso [Mitä on muuttunut MCP:ssä: 2026-07-28 -spesifikaatio](../01-CoreConcepts/mcp-2026-07-28.md)
> täydellisestä listauksesta valtuutusmuutoksille.

## 🏔️ MCP Security Summit -työpaja (Sherpa)

Käytännön tietoturvakoulutusta varten suosittelemme lämpimästi **MCP Security Summit Workshop** (Sherpa) - kokonaista opastettua retkeä MCP-palvelinten suojaamiseen Microsoft Azure -ympäristössä.

### Työpajan yleiskatsaus

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) tarjoaa käytännönläheistä, sovellettavaa tietoturvakoulutusta todistetulla "haavoittuvuus → hyväksikäyttö → korjaus → validointi" -menetelmällä. Sinä:

- **Opiskele rikkomalla asioita**: Kokea haavoittuvuuksia suoraan hyväksikäyttämällä tarkoituksellisesti epävarmoja palvelimia
- **Käytä Azure-nativeo tietoturvaa**: Hyödynnä Azure Entra ID:tä, Key Vaultia, API Managementia ja AI Content Safetyä
- **Noudata Defense-in-Depthiä**: Edisty leireittäin rakentaen kattavia tietoturvakerroksia
- **Sovella OWASP-standardeja**: Jokainen tekniikka vastaa [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) -ohjeistusta
- **Saat tuotantokoodin**: Saat käyttöösi toimivat, testatut toteutukset

### Retken reitti

| Leiri | Fokus | Kattavat OWASP-riskit |
|------|-------|---------------------|
| **Perusleiri** | MCP:n perusteet ja todennushaavoittuvuudet | MCP01, MCP07 |
| **Leiri 1: Identiteetti** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Leiri 2: Välityspalvelin** | API Management, Private Endpoints, hallinta | MCP02, MCP06, MCP07, MCP09 |
| **Leiri 3: Sisääntulo/uloskäynti-tietoturva** | Kehotteen injektio, PII-suojaus, sisältöturva | MCP03, MCP05, MCP06, MCP10 |
| **Leiri 4: Valvonta** | Lokianalytiikka, koontinäytöt, uhkien havaitseminen | MCP04, MCP08 |
| **Huippukokous** | Red Team / Blue Team -integraatiotesti | Kaikki |

**Aloita tästä**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 turvallisuusriskiä

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) kuvaa kymmenen kriittisintä tietoturvariskiä MCP-toteutuksille:

| Riski | Kuvaus | Azure-lievitys |
|------|-------------|------------------|
| **MCP01** | Tunnisteiden huono hallinta ja salaisuuksien vuoto | Azure Key Vault, Managed Identity |
| **MCP02** | Oikeustason korotus päällekkäisillä oikeuksilla | RBAC, Ehdollinen pääsy |
| **MCP03** | Työkalumyrkytys | Työkalujen validointi, eheyden varmistus |
| **MCP04** | Ohjelmistotoimitusketjun hyökkäykset ja riippuvuuksien manipulointi | GitHub Advanced Security, riippuvuusskannaus |
| **MCP05** | Komentoinjektio ja suorittaminen | Syötteen validointi, hiekkalaatikkoympäristö |
| **MCP06** | Aikomuksen ohjausvirheet | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Puutteellinen todennus ja valtuutus | Azure Entra ID, OAuth 2.1 PKCE:llä |
| **MCP08** | Tarkastus- ja telemetriavaje | Azure Monitor, Application Insights |
| **MCP09** | Varjopalvelimet MCP:lle | API Center -hallinta, verkkoeristys |
| **MCP10** | Kontekstin injektio ja liiallinen tiedonjako | Datan luokittelu, minimaltaltistus |

### MCP-todennuksen kehitys

MCP-spesifikaatio on kehittynyt merkittävästi todennuksen ja valtuutuksen osalta:

- **Alkuperäinen lähestymistapa**: Varhaiset spesifikaatiot edellyttivät kehittäjiä toteuttamaan mukautettuja todennuspalvelimia, joissa MCP-palvelimet toimivat OAuth 2.0 -valtuutuspalvelimina halliten käyttäjien todennusta suoraan
- **Nykyinen standardi (`2026-07-28`)**: MCP-palvelimet voivat delegoida todennuksen
  ulkoisille identiteetin tarjoajille, kuten Microsoft Entra ID:lle. Asiakkaiden on myös
  noudatettava nykyisiä julkaisijan tarkistus- ja tunnistetietojen sitomisvaatimuksia.
- **Kuljetuskerroksen turvallisuus**: Parannettu tuki turvallisille siirtomekanismeille paikallisissa (STDIO) ja etäyhteyksissä (Streamable HTTP) asianmukaisilla todennusmalleilla

## Todennus- ja valtuutusturva

### Nykyiset turvallisuushaasteet

Nykyaikaiset MCP-toteutukset kohtaavat useita todennus- ja valtuutushaasteita:

### Riskit & Uhkamallit

- **Väärin konfiguroitu valtuutuslogiikka**: MCP-palvelinten virheellinen valtuutuksen toteutus voi paljastaa arkaluonteisia tietoja ja soveltaa pääsynkontrolleja väärin
- **OAuth-tunnisteiden vaarantuminen**: Paikallisen MCP-palvelimen tunnisteiden varastaminen mahdollistaa hyökkääjien esiintymisen palvelimina ja pääsyn alasuuntapalveluihin
- **Tunnisteiden läpikulun haavoittuvuudet**: Virheellinen tunnisten käsittely luo turvallisuusohjaimien kiertämiä ja vastuukatoja
- **Liialliset käyttöoikeudet**: Yli oikeutetut MCP-palvelimet rikkovat vähiten oikeuksia -periaatetta ja laajentavat hyökkäyspintaa

#### Tunnisteiden läpikulku: kriittinen anti-kuvio

**Tunnisteiden läpikulkua on nykyisessä MCP-valtuutussääntelyssä nimenomaisesti kielletty** vakavien turvallisuusvaikutusten vuoksi:

##### Turvallisuusohjaimien kierto
- MCP-palvelimet ja alasuuntaiset API:t toteuttavat kriittisiä tietoturvaohjaimia (kuten käyttörajoitukset, pyyntötarkastukset, liikenteen seuranta), jotka perustuvat asianmukaiseen tunnisteratkaisuun
- Suora asiakas-API-tunnisteiden käyttö ohittaa nämä oleelliset suojaukset, heikentäen turvallisuusarkkitehtuuria

##### Vastuu- ja tarkastushaasteet  
- MCP-palvelimet eivät pysty erottamaan asiakkaita, jotka käyttävät ylävirran myöntämiä tunnisteita, katkaisten tarkasteluketjut
- Alasuunnan resurssipalvelimen lokit näyttävät harhaanjohtavia pyyntöjen alkuperää todellisten MCP-välittäjien sijaan
- Tapaustutkinnat ja vaatimustenmukaisuustarkastukset vaikeutuvat merkittävästi

##### Datan ulosvuotoriskit
- Vahvistamattomat tunnisteväitteet mahdollistavat pahoissa tarkoituksissa varastettujen tunnisteiden käyttämisen MCP-palvelimien kautta datan ulosvientiin
- Luottamusrikkomukset sallivat valtuuttamattomat pääsytavat, jotka ohittavat suunnitellut turvallisuusohjaimet

##### Moni-palvelun hyökkäysvektorit
- Hyväksytyt vaarantuneet tunnisteet monissa palveluissa mahdollistavat sivuttaisliikettä yhteyksissä
- Luottamusolettamukset palveluiden välillä voivat rikkoutua, kun tunnisteen alkuperää ei voida varmistaa

### Turvallisuusohjaimet ja lieventäminen

**Kriittiset turvallisuusvaatimukset:**

> **VÄLTTÄMÄTÖNTÄ:** MCP-palvelimet **EIVÄT SAA** hyväksyä tunnisteita, joita ei nimenomaisesti ole myönnetty kyseiselle MCP-palvelimelle

#### Todennus- ja valtuutusohjaimet

- **Tiukka valtuutuksen tarkastelu**: Suorita perusteellisia auditointeja MCP-palvelinten valtuutuslogiikasta varmistaaksesi, että vain tarkoitetut käyttäjät ja asiakkaat pääsevät arkaluonteisiin resursseihin
  - **Toteutusopas**: [Azure API Management MCP-palvelimien tunnistuksen porttina](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identiteettien integraatio**: [Microsoft Entra ID:n käyttö MCP-palvelinten todennuksessa](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Turvallinen tunnisteiden hallinta**: Käytä [Microsoftin tunnisteiden validointi- ja elinkaaren parhaat käytännöt](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Varmista tunnisteen vastaanottajan väitteet vastaamaan MCP-palvelimen identiteettiä
  - Toteuta asianmukaiset tunnisteiden kierto- ja vanhenemiskäytännöt
  - Estä tunnisteiden uudelleenkäyttöhyökkäykset ja valtuuttamaton käyttö

- **Suojaus tunnisteiden säilytyksessä**: Salaa tunnisteet sekä levossa että siirrossa
  - **Parhaat käytännöt**: [Turvallinen tunnisteiden säilytys ja salaussuositukset](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Pääsynvalvonnan toteutus

- **Vähimmäisoikeuden periaate**: Myönnä MCP-palvelimille vain toiminnallisuuteen tarvittavat minimioikeudet
  - Säännölliset käyttöoikeuksien tarkistukset ja päivitykset estämään käyttöoikeuksien kasvu
  - **Microsoft-dokumentaatio**: [Turvallinen vähimmäisoikeuksien käyttö](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Roolipohjainen pääsynvalvonta (RBAC)**: Toteuta hienojakoiset roolimääritykset
  - Kohdista roolit tarkasti tiettyihin resursseihin ja toimintoihin
  - Vältä laajoja tai tarpeettomia oikeuksia, jotka laajentavat hyökkäyspintaa

- **Jatkuva käyttöoikeuksien valvonta**: Toteuta jatkuva pääsyn auditointi ja seuranta
  - Seuraa käyttöoikeuksien käyttökuvioita poikkeavuuksien varalta
  - Korjaa nopeasti liialliset tai käyttämättömät oikeudet

## AI-spesifiset tietoturvauhat

### Kehotteen injektio- ja työkalumanipulaatiohyökkäykset

Nykyaikaiset MCP-toteutukset kohtaavat kehittyneitä AI-spesifisiä hyökkäysmuotoja, joita perinteiset tietoturvatoimet eivät täysin kata:

#### **Epäsuora kehotteen injektio (ristialueen kehotteen injektio)**

**Epäsuora kehotteen injektio** on yksi kriittisimmistä haavoittuvuuksista MCP-vuorovaikutteisia AI-järjestelmiä käytettäessä. Hyökkääjät upottavat haitallisia käskyjä ulkoiseen sisältöön—dokumentteihin, verkkosivuihin, sähköposteihin tai tietolähteisiin—joita AI-järjestelmät käsittelevät myöhemmin oikeina käskyinä.

**Hyökkäysskenaariot:**
- **Dokumenttipohjainen injektio**: Haitalliset ohjeet piilotettu käsiteltäviin dokumentteihin, jotka aiheuttavat tekoälyn suorittavan tahattomia toimia
- **Web-sisällön hyväksikäyttö**: Vaarantuneet verkkosivut sisältäen upotettuja kehotteita, jotka ohjaavat AI:n käyttäytymistä web-sivujen keruun yhteydessä
- **Sähköpostipohjaiset hyökkäykset**: Haitalliset kehotteet sähköposteissa, jotka saavat tekoälyavustajat vuotamaan tietoja tai suorittamaan valtuuttamattomia toimia
- **Tietolähteen saastutus**: Vaarantuneet tietokannat tai API:t, jotka tarjoavat saastunutta sisältöä AI-järjestelmille

**Todellinen vaikutus**: Nämä hyökkäykset voivat johtaa datan vuotoon, yksityisyyden loukkauksiin, haitallisen sisällön generointiin ja käyttäjävuorovaikutusten manipulointiin. Tarkempaan analyysiin katso [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Kehotteen injektiohyökkäyskaavio](../../../translated_images/fi/prompt-injection.ed9fbfde297ca877.webp)

#### **Työkalumyrkytyshyökkäykset**

**Työkalumyrkytys** kohdistuu MCP-työkalujen metatietoihin, hyväksikäyttäen tapaa, jolla LLM-mallit tulkitsevat työkalujen kuvauksia ja parametrejä suorituspäätösten tekemiseen.

**Hyökkäysmekanismit:**
- **Metatietojen manipulointi**: Hyökkääjät injektoivat haitallisia ohjeita työkalukuvausten, parametrien määrittelyjen tai käyttöesimerkkien sekaan
- **Näkymättömät ohjeet**: Piilotetut kehotteet työkalun metatiedoissa, joita AI-mallit käsittelevät mutta ihmiskäyttäjät eivät näe
- **Dynaaminen työkalun muokkaus ("Rug Pulls")**: Käyttäjien hyväksymät työkalut muokataan myöhemmin suorittamaan haitallisia toimia käyttäjän tietämättä
- **Parametrien injektio**: Haitallinen sisältö upotetaan työkalun parametriskeemoihin, vaikuttaen mallin käyttäytymiseen


**Isännöityjen palvelimien riskit**: Etä-MCP-palvelimet aiheuttavat kohonneita riskejä, koska työkalumäärittelyjä voidaan päivittää alkuperäisen käyttäjän hyväksynnän jälkeen, mikä luo tilanteita, joissa aiemmin turvalliset työkalut muuttuvat haitallisiksi. Yksityiskohtaiseen analyysiin katso [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Työkalun injektiohyökkäyksen kaavio](../../../translated_images/fi/tool-injection.3b0b4a6b24de6bef.webp)

#### **Lisättyjä tekoälyhyökkäysvektoreita**

- **Ristidomain-promptin injektio (XPIA)**: Edistyneet hyökkäykset, jotka hyödyntävät sisältöä useista domaineista turvatoimien ohittamiseksi
- **Dynaaminen kyvykkyyden muokkaus**: Työkalujen kyvykkyyksien reaaliaikaiset muutokset, jotka pakenemaan alkuperäiset turvallisuusarviot
- **Kontekstin ikkunan myrkytys**: Hyökkäykset, jotka manipuloivat suuria kontekstikonteksteja piilottaakseen haitalliset ohjeet
- **Mallin sekaannushyökkäykset**: Mallin rajoitusten hyväksikäyttö arvaamattomien tai turvattomien käyttäytymisten luomiseksi


### Tekoälyn turvallisuusriskin vaikutukset

**Korkean vaikutuksen seuraukset:**
- **Datan vuoto**: Luvaton pääsy ja arkaluonteisen yritys- tai henkilötiedon varastaminen
- **Yksityisyyden loukkaukset**: Henkilöllisyyteen liittyvän ja luottamuksellisen liiketoimintatiedon altistuminen  
- **Järjestelmän manipulointi**: Tahattomat muutokset kriittisiin järjestelmiin ja työnkulkuihin
- **Tunnistetietojen varastaminen**: Todennustunnusten ja palvelutunnusten vaarantuminen
- **Sivuttaisliikutus**: Hyväksikäytettyjen tekoälyjärjestelmien käyttö verkkohyökkäysten laajentamiseen

### Microsoftin tekoälytietoturvaratkaisut

#### **AI Prompt Shields: Edistynyt suojaus injektiohyökkäyksiä vastaan**

Microsoftin **AI Prompt Shields** tarjoaa kattavan puolustuksen sekä suorien että epäsuorien kehotteen injektiohyökkäysten varalta monilla turvakerroksilla:

##### **Perussuojausmekanismit:**

1. **Edistynyt tunnistus & suodatus**
   - Koneoppimisalgoritmit ja NLP-tekniikat havaitsevat haitalliset ohjeet ulkoisessa sisällössä
   - Asiakirjojen, verkkosivujen, sähköpostien ja tietolähteiden reaaliaikainen analyysi upotettujen uhkien havaitsemiseksi
   - Kontekstuaalinen ymmärrys laillisista vs. haitallisista kehotemuodoista

2. **Spotlight-tekniikat**  
   - Erottelee luotettavat järjestelmäohjeet potentiaalisesti vaarantuneista ulkoisista syötteistä
   - Tekstimuunnosmenetelmät, jotka parantavat mallin relevanssia samalla kun ne eristävät haitallisen sisällön
   - Auttaa tekoälyjärjestelmiä ylläpitämään oikean ohjehierarkian ja ohittaa injektoidut komennot

3. **Erotin- & datamerkintäjärjestelmät**
   - Selkeä rajaus luotettavien järjestelmäviestien ja ulkoisen tekstisyötteen välillä
   - Erityiset merkit korostavat rajoja luotettujen ja epäluotettavien tietolähteiden välillä
   - Selvä erottelu estää ohjeiden sekoittumisen ja luvattoman käskyn suorittamisen

4. **Jatkuva uhkatiedustelu**
   - Microsoft seuraa jatkuvasti uusia hyökkäysmalleja ja päivittää puolustusta
   - Proaktiivinen uhkien metsästys uusien injektiotekniikoiden ja hyökkäysvektorien tunnistamiseksi
   - Säännölliset turvallisuusmallipäivitykset tehokkuuden ylläpitämiseksi kehittyviä uhkia vastaan

5. **Azure Content Safety -integraatio**
   - Osa kattavaa Azure AI Content Safety -kokonaisuutta
   - Lisähavainnointi jailbreak-yrityksille, haitalliselle sisällölle ja turvallisuuspolitiikkojen rikkomisille
   - Yhtenäiset turvatoimet tekoälysovellusten komponenteille

**Toteutusresurssit**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/fi/prompt-shield.ff5b95be76e9c78c.webp)


## Kehittyneet MCP:n turvallisuusuhat

### Istunnonkaappaushaarukkeet

**Istunnonkaappaus** on kriittinen hyökkäysvektori tilallisten MCP-toteutusten yhteydessä, jossa luvattomat osapuolet hankkivat ja hyväksikäyttävät laillisia istunnon tunnisteita asiakkaina esiintymiseen ja luvattomien toimintojen suorittamiseen.

#### **Hyökkäysskenaariot & riskit**

- **Istunton kaappaus prompt injektio**: Hyökkääjät, joilla on varastetut istuntotunnukset, injektoivat haitallisia tapahtumia palvelimille, jotka jakavat istuntotilan, mahdollistaen vaaralliset toimet tai pääsyn arkaluonteiseen dataan
- **Suora naamioituminen**: Varastetut istuntotunnukset mahdollistavat suorat MCP-palvelukutsut, jotka ohittavat todennuksen ja käsittelevät hyökkääjää laillisena käyttäjänä
- **Vaarantuneet keskeytettävät virtaukset**: Hyökkääjät voivat keskeyttää pyynnöt ennenaikaisesti, jolloin lailliset asiakkaat jatkuvat mahdollisesti haitallisella sisällöllä

#### **Turvatoimet istunnoissa**

**Keskeiset vaatimukset:**
- **Valtuutuksen vahvistus**: MCP-palvelinten, jotka toteuttavat valtuutuksen, **TÄYTYY** tarkistaa KAIKKI sisääntulevat pyynnöt eikä niitä saa tukeutua istuntoihin todennuksessa
- **Turvallinen istunnon luonti**: Käytä kryptografisesti turvallisia, ei-deterministisiä istuntotunnuksia, jotka on luotu turvallisilla satunnaislukugeneraattoreilla
- **Käyttäjäkohtainen sitominen**: Sido istuntotunnukset käyttäjäkohtaisiin tietoihin esimerkiksi muodossa `<user_id>:<session_id>` käyttäjienvälisen väärinkäytön estämiseksi
- **Istunnon elinkaaren hallinta**: Toteuta asianmukainen vanheneminen, kierto ja mitätöinti haavoittuvuusaikojen rajaamiseksi
- **Siirron suojaus**: Pakollinen HTTPS kaikessa tiedonsiirrossa estämään istuntotunnusten sieppausta

### Sekava apurin ongelma

**Sekava apuri -ongelma** esiintyy, kun MCP-palvelimet toimivat todennusproxyina asiakkaiden ja kolmansien osapuolten palveluiden välillä, mikä luo mahdollisuuksia valtuutuksen ohittamiseen staattisten asiakastunnusten hyväksikäytöllä.

#### **Hyökkäysmekaniikka & riskit**

- **Evästeperusteinen suostumuksen ohitus**: Aiempi käyttäjän todennus luo suostumusevästeitä, joita hyökkääjät hyödyntävät haitallisilla valtuutuspyynnöillä, joissa on muokatut uudelleenohjaus-URI:t
- **Valtuutuskoodin varastaminen**: Olemassa olevat suostumusevästeet voivat aiheuttaa valtuutuspalvelinten ohittavan suostumussivut ja ohjaavan koodit hyökkääjän hallinnoimiin päätepisteisiin  
- **Luvaton API-pääsy**: Varastetut valtuutuskoodit mahdollistavat token-vaihdon ja käyttäjän naamioitumisen ilman selkeää hyväksyntää

#### **Vähentämisstrategiat**

**Pakolliset toimenpiteet:**
- **Nimenomainen suostumusvaatimus**: MCP-proxy-palvelinten, jotka käyttävät staattisia asiakastunnuksia, **TÄYTYY** hankkia käyttäjältä suostumus jokaiselle dynaamisesti rekisteröidylle asiakkaalle
- **OAuth 2.1 turvallisuuden toteutus**: Noudata nykyisiä OAuth-turvallisuusparhaita käytäntöjä, mukaan lukien PKCE (Proof Key for Code Exchange) kaikissa valtuutuspyynnöissä
- **Tiukka asiakasvahvistus**: Toteuta tarkka uudelleenohjausURI:n ja asiakastunnusten validointi hyväksikäytön estämiseksi

### Token-läpikulkukohdat

**Token-läpikulkukohtaus** on selkeä anti-kuvio, jossa MCP-palvelimet hyväksyvät asiakastokenit ilman asianmukaista validointia ja edelleenlähettävät ne alasvirran API:lle rikkomalla MCP:n valtuutusmäärittelyt.

#### **Turvallisuusvaikutukset**

- **Kontrollin kierto**: Suora asiakas-api-tokenin käyttö ohittaa kriittiset määrärajoitukset, validoinnit ja valvontatoimet
- **Auditointilokin korruptio**: Ylösvirtauksessa annetut tokenit tekevät asiakkaan tunnistamisen mahdottomaksi, mikä estää tapahtumatutkinnat
- **Proxy-pohjainen datavuoto**: Validointia vailla olevat tokenit mahdollistavat palvelimien hyväksikäytön dataan luvattomaan pääsyyn
- **Luottamusrajan rikkominen**: Alasvirran palvelujen luotto-oletukset voivat rikkoontua, kun tokenin alkuperää ei voida varmistaa
- **Monipalveluhyökkäyksen laajeneminen**: Hyväksikäytetyt tokenit eri palveluissa mahdollistavat sivuttaisliikkeen

#### **Vaaditut turvatoimenpiteet**

**Ei-neuvoteltavat vaatimukset:**
- **Tokenien validointi**: MCP-palvelinten **EI SAA** hyväksyä tokenia, joita ei ole nimenomaisesti myönnetty kyseiselle MCP-palvelimelle
- **Kohdeyleisön tarkistus**: Varmista aina, että tokenin audience-vaatimus vastaa MCP-palvelimen identiteettiä
- **Oikea token-elinkaari**: Toteuta lyhytikäisiä pääsytokeneita turvallisin kiertokäytännöin


## Toimitusketjuturvallisuus tekoälyjärjestelmille

Toimitusketjuturvallisuus on kehittynyt perinteisten ohjelmistoriippuvuuksien ulkopuolelle kattaen koko tekoälyekosysteemin. Modernit MCP-toteutukset **täytyy** tarkistaa ja valvoa kaikki tekoälyyn liittyvät komponentit huolellisesti, sillä jokainen tuo mukanaan mahdollisia haavoittuvuuksia, jotka voivat vaarantaa järjestelmän eheyden.

### Laajennetut tekoälytoimitusketjun komponentit

**Perinteiset ohjelmistoriippuvuudet:**
- Avoimen lähdekoodin kirjastot ja kehykset
- Konttikuvat ja perusjärjestelmät  
- Kehitystyökalut ja rakennusputket
- Infrastruktuurin komponentit ja palvelut

**Tekoälyyn liittyvät toimitusketjuelementit:**
- **Perusmallit**: Esikoulutetut mallit useilta tarjoajilta, jotka vaativat alkuperän todentamista
- **Upotepalvelut**: Ulkoiset vektorioinnit ja semanttiset hakupalvelut
- **Kontekstin tarjoajat**: Tietolähteet, tietopohjat ja asiakirjakokoelmat  
- **Kolmannen osapuolen API:t**: Ulkoiset tekoälypalvelut, koneoppimisen putket ja datan käsittelypisteet
- **Mallin artefaktit**: Painot, konfiguraatiot ja hienosäädetyt malliversiot
- **Koulutusdatalähteet**: Datasetit, joita käytetään mallien koulutukseen ja hienosäätöön

### Kattava toimitusketjuturvallisuusstrategia

#### **Komponenttien varmennus & luottamus**
- **Alkuperän validointi**: Varmista kaikkien tekoälykomponenttien alkuperä, lisensointi ja eheys ennen integrointia
- **Turvallisuusarviointi**: Suorita haavoittuvuusskannaukset ja turvatarkastukset malleille, datalähteille ja tekoälypalveluille
- **Maineanalyysi**: Arvioi tekoälypalveluntarjoajien turvallisuushistoria ja käytännöt
- **Säädösten noudattaminen**: Varmista, että kaikki komponentit täyttävät organisaation turvallisuus- ja säädösvaatimukset

#### **Turvalliset käyttöönotto-putket**  
- **Automaattinen CI/CD-turvallisuus**: Integroidu turvallisuusskannaukset läpi automatisoitujen käyttöönotto-prosessien
- **Artefaktien eheys**: Toteuta kryptografinen varmennus kaikille käyttöönotetuille artefakteille (koodi, mallit, konfiguraatiot)
- **Vaiheittainen käyttöönotto**: Käytä progressiivisia käyttöönotto-strategioita, joissa turvallisuusvarmennus käyttäjä kussakin vaiheessa
- **Luotetut artefaktivarastot**: Käytä vain varmennettuja ja turvallisia artefaktivarastoja ja rekistereitä

#### **Jatkuva valvonta & reagointi**
- **Riippuvuusskannaus**: Jatkuva haavoittuvuusvalvonta kaikille ohjelmisto- ja tekoälykomponenttien riippuvuuksille
- **Mallin valvonta**: Jatkuva mallikäyttäytymisen, suorituskyvyn muutosten ja turvallisuuspoikkeamien seuranta
- **Palveluiden kunnon seuranta**: Seuraa ulkoisten tekoälypalveluiden saatavuutta, turvallisuusincidenttejä ja politiikkamuutoksia
- **Uhkatiedustelun integrointi**: Sisällytä tekoäly- ja koneoppimisen turvallisuusuhkiin liittyvät uhkatiedot

#### **Pääsynvalvonta & vähimmän etuoikeuden periaate**
- **Komponenttikohtaiset käyttöoikeudet**: Rajoita pääsy malleihin, dataan ja palveluihin liiketoiminnan tarpeen mukaisesti
- **Palvelutilien hallinta**: Toteuta dedikoidut palvelutilit, joilla on vain minimivaatimukset täyttävät käyttöoikeudet
- **Verkkosegmentointi**: Eristä tekoälykomponentit ja rajoita verkon pääsy palveluiden välillä
- **API-porttien valvonta**: Käytä keskitettyjä API-portteja ulkoisten tekoälypalvelujen käytön hallintaan ja valvontaan

#### **Häiriötilanteiden hallinta & palautus**
- **Nopeat reagointimenettelyt**: Vakiintuneet prosessit vaarantuneiden tekoälykomponenttien paikalleenpanoon tai vaihtoihin
- **Tunnistetietojen kierto**: Automaattiset järjestelmät salaisuuksien, API-avainten ja palvelutunnusten kiertoon
- **Palautuskyvyt**: Kyky palauttaa nopeasti aiemmin tunnetusti turvallisiin versioihin tekoälykomponenteista
- **Toimitusketjun rikkomuspalautus**: Erityiset menettelytavat ylövirran tekoälypalveluiden turvallisuusongelmien hallintaan

### Microsoftin turvallisuustyökalut & integraatiot

**GitHub Advanced Security** tarjoaa kokonaisvaltaisen toimitusketjusuojauksen, mukaan lukien:
- **Salaisuusskannaus**: Automaattinen tunnistus tunnuksista, API-avaimista ja tokeneista arkistoissa
- **Riippuvuusskannaus**: Haavoittuvuuksien arviointi avoimen lähdekoodin riippuvuuksissa ja kirjastoissa
- **CodeQL-analyysi**: Staattinen koodianalyysi turvallisuusheikkouksien ja koodausongelmien havaitsemiseen
- **Toimitusketjun näkymä**: Näkyvyys riippuvuuksien terveydestä ja turvallisuustilasta

**Azure DevOps & Azure Repos -integraatio:**
- Saumaton turvallisuusskannauksen integrointi Microsoftin kehitys alustoilla
- Automaattiset turvallisuustarkistukset Azure Pipelines -putkissa tekoälyniikoille
- Politiikkojen noudattaminen turvallisessa tekoälykomponenttien käyttöönotossa

**Microsoftin sisäiset käytännöt:**
Microsoft toteuttaa laajoja toimitusketjun turvallisuuskäytäntöjä kaikissa tuotteissaan. Tutustu toimiviin menetelmiin [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Perusturvallisuuden parhaat käytännöt

MCP-toteutukset perivät ja rakentavat organisaatiosi olemassa olevan turvallisuusaseman päälle. Perusturvakäytäntöjen vahvistaminen parantaa merkittävästi tekoälyjärjestelmien ja MCP-käyttöönottojen kokonaisvaltaista turvallisuutta.

### Turvallisuuden ydinelementit

#### **Turvallinen kehitys**
- **OWASP-yhteensopivuus**: Suojaa [OWASP Top 10](https://owasp.org/www-project-top-ten/) -verkkosovelluksen haavoittuvuuksilta
- **Tekoälykohtaiset suojaukset**: Toteuta kontrollit [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Turvallinen salaisuuksien hallinta**: Käytä omistettuja holveja tunnuksille, API-avaimille ja arkaluontoiselle konfiguraatiodatalle
- **End-to-end-salaus**: Toteuta turvallinen tiedonsiirto kaikissa sovelluksen komponenteissa ja datavirroissa
- **Syötteiden validointi**: Tarkka validointi kaikille käyttäjien syötteille, API-parametreille ja datalähteille

#### **Infrastruktuurin vahvistaminen**
- **Monivaiheinen todennus**: Pakollinen MFA kaikille hallinnollisille ja palvelutilille
- **Päivitysten hallinta**: Automaattinen ja ajantasainen korjausten levitys käyttöjärjestelmille, kehyksille ja riippuvuuksille  
- **Identiteetin tarjoajan integraatio**: Keskitetty identiteetin hallinta yrityksen identiteetin tarjoajien kautta (Microsoft Entra ID, Active Directory)
- **Verkkosegmentointi**: MCP-komponenttien looginen eristäminen sivuttaisliikkeen rajoittamiseksi
- **Vähimmän etuoikeuden periaate**: Kaikille järjestelmäkomponenteille ja tileille vain välttämättömät käyttöoikeudet

#### **Turvallisuuden valvonta & tunnistus**
- **Kattava lokitus**: Yksityiskohtainen lokitus tekoälysovelluksen toiminnoista, mukaan lukien MCP-asiakas-palvelin-vuorovaikutukset
- **SIEM-integraatio**: Keskitetty turvallisuustietojen ja tapahtumien hallinta poikkeamien tunnistamiseksi
- **Käyttäytymisanalytiikka**: AI-pohjainen valvonta epätavallisten järjestelmä- ja käyttäjäkäyttäytymisten havaitsemiseksi
- **Uhkatiedustelu**: Ulkoisten uhkatietolähteiden ja kompromissioindikaattoreiden (IOC) integrointi
- **Vastausprosessi**: Hyvin määritellyt menettelytavat turvallisuustapahtumien tunnistukseen, reagointiin ja toipumiseen

#### **Zero Trust -arkkitehtuuri**
- **Älä koskaan luota, vahvista aina**: Käyttäjien, laitteiden ja verkkoyhteyksien jatkuva vahvistus
- **Mikrosementointi**: Tarkat verkkokontrollit yksittäisten työkuormien ja palvelujen eristämiseen
- **Identiteettikeskeinen turvallisuus**: Turvallisuuspolitiikat perustuvat vahvistettuihin identiteetteihin verkon sijainnin sijaan
- **Jatkuva riskinarviointi**: Dynaaminen turvallisuusaseman arviointi nykyisen kontekstin ja käyttäytymisen perusteella
- **Ehdollinen pääsy**: Pääsynhallinta, joka mukautuu riskitekijöiden, sijainnin ja laitteen luottamuksen mukaan

### Yrityksen integraatiomallit

#### **Microsoftin turvallisuus-ekosysteemin integraatio**
- **Microsoft Defender for Cloud**: Kattava pilven turvallisuusaseman hallinta
- **Azure Sentinel**: Pilvipohjainen SIEM- ja SOAR-kyvykkyydet tekoälykuormien suojaamiseen
- **Microsoft Entra ID**: Yritysidentiteetin ja pääsynhallinta ehdollisin käyttöoikeuskäytännöin
- **Azure Key Vault**: Keskitetty salaisuuksien hallinta laitteistoturvaohjelmistoalustalla (HSM)
- **Microsoft Purview**: Datan hallinta ja säädösten noudattaminen tekoälytietolähteille ja työnkuluille

#### **Säädösten noudattaminen & hallinto**
- **Säädöstenmukaisuus**: Varmista, että MCP-toteutukset täyttävät toimialakohtaiset vaatimukset (GDPR, HIPAA, SOC 2)

- **Tietojen luokittelu**: Sensitiivisten tietojen asianmukainen luokittelu ja käsittely tekoälyjärjestelmissä
- **Tarkastuslokit**: Laaja lokitus sääntelyn noudattamisen ja rikostutkinnan tukemiseksi
- **Tietosuojakontrollit**: Tietosuoja-periaatteiden toteuttaminen tekoälyjärjestelmän arkkitehtuurissa
- **Muutosten hallinta**: Viralliset prosessit tekoälyjärjestelmän muutosten turvallisuustarkastuksiin

Nämä perustavat käytännöt luovat vahvan turvallisuusperustan, joka parantaa MCP-spesifisten turvakontrollien tehokkuutta ja tarjoaa kattavan suojan tekoälypohjaisille sovelluksille.

## Keskeiset turvallisuusopit

- **Kerrostettu turvallisuuslähestymistapa**: Yhdistä perusturvakäytännöt (turvallinen koodaus, vähimmän oikeuden periaate, toimitusketjun varmistaminen, jatkuva valvonta) tekoälyspesifisiin kontrolleihin kattavan suojan saavuttamiseksi

- **Tekoälyjärjestelmien uhkakenttä**: MCP-järjestelmät kohtaavat ainutlaatuisia riskejä kuten kehotteen injektointi, työkalujen myrkytys, istunnon kaappaus, epäselvät valtuutukset, tokenien läpivientihaavoittuvuudet ja liialliset oikeudet, jotka vaativat erityisiä lieventäviä toimia

- **Todennus- ja valtuutusosaaminen**: Toteuta vahva todennus ulkoisilla identiteetin tarjoajilla (Microsoft Entra ID), validoi tokenit oikein, äläkä koskaan hyväksy tokenia, joka ei ole eksplisiittisesti MCP-palvelimellesi annettu

- **Tekoälyhyökkäysten ehkäisy**: Ota käyttöön Microsoft Prompt Shields ja Azure Content Safety epäsuoria kehotteen injektointi- ja työkalumyrkytyshyökkäyksiä vastaan, validoi työkalujen metadata ja seuraa dynaamisia muutoksia

- **Istunnon ja tiedonsiirron turvallisuus**: Käytä kryptografisesti turvallisia, ei-deterministisiä istuntotunnuksia, jotka sidotaan käyttäjäidentiteetteihin, toteuta asianmukainen istunnon elinkaaren hallinta, äläkä koskaan käytä istuntoja todennukseen

- **OAuth-turvallisuuden parhaat käytännöt**: Estä epäselvät valtuutushyökkäykset eksplisiittisellä käyttäjäluvallisella dynaamisille rekisteröidyille asiakkaille, toteuta OAuth 2.1 PKCE:n kera, ja vaadi tiukka uudelleenohjaus-URI:n validointi  

- **Token-turvallisuusperiaatteet**: Vältä tokenien läpivienti-virhekuviota, validoi tokenien kohdevaatimukset, toteuta lyhytikäiset tokenit turvallisella kierrätyksellä ja ylläpidä selkeät luottamuksen rajat

- **Kattava toimitusketjun turvallisuus**: Kohtele kaikkia tekoälyekosysteemin komponentteja (mallit, upotukset, kontekstin tarjoajat, ulkoiset API:t) yhtä kurinalaisesti kuin perinteisiä ohjelmistoriippuvuuksia

- **Jatkuva kehittyminen**: Pysy ajan tasalla nopeasti kehittyvien MCP-spesifikaatioiden kanssa, osallistu turvayhteisön standardeihin ja ylläpidä mukautuvia turvallisuusasenteita protokollan kehittyessä

- **Microsoftin turvallisuusintegraatio**: Hyödynnä Microsoftin kattavaa turvallisuus-ekosysteemiä (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) MCP-jakelun suojaamisessa

## Kattavat resurssit

### **Virallinen MCP-turvallisuusdokumentaatio**
- [MCP-spesifikaatio (Nykyinen: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP:n parhaat turvallisuuskäytännöt](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP-valtuutuksen spesifikaatio](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub-repositorio](https://github.com/modelcontextprotocol)

### **OWASP MCP -turvallisuusresurssit**
- [OWASP MCP Azure turvallisuusopas](https://microsoft.github.io/mcp-azure-security-guide/) - Kattava OWASP MCP Top 10 azuren toteutusohjeineen
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Viralliset OWASP MCP turvallisuusriskit
- [MCP Security Summittyöpaja (Sherpa)](https://azure-samples.github.io/sherpa/) - Käytännön turvallisuuskoulutus MCP:lle Azurella

### **Turvastandardit ja parhaat käytännöt**
- [OAuth 2.0 turvallisuuden parhaat käytännöt (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 verkkosovellusten turvallisuus](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 suurille kielimalleille](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Tekoälyn turvallisuustutkimus ja analyysi**
- [Kehotteen injektio MCP:ssä (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Työkalujen myrkytyshyökkäykset (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP:n turvallisuustutkimusraportti (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoftin turvallisuusratkaisut**
- [Microsoft Prompt Shields -dokumentaatio](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety -palvelu](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID:n turvallisuus](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management parhaat käytännöt](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Toteutusoppaat ja opetusmateriaalit**
- [Azure API Management MCP:n todennusporttina](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID -todennus MCP-palvelimille](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Turvallinen tokenien tallennus ja salaus (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Toimitusketjun turvallisuus**
- [Azure DevOpsin turvallisuus](https://azure.microsoft.com/products/devops)
- [Azure Reposin turvallisuus](https://azure.microsoft.com/products/devops/repos/)
- [Microsoftin toimitusketjuturvallisuusmatka](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Lisäturvallisuusdokumentaatio**

Kattavaa turvallisuusohjeistusta varten tutustu tähän osioon kerättyihin erikoistuneisiin dokumentteihin:

- **[CIMD ja DCR -valtuutusesimerkki](./samples/cimd-dcr-auth/README.md)** - Suoritettava TypeScript MCP `2026-07-28` resurssipalvelin, joka vertaa suositeltuja Client ID Metadata -dokumentteja vanhentuneeseen Dynamic Client Registration -varamuotoon
- **[MCP:n parhaat turvallisuuskäytännöt](./mcp-security-best-practices.md)** - Täydelliset turvallisuuden parhaat käytännöt MCP-toteutuksille
- **[Azure Content Safety -toteutus](./azure-content-safety-implementation.md)** - Käytännön toteutusesimerkit Azure Content Safetyn integroimiseksi  
- **[MCP:n turvakontrollit](./mcp-security-controls.md)** - Viimeisimmät turvakontrollit ja tekniikat MCP-jakeluissa
- **[MCP:n parhaat käytännöt pikaopas](./mcp-best-practices.md)** - Tiivis opas tärkeimmistä MCP-turvallisuuskäytännöistä
- **[BlueHat 2026: Tekoälyn tulevaisuuden suojaaminen: Syvällinen MCP:n puolustusmallit](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Syvällisen puolustuksen mallit Microsoft Security Response Centeriltä (MSRC)

### **Käytännön turvallisuuskoulutus**

- **[MCP Security Summittyöpaja (Sherpa)](https://azure-samples.github.io/sherpa/)** - Kattava käytännön työpaja MCP-palvelinten suojaamiseen Azurella, jossa etenemäkoulutus Base Campista Summit-tasolle
- **[OWASP MCP Azure turvallisuusopas](https://microsoft.github.io/mcp-azure-security-guide/)** - Viitearkkitehtuuri ja toteutusohjeet kaikille OWASP MCP Top 10 riskeille

---

## Mitä seuraavaksi

Seuraava: [Luku 3: Aloittaminen](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->