# Διακομιστής MCP με stdio Μεταφορά

> **⚠️ Σημαντική Ενημέρωση**: Από την Προδιαγραφή MCP 2025-06-18, η αυτόνομη μεταφορά SSE (Server-Sent Events) έχει **αποσυρθεί** και αντικαταστάθηκε από τη μεταφορά "Streamable HTTP". Η τρέχουσα προδιαγραφή MCP ορίζει δύο κύριους μηχανισμούς μεταφοράς:
> 1. **stdio** - Πρότυπη είσοδος/έξοδος (συνιστάται για τοπικούς διακομιστές)
> 2. **Streamable HTTP** - Για απομακρυσμένους διακομιστές που μπορεί να χρησιμοποιούν εσωτερικά SSE
>
> Αυτό το μάθημα έχει ενημερωθεί για να επικεντρωθεί στη **stdio μεταφορά**, που είναι η συνιστώμενη προσέγγιση για τις περισσότερες υλοποιήσεις διακομιστών MCP.

Η μεταφορά stdio επιτρέπει στους διακομιστές MCP να επικοινωνούν με τους πελάτες μέσω των ροών πρότυπης εισόδου και εξόδου. Αυτή είναι η πιο κοινά χρησιμοποιούμενη και συνιστώμενη μέθοδος μεταφοράς στην τρέχουσα προδιαγραφή MCP, παρέχοντας έναν απλό και αποδοτικό τρόπο για την κατασκευή διακομιστών MCP που μπορούν εύκολα να ενσωματωθούν με διάφορες πελατειακές εφαρμογές.

## Επισκόπηση

Αυτό το μάθημα καλύπτει το πώς να δημιουργήσετε και να καταναλώσετε Διακομιστές MCP χρησιμοποιώντας τη μεταφορά stdio.

## Στόχοι Μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Δημιουργήσετε έναν Διακομιστή MCP χρησιμοποιώντας τη μεταφορά stdio.
- Εντοπίσετε σφάλματα σε έναν Διακομιστή MCP χρησιμοποιώντας τον Inspector.
- Καταναλώσετε έναν Διακομιστή MCP χρησιμοποιώντας το Visual Studio Code.
- Κατανοήσετε τους τρέχοντες μηχανισμούς μεταφοράς MCP και γιατί η stdio είναι η συνιστώμενη.

## Μεταφορά stdio - Πώς λειτουργεί

Η μεταφορά stdio είναι ένας από τους δύο υποστηριζόμενους τύπους μεταφοράς στην τρέχουσα προδιαγραφή MCP (2025-06-18). Έτσι λειτουργεί:

- **Απλή Επικοινωνία**: Ο διακομιστής διαβάζει μηνύματα JSON-RPC από την πρότυπη είσοδο (`stdin`) και στέλνει μηνύματα στην πρότυπη έξοδο (`stdout`).
- **Βασισμένη σε Διαδικασία**: Ο πελάτης εκκινεί τον διακομιστή MCP ως υποδιαδικασία.
- **Μορφή Μηνυμάτων**: Τα μηνύματα είναι μεμονωμένα αιτήματα JSON-RPC, ειδοποιήσεις ή απαντήσεις, διαχωρισμένα με αλλαγές γραμμής.
- **Καταγραφή**: Ο διακομιστής ΜΠΟΡΕΙ να γράφει συμβολοσειρές UTF-8 στη τυπική σφάλμα (`stderr`) για σκοπούς καταγραφής.

### Κύριες Απαιτήσεις:
- Τα μηνύματα ΠΡΕΠΕΙ να διαχωρίζονται με αλλαγές γραμμής και ΔΕΝ ΠΡΕΠΕΙ να περιέχουν ενσωματωμένες αλλαγές γραμμής
- Ο διακομιστής ΔΕΝ ΠΡΕΠΕΙ να γράφει τίποτα στο `stdout` που να μην είναι έγκυρο μήνυμα MCP
- Ο πελάτης ΔΕΝ ΠΡΕΠΕΙ να γράφει τίποτα στο `stdin` του διακομιστή που να μην είναι έγκυρο μήνυμα MCP

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Στον προηγούμενο κώδικα:

