<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "882aae00f1d3f007e20d03b883f44afa",
  "translation_date": "2025-06-18T06:10:14+00:00",
  "source_file": "03-GettingStarted/samples/csharp/README.md",
  "language_code": "sl"
}
-->
# Osnovna kalkulator MCP storitev

Ta storitev omogoča osnovne kalkulatorske operacije preko Model Context Protocol (MCP). Namenjena je kot preprost primer za začetnike, ki se učijo o implementacijah MCP.

Za več informacij glejte [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funkcionalnosti

Ta kalkulatorska storitev ponuja naslednje zmogljivosti:

1. **Osnovne aritmetične operacije**:
   - Seštevanje dveh števil
   - Odštevanje enega števila od drugega
   - Množenje dveh števil
   - Deljenje enega števila z drugim (s preverjanjem deljenja z ničlo)

## Uporaba `stdio` tipa

## Konfiguracija

1. **Konfigurirajte MCP strežnike**:
   - Odprite svoj delovni prostor v VS Code.
   - Ustvarite `.vscode/mcp.json` datoteko v mapi delovnega prostora za konfiguracijo MCP strežnikov. Primer konfiguracije:

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

   - Pozvani boste, da vnesete koren GitHub repozitorija, ki ga lahko pridobite z ukazom, `git rev-parse --show-toplevel`.

## Using the Service

The service exposes the following API endpoints through the MCP protocol:

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract the second number from the first
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide the first number by the second (with zero check)
- isPrime(n): Check if a number is prime

## Test with Github Copilot Chat in VS Code

1. Try making a request to the service using the MCP protocol. For example, you can ask:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. To make sure it's using the tools add #MyCalculator to the prompt. For example:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator


## Containerized Version

The previous soultion is great when you have the .NET SDK installed, and all the dependencies are in place. However, if you would like to share the solution or run it in a different environment, you can use the containerized version.

1. Start Docker and make sure it's running.
1. From a terminal, navigate in the folder `03-GettingStarted\samples\csharp\src` 
1. To build the Docker image for the calculator service, execute the following command (replace `<YOUR-DOCKER-USERNAME>` z vašim uporabniškim imenom za Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Ko je slika zgrajena, jo naložimo na Docker Hub. Zaženite naslednji ukaz:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Uporaba dockerizirane različice

1. V datoteki `.vscode/mcp.json` zamenjajte konfiguracijo strežnika z naslednjo:
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
   Če pogledate konfiguracijo, boste videli, da je ukaz `docker` and the args are `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. The `--rm` flag ensures that the container is removed after it stops, and the `-i` flag allows you to interact with the container's standard input. The last argument is the name of the image we just built and pushed to Docker Hub.

## Test the Dockerized Version

Start the MCP Server by clicking the little Start button above `"mcp-calc": {`, in tako kot prej lahko prosite kalkulatorsko storitev, da za vas izvede nekaj računskih operacij.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.