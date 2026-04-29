# Penggunaan server tingkat lanjut

Ada dua jenis server yang tersedia dalam MCP SDK, server biasa dan server tingkat rendah. Biasanya, Anda akan menggunakan server reguler untuk menambahkan fitur. Namun, dalam beberapa kasus, Anda ingin mengandalkan server tingkat rendah seperti:

- Arsitektur yang lebih baik. Mungkin untuk membuat arsitektur yang bersih menggunakan server reguler dan server tingkat rendah, tetapi bisa dikatakan sedikit lebih mudah dengan server tingkat rendah.
- Ketersediaan fitur. Beberapa fitur lanjutan hanya bisa digunakan dengan server tingkat rendah. Anda akan melihat ini di bab-bab berikutnya ketika kita menambahkan sampling dan elicitation.

## Server reguler vs server tingkat rendah

Berikut adalah bagaimana pembuatan Server MCP dengan server reguler

**Python**

```python
mcp = FastMCP("Demo")

# Tambahkan alat penjumlahan
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

// Tambahkan alat penjumlahan
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

Intinya adalah Anda secara eksplisit menambahkan setiap tool, resource, atau prompt yang ingin dimiliki server. Tidak ada yang salah dengan itu.

### Pendekatan server tingkat rendah

Namun, saat Anda menggunakan pendekatan server tingkat rendah, Anda perlu memikirkannya secara berbeda. Alih-alih mendaftarkan setiap tool, Anda membuat dua handler per tipe fitur (tools, resources, atau prompts). Jadi misalnya untuk tools hanya memiliki dua fungsi seperti berikut:

- Mendaftar semua tools. Satu fungsi bertanggung jawab untuk semua upaya listing tools.
- Menangani pemanggilan semua tools. Di sini juga, hanya ada satu fungsi yang menangani panggilan ke sebuah tool.

Kedengarannya seperti mungkin lebih sedikit pekerjaan, bukan? Jadi daripada mendaftarkan sebuah tool, saya hanya perlu memastikan tool itu terdaftar saat saya listing semua tools dan dipanggil saat ada permintaan masuk untuk memanggil sebuah tool.

Mari kita lihat bagaimana kode sekarang terlihat:

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
  // Kembalikan daftar alat yang terdaftar
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

Di sini kita sekarang memiliki sebuah fungsi yang mengembalikan daftar fitur. Setiap entri dalam daftar tools sekarang memiliki field seperti `name`, `description`, dan `inputSchema` untuk sesuai dengan tipe pengembalian. Ini memungkinkan kita untuk menaruh definisi tools dan fitur kita di tempat lain. Kita sekarang bisa membuat semua tools kita dalam folder tools dan hal yang sama berlaku untuk semua fitur Anda sehingga proyek Anda bisa tiba-tiba terorganisir seperti ini:

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

Bagus, arsitektur kita bisa dibuat cukup bersih.

Bagaimana dengan pemanggilan tools, apakah ide yang sama? Satu handler untuk memanggil tool, apapun tool-nya? Ya, tepat sekali, ini kodenya:

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
    // TODO panggil alat,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Seperti yang Anda lihat dari kode di atas, kita perlu mengurai tool yang akan dipanggil, dan argumen apa, lalu kita lanjutkan untuk memanggil tool tersebut.

## Meningkatkan pendekatan dengan validasi

Sejauh ini, Anda sudah melihat bagaimana semua pendaftaran untuk menambahkan tools, resources, dan prompts bisa diganti dengan dua handler ini per tipe fitur. Apa lagi yang perlu kita lakukan? Kita harus menambahkan semacam validasi untuk memastikan tool dipanggil dengan argumen yang benar. Setiap runtime memiliki solusi sendiri untuk ini, misalnya Python menggunakan Pydantic dan TypeScript menggunakan Zod. Idenya adalah kita melakukan hal berikut:

- Pindahkan logika pembuatan fitur (tool, resource atau prompt) ke folder khususnya.
- Tambahkan cara untuk memvalidasi permintaan masuk misalnya untuk memanggil sebuah tool.

### Membuat sebuah fitur

Untuk membuat sebuah fitur, kita perlu membuat file untuk fitur tersebut dan memastikan ia memiliki field wajib yang dibutuhkan fitur itu. Field mana yang diperlukan sedikit berbeda antara tools, resources, dan prompts.

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
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambahkan Pydantic, sehingga kita bisa membuat AddInputModel dan memvalidasi argumen

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

di sini Anda bisa lihat bagaimana kita melakukan hal berikut:

- Membuat schema menggunakan Pydantic `AddInputModel` dengan field `a` dan `b` di file *schema.py*.
- Mencoba mengurai permintaan masuk menjadi tipe `AddInputModel`, jika ada ketidakcocokan parameter maka ini akan gagal:

   ```python
   # add.py
    try:
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Anda bisa memilih apakah logika parsing ini diletakkan di panggilan tool itu sendiri atau di fungsi handler.

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

- Dalam handler yang menangani semua panggilan tool, kita sekarang coba mengurai permintaan masuk menjadi schema yang didefinisikan tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jika berhasil maka lanjut kita panggil tool sebenarnya:

    ```typescript
    const result = await tool.callback(input);
    ```

Seperti yang Anda lihat, pendekatan ini menciptakan arsitektur yang bagus karena semuanya memiliki tempatnya, *server.ts* adalah file yang sangat kecil yang hanya menghubungkan handler permintaan dan setiap fitur ada di foldernya masing-masing yaitu tools/, resources/ atau /prompts.

