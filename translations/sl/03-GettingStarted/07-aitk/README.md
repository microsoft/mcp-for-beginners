# Uporaba strežnika iz razširitve AI Toolkit za Visual Studio Code

Ko ustvarjate AI agenta, ne gre le za generiranje pametnih odgovorov; pomembno je tudi omogočiti agentu, da lahko ukrepa. Tu pride v poštev Model Context Protocol (MCP). MCP omogoča agentom enostaven dostop do zunanjih orodij in storitev na dosleden način. Predstavljajte si ga kot povezavo vašega agenta s škatlo z orodji, ki jo lahko *dejansko* uporablja.

Recimo, da povežete agenta s strežnikom kalkulatorja MCP. Nenadoma lahko vaš agent izvaja matematične operacije samo z zahtevo, kot je "Koliko je 47 krat 89?" — brez potrebe po trdi kodi ali ustvarjanju posebnih API-jev.

## Pregled

Ta lekcija pokriva, kako povezati kalkulator MCP strežnik z agentom z razširitvijo [AI Toolkit](https://aka.ms/AIToolkit) v Visual Studio Code, kar agentu omogoča izvajanje matematičnih operacij, kot so seštevanje, odštevanje, množenje in deljenje skozi naravni jezik.

AI Toolkit je zmogljiva razširitev za Visual Studio Code, ki poenostavi razvoj agentov. AI inženirji lahko enostavno ustvarjajo AI aplikacije z razvojem in testiranjem generativnih AI modelov — lokalno ali v oblaku. Razširitev podpira večino najbolj znanih generativnih modelov danes.

*Opomba*: AI Toolkit trenutno podpira Python in TypeScript.

## Cilji učenja

Na koncu te lekcije boste znali:

- Uporabiti MCP strežnik preko AI Toolkita.
- Konfigurirati nastavitve agenta, da lahko odkrije in uporablja orodja, ki jih ponuja MCP strežnik.
- Uporabiti MCP orodja preko naravnega jezika.

## Pristop

Tako moramo pristopiti na visoki ravni:

- Ustvariti agenta in določiti njegov sistemski poziv.
- Ustvariti MCP strežnik s kalkulatorjem.
- Povezati Agent Builder s MCP strežnikom.
- Preizkusiti klic orodij agenta preko naravnega jezika.

Odlično, zdaj ko razumemo potek, konfigurirajmo AI agenta, da bo lahko uporabljal zunanja orodja preko MCP in tako izboljšal svoje zmogljivosti!

## Predpogoji

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit za Visual Studio Code](https://aka.ms/AIToolkit)

## Vaja: Uporaba strežnika

> [!WARNING]
> Opomba za uporabnike macOS. Trenutno preiskujemo težavo, ki vpliva na namestitev odvisnosti na macOS. Zaradi tega uporabniki macOS trenutno ne bodo mogli dokončati tega vodiča. Navodila bomo posodobili takoj, ko bo popravek na voljo. Hvala za vašo potrpežljivost in razumevanje!

V tej vaji boste zgradili, zagnali in izboljšali AI agenta z orodji iz MCP strežnika znotraj Visual Studio Code z uporabo AI Toolkita.

### -0- Predkorak, dodajte model OpenAI GPT-4o v Moji modeli

Vaja uporablja model **GPT-4o**. Model morate dodati v **Moji modeli** pred ustvarjanjem agenta.

![Posnetek zaslona vmesnika izbire modela v razširitvi AI Toolkit za Visual Studio Code. Naslov: "Poiščite pravo rešitev AI za vaš projekt" s podnaslovom, ki spodbuja odkrivanje, testiranje in uvajanje AI modelov. Pod “Popularni modeli” je prikazanih šest kartic modelov: DeepSeek-R1 (gostovan na GitHubu), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - majhen, hiter), in DeepSeek-R1 (gostovan na Ollama). Vsaka kartica vsebuje možnosti “Dodaj” ali “Preizkusi na igrišču”.](../../../../translated_images/sl/aitk-model-catalog.2acd38953bb9c119.webp)

1. Odprite razširitev **AI Toolkit** iz **Vrstice z aktivnostmi**.
1. V razdelku **Katalog** izberite **Modeli**, da odprete **Katalog modelov**. Izbira **Modeli** odpre **Katalog modelov** v novem zavihku urejevalnika.
1. V iskalno vrstico **Kataloga modelov** vnesite **OpenAI GPT-4o**.
1. Kliknite **+ Dodaj**, da model dodate na seznam **Moji modeli**. Prepričajte se, da ste izbrali model, ki je **gostovan na GitHubu**.
1. V **Vrstici z aktivnostmi** potrdite, da se model **OpenAI GPT-4o** pojavi na seznamu.

### -1- Ustvarite agenta

