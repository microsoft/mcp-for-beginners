# このサンプルの実行

`uv` のインストールを推奨しますが、必須ではありません。詳しくは [instructions](https://docs.astral.sh/uv/#highlights) をご覧ください。

## -0- 仮想環境の作成

```bash
python -m venv venv
```

## -1- 仮想環境の有効化

```bash
venv\Scrips\activate
```

## -2- 依存関係のインストール

```bash
pip install "mcp[cli]"
```

## -3- サンプルの実行

```bash
python client.py
```

以下のような出力が表示されるはずです：

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。