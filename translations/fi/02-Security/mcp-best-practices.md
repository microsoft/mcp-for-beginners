# MCP-turvallisuuden parhaat käytännöt - Päivitys syyskuu 2026

Tämä kattava opas määrittelee olennaiset turvallisuuden parhaat käytännöt
Model Context Protocol (MCP) -järjestelmien toteuttamiseen perustuen
**MCP Specification 2026-07-28** -määrittelyyn ja nykyisiin alan standardeihin. Nämä
käytännöt käsittelevät sekä perinteisiä turvallisuushuolia että MCP-käyttöönottoihin
liittyviä erityisiä uhkia tekoälyn osalta.

## Kriittiset turvallisuusvaatimukset

### Pakolliset turvallisuusvalvontatoimet (PITÄÄ-vaatimukset)

1. **Tokenin validointi**: MCP-palvelimet **EIVÄT SAA** hyväksyä mitään tokeneita, joita ei ole nimenomaisesti myönnetty kyseiselle MCP-palvelimelle
2. **Valtuutuksen tarkastus**: MCP-palvelimien, jotka toteuttavat valtuutuksen, **TÄYTYY** tarkistaa KAIKKI sisääntulevat pyynnöt ja **EI SAA** käyttää istuntoja todennukseen  
3. **Käyttäjän suostumus**: MCP-välityspalvelimien, jotka käyttävät staattisia kolmannen osapuolen asiakastunnuksia, **TÄYTYY** saada nimenomainen suostumus jokaiselle MCP-asiakkaalle ennen valtuutusprosessin ohjaamista
4. **State Handle -turvallisuus**: MCP-palvelimet **EIVÄT SAA** käsitellä sovelluksen state handle -omistusta todennuksena ja **PITÄÄ** valtuuttaa jokainen pyyntö, joka käyttää sellaista



## Perusturvallisuuskäytännöt

### 1. Syötteen validointi ja puhdistus
- **Laaja syötteen validointi**: Vahvista ja puhdista kaikki syötteet estääksesi injektiohyökkäykset, sekavien päälliköiden ongelmat ja kehotteen injektointiin liittyvät haavoittuvuudet
- **Parametrien skeeman valvonta**: Toteuta tiukka JSON-skeeman validointi kaikille työkalujen parametreille ja API-syötteille
- **Sisällön suodatus**: Käytä Microsoft Prompt Shields -suojauksia ja Azure Content Safetyä haitallisen sisällön suodattamiseen kehotteissa ja vastauksissa
- **Tulosten puhdistus**: Tarkista ja puhdista kaikki mallin tulosteet ennen niiden esittämistä käyttäjille tai alijärjestelmille

### 2. Todennus ja valtuutus huippuosaamisella  
- **Ulkoiset identiteetin tarjoajat**: Delegoi todennus vakiintuneille identiteetin tarjoajille (Microsoft Entra ID, OAuth 2.1 -tarjoajat) sen sijaan, että toteuttaisit oman todennuksen
- **Asiakaskirjautuminen**: Suosi Client ID Metadata -dokumentteja tai ennakkorekisteröintiä; käytä vanhentunutta Dynamic Client Registration -menetelmää vain yhteensopivuuden takia
- **Hienojakoinen käyttöoikeuksien hallinta**: Toteuta yksityiskohtaiset, työkalukohtaiset käyttöoikeudet tiukimman oikeuden periaatteen mukaisesti
- **Tokenien elinkaaren hallinta**: Käytä lyhytaikaisia käyttöoikeustokeneita, joille on varmistettu turvallinen kierto ja asianmukainen kohdevalidointi
- **Monivaiheinen todennus**: Vaadi MFA kaikissa hallinnollisissa pääsyissä ja arkaluonteisissa toiminnoissa

### 3. Turvalliset viestintäprotokollat
- **Transport Layer Security**: Käytä HTTPS:ää asianmukaisella sertifikaattien validoinnilla
	etä-HTTP MCP -viestintään; käytä prosessieristystä ja ympäristö­
	todennusta paikallisissa stdio-palvelimissa
- **End-to-End-salaus**: Toteuta lisäsalauskerrokset erityisen arkaluonteiselle datalle siirrossa ja lepotilassa
- **Sertifikaattien hallinta**: Ylläpidä asianmukaista sertifikaattien elinkaaren hallintaa automatisoiduilla uusintaprosesseilla
- **Protokollaversion valvonta**: Käytä MCP:tä versio `2026-07-28`, sisällytä vaadittu
	version metatieto jokaiseen pyyntöön ja hylkää tuettujen versioiden ulkopuoliset

