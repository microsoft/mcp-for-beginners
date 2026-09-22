# Προχωρημένη χρήση διακομιστή

Υπάρχουν δύο διαφορετικοί τύποι διακομιστών που εκτίθενται στο MCP SDK, ο κανονικός διακομιστής και ο χαμηλού επιπέδου διακομιστής. Κανονικά, θα χρησιμοποιούσατε τον κανονικό διακομιστή για να προσθέσετε λειτουργίες σε αυτόν. Σε κάποιες περιπτώσεις όμως, θέλετε να βασιστείτε στον χαμηλού επιπέδου διακομιστή όπως:

- Καλύτερη αρχιτεκτονική. Είναι δυνατόν να δημιουργηθεί μια καθαρή αρχιτεκτονική με τον κανονικό διακομιστή και τον χαμηλού επιπέδου διακομιστή αλλά μπορεί να υποστηριχθεί ότι είναι λίγο πιο εύκολο με χαμηλού επιπέδου διακομιστή.
- Διαθεσιμότητα λειτουργιών. Κάποιες προχωρημένες λειτουργίες μπορούν να χρησιμοποιηθούν μόνο με έναν
    χαμηλού επιπέδου διακομιστή. Τα επόμενα κεφάλαια καλύπτουν την Εξαγωγή και τη λειτουργία Sampling παλαιού τύπου,
    η οποία έχει αποσυρθεί στο MCP `2026-07-28`.

## Κανονικός διακομιστής εναντίον χαμηλού επιπέδου διακομιστή

Να πώς φαίνεται η δημιουργία ενός MCP Διακομιστή με τον κανονικό διακομιστή

**Python**

