# Klient Calculator LLM

> [!NOTE]
> Toto řešení se připojuje ke starší kalkulační službě HTTP+SSE kurzu a
> cíluje na MCP `2025-11-25` SDK API. Není to příklad `2026-07-28` Streamable HTTP.




## Požadavky

- Java 21 nebo novější
- Maven 3.6+ (nebo použijte zahrnutý Maven wrapper)
- Klíč MiniMax API
- Kalkulační služba MCP běžící na `http://localhost:8080`

## Získání API klíče

Tato aplikace používá MiniMax API kompatibilní s OpenAI. Postupujte podle těchto kroků pro získání klíče a koncového bodu:

### 1. Vyberte koncový bod
1. Použijte `https://api.minimax.io/v1` pro globální koncový bod
2. Použijte `https://api.minimaxi.com/v1` pro čínský koncový bod

### 2. Vytvoření API klíče
1. Vytvořte klíč MiniMax API ze svého MiniMax účtu
2. Uchovejte klíč na bezpečném místě

### 3. Nastavení proměnných prostředí

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

1. **Naklonujte nebo přejděte do adresáře projektu**

2. **Nainstalujte závislosti**:
   ```cmd
   mvnw clean install
   ```
   Nebo pokud máte Maven nainstalovaný globálně:
   ```cmd
   mvn clean install
   ```

3. **Nastavte proměnné prostředí** (viz sekce "Získání API klíče" výše)

4. **Spusťte MCP Kalkulační službu**:
   Ujistěte se, že máte spuštěnou MCP kalkulační službu z kapitoly 1 na `http://localhost:8080/sse`. Tato služba by měla být spuštěná před startem klienta.

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

Při úspěšném spuštění byste měli vidět podobný výstup:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Řešení problémů

### Běžné problémy

1. **"PROMĚNNÁ PROSTŘEDÍ OPENAI_API_KEY není nastavena"**
   - Ujistěte se, že máte nastavenou proměnnou prostředí `OPENAI_API_KEY`
   - Po nastavení proměnné restartujte terminál/příkazový řádek

2. **"Připojení odmítnuto k localhost:8080"**
   - Zkontrolujte, zda MCP kalkulační služba běží na portu 8080
   - Zkontrolujte, zda jiná služba nepoužívá port 8080

3. **"Ověření selhalo"**
   - Ověřte platnost vašeho API klíče
   - Zkontrolujte, zda `OPENAI_BASE_URL` odpovídá vámi zamýšlenému koncovému bodu

4. **Chybové hlášky při sestavení v Maven**
   - Zkontrolujte, že používáte Java 21 nebo novější: `java -version`
   - Zkuste vyčistit sestavení: `mvnw clean`

### Ladění

Pro povolení ladícího protokolování přidejte při spuštění následující JVM argument:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurace

Aplikace je nakonfigurována takto:
- Ve výchozím stavu používá MiniMax-M3; nastavte `MINIMAX_MODEL_ID` pro výběr mezi `MiniMax-M3` nebo `MiniMax-M2.7`
- Připojuje se na `OPENAI_BASE_URL`, pokud je nastavena; jinak používá `https://api.minimaxi.com/v1`, když je `MINIMAX_REGION=cn_zh`, nebo výchozí `https://api.minimax.io/v1`
- Připojuje se ke službě MCP na `http://localhost:8080/sse`
- Pro požadavky používá timeout 60 sekund

## Závislosti

Hlavní závislosti použité v tomto projektu:
- **LangChain4j**: Pro AI integraci a správu nástrojů
- **LangChain4j MCP**: Pro podporu Model Context Protocolu
- **LangChain4j OpenAI official**: Pro integraci MiniMax API kompatibilního s OpenAI
- **Spring Boot**: Pro aplikační framework a závislostní injekci

## Licence

Tento projekt je licencován pod Apache licencí 2.0 - podrobnosti najdete v souboru [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->