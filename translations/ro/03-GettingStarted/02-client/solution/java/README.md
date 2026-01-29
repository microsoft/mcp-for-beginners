# MCP Java Client - Demo Calculator

Acest proiect demonstrează cum să creezi un client Java care se conectează și interacționează cu un server MCP (Model Context Protocol). În acest exemplu, ne vom conecta la serverul calculator din Capitolul 01 și vom efectua diverse operații matematice.

## Cerințe preliminare

Înainte de a rula acest client, trebuie să:

1. **Pornești Serverul Calculator** din Capitolul 01:
   - Navighează în directorul serverului calculator: `03-GettingStarted/01-first-server/solution/java/`
   - Compilează și pornește serverul calculator:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Serverul ar trebui să ruleze la `http://localhost:8080`

2. Ai instalat **Java 21 sau o versiune superioară** pe sistemul tău
3. Ai instalat **Maven** (inclus prin Maven Wrapper)

## Ce este SDKClient?

`SDKClient` este o aplicație Java care demonstrează cum să:
- Te conectezi la un server MCP folosind transportul Server-Sent Events (SSE)
- Listezi uneltele disponibile de pe server
- Apelezi diverse funcții ale calculatorului de la distanță
- Gestionezi răspunsurile și afișezi rezultatele

## Cum funcționează

Clientul folosește cadrul Spring AI MCP pentru a:

1. **Stabili conexiunea**: Creează un client WebFlux SSE pentru a se conecta la serverul calculator
2. **Inițializa clientul**: Configurează clientul MCP și stabilește conexiunea
3. **Descoperi uneltele**: Listează toate operațiile disponibile ale calculatorului
4. **Executa operații**: Apelează diverse funcții matematice cu date de exemplu
5. **Afișa rezultatele**: Arată rezultatele fiecărui calcul

## Structura proiectului

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

## Dependențe cheie

Proiectul folosește următoarele dependențe principale:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Această dependență oferă:
- `McpClient` - Interfața principală a clientului
- `WebFluxSseClientTransport` - Transport SSE pentru comunicare web
- Schemele protocolului MCP și tipurile de cereri/răspunsuri

## Construirea proiectului

Construiește proiectul folosind Maven wrapper:

```cmd
.\mvnw clean install
```

## Rularea clientului

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Notă**: Asigură-te că serverul calculator rulează la `http://localhost:8080` înainte de a executa oricare dintre aceste comenzi.

## Ce face clientul

Când rulezi clientul, acesta va:

1. **Se conecta** la serverul calculator la `http://localhost:8080`
2. **Lista uneltele** - Afișează toate operațiile disponibile ale calculatorului
3. **Efectua calcule**:
   - Adunare: 5 + 3 = 8
   - Scădere: 10 - 4 = 6
   - Înmulțire: 6 × 7 = 42
   - Împărțire: 20 ÷ 4 = 5
   - Putere: 2^8 = 256
   - Rădăcină pătrată: √16 = 4
   - Valoare absolută: |-5.5| = 5.5
   - Ajutor: Afișează operațiile disponibile

## Rezultatul așteptat

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

**Notă**: Este posibil să vezi avertismente Maven despre fire rămase active la final - acest comportament este normal pentru aplicațiile reactive și nu indică o eroare.

## Înțelegerea codului

### 1. Configurarea transportului
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Aceasta creează un transport SSE (Server-Sent Events) care se conectează la serverul calculator.

### 2. Crearea clientului
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Creează un client MCP sincron și inițializează conexiunea.

### 3. Apelarea uneltelor
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Apelează unealta "add" cu parametrii a=5.0 și b=3.0.

## Depanare

### Serverul nu rulează
Dacă primești erori de conexiune, asigură-te că serverul calculator din Capitolul 01 este pornit:
```
Error: Connection refused
```
**Soluție**: Pornește mai întâi serverul calculator.

### Portul este deja folosit
Dacă portul 8080 este ocupat:
```
Error: Address already in use
```
**Soluție**: Oprește alte aplicații care folosesc portul 8080 sau modifică serverul să folosească un alt port.

### Erori la construire
Dacă întâmpini erori la construire:
```cmd
.\mvnw clean install -DskipTests
```

## Mai multe informații

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.