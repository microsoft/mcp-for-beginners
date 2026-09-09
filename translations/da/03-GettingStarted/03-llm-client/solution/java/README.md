# Calculator LLM-klient

En Java-applikation, der demonstrerer, hvordan man bruger LangChain4j til at forbinde til en MCP (Model Context Protocol) lommeregner-tjeneste gennem MiniMax OpenAI-kompatibel API.

## Forudsætninger

- Java 21 eller højere
- Maven 3.6+ (eller brug den medfølgende Maven-wrapper)
- En MiniMax API-nøgle
- En MCP lommeregner-tjeneste, der kører på `http://localhost:8080`

## Sådan får du API-nøglen

Denne applikation bruger MiniMax OpenAI-kompatibel API. Følg disse trin for at få din nøgle og endpoint:

### 1. Vælg en endpoint
1. Brug `https://api.minimax.io/v1` for den globale endpoint
2. Brug `https://api.minimaxi.com/v1` for Kina-endpoint

### 2. Opret en API-nøgle
1. Opret en MiniMax API-nøgle fra din MiniMax-konto
2. Opbevar nøglen sikkert

### 3. Indstil miljøvariablerne

#### På Windows (Kommandoprompt):
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

## Opsætning og installation

1. **Klon eller naviger til projektmappen**

2. **Installer afhængigheder**:
   ```cmd
   mvnw clean install
   ```
   Eller hvis du har Maven installeret globalt:
   ```cmd
   mvn clean install
   ```

3. **Opsæt miljøvariablerne** (se afsnittet "Sådan får du API-nøglen" ovenfor)

4. **Start MCP lommeregner-tjenesten**:
   Sørg for, at MCP lommeregner-tjenesten fra kapitel 1 kører på `http://localhost:8080/sse`. Den skal køre, før du starter klienten.

## Sådan kører du applikationen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Hvad applikationen gør

Applikationen demonstrerer tre hovedinteraktioner med lommeregner-tjenesten:

1. **Addition**: Beregner summen af 24.5 og 17.3
2. **Kvadratrod**: Beregner kvadratroden af 144
3. **Hjælp**: Viser tilgængelige lommeregner-funktioner

## Forventet output

Når det kører korrekt, bør du se output svarende til:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Fejlfinding

### Almindelige problemer

1. **"OPENAI_API_KEY miljøvariablen er ikke sat"**
   - Sørg for, at du har sat miljøvariablen `OPENAI_API_KEY`
   - Genstart din terminal/kommandoprompt efter at have sat variablen

2. **"Forbindelse nægtet til localhost:8080"**
   - Sikr dig, at MCP lommeregner-tjenesten kører på port 8080
   - Tjek om en anden tjeneste bruger port 8080

3. **"Godkendelse mislykkedes"**
   - Bekræft at din API-nøgle er gyldig
   - Kontrollér at `OPENAI_BASE_URL` matcher den endpoint, du ønskede at bruge

4. **Maven build-fejl**
   - Sørg for at du bruger Java 21 eller højere: `java -version`
   - Prøv at rense byggeriet: `mvnw clean`

### Debugging

For at aktivere debug-logning, tilføj følgende JVM-argument ved kørsel:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguration

Applikationen er konfigureret til:
- At bruge MiniMax-M3 som standard, eller MiniMax-M2.7 når `MINIMAX_MODEL_ID` er sat
- At forbinde til `OPENAI_BASE_URL` når den er sat; ellers bruge `https://api.minimaxi.com/v1` når `MINIMAX_REGION=cn_zh`, eller `https://api.minimax.io/v1` som standard
- At forbinde til MCP-tjenesten på `http://localhost:8080/sse`
- At bruge en timeout på 60 sekunder for forespørgsler

## Afhængigheder

Vigtige afhængigheder brugt i dette projekt:
- **LangChain4j**: Til AI-integration og værktøjsstyring
- **LangChain4j MCP**: Til Model Context Protocol-understøttelse
- **LangChain4j OpenAI officiel**: Til integration med MiniMax OpenAI-kompatibel API
- **Spring Boot**: Til applikationsframework og dependency injection

## Licens

Dette projekt er licenseret under Apache License 2.0 – se [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) filen for detaljer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->