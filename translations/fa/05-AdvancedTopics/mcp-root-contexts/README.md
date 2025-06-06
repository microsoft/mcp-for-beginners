<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e1cbc99fa7185139ad6d539eca09a2b3",
  "translation_date": "2025-06-02T20:21:46+00:00",
  "source_file": "05-AdvancedTopics/mcp-root-contexts/README.md",
  "language_code": "fa"
}
-->
## نمونه: پیاده‌سازی Root Context برای تحلیل مالی

در این مثال، یک root context برای یک جلسه تحلیل مالی ایجاد می‌کنیم و نشان می‌دهیم چگونه می‌توان وضعیت را در طول چندین تعامل حفظ کرد.

## نمونه: مدیریت Root Context

مدیریت مؤثر root contextها برای حفظ تاریخچه گفتگو و وضعیت اهمیت زیادی دارد. در ادامه نمونه‌ای از نحوه پیاده‌سازی مدیریت root context آورده شده است.

## Root Context برای کمک چند مرحله‌ای

در این مثال، یک root context برای یک جلسه کمک چند مرحله‌ای ایجاد می‌کنیم و نشان می‌دهیم چگونه می‌توان وضعیت را در طول چندین تعامل حفظ کرد.

## بهترین شیوه‌های Root Context

در اینجا چند بهترین شیوه برای مدیریت مؤثر root contextها آورده شده است:

- **ایجاد contextهای متمرکز**: برای اهداف یا حوزه‌های مختلف گفتگو، root contextهای جداگانه ایجاد کنید تا وضوح حفظ شود.

- **تنظیم سیاست‌های انقضا**: سیاست‌هایی برای آرشیو یا حذف contextهای قدیمی پیاده‌سازی کنید تا مدیریت ذخیره‌سازی و رعایت سیاست‌های نگهداری داده‌ها انجام شود.

- **ذخیره متادیتای مرتبط**: از متادیتای context برای ذخیره اطلاعات مهم درباره گفتگو که ممکن است بعداً مفید باشد استفاده کنید.

- **استفاده مداوم از شناسه‌های context**: پس از ایجاد یک context، شناسه آن را به طور مداوم برای همه درخواست‌های مرتبط استفاده کنید تا پیوستگی حفظ شود.

- **تولید خلاصه‌ها**: وقتی یک context بزرگ می‌شود، تولید خلاصه‌هایی را مد نظر قرار دهید تا اطلاعات ضروری ثبت شود و همزمان اندازه context مدیریت شود.

- **پیاده‌سازی کنترل دسترسی**: برای سیستم‌های چندکاربره، کنترل‌های دسترسی مناسب پیاده‌سازی کنید تا حریم خصوصی و امنیت contextهای گفتگو حفظ شود.

- **مدیریت محدودیت‌های context**: از محدودیت‌های اندازه context آگاه باشید و استراتژی‌هایی برای مدیریت گفتگوهای بسیار طولانی پیاده‌سازی کنید.

- **آرشیو پس از اتمام**: پس از پایان گفتگوها، contextها را آرشیو کنید تا منابع آزاد شده و تاریخچه گفتگو حفظ شود.

## گام بعدی

- [مسیردهی](../mcp-routing/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.