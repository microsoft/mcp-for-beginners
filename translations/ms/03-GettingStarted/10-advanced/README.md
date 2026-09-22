# Penggunaan pelayan lanjutan

Terdapat dua jenis pelayan yang berbeza yang didedahkan dalam MCP SDK, pelayan biasa anda dan pelayan tahap rendah. Biasanya, anda akan menggunakan pelayan biasa untuk menambah ciri kepadanya. Namun untuk beberapa kes, anda ingin bergantung pada pelayan tahap rendah seperti:

- Senibina yang lebih baik. Adalah mungkin untuk mencipta senibina yang bersih dengan kedua-dua pelayan biasa dan pelayan tahap rendah tetapi boleh diperdebatkan bahawa ia sedikit lebih mudah dengan pelayan tahap rendah.
- Ketersediaan ciri. Sesetengah ciri lanjutan hanya boleh digunakan dengan
    pelayan tahap rendah. Bab-bab kemudian membincangkan Elicitation dan ciri Sampling warisan,
    yang telah dihentikan dalam MCP `2026-07-28`.

## Pelayan biasa vs pelayan tahap rendah

Berikut adalah bagaimana penciptaan Pelayan MCP kelihatan dengan pelayan biasa

**Python**

```python
mcp = FastMCP("Demo")

# Tambahkan alat penambahan
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

// Tambah alat penambahan
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

Intinya adalah anda secara eksplisit menambah setiap alat, sumber atau prompt yang anda mahu pelayan miliki. Tiada apa yang salah dengan itu.  

### Pendekatan pelayan tahap rendah

Namun, apabila anda menggunakan pendekatan pelayan tahap rendah anda perlu berfikir dengan cara yang berbeza. Daripada mendaftar setiap alat, anda sebaliknya mencipta dua pengendali bagi setiap jenis ciri (alat, sumber atau prompt). Jadi sebagai contoh alat hanya mempunyai dua fungsi seperti berikut:

- Menyenaraikan semua alat. Satu fungsi akan bertanggungjawab untuk semua percubaan untuk menyenaraikan alat.
- mengendalikan panggilan semua alat. Di sini juga, hanya ada satu fungsi yang mengendalikan panggilan kepada alat

Kedengarannya mungkin kerja yang kurang kan? Jadi daripada mendaftar alat, saya hanya perlu pastikan alat disenaraikan apabila saya menyenaraikan semua alat dan ia dipanggil apabila ada permintaan masuk untuk memanggil alat. 

Mari kita lihat bagaimana kod kini kelihatan:

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
  // Kembalikan senarai alat yang berdaftar
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

Di sini kita kini mempunyai fungsi yang mengembalikan senarai ciri. Setiap entri dalam senarai alat kini mempunyai medan seperti `name`, `description` dan `inputSchema` untuk mematuhi jenis pulangan. Ini membolehkan kita meletakkan alat dan definisi ciri kita di tempat lain. Kita kini boleh mencipta semua alat dalam folder alat dan begitu juga untuk semua ciri anda supaya projek anda tiba-tiba boleh disusun seperti berikut:

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

Bagus, senibina kita boleh dibuat kelihatan sangat bersih.

Bagaimana pula dengan memanggil alat, adakah ia idea yang sama juga, satu pengendali untuk memanggil alat, mana-mana alat? Ya, tepat, berikut adalah kod untuk itu:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools adalah sebuah kamus dengan nama alat sebagai kunci
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
    // TODO panggil alat tersebut,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Seperti yang anda boleh lihat dari kod di atas, kita perlu mengurai alat untuk dipanggil, dan dengan hujah apa, dan kemudian kita perlu meneruskan memanggil alat itu.

## Memperbaiki pendekatan dengan pengesahan

Setakat ini, anda telah melihat bagaimana semua pendaftaran anda untuk menambah alat, sumber dan prompt boleh digantikan dengan dua pengendali ini bagi setiap jenis ciri. Apa lagi yang perlu kita lakukan? Baiklah, kita sepatutnya menambah beberapa bentuk pengesahan untuk memastikan bahawa alat dipanggil dengan hujah yang betul. Setiap runtime mempunyai penyelesaian mereka sendiri untuk ini, sebagai contoh Python menggunakan Pydantic dan TypeScript menggunakan Zod. Idea adalah kita melakukan yang berikut:

- Pindahkan logik untuk mencipta ciri (alat, sumber atau prompt) ke folder khususnya.
- Tambah cara untuk mengesahkan permintaan masuk yang meminta sebagai contoh memanggil alat.

### Mencipta ciri

Untuk mencipta ciri, kita perlu mencipta fail untuk ciri itu dan pastikan ia mempunyai medan wajib yang diperlukan oleh ciri itu. Medan yang berbeza sedikit antara alat, sumber dan prompt.

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
        # Sahkan input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambah Pydantic, supaya kita boleh membuat AddInputModel dan sahkan args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

di sini anda boleh melihat bagaimana kita melakukan yang berikut:

- Cipta skema menggunakan Pydantic `AddInputModel` dengan medan `a` dan `b` dalam fail *schema.py*.
- Cuba uraikan permintaan masuk menjadi jenis `AddInputModel`, jika terdapat ketidakpadanan parameter ini akan menyebabkan kerosakan:

   ```python
   # add.py
    try:
        # Sahkan input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Anda boleh memilih sama ada untuk meletakkan logik penguraian ini dalam panggilan alat itu sendiri atau dalam fungsi pengendali.

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

