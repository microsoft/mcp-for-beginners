# Uso avançado do servidor

Existem dois tipos diferentes de servidores expostos no MCP SDK, seu servidor normal e o servidor de baixo nível. Normalmente, você usaria o servidor regular para adicionar recursos a ele. Mas em alguns casos, você quer depender do servidor de baixo nível, como por exemplo:

- Arquitetura melhor. É possível criar uma arquitetura limpa com tanto o servidor regular quanto um servidor de baixo nível, mas pode-se argumentar que é ligeiramente mais fácil com um servidor de baixo nível.
- Disponibilidade de recursos. Alguns recursos avançados só podem ser usados com um servidor de baixo nível. Você verá isso em capítulos posteriores quando adicionarmos amostragem e elicitação.

## Servidor regular vs servidor de baixo nível

Veja como é a criação de um Servidor MCP com o servidor regular

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

A questão é que você adiciona explicitamente cada ferramenta, recurso ou prompt que deseja que o servidor tenha. Não há nada de errado nisso.

### Abordagem do servidor de baixo nível

No entanto, quando você usa a abordagem do servidor de baixo nível, você precisa pensar de forma diferente. Em vez de registrar cada ferramenta, você cria dois manipuladores por tipo de recurso (ferramentas, recursos ou prompts). Por exemplo, as ferramentas agora têm apenas duas funções assim:

- Listar todas as ferramentas. Uma função seria responsável por todas as tentativas de listar ferramentas.
- Lidar com chamadas a todas as ferramentas. Aqui também, há apenas uma função lidando com chamadas a uma ferramenta.

Parece que dá menos trabalho, certo? Então, em vez de registrar uma ferramenta, só preciso garantir que a ferramenta esteja listada quando eu listar todas as ferramentas e que ela seja chamada quando houver uma solicitação para chamar uma ferramenta.

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
  // Retorna a lista de ferramentas registradas
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

Aqui agora temos uma função que retorna uma lista de recursos. Cada entrada na lista de ferramentas agora tem campos como `name`, `description` e `inputSchema` para aderir ao tipo de retorno. Isso nos permite colocar nossas ferramentas e definição de recursos em outro lugar. Agora podemos criar todas as nossas ferramentas em uma pasta tools e o mesmo vale para todos os seus recursos, assim seu projeto pode ser organizado assim:

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

Isso é ótimo, nossa arquitetura pode ficar bem limpa.

E quanto a chamar ferramentas, é a mesma ideia então, um manipulador para chamar qualquer ferramenta? Sim, exatamente, aqui está o código para isso:

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

Como você pode ver pelo código acima, precisamos analisar qual ferramenta chamar e com quais argumentos, e então precisamos seguir para chamar a ferramenta.

## Melhorando a abordagem com validação

Até agora, você viu como todos os seus registros para adicionar ferramentas, recursos e prompts podem ser substituídos por esses dois manipuladores por tipo de recurso. O que mais precisamos fazer? Bem, devemos adicionar algum tipo de validação para garantir que a ferramenta seja chamada com os argumentos corretos. Cada runtime tem sua própria solução para isso, por exemplo Python usa Pydantic e TypeScript usa Zod. A ideia é que façamos o seguinte:

- Mover a lógica para criar um recurso (ferramenta, recurso ou prompt) para sua pasta dedicada.
- Adicionar uma forma de validar uma solicitação recebida pedindo, por exemplo, para chamar uma ferramenta.

### Criar um recurso

Para criar um recurso, precisaremos criar um arquivo para esse recurso e garantir que ele tenha os campos obrigatórios requeridos para esse recurso. Os campos diferem um pouco entre ferramentas, recursos e prompts.

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
        # Validar entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adicionar Pydantic, para que possamos criar um AddInputModel e validar os argumentos

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

aqui você pode ver como fazemos o seguinte:

- Criar um esquema usando Pydantic `AddInputModel` com os campos `a` e `b` no arquivo *schema.py*.
- Tentar analisar a solicitação recebida para ser do tipo `AddInputModel`, se houver incompatibilidade nos parâmetros isso vai falhar:

   ```python
   # add.py
    try:
        # Validar entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Você pode escolher colocar essa lógica de análise na própria chamada da ferramenta ou na função do manipulador.

**TypeScript**

```typescript
// servidor.ts
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

// esquema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// adicionar.ts
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

- No manipulador lidando com todas as chamadas de ferramentas, agora tentamos analisar a solicitação recebida conforme o esquema definido da ferramenta:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    se isso funcionar, então prosseguimos para chamar a ferramenta real:

    ```typescript
    const result = await tool.callback(input);
    ```

Como você pode ver, essa abordagem cria uma ótima arquitetura pois tudo tem seu lugar, o *server.ts* é um arquivo muito pequeno que apenas conecta os manipuladores de requisição e cada recurso está em sua respectiva pasta, ou seja, tools/, resources/ ou /prompts.

