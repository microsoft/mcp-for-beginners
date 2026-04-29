## ٹیسٹنگ اور ڈیبگنگ

اپنے MCP سرور کی ٹیسٹنگ شروع کرنے سے پہلے، یہ سمجھنا ضروری ہے کہ دستیاب ٹولز اور ڈیبگنگ کے بہترین طریقے کیا ہیں۔ مؤثر ٹیسٹنگ اس بات کو یقینی بناتی ہے کہ آپ کا سرور متوقع طور پر کام کرے اور آپ کو مسائل کی جلد شناخت اور حل کرنے میں مدد دیتی ہے۔ درج ذیل سیکشن میں آپ کے MCP امپلیمنٹیشن کی جانچ کے لیے سفارش کردہ طریقے بیان کیے گئے ہیں۔

## جائزہ

یہ سبق درست ٹیسٹنگ طریقہ کار منتخب کرنے اور مؤثر ترین ٹیسٹنگ ٹول کے بارے میں ہے۔

## تعلیمی مقاصد

اس سبق کے اختتام تک، آپ کر سکیں گے:

- ٹیسٹنگ کے مختلف طریقوں کی وضاحت کریں۔
- مؤثر طریقے سے اپنے کوڈ کی جانچ کے لیے مختلف ٹولز استعمال کریں۔

## MCP سرورز کی ٹیسٹنگ

MCP ایسے ٹولز فراہم کرتا ہے جو آپ کو اپنے سرورز کی جانچ اور ڈیبگنگ میں مدد دیتے ہیں:

- **MCP Inspector**: ایک کمانڈ لائن ٹول جو CLI ٹول اور بصری ٹول دونوں کے طور پر چلایا جا سکتا ہے۔
- **دستی ٹیسٹنگ**: آپ curl جیسے ٹول کا استعمال کر کے ویب درخواستیں بھیج سکتے ہیں، لیکن کوئی بھی ایسا ٹول جو HTTP رن کر سکے، کام دے گا۔
- **یونٹ ٹیسٹنگ**: آپ اپنے پسندیدہ ٹیسٹنگ فریم ورک کو استعمال کر کے سرور اور کلائنٹ دونوں کی خصوصیات کی جانچ کر سکتے ہیں۔

### MCP Inspector کا استعمال

ہم نے پچھلے اسباق میں اس ٹول کے استعمال کی وضاحت کی ہے لیکن آئیے اسے ایک عمومی سطح پر تھوڑا بیان کرتے ہیں۔ یہ ایک Node.js میں بنایا ہوا ٹول ہے اور آپ اسے `npx` executable کو کال کر کے استعمال کر سکتے ہیں جو ٹول کو عارضی طور پر ڈاؤن لوڈ اور انسٹال کرے گا اور آپ کی درخواست چلنے کے بعد خود بخود صاف کر دے گا۔

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) آپ کی مدد کرتا ہے:

- **سرور صلاحیتوں کی دریافت**: دستیاب وسائل، ٹولز، اور پرامپٹس کو خودکار طریقے سے شناخت کریں
- **ٹول کی ٹیسٹنگ**: مختلف پیرا میٹرز آزما کر جواب کو حقیقی وقت میں دیکھیں
- **سرور میٹا ڈیٹا دیکھیں**: سرور کی معلومات، اسکیمہ، اور کنفیگریشن کا جائزہ لیں

ایک عام رن اس طرح نظر آتا ہے:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

اوپر والا حکم MCP اور اس کا بصری انٹرفیس شروع کرتا ہے اور آپ کے براؤزر میں ایک مقامی ویب انٹرفیس لانچ کرتا ہے۔ آپ ایک ڈیش بورڈ دیکھیں گے جو رجسٹرڈ MCP سرورز، ان کے دستیاب ٹولز، وسائل، اور پرامپٹس ظاہر کرتا ہے۔ یہ انٹرفیس آپ کو تعاملاتی طور پر ٹول کے نفاذ کی جانچ کرنے، سرور میٹا ڈیٹا معائنہ کرنے، اور حقیقی وقت میں جوابات دیکھنے کی سہولت دیتا ہے، جس سے MCP سرور امپلیمنٹیشن کی تصدیق اور ڈیبگنگ آسان ہو جاتی ہے۔

