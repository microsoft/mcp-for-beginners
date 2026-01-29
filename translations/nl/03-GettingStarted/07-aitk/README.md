# Een server gebruiken vanuit de AI Toolkit-extensie voor Visual Studio Code

Wanneer je een AI-agent bouwt, gaat het niet alleen om het genereren van slimme antwoorden; het gaat er ook om je agent in staat te stellen actie te ondernemen. Dat is waar het Model Context Protocol (MCP) van pas komt. MCP maakt het eenvoudig voor agents om externe tools en diensten op een consistente manier te gebruiken. Zie het als het aansluiten van je agent op een gereedschapskist die het *echt* kan gebruiken.

Stel dat je een agent verbindt met je rekenmachine-MCP-server. Plotseling kan je agent wiskundige berekeningen uitvoeren door simpelweg een prompt te ontvangen zoals "Wat is 47 keer 89?"—zonder dat je logica hoeft te hardcoderen of aangepaste API's hoeft te bouwen.

## Overzicht

Deze les behandelt hoe je een rekenmachine-MCP-server kunt verbinden met een agent via de [AI Toolkit](https://aka.ms/AIToolkit)-extensie in Visual Studio Code, zodat je agent wiskundige bewerkingen zoals optellen, aftrekken, vermenigvuldigen en delen kan uitvoeren via natuurlijke taal.

AI Toolkit is een krachtige extensie voor Visual Studio Code die de ontwikkeling van agents vereenvoudigt. AI-ingenieurs kunnen eenvoudig AI-toepassingen bouwen door generatieve AI-modellen te ontwikkelen en te testen—lokaal of in de cloud. De extensie ondersteunt de meeste grote generatieve modellen die vandaag beschikbaar zijn.

*Opmerking*: De AI Toolkit ondersteunt momenteel Python en TypeScript.

## Leerdoelen

Aan het einde van deze les kun je:

- Een MCP-server gebruiken via de AI Toolkit.
- Een agentconfiguratie instellen zodat deze tools van de MCP-server kan ontdekken en gebruiken.
- MCP-tools gebruiken via natuurlijke taal.

## Aanpak

Hier is hoe we dit op hoofdlijnen aanpakken:

- Maak een agent en definieer zijn systeemprompt.
- Maak een MCP-server met rekenmachinetools.
- Verbind de Agent Builder met de MCP-server.
- Test de toolaanroepen van de agent via natuurlijke taal.

Geweldig, nu we de workflow begrijpen, laten we een AI-agent configureren om externe tools via MCP te gebruiken en zijn mogelijkheden te verbeteren!

## Vereisten

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit voor Visual Studio Code](https://aka.ms/AIToolkit)

## Oefening: Een server gebruiken

> [!WARNING]
> Opmerking voor macOS-gebruikers. We onderzoeken momenteel een probleem met de installatie van afhankelijkheden op macOS. Hierdoor kunnen macOS-gebruikers deze tutorial op dit moment niet voltooien. We zullen de instructies bijwerken zodra er een oplossing beschikbaar is. Bedankt voor je geduld en begrip!

In deze oefening bouw je een AI-agent, voer je deze uit en verbeter je deze met tools van een MCP-server binnen Visual Studio Code met behulp van de AI Toolkit.

### -0- Voorstap, voeg het OpenAI GPT-4o-model toe aan Mijn Modellen

De oefening maakt gebruik van het **GPT-4o**-model. Het model moet worden toegevoegd aan **Mijn Modellen** voordat je de agent maakt.

1. Open de **AI Toolkit**-extensie vanuit de **Activiteitenbalk**.
1. Selecteer in de sectie **Catalogus** de optie **Modellen** om de **Modelcatalogus** te openen. Het selecteren van **Modellen** opent de **Modelcatalogus** in een nieuw tabblad.
1. Voer in de zoekbalk van de **Modelcatalogus** **OpenAI GPT-4o** in.
1. Klik op **+ Toevoegen** om het model toe te voegen aan je lijst met **Mijn Modellen**. Zorg ervoor dat je het model selecteert dat **Gehost door GitHub** is.
1. Controleer in de **Activiteitenbalk** of het **OpenAI GPT-4o**-model in de lijst verschijnt.

### -1- Maak een agent

De **Agent (Prompt) Builder** stelt je in staat om je eigen AI-gestuurde agents te maken en aan te passen. In deze sectie maak je een nieuwe agent en wijs je een model toe om het gesprek aan te sturen.

1. Open de **AI Toolkit**-extensie vanuit de **Activiteitenbalk**.
1. Selecteer in de sectie **Tools** de optie **Agent (Prompt) Builder**. Het selecteren van **Agent (Prompt) Builder** opent de **Agent (Prompt) Builder** in een nieuw tabblad.
1. Klik op de knop **+ Nieuwe Agent**. De extensie start een configuratiewizard via de **Command Palette**.
1. Voer de naam **Rekenmachine Agent** in en druk op **Enter**.
1. Selecteer in de **Agent (Prompt) Builder** voor het veld **Model** het model **OpenAI GPT-4o (via GitHub)**.

### -2- Maak een systeemprompt voor de agent

Nu de agent is opgezet, is het tijd om zijn persoonlijkheid en doel te definiëren. In deze sectie gebruik je de functie **Systeemprompt genereren** om het beoogde gedrag van de agent te beschrijven—een rekenmachine-agent in dit geval—en laat je het model de systeemprompt voor je schrijven.

1. Klik in de sectie **Prompts** op de knop **Systeemprompt genereren**. Deze knop opent de prompt builder die AI gebruikt om een systeemprompt voor de agent te genereren.
1. Voer in het venster **Een prompt genereren** het volgende in: `Je bent een behulpzame en efficiënte wiskunde-assistent. Wanneer je een probleem krijgt dat basisrekenkunde omvat, geef je het juiste resultaat als antwoord.`
1. Klik op de knop **Genereren**. Een melding verschijnt rechtsonder in het scherm om te bevestigen dat de systeemprompt wordt gegenereerd. Zodra de prompt is gegenereerd, verschijnt deze in het veld **Systeemprompt** van de **Agent (Prompt) Builder**.
1. Controleer de **Systeemprompt** en pas deze indien nodig aan.

### -3- Maak een MCP-server

Nu je de systeemprompt van je agent hebt gedefinieerd—die zijn gedrag en reacties stuurt—is het tijd om de agent praktische mogelijkheden te geven. In deze sectie maak je een rekenmachine-MCP-server met tools om optel-, aftrek-, vermenigvuldigings- en delingsberekeningen uit te voeren. Deze server stelt je agent in staat om realtime wiskundige berekeningen uit te voeren als reactie op natuurlijke taalprompts.

De AI Toolkit is uitgerust met sjablonen om het maken van je eigen MCP-server te vergemakkelijken. We gebruiken het Python-sjabloon om de rekenmachine-MCP-server te maken.

*Opmerking*: De AI Toolkit ondersteunt momenteel Python en TypeScript.

1. Klik in de sectie **Tools** van de **Agent (Prompt) Builder** op de knop **+ MCP Server**. De extensie start een configuratiewizard via de **Command Palette**.
1. Selecteer **+ Server toevoegen**.
1. Selecteer **Maak een nieuwe MCP-server**.
1. Selecteer **python-weather** als sjabloon.
1. Selecteer **Standaardmap** om het MCP-server-sjabloon op te slaan.
1. Voer de volgende naam in voor de server: **Rekenmachine**.
1. Een nieuw Visual Studio Code-venster wordt geopend. Selecteer **Ja, ik vertrouw de auteurs**.
1. Gebruik de terminal (**Terminal** > **Nieuwe Terminal**) om een virtuele omgeving te maken: `python -m venv .venv`.
1. Activeer de virtuele omgeving via de terminal:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Installeer de afhankelijkheden via de terminal: `pip install -e .[dev]`.
1. Breid in de **Verkenner**-weergave van de **Activiteitenbalk** de map **src** uit en selecteer **server.py** om het bestand in de editor te openen.
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

### -4- Voer de agent uit met de rekenmachine-MCP-server

Nu je agent tools heeft, is het tijd om ze te gebruiken! In deze sectie voer je prompts in bij de agent om te testen en te valideren of de agent de juiste tool van de rekenmachine-MCP-server gebruikt.

1. Druk op `F5` om de MCP-server te debuggen. De **Agent (Prompt) Builder** wordt geopend in een nieuw tabblad. De status van de server is zichtbaar in de terminal.
1. Voer in het veld **Gebruikersprompt** van de **Agent (Prompt) Builder** de volgende prompt in: `Ik kocht 3 items van $25 elk en gebruikte vervolgens een korting van $20. Hoeveel heb ik betaald?`
1. Klik op de knop **Uitvoeren** om de reactie van de agent te genereren.
1. Controleer de uitvoer van de agent. Het model zou moeten concluderen dat je **$55** hebt betaald.
1. Hier is een overzicht van wat er zou moeten gebeuren:
    - De agent selecteert de tools **vermenigvuldigen** en **aftrekken** om te helpen bij de berekening.
    - De respectieve `a`- en `b`-waarden worden toegewezen voor de tool **vermenigvuldigen**.
    - De respectieve `a`- en `b`-waarden worden toegewezen voor de tool **aftrekken**.
    - De respons van elke tool wordt weergegeven in de respectieve **Tool Response**.
    - De uiteindelijke uitvoer van het model wordt weergegeven in de **Model Response**.
1. Voer extra prompts in om de agent verder te testen. Je kunt de bestaande prompt in het veld **Gebruikersprompt** wijzigen door in het veld te klikken en de bestaande prompt te vervangen.
1. Zodra je klaar bent met het testen van de agent, kun je de server stoppen via de **terminal** door **CTRL/CMD+C** in te voeren om te stoppen.

## Opdracht

Probeer een extra tool toe te voegen aan je **server.py**-bestand (bijvoorbeeld: de vierkantswortel van een getal retourneren). Voer extra prompts in die vereisen dat de agent je nieuwe tool (of bestaande tools) gebruikt. Zorg ervoor dat je de server opnieuw start om de nieuw toegevoegde tools te laden.

## Oplossing

[Oplossing](./solution/README.md)

## Belangrijkste inzichten

De belangrijkste inzichten uit dit hoofdstuk zijn de volgende:

- De AI Toolkit-extensie is een geweldige client waarmee je MCP-servers en hun tools kunt gebruiken.
- Je kunt nieuwe tools toevoegen aan MCP-servers, waardoor de mogelijkheden van de agent worden uitgebreid om aan veranderende eisen te voldoen.
- De AI Toolkit bevat sjablonen (bijvoorbeeld Python MCP-server-sjablonen) om het maken van aangepaste tools te vereenvoudigen.

## Aanvullende bronnen

- [AI Toolkit-documentatie](https://aka.ms/AIToolkit/doc)

## Wat nu?
- Volgende: [Testen & Debuggen](../08-testing/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.