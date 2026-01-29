# Παράδειγμα

Αυτό είναι ένα παράδειγμα Typescript για έναν MCP Server

Έτσι φαίνεται το τμήμα του υπολογιστή:

```typescript
// Define calculator tools for each operation
server.tool(
  "add",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.tool(
  "subtract",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a - b) }]
  })
);

server.tool(
  "multiply",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a * b) }]
  })
);

server.tool(
  "divide",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => {
    if (b === 0) {
      return {
        content: [{ type: "text", text: "Error: Cannot divide by zero" }],
        isError: true
      };
    }
    return {
      content: [{ type: "text", text: String(a / b) }]
    };
  }
);
```

## Εγκατάσταση

Τρέξτε την παρακάτω εντολή:

```bash
npm install
```

## Εκτέλεση

```bash
npm start
```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.