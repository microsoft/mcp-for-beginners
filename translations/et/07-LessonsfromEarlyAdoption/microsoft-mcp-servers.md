# 🚀 10 Microsoft MCP-serverit, mis muudavad arendaja tootlikkust

## 🎯 Mida sa selles juhendis õpid

See praktiline juhend tutvustab kümmet Microsofti MCP-serverit, mis muudavad aktiivselt seda, kuidas arendajad töötavad AI-abilistega. Selle asemel, et ainult selgitada, mida MCP-serverid *võivad* teha, näitame servereid, mis juba teevad igapäevases arendustöös Microsoftis ja mujal tõelist vahet.

Iga selles juhendis olev server on valitud päriselulise kasutuse ja arendajate tagasiside põhjal. Avastad mitte ainult seda, mida iga server teeb, vaid miks see on oluline ja kuidas sellest oma projektides maksimaalselt kasu lõigata. Olenemata sellest, kas oled MCP-s täiesti uus või soovid oma olemasolevat seadistust laiendada, esindavad need serverid mõned Microsofti ökosüsteemi kõige praktilisemad ja mõjusamad tööriistad.

> **💡 Kiire alguse näpunäide**
> 
> Uus MCP-s? Ära muretse! See juhend on loodud algajatele. Selgitame mõisteid jooksvalt ja sa võid alati viidata meie [Sissejuhatus MCP-sse](../00-Introduction/README.md) ja [Põhikontseptsioonid](../01-CoreConcepts/README.md) moodulitele põhjalikuma tausta saamiseks.

## Ülevaade

See põhjalik juhend uurib kümmet Microsofti MCP-serverit, mis revolutsioneerivad seda, kuidas arendajad suhtlevad AI-abiliste ja väliste tööriistadega. Alates Azure'i ressursside haldamisest kuni dokumentide töötlemiseni näitavad need serverid Model Context Protocoli jõudu sujuvate ja produktiivsete arendusvoogude loomiseks.

## Õpieesmärgid

Selle juhendi lõpuks oskad:
- Mõista, kuidas MCP-serverid suurendavad arendajate tootlikkust
- Tutvuda Microsofti kõige mõjukamate MCP-serveri lahendustega
- Avastada iga serveri praktilised kasutusjuhtumid
- Teada, kuidas neid servereid seadistada ja konfigureerida VS Code'is ja Visual Studios
- Uurida laiemat MCP-ökosüsteemi ja tuleviku suundi

## 🔧 MCP-serverite mõistmine: juhend algajale

### Mis on MCP-serverid?

Nagu Model Context Protocol (MCP) algajana võid imestada: "Mis täpselt on MCP-server, ja miks see mind peaks huvitama?" Alustame lihtsa võrdlusega.

Mõtle MCP-serveritele kui spetsialiseerunud assistentidele, mis aitavad su AI-kodeerimiskaaslasel (näiteks GitHub Copilot) ühenduda väliste tööriistade ja teenustega. Nii nagu võid telefonis kasutada erinevaid rakendusi eri ülesannete jaoks—üht ilma jaoks, teist navigatsiooni jaoks, kolmandat panganduse jaoks—annavad MCP-serverid su AI-abilisele võime suhelda erinevate arendustööriistade ja teenustega.

### Probleem, mida MCP-serverid lahendavad

Enne MCP-serverite kasutuselevõttu, kui soovisid:
- Kontrollida oma Azure'i ressursse
- Luua GitHubi issue 
- Pärida oma andmebaasi
- Otsida dokumentatsioonist

Peaksid lõpetama kodeerimise, avama brauseri, minema vastavale veebilehele ja need toimingud käsitsi tegema. See pidev kontekstivahetus katkestab su töövoo ja vähendab tootlikkust.

### Kuidas MCP-serverid muudavad su arenduskogemust

MCP-serveritega saad jääda oma arenduskeskkonda (VS Code, Visual Studio jne) ja paluda lihtsalt oma AI-abilisel neid ülesandeid täita. Näiteks:

**Selle traditsioonilise töövoo asemel:**
1. Lõpeta kodeerimine
2. Ava brauser
3. Ava Azure'i portaal
4. Otsi üles salvestuskonto andmed
5. Naase VS Code'i
6. Jätka kodeerimist

**Sa võid nüüd teha järgmist:**
1. Kysi AI-ilt: "Mis on minu Azure'i salvestuskontode olek?"
2. Jätka kodeerimist antud teabe abil

### Põhilised eelised algajatele

#### 1. 🔄 **Jää vooluseisundisse**
- Pole vaja enam rakenduste vahel vahetada
- Hoia keskendumine kirjutatavale koodile
- Vähenda vaimset koormust erinevate tööriistade haldamisel

#### 2. 🤖 **Kasuta loomulikku keelt keeruliste käskude asemel**
- Selle asemel, et pähe õppida SQL-i süntaksit, kirjelda, milliseid andmeid vajad
- Selle asemel, et meeles pidada Azure CLI käske, selgita, mida soovid saavutada
- Lase AI-l tegeleda tehniliste detailidega, samal ajal kui sa keskendud loogikale

#### 3. 🔗 **Ühenda mitmeid tööriistu omavahel**
- Loo võimsaid töövooge, kombineerides erinevaid teenuseid
- Näide: "Hangi kõik viimased GitHubi issue'd ja loo vastavad Azure DevOpsi tööüksused"
- Ehita automatiseerimine ilma keerulisi skripte kirjutamata

#### 4. 🌐 **Juurdepääs kasvavale ökosüsteemile**
- Saa kasu Microsofti, GitHubi ja teiste ettevõtete loodud serveritest
- Ühenda erinevate pakkujate tööriistu sujuvalt
- Liitu standardiseeritud ökosüsteemiga, mis töötab erinevate AI-abilistega

