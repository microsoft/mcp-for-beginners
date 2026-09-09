# Calculator LLM-klient

En Java-applikation som demonstrerar hur man använder LangChain4j för att ansluta till en MCP (Model Context Protocol) kalkylatortjänst via MiniMax OpenAI-kompatibla API.

## Förutsättningar

- Java 21 eller högre
- Maven 3.6+ (eller använd medföljande Maven wrapper)
- En MiniMax API-nyckel
- En MCP kalkylatortjänst som körs på `http://localhost:8080`

## Skaffa API-nyckeln

Den här applikationen använder MiniMax OpenAI-kompatibla API. Följ dessa steg för att få din nyckel och endpoint:

### 1. Välj en endpoint
1. Använd `https://api.minimax.io/v1` för global endpoint
2. Använd `https://api.minimaxi.com/v1` för Kina-endpoint

### 2. Skapa en API-nyckel
1. Skapa en MiniMax API-nyckel från ditt MiniMax-konto
2. Spara nyckeln på en säker plats

### 3. Ställ in miljövariablerna

#### På Windows (Kommandotolk):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### På Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### På macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Installation och konfiguration

1. **Klona eller navigera till projektmappen**

2. **Installera beroenden**:
   ```cmd
   mvnw clean install
   ```
   Eller om du har Maven installerat globalt:
   ```cmd
   mvn clean install
   ```

3. **Ställ in miljövariablerna** (se avsnittet "Skaffa API-nyckeln" ovan)

4. **Starta MCP kalkylatortjänsten**:
   Se till att du har kapitel 1:s MCP kalkylatortjänst igång på `http://localhost:8080/sse`. Den ska köras innan klienten startar.

## Köra applikationen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Vad applikationen gör

Applikationen demonstrerar tre huvudsakliga interaktioner med kalkylatortjänsten:

1. **Addition**: Beräknar summan av 24.5 och 17.3
2. **Kvadratrot**: Beräknar kvadratroten av 144
3. **Hjälp**: Visar tillgängliga kalkylatorfunktioner

## Förväntad utdata

Vid lyckad körning bör du se output liknande:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Felsökning

### Vanliga problem

1. **"OPENAI_API_KEY miljövariabel är inte satt"**
   - Kontrollera att du har satt miljövariabeln `OPENAI_API_KEY`
   - Starta om terminalen/kommandotolken efter att du satt variabeln

2. **"Connection refused to localhost:8080"**
   - Säkerställ att MCP kalkylatortjänsten körs på port 8080
   - Kontrollera om en annan tjänst använder port 8080

3. **"Autentisering misslyckades"**
   - Verifiera att din API-nyckel är giltig
   - Kontrollera att `OPENAI_BASE_URL` stämmer överens med den endpoint du tänkt använda

4. **Maven build-fel**
   - Kontrollera att du använder Java 21 eller högre: `java -version`
   - Försök att göra en ren build: `mvnw clean`

### Debugging

För att aktivera debug-loggning, lägg till följande JVM-argument vid körning:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguration

Applikationen är konfigurerad för att:
- Använda MiniMax-M3 som standard, eller MiniMax-M2.7 när `MINIMAX_MODEL_ID` är satt
- Ansluta till `OPENAI_BASE_URL` när den är satt; annars använda `https://api.minimaxi.com/v1` när `MINIMAX_REGION=cn_zh`, eller `https://api.minimax.io/v1` som standard
- Ansluta till MCP-tjänsten på `http://localhost:8080/sse`
- Använda en timeout på 60 sekunder för förfrågningar

## Beroenden

Nyckelberoenden som används i detta projekt:
- **LangChain4j**: För AI-integration och verktygshantering
- **LangChain4j MCP**: För stöd av Model Context Protocol
- **LangChain4j OpenAI official**: För MiniMax OpenAI-kompatibel API-integration
- **Spring Boot**: För applikationsramverk och dependency injection

## Licens

Detta projekt är licensierat under Apache License 2.0 - se [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE)-filen för detaljer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->