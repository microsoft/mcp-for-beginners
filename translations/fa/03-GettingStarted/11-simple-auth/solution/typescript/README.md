# اجرای نمونه

## نصب وابستگی‌ها

```sh
npm install
```

## ساخت

```sh
npm run build
```

## تولید توکن‌ها

```sh
npm run generate
```

این عملیات یک توکن در فایل *.env* ایجاد می‌کند. کلاینت از این فایل خوانده خواهد شد.

## اجرای کد

سرور را با دستور زیر راه‌اندازی کنید:

```sh
npm start
```

کلاینت را در یک ترمینال جداگانه اجرا کنید با:

```sh
npm run client
```

در ترمینال سرور، باید خروجی مشابه زیر را مشاهده کنید:

```text
User exists
User has required scopes
Middleware executed
```

و در ترمینال کلاینت، باید خروجی مشابه زیر را مشاهده کنید:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### تغییرات

بیایید مطمئن شویم که محدوده‌ها را درک می‌کنیم. فایل *server.ts* را پیدا کنید و این کد را مشاهده کنید:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

این کد می‌گوید توکن ارسال‌شده باید دارای "User.Read" باشد، حالا آن را به "User.Write" تغییر دهید. سپس دستور `npm run build` را اجرا کنید و سرور را با دستور `npm start` مجدداً راه‌اندازی کنید. اکنون باید ببینید که احراز هویت شکست خورده است زیرا این محدوده را نداریم (ما فقط User.Read و Admin.Write داریم):

کلاینت اکنون می‌گوید

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

و می‌توانید در ترمینال سرور مشاهده کنید که می‌گوید:

```text
User exists
```

و از این نقطه جلوتر نمی‌رود.

یا این محدوده "User.Write" را اضافه کنید و دستور `npm run generate` را اجرا کنید و کلاینت را دوباره اجرا کنید، یا کد سرور را به حالت قبلی برگردانید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.