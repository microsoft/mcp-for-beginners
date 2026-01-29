# サンプルを実行

## 仮想環境のセットアップ

```sh
python -m venv venv
source ./venv/bin/activate
```

## 依存関係のインストール

```sh
pip install "mcp[cli]"
```

## コードの実行

```sh
python client.py
```

以下のテキストが表示されるはずです:

```text
Available tools: ['add']
Result of add tool: meta=None content=[TextContent(type='text', text='8.0', annotations=None, meta=None)] structuredContent=None isError=False
```

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤解釈について、当方は一切の責任を負いません。