# कैलकुलेटर LLM क्लाइंट

एक जावा एप्लिकेशन जो दिखाता है कि LangChain4j का उपयोग करके MiniMax OpenAI- अनुकूल API के माध्यम से MCP (मॉडल कॉन्टेक्स्ट प्रोटोकॉल) कैलकुलेटर सेवा से कैसे कनेक्ट किया जाए।

## पूर्व आवश्यकताएँ

- जावा 21 या उससे ऊपर
- Maven 3.6+ (या शामिल Maven व्रैपर का उपयोग करें)
- एक MiniMax API कुंजी
- `http://localhost:8080` पर चल रही MCP कैलकुलेटर सेवा

## API कुंजी प्राप्त करना

यह एप्लिकेशन MiniMax OpenAI- अनुकूल API का उपयोग करता है। अपनी कुंजी और एंडपॉइंट प्राप्त करने के लिए निम्न चरणों का पालन करें:

### 1. एक एंडपॉइंट चुनें
1. वैश्विक एंडपॉइंट के लिए `https://api.minimax.io/v1` का उपयोग करें
2. चीन एंडपॉइंट के लिए `https://api.minimaxi.com/v1` का उपयोग करें

### 2. API कुंजी बनाएँ
1. अपने MiniMax खाते से एक MiniMax API कुंजी बनाएँ
2. कुंजी को कहीं सुरक्षित रखें

### 3. पर्यावरण चर सेट करें

#### Windows (कमांड प्रॉम्प्ट) पर:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (पावरशेल) पर:
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux पर:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## सेटअप और इंस्टॉलेशन

1. **प्रोजेक्ट डायरेक्टरी को क्लोन करें या नेविगेट करें**

2. **निर्भरता इंस्टॉल करें**:
   ```cmd
   mvnw clean install
   ```
   या यदि आपने Maven ग्लोबली इंस्टॉल किया है:
   ```cmd
   mvn clean install
   ```

3. **पर्यावरण चर सेट करें** (ऊपर "API कुंजी प्राप्त करना" अनुभाग देखें)

4. **MCP कैलकुलेटर सेवा शुरू करें**:
   सुनिश्चित करें कि आपके पास अध्याय 1 की MCP कैलकुलेटर सेवा `http://localhost:8080/sse` पर चल रही है। यह क्लाइंट शुरू करने से पहले चल रही होनी चाहिए।

## एप्लिकेशन चलाना

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## एप्लिकेशन क्या करता है

एप्लिकेशन कैलकुलेटर सेवा के साथ तीन मुख्य इंटरैक्शन दिखाता है:

1. **जोड़ना**: 24.5 और 17.3 का योग निकालता है
2. **वर्गमूल**: 144 का वर्गमूल निकालता है
3. **मदद**: उपलब्ध कैलकुलेटर फ़ंक्शन्स दिखाता है

## अपेक्षित आउटपुट

सफलतापूर्वक चलाने पर, आपको इस तरह का आउटपुट दिखाई देगा:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या निवारण

### सामान्य समस्याएं

1. **"OPENAI_API_KEY पर्यावरण चर सेट नहीं है"**
   - सुनिश्चित करें कि आपने `OPENAI_API_KEY` पर्यावरण चर सेट किया है
   - चर सेट करने के बाद अपने टर्मिनल/कमांड प्रॉम्प्ट को पुनः प्रारंभ करें

2. **"localhost:8080 से कनेक्शन अस्वीकार"**
   - सुनिश्चित करें कि MCP कैलकुलेटर सेवा पोर्ट 8080 पर चल रही है
   - जांचें कि कोई अन्य सेवा पोर्ट 8080 का उपयोग तो नहीं कर रही है

3. **"प्रमाणीकरण विफल"**
   - अपनी API कुंजी मान्य है यह सत्यापित करें
   - जांचें कि `OPENAI_BASE_URL` उस एंडपॉइंट से मेल खाता हो जिसे आप उपयोग करना चाहते हैं

4. **Maven बिल्ड त्रुटियां**
   - सुनिश्चित करें कि आप जावा 21 या उससे ऊपर उपयोग कर रहे हैं: `java -version`
   - बिल्ड साफ़ करने की कोशिश करें: `mvnw clean`

### डिबगिंग

डिबग लॉगिंग सक्षम करने के लिए, रन करते समय निम्न JVM तर्क जोड़ें:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कॉन्फ़िगरेशन

एप्लिकेशन इस प्रकार कॉन्फ़िगर किया गया है:
- डिफ़ॉल्ट रूप से MiniMax-M3 का उपयोग करें; `MINIMAX_MODEL_ID` सेट करके `MiniMax-M3` या `MiniMax-M2.7` चुनें
- जब `OPENAI_BASE_URL` सेट हो तो उससे कनेक्ट करें; अन्यथा `MINIMAX_REGION=cn_zh` होने पर `https://api.minimaxi.com/v1`, या डिफ़ॉल्ट रूप से `https://api.minimax.io/v1` का उपयोग करें
- MCP सेवा से कनेक्ट करें `http://localhost:8080/sse`
- रिक्वेस्ट के लिए 60 सेकंड का टाइमआउट उपयोग करें

## निर्भरताएँ

इस प्रोजेक्ट में उपयोग की गई मुख्य निर्भरताएँ:
- **LangChain4j**: AI इंटीग्रेशन और टूल प्रबंधन के लिए
- **LangChain4j MCP**: मॉडल कॉन्टेक्स्ट प्रोटोकॉल सपोर्ट के लिए
- **LangChain4j OpenAI official**: MiniMax OpenAI- अनुकूल API इंटीग्रेशन के लिए
- **Spring Boot**: एप्लिकेशन फ्रेमवर्क और निर्भरता इंजेक्शन के लिए

## लाइसेंस

यह प्रोजेक्ट Apache License 2.0 के तहत लाइसेंस प्राप्त है - विवरण के लिए [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फ़ाइल देखें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->