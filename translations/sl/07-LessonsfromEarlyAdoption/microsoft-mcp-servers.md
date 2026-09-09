# 🚀 10 Microsoft MCP strežnikov, ki spreminjajo produktivnost razvijalcev

## 🎯 Kaj se boste naučili v tem vodiču

Ta praktičen vodič predstavlja deset Microsoft MCP strežnikov, ki aktivno spreminjajo način dela razvijalcev z AI asistenti. Namesto da bi le razlagali, kaj MCP strežniki *lahko* naredijo, vam bomo pokazali strežnike, ki že dejansko vplivajo na vsakodnevne razvojne delovne tokove v Microsoftu in drugod.

Vsak strežnik v tem vodiču je bil izbran na podlagi dejanske uporabe in povratnih informacij razvijalcev. Spoznali boste ne le, kaj vsak strežnik počne, temveč tudi, zakaj je pomemben in kako ga najbolje izkoristiti pri svojih projektih. Ne glede na to, ali ste popoln začetnik pri MCP ali želite razširiti svojo obstoječo nastavitve, ti strežniki predstavljajo nekatere najbolj praktične in vplivne orodja v Microsoftovem ekosistemu.

> **💡 Nasvet za hiter začetek**
> 
> Ste novi pri MCP? Brez skrbi! Ta vodič je zasnovan tako, da je prijazen do začetnikov. Koncepte bomo razložili sproti, vedno pa se lahko vrnete k našima moduloma [Uvod v MCP](../00-Introduction/README.md) in [Osnovni koncepti](../01-CoreConcepts/README.md) za poglobljeno ozadje.

## Pregled

Ta celovit vodič raziskuje deset Microsoft MCP strežnikov, ki revolucionarno spreminjajo način, kako razvijalci sodelujejo z AI asistenti in zunanjimi orodji. Od upravljanja virov Azure do obdelave dokumentov ti strežniki prikazujejo moč protokola Model Context za ustvarjanje nemotenih in produktivnih razvojnih delovnih tokov.

## Cilji učenja

Do konca tega vodiča boste:
- Razumeli, kako MCP strežniki izboljšujejo produktivnost razvijalcev
- Spoznali najbolj vplivne implementacije MCP strežnikov pri Microsoftu
- Odkrijte praktične primere uporabe vsakega strežnika
- Znali nastaviti in konfigurirati te strežnike v VS Code in Visual Studio
- Raziskali širši ekosistem MCP in prihodnje smernice

## 🔧 Razumevanje MCP strežnikov: Vodič za začetnike

### Kaj so MCP strežniki?

Kot začetnik v protokolu Model Context Protocol (MCP) se morda sprašujete: "Kaj pravzaprav je MCP strežnik in zakaj bi me to moralo zanimati?" Začnimo s preprosto analogijo.

Pomislite na MCP strežnike kot specializirane asistente, ki pomagajo vašemu AI kodirnemu spremljevalcu (kot je GitHub Copilot) povezati se z zunanjimi orodji in storitvami. Tako kot uporabljate različne aplikacije na telefonu za različna opravila – eno za vremensko napoved, eno za navigacijo, eno za bančništvo – MCP strežniki dajejo vašemu AI asistentu zmožnost interakcije z različnimi razvojnimi orodji in storitvami.

### Problem, ki ga MCP Strežniki rešujejo

Preden so bili MCP strežniki, če ste želeli:
- Preveriti svoje vire v Azure
- Ustvariti GitHub zadevo
- Poizvedovati v podatkovni bazi
- Iskati v dokumentaciji

Ste morali prenehati s kodiranjem, odpreti brskalnik, iti na ustrezno spletno stran in ročno opraviti te naloge. Ta stalno preklapljanje konteksta prekine vaš tok dela in zmanjša produktivnost.

### Kako MCP strežniki spremenijo vašo razvojno izkušnjo

Z MCP strežniki lahko ostanete v svojem razvojnem okolju (VS Code, Visual Studio itd.) in preprosto prosite AI asistenta, naj opravi te naloge. Na primer:

**Namesto tega tradicionalnega delovnega toka:**
1. Prenehajte s kodiranjem
2. Odprite brskalnik
3. Pojdite na Azure portal
4. Poiščite podrobnosti o računu za shranjevanje
5. Vrnite se v VS Code
6. Nadaljujte s kodiranjem

**Zdaj lahko naredite to:**
1. Vprašajte AI: "Kakšen je status mojih Azure računov za shranjevanje?"
2. Nadaljujte s kodiranjem z pridobljenimi informacijami

### Ključne koristi za začetnike

#### 1. 🔄 **Ostanite v svojem toku**
- Ne preklapljajte več med različnimi aplikacijami
- Osredotočite se na kodo, ki jo pišete
- Zmanjšajte mentalno obremenitev upravljanja različnih orodij

#### 2. 🤖 **Uporabljajte naravni jezik namesto zapletenih ukazov**
- Namesto pomnjenja SQL sintakse opišite, katere podatke potrebujete
- Namesto pomnjenja ukazov Azure CLI razložite, kaj želite doseči
- Pustite, da AI uredi tehnične podrobnosti, vi pa se osredotočite na logiko

#### 3. 🔗 **Povežite več orodij skupaj**
- Ustvarite močne delovne tokove z združevanjem različnih storitev
- Primer: "Pridobi vse nedavne GitHub zadeve in ustvari ustrezne delovne elemente v Azure DevOps"
- Ustvarite avtomatizacijo brez pisanja zapletenih skript

