# Serverio naudojimas iš AI Toolkit plėtinio Visual Studio Code aplinkoje

Kai kuriate AI agentą, tai nėra tik apie protingų atsakymų generavimą; taip pat svarbu suteikti agentui galimybę imtis veiksmų. Čia įžengia Model Context Protocol (MCP). MCP leidžia agentams lengvai prieiti prie išorinių įrankių ir paslaugų nuosekliai. Galvokite apie tai kaip prisijungimą prie įrankių dėžės, kurią jūsų agentas *iš tikrųjų* gali naudoti.

Tarkime, jūs jungi agentą prie savo skaičiuoklės MCP serverio. Staiga jūsų agentas gali atlikti matematinius veiksmus tiesiog gavęs užklausą, pavyzdžiui, „Kiek yra 47 kart 89?“ – nereikia koduoti logikos ar kurti specialių API.

## Apžvalga

Ši pamoka aptaria, kaip prijungti skaičiuoklės MCP serverį prie agento naudojant [AI Toolkit](https://aka.ms/AIToolkit) plėtinį Visual Studio Code, leidžiant agentui atlikti matematinius veiksmus, tokius kaip sudėtis, atimtis, daugyba ir dalyba per natūralią kalbą.

AI Toolkit yra galingas Visual Studio Code plėtinys, palengvinantis agentų kūrimą. AI inžinieriai gali lengvai kurti AI programas, tobulindami ir testuodami generatyvinius AI modelius – tiek lokaliai, tiek debesyje. Plėtinys palaiko daugumą šiandien prieinamų pagrindinių generatyvinių modelių.

*Pastaba*: Šiuo metu AI Toolkit palaiko Python ir TypeScript.

## Mokymosi tikslai

Pasibaigus šiai pamokai, jūs galėsite:

- Naudoti MCP serverį per AI Toolkit.
- Konfigūruoti agento sąranka, kad jis galėtų atrasti ir naudotis MCP serverio įrankiais.
- Naudoti MCP įrankius natūralia kalba.

## Veiksmų planas

Štai kaip turime atlikti šiuos veiksmus aukštu lygiu:

- Sukurti agentą ir apibrėžti jo sistemos užklausą.
- Sukurti MCP serverį su skaičiuoklės įrankiais.
- Prijungti Agent Builder prie MCP serverio.
- Išbandyti agento įrankių iškvietimą natūralia kalba.

Puiku, dabar, kai suprantame srautą, sukonfigūruokime AI agentą naudotis išoriniais įrankiais per MCP, taip praplėsdami jo galimybes!

## Reikalingos sąlygos

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Pratimai: Serverio naudojimas

> [!WARNING]
> Pastaba macOS naudotojams. Šiuo metu tiriame problemą, susijusią su priklausomybių diegimu macOS sistemoje. Dėl to macOS naudotojai šią pamoką šiuo metu negalės baigti. Instrukcijos bus atnaujintos iškart, kai bus prieinama pataisa. Ačiū už kantrybę ir supratimą!

Šiame pratime jūs kursite, paleisite ir tobulinsite AI agentą su įrankiais iš MCP serverio Visual Studio Code aplinkoje, naudojant AI Toolkit.

### -0- Prieš žingsnį: pridėkite OpenAI GPT-4o modelį į „My Models“

Pratimas naudoja **GPT-4o** modelį. Modelis turėtų būti pridėtas prie **My Models** prieš kuriant agentą.

![Ekrano kopija, rodanti modelių pasirinkimo sąsają AI Toolkit plėtinyje Visual Studio Code. Antraštė skelbia „Raskite tinkamą modelį savo AI sprendimui“ su pastraipa, skatinančia naudotojus atrasti, išbandyti ir diegti AI modelius. Žemiau, skiltyje „Populiarūs modeliai“ rodomos šešios modelių kortelės: DeepSeek-R1 (GitHub saugomas), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Mažas, Greitas) ir DeepSeek-R1 (Ollama saugomas). Kiekvienoje kortelėje yra mygtukas „Add“ ir „Try in Playground“.](../../../../translated_images/lt/aitk-model-catalog.2acd38953bb9c119.webp)

1. Atidarykite **AI Toolkit** plėtinį iš **Activity Bar**.
1. Skiltyje **Catalog** pasirinkite **Models**, kad atidarytumėte **Model Catalog**. Pasirinkus **Models** atsidarys **Model Catalog** naujame redaktoriaus skirtuke.
1. Modelių katalogo paieškos juostoje įveskite **OpenAI GPT-4o**.
1. Spustelėkite **+ Add**, kad pridėtumėte modelį į savo **My Models** sąrašą. Įsitikinkite, kad pasirinkote modelį, kuris yra **hostinamas GitHub**.
1. Activity Bar patikrinkite, ar modelis **OpenAI GPT-4o** rodomas sąraše.

### -1- Sukurkite agentą

**Agent (Prompt) Builder** leidžia kurti ir pritaikyti savo AI agentus. Šioje skiltyje sukursite naują agentą ir priskirsite modelį pokalbio palaikymui.

