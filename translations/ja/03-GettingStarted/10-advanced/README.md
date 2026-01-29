# 高度なサーバーの使用方法

MCP SDKでは、通常のサーバーと低レベルサーバーの2種類のサーバーが提供されています。通常は、通常のサーバーを使用して機能を追加します。ただし、以下のような場合には低レベルサーバーを使用することが推奨されます。

- **より良いアーキテクチャ**: 通常のサーバーと低レベルサーバーの両方でクリーンなアーキテクチャを構築することは可能ですが、低レベルサーバーの方がやや簡単であると言えます。
- **機能の利用可能性**: 一部の高度な機能は低レベルサーバーでのみ使用可能です。後の章で、サンプリングやエリシテーションを追加する際にこれを確認できます。

## 通常のサーバー vs 低レベルサーバー

以下は、通常のサーバーを使用してMCPサーバーを作成する例です。

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

この方法では、サーバーに追加したいツール、リソース、プロンプトを明示的に登録します。この方法自体には問題はありません。

### 低レベルサーバーのアプローチ

しかし、低レベルサーバーを使用する場合、考え方が少し異なります。各機能タイプ（ツール、リソース、プロンプト）ごとに2つのハンドラーを作成する必要があります。例えば、ツールの場合、以下のような2つの関数を持つことになります。

- **ツールの一覧表示**: ツールを一覧表示する試みをすべて処理する関数。
- **ツールの呼び出し処理**: ツールを呼び出すリクエストを処理する関数。

これにより、作業量が減るように感じられるかもしれません。ツールを登録する代わりに、ツールが一覧表示されることと、ツール呼び出しリクエストが処理されることを確認するだけで済みます。

コードがどのように見えるか見てみましょう。

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

ここでは、機能のリストを返す関数を作成しています。ツールリストの各エントリには、`name`、`description`、`inputSchema`といったフィールドが含まれており、返り値の型に準拠しています。この方法により、ツールや機能の定義を別の場所に移動できます。ツールをすべてtoolsフォルダーに作成し、他の機能も同様に整理することで、プロジェクトを以下のように構成できます。

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

これにより、アーキテクチャが非常にクリーンになります。

ツールの呼び出しについても同じ考え方で、どのツールでも1つのハンドラーで処理するのでしょうか？その通りです。以下はそのコード例です。

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

上記のコードでは、呼び出すツールとその引数を解析し、その後ツールを呼び出す処理を行っています。

## アプローチの改善: バリデーションの追加

これまで、ツール、リソース、プロンプトを追加するための登録を各機能タイプごとの2つのハンドラーに置き換える方法を見てきました。次に必要なのは何でしょうか？ツールが正しい引数で呼び出されることを確認するためのバリデーションを追加するべきです。各ランタイムには独自のソリューションがあります。例えば、PythonではPydanticを使用し、TypeScriptではZodを使用します。このアイデアは以下の通りです。

- 機能（ツール、リソース、プロンプト）を作成するロジックを専用のフォルダーに移動する。
- ツールを呼び出すリクエストなどを検証する方法を追加する。

### 機能の作成

機能を作成するには、その機能専用のファイルを作成し、必要なフィールドを含める必要があります。フィールドはツール、リソース、プロンプトによって少し異なります。

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

ここでは以下のことを行っています。

- *schema.py*ファイルでPydanticの`AddInputModel`を使用してフィールド`a`と`b`を持つスキーマを作成。
- リクエストを`AddInputModel`型に解析しようと試み、パラメータが一致しない場合はクラッシュします。

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

この解析ロジックをツール呼び出し自体に含めるか、ハンドラー関数に含めるかは選択できます。

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

- ツール呼び出しを処理するハンドラーでは、リクエストをツールの定義されたスキーマに解析しようとします。

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    これが成功すれば、実際のツールを呼び出します。

    ```typescript
    const result = await tool.callback(input);
    ```

このアプローチにより、すべてが整理され、*server.ts*ファイルはリクエストハンドラーを接続するだけの非常に小さなファイルとなり、各機能はそれぞれのフォルダー（tools/、resources/、prompts/）に配置されます。

