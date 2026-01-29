# Calculator LLM Client

Java aplikacija koja pokazuje kako koristiti LangChain4j za povezivanje s MCP (Model Context Protocol) kalkulator servisom s integracijom GitHub Models.

## Preduvjeti

- Java 21 ili noviji
- Maven 3.6+ (ili koristite priloženi Maven wrapper)
- GitHub račun s pristupom GitHub Models
- MCP kalkulator servis koji radi na `http://localhost:8080`

## Dobivanje GitHub Tokena

Ova aplikacija koristi GitHub Models koji zahtijeva GitHub personal access token. Slijedite ove korake da biste dobili svoj token:

### 1. Pristup GitHub Models
1. Idite na [GitHub Models](https://github.com/marketplace/models)
2. Prijavite se sa svojim GitHub računom
3. Zatražite pristup GitHub Models ako ga još nemate

### 2. Kreirajte Personal Access Token
1. Idite na [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Kliknite "Generate new token" → "Generate new token (classic)"
3. Dajte tokenu opisno ime (npr. "MCP Calculator Client")
4. Postavite trajanje valjanosti prema potrebi
5. Odaberite sljedeće ovlasti:
   - `repo` (ako pristupate privatnim repozitorijima)
   - `user:email`
6. Kliknite "Generate token"
7. **Važno**: Odmah kopirajte token - nakon toga ga nećete moći ponovno vidjeti!

### 3. Postavite Varijablu Okoline

#### Na Windowsu (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Na Windowsu (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Na macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Postavljanje i Instalacija

1. **Klonirajte ili se premjestite u direktorij projekta**

2. **Instalirajte ovisnosti**:
   ```cmd
   mvnw clean install
   ```
   Ili ako imate globalno instaliran Maven:
   ```cmd
   mvn clean install
   ```

3. **Postavite varijablu okoline** (pogledajte odjeljak "Dobivanje GitHub Tokena" gore)

4. **Pokrenite MCP Calculator Service**:
   Provjerite da je MCP kalkulator servis iz poglavlja 1 pokrenut na `http://localhost:8080/sse`. Servis mora biti aktivan prije pokretanja klijenta.

## Pokretanje Aplikacije

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Što Aplikacija Radi

Aplikacija demonstrira tri glavne interakcije s kalkulator servisom:

1. **Zbrajanje**: Izračunava zbroj 24.5 i 17.3
2. **Kvadratni korijen**: Izračunava kvadratni korijen od 144
3. **Pomoć**: Prikazuje dostupne funkcije kalkulatora

## Očekivani Izlaz

Ako aplikacija radi ispravno, trebali biste vidjeti izlaz sličan ovom:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Rješavanje Problema

### Česti Problemi

1. **"GITHUB_TOKEN environment variable not set"**
   - Provjerite jeste li postavili `GITHUB_TOKEN` varijablu okoline
   - Ponovno pokrenite terminal/command prompt nakon postavljanja varijable

2. **"Connection refused to localhost:8080"**
   - Provjerite je li MCP kalkulator servis pokrenut na portu 8080
   - Provjerite koristi li neki drugi servis port 8080

3. **"Authentication failed"**
   - Provjerite je li vaš GitHub token valjan i ima li potrebne ovlasti
   - Provjerite imate li pristup GitHub Models

4. **Maven build greške**
   - Provjerite koristite li Java 21 ili noviju verziju: `java -version`
   - Pokušajte očistiti build: `mvnw clean`

### Debugging

Za uključivanje debug logiranja, dodajte sljedeći JVM argument prilikom pokretanja:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracija

Aplikacija je konfigurirana da:
- Koristi GitHub Models s modelom `gpt-4.1-nano`
- Povezuje se na MCP servis na `http://localhost:8080/sse`
- Koristi timeout od 60 sekundi za zahtjeve
- Omogućuje logiranje zahtjeva/odgovora za potrebe debugiranja

## Ovisnosti

Ključne ovisnosti u ovom projektu:
- **LangChain4j**: Za AI integraciju i upravljanje alatima
- **LangChain4j MCP**: Za podršku Model Context Protocolu
- **LangChain4j GitHub Models**: Za integraciju GitHub Models
- **Spring Boot**: Za aplikacijski okvir i injekciju ovisnosti

## Licenca

Ovaj projekt je licenciran pod Apache License 2.0 - pogledajte [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) datoteku za detalje.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.