# Utilização avançada do servidor

Existem dois tipos diferentes de servidores expostos no SDK MCP, o seu servidor normal e o servidor de baixo nível. Normalmente, usaria o servidor regular para adicionar funcionalidades ao mesmo. Em alguns casos, porém, quer usar o servidor de baixo nível, como por exemplo:

- Melhor arquitetura. É possível criar uma arquitetura limpa tanto com o servidor regular como com o servidor de baixo nível, mas pode-se argumentar que é um pouco mais fácil com o servidor de baixo nível.
- Disponibilidade de funcionalidades. Algumas funcionalidades avançadas só podem ser usadas com um
    servidor de baixo nível. Capítulos posteriores cobrem a Elicitação e a funcionalidade legada de Amostragem,
    que está obsoleta no MCP `2026-07-28`.

## Servidor regular vs servidor de baixo nível

Eis como se cria um Servidor MCP com o servidor regular:

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

// Adicionar uma ferramenta de soma
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

O ponto é que adiciona explicitamente cada ferramenta, recurso ou prompt que quer que o servidor tenha. Não há nada de errado nisso.  

### Abordagem do servidor de baixo nível

No entanto, quando se usa a abordagem do servidor de baixo nível, é preciso pensar de modo diferente. Em vez de registar cada ferramenta, cria-se dois manipuladores por tipo de funcionalidade (ferramentas, recursos ou prompts). Por exemplo, as ferramentas têm apenas duas funções como segue:

- Listar todas as ferramentas. Uma função seria responsável por todas as tentativas de listar ferramentas.
- Tratar chamadas a todas as ferramentas. Aqui também, há apenas uma função que trata as chamadas a uma ferramenta.

Parece potencialmente menos trabalho certo? Então, em vez de registar uma ferramenta, só preciso garantir que a ferramenta está listada quando listar todas as ferramentas e que é chamada quando há um pedido para chamar uma ferramenta. 

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

Aqui temos uma função que retorna uma lista de funcionalidades. Cada entrada na lista de ferramentas tem agora campos como `name`, `description` e `inputSchema` para obedecer ao tipo de retorno. Isso permite colocar as nossas ferramentas e definições de funcionalidades noutro local. Agora podemos criar todas as nossas ferramentas numa pasta tools e o mesmo vale para todas as suas funcionalidades, para que o seu projeto possa, de repente, estar organizado assim:

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

Isso é ótimo, a nossa arquitetura pode ser feita para parecer bastante limpa.

E quanto a chamar ferramentas, é a mesma ideia então, um manipulador para chamar uma ferramenta, qualquer ferramenta? Sim, exatamente, aqui está o código para isso:

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

Como vê no código acima, precisamos de analisar qual a ferramenta a chamar e com que argumentos, e depois proceder à chamada da ferramenta.

## Melhorar a abordagem com validação

Até agora, viu como todos os seus registos para adicionar ferramentas, recursos e prompts podem ser substituídos por estes dois manipuladores por tipo de funcionalidade. O que mais precisamos de fazer? Bem, devemos adicionar algum tipo de validação para garantir que a ferramenta é chamada com os argumentos corretos. Cada ambiente de execução tem a sua própria solução para isso, por exemplo Python usa Pydantic e TypeScript usa Zod. A ideia é que fazemos o seguinte:

- Mover a lógica para criar uma funcionalidade (ferramenta, recurso ou prompt) para a sua pasta dedicada.
- Adicionar uma forma de validar um pedido que entra para, por exemplo, chamar uma ferramenta.

### Criar uma funcionalidade

Para criar uma funcionalidade, precisaremos de criar um ficheiro para essa funcionalidade e certificar-nos de que tem os campos obrigatórios exigidos para essa funcionalidade, os campos que diferem um pouco entre ferramentas, recursos e prompts.

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
        # Validar entrada usando o modelo Pydantic
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

aqui pode ver como fazemos o seguinte:

