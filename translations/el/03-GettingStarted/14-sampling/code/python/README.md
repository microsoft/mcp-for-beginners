# Εκτέλεση του δείγματος

> [!WARNING]
> Αυτό το δείγμα χρησιμοποιεί αποσυρμένο Sampling και ένα παλαιότερο endpoint HTTP+SSE. Διατηρείται για συμβατότητα με MCP `2025-11-25`. Οι νέες υλοποιήσεις θα πρέπει να καλούν απευθείας έναν πάροχο LLM και να χρησιμοποιούν Streamable HTTP για απομακρυσμένη κίνηση MCP.
> retained for MCP `2025-11-25` compatibility. New implementations should call
> an LLM provider directly and use Streamable HTTP for remote MCP traffic.

## Δημιουργία εικονικού περιβάλλοντος

```sh
python -m venv venv
source ./venv/bin/activate
```

## Εγκατάσταση εξαρτημάτων

```sh
pip install "mcp[cli]"
```

## Εκτέλεση του διακομιστή

```sh
uvicorn server:app --port 8000
```

## Δοκιμή του διακομιστή με το GitHub Copilot και το VS Code

Προσθέστε την καταχώρηση στο mcp.json ως εξής:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Βεβαιωθείτε ότι πατήσατε "start" στον διακομιστή.

Στο GitHub Copilot επικολλήστε την ακόλουθη προτροπή:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Την πρώτη φορά θα σας ζητηθεί αν θα δεχτείτε μια ενέργεια Sampling, μετά θα σας ζητηθεί να αποδεχτείτε το εργαλείο για να εκτελέσει το "create_blog". Θα πρέπει να δείτε μια απάντηση παρόμοια με:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->