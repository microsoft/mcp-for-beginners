# Εκτέλεση αυτού του παραδείγματος

Συνιστάται να εγκαταστήσετε το `uv`, αλλά δεν είναι απαραίτητο, δείτε τις [οδηγίες](https://docs.astral.sh/uv/#highlights)

## -0- Δημιουργία ενός εικονικού περιβάλλοντος

```bash
python -m venv venv
```

## -1- Ενεργοποίηση του εικονικού περιβάλλοντος

```bash
venv\Scrips\activate
```

## -2- Εγκατάσταση των εξαρτήσεων

```bash
pip install "mcp[cli]"
```

## -3- Εκτέλεση του παραδείγματος


```bash
python client.py
```

Θα πρέπει να δείτε μια έξοδο παρόμοια με:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.