# MCP:n turvallisuuden parhaat käytännöt 2025

Tämä kattava opas esittelee olennaiset turvallisuuden parhaat käytännöt Model Context Protocol (MCP) -järjestelmien toteuttamiseen perustuen uusimpaan **MCP Specification 2025-11-25** -määrittelyyn ja nykyisiin alan standardeihin. Nämä käytännöt käsittelevät sekä perinteisiä turvallisuuskysymyksiä että MCP-järjestelmiin liittyviä tekoälyyn liittyviä uhkia.

## Kriittiset turvallisuusvaatimukset

### Pakolliset turvallisuusohjaimet (MUST-vaatimukset)

1. **Tokenin validointi**: MCP-palvelimet **EIVÄT SAA** hyväksyä mitään tokeneita, joita ei ole nimenomaisesti myönnetty kyseiselle MCP-palvelimelle
2. **Valtuutuksen tarkistus**: MCP-palvelimet, jotka toteuttavat valtuutuksen, **MUST** tarkistaa KAIKKI saapuvat pyynnöt eikä **SAA** käyttää istuntoja todennukseen  
3. **Käyttäjän suostumus**: MCP-välipalvelimet, jotka käyttävät staattisia asiakastunnuksia, **MUST** hankkia käyttäjän nimenomainen suostumus jokaiselle dynaamisesti rekisteröidylle asiakkaalle
4. **Turvalliset istuntotunnukset**: MCP-palvelimet **MUST** käyttää kryptografisesti turvallisia, ei-deterministisiä istuntotunnuksia, jotka on luotu turvallisilla satunnaislukugeneraattoreilla

## Keskeiset turvallisuuskäytännöt

### 1. Syötteen validointi ja puhdistus
- **Kattava syötteen validointi**: Validoi ja puhdista kaikki syötteet estääksesi injektiohyökkäykset, sekaannusongelmat ja kehotteen injektiohaavoittuvuudet
- **Parametrien skeeman noudattaminen**: Toteuta tiukka JSON-skeeman validointi kaikille työkalujen parametreille ja API-syötteille
- **Sisällön suodatus**: Käytä Microsoft Prompt Shields- ja Azure Content Safety -ratkaisuja haitallisen sisällön suodattamiseen kehotteissa ja vastauksissa
- **Tulosteen puhdistus**: Validoi ja puhdista kaikki mallin tuottamat tulosteet ennen niiden esittämistä käyttäjille tai alajärjestelmille

### 2. Todennus- ja valtuutusosaaminen  
- **Ulkoiset identiteetin tarjoajat**: Delegoi todennus vakiintuneille identiteetin tarjoajille (Microsoft Entra ID, OAuth 2.1 -tarjoajat) sen sijaan, että toteuttaisit oman todennuksen
- **Hienojakoiset käyttöoikeudet**: Toteuta granulaariset, työkalukohtaiset käyttöoikeudet vähimmän oikeuden periaatteen mukaisesti
- **Tokenin elinkaaren hallinta**: Käytä lyhytikäisiä käyttöoikeustokeneita turvallisella kierrätyksellä ja asianmukaisella kohdeyleisön validoinnilla
- **Monivaiheinen todennus**: Vaadi MFA kaikessa hallinnollisessa pääsyssä ja arkaluonteisissa toiminnoissa

### 3. Turvalliset viestintäprotokollat
- **Kuljetuskerroksen suojaus**: Käytä HTTPS/TLS 1.3 -protokollaa kaikessa MCP-viestinnässä asianmukaisella sertifikaattien validoinnilla
- **Päätepisteestä päätepisteeseen -salaus**: Toteuta lisäsalauskerrokset erittäin arkaluonteisille tiedoille siirrossa ja levossa
- **Sertifikaattien hallinta**: Huolehdi asianmukaisesta sertifikaattien elinkaaren hallinnasta automaattisilla uusintaprosesseilla
- **Protokollaversion noudattaminen**: Käytä nykyistä MCP-protokollaversiota (2025-11-25) asianmukaisella version neuvottelulla

### 4. Kehittynyt nopeusrajoitus ja resurssien suojaus
- **Monikerroksinen nopeusrajoitus**: Toteuta nopeusrajoitus käyttäjä-, istunto-, työkalu- ja resurssitasoilla väärinkäytösten estämiseksi
- **Soveltuva nopeusrajoitus**: Käytä koneoppimiseen perustuvaa nopeusrajoitusta, joka mukautuu käyttökuvioihin ja uhkaindikaattoreihin
- **Resurssikiintiöiden hallinta**: Aseta sopivat rajat laskentaresursseille, muistin käytölle ja suorituksen kestolle
- **DDoS-suojaus**: Ota käyttöön kattava DDoS-suojaus ja liikenteen analysointijärjestelmät

