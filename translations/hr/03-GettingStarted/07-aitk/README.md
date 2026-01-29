# Korištenje servera iz AI Toolkit ekstenzije za Visual Studio Code

Kada gradite AI agenta, nije dovoljno samo generirati pametne odgovore; važno je omogućiti agentu da poduzima akcije. Tu dolazi Model Context Protocol (MCP). MCP omogućuje agentima da pristupe vanjskim alatima i uslugama na dosljedan način. Zamislite to kao da povezujete svog agenta s kutijom alata koju *zaista* može koristiti.

Recimo da povežete agenta s MCP serverom kalkulatora. Odjednom vaš agent može izvoditi matematičke operacije samo na temelju upita poput "Koliko je 47 puta 89?"—bez potrebe za hardkodiranjem logike ili izradom prilagođenih API-ja.

## Pregled

Ova lekcija pokriva kako povezati MCP server kalkulatora s agentom pomoću [AI Toolkit](https://aka.ms/AIToolkit) ekstenzije u Visual Studio Code-u, omogućujući vašem agentu da izvodi matematičke operacije poput zbrajanja, oduzimanja, množenja i dijeljenja putem prirodnog jezika.

AI Toolkit je moćna ekstenzija za Visual Studio Code koja pojednostavljuje razvoj agenata. AI inženjeri mogu lako graditi AI aplikacije razvijanjem i testiranjem generativnih AI modela—lokalno ili u oblaku. Ekstenzija podržava većinu glavnih generativnih modela dostupnih danas.

*Napomena*: AI Toolkit trenutno podržava Python i TypeScript.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Koristiti MCP server putem AI Toolkita.
- Konfigurirati postavke agenta kako bi mogao otkriti i koristiti alate koje pruža MCP server.
- Koristiti MCP alate putem prirodnog jezika.

## Pristup

Evo kako ćemo pristupiti ovom procesu na visokoj razini:

- Kreirati agenta i definirati njegov sistemski prompt.
- Kreirati MCP server s alatima kalkulatora.
- Povezati Agent Builder s MCP serverom.
- Testirati pozivanje alata agenta putem prirodnog jezika.

Odlično, sada kada razumijemo tijek, konfigurirajmo AI agenta kako bi koristio vanjske alate putem MCP-a, proširujući njegove mogućnosti!

## Preduvjeti

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit za Visual Studio Code](https://aka.ms/AIToolkit)

## Vježba: Korištenje servera

> [!WARNING]
> Napomena za korisnike macOS-a. Trenutno istražujemo problem koji utječe na instalaciju ovisnosti na macOS-u. Zbog toga korisnici macOS-a trenutno neće moći dovršiti ovaj vodič. Ažurirat ćemo upute čim bude dostupno rješenje. Hvala na strpljenju i razumijevanju!

U ovoj vježbi izgradit ćete, pokrenuti i unaprijediti AI agenta s alatima iz MCP servera unutar Visual Studio Code-a koristeći AI Toolkit.

### -0- Pripremni korak, dodajte OpenAI GPT-4o model u Moji modeli

Vježba koristi **GPT-4o** model. Model treba dodati u **Moji modeli** prije kreiranja agenta.

1. Otvorite **AI Toolkit** ekstenziju iz **Activity Bar**.
1. U sekciji **Catalog**, odaberite **Models** kako biste otvorili **Model Catalog**. Odabir **Models** otvara **Model Catalog** u novom editor tabu.
1. U traci za pretraživanje **Model Catalog**, unesite **OpenAI GPT-4o**.
1. Kliknite **+ Add** kako biste dodali model u svoj popis **My Models**. Provjerite jeste li odabrali model koji je **Hosted by GitHub**.
1. U **Activity Bar**, potvrdite da se model **OpenAI GPT-4o** pojavljuje na popisu.

### -1- Kreirajte agenta

**Agent (Prompt) Builder** omogućuje vam kreiranje i prilagodbu vlastitih AI agenata. U ovom dijelu kreirat ćete novog agenta i dodijeliti mu model za vođenje razgovora.

1. Otvorite **AI Toolkit** ekstenziju iz **Activity Bar**.
1. U sekciji **Tools**, odaberite **Agent (Prompt) Builder**. Odabir **Agent (Prompt) Builder** otvara **Agent (Prompt) Builder** u novom editor tabu.
1. Kliknite na gumb **+ New Agent**. Ekstenzija će pokrenuti čarobnjak za postavljanje putem **Command Palette**.
1. Unesite ime **Calculator Agent** i pritisnite **Enter**.
1. U **Agent (Prompt) Builder**, za polje **Model**, odaberite model **OpenAI GPT-4o (via GitHub)**.

### -2- Kreirajte sistemski prompt za agenta

Sada kada ste postavili osnovu za agenta, vrijeme je da definirate njegovu osobnost i svrhu. U ovom dijelu koristit ćete značajku **Generate system prompt** kako biste opisali namjeravano ponašanje agenta—u ovom slučaju, agenta kalkulatora—i omogućili modelu da napiše sistemski prompt za vas.

1. Za sekciju **Prompts**, kliknite gumb **Generate system prompt**. Ovaj gumb otvara alat za generiranje prompta koji koristi AI za generiranje sistemskog prompta za agenta.
1. U prozoru **Generate a prompt**, unesite sljedeće: `Vi ste koristan i učinkovit matematički asistent. Kada vam se postavi problem koji uključuje osnovnu aritmetiku, odgovarate s točnim rezultatom.`
1. Kliknite gumb **Generate**. Obavijest će se pojaviti u donjem desnom kutu potvrđujući da se sistemski prompt generira. Kada je generiranje prompta završeno, prompt će se pojaviti u polju **System prompt** u **Agent (Prompt) Builder**.
1. Pregledajte **System prompt** i po potrebi ga izmijenite.

### -3- Kreirajte MCP server

Sada kada ste definirali sistemski prompt vašeg agenta—usmjeravajući njegovo ponašanje i odgovore—vrijeme je da opremite agenta praktičnim mogućnostima. U ovom dijelu kreirat ćete MCP server kalkulatora s alatima za izvođenje zbrajanja, oduzimanja, množenja i dijeljenja. Ovaj server omogućit će vašem agentu da izvodi matematičke operacije u stvarnom vremenu kao odgovor na upite prirodnog jezika.

AI Toolkit dolazi s predlošcima koji olakšavaju kreiranje vlastitog MCP servera. Koristit ćemo Python predložak za kreiranje MCP servera kalkulatora.

*Napomena*: AI Toolkit trenutno podržava Python i TypeScript.

1. U sekciji **Tools** u **Agent (Prompt) Builder**, kliknite gumb **+ MCP Server**. Ekstenzija će pokrenuti čarobnjak za postavljanje putem **Command Palette**.
1. Odaberite **+ Add Server**.
1. Odaberite **Create a New MCP Server**.
1. Odaberite **python-weather** kao predložak.
1. Odaberite **Default folder** za spremanje predloška MCP servera.
1. Unesite sljedeće ime za server: **Calculator**
1. Novi prozor Visual Studio Code-a će se otvoriti. Odaberite **Yes, I trust the authors**.
1. Koristeći terminal (**Terminal** > **New Terminal**), kreirajte virtualno okruženje: `python -m venv .venv`
1. Koristeći terminal, aktivirajte virtualno okruženje:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Koristeći terminal, instalirajte ovisnosti: `pip install -e .[dev]`
1. U **Explorer** prikazu **Activity Bar**, proširite direktorij **src** i odaberite **server.py** kako biste otvorili datoteku u editoru.
1. Zamijenite kod u datoteci **server.py** sa sljedećim i spremite:

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

### -4- Pokrenite agenta s MCP serverom kalkulatora

Sada kada vaš agent ima alate, vrijeme je da ih koristi! U ovom dijelu, poslat ćete upite agentu kako biste testirali i provjerili koristi li odgovarajući alat iz MCP servera kalkulatora.

1. Pritisnite `F5` za pokretanje MCP servera. **Agent (Prompt) Builder** će se otvoriti u novom editor tabu. Status servera vidljiv je u terminalu.
1. U polje **User prompt** u **Agent (Prompt) Builder**, unesite sljedeći upit: `Kupio sam 3 artikla po cijeni od $25 svaki, a zatim iskoristio popust od $20. Koliko sam platio?`
1. Kliknite gumb **Run** za generiranje odgovora agenta.
1. Pregledajte izlaz agenta. Model bi trebao zaključiti da ste platili **$55**.
1. Evo što bi se trebalo dogoditi:
    - Agent odabire alate **multiply** i **subtract** kako bi pomogao u izračunu.
    - Odgovarajuće vrijednosti `a` i `b` dodijeljene su za alat **multiply**.
    - Odgovarajuće vrijednosti `a` i `b` dodijeljene su za alat **subtract**.
    - Odgovor svakog alata prikazan je u odgovarajućem **Tool Response**.
    - Konačni izlaz modela prikazan je u završnom **Model Response**.
1. Pošaljite dodatne upite kako biste dodatno testirali agenta. Možete izmijeniti postojeći upit u polju **User prompt** klikom u polje i zamjenom postojećeg upita.
1. Kada završite s testiranjem agenta, možete zaustaviti server putem **terminala** unosom **CTRL/CMD+C** za izlaz.

## Zadatak

Pokušajte dodati dodatni alat u svoju datoteku **server.py** (npr. vraćanje kvadratnog korijena broja). Pošaljite dodatne upite koji bi zahtijevali od agenta da koristi vaš novi alat (ili postojeće alate). Obavezno ponovno pokrenite server kako biste učitali novododane alate.

## Rješenje

[Rješenje](./solution/README.md)

## Ključni zaključci

Zaključci iz ovog poglavlja su sljedeći:

- AI Toolkit ekstenzija je izvrstan klijent koji omogućuje korištenje MCP servera i njihovih alata.
- Možete dodavati nove alate MCP serverima, proširujući mogućnosti agenta kako bi zadovoljio nove zahtjeve.
- AI Toolkit uključuje predloške (npr. Python MCP server predloške) za pojednostavljenje kreiranja prilagođenih alata.

## Dodatni resursi

- [AI Toolkit dokumentacija](https://aka.ms/AIToolkit/doc)

## Što slijedi
- Sljedeće: [Testiranje i ispravljanje grešaka](../08-testing/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.