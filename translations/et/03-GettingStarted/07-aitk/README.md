# Serveri kasutamine AI Toolkit laiendusest Visual Studio Code jaoks

Kui ehitate tehisintellekti agendi, pole asi ainult nutikate vastuste genereerimises; oluline on anda agentidele ka võime tegutseda. Just siin tuleb mängu Model Context Protocol (MCP). MCP teeb lihtsaks agentide ligipääsu välistele tööriistadele ja teenustele ühtsel viisil. Mõelge sellele kui agenti ühendamine tööriistakasti, mida ta *tõesti* kasutada saab.

Oletame, et ühendate agendi kalkulaatori MCP serveriga. Äkitselt saab teie agent teha matemaatilisi operatsioone lihtsalt küsides näiteks “Mis on 47 korda 89?” — pole vaja keerulist loogikat kodeerida ega luua kohandatud API-sid.

## Ülevaade

See õppetund käsitleb, kuidas ühendada kalkulaatori MCP server agentiga, kasutades Visual Studio Code'is [AI Toolkit](https://aka.ms/AIToolkit) laiendust, võimaldades agendil läbi loomuliku keele teostada liitmist, lahutamist, korrutamist ja jagamist.

AI Toolkit on võimas Visual Studio Code'i laiendus, mis lihtsustab agentide arendamist. Tehisintellekti insenerid saavad hõlpsalt arendada ja testida generatiivseid AI mudeleid nii lokaalselt kui pilves. Laiendus toetab enamikku tänapäeval saadaolevaid suurimaid generatiivseid mudeleid.

*Märkus*: AI Toolkit toetab praegu Pythoni ja TypeScripti.

## Õpieesmärgid

Selle õppetunni lõpuks oskate:

- Kasutada MCP serverit AI Toolkit'i kaudu.
- Konfigureerida agendi seadistus selliselt, et see oskaks MCP serveri tööriistu avastada ja kasutada.
- Kasutada MCP tööriistu loomuliku keele abil.

## Lähenemine

Siin on kõrgetasemeline plaan:

- Luua agent ja määratleda tema süsteemipäring.
- Luua MCP server kalkulaatori tööriistadega.
- Ühenduda Agent Builderiga MCP serveri külge.
- Testida agendi tööriistade kutsumist loomuliku keele abil.

Väga hästi, nüüd kui voog on selge, seadistame AI agendi, et ta kasutaks väliseid tööriistu MCP kaudu ja tõstaks oma võimekust!

