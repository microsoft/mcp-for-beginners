# اس نمونے کو چلانا

یہ نمونہ کلائنٹ پر ایک LLM رکھنے سے متعلق ہے۔ LLM کو چاہیے کہ آپ اسے Codespaces میں چلائیں یا GitHub میں ایک ذاتی رسائی ٹوکن سیٹ اپ کریں تاکہ یہ کام کرے۔

## -1- انحصارات انسٹال کریں

```bash
npm install
```

## -3- سرور چلائیں

```bash
npm run build
```

## -4- کلائنٹ چلائیں

```sh
npm run client
```

آپ کو ایک ایسا نتیجہ نظر آئے گا:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