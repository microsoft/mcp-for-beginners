# Calculator LLM Client

> [!NOTE]
> Dis solution dey connect to di course legacy HTTP+SSE calculator service an
> e dey target MCP `2025-11-25` SDK APIs. E no be `2026-07-28` Streamable HTTP
> example.

Java application wey dey show how to use LangChain4j take connect MCP (Model Context Protocol) calculator service through di MiniMax OpenAI-compatible API.

## Prerequisites

- Java 21 or higher
- Maven 3.6+ (or use di included Maven wrapper)
- MiniMax API key
- MCP calculator service wey dey run for `http://localhost:8080`

## How to Get the API Key

Dis application dey use MiniMax OpenAI-compatible API. Follow dis steps to get your key an endpoint:

### 1. Choose di endpoint
1. Use `https://api.minimax.io/v1` for di global endpoint
2. Use `https://api.minimaxi.com/v1` for di China endpoint

### 2. Create API key
1. Make MiniMax API key from your MiniMax account
2. Keep di key somewhere wey safe

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

## Setup and Installation

1. **Clone or waka go di project directory**

2. **Install dependencies**:
   ```cmd
   mvnw clean install
   ```
   Or if you get Maven installed globally:
   ```cmd
   mvn clean install
   ```

3. **Setup environment variables** (see di "Getting the API Key" section above)

4. **Start di MCP Calculator Service**:
   Make sure sey di chapter 1 MCP calculator service dey run for `http://localhost:8080/sse`. E suppose dey run before you start di client.

## How to Run di Application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Wetin di Application Dey Do

Di application go show three main things wey e fit do with di calculator service:

1. **Addition**: E go calculate sum of 24.5 and 17.3
2. **Square Root**: E go calculate di square root of 144
3. **Help**: E go show di calculator functions wey dey available

## Wetin You Go See as Output

When e run well, you suppose see output like dis:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Troubleshooting

### Common Wahala

1. **"OPENAI_API_KEY environment variable no dey set"**
   - Make sure sey you don set di `OPENAI_API_KEY` environment variable
   - Restart your terminal/command prompt after you don set di variable

2. **"Connection refused to localhost:8080"**
   - Make sure di MCP calculator service dey run for port 8080
   - Check if another service dey use port 8080

3. **"Authentication failed"**
   - Check if your API key valid
   - Make sure say `OPENAI_BASE_URL` match di endpoint wey you mean to use

4. **Maven build errors**
   - Make sure you dey use Java 21 or pass: `java -version`
   - Try cleaning di build: `mvnw clean`

### Debugging

To enable debug logging, add dis JVM argument when you dey run:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

Di application dey configured to:
- Use MiniMax-M3 as default; set `MINIMAX_MODEL_ID` to choose whether `MiniMax-M3` or `MiniMax-M2.7`
- Connect to `OPENAI_BASE_URL` if e set; otherwise use `https://api.minimaxi.com/v1` if `MINIMAX_REGION=cn_zh`, or `https://api.minimax.io/v1` as default
- Connect to MCP service for `http://localhost:8080/sse`
- Use 60 seconds timeout for requests

## Dependencies

Main dependencies wey dis project use:
- **LangChain4j**: For AI integration an tool management
- **LangChain4j MCP**: For Model Context Protocol support
- **LangChain4j OpenAI official**: For MiniMax OpenAI-compatible API integration
- **Spring Boot**: For application framework and dependency injection

## License

Dis project dey licensed under Apache License 2.0 - check [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) file for details.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->