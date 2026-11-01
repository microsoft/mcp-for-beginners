# MCP Turvallisuuden parhaat käytännöt - Päivitys syyskuu 2026

> **Tärkeää:** Tämä asiakirja heijastaa
> [MCP-spesifikaatiota 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> ja virallista
> [MCP Turvallisuuden parhaat käytännöt](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Käytännön turvallisuuskoulutus

Käytännön toteutuskokemuksen saamiseksi suosittelemme **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - kattavaa ohjattua retkeä MCP-palvelimien suojaamiseksi Azure-ympäristössä. Työpaja käsittelee kaikki OWASP MCP Top 10 -riskit "haavoittuvainen → hyväksikäyttö → korjaus → validointi" -menetelmän avulla.

Kaikki tässä asiakirjassa esitetyt käytännöt ovat linjassa **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** kanssa Azure-spesifisten toteutusohjeiden osalta.

## Välttämättömät turvallisuuskäytännöt MCP-toteutuksille

Model Context Protocol tuo ainutlaatuisia turvallisuushaasteita, jotka ylittävät perinteisen ohjelmistoturvallisuuden. Nämä käytännöt käsittelevät perustavanlaatuisia vaatimuksia ja MCP-spesifisiä uhkia kuten kehotteen injektointi, työkalun myrkyttäminen, tilankäsittelijän kaappaaminen, sekaantunut välittäjä -ongelmat ja tunnisteiden läpivientihaavoittuvuudet.

### **VELVOITTAVAT turvallisuusvaatimukset** 

**Kriittiset vaatimukset MCP-spesifikaatiosta:**

> **EI SAA:** MCP-palvelimet **EI SAA** hyväksyä tunnisteita, jotka eivät ole nimenomaisesti myönnetty tälle MCP-palvelimelle

> **ON TARPEEN:** MCP-palvelinten, jotka toteuttavat valtuutuksen, **ON TARPEEN** tarkistaa KAIKKI saapuvat pyynnöt

> **EI SAA:** MCP-palvelimet **EI SAA** käyttää sessioita autentikointiin
>
> **ON TARPEEN:** MCP-välipalvelimien, jotka käyttävät staattista kolmannen osapuolen asiakas-ID:tä, **ON TARPEEN**
> hankkia suostumus jokaiselta MCP-asiakkaalta ennen valtuutuksen välittämistä

---

## 1. **Tunnisteturva & autentikointi**

**Autentikointi- ja valtuutussäätimet:**

   - **Ulkoinen identiteetin tarjoajan integraatio**: Käytä tunnettuja identiteetin tarjoajia kuten Microsoft Entra ID:tä sen sijaan, että toteutat omaa autentikointia

   - **Oikea tunnisteen elinkaari**: Toteuta turvallinen tunnisteiden kierto, vanhenemiskäytännöt ja estä tunnisteiden uudelleenkäyttöhyökkäykset

**Suojaettu tunnisteiden tallennus:**
   - Käytä Azure Key Vaultia tai vastaavia turvallisia tunnistetallennuksia kaikille salaisuuksille
   - Toteuta salaus tunnisteille sekä levossa että siirrossa


## 2. **Tilanhallinta & siirtoturva**

**Turvalliset sovellustilan käytännöt:**

- **Hämärät tilankäsittelijät**: Käytä turvallisia, ei-deterministisiä käsittelijöitä sovellustilalle, joka kattaa pyynnöt

- **Elinkaaren hallinta**: Vanhenna ja peru käsittelijät haavoittuvuusaikojen rajoittamiseksi


**Siirtokerroksen turvallisuus:**

- Vaatimus HTTPS:stä etä-HTTP-siirroissa tuotannossa
- Käytä prosessieristystä ja ympäristön tunnistetietoja paikallisissa stdio-palvelimissa
- Määritä moderni TLS oikeilla sertifikaattien kierto- ja validointikäytännöillä

## 3. **Tekoälyspesifinen uhkasuoja** 🤖

**Kehotteen injektoinnin puolustus:**

   - **Syötteen puhdistus**: Varmista ja puhdista kaikki syötteet estääksesi injektointihyökkäykset ja sekaantuneen välittäjän ongelmat
   - **Sisällön rajat**: Käytä erotin- ja datamerkintäjärjestelmiä luotettujen ohjeiden ja ulkoisen sisällön erottamiseen


   - **Työkalun metatietojen validointi**: Toteuta eheystarkastuksia työkalumäärittelyille ja seuraa odottamattomia muutoksia

   - **Hyväksymisprosessit**: Vaadi käyttäjän nimenomainen hyväksyntä työkalumuutoksille ja toiminnallisuuden muutoksille

## 4. **Pääsynvalvonta & käyttöoikeudet**


   - Myönnä MCP-palvelimille vain välttämätön määrä oikeuksia tarkoitetun toiminnallisuuden toteuttamiseksi
   - Toteuta roolipohjainen käyttöoikeuksien hallinta (RBAC) hienojakoisilla oikeuksilla
   - Säännölliset käyttöoikeuksien tarkastukset ja jatkuva valvonta käyttöoikeuksien korotusten estämiseksi


   - Käytä resurssirajoituksia estämään resurssien loppuun kuluminen hyökkäyksiä

   - Toteuta just-in-time-pääsy hallinnollisiin toimintoihin

## 5. **Sisällönturva & valvonta**


   - **Azure Content Safety -integraatio**: Käytä Azure Content Safetyä haitallisen sisällön, jailbreak-yritysten ja politiikkarikkomusten havaitsemiseen
   - **Käyttäytymisanalyysi**: Toteuta ajonaikaista käyttäytymisen valvontaa MCP-palvelimen ja työkalujen suorituksessa poikkeamien havaitsemiseksi
   - **Kattava lokitus**: Kirjaa kaikki autentikointiyritykset, työkalukutsut ja turvallisuustapahtumat turvalliseen, väärentämättömään tallennukseen


   - Reaaliaikaiset hälytykset epäilyttävistä kuvioista ja luvattomista pääsyoikeuksien yrityksistä

   - Säännölliset turvallisuusauditoinnit ja tunkeutumistestaukset MCP-toteutuksille

## 6. **Toimitusketjun turvallisuus**


   - **Riippuvuusskannaus**: Käytä automatisoituja haavoittuvuusskannauksia kaikille ohjelmistoruudelmille ja tekoälykomponenteille
   - **Alkuperätarkastus**: Varmista mallien, tietolähteiden ja ulkoisten palveluiden alkuperä, lisenssitiedot ja eheys
   - **Allekirjoitetut paketit**: Käytä kryptografisesti allekirjoitettuja paketteja ja varmista allekirjoitukset ennen käyttöönottoa


   - **GitHub Advanced Security**: Toteuta salaisuusskannaus, riippuvuusanalyysi ja CodeQL staattinen analyysi

   - **Artefaktien eheys**: Toteuta kryptografinen varmistus käyttöön otetuille artefakteille ja konfiguraatioille

## 7. **OAuth-turvallisuus & sekaantuneen välittäjän estäminen**


   - **PKCE-toteutus**: Käytä Proof Key for Code Exchange (PKCE) kaikissa valtuutuspyynnöissä
   - **Asiakasrekisteröinti**: Suosi Client ID Metadata Documents tai esirekisteröintiä; käytä vain vanhentunutta Dynamic Client Registrationia yhteensopivuuden takaamiseksi
   - **Nimenomainen suostumus**: MCP-proxyt, jotka käyttävät staattista kolmannen osapuolen asiakas-ID:tä, on hankittava suostumus jokaiselta MCP-asiakkaalta ennen valtuutuksen välittämistä
   - **Redirect URI -validointi**: Toteuta tiukka uudelleenohjaus-URI:en ja asiakastunnisteiden validointi

**Välipalvelimen turvallisuus:**

   - Toteuta asianmukaiset suostumusprosessit kolmannen osapuolen API-käyttöä varten
   - Valvo varkaiden valtuutuskoodien ja luvattoman API-käytön havaitsemista

## 8. **Hätätilanteisiin reagointi & palautuminen**

**Nopeat vastekyvyt:**
   - **Automaattinen vaste**: Toteuta automatisoituja järjestelmiä tunnistetietojen kiertämiseen ja uhkien rajaamiseen
   - **Palautusmenettelyt**: Mahdollisuus nopeasti palauttaa tunnetusti toimivat konfiguraatiot ja komponentit


**Viestintä & koordinointi:**
   - Selkeät eskalointiprosessit turvallisuustapauksiin
   - Integraatio organisaation hätätilanteiden reagointiryhmiin




**Sääntelyn noudattaminen:**
   - Varmista, että MCP-toteutukset täyttävät toimialakohtaiset vaatimukset (GDPR, HIPAA, SOC 2)
   - Toteuta AI-datan käsittelyn tietoluokittelu ja tietosuojakontrollit


**Muutoshallinta:**
   - Viralliset turvallisuustarkastukset kaikille MCP-järjestelmän muutoksille
   - Versionhallinta ja hyväksyntäprosessit konfiguraatiomuutoksille




**Zero Trust -arkkitehtuuri:**
   - **Älä koskaan luota, tarkista aina**: Jatkuva käyttäjien, laitteiden ja yhteyksien tarkistus
   - **Mikrosegmentointi**: Tarkat verkkokontrollit, jotka eristävät yksittäiset MCP-komponentit


**Ajonaikainen sovellussuojaus:**
   - **Runtime Application Self-Protection (RASP)**: Ota käyttöön RASP-menetelmiä reaaliaikaiseen uhkien havaitsemiseen
   - **Sovelluksen suorituskyvyn valvonta**: Seuraa suorituskyvyn poikkeavuuksia, jotka voivat viitata hyökkäyksiin




**Kattava Microsoft-tietoturva:**
   - **Microsoft Defender for Cloud**: Pilven turvallisuusaseman hallinta MCP-kuormille
   - **Azure Sentinel**: Pilvipohjainen SIEM- ja SOAR-ratkaisu edistyneeseen uhkien havaitsemiseen


**Identiteetin ja pääsynhallinta:**
   - **Microsoft Entra ID**: Yritysidentiteetin hallinta ehdollisilla pääsynhallintapolitiikoilla
   - **Privileged Identity Management (PIM)**: Just-in-time-pääsy ja hyväksymisprosessit hallinnollisille toiminnoille




**Ajantasalla pysyminen:**
   - **Spesifikaation seuranta**: Säännöllinen MCP-spesifikaation päivitysten ja turvallisuusohjeiden muutosten tarkastelu
   - **Uhkatiedustelu**: AI-spesifisten uhkatietovirtojen ja kompromissin indikaattoreiden integrointi

**Identiteetin- ja pääsynhallinta:**
   - **Microsoft Entra ID**: Yrityksen identiteetinhallinta ehdollisilla käyttöoikeuspolitiikoilla
   - **Privileged Identity Management (PIM)**: Tarveperusteinen pääsy ja hyväksyntätyönkulut hallinnollisiin toimintoihin
   - **Identity Protection**: Riskiin perustuva ehdollinen pääsy ja automaattinen uhkavaste

## 12. **Jatkuva turvallisuuden kehittyminen**

**Ajantasalla pysyminen:**
   - **Määrittelyn seuranta**: MCP-määrittelypäivitysten ja turvallisuusohjeiden muutosten säännöllinen tarkastelu
   - **Uhkatiedustelu**: AI-spesifisten uhkasyötteiden ja rikkomusindikaattorien integrointi
   - **Turvallisuusyhteisön osallistuminen**: Aktiivinen osallistuminen MCP:n turvallisuusyhteisöön ja haavoittuvuuksien paljastusohjelmiin

**Sopeutuva turvallisuus:**
   - **Koneoppimisen turvallisuus**: Koneoppimispohjaisten poikkeavuuksien tunnistusten käyttäminen uusien hyökkäysmallien havaitsemiseksi
   - **Ennakoiva turvallisuusanalytiikka**: Ennakoivien mallien implementointi uhkien proaktiiviseen tunnistamiseen
   - **Turvallisuuden automaatio**: Turvapolitiikan automaattiset päivitykset uhkatiedon ja määrittelymuutosten perusteella

---

## **Kriittiset turvallisuusresurssit**

### **Viralliset MCP-dokumentaatiot**
- [MCP-määrittely (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP:n turvallisuuden parhaat käytännöt](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP:n valtuutuksen määrittely](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP:n turvallisuusresurssit**
- [OWASP MCP Azure -turvaopas](https://microsoft.github.io/mcp-azure-security-guide/) - Kattava OWASP MCP Top 10 Azure-toteutuksella
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Viralliset OWASP MCP:n turvallisuusriskit
- [MCP Security Summit -työpaja (Sherpa)](https://azure-samples.github.io/sherpa/) - Käytännön turvallisuuskoulutus MCP:lle Azurella

### **Microsoftin turvallisuusratkaisut**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Turvastandardit**
- [OAuth 2.0 -turvallisuuden parhaat käytännöt (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 suurille kielimalleille](https://genai.owasp.org/)
- [NIST:n tekoälyn riskienhallintakehys](https://www.nist.gov/itl/ai-risk-management-framework)

### **Toteutusoppaat**
- [Azure API Management MCP -todennusportti](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID MCP-palvelimilla](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Turvallisuusilmoitus:** MCP:n turvallisuuskäytännöt kehittyvät nopeasti. Tarkista aina
> nykyinen [MCP-määrittely](https://modelcontextprotocol.io/specification/2026-07-28/)
> ja [virallinen turvallisuusdokumentaatio](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> ennen toteutusta.

## Mitä seuraavaksi

- Lue: [MCP:n turvallisuusvalvonta](./mcp-security-controls.md)
- Palaa: [Turvallisuusmoduulin yleiskatsaus](./README.md)
- Jatka: [Moduuli 3: Aloittaminen](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->