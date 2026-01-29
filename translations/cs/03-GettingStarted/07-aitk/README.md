# Spotřebovávání serveru z rozšíření AI Toolkit pro Visual Studio Code

Když vytváříte AI agenta, nejde jen o generování chytrých odpovědí; jde také o to, dát vašemu agentovi schopnost jednat. A právě zde přichází na řadu Model Context Protocol (MCP). MCP umožňuje agentům snadno a konzistentně přistupovat k externím nástrojům a službám. Představte si to jako připojení vašeho agenta k nástrojové sadě, kterou může *skutečně* používat.

Představte si, že připojíte agenta k MCP serveru kalkulačky. Najednou váš agent dokáže provádět matematické operace jen na základě zadání, jako je „Kolik je 47 krát 89?“—není třeba hardcodovat logiku nebo vytvářet vlastní API.

## Přehled

Tato lekce pokrývá, jak připojit MCP server kalkulačky k agentovi pomocí rozšíření [AI Toolkit](https://aka.ms/AIToolkit) ve Visual Studio Code, což umožní vašemu agentovi provádět matematické operace, jako je sčítání, odčítání, násobení a dělení, prostřednictvím přirozeného jazyka.

AI Toolkit je výkonné rozšíření pro Visual Studio Code, které zjednodušuje vývoj agentů. AI inženýři mohou snadno vytvářet AI aplikace tím, že vyvíjejí a testují generativní AI modely—lokálně nebo v cloudu. Rozšíření podporuje většinu hlavních generativních modelů dostupných dnes.

*Poznámka*: AI Toolkit aktuálně podporuje Python a TypeScript.

## Cíle učení

Na konci této lekce budete schopni:

- Spotřebovávat MCP server prostřednictvím AI Toolkitu.
- Nakonfigurovat konfiguraci agenta tak, aby mohl objevovat a využívat nástroje poskytované MCP serverem.
- Využívat MCP nástroje prostřednictvím přirozeného jazyka.

## Přístup

Zde je přehledný postup, jak na to:

- Vytvořte agenta a definujte jeho systémový prompt.
- Vytvořte MCP server s nástroji kalkulačky.
- Připojte Agent Builder k MCP serveru.
- Otestujte vyvolání nástrojů agenta prostřednictvím přirozeného jazyka.

Skvělé, teď když rozumíme postupu, pojďme nakonfigurovat AI agenta, aby využíval externí nástroje prostřednictvím MCP a rozšířil tak své schopnosti!

## Předpoklady

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pro Visual Studio Code](https://aka.ms/AIToolkit)

## Cvičení: Spotřebovávání serveru

> [!WARNING]
> Poznámka pro uživatele macOS. Aktuálně zkoumáme problém, který ovlivňuje instalaci závislostí na macOS. Z tohoto důvodu uživatelé macOS nebudou schopni toto cvičení momentálně dokončit. Jakmile bude k dispozici oprava, aktualizujeme pokyny. Děkujeme za vaši trpělivost a pochopení!

V tomto cvičení vytvoříte, spustíte a vylepšíte AI agenta s nástroji z MCP serveru uvnitř Visual Studio Code pomocí AI Toolkitu.

### -0- Předkrok: Přidejte model OpenAI GPT-4o do sekce My Models

Cvičení využívá model **GPT-4o**. Model by měl být přidán do sekce **My Models** před vytvořením agenta.

1. Otevřete rozšíření **AI Toolkit** z **Activity Bar**.
1. V sekci **Catalog** vyberte **Models**, čímž otevřete **Model Catalog**. Výběr **Models** otevře **Model Catalog** v nové záložce editoru.
1. Do vyhledávacího pole **Model Catalog** zadejte **OpenAI GPT-4o**.
1. Klikněte na **+ Add**, abyste přidali model do seznamu **My Models**. Ujistěte se, že jste vybrali model **Hosted by GitHub**.
1. V **Activity Bar** potvrďte, že se model **OpenAI GPT-4o** objevil v seznamu.

### -1- Vytvořte agenta

**Agent (Prompt) Builder** umožňuje vytvářet a přizpůsobovat vlastní AI agenty. V této části vytvoříte nového agenta a přiřadíte mu model pro pohánění konverzace.

1. Otevřete rozšíření **AI Toolkit** z **Activity Bar**.
1. V sekci **Tools** vyberte **Agent (Prompt) Builder**. Výběr **Agent (Prompt) Builder** otevře **Agent (Prompt) Builder** v nové záložce editoru.
1. Klikněte na tlačítko **+ New Agent**. Rozšíření spustí průvodce nastavením prostřednictvím **Command Palette**.
1. Zadejte název **Calculator Agent** a stiskněte **Enter**.
1. V **Agent (Prompt) Builder** vyberte pro pole **Model** model **OpenAI GPT-4o (via GitHub)**.

### -2- Vytvořte systémový prompt pro agenta

Po vytvoření základní struktury agenta je čas definovat jeho osobnost a účel. V této části použijete funkci **Generate system prompt**, abyste popsali zamýšlené chování agenta—v tomto případě kalkulačkového agenta—a nechali model vygenerovat systémový prompt za vás.

1. V sekci **Prompts** klikněte na tlačítko **Generate system prompt**. Toto tlačítko otevře nástroj pro tvorbu promptů, který využívá AI k vygenerování systémového promptu pro agenta.
1. V okně **Generate a prompt** zadejte následující: `Jste užitečný a efektivní matematický asistent. Když dostanete úlohu zahrnující základní aritmetiku, odpovíte správným výsledkem.`
1. Klikněte na tlačítko **Generate**. V pravém dolním rohu se zobrazí oznámení potvrzující, že systémový prompt se generuje. Po dokončení se prompt objeví v poli **System prompt** v **Agent (Prompt) Builder**.
1. Zkontrolujte **System prompt** a v případě potřeby jej upravte.

### -3- Vytvořte MCP server

Nyní, když jste definovali systémový prompt agenta—který řídí jeho chování a odpovědi—je čas vybavit agenta praktickými schopnostmi. V této části vytvoříte MCP server kalkulačky s nástroji pro provádění sčítání, odčítání, násobení a dělení. Tento server umožní vašemu agentovi provádět matematické operace v reálném čase na základě přirozeného jazyka.

AI Toolkit je vybaven šablonami pro snadné vytváření vlastních MCP serverů. Použijeme šablonu Python pro vytvoření MCP serveru kalkulačky.

*Poznámka*: AI Toolkit aktuálně podporuje Python a TypeScript.

1. V sekci **Tools** v **Agent (Prompt) Builder** klikněte na tlačítko **+ MCP Server**. Rozšíření spustí průvodce nastavením prostřednictvím **Command Palette**.
1. Vyberte **+ Add Server**.
1. Vyberte **Create a New MCP Server**.
1. Vyberte šablonu **python-weather**.
1. Vyberte **Default folder** pro uložení šablony MCP serveru.
1. Zadejte následující název serveru: **Calculator**.
1. Otevře se nové okno Visual Studio Code. Vyberte **Yes, I trust the authors**.
1. Pomocí terminálu (**Terminal** > **New Terminal**) vytvořte virtuální prostředí: `python -m venv .venv`.
1. Aktivujte virtuální prostředí:
    - Windows - `.venv\Scripts\activate`
    - macOS/Linux - `source .venv/bin/activate`
1. Nainstalujte závislosti: `pip install -e .[dev]`.
1. V **Explorer** zobrazení v **Activity Bar** rozbalte adresář **src** a otevřete soubor **server.py** v editoru.
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

### -4- Spusťte agenta s MCP serverem kalkulačky

Nyní, když váš agent má nástroje, je čas je použít! V této části zadáte prompt agentovi, abyste otestovali a ověřili, zda agent využívá příslušný nástroj z MCP serveru kalkulačky.

1. Stiskněte `F5`, abyste spustili ladění MCP serveru. **Agent (Prompt) Builder** se otevře v nové záložce editoru. Stav serveru je viditelný v terminálu.
1. Do pole **User prompt** v **Agent (Prompt) Builder** zadejte následující prompt: `Koupil jsem 3 položky za $25 každou a poté použil slevu $20. Kolik jsem zaplatil?`
1. Klikněte na tlačítko **Run**, abyste vygenerovali odpověď agenta.
1. Zkontrolujte výstup agenta. Model by měl dojít k závěru, že jste zaplatili **$55**.
1. Zadejte další prompty pro další testování agenta. Můžete upravit existující prompt v poli **User prompt** kliknutím do pole a nahrazením existujícího promptu.
1. Po dokončení testování agenta můžete server zastavit v **terminálu** zadáním **CTRL/CMD+C** pro ukončení.

## Zadání

Zkuste přidat další nástroj do souboru **server.py** (např. výpočet druhé odmocniny čísla). Zadejte další prompty, které by vyžadovaly, aby agent využil váš nový nástroj (nebo stávající nástroje). Nezapomeňte restartovat server, aby se načetly nově přidané nástroje.

## Řešení

[Řešení](./solution/README.md)

## Klíčové poznatky

Klíčové poznatky z této kapitoly jsou následující:

- Rozšíření AI Toolkit je skvělý klient, který umožňuje spotřebovávat MCP servery a jejich nástroje.
- Můžete přidávat nové nástroje do MCP serverů, čímž rozšiřujete schopnosti agenta, aby splňoval rostoucí požadavky.
- AI Toolkit obsahuje šablony (např. šablony Python MCP serverů) pro zjednodušení vytváření vlastních nástrojů.

## Další zdroje

- [Dokumentace AI Toolkit](https://aka.ms/AIToolkit/doc)

## Co dál
- Další: [Testování a ladění](../08-testing/README.md)

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.