```python
mcp = FastMCP("Demo")

# Προσθήκη ενός εργαλείου πρόσθεσης
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

Το θέμα είναι ότι προσθέτετε ρητά κάθε εργαλείο, πόρο ή προτροπή που θέλετε να έχει ο διακομιστής. Δεν υπάρχει τίποτα κακό με αυτό.  

### Προσέγγιση χαμηλού επιπέδου διακομιστή

Ωστόσο, όταν χρησιμοποιείτε την προσέγγιση χαμηλού επιπέδου διακομιστή πρέπει να το σκεφτείτε διαφορετικά. Αντί να εγγράφετε κάθε εργαλείο, δημιουργείτε δύο χειριστές ανά τύπο λειτουργίας (εργαλεία, πόροι ή προτροπές). Έτσι για παράδειγμα, τα εργαλεία έχουν μόνο δύο συναρτήσεις ως εξής:

- Λίστα όλων των εργαλείων. Μια συνάρτηση θα είναι υπεύθυνη για όλες τις προσπάθειες να παραθέσει εργαλεία.
- Χειρισμός κλήσης όλων των εργαλείων. Εδώ επίσης, υπάρχει μόνο μία συνάρτηση που χειρίζεται κλήσεις σε ένα εργαλείο

Ακούγεται σαν ενδεχομένως λιγότερη δουλειά, έτσι δεν είναι; Έτσι αντί να εγγράψω ένα εργαλείο, απλά πρέπει να βεβαιωθώ ότι το εργαλείο αναφέρεται όταν παραθέτω όλα τα εργαλεία και ότι καλείται όταν υπάρχει εισερχόμενο αίτημα για κλήση εργαλείου. 

Ας ρίξουμε μια ματιά πώς φαίνεται τώρα ο κώδικας:

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
  // Επιστρέψτε τη λίστα των καταχωρημένων εργαλείων
  return {
    tools: [{
        name: "add",
        description: "Add two numbers",
        inputSchema: {
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

Εδώ τώρα έχουμε μια συνάρτηση που επιστρέφει μια λίστα λειτουργιών. Κάθε καταχώρηση στη λίστα εργαλείων έχει πεδία όπως `name`, `description` και `inputSchema` για να τηρεί τον τύπο επιστροφής. Αυτό μας επιτρέπει να τοποθετήσουμε τα εργαλεία και τον ορισμό λειτουργίας κάπου αλλού. Τώρα μπορούμε να δημιουργήσουμε όλα μας τα εργαλεία σε ένα φάκελο tools και το ίδιο ισχύει και για όλες τις λειτουργίες σας, ώστε το έργο σας να οργανωθεί ξαφνικά ως εξής:

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

Αυτό είναι υπέροχο, η αρχιτεκτονική μας μπορεί να γίνει αρκετά καθαρή.

Τι γίνεται με την κλήση εργαλείων, η ιδέα είναι η ίδια, ένας χειριστής να καλέσει ένα εργαλείο, όποιο κι αν είναι; Ναι, ακριβώς, να ο κώδικας για αυτό:

**Python**

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

Όπως βλέπετε από τον παραπάνω κώδικα, πρέπει να αναλύσουμε ποιο εργαλείο να καλέσουμε, και με ποια ορίσματα, και στη συνέχεια προχωρούμε στην κλήση του εργαλείου.

## Βελτίωση της προσέγγισης με επικύρωση

Μέχρι τώρα, είδατε πώς όλες οι εγγραφές σας για την προσθήκη εργαλείων, πόρων και προτροπών μπορούν να αντικατασταθούν με αυτούς τους δύο χειριστές ανά τύπο λειτουργίας. Τι άλλο πρέπει να κάνουμε; Λοιπόν, πρέπει να προσθέσουμε κάποια μορφή επικύρωσης για να διασφαλίσουμε ότι το εργαλείο καλείται με τα σωστά επιχειρήματα. Κάθε περιβάλλον εκτέλεσης έχει τη δική του λύση για αυτό, για παράδειγμα η Python χρησιμοποιεί τον Pydantic και η TypeScript χρησιμοποιεί τον Zod. Η ιδέα είναι να κάνουμε τα εξής:

- Μεταφορά της λογικής δημιουργίας μιας λειτουργίας (εργαλείο, πόρος ή προτροπή) στον αφιερωμένο φάκελό της.
- Προσθήκη τρόπου για επικύρωση ενός εισερχόμενου αιτήματος που ζητά για παράδειγμα να καλέσει ένα εργαλείο.

### Δημιουργία λειτουργίας

Για να δημιουργήσουμε μια λειτουργία, θα χρειαστεί να δημιουργήσουμε ένα αρχείο για αυτή τη λειτουργία και να βεβαιωθούμε ότι έχει τα υποχρεωτικά πεδία που απαιτούνται από αυτή τη λειτουργία. Ποια πεδία διαφέρουν λίγο ανάμεσα σε εργαλεία, πόρους και προτροπές.

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
        # Επικυρώστε την είσοδο χρησιμοποιώντας μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: προσθήκη Pydantic, ώστε να μπορούμε να δημιουργήσουμε ένα AddInputModel και να επικυρώσουμε τα επιχειρήματα

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

εδώ μπορείτε να δείτε πώς κάνουμε τα εξής:

- Δημιουργούμε ένα σχήμα χρησιμοποιώντας τον Pydantic `AddInputModel` με πεδία `a` και `b` στο αρχείο *schema.py*.
- Προσπαθούμε να αναλύσουμε το εισερχόμενο αίτημα ώστε να είναι του τύπου `AddInputModel`, αν υπάρχει ασυμφωνία στα παραμέτρων αυτό θα προκαλέσει σφάλμα:

   ```python
   # add.py
    try:
        # Επαληθεύστε την είσοδο χρησιμοποιώντας το μοντέλο Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Μπορείτε να επιλέξετε αν θα τοποθετήσετε αυτή τη λογική ανάλυσης στην ίδια την κλήση του εργαλείου ή στη συνάρτηση χειρισμού.

**TypeScript**

