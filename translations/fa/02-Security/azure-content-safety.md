# امنیت پیشرفته MCP با Azure Content Safety

Azure Content Safety ابزارهای قدرتمندی ارائه می‌دهد که می‌توانند امنیت پیاده‌سازی‌های MCP شما را بهبود بخشند:

## سپرهای Prompt

سپرهای AI Prompt مایکروسافت حفاظت قوی در برابر حملات تزریق مستقیم و غیرمستقیم prompt از طریق موارد زیر فراهم می‌کنند:

1. **شناسایی پیشرفته**: با استفاده از یادگیری ماشین، دستورالعمل‌های مخرب جاسازی شده در محتوا را شناسایی می‌کند.
2. **برجسته‌سازی**: متن ورودی را تغییر می‌دهد تا سیستم‌های AI بتوانند بین دستورالعمل‌های معتبر و ورودی‌های خارجی تمایز قائل شوند.
3. **مرزگذاری و علامت‌گذاری داده‌ها**: مرز بین داده‌های مورد اعتماد و غیرمورد اعتماد را مشخص می‌کند.
4. **ادغام با Content Safety**: با Azure AI Content Safety همکاری می‌کند تا تلاش‌های فرار از محدودیت (jailbreak) و محتوای مضر را شناسایی کند.
5. **به‌روزرسانی مداوم**: مایکروسافت به طور منظم مکانیزم‌های حفاظتی را در برابر تهدیدات نوظهور به‌روزرسانی می‌کند.

## پیاده‌سازی Azure Content Safety با MCP

این روش حفاظت چندلایه‌ای ارائه می‌دهد:
- اسکن ورودی‌ها قبل از پردازش
- اعتبارسنجی خروجی‌ها قبل از بازگرداندن
- استفاده از فهرست‌های مسدودسازی برای الگوهای شناخته شده مضر
- بهره‌گیری از مدل‌های به‌روزرسانی شده مداوم Azure Content Safety

## منابع Azure Content Safety

برای کسب اطلاعات بیشتر درباره پیاده‌سازی Azure Content Safety با سرورهای MCP خود، به منابع رسمی زیر مراجعه کنید:

1. [مستندات Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - مستندات رسمی Azure Content Safety.
2. [مستندات Prompt Shield](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - آموزش جلوگیری از حملات تزریق prompt.
3. [مرجع API Content Safety](https://learn.microsoft.com/rest/api/contentsafety/) - مرجع دقیق API برای پیاده‌سازی Content Safety.
4. [شروع سریع: Azure Content Safety با C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - راهنمای سریع پیاده‌سازی با استفاده از C#.
5. [کتابخانه‌های کلاینت Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - کتابخانه‌های کلاینت برای زبان‌های برنامه‌نویسی مختلف.
6. [شناسایی تلاش‌های فرار از محدودیت (jailbreak)](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - راهنمای خاص برای شناسایی و جلوگیری از تلاش‌های jailbreak.
7. [بهترین روش‌ها برای Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - بهترین روش‌ها برای پیاده‌سازی مؤثر Content Safety.

برای پیاده‌سازی عمیق‌تر، راهنمای [پیاده‌سازی Azure Content Safety](./azure-content-safety-implementation.md) ما را ببینید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.