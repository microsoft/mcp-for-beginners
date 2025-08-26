<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7074b9f4c8cd147c1c10f569d8508c82",
  "translation_date": "2025-08-26T16:57:46+00:00",
  "source_file": "03-GettingStarted/02-client/solution/java/README.md",
  "language_code": "lt"
}
-->
# MCP Java Klientas - Skaičiuotuvo Demonstracija

Šis projektas parodo, kaip sukurti Java klientą, kuris jungiasi prie MCP (Model Context Protocol) serverio ir su juo sąveikauja. Šiame pavyzdyje mes prisijungsime prie skaičiuotuvo serverio iš 1 skyriaus ir atliksime įvairias matematines operacijas.

## Reikalavimai

Prieš paleidžiant šį klientą, reikia:

1. **Paleisti Skaičiuotuvo Serverį** iš 1 skyriaus:
   - Eikite į skaičiuotuvo serverio katalogą: `03-GettingStarted/01-first-server/solution/java/`
   - Sukurkite ir paleiskite skaičiuotuvo serverį:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Serveris turėtų veikti adresu `http://localhost:8080`

2. **Java 21 ar naujesnė versija** įdiegta jūsų sistemoje
3. **Maven** (pridedama per Maven Wrapper)

## Kas yra SDKClient?

`SDKClient` yra Java programa, kuri demonstruoja, kaip:
- Prisijungti prie MCP serverio naudojant Server-Sent Events (SSE) transportą
- Gauti serverio siūlomų įrankių sąrašą
- Nuotoliniu būdu iškviesti įvairias skaičiuotuvo funkcijas
- Apdoroti atsakymus ir parodyti rezultatus

## Kaip tai veikia

Klientas naudoja Spring AI MCP sistemą, kad:

1. **Užmegztų ryšį**: Sukuria WebFlux SSE klientą, kuris jungiasi prie skaičiuotuvo serverio
2. **Inicializuotų klientą**: Nustato MCP klientą ir užmezga ryšį
3. **Aptiktų įrankius**: Parodo visas galimas skaičiuotuvo operacijas
4. **Vykdytų operacijas**: Iškviečia įvairias matematines funkcijas su pavyzdiniais duomenimis
5. **Parodytų rezultatus**: Parodo kiekvienos operacijos rezultatus

## Projekto Struktūra

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

## Pagrindinės Priklausomybės

Projektas naudoja šias pagrindines priklausomybes:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Ši priklausomybė suteikia:
- `McpClient` - Pagrindinė kliento sąsaja
- `WebFluxSseClientTransport` - SSE transportas žiniatinklio ryšiui
- MCP protokolo schemas ir užklausų/atsakymų tipus

## Projekto Kūrimas

Sukurkite projektą naudodami Maven Wrapper:

```cmd
.\mvnw clean install
```

## Kliento Paleidimas

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Pastaba**: Prieš vykdydami šias komandas, įsitikinkite, kad skaičiuotuvo serveris veikia adresu `http://localhost:8080`.

## Ką Atlieka Klientas

Kai paleidžiate klientą, jis:

1. **Prisijungia** prie skaičiuotuvo serverio adresu `http://localhost:8080`
2. **Parodo Įrankius** - Parodo visas galimas skaičiuotuvo operacijas
3. **Atlieka Skaičiavimus**:
   - Sudėtis: 5 + 3 = 8
   - Atimtis: 10 - 4 = 6
   - Daugyba: 6 × 7 = 42
   - Dalyba: 20 ÷ 4 = 5
   - Laipsnis: 2^8 = 256
   - Kvadratinė Šaknis: √16 = 4
   - Absoliuti Vertė: |-5.5| = 5.5
   - Pagalba: Parodo galimas operacijas

## Tikėtinas Rezultatas

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

**Pastaba**: Galite matyti Maven įspėjimus apie likusius procesus programos pabaigoje - tai yra normalu reaktyviose programose ir nereiškia klaidos.

## Kodo Supratimas

### 1. Transporto Nustatymas
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Tai sukuria SSE (Server-Sent Events) transportą, kuris jungiasi prie skaičiuotuvo serverio.

### 2. Kliento Sukūrimas
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Sukuria sinchroninį MCP klientą ir inicializuoja ryšį.

### 3. Įrankių Iškvietimas
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Iškviečia „add“ įrankį su parametrais a=5.0 ir b=3.0.

## Trikčių Šalinimas

### Serveris Neveikia
Jei gaunate ryšio klaidas, įsitikinkite, kad skaičiuotuvo serveris iš 1 skyriaus veikia:
```
Error: Connection refused
```
**Sprendimas**: Pirmiausia paleiskite skaičiuotuvo serverį.

### Uostas Jau Naudojamas
Jei uostas 8080 užimtas:
```
Error: Address already in use
```
**Sprendimas**: Sustabdykite kitas programas, naudojančias uostą 8080, arba pakeiskite serverio uostą.

### Kūrimo Klaidos
Jei susiduriate su kūrimo klaidomis:
```cmd
.\mvnw clean install -DskipTests
```

## Sužinokite Daugiau

- [Spring AI MCP Dokumentacija](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specifikacija](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentacija](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.