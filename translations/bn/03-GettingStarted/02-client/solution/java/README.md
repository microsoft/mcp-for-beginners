# MCP Java Client - Calculator Demo

এই প্রজেক্টটি দেখায় কিভাবে একটি Java ক্লায়েন্ট তৈরি করা যায় যা MCP (Model Context Protocol) সার্ভারের সাথে সংযুক্ত হয় এবং ইন্টারঅ্যাক্ট করে। এই উদাহরণে, আমরা Chapter 01 থেকে calculator সার্ভারের সাথে সংযোগ করব এবং বিভিন্ন গাণিতিক অপারেশন সম্পাদন করব।

## প্রয়োজনীয়তা

এই ক্লায়েন্ট চালানোর আগে, আপনাকে:

1. **Chapter 01 থেকে Calculator Server চালু করুন**:
   - calculator সার্ভার ডিরেক্টরিতে যান: `03-GettingStarted/01-first-server/solution/java/`
   - calculator সার্ভার বিল্ড এবং রান করুন:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - সার্ভারটি `http://localhost:8080` এ চলমান থাকা উচিত

2. আপনার সিস্টেমে **Java 21 বা তার উপরে** ইনস্টল করা থাকতে হবে
3. **Maven** (Maven Wrapper এর মাধ্যমে অন্তর্ভুক্ত)

## SDKClient কী?

`SDKClient` একটি Java অ্যাপ্লিকেশন যা দেখায় কিভাবে:
- Server-Sent Events (SSE) ট্রান্সপোর্ট ব্যবহার করে MCP সার্ভারের সাথে সংযোগ স্থাপন করতে হয়
- সার্ভার থেকে উপলব্ধ টুলসের তালিকা পেতে হয়
- বিভিন্ন calculator ফাংশন রিমোটলি কল করতে হয়
- রেসপন্স হ্যান্ডেল করে ফলাফল প্রদর্শন করতে হয়

## এটি কিভাবে কাজ করে

ক্লায়েন্টটি Spring AI MCP ফ্রেমওয়ার্ক ব্যবহার করে:

1. **সংযোগ স্থাপন**: calculator সার্ভারের সাথে সংযোগ করার জন্য WebFlux SSE ক্লায়েন্ট ট্রান্সপোর্ট তৈরি করে
2. **ক্লায়েন্ট ইনিশিয়ালাইজেশন**: MCP ক্লায়েন্ট সেটআপ করে এবং সংযোগ স্থাপন করে
3. **টুলস আবিষ্কার**: উপলব্ধ সব calculator অপারেশন তালিকাভুক্ত করে
4. **অপারেশন সম্পাদন**: নমুনা ডেটা দিয়ে বিভিন্ন গাণিতিক ফাংশন কল করে
5. **ফলাফল প্রদর্শন**: প্রতিটি গণনার ফলাফল দেখায়

## প্রজেক্ট স্ট্রাকচার

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

## প্রধান ডিপেন্ডেন্সি

প্রজেক্টটি নিম্নলিখিত প্রধান ডিপেন্ডেন্সি ব্যবহার করে:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

এই ডিপেন্ডেন্সিগুলো প্রদান করে:
- `McpClient` - প্রধান ক্লায়েন্ট ইন্টারফেস
- `WebFluxSseClientTransport` - ওয়েব ভিত্তিক যোগাযোগের জন্য SSE ট্রান্সপোর্ট
- MCP প্রোটোকল স্কিমা এবং রিকোয়েস্ট/রেসপন্স টাইপস

## প্রজেক্ট বিল্ড করা

Maven wrapper ব্যবহার করে প্রজেক্ট বিল্ড করুন:

```cmd
.\mvnw clean install
```

## ক্লায়েন্ট চালানো

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: এই কমান্ডগুলো চালানোর আগে নিশ্চিত করুন calculator সার্ভার `http://localhost:8080` এ চলমান আছে।

## ক্লায়েন্ট কী করে

ক্লায়েন্ট চালানোর সময় এটি:

1. `http://localhost:8080` এ calculator সার্ভারের সাথে **সংযোগ স্থাপন** করে
2. **টুলস তালিকা** দেখায় - উপলব্ধ সব calculator অপারেশন
3. **গণনা সম্পাদন করে**:
   - যোগ: 5 + 3 = 8
   - বিয়োগ: 10 - 4 = 6
   - গুণ: 6 × 7 = 42
   - ভাগ: 20 ÷ 4 = 5
   - পাওয়ার: 2^8 = 256
   - বর্গমূল: √16 = 4
   - পরম মান: |-5.5| = 5.5
   - সাহায্য: উপলব্ধ অপারেশনগুলো দেখায়

## প্রত্যাশিত আউটপুট

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

**Note**: শেষের দিকে Maven থেকে থ্রেড সংক্রান্ত সতর্কতা দেখতে পারেন - এটি reactive অ্যাপ্লিকেশনগুলোর জন্য স্বাভাবিক এবং কোনো ত্রুটি নির্দেশ করে না।

## কোড বোঝা

### 1. ট্রান্সপোর্ট সেটআপ
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
এটি একটি SSE (Server-Sent Events) ট্রান্সপোর্ট তৈরি করে যা calculator সার্ভারের সাথে সংযোগ স্থাপন করে।

### 2. ক্লায়েন্ট তৈরি
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
একটি synchronous MCP ক্লায়েন্ট তৈরি করে এবং সংযোগ ইনিশিয়ালাইজ করে।

### 3. টুলস কল করা
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
"add" টুলটি প্যারামিটার a=5.0 এবং b=3.0 দিয়ে কল করে।

## সমস্যা সমাধান

### সার্ভার চালু নেই
যদি সংযোগ ত্রুটি পান, নিশ্চিত করুন Chapter 01 থেকে calculator সার্ভার চালু আছে:
```
Error: Connection refused
```
**সমাধান**: প্রথমে calculator সার্ভার চালু করুন।

### পোর্ট ইতিমধ্যে ব্যবহৃত হচ্ছে
যদি পোর্ট 8080 ব্যস্ত থাকে:
```
Error: Address already in use
```
**সমাধান**: পোর্ট 8080 ব্যবহার করছে এমন অন্য অ্যাপ্লিকেশন বন্ধ করুন অথবা সার্ভারকে অন্য পোর্টে চালু করুন।

### বিল্ড ত্রুটি
যদি বিল্ড ত্রুটি পান:
```cmd
.\mvnw clean install -DskipTests
```

## আরও জানুন

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।