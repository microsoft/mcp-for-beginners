# Calculator LLM Client

En Java-applikation, der demonstrerer, hvordan man bruger LangChain4j til at forbinde til en MCP (Model Context Protocol) calculator-service med GitHub Models-integration.

## Forudsætninger

- Java 21 eller nyere  
- Maven 3.6+ (eller brug den medfølgende Maven wrapper)  
- En GitHub-konto med adgang til GitHub Models  
- En MCP calculator-service kørende på `http://localhost:8080`

## Sådan får du GitHub-tokenet

Denne applikation bruger GitHub Models, som kræver et personligt adgangstoken fra GitHub. Følg disse trin for at få dit token:

### 1. Få adgang til GitHub Models  
1. Gå til [GitHub Models](https://github.com/marketplace/models)  
2. Log ind med din GitHub-konto  
3. Anmod om adgang til GitHub Models, hvis du ikke allerede har det

### 2. Opret et personligt adgangstoken  
1. Gå til [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)  
2. Klik på "Generate new token" → "Generate new token (classic)"  
3. Giv dit token et beskrivende navn (f.eks. "MCP Calculator Client")  
4. Sæt udløbsdato efter behov  
5. Vælg følgende scopes:  
   - `repo` (hvis du skal have adgang til private repositories)  
   - `user:email`  
6. Klik på "Generate token"  
7. **Vigtigt**: Kopiér tokenet med det samme – du kan ikke se det igen!

### 3. Sæt miljøvariablen

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

3. **Sæt miljøvariablen** (se afsnittet "Sådan får du GitHub-tokenet" ovenfor)

4. **Start MCP Calculator Service**:  
   Sørg for, at MCP calculator-servicen fra kapitel 1 kører på `http://localhost:8080/sse`. Den skal være kørende, før du starter klienten.

## Kørsel af applikationen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Hvad applikationen gør

Applikationen demonstrerer tre hovedinteraktioner med calculator-servicen:

1. **Addition**: Beregner summen af 24.5 og 17.3  
2. **Kvadratrod**: Beregner kvadratroden af 144  
3. **Hjælp**: Viser tilgængelige calculator-funktioner

## Forventet output

Når det kører korrekt, bør du se output, der ligner:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Fejlfinding

### Almindelige problemer

1. **"GITHUB_TOKEN environment variable not set"**  
   - Sørg for, at du har sat miljøvariablen `GITHUB_TOKEN`  
   - Genstart dit terminal- eller kommandopromptvindue efter opsætning

2. **"Connection refused to localhost:8080"**  
   - Tjek at MCP calculator-servicen kører på port 8080  
   - Undersøg om en anden service bruger port 8080

3. **"Authentication failed"**  
   - Bekræft at dit GitHub-token er gyldigt og har de rette tilladelser  
   - Tjek om du har adgang til GitHub Models

4. **Maven build-fejl**  
   - Sørg for, at du bruger Java 21 eller nyere: `java -version`  
   - Prøv at rydde build: `mvnw clean`

### Debugging

For at aktivere debug-logging, tilføj følgende JVM-argument ved kørsel:  
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguration

Applikationen er konfigureret til at:  
- Bruge GitHub Models med modellen `gpt-4.1-nano`  
- Forbinde til MCP-servicen på `http://localhost:8080/sse`  
- Bruge en timeout på 60 sekunder for forespørgsler  
- Aktivere logging af forespørgsler/svar til debugging

## Afhængigheder

Vigtige afhængigheder i dette projekt:  
- **LangChain4j**: Til AI-integration og værktøjsstyring  
- **LangChain4j MCP**: Til Model Context Protocol-support  
- **LangChain4j GitHub Models**: Til GitHub Models-integration  
- **Spring Boot**: Til applikationsframework og dependency injection

## Licens

Dette projekt er licenseret under Apache License 2.0 – se [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) filen for detaljer.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.