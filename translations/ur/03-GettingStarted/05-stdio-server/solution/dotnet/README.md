# MCP stdio سرور - .NET حل

> **⚠️ اہم**: اس حل کو **stdio transport** استعمال کرنے کے لیے اپ ڈیٹ کیا گیا ہے جیسا کہ MCP Specification 2025-06-18 میں تجویز کیا گیا ہے۔ پرانا SSE transport اب ختم کر دیا گیا ہے۔

## جائزہ

یہ .NET حل دکھاتا ہے کہ موجودہ stdio transport استعمال کرتے ہوئے MCP سرور کیسے بنایا جائے۔ stdio transport زیادہ آسان، محفوظ، اور پرانے SSE طریقے کے مقابلے میں بہتر کارکردگی فراہم کرتا ہے۔

## ضروریات

- .NET 9.0 SDK یا اس سے جدید
- .NET dependency injection کی بنیادی سمجھ

## سیٹ اپ ہدایات

### مرحلہ 1: dependencies بحال کریں

```bash
dotnet restore
```

### مرحلہ 2: پروجیکٹ بنائیں

```bash
dotnet build
```

## سرور چلانا

stdio سرور پرانے HTTP-based سرور سے مختلف طریقے سے چلتا ہے۔ ویب سرور شروع کرنے کے بجائے، یہ stdin/stdout کے ذریعے بات چیت کرتا ہے:

```bash
dotnet run
```

**اہم**: سرور "hang" ہوتا ہوا نظر آئے گا - یہ معمول کی بات ہے! یہ stdin سے JSON-RPC پیغامات کا انتظار کر رہا ہے۔

## سرور کی جانچ

### طریقہ 1: MCP Inspector استعمال کرنا (تجویز کردہ)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

یہ کرے گا:
1. آپ کے سرور کو subprocess کے طور پر لانچ کرے گا
2. ٹیسٹنگ کے لیے ویب انٹرفیس کھولے گا
3. آپ کو تمام سرور ٹولز انٹرایکٹیو طور پر ٹیسٹ کرنے کی اجازت دے گا

### طریقہ 2: براہ راست کمانڈ لائن ٹیسٹنگ

آپ Inspector کو براہ راست لانچ کر کے بھی ٹیسٹ کر سکتے ہیں:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### دستیاب ٹولز

سرور یہ ٹولز فراہم کرتا ہے:

- **AddNumbers(a, b)**: دو نمبروں کو جمع کریں
- **MultiplyNumbers(a, b)**: دو نمبروں کو ضرب دیں  
- **GetGreeting(name)**: ایک ذاتی پیغام تیار کریں
- **GetServerInfo()**: سرور کے بارے میں معلومات حاصل کریں

### Claude Desktop کے ساتھ ٹیسٹنگ

اس سرور کو Claude Desktop کے ساتھ استعمال کرنے کے لیے، یہ configuration اپنے `claude_desktop_config.json` میں شامل کریں:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## پروجیکٹ کی ساخت

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE سے اہم فرق

**stdio transport (موجودہ):**
- ✅ آسان سیٹ اپ - ویب سرور کی ضرورت نہیں
- ✅ بہتر سیکیورٹی - کوئی HTTP endpoints نہیں
- ✅ `Host.CreateApplicationBuilder()` استعمال کرتا ہے بجائے `WebApplication.CreateBuilder()` کے
- ✅ `WithStdioTransport()` بجائے `WithHttpTransport()` کے
- ✅ کنسول ایپلیکیشن بجائے ویب ایپلیکیشن کے
- ✅ بہتر کارکردگی

**HTTP/SSE transport (ختم شدہ):**
- ❌ ASP.NET Core ویب سرور کی ضرورت تھی
- ❌ `app.MapMcp()` routing setup کی ضرورت تھی
- ❌ زیادہ پیچیدہ configuration اور dependencies
- ❌ اضافی سیکیورٹی کے مسائل
- ❌ اب MCP 2025-06-18 میں ختم کر دیا گیا ہے

## ترقیاتی خصوصیات

- **Dependency Injection**: خدمات اور لاگنگ کے لیے مکمل DI سپورٹ
- **Structured Logging**: `ILogger<T>` استعمال کرتے ہوئے stderr پر مناسب لاگنگ
- **Tool Attributes**: `[McpServerTool]` attributes استعمال کرتے ہوئے صاف ٹول تعریف
- **Async Support**: تمام ٹولز async آپریشنز سپورٹ کرتے ہیں
- **Error Handling**: غلطیوں کو خوش اسلوبی سے ہینڈل کرنا اور لاگنگ

## ترقیاتی تجاویز

- لاگنگ کے لیے `ILogger` استعمال کریں (stdout پر براہ راست نہ لکھیں)
- ٹیسٹنگ سے پہلے `dotnet build` کے ساتھ بنائیں
- بصری debugging کے لیے Inspector کے ساتھ ٹیسٹ کریں
- تمام لاگنگ خود بخود stderr پر جاتی ہے
- سرور shutdown signals کو خوش اسلوبی سے ہینڈل کرتا ہے

یہ حل موجودہ MCP specification کی پیروی کرتا ہے اور .NET استعمال کرتے ہوئے stdio transport implementation کے بہترین طریقے دکھاتا ہے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