![Ekrano kopija rodanti „Calculator Agent“ kūrimo sąsają AI Toolkit plėtinyje Visual Studio Code. Kairėje panelėje pasirinktas modelis „OpenAI GPT-4o (per GitHub).“ Sistemos užklausa skelbia „Jūs esate profesorius universitete, dėstantis matematiką,“ o naudotojo užklausa sako „Paaiškinkite man Fourier lygtį paprastai.“ Kituose skyriuose yra mygtukai įrankiams pridėti, MCP serveriui įjungti ir struktūruoto išvesties formato pasirinkimui. Apačioje yra mėlynas mygtukas „Run.“ Dešinėje panelėje, skyriuje „Get Started with Examples,“ yra trys pavyzdiniai agentai: Web Developer (su MCP Serveriu, antros klasės supaprastintuvu ir sapnų aiškintojų, su trumpais funkciijų aprašymais).](../../../../translated_images/lt/aitk-agent-builder.901e3a2960c3e477.webp)

1. Atidarykite **AI Toolkit** plėtinį **Activity Bar**.
1. Skiltyje **Tools** pasirinkite **Agent (Prompt) Builder**. Pasirinkus atsidarys **Agent (Prompt) Builder** naujame redaktoriaus skirtuke.
1. Spauskite mygtuką **+ New Agent**. Plėtinys paleis nustatymo vedlį per **Command Palette**.
1. Įveskite pavadinimą **Calculator Agent** ir paspauskite **Enter**.
1. Agent (Prompt) Builder lange lauke **Model** pasirinkite **OpenAI GPT-4o (per GitHub)** modelį.

### -2- Sukurkite agentui sistemos užklausą

Sukūrus agento karkasą, laikas apibrėžti jo asmenybę ir paskirtį. Šioje skiltyje naudosite funkciją **Generate system prompt**, kad aprašytumėte agento elgesį – šiuo atveju skaičiuoklės agentui, o modelis parašys sistemos užklausą už jus.

