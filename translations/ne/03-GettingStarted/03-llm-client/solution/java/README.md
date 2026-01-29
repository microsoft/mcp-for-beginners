# Calculator LLM Client

LangChain4j प्रयोग गरेर MCP (Model Context Protocol) क्याल्कुलेटर सेवा GitHub Models इंटिग्रेशनसँग कसरी जडान गर्ने देखाउने एउटा Java एप्लिकेशन।

## आवश्यकताहरू

- Java 21 वा माथि
- Maven 3.6+ (वा समावेश गरिएको Maven wrapper प्रयोग गर्नुहोस्)
- GitHub Models पहुँच भएको GitHub खाता
- `http://localhost:8080` मा चलिरहेको MCP क्याल्कुलेटर सेवा

## GitHub टोकन प्राप्त गर्ने तरिका

यो एप्लिकेशन GitHub Models प्रयोग गर्छ जसका लागि GitHub व्यक्तिगत पहुँच टोकन आवश्यक हुन्छ। आफ्नो टोकन प्राप्त गर्न यी चरणहरू पालना गर्नुहोस्:

### 1. GitHub Models पहुँच गर्नुहोस्
1. [GitHub Models](https://github.com/marketplace/models) मा जानुहोस्
2. आफ्नो GitHub खाताबाट साइन इन गर्नुहोस्
3. यदि पहिले नगरेको भए GitHub Models पहुँचको लागि अनुरोध गर्नुहोस्

### 2. व्यक्तिगत पहुँच टोकन सिर्जना गर्नुहोस्
1. [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens) मा जानुहोस्
2. "Generate new token" → "Generate new token (classic)" क्लिक गर्नुहोस्
3. आफ्नो टोकनलाई अर्थपूर्ण नाम दिनुहोस् (जस्तै, "MCP Calculator Client")
4. आवश्यक अनुसार समाप्ति मिति सेट गर्नुहोस्
5. तलका स्कोपहरू चयन गर्नुहोस्:
   - `repo` (यदि निजी रिपोजिटोरीहरू पहुँच गर्नुपर्ने हो भने)
   - `user:email`
6. "Generate token" क्लिक गर्नुहोस्
7. **महत्वपूर्ण**: टोकन तुरुन्तै कपी गर्नुहोस् - यो फेरि देख्न सकिँदैन!

### 3. वातावरण चर सेट गर्नुहोस्

#### Windows (Command Prompt) मा:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) मा:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux मा:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## सेटअप र स्थापना

1. **प्रोजेक्ट डाइरेक्टरी क्लोन वा त्यहाँ जानुहोस्**

2. **निर्भरता स्थापना गर्नुहोस्**:
   ```cmd
   mvnw clean install
   ```
   वा यदि Maven ग्लोबली इन्स्टल छ भने:
   ```cmd
   mvn clean install
   ```

3. **वातावरण चर सेट गर्नुहोस्** ("Getting the GitHub Token" सेक्सन हेर्नुहोस्)

4. **MCP क्याल्कुलेटर सेवा सुरु गर्नुहोस्**:
   सुनिश्चित गर्नुहोस् कि अध्याय 1 को MCP क्याल्कुलेटर सेवा `http://localhost:8080/sse` मा चलिरहेको छ। क्लाइन्ट सुरु गर्नु अघि यो चलिरहेको हुनुपर्छ।

## एप्लिकेशन चलाउने तरिका

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## एप्लिकेशनले के गर्छ

एप्लिकेशनले क्याल्कुलेटर सेवासँग तीन मुख्य अन्तरक्रियाहरू देखाउँछ:

1. **जोड**: 24.5 र 17.3 को योग गणना गर्छ
2. **वर्गमूल**: 144 को वर्गमूल गणना गर्छ
3. **मद्दत**: उपलब्ध क्याल्कुलेटर फंक्शनहरू देखाउँछ

## अपेक्षित नतिजा

सफलतापूर्वक चलाउँदा, तपाईंले यस्तै नतिजा देख्नुहुनेछ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## समस्या समाधान

### सामान्य समस्या

1. **"GITHUB_TOKEN environment variable not set"**
   - `GITHUB_TOKEN` वातावरण चर सेट गरेको सुनिश्चित गर्नुहोस्
   - चर सेट गरेपछि टर्मिनल/कमाण्ड प्रम्प्ट पुनः सुरु गर्नुहोस्

2. **"Connection refused to localhost:8080"**
   - MCP क्याल्कुलेटर सेवा पोर्ट 8080 मा चलिरहेको छ कि छैन जाँच गर्नुहोस्
   - अर्को सेवा पोर्ट 8080 प्रयोग गरिरहेको छ कि छैन जाँच गर्नुहोस्

3. **"Authentication failed"**
   - आफ्नो GitHub टोकन मान्य छ र सही अनुमति छ कि छैन जाँच गर्नुहोस्
   - GitHub Models पहुँच छ कि छैन जाँच गर्नुहोस्

4. **Maven बिल्ड त्रुटिहरू**
   - Java 21 वा माथि प्रयोग गरिरहेको छ कि छैन जाँच गर्नुहोस्: `java -version`
   - बिल्ड सफा गर्ने प्रयास गर्नुहोस्: `mvnw clean`

### डिबगिङ

डिबग लगिङ सक्षम गर्न, एप्लिकेशन चलाउँदा तलको JVM आर्गुमेन्ट थप्नुहोस्:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## कन्फिगरेसन

एप्लिकेशन यसरी कन्फिगर गरिएको छ:
- GitHub Models `gpt-4.1-nano` मोडेलसँग प्रयोग गर्ने
- MCP सेवा `http://localhost:8080/sse` मा जडान गर्ने
- अनुरोधहरूको लागि 60 सेकेन्ड टाइमआउट सेट गर्ने
- डिबगिङका लागि अनुरोध/प्रतिक्रिया लगिङ सक्षम गर्ने

## निर्भरता

यस प्रोजेक्टमा प्रयोग भएका मुख्य निर्भरता:
- **LangChain4j**: AI इंटिग्रेशन र टुल व्यवस्थापनका लागि
- **LangChain4j MCP**: Model Context Protocol समर्थनका लागि
- **LangChain4j GitHub Models**: GitHub Models इंटिग्रेशनका लागि
- **Spring Boot**: एप्लिकेशन फ्रेमवर्क र निर्भरता इन्जेक्शनका लागि

## लाइसेन्स

यो प्रोजेक्ट Apache License 2.0 अन्तर्गत लाइसेन्स गरिएको छ - विवरणका लागि [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) फाइल हेर्नुहोस्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।