# Klient kalkulačky LLM

Java aplikácia, ktorá demonštruje, ako použiť LangChain4j na pripojenie k MCP (Model Context Protocol) kalkulačnej službe cez MiniMax OpenAI-kompatibilné API.

## Požiadavky

- Java 21 alebo vyššia
- Maven 3.6+ (alebo použite zahrnutý Maven wrapper)
- MiniMax API kľúč
- MCP kalkulačná služba bežiaca na `http://localhost:8080`

## Získanie API kľúča

Táto aplikácia používa MiniMax OpenAI-kompatibilné API. Nasledujte tieto kroky na získanie vášho kľúča a koncového bodu:

### 1. Vyberte koncový bod
1. Použite `https://api.minimax.io/v1` pre globálny koncový bod
2. Použite `https://api.minimaxi.com/v1` pre čínsky koncový bod

### 2. Vytvorte API kľúč
1. Vytvorte MiniMax API kľúč vo vašom MiniMax účte
2. Uchovajte kľúč na bezpečnom mieste

### 3. Nastavte premenné prostredia

#### Na Windows (Príkazový riadok):
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

## Nastavenie a inštalácia

1. **Klonujte alebo prejdite do adresára projektu**

2. **Nainštalujte závislosti**:
   ```cmd
   mvnw clean install
   ```
   Alebo ak máte Maven nainštalovaný globálne:
   ```cmd
   mvn clean install
   ```

3. **Nastavte premenné prostredia** (pozrite sekciu "Získanie API kľúča" vyššie)

4. **Spustite MCP Kalkulačnú službu**:
   Uistite sa, že máte spustenú MCP kalkulačnú službu z kapitoly 1 na `http://localhost:8080/sse`. Táto služba by mala byť spustená pred spustením klienta.

## Spustenie aplikácie

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Čo aplikácia robí

Aplikácia demonštruje tri hlavné interakcie s kalkulačnou službou:

1. **Sčítanie**: Vypočíta súčet 24.5 a 17.3
2. **Druhá odmocnina**: Vypočíta druhú odmocninu z 144
3. **Pomoc**: Zobrazí dostupné kalkulačné funkcie

## Očakávaný výstup

Pri úspešnom spustení by ste mali vidieť výstup podobný:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Riešenie problémov

### Bežné problémy

1. **"OPENAI_API_KEY environment variable is not set"**
   - Uistite sa, že ste nastavili premennú prostredia `OPENAI_API_KEY`
   - Reštartujte terminál/príkazový riadok po nastavení premenných

2. **"Connection refused to localhost:8080"**
   - Overte, či MCP kalkulačná služba beží na porte 8080
   - Skontrolujte, či iná služba nezaberá port 8080

3. **"Authentication failed"**
   - Overte platnosť vášho API kľúča
   - Skontrolujte, či `OPENAI_BASE_URL` zodpovedá zamýšľanému koncovému bodu

4. **Maven build chyby**
   - Uistite sa, že používate Java 21 alebo vyššiu: `java -version`
   - Skúste vyčistiť build: `mvnw clean`

### Ladenie

Pre povolenie debug logovania pridajte pri spustení JVM nasledujúci argument:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurácia

Aplikácia je nakonfigurovaná na:
- Používať predvolene MiniMax-M3; nastavte `MINIMAX_MODEL_ID` pre výber medzi `MiniMax-M3` alebo `MiniMax-M2.7`
- Pripojiť sa na `OPENAI_BASE_URL`, ak je nastavený; inak používa `https://api.minimaxi.com/v1` pre `MINIMAX_REGION=cn_zh`, alebo predvolene `https://api.minimax.io/v1`
- Pripojiť sa na MCP službu na `http://localhost:8080/sse`
- Používať 60-sekundový timeout pre požiadavky

## Závislosti

Kľúčové závislosti použité v tomto projekte:
- **LangChain4j**: Pre integráciu AI a správu nástrojov
- **LangChain4j MCP**: Pre podporu Model Context Protocol
- **LangChain4j OpenAI official**: Pre integráciu MiniMax OpenAI-kompatibilného API
- **Spring Boot**: Pre aplikačný rámec a dependency injection

## Licencia

Tento projekt je licencovaný pod Apache License 2.0 - pozrite si súbor [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) pre podrobnosti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->