### 5. Kattava lokitus ja valvonta
- **Rakenteinen auditointilokitus**: Toteuta yksityiskohtaiset, haettavat lokit kaikista MCP-toiminnoista, työkalujen suorituksista ja turvallisuustapahtumista
- **Reaaliaikainen turvallisuusvalvonta**: Ota käyttöön SIEM-järjestelmät tekoälypohjaisella poikkeamien havaitsemisella MCP-kuormille
- **Tietosuojavaatimusten mukainen lokitus**: Kirjaa turvallisuustapahtumat kunnioittaen tietosuojavaatimuksia ja säädöksiä
- **Häiriötilanteiden hallinnan integrointi**: Yhdistä lokitusjärjestelmät automatisoituihin häiriötilanteiden hallinnan työnkulkuihin

### 6. Parannetut turvalliset tallennuskäytännöt
- **Laitteistoturvamoduulit**: Käytä HSM-tukea avainten tallennukseen (Azure Key Vault, AWS CloudHSM) kriittisissä kryptografisissa toiminnoissa
- **Salausavainten hallinta**: Toteuta asianmukainen avainten kierto, erottelu ja käyttöoikeuksien hallinta salausavaimille
- **Salaisuuksien hallinta**: Tallenna kaikki API-avaimet, tokenit ja tunnistetiedot omiin salaisuuksien hallintajärjestelmiin
- **Datan luokittelu**: Luokittele data arkaluonteisuuden mukaan ja käytä asianmukaisia suojaustoimenpiteitä

### 7. Kehittynyt tokenien hallinta
- **Tokenien läpiviennin estäminen**: Kiellä nimenomaisesti tokenien läpivientimallit, jotka ohittavat turvallisuusohjaimet
- **Kohdeyleisön validointi**: Varmista aina, että tokenin kohdeyleisön väitteet vastaavat tarkoitettua MCP-palvelimen identiteettiä
- **Väitteisiin perustuva valtuutus**: Toteuta hienojakoinen valtuutus tokenin väitteiden ja käyttäjäattribuuttien perusteella
- **Tokenin sitominen**: Sido tokenit tarvittaessa tiettyihin istuntoihin, käyttäjiin tai laitteisiin

### 8. Turvallinen istuntojen hallinta
- **Kryptografiset istuntotunnukset**: Luo istuntotunnukset kryptografisesti turvallisilla satunnaislukugeneraattoreilla (ei ennustettavia sekvenssejä)
- **Käyttäjäkohtainen sitominen**: Sido istuntotunnukset käyttäjäkohtaisiin tietoihin turvallisilla formaateilla kuten `<user_id>:<session_id>`
- **Istunnon elinkaaren hallinta**: Toteuta asianmukainen istunnon vanhentuminen, kierto ja mitätöintimekanismit
- **Istunnon suojausotsikot**: Käytä asianmukaisia HTTP-turvallisuusotsikoita istuntojen suojaamiseen

### 9. Tekoälyyn liittyvät turvallisuusohjaimet
- **Kehotteen injektion puolustus**: Ota käyttöön Microsoft Prompt Shields, joissa on spotlighting-, erotin- ja datamerkintätekniikat
- **Työkalujen myrkytyksen estäminen**: Validoi työkalujen metatiedot, valvo dynaamisia muutoksia ja varmista työkalujen eheys
- **Mallin tulosteen validointi**: Skannaa mallin tulosteet mahdollisen datavuodon, haitallisen sisällön tai turvallisuuspolitiikan rikkomusten varalta
- **Kontekstin ikkunan suojaus**: Toteuta ohjaimet kontekstin ikkunan myrkytyksen ja manipulointihyökkäysten estämiseksi

### 10. Työkalujen suorituksen turvallisuus
- **Suorituksen hiekkalaatikkoympäristö**: Suorita työkalut konttien sisällä eristetyissä ympäristöissä, joissa on resurssirajoitukset
- **Oikeuksien erottelu**: Suorita työkalut vähimmillä tarvittavilla oikeuksilla ja erillisillä palvelutilitunnuksilla
- **Verkkosegmentointi**: Toteuta verkkosegmentointi työkalujen suoritusyhteyksille
- **Suorituksen valvonta**: Valvo työkalujen suoritusta poikkeavan käyttäytymisen, resurssien käytön ja turvallisuusloukkausten varalta

