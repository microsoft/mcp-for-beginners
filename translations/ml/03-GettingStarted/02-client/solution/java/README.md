<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7074b9f4c8cd147c1c10f569d8508c82",
  "translation_date": "2025-12-11T13:36:29+00:00",
  "source_file": "03-GettingStarted/02-client/solution/java/README.md",
  "language_code": "ml"
}
-->
# MCP ജാവ ക്ലയന്റ് - കാൽക്കുലേറ്റർ ഡെമോ

ഈ പ്രോജക്ട് MCP (Model Context Protocol) സെർവറുമായി കണക്റ്റ് ചെയ്ത് ഇടപഴകുന്ന ജാവ ക്ലയന്റ് എങ്ങനെ സൃഷ്ടിക്കാമെന്ന് കാണിക്കുന്നു. ഈ ഉദാഹരണത്തിൽ, നാം Chapter 01 ലെ കാൽക്കുലേറ്റർ സെർവറുമായി കണക്റ്റ് ചെയ്ത് വിവിധ ഗണിത പ്രവർത്തനങ്ങൾ നടത്തും.

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

ഈ ക്ലയന്റ് പ്രവർത്തിപ്പിക്കുന്നതിന് മുമ്പ്, നിങ്ങൾക്ക് ചെയ്യേണ്ടത്:

1. Chapter 01 ലെ **കാൽക്കുലേറ്റർ സെർവർ ആരംഭിക്കുക**:
   - കാൽക്കുലേറ്റർ സെർവർ ഡയറക്ടറിയിലേക്ക് പോകുക: `03-GettingStarted/01-first-server/solution/java/`
   - കാൽക്കുലേറ്റർ സെർവർ ബിൽഡ് ചെയ്ത് പ്രവർത്തിപ്പിക്കുക:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - സെർവർ `http://localhost:8080` ൽ പ്രവർത്തിക്കണം

2. നിങ്ങളുടെ സിസ്റ്റത്തിൽ **Java 21 അല്ലെങ്കിൽ അതിനുമുകളിൽ** ഇൻസ്റ്റാൾ ചെയ്തിരിക്കണം
3. **Maven** (Maven Wrapper വഴി ഉൾപ്പെടുത്തിയിട്ടുണ്ട്)

## SDKClient എന്താണ്?

`SDKClient` ഒരു ജാവ അപ്ലിക്കേഷനാണ്, ഇത് കാണിക്കുന്നു:
- Server-Sent Events (SSE) ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവറുമായി കണക്റ്റ് ചെയ്യുന്നത്
- സെർവറിൽ ലഭ്യമായ ടൂളുകൾ ലിസ്റ്റ് ചെയ്യുന്നത്
- വിവിധ കാൽക്കുലേറ്റർ ഫംഗ്ഷനുകൾ റിമോട്ടായി വിളിക്കുന്നത്
- പ്രതികരണങ്ങൾ കൈകാര്യം ചെയ്ത് ഫലങ്ങൾ പ്രദർശിപ്പിക്കുന്നത്

## ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു

ക്ലയന്റ് Spring AI MCP ഫ്രെയിംവർക്ക് ഉപയോഗിക്കുന്നു:

1. **കണക്ഷൻ സ്ഥാപിക്കൽ**: കാൽക്കുലേറ്റർ സെർവറുമായി കണക്റ്റ് ചെയ്യാൻ WebFlux SSE ക്ലയന്റ് ട്രാൻസ്പോർട്ട് സൃഷ്ടിക്കുന്നു
2. **ക്ലയന്റ് ഇൻഷിയലൈസ് ചെയ്യൽ**: MCP ക്ലയന്റ് സജ്ജമാക്കി കണക്ഷൻ സ്ഥാപിക്കുന്നു
3. **ടൂളുകൾ കണ്ടെത്തൽ**: ലഭ്യമായ എല്ലാ കാൽക്കുലേറ്റർ പ്രവർത്തനങ്ങളും ലിസ്റ്റ് ചെയ്യുന്നു
4. **ഓപ്പറേഷനുകൾ നിർവഹിക്കൽ**: സാമ്പിൾ ഡാറ്റ ഉപയോഗിച്ച് വിവിധ ഗണിത ഫംഗ്ഷനുകൾ വിളിക്കുന്നു
5. **ഫലങ്ങൾ പ്രദർശിപ്പിക്കൽ**: ഓരോ കാൽക്കുലേഷന്റെ ഫലങ്ങളും കാണിക്കുന്നു

## പ്രോജക്ട് ഘടന

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

## പ്രധാന ആശ്രിതങ്ങൾ

പ്രോജക്ട് താഴെപ്പറയുന്ന പ്രധാന ആശ്രിതങ്ങൾ ഉപയോഗിക്കുന്നു:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

ഈ ആശ്രിതം നൽകുന്നത്:
- `McpClient` - പ്രധാന ക്ലയന്റ് ഇന്റർഫേസ്
- `WebFluxSseClientTransport` - വെബ് അടിസ്ഥാനത്തിലുള്ള SSE ട്രാൻസ്പോർട്ട്
- MCP പ്രോട്ടോക്കോൾ സ്കീമകളും അഭ്യർത്ഥന/പ്രതികരണ തരംകളും

