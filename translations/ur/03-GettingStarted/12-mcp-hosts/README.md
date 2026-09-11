# مقبول MCP ہوسٹ کلائنٹس کی ترتیب

> [!NOTE]
> وہ ہوسٹ کنفیگریشنز جو `/sse` کی طرف اشارہ کرتی ہیں وہ MCP `2025-11-25` کے لیے پرانی HTTP+SSE مثالیں ہیں۔ MCP `2026-07-28` کے لیے، ان ہوسٹس میں جو اس کی حمایت کرتے ہیں، Streamable HTTP منتخب کریں اور سرور کے ذریعہ کنفیگرڈ اینڈپوائنٹ استعمال کریں۔
> 
>

یہ رہنما مقبول AI ہوسٹ ایپلیکیشنز کے ساتھ MCP سرورز کو کنفیگر کرنے اور استعمال کرنے کا طریقہ بتاتی ہے۔ ہر ہوسٹ اپنی کنفیگریشن کا طریقہ رکھتا ہے، لیکن ایک بار ترتیب دینے کے بعد، وہ سب MCP سرورز کے ساتھ معیاری پروٹوکول کا استعمال کرتے ہوئے رابطہ کرتے ہیں۔

## MCP ہوسٹ کیا ہے؟

ایک **MCP ہوسٹ** ایک AI ایپلیکیشن ہے جو MCP سرورز سے جڑ سکتی ہے تاکہ اپنی صلاحیتوں کو بڑھایا جا سکے۔ اسے "فرنٹ اینڈ" سمجھیں جس سے صارفین تعامل کرتے ہیں، جبکہ MCP سرور "بیک اینڈ" ٹولز اور ڈیٹا فراہم کرتے ہیں۔

```mermaid
flowchart LR
    User[👤 صارف] --> Host[🖥️ MCP میزبان]
    Host --> S1[MCP سرور A]
    Host --> S2[MCP سرور B]
    Host --> S3[MCP سرور C]
    
    subgraph "مقبول میزبان"
        H1[کلاؤڈ ڈیسک ٹاپ]
        H2[VS کوڈ]
        H3[کرسر]
        H4[کلائن]
        H5[ونڈسرف]
    end
```

## ضروریات

- ایک MCP سرور جس سے جڑنا ہو (دیکھیے [ماڈیول 3.1 - پہلا سرور](../01-first-server/README.md))
- آپ کے نظام پر ہوسٹ ایپلیکیشن نصب ہو
- JSON کنفیگریشن فائلوں کی بنیادی واقفیت

---

## 1۔ کلاؤڈ ڈیسک ٹاپ

**کلاؤڈ ڈیسک ٹاپ** Anthropics کی سرکاری ڈیسک ٹاپ ایپلیکیشن ہے جو MCP کو قدرتی طور پر سپورٹ کرتی ہے۔

### تنصیب

