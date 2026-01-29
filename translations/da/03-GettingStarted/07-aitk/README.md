# Forbrug af en server fra AI Toolkit-udvidelsen til Visual Studio Code

Når du bygger en AI-agent, handler det ikke kun om at generere smarte svar; det handler også om at give din agent evnen til at handle. Det er her, Model Context Protocol (MCP) kommer ind i billedet. MCP gør det nemt for agenter at få adgang til eksterne værktøjer og tjenester på en ensartet måde. Tænk på det som at tilslutte din agent til en værktøjskasse, den rent faktisk kan *bruge*.

Lad os sige, at du forbinder en agent til din MCP-server for en lommeregner. Pludselig kan din agent udføre matematiske operationer blot ved at modtage en prompt som "Hvad er 47 gange 89?"—uden at skulle hardkode logik eller bygge brugerdefinerede API'er.

## Oversigt

Denne lektion dækker, hvordan man forbinder en MCP-server for en lommeregner til en agent med [AI Toolkit](https://aka.ms/AIToolkit)-udvidelsen i Visual Studio Code, så din agent kan udføre matematiske operationer som addition, subtraktion, multiplikation og division via naturligt sprog.

AI Toolkit er en kraftfuld udvidelse til Visual Studio Code, der gør udviklingen af agenter mere strømlinet. AI-ingeniører kan nemt bygge AI-applikationer ved at udvikle og teste generative AI-modeller—lokalt eller i skyen. Udvidelsen understøtter de fleste større generative modeller, der er tilgængelige i dag.

*Bemærk*: AI Toolkit understøtter i øjeblikket Python og TypeScript.

## Læringsmål

Ved afslutningen af denne lektion vil du være i stand til at:

- Forbruge en MCP-server via AI Toolkit.
- Konfigurere en agentkonfiguration, så den kan opdage og bruge værktøjer leveret af MCP-serveren.
- Bruge MCP-værktøjer via naturligt sprog.

## Fremgangsmåde

Her er den overordnede fremgangsmåde:

- Opret en agent og definer dens systemprompt.
- Opret en MCP-server med værktøjer til lommeregneren.
- Forbind Agent Builder til MCP-serveren.
- Test agentens brug af værktøjer via naturligt sprog.

Fremragende, nu hvor vi forstår processen, lad os konfigurere en AI-agent til at udnytte eksterne værktøjer via MCP og forbedre dens evner!

## Forudsætninger

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit til Visual Studio Code](https://aka.ms/AIToolkit)

## Øvelse: Forbrug af en server

> [!WARNING]
> Bemærk til macOS-brugere. Vi undersøger i øjeblikket et problem, der påvirker installationen af afhængigheder på macOS. Som følge heraf vil macOS-brugere ikke kunne gennemføre denne vejledning på nuværende tidspunkt. Vi opdaterer instruktionerne, så snart der er en løsning. Tak for din tålmodighed og forståelse!

I denne øvelse vil du bygge, køre og forbedre en AI-agent med værktøjer fra en MCP-server i Visual Studio Code ved hjælp af AI Toolkit.

### -0- Forberedelse: Tilføj OpenAI GPT-4o-modellen til Mine Modeller

Øvelsen bruger **GPT-4o**-modellen. Modellen skal tilføjes til **Mine Modeller**, før du opretter agenten.

1. Åbn **AI Toolkit**-udvidelsen fra **Aktivitetslinjen**.
1. I sektionen **Katalog**, vælg **Modeller** for at åbne **Modelkataloget**. Når du vælger **Modeller**, åbnes **Modelkataloget** i en ny redigeringstab.
1. I søgefeltet i **Modelkataloget**, indtast **OpenAI GPT-4o**.
1. Klik på **+ Tilføj** for at tilføje modellen til din liste over **Mine Modeller**. Sørg for, at du har valgt modellen, der er **hostet af GitHub**.
1. Bekræft i **Aktivitetslinjen**, at **OpenAI GPT-4o**-modellen vises på listen.

### -1- Opret en agent

**Agent (Prompt) Builder** giver dig mulighed for at oprette og tilpasse dine egne AI-drevne agenter. I denne sektion vil du oprette en ny agent og tildele en model til at drive samtalen.

1. Åbn **AI Toolkit**-udvidelsen fra **Aktivitetslinjen**.
1. I sektionen **Værktøjer**, vælg **Agent (Prompt) Builder**. Når du vælger **Agent (Prompt) Builder**, åbnes den i en ny redigeringstab.
1. Klik på knappen **+ Ny Agent**. Udvidelsen starter en opsætningsguide via **Kommando Paletten**.
1. Indtast navnet **Lommeregner Agent** og tryk på **Enter**.
1. I **Agent (Prompt) Builder**, vælg modellen **OpenAI GPT-4o (via GitHub)** i feltet **Model**.

### -2- Opret en systemprompt til agenten

Når agenten er oprettet, er det tid til at definere dens personlighed og formål. I denne sektion vil du bruge funktionen **Generer systemprompt** til at beskrive agentens tilsigtede adfærd—i dette tilfælde en lommeregneragent—og lade modellen skrive systemprompten for dig.

1. I sektionen **Prompter**, klik på knappen **Generer systemprompt**. Denne knap åbner promptbyggeren, som bruger AI til at generere en systemprompt til agenten.
1. I vinduet **Generer en prompt**, indtast følgende: `Du er en hjælpsom og effektiv matematikassistent. Når du får et problem, der involverer grundlæggende aritmetik, svarer du med det korrekte resultat.`
1. Klik på knappen **Generer**. En notifikation vil vises i nederste højre hjørne, der bekræfter, at systemprompten genereres. Når prompten er færdig, vises den i feltet **Systemprompt** i **Agent (Prompt) Builder**.
1. Gennemgå **Systemprompten** og tilpas den, hvis nødvendigt.

### -3- Opret en MCP-server

Nu hvor du har defineret din agents systemprompt—som guider dens adfærd og svar—er det tid til at udstyre agenten med praktiske evner. I denne sektion vil du oprette en MCP-server for en lommeregner med værktøjer til at udføre addition, subtraktion, multiplikation og division. Denne server vil gøre det muligt for din agent at udføre matematiske operationer i realtid som svar på naturlige sprogprompter.

AI Toolkit er udstyret med skabeloner, der gør det nemt at oprette dine egne MCP-servere. Vi bruger Python-skabelonen til at oprette MCP-serveren for lommeregneren.

*Bemærk*: AI Toolkit understøtter i øjeblikket Python og TypeScript.

1. I sektionen **Værktøjer** i **Agent (Prompt) Builder**, klik på knappen **+ MCP Server**. Udvidelsen starter en opsætningsguide via **Kommando Paletten**.
1. Vælg **+ Tilføj Server**.
1. Vælg **Opret en Ny MCP Server**.
1. Vælg **python-weather** som skabelon.
1. Vælg **Standardmappe** for at gemme MCP-serverens skabelon.
1. Indtast følgende navn til serveren: **Lommeregner**
1. Et nyt Visual Studio Code-vindue åbnes. Vælg **Ja, jeg stoler på forfatterne**.
1. Brug terminalen (**Terminal** > **Ny Terminal**) til at oprette et virtuelt miljø: `python -m venv .venv`
1. Brug terminalen til at aktivere det virtuelle miljø:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Brug terminalen til at installere afhængighederne: `pip install -e .[dev]`
1. I **Udforsker**-visningen i **Aktivitetslinjen**, udvid **src**-mappen, og vælg **server.py** for at åbne filen i editoren.
1. Erstat koden i **server.py**-filen med følgende og gem:

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

### -4- Kør agenten med MCP-serveren for lommeregneren

Nu hvor din agent har værktøjer, er det tid til at bruge dem! I denne sektion vil du indsende prompter til agenten for at teste og validere, om agenten bruger det relevante værktøj fra MCP-serveren for lommeregneren.

1. Tryk på `F5` for at starte debugging af MCP-serveren. **Agent (Prompt) Builder** åbnes i en ny redigeringstab. Serverens status er synlig i terminalen.
1. I feltet **Brugerprompt** i **Agent (Prompt) Builder**, indtast følgende prompt: `Jeg købte 3 varer til $25 hver og brugte derefter en rabat på $20. Hvor meget betalte jeg?`
1. Klik på knappen **Kør** for at generere agentens svar.
1. Gennemgå agentens output. Modellen bør konkludere, at du betalte **$55**.
1. Her er en oversigt over, hvad der bør ske:
    - Agenten vælger værktøjerne **multiply** og **subtract** for at hjælpe med beregningen.
    - De respektive værdier `a` og `b` tildeles for værktøjet **multiply**.
    - De respektive værdier `a` og `b` tildeles for værktøjet **subtract**.
    - Svaret fra hvert værktøj gives i det respektive **Værktøjssvar**.
    - Det endelige output fra modellen gives i det endelige **Modelsvar**.
1. Indsend yderligere prompter for at teste agenten yderligere. Du kan ændre den eksisterende prompt i feltet **Brugerprompt** ved at klikke i feltet og erstatte den eksisterende prompt.
1. Når du er færdig med at teste agenten, kan du stoppe serveren via **terminalen** ved at indtaste **CTRL/CMD+C** for at afslutte.

## Opgave

Prøv at tilføje en ekstra værktøjsindgang til din **server.py**-fil (f.eks. returnere kvadratroden af et tal). Indsend yderligere prompter, der kræver, at agenten bruger dit nye værktøj (eller eksisterende værktøjer). Sørg for at genstarte serveren for at indlæse de nytilføjede værktøjer.

## Løsning

[Løsning](./solution/README.md)

## Vigtige pointer

De vigtigste pointer fra dette kapitel er følgende:

- AI Toolkit-udvidelsen er en fremragende klient, der giver dig mulighed for at forbruge MCP-servere og deres værktøjer.
- Du kan tilføje nye værktøjer til MCP-servere og udvide agentens evner til at imødekomme skiftende krav.
- AI Toolkit inkluderer skabeloner (f.eks. Python MCP-server-skabeloner) for at forenkle oprettelsen af brugerdefinerede værktøjer.

## Yderligere ressourcer

- [AI Toolkit-dokumentation](https://aka.ms/AIToolkit/doc)

## Hvad er det næste?
- Næste: [Test og fejlfinding](../08-testing/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.