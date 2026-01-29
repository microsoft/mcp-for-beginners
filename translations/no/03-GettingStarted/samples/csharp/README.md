# Basic Calculator MCP Service

Denne tjenesten tilbyr grunnleggende kalkulatoroperasjoner gjennom Model Context Protocol (MCP). Den er laget som et enkelt eksempel for nybegynnere som lærer om MCP-implementasjoner.

For mer informasjon, se [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funksjoner

Denne kalkulatortjenesten tilbyr følgende muligheter:

1. **Grunnleggende aritmetiske operasjoner**:
   - Addisjon av to tall
   - Subtraksjon av ett tall fra et annet
   - Multiplikasjon av to tall
   - Divisjon av ett tall med et annet (med sjekk for null-divisjon)

## Bruke `stdio`-typen

## Konfigurasjon

1. **Konfigurer MCP-servere**:
   - Åpne arbeidsområdet ditt i VS Code.
   - Opprett en `.vscode/mcp.json`-fil i arbeidsområdet ditt for å konfigurere MCP-servere. Eksempel på konfigurasjon:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Du vil bli bedt om å oppgi roten til GitHub-repositoriet, som kan hentes med kommandoen `git rev-parse --show-toplevel`.

## Bruke tjenesten

Tjenesten eksponerer følgende API-endepunkter gjennom MCP-protokollen:

- `add(a, b)`: Legg sammen to tall
- `subtract(a, b)`: Trekk det andre tallet fra det første
- `multiply(a, b)`: Multipliser to tall
- `divide(a, b)`: Del det første tallet med det andre (med sjekk for null)
- isPrime(n): Sjekk om et tall er et primtall

## Test med Github Copilot Chat i VS Code

1. Prøv å sende en forespørsel til tjenesten ved hjelp av MCP-protokollen. For eksempel kan du spørre:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. For å sikre at verktøyene brukes, legg til #MyCalculator i prompten. For eksempel:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Containerisert versjon

Den forrige løsningen er flott når du har .NET SDK installert og alle avhengigheter på plass. Men hvis du ønsker å dele løsningen eller kjøre den i et annet miljø, kan du bruke den containeriserte versjonen.

1. Start Docker og sørg for at det kjører.
1. Fra en terminal, naviger til mappen `03-GettingStarted\samples\csharp\src`
1. For å bygge Docker-imaget for kalkulatortjenesten, kjør følgende kommando (erstatt `<YOUR-DOCKER-USERNAME>` med ditt Docker Hub-brukernavn):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Etter at imaget er bygget, laster vi det opp til Docker Hub. Kjør følgende kommando:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Bruke den Dockeriserte versjonen

1. I `.vscode/mcp.json`-filen, erstatt serverkonfigurasjonen med følgende:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Ser du på konfigurasjonen, kan du se at kommandoen er `docker` og argumentene er `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. `--rm`-flagget sørger for at containeren fjernes etter at den stopper, og `-i`-flagget lar deg interagere med containerens standard input. Det siste argumentet er navnet på imaget vi nettopp bygde og lastet opp til Docker Hub.

## Test den Dockeriserte versjonen

Start MCP-serveren ved å klikke på den lille Start-knappen over `"mcp-calc": {`, og akkurat som før kan du be kalkulatortjenesten om å gjøre noen utregninger for deg.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.