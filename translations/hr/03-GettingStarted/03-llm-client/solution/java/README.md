# Calculator LLM Klijent

Java aplikacija koja demonstrira kako koristiti LangChain4j za povezivanje s MCP (Model Context Protocol) kalkulator servisom putem MiniMax OpenAI-kompatibilnog API-ja.

## Preduvjeti

- Java 21 ili noviji
- Maven 3.6+ (ili koristite priloženi Maven wrapper)
- MiniMax API ključ
- MCP kalkulator servis koji radi na `http://localhost:8080`

## Dobivanje API ključa

Ova aplikacija koristi MiniMax OpenAI-kompatibilni API. Slijedite ove korake da dobijete svoj ključ i endpoint:

### 1. Odaberite endpoint
1. Koristite `https://api.minimax.io/v1` za globalni endpoint
2. Koristite `https://api.minimaxi.com/v1` za kineski endpoint

### 2. Kreirajte API ključ
1. Kreirajte MiniMax API ključ iz vašeg MiniMax računa
2. Sačuvajte ključ na sigurnom mjestu

### 3. Postavite varijable okoline

#### Na Windows-u (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Na Windows-u (PowerShell):
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

1. **Klonirajte ili se navigirajte do direktorija projekta**

2. **Instalirajte ovisnosti**:
   ```cmd
   mvnw clean install
   ```
   Ili ako imate globalno instaliran Maven:
   ```cmd
   mvn clean install
   ```

3. **Postavite varijable okoline** (pogledajte odjeljak "Dobivanje API ključa" iznad)

4. **Pokrenite MCP Kalkulator Servis**:
   Provjerite da je MCP kalkulator servis iz poglavlja 1 pokrenut na `http://localhost:8080/sse`. To treba biti pokrenuto prije nego što pokrenete klijent.

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

## Očekivani rezultat

Kada aplikacija uspješno radi, trebali biste vidjeti izlaz sličan:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Rješavanje problema

### Česti problemi

1. **"OPENAI_API_KEY varijabla okoline nije postavljena"**
   - Provjerite jeste li postavili `OPENAI_API_KEY` varijablu okoline
   - Ponovno pokrenite terminal/Command Prompt nakon postavljanja varijable

2. **"Veza odbijena na localhost:8080"**
   - Provjerite radi li MCP kalkulator servis na portu 8080
   - Provjerite koristi li neki drugi servis port 8080

3. **"Autentifikacija nije uspjela"**
   - Potvrdite da je vaš API ključ valjan
   - Provjerite da `OPENAI_BASE_URL` odgovara endpointu koji ste namjeravali koristiti

4. **Greške u build-u s Mavenom**
   - Provjerite da koristite Java 21 ili noviju verziju: `java -version`
   - Pokušajte očistiti build: `mvnw clean`

### Debugging

Da omogućite debug logiranje, dodajte sljedeći JVM argument prilikom pokretanja:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracija

Aplikacija je konfigurirana da:
- Koristi MiniMax-M3 prema zadanim postavkama, ili MiniMax-M2.7 kada je `MINIMAX_MODEL_ID` postavljen
- Spoji se na `OPENAI_BASE_URL` kada je postavljen; inače koristi `https://api.minimaxi.com/v1` kada je `MINIMAX_REGION=cn_zh`, ili `https://api.minimax.io/v1` prema zadanim postavkama
- Spoji se na MCP servis na `http://localhost:8080/sse`
- Koristi timeout od 60 sekundi za zahtjeve

## Ovisnosti

Ključne ovisnosti korištene u ovom projektu:
- **LangChain4j**: Za AI integraciju i upravljanje alatima
- **LangChain4j MCP**: Za podršku Model Context Protocol-a
- **LangChain4j OpenAI official**: Za integraciju MiniMax OpenAI-kompatibilnog API-ja
- **Spring Boot**: Za aplikacijski okvir i injektiranje ovisnosti

## Licenca

Ovaj projekt je licenciran pod Apache licencom 2.0 - pogledajte [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) datoteku za detalje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->