### 4. Kehittynyt nopeusrajoitus ja resurssien suojaus
- **Monitasoinen nopeusrajoitus**: Toteuta nopeusrajoitus käyttäjän, tunnisteen,
  toiminnon, työkalun ja resurssin mukaan väärinkäytösten ehkäisemiseksi
- **Soveltuva nopeusrajoitus**: Käytä koneoppimispohjaista nopeusrajoitusta, joka mukautuu käyttökuvioihin ja uhkaindikaattoreihin
- **Resurssien määrärajojen hallinta**: Aseta sopivat rajat laskentaresursseille, muistin käytölle ja suoritusoikohtaiselle ajalle
- **DDoS-suojaus**: Käytä kattavaa DDoS-suojausta ja liikenteen analysointijärjestelmiä

### 5. Kattava lokitus ja valvonta
- **Strukturoitu auditointilokitus**: Toteuta yksityiskohtaiset, haettavat lokit kaikista MCP-toiminnoista, työkalujen suorituksista ja turvallisuustapahtumista
- **Reaaliaikainen turvallisuusvalvonta**: Ota käyttöön SIEM-järjestelmät tekoälypohjaisella poikkeavuuksien havaitsemisella MCP-kuormituksille
- **Tietosuojan mukainen lokitus**: Kirjaa turvallisuustapahtumat, kunnioittaen tietosuojavaatimuksia ja -sääntöjä
- **Poikkeamiin reagoinnin integraatio**: Kytke lokitusjärjestelmät automatisoituihin poikkeamien reagointiprosesseihin

### 6. Parannetut turvalliset tallennuskäytännöt
- **Laitteistoturvamoduulit (HSM)**: Käytä HSM:llä tuettua avainten säilytystä (Azure Key Vault, AWS CloudHSM) kriittisissä kryptografisissa toiminnoissa
- **Salausavainten hallinta**: Toteuta asianmukainen avainten kierto, eristys ja pääsynvalvonta salausavaimille
- **Salaisuuksien hallinta**: Säilytä kaikki API-avaimet, tokenit ja tunnistetiedot omissa salaisuuksien hallintajärjestelmissä
- **Datan luokittelu**: Luokittele data herkkyystasojen mukaan ja sovella asianmukaisia suojaustoimia

### 7. Kehittynyt tokenien hallinta
- **Tokenien läpivienti-eston toteutus**: Kielletään eksplisiittisesti tokenien läpivientimalleja, jotka ohittavat turvallisuusvalvonnat
- **Kohdevalidointi**: Tarkista aina, että tokenien kohdevaatimukset vastaavat tarkoitetun MCP-palvelimen identiteettiä
- **Vaatimuksiin perustuva valtuutus**: Toteuta hienojakoinen valtuutus tokenin vaatimusten ja käyttäjäominaisuuksien perusteella
- **Tokenien sitominen**: Varmista, että tokenit kohdistuvat tarkoitetulle MCP-resurssille ja
	sido sovelluksen state handle -tunnisteet palvelinpuolella todennettuun tunnukseen

### 8. Turvallinen sovelluksen tila

- **Kryptografiset state handle -tunnisteet**: Luo epäselviä, ei-deterministisiä tunnisteita
	tiloille, jotka ulottuvat useisiin pyyntöihin
- **Käyttäjäkohtainen sitominen**: Sido kukin tunniste palvelinpuolella todennettuun tunnukseen; älä luota käyttäjän toimittamaan tunnukseen
- **Elinkaarihallinta**: Vanhenna ja peruuta tunnisteet sekä määrittele, kuinka kutsujat
	pääsevät käsiksi vanhentuneeseen tilaan
- **Valtuutuksen uudelleentarkastus pyynnöittäin**: Tarkista valtuutus aina, kun tunniste esitetään; tunniste on nimi, ei todennus



### 9. Tekoälyyn liittyvät turvallisuusvalvontatoimet
- **Kehotteen injektion torjunta**: Käytä Microsoft Prompt Shields -suojauksia korostuksilla, erottimilla ja datamerkintätekniikoilla
- **Työkalujen myrkytyksen esto**: Tarkista työkalujen metatiedot, valvo dynaamisia muutoksia ja varmista työkalujen eheys
- **Mallin tulosten validointi**: Tarkista mallin tulokset mahdollisen datavuodon, haitallisen sisällön tai turvallisuuspolitiikan rikkomusten varalta
- **Kontekstin suojaus**: Toteuta kontrollit kontekstin ruudun myrkytyksen ja manipulointihyökkäysten estämiseksi

