# कॅलक्युलेटर LLM क्लायंट

> [!NOTE]
> हा उपाय कोर्सच्या लेगसी HTTP+SSE कॅलक्युलेटर सेवेशी कनेक्ट होतो आणि
> MCP `2025-11-25` SDK API लक्ष्य करतो. हा `2026-07-28` स्ट्रीमॅबल HTTP चा
> उदाहरण नाही.

एक Java अॅप्लिकेशन जे LangChain4j वापरून MiniMax OpenAI-सुसंगत API द्वारे MCP (मॉडेल कंटेक्स्ट प्रोटोकॉल) कॅलक्युलेटर सेवेशी कनेक्ट होण्याचा दाखला देते.

## पूर्वअट

- Java 21 किंवा त्याहून वर
- Maven 3.6+ (किंवा समाविष्ट Maven रॅपर वापरा)
- एक MiniMax API की
- `http://localhost:8080` वर चालणारी MCP कॅलक्युलेटर सेवा

## API की मिळविणे

ह्या अॅप्लिकेशनमध्ये MiniMax OpenAI-सुसंगत API वापरले आहे. आपली की आणि एंडपॉइंट मिळविण्यासाठी खालील पद्धती फॉलो करा:

### 1. एक एंडपॉइंट निवडा
1. जागतिक एंडपॉइंटसाठी `https://api.minimax.io/v1` वापरा
2. चीन एंडपॉइंटसाठी `https://api.minimaxi.com/v1` वापरा

### 2. API की तयार करा
1. आपल्या MiniMax खात्यातून MiniMax API की तयार करा
2. की सुरक्षित ठिकाणी ठेवा

### 3. पर्यावरण चल (Environment Variables) सेट करा

#### Windows (Command Prompt) वर:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (PowerShell) वर:
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux वर:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## सेटअप आणि इंस्टॉलेशन

1. **प्रोजेक्ट डिरेक्टरी क्लोन करा किंवा त्यात जा**

2. **आवश्यकता इंस्टॉल करा**:
   ```cmd
   mvnw clean install
   ```
   किंवा आपण Maven जागतिक पातळीवर इंस्टॉल केले असल्यास:
   ```cmd
   mvn clean install
   ```

3. **पर्यावरण चल सेट करा** ("Getting the API Key" विभाग पहा)

4. **MCP कॅलक्युलेटर सेवा सुरू करा**:
   खात्री करा की आपल्याकडे चेप्टर 1 चे MCP कॅलक्युलेटर सेवा `http://localhost:8080/sse` वर चालू आहे. क्लायंट सुरू करण्यापूर्वी ही सेवा चालू असावी.

## अॅप्लिकेशन चालविणे

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## अॅप्लिकेशन काय करते

अॅप्लिकेशन कॅलक्युलेटर सेवेचे तीन मुख्य संवाद दाखवते:

1. **बेरीज**: 24.5 आणि 17.3 ची बेरीज काढते
2. **वर्गमूळ**: 144 चा वर्गमूळ काढते
3. **मदत**: उपलब्ध कॅलक्युलेटर फंक्शन्स दाखवते

## अपेक्षित आउटपुट

यशस्वीपणे चालवताना, आपल्याला खालीलप्रमाणे आउटपुट दिसेल:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या निवारण

### सामान्य समस्या

1. **"OPENAI_API_KEY पर्यावरण चल सेट केलेले नाही"**
   - खात्री करा की `OPENAI_API_KEY` पर्यावरण चल सेट केले आहे
   - चल सेट केल्यानंतर टर्मिनल/कमांड प्रॉम्प्ट पुन्हा सुरू करा

2. **"localhost:8080 कनेक्शन नाकारले"**
   - खात्री करा की MCP कॅलक्युलेटर सेवा पोर्ट 8080 वर चालू आहे
   - तपासा की दुसरी सेवा पोर्ट 8080 वापरत नाही आहे का

3. **"प्रमाणीकरण अयशस्वी"**
   - आपल्या API कीची वैधता पडताळा
   - तपासा की `OPENAI_BASE_URL` आपण वापरू इच्छित एंडपॉइंटशी जुळते

4. **Maven बिल्ड त्रुटी**
   - खात्री करा की आपण Java 21 किंवा त्याहून वर वापरत आहात: `java -version`
   - बिल्ड साफ करण्याचा प्रयत्न करा: `mvnw clean`

### डीबगिंग

डीबग लॉगिंग सक्षम करण्यासाठी, अॅप्लिकेशन चालवताना खालील JVM आर्ग्युमेंट जोडा:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कॉन्फिगरेशन

अॅप्लिकेशन खालीलप्रमाणे कॉन्फिगर केले आहे:
- डिफॉल्टने MiniMax-M3 वापरले जाते; `MINIMAX_MODEL_ID` सेट करून `MiniMax-M3` किंवा `MiniMax-M2.7` निवडा
- `OPENAI_BASE_URL` सेट असेल तर त्याला कनेक्ट होते; अन्यथा, `MINIMAX_REGION=cn_zh` असल्यास `https://api.minimaxi.com/v1` वापरा, आणि वरवर `https://api.minimax.io/v1` वापरले जाते
- `http://localhost:8080/sse` वर MCP सेवा कनेक्ट करा
- विनंत्यांसाठी 60 सेकंद टाइमआउट वापरा

## अवलंबन

या प्रोजेक्टमध्ये वापरलीली मुख्य अवलंबने:
- **LangChain4j**: AI एकत्रीकरण आणि टूल व्यवस्थापनासाठी
- **LangChain4j MCP**: मॉडेल कंटेक्स्ट प्रोटोकॉल सपोर्टसाठी
- **LangChain4j OpenAI official**: MiniMax OpenAI-सुसंगत API एकत्रीकरणासाठी
- **Spring Boot**: अॅप्लिकेशन फ्रेमवर्क आणि अवलंबन इंजेक्शनसाठी

## परवाना

हा प्रोजेक्ट Apache License 2.0 अंतर्गत परवानाधीन आहे - तपशीलांसाठी [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फाइल पाहा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->