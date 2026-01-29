# مطالعه موردی: انتشار REST API در مدیریت API به عنوان یک سرور MCP

مدیریت API در Azure، سرویسی است که یک Gateway را بر روی نقاط انتهایی API شما فراهم می‌کند. این سرویس به عنوان یک پروکسی در جلوی API‌های شما عمل می‌کند و می‌تواند تصمیم بگیرد که با درخواست‌های ورودی چه کاری انجام دهد.

با استفاده از این سرویس، می‌توانید مجموعه‌ای از ویژگی‌های اضافی را اضافه کنید، مانند:

- **امنیت**: می‌توانید از کلیدهای API، JWT، یا هویت مدیریت‌شده استفاده کنید.
- **محدودیت نرخ**: ویژگی عالی این است که می‌توانید تعیین کنید چند درخواست در یک بازه زمانی مشخص مجاز است. این کار تجربه کاربری بهتری را تضمین می‌کند و همچنین از بار زیاد روی سرویس شما جلوگیری می‌کند.
- **مقیاس‌پذیری و تعادل بار**: می‌توانید چندین نقطه انتهایی را برای تعادل بار تنظیم کنید و همچنین تصمیم بگیرید که چگونه بار را توزیع کنید.
- **ویژگی‌های هوش مصنوعی مانند کش معنایی**، محدودیت توکن، نظارت بر توکن و موارد دیگر. این ویژگی‌ها پاسخگویی را بهبود می‌بخشند و به شما کمک می‌کنند مصرف توکن خود را مدیریت کنید. [بیشتر بخوانید](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## چرا MCP + مدیریت API در Azure؟

پروتکل Model Context (MCP) به سرعت به یک استاندارد برای برنامه‌های هوش مصنوعی عامل‌محور تبدیل شده است و راهی برای انتشار ابزارها و داده‌ها به صورت یکپارچه فراهم می‌کند. مدیریت API در Azure یک انتخاب طبیعی است زمانی که نیاز به "مدیریت" API‌ها دارید. سرورهای MCP اغلب با سایر API‌ها برای پاسخ به درخواست‌ها ادغام می‌شوند. بنابراین ترکیب مدیریت API در Azure و MCP منطقی است.

## نمای کلی

در این مورد خاص، یاد می‌گیریم که چگونه نقاط انتهایی API را به عنوان یک سرور MCP منتشر کنیم. با این کار، می‌توانیم به راحتی این نقاط انتهایی را بخشی از یک برنامه عامل‌محور کنیم و در عین حال از ویژگی‌های مدیریت API در Azure بهره‌مند شویم.

## ویژگی‌های کلیدی

- شما می‌توانید روش‌های نقاط انتهایی که می‌خواهید به عنوان ابزار منتشر شوند را انتخاب کنید.
- ویژگی‌های اضافی که دریافت می‌کنید به تنظیماتی که در بخش سیاست‌ها برای API خود پیکربندی می‌کنید بستگی دارد. اما در اینجا نشان می‌دهیم که چگونه می‌توانید محدودیت نرخ را اضافه کنید.

## مرحله پیش‌نیاز: وارد کردن یک API

اگر قبلاً یک API در مدیریت API در Azure دارید، می‌توانید این مرحله را رد کنید. اگر نه، این لینک را بررسی کنید: [وارد کردن یک API به مدیریت API در Azure](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## انتشار API به عنوان سرور MCP

برای انتشار نقاط انتهایی API، مراحل زیر را دنبال کنید:

1. به پورتال Azure و آدرس زیر بروید: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   به نمونه مدیریت API خود بروید.

1. در منوی سمت چپ، گزینه **APIs > MCP Servers > + Create new MCP Server** را انتخاب کنید.

1. در بخش API، یک REST API را برای انتشار به عنوان سرور MCP انتخاب کنید.

1. یک یا چند عملیات API را برای انتشار به عنوان ابزار انتخاب کنید. می‌توانید همه عملیات یا فقط عملیات خاصی را انتخاب کنید.

    ![انتخاب روش‌ها برای انتشار](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. گزینه **Create** را انتخاب کنید.

1. به منوی **APIs** و **MCP Servers** بروید. باید صفحه‌ای مشابه زیر ببینید:

    ![مشاهده سرور MCP در پنل اصلی](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    سرور MCP ایجاد شده و عملیات API به عنوان ابزار منتشر شده‌اند. سرور MCP در پنل MCP Servers لیست شده است. ستون URL آدرس سرور MCP را نشان می‌دهد که می‌توانید برای تست یا در یک برنامه کلاینت از آن استفاده کنید.

## اختیاری: پیکربندی سیاست‌ها

مدیریت API در Azure مفهوم اصلی سیاست‌ها را دارد که در آن می‌توانید قوانین مختلفی را برای نقاط انتهایی خود تنظیم کنید، مانند محدودیت نرخ یا کش معنایی. این سیاست‌ها در قالب XML نوشته می‌شوند.

در اینجا نحوه تنظیم یک سیاست برای محدودیت نرخ سرور MCP آورده شده است:

1. در پورتال، در بخش APIs، گزینه **MCP Servers** را انتخاب کنید.

1. سرور MCP که ایجاد کرده‌اید را انتخاب کنید.

1. در منوی سمت چپ، در بخش MCP، گزینه **Policies** را انتخاب کنید.

1. در ویرایشگر سیاست، سیاست‌هایی که می‌خواهید به ابزارهای سرور MCP اعمال کنید را اضافه یا ویرایش کنید. سیاست‌ها در قالب XML تعریف می‌شوند. برای مثال، می‌توانید سیاستی اضافه کنید که تعداد تماس‌ها به ابزارهای سرور MCP را محدود کند (در این مثال، ۵ تماس در هر ۳۰ ثانیه برای هر آدرس IP کلاینت). این کد XML باعث محدودیت نرخ می‌شود:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    تصویر زیر ویرایشگر سیاست را نشان می‌دهد:

    ![ویرایشگر سیاست](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## آزمایش

بیایید مطمئن شویم که سرور MCP ما همانطور که انتظار می‌رود کار می‌کند.

برای این کار، از Visual Studio Code و GitHub Copilot در حالت Agent استفاده می‌کنیم. سرور MCP را به یک فایل *mcp.json* اضافه می‌کنیم. با این کار، Visual Studio Code به عنوان یک کلاینت با قابلیت‌های عامل‌محور عمل می‌کند و کاربران نهایی می‌توانند یک درخواست وارد کنند و با سرور تعامل داشته باشند.

### نحوه اضافه کردن سرور MCP در Visual Studio Code:

1. از دستور **MCP: Add Server** در Command Palette استفاده کنید.

1. وقتی از شما خواسته شد، نوع سرور را انتخاب کنید: **HTTP (HTTP یا Server Sent Events)**.

1. آدرس URL سرور MCP در مدیریت API را وارد کنید. مثال: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (برای نقطه انتهایی SSE) یا **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (برای نقطه انتهایی MCP). توجه کنید که تفاوت بین انتقال‌ها در `/sse` یا `/mcp` است.

1. یک شناسه سرور به انتخاب خود وارد کنید. این مقدار مهم نیست اما به شما کمک می‌کند این نمونه سرور را به خاطر بسپارید.

1. انتخاب کنید که آیا تنظیمات را در تنظیمات فضای کاری یا تنظیمات کاربر ذخیره کنید.

  - **تنظیمات فضای کاری** - پیکربندی سرور در یک فایل .vscode/mcp.json ذخیره می‌شود که فقط در فضای کاری فعلی در دسترس است.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    یا اگر انتقال HTTP استریمینگ را انتخاب کنید، کمی متفاوت خواهد بود:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **تنظیمات کاربر** - پیکربندی سرور به فایل *settings.json* جهانی شما اضافه می‌شود و در همه فضاهای کاری در دسترس است. پیکربندی مشابه زیر خواهد بود:

    ![تنظیمات کاربر](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. همچنین باید یک هدر اضافه کنید تا مطمئن شوید که به درستی به مدیریت API در Azure احراز هویت می‌کند. این کار از طریق هدر **Ocp-Apim-Subscription-Key** انجام می‌شود.

    - در اینجا نحوه اضافه کردن آن به تنظیمات آمده است:

    ![اضافه کردن هدر برای احراز هویت](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)، این کار باعث می‌شود یک درخواست برای وارد کردن مقدار کلید API نمایش داده شود که می‌توانید آن را در پورتال Azure برای نمونه مدیریت API خود پیدا کنید.

   - برای اضافه کردن آن به *mcp.json*، می‌توانید به این صورت عمل کنید:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### استفاده از حالت Agent

اکنون همه چیز در تنظیمات یا در *.vscode/mcp.json* تنظیم شده است. بیایید آن را امتحان کنیم.

باید یک آیکون ابزار مانند زیر وجود داشته باشد که ابزارهای منتشر شده از سرور شما را لیست می‌کند:

![ابزارها از سرور](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. روی آیکون ابزار کلیک کنید و باید لیستی از ابزارها مانند زیر ببینید:

    ![ابزارها](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. یک درخواست در چت وارد کنید تا ابزار را فراخوانی کنید. برای مثال، اگر ابزاری برای دریافت اطلاعات سفارش انتخاب کرده‌اید، می‌توانید از عامل درباره یک سفارش بپرسید. مثال:

    ```text
    get information from order 2
    ```

    اکنون یک آیکون ابزار نمایش داده می‌شود که از شما می‌خواهد برای فراخوانی ابزار ادامه دهید. انتخاب کنید که ابزار را اجرا کنید، باید خروجی مشابه زیر ببینید:

    ![نتیجه درخواست](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **آنچه در بالا می‌بینید بستگی به ابزارهایی دارد که تنظیم کرده‌اید، اما ایده این است که یک پاسخ متنی مانند بالا دریافت کنید.**

## منابع

در اینجا می‌توانید اطلاعات بیشتری کسب کنید:

- [آموزش مدیریت API در Azure و MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [نمونه پایتون: ایمن‌سازی سرورهای MCP از راه دور با استفاده از مدیریت API در Azure (تجربی)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [آزمایشگاه احراز هویت کلاینت MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [استفاده از افزونه مدیریت API در Azure برای VS Code برای وارد کردن و مدیریت API‌ها](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ثبت و کشف سرورهای MCP از راه دور در مرکز API Azure](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) مخزن عالی که بسیاری از قابلیت‌های هوش مصنوعی با مدیریت API در Azure را نشان می‌دهد.
- [کارگاه‌های AI Gateway](https://azure-samples.github.io/AI-Gateway/) شامل کارگاه‌هایی با استفاده از پورتال Azure، که راهی عالی برای شروع ارزیابی قابلیت‌های هوش مصنوعی است.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.