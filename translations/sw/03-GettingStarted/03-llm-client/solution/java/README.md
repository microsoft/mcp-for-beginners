# Mteja wa Calculator LLM

Programu ya Java inayothibitisha jinsi ya kutumia LangChain4j kuunganishwa na huduma ya kalikuleta MCP (Model Context Protocol) kupitia API inayolingana na MiniMax OpenAI.

## Mahitaji ya Awali

- Java 21 au zaidi
- Maven 3.6+ (au tumia wrapper ya Maven iliyojumuishwa)
- Funguo ya API ya MiniMax
- Huduma ya kalikuleta MCP inayotendeka kwenye `http://localhost:8080`

## Kupata Funguo ya API

Programu hii inatumia API inayolingana na MiniMax OpenAI. Fuata hatua hizi kupata funguo na sehemu ya kuunganishia:

### 1. Chagua sehemu ya kuunganishia
1. Tumia `https://api.minimax.io/v1` kwa sehemu ya dunia nzima
2. Tumia `https://api.minimaxi.com/v1` kwa sehemu ya China

### 2. Tengeneza funguo ya API
1. Tengeneza funguo ya MiniMax API kutoka kwenye akaunti yako ya MiniMax
2. Hifadhi funguo mahali salama

### 3. Weka Mabadiliko ya Mazingira

#### Katika Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Katika Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Katika macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Usanidi na Ufungaji

1. **Nakili au nenda kwenye saraka ya mradi**

2. **Sakinisha mahitaji**:
   ```cmd
   mvnw clean install
   ```
   Au ikiwa una Maven umewekwa kimataifa:
   ```cmd
   mvn clean install
   ```

3. **Weka mabadiliko ya mazingira** (angalau kwenye sehemu "Kupata Funguo ya API" hapo juu)

4. **Anzisha Huduma ya Kalikuleta MCP**:
   Hakikisha huduma ya kalikuleta MCP ya sura ya 1 inafanya kazi kwenye `http://localhost:8080/sse`. Hii inapaswa kuwa inafanya kazi kabla ya kuanzisha mteja.

## Kuendesha Programu

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Kile Programu Hufanya

Programu inathibitisha mwingiliano kuu tatu na huduma ya kalikuleta:

1. **Kuweka pamoja**: Huhesabu jumla ya 24.5 na 17.3
2. **Mizizi wa Mraba**: Huhesabu mizizi ya mraba ya 144
3. **Msaada**: Inaonyesha kazi zinapatikana za kalikuleta

## Matokeo Yanayotarajiwa

Unapoendesha kwa mafanikio, unapaswa kuona matokeo yanayofanana na:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Utatuzi wa Matatizo

### Masuala ya Kawaida

1. **"Mabadiliko ya mazingira ya OPENAI_API_KEY hayajawekwa"**
   - Hakikisha umeweka mabadiliko ya mazingira ya `OPENAI_API_KEY`
   - Zima na anzisha tena terminal/command prompt baada ya kuweka mabadiliko hayo

2. **"Muunganisho ulikanushwa kwa localhost:8080"**
   - Hakikisha huduma ya kalikuleta MCP inafanya kazi kwenye bandari 8080
   - Angalia kama huduma nyingine inatumia bandari 8080

3. **"Uthibitishaji umeshindikana"**
   - Thibitisha kuwa funguo yako ya API ni halali
   - Hakikisha `OPENAI_BASE_URL` inaendana na sehemu ya kuunganishia uliokusudia kutumia

4. **Makosa ya kujenga Maven**
   - Hakikisha unatumia Java 21 au zaidi: `java -version`
   - Jaribu kusafisha ujenzi: `mvnw clean`

### Kupepesa Masuala

Ili kuwezesha kurekodi matatizo, ongeza hujuma ifuatayo ya JVM unapoendesha:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Usanidi

Programu imewekwa ili:
- Tumia MiniMax-M3 kwa default; weka `MINIMAX_MODEL_ID` kuchagua kati ya `MiniMax-M3` au `MiniMax-M2.7`
- Unganisha na `OPENAI_BASE_URL` wakati umewekwa; vinginevyo tumia `https://api.minimaxi.com/v1` wakati `MINIMAX_REGION=cn_zh`, au `https://api.minimax.io/v1` kwa default
- Unganisha na huduma ya MCP kwenye `http://localhost:8080/sse`
- Tumia muda wa dakika 60 kwa maombi

## Mategemeo

Mategemeo muhimu yanayotumika katika mradi huu:
- **LangChain4j**: Kwa ushirikiano wa AI na usimamizi wa zana
- **LangChain4j MCP**: Kwa msaada wa Protokoli ya Muktadha wa Mfano
- **LangChain4j OpenAI rasmi**: Kwa ushirikiano wa API inayolingana na MiniMax OpenAI
- **Spring Boot**: Kwa mfumo wa programu na sindano ya utegemezi

## Leseni

Mradi huu una leseni chini ya Apache Leseni 2.0 - tazama faili la [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) kwa maelezo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->