- Dalam pengendali yang mengendalikan semua panggilan alat, kita kini cuba mengurai permintaan masuk ke dalam skema alat yang telah didefinisikan:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika itu berjaya maka kita teruskan untuk memanggil alat sebenar:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang anda boleh lihat, pendekatan ini mencipta satu senibina yang bagus kerana segala-galanya ada tempatnya, *server.ts* adalah fail yang sangat kecil yang hanya menyambungkan pengendali permintaan dan setiap ciri berada dalam folder masing-masing iaitu tools/, resources/ atau /prompts.

Bagus, mari kita cuba bina ini seterusnya. 

## Latihan: Mencipta pelayan tahap rendah

Dalam latihan ini, kita akan melakukan yang berikut:

1. Cipta pelayan tahap rendah yang mengendalikan penyenaraian alat dan pemanggilan alat.
1. Laksanakan satu senibina yang boleh anda bina di atasnya.
1. Tambah pengesahan untuk memastikan panggilan alat anda disahkan dengan betul.

### -1- Cipta senibina

Perkara pertama yang perlu kita atasi ialah satu senibina yang membantu kita membangun apabila kita menambah lebih banyak ciri, berikut adalah rupa bentuknya:

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

Kini kita telah menyusun satu senibina yang memastikan kita boleh dengan mudah menambah alat baru di dalam folder alat. Sila ikut cara ini untuk menambah subdirektori untuk sumber dan prompt juga.

### -2- Mencipta alat

Mari kita lihat bagaimana mencipta alat seterusnya. Pertama, ia perlu dicipta dalam subdirektori *tool* seperti berikut:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Sahkan input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambah Pydantic, supaya kita boleh buat AddInputModel dan sahkan args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Apa yang kita lihat di sini adalah bagaimana kita mentakrifkan nama, keterangan, dan skema input menggunakan Pydantic dan pengendali yang akan dipanggil apabila alat ini dipanggil. Akhir sekali, kita dedahkan `tool_add` yang merupakan kamus yang memegang semua sifat ini.

Terdapat juga *schema.py* yang digunakan untuk mentakrifkan skema input yang digunakan oleh alat kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori alat dianggap sebagai modul. Tambahan pula, kita perlu dedahkan modul di dalamnya seperti berikut:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita boleh terus menambah pada fail ini apabila kita menambah lebih banyak alat.

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

Di sini kita mencipta satu kamus yang mengandungi sifat:

