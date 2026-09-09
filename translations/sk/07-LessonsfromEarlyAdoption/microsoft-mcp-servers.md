# 🚀 10 Microsoft MCP serverov, ktoré transformujú produktivitu vývojárov

## 🎯 Čo sa v tomto návode naučíte

Tento praktický návod predstavuje desať Microsoft MCP serverov, ktoré aktívne menia spôsob, akým vývojári pracujú s AI asistentmi. Namiesto toho, aby sme len vysvetľovali, čo MCP servery *môžu* robiť, ukážeme vám servery, ktoré už robia skutočný rozdiel v každodenných vývojových pracovných tokoch v Microsoft a mimo neho.

Každý server v tomto návode bol vybraný na základe reálneho používania a spätnej väzby od vývojárov. Zistíte nielen čo každý server robí, ale aj prečo je to dôležité a ako z neho vyťažiť maximum vo vlastných projektoch. Či už ste úplný nováčik v MCP, alebo chcete rozšíriť svoje existujúce nastavenie, tieto servery predstavujú niektoré z najpraktickejších a najúčinnějších nástrojov dostupných v ekosystéme Microsoft.

> **💡 Rýchla rada na začiatok**
> 
> Ste nováčik v MCP? Nemajte obavy! Tento návod je navrhnutý tak, aby bol priateľský pre začiatočníkov. Budeme vysvetľovať koncepty priebežne a vždy sa môžete vrátiť k našim modulom [Úvod do MCP](../00-Introduction/README.md) a [Základné koncepty](../01-CoreConcepts/README.md) pre hlbšie pozadie.

## Prehľad

Tento komplexný návod skúma desať Microsoft MCP serverov, ktoré revolučne menia spôsob, akým vývojári komunikujú s AI asistentmi a externými nástrojmi. Od správy Azure zdrojov po spracovanie dokumentov, tieto servery demonštrujú silu Model Context Protocol v tvorbe plynulých, produktívnych vývojových pracovných tokov.

## Výukové ciele

Po prečítaní tohto návodu budete:
- Pochopiť, ako MCP servery zvyšujú produktivitu vývojárov
- Naučiť sa o najdôležitejších implementáciách MCP serverov od Microsoftu
- Objaviť praktické prípady použitia každého servera
- Vedieť, ako nastaviť a nakonfigurovať tieto servery vo VS Code a Visual Studio
- Preskúmať širší ekosystém MCP a jeho budúce smery

## 🔧 Pochopenie MCP serverov: Návod pre začiatočníkov

### Čo sú MCP servery?

Ako začiatočník v Model Context Protocol (MCP) sa možno pýtate: „Čo vlastne je MCP server a prečo by ma to malo zaujímať?“ Začnime jednoduchou analógiou.

Predstavte si MCP servery ako špecializovaných asistentov, ktorí pomáhajú vášmu AI kódovaciemu spoločníkovi (ako je GitHub Copilot) pripojiť sa k externým nástrojom a službám. Rovnako ako používate na telefóne rôzne aplikácie na rôzne úlohy – jednu na počasie, jednu na navigáciu, jednu na bankovníctvo – MCP servery dávajú vášmu AI asistentovi schopnosť komunikovať s rôznymi vývojovými nástrojmi a službami.

### Problém, ktorý MCP servery riešia

Pred MCP servermi, ak ste chceli:
- Skontrolovať svoje Azure zdroje
- Vytvoriť GitHub issue
- Dotazovať svoju databázu
- Hľadať v dokumentácii

Museli ste prestať kódovať, otvoriť prehliadač, prejsť na príslušnú webovú stránku a manuálne tieto úlohy vykonať. Tento neustály presun kontextu narušuje váš pracovný tok a znižuje produktivitu.

### Ako MCP servery menia váš vývojový zážitok

S MCP servermi môžete zostať vo vašom vývojovom prostredí (VS Code, Visual Studio atď.) a jednoducho požiadať svojho AI asistenta, aby sa postaral o tieto úlohy. Napríklad:

**Namiesto tohto tradičného postupu:**
1. Prestať kódovať
2. Otvoriť prehliadač
3. Prejsť do Azure portálu
4. Vyhľadať detaily o úložnom účte
5. Vrátiť sa do VS Code
6. Pokračovať v kódovaní

**Môžete teraz robiť toto:**
1. Požiadať AI: „Aký je stav mojich Azure úložných účtov?“
2. Pokračovať v kódovaní s poskytnutými informáciami

### Hlavné výhody pre začiatočníkov

#### 1. 🔄 **Zostaňte vo svojom pracovnom toku**
- Už žiadne prepínanie medzi viacerými aplikáciami
- Sústreďte sa na kód, ktorý píšete
- Znížte mentálnu záťaž z ovládania viacerých nástrojov

#### 2. 🤖 **Používajte prirodzený jazyk namiesto zložitých príkazov**
- Namiesto učenia sa syntaxe SQL popíšte, ktoré dáta potrebujete
- Namiesto zapamätania Azure CLI príkazov vysvetlite, čo chcete dosiahnuť
- Nechajte AI riešiť technické detaily, zatiaľ čo vy sa sústredíte na logiku

#### 3. 🔗 **Prepojte viaceré nástroje dohromady**
- Vytvorte silné pracovné toky spojením rôznych služieb
- Príklad: „Získaj všetky nedávne GitHub issues a vytvor zodpovedajúce Azure DevOps work itemy“
- Budujte automatizácie bez písania zložitých skriptov

