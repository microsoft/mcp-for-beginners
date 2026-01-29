# Model Context Protocol (MCP) Python 実装

このリポジトリには、Model Context Protocol (MCP) のPython実装が含まれており、MCP標準を使って通信するサーバーとクライアントアプリケーションの作成方法を示しています。

## 概要

MCPの実装は主に2つのコンポーネントで構成されています：

1. **MCPサーバー (`server.py`)** - 以下を提供するサーバー：
   - **Tools**：リモートで呼び出せる関数
   - **Resources**：取得可能なデータ
   - **Prompts**：言語モデル用のプロンプトテンプレート

2. **MCPクライアント (`client.py`)** - サーバーに接続し、その機能を利用するクライアントアプリケーション

## 機能

この実装では、MCPの主要な機能をいくつか示しています：

### Tools
- `completion` - AIモデルからテキスト補完を生成（シミュレーション）
- `add` - 2つの数字を加算するシンプルな計算機

### Resources
- `models://` - 利用可能なAIモデルの情報を返す
- `greeting://{name}` - 指定した名前に対するパーソナライズされた挨拶を返す

### Prompts
- `review_code` - コードレビュー用のプロンプトを生成

## インストール

このMCP実装を使うには、必要なパッケージをインストールしてください：

```powershell
pip install mcp-server mcp-client
```

## サーバーとクライアントの起動

### サーバーの起動

別のターミナルでサーバーを起動します：

```powershell
python server.py
```

MCP CLIを使って開発モードでサーバーを起動することもできます：

```powershell
mcp dev server.py
```

または、Claude Desktopにインストールして起動することも可能です（利用可能な場合）：

```powershell
mcp install server.py
```

### クライアントの起動

別のターミナルでクライアントを起動します：

```powershell
python client.py
```

これによりサーバーに接続し、利用可能なすべての機能を実演します。

### クライアントの使い方

クライアント (`client.py`) はMCPの全機能を示しています：

```powershell
python client.py
```

これによりサーバーに接続し、tools、resources、promptsを含むすべての機能を利用します。出力には以下が表示されます：

1. 計算機ツールの結果（5 + 7 = 12）
2. 「What is the meaning of life?」に対するcompletionツールの応答
3. 利用可能なAIモデルの一覧
4. 「MCP Explorer」へのパーソナライズされた挨拶
5. コードレビュー用のプロンプトテンプレート

## 実装の詳細

サーバーは`FastMCP` APIを使って実装されており、MCPサービスを定義するための高レベルの抽象化を提供します。以下はツールの定義例です：

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

クライアントはMCPクライアントライブラリを使ってサーバーに接続し、呼び出します：

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## 詳しく知るには

MCPの詳細については、以下を参照してください： https://modelcontextprotocol.io/

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。