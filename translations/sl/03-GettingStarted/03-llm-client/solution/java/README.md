# Kalkulator LLM odjemalec

Java aplikacija, ki prikazuje, kako uporabiti LangChain4j za povezavo na MCP (Model Context Protocol) kalkulatorsko storitev preko MiniMax OpenAI združljivega API-ja.

## Predpogoji

- Java 21 ali novejši
- Maven 3.6+ (ali uporabi priložen Maven wrapper)
- MiniMax API ključ
- MCP kalkulatorska storitev, ki teče na `http://localhost:8080`

## Pridobivanje API ključa

Ta aplikacija uporablja MiniMax OpenAI združljiv API. Sledi tem korakom za pridobitev ključa in končne točke:

### 1. Izberi končno točko
1. Uporabi `https://api.minimax.io/v1` za globalno končno točko
2. Uporabi `https://api.minimaxi.com/v1` za kitajsko končno točko

### 2. Ustvari API ključ
1. Ustvari MiniMax API ključ iz svojega MiniMax računa
2. Shrani ključ na varno mesto

### 3. Nastavi okoljske spremenljivke

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

## Namestitev in postavitev

1. **Kloniraj ali pojdi v mapo projekta**

2. **Namesti odvisnosti**:
   ```cmd
   mvnw clean install
   ```
   Ali če imaš Maven nameščen globalno:
   ```cmd
   mvn clean install
   ```

3. **Nastavi okoljske spremenljivke** (glej zgornji odsek "Pridobivanje API ključa")

4. **Zaženi MCP kalkulatorsko storitev**:
   Prepričaj se, da imaš zagnano MCP kalkulatorsko storitev iz prvega poglavja na `http://localhost:8080/sse`. To mora biti zagnano pred zagonem odjemalca.

## Zagon aplikacije

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Kaj aplikacija počne

Aplikacija prikazuje tri glavne interakcije z kalkulatorsko storitvijo:

1. **Seštevanje**: Izračuna vsoto 24.5 in 17.3
2. **Kvadratni koren**: Izračuna kvadratni koren števila 144
3. **Pomoč**: Prikaže razpoložljive funkcije kalkulatorja

## Pričakovani izhod

Ob uspešnem zagonu bi moral videti izhod podoben temu:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Reševanje težav

### Pogoste težave

1. **"OPENAI_API_KEY okoljska spremenljivka ni nastavljena"**
   - Preveri, da si nastavil `OPENAI_API_KEY` okoljsko spremenljivko
   - Po nastavitvi spremenljivke ponovno zaženi terminal/ukazni poziv

2. **"Povezava zavrnjena na localhost:8080"**
   - Prepričaj se, da MCP kalkulatorska storitev teče na portu 8080
   - Preveri, ali drug servis uporablja port 8080

3. **"Avtentikacija ni uspela"**
   - Preveri veljavnost svojega API ključa
   - Preveri, da se `OPENAI_BASE_URL` ujema s končno točko, ki jo želiš uporabljati

4. **Napake pri sestavi v Maven-u**
   - Prepričaj se, da uporabljaš Java 21 ali novejšo: `java -version`
   - Poskusi očistiti sestavo projekta: `mvnw clean`

### Odpravljanje napak

Za omogočanje debug zapisovanja dodaj naslednji JVM argument pri zagonu:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracija

Aplikacija je konfigurirana tako, da:
- Privzeto uporablja MiniMax-M3, ali MiniMax-M2.7, ko je nastavljena `MINIMAX_MODEL_ID`
- Povezuje se na `OPENAI_BASE_URL`, če je nastavljena; sicer uporabljaj `https://api.minimaxi.com/v1`, če je `MINIMAX_REGION=cn_zh`, ali `https://api.minimax.io/v1` privzeto
- Povezuje se na MCP storitev na `http://localhost:8080/sse`
- Uporablja 60-sekundni timeout za zahteve

## Odvisnosti

Ključne odvisnosti, uporabljene v tem projektu:
- **LangChain4j**: Za AI integracijo in upravljanje orodij
- **LangChain4j MCP**: Za podporo Model Context Protocol
- **LangChain4j OpenAI uradni**: Za integracijo MiniMax OpenAI združljivega API-ja
- **Spring Boot**: Za aplikacijski okvir in injekcijo odvisnosti

## Licenca

Ta projekt je licenciran pod Apache licenco 2.0 - za podrobnosti glej [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) datoteko.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->