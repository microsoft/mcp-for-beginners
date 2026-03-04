## آغاز کرنا  

[![اپنا پہلا MCP سرور بنائیں](../../../translated_images/ur/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

یہ سیکشن کئی اسباق پر مشتمل ہے:

- **1 آپ کا پہلا سرور**، اس پہلے سبق میں، آپ سیکھیں گے کہ اپنا پہلا سرور کیسے بنانا ہے اور اسے انسپکٹر ٹول کے ذریعے جانچنا ہے، جو کہ آپ کے سرور کو جانچنے اور ڈیبگ کرنے کا ایک قیمتی طریقہ ہے، [سبق پر جائیں](01-first-server/README.md)

- **2 کلائنٹ**، اس سبق میں، آپ سیکھیں گے کہ ایک کلائنٹ کیسے لکھا جائے جو آپ کے سرور سے جڑ سکے، [سبق پر جائیں](02-client/README.md)

- **3 LLM کے ساتھ کلائنٹ**، کلائنٹ لکھنے کا ایک بہتر طریقہ یہ ہے کہ اس میں LLM شامل کریں تاکہ یہ آپ کے سرور کے ساتھ "مذاکرہ" کر سکے کہ کیا کرنا ہے، [سبق پر جائیں](03-llm-client/README.md)

- **4 ویژوئل اسٹوڈیو کوڈ میں سرور GitHub کوپائلٹ ایجنٹ موڈ کا استعمال**۔ یہاں، ہم ویژوئل اسٹوڈیو کوڈ کے اندر اپنے MCP سرور کو چلانے کا طریقہ دیکھ رہے ہیں، [سبق پر جائیں](04-vscode/README.md)

- **5 stdio ٹرانسپورٹ سرور** stdio ٹرانسپورٹ مقامی MCP سرور-کلائنٹ کمیونیکیشن کے لیے تجویز کردہ معیار ہے، جو محفوظ subprocess-based رابطہ کاری اور پروسیس علیحدگی فراہم کرتا ہے، [سبق پر جائیں](05-stdio-server/README.md)

- **6 MCP کے ساتھ HTTP اسٹریمنگ (Streamable HTTP)**۔ جدید HTTP اسٹریمنگ ٹرانسپورٹ کے بارے میں جانیں (جو دور دراز MCP سرورز کے لیے تجویز کردہ طریقہ ہے جیسا کہ [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http) میں ذکر ہے)، پیش رفت کی اطلاعات، اور اسٹریمیبل HTTP استعمال کرتے ہوئے وسیع پیمانے پر حقیقی وقت کے MCP سرورز اور کلائنٹس کیسے بنائیں۔ [سبق پر جائیں](06-http-streaming/README.md)

- **7 VSCode کے لیے AI ٹول کٹ کا استعمال** تاکہ آپ اپنے MCP کلائنٹس اور سرورز کو استعمال اور ٹیسٹ کر سکیں، [سبق پر جائیں](07-aitk/README.md)

- **8 ٹیسٹنگ**۔ یہاں ہم خاص طور پر دیکھیں گے کہ کیسے ہم اپنے سرور اور کلائنٹ کو مختلف طریقوں سے ٹیسٹ کر سکتے ہیں، [سبق پر جائیں](08-testing/README.md)

- **9 تعیناتی**۔ اس باب میں آپ کے MCP حلوں کو تعینات کرنے کے مختلف طریقے دیکھے جائیں گے، [سبق پر جائیں](09-deployment/README.md)

- **10 اعلی درجے کا سرور کا استعمال**۔ یہ باب اعلی درجے کے سرور کے استعمال کا احاطہ کرتا ہے، [سبق پر جائیں](./10-advanced/README.md)

- **11 توثیق**۔ یہ باب سادہ توثیق کے اضافے کے بارے میں ہے، Basic Auth سے لے کر JWT اور RBAC کے استعمال تک۔ یہاں شروع کرنے کی تجویز دی جاتی ہے اور پھر باب 5 کے اعلی درجے کے موضوعات میں دیکھیں اور باب 2 کی سفارشات کے ذریعے مزید سیکیورٹی مضبوطی کریں، [سبق پر جائیں](./11-simple-auth/README.md)

- **12 MCP ہوسٹ**۔ مقبول MCP ہوسٹ کلائنٹس جیسے Claude Desktop، Cursor، Cline، اور Windsurf کو ترتیب دیں اور استعمال کریں۔ ٹرانسپورٹ اقسام اور مسائل حل کرنے کا طریقہ جانیں، [سبق پر جائیں](./12-mcp-hosts/README.md)

- **13 MCP انسپکٹر**۔ MCP انسپکٹر ٹول کا استعمال کرتے ہوئے اپنے MCP سرورز کو انٹرایکٹیولی ڈیبگ اور ٹیسٹ کریں۔ ٹربل شوٹنگ ٹولز، وسائل، اور پروٹوکول پیغاموں کو سیکھیں، [سبق پر جائیں](./13-mcp-inspector/README.md)

- **14 سیمپلنگ**۔ MCP سرورز بنائیں جو LLM سے متعلقہ کاموں پر MCP کلائنٹس کے ساتھ تعاون کرتے ہیں۔ [سبق پر جائیں](./14-sampling/README.md)

- **15 MCP ایپس**۔ MCP سرورز بنائیں جو UI ہدایات کے ساتھ بھی جواب دیتے ہیں، [سبق پر جائیں](./15-mcp-apps/README.md)

ماڈل کانٹیکسٹ پروٹوکول (MCP) ایک کھلا پروٹوکول ہے جو یہ معیاری بناتا ہے کہ ایپلی کیشنز LLMs کو کس طرح کانٹیکسٹ فراہم کرتی ہیں۔ MCP کو AI ایپلی کیشنز کے لیے USB-C پورٹ کی طرح سمجھیں - یہ AI ماڈلز کو مختلف ڈیٹا ذرائع اور ٹولز سے جوڑنے کا معیاری طریقہ فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے آخر تک، آپ قابل ہوں گے کہ:

- C#, Java, Python, TypeScript، اور JavaScript میں MCP کے لیے ترقیاتی ماحول ترتیب دیں
- کسٹم خصوصیات (وسائل، پرامپٹس، اور ٹولز) کے ساتھ بنیادی MCP سرورز تیار کریں اور تعینات کریں
- ہوسٹ ایپلی کیشنز بنائیں جو MCP سرورز سے جڑتی ہیں
- MCP اطلاقات کو ٹیسٹ اور ڈیبگ کریں
- عام سیٹ اپ چیلنجز اور ان کے حل سمجھیں
- اپنے MCP اطلاقات کو مقبول LLM خدمات سے جوڑیں

## اپنے MCP ماحول کی ترتیب

MCP کے ساتھ کام شروع کرنے سے پہلے، اپنے ترقیاتی ماحول کو تیار کرنا اور بنیادی ورک فلو کو سمجھنا ضروری ہے۔ یہ سیکشن آپ کو ابتدائی سیٹ اپ اقدامات سے لے کر MCP کے ساتھ ہموار آغاز کرنے میں رہنمائی کرے گا۔

### بنیادی ضروریات

MCP کی ترقی میں کودنے سے پہلے، یقینی بنائیں کہ آپ کے پاس ہے:

- **ترقیاتی ماحول**: اپنی منتخب شدہ زبان کے لیے (C#, Java, Python, TypeScript، یا JavaScript)
- **IDE/ایڈیٹر**: Visual Studio، Visual Studio Code، IntelliJ، Eclipse، PyCharm، یا کوئی جدید کوڈ ایڈیٹر
- **پیکیج مینیجرز**: NuGet، Maven/Gradle، pip، یا npm/yarn
- **API کیز**: کسی بھی AI خدمات کے لیے جو آپ اپنی ہوسٹ ایپلی کیشنز میں استعمال کرنے کا ارادہ رکھتے ہیں

### سرکاری SDKs

آنے والے ابواب میں آپ Python، TypeScript، Java، اور .NET استعمال کرتے ہوئے حل دیکھیں گے۔ یہاں تمام سرکاری طور پر حمایت یافتہ SDKs موجود ہیں۔

MCP متعدد زبانوں کے لیے سرکاری SDKs فراہم کرتا ہے (جو [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) کے مطابق ہیں):
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - مائیکروسافٹ کے ساتھ تعاون میں دیکھ بھال کی جاتی ہے
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI کے ساتھ تعاون میں دیکھ بھال کی جاتی ہے
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - سرکاری TypeScript نفاذ
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - سرکاری Python نفاذ (FastMCP)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - سرکاری Kotlin نفاذ
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI کے ساتھ تعاون میں دیکھ بھال کی جاتی ہے
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - سرکاری Rust نفاذ
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - سرکاری Go نفاذ

## اہم نکات

- MCP ترقیاتی ماحول کی ترتیب زبان کے مخصوص SDKs کے ساتھ آسان ہے
- MCP سرور بنانے میں واضح اسکیموں کے ساتھ ٹولز تیار کرنا اور رجسٹر کرنا شامل ہے
- MCP کلائنٹس سرورز اور ماڈلز سے جڑ کر اضافی صلاحیتوں کا فائدہ اٹھاتے ہیں
- ٹیسٹنگ اور ڈیبگنگ MCP اطلاقات کی قابل اعتماد کارکردگی کے لیے ضروری ہے
- تعیناتی کے اختیارات مقامی ترقی سے کلاؤڈ پر مبنی حل تک ہوتے ہیں

## مشق کرنا

ہمارے پاس نمونہ جات کا ایک مجموعہ ہے جو آپ کو اس سیکشن کے تمام ابواب میں دیکھنے والی مشقوں کے ساتھ مکمل کرتے ہیں۔ علاوہ ازیں ہر باب میں اپنی مشقیں اور اسائنمنٹ بھی ہیں

- [Java کیلکولیٹر](./samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../03-GettingStarted/samples/csharp)
- [JavaScript کیلکولیٹر](./samples/javascript/README.md)
- [TypeScript کیلکولیٹر](./samples/typescript/README.md)
- [Python کیلکولیٹر](../../../03-GettingStarted/samples/python)

## اضافی وسائل

- [Azure پر Model Context Protocol استعمال کرتے ہوئے Agents بنائیں](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps کے ساتھ دور دراز MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## آگے کیا ہے

پہلے سبق سے شروع کریں: [اپنا پہلا MCP سرور بنانا](01-first-server/README.md)

اس ماڈیول کو مکمل کرنے کے بعد، جاری رکھیں: [ماڈیول 4: عملی نفاذ](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->