### 11. Jatkuva turvallisuuden validointi
- **Automaattinen turvallisuustestaus**: Integroi turvallisuustestaus CI/CD-putkiin työkaluilla kuten GitHub Advanced Security
- **Haavoittuvuuksien hallinta**: Skannaa säännöllisesti kaikki riippuvuudet, mukaan lukien tekoälymallit ja ulkoiset palvelut
- **Penetraatiotestaus**: Suorita säännöllisiä turvallisuusarviointeja, jotka kohdistuvat erityisesti MCP-toteutuksiin
- **Turvallisuuskoodin tarkastukset**: Toteuta pakolliset turvallisuustarkastukset kaikille MCP-koodimuutoksille

### 12. Tekoälyn toimitusketjun turvallisuus
- **Komponenttien varmennus**: Varmista kaikkien tekoälykomponenttien (mallit, upotukset, API:t) alkuperä, eheys ja turvallisuus
- **Riippuvuuksien hallinta**: Pidä ajan tasalla kaikki ohjelmisto- ja tekoälyriippuvuudet haavoittuvuuksien seurannalla
- **Luotetut arkistot**: Käytä varmennettuja, luotettuja lähteitä kaikille tekoälymalleille, kirjastoille ja työkaluilla
- **Toimitusketjun valvonta**: Seuraa jatkuvasti tekoälypalveluntarjoajien ja mallivarastojen kompromissitilanteita

## Kehittyneet turvallisuusmallit

### Nollaluottamuksen arkkitehtuuri MCP:lle
- **Älä koskaan luota, tarkista aina**: Toteuta jatkuva tarkistus kaikille MCP-osapuolille
- **Mikrosegmentointi**: Eristä MCP-komponentit granulaarisilla verkko- ja identiteettiohjauksilla
- **Ehdollinen pääsy**: Toteuta riskipohjaiset pääsynhallinnat, jotka mukautuvat kontekstiin ja käyttäytymiseen
- **Jatkuva riskinarviointi**: Arvioi dynaamisesti turvallisuusasema nykyisten uhkaindikaattoreiden perusteella

### Tietosuojaa kunnioittava tekoälyn toteutus
- **Datan minimointi**: Paljasta vain kunkin MCP-toiminnon kannalta välttämätön vähimmäismäärä dataa
- **Differential Privacy**: Toteuta tietosuojaa parantavia menetelmiä arkaluonteisen datan käsittelyssä
- **Homomorfinen salaus**: Käytä kehittyneitä salausmenetelmiä turvalliseen laskentaan salatussa datassa
- **Federated Learning**: Toteuta hajautettuja oppimismenetelmiä, jotka säilyttävät datan paikallisuuden ja yksityisyyden

### Häiriötilanteiden hallinta tekoälyjärjestelmissä
- **Tekoälykohtaiset häiriömenettelyt**: Kehitä häiriötilanteiden hallinnan menettelyt, jotka on räätälöity tekoälyyn ja MCP:n erityisuhkiin
- **Automaattinen reagointi**: Toteuta automaattinen rajoitus ja korjaus yleisille tekoälyn turvallisuustapahtumille  
- **Oikeuslääketieteelliset valmiudet**: Pidä yllä oikeuslääketieteellistä valmiutta tekoälyjärjestelmien kompromisseihin ja tietovuotoihin
- **Palautusmenettelyt**: Määritä menettelyt tekoälymallien myrkytyksestä, kehotteen injektiohyökkäyksistä ja palvelun kompromisseista palautumiseen

## Toteutusresurssit ja standardit

### Virallinen MCP-dokumentaatio
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Nykyinen MCP-protokollan määrittely
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Viralliset turvallisuusohjeet
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Todennus- ja valtuutusmallit
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Kuljetuskerroksen turvallisuusvaatimukset

### Microsoftin turvallisuusratkaisut
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Kehotteen injektion kehittynyt suojaus
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Kattava tekoälyn sisällön suodatus
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Yrityksen identiteetin ja pääsyn hallinta
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Turvallinen salaisuuksien ja tunnistetietojen hallinta
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Toimitusketjun ja koodin turvallisuusskannaus

