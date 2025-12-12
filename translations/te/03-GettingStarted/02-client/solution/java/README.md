<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7074b9f4c8cd147c1c10f569d8508c82",
  "translation_date": "2025-12-11T13:35:41+00:00",
  "source_file": "03-GettingStarted/02-client/solution/java/README.md",
  "language_code": "te"
}
-->
# MCP జావా క్లయింట్ - క్యాల్క్యులేటర్ డెమో

ఈ ప్రాజెక్ట్ MCP (మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్) సర్వర్‌కు కనెక్ట్ అయ్యి ఇంటరాక్ట్ అయ్యే జావా క్లయింట్‌ను ఎలా సృష్టించాలో చూపిస్తుంది. ఈ ఉదాహరణలో, మనం చాప్టర్ 01 నుండి క్యాల్క్యులేటర్ సర్వర్‌కు కనెక్ట్ అయి వివిధ గణిత చర్యలను నిర్వహిస్తాము.

## ముందస్తు అవసరాలు

ఈ క్లయింట్‌ను నడపడానికి ముందు, మీరు:

1. **చాప్టర్ 01 నుండి క్యాల్క్యులేటర్ సర్వర్‌ను ప్రారంభించండి**:
   - క్యాల్క్యులేటర్ సర్వర్ డైరెక్టరీకి వెళ్లండి: `03-GettingStarted/01-first-server/solution/java/`
   - క్యాల్క్యులేటర్ సర్వర్‌ను బిల్డ్ చేసి నడపండి:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - సర్వర్ `http://localhost:8080` పై నడుస్తుండాలి

2. మీ సిస్టమ్‌లో **జావా 21 లేదా అంతకంటే పైగా** ఇన్‌స్టాల్ చేయబడాలి
3. **మావెన్** (మావెన్ రాపర్ ద్వారా చేర్చబడింది)

## SDKClient అంటే ఏమిటి?

`SDKClient` అనేది ఒక జావా అప్లికేషన్, ఇది ఎలా చేయాలో చూపిస్తుంది:
- Server-Sent Events (SSE) ట్రాన్స్‌పోర్ట్ ఉపయోగించి MCP సర్వర్‌కు కనెక్ట్ అవ్వడం
- సర్వర్ నుండి అందుబాటులో ఉన్న టూల్స్ జాబితా చేయడం
- వివిధ క్యాల్క్యులేటర్ ఫంక్షన్లను రిమోట్‌గా కాల్ చేయడం
- ప్రతిస్పందనలను హ్యాండిల్ చేసి ఫలితాలను ప్రదర్శించడం

## ఇది ఎలా పనిచేస్తుంది

క్లయింట్ Spring AI MCP ఫ్రేమ్‌వర్క్‌ను ఉపయోగించి:

1. **కనెక్షన్ స్థాపన**: క్యాల్క్యులేటర్ సర్వర్‌కు కనెక్ట్ కావడానికి WebFlux SSE క్లయింట్ ట్రాన్స్‌పోర్ట్ సృష్టిస్తుంది
2. **క్లయింట్ ప్రారంభం**: MCP క్లయింట్‌ను సెట్ చేసి కనెక్షన్‌ను స్థాపిస్తుంది
3. **టూల్స్ కనుగొనడం**: అందుబాటులో ఉన్న అన్ని క్యాల్క్యులేటర్ ఆపరేషన్ల జాబితా
4. **ఆపరేషన్లు నిర్వహించడం**: నమూనా డేటాతో వివిధ గణిత ఫంక్షన్లను కాల్ చేయడం
5. **ఫలితాలు ప్రదర్శించడం**: ప్రతి గణన ఫలితాలను చూపించడం

## ప్రాజెక్ట్ నిర్మాణం

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

## ముఖ్యమైన డిపెండెన్సీలు

ప్రాజెక్ట్ క్రింది ముఖ్యమైన డిపెండెన్సీలను ఉపయోగిస్తుంది:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

ఈ డిపెండెన్సీ అందిస్తుంది:
- `McpClient` - ప్రధాన క్లయింట్ ఇంటర్‌ఫేస్
- `WebFluxSseClientTransport` - వెబ్ ఆధారిత కమ్యూనికేషన్ కోసం SSE ట్రాన్స్‌పోర్ట్
- MCP ప్రోటోకాల్ స్కీమాలు మరియు రిక్వెస్ట్/రెస్పాన్స్ రకాల

