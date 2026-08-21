# Korištenje servera iz AI Toolkit ekstenzije za Visual Studio Code

Kada gradite AI agenta, nije riječ samo o generiranju pametnih odgovora; radi se i o davanju vašem agentu mogućnost da poduzme akciju. Tu na scenu stupa Model Context Protocol (MCP). MCP olakšava agentima pristup vanjskim alatima i uslugama na dosljedan način. Zamislite to kao priključivanje vašeg agenta u alatni okvir koji on *zapravo* može koristiti.

Recimo da povežete agenta s vašim kalkulator MCP serverom. Odjednom, vaš agent može izvršavati matematičke operacije samo primanjem upita kao što je „Koliko je 47 puta 89?“—nema potrebe za ručnim kodiranjem logike ili izradom prilagođenih API-ja.

## Pregled

Ova lekcija pokriva kako povezati kalkulator MCP server s agentom koristeći [AI Toolkit](https://aka.ms/AIToolkit) ekstenziju u Visual Studio Code-u, omogućujući vašem agentu da izvršava matematičke operacije kao što su zbrajanje, oduzimanje, množenje i dijeljenje putem prirodnog jezika.

AI Toolkit je moćna ekstenzija za Visual Studio Code koja pojednostavljuje razvoj agenata. AI inženjeri mogu lako graditi AI aplikacije razvijanjem i testiranjem generativnih AI modela—lokalno ili u oblaku. Ekstenzija podržava većinu glavnih današnjih generativnih modela.

*Napomena*: AI Toolkit trenutačno podržava Python i TypeScript.

## Ciljevi učenja

Do kraja ove lekcije, moći ćete:

- Koristiti MCP server putem AI Toolkita.
- Konfigurirati postavke agenta kako bi mogao otkriti i koristiti alate koje pruža MCP server.
- Koristiti MCP alate putem prirodnog jezika.

## Pristup

Evo kako trebamo pristupiti ovome na visokoj razini:

- Kreirati agenta i definirati njegov sistemski prompt.
- Kreirati MCP server s kalkulator alatima.
- Povezati Agent Builder s MCP serverom.
- Testirati pozivanje alata agenta putem prirodnog jezika.

Odlično, sada kad razumijemo tijek, konfigurirajmo AI agenta da koristi vanjske alate preko MCP-a, čime ćemo unaprijediti njegove sposobnosti!

## Preduvjeti

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit za Visual Studio Code](https://aka.ms/AIToolkit)

## Vježba: Korištenje servera

> [!WARNING]
> Napomena za korisnike macOS-a. Trenutno istražujemo problem s instalacijom ovisnosti na macOS-u. Kao rezultat toga, korisnici macOS-a trenutno neće moći dovršiti ovaj vodič. Ažurirat ćemo upute čim poprave budu dostupne. Hvala na vašem strpljenju i razumijevanju!

U ovoj vježbi izgradit ćete, pokrenuti i unaprijediti AI agenta s alatima s MCP servera unutar Visual Studio Code koristeći AI Toolkit.

### -0- Prekorak, dodajte OpenAI GPT-4o model u Moje modele

Vježba koristi **GPT-4o** model. Model treba biti dodan u **Moje modele** prije stvaranja agenta.

![Screenshot sučelja za odabir modela u AI Toolkit ekstenziji Visual Studio Codea. Naslov glasi "Pronađite pravi model za svoje AI rješenje" s podnaslovom koji poziva korisnike da otkriju, testiraju i implementiraju AI modele. Ispod, pod "Popularni modeli," prikazano je šest model karata: DeepSeek-R1 (hostan na GitHubu), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Mali, Brzi) i DeepSeek-R1 (hostan na Ollami). Svaka karta uključuje opcije "Dodaj" model ili "Isprobaj u Playgroundu](../../../../translated_images/hr/aitk-model-catalog.2acd38953bb9c119.webp)

1. Otvorite **AI Toolkit** ekstenziju iz **Activity Bar**.
1. U odjeljku **Katalog** odaberite **Modele** da otvorite **Katalog modela**. Odabirom **Modeli** otvara se **Katalog modela** u novoj kartici uređivača.
1. U tražilici **Kataloga modela** unesite **OpenAI GPT-4o**.
1. Kliknite **+ Dodaj** da dodate model na svoj popis **Moji modeli**. Provjerite da ste odabrali model koji je **hostan na GitHubu**.
1. U **Activity Bar** potvrdite da se model **OpenAI GPT-4o** nalazi na popisu.

### -1- Kreirajte agenta

**Agent (Prompt) Builder** omogućuje vam stvaranje i prilagodbu vlastitih AI-agenta. U ovom dijelu kreirat ćete novog agenta i odabrati model koji će pokretati razgovor.

![Screenshot sučelja "Calculator Agent" builder u AI Toolkit ekstenziji za Visual Studio Code. Na lijevoj ploči odabrani model je "OpenAI GPT-4o (putem GitHuba)." Sistemski prompt glasi "Vi ste profesor na sveučilištu koji predaje matematiku," a korisnički prompt kaže "Objasni mi Fourierovu jednadžbu jednostavnim rječnikom." Dodatne opcije uključuju gumbe za dodavanje alata, omogućavanje MCP Servera i odabir strukturiranog izlaza. Na dnu plave “Pokreni” tipke. Na desnoj ploči, pod "Započnite s primjerima," navedena su tri uzorka agenta: Web Developer (s MCP Serverom, pojednostavniteljem za drugi razred i tumačem snova, svaki sa kratkim opisima funkcija).](../../../../translated_images/hr/aitk-agent-builder.901e3a2960c3e477.webp)

1. Otvorite **AI Toolkit** ekstenziju iz **Activity Bar**.
1. U odjeljku **Alati** odaberite **Agent (Prompt) Builder**. Odabirom **Agent (Prompt) Builder** otvara se u novoj kartici uređivača.
1. Kliknite gumb **+ Novi agent**. Ekstenzija će pokrenuti postavke putem **Command Palette**.
1. Unesite naziv **Calculator Agent** i pritisnite **Enter**.
1. U **Agent (Prompt) Builder**, u polju **Model**, odaberite model **OpenAI GPT-4o (putem GitHuba)**.

### -2- Kreirajte sistemski prompt za agenta

Sada kad ste kreirali načelo agenta, vrijeme je da definirate njegovu osobnost i svrhu. U ovom dijelu koristit ćete značajku **Generate system prompt** da opišete namjeravano ponašanje agenta—u ovom slučaju agenta kalkulatora—i da model napiše sistemski prompt za vas.

![Screenshot sučelja "Calculator Agent" u AI Toolkitu za Visual Studio Code sa otvorenim modalnim prozorom pod nazivom "Generate a prompt." Modal objašnjava da se predložak prompta može generirati dijeljenjem osnovnih podataka i sadrži tekstni okvir s primjerom sistemskog prompta: "Vi ste koristan i učinkovit pomoćnik za matematiku. Kada vam se ponudi problem koji uključuje osnovnu aritmetiku, odgovarate s točnim rezultatom." Ispod tekstnog okvira su gumbi "Zatvori" i "Generiraj." U pozadini je vidljiv dio konfiguracije agenta, uključujući odabrani model "OpenAI GPT-4o (putem GitHuba)" i polja za sistemski i korisnički prompt.](../../../../translated_images/hr/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. U odjeljku **Promptovi** kliknite gumb **Generate system prompt**. Ovaj gumb otvara alat za izradu prompta koji koristi AI za generiranje sistemskog prompta za agenta.
1. U prozoru **Generate a prompt** unesite sljedeće: `Vi ste koristan i učinkovit matematički pomoćnik. Kada vam se ponudi problem koji uključuje osnovnu aritmetiku, odgovarate točnim rezultatom.`
1. Kliknite gumb **Generate**. Obavijest će se pojaviti u donjem desnom kutu potvrđujući da se sistemski prompt generira. Nakon što generiranje prompta završi, prompt će se pojaviti u polju **System prompt** u **Agent (Prompt) Builderu**.
1. Pregledajte **System prompt** i po potrebi ga izmijenite.

### -3- Kreirajte MCP server

Sada kad ste definirali sistemski prompt vašeg agenta—koji vodi njegovo ponašanje i odgovore—vrijeme je da agenta opremite praktičnim sposobnostima. U ovom dijelu kreirat ćete kalkulator MCP server s alatima za izvođenje zbrajanja, oduzimanja, množenja i dijeljenja. Ovaj server će omogućiti vašem agentu da izvede matematičke operacije u stvarnom vremenu kao odgovor na upite na prirodnom jeziku.

!["Screenshot donjeg dijela sučelja Calculator Agent u AI Toolkit ekstenziji za Visual Studio Code. Prikazuje proširive izbornike za “Alate” i “Strukturirani izlaz,” zajedno s padajućim izbornikom naziva “Odaberi format izlaza” postavljenim na “tekst.” S desne strane gumb “+ MCP Server” za dodavanje Model Context Protocol servera. Iznad sekcije Alati prikazuje se rezervirano mjesto za ikonu slike.](../../../../translated_images/hr/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit opremljen je predlošcima za lakše kreiranje vlastitih MCP servera. Koristit ćemo Python predložak za kreiranje kalkulator MCP servera.

*Napomena*: AI Toolkit trenutačno podržava Python i TypeScript.

1. U odjeljku **Alati** u **Agent (Prompt) Builderu**, kliknite gumb **+ MCP Server**. Ekstenzija će pokrenuti postavke putem **Command Palette**.
1. Odaberite **+ Dodaj server**.
1. Odaberite **Kreiraj novi MCP server**.
1. Odaberite predložak **python-weather**.
1. Odaberite **Zadana mapa** za spremanje predloška MCP servera.
1. Unesite sljedeći naziv za server: **Calculator**
1. Otvorit će se novi Visual Studio Code prozor. Odaberite **Da, vjerujem autorima**.
1. Koristeći terminal (**Terminal** > **Novi terminal**), kreirajte virtualno okruženje: `python -m venv .venv`
1. Koristeći terminal, aktivirajte virtualno okruženje:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Koristeći terminal, instalirajte ovisnosti: `pip install -e .[dev]`
1. U pogledu **Explorer** u **Activity Bar**, proširite direktorij **src** i odaberite **server.py** da otvorite datoteku u uređivaču.
1. Zamijenite kod u datoteci **server.py** sljedećim i spremite:

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

### -4- Pokrenite agenta s kalkulator MCP serverom

Sada kad vaš agent ima alate, vrijeme je da ih upotrijebite! U ovom dijelu možete poslati upite agentu da testirate i potvrdite koristi li agent odgovarajući alat s kalkulator MCP servera.

![Screenshot sučelja Calculator Agent u AI Toolkit ekstenziji za Visual Studio Code. Na lijevom panelu, pod “Alati,” dodan je MCP server pod imenom local-server-calculator_server, koji prikazuje četiri dostupna alata: zbrajanje, oduzimanje, množenje i dijeljenje. Prikazana je oznaka da su četiri alata aktivna. Ispod je sklopljen odjeljak “Strukturirani izlaz” i plavi gumb “Pokreni.” Na desnom panelu, pod “Odgovor modela,” agent poziva alate za množenje i oduzimanje s unosima {"a": 3, "b": 25} i {"a": 75, "b": 20} redom. Konačni “Odgovor alata” prikazan je kao 75.0. Na dnu se pojavljuje gumb “Prikaži kod.”](../../../../translated_images/hr/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Pokrenut ćete kalkulator MCP server na svojem lokalnom razvojnom računalu putem **Agent Buildera** kao MCP klijenta.

1. Pritisnite `F5` za početak debugiranja MCP servera. **Agent (Prompt) Builder** otvorit će se u novoj kartici uređivača. Status servera vidljiv je u terminalu.
1. U polju **User prompt** u **Agent (Prompt) Builderu** unesite ovaj prompt: `Kupio sam 3 artikla po cijeni od 25 $, i zatim iskoristio popust od 20 $. Koliko sam platio?`
1. Kliknite gumb **Pokreni** da generirate odgovor agenta.
1. Pregledajte izlaz agenta. Model bi trebao zaključiti da ste platili **55 $**.
1. Evo pregleda što bi se trebalo dogoditi:
    - Agent bira alate **množenje** i **oduzimanje** za pomoć u izračunu.
    - Dodijeljene su odgovarajuće vrijednosti `a` i `b` za alat **množenje**.
    - Dodijeljene su odgovarajuće vrijednosti `a` i `b` za alat **oduzimanje**.
    - Odgovor iz svakog alata prikazan je u polju **Odgovor alata**.
    - Konačni rezultat iz modela prikazan je u polju **Odgovor modela**.
1. Pošaljite dodatne upite za daljnje testiranje agenta. Možete izmijeniti postojeći prompt u polju **User prompt** klikom unutar polja i zamjenom postojećeg prompta.
1. Kad završite s testiranjem agenta, možete zaustaviti server putem **terminala** pritiskom **CTRL/CMD+C** da izađete.

## Zadatak

Pokušajte dodati dodatni alat u svoju datoteku **server.py** (npr.: vraćanje kvadratnog korijena broja). Pošaljite dodatne upite koji zahtijevaju da agent koristi novi alat (ili postojeće alate). Obavezno ponovno pokrenite server da bi se učitali novododani alati.

## Rješenje

[Rješenje](./solution/README.md)

## Ključni zaključci

Zaključci iz ovog poglavlja su sljedeći:

- AI Toolkit ekstenzija je izvrstan klijent koji vam omogućuje korištenje MCP servera i njihovih alata.
- Možete dodavati nove alate MCP serverima, šireći mogućnosti agenta da zadovolji mijenjajuće zahtjeve.
- AI Toolkit uključuje predloške (npr. Python MCP server predloške) koji pojednostavljuju izradu prilagođenih alata.

## Dodatni resursi

- [AI Toolkit dokumentacija](https://aka.ms/AIToolkit/doc)

## Što slijedi
- Sljedeće: [Testiranje i otklanjanje pogrešaka](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->