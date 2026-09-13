# Gelişmiş sunucu kullanımı

MCP SDK'da iki farklı sunucu türü bulunmaktadır, normal sunucunuz ve düşük seviyeli sunucu. Normalde, ek özellikler eklemek için düzenli sunucuyu kullanırsınız. Ancak bazı durumlarda şu gibi nedenlerle düşük seviyeli sunucuya güvenmek istersiniz:

- Daha iyi mimari. Hem düzenli sunucu hem de düşük seviyeli sunucu ile temiz bir mimari oluşturmak mümkündür ama düşük seviyeli sunucu ile biraz daha kolay olduğu ileri sürülebilir.
- Özellik kullanılabilirliği. Bazı gelişmiş özellikler sadece
    düşük seviyeli sunucu ile kullanılabilir. Sonraki bölümlerde MCP `2026-07-28` sürümünde kullanımdan kaldırılmış olan
    Elicitation ve eski Sampling özelliği ele alınacaktır.

## Düzenli sunucu vs düşük seviyeli sunucu

MCP Sunucusunun düzenli sunucu ile oluşturulması şöyle görünür:

**Python**

```python
mcp = FastMCP("Demo")

# Bir toplama aracı ekle
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

// Bir toplama aracı ekle
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

Buradaki nokta, sunucunun sahip olmasını istediğiniz her araç, kaynak ya da istemi açıkça eklemenizdir. Bunun hiçbir sakıncası yoktur.  

### Düşük seviyeli sunucu yaklaşımı

Ancak, düşük seviyeli sunucu yaklaşımını kullandığınızda bunu farklı düşünmeniz gerekir. Her araç yerine, her özellik türü (araçlar, kaynaklar veya istemler) için iki işleyici oluşturursunuz. Örneğin, araçların sadece iki işlevi olur şöyle:

- Tüm araçların listelenmesi. Bir işlev, araçları listelemek için yapılan tüm denemelerden sorumlu olur.
- Her araca yapılan çağrıyı işlemek. Burada da sadece tek bir işlev, araca yapılan çağrıları yönetir.

Bu muhtemelen daha az iş gibi görünüyor, değil mi? Yani bir aracı kaydetmek yerine, tüm araçları listelerken aracın listede olmasını ve bir aracı çağırma isteği geldiğinde çağrılmasını sağlamam yeterli.

Şimdi koda bakalım:

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
  // Kayıtlı araçların listesini döndür
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

Burada artık özelliklerin bir listesini döndüren bir işlev var. Araçlar listesindeki her giriş artık `name` (isim), `description` (açıklama) ve `inputSchema` gibi dönüş tipine uymak için alanlara sahip. Bu, araçlarımızı ve özellik tanımlarımızı başka yere koymamıza olanak tanır. Artık tüm araçlarımızı tools (araçlar) klasöründe oluşturabiliriz ve aynı şekilde tüm özellikleriniz için de böyle olabilir, böylece projeniz aniden şöyle organize olabilir:

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

Harika, mimarimiz oldukça temiz görünebilir.

Araçların çağrılmasına ne dersiniz, aynı fikir mi; bir işleyici herhangi bir aracı çağırıyor mu? Evet, kesinlikle, işte bunun kodu:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools, araç isimlerinin anahtar olduğu bir sözlüktür
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
    // TODO aracı çağır,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Yukarıdaki koddan görebileceğiniz gibi, çağrılacak aracı ve hangi argümanlarla çağrılacağını ayrıştırmamız gerekiyor, sonra aracı çağırmaya geçmemiz gerekiyor.

## Yaklaşımı doğrulama ile geliştirmek

Şimdiye kadar, araçlar, kaynaklar ve istemler eklemek için tüm kayıtların bu iki işleyici ile nasıl değiştirilebileceğini gördünüz. Başka ne yapmamız gerekiyor? Aslında, aracın doğru argümanlarla çağrıldığından emin olmak için bir tür doğrulama eklemeliyiz. Her çalışma zamanı bunu kendi çözümüyle yapar, örneğin Python Pydantic kullanır, TypeScript ise Zod. Fikir şudur:

- Bir özelliğin (araç, kaynak veya istem) oluşturulma mantığını kendi klasörüne taşımak.
- Gelen bir isteğin, örneğin bir aracı çağırma talebinin doğrulanmasını sağlamanın bir yolunu eklemek.

### Bir özellik oluşturmak

Bir özellik oluşturmak için o özellik için bir dosya oluşturmalıyız ve o özelliğin zorunlu alanlarını içerdiğinden emin olmalıyız. Bu alanlar araçlar, kaynaklar ve istemler arasında biraz farklılık gösterir.

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
        # Girişi Pydantic modeli kullanarak doğrula
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # YAPILACAK: Pydantic ekle, böylece bir AddInputModel oluşturabilir ve argümanları doğrulayabiliriz

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

burada şu işlemleri nasıl yaptığımızı görebilirsiniz:

- *schema.py* dosyasında `AddInputModel` adında Pydantic kullanılarak `a` ve `b` alanlarına sahip bir şema oluşturmak.
- Gelen isteği `AddInputModel` türünde ayrıştırmaya çalışmak, parametreler uyuşmazsa burada hata verecektir:

   ```python
   # add.py
    try:
        # Girdiyi Pydantic modeli kullanarak doğrula
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bu ayrıştırma mantığını araç çağrısının içinde veya işleyici fonksiyonda yapmayı seçebilirsiniz.

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