#### 4. 🌐 **Prístup k rastúcemu ekosystému**
- Využite servery vytvorené Microsoftom, GitHubom a inými spoločnosťami
- Bez problémov kombinujte nástroje od rôznych dodávateľov
- Pripojte sa k štandardizovanému ekosystému, ktorý funguje naprieč rôznymi AI asistentmi

#### 5. 🛠️ **Učte sa prakticky**
- Začnite s predpripravenými servermi, aby ste pochopili koncepty
- Postupne si budujte vlastné servery, keď budete pohodlnejší
- Používajte dostupné SDK a dokumentáciu na vedenie učenia

### Skutočný príklad pre začiatočníkov

Povedzme, že ste nový vo webovom vývoji a pracujete na svojom prvom projekte. Toto je, ako MCP servery môžu pomôcť:

**Tradičný prístup:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**S MCP servermi:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Výhoda štandardu pre podniky

MCP sa stáva priemyselným štandardom, čo znamená:
- **Konzistentnosť**: Podobný zážitok naprieč rôznymi nástrojmi a spoločnosťami
- **Interoperabilita**: Servery od rôznych dodávateľov spolupracujú
- **Budúca použiteľnosť**: Zručnosti a nastavenia sa prenášajú medzi rôznymi AI asistentmi
- **Komunita**: Veľký ekosystém zdielaných znalostí a zdrojov

### Začíname: Čo sa naučíte

V tomto návode preskúmame 10 Microsoft MCP serverov, ktoré sú obzvlášť užitočné pre vývojárov na všetkých úrovniach. Každý server je navrhnutý tak, aby:
- Riešil bežné vývojové výzvy
- Znižoval opakujúce sa úlohy
- Zlepšoval kvalitu kódu
- Zvyšoval príležitosti na učenie

> **💡 Rada na učenie**
> 
> Ak ste úplný nováčik v MCP, najprv začnite s našimi modulmi [Úvod do MCP](../00-Introduction/README.md) a [Základné koncepty](../01-CoreConcepts/README.md). Potom sa vráťte sem, aby ste videli tieto koncepty v akcii s reálnymi Microsoft nástrojmi.
>
> Pre ďalší kontext o význame MCP sa pozrite na príspevok Marie Naggagovej: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Začíname s MCP vo VS Code a Visual Studio 🚀

Nastavenie týchto MCP serverov je jednoduché, ak používate Visual Studio Code alebo Visual Studio 2022 s GitHub Copilot.

### Nastavenie vo VS Code

Tu je základný proces pre VS Code:

1. **Zapnite režim Agenta**: Vo VS Code prepnite na režim Agenta v okne Copilot Chat
2. **Nakonfigurujte MCP servery**: Pridajte konfigurácie servera do súboru settings.json vo VS Code
3. **Spustite servery**: Kliknite na tlačidlo „Start“ pre každý server, ktorý chcete použiť
4. **Vyberte nástroje**: Vyberte, ktoré MCP servery povolíte pre svoju aktuálnu reláciu

