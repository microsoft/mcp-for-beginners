# 🚀 10 Microsoft MCP serverit, mis muudavad arendajate produktiivsust

## 🎯 Mida õpid sellest juhendist

See praktiline juhend tutvustab kümmet Microsoft MCP serverit, mis aktiivselt muudavad arendajate tööd AI-assistentidega. Selle asemel, et lihtsalt selgitada, mida MCP serverid *võivad* teha, näitame servereid, mis juba igapäevases arendustöös Microsoftis ja mujal reaalselt mõju avaldavad.

Iga server selles juhendis on valitud reaalse kasutuse ja arendajate tagasiside põhjal. Sa saad teada mitte ainult, mida iga server teeb, vaid ka miks see oluline on ja kuidas sellest oma projektides maksimumi võtta. Olgu sa MCP-ga täiesti algaja või otsid võimalusi oma olemasoleva seadistuse laiendamiseks, need serverid esindavad Microsofti ökosüsteemi kõige praktilisemaid ja mõjusamaid tööriistu.

> **💡 Kiire alustamise näpunäide**
> 
> Uus MCP-s? Pole probleemi! See juhend on loodud algajasõbralikuks. Selgitame kontseptsioone järk-järgult ja vajadusel saad alati tagasi pöörduda meie [MCP sissejuhatuse](../00-Introduction/README.md) ja [Põhikontseptsioonide](../01-CoreConcepts/README.md) moodulite juurde, et saada sügavam taust.

## Ülevaade

See põhjalik juhend uurib kümmet Microsoft MCP serverit, mis revolutsioneerivad arendajate suhtlust AI-assistentide ja väliste tööriistadega. Alates Azure'i ressursside haldamisest kuni dokumentide töötlemiseni näitavad need serverid Model Context Protocoli võimsust sujuvate ja produktiivsete arendustöövoogude loomisel.

## Õpieesmärgid

Selle juhendi lõpuks:
- Mõistad, kuidas MCP serverid suurendavad arendajate produktiivsust
- Õpid tundma Microsofti kõige mõjusamaid MCP serveri rakendusi
- Avastad praktilisi kasutusviise iga serveri jaoks
- Tead, kuidas neid servereid seadistada ja konfigureerida VS Code'is ja Visual Studios
- Uurid MCP ökosüsteemi laiemat pilti ja tulevikusuundi

## 🔧 MCP serverite mõistmine: algaja juhend

### Mis on MCP serverid?

Kui oled Model Context Protocoli (MCP) algaja, võid küsida: "Mis täpselt on MCP server ja miks peaks see mind huvitama?" Alustame lihtsa analoogiaga.

Mõtle MCP serveritele kui spetsialiseeritud assistentidele, mis aitavad sinu AI-koodikaaslasel (näiteks GitHub Copilot) ühenduda väliste tööriistade ja teenustega. Nii nagu kasutad oma telefonis erinevaid rakendusi erinevate ülesannete jaoks – üks ilma jaoks, teine navigeerimiseks, kolmas panganduseks – annavad MCP serverid sinu AI-assistendile võime suhelda erinevate arendustööriistade ja teenustega.

### Probleem, mida MCP serverid lahendavad

Enne MCP serverite kasutuselevõttu, kui tahtsid:
- Kontrollida oma Azure'i ressursse
- Luua GitHubi probleemi
- Pärida oma andmebaasi
- Otsida dokumentatsioonist

Pidid koodi kirjutamise katkestama, avama brauseri, navigeerima vastavale veebisaidile ja need ülesanded käsitsi täitma. See pidev konteksti vahetamine katkestab sinu töövoo ja vähendab produktiivsust.

### Kuidas MCP serverid muudavad sinu arenduskogemust

MCP serveritega saad jääda oma arenduskeskkonda (VS Code, Visual Studio jne) ja lihtsalt paluda oma AI-assistendil need ülesanded täita. Näiteks:

**Traditsiooniline töövoog:**
1. Katkesta koodi kirjutamine
2. Ava brauser
3. Navigeeri Azure'i portaali
4. Otsi salvestuskonto üksikasju
5. Naase VS Code'i
6. Jätka koodi kirjutamist

**Uus töövoog MCP serveritega:**
1. Küsi AI-lt: "Mis on minu Azure'i salvestuskontode staatus?"
2. Jätka koodi kirjutamist saadud teabe põhjal

### Peamised eelised algajatele

#### 1. 🔄 **Jää oma töövoogu**
- Ei mingit vahetamist mitme rakenduse vahel
- Keskendu koodile, mida kirjutad
- Vähenda vaimset koormust erinevate tööriistade haldamisel

#### 2. 🤖 **Kasuta loomulikku keelt keeruliste käskude asemel**
- SQL-i süntaksi meeldejätmise asemel kirjelda, millist andmeid vajad
- Azure CLI käskude meeldejätmise asemel selgita, mida tahad saavutada
- Lase AI-l tegeleda tehniliste detailidega, samal ajal kui sina keskendud loogikale

#### 3. 🔗 **Ühenda mitu tööriista**
- Loo võimsad töövood, kombineerides erinevaid teenuseid
- Näide: "Hangi kõik hiljutised GitHubi probleemid ja loo vastavad Azure DevOpsi tööüksused"
- Automatiseeri ilma keerulisi skripte kirjutamata

#### 4. 🌐 **Ligipääs kasvavale ökosüsteemile**
- Kasuta servereid, mille on loonud Microsoft, GitHub ja teised ettevõtted
- Kombineeri erinevate tarnijate tööriistu sujuvalt
- Liitu standardiseeritud ökosüsteemiga, mis töötab erinevate AI-assistentidega