- Tüm araç çağrılarıyla ilgilenen işleyicide, gelen isteği aracın tanımlı şemasına ayrıştırmaya çalışırız:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    eğer işe yararsa, gerçek aracı çağırmaya devam ederiz:

    ```typescript
    const result = await tool.callback(input);
    ```

Gördüğünüz gibi, bu yaklaşım çok güzel bir mimari oluşturur çünkü her şey yerinde olur; *server.ts* dosyası sadece istek işleyicilerini bağlayan çok küçük bir dosyadır ve her özellik kendi klasöründedir: tools/, resources/ veya /prompts.

Harika, bunu şimdi oluşturmaya çalışalım.

## Alıştırma: Düşük seviyeli sunucu oluşturma

Bu alıştırmada şunları yapacağız:

1. Araçların listelenmesi ve çağrılması işlemlerini yöneten düşük seviyeli bir sunucu oluşturun.
1. Üzerine inşa edebileceğiniz bir mimari uygulayın.
1. Araç çağrılarınızın doğru şekilde doğrulandığından emin olmak için doğrulama ekleyin.

### -1- Mimari oluşturmak

Öncelikle, daha fazla özellik ekledikçe ölçeklendirmemize yardımcı olacak bir mimariye ihtiyacımız var, şöyle görünür:

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

Artık araçların tools klasörüne kolayca eklenmesini sağlayan bir mimari kurduk. Kaynaklar ve istemler için alt dizinler eklemek isterseniz bunu takip edin.

### -2- Bir araç oluşturmak

Bir aracı oluşturmanın nasıl göründüğüne bakalım. Öncelikle, *tool* alt dizininde oluşturulmalıdır şöyle:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Girdiyi Pydantic modeli kullanarak doğrula
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # YAPILACAK: Pydantic ekle, böylece bir AddInputModel oluşturup argümanları doğrulayabiliriz

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Burada isim, açıklama ve girdi şeması Pydantic ile tanımlanıyor ve araç çağrıldığında tetiklenen bir işleyici var. Son olarak, tüm bu özellikleri içeren bir sözlük olan `tool_add`i dışa açıyoruz.

Ayrıca aracımızın kullandığı girdiyi tanımlamak için kullanılan *schema.py* de vardır:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Araçlar klasörünün modül olarak kabul edilmesi için *__init__.py* dosyasını da doldurmamız gerekiyor. Ayrıca içindeki modülleri şöyle dışa açmalıyız:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Daha fazla araç ekledikçe bu dosyaya eklemeye devam edebiliriz.

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

