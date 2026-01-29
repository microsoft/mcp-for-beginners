# Calculator LLM Client

Μια εφαρμογή Java που δείχνει πώς να χρησιμοποιήσετε το LangChain4j για να συνδεθείτε σε μια υπηρεσία MCP (Model Context Protocol) calculator με ενσωμάτωση GitHub Models.

## Απαιτήσεις

- Java 21 ή νεότερη έκδοση
- Maven 3.6+ (ή χρησιμοποιήστε τον ενσωματωμένο Maven wrapper)
- Λογαριασμός GitHub με πρόσβαση στα GitHub Models
- Μια υπηρεσία MCP calculator που τρέχει στο `http://localhost:8080`

## Λήψη του GitHub Token

Αυτή η εφαρμογή χρησιμοποιεί τα GitHub Models, τα οποία απαιτούν ένα προσωπικό access token από το GitHub. Ακολουθήστε τα παρακάτω βήματα για να αποκτήσετε το token σας:

### 1. Πρόσβαση στα GitHub Models
1. Μεταβείτε στο [GitHub Models](https://github.com/marketplace/models)
2. Συνδεθείτε με τον λογαριασμό σας στο GitHub
3. Ζητήστε πρόσβαση στα GitHub Models αν δεν το έχετε ήδη κάνει

### 2. Δημιουργία Προσωπικού Access Token
1. Μεταβείτε στο [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Πατήστε "Generate new token" → "Generate new token (classic)"
3. Δώστε στο token σας ένα περιγραφικό όνομα (π.χ., "MCP Calculator Client")
4. Ορίστε την ημερομηνία λήξης όπως χρειάζεται
5. Επιλέξτε τα παρακάτω scopes:
   - `repo` (αν χρειάζεστε πρόσβαση σε ιδιωτικά αποθετήρια)
   - `user:email`
6. Πατήστε "Generate token"
7. **Σημαντικό**: Αντιγράψτε το token αμέσως - δεν θα μπορείτε να το δείτε ξανά!

### 3. Ορισμός της Μεταβλητής Περιβάλλοντος

#### Σε Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Σε Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Σε macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Ρύθμιση και Εγκατάσταση

1. **Κλωνοποιήστε ή μεταβείτε στον φάκελο του έργου**

2. **Εγκαταστήστε τις εξαρτήσεις**:
   ```cmd
   mvnw clean install
   ```
   Ή αν έχετε εγκατεστημένο το Maven παγκοσμίως:
   ```cmd
   mvn clean install
   ```

3. **Ορίστε τη μεταβλητή περιβάλλοντος** (δείτε την ενότητα "Λήψη του GitHub Token" παραπάνω)

4. **Εκκινήστε την υπηρεσία MCP Calculator**:
   Βεβαιωθείτε ότι η υπηρεσία MCP calculator από το κεφάλαιο 1 τρέχει στο `http://localhost:8080/sse`. Πρέπει να είναι ενεργή πριν ξεκινήσετε τον client.

## Εκτέλεση της Εφαρμογής

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Τι Κάνει η Εφαρμογή

Η εφαρμογή δείχνει τρεις βασικές αλληλεπιδράσεις με την υπηρεσία calculator:

1. **Πρόσθεση**: Υπολογίζει το άθροισμα των 24.5 και 17.3
2. **Τετραγωνική Ρίζα**: Υπολογίζει την τετραγωνική ρίζα του 144
3. **Βοήθεια**: Εμφανίζει τις διαθέσιμες λειτουργίες του calculator

## Αναμενόμενη Έξοδος

Όταν τρέξει επιτυχώς, θα δείτε έξοδο παρόμοια με:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Επίλυση Προβλημάτων

### Συνηθισμένα Προβλήματα

1. **"GITHUB_TOKEN environment variable not set"**
   - Βεβαιωθείτε ότι έχετε ορίσει τη μεταβλητή περιβάλλοντος `GITHUB_TOKEN`
   - Επανεκκινήστε το τερματικό/command prompt μετά τον ορισμό της μεταβλητής

2. **"Connection refused to localhost:8080"**
   - Ελέγξτε ότι η υπηρεσία MCP calculator τρέχει στην πόρτα 8080
   - Βεβαιωθείτε ότι δεν τρέχει άλλη υπηρεσία στην πόρτα 8080

3. **"Authentication failed"**
   - Επαληθεύστε ότι το GitHub token σας είναι έγκυρο και έχει τα σωστά δικαιώματα
   - Ελέγξτε αν έχετε πρόσβαση στα GitHub Models

4. **Σφάλματα κατά το build με Maven**
   - Βεβαιωθείτε ότι χρησιμοποιείτε Java 21 ή νεότερη: `java -version`
   - Δοκιμάστε να καθαρίσετε το build: `mvnw clean`

### Αποσφαλμάτωση

Για να ενεργοποιήσετε το debug logging, προσθέστε το παρακάτω όρισμα JVM κατά την εκτέλεση:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ρυθμίσεις

Η εφαρμογή έχει ρυθμιστεί να:
- Χρησιμοποιεί τα GitHub Models με το μοντέλο `gpt-4.1-nano`
- Συνδέεται στην υπηρεσία MCP στο `http://localhost:8080/sse`
- Χρησιμοποιεί timeout 60 δευτερολέπτων για τα αιτήματα
- Ενεργοποιεί logging αιτημάτων/απαντήσεων για αποσφαλμάτωση

## Εξαρτήσεις

Κύριες εξαρτήσεις που χρησιμοποιούνται σε αυτό το έργο:
- **LangChain4j**: Για ενσωμάτωση AI και διαχείριση εργαλείων
- **LangChain4j MCP**: Για υποστήριξη Model Context Protocol
- **LangChain4j GitHub Models**: Για ενσωμάτωση GitHub Models
- **Spring Boot**: Για το πλαίσιο εφαρμογής και dependency injection

## Άδεια Χρήσης

Αυτό το έργο διατίθεται υπό την άδεια Apache License 2.0 - δείτε το αρχείο [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) για λεπτομέρειες.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.