- Εισάγουμε την κλάση `Server` και τον `StdioServerTransport` από το MCP SDK
- Δημιουργούμε ένα παράδειγμα διακομιστή με βασική διαμόρφωση και δυνατότητες
- Δημιουργούμε ένα παράδειγμα `StdioServerTransport` και συνδέουμε τον διακομιστή σε αυτό, ενεργοποιώντας την επικοινωνία μέσω stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Δημιουργήστε μια παρουσία εξυπηρετητή
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Στον προηγούμενο κώδικα:

- Δημιουργούμε ένα παράδειγμα διακομιστή χρησιμοποιώντας το MCP SDK
- Ορίζουμε εργαλεία χρησιμοποιώντας διακοσμητές
- Χρησιμοποιούμε τον context manager stdio_server για τη διαχείριση της μεταφοράς

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Η βασική διαφορά από το SSE είναι ότι οι διακομιστές stdio:

- Δεν απαιτούν ρύθμιση web server ή HTTP endpoints
- Εκκινούνται ως υποδιαδικασίες από τον πελάτη
- Επικοινωνούν μέσω των ροών stdin/stdout
- Είναι πιο απλοί στην υλοποίηση και αποσφαλμάτωση

## Άσκηση: Δημιουργώντας έναν stdio Διακομιστή

Για να δημιουργήσουμε τον διακομιστή μας, πρέπει να έχουμε υπόψη δύο πράγματα:

- Χρειαζόμαστε να χρησιμοποιήσουμε web server για να εκθέσουμε endpoints για σύνδεση και μηνύματα.

## Εργαστήριο: Δημιουργία απλού MCP stdio διακομιστή

Σε αυτό το εργαστήριο, θα δημιουργήσουμε έναν απλό διακομιστή MCP χρησιμοποιώντας τη συνιστώμενη μεταφορά stdio. Ο διακομιστής αυτός θα εκθέτει εργαλεία που οι πελάτες μπορούν να καλέσουν χρησιμοποιώντας το πρότυπο Model Context Protocol.

### Προαπαιτούμενα

- Python 3.8 ή νεότερη έκδοση
- MCP Python SDK: `pip install mcp`
- Βασική κατανόηση ασύγχρονου προγραμματισμού

Ας ξεκινήσουμε δημιουργώντας τον πρώτο μας MCP stdio διακομιστή:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Διαμορφώστε την καταγραφή
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Δημιουργήστε τον διακομιστή
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Χρησιμοποιήστε τη μεταφορά stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


## Κύριες διαφορές από την αποσυρθείσα μέθοδο SSE

**Μεταφορά Stdio (Τρέχον Πρότυπο):**
- Απλό μοντέλο υποδιαδικασιών - ο πελάτης εκκινεί τον διακομιστή ως υποδιαδικασία
- Επικοινωνία μέσω stdin/stdout με μηνύματα JSON-RPC
- Δεν απαιτείται ρύθμιση HTTP server
- Καλύτερη απόδοση και ασφάλεια
- Ευκολότερη αποσφαλμάτωση και ανάπτυξη

**Μεταφορά SSE (Αποσυρθείσα από MCP 2025-06-18):**
- Απαίτηση HTTP server με SSE endpoints
- Πιο περίπλοκη ρύθμιση με υποδομή web server
- Επιπλέον ζητήματα ασφάλειας για HTTP endpoints
- Τώρα αντικαταστάθηκε από Streamable HTTP για σενάρια βασισμένα στον ιστό

### Δημιουργώντας διακομιστή με μεταφορά stdio

Για να δημιουργήσουμε τον stdio διακομιστή μας, πρέπει να:

