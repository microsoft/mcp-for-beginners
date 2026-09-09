# कॅल्क्युलेटर LLM क्लायंट

LangChain4j वापरून MiniMax OpenAI-सुसंगत API द्वारे MCP (मॉडेल कॉन्टेक्स्ट प्रोटोकॉल) कॅल्क्युलेटर सेवा जोडण्याची एक Java अनुप्रयोग दर्शवणारी उदाहरणे.

## आवश्यक पूर्वअट्स

- Java 21 किंवा त्याहून अधिक
- Maven 3.6+ (किंवा समाविष्ट Maven रॅपर वापरा)
- एक MiniMax API की
- `http://localhost:8080` वर चालणारी MCP कॅल्क्युलेटर सेवा

## API की मिळविणे

या अनुप्रयोगासाठी MiniMax OpenAI-सुसंगत API वापरला जातो. आपली की आणि एंडपॉइंट मिळवण्यासाठी खालील चरणांचे पालन करा:

### 1. एक एंडपॉइंट निवडा
1. जागतिक एंडपॉइंटसाठी `https://api.minimax.io/v1` वापरा
2. चीन एंडपॉइंटसाठी `https://api.minimaxi.com/v1` वापरा

### 2. API की तयार करा
1. आपल्या MiniMax खात्यातून MiniMax API की तयार करा
2. ही की सुरक्षित ठिकाणी ठेवा

### 3. पर्यावरण चर सेट करा

#### Windows (कमांड प्रॉम्प्ट) वर:
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

## सेटअप आणि स्थापना

1. **प्रोजेक्ट डायरेक्टरी क्लोन करा किंवा त्यावर जा**

2. **आश्रितता स्थापित करा**:
   ```cmd
   mvnw clean install
   ```
   किंवा आपल्याकडे Maven जागतिकरित्या स्थापित असल्यास:
   ```cmd
   mvn clean install
   ```

3. **पर्यावरण चर सेट करा** (वरील "API की मिळविणे" विभाग पहा)

4. **MCP कॅल्क्युलेटर सेवा सुरू करा**:
   chapter 1 मध्ये दिलेल्या MCP कॅल्क्युलेटर सेवा `http://localhost:8080/sse` वर चालू असल्याची खात्री करा. क्लायंट सुरू करण्यापूर्वी ही सेवा चालू असावी.

## अनुप्रयोग चालविणे

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## अनुप्रयोग काय करतो

अनुप्रयोग कॅल्क्युलेटर सेवेशी तीन प्रमुख संवाद दाखवतो:

1. **बेरीज**: 24.5 आणि 17.3 ची बेरीज गणना करते
2. **वर्गमूल**: 144 चा वर्गमूल गणना करते
3. **मदत**: उपलब्ध कॅल्क्युलेटर फंक्शन्स दाखवते

## अपेक्षित आउटपुट

यशस्वीपणे चालविल्यास, आपल्याला खालीलप्रमाणे आउटपुट पाहायला मिळेल:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या निराकरण

### सामान्य समस्या

1. **"OPENAI_API_KEY पर्यावरण चर सेट केले नाही"**
   - सुनिश्चित करा की आपण `OPENAI_API_KEY` पर्यावरण चर सेट केले आहे
   - वैशिष्ट्ये सेट केल्यानंतर आपला टर्मिनल/कमांड प्रॉम्प्ट पुन्हा सुरू करा

2. **"localhost:8080 शी कनेक्शन नाकारले"**
   - खात्री करा की MCP कॅल्क्युलेटर सेवा पोर्ट 8080 वर चालू आहे
   - तपासा की दुसरी सेवा पोर्ट 8080 वापरत नाहीये का

3. **"प्रमाणीकरण अयशस्वी"**
   - आपली API की वैध आहे का ते तपासा
   - `OPENAI_BASE_URL` आपल्या इच्छित एंडपॉइंटशी जुळते का ते तपासा

4. **Maven बिल्ड त्रुटी**
   - सुनिश्चित करा की आपण Java 21 किंवा त्याहून अधिक वापरत आहात: `java -version`
   - बिल्ड क्लीन करा: `mvnw clean`

### डिबगिंग

डिबग लॉगिंग सक्षम करण्यासाठी, चालवताना खालील JVM आर्ग्युमेंट जोडा:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कॉन्फिगरेशन

अनुप्रयोग असे कॉन्फिगर केलेले आहे:
- डीफॉल्टने MiniMax-M3 वापरते; `MINIMAX_MODEL_ID` सेट करून `MiniMax-M3` किंवा `MiniMax-M2.7` निवडा
- `OPENAI_BASE_URL` सेट केल्यावर तो वापरतो; अन्यथा `MINIMAX_REGION=cn_zh` असल्यास `https://api.minimaxi.com/v1` वापरतो, नाहीतर डीफॉल्टने `https://api.minimax.io/v1`
- MCP सेवा `http://localhost:8080/sse` शी कनेक्ट होतो
- विनंत्यांसाठी 60 सेकंदांची टाइमआऊट वापरतो

## आश्रितता

या प्रोजेक्टमध्ये वापरलेली मुख्य आश्रितता:
- **LangChain4j**: AI एकत्रीकरण आणि टूल व्यवस्थापनासाठी
- **LangChain4j MCP**: मॉडेल कॉन्टेक्स्ट प्रोटोकॉल समर्थनासाठी
- **LangChain4j OpenAI अधिकृत**: MiniMax OpenAI-सुसंगत API एकत्रीकरणासाठी
- **Spring Boot**: अनुप्रयोग फ्रेमवर्क आणि आश्रितता इंजेक्शनसाठी

## परवाना

हा प्रोजेक्ट Apache License 2.0 अंतर्गत परवाना प्राप्त आहे - तपशीलांसाठी [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फाइल पहा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->