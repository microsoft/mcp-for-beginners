# Calculator LLM Client

Java application wey dey show how to use LangChain4j to connect to MCP (Model Context Protocol) calculator service through MiniMax OpenAI-compatible API.

## Wetin You Need Before

- Java 21 or pass am
- Maven 3.6+ (or fit use di Maven wrapper wey dey inside)
- MiniMax API key
- MCP calculator service wey dey run for `http://localhost:8080`

## How To Get di API Key

Dis application dey use MiniMax OpenAI-compatible API. Follow dis steps to get your key and endpoint:

### 1. Pick endpoint
1. Use `https://api.minimax.io/v1` for global endpoint
2. Use `https://api.minimaxi.com/v1` for China endpoint

### 2. Create API key
1. Create MiniMax API key from your MiniMax account
2. Keep your key for somewhere wey safe

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

## How To Setup and Install

1. **Clone or go enter the project directory**

2. **Install dependencies**:
   ```cmd
   mvnw clean install
   ```
   Or if you get Maven globally installed:
   ```cmd
   mvn clean install
   ```

3. **Set di environment variables** (check "How To Get di API Key" section above)

4. **Start di MCP Calculator Service**:
   Make sure say di chapter 1 MCP calculator service dey run for `http://localhost:8080/sse`. E suppose dey run before you start the client.

## How To Run di Application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Wetin di Application Dey Do

Di application dey show three main ways to take interact with di calculator service:

1. **Addition**: Calculate the sum of 24.5 and 17.3
2. **Square Root**: Calculate square root of 144
3. **Help**: Show all di calculator functions wey dey available

## Wetin You Go Expect as Output

When e run well, you go see output wey resemble dis one:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## How To Solve Wahala

### Wahala wey dey happen often

1. **"OPENAI_API_KEY environment variable no set"**
   - Make sure say you don set `OPENAI_API_KEY` environment variable
   - Restart your terminal/command prompt after you set am

2. **"Connection refuse localhost:8080"**
   - Confirm say MCP calculator service dey run for port 8080
   - Check if another service no dey use port 8080

3. **"Authentication failed"**
   - Confirm say your API key dey correct
   - Check say `OPENAI_BASE_URL` match di endpoint wey you suppose use

4. **Maven build errors**
   - Confirm say you dey use Java 21 or above: `java -version`
   - Try clean di build: `mvnw clean`

### How To Debug

To enable debug logging, add dis JVM argument wen you dey run am:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

Di application don set to:
- Use MiniMax-M3 as default; fit set `MINIMAX_MODEL_ID` to choose either `MiniMax-M3` or `MiniMax-M2.7`
- Connect to `OPENAI_BASE_URL` if e set; otherwise use `https://api.minimaxi.com/v1` if `MINIMAX_REGION=cn_zh`, or `https://api.minimax.io/v1` as default
- Connect to MCP service for `http://localhost:8080/sse`
- Use 60 seconds timeout for requests

## Dependencies

Important dependencies wey this project dey use:
- **LangChain4j**: For AI integration and tool management
- **LangChain4j MCP**: For Model Context Protocol support
- **LangChain4j OpenAI official**: For MiniMax OpenAI-compatible API integration
- **Spring Boot**: For app framework and dependency injection

## License

Dis project get license under Apache License 2.0 - see di [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) file for more details.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->