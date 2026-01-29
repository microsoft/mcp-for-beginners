# 🚀 10 Microsoft MCP serverů, které mění produktivitu vývojářů

## 🎯 Co se v tomto průvodci naučíte

Tento praktický průvodce představuje deset Microsoft MCP serverů, které aktivně mění způsob, jakým vývojáři pracují s AI asistenty. Místo pouhého vysvětlování, co MCP servery *mohou* dělat, vám ukážeme servery, které už skutečně ovlivňují každodenní vývojové pracovní postupy v Microsoftu i mimo něj.

Každý server v tomto průvodci byl vybrán na základě reálného používání a zpětné vazby od vývojářů. Dozvíte se nejen, co každý server dělá, ale také proč je důležitý a jak z něj vytěžit maximum ve svých vlastních projektech. Ať už jste v MCP úplný začátečník, nebo chcete rozšířit své stávající nastavení, tyto servery představují některé z nejpraktických a nejefektivnějších nástrojů v ekosystému Microsoftu.

> **💡 Rychlý tip na start**
> 
> Jste v MCP nováček? Nebojte se! Tento průvodce je navržen tak, aby byl přívětivý i pro začátečníky. Vysvětlíme pojmy postupně a kdykoliv se můžete vrátit k našim modulům [Úvod do MCP](../00-Introduction/README.md) a [Základní koncepty](../01-CoreConcepts/README.md) pro hlubší pochopení.

## Přehled

Tento komplexní průvodce zkoumá deset Microsoft MCP serverů, které revolučně mění způsob, jakým vývojáři komunikují s AI asistenty a externími nástroji. Od správy Azure zdrojů po zpracování dokumentů – tyto servery ukazují sílu Model Context Protocol při vytváření plynulých a produktivních vývojových workflow.

## Cíle učení

Na konci tohoto průvodce budete:
- Rozumět tomu, jak MCP servery zvyšují produktivitu vývojářů
- Seznámeni s nejvlivnějšími implementacemi MCP serverů od Microsoftu
- Objevovat praktické scénáře použití každého serveru
- Vědět, jak tyto servery nastavit a konfigurovat ve VS Code a Visual Studiu
- Prozkoumat širší MCP ekosystém a jeho budoucí směřování

## 🔧 Pochopení MCP serverů: Průvodce pro začátečníky

### Co jsou MCP servery?

Jako začátečník v Model Context Protocol (MCP) si možná říkáte: „Co přesně je MCP server a proč by mě to mělo zajímat?“ Začněme jednoduchou analogií.

Představte si MCP servery jako specializované asistenty, kteří pomáhají vašemu AI kódovacímu společníkovi (například GitHub Copilot) připojit se k externím nástrojům a službám. Stejně jako na telefonu používáte různé aplikace pro různé úkoly – jednu na počasí, druhou na navigaci, třetí na bankovnictví – MCP servery dávají vašemu AI asistentovi schopnost komunikovat s různými vývojářskými nástroji a službami.

### Problém, který MCP servery řeší

Před MCP servery, pokud jste chtěli:
- Zkontrolovat své Azure zdroje
- Vytvořit GitHub issue
- Dotázat se databáze
- Prohledat dokumentaci

museli jste přestat kódovat, otevřít prohlížeč, přejít na příslušnou stránku a tyto úkoly provést ručně. Neustálé přepínání kontextu narušovalo váš pracovní tok a snižovalo produktivitu.

### Jak MCP servery mění váš vývojářský zážitek

S MCP servery můžete zůstat ve svém vývojovém prostředí (VS Code, Visual Studio atd.) a jednoduše požádat AI asistenta, aby tyto úkoly vyřešil za vás. Například:

**Místo tradičního postupu:**
1. Přestat kódovat
2. Otevřít prohlížeč
3. Přejít do Azure portálu
4. Vyhledat detaily o storage účtu
5. Vrátit se do VS Code
6. Pokračovat v kódování

**Můžete nyní udělat toto:**
1. Zeptat se AI: „Jaký je stav mých Azure storage účtů?“
2. Pokračovat v kódování s poskytnutými informacemi

### Klíčové výhody pro začátečníky

#### 1. 🔄 **Zůstaňte v pracovním flow**
- Už žádné přepínání mezi různými aplikacemi
- Soustřeďte se na psaní kódu
- Snižte mentální zátěž spojenou s ovládáním různých nástrojů

#### 2. 🤖 **Používejte přirozený jazyk místo složitých příkazů**
- Místo zapamatování SQL syntaxe popište, jaká data potřebujete
- Místo pamatování Azure CLI příkazů vysvětlete, čeho chcete dosáhnout
- Nechte AI řešit technické detaily, zatímco vy se soustředíte na logiku

#### 3. 🔗 **Propojte více nástrojů dohromady**
- Vytvářejte silné workflow kombinací různých služeb
- Příklad: „Získej všechny nedávné GitHub issues a vytvoř odpovídající Azure DevOps work itemy“
- Budujte automatizace bez psaní složitých skriptů

