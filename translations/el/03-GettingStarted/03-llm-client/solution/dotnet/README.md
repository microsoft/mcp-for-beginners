# Εκτέλεση αυτού του δείγματος

> [!NOTE]
> Αυτό το δείγμα υποθέτει ότι χρησιμοποιείτε ένα περιβάλλον GitHub Codespaces. Αν θέλετε να το εκτελέσετε τοπικά, θα χρειαστεί να δημιουργήσετε ένα προσωπικό access token (PAT) στο GitHub.
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## Εγκατάσταση βιβλιοθηκών

```sh
dotnet restore
```

Πρέπει να εγκατασταθούν οι εξής βιβλιοθήκες: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## Εκτέλεση

```sh 
dotnet run
```

Θα πρέπει να δείτε μια έξοδο παρόμοια με:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

Πολλά από τα αποτελέσματα είναι απλώς για debugging, αλλά το σημαντικό είναι ότι εμφανίζετε εργαλεία από τον MCP Server, τα μετατρέπετε σε εργαλεία LLM και στο τέλος λαμβάνετε μια απάντηση πελάτη MCP "Sum 6".

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.