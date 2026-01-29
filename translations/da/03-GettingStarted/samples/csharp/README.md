# Basic Calculator MCP Service

Denne service tilbyder grundlæggende lommeregnerfunktioner via Model Context Protocol (MCP). Den er designet som et simpelt eksempel for begyndere, der lærer om MCP-implementeringer.

For mere information, se [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funktioner

Denne lommeregner-service tilbyder følgende funktioner:

1. **Grundlæggende aritmetiske operationer**:
   - Addition af to tal
   - Subtraktion af et tal fra et andet
   - Multiplikation af to tal
   - Division af et tal med et andet (med kontrol for division med nul)

## Brug af `stdio` Type

## Konfiguration

1. **Konfigurer MCP-servere**:
   - Åbn dit workspace i VS Code.
   - Opret en `.vscode/mcp.json` fil i din workspace-mappe for at konfigurere MCP-servere. Eksempel på konfiguration:

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

   - Du vil blive bedt om at indtaste roden af GitHub-repositoriet, som kan hentes med kommandoen `git rev-parse --show-toplevel`.

## Brug af Servicen

Servicen eksponerer følgende API-endpoints via MCP-protokollen:

- `add(a, b)`: Læg to tal sammen
- `subtract(a, b)`: Træk det andet tal fra det første
- `multiply(a, b)`: Gange to tal
- `divide(a, b)`: Divider det første tal med det andet (med nul-kontrol)
- isPrime(n): Tjek om et tal er et primtal

## Test med Github Copilot Chat i VS Code

1. Prøv at lave en forespørgsel til servicen via MCP-protokollen. For eksempel kan du spørge:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. For at sikre, at den bruger værktøjerne, tilføj #MyCalculator til prompten. For eksempel:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Containeriseret Version

Den tidligere løsning er god, når du har .NET SDK installeret, og alle afhængigheder er på plads. Men hvis du vil dele løsningen eller køre den i et andet miljø, kan du bruge den containeriserede version.

1. Start Docker og sørg for, at det kører.
1. Fra en terminal, naviger til mappen `03-GettingStarted\samples\csharp\src`
1. For at bygge Docker-billedet til lommeregner-servicen, kør følgende kommando (erstat `<YOUR-DOCKER-USERNAME>` med dit Docker Hub brugernavn):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Når billedet er bygget, uploader vi det til Docker Hub. Kør følgende kommando:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Brug den Dockeriserede Version

1. I `.vscode/mcp.json` filen, erstat serverkonfigurationen med følgende:
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
   Hvis du kigger på konfigurationen, kan du se, at kommandoen er `docker` og argumenterne er `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Flaget `--rm` sikrer, at containeren fjernes efter den stopper, og flaget `-i` tillader interaktion med containerens standardinput. Det sidste argument er navnet på det billede, vi netop har bygget og uploadet til Docker Hub.

## Test den Dockeriserede Version

Start MCP-serveren ved at klikke på den lille Start-knap over `"mcp-calc": {`, og ligesom før kan du bede lommeregner-servicen om at udføre nogle beregninger for dig.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.