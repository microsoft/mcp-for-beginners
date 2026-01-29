# Calculator LLM Client

En Java-applikation som visar hur man använder LangChain4j för att ansluta till en MCP (Model Context Protocol) kalkylatortjänst med GitHub Models-integration.

## Förutsättningar

- Java 21 eller högre
- Maven 3.6+ (eller använd den medföljande Maven-wrappern)
- Ett GitHub-konto med tillgång till GitHub Models
- En MCP kalkylatortjänst som körs på `http://localhost:8080`

## Skaffa GitHub-token

Denna applikation använder GitHub Models som kräver en personlig åtkomsttoken från GitHub. Följ dessa steg för att få din token:

### 1. Gå till GitHub Models
1. Besök [GitHub Models](https://github.com/marketplace/models)
2. Logga in med ditt GitHub-konto
3. Begär åtkomst till GitHub Models om du inte redan har det

### 2. Skapa en personlig åtkomsttoken
1. Gå till [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klicka på "Generate new token" → "Generate new token (classic)"
3. Ge din token ett beskrivande namn (t.ex. "MCP Calculator Client")
4. Ställ in utgångsdatum efter behov
5. Välj följande scopes:
   - `repo` (om du behöver åtkomst till privata repositories)
   - `user:email`
6. Klicka på "Generate token"
7. **Viktigt**: Kopiera token direkt – du kommer inte kunna se den igen!

### 3. Sätt miljövariabeln

#### På Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### På Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### På macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Installation och uppsättning

1. **Klona eller navigera till projektmappen**

2. **Installera beroenden**:
   ```cmd
   mvnw clean install
   ```
   Eller om du har Maven installerat globalt:
   ```cmd
   mvn clean install
   ```

3. **Sätt miljövariabeln** (se avsnittet "Skaffa GitHub-token" ovan)

4. **Starta MCP Calculator Service**:
   Se till att kapitel 1:s MCP kalkylatortjänst körs på `http://localhost:8080/sse`. Den måste vara igång innan du startar klienten.

## Köra applikationen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Vad applikationen gör

Applikationen visar tre huvudsakliga interaktioner med kalkylatortjänsten:

1. **Addition**: Beräknar summan av 24.5 och 17.3
2. **Kvadratrot**: Beräknar kvadratroten av 144
3. **Hjälp**: Visar tillgängliga kalkylatorfunktioner

## Förväntad utdata

När allt fungerar korrekt bör du se en utdata liknande denna:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Felsökning

### Vanliga problem

1. **"GITHUB_TOKEN environment variable not set"**
   - Kontrollera att du har satt miljövariabeln `GITHUB_TOKEN`
   - Starta om terminalen/kommandoprompten efter att du satt variabeln

2. **"Connection refused to localhost:8080"**
   - Kontrollera att MCP kalkylatortjänsten körs på port 8080
   - Se om någon annan tjänst använder port 8080

3. **"Authentication failed"**
   - Verifiera att din GitHub-token är giltig och har rätt behörigheter
   - Kontrollera att du har åtkomst till GitHub Models

4. **Maven build-fel**
   - Säkerställ att du använder Java 21 eller högre: `java -version`
   - Prova att rensa bygget: `mvnw clean`

### Felsökning

För att aktivera debug-loggning, lägg till följande JVM-argument när du kör:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguration

Applikationen är konfigurerad för att:
- Använda GitHub Models med modellen `gpt-4.1-nano`
- Ansluta till MCP-tjänsten på `http://localhost:8080/sse`
- Använda en timeout på 60 sekunder för förfrågningar
- Aktivera loggning av förfrågningar/svar för felsökning

## Beroenden

Viktiga beroenden i detta projekt:
- **LangChain4j**: För AI-integration och verktygshantering
- **LangChain4j MCP**: För stöd av Model Context Protocol
- **LangChain4j GitHub Models**: För integration med GitHub Models
- **Spring Boot**: För applikationsramverk och beroendeinjektion

## Licens

Detta projekt är licensierat under Apache License 2.0 - se [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) för detaljer.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.