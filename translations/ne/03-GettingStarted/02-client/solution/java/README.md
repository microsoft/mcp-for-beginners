# MCP Java Client - क्याल्कुलेटर डेमो

यो प्रोजेक्टले कसरी Java क्लाइन्ट बनाउने र MCP (Model Context Protocol) सर्भरसँग जडान भएर अन्तरक्रिया गर्ने देखाउँछ। यस उदाहरणमा, हामी अध्याय ०१ को क्याल्कुलेटर सर्भरसँग जडान भएर विभिन्न गणितीय अपरेसनहरू गर्नेछौं।

## आवश्यकताहरू

यो क्लाइन्ट चलाउनु अघि, तपाईंले:

1. **अध्याय ०१ बाट क्याल्कुलेटर सर्भर सुरु गर्नुहोस्**:
   - क्याल्कुलेटर सर्भर डाइरेक्टरीमा जानुहोस्: `03-GettingStarted/01-first-server/solution/java/`
   - क्याल्कुलेटर सर्भर बनाउनुहोस् र चलाउनुहोस्:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - सर्भर `http://localhost:8080` मा चलिरहेको हुनुपर्छ

2. तपाईंको सिस्टममा **Java 21 वा माथि** इन्स्टल गरिएको हुनुपर्छ
3. **Maven** (Maven Wrapper मार्फत समावेश गरिएको)

## SDKClient के हो?

`SDKClient` एउटा Java एप्लिकेसन हो जसले देखाउँछ कि कसरी:
- Server-Sent Events (SSE) ट्रान्सपोर्ट प्रयोग गरेर MCP सर्भरसँग जडान गर्ने
- सर्भरबाट उपलब्ध उपकरणहरूको सूची प्राप्त गर्ने
- विभिन्न क्याल्कुलेटर फङ्सनहरू रिमोटली कल गर्ने
- प्रतिक्रिया सम्हाल्ने र नतिजा देखाउने

## यो कसरी काम गर्छ

क्लाइन्टले Spring AI MCP फ्रेमवर्क प्रयोग गरेर:

1. **जडान स्थापना गर्ने**: क्याल्कुलेटर सर्भरसँग जडान गर्न WebFlux SSE क्लाइन्ट ट्रान्सपोर्ट बनाउँछ
2. **क्लाइन्ट सुरु गर्ने**: MCP क्लाइन्ट सेटअप गरी जडान स्थापना गर्छ
3. **उपकरणहरू पत्ता लगाउने**: उपलब्ध सबै क्याल्कुलेटर अपरेसनहरूको सूची देखाउँछ
4. **अपरेसनहरू चलाउने**: नमूना डाटासँग विभिन्न गणितीय फङ्सनहरू कल गर्छ
5. **नतिजा देखाउने**: प्रत्येक गणनाको नतिजा देखाउँछ

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

## मुख्य निर्भरता

प्रोजेक्टले तलका मुख्य निर्भरता प्रयोग गर्छ:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

यस निर्भरता मार्फत उपलब्ध हुन्छ:
- `McpClient` - मुख्य क्लाइन्ट इन्टरफेस
- `WebFluxSseClientTransport` - वेब-आधारित सञ्चारका लागि SSE ट्रान्सपोर्ट
- MCP प्रोटोकल स्किमाहरू र अनुरोध/प्रतिक्रिया प्रकारहरू

## प्रोजेक्ट बनाउने तरिका

Maven wrapper प्रयोग गरेर प्रोजेक्ट बनाउनुहोस्:

```cmd
.\mvnw clean install
```

## क्लाइन्ट चलाउने तरिका

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**[!NOTE]**: यी कमाण्डहरू चलाउनु अघि क्याल्कुलेटर सर्भर `http://localhost:8080` मा चलिरहेको छ भनी सुनिश्चित गर्नुहोस्।

## क्लाइन्टले के गर्छ

क्लाइन्ट चलाउँदा यसले:

1. `http://localhost:8080` मा क्याल्कुलेटर सर्भरसँग **जडान** हुन्छ
2. **उपकरणहरूको सूची देखाउँछ** - उपलब्ध सबै क्याल्कुलेटर अपरेसनहरू देखाउँछ
3. **गणना गर्छ**:
   - जोड: 5 + 3 = 8
   - घटाउ: 10 - 4 = 6
   - गुणा: 6 × 7 = 42
   - भाग: 20 ÷ 4 = 5
   - घात: 2^8 = 256
   - वर्गमूल: √16 = 4
   - पूर्ण मान: |-5.5| = 5.5
   - सहायता: उपलब्ध अपरेसनहरू देखाउँछ

## अपेक्षित नतिजा

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

**[!NOTE]**: अन्त्यमा Maven ले केही थ्रेडहरू अझै चलिरहेको छ भनी चेतावनी दिन सक्छ - यो प्रतिक्रियाशील एप्लिकेसनहरूमा सामान्य हो र त्रुटि होइन।

## कोड बुझ्न

### १. ट्रान्सपोर्ट सेटअप
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
यसले क्याल्कुलेटर सर्भरसँग जडान गर्न SSE (Server-Sent Events) ट्रान्सपोर्ट बनाउँछ।

### २. क्लाइन्ट सिर्जना
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
सिंक्रोनस MCP क्लाइन्ट बनाउँछ र जडान सुरु गर्छ।

### ३. उपकरणहरू कल गर्ने
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
"add" उपकरणलाई a=5.0 र b=3.0 प्यारामिटरहरूसँग कल गर्छ।

## समस्या समाधान

### सर्भर चलिरहेको छैन
यदि जडान त्रुटि आयो भने, अध्याय ०१ को क्याल्कुलेटर सर्भर चलिरहेको छ कि छैन जाँच गर्नुहोस्:
```
Error: Connection refused
```
**समाधान**: पहिले क्याल्कुलेटर सर्भर सुरु गर्नुहोस्।

### पोर्ट पहिले नै प्रयोगमा छ
यदि पोर्ट 8080 प्रयोगमा छ भने:
```
Error: Address already in use
```
**समाधान**: पोर्ट 8080 प्रयोग गरिरहेका अन्य एप्लिकेसनहरू बन्द गर्नुहोस् वा सर्भरलाई फरक पोर्टमा चलाउनुहोस्।

### बिल्ड त्रुटि
यदि बिल्ड त्रुटि आयो भने:
```cmd
.\mvnw clean install -DskipTests
```

## थप जान्न

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।