# مثال: میزبان پایه

یک پیاده‌سازی مرجع که نشان می‌دهد چگونه یک برنامه میزبان MCP بسازیم که به سرورهای MCP متصل می‌شود و رابط‌های ابزار را در یک محیط امن رندر می‌کند.

این میزبان پایه همچنین می‌تواند برای آزمایش برنامه‌های MCP در طول توسعه محلی استفاده شود.

## فایل‌های کلیدی

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - میزبان رابط React با انتخاب ابزار، ورودی پارامتر، و مدیریت iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - پروکسی iframe بیرونی با اعتبارسنجی امنیتی و ارسال پیام دوطرفه
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - منطق اصلی: اتصال به سرور، فراخوانی ابزار، و راه‌اندازی AppBridge

## شروع به کار

```bash
npm install
npm run start
# باز کردن http://localhost:8080
```

به طور پیش‌فرض، برنامه میزبان سعی می‌کند به سرور MCP در `http://localhost:3001/mcp` متصل شود. شما می‌توانید این رفتار را با تنظیم متغیر محیطی `SERVERS` به یک آرایه JSON از آدرس‌های سرور پیکربندی کنید:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## معماری

این مثال از الگوی ساندباکس با دو iframe برای جداسازی امن رابط کاربری استفاده می‌کند:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**چرا دو iframe؟**

- iframe بیرونی روی منبع جداگانه (پورت 8081) اجرا می‌شود که دسترسی مستقیم به میزبان را مسدود می‌کند
- iframe داخلی از طریق `srcdoc` دریافت HTML دارد و توسط ویژگی‌های sandbox محدود شده است
- پیام‌ها از طریق iframe بیرونی جریان دارند که آنها را اعتبارسنجی کرده و به صورت دوطرفه ارسال می‌کند

این معماری تضمین می‌کند که حتی اگر کد رابط ابزار مخرب باشد، نمی‌تواند به DOM، کوکی‌ها یا زمینه جاوااسکریپت برنامه میزبان دسترسی پیدا کند.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلان سلب مسئولیت**:
این سند با استفاده از خدمات ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطا یا نادرستی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->