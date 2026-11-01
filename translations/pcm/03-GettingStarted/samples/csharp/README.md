# Simple Calculator MCP Service

Dis service dey provide basic calculator operations through the Model Context Protocol (MCP). E design as simple example for beginners wey dey learn about MCP implementations.

For more info, check [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Wetin Di Service Fit Do

Dis calculator service get di following things e fit do:

1. **Basic Arithmetic Operations**:
   - Addition of two numbers
   - Subtraction of one number from another
   - Multiplication of two numbers
   - Division of one number by another (with zero division check)

## Using `stdio` Type
  
## Configuration

1. **Configure MCP Servers**:
   - Open your workspace in VS Code.
   - Create a `.vscode/mcp.json` file in your workspace folder to configure MCP servers. Example configuration:

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

   - Dem go ask you to enter the GitHub repository root, wey you fit fetch from the command, `git rev-parse --show-toplevel`.

## Using the Service

Di service dey expose the following API endpoints through di MCP protocol:

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract the second number from the first
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide the first number by the second (with zero check)
- isPrime(n): Check if a number is prime

## Test with Github Copilot Chat in VS Code

1. Try make request to di service using di MCP protocol. For example, you fit ask:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. To make sure say e dey use di tools add #MyCalculator to the prompt. For example:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator


## Containerized Version

Di previous solution good if you don get di .NET SDK installed and all dependencies dey. But if you wan share di solution or run am for different environment, you fit use di containerized version.

1. Start Docker and make sure say e dey run.
1. From terminal, navigate into di folder `03-GettingStarted\samples\csharp\src` 
1. To build the Docker image for di calculator service, run di following command (replace `<YOUR-DOCKER-USERNAME>` with your Docker Hub username):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. After the image is built, make we upload am to Docker Hub. Run di following command:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Use the Dockerized Version

1. In the `.vscode/mcp.json` file, replace the server configuration with the following:
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
   When you look di configuration, you go see say di command na `docker` and di args na `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Di `--rm` flag make sure say di container go remove after e stop, and di `-i` flag allow you to interact with di container's standard input. Di last argument na di name of di image we just build and push to Docker Hub.

## Test the Dockerized Version

Start di MCP Server by clicking di small Start button above `"mcp-calculator": {`, and like before you fit ask di calculator service make e do some math for you.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->