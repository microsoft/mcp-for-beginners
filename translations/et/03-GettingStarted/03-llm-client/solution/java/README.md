# Kalkulaatori LLM kliendi rakendus

Java rakendus, mis demonstreerib, kuidas kasutada LangChain4j MCP (Mudeli Konteksti Protokolli) kalkulaatoriteenusega ühenduse loomiseks läbi MiniMax OpenAI-ühilduva API.

## Eeltingimused

- Java 21 või uuem versioon
- Maven 3.6+ (või kasuta kaasasolevat Maven wrapperit)
- MiniMax API võti
- MCP kalkulaatori teenus töötab aadressil `http://localhost:8080`

## API võtme saamine

See rakendus kasutab MiniMax OpenAI-ühilduvat API-t. Järgi neid samme, et saada oma võti ja lõpp-punkt:

### 1. Vali lõpp-punkt
1. Kasuta globaalset lõpp-punkti `https://api.minimax.io/v1`
2. Kasuta Hiina lõpp-punkti `https://api.minimaxi.com/v1`

### 2. Loo API võti
1. Loo MiniMax API võti oma MiniMax kontolt
2. Säilita võti turvalises kohas

### 3. Määra keskkonnamuutujad

#### Windowsis (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windowsis (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Paigaldamine ja seadistamine

1. **Klooni või liigu projekti kausta**

2. **Paigalda sõltuvused**:
   ```cmd
   mvnw clean install
   ```
   Või kui sul on Maven üle süsteemi paigaldatud:
   ```cmd
   mvn clean install
   ```

3. **Sea keskkonnamuutujad** (vt ülal "API võtme saamine" osa)

4. **Käivita MCP kalkulaatori teenus**:
   Veendu, et peatüki 1 MCP kalkulaatori teenus töötab aadressil `http://localhost:8080/sse`. See peab töötama enne kliendi käivitamist.

## Rakenduse käivitamine

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mida rakendus teeb

Rakendus demonstreerib kolme peamist suhtlust kalkulaatori teenusega:

1. **Liitmine**: Arvutab summa 24.5 ja 17.3 vahel
2. **Ruudujuur**: Arvutab ruutjuure arvust 144
3. **Abi**: Kuvab saadaval olevad kalkulaatori funktsioonid

## Oodatav väljund

Kui rakendus jookseb edukalt, näed väljundit, mis on sarnane:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Tõrkeotsing

### Tüüpilised probleemid

1. **"OPENAI_API_KEY keskkonnamuutuja ei ole määratud"**
   - Veendu, et `OPENAI_API_KEY` keskkonnamuutuja on defineeritud
   - Taaskäivita konsool või käsurea aken muutujate seadistamise järel

2. **"Ühendus localhost:8080 on keelatud"**
   - Kontrolli, et MCP kalkulaatori teenus töötab pordil 8080
   - Veendu, et midagi muud ei kasuta porti 8080

3. **"Autentimine ebaõnnestus"**
   - Kontrolli, et sinu API võti on kehtiv
   - Veendu, et `OPENAI_BASE_URL` vastab valitud lõpp-punktile

4. **Maven ehitusvead**
   - Veendu, et kasutad Java 21 või uuemat: `java -version`
   - Proovi ehitust puhastada: `mvnw clean`

### Silumise võimaldamine

Luba silumise logimine, lisades käivitamisel järgmise JVM argumendi:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguratsioon

Rakendus on seadistatud nii:
- Vaikimisi kasutab MiniMax-M3 mudelit; vali `MINIMAX_MODEL_ID` abil kas `MiniMax-M3` või `MiniMax-M2.7`
- Ühendub `OPENAI_BASE_URL` aadressile, kui see on määratud; muul juhul kasutab `https://api.minimaxi.com/v1`, kui `MINIMAX_REGION=cn_zh`, või vaikimisi `https://api.minimax.io/v1`
- Ühendub MCP teenusega aadressil `http://localhost:8080/sse`
- Kasutab päringute ajal 60-sekundilist taimerit

## Sõltuvused

Peamised selles projektis kasutatavad sõltuvused:
- **LangChain4j**: AI integreerimiseks ja tööriistade haldamiseks
- **LangChain4j MCP**: Mudeli konteksti protokolli toeks
- **LangChain4j OpenAI ametlik**: MiniMax OpenAI-ühilduva API integreerimiseks
- **Spring Boot**: Rakenduse raamistik ja sõltuvuste süstimine

## Litsents

See projekt on litsentseeritud Apache litsentsi 2.0 all - vt üksikasju failist [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->