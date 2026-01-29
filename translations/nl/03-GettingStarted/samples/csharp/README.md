# Basic Calculator MCP Service

Deze service biedt basisrekenkundige bewerkingen via het Model Context Protocol (MCP). Het is ontworpen als een eenvoudig voorbeeld voor beginners die MCP-implementaties leren.

Voor meer informatie, zie [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Functies

Deze calculatorservice biedt de volgende mogelijkheden:

1. **Basisrekenkundige bewerkingen**:
   - Optellen van twee getallen
   - Aftrekken van het ene getal van het andere
   - Vermenigvuldigen van twee getallen
   - Delen van het ene getal door het andere (met controle op deling door nul)

## Gebruik van het `stdio` type
  
## Configuratie

1. **Configureer MCP-servers**:
   - Open je werkruimte in VS Code.
   - Maak een `.vscode/mcp.json` bestand aan in je werkmap om MCP-servers te configureren. Voorbeeldconfiguratie:

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

   - Je wordt gevraagd om de root van de GitHub-repository in te voeren, die je kunt ophalen met het commando `git rev-parse --show-toplevel`.

## Gebruik van de Service

De service biedt de volgende API-eindpunten via het MCP-protocol:

- `add(a, b)`: Tel twee getallen bij elkaar op
- `subtract(a, b)`: Trek het tweede getal af van het eerste
- `multiply(a, b)`: Vermenigvuldig twee getallen
- `divide(a, b)`: Deel het eerste getal door het tweede (met controle op nul)
- isPrime(n): Controleer of een getal een priemgetal is

## Test met Github Copilot Chat in VS Code

1. Probeer een verzoek te doen aan de service via het MCP-protocol. Bijvoorbeeld, je kunt vragen:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Om zeker te zijn dat de tools worden gebruikt, voeg #MyCalculator toe aan de prompt. Bijvoorbeeld:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Containerized Versie

De vorige oplossing is ideaal als je de .NET SDK hebt geïnstalleerd en alle afhankelijkheden aanwezig zijn. Maar als je de oplossing wilt delen of in een andere omgeving wilt draaien, kun je de containerized versie gebruiken.

1. Start Docker en zorg dat het draait.
1. Navigeer in een terminal naar de map `03-GettingStarted\samples\csharp\src`
1. Om de Docker-image voor de calculatorservice te bouwen, voer je het volgende commando uit (vervang `<YOUR-DOCKER-USERNAME>` door je Docker Hub gebruikersnaam):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Nadat de image is gebouwd, uploaden we deze naar Docker Hub. Voer het volgende commando uit:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Gebruik de Dockerized Versie

1. Vervang in het `.vscode/mcp.json` bestand de serverconfiguratie door het volgende:
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
   Als je naar de configuratie kijkt, zie je dat het commando `docker` is en de argumenten `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. De `--rm` vlag zorgt ervoor dat de container wordt verwijderd nadat deze stopt, en de `-i` vlag maakt interactie met de standaardinvoer van de container mogelijk. Het laatste argument is de naam van de image die we zojuist hebben gebouwd en naar Docker Hub hebben gepusht.

## Test de Dockerized Versie

Start de MCP Server door op de kleine Start-knop boven `"mcp-calc": {` te klikken, en net als eerder kun je de calculatorservice vragen om wat rekenwerk voor je te doen.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.