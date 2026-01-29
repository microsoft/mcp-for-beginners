# Basic Calculator MCP Service

Deze service biedt basisrekenkundige bewerkingen via het Model Context Protocol (MCP) met Spring Boot en WebFlux transport. Het is ontworpen als een eenvoudig voorbeeld voor beginners die MCP-implementaties willen leren.

Voor meer informatie, zie de [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) referentiedocumentatie.

## Overzicht

De service laat zien:
- Ondersteuning voor SSE (Server-Sent Events)
- Automatische tool-registratie met de `@Tool` annotatie van Spring AI
- Basis calculatorfuncties:
  - Optellen, aftrekken, vermenigvuldigen, delen
  - Machtsverheffen en worteltrekken
  - Modulus (rest) en absolute waarde
  - Helpfunctie voor beschrijvingen van bewerkingen

## Functies

Deze calculator service biedt de volgende mogelijkheden:

1. **Basisrekenkundige bewerkingen**:
   - Optellen van twee getallen
   - Aftrekken van het ene getal van het andere
   - Vermenigvuldigen van twee getallen
   - Delen van het ene getal door het andere (met controle op delen door nul)

2. **Geavanceerde bewerkingen**:
   - Machtsverheffen (basis tot exponent)
   - Worteltrekken (met controle op negatieve getallen)
   - Modulus (rest) berekening
   - Absolute waarde berekening

3. **Helpsysteem**:
   - Ingebouwde helpfunctie die alle beschikbare bewerkingen uitlegt

## Gebruik van de Service

De service biedt de volgende API-eindpunten via het MCP-protocol:

- `add(a, b)`: Tel twee getallen bij elkaar op
- `subtract(a, b)`: Trek het tweede getal af van het eerste
- `multiply(a, b)`: Vermenigvuldig twee getallen
- `divide(a, b)`: Deel het eerste getal door het tweede (met controle op nul)
- `power(base, exponent)`: Bereken de macht van een getal
- `squareRoot(number)`: Bereken de wortel (met controle op negatieve getallen)
- `modulus(a, b)`: Bereken de rest bij deling
- `absolute(number)`: Bereken de absolute waarde
- `help()`: Verkrijg informatie over beschikbare bewerkingen

## Test Client

Een eenvoudige testclient is opgenomen in het pakket `com.microsoft.mcp.sample.client`. De klasse `SampleCalculatorClient` toont de beschikbare bewerkingen van de calculator service.

## Gebruik van de LangChain4j Client

Het project bevat een LangChain4j voorbeeldclient in `com.microsoft.mcp.sample.client.LangChain4jClient` die laat zien hoe je de calculator service integreert met LangChain4j en GitHub-modellen:

### Vereisten

1. **GitHub Token Instellen**:
   
   Om de AI-modellen van GitHub (zoals phi-4) te gebruiken, heb je een persoonlijke toegangstoken van GitHub nodig:

   a. Ga naar je GitHub accountinstellingen: https://github.com/settings/tokens
   
   b. Klik op "Generate new token" → "Generate new token (classic)"
   
   c. Geef je token een duidelijke naam
   
   d. Selecteer de volgende scopes:
      - `repo` (Volledige controle over privé repositories)
      - `read:org` (Lezen van organisatie- en teamlidmaatschappen, lezen van organisatieprojecten)
      - `gist` (Gists aanmaken)
      - `user:email` (Toegang tot e-mailadressen van gebruikers (alleen lezen))
   
   e. Klik op "Generate token" en kopieer je nieuwe token
   
   f. Stel het in als een omgevingsvariabele:
      
      Op Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      Op macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Voor een blijvende instelling, voeg het toe aan je omgevingsvariabelen via de systeeminstellingen

2. Voeg de LangChain4j GitHub dependency toe aan je project (al opgenomen in pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Zorg dat de calculator server draait op `localhost:8080`

### LangChain4j Client Uitvoeren

Dit voorbeeld laat zien:
- Verbinden met de calculator MCP server via SSE transport
- Gebruik van LangChain4j om een chatbot te maken die calculatorbewerkingen gebruikt
- Integratie met GitHub AI-modellen (nu met het phi-4 model)

De client verstuurt de volgende voorbeeldvragen om de functionaliteit te demonstreren:
1. De som van twee getallen berekenen
2. De wortel van een getal vinden
3. Hulpinformatie opvragen over beschikbare calculatorbewerkingen

Voer het voorbeeld uit en bekijk de console-uitvoer om te zien hoe het AI-model de calculator-tools gebruikt om te antwoorden.

### GitHub Modelconfiguratie

De LangChain4j client is geconfigureerd om het phi-4 model van GitHub te gebruiken met de volgende instellingen:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Om andere GitHub-modellen te gebruiken, wijzig je eenvoudig de `modelName` parameter naar een ander ondersteund model (bijv. "claude-3-haiku-20240307", "llama-3-70b-8192", enz.).

## Afhankelijkheden

Het project vereist de volgende belangrijke afhankelijkheden:

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

## Project Bouwen

Bouw het project met Maven:
```bash
./mvnw clean install -DskipTests
```

## Server Starten

### Met Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Met MCP Inspector

De MCP Inspector is een handig hulpmiddel om met MCP-services te werken. Om het te gebruiken met deze calculator service:

1. **Installeer en start MCP Inspector** in een nieuw terminalvenster:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Open de webinterface** door te klikken op de URL die de app toont (meestal http://localhost:6274)

3. **Configureer de verbinding**:
   - Stel het transporttype in op "SSE"
   - Stel de URL in op de SSE-eindpunt van je draaiende server: `http://localhost:8080/sse`
   - Klik op "Connect"

4. **Gebruik de tools**:
   - Klik op "List Tools" om beschikbare calculatorbewerkingen te zien
   - Selecteer een tool en klik op "Run Tool" om een bewerking uit te voeren

![MCP Inspector Screenshot](../../../../../../translated_images/nl/tool.c75a0b2380efcf1a47a8478f54380a36ddcca7943b98f56dabbac8b07e15c3bb.png)

### Met Docker

Het project bevat een Dockerfile voor containerized deployment:

1. **Bouw de Docker image**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Start de Docker container**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Dit zal:
- Een multi-stage Docker image bouwen met Maven 3.9.9 en Eclipse Temurin 24 JDK
- Een geoptimaliseerde container image creëren
- De service beschikbaar maken op poort 8080
- De MCP calculator service binnen de container starten

Je kunt de service bereiken via `http://localhost:8080` zodra de container draait.

## Problemen Oplossen

### Veelvoorkomende problemen met GitHub Token

1. **Token permissieproblemen**: Als je een 403 Forbidden fout krijgt, controleer dan of je token de juiste permissies heeft zoals beschreven in de vereisten.

2. **Token niet gevonden**: Als je de foutmelding "No API key found" krijgt, zorg dan dat de GITHUB_TOKEN omgevingsvariabele correct is ingesteld.

3. **Rate limiting**: De GitHub API heeft limieten. Als je een rate limit fout (statuscode 429) krijgt, wacht dan een paar minuten en probeer het opnieuw.

4. **Token verlopen**: GitHub tokens kunnen verlopen. Als je na enige tijd authenticatiefouten krijgt, genereer dan een nieuw token en werk je omgevingsvariabele bij.

Als je verdere hulp nodig hebt, raadpleeg dan de [LangChain4j documentatie](https://github.com/langchain4j/langchain4j) of de [GitHub API documentatie](https://docs.github.com/en/rest).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.