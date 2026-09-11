# Calculator LLM Client

> [!NOTE]
> Deze oplossing maakt verbinding met de legacy HTTP+SSE calculatorservice van de cursus en
> richt zich op MCP `2025-11-25` SDK-API's. Het is geen `2026-07-28` Streamable HTTP
> voorbeeld.

Een Java-toepassing die demonstreert hoe LangChain4j te gebruiken om verbinding te maken met een MCP (Model Context Protocol) calculatorservice via de MiniMax OpenAI-compatibele API.

## Vereisten

- Java 21 of hoger
- Maven 3.6+ (of gebruik de meegeleverde Maven-wrapper)
- Een MiniMax API-sleutel
- Een MCP calculatorservice die draait op `http://localhost:8080`

## Het verkrijgen van de API-sleutel

Deze applicatie gebruikt de MiniMax OpenAI-compatibele API. Volg deze stappen om je sleutel en endpoint te verkrijgen:

### 1. Kies een endpoint
1. Gebruik `https://api.minimax.io/v1` voor het globale endpoint
2. Gebruik `https://api.minimaxi.com/v1` voor het China-endpoint

### 2. Maak een API-sleutel aan
1. Maak een MiniMax API-sleutel aan vanuit je MiniMax-account
2. Bewaar de sleutel op een veilige plaats

### 3. Stel de Omgevingsvariabelen in

#### Op Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Op Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Op macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Installatie en Configuratie

1. **Clone of navigeer naar de projectmap**

2. **Installeer dependencies**:
   ```cmd
   mvnw clean install
   ```
   Of als Maven globaal geïnstalleerd is:
   ```cmd
   mvn clean install
   ```

3. **Stel de omgevingsvariabelen in** (zie de sectie "Het verkrijgen van de API-sleutel" hierboven)

4. **Start de MCP Calculator Service**:
   Zorg dat je hoofdstuk 1's MCP calculatorservice hebt draaien op `http://localhost:8080/sse`. Deze moet actief zijn voordat je de client start.

## De applicatie uitvoeren

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Wat de Applicatie Doet

De applicatie demonstreert drie hoofdinteracties met de calculatorservice:

1. **Optellen**: Bereken de som van 24,5 en 17,3
2. **Vierkantswortel**: Bereken de vierkantswortel van 144
3. **Help**: Toont beschikbare calculatorfuncties

## Verwachte Uitvoer

Bij succesvol uitvoeren zou je een uitvoer moeten zien die lijkt op:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Problemen oplossen

### Veelvoorkomende problemen

1. **"OPENAI_API_KEY omgevingsvariabele is niet ingesteld"**
   - Zorg dat je de `OPENAI_API_KEY` omgevingsvariabele hebt ingesteld
   - Herstart je terminal/command prompt nadat je de variabele hebt ingesteld

2. **"Verbinding geweigerd naar localhost:8080"**
   - Controleer of de MCP calculatorservice draait op poort 8080
   - Controleer of een andere service poort 8080 niet al in gebruik heeft

3. **"Authenticatie mislukt"**
   - Controleer of je API-sleutel geldig is
   - Controleer dat `OPENAI_BASE_URL` overeenkomt met het endpoint dat je wilde gebruiken

4. **Maven build fouten**
   - Controleer dat je Java 21 of hoger gebruikt: `java -version`
   - Probeer de build schoon te maken: `mvnw clean`

### Debuggen

Om debug logging in te schakelen, voeg de volgende JVM-parameter toe bij het uitvoeren:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuratie

De applicatie is geconfigureerd om:
- Standaard MiniMax-M3 te gebruiken; stel `MINIMAX_MODEL_ID` in om te kiezen tussen `MiniMax-M3` of `MiniMax-M2.7`
- Verbinden met `OPENAI_BASE_URL` indien ingesteld; anders `https://api.minimaxi.com/v1` gebruiken wanneer `MINIMAX_REGION=cn_zh`, of standaard `https://api.minimax.io/v1`
- Verbinden met MCP-service op `http://localhost:8080/sse`
- Een timeout van 60 seconden gebruiken voor verzoeken

## Afhankelijkheden

Belangrijke afhankelijkheden gebruikt in dit project:
- **LangChain4j**: Voor AI-integratie en toolbeheer
- **LangChain4j MCP**: Voor Model Context Protocol-ondersteuning
- **LangChain4j OpenAI officieel**: Voor MiniMax OpenAI-compatibele API-integratie
- **Spring Boot**: Voor applicatiekader en dependency injection

## Licentie

Dit project is gelicenseerd onder de Apache License 2.0 - zie het [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) bestand voor details.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->