1. **Εισάγουμε τις απαραίτητες βιβλιοθήκες** - Χρειαζόμαστε τα στοιχεία διακομιστή MCP και τη μεταφορά stdio
2. **Δημιουργήσουμε ένα παράδειγμα διακομιστή** - Ορίζουμε τον διακομιστή με τις δυνατότητές του
3. **Ορίσουμε εργαλεία** - Προσθέτουμε τη λειτουργικότητα που θέλουμε να εκθέσουμε
4. **Ρυθμίσουμε τη μεταφορά** - Διαμορφώνουμε την επικοινωνία stdio
5. **Τρέξουμε τον διακομιστή** - Ξεκινάμε τον διακομιστή και διαχειριζόμαστε τα μηνύματα

Ας το χτίσουμε βήμα-βήμα:

### Βήμα 1: Δημιουργία βασικού stdio διακομιστή

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Διαμόρφωση καταγραφής
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Δημιουργήστε τον διακομιστή
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


### Βήμα 2: Προσθήκη περισσότερων εργαλείων

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```


### Βήμα 3: Εκτέλεση του διακομιστή

Αποθηκεύστε τον κώδικα ως `server.py` και τρέξτε τον από τη γραμμή εντολών:

```bash
python server.py
```

Ο διακομιστής θα ξεκινήσει και θα περιμένει εισόδους από το stdin. Επικοινωνεί χρησιμοποιώντας μηνύματα JSON-RPC πάνω στη μεταφορά stdio.

### Βήμα 4: Δοκιμή με τον Inspector

Μπορείτε να δοκιμάσετε τον διακομιστή σας χρησιμοποιώντας τον MCP Inspector:

1. Εγκαταστήστε τον Inspector: `npx @modelcontextprotocol/inspector`
2. Τρέξτε τον Inspector και δείξτε τον στον διακομιστή σας
3. Δοκιμάστε τα εργαλεία που έχετε δημιουργήσει

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Αποσφαλμάτωση του stdio διακομιστή σας

### Χρήση του MCP Inspector

Ο MCP Inspector είναι ένα πολύτιμο εργαλείο για την αποσφαλμάτωση και δοκιμή διακομιστών MCP. Δείτε πώς να τον χρησιμοποιήσετε με τον stdio διακομιστή σας:

1. **Εγκαταστήστε τον Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Τρέξτε τον Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Δοκιμάστε τον διακομιστή σας**: Ο Inspector παρέχει διεπαφή web όπου μπορείτε να:
   - Δείτε τις δυνατότητες του διακομιστή
   - Δοκιμάσετε εργαλεία με διαφορετικές παραμέτρους
   - Παρακολουθήσετε μηνύματα JSON-RPC
   - Αποσφαλματώσετε προβλήματα σύνδεσης

### Χρήση του VS Code

Μπορείτε επίσης να αποσφαλματώσετε τον διακομιστή MCP απευθείας στο VS Code:

1. Δημιουργήστε μια διαμόρφωση εκκίνησης στο `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Ορίστε σημεία διακοπής στον κώδικά σας
3. Τρέξτε τον αποσφαλματωτή και δοκιμάστε με τον Inspector

### Συμβουλές αποσφαλμάτωσης

- Χρησιμοποιήστε το `stderr` για καταγραφή - μην γράφετε ποτέ στο `stdout` καθώς προορίζεται για μηνύματα MCP
- Διασφαλίστε ότι όλα τα μηνύματα JSON-RPC διαχωρίζονται με νέα γραμμή
- Δοκιμάστε πρώτα με απλά εργαλεία πριν προσθέσετε πολύπλοκη λειτουργικότητα
- Χρησιμοποιήστε τον Inspector για να επιβεβαιώσετε τη μορφοποίηση των μηνυμάτων

## Κατανάλωση του stdio διακομιστή σας στο VS Code

Μόλις κατασκευάσετε τον MCP stdio διακομιστή σας, μπορείτε να τον ενσωματώσετε με το VS Code για να το χρησιμοποιήσετε με Claude ή άλλους πελάτες συμβατούς με MCP.

### Διαμόρφωση

