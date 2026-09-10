# 🚀 10 Microsoft MCP -palvelinta, jotka muuttavat kehittäjien tuottavuutta

## 🎯 Mitä opit tässä oppaassa

Tämä käytännön opas esittelee kymmenen Microsoftin MCP-palvelinta, jotka aktiivisesti muuttavat kehittäjien työtapoja AI-avustajien kanssa. Sen sijaan, että selittäisimme vain, mitä MCP-palvelimet *voivat* tehdä, näytämme palvelimia, jotka jo tekemällä todellisen eron päivittäisissä kehitysprosesseissa Microsoftilla ja muualla.

Jokainen tässä oppaassa oleva palvelin on valittu todelliseen käyttöön ja kehittäjäpalautteen perusteella. Saat selville, mitä kukin palvelin tekee, miksi se on merkityksellinen ja miten saat siitä parhaan hyödyn omissa projekteissasi. Olitpa sitten täysin uusi MCP:n kanssa tai haluat laajentaa nykyistä ympäristöösi, nämä palvelimet edustavat käytännöllisimpiä ja vaikuttavimpia työkaluja Microsoftin ekosysteemissä.

> **💡 Pikavinkki**
> 
> Uusi MCP:n parissa? Ei hätää! Tämä opas on suunniteltu aloittelijaystävälliseksi. Selitämme käsitteitä matkan varrella, ja voit aina palata takaisin lukemaan [MCP:n johdanto](../00-Introduction/README.md) ja [Peruskäsitteet](../01-CoreConcepts/README.md) moduuleja syvempää taustatietoa varten.

## Yleiskatsaus

Tämä kattava opas tutkii kymmentä Microsoft MCP -palvelinta, jotka mullistavat tapaa, jolla kehittäjät ovat vuorovaikutuksessa AI-avustajien ja ulkoisten työkalujen kanssa. Azuren resurssien hallinnasta asiakirjojen käsittelyyn nämä palvelimet osoittavat Model Context Protocolin tehon luoda saumattomia, tuottavia kehitystyönkulkuja.

## Oppimistavoitteet

Oppaan lopussa osaat:
- Ymmärtää, miten MCP-palvelimet parantavat kehittäjien tuottavuutta
- Oppia Microsoftin vaikuttavimmista MCP-palvelinratkaisuista
- Löytää käytännön käyttötapaukset jokaiselle palvelimelle
- Tietää, miten palvelimet otetaan käyttöön ja konfiguroidaan VS Codessa ja Visual Studiossa
- Tutustua laajempaan MCP-ekosysteemiin ja tuleviin suuntiin

## 🔧 MCP-palvelinten ymmärtäminen: Aloittelijan opas

### Mitä MCP-palvelimet ovat?

MCP:n aloittelijana saatat miettiä: "Mikä täsmälleen on MCP-palvelin, ja miksi minun pitäisi siitä välittää?" Aloitetaan yksinkertaisella vertauksella.

Ajattele MCP-palvelimia erikoistuneina assistentteina, jotka auttavat AI-koodauskumppaniasi (kuten GitHub Copilot) yhdistämään ulkoisiin työkaluihin ja palveluihin. Samoin kuin käytät eri sovelluksia puhelimellasi eri tehtäviin – yksi sääälle, toinen navigointiin, kolmas pankkiasioihin – MCP-palvelimet antavat AI-avustajallesi mahdollisuuden olla vuorovaikutuksessa eri kehitystyökalujen ja palveluiden kanssa.

### Ongelma, jonka MCP-palvelimet ratkaisevat

Ennen MCP-palvelimia, jos halusit:
- Tarkistaa Azure-resurssisi
- Luoda GitHub-issue
- Kysellä tietokantaasi
- Etsiä dokumentaatiosta

Sinun piti lopettaa koodaaminen, avata selain, siirtyä oikealle verkkosivulle ja tehdä nämä tehtävät manuaalisesti. Tämä jatkuva kontekstinvaihto katkaisee työskentelyvirran ja vähentää tuottavuutta.

### Miten MCP-palvelimet muuttavat kehityskokemustasi

MCP-palvelimien avulla voit pysyä kehitysympäristössäsi (VS Code, Visual Studio jne.) ja pyytää AI-avustajaa hoitamaan nämä tehtävät. Esimerkiksi:

**Perinteisen työnkulun sijasta:**
1. Lopeta koodaaminen
2. Avaa selain
3. Siirry Azure-portaaliin
4. Tarkista tallennustilin tiedot
5. Palaa VS Codeen
6. Jatka koodaamista

**Voit nyt tehdä tämän:**
1. Kysy AI:lta: "Mikä on Azure-tallennustilieni tila?"
2. Jatka koodaamista tarjotun tiedon pohjalta

### Tärkeimmät edut aloittelijoille

#### 1. 🔄 **Pysy flow-tilassasi**
- Ei enää siirtymistä useiden sovellusten välillä
- Keskity kirjoittamaasi koodiin
- Vähennä erilaisten työkalujen hallinnan henkistä kuormitusta

#### 2. 🤖 **Käytä luonnollista kieltä monimutkaisten komentojen sijaan**
- Älä opettele SQL-syntaksia ulkoa, kuvaile tarvittavat tiedot
- Älä muistele Azure CLI -komentoja, selitä, mitä haluat saavuttaa
- Anna AI:n hoitaa tekniset yksityiskohdat, kun keskityt logiikkaan

#### 3. 🔗 **Yhdistä useita työkaluja keskenään**
- Luo tehokkaita työnkulkuja yhdistämällä eri palveluita
- Esimerkki: "Hae kaikki uudet GitHub-asiat ja luo vastaavat Azure DevOps -työtehtävät"
- Rakenna automaatioita ilman monimutkaisia skriptejä

#### 4. 🌐 **Pääsy kasvavaan ekosysteemiin**
- Hyödynnä Microsoftin, GitHubin ja muiden yritysten kehittämiä palvelimia
- Yhdistä eri toimittajien työkaluja saumattomasti
- Liity standardoituneeseen ekosysteemiin, joka toimii eri AI-avustajien kanssa

