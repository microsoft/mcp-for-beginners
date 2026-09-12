# راه‌اندازی کلاینت‌های محبوب میزبان MCP

> [!NOTE]
> پیکربندی‌های میزبان که به `/sse` اشاره می‌کنند نمونه‌های قدیمی HTTP+SSE برای
> MCP `2025-11-25` هستند. برای MCP `2026-07-28`، در میزبان‌هایی که
> از آن پشتیبانی می‌کنند Streamable HTTP را انتخاب کرده و از نقطه پایانی تنظیم‌شده توسط سرور استفاده کنید.

این راهنما نحوه پیکربندی و استفاده از سرورهای MCP با برنامه‌های محبوب هوش مصنوعی را پوشش می‌دهد. هر میزبان رویکرد پیکربندی خاص خود را دارد، اما پس از راه‌اندازی، همه آنها از طریق پروتکل استاندارد با سرورهای MCP ارتباط برقرار می‌کنند.

## میزبان MCP چیست؟

یک **میزبان MCP** برنامه‌ای هوش مصنوعی است که می‌تواند به سرورهای MCP متصل شود تا قابلیت‌های خود را گسترش دهد. آن را به عنوان "رابط کاربری" که کاربران با آن تعامل دارند در نظر بگیرید، در حالی که سرورهای MCP ابزارها و داده‌های "پشت‌صحنه" را فراهم می‌کنند.

```mermaid
flowchart LR
    User[👤 کاربر] --> Host[🖥️ میزبان MCP]
    Host --> S1[سرور MCP A]
    Host --> S2[سرور MCP B]
    Host --> S3[سرور MCP C]
    
    subgraph "میزبان‌های محبوب"
        H1[کلود دسکتاپ]
        H2[وی‌اس کد]
        H3[کورسر]
        H4[کلاین]
        H5[ویندسورف]
    end
```

## پیش‌نیازها

- یک سرور MCP برای اتصال (به [Module 3.1 - First Server](../01-first-server/README.md) مراجعه کنید)
- برنامه میزبان روی سیستم شما نصب شده باشد
- آشنایی پایه با فایل‌های پیکربندی JSON

---

## 1. Claude Desktop

**Claude Desktop** برنامه رسمی دسکتاپ Anthropic است که به‌طور بومی از MCP پشتیبانی می‌کند.

### نصب