## Eeltingimused

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit Visual Studio Code jaoks](https://aka.ms/AIToolkit)

## Harjutus: Serveri kasutamine

> [!WARNING]
> Märkus macOS kasutajatele. Hetkel uurime macOS-il sõltuvuste paigaldamise probleemi. Seetõttu ei saa macOS kasutajad seda juhendit praegu lõpule viia. Täiendame juhiseid niipea, kui lahendus on olemas. Täname kannatlikkuse ja mõistva suhtumise eest!

Selles harjutuses ehitate, käivitate ja täiustate AI agendi MCP serveri tööriistadega Visual Studio Code'is, kasutades AI Toolkit'i.

### -0- Eeltöö: lisage OpenAI GPT-4o mudel My Models sektsiooni

Harjutus kasutab **GPT-4o** mudelit. Mudel tuleks lisada enne agendi loomist sektsiooni **My Models**.

![Kuvatõmmis mudelivaliku liidesest Visual Studio Code'i AI Toolkit laienduses. Pealkirjas on "Leia oma AI lahendusele sobiv mudel" ja alapealkirjas julgustatakse avastama, testima ja juurutama AI mudeleid. All “Popular Models” rubriigis on kuus mudelikaarte: DeepSeek-R1 (GitHub-hostitud), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - väike, kiire) ja DeepSeek-R1 (Ollama-hostitud). Iga kaart sisaldab valikuid “Lisa” või “Proovi mänguväljakul”.](../../../../translated_images/et/aitk-model-catalog.2acd38953bb9c119.webp)

1. Ava **AI Toolkit** laiendus **Activity Bar**'st.
1. Osas **Catalog** vali **Models**, et avada **Model Catalog**. Mudelite valimine avab uue editori vahekaardil **Model Catalog**.
1. Sisesta otsinguribale **OpenAI GPT-4o**.
1. Klõpsa **+ Add**, et lisada mudel oma **My Models** nimekirja. Veendu, et valitud mudel on **GitHub-hostitud**.
1. Kontrolli, et mudel **OpenAI GPT-4o** kuvatakse **Activity Bar'i** nimekirjas.

### -1- Agent looja

**Agent (Prompt) Builder** võimaldab sul luua ja kohandada AI-agente. Selles osas lood uue agendi ja määrad sellele mudeli, mis juhib vestlust.

![Kuvatõmmis "Calculator Agent" liidesest AI Toolkit laienduses Visual Studio Code'is. Vasakul valitud mudel on "OpenAI GPT-4o (via GitHub)." Süsteemipäringuks on "Oled ülikooli matemaatikaprofessor" ja kasutaja päringuks "Selgita mulle Fourier võrrandit lihtsate sõnadega." Lisavõimalused sisaldavad nuppe tööriistade lisamiseks, MCP serveri lubamiseks ja struktureeritud väljundi valimiseks. Alumine sinine nupp on “Run.” Paremal on "Get Started with Examples" sektsioonis kolm näidisagenti: Veebiarendaja (MCP Server, teise klassi lihtsustaja ja unistuste tõlgendaja), igaühel lühikirjeldus funktsioonidest.](../../../../translated_images/et/aitk-agent-builder.901e3a2960c3e477.webp)

1. Ava **AI Toolkit** laiendus **Activity Bar** kaudu.
1. Osas **Tools** vali **Agent (Prompt) Builder**. Valik avab uues editori vahekaardis **Agent (Prompt) Builder**.
1. Klõpsa nuppu **+ New Agent**. Laiendus avab seadistusviisardi **Command Palette** kaudu.
1. Sisesta nimi **Calculator Agent** ja vajuta **Enter**.
1. **Agent (Prompt) Builder** lahtris **Model** vali mudeliks **OpenAI GPT-4o (via GitHub)**.

### -2- Loo agendile süsteemipäring

Kui agent on loodud, on aeg määratleda tema iseloom ja eesmärk. Selles osas kasutad funktsiooni **Generate system prompt**, et kirjeldada agendi käitumist—sel juhul kalkulaatori agenti—ja mudel genereerib süsteemipäringu sinu eest.

![Kuvatõmmis "Calculator Agent" liidesest AI Toolkitis Visual Studio Code'is, kus avaneb modalaken pealkirjaga "Generate a prompt." Modalaken selgitab, et päringu mall genereeritakse põhiteadete jagamisega ja sisaldab teksti sisestusvälja näidis süsteemipäringuga: "Oled abivalmis ja tõhus matemaatika assistent. Kui sulle antakse probleem põhilise aritmeetika kohta, vastad õige tulemusega." All on nupud "Close" ja "Generate." Taustal on nähtav osa agendi seadistusest koos valitud mudeliga "OpenAI GPT-4o (via GitHub)" ning lahtrid süsteemipäringu ja kasutaja päringu jaoks.](../../../../translated_images/et/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Sektsioonis **Prompts** klõpsa nuppu **Generate system prompt**. See avab päringu koostaja, mis kasutab AI-d süsteemipäringu genereerimiseks agenti jaoks.
1. Kõneaknas **Generate a prompt** sisesta järgnev: `Oled abivalmis ja tõhus matemaatika assistent. Kui sulle antakse probleem põhilise aritmeetika kohta, vastad õige tulemusega.`
1. Klõpsa nuppu **Generate**. Alumises paremas nurgas kuvatakse teavitus, et süsteemipäringu genereerimine on alanud. Kui genereerimine lõpeb, kuvatakse päring väljal **System prompt** **Agent (Prompt) Builderis**.
1. Vaata üle **System prompt** ja vajadusel muuda.

### -3- Loo MCP server

Kui oled agendi süsteemipäringu määratlenud—mida juhib tema käitumine ja vastused—on aeg anda agentidele praktilised võimed. Selles osas lood kalkulaatori MCP serveri, mille tööriistad teostavad liitmist, lahutamist, korrutamist ja jagamist. See server võimaldab agendil teha reaalajas matemaatilisi operatsioone loomulike keelepäringute põhjal.

![Kuvatõmmis Kalkulaatori Agendi liidese alumisest osast AI Toolkit laienduses Visual Studio Code'is. Kuvatud on laiendatavad menüüd “Tools” ja “Structure output,” samuti rippmenüü “Choose output format” väärtusega “text.” Paremal on nupp “+ MCP Server” Model Context Protocoli serveri lisamiseks. Üles on pildikoha ikoon.](../../../../translated_images/et/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit sisaldab malle, mis lihtsustavad oma MCP serveri loomist. Siin kasutame kalkulaatori MCP serveri loomisel Python malle.

*Märkus*: AI Toolkit toetab praegu Pythoni ja TypeScripti.

1. Sektsioonis **Tools** **Agent (Prompt) Builder** aknas klõpsa nuppu **+ MCP Server**. Laiendus käivitab seadistusviisardi **Command Palette** kaudu.
1. Vali **+ Add Server**.
1. Vali **Create a New MCP Server**.
1. Vali malliks **python-weather**.
1. Vali salvestamiseks **Default folder**.
1. Sisesta serveri nimeks: **Calculator**
1. Avaneb uus Visual Studio Code'i aken. Vali **Yes, I trust the authors**.
1. Terminalis (**Terminal** > **New Terminal**) loo virtuaalne keskkond: `python -m venv .venv`
1. Terminalis aktiveeri virtuaalne keskkond:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Terminalis paigalda sõltuvused: `pip install -e .[dev]`
1. **Exploreri** vaates **Activity Bar'is** ava kataloog **src** ja vali fail **server.py**, et faili editoris avada.
1. Asenda faili **server.py** sisu järgnevaga ja salvesta:

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

### -4- Käivita agent kalkulaatori MCP serveriga

Nüüd, kui agendil on tööriistad, on aeg neid kasutada! Selles osas saad agendile esitada päringuid, et testida ja kontrollida, kas agent kasutab kalkulaatori MCP serveri sobivat tööriista.

![Kuvatõmmis Kalkulaatori Agendi liidesest AI Toolkit laienduses Visual Studio Code'is. Vasakul paneelil on “Tools” all lisatud MCP server nimega local-server-calculator_server, mis kuvab neli saadaolevat tööriista: add, subtract, multiply ja divide. Märge näitab, et neli tööriista on aktiivsed. All on kokkupandud sektsioon “Structure output” ja sinine nupp “Run.” Paremal paneelil “Model Response” osas kutsub agent korrutamise ja lahutamise tööriistu sisenditega {"a": 3, "b": 25} ja {"a": 75, "b": 20}. Lõplik “Tool Response” on 75.0. All on nupp “View Code.”](../../../../translated_images/et/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Sa jooksutad kalkulaatori MCP serverit oma lokaalses arenduskeskkonnas läbi **Agent Builderi** MCP kliendina.

1. Vajuta `F5`, et alustada MCP serveri silumist. **Agent (Prompt) Builder** avaneb uues editori vahekaardis. Serveri olek on nähtav terminalis.
1. Sisesta **User prompt** väljale **Agent (Prompt) Builderis** järgmine päring: `Ma ostsin 3 eset hinnaga 25 dollarit tükk ja kasutasin 20 dollari suurust allahindlust. Kui palju ma maksin?`
1. Klõpsa nuppu **Run**, et genereerida agendi vastus.
1. Vaata üle agendi väljund. Mudel peaks jõudma järeldusele, et maksisite **55 dollarit**.
1. Tööprotsessi jagunemine peaks olema järgmine:
    - Agent valib arvutamiseks tööriistad **multiply** ja **subtract**.
    - Tööriistale **multiply** määratakse vastavad väärtused `a` ja `b`.
    - Tööriistale **subtract** määratakse vastavad väärtused `a` ja `b`.
    - Mõlema tööriista vastused kuvatakse välja **Tool Response** all.
    - Mudeli lõplik väljund kuvatakse välja **Model Response** all.
1. Esita agendile täiendavaid päringuid testi laiendamiseks. Sa võid muuta olemasolevat päringut **User prompt** väljal, klõpsates sinna ja asendades tekst.
1. Kui testimine on tehtud, saad serveri terminalis peatada vajutades **CTRL/CMD+C**.

## Kodutöö

Proovi lisada lisatööriist oma faili **server.py** (näiteks ruutjuure leidmine). Esita agendile päringuid, mis nõuavad sinu uue või olemasolevate tööriistade kasutamist. Ära unusta server uuesti käivitada uus lisatud tööriistade laadimiseks.

## Lahendus

[Lahendus](./solution/README.md)

## Peamised mõtted

Selle peatüki peamised mõtted on järgmised:

- AI Toolkit laiendus on suurepärane klient, mis võimaldab MCP servereid ja nende tööriistu kasutada.
- Sa saad MCP serveritele lisada uusi tööriistu, laiendades agendi võimekust vastavalt muutuvatele nõudmistele.
- AI Toolkit sisaldab malle (näiteks Python MCP serveri malle), mis lihtsustavad kohandatud tööriistade loomist.

## Lisamaterjalid

- [AI Toolkit dokumentatsioon](https://aka.ms/AIToolkit/doc)

## Mis järgnevalt
- Järgmine: [Testimine ja silumine](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->