```typescript
// διακομιστής.ts
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

// σχήμα.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// πρόσθεσε.ts
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

- Στον χειριστή που διαχειρίζεται όλες τις κλήσεις εργαλείων, τώρα προσπαθούμε να αναλύσουμε το εισερχόμενο αίτημα στο ορισμένο σχήμα του εργαλείου:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    αν αυτό λειτουργήσει τότε προχωρούμε στην κλήση του πραγματικού εργαλείου:

    ```typescript
    const result = await tool.callback(input);
    ```

Όπως βλέπετε, αυτή η προσέγγιση δημιουργεί μια εξαιρετική αρχιτεκτονική καθώς όλα έχουν τη θέση τους, το *server.ts* είναι ένα πολύ μικρό αρχείο που απλώς συνδέει τους χειριστές αιτημάτων και κάθε λειτουργία βρίσκεται στον αντίστοιχο φάκελό της π.χ. tools/, resources/ ή /prompts.

Υπέροχα, ας προσπαθήσουμε να το χτίσουμε αυτό στη συνέχεια. 

## Άσκηση: Δημιουργία χαμηλού επιπέδου διακομιστή

Σε αυτή την άσκηση, θα κάνουμε τα εξής:

1. Δημιουργία χαμηλού επιπέδου διακομιστή που διαχειρίζεται την καταγραφή και την κλήση εργαλείων.
1. Υλοποίηση μιας αρχιτεκτονικής πάνω στην οποία μπορείτε να οικοδομήσετε.
1. Προσθήκη επικύρωσης για να διασφαλίσετε ότι οι κλήσεις εργαλείων σας επικυρώνονται σωστά.

### -1- Δημιουργία αρχιτεκτονικής

Το πρώτο που πρέπει να επιλύσουμε είναι μια αρχιτεκτονική που μας βοηθά να κλιμακώσουμε καθώς προσθέτουμε περισσότερες λειτουργίες, να πώς φαίνεται:

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

Τώρα έχουμε ρυθμίσει μια αρχιτεκτονική που διασφαλίζει ότι μπορούμε εύκολα να προσθέσουμε νέα εργαλεία σε ένα φάκελο tools. Μη διστάσετε να ακολουθήσετε αυτή για να προσθέσετε υποφακέλους για πόρους και προτροπές.

### -2- Δημιουργία εργαλείου

Ας δούμε πώς είναι η δημιουργία ενός εργαλείου στη συνέχεια. Πρώτα, πρέπει να δημιουργηθεί στον υποφάκελο *tool* ως εξής:

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

Αυτό που βλέπουμε εδώ είναι πώς ορίζουμε το όνομα, την περιγραφή και το σχήμα εισόδου χρησιμοποιώντας τον Pydantic και έναν χειριστή που θα καλείται μόλις κληθεί αυτό το εργαλείο. Τέλος, εκθέτουμε το `tool_add` που είναι ένα λεξικό που κρατά όλες αυτές τις ιδιότητες.

Υπάρχει επίσης το *schema.py* που χρησιμοποιείται για να ορίσει το σχήμα εισόδου που χρησιμοποιεί το εργαλείο μας:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Πρέπει επίσης να συμπληρώσουμε το *__init__.py* για να εξασφαλίσουμε ότι ο φάκελος tools αντιμετωπίζεται ως module. Επιπλέον, πρέπει να εκθέσουμε τα modules μέσα σε αυτόν ως εξής:

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

- όνομα, είναι το όνομα του εργαλείου.
- rawSchema, είναι το σχήμα Zod, θα χρησιμοποιηθεί για την επικύρωση εισερχόμενων αιτημάτων για την κλήση αυτού του εργαλείου.
- inputSchema, αυτό το σχήμα θα χρησιμοποιηθεί από τον χειριστή.
- callback, αυτό χρησιμοποιείται για να καλέσει το εργαλείο.

Υπάρχει επίσης το `Tool` που χρησιμοποιείται για να μετατρέψει αυτό το λεξικό σε έναν τύπο που ο χειριστής του mcp server μπορεί να δεχτεί και έχει ως εξής:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Και υπάρχει το *schema.ts* όπου αποθηκεύουμε τα σχήματα εισόδου για κάθε εργαλείο που φαίνεται ως εξής με μόνο ένα σχήμα προς το παρόν αλλά καθώς προσθέτουμε εργαλεία μπορούμε να προσθέσουμε και άλλες καταχωρήσεις:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Υπέροχα, ας προχωρήσουμε στη διαχείριση της καταγραφής των εργαλείων μας στη συνέχεια.

### -3- Διαχείριση καταγραφής εργαλείων

Στη συνέχεια, για να χειριστούμε την καταγραφή των εργαλείων μας, πρέπει να ρυθμίσουμε έναν χειριστή αιτήσεων γι' αυτό. Να τι πρέπει να προσθέσουμε στο αρχείο του διακομιστή μας:

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

Εδώ, προσθέτουμε το διακοσμητή `@server.list_tools` και τη συνάρτηση υλοποίησης `handle_list_tools`. Σε αυτήν, πρέπει να παράγουμε μια λίστα εργαλείων. Σημειώστε πως κάθε εργαλείο πρέπει να έχει όνομα, περιγραφή και inputSchema.   

**TypeScript**

Για να ρυθμίσουμε τον χειριστή αιτήσεων για την καταγραφή εργαλείων, πρέπει να καλέσουμε το `setRequestHandler` στον διακομιστή με ένα σχήμα που ταιριάζει σε αυτό που προσπαθούμε να κάνουμε, σε αυτή την περίπτωση το `ListToolsRequestSchema`. 

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
// ο κώδικας παραλείπεται για λόγους συντομίας
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Επιστρέψτε τη λίστα με τα καταχωρημένα εργαλεία
  return {
    tools: tools
  };
});
```