#### 5. 🛠️ **Õpi praktilise kogemuse kaudu**
- Alusta eelkonfigureeritud serveritega, et mõista kontseptsioone
- Loo järk-järgult oma servereid, kui muutud mugavamaks
- Kasuta olemasolevaid SDK-sid ja dokumentatsiooni, et suunata oma õppimist

### Reaalne näide algajatele

Oletame, et oled veebiarenduses uus ja töötad oma esimese projekti kallal. Siin on, kuidas MCP serverid aitavad:

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


### Ettevõtte standardi eelis

MCP muutub tööstusharu standardiks, mis tähendab:
- **Järjepidevus**: Sarnane kogemus erinevate tööriistade ja ettevõtete vahel
- **Ühilduvus**: Erinevate tarnijate serverid töötavad koos
- **Tulevikukindlus**: Oskused ja seadistused kanduvad üle erinevate AI-assistentide vahel
- **Kogukond**: Suur ökosüsteem jagatud teadmiste ja ressurssidega

### Alustamine: Mida õpid

Selles juhendis uurime 10 Microsoft MCP serverit, mis on eriti kasulikud arendajatele igal tasemel. Iga server on loodud:
- Lahendama levinud arendusprobleeme
- Vähendama korduvaid ülesandeid
- Parandama koodi kvaliteeti
- Suurendama õppimisvõimalusi

