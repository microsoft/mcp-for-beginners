# Calculator LLM Client

Java aplikacija, ki prikazuje, kako uporabiti LangChain4j za povezavo s kalkulatorjem MCP (Model Context Protocol) s podporo GitHub Models.

## Zahteve

- Java 21 ali novejša
- Maven 3.6+ (ali uporabi priložen Maven wrapper)
- GitHub račun z dostopom do GitHub Models
- MCP kalkulator storitev, ki teče na `http://localhost:8080`

## Pridobitev GitHub žetona

Ta aplikacija uporablja GitHub Models, kar zahteva osebni dostopni žeton GitHub. Sledi tem korakom za pridobitev žetona:

### 1. Dostop do GitHub Models
1. Obišči [GitHub Models](https://github.com/marketplace/models)
2. Prijavi se s svojim GitHub računom
3. Če še nimaš dostopa do GitHub Models, ga zahtej

### 2. Ustvari osebni dostopni žeton
1. Obišči [GitHub Nastavitve → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klikni "Generate new token" → "Generate new token (classic)"
3. Poimenuj žeton (npr. "MCP Calculator Client")
4. Nastavi potek veljavnosti po potrebi
5. Izberi naslednje pravice:
   - `repo` (če dostopaš do zasebnih repozitorijev)
   - `user:email`
6. Klikni "Generate token"
7. **Pomembno**: Žeton takoj kopiraj - kasneje ga ne boš več videl!

### 3. Nastavi okoljsko spremenljivko

#### Na Windows (Command Prompt):
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

## Namestitev in nastavitev

1. **Kloniraj ali pojdi v mapo projekta**

2. **Namesti odvisnosti**:
   ```cmd
   mvnw clean install
   ```
   Ali če imaš Maven nameščen globalno:
   ```cmd
   mvn clean install
   ```

3. **Nastavi okoljsko spremenljivko** (glej razdelek "Pridobitev GitHub žetona" zgoraj)

4. **Zaženi MCP kalkulator storitev**:
   Prepričaj se, da imaš zagnano MCP kalkulator storitev iz poglavja 1 na `http://localhost:8080/sse`. Ta mora teči pred zagonom klienta.

## Zagon aplikacije

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Kaj aplikacija počne

Aplikacija prikazuje tri glavne interakcije s kalkulator storitvijo:

1. **Seštevanje**: Izračuna vsoto 24.5 in 17.3
2. **Kvadratni koren**: Izračuna kvadratni koren števila 144
3. **Pomoč**: Prikaže razpoložljive funkcije kalkulatorja

## Pričakovani izpis

Ob uspešnem zagonu bi moral videti izpis, podoben temu:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Reševanje težav

### Pogoste težave

1. **"GITHUB_TOKEN environment variable not set"**
   - Preveri, da si nastavil `GITHUB_TOKEN` okoljsko spremenljivko
   - Po nastavitvi ponovno zaženi terminal/ukazno vrstico

2. **"Connection refused to localhost:8080"**
   - Preveri, da MCP kalkulator storitev teče na vratih 8080
   - Preveri, ali katera druga storitev ne uporablja vrat 8080

3. **"Authentication failed"**
   - Preveri, da je tvoj GitHub žeton veljaven in ima ustrezne pravice
   - Preveri, ali imaš dostop do GitHub Models

4. **Napake pri Maven build-u**
   - Preveri, da uporabljaš Java 21 ali novejšo: `java -version`
   - Poskusi očistiti build: `mvnw clean`

### Odpravljanje napak

Za omogočanje debug logiranja dodaj naslednji JVM argument ob zagonu:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguracija

Aplikacija je nastavljena tako, da:
- Uporablja GitHub Models z modelom `gpt-4.1-nano`
- Povezuje se na MCP storitev na `http://localhost:8080/sse`
- Uporablja 60-sekundni timeout za zahteve
- Omogoča beleženje zahtev in odgovorov za lažje odpravljanje napak

## Odvisnosti

Ključne odvisnosti v tem projektu:
- **LangChain4j**: za AI integracijo in upravljanje orodij
- **LangChain4j MCP**: za podporo Model Context Protocol
- **LangChain4j GitHub Models**: za integracijo GitHub Models
- **Spring Boot**: za ogrodje aplikacije in injekcijo odvisnosti

## Licenca

Ta projekt je licenciran pod Apache License 2.0 - podrobnosti najdeš v datoteki [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.