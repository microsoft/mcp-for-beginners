<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f00aedb7b1d11b7eaacb0618d8791c65",
  "translation_date": "2025-05-29T23:02:01+00:00",
  "source_file": "02-Security/README.md",
  "language_code": "fa"
}
-->
# بهترین شیوه‌های امنیتی

پذیرش پروتکل مدل کانتکست (MCP) قابلیت‌های قدرتمندی را به برنامه‌های مبتنی بر هوش مصنوعی اضافه می‌کند، اما چالش‌های امنیتی منحصر به فردی را نیز به همراه دارد که فراتر از ریسک‌های نرم‌افزاری سنتی است. علاوه بر نگرانی‌های شناخته‌شده مانند کدنویسی امن، حداقل دسترسی و امنیت زنجیره تأمین، MCP و بارهای کاری هوش مصنوعی با تهدیدات جدیدی مانند تزریق فرمان، مسمومیت ابزار و تغییرات دینامیک ابزار مواجه هستند. اگر این ریسک‌ها به درستی مدیریت نشوند، می‌توانند منجر به استخراج داده‌ها، نقض حریم خصوصی و رفتارهای ناخواسته سیستم شوند.

این درس به بررسی مهم‌ترین ریسک‌های امنیتی مرتبط با MCP—از جمله احراز هویت، مجوزدهی، دسترسی‌های بیش از حد، تزریق فرمان غیرمستقیم و آسیب‌پذیری‌های زنجیره تأمین—می‌پردازد و کنترل‌ها و بهترین شیوه‌های عملی برای کاهش آن‌ها را ارائه می‌دهد. همچنین یاد می‌گیرید چگونه با استفاده از راهکارهای مایکروسافت مانند Prompt Shields، Azure Content Safety و GitHub Advanced Security پیاده‌سازی MCP خود را تقویت کنید. با درک و اعمال این کنترل‌ها، می‌توانید احتمال وقوع نفوذ امنیتی را به طور چشمگیری کاهش دهید و اطمینان حاصل کنید که سیستم‌های هوش مصنوعی شما مقاوم و قابل اعتماد باقی می‌مانند.

# اهداف یادگیری

تا پایان این درس، قادر خواهید بود:

- ریسک‌های امنیتی منحصر به فردی که پروتکل مدل کانتکست (MCP) ایجاد می‌کند را شناسایی و توضیح دهید، از جمله تزریق فرمان، مسمومیت ابزار، دسترسی‌های بیش از حد و آسیب‌پذیری‌های زنجیره تأمین.
- کنترل‌های مؤثر کاهش‌دهنده ریسک‌های امنیتی MCP مانند احراز هویت قوی، حداقل دسترسی، مدیریت امن توکن و تأیید زنجیره تأمین را توصیف و به کار ببرید.
- راهکارهای مایکروسافت مانند Prompt Shields، Azure Content Safety و GitHub Advanced Security را برای محافظت از MCP و بارهای کاری هوش مصنوعی درک و استفاده کنید.
- اهمیت اعتبارسنجی متادیتای ابزار، پایش تغییرات دینامیک و دفاع در برابر حملات تزریق فرمان غیرمستقیم را تشخیص دهید.
- بهترین شیوه‌های امنیتی تثبیت‌شده مانند کدنویسی امن، سخت‌سازی سرور و معماری اعتماد صفر را در پیاده‌سازی MCP خود ادغام کنید تا احتمال و تأثیر نفوذهای امنیتی کاهش یابد.

# کنترل‌های امنیتی MCP

هر سیستمی که به منابع مهم دسترسی دارد، چالش‌های امنیتی ضمنی دارد. به طور کلی، این چالش‌ها با به‌کارگیری صحیح کنترل‌ها و مفاهیم بنیادی امنیت قابل مدیریت هستند. از آنجا که MCP تازه تعریف شده است، مشخصات آن به سرعت در حال تغییر است و با پیشرفت پروتکل، کنترل‌های امنیتی درون آن تکامل می‌یابند تا امکان یکپارچگی بهتر با معماری‌های سازمانی و بهترین شیوه‌های امنیتی فراهم شود.

