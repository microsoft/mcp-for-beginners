# 🚀 10 Microsoft MCP -palvelinta, jotka mullistavat kehittäjien tuottavuuden

## 🎯 Mitä opit tässä oppaassa

Tämä käytännön opas esittelee kymmenen Microsoftin MCP-palvelinta, jotka muuttavat aktiivisesti kehittäjien työskentelyä tekoälyavustajien kanssa. Sen sijaan, että selittäisimme vain, mitä MCP-palvelimet *voivat* tehdä, näytämme palvelimia, jotka jo tekevät todellista eroa päivittäisissä kehitysprosesseissa Microsoftilla ja sen ulkopuolella.

Jokainen tässä oppaassa esitelty palvelin on valittu todellisen käytön ja kehittäjäpalautteen perusteella. Opit paitsi mitä kukin palvelin tekee, myös miksi se on tärkeä ja miten saat siitä parhaan hyödyn omissa projekteissasi. Olitpa täysin uusi MCP:n kanssa tai haluat laajentaa nykyistä ympäristöäsi, nämä palvelimet edustavat käytännöllisimpiä ja vaikuttavimpia työkaluja Microsoftin ekosysteemissä.

> **💡 Pikavinkki**
> 
> Uusi MCP:ssä? Ei hätää! Tämä opas on suunniteltu aloittelijaystävälliseksi. Selitämme käsitteitä matkan varrella, ja voit aina palata [Johdantoon MCP:hen](../00-Introduction/README.md) ja [Peruskäsitteisiin](../01-CoreConcepts/README.md) syvempää taustaa varten.

## Yleiskatsaus

Tämä kattava opas tutkii kymmentä Microsoftin MCP-palvelinta, jotka mullistavat kehittäjien vuorovaikutuksen tekoälyavustajien ja ulkoisten työkalujen kanssa. Azure-resurssien hallinnasta dokumenttien käsittelyyn nämä palvelimet osoittavat Model Context Protocolin voiman luoda saumattomia ja tuottavia kehitysprosesseja.

## Oppimistavoitteet

Oppaan lopussa osaat:
- Ymmärtää, miten MCP-palvelimet parantavat kehittäjien tuottavuutta
- Tutustua Microsoftin vaikuttavimpiin MCP-palvelinratkaisuihin
- Löytää käytännön käyttötapauksia jokaiselle palvelimelle
- Tietää, miten palvelimet asennetaan ja konfiguroidaan VS Codessa ja Visual Studiossa
- Tutkia laajempaa MCP-ekosysteemiä ja tulevia suuntauksia

## 🔧 MCP-palvelinten ymmärtäminen: Aloittelijan opas

### Mitä MCP-palvelimet ovat?

Model Context Protocolin (MCP) aloittelijana saatat miettiä: "Mikä tarkalleen on MCP-palvelin, ja miksi se on tärkeä?" Aloitetaan yksinkertaisella vertauksella.

Ajattele MCP-palvelimia erikoistuneina avustajina, jotka auttavat tekoälykoodauskumppaniasi (kuten GitHub Copilot) yhdistymään ulkoisiin työkaluihin ja palveluihin. Aivan kuten käytät eri sovelluksia puhelimellasi eri tehtäviin – yhtä säälle, toista navigointiin, kolmatta pankkiasiointiin – MCP-palvelimet antavat tekoälyavustajallesi mahdollisuuden olla vuorovaikutuksessa eri kehitystyökalujen ja palveluiden kanssa.

### Ongelma, jonka MCP-palvelimet ratkaisevat

Ennen MCP-palvelimia, jos halusit:
- Tarkistaa Azure-resurssisi
- Luoda GitHub-ongelman
- Kysellä tietokantaasi
- Etsiä dokumentaatiosta

Sinun piti lopettaa koodaus, avata selain, siirtyä oikealle sivustolle ja tehdä nämä tehtävät manuaalisesti. Tämä jatkuva kontekstin vaihto katkaisee flow-tilasi ja heikentää tuottavuutta.

### Miten MCP-palvelimet muuttavat kehityskokemustasi

MCP-palvelimien avulla voit pysyä kehitysympäristössäsi (VS Code, Visual Studio jne.) ja pyytää tekoälyavustajaa hoitamaan nämä tehtävät. Esimerkiksi:

**Perinteisen työnkulun sijaan:**
1. Lopeta koodaus
2. Avaa selain
3. Mene Azure-portaaliin
4. Tarkista tallennustilin tiedot
5. Palaa VS Codeen
6. Jatka koodaamista

**Voit nyt tehdä näin:**
1. Kysy tekoälyltä: "Mikä on Azure-tallennustilieni tila?"
2. Jatka koodaamista saamiesi tietojen pohjalta

### Tärkeimmät hyödyt aloittelijoille

#### 1. 🔄 **Pysy flow-tilassa**
- Ei enää sovellusten välillä hyppimistä
- Keskity kirjoittamaasi koodiin
- Vähennä eri työkalujen hallinnan henkistä kuormitusta

#### 2. 🤖 **Käytä luonnollista kieltä monimutkaisten komentojen sijaan**
- Älä opettele SQL-syntaksia ulkoa, kuvaile mitä dataa tarvitset
- Älä muista Azure CLI -komentoja, kerro mitä haluat tehdä
- Anna tekoälyn hoitaa tekniset yksityiskohdat, sinä keskityt logiikkaan

#### 3. 🔗 **Yhdistä useita työkaluja**
- Luo tehokkaita työnkulkuja yhdistämällä eri palveluita
- Esimerkki: "Hae kaikki uudet GitHub-ongelmat ja luo niistä vastaavat Azure DevOps -työtehtävät"
- Rakenna automaatioita ilman monimutkaisia skriptejä

