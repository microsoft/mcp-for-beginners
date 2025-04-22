# Basic Calculator MCP Service

This service provides basic calculator operations through the Model Context Protocol (MCP). It's designed as a simple example for beginners learning about MCP implementations.

For more information, see [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Features

This calculator service offers the following capabilities:

1. **Basic Arithmetic Operations**:
   - Addition of two numbers
   - Subtraction of one number from another
   - Multiplication of two numbers
   - Division of one number by another (with zero division check)
  
## Configuration

1. **Configure MCP Servers**:
   - Open your workspace in VS Code.
   - Create a `.vscode/mcp.json` file in your workspace folder to configure MCP servers. Example configuration:
     ```json
     {
       "servers": {
         "MyCalculator": {
           "command": "dotnet",
           "args": [
                "run",
                "--project",
                "D:\\source\\03-GettingStarted\\samples\\csharp\\src\\calculator.csproj"
            ],
           "env": {}
         }
       }
     }
     ```
	- Replace the path with the path to your project. The path should be absolute and not relative to the workspace folder. (Example: D:\\gh\\mcp-for-beginners\\03-GettingStarted\\samples\\csharp\\src\\calculator.csproj)

## Using the Service

The service exposes the following API endpoints through the MCP protocol:

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract the second number from the first
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide the first number by the second (with zero check)

## Test with Github Copilot Chat in VS Code

1. Try making a request to the service using the MCP protocol. For example, you can ask:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
2. To make sure it's using the tools add #MyCalculator to the prompt. For example:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator