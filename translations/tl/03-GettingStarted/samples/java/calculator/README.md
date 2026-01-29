# Basic Calculator MCP Service

Ang serbisyong ito ay nagbibigay ng mga pangunahing operasyon ng calculator gamit ang Model Context Protocol (MCP) sa pamamagitan ng Spring Boot na may WebFlux transport. Dinisenyo ito bilang isang simpleng halimbawa para sa mga nagsisimula na gustong matutunan ang tungkol sa mga implementasyon ng MCP.

Para sa karagdagang impormasyon, tingnan ang [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) na dokumentasyon.

## Overview

Ipinapakita ng serbisyo ang mga sumusunod:
- Suporta para sa SSE (Server-Sent Events)
- Awtomatikong pagrerehistro ng tool gamit ang `@Tool` annotation ng Spring AI
- Mga pangunahing function ng calculator:
  - Pagdaragdag, pagbabawas, pagpaparami, paghahati
  - Pagkalkula ng power at square root
  - Modulus (natitirang bahagi) at absolute value
  - Help function para sa mga paglalarawan ng operasyon

## Features

Nag-aalok ang calculator service na ito ng mga sumusunod na kakayahan:

1. **Pangunahing Operasyon sa Aritmetika**:
   - Pagdaragdag ng dalawang numero
   - Pagbabawas ng isang numero mula sa isa pa
   - Pagpaparami ng dalawang numero
   - Paghahati ng isang numero sa isa pa (may check sa paghahati sa zero)

2. **Mas Advanced na Operasyon**:
   - Pagkalkula ng power (pagtataas ng base sa exponent)
   - Pagkalkula ng square root (may check sa negatibong numero)
   - Pagkalkula ng modulus (natitirang bahagi)
   - Pagkalkula ng absolute value

3. **Sistema ng Tulong**:
   - Naka-built-in na help function na nagpapaliwanag sa lahat ng magagamit na operasyon

## Using the Service

Ipinapakita ng serbisyo ang mga sumusunod na API endpoints sa pamamagitan ng MCP protocol:

- `add(a, b)`: Pagdaragdag ng dalawang numero
- `subtract(a, b)`: Pagbabawas ng pangalawang numero mula sa una
- `multiply(a, b)`: Pagpaparami ng dalawang numero
- `divide(a, b)`: Paghahati ng unang numero sa pangalawa (may check sa zero)
- `power(base, exponent)`: Pagkalkula ng power ng isang numero
- `squareRoot(number)`: Pagkalkula ng square root (may check sa negatibong numero)
- `modulus(a, b)`: Pagkalkula ng natitirang bahagi sa paghahati
- `absolute(number)`: Pagkalkula ng absolute value
- `help()`: Pagkuha ng impormasyon tungkol sa mga magagamit na operasyon

## Test Client

May kasamang simpleng test client sa `com.microsoft.mcp.sample.client` package. Ipinapakita ng `SampleCalculatorClient` class ang mga magagamit na operasyon ng calculator service.

## Using the LangChain4j Client

Kasama sa proyekto ang isang LangChain4j example client sa `com.microsoft.mcp.sample.client.LangChain4jClient` na nagpapakita kung paano i-integrate ang calculator service sa LangChain4j at GitHub models:

### Prerequisites

1. **GitHub Token Setup**:
   
   Para magamit ang AI models ng GitHub (tulad ng phi-4), kailangan mo ng personal access token mula sa GitHub:

   a. Pumunta sa iyong GitHub account settings: https://github.com/settings/tokens
   
   b. I-click ang "Generate new token" → "Generate new token (classic)"
   
   c. Bigyan ng malinaw na pangalan ang iyong token
   
   d. Piliin ang mga sumusunod na scopes:
      - `repo` (Buong kontrol sa private repositories)
      - `read:org` (Basahin ang org at team membership, basahin ang org projects)
      - `gist` (Gumawa ng gists)
      - `user:email` (Access sa email address ng user (read-only))
   
   e. I-click ang "Generate token" at kopyahin ang bagong token
   
   f. I-set ito bilang environment variable:
      
      Sa Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      Sa macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Para sa permanenteng setup, idagdag ito sa iyong environment variables sa system settings

2. Idagdag ang LangChain4j GitHub dependency sa iyong proyekto (naka-include na sa pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Siguraduhing tumatakbo ang calculator server sa `localhost:8080`

### Running the LangChain4j Client

Ipinapakita ng halimbawa na ito:
- Pagkonekta sa calculator MCP server gamit ang SSE transport
- Paggamit ng LangChain4j para gumawa ng chat bot na gumagamit ng mga operasyon ng calculator
- Pag-integrate sa GitHub AI models (ngayon gamit ang phi-4 model)

Ipinapadala ng client ang mga sumusunod na sample queries para ipakita ang functionality:
1. Pagkalkula ng suma ng dalawang numero
2. Pagkuha ng square root ng isang numero
3. Pagkuha ng impormasyon tungkol sa mga magagamit na operasyon ng calculator

Patakbuhin ang halimbawa at tingnan ang output sa console para makita kung paano ginagamit ng AI model ang mga tool ng calculator sa pagsagot sa mga tanong.

### GitHub Model Configuration

Nakakonpigur ang LangChain4j client para gamitin ang GitHub phi-4 model na may mga sumusunod na settings:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Para gumamit ng ibang GitHub models, palitan lang ang `modelName` parameter sa isa pang suportadong modelo (halimbawa, "claude-3-haiku-20240307", "llama-3-70b-8192", atbp.).

## Dependencies

Kailangan ng proyekto ang mga sumusunod na pangunahing dependencies:

```xml
<!-- For MCP Server -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- For LangChain4j integration -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>${langchain4j.version}</version>
</dependency>

<!-- For GitHub models support -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-github</artifactId>
    <version>${langchain4j.version}</version>
</dependency>
```

## Building the Project

I-build ang proyekto gamit ang Maven:
```bash
./mvnw clean install -DskipTests
```

## Running the Server

### Using Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Using MCP Inspector

Ang MCP Inspector ay isang kapaki-pakinabang na tool para makipag-interact sa MCP services. Para gamitin ito sa calculator service na ito:

1. **I-install at patakbuhin ang MCP Inspector** sa bagong terminal window:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Buksan ang web UI** sa pamamagitan ng pag-click sa URL na ipinapakita ng app (karaniwang http://localhost:6274)

3. **I-configure ang koneksyon**:
   - Itakda ang transport type sa "SSE"
   - Itakda ang URL sa SSE endpoint ng iyong tumatakbong server: `http://localhost:8080/sse`
   - I-click ang "Connect"

4. **Gamitin ang mga tool**:
   - I-click ang "List Tools" para makita ang mga magagamit na operasyon ng calculator
   - Piliin ang isang tool at i-click ang "Run Tool" para isagawa ang operasyon

![MCP Inspector Screenshot](../../../../../../translated_images/tl/tool.c75a0b2380efcf1a47a8478f54380a36ddcca7943b98f56dabbac8b07e15c3bb.png)

### Using Docker

Kasama sa proyekto ang Dockerfile para sa containerized deployment:

1. **I-build ang Docker image**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Patakbuhin ang Docker container**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Ito ay:
- Magbuo ng multi-stage Docker image gamit ang Maven 3.9.9 at Eclipse Temurin 24 JDK
- Gumawa ng optimized container image
- I-expose ang serbisyo sa port 8080
- Simulan ang MCP calculator service sa loob ng container

Maaari mong ma-access ang serbisyo sa `http://localhost:8080` kapag tumatakbo na ang container.

## Troubleshooting

### Common Issues with GitHub Token

1. **Token Permission Issues**: Kung makakatanggap ka ng 403 Forbidden error, siguraduhing tama ang mga permiso ng token ayon sa mga nakasaad sa prerequisites.

2. **Token Not Found**: Kung makakatanggap ka ng "No API key found" error, tiyaking maayos na na-set ang GITHUB_TOKEN environment variable.

3. **Rate Limiting**: May limitasyon ang GitHub API sa dami ng request. Kung makaranas ng rate limit error (status code 429), maghintay ng ilang minuto bago subukang muli.

4. **Token Expiration**: Puwedeng mag-expire ang mga GitHub token. Kung makakatanggap ng authentication errors pagkatapos ng ilang panahon, gumawa ng bagong token at i-update ang iyong environment variable.

Kung kailangan mo pa ng tulong, tingnan ang [LangChain4j documentation](https://github.com/langchain4j/langchain4j) o [GitHub API documentation](https://docs.github.com/en/rest).

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.