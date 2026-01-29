# MCP:n turvallisuuden parhaat käytännöt – joulukuu 2025 päivitys

> **Tärkeää**: Tämä asiakirja heijastaa uusimpia [MCP-spesifikaation 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) turvallisuusvaatimuksia ja virallisia [MCP:n turvallisuuden parhaita käytäntöjä](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Viittaa aina ajantasaiseen spesifikaatioon saadaksesi viimeisimmät ohjeet.

## Keskeiset turvallisuuskäytännöt MCP-toteutuksille

Model Context Protocol tuo mukanaan ainutlaatuisia turvallisuushaasteita, jotka ylittävät perinteisen ohjelmistoturvallisuuden. Nämä käytännöt käsittelevät sekä perustason turvallisuusvaatimuksia että MCP-spesifisiä uhkia, kuten kehotteen injektiota, työkalujen myrkyttämistä, istunnon kaappausta, sekaannuskomissaariongelmia ja tunnisteiden läpivientivaurioita.

### **PAKOLLINEN turvallisuusvaatimukset**

**Kriittiset vaatimukset MCP-spesifikaatiosta:**

### **PAKOLLINEN turvallisuusvaatimukset**

**Kriittiset vaatimukset MCP-spesifikaatiosta:**

> **EI SAA**: MCP-palvelimet **EIVÄT SAA** hyväksyä tunnisteita, joita ei ole nimenomaisesti myönnetty kyseiselle MCP-palvelimelle  
>  
> **SAA**: MCP-palvelimet, jotka toteuttavat valtuutuksen, **SAA** tarkistaa KAIKKI saapuvat pyynnöt  
>  
> **EI SAA**: MCP-palvelimet **EIVÄT SAA** käyttää istuntoja todennukseen  
>  
> **SAA**: MCP-välipalvelimet, jotka käyttävät staattisia asiakastunnuksia, **SAA** hankkia käyttäjän suostumus jokaiselle dynaamisesti rekisteröidylle asiakkaalle

---

## 1. **Tunnisteiden turvallisuus ja todennus**

**Todennus- ja valtuutusvalvonta:**
   - **Tiukka valtuutuksen tarkastus**: Suorita kattavat auditoinnit MCP-palvelimen valtuutuslogiikasta varmistaaksesi, että vain tarkoitetut käyttäjät ja asiakkaat pääsevät resursseihin
   - **Ulkoinen identiteetin tarjoajan integrointi**: Käytä vakiintuneita identiteetin tarjoajia, kuten Microsoft Entra ID:tä, sen sijaan että toteuttaisit omaa todennusta
   - **Tunnisteen kohdevalidointi**: Varmista aina, että tunnisteet on nimenomaisesti myönnetty sinun MCP-palvelimellesi – älä koskaan hyväksy ylemmän tason tunnisteita
   - **Oikea tunnisteen elinkaaren hallinta**: Toteuta turvallinen tunnisteiden kierto, vanhentumiskäytännöt ja estä tunnisteiden uudelleenkäyttöhyökkäykset

**Suojaettu tunnisteiden tallennus:**
   - Käytä Azure Key Vaultia tai vastaavia turvallisia tunnistetietovarastoja kaikille salaisuuksille
   - Toteuta salaus tunnisteille sekä levossa että siirrossa
   - Säännöllinen tunnistetietojen kierto ja valvonta luvattoman käytön estämiseksi

## 2. **Istunnon hallinta ja siirtoturvallisuus**

**Turvalliset istuntokäytännöt:**
   - **Kryptografisesti turvalliset istunto-ID:t**: Käytä turvallisia, ei-deterministisiä istunto-ID:itä, jotka on luotu turvallisilla satunnaislukugeneraattoreilla
   - **Käyttäjäkohtainen sidonta**: Sido istunto-ID:t käyttäjäidentiteetteihin muodoilla kuten `<user_id>:<session_id>` estääksesi istuntojen väärinkäytön eri käyttäjien välillä
   - **Istunnon elinkaaren hallinta**: Toteuta asianmukainen vanhentuminen, kierto ja mitätöinti haavoittuvuuksien rajoittamiseksi
   - **HTTPS/TLS-vaatimus**: Pakollinen HTTPS kaikessa viestinnässä estämään istunto-ID:n sieppaus

**Siirtokerroksen turvallisuus:**
   - Määritä TLS 1.3 mahdollisuuksien mukaan asianmukaisella sertifikaattien hallinnalla
   - Toteuta sertifikaattien pinnaus kriittisille yhteyksille
   - Säännöllinen sertifikaattien kierto ja voimassaolon tarkistus

## 3. **AI-spesifinen uhkasuojaus** 🤖

**Kehotteen injektion torjunta:**
   - **Microsoft Prompt Shields**: Ota käyttöön AI Prompt Shields kehittyneeseen haitallisten ohjeiden tunnistukseen ja suodatukseen
   - **Syötteen puhdistus**: Varmista ja puhdista kaikki syötteet estääksesi injektiohyökkäykset ja sekaannuskomissaariongelmat
   - **Sisällön rajat**: Käytä erotin- ja datamerkintäjärjestelmiä erottaaksesi luotetut ohjeet ulkoisesta sisällöstä

**Työkalujen myrkytyksen estäminen:**
   - **Työkalun metatietojen validointi**: Toteuta eheystarkastukset työkalumäärittelyille ja valvo odottamattomia muutoksia
   - **Dynaaminen työkalujen valvonta**: Seuraa suoritusaikaa ja aseta hälytykset odottamattomista suoritustavoista
   - **Hyväksyntätyönkulut**: Vaadi käyttäjän nimenomainen hyväksyntä työkalumuutoksille ja kyvykkyyksien muutoksille

## 4. **Pääsynvalvonta ja käyttöoikeudet**

**Vähimmän oikeuden periaate:**
   - Myönnä MCP-palvelimille vain vähimmäisoikeudet, jotka ovat tarpeen tarkoitetulle toiminnallisuudelle
   - Toteuta roolipohjainen pääsynvalvonta (RBAC) hienojakoisilla käyttöoikeuksilla
   - Säännölliset käyttöoikeuksien tarkastukset ja jatkuva valvonta oikeuksien laajentumisen estämiseksi

**Suoritusaikaiset käyttöoikeuksien valvonnat:**
   - Aseta resurssirajoituksia estämään resurssien loppumishyökkäyksiä
   - Käytä konttien eristystä työkalujen suoritusalustoilla  
   - Toteuta juuri oikeaan aikaan -pääsy hallinnollisille toiminnoille

## 5. **Sisällön turvallisuus ja valvonta**

**Sisällön turvallisuuden toteutus:**
   - **Azure Content Safety -integraatio**: Käytä Azure Content Safetyä haitallisen sisällön, jailbreak-yritysten ja politiikkarikkomusten havaitsemiseen
   - **Käyttäytymisanalyysi**: Toteuta suoritusaikainen käyttäytymisen valvonta MCP-palvelimen ja työkalujen suorituksessa poikkeamien havaitsemiseksi
   - **Kattava lokitus**: Kirjaa kaikki todennusyritykset, työkalukutsut ja turvallisuustapahtumat turvalliseen, muuttumattomaan tallennukseen

**Jatkuva valvonta:**
   - Reaaliaikaiset hälytykset epäilyttävistä kuvioista ja luvattomista pääsyyrityksistä  
   - Integraatio SIEM-järjestelmiin keskitettyä turvallisuustapahtumien hallintaa varten
   - Säännölliset turvallisuusauditoinnit ja tunkeutumistestaukset MCP-toteutuksille

## 6. **Toimitusketjun turvallisuus**

**Komponenttien varmistus:**
   - **Riippuvuusskannaus**: Käytä automatisoituja haavoittuvuusskannauksia kaikille ohjelmisto- ja AI-riippuvuuksille
   - **Alkuperän validointi**: Varmista mallien, tietolähteiden ja ulkoisten palveluiden alkuperä, lisensointi ja eheys
   - **Allekirjoitetut paketit**: Käytä kryptografisesti allekirjoitettuja paketteja ja varmista allekirjoitukset ennen käyttöönottoa

**Turvallinen kehityspipeline:**
   - **GitHub Advanced Security**: Toteuta salaisuuksien skannaus, riippuvuusanalyysi ja CodeQL-staattinen analyysi
   - **CI/CD-turvallisuus**: Integroi turvallisuuden validointi automatisoituihin käyttöönottoihin
   - **Artefaktien eheys**: Toteuta kryptografinen varmennus käyttöönotetuille artefakteille ja konfiguraatioille

## 7. **OAuth-turvallisuus ja sekaannuskomissaariongelman estäminen**

**OAuth 2.1 -toteutus:**
   - **PKCE-toteutus**: Käytä Proof Key for Code Exchange (PKCE) -menetelmää kaikissa valtuutuspyynnöissä
   - **Nimenomainen suostumus**: Hanki käyttäjän suostumus jokaiselle dynaamisesti rekisteröidylle asiakkaalle sekaannuskomissaariongelmien estämiseksi
   - **Redirect URI:n validointi**: Toteuta tiukka uudelleenohjaus-URI:en ja asiakastunnusten validointi

**Välipalvelimen turvallisuus:**
   - Estä valtuutuksen ohitus staattisten asiakastunnusten hyväksikäytöllä
   - Toteuta asianmukaiset suostumustyönkulut kolmannen osapuolen API-pääsyille
   - Valvo valtuutuskoodin varastamista ja luvattomia API-pääsyjä

## 8. **Häiriötilanteisiin reagointi ja palautuminen**

**Nopeat reagointikyvyt:**
   - **Automaattinen reagointi**: Toteuta automatisoidut järjestelmät tunnistetietojen kiertoon ja uhkien rajoittamiseen
   - **Palautusmenettelyt**: Mahdollisuus nopeasti palauttaa tunnetusti toimivat konfiguraatiot ja komponentit
   - **Forensiikkakyvyt**: Yksityiskohtaiset auditointilokit ja lokit häiriötutkintaa varten

**Viestintä ja koordinointi:**
   - Selkeät eskalointimenettelyt turvallisuustapahtumille
   - Integraatio organisaation häiriötilanteiden reagointitiimien kanssa
   - Säännölliset turvallisuustapahtumien simulaatiot ja pöytätoimintaharjoitukset

## 9. **Säädösten noudattaminen ja hallinto**

**Säädösten noudattaminen:**
   - Varmista, että MCP-toteutukset täyttävät toimialakohtaiset vaatimukset (GDPR, HIPAA, SOC 2)
   - Toteuta tietoluokittelu ja yksityisyydensuojakontrollit AI-datan käsittelyyn
   - Pidä kattava dokumentaatio vaatimustenmukaisuuden auditointia varten

**Muutosten hallinta:**
   - Viralliset turvallisuustarkastusprosessit kaikille MCP-järjestelmän muutoksille
   - Versiohallinta ja hyväksyntätyönkulut konfiguraatiomuutoksille
   - Säännölliset vaatimustenmukaisuuden arvioinnit ja puutteiden analyysit

## 10. **Edistyneet turvallisuusvalvonnat**

**Zero Trust -arkkitehtuuri:**
   - **Älä koskaan luota, varmista aina**: Jatkuva käyttäjien, laitteiden ja yhteyksien varmennus
   - **Mikrosegmentointi**: Hienojakoiset verkkovalvonnat, jotka eristävät yksittäiset MCP-komponentit
   - **Ehdollinen pääsy**: Riskipohjaiset pääsynvalvonnat, jotka mukautuvat nykyiseen kontekstiin ja käyttäytymiseen

**Suoritusaikainen sovellusturva:**
   - **Runtime Application Self-Protection (RASP)**: Ota käyttöön RASP-tekniikoita reaaliaikaiseen uhkien havaitsemiseen
   - **Sovelluksen suorituskyvyn valvonta**: Seuraa suorituskyvyn poikkeamia, jotka voivat viitata hyökkäyksiin
   - **Dynaamiset turvallisuuspolitiikat**: Toteuta turvallisuuspolitiikat, jotka mukautuvat nykyisen uhkakentän mukaan

## 11. **Microsoftin turvallisuus-ekosysteemin integrointi**

**Kattava Microsoftin turvallisuus:**
   - **Microsoft Defender for Cloud**: Pilven turvallisuusaseman hallinta MCP-kuormille
   - **Azure Sentinel**: Pilvipohjainen SIEM- ja SOAR-kyvykkyydet kehittyneeseen uhkien havaitsemiseen
   - **Microsoft Purview**: Datan hallinta ja vaatimustenmukaisuus AI-työnkuluille ja tietolähteille

**Identiteetin ja pääsyn hallinta:**
   - **Microsoft Entra ID**: Yritystason identiteetin hallinta ehdollisilla pääsypolitiikoilla
   - **Privileged Identity Management (PIM)**: Juuri oikeaan aikaan -pääsy ja hyväksyntätyönkulut hallinnollisille toiminnoille
   - **Identiteettisuojaus**: Riskipohjainen ehdollinen pääsy ja automatisoitu uhkavaste

## 12. **Jatkuva turvallisuuden kehitys**

**Ajantasalla pysyminen:**
   - **Spesifikaation seuranta**: Säännöllinen MCP-spesifikaation päivitysten ja turvallisuusohjeiden muutosten tarkastelu
   - **Uhkatiedustelu**: AI-spesifisten uhkatietovirtojen ja kompromissin indikaattoreiden integrointi
   - **Turvallisuusyhteisön osallistuminen**: Aktiivinen osallistuminen MCP-turvallisuusyhteisöön ja haavoittuvuuksien ilmoitusohjelmiin

**Mukautuva turvallisuus:**
   - **Koneoppimisen turvallisuus**: Käytä ML-pohjaista poikkeamien tunnistusta uusien hyökkäyskuvioiden havaitsemiseen
   - **Ennakoiva turvallisuusanalytiikka**: Toteuta ennakoivia malleja uhkien proaktiiviseen tunnistamiseen
   - **Turvallisuuden automaatio**: Automaattiset turvallisuuspolitiikan päivitykset uhkatiedustelun ja spesifikaatiomuutosten perusteella

---

## **Kriittiset turvallisuusresurssit**

### **Virallinen MCP-dokumentaatio**
- [MCP-spesifikaatio (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP:n turvallisuuden parhaat käytännöt](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP-valtuutuksen spesifikaatio](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoftin turvallisuusratkaisut**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID:n turvallisuus](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Turvallisuusstandardit**
- [OAuth 2.0:n parhaat turvallisuuskäytännöt (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 suurille kielimalleille](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Toteutusoppaat**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID MCP-palvelimilla](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Turvallisuustiedote**: MCP:n turvallisuuskäytännöt kehittyvät nopeasti. Varmista aina ajantasaiset tiedot nykyisestä [MCP-spesifikaatiosta](https://spec.modelcontextprotocol.io/) ja [virallisesta turvallisuusdokumentaatiosta](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) ennen toteutusta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->