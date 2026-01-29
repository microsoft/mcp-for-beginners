# MCP Java Client - Skaičiuotuvo Demonstracija

Šis projektas parodo, kaip sukurti Java klientą, kuris jungiasi prie MCP (Model Context Protocol) serverio ir sąveikauja su juo. Šiame pavyzdyje prisijungsime prie skaičiuotuvo serverio iš 01 skyriaus ir atliksime įvairias matematines operacijas.

## Reikalavimai

Prieš paleisdami klientą, turite:

1. **Paleisti Skaičiuotuvo Serverį** iš 01 skyriaus:
   - Eikite į skaičiuotuvo serverio katalogą: `03-GettingStarted/01-first-server/solution/java/`
   - Sukurkite ir paleiskite skaičiuotuvo serverį:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Serveris turėtų veikti adresu `http://localhost:8080`

2. **Java 21 ar naujesnė versija** įdiegta jūsų sistemoje
3. **Maven** (įtrauktas per Maven Wrapper)

## Kas yra SDKClient?

`SDKClient` yra Java programa, kuri parodo, kaip:
- Prisijungti prie MCP serverio naudojant Server-Sent Events (SSE) transportą
- Peržiūrėti serverio siūlomus įrankius
- Nuotoliniu būdu iškviesti įvairias skaičiuotuvo funkcijas
- Tvarkyti atsakymus ir rodyti rezultatus

## Kaip tai veikia

Klientas naudoja Spring AI MCP sistemą, kad:

1. **Užmegztų ryšį**: Sukuria WebFlux SSE klientą, kuris jungiasi prie skaičiuotuvo serverio
2. **Inicializuotų klientą**: Nustato MCP klientą ir užmezga ryšį
3. **Atrastų įrankius**: Peržiūri visus galimus skaičiuotuvo veiksmus
4. **Vykdytų operacijas**: Nuotoliniu būdu iškviečia matematines funkcijas su pavyzdiniais duomenimis
5. **Rodytų rezultatus**: Parodo kiekvienos operacijos rezultatus

## Projekto struktūra

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

## Pagrindinės priklausomybės

Projektas naudoja šias pagrindines priklausomybes:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Ši priklausomybė suteikia:
- `McpClient` - Pagrindinę kliento sąsają
- `WebFluxSseClientTransport` - SSE transportą, skirtą komunikacijai per internetą
- MCP protokolo schemas ir užklausų/atsakymų tipus

## Projekto kūrimas

Sukurkite projektą naudodami Maven Wrapper:

```cmd
.\mvnw clean install
```

## Kliento paleidimas

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Pastaba**: Prieš vykdydami bet kurią iš šių komandų, įsitikinkite, kad skaičiuotuvo serveris veikia adresu `http://localhost:8080`.

## Ką daro klientas

Kai paleisite klientą, jis:

1. **Prisijungs** prie skaičiuotuvo serverio adresu `http://localhost:8080`
2. **Peržiūrės įrankius** - Parodys visus galimus skaičiuotuvo veiksmus
3. **Atliks skaičiavimus**:
   - Sudėtis: 5 + 3 = 8
   - Atimtis: 10 - 4 = 6
   - Daugyba: 6 × 7 = 42
   - Dalyba: 20 ÷ 4 = 5
   - Laipsnis: 2^8 = 256
   - Kvadratinė šaknis: √16 = 4
   - Absoliuti vertė: |-5.5| = 5.5
   - Pagalba: Parodo galimus veiksmus

## Tikėtinas rezultatas

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

**Pastaba**: Galite matyti Maven įspėjimus apie likusius gijas programos pabaigoje - tai yra normalu reaktyviose programose ir nereiškia klaidos.

## Kodo supratimas

### 1. Transporto nustatymas
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Tai sukuria SSE (Server-Sent Events) transportą, kuris jungiasi prie skaičiuotuvo serverio.

### 2. Kliento sukūrimas
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Sukuria sinchroninį MCP klientą ir inicializuoja ryšį.

### 3. Įrankių iškvietimas
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Iškviečia „add“ įrankį su parametrais a=5.0 ir b=3.0.

## Trikčių šalinimas

### Serveris neveikia
Jei gaunate ryšio klaidas, įsitikinkite, kad skaičiuotuvo serveris iš 01 skyriaus veikia:
```
Error: Connection refused
```
**Sprendimas**: Pirmiausia paleiskite skaičiuotuvo serverį.

### Uostas jau naudojamas
Jei uostas 8080 užimtas:
```
Error: Address already in use
```
**Sprendimas**: Sustabdykite kitas programas, naudojančias uostą 8080, arba pakeiskite serverio uostą.

### Kūrimo klaidos
Jei susiduriate su kūrimo klaidomis:
```cmd
.\mvnw clean install -DskipTests
```

## Sužinokite daugiau

- [Spring AI MCP Dokumentacija](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specifikacija](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentacija](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.