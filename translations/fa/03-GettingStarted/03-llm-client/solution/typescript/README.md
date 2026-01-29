# اجرای این نمونه

این نمونه شامل داشتن یک LLM در سمت کلاینت است. LLM نیاز دارد که یا این را در Codespaces اجرا کنید یا یک توکن دسترسی شخصی در GitHub تنظیم کنید تا کار کند.

## -1- نصب وابستگی‌ها

```bash
npm install
```

## -3- اجرای سرور

```bash
npm run build
```

## -4- اجرای کلاینت

```sh
npm run client
```

باید نتیجه‌ای مشابه زیر ببینید:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.