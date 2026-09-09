# Kalkulator LLM Klijent

Java aplikacija koja pokazuje kako koristiti LangChain4j za povezivanje s MCP (Model Context Protocol) kalkulator servisom putem MiniMax OpenAI-kompatibilnog API-ja.

## Preduvjeti

- Java 21 ili noviji
- Maven 3.6+ (ili koristite priloženi Maven wrapper)
- MiniMax API ključ
- MCP kalkulator servis koji radi na `http://localhost:8080`

## Dobivanje API Ključa

Ova aplikacija koristi MiniMax OpenAI-kompatibilni API. Slijedite ove korake da dobijete svoj ključ i endpoint:

### 1. Odaberite endpoint
1. Koristite `https://api.minimax.io/v1` za globalni endpoint
2. Koristite `https://api.minimaxi.com/v1` za China endpoint

### 2. Kreirajte API ključ
1. Kreirajte MiniMax API ključ iz svog MiniMax računa
2. Čuvajte ključ na sigurnom mjestu

### 3. Postavite varijable okoline

#### Na Windowsu (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Na Windowsu (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Na macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Postavljanje i instalacija

1. **Klonirajte ili navigirajte do direktorija projekta**

2. **Instalirajte ovisnosti**:
   ```cmd
   mvnw clean install
   ```
   Ili ako imate Maven instaliran globalno:
   ```cmd
   mvn clean install
   ```

3. **Postavite varijable okoline** (pogledajte odjeljak "Dobivanje API Ključa" iznad)

4. **Pokrenite MCP Kalkulator Servis**:
   Provjerite da imate pokrenut MCP kalkulator servis iz poglavlja 1 na `http://localhost:8080/sse`. To bi trebalo biti pokrenuto prije nego što pokrenete klijenta.

## Pokretanje aplikacije

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Što aplikacija radi

Aplikacija demonstrira tri glavne interakcije s kalkulator servisom:

1. **Zbrajanje**: Izračunava zbroj 24.5 i 17.3
2. **Kvadratni korijen**: Izračunava kvadratni korijen od 144
3. **Pomoć**: Prikazuje dostupne funkcije kalkulatora

## Očekivani izlaz

Kada se uspješno pokrene, trebali biste vidjeti izlaz sličan:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Rješavanje problema

### Česti problemi

1. **"OPENAI_API_KEY varijabla okoline nije postavljena"**
   - Provjerite jeste li postavili `OPENAI_API_KEY` varijablu okoline
   - Ponovno pokrenite terminal/command prompt nakon postavljanja varijable

2. **"Povezivanje odbijeno na localhost:8080"**
   - Provjerite je li MCP kalkulator servis pokrenut na portu 8080
   - Provjerite koristi li neki drugi servis port 8080

3. **"Autentikacija nije uspjela"**
   - Provjerite je li vaš API ključ valjan
   - Provjerite da `OPENAI_BASE_URL` odgovara endpointu koji ste namjeravali koristiti

4. **Greške pri Maven buildu**
   - Provjerite koristite li Java 21 ili noviji: `java -version`
   - Pokušajte očistiti build: `mvnw clean`

### Debugging

Za uključivanje debug logiranja, dodajte sljedeći JVM argument prilikom pokretanja:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracija

Aplikacija je konfigurirana da:
- Koristi MiniMax-M3 prema zadanim postavkama; postavite `MINIMAX_MODEL_ID` da odaberete između `MiniMax-M3` ili `MiniMax-M2.7`
- Povezuje se na `OPENAI_BASE_URL` ako je postavljen; inače koristi `https://api.minimaxi.com/v1` ako je `MINIMAX_REGION=cn_zh`, ili `https://api.minimax.io/v1` prema zadanim postavkama
- Povezuje se na MCP servis na `http://localhost:8080/sse`
- Koristi timeout od 60 sekundi za zahtjeve

## Ovisnosti

Ključne ovisnosti u ovom projektu:
- **LangChain4j**: Za AI integraciju i upravljanje alatima
- **LangChain4j MCP**: Za podršku Model Context Protocol-a
- **LangChain4j OpenAI official**: Za integraciju MiniMax OpenAI-kompatibilnog API-ja
- **Spring Boot**: Za aplikacijski framework i dependency injection

## Licenca

Ovaj projekt je licenciran pod Apache licencom 2.0 - pogledajte [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) datoteku za detalje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->