### Turvallisuusstandardit ja -kehykset
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Nykyiset OAuth-turvallisuusohjeet
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Verkkosovellusten turvallisuusriskit
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Tekoälykohtaiset turvallisuusriskit
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Kattava tekoälyn riskienhallinta
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Tietoturvan hallintajärjestelmät

### Toteutusoppaat ja tutoriaalit
- [Azure API Management MCP:n todennusporttina](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Yritystason todennusmallit
- [Microsoft Entra ID MCP-palvelimilla](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Identiteetin tarjoajan integrointi
- [Turvallisen tokenin tallennuksen toteutus](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Tokenien hallinnan parhaat käytännöt
- [Päätepisteestä päätepisteeseen -salaus tekoälylle](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Kehittyneet salausmallit

### Kehittyneet turvallisuusresurssit
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Turvallisen kehityksen käytännöt
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Tekoälykohtainen turvallisuustestaus
- [Uhkamallinnus tekoälyjärjestelmille](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Tekoälyn uhkamallinnusmenetelmä
- [Tietosuojatekniikat tekoälylle](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Tietosuojaa parantavat tekoälytekniikat

### Säädösten noudattaminen ja hallinto
- [GDPR-yhteensopivuus tekoälylle](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Tietosuojavaatimukset tekoälyjärjestelmissä
- [Tekoälyn hallintakehys](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Vastuullinen tekoälyn toteutus
- [SOC 2 tekoälypalveluille](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Turvallisuusohjaimet tekoälypalveluntarjoajille
- [HIPAA-yhteensopivuus tekoälylle](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Terveydenhuollon tekoälyn vaatimukset

### DevSecOps ja automaatio
- [DevSecOps-putki tekoälylle](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Turvalliset tekoälyn kehityspolut
- [Automaattinen turvallisuustestaus](https://learn.microsoft.com/security/engineering/devsecops) - Jatkuva turvallisuuden validointi
- [Infrastruktuuri koodina -turvallisuus](https://learn.microsoft.com/security/engineering/infrastructure-security) - Turvallinen infrastruktuurin käyttöönotto
- [Konttien turvallisuus tekoälykuormille](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Tekoälykuormien konttien turvallisuus

### Valvonta ja häiriötilanteiden hallinta  
- [Azure Monitor tekoälykuormille](https://learn.microsoft.com/azure/azure-monitor/overview) - Kattavat valvontaratkaisut
- [Tekoälyn turvallisuushäiriöiden hallinta](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Tekoälykohtaiset häiriömenettelyt
- [SIEM tekoälyjärjestelmille](https://learn.microsoft.com/azure/sentinel/overview) - Turvallisuustiedon ja tapahtumien hallinta
- [Uhkatiedustelu tekoälylle](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Tekoälyn uhkatiedustelulähteet

## 🔄 Jatkuva parantaminen

### Pysy ajan tasalla kehittyvien standardien kanssa
- **MCP-määrittelyn päivitykset**: Seuraa virallisia MCP-määrittelyn muutoksia ja turvallisuustiedotteita
- **Uhkatiedustelu**: Tilaa tekoälyn turvallisuusuhkien syötteitä ja haavoittuvuustietokantoja  
- **Yhteisön osallistuminen**: Osallistu MCP:n turvallisuusyhteisön keskusteluihin ja työryhmiin
- **Säännöllinen arviointi**: Suorita neljännesvuosittaiset turvallisuusaseman arvioinnit ja päivitä käytäntöjä sen mukaisesti

### Osallistuminen MCP:n turvallisuuteen
- **Turvallisuustutkimus**: Osallistu MCP:n turvallisuustutkimukseen ja haavoittuvuuksien ilmoitusohjelmiin
- **Parhaiden käytäntöjen jakaminen**: Jaa turvallisuustoteutuksia ja oppeja yhteisön kanssa
- **Vakioiden kehitys**: Osallistua MCP-spesifikaation kehittämiseen ja turvallisuusstandardien luomiseen  
- **Työkalujen kehitys**: Kehittää ja jakaa turvallisuustyökaluja ja kirjastoja MCP-ekosysteemille  

---

*Tämä asiakirja heijastaa MCP:n turvallisuuden parhaita käytäntöjä 18. joulukuuta 2025 lähtien, perustuen MCP-spesifikaatioon 2025-11-25. Turvallisuuskäytäntöjä tulisi säännöllisesti tarkistaa ja päivittää protokollan ja uhkaympäristön kehittyessä.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->