## പ്രോജക്ട് ബിൽഡ് ചെയ്യൽ

Maven wrapper ഉപയോഗിച്ച് പ്രോജക്ട് ബിൽഡ് ചെയ്യുക:

```cmd
.\mvnw clean install
```

## ക്ലയന്റ് പ്രവർത്തിപ്പിക്കൽ

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**കുറിപ്പ്**: ഈ കമാൻഡുകൾ പ്രവർത്തിപ്പിക്കുന്നതിന് മുമ്പ് കാൽക്കുലേറ്റർ സെർവർ `http://localhost:8080` ൽ പ്രവർത്തിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക.

## ക്ലയന്റ് ചെയ്യുന്നത്

ക്ലയന്റ് പ്രവർത്തിപ്പിക്കുമ്പോൾ, ഇത് ചെയ്യും:

1. `http://localhost:8080` ൽ കാൽക്കുലേറ്റർ സെർവറുമായി **കണക്റ്റ്** ചെയ്യുക
2. **ടൂളുകൾ ലിസ്റ്റ് ചെയ്യുക** - ലഭ്യമായ എല്ലാ കാൽക്കുലേറ്റർ പ്രവർത്തനങ്ങളും കാണിക്കുക
3. **കാൽക്കുലേഷനുകൾ നടത്തുക**:
   - കൂട്ടിച്ചേർക്കൽ: 5 + 3 = 8
   - കുറയ്ക്കൽ: 10 - 4 = 6
   - ഗുണനം: 6 × 7 = 42
   - വിഭജനം: 20 ÷ 4 = 5
   - പവർ: 2^8 = 256
   - വേരിന്റെ ചതുരം: √16 = 4
   - ആബ്സല്യൂട്ട് വാല്യു: |-5.5| = 5.5
   - സഹായം: ലഭ്യമായ പ്രവർത്തനങ്ങൾ കാണിക്കുക

## പ്രതീക്ഷിക്കുന്ന ഔട്ട്പുട്ട്

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

**കുറിപ്പ്**: അവസാനത്തിൽ Maven ലിങ്ക് ചെയ്ത ത്രെഡുകൾക്കുള്ള മുന്നറിയിപ്പുകൾ കാണാം - ഇത് റിയാക്ടീവ് അപ്ലിക്കേഷനുകൾക്ക് സാധാരണമാണ്, പിശക് അല്ല.

## കോഡ് മനസ്സിലാക്കൽ

### 1. ട്രാൻസ്പോർട്ട് സജ്ജീകരണം
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
ഇത് കാൽക്കുലേറ്റർ സെർവറുമായി കണക്റ്റ് ചെയ്യുന്ന SSE (Server-Sent Events) ട്രാൻസ്പോർട്ട് സൃഷ്ടിക്കുന്നു.

### 2. ക്ലയന്റ് സൃഷ്ടിക്കൽ
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
സിങ്ക്രണസ് MCP ക്ലയന്റ് സൃഷ്ടിച്ച് കണക്ഷൻ ഇൻഷിയലൈസ് ചെയ്യുന്നു.

### 3. ടൂളുകൾ വിളിക്കൽ
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
a=5.0, b=3.0 എന്ന പാരാമീറ്ററുകളോടെ "add" ടൂൾ വിളിക്കുന്നു.

## പ്രശ്നപരിഹാരം

### സെർവർ പ്രവർത്തിക്കുന്നില്ല
കണക്ഷൻ പിശകുകൾ ഉണ്ടെങ്കിൽ, Chapter 01 ലെ കാൽക്കുലേറ്റർ സെർവർ പ്രവർത്തിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക:
```
Error: Connection refused
```
**പരിഹാരം**: ആദ്യം കാൽക്കുലേറ്റർ സെർവർ ആരംഭിക്കുക.

### പോർട്ട് ഇതിനകം ഉപയോഗത്തിലാണ്
പോർട്ട് 8080 തിരക്കിലാണ് എങ്കിൽ:
```
Error: Address already in use
```
**പരിഹാരം**: 8080 പോർട്ട് ഉപയോഗിക്കുന്ന മറ്റ് ആപ്ലിക്കേഷനുകൾ നിർത്തുക അല്ലെങ്കിൽ സെർവർ വ്യത്യസ്ത പോർട്ട് ഉപയോഗിക്കാൻ മാറ്റുക.

### ബിൽഡ് പിശകുകൾ
ബിൽഡ് പിശകുകൾ ഉണ്ടെങ്കിൽ:
```cmd
.\mvnw clean install -DskipTests
```

## കൂടുതൽ പഠിക്കുക

- [Spring AI MCP ഡോക്യുമെന്റേഷൻ](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol സ്പെസിഫിക്കേഷൻ](https://modelcontextprotocol.io/)
- [Spring WebFlux ഡോക്യുമെന്റേഷൻ](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->