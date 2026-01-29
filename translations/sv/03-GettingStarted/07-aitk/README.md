# Konsumera en server från AI Toolkit-tillägget för Visual Studio Code

När du bygger en AI-agent handlar det inte bara om att generera smarta svar; det handlar också om att ge din agent förmågan att agera. Det är här Model Context Protocol (MCP) kommer in. MCP gör det enkelt för agenter att få tillgång till externa verktyg och tjänster på ett konsekvent sätt. Tänk på det som att koppla din agent till en verktygslåda som den faktiskt kan *använda*.

Låt oss säga att du ansluter en agent till din kalkylator-MCP-server. Plötsligt kan din agent utföra matematiska operationer bara genom att få en fråga som "Vad är 47 gånger 89?"—utan att behöva hårdkoda logik eller bygga anpassade API:er.

## Översikt

Den här lektionen täcker hur man ansluter en kalkylator-MCP-server till en agent med [AI Toolkit](https://aka.ms/AIToolkit)-tillägget i Visual Studio Code, vilket gör det möjligt för din agent att utföra matematiska operationer som addition, subtraktion, multiplikation och division via naturligt språk.

AI Toolkit är ett kraftfullt tillägg för Visual Studio Code som förenklar utvecklingen av agenter. AI-ingenjörer kan enkelt bygga AI-applikationer genom att utveckla och testa generativa AI-modeller—lokalt eller i molnet. Tillägget stöder de flesta större generativa modeller som finns tillgängliga idag.

*Obs*: AI Toolkit stöder för närvarande Python och TypeScript.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Konsumera en MCP-server via AI Toolkit.
- Konfigurera en agentkonfiguration för att göra det möjligt för den att upptäcka och använda verktyg som tillhandahålls av MCP-servern.
- Använda MCP-verktyg via naturligt språk.

## Tillvägagångssätt

Så här ska vi närma oss detta på en övergripande nivå:

- Skapa en agent och definiera dess systemprompt.
- Skapa en MCP-server med kalkylatorverktyg.
- Anslut Agent Builder till MCP-servern.
- Testa agentens användning av verktyg via naturligt språk.

Bra, nu när vi förstår flödet, låt oss konfigurera en AI-agent för att utnyttja externa verktyg via MCP och förbättra dess kapacitet!

## Förutsättningar

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit för Visual Studio Code](https://aka.ms/AIToolkit)

## Övning: Konsumera en server

> [!WARNING]
> Obs för macOS-användare. Vi undersöker för närvarande ett problem som påverkar installationen av beroenden på macOS. Som ett resultat kommer macOS-användare inte att kunna slutföra denna handledning just nu. Vi kommer att uppdatera instruktionerna så snart en lösning är tillgänglig. Tack för ert tålamod och förståelse!

I denna övning kommer du att bygga, köra och förbättra en AI-agent med verktyg från en MCP-server i Visual Studio Code med hjälp av AI Toolkit.

### -0- Förberedelse, lägg till OpenAI GPT-4o-modellen till Mina modeller

Övningen använder **GPT-4o**-modellen. Modellen bör läggas till i **Mina modeller** innan du skapar agenten.

1. Öppna **AI Toolkit**-tillägget från **Aktivitetsfältet**.
1. I **Katalog**-sektionen, välj **Modeller** för att öppna **Model Catalog**. När du väljer **Modeller** öppnas **Model Catalog** i en ny redigeringsflik.
1. I sökfältet för **Model Catalog**, skriv **OpenAI GPT-4o**.
1. Klicka på **+ Lägg till** för att lägga till modellen i din lista över **Mina modeller**. Se till att du har valt modellen som är **Hostad av GitHub**.
1. I **Aktivitetsfältet**, bekräfta att **OpenAI GPT-4o**-modellen visas i listan.

### -1- Skapa en agent

**Agent (Prompt) Builder** gör det möjligt för dig att skapa och anpassa dina egna AI-drivna agenter. I denna sektion kommer du att skapa en ny agent och tilldela en modell för att driva konversationen.

1. Öppna **AI Toolkit**-tillägget från **Aktivitetsfältet**.
1. I **Verktyg**-sektionen, välj **Agent (Prompt) Builder**. När du väljer **Agent (Prompt) Builder** öppnas **Agent (Prompt) Builder** i en ny redigeringsflik.
1. Klicka på **+ Ny agent**-knappen. Tillägget startar en installationsguide via **Kommandopaletten**.
1. Ange namnet **Kalkylatoragent** och tryck på **Enter**.
1. I **Agent (Prompt) Builder**, för fältet **Modell**, välj modellen **OpenAI GPT-4o (via GitHub)**.

### -2- Skapa en systemprompt för agenten

När agenten är skapad är det dags att definiera dess personlighet och syfte. I denna sektion kommer du att använda funktionen **Generera systemprompt** för att beskriva agentens avsedda beteende—i detta fall en kalkylatoragent—och låta modellen skriva systemprompten åt dig.

1. För sektionen **Prompter**, klicka på knappen **Generera systemprompt**. Denna knapp öppnar promptbyggaren som använder AI för att generera en systemprompt för agenten.
1. I fönstret **Generera en prompt**, ange följande: `Du är en hjälpsam och effektiv matematikassistent. När du får ett problem som involverar grundläggande aritmetik, svarar du med rätt resultat.`
1. Klicka på **Generera**-knappen. En notifikation kommer att visas i det nedre högra hörnet som bekräftar att systemprompten genereras. När promptgenereringen är klar kommer prompten att visas i fältet **Systemprompt** i **Agent (Prompt) Builder**.
1. Granska **Systemprompten** och ändra vid behov.

### -3- Skapa en MCP-server

Nu när du har definierat din agents systemprompt—som styr dess beteende och svar—är det dags att utrusta agenten med praktiska funktioner. I denna sektion kommer du att skapa en kalkylator-MCP-server med verktyg för att utföra addition, subtraktion, multiplikation och division. Denna server gör det möjligt för din agent att utföra matematiska operationer i realtid som svar på naturliga språkfrågor.

AI Toolkit är utrustat med mallar för att enkelt skapa din egen MCP-server. Vi kommer att använda Python-mallen för att skapa kalkylator-MCP-servern.

*Obs*: AI Toolkit stöder för närvarande Python och TypeScript.

1. I sektionen **Verktyg** i **Agent (Prompt) Builder**, klicka på knappen **+ MCP Server**. Tillägget startar en installationsguide via **Kommandopaletten**.
1. Välj **+ Lägg till server**.
1. Välj **Skapa en ny MCP-server**.
1. Välj **python-weather** som mall.
1. Välj **Standardmapp** för att spara MCP-servermallen.
1. Ange följande namn för servern: **Kalkylator**
1. Ett nytt Visual Studio Code-fönster öppnas. Välj **Ja, jag litar på författarna**.
1. Använd terminalen (**Terminal** > **Ny terminal**) för att skapa en virtuell miljö: `python -m venv .venv`
1. Använd terminalen för att aktivera den virtuella miljön:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Använd terminalen för att installera beroenden: `pip install -e .[dev]`
1. I **Utforskaren**-vyn i **Aktivitetsfältet**, expandera katalogen **src** och välj **server.py** för att öppna filen i redigeraren.
1. Ersätt koden i filen **server.py** med följande och spara:

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

### -4- Kör agenten med kalkylator-MCP-servern

Nu när din agent har verktyg är det dags att använda dem! I denna sektion kommer du att skicka frågor till agenten för att testa och validera om agenten använder rätt verktyg från kalkylator-MCP-servern.

Du kommer att köra kalkylator-MCP-servern på din lokala utvecklingsdator via **Agent Builder** som MCP-klient.

1. Tryck på `F5` för att starta felsökning av MCP-servern. **Agent (Prompt) Builder** öppnas i en ny redigeringsflik. Serverns status är synlig i terminalen.
1. I fältet **Användarprompt** i **Agent (Prompt) Builder**, ange följande fråga: `Jag köpte 3 varor som kostade $25 styck och använde sedan en rabatt på $20. Hur mycket betalade jag?`
1. Klicka på **Kör**-knappen för att generera agentens svar.
1. Granska agentens output. Modellen bör komma fram till att du betalade **$55**.
1. Här är en sammanfattning av vad som bör hända:
    - Agenten väljer verktygen **multiply** och **subtract** för att hjälpa till med beräkningen.
    - Respektive värden `a` och `b` tilldelas för verktyget **multiply**.
    - Respektive värden `a` och `b` tilldelas för verktyget **subtract**.
    - Svaret från varje verktyg tillhandahålls i respektive **Verktygssvar**.
    - Det slutliga svaret från modellen tillhandahålls i det slutliga **Modelsvar**.
1. Skicka ytterligare frågor för att testa agenten vidare. Du kan ändra den befintliga frågan i fältet **Användarprompt** genom att klicka i fältet och ersätta den befintliga frågan.
1. När du är klar med att testa agenten kan du stoppa servern via **terminalen** genom att ange **CTRL/CMD+C** för att avsluta.

## Uppgift

Försök att lägga till en ytterligare verktygsfunktion i din **server.py**-fil (t.ex. returnera kvadratroten av ett tal). Skicka ytterligare frågor som kräver att agenten använder ditt nya verktyg (eller befintliga verktyg). Se till att starta om servern för att ladda de nyss tillagda verktygen.

## Lösning

[Lösning](./solution/README.md)

## Viktiga lärdomar

Lärdomarna från detta kapitel är följande:

- AI Toolkit-tillägget är en utmärkt klient som låter dig konsumera MCP-servrar och deras verktyg.
- Du kan lägga till nya verktyg till MCP-servrar, vilket utökar agentens kapacitet för att möta föränderliga krav.
- AI Toolkit innehåller mallar (t.ex. Python MCP-servermallar) för att förenkla skapandet av anpassade verktyg.

## Ytterligare resurser

- [AI Toolkit-dokumentation](https://aka.ms/AIToolkit/doc)

## Vad händer härnäst
- Nästa: [Testning & Felsökning](../08-testing/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.