#### 4. 🌐 **Dostop do rastočega ekosistema**
- Izkoristite strežnike, ki jih ustvarjajo Microsoft, GitHub in druge družbe
- Brez težav kombinirajte orodja različnih ponudnikov
- Pridružite se standardiziranemu ekosistemu, ki deluje z različnimi AI asistenti

#### 5. 🛠️ **Učite se z delom**
- Začnite s predhodno izdelanimi strežniki, da razumete koncepte
- Postopoma izdelajte svoje lastne strežnike, ko boste bolj udobni
- Uporabite razpoložljive SDK-je in dokumentacijo za vodilo učenja

### Primer iz resničnega sveta za začetnike

Recimo, da ste novi v spletni razvoj in delate na svojem prvem projektu. Tako vam lahko MCP strežniki pomagajo:

**Tradicionalni pristop:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**S MCP strežniki:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Prednost standarda za podjetja

MCP postaja industrijski standard, kar pomeni:
- **Doslednost**: Podobna izkušnja med različnimi orodji in družbami
- **Medsebojna združljivost**: Strežniki različnih ponudnikov medsebojno delujejo
- **Pripravljenost za prihodnost**: Spretnosti in nastavitve se prenašajo med različnimi AI asistenti
- **Skupnost**: Velik ekosistem deljenih znanj in virov

### Začetek: Kaj se boste naučili

V tem vodiču bomo raziskali 10 Microsoft MCP strežnikov, ki so še posebej koristni za razvijalce na vseh ravneh. Vsak strežnik je zasnovan, da:
- Reši pogoste razvojne izzive
- Zmanjša ponavljajoča se opravila
- Izboljša kakovost kode
- Izboljša priložnosti za učenje

> **💡 Nasvet za učenje**
> 
> Če ste popolnoma novi pri MCP, najprej začnite z našima moduloma [Uvod v MCP](../00-Introduction/README.md) in [Osnovni koncepti](../01-CoreConcepts/README.md). Nato se vrnite sem, da si ogledate te koncepte v praksi z realnimi Microsoftovimi orodji.
>
> Za dodatni kontekst o pomenu MCP si oglejte zapis Marije Naggaga: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Začetek z MCP v VS Code in Visual Studio 🚀

Nastavitev teh MCP strežnikov je enostavna, če uporabljate Visual Studio Code ali Visual Studio 2022 z GitHub Copilot.

### Nastavitev VS Code

Tukaj je osnovni postopek za VS Code:

1. **Omogočite način agenta**: V VS Code preklopite na način agenta v oknu Copilot Chat
2. **Konfigurirajte MCP strežnike**: Dodajte konfiguracije strežnikov v vašo datoteko settings.json
3. **Zaženi strežnike**: Kliknite gumb "Start" za vsak strežnik, ki ga želite uporabiti
4. **Izberite orodja**: Izberite, katere MCP strežnike želite omogočiti za svojo trenutno sejo

