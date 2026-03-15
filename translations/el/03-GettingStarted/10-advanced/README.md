# Προηγμένη χρήση διακομιστή

Υπάρχουν δύο διαφορετικοί τύποι διακομιστών που εκτίθενται στο MCP SDK, ο κανονικός διακομιστής και ο χαμηλού επιπέδου διακομιστής. Κανονικά, θα χρησιμοποιούσατε τον τακτικό διακομιστή για να προσθέσετε λειτουργίες σε αυτόν. Σε ορισμένες περιπτώσεις όμως, θέλετε να βασιστείτε στον διακομιστή χαμηλού επιπέδου όπως:

- Καλύτερη αρχιτεκτονική. Είναι δυνατή η δημιουργία μιας καθαρής αρχιτεκτονικής τόσο με τον κανονικό διακομιστή όσο και με έναν διακομιστή χαμηλού επιπέδου, αλλά μπορεί να ειπωθεί ότι είναι ελαφρώς πιο εύκολο με έναν διακομιστή χαμηλού επιπέδου.
- Διαθεσιμότητα λειτουργιών. Ορισμένες προηγμένες λειτουργίες μπορούν να χρησιμοποιηθούν μόνο με διακομιστή χαμηλού επιπέδου. Θα το δείτε σε μετέπειτα κεφάλαια καθώς προσθέτουμε δειγματοληψία και εlicitación.

## Κανονικός διακομιστής vs διακομιστής χαμηλού επιπέδου

Να πώς μοιάζει η δημιουργία ενός MCP Server με τον κανονικό διακομιστή

**Python**

```python
mcp = FastMCP("Demo")

# Προσθέστε ένα εργαλείο πρόσθεσης
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**TypeScript**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// Προσθέστε ένα εργαλείο πρόσθεσης
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);
```

Το σημείο είναι ότι προσθέτετε ρητά κάθε εργαλείο, πόρο ή προτροπή που θέλετε να έχει ο διακομιστής. Δεν υπάρχει τίποτα κακό σε αυτό.

### Προσέγγιση διακομιστή χαμηλού επιπέδου

Ωστόσο, όταν χρησιμοποιείτε την προσέγγιση διακομιστή χαμηλού επιπέδου, πρέπει να σκεφτείτε διαφορετικά. Αντί να καταχωρίζετε κάθε εργαλείο, δημιουργείτε δύο χειριστές ανά τύπο λειτουργίας (εργαλεία, πόροι ή προτροπές). Για παράδειγμα, τα εργαλεία έχουν μόνο δύο συναρτήσεις ως εξής:

- Καταχώριση όλων των εργαλείων. Μια συνάρτηση θα είναι υπεύθυνη για όλες τις προσπάθειες καταχώρισης εργαλείων.
- Χειρισμός κλήσεων όλων των εργαλείων. Εδώ επίσης, υπάρχει μόνο μία συνάρτηση που χειρίζεται κλήσεις σε ένα εργαλείο.

Ακούγεται σαν λιγότερη δουλειά, σωστά; Έτσι, αντί να καταχωρίσω ένα εργαλείο, απλά χρειάζεται να βεβαιωθώ ότι το εργαλείο αναφέρεται όταν καταχωρώ όλα τα εργαλεία και ότι καλείται όταν υπάρχει αίτημα για κλήση ενός εργαλείου.

Ας δούμε πώς μοιάζει τώρα ο κώδικας:

