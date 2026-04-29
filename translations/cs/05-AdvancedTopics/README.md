# Pokročilá témata v MCP

[![Pokročilé MCP: zabezpečené, škálovatelné a multimodální AI agenty](../../../translated_images/cs/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klikněte na obrázek výše pro zobrazení videa k této lekci)_

Tato kapitola pokrývá sérii pokročilých témat v implementaci Model Context Protocol (MCP), včetně multimodální integrace, škálovatelnosti, nejlepších praktik zabezpečení a integrace do podnikových systémů. Tato témata jsou zásadní pro tvorbu robustních a produkčně připravených aplikací MCP, které dokážou splnit požadavky moderních AI systémů.

## Přehled

Tato lekce zkoumá pokročilé koncepty implementace Model Context Protocol, se zaměřením na multimodální integraci, škálovatelnost, nejlepší bezpečnostní praktiky a podnikovou integraci. Tato témata jsou nezbytná pro budování produkčně kvalitních aplikací MCP, které zvládnou složité požadavky v podnikových prostředích.

## Výukové cíle

Na konci této lekce budete schopni:

- Implementovat multimodální schopnosti v rámci MCP frameworku
- Navrhnout škálovatelné MCP architektury pro scénáře s vysokou zátěží
- Aplikovat nejlepší bezpečnostní praktiky v souladu s bezpečnostními principy MCP
- Integrovat MCP s podnikovými AI systémy a rámci
- Optimalizovat výkon a spolehlivost v produkčním prostředí

## Lekce a ukázkové projekty

| Odkaz | Název | Popis |
|------|-------|-------------|
| [5.1 Integrace s Azure](./mcp-integration/README.md) | Integrace s Azure | Naučte se, jak integrovat váš MCP server na Azure |
| [5.2 Multimodální ukázka](./mcp-multi-modality/README.md) | MCP multimodální ukázky | Ukázky pro audio, obraz a multimodální odpovědi |
| [5.3 MCP OAuth2 ukázka](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimální aplikace Spring Boot ukazující OAuth2 s MCP, jakož i autorizační a zdrojový server. Demonstruje zabezpečené vydávání tokenů, chráněné koncové body, nasazení na Azure Container Apps a integraci s API Management. |
| [5.4 Kořenové kontexty](./mcp-root-contexts/README.md) | Kořenové kontexty | Naučte se více o kořenovém kontextu a jak jej implementovat |
| [5.5 Směrování](./mcp-routing/README.md) | Směrování | Naučte se různé typy směrování |
| [5.6 Vzorkování](./mcp-sampling/README.md) | Vzorkování | Naučte se, jak pracovat se vzorkováním |
| [5.7 Škálování](./mcp-scaling/README.md) | Škálování | Naučte se o škálování |
| [5.8 Zabezpečení](./mcp-security/README.md) | Zabezpečení | Zabezpečte svůj MCP server |
| [5.9 Webové vyhledávání MCP](./web-search-mcp/README.md) | Webové vyhledávání MCP | Python MCP server a klient integrující se s SerpAPI pro vyhledávání na webu, novinkách, produktech a Q&A v reálném čase. Demonstruje orchestraci více nástrojů, integraci externích API a robustní zpracování chyb. |
| [5.10 Streamování v reálném čase](./mcp-realtimestreaming/README.md) | Streamování | Streamování dat v reálném čase se stalo klíčovým v dnešním světě řízeném daty, kde firmy a aplikace vyžadují okamžitý přístup k informacím pro rychlé rozhodování. |
| [5.11 Webové vyhledávání v reálném čase](./mcp-realtimesearch/README.md) | Webové vyhledávání | Jak MCP transformuje webové vyhledávání v reálném čase poskytováním standardizovaného přístupu k řízení kontextu napříč AI modely, vyhledávači a aplikacemi. |
| [5.12 Autentizace Entra ID pro servery Model Context Protocol](./mcp-security-entra/README.md) | Autentizace Entra ID | Microsoft Entra ID poskytuje robustní cloudové řešení pro správu identity a přístupů, které zajišťuje, že pouze autorizovaní uživatelé a aplikace mohou komunikovat s vaším MCP serverem. |
| [5.13 Integrace Azure AI Foundry agenta](./mcp-foundry-agent-integration/README.md) | Integrace Azure AI Foundry | Naučte se, jak integrovat Model Context Protocol servery s Azure AI Foundry agenty, což umožňuje výkonnou orchestraci nástrojů a podnikové AI schopnosti se standardizovanými připojeními k externím zdrojům dat. |
| [5.14 Inženýrství kontextu](./mcp-contextengineering/README.md) | Inženýrství kontextu | Budoucí příležitosti technik inženýrství kontextu pro MCP servery, včetně optimalizace kontextu, dynamické správy kontextu a strategií efektivního návrhu promptů v rámci MCP frameworků. |
| [5.15 Vlastní transport MCP](./mcp-transport/README.md) | Vlastní transport | Naučte se implementovat vlastní transportní mechanismy pro specializované scénáře komunikace MCP. |
| [5.16 Hluboký průzkum funkcí protokolu](./mcp-protocol-features/README.md) | Funkce protokolu | Ovládněte pokročilé funkce protokolu včetně notifikací o průběhu, zrušení požadavků, šablon zdrojů a vzorů zpracování chyb. |
| [5.17 Adversariální multi-agentní uvažování](./mcp-adversarial-agents/README.md) | Adversariální agenti | Použijte dva agenty s protichůdnými názory, sdílející jeden MCP nástrojový set, k identifikaci halucinací, odhalení hranic případů a vytváření lépe kalibrovaných výstupů skrze strukturovanou debatu. |

> **Novinky ve specifikaci MCP 2025-11-25**: Specifikace nyní zahrnuje experimentální podporu pro **Úkoly** (dlouhodobé operace s průběžným sledováním), **Anotace nástrojů** (metadata o chování nástrojů pro bezpečnost), **URL mód vyžádání** (vyžádání konkrétního obsahu URL od klientů) a rozšířené **Kořeny** (pro správu pracovních kontextů). Kompletní detaily naleznete v [changelog specifikace MCP](https://spec.modelcontextprotocol.io/).

## Další odkazy

Pro nejaktuálnější informace o pokročilých tématech MCP si prostudujte:
- [Dokumentace MCP](https://modelcontextprotocol.io/)
- [Specifikace MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub repozitář](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Bezpečnostní rizika a opatření
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktický bezpečnostní trénink

## Klíčové poznatky

- Multimodální implementace MCP rozšiřují AI schopnosti nad rámec zpracování textu
- Škálovatelnost je zásadní pro nasazení v podnikovém prostředí a je možné ji řešit horizontálním i vertikálním škálováním
- Komplexní bezpečnostní opatření chrání data a zajišťují správnou kontrolu přístupu
- Podniková integrace s platformami jako Azure OpenAI a Microsoft AI Foundry rozšiřuje schopnosti MCP
- Pokročilé implementace MCP těží z optimalizovaných architektur a pečlivého řízení zdrojů

## Cvičení

Navrhněte podnikovou implementaci MCP pro konkrétní případ použití:

1. Identifikujte multimodální požadavky pro váš případ použití
2. Nastíněte bezpečnostní opatření potřebná pro ochranu citlivých dat
3. Navrhněte škálovatelnou architekturu, která zvládne proměnlivé zatížení
4. Naplánujte integrační body s podniková AI systémy
5. Zdokumentujte možné výkonové úzká místa a strategie jejich zmírnění

## Další zdroje

- [Dokumentace Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Dokumentace Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Co dál

Prozkoumejte lekce v tomto modulu začínaje: [5.1 Integrace MCP](./mcp-integration/README.md)

Po dokončení tohoto modulu pokračujte na: [Modul 6: Příspěvky komunity](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho originálním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->