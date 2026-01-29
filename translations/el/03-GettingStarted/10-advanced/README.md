# Προχωρημένη χρήση διακομιστή

Υπάρχουν δύο διαφορετικοί τύποι διακομιστών που εκτίθενται στο MCP SDK: ο κανονικός διακομιστής και ο διακομιστής χαμηλού επιπέδου. Συνήθως, χρησιμοποιείτε τον κανονικό διακομιστή για να προσθέσετε λειτουργίες. Ωστόσο, σε ορισμένες περιπτώσεις, μπορεί να θέλετε να βασιστείτε στον διακομιστή χαμηλού επιπέδου, όπως:

- Καλύτερη αρχιτεκτονική. Είναι δυνατό να δημιουργηθεί μια καθαρή αρχιτεκτονική τόσο με τον κανονικό διακομιστή όσο και με τον διακομιστή χαμηλού επιπέδου, αλλά μπορεί να υποστηριχθεί ότι είναι ελαφρώς πιο εύκολο με τον διακομιστή χαμηλού επιπέδου.
- Διαθεσιμότητα λειτουργιών. Ορισμένες προηγμένες λειτουργίες μπορούν να χρησιμοποιηθούν μόνο με διακομιστή χαμηλού επιπέδου. Θα το δείτε αυτό σε επόμενα κεφάλαια καθώς προσθέτουμε δειγματοληψία και εκμαίευση.

## Κανονικός διακομιστής vs διακομιστής χαμηλού επιπέδου

Ακολουθεί πώς φαίνεται η δημιουργία ενός MCP διακομιστή με τον κανονικό διακομιστή:

**Python**

