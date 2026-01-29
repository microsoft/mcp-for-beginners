# Penggunaan Server Lanjutan

Ada dua jenis server yang tersedia dalam MCP SDK, yaitu server biasa dan server tingkat rendah. Biasanya, Anda akan menggunakan server biasa untuk menambahkan fitur. Namun, dalam beberapa kasus, Anda mungkin ingin menggunakan server tingkat rendah, seperti:

- Arsitektur yang lebih baik. Meskipun memungkinkan untuk menciptakan arsitektur yang bersih dengan server biasa maupun server tingkat rendah, dapat dikatakan bahwa menggunakan server tingkat rendah sedikit lebih mudah.
- Ketersediaan fitur. Beberapa fitur lanjutan hanya dapat digunakan dengan server tingkat rendah. Anda akan melihat ini di bab-bab berikutnya saat kita menambahkan sampling dan elicitation.

## Server Biasa vs Server Tingkat Rendah

Berikut adalah contoh pembuatan MCP Server menggunakan server biasa:

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

Intinya adalah Anda secara eksplisit menambahkan setiap alat, sumber daya, atau prompt yang ingin dimiliki oleh server. Tidak ada yang salah dengan pendekatan ini.

### Pendekatan Server Tingkat Rendah

Namun, saat menggunakan pendekatan server tingkat rendah, Anda perlu berpikir dengan cara yang berbeda, yaitu alih-alih mendaftarkan setiap alat, Anda cukup membuat dua handler untuk setiap jenis fitur (alat, sumber daya, atau prompt). Misalnya, untuk alat, hanya ada dua fungsi seperti ini:

- Daftar semua alat. Satu fungsi bertanggung jawab untuk semua upaya mendata alat.
- Menangani pemanggilan semua alat. Di sini juga, hanya ada satu fungsi yang menangani pemanggilan alat.

Kedengarannya seperti pekerjaan yang lebih sedikit, bukan? Jadi, alih-alih mendaftarkan alat, saya hanya perlu memastikan alat tersebut terdaftar saat mendata semua alat dan dipanggil saat ada permintaan masuk untuk memanggil alat.

Mari kita lihat bagaimana kode ini terlihat sekarang:

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

Di sini kita memiliki fungsi yang mengembalikan daftar fitur. Setiap entri dalam daftar alat sekarang memiliki field seperti `name`, `description`, dan `inputSchema` untuk memenuhi tipe pengembalian. Ini memungkinkan kita untuk meletakkan definisi alat dan fitur kita di tempat lain. Kita sekarang dapat membuat semua alat kita di folder alat, begitu juga dengan semua fitur lainnya sehingga proyek kita dapat diorganisasi seperti ini:

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

Hebat, arsitektur kita bisa dibuat terlihat cukup bersih.

Bagaimana dengan pemanggilan alat, apakah idenya sama, satu handler untuk memanggil alat, alat mana pun? Ya, persis seperti itu, berikut adalah kode untuk itu:

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

Seperti yang Anda lihat dari kode di atas, kita perlu mem-parsing alat yang akan dipanggil, dengan argumen apa, lalu melanjutkan untuk memanggil alat tersebut.

## Meningkatkan Pendekatan dengan Validasi

Sejauh ini, Anda telah melihat bagaimana semua pendaftaran untuk menambahkan alat, sumber daya, dan prompt dapat digantikan dengan dua handler per jenis fitur. Apa lagi yang perlu kita lakukan? Nah, kita harus menambahkan beberapa bentuk validasi untuk memastikan bahwa alat dipanggil dengan argumen yang benar. Setiap runtime memiliki solusi masing-masing untuk ini, misalnya Python menggunakan Pydantic dan TypeScript menggunakan Zod. Idenya adalah kita melakukan hal berikut:

- Memindahkan logika untuk membuat fitur (alat, sumber daya, atau prompt) ke folder khusus.
- Menambahkan cara untuk memvalidasi permintaan masuk yang meminta, misalnya, memanggil alat.

### Membuat Fitur

Untuk membuat fitur, kita perlu membuat file untuk fitur tersebut dan memastikan file tersebut memiliki field wajib yang diperlukan oleh fitur tersebut. Field yang diperlukan sedikit berbeda antara alat, sumber daya, dan prompt.

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

Di sini Anda dapat melihat bagaimana kita melakukan hal berikut:

- Membuat skema menggunakan Pydantic `AddInputModel` dengan field `a` dan `b` di file *schema.py*.
- Mencoba mem-parsing permintaan masuk agar sesuai dengan tipe `AddInputModel`, jika ada ketidaksesuaian parameter, ini akan gagal:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Anda dapat memilih apakah ingin meletakkan logika parsing ini di pemanggilan alat itu sendiri atau di fungsi handler.

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

- Dalam handler yang menangani semua pemanggilan alat, kita sekarang mencoba mem-parsing permintaan masuk ke dalam skema yang telah didefinisikan oleh alat:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika berhasil, kita melanjutkan untuk memanggil alat yang sebenarnya:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang Anda lihat, pendekatan ini menciptakan arsitektur yang hebat karena semuanya memiliki tempatnya masing-masing, *server.ts* adalah file yang sangat kecil yang hanya menghubungkan handler permintaan, dan setiap fitur berada di folder masing-masing, yaitu tools/, resources/, atau /prompts.

