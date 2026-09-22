# إعداد عملاء المضيفين الشائعين لـ MCP

> [!NOTE]
> تكوينات المضيف التي تشير إلى `/sse` هي أمثلة قديمة لـ HTTP+SSE لـ
> MCP `2025-11-25`. بالنسبة لـ MCP `2026-07-28`، اختر HTTP القابل للبث في المضيفين الذين
> يدعمونه واستخدم نقطة النهاية التي يضبطها الخادم.

يغطي هذا الدليل كيفية تكوين واستخدام خوادم MCP مع تطبيقات مضيف الذكاء الاصطناعي الشائعة. لكل مضيف نهج التكوين الخاص به، لكن بمجرد الإعداد، كلها تتواصل مع خوادم MCP باستخدام البروتوكول الموحد.

## ما هو المضيف MCP؟

**المضيف MCP** هو تطبيق ذكاء اصطناعي يمكنه الاتصال بخوادم MCP لتوسيع قدراته. فكّر فيه كـ "الواجهة الأمامية" التي يتفاعل معها المستخدمون، بينما توفر خوادم MCP الأدوات والبيانات في "الواجهة الخلفية".

```mermaid
flowchart LR
    User[👤 المستخدم] --> Host[🖥️ مضيف MCP]
    Host --> S1[خادم MCP أ]
    Host --> S2[خادم MCP ب]
    Host --> S3[خادم MCP ج]
    
    subgraph "المضيفون الشائعون"
        H1[كلود سطح المكتب]
        H2[VS كود]
        H3[كورسر]
        H4[كلاين]
        H5[ويندسيرف]
    end
```

## المتطلبات الأساسية

- خادم MCP للاتصال به (راجع [الوحدة 3.1 - الخادم الأول](../01-first-server/README.md))
- تطبيق المضيف مثبت على نظامك
- دراية أساسية بملفات تكوين JSON

---

## 1. Claude Desktop

**Claude Desktop** هو تطبيق سطح مكتب رسمي من Anthropic يدعم MCP بشكل أصلي.

### التثبيت

