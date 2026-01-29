# MCP Java Client - Calculator Demo

हा प्रकल्प Java क्लायंट कसा तयार करायचा आणि MCP (Model Context Protocol) सर्व्हरशी कसा कनेक्ट होऊन संवाद साधायचा हे दाखवतो. या उदाहरणात, आपण Chapter 01 मधील कॅल्क्युलेटर सर्व्हरशी कनेक्ट होऊन विविध गणिती क्रिया पार पाडणार आहोत.

## आवश्यक पूर्वतयारी

हा क्लायंट चालवण्यापूर्वी, तुम्हाला खालील गोष्टी कराव्या लागतील:

1. **Chapter 01 मधील Calculator Server सुरू करा**:
   - कॅल्क्युलेटर सर्व्हर डिरेक्टरीमध्ये जा: `03-GettingStarted/01-first-server/solution/java/`
   - कॅल्क्युलेटर सर्व्हर बिल्ड आणि रन करा:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - सर्व्हर `http://localhost:8080` वर चालू असावा

2. तुमच्या सिस्टीमवर **Java 21 किंवा त्याहून वरची आवृत्ती** इन्स्टॉल असावी
3. **Maven** (Maven Wrapper द्वारे समाविष्ट)

## SDKClient म्हणजे काय?

`SDKClient` हा एक Java अ‍ॅप्लिकेशन आहे जो दाखवतो की:
- Server-Sent Events (SSE) ट्रान्सपोर्ट वापरून MCP सर्व्हरशी कसे कनेक्ट करायचे
- सर्व्हरवर उपलब्ध टूल्सची यादी कशी मिळवायची
- विविध कॅल्क्युलेटर फंक्शन्स रिमोटली कसे कॉल करायचे
- प्रतिसाद कसे हाताळायचे आणि निकाल कसे दाखवायचे

## हे कसे कार्य करते

हा क्लायंट Spring AI MCP फ्रेमवर्क वापरतो जेणेकरून:

1. **कनेक्शन स्थापन करणे**: कॅल्क्युलेटर सर्व्हरशी कनेक्ट होण्यासाठी WebFlux SSE क्लायंट ट्रान्सपोर्ट तयार करतो
2. **क्लायंट इनिशियलाइझ करणे**: MCP क्लायंट सेटअप करतो आणि कनेक्शन स्थापन करतो
3. **टूल्स शोधणे**: उपलब्ध सर्व कॅल्क्युलेटर ऑपरेशन्सची यादी करतो
4. **ऑपरेशन्स पार पाडणे**: नमुना डेटा वापरून विविध गणिती फंक्शन्स कॉल करतो
5. **निकाल दाखवणे**: प्रत्येक गणनेचा निकाल दाखवतो

## प्रकल्प रचना

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## मुख्य अवलंबित्वे

हा प्रकल्प खालील मुख्य अवलंबित्वे वापरतो:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

हे अवलंबित्व प्रदान करते:
- `McpClient` - मुख्य क्लायंट इंटरफेस
- `WebFluxSseClientTransport` - वेब-आधारित संवादासाठी SSE ट्रान्सपोर्ट
- MCP प्रोटोकॉल स्कीमा आणि विनंती/प्रतिसाद प्रकार

## प्रकल्प बिल्ड करणे

Maven wrapper वापरून प्रकल्प बिल्ड करा:

```cmd
.\mvnw clean install
```

## क्लायंट चालवणे

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**[!NOTE]**: कोणतेही कमांड चालवण्यापूर्वी कॅल्क्युलेटर सर्व्हर `http://localhost:8080` वर चालू असल्याची खात्री करा.

## क्लायंट काय करतो

क्लायंट चालविल्यावर, तो:

1. `http://localhost:8080` वर कॅल्क्युलेटर सर्व्हरशी **कनेक्ट** होतो
2. **टूल्सची यादी** दाखवतो - उपलब्ध सर्व कॅल्क्युलेटर ऑपरेशन्स
3. **गणना करतो**:
   - बेरीज: 5 + 3 = 8
   - वजाबाकी: 10 - 4 = 6
   - गुणाकार: 6 × 7 = 42
   - भागाकार: 20 ÷ 4 = 5
   - घातांक: 2^8 = 256
   - वर्गमूळ: √16 = 4
   - परिमाण (Absolute Value): |-5.5| = 5.5
   - मदत: उपलब्ध ऑपरेशन्स दाखवते

## अपेक्षित आउटपुट

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**[!NOTE]**: शेवटी Maven कडून काही थ्रेड्स उरल्याबाबत चेतावणी दिसू शकते - हे reactive applications मध्ये सामान्य आहे आणि त्रुटीचे संकेत नाही.

## कोड समजून घेणे

### 1. ट्रान्सपोर्ट सेटअप
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
हे SSE (Server-Sent Events) ट्रान्सपोर्ट तयार करते जे कॅल्क्युलेटर सर्व्हरशी कनेक्ट होते.

### 2. क्लायंट तयार करणे
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
सिंक्रोनस MCP क्लायंट तयार करतो आणि कनेक्शन इनिशियलाइझ करतो.

### 3. टूल्स कॉल करणे
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
"add" टूलला a=5.0 आणि b=3.0 या पॅरामीटर्ससह कॉल करतो.

## समस्या निवारण

### सर्व्हर चालू नाही
जर कनेक्शन त्रुटी आल्या तर, Chapter 01 मधील कॅल्क्युलेटर सर्व्हर चालू आहे का ते तपासा:
```
Error: Connection refused
```
**उपाय**: प्रथम कॅल्क्युलेटर सर्व्हर सुरू करा.

### पोर्ट आधीच वापरात आहे
जर पोर्ट 8080 वापरात असेल:
```
Error: Address already in use
```
**उपाय**: पोर्ट 8080 वापरणाऱ्या इतर अ‍ॅप्लिकेशन्स थांबवा किंवा सर्व्हर वेगळा पोर्ट वापरण्यासाठी बदला.

### बिल्ड त्रुटी
जर बिल्ड करताना त्रुटी आल्या:
```cmd
.\mvnw clean install -DskipTests
```

## अधिक जाणून घ्या

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.