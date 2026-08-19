# Använda en server från AI Toolkit-tillägget för Visual Studio Code

När du bygger en AI-agent handlar det inte bara om att generera smarta svar; det handlar också om att ge din agent förmågan att agera. Det är här Model Context Protocol (MCP) kommer in. MCP gör det enkelt för agenter att få tillgång till externa verktyg och tjänster på ett konsekvent sätt. Tänk på det som att koppla in din agent i en verktygslåda som den *verkligen* kan använda.

Låt oss säga att du kopplar en agent till din kalkylator-MCP-server. Plötsligt kan din agent utföra matematiska operationer bara genom att få en uppmaning som "Vad är 47 gånger 89?"—ingen anledning att hårdkoda logik eller bygga anpassade API:er.

## Översikt

Denna lektion täcker hur du kopplar en kalkylator-MCP-server till en agent med [AI Toolkit](https://aka.ms/AIToolkit)-tillägget i Visual Studio Code, så att din agent kan utföra matematiska operationer som addition, subtraktion, multiplikation och division genom naturligt språk.

AI Toolkit är ett kraftfullt tillägg för Visual Studio Code som förenklar agentutveckling. AI-ingenjörer kan enkelt bygga AI-applikationer genom att utveckla och testa generativa AI-modeller—lokalt eller i molnet. Tillägget stödjer de flesta större generativa modeller som finns idag.

*Notera*: AI Toolkit stödjer för närvarande Python och TypeScript.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Använda en MCP-server via AI Toolkit.
- Konfigurera en agentkonfiguration så att den kan upptäcka och använda verktyg som tillhandahålls av MCP-servern.
- Använda MCP-verktyg via naturligt språk.

## Tillvägagångssätt

Så här behöver vi närma oss detta på en övergripande nivå:

- Skapa en agent och definiera dess systemprompt.
- Skapa en MCP-server med kalkylatorverktyg.
- Koppla Agent Builder till MCP-servern.
- Testa agentens verktygsanrop via naturligt språk.

Toppen, nu när vi förstår flödet, låt oss konfigurera en AI-agent för att använda externa verktyg via MCP och därmed förbättra dess kapabiliteter!

## Förutsättningar

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit för Visual Studio Code](https://aka.ms/AIToolkit)

## Övning: Använda en server

> [!WARNING]
> Notering för macOS-användare. Vi undersöker för närvarande ett problem som påverkar installationsberoenden på macOS. Som ett resultat kommer macOS-användare inte kunna slutföra denna handledning för närvarande. Vi uppdaterar instruktionerna så snart en lösning finns tillgänglig. Tack för ditt tålamod och förståelse!

I denna övning kommer du att bygga, köra och förbättra en AI-agent med verktyg från en MCP-server inuti Visual Studio Code med hjälp av AI Toolkit.

### -0- Försteg, lägg till OpenAI GPT-4o-modellen till Mina Modeller

Övningen använder **GPT-4o**-modellen. Modellen bör läggas till under **Mina Modeller** innan du skapar agenten.

![Screenshot of a model selection interface in Visual Studio Code's AI Toolkit extension. The heading reads "Find the right model for your AI Solution" with a subtitle encouraging users to discover, test, and deploy AI models. Below, under “Popular Models,” six model cards are displayed: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card includes options to “Add” the model or “Try in Playground](../../../../translated_images/sv/aitk-model-catalog.2acd38953bb9c119.webp)

1. Öppna **AI Toolkit**-tillägget från **Aktivitetsfältet**.
1. I avsnittet **Katalog**, välj **Modeller** för att öppna **Modellkatalogen**. Att välja **Modeller** öppnar **Modellkatalogen** i en ny flik i editorn.
1. I sökfältet i **Modellkatalogen**, skriv **OpenAI GPT-4o**.
1. Klicka på **+ Lägg till** för att lägga till modellen i din lista **Mina Modeller**. Se till att du har valt modellen som är **Hostad av GitHub**.
1. I **Aktivitetsfältet**, bekräfta att modellen **OpenAI GPT-4o** syns i listan.

### -1- Skapa en agent

**Agent (Prompt)-byggaren** låter dig skapa och anpassa dina egna AI-drivna agenter. I detta avsnitt skapar du en ny agent och tilldelar en modell för att driva samtalet.

![Screenshot of the "Calculator Agent" builder interface in the AI Toolkit extension for Visual Studio Code. On the left panel, the model selected is "OpenAI GPT-4o (via GitHub)." A system prompt reads "You are a professor in university teaching math," and the user prompt says, "Explain to me the Fourier equation in simple terms." Additional options include buttons for adding tools, enabling MCP Server, and selecting structured output. A blue “Run” button is at the bottom. On the right panel, under "Get Started with Examples," three sample agents are listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with brief descriptions of their functions.](../../../../translated_images/sv/aitk-agent-builder.901e3a2960c3e477.webp)

1. Öppna **AI Toolkit**-tillägget från **Aktivitetsfältet**.
1. I avsnittet **Verktyg**, välj **Agent (Prompt) Builder**. Att välja **Agent (Prompt) Builder** öppnar **Agent (Prompt) Builder** i en ny editorflik.
1. Klicka på **+ Ny Agent**-knappen. Tillägget startar en installationsguide via **Kommandopaletten**.
1. Ange namnet **Calculator Agent** och tryck på **Enter**.
1. I **Agent (Prompt) Builder**, för fältet **Modell**, välj modellen **OpenAI GPT-4o (via GitHub)**.

### -2- Skapa en systemprompt för agenten

När agenten är upprättad är det dags att definiera dess personlighet och syfte. I detta avsnitt kommer du att använda funktionen **Generera systemprompt** för att beskriva agentens avsedda beteende—i detta fall en kalkylatoragent—och låta modellen skriva systemprompten åt dig.

![Screenshot of the "Calculator Agent" interface in the AI Toolkit for Visual Studio Code with a modal window open titled "Generate a prompt." The modal explains that a prompt template can be generated by sharing basic details and includes a text box with the sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box are "Close" and "Generate" buttons. In the background, part of the agent configuration is visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](../../../../translated_images/sv/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. För avsnittet **Prompter**, klicka på **Generera systemprompt**-knappen. Den här knappen öppnar promptbyggaren som använder AI för att generera en systemprompt för agenten.
1. I fönstret **Generera en prompt**, skriv in följande: `Du är en hjälpsam och effektiv matteassistent. När du får ett problem som involverar grundläggande aritmetik, svarar du med rätt resultat.`
1. Klicka på **Generera**-knappen. En notifiering visas nere till höger som bekräftar att systemprompten genereras. När promptgenereringen är klar visas prompten i fältet **Systemprompt** i **Agent (Prompt) Builder**.
1. Granska **Systemprompt** och ändra vid behov.

### -3- Skapa en MCP-server

Nu när du har definierat agentens systemprompt—som vägleder dess beteende och svar—är det dags att utrusta agenten med praktiska möjligheter. I detta avsnitt kommer du att skapa en kalkylator-MCP-server med verktyg för att utföra addition, subtraktion, multiplikation och division. Denna server gör det möjligt för din agent att utföra matematiska operationer i realtid som svar på naturliga språk.

!["Screenshot of the lower section of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. It shows expandable menus for “Tools” and “Structure output,” along with a dropdown menu labeled “Choose output format” set to “text.” To the right, there is a button labeled “+ MCP Server” for adding a Model Context Protocol server. An image icon placeholder is shown above the Tools section.](../../../../translated_images/sv/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit är utrustat med mallar för att enkelt skapa egna MCP-servrar. Vi kommer att använda Python-mallen för att skapa kalkylator-MCP-servern.

*Notera*: AI Toolkit stödjer för närvarande Python och TypeScript.

1. I **Verktyg**-sektionen i **Agent (Prompt) Builder**, klicka på **+ MCP Server**-knappen. Tillägget startar en installationsguide via **Kommandopaletten**.
1. Välj **+ Lägg till server**.
1. Välj **Skapa en ny MCP-server**.
1. Välj mallen **python-weather**.
1. Välj **Standardmapp** för att spara MCP-servermallen.
1. Ange följande namn för servern: **Calculator**
1. Ett nytt Visual Studio Code-fönster öppnas. Välj **Ja, jag litar på författarna**.
1. Använd terminalen (**Terminal** > **Ny terminal**) för att skapa en virtuell miljö: `python -m venv .venv`
1. Använd terminalen för att aktivera den virtuella miljön:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Använd terminalen för att installera beroenden: `pip install -e .[dev]`
1. I **Utforskaren** i **Aktivitetsfältet**, expandera katalogen **src** och välj **server.py** för att öppna filen i editorn.
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

Nu när din agent har verktyg är det dags att använda dem! I detta avsnitt kommer du att skicka prompts till agenten för att testa och verifiera om agenten använder rätt verktyg från kalkylator-MCP-servern.

![Screenshot of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. On the left panel, under “Tools,” an MCP server named local-server-calculator_server is added, showing four available tools: add, subtract, multiply, and divide. A badge shows that four tools are active. Below is a collapsed “Structure output” section and a blue “Run” button. On the right panel, under “Model Response,” the agent invokes the multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. The final “Tool Response” is shown as 75.0. A “View Code” button appears at the bottom.](../../../../translated_images/sv/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Du kommer att köra kalkylator-MCP-servern på din lokala utvecklingsmaskin via **Agent Builder** som MCP-klient.

1. Tryck på `F5` för att starta felsökning av MCP-servern. **Agent (Prompt) Builder** öppnas i en ny editorflik. Serverns status visas i terminalen.
1. I fältet **Användarprompt** i **Agent (Prompt) Builder**, skriv följande prompt: `Jag köpte 3 artiklar som kostar 25 dollar styck, och använde sedan en rabatt på 20 dollar. Hur mycket betalade jag?`
1. Klicka på **Kör**-knappen för att generera agentens svar.
1. Granska agentens output. Modellen bör dra slutsatsen att du betalade **55 dollar**.
1. Här är en genomgång av vad som ska hända:
    - Agenten väljer verktygen **multiplicera** och **subtrahera** för att hjälpa till med beräkningen.
    - Respektive värden `a` och `b` tilldelas för verktyget **multiplicera**.
    - Respektive värden `a` och `b` tilldelas för verktyget **subtrahera**.
    - Svaren från varje verktyg returneras i respektive **Verktygsvar**.
    - Den slutliga outputen från modellen visas i den slutgiltiga **Modellsvar**.
1. Skicka fler prompts för att testa agenten ytterligare. Du kan ändra den befintliga prompten i fältet **Användarprompt** genom att klicka i fältet och ersätta den befintliga prompten.
1. När du är klar med att testa agenten kan du stoppa servern via **terminalen** genom att trycka på **CTRL/CMD+C** för att avsluta.

## Uppgift

Försök att lägga till ett extra verktygsbeskrivning i din fil **server.py** (t.ex. returnera kvadratroten av ett tal). Skicka fler prompts som kräver att agenten använder ditt nya verktyg (eller befintliga verktyg). Kom ihåg att starta om servern för att ladda nyss tillagda verktyg.

## Lösning

[Lösning](./solution/README.md)

## Viktiga insikter

Följande är de viktigaste insikterna från detta kapitel:

- AI Toolkit-tillägget är en utmärkt klient som låter dig använda MCP-servrar och deras verktyg.
- Du kan lägga till nya verktyg till MCP-servrar, vilket utökar agentens kapabiliteter för att möta förändrade krav.
- AI Toolkit inkluderar mallar (t.ex. Python MCP-servermallar) för att förenkla skapandet av anpassade verktyg.

## Ytterligare resurser

- [AI Toolkit-dokumentation](https://aka.ms/AIToolkit/doc)

## Vad som kommer härnäst
- Nästa: [Testning & Felsökning](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->