Υπέροχα, τώρα λύσαμε το κομμάτι της καταγραφής εργαλείων, ας δούμε πώς θα μπορούσαμε να καλούμε εργαλεία στη συνέχεια.

### -4- Διαχείριση κλήσης εργαλείου

Για να καλέσουμε ένα εργαλείο, πρέπει να ρυθμίσουμε έναν άλλο χειριστή αιτήσεων, αυτή τη φορά εστιασμένο στο να διαχειρίζεται ένα αίτημα που προσδιορίζει ποια λειτουργία να καλέσει και με ποια επιχειρήματα.

**Python**

Ας χρησιμοποιήσουμε το διακοσμητή `@server.call_tool` και να το υλοποιήσουμε με μια συνάρτηση όπως η `handle_call_tool`. Μέσα σε αυτή τη συνάρτηση, πρέπει να αναλύσουμε το όνομα του εργαλείου, το όρισμά του και να βεβαιωθούμε ότι τα επιχειρήματα είναι έγκυρα για το εκάστοτε εργαλείο. Μπορούμε είτε να επικυρώσουμε τα επιχειρήματα σε αυτή τη συνάρτηση είτε κατόπιν στη πραγματική κλήση εργαλείου.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # τα εργαλεία είναι ένα λεξικό με ονόματα εργαλείων ως κλειδιά
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # καλεί το εργαλείο
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Να τι συμβαίνει:

- Το όνομα του εργαλείου υπάρχει ήδη ως η παράμετρος εισόδου `name` όπως και τα επιχειρήματα στη μορφή του λεξικού `arguments`.

- Το εργαλείο καλείται με `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Η επικύρωση των επιχειρημάτων γίνεται στην ιδιότητα `handler` που δείχνει σε μια συνάρτηση, αν αυτό αποτύχει θα προκαλέσει εξαίρεση. 

Έτσι, τώρα έχουμε πλήρη κατανόηση της καταγραφής και κλήσης εργαλείων χρησιμοποιώντας έναν χαμηλού επιπέδου διακομιστή.

Δείτε το [πλήρες παράδειγμα](./code/README.md) εδώ

## Ανάθεση

Επεκτείνετε τον κώδικα που σας δόθηκε με έναν αριθμό εργαλείων, πόρων και προτροπών και σκεφτείτε πώς παρατηρείτε ότι χρειάζεται μόνο να προσθέσετε αρχεία στον φάκελο tools και πουθενά αλλού. 

*Δεν παρέχεται λύση*

## Περίληψη

Σε αυτό το κεφάλαιο, είδαμε πώς λειτουργεί η προσέγγιση χαμηλού επιπέδου διακομιστή και πώς αυτό μπορεί να μας βοηθήσει να δημιουργήσουμε μια ωραία αρχιτεκτονική πάνω στην οποία μπορούμε να συνεχίσουμε να χτίζουμε. Συζητήσαμε επίσης την επικύρωση και σας δείξαμε πώς να δουλέψετε με βιβλιοθήκες επικύρωσης για να δημιουργήσετε σχήματα για την επικύρωση εισόδων.

## Τι έπεται

- Επόμενο: [Απλή Αυθεντικοποίηση](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->