# 🚀 10 Microsoft MCP serverit, mis muudavad arendajate tootlikkust

## 🎯 Mida sa selles juhendis õpid

See praktiline juhend tutvustab kümmet Microsofti MCP serverit, mis muudavad aktiivselt seda, kuidas arendajad töötavad tehisintellekti assistentidega. Selle asemel, et lihtsalt seletada, mida MCP serverid *võivad* teha, näitame servereid, mis juba teevad reaalselt iga päev Microsoftis ja mujal arendustegevuses vahet.

Iga server selles juhendis on valitud põhinedes reaalsel kasutusel ja arendajate tagasisidel. Sa avastad mitte ainult selle, mida iga server teeb, vaid miks see on oluline ja kuidas sellest oma projektides maksimaalselt kasu saada. Olenemata sellest, kas oled MCP-ga täiesti uus või soovid oma olemasolevat seadistust laiendada, esindavad need serverid mõningaid praktilisemaid ja mõjukamaid tööriistu Microsofti ökosüsteemis.

> **💡 Kiirkäivitusnipp**
> 
> MCP-ga uus? Ära muretse! See juhend on loodud algajasõbralikult. Selgitame mõisteid jooksvalt, ja sa võid alati tagasi vaadata meie [Sissejuhatus MCP-sse](../00-Introduction/README.md) ja [Põhimõisted](../01-CoreConcepts/README.md) moodulitesse sügavama tausta saamiseks.

## Ülevaade

See põhjalik juhend uurib kümmet Microsofti MCP serverit, mis muudavad seda, kuidas arendajad suhtlevad tehisintellekti assistentide ja välistööriistadega. Alates Azure ressursihaldusest kuni dokumentide töötlemiseni – need serverid demonstreerivad Model Context Protocol’i jõudu sujuvate ja produktiivsete arendustöövoogude loomisel.

## Õpieesmärgid

Selle juhendi lõpuks sa:
- Saan aru, kuidas MCP serverid parandavad arendajate tootlikkust
- Õpid Microsofti mõjukamaid MCP serveri rakendusi
- Avastad iga serveri praktilisi kasutusjuhtumeid
- Tead, kuidas neid servereid VS Code’is ja Visual Studios seadistada ja konfigureerida
- Uurid laiemat MCP ökosüsteemi ja tuleviku suundi

## 🔧 MCP serverite mõistmine: algaja juhend

### Mis on MCP serverid?

MCP, ehk Model Context Protocol, algajana võid mõelda: "Mis täpselt on MCP server ja miks see mind huvitama peaks?" Alustame lihtsa võrdlusega.

Mõtle MCP servereid kui spetsialiseeritud assistentideks, mis aitavad sinu tehisintellekti koodikaaslasel (näiteks GitHub Copilot) ühendada välistööriistade ja teenustega. Nii nagu kasutad telefonis erinevaid rakendusi erinevate ülesannete jaoks – näiteks ühte ilmaennustuseks, teist navigeerimiseks ja kolmandat panganduseks – annavad MCP serverid sinu AI assistendile võimekus suhelda erinevate arendustööriistade ja teenustega.

### Probleem, mida MCP serverid lahendavad

Enne MCP serverite kasutuselevõttu, kui tahtsid näiteks:
- Kontrollida oma Azure ressursse
- Luua GitHub issue
- Pärida oma andmebaasi
- Otsida dokumentatsioonist

Pidi sa koodi kirjutamise lõpetama, avama brauseri, navigeerima sobivale veebilehele ja need ülesanded käsitsi tegema. See pidev konteksti vahetus katkestas su töövoo ja vähendas tootlikkust.

### Kuidas MCP serverid muudavad sinu arenduskogemust

MCP serveritega võid jääda oma arenduskeskkonda (VS Code, Visual Studio jms) ja lihtsalt paluda oma AI assistendil need ülesanded ära teha. Näiteks:

**Selle asemel traditsiooniline töövoog:**
1. Lõpeta koodi kirjutamine
2. Ava brauser
3. Mine Azure portaali
4. Vaata salvestuskonto andmeid
5. Tule tagasi VS Code’i
6. Jätka koodi kirjutamist

**Nüüd saad teha järgmist:**
1. Küsi AI-lt: "Milline on minu Azure salvestuskontode olek?"
2. Jätka koodi kirjutamist, kasutades saadud infot

### Algajatele olulised eelised

#### 1. 🔄 **Jää samasse töövoogu**
- Pole vaja vahetada mitme rakenduse vahel
- Hoia tähelepanu kirjutataval koodil
- Vähenda mentaalset ülekoormust tööriistade haldamisel

#### 2. 🤖 **Kasuta loomulikku keelt keerukate käskude asemel**
- SQL süntaksi meeldejätmise asemel kirjeldad, millist andmeid vajad
- Azure CLI käskude mäletamise asemel seletad, mida tahad saavutada
- Lase AI-l hallata tehnilisi detaile, sina keskendu loogikale

#### 3. 🔗 **Ühenda mitmed tööriistad omavahel**
- Loo võimsad töövood eraldiseisvate teenuste ühendamisel
- Näide: "Hangi kõik viimased GitHub issue’d ja loo nendega seotud Azure DevOps töökirjed"
- Ehita automatiseerimise ilma keeruka skriptita

#### 4. 🌐 **Juurdepääs kasvavale ökosüsteemile**
- Kasuta Microsofti, GitHubi ja teiste firmade loodud servereid
- Sobita ja ühenda erinevate tarnijate tööriistu sujuvalt
- Liitu standardiseeritud ökosüsteemiga, mis toimib erinevate AI assistentidega

