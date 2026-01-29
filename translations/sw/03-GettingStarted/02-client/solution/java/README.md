# MCP Java Client - Demo ya Calculator

Mradi huu unaonyesha jinsi ya kuunda mteja wa Java unaounganisha na kuingiliana na seva ya MCP (Model Context Protocol). Katika mfano huu, tutajiunga na seva ya calculator kutoka Sura ya 01 na kufanya shughuli mbalimbali za hisabati.

## Mahitaji ya Awali

Kabla ya kuendesha mteja huyu, unahitaji:

1. **Anzisha Seva ya Calculator** kutoka Sura ya 01:
   - Nenda kwenye saraka ya seva ya calculator: `03-GettingStarted/01-first-server/solution/java/`
   - Jenga na endesha seva ya calculator:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Seva inapaswa kuwa inafanya kazi kwenye `http://localhost:8080`

2. **Java 21 au zaidi** imewekwa kwenye mfumo wako  
3. **Maven** (imejumuishwa kupitia Maven Wrapper)

## SDKClient ni Nini?

`SDKClient` ni programu ya Java inayonyesha jinsi ya:
- Kuungana na seva ya MCP kwa kutumia usafirishaji wa Server-Sent Events (SSE)  
- Orodhesha zana zinazopatikana kutoka seva  
- Piga simu kwa kazi mbalimbali za calculator kwa mbali  
- Shughulikia majibu na kuonyesha matokeo  

## Inavyofanya Kazi

Mteja hutumia mfumo wa Spring AI MCP ili:

1. **Kuweka Muunganisho**: Unda usafirishaji wa WebFlux SSE kuungana na seva ya calculator  
2. **Anzisha Mteja**: Weka mteja wa MCP na anza muunganisho  
3. **Gundua Zana**: Orodhesha shughuli zote zinazopatikana za calculator  
4. **Fanya Shughuli**: Piga simu kwa kazi mbalimbali za hisabati kwa data za mfano  
5. **Onyesha Matokeo**: Onyesha matokeo ya kila hesabu  

## Muundo wa Mradi

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

## Mategemeo Muhimu

Mradi hutumia mategemeo yafuatayo muhimu:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Mategemeo haya yanatoa:  
- `McpClient` - Kiolesura kikuu cha mteja  
- `WebFluxSseClientTransport` - Usafirishaji wa SSE kwa mawasiliano ya mtandao  
- Mipangilio ya itifaki ya MCP na aina za maombi/jawabu  

## Kujenga Mradi

Jenga mradi kwa kutumia Maven wrapper:

```cmd
.\mvnw clean install
```

## Kuendesha Mteja

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: Hakikisha seva ya calculator inafanya kazi kwenye `http://localhost:8080` kabla ya kutekeleza amri yoyote.

## Mteja Hufanya Nini

Unapoendesha mteja, utakuwa:

1. **Unganisha** na seva ya calculator kwenye `http://localhost:8080`  
2. **Orodhesha Zana** - Onyesha shughuli zote zinazopatikana za calculator  
3. **Fanya Hesabu**:  
   - Jumlisha: 5 + 3 = 8  
   - Toa: 10 - 4 = 6  
   - Zidisha: 6 × 7 = 42  
   - Gawanya: 20 ÷ 4 = 5  
   - Nguvu: 2^8 = 256  
   - Mizizi ya Mraba: √16 = 4  
   - Thamani Kamili: |-5.5| = 5.5  
   - Msaada: Onyesha shughuli zinazopatikana  

## Matokeo Yanayotarajiwa

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

**Note**: Unaweza kuona onyo la Maven kuhusu thread zinazobaki mwishoni - hii ni kawaida kwa programu za reactive na haimaanishi kosa.

## Kuelewa Msimbo

### 1. Kuanzisha Usafirishaji  
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```  
Hii huunda usafirishaji wa SSE (Server-Sent Events) unaounganisha na seva ya calculator.

### 2. Kuunda Mteja  
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```  
Huunda mteja wa MCP wa synchronous na kuanzisha muunganisho.

### 3. Kupiga Simu Zana  
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```  
Inapiga simu kwa zana ya "add" kwa vigezo a=5.0 na b=3.0.

## Kutatua Matatizo

### Seva Haifanyi Kazi  
Kama unapata makosa ya muunganisho, hakikisha seva ya calculator kutoka Sura ya 01 inafanya kazi:  
```
Error: Connection refused
```  
**Solution**: Anzisha seva ya calculator kwanza.

### Bandari Tayari Inatumika  
Kama bandari 8080 inatumika:  
```
Error: Address already in use
```  
**Solution**: Zima programu nyingine zinazotumia bandari 8080 au badilisha seva kutumia bandari tofauti.

### Makosa ya Kujenga  
Kama unakutana na makosa ya kujenga:  
```cmd
.\mvnw clean install -DskipTests
```

## Jifunze Zaidi

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)  
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)  
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.