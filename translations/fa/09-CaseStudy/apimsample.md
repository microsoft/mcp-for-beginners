# مطالعه موردی: نمایش REST API در مدیریت API به عنوان یک سرور MCP

Azure API Management، سرویسی است که یک دروازه (Gateway) روی نقاط انتهایی API شما ارائه می‌دهد. نحوه عملکرد آن به این صورت است که Azure API Management مانند یک پروکسی در جلوی API های شما عمل می‌کند و می‌تواند تصمیم بگیرد که چه کاری با درخواست‌های ورودی انجام دهد.

با استفاده از آن، مجموعه‌ای از قابلیت‌ها را اضافه می‌کنید مانند:

- **امنیت**، می‌توانید از روش‌های مختلفی مانند کلیدهای API، JWT تا هویت مدیریت شده استفاده کنید.
- **محدودیت نرخ**، یک ویژگی عالی این است که بتوانید تصمیم بگیرید چند تماس در واحد زمان خاصی عبور کنند. این کمک می‌کند تا همه کاربران تجربه خوبی داشته باشند و همچنین اطمینان حاصل شود که سرویس شما با درخواست‌های زیاد مواجه نمی‌شود.
- **مقیاس‌پذیری و تعادل بار**. می‌توانید تعدادی نقطه انتهایی تنظیم کنید تا بار را متعادل کند و همچنین می‌توانید تصمیم بگیرید چگونه «تعادل بار» را پیاده کنید.
- **ویژگی‌های هوش مصنوعی مانند کش معنایی، محدودیت توکن و نظارت بر توکن و غیره**. این‌ها ویژگی‌های خوبی هستند که پاسخگویی را بهبود می‌بخشند و همچنین به شما کمک می‌کنند بر مصرف توکن‌ها کنترل داشته باشید. [اینجا بیشتر بخوانید](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## چرا MCP + Azure API Management؟

پروتکل زمینه مدل (Model Context Protocol) به سرعت در حال تبدیل شدن به استانداردی برای برنامه‌های هوش مصنوعی عاملیت‌دار و نحوه ارائه ابزارها و داده‌ها به صورت منسجم است. Azure API Management انتخاب طبیعی است وقتی نیاز دارید API ها را «مدیریت» کنید. سرورهای MCP اغلب با API های دیگر ادغام می‌شوند تا درخواست‌ها را برای ابزاری مثلاً پاسخ دهند. بنابراین ترکیب Azure API Management و MCP بسیار منطقی است.

## نمای کلی

در این مورد استفاده خاص، یاد می‌گیریم چگونه نقاط انتهایی API را به عنوان یک سرور MCP نمایش دهیم. با انجام این کار، می‌توانیم به راحتی این نقاط انتهایی را بخشی از برنامه‌ای عاملیت‌دار کنیم و همزمان از ویژگی‌های Azure API Management بهره ببریم.

## ویژگی‌های کلیدی

- شما متدهایی را که می‌خواهید به عنوان ابزار نمایش داده شوند انتخاب می‌کنید.
- ویژگی‌های اضافی که دریافت می‌کنید بستگی به تنظیمات بخش سیاست‌ها در API شما دارد. اما در اینجا به شما نشان می‌دهیم چگونه می‌توانید محدودیت نرخ را اضافه کنید.

## گام پیش‌نیاز: وارد کردن یک API

اگر از قبل API در Azure API Management دارید که عالی است، می‌توانید این مرحله را رد کنید. اگر ندارید، این لینک را ببینید، [وارد کردن API به Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## نمایش API به عنوان سرور MCP

برای نمایش نقاط انتهایی API، مراحل زیر را دنبال کنید:

1. به پورتال Azure مراجعه کنید و آدرس زیر را باز کنید <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
به نمونه مدیریت API خود بروید.

1. در منوی سمت چپ، گزینه APIs > MCP Servers > + Create new MCP Server را انتخاب کنید.

1. در API، یک REST API را که می‌خواهید به عنوان سرور MCP نمایش دهید، انتخاب کنید.

1. یک یا چند عملیات API را برای نمایش به عنوان ابزار انتخاب کنید. می‌توانید همه عملیات‌ها یا فقط عملیات‌های خاصی را انتخاب کنید.

    ![انتخاب متدها برای نمایش](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. دکمه **Create** را انتخاب کنید.

1. به منوی **APIs** و سپس **MCP Servers** بروید، باید موارد زیر را ببینید:

    ![نمایش سرور MCP در پنل اصلی](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    سرور MCP ایجاد شده و عملیات API به عنوان ابزار نمایش داده شده‌اند. سرور MCP در پنل MCP Servers لیست شده است. ستون URL نقطه انتهایی سرور MCP را نشان می‌دهد که می‌توانید برای تست یا درون برنامه مشتری آن را فراخوانی کنید.

## اختیاری: پیکربندی سیاست‌ها

Azure API Management مفهوم اصلی سیاست‌ها را دارد که در آن قوانین مختلفی برای نقاط انتهایی خود تنظیم می‌کنید، مثلاً محدودیت نرخ یا کش معنایی. این سیاست‌ها به صورت XML نوشته می‌شوند.

در اینجا نحوه تنظیم سیاست برای محدود کردن نرخ سرور MCP را توضیح می‌دهیم:

1. در پورتال، زیر منوی APIs، گزینه **MCP Servers** را انتخاب کنید.

1. سرور MCP که ساخته‌اید را انتخاب کنید.

1. در منوی سمت چپ، زیر MCP، گزینه **Policies** را انتخاب کنید.

1. در ویرایشگر سیاست‌ها، سیاست‌های مورد نظر خود را برای اعمال روی ابزارهای سرور MCP اضافه یا ویرایش کنید. سیاست‌ها به صورت XML تعریف می‌شوند. برای مثال، می‌توانید سیاستی اضافه کنید که تماس‌ها با ابزارهای سرور MCP را (در این مثال، ۵ تماس در هر ۳۰ ثانیه برای هر آدرس IP کلاینت) محدود کند. این کد XML باعث اعمال محدودیت نرخ می‌شود:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    در اینجا تصویری از ویرایشگر سیاست‌ها است:

    ![ویرایشگر سیاست‌ها](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## امتحان کنید

بیایید مطمئن شویم که سرور MCP ما به درستی کار می‌کند.

> [!NOTE]
> Azure API Management در حال حاضر این سرور را از طریق نقطه انتهایی HTTP قابل جریان `/mcp` ارائه می‌دهد. انتقال قدیمی‌تر HTTP+SSE `/sse` منسوخ شده و
> باید فقط با کلاینت‌های قدیمی استفاده شود.


برای اینکار، از Visual Studio Code و GitHub Copilot و حالت Agent آن استفاده خواهیم کرد. ما سرور MCP را به *mcp.json* اضافه می‌کنیم. با این کار، Visual Studio Code به‌عنوان یک کلاینت با قابلیت‌های عاملیت عمل می‌کند و کاربران نهایی می‌توانند پرامپتی تایپ کنند و با آن سرور تعامل داشته باشند.

ببینیم چگونه می‌توان سرور MCP را در Visual Studio Code اضافه کرد:

1. از فرمان MCP: **Add Server command از Command Palette** استفاده کنید.

1. وقتی از شما خواسته شد، نوع سرور را انتخاب کنید: **HTTP (HTTP یا Server Sent Events)**.

1. آدرس HTTP قابل جریان نمایش داده شده برای سرور MCP در API Management را وارد کنید.
    مثلاً:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. شناسه سرور دلخواه خود را وارد کنید. این مقدار مهم نیست ولی به شما کمک می‌کند که این نمونه سرور را به‌خاطر بسپارید.

1. انتخاب کنید که تنظیمات را در Workspace settings یا User settings ذخیره کنید.

  - **تنظیمات Workspace** - پیکربندی سرور فقط در فایلی به نام .vscode/mcp.json ذخیره می‌شود که فقط در Workspace جاری در دسترس است.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **تنظیمات کاربر** - پیکربندی سرور به فایل جهانی *settings.json* شما اضافه می‌شود و در همه Workspace ها در دسترس است. پیکربندی شبیه به شکل زیر است:

    ![تنظیمات کاربر](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. همچنین باید پیکربندی هدر اضافه کنید تا اطمینان حاصل شود به درستی به Azure API Management احراز هویت می‌شود. از هدر **Ocp-Apim-Subscription-Key** استفاده می‌کند.

    - در اینجا نحوه افزودن آن به تنظیمات آمده است:

    ![افزودن هدر برای احراز هویت](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png) این باعث می‌شود پنجره‌ای باز شود و از شما مقدار کلید API که می‌توانید در پرتال Azure برای نمونه Azure API Management خود بیابید، پرسیده شود.

   - برای افزودن به *mcp.json* می‌توانید آن را به این شکل اضافه کنید:

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

اکنون در هر دو حالت تنظیمات یا در *.vscode/mcp.json* همه چیز آماده است. بیایید امتحان کنیم.

باید آیکون ابزارها (Tools) را ببینید، جایی که ابزارهای نمایش داده شده از سرور شما لیست شده‌اند:

![ابزارهای سرور](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. روی آیکون ابزارها کلیک کنید و باید فهرستی از ابزارها را ببینید:

    ![ابزارها](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. در چت یک پرامپت وارد کنید تا ابزار فراخوانی شود. به عنوان مثال، اگر ابزاری برای دریافت اطلاعات در مورد یک سفارش انتخاب کرده‌اید، می‌توانید از عامل درباره یک سفارش سوال کنید. این یک پرامپت نمونه است:

    ```text
    get information from order 2
    ```

    اکنون یک آیکون ابزار نمایش داده می‌شود که از شما می‌خواهد برای ادامه فراخوانی ابزار را تایید کنید. برای ادامه اجرای ابزار انتخاب کنید، اکنون باید خروجی مشابه زیر ببینید:

    ![نتیجه پرامپت](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **آنچه در بالا می‌بینید بستگی به ابزارهایی دارد که تنظیم کرده‌اید، اما ایده این است که پاسخ متنی مانند بالا دریافت کنید.**


## منابع

در اینجا چگونگی یادگیری بیشتر را می‌بینید:

- [آموزش در مورد Azure API Management و MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [نمونه پایتون: امن کردن سرورهای MCP از راه دور با استفاده از Azure API Management (آزمایشی)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [آزمایشگاه مجوزدهی کلاینت MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [استفاده از افزونه Azure API Management برای VS Code برای وارد کردن و مدیریت API ها](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ثبت و کشف سرورهای MCP از راه دور در Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) مخزن عالی که قابلیت‌های زیادی از هوش مصنوعی با Azure API Management نشان می‌دهد
- [کارگاه‌های AI Gateway](https://azure-samples.github.io/AI-Gateway/) شامل کارگاه‌هایی با استفاده از Azure Portal که راهی عالی برای شروع ارزیابی قابلیت‌های هوش مصنوعی است.

## مرحله بعد

- بازگشت به: [نمای کلی مطالعات موردی](./README.md)
- بعدی: [عاملین سفر هوش مصنوعی Azure](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->