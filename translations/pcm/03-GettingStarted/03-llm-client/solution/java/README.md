# Calculator LLM Client

Na Java app wey dey show how to use LangChain4j take connect to MCP (Model Context Protocol) calculator service through MiniMax OpenAI-compatible API.

## Wetin You Need First

- Java 21 or pass am
- Maven 3.6+ (or use di Maven wrapper wey dey)
- MiniMax API key
- MCP calculator service dey run for `http://localhost:8080`

## How To Get API Key

Dis app dey use MiniMax OpenAI-compatible API. Follow dis steps to get your key and endpoint:

### 1. Choose endpoint
1. Use `https://api.minimax.io/v1` for global endpoint
2. Use `https://api.minimaxi.com/v1` for China endpoint

### 2. Create API key
1. Create MiniMax API key from your MiniMax account
2. Keep the key for safe place

### 3. Set Environment Variables

#### For Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### For Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### For macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Setup and How To Install

1. **Clone or waka enter project directory**

2. **Install dependencies**:
   ```cmd
   mvnw clean install
   ```
   Or if Maven dey installed globally:
   ```cmd
   mvn clean install
   ```

3. **Set environment variables** (check "How To Get API Key" part wey dey top)

4. **Start MCP Calculator Service**:
   Make sure say chapter 1 MCP calculator service dey run for `http://localhost:8080/sse`. E suppose dey run before you start client.

## How To Run Di App

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Wetin Di App Dey Do

Di app dey show three main ways to interact with calculator service:

1. **Addition**: Calculate sum of 24.5 and 17.3
2. **Square Root**: Calculate square root of 144
3. **Help**: Show di calculator functions wey dey available

## Wetin You Go See As Output

If e run well, you go see output wey be like:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## If Problem Show (Troubleshooting)

### Common Wahala

1. **"OPENAI_API_KEY environment variable never set"**
   - Make sure say you don set `OPENAI_API_KEY` environment variable
   - Restart your terminal/command prompt after you set am

2. **"Connection refuse to localhost:8080"**
   - Check say MCP calculator service dey run for port 8080
   - Check if another service dey use port 8080

3. **"Authentication fail"**
   - Make sure say your API key correct
   - Check say `OPENAI_BASE_URL` match the endpoint wey you wan use

4. **Maven build errors**
   - Make sure say you dey use Java 21 or pass: `java -version`
   - Try clean build: `mvnw clean`

### How To Debug

To enable debug logging, add dis JVM argument when you dey run:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

Di app configure to:
- Use MiniMax-M3 by default, or MiniMax-M2.7 if `MINIMAX_MODEL_ID` dey set
- Connect to `OPENAI_BASE_URL` if e set; else use `https://api.minimaxi.com/v1` if `MINIMAX_REGION=cn_zh`, or `https://api.minimax.io/v1` by default
- Connect to MCP service for `http://localhost:8080/sse`
- Use 60 seconds timeout for requests

## Dependencies

Main dependencies wey dis project dey use:
- **LangChain4j**: For AI integration and tool management
- **LangChain4j MCP**: For Model Context Protocol support
- **LangChain4j OpenAI official**: For MiniMax OpenAI-compatible API integration
- **Spring Boot**: For application framework and dependency injection

## License

Dis project get Apache License 2.0 - check [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) file for details.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->