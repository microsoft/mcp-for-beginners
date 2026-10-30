# Basisrekenmachine MCP-service

Deze dienst biedt basisrekenmachinebewerkingen via het Model Context Protocol (MCP). Het is ontworpen als een eenvoudig voorbeeld voor beginners die leren over MCP-implementaties.

Voor meer informatie, zie [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Kenmerken

Deze rekenmachineservice biedt de volgende mogelijkheden:

1. **Basisrekenkundige bewerkingen**:
   - Optellen van twee getallen
   - Aftrekken van het ene getal van het andere
   - Vermenigvuldigen van twee getallen
   - Delen van het ene getal door het andere (met controle op deling door nul)

## Gebruik van `stdio` Type
  
## Configuratie

1. **Configureer MCP-servers**:
   - Open je werkruimte in VS Code.
   - Maak een `.vscode/mcp.json` bestand in je werkmap om MCP-servers te configureren. Voorbeeldconfiguratie:

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

   - Je wordt gevraagd de root van de GitHub-repository in te voeren, die opgehaald kan worden via het commando `git rev-parse --show-toplevel`.

## Gebruik van de Dienst

De dienst biedt de volgende API-eindpunten via het MCP-protocol:

- `add(a, b)`: Tel twee getallen bij elkaar op
- `subtract(a, b)`: Trek het tweede getal af van het eerste
- `multiply(a, b)`: Vermenigvuldig twee getallen
- `divide(a, b)`: Deel het eerste getal door het tweede (met nulcontrole)
- isPrime(n): Controleer of een getal een priemgetal is

## Test met Github Copilot Chat in VS Code

1. Probeer een verzoek naar de dienst te sturen via het MCP-protocol. Bijvoorbeeld, je kunt vragen:
   - "Tel 5 en 3 op"
   - "Trek 10 af van 4"
   - "Vermenigvuldig 6 en 7"
   - "Deel 8 door 2"
   - "Is 37854 een priemgetal?"
   - "Wat zijn de 3 priemgetallen vóór en na 4242?"
2. Om ervoor te zorgen dat het de tools gebruikt, voeg #MyCalculator toe aan de prompt. Bijvoorbeeld:
   - "Tel 5 en 3 op #MyCalculator"
   - "Trek 10 af van 4 #MyCalculator


## Gecontaineriseerde Versie

De vorige oplossing is prima als je de .NET SDK geïnstalleerd hebt en alle afhankelijkheden aanwezig zijn. Als je de oplossing echter wilt delen of in een andere omgeving wilt uitvoeren, kun je de gecontaineriseerde versie gebruiken.

1. Start Docker en zorg dat het draait.
1. Navigeer vanuit een terminal naar de map `03-GettingStarted\samples\csharp\src` 
1. Om de Docker-image voor de rekenmachineservice te bouwen, voer je het volgende commando uit (vervang `<YOUR-DOCKER-USERNAME>` door je Docker Hub-gebruikersnaam):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Nadat de image is gebouwd, uploaden we die naar Docker Hub. Voer het volgende commando uit:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Gebruik de Dockerized Versie

1. Vervang in het `.vscode/mcp.json` bestand de serverconfiguratie door het volgende:
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
   Kijken we naar de configuratie, dan zie je dat het commando `docker` is en de args `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. De `--rm` vlag zorgt ervoor dat de container wordt verwijderd nadat die stopt, en de `-i` vlag maakt het mogelijk om met de standaardinvoer van de container te communiceren. Het laatste argument is de naam van de image die we zojuist hebben gebouwd en naar Docker Hub hebben gepusht.

## Test de Dockerized Versie

Start de MCP Server door op de kleine startknop boven `"mcp-calculator": {` te klikken, en net als eerder kun je de rekenmachineservice vragen om wat wiskunde voor je te doen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->