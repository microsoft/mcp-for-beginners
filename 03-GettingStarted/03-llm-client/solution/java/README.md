# Calculator LLM Client

A Java application that demonstrates how to use LangChain4j to connect to an MCP (Model Context Protocol) calculator service through the MiniMax OpenAI-compatible API.

## Prerequisites

- Java 21 or higher
- Maven 3.6+ (or use the included Maven wrapper)
- A MiniMax API key
- An MCP calculator service running on `http://localhost:8080`

## Getting the API Key

This application uses the MiniMax OpenAI-compatible API. Follow these steps to get your key and endpoint:

### 1. Choose an endpoint
1. Use `https://api.minimax.io/v1` for the global endpoint
2. Use `https://api.minimaxi.com/v1` for the China endpoint

### 2. Create an API key
1. Create a MiniMax API key from your MiniMax account
2. Keep the key somewhere secure

### 3. Set the Environment Variables

#### On Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### On Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### On macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Setup and Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies**:
   ```cmd
   mvnw clean install
   ```
   Or if you have Maven installed globally:
   ```cmd
   mvn clean install
   ```

3. **Set up the environment variables** (see "Getting the API Key" section above)

4. **Start the MCP Calculator Service**:
   Make sure you have chapter 1's MCP calculator service running on `http://localhost:8080/sse`. This should be running before you start the client.

## Running the Application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## What the Application Does

The application demonstrates three main interactions with the calculator service:

1. **Addition**: Calculates the sum of 24.5 and 17.3
2. **Square Root**: Calculates the square root of 144
3. **Help**: Shows available calculator functions

## Expected Output

When running successfully, you should see output similar to:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY environment variable is not set"**
   - Make sure you've set the `OPENAI_API_KEY` environment variable
   - Restart your terminal/command prompt after setting the variable

2. **"Connection refused to localhost:8080"**
   - Ensure the MCP calculator service is running on port 8080
   - Check if another service is using port 8080

3. **"Authentication failed"**
   - Verify your API key is valid
   - Check that `OPENAI_BASE_URL` matches the endpoint you intended to use

4. **Maven build errors**
   - Ensure you're using Java 21 or higher: `java -version`
   - Try cleaning the build: `mvnw clean`

### Debugging

To enable debug logging, add the following JVM argument when running:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

The application is configured to:
- Use MiniMax-M3 by default; set `MINIMAX_MODEL_ID` to select either `MiniMax-M3` or `MiniMax-M2.7`
- Connect to `OPENAI_BASE_URL` when it is set; otherwise use `https://api.minimaxi.com/v1` when `MINIMAX_REGION=cn_zh`, or `https://api.minimax.io/v1` by default
- Connect to MCP service at `http://localhost:8080/sse`
- Use a 60-second timeout for requests

## Dependencies

Key dependencies used in this project:
- **LangChain4j**: For AI integration and tool management
- **LangChain4j MCP**: For Model Context Protocol support
- **LangChain4j OpenAI official**: For MiniMax OpenAI-compatible API integration
- **Spring Boot**: For application framework and dependency injection

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
