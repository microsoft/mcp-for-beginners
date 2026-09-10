# Skaičiuotuvo LLM klientas

Java programa, demonstruojanti, kaip naudoti LangChain4j, norint prijungti MCP (Modelio konteksto protokolo) skaičiuotuvo paslaugą per MiniMax OpenAI suderinamą API.

## Priešreikšmės

- Java 21 arba naujesnė versija
- Maven 3.6+ (arba naudokite pridėtą Maven wrapper)
- MiniMax API raktas
- MCP skaičiuotuvo paslauga veikianti adresu `http://localhost:8080`

## Kaip gauti API raktą

Ši programa naudoja MiniMax OpenAI suderinamą API. Sekite šiuos žingsnius, kad gautumėte savo raktą ir galutinį tašką:

### 1. Pasirinkite galinį tašką
1. Naudokite `https://api.minimax.io/v1` kaip globalų galinį tašką
2. Naudokite `https://api.minimaxi.com/v1` kaip Kinijos galinį tašką

### 2. Sukurkite API raktą
1. Sukurkite MiniMax API raktą savo MiniMax paskyroje
2. Laikykite raktą saugioje vietoje

### 3. Nustatykite aplinkos kintamuosius

#### Windows (Komandų eilutė):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (PowerShell):
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

## Įdiegimas ir paruošimas

1. **Klonuokite arba eikite į projekto katalogą**

2. **Įdiekite priklausomybes**:
   ```cmd
   mvnw clean install
   ```
   Arba, jei turite Maven įdiegtą globaliai:
   ```cmd
   mvn clean install
   ```

3. **Nustatykite aplinkos kintamuosius** (žr. skyrių „Kaip gauti API raktą“ aukščiau)

4. **Paleiskite MCP skaičiuotuvo paslaugą**:
   Įsitikinkite, kad 1-ojo skyriaus MCP skaičiuotuvo paslauga veikia adresu `http://localhost:8080/sse`. Ji turi veikti prieš paleidžiant klientą.

## Programos paleidimas

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ką programa atlieka

Programa demonstruoja tris pagrindinius sąveikos su skaičiuotuvo paslauga būdus:

1. **Sudėtis**: Apskaičiuoja 24.5 ir 17.3 sumą
2. **Kvadratinė šaknis**: Apskaičiuoja 144 kvadratinę šaknį
3. **Pagalba**: Parodo galimas skaičiuotuvo funkcijas

## Tikėtinas rezultatas

Sėkmingai paleidus turėtumėte matyti panašų rezultatą:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Klaidų šalinimas

### Dažnos problemos

1. **„OPENAI_API_KEY aplinkos kintamasis nenustatytas“**
   - Įsitikinkite, kad nustatėte `OPENAI_API_KEY` aplinkos kintamąjį
   - Perkraukite terminalą/komandų eilutę po kintamojo nustatymo

2. **„Ryšys su localhost:8080 atmestas“**
   - Patikrinkite, ar MCP skaičiuotuvo paslauga veikia 8080 prievade
   - Patikrinkite, ar kitas servisas nenaudoja 8080 prievado

3. **„Autentifikavimas nesėkmingas“**
   - Patikrinkite, ar jūsų API raktas galioja
   - Įsitikinkite, kad `OPENAI_BASE_URL` atitinka norimą naudoti galinį tašką

4. **Maven kompiliavimo klaidos**
   - Patikrinkite, ar naudojate Java 21 ar naujesnę: `java -version`
   - Pabandykite išvalyti projektą: `mvnw clean`

### Derinimas

Norėdami įjungti derinimo žurnalus, pridėkite šį JVM argumentą paleidžiant:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigūracija

Programa yra sukonfigūruota taip:
- Pagal nutylėjimą naudoja MiniMax-M3; nustatykite `MINIMAX_MODEL_ID`, kad pasirinktumėte tarp `MiniMax-M3` arba `MiniMax-M2.7`
- Jungiasi prie `OPENAI_BASE_URL`, jei jis nustatytas; kitaip naudoja `https://api.minimaxi.com/v1` kai `MINIMAX_REGION=cn_zh`, arba `https://api.minimax.io/v1` pagal nutylėjimą
- Jungiasi prie MCP paslaugos adresu `http://localhost:8080/sse`
- Naudoja 60 sekundžių laukimo limitą užklausoms

## Priklausomybės

Pagrindinės šiame projekte naudojamos priklausomybės:
- **LangChain4j**: AI integracijai ir įrankių valdymui
- **LangChain4j MCP**: Modelio konteksto protokolo palaikymui
- **LangChain4j OpenAI oficialus**: MiniMax OpenAI suderinamos API integracijai
- **Spring Boot**: Programos karkasui ir priklausomybių injekcijai

## Licencija

Šis projektas licencijuotas pagal Apache licenciją 2.0 - žr. [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) failą detaliau.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->