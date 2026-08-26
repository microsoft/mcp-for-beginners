# Kalkulaatori LLM klient

Java rakendus, mis demonstreerib, kuidas kasutada LangChain4j ühendamiseks MCP (Model Context Protocol) kalkulaatoriteenusega läbi MiniMax OpenAI-ühilduva API.

## Eeldused

- Java 21 või uuem
- Maven 3.6+ (või kasuta kaasasolevat Maven wrapperit)
- MiniMax API võti
- MCP kalkulaatori teenus töötab aadressil `http://localhost:8080`

## API võtme hankimine

See rakendus kasutab MiniMax OpenAI-ühilduvat API-d. Järgi neid samme, et saada oma võti ja lõpp-punkt:

### 1. Vali lõpp-punkt
1. Kasuta globaalset lõpp-punkti jaoks `https://api.minimax.io/v1`
2. Kasuta Hiina lõpp-punkti jaoks `https://api.minimaxi.com/v1`

### 2. Loo API võti
1. Loo MiniMax API võti oma MiniMax konto kaudu
2. Hoia võti turvalises kohas

### 3. Määra keskkonnamuutujad

#### Windowsis (käsklusrida):
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

## Paigaldus ja seadistamine

1. **Klooni või mine projekti kausta**

2. **Paigalda sõltuvused**:
   ```cmd
   mvnw clean install
   ```
   Või kui sul on Maven globaalne:
   ```cmd
   mvn clean install
   ```

3. **Määra keskkonnamuutujad** (loe "API võtme hankimine" jaotisest ülespoole)

4. **Käivita MCP kalkulaatori teenus**:
   Veendu, et 1. peatüki MCP kalkulaatori teenus töötab aadressil `http://localhost:8080/sse`. See peab olema käivitatud enne kliendi käivitamist.

## Rakenduse käivitamine

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mida rakendus teeb

Rakendus demonstreerib kolme peamist suhtlust kalkulaatori teenusega:

1. **Liitmine**: Arvutab kokku 24.5 ja 17.3 summa
2. **Ruutjuur**: Arvutab välja 144 ruutjuure
3. **Abi**: Näitab saadaval olevaid kalkulaatori funktsioone

## Oodatav väljund

Eduka töö korral näed väljundit, mis näeb välja umbes selline:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Tõrkeotsing

### Levinumad probleemid

1. **"OPENAI_API_KEY keskkonnamuutuja pole määratud"**
   - Veendu, et oled määranud `OPENAI_API_KEY` keskkonnamuutuja
   - Taaskäivita terminal / käsklusrida pärast muutuja seadistamist

2. **"Ühendus localhost:8080 keelatud"**
   - Veendu, et MCP kalkulaatori teenus töötab pordil 8080
   - Kontrolli, kas mõni teine teenus ei kasuta juba porti 8080

3. **"Autentimine ebaõnnestus"**
   - Kontrolli, kas sinu API võti on kehtiv
   - Kontrolli, et `OPENAI_BASE_URL` vastab lõpp-punktile, mida kavatsesid kasutada

4. **Maveni build-vead**
   - Veendu, et kasutad Java 21 või uuemat versiooni: `java -version`
   - Proovi puhastada build: `mvnw clean`

### Silumine

Et lubada silumise logi, lisa käivitamisel järgmine JVM argument:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguratsioon

Rakendus on seadistatud nii:
- Vaikimisi kasutab MiniMax-M3, või MiniMax-M2.7 kui on määratud `MINIMAX_MODEL_ID`
- Ühendub `OPENAI_BASE_URL`-iga kui see on määratud; muidu kasutab `https://api.minimaxi.com/v1`, kui `MINIMAX_REGION=cn_zh`, või vaikimisi `https://api.minimax.io/v1`
- Ühendub MCP teenusega aadressil `http://localhost:8080/sse`
- Kasutab päringute jaoks 60-sekundilist ajapiirangut

## Sõltuvused

Peamised selles projektis kasutatavad sõltuvused:
- **LangChain4j**: AI integreerimiseks ja tööriistade haldamiseks
- **LangChain4j MCP**: Model Context Protocol toe jaoks
- **LangChain4j OpenAI ametlik**: MiniMax OpenAI-ühilduva API integratsiooniks
- **Spring Boot**: Rakenduse raamistikuks ja sõltuvuste süstimiseks

## Litsents

See projekt on litsentseeritud Apache litsentsi 2.0 alusel - vaata üksikasju failist [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->