#### 5. 🛠️ **Õpi praktikas**
- Alusta eelnevalt ehitatud serveritega, et mõista kontseptsioone
- Ehita järk-järgult oma servereid, kui tunned end mugavamalt
- Kasuta olemasolevaid SDK-sid ja dokumentatsiooni, et oma õppimist juhendada

### Päriselu näide algajatele

Oletame, et oled uus veebiarenduses ja töötad oma esimesel projektil. Siin on, kuidas MCP-serverid saavad aidata:

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

**MCP-serveritega:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Ettevõtte standardi eelis

MCP-st saab tööstusharuülene standard, mis tähendab:
- **Järjepidevus**: Sarnane kogemus erinevate tööriistade ja ettevõtete vahel
- **Ühilduvus**: Erinevate pakkujate serverid töötavad koos
- **Tulevikukindlus**: Oskused ja seadistused kantakse üle erinevate AI-abiliste vahel
- **Kogukond**: Lai ökosüsteem jagatud teadmiste ja ressurssidega

### Alustamine: mida sa õpid

Selles juhendis uurime 10 Microsofti MCP-serverit, mis on eriti kasulikud arendajatele kõikidel tasemetel. Iga server on loodud selleks, et:
- Lahendada levinud arendusprobleeme
- Vähendada korduvaid ülesandeid
- Parandada koodi kvaliteeti
- Suurendada õppimisvõimalusi

