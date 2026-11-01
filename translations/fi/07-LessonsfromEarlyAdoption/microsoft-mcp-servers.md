# 🚀 10 Microsoft MCP -palvelinta, jotka mullistavat kehittäjien tuottavuuden

## 🎯 Mitä opit tässä oppaassa

Tämä käytännön opas esittelee kymmenen Microsoftin MCP-palvelinta, jotka aktiivisesti muuttavat kehittäjien tapaa työskennellä tekoälyavustajien kanssa. Emme pelkästään selitä, mitä MCP-palvelimet *voivat* tehdä, vaan näytämme palvelimia, jotka jo tekevät todellisen eron päivittäisissä kehitystyön työnkuluissa Microsoftilla ja muualla.

Jokainen tämän oppaan palvelin on valittu todellisen maailman käytön ja kehittäjäpalautteen perusteella. Tutustut paitsi siihen, mitä kukin palvelin tekee, myös miksi se on tärkeä ja miten voit saada siitä parhaan hyödyn omissa projekteissasi. Olitpa sitten täysin uusi MCP:n käyttäjä tai haluat laajentaa nykyisiä asetuksiasi, nämä palvelimet edustavat käytännöllisimpiä ja vaikuttavimpia työkaluja Microsoftin ekosysteemissä.

> **💡 Pikavinkki**
> 
> Oletko uusi MCP:ssä? Ei hätää! Tämä opas on suunniteltu aloittelijaystävälliseksi. Selitämme käsitteet samalla kun etenemme, ja voit aina palata takaisin [Johdanto MCP:hen](../00-Introduction/README.md) ja [Peruskäsitteet](../01-CoreConcepts/README.md) -moduuleihimme syvempää taustaa varten.

## Yleiskatsaus

Tämä kattava opas tarkastelee kymmentä Microsoftin MCP-palvelinta, jotka ovat mullistamassa sitä, miten kehittäjät ovat vuorovaikutuksessa tekoälyavustajien ja ulkoisten työkalujen kanssa. Azure-resurssien hallinnasta asiakirjojen käsittelyyn nämä palvelimet näyttävät Model Context Protocolin voiman luoda saumattomia ja tuottavia kehitystyön työnkulkuja.

## Oppimistavoitteet

Tämän oppaan lopussa osaat:
- Ymmärtää, miten MCP-palvelimet parantavat kehittäjien tuottavuutta
- Oppia Microsoftin merkittävimmistä MCP-palvelinratkaisuista
- Löytää käytännön käyttötapauksia jokaiselle palvelimelle
- Tietää, miten nämä palvelimet asetetaan ja konfiguroidaan VS Codessa ja Visual Studiossa
- Tutustua laajempaan MCP-ekosysteemiin ja tulevaisuuden suuntiin

## 🔧 MCP-palvelimien ymmärtäminen: Aloittelijan opas

### Mitä MCP-palvelimet ovat?

MCP:n eli Model Context Protocolin aloittelijana saatat pohtia: "Mitä MCP-palvelin oikeastaan on ja miksi minun pitäisi välittää siitä?" Aloitetaan yksinkertaisella vertauksella.

Ajattele MCP-palvelimia erikoistuneina avustajina, jotka auttavat tekoälykoodauskumppaniasi (kuten GitHub Copilot) yhdistymään ulkoisiin työkaluihin ja palveluihin. Samoin kuin käytät puhelimellasi eri sovelluksia eri tehtäviin — yksi sääennusteeseen, toinen navigointiin, kolmas pankkiasiointiin — MCP-palvelimet antavat tekoälyavustajallesi kyvyn olla vuorovaikutuksessa eri kehitystyökalujen ja -palvelujen kanssa.

### Ongelma, jonka MCP-palvelimet ratkaisevat

Ennen MCP-palvelimia, jos halusit:
- Tarkistaa Azure-resurssisi
- Luoda GitHub-ongelman 
- Kysellä tietokannastasi
- Etsiä dokumentaatiosta

Sinun piti lopettaa koodaus, avata selain, siirtyä sopivalle verkkosivulle ja suorittaa nämä tehtävät manuaalisesti. Tämä jatkuva kontekstin vaihtaminen katkaisee työnkulun ja vähentää tuottavuutta.

### Miten MCP-palvelimet mullistavat kehityskokemuksen

MCP-palvelimien avulla voit pysyä kehitysympäristössäsi (VS Code, Visual Studio jne.) ja yksinkertaisesti pyytää tekoälyavustajaasi hoitamaan nämä tehtävät. Esimerkiksi:

**Perinteisen työnkulun sijaan:**
1. Lopeta koodaus
2. Avaa selain
3. Mene Azure-portaaliin
4. Tarkista tallennustilin tiedot
5. Palaa VS Codeen
6. Jatka koodausta

**Voit nyt tehdä tämän:**
1. Kysy tekoälyltä: "Mikä on Azure-tallennustilieni tila?"
2. Jatka koodausta saamiesi tietojen perusteella

### Keskeiset edut aloittelijoille

#### 1. 🔄 **Pysy virtaustilassa**
- Lopeta sovellusten välillä hyppiminen
- Keskity koodaukseen, jota teet
- Vähennä erilaisten työkalujen hallinnan muistikuormaa

#### 2. 🤖 **Käytä luonnollista kieltä monimutkaisten komentojen sijaan**
- Sen sijaan, että muistat SQL-syntaksin, kuvaile tarvitsemasi tiedot
- Sen sijaan, että muistaisit Azure CLI -komennot, kerro, mitä haluat saavuttaa
- Anna tekoälyn hoitaa tekniset yksityiskohdat, kun keskityt logiikkaan

#### 3. 🔗 **Yhdistä useita työkaluja**
- Luo tehokkaita työnkulkuja yhdistämällä eri palveluja
- Esimerkki: "Hae kaikki viimeisimmät GitHub-ongelmat ja luo niistä vastaavat Azure DevOps -työtehtävät"
- Rakenna automaatiota ilman monimutkaisia skriptejä

