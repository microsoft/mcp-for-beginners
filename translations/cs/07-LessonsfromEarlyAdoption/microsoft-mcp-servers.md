# 🚀 10 Microsoft MCP serverů, které mění produktivitu vývojářů

## 🎯 Co se v této příručce naučíte

Tato praktická příručka představuje deset Microsoft MCP serverů, které aktivně mění způsob, jakým vývojáři pracují s AI asistenty. Místo toho, abychom jen vysvětlovali, co MCP servery *mohou* dělat, ukážeme vám servery, které již nyní skutečně ovlivňují každodenní vývojové toky práce v Microsoftu a mimo něj.

Každý server v této příručce byl vybrán na základě reálného používání a zpětné vazby vývojářů. Dozvíte se nejen, co každý server dělá, ale proč je důležitý a jak z něj vytěžit maximum ve svých projektech. Ať už jste v MCP úplný začátečník, nebo chcete rozšířit své stávající nastavení, tyto servery reprezentují některé z nejpraktickějších a nejúčinnějších nástrojů v ekosystému Microsoftu.

> **💡 Rychlý tip pro start**
> 
> Jste v MCP noví? Nechte si to uklidnit! Tato příručka je navržena tak, aby byla přívětivá k začátečníkům. Vysvětlíme pojmy za pochodu a vždy se můžete vrátit k našim modulům [Úvod do MCP](../00-Introduction/README.md) a [Základní koncepty](../01-CoreConcepts/README.md) pro hlubší znalosti.

## Přehled

Tato obsáhlá příručka zkoumá deset Microsoft MCP serverů, které revolucionalizují způsob, jakým vývojáři komunikují s AI asistenty a externími nástroji. Od správy Azure zdrojů po zpracování dokumentů tyto servery ukazují sílu Model Context Protocol při vytváření bezproblémových a produktivních vývojových toků práce.

## Výukové cíle

Na konci této příručky budete:
- Rozumět tomu, jak MCP servery zvyšují produktivitu vývojářů
- Seznámit se s nejvlivnějšími MCP servery od Microsoftu
- Objevit praktické případy použití jednotlivých serverů
- Vědět, jak tyto servery nastavit a konfigurovat ve VS Code a Visual Studiu
- Prozkoumat širší MCP ekosystém a budoucí směry

## 🔧 Pochopení MCP serverů: Příručka pro začátečníky

### Co jsou MCP servery?

Jako začátečník v Model Context Protocol (MCP) si možná říkáte: „Co přesně je MCP server a proč by mě to mělo zajímat?“ Začněme jednoduchou analogií.

Představte si MCP servery jako specializované asistenty, kteří pomáhají vašemu AI kódovacímu společníkovi (například GitHub Copilot) připojit se k externím nástrojům a službám. Stejně jako používáte různé aplikace na telefonu pro různé úkoly — jednu pro počasí, jednu pro navigaci, jednu pro bankovnictví — MCP servery dávají vašemu AI asistentovi možnost interagovat s různými vývojovými nástroji a službami.

### Problém, který MCP servery řeší

Před MCP servery, pokud jste chtěli:
- Zkontrolovat své Azure zdroje
- Vytvořit GitHub issue
- Dotazovat svou databázi
- Prohledat dokumentaci

Museli jste přestat kódovat, otevřít prohlížeč, přejít na příslušnou webovou stránku a ručně tyto úkoly vykonat. Toto neustálé přepínání kontextu narušuje váš tok práce a snižuje produktivitu.

### Jak MCP servery mění vaši vývojovou zkušenost

S MCP servery můžete zůstat ve svém vývojovém prostředí (VS Code, Visual Studio atd.) a jednoduše požádat svého AI asistenta, aby tyto úkoly vykonal. Například:

**Místo tohoto tradičního postupu:**
1. Přestat kódovat
2. Otevřít prohlížeč
3. Přejít na Azure portál
4. Vyhledat podrobnosti o úložišti
5. Vrátit se do VS Code
6. Pokračovat v kódování

**Nyní můžete dělat toto:**
1. Zeptat se AI: „Jaký je stav mých Azure úložišť?“
2. Pokračovat v kódování s poskytnutými informacemi

### Klíčové výhody pro začátečníky

#### 1. 🔄 **Zůstaňte ve svém proudu práce**
- Už žádné přepínání mezi různými aplikacemi
- Zachovejte si pozornost na kódu, který píšete
- Snižte mentální zátěž z ovládání různých nástrojů

#### 2. 🤖 **Používejte přirozený jazyk místo složitých příkazů**
- Místo zapamatování syntaxe SQL popište, jaká data potřebujete
- Místo vzpomínání příkazů Azure CLI vysvětlete, čeho chcete dosáhnout
- Nechte AI řešit technické detaily, ať se vy zaměříte na logiku

#### 3. 🔗 **Propojte více nástrojů dohromady**
- Vytvářejte silné toky práce kombinací různých služeb
- Příklad: „Získej všechny nedávné GitHub issue a vytvoř odpovídající pracovní položky v Azure DevOps“
- Vytvářejte automatizace bez psaní složitých skriptů