Pre podrobné inštrukcie nastavenia pozrite dokumentáciu [VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profesionálny tip: Spravujte MCP servery ako profesionál!**
> 
> Zobrazenie rozšírení vo VS Code teraz obsahuje [praktické nové používateľské rozhranie na správu nainštalovaných MCP serverov](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Máte rýchly prístup na spustenie, zastavenie a správu akýchkoľvek nainštalovaných MCP serverov pomocou jasného a jednoduchého rozhrania. Vyskúšajte to!

### Nastavenie vo Visual Studio 2022

Pre Visual Studio 2022 (verzia 17.14 alebo novšia):

1. **Zapnite režim Agenta**: Kliknite na rozbaľovaciu ponuku „Ask“ v okne GitHub Copilot Chat a vyberte „Agent“
2. **Vytvorte konfiguračný súbor**: Vytvorte súbor `.mcp.json` v adresári svojho riešenia (odporúčané miesto: `<SOLUTIONDIR>\.mcp.json`)
3. **Nakonfigurujte servery**: Pridajte svoje konfigurácie MCP serverov pomocou štandardného formátu MCP
4. **Schválenie nástrojov**: Keď budete vyzvaní, schváľte nástroje, ktoré chcete používať, s príslušnými oprávneniami rozsahu

Pre podrobné inštrukcie nastavenia Visual Studio pozrite si dokumentáciu [Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Každý MCP server má svoje vlastné požiadavky na konfiguráciu (reťazce pripojení, autentifikácia atď.), ale vzor nastavenia je konzistentný pre obe IDE.

## Ponaučenie z Microsoft MCP serverov 🛠️

### 1. 📚 Microsoft Learn Docs MCP server

[![Instalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Instalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Čo robí**: Microsoft Learn Docs MCP server je cloudová služba, ktorá poskytuje AI asistentom prístup v reálnom čase k oficiálnej dokumentácii Microsoft cez Model Context Protocol. Pripája sa na `https://learn.microsoft.com/api/mcp` a umožňuje sémantické vyhľadávanie v rámci Microsoft Learn, Azure dokumentácie, Microsoft 365 dokumentácie a ďalších oficiálnych zdrojov Microsoft.

**Prečo je užitočný**: Aj keď sa to môže zdať ako „len dokumentácia“, tento server je v skutočnosti kľúčový pre každého vývojára používajúceho Microsoft technológie. Jednou z najväčších sťažností .NET vývojárov na AI kódovacích asistentov je, že nie sú aktuálni s najnovšími vydaniami .NET a C#. Microsoft Learn Docs MCP server to rieši tým, že poskytuje prístup v reálnom čase k najaktuálnejšej dokumentácii, API referenciám a osvedčeným postupom. Či už pracujete s najnovšími Azure SDK, skúmate nové funkcie C# 13, alebo implementujete najmodernejšie Aspire vzory, tento server zaručuje, že váš AI asistent má prístup k autoritatívnym, aktuálnym informáciám potrebným na generovanie presného a moderného kódu.

**Reálne použitie**: „Aké sú az cli príkazy na vytvorenie Azure container aplikácie podľa oficiálnej dokumentácie Microsoft Learn?“ alebo „Ako nakonfigurovať Entity Framework s dependency injection v ASP.NET Core?“ Alebo „Skontroluj tento kód, či zodpovedá výkonovým odporúčaniam v Microsoft Learn dokumentácii.“ Server poskytuje komplexné pokrytie v rámci Microsoft Learn, Azure dokumentácie a Microsoft 365 dokumentácie pomocou pokročilého sémantického vyhľadávania na nájdenie najrelevantnejších kontextových informácií. Vracia až 10 vysoko kvalitných obsahových blokov s názvami článkov a URL odkazmi, vždy pristupujúc k najnovšej Microsoft dokumentácii v čase jej publikovania.

**Ukážkový príklad**: Server sprístupňuje nástroj `microsoft_docs_search`, ktorý vykonáva sémantické vyhľadávanie v oficiálnej technickej dokumentácii Microsoft. Po nastavení môžete klásť otázky ako „Ako implementovať JWT autentifikáciu v ASP.NET Core?“ a získať podrobné, oficiálne odpovede s odkazmi na zdroje. Kvalita vyhľadávania je výnimočná, pretože rozumie kontextu – otázka o „kontajneroch“ v Azure kontexte vráti dokumentáciu Azure Container Instances, zatiaľ čo ten istý pojem v .NET kontexte vráti relevantné informácie o C# kolekciách.

To je obzvlášť užitočné pre rýchlo sa meniace alebo nedávno aktualizované knižnice a prípady použitia. Napríklad v niektorých nedávnych kódovacích projektoch som chcel využiť funkcie v najnovších vydaniach Aspire a Microsoft.Extensions.AI. Zaradením Microsoft Learn Docs MCP servera som mohol využiť nielen API dokumentáciu, ale aj návody a usmernenia, ktoré práve vyšli.

> **💡 Profesionálny tip**
> 
> Aj modely priateľské k nástrojom potrebujú povzbudenie na používanie MCP nástrojov! Zvážte pridanie systémového promptu alebo [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) ako: „Máte prístup k `microsoft.docs.mcp` – používajte tento nástroj na vyhľadávanie najnovšej oficiálnej dokumentácie Microsoft pri riešení otázok o Microsoft technológiách ako C#, Azure, ASP.NET Core, alebo Entity Framework.“
>
> Pre skvelý príklad toho v praxi si pozrite režim chatovania [C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) z repoziára Awesome GitHub Copilot. Tento režim špecificky využíva Microsoft Learn Docs MCP server na pomoc s čistením a modernizáciou C# kódu použitím najnovších vzorov a osvedčených postupov.
### 2. ☁️ Azure MCP Server


[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Čo robí**: Azure MCP Server je komplexná sada viac ako 15 špecializovaných konektorov Azure služieb, ktoré prinášajú celý ekosystém Azure do vášho AI pracovného postupu. Toto nie je len jeden server – je to výkonná kolekcia zahŕňajúca správu zdrojov, pripojenie k databázam (PostgreSQL, SQL Server), analýzu logov Azure Monitor pomocou KQL, integráciu Cosmos DB a mnoho ďalšieho.

**Prečo je užitočný**: Okrem správy zdrojov Azure tento server výrazne zlepšuje kvalitu kódu pri práci s Azure SDK. Použitím Azure MCP v režime Agenta vám neprináša len pomoc s písaním kódu – pomáha vám písať *lepšie* Azure kódy, ktoré dodržiavajú aktuálne vzory autentifikácie, najlepšie postupy správy chýb a využívajú najnovšie funkcie SDK. Namiesto generického kódu, ktorý možno funguje, dostanete kód, ktorý nasleduje odporúčané vzory Azure pre produkčné prostredia.

**Kľúčové moduly zahŕňajú**:
- **🗄️ Konektory databáz**: Priamy prístup v prirodzenom jazyku do Azure Database pre PostgreSQL a SQL Server
- **📊 Azure Monitor**: Analýza logov pomocou KQL a prevádzkové poznatky
- **🌐 Správa zdrojov**: Kompletná správa životného cyklu zdrojov Azure
- **🔐 Autentifikácia**: Vzory DefaultAzureCredential a spravované identity
- **📦 Úložné služby**: Operácie Blob Storage, Queue Storage a Table Storage
- **🚀 Kontajnerové služby**: Azure Container Apps, Container Instances a správa AKS
- **A mnoho ďalších špecializovaných konektorov**

**Reálne použitie**: „Zoznam mojich Azure úložných účtov“, „Dotaz na moje Log Analytics pracovisko pre chyby v poslednej hodine“ alebo „Pomôž mi vytvoriť Azure aplikáciu v Node.js s riadnou autentifikáciou“

**Úplné demo použitie**: Tu je kompletný postup, ktorý ukazuje silu kombinácie Azure MCP s rozšírením GitHub Copilot pre Azure vo VS Code. Keď máte oba nainštalované a zadáte príkaz:

> „Vytvor Python skript, ktorý nahraje súbor do Azure Blob Storage pomocou autentifikácie DefaultAzureCredential. Skript by sa mal pripojiť k môjmu Azure úložnému účtu s názvom 'mycompanystorage', nahrať do kontajnera s názvom 'documents', vytvoriť testovací súbor s aktuálnym časovým údajom na nahranie, ošetriť chyby potrebným spôsobom a poskytnúť informatívny výstup, dodržiavať najlepšie postupy Azure pre autentifikáciu a spracovanie chýb, zahrnúť komentáre vysvetľujúce, ako funguje autentifikácia DefaultAzureCredential, a urobiť skript dobre štruktúrovaný s vhodnými funkciami a dokumentáciou.“

Azure MCP Server vygeneruje kompletný, produkčne pripravený Python skript, ktorý:
- Používa najnovšie Azure Blob Storage SDK s korektnými asynchrónnymi vzormi
- Implementuje DefaultAzureCredential s podrobným vysvetlením reťazca záložných variantov
- Zahrnuje robustnú správu chýb s konkrétnymi typmi výnimiek Azure
- Dodržiava najlepšie postupy Azure SDK pre správu zdrojov a spracovanie pripojení
- Poskytuje podrobné protokolovanie a informatívny výstup na konzolu
- Vytvára správne štruktúrovaný skript s funkciami, dokumentáciou a typovými anotáciami

Čo je na tom pozoruhodné, je, že bez Azure MCP by ste mohli získať generický kód pre blob storage, ktorý funguje, no nedodržiava aktuálne Azure vzory. S Azure MCP dostávate kód, ktorý využíva najnovšie metódy autentifikácie, rieši Azure-špecifické chyby a nasleduje odporúčané postupy Microsoftu pre produkčné aplikácie.

**Ukážkový príklad**: Mal som problém si zapamätať špecifické príkazy pre CLI `az` a `azd` pre ad-hoc použitie. Pre mňa je to vždy dvojkrokový proces: najprv si vyhľadať syntax, potom spustiť príkaz. Často som len vošiel do portálu a klikol okolo, aby som prácu dokončil, pretože som nechcel priznať, že si syntax CLI nepamätám. Byť schopný len opísať, čo chcem, je úžasné, a ešte lepšie je môcť to urobiť bez opustenia môjho IDE!

V [Azure MCP repozitári](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) je skvelý zoznam prípadov použitia, ktoré vám pomôžu začať. Pre komplexné návody na nastavenie a pokročilé možnosti konfigurácie si pozrite [oficiálnu dokumentáciu Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Čo robí**: Oficiálny GitHub MCP Server zabezpečuje bezproblémovú integráciu s celým ekosystémom GitHub, ponúkajúc možnosti hosťovaného vzdialeného prístupu aj lokálnej inštalácie cez Docker. Toto nie je iba o základných operáciách s repozitármi – ide o komplexný nástrojový balík, ktorý zahŕňa správu GitHub Actions, pracovné postupy pre pull requesty, sledovanie issues, bezpečnostné skenovanie, notifikácie a pokročilé možnosti automatizácie.

**Prečo je užitočný**: Tento server mení spôsob, akým pracujete s GitHub, tým, že prináša plnohodnotnú platformu priamo do vášho vývojového prostredia. Namiesto neustáleho prepínania medzi VS Code a GitHub.com pre správu projektov, kontrolu kódu a monitoring CI/CD môžete všetko riešiť príkazmi v prirodzenom jazyku, a pritom zostať sústredení na kód.

> **ℹ️ Poznámka: Rôzne typy 'agentov'**
> 
> Nezamieňajte tento GitHub MCP Server s GitHub Coding Agentom (AI agent, ktorému môžete priradiť issues na automatické vykonávanie kódovacích úloh). GitHub MCP Server pracuje v rámci VS Code v režime Agenta a poskytuje integráciu GitHub API, zatiaľ čo GitHub Coding Agent je samostatná funkcia, ktorá vytvára pull requesty, keď je priradený k issue.

**Kľúčové schopnosti zahŕňajú**:
- **⚙️ GitHub Actions**: Kompletná správa CI/CD pipeline, monitorovanie workflow a spracovanie artefaktov
- **🔀 Pull Requests**: Vytvorenie, kontrola, zlúčenie a správa PR s komplexným sledovaním stavu
- **🐛 Issues**: Kompletná správa životného cyklu issues, komentovanie, označovanie a priraďovanie
- **🔒 Bezpečnosť**: Upozornenia o skenovaní kódu, detekcia tajomstiev a integrácia Dependabota
- **🔔 Notifikácie**: Inteligentná správa upozornení a kontrola prihlásenia k repozitárom
- **📁 Správa repozitárov**: Operácie so súbormi, správa vetiev a administrácia repozitárov
- **👥 Spolupráca**: Vyhľadávanie používateľov a organizácií, správa tímov a kontrola prístupov

**Reálne použitie**: „Vytvor pull request z mojej feature vetvy“, „Ukáž všetky neúspešné CI behy tento týždeň“, „Zoznam otvorených bezpečnostných upozornení pre moje repozitáre“ alebo „Nájdi všetky issues priradené mne v mojich organizáciách“

**Úplné demo použitie**: Tu je silný pracovný postup, ktorý demonštruje schopnosti GitHub MCP Servera:

> „Potrebujem sa pripraviť na náš sprint review. Ukáž mi všetky pull requesty, ktoré som tento týždeň vytvoril, skontroluj stav našich CI/CD pipeline, vytvor súhrn bezpečnostných upozornení, ktoré musíme riešiť, a pomôž mi zostaviť poznámky k vydaniu na základe zlúčených PRs s označením 'feature'.“

GitHub MCP Server:
- Vyhľadá tvoje nedávne pull requesty s podrobnými informáciami o stave
- Analyzuje behy workflow a zvýrazní akékoľvek zlyhania alebo problémy s výkonom
- Kompiluje výsledky bezpečnostného skenovania a zoraďuje kritické upozornenia
- Generuje komplexné poznámky k vydaniu extrahovaním informácií zo zlúčených PRs
- Poskytuje konkrétne ďalšie kroky pre plánovanie sprintu a prípravu vydania

**Ukážkový príklad**: Rád ho používam pre pracovné postupy kontroly kódu. Namiesto preskakovania medzi VS Code, GitHub notifikáciami a stránkami pull requestov môžem povedať „Ukáž mi všetky PRs čakajúce na moju recenziu“ a potom „Pridaj komentár k PR #123 pýtajúci sa na spracovanie chýb v autentifikačnej metóde.“ Server spravuje volania GitHub API, udržiava kontext diskusie a dokonca mi pomáha vytvárať konštruktívnejšie recenzné komentáre.

**Možnosti autentifikácie**: Server podporuje OAuth (bezproblémové vo VS Code) a osobné prístupové tokeny, s konfigurovateľným sadami nástrojov pre zapnutie len potrebných GitHub funkcií. Môžete ho používať ako hosťovanú vzdialenú službu pre okamžité nasadenie alebo lokálne cez Docker pre úplnú kontrolu.

> **💡 Tip**
> 
> Povoliť len tie sady nástrojov, ktoré potrebujete, konfiguráciou parametra `--toolsets` v nastaveniach MCP servera na zníženie veľkosti kontextu a zlepšenie výberu AI nástrojov. Napríklad pridajte `"--toolsets", "repos,issues,pull_requests,actions"` do argumentov konfigurácie MCP pre základné vývojové pracovné postupy, alebo použite `"--toolsets", "notifications, security"`, ak chcete prevažne monitorovacie schopnosti GitHub.
### 4. 🔄 Azure DevOps MCP Server

[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Čo robí**: Pripája sa k Azure DevOps službám pre komplexnú správu projektov, sledovanie pracovných položiek, správu build pipeline a operácie s repozitármi.

**Prečo je užitočný**: Pre tímy používajúce Azure DevOps ako primárnu DevOps platformu tento MCP server eliminuje neustále prepínanie záložiek medzi vývojovým prostredím a webovým rozhraním Azure DevOps. Môžete spravovať pracovné položky, kontrolovať stavy buildov, dotazovať repozitáre a riešiť projektové úlohy priamo cez svojho AI asistenta.

**Reálne použitie**: „Ukáž mi všetky aktívne pracovné položky v aktuálnom sprinte pre projekt WebApp“, „Vytvor hlásenie o chybe na problém s prihlasovaním, ktorý som práve našiel“, alebo „Skontroluj stav našich build pipeline a ukáž mi nedávne neúspechy“

**Ukážkový príklad**: Jednoducho si môžete skontrolovať stav aktuálneho sprintu vášho tímu pomocou jednoduchého dotazu ako „Ukáž mi všetky aktívne pracovné položky v aktuálnom sprinte pre projekt WebApp“ alebo „Vytvor hlásenie o chybe na problém s prihlasovaním, ktorý som práve našiel“ bez opustenia vášho vývojového prostredia.

### 5. 📝 MarkItDown MCP Server


[![Nainštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Nainštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Čo robí**: MarkItDown je komplexný server na konverziu dokumentov, ktorý transformuje rôzne formáty súborov do vysoko kvalitného Markdownu, optimalizovaného pre spracovanie veľkých jazykových modelov (LLM) a pracovné procesy analýzy textu.

**Prečo je užitočný**: Nevyhnutný pre moderné pracovné postupy dokumentácie! MarkItDown zvláda pôsobivý rozsah formátov súborov a pritom zachováva kritickú štruktúru dokumentu, ako sú nadpisy, zoznamy, tabuľky a odkazy. Na rozdiel od jednoduchých nástrojov na extrakciu textu sa zameriava na udržanie sémantického významu a formátovania, ktoré sú cenné pre spracovanie umelou inteligenciou aj pre ľahkú čitateľnosť.

**Podporované formáty súborov**:
- **Office dokumenty**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Mediálne súbory**: Obrázky (s EXIF metadátami a OCR), Audio (s EXIF metadátami a prepisom reči)
- **Webový obsah**: HTML, RSS kanály, YouTube URL, Wikipedické stránky
- **Dátové formáty**: CSV, JSON, XML, ZIP súbory (rekurzívne spracováva obsah)
- **Publikačné formáty**: EPub, Jupyter notebooky (.ipynb)
- **E-mail**: Outlook správy (.msg)
- **Pokročilé**: Integrácia Azure Document Intelligence pre rozšírené spracovanie PDF

**Pokročilé schopnosti**: MarkItDown podporuje popisy obrázkov generované pomocou LLM (ak je k dispozícii klient OpenAI), Azure Document Intelligence pre rozšírené spracovanie PDF, prepis audia obsahu reči a systém pluginov na rozšírenie o ďalšie formáty súborov.

**Praktické použitie**: „Konvertuj túto PowerPoint prezentáciu do Markdownu pre náš dokumentačný web“, „Extrahuj text z tohto PDF so správnou štruktúrou nadpisov“ alebo „Transformuj túto Excel tabuľku do čitateľného formátu tabuliek“

**Ukážkový príklad**: Citujem z [MarkItDown dokumentácie](https://github.com/microsoft/markitdown#why-markdown):

> Markdown je extrémne blízky čistému textu, s minimálnou značkovacou alebo formátovacou syntaxou, no stále poskytuje spôsob, ako reprezentovať dôležitú štruktúru dokumentu. Hlavné LLM, ako napríklad OpenAI GPT-4o, prirodzene „hovoria“ Markdownom a často do svojich odpovedí začleňujú Markdown bez vyzvania. To naznačuje, že boli trénované na obrovskom množstve textov formátovaných v Markdown a dobre tomuto formátu rozumejú. Ako vedľajší efekt sú konvencie Markdownu tiež veľmi efektívne z hľadiska tokenov.

MarkItDown je naozaj dobrý v zachovaní štruktúry dokumentu, čo je dôležité pre pracovné postupy AI. Napríklad pri konverzii PowerPoint prezentácie zachováva usporiadanie snímok s vhodnými nadpismi, extrahuje tabuľky ako Markdown tabuľky, pridáva alt text obrázkov a dokonca spracúva poznámky rečníka. Grafy sú prevedené do čitateľných dátových tabuliek a výsledný Markdown si zachováva logický tok pôvodnej prezentácie. To je ideálne na napájanie prezentácií do AI systémov alebo tvorbu dokumentácie zo existujúcich snímok.
### 6. 🗃️ SQL Server MCP Server

[![Nainštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Nainštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Čo robí**: Umožňuje konverzačný prístup k databázam SQL Server (on-premises, Azure SQL alebo Fabric)

**Prečo je užitočný**: Podobný ako PostgreSQL server, ale pre ekosystém Microsoft SQL. Pripojte sa jednoduchým pripojovacím reťazcom a začnite dotazovať prirodzeným jazykom – žiadne prepínanie kontextu!

**Praktické použitie**: „Nájdi všetky objednávky, ktoré neboli splnené za posledných 30 dní“ sa preloží na vhodné SQL dotazy a vráti formátované výsledky

**Ukážkový príklad**: Akonáhle nastavíte pripojenie k databáze, môžete okamžite začať viesť konverzácie s vašimi dátami. Blogový príspevok to ukazuje jednoduchou otázkou: „Na ktorú databázu ste pripojení?“ MCP server odpovie vyvolaním príslušného databázového nástroja, pripojením na váš SQL Server inštanciu a vráti podrobnosti o aktuálnom pripojení k databáze – všetko bez napísania jediného riadku SQL. Server podporuje komplexné operácie s databázou od správy schémy po manipuláciu s dátami, všetko prostredníctvom prirodzených jazykových podnetov. Kompletné pokyny na nastavenie a konfiguračné príklady s VS Code a Claude Desktop nájdete tu: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP Server

[![Nainštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Nainštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Čo robí**: Umožňuje AI agentom interagovať s webovými stránkami pre testovanie a automatizáciu

> **ℹ️ Poháňa GitHub Copilot**
> 
> Playwright MCP Server poháňa Kodovací agent GitHub Copilot, čo mu dáva schopnosti prehliadať web! [Viac o tejto funkcii](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Prečo je užitočný**: Perfektný na automatizované testovanie pomocou popisu v prirodzenom jazyku. AI môže navigovať po webových stránkach, vyplňovať formuláre a extrahovať dáta cez štruktúrované snapshoty prístupnosti – to je nesmierne silná vec!

**Praktické použitie**: „Otestuj prihlasovací proces a over, či sa správne načíta dashboard“ alebo „Vygeneruj test, ktorý vyhľadáva produkty a overí stránku výsledkov“ – to všetko bez potreby zdrojového kódu aplikácie

**Ukážkový príklad**: Moja kolegyňa Debbie O'Brien v poslednej dobe odvádza úžasnú prácu s Playwright MCP Serverom! Napríklad nedávno ukázala, ako môžete vygenerovať kompletné Playwright testy bez toho, aby ste mali prístup k zdrojovému kódu aplikácie. V jej scenári požiadala Copilota o vytvorenie testu na vyhľadávanie filmov: prejdite na stránku, vyhľadajte „Garfield“ a overte, že sa film objaví vo výsledkoch. MCP spustil reláciu prehliadača, preskúmal štruktúru stránky pomocou DOM snapshotov, našiel správne selektory a vygeneroval plnohodnotný TypeScript test, ktorý prešiel už pri prvom spustení.

To, čo je na tom naozaj silné, je, že to premoštováva medzeru medzi inštrukciami v prirodzenom jazyku a vykonateľným testovacím kódom. Tradičné prístupy vyžadujú buď manuálne písanie testov, alebo prístup ku kódu pre kontext. Ale s Playwright MCP môžete testovať externé stránky, klientské aplikácie alebo pracovať v black-box testovacích scenároch, kde prístup ku kódu nie je možný.


### 8. 💻 Dev Box MCP Server

[![Nainštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Nainštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Čo robí**: Spravuje prostredia Microsoft Dev Box cez prirodzený jazyk

**Prečo je užitočný**: Veľmi zjednodušuje správu vývojových prostredí! Vytvorte, nakonfigurujte a spravujte vývojové prostredia bez nutnosti pamätať si konkrétne príkazy.

**Praktické použitie**: „Nastav nový Dev Box s najnovším .NET SDK a nakonfiguruj ho pre náš projekt“, „Skontroluj stav všetkých mojich vývojových prostredí“ alebo „Vytvor štandardizované demo prostredie pre naše tímové prezentácie“

**Ukážkový príklad**: Som veľkým fanúšikom používania Dev Box pre osobný vývoj. Môj moment osvietenia prišiel, keď James Montemagno vysvetlil, ako super je Dev Box na konferenčné demo, pretože má super rýchle ethernetové pripojenie bez ohľadu na wifi v hoteli, na konferencii alebo v lietadle, ktoré práve používam. Nedávno som dokonca robil konferenčné demo cvičenie, keď môj laptop bol pripojený na hotspot môjho telefónu počas cesty autobusom z Bruges do Antwerp! Mojím ďalším krokom je viac tímovo spravovať viaceré vývojové prostredia a štandardizované demo prostredia. A ďalšie veľké využitie, o ktorom počúvam od zákazníkov a kolegov, je používanie Dev Box na predkonfigurované vývojové prostredia. V oboch prípadoch enable používanie MCP na konfiguráciu a správu Dev Boxov umožňuje komunikáciu prirodzeným jazykom, pričom ste stále vo vašom vývojovom prostredí.

### 9. 🤖 Microsoft Foundry MCP Server


[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Čo to robí**: Microsoft Foundry MCP Server poskytuje vývojárom komplexný prístup k ekosystému Azure AI, vrátane katalógov modelov, správy nasadení, indexovania znalostí s Azure AI Search a hodnotiacich nástrojov. Tento experimentálny server prepája vývoj AI a výkonnú AI infraštruktúru Azure, čím uľahčuje vytváranie, nasadenie a hodnotenie AI aplikácií.

**Prečo je to užitočné**: Tento server mení spôsob, akým pracujete so službami Azure AI tým, že prináša prvotriedne AI schopnosti priamo do vášho vývojového pracovného postupu. Namiesto prechádzania medzi Azure portálom, dokumentáciou a vaším IDE môžete objavovať modely, nasadzovať služby, spravovať znalostné bázy a hodnotiť výkon AI pomocou príkazov v prirodzenom jazyku. Je obzvlášť silný pre vývojárov, ktorí vytvárajú RAG (Retrieval-Augmented Generation) aplikácie, spravujú viacnásobné modelové nasadenia alebo implementujú komplexné hodnotiace pipeline pre AI.

**Hlavné schopnosti pre vývojárov**:
- **🔍 Objevovanie modelov a nasadenie**: Preskúmajte katalóg modelov Microsoft Foundry, získajte podrobné informácie o modeloch s príkladmi kódu a nasadzujte modely do služieb Azure AI
- **📚 Správa znalostí**: Vytvárajte a spravujte indexy Azure AI Search, pridávajte dokumenty, konfigurujte indexery a vytvárajte sofistikované RAG systémy
- **⚡ Integrácia AI agentov**: Pripojte sa k Azure AI Agentom, vyhľadávajte existujúcich agentov a hodnotte výkon agentov v produkčných scenároch
- **📊 Hodnotiaci rámec**: Spúšťajte komplexné textové a agentné hodnotenia, generujte markdown správy a implementujte kontrolu kvality pre AI aplikácie
- **🚀 Nástroje na prototypovanie**: Získajte inštrukcie na nastavenie prototypovania na GitHub a prístup k Microsoft Foundry Labs pre najmodernejšie výskumné modely

**Použitie v reálnom svete pre vývojárov**: "Nasadiť Phi-4 model do Azure AI služieb pre moju aplikáciu", "Vytvoriť nový vyhľadávací index pre môj dokumentačný RAG systém", "Hodnotiť odpovede môjho agenta podľa kvalitatívnych metrík" alebo "Nájsť najlepší model vyvodzovania záverov pre moje komplexné analytické úlohy"

**Kompletný demo scenár**: Tu je výkonný pracovný tok pre vývoj AI:

> "Vytváram zákazníckeho podporcu. Pomôž mi nájsť dobrý model vyvodzovania záverov z katalógu, nasadiť ho do Azure AI služieb, vytvoriť znalostnú databázu z našej dokumentácie, nastaviť hodnotiaci rámec na testovanie kvality odpovedí a potom mi pomôž prototypovať integráciu s GitHub tokenom na testovanie."

Microsoft Foundry MCP Server:
- Vyhľadá v katalógu modelov odporúčania optimálnych modelov vyvodzovania záverov podľa vašich požiadaviek
- Poskytne príkazy na nasadenie a informácie o kvótach pre preferovaný región Azure
- Nastaví indexy Azure AI Search s vhodnou schémou pre vašu dokumentáciu
- Nakonfiguruje hodnotiace pipeline s kvalitatívnymi metrikami a bezpečnostnými kontrolami
- Vygeneruje kód na prototypovanie s GitHub autentifikáciou pre okamžité testovanie
- Poskytne komplexné návody na nastavenie prispôsobené vášmu konkrétnemu technologickému stacku

**Predstavený príklad**: Ako vývojár som mal problémy udržať krok s rôznymi LLM modelmi. Poznám pár hlavných, ale mal som pocit, že prichádzam o možné zvýšenie produktivity a efektivity. A tokeny a kvóty sú stresujúce a ťažké na správu – nikdy neviem, či vyberám správny model na správnu úlohu alebo neefektívne míňam rozpočet. Počul som o tomto MCP Serveri od Jamesa Montemagna, keď som sa pýtal tímu na odporúčania na MCP Server pre tento príspevok, a som nadšený, že ho môžem použiť! Schopnosti objavovania modelov vyzerajú obzvlášť pôsobivo pre niekoho ako som ja, kto chce preskúmať možnosti za hranicami bežných modelov a nájsť modely optimalizované pre špecifické úlohy. Hodnotiaci rámec mi pomôže overiť, že naozaj dosahujem lepšie výsledky a nie len experimentujem pre experimentovanie.

> **ℹ️ Experimentálny stav**
> 
> Tento MCP server je experimentálny a je aktívne vyvíjaný. Funkcie a API sa môžu meniť. Ideálny na skúmanie schopností Azure AI a vytváranie prototypov, ale pri produkčnom použití je potrebné overiť stabilitu.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Čo to robí**: Poskytuje vývojárom základné nástroje na vytváranie AI agentov a aplikácií, ktoré sa integrujú s Microsoft 365 a Microsoft 365 Copilot, vrátane validácie schém, získavania ukážkového kódu a pomoci pri riešení problémov.

**Prečo je to užitočné**: Vývoj pre Microsoft 365 a Copilot zahŕňa zložité manifestové schémy a špecifické vývojové vzory. Tento MCP server prináša nevyhnutné vývojové zdroje priamo do vášho kódovacieho prostredia, pomáha validovať schémy, nájsť ukážkový kód a riešiť bežné problémy bez nutnosti neustáleho otvárania dokumentácie.

**Použitie v reálnom svete**: "Validovať môj deklaratívny agent manifest a opraviť chyby v schéme", "Ukáž mi ukážkový kód na implementáciu Microsoft Graph API pluginu" alebo "Pomôž mi vyriešiť problémy s autentifikáciou mojej Teams aplikácie"

**Predstavený príklad**: Obrátil som sa na môjho priateľa Johna Millera po rozhovore na konferencii Build o M365 Agentoch a on mi odporučil tento MCP. Tento nástroj môže byť skvelý pre vývojárov, ktorí sú noví v M365 Agents, pretože poskytuje šablóny, ukážkový kód a kostru na začiatok bez ton dokumentácie. Funkcie validácie schém vyzerajú obzvlášť užitočne na zabránenie chýb v štruktúre manifestu, ktoré by mohli spôsobiť hodiny ladenia.

> **💡 Užitečný tip**
> 
> Používajte tento server spolu s Microsoft Learn Docs MCP Serverom pre komplexnú podporu vývoja M365 – jeden poskytuje oficiálnu dokumentáciu a tento praktické nástroje na vývoj a riešenie problémov.


## Čo ďalej? 🔮

## 📋 Záver

Protokol Model Context Protocol (MCP) mení spôsob, akým vývojári interagujú s AI asistentmi a externými nástrojmi. Týchto 10 Microsoft MCP serverov demonštruje silu štandardizovanej AI integrácie, ktorá umožňuje hladké pracovné toky a pomáha vývojárom zostať v ich kreatívnom prúde pri prístupe k výkonným vonkajším schopnostiam.

Od komplexnej integrácie Azure ekosystému po špecializované nástroje ako Playwright pre automatizáciu prehliadača a MarkItDown pre spracovanie dokumentov, tieto servery ukazujú, ako MCP môže zvýšiť produktivitu v rôznych vývojových scenároch. Štandardizovaný protokol zabezpečuje, že tieto nástroje spolupracujú bezproblémovo a vytvárajú koherentný vývojový zážitok.

Ako sa MCP ekosystém ďalej vyvíja, kľúčové bude zostať aktívnym v komunite, skúmať nové servery a vytvárať vlastné riešenia na maximalizáciu vašej vývojovej produktivity. Otvorený štandard MCP znamená, že môžete kombinovať nástroje od rôznych dodávateľov a vytvoriť si ideálny pracovný tok podľa svojich potrieb.

## 🔗 Dodatočné zdroje

- [Oficiálny Microsoft MCP repozitár](https://github.com/microsoft/mcp)
- [MCP komunita a dokumentácia](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentácia](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentácia](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentácia](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP udalosti](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Úžasné prispôsobenia GitHub Copilot](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days naživo 29./30. júla alebo pozrieť na požiadanie](https://aka.ms/mcpdevdays)

## 🎯 Cvičenia

1. **Inštalácia a konfigurácia**: Nastavte jeden z MCP serverov vo vašom VS Code prostredí a otestujte základnú funkčnosť.
2. **Integrácia pracovného toku**: Navrhnite vývojový pracovný tok, ktorý kombinuje aspoň tri rôzne MCP servery.
3. **Plánovanie vlastného servera**: Identifikujte úlohu vo vašom dennom vývojovom režime, ktorá by mohla profitovať z vlastného MCP servera, a vytvorte preň špecifikáciu.
4. **Analýza výkonu**: Porovnajte efektívnosť použitia MCP serverov oproti tradičným prístupom pre bežné vývojové úlohy.
5. **Hodnotenie bezpečnosti**: Zhodnoťte bezpečnostné dôsledky používania MCP serverov vo vašom vývojovom prostredí a navrhnite osvedčené postupy.


Ďalej:[Najlepšie praktiky](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->