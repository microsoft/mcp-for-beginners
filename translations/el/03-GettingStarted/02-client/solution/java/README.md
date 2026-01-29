# MCP Java Client - Παράδειγμα Αριθμομηχανής

Αυτό το έργο δείχνει πώς να δημιουργήσετε έναν Java client που συνδέεται και αλληλεπιδρά με έναν MCP (Model Context Protocol) server. Σε αυτό το παράδειγμα, θα συνδεθούμε στον server της αριθμομηχανής από το Κεφάλαιο 01 και θα εκτελέσουμε διάφορες μαθηματικές πράξεις.

## Προαπαιτούμενα

Πριν τρέξετε αυτόν τον client, πρέπει να:

1. **Εκκινήσετε τον Calculator Server** από το Κεφάλαιο 01:
   - Μεταβείτε στον φάκελο του calculator server: `03-GettingStarted/01-first-server/solution/java/`
   - Δημιουργήστε και τρέξτε τον calculator server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Ο server θα πρέπει να τρέχει στο `http://localhost:8080`

2. Έχετε εγκατεστημένο **Java 21 ή νεότερη έκδοση** στο σύστημά σας  
3. Έχετε **Maven** (περιλαμβάνεται μέσω Maven Wrapper)

## Τι είναι το SDKClient;

Το `SDKClient` είναι μια Java εφαρμογή που δείχνει πώς να:
- Συνδεθείτε σε έναν MCP server χρησιμοποιώντας Server-Sent Events (SSE) μεταφορά
- Λίστα διαθέσιμων εργαλείων από τον server
- Καλείτε διάφορες λειτουργίες της αριθμομηχανής απομακρυσμένα
- Διαχειρίζεστε τις απαντήσεις και εμφανίζετε τα αποτελέσματα

## Πώς Λειτουργεί

Ο client χρησιμοποιεί το Spring AI MCP framework για να:

1. **Εγκαθιδρύσει Σύνδεση**: Δημιουργεί έναν WebFlux SSE client transport για να συνδεθεί στον calculator server  
2. **Αρχικοποιήσει τον Client**: Ρυθμίζει τον MCP client και δημιουργεί τη σύνδεση  
3. **Ανακαλύψει Εργαλεία**: Λίστα με όλες τις διαθέσιμες λειτουργίες της αριθμομηχανής  
4. **Εκτελέσει Πράξεις**: Καλεί διάφορες μαθηματικές συναρτήσεις με δείγματα δεδομένων  
5. **Εμφανίσει Αποτελέσματα**: Δείχνει τα αποτελέσματα κάθε υπολογισμού

## Δομή του Έργου

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

## Κύριες Εξαρτήσεις

Το έργο χρησιμοποιεί τις παρακάτω βασικές εξαρτήσεις:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Αυτή η εξάρτηση παρέχει:  
- `McpClient` - Η κύρια διεπαφή client  
- `WebFluxSseClientTransport` - SSE μεταφορά για επικοινωνία μέσω web  
- Σχήματα πρωτοκόλλου MCP και τύπους αιτήσεων/απαντήσεων

## Δημιουργία του Έργου

Δημιουργήστε το έργο χρησιμοποιώντας τον Maven wrapper:

```cmd
.\mvnw clean install
```

## Εκτέλεση του Client

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Σημείωση**: Βεβαιωθείτε ότι ο calculator server τρέχει στο `http://localhost:8080` πριν εκτελέσετε οποιαδήποτε από αυτές τις εντολές.

## Τι Κάνει ο Client

Όταν τρέξετε τον client, θα:

1. **Συνδεθεί** στον calculator server στο `http://localhost:8080`  
2. **Λίστα Εργαλείων** - Εμφανίζει όλες τις διαθέσιμες λειτουργίες της αριθμομηχανής  
3. **Εκτελέσει Υπολογισμούς**:  
   - Πρόσθεση: 5 + 3 = 8  
   - Αφαίρεση: 10 - 4 = 6  
   - Πολλαπλασιασμός: 6 × 7 = 42  
   - Διαίρεση: 20 ÷ 4 = 5  
   - Δύναμη: 2^8 = 256  
   - Τετραγωνική Ρίζα: √16 = 4  
   - Απόλυτη Τιμή: |-5.5| = 5.5  
   - Βοήθεια: Εμφανίζει τις διαθέσιμες λειτουργίες

## Αναμενόμενη Έξοδος

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

**Σημείωση**: Μπορεί να δείτε προειδοποιήσεις Maven για εκκρεμείς νήματα στο τέλος - αυτό είναι φυσιολογικό για εφαρμογές με reactive προγραμματισμό και δεν υποδηλώνει σφάλμα.

## Κατανόηση του Κώδικα

### 1. Ρύθμιση Μεταφοράς
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```  
Αυτό δημιουργεί μια SSE (Server-Sent Events) μεταφορά που συνδέεται στον calculator server.

### 2. Δημιουργία Client
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```  
Δημιουργεί έναν συγχρονισμένο MCP client και αρχικοποιεί τη σύνδεση.

### 3. Κλήση Εργαλείων
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```  
Καλεί το εργαλείο "add" με παραμέτρους a=5.0 και b=3.0.

## Αντιμετώπιση Προβλημάτων

### Ο Server Δεν Τρέχει  
Αν λαμβάνετε σφάλματα σύνδεσης, βεβαιωθείτε ότι ο calculator server από το Κεφάλαιο 01 τρέχει:  
```
Error: Connection refused
```  
**Λύση**: Ξεκινήστε πρώτα τον calculator server.

### Η Θύρα Είναι Κατειλημμένη  
Αν η θύρα 8080 είναι κατειλημμένη:  
```
Error: Address already in use
```  
**Λύση**: Σταματήστε άλλες εφαρμογές που χρησιμοποιούν τη θύρα 8080 ή τροποποιήστε τον server να χρησιμοποιεί άλλη θύρα.

### Σφάλματα Κατασκευής  
Αν αντιμετωπίζετε σφάλματα κατά την κατασκευή:  
```cmd
.\mvnw clean install -DskipTests
```

## Μάθετε Περισσότερα

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)  
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)  
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.