# Gelişmiş Sunucu Kullanımı

MCP SDK'de iki farklı türde sunucu bulunur: normal sunucu ve düşük seviyeli sunucu. Genelde, normal sunucuyu kullanarak özellikler eklemek istersiniz. Ancak bazı durumlarda düşük seviyeli sunucuya güvenmek isteyebilirsiniz, örneğin:

- Daha iyi mimari. Hem normal sunucu hem de düşük seviyeli sunucu ile temiz bir mimari oluşturmak mümkündür, ancak düşük seviyeli sunucu ile bunu yapmak biraz daha kolay olabilir.
- Özellik kullanılabilirliği. Bazı gelişmiş özellikler yalnızca düşük seviyeli sunucu ile kullanılabilir. Örnek olarak, ilerleyen bölümlerde örnekleme ve bilgi toplama eklerken bunu göreceksiniz.

## Normal Sunucu vs Düşük Seviyeli Sunucu

Bir MCP Sunucusu oluşturmanın normal sunucu ile nasıl göründüğüne bakalım:

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

Burada, sunucunun sahip olmasını istediğiniz her aracı, kaynağı veya istemi açıkça eklediğinizi görebilirsiniz. Bu yöntemde bir sorun yok.

### Düşük Seviyeli Sunucu Yaklaşımı

Ancak düşük seviyeli sunucu yaklaşımını kullandığınızda, her aracı kaydetmek yerine her özellik türü (araçlar, kaynaklar veya istemler) için iki işleyici oluşturmanız gerektiğini düşünmelisiniz. Örneğin araçlar için yalnızca iki işlev bulunur:

- Tüm araçları listeleme. Bir işlev, araçları listeleme girişimlerinden sorumlu olur.
- Tüm araçları çağırma. Burada da, bir aracı çağırma taleplerini işleyen yalnızca bir işlev bulunur.

Bu kulağa daha az iş gibi geliyor, değil mi? Yani bir aracı kaydetmek yerine, araçları listelediğimde aracın listelendiğinden ve bir aracı çağırma isteği geldiğinde çağrıldığından emin olmam gerekiyor.

Şimdi kodun nasıl göründüğüne bakalım:

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

Burada artık bir özellik listesi döndüren bir işlevimiz var. Araçlar listesindeki her bir giriş artık `name`, `description` ve `inputSchema` gibi alanlara sahip ve dönüş türüne uygun. Bu, araçlarımızı ve özellik tanımlarımızı başka bir yerde tutmamıza olanak tanır. Artık tüm araçlarımızı bir araçlar klasöründe ve aynı şekilde tüm özelliklerinizi başka bir yerde oluşturabilirsiniz, böylece projeniz şu şekilde düzenlenebilir:

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

Peki araçları çağırmak nasıl olacak, aynı fikir mi? Yani, hangi araç olursa olsun bir işleyici mi? Evet, tam olarak, işte bunun kodu:

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

Yukarıdaki koddan görebileceğiniz gibi, çağrılacak aracı ve hangi argümanlarla çağrılacağını ayırmamız gerekiyor, ardından aracı çağırmaya devam etmemiz gerekiyor.

## Yaklaşımı Doğrulama ile İyileştirme

Şimdiye kadar, araçlar, kaynaklar ve istemler eklemek için tüm kayıtlarınızın her özellik türü için bu iki işleyici ile değiştirilebileceğini gördünüz. Peki başka ne yapmamız gerekiyor? Gelen isteğin doğru argümanlarla çağrıldığından emin olmak için bir tür doğrulama eklemeliyiz. Her çalışma zamanı kendi çözümüne sahiptir, örneğin Python Pydantic kullanır ve TypeScript Zod kullanır. Fikir şu şekilde:

- Bir özelliği (araç, kaynak veya istem) oluşturma mantığını kendi özel klasörüne taşıyın.
- Örneğin bir aracı çağırma isteğini doğrulamak için bir yol ekleyin.

### Bir Özellik Oluşturma

Bir özellik oluşturmak için, o özellik için bir dosya oluşturmanız ve o özelliğin zorunlu alanlarına sahip olduğundan emin olmanız gerekir. Hangi alanların gerekli olduğu araçlar, kaynaklar ve istemler arasında biraz farklılık gösterir.

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

Burada şu işlemleri yaptığımızı görebilirsiniz:

- *schema.py* dosyasında `a` ve `b` alanlarına sahip Pydantic `AddInputModel` kullanarak bir şema oluşturma.
- Gelen isteği `AddInputModel` türünde olmaya çalıştırma, parametrelerde bir uyumsuzluk varsa bu hata verecektir:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bu ayrıştırma mantığını araç çağrısının kendisine veya işleyici işlevine koymayı seçebilirsiniz.

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

- Tüm araç çağrılarını ele alan işleyicide, gelen isteği aracın tanımlı şemasına ayrıştırmaya çalışıyoruz:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Eğer bu işe yararsa, gerçek aracı çağırmaya devam ediyoruz:

    ```typescript
    const result = await tool.callback(input);
    ```

Gördüğünüz gibi, bu yaklaşım harika bir mimari oluşturur çünkü her şeyin bir yeri vardır, *server.ts* dosyası yalnızca istek işleyicilerini bağlar ve her özellik kendi klasöründe yer alır, yani tools/, resources/ veya /prompts.

Harika, şimdi bunu oluşturmaya çalışalım.

