# कॅल्क्युलेटर LLM क्लायंट

एक Java अनुप्रयोग जो LangChain4j वापरून MiniMax OpenAI-सुसंगत API द्वारे MCP (मॉडेल संदर्भ प्रोटोकॉल) कॅल्क्युलेटर सेवेशी कसे कनेक्ट करायचे हे दर्शवितो.

## पूर्वअट

- Java 21 किंवा त्याहून उच्च
- Maven 3.6+ (किंवा समाविष्ट Maven रॅपर वापरा)
- एक MiniMax API की
- `http://localhost:8080` वर चालणारी MCP कॅल्क्युलेटर सेवा

## API की मिळवणे

हा अनुप्रयोग MiniMax OpenAI-सुसंगत API वापरतो. तुमची की आणि एन्डपॉइंट मिळवण्यासाठी खालील पावले फॉलो करा:

### 1. एक एन्डपॉइंट निवडा
1. जागतिक एन्डपॉइंटसाठी `https://api.minimax.io/v1` वापरा
2. चीन एन्डपॉइंटसाठी `https://api.minimaxi.com/v1` वापरा

### 2. API की तयार करा
1. तुमच्या MiniMax खात्यातून MiniMax API की तयार करा
2. की कुठेतरी सुरक्षित ठिकाणी ठेवा

### 3. पर्यावरणीय चल सेट करा

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

1. **प्रकल्पाचे डिरेक्टरी क्लोन करा किंवा त्या ठिकाणी जा**

2. **आवश्यकता इन्स्टॉल करा**:
   ```cmd
   mvnw clean install
   ```
   किंवा जर तुमच्याकडे Maven जागतिकरित्या इन्स्टॉल असेल तर:
   ```cmd
   mvn clean install
   ```

3. **पर्यावरणीय चल सेट करा** ("API की मिळवणे" विभाग पहा)

4. **MCP कॅल्क्युलेटर सेवा सुरू करा**:
   chapter 1 ची MCP कॅल्क्युलेटर सेवा `http://localhost:8080/sse` वर चालू असल्याची खात्री करा. क्लायंट सुरू करण्यापूर्वी ही सेवा चालू असणे आवश्यक आहे.

## अनुप्रयोग चालवणे

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## अनुप्रयोग काय करतो

अनुप्रयोग कॅल्क्युलेटर सेवेशी तीन मुख्य संवाद दाखवतो:

1. **बेरीज**: 24.5 आणि 17.3 यांचा योग गणना करतो
2. **वर्गमूळ**: 144 चा वर्गमूळ गणना करतो
3. **मदत**: उपलब्ध कॅल्क्युलेटर फंक्शन्स दाखवतो

## अपेक्षित आउटपुट

यशस्वीपणे चालविल्यास, तुम्हाला खालील सारखे आउटपुट दिसेल:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्यांचे निराकरण

### सामान्य समस्या

1. **"OPENAI_API_KEY पर्यावरणीय चल सेट केलेले नाही"**
   - तुम्ही `OPENAI_API_KEY` पर्यावरणीय चल सेट केले आहे याची खात्री करा
   - चल सेट केल्यानंतर टर्मिनल/कमांड प्रॉम्प्ट पुनः सुरू करा

2. **"localhost:8080 शी कनेक्शन नाकारले"**
   - MCP कॅल्क्युलेटर सेवा पोर्ट 8080 वर चालू आहे याची खात्री करा
   - दुसरी कोणती सेवा पोर्ट 8080 वापरत आहे का हे तपासा

3. **"प्रमाणीकरण अयशस्वी"**
   - तुमची API की वैध आहे का तपासा
   - `OPENAI_BASE_URL` तुम्ही वापरू इच्छित असलेल्या एन्डपॉइंटशी जुळते का तपासा

4. **Maven बिल्ड त्रुटी**
   - तुम्ही Java 21 किंवा त्याहून वर वापरता आहे का याची खात्री करा: `java -version`
   - बिल्ड क्लीन करण्याचा प्रयत्न करा: `mvnw clean`

### डीबगिंग

डीबग लॉगिंग सक्षम करण्यासाठी, चालवताना खालील JVM आर्ग्युमेंट जोडा:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## संरचना

अनुप्रयोग खालील प्रमाणे संरचित आहे:
- डीफॉल्टने MiniMax-M3 वापरा, किंवा `MINIMAX_MODEL_ID` सेट असल्यास MiniMax-M2.7 वापरा
- `OPENAI_BASE_URL` सेट असल्यास तिथे कनेक्ट करा; अन्यथा `MINIMAX_REGION=cn_zh` असल्यास `https://api.minimaxi.com/v1`, नाहीतर डीफॉल्टने `https://api.minimax.io/v1` वापरा
- `http://localhost:8080/sse` वर MCP सेवेशी कनेक्ट करा
- विनंत्यांसाठी 60 सेकंदांची टाईमआउट वापरा

## अवलंबित्व

या प्रकल्पामध्ये वापरलेली मुख्य अवलंबित्वे:
- **LangChain4j**: AI एकत्रीकरण आणि साधन व्यवस्थापनासाठी
- **LangChain4j MCP**: मॉडेल संदर्भ प्रोटोकॉल समर्थनासाठी
- **LangChain4j OpenAI official**: MiniMax OpenAI-सुसंगत API एकत्रीकरणासाठी
- **Spring Boot**: अनुप्रयोग फ्रेमवर्क आणि अवलंबित्व इंजेक्शनसाठी

## परवाना

हा प्रकल्प Apache License 2.0 अंतर्गत परवानाधारित आहे - तपशीलांसाठी [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फाईल पहा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->