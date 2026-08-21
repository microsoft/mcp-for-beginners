# Een server gebruiken vanuit de AI Toolkit-extensie voor Visual Studio Code

Wanneer je een AI-agent bouwt, gaat het niet alleen om het genereren van slimme antwoorden; het gaat er ook om dat je agent in staat is acties uit te voeren. Dat is waar het Model Context Protocol (MCP) om de hoek komt kijken. MCP maakt het agents gemakkelijk om op een consistente manier toegang te krijgen tot externe tools en diensten. Zie het als het aansluiten van je agent op een gereedschapskist die hij *echt* kan gebruiken.

Stel dat je een agent verbindt met je rekenmachine MCP-server. Plotseling kan je agent wiskundige bewerkingen uitvoeren door simpelweg een prompt te krijgen zoals “Wat is 47 keer 89?”—er is geen noodzaak meer om logica hard te coderen of aangepaste API’s te bouwen.

## Overzicht

Deze les behandelt hoe je een rekenmachine MCP-server verbindt met een agent via de [AI Toolkit](https://aka.ms/AIToolkit) extensie in Visual Studio Code, waarmee je agent wiskundige bewerkingen kan uitvoeren zoals optellen, aftrekken, vermenigvuldigen en delen via natuurlijke taal.

AI Toolkit is een krachtige extensie voor Visual Studio Code die de ontwikkeling van agents vereenvoudigt. AI Engineers kunnen eenvoudig AI-toepassingen bouwen door generatieve AI-modellen te ontwikkelen en te testen—lokaal of in de cloud. De extensie ondersteunt vrijwel alle grote generatieve modellen die tegenwoordig beschikbaar zijn.

*Opmerking*: De AI Toolkit ondersteunt momenteel Python en TypeScript.

## Leerdoelen

Aan het einde van deze les kun je:

- Een MCP-server gebruiken via de AI Toolkit.
- Een agentconfiguratie instellen zodat deze tools kan ontdekken en gebruiken die door de MCP-server worden aangeboden.
- MCP-tools gebruiken via natuurlijke taal.

## Aanpak

Dit is de aanpak op hoofdlijnen:

- Maak een agent aan en definieer zijn systeem prompt.
- Maak een MCP-server met rekenmachine tools.
- Verbind de Agent Builder met de MCP-server.
- Test de aanroep van de tools van de agent via natuurlijke taal.

Geweldig, nu we het proces begrijpen, laten we een AI-agent configureren die externe tools via MCP gebruikt, zodat zijn mogelijkheden worden uitgebreid!

## Vereisten

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit voor Visual Studio Code](https://aka.ms/AIToolkit)

## Oefening: Een server gebruiken

> [!WARNING]
> Opmerking voor macOS-gebruikers. We onderzoeken momenteel een probleem dat het installeren van dependencies op macOS beïnvloedt. Daardoor kunnen macOS-gebruikers deze tutorial op dit moment niet voltooien. We zullen de instructies bijwerken zodra er een oplossing beschikbaar is. Dank voor je geduld en begrip!

In deze oefening bouw, draai en verbeter je een AI-agent met tools van een MCP-server binnen Visual Studio Code met de AI Toolkit.

### -0- Pre-stap, voeg het OpenAI GPT-4o model toe aan Mijn Modellen

De oefening gebruikt het **GPT-4o** model. Het model moet aan **Mijn Modellen** worden toegevoegd voordat je de agent maakt.

![Screenshot van een modelselectie-interface in de AI Toolkit-extensie van Visual Studio Code. De koptekst luidt "Vind het juiste model voor je AI-oplossing" met een subtitel die gebruikers aanmoedigt om AI-modellen te ontdekken, testen en implementeren. Daaronder staan onder “Populaire Modellen” zes modelkaarten: DeepSeek-R1 (gehost op GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Klein, Snel) en DeepSeek-R1 (gehost op Ollama). Elke kaart bevat opties om het model “Toe te voegen” of “Te Proberen in Playground.](../../../../translated_images/nl/aitk-model-catalog.2acd38953bb9c119.webp)

1. Open de **AI Toolkit** extensie vanuit de **Activity Bar**.
1. Selecteer in de **Catalogus** sectie **Modellen** om de **Model Catalogus** te openen. Het selecteren van **Modellen** opent de **Model Catalogus** in een nieuw editor-tabblad.
1. Typ in de zoekbalk van de **Model Catalogus** **OpenAI GPT-4o**.
1. Klik op **+ Toevoegen** om het model toe te voegen aan je lijst **Mijn Modellen**. Zorg dat je het model kiest dat **gehost wordt door GitHub**.
1. Controleer in de **Activity Bar** of het **OpenAI GPT-4o** model in de lijst verschijnt.

### -1- Maak een agent aan

De **Agent (Prompt) Builder** stelt je in staat om je eigen door AI aangedreven agents te maken en aan te passen. In deze sectie maak je een nieuwe agent aan en wijs je een model toe om het gesprek aan te sturen.

![Screenshot van de "Calculator Agent" builder interface in de AI Toolkit extensie voor Visual Studio Code. In het linker paneel is het geselecteerde model "OpenAI GPT-4o (via GitHub)." Een systeem prompt luidt "Je bent een professor aan de universiteit die wiskunde geeft," en de gebruikersprompt zegt, "Leg me de Fourier-vergelijking uit in eenvoudige termen." Extra opties omvatten knoppen om tools toe te voegen, MCP Server in te schakelen, en gestructureerde output te selecteren. Onderaan is een blauwe “Run” knop. In het rechter paneel, onder "Begin met voorbeelden," staan drie voorbeeldagents: Web Developer (met MCP Server, Tweede-klasser vereenvoudiger, en Droomuitlegger, elk met korte beschrijvingen van hun functies.](../../../../translated_images/nl/aitk-agent-builder.901e3a2960c3e477.webp)

1. Open de **AI Toolkit** extensie vanuit de **Activity Bar**.
1. Selecteer in de **Tools** sectie **Agent (Prompt) Builder**. Dit opent de **Agent (Prompt) Builder** in een nieuw editor-tabblad.
1. Klik op de **+ Nieuwe Agent** knop. De extensie start een setup wizard via de **Command Palette**.
1. Voer de naam **Calculator Agent** in en druk op **Enter**.
1. Selecteer in de **Agent (Prompt) Builder**, bij het veld **Model**, het model **OpenAI GPT-4o (via GitHub)**.

### -2- Maak een systeem prompt voor de agent

Nu de agent gestructureerd is, is het tijd om zijn persoonlijkheid en doel te definiëren. In deze sectie gebruik je de functie **Genereer systeem prompt** om het beoogde gedrag van de agent te beschrijven—in dit geval een rekenmachine-agent—en laat je het model de systeem prompt voor je schrijven.

![Screenshot van de "Calculator Agent" interface in de AI Toolkit voor Visual Studio Code met een modal window open getiteld "Genereer een prompt." De modal legt uit dat een prompt template gegenereerd kan worden door basisgegevens te delen en bevat een tekstvak met het voorbeeld van de systeem prompt: "Je bent een behulpzame en efficiënte rekenhulp. Wanneer je een probleem krijgt met basale wiskunde, geef je het juiste resultaat." Onder het tekstvak zijn "Sluiten" en "Genereer" knoppen te zien. Op de achtergrond is een deel van de agentconfiguratie zichtbaar, inclusief het geselecteerde model "OpenAI GPT-4o (via GitHub)" en velden voor systeem- en gebruikersprompts.](../../../../translated_images/nl/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Klik in de **Prompts** sectie op de knop **Genereer systeem prompt**. Hiermee opent de prompt builder die AI gebruikt om een systeem prompt voor de agent te genereren.
1. Voer in het venster **Genereer een prompt** het volgende in: `Je bent een behulpzame en efficiënte rekenhulp. Wanneer je een probleem krijgt met basale wiskunde, geef je het juiste resultaat.`
1. Klik op de knop **Genereer**. Er verschijnt een notificatie rechtsonder dat de systeem prompt wordt gegenereerd. Zodra dit klaar is, verschijnt de prompt in het veld **Systeem prompt** van de **Agent (Prompt) Builder**.
1. Bekijk de **Systeem prompt** en pas deze aan indien nodig.

### -3- Maak een MCP-server

Nu je de systeem prompt van je agent hebt gedefinieerd, die zijn gedrag en antwoorden stuurt, is het tijd om je agent praktische mogelijkheden te geven. In deze sectie maak je een rekenmachine MCP-server met tools om optellen, aftrekken, vermenigvuldigen en delen uit te voeren. Deze server maakt het mogelijk dat je agent realtime wiskundige bewerkingen doet als reactie op natuurlijke taal prompts.

!["Screenshot van het onderste gedeelte van de Calculator Agent interface in de AI Toolkit extensie voor Visual Studio Code. Het toont uitklapbare menu's voor “Tools” en “Gestructureerde output,” samen met een dropdownmenu genaamd “Kies uitvoerformaat” ingesteld op “tekst.” Rechts is er een knop met de tekst “+ MCP Server” om een Model Context Protocol-server toe te voegen. Boven de Tools-sectie is een afbeelding icoon placeholder.](../../../../translated_images/nl/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit is voorzien van sjablonen om het gemakkelijk te maken je eigen MCP-server te maken. We gebruiken de Python-sjabloon voor het maken van de rekenmachine MCP-server.

*Opmerking*: De AI Toolkit ondersteunt momenteel Python en TypeScript.

1. Klik in de **Tools** sectie van de **Agent (Prompt) Builder** op de knop **+ MCP Server**. De extensie start een setup wizard via de **Command Palette**.
1. Selecteer **+ Server Toevoegen**.
1. Selecteer **Maak een nieuwe MCP Server**.
1. Selecteer **python-weather** als template.
1. Selecteer **Standaard map** om de MCP server template op te slaan.
1. Voer als naam voor de server in: **Calculator**
1. Er opent een nieuw Visual Studio Code-venster. Selecteer **Ja, ik vertrouw de auteurs**.
1. Maak met de terminal (**Terminal** > **Nieuwe Terminal**) een virtuele omgeving aan: `python -m venv .venv`
1. Activeer in de terminal de virtuele omgeving:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Installeer in de terminal de afhankelijkheden: `pip install -e .[dev]`
1. Open in de **Explorer** weergave van de **Activity Bar** de **src** directory en selecteer **server.py** om het bestand in de editor te openen.
1. Vervang de code in het bestand **server.py** door het volgende en sla op:

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

### -4- Draai de agent met de rekenmachine MCP-server

Nu je agent tools heeft, is het tijd om ze te gebruiken! In deze sectie dien je prompts in bij de agent om te testen en valideren of de agent de juiste tool van de rekenmachine MCP-server gebruikt.

![Screenshot van de Calculator Agent interface in de AI Toolkit extensie voor Visual Studio Code. In het linker paneel, onder “Tools,” is een MCP-server toegevoegd met naam local-server-calculator_server, waarop vier beschikbare tools zijn: add, subtract, multiply, en divide. Een badge toont dat vier tools actief zijn. Daaronder is een ingeklapt “Gestructureerde output” gedeelte en een blauwe “Run” knop. In het rechter paneel, onder “Model Response,” roept de agent de multiply en subtract tools aan met inputs {"a": 3, "b": 25} en {"a": 75, "b": 20} respectievelijk. De uiteindelijke “Tool Response” is 75.0. Onderaan is een “Bekijk code” knop zichtbaar.](../../../../translated_images/nl/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Je zult de rekenmachine MCP-server lokaal op je ontwikkelmachine draaien via de **Agent Builder** als MCP-client.

1. Druk op `F5` om te starten met debuggen van de MCP-server. De **Agent (Prompt) Builder** opent in een nieuw editor-tabblad. De status van de server is zichtbaar in de terminal.
1. Voer in het veld **Gebruikersprompt** van de **Agent (Prompt) Builder** de volgende prompt in: `Ik kocht 3 items van elk $25, en gebruikte daarna een korting van $20. Hoeveel betaalde ik?`
1. Klik op de **Run** knop om de reactie van de agent te genereren.
1. Bekijk de uitkomst van de agent. Het model zou moeten concluderen dat je **$55** hebt betaald.
1. Dit is een overzicht van wat er gebeurt:
    - De agent selecteert de **multiply** en **subtract** tools ter ondersteuning van de berekening.
    - De respectievelijke waarden van `a` en `b` worden aan de **multiply** tool toegewezen.
    - De respectievelijke waarden van `a` en `b` worden aan de **subtract** tool toegewezen.
    - De reacties van elke tool worden teruggegeven in respectievelijke **Tool Response**.
    - De uiteindelijke output van het model wordt getoond in de laatste **Model Response**.
1. Dien extra prompts in om de agent verder te testen. Je kunt de bestaande prompt aanpassen in het veld **Gebruikersprompt** door erin te klikken en de tekst te wijzigen.
1. Als je klaar bent met testen, kun je de server stoppen via de **terminal** door **CTRL/CMD+C** in te voeren om te stoppen.

## Opdracht

Probeer een extra tool toe te voegen in je **server.py** bestand (bijv. het wortel trekken van een getal). Dien extra prompts in die de agent dwingen om jouw nieuwe tool (of bestaande tools) te gebruiken. Vergeet niet de server te herstarten om nieuwe tools te laden.

## Oplossing

[Oplossing](./solution/README.md)

## Belangrijke punten

De belangrijkste punten uit dit hoofdstuk zijn de volgende:

- De AI Toolkit extensie is een prima client die je toelaat MCP Servers en hun tools te gebruiken.
- Je kunt nieuwe tools toevoegen aan MCP-servers, waardoor de mogelijkheden van de agent uitgebreid worden om aan nieuwe behoeften te voldoen.
- De AI Toolkit bevat sjablonen (bijv. Python MCP server sjablonen) om het maken van aangepaste tools te vereenvoudigen.

## Extra bronnen

- [AI Toolkit documentatie](https://aka.ms/AIToolkit/doc)

## Wat komt hierna
- Volgende: [Testen & Debuggen](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->