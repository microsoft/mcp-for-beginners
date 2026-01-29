# 🚀 10 Microsoft MCP serverov, ktoré menia produktivitu vývojárov

## 🎯 Čo sa v tejto príručke naučíte

Táto praktická príručka predstavuje desať Microsoft MCP serverov, ktoré aktívne menia spôsob, akým vývojári pracujú s AI asistentmi. Namiesto toho, aby sme len vysvetľovali, čo MCP servery *môžu* robiť, ukážeme vám servery, ktoré už dnes skutočne zlepšujú každodenné vývojové pracovné postupy v Microsofte a mimo neho.

Každý server v tejto príručke bol vybraný na základe reálneho používania a spätnej väzby od vývojárov. Objavíte nielen to, čo každý server robí, ale aj prečo je dôležitý a ako z neho vyťažiť maximum vo vlastných projektoch. Či už ste úplný nováčik v MCP, alebo chcete rozšíriť svoje existujúce nastavenie, tieto servery predstavujú niektoré z najpraktickejších a najefektívnejších nástrojov v ekosystéme Microsoftu.

> **💡 Rýchly tip na začiatok**
> 
> Ste nováčik v MCP? Nebojte sa! Táto príručka je navrhnutá tak, aby bola prístupná pre začiatočníkov. Pojmy vysvetlíme priebežne a vždy sa môžete vrátiť k našim modulom [Úvod do MCP](../00-Introduction/README.md) a [Základné koncepty](../01-CoreConcepts/README.md) pre hlbšie pochopenie.

## Prehľad

Táto komplexná príručka skúma desať Microsoft MCP serverov, ktoré revolučne menia spôsob, akým vývojári komunikujú s AI asistentmi a externými nástrojmi. Od správy Azure zdrojov až po spracovanie dokumentov, tieto servery ukazujú silu Model Context Protocol pri vytváraní plynulých a produktívnych vývojových pracovných postupov.

## Ciele učenia

Na konci tejto príručky budete:
- Rozumieť, ako MCP servery zvyšujú produktivitu vývojárov
- Spoznáte najvýznamnejšie implementácie MCP serverov od Microsoftu
- Objavíte praktické použitia pre každý server
- Vedieť, ako tieto servery nastaviť a konfigurovať vo VS Code a Visual Studio
- Preskúmate širší ekosystém MCP a jeho budúce smery

## 🔧 Pochopenie MCP serverov: Príručka pre začiatočníkov

### Čo sú MCP servery?

Ak ste začiatočník v Model Context Protocol (MCP), možno sa pýtate: „Čo presne je MCP server a prečo by ma to malo zaujímať?“ Začnime jednoduchou analógiou.

Predstavte si MCP servery ako špecializovaných asistentov, ktorí pomáhajú vášmu AI kódovaciemu spoločníkovi (napríklad GitHub Copilot) pripojiť sa k externým nástrojom a službám. Rovnako ako používate rôzne aplikácie v telefóne na rôzne úlohy – jednu na počasie, druhú na navigáciu, tretiu na bankovníctvo – MCP servery dávajú vášmu AI asistentovi možnosť komunikovať s rôznymi vývojovými nástrojmi a službami.

### Problém, ktorý MCP servery riešia

Pred MCP servermi, ak ste chceli:
- Skontrolovať svoje Azure zdroje
- Vytvoriť GitHub issue
- Dotazovať sa do databázy
- Vyhľadávať v dokumentácii

museli ste prestať kódovať, otvoriť prehliadač, prejsť na príslušnú stránku a tieto úlohy vykonať manuálne. Neustále prepínanie kontextu narušovalo váš pracovný tok a znižovalo produktivitu.

### Ako MCP servery menia váš vývojový zážitok

S MCP servermi môžete zostať vo svojom vývojovom prostredí (VS Code, Visual Studio a pod.) a jednoducho požiadať AI asistenta, aby tieto úlohy vybavil za vás. Napríklad:

**Namiesto tradičného postupu:**
1. Prestať kódovať  
2. Otvoriť prehliadač  
3. Prejsť na Azure portál  
4. Vyhľadať detaily o storage účte  
5. Vrátiť sa do VS Code  
6. Pokračovať v kódovaní  

**Môžete teraz urobiť toto:**
1. Spýtať sa AI: „Aký je stav mojich Azure storage účtov?“  
2. Pokračovať v kódovaní s poskytnutými informáciami  

### Kľúčové výhody pre začiatočníkov

#### 1. 🔄 **Zostaňte v pracovnom flow**
- Už žiadne prepínanie medzi viacerými aplikáciami  
- Sústreďte sa na kód, ktorý píšete  
- Znížte mentálnu záťaž z riadenia rôznych nástrojov  

#### 2. 🤖 **Používajte prirodzený jazyk namiesto zložitých príkazov**
- Namiesto učenia sa SQL syntaxe popíšte, aké dáta potrebujete  
- Namiesto zapamätania Azure CLI príkazov vysvetlite, čo chcete dosiahnuť  
- Nechajte AI riešiť technické detaily, vy sa sústreďte na logiku  

#### 3. 🔗 **Prepojte viacero nástrojov dohromady**
- Vytvárajte silné pracovné postupy kombinovaním rôznych služieb  
- Príklad: „Získaj všetky nedávne GitHub issues a vytvor zodpovedajúce Azure DevOps work itemy“  
- Automatizujte bez písania zložitých skriptov  

