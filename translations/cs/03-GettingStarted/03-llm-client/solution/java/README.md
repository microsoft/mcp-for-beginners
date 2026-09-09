# Klient Calculator LLM

Java aplikace, která demonstruje, jak používat LangChain4j pro připojení k MCP (Model Context Protocol) kalkulační službě prostřednictvím MiniMax API kompatibilního s OpenAI.

## Požadavky

- Java 21 nebo novější
- Maven 3.6+ (nebo použijte přiložený Maven wrapper)
- Klíč MiniMax API
- MCP kalkulační služba běžící na `http://localhost:8080`

## Získání API klíče

Tato aplikace používá MiniMax API kompatibilní s OpenAI. Postupujte podle těchto kroků pro získání klíče a endpointu:

### 1. Vyberte endpoint
1. Použijte `https://api.minimax.io/v1` pro globální endpoint
2. Použijte `https://api.minimaxi.com/v1` pro čínský endpoint

### 2. Vytvořte API klíč
1. Vytvořte MiniMax API klíč ze svého MiniMax účtu
2. Uložte klíč na bezpečné místo

### 3. Nastavte proměnné prostředí

#### Ve Windows (Příkazový řádek):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Ve Windows (PowerShell):
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

## Nastavení a instalace

1. **Naklonujte nebo přejděte do složky projektu**

2. **Nainstalujte závislosti**:
   ```cmd
   mvnw clean install
   ```
   Nebo pokud máte nainstalovaný Maven globálně:
   ```cmd
   mvn clean install
   ```

3. **Nastavte proměnné prostředí** (viz sekce "Získání API klíče" výše)

4. **Spusťte MCP kalkulační službu**:
   Ujistěte se, že máte spuštěnou kapitolu 1 MCP kalkulační službu na `http://localhost:8080/sse`. Ta by měla běžet před spuštěním klienta.

## Spuštění aplikace

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Co aplikace dělá

Aplikace demonstruje tři hlavní interakce s kalkulační službou:

1. **Sčítání**: Vypočítá součet 24.5 a 17.3
2. **Druhá odmocnina**: Vypočítá druhou odmocninu z 144
3. **Nápověda**: Zobrazí dostupné kalkulační funkce

## Očekávaný výstup

Při úspěšném spuštění byste měli vidět výstup podobný:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Řešení problémů

### Časté problémy

1. **"Proměnná OPENAI_API_KEY není nastavena"**
   - Ujistěte se, že máte nastavenou proměnnou prostředí `OPENAI_API_KEY`
   - Po nastavení proměnné restartujte terminál/příkazový řádek

2. **"Připojení odmítnuto localhost:8080"**
   - Ujistěte se, že MCP kalkulační služba běží na portu 8080
   - Zkontrolujte, zda jiná služba nepoužívá port 8080

3. **"Ověření selhalo"**
   - Zkontrolujte, že váš API klíč je platný
   - Ověřte, že `OPENAI_BASE_URL` odpovídá použitému endpointu

4. **Chyby při sestavení v Maven**
   - Ujistěte se, že používáte Java 21 nebo novější: `java -version`
   - Zkuste vyčistit sestavení: `mvnw clean`

### Ladění

Pro povolení ladicího logování přidejte při spuštění následující argument JVM:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurace

Aplikace je nastavena takto:
- Výchozí použití MiniMax-M3, nebo MiniMax-M2.7 pokud je nastaven `MINIMAX_MODEL_ID`
- Připojení k `OPENAI_BASE_URL` pokud je nastaveno; jinak použije `https://api.minimaxi.com/v1` pokud je `MINIMAX_REGION=cn_zh`, nebo výchozí `https://api.minimax.io/v1`
- Připojení k MCP službě na `http://localhost:8080/sse`
- Časový limit požadavků 60 sekund

## Závislosti

Klíčové závislosti použité v tomto projektu:
- **LangChain4j**: Pro integraci AI a správu nástrojů
- **LangChain4j MCP**: Pro podporu Model Context Protocol
- **LangChain4j OpenAI oficial**: Pro integraci MiniMax OpenAI-kompatibilní API
- **Spring Boot**: Pro aplikační rámec a injektování závislostí

## Licence

Tento projekt je licencován pod licencí Apache 2.0 - podrobnosti najdete v souboru [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->