#### 4. 🌐 **Přístup k rostoucímu ekosystému**
- Využívejte servery od Microsoftu, GitHubu a dalších společností
- Bezproblémově kombinujte nástroje od různých dodavatelů
- Připojte se ke standardizovanému ekosystému fungujícímu napříč AI asistenty

#### 5. 🛠️ **Učte se praxí**
- Začněte s předpřipravenými servery, abyste pochopili koncepty
- Postupně si vytvářejte vlastní servery, jakmile získáte jistotu
- Využívejte dostupné SDK a dokumentaci jako průvodce

### Příklad z praxe pro začátečníky

Řekněme, že jste noví ve webovém vývoji a pracujete na svém prvním projektu. Takto vám MCP servery mohou pomoci:

**Tradiční přístup:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**S MCP servery:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Výhoda podnikové standardizace

MCP se stává průmyslovým standardem, což znamená:
- **Konzistence**: Podobný zážitek napříč různými nástroji a firmami
- **Interoperabilita**: Servery od různých dodavatelů spolupracují
- **Budoucí připravenost**: Dovednosti a nastavení přenositelné mezi různými AI asistenty
- **Komunita**: Velký ekosystém sdílených znalostí a zdrojů

### Začínáme: Co se naučíte

V tomto průvodci prozkoumáme 10 Microsoft MCP serverů, které jsou obzvlášť užitečné pro vývojáře na všech úrovních. Každý server je navržen tak, aby:
- Řešil běžné vývojářské výzvy
- Snižoval opakující se úkoly
- Zlepšoval kvalitu kódu
- Podporoval možnosti učení

> **💡 Tip na učení**
> 
> Pokud jste v MCP úplný začátečník, začněte moduly [Úvod do MCP](../00-Introduction/README.md) a [Základní koncepty](../01-CoreConcepts/README.md). Pak se vraťte sem a uvidíte tyto koncepty v praxi s reálnými Microsoft nástroji.
>
> Pro další kontext o důležitosti MCP doporučujeme příspěvek Marie Naggagy: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Začínáme s MCP ve VS Code a Visual Studiu 🚀

Nastavení těchto MCP serverů je jednoduché, pokud používáte Visual Studio Code nebo Visual Studio 2022 s GitHub Copilotem.

### Nastavení ve VS Code

Základní postup pro VS Code:

1. **Povolit Agent Mode**: Ve VS Code přepněte v okně Copilot Chat do režimu Agent
2. **Konfigurovat MCP servery**: Přidejte konfigurace serverů do souboru settings.json ve VS Code
3. **Spustit servery**: Klikněte na tlačítko „Start“ u každého serveru, který chcete používat
4. **Vybrat nástroje**: Zvolte, které MCP servery chcete povolit pro aktuální relaci