#### 4. 🌐 **Přístup k rostoucímu ekosystému**
- Využívejte servery vyvinuté Microsoftem, GitHubem a dalšími společnostmi
- Bezproblémové kombinování nástrojů od různých dodavatelů
- Připojte se ke standardizovanému ekosystému, který funguje napříč různými AI asistenty

#### 5. 🛠️ **Učte se praxí**
- Začněte s předem připravenými servery, abyste pochopili koncepty
- Postupně vytvářejte své vlastní servery, jakmile získáte jistotu
- Používejte dostupné SDK a dokumentaci pro svůj rozvoj

### Reálný příklad pro začátečníky

Představme si, že jste nováček ve webovém vývoji a pracujete na svém prvním projektu. Zde je, jak vám MCP servery mohou pomoci:

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

### Výhoda průmyslového standardu pro firmy

MCP se stává průmyslovým standardem, což znamená:
- **Konzistence**: Podobná zkušenost napříč různými nástroji a společnostmi
- **Interoperabilita**: Servery od různých dodavatelů spolupracují
- **Budoucí udržitelnost**: Dovednosti a nastavení se přenášejí mezi různými AI asistenty
- **Komunita**: Velký ekosystém sdílených znalostí a zdrojů

### Začínáme: Co se naučíte

V této příručce prozkoumáme 10 Microsoft MCP serverů, které jsou zvláště užitečné pro vývojáře na všech úrovních. Každý server je navržen tak, aby:
- Řešil běžné vývojové výzvy
- Snižoval opakující se úkoly
- Zlepšil kvalitu kódu
- Rozšiřoval příležitosti k učení

> **💡 Výukový tip**
> 
> Pokud jste v MCP úplní nováčci, začněte s našimi moduly [Úvod do MCP](../00-Introduction/README.md) a [Základní koncepty](../01-CoreConcepts/README.md). Pak se sem vraťte, abyste viděli tyto koncepty v akci s reálnými nástroji Microsoftu.
>
> Pro další kontext o důležitosti MCP doporučuji příspěvek Marie Naggaga: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Začínáme s MCP ve VS Code a Visual Studiu 🚀

Nastavení těchto MCP serverů je jednoduché, pokud používáte Visual Studio Code nebo Visual Studio 2022 s GitHub Copilot.

### Nastavení ve VS Code

Zde je základní postup pro VS Code:

1. **Povolit režim agenta**: Ve VS Code přepněte do režimu Agenta v okně Copilot Chat
2. **Konfigurace MCP serverů**: Přidejte konfigurace serverů do svého souboru settings.json ve VS Code
3. **Spuštění serverů**: Klikněte na tlačítko „Start“ u každého serveru, který chcete použít
4. **Výběr nástrojů**: Vyberte, které MCP servery chcete povolit pro aktuální relaci