Hebat, mari kita coba membangun ini selanjutnya.

## Latihan: Membuat Server Tingkat Rendah

Dalam latihan ini, kita akan melakukan hal berikut:

1. Membuat server tingkat rendah yang menangani daftar alat dan pemanggilan alat.
1. Menerapkan arsitektur yang dapat Anda kembangkan.
1. Menambahkan validasi untuk memastikan pemanggilan alat Anda divalidasi dengan benar.

### -1- Membuat Arsitektur

Hal pertama yang perlu kita atasi adalah arsitektur yang membantu kita berkembang saat menambahkan lebih banyak fitur, berikut tampilannya:

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

Sekarang kita telah menyiapkan arsitektur yang memastikan kita dapat dengan mudah menambahkan alat baru di folder alat. Anda bebas mengikuti ini untuk menambahkan subdirektori untuk sumber daya dan prompt.

### -2- Membuat Alat

Mari kita lihat bagaimana membuat alat selanjutnya. Pertama, alat tersebut perlu dibuat di subdirektori *tool* seperti ini:

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

Di sini kita melihat bagaimana kita mendefinisikan nama, deskripsi, skema input menggunakan Pydantic, dan handler yang akan dipanggil saat alat ini dipanggil. Terakhir, kita mengekspos `tool_add` yang merupakan dictionary yang berisi semua properti ini.

Ada juga *schema.py* yang digunakan untuk mendefinisikan skema input yang digunakan oleh alat kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori alat diperlakukan sebagai modul. Selain itu, kita perlu mengekspos modul-modul di dalamnya seperti ini:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita dapat terus menambahkan ke file ini saat kita menambahkan lebih banyak alat.

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

Di sini kita membuat dictionary yang terdiri dari properti:

- name, ini adalah nama alat.
- rawSchema, ini adalah skema Zod, yang akan digunakan untuk memvalidasi permintaan masuk untuk memanggil alat ini.
- inputSchema, skema ini akan digunakan oleh handler.
- callback, ini digunakan untuk memanggil alat.

Ada juga `Tool` yang digunakan untuk mengonversi dictionary ini menjadi tipe yang dapat diterima oleh handler server MCP, dan tampilannya seperti ini:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan ada *schema.ts* tempat kita menyimpan skema input untuk setiap alat yang terlihat seperti ini dengan hanya satu skema saat ini, tetapi saat kita menambahkan alat, kita dapat menambahkan lebih banyak entri:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Hebat, mari kita lanjutkan untuk menangani daftar alat kita selanjutnya.

### -3- Menangani Daftar Alat

Selanjutnya, untuk menangani daftar alat kita, kita perlu menyiapkan handler permintaan untuk itu. Berikut adalah apa yang perlu kita tambahkan ke file server kita:

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

Di sini kita menambahkan dekorator `@server.list_tools` dan fungsi implementasi `handle_list_tools`. Dalam fungsi tersebut, kita perlu menghasilkan daftar alat. Perhatikan bagaimana setiap alat perlu memiliki nama, deskripsi, dan inputSchema.

**TypeScript**

Untuk menyiapkan handler permintaan untuk daftar alat, kita perlu memanggil `setRequestHandler` pada server dengan skema yang sesuai dengan apa yang kita coba lakukan, dalam hal ini `ListToolsRequestSchema`.

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

Hebat, sekarang kita telah menyelesaikan bagian daftar alat, mari kita lihat bagaimana kita dapat memanggil alat selanjutnya.

### -4- Menangani Pemanggilan Alat

Untuk memanggil alat, kita perlu menyiapkan handler permintaan lain, kali ini berfokus pada menangani permintaan yang menentukan fitur mana yang akan dipanggil dan dengan argumen apa.

**Python**

Mari kita gunakan dekorator `@server.call_tool` dan mengimplementasikannya dengan fungsi seperti `handle_call_tool`. Dalam fungsi tersebut, kita perlu mem-parsing nama alat, argumennya, dan memastikan argumen tersebut valid untuk alat yang dimaksud. Kita dapat memvalidasi argumen dalam fungsi ini atau di bagian downstream dalam alat yang sebenarnya.

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

Berikut adalah apa yang terjadi:

- Nama alat kita sudah ada sebagai parameter input `name`, yang juga berlaku untuk argumen kita dalam bentuk dictionary `arguments`.

- Alat dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validasi argumen terjadi di properti `handler` yang menunjuk ke fungsi, jika gagal, itu akan menghasilkan exception.

Selesai, sekarang kita memiliki pemahaman penuh tentang daftar dan pemanggilan alat menggunakan server tingkat rendah.

Lihat [contoh lengkap](./code/README.md) di sini.

## Tugas

Perluas kode yang telah diberikan dengan sejumlah alat, sumber daya, dan prompt, lalu refleksikan bagaimana Anda hanya perlu menambahkan file di direktori alat dan tidak di tempat lain.

*Tidak ada solusi yang diberikan*

## Ringkasan

Dalam bab ini, kita melihat bagaimana pendekatan server tingkat rendah bekerja dan bagaimana itu dapat membantu kita menciptakan arsitektur yang baik untuk terus dikembangkan. Kita juga membahas validasi dan Anda diperlihatkan cara bekerja dengan pustaka validasi untuk membuat skema validasi input.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.