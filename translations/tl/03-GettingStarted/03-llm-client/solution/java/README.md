# Calculator LLM Client

Isang Java application na nagpapakita kung paano gamitin ang LangChain4j para kumonekta sa isang MCP (Model Context Protocol) calculator service na may GitHub Models integration.

## Prerequisites

- Java 21 o mas mataas
- Maven 3.6+ (o gamitin ang kasama na Maven wrapper)
- Isang GitHub account na may access sa GitHub Models
- Isang MCP calculator service na tumatakbo sa `http://localhost:8080`

## Getting the GitHub Token

Gumagamit ang application na ito ng GitHub Models na nangangailangan ng GitHub personal access token. Sundin ang mga hakbang na ito para makuha ang iyong token:

### 1. Access GitHub Models
1. Pumunta sa [GitHub Models](https://github.com/marketplace/models)
2. Mag-sign in gamit ang iyong GitHub account
3. Humiling ng access sa GitHub Models kung hindi ka pa nakakuha

### 2. Create a Personal Access Token
1. Pumunta sa [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. I-click ang "Generate new token" → "Generate new token (classic)"
3. Bigyan ang iyong token ng malinaw na pangalan (hal., "MCP Calculator Client")
4. Itakda ang expiration kung kinakailangan
5. Piliin ang mga sumusunod na scopes:
   - `repo` (kung aakses ang private repositories)
   - `user:email`
6. I-click ang "Generate token"
7. **Mahalaga**: Kopyahin agad ang token - hindi mo na ito makikita muli!

### 3. Set the Environment Variable

#### Sa Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Sa Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Sa macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Setup and Installation

1. **I-clone o pumunta sa project directory**

2. **I-install ang mga dependencies**:
   ```cmd
   mvnw clean install
   ```
   O kung naka-install ang Maven globally:
   ```cmd
   mvn clean install
   ```

3. **I-set up ang environment variable** (tingnan ang seksyon na "Getting the GitHub Token" sa itaas)

4. **Simulan ang MCP Calculator Service**:
   Siguraduhing tumatakbo ang MCP calculator service mula sa chapter 1 sa `http://localhost:8080/sse`. Dapat ito ay tumatakbo bago simulan ang client.

## Running the Application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ano ang Ginagawa ng Application

Ipinapakita ng application ang tatlong pangunahing interaksyon sa calculator service:

1. **Addition**: Kinakalkula ang kabuuan ng 24.5 at 17.3
2. **Square Root**: Kinakalkula ang square root ng 144
3. **Help**: Ipinapakita ang mga available na calculator functions

## Expected Output

Kapag matagumpay na tumakbo, makikita mo ang output na katulad ng:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Troubleshooting

### Karaniwang Problema

1. **"GITHUB_TOKEN environment variable not set"**
   - Siguraduhing na-set mo ang `GITHUB_TOKEN` environment variable
   - I-restart ang terminal/command prompt pagkatapos i-set ang variable

2. **"Connection refused to localhost:8080"**
   - Siguraduhing tumatakbo ang MCP calculator service sa port 8080
   - Tingnan kung may ibang serbisyo na gumagamit ng port 8080

3. **"Authentication failed"**
   - Siguraduhing valid ang iyong GitHub token at may tamang permissions
   - Tingnan kung may access ka sa GitHub Models

4. **Maven build errors**
   - Siguraduhing gumagamit ka ng Java 21 o mas mataas: `java -version`
   - Subukang i-clean ang build: `mvnw clean`

### Debugging

Para paganahin ang debug logging, idagdag ang sumusunod na JVM argument kapag nagpapatakbo:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuration

Nakakonpigura ang application para:
- Gamitin ang GitHub Models gamit ang `gpt-4.1-nano` model
- Kumonekta sa MCP service sa `http://localhost:8080/sse`
- Gumamit ng 60-segundong timeout para sa mga request
- Paganahin ang request/response logging para sa debugging

## Dependencies

Pangunahing dependencies na ginamit sa proyektong ito:
- **LangChain4j**: Para sa AI integration at tool management
- **LangChain4j MCP**: Para sa Model Context Protocol support
- **LangChain4j GitHub Models**: Para sa GitHub Models integration
- **Spring Boot**: Para sa application framework at dependency injection

## License

Ang proyektong ito ay lisensyado sa ilalim ng Apache License 2.0 - tingnan ang [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) file para sa mga detalye.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.