# Calculator LLM Client

Programu ya Java inayonyesha jinsi ya kutumia LangChain4j kuunganishwa na huduma ya kalkuleta ya MCP (Model Context Protocol) yenye ushirikiano na GitHub Models.

## Mahitaji

- Java 21 au zaidi
- Maven 3.6+ (au tumia Maven wrapper iliyojumuishwa)
- Akaunti ya GitHub yenye ufikiaji wa GitHub Models
- Huduma ya kalkuleta ya MCP inayotumika kwenye `http://localhost:8080`

## Kupata Tokeni ya GitHub

Programu hii inatumia GitHub Models ambayo inahitaji tokeni ya ufikiaji wa kibinafsi ya GitHub. Fuata hatua hizi kupata tokeni yako:

### 1. Ingia GitHub Models
1. Nenda kwenye [GitHub Models](https://github.com/marketplace/models)
2. Ingia kwa akaunti yako ya GitHub
3. Omba ruhusa ya kutumia GitHub Models kama bado hujafanya hivyo

### 2. Tengeneza Tokeni ya Ufikiaji wa Kibinafsi
1. Nenda kwenye [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Bonyeza "Generate new token" → "Generate new token (classic)"
3. Toa jina linaloelezea tokeni yako (mfano, "MCP Calculator Client")
4. Weka muda wa kumalizika kulingana na mahitaji
5. Chagua maeneo yafuatayo:
   - `repo` (kama unahitaji kufikia repositories binafsi)
   - `user:email`
6. Bonyeza "Generate token"
7. **Muhimu**: Nakili tokeni mara moja - hutaweza kuiona tena!

### 3. Weka Kigezo cha Mazingira

#### Kwenye Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Kwenye Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Kwenye macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Usanidi na Ufungaji

1. **Fanya clone au nenda kwenye saraka ya mradi**

2. **Sakinisha utegemezi**:
   ```cmd
   mvnw clean install
   ```
   Au kama una Maven imewekwa kimataifa:
   ```cmd
   mvn clean install
   ```

3. **Weka kigezo cha mazingira** (angalia sehemu ya "Kupata Tokeni ya GitHub" hapo juu)

4. **Anzisha Huduma ya MCP Calculator**:
   Hakikisha huduma ya kalkuleta ya MCP ya sura ya 1 inafanya kazi kwenye `http://localhost:8080/sse`. Huduma hii inapaswa kuwa inayoendesha kabla ya kuanzisha client.

## Kuendesha Programu

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Kazi za Programu

Programu inaonyesha mwingiliano kuu tatu na huduma ya kalkuleta:

1. **Jumlisha**: Huhesabu jumla ya 24.5 na 17.3
2. **Mzizi wa Mraba**: Huhesabu mzizi wa mraba wa 144
3. **Msaada**: Inaonyesha kazi zinazopatikana za kalkuleta

## Matokeo Yanayotarajiwa

Unapofanikisha kuendesha, utaona matokeo yanayofanana na:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Utatuzi wa Matatizo

### Masuala ya Kawaida

1. **"GITHUB_TOKEN environment variable not set"**
   - Hakikisha umeweka kigezo cha mazingira `GITHUB_TOKEN`
   - Anzisha upya terminal/command prompt baada ya kuweka kigezo

2. **"Connection refused to localhost:8080"**
   - Hakikisha huduma ya MCP calculator inaendesha kwenye port 8080
   - Angalia kama huduma nyingine inatumia port 8080

3. **"Authentication failed"**
   - Hakiki tokeni yako ya GitHub ni halali na ina ruhusa sahihi
   - Angalia kama una ufikiaji wa GitHub Models

4. **Makosa ya ujenzi wa Maven**
   - Hakikisha unatumia Java 21 au zaidi: `java -version`
   - Jaribu kusafisha ujenzi: `mvnw clean`

### Ufuatiliaji wa Makosa

Ili kuwezesha kurekodi makosa ya debug, ongeza hoja ifuatayo ya JVM unapoendesha:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Usanidi

Programu imewekwa kutumia:
- GitHub Models na mfano `gpt-4.1-nano`
- Kuunganishwa na huduma ya MCP kwenye `http://localhost:8080/sse`
- Muda wa kusubiri majibu wa sekunde 60
- Kuwezesha kurekodi maombi/jawabu kwa ajili ya debugging

## Tegemezi

Tegemezi muhimu zinazotumika katika mradi huu:
- **LangChain4j**: Kwa ushirikiano wa AI na usimamizi wa zana
- **LangChain4j MCP**: Kwa msaada wa Model Context Protocol
- **LangChain4j GitHub Models**: Kwa ushirikiano na GitHub Models
- **Spring Boot**: Kwa mfumo wa programu na sindano ya utegemezi

## Leseni

Mradi huu umepewa leseni chini ya Apache License 2.0 - angalia faili la [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) kwa maelezo zaidi.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.