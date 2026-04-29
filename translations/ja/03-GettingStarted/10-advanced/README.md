# 高度なサーバーの使用方法

MCP SDKには、通常のサーバーと低レベルサーバーの2種類のサーバーが用意されています。通常は、機能を追加するために通常のサーバーを使用します。しかし、次のような場合には低レベルサーバーに頼りたいことがあります。

- より良いアーキテクチャ。通常のサーバーと低レベルサーバーの両方でクリーンなアーキテクチャを作成することは可能ですが、低レベルサーバーの方がわずかに簡単だと議論することができます。
- 機能の利用可能性。高度な機能の一部は低レベルサーバーでのみ使用できます。後の章でサンプリングや引き出しを追加する際にこれを確認します。

## 通常のサーバー vs 低レベルサーバー

通常のサーバーでMCPサーバーを作成するコードは次のようになります。

**Python**

```python
mcp = FastMCP("Demo")

# 加算ツールを追加する
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

// 追加ツールを追加する
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

要点は、サーバーに持たせたいツール、リソース、プロンプトを明示的にそれぞれ追加することです。それ自体は問題ありません。

### 低レベルサーバーのアプローチ

しかし、低レベルサーバーのアプローチを使う場合は別の考え方が必要です。各ツールを登録する代わりに、機能タイプ（ツール、リソース、プロンプト）ごとに2つのハンドラーを作成します。例えばツールの場合は以下の2つの関数だけになります。

- 全ツールを一覧表示する。全てのツール一覧取得の試みに対して1つの関数が担当します。
- 全てのツール呼び出しを処理する。ツールを呼び出す要求を処理する関数も1つだけです。

これなら作業が減りそうですよね？つまり、ツールを登録する代わりに、ツール一覧取得時にツールが挙がるようにし、ツール呼び出し要求が来たときに該当ツールが呼ばれることを確実にすれば良いのです。

コードは次のようになります。

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
  // 登録されたツールのリストを返します
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

ここでは、機能のリストを返す関数があります。toolsリストの各エントリは`name`、`description`、`inputSchema`などのフィールドを持ち、返却型に準拠しています。これにより、ツールや機能定義を別の場所に置くことが可能になります。これでツールはtoolsフォルダにまとめられるようになり、他の機能も同様に整理され、プロジェクトは次のようになります。

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

素晴らしいです。これでアーキテクチャをかなりクリーンにできます。

ツールを呼び出すのはどうでしょう？同じ考え方で、1つのハンドラーでどのツールでも呼び出せますか？そうです、その通りです。次にそのコードです。

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools はツール名をキーとする辞書です
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
    // TODO ツールを呼び出す、

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

上記コードの通り、呼び出すツールと引数をパースし、その後ツールを呼び出す必要があります。

## バリデーションによるアプローチの改善

ここまでで、ツール、リソース、プロンプト追加の登録はすべてタイプごとに2つのハンドラーに置き換えられることを見てきました。ではその他に何が必要でしょう？ツールを正しい引数で呼び出しているかを保証するためのバリデーションが必要です。各環境は独自の解決策を持っています。例えばPythonはPydantic、TypeScriptはZodを使用します。考え方は以下です。

- 機能（ツール、リソース、プロンプト）作成のロジックを専用フォルダへ移動する。
- 例えばツール呼び出し要求があった際に、その引数が正しいか検証できるようにする。

### 機能を作成する

機能を作成するには、その機能用のファイルを作り、必須フィールドを含める必要があります。ツール、リソース、プロンプトで必須フィールドは多少異なります。

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
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticを追加して、AddInputModelを作成し、引数を検証できるようにする

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ここでは以下を行っています。

- Pydanticの`AddInputModel`スキーマを<em>schema.py</em>ファイル内で作成し、`a`と`b`フィールドを定義。
- 受け取ったリクエストを`AddInputModel`型としてパースを試み、パラメータに不一致があればエラーとなります。

   ```python
   # add.py
    try:
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

このパース処理をツール呼び出しの中で行うか、ハンドラー関数内で行うかは選べます。

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

- 全ツール呼び出しを扱うハンドラー内で、入ってきたリクエストをツールが定義するスキーマにパースを試みます。

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

上手くいけば実際のツール呼び出しに進みます。

    ```typescript
    const result = await tool.callback(input);
    ```

この方法により、すべてが自分の場所を持ち、<em>server.ts</em>はリクエストハンドラーの配線のみ行う非常に小さなファイルとなり、各機能がそれぞれのフォルダ（tools/、resources/、prompts/）に整理される優れたアーキテクチャになります。

