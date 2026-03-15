# İleri düzey sunucu kullanımı

MCP SDK'da iki farklı sunucu türü bulunmaktadır; normal sunucunuz ve düşük seviyeli sunucu. Normalde, özellik eklemek için düzenli sunucuyu kullanırsınız. Ancak bazı durumlarda, aşağıdakiler gibi düşük seviyeli sunucuya güvenmek isteyebilirsiniz:

- Daha iyi mimari. Hem düzenli sunucu hem de düşük seviyeli sunucu ile temiz bir mimari oluşturmak mümkündür, ancak düşük seviyeli sunucu ile biraz daha kolay olduğu söylenebilir.
- Özellik uygunluğu. Bazı gelişmiş özellikler sadece düşük seviyeli sunucuyla kullanılabilir. Örnek olarak, örnekleme ve tetikleme eklerken bunları sonraki bölümlerde göreceksiniz.

## Düzenli sunucu vs düşük seviyeli sunucu

MCP Sunucusu oluşturmanın düzenli sunucu ile nasıl göründüğüne bakalım

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

// Toplama aracı ekle
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

Buradaki nokta, sunucuda bulunmasını istediğiniz her araç, kaynak veya istemi açıkça eklemenizdir. Bunun hiçbir sakıncası yoktur.

### Düşük seviyeli sunucu yaklaşımı

Ancak, düşük seviyeli sunucu yaklaşımını kullandığınızda farklı düşünmeniz gerekir. Her aracı kaydetmek yerine, özellik türü başına (araçlar, kaynaklar veya istemler) iki işleyici oluşturursunuz. Örneğin araçlar için sadece iki işlev olur:

- Tüm araçları listeleme. Bir işlev, araçları listelemeye yönelik tüm denemelerden sorumlu olur.
- Araç çağrılarını işleme. Burada da sadece tek bir işlev, bir araca yapılan çağrıları işler.

Bu potansiyel olarak daha az işmiş gibi mi geliyor? Yani bir araç kaydetmek yerine, sadece araçlar listelendiğinde aracın listede olmasını ve bir araç çağrısı geldiğinde çağrılmasını sağlamam gerekiyor.

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
  // Kayıtlı araçların listesini döndürür
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

Burada artık bir özellikler listesini döndüren bir işlevimiz var. Araçlar listesindeki her kayıt, dönüş türüne uymak için `name`, `description` ve `inputSchema` gibi alanlara sahiptir. Bu, araçlarımızı ve özellik tanımlarımızı başka bir yere koymamıza olanak sağlar. Artık tüm araçlarımızı tools klasöründe oluşturabiliriz ve tüm özellikleriniz için aynı durum geçerlidir, böylece projeniz aniden şu şekilde düzenlenebilir:

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

Harika, mimarimiz oldukça temiz görülebilir.

Peki araçları çağırmak, aynı fikir mi yani, hangi araç olursa olsun aracı çağırmak için tek bir işleyici mi? Evet, tam olarak, işte bunun kodu:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools, anahtarları araç isimleri olan bir sözlüktür
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

Yukarıdaki koddan görebileceğiniz üzere, çağrılacak aracı ve hangi argümanlarla çağrılacağını ayrıştırmamız gerekiyor ve ardından aracı çağırmaya devam etmemiz gerekir.

## Yaklaşımı doğrulama ile geliştirme

Şimdiye kadar araçlar, kaynaklar ve istemler eklemek için yaptığınız tüm kayıtların her özellik türü başına bu iki işleyici ile nasıl değiştirilebileceğini gördünüz. Başka ne yapmamız gerekiyor? Araçların doğru argümanlarla çağrıldığından emin olmak için bir tür doğrulama eklemeliyiz. Her çalışma zamanı kendi çözümünü kullanır; örneğin Python Pydantic kullanır ve TypeScript Zod kullanır. Buradaki fikir:

