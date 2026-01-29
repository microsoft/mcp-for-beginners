# Calculator LLM Client

Java aplikácia, ktorá ukazuje, ako použiť LangChain4j na pripojenie k MCP (Model Context Protocol) kalkulačnej službe s integráciou GitHub Models.

## Požiadavky

- Java 21 alebo novšia
- Maven 3.6+ (alebo použite priložený Maven wrapper)
- GitHub účet s prístupom k GitHub Models
- MCP kalkulačná služba bežiaca na `http://localhost:8080`

## Získanie GitHub Tokenu

Táto aplikácia používa GitHub Models, ktoré vyžadujú osobný prístupový token GitHub. Postupujte podľa týchto krokov, aby ste získali svoj token:

### 1. Prístup k GitHub Models
1. Prejdite na [GitHub Models](https://github.com/marketplace/models)
2. Prihláste sa so svojím GitHub účtom
3. Požiadajte o prístup k GitHub Models, ak ho ešte nemáte

### 2. Vytvorenie osobného prístupového tokenu
1. Prejdite na [GitHub Nastavenia → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Kliknite na "Generate new token" → "Generate new token (classic)"
3. Pomenujte token popisným názvom (napr. "MCP Calculator Client")
4. Nastavte platnosť podľa potreby
5. Vyberte nasledujúce oprávnenia:
   - `repo` (ak pristupujete k súkromným repozitárom)
   - `user:email`
6. Kliknite na "Generate token"
7. **Dôležité**: Token si ihneď skopírujte – už ho nebudete môcť zobraziť!

### 3. Nastavenie environmentálnej premennej

#### Na Windows (Príkazový riadok):
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

## Nastavenie a inštalácia

1. **Naklonujte alebo prejdite do adresára projektu**

2. **Nainštalujte závislosti**:
   ```cmd
   mvnw clean install
   ```
   Alebo ak máte Maven nainštalovaný globálne:
   ```cmd
   mvn clean install
   ```

3. **Nastavte environmentálnu premennú** (pozrite sekciu "Získanie GitHub Tokenu" vyššie)

4. **Spustite MCP kalkulačnú službu**:
   Uistite sa, že máte spustenú MCP kalkulačnú službu z kapitoly 1 na `http://localhost:8080/sse`. Táto služba musí bežať pred spustením klienta.

## Spustenie aplikácie

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Čo aplikácia robí

Aplikácia demonštruje tri hlavné interakcie s kalkulačnou službou:

1. **Sčítanie**: Vypočíta súčet 24.5 a 17.3
2. **Druhá odmocnina**: Vypočíta druhú odmocninu z 144
3. **Pomoc**: Zobrazí dostupné funkcie kalkulačky

## Očakávaný výstup

Pri úspešnom spustení by ste mali vidieť výstup podobný tomuto:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Riešenie problémov

### Bežné problémy

1. **"GITHUB_TOKEN environment variable not set"**
   - Skontrolujte, či ste nastavili environmentálnu premennú `GITHUB_TOKEN`
   - Po nastavení premennej reštartujte terminál/príkazový riadok

2. **"Connection refused to localhost:8080"**
   - Overte, či MCP kalkulačná služba beží na porte 8080
   - Skontrolujte, či iná služba nepoužíva port 8080

3. **"Authentication failed"**
   - Overte platnosť GitHub tokenu a správne oprávnenia
   - Skontrolujte, či máte prístup k GitHub Models

4. **Chyby pri buildovaní Mavenom**
   - Uistite sa, že používate Java 21 alebo novšiu: `java -version`
   - Skúste vyčistiť build: `mvnw clean`

### Ladenie

Pre zapnutie debug logovania pridajte pri spustení JVM nasledujúci argument:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurácia

Aplikácia je nakonfigurovaná tak, aby:
- Používala GitHub Models s modelom `gpt-4.1-nano`
- Pripájala sa k MCP službe na `http://localhost:8080/sse`
- Mala timeout 60 sekúnd pre požiadavky
- Povolené logovanie požiadaviek a odpovedí pre ladenie

## Závislosti

Hlavné závislosti použité v tomto projekte:
- **LangChain4j**: Pre AI integráciu a správu nástrojov
- **LangChain4j MCP**: Pre podporu Model Context Protocol
- **LangChain4j GitHub Models**: Pre integráciu GitHub Models
- **Spring Boot**: Pre aplikačný framework a dependency injection

## Licencia

Tento projekt je licencovaný pod Apache License 2.0 - podrobnosti nájdete v súbore [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.