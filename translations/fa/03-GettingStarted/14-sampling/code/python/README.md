# اجرای نمونه

> [!WARNING]
> این نمونه از Sampling منسوخ شده و یک نقطه پایانی HTTP+SSE قدیمی استفاده می‌کند.
> این نمونه برای سازگاری با MCP `2025-11-25` حفظ شده است. پیاده‌سازی‌های جدید باید
> مستقیماً یک ارائه‌دهنده LLM را فراخوانی کنند و برای ترافیک راه دور MCP از HTTP قابل استریم استفاده نمایند.

## ایجاد محیط مجازی

```sh
python -m venv venv
source ./venv/bin/activate
```

## نصب وابستگی‌ها

```sh
pip install "mcp[cli]"
```

## اجرای سرور

```sh
uvicorn server:app --port 8000
```

## آزمایش سرور با GitHub Copilot و VS Code

ورودی را به صورت زیر به mcp.json اضافه کنید:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

مطمئن شوید که روی "start" در سرور کلیک کرده‌اید.

در GitHub Copilot، رشته درخواست (prompt) زیر را جای‌گذاری کنید:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

اولین بار از شما خواسته می‌شود که آیا عملیات Sampling را قبول می‌کنید، سپس از شما خواسته خواهد شد ابزار "create_blog" را اجرا کنید. باید پاسخ مشابه زیر را مشاهده کنید:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->