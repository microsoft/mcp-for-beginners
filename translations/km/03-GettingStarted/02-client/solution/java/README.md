# MCP Java Client - ទិដ្ឋភាពប្រើប្រាស់ Calculator

គម្រោងនេះបង្ហាញពីរបៀបបង្កើត client Java ដែលភ្ជាប់ទៅនឹង និងធ្វើអន្តរកម្មជាមួយម៉ាស៊ីនមេ MCP (Model Context Protocol) ។ ក្នុងឧទាហរណ៍នេះ យើងនឹងភ្ជាប់ទៅម៉ាស៊ីនមេ calculator នៃជំពូក 01 ហើយអនុវត្តិប្រតិបត្តិការគណិតវិទ្យាផ្សេងៗ។

## សេចក្តីមុនចាំបាច់

មុនដំណើរការមាន client នេះ អ្នកត្រូវតែ៖

1. **ចាប់ផ្ដើមម៉ាស៊ីនមេ Calculator** ពីជំពូក 01៖
   - ទៅកាន់ថតម៉ាស៊ីនមេ calculator៖ `03-GettingStarted/01-first-server/solution/java/`
   - បង្កើត និងរត់ម៉ាស៊ីនមេ calculator៖
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - ម៉ាស៊ីនមេស្អាតជារដ្ឋត្រូវរត់នៅលើ `http://localhost:8080`

2. **Java 21 ឬខ្ពស់ជាងទៀត** ត្រូវបានដំឡើងលើប្រព័ន្ធរបស់អ្នក
3. **Maven** (បានដាក់បញ្ចូលតាមរយៈ Maven Wrapper)

## SDKClient ជាអ្វី?

`SDKClient` គឺជាកម្មវិធី Java ដែលបង្ហាញពីរបៀប៖
- ភ្ជាប់ទៅម៉ាស៊ីនមេ MCP ប្រើ Server-Sent Events (SSE) សម្រាប់ការដំណើរការ
- បញ្ជីឧបករណ៍ដែលមាននៅលើម៉ាស៊ីនមេ
- ហៅមុខងារ calculator ផ្សេងៗពីចម្ងាយ
- ដោះស្រាយចម្លើយ និងបង្ហាញលទ្ធផល

## វាដំណើរការយ៉ាងដូចម្តេច

client នេះប្រើ Spring AI MCP framework ដើម្បី៖

1. **បង្កើតការភ្ជាប់**៖ បង្កើតតំណភ្ជាប់ SSE client ដើម្បីភ្ជាប់ទៅម៉ាស៊ីនមេ calculator
2. **ផ្តើម client**៖ កំណត់ client MCP ហើយបង្កើតការភ្ជាប់
3. **ស្វែងរកឧបករណ៍**៖ បញ្ជីបញ្ចូលគ្រប់មុខងារគណនីដែលមាន
4. **អនុវត្តការប្រតិបត្តិការ**៖ ហៅមុខងារគណិតវិទ្យាជាមួយទិន្នន័យគំរូ
5. **បង្ហាញលទ្ធផល**៖ បង្ហាញលទ្ធផលនៃការគណនា

## រចនាសម្ព័ន្ធគម្រោង

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

## ឧបករណ៍ផ្គត់ផ្គង់សំខាន់ៗ

គម្រោងបានប្រើឧបករណ៍ផ្គត់ផ្គង់សំខាន់ៗដូចតទៅ៖

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

ឧបករណ៍នេះផ្ដល់៖
- `McpClient` - ចំណុចចូល client សំខាន់
- `WebFluxSseClientTransport` - ការដឹកជញ្ជូន SSE សម្រាប់ទំនាក់ទំនងតាមវ៉េប
- គំរូ protocol MCP និងប្រភេទសំណើ/ចម្លើយ

## របៀបសង់គម្រោង

សង់គម្រោងដោយប្រើ Maven wrapper៖

```cmd
.\mvnw clean install
```

## របៀបរត់ client

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**កំណត់សម្គាល់**៖ ត្រូវប្រាកដថាម៉ាស៊ីនមេ calculator កំពុងរត់នៅលើ `http://localhost:8080` មុនពេលអនុវត្តពាក្យបញ្ជាទាំងនេះ។

## client ធ្វើអ្វី

ពេលអ្នករត់ client នេះ វានឹង៖

1. **ភ្ជាប់** ទៅម៉ាស៊ីនមេ calculator នៅ `http://localhost:8080`
2. **បញ្ជីឧបករណ៍** - បង្ហាញគ្រប់មុខងារគណនីដែលមាន
3. **អនុវត្តការគណនា**៖
   - បូក: 5 + 3 = 8
   - ដក: 10 - 4 = 6
   - គុណ: 6 × 7 = 42
   - ចែក: 20 ÷ 4 = 5
   - លំនាយ: 2^8 = 256
   - ប្រព្រឹត្តមូល: √16 = 4
   - តម្លៃអប្បបរមា: |-5.5| = 5.5
   - ជំនួយ: បង្ហាញមុខងារដែលមាន

## លទ្ធផលដែលរំពឹងទុក

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

**កំណត់សម្គាល់**៖ អ្នកអាចឃើញការជូនដំណឹង Maven អំពី thread ដែលនៅសល់នៅចុងក្រោយ - នេះជារឿងធម្មតាសម្រាប់កម្មវិធី reactive ហើយមិនមែនបញ្ហាខុស។

## ការយល់ដឹងពីកូដ

### 1. ការកំណត់រចនាសម្ព័ន្ធដឹកជញ្ជូន
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
 បង្កើតតំណភ្ជាប់ SSE (Server-Sent Events) ដែលភ្ជាប់ទៅម៉ាស៊ីនមេ calculator។

### 2. ការបង្កើត client
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
បង្កើត client MCP ប្រកបដោយសម្រួល synchronous ហើយចាប់ផ្ដើមការភ្ជាប់។

### 3. ការហៅឧបករណ៍
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
ហៅឧបករណ៍ "add" ជាមួយប៉ារ៉ាម៉ែត្រ a=5.0 និង b=3.0។

## ជំនួយបញ្ហា

### ម៉ាស៊ីនមេមិនរត់
បើអ្នកបានឃើញកំហុសភ្ជាប់ សូមប្រាកដថា ម៉ាស៊ីនមេ calculator ពីជំពូក 01 កំពុងរត់៖
```
Error: Connection refused
```
**ដំណោះស្រាយ**៖ ចាប់ផ្ដើមម៉ាស៊ីនមេ calculator ជាមុន។

### បំពង់តំណរត្រូវបានប្រើរួចហើយ
បើ port 8080 ត្រូវបានប្រើប្រាស់រួចហើយ៖
```
Error: Address already in use
```
**ដំណោះស្រាយ**៖ បិទកម្មវិធីផ្សេងទៀតដែលកំពុងប្រើ port 8080 ឬកែប្រែម៉ាស៊ីនមេឲ្យប្រើ port ផ្សេង។

### កំហុសក្នុងការសង់
បើអ្នកជួបកំហុសក្នុងការសង់៖
```cmd
.\mvnw clean install -DskipTests
```

## ស្វែងយល់បន្ថែម

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិក្នុងខ្លឹមសារអាចមានកំហុស ឬការផ្ទុះផ្សេងៗ។ ឯកសារដើមនៅក្នុងភាសាទាំងដើមគួរត្រូវបានយកថាជាធនធានដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សជំនាញគឺត្រូវបានផ្ដល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំន ឬការប្រែបកផ្សេងៗដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->