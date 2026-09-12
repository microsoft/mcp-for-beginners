# 🚀 MCP-palvelin PostgreSQL:llä - Täydellinen oppaallinen opas

## 🧠 Yleiskatsaus MCP-tietokantaintegraation oppimispolkuun

Tämä kattava oppimisopas opettaa, miten rakennetaan tuotantovalmiita **Model Context Protocol (MCP) -palvelimia**, jotka integroituvat tietokantoihin käytännön vähittäiskaupan analytiikan käyttötapauksen kautta. Opit yritystason malleja, mukaan lukien **rivitasoturvallisuus (Row Level Security, RLS)**, **semanttinen haku**, **Azure AI -integraatio** ja **monivuokraajainen tietojen käyttöoikeus**.

Olitpa sitten backend-kehittäjä, AI-insinööri tai data-arkkitehti, tämä opas tarjoaa rakenteellisen oppimisen todellisilla esimerkeillä ja käytännön harjoituksilla, jotka johdattavat sinut MCP-palvelimeen osoitteessa https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Viralliset MCP-resurssit

- 📘 [MCP-dokumentaatio](https://modelcontextprotocol.io/) – Yksityiskohtaiset opetusohjelmat ja käyttöohjeet
- 📜 [MCP-spesifikaatio (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protokollan arkkitehtuuri ja tekniset viitteet
- 🧑‍💻 [MCP GitHub -varasto](https://github.com/modelcontextprotocol) – Avoimen lähdekoodin SDK:t, työkalut ja koodiesimerkit
- 🌐 [MCP-yhteisö](https://github.com/orgs/modelcontextprotocol/discussions) – Osallistu keskusteluihin ja tue yhteisöä
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Turvallisuuden parhaat käytännöt ja riskienhallinta


## 🧭 MCP-tietokantaintegraation oppimispolku

### 📚 Kokonaisvaltainen oppimisrakenne https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail -projektia varten

| Lab | Aihe | Kuvaus | Linkki |
|--------|-------|-------------|------|
| **Lab 1-3: Perustukset** | | | |
| 00 | [Johdatus MCP-tietokantaintegraatioon](./00-Introduction/README.md) | Yleiskatsaus MCP:stä tietokantaintegraation ja vähittäiskaupan analytiikan käyttötapauksen kanssa | [Aloita tästä](./00-Introduction/README.md) |
| 01 | [Ydinarkkitehtuurin käsitteet](./01-Architecture/README.md) | MCP-palvelimen arkkitehtuurin, tietokantakerrosten ja turvallisuusmallien ymmärtäminen | [Lue](./01-Architecture/README.md) |
| 02 | [Turvallisuus ja monivuokraajaisuus](./02-Security/README.md) | Rivitasoturvallisuus, tunnistautuminen ja monivuokraajainen tietojen käyttöoikeus | [Lue](./02-Security/README.md) |
| 03 | [Ympäristön asennus](./03-Setup/README.md) | Kehitysympäristön, Dockerin ja Azure-resurssien perustaminen | [Asenna](./03-Setup/README.md) |
| **Lab 4-6: MCP-palvelimen rakentaminen** | | | |
| 04 | [Tietokannan suunnittelu ja skeema](./04-Database/README.md) | PostgreSQL:n asennus, vähittäiskaupan skeeman suunnittelu ja esimerkkidata | [Rakenna](./04-Database/README.md) |
| 05 | [MCP-palvelimen toteutus](./05-MCP-Server/README.md) | FastMCP-palvelimen rakentaminen tietokantaintegraatiolla | [Rakenna](./05-MCP-Server/README.md) |
| 06 | [Työkalujen kehitys](./06-Tools/README.md) | Tietokantakyselytyökalujen ja skeeman introspektion luominen | [Rakenna](./06-Tools/README.md) |
| **Lab 7-9: Edistyneet ominaisuudet** | | | |
| 07 | [Semanttisen haun integraatio](./07-Semantic-Search/README.md) | Vektoriesitysten toteutus Azure OpenAI:n ja pgvectorin avulla | [Laajenna](./07-Semantic-Search/README.md) |
| 08 | [Testaus ja virheenkorjaus](./08-Testing/README.md) | Testausstrategiat, virheenkorjaustyökalut ja validointimenetelmät | [Testaa](./08-Testing/README.md) |
| 09 | [VS Code -integraatio](./09-VS-Code/README.md) | VS Code MCP -integraation ja AI-chatin käyttöönotto | [Integroi](./09-VS-Code/README.md) |
| **Lab 10-12: Tuotanto ja parhaat käytännöt** | | | |
| 10 | [Julkaisustrategiat](./10-Deployment/README.md) | Docker-julkaisu, Azure Container Apps ja skaalausnäkökohdat | [Julkaise](./10-Deployment/README.md) |
| 11 | [Seuranta ja havaittavuus](./11-Monitoring/README.md) | Application Insights, lokitus ja suorituskyvyn seuranta | [Seuraa](./11-Monitoring/README.md) |
| 12 | [Parhaat käytännöt ja optimointi](./12-Best-Practices/README.md) | Suorituskyvyn optimointi, turvallisuuden vahvistaminen ja tuotantovinkit | [Optimoi](./12-Best-Practices/README.md) |

### 💻 Mitä rakennat

Tämän oppimispolun lopussa olet rakentanut kokonaisen **Zava Retail Analytics MCP -palvelimen**, joka sisältää:

- **Monitaulukkoinen vähittäiskaupan tietokanta** asiakkaiden tilauksille, tuotteille ja varastolle
- **Rivitasoturvallisuuden** myymäläkohtaiselle datan eristämiselle
- **Semanttisen tuotteen haun** Azure OpenAI -upotuksilla
- **VS Code AI Chat -integraation** luonnollisen kielen kyselyille
- **Tuotantovalmiin käyttöönoton** Dockerilla ja Azurella
- **Laajan seurannan** Application Insights -työkalulla

## 🎯 Oppimisen edellytykset

Saadaksesi parhaan hyödyn tästä oppimispolusta sinun tulisi hallita:

- **Ohjelmointikokemus**: Tuntemus Pythonista (suositeltu) tai vastaavista kielistä
- **Tietokantatieto**: Peruskäsitys SQL:stä ja relaatiotietokannoista
- **API-käsitteet**: REST API:en ja HTTP:n ymmärtäminen
- **Kehitystyökalut**: Kokemusta komentorivistä, Gitistä ja koodieditoreista
- **Pilvipohjatiedot**: (Valinnainen) Perustieto Azuresta tai muista pilvialustoista
- **Docker-tuntemus**: (Valinnainen) Ymmärrys konttiteknologiasta

### Vaatimukset työkaluille

- **Docker Desktop** - PostgreSQL:n ja MCP-palvelimen ajamiseen
- **Azure CLI** - Pilviresurssien käyttöönottoon
- **VS Code** - Kehitykseen ja MCP-integraatioon
- **Git** - Versiohallintaan
- **Python 3.8+** - MCP-palvelimen kehittämiseen

## 📚 Opas ja resurssit

Tämä oppimispolku sisältää kattavat resurssit sujuvaan etenemiseen:

### Opas

Jokainen lab sisältää:
- **Selkeät oppimistavoitteet** - Mitä saavutetaan
- **Vaiheittaiset ohjeet** - Yksityiskohtaiset toteutusoppaat
- **Koodiesimerkit** - Toimivat näytteet selityksillä
- **Harjoitukset** - Käytännön harjoituksia
- **Vianetsintäoppaat** - Yleiset ongelmat ja ratkaisut
- **Lisäresurssit** - Syventävää lukemista ja tutkimista

### Edellytysten tarkistus

Ennen jokaista labia löydät:
- **Vaadittava tieto** - Mitä tulisi osata ennakolta
- **Ympäristön validointi** - Miten varmistaa ympäristösi toimivuus
- **Aikatauluarviot** - Odotettu suoritusajankohta
- **Oppimistulokset** - Mitä opit suorittamisen jälkeen

### Suositellut oppimispolut

Valitse polkusi kokemuksesi perusteella:

#### 🟢 **Aloittelijan polku** (Uusi MCP:hen)
1. Varmista, että olet suorittanut jaksot 0-10 [MCP for Beginners](https://aka.ms/mcp-for-beginners) -materialista ensin
2. Suorita labit 00-03 vahvistaaksesi perusteet
3. Seuraa labit 04-06 käytännön rakentamiseksi
4. Kokeile labit 07-09 käytännön käyttöön

#### 🟡 **Keskitasoinen polku** (Jonkin verran MCP-kokemusta)
1. Tarkastele labit 00-01 tietokantakohtaisiin käsitteisiin
2. Keskity labiin 02-06 toteutuksen osalta
3. Syvenny laboreihin 07-12 edistyneisiin ominaisuuksiin

#### 🔴 **Edistynyt polku** (Kokenut MCP:n kanssa)
1. Silmäile labit 00-03 kontekstin vuoksi
2. Tarkenna labien 04-09 tietokantaintegraatioon
3. Keskity labien 10-12 tuotantoon ja käyttöönottoon

## 🛠️ Miten käyttää tätä oppimispolkua tehokkaasti

### Peräkkäinen oppiminen (Suositus)

Käy labit järjestyksessä kattavan ymmärryksen saamiseksi:

1. **Lue yleiskatsaus** - Ymmärrä mitä opit
2. **Tarkista edellytykset** - Varmista, että hallitset tarvittavan tiedon
3. **Seuraa vaiheittaisia ohjeita** - Toteuta samalla kun opit
4. **Suorita harjoitukset** - Vahvista oppimistasi
5. **Kertaa tärkeimmät opit** - Vahvista oppimistulokset

### Kohdennettu oppiminen

Tarvittaessa tiettyjä taitoja:

- **Tietokantaintegraatio**: Keskity laboreihin 04-06
- **Turvallisuuden toteutus**: Keskity laboreihin 02, 08, 12
- **AI/Semanttinen haku**: Syvenny labi 07
- **Tuotantokäyttöönotto**: Tutki labourit 10-12

### Käytännön harjoitus

Jokainen lab sisältää:
- **Toimivat koodiesimerkit** - Kopioi, muokkaa ja kokeile
- **Todelliset skenaariot** - Käytännön vähittäiskaupan analytiikan käyttötapaukset
- **Kehittyvä monimutkaisuus** - Rakentaminen yksinkertaisesta edistyneeseen
- **Validointivaiheet** - Varmista, että toteutus toimii

## 🌟 Yhteisö ja tuki

### Hanki apua

- **Azure AI Discord**: [Liity asiantuntijatukeen](https://discord.com/invite/ByRwuEEgH4)
- **GitHub-varasto ja toteutusnäyte**: [Käyttöönottomalli ja resurssit](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP-yhteisö**: [Liity laajempiin MCP-keskusteluihin](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Valmis aloittamaan?

Aloita matkasi **[Lab 00: Johdatus MCP-tietokantaintegraatioon](./00-Introduction/README.md)**

---

*Hallinnoi tuotantovalmiiden MCP-palvelimien rakentamista tietokantaintegraatiolla tämän kattavan ja käytännönläheisen oppimiskokemuksen avulla.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->