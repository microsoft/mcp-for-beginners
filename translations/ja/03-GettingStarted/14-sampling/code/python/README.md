# サンプルの実行

> [!WARNING]
> このサンプルは非推奨のSamplingとレガシーなHTTP+SSEエンドポイントを使用しています。これは
> MCP `2025-11-25` の互換性のために残されています。新しい実装ではLLMプロバイダーを直接呼び出し、
> リモートのMCPトラフィックにはStreamable HTTPを使用するべきです。

## 仮想環境の作成

```sh
python -m venv venv
source ./venv/bin/activate
```

## 依存関係のインストール

```sh
pip install "mcp[cli]"
```

## サーバーの起動

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot と VS Codeでサーバーをテストする

mcp.jsonに次のようにエントリを追加します:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

サーバーで「start」をクリックするのを忘れないでください。

GitHub Copilotで次のプロンプトを貼り付けます:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

最初にSamplingアクションの承認を求められ、その後「create_blog」を実行するツールの承認を求められます。以下のような応答が表示されるはずです:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->