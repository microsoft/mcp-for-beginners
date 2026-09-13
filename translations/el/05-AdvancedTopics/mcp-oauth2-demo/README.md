# Επίδειξη MCP OAuth2

> [!WARNING]
> Αυτό είναι ένα τοπικό δείγμα μάθησης, όχι μια υπηρεσία εξουσιοδότησης παραγωγής. Χρησιμοποιεί έναν πελάτη στη μνήμη και δημιουργεί ένα νέο κλειδί υπογραφής κατά την εκκίνηση. Μην
> το αναπτύσσετε ποτέ με κοινόχρηστο, προεπιλεγμένο ή υπό έλεγχο έκδοσης μυστικό πελάτη.


## Εισαγωγή

Το OAuth2 είναι το βιομηχανικό πρότυπο πρωτόκολλο για την εξουσιοδότηση, επιτρέποντας ασφαλή πρόσβαση σε πόρους χωρίς την κοινοποίηση διαπιστευτηρίων. Στις υλοποιήσεις MCP (Model Context Protocol), το OAuth2 παρέχει έναν ισχυρό τρόπο πιστοποίησης και εξουσιοδότησης πελατών (όπως οι πράκτορες AI) για πρόσβαση σε διακομιστές MCP και τα εργαλεία τους.

Αυτό το μάθημα δείχνει πώς να υλοποιήσετε πιστοποίηση OAuth2 για διακομιστές MCP χρησιμοποιώντας Spring Boot, ένα κοινό μοτίβο για επιχειρησιακές και παραγωγικές αναπτύξεις.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του μαθήματος, θα:
- Κατανοείτε πώς το OAuth2 ενσωματώνεται με διακομιστές MCP
- Υλοποιείτε έναν Spring Authorization Server για έκδοση token
- Προστατεύετε τα σημεία πρόσβασης MCP με πιστοποίηση βασισμένη σε JWT
- Διαμορφώνετε τη ροή client credentials για επικοινωνία μηχανής με μηχανή

## Προαπαιτούμενα

- Βασική κατανόηση της Java και του Spring Boot
- Εξοικείωση με τις έννοιες MCP από προηγούμενα μαθήματα
- Εγκατάσταση Maven ή Gradle

---

## Επισκόπηση Έργου

Αυτό το έργο είναι μια **ελάχιστη εφαρμογή Spring Boot** που λειτουργεί και ως:

* **Spring Authorization Server** (εκδίδοντας JWT access tokens μέσω της ροής `client_credentials`), και  
* **Resource Server** (προστατεύοντας το δικό του σημείο πρόσβασης `/hello`).

Αντικατοπτρίζει τη διαμόρφωση που εμφανίζεται στην [ανάρτηση ιστολογίου Spring (2 Απρ 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Γρήγορη εκκίνηση (τοπικά)

```bash
# Χρησιμοποιήστε μια μοναδική τοπική τιμή και κρατήστε την εκτός ιστορικού του shell όπου είναι δυνατόν.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# λάβετε ένα διακριτικό
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# καλέστε το προστατευμένο σημείο τερματισμού
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Δοκιμή της διαμόρφωσης OAuth2

Μπορείτε να δοκιμάσετε τη διαμόρφωση ασφαλείας OAuth2 με τα ακόλουθα βήματα:

### 1. Επιβεβαιώστε ότι ο διακομιστής λειτουργεί και είναι ασφαλής

```bash
# Αυτό θα πρέπει να επιστρέψει 401 Unauthorized, επιβεβαιώνοντας ότι η ασφάλεια OAuth2 είναι ενεργή
curl -v http://localhost:8081/
```

### 2. Πάρτε ένα access token χρησιμοποιώντας τα διαπιστευτήρια πελάτη

```bash
# Λάβετε και εξαγάγετε την πλήρη απάντηση του διακριτικού
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Ή για να εξαγάγετε μόνο το διακριτικό (απαιτεί jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Στο PowerShell, ορίστε το τοπικό μυστικό πριν τρέξετε το Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Πρόσβαση στο προστατευμένο σημείο πρόσβασης με το token

```bash
# Χρήση του αποθηκευμένου token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Ή απευθείας με την τιμή του token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Μια επιτυχημένη απόκριση με "Hello from MCP OAuth2 Demo!" επιβεβαιώνει ότι η διαμόρφωση OAuth2 λειτουργεί σωστά.

---

## Κατασκευή κοντέινερ

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Ασφάλεια παραγωγής

Για μια παραγωγική ανάπτυξη, χρησιμοποιήστε έναν αφιερωμένο πάροχο ταυτότητας αντί
αυτού του ενδοδιαδικαστικού demo authorization server. Αποθηκεύστε διαπιστευτήρια σε
έναν διαχειριζόμενο αποθηκευτικό χώρο μυστικών, ανανεώστε τα, χρησιμοποιήστε μόνιμα κλειδιά υπογραφής, περιορίστε τους χώρους αρμοδιότητας και
ορίστε ρητά τον εκδότη. Ποτέ μην βάζετε μυστικό πελάτη σε πηγαίο κώδικα, εικόνες κοντέινερ,
εκθέσεις ανάπτυξης ή έξοδο εντολών.

Για το Azure Container Apps, αποθηκεύστε την τιμή ως μυστικό Container Apps υποστηριζόμενο από
το Key Vault όπου είναι δυνατόν, και εκθέστε μόνο μια αναφορά μυστικού μέσω της
μεταβλητής περιβάλλοντος `OAUTH_CLIENT_SECRET`.

---

## Ανάπτυξη σε **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Το fully qualified domain name εισόδου γίνεται ο **εκδότης** σας (`https://<fqdn>`).  
Το Azure παρέχει αυτόματα ένα έγκυρο πιστοποιητικό TLS για `*.azurecontainerapps.io`.

---

## Σύνδεση με **Azure API Management**

Προσθέστε αυτή την πολιτική εισερχομένων στο API σας:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

Το APIM θα λάβει το JWKS και θα επαληθεύει κάθε αίτημα.

---

## Τι ακολουθεί

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->