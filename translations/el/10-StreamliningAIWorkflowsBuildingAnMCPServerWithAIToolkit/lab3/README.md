# 🔧 Ενότητα 3: Προχωρημένη Ανάπτυξη MCP με Microsoft Foundry Toolkit

> [!NOTE]
> Οι διευθύνσεις URL του Inspector σε αυτό το εργαστήριο χρησιμοποιούν το παλαιό endpoint `/sse` και στοχεύουν τις
> σταθερές εξαρτήσεις MCP SDK `1.9.3` και Inspector `0.14.0`. Δεν είναι
> τρέχοντα παραδείγματα Streamable HTTP της ημερομηνίας `2026-07-28`.

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Στόχοι Μάθησης

Στο τέλος αυτού του εργαστηρίου, θα μπορείτε να:

- ✅ Δημιουργήσετε προσαρμοσμένους MCP servers χρησιμοποιώντας το Microsoft Foundry Toolkit
- ✅ Ρυθμίσετε και να χρησιμοποιήσετε το πιο πρόσφατο MCP Python SDK (v1.9.3)
- ✅ Ρυθμίσετε και να αξιοποιήσετε το MCP Inspector για εντοπισμό σφαλμάτων
- ✅ Εντοπίσετε σφάλματα σε MCP servers τόσο στο Agent Builder όσο και στο Inspector
- ✅ Κατανοήσετε προχωρημένες ροές εργασίας ανάπτυξης MCP server

## 📋 Προαπαιτούμενα

- Ολοκλήρωση του Εργαστηρίου 2 (Βασικά MCP)
- VS Code με εγκατεστημένη την επέκταση Microsoft Foundry Toolkit
- Περιβάλλον Python 3.10+
- Node.js και npm για τη ρύθμιση του Inspector

## 🏗️ Τι θα Δημιουργήσετε

Σε αυτό το εργαστήριο, θα δημιουργήσετε έναν **Weather MCP Server** που παρουσιάζει:
- Προσαρμοσμένη υλοποίηση MCP server
- Ενσωμάτωση με το Microsoft Foundry Toolkit Agent Builder
- Επαγγελματικές ροές εργασίας εντοπισμού σφαλμάτων
- Τεχνολογίες σύγχρονης χρήσης MCP SDK

---

## 🔧 Επισκόπηση Βασικών Στοιχείων

### 🐍 MCP Python SDK
Το Model Context Protocol Python SDK παρέχει τη βάση για τη δημιουργία προσαρμοσμένων MCP servers. Θα χρησιμοποιήσετε την έκδοση 1.9.3 με ενισχυμένες δυνατότητες εντοπισμού σφαλμάτων.

### 🔍 MCP Inspector
Ένα ισχυρό εργαλείο εντοπισμού σφαλμάτων που παρέχει:
- Παρακολούθηση server σε πραγματικό χρόνο
- Οπτικοποίηση εκτέλεσης εργαλείων
- Επιθεώρηση δικτυακών αιτημάτων/απαντήσεων
- Διαδραστικό περιβάλλον δοκιμών

---

## 📖 Υλοποίηση Βήμα προς Βήμα

### Βήμα 1: Δημιουργία ενός WeatherAgent στο Agent Builder

1. **Εκκινήστε το Agent Builder** στο VS Code μέσω της επέκτασης Microsoft Foundry Toolkit
2. **Δημιουργήστε έναν νέο agent** με την εξής διαμόρφωση:
   - Όνομα Agent: `WeatherAgent`

![Agent Creation](../../../../translated_images/el/Agent.c9c33f6a412b4cde.webp)

### Βήμα 2: Αρχικοποίηση Έργου MCP Server

1. **Πλοηγηθείτε στα Εργαλεία** → **Προσθήκη Εργαλείου** στο Agent Builder
2. **Επιλέξτε "MCP Server"** από τις διαθέσιμες επιλογές
3. **Επιλέξτε "Δημιουργία νέου MCP Server"**
4. **Επιλέξτε το πρότυπο `python-weather`**
5. **Ονομάστε τον server σας:** `weather_mcp`

![Python Template Selection](../../../../translated_images/el/Pythontemplate.9d0a2913c6491500.webp)

### Βήμα 3: Άνοιγμα και Εξέταση του Έργου

1. **Ανοίξτε το δημιουργημένο έργο** στο VS Code
2. **Ελέγξτε τη δομή του έργου:**
   ```
   weather_mcp/
   ├── src/
   │   ├── __init__.py
   │   └── server.py
   ├── inspector/
   │   ├── package.json
   │   └── package-lock.json
   ├── .vscode/
   │   ├── launch.json
   │   └── tasks.json
   ├── pyproject.toml
   └── README.md
   ```