#### 5. 🛠️ **Opiskele tekemällä**
- Aloita valmiiksi rakennetuilla palvelimilla oppiaksesi käsitteet
- Rakenna vähitellen omia palvelimia, kun tulet varmemmaksi
- Käytä saatavilla olevia SDK:ita ja dokumentaatiota oppimisen tukena

### Todellinen esimerkki aloittelijoille

Kuvitellaan, että olet uusi web-kehityksen parissa ja työskentelet ensimmäisen projektisi parissa. Näin MCP-palvelimet voivat auttaa:

**Perinteinen lähestymistapa:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP-palvelimilla:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Enterprise-standardin etu

MCP on kehittymässä alan laajuiseksi standardiksi, mikä tarkoittaa:
- **Johdonmukaisuus**: Samankaltainen käyttökokemus eri työkaluissa ja yrityksissä
- **Yhteensopivuus**: Eri toimittajien palvelimet toimivat yhteen
- **Tulevaisuuden turvaaminen**: Taidot ja asetukset siirtyvät eri AI-avustajien välillä
- **Yhteisö**: Laaja ekosysteemi jaettuine tietoineen ja resursseineen

### Aloittaminen: Mitä opit

Tässä oppaassa tutustumme 10 Microsoftin MCP -palvelimeen, jotka ovat erityisen hyödyllisiä kehittäjille kaikilla tasoilla. Jokainen palvelin on suunniteltu:
- Ratkaisemaan yleisiä kehityshaasteita
- Vähentämään toistuvia tehtäviä
- Parantamaan koodin laatua
- Tukemaan oppimismahdollisuuksia

> **💡 Oppimisvinkki**
> 
> Jos olet täysin uusi MCP:n parissa, aloita moduuleista [MCP:n johdanto](../00-Introduction/README.md) ja [Peruskäsitteet](../01-CoreConcepts/README.md). Palaa sitten tänne katsomaan, miten nämä käsitteet toteutuvat käytännön Microsoft-työkaluissa.
>
> Lisätietoja MCP:n merkityksestä löydät Maria Naggagan kirjoituksesta: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## MCP:n käyttöönotto VS Codessa ja Visual Studiossa 🚀

Näiden MCP-palvelimien käyttöönotto on helppoa, jos käytät Visual Studio Codea tai Visual Studio 2022:ta GitHub Copilotin kanssa.

### VS Coden asetukset

Perusprosessi VS Codessa:

1. **Ota Agent-tila käyttöön**: Vaihda VS Codessa Copilot Chat -ikkunassa Agent-tilaan
2. **Konfiguroi MCP-palvelimet**: Lisää palvelinkonfiguraatiot VS Code -asetustiedostoosi settings.json
3. **Käynnistä palvelimet**: Klikkaa "Start"-painiketta jokaisen haluamasi palvelimen kohdalla
4. **Valitse työkalut**: Valitse, mitkä MCP-palvelimet otetaan käyttöön nykyisessä istunnossasi