## Alıştırma: Düşük Seviyeli Sunucu Oluşturma

Bu alıştırmada şunları yapacağız:

1. Araçları listeleme ve araçları çağırmayı ele alan bir düşük seviyeli sunucu oluşturun.
1. Üzerine inşa edebileceğiniz bir mimari uygulayın.
1. Araç çağrılarınızın doğru şekilde doğrulandığından emin olmak için doğrulama ekleyin.

### -1- Bir Mimari Oluşturma

İlk olarak, daha fazla özellik ekledikçe ölçeklenmemize yardımcı olacak bir mimari ele almamız gerekiyor, işte nasıl göründüğü:

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

Artık araçlar klasöründe kolayca yeni araçlar ekleyebileceğimiz bir mimari kurduk. Kaynaklar ve istemler için alt dizinler eklemekten çekinmeyin.

### -2- Bir Araç Oluşturma

Şimdi bir araç oluşturmanın nasıl göründüğüne bakalım. Öncelikle, *tool* alt dizininde şu şekilde oluşturulması gerekiyor:

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

Burada, ad, açıklama, Pydantic kullanarak bir giriş şeması ve bu araç çağrıldığında tetiklenecek bir işleyici tanımladığımızı görüyoruz. Son olarak, tüm bu özellikleri içeren bir sözlük olan `tool_add` öğesini açığa çıkarıyoruz.

Ayrıca, aracımız tarafından kullanılan giriş şemasını tanımlamak için kullanılan *schema.py* dosyası da var:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Ayrıca, araçlar dizininin bir modül olarak ele alınmasını sağlamak için *__init__.py* dosyasını doldurmamız gerekiyor. Ek olarak, içindeki modülleri şu şekilde açığa çıkarmamız gerekiyor:

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

Burada şu özelliklerden oluşan bir sözlük oluşturuyoruz:

- name, bu aracın adı.
- rawSchema, bu Zod şemasıdır, gelen istekleri doğrulamak için kullanılacaktır.
- inputSchema, bu şema işleyici tarafından kullanılacaktır.
- callback, bu araç çağrıldığında tetiklenecek işlevdir.

Ayrıca, bu sözlüğü mcp sunucu işleyicisinin kabul edebileceği bir türe dönüştürmek için kullanılan `Tool` var ve şu şekilde görünüyor:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ve her araç için giriş şemalarını sakladığımız *schema.ts* dosyası var, şu anda yalnızca bir şema var ancak araç ekledikçe daha fazla giriş ekleyebiliriz:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Harika, şimdi araçlarımızı listelemeyi ele almaya geçelim.

### -3- Araç Listelemeyi Ele Alma

Sonraki adımda, araçlarımızı listelemek için bir istek işleyici kurmamız gerekiyor. İşte sunucu dosyamıza eklememiz gerekenler:

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

Burada `@server.list_tools` dekoratörünü ve uygulama işlevi `handle_list_tools` öğesini ekliyoruz. İkincisinde, araçların bir listesini üretmemiz gerekiyor. Her aracın bir adı, açıklaması ve inputSchema'sı olması gerektiğine dikkat edin.

**TypeScript**

Araçları listelemek için istek işleyicisini ayarlamak için, `ListToolsRequestSchema` ile uyumlu bir şema ile sunucuda `setRequestHandler` çağırmamız gerekiyor.

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

Harika, şimdi araçları listeleme parçasını çözdük, bir aracı çağırmanın nasıl olacağına bakalım.

### -4- Bir Aracı Çağırmayı Ele Alma

Bir aracı çağırmak için, hangi özelliğin çağrılacağını ve hangi argümanlarla çağrılacağını belirten bir istekle ilgilenen başka bir istek işleyici kurmamız gerekiyor.

**Python**

`@server.call_tool` dekoratörünü kullanalım ve bunu `handle_call_tool` gibi bir işlevle uygulayalım. Bu işlevde, araç adını, argümanlarını ayırmamız ve argümanların ilgili araç için geçerli olduğundan emin olmamız gerekiyor. Argümanları bu işlevde veya aşağı akışta, gerçek araçta doğrulayabiliriz.

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

Burada olanlar:

- Araç adımız zaten `name` giriş parametresi olarak mevcut, bu argümanlar için de `arguments` sözlüğü şeklinde geçerli.

- Araç `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ile çağrılır. Argümanların doğrulanması, bir işlevi işaret eden `handler` özelliğinde gerçekleşir, eğer başarısız olursa bir istisna oluşturur.

İşte bu kadar, artık düşük seviyeli bir sunucu kullanarak araçları listeleme ve çağırma konusunda tam bir anlayışa sahibiz.

Tam örneği [burada](./code/README.md) görebilirsiniz.

## Ödev

Size verilen kodu bir dizi araç, kaynak ve istem ile genişletin ve yalnızca araçlar dizininde dosya eklemeniz gerektiğini fark ettiğinizde bunu düşünün.

*Çözüm verilmedi*

## Özet

Bu bölümde, düşük seviyeli sunucu yaklaşımının nasıl çalıştığını ve bunun üzerine inşa edebileceğimiz güzel bir mimari oluşturmamıza nasıl yardımcı olabileceğini gördük. Ayrıca doğrulamayı tartıştık ve giriş doğrulama için şemalar oluşturmak üzere doğrulama kütüphaneleriyle nasıl çalışacağınızı gösterdik.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.