### Βήμα 4: Αναβάθμιση στην Πιο Νεότερη MCP SDK

> **🔍 Γιατί Αναβάθμιση;** Θέλουμε να χρησιμοποιήσουμε την πιο πρόσφατη MCP SDK (v1.9.3) και την υπηρεσία Inspector (0.14.0) για βελτιωμένα χαρακτηριστικά και καλύτερες δυνατότητες εντοπισμού σφαλμάτων.

#### 4α. Ενημέρωση Εξαρτήσεων Python

**Επεξεργαστείτε το `pyproject.toml`:** ενημερώστε [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4β. Ενημέρωση Ρυθμίσεων Inspector

**Επεξεργαστείτε το `inspector/package.json`:** ενημερώστε [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4γ. Ενημέρωση Εξαρτήσεων Inspector

**Επεξεργαστείτε το `inspector/package-lock.json`:** ενημερώστε [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Σημείωση:** Αυτό το αρχείο περιέχει εκτενείς ορισμούς εξαρτήσεων. Παρακάτω παρουσιάζεται η βασική δομή - το πλήρες περιεχόμενο εξασφαλίζει σωστή επίλυση εξαρτήσεων.


> **⚡ Πλήρες Package Lock:** Το πλήρες package-lock.json περιέχει περίπου 3000 γραμμές ορισμών εξαρτήσεων. Το παραπάνω δείχνει τη βασική δομή - χρησιμοποιήστε το παρεχόμενο αρχείο για πλήρη επίλυση εξαρτήσεων.

### Βήμα 5: Ρύθμιση Εντοπισμού Σφαλμάτων στο VS Code

*Σημείωση: Παρακαλείστε να αντιγράψετε το αρχείο στην καθορισμένη διαδρομή για να αντικαταστήσετε το αντίστοιχο τοπικό αρχείο*

#### 5α. Ενημέρωση Διαμόρφωσης Εκκίνησης

**Επεξεργαστείτε το `.vscode/launch.json`:**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Local MCP",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen",
      "postDebugTask": "Terminate All Tasks"
    },
    {
      "name": "Launch Inspector (Edge)",
      "type": "msedge",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Launch Inspector (Chrome)",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    }
  ],
  "compounds": [
    {
      "name": "Debug in Agent Builder",
      "configurations": [
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Open Agent Builder",
    },
    {
      "name": "Debug in Inspector (Edge)",
      "configurations": [
        "Launch Inspector (Edge)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    },
    {
      "name": "Debug in Inspector (Chrome)",
      "configurations": [
        "Launch Inspector (Chrome)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    }
  ]
}
```

**Επεξεργαστείτε το `.vscode/tasks.json`:**

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Server",
      "type": "shell",
      "command": "python -m debugpy --listen 127.0.0.1:5678 src/__init__.py sse",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}",
        "env": {
          "PORT": "3001"
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": ".*",
          "endsPattern": "Application startup complete|running"
        }
      }
    },
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npm run dev:inspector",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}/inspector",
        "env": {
          "CLIENT_PORT": "6274",
          "SERVER_PORT": "6277",
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting MCP inspector",
          "endsPattern": "Proxy server listening on port"
        }
      },
      "dependsOn": [
        "Start MCP Server"
      ]
    },
    {
      "label": "Open Agent Builder",
      "type": "shell",
      "command": "echo ${input:openAgentBuilder}",
      "presentation": {
        "reveal": "never"
      },
      "dependsOn": [
        "Start MCP Server"
      ],
    },
    {
      "label": "Terminate All Tasks",
      "command": "echo ${input:terminate}",
      "type": "shell",
      "problemMatcher": []
    }
  ],
  "inputs": [
    {
      "id": "openAgentBuilder",
      "type": "command",
      "command": "ai-mlstudio.agentBuilder",
      "args": {
        "initialMCPs": [ "local-server-weather_mcp" ],
        "triggeredFrom": "vsc-tasks"
      }
    },
    {
      "id": "terminate",
      "type": "command",
      "command": "workbench.action.tasks.terminate",
      "args": "terminateAll"
    }
  ]
}
```


---

## 🚀 Εκτέλεση και Δοκιμή του MCP Server σας

### Βήμα 6: Εγκατάσταση Εξαρτήσεων

Μετά από τις αλλαγές ρύθμισης, εκτελέστε τις ακόλουθες εντολές:

**Εγκαθιστώντας τις Python εξαρτήσεις:**
```bash
uv sync
```

**Εγκαθιστώντας τις εξαρτήσεις του Inspector:**
```bash
cd inspector
npm install
```

### Βήμα 7: Εντοπισμός Σφαλμάτων με Agent Builder

1. **Πατήστε F5** ή χρησιμοποιήστε τη διαμόρφωση **"Debug in Agent Builder"**
2. **Επιλέξτε την σύνθετη διαμόρφωση** από τον πίνακα εντοπισμού σφαλμάτων
3. **Περιμένετε να ξεκινήσει ο server** και να ανοίξει το Agent Builder
4. **Δοκιμάστε τον weather MCP server σας** με ερωτήματα σε φυσική γλώσσα

Πληκτρολογήστε παρόμοιο prompt

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/el/Result.6ac570f7d2b1d538.webp)

### Βήμα 8: Εντοπισμός Σφαλμάτων με MCP Inspector

1. **Χρησιμοποιήστε τη διαμόρφωση "Debug in Inspector"** (Edge ή Chrome)
2. **Ανοίξτε την διεπαφή του Inspector** στο `http://localhost:6274`
3. **Εξερευνήστε το διαδραστικό περιβάλλον δοκιμών:**
   - Δείτε τα διαθέσιμα εργαλεία
   - Δοκιμάστε την εκτέλεση εργαλείων
   - Παρακολουθήστε δικτυακά αιτήματα
   - Εντοπίστε σφάλματα στις απαντήσεις του server

![MCP Inspector Interface](../../../../translated_images/el/Inspector.5672415cd02fe873.webp)

---

## 🎯 Κύρια Αποτελέσματα Μάθησης

Ολοκληρώνοντας αυτό το εργαστήριο, έχετε:

- [x] **Δημιουργήσει έναν προσαρμοσμένο MCP server** χρησιμοποιώντας πρότυπα Microsoft Foundry Toolkit
- [x] **Αναβαθμίσει στο πιο πρόσφατο MCP SDK** (v1.9.3) για βελτιωμένη λειτουργικότητα
- [x] **Ρυθμίσει επαγγελματικές ροές εργασίας εντοπισμού σφαλμάτων** για Agent Builder και Inspector
- [x] **Εγκαταστήσει το MCP Inspector** για διαδραστικές δοκιμές του server
- [x] **Κατακτήσει τις ρυθμίσεις εντοπισμού σφαλμάτων στο VS Code** για ανάπτυξη MCP

## 🔧 Προχωρημένα Χαρακτηριστικά που Εξερευνήθηκαν

| Χαρακτηριστικό | Περιγραφή | Περίπτωση Χρήσης |
|---------|-------------|----------|
| **MCP Python SDK v1.9.3** | Τελευταία υλοποίηση πρωτοκόλλου | Σύγχρονη ανάπτυξη server |
| **MCP Inspector 0.14.0** | Διαδραστικό εργαλείο εντοπισμού σφαλμάτων | Δοκιμή server σε πραγματικό χρόνο |
| **VS Code Debugging** | Ενσωματωμένο περιβάλλον ανάπτυξης | Επαγγελματική ροή εργασίας εντοπισμού σφαλμάτων |
| **Agent Builder Integration** | Άμεση σύνδεση με Microsoft Foundry Toolkit | Ολοκληρωμένη δοκιμή agent |

## 📚 Πρόσθετοι Πόροι

- [MCP Python SDK Documentation](https://modelcontextprotocol.io/docs/sdk/python)
- [Οδηγός Επέκτασης Microsoft Foundry Toolkit](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [Τεκμηρίωση Εντοπισμού Σφαλμάτων VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [Προδιαγραφή Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Συγχαρητήρια!** Ολοκληρώσατε επιτυχώς το Εργαστήριο 3 και πλέον μπορείτε να δημιουργείτε, να εντοπίζετε σφάλματα και να αναπτύσσετε προσαρμοσμένους MCP servers χρησιμοποιώντας επαγγελματικές ροές εργασίας ανάπτυξης.

### 🔜 Συνέχεια στην Επόμενη Ενότητα

Έτοιμοι να εφαρμόσετε τις δεξιότητές σας στο MCP σε μια πραγματική ροή εργασίας ανάπτυξης; Συνεχίστε στο **[Ενότητα 4: Πρακτική Ανάπτυξη MCP - Προσαρμοσμένος Server Αντιγραφής GitHub](../lab4/README.md)** όπου θα:
- Δημιουργήσετε έναν παραγωγικό MCP server που αυτοματοποιεί τις λειτουργίες του αποθετηρίου GitHub
- Υλοποιήσετε λειτουργικότητα κλωνοποίησης αποθετηρίου GitHub μέσω MCP
- Ενσωματώσετε προσαρμοσμένους MCP servers με το VS Code και το GitHub Copilot Agent Mode
- Δοκιμάσετε και αναπτύξετε προσαρμοσμένους MCP servers σε παραγωγικά περιβάλλοντα
- Μάθετε πρακτική αυτοματοποίηση ροών εργασίας για προγραμματιστές

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->