# Calculator LLM Client

एक Java एप्लिकेशन जो दिखाता है कि LangChain4j का उपयोग करके MCP (Model Context Protocol) कैलकुलेटर सेवा से GitHub Models इंटीग्रेशन के साथ कैसे कनेक्ट किया जाए।

## आवश्यकताएँ

- Java 21 या उससे ऊपर
- Maven 3.6+ (या शामिल Maven wrapper का उपयोग करें)
- GitHub Models तक पहुंच वाला GitHub खाता
- `http://localhost:8080` पर चल रही MCP कैलकुलेटर सेवा

## GitHub टोकन प्राप्त करना

यह एप्लिकेशन GitHub Models का उपयोग करता है जिसके लिए GitHub पर्सनल एक्सेस टोकन की आवश्यकता होती है। अपना टोकन पाने के लिए निम्न चरणों का पालन करें:

### 1. GitHub Models तक पहुंचें
1. [GitHub Models](https://github.com/marketplace/models) पर जाएं
2. अपने GitHub खाते से साइन इन करें
3. यदि आपने पहले से एक्सेस नहीं लिया है तो GitHub Models के लिए एक्सेस का अनुरोध करें

### 2. पर्सनल एक्सेस टोकन बनाएं
1. [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens) पर जाएं
2. "Generate new token" → "Generate new token (classic)" पर क्लिक करें
3. अपने टोकन को एक वर्णनात्मक नाम दें (जैसे, "MCP Calculator Client")
4. आवश्यकतानुसार एक्सपायरी सेट करें
5. निम्न स्कोप चुनें:
   - `repo` (यदि प्राइवेट रिपॉजिटरीज़ तक पहुंचना है)
   - `user:email`
6. "Generate token" पर क्लिक करें
7. **महत्वपूर्ण**: टोकन को तुरंत कॉपी कर लें - आप इसे बाद में नहीं देख पाएंगे!

### 3. पर्यावरण चर सेट करें

#### Windows (Command Prompt) पर:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) पर:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux पर:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## सेटअप और इंस्टॉलेशन

1. **प्रोजेक्ट डायरेक्टरी क्लोन करें या उसमें जाएं**

2. **डिपेंडेंसीज़ इंस्टॉल करें**:
   ```cmd
   mvnw clean install
   ```
   या यदि आपके पास Maven ग्लोबली इंस्टॉल है:
   ```cmd
   mvn clean install
   ```

3. **पर्यावरण चर सेट करें** (ऊपर "Getting the GitHub Token" सेक्शन देखें)

4. **MCP Calculator Service शुरू करें**:
   सुनिश्चित करें कि आपने चैप्टर 1 की MCP कैलकुलेटर सेवा `http://localhost:8080/sse` पर चल रही हो। क्लाइंट शुरू करने से पहले यह सेवा चल रही होनी चाहिए।

## एप्लिकेशन चलाना

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## एप्लिकेशन क्या करता है

यह एप्लिकेशन कैलकुलेटर सेवा के साथ तीन मुख्य इंटरैक्शन दिखाता है:

1. **जोड़**: 24.5 और 17.3 का योग निकालता है
2. **वर्गमूल**: 144 का वर्गमूल निकालता है
3. **मदद**: उपलब्ध कैलकुलेटर फ़ंक्शंस दिखाता है

## अपेक्षित आउटपुट

सफलतापूर्वक चलने पर, आपको निम्न जैसा आउटपुट दिखेगा:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या निवारण

### सामान्य समस्याएँ

1. **"GITHUB_TOKEN environment variable not set"**
   - सुनिश्चित करें कि आपने `GITHUB_TOKEN` पर्यावरण चर सेट किया है
   - सेट करने के बाद टर्मिनल/कमांड प्रॉम्प्ट को पुनः शुरू करें

2. **"Connection refused to localhost:8080"**
   - जांचें कि MCP कैलकुलेटर सेवा पोर्ट 8080 पर चल रही है
   - देखें कि कोई अन्य सेवा पोर्ट 8080 का उपयोग तो नहीं कर रही

3. **"Authentication failed"**
   - अपने GitHub टोकन की वैधता और सही अनुमतियाँ जांचें
   - सुनिश्चित करें कि आपके पास GitHub Models तक पहुंच है

4. **Maven बिल्ड त्रुटियाँ**
   - जांचें कि आप Java 21 या उससे ऊपर का उपयोग कर रहे हैं: `java -version`
   - बिल्ड साफ़ करने की कोशिश करें: `mvnw clean`

### डिबगिंग

डिबग लॉगिंग सक्षम करने के लिए, रन करते समय निम्न JVM आर्गुमेंट जोड़ें:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कॉन्फ़िगरेशन

एप्लिकेशन इस प्रकार कॉन्फ़िगर है:
- GitHub Models का उपयोग `gpt-4.1-nano` मॉडल के साथ
- MCP सेवा से कनेक्ट `http://localhost:8080/sse` पर
- अनुरोधों के लिए 60 सेकंड का टाइमआउट
- डिबगिंग के लिए अनुरोध/प्रतिक्रिया लॉगिंग सक्षम

## डिपेंडेंसीज़

इस प्रोजेक्ट में उपयोग की गई मुख्य डिपेंडेंसीज़:
- **LangChain4j**: AI इंटीग्रेशन और टूल प्रबंधन के लिए
- **LangChain4j MCP**: Model Context Protocol सपोर्ट के लिए
- **LangChain4j GitHub Models**: GitHub Models इंटीग्रेशन के लिए
- **Spring Boot**: एप्लिकेशन फ्रेमवर्क और डिपेंडेंसी इंजेक्शन के लिए

## लाइसेंस

यह प्रोजेक्ट Apache License 2.0 के तहत लाइसेंस प्राप्त है - विवरण के लिए [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फ़ाइल देखें।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।