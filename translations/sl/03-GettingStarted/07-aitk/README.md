# Uporaba strežnika iz razširitve AI Toolkit za Visual Studio Code

Ko gradite AI agenta, ni pomembno le, da ustvarja pametne odgovore, temveč tudi, da ima sposobnost ukrepanja. Tukaj pride v igro Model Context Protocol (MCP). MCP omogoča agentom dostop do zunanjih orodij in storitev na dosleden način. Predstavljajte si, da svojega agenta priključite na orodjarno, ki jo lahko *dejansko* uporablja.

Recimo, da povežete agenta s strežnikom MCP za kalkulator. Nenadoma lahko vaš agent izvaja matematične operacije samo z vnosom, kot je "Koliko je 47 krat 89?"—brez potrebe po ročnem kodiranju logike ali gradnji prilagojenih API-jev.

## Pregled

Ta lekcija pokriva, kako povezati strežnik MCP za kalkulator z agentom z uporabo razširitve [AI Toolkit](https://aka.ms/AIToolkit) v Visual Studio Code, kar omogoča vašemu agentu izvajanje matematičnih operacij, kot so seštevanje, odštevanje, množenje in deljenje prek naravnega jezika.

AI Toolkit je zmogljiva razširitev za Visual Studio Code, ki poenostavi razvoj agentov. AI inženirji lahko enostavno gradijo AI aplikacije z razvojem in testiranjem generativnih AI modelov—lokalno ali v oblaku. Razširitev podpira večino glavnih generativnih modelov, ki so danes na voljo.

*Opomba*: AI Toolkit trenutno podpira Python in TypeScript.

## Cilji učenja

Do konca te lekcije boste sposobni:

- Uporabiti strežnik MCP prek AI Toolkit.
- Konfigurirati konfiguracijo agenta, da omogočite odkrivanje in uporabo orodij, ki jih ponuja strežnik MCP.
- Uporabljati MCP orodja prek naravnega jezika.

## Pristop

Tukaj je visok nivo pristopa, ki ga moramo upoštevati:

- Ustvarite agenta in definirajte njegov sistemski poziv.
- Ustvarite strežnik MCP z orodji za kalkulator.
- Povežite Agent Builder s strežnikom MCP.
- Testirajte uporabo orodij agenta prek naravnega jezika.

Odlično, zdaj ko razumemo potek, konfigurirajmo AI agenta, da izkoristi zunanja orodja prek MCP in izboljša svoje zmogljivosti!

## Predpogoji

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit za Visual Studio Code](https://aka.ms/AIToolkit)

## Vaja: Uporaba strežnika

> [!WARNING]
> Opomba za uporabnike macOS. Trenutno preiskujemo težavo, ki vpliva na namestitev odvisnosti na macOS. Zaradi tega uporabniki macOS trenutno ne bodo mogli dokončati tega vodiča. Navodila bomo posodobili takoj, ko bo na voljo rešitev. Hvala za vašo potrpežljivost in razumevanje!

V tej vaji boste zgradili, zagnali in izboljšali AI agenta z orodji iz strežnika MCP znotraj Visual Studio Code z uporabo AI Toolkit.

### -0- Predkorak, dodajte model OpenAI GPT-4o v Moji modeli

Vaja uporablja model **GPT-4o**. Model mora biti dodan v **Moji modeli** pred ustvarjanjem agenta.

1. Odprite razširitev **AI Toolkit** iz **Activity Bar**.
1. V razdelku **Catalog** izberite **Models**, da odprete **Model Catalog**. Izbira **Models** odpre **Model Catalog** v novem zavihku urejevalnika.
1. V iskalni vrstici **Model Catalog** vnesite **OpenAI GPT-4o**.
1. Kliknite **+ Add**, da dodate model v svoj seznam **Moji modeli**. Prepričajte se, da ste izbrali model, ki je **Hosted by GitHub**.
1. V **Activity Bar** potrdite, da se model **OpenAI GPT-4o** pojavi na seznamu.

### -1- Ustvarite agenta

**Agent (Prompt) Builder** omogoča ustvarjanje in prilagajanje lastnih AI agentov. V tem razdelku boste ustvarili novega agenta in mu dodelili model za pogovor.

1. Odprite razširitev **AI Toolkit** iz **Activity Bar**.
1. V razdelku **Tools** izberite **Agent (Prompt) Builder**. Izbira **Agent (Prompt) Builder** odpre **Agent (Prompt) Builder** v novem zavihku urejevalnika.
1. Kliknite gumb **+ New Agent**. Razširitev bo zagnala čarovnika za nastavitev prek **Command Palette**.
1. Vnesite ime **Calculator Agent** in pritisnite **Enter**.
1. V **Agent (Prompt) Builder** za polje **Model** izberite model **OpenAI GPT-4o (via GitHub)**.

### -2- Ustvarite sistemski poziv za agenta

Ko je agent pripravljen, je čas, da definirate njegovo osebnost in namen. V tem razdelku boste uporabili funkcijo **Generate system prompt**, da opišete namen agenta—v tem primeru kalkulatorski agent—in omogočili modelu, da napiše sistemski poziv za vas.

1. Za razdelek **Prompts** kliknite gumb **Generate system prompt**. Ta gumb odpre graditelj pozivov, ki uporablja AI za generiranje sistemskega poziva za agenta.
1. V oknu **Generate a prompt** vnesite naslednje: `Vi ste koristen in učinkovit matematični asistent. Ko prejmete nalogo, ki vključuje osnovno aritmetiko, odgovorite s pravilnim rezultatom.`
1. Kliknite gumb **Generate**. Obvestilo se bo pojavilo v spodnjem desnem kotu, ki potrjuje, da se sistemski poziv generira. Ko je generacija poziva končana, se bo poziv pojavil v polju **System prompt** v **Agent (Prompt) Builder**.
1. Preglejte **System prompt** in ga po potrebi spremenite.

### -3- Ustvarite strežnik MCP

Zdaj, ko ste definirali sistemski poziv agenta—ki usmerja njegovo vedenje in odgovore—je čas, da agenta opremite s praktičnimi zmogljivostmi. V tem razdelku boste ustvarili strežnik MCP za kalkulator z orodji za izvajanje seštevanja, odštevanja, množenja in deljenja. Ta strežnik bo omogočil vašemu agentu izvajanje matematičnih operacij v realnem času kot odgovor na naravne jezikovne pozive.

AI Toolkit je opremljen s predlogami za enostavno ustvarjanje lastnega strežnika MCP. Uporabili bomo Python predlogo za ustvarjanje strežnika MCP za kalkulator.

*Opomba*: AI Toolkit trenutno podpira Python in TypeScript.

1. V razdelku **Tools** v **Agent (Prompt) Builder** kliknite gumb **+ MCP Server**. Razširitev bo zagnala čarovnika za nastavitev prek **Command Palette**.
1. Izberite **+ Add Server**.
1. Izberite **Create a New MCP Server**.
1. Izberite **python-weather** kot predlogo.
1. Izberite **Default folder** za shranjevanje predloge strežnika MCP.
1. Vnesite naslednje ime za strežnik: **Calculator**
1. Novo okno Visual Studio Code se bo odprlo. Izberite **Yes, I trust the authors**.
1. Uporabite terminal (**Terminal** > **New Terminal**) za ustvarjanje virtualnega okolja: `python -m venv .venv`
1. Uporabite terminal za aktivacijo virtualnega okolja:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Uporabite terminal za namestitev odvisnosti: `pip install -e .[dev]`
1. V **Explorer** pogledu **Activity Bar** razširite imenik **src** in izberite **server.py**, da odprete datoteko v urejevalniku.
1. Zamenjajte kodo v datoteki **server.py** z naslednjo in shranite:

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

### -4- Zaženite agenta s strežnikom MCP za kalkulator

Zdaj, ko ima vaš agent orodja, je čas, da jih uporabite! V tem razdelku boste poslali pozive agentu, da testirate in preverite, ali agent uporablja ustrezno orodje iz strežnika MCP za kalkulator.

1. Pritisnite `F5`, da začnete odpravljanje napak strežnika MCP. **Agent (Prompt) Builder** se bo odprl v novem zavihku urejevalnika. Status strežnika je viden v terminalu.
1. V polje **User prompt** v **Agent (Prompt) Builder** vnesite naslednji poziv: `Kupil sem 3 izdelke po ceni $25 vsak, nato pa uporabil $20 popust. Koliko sem plačal?`
1. Kliknite gumb **Run**, da generirate odgovor agenta.
1. Preglejte izhod agenta. Model bi moral zaključiti, da ste plačali **$55**.
1. Tukaj je razčlenitev, kaj bi se moralo zgoditi:
    - Agent izbere orodji **multiply** in **subtract**, da pomaga pri izračunu.
    - Ustrezne vrednosti `a` in `b` so dodeljene za orodje **multiply**.
    - Ustrezne vrednosti `a` in `b` so dodeljene za orodje **subtract**.
    - Odziv vsakega orodja je prikazan v ustreznem **Tool Response**.
    - Končni izhod modela je prikazan v končnem **Model Response**.
1. Pošljite dodatne pozive za nadaljnje testiranje agenta. Obstoječi poziv v polju **User prompt** lahko spremenite tako, da kliknete v polje in zamenjate obstoječi poziv.
1. Ko končate testiranje agenta, lahko strežnik ustavite prek **terminala** z vnosom **CTRL/CMD+C**, da ga zaprete.

## Naloga

Poskusite dodati dodatno orodje v svojo datoteko **server.py** (npr. vrnite kvadratni koren števila). Pošljite dodatne pozive, ki bi zahtevali, da agent uporabi vaše novo orodje (ali obstoječa orodja). Prepričajte se, da ponovno zaženete strežnik, da naložite novo dodana orodja.

## Rešitev

[Rešitev](./solution/README.md)

## Ključne točke

Ključne točke iz tega poglavja so naslednje:

- Razširitev AI Toolkit je odličen odjemalec, ki omogoča uporabo strežnikov MCP in njihovih orodij.
- Strežnikom MCP lahko dodate nova orodja, s čimer razširite zmogljivosti agenta za izpolnjevanje spreminjajočih se zahtev.
- AI Toolkit vključuje predloge (npr. Python predloge za strežnike MCP), ki poenostavijo ustvarjanje prilagojenih orodij.

## Dodatni viri

- [Dokumentacija AI Toolkit](https://aka.ms/AIToolkit/doc)

## Kaj sledi
- Naslednje: [Testiranje in odpravljanje napak](../08-testing/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.