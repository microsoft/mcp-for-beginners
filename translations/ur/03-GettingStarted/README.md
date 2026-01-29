## شروع کریں  

[![اپنا پہلا MCP سرور بنائیں](../../../translated_images/ur/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(اوپر دی گئی تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھ سکیں)_

یہ سیکشن کئی اسباق پر مشتمل ہے:

- **1 آپ کا پہلا سرور**، اس پہلے سبق میں، آپ سیکھیں گے کہ اپنا پہلا سرور کیسے بنائیں اور اسے انسپکٹر ٹول کے ذریعے جانچیں، جو آپ کے سرور کو ٹیسٹ اور ڈیبگ کرنے کا ایک قیمتی طریقہ ہے، [سبق دیکھیں](01-first-server/README.md)

- **2 کلائنٹ**، اس سبق میں، آپ سیکھیں گے کہ ایسا کلائنٹ کیسے لکھا جائے جو آپ کے سرور سے جڑ سکے، [سبق دیکھیں](02-client/README.md)

- **3 LLM کے ساتھ کلائنٹ**، کلائنٹ لکھنے کا ایک اور بہتر طریقہ یہ ہے کہ اس میں LLM شامل کریں تاکہ وہ آپ کے سرور کے ساتھ "بات چیت" کر سکے کہ کیا کرنا ہے، [سبق دیکھیں](03-llm-client/README.md)

- **4 Visual Studio Code میں GitHub Copilot Agent موڈ کے ساتھ سرور کا استعمال**۔ یہاں، ہم Visual Studio Code کے اندر سے اپنا MCP سرور چلانے پر غور کریں گے، [سبق دیکھیں](04-vscode/README.md)

- **5 stdio Transport Server**۔ stdio transport موجودہ وضاحت میں MCP سرور سے کلائنٹ کمیونیکیشن کے لیے تجویز کردہ معیار ہے، جو محفوظ سب پروسیس پر مبنی کمیونیکیشن فراہم کرتا ہے، [سبق دیکھیں](05-stdio-server/README.md)

- **6 MCP کے ساتھ HTTP Streaming (Streamable HTTP)**۔ جدید HTTP اسٹریمنگ، پروگریس نوٹیفکیشنز، اور Streamable HTTP کا استعمال کرتے ہوئے قابل پیمائش، ریئل ٹائم MCP سرورز اور کلائنٹس کو نافذ کرنے کے بارے میں جانیں۔ [سبق دیکھیں](06-http-streaming/README.md)

- **7 VSCode کے لیے AI Toolkit کا استعمال**۔ اپنے MCP کلائنٹس اور سرورز کو استعمال کرنے اور ٹیسٹ کرنے کے لیے [سبق دیکھیں](07-aitk/README.md)

- **8 ٹیسٹنگ**۔ یہاں ہم خاص طور پر اس پر توجہ دیں گے کہ ہم مختلف طریقوں سے اپنے سرور اور کلائنٹ کو کیسے ٹیسٹ کر سکتے ہیں، [سبق دیکھیں](08-testing/README.md)

- **9 ڈیپلائمنٹ**۔ یہ باب آپ کے MCP حلوں کو مختلف طریقوں سے ڈیپلائے کرنے پر غور کرے گا، [سبق دیکھیں](09-deployment/README.md)

- **10 ایڈوانسڈ سرور استعمال**۔ یہ باب ایڈوانسڈ سرور کے استعمال کا احاطہ کرتا ہے، [سبق دیکھیں](./10-advanced/README.md)

- **11 Auth**۔ یہ باب سادہ Auth شامل کرنے کا احاطہ کرتا ہے، Basic Auth سے لے کر JWT اور RBAC کے استعمال تک۔ آپ کو یہاں سے شروع کرنے کی ترغیب دی جاتی ہے اور پھر باب 5 میں ایڈوانسڈ موضوعات کو دیکھیں اور باب 2 میں دی گئی سفارشات کے ذریعے اضافی سیکیورٹی سختی کریں، [سبق دیکھیں](./11-simple-auth/README.md)

Model Context Protocol (MCP) ایک اوپن پروٹوکول ہے جو اس بات کو معیاری بناتا ہے کہ ایپلیکیشنز LLMs کو کانٹیکسٹ کیسے فراہم کرتی ہیں۔ MCP کو AI ایپلیکیشنز کے لیے USB-C پورٹ کی طرح سمجھیں - یہ AI ماڈلز کو مختلف ڈیٹا سورسز اور ٹولز سے جوڑنے کا ایک معیاری طریقہ فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ قابل ہوں گے:

- C#, Java, Python, TypeScript، اور JavaScript میں MCP کے لیے ڈیولپمنٹ ماحول قائم کریں
- کسٹم فیچرز (resources, prompts، اور tools) کے ساتھ بنیادی MCP سرورز بنائیں اور ڈیپلائے کریں
- میزبان ایپلیکیشنز بنائیں جو MCP سرورز سے جڑ سکیں
- MCP implementations کو ٹیسٹ اور ڈیبگ کریں
- عام سیٹ اپ چیلنجز اور ان کے حل کو سمجھیں
- اپنی MCP implementations کو مشہور LLM سروسز سے جوڑیں

## اپنا MCP ماحول قائم کرنا

MCP کے ساتھ کام شروع کرنے سے پہلے، یہ ضروری ہے کہ آپ اپنا ڈیولپمنٹ ماحول تیار کریں اور بنیادی ورک فلو کو سمجھیں۔ یہ سیکشن آپ کو ابتدائی سیٹ اپ کے مراحل کے ذریعے رہنمائی کرے گا تاکہ MCP کے ساتھ ایک ہموار آغاز یقینی بنایا جا سکے۔

### ضروریات

MCP ڈیولپمنٹ میں جانے سے پہلے، یقینی بنائیں کہ آپ کے پاس:

- **ڈیولپمنٹ ماحول**: آپ کی منتخب کردہ زبان کے لیے (C#, Java, Python, TypeScript، یا JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm، یا کوئی بھی جدید کوڈ ایڈیٹر
- **پیکیج مینیجرز**: NuGet, Maven/Gradle, pip، یا npm/yarn
- **API Keys**: کسی بھی AI سروسز کے لیے جو آپ اپنی میزبان ایپلیکیشنز میں استعمال کرنے کا ارادہ رکھتے ہیں

### آفیشل SDKs

آنے والے ابواب میں آپ Python, TypeScript, Java اور .NET کا استعمال کرتے ہوئے بنائے گئے حل دیکھیں گے۔ یہاں تمام آفیشل سپورٹڈ SDKs ہیں۔

MCP کئی زبانوں کے لیے آفیشل SDKs فراہم کرتا ہے:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft کے تعاون سے برقرار رکھا گیا
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI کے تعاون سے برقرار رکھا گیا
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - آفیشل TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - آفیشل Python implementation
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - آفیشل Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI کے تعاون سے برقرار رکھا گیا
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - آفیشل Rust implementation

## اہم نکات

- MCP ڈیولپمنٹ ماحول قائم کرنا زبان کے مخصوص SDKs کے ساتھ آسان ہے
- MCP سرورز بنانا واضح اسکیموں کے ساتھ ٹولز بنانے اور رجسٹر کرنے پر مشتمل ہے
- MCP کلائنٹس سرورز اور ماڈلز سے جڑتے ہیں تاکہ اضافی صلاحیتوں سے فائدہ اٹھا سکیں
- قابل اعتماد MCP implementations کے لیے ٹیسٹنگ اور ڈیبگنگ ضروری ہیں
- ڈیپلائمنٹ کے اختیارات مقامی ڈیولپمنٹ سے لے کر کلاؤڈ پر مبنی حل تک ہیں

## مشق کرنا

ہمارے پاس نمونوں کا ایک سیٹ ہے جو اس سیکشن کے تمام ابواب میں آپ کو نظر آنے والے مشقوں کی تکمیل کرتا ہے۔ اس کے علاوہ، ہر باب کے اپنے مشقیں اور اسائنمنٹس بھی ہیں۔

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## اضافی وسائل

- [Azure پر Model Context Protocol کا استعمال کرتے ہوئے ایجنٹس بنائیں](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps کے ساتھ Remote MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## آگے کیا ہے

اگلا: [اپنا پہلا MCP سرور بنانا](01-first-server/README.md)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