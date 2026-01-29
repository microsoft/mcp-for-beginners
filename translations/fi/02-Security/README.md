# MCP-turvallisuus: Kattava suojaus tekoälyjärjestelmille

[![MCP Security Best Practices](../../../translated_images/fi/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Turvallisuus on tekoälyjärjestelmien suunnittelun perusta, minkä vuoksi se on prioriteettimme toisessa osiossa. Tämä noudattaa Microsoftin **Secure by Design** -periaatetta [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/) -ohjelmasta.

Model Context Protocol (MCP) tuo tekoälypohjaisiin sovelluksiin tehokkaita uusia ominaisuuksia, mutta samalla se tuo mukanaan ainutlaatuisia turvallisuushaasteita, jotka ylittävät perinteiset ohjelmistoriskit. MCP-järjestelmät kohtaavat sekä vakiintuneita turvallisuusuhkia (turvallinen koodaus, vähimmän oikeuden periaate, toimitusketjun turvallisuus) että uusia tekoälyyn liittyviä uhkia, kuten kehotteen injektointi, työkalujen myrkytys, istunnon kaappaus, sekaantunut edustaja -hyökkäykset, tunnisteiden läpivientihaavoittuvuudet ja dynaaminen kyvykkyyksien muokkaus.

Tässä oppitunnissa käsitellään tärkeimpiä turvallisuusriskejä MCP-toteutuksissa — mukaan lukien todennus, valtuutus, liialliset oikeudet, epäsuora kehotteen injektointi, istunnon turvallisuus, sekaantuneen edustajan ongelmat, tunnisteiden hallinta ja toimitusketjun haavoittuvuudet. Opit käytännön ohjaimia ja parhaita käytäntöjä näiden riskien lieventämiseksi hyödyntäen Microsoftin ratkaisuja kuten Prompt Shields, Azure Content Safety ja GitHub Advanced Security vahvistaaksesi MCP-käyttöönottoasi.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- **Tunnistaa MCP-kohtaiset uhat**: Tunnistaa MCP-järjestelmien ainutlaatuiset turvallisuusuhat, mukaan lukien kehotteen injektointi, työkalujen myrkytys, liialliset oikeudet, istunnon kaappaus, sekaantuneen edustajan ongelmat, tunnisteiden läpivientihaavoittuvuudet ja toimitusketjun riskit
- **Soveltaa turvallisuusohjaimia**: Toteuttaa tehokkaita lieventäviä toimia, kuten vahva todennus, vähimmän oikeuden pääsy, turvallinen tunnisteiden hallinta, istunnon turvallisuusohjaimet ja toimitusketjun varmennus
- **Hyödyntää Microsoftin turvallisuusratkaisuja**: Ymmärtää ja ottaa käyttöön Microsoft Prompt Shields, Azure Content Safety ja GitHub Advanced Security MCP-kuormituksen suojaamiseksi
- **Varmistaa työkalujen turvallisuus**: Tunnistaa työkalujen metatietojen validoinnin merkitys, dynaamisten muutosten valvonta ja puolustautuminen epäsuoria kehotteen injektointihyökkäyksiä vastaan
- **Yhdistää parhaat käytännöt**: Yhdistää vakiintuneet turvallisuuden perusteet (turvallinen koodaus, palvelimen koventaminen, zero trust) MCP-kohtaisiin ohjaimiin kattavan suojauksen saavuttamiseksi

# MCP-turvallisuusarkkitehtuuri ja ohjaimet

Nykyaikaiset MCP-toteutukset vaativat kerroksellisia turvallisuuslähestymistapoja, jotka käsittelevät sekä perinteistä ohjelmistoturvallisuutta että tekoälykohtaisia uhkia. Nopeasti kehittyvä MCP-määrittely jatkaa turvallisuusohjaimiensa kypsyttämistä, mahdollistaen paremman integraation yritysturvallisuusarkkitehtuureihin ja vakiintuneisiin parhaisiin käytäntöihin.

[Microsoft Digital Defense Report](https://aka.ms/mddr) -tutkimus osoittaa, että **98 % raportoituja tietomurtoja voitaisiin estää vahvalla turvallisuushygienialla**. Tehokkain suojausstrategia yhdistää perustavanlaatuiset turvallisuuskäytännöt MCP-kohtaisiin ohjaimiin — todistetut perusmittarit ovat edelleen merkittävin tekijä kokonaisriskin vähentämisessä.

## Nykyinen turvallisuusympäristö

> **Huom:** Tämä tieto heijastaa MCP-turvallisuusstandardeja tilassa **18. joulukuuta 2025**. MCP-protokolla kehittyy nopeasti, ja tulevat toteutukset voivat tuoda uusia todennusmalleja ja parannettuja ohjaimia. Viittaa aina ajantasaiseen [MCP-määrittelyyn](https://spec.modelcontextprotocol.io/), [MCP GitHub-repositorioon](https://github.com/modelcontextprotocol) ja [turvallisuuden parhaiden käytäntöjen dokumentaatioon](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) viimeisimmän ohjeistuksen saamiseksi.

### MCP-todennuksen kehitys

MCP-määrittely on kehittynyt merkittävästi todennuksen ja valtuutuksen lähestymistavoissa:

- **Alkuperäinen lähestymistapa**: Varhaisissa määrittelyissä kehittäjien tuli toteuttaa omat todennuspalvelimensa, ja MCP-palvelimet toimivat OAuth 2.0 -valtuutuspalvelimina, jotka hallinnoivat käyttäjien todennusta suoraan
- **Nykyinen standardi (2025-11-25)**: Päivitetty määrittely sallii MCP-palvelimien delegoida todennuksen ulkoisille identiteetin tarjoajille (kuten Microsoft Entra ID), parantaen turvallisuusasemaa ja vähentäen toteutuksen monimutkaisuutta
- **Kuljetuskerroksen turvallisuus**: Parannettu tuki turvallisille siirtomekanismeille asianmukaisilla todennusmalleilla sekä paikallisissa (STDIO) että etäyhteyksissä (Streamable HTTP)

## Todennus- ja valtuutusturvallisuus

### Nykyiset turvallisuushaasteet

Nykyaikaiset MCP-toteutukset kohtaavat useita todennus- ja valtuutushaasteita:

### Riskit ja uhkavektorit

- **Väärin konfiguroitu valtuutuslogiikka**: Virheellinen valtuutuksen toteutus MCP-palvelimissa voi paljastaa arkaluonteisia tietoja ja soveltaa väärin pääsynvalvontaa
- **OAuth-tunnisteen vaarantuminen**: Paikallisen MCP-palvelimen tunnisteen varastaminen mahdollistaa hyökkääjien esiintymisen palvelimena ja pääsyn alaspäin suuntautuville palveluille
- **Tunnisteiden läpivientihaavoittuvuudet**: Virheellinen tunnisteiden käsittely luo turvallisuusohjainten ohituksia ja vastuullisuusaukkoja
- **Liialliset oikeudet**: Ylivaltuutetut MCP-palvelimet rikkovat vähimmän oikeuden periaatetta ja laajentavat hyökkäyspintaa

#### Tunnisteiden läpivienti: kriittinen anti-malli

**Tunnisteiden läpivienti on nimenomaisesti kielletty** nykyisessä MCP-valtuutusmäärittelyssä vakavien turvallisuusvaikutusten vuoksi:

##### Turvallisuusohjainten kiertäminen
- MCP-palvelimet ja alaspäin suuntautuvat API:t toteuttavat kriittisiä turvallisuusohjaimia (kyselyrajoitus, pyyntöjen validointi, liikenteen valvonta), jotka perustuvat asianmukaiseen tunnisteiden validointiin
- Suora asiakas-API-tunnisteiden käyttö ohittaa nämä olennaiset suojaukset, heikentäen turvallisuusarkkitehtuuria

##### Vastuullisuus- ja auditointiongelmat  
- MCP-palvelimet eivät pysty erottamaan asiakkaita, jotka käyttävät ylävirran myöntämiä tunnisteita, mikä rikkoo auditointiketjuja
- Alaspäin suuntautuvien resurssipalvelimien lokit näyttävät harhaanjohtavia pyyntöjen alkuperäisiä MCP-palvelimen välittäjien sijaan
- Tapaustutkinta ja vaatimustenmukaisuuden auditointi vaikeutuvat merkittävästi

##### Tietovuotoriskit
- Vahvistamattomat tunnisteväitteet mahdollistavat pahantahtoisten toimijoiden käyttää varastettuja tunnisteita MCP-palvelimien välityspalvelimina tietojen vuotamiseen
- Luottamusrakenteiden rikkomukset sallivat luvattomia pääsykuvioita, jotka ohittavat suunnitellut turvallisuusohjaimet

##### Monipalveluhyökkäysvektorit
- Vaarantuneet tunnisteet, joita hyväksytään useissa palveluissa, mahdollistavat sivuttaisen liikkumisen yhdistettyjen järjestelmien välillä
- Luottamuspalveluiden väliset oletukset voivat rikkoutua, kun tunnisteiden alkuperää ei voida varmistaa

### Turvallisuusohjaimet ja lieventämistoimet

**Kriittiset turvallisuusvaatimukset:**

> **VELVOITTAVA**: MCP-palvelimet **EIVÄT SAA** hyväksyä tunnisteita, joita ei nimenomaisesti ole myönnetty kyseiselle MCP-palvelimelle

#### Todennus- ja valtuutusohjaimet

- **Tiukka valtuutuksen tarkastus**: Suorita kattavat auditoinnit MCP-palvelimen valtuutuslogiikasta varmistaaksesi, että vain tarkoitetut käyttäjät ja asiakkaat pääsevät arkaluonteisiin resursseihin
  - **Toteutusopas**: [Azure API Management todennusporttina MCP-palvelimille](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identiteetin integrointi**: [Microsoft Entra ID:n käyttö MCP-palvelimen todennuksessa](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Turvallinen tunnisteiden hallinta**: Toteuta [Microsoftin tunnisteiden validointi- ja elinkaaren parhaat käytännöt](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Varmista, että tunnisteen vastaanottajaväitteet vastaavat MCP-palvelimen identiteettiä
  - Toteuta asianmukaiset tunnisteiden kierto- ja vanhenemiskäytännöt
  - Estä tunnisteiden uudelleenkäyttöhyökkäykset ja luvaton käyttö

- **Suojaus tunnisteiden tallennuksessa**: Salaa tunnisteet sekä levossa että siirrossa
  - **Parhaat käytännöt**: [Turvallinen tunnisteiden tallennus ja salausohjeet](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Pääsynvalvonnan toteutus

- **Vähimmän oikeuden periaate**: Myönnä MCP-palvelimille vain vähimmäisoikeudet, jotka ovat tarpeen suunnitellulle toiminnallisuudelle
  - Säännölliset oikeuksien tarkastukset ja päivitykset etuoikeuksien kasvun estämiseksi
  - **Microsoftin dokumentaatio**: [Turvallinen vähimmän oikeuden pääsy](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Roolipohjainen pääsynvalvonta (RBAC)**: Toteuta hienojakoiset roolijakoasetukset
  - Rajaa roolit tiukasti tiettyihin resursseihin ja toimiin
  - Vältä laajoja tai tarpeettomia oikeuksia, jotka laajentavat hyökkäyspintaa

- **Jatkuva oikeuksien valvonta**: Toteuta jatkuva pääsyn auditointi ja valvonta
  - Seuraa oikeuksien käyttökuvioita poikkeamien varalta
  - Korjaa nopeasti liialliset tai käyttämättömät oikeudet

## Tekoälykohtaiset turvallisuusuhat

### Kehotteen injektointi ja työkalujen manipulointihyökkäykset

Nykyaikaiset MCP-toteutukset kohtaavat kehittyneitä tekoälykohtaisia hyökkäysvektoreita, joita perinteiset turvallisuustoimet eivät täysin kata:

#### **Epäsuora kehotteen injektointi (Cross-Domain Prompt Injection)**

**Epäsuora kehotteen injektointi** on yksi kriittisimmistä haavoittuvuuksista MCP-kykyisissä tekoälyjärjestelmissä. Hyökkääjät upottavat haitallisia ohjeita ulkoiseen sisältöön — asiakirjoihin, verkkosivuihin, sähköposteihin tai tietolähteisiin — joita tekoälyjärjestelmät käsittelevät myöhemmin laillisina käskyinä.

**Hyökkäysskenaariot:**
- **Asiakirjapohjainen injektio**: Haitalliset ohjeet piilotettuina käsiteltäviin asiakirjoihin, jotka laukaisevat ei-toivottuja tekoälytoimia
- **Verkkosisällön hyväksikäyttö**: Kaapattuja verkkosivuja, jotka sisältävät upotettuja kehotteita, jotka manipuloivat tekoälyn käyttäytymistä kun ne indeksoidaan
- **Sähköpostipohjaiset hyökkäykset**: Haitalliset kehotteet sähköposteissa, jotka saavat tekoälyavustajat vuotamaan tietoja tai suorittamaan luvattomia toimia
- **Tietolähteiden saastuttaminen**: Kaapattuja tietokantoja tai API:ita, jotka tarjoavat saastunutta sisältöä tekoälyjärjestelmille

**Todellinen vaikutus**: Nämä hyökkäykset voivat johtaa tietovuotoihin, yksityisyyden loukkauksiin, haitallisen sisällön tuottamiseen ja käyttäjävuorovaikutusten manipulointiin. Tarkempaan analyysiin katso [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/fi/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Työkalujen myrkytyshyökkäykset**

**Työkalujen myrkytys** kohdistuu MCP-työkalujen metatietoihin, hyväksikäyttäen sitä, miten LLM-mallit tulkitsevat työkalujen kuvauksia ja parametreja tehdäkseen suorituspäätöksiä.

**Hyökkäysmekanismit:**
- **Metatietojen manipulointi**: Hyökkääjät injektoivat haitallisia ohjeita työkalujen kuvauksiin, parametrien määritelmiin tai käyttöesimerkkeihin
- **Näkymättömät ohjeet**: Piilotetut kehotteet työkalujen metatiedoissa, joita tekoälymallit käsittelevät mutta ihmiset eivät näe
- **Dynaaminen työkalumuokkaus ("Rug Pulls")**: Käyttäjien hyväksymät työkalut muokataan myöhemmin suorittamaan haitallisia toimia ilman käyttäjän tietoa
- **Parametrien injektointi**: Haitallinen sisältö upotettuna työkalujen parametrien skeemoihin, jotka vaikuttavat mallin käyttäytymiseen

**Isännöidyn palvelimen riskit**: Etä-MCP-palvelimet ovat erityisen riskialttiita, koska työkalumäärittelyjä voidaan päivittää käyttäjän alkuperäisen hyväksynnän jälkeen, mikä luo tilanteita, joissa aiemmin turvalliset työkalut muuttuvat haitallisiksi. Kattavaan analyysiin katso [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/fi/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Lisää tekoälyhyökkäysvektoreita**

- **Cross-Domain Prompt Injection (XPIA)**: Kehittyneet hyökkäykset, jotka hyödyntävät sisältöä useilta eri alueilta ohittaakseen turvallisuusohjaimet
- **Dynaaminen kyvykkyyksien muokkaus**: Työkalujen kyvykkyyksien reaaliaikaiset muutokset, jotka välttävät alkuperäiset turvallisuusarviot
- **Kontekstin ikkunan myrkytys**: Hyökkäykset, jotka manipuloivat suuria kontekstin ikkunoita piilottaakseen haitallisia ohjeita
- **Mallin sekaannushyökkäykset**: Mallin rajoitusten hyväksikäyttö ennakoimattomien tai turvattomien käyttäytymisten luomiseksi

### Tekoälyn turvallisuusriskien vaikutukset

**Korkean vaikutuksen seuraukset:**
- **Tietovuodot**: Luvaton pääsy ja arkaluonteisten yritys- tai henkilötietojen varastaminen
- **Yksityisyyden loukkaukset**: Henkilötietojen (PII) ja luottamuksellisten liiketoimintatietojen paljastuminen  
- **Järjestelmien manipulointi**: Ei-toivotut muutokset kriittisiin järjestelmiin ja työnkulkuihin
- **Tunnistetietojen varastaminen**: Todennustunnisteiden ja palvelutunnusten vaarantuminen
- **Sivuttaisliike**: Vaarantuneiden tekoälyjärjestelmien käyttö laajempien verkkojen hyökkäysten pivot-pisteinä

### Microsoftin tekoälytietoturvaratkaisut

#### **AI Prompt Shields: Edistynyt suojaus injektointihyökkäyksiä vastaan**

Microsoftin **AI Prompt Shields** tarjoavat kattavan suojan sekä suorilta että epäsuorilta kehotteen injektointihyökkäyksiltä monikerroksisten turvallisuusmekanismien avulla:

##### **Keskeiset suojausmekanismit:**

1. **Edistynyt havaitseminen ja suodatus**
   - Koneoppimisalgoritmit ja NLP-tekniikat tunnistavat haitalliset ohjeet ulkoisessa sisällössä
   - Reaaliaikainen analyysi asiakirjoista, verkkosivuista, sähköposteista ja tietolähteistä upotettujen uhkien varalta
   - Kontekstuaalinen ymmärrys laillisista vs. haitallisista kehotemalleista

2. **Korostustekniikat**  
   - Erottaa luotetut järjestelmäohjeet ja mahdollisesti vaarantuneet ulkoiset syötteet
   - Tekstin muunnosmenetelmät, jotka parantavat mallin relevanssia samalla eristäen haitallisen sisällön
   - Auttaa tekoälyjärjestelmiä ylläpitämään oikeaa ohjehierarkiaa ja ohittamaan injektoidut käskyt

3. **Erotin- ja datamerkintäjärjestelmät**
   - Selkeä rajaus luotettujen järjestelmäviestien ja ulkoisen syötteen tekstin välillä
   - Erityiset merkit korostavat rajapintoja luotettujen ja epäluotettujen tietolähteiden välillä
   - Selkeä erottelu estää ohjeiden sekoittumisen ja luvattoman käskyjen suorittamisen

4. **Jatkuva uhkatiedustelu**
   - Microsoft valvoo jatkuvasti nousevia hyökkäysmalleja ja päivittää puolustuksia
   - Proaktiivinen uhkien metsästys uusille injektointitekniikoille ja hyökkäysvektoreille
   - Säännölliset turvallisuusmallipäivitykset tehokkuuden ylläpitämiseksi kehittyviä uhkia vastaan

5. **Azure Content Safety -integraatio**
   - Osa kattavaa Azure AI Content Safety -kokonaisuutta
   - Lisähavaintoja jailbreak-yrityksistä, haitallisesta sisällöstä ja turvallisuuspolitiikan rikkomuksista
   - Yhtenäiset turvallisuusohjaimet tekoälysovellusten komponenteille

**Toteutusresurssit**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/fi/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Edistyneet MCP-turvallisuusuhat

### Istunnon kaappaushaavoittuvuudet

**Istunnon kaappaus** on kriittinen hyökkäysvektori tilallisten MCP-toteutusten yhteydessä, joissa luvattomat osapuolet saavat haltuunsa ja väärinkäyttävät laillisia istunnon tunnisteita esiintyäkseen asiakkaina ja suorittaakseen luvattomia toimia.

#### **Hyökkäysskenaariot ja riskit**

- **Istunnon kaappaus kehotteen injektoinnilla**: Hyökkääjät, joilla on varastetut istunnon tunnisteet, injektoivat haitallisia tapahtumia palvelimille, jotka jakavat istuntotilan, mahdollisesti laukaisten haitallisia toimintoja tai pääsyn arkaluonteisiin tietoihin
- **Suora esiintyminen**: Varastetut istunnon tunnisteet mahdollistavat suorat MCP-palvelinkutsut, jotka ohittavat todennuksen ja käsittelevät hyökkääjiä laillisina käyttäjinä
- **Vaarantuneet jatkettavat virtaukset**: Hyökkääjät voivat keskeyttää pyynnöt ennenaikaisesti, aiheuttaen laillisten asiakkaiden jatkavan mahdollisesti haitallisen sisällön kanssa

#### **Istunnon hallinnan turvallisuusohjaimet**

**Kriittiset vaatimukset:**
- **Valtuutuksen vahvistus**: MCP-palvelimien, jotka toteuttavat valtuutusta, **TÄYTYY** tarkistaa KAIKKI saapuvat pyynnöt, eikä niiden **TULE** luottaa istuntoihin todennuksessa
- **Turvallinen istunnon luonti**: Käytä kryptografisesti turvallisia, ei-deterministisiä istunto-ID:itä, jotka on luotu turvallisilla satunnaislukugeneraattoreilla
- **Käyttäjäkohtainen sidonta**: Sido istunto-ID:t käyttäjäkohtaisiin tietoihin käyttämällä muotoja kuten `<user_id>:<session_id>`, jotta estetään istuntojen väärinkäyttö eri käyttäjien välillä
- **Istunnon elinkaaren hallinta**: Toteuta asianmukainen vanhentuminen, kierto ja mitätöinti haavoittuvuusaikojen rajoittamiseksi
- **Siirtoturvallisuus**: Pakollinen HTTPS kaikessa viestinnässä istunto-ID:n sieppauksen estämiseksi

### Sekava edustaja -ongelma

**Sekava edustaja -ongelma** ilmenee, kun MCP-palvelimet toimivat todennusvälittäjinä asiakkaiden ja kolmansien osapuolten palveluiden välillä, mikä luo mahdollisuuksia valtuutuksen ohittamiseen staattisten asiakastunnusten hyväksikäytön kautta.

#### **Hyökkäysmekaniikka & riskit**

- **Evästeisiin perustuva suostumuksen ohitus**: Aiempi käyttäjän todennus luo suostumusevästeitä, joita hyökkääjät käyttävät hyväkseen haitallisten valtuutuspyyntöjen avulla, joissa on muokatut uudelleenohjaus-URI:t
- **Valtuutuskoodin varastaminen**: Olemassa olevat suostumusevästeet voivat saada valtuutuspalvelimet ohittamaan suostumusnäytöt ja ohjaamaan koodit hyökkääjän hallinnoimiin päätepisteisiin  
- **Luvaton API-käyttö**: Varastetut valtuutuskoodit mahdollistavat tokenin vaihdon ja käyttäjän esiintymisen ilman nimenomaista hyväksyntää

#### **Vähennysstrategiat**

**Pakolliset kontrollit:**
- **Nimenomaiset suostumusvaatimukset**: MCP-välityspalvelimien, jotka käyttävät staattisia asiakastunnuksia, **TÄYTYY** saada käyttäjän suostumus jokaiselle dynaamisesti rekisteröidylle asiakkaalle
- **OAuth 2.1 -turvallisuuden toteutus**: Noudata nykyisiä OAuth-turvallisuuskäytäntöjä, mukaan lukien PKCE (Proof Key for Code Exchange) kaikissa valtuutuspyynnöissä
- **Tiukka asiakasvalidointi**: Toteuta tiukka uudelleenohjaus-URI:en ja asiakastunnisteiden validointi hyväksikäytön estämiseksi

### Tokenin läpivientiin liittyvät haavoittuvuudet  

**Tokenin läpivienti** on selkeä anti-kuvio, jossa MCP-palvelimet hyväksyvät asiakastokenit ilman asianmukaista validointia ja välittävät ne eteenpäin alaspäin meneville API:lle, mikä rikkoo MCP:n valtuutusmäärittelyjä.

#### **Turvallisuusvaikutukset**

- **Kontrollien kiertäminen**: Suora asiakas-API-tokenin käyttö ohittaa kriittiset nopeusrajoitukset, validoinnit ja valvontakontrollit
- **Tarkastuspolun korruptio**: Ylätason myöntämät tokenit tekevät asiakkaan tunnistamisesta mahdotonta, mikä estää tapaustutkinnan
- **Välityspalvelinperäinen tiedon vuoto**: Vahvistamattomat tokenit mahdollistavat palvelimien käytön välityspalvelimina luvattomaan tiedon käyttöön
- **Luottamuksen rajojen rikkominen**: Alaspäin menevien palveluiden luottamusolettamat voivat rikkoutua, kun tokenin alkuperää ei voida varmistaa
- **Monipalveluhyökkäysten laajentuminen**: Hyväksytyt vaarantuneet tokenit useissa palveluissa mahdollistavat sivuttaisliikkeen

#### **Vaaditut turvallisuuskontrollit**

**Neuvottelemattomat vaatimukset:**
- **Tokenin validointi**: MCP-palvelimet **EIVÄT SAA** hyväksyä tokeneita, joita ei ole nimenomaisesti myönnetty MCP-palvelimelle
- **Kohdeyleisön tarkistus**: Varmista aina, että tokenin kohdeyleisövaatimukset vastaavat MCP-palvelimen identiteettiä
- **Asianmukainen tokenin elinkaari**: Toteuta lyhytikäiset käyttöoikeustokenit turvallisilla kiertokäytännöillä


## Toimitusketjun turvallisuus tekoälyjärjestelmissä

Toimitusketjun turvallisuus on kehittynyt perinteisistä ohjelmistoriippuvuuksista kattamaan koko tekoälyekosysteemin. Nykyaikaisten MCP-toteutusten on tarkasti varmistettava ja valvottava kaikkia tekoälyyn liittyviä komponentteja, sillä jokainen niistä voi tuoda haavoittuvuuksia, jotka vaarantavat järjestelmän eheyden.

### Laajennetut tekoälyn toimitusketjun komponentit

**Perinteiset ohjelmistoriippuvuudet:**
- Avoimen lähdekoodin kirjastot ja kehykset
- Konttikuvat ja perusjärjestelmät  
- Kehitystyökalut ja rakennusputket
- Infrastruktuurikomponentit ja palvelut

**Tekoälykohtaiset toimitusketjun elementit:**
- **Perusmallit**: Eri tarjoajilta saadut esikoulutetut mallit, joiden alkuperä on varmistettava
- **Upotuspalvelut**: Ulkoiset vektorisointi- ja semanttisen haun palvelut
- **Kontekstin tarjoajat**: Tietolähteet, tietopankit ja asiakirjavarastot  
- **Kolmannen osapuolen API:t**: Ulkoiset tekoälypalvelut, ML-putket ja datankäsittelypäätepisteet
- **Mallin artefaktit**: Painot, konfiguraatiot ja hienosäädetyt mallivariantit
- **Koulutusdatat**: Mallin koulutuksessa ja hienosäädössä käytetyt aineistot

### Kattava toimitusketjun turvallisuusstrategia

#### **Komponenttien varmistus & luottamus**
- **Alkuperän validointi**: Varmista kaikkien tekoälykomponenttien alkuperä, lisenssit ja eheys ennen integrointia
- **Turvallisuusarviointi**: Suorita haavoittuvuusskannaukset ja turvallisuustarkastukset malleille, tietolähteille ja tekoälypalveluille
- **Maineanalyysi**: Arvioi tekoälypalveluntarjoajien turvallisuushistoria ja käytännöt
- **Säädösten noudattaminen**: Varmista, että kaikki komponentit täyttävät organisaation turvallisuus- ja sääntelyvaatimukset

#### **Turvalliset käyttöönotto-putket**  
- **Automaattinen CI/CD-turvallisuus**: Integroi turvallisuusskannaukset automatisoituihin käyttöönotto-putkiin
- **Artefaktien eheys**: Toteuta kryptografinen varmennus kaikille käyttöön otetuille artefakteille (koodi, mallit, konfiguraatiot)
- **Vaiheittainen käyttöönotto**: Käytä asteittaisia käyttöönotto-strategioita turvallisuusvalidoinnilla jokaisessa vaiheessa
- **Luotetut artefaktivarastot**: Ota käyttöön vain varmennetuista, turvallisista artefaktirekistereistä ja -varastoista

#### **Jatkuva valvonta & reagointi**
- **Riippuvuusskannaus**: Jatkuva haavoittuvuuksien seuranta kaikille ohjelmisto- ja tekoälykomponenttien riippuvuuksille
- **Mallin valvonta**: Jatkuva arviointi mallin käyttäytymisestä, suorituskyvyn muutoksista ja turvallisuuspoikkeamista
- **Palvelun tilan seuranta**: Valvo ulkoisia tekoälypalveluita saatavuuden, turvallisuuspoikkeamien ja politiikkamuutosten osalta
- **Uhkatiedon integrointi**: Sisällytä tekoälyyn ja koneoppimisen turvallisuusriskeihin liittyvät uhkatiedot

#### **Pääsynhallinta & vähimmän oikeuden periaate**
- **Komponenttikohtaiset käyttöoikeudet**: Rajoita pääsy malleihin, dataan ja palveluihin liiketoiminnan tarpeen mukaan
- **Palvelutilien hallinta**: Toteuta omistetut palvelutilit, joilla on vain välttämättömät oikeudet
- **Verkkosegmentointi**: Eristä tekoälykomponentit ja rajoita verkkoyhteydet palveluiden välillä
- **API-porttien kontrollit**: Käytä keskitettyjä API-portteja ulkoisten tekoälypalveluiden pääsyn hallintaan ja valvontaan

#### **Häiriötilanteisiin reagointi & palautuminen**
- **Nopeat reagointimenettelyt**: Vakiintuneet prosessit vaarantuneiden tekoälykomponenttien korjaamiseen tai vaihtamiseen
- **Tunnistetietojen kierto**: Automaattiset järjestelmät salaisuuksien, API-avainten ja palvelutunnusten kiertoon
- **Palautusmahdollisuudet**: Kyky nopeasti palauttaa aiemmat tunnetusti toimivat versiot tekoälykomponenteista
- **Toimitusketjun rikkomusten palautuminen**: Erityiset menettelyt ylätason tekoälypalveluiden vaarantumisiin reagointiin

### Microsoftin turvallisuustyökalut & integraatio

**GitHub Advanced Security** tarjoaa kattavan toimitusketjun suojauksen, mukaan lukien:
- **Salaisuuksien skannaus**: Automaattinen tunnistus tunnuksista, API-avaimista ja tokeneista repositorioissa
- **Riippuvuusskannaus**: Haavoittuvuuksien arviointi avoimen lähdekoodin riippuvuuksille ja kirjastoille
- **CodeQL-analyysi**: Staattinen koodianalyysi turvallisuuspuutteiden ja koodausongelmien löytämiseksi
- **Toimitusketjun näkymät**: Näkyvyys riippuvuuksien terveydestä ja turvallisuustilasta

**Azure DevOps & Azure Repos -integraatio:**
- Saumaton turvallisuusskannaus Microsoftin kehitysalustoilla
- Automaattiset turvallisuustarkistukset Azure Pipelinesissa tekoälykuormille
- Politiikkojen valvonta turvalliselle tekoälykomponenttien käyttöönotolle

**Microsoftin sisäiset käytännöt:**
Microsoft toteuttaa laajoja toimitusketjun turvallisuuskäytäntöjä kaikissa tuotteissaan. Tutustu todistettuihin lähestymistapoihin [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Perusturvallisuuden parhaat käytännöt

MCP-toteutukset perivät ja rakentavat organisaatiosi olemassa olevan turvallisuusaseman päälle. Perusturvallisuuskäytäntöjen vahvistaminen parantaa merkittävästi tekoälyjärjestelmien ja MCP-käyttöönottojen kokonaisvaltaista turvallisuutta.

### Keskeiset turvallisuuden perusteet

#### **Turvalliset kehityskäytännöt**
- **OWASP-vaatimustenmukaisuus**: Suojaa [OWASP Top 10](https://owasp.org/www-project-top-ten/) -verkkosovellusten haavoittuvuuksilta
- **Tekoälykohtaiset suojaukset**: Toteuta kontrollit [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) -listan mukaisesti
- **Turvallinen salaisuuksien hallinta**: Käytä omistettuja holveja tokeneille, API-avaimille ja arkaluonteisille konfiguraatiotiedoille
- **Päätepisteiden välinen salaus**: Toteuta turvallinen viestintä kaikissa sovelluskomponenteissa ja datavirroissa
- **Syötteen validointi**: Tiukka validointi kaikille käyttäjän syötteille, API-parametreille ja tietolähteille

#### **Infrastruktuurin koventaminen**
- **Monivaiheinen tunnistautuminen**: Pakollinen MFA kaikille hallinnollisille ja palvelutilille
- **Päivitysten hallinta**: Automaattinen ja ajantasainen korjausten hallinta käyttöjärjestelmille, kehyksille ja riippuvuuksille  
- **Identiteetin tarjoajan integrointi**: Keskitetty identiteetinhallinta yrityksen identiteetin tarjoajien (Microsoft Entra ID, Active Directory) kautta
- **Verkkosegmentointi**: MCP-komponenttien looginen eristäminen sivuttaisliikkeen rajoittamiseksi
- **Vähimmän oikeuden periaate**: Vain välttämättömät oikeudet kaikille järjestelmäkomponenteille ja tileille

#### **Turvallisuuden valvonta & havaitseminen**
- **Kattava lokitus**: Yksityiskohtainen lokitus tekoälysovellusten toiminnoista, mukaan lukien MCP-asiakas-palvelin-vuorovaikutukset
- **SIEM-integraatio**: Keskitetty turvallisuustiedon ja tapahtumien hallinta poikkeamien havaitsemiseksi
- **Käyttäytymisanalytiikka**: Tekoälypohjainen valvonta epätavallisten järjestelmä- ja käyttäjäkäyttäytymismallien tunnistamiseksi
- **Uhkatiedon hyödyntäminen**: Ulkoisten uhkatietovirtojen ja kompromissin indikaattoreiden (IOC) integrointi
- **Häiriötilanteisiin reagointi**: Hyvin määritellyt menettelyt turvallisuuspoikkeamien havaitsemiseen, reagointiin ja palautumiseen

#### **Zero Trust -arkkitehtuuri**
- **Älä koskaan luota, varmista aina**: Jatkuva käyttäjien, laitteiden ja verkkoyhteyksien varmistaminen
- **Mikrosegmentointi**: Tarkat verkkokontrollit, jotka eristävät yksittäiset työkuormat ja palvelut
- **Identiteettikeskeinen turvallisuus**: Turvapolitiikat perustuvat varmennettuihin identiteetteihin verkkoalueen sijaan
- **Jatkuva riskinarviointi**: Dynaaminen turvallisuusaseman arviointi nykyisen kontekstin ja käyttäytymisen perusteella
- **Ehdollinen pääsy**: Pääsynhallinta, joka mukautuu riskitekijöiden, sijainnin ja laitteen luotettavuuden mukaan

### Yritysintegrointimallit

#### **Microsoftin turvallisuus-ekosysteemin integraatio**
- **Microsoft Defender for Cloud**: Kattava pilven turvallisuusaseman hallinta
- **Azure Sentinel**: Pilvipohjainen SIEM- ja SOAR-ratkaisu tekoälykuormien suojaamiseen
- **Microsoft Entra ID**: Yritystason identiteetin ja pääsynhallinta ehdollisilla pääsypolitiikoilla
- **Azure Key Vault**: Keskitetty salaisuuksien hallinta laitteistoturvallisuusmoduulilla (HSM)
- **Microsoft Purview**: Tiedonhallinta ja säädösten noudattaminen tekoälydatalähteille ja työnkuluissa

#### **Säädösten noudattaminen & hallinto**
- **Sääntelyn mukaisuus**: Varmista, että MCP-toteutukset täyttävät toimialakohtaiset vaatimukset (GDPR, HIPAA, SOC 2)
- **Datan luokittelu**: Arkaluonteisen datan asianmukainen luokittelu ja käsittely tekoälyjärjestelmissä
- **Tarkastuspolut**: Kattava lokitus sääntelyn noudattamiseksi ja oikeuslääketieteelliseen tutkimukseen
- **Tietosuojakontrollit**: Tietosuojan sisällyttäminen suunnitteluvaiheessa tekoälyjärjestelmän arkkitehtuuriin
- **Muutoshallinta**: Viralliset prosessit tekoälyjärjestelmän muutosten turvallisuustarkastuksille

Nämä perustavat käytännöt luovat vahvan turvallisuusperustan, joka parantaa MCP-spesifisten turvallisuuskontrollien tehokkuutta ja tarjoaa kattavan suojan tekoälypohjaisille sovelluksille.

## Keskeiset turvallisuusopit

- **Kerrostettu turvallisuuslähestymistapa**: Yhdistä perusturvallisuuskäytännöt (turvallinen koodaus, vähimmän oikeuden periaate, toimitusketjun varmistus, jatkuva valvonta) tekoälykohtaisiin kontrollitoimiin kattavan suojan saavuttamiseksi

- **Tekoälykohtainen uhkakenttä**: MCP-järjestelmät kohtaavat ainutlaatuisia riskejä, kuten kehotteen injektointi, työkalujen myrkytys, istunnon kaappaus, sekava edustaja -ongelmat, tokenin läpivientiin liittyvät haavoittuvuudet ja liialliset käyttöoikeudet, jotka vaativat erikoistuneita lieventäviä toimia

- **Todennus- ja valtuutusosaaminen**: Toteuta vahva todennus ulkoisten identiteetin tarjoajien (Microsoft Entra ID) avulla, pakota asianmukainen tokenin validointi, äläkä koskaan hyväksy tokeneita, joita ei ole nimenomaisesti myönnetty MCP-palvelimellesi

- **Tekoälyhyökkäysten ehkäisy**: Ota käyttöön Microsoft Prompt Shields ja Azure Content Safety epäsuorien kehotteen injektointi- ja työkalujen myrkytyshyökkäysten torjumiseksi, validoi työkalujen metatiedot ja valvo dynaamisia muutoksia

- **Istunto- ja siirtoturvallisuus**: Käytä kryptografisesti turvallisia, ei-deterministisiä istunto-ID:itä, jotka on sidottu käyttäjäidentiteetteihin, toteuta asianmukainen istunnon elinkaaren hallinta, äläkä koskaan käytä istuntoja todennukseen

- **OAuth-turvallisuuden parhaat käytännöt**: Estä sekavan edustajan hyökkäykset nimenomaisella käyttäjän suostumuksella dynaamisesti rekisteröidyille asiakkaille, asianmukaisella OAuth 2.1 -toteutuksella PKCE:llä ja tiukalla uudelleenohjaus-URI:n validoinnilla  

- **Token-turvallisuuden periaatteet**: Vältä tokenin läpivientiin liittyviä anti-kuvioita, validoi tokenin kohdeyleisövaatimukset, toteuta lyhytikäiset tokenit turvallisella kiertolla ja ylläpidä selkeät luottamusrajat

- **Kattava toimitusketjun turvallisuus**: Kohtele kaikkia tekoälyekosysteemin komponentteja (mallit, upotukset, kontekstin tarjoajat, ulkoiset API:t) samalla turvallisuustarkkuudella kuin perinteisiä ohjelmistoriippuvuuksia

- **Jatkuva kehittyminen**: Pysy ajan tasalla nopeasti kehittyvien MCP-määrittelyjen kanssa, osallistu turvallisuusyhteisön standardeihin ja ylläpidä mukautuvaa turvallisuusasemaa protokollan kehittyessä

- **Microsoftin turvallisuusintegraatio**: Hyödynnä Microsoftin kattavaa turvallisuus-ekosysteemiä (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) MCP-käyttöönoton suojaamiseksi

## Kattavat resurssit

### **Viralliset MCP-turvallisuusdokumentaatiot**
- [MCP-määrittely (Ajantasainen: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP:n turvallisuuden parhaat käytännöt](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP:n valtuutusmäärittely](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub-repositorio](https://github.com/modelcontextprotocol)

### **Turvallisuusstandardit & parhaat käytännöt**
- [OAuth 2.0:n turvallisuuden parhaat käytännöt (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 verkkosovellusten turvallisuus](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 suurille kielimalleille](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Tekoälyn turvallisuustutkimus & analyysi**
- [Kehotteen injektointi MCP:ssä (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Työkalujen myrkytyshyökkäykset (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP:n tietoturvatutkimusraportti (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoftin tietoturvaratkaisut**
- [Microsoft Prompt Shields -dokumentaatio](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety -palvelu](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID:n tietoturva](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Managementin parhaat käytännöt](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Toteutusoppaat ja opetusohjelmat**
- [Azure API Management MCP-todennussillanasi](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID -todennus MCP-palvelimilla](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Turvallinen tunnisteiden tallennus ja salaus (video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps- ja toimitusketjun tietoturva**
- [Azure DevOpsin tietoturva](https://azure.microsoft.com/products/devops)
- [Azure Reposin tietoturva](https://azure.microsoft.com/products/devops/repos/)
- [Microsoftin toimitusketjun tietoturvamatka](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Lisätietoturvadokumentaatio**

Kattavaa tietoturvaohjeistusta varten tutustu tähän osioon kuuluvien erikoisdokumenttien sisältöön:

- **[MCP:n tietoturvan parhaat käytännöt 2025](./mcp-security-best-practices-2025.md)** - Täydelliset tietoturvan parhaat käytännöt MCP-toteutuksille
- **[Azure Content Safety -toteutus](./azure-content-safety-implementation.md)** - Käytännön toteutusesimerkkejä Azure Content Safety -integraatioon  
- **[MCP:n tietoturvakontrollit 2025](./mcp-security-controls-2025.md)** - Viimeisimmät tietoturvakontrollit ja -menetelmät MCP-järjestelmiin
- **[MCP:n parhaat käytännöt pikaopas](./mcp-best-practices.md)** - Pikaopas keskeisiin MCP-tietoturvakäytäntöihin

---

## Mitä seuraavaksi

Seuraava: [Luku 3: Aloittaminen](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->