![Ekrano kopija rodanti „Calculator Agent“ sąsają AI Toolkit Visual Studio Code plėtinyje. Atidarytas modalinis langas „Generate a prompt.“ Modalas paaiškina, kad galima sugeneruoti užklausos šabloną pateikiant pagrindinius duomenis, ir yra teksto laukas su pavyzdine sistemos užklausa: „Jūs esate naudinga ir efektyvi matematikos pagalbininkė. Gavus užduotį, susijusią su pagrindine aritmetika, jūs atsakote teisingu rezultatu.“ Apačioje yra mygtukai „Close“ ir „Generate.“ Fone matoma dalis agento konfigūracijos, įskaitant pasirinktą modelį „OpenAI GPT-4o (per GitHub)“ ir laukus sisteminėms bei naudotojo užklausoms.](../../../../translated_images/lt/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Skiltyje **Prompts** spustelėkite mygtuką **Generate system prompt**. Šis mygtukas atidaro užklausų kūrimo įrankį, kuris naudoja AI sistemos užklausai sugeneruoti.
1. Langelyje **Generate a prompt** įveskite: `Jūs esate naudinga ir efektyvi matematikos pagalbininkė. Gavus užduotį, susijusią su pagrindine aritmetika, jūs atsakote teisingu rezultatu.`
1. Spustelėkite mygtuką **Generate**. Apatinėje dešinėje ekrano pusėje bus rodoma, kad sistema generuoja užklausą. Užklausai sugeneruoti baigus, ji pasirodys lauke **System prompt** Agent (Prompt) Builder lange.
1. Peržiūrėkite **System prompt** ir, jei reikia, pakoreguokite.

### -3- Sukurkite MCP serverį

Dabar, kai apibrėžėte agento sistemos užklausą, kuri nukreipia jo elgesį ir atsakymus, laikas aprūpinti agentą praktinėmis galimybėmis. Šioje dalyje kursite skaičiuoklės MCP serverį su įrankiais, leidžiančiais atlikti sudėtį, atimtį, daugybą ir dalybą. Šis serveris leis agentui atlikti realaus laiko matematinius veiksmus pagal natūralios kalbos užklausas.

![Ekrano kopija rodanti „Calculator Agent“ sąsajos apatinę dalį AI Toolkit plėtinyje Visual Studio Code. Rodomi išplečiami meniu „Tools“ ir „Structure output“, taip pat išskleidžiamas meniu „Pasirinkti išvesties formatą“ su pasirinkta „text“. Dešinėje yra mygtukas „+ MCP Server“ naujam Model Context Protocol serveriui pridėti. Virš „Tools“ skyriaus yra paveiksliuko piktograma.](../../../../translated_images/lt/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit turi šablonus, palengvinančius savo MCP serverių kūrimą. Mes naudosime Python šabloną skaičiuoklės MCP serverio kūrimui.

*Pastaba*: Šiuo metu AI Toolkit palaiko Python ir TypeScript.

1. Agent (Prompt) Builder lange, skiltyje **Tools**, spustelėkite mygtuką **+ MCP Server**. Plėtinys paleis nustatymo vedlį per **Command Palette**.
1. Pasirinkite **+ Add Server**.
1. Pasirinkite **Create a New MCP Server**.
1. Pasirinkite **python-weather** kaip šabloną.
1. Pasirinkite **Default folder** MCP serverio šablonui įrašyti.
1. Įveskite serverio pavadinimą: **Calculator**
1. Atsidarys naujas Visual Studio Code langas. Pasirinkite **Yes, I trust the authors**.
1. Naudodami terminalą (**Terminal** > **New Terminal**) sukurkite virtualią aplinką: `python -m venv .venv`
1. Naudodami terminalą aktyvuokite virtualią aplinką:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Naudodami terminalą įdiekite priklausomybes: `pip install -e .[dev]`
1. Naršyklės lange (Explorer) plėskite **src** katalogą ir atidarykite **server.py** failą redaktoriuje.
1. Pakeiskite **server.py** faile esantį kodą šiuo ir išsaugokite:

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

### -4- Paleiskite agentą su skaičiuoklės MCP serveriu

Dabar, kai jūsų agentas turi įrankius, laikas juos panaudoti! Šioje dalyje įveskite užklausas agentui, kad išbandytumėte ir įvertintumėte, ar agentas tinkamai naudoja skaičiuoklės MCP serverio įrankius.

![Ekrano kopija rodanti „Calculator Agent“ sąsają AI Toolkit plėtinyje Visual Studio Code. Kairėje panelėje, skyriuje „Tools“, pridėtas MCP serveris local-server-calculator_server su keturiais prieinamais įrankiais: add, subtract, multiply ir divide. Yra ženklelis, rodantis, kad keturi įrankiai aktyvūs. Žemiau matoma sugrupuota skiltis „Structure output“ ir mėlynas mygtukas „Run“. Dešinėje panelėje, skiltyje „Model Response“, agentas naudoja multiply ir subtract įrankius su duomenimis {"a": 3, "b": 25} ir {"a": 75, "b": 20}. Galutinis „Tool Response“ rodomas kaip 75.0. Po juo yra mygtukas „View Code“.](../../../../translated_images/lt/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Paleisite skaičiuoklės MCP serverį savo vietiniame kūrimo kompiuteryje per **Agent Builder** kaip MCP klientą.

1. Paspauskite `F5`, kad pradėtumėte dauginimą MCP serveriui. Agent (Prompt) Builder atsidarys naujame redaktoriaus skirtuke. Serverio būsena matoma terminale.
1. Agent (Prompt) Builder laukelyje **User prompt** įveskite užklausą: `Aš nusipirkau 3 prekes po 25 dolerius kiekviena, tada panaudojau 20 dolerių nuolaidą. Kiek sumokėjau?`
1. Spustelėkite mygtuką **Run**, kad sugeneruotumėte agento atsakymą.
1. Peržiūrėkite agento atsakymą. Modelis turėtų nuspręsti, kad sumokėjote **55 $**.
1. Štai kas turėtų vykti:
    - Agentas pasirenka **multiply** ir **subtract** įrankius skaičiavimams atlikti.
    - Liūdamos reikšmės `a` ir `b` priskiriamos **multiply** įrankiui.
    - Liūdamos reikšmės `a` ir `b` priskiriamos **subtract** įrankiui.
    - Kiekvieno įrankio atsakymai pateikiami atitinkamoje **Tool Response** dalyje.
    - Galutinis modelio atsakymas pateikiamas galutinėje **Model Response** dalyje.
1. Įveskite papildomas užklausas agentui toliau testuoti. Galite pakeisti esamą užklausą lauke **User prompt** paspausdami i ją ir pakeisdami tekstą.
1. Baigę testuoti, galite sustabdyti serverį terminale paspausdami **CTRL/CMD+C**.

## Užduotis

Pabandykite pridėti papildomą įrankį į savo **server.py** failą (pvz., funkciją, kuri apskaičiuoja skaičiaus kvadratinę šaknį). Įveskite papildomas užklausas, reikalaujančias naudoti jūsų naują įrankį (arba esamus). Nepamirškite perkrauti serverio, kad būtų įkelti nauji įrankiai.

## Sprendimas

[Sprendimas](./solution/README.md)

## Pagrindinės išvados

Šios pamokos pagrindinės išvados yra šios:

- AI Toolkit plėtinys yra puikus klientas, leidžiantis naudotis MCP serveriais ir jų įrankiais.
- Galite pridėti naujus įrankius MCP serveriams, plečiant agento galimybes prisitaikyti prie kintančių reikalavimų.
- AI Toolkit apima šablonus (pvz., Python MCP serverių šablonus), kurie palengvina tinkintų įrankių kūrimą.

## Papildomi ištekliai

- [AI Toolkit dokumentacija](https://aka.ms/AIToolkit/doc)

## Kas toliau
- Toliau: [Testavimas ir derinimas](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->