Bagus, mari kita coba bangun ini berikutnya.

## Latihan: Membuat server tingkat rendah

Dalam latihan ini, kita akan melakukan hal berikut:

1. Membuat server tingkat rendah yang menangani listing tools dan pemanggilan tools.
1. Mengimplementasikan arsitektur yang bisa Anda kembangkan lebih lanjut.
1. Menambahkan validasi untuk memastikan panggilan tool Anda tervalidasi dengan benar.

### -1- Membuat arsitektur

Hal pertama yang perlu kita atasi adalah arsitektur yang membantu skala saat kita menambahkan lebih banyak fitur, ini tampilannya:

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

Sekarang kita sudah menyiapkan arsitektur yang memastikan kita bisa dengan mudah menambahkan tools baru di folder tools. Silakan ikuti ini untuk menambahkan subdirektori untuk resources dan prompts.

### -2- Membuat sebuah tool

Mari kita lihat bagaimana membuat sebuah tool setelah ini. Pertama, tool harus dibuat di subdirektori *tool* seperti ini:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validasi input menggunakan model Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tambahkan Pydantic, sehingga kita dapat membuat AddInputModel dan memvalidasi args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Yang kita lihat di sini adalah bagaimana kita mendefinisikan nama, deskripsi, dan schema input menggunakan Pydantic serta handler yang akan dipanggil saat tool ini dipanggil. Terakhir, kita mengekspos `tool_add` yang adalah dictionary yang memuat semua properti ini.

Ada juga *schema.py* yang digunakan untuk mendefinisikan schema input yang dipakai tool kita:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kita juga perlu mengisi *__init__.py* untuk memastikan direktori tools dikenali sebagai modul. Selain itu, kita perlu mengekspos modul di dalamnya seperti ini:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Kita bisa terus menambah ke file ini saat menambah lebih banyak tools.

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

Di sini kita membuat sebuah dictionary yang terdiri dari properti:

- name, ini adalah nama tool.
- rawSchema, ini adalah schema Zod, akan digunakan untuk memvalidasi permintaan masuk untuk memanggil tool ini.
- inputSchema, schema ini akan digunakan oleh handler.
- callback, ini digunakan untuk memanggil tool.

Ada juga `Tool` yang dipakai untuk mengonversi dictionary ini menjadi tipe yang bisa diterima handler server mcp dan bentuknya seperti ini:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dan ada *schema.ts* yang menyimpan schema input untuk setiap tool yang tampilannya seperti ini dengan hanya satu schema saat ini tapi saat kita menambah tool kita bisa tambah entri lagi:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Bagus, mari lanjut ke menangani listing tools kita berikutnya.

### -3- Menangani listing tools

Berikutnya, untuk menangani listing tools kita, kita perlu menyiapkan handler permintaan untuk itu. Ini yang perlu kita tambahkan ke file server kita:

**Python**

```python
# kode dihilangkan demi singkatnya
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

Di sini, kita menambahkan decorator `@server.list_tools` dan fungsi implementasi `handle_list_tools`. Di fungsi ini, kita harus menghasilkan daftar tools. Perhatikan bagaimana setiap tool harus memiliki nama, deskripsi dan inputSchema.

**TypeScript**

Untuk menyiapkan handler permintaan untuk listing tools, kita perlu memanggil `setRequestHandler` pada server dengan schema yang sesuai dengan apa yang ingin kita lakukan, kali ini `ListToolsRequestSchema`.

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
// kode dihilangkan untuk ringkasan
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Kembalikan daftar alat yang terdaftar
  return {
    tools: tools
  };
});
```

Bagus, sekarang kita sudah menyelesaikan bagian listing tools, mari kita lihat bagaimana kita bisa memanggil tools berikutnya.

### -4- Menangani pemanggilan tool

Untuk memanggil tool, kita perlu menyiapkan handler permintaan lain, kali ini fokus pada menangani permintaan yang menentukan fitur mana dipanggil dan dengan argumen apa.

**Python**

Mari gunakan decorator `@server.call_tool` dan implementasi dengan fungsi seperti `handle_call_tool`. Di dalam fungsi itu, kita perlu mengurai nama tool, argumennya dan memastikan argumen valid untuk tool tersebut. Kita bisa memvalidasi argumen di fungsi ini atau di dalam tool yang sebenarnya.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools adalah kamus dengan nama alat sebagai kunci
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # panggil alat tersebut
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Inilah yang terjadi:

- Nama tool kita sudah ada sebagai parameter input `name` yang benar untuk argumen dalam bentuk dictionary `arguments`.

- Tool dipanggil dengan `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validasi argumen terjadi di properti `handler` yang mengarah ke sebuah fungsi, jika gagal akan memunculkan pengecualian.

Nah, sekarang kita punya pemahaman lengkap tentang listing dan pemanggilan tools menggunakan server tingkat rendah.

Lihat [contoh lengkap](./code/README.md) di sini

## Tugas

Perluas kode yang Anda terima dengan sejumlah tools, resources, dan prompt dan refleksikan bagaimana Anda hanya perlu menambahkan file di direktori tools dan tidak di tempat lain.

*Tidak diberikan solusi*

## Ringkasan

Di bab ini, kita melihat bagaimana pendekatan server tingkat rendah bekerja dan bagaimana itu membantu kita membuat arsitektur yang rapi untuk terus dikembangkan. Kita juga membahas validasi dan Anda telah diperlihatkan cara bekerja dengan library validasi untuk membuat schema validasi input.

## Selanjutnya

- Berikutnya: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan interpretasi yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->