تحقیقات منتشر شده در [Microsoft Digital Defense Report](https://aka.ms/mddr) نشان می‌دهد که ۹۸٪ از نفوذهای گزارش شده با رعایت بهداشت امنیتی قوی قابل پیشگیری هستند و بهترین حفاظت در برابر هر نوع نفوذ، اجرای درست بهداشت امنیتی پایه، بهترین شیوه‌های کدنویسی امن و امنیت زنجیره تأمین است — آن روش‌های آزموده شده و شناخته‌شده همچنان بیشترین تأثیر را در کاهش ریسک امنیتی دارند.

بیایید برخی از روش‌هایی را بررسی کنیم که می‌توانید برای پرداختن به ریسک‌های امنیتی هنگام پذیرش MCP شروع کنید.

> **Note:** اطلاعات زیر تا تاریخ **۲۹ مه ۲۰۲۵** معتبر است. پروتکل MCP به طور مداوم در حال توسعه است و پیاده‌سازی‌های آینده ممکن است الگوها و کنترل‌های جدید احراز هویت را معرفی کنند. برای به‌روزرسانی‌ها و راهنمایی‌های جدید همیشه به [MCP Specification](https://spec.modelcontextprotocol.io/) و مخزن رسمی [MCP GitHub](https://github.com/modelcontextprotocol) و [صفحه بهترین شیوه‌های امنیتی](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) مراجعه کنید.

### بیان مسئله  
مشخصات اولیه MCP فرض کرده بود که توسعه‌دهندگان سرور احراز هویت خود را می‌نویسند. این نیازمند دانش OAuth و محدودیت‌های امنیتی مرتبط بود. سرورهای MCP به عنوان سرورهای مجوزدهی OAuth 2.0 عمل می‌کردند و احراز هویت کاربران را مستقیماً مدیریت می‌کردند، به جای واگذاری آن به سرویس خارجی مانند Microsoft Entra ID. از تاریخ **۲۶ آوریل ۲۰۲۵**، به‌روزرسانی مشخصات MCP امکان واگذاری احراز هویت کاربران به سرویس خارجی را فراهم می‌کند.

### ریسک‌ها
- منطق مجوزدهی نادرست در سرور MCP می‌تواند منجر به افشای داده‌های حساس و اعمال نادرست کنترل‌های دسترسی شود.
- سرقت توکن OAuth در سرور محلی MCP. در صورت سرقت، توکن می‌تواند برای جعل هویت سرور MCP و دسترسی به منابع و داده‌های سرویس مربوطه استفاده شود.

#### عبور توکن
عبور توکن در مشخصات مجوزدهی به صراحت ممنوع است چون ریسک‌های امنیتی متعددی ایجاد می‌کند، از جمله:

#### دور زدن کنترل‌های امنیتی
سرور MCP یا APIهای پایین‌دستی ممکن است کنترل‌های امنیتی مهمی مانند محدودیت نرخ، اعتبارسنجی درخواست یا پایش ترافیک را پیاده‌سازی کنند که به مخاطب توکن یا محدودیت‌های دیگر وابسته است. اگر کلاینت‌ها بتوانند توکن‌ها را مستقیماً با APIهای پایین‌دستی بدون اعتبارسنجی صحیح سرور MCP استفاده کنند، این کنترل‌ها دور زده می‌شوند.

#### مشکلات پاسخگویی و ردگیری
سرور MCP قادر به شناسایی یا تمایز بین کلاینت‌های MCP نخواهد بود وقتی کلاینت‌ها با توکن دسترسی صادرشده از بالا (که ممکن است برای سرور MCP مبهم باشد) فراخوانی کنند.
لاگ‌های سرور منبع پایین‌دستی ممکن است درخواست‌هایی را نشان دهند که به نظر از منبع یا هویتی متفاوت می‌آیند، نه سرور MCP که در واقع توکن‌ها را ارسال می‌کند.
هر دو مورد بررسی حادثه، کنترل‌ها و حسابرسی را دشوارتر می‌کند.
اگر سرور MCP توکن‌ها را بدون اعتبارسنجی ادعاها (مانند نقش‌ها، امتیازات یا مخاطب) یا متادیتای دیگر عبور دهد، یک بازیگر مخرب که توکن سرقت‌شده را دارد می‌تواند از سرور به عنوان واسطه برای استخراج داده‌ها استفاده کند.

#### مسائل مرز اعتماد
سرور منبع پایین‌دستی به موجودیت‌های خاصی اعتماد می‌کند. این اعتماد ممکن است شامل فرضیات درباره منشأ یا الگوهای رفتار کلاینت باشد. شکستن این مرز اعتماد می‌تواند منجر به مشکلات غیرمنتظره شود.
اگر توکن بدون اعتبارسنجی صحیح توسط چندین سرویس پذیرفته شود، یک مهاجم که یکی از سرویس‌ها را به خطر انداخته می‌تواند از توکن برای دسترسی به سایر سرویس‌های متصل استفاده کند.

#### ریسک سازگاری آینده
حتی اگر سرور MCP امروز به عنوان یک «پراکسی خالص» شروع کند، ممکن است بعداً نیاز به افزودن کنترل‌های امنیتی داشته باشد. شروع با تفکیک صحیح مخاطب توکن، مدل امنیتی را برای تکامل آسان‌تر می‌کند.

### کنترل‌های کاهش‌دهنده

**سرورهای MCP نباید هیچ توکنی را قبول کنند که صراحتاً برای سرور MCP صادر نشده باشد**

- **بازبینی و تقویت منطق مجوزدهی:** پیاده‌سازی مجوزدهی سرور MCP خود را با دقت بررسی کنید تا مطمئن شوید فقط کاربران و کلاینت‌های مورد نظر به منابع حساس دسترسی دارند. برای راهنمایی عملی، به [Azure API Management Your Auth Gateway For MCP Servers | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) و [Using Microsoft Entra ID To Authenticate With MCP Servers Via Sessions - Den Delimarsky](https://den.dev/blog/mcp-server-auth-entra-id-session/) مراجعه کنید.
- **اجرای شیوه‌های امن توکن:** از [بهترین شیوه‌های مایکروسافت برای اعتبارسنجی و مدت زمان توکن](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) پیروی کنید تا از سوءاستفاده از توکن‌های دسترسی جلوگیری و ریسک تکرار یا سرقت توکن کاهش یابد.
- **حفاظت از ذخیره‌سازی توکن:** همیشه توکن‌ها را به صورت امن ذخیره کنید و برای محافظت در حالت استراحت و انتقال از رمزنگاری استفاده کنید. برای نکات پیاده‌سازی، به [Use secure token storage and encrypt tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) مراجعه کنید.

# دسترسی‌های بیش از حد برای سرورهای MCP

### بیان مسئله  
ممکن است به سرورهای MCP دسترسی‌های بیش از حد به سرویس یا منبع داده شده باشد. به عنوان مثال، سرور MCP که بخشی از یک برنامه فروش مبتنی بر هوش مصنوعی است و به یک مخزن داده سازمانی متصل می‌شود، باید فقط به داده‌های فروش دسترسی داشته باشد و اجازه دسترسی به همه فایل‌های مخزن را نداشته باشد. با بازگشت به اصل حداقل دسترسی (یکی از قدیمی‌ترین اصول امنیتی)، هیچ منبعی نباید دسترسی بیش از حد مورد نیاز برای انجام وظایف خود داشته باشد. هوش مصنوعی چالش بیشتری در این زمینه ایجاد می‌کند چون برای انعطاف‌پذیری، تعریف دقیق دسترسی‌های لازم دشوار است.

### ریسک‌ها  
- اعطای دسترسی‌های بیش از حد می‌تواند منجر به استخراج یا تغییر داده‌هایی شود که سرور MCP قرار نبوده به آن‌ها دسترسی داشته باشد. این موضوع همچنین می‌تواند مشکل حریم خصوصی باشد اگر داده‌ها اطلاعات شناسایی شخصی (PII) باشند.

### کنترل‌های کاهش‌دهنده  
- **اجرای اصل حداقل دسترسی:** فقط حداقل دسترسی‌های لازم برای انجام وظایف سرور MCP را اعطا کنید. این دسترسی‌ها را به طور منظم بازبینی و به‌روزرسانی کنید تا از عدم تجاوز آن‌ها به نیاز واقعی اطمینان حاصل شود. برای راهنمایی دقیق‌تر، به [Secure least-privileged access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access) مراجعه کنید.
- **استفاده از کنترل دسترسی مبتنی بر نقش (RBAC):** نقش‌هایی به سرور MCP اختصاص دهید که به منابع و عملیات خاص محدود شده‌اند و از دسترسی‌های گسترده یا غیرضروری جلوگیری کنید.
- **پایش و حسابرسی دسترسی‌ها:** استفاده از دسترسی‌ها را به طور مداوم پایش کرده و لاگ‌های دسترسی را برای شناسایی و رفع سریع امتیازات بیش از حد یا بلااستفاده بررسی کنید.

# حملات تزریق فرمان غیرمستقیم

### بیان مسئله

سرورهای MCP مخرب یا به خطر افتاده می‌توانند با افشای داده‌های مشتری یا فعال‌سازی اقدامات ناخواسته ریسک‌های قابل توجهی ایجاد کنند. این ریسک‌ها به ویژه در بارهای کاری مبتنی بر هوش مصنوعی و MCP مرتبط هستند، جایی که:

- **حملات تزریق فرمان:** مهاجمان دستورات مخرب را در فرمان‌ها یا محتوای خارجی جاسازی می‌کنند که باعث می‌شود سیستم هوش مصنوعی اقدامات ناخواسته انجام دهد یا داده‌های حساس را افشا کند. اطلاعات بیشتر: [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- **مسمومیت ابزار:** مهاجمان متادیتای ابزار (مانند توضیحات یا پارامترها) را دستکاری می‌کنند تا رفتار هوش مصنوعی را تحت تأثیر قرار دهند، احتمالاً کنترل‌های امنیتی را دور زده یا داده‌ها را استخراج کنند. جزئیات: [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- **تزریق فرمان میان‌دامنه:** دستورات مخرب در اسناد، صفحات وب یا ایمیل‌ها جاسازی می‌شوند که سپس توسط هوش مصنوعی پردازش شده و منجر به نشت یا دستکاری داده‌ها می‌شود.
- **تغییر دینامیک ابزار (Rug Pulls):** تعاریف ابزار پس از تأیید کاربر می‌توانند تغییر کنند و رفتارهای مخرب جدیدی بدون اطلاع کاربر ایجاد کنند.

این آسیب‌پذیری‌ها نیازمند اعتبارسنجی قوی، پایش و کنترل‌های امنیتی هنگام ادغام سرورها و ابزارهای MCP در محیط شما هستند. برای بررسی عمیق‌تر، به منابع لینک شده مراجعه کنید.

![prompt-injection-lg-2048x1034](../../../translated_images/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.fa.png)

**تزریق فرمان غیرمستقیم** (که به عنوان تزریق فرمان میان‌دامنه یا XPIA نیز شناخته می‌شود) یک آسیب‌پذیری حیاتی در سیستم‌های تولیدی هوش مصنوعی است، از جمله آن‌هایی که از پروتکل مدل کانتکست (MCP) استفاده می‌کنند. در این حمله، دستورات مخرب در محتوای خارجی—مانند اسناد، صفحات وب یا ایمیل‌ها—پنهان می‌شوند. وقتی سیستم هوش مصنوعی این محتوا را پردازش می‌کند، ممکن است دستورات جاسازی‌شده را به عنوان فرمان‌های معتبر کاربر تفسیر کند که منجر به اقدامات ناخواسته‌ای مانند نشت داده‌ها، تولید محتوای مضر یا دستکاری تعاملات کاربر می‌شود. برای توضیح مفصل و نمونه‌های واقعی، به [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) مراجعه کنید.

شکل به‌خصوص خطرناک این حمله، **مسمومیت ابزار** است. در اینجا، مهاجمان دستورات مخرب را در متادیتای ابزارهای MCP (مانند توضیحات یا پارامترها) تزریق می‌کنند. از آنجا که مدل‌های زبانی بزرگ (LLM) برای تصمیم‌گیری در مورد ابزارهایی که باید فراخوانی شوند به این متادیتا تکیه دارند، توضیحات به‌خطر افتاده می‌توانند مدل را فریب دهند تا تماس‌های غیرمجاز با ابزار را اجرا کند یا کنترل‌های امنیتی را دور بزند. این دستکاری‌ها اغلب برای کاربران نهایی نامرئی هستند اما توسط سیستم هوش مصنوعی تفسیر و اجرا می‌شوند. این ریسک در محیط‌های میزبانی شده سرور MCP که تعاریف ابزار پس از تأیید کاربر به‌روزرسانی می‌شوند (که گاهی به آن "[rug pull](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)" گفته می‌شود) افزایش می‌یابد. در این موارد، ابزاری که قبلاً ایمن بود ممکن است بعداً برای انجام اقدامات مخرب مانند استخراج داده یا تغییر رفتار سیستم بدون اطلاع کاربر تغییر کند. برای اطلاعات بیشتر در مورد این بردار حمله، به [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) مراجعه کنید.

![tool-injection-lg-2048x1239 (1)](../../../translated_images/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.fa.png)

## ریسک‌ها  
اقدامات ناخواسته هوش مصنوعی ریسک‌های متنوعی از جمله استخراج داده و نقض حریم خصوصی ایجاد می‌کند.

### کنترل‌های کاهش‌دهنده  
### استفاده از Prompt Shields برای محافظت در برابر حملات تزریق فرمان غیرمستقیم
-----------------------------------------------------------------------------

**AI Prompt Shields** راهکاری است که توسط مایکروسافت توسعه یافته تا در برابر حملات تزریق فرمان مستقیم و غیرمستقیم دفاع کند. این راهکارها به روش‌های زیر کمک می‌کنند:

1.  **شناسایی و فیلتر کردن:** Prompt Shields با استفاده از الگوریتم‌های پیشرفته یادگیری ماشین و پردازش زبان طبیعی، دستورات مخرب جاسازی شده در محتوای خارجی مانند اسناد، صفحات وب یا ایمیل‌ها را شناسایی و فیلتر می‌کنند.
    
2.  **برجسته‌سازی (Spotlighting):** این تکنیک به سیستم هوش مصنوعی کمک می‌کند تا بین دستورات معتبر سیستم و ورودی‌های خارجی احتمالا غیرقابل اعتماد تمایز قائل شود. با تبدیل متن ورودی به شکلی که برای مدل مرتبط‌تر باشد، Spotlighting اطمینان می‌دهد که هوش مصنوعی بهتر می‌تواند دستورات مخرب را شناسایی و نادیده بگیرد.
    
3.  **مرزبندی و نشانه‌گذاری داده:** درج مرزها در پیام سیستم به وضوح محل متن ورودی را مشخص می‌کند و به سیستم هوش مصنوعی کمک می‌کند ورودی‌های کاربر را از محتوای خارجی بالقوه مضر جدا کند. نشانه‌گذاری داده این مفهوم را با استفاده از نشانگرهای ویژه برای برجسته‌سازی مرزهای داده‌های مورد اعتماد و غیرمطمئن گسترش می‌دهد.
    
4.  **پایش و به‌روزرسانی مداوم:** مایکروسافت به طور مستمر Prompt Shields را پایش و به‌روزرسانی می‌کند تا به تهدیدات جدید و در حال تحول پاسخ دهد. این رویکرد پیشگیرانه تضمین می‌کند که دفاع‌ها در برابر جدیدترین تکنیک‌های حمله مؤثر باقی بمانند.
    
5. **ادغام با Azure Content Safety:** Prompt Shields بخشی از مجموعه گسترده‌تر Azure AI Content Safety است که ابزارهای بیشتری برای شناسایی تلاش‌های فرار از محدودیت‌ها، محتوای مضر و دیگر ریسک‌های امنیتی در برنامه‌های هوش مصنوعی فراهم می‌کند.

برای مطالعه بیشتر درباره AI prompt shields به [مستندات Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) مراجعه کنید.

![prompt-shield-lg-
- [OWASP ده برتر](https://owasp.org/www-project-top-ten/)
- [OWASP ده برتر برای LLMها](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [امنیت پیشرفته GitHub](https://github.com/security/advanced-security)
- [Azure DevOps](https://azure.microsoft.com/products/devops)
- [مخازن Azure](https://azure.microsoft.com/products/devops/repos/)
- [سفر به سوی تأمین امنیت زنجیره تأمین نرم‌افزار در مایکروسافت](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)
- [دسترسی کمترین امتیاز امن (مایکروسافت)](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [بهترین روش‌ها برای اعتبارسنجی توکن و مدت زمان آن](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [استفاده از ذخیره‌سازی امن توکن و رمزنگاری توکن‌ها (YouTube)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)
- [مدیریت API Azure به عنوان دروازه احراز هویت برای MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [بهترین روش امنیتی MCP](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [استفاده از Microsoft Entra ID برای احراز هویت با سرورهای MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

### بعدی

بعدی: [فصل ۳: شروع کار](/03-GettingStarted/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.