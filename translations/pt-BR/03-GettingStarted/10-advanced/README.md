# Uso avançado de servidor

Existem dois tipos diferentes de servidores expostos no MCP SDK: o servidor normal e o servidor de baixo nível. Normalmente, você usaria o servidor regular para adicionar funcionalidades. No entanto, em alguns casos, pode ser necessário usar o servidor de baixo nível, como:

- Melhor arquitetura. É possível criar uma arquitetura limpa com ambos os tipos de servidor, mas pode-se argumentar que é um pouco mais fácil com o servidor de baixo nível.
- Disponibilidade de recursos. Alguns recursos avançados só podem ser utilizados com um servidor de baixo nível. Você verá isso em capítulos posteriores, quando adicionarmos amostragem e elicitação.

## Servidor regular vs servidor de baixo nível

Veja como é a criação de um servidor MCP com o servidor regular:

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

A ideia aqui é que você adiciona explicitamente cada ferramenta, recurso ou prompt que deseja que o servidor tenha. Não há nada de errado com isso.

### Abordagem do servidor de baixo nível

No entanto, ao usar a abordagem do servidor de baixo nível, você precisa pensar de forma diferente. Em vez de registrar cada ferramenta, você cria dois manipuladores por tipo de recurso (ferramentas, recursos ou prompts). Por exemplo, para ferramentas, você teria apenas duas funções, como:

- Listar todas as ferramentas. Uma função seria responsável por todas as tentativas de listar ferramentas.
- Manipular chamadas para todas as ferramentas. Aqui também, há apenas uma função lidando com chamadas para uma ferramenta.

Isso parece ser menos trabalho, certo? Em vez de registrar uma ferramenta, basta garantir que ela seja listada ao listar todas as ferramentas e que seja chamada quando houver uma solicitação para utilizá-la.

Vamos dar uma olhada em como o código fica agora:

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

Aqui temos uma função que retorna uma lista de recursos. Cada entrada na lista de ferramentas agora possui campos como `name`, `description` e `inputSchema` para aderir ao tipo de retorno. Isso nos permite colocar nossas definições de ferramentas e recursos em outro lugar. Podemos criar todas as nossas ferramentas em uma pasta de ferramentas e fazer o mesmo para todos os recursos, organizando o projeto da seguinte forma:

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

Isso é ótimo, nossa arquitetura pode ser organizada de forma bastante limpa.

E quanto a chamar ferramentas? É a mesma ideia, um manipulador para chamar qualquer ferramenta? Sim, exatamente, aqui está o código para isso:

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

Como você pode ver no código acima, precisamos analisar qual ferramenta chamar, com quais argumentos, e então prosseguir para chamar a ferramenta.

## Melhorando a abordagem com validação

Até agora, você viu como todas as suas registras para adicionar ferramentas, recursos e prompts podem ser substituídas por esses dois manipuladores por tipo de recurso. O que mais precisamos fazer? Bem, devemos adicionar alguma forma de validação para garantir que a ferramenta seja chamada com os argumentos corretos. Cada runtime tem sua própria solução para isso, por exemplo, Python usa Pydantic e TypeScript usa Zod. A ideia é fazer o seguinte:

- Mover a lógica para criar um recurso (ferramenta, recurso ou prompt) para sua pasta dedicada.
- Adicionar uma forma de validar uma solicitação recebida, como uma chamada para uma ferramenta.

### Criar um recurso

Para criar um recurso, precisamos criar um arquivo para ele e garantir que ele tenha os campos obrigatórios exigidos. Esses campos variam um pouco entre ferramentas, recursos e prompts.

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

Aqui você pode ver como fazemos o seguinte:

- Criamos um esquema usando Pydantic `AddInputModel` com os campos `a` e `b` no arquivo *schema.py*.
- Tentamos analisar a solicitação recebida para ser do tipo `AddInputModel`. Se houver incompatibilidade nos parâmetros, isso causará um erro:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Você pode escolher se deseja colocar essa lógica de análise na própria chamada da ferramenta ou na função manipuladora.

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

- No manipulador que lida com todas as chamadas de ferramentas, tentamos analisar a solicitação recebida no esquema definido da ferramenta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Se isso funcionar, prosseguimos para chamar a ferramenta real:

    ```typescript
    const result = await tool.callback(input);
    ```

Como você pode ver, essa abordagem cria uma ótima arquitetura, pois tudo tem seu lugar. O arquivo *server.ts* é muito pequeno e apenas conecta os manipuladores de solicitação, enquanto cada recurso está em sua respectiva pasta, como tools/, resources/ ou prompts/.

Ótimo, vamos tentar construir isso a seguir.

## Exercício: Criando um servidor de baixo nível

