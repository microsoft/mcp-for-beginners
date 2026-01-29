# Konsumere en server fra AI Toolkit-utvidelsen for Visual Studio Code

Når du bygger en AI-agent, handler det ikke bare om å generere smarte svar; det handler også om å gi agenten evnen til å utføre handlinger. Det er her Model Context Protocol (MCP) kommer inn. MCP gjør det enkelt for agenter å få tilgang til eksterne verktøy og tjenester på en konsistent måte. Tenk på det som å koble agenten din til en verktøykasse den faktisk kan *bruke*.

La oss si at du kobler en agent til MCP-serveren for kalkulator. Plutselig kan agenten utføre matematiske operasjoner bare ved å motta en forespørsel som "Hva er 47 ganger 89?"—uten behov for å hardkode logikk eller bygge tilpassede API-er.

## Oversikt

Denne leksjonen dekker hvordan du kobler en MCP-server for kalkulator til en agent med [AI Toolkit](https://aka.ms/AIToolkit)-utvidelsen i Visual Studio Code, slik at agenten kan utføre matematiske operasjoner som addisjon, subtraksjon, multiplikasjon og divisjon via naturlig språk.

AI Toolkit er en kraftig utvidelse for Visual Studio Code som forenkler utviklingen av agenter. AI-ingeniører kan enkelt bygge AI-applikasjoner ved å utvikle og teste generative AI-modeller—lokalt eller i skyen. Utvidelsen støtter de fleste store generative modeller som er tilgjengelige i dag.

*Merk*: AI Toolkit støtter for øyeblikket Python og TypeScript.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Konsumere en MCP-server via AI Toolkit.
- Konfigurere en agentkonfigurasjon for å gjøre det mulig for agenten å oppdage og bruke verktøy levert av MCP-serveren.
- Bruke MCP-verktøy via naturlig språk.

## Tilnærming

Her er hvordan vi skal tilnærme oss dette på et overordnet nivå:

- Opprett en agent og definer dens systemprompt.
- Opprett en MCP-server med kalkulatorverktøy.
- Koble Agent Builder til MCP-serveren.
- Test agentens bruk av verktøy via naturlig språk.

Flott, nå som vi forstår flyten, la oss konfigurere en AI-agent til å utnytte eksterne verktøy gjennom MCP og forbedre dens evner!

## Forutsetninger

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Øvelse: Konsumere en server

> [!WARNING]
> Merk for macOS-brukere. Vi undersøker for øyeblikket et problem som påvirker installasjon av avhengigheter på macOS. Som et resultat vil macOS-brukere ikke kunne fullføre denne opplæringen på nåværende tidspunkt. Vi vil oppdatere instruksjonene så snart en løsning er tilgjengelig. Takk for tålmodigheten og forståelsen!

I denne øvelsen vil du bygge, kjøre og forbedre en AI-agent med verktøy fra en MCP-server inne i Visual Studio Code ved hjelp av AI Toolkit.

### -0- Forberedelse, legg til OpenAI GPT-4o-modellen i Mine Modeller

Øvelsen bruker **GPT-4o**-modellen. Modellen bør legges til **Mine Modeller** før du oppretter agenten.

![Skjermbilde av modellvalggrensesnittet i AI Toolkit-utvidelsen for Visual Studio Code. Overskriften lyder "Finn den rette modellen for din AI-løsning" med en undertittel som oppmuntrer brukere til å oppdage, teste og distribuere AI-modeller. Under "Populære modeller" vises seks modellkort: DeepSeek-R1 (GitHub-hostet), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Liten, Rask), og DeepSeek-R1 (Ollama-hostet). Hvert kort inkluderer alternativer for å "Legge til" modellen eller "Prøve i Playground](../../../../translated_images/no/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.png)

1. Åpne **AI Toolkit**-utvidelsen fra **Aktivitetsfeltet**.
1. I **Katalog**-seksjonen, velg **Modeller** for å åpne **Model Catalog**. Når du velger **Modeller**, åpnes **Model Catalog** i en ny editorfane.
1. I søkefeltet i **Model Catalog**, skriv inn **OpenAI GPT-4o**.
1. Klikk **+ Legg til** for å legge modellen til listen **Mine Modeller**. Sørg for at du har valgt modellen som er **Hostet av GitHub**.
1. I **Aktivitetsfeltet**, bekreft at modellen **OpenAI GPT-4o** vises i listen.

### -1- Opprett en agent

**Agent (Prompt) Builder** lar deg opprette og tilpasse dine egne AI-drevne agenter. I denne delen vil du opprette en ny agent og tilordne en modell for å drive samtalen.

![Skjermbilde av "Kalkulatoragent"-byggergrensesnittet i AI Toolkit-utvidelsen for Visual Studio Code. På venstre panel er modellen som er valgt "OpenAI GPT-4o (via GitHub)." En systemprompt lyder "Du er en professor ved universitetet som underviser i matematikk," og brukerprompten sier "Forklar Fourier-ligningen på en enkel måte." Ytterligere alternativer inkluderer knapper for å legge til verktøy, aktivere MCP-server og velge strukturert output. En blå "Kjør"-knapp er nederst. På høyre panel, under "Kom i gang med eksempler," er tre eksempelagenter listet opp: Webutvikler (med MCP-server, Andreklasseforenkler og Drømmetolk, hver med korte beskrivelser av deres funksjoner.](../../../../translated_images/no/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.png)

1. Åpne **AI Toolkit**-utvidelsen fra **Aktivitetsfeltet**.
1. I **Verktøy**-seksjonen, velg **Agent (Prompt) Builder**. Når du velger **Agent (Prompt) Builder**, åpnes **Agent (Prompt) Builder** i en ny editorfane.
1. Klikk på **+ Ny Agent**-knappen. Utvidelsen vil starte en oppsettsveiviser via **Kommandopaletten**.
1. Skriv inn navnet **Kalkulatoragent** og trykk **Enter**.
1. I **Agent (Prompt) Builder**, for feltet **Modell**, velg modellen **OpenAI GPT-4o (via GitHub)**.

### -2- Opprett en systemprompt for agenten

Med agenten opprettet, er det på tide å definere dens personlighet og formål. I denne delen vil du bruke funksjonen **Generer systemprompt** for å beskrive agentens tiltenkte oppførsel—i dette tilfellet en kalkulatoragent—og la modellen skrive systemprompten for deg.

![Skjermbilde av "Kalkulatoragent"-grensesnittet i AI Toolkit for Visual Studio Code med et modalt vindu åpent med tittelen "Generer en prompt." Modalen forklarer at en promptmal kan genereres ved å dele grunnleggende detaljer og inkluderer en tekstboks med eksempelsystemprompten: "Du er en hjelpsom og effektiv matematikkassistent. Når du får et problem som involverer grunnleggende aritmetikk, svarer du med riktig resultat." Under tekstboksen er knapper for "Lukk" og "Generer." I bakgrunnen er en del av agentkonfigurasjonen synlig, inkludert den valgte modellen "OpenAI GPT-4o (via GitHub)" og felt for system- og brukerprompter.](../../../../translated_images/no/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.png)

1. For seksjonen **Prompter**, klikk på knappen **Generer systemprompt**. Denne knappen åpner promptbyggeren som bruker AI til å generere en systemprompt for agenten.
1. I vinduet **Generer en prompt**, skriv inn følgende: `Du er en hjelpsom og effektiv matematikkassistent. Når du får et problem som involverer grunnleggende aritmetikk, svarer du med riktig resultat.`
1. Klikk på **Generer**-knappen. En varsling vil vises nederst til høyre som bekrefter at systemprompten genereres. Når genereringen er fullført, vil prompten vises i feltet **Systemprompt** i **Agent (Prompt) Builder**.
1. Gjennomgå **Systemprompten** og modifiser den om nødvendig.

### -3- Opprett en MCP-server

Nå som du har definert agentens systemprompt—som styrer dens oppførsel og svar—er det på tide å utstyre agenten med praktiske evner. I denne delen vil du opprette en MCP-server for kalkulator med verktøy for å utføre addisjon, subtraksjon, multiplikasjon og divisjon. Denne serveren vil gjøre det mulig for agenten å utføre matematiske operasjoner i sanntid som svar på naturlige språkforespørsler.

!["Skjermbilde av den nedre delen av Kalkulatoragent-grensesnittet i AI Toolkit-utvidelsen for Visual Studio Code. Det viser utvidbare menyer for “Verktøy” og “Strukturert output,” sammen med en rullegardinmeny merket “Velg outputformat” satt til “tekst.” Til høyre er det en knapp merket “+ MCP Server” for å legge til en Model Context Protocol-server. Et bildeikonplassholder vises over Verktøy-seksjonen.](../../../../translated_images/no/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.png)

AI Toolkit er utstyrt med maler for å gjøre det enkelt å opprette din egen MCP-server. Vi vil bruke Python-malen for å opprette MCP-serveren for kalkulator.

*Merk*: AI Toolkit støtter for øyeblikket Python og TypeScript.

1. I seksjonen **Verktøy** i **Agent (Prompt) Builder**, klikk på knappen **+ MCP Server**. Utvidelsen vil starte en oppsettsveiviser via **Kommandopaletten**.
1. Velg **+ Legg til Server**.
1. Velg **Opprett en ny MCP-server**.
1. Velg **python-weather** som malen.
1. Velg **Standardmappe** for å lagre MCP-servermalen.
1. Skriv inn følgende navn for serveren: **Kalkulator**
1. Et nytt Visual Studio Code-vindu vil åpne seg. Velg **Ja, jeg stoler på forfatterne**.
1. Bruk terminalen (**Terminal** > **Ny Terminal**) til å opprette et virtuelt miljø: `python -m venv .venv`
1. Bruk terminalen til å aktivere det virtuelle miljøet:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Bruk terminalen til å installere avhengighetene: `pip install -e .[dev]`
1. I **Utforsker**-visningen i **Aktivitetsfeltet**, utvid katalogen **src** og velg **server.py** for å åpne filen i editoren.
1. Erstatt koden i **server.py**-filen med følgende og lagre:

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

### -4- Kjør agenten med MCP-serveren for kalkulator

Nå som agenten din har verktøy, er det på tide å bruke dem! I denne delen vil du sende forespørsler til agenten for å teste og validere om agenten bruker det riktige verktøyet fra MCP-serveren for kalkulator.

![Skjermbilde av Kalkulatoragent-grensesnittet i AI Toolkit-utvidelsen for Visual Studio Code. På venstre panel, under “Verktøy,” er en MCP-server kalt local-server-calculator_server lagt til, som viser fire tilgjengelige verktøy: add, subtract, multiply og divide. Et merke viser at fire verktøy er aktive. Under er en kollapset “Strukturert output”-seksjon og en blå “Kjør”-knapp. På høyre panel, under “Modellrespons,” bruker agenten verktøyene multiply og subtract med input {"a": 3, "b": 25} og {"a": 75, "b": 20} henholdsvis. Den endelige “Verktøyresponsen” vises som 75.0. En “Vis kode”-knapp vises nederst.](../../../../translated_images/no/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.png)

Du vil kjøre MCP-serveren for kalkulator på din lokale utviklingsmaskin via **Agent Builder** som MCP-klient.

1. Trykk `F5` for å starte debugging av MCP-serveren. **Agent (Prompt) Builder** vil åpne seg i en ny editorfane. Statusen til serveren er synlig i terminalen.
1. I feltet **Brukerprompt** i **Agent (Prompt) Builder**, skriv inn følgende prompt: `Jeg kjøpte 3 varer til $25 hver, og brukte deretter en rabatt på $20. Hvor mye betalte jeg?`
1. Klikk på **Kjør**-knappen for å generere agentens respons.
1. Gjennomgå agentens output. Modellen bør konkludere med at du betalte **$55**.
1. Her er en oversikt over hva som bør skje:
    - Agenten velger verktøyene **multiply** og **subtract** for å hjelpe med beregningen.
    - De respektive `a`- og `b`-verdiene tildeles for verktøyet **multiply**.
    - De respektive `a`- og `b`-verdiene tildeles for verktøyet **subtract**.
    - Responsen fra hvert verktøy gis i den respektive **Verktøyresponsen**.
    - Den endelige outputen fra modellen gis i den endelige **Modellresponsen**.
1. Send inn flere forespørsler for å teste agenten ytterligere. Du kan endre den eksisterende prompten i feltet **Brukerprompt** ved å klikke inn i feltet og erstatte den eksisterende prompten.
1. Når du er ferdig med å teste agenten, kan du stoppe serveren via **terminalen** ved å skrive **CTRL/CMD+C** for å avslutte.

## Oppgave

Prøv å legge til en ekstra verktøyoppføring i filen **server.py** (f.eks.: returnere kvadratroten av et tall). Send inn flere forespørsler som krever at agenten bruker ditt nye verktøy (eller eksisterende verktøy). Sørg for å starte serveren på nytt for å laste inn nylig lagt til verktøy.

## Løsning

[Løsning](./solution/README.md)

## Viktige punkter

De viktigste punktene fra dette kapittelet er følgende:

- AI Toolkit-utvidelsen er en flott klient som lar deg konsumere MCP-servere og deres verktøy.
- Du kan legge til nye verktøy i MCP-servere, og utvide agentens evner for å møte utviklende krav.
- AI Toolkit inkluderer maler (f.eks. Python MCP-servermaler) for å forenkle opprettelsen av tilpassede verktøy.

## Tilleggsressurser

- [AI Toolkit-dokumentasjon](https://aka.ms/AIToolkit/doc)

## Hva er neste
- Neste: [Testing og Feilsøking](../08-testing/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.