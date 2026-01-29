# Calculator HTTP Streaming Demo

Αυτό το έργο παρουσιάζει HTTP streaming χρησιμοποιώντας Server-Sent Events (SSE) με Spring Boot WebFlux. Αποτελείται από δύο εφαρμογές:

- **Calculator Server**: Μια αντιδραστική web υπηρεσία που εκτελεί υπολογισμούς και μεταδίδει αποτελέσματα μέσω SSE  
- **Calculator Client**: Μια πελατειακή εφαρμογή που καταναλώνει το streaming endpoint

## Προαπαιτούμενα

- Java 17 ή νεότερη έκδοση  
- Maven 3.6 ή νεότερη έκδοση

## Δομή Έργου

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Πώς Λειτουργεί

1. Ο **Calculator Server** εκθέτει ένα endpoint `/calculate` που:  
   - Δέχεται παραμέτρους ερωτήματος: `a` (αριθμός), `b` (αριθμός), `op` (λειτουργία)  
   - Υποστηριζόμενες λειτουργίες: `add`, `sub`, `mul`, `div`  
   - Επιστρέφει Server-Sent Events με την πρόοδο του υπολογισμού και το αποτέλεσμα

2. Ο **Calculator Client** συνδέεται με τον server και:  
   - Κάνει αίτημα για τον υπολογισμό `7 * 5`  
   - Καταναλώνει την streaming απάντηση  
   - Εκτυπώνει κάθε event στην κονσόλα

## Εκτέλεση των Εφαρμογών

### Επιλογή 1: Χρήση Maven (Συνιστάται)

#### 1. Εκκίνηση του Calculator Server

Άνοιξε ένα τερματικό και πήγαινε στον φάκελο του server:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Ο server θα ξεκινήσει στο `http://localhost:8080`

Θα δεις έξοδο όπως:  
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Εκτέλεση του Calculator Client

Άνοιξε **νέο τερματικό** και πήγαινε στον φάκελο του client:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Ο client θα συνδεθεί με τον server, θα εκτελέσει τον υπολογισμό και θα εμφανίσει τα streaming αποτελέσματα.

### Επιλογή 2: Χρήση Java απευθείας

#### 1. Μεταγλώττιση και εκτέλεση του server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Μεταγλώττιση και εκτέλεση του client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Χειροκίνητος Έλεγχος του Server

Μπορείς επίσης να δοκιμάσεις τον server χρησιμοποιώντας έναν web browser ή curl:

### Χρήση web browser:  
Επισκέψου: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Χρήση curl:  
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Αναμενόμενη Έξοδος

Κατά την εκτέλεση του client, θα δεις streaming έξοδο παρόμοια με:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Υποστηριζόμενες Λειτουργίες

- `add` - Πρόσθεση (a + b)  
- `sub` - Αφαίρεση (a - b)  
- `mul` - Πολλαπλασιασμός (a * b)  
- `div` - Διαίρεση (a / b, επιστρέφει NaN αν b = 0)

## Αναφορά API

### GET /calculate

**Παράμετροι:**  
- `a` (απαραίτητο): Πρώτος αριθμός (double)  
- `b` (απαραίτητο): Δεύτερος αριθμός (double)  
- `op` (απαραίτητο): Λειτουργία (`add`, `sub`, `mul`, `div`)

**Απάντηση:**  
- Content-Type: `text/event-stream`  
- Επιστρέφει Server-Sent Events με την πρόοδο και το αποτέλεσμα του υπολογισμού

**Παράδειγμα Αιτήματος:**  
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Παράδειγμα Απάντησης:**  
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Αντιμετώπιση Προβλημάτων

### Συνηθισμένα Προβλήματα

1. **Η θύρα 8080 χρησιμοποιείται ήδη**  
   - Σταμάτησε οποιεσδήποτε άλλες εφαρμογές που χρησιμοποιούν τη θύρα 8080  
   - Ή άλλαξε τη θύρα του server στο `calculator-server/src/main/resources/application.yml`

2. **Απόρριψη σύνδεσης**  
   - Βεβαιώσου ότι ο server τρέχει πριν ξεκινήσεις τον client  
   - Έλεγξε ότι ο server ξεκίνησε επιτυχώς στη θύρα 8080

3. **Προβλήματα με ονόματα παραμέτρων**  
   - Το έργο περιλαμβάνει ρύθμιση Maven compiler με τη σημαία `-parameters`  
   - Αν αντιμετωπίσεις προβλήματα με το binding παραμέτρων, βεβαιώσου ότι το έργο έχει χτιστεί με αυτή τη ρύθμιση

### Τερματισμός των Εφαρμογών

- Πάτησε `Ctrl+C` στο τερματικό όπου τρέχει κάθε εφαρμογή  
- Ή χρησιμοποίησε `mvn spring-boot:stop` αν τρέχει ως background process

## Τεχνολογικό Υπόβαθρο

- **Spring Boot 3.3.1** - Πλαίσιο εφαρμογής  
- **Spring WebFlux** - Αντιδραστικό web πλαίσιο  
- **Project Reactor** - Βιβλιοθήκη reactive streams  
- **Netty** - Server μη αποκλειστικής εισόδου/εξόδου  
- **Maven** - Εργαλείο κατασκευής  
- **Java 17+** - Γλώσσα προγραμματισμού

## Επόμενα Βήματα

Δοκίμασε να τροποποιήσεις τον κώδικα για να:  
- Προσθέσεις περισσότερες μαθηματικές λειτουργίες  
- Ενσωματώσεις χειρισμό σφαλμάτων για μη έγκυρες λειτουργίες  
- Προσθέσεις καταγραφή αιτημάτων/απαντήσεων  
- Υλοποιήσεις αυθεντικοποίηση  
- Προσθέσεις unit tests

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.