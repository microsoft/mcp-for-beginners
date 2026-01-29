# Calculator LLM Client

En Java-applikasjon som viser hvordan man bruker LangChain4j for å koble til en MCP (Model Context Protocol) kalkulatortjeneste med GitHub Models-integrasjon.

## Forutsetninger

- Java 21 eller nyere
- Maven 3.6+ (eller bruk den medfølgende Maven-wrapperen)
- En GitHub-konto med tilgang til GitHub Models
- En MCP kalkulatortjeneste som kjører på `http://localhost:8080`

## Slik får du GitHub-tokenet

Denne applikasjonen bruker GitHub Models, som krever en personlig tilgangstoken fra GitHub. Følg disse stegene for å få tokenet ditt:

### 1. Gå til GitHub Models
1. Gå til [GitHub Models](https://github.com/marketplace/models)
2. Logg inn med GitHub-kontoen din
3. Be om tilgang til GitHub Models hvis du ikke allerede har det

### 2. Opprett en personlig tilgangstoken
1. Gå til [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klikk på "Generate new token" → "Generate new token (classic)"
3. Gi tokenet et beskrivende navn (f.eks. "MCP Calculator Client")
4. Sett utløpstid etter behov
5. Velg følgende scopes:
   - `repo` (hvis du skal ha tilgang til private repositories)
   - `user:email`
6. Klikk på "Generate token"
7. **Viktig**: Kopier tokenet med en gang – du får ikke se det igjen!

### 3. Sett miljøvariabelen

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

## Oppsett og installasjon

1. **Klon eller naviger til prosjektmappen**

2. **Installer avhengigheter**:
   ```cmd
   mvnw clean install
   ```
   Eller hvis du har Maven installert globalt:
   ```cmd
   mvn clean install
   ```

3. **Sett miljøvariabelen** (se avsnittet "Slik får du GitHub-tokenet" over)

4. **Start MCP kalkulatortjenesten**:
   Sørg for at MCP kalkulatortjenesten fra kapittel 1 kjører på `http://localhost:8080/sse`. Denne må være i gang før du starter klienten.

## Kjøre applikasjonen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Hva applikasjonen gjør

Applikasjonen demonstrerer tre hovedinteraksjoner med kalkulatortjenesten:

1. **Addisjon**: Regner ut summen av 24.5 og 17.3
2. **Kvadratrot**: Regner ut kvadratroten av 144
3. **Hjelp**: Viser tilgjengelige kalkulatorfunksjoner

## Forventet resultat

Når applikasjonen kjører som den skal, bør du se noe lignende:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Feilsøking

### Vanlige problemer

1. **"GITHUB_TOKEN environment variable not set"**
   - Sørg for at `GITHUB_TOKEN` miljøvariabelen er satt
   - Start terminalen/kommandoprompten på nytt etter at du har satt variabelen

2. **"Connection refused to localhost:8080"**
   - Sjekk at MCP kalkulatortjenesten kjører på port 8080
   - Kontroller om en annen tjeneste bruker port 8080

3. **"Authentication failed"**
   - Bekreft at GitHub-tokenet ditt er gyldig og har riktige tillatelser
   - Sjekk at du har tilgang til GitHub Models

4. **Maven byggefeil**
   - Sørg for at du bruker Java 21 eller nyere: `java -version`
   - Prøv å rydde opp i bygget: `mvnw clean`

### Debugging

For å aktivere debug-logging, legg til følgende JVM-argument når du kjører:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasjon

Applikasjonen er konfigurert til å:
- Bruke GitHub Models med modellen `gpt-4.1-nano`
- Koble til MCP-tjenesten på `http://localhost:8080/sse`
- Bruke 60 sekunders timeout for forespørsler
- Aktivere logging av forespørsler/svar for debugging

## Avhengigheter

Nøkkelavhengigheter brukt i dette prosjektet:
- **LangChain4j**: For AI-integrasjon og verktøyhåndtering
- **LangChain4j MCP**: For Model Context Protocol-støtte
- **LangChain4j GitHub Models**: For GitHub Models-integrasjon
- **Spring Boot**: For applikasjonsrammeverk og dependency injection

## Lisens

Dette prosjektet er lisensiert under Apache License 2.0 - se [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) filen for detaljer.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.