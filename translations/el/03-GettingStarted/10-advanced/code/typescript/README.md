# Εκτέλεση δείγματος

## Εγκατάσταση εξαρτήσεων

```sh
npm install
```

## Δημιουργία

```sh
npm run build
```

## Εκτέλεση

```sh
npm start
```

Θα πρέπει να δείτε το κείμενο:

```text
Registering tools...
Starting server...
```

Τέλεια, αυτό σημαίνει ότι ξεκινά σωστά.

## Δοκιμή του διακομιστή

Δοκιμάστε τις δυνατότητες με την ακόλουθη εντολή:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

Αυτό θα πρέπει να εκκινήσει τη διαδικτυακή διεπαφή του εργαλείου επιθεώρησης.

### Δοκιμή σε λειτουργία CLI

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

Θα πρέπει να δείτε την ακόλουθη έξοδο:

```json
{
  "tools": [
    {
      "name": "add",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    },
    {
      "name": "subtract",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    }
  ]
}
```

Εκτέλεση εργαλείου:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Θα πρέπει να δείτε μια απάντηση παρόμοια με:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

Δοκιμάστε να ελέγξετε ένα εργαλείο που δεν υπάρχει, όπως το "add2", με αυτήν την εντολή:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

Θα πρέπει τώρα να δείτε αυτό το μήνυμα που δείχνει ότι η επικύρωσή σας λειτουργεί:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

Επίσης, δοκιμάστε να στείλετε μια παράμετρο `c` που θα πρέπει να απορριφθεί από το σχήμα, όπως:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

Θα πρέπει τώρα να δείτε το σφάλμα "μη έγκυρα επιχειρήματα":

```text
{
  "content": [],
  "error": {
    "code": "invalid_arguments",
    "message": "Invalid arguments for tool add: [\n  {\n    \"code\": \"invalid_type\",\n    \"expected\": \"number\",\n    \"received\": \"undefined\",\n    \"path\": [\n      \"b\"\n    ],\n    \"message\": \"Required\"\n  }\n]"
  }
}
```

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.