### 10. Työkalujen suoritusturvallisuus
- **Suorituksen hiekkalaatikkotila**: Suorita työkalut kontissa eristetyissä ympäristöissä, joissa on resurssirajoituksia
- **Oikeuksien eristäminen**: Suorita työkalut mahdollisimman vähäisin oikeuksin ja erillisillä palvelutilitunnuksilla
- **Verkkosegmentointi**: Toteuta verkkosegmentointi työkalujen suoritusympäristöissä
- **Suorituksen valvonta**: Valvo työkalujen suorituksia poikkeavien käyttäytymisten, resurssien käytön ja turvallisuusloukkausten havaitsemiseksi

### 11. Jatkuva turvallisuuden validointi
- **Automatisoitu turvallisuustestaus**: Integroi turvallisuustestaus CI/CD-putkiin työkalujen, kuten GitHub Advanced Security, avulla
- **Haavoittuvuuksien hallinta**: Skannaa säännöllisesti kaikki riippuvuudet, mukaan lukien tekoälymallit ja ulkoiset palvelut
- **Penetraatiotestaus**: Suorita säännöllisiä turvallisuustarkastuksia, jotka kohdistuvat erityisesti MCP-toteutuksiin
- **Turvallisuuskoodin tarkastukset**: Toteuta pakolliset turvallisuustarkastukset kaikille MCP-koodimuutoksille

### 12. Toimittajaketjun turvallisuus tekoälylle
- **Komponenttien varmennus**: Varmista kaikkien tekoälykomponenttien (mallit, upotukset, API:t) alkuperä, eheys ja turvallisuus
- **Riippuvuuksien hallinta**: Pidä yllä ajantasaisia inventaarioita kaikista ohjelmisto- ja tekoälyriippuvuuksista haavoittuvuusseurannalla
- **Luotetut arkistot**: Käytä varmennettuja, luotettavia lähteitä kaikille tekoälymalleille, kirjastoille ja työkaluillesi
- **Toimittajaketjun seuranta**: Valvo jatkuvasti tekoälypalveluntarjoajien ja mallien arkistojen kompromissien varalta

## Kehittyneet turvallisuusmallit

### Nollaluottamusarkkitehtuuri MCP:lle
- **Älä koskaan luota, varmista aina**: Toteuta jatkuva varmistus kaikille MCP-osapuolille
- **Mikrosegmentointi**: Eristä MCP-komponentit hienojakoisilla verkko- ja identiteettivalvonnalla
- **Ehdollinen pääsy**: Toteuta riskipohjaiset pääsynhallinnat, jotka mukautuvat kontekstiin ja käyttäytymiseen
- **Jatkuva riskinarviointi**: Arvioi dynaamisesti turvallisuusasema nykyisten uhkaindikaattorien perusteella

### Yksityisyyttä suojeleva tekoälyn toteutus
- **Datan minimointi**: Näytä vain kunkin MCP-toiminnon kannalta välttämätön vähimmäismäärä tietoa
- **Diferentiaalinen yksityisyys**: Toteuta yksityisyyttä suojavia menetelmiä arkaluonteisten tietojen käsittelyssä
- **Homomorfinen salaus**: Käytä kehittyneitä salausmenetelmiä turvalliseen laskentaan salatun datan päällä
- **Jakamislaskenta**: Toteuta hajautettuja oppimismenetelmiä, jotka säilyttävät datan paikallisuuden ja yksityisyyden

### Tekoälyjärjestelmien poikkeamiin reagointi
- **Tekoälyyn kohdistuvat poikkeamamenettelyt**: Kehitä poikkeamiin reagoinnin prosessit, jotka on räätälöity tekoälyyn ja MCP:hen liittyville uhkille
- **Automatisoitu reagointi**: Toteuta automatisoitu saartaminen ja korjaaminen yleisille tekoälyn turvallisuuden poikkeamille  
- **Oikeuslääketieteelliset valmiudet**: Pidä yllä valmiutta tekoälyjärjestelmien kompromisseihin ja tietovuotoihin
- **Palautusmenettelyt**: Määrittele menettelyt tekoälymallien myrkytyksestä, kehotteen injektointihyökkäyksistä ja palvelujen kompromisseista palautumiseksi

## Toteutusresurssit ja standardit

### 🏔️ Käytännön turvallisuuskoulutus
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Kattava käytännön työpaja MCP-palvelinten suojaamiseen Azuren ympäristössä
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Viitearkkitehtuuri ja OWASP MCP Top 10 -toteutusohjeet

### Virallinen MCP-dokumentaatio
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Ajantasainen MCP-protokollan määrittely
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Viralliset turvallisuusohjeet
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP-valtuutusmallit
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Siirtovaatimukset

### Microsoftin turvallisuusratkaisut
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Kehittynyt kehotteen injektion suojaus
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Kattava tekoälysisällön suodatus
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Toimialueen identiteetti- ja pääsynhallinta
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Turvallinen salaisuuksien ja tunnistetietojen hallinta
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Toimitusketjun ja koodin turvallisuusskannaus