#### 4. 🌐 **Prístup k rastúcemu ekosystému**
- Využívajte servery vytvorené Microsoftom, GitHubom a ďalšími firmami  
- Bezproblémovo kombinujte nástroje od rôznych dodávateľov  
- Pripojte sa k štandardizovanému ekosystému, ktorý funguje naprieč rôznymi AI asistentmi  

#### 5. 🛠️ **Učte sa praxou**
- Začnite s predpripravenými servermi, aby ste pochopili koncepty  
- Postupne si vytvárajte vlastné servery, keď získate istotu  
- Používajte dostupné SDK a dokumentáciu ako sprievodcu  

### Reálny príklad pre začiatočníkov

Povedzme, že ste nováčik vo webovom vývoji a pracujete na svojom prvom projekte. Takto vám MCP servery môžu pomôcť:

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
- **Konzistentnosť**: Podobný zážitok naprieč rôznymi nástrojmi a firmami  
- **Interoperabilita**: Servery od rôznych dodávateľov spolupracujú  
- **Budúca pripravenosť**: Zručnosti a nastavenia sa prenášajú medzi rôznymi AI asistentmi  
- **Komunita**: Veľký ekosystém zdieľaných znalostí a zdrojov  

### Začíname: Čo sa naučíte

V tejto príručke preskúmame 10 Microsoft MCP serverov, ktoré sú obzvlášť užitočné pre vývojárov na všetkých úrovniach. Každý server je navrhnutý tak, aby:  
- Riešil bežné vývojové výzvy  
- Znižoval opakujúce sa úlohy  
- Zlepšoval kvalitu kódu  
- Podporoval možnosti učenia  

> **💡 Tip na učenie**  
> 
> Ak ste úplný nováčik v MCP, začnite s našimi modulmi [Úvod do MCP](../00-Introduction/README.md) a [Základné koncepty](../01-CoreConcepts/README.md). Potom sa sem vráťte a uvidíte tieto koncepty v praxi s reálnymi Microsoft nástrojmi.  
> 
> Pre ďalší kontext o dôležitosti MCP si pozrite príspevok Marie Naggaga: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Začíname s MCP vo VS Code a Visual Studio 🚀

Nastavenie týchto MCP serverov je jednoduché, ak používate Visual Studio Code alebo Visual Studio 2022 s GitHub Copilot.

### Nastavenie vo VS Code

Základný postup pre VS Code:

1. **Povoliť Agent Mode**: Vo VS Code prepnite do Agent módu v okne Copilot Chat  
2. **Konfigurovať MCP servery**: Pridajte konfigurácie serverov do súboru settings.json vo VS Code  
3. **Spustiť servery**: Kliknite na tlačidlo „Start“ pri každom serveri, ktorý chcete používať  
4. **Vybrať nástroje**: Zvoľte, ktoré MCP servery chcete povoliť pre aktuálnu reláciu  

