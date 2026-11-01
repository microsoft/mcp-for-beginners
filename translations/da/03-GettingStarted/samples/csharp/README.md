# Grundlæggende Lommeregner MCP Service

Denne service tilbyder grundlæggende lommeregneroperationer gennem Model Context Protocol (MCP). Den er designet som et simpelt eksempel for begyndere, der lærer om MCP-implementeringer.

For mere information, se [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funktioner

Denne lommeregner-service tilbyder følgende kapabiliteter:

1. **Grundlæggende Regneoperationer**:
   - Addition af to tal
   - Subtraktion af et tal fra et andet
   - Multiplikation af to tal
   - Division af et tal med et andet (med nuldelingskontrol)

## Brug af `stdio` Type
  
## Konfiguration

1. **Konfigurer MCP Servere**:
   - Åbn dit arbejdsområde i VS Code.
   - Opret en `.vscode/mcp.json` fil i din arbejdsmappe for at konfigurere MCP servere. Eksempel på konfiguration:

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

   - Du vil blive bedt om at indtaste GitHub-arkivets rod, som kan hentes fra kommandoen, `git rev-parse --show-toplevel`.

## Brug af Servicen

Servicen eksponerer følgende API-endepunkter via MCP protokollen:

- `add(a, b)`: Læg to tal sammen
- `subtract(a, b)`: Træk det andet tal fra det første
- `multiply(a, b)`: Gang to tal
- `divide(a, b)`: Divider det første tal med det andet (med nul-kontrol)
- isPrime(n): Tjek om et tal er et primtal

## Test med Github Copilot Chat i VS Code

1. Prøv at lave en forespørgsel til servicen ved at bruge MCP protokollen. For eksempel kan du spørge:
   - "Læg 5 og 3 sammen"
   - "Træk 10 fra 4"
   - "Gange 6 og 7"
   - "Divider 8 med 2"
   - "Er 37854 et primtal?"
   - "Hvad er de 3 primtal før og efter 4242?"
2. For at sikre, at det bruger værktøjerne, tilføj #MyCalculator til prompten. For eksempel:
   - "Læg 5 og 3 sammen #MyCalculator"
   - "Træk 10 fra 4 #MyCalculator


## Containeriseret Version

Den tidligere løsning er god, når du har .NET SDK installeret, og alle afhængigheder er på plads. Men hvis du vil dele løsningen eller køre den i et andet miljø, kan du bruge den containeriserede version.

1. Start Docker og sørg for, at det kører.
1. Naviger fra en terminal til mappen `03-GettingStarted\samples\csharp\src` 
1. For at bygge Docker-billedet til lommeregnerservicen, kør følgende kommando (erstat `<YOUR-DOCKER-USERNAME>` med dit Docker Hub brugernavn):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Efter billedet er bygget, upload det til Docker Hub. Kør følgende kommando:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Brug den Dockeriserede Version

1. I `.vscode/mcp.json` filen, erstat serverkonfigurationen med følgende:
   ```json
    "mcp-calculator": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calculator"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Når du kigger på konfigurationen, kan du se, at kommandoen er `docker` og argumenterne er `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Flaget `--rm` sikrer, at containeren fjernes efter den stopper, og flaget `-i` tillader, at du interagerer med containerens standardinput. Det sidste argument er navnet på billedet, vi netop har bygget og uploadet til Docker Hub.

## Test den Dockeriserede Version

Start MCP Serveren ved at klikke på den lille Start-knap over `"mcp-calculator": {`, og ligesom før kan du bede lommeregner-servicen om at lave lidt matematik for dig.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->