Neste exercício, faremos o seguinte:

1. Criar um servidor de baixo nível que lida com a listagem de ferramentas e chamadas de ferramentas.
1. Implementar uma arquitetura que você possa expandir.
1. Adicionar validação para garantir que as chamadas de ferramentas sejam devidamente validadas.

### -1- Criar uma arquitetura

A primeira coisa que precisamos abordar é uma arquitetura que nos ajude a escalar conforme adicionamos mais recursos. Veja como ela se parece:

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

Agora configuramos uma arquitetura que garante que podemos adicionar novas ferramentas facilmente em uma pasta de ferramentas. Sinta-se à vontade para seguir isso e adicionar subdiretórios para recursos e prompts.

### -2- Criar uma ferramenta

Vamos ver como criar uma ferramenta. Primeiro, ela precisa ser criada em seu subdiretório *tool*, como:

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

Aqui vemos como definimos o nome, descrição, um esquema de entrada usando Pydantic e um manipulador que será invocado quando essa ferramenta for chamada. Por fim, expomos `tool_add`, que é um dicionário contendo todas essas propriedades.

Também há o arquivo *schema.py*, usado para definir o esquema de entrada utilizado pela ferramenta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Também precisamos preencher *__init__.py* para garantir que o diretório de ferramentas seja tratado como um módulo. Além disso, precisamos expor os módulos dentro dele, como:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos continuar adicionando a este arquivo conforme adicionamos mais ferramentas.

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

Aqui criamos um dicionário consistindo de propriedades:

- name: o nome da ferramenta.
- rawSchema: o esquema Zod, usado para validar solicitações recebidas para chamar esta ferramenta.
- inputSchema: o esquema usado pelo manipulador.
- callback: usado para invocar a ferramenta.

Também há `Tool`, usado para converter este dicionário em um tipo que o manipulador do servidor MCP pode aceitar, e ele se parece com:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

E há o arquivo *schema.ts*, onde armazenamos os esquemas de entrada para cada ferramenta. Ele se parece com isso, com apenas um esquema no momento, mas podemos adicionar mais entradas conforme adicionamos ferramentas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Ótimo, vamos prosseguir para lidar com a listagem de nossas ferramentas.

### -3- Lidar com a listagem de ferramentas

Para lidar com a listagem de ferramentas, precisamos configurar um manipulador de solicitações para isso. Veja o que precisamos adicionar ao nosso arquivo de servidor:

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

Aqui adicionamos o decorador `@server.list_tools` e a função implementada `handle_list_tools`. Nesta última, precisamos produzir uma lista de ferramentas. Note como cada ferramenta precisa ter um nome, descrição e inputSchema.

**TypeScript**

Para configurar o manipulador de solicitações para listar ferramentas, precisamos chamar `setRequestHandler` no servidor com um esquema adequado ao que estamos tentando fazer, neste caso `ListToolsRequestSchema`.

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

Ótimo, agora resolvemos a parte de listar ferramentas. Vamos ver como podemos chamar ferramentas a seguir.

### -4- Lidar com chamadas de ferramentas

Para chamar uma ferramenta, precisamos configurar outro manipulador de solicitações, desta vez focado em lidar com uma solicitação que especifica qual recurso chamar e com quais argumentos.

**Python**

Vamos usar o decorador `@server.call_tool` e implementá-lo com uma função como `handle_call_tool`. Dentro dessa função, precisamos analisar o nome da ferramenta, seus argumentos e garantir que os argumentos sejam válidos para a ferramenta em questão. Podemos validar os argumentos nesta função ou mais adiante na própria ferramenta.

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

Aqui está o que acontece:

- O nome da ferramenta já está presente como o parâmetro de entrada `name`, o mesmo vale para os argumentos na forma do dicionário `arguments`.

- A ferramenta é chamada com `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. A validação dos argumentos ocorre na propriedade `handler`, que aponta para uma função. Se isso falhar, uma exceção será levantada.

Pronto, agora temos uma compreensão completa de como listar e chamar ferramentas usando um servidor de baixo nível.

Veja o [exemplo completo](./code/README.md) aqui.

## Tarefa

Expanda o código fornecido com várias ferramentas, recursos e prompts e reflita sobre como você percebe que só precisa adicionar arquivos no diretório de ferramentas e em nenhum outro lugar.

*Sem solução fornecida*

## Resumo

Neste capítulo, vimos como funciona a abordagem do servidor de baixo nível e como ela pode nos ajudar a criar uma arquitetura organizada que podemos continuar expandindo. Também discutimos validação e mostramos como trabalhar com bibliotecas de validação para criar esquemas para validação de entrada.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante estar ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.