Podrobné instrukce najdete v [dokumentaci VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profesionální tip: Spravujte MCP servery jako profík!**
> 
> Zobrazení rozšíření ve VS Code nyní obsahuje [přehledné nové uživatelské rozhraní pro správu nainstalovaných MCP serverů](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Máte rychlý přístup ke spuštění, zastavení a správě jakýchkoli MCP serverů pomocí jasného a jednoduchého rozhraní. Vyzkoušejte to!

### Nastavení ve Visual Studio 2022

Pro Visual Studio 2022 (verze 17.14 a novější):

1. **Povolit Agent Mode**: Klikněte na rozbalovací nabídku „Ask“ v okně GitHub Copilot Chat a vyberte „Agent“
2. **Vytvořit konfigurační soubor**: Vytvořte soubor `.mcp.json` ve složce řešení (doporučené umístění: `<SOLUTIONDIR>\.mcp.json`)
3. **Konfigurovat servery**: Přidejte konfigurace MCP serverů ve standardním MCP formátu
4. **Schválení nástrojů**: Po výzvě schvalte nástroje, které chcete používat, s příslušnými oprávněními

Podrobné instrukce pro Visual Studio najdete v [dokumentaci Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Každý MCP server má své vlastní požadavky na konfiguraci (připojovací řetězce, autentizace atd.), ale vzor nastavení je konzistentní v obou IDE.

## Lekce z Microsoft MCP serverů 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co dělá**: Microsoft Learn Docs MCP Server je cloudová služba, která poskytuje AI asistentům přístup v reálném čase k oficiální dokumentaci Microsoftu prostřednictvím Model Context Protocol. Připojuje se na `https://learn.microsoft.com/api/mcp` a umožňuje sémantické vyhledávání napříč Microsoft Learn, dokumentací Azure, Microsoft 365 a dalšími oficiálními zdroji Microsoftu.

**Proč je užitečný**: I když to může vypadat jako „jen dokumentace“, tento server je klíčový pro každého vývojáře používajícího technologie Microsoftu. Jednou z nejčastějších stížností .NET vývojářů na AI asistenty je, že nejsou aktuální s nejnovějšími verzemi .NET a C#. Microsoft Learn Docs MCP Server to řeší tím, že poskytuje přístup v reálném čase k nejnovější dokumentaci, referencím API a osvědčeným postupům. Ať už pracujete s nejnovějšími Azure SDK, zkoumáte nové funkce C# 13, nebo implementujete moderní .NET Aspire vzory, tento server zajistí, že váš AI asistent má přístup k autoritativním a aktuálním informacím potřebným k generování přesného a moderního kódu.

**Použití v praxi**: „Jaké jsou az cli příkazy pro vytvoření Azure container app podle oficiální dokumentace Microsoft Learn?“ nebo „Jak nakonfigurovat Entity Framework s dependency injection v ASP.NET Core?“ Nebo třeba „Zkontroluj tento kód, jestli odpovídá doporučením pro výkon v Microsoft Learn dokumentaci.“ Server poskytuje komplexní pokrytí Microsoft Learn, Azure dokumentace a Microsoft 365 dokumentace pomocí pokročilého sémantického vyhledávání, které najde nejrelevantnější informace v kontextu. Vrací až 10 kvalitních obsahových bloků s názvy článků a URL, vždy přistupuje k nejnovější dokumentaci Microsoftu, jakmile je publikována.

**Ukázkový příklad**: Server zpřístupňuje nástroj `microsoft_docs_search`, který provádí sémantické vyhledávání v oficiální technické dokumentaci Microsoftu. Po konfiguraci můžete klást otázky jako „Jak implementovat JWT autentizaci v ASP.NET Core?“ a získat podrobné, oficiální odpovědi s odkazy na zdroje. Kvalita vyhledávání je výjimečná, protože rozumí kontextu – dotaz na „containers“ v Azure kontextu vrátí dokumentaci Azure Container Instances, zatímco stejný termín v .NET kontextu vrátí relevantní informace o C# kolekcích.

To je obzvlášť užitečné pro rychle se měnící nebo nedávno aktualizované knihovny a scénáře použití. Například v některých nedávných projektech jsem chtěl využít funkce v nejnovějších verzích .NET Aspire a Microsoft.Extensions.AI. Díky zařazení Microsoft Learn Docs MCP serveru jsem mohl využít nejen API dokumentaci, ale i průvodce a návody, které byly právě publikovány.
> **💡 Užitečný tip**
> 
> I modely přátelské k nástrojům potřebují povzbuzení, aby používaly MCP nástroje! Zvažte přidání systémového promptu nebo [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) například: „Máte přístup k `microsoft.docs.mcp` – použijte tento nástroj k vyhledávání nejnovější oficiální dokumentace Microsoftu při řešení otázek týkajících se technologií Microsoft, jako jsou C#, Azure, ASP.NET Core nebo Entity Framework.“
>
> Pro skvělý příklad toho, jak to funguje v praxi, se podívejte na [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) z repozitáře Awesome GitHub Copilot. Tento režim konkrétně využívá MCP server Microsoft Learn Docs k pomoci s úklidem a modernizací C# kódu pomocí nejnovějších vzorů a osvědčených postupů.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co to dělá**: Azure MCP Server je komplexní sada více než 15 specializovaných konektorů pro služby Azure, která přináší celý ekosystém Azure přímo do vašeho AI pracovního postupu. Nejde jen o jeden server – je to výkonná kolekce zahrnující správu zdrojů, připojení k databázím (PostgreSQL, SQL Server), analýzu logů Azure Monitor pomocí KQL, integraci Cosmos DB a mnoho dalšího.

**Proč je to užitečné**: Kromě správy Azure zdrojů tento server výrazně zlepšuje kvalitu kódu při práci s Azure SDK. Když používáte Azure MCP v režimu Agent, nepomáhá vám jen psát kód – pomáhá vám psát *lepší* Azure kód, který dodržuje aktuální vzory autentizace, nejlepší postupy pro zpracování chyb a využívá nejnovější funkce SDK. Místo generického kódu, který možná funguje, dostanete kód, který odpovídá doporučeným vzorům Azure pro produkční nasazení.

**Klíčové moduly zahrnují**:
- **🗄️ Konektory k databázím**: Přímý přístup v přirozeném jazyce k Azure Database pro PostgreSQL a SQL Server
- **📊 Azure Monitor**: Analýza logů a provozní přehledy poháněné KQL
- **🌐 Správa zdrojů**: Kompletní správa životního cyklu Azure zdrojů
- **🔐 Autentizace**: Vzory DefaultAzureCredential a managed identity
- **📦 Služby úložiště**: Operace s Blob Storage, Queue Storage a Table Storage
- **🚀 Služby kontejnerů**: Správa Azure Container Apps, Container Instances a AKS
- **A mnoho dalších specializovaných konektorů**

**Praktické použití**: „Vyjmenuj mé Azure storage účty“, „Zeptej se mého Log Analytics workspace na chyby za poslední hodinu“ nebo „Pomoz mi vytvořit Azure aplikaci v Node.js s řádnou autentizací“

**Kompletní demonstrační scénář**: Zde je kompletní průvodce, který ukazuje sílu kombinace Azure MCP s rozšířením GitHub Copilot pro Azure ve VS Code. Když máte obojí nainstalované a zadáte:

> „Vytvoř Python skript, který nahraje soubor do Azure Blob Storage pomocí autentizace DefaultAzureCredential. Skript by se měl připojit k mému Azure storage účtu s názvem 'mycompanystorage', nahrát do kontejneru 'documents', vytvořit testovací soubor s aktuálním časovým razítkem k nahrání, elegantně zpracovat chyby a poskytnout informativní výstup, dodržovat nejlepší postupy Azure pro autentizaci a zpracování chyb, obsahovat komentáře vysvětlující, jak funguje autentizace DefaultAzureCredential, a být dobře strukturovaný se správnými funkcemi a dokumentací.“

Azure MCP Server vygeneruje kompletní, produkčně připravený Python skript, který:
- Používá nejnovější Azure Blob Storage SDK s řádnými asynchronními vzory
- Implementuje DefaultAzureCredential s podrobným vysvětlením fallback řetězce
- Obsahuje robustní zpracování chyb se specifickými typy výjimek Azure
- Dodržuje nejlepší postupy Azure SDK pro správu zdrojů a připojení
- Poskytuje detailní logování a informativní výstup do konzole
- Vytváří správně strukturovaný skript s funkcemi, dokumentací a typovými anotacemi

Co je na tom pozoruhodné, je fakt, že bez Azure MCP byste mohli dostat generický kód pro blob storage, který funguje, ale neodpovídá aktuálním vzorům Azure. S Azure MCP získáte kód, který využívá nejnovější autentizační metody, řeší specifické scénáře chyb Azure a dodržuje doporučené postupy Microsoftu pro produkční aplikace.

**Ukázkový příklad**: Měl jsem problém si zapamatovat konkrétní příkazy pro CLI `az` a `azd` pro ad-hoc použití. Vždy to pro mě bylo dvoukrokové: nejdřív najít syntaxi, pak spustit příkaz. Často jsem raději skočil do portálu a klikal, protože jsem nechtěl přiznat, že si nepamatuji syntax CLI. Možnost jednoduše popsat, co chci, je úžasná, a ještě lepší je to zvládnout přímo v IDE!

Skvělý seznam případů použití najdete v [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server). Pro podrobné návody na nastavení a pokročilé možnosti konfigurace navštivte [oficiální dokumentaci Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Co to dělá**: Oficiální GitHub MCP Server nabízí bezproblémovou integraci s celým ekosystémem GitHubu, a to jak formou hostovaného vzdáleného přístupu, tak i lokálního nasazení přes Docker. Nejde jen o základní operace s repozitáři – je to komplexní nástroj zahrnující správu GitHub Actions, workflow pull requestů, sledování issues, bezpečnostní skenování, notifikace a pokročilé automatizační funkce.

**Proč je to užitečné**: Tento server mění způsob, jakým pracujete s GitHubem, tím, že přináší plnohodnotnou platformu přímo do vašeho vývojového prostředí. Místo neustálého přepínání mezi VS Code a GitHub.com pro správu projektů, revize kódu a sledování CI/CD můžete vše řešit pomocí příkazů v přirozeném jazyce a zároveň zůstat soustředění na kód.

> **ℹ️ Poznámka: Různé typy „Agentů“**
> 
> Nezaměňujte tento GitHub MCP Server s GitHub Coding Agentem (AI agentem, kterému můžete přiřadit issues pro automatizované kódování). GitHub MCP Server funguje v režimu Agent ve VS Code a poskytuje integraci s GitHub API, zatímco GitHub Coding Agent je samostatná funkce, která vytváří pull requesty přiřazené k GitHub issues.

**Klíčové funkce zahrnují**:
- **⚙️ GitHub Actions**: Kompletní správa CI/CD pipeline, sledování workflow a práce s artefakty
- **🔀 Pull Requests**: Vytváření, revize, slučování a správa PR s podrobným sledováním stavu
- **🐛 Issues**: Kompletní správa životního cyklu issues, komentování, označování a přiřazování
- **🔒 Bezpečnost**: Upozornění na skenování kódu, detekce tajemství a integrace Dependabot
- **🔔 Notifikace**: Inteligentní správa oznámení a kontrola odběru repozitářů
- **📁 Správa repozitářů**: Operace se soubory, správa větví a administrace repozitářů
- **👥 Spolupráce**: Vyhledávání uživatelů a organizací, správa týmů a kontrola přístupů

**Praktické použití**: „Vytvoř pull request z mé feature větve“, „Ukaž mi všechny neúspěšné CI běhy tento týden“, „Vyjmenuj otevřené bezpečnostní upozornění pro mé repozitáře“ nebo „Najdi všechny issues přiřazené mně napříč mými organizacemi“

**Kompletní demonstrační scénář**: Zde je silný pracovní postup, který ukazuje schopnosti GitHub MCP Serveru:

> „Potřebuji se připravit na sprint review. Ukaž mi všechny pull requesty, které jsem tento týden vytvořil, zkontroluj stav našich CI/CD pipeline, vytvoř shrnutí bezpečnostních upozornění, která je třeba řešit, a pomoz mi sestavit poznámky k vydání na základě sloučených PR s označením 'feature'.“

GitHub MCP Server:
- Vyhledá vaše nedávné pull requesty s podrobnými informacemi o stavu
- Analyzuje běhy workflow a zvýrazní případné chyby nebo problémy s výkonem
- Sestaví výsledky bezpečnostního skenování a upřednostní kritická upozornění
- Vygeneruje komplexní poznámky k vydání extrahováním informací ze sloučených PR
- Poskytne konkrétní další kroky pro plánování sprintu a přípravu vydání

**Ukázkový příklad**: Rád to používám pro workflow revize kódu. Místo přepínání mezi VS Code, GitHub notifikacemi a stránkami pull requestů mohu říct „Ukaž mi všechny PR čekající na moji revizi“ a pak „Přidej komentář k PR #123 s dotazem na zpracování chyb v autentizační metodě.“ Server vyřídí volání GitHub API, udrží kontext diskuse a dokonce mi pomůže napsat konstruktivnější komentáře k revizi.

**Možnosti autentizace**: Server podporuje jak OAuth (bezproblémové ve VS Code), tak Personal Access Tokens, s konfigurovatelnými sadami nástrojů, které umožňují povolit jen ty funkce GitHubu, které potřebujete. Můžete jej spustit jako hostovanou vzdálenou službu pro rychlé nastavení nebo lokálně přes Docker pro plnou kontrolu.

> **💡 Tip pro profesionály**
> 
> Povolit pouze potřebné sady nástrojů pomocí parametru `--toolsets` v nastavení MCP serveru, abyste snížili velikost kontextu a zlepšili výběr AI nástrojů. Například přidejte `"--toolsets", "repos,issues,pull_requests,actions"` do argumentů konfigurace MCP pro základní vývojové workflow, nebo použijte `"--toolsets", "notifications, security"`, pokud chcete primárně sledovat GitHub.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Co to dělá**: Připojuje se ke službám Azure DevOps pro komplexní správu projektů, sledování pracovních položek, správu build pipeline a operace s repozitáři.

**Proč je to užitečné**: Pro týmy, které používají Azure DevOps jako hlavní DevOps platformu, tento MCP server eliminuje neustálé přepínání mezi vývojovým prostředím a webovým rozhraním Azure DevOps. Můžete spravovat pracovní položky, kontrolovat stav buildů, dotazovat se na repozitáře a řešit úkoly projektového řízení přímo přes svého AI asistenta.

**Praktické použití**: „Ukaž mi všechny aktivní pracovní položky v aktuálním sprintu pro projekt WebApp“, „Vytvoř hlášení o chybě pro problém s přihlášením, který jsem právě našel“ nebo „Zkontroluj stav našich build pipeline a ukaž mi poslední neúspěchy“

**Ukázkový příklad**: Snadno zkontrolujete stav aktuálního sprintu vašeho týmu jednoduchým dotazem jako „Ukaž mi všechny aktivní pracovní položky v aktuálním sprintu pro projekt WebApp“ nebo „Vytvoř hlášení o chybě pro problém s přihlášením, který jsem právě našel“ bez opuštění vývojového prostředí.

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Co to dělá**: MarkItDown je komplexní server pro převod dokumentů, který přeměňuje různé formáty souborů na vysoce kvalitní Markdown, optimalizovaný pro zpracování LLM a pracovní postupy analýzy textu.

**Proč je to užitečné**: Nezbytné pro moderní pracovní postupy dokumentace! MarkItDown zvládá širokou škálu formátů souborů a zároveň zachovává klíčovou strukturu dokumentu, jako jsou nadpisy, seznamy, tabulky a odkazy. Na rozdíl od jednoduchých nástrojů pro extrakci textu se zaměřuje na udržení sémantického významu a formátování, které je cenné jak pro AI zpracování, tak pro lidskou čitelnost.

**Podporované formáty souborů**:
- **Office dokumenty**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Mediální soubory**: Obrázky (s EXIF metadaty a OCR), Audio (s EXIF metadaty a přepisem řeči)
- **Webový obsah**: HTML, RSS kanály, YouTube URL, stránky Wikipedie
- **Datové formáty**: CSV, JSON, XML, ZIP soubory (rekurzivně zpracovává obsah)
- **Publikační formáty**: EPub, Jupyter notebooky (.ipynb)
- **E-maily**: Outlook zprávy (.msg)
- **Pokročilé**: Integrace Azure Document Intelligence pro vylepšené zpracování PDF

**Pokročilé schopnosti**: MarkItDown podporuje popisy obrázků poháněné LLM (pokud je k dispozici OpenAI klient), Azure Document Intelligence pro lepší zpracování PDF, přepis audia pro řečový obsah a systém pluginů pro rozšíření o další formáty souborů.

**Reálné použití**: „Převeď tuto PowerPoint prezentaci do Markdownu pro náš dokumentační web“, „Extrahuj text z tohoto PDF se správnou strukturou nadpisů“ nebo „Přeměň tento Excelový sešit do čitelné tabulkové podoby“

**Ukázkový příklad**: Citace z [MarkItDown dokumentace](https://github.com/microsoft/markitdown#why-markdown):


> Markdown je velmi blízký prostému textu, s minimálním značením nebo formátováním, ale přesto umožňuje reprezentovat důležitou strukturu dokumentu. Hlavní LLM, jako OpenAI GPT-4o, nativně „mluví“ Markdownem a často jej do svých odpovědí začleňují bez výzvy. To naznačuje, že byly trénovány na obrovském množství textů ve formátu Markdown a dobře mu rozumí. Jako vedlejší efekt jsou Markdown konvence také velmi efektivní z hlediska tokenů.

MarkItDown je opravdu dobrý v zachování struktury dokumentu, což je důležité pro AI pracovní postupy. Například při převodu PowerPoint prezentace zachovává organizaci snímků s odpovídajícími nadpisy, extrahuje tabulky jako Markdown tabulky, zahrnuje alternativní texty k obrázkům a dokonce zpracovává poznámky přednášejícího. Grafy jsou převedeny na čitelné datové tabulky a výsledný Markdown udržuje logický tok původní prezentace. Díky tomu je ideální pro předávání obsahu prezentací do AI systémů nebo tvorbu dokumentace z existujících snímků.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co to dělá**: Poskytuje konverzační přístup k SQL Server databázím (on-premises, Azure SQL nebo Fabric)

**Proč je to užitečné**: Podobné jako PostgreSQL server, ale pro Microsoft SQL ekosystém. Připojte se pomocí jednoduchého connection stringu a začněte dotazovat v přirozeném jazyce – žádné přepínání kontextu!

**Reálné použití**: „Najdi všechny objednávky, které nebyly splněny za posledních 30 dní“ se přeloží do odpovídajících SQL dotazů a vrátí formátované výsledky

**Ukázkový příklad**: Jakmile nastavíte připojení k databázi, můžete okamžitě začít komunikovat se svými daty. Blogový příspěvek to ukazuje na jednoduché otázce: „ke které databázi jste připojeni?“ MCP server odpoví vyvoláním příslušného databázového nástroje, připojí se k vaší SQL Server instanci a vrátí informace o aktuálním připojení – to vše bez nutnosti psát jediný řádek SQL. Server podporuje komplexní databázové operace od správy schémat po manipulaci s daty, vše prostřednictvím příkazů v přirozeném jazyce. Kompletní návod na nastavení a příklady konfigurace s VS Code a Claude Desktop najdete zde: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Co to dělá**: Umožňuje AI agentům interagovat s webovými stránkami pro testování a automatizaci

> **ℹ️ Pohání GitHub Copilot**
> 
> Playwright MCP Server pohání Coding Agenta GitHub Copilota, který tak získává schopnost prohlížet web! [Více o této funkci](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Proč je to užitečné**: Ideální pro automatizované testování řízené popisy v přirozeném jazyce. AI může procházet weby, vyplňovat formuláře a extrahovat data pomocí strukturovaných snímků přístupnosti – to je opravdu silná věc!

**Reálné použití**: „Otestuj přihlašovací proces a ověř, že se dashboard načte správně“ nebo „Vygeneruj test, který vyhledá produkty a ověří stránku s výsledky“ – to vše bez nutnosti přístupu ke zdrojovému kódu aplikace

**Ukázkový příklad**: Moje kolegyně Debbie O'Brien v poslední době odvádí skvělou práci s Playwright MCP Serverem! Například nedávno ukázala, jak lze vygenerovat kompletní Playwright testy, aniž by měla přístup ke zdrojovému kódu aplikace. Ve svém scénáři požádala Copilota, aby vytvořil test pro aplikaci na vyhledávání filmů: naviguj na stránku, vyhledej „Garfield“ a ověř, že se film objeví ve výsledcích. MCP spustil relaci prohlížeče, prozkoumal strukturu stránky pomocí DOM snapshotů, našel správné selektory a vygeneroval plně funkční TypeScript test, který prošel na první pokus.

Co je na tom opravdu silné, je to, že to propojuje instrukce v přirozeném jazyce s vykonatelným testovacím kódem. Tradiční přístupy vyžadují buď ruční psaní testů, nebo přístup ke kódu pro kontext. S Playwright MCP však můžete testovat externí weby, klientské aplikace nebo pracovat v black-box testovacích scénářích, kde není přístup ke kódu dostupný.

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co to dělá**: Spravuje prostředí Microsoft Dev Box pomocí přirozeného jazyka

**Proč je to užitečné**: Výrazně zjednodušuje správu vývojových prostředí! Vytvářejte, konfigurujte a spravujte vývojová prostředí bez nutnosti pamatovat si konkrétní příkazy.

**Reálné použití**: „Nastav nový Dev Box s nejnovějším .NET SDK a nakonfiguruj ho pro náš projekt“, „Zkontroluj stav všech mých vývojových prostředí“ nebo „Vytvoř standardizované demo prostředí pro týmové prezentace“

**Ukázkový příklad**: Jsem velkým fanouškem používání Dev Boxu pro osobní vývoj. Můj moment „aha“ přišel, když James Montemagno vysvětlil, jak je Dev Box skvělý pro konferenční demo ukázky, protože má superrychlé ethernetové připojení bez ohledu na konferenci, hotel nebo Wi-Fi v letadle, které právě používám. Nedávno jsem dokonce cvičil konferenční demo, zatímco byl můj notebook připojený k hotspotu telefonu během jízdy autobusem z Brug do Antverp! Můj další krok je více se zaměřit na týmovou správu více vývojových prostředí a standardizovaných demo prostředí. Další velké využití, o kterém slyším od zákazníků a kolegů, je používání Dev Boxu pro předkonfigurovaná vývojová prostředí. V obou případech umožňuje MCP konfiguraci a správu Dev Boxů pomocí přirozeného jazyka, aniž byste museli opouštět své vývojové prostředí.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Co to dělá**: Azure AI Foundry MCP Server poskytuje vývojářům komplexní přístup k AI ekosystému Azure, včetně katalogů modelů, správy nasazení, indexování znalostí pomocí Azure AI Search a nástrojů pro hodnocení. Tento experimentální server propojuje vývoj AI s výkonnou AI infrastrukturou Azure, což usnadňuje vytváření, nasazení a hodnocení AI aplikací.

**Proč je to užitečné**: Tento server mění způsob, jakým pracujete se službami Azure AI, tím, že přináší podnikové AI funkce přímo do vašeho vývojového workflow. Místo přepínání mezi Azure portálem, dokumentací a IDE můžete objevovat modely, nasazovat služby, spravovat znalostní báze a hodnotit výkon AI pomocí příkazů v přirozeném jazyce. Je obzvlášť silný pro vývojáře, kteří vytvářejí RAG (Retrieval-Augmented Generation) aplikace, spravují nasazení více modelů nebo implementují komplexní AI hodnotící pipeline.

**Klíčové schopnosti pro vývojáře**:
- **🔍 Objevování a nasazení modelů**: Prozkoumejte katalog modelů Azure AI Foundry, získejte podrobné informace o modelech s ukázkami kódu a nasazujte modely do Azure AI Services
- **📚 Správa znalostí**: Vytvářejte a spravujte indexy Azure AI Search, přidávejte dokumenty, konfigurujte indexery a budujte sofistikované RAG systémy
- **⚡ Integrace AI agentů**: Připojte se k Azure AI Agentům, dotazujte se na existující agenty a hodnotte jejich výkon v produkčních scénářích
- **📊 Hodnotící rámec**: Proveďte komplexní hodnocení textu a agentů, generujte markdown reporty a implementujte kontrolu kvality AI aplikací
- **🚀 Nástroje pro prototypování**: Získejte instrukce pro nastavení prototypování založeného na GitHubu a přístup k Azure AI Foundry Labs pro nejnovější výzkumné modely

**Reálné použití vývojářů**: „Nasadit model Phi-4 do Azure AI Services pro mou aplikaci“, „Vytvořit nový vyhledávací index pro můj dokumentační RAG systém“, „Zhodnotit odpovědi mého agenta podle kvalitativních metrik“ nebo „Najít nejlepší model pro odvozování pro mé složité analytické úkoly“

**Plný demonstrační scénář**: Zde je silný vývojový workflow AI:


> „Vytvářím zákaznického podpůrného agenta. Pomoz mi najít dobrý model pro odvozování v katalogu, nasadit ho do Azure AI Services, vytvořit znalostní bázi z naší dokumentace, nastavit hodnotící rámec pro testování kvality odpovědí a pak mi pomoci s prototypováním integrace s GitHub tokenem pro testování.“

Azure AI Foundry MCP Server:
- Prohledá katalog modelů a doporučí optimální modely pro odvozování podle tvých požadavků
- Poskytne příkazy pro nasazení a informace o kvótách pro preferovaný region Azure
- Nastaví indexy Azure AI Search s vhodným schématem pro tvou dokumentaci
- Nakonfiguruje hodnotící pipeline s metrikami kvality a bezpečnostními kontrolami
- Vygeneruje prototypový kód s GitHub autentizací pro okamžité testování
- Poskytne komplexní návody na nastavení přizpůsobené tvému technologickému stacku

**Ukázkový příklad**: Jako vývojář jsem měl problém držet krok s různými dostupnými LLM modely. Znám pár hlavních, ale měl jsem pocit, že mi unikají možnosti zvýšení produktivity a efektivity. Tokeny a kvóty jsou stresující a těžko se spravují – nikdy nevím, jestli vybírám správný model pro správný úkol, nebo jestli neplýtvám rozpočtem. Nedávno jsem slyšel o tomto MCP Serveru od Jamese Montemagna, když jsem se ptal kolegů na doporučení MCP Serverů pro tento příspěvek, a jsem nadšený, že ho mohu vyzkoušet! Funkce objevování modelů vypadají obzvlášť působivě pro někoho jako já, kdo chce prozkoumat i méně známé modely optimalizované pro specifické úkoly. Hodnotící rámec by mi měl pomoci ověřit, že skutečně dosahuji lepších výsledků, a ne jen zkouším něco nového pro samotnou změnu.

> **ℹ️ Experimentální stav**
> 
> Tento MCP server je experimentální a je aktivně vyvíjen. Funkce a API se mohou měnit. Je ideální pro zkoumání možností Azure AI a tvorbu prototypů, ale pro produkční použití ověřte stabilitu.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Co to dělá**: Poskytuje vývojářům základní nástroje pro tvorbu AI agentů a aplikací integrujících se s Microsoft 365 a Microsoft 365 Copilot, včetně validace schémat, získávání ukázkového kódu a pomoci při řešení problémů.

**Proč je to užitečné**: Vývoj pro Microsoft 365 a Copilot zahrnuje složitá schémata manifestů a specifické vývojové vzory. Tento MCP server přináší klíčové vývojové zdroje přímo do vašeho vývojového prostředí, pomáhá validovat schémata, najít ukázkový kód a řešit běžné problémy bez nutnosti neustálého odkazování na dokumentaci.

**Reálné použití**: „Validuj manifest deklarativního agenta a oprav chyby ve schématu“, „Ukaž mi ukázkový kód pro implementaci pluginu Microsoft Graph API“ nebo „Pomoz mi vyřešit problémy s autentizací mé Teams aplikace“

**Ukázkový příklad**: Po rozhovoru s mým přítelem Johnem Millerem na konferenci Build o M365 Agentech mi doporučil tento MCP. Může být skvělý pro vývojáře, kteří s M365 Agenty začínají, protože nabízí šablony, ukázkový kód a základní strukturu pro rychlý start bez zahlcení dokumentací. Funkce validace schémat jsou obzvlášť užitečné pro předcházení chybám ve struktuře manifestu, které by mohly způsobit hodiny ladění.

> **💡 Tip**
> 
> Používejte tento server společně s Microsoft Learn Docs MCP Serverem pro komplexní podporu vývoje M365 – jeden poskytuje oficiální dokumentaci, druhý praktické nástroje a pomoc při řešení problémů.

## Co dál? 🔮

## 📋 Závěr

Model Context Protocol (MCP) mění způsob, jakým vývojáři komunikují s AI asistenty a externími nástroji. Těchto 10 Microsoft MCP serverů ukazuje sílu standardizované AI integrace, která umožňuje plynulé workflow, jež udržuje vývojáře v jejich pracovním flow a zároveň zpřístupňuje výkonné externí funkce.

Od komplexní integrace Azure ekosystému po specializované nástroje jako Playwright pro automatizaci prohlížeče a MarkItDown pro zpracování dokumentů, tyto servery ukazují, jak MCP může zvýšit produktivitu v různých vývojových scénářích. Standardizovaný protokol zajišťuje, že tyto nástroje spolupracují bez problémů a vytvářejí soudržný vývojový zážitek.

Jak se MCP ekosystém vyvíjí, klíčem k maximální produktivitě bude aktivní zapojení do komunity, zkoumání nových serverů a tvorba vlastních řešení. Otevřený standard MCP umožňuje kombinovat nástroje od různých dodavatelů a vytvořit tak ideální workflow přesně podle vašich potřeb.

## 🔗 Další zdroje

- [Oficiální Microsoft MCP repozitář](https://github.com/microsoft/mcp)
- [MCP komunita a dokumentace](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentace](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentace](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentace](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP události](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29./30. července nebo sledovat na vyžádání](https://aka.ms/mcpdevdays)

## 🎯 Cvičení

1. **Instalace a konfigurace**: Nainstalujte jeden z MCP serverů do svého VS Code prostředí a otestujte základní funkce.
2. **Integrace workflow**: Navrhněte vývojový workflow, který kombinuje alespoň tři různé MCP servery.
3. **Plánování vlastního serveru**: Identifikujte úkol ve svém denním vývojovém procesu, který by mohl využít vlastní MCP server, a vytvořte jeho specifikaci.
4. **Analýza výkonu**: Porovnejte efektivitu používání MCP serverů oproti tradičním přístupům u běžných vývojových úkolů.
5. **Hodnocení bezpečnosti**: Zhodnoťte bezpečnostní dopady používání MCP serverů ve vašem vývojovém prostředí a navrhněte nejlepší postupy.

Next:[Best Practices](../08-BestPractices/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.