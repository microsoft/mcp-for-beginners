# Basic Calculator MCP Service

Denna tjänst erbjuder grundläggande kalkylatoroperationer via Model Context Protocol (MCP). Den är utformad som ett enkelt exempel för nybörjare som vill lära sig om MCP-implementationer.

För mer information, se [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funktioner

Denna kalkylatortjänst erbjuder följande funktioner:

1. **Grundläggande aritmetiska operationer**:
   - Addition av två tal
   - Subtraktion av ett tal från ett annat
   - Multiplikation av två tal
   - Division av ett tal med ett annat (med kontroll för division med noll)

## Använda `stdio`-typen

## Konfiguration

1. **Konfigurera MCP-servrar**:
   - Öppna din arbetsyta i VS Code.
   - Skapa en fil `.vscode/mcp.json` i din arbetsmapp för att konfigurera MCP-servrar. Exempel på konfiguration:

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

   - Du kommer att bli ombedd att ange roten för GitHub-repositoriet, vilket kan hämtas med kommandot `git rev-parse --show-toplevel`.

## Använda tjänsten

Tjänsten exponerar följande API-endpoints via MCP-protokollet:

- `add(a, b)`: Lägg ihop två tal
- `subtract(a, b)`: Subtrahera det andra talet från det första
- `multiply(a, b)`: Multiplicera två tal
- `divide(a, b)`: Dividera det första talet med det andra (med kontroll för noll)
- isPrime(n): Kontrollera om ett tal är ett primtal

## Testa med Github Copilot Chat i VS Code

1. Prova att göra en förfrågan till tjänsten med MCP-protokollet. Till exempel kan du fråga:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. För att säkerställa att verktygen används, lägg till #MyCalculator i prompten. Till exempel:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Containeriserad version

Den tidigare lösningen är utmärkt när du har .NET SDK installerat och alla beroenden på plats. Men om du vill dela lösningen eller köra den i en annan miljö kan du använda den containeriserade versionen.

1. Starta Docker och se till att det körs.
1. Navigera i terminalen till mappen `03-GettingStarted\samples\csharp\src`
1. För att bygga Docker-imagen för kalkylatortjänsten, kör följande kommando (byt ut `<YOUR-DOCKER-USERNAME>` mot ditt Docker Hub-användarnamn):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. När imagen är byggd, ladda upp den till Docker Hub genom att köra följande kommando:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Använd den Dockeriserade versionen

1. I filen `.vscode/mcp.json`, ersätt serverkonfigurationen med följande:
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
   Om man tittar på konfigurationen ser du att kommandot är `docker` och argumenten är `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Flaggan `--rm` säkerställer att containern tas bort efter att den stoppats, och flaggan `-i` gör att du kan interagera med containerns standardinput. Det sista argumentet är namnet på imagen vi just byggde och pushade till Docker Hub.

## Testa den Dockeriserade versionen

Starta MCP-servern genom att klicka på den lilla Start-knappen ovanför `"mcp-calc": {`, och precis som tidigare kan du be kalkylatortjänsten göra lite matte åt dig.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.