```python
mcp = FastMCP("Demo")

# Add an addition tool
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

// Add an addition tool
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

Το σημείο εδώ είναι ότι προσθέτετε ρητά κάθε εργαλείο, πόρο ή προτροπή που θέλετε να έχει ο διακομιστής. Δεν υπάρχει τίποτα κακό σε αυτό.

### Προσέγγιση διακομιστή χαμηλού επιπέδου

Ωστόσο, όταν χρησιμοποιείτε την προσέγγιση διακομιστή χαμηλού επιπέδου, πρέπει να σκεφτείτε διαφορετικά, δηλαδή αντί να καταχωρείτε κάθε εργαλείο, δημιουργείτε δύο χειριστές ανά τύπο λειτουργίας (εργαλεία, πόροι ή προτροπές). Για παράδειγμα, για τα εργαλεία υπάρχουν μόνο δύο λειτουργίες όπως:

- Λίστα όλων των εργαλείων. Μια λειτουργία θα είναι υπεύθυνη για όλες τις προσπάθειες καταχώρησης εργαλείων.
- Χειρισμός κλήσεων όλων των εργαλείων. Εδώ επίσης, υπάρχει μόνο μία λειτουργία που χειρίζεται τις κλήσεις σε ένα εργαλείο.

Αυτό ακούγεται σαν λιγότερη δουλειά, σωστά; Έτσι, αντί να καταχωρώ ένα εργαλείο, απλά πρέπει να βεβαιωθώ ότι το εργαλείο περιλαμβάνεται στη λίστα όταν καταχωρώ όλα τα εργαλεία και ότι καλείται όταν υπάρχει εισερχόμενο αίτημα για κλήση εργαλείου.

Ας δούμε πώς φαίνεται τώρα ο κώδικας:

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
                    "a": {"type": "number", "description": "nubmer to add"}, 
                    "b": {"type": "number", "description": "nubmer to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "nubmer to add"}, 
                "b": {"type": "number", "description": "nubmer to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

Εδώ έχουμε τώρα μια λειτουργία που επιστρέφει μια λίστα λειτουργιών. Κάθε καταχώρηση στη λίστα εργαλείων έχει πεδία όπως `name`, `description` και `inputSchema` για να συμμορφώνεται με τον τύπο επιστροφής. Αυτό μας επιτρέπει να τοποθετήσουμε τα εργαλεία και τον ορισμό λειτουργιών μας αλλού. Τώρα μπορούμε να δημιουργήσουμε όλα τα εργαλεία μας σε έναν φάκελο εργαλείων και το ίδιο ισχύει για όλες τις λειτουργίες σας, ώστε το έργο σας να μπορεί ξαφνικά να οργανωθεί ως εξής:

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

Τι γίνεται με την κλήση εργαλείων; Είναι η ίδια ιδέα, ένας χειριστής για την κλήση ενός εργαλείου, οποιοδήποτε εργαλείο; Ναι, ακριβώς, εδώ είναι ο κώδικας για αυτό:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
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
    // TODO call the tool, 

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Όπως βλέπετε από τον παραπάνω κώδικα, πρέπει να αναλύσουμε το εργαλείο που θα κληθεί, με ποια επιχειρήματα, και στη συνέχεια να προχωρήσουμε στην κλήση του εργαλείου.

## Βελτίωση της προσέγγισης με επικύρωση

Μέχρι στιγμής, έχετε δει πώς όλες οι καταχωρήσεις σας για την προσθήκη εργαλείων, πόρων και προτροπών μπορούν να αντικατασταθούν με αυτούς τους δύο χειριστές ανά τύπο λειτουργίας. Τι άλλο πρέπει να κάνουμε; Λοιπόν, θα πρέπει να προσθέσουμε κάποια μορφή επικύρωσης για να διασφαλίσουμε ότι το εργαλείο καλείται με τα σωστά επιχειρήματα. Κάθε περιβάλλον εκτέλεσης έχει τη δική του λύση για αυτό, για παράδειγμα η Python χρησιμοποιεί το Pydantic και η TypeScript χρησιμοποιεί το Zod. Η ιδέα είναι ότι κάνουμε τα εξής:

- Μεταφέρουμε τη λογική για τη δημιουργία μιας λειτουργίας (εργαλείο, πόρος ή προτροπή) στον αντίστοιχο φάκελό της.
- Προσθέτουμε έναν τρόπο επικύρωσης ενός εισερχόμενου αιτήματος που ζητά, για παράδειγμα, την κλήση ενός εργαλείου.

### Δημιουργία λειτουργίας

Για να δημιουργήσουμε μια λειτουργία, θα χρειαστεί να δημιουργήσουμε ένα αρχείο για αυτή τη λειτουργία και να βεβαιωθούμε ότι έχει τα υποχρεωτικά πεδία που απαιτούνται για αυτή τη λειτουργία. Τα πεδία διαφέρουν λίγο μεταξύ εργαλείων, πόρων και προτροπών.

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
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

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

- Δημιουργούμε ένα σχήμα χρησιμοποιώντας το Pydantic `AddInputModel` με πεδία `a` και `b` στο αρχείο *schema.py*.
- Προσπαθούμε να αναλύσουμε το εισερχόμενο αίτημα ώστε να είναι τύπου `AddInputModel`. Αν υπάρχει ασυμφωνία στις παραμέτρους, αυτό θα αποτύχει:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Μπορείτε να επιλέξετε αν θα τοποθετήσετε αυτή τη λογική ανάλυσης στην ίδια την κλήση του εργαλείου ή στη λειτουργία χειριστή.

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

- Στον χειριστή που ασχολείται με όλες τις κλήσεις εργαλείων, προσπαθούμε να αναλύσουμε το εισερχόμενο αίτημα στο καθορισμένο σχήμα του εργαλείου:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Αν αυτό λειτουργήσει, τότε προχωράμε στην κλήση του πραγματικού εργαλείου:

    ```typescript
    const result = await tool.callback(input);
    ```

Όπως βλέπετε, αυτή η προσέγγιση δημιουργεί μια εξαιρετική αρχιτεκτονική, καθώς όλα έχουν τη θέση τους. Το *server.ts* είναι ένα πολύ μικρό αρχείο που απλώς συνδέει τους χειριστές αιτημάτων και κάθε λειτουργία βρίσκεται στον αντίστοιχο φάκελό της, δηλαδή tools/, resources/ ή prompts/.

Υπέροχα, ας προσπαθήσουμε να το υλοποιήσουμε αυτό στη συνέχεια.

## Άσκηση: Δημιουργία διακομιστή χαμηλού επιπέδου

Σε αυτή την άσκηση, θα κάνουμε τα εξής:

1. Δημιουργία διακομιστή χαμηλού επιπέδου που χειρίζεται την καταχώρηση εργαλείων και την κλήση εργαλείων.
1. Υλοποίηση μιας αρχιτεκτονικής που μπορείτε να επεκτείνετε.
1. Προσθήκη επικύρωσης για να διασφαλίσετε ότι οι κλήσεις εργαλείων σας επικυρώνονται σωστά.

### -1- Δημιουργία αρχιτεκτονικής

Το πρώτο πράγμα που πρέπει να αντιμετωπίσουμε είναι μια αρχιτεκτονική που μας βοηθά να επεκταθούμε καθώς προσθέτουμε περισσότερες λειτουργίες. Να πώς φαίνεται:

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

Τώρα έχουμε δημιουργήσει μια αρχιτεκτονική που διασφαλίζει ότι μπορούμε εύκολα να προσθέσουμε νέα εργαλεία σε έναν φάκελο εργαλείων. Μη διστάσετε να ακολουθήσετε αυτό το πρότυπο για να προσθέσετε υποφακέλους για πόρους και προτροπές.

### -2- Δημιουργία εργαλείου

Ας δούμε πώς φαίνεται η δημιουργία ενός εργαλείου. Πρώτα, πρέπει να δημιουργηθεί στον υποφάκελο *tool* όπως:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Αυτό που βλέπουμε εδώ είναι πώς ορίζουμε το όνομα, την περιγραφή, ένα σχήμα εισόδου χρησιμοποιώντας το Pydantic και έναν χειριστή που θα καλείται όταν αυτό το εργαλείο καλείται. Τέλος, εκθέτουμε το `tool_add`, το οποίο είναι ένα λεξικό που περιέχει όλες αυτές τις ιδιότητες.

Υπάρχει επίσης το *schema.py* που χρησιμοποιείται για τον ορισμό του σχήματος εισόδου που χρησιμοποιεί το εργαλείο μας:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Χρειάζεται επίσης να συμπληρώσουμε το *__init__.py* για να διασφαλίσουμε ότι ο φάκελος εργαλείων αντιμετωπίζεται ως module. Επιπλέον, πρέπει να εκθέσουμε τα modules μέσα σε αυτό όπως:

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

- name, το όνομα του εργαλείου.
- rawSchema, το σχήμα Zod, που θα χρησιμοποιηθεί για την επικύρωση εισερχόμενων αιτημάτων.
- inputSchema, το σχήμα που θα χρησιμοποιηθεί από τον χειριστή.
- callback, που χρησιμοποιείται για την κλήση του εργαλείου.

Υπάρχει επίσης το `Tool`, που χρησιμοποιείται για τη μετατροπή αυτού του λεξικού σε τύπο που μπορεί να αποδεχτεί ο χειριστής του MCP διακομιστή και φαίνεται ως εξής:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Υπάρχει επίσης το *schema.ts*, όπου αποθηκεύουμε τα σχήματα εισόδου για κάθε εργαλείο, που φαίνεται ως εξής με μόνο ένα σχήμα προς το παρόν, αλλά καθώς προσθέτουμε εργαλεία μπορούμε να προσθέσουμε περισσότερες καταχωρήσεις:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Υπέροχα, ας προχωρήσουμε στη διαχείριση της καταχώρησης εργαλείων στη συνέχεια.

### -3- Διαχείριση καταχώρησης εργαλείων

Στη συνέχεια, για να διαχειριστούμε την καταχώρηση εργαλείων, πρέπει να ρυθμίσουμε έναν χειριστή αιτημάτων για αυτό. Να τι πρέπει να προσθέσουμε στο αρχείο διακομιστή μας:

**Python**

```python
# code omitted for brevity
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

