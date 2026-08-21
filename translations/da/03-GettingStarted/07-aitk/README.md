# Forbrug af en server fra AI Toolkit-udvidelsen til Visual Studio Code

Når du bygger en AI-agent, handler det ikke kun om at generere smarte svar; det handler også om at give din agent evnen til at handle. Det er her Model Context Protocol (MCP) kommer ind i billedet. MCP gør det nemt for agenter at få adgang til eksterne værktøjer og tjenester på en konsistent måde. Tænk på det som at tilslutte din agent til en værktøjskasse, som den *rent faktisk* kan bruge.

Lad os sige, at du forbinder en agent til din calculator MCP-server. Pludselig kan din agent udføre matematiske operationer blot ved at modtage en prompt som “Hvad er 47 gange 89?”—uden at skulle kode logik direkte eller bygge brugerdefinerede API’er.

## Oversigt

Denne lektion dækker, hvordan du forbinder en calculator MCP-server til en agent med [AI Toolkit](https://aka.ms/AIToolkit) udvidelsen i Visual Studio Code, så din agent kan udføre matematiske operationer såsom addition, subtraktion, multiplikation og division gennem naturligt sprog.

AI Toolkit er en kraftfuld udvidelse til Visual Studio Code, der forenkler agentudvikling. AI-ingeniører kan nemt bygge AI-applikationer ved at udvikle og teste generative AI-modeller—lokalt eller i skyen. Udvidelsen understøtter de fleste større generative modeller, der findes i dag.

*Bemærk*: AI Toolkit understøtter i øjeblikket Python og TypeScript.

## Læringsmål

Når du er færdig med denne lektion, vil du kunne:

- Forbruge en MCP-server via AI Toolkit.
- Konfigurere en agentkonfiguration, så den kan opdage og anvende værktøjer leveret af MCP-serveren.
- Bruge MCP-værktøjer via naturligt sprog.

## Fremgangsmåde

Her er, hvordan vi skal gribe det an på et overordnet niveau:

- Opret en agent og definer dens systemprompt.
- Opret en MCP-server med calculator-værktøjer.
- Forbind Agent Builder til MCP-serveren.
- Test agentens brug af værktøjer via naturligt sprog.

Fantastisk, nu hvor vi forstår forløbet, lad os konfigurere en AI-agent til at udnytte eksterne værktøjer gennem MCP og dermed øge dens kapaciteter!

## Forudsætninger

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Øvelse: Forbrug af en server

> [!WARNING]
> Bemærk for macOS-brugere. Vi undersøger i øjeblikket et problem, der påvirker installation af afhængigheder på macOS. Derfor kan macOS-brugere ikke fuldføre denne vejledning lige nu. Vi opdaterer instruktionerne så snart en løsning foreligger. Tak for jeres tålmodighed og forståelse!

I denne øvelse vil du bygge, køre og forbedre en AI-agent med værktøjer fra en MCP-server inde i Visual Studio Code ved brug af AI Toolkit.

### -0- Forberedelse, tilføj OpenAI GPT-4o modellen til Mine Modeller

Øvelsen benytter **GPT-4o** modellen. Modellen skal tilføjes til **Mine Modeller** før oprettelsen af agenten.

![Skærmbillede af en modeludvælgelsesgrænseflade i Visual Studio Codes AI Toolkit-udvidelse. Overskriften lyder "Find den rigtige model til din AI-løsning" med en undertitel, der opfordrer brugere til at opdage, teste og implementere AI-modeller. Under “Populære modeller” vises seks modelkort: DeepSeek-R1 (hostet af GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Lille, Hurtig) og DeepSeek-R1 (hostet af Ollama). Hvert kort indeholder muligheder for at “Tilføje” modellen eller “Prøve i Playground](../../../../translated_images/da/aitk-model-catalog.2acd38953bb9c119.webp)

1. Åbn **AI Toolkit** udvidelsen fra **Activity Bar**.
1. I **Katalog** sektionen skal du vælge **Modeller** for at åbne **Modelkataloget**. Valg af **Modeller** åbner **Modelkataloget** i en ny editorfane.
1. I søgefeltet i **Modelkataloget** skal du indtaste **OpenAI GPT-4o**.
1. Klik på **+ Tilføj** for at tilføje modellen til din liste **Mine Modeller**. Sørg for, at du har valgt modellen, der er **hostet af GitHub**.
1. Bekræft i **Activity Bar**, at **OpenAI GPT-4o** modellen vises på listen.

### -1- Opret en agent

**Agent (Prompt) Builder** giver dig mulighed for at skabe og tilpasse dine egne AI-drevne agenter. I denne sektion opretter du en ny agent og tildeler en model, der skal drive samtalen.

![Skærmbillede af "Calculator Agent" builder-grænsefladen i AI Toolkit-udvidelsen til Visual Studio Code. På venstre panel er den valgte model "OpenAI GPT-4o (via GitHub)." En systemprompt lyder "Du er professor på universitetet, der underviser i matematik," og brugerprompten siger, "Forklar Fourier-ligningen for mig på en simpel måde." Yderligere muligheder inkluderer knapper til at tilføje værktøjer, aktivere MCP Server og vælge struktureret output. En blå “Kør”-knap er i bunden. På højre panel under "Kom i gang med eksempler" er tre prøveagenter listet: Webudvikler (med MCP Server, andet klasses forenkler og drømmetydningsagent, hver med korte beskrivelser af deres funktioner).](../../../../translated_images/da/aitk-agent-builder.901e3a2960c3e477.webp)

1. Åbn **AI Toolkit** udvidelsen fra **Activity Bar**.
1. I **Værktøjer** sektionen skal du vælge **Agent (Prompt) Builder**. Valg af **Agent (Prompt) Builder** åbner **Agent (Prompt) Builder** i en ny editorfane.
1. Klik på **+ Ny Agent** knappen. Udvidelsen vil starte en opsætningsguide via **Command Palette**.
1. Indtast navnet **Calculator Agent** og tryk på **Enter**.
1. I **Agent (Prompt) Builder**, vælg for **Model** feltet modellen **OpenAI GPT-4o (via GitHub)**.

### -2- Opret en systemprompt for agenten

Når agenten er opstillet, er det tid til at definere dens personlighed og formål. I denne sektion bruger du funktionen **Generer systemprompt** til at beskrive agentens tilsigtede adfærd—i dette tilfælde en calculator agent—og lade modellen skrive systemprompten for dig.

![Skærmbillede af "Calculator Agent" interface i AI Toolkit for Visual Studio Code med et modalvindue åbent kaldet "Generer en prompt." Modalen forklarer, at en promptskabelon kan genereres ved at dele grundlæggende information og inkluderer en tekstboks med eksempel-systemprompten: "Du er en hjælpsom og effektiv matematikassistent. Når du får et problem, der involverer grundlæggende regning, svarer du med det korrekte resultat." Under tekstboksen er der knapperne "Luk" og "Generer." I baggrunden er en del af agentkonfigurationen synlig, inklusive den valgte model "OpenAI GPT-4o (via GitHub)" og felter til system- og brugerprompter.](../../../../translated_images/da/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. For sektionen **Prompter**, klik på **Generer systemprompt** knappen. Denne knap åbner promptbyggeren, som bruger AI til at generere en systemprompt for agenten.
1. I vinduet **Generer en prompt**, indtast følgende: `Du er en hjælpsom og effektiv matematikassistent. Når du får et problem, der involverer grundlæggende regning, svarer du med det korrekte resultat.`
1. Klik på **Generer** knappen. En meddelelse vises nederst til højre og bekræfter, at systemprompten genereres. Når promptgenereringen er færdig, vises prompten i feltet **Systemprompt** i **Agent (Prompt) Builder**.
1. Gennemgå **Systemprompten** og rediger om nødvendigt.

### -3- Opret en MCP-server

Nu hvor du har defineret din agents systemprompt—som styrer dens adfærd og svar—er det tid til at udstyre agenten med praktiske evner. I denne sektion opretter du en calculator MCP-server med værktøjer til at udføre addition, subtraktion, multiplikation og division. Denne server vil gøre det muligt for din agent at udføre matematiske operationer i realtid som svar på naturlige sprogprompter.

![Skærmbillede af den nederste del af Calculator Agent interfacet i AI Toolkit-udvidelsen til Visual Studio Code. Det viser foldbare menuer for “Værktøjer” og “Struktureret output” samt en rullemenu mærket “Vælg outputformat” sat til “tekst.” Til højre er der en knap mærket “+ MCP Server” til tilføjelse af en Model Context Protocol server. Et billedeikon-placerholder vises over Værktøjer sektionen.](../../../../translated_images/da/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit er udstyret med skabeloner for nemt at skabe din egen MCP-server. Vi bruger Python-skabelonen til at lave calculator MCP-serveren.

*Bemærk*: AI Toolkit understøtter i øjeblikket Python og TypeScript.

1. I **Værktøjer** sektionen af **Agent (Prompt) Builder**, klik på **+ MCP Server** knappen. Udvidelsen vil starte en opsætningsguide via **Command Palette**.
1. Vælg **+ Tilføj Server**.
1. Vælg **Opret en ny MCP-server**.
1. Vælg **python-weather** som skabelon.
1. Vælg **Standardmappe** til at gemme MCP-server skabelonen.
1. Indtast følgende navn for serveren: **Calculator**
1. Et nyt Visual Studio Code-vindue åbnes. Vælg **Ja, jeg stoler på forfatterne**.
1. Brug terminalen (**Terminal** > **Ny terminal**) til at oprette et virtuelt miljø: `python -m venv .venv`
1. Brug terminalen til at aktivere det virtuelle miljø:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Brug terminalen til at installere afhængigheder: `pip install -e .[dev]`
1. I **Explorer** visningen i **Activity Bar**, udvid **src** mappen og vælg **server.py** for at åbne filen i editoren.
1. Erstat koden i **server.py** filen med følgende og gem:

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

### -4- Kør agenten med calculator MCP-serveren

Nu hvor din agent har værktøjer, er det tid til at bruge dem! I denne sektion vil du sende prompter til agenten for at teste og validere, om agenten udnytter det rette værktøj fra calculator MCP-serveren.

![Skærmbillede af Calculator Agent interfacet i AI Toolkit-udvidelsen til Visual Studio Code. På venstre panel under “Værktøjer” er en MCP-server ved navn local-server-calculator_server tilføjet, som viser fire tilgængelige værktøjer: add, subtract, multiply og divide. Et badge viser, at fire værktøjer er aktive. Nederst er en foldet sektion “Struktureret output” og en blå “Kør” knap. På højre panel under “Modelresponse” påkalder agenten multiply og subtract værktøjerne med inputs {"a": 3, "b": 25} og {"a": 75, "b": 20} henholdsvis. Den endelige “Tool Response” vises som 75.0. En “Se kode” knap er nederst.](../../../../translated_images/da/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Du vil køre calculator MCP-serveren på din lokale udviklingsmaskine via **Agent Builder** som MCP-klient.

1. Tryk på `F5` for at starte debugging af MCP-serveren. **Agent (Prompt) Builder** åbnes i en ny editorfane. Serverens status er synlig i terminalen.
1. I feltet **Brugerprompt** i **Agent (Prompt) Builder**, indtast følgende prompt: `Jeg købte 3 varer til $25 stykket og brugte derefter en rabat på $20. Hvor meget betalte jeg?`
1. Klik på **Kør** knappen for at generere agentens svar.
1. Gennemgå agentens output. Modellen burde konkludere, at du betalte **$55**.
1. Her er en gennemgang af, hvad der bør ske:
    - Agenten vælger værktøjerne **multiply** og **subtract** til at hjælpe med beregningen.
    - De respektive værdier for `a` og `b` tildeles for **multiply** værktøjet.
    - De respektive værdier for `a` og `b` tildeles for **subtract** værktøjet.
    - Svaret fra hvert værktøj leveres i den respektive **Tool Response**.
    - Det endelige output fra modellen vises i den endelige **Model Response**.
1. Indsend yderligere prompter for yderligere at teste agenten. Du kan ændre den eksisterende prompt i **Brugerprompt** feltet ved at klikke i feltet og erstatte den eksisterende prompt.
1. Når du er færdig med at teste agenten, kan du stoppe serveren via **terminalen** ved at trykke på **CTRL/CMD+C** for at afslutte.

## Opgave

Prøv at tilføje et ekstra værktøj til din **server.py** fil (f.eks. returner kvadratroden af et tal). Indsend yderligere prompter, som kræver, at agenten udnytter dit nye værktøj (eller eksisterende værktøjer). Husk at genstarte serveren for at indlæse nyligt tilføjede værktøjer.

## Løsning

[Løsning](./solution/README.md)

## Vigtige pointer

De vigtigste pointer fra dette kapitel er følgende:

- AI Toolkit-udvidelsen er en fremragende klient, der lader dig forbruge MCP-servere og deres værktøjer.
- Du kan tilføje nye værktøjer til MCP-servere, hvilket udvider agentens kapaciteter til at opfylde udviklende krav.
- AI Toolkit indeholder skabeloner (f.eks. Python MCP-server skabeloner) for at forenkle oprettelsen af brugerdefinerede værktøjer.

## Yderligere ressourcer

- [AI Toolkit dokumentation](https://aka.ms/AIToolkit/doc)

## Hvad er det næste
- Næste: [Test og debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->