#### 4. 🌐 **Pääsy kasvavaan ekosysteemiin**
- Hyödynnä Microsoftin, GitHubin ja muiden yritysten rakentamia palvelimia
- Yhdistä ja käytä saumattomasti eri toimittajien työkaluja
- Liity standardoituneeseen ekosysteemiin, joka toimii eri tekoälyavustajien kanssa

#### 5. 🛠️ **Opi tekemällä**
- Aloita valmiilla palvelimilla ymmärtääksesi käsitteet
- Rakenna vähitellen omia palvelimiasi, kun tunnet olosi mukavammaksi
- Käytä saatavilla olevia SDK:ita ja dokumentaatiota oppaana

### Todellinen esimerkki aloittelijoille

Oletetaan, että olet uusi web-kehityksessä ja työskentelet ensimmäisen projektisi parissa. Näin MCP-palvelimet voivat auttaa:

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

**MCP-palvelimien kanssa:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Yritystason standardin etu

MCP on kasvamassa teollisuuden laajuiseksi standardiksi, mikä tarkoittaa:
- **Johdonmukaisuus**: Samankaltainen käyttökokemus eri työkalujen ja yritysten välillä
- **Yhteentoimivuus**: Eri toimittajien palvelimet toimivat yhdessä
- **Tulevaisuuden kestävyys**: Taidot ja asetukset siirtyvät eri tekoälyavustajien välillä
- **Yhteisö**: Laaja jaettu tietämyksen ja resurssien ekosysteemi

### Aloittaminen: Mitä opit

Tässä oppaassa tutustumme 10 Microsoftin MCP-palvelimeen, jotka ovat erityisen hyödyllisiä kehittäjille kaikilla tasoilla. Jokainen palvelin on suunniteltu:
- Ratkaisemaan yleisiä kehityshaasteita
- Vähentämään toistuvia tehtäviä
- Parantamaan koodin laatua
- Lisäämään oppimismahdollisuuksia

> **💡 Oppimisvinkki**
> 
> Jos olet täysin uusi MCP:ssä, aloita meidän [Johdanto MCP:hen](../00-Introduction/README.md) ja [Peruskäsitteet](../01-CoreConcepts/README.md) -moduuleista. Palaa sitten tänne näkemään nämä käsitteet käytännössä todellisten Microsoft-työkalujen kanssa.
>
> Lisätaustaa MCP:n merkityksestä saat Maria Naggagan kirjoituksesta: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## MCP:n käyttöönotto VS Codessa ja Visual Studiossa 🚀

Näiden MCP-palvelimien perustaminen on suoraviivaista, jos käytät Visual Studio Codea tai Visual Studio 2022:ta GitHub Copilotin kanssa.

### VS Coden asetukset

Perusprosessi VS Codessa on seuraava:

1. **Ota käyttöön agenttitila**: Vaihda Copilot Chat -ikkunassa agenttitilaan
2. **Määritä MCP-palvelimet**: Lisää palvelinkonfiguraatiot settings.json -tiedostoon
3. **Käynnistä palvelimet**: Klikkaa "Start" painiketta jokaiselle käytettävälle palvelimelle
4. **Valitse työkalut**: Valitse, mitkä MCP-palvelimet otetaan käyttöön nykyisessä istunnossa

