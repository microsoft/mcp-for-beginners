# Calculator LLM Client

A Java application that demonstrates how to use LangChain4j to connect to an MCP (Model Context Protocol) calculator service with GitHub Models integration.

## Prerequisites

- Java 21 or higher
- Maven 3.6+ (or use the included Maven wrapper)
- A GitHub account with access to GitHub Models
- An MCP calculator service running on `http://localhost:8080`

## Getting the GitHub Token

This application uses GitHub Models which requires a GitHub personal access token. Follow these steps to get your token:

### 1. Access GitHub Models
1. Go to [GitHub Models](https://github.com/marketplace/models)
2. Sign in with your GitHub account
3. Request access to GitHub Models if you haven't already

### 2. Create a Personal Access Token
1. Go to [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Click "Generate new token" → "Generate new token (classic)"
3. Give your token a descriptive name (e.g., "MCP Calculator Client")
4. Set expiration as needed
5. Select the following scopes:
   - `repo` (if accessing private repositories)
   - `user:email`
6. Click "Generate token"
7. **Important**: Copy the token immediately - you won't be able to see it again!

### 3. Set the Environment Variable

#### On Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### On Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### On macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
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

3. **Set up the environment variable** (see "Getting the GitHub Token" section above)

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

1. **"GITHUB_TOKEN environment variable not set"**
   - Make sure you've set the `GITHUB_TOKEN` environment variable
   - Restart your terminal/command prompt after setting the variable

2. **"Connection refused to localhost:8080"**
   - Ensure the MCP calculator service is running on port 8080
   - Check if another service is using port 8080

3. **"Authentication failed"**
   - Verify your GitHub token is valid and has the correct permissions
   - Check if you have access to GitHub Models

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
- Use GitHub Models with the `gpt-4.1-nano` model
- Connect to MCP service at `http://localhost:8080/sse`
- Use a 60-second timeout for requests
- Enable request/response logging for debugging

## Dependencies

Key dependencies used in this project:
- **LangChain4j**: For AI integration and tool management
- **LangChain4j MCP**: For Model Context Protocol support
- **LangChain4j GitHub Models**: For GitHub Models integration
- **Spring Boot**: For application framework and dependency injection

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) file for details.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.