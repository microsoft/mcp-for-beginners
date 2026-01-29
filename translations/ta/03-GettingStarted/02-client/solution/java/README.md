# MCP ஜாவா கிளையன்ட் - கணக்கீடு டெமோ

இந்த திட்டம் MCP (மாடல் கான்டெக்ஸ்ட் புரோட்டோகால்) சர்வருடன் இணைந்து செயல்படும் ஜாவா கிளையன்டை உருவாக்குவது எப்படி என்பதை விளக்குகிறது. இந்த எடுத்துக்காட்டில், Chapter 01-இல் உள்ள கணக்கீடு சர்வருடன் இணைந்து பல கணித செயல்பாடுகளைச் செய்வோம்.

## முன் தேவைகள்

இந்த கிளையன்டை இயக்குவதற்கு முன், நீங்கள் பின்வரும் பணிகளைச் செய்ய வேண்டும்:

1. **Chapter 01-இல் உள்ள கணக்கீடு சர்வரை தொடங்கவும்**:
   - கணக்கீடு சர்வர் கோப்பகத்துக்கு செல்லவும்: `03-GettingStarted/01-first-server/solution/java/`
   - கணக்கீடு சர்வரை கட்டமைத்து இயக்கவும்:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - சர்வர் `http://localhost:8080`-ல் இயங்கிக் கொண்டிருக்க வேண்டும்

2. உங்கள் கணினியில் **Java 21 அல்லது அதற்கு மேல்** நிறுவப்பட்டிருக்க வேண்டும்  
3. **Maven** (Maven Wrapper மூலம் சேர்க்கப்பட்டுள்ளது)

## SDKClient என்றால் என்ன?

`SDKClient` என்பது ஒரு ஜாவா பயன்பாடாகும், இது பின்வருவனவற்றை விளக்குகிறது:
- Server-Sent Events (SSE) போக்குவரத்தைப் பயன்படுத்தி MCP சர்வருடன் இணைதல்
- சர்வரில் கிடைக்கும் கருவிகளை பட்டியலிடுதல்
- பல்வேறு கணக்கீடு செயல்பாடுகளை தொலைநிலையிலிருந்து அழைத்தல்
- பதில்களை கையாளுதல் மற்றும் முடிவுகளை காட்சிப்படுத்துதல்

## இது எப்படி செயல்படுகிறது

Spring AI MCP கட்டமைப்பைப் பயன்படுத்தி கிளையன்ட் பின்வருவனவற்றைச் செய்கிறது:

1. **இணைப்பை ஏற்படுத்துதல்**: கணக்கீடு சர்வருடன் இணைவதற்காக WebFlux SSE கிளையன்ட் போக்குவரத்தை உருவாக்குகிறது  
2. **கிளையன்டை தொடங்குதல்**: MCP கிளையன்டை அமைத்து இணைப்பை ஏற்படுத்துகிறது  
3. **கருவிகளை கண்டறிதல்**: கணக்கீடு செயல்பாடுகளை பட்டியலிடுகிறது  
4. **செயல்பாடுகளை இயக்குதல்**: மாதிரித் தரவுகளுடன் பல கணித செயல்பாடுகளை அழைக்கிறது  
5. **முடிவுகளை காட்சிப்படுத்துதல்**: ஒவ்வொரு கணக்கீட்டின் முடிவுகளையும் காட்சிப்படுத்துகிறது  

## திட்ட அமைப்பு

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

## முக்கிய சார்புகள்

இந்த திட்டம் பின்வரும் முக்கிய சார்புகளைப் பயன்படுத்துகிறது:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

இந்த சார்பு வழங்குகிறது:
- `McpClient` - முக்கிய கிளையன்ட் இடைமுகம்
- `WebFluxSseClientTransport` - வலை அடிப்படையிலான தொடர்புக்கு SSE போக்குவரத்து
- MCP புரோட்டோகால் ஸ்கீமாக்கள் மற்றும் கோரிக்கை/பதில் வகைகள்