**Agent (Prompt) Builder** vam omogoča ustvarjanje in prilagajanje AI agentov. V tem razdelku boste ustvarili novega agenta in ga povezali z modelom, ki bo poganjal pogovor.

![Posnetek zaslona vmesnika “Calculator Agent” v razširitvi AI Toolkit za Visual Studio Code. V levem panelu je izbran model "OpenAI GPT-4o (prek GitHub)". Sistemski poziv pravi “Ste profesor na univerzi, ki poučuje matematiko,” uporabniški poziv je “Razložite mi Fourierjevo enačbo na preprost način.” Dodatne možnosti vključujejo gumbe za dodajanje orodij, omogočanje MCP strežnika in izbiro strukturiranega izhoda. Na dnu je moder gumb “Zaženi”. Na desnem panelu, pod “Začnite z primeri,” so navedeni trije vzorčni agenti: spletni razvijalec (z MCP strežnikom, poenostavljalnik za drugi razred in tolmač sanj, vsak s kratkimi opisi funkcij).](../../../../translated_images/sl/aitk-agent-builder.901e3a2960c3e477.webp)

1. Odprite razširitev **AI Toolkit** iz **Vrstice z aktivnostmi**.
1. V razdelku **Orodja** izberite **Agent (Prompt) Builder**. Izbira **Agent (Prompt) Builder** odpre urejevalnik v novem zavihku.
1. Kliknite gumb **+ Nov agent**. Razširitev bo zagnala čarovnika za nastavitev preko **Ukazne palete**.
1. Vnesite ime **Calculator Agent** in pritisnite **Enter**.
1. V **Agent (Prompt) Builder** za polje **Model** izberite model **OpenAI GPT-4o (prek GitHub)**.

### -2- Ustvarite sistemski poziv za agenta

Ko je agent osnovan, je čas, da določite njegovo osebnost in namen. V tem delu boste uporabili možnost **Generiraj sistemski poziv**, da opišete predvideno vedenje agenta — v tem primeru kalkulatorskega agenta — in modelu prepustili, da napiše sistemski poziv za vas.

