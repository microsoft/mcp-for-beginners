# Kalkulaatori LLM klient

> [!NOTE]
> See lahendus ühendub kursuse pärand HTTP+SSE kalkulaatori teenusega ja
> sihib MCP `2025-11-25` SDK API-sid. See ei ole `2026-07-28` Streamable HTTP
> näide.

Java rakendus, mis demonstreerib, kuidas kasutada LangChain4j MCP (Model Context Protocol) kalkulaatori teenusega ühenduse loomiseks MiniMax OpenAI-ühilduva API kaudu.

## Eeldused

- Java 21 või uuem versioon
- Maven 3.6+ (või kasuta kaasas olevat Maven wrapperit)
- MiniMax API võti
- MCP kalkulaatori teenus, mis töötab aadressil `http://localhost:8080`

## API võtme hankimine

See rakendus kasutab MiniMax OpenAI-ühilduvat API-t. Järgige neid samme, et saada oma võti ja lõpp-punkt:

### 1. Valige lõpp-punkt
1. Kasutage globaalse lõpp-punkti jaoks aadressi `https://api.minimax.io/v1`
2. Kasutage Hiina lõpp-punkti jaoks aadressi `https://api.minimaxi.com/v1`

### 2. Looge API võti
1. Looge MiniMax API võti oma MiniMax konto alt
2. Hoidke võti turvalises kohas

### 3. Määrake keskkonnamuutujad

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

## Seadistamine ja paigaldus

1. **Kloonige või minge projekti kataloogi**

2. **Paigaldage sõltuvused**:
   ```cmd
   mvnw clean install
   ```
   Või kui teil on Maven globaalne paigaldus:
   ```cmd
   mvn clean install
   ```

3. **Seadistage keskkonnamuutujad** (vt eelnevalt "API võtme hankimine" jaotist)

4. **Käivitage MCP kalkulaatori teenus**:
   Veenduge, et peatüki 1 MCP kalkulaatori teenus töötab aadressil `http://localhost:8080/sse`. See peaks olema aktiivne enne kliendi käivitamist.

## Rakenduse käivitamine

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mida rakendus teeb

Rakendus demonstreerib kolme peamist suhtlust kalkulaatori teenusega:

1. **Liitmine**: Arvutab summa 24.5 ja 17.3 vahel
2. **Ruudujuur**: Arvutab arvu 144 ruutjuure
3. **Abi**: Kuvab olemasolevad kalkulaatori funktsioonid

## Oodatav väljund

Õnnestunud käivituse korral peaksite nägema väljundit, mis sarnaneb järgmisega:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Vigade lahendamine

### Levinumad probleemid

1. **"OPENAI_API_KEY keskkonnamuutuja ei ole määratud"**
   - Veenduge, et olete määranud `OPENAI_API_KEY` keskkonnamuutuja
   - Taaskäivitage terminal/käsureaaken pärast muutuja seadistamist

2. **"Ühendus localhost:8080 on keelatud"**
   - Veenduge, et MCP kalkulaatori teenus töötab pordil 8080
   - Kontrollige, kas mõni teine teenus kasutab porti 8080

3. **"Autentimine ebaõnnestus"**
   - Kontrollige, kas teie API võti on kehtiv
   - Kontollige, et `OPENAI_BASE_URL` vastab soovitud lõpp-punktile

4. **Maveni ehitusvead**
   - Veenduge, et kasutate Java 21 või uuemat: `java -version`
   - Proovige ehitust puhastada: `mvnw clean`

### Silumine

Silumislogi lubamiseks lisage käivitamisel järgmine JVM argument:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguratsioon

Rakendus on konfigureeritud järgmiselt:
- Vaikimisi kasutab MiniMax-M3; valimiseks seadke `MINIMAX_MODEL_ID` kas `MiniMax-M3` või `MiniMax-M2.7`
- Ühendub `OPENAI_BASE_URL`-iga, kui see on määratud; vastasel juhul kasutab `MINIMAX_REGION=cn_zh` korral `https://api.minimaxi.com/v1` või vaikimisi `https://api.minimax.io/v1`
- Ühendub MCP teenusega aadressil `http://localhost:8080/sse`
- Kasutab päringute jaoks 60-sekundilist ajapiirangut

## Sõltuvused

Projekti võtmesõltuvused:
- **LangChain4j**: tehisintellekti integreerimiseks ja tööriistade haldamiseks
- **LangChain4j MCP**: Model Context Protocol toe jaoks
- **LangChain4j OpenAI official**: MiniMax OpenAI-ühilduva API integreerimiseks
- **Spring Boot**: rakenduse raamistikuks ja sõltuvuste süstimiseks

## Litsents

See projekt on litsentseeritud Apache License 2.0 alusel - üksikasjade jaoks vaadake faili [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->