- Criar um schema usando Pydantic `AddInputModel` com os campos `a` e `b` no ficheiro *schema.py*.
- Tentar analisar o pedido que entra para ser do tipo `AddInputModel`, se houver um desajuste nos parâmetros, isto irá falhar:

   ```python
   # add.py
    try:
        # Validar entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Pode escolher se põe esta lógica de análise na própria chamada da ferramenta ou na função do manipulador.

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

- No manipulador que trata todas as chamadas às ferramentas, agora tentamos analisar o pedido que entra ao esquema definido para a ferramenta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    se isso funcionar, então procedemos a chamar a ferramenta:

    ```typescript
    const result = await tool.callback(input);
    ```

Como pode ver, esta abordagem cria uma excelente arquitetura porque tudo tem o seu lugar, o *server.ts* é um ficheiro muito pequeno que apenas liga os manipuladores de pedidos e cada funcionalidade está na sua pasta respetiva, ou seja tools/, resources/ ou prompts/.

Ótimo, vamos tentar construir isto a seguir. 

## Exercício: Criar um servidor de baixo nível

Neste exercício, vamos fazer o seguinte:

1. Criar um servidor de baixo nível que trata da listagem de ferramentas e chamadas de ferramentas.
1. Implementar uma arquitetura sobre a qual possa construir.
1. Adicionar validação para garantir que as chamadas às suas ferramentas são devidamente validadas.

### -1- Criar uma arquitetura

A primeira coisa que precisamos de resolver é uma arquitetura que nos ajude a escalar à medida que adicionamos mais funcionalidades, veja como fica:

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

Agora configurámos uma arquitetura que assegura que podemos facilmente adicionar novas ferramentas na pasta tools. Sinta-se à vontade para seguir esta estrutura e adicionar subdiretórios para resources e prompts.

### -2- Criar uma ferramenta

Vejamos o aspeto de criar uma ferramenta a seguir. Primeiro, precisa de ser criada na sua subpasta *tool* assim:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validar entrada usando modelo Pydantic
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

O que vemos aqui é como definimos o nome, a descrição e o esquema de entrada usando Pydantic e um manipulador que será invocado sempre que esta ferramenta for chamada. Por último, expomos `tool_add` que é um dicionário com todas estas propriedades.

Há também *schema.py* que é usado para definir o esquema de entrada usado pela nossa ferramenta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Também precisamos de preencher o *__init__.py* para garantir que o diretório tools é tratado como um módulo. Adicionalmente, precisamos de expor os módulos nesse diretório assim:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos continuar a adicionar a este ficheiro à medida que acrescentamos mais ferramentas.

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

Aqui criamos um dicionário com as propriedades:

- name, este é o nome da ferramenta.
- rawSchema, este é o esquema Zod, será usado para validar pedidos que cheguem para chamar esta ferramenta.
- inputSchema, este esquema será usado pelo manipulador.
- callback, este é usado para invocar a ferramenta.

Há também `Tool` que é usado para converter este dicionário num tipo que o manipulador do servidor MCP pode aceitar e fica assim:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

E existe *schema.ts* onde guardamos os esquemas de entrada para cada ferramenta, que parece assim, com apenas um esquema presente mas à medida que adicionamos ferramentas podemos adicionar mais entradas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Ótimo, continuemos para tratar da listagem das ferramentas a seguir.

### -3- Tratar da listagem de ferramentas

De seguida, para tratar da listagem das nossas ferramentas, precisamos de criar um manipulador de pedidos para isso. Eis o que precisamos adicionar ao nosso ficheiro do servidor:

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

Aqui, adicionamos o decorador `@server.list_tools` e a função de implementação `handle_list_tools`. Nesta última, precisamos de produzir uma lista de ferramentas. Note que cada ferramenta deve ter nome, descrição e inputSchema.   

**TypeScript**

Para configurar o manipulador de pedidos para listar as ferramentas, precisamos de chamar `setRequestHandler` no servidor com um esquema adequado ao que queremos fazer, neste caso `ListToolsRequestSchema`. 

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
// código omitido por brevidade
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Retorna a lista de ferramentas registadas
  return {
    tools: tools
  };
});
```

Ótimo, agora que resolvemos a parte da listagem de ferramentas, vejamos como poderíamos estar a chamar ferramentas a seguir.

### -4- Tratar da chamada a uma ferramenta

Para chamar uma ferramenta, precisamos de configurar outro manipulador de pedidos, desta vez focado em tratar um pedido que especifica qual a funcionalidade a chamar e com que argumentos.

**Python**

Vamos usar o decorador `@server.call_tool` e implementar com uma função como `handle_call_tool`. Dentro dessa função, precisamos de extrair o nome da ferramenta, os seus argumentos e garantir que os argumentos são válidos para a ferramenta em questão. Podemos validar os argumentos nesta função ou mais abaixo, na própria ferramenta.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools é um dicionário com os nomes das ferramentas como chaves
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

- O nome da nossa ferramenta já está presente como parâmetro de entrada `name`, que corresponde aos nossos argumentos no dicionário `arguments`.

- A ferramenta é chamada com `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. A validação dos argumentos ocorre na propriedade `handler` que aponta para uma função, se falhar, lançará uma exceção.

Aí está, agora temos uma compreensão completa de como listar e chamar ferramentas usando um servidor de baixo nível.

Veja o [exemplo completo](./code/README.md) aqui

## Tarefa

Expanda o código que lhe foi dado com várias ferramentas, recursos e prompts e reflita sobre como nota que só precisa de adicionar ficheiros na diretoria tools e em mais nenhum lugar. 

*Nenhuma solução fornecida*

## Resumo

Neste capítulo, vimos como funcionava a abordagem de servidor de baixo nível e como isso pode ajudar-nos a criar uma arquitetura agradável que podemos continuar a desenvolver. Também discutimos validação e foi mostrado como trabalhar com bibliotecas de validação para criar esquemas de validação de entrada.

## Próximos passos

- A seguir: [Autenticação simples](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->