Burada bir sözlük oluşturuyoruz ve içeriğinde şunlar var:

- name, aracın adı.
- rawSchema, Zod şeması, bu aracı çağırma isteklerini doğrulamak için kullanılır.
- inputSchema, bu şema işleyici tarafından kullanılır.
- callback, araç çağrısını gerçekleştirmek için kullanılır.

Ayrıca sözlüğü mcp sunucu işleyicisinin kabul edebileceği bir tipe dönüştürmek için kullanılan `Tool` vardır ve şöyle görünür:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Araçların girdi şemalarını saklamak için *schema.ts* dosyası vardır; burada şu anda tek bir şema var ama araçlar ekledikçe daha fazla giriş ekleyebiliriz:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Harika, şimdi araçların nasıl listeleneceğine geçelim.

### -3- Araç listesini yönetmek

Şimdi araç listesini yönetmek için bir istek işleyicisi kurmamız gerekiyor. Sunucu dosyamızda eklememiz gerekenler şöyle:

**Python**

```python
# kısaltma için kod atlandı
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

Burada, `@server.list_tools` dekoratörünü ve uygulama fonksiyonu `handle_list_tools`'u ekliyoruz. İşlevde bir araç listesi üretmemiz gerekiyor. Her aracın bir isme, açıklamaya ve inputSchema'ya sahip olması gerektiğine dikkat edin.   

**TypeScript**

Araç listesini oluşturmak için istek işleyicisi kurarken sunucuda, yapmaya çalıştığımız şeyi karşılayan bir şemayla `setRequestHandler` çağrılır, bu durumda `ListToolsRequestSchema`.

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
// kısalık için kod atlandı
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Kayıtlı araçların listesini döndürür
  return {
    tools: tools
  };
});
```

Harika, araçları listeleme işini çözdük, şimdi araç çağırma kısmına bakalım.

### -4- Bir araç çağrısını yönetmek

Bir aracı çağırmak için başka bir istek işleyicisi kurmamız gerekiyor, bu sefer hangi özelliğin hangi argümanlarla çağrıldığını belirleyen bir istekle ilgilenir.

**Python**

`@server.call_tool` dekoratörünü kullanalım ve `handle_call_tool` gibi bir işlevle uygulayalım. Bu işlevde, araç adını, argümanlarını ayrıştırmalı ve argümanların geçerli olduğundan emin olmalıyız. Bu doğrulamayı bu işlevde veya aşağı akışta asıl araç çağrısında yapabiliriz.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools, araç isimlerini anahtar olarak kullanan bir sözlüktür
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # aracı çağırmak
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

İşlem şu şekilde:

- Araç adımız giriş parametresi `name` olarak zaten mevcuttur; argümanlarımız ise `arguments` sözlüğünün şeklindedir.

- Araç, `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ile çağrılır. Argümanların doğrulanması `handler` özelliğinde, yani bir fonksiyona işaret eden yerde yapılır, başarısız olursa bir istisna fırlatılır.

İşte böyle, şimdi düşük seviyeli sunucu kullanarak araçları listeleme ve çağırma işlemlerini tamamen anladık.

[Tam örnek](./code/README.md) burada görülebilir

## Ödev

Verilen kodu birkaç araç, kaynak ve istemle genişletin ve sadece tools dizinine dosya eklemeniz gerektiğini fark edin, başka herhangi bir yere eklemenize gerek olmadığını gözlemleyin.

*Çözüm verilmedi*

## Özet

Bu bölümde, düşük seviyeli sunucu yaklaşımının nasıl çalıştığını ve üzerine inşa edilebilecek güzel bir mimari yaratmamıza nasıl olanak tanıdığını gördük. Doğrulamayı da tartıştık ve giriş doğrulaması için şemalar oluşturmak üzere doğrulama kütüphaneleri ile nasıl çalışılacağını gösterdik.

## Sonraki Adım

- Sonraki: [Basit Kimlik Doğrulama](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->