![Posnetek zaslona vmesnika "Calculator Agent" v AI Toolkit za Visual Studio Code z odprtim modalnim oknom z naslovom "Generiraj poziv." Modalno okno pojasnjuje, da je mogoče ustvariti predlogo poziva z deljenjem osnovnih podatkov in vsebuje besedilno polje s primerom sistemskega poziva: "Ste prijazen in učinkovit matematični asistent. Ob prejavi osnovnega aritmetičnega problema odgovorite z pravilnim rezultatom." Spodaj pod besedilnim poljem sta gumba "Zapri" in "Generiraj". V ozadju je del konfiguracije agenta, vključno z izbranim modelom "OpenAI GPT-4o (prek GitHub)" in polji za sistemski in uporabniški poziv.](../../../../translated_images/sl/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. V razdelku **Pozivi** kliknite gumb **Generiraj sistemski poziv**. Ta gumb odpre generator poziva, ki uporablja AI za generiranje sistemskega poziva za agenta.
1. V oknu **Generiraj poziv** vnesite naslednje: `Ste prijazen in učinkovit matematični asistent. Ob prejavi osnovnega aritmetičnega problema odgovorite z pravilnim rezultatom.`
1. Kliknite gumb **Generiraj**. V spodnjem desnem kotu se bo prikazalo obvestilo o poteku generiranja sistemskega poziva. Ko bo generiranje končano, se bo poziv prikazal v polju **Sistemski poziv** v **Agent (Prompt) Builder**.
1. Preglejte **Sistemski poziv** in ga po potrebi spremenite.

### -3- Ustvarite MCP strežnik

Zdaj, ko ste določili sistemski poziv agenta — ki usmerja njegovo vedenje in odzive — je čas, da agenta opremite s praktičnimi zmožnostmi. V tem delu boste ustvarili kalkulatorski MCP strežnik z orodji za izvajanje seštevanja, odštevanja, množenja in deljenja. Ta strežnik bo agentu omogočil izvajanje matematičnih operacij v realnem času na osnovi naravnih jezikovnih zahtev.

!["Posnetek zaslona spodnjega dela vmesnika za Calculator Agent v razširitvi AI Toolkit za Visual Studio Code. Prikazani so razširljivi meniji za “Orodja” in “Strukturiran izhod,” skupaj z padajočim menijem “Izberi format izhoda” nastavljeno na “besedilo”. Na desni je gumb z oznako “+ MCP Server” za dodajanje strežnika Model Context Protocol. Nad razdelkom Orodja je prikazan nadomestni simbol slike.](../../../../translated_images/sl/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit je opremljen s predlogami za enostavno ustvarjanje lastnih MCP strežnikov. Uporabili bomo Python predlogo za ustvarjanje kalkulatorskega MCP strežnika.

*Opomba*: AI Toolkit trenutno podpira Python in TypeScript.

1. V razdelku **Orodja** v **Agent (Prompt) Builder** kliknite gumb **+ MCP Server**. Razširitev bo zagnala čarovnika za nastavitev prek **Ukazne palete**.
1. Izberite **+ Dodaj strežnik**.
1. Izberite **Ustvari nov MCP strežnik**.
1. Izberite predlogo **python-weather**.
1. Izberite **Privzeta mapa** za shranjevanje predloge MCP strežnika.
1. Vnesite ime strežnika: **Calculator**
1. Odpre se novo okno Visual Studio Code. Izberite **Da, zaupam avtorjem**.
1. Z uporabo terminala (**Terminal** > **Nov terminal**) ustvarite virtualno okolje: `python -m venv .venv`
1. Z uporabo terminala aktivirajte virtualno okolje:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Z uporabo terminala namestite odvisnosti: `pip install -e .[dev]`
1. V pogledu **Explorer** z **Vrstice z aktivnostmi** razširite imenik **src** in izberite **server.py**, da odprete datoteko v urejevalniku.
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

### -4- Zaženite agenta s kalkulatorskim MCP strežnikom

Zdaj, ko ima vaš agent orodja, je čas, da jih uporabite! V tem delu boste agentu pošiljali pozive, da preizkusite in potrdite, ali agent uporablja ustrezno orodje iz kalkulatorskega MCP strežnika.

![Posnetek zaslona vmesnika Calculator Agent v razširitvi AI Toolkit za Visual Studio Code. Na levem panelu, pod “Orodja,” je dodan MCP strežnik z imenom local-server-calculator_server, prikazane so štiri razpoložljive funkcije: seštevanje, odštevanje, množenje in deljenje. Značka kaže, da so štiri orodja aktivna. Spodaj je strnjen razdelek “Strukturiran izhod” in moder gumb “Zaženi.” Na desnem panelu, pod “Odgovor modela,” agent kliče funkciji množenja in odštevanja z vhodoma {"a": 3, "b": 25} in {"a": 75, "b": 20}. Končni “Odgovor orodja” je prikazan kot 75.0. Na dnu je gumb “Poglej kodo.”](../../../../translated_images/sl/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Kalkulatorski MCP strežnik boste zagnali na svojem lokalnem razvojnem stroju prek **Agent Builderja** kot MCP odjemalec.

1. Pritisnite `F5`, da začnete razhroščevanje MCP strežnika. **Agent (Prompt) Builder** se bo odprl v novem urejevalniškem zavihku. Status strežnika je viden v terminalu.
1. V polje **Uporabniški poziv** v **Agent (Prompt) Builder** vnesite naslednji poziv: `Kupil sem 3 izdelke po 25 dolarjev vsak, nato pa uporabil 20 dolarjev popusta. Koliko sem plačal?`
1. Kliknite gumb **Zaženi**, da generirate odgovor agenta.
1. Preglejte izhod agenta. Model bi moral zaključiti, da ste plačali **55 $**.
1. Tukaj je razčlenitev dogajanja:
    - Agent izbere orodji **multiply** in **subtract** za pomoč pri izračunu.
    - Za orodje **multiply** so dodeljene vrednosti `a` in `b`.
    - Za orodje **subtract** so dodeljene vrednosti `a` in `b`.
    - Odgovori posameznega orodja so podani v **Odgovoru orodja**.
    - Končni izhod modela je prikazan v **Odgovoru modela**.
1. Pošljite dodatne pozive za nadaljnje testiranje agenta. Obstoječi poziv lahko spremenite tako, da kliknete v polje **Uporabniški poziv** in ga zamenjate.
1. Ko končate s testiranjem agenta, lahko strežnik ustavite preko terminala z vnosom **CTRL/CMD+C**.

## Naloga

Poskusite dodati novo orodje v datoteko **server.py** (npr.: vrnite kvadratni koren števila). Pošljite dodatne pozive, ki zahtevajo uporabo vašega novega orodja (ali obstoječih). Ne pozabite ponovno zagnati strežnika, da naložite nov dodatek.

## Rešitev

[Rešitev](./solution/README.md)

## Ključne ugotovitve

Ključni izsledki tega poglavja so naslednji:

- Razširitev AI Toolkit je odličen odjemalec, ki vam omogoča uporabo MCP strežnikov in njihovih orodij.
- Novim orodjem lahko razširite MCP strežnike, s čimer izboljšate zmožnosti agenta, da ustreza spreminjajočim se zahtevam.
- AI Toolkit vključuje predloge (npr. Python predloge za MCP strežnik), ki poenostavijo ustvarjanje lastnih orodij.

## Dodatni viri

- [Dokumentacija za AI Toolkit](https://aka.ms/AIToolkit/doc)

## Kaj sledi
- Naslednje: [Testiranje in razhroščevanje](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->