یہ کچھ اس طرح دکھ سکتا ہے: ![Inspector](../../../../translated_images/ur/connect.141db0b2bd05f096.webp)

آپ اس ٹول کو CLI موڈ میں بھی چلا سکتے ہیں، اس کے لیے `--cli` صفات شامل کریں۔ یہاں "CLI" موڈ میں ٹول چلانے کی مثال ہے جو سرور پر تمام ٹولز کی فہرست دکھاتی ہے:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### دستی ٹیسٹنگ

سرور کی صلاحیتوں کی جانچ کے لیے انسپکٹر ٹول چلانے کے علاوہ، ایک اور مشابه طریقہ HTTP استعمال کرنے والے کلائنٹ کو چلانا ہے جیسے curl۔

curl کے ساتھ، آپ MCP سرورز کی براہ راست HTTP درخواستوں سے جانچ کر سکتے ہیں:

```bash
# مثال: ٹیسٹ سرور میٹا ڈیٹا
curl http://localhost:3000/v1/metadata

# مثال: ایک اوزار چلائیں
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

جیسا کہ آپ curl کے اوپر استعمال سے دیکھ سکتے ہیں، آپ POST درخواست استعمال کر کے ٹول کو اس کے نام اور پیرا میٹرز کی حامل پے لوڈ کے ذریعے کال کرتے ہیں۔ وہ طریقہ استعمال کریں جو آپ کے لیے سب سے مناسب ہو۔ CLI ٹولز عام طور پر تیز تری سے استعمال ہوتے ہیں اور انھیں اسکرپٹ کیا جا سکتا ہے جو CI/CD ماحولیاتی نظام میں مفید ہو سکتا ہے۔

### یونٹ ٹیسٹنگ

اپنے ٹولز اور وسائل کے لیے یونٹ ٹیسٹ بنائیں تاکہ یقینی بنایا جا سکے کہ وہ متوقع طریقے سے کام کرتے ہیں۔ یہاں کچھ مثال ٹیسٹنگ کوڈ دیا گیا ہے۔

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# پورے ماڈیول کو غیر متزامن ٹیسٹ کے لیے نشان زد کریں
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # کچھ ٹیسٹ ٹولز بنائیں
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # کرسر پیرامیٹر کے بغیر ٹیسٹ کریں (چھوڑ دیا گیا)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # کرسر=None کے ساتھ ٹیسٹ کریں
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # کرسر کو سٹرنگ کے طور پر ٹیسٹ کریں
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # خالی سٹرنگ کرسر کے ساتھ ٹیسٹ کریں
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

اوپر دیا گیا کوڈ درج ذیل کرتا ہے:

- pytest فریم ورک کا استعمال، جو آپ کو فنکشن کی صورت میں ٹیسٹ بنانے اور assert سٹیٹمنٹس استعمال کرنے دیتا ہے۔
- دو مختلف ٹولز کے ساتھ ایک MCP سرور بناتا ہے۔
- `assert` بیان کا استعمال کرتا ہے تاکہ چیک کرے کہ مخصوص شرائط پوری ہو رہی ہیں۔

[مکمل فائل یہاں دیکھیں](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

مذکورہ بالا فائل کو مدنظر رکھتے ہوئے، آپ اپنے سرور کی جانچ کر سکتے ہیں تاکہ صلاحیتیں اسی طرح بنیں جیسا ہونا چاہیے۔

تمام بڑے SDKs میں اسی طرح کے ٹیسٹنگ سیکشنز ہوتے ہیں تاکہ آپ اپنے منتخب کردہ رن ٹائم کے مطابق ایڈجسٹ کر سکیں۔

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھن کیلکولیٹر](../../../../03-GettingStarted/samples/python)

## اضافی وسائل

- [پائتھن SDK](https://github.com/modelcontextprotocol/python-sdk)

## آگے کیا ہے

- اگلا: [تعمیر و تنصیب](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے تیار کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مادری زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->