## ప్రాజెక్ట్ బిల్డ్ చేయడం

మావెన్ రాపర్ ఉపయోగించి ప్రాజెక్ట్‌ను బిల్డ్ చేయండి:

```cmd
.\mvnw clean install
```

## క్లయింట్ నడపడం

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**గమనిక**: ఈ ఆదేశాలను అమలు చేయడానికి ముందు క్యాల్క్యులేటర్ సర్వర్ `http://localhost:8080` పై నడుస్తున్నదని నిర్ధారించుకోండి.

## క్లయింట్ ఏమి చేస్తుంది

మీరు క్లయింట్‌ను నడిపినప్పుడు, ఇది:

1. `http://localhost:8080` వద్ద క్యాల్క్యులేటర్ సర్వర్‌కు **కనెక్ట్** అవుతుంది
2. **టూల్స్ జాబితా** - అందుబాటులో ఉన్న అన్ని క్యాల్క్యులేటర్ ఆపరేషన్లను చూపిస్తుంది
3. **గణనలను నిర్వహిస్తుంది**:
   - జోడింపు: 5 + 3 = 8
   - తీసివేత: 10 - 4 = 6
   - గుణకం: 6 × 7 = 42
   - భాగాకారం: 20 ÷ 4 = 5
   - శక్తి: 2^8 = 256
   - వర్గమూలం: √16 = 4
   - పరమాణు విలువ: |-5.5| = 5.5
   - సహాయం: అందుబాటులో ఉన్న ఆపరేషన్లను చూపిస్తుంది

## ఆశించిన అవుట్‌పుట్

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

**గమనిక**: చివరలో మావెన్ లింకింగ్ థ్రెడ్స్ గురించి హెచ్చరికలు కనిపించవచ్చు - ఇది రియాక్టివ్ అప్లికేషన్లకు సాధారణం మరియు ఇది లోపం కాదు.

## కోడ్‌ను అర్థం చేసుకోవడం

### 1. ట్రాన్స్‌పోర్ట్ సెటప్
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
ఇది క్యాల్క్యులేటర్ సర్వర్‌కు కనెక్ట్ అయ్యే SSE (సర్వర్-సెంట్ ఈవెంట్స్) ట్రాన్స్‌పోర్ట్‌ను సృష్టిస్తుంది.

### 2. క్లయింట్ సృష్టి
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
సింక్రోనస్ MCP క్లయింట్‌ను సృష్టించి కనెక్షన్‌ను ప్రారంభిస్తుంది.

### 3. టూల్స్ కాల్ చేయడం
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
పారామీటర్లు a=5.0 మరియు b=3.0 తో "add" టూల్‌ను కాల్ చేస్తుంది.

## సమస్యలు పరిష్కరించడం

### సర్వర్ నడవడం లేదు
కనెక్షన్ లోపాలు వస్తే, చాప్టర్ 01 నుండి క్యాల్క్యులేటర్ సర్వర్ నడుస్తున్నదని నిర్ధారించుకోండి:
```
Error: Connection refused
```
**పరిష్కారం**: ముందుగా క్యాల్క్యులేటర్ సర్వర్‌ను ప్రారంభించండి.

### పోర్ట్ ఇప్పటికే ఉపయోగంలో ఉంది
పోర్ట్ 8080 బిజీగా ఉంటే:
```
Error: Address already in use
```
**పరిష్కారం**: పోర్ట్ 8080 ఉపయోగిస్తున్న ఇతర అప్లికేషన్లను ఆపండి లేదా సర్వర్‌ను వేరే పోర్ట్ ఉపయోగించ도록 మార్చండి.

### బిల్డ్ లోపాలు
బిల్డ్ లోపాలు ఎదురైతే:
```cmd
.\mvnw clean install -DskipTests
```

## మరింత తెలుసుకోండి

- [Spring AI MCP డాక్యుమెంటేషన్](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ స్పెసిఫికేషన్](https://modelcontextprotocol.io/)
- [Spring WebFlux డాక్యుమెంటేషన్](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->