# Serveri kasutamine Visual Studio Code'i AI Toolkit laienduses

AI-agendi loomisel ei ole oluline ainult nutikate vastuste genereerimine, vaid ka agendi võimekus tegutseda. Siin tuleb mängu Model Context Protocol (MCP). MCP muudab agentidele väliste tööriistade ja teenuste ühtse viisi kaudu ligipääsu lihtsaks. Kujutage ette, et ühendate oma agendi tööriistakastiga, mida ta *päriselt* kasutada saab.

Oletame, et ühendate agendi oma kalkulaatori MCP serveriga. Järsku saab teie agent matemaatilisi tehteid teha lihtsalt vastates küsimusele nagu „Mis on 47 korda 89?“—ilma vajaduseta koodida loogikat või luua kohandatud API-sid.

## Ülevaade

Selles peatükis õpite, kuidas ühendada kalkulaatori MCP server agendiga, kasutades [AI Toolkit](https://aka.ms/AIToolkit) laiendust Visual Studio Code'is. See võimaldab teie agendil teha matemaatilisi tehteid, nagu liitmine, lahutamine, korrutamine ja jagamine, kasutades loomulikku keelt.

AI Toolkit on võimas Visual Studio Code'i laiendus, mis lihtsustab agendi arendamist. AI-insenerid saavad hõlpsasti luua AI-rakendusi, arendades ja testides generatiivseid AI-mudeleid—kohapeal või pilves. Laiendus toetab enamikku tänapäeval saadaolevatest generatiivsetest mudelitest.

*NB*: AI Toolkit toetab praegu Pythonit ja TypeScripti.

## Õpieesmärgid

Selle peatüki lõpuks oskate:

- Kasutada MCP serverit AI Toolkiti kaudu.
- Konfigureerida agendi seadistust, et võimaldada tal avastada ja kasutada MCP serveri pakutavaid tööriistu.
- Kasutada MCP tööriistu loomuliku keele kaudu.

## Lähenemine

Siin on üldine lähenemisviis:

- Looge agent ja määratlege selle süsteemiprompt.
- Looge MCP server kalkulaatori tööriistadega.
- Ühendage Agent Builder MCP serveriga.
- Testige agendi tööriistade kasutamist loomuliku keele kaudu.

Suurepärane, nüüd kui mõistame protsessi, konfigureerime AI-agendi, et MCP kaudu väliseid tööriistu kasutada ja selle võimekust suurendada!

## Eeltingimused

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Harjutus: Serveri kasutamine

> [!WARNING]
> Märkus macOS-i kasutajatele. Uurime praegu probleemi, mis mõjutab sõltuvuste installimist macOS-is. Selle tulemusena ei saa macOS-i kasutajad praegu seda juhendit lõpule viia. Uuendame juhiseid niipea, kui lahendus on saadaval. Täname teid kannatlikkuse ja mõistmise eest!

Selles harjutuses loote, käivitate ja täiustate AI-agenti MCP serveri tööriistadega Visual Studio Code'is, kasutades AI Toolkiti.

### -0- Eelnev samm: lisage OpenAI GPT-4o mudel Minu Mudelitesse

Harjutus kasutab **GPT-4o** mudelit. Mudel tuleks lisada **Minu Mudelitesse** enne agendi loomist.

![Kuvapilt Visual Studio Code'i AI Toolkiti laienduse mudelivaliku liidesest. Pealkiri on "Leia õige mudel oma AI lahenduse jaoks" koos alapealkirjaga, mis julgustab kasutajaid avastama, testima ja juurutama AI-mudeleid. Allpool, jaotises “Populaarsed mudelid,” kuvatakse kuus mudelikaarti: DeepSeek-R1 (GitHub-hostitud), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Väike, Kiire) ja DeepSeek-R1 (Ollama-hostitud). Igal kaardil on valikud “Lisa” mudel või “Proovi mänguväljakus.”](../../../../translated_images/et/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.png)

1. Avage **AI Toolkit** laiendus **Activity Bar**-ist.
1. **Kataloogi** jaotises valige **Mudelid**, et avada **Mudelite kataloog**. Mudelite valimine avab **Mudelite kataloogi** uues redaktori vahekaardil.
1. **Mudelite kataloogi** otsinguribale sisestage **OpenAI GPT-4o**.
1. Klõpsake **+ Lisa**, et lisada mudel oma **Minu Mudelitesse**. Veenduge, et olete valinud mudeli, mis on **GitHubi poolt hostitud**.
1. **Activity Bar**-is kinnitage, et **OpenAI GPT-4o** mudel ilmub loendisse.

### -1- Looge agent

**Agent (Prompt) Builder** võimaldab teil luua ja kohandada oma AI-põhiseid agente. Selles jaotises loote uue agendi ja määrate mudeli vestluse juhtimiseks.

![Kuvapilt "Kalkulaatori agendi" ehitaja liidesest Visual Studio Code'i AI Toolkiti laienduses. Vasakul paneelil on valitud mudel "OpenAI GPT-4o (GitHubi kaudu)." Süsteemiprompt on "Olete ülikooli professor, kes õpetab matemaatikat," ja kasutajaprompt on "Selgitage Fourier'i võrrandit lihtsate sõnadega." Täiendavad valikud hõlmavad nuppe tööriistade lisamiseks, MCP serveri lubamiseks ja struktureeritud väljundi valimiseks. Allosas on sinine “Käivita” nupp. Paremal paneelil, jaotises "Alustage näidetega," on loetletud kolm näidisagenti: Veebiarendaja (koos MCP serveriga), Teise klassi lihtsustaja ja Unenäotõlgendaja, igaühe lühikirjeldustega nende funktsioonidest.](../../../../translated_images/et/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.png)

1. Avage **AI Toolkit** laiendus **Activity Bar**-ist.
1. **Tööriistade** jaotises valige **Agent (Prompt) Builder**. Agendi valimine avab **Agent (Prompt) Builder** uues redaktori vahekaardil.
1. Klõpsake **+ Uus agent** nuppu. Laiendus käivitab seadistusviisardi **Command Palette** kaudu.
1. Sisestage nimi **Kalkulaatori agent** ja vajutage **Enter**.
1. **Agent (Prompt) Builder**-is valige **Mudel**-väljal **OpenAI GPT-4o (GitHubi kaudu)** mudel.

### -2- Looge agendi süsteemiprompt

Kui agent on loodud, on aeg määratleda selle isiksus ja eesmärk. Selles jaotises kasutate **Generate system prompt** funktsiooni, et kirjeldada agendi kavandatud käitumist—antud juhul kalkulaatori agenti—ja lasete mudelil süsteemiprompti teie eest kirjutada.

![Kuvapilt "Kalkulaatori agendi" liidesest Visual Studio Code'i AI Toolkiti laienduses, kus on avatud modaalaken pealkirjaga "Loo prompt." Modaal selgitab, et prompti mall saab luua, jagades põhiandmeid, ja sisaldab tekstikasti näidissüsteemipromptiga: "Olete abivalmis ja tõhus matemaatikaassistent. Kui teile antakse probleem, mis hõlmab põhiaritmeetikat, vastate õige tulemusega." Tekstikasti all on nupud "Sulge" ja "Loo." Taustal on näha osa agendi konfiguratsioonist, sealhulgas valitud mudel "OpenAI GPT-4o (GitHubi kaudu)" ja väljad süsteemi- ja kasutajapromptide jaoks.](../../../../translated_images/et/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.png)

1. **Promptide** jaotises klõpsake **Generate system prompt** nuppu. See nupp avab prompti generaatori, mis kasutab AI-d agendi süsteemiprompti loomiseks.
1. **Generate a prompt** aknas sisestage järgmine: `Olete abivalmis ja tõhus matemaatikaassistent. Kui teile antakse probleem, mis hõlmab põhiaritmeetikat, vastate õige tulemusega.`
1. Klõpsake **Loo** nuppu. Teade ilmub paremas alanurgas, kinnitades, et süsteemiprompti genereerimine on käimas. Kui prompti genereerimine on lõpule jõudnud, ilmub prompt **System prompt**-väljal **Agent (Prompt) Builder**-is.
1. Vaadake üle **System prompt** ja vajadusel muutke seda.

### -3- Looge MCP server

Nüüd, kui olete määratlenud oma agendi süsteemiprompti—juhendades selle käitumist ja vastuseid—on aeg varustada agent praktiliste võimekustega. Selles jaotises loote kalkulaatori MCP serveri tööriistadega, mis võimaldavad teostada liitmise, lahutamise, korrutamise ja jagamise arvutusi. See server võimaldab teie agendil teha reaalajas matemaatilisi tehteid vastuseks loomuliku keele promptidele.

!["Kuvapilt Kalkulaatori agendi liidese alumisest osast Visual Studio Code'i AI Toolkiti laienduses. Näidatud on laiendatavad menüüd “Tööriistad” ja “Struktureeritud väljund,” koos rippmenüüga “Vali väljundi formaat,” mis on seatud “tekst.” Paremal on nupp “+ MCP Server” Model Context Protocol serveri lisamiseks. Tööriistade jaotise kohal on pildiikooni kohatäide.](../../../../translated_images/et/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.png)

AI Toolkit on varustatud mallidega, mis lihtsustavad oma MCP serveri loomist. Kasutame kalkulaatori MCP serveri loomiseks Python-malli.

*NB*: AI Toolkit toetab praegu Pythonit ja TypeScripti.

1. **Agent (Prompt) Builder**-i **Tööriistade** jaotises klõpsake **+ MCP Server** nuppu. Laiendus käivitab seadistusviisardi **Command Palette** kaudu.
1. Valige **+ Lisa server**.
1. Valige **Loo uus MCP server**.
1. Valige malliks **python-weather**.
1. Valige **Vaikimisi kaust**, et salvestada MCP serveri mall.
1. Sisestage serveri nimeks: **Kalkulaator**
1. Avaneb uus Visual Studio Code'i aken. Valige **Jah, usaldan autoreid**.
1. Kasutades terminali (**Terminal** > **Uus terminal**), looge virtuaalne keskkond: `python -m venv .venv`
1. Kasutades terminali, aktiveerige virtuaalne keskkond:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Kasutades terminali, installige sõltuvused: `pip install -e .[dev]`
1. **Activity Bar**-i **Explorer** vaates laiendage **src** kataloogi ja valige **server.py**, et avada fail redaktoris.
1. Asendage **server.py** failis olev kood järgmisega ja salvestage:

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

### -4- Käivitage agent kalkulaatori MCP serveriga

Nüüd, kui teie agendil on tööriistad, on aeg neid kasutada! Selles jaotises esitate agendile promptid, et testida ja valideerida, kas agent kasutab kalkulaatori MCP serveri sobivat tööriista.

![Kuvapilt Kalkulaatori agendi liidesest Visual Studio Code'i AI Toolkiti laienduses. Vasakul paneelil, jaotises “Tööriistad,” on lisatud MCP server nimega local-server-calculator_server, mis näitab nelja saadaval olevat tööriista: liitmine, lahutamine, korrutamine ja jagamine. Märk näitab, et neli tööriista on aktiivsed. Allpool on kokkuvolditud “Struktureeritud väljund” ja sinine “Käivita” nupp. Paremal paneelil, jaotises “Mudelivastus,” kutsub agent esile korrutamise ja lahutamise tööriistad sisenditega {"a": 3, "b": 25} ja {"a": 75, "b": 20} vastavalt. Lõplik “Tööriistavastus” on näidatud kui 75.0. Allosas on nupp “Vaata koodi.”](../../../../translated_images/et/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.png)

Kalkulaatori MCP server käivitatakse teie kohalikus arendusmasinas **Agent Builder**-i kaudu MCP kliendina.

1. Vajutage `F5`, et alustada MCP serveri silumist. **Agent (Prompt) Builder** avaneb uues redaktori vahekaardil. Serveri olek on nähtav terminalis.
1. **Agent (Prompt) Builder**-i **Kasutajaprompti** väljal sisestage järgmine prompt: `Ostsin 3 eset hinnaga $25 tükk ja kasutasin $20 soodustust. Kui palju ma maksin?`
1. Klõpsake **Käivita** nuppu, et genereerida agendi vastus.
1. Vaadake üle agendi väljund. Mudel peaks järeldama, et maksite **$55**.
1. Siin on ülevaade, mis peaks toimuma:
    - Agent valib **korrutamise** ja **lahutamise** tööriistad, et aidata arvutuses.
    - Vastavad `a` ja `b` väärtused määratakse **korrutamise** tööriistale.
    - Vastavad `a` ja `b` väärtused määratakse **lahutamise** tööriistale.
    - Iga tööriista vastus esitatakse vastavas **Tööriistavastuses**.
    - Lõplik mudeli väljund esitatakse lõplikus **Mudelivastuses**.
1. Esitage täiendavaid prompti, et agenti edasi testida. Saate olemasolevat prompti **Kasutajaprompti** väljal muuta, klõpsates väljal ja asendades olemasoleva prompti.
1. Kui olete agendi testimise lõpetanud, saate serveri terminali kaudu peatada, sisestades **CTRL/CMD+C**, et väljuda.

## Ülesanne

Proovige lisada oma **server.py** faili täiendav tööriista kirje (nt tagastage arvu ruutjuur). Esitage täiendavaid prompti, mis nõuaksid agendilt teie uue tööriista (või olemasolevate tööriistade) kasutamist. Veenduge, et server taaskäivituks, et laadida äsja lisatud tööriistad.

## Lahendus

[Lahendus](./solution/README.md)

## Peamised õppetunnid

Selle peatüki peamised õppetunnid on järgmised:

- AI Toolkiti laiendus on suurepärane klient, mis võimaldab MCP serverite ja nende tööriistade kasutamist.
- MCP serveritele saab lisada uusi tööriistu, laiendades agendi võimekust vastavalt muutuvatele nõuetele.
- AI Toolkit sisaldab malle (nt Python MCP serveri mallid), et lihtsustada kohandatud tööriistade loomist.

## Täiendavad ressursid

- [AI Toolkiti dokumentatsioon](https://aka.ms/AIToolkit/doc)

## Mis edasi
- Järgmine: [Testimine ja silumine](../08-testing/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.