1. Claude Desktop را از [claude.ai/download](https://claude.ai/download) دانلود کنید
2. نصب و ورود با حساب Anthropic خود

### پیکربندی

Claude Desktop از یک فایل پیکربندی JSON برای تعریف سرورهای MCP استفاده می‌کند.

**محل فایل پیکربندی:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**نمونه پیکربندی:**

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

### گزینه‌های پیکربندی

| فیلد | شرح | مثال |
|-------|-------------|---------|
| `command` | اجرایی که باید اجرا شود | `"python"`, `"node"`, `"npx"` |
| `args` | آرگومان‌های خط فرمان | `["-m", "my_server"]` |
| `env` | متغیرهای محیطی | `{"API_KEY": "xxx"}` |
| `cwd` | دایرکتوری کاری | `"/path/to/server"` |

### آزمایش راه‌اندازی شما

1. فایل پیکربندی را ذخیره کنید
2. Claude Desktop را کاملاً ری‌استارت کنید (خروج و بازگشایی مجدد)
3. یک مکالمه جدید باز کنید
4. به دنبال آیکون 🔌 باشید که نشان‌دهنده سرورهای متصل است
5. سعی کنید از Claude بخواهید یکی از ابزارهای شما را استفاده کند

### عیب‌یابی Claude Desktop

**عدم نمایش سرور:**
- نحوه نوشتار فایل پیکربندی را با یک اعتبارسنج JSON بررسی کنید
- مسیر فرمان را بررسی کنید که صحیح باشد
- لاگ‌های Claude Desktop را چک کنید: Help → Show Logs

**کرش سرور هنگام راه‌اندازی:**
- ابتدا سرور خود را به‌صورت دستی در ترمینال تست کنید
- مطمئن شوید متغیرهای محیطی به درستی تنظیم شده‌اند
- مطمئن شوید همه وابستگی‌ها نصب شده‌اند

---

## 2. VS Code با GitHub Copilot

VS Code از طریق افزونه‌های GitHub Copilot Chat از MCP پشتیبانی می‌کند.

### پیش‌نیازها

1. نصب نسخه 1.99+ VS Code
2. نصب افزونه GitHub Copilot
3. نصب افزونه GitHub Copilot Chat

### پیکربندی

VS Code از `.vscode/mcp.json` در فضای کاری یا تنظیمات کاربر استفاده می‌کند.

**پیکربندی فضای کاری** (`.vscode/mcp.json`):

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

**تنظیمات کاربر** (`settings.json`):

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

### استفاده از MCP در VS Code

1. پنل Copilot Chat را باز کنید (Ctrl+Shift+I / Cmd+Shift+I)
2. برای دیدن ابزارهای موجود MCP علامت `@` را تایپ کنید
3. با زبان طبیعی ابزارها را فراخوانی کنید: «محاسبه ۲۵ * ۴۸ با استفاده از ماشین‌حساب»

### عیب‌یابی VS Code

**بارگذاری نشدن سرورهای MCP:**
- پنل خروجی را بررسی کنید → "MCP" برای لاگ‌های خطا
- پنجره را ری‌لود کنید: Ctrl+Shift+P → "Developer: Reload Window"
- ابتدا مطمئن شوید سرور به‌صورت مستقل اجرا می‌شود

---

## 3. Cursor

**Cursor** یک ویرایشگر کد مبتنی بر هوش مصنوعی است که از MCP پشتیبانی داخلی دارد.

### نصب

1. Cursor را از [cursor.sh](https://cursor.sh) دانلود کنید
2. نصب و ورود

### پیکربندی

Cursor از فرمت پیکربندی مشابه Claude Desktop استفاده می‌کند.

**محل فایل پیکربندی:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**نمونه پیکربندی:**

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

### استفاده از MCP در Cursor

1. چت AI در Cursor را باز کنید (Ctrl+L / Cmd+L)
2. ابزارهای MCP به‌طور خودکار در پیشنهادات ظاهر می‌شوند
3. از هوش مصنوعی بخواهید با سرورهای متصل وظایف را انجام دهد

---

## 4. Cline (مبتنی بر ترمینال)

**Cline** یک کلاینت MCP مبتنی بر ترمینال است که برای گردش کار خط فرمان ایده‌آل است.

### نصب

```bash
npm install -g @anthropic/cline
```

### پیکربندی

Cline از متغیرهای محیطی و آرگومان‌های خط فرمان استفاده می‌کند.

**استفاده از متغیرهای محیطی:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**استفاده از آرگومان‌های خط فرمان:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**فایل پیکربندی** (`~/.clinerc`):

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

### استفاده از Cline

```bash
# شروع یک جلسه تعاملی
cline

# پرس و جوی منفرد با MCP
cline "Calculate the square root of 144 using the calculator"

# فهرست ابزارهای موجود
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** یک ویرایشگر کد مبتنی بر هوش مصنوعی دیگر است که از MCP پشتیبانی می‌کند.

### نصب

1. Windsurf را از [codeium.com/windsurf](https://codeium.com/windsurf) دانلود کنید
2. نصب و ایجاد حساب کاربری

### پیکربندی

پیکربندی Windsurf از طریق رابط کاربری تنظیمات مدیریت می‌شود:

1. تنظیمات را باز کنید (Ctrl+, / Cmd+,)
2. عبارت "MCP" را جستجو کنید
3. روی "Edit in settings.json" کلیک کنید

**نمونه پیکربندی:**

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

## مقایسه انواع انتقال

میزبان‌های مختلف از مکانیزم‌های انتقال مختلف پشتیبانی می‌کنند:

| میزبان | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (ورودی/خروجی استاندارد): بهترین برای سرورهای محلی که توسط میزبان راه‌اندازی می‌شوند
**SSE/HTTP**: بهترین برای سرورهای راه دور یا سرورهایی که بین چندین کلاینت به اشتراک گذاشته می‌شوند

---

## عیب‌یابی رایج

### سرور راه‌اندازی نمی‌شود

1. **ابتدا سرور را به‌صورت دستی تست کنید:**
   ```bash
   # برای پایتون
   python -m your_server_module
   
   # برای نود.جی‌اس
   node /path/to/server/index.js
   ```

2. **مسیر فرمان را بررسی کنید:**

   - در صورت امکان از مسیرهای مطلق استفاده کنید
   - اطمینان حاصل کنید که فایل اجرایی در PATH شما قرار دارد

3. **وابستگی‌ها را بررسی کنید:**
   ```bash
   # پایتون
   pip list | grep mcp
   
   # نود.جی‌اس
   npm list @modelcontextprotocol/sdk
   ```

### سرور متصل است اما ابزارها کار نمی‌کنند

1. **لاگ‌های سرور را بررسی کنید** - اکثر میزبان‌ها گزینه‌های لاگ‌گیری دارند
2. **ثبت ابزار را تأیید کنید** - از MCP Inspector برای تست استفاده کنید
3. **مجوزها را بررسی کنید** - برخی ابزارها به دسترسی به فایل/شبکه نیاز دارند

### متغیرهای محیطی منتقل نمی‌شوند

- برخی میزبان‌ها متغیرهای محیطی را پاک‌سازی می‌کنند
- از فیلد پیکربندی `env` به صورت صریح استفاده کنید
- از داده‌های حساس در فایل‌های پیکربندی اجتناب کنید (از مدیریت اسرار استفاده کنید)

---

## بهترین روش‌های امنیتی

1. **هرگز کلیدهای API را در فایل‌های پیکربندی کامیت نکنید**
2. **برای داده‌های حساس از متغیرهای محیطی استفاده کنید**
3. **مجوزهای سرور را فقط به حد نیاز محدود کنید**
4. **کد سرور را قبل از دادن دسترسی به سیستم خود بررسی کنید**
5. **از فهرست‌های مجاز برای دسترسی به فایل‌ها و شبکه استفاده کنید**

---

## مراحل بعدی

- [3.13 - اشکال‌زدایی با MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - ایجاد اولین سرور MCP خود](../01-first-server/README.md)
- [ماژول ۵ - موضوعات پیشرفته](../../05-AdvancedTopics/README.md)

---

## منابع بیشتر

- [مستندات MCP دسکتاپ Claude](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [افزونه VS Code MCP](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [مشخصات MCP - انتقال‌ها](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [ثبت رسمی سرورهای MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->