Pro podrobné instrukce nastavení viz [VS Code MCP dokumentace](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profesionální tip: Spravujte MCP servery jako profík!**
> 
> Zobrazení rozšíření VS Code nyní obsahuje [užitečné nové UI pro správu nainstalovaných MCP serverů](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Máte rychlý přístup ke spuštění, zastavení a správě jakýchkoli nainstalovaných MCP serverů přes jasné a jednoduché rozhraní. Vyzkoušejte to!

### Nastavení ve Visual Studiu 2022

Pro Visual Studio 2022 (verze 17.14 nebo novější):

1. **Povolit režim agenta**: Klikněte na rozbalovací menu „Ask“ v okně GitHub Copilot Chat a vyberte „Agent“
2. **Vytvořit konfigurační soubor**: Vytvořte soubor `.mcp.json` v adresáři řešení (doporučené umístění: `<SOLUTIONDIR>\.mcp.json`)
3. **Konfigurace serverů**: Přidejte konfigurace vašich MCP serverů pomocí standardního MCP formátu
4. **Schválení nástrojů**: Po výzvě schvalujte nástroje, které chcete použít, s odpovídajícími oprávněními

Pro podrobné instrukce nastavení ve Visual Studiu viz [Visual Studio MCP dokumentaci](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Každý MCP server má vlastní požadavky na konfiguraci (připojovací řetězce, autentizace atd.), ale vzor nastavení je konzistentní v obou IDE.

## Lekce z Microsoft MCP serverů 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Nainstalovat ve VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Nainstalovat ve VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co dělá**: Microsoft Learn Docs MCP Server je cloudová služba, která AI asistentům poskytuje přístup v reálném čase k oficiální dokumentaci Microsoftu prostřednictvím Model Context Protocol. Připojuje se k `https://learn.microsoft.com/api/mcp` a umožňuje sémantické vyhledávání napříč Microsoft Learn, dokumentací Azure, Microsoft 365 a dalšími oficiálními zdroji Microsoftu.

**Proč je užitečný**: Ačkoli to může vypadat jako „jen dokumentace“, tento server je ve skutečnosti klíčový pro každého vývojáře pracujícího s technologiemi Microsoftu. Jednou z nejčastějších stížností vývojářů .NET na AI asistentů kódu je, že nejsou aktuální s nejnovějšími vydáními .NET a C#. Microsoft Learn Docs MCP Server to řeší tím, že poskytuje přístup v reálném čase k nejaktuálnější dokumentaci, referencím API a osvědčeným postupům. Ať už pracujete s nejnovějšími Azure SDK, zkoumáte nové funkce C# 13, nebo implementujete špičkové Aspire vzory, tento server zajistí, že váš AI asistent má přístup k autoritativním a aktuálním informacím potřebným k generování přesného a moderního kódu.

**Reálné použití**: „Jaké jsou az cli příkazy pro vytvoření Azure container app podle oficiální dokumentace Microsoft Learn?“ nebo „Jak nakonfigurovat Entity Framework s dependency injection v ASP.NET Core?“ Nebo co třeba „Zkontroluj tento kód, aby odpovídal výkonovým doporučením v Microsoft Learn dokumentaci.“ Server poskytuje komplexní pokrytí napříč Microsoft Learn, Azure dokumentací a Microsoft 365 dokumentací použitím pokročilého sémantického vyhledávání pro nalezení nejkontextuálnějších informací. Vrací až 10 kvalitních obsahových bloků s názvy článků a URL, vždy přistupuje k nejnovější dokumentaci Microsoftu ihned po jejím vydání.

**Ukázkový příklad**: Server zpřístupňuje nástroj `microsoft_docs_search`, který provádí sémantické vyhledávání v oficiální technické dokumentaci Microsoftu. Po konfiguraci můžete klást otázky jako „Jak implementovat JWT autentizaci v ASP.NET Core?“ a dostanete podrobné oficiální odpovědi s odkazy na zdroje. Kvalita vyhledávání je výjimečná, protože chápe kontext – dotaz na „containers“ v Azure kontextu vrátí dokumentaci Azure Container Instances, zatímco tentýž výraz v .NET kontextu poskytne relevantní informace o kolekcích C#.

To je obzvlášť užitečné pro rychle se měnící nebo nedávno aktualizované knihovny a použití. Například v několika nedávných projektech jsem chtěl využít funkce v nejnovějších verzích Aspire a Microsoft.Extensions.AI. Zařazením Microsoft Learn Docs MCP serveru jsem mohl využívat nejen API dokumentaci, ale i průvodce a návody, které právě vyšly.

> **💡 Profesionální tip**
> 
> I modely přívětivé k nástrojům je třeba povzbuzovat, aby používaly MCP nástroje! Zvažte přidání systémového promptu nebo [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot), například: „Máš přístup k `microsoft.docs.mcp` – použij tento nástroj k vyhledávání nejnovější oficiální dokumentace Microsoftu při zodpovídání otázek o technologiích Microsoft, jako jsou C#, Azure, ASP.NET Core nebo Entity Framework.“
>
> Pro skvělý příklad v praxi se podívejte na [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) v repozitáři Awesome GitHub Copilot. Tento režim přímo využívá Microsoft Learn Docs MCP server k pomoci s údržbou a modernizací C# kódu podle nejnovějších vzorů a osvědčených praktik.
### 2. ☁️ Azure MCP Server


[![Nainstalovat ve VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Nainstalovat ve VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co to dělá**: Azure MCP Server je komplexní sada více než 15 specializovaných konektorů Azure služeb, která přináší celý ekosystém Azure do vašeho AI pracovního postupu. Nejde jen o jeden server – je to výkonná kolekce, která zahrnuje správu zdrojů, připojení k databázím (PostgreSQL, SQL Server), analýzu protokolů Azure Monitor pomocí KQL, integraci Cosmos DB a mnoho dalšího.

**Proč je to užitečné**: Kromě správy Azure zdrojů tento server výrazně zlepšuje kvalitu kódu při práci s Azure SDK. Když používáte Azure MCP v režimu Agenta, nepomáhá vám jen psát kód – pomáhá vám psát *lepší* Azure kód, který dodržuje aktuální autentizační vzory, nejlepší postupy zpracování chyb a využívá nejnovější funkce SDK. Místo generického kódu, který může fungovat, získáte kód, který sleduje doporučené vzory Azure pro produkční pracovní zatížení.

**Klíčové moduly zahrnují**:
- **🗄️ Konektory databází**: Přímý přístup v přirozeném jazyce k Azure Database pro PostgreSQL a SQL Server
- **📊 Azure Monitor**: Analýza protokolů a provozní přehledy s podporou KQL
- **🌐 Správa zdrojů**: Kompletní správa životního cyklu Azure zdrojů
- **🔐 Autentizace**: Vzory DefaultAzureCredential a managed identity
- **📦 Úložné služby**: Operace s Blob Storage, Queue Storage a Table Storage
- **🚀 Kontejnerové služby**: Správa Azure Container Apps, Container Instances a AKS
- **A mnoho dalších specializovaných konektorů**

**Reálné použití**: „Vylistuj mé Azure účty pro úložiště“, „Zeptej se mého Log Analytics workspace na chyby za poslední hodinu“ nebo „Pomoz mi vytvořit Azure aplikaci v Node.js s náležitou autentizací“

**Úplné demonstrační scénář**: Zde je kompletní průchod, který ukazuje sílu kombinace Azure MCP s rozšířením GitHub Copilot pro Azure ve VS Code. Když máte obojí nainstalované a zadáte:

> „Vytvoř Python skript, který nahraje soubor do Azure Blob Storage pomocí autentizace DefaultAzureCredential. Skript se připojí k mému Azure storage účtu nazvanému 'mycompanystorage', nahraje do kontejneru nazvaného 'documents', vytvoří testovací soubor s aktuálním časovým razítkem k nahrání, zvládne chyby elegantně a poskytne informativní výstup, dodrží nejlepší postupy Azure pro autentizaci a zpracování chyb, obsahuje komentáře vysvětlující, jak funguje autentizace DefaultAzureCredential, a udělá skript dobře strukturovaný s náležitými funkcemi a dokumentací.“

Azure MCP Server vygeneruje kompletní, produkčně připravený Python skript, který:
- Používá nejnovější Azure Blob Storage SDK s náležitými asynchronními vzory
- Implementuje DefaultAzureCredential s podrobným vysvětlením režimu záložních variant
- Obsahuje robustní zpracování chyb s konkrétními typy Azure výjimek
- Dbá na nejlepší postupy Azure SDK pro správu zdrojů a správu připojení
- Poskytuje detailní logování a informativní výstup v konzoli
- Vytváří správně strukturovaný skript s funkcemi, dokumentací a typovými nápovědami

To, co je na tom pozoruhodné, je, že bez Azure MCP byste mohli dostat generický kód pro blob storage, který funguje, ale nesleduje aktuální vzory Azure. S Azure MCP dostáváte kód, který využívá nejnovější autentizační metody, zvládá scénáře chyb specifické pro Azure a dodržuje doporučené postupy Microsoftu pro produkční aplikace.

**Ukázka z praxe**: Měl jsem problém si pamatovat konkrétní příkazy pro CLI `az` a `azd` pro ad-hoc použití. Pro mě je to vždy dvoufázový proces: nejprve najít syntaxi, pak spustit příkaz. Často raději skočím do portálu a klikám kolem, abych práci dokončil, protože se nechci přiznat, že si nepamatuji syntaxi CLI. Možnost jen popsat, co chci, je úžasná, a ještě lepší je to dělat bez opuštění IDE!

Skvělý seznam případů použití najdete v [repozitáři Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server), který vás uvede do práce. Pro komplexní průvodce nastavením a pokročilé možnosti konfigurace navštivte [oficiální dokumentaci Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Nainstalovat ve VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Nainstalovat ve VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Co to dělá**: Oficiální GitHub MCP Server poskytuje bezproblémovou integraci s celým ekosystémem GitHub a nabízí jak hostovaný vzdálený přístup, tak možnost lokálního nasazení přes Docker. Nejde jen o základní operace s repozitáři – je to komplexní sada nástrojů, která zahrnuje správu GitHub Actions, pracovní toky pull requestů, sledování problémů, bezpečnostní skenování, oznámení a pokročilé automatizační schopnosti.

**Proč je to užitečné**: Tento server mění způsob, jakým interagujete s GitHubem, přináší plnohodnotnou platformu přímo do vývojového prostředí. Místo neustálého přepínání mezi VS Code a GitHub.com pro správu projektů, kontrolu kódu a sledování CI/CD můžete vše řešit pomocí příkazů v přirozeném jazyce a přitom zůstat soustředění na svůj kód.

> **ℹ️ Poznámka: Různé typy 'Agentů'**
> 
> Nesměšujte tento GitHub MCP Server s GitHub Coding Agentem (AI agentem, kterého můžete přiřadit k issue pro automatické programovací úkoly). GitHub MCP Server pracuje v režimu Agenta VS Code, aby poskytl integraci GitHub API, zatímco GitHub Coding Agent je samostatná funkce, která vytváří pull requesty, když je přiřazen k GitHub issues.

**Klíčové schopnosti zahrnují**:
- **⚙️ GitHub Actions**: Kompletní správa CI/CD pipeline, sledování workflow a správa artefaktů
- **🔀 Pull Requesty**: Vytváření, recenze, sloučení a správa PR s podrobným sledováním stavu
- **🐛 Issues**: Kompletní správa životního cyklu issue, komentování, označování a přiřazování
- **🔒 Bezpečnost**: Upozornění na skenování kódu, detekce tajných klíčů a integrace Dependabot
- **🔔 Oznámení**: Inteligentní správa oznámení a kontrola předplatného repozitářů
- **📁 Správa Repozitářů**: Operace se soubory, správa větví a správa repozitářů
- **👥 Spolupráce**: Vyhledávání uživatelů a organizací, správa týmů a kontrola přístupů

**Reálné použití**: „Vytvoř pull request z mé feature větve“, „Ukaž mi všechny neúspěšné CI běhy tento týden“, „Vylistuj otevřená bezpečnostní upozornění pro mé repozitáře“ nebo „Najdi všechny issues přiřazené mně napříč mými organizacemi“

**Úplné demonstrační scénář**: Zde je výkonný pracovní postup, který ukazuje schopnosti GitHub MCP Serveru:

> „Potřebuji se připravit na naši sprint review. Ukaž mi všechny pull requesty, které jsem tento týden vytvořil, zkontroluj stav našich CI/CD pipeline, vytvoř souhrn bezpečnostních upozornění, která musíme řešit, a pomoz mi připravit poznámky k vydání na základě sloučených PR s označením 'feature'.“

GitHub MCP Server:
- Vyhledá vaše nedávné pull requesty s podrobnými informacemi o stavu
- Analyzuje běhy workflow a zvýrazní případné chyby nebo výkonové problémy
- Sestaví výsledky bezpečnostního skenování a priorizuje kritická upozornění
- Vygeneruje podrobné poznámky k vydání extrahováním informací ze sloučených PR
- Poskytne konkrétní další kroky pro plánování sprintu a přípravu vydání

**Ukázka z praxe**: Rád to používám pro pracovní postupy k recenzi kódu. Místo přeskakování mezi VS Code, GitHub notifikacemi a stránkami pull requestů můžu říct „Ukaž mi všechny PR čekající na moji recenzi“ a pak „Přidej komentář k PR #123 s dotazem na zpracování chyb v autentizační metodě.“ Server zpracovává volání GitHub API, udržuje kontext diskuze a dokonce pomáhá vytvořit konstruktivnější recenzní komentáře.

**Možnosti autentizace**: Server podporuje jak OAuth (bezproblémové ve VS Code), tak Personal Access Tokeny, s konfigurovatelnými sady nástrojů, abyste povolili jen funkce GitHub, které potřebujete. Můžete ho spustit jako hostovanou vzdálenou službu pro okamžité nastavení nebo lokálně přes Docker pro plnou kontrolu.

> **💡 Tip pro profesionály**
> 
> Povolte jen ty sady nástrojů, které potřebujete, nastavením parametru `--toolsets` ve vašich nastaveních MCP serveru pro snížení velikosti kontextu a zlepšení výběru AI nástrojů. Například přidejte `"--toolsets", "repos,issues,pull_requests,actions"` do argumentů konfigurace MCP pro základní vývojové pracovní postupy, nebo použijte `"--toolsets", "notifications, security"`, pokud chcete převážně monitorovací funkce GitHubu.
### 4. 🔄 Azure DevOps MCP Server

[![Nainstalovat ve VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Nainstalovat ve VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Co to dělá**: Připojuje se k službám Azure DevOps pro komplexní správu projektů, sledování pracovních položek, správu build pipeline a operace s repozitáři.

**Proč je to užitečné**: Pro týmy, které používají Azure DevOps jako svou primární platformu DevOps, tento MCP server eliminuje neustálé přepínání mezi vývojovým prostředím a webovým rozhraním Azure DevOps. Můžete spravovat pracovní položky, kontrolovat stav buildů, dotazovat repozitáře a řešit úkoly projektového řízení přímo z vašeho AI asistenta.

**Reálné použití**: „Ukaž mi všechny aktivní pracovní položky v aktuálním sprintu pro projekt WebApp“, „Vytvoř hlášení o chybě pro problém s přihlášením, který jsem právě zjistil“ nebo „Zkontroluj stav našich build pipeline a ukaž mi poslední neúspěchy“

**Ukázka z praxe**: Snadno můžeš zkontrolovat stav aktuálního sprintu vašeho týmu jednoduchým dotazem jako „Ukaž mi všechny aktivní pracovní položky v aktuálním sprintu pro projekt WebApp“ nebo „Vytvoř hlášení o chybě pro problém s přihlášením, který jsem právě zjistil“ bez opuštění vývojového prostředí.

### 5. 📝 MarkItDown MCP Server


[![Nainstalujte do VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Nainstalujte do VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Co dělá**: MarkItDown je komplexní server pro konverzi dokumentů, který převádí různé formáty souborů do vysoce kvalitního Markdownu, optimalizovaného pro spotřebu LLM a pracovní postupy textové analýzy.

**Proč je užitečný**: Nezbytný pro moderní pracovní postupy dokumentace! MarkItDown zvládá impozantní škálu formátů souborů a zároveň zachovává kritickou strukturu dokumentu, jako jsou nadpisy, seznamy, tabulky a odkazy. Na rozdíl od jednoduchých nástrojů pro extrakci textu se zaměřuje na udržení sémantického významu a formátování, které je cenné jak pro zpracování AI, tak pro lidskou čitelnost.

**Podporované formáty souborů**:
- **Office dokumenty**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Mediální soubory**: Obrázky (s EXIF metadaty a OCR), Audio (s EXIF metadaty a přepisem řeči)
- **Webový obsah**: HTML, RSS kanály, YouTube URL, Wikipedie stránky
- **Datové formáty**: CSV, JSON, XML, ZIP soubory (rekurzivně zpracovává obsah)
- **Formáty pro publikování**: EPub, Jupyter notebooky (.ipynb)
- **E-mail**: Outlook zprávy (.msg)
- **Pokročilé**: Integrace Azure Document Intelligence pro pokročilé zpracování PDF

**Pokročilé schopnosti**: MarkItDown podporuje popisy obrázků pomocí LLM (při poskytnutí OpenAI klienta), Azure Document Intelligence pro lepší zpracování PDF, přepis audia pro mluvený obsah a systém pluginů pro rozšíření o další formáty souborů.

**Reálné použití**: „Převést tuto PowerPoint prezentaci do Markdownu pro naše dokumentační stránky“, „Extrahovat text z tohoto PDF s řádnou strukturou nadpisů“ nebo „Přeměnit tento Excelový tabulkový soubor do čitelného formátu tabulky“

**Zajímavý příklad**: Citace z [MarkItDown dokumentace](https://github.com/microsoft/markitdown#why-markdown):

> Markdown je extrémně blízký prostému textu, s minimálním značením nebo formátováním, ale přesto poskytuje způsob, jak reprezentovat důležitou strukturu dokumentu. Hlavní LLM jako OpenAI GPT-4o nativně „mluví“ Markdownem a často do svých odpovědí začleňují Markdown bez výzvy. To naznačuje, že byly trénovány na obrovském množství textu ve formátu Markdown a dobře mu rozumějí. Jako vedlejší účinek jsou Markdown konvence také velmi efektivní z hlediska tokenů.

MarkItDown je opravdu dobrý v zachování struktury dokumentu, což je důležité pro AI pracovní postupy. Například při převodu PowerPoint prezentace zachovává organizaci snímků s odpovídajícími nadpisy, extrahuje tabulky jako Markdown tabulky, zahrnuje alternativní text pro obrázky a dokonce zpracovává poznámky přednášejícího. Grafy jsou převedeny na čitelné datové tabulky a výsledný Markdown udržuje logický tok původní prezentace. To je perfektní pro předání obsahu prezentace AI systémům nebo tvorbu dokumentace z existujících snímků.
### 6. 🗃️ SQL Server MCP Server

[![Nainstalujte do VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Nainstalujte do VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co dělá**: Poskytuje konverzační přístup k SQL Server databázím (na místě, Azure SQL nebo Fabric)

**Proč je užitečný**: Podobné jako PostgreSQL server, ale pro ekosystém Microsoft SQL. Připojte se pomocí jednoduchého připojovacího řetězce a začněte dotazovat pomocí přirozeného jazyka – bez nutnosti přepínání kontextu!

**Reálné použití**: „Najdi všechny objednávky, které nebyly splněny za posledních 30 dní“ se přeloží do vhodných SQL dotazů a vrátí naformátované výsledky

**Zajímavý příklad**: Po nastavení připojení k databázi můžete okamžitě začít komunikovat s vašimi daty. Blogový příspěvek to ukazuje jednoduchou otázkou: „k které databázi jste připojen?“ MCP server odpoví vyvoláním vhodného nástroje pro databázi, připojením k vaší instanci SQL Serveru a vrácením podrobností o aktuálním připojení k databázi – to vše bez napsání jediného řádku SQL. Server podporuje komplexní databázové operace od správy schématu po manipulaci s daty, vše pomocí výzev v přirozeném jazyce. Pro kompletní instrukce k nastavení a příklady konfigurace s VS Code a Claude Desktop viz: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP Server

[![Nainstalujte do VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Nainstalujte do VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Co dělá**: Umožňuje AI agentům interagovat s webovými stránkami pro testování a automatizaci

> **ℹ️ Pohání GitHub Copilot**
> 
> Playwright MCP Server pohání Coding Agent GitHub Copilota, který mu dává schopnosti prohlížet web! [Zjistěte více o této funkci](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Proč je užitečný**: Ideální pro automatizované testování řízené popisy v přirozeném jazyce. AI může navigovat na webových stránkách, vyplňovat formuláře a získávat data prostřednictvím strukturovaných snímků přístupnosti – to je neuvěřitelně silná věc!

**Reálné použití**: „Otestuj přihlašovací proces a ověř, že se dashboard načítá správně“ nebo „Vygeneruj test, který vyhledává produkty a ověřuje stránku výsledků“ – vše bez potřeby zdrojového kódu aplikace

**Zajímavý příklad**: Moje kolegyně Debbie O'Brien v poslední době odvádí skvělou práci s Playwright MCP Serverem! Například nedávno ukázala, jak generovat kompletní Playwright testy aniž by měla přístup ke zdrojovému kódu aplikace. V jejím scénáři požádala Copilota o vytvoření testu pro aplikaci na vyhledávání filmů: jdi na web, vyhledej „Garfield“ a ověř, že se film zobrazí ve výsledcích. MCP spustil relaci prohlížeče, prozkoumal strukturu stránky pomocí DOM snapshotů, určil správné selektory a vygeneroval plně funkční TypeScript test, který prošel na první pokus.

Co dělá tuto metodu opravdu silnou, je, že překonává propast mezi instrukcemi v přirozeném jazyce a spustitelným testovacím kódem. Tradiční přístupy vyžadují buď ruční psaní testů, nebo přístup ke zdrojovému kódu pro kontext. Ale s Playwright MCP můžete testovat externí stránky, klientské aplikace nebo pracovat v black-box testovacích scénářích, kde přístup ke kódu není dostupný.


### 8. 💻 Dev Box MCP Server

[![Nainstalujte do VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Nainstalujte do VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co dělá**: Spravuje prostředí Microsoft Dev Box pomocí přirozeného jazyka

**Proč je užitečný**: Obrovsky zjednodušuje správu vývojového prostředí! Vytvářejte, konfigurujte a spravujte vývojová prostředí, aniž byste si museli pamatovat konkrétní příkazy.

**Reálné použití**: „Nastav nový Dev Box s nejnovějším .NET SDK a nakonfiguruj ho pro náš projekt“, „Zkontroluj stav všech mých vývojových prostředí“ nebo „Vytvoř standardizované demo prostředí pro naše týmové prezentace“

**Zajímavý příklad**: Jsem velký fanoušek používání Dev Boxu na vlastní vývoj. Můj moment osvícení byl, když James Montemagno vysvětlil, jak je Dev Box skvělý pro konferenční demo prezentace, protože má superrychlé ethernetové připojení bez ohledu na konferenci / hotel / wi-fi v letadle, které právě používám. Vlastně jsem nedávno nacvičoval konferenční prezentaci, zatímco byl můj notebook připojený k hotspotu mého telefonu během cesty autobusem z Bruges do Antverp! Dalším krokem zde je podívat se na hromadné řízení více vývojových prostředí a standardizovaných demo prostředí. Další velký případ použití, o kterém slyším od zákazníků a kolegů, je samozřejmě použití Dev Boxu pro předkonfigurovaná vývojová prostředí. V obou případech umožňuje použití MCP pro konfiguraci a správu Dev Boxů interakci v přirozeném jazyce, a přitom zůstat ve vývojovém prostředí.

### 9. 🤖 Microsoft Foundry MCP Server


[![Nainstalovat ve VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Nainstalovat ve VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Co dělá**: Microsoft Foundry MCP Server poskytuje vývojářům komplexní přístup k ekosystému Azure AI, včetně katalogů modelů, správy nasazení, indexování znalostí pomocí Azure AI Search a nástrojů pro hodnocení. Tento experimentální server překonává propast mezi vývojem AI a výkonnou AI infrastrukturou Azure, což usnadňuje vytváření, nasazení a hodnocení AI aplikací.

**Proč je užitečný**: Tento server mění způsob, jakým pracujete se službami Azure AI, tím že přináší podnikovou AI funkcionalitu přímo do vašeho vývojového pracovního toku. Místo přepínání mezi Azure portálem, dokumentací a vaším vývojovým prostředím můžete objevovat modely, nasazovat služby, spravovat znalostní báze a hodnotit AI výkon pomocí příkazů v přirozeném jazyce. Je obzvláště užitečný pro vývojáře vytvářející aplikace RAG (Retrieval-Augmented Generation), spravující vícemodelová nasazení nebo implementující komplexní hodnoticí pipeline.

**Klíčové schopnosti pro vývojáře**:
- **🔍 Objevování a nasazení modelů**: Prozkoumejte katalog modelů Microsoft Foundry, získejte podrobné informace o modelech s ukázkami kódu a nasazujte modely do Azure AI služeb
- **📚 Správa znalostí**: Vytvářejte a spravujte Azure AI Search indexy, přidávejte dokumenty, konfigurujte indexery a budujte sofistikované RAG systémy
- **⚡ Integrace AI agentů**: Připojte se k Azure AI agentům, dotazujte existující agenty a hodnotte výkon agentů v produkčních scénářích
- **📊 Hodnotící rámec**: Proveďte komplexní hodnocení textů a agentů, generujte markdown reporty a implementujte zajištění kvality AI aplikací
- **🚀 Nástroje pro prototypování**: Získejte instrukce pro nastavení GitHub-based prototypování a přístup k Microsoft Foundry Labs pro nejmodernější výzkumné modely

**Skutečné příklady použití vývojáři**: "Nasadit model Phi-4 do Azure AI služeb pro mou aplikaci", "Vytvořit nový vyhledávací index pro můj dokumentační RAG systém", "Zhodnotit odezvy mého agenta podle kvalitativních metrik" nebo "Najít nejlepší odvozovací model pro mé složité analytické úlohy"

**Plný demonstrační scénář**: Zde je výkonný AI vývojářský pracovní postup:

> "Vytvářím zákaznického podpůrného agenta. Pomoz mi najít dobrý odvodzovací model v katalogu, nasadit ho do Azure AI služeb, vytvořit znalostní bázi z naší dokumentace, nastavit hodnoticí rámec pro testování kvality odpovědí a poté mi pomoci s prototypováním integrace s GitHub tokenem pro testování."

Microsoft Foundry MCP Server:
- Prohledá katalog modelů a doporučí optimální odvodzovací modely podle tvých požadavků
- Poskytne příkazy pro nasazení a informace o kvótách pro tvůj preferovaný Azure region
- Nastaví Azure AI Search indexy s vhodným schématem pro tvou dokumentaci
- Nakonfiguruje hodnoticí pipeline s kvalitativními metrikami a bezpečnostními kontrolami
- Vygeneruje prototypovací kód s GitHub autentizací pro okamžité testování
- Poskytne komplexní návody pro nastavení přizpůsobené tvému technologickému stacku

**Vybraný příklad**: Jako vývojář jsem měl problém držet krok s dostupnými LLM modely. Znám pár hlavních, ale měl jsem pocit, že mi unikají některé produktivitní a efektivní výhody. Tokeny a kvóty jsou stresující a těžko se spravují – nikdy nevím, jestli vybírám správný model pro správný úkol, nebo jestli neplytvám svým rozpočtem neefektivně. Nedávno jsem slyšel o tomto MCP Serveru od Jamese Montemagna, když jsem se ptal kolegů na doporučení MCP Serverů pro tento příspěvek, a těším se, že ho vyzkouším! Schopnosti objevování modelů vypadají obzvlášť působivě pro někoho jako já, kdo chce prozkoumat víc než obvyklé volby a najít modely optimalizované pro specifické úkoly. Hodnotící rámec by mi měl pomoci ověřit, že skutečně dosahuji lepších výsledků, ne jen zkouším něco nového kvůli novosti.

> **ℹ️ Experimentální stav**
> 
> Tento MCP server je experimentální a aktivně vyvíjený. Funkce a API se mohou měnit. Ideální pro prozkoumání možností Azure AI a tvorbu prototypů, ale pro produkční použití je třeba ověřit stabilitu.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Nainstalovat ve VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Nainstalovat ve VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Co dělá**: Poskytuje vývojářům základní nástroje pro vytváření AI agentů a aplikací integrujících se s Microsoft 365 a Microsoft 365 Copilot, včetně ověření schématu, získání ukázkového kódu a asistence při řešení problémů.

**Proč je užitečný**: Vývoj pro Microsoft 365 a Copilot zahrnuje složitá schémata manifestů a specifické vývojové vzory. Tento MCP server přináší klíčové vývojářské zdroje přímo do vašeho kódovacího prostředí, pomáhá vám ověřit schémata, najít ukázkový kód a řešit běžné problémy bez neustálého odkazování na dokumentaci.

**Skutečné použití**: "Ověřit manifest deklarativního agenta a opravit chyby ve schématu", "Ukázat mi ukázkový kód pro implementaci Microsoft Graph API pluginu" nebo "Pomoci mi vyřešit problémy s autentizací mé Teams aplikace"

**Vybraný příklad**: Po rozhovoru s Johnem Millerem na Buildu o M365 Agents jsem ho kontaktoval a doporučil mi tento MCP. Může být skvělý pro vývojáře nováčky v M365 Agents, protože nabízí šablony, ukázkový kód a základní struktury pro snadný start bez zahlcení dokumentací. Funkce ověření schématu vypadá obzvlášť užitečně pro zabránění chybám ve struktuře manifestu, které mohou způsobovat hodiny ladění.

> **💡 Tip na závěr**
> 
> Používejte tento server společně s Microsoft Learn Docs MCP Serverem pro komplexní podporu vývoje v M365 – jeden poskytuje oficiální dokumentaci, zatímco tento nabízí praktické vývojové nástroje a asistenci při řešení problémů.


## Co dál? 🔮

## 📋 Závěr

Protokol Model Context Protocol (MCP) mění způsob, jakým vývojáři komunikují s AI asistenty a externími nástroji. Těchto 10 Microsoft MCP serverů ukazuje sílu standardizované AI integrace, umožňující plynulé pracovní postupy, které udržují vývojáře v jejich toku při přístupu k výkonným externím schopnostem.

Od komplexní integrace Azure ekosystému po specializované nástroje jako Playwright pro automatizaci prohlížeče a MarkItDown pro zpracování dokumentů, tyto servery ukazují, jak MCP může zvýšit produktivitu v různých vývojářských scénářích. Standardizovaný protokol zajišťuje, že tyto nástroje fungují bezproblémově spolu a vytváří ucelený vývojářský zážitek.

Jak se MCP ekosystém dál rozvíjí, klíčem k maximální produktivitě ve vývoji bude aktivní účast v komunitě, prozkoumávání nových serverů a tvorba vlastních řešení. Otevřený standard MCP znamená, že si můžete kombinovat nástroje od různých dodavatelů a vytvořit si tak ideální pracovní postup pro své specifické potřeby.

## 🔗 Další zdroje

- [Oficiální Microsoft MCP repozitář](https://github.com/microsoft/mcp)
- [MCP komunita a dokumentace](https://modelcontextprotocol.io/introduction)
- [VS Code MCP dokumentace](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP dokumentace](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP dokumentace](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Pojďme se učit – MCP události](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Úžasné úpravy GitHub Copilota](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days naživo 29./30. července nebo sledovat na vyžádání](https://aka.ms/mcpdevdays)

## 🎯 Cvičení

1. **Nainstalujte a nakonfigurujte**: Nainstalujte jeden z MCP serverů ve vašem VS Code prostředí a otestujte základní funkce.
2. **Integrace pracovního toku**: Navrhněte vývojářský pracovní postup, který kombinuje alespoň tři různé MCP servery.
3. **Plánování vlastního serveru**: Identifikujte úkol ve vašem denním vývojovém režimu, který by mohl těžit z vlastního MCP serveru, a vytvořte jeho specifikaci.
4. **Analýza výkonu**: Porovnejte efektivitu používání MCP serverů oproti tradičním přístupům pro běžné vývojové úkoly.
5. **Hodnocení bezpečnosti**: Zhodnoťte bezpečnostní aspekty používání MCP serverů ve vašem vývojovém prostředí a navrhněte nejlepší postupy.


Další: [Nejlepší praktiky](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->