#### 4. 🌐 **Pääsy kasvavaan ekosysteemiin**
- Hyödynnä Microsoftin, GitHubin ja muiden yritysten rakentamia palvelimia
- Yhdistä eri toimittajien työkaluja saumattomasti
- Liity standardoituun ekosysteemiin, joka toimii eri tekoälyavustajien kanssa

#### 5. 🛠️ **Opiskele tekemällä**
- Aloita valmiilla palvelimilla ymmärtääksesi periaatteet
- Rakenna vähitellen omia palvelimia, kun tunnet olosi varmemmaksi
- Käytä saatavilla olevia SDK:ita ja dokumentaatiota oppimisen tukena

### Käytännön esimerkki aloittelijoille

Oletetaan, että olet uusi web-kehityksessä ja työskentelet ensimmäisen projektisi parissa. Näin MCP-palvelimet voivat auttaa:

**Perinteinen tapa:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP-palvelimien kanssa:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Yritystason standardin etu

MCP on muodostumassa alan laajuiseksi standardiksi, mikä tarkoittaa:
- **Yhtenäisyys**: Samankaltainen käyttökokemus eri työkaluissa ja yrityksissä
- **Yhteentoimivuus**: Eri toimittajien palvelimet toimivat yhdessä
- **Tulevaisuuden kestävyys**: Taidot ja asetukset siirtyvät eri tekoälyavustajien välillä
- **Yhteisö**: Laaja ekosysteemi jaettuine tietoineen ja resursseineen

### Aloittaminen: Mitä opit

Tässä oppaassa tutustumme 10 Microsoftin MCP-palvelimeen, jotka ovat erityisen hyödyllisiä kehittäjille kaikilla tasoilla. Jokainen palvelin on suunniteltu:
- Ratkaisemaan yleisiä kehityshaasteita
- Vähentämään toistuvia tehtäviä
- Parantamaan koodin laatua
- Tarjoamaan oppimismahdollisuuksia

> **💡 Oppimisvinkki**
> 
> Jos olet täysin uusi MCP:ssä, aloita [Johdannosta MCP:hen](../00-Introduction/README.md) ja [Peruskäsitteistä](../01-CoreConcepts/README.md). Palaa sitten tänne katsomaan, miten nämä käsitteet toimivat käytännössä Microsoftin työkalujen kanssa.
>
> MCP:n merkityksestä lisää voit lukea Maria Naggagan kirjoituksen: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## MCP:n käyttöönotto VS Codessa ja Visual Studiossa 🚀

Näiden MCP-palvelimien käyttöönotto on helppoa, jos käytät Visual Studio Codea tai Visual Studio 2022:ta GitHub Copilotin kanssa.

### VS Code -asennus

Perusprosessi VS Codessa:

1. **Ota käyttöön Agent-tila**: Vaihda Copilot Chat -ikkunassa Agent-tilaan
2. **Määritä MCP-palvelimet**: Lisää palvelinkonfiguraatiot VS Code -asetustiedostoon settings.json
3. **Käynnistä palvelimet**: Klikkaa "Start" jokaisen haluamasi palvelimen kohdalla
4. **Valitse työkalut**: Valitse, mitkä MCP-palvelimet otetaan käyttöön nykyisessä istunnossa

