# Spotrebovanie servera z rozšírenia AI Toolkit pre Visual Studio Code

Keď vytvárate AI agenta, nejde len o generovanie inteligentných odpovedí; ide aj o to, aby váš agent dokázal vykonávať akcie. Tu prichádza na scénu Model Context Protocol (MCP). MCP umožňuje agentom jednoduchý prístup k externým nástrojom a službám konzistentným spôsobom. Predstavte si to ako pripojenie vášho agenta k nástrojovej sade, ktorú môže *skutočne* používať.

Predstavme si, že pripojíte agenta k MCP serveru kalkulačky. Zrazu váš agent dokáže vykonávať matematické operácie len na základe zadania, ako napríklad „Koľko je 47 krát 89?“—bez potreby pevne zakódovanej logiky alebo vytvárania vlastných API.

## Prehľad

Táto lekcia pokrýva, ako pripojiť MCP server kalkulačky k agentovi pomocou rozšírenia [AI Toolkit](https://aka.ms/AIToolkit) vo Visual Studio Code, čím umožníte vášmu agentovi vykonávať matematické operácie, ako sú sčítanie, odčítanie, násobenie a delenie prostredníctvom prirodzeného jazyka.

AI Toolkit je výkonné rozšírenie pre Visual Studio Code, ktoré zjednodušuje vývoj agentov. AI inžinieri môžu ľahko vytvárať AI aplikácie vývojom a testovaním generatívnych AI modelov—lokálne alebo v cloude. Rozšírenie podporuje väčšinu hlavných generatívnych modelov dostupných dnes.

*Poznámka*: AI Toolkit aktuálne podporuje Python a TypeScript.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Spotrebovať MCP server prostredníctvom AI Toolkit.
- Konfigurovať konfiguráciu agenta tak, aby dokázal objaviť a využívať nástroje poskytované MCP serverom.
- Využívať MCP nástroje prostredníctvom prirodzeného jazyka.

## Prístup

Tu je vysoká úroveň prístupu, ktorý potrebujeme:

- Vytvoriť agenta a definovať jeho systémový prompt.
- Vytvoriť MCP server s nástrojmi kalkulačky.
- Pripojiť Agent Builder k MCP serveru.
- Otestovať vyvolanie nástrojov agenta prostredníctvom prirodzeného jazyka.

Skvelé, teraz keď rozumieme toku, nakonfigurujme AI agenta tak, aby využíval externé nástroje prostredníctvom MCP, čím rozšírime jeho schopnosti!

## Predpoklady

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pre Visual Studio Code](https://aka.ms/AIToolkit)

## Cvičenie: Spotrebovanie servera

> [!WARNING]
> Poznámka pre používateľov macOS. Aktuálne skúmame problém ovplyvňujúci inštaláciu závislostí na macOS. Z tohto dôvodu používatelia macOS nebudú môcť dokončiť tento tutoriál v súčasnosti. Pokyny aktualizujeme hneď, ako bude k dispozícii oprava. Ďakujeme za vašu trpezlivosť a pochopenie!

V tomto cvičení vytvoríte, spustíte a vylepšíte AI agenta s nástrojmi z MCP servera vo Visual Studio Code pomocou AI Toolkit.

### -0- Predkrok, pridajte model OpenAI GPT-4o do Moje modely

Cvičenie využíva model **GPT-4o**. Model by mal byť pridaný do **Moje modely** pred vytvorením agenta.

1. Otvorte rozšírenie **AI Toolkit** z **Activity Bar**.
1. V sekcii **Catalog** vyberte **Models**, aby ste otvorili **Model Catalog**. Výberom **Models** sa otvorí **Model Catalog** v novom editore.
1. Do vyhľadávacieho poľa **Model Catalog** zadajte **OpenAI GPT-4o**.
1. Kliknite na **+ Add**, aby ste pridali model do zoznamu **Moje modely**. Uistite sa, že ste vybrali model, ktorý je **Hosted by GitHub**.
1. V **Activity Bar** potvrďte, že model **OpenAI GPT-4o** sa zobrazuje v zozname.

### -1- Vytvorte agenta

**Agent (Prompt) Builder** umožňuje vytvárať a prispôsobovať vlastných AI agentov. V tejto sekcii vytvoríte nového agenta a priradíte model na pohon konverzácie.

1. Otvorte rozšírenie **AI Toolkit** z **Activity Bar**.
1. V sekcii **Tools** vyberte **Agent (Prompt) Builder**. Výberom **Agent (Prompt) Builder** sa otvorí **Agent (Prompt) Builder** v novom editore.
1. Kliknite na tlačidlo **+ New Agent**. Rozšírenie spustí sprievodcu nastavením prostredníctvom **Command Palette**.
1. Zadajte názov **Calculator Agent** a stlačte **Enter**.
1. V **Agent (Prompt) Builder**, pre pole **Model**, vyberte model **OpenAI GPT-4o (via GitHub)**.

### -2- Vytvorte systémový prompt pre agenta

Keď je agent pripravený, je čas definovať jeho osobnosť a účel. V tejto sekcii použijete funkciu **Generate system prompt**, aby ste opísali zamýšľané správanie agenta—v tomto prípade kalkulačného agenta—a necháte model napísať systémový prompt za vás.

1. Pre sekciu **Prompts** kliknite na tlačidlo **Generate system prompt**. Toto tlačidlo otvorí generátor promptov, ktorý využíva AI na generovanie systémového promptu pre agenta.
1. V okne **Generate a prompt** zadajte nasledujúce: `Ste užitočný a efektívny matematický asistent. Keď dostanete úlohu zahŕňajúcu základnú aritmetiku, odpoviete správnym výsledkom.`
1. Kliknite na tlačidlo **Generate**. V pravom dolnom rohu sa zobrazí notifikácia potvrdzujúca, že systémový prompt sa generuje. Po dokončení generovania sa prompt zobrazí v poli **System prompt** v **Agent (Prompt) Builder**.
1. Skontrolujte **System prompt** a upravte ho, ak je to potrebné.

### -3- Vytvorte MCP server

Teraz, keď ste definovali systémový prompt agenta—ktorý usmerňuje jeho správanie a odpovede—je čas vybaviť agenta praktickými schopnosťami. V tejto sekcii vytvoríte MCP server kalkulačky s nástrojmi na vykonávanie sčítania, odčítania, násobenia a delenia. Tento server umožní vášmu agentovi vykonávať matematické operácie v reálnom čase ako odpoveď na prirodzené jazykové zadania.

AI Toolkit je vybavený šablónami na jednoduché vytváranie vlastných MCP serverov. Použijeme šablónu Python na vytvorenie MCP servera kalkulačky.

*Poznámka*: AI Toolkit aktuálne podporuje Python a TypeScript.

1. V sekcii **Tools** v **Agent (Prompt) Builder** kliknite na tlačidlo **+ MCP Server**. Rozšírenie spustí sprievodcu nastavením prostredníctvom **Command Palette**.
1. Vyberte **+ Add Server**.
1. Vyberte **Create a New MCP Server**.
1. Vyberte **python-weather** ako šablónu.
1. Vyberte **Default folder** na uloženie šablóny MCP servera.
1. Zadajte nasledujúci názov pre server: **Calculator**
1. Otvorí sa nové okno Visual Studio Code. Vyberte **Yes, I trust the authors**.
1. Pomocou terminálu (**Terminal** > **New Terminal**) vytvorte virtuálne prostredie: `python -m venv .venv`
1. Pomocou terminálu aktivujte virtuálne prostredie:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Pomocou terminálu nainštalujte závislosti: `pip install -e .[dev]`
1. V zobrazení **Explorer** v **Activity Bar** rozbaľte adresár **src** a vyberte **server.py**, aby ste otvorili súbor v editore.
1. Nahraďte kód v súbore **server.py** nasledujúcim a uložte:

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

### -4- Spustite agenta s MCP serverom kalkulačky

Teraz, keď má váš agent nástroje, je čas ich použiť! V tejto sekcii zadáte prompt agentovi, aby ste otestovali a overili, či agent využíva vhodný nástroj z MCP servera kalkulačky.

1. Stlačte `F5`, aby ste spustili ladenie MCP servera. **Agent (Prompt) Builder** sa otvorí v novom editore. Stav servera je viditeľný v termináli.
1. Do poľa **User prompt** v **Agent (Prompt) Builder** zadajte nasledujúci prompt: `Kúpil som 3 položky za cenu $25 každá a potom som použil zľavu $20. Koľko som zaplatil?`
1. Kliknite na tlačidlo **Run**, aby ste vygenerovali odpoveď agenta.
1. Skontrolujte výstup agenta. Model by mal dospieť k záveru, že ste zaplatili **$55**.
1. Tu je rozpis toho, čo by sa malo stať:
    - Agent vyberie nástroje **multiply** a **subtract**, aby pomohol s výpočtom.
    - Príslušné hodnoty `a` a `b` sú priradené pre nástroj **multiply**.
    - Príslušné hodnoty `a` a `b` sú priradené pre nástroj **subtract**.
    - Odpoveď z každého nástroja je poskytnutá v príslušnom **Tool Response**.
    - Konečný výstup z modelu je poskytnutý v konečnom **Model Response**.
1. Zadajte ďalšie prompty na ďalšie testovanie agenta. Môžete upraviť existujúci prompt v poli **User prompt** kliknutím do poľa a nahradením existujúceho promptu.
1. Keď skončíte s testovaním agenta, môžete server zastaviť prostredníctvom **terminálu** zadaním **CTRL/CMD+C**, aby ste ukončili.

## Zadanie

Skúste pridať ďalší nástroj do vášho súboru **server.py** (napr. vrátiť druhú odmocninu čísla). Zadajte ďalšie prompty, ktoré by vyžadovali, aby agent využil váš nový nástroj (alebo existujúce nástroje). Uistite sa, že ste reštartovali server, aby sa načítali novo pridané nástroje.

## Riešenie

[Riešenie](./solution/README.md)

## Kľúčové poznatky

Kľúčové poznatky z tejto kapitoly sú nasledujúce:

- Rozšírenie AI Toolkit je skvelý klient, ktorý umožňuje spotrebovať MCP servery a ich nástroje.
- Môžete pridávať nové nástroje do MCP serverov, čím rozširujete schopnosti agenta na splnenie vyvíjajúcich sa požiadaviek.
- AI Toolkit obsahuje šablóny (napr. šablóny Python MCP serverov), ktoré zjednodušujú vytváranie vlastných nástrojov.

## Ďalšie zdroje

- [Dokumentácia AI Toolkit](https://aka.ms/AIToolkit/doc)

## Čo ďalej
- Ďalej: [Testovanie a ladenie](../08-testing/README.md)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.