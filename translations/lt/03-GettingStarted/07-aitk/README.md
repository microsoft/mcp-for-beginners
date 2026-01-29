# Naudojimasis serveriu iš AI Toolkit plėtinio Visual Studio Code

Kuriant dirbtinio intelekto agentą, svarbu ne tik generuoti išmanius atsakymus, bet ir suteikti agentui galimybę veikti. Čia pasitarnauja Model Context Protocol (MCP). MCP leidžia agentams lengvai ir nuosekliai pasiekti išorinius įrankius bei paslaugas. Galvokite apie tai kaip apie įrankių dėžę, kurią jūsų agentas gali *tikrai* naudoti.

Pavyzdžiui, prijungus agentą prie skaičiuotuvo MCP serverio, jūsų agentas galės atlikti matematines operacijas tiesiog gavęs užklausą, pavyzdžiui, „Kiek yra 47 kart 89?“—nereikia kietai koduoti logikos ar kurti individualių API.

## Apžvalga

Šioje pamokoje aptarsime, kaip prijungti skaičiuotuvo MCP serverį prie agento naudojant [AI Toolkit](https://aka.ms/AIToolkit) plėtinį Visual Studio Code, leidžiant agentui atlikti matematines operacijas, tokias kaip sudėtis, atimtis, daugyba ir dalyba, naudojant natūralią kalbą.

AI Toolkit yra galingas Visual Studio Code plėtinys, kuris supaprastina agentų kūrimą. Dirbtinio intelekto inžinieriai gali lengvai kurti AI programas, testuoti generatyvinius modelius tiek lokaliai, tiek debesyje. Šis plėtinys palaiko daugumą šiandien populiarių generatyvinių modelių.

*Pastaba*: AI Toolkit šiuo metu palaiko Python ir TypeScript.

## Mokymosi tikslai

Šios pamokos pabaigoje jūs galėsite:

- Naudoti MCP serverį per AI Toolkit.
- Suformuoti agento konfigūraciją, kad jis galėtų aptikti ir naudoti MCP serverio teikiamus įrankius.
- Naudoti MCP įrankius per natūralią kalbą.

## Metodika

Štai kaip mes tai atliksime:

- Sukursime agentą ir apibrėšime jo sistemos užklausą.
- Sukursime MCP serverį su skaičiuotuvo įrankiais.
- Prijungsime Agent Builder prie MCP serverio.
- Išbandysime agento įrankių naudojimą per natūralią kalbą.

Puiku, dabar, kai suprantame procesą, sukonfigūruokime AI agentą, kad jis galėtų naudotis išoriniais įrankiais per MCP ir taip pagerintų savo galimybes!

## Reikalavimai

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Pratimas: Naudojimasis serveriu

> [!WARNING]
> Pastaba macOS naudotojams. Šiuo metu tiriame problemą, susijusią su priklausomybių diegimu macOS sistemoje. Dėl šios priežasties macOS naudotojai šiuo metu negalės užbaigti šios pamokos. Mes atnaujinsime instrukcijas, kai tik bus išspręsta problema. Dėkojame už jūsų kantrybę ir supratingumą!

Šiame pratime sukursite, paleisite ir patobulinsite AI agentą su MCP serverio įrankiais Visual Studio Code aplinkoje, naudodami AI Toolkit.

### -0- Pradinis žingsnis: pridėkite OpenAI GPT-4o modelį į Mano modelius

Šiame pratime naudojamas **GPT-4o** modelis. Modelis turi būti pridėtas į **Mano modelius** prieš kuriant agentą.

1. Atidarykite **AI Toolkit** plėtinį iš **Activity Bar**.
1. **Katalogo** skiltyje pasirinkite **Models**, kad atidarytumėte **Modelių katalogą**. Pasirinkus **Models**, **Modelių katalogas** atsidarys naujame redaktoriaus skirtuke.
1. **Modelių katalogo** paieškos laukelyje įveskite **OpenAI GPT-4o**.
1. Spustelėkite **+ Add**, kad pridėtumėte modelį į savo **Mano modelius** sąrašą. Įsitikinkite, kad pasirinkote modelį, kuris yra **Hosted by GitHub**.
1. **Activity Bar** patikrinkite, ar **OpenAI GPT-4o** modelis rodomas sąraše.

### -1- Sukurkite agentą

**Agent (Prompt) Builder** leidžia jums kurti ir pritaikyti savo AI agentus. Šioje dalyje sukursite naują agentą ir priskirsite modelį, kuris valdys pokalbį.

1. Atidarykite **AI Toolkit** plėtinį iš **Activity Bar**.
1. **Įrankių** skiltyje pasirinkite **Agent (Prompt) Builder**. Pasirinkus **Agent (Prompt) Builder**, jis atsidarys naujame redaktoriaus skirtuke.
1. Spustelėkite **+ New Agent** mygtuką. Plėtinys paleis nustatymų vedlį per **Command Palette**.
1. Įveskite pavadinimą **Calculator Agent** ir paspauskite **Enter**.
1. **Agent (Prompt) Builder** lange, **Modelio** lauke, pasirinkite **OpenAI GPT-4o (via GitHub)** modelį.

### -2- Sukurkite sistemos užklausą agentui

Sukūrus agento struktūrą, laikas apibrėžti jo asmenybę ir tikslą. Šioje dalyje naudosite **Generate system prompt** funkciją, kad aprašytumėte agento elgesį—šiuo atveju, skaičiuotuvo agentą—ir leisite modeliui sugeneruoti sistemos užklausą už jus.

1. **Užklausų** skiltyje spustelėkite **Generate system prompt** mygtuką. Šis mygtukas atidaro užklausų kūrimo įrankį, kuris naudoja AI, kad sugeneruotų sistemos užklausą agentui.
1. **Generate a prompt** lange įveskite: `Jūs esate naudingas ir efektyvus matematikos asistentas. Gavęs užduotį, susijusią su pagrindine aritmetika, atsakote teisingu rezultatu.`
1. Spustelėkite **Generate** mygtuką. Apatinėje dešinėje ekrano pusėje pasirodys pranešimas, patvirtinantis, kad sistemos užklausa generuojama. Kai užklausos generavimas bus baigtas, ji pasirodys **System prompt** lauke **Agent (Prompt) Builder** lange.
1. Peržiūrėkite **System prompt** ir, jei reikia, pakoreguokite.

### -3- Sukurkite MCP serverį

Dabar, kai apibrėžėte agento sistemos užklausą—nustatydami jo elgesį ir atsakymus—laikas suteikti agentui praktinių galimybių. Šioje dalyje sukursite skaičiuotuvo MCP serverį su įrankiais, kurie vykdo sudėties, atimties, daugybos ir dalybos skaičiavimus. Šis serveris leis jūsų agentui realiu laiku atlikti matematines operacijas, reaguojant į natūralios kalbos užklausas.

AI Toolkit turi šablonus, kurie palengvina MCP serverių kūrimą. Naudosime Python šabloną skaičiuotuvo MCP serverio kūrimui.

*Pastaba*: AI Toolkit šiuo metu palaiko Python ir TypeScript.

1. **Įrankių** skiltyje **Agent (Prompt) Builder** lange spustelėkite **+ MCP Server** mygtuką. Plėtinys paleis nustatymų vedlį per **Command Palette**.
1. Pasirinkite **+ Add Server**.
1. Pasirinkite **Create a New MCP Server**.
1. Pasirinkite **python-weather** kaip šabloną.
1. Pasirinkite **Default folder**, kad išsaugotumėte MCP serverio šabloną.
1. Įveskite šį serverio pavadinimą: **Calculator**.
1. Naujas Visual Studio Code langas atsidarys. Pasirinkite **Yes, I trust the authors**.
1. Terminale (**Terminal** > **New Terminal**) sukurkite virtualią aplinką: `python -m venv .venv`.
1. Terminale aktyvuokite virtualią aplinką:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Terminale įdiekite priklausomybes: `pip install -e .[dev]`.
1. **Activity Bar** **Explorer** skiltyje išskleiskite **src** katalogą ir pasirinkite **server.py**, kad atidarytumėte failą redaktoriuje.
1. Pakeiskite **server.py** failo kodą šiuo ir išsaugokite:

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

### -4- Paleiskite agentą su skaičiuotuvo MCP serveriu

Dabar, kai jūsų agentas turi įrankius, laikas juos naudoti! Šioje dalyje pateiksite užklausas agentui, kad išbandytumėte ir patikrintumėte, ar agentas naudoja tinkamą įrankį iš skaičiuotuvo MCP serverio.

1. Paspauskite `F5`, kad pradėtumėte MCP serverio derinimą. **Agent (Prompt) Builder** atsidarys naujame redaktoriaus skirtuke. Serverio būsena bus matoma terminale.
1. **User prompt** lauke **Agent (Prompt) Builder** lange įveskite šią užklausą: `Aš nusipirkau 3 prekes, kurių kiekviena kainavo 25 $, o tada pasinaudojau 20 $ nuolaida. Kiek sumokėjau?`
1. Spustelėkite **Run** mygtuką, kad sugeneruotumėte agento atsakymą.
1. Peržiūrėkite agento atsakymą. Modelis turėtų apskaičiuoti, kad sumokėjote **55 $**.
1. Štai kas turėtų įvykti:
    - Agentas pasirenka **multiply** ir **subtract** įrankius, kad atliktų skaičiavimą.
    - **multiply** įrankiui priskiriamos atitinkamos `a` ir `b` reikšmės.
    - **subtract** įrankiui priskiriamos atitinkamos `a` ir `b` reikšmės.
    - Kiekvieno įrankio atsakymas pateikiamas **Tool Response** lauke.
    - Galutinis modelio atsakymas pateikiamas **Model Response** lauke.
1. Pateikite papildomas užklausas, kad toliau testuotumėte agentą. Galite pakeisti esamą užklausą **User prompt** lauke, spustelėdami į lauką ir pakeisdami esamą tekstą.
1. Baigę testuoti agentą, galite sustabdyti serverį terminale įvesdami **CTRL/CMD+C**, kad išeitumėte.

## Užduotis

Pabandykite pridėti papildomą įrankį į savo **server.py** failą (pvz., grąžinti skaičiaus kvadratinę šaknį). Pateikite papildomas užklausas, kurios reikalautų, kad agentas naudotų jūsų naują įrankį (arba esamus įrankius). Nepamirškite iš naujo paleisti serverio, kad įkeltumėte naujai pridėtus įrankius.

## Sprendimas

[Sprendimas](./solution/README.md)

## Pagrindinės išvados

Šio skyriaus pagrindinės išvados:

- AI Toolkit plėtinys yra puikus klientas, leidžiantis naudoti MCP serverius ir jų įrankius.
- Galite pridėti naujų įrankių į MCP serverius, išplėsdami agento galimybes, kad jos atitiktų besikeičiančius poreikius.
- AI Toolkit turi šablonus (pvz., Python MCP serverio šablonus), kurie supaprastina individualių įrankių kūrimą.

## Papildomi ištekliai

- [AI Toolkit dokumentacija](https://aka.ms/AIToolkit/doc)

## Kas toliau
- Toliau: [Testavimas ir derinimas](../08-testing/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.