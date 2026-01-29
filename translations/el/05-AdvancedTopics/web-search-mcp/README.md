# Μάθημα: Δημιουργία ενός Web Search MCP Server

Αυτό το κεφάλαιο δείχνει πώς να δημιουργήσετε έναν πραγματικό AI agent που ενσωματώνεται με εξωτερικά APIs, διαχειρίζεται διάφορους τύπους δεδομένων, χειρίζεται σφάλματα και συντονίζει πολλαπλά εργαλεία — όλα σε μορφή έτοιμη για παραγωγή. Θα δείτε:

- **Ενσωμάτωση με εξωτερικά APIs που απαιτούν αυθεντικοποίηση**
- **Διαχείριση διαφορετικών τύπων δεδομένων από πολλαπλά endpoints**
- **Αξιόπιστη διαχείριση σφαλμάτων και στρατηγικές καταγραφής**
- **Συντονισμός πολλαπλών εργαλείων σε έναν ενιαίο server**

Στο τέλος, θα έχετε πρακτική εμπειρία με πρότυπα και βέλτιστες πρακτικές που είναι απαραίτητες για προηγμένες εφαρμογές AI και LLM.

## Εισαγωγή

Σε αυτό το μάθημα, θα μάθετε πώς να δημιουργήσετε έναν προηγμένο MCP server και client που επεκτείνει τις δυνατότητες των LLM με δεδομένα web σε πραγματικό χρόνο χρησιμοποιώντας το SerpAPI. Αυτή είναι μια κρίσιμη δεξιότητα για την ανάπτυξη δυναμικών AI agents που μπορούν να έχουν πρόσβαση σε ενημερωμένες πληροφορίες από το διαδίκτυο.

## Στόχοι Μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Ενσωματώνετε εξωτερικά APIs (όπως το SerpAPI) με ασφάλεια σε έναν MCP server
- Υλοποιείτε πολλαπλά εργαλεία για αναζήτηση στο web, ειδήσεις, προϊόντα και Q&A
- Αναλύετε και μορφοποιείτε δομημένα δεδομένα για κατανάλωση από LLM
- Διαχειρίζεστε σφάλματα και όρια ρυθμού API αποτελεσματικά
- Δημιουργείτε και δοκιμάζετε τόσο αυτοματοποιημένους όσο και διαδραστικούς MCP clients

## Web Search MCP Server

Αυτή η ενότητα παρουσιάζει την αρχιτεκτονική και τα χαρακτηριστικά του Web Search MCP Server. Θα δείτε πώς το FastMCP και το SerpAPI χρησιμοποιούνται μαζί για να επεκτείνουν τις δυνατότητες των LLM με δεδομένα web σε πραγματικό χρόνο.

### Επισκόπηση

Αυτή η υλοποίηση περιλαμβάνει τέσσερα εργαλεία που αναδεικνύουν την ικανότητα του MCP να χειρίζεται ποικίλες, εξωτερικές εργασίες API με ασφάλεια και αποδοτικότητα:

- **general_search**: Για ευρείες αναζητήσεις στο διαδίκτυο
- **news_search**: Για πρόσφατους τίτλους ειδήσεων
- **product_search**: Για δεδομένα ηλεκτρονικού εμπορίου
- **qna**: Για αποσπάσματα ερωτήσεων και απαντήσεων

### Χαρακτηριστικά
- **Παραδείγματα Κώδικα**: Περιλαμβάνει μπλοκ κώδικα για Python (και εύκολα επεκτάσιμα σε άλλες γλώσσες) με χρήση code pivots για σαφήνεια

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Πριν τρέξετε τον client, είναι χρήσιμο να κατανοήσετε τι κάνει ο server. Το αρχείο [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) υλοποιεί τον MCP server, εκθέτοντας εργαλεία για αναζήτηση στο web, ειδήσεις, προϊόντα και Q&A μέσω ενσωμάτωσης με το SerpAPI. Διαχειρίζεται εισερχόμενα αιτήματα, καλεί τα APIs, αναλύει τις απαντήσεις και επιστρέφει δομημένα αποτελέσματα στον client.

