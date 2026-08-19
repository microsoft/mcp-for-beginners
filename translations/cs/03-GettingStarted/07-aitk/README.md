# Používání serveru z rozšíření AI Toolkit pro Visual Studio Code

Když vytváříte AI agenta, nejde jen o generování chytrých odpovědí; jde také o to, dát agentovi možnost jednat. Zde přichází na řadu Model Context Protocol (MCP). MCP usnadňuje agentům přístup k externím nástrojům a službám konzistentním způsobem. Představte si to jako připojení vašeho agenta do toolboxu, který *opravdu* může využívat.

Řekněme, že připojíte agenta k vašemu MCP serveru kalkulačky. Najednou může váš agent provádět matematické operace pouze tím, že obdrží výzvu jako „Kolik je 47 krát 89?“ — není potřeba tvrdě kódovat logiku nebo budovat vlastní API.

## Přehled

V této lekci si ukážeme, jak připojit server kalkulačky MCP k agentovi pomocí rozšíření [AI Toolkit](https://aka.ms/AIToolkit) ve Visual Studio Code, což umožní vašemu agentovi provádět matematické operace, jako je sčítání, odčítání, násobení a dělení pomocí přirozeného jazyka.

AI Toolkit je výkonné rozšíření pro Visual Studio Code, které zjednodušuje vývoj agentů. AI inženýři mohou snadno vytvářet AI aplikace vyvíjením a testováním generativních AI modelů — lokálně nebo v cloudu. Rozšíření podporuje většinu hlavních generativních modelů dostupných dnes.

*Poznámka*: AI Toolkit aktuálně podporuje Python a TypeScript.

## Cíle učení

Na konci této lekce budete schopni:

- Používat MCP server přes AI Toolkit.
- Konfigurovat agentovu konfiguraci tak, aby mohl objevit a využívat nástroje poskytované MCP serverem.
- Využívat MCP nástroje pomocí přirozeného jazyka.

## Přístup

Zde je postup, jak k tomu přistoupit na vyšší úrovni:

- Vytvořit agenta a definovat jeho systémovou výzvu.
- Vytvořit MCP server s kalkulačními nástroji.
- Připojit Agent Builder k MCP serveru.
- Otestovat vyvolání nástroje agenta přes přirozený jazyk.

Skvělé, nyní když chápeme tok, nakonfigurujme AI agenta tak, aby využil externí nástroje přes MCP a vylepšil své schopnosti!

## Požadavky

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pro Visual Studio Code](https://aka.ms/AIToolkit)

## Cvičení: Používání serveru

> [!WARNING]
> Poznámka pro uživatele macOS. Nyní zjišťujeme problém s instalací závislostí na macOS. V důsledku toho uživatelé macOS nyní tuto lekci nemohou dokončit. Jakmile bude k dispozici oprava, instrukce aktualizujeme. Děkujeme za trpělivost a pochopení!

V tomto cvičení si vytvoříte, spustíte a vylepšíte AI agenta s nástroji z MCP serveru přímo ve Visual Studio Code pomocí AI Toolkitu.

### -0- Předkrok, přidat model OpenAI GPT-4o do My Models

Cvičení využívá model **GPT-4o**. Model by měl být přidán do **My Models** před vytvořením agenta.

![Screenshot rozhraní výběru modelu v AI Toolkit rozšíření Visual Studio Code. Nadpis říká „Find the right model for your AI Solution“ s podnadpisem vybízejícím objevit, testovat a nasadit AI modely. Pod tím, sekce “Popular Models” se šesti kartami modelů: DeepSeek-R1 (hostováno na GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast) a DeepSeek-R1 (hostováno na Ollama). Každá karta obsahuje možnosti „Add“ nebo „Try in Playground“](../../../../translated_images/cs/aitk-model-catalog.2acd38953bb9c119.webp)

1. Otevřete rozšíření **AI Toolkit** z **Activity Bar**.
1. V sekci **Catalog** vyberte **Models** pro otevření **Model Catalog**. Výběr **Models** otevře **Model Catalog** v nové záložce editoru.
1. Ve vyhledávacím poli **Model Catalog** zadejte **OpenAI GPT-4o**.
1. Klikněte na **+ Add** pro přidání modelu do seznamu **My Models**. Ujistěte se, že jste vybrali model, který je **hostovaný na GitHub**.
1. V **Activity Bar** potvrďte, že model **OpenAI GPT-4o** se objevil v seznamu.

### -1- Vytvořit agenta

**Agent (Prompt) Builder** umožňuje vytvářet a přizpůsobovat své vlastní AI-powered agenty. V této sekci vytvoříte nového agenta a přiřadíte model, který bude pohánět konverzaci.

![Screenshot rozhraní "Calculator Agent" builderu v AI Toolkit rozšíření Visual Studio Code. Na levém panelu je vybraný model „OpenAI GPT-4o (via GitHub).“ Systémová výzva říká „Jste profesor na univerzitě, který vyučuje matematiku,“ a uživatelská výzva říká „Vysvětli mi Fourierovu rovnici jednoduše.“ Další možnosti zahrnují tlačítka pro přidání nástrojů, aktivaci MCP Server a výběr strukturovaného výstupu. Dole je modré tlačítko „Run.“ Na pravém panelu, pod „Get Started with Examples,“ jsou tři ukázkové agenti: Web Developer (s MCP Serverem, Second-Grade Simplifier a Dream Interpreter, každý s krátkým popisem jejich funkcí.](../../../../translated_images/cs/aitk-agent-builder.901e3a2960c3e477.webp)

1. Otevřete rozšíření **AI Toolkit** z **Activity Bar**.
1. V sekci **Tools** vyberte **Agent (Prompt) Builder**. Výběr **Agent (Prompt) Builder** otevře tuto funkci v nové záložce editoru.
1. Klikněte na tlačítko **+ New Agent**. Rozšíření spustí průvodce nastavením přes **Command Palette**.
1. Zadejte jméno **Calculator Agent** a stiskněte **Enter**.
1. V **Agent (Prompt) Builder** u pole **Model** vyberte model **OpenAI GPT-4o (via GitHub)**.

### -2- Vytvořit systémovou výzvu pro agenta

Po zprovoznění agenta je čas definovat jeho osobnost a účel. V této sekci použijete funkci **Generate system prompt** k popsání zamýšleného chování agenta — v tomto případě kalkulačkového agenta — a nechat model, aby pro vás vytvořil systémovou výzvu.

![Screenshot rozhraní "Calculator Agent" v AI Toolkit pro Visual Studio Code s otevřeným modálním oknem s názvem "Generate a prompt." Modal vysvětluje, že lze vygenerovat šablonu výzvy sdílením základních detailů a obsahuje textové pole s ukázkovou systémovou výzvou: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Pod textovým polem jsou tlačítka "Close" a "Generate." V pozadí je viditelná část konfigurace agenta, včetně vybraného modelu "OpenAI GPT-4o (via GitHub)" a polí pro systémovou a uživatelskou výzvu.](../../../../translated_images/cs/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. V sekci **Prompts** klikněte na tlačítko **Generate system prompt**. Toto tlačítko otevře tvůrce výzev, který využívá AI k vytvoření systémové výzvy pro agenta.
1. V okně **Generate a prompt** zadejte následující text: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Klikněte na tlačítko **Generate**. V pravém dolním rohu se zobrazí oznámení potvrzující, že se generuje systémová výzva. Po dokončení generování se výzva objeví v poli **System prompt** v **Agent (Prompt) Builder**.
1. Zkontrolujte **System prompt** a případně ji upravte.

### -3- Vytvořit MCP server

Nyní, když jste definovali systémovou výzvu agenta — která řídí jeho chování a odpovědi — je čas vybavit agenta praktickými funkcemi. V této sekci vytvoříte kalkulační MCP server s nástroji pro provádění sčítání, odčítání, násobení a dělení. Tento server umožní vašemu agentovi provádět matematické operace v reálném čase na základě přirozených jazykových požadavků.

![Screenshot dolní části rozhraní Calculator Agent v AI Toolkit rozšíření pro Visual Studio Code. Ukazuje rozbalovací menu “Tools” a “Structure output,” spolu s rozevíracím menu označeným „Choose output format“ nastaveným na „text.“ Vpravo je tlačítko „+ MCP Server“ pro přidání Model Context Protocol serveru. Nad sekcí Tools je zástupný symbol obrázku.](../../../../translated_images/cs/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit je vybaven šablonami pro snadné vytvoření vlastního MCP serveru. Použijeme Python šablonu pro vytvoření kalkulačního MCP serveru.

*Poznámka*: AI Toolkit aktuálně podporuje Python a TypeScript.

1. V sekci **Tools** v **Agent (Prompt) Builder** klikněte na tlačítko **+ MCP Server**. Rozšíření spustí průvodce nastavením přes **Command Palette**.
1. Vyberte **+ Add Server**.
1. Vyberte **Create a New MCP Server**.
1. Vyberte šablonu **python-weather**.
1. Vyberte **Default folder** pro uložení MCP server šablony.
1. Zadejte následující název serveru: **Calculator**
1. Otevře se nové okno Visual Studio Code. Vyberte **Yes, I trust the authors**.
1. Pomocí terminálu (**Terminal** > **New Terminal**) vytvořte virtuální prostředí: `python -m venv .venv`
1. Pomocí terminálu aktivujte virtuální prostředí:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Pomocí terminálu nainstalujte závislosti: `pip install -e .[dev]`
1. V zobrazení **Explorer** v **Activity Bar** rozbalte adresář **src** a vyberte soubor **server.py** pro otevření v editoru.
1. Nahraďte kód v souboru **server.py** následujícím a uložte:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Spustit agenta s MCP serverem kalkulačky

Nyní, když má váš agent nástroje, je čas je využít! V této sekci budete agentovi zadávat výzvy, abyste otestovali a ověřili, zda agent využívá správný nástroj z kalkulačního MCP serveru.

![Screenshot rozhraní Calculator Agent v AI Toolkit rozšíření pro Visual Studio Code. Na levém panelu, pod “Tools,” je přidán MCP server s názvem local-server-calculator_server, zobrazující čtyři dostupné nástroje: add, subtract, multiply a divide. Odznak ukazuje, že čtyři nástroje jsou aktivní. Pod tím je složená sekce „Structure output“ a modré tlačítko „Run.“ Na pravém panelu, pod „Model Response,“ agent vyvolává nástroje multiply a subtract s vstupy {"a": 3, "b": 25} a {"a": 75, "b": 20} respektive. Konečná „Tool Response“ je zobrazena jako 75.0. Tlačítko „View Code“ je na spodku.](../../../../translated_images/cs/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Kalkulační MCP server poběží na vašem lokálním vývojovém počítači přes **Agent Builder** jako MCP klient.

1. Stiskněte `F5` pro spuštění ladění MCP serveru. **Agent (Prompt) Builder** se otevře v nové záložce editoru. Stav serveru je viditelný v terminálu.
1. Do pole **User prompt** v **Agent (Prompt) Builder** zadejte následující výzvu: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Klikněte na tlačítko **Run** pro vygenerování odpovědi agenta.
1. Zkontrolujte výstup agenta. Model by měl dojít k závěru, že jste zaplatili **55 $**.
1. Zde je rozpis, co by se mělo stát:
    - Agent vybere nástroje **multiply** a **subtract** pro pomoc s výpočtem.
    - Příslušné hodnoty `a` a `b` jsou přiřazeny pro nástroj **multiply**.
    - Příslušné hodnoty `a` a `b` jsou přiřazeny pro nástroj **subtract**.
    - Odpověď z každého nástroje je uvedena v příslušném poli **Tool Response**.
    - Konečný výstup z modelu je uveden v konečné **Model Response**.
1. Zadejte další výzvy a otestujte agenta. Můžete upravit existující výzvu v poli **User prompt** kliknutím dovnitř a nahrazením textu.
1. Po testování agenta server zastavíte v terminálu stisknutím **CTRL/CMD+C** pro ukončení.

## Zadání

Zkuste přidat další nástroj do souboru **server.py** (například vrácení druhé odmocniny čísla). Zadejte další výzvy, které budou vyžadovat, aby agent využil váš nový nástroj (nebo existující nástroje). Nezapomeňte restartovat server, aby se načetly nově přidané nástroje.

## Řešení

[Řešení](./solution/README.md)

## Klíčové poznatky

Z této kapitoly si odnášíme následující:

- Rozšíření AI Toolkit je skvělý klient, který vám umožní používat MCP servery a jejich nástroje.
- Můžete přidávat nové nástroje do MCP serverů, čímž rozšiřujete schopnosti agenta podle vyvíjejících se požadavků.
- AI Toolkit obsahuje šablony (např. Python MCP server šablony), které usnadňují vytváření vlastních nástrojů.

## Další zdroje

- [Dokumentace AI Toolkit](https://aka.ms/AIToolkit/doc)

## Co dál
- Další: [Testování a ladění](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->