Tarkat asennusohjeet löydät [VS Code MCP -dokumentaatiosta](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Pro-vinkki: Hallitse MCP-palvelimia kuin ammattilainen!**
> 
> VS Code Extensions -näkymä sisältää nyt [kätevän uuden käyttöliittymän asennettujen MCP-palvelimien hallintaan](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Saat nopean pääsyn käynnistääksesi, pysäyttääksesi ja hallinnoidaksesi asennettuja MCP-palvelimia selkeän ja yksinkertaisen käyttöliittymän avulla. Kokeile jo tänään!

### Visual Studio 2022:n asetukset

Visual Studio 2022:ssa (versiosta 17.14 alkaen):

1. **Ota Agent-tila käyttöön**: Klikkaa GitHub Copilot Chat -ikkunan "Ask"-valikkoa ja valitse "Agent"
2. **Luo konfiguraatiotiedosto**: Luo `.mcp.json`-tiedosto ratkaisukansioon (suositeltu sijainti: `<SOLUTIONDIR>\.mcp.json`)
3. **Konfiguroi palvelimet**: Lisää MCP-palvelinkonfiguraatiot standardin MCP-muodon mukaisesti
4. **Tool Approval**: Kun pyydetään, hyväksy käyttämäsi työkalut asianmukaisilla käyttöoikeuksilla

Tarkat Visual Studio -asennusohjeet löydät [Visual Studio MCP -dokumentaatiosta](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Jokaisella MCP-palvelimella on omat konfiguraatiovaatimuksensa (yhteysmerkkijonot, todennus jne.), mutta asennuskaava on samanlainen molemmissa IDE:ssä.

## Opitut läksyt Microsoft MCP -palvelimista 🛠️

### 1. 📚 Microsoft Learn Docs MCP -palvelin

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mitä se tekee**: Microsoft Learn Docs MCP -palvelin on pilvipalvelu, joka antaa AI-avustajille reaaliaikaisen pääsyn viralliseen Microsoftin dokumentaatioon Model Context Protocolin kautta. Se yhdistää osoitteeseen `https://learn.microsoft.com/api/mcp` ja mahdollistaa semanttisen haun Microsoft Learn -sivustolle, Azure-dokumentaatioon, Microsoft 365 -dokumentaatioon ja muille virallisille Microsoft-lähteille.

**Miksi se on hyödyllinen**: Vaikka se saattaa vaikuttaa "vain dokumentaatiolta", tämä palvelin on välttämätön jokaiselle Microsoft-teknologioiden käyttäjälle. Yksi suurimmista valituksenaiheista .NET-kehittäjillä AI-koodausavustajista on, etteivät ne ole ajan tasalla uusimmista .NET- ja C# -julkaisuista. Microsoft Learn Docs MCP -palvelin ratkaisee tämän tarjoamalla reaaliaikaisen pääsyn ajantasaisimpaan dokumentaatioon, API-viitteisiin ja parhaisiin käytäntöihin. Olitpa sitten työskentelemässä uusimpien Azure SDK:iden kanssa, tutkimassa uusia C# 13 -ominaisuuksia tai toteuttamassa huipputason Aspire-malleja, tämä palvelin varmistaa, että AI-avustajallasi on pääsy auktoritatiiviseen ja ajan tasalla olevaan tietoon tuottaakseen tarkkaa ja modernia koodia.

**Todellinen käyttö:** "Mitkä ovat az cli -komennot Azure Container Appin luomiseen virallisten Microsoft Learn -dokumenttien mukaisesti?" tai "Miten konfiguroin Entity Frameworkin riippuvuussuihkutuksen kanssa ASP.NET Core -sovelluksessa?" Tai entä "Arvioi tämä koodi varmistaaksesi, että se vastaa Microsoft Learn Documentationin suorituskykysuosituksia." Palvelin kattaa laajasti Microsoft Learn, Azure-dokumentaation ja Microsoft 365 -dokumentaation käyttäen edistynyttä semanttista hakua löytääkseen kontekstin kannalta merkityksellisimmät tiedot. Se palauttaa jopa 10 korkealaatuista sisältökappaletta artikkelien otsikoiden ja URL-osoitteiden kanssa, ja se aina käyttää uusinta Microsoftin dokumentaatiota julkaisun hetkellä.

**Esimerkkitoiminto:** Palvelin avaa `microsoft_docs_search` -työkalun, joka suorittaa semanttisen haun Microsoftin virallista teknistä dokumentaatiota vastaan. Kun konfiguroitu, voit kysyä esimerkiksi "Miten toteutan JWT-todennuksen ASP.NET Core -sovelluksessa?" ja saada yksityiskohtaisia virallisia vastauksia lähde-linkkeineen. Hakutulosten laatu on erinomainen, koska se ymmärtää kontekstin – kysymys "kontteista" Azuren yhteydessä palauttaa Azure Container Instances -dokumentaation, kun taas sama termi .NET-kontekstissa palauttaa oleellista tietoa C# -kokoelmista.

Tämä on erityisen hyödyllistä nopeasti muuttuville tai juuri päivitetyille kirjastoille ja käyttötapauksille. Esimerkiksi muutamissa viimeisissä koodausprojekteissani halusin hyödyntää ominaisuuksia uusimmissa Aspire- ja Microsoft.Extensions.AI -julkaisuissa. Sisällyttämällä Microsoft Learn Docs MCP -palvelimen, pystyin hyödyntämään paitsi API-dokumentaatiota myös juuri julkaistuja ohjeita ja läpikäyntejä.

> **💡 Pro-vinkki**
> 
> Jopa työkalujen kanssa käyttäytyvät mallit tarvitsevat kannustusta MCP-työkalujen käyttöön! Harkitse järjestelmäkehotteiden tai [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) lisäämistä, esimerkiksi: "Sinulla on pääsy `microsoft.docs.mcp` -työkaluun – käytä tätä työkalua etsiäksesi Microsoftin uusinta virallista dokumentaatiota Microsoft-teknologioiden, kuten C#, Azure, ASP.NET Core tai Entity Framework, kysymyksiä käsitellessäsi."
>
> Erinomainen esimerkki käytännöstä löytyy [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) -tilasta Awesome GitHub Copilot -kokoelmasta. Tämä tila hyödyntää erityisesti Microsoft Learn Docs MCP -palvelinta puhdistamaan ja modernisoimaan C#-koodia uusimpien mallien ja parhaiden käytäntöjen avulla.
### 2. ☁️ Azure MCP Server


[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mitä se tekee**: Azure MCP Server on kattava kokoelma yli 15 erikoistunutta Azure-palveluiden liitintä, jotka tuovat koko Azure-ekosysteemin AI-työnkulkuusi. Tämä ei ole vain yksittäinen palvelin – se on tehokas kokoelma, joka sisältää resurssien hallinnan, tietokantayhteydet (PostgreSQL, SQL Server), Azure Monitorin lokianalyysin KQL:llä, Cosmos DB -integraation ja paljon muuta.

**Miksi se on hyödyllinen**: Pelkän Azure-resurssien hallinnan lisäksi tämä palvelin parantaa merkittävästi koodin laatua työskennellessäsi Azure SDK:iden kanssa. Kun käytät Azure MCP:tä Agent-tilassa, se ei ainoastaan auta sinua kirjoittamaan koodia – se auttaa sinua kirjoittamaan *parempaa* Azure-koodia, joka noudattaa nykyisiä tunnistautumismalleja, virheenkäsittelyn parhaita käytäntöjä ja hyödyntää uusimpia SDK-ominaisuuksia. Saat koodin, joka noudattaa Azuren suosituksia tuotantokuormituksia varten sen sijaan, että saisit geneeristä koodia, joka saattaa toimia.

**Keskeiset moduulit sisältävät**:
- **🗄️ Tietokantaliittimet**: Luonnollisen kielen suora pääsy Azure Database for PostgreSQL ja SQL Server -tietokantoihin
- **📊 Azure Monitor**: KQL-pohjainen lokianalyysi ja operatiiviset näkymät
- **🌐 Resurssien hallinta**: Täysi Azure-resurssien elinkaaren hallinta
- **🔐 Tunnistautuminen**: DefaultAzureCredential- ja hallitun identiteetin mallit
- **📦 Tallennuspalvelut**: Blob Storage, Queue Storage ja Table Storage -operaatiot
- **🚀 Konttipalvelut**: Azure Container Apps, Container Instances ja AKS-hallinta
- **Ja monia muita erikoistuneita liittimiä**

**Todelliset käyttötapaukset**: "Listaa Azure-tallennustilini tilit", "Kysy Log Analytics -työtilastani virheitä viimeisen tunnin ajalta" tai "Auta rakentamaan Azure-sovellus Node.js:llä oikein tunnistaen"

**Täysi demo-skenaario**: Tässä on täydellinen läpikäynti, joka näyttää Azure MCP:n ja GitHub Copilot for Azure -laajennuksen yhdistämisen voiman VS Codessa. Kun molemmat on asennettu ja annat kehotteen:

> "Luo Python-skripti, joka lataa tiedoston Azure Blob Storageen DefaultAzureCredential-tunnistautumista käyttäen. Skriptin pitää yhdistää Azure-tallennustiliini nimeltä 'mycompanystorage', ladata konttiin nimeltä 'documents', luoda testitiedosto nykyisellä aikaleimalla ladattavaksi, käsitellä virheet nätisti ja antaa informatiivista palautetta, noudattaa Azuren parhaita käytäntöjä tunnistautumisessa ja virheenkäsittelyssä, sisältää kommentteja siitä, miten DefaultAzureCredential-tunnistautuminen toimii, ja tehdä skriptistä hyvin jäsennelty funktioineen ja dokumentaatiollaan."

Azure MCP Server tuottaa täydellisen, tuotantovalmiin Python-skriptin, joka:
- Käyttää uusinta Azure Blob Storage SDK:ta oikein asynkronisissa malleissa
- Toteuttaa DefaultAzureCredentialin kattavalla varajärjestyksen selityksellä
- Sisältää vahvan virheenkäsittelyn erityyppisillä Azure-poikkeuksilla
- Noudattaa Azure SDK:n parhaita käytäntöjä resurssien ja yhteyksien hallinnassa
- Tarjoaa yksityiskohtaisen lokituksen ja informatiivisen konsolitulosteen
- Luo hyvin jäsennellyn skriptin, jossa on funktiot, dokumentaatio ja tyyppivihjeet

Merkittävää tässä on se, että ilman Azure MCP:tä saatat saada geneeristä blob storage -koodia, joka toimii mutta ei noudata nykyisiä Azure-malleja. Azure MCP:llä saat koodia, joka hyödyntää uusimpia tunnistautumismenetelmiä, käsittelee Azure-spesifisiä virhetilanteita ja noudattaa Microsoftin suosituksia tuotantosovelluksille.

**Esimerkkitapaus**: Minulla on ollut vaikeuksia muistaa `az` ja `azd` komentorivien syntaksi ad-hoc-käytössä. Se on aina kaksivaiheinen prosessi: ensin etsin syntaksin, sitten suoritan komennon. Menen usein portaalin puolelle ja klikkailen siellä, koska en halua myöntää etten muista CLI-syntaksia. Pystyä sanomaan suoraan, mitä haluan, on hämmästyttävää – ja vielä parempi, että se onnistuu ilman, että lähden pois IDE:stä!

Aloitukseen on loistava lista käyttötapauksia [Azure MCP -varastossa](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server). Täydellisiä asennusohjeita ja edistyneitä konfigurointivaihtoehtoja löydät [virallisesta Azure MCP -dokumentaatiosta](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mitä se tekee**: Virallinen GitHub MCP Server tarjoaa saumattoman integraation GitHubin koko ekosysteemiin, tarjoten sekä isännöidyn etäkäytön että paikallisen Docker-asennuksen vaihtoehdot. Tämä ei ole pelkkä perusvaraston hallinta – se on kattava työkaluvalikoima, joka sisältää GitHub Actionsin hallinnan, pull request -työnkulut, ongelmien seurannan, tietoturvaskannauksen, ilmoitukset ja edistyneet automaatiomahdollisuudet.

**Miksi se on hyödyllinen**: Tämä palvelin muuttaa sitä, miten vuorovaikutat GitHubin kanssa tuomalla koko alustan kokemuksen suoraan kehitysympäristöösi. Sen sijaan, että vaihdat jatkuvasti VS Coden ja GitHub.comin välillä projektinhallintaan, koodikatselmuksiin ja CI/CD-seurantaan, voit hoitaa kaiken luonnollisen kielen komennoilla pysyen keskittyneenä koodiin.

> **ℹ️ Huomautus: Eri tyypit 'agenteille'**
> 
> Älä sekoita tätä GitHub MCP Serveriä GitHubin Coding Agentiin (AI-agentti, jolle voi osoittaa tehtäviä koodauksen automatisointiin). GitHub MCP Server toimii VS Code -agentin tilassa tarjoten GitHub API -integraation, kun taas GitHubin Coding Agent on erillinen ominaisuus, joka luo pull requesteja, kun se on osoitettu GitHubin ongelmiin.

**Keskeiset ominaisuudet sisältävät**:
- **⚙️ GitHub Actions**: Täydellinen CI/CD-putkilinjan hallinta, työnkulkujen seuranta ja artefaktien käsittely
- **🔀 Pull Requests**: PR:ien luonti, tarkastus, yhdistäminen ja hallinta kattavalla tilan seurannalla
- **🐛 Ongelmat**: Koko ongelmakierteen hallinta, kommentointi, merkinnät ja osoittaminen
- **🔒 Tietoturva**: Koodin skannaushälytykset, salaisuuksien tunnistus ja Dependabot-integraatio
- **🔔 Ilmoitukset**: Älykäs ilmoitusten hallinta ja varaston tilauskontrolli
- **📁 Varaston hallinta**: Tiedostotoiminnot, haaran hallinta ja varaston ylläpito
- **👥 Yhteistyö**: Käyttäjä- ja organisaatiohaut, tiimien hallinta ja käyttöoikeuksien valvonta

**Todelliset käyttötapaukset**: "Luo pull request ominaisuusharastani", "Näytä kaikki tämän viikon epäonnistuneet CI-ajot", "Listaa avoimet tietoturvahälytykset varastoilleni" tai "Etsi kaikki minulle osoitetut ongelmat kaikista organisaatioistani"

**Täysi demo-skenaario**: Tässä on tehokas työnkulku, joka demonstroi GitHub MCP Serverin kyvykkyydet:

> "Minun täytyy valmistautua sprinttikäyttöön. Näytä kaikki tämän viikon luomani pull requestit, tarkista CI/CD-putkistojen tila, tee yhteenveto kaikista korjattavista tietoturvahälytyksistä ja auta laatimaan julkaisumuistiinpanot yhdistetyistä PR:istä, joissa on 'feature'-tunniste."

GitHub MCP Server:
- Kysyy viimeisimmät pull requestisi yksityiskohtaisen tilatiedon kera
- Analysoi työnkulkujen ajoja ja korostaa kaikki epäonnistumiset tai suorituskykyongelmat
- Kokoa tietoturvaskannauksen tulokset ja priorisoi kriittiset hälytykset
- Laatii kattavat julkaisumuistiinpanot purkamalla tietoja yhdistetyistä PR:istä
- Tarjoaa käytännön seuraavia askeleita sprintin suunnitteluun ja julkaisun valmisteluun

**Esimerkkitapaus**: Käytän tätä mielelläni koodikatselmuksen työnkulkuihin. Sen sijaan, että hyppäisin VS Coden, GitHub-ilmoitusten ja pull request -sivujen välillä, voin sanoa "Näytä kaikki PR:t, jotka odottavat minun tarkistustani" ja sitten "Lisää kommentti PR:ään #123 kysyen virheenkäsittelystä tunnistautumismenetelmässä." Palvelin hoitaa GitHub API -kutsut, ylläpitää keskustelukontekstia ja auttaa jopa laatimaan rakentavampia katselmointikommentteja.

**Tunnistautumisvaihtoehdot**: Palvelin tukee sekä OAuthia (saumaton VS Codessa) että henkilökohtaisia käyttöoikeustunnuksia, ja siinä on konfiguroitavat työkalusarjat, joilla voit ottaa käyttöön vain tarvitsemasi GitHub-toiminnot. Voit ajaa sen etäisännöitynä palveluna nopeaan käyttöönottoon tai paikallisesti Dockerilla täydelliseen hallintaan.

> **💡 Vinkki**
> 
> Ota käyttöön vain tarvitsemiasi työkalusarjoja määrittämällä `--toolsets` -parametri MCP-palvelinasetuksissasi kontekstin koon pienentämiseksi ja AI-työkalun valinnan parantamiseksi. Esimerkiksi lisää `"--toolsets", "repos,issues,pull_requests,actions"` MCP-kokoonpanoon ydin kehitystyönkulkuja varten, tai käytä `"--toolsets", "notifications, security"` jos haluat pääasiassa GitHubin valvontamahdollisuuksia.
### 4. 🔄 Azure DevOps MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mitä se tekee**: Yhdistää Azure DevOps -palveluihin tarjoten kattavan projektinhallinnan, työtehtävien seurannan, build-putkistojen hallinnan ja varastojen toiminnot.

**Miksi se on hyödyllinen**: Tiimeille, jotka käyttävät Azure DevOpsia ensisijaisena DevOps-alustanaan, tämä MCP-palvelin poistaa jatkuvan välilehtien vaihdon kehitysympäristön ja Azure DevOpsin verkkokäyttöliittymän välillä. Voit hallita työtehtäviä, tarkistaa buildien tilat, kysellä varastoja ja hoitaa projektinhallintatehtäviä suoraan AI-avustajaltasi.

**Todelliset käyttötapaukset**: "Näytä kaikki aktiiviset työtehtävät nykyisessä sprintissä WebApp-projektille", "Luo bugiraportti juuri löytämästäni kirjautumisongelmasta" tai "Tarkista build-putkistojemme tila ja näytä viimeisimmät virheet"

**Esimerkkitapaus**: Voit helposti tarkistaa tiimisi tämänhetkisen sprintin tilanteen yksinkertaisella kyselyllä kuten "Näytä kaikki aktiiviset työtehtävät nykyisessä sprintissä WebApp-projektille" tai "Luo bugiraportti juuri löytämästäni kirjautumisongelmasta" ilman, että poistut kehitysympäristöstäsi.

### 5. 📝 MarkItDown MCP Server


[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mitä se tekee**: MarkItDown on monipuolinen asiakirjojen muunninpalvelin, joka muuntaa erilaisia tiedostomuotoja korkealaatuiseksi Markdowniksi, optimoituna LLM-kulutukseen ja tekstianalyysityönkulkuihin.

**Miksi se on hyödyllinen**: Oleellinen nykyaikaisissa dokumentaatiotyönkuluissa! MarkItDown käsittelee vaikuttavan laajan valikoiman tiedostomuotoja säilyttäen samalla asiakirjan keskeisen rakenteen kuten otsikot, luettelot, taulukot ja linkit. Toisin kuin yksinkertaiset tekstin poimintatyökalut, se keskittyy säilyttämään semanttisen merkityksen ja muotoilun, joka on arvokasta sekä tekoälyprosessointiin että ihmisten luettavuuteen.

**Tuetut tiedostomuodot**:
- **Office-asiakirjat**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Mediatiedostot**: Kuvakkeet (EXIF-metadata ja OCR), ääni (EXIF-metadata ja puheen transkriptio)
- **Verkkosisältö**: HTML, RSS-syötteet, YouTube-URL-osoitteet, Wikipedia-sivut
- **Datan muodot**: CSV, JSON, XML, ZIP-tiedostot (käsittelee sisällöt rekursiivisesti)
- **Julkaisumuodot**: EPub, Jupyter-muistiinpanot (.ipynb)
- **Sähköposti**: Outlook-viestit (.msg)
- **Edistynyt**: Azure Document Intelligence -integraatio parannetulle PDF-käsittelylle

**Edistyneet ominaisuudet**: MarkItDown tukee LLM-pohjaisia kuvailuja (kun käytössä on OpenAI-asiakas), Azure Document Intelligencea parannetulle PDF-käsittelylle, äänidokumenttien puheentunnistusta sekä liitännäisjärjestelmää lisätiedostomuotojen laajentamiseen.

**Käytännön käyttö**: "Muunna tämä PowerPoint-esitys Markdowniksi dokumentaatiosivustollemme", "Poimi teksti tästä PDF:stä asianmukaisella otsikkorakenteella" tai "Muunna tämä Excel-taulukko luettavaan taulukkomuotoon"

**Näyte-esimerkki**: Siteeratakseni [MarkItDown-dokumentaatiota](https://github.com/microsoft/markitdown#why-markdown):

> Markdown on erittäin lähellä raakatekstiä, sisältäen minimaalista merkintää tai muotoilua, mutta tarjoaa silti tavan esittää tärkeä asiakirjan rakenne. Suurimmat LLM:t kuten OpenAI:n GPT-4o "puhuvat" natiivisti Markdownia ja usein sisällyttävät sitä vastauksiinsa itsestään. Tämä viittaa siihen, että ne on koulutettu valtavilla määrillä Markdown-muotoiltua tekstiä ja ymmärtävät sitä hyvin. Lisäetuna Markdownin konventiot ovat myös erittäin token-tehokkaita.

MarkItDown on todella hyvä säilyttämään asiakirjarakenteen, mikä on tärkeää tekoälyn työnkuluissa. Esimerkiksi PowerPoint-esitystä muuntamalla se säilyttää dian järjestyksen oikeilla otsikoilla, poimii taulukot Markdown-taulukkoina, lisää kuville alt-tekstit ja jopa käsittelee puheenvuoromuistiinpanot. Kaaviot muunnetaan luettaviksi datataulukoiksi ja tuloksena saatu Markdown säilyttää alkuperäisen esityksen loogisen kulun. Tämä tekee siitä täydellisen syötteen esityssisällölle tekoälyjärjestelmiin tai dokumentaation luontiin olemassa olevista dioista.
### 6. 🗃️ SQL Server MCP -palvelin

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mitä se tekee**: Tarjoaa keskustelukäyttöliittymän SQL Server -tietokantoihin (paikallisesti, Azure SQL:ssä tai Fabricissa)

**Miksi se on hyödyllinen**: Vastaava kuin PostgreSQL-palvelin mutta Microsoftin SQL-ekosysteemille. Yhdistää yksinkertaisella yhteysmerkkijonolla ja aloittaa kyselyt luonnollisella kielellä – ei enää kontekstinvaihtoa!

**Käytännön käyttö**: "Etsi kaikki tilaukset, joita ei ole täytetty viimeisen 30 päivän aikana" käännetään sopiviksi SQL-kyselyiksi ja palauttaa muotoillut tulokset

**Näyte-esimerkki**: Kun tietokantayhteys on määritetty, voit aloittaa keskustelut tiedoistasi välittömästi. Blogikirjoitus esittelee tämän yksinkertaisen kysymyksen kautta: "mihin tietokantaan olet yhteydessä?" MCP-palvelin vastaa kutsumalla sopivan tietokantatyökalun, yhdistämällä SQL Server -instanssiisi ja palauttaen tietoja nykyisestä tietokantayhteydestä – kaikki ilman SQL-koodin kirjoittamista. Palvelin tukee kattavia tietokannan toimintoja skeeman hallinnasta datan käsittelyyn, kaikki luonnollisen kielen kehotteilla. Täydelliset asennusohjeet ja konfigurointiesimerkit VS Codella ja Claude Desktopilla löytyvät kohteesta: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP -palvelin

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mitä se tekee**: Mahdollistaa tekoälyedustajien vuorovaikutuksen verkkosivujen kanssa testausta ja automaatiota varten

> **ℹ️ Tehostaa GitHub Copilotia**
> 
> Playwright MCP Server tehostaa GitHub Copilotin Coding Agentia, antaen sille verkkoselailumahdollisuudet! [Lisätietoja tästä ominaisuudesta](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miksi se on hyödyllinen**: Täydellinen luonnollisen kielen kuvailujen ohjaamaan automatisoituun testaukseen. Tekoäly voi navigoida verkkosivustoilla, täyttää lomakkeita ja poimia dataa rakenteellisten saavutettavuuskuvien avulla – tämä on todella tehokasta!

**Käytännön käyttö**: "Testaa kirjautumisprosessi ja varmista, että hallintapaneeli latautuu oikein" tai "Luo testi, joka etsii tuotteita ja validioi tulossivun" – kaikki ilman, että tarvitsee sovelluksen lähdekoodia

**Näyte-esimerkki**: Työkaverini Debbie O'Brien on tehnyt viime aikoina upeaa työtä Playwright MCP Serverin kanssa! Hän esimerkiksi näytti hiljattain, miten voi generoida täydellisiä Playwright-testejä jopa ilman pääsyä sovelluksen lähdekoodiin. Hänen esimerkissään hän pyysi Copilotia luomaan testin elokuhaun sovellukselle: siirry sivustolle, etsi "Garfield" ja vahvista, että elokuva näkyy tuloksissa. MCP käynnisti selaussession, tutki sivun rakennetta DOM-kuvien avulla, löysi oikeat valitsimet ja generoi täysin toimivan TypeScript-testin, joka läpäisi ensimmäisellä ajolla.

Mikä tekee tästä todella tehokkaan on, että se yhdistää luonnollisen kielen ohjeet suoritettavaan testikoodiin. Perinteiset lähestymistavat vaativat joko manuaalista testien kirjoitusta tai pääsyä koodipohjaan kontekstia varten. Mutta Playwright MCP:llä voit testata ulkoisia sivustoja, asiakasohjelmia tai toimia mustan laatikon testausympäristöissä, joissa koodiin ei ole pääsyä.


### 8. 💻 Dev Box MCP -palvelin

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mitä se tekee**: Hallinnoi Microsoft Dev Box -ympäristöjä luonnollisen kielen avulla

**Miksi se on hyödyllinen**: Yksinkertaistaa kehitysympäristöjen hallintaa valtavasti! Luo, konfiguroi ja hallitse kehitysympäristöjä ilman, että tarvitsee muistaa tiettyjä komentoja.

**Käytännön käyttö**: "Luo uusi Dev Box, jossa on uusin .NET SDK ja konfiguroi se projektiamme varten", "Tarkista kaikkien kehitysympäristöjeni tila" tai "Luo standardoitu demo-ympäristö tiimiesityksiämme varten"

**Näyte-esimerkki**: Olen suuri Dev Boxin käyttäjä henkilökohtaiseen kehitykseen. Oivalsin sen loistavuuden, kun James Montemagno kertoi, miten erinomainen Dev Box on konferenssidemoihin, koska siinä on supernopea ethernet-yhteys riippumatta siitä, millaista konferenssi-/hotelli-/lentosanomaverkkoa käytän. Itse asiassa harjoittelin hiljattain konferenssidemoa kannettavani ollessa puhelimen hotspotissa bussimatkalla Brugesista Antwerpeniin! Seuraava askel on tutkia tiimin monen kehitysympäristön hallintaa ja standardoitujen demo-ympäristöjen luomista. Toinen suuri käyttötapaus, jonka olen kuullut asiakkailta ja työkavereilta, on Dev Boxin käyttö esikonfiguroituihin kehitysympäristöihin. Molemmissa tapauksissa MCP:n käyttäminen Dev Boxien konfigurointiin ja hallintaan mahdollistaa luonnollisen kielen vuorovaikutuksen, kaiken tämän samalla kun pysyt omassa kehitysympäristössäsi.

### 9. 🤖 Microsoft Foundry MCP -palvelin


[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Mitä se tekee**: Microsoft Foundry MCP Server tarjoaa kehittäjille kattavan pääsyn Azuren tekoälyekosysteemiin, mukaan lukien mallikatalogit, käyttöönoton hallinta, tiedon indeksointi Azure AI Searchilla ja arviointityökalut. Tämä kokeellinen palvelin yhdistää tekoälyn kehityksen ja Azuren tehokkaan tekoälyinfrastruktuurin, tehden tekoälysovellusten rakentamisesta, käyttöönotosta ja arvioinnista helpompaa.

**Miksi se on hyödyllinen**: Tämä palvelin muuttaa tapaa, jolla työskentelet Azure AI -palveluiden kanssa, tuomalla yritystason tekoälyominaisuudet suoraan kehitystyöhösi. Sen sijaan, että vaihtaisit Azuren portaalin, dokumentaation ja IDE:n välillä, voit löytää malleja, ottaa palveluita käyttöön, hallita tietokantoja ja arvioida tekoälyn suorituskykyä luonnollisen kielen komennoilla. Se on erityisen tehokas kehittäjille, jotka rakentavat RAG (Retrieval-Augmented Generation) -sovelluksia, hallitsevat monimallisia käyttöönottoja tai toteuttavat kattavia tekoälyn arviointiputkia.

**Keskeiset kehittäjäominaisuudet**:
- **🔍 Mallin löytäminen ja käyttöönotto**: Tutki Microsoft Foundryn mallikatalogia, saa yksityiskohtaisia mallin tietoja esimerkkikoodien kanssa ja ota malleja käyttöön Azure AI Servicesissä
- **📚 Tiedon hallinta**: Luo ja hallinnoi Azure AI Search -indeksejä, lisää dokumentteja, konfiguroi indeksoijat ja rakenna edistyneitä RAG-järjestelmiä
- **⚡ Tekoälyagenttien integrointi**: Yhdistä Azure AI Agentteihin, kysy olemassa olevista agenteista ja arvioi agenttien suorituskykyä tuotantoympäristöissä
- **📊 Arviointikehys**: Suorita kattavia tekstin ja agenttien arviointeja, luo markdown-raportteja ja toteuta laadunvarmistusta tekoälysovelluksille
- **🚀 Prototyyppityökalut**: Hanki asennusohjeet GitHub-pohjaiseen prototypointiin ja pääsy Microsoft Foundry Labsin huippuluokan tutkimusmalleihin

**Kehittäjän käytännön esimerkki**: "Ota Phi-4-malli käyttöön Azure AI Servicesissä sovellukselleni", "Luo uusi hakemisto dokumentaation RAG-järjestelmää varten", "Arvioi agenttini vastaukset laadun mittarien perusteella" tai "Löydä paras päättelymalli monimutkaisiin analyysitehtäviini"

**Täysi demonstraatio**: Tässä on tehokas tekoälyn kehityksen työnkulku:

> "Rakennan asiakastukikontaktia. Auta minua löytämään hyvä päättelymalli katalogista, ottamaan se käyttöön Azure AI Servicesissä, luomaan tietopohja dokumentaatiostamme, perustamaan arviointikehyksen vastausten laadun testaamiseksi, ja sitten auttamaan integraation prototypoinnissa GitHub-tokenin avulla testaukseen."

Microsoft Foundry MCP Server tekee seuraavaa:
- Kysyy mallikatalogia suositellakseen parhaita päättelymalleja tarpeidesi perusteella
- Tarjoaa käyttöönotto-komennot ja kiintiötiedot valitsemallesi Azure-alueelle
- Perustaa Azure AI Search -indeksit oikealla skeemalla dokumentaatiollesi
- Konfiguroi arviointiputket laadun mittareilla ja turvallisuustarkastuksilla
- Luo prototypointikoodin GitHub-todennuksella välittömään testaukseen
- Tarjoaa kattavat asennusoppaat juuri sinun teknologiakokonaisuutesi mukaan

**Esimerkki kehittäjän näkökulmasta**: Olen kamppaillut eri LLM-mallien seuraamisessa. Tunnen muutaman päämallin, mutta olen tuntenut jääväni vaille tuottavuutta ja tehokkuutta lisääviä mahdollisuuksia. Tokenit ja kiintiöt ovat stressaavia ja vaikeita hallita – en koskaan tiedä, valitsenko oikean mallin oikeaan tehtävään vai kulutan budjettiani tehottomasti. Kuulin tästä MCP Serveristä James Montemagnolta, kun kyselin tiimikavereilta MCP Server -suosituksia tälle postaukselle, ja olen innoissani kokeilemassa sitä! Mallin etsintäominaisuudet näyttävät erityisen vaikuttavilta minulle, joka haluan tutkia tavallisten mallien ulkopuolelle ja löytää tehtäviin optimoituja malleja. Arviointikehys auttaa varmistamaan, että saan oikeasti parempia tuloksia, en vain kokeile uutta kokeilun vuoksi.

> **ℹ️ Kokeellinen tila**
> 
> Tämä MCP-palvelin on kokeellinen ja aktiivisessa kehityksessä. Ominaisuudet ja API:t saattavat muuttua. Erinomainen Azure AI -ominaisuuksien tutkimiseen ja prototyyppien rakentamiseen, mutta varmista vakaus vaativaan tuotantokäyttöön.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Mitä se tekee**: Tarjoaa kehittäjille olennaiset työkalut tekoälyagenttien ja sovellusten rakentamiseen, jotka integroituvat Microsoft 365:een ja Microsoft 365 Copilotiin, mukaan lukien skeeman validointityökalut, esimerkkikoodien hakeminen ja vikojen selvitysapu.

**Miksi se on hyödyllinen**: Microsoft 365:lle ja Copilotille rakentaminen sisältää monimutkaisia manifest-skeemoja ja erityisiä kehityskäytäntöjä. Tämä MCP-palvelin tuo olennaiset kehitysvälineet suoraan koodausympäristöösi auttaen sinua validoimaan skeemat, löytämään esimerkkikoodia ja ratkaisemaan yleisiä ongelmia ilman, että sinun tarvitsee jatkuvasti tarkistaa dokumentaatiota.

**Käytännön esimerkkejä**: "Vahvista deklaratiivisen agentin manifestini ja korjaa skeemavirheet", "Näytä esimerkkikoodi Microsoft Graph API -laajennuksen toteuttamiseen", tai "Auta ratkaisemaan Teams-sovellukseni tunnistautumisongelmat"

**Esimerkki kehittäjältä**: Ota yhteyttä ystävääni John Milleriin Buildin aikana keskusteltuani hänelle M365 Agentseista, ja hän suositteli tätä MCP:tä. Tämä voisi olla loistava kehittäjille, jotka ovat uusia M365 Agentseille, koska se tarjoaa malleja, esimerkkikoodeja ja rakennetta aloitukseen ilman että dokumentaatioon hukkuu. Skeeman validointiominaisuudet näyttävät erityisen hyödyllisiltä virheiden välttämiseen, jotka voivat aiheuttaa tuntien virheenkorjausta.

> **💡 Vinkki**
> 
> Käytä tätä palvelinta yhdessä Microsoft Learn Docs MCP Serverin kanssa kattavaan M365-kehitystukeen – toinen tarjoaa virallisen dokumentaation, kun taas tämä tarjoaa käytännön kehitystyökaluja ja vikojen ratkaisua.


## Mitä seuraavaksi? 🔮

## 📋 Yhteenveto

Model Context Protocol (MCP) muuttaa tapaa, jolla kehittäjät ovat vuorovaikutuksessa tekoälyavustajien ja ulkoisten työkalujen kanssa. Nämä 10 Microsoft MCP -palvelinta osoittavat standardoidun tekoälyintegraation voiman, mahdollistaen saumattomat työnkulut, jotka pitävät kehittäjät virtaustilassa samalla, kun he käyttävät tehokkaita ulkoisia kyvykkyyksiä.

Laajasta Azure-ekosysteemin integraatiosta erikoistyökaluihin kuten Playwright selainautomaatiota varten ja MarkItDown dokumenttien käsittelyyn, nämä palvelimet demonstroivat, kuinka MCP voi parantaa tuottavuutta monipuolisissa kehitystilanteissa. Standardoitu protokolla varmistaa, että nämä työkalut toimivat saumattomasti yhdessä, luoden yhtenäisen kehityskokemuksen.

MCP-ekosysteemin kehittyessä, aktiivinen osallistuminen yhteisöön, uusien palvelinten tutkiminen ja räätälöityjen ratkaisujen rakentaminen ovat avain kehitystuottavuuden maksimoimiseen. MCP:n avoin standardiluonne tarkoittaa, että voit yhdistellä eri toimittajien työkaluja luodaksesi täydellisen työnkulun juuri sinun tarpeisiisi.

## 🔗 Lisäresurssit

- [Virallinen Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP Yhteisö & Dokumentaatio](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Dokumentaatio](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Dokumentaatio](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Dokumentaatio](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Tapahtumat](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Upeita GitHub Copilot -muokkauksia](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29./30. heinäkuuta tai katso tallenteena](https://aka.ms/mcpdevdays)

## 🎯 Harjoitukset

1. **Asenna ja konfiguroi**: Ota käyttöön yksi MCP-palvelimista VS Code -ympäristössäsi ja testaa perustoiminnallisuudet.
2. **Työnkulun integraatio**: Suunnittele kehitystyönkulku, joka yhdistää vähintään kolme eri MCP-palvelinta.
3. **Mukautetun palvelimen suunnittelu**: Tunnista päivittäisessä kehitystyössäsi tehtävä, joka hyötyisi omasta MCP-palvelimesta, ja luo sille määrittely.
4. **Suorituskyvyn analyysi**: Vertaa MCP-palvelinten käyttöä perinteisiin menetelmiin tavallisissa kehitystehtävissä.
5. **Turvallisuusarviointi**: Arvioi MCP-palvelinten käytön turvallisuusvaikutukset kehitysympäristössäsi ja ehdota parhaita käytäntöjä.


Seuraava: [Parhaat käytännöt](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->