1۔ [claude.ai/download](https://claude.ai/download) سے کلاؤڈ ڈیسک ٹاپ ڈاؤن لوڈ کریں
2۔ انسٹال کریں اور اپنے Anthropic اکاؤنٹ سے سائن ان ہوں

### کنفیگریشن

کلاؤڈ ڈیسک ٹاپ MCP سرورز متعین کرنے کے لیے JSON کنفیگریشن فائل استعمال کرتا ہے۔

**کنفیگریشن فائل کا مقام:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**مثال کنفیگریشن:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### کنفیگریشن اختیارات

| فیلڈ | وضاحت | مثال |
|-------|-------------|---------|
| `command` | چلانے والا قابلِ عمل پروگرام | `"python"`, `"node"`, `"npx"` |
| `args` | کمانڈ لائن آرگیومنٹس | `["-m", "my_server"]` |
| `env` | ماحولیاتی متغیرات | `{"API_KEY": "xxx"}` |
| `cwd` | ورکنگ ڈائریکٹری | `"/path/to/server"` |

### اپنی ترتیب کی جانچ کریں

1۔ کنفیگریشن فائل محفوظ کریں
2۔ کلاؤڈ ڈیسک ٹاپ کو مکمل طور پر دوبارہ شروع کریں (بند کریں اور دوبارہ کھولیں)
3۔ نیا گفتگو کھولیں
4۔ جڑے ہوئے سرورز کی نشاندہی کے لیے 🔌 آئکن دیکھیں
5۔ کلاؤڈ سے کہیں کہ آپ کے ٹولز میں سے کسی ایک کا استعمال کرے

### کلاؤڈ ڈیسک ٹاپ کی خرابی کا ازالہ

**سرور ظاہر نہیں ہو رہا:**
- JSON ویلڈیٹر سے کنفیگریشن فائل کا نحو چیک کریں
- کمانڈ کے راستے کی درستگی یقینی بنائیں
- کلاؤڈ ڈیسک ٹاپ کے لاگز چیک کریں: Help → Show Logs

**شروع کرنے پر سرور کریش ہو رہا ہے:**
- سب سے پہلے ٹرمینل میں دستی طور پر سرور آزمانے کی کوشش کریں
- ماحولیاتی متغیرات کی درست سیٹنگ چیک کریں
- تمام انحصارات کی تنصیب یقینی بنائیں

---

## 2۔ VS کوڈ اور GitHub Copilot

VS کوڈ MCP کو GitHub Copilot Chat ایکسٹینشنز کے ذریعے سپورٹ کرتا ہے۔

### ضروریات

1۔ VS کوڈ 1.99+ انسٹال کیا ہوا ہو
2۔ GitHub Copilot ایکسٹینشن انسٹال ہو
3۔ GitHub Copilot Chat ایکسٹینشن انسٹال ہو

### کنفیگریشن

VS کوڈ آپ کے ورک اسپیس یا یوزر سیٹنگز میں `.vscode/mcp.json` استعمال کرتا ہے۔

**ورک اسپیس کنفیگریشن** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**یوزر سیٹنگز** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### VS کوڈ میں MCP کا استعمال

1۔ Copilot Chat پینل کھولیں (Ctrl+Shift+I / Cmd+Shift+I)
2۔ دستیاب MCP ٹولز دیکھنے کے لیے `@` ٹائپ کریں
3۔ ٹولز چلانے کے لیے قدرتی زبان استعمال کریں: "کیلکولیٹر کا استعمال کرتے ہوئے 25 * 48 کا حساب لگائیں"

### VS کوڈ کی خرابی کا ازالہ

**MCP سرور لوڈ نہیں ہو رہے:**
- آؤٹ پٹ پینل → "MCP" میں ایرر لاگز چیک کریں
- ونڈو کو ری لوڈ کریں: Ctrl+Shift+P → "Developer: Reload Window"
- سب سے پہلے یہ یقینی بنائیں کہ سرور خود چل رہا ہے

---

## 3۔ کرسر

**کرسر** ایک AI پر مبنی کوڈ ایڈیٹر ہے جس میں MCP کی بلٹ ان سپورٹ ہے۔

### تنصیب

1۔ [cursor.sh](https://cursor.sh) سے کرسر ڈاؤن لوڈ کریں
2۔ انسٹال کریں اور سائن ان ہوں

### کنفیگریشن

کرسر کلاؤڈ ڈیسک ٹاپ کے مماثل کنفیگریشن فارمیٹ استعمال کرتا ہے۔

**کنفیگریشن فائل کا مقام:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**مثال کنفیگریشن:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### کرسر میں MCP کا استعمال

1۔ کرسر کی AI چیٹ کھولیں (Ctrl+L / Cmd+L)
2۔ MCP ٹولز آٹومیٹک مشوروں میں ظاہر ہوتے ہیں
3۔ AI سے جڑے ہوئے سرورز کے ذریعے کام کرنے کو کہیں

---

## 4۔ کلائن (ٹرمینل پر مبنی)

**کلائن** ایک ٹرمینل پر مبنی MCP کلائنٹ ہے، جو کمانڈ لائن کے کام کے لیے مثالی ہے۔

### تنصیب

```bash
npm install -g @anthropic/cline
```

### کنفیگریشن

کلائن ماحولیاتی متغیرات اور کمانڈ لائن آرگیومنٹس استعمال کرتا ہے۔

**ماحولیاتی متغیرات کا استعمال:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**کمانڈ لائن آرگیومنٹس کا استعمال:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**کنفیگریشن فائل** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### کلائن کا استعمال

```bash
# ایک تفاعلی سیشن شروع کریں
cline

# MCP کے ساتھ واحد سوال
cline "Calculate the square root of 144 using the calculator"

# دستیاب ٹولز کی فہرست بنائیں
cline --list-tools
```

---

## 5۔ ونڈسرف

**ونڈسرف** ایک اور AI پر مبنی کوڈ ایڈیٹر ہے جس میں MCP کی سپورٹ موجود ہے۔

### تنصیب

1۔ [codeium.com/windsurf](https://codeium.com/windsurf) سے ونڈسرف ڈاؤن لوڈ کریں
2۔ انسٹال کریں اور اکاؤنٹ بنائیں

### کنفیگریشن

ونڈسرف کی کنفیگریشن سیٹنگز UI کے ذریعے منظم ہوتی ہے:

1۔ سیٹنگز کھولیں (Ctrl+, / Cmd+,)
2۔ "MCP" تلاش کریں
3۔ "Edit in settings.json" پر کلک کریں

**مثال کنفیگریشن:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## ٹرانسپورٹ اقسام کا موازنہ

مختلف ہوسٹس مختلف ٹرانسپورٹ میکانزم کو سپورٹ کرتے ہیں:

| ہوسٹ | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| کلاؤڈ ڈیسک ٹاپ | ✅ | ❌ | ❌ |
| VS کوڈ | ✅ | ✅ | ❌ |
| کرسر | ✅ | ✅ | ❌ |
| کلائن | ✅ | ✅ | ❌ |
| ونڈسرف | ✅ | ✅ | ❌ |

**stdio** (معیاری ان پٹ/آؤٹ پٹ): مقامی سرورز کیلئے بہترین جو ہوسٹ کے ذریعہ شروع کیے جائیں
**SSE/HTTP**: دور دراز کے سرورز یا متعدد کلائنٹس کے درمیان مشترکہ سرورز کے لیے بہترین

---

## عام خرابیوں کا ازالہ

### سرور شروع نہیں ہوتا

1۔ **سب سے پہلے سرور کو دستی طور پر آزمائیں:**
   ```bash
   # پائتھن کے لیے
   python -m your_server_module
   
   # نوڈ.جے ایس کے لیے
   node /path/to/server/index.js
   ```

2۔ **کمانڈ کے راستے کی جانچ کریں:**
   - اگر ممکن ہو تو مکمل راستے استعمال کریں
   - یقینی بنائیں کہ قابلِ عمل پروگرام آپ کے PATH میں ہے

3۔ **انحصارات کی تصدیق کریں:**
   ```bash
   # پایتھن
   pip list | grep mcp
   
   # نوڈ.جے‌ایس
   npm list @modelcontextprotocol/sdk
   ```

### سرور جڑ تو جاتا ہے لیکن ٹول کام نہیں کرتے

1۔ **سرور کے لاگز چیک کریں** - زیادہ تر ہوسٹس لاگنگ کے اختیارات رکھتے ہیں
2۔ **ٹول کی رجسٹریشن کی تصدیق کریں** - MCP انسپکٹر سے ٹیسٹ کریں
3۔ **اجازتوں کی جانچ کریں** - بعض ٹولز کو فائل/نیٹ ورک کی رسائی کی ضرورت ہوتی ہے

### ماحولیاتی متغیرات منتقل نہیں ہوتے

- کچھ ہوسٹس ماحولیاتی متغیرات کو صاف کرتے ہیں
- وضاحتی طور پر `env` کنفیگریشن فیلڈ استعمال کریں
- کنفیگریشن فائلوں میں حساس ڈیٹا سے گریز کریں (راز مینجمنٹ استعمال کریں)

---

## سیکیورٹی کی بہترین مشقیں

1۔ **کسی بھی کنفیگریشن فائل میں API کیز کو کبھی کمٹ نہ کریں**
2۔ **حساس معلومات کے لیے ماحولیاتی متغیرات کا استعمال کریں**
3۔ **سرور کی اجازتوں کو صرف ضروریات تک محدود کریں**
4۔ **اپنے نظام تک رسائی دینے سے پہلے سرور کوڈ کا جائزہ لیں**
5۔ **فائل سسٹم اور نیٹ ورک رسائی کے لیے الرٹ لسٹ استعمال کریں**

---

## آگے کیا ہے

- [3.13 - MCP انسپکٹر کے ساتھ خرابی تلاش کرنا](../13-mcp-inspector/README.md)
- [3.1 - اپنا پہلا MCP سرور بنائیں](../01-first-server/README.md)
- [ماڈیول 5 - جدید موضوعات](../../05-AdvancedTopics/README.md)

---

## اضافی ذرائع

- [کلاؤڈ ڈیسک ٹاپ MCP دستاویزات](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS کوڈ MCP ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP وضاحت - ٹرانسپورٹس](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [سرکاری MCP سرورز رجسٹری](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->