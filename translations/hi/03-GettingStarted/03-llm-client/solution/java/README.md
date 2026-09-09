# कैलकुलेटर LLM क्लाइंट

एक जावा एप्लिकेशन जो दिखाता है कि LangChain4j का उपयोग करके MiniMax OpenAI-संगत API के माध्यम से MCP (मॉडल कॉन्टेक्स्ट प्रोटोकॉल) कैलकुलेटर सेवा से कैसे कनेक्ट किया जाए।

## पूर्वापेक्षाएँ

- जावा 21 या उससे ऊपर
- मेवन 3.6+ (या शामिल मेवन रैपर का उपयोग करें)
- एक MiniMax API कुंजी
- `http://localhost:8080` पर चल रही MCP कैलकुलेटर सेवा

## API कुंजी प्राप्त करना

यह एप्लिकेशन MiniMax OpenAI-संगत API का उपयोग करता है। अपनी कुंजी और एंडपॉइंट प्राप्त करने के लिए ये चरण अपनाएं:

### 1. एक एंडपॉइंट चुनें
1. वैश्विक एंडपॉइंट के लिए `https://api.minimax.io/v1` का उपयोग करें
2. चीन एंडपॉइंट के लिए `https://api.minimaxi.com/v1` का उपयोग करें

### 2. एक API कुंजी बनाएं
1. अपने MiniMax खाते से एक MiniMax API कुंजी बनाएं
2. कुंजी को कहीं सुरक्षित रखें

### 3. पर्यावरण चर सेट करें

#### विंडोज़ (कमांड प्रॉम्प्ट) पर:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### विंडोज़ (पावरशेल) पर:
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

## सेटअप और स्थापना

1. **प्रोजेक्ट डायरेक्टरी क्लोन करें या उसमें जाएं**

2. **निर्भरता स्थापित करें**:
   ```cmd
   mvnw clean install
   ```
   या अगर आपके पास मेवन ग्लोबली इंस्टॉल है:
   ```cmd
   mvn clean install
   ```

3. **पर्यावरण चर सेट करें** ("API कुंजी प्राप्त करना" अनुभाग देखें)

4. **MCP कैलकुलेटर सेवा शुरू करें**:
   सुनिश्चित करें कि आपने अध्याय 1 की MCP कैलकुलेटर सेवा `http://localhost:8080/sse` पर चला रखी है। क्लाइंट शुरू करने से पहले यह चल रही होनी चाहिए।

## एप्लिकेशन चलाना

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## एप्लिकेशन क्या करता है

एप्लिकेशन कैलकुलेटर सेवा के साथ तीन मुख्य इंटरएक्शन दिखाता है:

1. **जोड़**: 24.5 और 17.3 का योग निकालता है
2. **वर्गमूल**: 144 का वर्गमूल निकालता है
3. **मदद**: उपलब्ध कैलकुलेटर फ़ंक्शन दिखाता है

## अपेक्षित आउटपुट

सफलतापूर्वक चलाने पर, आपको लगभग ऐसा आउटपुट दिखाई देगा:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या निवारण

### सामान्य समस्याएं

1. **"OPENAI_API_KEY पर्यावरण चर सेट नहीं है"**
   - सुनिश्चित करें कि आपने `OPENAI_API_KEY` पर्यावरण चर सेट किया है
   - चर सेट करने के बाद टर्मिनल/कमांड प्रॉम्प्ट पुनः प्रारंभ करें

2. **"localhost:8080 से कनेक्शन अस्वीकृत"**
   - सुनिश्चित करें कि MCP कैलकुलेटर सेवा पोर्ट 8080 पर चल रही है
   - जांचें कि कोई अन्य सेवा पोर्ट 8080 का उपयोग तो नहीं कर रही

3. **"प्रमाणीकरण असफल"**
   - अपनी API कुंजी मान्य है यह जांचें
   - जांचें कि `OPENAI_BASE_URL` आपके इच्छित एंडपॉइंट से मेल खाता है

4. **मावेन बिल्ड त्रुटियाँ**
   - सुनिश्चित करें कि आप Java 21 या उससे ऊपर का उपयोग कर रहे हैं: `java -version`
   - बिल्ड साफ़ करने का प्रयास करें: `mvnw clean`

### डिबगिंग

डिबग लॉगिंग सक्षम करने के लिए, एप्लिकेशन चलाते समय निम्न JVM आर्गुमेंट जोड़ें:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कॉन्फ़िगरेशन

एप्लिकेशन को कॉन्फ़िगर किया गया है:
- डिफ़ॉल्ट रूप से MiniMax-M3 का उपयोग करें, या जब `MINIMAX_MODEL_ID` सेट हो तो MiniMax-M2.7
- `OPENAI_BASE_URL` से कनेक्ट करें जब यह सेट हो; नहीं तो `MINIMAX_REGION=cn_zh` होने पर `https://api.minimaxi.com/v1` या डिफ़ॉल्ट रूप से `https://api.minimax.io/v1`
- MCP सेवा से `http://localhost:8080/sse` पर कनेक्ट करें
- अनुरोधों के लिए 60 सेकंड का टाइमआउट उपयोग करें

## निर्भरताएँ

इस प्रोजेक्ट में उपयोग की गई मुख्य निर्भरताएँ:
- **LangChain4j**: एआई एकीकरण और टूल प्रबंधन के लिए
- **LangChain4j MCP**: मॉडल कॉन्टेक्स्ट प्रोटोकॉल सपोर्ट के लिए
- **LangChain4j OpenAI official**: MiniMax OpenAI-संगत API एकीकरण के लिए
- **Spring Boot**: एप्लिकेशन फ्रेमवर्क और निर्भरता इंजेक्शन के लिए

## लाइसेंस

यह प्रोजेक्ट Apache License 2.0 के तहत लाइसेंस प्राप्त है - विवरण के लिए [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फ़ाइल देखें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->