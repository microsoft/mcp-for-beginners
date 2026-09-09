# Skaičiuotuvas LLM klientas

Java programa, rodanti, kaip naudoti LangChain4j, kad prisijungtumėte prie MCP (Modelio konteksto protokolo) skaičiuotuvo paslaugos per MiniMax OpenAI suderinamą API.

## Prieš tai būtina turėti

- Java 21 arba naujesnę versiją
- Maven 3.6+ (arba naudokite įtrauktą Maven wrapper)
- MiniMax API raktą
- Veikiančią MCP skaičiuotuvo paslaugą adresu `http://localhost:8080`

## Kaip gauti API raktą

Ši programa naudoja MiniMax OpenAI suderinamą API. Sekite šiuos veiksmus, kad gautumėte savo raktą ir galinį tašką:

### 1. Pasirinkite galinį tašką
1. Naudokite `https://api.minimax.io/v1` – globaliam galiniam taškui
2. Naudokite `https://api.minimaxi.com/v1` – Kinijos galiniam taškui

### 2. Sukurkite API raktą
1. Sukurkite MiniMax API raktą savo MiniMax paskyroje
2. Saugiai išsaugokite šį raktą

### 3. Nustatykite aplinkos kintamuosius

#### Windows (Komandinėje eilutėje):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (PowerShell aplinkoje):
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

## Diegimas ir nustatymas

1. **Klonuokite arba pereikite į projekto katalogą**

2. **Įdiekite priklausomybes**:
   ```cmd
   mvnw clean install
   ```
   Arba, jei turite globaliai įdiegtą Maven:
   ```cmd
   mvn clean install
   ```

3. **Nustatykite aplinkos kintamuosius** (žr. aukščiau skyrių "Kaip gauti API raktą")

4. **Paleiskite MCP skaičiuotuvo paslaugą**:
   Įsitikinkite, kad 1 skyriuje aptarta MCP skaičiuotuvo paslauga veikia adresu `http://localhost:8080/sse`. Ji turi veikti prieš paleidžiant klientą.

## Programos paleidimas

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ką daro programa

Programa demonstruoja tris pagrindinius veiksmus su skaičiuotuvo paslauga:

1. **Sudėtis**: Apskaičiuoja 24,5 ir 17,3 sumą
2. **Kvadratinė šaknis**: Apskaičiuoja 144 kvadratinę šaknį
3. **Pagalba**: Rodo prieinamas skaičiuotuvo funkcijas

## Tikėtinas rezultatas

Sėkmingai paleidus, turėtumėte pamatyti panašų išvestį:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Problemos sprendimas

### Dažnos problemos

1. **"OPENAI_API_KEY aplinkos kintamasis nėra nustatytas"**
   - Įsitikinkite, kad nustatėte `OPENAI_API_KEY` aplinkos kintamąjį
   - Po nustatymo iš naujo paleiskite terminalą/komandų eilutę

2. **"Negalima prisijungti prie localhost:8080"**
   - Įsitikinkite, kad MCP skaičiuotuvo paslauga veikia 8080 prievade
   - Patikrinkite, ar kitos paslaugos nenaudoja 8080 prievado

3. **"Autentifikacija nepavyko"**
   - Patikrinkite, ar jūsų API raktas galioja
   - Užtikrinkite, kad `OPENAI_BASE_URL` atitinka jūsų pasirinkto galinio taško adresą

4. **Maven kūrimo klaidos**
   - Patikrinkite, ar naudojate Java 21 ar naujesnę versiją: `java -version`
   - Pabandykite išvalyti kūrimą: `mvnw clean`

### Derinimas

Norėdami įjungti derinimo žurnalą, paleidimo metu pridėkite šią JVM parinktį:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigūracija

Programa sukonfigūruota taip:
- Pagal numatytąją reikšmę naudoja MiniMax-M3 arba MiniMax-M2.7, jei nustatytas `MINIMAX_MODEL_ID`
- Prisijungia prie `OPENAI_BASE_URL`, jei jis nustatytas; kitaip naudoja `https://api.minimaxi.com/v1`, jei `MINIMAX_REGION=cn_zh`, arba `https://api.minimax.io/v1` pagal numatytuosius nustatymus
- Prisijungia prie MCP paslaugos adresu `http://localhost:8080/sse`
- Naudoja 60 sekundžių užklausų laiko limitą

## Priklausomybės

Pagrindinės šio projekto priklausomybės:
- **LangChain4j**: Dirbtinio intelekto integracijai ir įrankių valdymui
- **LangChain4j MCP**: Modelio konteksto protokolo palaikymui
- **LangChain4j OpenAI official**: MiniMax OpenAI suderinamos API integracijai
- **Spring Boot**: Programų karkasui ir priklausomybių injekcijai

## Licencija

Šis projektas licencijuotas pagal Apache licenciją 2.0 - žr. [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) failą dėl detalių.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->