Yksityiskohtaiset asennusohjeet löytyvät [VS Code MCP -dokumentaatiosta](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Pro-vinkki: Hallitse MCP-palvelimia kuin ammattilainen!**
> 
> VS Code Extensions -näkymä sisältää nyt [kätevän uuden käyttöliittymän asennettujen MCP-palvelimien hallintaan](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Saat nopeasti käynnistettyä, pysäytettyä ja hallinnoitua palvelimia selkeän ja yksinkertaisen käyttöliittymän kautta. Kokeile!

### Visual Studio 2022 -asennus

Visual Studio 2022:ssa (versio 17.14 tai uudempi):

1. **Ota käyttöön Agent-tila**: Klikkaa GitHub Copilot Chat -ikkunan "Ask"-valikkoa ja valitse "Agent"
2. **Luo konfiguraatiotiedosto**: Luo `.mcp.json` -tiedosto ratkaisukansioon (suositeltu sijainti: `<SOLUTIONDIR>\.mcp.json`)
3. **Määritä palvelimet**: Lisää MCP-palvelinkonfiguraatiot standardin MCP-muodon mukaisesti
4. **Hyväksy työkalut**: Kun sinulta kysytään, hyväksy käytettävät työkalut asianmukaisilla käyttöoikeuksilla

Yksityiskohtaiset Visual Studio -asennusohjeet löytyvät [Visual Studio MCP -dokumentaatiosta](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Jokaisella MCP-palvelimella on omat konfiguraatiovaatimuksensa (yhteysmerkkijonot, todennus jne.), mutta asennusmalli on molemmissa IDE:issä yhtenäinen.

## Opetus Microsoftin MCP-palvelimista 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mitä se tekee**: Microsoft Learn Docs MCP Server on pilvipalvelu, joka tarjoaa tekoälyavustajille reaaliaikaisen pääsyn viralliseen Microsoft-dokumentaatioon Model Context Protocolin kautta. Se yhdistyy osoitteeseen `https://learn.microsoft.com/api/mcp` ja mahdollistaa semanttisen haun Microsoft Learnin, Azure-dokumentaation, Microsoft 365 -dokumentaation ja muiden virallisten Microsoft-lähteiden yli.

**Miksi se on hyödyllinen**: Vaikka se saattaa vaikuttaa "vain dokumentaatiolta", tämä palvelin on itse asiassa ratkaisevan tärkeä jokaiselle Microsoft-teknologioita käyttävälle kehittäjälle. Yksi suurimmista valituksista .NET-kehittäjiltä tekoälykoodausavustajista on, etteivät ne ole ajan tasalla uusimmista .NET- ja C#-julkaisuista. Microsoft Learn Docs MCP Server ratkaisee tämän tarjoamalla reaaliaikaisen pääsyn ajantasaisimpaan dokumentaatioon, API-viitteisiin ja parhaisiin käytäntöihin. Olitpa sitten työskentelemässä uusimpien Azure SDK:iden kanssa, tutkimassa uusia C# 13 -ominaisuuksia tai toteuttamassa huippuluokan .NET Aspire -malleja, tämä palvelin varmistaa, että tekoälyavustajallasi on pääsy auktoritatiiviseen ja ajantasaiseen tietoon, jonka avulla se voi luoda tarkkaa ja modernia koodia.

**Käytännön käyttö**: "Mitkä ovat az cli -komennot Azure Container Appin luomiseen virallisen Microsoft Learn -dokumentaation mukaan?" tai "Miten konfiguroin Entity Frameworkin riippuvuussyötön ASP.NET Core -sovelluksessa?" Tai entä "Tarkista tämä koodi varmistaaksesi, että se vastaa Microsoft Learn -dokumentaation suorituskykysuosituksia." Palvelin tarjoaa kattavan haun Microsoft Learnin, Azure-dokumentaation ja Microsoft 365 -dokumentaation yli käyttäen edistynyttä semanttista hakua löytääkseen kontekstuaalisesti relevantimmat tiedot. Se palauttaa jopa 10 korkealaatuista sisältölohkoa artikkelien otsikoineen ja URL-osoitteineen, aina pääsyllä uusimpaan Microsoft-dokumentaatioon heti julkaisun jälkeen.

**Esimerkkitapaus**: Palvelin tarjoaa `microsoft_docs_search` -työkalun, joka suorittaa semanttisen haun Microsoftin viralliseen tekniseen dokumentaatioon. Kun palvelin on konfiguroitu, voit kysyä esimerkiksi "Miten toteutan JWT-todennuksen ASP.NET Core -sovelluksessa?" ja saada yksityiskohtaisia, virallisia vastauksia lähde-linkkeineen. Haun laatu on erinomainen, koska se ymmärtää kontekstin – kysymys "containers" Azure-kontekstissa palauttaa Azure Container Instances -dokumentaation, kun taas sama termi .NET-kontekstissa palauttaa C#-kokoelmiin liittyvää tietoa.

Tämä on erityisen hyödyllistä nopeasti muuttuvien tai äskettäin päivitettyjen kirjastojen ja käyttötapausten kohdalla. Esimerkiksi joissain viimeaikaisissa koodausprojekteissani halusin hyödyntää ominaisuuksia uusimmista .NET Aspire- ja Microsoft.Extensions.AI -julkaisuista. Sisällyttämällä Microsoft Learn Docs MCP -palvelimen pystyin hyödyntämään paitsi API-dokumentaatiota myös juuri julkaistuja opastuksia ja ohjeita.
> **💡 Vinkki ammattilaisille**
> 
> Myös työkaluystävälliset mallit tarvitsevat kannustusta MCP-työkalujen käyttöön! Harkitse järjestelmäkehotteen tai [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) lisäämistä, esimerkiksi: "Sinulla on pääsy `microsoft.docs.mcp` -työkaluun – käytä tätä työkalua etsiäksesi Microsoftin uusinta virallista dokumentaatiota, kun käsittelet kysymyksiä Microsoftin teknologioista kuten C#, Azure, ASP.NET Core tai Entity Framework."
>
> Erinomainen esimerkki tästä löytyy [C# .NET Janitor chat -tilasta](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) Awesome GitHub Copilot -varastosta. Tämä tila hyödyntää erityisesti Microsoft Learn Docs MCP -palvelinta auttaakseen siistimään ja modernisoimaan C#-koodia uusimpien mallien ja parhaiden käytäntöjen mukaisesti.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mitä se tekee**: Azure MCP Server on kattava kokoelma yli 15 erikoistunutta Azure-palveluliitintä, jotka tuovat koko Azure-ekosysteemin osaksi AI-työnkulkua. Tämä ei ole pelkkä yksittäinen palvelin – se on tehokas paketti, joka sisältää resurssien hallinnan, tietokantayhteydet (PostgreSQL, SQL Server), Azure Monitorin lokianalyysin KQL:llä, Cosmos DB -integraation ja paljon muuta.

**Miksi se on hyödyllinen**: Pelkän Azure-resurssien hallinnan lisäksi tämä palvelin parantaa merkittävästi koodin laatua työskennellessäsi Azure SDK:iden kanssa. Kun käytät Azure MCP:tä Agent-tilassa, se ei vain auta sinua kirjoittamaan koodia – se auttaa sinua kirjoittamaan *parempaa* Azure-koodia, joka noudattaa nykyisiä todennuskäytäntöjä, virheenkäsittelyn parhaita käytäntöjä ja hyödyntää uusimpia SDK-ominaisuuksia. Sen sijaan, että saisit geneeristä koodia, joka saattaa toimia, saat koodia, joka noudattaa Azuren suositeltuja malleja tuotantokuormituksissa.

**Keskeiset moduulit sisältävät**:
- **🗄️ Tietokantaliittimet**: Luonnollisen kielen suora pääsy Azure Database for PostgreSQL:ään ja SQL Serveriin
- **📊 Azure Monitor**: KQL-pohjainen lokianalyysi ja operatiiviset näkymät
- **🌐 Resurssien hallinta**: Täysi Azure-resurssien elinkaaren hallinta
- **🔐 Todennus**: DefaultAzureCredential ja hallinnoidut identiteettimallit
- **📦 Tallennuspalvelut**: Blob Storage, Queue Storage ja Table Storage -toiminnot
- **🚀 Konttipalvelut**: Azure Container Apps, Container Instances ja AKS-hallinta
- **Ja monia muita erikoistuneita liittimiä**

**Käytännön esimerkkejä**: "Listaa Azure-tallennustilini tilit", "Kysy Log Analytics -työtilastani virheitä viimeisen tunnin ajalta" tai "Auta minua rakentamaan Azure-sovellus Node.js:llä oikealla todennuksella"

**Täysi demoesimerkki**: Tässä on kattava läpikäynti, joka näyttää Azure MCP:n ja GitHub Copilot for Azure -laajennuksen yhdistämisen voiman VS Codessa. Kun molemmat ovat asennettuina ja annat kehotteen:

> "Luo Python-skripti, joka lataa tiedoston Azure Blob Storageen käyttäen DefaultAzureCredential-todennusta. Skriptin tulee yhdistää Azure-tallennustililleni nimeltä 'mycompanystorage', ladata tiedosto 'documents'-konttiin, luoda testitiedosto nykyisellä aikaleimalla ladattavaksi, käsitellä virheet sujuvasti ja antaa informatiivista palautetta, noudattaa Azuren parhaita käytäntöjä todennuksessa ja virheenkäsittelyssä, sisältää kommentteja, jotka selittävät DefaultAzureCredential-todennuksen toimintaa, ja tehdä skriptistä hyvin jäsennelty funktioineen ja dokumentaation kera."

Azure MCP Server luo täydellisen, tuotantovalmiin Python-skriptin, joka:
- Käyttää uusinta Azure Blob Storage SDK:ta oikeilla async-malleilla
- Toteuttaa DefaultAzureCredentialin kattavalla varajärjestelmän selityksellä
- Sisältää vankan virheenkäsittelyn erityyppisillä Azure-poikkeuksilla
- Noudattaa Azure SDK:n parhaita käytäntöjä resurssien ja yhteyksien hallinnassa
- Tarjoaa yksityiskohtaisen lokituksen ja informatiivisen konsolitulosteen
- Luo hyvin jäsennellyn skriptin funktioineen, dokumentaation ja tyyppivihjeineen

Merkittävää on se, että ilman Azure MCP:tä saatat saada geneeristä blob storage -koodia, joka toimii, mutta ei noudata nykyisiä Azure-malleja. Azure MCP:n kanssa saat koodia, joka hyödyntää uusimpia todennusmenetelmiä, käsittelee Azure-spesifisiä virhetilanteita ja noudattaa Microsoftin suosituksia tuotantosovelluksissa.

**Esimerkkitapaus**: Minulla on ollut vaikeuksia muistaa tarkat komennot `az` ja `azd` CLI:lle ad-hoc-käytössä. Se on aina kahden vaiheen prosessi: ensin etsin syntaksin, sitten suoritan komennon. Usein menen vain portaalille ja klikkailen, koska en halua myöntää, etten muista CLI-syntaksia. Mahdollisuus vain kuvailla haluamani asia on mahtavaa, ja vielä parempi, että sen voi tehdä ilman, että tarvitsee poistua IDE:stä!

[Azure MCP -repositoriossa](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) on erinomainen lista käyttötapauksista aloittamiseen. Kattavia asennusohjeita ja edistyneitä konfigurointivaihtoehtoja löydät [virallisesta Azure MCP -dokumentaatiosta](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mitä se tekee**: Virallinen GitHub MCP Server tarjoaa saumattoman integraation GitHubin koko ekosysteemiin, tarjoten sekä isännöidyn etäkäytön että paikallisen Docker-asennuksen vaihtoehdot. Tämä ei ole pelkkää perusvaraston hallintaa – se on kattava työkalupakki, joka sisältää GitHub Actions -hallinnan, pull request -työnkulut, issue-seurannan, tietoturvaskannauksen, ilmoitukset ja edistyneet automaatiomahdollisuudet.

**Miksi se on hyödyllinen**: Tämä palvelin muuttaa tapasi olla vuorovaikutuksessa GitHubin kanssa tuomalla koko alustan kokemuksen suoraan kehitysympäristöösi. Sen sijaan, että vaihtelisit jatkuvasti VS Coden ja GitHub.comin välillä projektinhallintaan, koodikatselmuksiin ja CI/CD-seurantaan, voit hoitaa kaiken luonnollisen kielen komennoilla samalla kun pysyt keskittyneenä koodiin.

> **ℹ️ Huom:** Eri tyyppiset 'Agentit'  
>  
> Älä sekoita tätä GitHub MCP Serveriä GitHubin Coding Agenttiin (AI-agentti, jolle voi osoittaa issueita automatisoituihin kooditehtäviin). GitHub MCP Server toimii VS Coden Agent-tilassa tarjoten GitHub API -integraation, kun taas Coding Agent on erillinen ominaisuus, joka luo pull requesteja, kun se on osoitettu GitHub-issueille.

**Keskeiset ominaisuudet sisältävät**:
- **⚙️ GitHub Actions**: Täydellinen CI/CD-putken hallinta, työnkulkujen seuranta ja artefaktien käsittely
- **🔀 Pull Requests**: Luo, tarkista, yhdistä ja hallitse PR:itä kattavalla tilaseurannalla
- **🐛 Issues**: Täysi issue-elinkaaren hallinta, kommentointi, merkintä ja osoittaminen
- **🔒 Tietoturva**: Koodiskannauksen hälytykset, salaisuuksien tunnistus ja Dependabot-integraatio
- **🔔 Ilmoitukset**: Älykäs ilmoitusten hallinta ja varastotilausten ohjaus
- **📁 Varaston hallinta**: Tiedostotoiminnot, haarojen hallinta ja varaston ylläpito
- **👥 Yhteistyö**: Käyttäjä- ja organisaatiohaku, tiimien hallinta ja käyttöoikeuksien valvonta

**Käytännön esimerkkejä**: "Luo pull request ominaisuushaarastani", "Näytä kaikki epäonnistuneet CI-ajot tällä viikolla", "Listaa avoimet tietoturvahälytykset varastoilleni" tai "Etsi kaikki minulle osoitetut issueet organisaatioissani"

**Täysi demoesimerkki**: Tässä on tehokas työnkulku, joka demonstroi GitHub MCP Serverin kyvykkyyksiä:

> "Minun täytyy valmistautua sprinttikatsaukseen. Näytä kaikki tämän viikon luomani pull requestit, tarkista CI/CD-putkiemme tila, tee yhteenveto mahdollisista tietoturvahälytyksistä, jotka meidän pitää käsitellä, ja auta minua laatimaan julkaisumuistiinpanot yhdistettyjen 'feature'-tunnisteisten PR:ien perusteella."

GitHub MCP Server:
- Kysyy viimeisimmät pull requestisi yksityiskohtaisine tilatietoineen
- Analysoi työnkulkujen ajot ja korostaa mahdolliset virheet tai suorituskykyongelmat
- Kokoaa tietoturvaskannauksen tulokset ja priorisoi kriittiset hälytykset
- Luo kattavat julkaisumuistiinpanot poimimalla tiedot yhdistetyistä PR:istä
- Tarjoaa konkreettisia seuraavia askeleita sprintin suunnitteluun ja julkaisun valmisteluun

**Esimerkkitapaus**: Käytän tätä paljon koodikatselmuksissa. Sen sijaan, että hyppisin VS Coden, GitHub-ilmoitusten ja pull request -sivujen välillä, voin sanoa "Näytä kaikki PR:t, jotka odottavat minun tarkistustani" ja sitten "Lisää kommentti PR:ään #123 kysyen virheenkäsittelystä todennusmenetelmässä." Palvelin hoitaa GitHub API -kutsut, ylläpitää keskustelun kontekstin ja auttaa jopa muotoilemaan rakentavampia katselmointikommentteja.

**Todennusvaihtoehdot**: Palvelin tukee sekä OAuthia (saumaton VS Codessa) että Personal Access Tokenia, ja voit konfiguroida työkalusarjat käyttöösi vain tarvitsemasi GitHub-toiminnot varten. Voit ajaa sen etäpalveluna nopeaan käyttöönottoon tai paikallisesti Dockerilla täydelliseen hallintaan.

> **💡 Vinkki**  
>  
> Ota käyttöön vain tarvitsemasi työkalusarjat määrittämällä `--toolsets` -parametri MCP-palvelimen asetuksissa, jotta kontekstin koko pienenee ja AI-työkalujen valinta paranee. Esimerkiksi lisää `"--toolsets", "repos,issues,pull_requests,actions"` MCP-konfiguraation argumentteihin ydinkehitystyönkulkuja varten, tai käytä `"--toolsets", "notifications, security"` jos haluat pääasiassa GitHubin valvontamahdollisuuksia.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mitä se tekee**: Yhdistää Azure DevOps -palveluihin tarjoten kattavan projektinhallinnan, työtehtävien seurannan, build-putkien hallinnan ja varaston operoinnin.

**Miksi se on hyödyllinen**: Tiimeille, jotka käyttävät Azure DevOpsia ensisijaisena DevOps-alustanaan, tämä MCP-palvelin poistaa jatkuvan välilehtien vaihdon kehitysympäristön ja Azure DevOpsin web-käyttöliittymän välillä. Voit hallita työtehtäviä, tarkistaa buildien tilat, kysellä varastoja ja hoitaa projektinhallintatehtäviä suoraan AI-avustajaltasi.

**Käytännön esimerkkejä**: "Näytä kaikki aktiiviset työtehtävät tämän sprintin aikana WebApp-projektissa", "Luo bugiraportti juuri löytämästäni kirjautumisongelmasta" tai "Tarkista build-putkiemme tila ja näytä viimeisimmät epäonnistumiset"

**Esimerkkitapaus**: Voit helposti tarkistaa tiimisi nykyisen sprintin tilan yksinkertaisella kyselyllä kuten "Näytä kaikki aktiiviset työtehtävät tämän sprintin aikana WebApp-projektissa" tai "Luo bugiraportti juuri löytämästäni kirjautumisongelmasta" ilman, että poistut kehitysympäristöstäsi.

### 5. 📝 MarkItDown MCP Server
[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mitä se tekee**: MarkItDown on kattava dokumenttien muunnospalvelin, joka muuntaa erilaiset tiedostomuodot korkealaatuiseksi Markdowniksi, optimoituna LLM-käyttöön ja tekstianalyysityönkulkuihin.

**Miksi se on hyödyllinen**: Välttämätön nykyaikaisissa dokumentaatiotyönkuluissa! MarkItDown käsittelee vaikuttavan määrän tiedostomuotoja säilyttäen samalla tärkeän dokumenttien rakenteen, kuten otsikot, listat, taulukot ja linkit. Toisin kuin yksinkertaiset tekstinpoistotyökalut, se keskittyy säilyttämään semanttisen merkityksen ja muotoilun, joka on arvokasta sekä tekoälyn käsittelyssä että ihmisen luettavuudessa.

**Tuetut tiedostomuodot**:
- **Office-dokumentit**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Mediatiedostot**: Kuvat (EXIF-metatiedolla ja OCR:llä), Ääni (EXIF-metatiedolla ja puheen transkriptiolla)
- **Verkkosisältö**: HTML, RSS-syötteet, YouTube-URL:t, Wikipedia-sivut
- **Tietomuodot**: CSV, JSON, XML, ZIP-tiedostot (käsittelee sisällön rekursiivisesti)
- **Julkaisumuodot**: EPub, Jupyter-muistikirjat (.ipynb)
- **Sähköposti**: Outlook-viestit (.msg)
- **Edistynyt**: Azure Document Intelligence -integraatio parannettuun PDF-käsittelyyn

**Edistyneet ominaisuudet**: MarkItDown tukee LLM-pohjaisia kuvailuja (kun käytössä on OpenAI-asiakas), Azure Document Intelligencea parannettuun PDF-käsittelyyn, puheen transkriptiota äänisisällöille sekä laajennusjärjestelmää lisätiedostomuotojen tukemiseksi.

**Käytännön esimerkkejä**: "Muunna tämä PowerPoint-esitys Markdowniksi dokumentaatiosivustollemme", "Pura teksti tästä PDF:stä oikeilla otsikkorakenteilla" tai "Muunna tämä Excel-taulukko luettavaan taulukkomuotoon"

**Esimerkkilainaus**: Siteeraten [MarkItDown-dokumentaatiota](https://github.com/microsoft/markitdown#why-markdown):


> Markdown on erittäin lähellä pelkkää tekstiä, siinä on vain vähän merkintöjä tai muotoiluja, mutta se tarjoaa silti tavan esittää tärkeä dokumenttien rakenne. Suositut LLM-mallit, kuten OpenAI:n GPT-4o, "puhuvat" luonnostaan Markdownia ja usein käyttävät sitä vastauksissaan ilman erillistä kehotusta. Tämä viittaa siihen, että ne on koulutettu valtavilla määrillä Markdown-muotoiltua tekstiä ja ymmärtävät sitä hyvin. Lisäksi Markdownin käytännöt ovat erittäin token-tehokkaita.

MarkItDown on todella hyvä säilyttämään dokumenttien rakenteen, mikä on tärkeää tekoälytyönkuluissa. Esimerkiksi PowerPoint-esitystä muuntaessa se säilyttää diojen järjestyksen oikeilla otsikoilla, purkaa taulukot Markdown-taulukoiksi, lisää kuville vaihtoehtoisen tekstin ja käsittelee jopa puhujan muistiinpanot. Kaaviot muunnetaan luettaviksi datataulukoiksi, ja lopullinen Markdown säilyttää alkuperäisen esityksen loogisen rakenteen. Tämä tekee siitä täydellisen työkalun esityssisällön syöttämiseen tekoälyjärjestelmiin tai dokumentaation luomiseen olemassa olevista dioista.

### 6. 🗃️ SQL Server MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mitä se tekee**: Tarjoaa keskustelukäyttöliittymän SQL Server -tietokantoihin (paikalliset, Azure SQL tai Fabric)

**Miksi se on hyödyllinen**: Vastaava kuin PostgreSQL-palvelin, mutta Microsoft SQL -ekosysteemille. Yhdistä yksinkertaisella yhteysmerkkijonolla ja aloita kyselyt luonnollisella kielellä – ei enää kontekstin vaihtoa!

**Käytännön esimerkki**: "Etsi kaikki tilaukset, joita ei ole täytetty viimeisen 30 päivän aikana" käännetään sopiviksi SQL-kyselyiksi ja palauttaa muotoillut tulokset

**Esimerkkitapaus**: Kun olet määrittänyt tietokantayhteyden, voit aloittaa keskustelun tietojesi kanssa välittömästi. Blogikirjoitus näyttää tämän yksinkertaisella kysymyksellä: "mihin tietokantaan olet yhteydessä?" MCP-palvelin vastaa kutsumalla oikean tietokantatyökalun, yhdistämällä SQL Server -instanssiisi ja palauttamalla tiedot nykyisestä tietokantayhteydestä – ilman yhtään SQL-riviä. Palvelin tukee kattavia tietokantaoperaatioita skeeman hallinnasta datan käsittelyyn, kaikki luonnollisen kielen kehotteilla. Täydelliset asennusohjeet ja konfiguraatioesimerkit VS Coden ja Claude Desktopin kanssa löytyvät osoitteesta: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mitä se tekee**: Mahdollistaa tekoälyagenttien vuorovaikutuksen verkkosivujen kanssa testauksessa ja automaatiossa

> **ℹ️ GitHub Copilotin voimanlähde**
> 
> Playwright MCP Server tukee GitHub Copilotin Coding Agentia, antaen sille verkkoselausmahdollisuudet! [Lue lisää tästä ominaisuudesta](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miksi se on hyödyllinen**: Täydellinen luonnollisen kielen kuvauksilla ohjattuun automaattiseen testaukseen. Tekoäly voi navigoida verkkosivuilla, täyttää lomakkeita ja poimia tietoa rakenteellisten saavutettavuuskuvausten avulla – tämä on todella tehokasta!

**Käytännön esimerkki**: "Testaa kirjautumisprosessi ja varmista, että hallintapaneeli latautuu oikein" tai "Luo testi, joka hakee tuotteita ja tarkistaa tulossivun" – kaikki ilman sovelluksen lähdekoodin tarvetta

**Esimerkkitapaus**: Työkaverini Debbie O'Brien on tehnyt mahtavaa työtä Playwright MCP Serverin kanssa viime aikoina! Esimerkiksi hän näytti äskettäin, miten voi luoda täydellisiä Playwright-testejä ilman pääsyä sovelluksen lähdekoodiin. Hänen tapauksessaan hän pyysi Copilotia tekemään testin elokuvahakusovellukselle: siirry sivustolle, hae "Garfield" ja varmista, että elokuva näkyy tuloksissa. MCP käynnisti selaimen, tutki sivun rakennetta DOM-kuvien avulla, löysi oikeat valitsimet ja loi täysin toimivan TypeScript-testin, joka läpäisi ensimmäisellä ajolla.

Tämä on todella tehokasta, koska se yhdistää luonnollisen kielen ohjeet suoritettavaan testikoodiin. Perinteisesti testit kirjoitetaan manuaalisesti tai tarvitaan pääsy koodipohjaan kontekstin saamiseksi. Playwright MCP:n avulla voit testata ulkoisia sivustoja, asiakasohjelmia tai toimia mustalaatikkotestauksessa, jossa koodiin ei ole pääsyä.

### 8. 💻 Dev Box MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mitä se tekee**: Hallinnoi Microsoft Dev Box -ympäristöjä luonnollisen kielen avulla

**Miksi se on hyödyllinen**: Yksinkertaistaa kehitysympäristöjen hallintaa valtavasti! Luo, konfiguroi ja hallitse kehitysympäristöjä ilman, että tarvitsee muistaa tarkkoja komentoja.

**Käytännön esimerkki**: "Luo uusi Dev Box uusimmalla .NET SDK:lla ja konfiguroi se projektiamme varten", "Tarkista kaikkien kehitysympäristöjeni tila" tai "Luo standardoitu demo-ympäristö tiimimme esityksiä varten"

**Esimerkkitapaus**: Olen suuri Dev Boxin käyttäjä henkilökohtaisessa kehityksessä. Oivallukseni syntyi, kun James Montemagno kertoi, miten erinomainen Dev Box on konferenssidemoihin, koska siinä on supernopea ethernet-yhteys riippumatta siitä, millaista konferenssin, hotellin tai lentokoneen wifiä käytän. Itse asiassa harjoittelin äskettäin konferenssidemoa, kun kannettava tietokoneeni oli yhdistetty puhelimeni hotspotin kautta bussissa Brugesta Antwerpeniin! Seuraava tavoitteeni on syventyä tiimien monien kehitysympäristöjen hallintaan ja standardoituihin demo-ympäristöihin. Toinen iso käyttötapaus, josta olen kuullut asiakkailta ja työkavereilta, on Dev Boxin käyttö esikonfiguroiduissa kehitysympäristöissä. Molemmissa tapauksissa MCP:n käyttö Dev Boxien konfigurointiin ja hallintaan mahdollistaa luonnollisen kielen vuorovaikutuksen, kaikki samalla kun pysyt kehitysympäristössäsi.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Mitä se tekee**: Azure AI Foundry MCP Server tarjoaa kehittäjille laajat mahdollisuudet Azure AI -ekosysteemiin, mukaan lukien mallikatalogit, käyttöönoton hallinnan, tiedon indeksoinnin Azure AI Searchin avulla sekä arviointityökalut. Tämä kokeellinen palvelin yhdistää AI-kehityksen ja Azuren tehokkaan AI-infrastruktuurin, tehden AI-sovellusten rakentamisesta, käyttöönotosta ja arvioinnista helpompaa.

**Miksi se on hyödyllinen**: Tämä palvelin muuttaa tapaa, jolla työskentelet Azure AI -palveluiden kanssa, tuomalla yritystason AI-ominaisuudet suoraan kehitystyöhöysi. Sen sijaan, että vaihtaisit Azure-portaalin, dokumentaation ja IDE:n välillä, voit löytää malleja, ottaa palveluita käyttöön, hallita tietokantoja ja arvioida AI:n suorituskykyä luonnollisen kielen komennoilla. Se on erityisen tehokas kehittäjille, jotka rakentavat RAG (Retrieval-Augmented Generation) -sovelluksia, hallinnoivat monimallisia käyttöönottoja tai toteuttavat kattavia AI-arviointiputkia.

**Keskeiset kehittäjäominaisuudet**:
- **🔍 Mallien löytäminen ja käyttöönotto**: Tutki Azure AI Foundryn mallikatalogia, saa yksityiskohtaista mallin tietoa koodiesimerkkien kera ja ota malleja käyttöön Azure AI Services -palveluissa
- **📚 Tiedonhallinta**: Luo ja hallitse Azure AI Search -indeksejä, lisää dokumentteja, määritä indeksoijat ja rakenna kehittyneitä RAG-järjestelmiä
- **⚡ AI-agenttien integrointi**: Yhdistä Azure AI Agentteihin, kysy olemassa olevilta agenteilta ja arvioi agenttien suorituskykyä tuotantotilanteissa
- **📊 Arviointikehys**: Suorita kattavia tekstin ja agenttien arviointeja, luo markdown-raportteja ja toteuta laadunvarmistusta AI-sovelluksille
- **🚀 Prototyyppityökalut**: Saat asennusohjeet GitHub-pohjaiseen prototypointiin ja pääsyn Azure AI Foundry Labsin huippututkimusmalleihin

**Käytännön esimerkkejä kehittäjille**: "Ota Phi-4-malli käyttöön Azure AI Services -palvelussa sovellustani varten", "Luo uusi hakemisto dokumentaation RAG-järjestelmää varten", "Arvioi agenttini vastaukset laadun mittareita vasten" tai "Löydä paras päättelymalli monimutkaisiin analyysitehtäviini"

**Täysi demo-skenaario**: Tässä on tehokas AI-kehitystyönkulku:


> "Rakennan asiakastukirobottia. Auta minua löytämään hyvä päättelymalli katalogista, ottamaan se käyttöön Azure AI Services -palvelussa, luomaan tietopohja dokumentaatiostamme, perustamaan arviointikehys vastausten laadun testaamiseksi ja auttamaan prototyypin tekemisessä GitHub-tokenin avulla testaukseen."

Azure AI Foundry MCP Server:
- Kysyy mallikatalogia suositellakseen parhaita päättelymalleja tarpeidesi mukaan
- Tarjoaa käyttöönotto-komennot ja käyttökiintiöt valitsemallesi Azure-alueelle
- Määrittää Azure AI Search -indeksit oikealla skeemalla dokumentaatiollesi
- Konfiguroi arviointiputket laadun mittareilla ja turvallisuustarkistuksilla
- Luo prototyyppikoodin GitHub-todennuksella välittömään testaukseen
- Tarjoaa kattavat asennusoppaat juuri sinun teknologiapinoosi sopivina

**Esimerkkitarina**: Kehittäjänä minulla on ollut vaikeuksia pysyä perillä eri LLM-malleista. Tunnen muutaman päämallin, mutta olen tuntenut jääväni paitsi tuottavuuden ja tehokkuuden parannuksista. Tokenit ja kiintiöt ovat stressaavia ja vaikeita hallita – en koskaan tiedä, valitsenko oikean mallin oikeaan tehtävään vai kulutanko budjettini tehottomasti. Kuulin tästä MCP Serveristä James Montemagnolta, kun kyselin tiimikavereilta suosituksia MCP Servereistä tätä postausta varten, ja olen innoissani päästessäni käyttämään sitä! Mallien löytäminen näyttää erityisen vaikuttavalta minulle, joka haluan tutkia tavallisten mallien ulkopuolelle ja löytää tehtäviin optimoituja malleja. Arviointikehys auttaa minua varmistamaan, että saan oikeasti parempia tuloksia, en vain kokeile jotain uutta kokeilun vuoksi.

> **ℹ️ Kokeellinen tila**
> 
> Tämä MCP-palvelin on kokeellinen ja aktiivisessa kehityksessä. Ominaisuudet ja API:t voivat muuttua. Erinomainen Azure AI -ominaisuuksien tutkimiseen ja prototyyppien rakentamiseen, mutta varmista vakausvaatimukset tuotantokäyttöön.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Mitä se tekee**: Tarjoaa kehittäjille olennaiset työkalut AI-agenttien ja sovellusten rakentamiseen, jotka integroituvat Microsoft 365:een ja Microsoft 365 Copilotiin, mukaan lukien skeeman validointi, esimerkkikoodin haku ja vianmääritystuki.

**Miksi se on hyödyllinen**: Microsoft 365:lle ja Copilotille kehittäminen vaatii monimutkaisia manifest-skeemoja ja erityisiä kehityskäytäntöjä. Tämä MCP-palvelin tuo olennaiset kehitysvälineet suoraan koodausympäristöösi, auttaen sinua validoimaan skeemoja, löytämään esimerkkikoodeja ja ratkaisemaan yleisiä ongelmia ilman jatkuvaa dokumentaation selaamista.

**Käytännön esimerkkejä**: "Validoi deklaratiivinen agenttimanifestini ja korjaa skeemavirheet", "Näytä esimerkkikoodi Microsoft Graph API -laajennuksen toteuttamiseen" tai "Auta minua vianmäärityksessä Teams-sovellukseni todennuksessa"

**Esimerkkitarina**: Otin yhteyttä ystävääni John Milleriin, kun juttelimme Build-tapahtumassa M365 Agentseista, ja hän suositteli tätä MCP:tä. Tämä voi olla erinomainen kehittäjille, jotka ovat uusia M365 Agentseissa, sillä se tarjoaa malleja, esimerkkikoodeja ja pohjia aloittamiseen ilman, että hukkuu dokumentaatioon. Skeeman validointiominaisuudet näyttävät erityisen hyödyllisiltä manifestin rakenteellisten virheiden välttämiseen, jotka voivat aiheuttaa tuntikausia vianetsintää.

> **💡 Vinkki**
> 
> Käytä tätä palvelinta yhdessä Microsoft Learn Docs MCP Serverin kanssa saadaksesi kattavan M365-kehitystuen – toinen tarjoaa virallisen dokumentaation, tämä käytännön kehitystyökalut ja vianmäärityksen.

## Mitä seuraavaksi? 🔮

## 📋 Yhteenveto

Model Context Protocol (MCP) muuttaa tapaa, jolla kehittäjät ovat vuorovaikutuksessa AI-avustajien ja ulkoisten työkalujen kanssa. Nämä 10 Microsoft MCP -palvelinta osoittavat standardoidun AI-integraation voiman, mahdollistaen saumattomat työnkulut, jotka pitävät kehittäjät flow-tilassa samalla kun he pääsevät käsiksi tehokkaisiin ulkoisiin ominaisuuksiin.

Laajasta Azure-ekosysteemin integraatiosta erikoistyökaluihin kuten Playwright selaimen automaatioon ja MarkItDown dokumenttien käsittelyyn, nämä palvelimet näyttävät, miten MCP voi parantaa tuottavuutta monipuolisissa kehitystilanteissa. Standardoitu protokolla varmistaa, että nämä työkalut toimivat yhdessä saumattomasti, luoden yhtenäisen kehityskokemuksen.

MCP-ekosysteemin kehittyessä aktiivinen osallistuminen yhteisöön, uusien palvelimien tutkiminen ja räätälöityjen ratkaisujen rakentaminen ovat avainasemassa kehitystuottavuuden maksimoimiseksi. MCP:n avoimen standardin luonteen ansiosta voit yhdistellä eri toimittajien työkaluja luodaksesi juuri sinun tarpeisiisi sopivan työnkulun.

## 🔗 Lisäresurssit

- [Official Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Events](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29th/30th July or watch on Demand ](https://aka.ms/mcpdevdays)

## 🎯 Harjoitukset

1. **Asenna ja konfiguroi**: Ota käyttöön yksi MCP-palvelimista VS Code -ympäristössäsi ja testaa perustoiminnallisuudet.
2. **Työnkulun integrointi**: Suunnittele kehitystyönkulku, joka yhdistää vähintään kolme eri MCP-palvelinta.
3. **Oman palvelimen suunnittelu**: Tunnista päivittäisessä kehitystyössäsi tehtävä, joka hyötyisi räätälöidystä MCP-palvelimesta, ja laadi sille määrittely.
4. **Suorituskyvyn analyysi**: Vertaa MCP-palvelimien käyttöä perinteisiin menetelmiin yleisissä kehitystehtävissä.
5. **Turvallisuusarviointi**: Arvioi MCP-palvelimien käytön turvallisuusvaikutukset kehitysympäristössäsi ja ehdota parhaita käytäntöjä.

Seuraava: [Best Practices](../08-BestPractices/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.