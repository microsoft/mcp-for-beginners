# Calculator LLM Client

Java aplikace, která ukazuje, jak použít LangChain4j pro připojení ke službě MCP (Model Context Protocol) kalkulačky s integrací GitHub Models.

## Požadavky

- Java 21 nebo novější
- Maven 3.6+ (nebo použijte přiložený Maven wrapper)
- GitHub účet s přístupem k GitHub Models
- MCP kalkulační služba běžící na `http://localhost:8080`

## Získání GitHub Tokenu

Tato aplikace používá GitHub Models, které vyžadují osobní přístupový token GitHubu. Postupujte podle těchto kroků, jak token získat:

### 1. Přístup k GitHub Models
1. Přejděte na [GitHub Models](https://github.com/marketplace/models)
2. Přihlaste se pomocí svého GitHub účtu
3. Požádejte o přístup k GitHub Models, pokud ho ještě nemáte

### 2. Vytvoření osobního přístupového tokenu
1. Přejděte na [GitHub Nastavení → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klikněte na "Generate new token" → "Generate new token (classic)"
3. Pojmenujte token popisným názvem (např. "MCP Calculator Client")
4. Nastavte platnost tokenu podle potřeby
5. Vyberte následující oprávnění:
   - `repo` (pokud přistupujete k soukromým repozitářům)
   - `user:email`
6. Klikněte na "Generate token"
7. **Důležité**: Token si ihned zkopírujte – už ho znovu neuvidíte!

### 3. Nastavení proměnné prostředí

#### Na Windows (Příkazový řádek):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Na Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Na macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
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

3. **Nastavte proměnnou prostředí** (viz sekce "Získání GitHub Tokenu" výše)

4. **Spusťte MCP kalkulační službu**:
   Ujistěte se, že máte spuštěnou MCP kalkulační službu z kapitoly 1 na `http://localhost:8080/sse`. Tato služba musí běžet před spuštěním klienta.

## Spuštění aplikace

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Co aplikace dělá

Aplikace demonstruje tři hlavní interakce se službou kalkulačky:

1. **Sčítání**: Vypočítá součet 24.5 a 17.3
2. **Druhá odmocnina**: Vypočítá druhou odmocninu z 144
3. **Nápověda**: Zobrazí dostupné funkce kalkulačky

## Očekávaný výstup

Při úspěšném spuštění byste měli vidět výstup podobný tomuto:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Řešení problémů

### Běžné problémy

1. **"GITHUB_TOKEN environment variable not set"**
   - Ujistěte se, že máte nastavenou proměnnou prostředí `GITHUB_TOKEN`
   - Po nastavení proměnné restartujte terminál/příkazový řádek

2. **"Connection refused to localhost:8080"**
   - Zkontrolujte, že MCP kalkulační služba běží na portu 8080
   - Ověřte, zda port 8080 nepoužívá jiná služba

3. **"Authentication failed"**
   - Ověřte platnost GitHub tokenu a správná oprávnění
   - Zkontrolujte, zda máte přístup k GitHub Models

4. **Chyby při sestavení Mavenem**
   - Ujistěte se, že používáte Java 21 nebo novější: `java -version`
   - Zkuste vyčistit sestavení: `mvnw clean`

### Ladění

Pro zapnutí ladicích logů přidejte při spuštění následující JVM argument:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurace

Aplikace je nakonfigurována takto:
- Používá GitHub Models s modelem `gpt-4.1-nano`
- Připojuje se ke službě MCP na `http://localhost:8080/sse`
- Nastavuje timeout požadavků na 60 sekund
- Povolené logování požadavků a odpovědí pro ladění

## Závislosti

Hlavní závislosti použité v projektu:
- **LangChain4j**: Pro AI integraci a správu nástrojů
- **LangChain4j MCP**: Pro podporu Model Context Protocol
- **LangChain4j GitHub Models**: Pro integraci GitHub Models
- **Spring Boot**: Pro aplikační framework a dependency injection

## Licence

Tento projekt je licencován pod Apache License 2.0 – podrobnosti najdete v souboru [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.