# Calculator LLM Client

Java app wey dey show how to use LangChain4j connect to MCP (Model Context Protocol) calculator service wey get GitHub Models integration.

## Wetin you go need

- Java 21 or higher
- Maven 3.6+ (or use the Maven wrapper wey dey inside)
- GitHub account wey get access to GitHub Models
- MCP calculator service wey dey run for `http://localhost:8080`

## How to get GitHub Token

Dis app dey use GitHub Models wey need GitHub personal access token. Follow dis steps to get your token:

### 1. Enter GitHub Models
1. Go [GitHub Models](https://github.com/marketplace/models)
2. Log in with your GitHub account
3. Request access to GitHub Models if you never get am before

### 2. Create Personal Access Token
1. Go [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Click "Generate new token" → "Generate new token (classic)"
3. Give your token better name (e.g., "MCP Calculator Client")
4. Set expiration as you want
5. Select dis scopes:
   - `repo` (if you dey access private repositories)
   - `user:email`
6. Click "Generate token"
7. **Important**: Copy the token quick - you no go fit see am again!

### 3. Set Environment Variable

#### For Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### For Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### For macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## How to Set Up and Install

1. **Clone or enter the project folder**

2. **Install dependencies**:
   ```cmd
   mvnw clean install
   ```
   Or if you don install Maven globally:
   ```cmd
   mvn clean install
   ```

3. **Set environment variable** (check "How to get GitHub Token" section above)

4. **Start MCP Calculator Service**:
   Make sure say chapter 1 MCP calculator service dey run for `http://localhost:8080/sse`. E suppose dey run before you start the client.

## How to Run the App

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Wetin the App Dey Do

Dis app dey show three main ways to interact with the calculator service:

1. **Addition**: E go calculate the sum of 24.5 and 17.3
2. **Square Root**: E go calculate the square root of 144
3. **Help**: E go show the calculator functions wey dey available

## Wetin You Go See for Output

If e run well, you go see output wey be like dis:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## How to Solve Problems

### Common Wahala

1. **"GITHUB_TOKEN environment variable not set"**
   - Make sure say you don set `GITHUB_TOKEN` environment variable
   - Restart your terminal/command prompt after you set the variable

2. **"Connection refused to localhost:8080"**
   - Make sure say MCP calculator service dey run for port 8080
   - Check if another service dey use port 8080

3. **"Authentication failed"**
   - Confirm say your GitHub token dey valid and e get correct permissions
   - Check if you get access to GitHub Models

4. **Maven build errors**
   - Make sure say you dey use Java 21 or higher: `java -version`
   - Try clean the build: `mvnw clean`

### Debugging

To enable debug logging, add dis JVM argument when you dey run:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

Dis app don configure to:
- Use GitHub Models with `gpt-4.1-nano` model
- Connect to MCP service for `http://localhost:8080/sse`
- Use 60 seconds timeout for requests
- Enable request/response logging for debugging

## Dependencies

Key dependencies wey dis project dey use:
- **LangChain4j**: For AI integration and tool management
- **LangChain4j MCP**: For Model Context Protocol support
- **LangChain4j GitHub Models**: For GitHub Models integration
- **Spring Boot**: For application framework and dependency injection

## License

Dis project dey under Apache License 2.0 - check [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) file for details.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important information, e good make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->