# Calculator LLM Client

LangChain4j प्रयोग गरेर MiniMax OpenAI-समर्थित API मार्फत MCP (Model Context Protocol) कलकुलेटर सेवा सँग कसरी जडान गर्ने देखाउने एउटा Java एप्लिकेशन।

## पूर्वआवश्यकताहरू

- Java २१ वा माथिको संस्करण
- Maven ३.६+ (वा संगै आएको Maven wrapper प्रयोग गर्नुहोस्)
- MiniMax API की
- `http://localhost:8080` मा चलिरहेको MCP कलकुलेटर सेवा

## API की कसरी प्राप्त गर्ने

यो एप्लिकेशन MiniMax OpenAI-समर्थित API प्रयोग गर्छ। तपाईंको की र endpoint पाउन यी चरणहरू पालन गर्नुहोस्:

### १. Endpoint छनौट गर्नुहोस्
१. विश्वव्यापी endpoint का लागि `https://api.minimax.io/v1` प्रयोग गर्नुहोस्
२. चीन endpoint का लागि `https://api.minimaxi.com/v1` प्रयोग गर्नुहोस्

### २. API की सिर्जना गर्नुहोस्
१. आफ्नो MiniMax खाताबाट MiniMax API की सिर्जना गर्नुहोस्
२. की राम्रोसँग सुरक्षित राख्नुहोस्

### ३. Environment Variables सेट गर्नुहोस्

#### Windows (कमाण्ड प्रॉम्प्ट) मा:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (PowerShell) मा:
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux मा:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## सेटअप र स्थापना

१. **प्रोजेक्ट डिरेक्टरी क्लोन वा नेभिगेट गर्नुहोस्**

२. **निर्भरता स्थापना गर्नुहोस्**:
   ```cmd
   mvnw clean install
   ```
   वा Maven पहिले नै ग्लोबली स्थापित छ भने:
   ```cmd
   mvn clean install
   ```

३. **Environment Variables सेटअप गर्नुहोस्** ("Getting the API Key" सेक्सन हेर्नुहोस्)

४. **MCP Calculator सेवा सुरु गर्नुहोस्**:
   chapter 1 को MCP calculator सेवा `http://localhost:8080/sse` मा चलिरहेको हुनुपर्छ। यसलाई क्लाइन्ट सुरु गर्नु अघि चलिरहेको हुन जरुरी छ।

## एप्लिकेशन कसरी चलाउने

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## एप्लिकेशनले के गर्छ

एप्लिकेशनले कलकुलेटर सेवासँग तीन मुख्य अन्तरक्रियाहरू देखाउँछ:

१. **जोड**: २४.५ र १७.३ को योगफल गणना गर्छ
२. **वर्गमूल**: १४४ को वर्गमूल गणना गर्छ
३. **मद्दत**: उपलब्ध कलकुलेटर फङ्सनहरू देखाउँछ

## अपेक्षित नतिजा

सफलतापूर्वक चल्दा, तपाईंले यस्तै नतिजा देख्नु हुनेछ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या समाधान

### सामान्य समस्याहरू

१. **"OPENAI_API_KEY environment variable सेट गरिएको छैन"**
   - निश्चित गर्नुहोस् `OPENAI_API_KEY` environment variable सेट गरिएको छ
   - सेट गरेपछि तपाइँको टर्मिनल/कमाण्ड प्रॉम्प्ट पुनः सुरु गर्नुहोस्

२. **"localhost:8080 मा कनेक्शन अस्वीकृत"**
   - MCP calculator सेवा पोर्ट ८०८० मा चलिरहेको छ भनी सुनिश्चित गर्नुहोस्
   - अर्को सेवा पोर्ट ८०८० प्रयोग गरिरहेको छैन भनी जाँच गर्नुहोस्

३. **"प्रमाणीकरण असफल भयो"**
   - तपाईंको API की मान्य छ भनी प्रमाणीकरण गर्नुहोस्
   - `OPENAI_BASE_URL` तपाइँले प्रयोग गर्न चाहेको endpoint सँग मेल खान्छ भनी जाँच गर्नुहोस्

४. **Maven बिल्ड त्रुटिहरू**
   - Java २१ वा माथि संस्करण प्रयोग गरिरहनु भएको छ भनी सुनिश्चित गर्नुहोस्: `java -version`
   - बिल्ड सफा गर्न प्रयास गर्नुहोस्: `mvnw clean`

### डीबगिङ

डीबग लगिङ सक्षम पार्न, चलाउँदा तलको JVM argument थप्नुहोस्:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कन्फिगरेसन

एप्लिकेशनमा कन्फिगर गरिएको छ:
- डिफ़ल्ट रूपमा MiniMax-M3 प्रयोग गर्न; `MINIMAX_MODEL_ID` सेट गरेर `MiniMax-M3` वा `MiniMax-M2.7` चयन गर्न सकिन्छ
- `OPENAI_BASE_URL` सेट भएको बेला त्यसमा जडान हुन्छ; नभएमा `MINIMAX_REGION=cn_zh` हुँदा `https://api.minimaxi.com/v1` वा डिफ़ल्ट रूपमा `https://api.minimax.io/v1` प्रयोग गर्छ
- MCP सेवा सँग `http://localhost:8080/sse` मा जडान हुन्छ
- अनुरोधको लागि ६० सेकेन्डको टाइमआउट प्रयोग गर्छ

## निर्भरशिलाहरू

यस प्रोजेक्टमा प्रयोग भएका मुख्य निर्भरशिलाहरू:
- **LangChain4j**: AI एकीकरण र उपकरण व्यवस्थापनका लागि
- **LangChain4j MCP**: Model Context Protocol समर्थनका लागि
- **LangChain4j OpenAI official**: MiniMax OpenAI-समर्थित API एकीकरणका लागि
- **Spring Boot**: एप्लिकेशन फ्रेमवर्क र निर्भरता इन्जेक्शनका लागि

## लाइसेन्स

यो प्रोजेक्ट Apache License २.० अन्तर्गत लाइसेन्स प्राप्त छ - विवरणका लागि [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फाइल हेर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->