**Python**

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "number to add"}, 
                    "b": {"type": "number", "description": "number to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Επιστρέψτε τη λίστα των εγγεγραμμένων εργαλείων
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "number to add"}, 
                "b": {"type": "number", "description": "number to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

Εδώ τώρα έχουμε μια συνάρτηση που επιστρέφει μια λίστα λειτουργιών. Κάθε καταχώριση στη λίστα εργαλείων έχει πλέον πεδία όπως `name`, `description` και `inputSchema` για να συμμορφώνεται με τον τύπο επιστροφής. Αυτό μας επιτρέπει να βάλουμε τα εργαλεία και τον ορισμό λειτουργίας αλλού. Μπορούμε τώρα να δημιουργήσουμε όλα τα εργαλεία μας σε έναν φάκελο εργαλείων και το ίδιο ισχύει για όλες τις λειτουργίες σας ώστε το έργο σας να μπορεί ξαφνικά να οργανωθεί ως εξής:

```text
app
--| tools
----| add
----| substract
--| resources
----| products
----| schemas
--| prompts
----| product-description
```

Αυτό είναι υπέροχο, η αρχιτεκτονική μας μπορεί να σχεδιαστεί ώστε να φαίνεται πολύ καθαρή.

Τι γίνεται με τις κλήσεις εργαλείων, ισχύει η ίδια ιδέα, ένας χειριστής για κλήση εργαλείου, όποιο εργαλείο; Ναι, ακριβώς, να ο κώδικας για αυτό:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools είναι ένα λεξικό με τα ονόματα εργαλείων ως κλειδιά
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

**TypeScript**

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if(!tool) {
        return {
            error: {
                code: "tool_not_found",
                message: `Tool ${name} not found.`
            }
       };
    }
    
    // args: request.params.arguments
    // TODO καλέστε το εργαλείο,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Όπως βλέπετε από τον παραπάνω κώδικα, πρέπει να αναλύσουμε ποιο εργαλείο θα κληθεί και με ποια επιχειρήματα, και στη συνέχεια πρέπει να προχωρήσουμε στην κλήση του εργαλείου.

## Βελτίωση της προσέγγισης με επικύρωση

Μέχρι στιγμής, έχετε δει πώς όλες οι καταχωρίσεις για την προσθήκη εργαλείων, πόρων και προτροπών μπορούν να αντικατασταθούν με αυτούς τους δύο χειριστές ανά τύπο λειτουργίας. Τι άλλο πρέπει να κάνουμε; Λοιπόν, θα πρέπει να προσθέσουμε κάποια μορφή επικύρωσης για να διασφαλίσουμε ότι το εργαλείο καλείται με τα σωστά επιχειρήματα. Κάθε runtime έχει τη δική της λύση για αυτό, για παράδειγμα η Python χρησιμοποιεί το Pydantic και η TypeScript χρησιμοποιεί το Zod. Η ιδέα είναι ότι κάνουμε τα εξής:

- Μεταφέρουμε τη λογική δημιουργίας μιας λειτουργίας (εργαλείο, πόρος ή προτροπή) στο αφιερωμένο φάκελό της.
- Προσθέτουμε έναν τρόπο για να επικυρώσουμε ένα εισερχόμενο αίτημα που ζητά π.χ. να καλέσει ένα εργαλείο.

### Δημιουργία λειτουργίας

Για να δημιουργήσουμε μια λειτουργία, θα χρειαστεί να δημιουργήσουμε ένα αρχείο για αυτήν τη λειτουργία και να διασφαλίσουμε ότι έχει τα απαραίτητα πεδία που απαιτούνται από αυτή τη λειτουργία. Τα πεδία διαφέρουν λίγο μεταξύ εργαλείων, πόρων και προτροπών.

**Python**

```python
# schema.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# add.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Επικυρώστε την είσοδο χρησιμοποιώντας το μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: προσθέστε Pydantic, ώστε να μπορούμε να δημιουργήσουμε ένα AddInputModel και να επικυρώσουμε τα επιχειρήματα

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Εδώ μπορείτε να δείτε πώς κάνουμε τα εξής:

- Δημιουργία ενός σχήματος χρησιμοποιώντας το Pydantic `AddInputModel` με πεδία `a` και `b` στο αρχείο *schema.py*.
- Προσπάθεια ανάλυσης του εισερχόμενου αιτήματος ώστε να είναι τύπου `AddInputModel`, αν υπάρχει ασυμφωνία στα παραμέτρους αυτό θα προκαλέσει σφάλμα:

   ```python
   # add.py
    try:
        # Επικύρωση εισόδου χρησιμοποιώντας το μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Μπορείτε να επιλέξετε αν θα βάζετε αυτή τη λογική ανάλυσης μέσα στην ίδια την κλήση εργαλείου ή στη συνάρτηση χειριστή.

**TypeScript**

```typescript
// server.ts
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if (!tool) {
       return {
        error: {
            code: "tool_not_found",
            message: `Tool ${name} not found.`
        }
       };
    }
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);

       // @ts-ignore
       const result = await tool.callback(input);

       return {
          content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
      };
    } catch (error) {
       return {
          error: {
             code: "invalid_arguments",
             message: `Invalid arguments for tool ${name}: ${error instanceof Error ? error.message : String(error)}`
          }
    };
   }

});

// schema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// add.ts
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

- Στον χειριστή που χειρίζεται όλες τις κλήσεις εργαλείων, τώρα προσπαθούμε να αναλύσουμε το εισερχόμενο αίτημα στο ορισμένο σχήμα του εργαλείου:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

  εάν αυτό δουλεύει προχωρούμε να καλέσουμε το πραγματικό εργαλείο:

    ```typescript
    const result = await tool.callback(input);
    ```

Όπως βλέπετε, αυτή η προσέγγιση δημιουργεί μια εξαιρετική αρχιτεκτονική καθώς όλα έχουν τη θέση τους, το *server.ts* είναι ένα πολύ μικρό αρχείο που μόνο συνδέει τους χειριστές αιτημάτων και κάθε λειτουργία είναι στο αντίστοιχο φάκελό της π.χ tools/, resources/ ή /prompts.

Υπέροχα, ας προσπαθήσουμε να το κατασκευάσουμε στη συνέχεια.

## Άσκηση: Δημιουργία διακομιστή χαμηλού επιπέδου

Σε αυτήν την άσκηση, θα κάνουμε τα εξής:

1. Δημιουργία διακομιστή χαμηλού επιπέδου που χειρίζεται την καταχώριση εργαλείων και την κλήση εργαλείων.
1. Υλοποίηση μιας αρχιτεκτονικής πάνω στην οποία μπορείτε να χτίσετε.
1. Προσθήκη επικύρωσης για να διασφαλίσετε ότι οι κλήσεις των εργαλείων σας επικυρώνονται σωστά.

### -1- Δημιουργία αρχιτεκτονικής

Το πρώτο που πρέπει να αντιμετωπίσουμε είναι μια αρχιτεκτονική που μας βοηθά να κλιμακωθούμε όσο προσθέτουμε περισσότερες λειτουργίες, να πώς μοιάζει:

**Python**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**TypeScript**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

Τώρα έχουμε ρυθμίσει μια αρχιτεκτονική που εξασφαλίζει ότι μπορούμε εύκολα να προσθέτουμε νέα εργαλεία σε έναν φάκελο εργαλείων. Μη διστάσετε να το ακολουθήσετε για να προσθέσετε υποφακέλους για πόρους και προτροπές.

### -2- Δημιουργία εργαλείου

Ας δούμε πώς μοιάζει η δημιουργία εργαλείου στη συνέχεια. Πρώτον, πρέπει να δημιουργηθεί στον υποφάκελο *tool* όπως παρακάτω:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Επικυρώστε την είσοδο χρησιμοποιώντας το μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: προσθέστε Pydantic, ώστε να μπορούμε να δημιουργήσουμε ένα AddInputModel και να επικυρώσουμε τα ορίσματα

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Εδώ βλέπουμε πώς ορίζουμε το όνομα, την περιγραφή και το σχήμα εισόδου χρησιμοποιώντας το Pydantic και έναν χειριστή που θα εκτελεστεί μόλις κληθεί αυτό το εργαλείο. Τέλος, εκθέτουμε το `tool_add` που είναι ένα λεξικό που κρατάει όλες αυτές τις ιδιότητες.

Υπάρχει επίσης το *schema.py* που χρησιμοποιείται για να ορίσει το σχήμα εισόδου που χρησιμοποιείται από το εργαλείο μας:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Πρέπει επίσης να ενημερώσουμε το *__init__.py* για να διασφαλίσουμε ότι ο φάκελος εργαλείων συμπεριφέρεται ως module. Επιπλέον, χρειάζεται να εκθέσουμε τα modules μέσα σε αυτό όπως:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Μπορούμε να συνεχίσουμε να προσθέτουμε σε αυτό το αρχείο καθώς προσθέτουμε περισσότερα εργαλεία.

**TypeScript**

```typescript
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

Εδώ δημιουργούμε ένα λεξικό που αποτελείται από ιδιότητες:

- name, αυτό είναι το όνομα του εργαλείου.
- rawSchema, αυτό είναι το Zod σχήμα, θα χρησιμοποιηθεί για την επικύρωση των εισερχόμενων αιτημάτων για κλήση αυτού του εργαλείου.
- inputSchema, αυτό το σχήμα θα χρησιμοποιηθεί από τον χειριστή.
- callback, αυτό χρησιμοποιείται για την κλήση του εργαλείου.

Υπάρχει επίσης το `Tool` που χρησιμοποιείται για να μετατρέπει αυτό το λεξικό σε τύπο που μπορεί να αποδεχτεί ο χειριστής του mcp server και μοιάζει ως εξής:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Και υπάρχει το *schema.ts* όπου αποθηκεύουμε τα σχήματα εισόδου για κάθε εργαλείο που μοιάζει ως εξής προς το παρόν με μόνο ένα σχήμα, αλλά καθώς προσθέτουμε εργαλεία, μπορούμε να προσθέσουμε περισσότερες καταχωρίσεις:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Υπέροχα, ας προχωρήσουμε στη διαχείριση της καταχώρισης εργαλείων στη συνέχεια.

### -3- Διαχείριση καταχώρισης εργαλείων

Έπειτα, για να διαχειριστούμε την καταχώριση των εργαλείων μας, πρέπει να ορίσουμε έναν χειριστή αιτημάτων για αυτό. Να τι πρέπει να προσθέσουμε στο αρχείο του διακομιστή μας:

**Python**

```python
# ο κώδικας παραλείπεται για συντομία
from tools import tools

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    tool_list = []
    print(tools)

    for tool in tools.values():
        tool_list.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=pydantic_to_json(tool["input_schema"]),
            )
        )
    return tool_list
```

Εδώ, προσθέτουμε το διακοσμητή `@server.list_tools` και τη λειτουργία υλοποίησης `handle_list_tools`. Σε αυτήν, πρέπει να δημιουργήσουμε μια λίστα εργαλείων. Σημειώστε πώς κάθε εργαλείο πρέπει να έχει όνομα, περιγραφή και inputSchema.

**TypeScript**

Για να ορίσουμε τον χειριστή αιτημάτων για την καταχώριση εργαλείων, πρέπει να καλέσουμε το `setRequestHandler` στον διακομιστή με ένα σχήμα που ταιριάζει σε αυτό που προσπαθούμε να κάνουμε, σε αυτήν την περίπτωση `ListToolsRequestSchema`.

```typescript
// index.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// server.ts
// ο κώδικας παραλείπεται για συντομία
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Επιστρέψτε τη λίστα των καταχωρημένων εργαλείων
  return {
    tools: tools
  };
});
```

Τέλεια, τώρα λύσαμε το θέμα της καταχώρισης εργαλείων, ας δούμε πώς μπορούμε να καλούμε τα εργαλεία στη συνέχεια.

### -4- Διαχείριση κλήσης εργαλείου

Για να καλέσουμε ένα εργαλείο, πρέπει να ορίσουμε έναν άλλο χειριστή αιτημάτων, αυτή τη φορά εστιασμένο στη διαχείριση ενός αιτήματος που καθορίζει ποια λειτουργία να κληθεί και με ποια επιχειρήματα.

**Python**

Χρησιμοποιούμε τον διακοσμητή `@server.call_tool` και τον υλοποιούμε με μια συνάρτηση όπως η `handle_call_tool`. Μέσα σε αυτήν τη συνάρτηση, πρέπει να αναλύσουμε το όνομα του εργαλείου, τα επιχειρήματά του και να διασφαλίσουμε ότι τα επιχειρήματα είναι έγκυρα για το εργαλείο που αφορά. Μπορούμε είτε να επικυρώνουμε τα επιχειρήματα σε αυτή τη συνάρτηση είτε κατόπιν στην ίδια την κλήση εργαλείου.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools είναι ένα λεξικό με ονόματα εργαλείων ως κλειδιά
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # καλέστε το εργαλείο
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Να τι συμβαίνει:

- Το όνομα του εργαλείου μας είναι ήδη παρόν ως η παράμετρος εισόδου `name`, το ίδιο ισχύει για τα επιχειρήματά μας στη μορφή του λεξικού `arguments`.

- Το εργαλείο καλείται με το `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Η επικύρωση των επιχειρημάτων γίνεται στην ιδιότητα `handler` που δείχνει σε μια συνάρτηση, αν αποτύχει, θα εγείρει εξαίρεση.

Τώρα έχουμε πλήρη κατανόηση της καταχώρισης και κλήσης εργαλείων χρησιμοποιώντας διακομιστή χαμηλού επιπέδου.

Δείτε το [πλήρες παράδειγμα](./code/README.md) εδώ

## Ανάθεση

Επεκτείνετε τον κώδικα που σας δόθηκε με έναν αριθμό εργαλείων, πόρων και προτροπών και σκεφτείτε πώς διαπιστώνετε ότι χρειάζεται μόνο να προσθέσετε αρχεία στον φάκελο εργαλείων και πουθενά αλλού.

*Δεν παρέχεται λύση*

## Περίληψη

Σε αυτό το κεφάλαιο, είδαμε πώς λειτουργούσε η προσέγγιση διακομιστή χαμηλού επιπέδου και πώς αυτό μπορεί να μας βοηθήσει να δημιουργήσουμε μια ωραία αρχιτεκτονική πάνω στην οποία μπορούμε να συνεχίσουμε να χτίζουμε. Συζητήσαμε επίσης την επικύρωση και σας δείξαμε πώς να εργαστείτε με βιβλιοθήκες επικύρωσης για να δημιουργήσετε σχήματα για επικύρωση εισόδων.

## Τι ακολουθεί

- Επόμενο: [Απλή Αυθεντικοποίηση](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Το παρόν έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρ' όλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η εξουσιοδοτημένη πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->