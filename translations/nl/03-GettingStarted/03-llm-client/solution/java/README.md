# Calculator LLM Client

Een Java-applicatie die laat zien hoe je LangChain4j gebruikt om verbinding te maken met een MCP (Model Context Protocol) calculatorservice met integratie van GitHub Models.

## Vereisten

- Java 21 of hoger
- Maven 3.6+ (of gebruik de meegeleverde Maven wrapper)
- Een GitHub-account met toegang tot GitHub Models
- Een MCP calculatorservice die draait op `http://localhost:8080`

## Het verkrijgen van de GitHub Token

Deze applicatie gebruikt GitHub Models, waarvoor een persoonlijke toegangstoken van GitHub nodig is. Volg deze stappen om je token te krijgen:

### 1. Toegang krijgen tot GitHub Models
1. Ga naar [GitHub Models](https://github.com/marketplace/models)
2. Log in met je GitHub-account
3. Vraag toegang aan tot GitHub Models als je dat nog niet hebt gedaan

### 2. Maak een persoonlijke toegangstoken aan
1. Ga naar [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klik op "Generate new token" → "Generate new token (classic)"
3. Geef je token een duidelijke naam (bijv. "MCP Calculator Client")
4. Stel de vervaldatum in naar wens
5. Selecteer de volgende scopes:
   - `repo` (als je toegang nodig hebt tot private repositories)
   - `user:email`
6. Klik op "Generate token"
7. **Belangrijk**: Kopieer de token direct - je kunt hem later niet meer zien!

### 3. Stel de omgevingsvariabele in

#### Op Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Op Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Op macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Installatie en Setup

1. **Clone of navigeer naar de projectmap**

2. **Installeer de dependencies**:
   ```cmd
   mvnw clean install
   ```
   Of als je Maven globaal hebt geïnstalleerd:
   ```cmd
   mvn clean install
   ```

3. **Stel de omgevingsvariabele in** (zie de sectie "Het verkrijgen van de GitHub Token" hierboven)

4. **Start de MCP Calculator Service**:
   Zorg dat de MCP calculatorservice uit hoofdstuk 1 draait op `http://localhost:8080/sse`. Deze moet actief zijn voordat je de client start.

## De applicatie uitvoeren

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Wat de applicatie doet

De applicatie demonstreert drie hoofdinteracties met de calculatorservice:

1. **Optellen**: Berekenen van de som van 24,5 en 17,3
2. **Vierkantswortel**: Berekenen van de vierkantswortel van 144
3. **Help**: Toont beschikbare calculatorfuncties

## Verwachte output

Bij een succesvolle uitvoering zie je een output vergelijkbaar met:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Problemen oplossen

### Veelvoorkomende problemen

1. **"GITHUB_TOKEN environment variable not set"**
   - Controleer of je de `GITHUB_TOKEN` omgevingsvariabele hebt ingesteld
   - Herstart je terminal/command prompt nadat je de variabele hebt ingesteld

2. **"Connection refused to localhost:8080"**
   - Controleer of de MCP calculatorservice draait op poort 8080
   - Kijk of een andere service poort 8080 gebruikt

3. **"Authentication failed"**
   - Controleer of je GitHub-token geldig is en de juiste permissies heeft
   - Controleer of je toegang hebt tot GitHub Models

4. **Maven build fouten**
   - Zorg dat je Java 21 of hoger gebruikt: `java -version`
   - Probeer de build schoon te maken: `mvnw clean`

### Debuggen

Om debug-logging in te schakelen, voeg je het volgende JVM-argument toe bij het uitvoeren:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuratie

De applicatie is geconfigureerd om:
- GitHub Models te gebruiken met het model `gpt-4.1-nano`
- Verbinding te maken met de MCP-service op `http://localhost:8080/sse`
- Een timeout van 60 seconden te gebruiken voor verzoeken
- Request/response logging in te schakelen voor debugging

## Dependencies

Belangrijke dependencies die in dit project worden gebruikt:
- **LangChain4j**: Voor AI-integratie en toolbeheer
- **LangChain4j MCP**: Voor ondersteuning van Model Context Protocol
- **LangChain4j GitHub Models**: Voor integratie met GitHub Models
- **Spring Boot**: Voor het applicatiekader en dependency injection

## Licentie

Dit project is gelicenseerd onder de Apache License 2.0 - zie het [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) bestand voor details.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.