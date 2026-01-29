# Calculator LLM Client

हा एक Java अॅप्लिकेशन आहे जो LangChain4j वापरून MCP (Model Context Protocol) कॅल्क्युलेटर सेवा GitHub Models इंटिग्रेशनसह कशी कनेक्ट करायची हे दाखवतो.

## आवश्यक अटी

- Java 21 किंवा त्याहून अधिक
- Maven 3.6+ (किंवा समाविष्ट Maven wrapper वापरा)
- GitHub Models साठी प्रवेश असलेले GitHub खाते
- `http://localhost:8080` वर चालणारी MCP कॅल्क्युलेटर सेवा

## GitHub टोकन मिळविणे

हे अॅप्लिकेशन GitHub Models वापरते ज्यासाठी GitHub वैयक्तिक प्रवेश टोकन आवश्यक आहे. तुमचा टोकन मिळविण्यासाठी खालील पायऱ्या फॉलो करा:

### 1. GitHub Models मध्ये प्रवेश करा
1. [GitHub Models](https://github.com/marketplace/models) येथे जा
2. तुमच्या GitHub खात्याने साइन इन करा
3. जर आधी प्रवेश नसेल तर GitHub Models साठी प्रवेश मागवा

### 2. वैयक्तिक प्रवेश टोकन तयार करा
1. [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens) येथे जा
2. "Generate new token" → "Generate new token (classic)" क्लिक करा
3. तुमच्या टोकनला अर्थपूर्ण नाव द्या (उदा. "MCP Calculator Client")
4. आवश्यकतेनुसार कालबाह्यता सेट करा
5. खालील स्कोप निवडा:
   - `repo` (जर खाजगी रिपॉझिटरीजमध्ये प्रवेश हवा असेल तर)
   - `user:email`
6. "Generate token" क्लिक करा
7. **महत्त्वाचे**: टोकन लगेच कॉपी करा - नंतर ते पुन्हा पाहता येणार नाही!

### 3. पर्यावरण चल सेट करा

#### Windows (Command Prompt) वर:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) वर:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux वर:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## सेटअप आणि इन्स्टॉलेशन

1. **प्रोजेक्ट डायरेक्टरी क्लोन करा किंवा त्यात जा**

2. **आवश्यकता इन्स्टॉल करा**:
   ```cmd
   mvnw clean install
   ```
   किंवा जर Maven ग्लोबली इन्स्टॉल असेल तर:
   ```cmd
   mvn clean install
   ```

3. **पर्यावरण चल सेट करा** (वरील "GitHub टोकन मिळविणे" विभाग पहा)

4. **MCP Calculator सेवा सुरू करा**:
   chapter 1 मधील MCP कॅल्क्युलेटर सेवा `http://localhost:8080/sse` वर चालू असावी. क्लायंट सुरू करण्यापूर्वी ही सेवा चालू असणे आवश्यक आहे.

## अॅप्लिकेशन चालविणे

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## अॅप्लिकेशन काय करते

हे अॅप्लिकेशन कॅल्क्युलेटर सेवेशी तीन मुख्य संवाद दाखवते:

1. **बेरीज**: 24.5 आणि 17.3 यांची बेरीज काढते
2. **वर्गमूळ**: 144 चा वर्गमूळ काढते
3. **मदत**: उपलब्ध कॅल्क्युलेटर फंक्शन्स दाखवते

## अपेक्षित आउटपुट

यशस्वीपणे चालवल्यास, तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या निवारण

### सामान्य समस्या

1. **"GITHUB_TOKEN environment variable not set"**
   - `GITHUB_TOKEN` पर्यावरण चल सेट केले आहे याची खात्री करा
   - चल सेट केल्यानंतर टर्मिनल/कमांड प्रॉम्प्ट पुन्हा सुरू करा

2. **"Connection refused to localhost:8080"**
   - MCP कॅल्क्युलेटर सेवा पोर्ट 8080 वर चालू आहे का ते तपासा
   - पोर्ट 8080 दुसरी सेवा वापरत नाही याची खात्री करा

3. **"Authentication failed"**
   - तुमचा GitHub टोकन वैध आहे आणि योग्य परवानग्या आहेत का ते तपासा
   - GitHub Models साठी तुमच्याकडे प्रवेश आहे का ते पहा

4. **Maven बिल्ड त्रुटी**
   - Java 21 किंवा त्याहून अधिक वापरत आहात का ते तपासा: `java -version`
   - बिल्ड क्लीन करण्याचा प्रयत्न करा: `mvnw clean`

### डीबगिंग

डीबग लॉगिंग सक्षम करण्यासाठी, अॅप्लिकेशन चालवताना खालील JVM आर्ग्युमेंट जोडा:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कॉन्फिगरेशन

अॅप्लिकेशन खालीलप्रमाणे कॉन्फिगर केले आहे:
- GitHub Models `gpt-4.1-nano` मॉडेल वापरणे
- MCP सेवा `http://localhost:8080/sse` वर कनेक्ट करणे
- विनंत्यांसाठी 60 सेकंदांचा टाइमआउट वापरणे
- डीबगिंगसाठी विनंती/प्रतिसाद लॉगिंग सक्षम करणे

## अवलंबित्वे

या प्रोजेक्टमध्ये वापरलेली मुख्य अवलंबित्वे:
- **LangChain4j**: AI इंटिग्रेशन आणि टूल मॅनेजमेंटसाठी
- **LangChain4j MCP**: Model Context Protocol साठी समर्थन
- **LangChain4j GitHub Models**: GitHub Models इंटिग्रेशनसाठी
- **Spring Boot**: अॅप्लिकेशन फ्रेमवर्क आणि अवलंबित्व इंजेक्शनसाठी

## परवाना

हा प्रोजेक्ट Apache License 2.0 अंतर्गत परवानाधारक आहे - तपशीलांसाठी [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फाइल पहा.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.