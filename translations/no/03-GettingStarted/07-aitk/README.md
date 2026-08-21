# Konsumere en server fra AI Toolkit-utvidelsen for Visual Studio Code

Når du bygger en AI-agent handler det ikke bare om å generere smarte svar; det handler også om å gi agenten din evnen til å utføre handlinger. Det er her Model Context Protocol (MCP) kommer inn. MCP gjør det enkelt for agenter å få tilgang til eksterne verktøy og tjenester på en konsekvent måte. Tenk på det som å koble agenten din til et verktøyskrin den *faktisk* kan bruke.

La oss si at du kobler en agent til kalkulator-MCP-serveren din. Plutselig kan agenten din utføre matematiske operasjoner bare ved å motta en prompt som «Hva er 47 ganger 89?» — ingen grunn til å hardkode logikk eller bygge tilpassede API-er.

## Oversikt

Denne leksjonen dekker hvordan du kobler en kalkulator MCP-server til en agent med [AI Toolkit](https://aka.ms/AIToolkit)-utvidelsen i Visual Studio Code, og gjør det mulig for agenten din å utføre matematiske operasjoner som addisjon, subtraksjon, multiplikasjon og divisjon gjennom naturlig språk.

AI Toolkit er en kraftig utvidelse for Visual Studio Code som effektiviserer agentutvikling. AI-ingeniører kan enkelt bygge AI-applikasjoner ved å utvikle og teste generative AI-modeller — lokalt eller i skyen. Utvidelsen støtter de fleste store generative modeller som er tilgjengelige i dag.

*Merk*: AI Toolkit støtter for øyeblikket Python og TypeScript.

## Læringsmål

Innen slutten av denne leksjonen vil du kunne:

- Konsumere en MCP-server via AI Toolkit.
- Konfigurere en agentkonfigurasjon for å gjøre det mulig å oppdage og bruke verktøy levert av MCP-serveren.
- Bruke MCP-verktøy via naturlig språk.

## Tilnærming

Slik bør vi tilnærme oss dette på et overordnet nivå:

- Opprett en agent og definer systemprompten.
- Opprett en MCP-server med kalkulatorverktøy.
- Koble Agent Builder til MCP-serveren.
- Test agentens bruk av verktøy via naturlig språk.

Flott, nå som vi forstår flyten, la oss konfigurere en AI-agent for å utnytte eksterne verktøy gjennom MCP og styrke dens evner!

## Forutsetninger

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Øvelse: Konsumere en server

> [!WARNING]
> Merknad for macOS-brukere. Vi undersøker for tiden et problem som påvirker installasjon av avhengigheter på macOS. Som et resultat vil ikke macOS-brukere kunne fullføre denne veiledningen akkurat nå. Vi oppdaterer instruksjonene så snart en løsning er tilgjengelig. Takk for tålmodigheten og forståelsen!

I denne øvelsen skal du bygge, kjøre og forbedre en AI-agent med verktøy fra en MCP-server inne i Visual Studio Code ved hjelp av AI Toolkit.

### -0- Forberedelse, legg til OpenAI GPT-4o-modellen i Mine modeller

Øvelsen bruker **GPT-4o**-modellen. Modellen bør legges til i **Mine modeller** før du oppretter agenten.

![Skjermbilde av et modellvalggrensesnitt i Visual Studio Codes AI Toolkit-utvidelse. Overskriften lyder "Finn riktig modell for din AI-løsning" med en undertittel som oppfordrer brukere til å oppdage, teste og distribuere AI-modeller. Under , under “Populære modeller,” vises seks modellkort: DeepSeek-R1 (hostet av GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Små, raske), og DeepSeek-R1 (hostet av Ollama). Hvert kort inkluderer alternativer for å “Legge til” modellen eller “Prøve i Playground”.](../../../../translated_images/no/aitk-model-catalog.2acd38953bb9c119.webp)

1. Åpne **AI Toolkit**-utvidelsen fra **Aktivitetslinjen**.
1. I **Katalog**-seksjonen, velg **Modeller** for å åpne **Modellkatalogen**. Valg av **Modeller** åpner **Modellkatalogen** i en ny redigeringsfane.
1. I søkefeltet i **Modellkatalogen**, skriv inn **OpenAI GPT-4o**.
1. Klikk **+ Legg til** for å legge modellen til i listen **Mine modeller**. Sørg for at du har valgt modellen som er **hostet av GitHub**.
1. I **Aktivitetslinjen**, bekreft at **OpenAI GPT-4o**-modellen vises i listen.

### -1- Opprett en agent

**Agent (Prompt) Builder** lar deg opprette og tilpasse dine egne AI-drevne agenter. I denne delen skal du opprette en ny agent og tilordne en modell for å drive samtalen.

![Skjermbilde av "Calculator Agent"-byggergrensesnittet i AI Toolkit-utvidelsen for Visual Studio Code. Til venstre er modellen valgt som "OpenAI GPT-4o (via GitHub)". En systemprompt lyder "Du er en professor ved universitet som underviser i matematikk," og brukerprompten sier, "Forklar Fourier-ligningen på en enkel måte." Ytterligere alternativer inkluderer knapper for å legge til verktøy, aktivere MCP-server og velge strukturert utdata. En blå “Kjør”-knapp er nederst. Til høyre, under "Kom i gang med eksempler," listes tre prøveagenter: Webutvikler (med MCP Server, Andreklassesforenkler og Drømmetydning, hver med korte beskrivelser av deres funksjoner).](../../../../translated_images/no/aitk-agent-builder.901e3a2960c3e477.webp)

1. Åpne **AI Toolkit**-utvidelsen fra **Aktivitetslinjen**.
1. I **Verktøy**-seksjonen, velg **Agent (Prompt) Builder**. Å velge **Agent (Prompt) Builder** åpner **Agent (Prompt) Builder** i en ny redigeringsfane.
1. Klikk på **+ Ny agent**-knappen. Utvidelsen starter en oppstartsguide via **Kommandopaletten**.
1. Skriv inn navnet **Calculator Agent** og trykk **Enter**.
1. I **Agent (Prompt) Builder**, velg **OpenAI GPT-4o (via GitHub)**-modellen i feltet **Modell**.

### -2- Opprett en systemprompt for agenten

Når agenten er satt opp, er det på tide å definere dens personlighet og formål. I denne delen skal du bruke funksjonen **Generer systemprompt** for å beskrive agentens tiltenkte oppførsel — i dette tilfellet en kalkulatoragent — og la modellen lage systemprompten for deg.

![Skjermbilde av "Calculator Agent"-grensesnittet i AI Toolkit for Visual Studio Code med et modalt vindu åpent med tittelen "Generer en prompt." Vinduet forklarer at en promptmal kan genereres ved å dele grunnleggende detaljer, og inneholder et tekstfelt med eksempel på systemprompt: "Du er en hjelpsom og effektiv matematikkassistent. Når du får et problem som involverer grunnleggende aritmetikk, svarer du med riktig resultat." Under tekstfeltet er knappene "Lukk" og "Generer". I bakgrunnen vises deler av agentkonfigurasjonen, inkludert den valgte modellen "OpenAI GPT-4o (via GitHub)" og felter for system- og brukerprompter.](../../../../translated_images/no/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. For seksjonen **Prompter** klikker du på knappen **Generer systemprompt**. Denne knappen åpner promptbyggeren som bruker AI til å generere en systemprompt for agenten.
1. I vinduet **Generer en prompt**, skriv inn følgende: `Du er en hjelpsom og effektiv matematikkassistent. Når du får et problem som involverer grunnleggende aritmetikk, svarer du med riktig resultat.`
1. Klikk på **Generer**-knappen. Et varsel vises nederst til høyre som bekrefter at systemprompten genereres. Når genereringen er fullført, vil prompten vises i feltet **Systemprompt** i **Agent (Prompt) Builder**.
1. Gjennomgå **Systemprompt** og endre om nødvendig.

### -3- Opprett en MCP-server

Nå som du har definert agentens systemprompt — som styrer dens oppførsel og svar — er det på tide å utruste agenten med praktiske evner. I denne delen skal du opprette en kalkulator MCP-server med verktøy for å utføre addisjon, subtraksjon, multiplikasjon og divisjon. Denne serveren gjør det mulig for agenten din å utføre sanntids matematiske operasjoner som svar på naturlige språkprompter.

![Skjermbilde av den nedre delen av Calculator Agent-grensesnittet i AI Toolkit-utvidelsen for Visual Studio Code. Den viser utvidbare menyer for “Verktøy” og “Strukturert utdata,” sammen med en rullegardinmeny merket “Velg utdataformat” satt til “tekst.” Til høyre er det en knapp merket “+ MCP Server” for å legge til en Model Context Protocol-server. En bildeikonplassholder vises over Verktøy-delen.](../../../../translated_images/no/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit er utstyrt med maler som gjør det enkelt å lage din egen MCP-server. Vi bruker Python-malen for å opprette kalkulator MCP-serveren.

*Merk*: AI Toolkit støtter for øyeblikket Python og TypeScript.

1. I **Verktøy**-seksjonen i **Agent (Prompt) Builder**, klikk på **+ MCP Server**-knappen. Utvidelsen starter en oppstartsguide via **Kommandopaletten**.
1. Velg **+ Legg til server**.
1. Velg **Opprett en ny MCP-server**.
1. Velg **python-weather** som mal.
1. Velg **Standardmappe** for å lagre MCP-server-malen.
1. Skriv inn følgende navn for serveren: **Calculator**
1. Et nytt Visual Studio Code-vindu åpnes. Velg **Ja, jeg stoler på forfatterne**.
1. Bruk terminalen (**Terminal** > **Ny terminal**) for å lage et virtuelt miljø: `python -m venv .venv`
1. Bruk terminalen for å aktivere det virtuelle miljøet:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Bruk terminalen for å installere avhengighetene: `pip install -e .[dev]`
1. I **Utforsker**-visningen på **Aktivitetslinjen**, utvid **src**-mappen og velg **server.py** for å åpne filen i redigeringsprogrammet.
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

### -4- Kjør agenten med kalkulator MCP-serveren

Nå som agenten din har verktøy, er det på tide å bruke dem! I denne delen skal du sende prompter til agenten for å teste og validere om agenten bruker riktig verktøy fra kalkulator MCP-serveren.

![Skjermbilde av Calculator Agent-grensesnittet i AI Toolkit-utvidelsen for Visual Studio Code. Til venstre, under “Verktøy,” er det lagt til en MCP-server med navnet local-server-calculator_server som viser fire tilgjengelige verktøy: add, subtract, multiply, og divide. Et merke viser at fire verktøy er aktive. Under er en kollapset “Strukturert utdata”-seksjon og en blå “Kjør”-knapp. Til høyre, under “Model Response,” bruker agenten multiply- og subtract-verktøy med innspillene {"a": 3, "b": 25} og {"a": 75, "b": 20} henholdsvis. Det endelige “Tool Response” vises som 75.0. En “Se kode”-knapp vises nederst.](../../../../translated_images/no/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Du vil kjøre kalkulator MCP-serveren på din lokale utviklingsmaskin via **Agent Builder** som MCP-klient.

1. Trykk på `F5` for å starte feilsøking av MCP-serveren. **Agent (Prompt) Builder** åpnes i en ny redigeringsfane. Serverens status er synlig i terminalen.
1. I feltet **Brukerprompt** i **Agent (Prompt) Builder**, skriv inn følgende prompt: `Jeg kjøpte 3 varer til $25 hver, og brukte deretter en rabatt på $20. Hvor mye betalte jeg?`
1. Klikk på **Kjør**-knappen for å generere agentens svar.
1. Gjennomgå agentens utdata. Modellen bør komme fram til at du betalte **$55**.
1. Her er en oversikt over hva som bør skje:
    - Agenten velger verktøyene **multiply** og **subtract** for å hjelpe med beregningen.
    - De respektive `a` og `b`-verdiene tildeles for **multiply**-verktøyet.
    - De respektive `a` og `b`-verdiene tildeles for **subtract**-verktøyet.
    - Svarene fra hvert verktøy vises i respektive **Svar fra verktøy**.
    - Det endelige svaret fra modellen vises i den endelige **Modellresponsen**.
1. Send inn flere prompter for å teste agenten ytterligere. Du kan endre eksisterende prompt i feltet **Brukerprompt** ved å klikke i feltet og erstatte den eksisterende prompen.
1. Når du er ferdig med å teste agenten, kan du stoppe serveren via **terminalen** ved å taste **CTRL/CMD+C** for å avslutte.

## Oppgave

Prøv å legge til en ekstra verktøypost i **server.py**-filen din (for eksempel: returner kvadratroten av et tall). Send inn flere prompter som krever at agenten bruker ditt nye verktøy (eller eksisterende verktøy). Husk å starte serveren på nytt for å laste inn nylig lagde verktøy.

## Løsning

[Løsning](./solution/README.md)

## Nøkkelpunkter

De viktigste læringspunktene i dette kapittelet er:

- AI Toolkit-utvidelsen er en flott klient som lar deg konsumere MCP-servere og deres verktøy.
- Du kan legge til nye verktøy i MCP-servere, noe som utvider agentens evner slik at den kan møte endrede krav.
- AI Toolkit inkluderer maler (for eksempel Python MCP-servermaler) for å forenkle opprettelsen av egendefinerte verktøy.

## Ytterligere ressurser

- [AI Toolkit-dokumentasjon](https://aka.ms/AIToolkit/doc)

## Hva er neste
- Neste: [Testing og feilsøking](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->