Yksityiskohtaiset asennusohjeet löytyvät [VS Code MCP -dokumentaatiosta](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Vinkki ammattilaisille: Hallitse MCP-palvelimia kuin ammattilainen!**
> 
> VS Coden Extensions-näkymään on nyt lisätty [kätevä uusi käyttöliittymä asennettujen MCP-palvelimien hallintaan](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Saat nopean pääsyn käynnistämään, pysäyttämään ja hallitsemaan mitä tahansa asennettuja MCP-palvelimia selkeän ja yksinkertaisen käyttöliittymän kautta. Kokeile jo tänään!

### Visual Studio 2022:n asetukset

Visual Studio 2022:ssa (versio 17.14 tai uudempi):

1. **Ota käyttöön agenttitila**: Klikkaa "Ask" -alasvetovalikkoa GitHub Copilot Chat -ikkunassa ja valitse "Agent"
2. **Luo konfiguraatiotiedosto**: Luo `.mcp.json` -tiedosto ratkaisukansioon (suositeltu sijainti: `<SOLUTIONDIR>\.mcp.json`)
3. **Määritä palvelimet**: Lisää MCP-palvelinkonfiguraatiot standardin MCP-muodon mukaisesti
4. **Työkalujen hyväksyminen**: Kun sinulta pyydetään, hyväksy työkalut, joita haluat käyttää sopivin oikeuksin

Yksityiskohtaiset Visual Studio -asetusohjeet löytyvät [Visual Studio MCP -dokumentaatiosta](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Jokaisella MCP-palvelimella on omat konfiguraatiovaatimuksensa (yhteysmerkkijonot, todennukset jne.), mutta asetusmalli on yhtenäinen molemmissa IDE:issä.

## Opit Microsoft MCP -palvelimista 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mitä se tekee**: Microsoft Learn Docs MCP Server on pilvipalvelu, joka tarjoaa tekoälyavustajille reaaliaikaisen pääsyn viralliseen Microsoft-dokumentaatioon Model Context Protocolin kautta. Se yhdistää `https://learn.microsoft.com/api/mcp` ja mahdollistaa semanttisen haun Microsoft Learnissa, Azure-dokumentaatiossa, Microsoft 365 -dokumentaatiossa ja muissa virallisissa Microsoft-lähteissä.

**Miksi se on hyödyllinen**: Vaikka se saattaa vaikuttaa "vain dokumentaatiolta", tämä palvelin on todella ratkaiseva jokaiselle Microsoft-teknologioita käyttävälle kehittäjälle. Yksi suurimmista valituksista .NET-kehittäjiltä tekoälykoodausavustajista on, etteivät ne ole ajan tasalla uusimpien .NET- ja C#-julkaisujen kanssa. Microsoft Learn Docs MCP Server ratkaisee tämän tarjoamalla reaaliaikaisen pääsyn ajantasaisimpaan dokumentaatioon, API-viitteisiin ja parhaisiin käytäntöihin. Olipa kyse viimeisimmistä Azure SDK:ista, uusien C# 13 -ominaisuuksien tutkimisesta tai huippuluokan Aspire-mallien toteuttamisesta, tämä palvelin varmistaa, että tekoälyavustajasi saa käyttöönsä auktoriteettisen ja ajan tasalla olevan tiedon tuottaakseen tarkkaa ja modernia koodia.

**Todellisessa käytössä**: "Mitkä ovat az-cli-komennot Azure Container Appin luomiseksi virallisen Microsoft Learn -dokumentaation mukaan?" tai "Miten konfiguroin Entity Frameworkin riippuvuuksien injektoinnilla ASP.NET Core -sovelluksessa?" Tai entä "Tarkista tämä koodi varmistaaksesi, että se vastaa Microsoft Learn -dokumentaation suorituskykysuosituksia." Palvelin tarjoaa kattavan haun Microsoft Learnista, Azure-dokumenteista ja Microsoft 365 -dokumentaatiosta käyttäen edistynyttä semanttista hakua löytääkseen kontekstuaalisesti relevanttimmat tiedot. Se palauttaa jopa 10 korkealaatuista sisältölohkoa artikkelien otsikoilla ja URL-osoitteilla, päästen aina viimeisimpiin Microsoft-dokumentaatioihin niiden julkaisun myötä.

**Korostettu esimerkki**: Palvelin tarjoaa `microsoft_docs_search` -työkalun, joka suorittaa semanttista hakua Microsoftin virallista teknistä dokumentaatiota vastaan. Kun se on konfiguroitu, voit esittää kysymyksiä kuten "Miten toteutan JWT-todennuksen ASP.NET Core -sovelluksessa?" ja saada yksityiskohtaisia, virallisia vastauksia lähdelinkkeineen. Haun laatu on erinomainen, koska se ymmärtää kontekstin – kun kysyt "kontteja" Azure-kontekstissa, saat Azure Container Instances -dokumentaation, kun taas sama termi .NET-kontekstissa palauttaa asiaankuuluvat C#-kokoelmatiedot.

Tämä on erityisen hyödyllistä nopeasti muuttuville tai äskettäin päivitetyille kirjastoille ja käyttötapauksille. Esimerkiksi muutamissa äskettäisissä koodausprojekteissani halusin hyödyntää Aspire- ja Microsoft.Extensions.AI-kirjastojen uusimman julkaisun ominaisuuksia. Sisällyttämällä Microsoft Learn Docs MCP -palvelimen sain hyödyntää paitsi API-dokumentaatiota myös juuri julkaistuja läpikäyntejä ja ohjeistuksia.

> **💡 Vinkki ammattilaisille**
> 
> Myös työkaluille ystävälliset mallit tarvitsevat kannustusta MCP-työkalujen käyttämiseen! Harkitse järjestelmäkehotteen tai [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) lisäämistä, kuten: "Sinulla on pääsy `microsoft.docs.mcp` – käytä tätä työkalua hakeaksesi Microsoftin uusinta virallista dokumentaatiota käsitellessäsi Microsoft-teknologioihin liittyviä kysymyksiä, kuten C#, Azure, ASP.NET Core tai Entity Framework."
>
> Erinomaiseen esimerkkiin tästä käytännössä tutustut [C# .NET Janitor chat-tilassa](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) Awesome GitHub Copilot -varastossa. Tämä tila hyödyntää erityisesti Microsoft Learn Docs MCP -palvelinta auttaakseen puhdistamaan ja modernisoimaan C#-koodia uusimpien mallien ja parhaiden käytäntöjen mukaisesti.
### 2. ☁️ Azure MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mitä se tekee**: Azure MCP Server on kattava yli 15 erikoistuneen Azure-palveluliitännän kokoelma, joka tuo koko Azure-ekosysteemin tekoälytyönkulkuusi. Tämä ei ole vain yksi palvelin – se on voimakas kokoelma, joka sisältää resurssien hallinnan, tietokantayhteydet (PostgreSQL, SQL Server), Azure Monitorin lokianalyysin KQL:llä, Cosmos DB -integraation ja paljon muuta.

**Miksi se on hyödyllinen**: Pelkän Azure-resurssien hallinnan lisäksi tämä palvelin parantaa dramaattisesti koodin laatua työskennellessäsi Azure SDK:iden kanssa. Kun käytät Azure MCP:tä agenttitilassa, se ei vain auta sinua kirjoittamaan koodia – se auttaa sinua kirjoittamaan *parempaa* Azure-koodia, joka noudattaa nykyisiä todennusmalleja, virheenkäsittelyn parhaita käytäntöjä ja hyödyntää uusimpia SDK-ominaisuuksia. Saat koodia, joka noudattaa Azureen suositeltuja tuotantokuormien malleja, sen sijaan että saisit geneeristä koodeja, jotka saattavat toimia.

**Keskeisiä moduuleja ovat**:
- **🗄️ Tietokantaliittimet**: Suora luonnolliskielinen pääsy Azure Database for PostgreSQL:ään ja SQL Serveriin
- **📊 Azure Monitor**: KQL-pohjainen lokianalyysi ja operatiiviset näkymät
- **🌐 Resurssien hallinta**: Täysi Azure-resurssien elinkaaren hallinta
- **🔐 Todennus**: DefaultAzureCredential ja hallinnoidut identiteettimallit
- **📦 Tallennuspalvelut**: Blob Storage, Queue Storage ja Table Storage -operaatiot
- **🚀 Säilöpalvelut (Container Services)**: Azure Container Apps, Container Instances ja AKS-hallinta
- **Ja monia muita erikoistuneita liittimiä**

**Todellisessa käytössä**: "Listaa Azure-tallennustilini", "Kysy Log Analytics -työtilastani virheitä viimeisen tunnin ajalta" tai "Auta rakentamaan Azure-sovellus Node.js:llä asianmukaisella todennuksella"

**Täydellinen demo-tapaus**: Tässä on täydellinen läpikäynti, joka näyttää Azure MCP:n ja GitHub Copilot for Azure -laajennuksen voiman VS Codessa. Kun molemmat ovat asennettuina ja kehote annettu:

> "Luo Python-skripti, joka lataa tiedoston Azure Blob Storageen käyttäen DefaultAzureCredential-todennusta. Skriptin tulisi yhdistää Azure-tallennustiliini nimeltä 'mycompanystorage', ladata säiliöön nimeltä 'documents', luoda ladattava testitiedosto nykyisellä ajankohdalla, käsitellä virheet sujuvasti ja antaa informatiivista palautetta, noudattaa Azuren parhaita käytäntöjä todennuksessa ja virheenkäsittelyssä, sisältää kommentteja, jotka selittävät, miten DefaultAzureCredential-todennus toimii, ja tehdä skriptistä hyvin jäsennelty funktioiden ja dokumentaation kera."

Azuren MCP-palvelin luo täydellisen, tuotantovalmiin Python-skriptin, joka:
- Käyttää uusinta Azure Blob Storage SDK:ta asianmukaisilla asynkronisilla malleilla
- Toteuttaa DefaultAzureCredentialin kattavalla varajärjestyksen selityksellä
- Sisältää vankan virheenkäsittelyn Azurea koskevine erityispoikkeuksineen
- Noudattaa Azure SDK:n parhaita käytäntöjä resurssien hallinnassa ja yhteyksien käsittelyssä
- Tarjoaa yksityiskohtaista lokitusta ja informatiivisia konsolilähtöjä
- Luo asianmukaisesti jäsennellyn skriptin, jossa on funktioita, dokumentaatiota ja tyyppiviitteitä

Mikä tekee tästä merkittävän, on se, että ilman Azuren MCP:tä saisit yleensä geneeristä blob-tallennuskoodia, joka toimii, mutta ei noudata nykyisiä Azure-malleja. Azuren MCP:llä saat koodin, joka hyödyntää uusimpia todennusmenetelmiä, käsittelee Azureen liittyviä erityisiä virhetilanteita ja noudattaa Microsoftin suosituksia tuotantosovelluksissa.

**Esimerkkitapaus**: Minulla on ollut vaikeuksia muistaa tarkkoja käskyjä `az` ja `azd` CLI:lle ad-hoc-käytössä. Se on aina minulle kaksivaiheinen prosessi: ensin etsin syntaksin, sitten suoritan komennon. Usein menen vain portaalin kautta klikkaamaan homman hoidettuani, koska en halua myöntää, etten muista CLI-syntaksia. Mahdollisuus vain kuvailla haluamani asia on mahtavaa, ja vielä parempi, että sen voi tehdä ilman, että pitää poistua IDE:stäni!

Löydät erinomaisen listan käyttötapauksista [Azure MCP -varastosta](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) aloitukseksi. Kattavia asennusohjeita ja edistyneitä konfigurointivaihtoehtoja löytyy [virallisesta Azure MCP -dokumentaatiosta](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mitä se tekee**: Virallinen GitHub MCP Server tarjoaa saumattoman integraation GitHubin koko ekosysteemiin, tarjoten sekä isännöidyn etäkäytön että paikallisen Docker-asennuksen vaihtoehtoja. Tämä ei ole vain perustoimintojen hallintaa – kyseessä on kattava työkalupaketti, joka sisältää GitHub Actionsin hallinnan, pull request -työnkulut, issue-seurannan, turvallisuusskannaukset, ilmoitukset ja edistyneet automaatiokyvyt.

**Miksi se on hyödyllinen**: Tämä palvelin muuttaa tapasi olla vuorovaikutuksessa GitHubin kanssa tuomalla koko alustan käyttökokemuksen suoraan kehitysympäristöösi. Sen sijaan, että jatkuvasti vaihtaisit VS Coden ja GitHub.comin välillä projektinhallinnassa, koodikatselmuksissa ja CI/CD-valvonnassa, voit hoitaa kaiken luonnollisilla kielikomennoilla keskittyessäsi koodiin.

> **ℹ️ Huomautus: Eri tyyppisiä 'Agentteja'**
> 
> Älä sekoita tätä GitHub MCP Serveriä GitHubin Coding Agenttiin (tekoälyagentti, jolle voi määrittää issueita automatisoituihin kooditehtäviin). GitHub MCP Server toimii VS Coden Agent-tilassa tarjoten GitHub API -integraation, kun taas GitHubin Coding Agent on erillinen ominaisuus, joka luo pull requesteja, kun se on määritetty GitHub-issuisiin.

**Keskeiset ominaisuudet**:
- **⚙️ GitHub Actions**: Täydellinen CI/CD-putkihallinta, työnkulun valvonta ja artefaktien käsittely
- **🔀 Pull Requestit**: Luo, tarkista, yhdistä ja hallinnoi PR:itä kattavalla tilaseurannalla
- **🐛 Issues**: Kattava issueiden elinkaaren hallinta, kommentointi, merkintä ja määrittely
- **🔒 Turvallisuus**: Koodin skannausvaroitukset, salaisuuksien tunnistus ja Dependabot-integraatio
- **🔔 Ilmoitukset**: Älykäs ilmoitusten hallinta ja repositorion tilausvalvonta
- **📁 Repositorion hallinta**: Tiedostojen käsittely, haarojen hallinta ja varaston hallinnointi
- **👥 Yhteistyö**: Käyttäjä- ja organisaatiohaut, tiimien hallinta ja käyttöoikeuksien hallinta

**Todellinen käyttö**: "Luo pull request ominaisuushaarastani", "Näytä kaikki epäonnistuneet CI-ajot tällä viikolla", "Listaa avoimet turvallisuusvaroitukset repositorioillani" tai "Etsi kaikki minulle määritellyt issuet organisaatioistani"

**Täysi demotilanne**: Tässä on tehokas työnkulku, joka demonstroi GitHub MCP Serverin kykyjä:

> "Minun täytyy valmistautua sprinttikatsaukseen. Näytä kaikki tänä viikon luomani pull requestit, tarkista CI/CD-putkien tila, laadi yhteenveto ratkaistavista turvallisuusvaroituksista ja auta minua laatimaan julkaisumuistiinpanot yhdistetyistä 'feature'-liputetuista PR:stä."

GitHub MCP Server:
- Kysyy äskettäiset pull requestisi yksityiskohtaisine tilatietoineen
- Analysoi työnkulkuajot ja korostaa kaikki epäonnistumiset tai suorituskykyongelmat
- Koostaa turvallisuusskannauksen tulokset ja asettaa kriittiset varoitukset etusijalle
- Luo kattavat julkaisumuistiinpanot poimimalla tietoa yhdistetyistä PR:istä
- Tarjoaa käytännön toimenpide-ehdotukset sprintin suunnitteluun ja julkaisun valmisteluun

**Esimerkkitapaus**: Rakastan käyttää tätä koodikatselmointityönkuluissa. Sen sijaan, että hyppäisin VS Coden, GitHub-ilmoitusten ja pull request -sivujen välillä, sanon vain "Näytä kaikki PR:t, jotka odottavat arviointiani" ja sitten "Lisää kommentti PR:ään #123 kysyen virheenkäsittelystä todennustavassa." Palvelin hoitaa GitHub API -kutsut, ylläpitää keskustelun kontekstin ja auttaa minua jopa laatimaan rakentavampia kommentteja.

**Todennusvaihtoehdot**: Palvelin tukee sekä OAuthia (saumaton VS Codessa) että henkilökohtaisia käyttöoikeustunnuksia, ja työkalut voidaan konfiguroida käyttämään vain tarvitsemaasi GitHub-toiminnallisuutta. Sen voi ajaa etäisännöitynä palveluna nopeaan käyttöönottoon tai paikallisesti Dockerin kautta täydelliseen hallintaan.

> **💡 Vinkki**
> 
> Ota käyttöön vain tarvitsemiasi työkalusarjoja määrittämällä `--toolsets`-parametri MCP-palvelinasetuksissasi vähentääksesi kontekstikokoa ja parantaaksesi tekoälytyökalujen valintaa. Lisää esimerkiksi `"--toolsets", "repos,issues,pull_requests,actions"` MCP-konfiguraatioargmenteihisi ydinkehitystyönkulkuihin, tai käytä `"--toolsets", "notifications, security"`, jos haluat enimmäkseen GitHubin valvontamahdollisuudet.
### 4. 🔄 Azure DevOps MCP Server

[![Asenna VS Codeen](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Asenna VS Code Insidersiin](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mitä se tekee**: Yhdistää Azure DevOps -palveluihin kattavaa projektinhallintaa, työtehtävien seurantaa, build-putkiston hallintaa ja varastotoimintoja varten.

**Mikä tekee siitä hyödyllisen**: Tiimeille, jotka käyttävät Azure DevOpsia ensisijaisena DevOps-alustanaan, tämä MCP-palvelin poistaa jatkuvan välilehtien vaihtamisen kehitysympäristön ja Azure DevOpsin verkkokäyttöliittymän välillä. Voit hallita työtehtäviä, tarkistaa rakennustilanteet, kysyä arkistoja ja hoitaa projektinhallintatehtäviä suoraan AI-avustajaltasi.

**Käytännön esimerkki**: "Näytä minulle kaikki aktiiviset työtehtävät nykyisessä sprintissä WebApp-projektille", "Luo virheraportti äsken löytyneestä kirjautumisongelmasta" tai "Tarkista rakennustemme putkien tila ja näytä viimeisimmät virheet"

**Esimerkkitapaus**: Voit helposti tarkistaa tiimisi nykyisen sprintin tilan yksinkertaisella kyselyllä kuten "Näytä minulle kaikki aktiiviset työtehtävät nykyisessä sprintissä WebApp-projektille" tai "Luo virheraportti äsken löytyneestä kirjautumisongelmasta" ilman, että sinun tarvitsee poistua kehitysympäristöstäsi.

### 5. 📝 MarkItDown MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mitä se tekee**: MarkItDown on kattava dokumenttien muunto-palvelin, joka muuttaa erilaisia tiedostomuotoja korkealaatuiseksi Markdowniksi, optimoituna LLM:n kulutukseen ja tekstianalyysityönkulkuihin.

**Miksi se on hyödyllinen**: Olennaista nykyaikaisissa dokumentaatiotyönkuluissa! MarkItDown käsittelee vaikuttavan valikoiman tiedostomuotoja säilyttäen samalla kriittiset dokumentin rakenteet kuten otsikot, luettelot, taulukot ja linkit. Toisin kuin yksinkertaiset tekstin poisto-ohjelmat, se keskittyy merkityksen ja muotoilun säilyttämiseen, mikä on arvokasta sekä AI-käsittelyssä että ihmisten luettavuudessa.

**Tuetut tiedostomuodot**:
- **Toimistodokumentit**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Media-tiedostot**: Kuvia (EXIF-metatiedoin ja OCR:llä), Ääni (EXIF-metatiedoin ja puheen tekstityksellä)
- **Web-sisältö**: HTML, RSS-syötteet, YouTube-URL:t, Wikipedia-sivut
- **Tietomuodot**: CSV, JSON, XML, ZIP-tiedostot (käsittelee sisällön rekursiivisesti)
- **Julkaisumuodot**: EPub, Jupyter-muistikirjat (.ipynb)
- **Sähköposti**: Outlook-viestit (.msg)
- **Edistynyt**: Azure Document Intelligence -integraatio paranneltuun PDF-käsittelyyn

**Edistyneet ominaisuudet**: MarkItDown tukee LLM-pohjaisia kuvausominaisuuksia kuville (kun käytettävissä on OpenAI-asiakas), Azure Document Intelligencea paranneltuun PDF-käsittelyyn, puheen tekstitystä äänisisällöissä sekä laajennusjärjestelmää lisätiedostomuotojen tukemiseksi.

**Käytännön esimerkki**: "Muunna tämä PowerPoint-esitys Markdowniksi dokumentaatiopalvelua varten", "Poimi teksti tästä PDF:stä oikealla otsikkorakenteella" tai "Muunna tämä Excel-taulukko luettavaksi taulukkomuodoksi"

**Esimerkkitapaus (parafraasi)**: 
[MarkItDown-dokumentaatio](https://github.com/microsoft/markitdown#why-markdown) selittää,
että Markdown säilyttää dokumentin rakenteen vähäisellä muotoilukuormalla.
Kielenmallit tuottavat yleisesti Markdownia, mikä tekee siitä hyödyllisen ja token-tehokkaan
formaatin dokumenttien käsittelyyn.

MarkItDown on todella hyvä säilyttämään dokumentin rakennetta, joka on tärkeää AI-työnkuluissa. Esimerkiksi PowerPoint-esitystä muuntaessa se säilyttää diojen järjestyksen oikeilla otsikoilla, poimii taulukot Markdown-taulukoina, sisältää vaihtoehtoisen tekstin kuville ja käsittelee jopa puhujan muistiinpanot. Kaaviot muunnetaan luettaviksi datataulukoiksi ja tuloksena syntyvä Markdown säilyttää alkuperäisen esityksen loogisen rakenteen. Tämä tekee siitä täydellisen esityssisällön syöttämiseen AI-järjestelmiin tai dokumentaation luomiseen olemassa olevista dioista.
### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mitä se tekee**: Tarjoaa keskustelukäyttöliittymän SQL Server -tietokantoihin (paikalliset, Azure SQL tai Fabric)

**Miksi se on hyödyllinen**: Vastaava kuin PostgreSQL-palvelin, mutta Microsoft SQL -ekosysteemille. Yhdistä yksinkertaisella yhteysmerkkijonolla ja aloita luonnollisella kielellä kyselyt – ei enää kontekstinvaihtoa!

**Käytännön esimerkki**: "Etsi kaikki tilaukset, joita ei ole täytetty viimeisten 30 päivän aikana" käännetään sopiviksi SQL-kyselyiksi ja palauttaa muotoillut tulokset

**Esimerkkitapaus**: Kun yhteys tietokantaan on asetettu, voit aloittaa keskustelun datasi kanssa välittömästi. Blogikirjoitus esittelee tämän yksinkertaisella kysymyksellä: "mihin tietokantaan olet yhteydessä?" MCP-palvelin vastaa kutsumalla sopivaa tietokantatyökalua, yhdistämällä SQL Serverisi instanssiin ja palauttamalla yksityiskohtia nykyisestä tietokantayhteydestä – eikä sinun tarvitse kirjoittaa riviäkään SQL:ää. Palvelin tukee kattavia tietokantatoimintoja skeeman hallinnasta datan muokkaukseen, kaikki luonnollisen kielen kehotteilla. Täydelliset asennusohjeet ja konfiguraatioesimerkit VS Coden ja Claude Desktopin kanssa löytyvät: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mitä se tekee**: Mahdollistaa AI-agenttien vuorovaikutuksen verkkosivujen kanssa testauksessa ja automaatiossa

> **ℹ️ GitHub Copilotin moottorina**
> 
> Playwright MCP Server toimii GitHub Copilotin Coding Agenttin moottorina, antaen sille verkkoselailuominaisuudet! [Lue tästä ominaisuudesta lisää](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miksi se on hyödyllinen**: Täydellinen luonnollisella kielellä ohjatulle automatisoidulle testaukselle. AI voi navigoida verkkosivuilla, täyttää lomakkeita ja poimia dataa rakenteellisten saavutettavuuskuvien avulla – tämä on uskomattoman tehokasta!

**Käytännön esimerkki**: "Testaa kirjautumisprosessi ja varmista, että hallintapaneeli latautuu oikein" tai "Luo testi, joka etsii tuotteita ja validoi tulossivun" – kaikki ilman, että tarvitsee sovelluksen lähdekoodia

**Esimerkkitapaus**: Työtoverini Debbie O'Brien on tehnyt huikeaa työtä Playwright MCP Serverin kanssa viime aikoina! Esimerkiksi hän osoitti äskettäin, miten voi generoida täydellisiä Playwright-testejä ilman pääsyä sovelluksen lähdekoodiin. Hänen tilanteessaan hän pyysi Copilotia luomaan testin elokuhaushakusovellukselle: siirry sivustolle, hae "Garfield" ja varmista että elokuva näkyy tuloksissa. MCP käynnisti selaussession, tutki sivun rakennetta DOM-kuvien avulla, selvitti oikeat valitsimet ja loi täysin toimivan TypeScript-testin, joka läpäisi ensimmäisellä ajolla.

Sen voiman salaisuus on siinä, että se yhdistää luontevan kielen ohjeistuksen ja suoritettavan testikoodin. Perinteiset menetelmät vaativat joko manuaalista testien kirjoittamista tai pääsyä koodipohjaan kontekstin saamiseksi. Mutta Playwright MCP:n avulla voit testata ulkoisia sivustoja, asiakasohjelmia tai toimia mustan laatikon testaus -tilanteissa, joissa koodiin ei ole pääsyä.  


### 8. 💻 Dev Box MCP Server  

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)  

**Mitä se tekee**: Hallinnoi Microsoft Dev Box -ympäristöjä luonnollisen kielen avulla  

**Miksi se on hyödyllinen**: Yksinkertaistaa kehitysympäristöjen hallintaa huomattavasti! Luo, määritä ja hallitse kehitysympäristöjä ilman, että tarvitsee muistaa tarkkoja komentoja.  

**Käytännön esimerkki**: "Luo uusi Dev Box uusimmalla .NET SDK:lla ja määritä se projektiamme varten", "Tarkista kaikkien kehitysympäristöjeni tila" tai "Luo standardoitu demo-ympäristö tiimiesityksiämme varten"  

**Esimerkkitapaus**: Olen suuri fani Dev Boxin käytöstä henkilökohtaisessa kehityksessä. Minun valaiseva hetkeni oli, kun James Montemagno kertoi, kuinka loistava Dev Box on konferenssidemoihin, koska siinä on erittäin nopea ethernet-yhteys riippumatta siitä, käytänkö konferenssin, hotellin tai lentokoneen wifiä. Itse asiassa harjoittelin äskettäin konferenssidemoa, kun kannettava tietokoneeni oli yhdistetty puhelimeni hotspotin kautta matkalla bussilla Bruggeistä Antwerpeniin! Seuraava askeleeni on tutkia tiimien hallintaa useille kehitysympäristöille ja standardoituja demo-ympäristöjä. Toinen merkittävä käyttötapaus, josta olen kuullut asiakkailta ja työkavereilta, on valmiiksi määritettyjen kehitysympäristöjen käyttö Dev Boxilla. Molemmissa tapauksissa MCP:n käyttö Dev Boxien määrittämiseen ja hallintaan mahdollistaa luonnollisen kielisen vuorovaikutuksen, pysyen samalla omassa kehitysympäristössä.  

### 9. 🤖 Microsoft Foundry MCP Server  

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)  

**Mitä se tekee**: Microsoft Foundry MCP Server tarjoaa kehittäjille kattavan pääsyn Azuren tekoälyekosysteemiin, mukaan lukien mallikatalogit, käyttöönoton hallinta, tiedon indeksointi Azure AI Searchin avulla ja arviointityökalut. Tämä kokeellinen palvelin yhdistää tekoälyn kehityksen ja Azuren tehokkaan tekoälyinfrastruktuurin, jolloin tekoälysovellusten rakentaminen, käyttöönotto ja arviointi on helpompaa.  

**Miksi se on hyödyllinen**: Tämä palvelin muuttaa tapasi työskennellä Azure AI -palvelujen kanssa tuomalla yritystason tekoälyominaisuudet suoraan kehitystyöhön. Sen sijaan, että vaihtelisit Azuren portaalin, dokumentaation ja IDE:n välillä, voit löytää malleja, ottaa palveluja käyttöön, hallita tietopohjia ja arvioida tekoälyn suorituskykyä luonnollisen kielen komennoilla. Se on erityisen tehokas RAG (Retrieval-Augmented Generation) -sovelluksia rakentaville kehittäjille, monimallien hallinnoijille tai kattavien tekoälyarviointiputkien toteuttajille.  

**Tärkeimmät kehittäjäominaisuudet**:  
- **🔍 Mallien löytäminen ja käyttöönotto**: Tutki Microsoft Foundryn mallikatalogia, saa yksityiskohtaista mallin tietoa koodiesimerkkien kera ja ota malleja käyttöön Azure AI Servicesissä  
- **📚 Tiedon hallinta**: Luo ja hallitse Azure AI Search -indeksejä, lisää dokumentteja, määritä indeksoijat ja rakenna monimutkaisia RAG-järjestelmiä  
- **⚡ AI-agenttien integrointi**: Yhdistä Azure AI Agentteihin, kysy olemassa olevilta agenteilta ja arvioi agenttien toimintaa tuotantotilanteissa  
- **📊 Arviointikehys**: Suorita kattavia teksti- ja agenttiarviointeja, generoi markdown-raportteja ja toteuta laadunvarmistusta tekoälysovelluksille  
- **🚀 Prototyyppityökalut**: Saat ohjeet GitHub-pohjaiseen prototypointiin ja pääsyn Microsoft Foundry Labsiin huippututkimusmalleja varten  

**Käytännön kehittäjäesimerkki**: "Ota Phi-4-malli käyttöön Azure AI Servicesissä sovellukselleni", "Luo uusi hakemisto dokumentaation RAG-järjestelmälleni", "Arvioi agenttini vastaukset laatukriteerien perusteella" tai "Löydä paras päättelymalli monimutkaisiin analyysitehtäviini"  

**Täydellinen demoskenaario**: Tässä tehokas tekoälyn kehitystyönkulku:  

> "Rakennan asiakastukagenttia. Auta minua löytämään hyvä päättelymalli katalogista, ottamaan se käyttöön Azure AI Servicesissä, luomaan tietopohjan dokumentaatiostamme, perustamaan arviointikehys vastausten laadun testaamiseksi ja auttamaan integraation prototypoinnissa GitHub-tokenilla testausta varten."  

Microsoft Foundry MCP Server tekee seuraavat:  
- Kysyy mallikatalogia suositellakseen parhaita päättelymalleja vaatimustesi perusteella  
- Tarjoaa käyttöönotto-komentoja ja kiintiötietoja valitsemallesi Azure-alueelle  
- Asettaa Azure AI Search -hakemistoja oikeilla kaavoilla dokumentaatiollesi  
- Määrittää arviointiputkia laatumittareilla ja turvallisuustarkistuksilla  
- Generoi prototypointikoodia GitHub-todennuksella välitöntä testausta varten  
- Tarjoaa kattavat asennusoppaat juuri sinun teknologiapinoosi sopiviksi  

**Esimerkkitapaus**: Kehittäjänä minulla on ollut vaikeuksia pysyä mukana kaikissa saatavilla olevissa LLM-malleissa. Tunnen muutaman päämallin, mutta olen tuntenut jääväni paitsi tuottavuus- ja tehokkuusetuuksista. Tokeneiden ja kiintiöiden hallinta on stressaavaa ja haastavaa – en koskaan tiedä, valitsenko oikean mallin oikeaan tehtävään vai kulutanko budjettia tehotta. Kuulin tästä MCP-palvelimesta James Montemagnolta, kun kyselin tiimiläisiltä MCP-palvelinsuosituksia tätä postausta varten, ja olen innoissani sen käytöstä! Mallinlöytöominaisuudet näyttävät erityisen vaikuttavilta minulle, joka haluan tutkia tavallisten mallien ulkopuolelle ja löytää tehtäviin optimoituja malleja. Arviointikehys auttaa minua varmistamaan, että saan todella parempia tuloksia, en vain kokeile vain kokeilemisen ilosta.  

> **ℹ️ Kokeellinen Tila**  
>  
> Tämä MCP-palvelin on kokeellinen ja aktiivisessa kehityksessä. Ominaisuudet ja rajapinnat saattavat muuttua. Täydellinen Azuren tekoälyominaisuuksien tutkimiseen ja prototyyppien rakentamiseen, mutta tarkista vakausvaatimukset tuotantokäyttöä varten.  
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server  

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)  

**Mitä se tekee**: Tarjoaa kehittäjille olennaiset työkalut tekoälyagenttien ja sovellusten rakentamiseen, jotka integroituvat Microsoft 365:een ja Microsoft 365 Copilotiin, mukaan lukien skeeman validointi, esimerkkikoodien hakeminen ja vianmääritysapu.  

**Miksi se on hyödyllinen**: Microsoft 365:ttä ja Copilotia rakennettaessa täytyy käsitellä monimutkaisia manifestiskeemoja ja tiettyjä kehitysmallimalleja. Tämä MCP-palvelin tuo olennaiset kehitysresurssit suoraan kehitysympäristöön, auttaen validoimaan skeemat, löytämään esimerkkikoodeja ja ratkaisemaan yleisiä ongelmia ilman, että tarvitsee jatkuvasti palata dokumentaatioon.  

**Käytännön esimerkki**: "Validoi deklaratiivinen agenttimani manifesti ja korjaa skeema-virheet", "Näytä esimerkkikoodi Microsoft Graph API -pluginin toteuttamiseen" tai "Auta minua selvittämään Teams-sovellukseni todennusongelmat"  

**Esimerkkitapaus**: Otin yhteyttä ystävääni John Milleriin keskusteltuani hänen kanssaan Build-tapahtumassa M365-agraateista, ja hän suositteli tätä MCP:tä. Tämä voisi olla erinomainen kehittäjille, jotka ovat uusia M365-agenttien kanssa, koska se tarjoaa malleja, esimerkkikoodeja ja rakenteita aloitukseen ilman, että hukkuu dokumentaatioon. Skeeman validointiominaisuudet näyttävät erityisen hyödyllisiltä manifestin rakenteellisten virheiden välttämiseksi, jotka voivat aiheuttaa tuntien vianetsintää.  

> **💡 Vinkki**  
>  
> Käytä tätä palvelinta yhdessä Microsoft Learn Docs MCP Serverin kanssa kokonaisvaltaisen M365-kehitystuen saamiseksi – toinen tarjoaa virallisen dokumentaation, tämä käytännön kehitystyökaluja ja vianmääritysapua.  


## Mitä seuraavaksi? 🔮  

## 📋 Yhteenveto  

Model Context Protocol (MCP) muuttaa tapaa, jolla kehittäjät käyttävät tekoälyavustajia ja ulkoisia työkaluja. Nämä 10 Microsoft MCP -palvelinta osoittavat standardoidun tekoälyintegraation voiman, mahdollistaen saumattomat työnkulut, jotka pitävät kehittäjät keskittyneinä samalla, kun he käyttävät tehokkaita ulkoisia ominaisuuksia.  

Laajasta Azure-ekosysteemin integraatiosta erikoistuneisiin työkaluihin kuten Playwright selaimen automaatioon ja MarkItDown dokumenttien käsittelyyn, nämä palvelimet näyttävät, miten MCP voi parantaa tuottavuutta monipuolisissa kehitystilanteissa. Standardoitu protokolla varmistaa, että nämä työkalut toimivat yhteen saumattomasti ja luovat yhtenäisen kehityskokemuksen.  

MCP-ekosysteemin kehittyessä on tärkeää pysyä mukana yhteisössä, tutkia uusia palvelimia ja rakentaa räätälöityjä ratkaisuja kehitystuottavuuden maksimoimiseksi. MCP:n avoimen standardin ansiosta voit yhdistellä eri toimittajien työkaluja luodaksesi täydellisen työnkulun omiin tarpeisiisi.  

## 🔗 Lisäresurssit  

- [Virallinen Microsoft MCP -varasto](https://github.com/microsoft/mcp)  
- [MCP-yhteisö & Dokumentaatio](https://modelcontextprotocol.io/introduction)  
- [VS Code MCP -dokumentaatio](https://code.visualstudio.com/docs/copilot/copilot-mcp)  
- [Visual Studio MCP -dokumentaatio](https://learn.microsoft.com/visualstudio/ide/mcp-servers)  
- [Azure MCP -dokumentaatio](https://learn.microsoft.com/azure/developer/azure-mcp-server/)  
- [Let's Learn – MCP-tapahtumat](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)  
- [Mahtavat GitHub Copilot -muokkaukset](https://github.com/awesome-copilot)  
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)  
- [MCP Dev Days Live 29./30. heinäkuuta tai katso jälkikäteen](https://aka.ms/mcpdevdays)  

## 🎯 Harjoitukset  

1. **Asenna ja määritä**: Asenna yksi MCP-palvelimista VS Code -ympäristöösi ja testaa perustoiminnallisuus.  
2. **Työnkulun integrointi**: Suunnittele kehitystyönkulku, joka yhdistää vähintään kolme eri MCP-palvelinta.  
3. **Mukautetun palvelimen suunnittelu**: Tunnista tehtävä päivittäisessä kehitysrytmissäsi, josta olisi hyötyä mukautetusta MCP-palvelimesta, ja laadi sille määrittely.  
4. **Suorituskyvyn analyysi**: Vertaa MCP-palvelimien käyttöä perinteisiin menetelmiin yleisissä kehitystehtävissä.  
5. **Turvallisuusarviointi**: Arvioi MCP-palvelimien käytön turvallisuusvaikutukset kehitysympäristössäsi ja ehdota parhaat käytännöt.  


Seuraava: [Parhaat käytännöt](../08-BestPractices/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->