Εδώ προσθέτουμε τον διακοσμητή `@server.list_tools` και τη λειτουργία υλοποίησης `handle_list_tools`. Στη δεύτερη, πρέπει να παράγουμε μια λίστα εργαλείων. Σημειώστε πώς κάθε εργαλείο πρέπει να έχει όνομα, περιγραφή και inputSchema.

**TypeScript**

Για να ρυθμίσουμε τον χειριστή αιτημάτων για την καταχώρηση εργαλείων, πρέπει να καλέσουμε το `setRequestHandler` στον διακομιστή με ένα σχήμα που ταιριάζει με αυτό που προσπαθούμε να κάνουμε, σε αυτή την περίπτωση το `ListToolsRequestSchema`.

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
// code omitted for brevity
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: tools
  };
});
```

Υπέροχα, τώρα λύσαμε το κομμάτι της καταχώρησης εργαλείων. Ας δούμε πώς θα μπορούσαμε να καλούμε εργαλεία στη συνέχεια.

### -4- Διαχείριση κλήσης εργαλείου

Για να καλέσουμε ένα εργαλείο, πρέπει να ρυθμίσουμε έναν άλλο χειριστή αιτημάτων, αυτή τη φορά εστιασμένο στη διαχείριση ενός αιτήματος που καθορίζει ποια λειτουργία να καλέσει και με ποια επιχειρήματα.

**Python**

Ας χρησιμοποιήσουμε τον διακοσμητή `@server.call_tool` και να τον υλοποιήσουμε με μια λειτουργία όπως `handle_call_tool`. Μέσα σε αυτή τη λειτουργία, πρέπει να αναλύσουμε το όνομα του εργαλείου, τα επιχειρήματά του και να διασφαλίσουμε ότι τα επιχειρήματα είναι έγκυρα για το εργαλείο που αφορά. Μπορούμε είτε να επικυρώσουμε τα επιχειρήματα σε αυτή τη λειτουργία είτε πιο κάτω στην πραγματική λειτουργία του εργαλείου.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invoke the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Αυτό που συμβαίνει εδώ:

- Το όνομα του εργαλείου μας είναι ήδη παρόν ως παράμετρος εισόδου `name`, το ίδιο ισχύει και για τα επιχειρήματα με τη μορφή του λεξικού `arguments`.

- Το εργαλείο καλείται με `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Η επικύρωση των επιχειρημάτων γίνεται στην ιδιότητα `handler`, η οποία δείχνει σε μια λειτουργία. Αν αποτύχει, θα προκαλέσει εξαίρεση.

Εκεί, τώρα έχουμε πλήρη κατανόηση της καταχώρησης και της κλήσης εργαλείων χρησιμοποιώντας έναν διακομιστή χαμηλού επιπέδου.

Δείτε το [πλήρες παράδειγμα](./code/README.md) εδώ.

## Εργασία

Επεκτείνετε τον κώδικα που σας δόθηκε με έναν αριθμό εργαλείων, πόρων και προτροπών και σκεφτείτε πώς παρατηρείτε ότι χρειάζεται μόνο να προσθέσετε αρχεία στον φάκελο εργαλείων και πουθενά αλλού.

*Δεν δίνεται λύση*

## Περίληψη

Σε αυτό το κεφάλαιο, είδαμε πώς λειτουργεί η προσέγγιση διακομιστή χαμηλού επιπέδου και πώς μπορεί να μας βοηθήσει να δημιουργήσουμε μια ωραία αρχιτεκτονική που μπορούμε να συνεχίσουμε να αναπτύσσουμε. Συζητήσαμε επίσης την επικύρωση και σας δείξαμε πώς να εργάζεστε με βιβλιοθήκες επικύρωσης για να δημιουργήσετε σχήματα για την επικύρωση εισόδου.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.