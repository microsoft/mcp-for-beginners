# Εκτέλεση δείγματος

## Εγκατάσταση εξαρτήσεων

```sh
npm install
```

## Δημιουργία

```sh
npm run build
```

## Δημιουργία tokens

```sh
npm run generate
```

Αυτό δημιουργεί ένα token σε ένα αρχείο *.env*. Ο client θα διαβάσει από αυτό το αρχείο.

## Εκτέλεση κώδικα

Ξεκινήστε τον server με:

```sh
npm start
```

Εκτελέστε τον client, σε ξεχωριστό τερματικό, με:

```sh
npm run client
```

Στο τερματικό του server, θα πρέπει να δείτε μια έξοδο παρόμοια με:

```text
User exists
User has required scopes
Middleware executed
```

και στο τερματικό του client, θα πρέπει να δείτε μια έξοδο παρόμοια με:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Αλλαγή παραμέτρων

Ας βεβαιωθούμε ότι κατανοούμε τα scopes. Εντοπίστε το αρχείο *server.ts* και αυτόν τον κώδικα:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Αυτό δηλώνει ότι το token που περνάει πρέπει να έχει "User.Read". Ας το αλλάξουμε σε "User.Write". Τώρα εκτελέστε `npm run build` και επανεκκινήστε τον server με `npm start`. Θα πρέπει τώρα να δείτε ότι η αυθεντικοποίηση αποτυγχάνει, καθώς δεν έχουμε αυτό το scope (έχουμε User.Read και Admin.Write):

Ο client τώρα λέει

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

και μπορείτε να δείτε στο τερματικό του server ότι λέει:

```text
User exists
```

και ότι δεν προχωράει πέρα από αυτό το σημείο.

Είτε προσθέστε αυτό το scope "User.Write" και εκτελέστε `npm run generate` και επανεκτελέστε τον client, είτε αλλάξτε ξανά τον κώδικα του server.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.