さあ、これを実際に構築してみましょう。

## 演習: 低レベルサーバーの作成

この演習では以下を行います。

1. ツールの一覧取得および呼び出しを扱う低レベルサーバーを作成する。
2. 発展させていけるアーキテクチャを実装する。
3. ツール呼び出しのバリデーションを追加して正しく検証できるようにする。

### -1- アーキテクチャの作成

まずは、機能を追加していく際にスケールしやすいアーキテクチャを用意します。以下のようになります。

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

これでtoolsフォルダに新しいツールを簡単に追加できるアーキテクチャが設定できました。resourcesやpromptsのためにサブディレクトリを追加しても構いません。

### -2- ツールを作成する

次にツール作成です。まず<em>tool</em>サブディレクトリに作成します。

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydanticモデルを使用して入力を検証する
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydanticを追加して、AddInputModelを作成し、引数を検証できるようにする

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ここではPydanticを使い、name、description、input schemaを定義し、呼び出されたときに呼ばれるハンドラーも用意しています。最後に`tool_add`という辞書にこれらのプロパティをまとめて公開しています。

また、ツール用の入力スキーマを定義する<em>schema.py</em>もあります。

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

<em>__init__.py</em>も埋めてtoolsディレクトリをモジュールと認識させる必要があります。さらに中のモジュールを外部に公開するために次のようにします。

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ツールが増えたらこのファイルにも追記していきます。

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

こちらでは以下のプロパティを持つ辞書を作成しています。

- name: ツールの名前
- rawSchema: Zodのスキーマで、ツール呼び出し時のリクエストを検証するために使います
- inputSchema: ハンドラーで使うスキーマ
- callback: ツールを実行する関数

また、この辞書をmcpサーバーハンドラーが受け入れられる型に変換する`Tool`があります。

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

そして<em>schema.ts</em>には各ツールの入力スキーマを格納しており、現時点では1つだけですが、ツール追加に応じて増やせます。

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

では次にツール一覧の処理を取り扱いましょう。

### -3- ツール一覧の処理

ツールの一覧情報を扱うリクエストハンドラーをセットアップします。サーバーファイルに次を追加しましょう。

**Python**

```python
# 簡潔にするためコードを省略しました
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

`@server.list_tools`デコレーターを追加し、`handle_list_tools`関数を実装します。この関数はツールの一覧を返す必要があり、各ツールはname、description、inputSchemaを持つ必要があります。

**TypeScript**

ツール一覧のリクエストハンドラーをセットアップするには、`setRequestHandler`を呼び、取扱うスキーマとして`ListToolsRequestSchema`を指定します。

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
// 簡潔にするためコードを省略
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // 登録されているツールの一覧を返す
  return {
    tools: tools
  };
});
```

これでツール一覧の取得部分が完成しました。続いてツール呼び出しの処理を見てみましょう。

### -4- ツール呼び出しの処理

ツール呼び出しのためのリクエストハンドラーを用意します。これはどの機能を呼び、どの引数を使うかが指定された要求を処理します。

**Python**

`@server.call_tool`デコレーターを使い、`handle_call_tool`関数として実装します。この中でツール名とパラメータをパースし、ツールが受け入れる引数かどうか検証します。検証はここで行っても実際のツール内部で行っても構いません。

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # toolsは、ツール名をキーとする辞書です
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ツールを呼び出す
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

処理の流れは次の通りです。

- ツール名はすでに`name`パラメータにあります。引数は`arguments`辞書として渡されます。
- ツールは`result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`で呼び出します。引数の検証は`handler`プロパティの関数内で行われ、失敗すると例外が発生します。

これで低レベルサーバーを用いたツール一覧と呼び出しについて理解できました。

[完全な例](./code/README.md)をご覧ください。

## 課題

与えられたコードにいくつかのツール、リソース、プロンプトを追加し、ツールディレクトリにファイルを追加するだけで他は触らずに済むことを体感してください。

<em>解答はありません</em>

## まとめ

この章では低レベルサーバーのアプローチとそれがどのようにクリーンなアーキテクチャ作成に役立つかを見ました。またバリデーションについても説明し、スキーマによる入力の検証方法を紹介しました。

## 次にやること

- 次: [簡易認証](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご理解ください。原文の母国語での文書が正式な情報源と見なされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じる誤解や解釈の相違について、当方は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->