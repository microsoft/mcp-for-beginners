# Basic Calculator MCP Service

Dis service dey provide basic calculator operations wit di Model Context Protocol (MCP). E dey designed as simple example for people wey dey learn MCP implementations.

For more info, check [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Features

Dis calculator service get di following things wey e fit do:

1. **Basic Arithmetic Operations**:
   - Add two numbers together
   - Subtract one number from another
   - Multiply two numbers
   - Divide one number by another (e dey check if di second number na zero)

## Using `stdio` Type
  
## Configuration

1. **Set MCP Servers**:
   - Open your workspace for VS Code.
   - Create `.vscode/mcp.json` file for your workspace folder to set MCP servers. Example configuration:

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

   - You go need enter di GitHub repository root, wey you fit get from dis command, `git rev-parse --show-toplevel`.

## Using di Service

Di service dey provide di following API endpoints wit MCP protocol:

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract di second number from di first
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide di first number by di second (e dey check if di second number na zero)
- isPrime(n): Check if one number na prime

## Test wit Github Copilot Chat for VS Code

1. Try make request to di service wit MCP protocol. Example, you fit ask:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. To make sure say e dey use di tools, add #MyCalculator for di prompt. Example:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator


## Containerized Version

Di previous solution dey good if you get di .NET SDK installed and all di dependencies dey ready. But if you wan share di solution or run am for different environment, you fit use di containerized version.

1. Start Docker and make sure say e dey run.
1. From terminal, go to di folder `03-GettingStarted\samples\csharp\src` 
1. To build di Docker image for di calculator service, run dis command (replace `<YOUR-DOCKER-USERNAME>` wit your Docker Hub username):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. After di image don build, make we upload am go Docker Hub. Run dis command:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Use the Dockerized Version

1. In the `.vscode/mcp.json` file, replace the server configuration by the following:
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
   If you look di configuration, you go see say di command na `docker` and di args na `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Di `--rm` flag dey make sure say di container go remove after e stop, and di `-i` flag dey allow you interact wit di container standard input. Di last argument na di name of di image wey we just build and push go Docker Hub.

## Test di Dockerized Version

Start di MCP Server by clicking di small Start button wey dey above `"mcp-calc": {`, and just like before, you fit ask di calculator service to do some math for you.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->