1. **Δημιουργήστε ένα αρχείο ρυθμίσεων MCP** στο `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ή `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Επανεκκινήστε τον Claude**: Κλείστε και ανοίξτε ξανά τον Claude για να φορτωθεί η νέα ρύθμιση διακομιστή.

3. **Δοκιμάστε τη σύνδεση**: Ξεκινήστε μια συνομιλία με τον Claude και δοκιμάστε να χρησιμοποιήσετε τα εργαλεία του διακομιστή σας:
   - "Μπορείς να μου χαιρετήσεις χρησιμοποιώντας το εργαλείο χαιρετισμού;"
   - "Υπολόγισε το άθροισμα του 15 και 27"
   - "Ποια είναι οι πληροφορίες του διακομιστή;"

### Παράδειγμα stdio διακομιστή TypeScript

Ακολουθεί ένα ολοκληρωμένο παράδειγμα σε TypeScript για αναφορά:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Προσθήκη εργαλείων
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```


### Παράδειγμα stdio διακομιστή .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```


## Περίληψη

Σε αυτό το ενημερωμένο μάθημα, μάθατε πώς να:

- Δημιουργείτε διακομιστές MCP χρησιμοποιώντας την τρέχουσα **stdio μεταφορά** (συνιστώμενη μέθοδος)
- Κατανοείτε γιατί η μεταφορά SSE αποσύρθηκε υπέρ της stdio και Streamable HTTP
- Δημιουργείτε εργαλεία που μπορούν να κληθούν από πελάτες MCP
- Αποσφαλματώνετε τον διακομιστή σας χρησιμοποιώντας τον MCP Inspector
- Ενσωματώνετε τον stdio διακομιστή σας με VS Code και Claude

Η μεταφορά stdio παρέχει έναν απλούστερο, πιο ασφαλή και πιο αποδοτικό τρόπο για την κατασκευή διακομιστών MCP σε σύγκριση με την αποσυρθείσα προσέγγιση SSE. Είναι η συνιστώμενη μεταφορά για τις περισσότερες υλοποιήσεις διακομιστών MCP από την προδιαγραφή 2025-06-18.

### .NET

1. Ας δημιουργήσουμε πρώτα κάποια εργαλεία, για αυτό θα δημιουργήσουμε ένα αρχείο *Tools.cs* με το ακόλουθο περιεχόμενο:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## Άσκηση: Δοκιμή του stdio διακομιστή σας

Τώρα που έχετε δημιουργήσει τον διακομιστή stdio, ας τον δοκιμάσουμε για να βεβαιωθούμε ότι λειτουργεί σωστά.

### Προαπαιτούμενα

1. Βεβαιωθείτε ότι έχετε εγκαταστήσει τον MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ο κώδικας του διακομιστή σας θα πρέπει να είναι αποθηκευμένος (π.χ., ως `server.py`)

### Δοκιμή με τον Inspector

1. **Ξεκινήστε τον Inspector με τον διακομιστή σας**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Ανοίξτε τη διεπαφή web**: Ο Inspector θα ανοίξει ένα παράθυρο προγράμματος περιήγησης που εμφανίζει τις δυνατότητες του διακομιστή σας.

3. **Δοκιμάστε τα εργαλεία**: 
   - Δοκιμάστε το εργαλείο `get_greeting` με διαφορετικά ονόματα
   - Δοκιμάστε το εργαλείο `calculate_sum` με διάφορους αριθμούς
   - Καλέστε το εργαλείο `get_server_info` για να δείτε μεταδεδομένα διακομιστή

4. **Παρακολουθήστε την επικοινωνία**: Ο Inspector δείχνει τα μηνύματα JSON-RPC που ανταλλάσσονται μεταξύ πελάτη και διακομιστή.

### Τι θα δείτε

Όταν ο διακομιστής σας ξεκινά σωστά, θα δείτε:
- Καταγεγραμμένες δυνατότητες διακομιστή στον Inspector
- Διαθέσιμα εργαλεία για δοκιμή
- Επιτυχείς ανταλλαγές μηνυμάτων JSON-RPC
- Απαντήσεις εργαλείων εμφανισμένες στη διεπαφή