#### 5. 🛠️ **Õpi läbi praktilise kogemuse**
- Alusta valmis serveritega, et mõista kontseptsioone
- Ehita järk-järgult omi servereid, kui oled mugavamaks saanud
- Kasuta SDK-sid ja dokumentatsiooni oma õppeprotsessi juhendamiseks

### Reaalne näide algajatele

Oletame, et oled veebiarenduse uus ning töötad oma esimesel projektis. Siin on, kuidas MCP serverid sind aidata suudavad:

**Traditsiooniline lähenemine:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP serveritega:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Enterprise standardi eelis

MCP saab tööstusharu standardiks, mis tähendab:
- **Järjepidevus**: Sarnane kasutajakogemus erinevate tööriistade ja ettevõtete vahel
- **Ühilduvus**: Erinevate tarnijate serverid töötavad omavahel koos
- **Tulevikukindlus**: Oska ja seadistusi saab üle kanda erinevate AI assistentide vahel
- **Kogukond**: Suur jagatud teadmiste ja ressursside ökosüsteem

### Alustamine: Mida sa õpid

Selles juhendis uurime 10 Microsofti MCP serverit, mis on kasulikud arendajatele igal tasemel. Iga server on loodud selleks, et:
- Lahendada tavalisi arendusprobleeme
- Vähendada korduvaid ülesandeid
- Parandada koodi kvaliteeti
- Suurendada õppimisvõimalusi

