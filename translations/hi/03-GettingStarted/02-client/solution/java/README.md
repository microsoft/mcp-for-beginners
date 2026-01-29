# MCP Java Client - Calculator Demo

यह प्रोजेक्ट दिखाता है कि कैसे एक Java क्लाइंट बनाया जाए जो MCP (Model Context Protocol) सर्वर से कनेक्ट होकर इंटरैक्ट करता है। इस उदाहरण में, हम चैप्टर 01 के कैलकुलेटर सर्वर से कनेक्ट करेंगे और विभिन्न गणितीय ऑपरेशन्स करेंगे।

## आवश्यकताएँ

इस क्लाइंट को चलाने से पहले, आपको निम्न करना होगा:

1. **चैप्टर 01 से Calculator Server शुरू करें**:
   - कैलकुलेटर सर्वर डायरेक्टरी पर जाएं: `03-GettingStarted/01-first-server/solution/java/`
   - कैलकुलेटर सर्वर को बिल्ड और रन करें:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - सर्वर `http://localhost:8080` पर चल रहा होना चाहिए

2. आपके सिस्टम में **Java 21 या उससे ऊपर** इंस्टॉल होना चाहिए
3. **Maven** (Maven Wrapper के माध्यम से शामिल)

## SDKClient क्या है?

`SDKClient` एक Java एप्लिकेशन है जो दिखाता है कि कैसे:
- Server-Sent Events (SSE) ट्रांसपोर्ट का उपयोग करके MCP सर्वर से कनेक्ट करें
- सर्वर से उपलब्ध टूल्स की सूची प्राप्त करें
- विभिन्न कैलकुलेटर फंक्शन्स को रिमोटली कॉल करें
- रिस्पॉन्स को हैंडल करें और परिणाम दिखाएं

## यह कैसे काम करता है

क्लाइंट Spring AI MCP फ्रेमवर्क का उपयोग करता है ताकि:

1. **कनेक्शन स्थापित करें**: कैलकुलेटर सर्वर से कनेक्ट करने के लिए WebFlux SSE क्लाइंट ट्रांसपोर्ट बनाता है
2. **क्लाइंट इनिशियलाइज़ करें**: MCP क्लाइंट सेटअप करता है और कनेक्शन स्थापित करता है
3. **टूल्स खोजें**: सभी उपलब्ध कैलकुलेटर ऑपरेशन्स की सूची दिखाता है
4. **ऑपरेशन्स चलाएं**: नमूना डेटा के साथ विभिन्न गणितीय फंक्शन्स कॉल करता है
5. **परिणाम दिखाएं**: हर कैलकुलेशन के परिणाम प्रदर्शित करता है

## प्रोजेक्ट संरचना

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

## मुख्य निर्भरताएँ

प्रोजेक्ट निम्न मुख्य निर्भरताओं का उपयोग करता है:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

यह निर्भरता प्रदान करती है:
- `McpClient` - मुख्य क्लाइंट इंटरफेस
- `WebFluxSseClientTransport` - वेब आधारित संचार के लिए SSE ट्रांसपोर्ट
- MCP प्रोटोकॉल स्कीमास और रिक्वेस्ट/रिस्पॉन्स टाइप्स

## प्रोजेक्ट बिल्ड करना

Maven wrapper का उपयोग करके प्रोजेक्ट बिल्ड करें:

```cmd
.\mvnw clean install
```

## क्लाइंट चलाना

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: कोई भी कमांड चलाने से पहले सुनिश्चित करें कि कैलकुलेटर सर्वर `http://localhost:8080` पर चल रहा हो।

## क्लाइंट क्या करता है

जब आप क्लाइंट चलाते हैं, तो यह:

1. `http://localhost:8080` पर कैलकुलेटर सर्वर से **कनेक्ट** होता है
2. **टूल्स की सूची दिखाता है** - सभी उपलब्ध कैलकुलेटर ऑपरेशन्स दिखाता है
3. **गणनाएँ करता है**:
   - जोड़: 5 + 3 = 8
   - घटाव: 10 - 4 = 6
   - गुणा: 6 × 7 = 42
   - भाग: 20 ÷ 4 = 5
   - घातांक: 2^8 = 256
   - वर्गमूल: √16 = 4
   - परिमाण (Absolute Value): |-5.5| = 5.5
   - सहायता: उपलब्ध ऑपरेशन्स दिखाता है

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

**Note**: अंत में Maven से कुछ चेतावनियाँ आ सकती हैं जैसे कि थ्रेड्स अभी भी चल रहे हैं - यह रिएक्टिव एप्लिकेशन्स के लिए सामान्य है और कोई त्रुटि नहीं है।

## कोड को समझना

### 1. ट्रांसपोर्ट सेटअप
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
यह एक SSE (Server-Sent Events) ट्रांसपोर्ट बनाता है जो कैलकुलेटर सर्वर से कनेक्ट होता है।

### 2. क्लाइंट बनाना
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
एक सिंक्रोनस MCP क्लाइंट बनाता है और कनेक्शन इनिशियलाइज़ करता है।

### 3. टूल्स कॉल करना
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
"add" टूल को पैरामीटर a=5.0 और b=3.0 के साथ कॉल करता है।

## समस्या निवारण

### सर्वर नहीं चल रहा
अगर कनेक्शन एरर आ रहे हैं, तो सुनिश्चित करें कि चैप्टर 01 का कैलकुलेटर सर्वर चल रहा हो:
```
Error: Connection refused
```
**समाधान**: पहले कैलकुलेटर सर्वर शुरू करें।

### पोर्ट पहले से उपयोग में है
अगर पोर्ट 8080 व्यस्त है:
```
Error: Address already in use
```
**समाधान**: पोर्ट 8080 का उपयोग कर रहे अन्य एप्लिकेशन्स को बंद करें या सर्वर को किसी अन्य पोर्ट पर चलाएं।

### बिल्ड एरर
अगर बिल्ड में त्रुटि आ रही है:
```cmd
.\mvnw clean install -DskipTests
```

## और जानें

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।