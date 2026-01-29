# اجرای این نمونه

## -1- نصب وابستگی‌ها

```bash
dotnet restore
```

## -2- اجرای نمونه

```bash
dotnet run
```

## -3- آزمایش نمونه

قبل از اجرای دستورات زیر، یک ترمینال جداگانه باز کنید (اطمینان حاصل کنید که سرور همچنان در حال اجرا است).

با اجرای سرور در یک ترمینال، یک ترمینال دیگر باز کنید و دستور زیر را اجرا کنید:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

این باید یک وب سرور با رابط بصری راه‌اندازی کند که به شما امکان آزمایش نمونه را می‌دهد.

> اطمینان حاصل کنید که **Streamable HTTP** به عنوان نوع انتقال انتخاب شده است و URL برابر با `http://localhost:3001/mcp` باشد.

پس از اتصال سرور:

- ابزارها را لیست کنید و `add` را اجرا کنید، با آرگومان‌های ۲ و ۴، باید نتیجه ۶ را مشاهده کنید.
- به منابع و قالب منابع بروید و "greeting" را فراخوانی کنید، یک نام وارد کنید و باید یک پیام خوش‌آمدگویی با نامی که وارد کرده‌اید مشاهده کنید.

### آزمایش در حالت CLI

می‌توانید آن را مستقیماً در حالت CLI با اجرای دستور زیر راه‌اندازی کنید:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

این تمام ابزارهای موجود در سرور را لیست می‌کند. باید خروجی زیر را مشاهده کنید:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

برای فراخوانی یک ابزار تایپ کنید:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

باید خروجی زیر را مشاهده کنید:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> معمولاً اجرای بازرس در حالت CLI بسیار سریع‌تر از مرورگر است.
> اطلاعات بیشتر درباره بازرس را [اینجا](https://github.com/modelcontextprotocol/inspector) بخوانید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.