### Turvallisuusstandardit ja -viitekehykset
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Ajantasaiset OAuth-turvaohjeet
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Verkkosovellusten turvallisuusuhat
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Tekoälyyn liittyvät turvallisuusuhat
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Kattava tekoälyn riskienhallinta
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Tietoturvan hallintajärjestelmät

### Toteutusoppaat ja opetusohjelmat
- [Azure API Management MCP:n todennusporttina](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Yritystason todennusmallit
- [Microsoft Entra ID MCP-palvelimien kanssa](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Identiteetin tarjoajan integrointi
- [Turvallinen tokenien tallennus](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Token-hallinnan parhaat käytännöt
- [Päätepisteestä päätepisteeseen -salaus tekoälylle](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Kehittyneet salausmallit

### Kehittyneet turvallisuusresurssit
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Turvallisen kehityksen käytännöt
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Tekoälyyn kohdistuva turvallisuustestaus
- [Uhkamallinnus tekoälyjärjestelmille](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Tekoälyn uhkamallinnuksen menetelmät
- [Tietosuojatekniikat tekoälylle](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Yksityisyyttä suojelevat tekoälytekniikat

### Noudattaminen ja hallinto
- [GDPR-yhteensopivuus tekoälylle](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Yksityisyyden suoja tekoälyjärjestelmissä
- [Tekoälyn hallintakehys](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Vastuullinen tekoälyn toteutus
- [SOC 2 tekoälypalveluille](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Turvallisuusvalvonnat tekoälypalveluntarjoajille
- [HIPAA-yhteensopivuus tekoälylle](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Terveydenhuollon tekoälyn vaatimukset

### DevSecOps ja automaatio
- [DevSecOps-putki tekoälylle](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Turvalliset tekoälyn kehityspolut
- [Automatisoitu turvallisuustestaus](https://learn.microsoft.com/security/engineering/devsecops) - Jatkuva turvallisuuden validointi
- [Infrastruktuurin turvallisuus koodina](https://learn.microsoft.com/security/engineering/infrastructure-security) - Turvallinen infrastruktuurin käyttöönotto
- [Konttien turvallisuus tekoälyssä](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Tekoälykuormien kontittamisen turvallisuus

### Valvonta ja poikkeamiin reagointi  
- [Azure Monitor tekoälyn kuormituksille](https://learn.microsoft.com/azure/azure-monitor/overview) - Kattavat valvontaratkaisut
- [Tekoälyn turvallisuuspoikkeamien käsittely](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Tekoälyyn kohdistuvat poikkeamamenettelyt
- [SIEM tekoälyjärjestelmille](https://learn.microsoft.com/azure/sentinel/overview) - Turvallisuustiedon ja -tapahtumien hallinta

- [Uhkatiedustelu tekoälylle](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Tekoälyn uhkatiedon lähteet

## 🔄 Jatkuva parantaminen

### Pysy ajan tasalla kehittyvien standardien kanssa
- **MCP-määritysten päivitykset**: Seuraa virallisia MCP-määritysten muutoksia ja tietoturvailmoituksia
- **Uhkatiedustelu**: Tilaa tekoälyn tietoturvauhkien syötteitä ja haavoittuvuustietokantoja  
- **Yhteisön osallistuminen**: Osallistu MCP:n tietoturvayhteisön keskusteluihin ja työryhmiin
- **Säännöllinen arviointi**: Tee neljännesvuosittaiset tietoturvan nykytilan arvioinnit ja päivitä toimintatapoja sen mukaisesti

### Osallistuminen MCP:n tietoturvaan
- **Tietoturvatutkimus**: Osallistu MCP:n tietoturvatutkimukseen ja haavoittuvuuksien raportointiohjelmiin
- **Parhaiden käytäntöjen jakaminen**: Jaa tietoturvan toteutuksia ja oppeja yhteisön kanssa
- **Standardien kehittäminen**: Osallistu MCP-määritysten kehittämiseen ja tietoturvastandardien luomiseen
- **Työkalujen kehittäminen**: Kehitä ja jaa tietoturvatyökaluja ja kirjastoja MCP-ekosysteemille

---

*Tämä dokumentti heijastaa MCP:n tietoturvan parhaita käytäntöjä 9. syyskuuta 2026,
perustuen MCP-määritykseen `2026-07-28`. Tietoturvakäytäntöjä tulisi tarkistaa
säännöllisesti, kun protokolla ja uhkakenttä kehittyvät.*

## Mitä seuraavaksi

- Lue: [MCP:n tietoturvan parhaat käytännöt](./mcp-security-best-practices.md)
- Palaa: [Tietoturvatoiminnon yleiskatsaus](./README.md)
- Jatka: [Moduuli 3: Aloittaminen](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->