> **💡 Õppimisnipp**
> 
> Kui oled MCP-ga täiesti uus, alusta meie [Sissejuhatus MCP](../00-Introduction/README.md) ja [Põhimõisted](../01-CoreConcepts/README.md) moodulitest. Seejärel tule tagasi siia, et näha neid mõisteid praktikas Microsofti tööriistadega.
>
> MCP tähtsuse paremaks mõistmiseks vaata Maria Naggaga postitust: [Ühenda korra, integreeri kõikjal MCP-ga](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Alustamine MCP-ga VS Code’is ja Visual Studios 🚀

Nende MCP serverite seadistamine on lihtne, kui kasutad Visual Studio Code’i või Visual Studio 2022 koos GitHub Copilotiga.

### VS Code’i seadistamine

Põhiline protsess VS Code’is on järgmine:

1. **Luba agendi režiim**: VS Code’is lülitu Copilot Chat aknas Agendi režiimile
2. **Sea MCP serverid**: Lisa serveri konfiguratsioonid oma VS Code seadistuse settings.json faili
3. **Alusta servereid**: Klõpsa “Alusta” nupul iga serveri jaoks, mida tahad kasutada
4. **Vali tööriistad**: Vali, milliseid MCP servereid oma praeguse sessiooni jaoks lubada

Täpsemate seadistamisjuhiste jaoks vaata [VS Code MCP dokumentatsiooni](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Professionaali nipp: halda MCP servereid nagu proff!**
> 
> VS Code laienduste vaates on nüüd [kasulik uus kasutajaliides MCP serverite haldamiseks](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Sul on kiire ligipääs igale paigaldatud MCP serverile käivitamiseks, peatamiseks ja haldamiseks selge, lihtsa liidese kaudu. Proovi järele!

### Visual Studio 2022 seadistamine

Visual Studio 2022 puhul (versioon 17.14 või uuem):

1. **Luba agendi režiim**: Klõpsa GitHub Copilot Chat aknas "Ask" rippmenüüs ja vali "Agent"
2. **Loo konfiguratsioonifail**: Loo oma lahenduse kataloogi `.mcp.json` fail (soovitatav asukoht: `<SOLUTIONDIR>\.mcp.json`)
3. **Sea serverid**: Lisa oma MCP serverite konfiguratsioonid standardse MCP formaadis
4. **Tööriistade heakskiit**: Kui küsitakse, luba tööriistade kasutus sobiva ulatusega õigustega

Täpsemate Visual Studio seadistamisjuhiste jaoks vaata [Visual Studio MCP dokumentatsiooni](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Igal MCP serveril on omad konfiguratsiooninõuded (ühendusstringid, autentimine jne), kuid seadistusprotsess on kummaski IDE-s ühtlane.

## Õppetund Microsofti MCP serveritest 🛠️

### 1. 📚 Microsoft Learn Docs MCP server

[![Paigalda VS Code’is](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Paigalda VS Code Insiders’is](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mida see teeb**: Microsoft Learn Docs MCP server on pilvehostitud teenus, mis annab tehisintellekti assistentidele reaalajas ligipääsu ametlikule Microsofti dokumentatsioonile Model Context Protocoli kaudu. See ühendub aadressiga `https://learn.microsoft.com/api/mcp` ja võimaldab semantilist otsingut Microsoft Learn'i, Azure dokumentatsioonis, Microsoft 365 dokumentatsioonis ja muudes ametlikes Microsofti allikates.

**Miks see on kasulik**: Kuigi tundub, nagu oleks see lihtsalt dokumentatsioon, on see server iga Microsofti tehnoloogiat kasutava arendaja jaoks äärmiselt oluline. Üks suurimaid kaebusi .NET arendajate seas AI-koodi assistentide kohta on see, et nad pole kursis uusimate .NET ja C# versioonidega. Microsoft Learn Docs MCP server lahendab selle, pakkudes reaalajas ligipääsu kõige värskemale dokumentatsioonile, API viidetele ja parimatele tavadele. Olenemata sellest, kas töötad uusimate Azure SDK-dega, uurid uue C# 13 funktsioone või rakendad uuenduslikke Aspire mustreid, tagab see server, et sinu AI assistendil on juurdepääs ametlikele, ajakohastele andmetele täpse ja kaasaegse koodi genereerimiseks.

**Reaalne kasutus**: "Millised on Azure konteinerirakenduse loomise az cli käsud vastavalt ametlikule Microsoft Learn dokumentatsioonile?" või "Kuidas konfigureerida Entity Framework’i sõltuvussüsti ASP.NET Core’is?" Või näiteks "Vaata üle see kood, et olla kindel, et see vastab Microsoft Learn dokumentatsiooni jõudlussoovitustele." Server pakub põhjalikku katvust Microsoft Learn’i, Azure ja Microsoft 365 dokumentatsiooni osas, kasutades täiustatud semantilist otsingut, mis leiab kõige kontekstiga sobivama info. Tagastab kuni 10 kõrgekvaliteedilist sisutükki koos artiklititlite ja URL-idega, pääsedes alati ligi uusimale Microsofti dokumentatsioonile kohe, kui see avaldatakse.

**Esiisitatav näide**: Server pakub `microsoft_docs_search` tööriista, mis teostab semantilist otsingut Microsofti ametliku tehnilise dokumentatsiooni vastu. Kui see on seadistatud, võid küsida näiteks "Kuidas rakendada JWT autentimist ASP.NET Core’is?" ja saada üksikasjalikke ametlikke vastuseid koos allikavõimalustega. Otsingu kvaliteet on erakordne, sest see mõistab konteksti – Azure kontekstis päring terminile "containers" tagastab Azure Container Instances dokumentatsiooni, samas kui sama termin .NET kontekstis tagastab vastava C# kollektsiooniteabe.

See on eriti kasulik kiiresti muutuvate või hiljuti uuendatud raamistike ja kasutusjuhtumite puhul. Näiteks mõnedes minu hiljutistes arendusprojektides tahtsin ära kasutada Aspire ja Microsoft.Extensions.AI uusimate versioonide funktsioone. Microsoft Learn Docs MCP serveri lisamisega sain kasutada mitte ainult API dokumente, vaid ka vastavaid juhendeid ja läbivaateid, mis olid just avaldatud.

> **💡 Professionaali nipp**
> 
> Isegi tööriistasõbralikud mudelid vajavad julgustamist MCP tööriistu kasutama! Mõtle süsteemipõhise prompti või [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) lisamisele, mis ütleb: "Sul on ligipääs `microsoft.docs.mcp` – kasuta seda tööriista Microsofti uusima ametliku dokumentatsiooni otsimiseks küsimuste käsitlemisel Microsofti tehnoloogiate, nagu C#, Azure, ASP.NET Core või Entity Framework, kohta."
>
> Suurepärase näite selle kohta leiad [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) Awesome GitHub Copilot repositooriumist. See režiim kasutab spetsiaalselt Microsoft Learn Docs MCP serverit, et aidata puhastada ja uuendada C# koodi uusimate mustrite ja parimate tavade järgi.
### 2. ☁️ Azure MCP server


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mida see teeb**: Azure MCP Server on põhjalik komplekt enam kui 15 spetsialiseerunud Azure’i teenuse ühendajast, mis toob kogu Azure'i ökosüsteemi teie AI töövoogu. See ei ole lihtsalt üks server – see on võimas kogu, mis sisaldab ressursihaldust, andmebaasi ühenduvust (PostgreSQL, SQL Server), Azure Monitori logianalüüsi KQL-iga, Cosmos DB integreerimist ja palju muud.

**Miks see on kasulik**: Lisaks Azure ressursside haldamisele parandab see server koodi kvaliteeti oluliselt Azure SDK-dega töötades. Kui kasutate Azure MCP-d Agendi režiimis, ei aita see teil mitte ainult kirjutada koodi, vaid kirjutada *paremat* Azure koodi, mis järgib praeguseid autentimismustreid, parimaid vigade käsitlemise tavasid ning kasutab uusimaid SDK funktsioone. Selle asemel, et saada üldisi koode, mis võivad töötada, saate koodi, mis järgib Azure’i soovitatud mustreid tootmiskoormuste jaoks.

**Põhimoodulid hõlmavad**:
- **🗄️ Andmebaasi ühendajad**: Otse loomulikus keeles ligi pääsemine Azure Database for PostgreSQL ja SQL Server andmebaasidele
- **📊 Azure Monitor**: KQL-põhine logide analüüs ja tegevusinfot
- **🌐 Ressursside haldus**: Täielik Azure ressursi elutsükli haldus
- **🔐 Autentimine**: DefaultAzureCredential ja hallatava identiteedi mustrid
- **📦 Salvestusteenused**: Blob Storage, Queue Storage ja Table Storage operatsioonid
- **🚀 Konteineriteenused**: Azure Container Apps, Container Instances ja AKS haldus
- **Ja palju teisi spetsialiseerunud ühendajaid**

**Reaalne kasutus**: "Listeeri minu Azure salvestuskontod", "Küsitle minu Log Analytics tööruumi viimase tunni vigade kohta" või "Aita mul ehitada Azure rakendus Node.js-ga õige autentimisega"

**Täielik demo stsenaarium**: Siin on täielik juhend, mis näitab, kui võimas on ühendada Azure MCP GitHub Copilot for Azure laiendusega VS Code'is. Kui mõlemad on installitud ja esitate päringu:

> "Loo Python skript, mis üleslaadib faili Azure Blob Storage’i, kasutades DefaultAzureCredential autentimist. Skript peaks ühenduma minu Azure salvestuskontoga nimega 'mycompanystorage', üles laadima konteinerisse nimega 'documents', looma testfaili jooksva ajatempli põhjal üleslaadimiseks, käsitlema vigu sujuvalt ja pakkuma informatiivset väljundit, järgima Azure parimaid tavasid autentimisel ja vigade käsitlemisel, sisaldama kommentaare, mis seletavad, kuidas DefaultAzureCredential autentimine töötab, ning olema hästi struktureeritud sobivate funktsioonide ja dokumentatsiooniga."

Azure MCP Server genereerib täieliku, tootmiseks valmis Python skripti, mis:
- Kasutab uusimat Azure Blob Storage SDK-d koos õigete asünkroonsete mustritega
- Rakendab DefaultAzureCredential koos ulatusliku tagavarakeerme selgitusega
- Sisaldab tugevat vigade käsitlemist spetsiifiliste Azure eranditüüpidega
- Järgib Azure SDK parimaid tavasid ressursihalduse ja ühenduse käsitlemise osas
- Pakub detailset logimist ja informatiivset konsooliväljundit
- Loob korrektselt struktureeritud skripti funktsioonide, dokumentatsiooni ja tüübi vihjetega

See on tähelepanuväärne, sest ilma Azure MCP-ta võiksite saada üldist blob storage’i koodi, mis töötab, kuid ei järgi praeguseid Azure mustreid. Azure MCP-ga saate koodi, mis kasutab uusimaid autentimismeetodeid, haldab Azure-i spetsiifilisi vigade stsenaariume ning järgib Microsofti soovitatud tavasid tootmisrakendustele.

**Näide esiletõstmiseks**: Mulle on olnud raske meenutada täpseid käske `az` ja `azd` CLI-de jaoks ad-hoc kasutuseks. Tavaliselt on see minu jaoks kahe etapi protsess: esmalt otsin süntaksi üles, siis käivitan käsu. Sageli lähen lihtsalt portaalile ja klikin asja ära, sest ma ei taha tunnistada, et ma ei mäleta CLI süntaksit. Võimalus lihtsalt kirjeldada, mida ma tahan, on imeline ja veel parem, et seda teha saab ilma IDE-st lahkumata!

Azure MCP repositooriumis on suurepärane nimekiri kasutusjuhtudest, mis aitavad teil alustada: [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server). Põhjalike seadistusjuhendite ja täpsemate konfiguratsioonivõimaluste jaoks vaadake ametlikku [Azure MCP dokumentatsiooni](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mida see teeb**: Ametlik GitHub MCP Server pakub sujuvat integratsiooni kogu GitHub ökosüsteemiga, pakkudes nii hostitud kaugjuurdepääsu kui ka lokaalse Docker’i kasutuse valikuid. See ei ole pelgalt baastaseme repositooriumi operatsioonid – see on laiaulatuslik tööriistakast, mis sisaldab GitHub Actionite haldust, pull request töövooge, probleemide jälgimist, turvaskaneerimist, teavitusi ja arenenud automatiseerimisvõimalusi.

**Miks see on kasulik**: See server muudab teie suhtlemist GitHubiga, tuues täispaketi platvormikogemuse otse teie arenduskeskkonda. Selle asemel, et pidevalt vahetada VS Code ja GitHub.com-i vahel projekti halduse, koodikontrolli ja CI/CD jälgimise jaoks, saate kõike hallata loomulikus keeles käskudes, jäädes samal ajal koodi juurde.

> **ℹ️ Märkus: erinevat tüüpi 'agendid'**
> 
> Ärge segadusse ajage seda GitHub MCP Serverit GitHubi Coding Agendiga (tehisintellekti agent, kellele saate määrata probleeme automatiseeritud kooditööde jaoks). GitHub MCP Server töötab VS Code’i Agendi režiimis, pakkudes GitHub API integratsiooni, samas kui GitHubi Coding Agent on eraldi funktsioon, mis loob pull requeste määratud GitHubi probleemide jaoks.

**Põhifunktsioonid hõlmavad**:
- **⚙️ GitHub Actions**: Täielik CI/CD torujuhtme haldus, töövoogude jälgimine ja artefaktide käsitsemine
- **🔀 Pull requestid**: PR-ide loomine, ülevaatamine, ühendamine ja haldamine koos põhjaliku oleku jälgimisega
- **🐛 Probleemid**: Täielik probleemide elutsükli haldus, kommenteerimine, sildistamine ja määramine
- **🔒 Turvalisus**: Koodi skaneerimise hoiatused, saladuste tuvastamine ja Dependaboti integratsioon
- **🔔 Teavitused**: Nutikas teavituste haldus ja repositooriumi tellimuste kontroll
- **📁 Repositooriumi haldus**: Failioperatsioonid, harude haldus ja repositooriumi administraatorihaldus
- **👥 Koostöö**: Kasutaja- ja organisatsioonide otsing, tiimihaldus ja juurdepääsukontroll

**Reaalne kasutus**: "Loo pull request minu feature harust", "Näita mulle kõiki sel nädalal ebaõnnestunud CI jooksusid", "Listi minu repositooriumide avatud turvahoidete hoiatused" või "Leia kõik mulle määratud probleemid minu organisatsioonidest"

**Täielik demo stsenaarium**: Siin on võimas töövoog, mis demonstreerib GitHub MCP Serveri võimeid:

> "Ma pean valmistuma meie sprindi ülevaateks. Näita mulle kõiki sel nädalal loodud pull requeste, kontrolli meie CI/CD torujuhtmete staatust, koosta kokkuvõte turvahoiatustest, mida peame lahendama, ja aita mul koostada väljaandemärkmeid ühendatud PR-ide põhjal, millel on sildi 'feature'."

GitHub MCP Server teeb järgmist:
- Pärib teie hiljutised pull requestid koos detailse olekuinfoga
- Analüüsib töövoogude jooksusid ja tõstab esile võimalikud ebaõnnestumised või jõudlusprobleemid
- Koondab turvakontrolli tulemused ja seab prioriteediks kriitilised hoiatused
- Genereerib põhjalikud väljaandemärkmed ühendatud PR-idest eraldatud info põhjal
- Pakub praktilisi järgmisi samme sprindi planeerimiseks ja väljaande ettevalmistamiseks

**Näide esiletõstmiseks**: Mulle meeldib seda kasutada koodi ülevaatuse töövoogudes. Selle asemel, et hüpata VS Code’i, GitHubi teavituste ja PR lehtede vahel, ütlen lihtsalt "Näita mulle kõiki minu ülevaatust ootavaid PR-e" ja siis "Lisa kommentaar PR #123-le, küsides autentimismeetodi vigade käsitlemise kohta." Server haldab GitHub API kõnesid, hoiab arutelu konteksti ja aitab mul isegi kirjutada konstruktiivsemaid ülevaatuse kommentaare.

**Autentimisvalikud**: Server toetab nii OAuth-i (sujuv VS Code-is) kui ka isikupärastatud juurdepääsutokeneid, konfigureeritava tööriistakomplektiga, mis võimaldab lubada vaid vajaliku GitHub funktsionaalsuse. Seda saab kasutada nii kaughostitud teenusena kiireks seadistuseks kui ka lokaalselt Dockeriga täielikuks kontrolliks.

> **💡 Pro näpunäide**
> 
> Luba ainult need tööriistakomplektid, mida vajad, seadistades MCP serveri sätetes `--toolsets` parameetri, et vähendada konteksti suurust ja parandada AI tööriistade valikut. Näiteks lisa `"--toolsets", "repos,issues,pull_requests,actions"` oma MCP konfiguratsiooni argumentidesse põhiarenduse töövoogude jaoks või kasuta `"--toolsets", "notifications, security"`, kui soovid peamiselt GitHubi jälgimismehhanisme.
### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mida see teeb**: Ühendub Azure DevOps teenustega, pakkudes põhjalikku projektihaldust, töökohate jälgimist, ehitustorude haldust ja repositooriumi operatsioone.

**Miks see on kasulik**: Tiimidele, kes kasutavad Azure DevOps’i oma peamise DevOps platvormina, elimineerib see MCP server pideva vahelehtede vahetamise teie arenduskeskkonna ja Azure DevOps veebiliidese vahel. Saate hallata töökohte, kontrollida ehitusetappe, pärida repositooriume ja käsitleda projektihalduse ülesandeid otse oma AI assistendi kaudu.

**Reaalne kasutus**: "Näita mulle kõiki aktiivseid töökohte praeguses sprindis WebApp projekti jaoks", "Loo veateade äsja leitud sisselogimisprobleemi kohta" või "Kontrolli meie ehitustorude staatust ja näita mulle viimaseid ebaõnnestumisi"

**Näide esiletõstmiseks**: Saate lihtsalt kontrollida oma meeskonna praeguse sprindi staatust lihtsa päringuga nagu "Näita mulle kõiki aktiivseid töökohte praeguses sprindis WebApp projekti jaoks" või "Loo veateade äsja leitud sisselogimisprobleemi kohta" ilma oma arenduskeskkonnast lahkumata.

### 5. 📝 MarkItDown MCP Server


[![Installi VS Codesse](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Installi VS Code Insidersi](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mida see teeb**: MarkItDown on laiahaardeline dokumendi teisendamise server, mis muudab mitmesugused failivormingud kõrgekvaliteediliseks Markdowniks, optimeeritud LLM-i tarbimiseks ja tekstianalüüsi töövoogudeks.

**Miks see kasulik on**: Hädavajalik kaasaegsetes dokumentatsiooni töövoogudes! MarkItDown toetab muljetavaldavat hulka failivorminguid, säilitades samas olulise dokumendi struktuuri nagu pealkirjad, loendid, tabelid ja lingid. Erinevalt lihtsatest teksti väljavõtmise tööriistadest keskendub see semantilise tähenduse ja vorminduse säilitamisele, mis on väärtuslik nii tehisintellekti töötlemiseks kui ka inimloetavuseks.

**Toetatud failivormingud**:
- **Office'i dokumendid**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Meediafailid**: Pildid (koos EXIF-i metainformatsiooni ja OCR-iga), heli (koos EXIF-i metainformatsiooni ja kõnetõlkega)
- **Veebisisu**: HTML, RSS-vood, YouTube URL-id, Wikipedia leheküljed
- **Andmevormingud**: CSV, JSON, XML, ZIP-failid (sisud töötleb rekursiivselt)
- **Väljaandmisvormingud**: EPub, Jupyter märkmikud (.ipynb)
- **E-post**: Outlook sõnumid (.msg)
- **Täpsemad**: Azure Document Intelligence integratsioon täiustatud PDF töötlemiseks

**Täpsemad võimed**: MarkItDown toetab LLM-põhiseid pildikirjeldusi (kui on olemas OpenAI klient), Azure Document Intelligence'i täiustatud PDF töötlemist, heli transkriptsiooni kõnesisu jaoks ja pistikprogrammi süsteemi täiendavate failivormingute laiendamiseks.

**Tegelik kasutus**: "Teisenda see PowerPoint esitlus Markdown-iks meie dokumentatsiooni saidi jaoks", "Võta sellest PDF-ist tekst välja õigete pealkirjastega" või "Muuda see Exceli arvutustabel loetavaks tabeliformaadiks"

**Esiletõstetud näide**: Tsiteerides [MarkItDown dokumentatsiooni](https://github.com/microsoft/markitdown#why-markdown):

> Markdown on äärmiselt lähedane tavalisele tekstile, kasutades minimaalset märgistuskeelt või vormindust, kuid annab siiski võimaluse esindada olulist dokumendi struktuuri. Peamised LLM-id, nagu OpenAI GPT-4o, "räägivad" loomulikult Markdownit ja kasutavad tihti Markdownit oma vastustes ilma seda eraldi palumata. See viitab sellele, et neid on treenitud tohutul hulgal Markdown-vormingus tekstil ja nad mõistavad seda hästi. Lisaboonusena on Markdowni konventsioonid ka väga tokenitõhusad.

MarkItDown on väga hea dokumendi struktuuri säilitamisel, mis on oluline AI töövoogude jaoks. Näiteks PowerPoint esitluse teisendamisel hoiab see slaidide korralduse õige pealkirjastusega, ekstraheerib tabelid Markdown tabelitena, lisab piltidele alternatiivteksti ja töötleb isegi esinejanootid. Diagrammid teisendatakse loetavateks andmetabeliteks ja tulev Markdown säilitab esitluse loogilise voolu. See teeb selle ideaalseks AI süsteemidesse esitlusmaterjali sisestamiseks või olemasolevate slaidide põhjal dokumentatsiooni loomiseks.
### 6. 🗃️ SQL Server MCP Server

[![Installi VS Codesse](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Installi VS Code Insidersi](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mida see teeb**: Pakub vestluslikku juurdepääsu SQL Serveri andmebaasidele (kohaliku, Azure SQL või Fabricu peal)

**Miks see kasulik on**: Sarnaselt PostgreSQL serverile, aga Microsoft SQL ökosüsteemi jaoks. Ühendu lihtsa ühendusstringiga ja alusta päringute tegemist loodusliku keelega – pole enam vaja konteksti vahetada!

**Tegelik kasutus**: "Leia kõik tellimused, mis viimase 30 päeva jooksul täidetud pole" tõlgitakse sobivateks SQL-päringuteks ja tagastab vormindatud tulemused

**Esiletõstetud näide**: Kui oled oma andmebaasiühenduse loonud, saad kohe hakata oma andmetega vestlema. Blogipostitus demonstreerib seda lihtsa küsimusega: "millise andmebaasiga oled ühendatud?" MCP server vastab, kutsudes õiget andmebaasitööriista, ühendub SQL Serveri instantsiga ja tagastab andmed sinu praeguse andmebaasiühenduse kohta – ilma ühtki SQL rida kirjutamata. Server toetab põhjalikke andmebaasioperatsioone skeemi haldamisest kuni andmete töötlemiseni, kõik läbi loomulike keelekäskude. Täieliku seadistuse ja konfiguratsiooni juhiste ning näidete jaoks VS Code’i ja Claude Desktopiga vaata: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP Server

[![Installi VS Codesse](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Installi VS Code Insidersi](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mida see teeb**: Võimaldab AI agentidel veebilehtedega suhelda testimise ja automatiseerimise jaoks

> **ℹ️ Toidab GitHub Copiloti**
> 
> Playwright MCP Server toetab GitHub Copiloti koodiagenti, andes sellele veebisirvimise võimekuse! [Loe selle funktsiooni kohta lähemalt](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miks see kasulik on**: Täiuslik automatiseeritud testimiseks, mida juhivad loodusliku keele kirjeldused. AI saab navigeerida veebilehtedel, täita vorme ja väljavõtta andmeid struktureeritud ligipääsetavuse hetktõmmiste kaudu – see on uskumatult võimas!

**Tegelik kasutus**: "Testi sisselogimisvoog ja kontrolli, et juhtpaneel laeb korrektselt" või "Loo test, mis otsib tooteid ja kontrollib tulemuste lehte" – kõik ilma, et oleks vaja rakenduse lähtekoodi

**Esiletõstetud näide**: Minu meeskonnakaaslane Debbie O'Brien on viimasel ajal teinud Playwright MCP Serveriga imelisi töid! Näiteks näitas ta hiljuti, kuidas saab luua täielikke Playwrighi teste ilma rakenduse lähtekoodi ligipääsuta. Oma stsenaariumis palus ta Copilotil luua test filmide otsingu rakenduse jaoks: mine saidile, otsi "Garfieldit" ja kontrolli, et film kuvatakse tulemustes. MCP alustas brauseri seanssi, uuris lehe struktuuri DOM hetktõmmiste abil, leidis õiged selektorid ja genereeris täielikult toimiva TypeScripti testi, mis läbipääses kohe esimesel katsel.

Selle tõeliselt võimsaks teeb see, et ta sillutab lõhe loodusliku keele juhiste ja täidetava testikoodi vahel. Traditsioonilised lähenemised nõuavad kas käsitsi testikirjutust või ligipääsu koodibaasile konteksti saamiseks. Aga Playwright MCP abil saad testida väliseid saite, kliendirakendusi või töötada musta kasti testimise stsenaariumites, kus koodile ligipääsu pole.


### 8. 💻 Dev Box MCP Server

[![Installi VS Codesse](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Installi VS Code Insidersi](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mida see teeb**: Halda Microsoft Dev Box keskkondi loomulike keelekäskude kaudu

**Miks see kasulik on**: Lihtsustab arenduskeskkonna haldamist tohutult! Loo, konfigureeri ja halda arenduskeskkondi ilma konkreetseid käske meeles pidamata.

**Tegelik kasutus**: "Loo uus Dev Box uusima .NET SDK-ga ja configureeri see meie projekti jaoks", "Kontrolli kõigi minu arenduskeskkondade olekut" või "Loo standardiseeritud demo keskkond meie meeskonna esitlusteks"

**Esiletõstetud näide**: Olen suur Dev Boxi kasutaja isiklikuks arenduseks. Minu valgustav hetk oli siis, kui James Montemagno selgitas, kui hea on Dev Box konverentside demonstreerimiseks, kuna sellel on superkiire ethernet ühendus sõltumata konverentsi/ hotelli/ lennuki wifi olukorrast. Tegelikult harjutasin hiljuti konverentsi demo tegemist, olles oma sülearvuti telefoni hotspotiga ühenduses bussis Brugge'st Antwerpeni! Minu järgmine samm on sukelduda rohkem meeskondade haldamisse, kes haldavad mitut arenduskeskkonda ja standardiseeritud demosid. Ja teine suur kasutusjuhtum, mida olen klientidelt ja kolleegidelt kuulnud, on loomult eelkonfigureeritud arenduskeskkonnad. Mõlemas olukorras võimaldab MCP Dev Boxide konfigureerimise ja haldamise loomuliku keele kasutamist, samal ajal kui oled oma arenduskeskkonnas.

### 9. 🤖 Microsoft Foundry MCP Server


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Mida see teeb**: Microsoft Foundry MCP Server annab arendajatele põhjaliku juurdepääsu Azure'i tehisintellekti ökosüsteemile, kaasa arvatud mudelikaustad, juurutuse haldus, teadmiste indekseerimine Azure AI Searchiga ja hindamisvahendid. See eksperimentaalne server ühendab tehisintellekti arenduse ja Azure'i võimsa AI infrastruktuuri, muutes AI rakenduste loomiseks, juurutamiseks ja hindamiseks protsessi lihtsamaks.

**Miks see on kasulik**: See server muudab teie tööviisi Azure AI teenustega, tuues ettevõtte tasemel AI võimekused otse teie arendustöövoogu. Selle asemel, et vahetada Azure portaali, dokumentatsiooni ja oma IDE vahel, saate leida mudeleid, juurutada teenuseid, hallata teadmiste baase ja hinnata tehisintellekti jõudlust loomulikus keeles antud käskude kaudu. See on eriti võimas arendajatele, kes loovad RAG (Retrieval-Augmented Generation) rakendusi, haldavad mitut mudelit korraga või rakendavad terviklikke AI hindamispipeläine.

**Põhivõimalused arendajatele**:
- **🔍 Mudelite avastamine ja juurutamine**: Sirvi Microsoft Foundry mudelikausta, saa põhjalikku teavet mudelite kohta koos koodinäidistega ja juuruta mudeleid Azure AI Teenustesse
- **📚 Teadmiste haldus**: Loo ja halda Azure AI Search indekseid, lisa dokumente, seadista indeksereid ja ehita keerukaid RAG süsteeme
- **⚡ AI agendi integreerimine**: Ühenda Azure AI agentidega, päringu olemasolevatele agentidele ja hinda agentide jõudlust tootmiskeskkonnas
- **📊 Hinnangu raamistiku**: Käivita põhjalikke tekstipõhiseid ja agentide hindamisi, genereeri markdown-aruandeid ja järgi kvaliteedi tagamise protsesse AI rakenduste jaoks
- **🚀 Prototüüpimise tööriistad**: Saa paigaldusjuhised GitHub-põhistele prototüüpimisele ja pääse ligi Microsoft Foundry Labsile tipptasemel uurimismudelite jaoks

**Realistlik kasutusnäide arendajatele**: „Juurutan Phi-4 mudeli Azure AI Teenustesse oma rakenduse jaoks“, „Loon uue otsinguindeksi oma dokumentatsioonipõhise RAG süsteemi jaoks“, „Hindan oma agendi vastuseid kvaliteedimõõdikute alusel“ või „Leian parima arutlemismudeli keerukate analüüsitööde jaoks“

**Täielik demokava**: Siin on võimas AI arendustöövoog:

> „Ma ehitan klienditoe agenti. Aita mul leida hea arutlemismudel kataloogist, juuruta see Azure AI Teenustesse, loo teadmiste baas meie dokumentatsioonist, seadista hindamisraamistiku, et testida vastuste kvaliteeti ja seejärel aita mul prototüüpida integreerimist GitHubi tokeniga testimiseks.“

Microsoft Foundry MCP Server:
- Uurib mudelikausta, et soovitada optimaalseid arutlemismudeleid vastavalt teie nõudmistele
- Pakub juurutuskäske ja kvota teavet teie eelistatud Azure'i piirkonna jaoks
- Seadistab Azure AI Search indekseid sobiva skeemiga teie dokumentatsiooni jaoks
- Konfigureerib hindamispipeläinad kvaliteedimõõdikute ja ohutuskontrollidega
- Genereerib prototüüpimiskoodi GitHubi autentimisega kohese testimise jaoks
- Pakub põhjalikke seadistusjuhiseid, mis on kohandatud teie tehnoloogiapinu jaoks

**Esiletõstetud näide**: Arendajana on mul olnud raske kursis püsida erinevate LLM mudelitega. Ma tean mõnda põhilist mudelit, kuid tunnen, et jään ilma mõnest tootlikkuse ja efektiivsuse võidust. Märksõnad ja kvotad on stressirohked ja keerulised hallata – ma ei tea kunagi, kas valin õige mudeli õigeks ülesandeks või kulutan oma eelarvet ebaefektiivselt. Kuulsin just James Montemagnolt sellest MCP Serverist, kui uurisin meeskonnavendade käest MCP Serveri soovitusi selle postituse jaoks, ja olen elevil, et saan seda proovida! Mudelite avastamise võimalused tunduvad eriti muljetavaldavad inimeste jaoks nagu mina, kes tahavad uurida tavapärasest kaugemale ja leida ülesandele optimeeritud mudeleid. Hindamisraamistik peaks aitama mul kinnitada, et saan tõepoolest paremaid tulemusi, mitte ei proovi midagi uut lihtsalt niisama.

> **ℹ️ Eksperimentaalne staatus**
> 
> See MCP server on eksperimentaalne ja aktiivse arenduse all. Funktsioonid ja API-d võivad muutuda. Sobib ideaalselt Azure AI võimekuste uurimiseks ja prototüüpide ehitamiseks, kuid tootmiskasutuseks kontrollige stabiilsuse nõudeid.
### 10. 🏢 Microsoft 365 agentide tööriistakomplekti MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Mida see teeb**: Pakub arendajatele olulisi tööriistu AI agentide ja rakenduste loomisel, mis integreeruvad Microsoft 365 ja Microsoft 365 Copilotiga, sealhulgas skeemi valideerimine, koodinäidiste leidmine ja tõrkeotsingu abi.

**Miks see on kasulik**: Microsoft 365 ja Copiloti jaoks arendamine hõlmab keerukaid manusa skeeme ja spetsiifilisi arendusmustreid. See MCP server toob olulised arendusressursid otse teie koodikeskkonda, aidates skeeme valideerida, leida koodinäiteid ning lahendada tavapäraseid probleeme ilma pidevalt dokumentatsiooni lugemata.

**Reaalne kasutus**: „Valideeri minu deklaratiivne agendi manifest ja paranda skeemivead“, „Näita mulle koodinäidet Microsoft Graph API plugina rakendamiseks“ või „Aita mul lahendada minu Teamsi rakenduse autentimisprobleeme“

**Esiletõstetud näide**: Võtsin ühendust sõbra John Milleriga pärast Buildil M365 agentidest vestlemist, ja ta soovitas seda MCP-d. See võiks olla suurepärane M365 agentidega alustavatele arendajatele, kuna see pakub malle, näidiskoodi ja raamistikku alustamiseks ilma dokumentatsioonis ära uppumata. Skeemi valideerimise funktsioonid tunduvad eriti kasulikud, et vältida manifesti struktuurivigu, mis võivad põhjustada tunde aega nõudvat silumist.

> **💡 Nipp**
> 
> Kasuta seda serverit koos Microsoft Learn Docs MCP Serveriga terviklikuks M365 arendusabiks – üks pakub ametlikku dokumentatsiooni, teine praktikapõhiseid arendustööriistu ja tõrkeotsingu abi.


## Mis edasi? 🔮

## 📋 Kokkuvõte

Mudeli konteksti protokoll (MCP) muudab seda, kuidas arendajad suhtlevad AI assistentide ja väliste tööriistadega. Need 10 Microsofti MCP serverit näitavad standardiseeritud AI integratsiooni võimsust, võimaldades sujuvaid töövooge, mis hoiavad arendajad fookuses ning annavad juurdepääsu võimsatele välistele võimalustele.

Alates põhjalikust Azure'i ökosüsteemi integratsioonist kuni spetsialiseeritud tööriistadeni nagu Playwright veebibrauseri automatiseerimiseks ja MarkItDown dokumentide töötlemiseks, need serverid demonstreerivad, kuidas MCP suurendab tootlikkust erinevates arenduskeskkondades. Standardiseeritud protokoll tagab nende tööriistade sujuva koostöö, luues ühtse arenduskogemuse.

Kuna MCP ökosüsteem jätkab arengut, on oluline hoida sidet kogukonnaga, uurida uusi servereid ja luua kohandatud lahendusi, et maksimeerida oma arendustootlikkust. MCP avatud standard võimaldab kombineerida eri tarnijate tööriistu, et luua täiuslik töövoog just teie spetsiifiliste vajaduste jaoks.

## 🔗 Lisamaterjalid

- [Ametlik Microsoft MCP hoidla](https://github.com/microsoft/mcp)
- [MCP kogukond ja dokumentatsioon](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentatsioon](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentatsioon](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentatsioon](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Õpime koos – MCP üritused](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Äärmiselt head GitHub Copiloti kohandused](https://github.com/awesome-copilot)
- [C# MCP arenduskomplekt (SDK)](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days otseülekanne 29. ja 30. juulil või järelvaade](https://aka.ms/mcpdevdays)

## 🎯 Harjutused

1. **Paigalda ja seadista**: Sea üles üks MCP serveritest oma VS Code keskkonnas ja testi põhifunktsioone.
2. **Töövoo integratsioon**: Kujunda arendustöövoog, mis ühendab vähemalt kolm erinevat MCP serverit.
3. **Kohandatud serveri planeerimine**: Leia igapäevases arendustöös ülesanne, mis võiks kasu saada kohandatud MCP serverist, ja loo selle jaoks spetsifikatsioon.
4. **Tulemuste analüüs**: Võrdle MCP serverite kasutamise efektiivsust traditsiooniliste meetoditega tavapäraste arendustööde puhul.
5. **Turvalisuse hindamine**: Hinda MCP serverite turvariske oma arenduskeskkonnas ja paku parimaid tavasid.


Next:[Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->