> **💡 Õppimisnõuanne**
> 
> Kui oled MCP-s täiesti uus, alusta esmalt meie [Sissejuhatus MCP-sse](../00-Introduction/README.md) ja [Põhikontseptsioonid](../01-CoreConcepts/README.md) moodulitega. Siis tule siia tagasi, et näha neid kontseptsioone tegutsemises koos päris Microsofti tööriistadega.
>
> Täiendava konteksti saamiseks MCP tähtsuse kohta vaata Maria Naggaga postitust: [Ühenda korra, integreeri kõikjal MCP-ga](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## MCP-ga alustamine VS Code'is ja Visual Studios 🚀

Nende MCP-serverite seadistamine on lihtne, kui kasutad Visual Studio Code'i või Visual Studio 2022 koos GitHub Copilotiga.

### VS Code'i seadistamine

Siin on VS Code'i põhiprotsess:

1. **Lülita sisse Agent-režiim**: VS Code'is vaheta Copilot Chat aknas Agent-režiimile
2. **Konfigureeri MCP-serverid**: Lisa serveri konfiguratsioonid oma VS Code settings.json faili
3. **Käivita serverid**: Klõpsa iga serveri puhul nuppu "Käivita"
4. **Vali tööriistad**: Vali, milliseid MCP-servereid lubada oma praeguses sessioonis

For detailed setup instructions, see the [VS Code'i MCP dokumentatsioon](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Pro näpunäide: Halda MCP-servereid nagu proff!**
> 
> VS Code laienduste vaade sisaldab nüüd [mugavat uut kasutajaliidest installitud MCP-serverite haldamiseks](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Sul on kiire juurdepääs installitud MCP-serverite käivitamiseks, peatamiseks ja haldamiseks selge ja lihtsa liidese kaudu. Proovi järele!

### Visual Studio 2022 seadistamine

Visual Studio 2022 jaoks (versioon 17.14 või uuem):

1. **Lülita sisse Agent-režiim**: Klõpsa GitHub Copilot Chat aknas "Ask" rippmenüüd ja vali "Agent"
2. **Loo konfiguratsioonifail**: Loo `.mcp.json` fail oma lahenduse kataloogi (soovitatav asukoht: `<SOLUTIONDIR>\.mcp.json`)
3. **Konfigureeri serverid**: Lisa oma MCP-serverite konfiguratsioonid, kasutades standardset MCP-vormingut
4. **Tööriistade heakskiit**: Kui küsitakse, kinnita need tööriistad, mida soovid kasutada, sobivate õiguste ulatusega

Üksikasjalike Visual Studio seadistusjuhiste saamiseks vaata [Visual Studio MCP dokumentatsiooni](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Iga MCP-serveriga kaasnevad oma konfiguratsiooninõuded (ühendusstringid, autentimine jne), kuid seadistuse muster on mõlemas IDE-s ühtne.

## Õppetunnid Microsofti MCP-serveritelt 🛠️

### 1. 📚 Microsoft Learn Docs MCP-server

[![Paigalda VS Code'i](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Paigalda VS Code Insiders'i](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mida see teeb**: Microsoft Learn Docs MCP Server on pilves hostitud teenus, mis annab AI-abilistele reaalajas juurdepääsu ametlikule Microsofti dokumentatsioonile läbi Model Context Protocoli. See ühendub `https://learn.microsoft.com/api/mcp` ja võimaldab semantilist otsingut Microsoft Learnis, Azure'i dokumentatsioonis, Microsoft 365 dokumentatsioonis ja teistes ametlikes Microsofti allikates.

**Miks see kasulik on**: Kuigi see võib tunduda kui "lihtsalt dokumentatsioon", on see server tegelikult ülioluline iga arendaja jaoks, kes kasutab Microsofti tehnoloogiaid. Üks peamisi kaebusi .NET arendajatelt AI-kodeerimisabiliste kohta on, et need ei ole kursis uusimate .NET ja C# väljalasetega. Microsoft Learn Docs MCP Server lahendab selle, pakkudes reaalajas juurdepääsu kõige värskematele dokumentidele, API-viidetele ja parimatele praktikatele. Olgu sa töötad Azure SDK-de uusimate versioonidega, uurid uusi C# 13 funktsioone või rakendad tipptasemel Aspire-mustreid, see server tagab, et su AI-abilisel on juurdepääs autoriteetsele, ajakohasele infole, mida on vaja täpse ja moodsa koodi genereerimiseks.

**Reaalne kasutus**: „Millised on az cli käsud Azure container appi loomiseks vastavalt ametlikule Microsoft Learn dokumentatsioonile?” või „Kuidas konfigureerida Entity Frameworki sõltuvussüstimisega ASP.NET Core'is?” Või näiteks „Kontrolli seda koodi, et veenduda, kas see vastab Microsoft Learn dokumentatsiooni jõudlussoovitustele.” Server pakub põhjalikku katvust Microsoft Learnis, Azure'i dokumentatsioonis ja Microsoft 365 dokumentatsioonis, kasutades täiustatud semantilist otsingut kontekstitundlikuima info leidmiseks. See tagastab kuni 10 kõrgekvaliteedilist sisutükki koos artikli pealkirjade ja URL-idega, ligi pääsedes alati kõige värskematele Microsofti dokumentidele, kui need avaldatakse.

**Esiletõstetud näide**: Server avaldab `microsoft_docs_search` tööriista, mis teostab semantilist otsingut Microsofti ametliku tehnilise dokumentatsiooni vastu. Kui see on konfigureeritud, võid esitada küsimusi nagu „Kuidas rakendada JWT-autentimist ASP.NET Core'is?” ja saada üksikasjalikke, ametlikke vastuseid koos allikalingiga. Otsingu kvaliteet on erakordne, sest see mõistab konteksti – küsides „konteinerite” kohta Azure'i kontekstis tagastatakse Azure Container Instances dokumentatsioon, samal ajal kui sama termin .NET kontekstis tagastab asjakohast C# kollektsioonide infot.

See on eriti kasulik kiiresti muutuvate või hiljuti uuendatud raamistike ja kasutusjuhtumite puhul. Näiteks mõnes hiljutises arendusprojektis tahtsin kasutada funktsioone Aspire ja Microsoft.Extensions.AI viimastest väljalasetest. Microsoft Learn Docs MCP-serveri kaasamisega sain kasutada mitte ainult API-dokumente, vaid ka äsja avaldatud juhendeid ja samm-sammulisi õpetusi.

> **💡 Pro näpunäide**
> 
> Isegi tööriistasõbralikke mudeleid tuleb julgustada MCP-tööriistade kasutamiseks! Kaalu lisa süsteemiprompti või [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot), näiteks: "Sul on juurdepääs `microsoft.docs.mcp` – kasuta seda tööriista, et otsida Microsofti viimast ametlikku dokumentatsiooni, kui käsitled küsimusi Microsofti tehnoloogiate kohta nagu C#, Azure, ASP.NET Core või Entity Framework."
>
> Selle suurepärase näite toimimise nägemiseks vaata Awesome GitHub Copilot hoidlast [C# .NET Janitor vestlusrežiimi](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md). See režiim kasutab konkreetselt Microsoft Learn Docs MCP-serverit, et aidata C# koodi puhastada ja moderniseerida, kasutades uusimaid mustreid ja parimaid praktikaid.
### 2. ☁️ Azure MCP-server

[![Paigalda VS Code'i](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Paigalda VS Code Insiders'i](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mida see teeb**: Azure MCP Server on kõikehõlmav komplekt üle 15 spetsialiseeritud Azure'i teenuse ühendaja, mis toob kogu Azure'i ökosüsteemi su AI-töövoogu. See ei ole lihtsalt üks server – see on võimas kogu, mis sisaldab ressursside haldamist, andmebaasiühenduvust (PostgreSQL, SQL Server), Azure Monitori logianalüüsi KQL-iga, Cosmos DB integratsiooni ja palju muud.

**Miks see kasulik on**: Peale lihtsalt Azure'i ressursside haldamise parandab see server märkimisväärselt koodi kvaliteeti Azure SDK-dega töötades. Kui kasutad Azure MCP-d Agent-režiimis, siis see ei aita mitte ainult koodi kirjutada – see aitab kirjutada *paremat* Azure'i koodi, mis järgib praeguseid autentimismustreid, veahaldamise parimaid praktikaid ja kasutab uusimaid SDK-funktsioone. Selle asemel, et saada üldist koodi, mis võib töötada, saad koodi, mis järgib Azure'i soovitatud mustreid tootmistöökoormuste jaoks.

**Peamised moodulid sisaldavad**:
- **🗄️ Andmebaasi ühendused**: Otse loomulikus keeles juurdepääs Azure Database for PostgreSQL ja SQL Serveri teenustele
- **📊 Azure Monitor**: KQL-põhine logianalüüs ja operatiivsed ülevaated
- **🌐 Ressursside haldamine**: Täielik Azure'i ressursi elutsükli haldus
- **🔐 Autentimine**: DefaultAzureCredential ja hallatud identiteedi mustrid
- **📦 Salvestusteenused**: Blob Storage, Queue Storage ja Table Storage toimingud
- **🚀 Konteinriteenused**: Azure Container Apps, Container Instances ja AKS haldus
- **Ja palju rohkem spetsialiseeritud ühendajaid**

**Tõeline kasutus**: „Too välja minu Azure'i salvestuskontod”, „Päringu mu Log Analytics tööruumist viimase tunni vigade kohta” või „Aita mul ehitada Azure'i rakendust Node.jsiga koos korrektse autentimisega”

**Täielik demo stsenaarium**: Siin on täielik samm-sammuline juhend, mis näitab Azure MCP kombineerimise jõudu GitHub Copilot for Azure laiendiga VS Code'is. Kui sul on mõlemad installitud ja esitad prompti:

> "Loo Python-skript, mis üleslaadib faili Azure Blob Storage'i, kasutades DefaultAzureCredential autentimist. Skript peaks ühenduma minu Azure salvestuskontoga nimega 'mycompanystorage', üles laadima konteinerisse nimega 'documents', looma üleslaadimiseks testi faili, mille nimi sisaldab praegust ajatemplit, käsitlema vigu pehmelt ja andma informatiivset väljundit, järgima Azure'i parimaid tavasid autentimise ja veakäsitluse osas, sisaldama kommentaare, mis selgitavad, kuidas DefaultAzureCredential autentimine töötab, ning tegema skripti hästi struktureerituks õige funktsioonide ja dokumentatsiooniga."

The Azure MCP Server will generate a complete, production-ready Python script that:
- Kasutab uusimat Azure Blob Storage SDK-d koos sobivate asünkroonsete mustritega
- Rakendab DefaultAzureCredential'i koos põhjaliku varuplaanide ahela selgitusega
- Sisaldab tugevat veakäsitlust konkreetsete Azure'i erinditüüpidega
- Järgib Azure SDK parimaid tavasid ressursside haldamiseks ja ühenduste käsitlemiseks
- Pakub detailset logimist ja informatiivset konsooliväljundit
- Loodab korrektselt struktureeritud skripti koos funktsioonide, dokumentatsiooni ja tüübiviidetega

Mis seda silmapaistvaks teeb, on see, et ilma Azure MCP-ta võiksite saada üldise blob-salvestuse koodi, mis küll töötab, kuid ei järgi praeguseid Azure'i mustreid. Azure MCP abil saate koodi, mis kasutab uusimaid autentimismeetodeid, käsitleb Azure-spetsiifilisi veistsenaariume ja järgib Microsofti soovitatud tavasid tootmisrakenduste jaoks.

**Esiletõstetud näide**: Mul on olnud raske meeles pidada konkreetseid käske `az` ja `azd` CLI-de jaoks ad-hoc kasutuseks. See on minu jaoks alati kaheastmeline protsess: esmalt vaatan süntaksi üles, siis käivitan käsu. Sageli suundun lihtsalt portaali ja klikiksin ringi, et töö tehtud saada, sest ma ei taha tunnistada, et ei mäleta CLI süntaksit. Võimalus lihtsalt kirjeldada, mida ma tahan, on hämmastav ning veelgi parem on seda teha ilma IDE-st lahkumata!

Alustamiseks on suurepärane nimekiri kasutusjuhtudest [Azure MCP hoidlas](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server). Põhjalike seadistusjuhiste ja täiustatud konfiguratsioonivalikute jaoks vaadake [ametlikku Azure MCP dokumentatsiooni](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Installi VS Code'i](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Installi VS Code Insiders'i](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Mida see teeb**: Ametlik GitHub MCP Server pakub sujuvat integreeritust kogu GitHubi ökosüsteemiga, pakkudes nii hostitud kaugjuurdepääsu kui ka kohalikku Docker-põhist juurutamise võimalust. See ei puuduta ainult põhilisi hoidla toiminguid – see on kõikehõlmav tööriistakomplekt, mis sisaldab GitHub Actions'i haldust, pull requesti töövooge, probleemide jälgimist, turvaskaneerimist, teavitusi ja täiustatud automaatikavõimekusi.

**Miks see kasulik on**: See server muudab teie suhtlemist GitHubiga, tuues kogu platvormikogemuse otse teie arenduskeskkonda. Selle asemel, et pidevalt vahetada VS Code'i ja GitHub.com-i vahel projektihalduse, koodiarvustuste ja CI/CD jälgimise jaoks, saate kõike teha loomuliku keele käskude abil, jäädes samal ajal oma koodi peale keskendunuks.

> **ℹ️ Märkus: Erinevat tüüpi 'agendid'**
> 
> Ärge segi ajage seda GitHub MCP Server'it GitHubi Coding Agendiga (AI-agent, kellele saate ülesandeid määrata automatiseeritud kodeerimistööde jaoks). GitHub MCP Server töötab VS Code'i Agent režiimis, et pakkuda GitHub API integratsiooni, samas kui GitHubi Coding Agent on eraldiseisev funktsioon, mis loob pull requeste, kui see määratakse GitHubi issue'idele.

**Peamised võimekused hõlmavad**:
- **⚙️ GitHub Actions**: Täielik CI/CD torujuhtme haldus, töövoogude jälgimine ja artefaktide käsitsemine
- **🔀 Pull Requests**: Loo, vaata üle, ühenda ja halda pull requeste laiaulatusliku oleku jälgimisega
- **🐛 Issues**: Täielik issue elutsükli haldus, kommenteerimine, sildistamine ja määramine
- **🔒 Turvalisus**: Koodiskaneerimise hoiatused, salajaste andmete tuvastamine ja Dependabot'i integratsioon
- **🔔 Teavitused**: Nutikas teavituste haldus ja hoidla tellimuste kontroll
- **📁 Repository Management**: Failitoimingud, harude haldus ja hoidla administraatorlus
- **👥 Koostöö**: Kasutaja ja organisatsiooni otsing, tiimide haldus ja juurdepääsu kontroll

**Reaalne kasutus**: "Loo pull request minu feature-harust", "Näita mulle kõik sel nädalal ebaõnnestunud CI jooksud", "Loetle minu hoidlate avatud turvahoiatused", või "Leia kõik mulle määratud issue'id kõigis minu organisatsioonides"

**Täielik demo stsenaarium**: Siin on võimas töövoog, mis demonstreerib GitHub MCP Serveri võimeid:

> "Pean valmistuma meie sprint-ülevaatuseks. Näita mulle kõik pull requestid, mida ma sellel nädalal loonud olen, kontrolli meie CI/CD torujuhtmete olekut, koosta kokkuvõte kõigist turvahoiatustest, millega peame tegelema, ja aita mul koostada väljalasete märkmeid, mis põhinevad 'feature' sildiga ühendatud PR-idel."

GitHub MCP Server teeb järgmist:
- Pärib teie hiljutised pull requestid koos detailse olekuinfoga
- Analüüsib töövoogude jooksusid ja toob esile kõik ebaõnnestumised või jõudlusprobleemid
- Koondab turvaskaneerimise tulemused ja prioriseerib kriitilised hoiatused
- Genereerib põhjalikud väljalasete märkmed, ekstraheerides infot ühendatud PR-idest
- Pakub praktilisi järgmisi samme sprindi planeerimiseks ja väljalasete ettevalmistamiseks

**Esiletõstetud näide**: Mulle meeldib seda kasutada koodiarvustuste töövoogude jaoks. Selle asemel, et hüpata VS Code'i, GitHubi teavituste ja pull requesti lehtede vahel, saan öelda "Näita mulle kõiki PR-e, mis ootavad minu ülevaatust" ja seejärel "Lisa kommentaar PR-ile #123, küsides autentimismeetodi veakäsitluse kohta." Server tegeleb GitHub API kutsungitega, hoiab vestluse konteksti ja aitab isegi koostada konstruktiivsemaid arvustuskommentaare.

**Autentimisvõimalused**: Server toetab nii OAuth-i (sujuv VS Code'is) kui ka isiklikke juurdepääsu tokeneid, koos konfigureeritavate tööriistakomplektidega, et lubada ainult vajalik GitHubi funktsionaalsus. Saate seda käivitada kas kaughostitud teenusena kiireks seadistuseks või kohapeal Dockeriga täieliku kontrolli saamiseks.

> **💡 Pro nõuanne**
> 
> Lubage ainult need tööriistakomplektid, mida vajate, konfigureerides oma MCP serveri seadetes parameetri `--toolsets`, et vähendada konteksti suurust ja parandada AI tööriistade valikut. Näiteks lisage `"--toolsets", "repos,issues,pull_requests,actions"` oma MCP konfiguratsiooni argumentidesse põhiarenduse töövoogude jaoks või kasutage `"--toolsets", "notifications, security"`, kui soovite peamiselt GitHubi jälgimisvõimekust.
### 4. 🔄 Azure DevOps MCP Server

[![Installi VS Code'i](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Installi VS Code Insiders'i](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Mida see teeb**: Ühendub Azure DevOps teenustega pakkudes põhjalikku projektihaldust, tööüksuste jälgimist, build-torujuhtme haldust ja hoidla toiminguid.

**Miks see kasulik on**: Meeskondade jaoks, kes kasutavad Azure DevOps'i oma peamise DevOps platvormina, eemaldab see MCP server pideva vahelehtede vahetamise teie arenduskeskkonna ja Azure DevOps veebiliidese vahel. Saate hallata tööüksusi, kontrollida build-olekuid, pärida hoidlatesid ja käsitleda projektijuhtimise ülesandeid otse oma AI assistendilt.

**Tegelik kasutus**: "Näita mulle kõiki aktiivseid tööüksusi praeguses sprintis WebApp projekti jaoks", "Loo bugiaruanne sisselogimisprobleemi kohta, mille just leidsin", või "Kontrolli meie build-torude olekut ja näita mulle viimaseid ebaõnnestumisi"

**Esiletõstetud näide**: Saate hõlpsasti kontrollida oma meeskonna praeguse sprindi olekut lihtsa päringuga nagu "Näita mulle kõiki aktiivseid tööüksusi praeguses sprintis WebApp projekti jaoks" või "Loo bugiaruanne sisselogimisprobleemi kohta, mille just leidsin" ilma oma arenduskeskkonnast lahkumata.

### 5. 📝 MarkItDown MCP Server

[![Installi VS Code'i](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Installi VS Code Insiders'i](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Mida see teeb**: MarkItDown on põhjalik dokumendi konverteerimise server, mis teisendab erinevad failivormingud kõrgekvaliteediliseks Markdowniks, optimeeritud LLM-ide tarbimiseks ja tekstianalüüsi töövoogudele.

**Miks see kasulik on**: Hädavajalik kaasaegsete dokumentatsioonitöövoogude jaoks! MarkItDown töötab suurepäraselt paljude failivormingutega ning säilitab olulise dokumendi struktuuri nagu pealkirjad, loendid, tabelid ja lingid. Erinevalt lihtsatest teksti väljavõtmise tööriistadest keskendub see semantilise tähenduse ja vormingu säilitamisele, mis on väärtuslik nii AI töötlemiseks kui ka inimeste loetavuseks.

**Toetatud failivormingud**:
- **Office-dokumendid**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Meediumifailid**: Pildid (koos EXIF-metaandmetega ja OCR-iga), heli (koos EXIF-metaandmetega ja kõne transkriptsiooniga)
- **Veebisisu**: HTML, RSS-vood, YouTube URL-id, Wikipedia leheküljed
- **Andmevormingud**: CSV, JSON, XML, ZIP-failid (sisu rekursiivselt töötleb)
- **Avaldamise vormingud**: EPub, Jupyter notebooks (.ipynb)
- **E-post**: Outlook sõnumid (.msg)
- **Täiustatud**: Azure Document Intelligence integratsioon täiendatud PDF-töötluseks

**Täiustatud võimekused**: MarkItDown toetab LLM-i juhitud pildikirjeldusi (kui on saadaval OpenAI klient), Azure Document Intelligence'i täiustatud PDF-töötluseks, heli transkriptsiooni kõnesisu jaoks ning plugin-süsteemi täiendavate failivormingute toetamiseks.

**Tegelik kasutus**: "Teisenda see PowerPoint esitlus Markdowniks meie dokumentatsioonisaidi jaoks", "Eemalda tekst sellest PDF-ist, säilitades korraliku pealkirjastruktuuri", või "Muuda see Exceli arvutustabel loetavaks tabelivorminguks"

**Esiletõstetud näide (parafraseeritud)**:
[MarkItDowni dokumentatsioon](https://github.com/microsoft/markitdown#why-markdown) selgitab
et Markdown säilitab dokumendi struktuuri minimaalse vorminduskuluga.
Keelemudelid toodavad sageli Markdowni, muutes selle kasulikuks ning tokenite kasutamise osas tõhusaks
vorminguks dokumenditöötluse töövoogude jaoks.

MarkItDown on tõesti hea dokumendi struktuuri säilitamisel, mis on AI töövoogude jaoks oluline. Näiteks PowerPoint esitluse teisendamisel säilitab see slaidide organisatsiooni õige pealkirjastusega, ekstraktib tabelid Markdown-tabelitena, lisab piltidele alternatiivteksti ning töötleb isegi esineja märkmeid. Joonised teisendatakse loetavateks andmetabeliteks ja tulemuseks olev Markdown säilitab algse esituse loogilise voolu. See teeb selle ideaalseks esitlussisu söömiseks AI-süsteemidesse või dokumentatsiooni loomiseks olemasolevatest slaididest.
### 6. 🗃️ SQL Server MCP Server

[![Installi VS Code'i](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Installi VS Code Insiders'i](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Mida see teeb**: Pakub vestlusliku ligipääsu SQL Server andmebaasidele (kohapeal, Azure SQL või Fabric)

**Miks see kasulik on**: Sarnane PostgreSQL serverile, kuid Microsoft SQL ökosüsteemi jaoks. Ühenduge lihtsa ühendusstringiga ja alustage päringute esitamist loomulikus keeles – enam ei ole vaja konteksti vahetada!

**Tegelik kasutus**: "Leia kõik tellimused, mida viimase 30 päeva jooksul ei ole täidetud" tõlgitakse sobivateks SQL-päringuteks ja tagastatakse vormindatud tulemused

**Esiletõstetud näide**: Kui olete oma andmebaasi ühenduse seadistanud, saate kohe alustada vestlusi oma andmetega. Blogipostitus demonstreerib seda lihtsa küsimusega: "millise andmebaasiga olete ühendatud?" MCP server vastab, kutsudes sobiva andmebaasitööriista, ühendub teie SQL Server instantsiga ja tagastab andmed teie praeguse andmebaasiühenduse kohta – kõik ilma ühegi SQL-rea kirjutamiseta. Server toetab põhjalikke andmebaasioperatsioone skeemi haldamisest kuni andmetöötluseni, kõik loomulike keelekäskude kaudu. Täielike seadistusjuhiste ja konfiguratsiooni näidete jaoks VS Code'i ja Claude Desktopiga vaadake: [Tutvustame MSSQL MCP Serverit (Eelvaade)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP Server

[![Installi VS Code'i](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Installi VS Code Insiders'i](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Mida see teeb**: Võimaldab AI agentidel suhelda veebilehtedega testimise ja automatiseerimise jaoks

> **ℹ️ Toetab GitHub Copilot'i**
> 
> Playwright MCP Server annab GitHub Copilot'i Coding Agendile võime sirvida veebilehti! [Lisateave selle funktsiooni kohta](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Miks see kasulik on**: Ideaalne automatiseeritud testimiseks, mida juhitakse loomulike keelekirjelduste abil. AI võib navigeerida veebisaitidel, täita vorme ja ekstraktida andmeid läbi struktureeritud ligipääsetavuse hetkepiltide – see on erakordselt võimas!

**Tegelik kasutus**: "Testi sisselogimisvoogu ja kinnita, et juhtpaneel laeb õigesti" või "Loo test, mis otsib tooteid ja valideerib tulemuste lehe" – kõik ilma rakenduse lähtekoodita

**Esiletõstetud näide**: Minu meeskonnakaaslane Debbie O'Brien on viimasel ajal teinud Playwright MCP Serveriga hämmastavat tööd! Näiteks näitas ta hiljuti, kuidas saab genereerida täielikke Playwright teste ilma, et oleks juurdepääsu rakenduse lähtekoodile. Oma stsenaariumis palus ta Copilotil luua test filmiotsingu rakenduse jaoks: navigeeri saidile, otsi "Garfield" ja kinnita, et film ilmub tulemustes. MCP käivitas brauseri seansi, uuris lehe struktuuri DOM-hetkepiltide abil, leidis õiged selektorid ja genereeris täielikult toimiva TypeScript testi, mis läbis esimese jooksu.

Mis teeb selle tõeliselt võimsaks, on see, et see ühendab loomuliku keele juhised ja täidetava testkoodi vahele jääva lõhe. Traditsioonilised lähenemised nõuavad kas manuaalset testikirjutamist või ligipääsu koodibaasile konteksti saamiseks. Kuid Playwright MCP abil saate testida väliseid saite, kliendirakendusi või töötada musta kasti testimise stsenaariumites, kus koodi ligipääs ei ole võimalik.


### 8. 💻 Dev Boxi MCP-server

[![Paigalda VS Code'i](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Paigalda VS Code Insidersi](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Mida see teeb**: Halda Microsoft Dev Boxi keskkondi loomuliku keele abil

**Miks see kasulik on**: Lihtsustab arenduskeskkondade haldamist tohutult! Loo, seadista ja halda arenduskeskkondi ilma konkreetseid käske meelde pidamata.

**Tõeline kasutus**: "Seadista uus Dev Box uusima .NET SDK-ga ja seadista see meie projekti jaoks", "Kontrolli kõigi minu arenduskeskkondade olekut", või "Loo standardiseeritud demo-keskkond meie meeskonna esitluste jaoks"

**Esiletõstetud näide**: Mulle väga meeldib Dev Box'i kasutada isiklikuks arenduseks. Minu valgustav hetk oli siis, kui James Montemagno selgitas, kui suurepärane on Dev Box konverentside demo jaoks, kuna seal on ülikiire Etherneti-ühendus olenemata konverentsi / hotelli / lennuki wifi-st, mida ma parasjagu kasutan. Tegelikult harjutasin hiljuti konverentsi demo, kui mu sülearvuti oli ühendatud telefonihotspotiga ja ma sõitsin bussiga Brugesist Antwerpi! Kuid minu järgmine samm on uurida rohkem meeskonna haldamist mitme arenduskeskkonnaga ja standardiseeritud demo-keskkondi. Ja veel üks suur kasutusjuhtum, mida olen klientidelt ja töökaaslastelt kuulnud, on muidugi Dev Box'i kasutamine eelkonfigureeritud arenduskeskkondade jaoks. Mõlemas olukorras võimaldab MCP Dev Boxide konfigureerimist ja haldamist loomuliku keele kaudu, jäädes samal ajal teie arenduskeskkonda.

### 9. 🤖 Microsoft Foundry MCP-server

[![Paigalda VS Code'i](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Paigalda VS Code Insidersi](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Mida see teeb**: Microsoft Foundry MCP-server annab arendajatele põhjaliku juurdepääsu Azure'i tehisintellekti ökosüsteemile, sealhulgas mudelikataloogidele, juurutuse haldusele, teadmiste indekseerimisele Azure AI Searchiga ja hindamise tööriistadele. See eksperimentaalne server ühendab AI arenduse Azure'i võimsa AI-taristuga, muutes AI-rakenduste loomise, juurutamise ja hindamise lihtsamaks.

**Miks see kasulik on**: See server muudab teie tööd Azure'i AI-teenustega, tuues ettevõtte-tasemel AI-võimekuse otse teie arendustöövoogu. Azure'i portaali, dokumentatsiooni ja IDE vahel ringi liikumise asemel saate loomuliku keele käskluste abil leida mudeleid, juurutada teenuseid, hallata teadmistebaase ja hinnata AI jõudlust. See on eriti võimas arendajatele, kes loovad RAG (Retrieval-Augmented Generation) rakendusi, haldavad mitme mudeli juurutusi või rakendavad põhjalikke AI-hindamise torustikke.

**Põhilised arendaja võimekused**:
- **🔍 Mudelite leidmine ja juurutamine**: Sirvige Microsoft Foundry mudelikataloogi, saage üksikasjalikku mudeliinfot koos koodinäidetega ja juurutage mudeleid Azure AI teenustesse
- **📚 Teadmiste haldamine**: Looge ja haldage Azure AI Search indekseid, lisage dokumente, seadistage indekseerijaid ja looge keerukaid RAG-süsteeme
- **⚡ AI-agendi integratsioon**: Ühenduge Azure AI agentidega, pärige olemasolevaid agente ja hinnake agentide jõudlust tootmiskeskkonna stsenaariumites
- **📊 Hindamisraamistik**: Käivitage põhjalikke teksti- ja agendi hindamisi, genereerige markdown-aruandeid ja rakendage kvaliteedikontrolli AI-rakendustele
- **🚀 Prototüüpimisvahendid**: Saage seadistussammud GitHub-põhiseks prototüüpimiseks ja pääsete ligi Microsoft Foundry Labsi tipptasemel uurimusmudelitele

**Tegeliku elu arendaja kasutus**: "Juurutage Phi-4 mudel Azure AI teenustesse minu rakenduse jaoks", "Looge uus otsinguindeks minu dokumentatsiooni RAG-süsteemi jaoks", "Hinnake minu agendi vastuseid kvaliteetmeetmete alusel", või "Leidke parim põhjendusmudel minu keerukate analüüsülesannete jaoks"

**Täielik demo stsenaarium**: Siin on võimas AI arendustöövoog:

> "Ehitan klienditoe agenti. Aita mul leida kataloogist hea põhjendusmudel, juurutada see Azure AI teenustesse, luua meie dokumentatsioonist teadmistebaas, seadistada hindamisraamistik vastuste kvaliteedi testimiseks ja seejärel aidata prototüüpida integratsiooni GitHubi tokeni abil testimiseks."

Microsoft Foundry MCP-server:
- Pärib mudelikataloogi, et soovitada teie nõuetele vastavaid optimaalseid põhjendusmudeleid
- Pakub juurutuskäske ja kvoodi teavet teie eelistatud Azure'i regiooni jaoks
- Seadistab Azure AI Search indeksid sobiva skeemiga teie dokumentatsiooni jaoks
- Konfigureerib hindamistorustikud kvaliteedimõõdikute ja turvakontrollidega
- Genereerib prototüübi koodi GitHubi autentimisega koheseks testimiseks
- Pakub põhjalikke seadistusjuhendeid, mis on kohandatud teie konkreetse tehnoloogiapinu jaoks

**Esiletõstetud näide**: Arendajana on mul olnud raske kursis püsida erinevate saadaolevate LLM-mudelitega. Ma tunnen mõningaid peamisi mudeleid, kuid mul on tunne, et ma jään ilma mõnest tootlikkuse ja efektiivsuse kasvust. Ja tokenid ning kvoodid on stressirohked ja keerulised hallata – ma ei tea kunagi, kas valin õige mudeli õige ülesande jaoks või kulutan ebaefektiivselt oma eelarvet. Kuulsin sellest MCP-serverist just James Montemagnolt, kui küsisin meeskonnakaaslastelt MCP-serveri soovitusi selle postituse jaoks, ja olen põnevil, et saan seda kasutada! Mudelite avastamise võimekused näivad eriti muljetavaldavad kellegi jaoks nagu mina, kes soovib uurida tavapärasest kaugemale ja leida ülesandele optimeeritud mudeleid. Hindamisraamistik peaks aitama mul kinnitada, et ma tõesti saan paremaid tulemusi, mitte lihtsalt proovida midagi uut selle pärast.

> **ℹ️ Eksperimentaalne staatus**
>
> See MCP-server on eksperimentaalne ja aktiivses arenduses. Funktsioonid ja API-d võivad muutuda. Sobib ideaalselt Azure'i AI võimekuse uurimiseks ja prototüüpide ehitamiseks, kuid tootmiskasutuseks vajaliku stabiilsuse nõudeid tuleks kinnitada.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP-server

[![Paigalda VS Code'i](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Paigalda VS Code Insidersi](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Mida see teeb**: Pakub arendajatele olulisi tööriistu AI-agentide ja rakenduste loomiseks, mis integreeruvad Microsoft 365 ja Microsoft 365 Copilotiga, sealhulgas skeemi valideerimist, näidiskoodi leidmist ning tõrkeotsingu abi.

**Miks see kasulik on**: Microsoft 365 ja Copilot jaoks arendamine hõlmab keerukaid manifestiskeeme ja spetsiifilisi arendusmustreid. See MCP-server toob olulised arendusressursid otse teie kodeerimiskeskkonda, aidates valideerida skeeme, leida näidiskoodi ja lahendada levinud probleeme ilma pidevalt dokumentatsiooni juurde pöördumata.

**Tegeliku elu kasutus**: "Valideeri minu deklaratiivse agendi manifest ja paranda kõik skeemivead", "Näita mulle näidiskoodi Microsoft Graph API pistikprogrammi rakendamiseks", või "Aita mul tõrkeotsingus Teamsi rakenduse autentimisprobleeme lahendada"

**Esiletõstetud näide**: Võtsin ühendust oma sõbra John Milleriga pärast Buildi konverentsil M365 Agentidest rääkimist ja ta soovitas seda MCP-d. See võib olla suurepärane uutele M365 Agente kasutavatele arendajatele, kuna see pakub malle, näidiskoodi ja lähteplokke, et alustada ilma dokumentatsioonis uppumata. Skeemi valideerimise funktsioonid tunduvad eriti kasulikud manifestistruktuuri vigade vältimiseks, mis võivad põhjustada tunde kestvaid silumisprotsesse.

> **💡 Näpunäide**
>
> Kasuta seda serverit koos Microsoft Learn Docs MCP-serveriga põhjalikuks M365 arenduse toeks – üks pakub ametlikku dokumentatsiooni, teine aga praktilisi arendusvahendeid ja tõrkeotsingu abi.


## Mis järgmisena? 🔮

## 📋 Kokkuvõte

Model Context Protocol (MCP) muudab seda, kuidas arendajad suhtlevad tehisintellekti abistajate ja väliste tööriistadega. Need 10 Microsofti MCP-serverit demonstreerivad standardiseeritud AI-integratsiooni jõudu, võimaldades sujuvaid töövooge, mis hoiavad arendajad vooguses, võimaldades samal ajal juurdepääsu võimsatele välistele võimekustele.

Alates põhjalikust Azure'i ökosüsteemi integratsioonist kuni spetsialiseeritud tööriistadeni nagu Playwright brauseri automatiseerimiseks ja MarkItDown dokumentide töötlemiseks, näitavad need serverid, kuidas MCP saab parandada tootlikkust erinevates arendusstsenaariumides. Standardiseeritud protokoll tagab, et need tööriistad töötavad üheskoos sujuvalt, luues ühtse arenduskogemuse.

Kuna MCP-ökosüsteem jätkab arengut, on kogukonnaga suhtlemine, uute serverite uurimine ja kohandatud lahenduste loomine võtmetähtsusega teie arendusproduktiivsuse maksimeerimiseks. MCP avatud standard tähendab, et saate eri tarnijate tööriistu segada ja sobitada, et luua oma konkreetsetele vajadustele parim töövoog.

## 🔗 Täiendavad ressursid

- [Ametlik Microsofti MCP-hoidla](https://github.com/microsoft/mcp)
- [MCP kogukond ja dokumentatsioon](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentatsioon](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentatsioon](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentatsioon](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Õpime – MCP üritused](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Suurepärased GitHub Copilot kohandused](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days otse 29./30. juulil või vaata nõudmisel ](https://aka.ms/mcpdevdays)

## 🎯 Harjutused

1. **Paigalda ja seadista**: Sea üles üks MCP-serveritest oma VS Code keskkonnas ja testi põhilist funktsionaalsust.
2. **Töövoo integratsioon**: Kujunda arenduse töövoog, mis ühendab vähemalt kolme erinevat MCP-serverit.
3. **Kohandatud serveri planeerimine**: Tuvasta ülesanne oma igapäevases arendusprotsessis, mis võiks kasu saada kohandatud MCP-serverist, ja loo selle jaoks spetsifikatsioon.
4. **Jõudluse analüüs**: Võrdle MCP-serverite kasutamise tõhusust võrreldes traditsiooniliste lähenemistega levinud arendusülesannete puhul.
5. **Turbehindamine**: Hinda MCP-serverite kasutamise turvariske oma arenduskeskkonnas ja paku parimaid tavasid.


Next:[Parimad tavad](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->