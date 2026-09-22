# Skaičiuotuvas LLM klientas

> [!NOTE]
> Šis sprendimas jungiasi prie kurso legacy HTTP+SSE skaičiuotuvo paslaugos ir
> taikomas MCP `2025-11-25` SDK API. Tai nėra `2026-07-28` Streamable HTTP
> pavyzdys.

Java programa, parodanti, kaip naudoti LangChain4j, kad būtų galima jungtis prie MCP (Modelio konteksto protokolo) skaičiuotuvo paslaugos per MiniMax OpenAI suderinamą API.

## Reikalavimai

- Java 21 arba naujesnė versija
- Maven 3.6+ (arba naudoti pridėtą Maven wrapper)
- MiniMax API raktas
- MCP skaičiuotuvo paslauga veikianti adresu `http://localhost:8080`

## Kaip gauti API raktą

Ši programa naudoja MiniMax OpenAI suderinamą API. Sekite šiuos veiksmus, kad gautumėte savo raktą ir pabaigos tašką:

### 1. Pasirinkite pabaigos tašką
1. Naudokite `https://api.minimax.io/v1` globaliam pabaigos taškui
2. Naudokite `https://api.minimaxi.com/v1` Kinijos regiono pabaigos taškui

### 2. Sukurkite API raktą
1. Sukurkite MiniMax API raktą savo MiniMax paskyroje
2. Saugokite raktą saugioje vietoje

### 3. Nustatykite aplinkos kintamuosius

#### Windows (Command Prompt):
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

## Diegimas ir paruošimas

1. **Klonuokite arba eikite į projekto katalogą**

2. **Įdiekite priklausomybes**:
   ```cmd
   mvnw clean install
   ```
   Arba jei Maven įdiegtas globaliai:
   ```cmd
   mvn clean install
   ```

3. **Nustatykite aplinkos kintamuosius** (žr. aukščiau skyrių "Kaip gauti API raktą")

4. **Paleiskite MCP skaičiuotuvo paslaugą**:
   Įsitikinkite, kad 1-oje skyriaus MCP skaičiuotuvo paslauga veikia adresu `http://localhost:8080/sse`. Ji turi veikti prieš paleidžiant klientą.

## Programos paleidimas

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ką daro programa

Programa demonstruoja tris pagrindinius veiksmus su skaičiuotuvo paslauga:

1. **Sudėtis**: Apskaičiuoja 24.5 ir 17.3 sumą
2. **Kvadratinė šaknis**: Apskaičiuoja 144 kvadratinę šaknį
3. **Pagalba**: Parodo galimas skaičiuotuvo funkcijas

## Tikėtinas rezultatas

Sėkmingai paleidus, ekrane turėtų atsirasti panašus išvesties rezultatas:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Problemų sprendimas

### Dažnos problemos

1. **"OPENAI_API_KEY aplinkos kintamasis nėra nustatytas"**
   - Įsitikinkite, kad nustatėte `OPENAI_API_KEY` aplinkos kintamąjį
   - Po nustatymo perkraukite terminalą/komandinę eilutę

2. **"Nepavyksta prisijungti prie localhost:8080"**
   - Patikrinkite, ar MCP skaičiuotuvo paslauga veikia uoste 8080
   - Patikrinkite, ar kitas servisas neužima uosto 8080

3. **"Autentifikacija nepavyko"**
   - Patikrinkite, ar jūsų API raktas yra galiojantis
   - Įsitikinkite, kad `OPENAI_BASE_URL` atitinka naudojamą pabaigos tašką

4. **Maven kūrimo klaidos**
   - Įsitikinkite, kad naudojate Java 21 arba naujesnę: `java -version`
   - Pabandykite išvalyti build: `mvnw clean`

### Derinimas

Norėdami įjungti derinimo žurnalo įrašymą, paleisdami pridėkite šią JVM parinktį:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigūracija

Programa yra sukonfigūruota:
- Pagal numatytuosius nustatymus naudoti MiniMax-M3; nustatykite `MINIMAX_MODEL_ID`, kad pasirinktumėte `MiniMax-M3` arba `MiniMax-M2.7`
- Prisijungti prie `OPENAI_BASE_URL`, kai jis nustatytas; kitu atveju naudoti `https://api.minimaxi.com/v1` kai `MINIMAX_REGION=cn_zh`, arba `https://api.minimax.io/v1` pagal numatytuosius nustatymus
- Prisijungti prie MCP paslaugos adresu `http://localhost:8080/sse`
- Naudoti 60 sekundžių užklausų timeout

## Priklausomybės

Pagrindinės priklausomybės šiame projekte:
- **LangChain4j**: dirbtinio intelekto integracijai ir įrankių valdymui
- **LangChain4j MCP**: Modelio konteksto protokolo palaikymui
- **LangChain4j OpenAI official**: MiniMax OpenAI suderinamos API integracijai
- **Spring Boot**: programos karkasui ir priklausomybių injekcijai

## Licencija

Šis projektas licencijuotas pagal Apache licenciją 2.0 - žr. [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) failą dėl detalių.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->