- name, ini adalah nama alat.
- rawSchema, ini adalah skema Zod, ia akan digunakan untuk mengesahkan permintaan masuk untuk memanggil alat ini.
- inputSchema, skema ini akan digunakan oleh pengendali.
- callback, ini digunakan untuk memanggil alat.

Terdapat juga `Tool` yang digunakan untuk menukar kamus ini kepada jenis yang boleh diterima oleh pengendali pelayan mcp dan ia kelihatan seperti berikut:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan terdapat *schema.ts* di mana kita menyimpan skema input bagi setiap alat yang kelihatan seperti berikut dengan hanya satu skema buat masa ini tetapi apabila kita menambah alat kita boleh menambah lebih banyak entri:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Bagus, mari kita teruskan untuk mengendalikan penyenaraian alat kita seterusnya.

### -3- Mengendalikan penyenaraian alat

Seterusnya, untuk mengendalikan penyenaraian alat kita, kita perlu menetapkan pengendali permintaan untuk itu. Berikut adalah apa yang perlu kita tambah ke fail pelayan:

**Python**

```python
# kod dibuang untuk ringkasan
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

Di sini, kita tambah decorator `@server.list_tools` dan fungsi pelaksanaan `handle_list_tools`. Dalam fungsi terakhir, kita perlu menghasilkan satu senarai alat. Perhatikan bagaimana setiap alat perlu mempunyai nama, keterangan dan inputSchema.   

**TypeScript**

Untuk menetapkan pengendali permintaan bagi penyenaraian alat, kita perlu memanggil `setRequestHandler` pada pelayan dengan skema yang sesuai dengan apa yang kita cuba lakukan, dalam kes ini `ListToolsRequestSchema`. 

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
// kod disingkatkan
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Pulangkan senarai alat yang didaftarkan
  return {
    tools: tools
  };
});
```

Bagus, kini kita telah menyelesaikan bahagian menyenaraikan alat, mari kita lihat bagaimana kita boleh memanggil alat seterusnya.

### -4- Mengendalikan pemanggilan alat

Untuk memanggil alat, kita perlu menetapkan satu lagi pengendali permintaan, kali ini fokus kepada mengendalikan permintaan yang menyatakan ciri mana yang perlu dipanggil dan dengan hujah apa.

**Python**

Mari kita gunakan decorator `@server.call_tool` dan laksanakan dengan fungsi seperti `handle_call_tool`. Dalam fungsi itu, kita perlu mengurai nama alat, hujahnya dan pastikan hujah itu sah untuk alat tersebut. Kita boleh sama ada mengesahkan hujah dalam fungsi ini atau di bawah dalam alat sebenar.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ialah kamus dengan nama alat sebagai kekunci
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # sambungkan alat
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Berikut adalah apa yang berlaku:

- Nama alat kita sudah ada sebagai parameter input `name` yang juga betul untuk hujah kita dalam bentuk kamus `arguments`.

- Alat dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Pengesahan hujah berlaku dalam sifat `handler` yang menunjuk ke fungsi, jika gagal ia akan menaikkan pengecualian. 

Nah, kini kita mempunyai pemahaman penuh tentang cara menyenaraikan dan memanggil alat menggunakan pelayan tahap rendah.

Lihat [contoh penuh](./code/README.md) di sini

## Tugasan

Luaskan kod yang telah diberikan kepada anda dengan beberapa alat, sumber dan prompt dan renungkan bagaimana anda menyedari bahawa anda hanya perlu menambah fail dalam direktori alat dan tiada tempat lain. 

*Tiada penyelesaian diberikan*

## Ringkasan

Dalam bab ini, kita melihat bagaimana pendekatan pelayan tahap rendah berfungsi dan bagaimana itu boleh membantu kita mencipta satu senibina yang baik untuk kita terus bina. Kita juga membincangkan pengesahan dan anda ditunjukkan bagaimana untuk bekerja dengan perpustakaan pengesahan untuk mencipta skema bagi pengesahan input.

## Seterusnya

- Seterusnya: [Pengesahan Mudah](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->