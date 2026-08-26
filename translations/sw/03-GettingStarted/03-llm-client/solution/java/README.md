# Mteja wa Calculator LLM

Programu ya Java inayoonyesha jinsi ya kutumia LangChain4j kuunganishwa na huduma ya mkalkuleta wa MCP (Model Context Protocol) kupitia API inayolingana na MiniMax OpenAI.

## Mahitaji ya Awali

- Java 21 au zaidi
- Maven 3.6+ (au tumia kifungashio cha Maven kilichojumuishwa)
- Funguo ya API ya MiniMax
- Huduma ya mkalkuleta wa MCP inayotekelezwa kwenye `http://localhost:8080`

## Kupata Funguo ya API

Programu hii inatumia API inayolingana na MiniMax OpenAI. Fuata hatua hizi ili kupata funguo yako na kiungo:

### 1. Chagua kiungo
1. Tumia `https://api.minimax.io/v1` kwa kiungo cha ulimwengu mzima
2. Tumia `https://api.minimaxi.com/v1` kwa kiungo cha China

### 2. Tengeneza funguo ya API
1. Tengeneza funguo ya API ya MiniMax kutoka kwa akaunti yako ya MiniMax
2. Hifadhi funguo mahali salama

### 3. Weka Mabadiliko ya Mazingira (Environment Variables)

#### Kwenye Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Kwenye Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Kwenye macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Usanidi na Ufungaji

1. **Nakili au nenda kwenye saraka ya mradi**

2. **Sakinisha utegemezi**:
   ```cmd
   mvnw clean install
   ```
   Au kama una Maven imewekwa duniani kote:
   ```cmd
   mvn clean install
   ```

3. **Weka mabadiliko ya mazingira** (angalia sehemu ya "Kupata Funguo ya API" hapo juu)

4. **Anzisha Huduma ya MCP Calculator**:
   Hakikisha huduma ya mkalkuleta wa MCP ya sura ya 1 inaendeshwa kwenye `http://localhost:8080/sse`. Inapaswa kuwa inafanya kazi kabla hujaanza mteja.

## Kuendesha Programu

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Kile Programu Hufanya

Programu inaonyesha mwingiliano muhimu tatu na huduma ya mkalkuleta:

1. **Kuzidisha**: Huhesabu jumla ya 24.5 na 17.3
2. **Mzizi wa mraba**: Huhesabu mzizi wa mraba wa 144
3. **Msaada**: Inaonyesha kazi zinazopatikana za mkalkuleta

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
   - Hakikisha umeweka mabadiliko ya mazingira `OPENAI_API_KEY`
   - Restart terminal/command prompt baada ya kuweka mabadiliko

2. **"Muunganisho umezingirwa kwenye localhost:8080"**
   - Hakikisha huduma ya mkalkuleta wa MCP inaendesha kwenye bandari 8080
   - Angalia kama huduma nyingine inatumia bandari 8080

3. **"Uthibitishaji umeshindwa"**
   - Hakikisha funguo yako ya API ni halali
   - Angalia kuwa `OPENAI_BASE_URL` inaendana na kiungo ulichokusudia kutumia

4. **Makosa ya kujenga Maven**
   - Hakikisha unatumia Java 21 au zaidi: `java -version`
   - Jaribu kusafisha ujenzi: `mvnw clean`

### Kurekebisha Makosa ya Programu

Ili kuwezesha kurekodi annatakizo la debug, ongeza hoja ifuatayo ya JVM unapotekeleza:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Usanidi

Programu imesanidiwa kwa:
- Kutumia MiniMax-M3 kwa msingi, au MiniMax-M2.7 wakati `MINIMAX_MODEL_ID` imewekwa
- Kuunganishwa na `OPENAI_BASE_URL` wakati imewekwa; vinginevyo tumia `https://api.minimaxi.com/v1` wakati `MINIMAX_REGION=cn_zh`, au `https://api.minimax.io/v1` kama chaguo msingi
- Kuunganishwa na huduma ya MCP kwenye `http://localhost:8080/sse`
- Kutumia muda wa kusubiri wa sekunde 60 kwa maombi

## Tegemezi

Tegemezi kuu zinazotumiwa katika mradi huu:
- **LangChain4j**: Kwa ujumuishaji wa AI na usimamizi wa zana
- **LangChain4j MCP**: Kwa msaada wa Model Context Protocol
- **LangChain4j OpenAI rasmi**: Kwa ujumuishaji wa API inayolingana na MiniMax OpenAI
- **Spring Boot**: Kwa mfumo wa programu na usimamizi wa utegemezi

## Leseni

Mradi huu umepewa leseni chini ya Leseni ya Apache 2.0 - angalia faili ya [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) kwa maelezo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->