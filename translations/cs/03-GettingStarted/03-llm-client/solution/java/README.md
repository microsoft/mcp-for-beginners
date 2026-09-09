# Klient Kalkulačky LLM

Java aplikace, která demonstruje, jak použít LangChain4j pro připojení k MCP (Model Context Protocol) kalkulační službě prostřednictvím OpenAI-kompatibilní API MiniMax.

## Požadavky

- Java 21 nebo novější
- Maven 3.6+ (nebo použijte přiložený Maven wrapper)
- Klíč API MiniMax
- MCP kalkulační služba běžící na `http://localhost:8080`

## Získání klíče API

Tato aplikace používá OpenAI-kompatibilní API MiniMax. Postupujte podle těchto kroků pro získání klíče a endpointu:

### 1. Vyberte endpoint
1. Použijte `https://api.minimax.io/v1` pro globální endpoint
2. Použijte `https://api.minimaxi.com/v1` pro čínský endpoint

### 2. Vytvořte klíč API
1. Vytvořte klíč MiniMax API ze svého účtu MiniMax
2. Uchovejte klíč na bezpečném místě

### 3. Nastavte proměnné prostředí

#### Ve Windows (příkazový řádek):
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

1. **Klonujte nebo přejděte do adresáře projektu**

2. **Nainstalujte závislosti**:
   ```cmd
   mvnw clean install
   ```
   Nebo pokud máte Maven nainstalovaný globálně:
   ```cmd
   mvn clean install
   ```

3. **Nastavte proměnné prostředí** (viz sekce "Získání klíče API" výše)

4. **Spusťte MCP kalkulační službu**:
   Ujistěte se, že máte spuštěnou MCP kalkulační službu z kapitoly 1 na `http://localhost:8080/sse`. Ta musí běžet před spuštěním klienta.

## Spuštění aplikace

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Co aplikace dělá

Aplikace demonstruje tři hlavní interakce s kalkulační službou:

1. **Sčítání**: Vypočítá součet 24,5 a 17,3
2. **Druhý odmocnina**: Vypočítá druhou odmocninu z 144
3. **Nápověda**: Zobrazí dostupné kalkulační funkce

## Očekávaný výstup

Po úspěšném spuštění byste měli vidět výstup podobný:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Řešení problémů

### Běžné problémy

1. **"Proměnná prostředí OPENAI_API_KEY není nastavena"**
   - Ujistěte se, že jste nastavili proměnnou prostředí `OPENAI_API_KEY`
   - Po nastavení proměnné restartujte terminál/příkazový řádek

2. **"Připojení odmítnuto na localhost:8080"**
   - Zkontrolujte, že MCP kalkulační služba běží na portu 8080
   - Ujistěte se, že žádná jiná služba nepoužívá port 8080

3. **"Autentizace selhala"**
   - Ověřte platnost svého klíče API
   - Zkontrolujte, že `OPENAI_BASE_URL` odpovídá zamýšlenému endpointu

4. **Chyby při sestavení Maven**
   - Ujistěte se, že používáte Java 21 nebo vyšší: `java -version`
   - Zkuste vyčistit sestavení: `mvnw clean`

### Ladění

Pro povolení ladicího logování přidejte při spuštění tento argument JVM:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurace

Aplikace je nastavena takto:
- Výchozí model MiniMax-M3; nastavte `MINIMAX_MODEL_ID` pro výběr mezi `MiniMax-M3` nebo `MiniMax-M2.7`
- Připojí se na `OPENAI_BASE_URL`, pokud je nastavena; jinak použije `https://api.minimaxi.com/v1` při `MINIMAX_REGION=cn_zh`, nebo výchozí `https://api.minimax.io/v1`
- Připojí se k MCP službě na `http://localhost:8080/sse`
- Použije timeout 60 sekund pro požadavky

## Závislosti

Klíčové závislosti použité v tomto projektu:
- **LangChain4j**: Pro integraci AI a správu nástrojů
- **LangChain4j MCP**: Pro podporu Model Context Protocol
- **LangChain4j OpenAI official**: Pro integraci OpenAI-kompatibilního API MiniMax
- **Spring Boot**: Pro aplikační framework a dependency injection

## Licence

Tento projekt je licencován pod licencí Apache 2.0 - podrobnosti viz soubor [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->