## திட்டத்தை கட்டமைத்தல்

Maven Wrapper-ஐப் பயன்படுத்தி திட்டத்தை கட்டமைக்கவும்:

```cmd
.\mvnw clean install
```

## கிளையன்டை இயக்குதல்

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**குறிப்பு**: எந்தக் கட்டளையையும் இயக்குவதற்கு முன், கணக்கீடு சர்வர் `http://localhost:8080`-ல் இயங்கிக் கொண்டிருக்க வேண்டும் என்பதை உறுதிப்படுத்தவும்.

## கிளையன்ட் என்ன செய்கிறது

கிளையன்டை இயக்கும் போது, இது பின்வருவனவற்றைச் செய்கிறது:

1. **இணைதல்**: `http://localhost:8080`-ல் உள்ள கணக்கீடு சர்வருடன் இணைகிறது  
2. **கருவிகளை பட்டியலிடுதல்**: கணக்கீடு செயல்பாடுகளை காட்சிப்படுத்துகிறது  
3. **கணக்கீடுகளைச் செய்யுதல்**:
   - கூட்டல்: 5 + 3 = 8  
   - கழித்தல்: 10 - 4 = 6  
   - பெருக்கல்: 6 × 7 = 42  
   - வகுத்தல்: 20 ÷ 4 = 5  
   - சக்தி: 2^8 = 256  
   - சதுரவேர்: √16 = 4  
   - முழுமையான மதிப்பு: |-5.5| = 5.5  
   - உதவி: கிடைக்கும் செயல்பாடுகளை காட்சிப்படுத்துகிறது  

## எதிர்பார்க்கப்படும் வெளியீடு

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

**குறிப்பு**: செயலின் முடிவில் Maven தொடர்பான எச்சரிக்கைகள் (warnings) தோன்றலாம் - இது எதிர்பார்க்கப்பட்டதுதான், இது பிழையை குறிக்காது.

## குறியீட்டை புரிந்துகொள்வது

### 1. போக்குவரத்து அமைப்பு
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
இது கணக்கீடு சர்வருடன் இணைவதற்கான SSE (Server-Sent Events) போக்குவரத்தை உருவாக்குகிறது.

### 2. கிளையன்ட் உருவாக்கம்
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
இது ஒத்திசைவான MCP கிளையன்டை உருவாக்கி இணைப்பை தொடங்குகிறது.

### 3. கருவிகளை அழைத்தல்
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
இது "add" கருவியை a=5.0 மற்றும் b=3.0 என்ற அளவுருக்களுடன் அழைக்கிறது.

## சிக்கல்களை சரிசெய்தல்

### சர்வர் இயங்கவில்லை
இணைப்பு பிழைகள் ஏற்பட்டால், Chapter 01-இல் உள்ள கணக்கீடு சர்வர் இயங்குகிறதா என்பதை உறுதிப்படுத்தவும்:
```
Error: Connection refused
```
**தீர்வு**: முதலில் கணக்கீடு சர்வரை தொடங்கவும்.

### போர்ட் ஏற்கனவே பயன்படுத்தப்படுகிறது
போர்ட் 8080 பிஸியாக இருந்தால்:
```
Error: Address already in use
```
**தீர்வு**: போர்ட் 8080-ஐ பயன்படுத்தும் பிற பயன்பாடுகளை நிறுத்தவும் அல்லது சர்வரை வேறு போர்ட்டில் இயக்கவும்.

### கட்டமைப்பு பிழைகள்
கட்டமைப்பு பிழைகள் ஏற்பட்டால்:
```cmd
.\mvnw clean install -DskipTests
```

## மேலும் அறிக

- [Spring AI MCP ஆவணங்கள்](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [மாடல் கான்டெக்ஸ்ட் புரோட்டோகால் விவரக்குறிப்பு](https://modelcontextprotocol.io/)
- [Spring WebFlux ஆவணங்கள்](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.