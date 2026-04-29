## تست و دیباگ کردن

قبل از شروع تست سرور MCP خود، مهم است که ابزارهای موجود و بهترین روش‌ها برای دیباگ کردن را بشناسید. تست مؤثر اطمینان می‌دهد که سرور شما طبق انتظار رفتار می‌کند و به شما کمک می‌کند به‌سرعت مشکلات را شناسایی و حل کنید. بخش زیر روش‌های توصیه شده برای اعتبارسنجی پیاده‌سازی MCP شما را شرح می‌دهد.

## مرور کلی

این درس پوشش می‌دهد که چگونه روش تست درست و ابزار تست مؤثر را انتخاب کنید.

## اهداف یادگیری

تا پایان این درس، شما قادر خواهید بود:

- روش‌های مختلف برای تست را توصیف کنید.
- از ابزارهای مختلف برای تست مؤثر کد خود استفاده کنید.

## تست سرورهای MCP

MCP ابزارهایی برای کمک به شما در تست و دیباگ سرورها ارائه می‌دهد:

- **بازرس MCP**: ابزاری خط فرمان که هم به صورت CLI و هم به صورت بصری قابل اجراست.
- **تست دستی**: می‌توانید از ابزاری مانند curl برای اجرای درخواست‌های وب استفاده کنید، اما هر ابزاری که بتواند HTTP را اجرا کند قابل استفاده است.
- **تست واحد**: این امکان وجود دارد که از فریمورک تست دلخواه خود برای تست ویژگی‌های هم سرور و هم کلاینت استفاده کنید.

### استفاده از بازرس MCP

ما قبلاً کاربرد این ابزار را در درس‌های قبلی توضیح داده‌ایم اما اجازه دهید کمی به طور سطحی به آن بپردازیم. این ابزاری ساخته شده با Node.js است و می‌توانید با فراخوانی اجرایی `npx` از آن استفاده کنید که به طور موقت خود ابزار را دانلود و نصب می‌کند و پس از اجرای درخواست شما، خودش را پاک‌سازی می‌کند.

ابزار [MCP Inspector](https://github.com/modelcontextprotocol/inspector) به شما کمک می‌کند:

- **کشف قابلیت‌های سرور**: به طور خودکار منابع، ابزارها و پرامپت‌های موجود را شناسایی کند
- **تست اجرای ابزار**: پارامترهای مختلف را امتحان کرده و پاسخ‌ها را به صورت زنده مشاهده کنید
- **مشاهده متاداده سرور**: اطلاعات، اسکیم‌ها و پیکربندی‌های سرور را بررسی کنید

اجرای معمولی این ابزار به شکل زیر است:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

دستور بالا یک MCP و رابط بصری آن را راه‌اندازی کرده و یک رابط وب محلی در مرورگر شما باز می‌کند. انتظار می‌رود داشبوردی مشاهده کنید که سرورهای ثبت‌شده MCP شما، ابزارها، منابع و پرامپت‌های موجود را نمایش می‌دهد. این رابط به شما امکان می‌دهد اجرای ابزارها را به صورت تعاملی تست کنید، متاداده سرور را بازرسی نمایید و پاسخ‌های لحظه‌ای را مشاهده کنید، که اعتبارسنجی و دیباگ پیاده‌سازی‌های سرور MCP شما را آسان‌تر می‌کند.

این شکل آن می‌تواند باشد: ![Inspector](../../../../translated_images/fa/connect.141db0b2bd05f096.webp)

همچنین می‌توانید این ابزار را در حالت CLI اجرا کنید که در این صورت باید ویژگی `--cli` را اضافه کنید. مثال زیر اجرای ابزار در حالت "CLI" را نشان می‌دهد که تمام ابزارهای سرور را فهرست می‌کند:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### تست دستی

علاوه بر اجرای ابزار بازرس برای تست قابلیت‌های سرور، رویکرد مشابه دیگر، اجرای کلاینتی است که توانایی استفاده از HTTP را داشته باشد، برای مثال curl.

با curl می‌توانید سرورهای MCP را مستقیماً با درخواست‌های HTTP تست کنید:

```bash
# مثال: متادیتای سرور آزمایشی
curl http://localhost:3000/v1/metadata

# مثال: اجرای یک ابزار
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

همانطور که از استفاده بالا از curl مشاهده می‌کنید، با درخواست POST، ابزاری را از طریق بارگذاری‌ای که شامل نام ابزار و پارامترهایش است، فراخوانی می‌کنید. روشی که برای شما مناسب‌تر است را انتخاب کنید. ابزارهای CLI عموماً سریع‌تر برای استفاده هستند و به راحتی قابلیت اسکریپت‌سازی دارند که می‌تواند در محیط CI/CD مفید باشد.

### تست واحد

تست‌های واحد برای ابزارها و منابع خود ایجاد کنید تا اطمینان حاصل کنید که مطابق انتظار کار می‌کنند. در اینجا نمونه کد تستی آورده شده است.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# علامت‌گذاری کل ماژول برای تست‌های ناهمزمان
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # ایجاد چند ابزار تست
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # تست بدون پارامتر مکان‌نما (حذف شده)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # تست با مکان‌نمای None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # تست با مکان‌نما به صورت رشته
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # تست با مکان‌نمای رشته خالی
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

کد بالا کارهای زیر را انجام می‌دهد:

- از فریمورک pytest استفاده می‌کند که به شما امکان می‌دهد تست‌ها را به صورت تابع نوشته و از عبارات assert استفاده کنید.
- یک سرور MCP با دو ابزار مختلف ایجاد می‌کند.
- از عبارت `assert` برای بررسی برآورده شدن شرایط خاص استفاده می‌کند.

می‌توانید فایل کامل را از [این‌جا](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py) مشاهده کنید.

با توجه به فایل بالا، می‌توانید سرور خود را تست کنید تا اطمینان حاصل شود که قابلیت‌ها به درستی ایجاد شده‌اند.

تمام SDKهای اصلی بخش‌های تستی مشابهی دارند که می‌توانید مطابق محیط اجرایی انتخابی خود تنظیم کنید.

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)

## منابع اضافی

- [SDK پایتون](https://github.com/modelcontextprotocol/python-sdk)

## گام بعدی

- بعدی: [استقرار](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است دارای خطا یا نادرستی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->