- Bir özelliği (araç, kaynak veya istem) oluşturma mantığını ona adanmış klasöre taşımak.
- Örneğin bir araç çağrısı yapmak isteyen gelen bir isteği doğrulamanın bir yolunu eklemek.

### Bir özellik oluşturmak

Bir özellik oluşturmak için bu özellik için bir dosya yaratmanız ve o özelliğin gerektirdiği zorunlu alanların bulunduğundan emin olmanız gerekir. Hangi alanların farklılık gösterdiği araçlar, kaynaklar ve istemler arasında biraz değişir.

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
        # Girişi Pydantic modeli kullanarak doğrulayın
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ekle, böylece bir AddInputModel oluşturabilir ve argümanları doğrulayabiliriz

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Burada şu işlemleri nasıl yaptığımızı görebilirsiniz:

- *schema.py* dosyasında `a` ve `b` alanlarına sahip Pydantic `AddInputModel` şema oluşturmak.
- Gelen isteğin `AddInputModel` türünde olup olmadığını ayrıştırmaya çalışmak; parametrelerde uyumsuzluk varsa bu çökmesine neden olur:

   ```python
   # add.py
    try:
        # Girdiyi Pydantic modeli kullanarak doğrulayın
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Bu ayrıştırma mantığını, araç çağrısı içinde ya da işleyici fonksiyonda koymayı seçebilirsiniz.

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

- Tüm araç çağrılarını işleyen işleyicide, gelen isteği aracın tanımlı şemasına ayrıştırmaya çalışıyoruz:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Eğer bu başarılı olursa, gerçek aracı çağırmaya devam ediyoruz:

    ```typescript
    const result = await tool.callback(input);
    ```

Gördüğünüz gibi, bu yaklaşım harika bir mimari yaratıyor çünkü her şeyin yeri belli, *server.ts* sadece istek işleyicilerini bağlayan çok küçük bir dosya ve her özellik kendi klasöründe yani tools/, resources/ veya prompts/.

Harika, bunu şimdi oluşturmaya çalışalım.

## Egzersiz: Düşük seviyeli sunucu oluşturma

Bu egzersizde şu işlemleri yapacağız:

1. Araçların listelenmesini ve araçların çağrılmasını yöneten düşük seviyeli bir sunucu oluşturmak.
1. Üzerine inşa edebileceğiniz bir mimari gerçekleştirmek.
1. Araç çağrılarınızın doğru şekilde doğrulanmasını sağlamak için doğrulama eklemek.

### -1- Bir mimari oluşturmak

Ele almamız gereken ilk şey, daha fazla özellik ekledikçe büyümemize yardımcı olacak bir mimaridir, işte nasıl göründüğü:

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

Artık araçlar klasöründe kolayca yeni araçlar ekleyebileceğimiz bir mimari kurduk. İsterseniz kaynaklar ve istemler için alt dizinler ekleyebilirsiniz.

### -2- Bir araç oluşturmak

Şimdi bir araç oluşturmanın nasıl göründüğüne bakalım. Öncelikle, bunu tools alt dizininde oluşturmalısınız:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic modeli kullanarak girdiyi doğrulayın
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ekle, böylece bir AddInputModel oluşturup argümanları doğrulayabiliriz

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Burada adı, açıklaması ve Pydantic kullanarak giriş şeması nasıl tanımlanıyor ve bu araç çağrıldığında tetiklenecek bir işleyici olduğu gösteriliyor. Son olarak, tüm bu özellikleri tutan `tool_add` sözlüğünü dışarı açıyoruz.

Ayrıca aracımızın giriş şemasını tanımlamak için kullanılan *schema.py* var:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Araçlar dizininin modül olarak kabul edilmesini sağlamak için *__init__.py* dosyasını da doldurmamız gerekir. Ayrıca içindeki modülleri şöyle açığa çıkarmamız gerekir:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Daha fazla araç ekledikçe bu dosyayı genişletebiliriz.

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

Burada özelliklerden oluşan bir sözlük yaratıyoruz:

- name, aracın adı.
- rawSchema, Zod şemasıdır, bu araç çağrılarını doğrulamak için kullanılacak.
- inputSchema, bu şema işleyici tarafından kullanılacak.
- callback, aracı çağırmak için kullanılacak.

Ayrıca `Tool` var, bu sözlüğü mcp sunucu işleyicisinin kabul edebileceği türe dönüştürmek için kullanılır ve şöyle görünür:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ve her aracın giriş şemasını sakladığımız *schema.ts* var, şu anda sadece bir şema var ama araç ekledikçe yeni kayıtlar ekleyebiliriz:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Harika, şimdi araçlarımızın listesini nasıl yöneteceğimizi ele alalım.

### -3- Araç listesini yönetmek

Araçları listelemek için, bununla ilgili bir istek işleyici kurmamız gerekir. Sunucu dosyamıza eklememiz gerekenler şunlar:

**Python**

```python
# kısalık için kod atlandı
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

