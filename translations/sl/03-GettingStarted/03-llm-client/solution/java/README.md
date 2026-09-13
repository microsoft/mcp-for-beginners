# Odjemalec kalkulator LLM

> [!NOTE]
> Ta rešitev se povezuje s staro HTTP+SSE kalkulatorsko storitvijo tečaja in
> cilja na MCP API-je za razvojni komplet `2025-11-25`. Ni primer
> Streamable HTTP-ja `2026-07-28`.

Java aplikacija, ki prikazuje, kako uporabljati LangChain4j za povezavo s kalkulatorsko storitvijo MCP (Model Context Protocol) preko MiniMax API-ja, združljivega z OpenAI.

## Predpogoji

- Java 21 ali višji
- Maven 3.6+ (ali uporabi priloženi Maven wrapper)
- MiniMax API ključ
- Kalkulatorska storitev MCP, ki teče na `http://localhost:8080`

## Pridobivanje API ključa

Ta aplikacija uporablja MiniMax API, združljiv z OpenAI. Sledite tem korakom, da dobite svoj ključ in končno točko:

### 1. Izberite končno točko
1. Uporabite `https://api.minimax.io/v1` za globalno končno točko
2. Uporabite `https://api.minimaxi.com/v1` za kitajsko končno točko

### 2. Ustvarite API ključ
1. Ustvarite MiniMax API ključ v svojem MiniMax računu
2. Ključ shranite na varno mesto

### 3. Nastavite spremenljivke okolja

#### Na Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Na Windows (PowerShell):
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

## Namestitev in priprava

1. **Klonirajte ali pojdite v imenik projekta**

2. **Namestite odvisnosti**:
   ```cmd
   mvnw clean install
   ```
   Ali če imate Maven nameščen globalno:
   ```cmd
   mvn clean install
   ```

3. **Nastavite spremenljivke okolja** (glejte razdelek "Pridobivanje API ključa" zgoraj)

4. **Zaženite MCP kalkulatorsko storitev**:
   Prepričajte se, da imate kalkulatorsko storitev MCP iz poglavja 1 nameščeno in da teče na `http://localhost:8080/sse`. To mora biti zagnano pred zagonom odjemalca.

## Zagon aplikacije

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Kaj aplikacija počne

Aplikacija prikazuje tri glavne interakcije s kalkulatorsko storitvijo:

1. **Seštevanje**: Izračun vsote 24,5 in 17,3
2. **Kvadratni koren**: Izračun kvadratnega korena 144
3. **Pomoč**: Prikaže razpoložljive funkcije kalkulatorja

## Pričakovani izhod

Ko se uspešno zažene, bi morali videti izhod, podoben:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Odpravljanje težav

### Pogoste težave

1. **"OPENAI_API_KEY spremenljivka okolja ni nastavljena"**
   - Prepričajte se, da ste nastavili spremenljivko okolja `OPENAI_API_KEY`
   - Po nastavitvi spremenljivke ponovno zaženite terminal/ukazno vrstico

2. **"Povezava zavrnjena na localhost:8080"**
   - Prepričajte se, da kalkulatorska storitev MCP teče na vratih 8080
   - Preverite, ali druga storitev ne uporablja vrat 8080

3. **"Avtentikacija ni uspela"**
   - Preverite, ali je vaš API ključ veljaven
   - Preverite, da se `OPENAI_BASE_URL` ujema z izbrano končno točko

4. **Napake pri gradnji z Maven**
   - Prepričajte se, da uporabljate Java 21 ali višjo: `java -version`
   - Poskusite očistiti gradnjo: `mvnw clean`

### Prikaz debug informacij

Za vklop beleženja za razhroščevanje dodajte naslednji argument JVM pri zagonu:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracija

Aplikacija je konfigurirana tako, da:
- Privzeto uporablja MiniMax-M3; nastavite `MINIMAX_MODEL_ID`, da izberete `MiniMax-M3` ali `MiniMax-M2.7`
- Povezuje se z `OPENAI_BASE_URL`, če je nastavljen; sicer uporabi `https://api.minimaxi.com/v1`, če je `MINIMAX_REGION=cn_zh`, ali privzeto `https://api.minimax.io/v1`
- Povezuje se s storitvijo MCP na `http://localhost:8080/sse`
- Za zahteve uporablja 60-sekundni timeout

## Odvisnosti

Glavne odvisnosti, uporabljene v tem projektu:
- **LangChain4j**: Za integracijo umetne inteligence in upravljanje orodij
- **LangChain4j MCP**: Za podporo Model Context Protocol
- **LangChain4j uradni OpenAI**: Za integracijo MiniMax API-ja, združljivega z OpenAI
- **Spring Boot**: Za ogrodje aplikacije in injiciranje odvisnosti

## Licenca

Ta projekt je licenciran pod Apache licenco 2.0 - za podrobnosti glejte datoteko [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->