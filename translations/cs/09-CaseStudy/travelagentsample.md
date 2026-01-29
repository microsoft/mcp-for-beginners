# Případová studie: Azure AI Travel Agents – Referenční implementace

## Přehled

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) je komplexní referenční řešení vyvinuté společností Microsoft, které ukazuje, jak vytvořit aplikaci pro plánování cest s více agenty poháněnou umělou inteligencí pomocí Model Context Protocol (MCP), Azure OpenAI a Azure AI Search. Tento projekt představuje osvědčené postupy pro orchestraci více AI agentů, integraci podnikových dat a poskytování bezpečné, rozšiřitelné platformy pro reálné scénáře.

## Klíčové vlastnosti
- **Orchestrace více agentů:** Využívá MCP k koordinaci specializovaných agentů (např. agenti pro lety, hotely a itineráře), kteří spolupracují na plnění složitých úkolů při plánování cest.
- **Integrace podnikových dat:** Připojuje se k Azure AI Search a dalším podnikových zdrojům dat, aby poskytl aktuální a relevantní informace pro cestovní doporučení.
- **Bezpečná a škálovatelná architektura:** Využívá služby Azure pro autentizaci, autorizaci a škálovatelné nasazení podle nejlepších bezpečnostních praktik pro podniky.
- **Rozšiřitelné nástroje:** Implementuje znovupoužitelné MCP nástroje a šablony promptů, což umožňuje rychlé přizpůsobení novým oblastem nebo obchodním požadavkům.
- **Uživatelská zkušenost:** Nabízí konverzační rozhraní, kde uživatelé komunikují s cestovními agenty, poháněné Azure OpenAI a MCP.