> **💡 Õppimisnõuanne**
> 
> Kui oled MCP-ga täiesti algaja, alusta meie [MCP sissejuhatuse](../00-Introduction/README.md) ja [Põhikontseptsioonide](../01-CoreConcepts/README.md) moodulitega. Seejärel naase siia, et näha neid kontseptsioone tegevuses Microsofti tööriistadega.
>
> MCP olulisuse kohta lisakonteksti saamiseks vaata Maria Naggaga postitust: [Ühenda üks kord, integreeri kõikjal MCP-ga](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## MCP seadistamine VS Code'is ja Visual Studios 🚀

Nende MCP serverite seadistamine on lihtne, kui kasutad Visual Studio Code'i või Visual Studio 2022 koos GitHub Copilotiga.

### VS Code'i seadistamine

Siin on põhiprotsess VS Code'i jaoks:

1. **Luba Agent Mode**: VS Code'is lülitu Copilot Chat aknas Agent Mode'ile
2. **Konfigureeri MCP serverid**: Lisa serveri konfiguratsioonid oma VS Code'i settings.json faili
3. **Käivita serverid**: Klõpsa "Start" nuppu iga serveri jaoks, mida soovid kasutada
4. **Vali tööriistad**: Vali, millised MCP serverid lubada oma praeguses sessioonis

Üksikasjalike seadistusjuhiste jaoks vaata [VS Code MCP dokumentatsiooni](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Pro näpunäide: Halda MCP servereid nagu proff!**
> 
> VS Code'i laienduste vaates on nüüd [kasulik uus kasutajaliides MCP serverite haldamiseks](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Sul on kiire juurdepääs serverite käivitamiseks, peatamiseks ja haldamiseks selge ja lihtsa liidese kaudu. Proovi järele!

### Visual Studio 2022 seadistamine

Visual Studio 2022 jaoks (versioon 17.14 või uuem):

1. **Luba Agent Mode**: Klõpsa GitHub Copilot Chat aknas "Ask" rippmenüüd ja vali "Agent"
2. **Loo konfiguratsioonifail**: Loo `.mcp.json` fail oma lahenduse kataloogi (soovitatav asukoht: `<SOLUTIONDIR>\.mcp.json`)
3. **Konfigureeri serverid**: Lisa oma MCP serveri konfiguratsioonid, kasutades standardset MCP formaati
4. **Tööriistade kinnitamine**: Kui küsitakse, kinnita tööriistad, mida soovid kasutada, sobivate õigustega

Üksikasjalike Visual Studio seadistusjuhiste jaoks vaata [Visual Studio MCP dokumentatsiooni](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Igal MCP serveril on oma konfiguratsiooninõuded (ühendusstringid, autentimine jne), kuid seadistusmuster on mõlemas IDE-s järjepidev.

## Õppetunnid Microsoft MCP serveritest 🛠️

### 1. 📚 Microsoft Learn Docs MCP server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mida see teeb**: Microsoft Learn Docs MCP server on pilvepõhine teenus, mis pakub AI-assistentidele reaalajas juurdepääsu ametlikule Microsofti dokumentatsioonile Model Context Protocoli kaudu. See ühendub `https://learn.microsoft.com/api/mcp` ja võimaldab semantilist otsingut Microsoft Learn, Azure'i dokumentatsiooni, Microsoft 365 dokumentatsiooni ja teiste ametlike Microsofti allikate vahel.

**Miks see on kasulik**: Kuigi see võib tunduda "lihtsalt dokumentatsioonina", on see server tegelikult ülioluline iga arendaja jaoks, kes kasutab Microsofti tehnoloogiaid. Üks suurimaid kaebusi .NET arendajatelt AI-koodikaaslaste kohta on see, et need ei ole kursis uusimate .NET ja C# versioonidega. Microsoft Learn Docs MCP server lahendab selle, pakkudes reaalajas juurdepääsu kõige värskematele dokumentatsioonidele, API viidetele ja parimatele praktikatele. Olgu tegemist uusimate Azure SDK-dega, C# 13 funktsioonide uurimisega või tipptasemel .NET Aspire mustrite rakendamisega – see server tagab, et sinu AI-assistentil on juurdepääs autoriteetsele ja ajakohasele teabele, mida on vaja täpse ja kaasaegse koodi genereerimiseks.

**Reaalne kasutus**: "Millised on az cli käsud Azure'i konteinerirakenduse loomiseks vastavalt ametlikule Microsoft Learn dokumentatsioonile?" või "Kuidas konfigureerida Entity Frameworki sõltuvussüstega ASP.NET Core'is?" Või näiteks "Vaata üle see kood, et veenduda, et see vastab Microsoft Learn dokumentatsiooni jõudlussoovitustele." Server pakub põhjalikku katvust Microsoft Learn, Azure'i dokumentatsiooni ja Microsoft 365 dokumentatsiooni vahel, kasutades täiustatud semantilist otsingut, et leida kõige kontekstuaalselt asjakohasem teave. See tagastab kuni 10 kvaliteetset sisutükki koos artiklite pealkirjade ja URL-idega, alati juurdepääsuga kõige värskematele Microsofti dokumentatsioonidele nende avaldamise ajal.

**Esiletõstetud näide**: Server pakub `microsoft_docs_search` tööriista, mis teostab semantilist otsingut Microsofti ametliku tehnilise dokumentatsiooni vastu. Kui see on konfigureeritud, saad esitada küsimusi nagu "Kuidas rakendada JWT autentimist ASP.NET Core'is?" ja saada üksikasjalikke, ametlikke vastuseid koos allikaviidetega. Otsingu kvaliteet on erakordne, kuna see mõistab konteksti – Azure'i kontekstis "konteinerite" kohta küsimine tagastab Azure Container Instances dokumentatsiooni, samas kui sama termin .NET kontekstis tagastab asjakohase C# kogude teabe.

See on eriti kasulik kiiresti muutuvate või hiljuti uuendatud teekide ja kasutusjuhtude puhul. Näiteks mõnes hiljutises koodiprojektis tahtsin kasutada uusimate .NET Aspire ja Microsoft.Extensions.AI versioonide funktsioone. Microsoft Learn Docs MCP serveri kaasamisega sain kasutada mitte ainult API dokumente, vaid ka just avaldatud juhendeid ja juhiseid.

> **💡 Pro näpunäide**
> 
> Isegi tööriistasõbralikud mudelid vajavad julgustust MCP tööriistade kasutamiseks! Kaalu süsteemiprompti või [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) lisamist, näiteks: "Sul on juurdepääs `microsoft.docs.mcp` – kasuta seda tööriista Microsofti uusima ametliku dokumentatsiooni otsimiseks, kui käsitled küsimusi Microsofti tehnoloogiate kohta nagu C#, Azure, ASP.NET Core või Entity Framework."
>
> Selle suurepärase näite nägemiseks vaata [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) Awesome GitHub Copilot repository'st. See režiim kasutab spetsiaalselt Microsoft Learn Docs MCP serverit, et aidata puhastada ja moderniseerida C# koodi, kasutades uusimaid mustreid ja parimaid praktikaid.

### 2. ☁️ Azure MCP server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mida see teeb**: Azure MCP Server on terviklik komplekt enam kui 15 spetsialiseeritud Azure'i teenuse ühendajast, mis toovad kogu Azure'i ökosüsteemi teie AI töövoogu. See pole lihtsalt üks server – see on võimas kogum, mis hõlmab ressursside haldust, andmebaasiühendusi (PostgreSQL, SQL Server), Azure Monitori logianalüüsi KQL-iga, Cosmos DB integratsiooni ja palju muud.

**Miks see on kasulik**: Lisaks Azure'i ressursside haldamisele parandab see server oluliselt koodi kvaliteeti Azure SDK-dega töötamisel. Kui kasutate Azure MCP-d Agent-režiimis, ei aita see teil lihtsalt koodi kirjutada – see aitab teil kirjutada *paremat* Azure'i koodi, mis järgib praeguseid autentimismustreid, vigade käsitlemise parimaid tavasid ja kasutab uusimaid SDK funktsioone. Selle asemel, et saada üldist koodi, mis võib töötada, saate koodi, mis järgib Azure'i soovitatud mustreid tootmiskoormuste jaoks.

**Peamised moodulid**:
- **🗄️ Andmebaasiühendajad**: Loomulik keelepõhine juurdepääs Azure Database for PostgreSQL-le ja SQL Serverile
- **📊 Azure Monitor**: KQL-põhine logianalüüs ja operatiivsed ülevaated
- **🌐 Ressursside haldus**: Täielik Azure'i ressursside elutsükli haldus
- **🔐 Autentimine**: DefaultAzureCredential ja hallatud identiteedi mustrid
- **📦 Salvestusteenused**: Blob Storage, Queue Storage ja Table Storage operatsioonid
- **🚀 Konteineriteenused**: Azure Container Apps, Container Instances ja AKS haldus
- **Ja palju teisi spetsialiseeritud ühendajaid**

**Reaalne kasutus**: "Loetle minu Azure'i salvestuskontod", "Päring minu Log Analytics tööruumist viimase tunni vigade kohta" või "Aita mul luua Azure'i rakendus Node.js-is koos korrektse autentimisega"

**Täielik demo stsenaarium**: Siin on täielik juhend, mis näitab Azure MCP ja GitHub Copilot for Azure laienduse kombinatsiooni võimsust VS Code'is. Kui mõlemad on installitud, saate esitada järgmise päringu:

> "Loo Python skript, mis laadib faili üles Azure Blob Storage'i, kasutades DefaultAzureCredential autentimist. Skript peaks ühenduma minu Azure'i salvestuskontoga nimega 'mycompanystorage', laadima üles konteinerisse nimega 'documents', looma testfaili praeguse ajatempli alusel üleslaadimiseks, käsitlema vigu elegantselt ja pakkuma informatiivset väljundit, järgima Azure'i parimaid tavasid autentimise ja vigade käsitlemise osas, sisaldama kommentaare, mis selgitavad, kuidas DefaultAzureCredential autentimine töötab, ning olema hästi struktureeritud koos korrektsete funktsioonide ja dokumentatsiooniga."

Azure MCP Server genereerib täieliku, tootmisvalmis Python skripti, mis:
- Kasutab uusimat Azure Blob Storage SDK-d koos korrektsete asünkroonsete mustritega
- Rakendab DefaultAzureCredential koos põhjaliku varuahela selgitusega
- Sisaldab tugevat vigade käsitlemist koos konkreetsete Azure'i eranditüüpidega
- Järgib Azure SDK parimaid tavasid ressursside halduse ja ühenduse käsitlemise osas
- Pakub üksikasjalikku logimist ja informatiivset konsooliväljundit
- Loob korrektselt struktureeritud skripti koos funktsioonide, dokumentatsiooni ja tüüpide vihjetega

Mis teeb selle erakordseks, on see, et ilma Azure MCP-ta võite saada üldise Blob Storage koodi, mis töötab, kuid ei järgi praeguseid Azure'i mustreid. Azure MCP-ga saate koodi, mis kasutab uusimaid autentimismeetodeid, käsitleb Azure'i spetsiifilisi veastsenaarioid ja järgib Microsofti soovitatud tavasid tootmisrakenduste jaoks.

**Esiletõstetud näide**: Olen sageli hädas `az` ja `azd` CLI käskude konkreetse süntaksi meeldejätmisega juhuslikuks kasutamiseks. Minu jaoks on see alati kaheastmeline protsess: kõigepealt otsin süntaksi üles, siis käivitan käsu. Sageli lähen lihtsalt portaali ja klõpsan seal, et töö tehtud saada, sest ei taha tunnistada, et ei mäleta CLI süntaksit. Võimalus lihtsalt kirjeldada, mida ma tahan, on hämmastav, ja veel parem, et saan seda teha ilma oma IDE-st lahkumata!

Azure MCP repositooriumis on suurepärane nimekiri kasutusjuhtudest, mis aitavad teil alustada: [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server). Täielike seadistusjuhendite ja täiustatud konfiguratsioonivalikute jaoks vaadake [ametlikku Azure MCP dokumentatsiooni](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mida see teeb**: Ametlik GitHub MCP Server pakub sujuvat integreerimist GitHubi ökosüsteemiga, pakkudes nii hostitud kaugjuurdepääsu kui ka kohaliku Dockeri juurutamise võimalusi. See ei puuduta ainult põhilisi repositooriumi operatsioone – see on terviklik tööriistakomplekt, mis hõlmab GitHub Actions haldust, pull request töövooge, probleemide jälgimist, turvaskaneerimist, teavitusi ja täiustatud automatiseerimisvõimalusi.

**Miks see on kasulik**: See server muudab teie suhtlemist GitHubiga, tuues kogu platvormi kogemuse otse teie arenduskeskkonda. Selle asemel, et pidevalt vahetada VS Code'i ja GitHub.com-i vahel projektijuhtimise, koodiarvustuste ja CI/CD jälgimise jaoks, saate kõike hallata loomulike keelepõhiste käskudega, jäädes samal ajal keskendunuks oma koodile.

> **ℹ️ Märkus: Erinevad 'Agentide' tüübid**
> 
> Ärge ajage segamini GitHub MCP Serverit GitHubi Coding Agentiga (AI agent, kellele saab määrata ülesandeid automaatseks koodi loomiseks). GitHub MCP Server töötab VS Code'i Agent-režiimis, et pakkuda GitHub API integratsiooni, samas kui GitHubi Coding Agent on eraldi funktsioon, mis loob pull requeste, kui talle määratakse GitHubi probleeme.

**Peamised võimalused**:
- **⚙️ GitHub Actions**: Täielik CI/CD torujuhtme haldus, töövoo jälgimine ja artefaktide käsitlemine
- **🔀 Pull Requestid**: Loo, vaata üle, ühenda ja halda PR-e koos põhjaliku oleku jälgimisega
- **🐛 Probleemid**: Täielik probleemide elutsükli haldus, kommenteerimine, sildistamine ja määramine
- **🔒 Turvalisus**: Koodiskaneerimise hoiatused, salajaste andmete tuvastamine ja Dependabot integratsioon
- **🔔 Teavitused**: Nutikas teavituste haldus ja repositooriumi tellimuste kontroll
- **📁 Repositooriumi haldus**: Failioperatsioonid, harude haldus ja repositooriumi administratsioon
- **👥 Koostöö**: Kasutajate ja organisatsioonide otsing, meeskonna haldus ja juurdepääsu kontroll

**Reaalne kasutus**: "Loo pull request minu feature harust", "Näita mulle kõiki ebaõnnestunud CI jooksusid sel nädalal", "Loetle avatud turvahoiatused minu repositooriumides" või "Leia kõik probleemid, mis on määratud mulle minu organisatsioonides"

**Täielik demo stsenaarium**: Siin on võimas töövoog, mis demonstreerib GitHub MCP Serveri võimalusi:

> "Pean valmistuma meie sprindi ülevaateks. Näita mulle kõiki pull requeste, mille olen sel nädalal loonud, kontrolli meie CI/CD torujuhtmete olekut, loo kokkuvõte turvahoiatustest, mida peame lahendama, ja aita mul koostada väljalaskemärkmeid, mis põhinevad 'feature' sildiga ühendatud PR-idel."

GitHub MCP Server:
- Pärib teie hiljutised pull requestid koos üksikasjaliku olekuteabega
- Analüüsib töövoo jooksusid ja toob esile kõik ebaõnnestumised või jõudlusprobleemid
- Koostab turvaskaneerimise tulemused ja prioriseerib kriitilised hoiatused
- Genereerib põhjalikud väljalaskemärkmed, ekstraheerides teavet ühendatud PR-idest
- Pakub tegevuskõlblikke järgmisi samme sprindi planeerimiseks ja väljalaske ettevalmistamiseks

**Esiletõstetud näide**: Mulle meeldib seda kasutada koodiarvustuse töövoogude jaoks. Selle asemel, et hüpata VS Code'i, GitHubi teavituste ja pull request lehtede vahel, saan öelda "Näita mulle kõiki PR-e, mis ootavad minu arvustust" ja siis "Lisa kommentaar PR #123-le, küsides autentimismeetodi vigade käsitlemise kohta." Server haldab GitHub API kõnesid, säilitab arutelu konteksti ja aitab mul isegi koostada konstruktiivsemaid arvustuse kommentaare.

**Autentimisvõimalused**: Server toetab nii OAuthi (sujuv VS Code'is) kui ka isiklikke juurdepääsutokenit, koos konfigureeritavate tööriistakomplektidega, mis võimaldavad ainult vajalikke GitHubi funktsioone. Seda saab käivitada kaugteenusena kiireks seadistamiseks või kohapeal Dockeriga täieliku kontrolli jaoks.

> **💡 Pro nõuanne**
> 
> Lubage ainult vajalikke tööriistakomplekte, konfigureerides `--toolsets` parameetrit oma MCP serveri seadetes, et vähendada konteksti suurust ja parandada AI tööriistade valikut. Näiteks lisage `"--toolsets", "repos,issues,pull_requests,actions"` oma MCP konfiguratsiooni argumentidesse põhiarenduse töövoogude jaoks või kasutage `"--toolsets", "notifications, security"`, kui soovite peamiselt GitHubi jälgimisvõimalusi.
### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mida see teeb**: Ühendub Azure DevOps teenustega, pakkudes terviklikku projektijuhtimist, tööülesannete jälgimist, ehitustorude haldust ja repositooriumi operatsioone.

**Miks see on kasulik**: Meeskondadele, kes kasutavad Azure DevOpsi oma peamise DevOps platvormina, kõrvaldab see MCP server pideva vahetamise arenduskeskkonna ja Azure DevOps veebiliidese vahel. Saate hallata tööülesandeid, kontrollida ehituste olekuid, pärida repositooriume ja käsitleda projektijuhtimise ülesandeid otse oma AI assistendi kaudu.

**Reaalne kasutus**: "Näita mulle kõiki aktiivseid tööülesandeid praeguses sprindis WebApp projekti jaoks", "Loo veaaruanne sisselogimisprobleemi kohta, mille just avastasin" või "Kontrolli meie ehitustorude olekut ja näita mulle hiljutisi ebaõnnestumisi"

**Esiletõstetud näide**: Saate hõlpsalt kontrollida oma meeskonna praeguse sprindi olekut lihtsa päringuga nagu "Näita mulle kõiki aktiivseid tööülesandeid praeguses sprindis WebApp projekti jaoks" või "Loo veaaruanne sisselogimisprobleemi kohta, mille just avastasin" ilma arenduskeskkonnast lahkumata.

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mida see teeb**: MarkItDown on põhjalik dokumendikonversiooni server, mis teisendab erinevaid failivorminguid kvaliteetseks Markdowniks, optimeeritud LLM-i tarbimiseks ja tekstianalüüsi töövoogudeks.

**Miks see on kasulik**: Hädavajalik kaasaegsete dokumenteerimistöövoogude jaoks! MarkItDown suudab töödelda muljetavaldavat valikut failivorminguid, säilitades samal ajal olulise dokumendi struktuuri, nagu pealkirjad, loendid, tabelid ja lingid. Erinevalt lihtsatest teksti väljavõtmise tööriistadest keskendub see semantilise tähenduse ja vormingu säilitamisele, mis on väärtuslik nii AI töötlemiseks kui ka inimloetavuseks.

**Toetatud failivormingud**:
- **Office dokumendid**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Meediafailid**: Pildid (EXIF metaandmetega ja OCR-iga), heli (EXIF metaandmetega ja kõne transkriptsiooniga)
- **Veebisisu**: HTML, RSS vood, YouTube'i URL-id, Wikipedia lehed
- **Andmevormingud**: CSV, JSON, XML, ZIP-failid (töötleb sisu rekursiivselt)
- **Avaldamisvormingud**: EPub, Jupyteri märkmikud (.ipynb)
- **E-post**: Outlooki sõnumid (.msg)
- **Täpsemad**: Azure Document Intelligence integratsioon täiustatud PDF-töötluseks

**Täpsemad võimalused**: MarkItDown toetab LLM-i juhitud pildikirjeldusi (kui on olemas OpenAI klient), Azure Document Intelligence'i täiustatud PDF-töötluseks, kõne transkriptsiooni helisisu jaoks ja pistikprogrammide süsteemi täiendavate failivormingute lisamiseks.

**Reaalsed kasutusjuhtumid**: "Teisenda see PowerPointi esitlus Markdowniks meie dokumenteerimissaidi jaoks", "Ekstrakti tekst sellest PDF-ist koos korrektse pealkirja struktuuriga" või "Muuda see Exceli tabel loetavaks tabelivorminguks"

**Esiletõstetud näide**: Tsitaat [MarkItDown dokumentatsioonist](https://github.com/microsoft/markitdown#why-markdown):

> Markdown on väga lähedane lihttekstile, minimaalse märgistuse või vorminguga, kuid siiski võimaldab esitada olulist dokumendi struktuuri. Peamised LLM-id, nagu OpenAI GPT-4o, "räägivad" Markdowni loomulikult ja sageli lisavad Markdowni oma vastustesse ilma eraldi juhisteta. See viitab sellele, et neid on treenitud tohutul hulgal Markdown-vormingus tekstiga ja nad mõistavad seda hästi. Täiendava eelisena on Markdowni konventsioonid ka väga tõhusad tokenite osas.

MarkItDown on väga hea dokumendi struktuuri säilitamisel, mis on oluline AI töövoogude jaoks. Näiteks PowerPointi esitlust konverteerides säilitab see slaidide korralduse koos õigete pealkirjadega, ekstraktib tabelid Markdowni tabelitena, lisab piltidele alternatiivteksti ja töötleb isegi esineja märkmeid. Diagrammid teisendatakse loetavateks andmetabeliteks ja tulemuseks olev Markdown säilitab algse esitluse loogilise voolu. See teeb selle ideaalseks esitluse sisu AI-süsteemidesse sisestamiseks või olemasolevatest slaididest dokumentatsiooni loomiseks.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mida see teeb**: Pakub vestluslikku juurdepääsu SQL Serveri andmebaasidele (kohapeal, Azure SQL või Fabric)

**Miks see on kasulik**: Sarnane PostgreSQL serverile, kuid Microsoft SQL ökosüsteemi jaoks. Ühenda lihtsa ühenduse stringiga ja alusta päringute tegemist loomulikus keeles – enam pole vaja konteksti vahetada!

**Reaalsed kasutusjuhtumid**: "Leia kõik tellimused, mida pole viimase 30 päeva jooksul täidetud" tõlgitakse sobivateks SQL-päringuteks ja tagastatakse vormindatud tulemused.

**Esiletõstetud näide**: Kui oled oma andmebaasiühenduse seadistanud, saad kohe alustada vestlust oma andmetega. Blogipostitus näitab seda lihtsa küsimusega: "millise andmebaasiga oled ühendatud?" MCP server vastab, kutsudes esile sobiva andmebaasi tööriista, ühendades sinu SQL Serveri instantsiga ja tagastades üksikasjad sinu praeguse andmebaasiühenduse kohta – kõik ilma ühegi SQL-reani. Server toetab ulatuslikke andmebaasioperatsioone alates skeemihaldusest kuni andmete manipuleerimiseni, kõik läbi loomuliku keele käskude. Täielikud seadistusjuhised ja konfiguratsiooninäited VS Code'i ja Claude Desktopiga leiad siit: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mida see teeb**: Võimaldab AI agentidel veebilehtedega suhelda testimiseks ja automatiseerimiseks.

> **ℹ️ GitHub Copiloti jõustamine**
> 
> Playwright MCP Server toetab GitHub Copiloti Coding Agent'i, andes sellele veebibrauseri võimekuse! [Loe selle funktsiooni kohta rohkem](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miks see on kasulik**: Ideaalne automatiseeritud testimiseks, mida juhivad loomuliku keele kirjeldused. AI saab navigeerida veebisaitidel, täita vorme ja ekstraktida andmeid struktureeritud juurdepääsetavuse hetkepiltide kaudu – see on uskumatult võimas!

**Reaalsed kasutusjuhtumid**: "Testi sisselogimisvoogu ja kontrolli, kas armatuurlaud laaditakse õigesti" või "Loo test, mis otsib tooteid ja valideerib tulemuste lehe" – kõik ilma rakenduse lähtekoodi vajamata.

**Esiletõstetud näide**: Minu kolleeg Debbie O'Brien on viimasel ajal teinud hämmastavat tööd Playwright MCP Serveriga! Näiteks näitas ta hiljuti, kuidas saab luua täielikke Playwright teste isegi ilma rakenduse lähtekoodile juurdepääsuta. Tema stsenaariumis palus ta Copilotil luua testi filmide otsingu rakenduse jaoks: navigeeri saidile, otsi "Garfield" ja kontrolli, kas film ilmub tulemustes. MCP käivitas brauseri sessiooni, uuris lehe struktuuri DOM-i hetkepiltide abil, leidis õiged selektorid ja genereeris täielikult töötava TypeScripti testi, mis läbis esimese jooksu.

Mis teeb selle tõeliselt võimsaks, on see, et see ühendab loomuliku keele juhised ja täidetava testkoodi. Traditsioonilised lähenemised nõuavad kas käsitsi testide kirjutamist või juurdepääsu koodibaasile konteksti jaoks. Kuid Playwright MCP abil saab testida väliseid saite, kliendirakendusi või töötada musta kasti testimise stsenaariumides, kus koodile juurdepääs pole saadaval.

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mida see teeb**: Halda Microsoft Dev Box keskkondi loomuliku keele abil.

**Miks see on kasulik**: Lihtsustab arenduskeskkondade haldamist tohutult! Loo, konfigureeri ja halda arenduskeskkondi ilma konkreetseid käske meelde jätmata.

**Reaalsed kasutusjuhtumid**: "Seadista uus Dev Box koos uusima .NET SDK-ga ja konfigureeri see meie projekti jaoks", "Kontrolli kõigi minu arenduskeskkondade olekut" või "Loo standardiseeritud demo keskkond meie meeskonna esitluste jaoks".

**Esiletõstetud näide**: Olen suur Dev Boxi isikliku arenduse jaoks kasutamise fänn. Minu "ahhaa-moment" oli siin, kui James Montemagno selgitas, kui suurepärane Dev Box on konverentside demode jaoks, kuna sellel on ülikiire Etherneti ühendus, olenemata konverentsi / hotelli / lennuki wifi kvaliteedist, mida ma hetkel kasutan. Tegelikult tegin hiljuti konverentsi demo harjutusi, kui minu sülearvuti oli ühendatud telefoni hotspotiga, samal ajal kui sõitsin bussiga Brügge'ist Antwerpenisse! Kuid minu järgmine samm siin on süveneda rohkem meeskonna mitme arenduskeskkonna ja standardiseeritud demo keskkondade haldamisse. Ja teine suur kasutusjuhtum, mida olen klientidelt ja kolleegidelt kuulnud, on Dev Boxi kasutamine eelkonfigureeritud arenduskeskkondade jaoks. Mõlemal juhul võimaldab MCP Dev Boxide konfigureerimist ja haldamist loomuliku keele interaktsiooni kaudu, jäädes samal ajal sinu arenduskeskkonda.

### 9. 🤖 Azure AI Foundry MCP Server
[![Installige VS Code'is](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Installige VS Code Insiders'is](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Mida see teeb**: Azure AI Foundry MCP Server pakub arendajatele põhjalikku juurdepääsu Azure'i AI ökosüsteemile, sealhulgas mudelikataloogidele, juurutamise haldusele, teadmiste indekseerimisele Azure AI Search abil ja hindamisvahenditele. See eksperimentaalne server ühendab AI arenduse ja Azure'i võimsa AI infrastruktuuri, muutes AI rakenduste loomise, juurutamise ja hindamise lihtsamaks.

**Miks see on kasulik**: See server muudab Azure'i AI teenustega töötamise viisi, tuues ettevõtte tasemel AI võimalused otse teie arenduskeskkonda. Selle asemel, et vahetada Azure'i portaali, dokumentatsiooni ja IDE vahel, saate avastada mudeleid, juurutada teenuseid, hallata teadmistebaase ja hinnata AI jõudlust loomuliku keele käskude abil. See on eriti kasulik arendajatele, kes loovad RAG (Retrieval-Augmented Generation) rakendusi, haldavad mitme mudeli juurutusi või rakendavad põhjalikke AI hindamispipeline'e.

**Peamised arendaja võimalused**:
- **🔍 Mudelite avastamine ja juurutamine**: Uurige Azure AI Foundry mudelikataloogi, hankige üksikasjalikku mudeliteavet koos koodinäidetega ja juurutage mudeleid Azure AI teenustesse
- **📚 Teadmiste haldamine**: Looge ja hallake Azure AI Search indekseid, lisage dokumente, konfigureerige indekseerijaid ja ehitage keerukaid RAG süsteeme
- **⚡ AI agentide integreerimine**: Ühendage Azure AI agentidega, pärige olemasolevaid agente ja hinnake agentide jõudlust tootmistsenaariumides
- **📊 Hindamisraamistik**: Käivitage põhjalikke teksti ja agentide hindamisi, looge markdown-aruandeid ja rakendage kvaliteedikontrolli AI rakenduste jaoks
- **🚀 Prototüüpimise tööriistad**: Hankige seadistusjuhised GitHub-põhise prototüüpimise jaoks ja juurdepääs Azure AI Foundry laboritele tipptasemel uurimismudelite jaoks

**Reaalne arendaja kasutus**: "Juuruta Phi-4 mudel Azure AI teenustesse minu rakenduse jaoks", "Loo uus otsinguindeks minu dokumentatsiooni RAG süsteemi jaoks", "Hinda minu agendi vastuseid kvaliteedimõõdikute alusel" või "Leia parim põhjendusmudel minu keerukate analüüsitööde jaoks"

**Täielik demo stsenaarium**: Siin on võimas AI arenduse töövoog:

> "Ma ehitan klienditoe agenti. Aita mul leida kataloogist hea põhjendusmudel, juuruta see Azure AI teenustesse, loo teadmistebaas meie dokumentatsioonist, seadista hindamisraamistik vastuste kvaliteedi testimiseks ja aita mul prototüüpida integreerimist GitHubi tokeniga testimiseks."

Azure AI Foundry MCP Server:
- Pärib mudelikataloogi, et soovitada optimaalseid põhjendusmudeleid vastavalt teie nõuetele
- Pakub juurutamiskäske ja kvooditeavet teie eelistatud Azure'i piirkonna jaoks
- Seadistab Azure AI Search indekseid teie dokumentatsiooni jaoks sobiva skeemiga
- Konfigureerib hindamispipeline'id kvaliteedimõõdikute ja turvakontrollidega
- Genereerib prototüüpimiskoodi GitHubi autentimisega koheseks testimiseks
- Pakub põhjalikke seadistusjuhendeid, mis on kohandatud teie konkreetsele tehnoloogiapaketile

**Esiletõstetud näide**: Arendajana olen ma vaeva näinud, et hoida end kursis erinevate LLM mudelitega, mis on saadaval. Ma tean mõnda peamist, kuid tunnen, et jään ilma mõnest tootlikkuse ja efektiivsuse eelisest. Tokenid ja kvoodid on stressirohked ja keerulised hallata – ma ei tea kunagi, kas valin õige mudeli õige ülesande jaoks või kulutan oma eelarvet ebaefektiivselt. Kuulsin sellest MCP serverist James Montemagno käest, kui otsisin meeskonnakaaslaste soovitusi MCP serveri jaoks, ja olen põnevil, et saan seda kasutada! Mudelite avastamise võimalused tunduvad eriti muljetavaldavad kellegi jaoks nagu mina, kes tahab uurida tavapärasest kaugemale ja leida mudeleid, mis on optimeeritud konkreetsete ülesannete jaoks. Hindamisraamistik peaks aitama mul kinnitada, et saan tegelikult paremaid tulemusi, mitte lihtsalt proovin midagi uut proovimise pärast.

> **ℹ️ Eksperimentaalne staatus**
> 
> See MCP server on eksperimentaalne ja aktiivses arenduses. Funktsioonid ja API-d võivad muutuda. Ideaalne Azure AI võimaluste uurimiseks ja prototüüpide loomiseks, kuid kontrollige stabiilsusnõudeid tootmiskasutuseks.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Installige VS Code'is](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Installige VS Code Insiders'is](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Mida see teeb**: Pakub arendajatele olulisi tööriistu AI agentide ja rakenduste loomiseks, mis integreeruvad Microsoft 365 ja Microsoft 365 Copilotiga, sealhulgas skeemi valideerimine, näidiskoodi leidmine ja tõrkeotsingu abi.

**Miks see on kasulik**: Microsoft 365 ja Copiloti jaoks arendamine hõlmab keerukaid manifestiskeeme ja spetsiifilisi arendusmustreid. See MCP server toob olulised arendusressursid otse teie kodeerimiskeskkonda, aidates valideerida skeeme, leida näidiskoodi ja lahendada levinud probleeme ilma dokumentatsiooni pidevalt viitamata.

**Reaalne kasutus**: "Valideeri minu deklaratiivne agendi manifest ja paranda skeemivead", "Näita mulle näidiskoodi Microsoft Graph API plugin'i rakendamiseks" või "Aita mul lahendada Teamsi rakenduse autentimisprobleeme"

**Esiletõstetud näide**: Pöördusin oma sõbra John Milleri poole pärast vestlust temaga Buildi üritusel M365 agentide teemal, ja ta soovitas seda MCP-d. See võiks olla suurepärane algajatele M365 agentide arendajatele, kuna see pakub malle, näidiskoodi ja alustamiseks vajalikke tööriistu ilma dokumentatsioonis uppumata. Skeemi valideerimise funktsioonid tunduvad eriti kasulikud, et vältida manifestistruktuuri vigu, mis võivad põhjustada tundidepikkust silumist.

> **💡 Pro nõuanne**
> 
> Kasutage seda serverit koos Microsoft Learn Docs MCP serveriga, et saada terviklikku M365 arendustuge – üks pakub ametlikku dokumentatsiooni, samas kui teine pakub praktilisi arendustööriistu ja tõrkeotsingu abi.


## Mis edasi? 🔮

## 📋 Kokkuvõte

Model Context Protocol (MCP) muudab arendajate suhtlemist AI assistentide ja väliste tööriistadega. Need 10 Microsofti MCP serverit näitavad standardiseeritud AI integratsiooni jõudu, võimaldades sujuvaid töövooge, mis hoiavad arendajaid nende töövoos, pakkudes samal ajal võimsaid väliseid võimalusi.

Alates Azure'i ökosüsteemi põhjalikust integreerimisest kuni spetsialiseeritud tööriistadeni nagu Playwright brauseri automatiseerimiseks ja MarkItDown dokumentide töötlemiseks, need serverid näitavad, kuidas MCP võib suurendada tootlikkust mitmekesistes arendusstsenaariumides. Standardiseeritud protokoll tagab, et need tööriistad töötavad koos sujuvalt, luues ühtse arenduskogemuse.

Kuna MCP ökosüsteem areneb edasi, on kogukonnaga kaasas käimine, uute serverite uurimine ja kohandatud lahenduste loomine võtmetähtsusega, et maksimeerida arenduse tootlikkust. MCP avatud standardi olemus tähendab, et saate kombineerida tööriistu erinevatelt tarnijatelt, et luua täiuslik töövoog vastavalt oma konkreetsetele vajadustele.

## 🔗 Lisamaterjalid

- [Ametlik Microsoft MCP repo](https://github.com/microsoft/mcp)
- [MCP kogukond ja dokumentatsioon](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentatsioon](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentatsioon](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentatsioon](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP üritused](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot kohandused](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29./30. juuli või vaata nõudmisel](https://aka.ms/mcpdevdays)

## 🎯 Harjutused

1. **Paigaldamine ja konfigureerimine**: Seadistage üks MCP server oma VS Code keskkonnas ja testige põhifunktsionaalsust.
2. **Töövoo integreerimine**: Kujundage arendustöövoog, mis kombineerib vähemalt kolm erinevat MCP serverit.
3. **Kohandatud serveri planeerimine**: Määrake ülesanne oma igapäevases arendusrutiinis, mis võiks kasu saada kohandatud MCP serverist, ja looge selle spetsifikatsioon.
4. **Jõudluse analüüs**: Võrrelge MCP serverite kasutamise efektiivsust traditsiooniliste lähenemisviisidega tavapäraste arendustööde jaoks.
5. **Turvalisuse hindamine**: Hinnake MCP serverite kasutamise turvalisuse mõju oma arenduskeskkonnas ja tehke ettepanekuid parimate tavade kohta.


Next:[Parimad tavad](../08-BestPractices/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.