1. حمّل Claude Desktop من [claude.ai/download](https://claude.ai/download)
2. قم بالتثبيت وسجّل الدخول باستخدام حساب Anthropic الخاص بك

### التكوين

يستخدم Claude Desktop ملف تكوين JSON لتعريف خوادم MCP.

**موقع ملف التكوين:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**مثال على التكوين:**

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

### خيارات التكوين

| الحقل | الوصف | مثال |
|-------|-------------|---------|
| `command` | البرنامج التنفيذي للتشغيل | `"python"`, `"node"`, `"npx"` |
| `args` | معطيات سطر الأوامر | `["-m", "my_server"]` |
| `env` | متغيرات البيئة | `{"API_KEY": "xxx"}` |
| `cwd` | دليل العمل | `"/path/to/server"` |

### اختبار إعدادك

1. احفظ ملف التكوين
2. أعد تشغيل Claude Desktop بالكامل (اغلق وأعد فتح التطبيق)
3. افتح محادثة جديدة
4. ابحث عن أيقونة 🔌 التي تشير إلى وجود خوادم متصلة
5. حاول أن تطلب من Claude استخدام أحد أدواتك

### استكشاف أخطاء Claude Desktop

**الخادم لا يظهر:**
- تحقق من صحة ملف التكوين باستخدام مدقق JSON
- تأكد من أن مسار الأمر صحيح
- تحقق من سجلات Claude Desktop: المساعدة → عرض السجلات

**توقف الخادم عند بدء التشغيل:**
- اختبر الخادم يدويًا في الطرفية أولاً
- تحقق من إعداد متغيرات البيئة بشكل صحيح
- تأكد من تثبيت جميع التبعيات

---

## 2. VS Code مع GitHub Copilot

يدعم VS Code MCP من خلال امتدادات GitHub Copilot Chat.

### المتطلبات الأساسية

1. تثبيت VS Code 1.99 أو أحدث
2. تثبيت امتداد GitHub Copilot
3. تثبيت امتداد GitHub Copilot Chat

### التكوين

يستخدم VS Code ملف `.vscode/mcp.json` في مساحة العمل أو في إعدادات المستخدم.

**تكوين مساحة العمل** (`.vscode/mcp.json`):

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

**إعدادات المستخدم** (`settings.json`):

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

### استخدام MCP في VS Code

1. افتح لوحة محادثة Copilot (Ctrl+Shift+I / Cmd+Shift+I)
2. اكتب `@` لرؤية الأدوات المتاحة من MCP
3. استخدم اللغة الطبيعية لاستدعاء الأدوات: "احسب 25 * 48 باستخدام الآلة الحاسبة"

### استكشاف أخطاء VS Code

**خوادم MCP لا يتم تحميلها:**
- تحقق من لوحة الإخراج → "MCP" لمعرفة سجلات الأخطاء
- أعد تحميل النافذة: Ctrl+Shift+P → "المطور: إعادة تحميل النافذة"
- تحقق من أن الخادم يعمل بشكل منفرد أولاً

---

## 3. Cursor

**Cursor** هو محرر كود موجه للذكاء الاصطناعي مع دعم مدمج لـ MCP.

### التثبيت

1. حمّل Cursor من [cursor.sh](https://cursor.sh)
2. قم بالتثبيت وسجّل الدخول

### التكوين

يستخدم Cursor تنسيق تكوين مشابه لـ Claude Desktop.

**موقع ملف التكوين:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**مثال على التكوين:**

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

### استخدام MCP في Cursor

1. افتح دردشة AI في Cursor (Ctrl+L / Cmd+L)
2. تظهر أدوات MCP تلقائيًا في الاقتراحات
3. اطلب من الذكاء الاصطناعي أداء المهام باستخدام الخوادم المتصلة

---

## 4. Cline (مستند إلى الطرفية)

**Cline** هو عميل MCP يعتمد على الطرفية، مثالي لتدفقات العمل القائمة على سطر الأوامر.

### التثبيت

```bash
npm install -g @anthropic/cline
```

### التكوين

يستخدم Cline متغيرات البيئة ومعطيات سطر الأوامر.

**استخدام متغيرات البيئة:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**استخدام معطيات سطر الأوامر:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**ملف التكوين** (`~/.clinerc`):

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

### استخدام Cline

```bash
# بدء جلسة تفاعلية
cline

# استعلام فردي مع MCP
cline "Calculate the square root of 144 using the calculator"

# قائمة بالأدوات المتاحة
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** هو محرر كود مدعوم بالذكاء الاصطناعي مع دعم MCP.

### التثبيت

1. قم بتنزيل Windsurf من [codeium.com/windsurf](https://codeium.com/windsurf)
2. قم بالتثبيت وأنشئ حسابًا

### التكوين

يتم إدارة تكوين Windsurf عبر واجهة إعدادات المستخدم:

1. افتح الإعدادات (Ctrl+, / Cmd+,)
2. ابحث عن "MCP"
3. انقر على "تحرير في settings.json"

**مثال على التكوين:**

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

## مقارنة أنواع النقل

تدعم المضيفات آليات نقل مختلفة:

| المضيف | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (الإدخال/الإخراج القياسي): الأفضل للخوادم المحلية التي يبدأها المضيف
**SSE/HTTP**: الأفضل للخوادم البعيدة أو الخوادم المشتركة بين عدة عملاء

---

## حل المشاكل الشائعة

### الخادم لا يبدأ

1. **اختبر الخادم يدويًا أولاً:**
   ```bash
   # لبايثون
   python -m your_server_module
   
   # لنود.جي اس
   node /path/to/server/index.js
   ```

2. **تحقق من مسار الأمر:**
   - استخدم المسارات المطلقة قدر الإمكان
   - تأكد من وجود البرنامج التنفيذي ضمن PATH الخاص بك

3. **تحقق من التبعيات:**
   ```bash
   # بايثون
   pip list | grep mcp
   
   # نود.جي إس
   npm list @modelcontextprotocol/sdk
   ```

### يتصل الخادم ولكن الأدوات لا تعمل

1. **تحقق من سجلات الخادم** - معظم المضيفين لديهم خيارات للتسجيل
2. **تحقق من تسجيل الأدوات** - استخدم MCP Inspector للاختبار
3. **تحقق من الأذونات** - بعض الأدوات تحتاج إلى وصول إلى الملفات أو الشبكة

### متغيرات البيئة لم تنقل

- بعض المضيفين يعقمون متغيرات البيئة
- استخدم حقل `env` في التكوين صراحة
- تجنب وضع بيانات حساسة في ملفات التكوين (استخدم إدارة الأسرار)

---

## أفضل ممارسات الأمان

1. **لا تلتزم مطلقًا بمفاتيح API** في ملفات التكوين
2. **استخدم متغيرات البيئة** للبيانات الحساسة
3. **حدد أذونات الخادم** فقط على ما هو ضروري
4. **راجع كود الخادم** قبل منح الوصول إلى نظامك
5. **استخدم قوائم السماح** للوصول إلى نظام الملفات والشبكة

---

## ما التالي

- [3.13 - التصحيح باستخدام MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - أنشئ خادم MCP الأول الخاص بك](../01-first-server/README.md)
- [الوحدة 5 - مواضيع متقدمة](../../05-AdvancedTopics/README.md)

---

## موارد إضافية

- [وثائق Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [امتداد VS Code MCP](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [مواصفات MCP - وسائل النقل](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [السجل الرسمي لخوادم MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->