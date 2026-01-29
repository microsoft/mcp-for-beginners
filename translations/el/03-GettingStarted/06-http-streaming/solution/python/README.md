# Εκτέλεση αυτού του δείγματος

Ακολουθούν οι οδηγίες για την εκτέλεση του κλασικού HTTP streaming server και client, καθώς και του MCP streaming server και client χρησιμοποιώντας Python.

### Επισκόπηση

- Θα ρυθμίσετε έναν MCP server που μεταδίδει ειδοποιήσεις προόδου στον client καθώς επεξεργάζεται αντικείμενα.
- Ο client θα εμφανίζει κάθε ειδοποίηση σε πραγματικό χρόνο.
- Αυτός ο οδηγός καλύπτει τις προϋποθέσεις, τη ρύθμιση, την εκτέλεση και την αντιμετώπιση προβλημάτων.

### Προϋποθέσεις

- Python 3.9 ή νεότερη έκδοση
- Το πακέτο Python `mcp` (εγκατάσταση με `pip install mcp`)

### Εγκατάσταση & Ρύθμιση

1. Κλωνοποιήστε το αποθετήριο ή κατεβάστε τα αρχεία της λύσης.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Δημιουργήστε και ενεργοποιήστε ένα εικονικό περιβάλλον (συνιστάται):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Εγκαταστήστε τις απαιτούμενες εξαρτήσεις:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Αρχεία

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Εκτέλεση του Κλασικού HTTP Streaming Server

1. Μεταβείτε στον κατάλογο της λύσης:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Ξεκινήστε τον κλασικό HTTP streaming server:

   ```pwsh
   python server.py
   ```

3. Ο server θα ξεκινήσει και θα εμφανίσει:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Εκτέλεση του Κλασικού HTTP Streaming Client

1. Ανοίξτε ένα νέο τερματικό (ενεργοποιήστε το ίδιο εικονικό περιβάλλον και κατάλογο):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Θα δείτε μηνύματα που μεταδίδονται και εκτυπώνονται διαδοχικά:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Εκτέλεση του MCP Streaming Server

1. Μεταβείτε στον κατάλογο της λύσης:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Ξεκινήστε τον MCP server με το streamable-http transport:
   ```pwsh
   python server.py mcp
   ```
3. Ο server θα ξεκινήσει και θα εμφανίσει:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Εκτέλεση του MCP Streaming Client

1. Ανοίξτε ένα νέο τερματικό (ενεργοποιήστε το ίδιο εικονικό περιβάλλον και κατάλογο):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Θα δείτε ειδοποιήσεις να εκτυπώνονται σε πραγματικό χρόνο καθώς ο server επεξεργάζεται κάθε αντικείμενο:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Βασικά Βήματα Υλοποίησης

1. **Δημιουργήστε τον MCP server χρησιμοποιώντας το FastMCP.**
2. **Ορίστε ένα εργαλείο που επεξεργάζεται μια λίστα και στέλνει ειδοποιήσεις χρησιμοποιώντας `ctx.info()` ή `ctx.log()`.**
3. **Εκτελέστε τον server με `transport="streamable-http"`.**
4. **Υλοποιήστε έναν client με έναν χειριστή μηνυμάτων για να εμφανίζει ειδοποιήσεις καθώς φτάνουν.**

### Ανάλυση Κώδικα
- Ο server χρησιμοποιεί ασύγχρονες συναρτήσεις και το MCP context για να στέλνει ενημερώσεις προόδου.
- Ο client υλοποιεί έναν ασύγχρονο χειριστή μηνυμάτων για να εκτυπώνει ειδοποιήσεις και το τελικό αποτέλεσμα.

### Συμβουλές & Αντιμετώπιση Προβλημάτων

- Χρησιμοποιήστε `async/await` για μη μπλοκαρισμένες λειτουργίες.
- Πάντα να χειρίζεστε εξαιρέσεις τόσο στον server όσο και στον client για μεγαλύτερη αξιοπιστία.
- Δοκιμάστε με πολλούς clients για να παρατηρήσετε ενημερώσεις σε πραγματικό χρόνο.
- Εάν αντιμετωπίσετε σφάλματα, ελέγξτε την έκδοση της Python και βεβαιωθείτε ότι όλες οι εξαρτήσεις είναι εγκατεστημένες.

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.