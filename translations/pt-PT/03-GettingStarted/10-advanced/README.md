# Utilização avançada do servidor

Existem dois tipos diferentes de servidores expostos no MCP SDK, o seu servidor normal e o servidor de baixo nível. Normalmente, usaria o servidor regular para adicionar funcionalidades a ele. No entanto, em alguns casos, deseja confiar no servidor de baixo nível, tais como:

- Melhor arquitetura. É possível criar uma arquitetura limpa tanto com o servidor regular como com o servidor de baixo nível, mas pode-se argumentar que é ligeiramente mais fácil com um servidor de baixo nível.
- Disponibilidade de funcionalidades. Algumas funcionalidades avançadas só podem ser usadas com um servidor de baixo nível. Verá isto nos capítulos seguintes, à medida que adicionarmos amostragem e elicitação.

## Servidor regular vs servidor de baixo nível

Aqui está como a criação de um Servidor MCP se apresenta com o servidor regular

**Python**

```python
mcp = FastMCP("Demo")

# Adicionar uma ferramenta de adição
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

// Adicionar uma ferramenta de adição
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

A questão é que adiciona explicitamente cada ferramenta, recurso ou prompt que deseja que o servidor tenha. Não há nada de errado com isso.

### Abordagem do servidor de baixo nível

No entanto, quando usa a abordagem do servidor de baixo nível, precisa de pensar de forma diferente. Em vez de registar cada ferramenta, cria dois manipuladores por tipo de funcionalidade (ferramentas, recursos ou prompts). Por exemplo, as ferramentas têm apenas duas funções assim:

- Listar todas as ferramentas. Uma função é responsável por todas as tentativas de listar ferramentas.
- Manipular chamadas a todas as ferramentas. Aqui também, existe apenas uma função que trata as chamadas a uma ferramenta.

Parece potencialmente menos trabalho, certo? Então, em vez de registar uma ferramenta, só preciso garantir que a ferramenta está listada quando listo todas as ferramentas e que é chamada quando existe um pedido para chamar uma ferramenta.

Vamos ver como o código fica agora:

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
  // Retorna a lista de ferramentas registadas
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

Aqui temos uma função que retorna uma lista de funcionalidades. Cada entrada na lista de ferramentas tem campos como `name`, `description` e `inputSchema` para aderir ao tipo de retorno. Isto permite-nos colocar as nossas ferramentas e definições de funcionalidades noutro lugar. Podemos agora criar todas as nossas ferramentas numa pasta tools e o mesmo para todas as suas funcionalidades, de modo que o seu projeto pode subitamente ter a seguinte organização:

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

Isso é ótimo, a nossa arquitetura pode ficar bastante limpa.

E quanto a chamar as ferramentas, é a mesma ideia, um manipulador para chamar uma ferramenta, qualquer ferramenta? Sim, exatamente, aqui está o código para isso:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools é um dicionário com nomes de ferramentas como chaves
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
    // TODO chamar a ferramenta,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Como pode ver pelo código acima, precisamos de analisar qual a ferramenta a chamar, com que argumentos, e depois avançamos para chamar a ferramenta.

## Melhorando a abordagem com validação

Até agora, viu como todas as suas registos para adicionar ferramentas, recursos e prompts podem ser substituídos por estes dois manipuladores por tipo de funcionalidade. O que mais precisamos fazer? Bem, deveríamos adicionar algum tipo de validação para garantir que a ferramenta é chamada com os argumentos corretos. Cada runtime tem a sua própria solução para isso, por exemplo Python usa Pydantic e TypeScript usa Zod. A ideia é que façamos o seguinte:

- Mover a lógica para criar uma funcionalidade (ferramenta, recurso ou prompt) para a sua pasta dedicada.
- Adicionar uma forma de validar um pedido que chega a pedir, por exemplo, chamar uma ferramenta.

### Criar uma funcionalidade

Para criar uma funcionalidade, precisamos de criar um ficheiro para essa funcionalidade e garantir que tem os campos obrigatórios exigidos por essa funcionalidade. Que campos diferem um pouco entre ferramentas, recursos e prompts.

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
        # Validar a entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adicionar Pydantic, para podermos criar um AddInputModel e validar os argumentos

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Aqui pode ver como fazemos o seguinte:

- Criamos um esquema usando Pydantic `AddInputModel` com os campos `a` e `b` no ficheiro *schema.py*.
- Tentamos analisar o pedido que chega para ser do tipo `AddInputModel`, se houver um desacordo nos parâmetros isto irá falhar:

   ```python
   # add.py
    try:
        # Validar a entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Pode escolher se coloca esta lógica de parsing na própria chamada da ferramenta ou na função manipuladora.

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

- No manipulador que trata todas as chamadas a ferramentas, tentamos agora analisar o pedido que chega para o esquema definido pela ferramenta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    se isso funcionar, avançamos para chamar a ferramenta de fato:

    ```typescript
    const result = await tool.callback(input);
    ```

Como pode ver, esta abordagem cria uma excelente arquitetura pois tudo tem o seu lugar, o *server.ts* é um ficheiro muito pequeno que só liga os manipuladores de pedidos e cada funcionalidade está na sua pasta respetiva, ou seja tools/, resources/ ou /prompts.