素晴らしいですね。次にこれを構築してみましょう。

## 演習: 低レベルサーバーの作成

この演習では以下を行います。

1. ツールの一覧表示と呼び出しを処理する低レベルサーバーを作成する。
1. 拡張可能なアーキテクチャを実装する。
1. ツール呼び出しが適切に検証されるようにバリデーションを追加する。

### -1- アーキテクチャの作成

まず、機能を追加する際にスケールしやすいアーキテクチャを構築する必要があります。以下がその例です。

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

これで、toolsフォルダーに新しいツールを簡単に追加できるアーキテクチャが設定されました。リソースやプロンプトのサブディレクトリを追加することもできます。

### -2- ツールの作成

次に、ツールを作成する方法を見てみましょう。まず、ツールを*tool*サブディレクトリに作成する必要があります。

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

ここでは、名前、説明、Pydanticを使用した入力スキーマ、ツールが呼び出された際に実行されるハンドラーを定義しています。最後に、これらのプロパティを保持する辞書`tool_add`を公開します。

また、ツールで使用する入力スキーマを定義するための*schema.py*も必要です。

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

さらに、toolsディレクトリをモジュールとして扱うために*__init__.py*を更新し、内部のモジュールを公開する必要があります。

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

新しいツールを追加するたびにこのファイルを更新できます。

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

ここでは以下のプロパティを持つ辞書を作成します。

- **name**: ツールの名前。
- **rawSchema**: Zodスキーマ。ツール呼び出しリクエストを検証するために使用されます。
- **inputSchema**: ハンドラーで使用されるスキーマ。
- **callback**: ツールを呼び出すために使用されます。

また、この辞書をMCPサーバーハンドラーが受け入れる型に変換する`Tool`も作成します。

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

さらに、各ツールの入力スキーマを格納する*schema.ts*も作成します。現在は1つのスキーマしかありませんが、ツールを追加するたびにエントリを増やすことができます。

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

素晴らしいですね。次はツールの一覧表示を処理する方法を見てみましょう。

### -3- ツールの一覧表示を処理する

次に、ツールの一覧表示を処理するためのリクエストハンドラーを設定します。以下をサーバーファイルに追加します。

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

ここでは、デコレーター`@server.list_tools`と実装関数`handle_list_tools`を追加しています。後者では、ツールのリストを生成する必要があります。各ツールには`name`、`description`、`inputSchema`が必要です。

**TypeScript**

ツールの一覧表示を処理するリクエストハンドラーを設定するには、サーバーで`setRequestHandler`を呼び出し、`ListToolsRequestSchema`に適合するスキーマを指定します。

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

これでツールの一覧表示部分が解決しました。次はツールの呼び出し方法を見てみましょう。

### -4- ツールの呼び出しを処理する

ツールを呼び出すには、どの機能をどの引数で呼び出すかを指定するリクエストを処理するためのリクエストハンドラーを設定する必要があります。

**Python**

デコレーター`@server.call_tool`を使用し、`handle_call_tool`のような関数で実装します。この関数内で、ツール名とその引数を解析し、引数がツールに適しているかを確認します。引数の検証はこの関数内で行うか、ツール内で行うか選択できます。

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

ここで行われていることは以下の通りです。

- ツール名は入力パラメータ`name`として既に存在しており、引数は`arguments`辞書として存在しています。
- ツールは`result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`で呼び出されます。引数の検証は`handler`プロパティが指す関数内で行われ、失敗すると例外が発生します。

これで、低レベルサーバーを使用してツールの一覧表示と呼び出しを完全に理解できました。

[完全な例](./code/README.md)はこちらをご覧ください。

## 課題

提供されたコードを拡張して、複数のツール、リソース、プロンプトを追加し、toolsディレクトリにファイルを追加するだけで済むことを確認してください。

*解答はありません*

## まとめ

この章では、低レベルサーバーのアプローチがどのように機能するかを学び、それが拡張可能なアーキテクチャの構築にどのように役立つかを確認しました。また、バリデーションについて議論し、入力検証のためのスキーマを作成する方法を示しました。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当社は責任を負いません。