### Συνηθισμένα προβλήματα και λύσεις

**Ο διακομιστής δεν ξεκινά:**
- Ελέγξτε ότι όλες οι εξαρτήσεις είναι εγκατεστημένες: `pip install mcp`
- Επικυρώστε τη σύνταξη και την εσοχή του Python κώδικα
- Αναζητήστε μηνύματα σφάλματος στην κονσόλα

**Εργαλεία δεν εμφανίζονται:**
- Βεβαιωθείτε ότι οι διακοσμητές `@server.tool()` υπάρχουν
- Ελέγξτε ότι οι συναρτήσεις εργαλείων ορίζονται πριν από το `main()`
- Επιβεβαιώστε ότι ο διακομιστής έχει ρυθμιστεί σωστά

**Προβλήματα σύνδεσης:**
- Βεβαιωθείτε ότι ο διακομιστής χρησιμοποιεί σωστά τη μεταφορά stdio
- Ελέγξτε ότι δεν παρεμβαίνουν άλλες διαδικασίες
- Επιβεβαιώστε τη σύνταξη της εντολής του Inspector

## Ανάθεση

Δοκιμάστε να επεκτείνετε τον διακομιστή σας με περισσότερες δυνατότητες. Δείτε [αυτή τη σελίδα](https://api.chucknorris.io/) για παράδειγμα, προκειμένου να προσθέσετε ένα εργαλείο που καλεί ένα API. Εσείς αποφασίζετε πώς πρέπει να φαίνεται ο διακομιστής. Καλή διασκέδαση :)

## Λύση

[Λύση](./solution/README.md) Εδώ υπάρχει μια πιθανή λύση με λειτουργικό κώδικα.

## Κύρια Σημεία

Τα βασικά σημεία αυτού του κεφαλαίου είναι τα εξής:

- Η μεταφορά stdio είναι ο συνιστώμενος μηχανισμός για τοπικούς διακομιστές MCP.
- Η μεταφορά stdio επιτρέπει απρόσκοπτη επικοινωνία μεταξύ διακομιστών MCP και πελατών χρησιμοποιώντας τις ροές πρότυπης εισόδου και εξόδου.
- Μπορείτε να χρησιμοποιήσετε τόσο τον Inspector όσο και το Visual Studio Code για να καταναλώσετε απευθείας τους stdio διακομιστές, καθιστώντας την αποσφαλμάτωση και την ενσωμάτωση άμεσες.

## Παραδείγματα

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Πρόσθετοι Πόροι

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Τι Ακολουθεί

## Επόμενα Βήματα

Τώρα που μάθατε πώς να δημιουργείτε διακομιστές MCP με τη μεταφορά stdio, μπορείτε να εξερευνήσετε πιο προχωρημένα θέματα:

- **Επόμενο**: [HTTP Streaming με MCP (Streamable HTTP)](../06-http-streaming/README.md) - Μάθετε για τον άλλο υποστηριζόμενο μηχανισμό μεταφοράς για απομακρυσμένους διακομιστές
- **Προχωρημένο**: [Καλές Πρακτικές Ασφαλείας MCP](../../02-Security/README.md) - Εφαρμόστε ασφάλεια στους διακομιστές MCP σας
- **Παραγωγή**: [Στρατηγικές Ανάπτυξης](../09-deployment/README.md) - Αναπτύξτε τους διακομιστές σας για παραγωγική χρήση

## Πρόσθετοι Πόροι

- [Προδιαγραφή MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Επίσημη προδιαγραφή
- [Τεκμηρίωση MCP SDK](https://github.com/modelcontextprotocol/sdk) - Αναφορές SDK για όλες τις γλώσσες
- [Παραδείγματα Κοινότητας](../../06-CommunityContributions/README.md) - Περισσότερα παραδείγματα διακομιστών από την κοινότητα

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρερμηνείες ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->