Ótimo, vamos tentar construir isto a seguir.

## Exercício: Criar um servidor de baixo nível

Neste exercício, faremos o seguinte:

1. Criar um servidor de baixo nível que trate da listagem de ferramentas e chamada de ferramentas.
1. Implementar uma arquitetura sobre a qual possa construir.
1. Adicionar validação para garantir que as chamadas às suas ferramentas são devidamente validadas.

### -1- Criar uma arquitetura

A primeira coisa que precisamos de tratar é uma arquitetura que nos ajude a escalar conforme adicionamos mais funcionalidades, aqui está como fica:

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

Agora configurámos uma arquitetura que garante que podemos adicionar facilmente novas ferramentas numa pasta tools. Sinta-se à vontade para seguir isto e adicionar subdiretórios para resources e prompts.

### -2- Criar uma ferramenta

Vamos ver como criar uma ferramenta a seguir. Primeiro, precisa de ser criada no seu subdiretório *tool* assim:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validar a entrada usando o modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adicionar Pydantic, para podermos criar um AddInputModel e validar os argumentos

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

O que vemos aqui é como definimos o nome, descrição e o esquema de entrada usando Pydantic e um manipulador que será invocado quando esta ferramenta for chamada. Por fim, expomos `tool_add` que é um dicionário contendo todas estas propriedades.

Também existe *schema.py* que é usado para definir o esquema de entrada utilizado pela nossa ferramenta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Também precisamos de preencher o *__init__.py* para garantir que a pasta tools é tratada como um módulo. Além disso, precisamos de expor os módulos dentro dela assim:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos continuar a adicionar a este ficheiro conforme adicionamos mais ferramentas.

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

Aqui criamos um dicionário composto por propriedades:

- name, este é o nome da ferramenta.
- rawSchema, este é o esquema Zod, será usado para validar pedidos que cheguem para chamar esta ferramenta.
- inputSchema, este esquema será usado pelo manipulador.
- callback, isto é usado para invocar a ferramenta.

Também existe `Tool` que é usado para converter este dicionário num tipo que o manipulador do servidor mcp pode aceitar e fica assim:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

E há *schema.ts* onde armazenamos os esquemas de entrada para cada ferramenta que fica assim com apenas um esquema no momento, mas à medida que adicionamos ferramentas podemos adicionar mais entradas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Ótimo, vamos avançar para tratar a listagem das nossas ferramentas a seguir.

### -3- Tratar da listagem das ferramentas

A seguir, para tratar da listagem das nossas ferramentas, precisamos de configurar um manipulador de pedidos para isso. Aqui está o que precisamos adicionar ao nosso ficheiro do servidor:

**Python**

```python
# código omitido para brevidade
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

Aqui, adicionamos o decorador `@server.list_tools` e a função implementadora `handle_list_tools`. Nesta última, precisamos de produzir uma lista de ferramentas. Note como cada ferramenta precisa ter um nome, descrição e inputSchema.

**TypeScript**

Para configurar o manipulador do pedido para listar as ferramentas, precisamos de chamar `setRequestHandler` no servidor com um esquema adequado ao que queremos fazer, neste caso `ListToolsRequestSchema`.

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
// código omitido para brevidade
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Retorna a lista de ferramentas registadas
  return {
    tools: tools
  };
});
```

Ótimo, agora resolvemos a parte de listar as ferramentas, vejamos como poderíamos chamar ferramentas a seguir.

### -4- Tratar de chamar uma ferramenta

Para chamar uma ferramenta, precisamos de configurar outro manipulador de pedidos, desta vez focado em lidar com um pedido que especifica qual funcionalidade chamar e com que argumentos.

**Python**

Vamos usar o decorador `@server.call_tool` e implementá-lo com uma função como `handle_call_tool`. Dentro dessa função, precisamos de extrair o nome da ferramenta, o seu argumento e garantir que os argumentos são válidos para a ferramenta em questão. Podemos validar os argumentos nesta função ou a jusante na própria ferramenta.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools é um dicionário com nomes de ferramentas como chaves
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invocar a ferramenta
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Aqui está o que acontece:

- O nosso nome da ferramenta já está presente como o parâmetro de entrada `name` que é verdadeiro para os nossos argumentos na forma do dicionário `arguments`.

- A ferramenta é chamada com `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. A validação dos argumentos acontece na propriedade `handler` que aponta para uma função; se isso falhar, será levantada uma exceção.

Pronto, agora temos uma compreensão completa de listar e chamar ferramentas usando um servidor de baixo nível.

Veja o [exemplo completo](./code/README.md) aqui

## Tarefa

Estenda o código que lhe foi dado com várias ferramentas, recursos e prompts e reflita sobre como nota que só precisa de adicionar ficheiros no diretório tools e em nenhum outro sítio.

*Sem solução fornecida*

## Resumo

Neste capítulo, vimos como a abordagem do servidor de baixo nível funciona e como isso pode ajudar-nos a criar uma arquitetura agradável sobre a qual podemos continuar a construir. Também discutimos a validação e foi-lhe mostrado como trabalhar com bibliotecas de validação para criar esquemas para validação de entradas.

## Próximos passos

- A seguir: [Autenticação Simples](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->