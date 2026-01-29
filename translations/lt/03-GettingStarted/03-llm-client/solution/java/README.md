# Skaičiuotuvo LLM Klientas

Java programa, demonstruojanti, kaip naudoti LangChain4j prisijungimui prie MCP (Model Context Protocol) skaičiuotuvo paslaugos su GitHub Models integracija.

## Reikalavimai

- Java 21 ar naujesnė versija
- Maven 3.6+ (arba naudokite pridėtą Maven wrapper)
- GitHub paskyra su prieiga prie GitHub Models
- MCP skaičiuotuvo paslauga, veikianti adresu `http://localhost:8080`

## GitHub Token gavimas

Ši programa naudoja GitHub Models, kuriems reikalingas GitHub asmeninis prieigos raktas. Atlikite šiuos veiksmus, kad gautumėte savo raktą:

### 1. Prieiga prie GitHub Models
1. Eikite į [GitHub Models](https://github.com/marketplace/models)
2. Prisijunkite prie savo GitHub paskyros
3. Paprašykite prieigos prie GitHub Models, jei dar jos neturite

### 2. Sukurkite asmeninį prieigos raktą
1. Eikite į [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Spustelėkite "Generate new token" → "Generate new token (classic)"
3. Suteikite savo raktui aprašomąjį pavadinimą (pvz., "MCP Calculator Client")
4. Nustatykite galiojimo laiką pagal poreikį
5. Pasirinkite šias teises (scopes):
   - `repo` (jei reikia prieigos prie privačių saugyklų)
   - `user:email`
6. Spustelėkite "Generate token"
7. **Svarbu**: Nukopijuokite raktą iš karto – vėliau jo nebegalėsite matyti!

### 3. Nustatykite aplinkos kintamąjį

#### Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Diegimas ir nustatymas

1. **Klonuokite arba pereikite į projekto katalogą**

2. **Įdiekite priklausomybes**:
   ```cmd
   mvnw clean install
   ```
   Arba, jei Maven įdiegtas globaliai:
   ```cmd
   mvn clean install
   ```

3. **Nustatykite aplinkos kintamąjį** (žr. skyrių "GitHub Token gavimas")

4. **Paleiskite MCP skaičiuotuvo paslaugą**:
   Įsitikinkite, kad 1 skyriaus MCP skaičiuotuvo paslauga veikia adresu `http://localhost:8080/sse`. Ji turi būti paleista prieš pradedant klientą.

## Programos paleidimas

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ką programa daro

Programa demonstruoja tris pagrindines sąveikas su skaičiuotuvo paslauga:

1. **Sudėtis**: Apskaičiuoja 24.5 ir 17.3 sumą
2. **Kvadratinė šaknis**: Apskaičiuoja 144 kvadratinę šaknį
3. **Pagalba**: Parodo galimas skaičiuotuvo funkcijas

## Tikėtinas rezultatas

Sėkmingai paleidus, turėtumėte matyti rezultatą, panašų į:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Trikčių šalinimas

### Dažnos problemos

1. **"GITHUB_TOKEN environment variable not set"**
   - Įsitikinkite, kad nustatėte `GITHUB_TOKEN` aplinkos kintamąjį
   - Perkraukite terminalą/komandinę eilutę po kintamojo nustatymo

2. **"Connection refused to localhost:8080"**
   - Patikrinkite, ar MCP skaičiuotuvo paslauga veikia 8080 prievade
   - Patikrinkite, ar kitas procesas nenaudoja 8080 prievado

3. **"Authentication failed"**
   - Patikrinkite, ar jūsų GitHub raktas galioja ir turi tinkamas teises
   - Įsitikinkite, kad turite prieigą prie GitHub Models

4. **Maven kūrimo klaidos**
   - Įsitikinkite, kad naudojate Java 21 ar naujesnę versiją: `java -version`
   - Pabandykite išvalyti kūrimą: `mvnw clean`

### Derinimas

Norėdami įjungti derinimo žurnalus, pridėkite šį JVM argumentą paleidžiant:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigūracija

Programa sukonfigūruota:
- Naudoti GitHub Models su `gpt-4.1-nano` modeliu
- Prisijungti prie MCP paslaugos adresu `http://localhost:8080/sse`
- Naudoti 60 sekundžių užklausų laiko limitą
- Įjungti užklausų/atsakymų žurnalavimą derinimui

## Priklausomybės

Pagrindinės priklausomybės, naudojamos šiame projekte:
- **LangChain4j**: AI integracijai ir įrankių valdymui
- **LangChain4j MCP**: Model Context Protocol palaikymui
- **LangChain4j GitHub Models**: GitHub Models integracijai
- **Spring Boot**: Programos karkasui ir priklausomybių injekcijai

## Licencija

Šis projektas licencijuotas pagal Apache License 2.0 – daugiau informacijos rasite [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) faile.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kilusius dėl šio vertimo naudojimo.