Pre podrobné inštrukcie pozrite [dokumentáciu MCP pre VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profesionálny tip: Spravujte MCP servery ako expert!**  
> 
> Zobrazenie rozšírení vo VS Code teraz obsahuje [praktické nové rozhranie na správu nainštalovaných MCP serverov](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Máte rýchly prístup na spustenie, zastavenie a správu akýchkoľvek MCP serverov cez prehľadné a jednoduché rozhranie. Vyskúšajte to!

### Nastavenie vo Visual Studio 2022

Pre Visual Studio 2022 (verzia 17.14 alebo novšia):

1. **Povoliť Agent Mode**: Kliknite na rozbaľovaciu ponuku „Ask“ v okne GitHub Copilot Chat a vyberte „Agent“  
2. **Vytvoriť konfiguračný súbor**: Vytvorte súbor `.mcp.json` v adresári riešenia (odporúčané miesto: `<SOLUTIONDIR>\.mcp.json`)  
3. **Konfigurovať servery**: Pridajte konfigurácie MCP serverov podľa štandardného MCP formátu  
4. **Schválenie nástrojov**: Po výzve schváľte nástroje, ktoré chcete používať, s príslušnými oprávneniami  

Pre podrobné inštrukcie k Visual Studio pozrite [dokumentáciu MCP pre Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Každý MCP server má svoje vlastné požiadavky na konfiguráciu (pripojovacie reťazce, autentifikácia a pod.), ale vzor nastavenia je konzistentný v oboch IDE.

## Poučenie z Microsoft MCP serverov 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Čo robí**: Microsoft Learn Docs MCP Server je cloudová služba, ktorá poskytuje AI asistentom prístup v reálnom čase k oficiálnej dokumentácii Microsoftu cez Model Context Protocol. Pripája sa na `https://learn.microsoft.com/api/mcp` a umožňuje sémantické vyhľadávanie naprieč Microsoft Learn, dokumentáciou Azure, Microsoft 365 a ďalšími oficiálnymi zdrojmi Microsoftu.

**Prečo je užitočný**: Aj keď sa môže zdať, že ide len o „dokumentáciu“, tento server je kľúčový pre každého vývojára používajúceho technológie Microsoftu. Jednou z najväčších sťažností .NET vývojárov na AI kódovacích asistentov je, že nie sú aktuálni s najnovšími vydaniami .NET a C#. Microsoft Learn Docs MCP Server to rieši tým, že poskytuje prístup v reálnom čase k najnovšej dokumentácii, referenciám API a osvedčeným postupom. Či už pracujete s najnovšími Azure SDK, skúmate nové funkcie C# 13 alebo implementujete moderné .NET Aspire vzory, tento server zabezpečuje, že váš AI asistent má prístup k autoritatívnym a aktuálnym informáciám potrebným na generovanie presného a moderného kódu.

**Reálne použitie**: „Aké sú az cli príkazy na vytvorenie Azure container app podľa oficiálnej Microsoft Learn dokumentácie?“ alebo „Ako nakonfigurovať Entity Framework s dependency injection v ASP.NET Core?“ Alebo „Skontroluj tento kód, či zodpovedá odporúčaniam na výkon v Microsoft Learn dokumentácii.“ Server poskytuje komplexné pokrytie Microsoft Learn, Azure dokumentácie a Microsoft 365 pomocou pokročilého sémantického vyhľadávania, ktoré nájde najrelevantnejšie informácie v kontexte. Vracia až 10 kvalitných obsahových blokov s názvami článkov a URL, vždy pristupujúc k najnovšej dokumentácii Microsoftu hneď po jej zverejnení.

**Ukážkový príklad**: Server sprístupňuje nástroj `microsoft_docs_search`, ktorý vykonáva sémantické vyhľadávanie v oficiálnej technickej dokumentácii Microsoftu. Po konfigurácii môžete klásť otázky ako „Ako implementovať JWT autentifikáciu v ASP.NET Core?“ a dostať podrobné, oficiálne odpovede s odkazmi na zdroje. Kvalita vyhľadávania je výnimočná, pretože rozumie kontextu – otázka o „containers“ v Azure kontexte vráti dokumentáciu Azure Container Instances, zatiaľ čo ten istý pojem v .NET kontexte vráti relevantné informácie o C# kolekciách.

Toto je obzvlášť užitočné pre rýchlo sa meniace alebo nedávno aktualizované knižnice a použitia. Napríklad v niektorých nedávnych projektoch som chcel využiť funkcie v najnovších vydaniach .NET Aspire a Microsoft.Extensions.AI. Vďaka zahrnutiu Microsoft Learn Docs MCP servera som mohol využiť nielen API dokumentáciu, ale aj návody a odporúčania, ktoré boli práve zverejnené.
> **💡 Profesionálna rada**
> 
> Aj modely priateľské k nástrojom potrebujú motiváciu na používanie MCP nástrojov! Zvážte pridanie systémového promptu alebo [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) napríklad: „Máte prístup k `microsoft.docs.mcp` – použite tento nástroj na vyhľadávanie najnovšej oficiálnej dokumentácie Microsoftu pri riešení otázok o technológiách Microsoft, ako sú C#, Azure, ASP.NET Core alebo Entity Framework.“
> 
> Pre skvelý príklad toho, ako to funguje v praxi, si pozrite [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) z repozitára Awesome GitHub Copilot. Tento režim špecificky využíva MCP server Microsoft Learn Docs na pomoc s čistením a modernizáciou C# kódu pomocou najnovších vzorov a osvedčených postupov.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Čo to robí**: Azure MCP Server je komplexná sada viac ako 15 špecializovaných konektorov pre Azure služby, ktoré prinášajú celý Azure ekosystém priamo do vášho AI pracovného toku. Nie je to len jeden server – je to výkonná zbierka, ktorá zahŕňa správu zdrojov, pripojenie k databázam (PostgreSQL, SQL Server), analýzu logov Azure Monitor pomocou KQL, integráciu Cosmos DB a mnoho ďalšieho.

**Prečo je to užitočné**: Okrem správy Azure zdrojov tento server výrazne zlepšuje kvalitu kódu pri práci s Azure SDK. Keď používate Azure MCP v režime Agenta, nepomáha vám len písať kód – pomáha vám písať *lepšie* Azure kódy, ktoré dodržiavajú aktuálne vzory autentifikácie, najlepšie postupy spracovania chýb a využívajú najnovšie funkcie SDK. Namiesto generického kódu, ktorý môže fungovať, dostanete kód, ktorý nasleduje odporúčané vzory Azure pre produkčné nasadenia.

**Kľúčové moduly zahŕňajú**:
- **🗄️ Konektory databáz**: Priamy prístup v prirodzenom jazyku k Azure Database pre PostgreSQL a SQL Server
- **📊 Azure Monitor**: Analýza logov a prevádzkové prehľady poháňané KQL
- **🌐 Správa zdrojov**: Kompletná správa životného cyklu Azure zdrojov
- **🔐 Autentifikácia**: Vzory DefaultAzureCredential a managed identity
- **📦 Služby ukladania**: Operácie s Blob Storage, Queue Storage a Table Storage
- **🚀 Služby kontajnerov**: Správa Azure Container Apps, Container Instances a AKS
- **A mnoho ďalších špecializovaných konektorov**

**Praktické použitie**: „Zobraz moje Azure storage účty“, „Dotazuj sa na chyby v mojom Log Analytics workspace za poslednú hodinu“ alebo „Pomôž mi vytvoriť Azure aplikáciu v Node.js s riadnou autentifikáciou“

**Kompletný demo scenár**: Tu je kompletný prehľad, ktorý ukazuje silu kombinácie Azure MCP s rozšírením GitHub Copilot pre Azure vo VS Code. Keď máte oboje nainštalované a zadáte:

> „Vytvor Python skript, ktorý nahraje súbor do Azure Blob Storage pomocou autentifikácie DefaultAzureCredential. Skript by sa mal pripojiť k môjmu Azure storage účtu s názvom 'mycompanystorage', nahrať do kontajnera 'documents', vytvoriť testovací súbor s aktuálnym časovým pečiatkom na nahranie, spracovať chyby elegantne a poskytnúť informatívny výstup, dodržiavať najlepšie postupy Azure pre autentifikáciu a spracovanie chýb, obsahovať komentáre vysvetľujúce, ako funguje autentifikácia DefaultAzureCredential, a byť dobre štruktúrovaný so správnymi funkciami a dokumentáciou.“

Azure MCP Server vygeneruje kompletný, produkčne pripravený Python skript, ktorý:
- Používa najnovšie Azure Blob Storage SDK s riadnymi asynchrónnymi vzormi
- Implementuje DefaultAzureCredential s podrobným vysvetlením fallback reťazca
- Obsahuje robustné spracovanie chýb so špecifickými typmi výnimiek Azure
- Dodržiava najlepšie postupy Azure SDK pre správu zdrojov a pripojení
- Poskytuje detailné logovanie a informatívny výstup do konzoly
- Vytvára správne štruktúrovaný skript s funkciami, dokumentáciou a typovými anotáciami

Čo je na tom pozoruhodné, je fakt, že bez Azure MCP by ste mohli dostať generický kód pre blob storage, ktorý síce funguje, ale nedodržiava aktuálne Azure vzory. S Azure MCP dostanete kód, ktorý využíva najnovšie autentifikačné metódy, rieši špecifické chybové scenáre Azure a nasleduje odporúčané postupy Microsoftu pre produkčné aplikácie.

**Ukážkový príklad**: Mal som problém si zapamätať konkrétne príkazy pre `az` a `azd` CLI na ad-hoc použitie. Vždy to pre mňa bola dvojkroková záležitosť: najprv si vyhľadať syntax, potom spustiť príkaz. Často som radšej skočil do portálu a klikal, aby som prácu dokončil, pretože som nechcel priznať, že si syntax CLI nepamätám. Možnosť jednoducho opísať, čo chcem, je úžasná, a ešte lepšie je to vedieť urobiť priamo v IDE!

Skvelý zoznam prípadov použitia nájdete v [Azure MCP repozitári](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server), ktorý vám pomôže začať. Pre komplexné návody na nastavenie a pokročilé možnosti konfigurácie si pozrite [oficiálnu dokumentáciu Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Čo to robí**: Oficiálny GitHub MCP Server poskytuje bezproblémovú integráciu s celým ekosystémom GitHub, ponúkajúc možnosti hosťovaného vzdialeného prístupu aj lokálneho nasadenia cez Docker. Nejde len o základné operácie s repozitármi – je to komplexný nástroj, ktorý zahŕňa správu GitHub Actions, workflow pre pull requesty, sledovanie issues, bezpečnostné skenovanie, notifikácie a pokročilé automatizačné funkcie.

**Prečo je to užitočné**: Tento server mení spôsob, akým pracujete s GitHubom, tým, že prináša plnohodnotný zážitok platformy priamo do vášho vývojového prostredia. Namiesto neustáleho prepínania medzi VS Code a GitHub.com pre správu projektov, revízie kódu a monitorovanie CI/CD môžete všetko riešiť pomocou príkazov v prirodzenom jazyku a sústrediť sa na kód.

> **ℹ️ Poznámka: Rôzne typy 'Agentov'**
> 
> Nezamieňajte si tento GitHub MCP Server s GitHub Coding Agentom (AI agentom, ktorému môžete priradiť issues na automatizované kódovanie). GitHub MCP Server funguje v režime Agenta vo VS Code a poskytuje integráciu GitHub API, zatiaľ čo GitHub Coding Agent je samostatná funkcia, ktorá vytvára pull requesty, keď je priradený k GitHub issues.

**Kľúčové funkcie zahŕňajú**:
- **⚙️ GitHub Actions**: Kompletná správa CI/CD pipeline, monitorovanie workflow a správa artefaktov
- **🔀 Pull Requests**: Vytváranie, revízia, zlúčenie a správa PR s detailným sledovaním stavu
- **🐛 Issues**: Kompletná správa životného cyklu issues, komentovanie, označovanie a priraďovanie
- **🔒 Bezpečnosť**: Upozornenia na skenovanie kódu, detekcia tajomstiev a integrácia Dependabot
- **🔔 Notifikácie**: Inteligentná správa notifikácií a kontrola prihlásenia na repozitáre
- **📁 Správa repozitárov**: Operácie so súbormi, správa vetiev a administrácia repozitárov
- **👥 Spolupráca**: Vyhľadávanie používateľov a organizácií, správa tímov a kontrola prístupov

**Praktické použitie**: „Vytvor pull request z mojej feature vetvy“, „Ukáž mi všetky neúspešné CI behy tento týždeň“, „Zobraz otvorené bezpečnostné upozornenia pre moje repozitáre“ alebo „Nájdi všetky issues priradené mne naprieč mojimi organizáciami“

**Kompletný demo scenár**: Tu je silný pracovný tok, ktorý demonštruje schopnosti GitHub MCP Servera:

> „Potrebujem sa pripraviť na náš sprint review. Ukáž mi všetky pull requesty, ktoré som tento týždeň vytvoril, skontroluj stav našich CI/CD pipeline, vytvor súhrn bezpečnostných upozornení, ktoré treba riešiť, a pomôž mi zostaviť poznámky k vydaniu na základe zlúčených PR s označením 'feature'.“

GitHub MCP Server:
- Získa vaše nedávne pull requesty s detailnými informáciami o stave
- Analyzuje behy workflow a zvýrazní prípadné zlyhania alebo problémy s výkonom
- Zostaví výsledky bezpečnostného skenovania a uprednostní kritické upozornenia
- Vygeneruje komplexné poznámky k vydaniu extrahovaním informácií zo zlúčených PR
- Poskytne konkrétne ďalšie kroky pre plánovanie sprintu a prípravu vydania

**Ukážkový príklad**: Rád používam tento nástroj na workflow revízie kódu. Namiesto preskakovania medzi VS Code, GitHub notifikáciami a stránkami pull requestov môžem povedať „Ukáž mi všetky PR čakajúce na moju revíziu“ a potom „Pridaj komentár k PR #123 ohľadom spracovania chýb v autentifikačnej metóde.“ Server spracuje volania GitHub API, udrží kontext diskusie a dokonca mi pomôže vytvoriť konštruktívnejšie komentáre k revízii.

**Možnosti autentifikácie**: Server podporuje OAuth (bezproblémovo vo VS Code) aj Personal Access Tokens, s konfigurovateľnými nástrojmi, ktoré umožňujú povoliť len tie GitHub funkcie, ktoré potrebujete. Môžete ho spustiť ako vzdialenú hosťovanú službu pre rýchle nastavenie alebo lokálne cez Docker pre úplnú kontrolu.

> **💡 Tip na použitie**
> 
> Povoliť len tie nástroje, ktoré potrebujete, konfiguráciou parametra `--toolsets` v nastaveniach MCP servera, aby ste znížili veľkosť kontextu a zlepšili výber AI nástrojov. Napríklad pridajte `"--toolsets", "repos,issues,pull_requests,actions"` do argumentov konfigurácie MCP pre základné vývojové workflow, alebo použite `"--toolsets", "notifications, security"`, ak chcete primárne monitorovať GitHub.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Čo to robí**: Pripája sa k Azure DevOps službám pre komplexnú správu projektov, sledovanie pracovných položiek, správu build pipeline a operácie s repozitármi.

**Prečo je to užitočné**: Pre tímy, ktoré používajú Azure DevOps ako svoju hlavnú DevOps platformu, tento MCP server eliminuje neustále prepínanie medzi vývojovým prostredím a webovým rozhraním Azure DevOps. Môžete spravovať pracovné položky, kontrolovať stav buildov, dotazovať sa na repozitáre a riešiť úlohy projektového manažmentu priamo cez svojho AI asistenta.

**Praktické použitie**: „Ukáž mi všetky aktívne pracovné položky v aktuálnom sprinte pre projekt WebApp“, „Vytvor hlásenie o chybe pre problém s prihlásením, ktorý som práve našiel“ alebo „Skontroluj stav našich build pipeline a ukáž mi posledné zlyhania“

**Ukážkový príklad**: Jednoducho si môžete skontrolovať stav aktuálneho sprintu tímu pomocou jednoduchého dotazu ako „Ukáž mi všetky aktívne pracovné položky v aktuálnom sprinte pre projekt WebApp“ alebo „Vytvor hlásenie o chybe pre problém s prihlásením, ktorý som práve našiel“ bez opustenia vývojového prostredia.

### 5. 📝 MarkItDown MCP Server
[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Čo to robí**: MarkItDown je komplexný server na konverziu dokumentov, ktorý prevádza rôzne formáty súborov na kvalitný Markdown, optimalizovaný pre spracovanie LLM a pracovné postupy analýzy textu.

**Prečo je to užitočné**: Nevyhnutné pre moderné pracovné postupy dokumentácie! MarkItDown zvláda širokú škálu formátov súborov a pritom zachováva dôležitú štruktúru dokumentu, ako sú nadpisy, zoznamy, tabuľky a odkazy. Na rozdiel od jednoduchých nástrojov na extrakciu textu sa zameriava na udržanie sémantického významu a formátovania, ktoré sú cenné pre spracovanie AI aj pre ľudskú čitateľnosť.

**Podporované formáty súborov**:
- **Office dokumenty**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Mediálne súbory**: Obrázky (s EXIF metadátami a OCR), Audio (s EXIF metadátami a prepisom reči)
- **Webový obsah**: HTML, RSS kanály, YouTube URL, stránky Wikipédie
- **Dátové formáty**: CSV, JSON, XML, ZIP súbory (rekurzívne spracováva obsah)
- **Publikačné formáty**: EPub, Jupyter notebooky (.ipynb)
- **Emaily**: Outlook správy (.msg)
- **Pokročilé**: Integrácia Azure Document Intelligence pre vylepšené spracovanie PDF

**Pokročilé funkcie**: MarkItDown podporuje popisy obrázkov poháňané LLM (ak je k dispozícii OpenAI klient), Azure Document Intelligence pre lepšie spracovanie PDF, prepis reči z audio obsahu a systém pluginov na rozšírenie o ďalšie formáty súborov.

**Reálne použitie**: „Preveď túto PowerPoint prezentáciu do Markdownu pre náš dokumentačný web“, „Extrahuj text z tohto PDF so správnou štruktúrou nadpisov“ alebo „Premeň tento Excel súbor na čitateľnú tabuľku“.

**Ukážkový príklad**: Citujem z [MarkItDown dokumentácie](https://github.com/microsoft/markitdown#why-markdown):

> Markdown je veľmi blízky obyčajnému textu, s minimálnym značením alebo formátovaním, no stále poskytuje spôsob, ako reprezentovať dôležitú štruktúru dokumentu. Hlavné LLM, ako napríklad OpenAI GPT-4o, natívne „rozumejú“ Markdownu a často ho do svojich odpovedí automaticky začleňujú. To naznačuje, že boli trénované na obrovskom množstve textov vo formáte Markdown a dobre mu rozumejú. Ako vedľajší efekt sú Markdown konvencie veľmi efektívne z hľadiska tokenov.

MarkItDown je naozaj dobrý v zachovaní štruktúry dokumentu, čo je dôležité pre AI pracovné postupy. Napríklad pri konverzii PowerPoint prezentácie zachováva organizáciu snímok s vhodnými nadpismi, extrahuje tabuľky ako Markdown tabuľky, pridáva alt text k obrázkom a dokonca spracováva poznámky rečníka. Grafy sa premenia na čitateľné dátové tabuľky a výsledný Markdown zachováva logický tok pôvodnej prezentácie. To je ideálne na napájanie obsahu prezentácií do AI systémov alebo na tvorbu dokumentácie z existujúcich snímok.

### 6. 🗃️ SQL Server MCP Server

[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Čo to robí**: Poskytuje konverzačný prístup k SQL Server databázam (on-premises, Azure SQL alebo Fabric)

**Prečo je to užitočné**: Podobné ako PostgreSQL server, ale pre Microsoft SQL ekosystém. Pripojte sa jednoduchým connection stringom a začnite klásť otázky v prirodzenom jazyku – žiadne prepínanie kontextu!

**Reálne použitie**: „Nájdi všetky objednávky, ktoré neboli splnené za posledných 30 dní“ sa preloží do vhodných SQL dotazov a vráti naformátované výsledky.

**Ukážkový príklad**: Po nastavení pripojenia k databáze môžete okamžite začať komunikovať s vašimi dátami. Blogový príspevok to ukazuje na jednoduchej otázke: „Na ktorú databázu ste pripojený?“ MCP server odpovie vyvolaním príslušného databázového nástroja, pripojí sa k vašej SQL Server inštancii a vráti detaily o aktuálnom pripojení – všetko bez písania jediného riadku SQL. Server podporuje komplexné databázové operácie od správy schémy až po manipuláciu s dátami, všetko cez prirodzené jazykové príkazy. Kompletné inštrukcie na nastavenie a príklady konfigurácie s VS Code a Claude Desktop nájdete tu: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Čo to robí**: Umožňuje AI agentom interagovať s webovými stránkami na testovanie a automatizáciu

> **ℹ️ Poháňa GitHub Copilot**
> 
> Playwright MCP Server poháňa Coding Agenta GitHub Copilota, ktorý tak získava schopnosť prehliadať web! [Viac o tejto funkcii](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Prečo je to užitočné**: Ideálne pre automatizované testovanie riadené prirodzeným jazykom. AI môže prechádzať weby, vypĺňať formuláre a extrahovať dáta cez štruktúrované snímky prístupnosti – to je neuveriteľne silná funkcia!

**Reálne použitie**: „Otestuj prihlasovací proces a over, či sa správne načíta dashboard“ alebo „Vygeneruj test, ktorý vyhľadá produkty a overí stránku s výsledkami“ – to všetko bez potreby zdrojového kódu aplikácie.

**Ukážkový príklad**: Moja kolegyňa Debbie O'Brien v poslednej dobe odvádza skvelú prácu s Playwright MCP Serverom! Napríklad nedávno ukázala, ako môžete vygenerovať kompletné Playwright testy bez prístupu k zdrojovému kódu aplikácie. V jej scenári požiadala Copilota o test pre aplikáciu na vyhľadávanie filmov: prejsť na stránku, vyhľadať „Garfield“ a overiť, že sa film zobrazil vo výsledkoch. MCP spustil prehliadač, preskúmal štruktúru stránky pomocou DOM snímok, našiel správne selektory a vygeneroval plne funkčný TypeScript test, ktorý prešiel na prvý pokus.

Čo robí toto naozaj silným, je premostenie medzery medzi inštrukciami v prirodzenom jazyku a vykonateľným testovacím kódom. Tradičné prístupy vyžadujú buď manuálne písanie testov, alebo prístup k zdrojovému kódu pre kontext. S Playwright MCP však môžete testovať externé stránky, klientské aplikácie alebo pracovať v black-box testovacích scenároch, kde prístup ku kódu nie je možný.

### 8. 💻 Dev Box MCP Server

[![Inštalovať vo VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Inštalovať vo VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Čo to robí**: Spravuje Microsoft Dev Box prostredia pomocou prirodzeného jazyka

**Prečo je to užitočné**: Výrazne zjednodušuje správu vývojových prostredí! Vytvárajte, konfigurujte a spravujte vývojové prostredia bez nutnosti pamätať si konkrétne príkazy.

**Reálne použitie**: „Nastav nový Dev Box s najnovším .NET SDK a nakonfiguruj ho pre náš projekt“, „Skontroluj stav všetkých mojich vývojových prostredí“ alebo „Vytvor štandardizované demo prostredie pre naše tímové prezentácie“.

**Ukážkový príklad**: Som veľkým fanúšikom používania Dev Boxu na osobný vývoj. Môj moment „aha“ nastal, keď James Montemagno vysvetlil, aký je Dev Box skvelý na konferenčné demo, pretože má superrýchle ethernetové pripojenie bez ohľadu na wifi v hoteli, na konferencii alebo v lietadle. V skutočnosti som nedávno cvičil konferenčné demo, keď bol môj laptop pripojený cez hotspot telefónu počas jazdy autobusom z Bruggy do Antverp! Môj ďalší krok je viac sa venovať správe viacerých vývojových prostredí v tíme a štandardizovaným demo prostrediam. Ďalším veľkým prípadom použitia, o ktorom počúvam od zákazníkov a kolegov, je používanie Dev Boxu na predkonfigurované vývojové prostredia. V oboch prípadoch použitie MCP na konfiguráciu a správu Dev Boxov umožňuje interakciu v prirodzenom jazyku, pričom zostávate vo svojom vývojovom prostredí.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Čo to robí**: Azure AI Foundry MCP Server poskytuje vývojárom komplexný prístup k AI ekosystému Azure, vrátane katalógov modelov, správy nasadenia, indexovania znalostí pomocou Azure AI Search a nástrojov na hodnotenie. Tento experimentálny server prekladá priepasť medzi vývojom AI a výkonnou AI infraštruktúrou Azure, čím uľahčuje tvorbu, nasadenie a hodnotenie AI aplikácií.

**Prečo je to užitočné**: Tento server mení spôsob, akým pracujete so službami Azure AI, tým, že prináša podnikové AI funkcie priamo do vášho vývojového workflow. Namiesto prepínania medzi Azure portálom, dokumentáciou a IDE môžete objavovať modely, nasadzovať služby, spravovať znalostné bázy a hodnotiť výkon AI pomocou príkazov v prirodzenom jazyku. Je obzvlášť silný pre vývojárov, ktorí vytvárajú RAG (Retrieval-Augmented Generation) aplikácie, spravujú viacmodelové nasadenia alebo implementujú komplexné hodnotiace pipeline pre AI.

**Kľúčové schopnosti pre vývojárov**:
- **🔍 Objavovanie a nasadenie modelov**: Preskúmajte katalóg modelov Azure AI Foundry, získajte podrobné informácie o modeloch s ukážkami kódu a nasadzujte modely do Azure AI Services
- **📚 Správa znalostí**: Vytvárajte a spravujte indexy v Azure AI Search, pridávajte dokumenty, konfigurujte indexery a budujte sofistikované RAG systémy
- **⚡ Integrácia AI agentov**: Pripojte sa k Azure AI Agentom, dotazujte sa na existujúcich agentov a hodnotte ich výkon v produkčných scenároch
- **📊 Hodnotiaci rámec**: Spúšťajte komplexné hodnotenia textov a agentov, generujte markdown reporty a implementujte kontrolu kvality AI aplikácií
- **🚀 Nástroje na prototypovanie**: Získajte inštrukcie na nastavenie prototypovania cez GitHub a prístup k Azure AI Foundry Labs pre najmodernejšie výskumné modely

**Reálne použitie vývojárom**: „Nasadiť model Phi-4 do Azure AI Services pre moju aplikáciu“, „Vytvoriť nový vyhľadávací index pre môj dokumentačný RAG systém“, „Hodnotiť odpovede môjho agenta podľa kvalitatívnych metrík“ alebo „Nájsť najlepší model na uvažovanie pre moje komplexné analytické úlohy“

**Plný demo scenár**: Tu je silný AI vývojový workflow:

> „Vytváram zákazníckeho podporného agenta. Pomôž mi nájsť dobrý model na uvažovanie v katalógu, nasadiť ho do Azure AI Services, vytvoriť znalostnú bázu z našej dokumentácie, nastaviť hodnotiaci rámec na testovanie kvality odpovedí a potom mi pomôž s prototypovaním integrácie s GitHub tokenom na testovanie.“

Azure AI Foundry MCP Server:
- Dotáže sa katalógu modelov a odporučí optimálne modely na uvažovanie podľa tvojich požiadaviek
- Poskytne príkazy na nasadenie a informácie o kvótach pre preferovaný Azure región
- Nastaví Azure AI Search indexy s vhodnou schémou pre tvoju dokumentáciu
- Nakonfiguruje hodnotiace pipeline s metrikami kvality a bezpečnostnými kontrolami
- Vygeneruje prototypovací kód s GitHub autentifikáciou na okamžité testovanie
- Poskytne komplexné návody na nastavenie prispôsobené tvojmu technologickému stacku

**Ukážkový príklad**: Ako vývojár som mal problém držať krok s rôznymi dostupnými LLM modelmi. Poznám pár hlavných, ale mal som pocit, že mi unikajú možnosti zvýšenia produktivity a efektivity. Tokeny a kvóty sú stresujúce a ťažko sa s nimi manažuje – nikdy neviem, či vyberám správny model na správnu úlohu alebo či neplytvám rozpočtom. Počul som o tomto MCP Serveri od Jamesa Montemagna, keď som sa pýtal kolegov na odporúčania MCP Serverov pre tento príspevok, a som nadšený, že ho môžem vyskúšať! Funkcie na objavovanie modelov vyzerajú obzvlášť pôsobivo pre niekoho ako ja, kto chce preskúmať viac než len bežné modely a nájsť tie optimalizované na špecifické úlohy. Hodnotiaci rámec by mi mal pomôcť overiť, že skutočne dosahujem lepšie výsledky, nie len skúšam niečo nové pre samotné skúšanie.

> **ℹ️ Experimentálny stav**
> 
> Tento MCP server je experimentálny a aktívne sa vyvíja. Funkcie a API sa môžu meniť. Ideálny na skúmanie možností Azure AI a tvorbu prototypov, ale pre produkčné použitie overte stabilitu.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Čo to robí**: Poskytuje vývojárom základné nástroje na tvorbu AI agentov a aplikácií, ktoré sa integrujú s Microsoft 365 a Microsoft 365 Copilot, vrátane validácie schém, získavania ukážkového kódu a pomoci pri riešení problémov.

**Prečo je to užitočné**: Vývoj pre Microsoft 365 a Copilot zahŕňa zložité manifestové schémy a špecifické vývojové vzory. Tento MCP server prináša základné vývojové zdroje priamo do vášho kódovacieho prostredia, pomáha vám validovať schémy, nájsť ukážkový kód a riešiť bežné problémy bez neustáleho odkazovania na dokumentáciu.

**Reálne použitie**: „Validuj môj deklaratívny manifest agenta a oprav chyby v schéme“, „Ukáž mi ukážkový kód na implementáciu pluginu Microsoft Graph API“ alebo „Pomôž mi vyriešiť problémy s autentifikáciou mojej Teams aplikácie“

**Ukážkový príklad**: Po rozhovore s priateľom Johnom Millerom na konferencii Build o M365 Agents mi odporučil tento MCP. Môže byť skvelý pre vývojárov, ktorí sú v M365 Agents noví, pretože poskytuje šablóny, ukážkový kód a základné štruktúry na rýchly štart bez zahltenia dokumentáciou. Funkcie validácie schém vyzerajú obzvlášť užitočne na predchádzanie chybám v štruktúre manifestu, ktoré môžu spôsobiť hodiny ladenia.

> **💡 Tip**
> 
> Používajte tento server spolu s Microsoft Learn Docs MCP Serverom pre komplexnú podporu vývoja M365 – jeden poskytuje oficiálnu dokumentáciu, druhý praktické nástroje a pomoc pri riešení problémov.

## Čo ďalej? 🔮

## 📋 Záver

Model Context Protocol (MCP) mení spôsob, akým vývojári komunikujú s AI asistentmi a externými nástrojmi. Týchto 10 Microsoft MCP serverov ukazuje silu štandardizovanej AI integrácie, ktorá umožňuje plynulé workflow, ktoré udržujú vývojárov v ich pracovnom flow a zároveň poskytujú prístup k výkonným externým funkciám.

Od komplexnej integrácie Azure ekosystému až po špecializované nástroje ako Playwright pre automatizáciu prehliadača a MarkItDown pre spracovanie dokumentov, tieto servery ukazujú, ako MCP môže zvýšiť produktivitu v rôznych vývojových scenároch. Štandardizovaný protokol zabezpečuje, že tieto nástroje spolupracujú bez problémov a vytvárajú jednotný vývojový zážitok.

Ako sa MCP ekosystém ďalej vyvíja, kľúčové bude zostať aktívne zapojený v komunite, skúmať nové servery a vytvárať vlastné riešenia na maximalizáciu vašej vývojovej produktivity. Otvorená štandardná povaha MCP znamená, že môžete kombinovať nástroje od rôznych dodávateľov a vytvoriť si ideálny workflow pre svoje konkrétne potreby.

## 🔗 Dodatočné zdroje

- [Oficiálne Microsoft MCP úložisko](https://github.com/microsoft/mcp)
- [MCP komunita a dokumentácia](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentácia](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentácia](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentácia](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP udalosti](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29./30. júla alebo pozrite na požiadanie](https://aka.ms/mcpdevdays)

## 🎯 Cvičenia

1. **Inštalácia a konfigurácia**: Nastavte jeden z MCP serverov vo vašom VS Code prostredí a otestujte základnú funkcionalitu.
2. **Integrácia workflow**: Navrhnite vývojový workflow, ktorý kombinuje aspoň tri rôzne MCP servery.
3. **Plánovanie vlastného servera**: Identifikujte úlohu vo vašej každodennej vývojovej rutine, ktorá by mohla profitovať z vlastného MCP servera, a vytvorte jej špecifikáciu.
4. **Analýza výkonu**: Porovnajte efektivitu používania MCP serverov oproti tradičným prístupom pri bežných vývojových úlohách.
5. **Hodnotenie bezpečnosti**: Zhodnoťte bezpečnostné dôsledky používania MCP serverov vo vašom vývojovom prostredí a navrhnite najlepšie postupy.

Next:[Best Practices](../08-BestPractices/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.