## Architektura
![Architektura](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Popis architektonického diagramu

Řešení Azure AI Travel Agents je navrženo s důrazem na modularitu, škálovatelnost a bezpečnou integraci více AI agentů a podnikových zdrojů dat. Hlavní komponenty a tok dat jsou následující:

- **Uživatelské rozhraní:** Uživatelé komunikují se systémem prostřednictvím konverzačního UI (například webový chat nebo Teams bot), které odesílá uživatelské dotazy a přijímá cestovní doporučení.
- **MCP Server:** Slouží jako centrální orchestrátor, přijímá vstupy od uživatele, spravuje kontext a koordinuje činnosti specializovaných agentů (např. FlightAgent, HotelAgent, ItineraryAgent) pomocí Model Context Protocol.
- **AI agenti:** Každý agent je zodpovědný za konkrétní oblast (lety, hotely, itineráře) a je implementován jako MCP nástroj. Agenti používají šablony promptů a logiku k zpracování požadavků a generování odpovědí.
- **Azure OpenAI Service:** Poskytuje pokročilé porozumění přirozenému jazyku a generování textu, což umožňuje agentům interpretovat uživatelský záměr a vytvářet konverzační odpovědi.
- **Azure AI Search & podniková data:** Agenti dotazují Azure AI Search a další podnikové zdroje dat, aby získali aktuální informace o letech, hotelech a možnostech cestování.
- **Autentizace a bezpečnost:** Integruje se s Microsoft Entra ID pro bezpečnou autentizaci a uplatňuje princip nejmenších oprávnění ke všem zdrojům.
- **Nasazení:** Navrženo pro nasazení na Azure Container Apps, což zajišťuje škálovatelnost, monitoring a efektivní provoz.

Tato architektura umožňuje plynulou orchestraci více AI agentů, bezpečnou integraci podnikových dat a robustní, rozšiřitelnou platformu pro vytváření AI řešení specifických pro danou oblast.

## Podrobný popis architektonického diagramu krok za krokem
Představte si, že plánujete velký výlet a máte tým odborných asistentů, kteří vám pomáhají s každým detailem. Systém Azure AI Travel Agents funguje podobně, používá různé části (jako členy týmu), z nichž každý má svou specializaci. Takto to všechno funguje dohromady:

### Uživatelské rozhraní (UI):
Představte si to jako přepážku vašeho cestovního agenta. Zde vy (uživatel) kladete otázky nebo zadáváte požadavky, například „Najdi mi let do Paříže.“ Může to být chatovací okno na webu nebo v aplikaci pro zasílání zpráv.

### MCP Server (Koordinátor):
MCP Server je jako manažer, který poslouchá váš požadavek na přepážce a rozhoduje, který specialista by měl řešit jednotlivé části. Sleduje průběh konverzace a zajišťuje, že vše probíhá hladce.

### AI agenti (Specialisté):
Každý agent je odborník na určitou oblast – jeden zná vše o letech, druhý o hotelech a další o plánování itineráře. Když požádáte o cestu, MCP Server předá váš požadavek správnému agentovi nebo agentům. Ti využívají své znalosti a nástroje, aby našli nejlepší možnosti pro vás.

### Azure OpenAI Service (Jazykový expert):
Je to jako mít jazykového experta, který přesně rozumí tomu, co žádáte, bez ohledu na to, jak to formulujete. Pomáhá agentům pochopit vaše požadavky a odpovídat přirozeným, konverzačním jazykem.

### Azure AI Search & podniková data (Informační knihovna):
Představte si obrovskou, aktuální knihovnu se všemi nejnovějšími informacemi o cestování – letové řády, dostupnost hotelů a další. Agenti tuto knihovnu prohledávají, aby vám poskytli co nejpřesnější odpovědi.

### Autentizace a bezpečnost (Bezpečnostní stráž):
Stejně jako bezpečnostní stráž kontroluje, kdo může vstoupit do určitých prostor, tato část zajišťuje, že pouze oprávněné osoby a agenti mají přístup k citlivým informacím. Vaše data tak zůstávají v bezpečí a soukromí.

### Nasazení na Azure Container Apps (Budova):
Všichni tito asistenti a nástroje spolupracují uvnitř bezpečné, škálovatelné „budovy“ (cloudu). To znamená, že systém zvládne obsloužit mnoho uživatelů najednou a je vždy k dispozici, když ho potřebujete.

## Jak to všechno funguje dohromady:

Začnete tím, že položíte otázku na přepážce (UI).  
Manažer (MCP Server) zjistí, který specialista (agent) vám má pomoci.  
Specialista využije jazykového experta (OpenAI), aby pochopil váš požadavek, a knihovnu (AI Search), aby našel nejlepší odpověď.  
Bezpečnostní stráž (Autentizace) zajistí, že je vše v bezpečí.  
To vše probíhá uvnitř spolehlivé, škálovatelné budovy (Azure Container Apps), takže vaše zkušenost je plynulá a bezpečná.  
Tato týmová spolupráce umožňuje systému rychle a bezpečně pomoci s plánováním vaší cesty, stejně jako tým zkušených cestovních agentů pracujících společně v moderní kanceláři!

## Technická implementace
- **MCP Server:** Hostuje hlavní orchestraci, zpřístupňuje nástroje agentů a spravuje kontext pro vícestupňové pracovní postupy plánování cest.
- **Agenti:** Každý agent (např. FlightAgent, HotelAgent) je implementován jako MCP nástroj se svými vlastními šablonami promptů a logikou.
- **Integrace Azure:** Využívá Azure OpenAI pro porozumění přirozenému jazyku a Azure AI Search pro získávání dat.
- **Bezpečnost:** Integruje se s Microsoft Entra ID pro autentizaci a uplatňuje princip nejmenších oprávnění ke všem zdrojům.
- **Nasazení:** Podporuje nasazení do Azure Container Apps pro škálovatelnost a efektivní provoz.

## Výsledky a dopad
- Ukazuje, jak lze MCP využít k orchestraci více AI agentů v reálném, produkčním prostředí.
- Urychluje vývoj řešení díky poskytování znovupoužitelných vzorů pro koordinaci agentů, integraci dat a bezpečné nasazení.
- Slouží jako vzor pro vytváření oborově specifických aplikací poháněných AI pomocí MCP a služeb Azure.

## Reference
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.