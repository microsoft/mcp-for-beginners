# Konzumácia servera z rozšírenia AI Toolkit pre Visual Studio Code

Keď vytvárate AI agenta, nejde len o generovanie inteligentných odpovedí; ide aj o to, aby ste svojmu agentovi dali schopnosť konať. Práve tu prichádza na scénu Protokol kontextu modelu (Model Context Protocol, MCP). MCP uľahčuje agentom prístup k externým nástrojom a službám konzistentným spôsobom. Predstavte si to ako pripojenie vášho agenta do nástroja, ktorý môže *skutočne* používať.

Povedzme, že pripojíte agenta k vášmu serveru MCP kalkulačky. Zrazu môže váš agent vykonávať matematické operácie len na základe výzvy ako „Koľko je 47 krát 89?“ — nie je nutné programovať logiku ani vytvárať vlastné API.

## Prehľad

Táto lekcia pokrýva, ako pripojiť server MCP kalkulačky k agentovi pomocou rozšírenia [AI Toolkit](https://aka.ms/AIToolkit) vo Visual Studio Code, čo umožňuje vášmu agentovi vykonávať matematické operácie ako sčítanie, odčítanie, násobenie a delenie prostredníctvom prirodzeného jazyka.

AI Toolkit je výkonné rozšírenie pre Visual Studio Code, ktoré zjednodušuje vývoj agentov. AI inžinieri môžu ľahko vytvárať AI aplikácie vývojom a testovaním generatívnych AI modelov — lokálne alebo v cloude. Rozšírenie podporuje väčšinu hlavných dostupných generatívnych modelov.

*Poznámka*: AI Toolkit momentálne podporuje Python a TypeScript.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Konzumovať server MCP cez AI Toolkit.
- Konfigurovať nastavenie agenta tak, aby vedel objaviť a využiť nástroje poskytované serverom MCP.
- Využívať nástroje MCP prostredníctvom prirodzeného jazyka.

## Prístup

Tu je náš vysokúrovňový prístup:

- Vytvoriť agenta a definovať jeho systémovú výzvu (prompt).
- Vytvoriť server MCP s nástrojmi kalkulačky.
- Pripojiť Agent Builder k serveru MCP.
- Otestovať volanie nástrojov agenta cez prirodzený jazyk.

Výborne, teraz keď rozumieme postupu, nakonfigurujeme AI agenta tak, aby využíval externé nástroje cez MCP a rozšíril tak svoje schopnosti!

## Predpoklady

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit pre Visual Studio Code](https://aka.ms/AIToolkit)

## Cvičenie: Konzumácia servera

> [!WARNING]
> Poznámka pre používateľov macOS. Momentálne skúmame problém, ktorý ovplyvňuje inštaláciu závislostí na macOS. V dôsledku toho používatelia macOS momentálne nemôžu dokončiť tento tutoriál. Návody aktualizujeme hneď, ako bude dostupné riešenie. Ďakujeme za vašu trpezlivosť a pochopenie!

V tomto cvičení vybudujete, spustíte a vylepšíte AI agenta s nástrojmi zo servera MCP priamo vo Visual Studio Code pomocou AI Toolkit.

### -0- Predkrok, pridajte model OpenAI GPT-4o do Moje Modely

Cvičenie využíva model **GPT-4o**. Model by mal byť pridaný do **Moje Modely** pred vytvorením agenta.

![Screenshot rozhrania výberu modelu v rozšírení AI Toolkit pre Visual Studio Code. Nadpis znie "Nájdite správny model pre vaše AI riešenie" s podnadpisom, ktorý vyzýva užívateľov objavovať, testovať a nasadzovať AI modely. Pod tým, v sekcii „Populárne modely“, je zobrazených šesť modelových kariet: DeepSeek-R1 (hostované na GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - malý, rýchly) a DeepSeek-R1 (hostované na Ollama). Každá karta obsahuje možnosti „Pridať“ model alebo „Vyskúšať v Playground](../../../../translated_images/sk/aitk-model-catalog.2acd38953bb9c119.webp)

1. Otvorte rozšírenie **AI Toolkit** z **Activity Bar**.
1. V sekcii **Catalog** vyberte **Models** na otvorenie **Model Catalog**. Výberom **Models** sa **Model Catalog** otvorí v novej záložke editora.
1. Do vyhľadávacieho poľa v **Model Catalog** zadajte **OpenAI GPT-4o**.
1. Kliknite na **+ Add** pre pridanie modelu do vášho zoznamu **My Models**. Uistite sa, že ste vybrali model **hostovaný na GitHub**.
1. Na **Activity Bar** potvrďte, že model **OpenAI GPT-4o** sa zobrazil v zozname.

### -1- Vytvorte agenta

**Agent (Prompt) Builder** vám umožňuje vytvárať a prispôsobovať vlastných AI agentov. V tejto sekcii vytvoríte nového agenta a pridelíte model, ktorý bude poháňať konverzáciu.

![Screenshot rozhrania tvorcu "Calculator Agent" v rozšírení AI Toolkit pre Visual Studio Code. Na ľavom paneli je vybraný model "OpenAI GPT-4o (cez GitHub)". Systémová výzva hovorí "You are a professor in university teaching math," a používateľská výzva "Explain to me the Fourier equation in simple terms." Ďalšie možnosti obsahujú tlačidlá pre pridanie nástrojov, povolenie MCP Server a výber štruktúrovaného výstupu. Dole je modré tlačidlo „Run“. Na pravom paneli, pod "Get Started with Examples," sú uvedení traja ukážkoví agenti: Web Developer (s MCP Server, Simplifier druháčka, a Dream Interpreter, každý s krátkym popisom svojich funkcií.](../../../../translated_images/sk/aitk-agent-builder.901e3a2960c3e477.webp)

1. Otvorte rozšírenie **AI Toolkit** z **Activity Bar**.
1. V sekcii **Tools** vyberte **Agent (Prompt) Builder**. Výberom sa **Agent (Prompt) Builder** otvorí v novej záložke editora.
1. Kliknite na tlačidlo **+ New Agent**. Rozšírenie spustí inštalačný sprievodca cez **Command Palette**.
1. Zadajte názov **Calculator Agent** a stlačte **Enter**.
1. V **Agent (Prompt) Builder** v poli **Model** vyberte model **OpenAI GPT-4o (cez GitHub)**.

### -2- Vytvorte systémovú výzvu pre agenta

Po vytvorení agenta je čas definovať jeho osobnosť a účel. V tejto sekcii použijete funkciu **Generate system prompt** na opísanie správania agenta — v tomto prípade agenta kalkulačky — a necháte model, aby systémovú výzvu za vás vytvoril.

![Screenshot rozhrania agenta "Calculator Agent" v AI Toolkit pre Visual Studio Code so zobrazeným modálnym oknom nazvaným "Generate a prompt." Modál vysvetľuje, že šablóna výzvy môže byť vygenerovaná zdieľaním základných údajov a obsahuje textové pole so vzorovou systémovou výzvou: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Pod textovým poľom sú tlačidlá "Close" a "Generate". V pozadí je viditeľná časť konfigurácie agenta so zvoleným modelom "OpenAI GPT-4o (cez GitHub)" a poľami systémovej a používateľskej výzvy.](../../../../translated_images/sk/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. V sekcii **Prompts** kliknite na tlačidlo **Generate system prompt**. Toto tlačidlo otvorí generátor výzvy, ktorý využíva AI na vytvorenie systémovej výzvy pre agenta.
1. V okne **Generate a prompt** zadajte nasledovné: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Kliknite na tlačidlo **Generate**. V pravom dolnom rohu sa zobrazí oznámenie o generovaní systémovej výzvy. Po dokončení generovania sa výzva zobrazí v poli **System prompt** vo **Agent (Prompt) Builder**.
1. Skontrolujte **System prompt** a prípadne upravte.

### -3- Vytvorte MCP server

Teraz, keď ste definovali systémovú výzvu svojho agenta — ktorá riadi jeho správanie a odpovede — je čas vybaviť agenta praktickými schopnosťami. V tejto sekcii vytvoríte server MCP kalkulačky s nástrojmi na vykonávanie sčítania, odčítania, násobenia a delenia. Tento server umožní agentovi vykonávať matematické operácie v reálnom čase v reakcii na prirodzený jazyk.

!["Screenshot spodnej časti rozhrania Calculator Agent v rozšírení AI Toolkit pre Visual Studio Code. Zobrazuje rozbaľovacie menu pre „Tools“ a „Structure output“ spolu s rozbaľovacím menu s označením „Choose output format“ nastaveným na „text.“ Vpravo je tlačidlo „+ MCP Server“ na pridanie Model Context Protocol servera. Nad sekciou Tools je ikonka obrázka.](../../../../translated_images/sk/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit je vybavený šablónami, ktoré uľahčujú vytvorenie vlastného servera MCP. Použijeme šablónu pre Python na vytvorenie servera MCP kalkulačky.

*Poznámka*: AI Toolkit momentálne podporuje Python a TypeScript.

1. V sekcii **Tools** vo **Agent (Prompt) Builder** kliknite na tlačidlo **+ MCP Server**. Rozšírenie spustí inštalačného sprievodcu cez **Command Palette**.
1. Vyberte **+ Add Server**.
1. Vyberte **Create a New MCP Server**.
1. Vyberte šablónu **python-weather**.
1. Vyberte **Default folder** pre uloženie šablóny servera MCP.
1. Zadajte nasledujúci názov servera: **Calculator**
1. Otvorí sa nové okno Visual Studio Code. Vyberte **Yes, I trust the authors**.
1. Pomocou terminálu (**Terminal** > **New Terminal**) vytvorte virtuálne prostredie: `python -m venv .venv`
1. Pomocou terminálu aktivujte virtuálne prostredie:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Pomocou terminálu nainštalujte závislosti: `pip install -e .[dev]`
1. V zobrazení **Explorer** v **Activity Bar** rozbaľte adresár **src** a vyberte **server.py** na otvorenie súboru v editore.
1. Nahraďte kód v súbore **server.py** nasledovným a uložte:

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

### -4- Spustite agenta so serverom MCP kalkulačky

Teraz, keď má váš agent nástroje, je čas ich použiť! V tejto sekcii pošlete agentovi výzvy, aby ste otestovali a overili, či agent využíva správny nástroj zo servera MCP kalkulačky.

![Screenshot rozhrania Calculator Agent v rozšírení AI Toolkit pre Visual Studio Code. Na ľavom paneli, v sekcii „Tools“, je pridaný MCP server pomenovaný local-server-calculator_server so štyrmi dostupnými nástrojmi: add, subtract, multiply a divide. Odznak ukazuje, že štyri nástroje sú aktívne. Pod tým je zbalená sekcia „Structure output“ a modré tlačidlo „Run“. Na pravom paneli, pod „Model Response“, agent vyvoláva nástroje multiply a subtract s vstupmi {"a": 3, "b": 25} a {"a": 75, "b": 20}. Konečná „Tool Response“ je zobrazená ako 75,0. Dole sa nachádza tlačidlo „View Code“.](../../../../translated_images/sk/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Bude sa spúšťať server MCP kalkulačky na vašom lokálnom vývojovom počítači cez **Agent Builder** ako MCP klienta.

1. Stlačte `F5` na spustenie ladenia servera MCP. **Agent (Prompt) Builder** sa otvorí v novej záložke editora. Stav servera je viditeľný v termináli.
1. Do poľa **User prompt** vo **Agent (Prompt) Builder** zadajte túto výzvu: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Kliknite na tlačidlo **Run** pre generovanie odpovede agenta.
1. Skontrolujte výstup agenta. Model by mal dospieť k záveru, že ste zaplatili **55 dolárov**.
1. Tu je prehľad toho, čo by sa malo udiať:
    - Agent vyberie nástroje **multiply** a **subtract** na pomoc pri výpočte.
    - Priradia sa príslušné hodnoty `a` a `b` pre nástroj **multiply**.
    - Priradia sa príslušné hodnoty `a` a `b` pre nástroj **subtract**.
    - Odpovede od každého nástroja sa zobrazia v príslušných poliach **Tool Response**.
    - Konečný výstup modelu sa zobrazuje v konečnej odpovedi **Model Response**.
1. Pošlite ďalšie výzvy na ďalšie testovanie agenta. Existujúcu výzvu v poli **User prompt** môžete upraviť kliknutím a zmenou textu.
1. Keď dokončíte testovanie agenta, server môžete zastaviť cez **terminál** pomocou **CTRL/CMD+C** na ukončenie.

## Zadanie

Skúste do súboru **server.py** pridať ďalší nástroj (napr. vrátiť druhú odmocninu z čísla). Pošlite ďalšie výzvy, ktoré budú vyžadovať využitie vášho nového alebo existujúcich nástrojov. Nezabudnite reštartovať server, aby sa nové nástroje načítali.

## Riešenie

[Riešenie](./solution/README.md)

## Kľúčové poznatky

Z tejto kapitoly si vezmite nasledovné:

- Rozšírenie AI Toolkit je skvelý klient, ktorý umožňuje konzumovať MCP servery a ich nástroje.
- Môžete pridávať nové nástroje do MCP serverov, čím rozširujete schopnosti agenta podľa vyvíjajúcich sa požiadaviek.
- AI Toolkit obsahuje šablóny (napr. python šablóny pre MCP servery) na zjednodušenie tvorby vlastných nástrojov.

## Dodatočné zdroje

- [Dokumentácia AI Toolkit](https://aka.ms/AIToolkit/doc)

## Čo ďalej
- Ďalej: [Testovanie a ladenie](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->