Burada `@server.list_tools` dekoratörünü ve bunu uygulayan `handle_list_tools` fonksiyonunu ekliyoruz. Bu fonksiyon içinde bir araçlar listesi üretmeliyiz. Her aracın bir adı, açıklaması ve inputSchema alanına sahip olması gerektiğine dikkat edin.

**TypeScript**

Araçları listelemek için istek işleyiciyi kurmak adına, `setRequestHandler` fonksiyonunu, yapmak istediğimiz işe uygun bir şema ile birlikte sunucuda çağırmalıyız; burada `ListToolsRequestSchema` kullanılıyor.

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
  // Kayıtlı araçların listesini döndür
  return {
    tools: tools
  };
});
```

Harika, artık araçları listeleme kısmını çözdük, sırada araçların nasıl çağrılacağı var.

### -4- Araç çağrısını yönetmek

Bir aracı çağırmak için, hangi özelliğin çağrılacağı ve hangi argümanlarla belirtildiğine odaklanan yeni bir istek işleyici kurmamız gerekiyor.

**Python**

`@server.call_tool` dekoratörünü kullanalım ve `handle_call_tool` gibi bir fonksiyon ile uygulayalım. Bu fonksiyon içinde araç adını, argümanlarını ayrıştırmalı ve argümanların ilgili araç için geçerli olduklarından emin olmalıyız. Argüman doğrulamasını bu fonksiyonda veya daha aşağıda, gerçek araçta yapabiliriz.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools, anahtarları araç isimleri olan bir sözlüktür
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # aracı çağır
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Yapılanlar şunlar:

- Aracın adı, girdi parametresi `name` olarak zaten mevcuttur ve argümanlarımız burada `arguments` adlı sözlük şeklindedir.

- Araç `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ile çağrılır. Argüman doğrulama, `handler` özelliği tarafından işlenir; burası bir fonksiyona işaret eder, doğrulama başarısız olursa hata oluşturur.

Artık düşük seviyeli sunucu kullanarak araçları listeleme ve çağırma konusunda tam bir anlayışa sahibiz.

Tam örneği [buradan](./code/README.md) görebilirsiniz.

## Ödev

Size verilen kodu, çeşitli araçlar, kaynaklar ve istemlerle genişletin ve sadece tools dizinine dosya eklemekle yetindiğinizi fark edin.

*Çözüm verilmemiştir*

## Özet

Bu bölümde düşük seviyeli sunucu yaklaşımının nasıl işlediğini ve bunun üzerine inşa edebileceğimiz iyi bir mimari oluşturulmasına nasıl yardımcı olabileceğini gördük. Ayrıca doğrulamayı ele aldık ve girdi doğrulaması için doğrulama kütüphaneleriyle nasıl şema oluşturulacağını gösterdik.

## Sonraki

- Sonraki: [Basit Kimlik Doğrulama](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanılması sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalar konusunda sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->