Ótimo, vamos tentar construir isso a seguir.

## Exercício: Criando um servidor de baixo nível

Neste exercício, faremos o seguinte:

1. Criar um servidor de baixo nível que lide com a listagem de ferramentas e chamadas de ferramentas.
1. Implementar uma arquitetura na qual você possa construir em cima.
1. Adicionar validação para garantir que suas chamadas de ferramentas sejam validadas corretamente.

### -1- Criar uma arquitetura

A primeira coisa que precisamos abordar é uma arquitetura que nos ajude a escalar à medida que adicionamos mais recursos, veja como fica:

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

Agora definimos uma arquitetura que garante que podemos adicionar facilmente novas ferramentas em uma pasta tools. Sinta-se à vontade para seguir isso e adicionar subdiretórios para resources e prompts.

### -2- Criando uma ferramenta

Vamos ver como criar uma ferramenta a seguir. Primeiro, ela precisa ser criada em seu subdiretório *tool* assim:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validar entrada usando modelo Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adicionar Pydantic, para que possamos criar um AddInputModel e validar os argumentos

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Aqui vemos como definimos nome, descrição e esquema de entrada usando Pydantic e um manipulador que será invocado quando essa ferramenta for chamada. Por fim, expomos `tool_add`, que é um dicionário contendo todas essas propriedades.

Também temos *schema.py* que é usado para definir o esquema de entrada usado pela nossa ferramenta:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Também precisamos preencher *__init__.py* para garantir que o diretório tools seja tratado como um módulo. Além disso, precisamos expor os módulos dentro dele assim:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Podemos continuar adicionando a esse arquivo conforme adicionamos mais ferramentas.

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

Aqui criamos um dicionário composto das propriedades:

- name, esse é o nome da ferramenta.
- rawSchema, esse é o esquema Zod, que será usado para validar solicitações recebidas para chamar essa ferramenta.
- inputSchema, esse esquema será usado pelo manipulador.
- callback, isso é usado para invocar a ferramenta.

Também existe o `Tool` que é usado para converter esse dicionário em um tipo que o manipulador do servidor mcp pode aceitar, e fica assim:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

E há *schema.ts* onde armazenamos os esquemas de entrada para cada ferramenta, que fica assim com apenas um esquema no momento, mas conforme adicionamos ferramentas podemos adicionar mais entradas:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Ótimo, vamos prosseguir para lidar com a listagem das nossas ferramentas a seguir.

### -3- Lidar com listagem de ferramentas

Em seguida, para lidar com a listagem das nossas ferramentas, precisamos configurar um manipulador de requisição para isso. Veja o que precisamos adicionar ao nosso arquivo do servidor:

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

Aqui, adicionamos o decorador `@server.list_tools` e a função de implementação `handle_list_tools`. Nesta última, precisamos gerar uma lista de ferramentas. Note que cada ferramenta precisa ter um name, description e inputSchema.

**TypeScript**

Para configurar o manipulador de requisição para listar ferramentas, precisamos chamar `setRequestHandler` no servidor com um esquema adequado ao que estamos tentando fazer, neste caso `ListToolsRequestSchema`.

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
  // Retorna a lista de ferramentas registradas
  return {
    tools: tools
  };
});
```

Ótimo, agora resolvemos a parte de listar ferramentas, vamos ver como poderíamos chamar ferramentas a seguir.

### -4- Lidar com chamada de uma ferramenta

Para chamar uma ferramenta, precisamos configurar outro manipulador de requisição, desta vez focado em lidar com uma solicitação especificando qual recurso chamar e com quais argumentos.

**Python**

Vamos usar o decorador `@server.call_tool` e implementá-lo com uma função como `handle_call_tool`. Dentro dessa função, precisamos analisar o nome da ferramenta, seu argumento e garantir que os argumentos sejam válidos para a ferramenta em questão. Podemos validar os argumentos nesta função ou depois, na própria ferramenta.

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

- O nome da ferramenta já está presente como o parâmetro de entrada `name`, e os argumentos estão no dicionário `arguments`.

- A ferramenta é chamada com `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. A validação dos argumentos acontece na propriedade `handler` que aponta para uma função, se isso falhar ela lançará uma exceção.

Pronto, agora temos um entendimento completo de listar e chamar ferramentas usando um servidor de baixo nível.

Veja o [exemplo completo](./code/README.md) aqui

## Tarefa

Estenda o código que você recebeu com diversas ferramentas, recursos e prompts e reflita sobre como você percebe que só precisa adicionar arquivos no diretório tools e em nenhum outro lugar.

*Nenhuma solução fornecida*

## Resumo

Neste capítulo, vimos como funciona a abordagem do servidor de baixo nível e como isso pode nos ajudar a criar uma arquitetura bacana para continuarmos construindo. Também discutimos validação e foi mostrado como trabalhar com bibliotecas de validação para criar esquemas para validação de entrada.

## O que vem a seguir

- Próximo: [Autenticação Simples](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->