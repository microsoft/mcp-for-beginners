# Kalkulator LLM-klient

En Java-applikasjon som demonstrerer hvordan man bruker LangChain4j for å koble til en MCP (Model Context Protocol) kalkulatortjeneste gjennom MiniMax OpenAI-kompatibel API.

## Forutsetninger

- Java 21 eller nyere
- Maven 3.6+ (eller bruk medfølgende Maven wrapper)
- En MiniMax API-nøkkel
- En MCP kalkulatortjeneste som kjører på `http://localhost:8080`

## Skaff API-nøkkelen

Denne applikasjonen bruker MiniMax OpenAI-kompatibel API. Følg disse stegene for å få nøkkelen og endepunktet:

### 1. Velg et endepunkt
1. Bruk `https://api.minimax.io/v1` for det globale endepunktet
2. Bruk `https://api.minimaxi.com/v1` for Kina-endepunktet

### 2. Opprett en API-nøkkel
1. Opprett en MiniMax API-nøkkel fra din MiniMax-konto
2. Oppbevar nøkkelen sikkert

### 3. Sett miljøvariablene

#### På Windows (Command Prompt):
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

3. **Sett miljøvariablene** (se "Skaff API-nøkkelen" seksjonen over)

4. **Start MCP kalkulatortjenesten**:
   Sørg for at du har MCP kalkulatortjenesten fra kapittel 1 kjørende på `http://localhost:8080/sse`. Denne bør kjøre før du starter klienten.

## Kjøre applikasjonen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Hva applikasjonen gjør

Applikasjonen demonstrerer tre hovedinteraksjoner med kalkulatortjenesten:

1. **Addisjon**: Beregner summen av 24.5 og 17.3
2. **Kvadratrot**: Beregner kvadratroten av 144
3. **Hjelp**: Viser tilgjengelige kalkulatorfunksjoner

## Forventet utdata

Når applikasjonen kjører riktig, skal du se utdata som ligner:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Feilsøking

### Vanlige problemer

1. **"OPENAI_API_KEY miljøvariabel er ikke satt"**
   - Sørg for at du har satt `OPENAI_API_KEY` miljøvariabelen
   - Start terminalen/kommandoprompten på nytt etter å ha satt variabelen

2. **"Connection refused to localhost:8080"**
   - Kontroller at MCP kalkulatortjenesten kjører på port 8080
   - Sjekk om en annen tjeneste bruker port 8080

3. **"Authentication failed"**
   - Verifiser at API-nøkkelen din er gyldig
   - Sjekk at `OPENAI_BASE_URL` matcher endepunktet du ønsket å bruke

4. **Maven build feil**
   - Sørg for at du bruker Java 21 eller nyere: `java -version`
   - Prøv å rense bygget: `mvnw clean`

### Feilsøking

For å aktivere feilsøkingslogging, legg til følgende JVM-argument ved kjøring:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasjon

Applikasjonen er konfigurert til å:
- Bruke MiniMax-M3 som standard; sett `MINIMAX_MODEL_ID` for å velge enten `MiniMax-M3` eller `MiniMax-M2.7`
- Koble til `OPENAI_BASE_URL` når den er satt; ellers bruk `https://api.minimaxi.com/v1` når `MINIMAX_REGION=cn_zh`, eller `https://api.minimax.io/v1` som standard
- Koble til MCP tjenesten på `http://localhost:8080/sse`
- Bruke 60 sekunders timeout for forespørsler

## Avhengigheter

Nøkkelavhengigheter brukt i dette prosjektet:
- **LangChain4j**: For AI-integrasjon og verktøyhåndtering
- **LangChain4j MCP**: For Model Context Protocol støtte
- **LangChain4j OpenAI offisiell**: For MiniMax OpenAI-kompatibel API-integrasjon
- **Spring Boot**: For applikasjonsrammeverk og avhengighetsinjeksjon

## Lisens

Dette prosjektet er lisensiert under Apache License 2.0 - se [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) filen for detaljer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->