Μπορείτε να δείτε την πλήρη υλοποίηση στο [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Ακολουθεί ένα σύντομο παράδειγμα για το πώς ο server ορίζει και καταχωρεί ένα εργαλείο:

### Python Server

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Ενσωμάτωση Εξωτερικού API**: Δείχνει ασφαλή διαχείριση κλειδιών API και εξωτερικών αιτημάτων
- **Ανάλυση Δομημένων Δεδομένων**: Δείχνει πώς να μετατρέπετε τις απαντήσεις API σε μορφές φιλικές προς LLM
- **Διαχείριση Σφαλμάτων**: Αξιόπιστη διαχείριση σφαλμάτων με κατάλληλη καταγραφή
- **Διαδραστικός Client**: Περιλαμβάνει τόσο αυτοματοποιημένες δοκιμές όσο και διαδραστική λειτουργία για δοκιμές
- **Διαχείριση Συμφραζομένων**: Χρησιμοποιεί το MCP Context για καταγραφή και παρακολούθηση αιτημάτων

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι το περιβάλλον σας είναι σωστά ρυθμισμένο ακολουθώντας τα παρακάτω βήματα. Αυτό θα εξασφαλίσει ότι όλες οι εξαρτήσεις είναι εγκατεστημένες και τα κλειδιά API σας έχουν ρυθμιστεί σωστά για ομαλή ανάπτυξη και δοκιμές.

- Python 3.8 ή νεότερη
- Κλειδί API SerpAPI (Εγγραφείτε στο [SerpAPI](https://serpapi.com/) - υπάρχει δωρεάν επίπεδο)

## Εγκατάσταση

Για να ξεκινήσετε, ακολουθήστε τα παρακάτω βήματα για να ρυθμίσετε το περιβάλλον σας:

1. Εγκαταστήστε τις εξαρτήσεις χρησιμοποιώντας uv (συνιστάται) ή pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Δημιουργήστε ένα αρχείο `.env` στον ριζικό φάκελο του έργου με το κλειδί SerpAPI σας:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Χρήση

Ο Web Search MCP Server είναι το βασικό συστατικό που εκθέτει εργαλεία για αναζήτηση στο web, ειδήσεις, προϊόντα και Q&A μέσω ενσωμάτωσης με το SerpAPI. Διαχειρίζεται εισερχόμενα αιτήματα, καλεί τα APIs, αναλύει τις απαντήσεις και επιστρέφει δομημένα αποτελέσματα στον client.

Μπορείτε να δείτε την πλήρη υλοποίηση στο [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Εκκίνηση του Server

Για να ξεκινήσετε τον MCP server, χρησιμοποιήστε την παρακάτω εντολή:

```bash
python server.py
```

Ο server θα τρέξει ως stdio-based MCP server στον οποίο ο client μπορεί να συνδεθεί απευθείας.

### Λειτουργίες Client

Ο client (`client.py`) υποστηρίζει δύο λειτουργίες για αλληλεπίδραση με τον MCP server:

- **Κανονική λειτουργία**: Τρέχει αυτοματοποιημένες δοκιμές που ελέγχουν όλα τα εργαλεία και επαληθεύουν τις απαντήσεις τους. Αυτό είναι χρήσιμο για γρήγορο έλεγχο ότι ο server και τα εργαλεία λειτουργούν όπως αναμένεται.
- **Διαδραστική λειτουργία**: Ξεκινά ένα μενού όπου μπορείτε χειροκίνητα να επιλέξετε και να καλέσετε εργαλεία, να εισάγετε προσαρμοσμένα ερωτήματα και να δείτε τα αποτελέσματα σε πραγματικό χρόνο. Ιδανικό για εξερεύνηση των δυνατοτήτων του server και πειραματισμό με διαφορετικές εισόδους.

Μπορείτε να δείτε την πλήρη υλοποίηση στο [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Εκτέλεση του Client

Για να τρέξετε τις αυτοματοποιημένες δοκιμές (αυτό θα ξεκινήσει αυτόματα και τον server):

```bash
python client.py
```

Ή τρέξτε σε διαδραστική λειτουργία:

```bash
python client.py --interactive
```

### Δοκιμές με Διάφορες Μεθόδους

Υπάρχουν πολλοί τρόποι να δοκιμάσετε και να αλληλεπιδράσετε με τα εργαλεία που παρέχει ο server, ανάλογα με τις ανάγκες και τη ροή εργασίας σας.

#### Δημιουργία Προσαρμοσμένων Script Δοκιμών με το MCP Python SDK
Μπορείτε επίσης να φτιάξετε τα δικά σας script δοκιμών χρησιμοποιώντας το MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Σε αυτό το πλαίσιο, ένα "script δοκιμής" σημαίνει ένα προσαρμοσμένο πρόγραμμα Python που γράφετε για να λειτουργεί ως client του MCP server. Αντί να είναι μια επίσημη μονάδα δοκιμής, αυτό το script σας επιτρέπει να συνδεθείτε προγραμματιστικά στον server, να καλέσετε οποιοδήποτε από τα εργαλεία του με παραμέτρους της επιλογής σας και να ελέγξετε τα αποτελέσματα. Αυτή η προσέγγιση είναι χρήσιμη για:
- Πρωτοτυποποίηση και πειραματισμό με κλήσεις εργαλείων
- Επαλήθευση της απόκρισης του server σε διαφορετικές εισόδους
- Αυτοματοποίηση επαναλαμβανόμενων κλήσεων εργαλείων
- Δημιουργία δικών σας ροών εργασίας ή ενσωματώσεων πάνω από τον MCP server

Μπορείτε να χρησιμοποιήσετε τα script δοκιμών για να δοκιμάσετε γρήγορα νέα ερωτήματα, να εντοπίσετε σφάλματα στη συμπεριφορά εργαλείων ή ακόμα και ως αφετηρία για πιο προηγμένη αυτοματοποίηση. Παρακάτω είναι ένα παράδειγμα χρήσης του MCP Python SDK για τη δημιουργία τέτοιου script:

## Περιγραφές Εργαλείων

Μπορείτε να χρησιμοποιήσετε τα παρακάτω εργαλεία που παρέχει ο server για να εκτελέσετε διαφορετικούς τύπους αναζητήσεων και ερωτημάτων. Κάθε εργαλείο περιγράφεται παρακάτω με τις παραμέτρους και παραδείγματα χρήσης.

Αυτή η ενότητα παρέχει λεπτομέρειες για κάθε διαθέσιμο εργαλείο και τις παραμέτρους του.

### general_search

Εκτελεί γενική αναζήτηση στο διαδίκτυο και επιστρέφει μορφοποιημένα αποτελέσματα.

**Πώς να καλέσετε αυτό το εργαλείο:**

Μπορείτε να καλέσετε το `general_search` από το δικό σας script χρησιμοποιώντας το MCP Python SDK, ή διαδραστικά μέσω του Inspector ή της διαδραστικής λειτουργίας του client. Ακολουθεί παράδειγμα κώδικα με το SDK:

# [Παράδειγμα Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Εναλλακτικά, σε διαδραστική λειτουργία, επιλέξτε `general_search` από το μενού και εισάγετε το ερώτημά σας όταν σας ζητηθεί.

**Παράμετροι:**
- `query` (string): Το ερώτημα αναζήτησης

**Παράδειγμα Αιτήματος:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Αναζητά πρόσφατα άρθρα ειδήσεων σχετικά με ένα ερώτημα.

**Πώς να καλέσετε αυτό το εργαλείο:**

Μπορείτε να καλέσετε το `news_search` από το δικό σας script χρησιμοποιώντας το MCP Python SDK, ή διαδραστικά μέσω του Inspector ή της διαδραστικής λειτουργίας του client. Ακολουθεί παράδειγμα κώδικα με το SDK:

# [Παράδειγμα Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Εναλλακτικά, σε διαδραστική λειτουργία, επιλέξτε `news_search` από το μενού και εισάγετε το ερώτημά σας όταν σας ζητηθεί.

**Παράμετροι:**
- `query` (string): Το ερώτημα αναζήτησης

**Παράδειγμα Αιτήματος:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Αναζητά προϊόντα που ταιριάζουν με ένα ερώτημα.

**Πώς να καλέσετε αυτό το εργαλείο:**

Μπορείτε να καλέσετε το `product_search` από το δικό σας script χρησιμοποιώντας το MCP Python SDK, ή διαδραστικά μέσω του Inspector ή της διαδραστικής λειτουργίας του client. Ακολουθεί παράδειγμα κώδικα με το SDK:

# [Παράδειγμα Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Εναλλακτικά, σε διαδραστική λειτουργία, επιλέξτε `product_search` από το μενού και εισάγετε το ερώτημά σας όταν σας ζητηθεί.

**Παράμετροι:**
- `query` (string): Το ερώτημα αναζήτησης προϊόντων

**Παράδειγμα Αιτήματος:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Παίρνει άμεσες απαντήσεις σε ερωτήσεις από μηχανές αναζήτησης.

**Πώς να καλέσετε αυτό το εργαλείο:**

Μπορείτε να καλέσετε το `qna` από το δικό σας script χρησιμοποιώντας το MCP Python SDK, ή διαδραστικά μέσω του Inspector ή της διαδραστικής λειτουργίας του client. Ακολουθεί παράδειγμα κώδικα με το SDK:

# [Παράδειγμα Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Εναλλακτικά, σε διαδραστική λειτουργία, επιλέξτε `qna` από το μενού και εισάγετε την ερώτησή σας όταν σας ζητηθεί.

**Παράμετροι:**
- `question` (string): Η ερώτηση για την οποία θέλετε απάντηση

**Παράδειγμα Αιτήματος:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Λεπτομέρειες Κώδικα

Αυτή η ενότητα παρέχει αποσπάσματα κώδικα και αναφορές για τις υλοποιήσεις του server και του client.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Δείτε τα αρχεία [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) και [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) για πλήρεις λεπτομέρειες υλοποίησης.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Προχωρημένες Έννοιες σε Αυτό το Μάθημα

Πριν ξεκινήσετε την κατασκευή, εδώ είναι μερικές σημαντικές προχωρημένες έννοιες που θα εμφανιστούν σε όλο το κεφάλαιο. Η κατανόησή τους θα σας βοηθήσει να ακολουθήσετε, ακόμα κι αν είναι καινούργιες για εσάς:

- **Συντονισμός Πολλαπλών Εργαλείων**: Αυτό σημαίνει ότι τρέχετε διάφορα εργαλεία (όπως αναζήτηση web, ειδήσεις, προϊόντα και Q&A) μέσα σε έναν μόνο MCP server. Επιτρέπει στον server σας να χειρίζεται ποικίλες εργασίες, όχι μόνο μία.
- **Διαχείριση Ορίων Ρυθμού API**: Πολλά εξωτερικά APIs (όπως το SerpAPI) περιορίζουν πόσα αιτήματα μπορείτε να κάνετε σε συγκεκριμένο χρόνο. Ο καλός κώδικας ελέγχει αυτά τα όρια και τα διαχειρίζεται ομαλά, ώστε η εφαρμογή σας να μην σπάει αν φτάσετε σε όριο.
- **Ανάλυση Δομημένων Δεδομένων**: Οι απαντήσεις API είναι συχνά πολύπλοκες και εμφωλευμένες. Αυτή η έννοια αφορά τη μετατροπή αυτών των απαντήσεων σε καθαρές, εύχρηστες μορφές που είναι φιλικές προς LLM ή άλλα προγράμματα.
- **Ανάκτηση από Σφάλματα**: Μερικές φορές κάτι πάει στραβά — ίσως η σύνδεση αποτύχει ή το API δεν επιστρέψει αυτό που περιμένετε. Η ανάκτηση από σφάλματα σημαίνει ότι ο κώδικάς σας μπορεί να χειριστεί αυτά τα προβλήματα και να δώσει χρήσιμη ανατροφοδότηση, αντί να καταρρεύσει.
- **Επικύρωση Παραμέτρων**: Αυτό αφορά τον έλεγχο ότι όλες οι είσοδοι στα εργαλεία σας είναι σωστές και ασφαλείς για χρήση. Περιλαμβάνει τον ορισμό προεπιλεγμένων τιμών και την επιβεβαίωση των τύπων, που βοηθά στην αποφυγή σφαλμάτων και σύγχυσης.

Αυτή η ενότητα θα σας βοηθήσει να διαγνώσετε και να επιλύσετε κοινά προβλήματα που μπορεί να συναντήσετε κατά την εργασία με τον Web Search MCP Server. Αν αντιμετωπίσετε σφάλματα ή απρόβλεπτη συμπεριφορά, αυτή η ενότητα αντιμετώπισης προβλημάτων παρέχει λύσεις στα πιο συνηθισμένα ζητήματα. Ανατρέξτε σε αυτές τις συμβουλές πριν ζητήσετε περαιτέρω βοήθεια — συχνά επιλύουν γρήγορα τα προβλήματα.

## Αντιμετώπιση Προβλημάτων

Κατά την εργασία με τον Web Search MCP Server, μπορεί περιστασιακά να αντιμετωπίσετε προβλήματα — αυτό είναι φυσιολογικό όταν αναπτύσσετε με εξωτερικά APIs και νέα εργαλεία. Αυτή η ενότητα παρέχει πρακτικές λύσεις στα πιο κοινά προβλήματα, ώστε να επιστρέψετε γρήγορα σε ομαλή λειτουργία. Αν συναντήσετε σφάλμα, ξεκινήστε από εδώ: οι παρακάτω συμβουλές καλύπτουν τα ζητήματα που αντιμετωπίζουν οι περισσότεροι χρήστες και συχνά επιλύουν το πρόβλημά σας χωρίς επιπλέον βοήθεια.

### Συνηθισμένα Προβλήματα

Παρακάτω είναι μερ
Για να ενεργοποιήσετε τη λειτουργία DEBUG, ορίστε το επίπεδο καταγραφής σε DEBUG στην κορυφή του `client.py` ή `server.py` σας:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Τι ακολουθεί

- [5.10 Ροή σε Πραγματικό Χρόνο](../mcp-realtimestreaming/README.md)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.