Za podrobna navodila za nastavitev si oglejte [dokumentacijo VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Strokovni nasvet: Upravljajte MCP strežnike kot profesionalec!**
> 
> Pogled razširitev VS Code zdaj vključuje [praktičen nov vmesnik za upravljanje nameščenih MCP strežnikov](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Hitro dostopate do zagona, zaustavitve in upravljanja vseh nameščenih MCP strežnikov z jasnim in preprostim vmesnikom. Preizkusite!

### Nastavitev Visual Studio 2022

Za Visual Studio 2022 (verzija 17.14 ali novejša):

1. **Omogočite način agenta**: Kliknite spustni meni "Ask" v oknu GitHub Copilot Chat in izberite "Agent"
2. **Ustvarite konfiguracijsko datoteko**: Ustvarite `.mcp.json` datoteko v imeniku rešitve (priporočena lokacija: `<SOLUTIONDIR>\.mcp.json`)
3. **Konfigurirajte strežnike**: Dodajte konfiguracije MCP strežnikov z uporabo standardnega MCP formata
4. **Odobritev orodij**: Ko ste pozvani, odobrite orodja, ki jih želite uporabljati z ustreznimi dovoljenji območij

Za podrobna navodila za nastavitev Visual Studia si oglejte [dokumentacijo Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Vsak MCP strežnik ima svoje zahteve glede konfiguracije (povezovalni nizi, avtentikacija itd.), vendar je vzorec nastavitve konzistenten v obeh IDE-jih.

## Lekcija iz Microsoft MCP strežnikov 🛠️

### 1. 📚 Microsoft Learn Docs MCP strežnik

[![Namesti v VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Namesti v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Kaj počne**: Microsoft Learn Docs MCP strežnik je oblačna storitev, ki AI asistentom omogoča dostop v realnem času do uradne Microsoftove dokumentacije preko protokola Model Context. Povezuje se na `https://learn.microsoft.com/api/mcp` in omogoča semantično iskanje po Microsoft Learn, Azure dokumentaciji, Microsoft 365 dokumentaciji in drugih uradnih Microsoftovih virih.

**Zakaj je uporaben**: Čeprav se morda zdi "le dokumentacija", je ta strežnik dejansko ključnega pomena za vsakega razvijalca, ki uporablja Microsoftove tehnologije. Ena največjih pritožb razvijalcev .NET glede AI kodirnih asistentov je, da niso na tekočem z zadnjimi izdajami .NET-a in C#. Microsoft Learn Docs MCP strežnik to rešuje z zagotavljanjem dostopa v realnem času do najnovejše dokumentacije, API referenc in najboljših praks. Ne glede na to, ali delate z najnovejšimi Azure SDK-ji, raziskujete nove funkcije C# 13 ali uporabljate napredne Aspire vzorce, ta strežnik zagotavlja, da ima vaš AI asistent dostop do avtoritativnih, posodobljenih informacij, potrebnih za generiranje točne, sodobne kode.

**Resnična uporaba**: "Kateri az cli ukazi ustvarijo Azure container app po uradni Microsoft Learn dokumentaciji?" ali "Kako konfiguriram Entity Framework z odvisnostnim vbrizganjem v ASP.NET Core?" Ali kako pa "Preglej ta kodo, da se prepričamo, da ustreza priporočilom za zmogljivost v Microsoft Learn dokumentaciji." Strežnik zagotavlja obsežno pokritost po Microsoft Learn, Azure dokumentih in Microsoft 365 dokumentaciji z uporabo naprednega semantičnega iskanja za iskanje najbolj kontekstualno relevantnih informacij. Vrača do 10 kakovostnih vsebinskih kosov z naslovi člankov in URL-ji, vedno dostopajoč do najnovejše Microsoftove dokumentacije takoj, ko je objavljena.

**Izpostavljen primer**: Strežnik izpostavlja orodje `microsoft_docs_search`, ki izvaja semantično iskanje po uradni Microsoftovi tehnični dokumentaciji. Ko je konfigurirano, lahko postavite vprašanja, kot je "Kako implementiram JWT avtentikacijo v ASP.NET Core?" in dobite podrobne, uradne odgovore z viri povezav. Kakovost iskanja je izjemna, ker razume kontekst – vprašanje o "kontejnerjih" v kontekstu Azure bo vrnilo dokumentacijo Azure Container Instances, medtem ko isti izraz v .NET kontekstu vrne relevantne informacije o C# zbirkah.

To je posebej uporabno za hitro spreminjajoče se ali nedavno posodobljene knjižnice in primere uporabe. Na primer, v nekaterih nedavnih kodirnih projektih sem želel izkoristiti funkcije v najnovejših izdajah Aspire in Microsoft.Extensions.AI. Z vključitvijo Microsoft Learn Docs MCP strežnika sem lahko izkoristil ne le API dokumentacijo, ampak tudi predstavitve in vodnike, ki so bili pravkar objavljeni.

> **💡 Strokovni nasvet**
> 
> Tudi modelom, prijaznim do orodij, je treba dati spodbudo za uporabo MCP orodij! Razmislite o dodajanju sistemskega poziva ali [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot), kot je: "Imate dostop do `microsoft.docs.mcp` – uporabite to orodje za iskanje v najnovejši uradni Microsoftovi dokumentaciji pri odgovarjanju na vprašanja o Microsoftovih tehnologijah, kot so C#, Azure, ASP.NET Core ali Entity Framework."
>
> Za odličen primer tega v praksi, si oglejte [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) iz Awesome GitHub Copilot repozitorija. Ta način posebej izkorišča Microsoft Learn Docs MCP strežnik za pomoč pri čiščenju in modernizaciji C# kode z uporabo najnovejših vzorcev in najboljših praks.
### 2. ☁️ Azure MCP strežnik


[![Namestitev v VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Namestitev v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Kaj počne**: Azure MCP strežnik je obsežen paket več kot 15 specializiranih povezovalnikov za Azure storitve, ki prinaša celoten Azure ekosistem v vaš AI delovni proces. To ni samo en strežnik – gre za zmogljiv nabor, ki vključuje upravljanje virov, povezljivost z bazami podatkov (PostgreSQL, SQL Server), analizo dnevnikov Azure Monitor z uporabo KQL, integracijo Cosmos DB in še veliko več.

**Zakaj je uporaben**: Poleg upravljanja Azure virov ta strežnik bistveno izboljša kakovost kode pri delu z Azure SDK-ji. Ko uporabljate Azure MCP v Agent načinu, vam ne pomaga samo pisati kodo – pomaga vam pisati *boljšo* Azure kodo, ki upošteva sodobne načine avtentikacije, najboljše prakse obvladovanja napak in izkorišča najnovejše funkcije SDK-jev. Namesto generične kode, ki morda deluje, dobite kodo, ki sledi priporočilom Azure za produkcijska opravila.

**Ključni moduli vključujejo**:
- **🗄️ Povezovalniki za baze podatkov**: Neposreden dostop z naravnim jezikom do Azure Database za PostgreSQL in SQL Server
- **📊 Azure Monitor**: Analiza dnevnikov in operativni vpogledi na osnovi KQL
- **🌐 Upravljanje virov**: Popolno upravljanje življenjskega cikla Azure virov
- **🔐 Avtentikacija**: DefaultAzureCredential in vzorci upravljanih identitet
- **📦 Storage storitve**: Operacije z Blob Storage, Queue Storage in Table Storage
- **🚀 Storitve kontejnerjev**: Upravljanje Azure Container Apps, Container Instances in AKS
- **In še mnogo več specializiranih povezovalnikov**

**Uporaba v praksi**: "Naštej moje Azure račune za shranjevanje", "Poizvedi mojo Log Analytics delovno okolje za napake v zadnji uri" ali "Pomoč pri izdelavi Azure aplikacije z Node.js z ustrezno avtentikacijo"

**Celoten demo scenarij**: Tukaj je popolna predstavitev, ki pokaže moč združitve Azure MCP s GitHub Copilot za Azure razširitev v VS Code. Ko oba imata nameščena in vnesete:

> "Ustvari Python skripto, ki naloži datoteko v Azure Blob Storage z uporabo avtentikacije DefaultAzureCredential. Skripta naj se poveže z mojim Azure računom za shranjevanje z imenom 'mycompanystorage', naloži v kontejner z imenom 'documents', ustvari testno datoteko s trenutnim časovnim žigom za nalaganje, obravnava napake na prijazen način in zagotavlja informativen izpis, sledi najboljšim praksam Azure za avtentikacijo in obvladovanje napak, vključuje komentarje, ki razlagajo, kako deluje avtentikacija DefaultAzureCredential, in naredi skripto dobro strukturirano z ustreznimi funkcijami in dokumentacijo."

Azure MCP strežnik bo ustvaril popolno, produkcijsko pripravljeno Python skripto, ki:
- Uporablja najnovejši Azure Blob Storage SDK z ustreznimi asinhronimi vzorci
- Izvaja DefaultAzureCredential z obsežno razlago verige zasilnih možnosti
- Vključuje robustno obvladovanje napak s specifičnimi tipi Azure izjem
- Sledi najboljšim praksam Azure SDK za upravljanje virov in povezav
- Zagotavlja podrobno beleženje in informativen konzolni izpis
- Ustvari pravilno strukturirano skripto s funkcijami, dokumentacijo in tipnimi namigi

Izjemno je, da brez Azure MCP dobite generično kodo za blob storage, ki deluje, vendar ne upošteva aktualnih Azure vzorcev. Z Azure MCP dobite kodo, ki uporablja najnovejše metode avtentikacije, obravnava Azure-specifične scenarije napak in sledi Microsoftovim priporočilom za produkcijske aplikacije.

**Izpostavljen primer**: Težko sem si zapomnil specifične ukaze za `az` in `azd` CLI-je za ad-hoc uporabo. Vedno je dvostopenjski postopek: najprej preverim sintakso, potem zaženem ukaz. Pogosto sem se preprosto prijavil v portal in kliknil okoli, da opravim delo, ker nisem hotel priznati, da ne znam sintakse CLI-ja. Sposobnost samo opisati, kar želim, je neverjetna, še boljše pa je, da to naredim brez zapuščanja IDE!

Odličen seznam primerov uporabe najdete v [Azure MCP repozitoriju](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) za začetek. Za celovite vodiče za nastavitev in napredne možnosti konfiguracije preverite [uradno Azure MCP dokumentacijo](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP strežnik

[![Namestitev v VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Namestitev v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Kaj počne**: Uradni GitHub MCP strežnik omogoča neprekinjeno integracijo z celotnim GitHub ekosistemom, ponuja možnosti gostovanega oddaljenega dostopa in lokalnega zagona preko Dockerja. To ni zgolj osnovno upravljanje repozitorijev – gre za celovit nabor orodij, ki vključuje upravljanje GitHub Actions, tokove dela pull requestov, sledenje težavam, varnostno skeniranje, obvestila in napredne zmogljivosti avtomatizacije.

**Zakaj je uporaben**: Ta strežnik spremeni način, kako sodelujete z GitHubom, tako da celotno platformo pripelje neposredno v vaše razvojno okolje. Namesto nenehnega preklapljanja med VS Code in GitHub.com za upravljanje projektov, preglede kode in spremljanje CI/CD lahko vse uredite z naravnimi jezikovnimi ukazi, medtem ko ostanete osredotočeni na svojo kodo.

> **ℹ️ Opomba: Različne vrste 'agentov'**
> 
> Ne zamenjujte tega GitHub MCP strežnika z GitHub Coding Agentom (AI agent, kateremu lahko dajete težave za avtomatizirane naloge kodiranja). GitHub MCP strežnik deluje znotraj VS Code Agent načina za zagotavljanje integracije z GitHub API-jem, medtem ko je GitHub Coding Agent ločena funkcija, ki ustvarja pull requeste ob dodelitvi GitHub težavam.

**Ključne zmožnosti vključujejo**:
- **⚙️ GitHub Actions**: Popolno upravljanje CI/CD cevovodov, spremljanje potekov dela in upravljanje artefaktov
- **🔀 Pull requesti**: Ustvarjanje, pregledovanje, združevanje in upravljanje PR-jev z obsežnim sledenjem stanja
- **🐛 Težave**: Celoten življenjski cikel težav, komentiranje, označevanje in dodeljevanje
- **🔒 Varnost**: Opozorila pri skeniranju kode, zaznavanje skrivnosti in integracija Dependabot
- **🔔 Obvestila**: Pametno upravljanje obvestil in kontrola naročnine na repozitorije
- **📁 Upravljanje repozitorijev**: Operacije z datotekami, upravljanje vej in administracija repozitorijev
- **👥 Sodelovanje**: Iskanje uporabnikov in organizacij, upravljanje ekip in nadzor dostopa

**Uporaba v praksi**: "Ustvari pull request iz moje feature veje", "Pokaži mi vse neuspešne CI zagonne teste ta teden", "Naštej odprta varnostna opozorila za moje repozitorije" ali "Najdi vse težave dodeljene meni po vseh mojih organizacijah"

**Celoten demo scenarij**: Tukaj je zmogljiv delovni tok, ki prikazuje zmožnosti GitHub MCP strežnika:

> "Moram se pripraviti na naš sprint pregled. Pokaži mi vse pull requeste, ki sem jih ustvaril ta teden, preveri stanje naših CI/CD cevovodov, ustvari povzetek vseh varnostnih opozoril, ki jih moramo rešiti, in pomagaj pripraviti izpise za izdajo na podlagi združenih PR-jev z oznako 'feature'."

GitHub MCP strežnik bo:
- Poizvedoval o tvojih nedavnih pull requestih z podrobnimi informacijami o stanju
- Analiziral poteke dela in izpostavil vse napake ali težave s hitrostjo
- Pripravil rezultate skeniranja varnosti in prednostno uredil kritična opozorila
- Ustvarjal obsežne izpiske za izdaje z izvlečki iz združenih PR-jev
- Zagotovil izvedljive naslednje korake za načrtovanje sprinta in pripravo izdaj

**Izpostavljen primer**: Rad uporabljam to za delovne tokove pregleda kode. Namesto preskakovanja med VS Code, GitHub obvestili in stranmi pull requestov lahko rečem "Pokaži mi vse PR-je, ki čakajo na moj pregled" in nato "Dodaj komentar k PR #123 glede obravnave napak v metodi avtentikacije." Strežnik upravlja klice GitHub API-ja, ohranja kontekst razprave in celo pomaga oblikovati bolj konstruktivne komentarje za pregled.

**Možnosti avtentikacije**: Strežnik podpira tako OAuth (brezhibno v VS Code) kot tudi osebne dostopne žetone, z nastavljivimi orodnimi paketi za omogočanje samo potrebnih GitHub funkcionalnosti. Lahko ga poganjate kot gostovano oddaljeno storitev za takojšnjo nastavitev ali lokalno preko Dockerja za popoln nadzor.

> **💡 Profesionalni nasvet**
> 
> Omogočite samo tiste orodne pakete, ki jih potrebujete, tako da konfigurirate parameter `--toolsets` v nastavitvah MCP strežnika, da zmanjšate velikost konteksta in izboljšate izbiro AI orodij. Na primer, dodajte `"--toolsets", "repos,issues,pull_requests,actions"` v argumente konfiguracije MCP za osnovne razvojne delovne tokove ali uporabite `"--toolsets", "notifications, security"`, če želite predvsem zmogljivosti spremljanja GitHub.
### 4. 🔄 Azure DevOps MCP strežnik

[![Namestitev v VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Namestitev v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Kaj počne**: Povezuje se z Azure DevOps storitvami za celovito upravljanje projektov, sledenje delovnim elementom, upravljanje cevovodov za gradnjo in upravljanje repozitorijev.

**Zakaj je uporaben**: Za ekipe, ki uporabljajo Azure DevOps kot svojo glavno DevOps platformo, ta MCP strežnik odpravi nenehno preklapljanje med razvojnim okoljem in spletnim vmesnikom Azure DevOps. Iz AI pomočnika lahko upravljate delovne elemente, preverjate stanje gradnje, poizvedujete repozitorije in urejate naloge upravljanja projektov.

**Uporaba v praksi**: "Pokaži mi vse aktivne delovne elemente v trenutnem sprintu za projekt WebApp", "Ustvari poročilo o napaki za težavo z prijavo, ki sem jo pravkar odkril", ali "Preveri stanje naših gradbenih cevovodov in pokaži vse nedavne napake"

**Izpostavljen primer**: Zlahka lahko preverite stanje trenutnega sprinta vaše ekipe z enostavno poizvedbo, kot je "Pokaži mi vse aktivne delovne elemente v trenutnem sprintu za projekt WebApp" ali "Ustvari poročilo o napaki za težavo z prijavo, ki sem jo pravkar odkril" brez zapuščanja razvojnega okolja.

### 5. 📝 MarkItDown MCP strežnik


[![Namesti v VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Namesti v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Kaj počne**: MarkItDown je celovit strežnik za pretvorbo dokumentov, ki spreminja različne formate datotek v visokokakovostni Markdown, optimiziran za potrošnjo LLM in delovne procese analize besedila.

**Zakaj je uporaben**: Nujno orodje za sodobne delovne procese dokumentacije! MarkItDown podpira impresiven nabor formatov datotek, hkrati pa ohranja ključno strukturo dokumenta, kot so naslovi, seznami, tabele in povezave. Za razliko od preprostih orodij za ekstrakcijo besedila se osredotoča na ohranjanje semantičnega pomena in oblikovanja, ki je dragoceno tako za AI obdelavo kot za človeško berljivost.

**Podprti formati datotek**:
- **Pisarnaški dokumenti**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Medijski datoteki**: Slike (z EXIF metapodatki in OCR), Zvok (z EXIF metapodatki in govorjeno transkripcijo)
- **Spletna vsebina**: HTML, RSS viri, YouTube URL-ji, Wikipedia strani
- **Podatkovni formati**: CSV, JSON, XML, ZIP datoteke (rekurzivno obdela vsebine)
- **Publish formati**: EPub, Jupyter zapiski (.ipynb)
- **E-pošta**: Outlook sporočila (.msg)
- **Napredne funkcije**: Azure Document Intelligence integracija za izboljšano obdelavo PDF-jev

**Napredne zmogljivosti**: MarkItDown podpira opise slik, ki jih poganja LLM (če je na voljo OpenAI odjemalec), Azure Document Intelligence za izboljšano obdelavo PDF, transkripcijo zvoka za govorjeno vsebino in sistem vtičnikov za razširitev na dodatne formate datotek.

**Praktična uporaba**: "Pretvori to PowerPoint predstavitev v Markdown za našo dokumentacijsko spletno stran", "Izvleci besedilo iz tega PDF-ja z ustrezno strukturo naslovov" ali "Pretvori to Excel preglednico v berljivo tabelo"

**Izstopajoč primer**: Za citat iz [MarkItDown dokumentacije](https://github.com/microsoft/markitdown#why-markdown):

> Markdown je zelo podoben navadnemu besedilu, z minimalno oznako ali oblikovanjem, vendar še vedno nudi način za predstavitev pomembne strukture dokumenta. Glavni LLM-ji, kot je OpenAI GPT-4o, izvorno "govorijo" Markdown in pogosto nepozvano vključujejo Markdown v svoje odgovore. To nakazuje, da so bili usposobljeni na velikih količinah besedil v Markdown obliki in ga dobro razumejo. Kot stranski učinek so tudi Markdown konvencije zelo token-učinkovite.

MarkItDown je res dober v ohranjanju strukture dokumentov, kar je pomembno za AI delovne procese. Na primer, pri pretvorbi PowerPoint predstavitve ohrani organizacijo diapozitivov s pravimi naslovi, izvleče tabele kot Markdown tabele, vključuje alt besedilo za slike in obdeluje tudi zvočne zapiske govornika. Grafikoni se pretvorijo v berljive podatkovne tabele, končni Markdown pa ohranja logični tok prvotne predstavitve. To je popolno za hranjenje predstavitvene vsebine v AI sisteme ali ustvarjanje dokumentacije iz obstoječih diapozitivov.
### 6. 🗃️ SQL Server MCP strežnik

[![Namesti v VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Namesti v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Kaj počne**: Omogoča pogovorni dostop do SQL Server baz podatkov (lokalno, Azure SQL ali Fabric)

**Zakaj je uporaben**: Podobno kot PostgreSQL strežnik, vendar za Microsoft SQL ekosistem. Povezava preko preproste povezovalne vrstice in zagon poizvedb v naravnem jeziku – brez preklapljanja konteksta!

**Praktična uporaba**: "Poišči vsa naročila, ki niso bila izpolnjena v zadnjih 30 dneh" se prevede v ustrezne SQL poizvedbe in vrne oblikovane rezultate

**Izstopajoč primer**: Ko nastavite povezavo do baze, lahko takoj začnete pogovore s svojimi podatki. Blog objava to prikaže z enostavnim vprašanjem: "Na katero bazo ste povezani?" MCP strežnik odgovori z uporabo ustreznega orodja za bazo, poveže se na vašo SQL Server instanco in vrne podrobnosti o trenutni povezavi z bazo – vse brez pisanja ene same vrstice SQL. Strežnik podpira celovite operacije nad bazo od upravljanja shem do manipulacije podatkov, vse preko naravnih jezikovnih ukazov. Za popolna navodila za nastavitev in primere konfiguracije z VS Code in Claude Desktop glejte: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP strežnik

[![Namesti v VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Namesti v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Kaj počne**: Omogoča AI agentom interakcijo s spletnimi stranmi za testiranje in avtomatizacijo

> **ℹ️ Poganja GitHub Copilot**
> 
> Playwright MCP strežnik poganja GitHub Copilot Coding Agenta, ki dobi zmožnost brskanja po spletu! [Več o tej funkciji](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Zakaj je uporaben**: Popolno za avtomatizirano testiranje, ki temelji na opisih v naravnem jeziku. AI lahko krmili spletne strani, izpolnjuje obrazce in izvleče podatke preko strukturiranih posnetkov dostopnosti – to je izjemno močno!

**Praktična uporaba**: "Testiraj prijavni potek in preveri, da se nadzorna plošča nalaga pravilno" ali "Ustvari test, ki išče izdelke in preveri stran z rezultati" – vse brez potrebe po izvorni kodi aplikacije

**Izstopajoč primer**: Moja sodelavka Debbie O'Brien je v zadnjem času opravila neverjetno delo s Playwright MCP strežnikom! Na primer, pokazala je, kako lahko ustvariš popolne Playwright teste brez dostopa do izvorne kode aplikacije. V njenem primeru je Copilotu naročila, naj naredi test za aplikacijo iskanja filmov: obišči stran, poišči "Garfield" in preveri, ali se film pojavi med rezultati. MCP je zagnal brskalnik, raziskal strukturo strani z DOM posnetki, našel prave selektorje in ustvaril popolnoma delujoč TypeScript test, ki je bil uspešno opravljen takoj ob prvem zagonu.

To, kar je res močno, je, da premošča vrzel med navodili v naravnem jeziku in izvršljivo testno kodo. Tradicionalni pristopi zahtevajo ročno pisanje testov ali dostop do kode za kontekst. Z Playwright MCP pa lahko testiraš zunanje strani, odjemalske aplikacije ali delaš v črno-skrinnih testnih scenarijih, kjer dostop do kode ni možen.


### 8. 💻 Dev Box MCP strežnik

[![Namesti v VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Namesti v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Kaj počne**: Upravljanje Microsoft Dev Box okolij preko naravnega jezika

**Zakaj je uporaben**: Izjemno poenostavi upravljanje razvojnega okolja! Ustvari, konfiguriraj in upravljaj razvojna okolja brez potrebe po pomnjenju specifičnih ukazov.

**Praktična uporaba**: "Nastavi nov Dev Box z najnovejšim .NET SDK in ga konfiguriraj za naš projekt", "Preveri stanje vseh mojih razvojnih okolij" ali "Ustvari standardizirano demo okolje za naše predstavitve ekipe"

**Izstopajoč primer**: Sem velik oboževalec uporabe Dev Box za osebni razvoj. Moj 'lightbulb' trenutek je bil, ko je James Montemagno pojasnil, kako odličen je Dev Box za konferenčne demonstracije, saj ima super hitro ethernet povezavo ne glede na konferenco / hotel / wifi na letalu, ki ga morda uporabljam. Pravzaprav sem nedavno vadil konferenčno demo, medtem ko je bil moj prenosnik povezan preko telefonskega hotspota na avtobusu iz Brugge v Antwerpen! Naslednji korak je, da se bolj osredotočim na upravljanje več razvojnih okolij in standardiziranih demo okolij za ekipe. In še ena velika uporaba, ki jo slišim od strank in sodelavcev, je uporaba Dev Box za predkonfigurirana razvojna okolja. V obeh primerih uporaba MCP za konfiguracijo in upravljanje Dev Boxov omogoča uporabo interakcije v naravnem jeziku, vse to pa ostane znotraj razvojnega okolja.

### 9. 🤖 Microsoft Foundry MCP strežnik


[![Namesti v VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Namesti v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Kaj počne**: Microsoft Foundry MCP Server razvijalcem omogoča celovit dostop do Azure AI ekosistema, vključno s katalogi modelov, upravljanjem uvajanja, indeksiranjem znanja z Azure AI Search in orodji za vrednotenje. Ta eksperimentalni strežnik premošča vrzel med razvojem umetne inteligence in močnimi Azure AI infrastrukturami, kar olajša gradnjo, uvajanje in vrednotenje AI aplikacij.

**Zakaj je uporaben**: Ta strežnik spreminja način vašega dela z Azure AI storitvami, saj prinaša zmogljivosti AI na ravni podjetja neposredno v vaš razvojni proces. Namesto stalnega preklapljanja med Azure portalom, dokumentacijo in vašim IDE-jem, lahko odkrijete modele, uvajate storitve, upravljate baze znanja in vrednotite AI zmogljivost prek ukazov v naravnem jeziku. Posebej je močan za razvijalce, ki gradijo RAG (Retrieval-Augmented Generation) aplikacije, upravljajo uvajanje več modelov ali izvajajo celovite AI vrednotitvene tokove.

**Ključne zmogljivosti za razvijalce**:
- **🔍 Odkritje in uvajanje modelov**: Raziskujte katalog modelov Microsoft Foundry, pridobite podrobne informacije o modelih s primeri kode in uvajajte modele v Azure AI storitve
- **📚 Upravljanje znanja**: Ustvarjajte in upravljajte Azure AI Search indekse, dodajajte dokumente, konfigurirajte indexerje in gradite sofisticirane RAG sisteme
- **⚡ Integracija AI agentov**: Povežite se z Azure AI agenti, poizvedujte obstoječe agente in vrednotite zmogljivost agentov v produkcijskih scenarijih
- **📊 Okvir za vrednotenje**: Izvajajte celovito vrednotenje besedil in agentov, ustvarjajte poročila v markdownu in izvajajte nadzor kakovosti AI aplikacij
- **🚀 Orodja za prototipiranje**: Pridobite navodila za nastavitev za prototipiranje na GitHubu in dostop do Microsoft Foundry Labs za najsodobnejše raziskovalne modele

**Primer uporabe v praksi**: "Uvedi Phi-4 model v Azure AI storitve za mojo aplikacijo", "Ustvari nov iskalni indeks za moj dokumentacijski RAG sistem", "Vrednoti odzive mojega agenta glede na merila kakovosti" ali "Najdi najboljši model za sklepanje za moje zahtevne analize"

**Celoten demo scenarij**: Tukaj je učinkovit razvojni postopek za AI:

> "Razvijam agenta za podporo strankam. Pomagaj mi najti dober model za sklepanje iz kataloga, uvedi ga v Azure AI storitve, ustvari bazo znanja iz naše dokumentacije, vzpostavi okvir za vrednotenje kakovosti odgovorov in nato pomagaj pri prototipiranju integracije s GitHub žetonom za testiranje."

Microsoft Foundry MCP Server bo:
- Poizvedoval po katalogu modelov in priporočal optimalne modele za sklepanje glede na vaše zahteve
- Zagotovil ukaze za uvajanje in informacije o kvotah za želeno Azure regijo
- Nastavil Azure AI Search indekse s pravilno shemo za vašo dokumentacijo
- Konfiguriral vrednotitvene tokove z merili kakovosti in varnostnimi pregledi
- Ustvaril prototipno kodo z GitHub avtentikacijo za takojšnje testiranje
- Zagotovil celovita navodila za nastavitev, prilagojena vaši tehnološki platformi

**Prikazan primer**: Kot razvijalec sem imel težave slediti različnim LLM modelom. Poznam nekaj glavnih, a sem imel občutek, da zamujam priložnosti za povečanje produktivnosti in učinkovitosti. Upravljanje tokenov in kvot je stresno in zahtevno – nikoli ne vem, ali izbiram pravi model za pravo nalogo ali pa neučinkovito trošim svoj proračun. Slišal sem za ta MCP strežnik od Jamesa Montemagna, ko sem spraševal sodelavce za priporočila glede MCP strežnika za ta zapis, in navdušen sem, da ga preizkusim! Zmožnosti odkrivanja modelov so posebej impresivne za nekoga, kot sem jaz, ki želi raziskovati onkraj običajnih modelov in najti modele, optimizirane za določene naloge. Okvir za vrednotenje bi mi moral pomagati potrditi, da dejansko dosegam boljše rezultate, ne le preizkušam nekaj novega zaradi samega preizkušanja.

> **ℹ️ Eksperimentalni status**
> 
> Ta MCP strežnik je eksperimentalni in je v aktivnem razvoju. Funkcije in API-ji se lahko spreminjajo. Odličen za raziskovanje zmogljivosti Azure AI in gradnjo prototipov, vendar preverite zahteve stabilnosti za produkcijsko uporabo.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Namesti v VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Namesti v VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Kaj počne**: Razvijalcem nudi ključna orodja za gradnjo AI agentov in aplikacij, ki se integrirajo z Microsoft 365 in Microsoft 365 Copilot, vključno s preverjanjem shem, pridobivanjem primerov kode in pomočjo pri odpravljanju težav.

**Zakaj je uporaben**: Razvijanje za Microsoft 365 in Copilot vključuje zapletene manifestne sheme in specifične razvojne vzorce. Ta MCP strežnik prinaša ključne razvojne vire neposredno v vaše razvojno okolje, pomaga pri preverjanju shem, iskanju primerov kode in odpravljanju pogostih težav brez stalnega sklicevanja na dokumentacijo.

**Uporaba v praksi**: "Preveri moj deklarativni manifest agenta in odpravi morebitne napake v shemi", "Pokaži mi primere kode za implementacijo vtičnika Microsoft Graph API" ali "Pomagaj mi odpraviti težave z avtentikacijo moje Teams aplikacije"

**Prikazan primer**: Obrnil sem se na svojega prijatelja Johna Millerja po pogovoru na konferenci Build o M365 agentih in priporočil je ta MCP. To bi bilo odlično za razvijalce, ki so novi v M365 agentih, saj ponuja predloge, primere kode in osnovno strukturo za lahek začetek brez utapljanja v dokumentaciji. Funkcije za preverjanje shem so še posebej uporabne za preprečevanje napak v strukturi manifesta, ki lahko povzročijo ure odpravljanja napak.

> **💡 Nasvet strokovnjaka**
> 
> Uporabite ta strežnik skupaj z Microsoft Learn Docs MCP strežnikom za celovito podporo razvoju M365 – eden nudi uradno dokumentacijo, ta pa praktična razvojna orodja in pomoč pri odpravljanju težav.


## Kaj sledi? 🔮

## 📋 Zaključek

Protokol Model Context (MCP) spreminja način interakcije razvijalcev z AI asistenti in zunanjimi orodji. Ti 10 Microsoft MCP strežnikov prikazujejo moč standardizirane AI integracije, ki omogoča nemoten razvojni potek, kjer razvijalci ostanejo v svojem toku, hkrati pa dostopajo do zmogljivih zunanjih funkcionalnosti.

Od celovite integracije Azure ekosistema do specializiranih orodij, kot sta Playwright za avtomatizacijo brskalnika in MarkItDown za procesiranje dokumentov, ti strežniki prikazujejo, kako lahko MCP poveča produktivnost skozi različne razvojne scenarije. Standardiziran protokol zagotavlja, da ta orodja brezhibno sodelujejo in ustvarjajo povezano razvojno izkušnjo.

S nadaljnjim razvojem MCP ekosistema bo ključnega pomena, da ostanete vključeni v skupnost, raziskujete nove strežnike in gradite prilagojene rešitve za maksimalno izboljšanje svoje razvojne produktivnosti. Odprta narava standarda MCP omogoča združevanje orodij različnih ponudnikov za ustvarjanje popolnega delovnega procesa po vaših specifičnih potrebah.

## 🔗 Dodatni viri

- [Uradno Microsoft MCP skladišče](https://github.com/microsoft/mcp)
- [MCP skupnost & Dokumentacija](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentacija](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentacija](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentacija](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Lets Learn – MCP dogodki](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Odlične prilagoditve GitHub Copilot](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days v živo 29. in 30. julij ali ogled na zahtevo](https://aka.ms/mcpdevdays)

## 🎯 Vaje

1. **Namestitev in konfiguracija**: Namestite enega od MCP strežnikov v vašem VS Code okolju in preizkusite osnovno funkcionalnost.
2. **Integracija delovnega toka**: Oblikujte razvojni potek, ki združuje najmanj tri različne MCP strežnike.
3. **Načrtovanje po meri strežnika**: Prepoznajte nalogo v vašem vsakodnevnem razvojnem procesu, ki bi lahko imela koristi od prilagojenega MCP strežnika, in ustvarite specifikacijo zanj.
4. **Analiza zmogljivosti**: Primerjajte učinkovitost uporabe MCP strežnikov z običajnimi pristopi pri pogostih razvojnih nalogah.
5. **Varnostna ocena**: Ocenite varnostne posledice uporabe MCP strežnikov v vašem razvojnem okolju in predlagajte najboljše prakse.


Naslednje:[Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->