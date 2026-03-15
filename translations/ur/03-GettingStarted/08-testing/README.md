## جانچ اور خرابیوں کا ازالہ

اپنے MCP سرور کی جانچ شروع کرنے سے پہلے، دستیاب ٹولز اور خرابیوں کا ازالہ کرنے کے بہترین طریقوں کو سمجھنا ضروری ہے۔ مؤثر جانچ اس بات کو یقینی بناتی ہے کہ آپ کا سرور متوقع طریقے سے کام کرے اور آپ کو مسائل کو جلد شناخت اور حل کرنے میں مدد دیتی ہے۔ درج ذیل سیکشن آپ کے MCP نفاذ کی تصدیق کے لیے تجویز کردہ طریقے بیان کرتا ہے۔

## جائزہ

یہ سبق صحیح جانچ کا طریقہ منتخب کرنے اور سب سے مؤثر جانچ کے ٹول کو استعمال کرنے کے بارے میں ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام پر، آپ قابل ہوں گے:

- جانچ کے مختلف طریقوں کی وضاحت کریں۔
- اپنے کوڈ کی مؤثر جانچ کے لیے مختلف ٹولز کا استعمال کریں۔

## MCP سرورز کی جانچ

MCP ایسے ٹولز فراہم کرتا ہے جو آپ کو اپنے سرورز کی جانچ اور خرابیوں کے ازالہ میں مدد دیتے ہیں:

- **MCP انسپیکٹر**: ایک کمانڈ لائن ٹول جو CLI ٹول کے طور پر اور بصری ٹول کے طور پر دونوں چلایا جا سکتا ہے۔
- **دستی جانچ**: آپ curl جیسے ٹول کا استعمال کرتے ہوئے ویب درخواستیں چلا سکتے ہیں، لیکن کوئی بھی ٹول جو HTTP چلا سکتا ہو کافی ہے۔
- **یونٹ ٹیسٹنگ**: آپ اپنے پسندیدہ ٹیسٹنگ فریم ورک کا استعمال کرتے ہوئے سرور اور کلائنٹ دونوں کی خصوصیات کی جانچ کر سکتے ہیں۔

### MCP انسپیکٹر کا استعمال

ہم نے اس ٹول کے استعمال کو پچھلے اسباق میں بیان کیا ہے لیکن آئیے اس پر تھوڑی اعلی سطح پر بات کرتے ہیں۔ یہ Node.js میں بنایا گیا ایک ٹول ہے اور آپ اسے `npx` executable کو کال کرکے استعمال کر سکتے ہیں، جو خود ٹول کو عارضی طور پر ڈاؤن لوڈ اور انسٹال کرے گا اور درخواست چلانے کے بعد خود کو صاف کر دے گا۔

[MCP انسپیکٹر](https://github.com/modelcontextprotocol/inspector) مدد دیتا ہے:

- **سرور کی صلاحیتوں کا پتہ لگانا**: دستیاب وسائل، ٹولز، اور پرامپٹس کو خودکار طور پر دریافت کرنا
- **ٹول کے نفاذ کی جانچ**: مختلف پیرامیٹر آزمانا اور حقیقی وقت میں جوابات دیکھنا
- **سرور کے میٹاڈیٹا کا جائزہ**: سرور کی معلومات، اسکیمے، اور ترتیبات کا معائنہ کرنا

ٹول کا ایک معمول کا چلانے کا طریقہ درج ذیل ہے:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

اوپر دیا گیا کمانڈ ایک MCP اور اس کا بصری انٹرفیس شروع کرتا ہے اور آپ کے براؤزر میں لوکل ویب انٹرفیس لانچ کرتا ہے۔ آپ ایک ڈیش بورڈ دیکھنے کی توقع کر سکتے ہیں جو آپ کے رجسٹرڈ MCP سرورز، ان کے دستیاب ٹولز، وسائل، اور پرامپٹس کو ظاہر کرتا ہے۔ یہ انٹرفیس آپ کو انٹرایکٹیوی طور پر ٹول کے نفاذ کی جانچ کرنے، سرور میٹاڈیٹا کی جانچ کرنے، اور حقیقی وقت کے جوابات دیکھنے کی سہولت دیتا ہے، جس سے آپ کے MCP سرور کے نفاذ کی تصدیق اور خرابیوں کا ازالہ آسان ہو جاتا ہے۔

یہ کچھ اس طرح دکھائی دے سکتا ہے: ![Inspector](../../../../translated_images/ur/connect.141db0b2bd05f096.webp)

آپ اس ٹول کو CLI موڈ میں بھی چلا سکتے ہیں، جس صورت میں آپ `--cli` وصف شامل کریں گے۔ یہاں "CLI" موڈ میں ٹول چلانے کی ایک مثال ہے جو سرور پر تمام ٹولز کی فہرست دکھاتی ہے:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### دستی جانچ

انسپیکٹر ٹول چلانے کے علاوہ، سرور کی صلاحیتوں کی جانچ کے لیے ایک اور مماثل طریقہ HTTP استعمال کرنے والے کلائنٹ کو چلانا ہے، جیسے curl۔

curl کے ساتھ، آپ MCP سرورز کی براہ راست HTTP درخواستوں سے جانچ کر سکتے ہیں:

```bash
# مثال: ٹیسٹ سرور میٹا ڈیٹا
curl http://localhost:3000/v1/metadata

# مثال: ایک ٹول چلائیں
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

جیسا کہ آپ curl کے اوپر استعمال سے دیکھ سکتے ہیں، آپ POST درخواست کا استعمال کرکے ایک ٹول کو اس کے نام اور اس کے پیرامیٹرز پر مشتمل پی لوڈ کے ذریعے کال کرتے ہیں۔ وہ طریقہ استعمال کریں جو آپ کے لیے سب سے بہتر ہو۔ عموماً CLI ٹولز استعمال کرنے میں تیز ہوتے ہیں اور ان کو اسکرپٹ کیا جا سکتا ہے جو CI/CD ماحول میں مفید ہو سکتا ہے۔

### یونٹ ٹیسٹنگ

اپنے ٹولز اور وسائل کے لیے یونٹ ٹیسٹ بنائیں تاکہ یہ یقینی بنایا جا سکے کہ وہ متوقع طریقے سے کام کرتے ہیں۔ یہاں کچھ مثال کا ٹیسٹنگ کوڈ ہے۔

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

    # چند ٹیسٹ ٹولز تخلیق کریں
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

        # کرسر کو اسٹرنگ کے طور پر ٹیسٹ کریں
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # خالی سٹرنگ کرسر کے ساتھ ٹیسٹ کریں
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

مندرجہ بالا کوڈ درج ذیل کام کرتا ہے:

- pytest فریم ورک کا استعمال کرتا ہے جو آپ کو ٹیسٹ کو فنکشنز کی صورت میں بنانے اور assert بیانات استعمال کرنے دیتا ہے۔
- دو مختلف ٹولز کے ساتھ MCP سرور بناتا ہے۔
- certain حالات کے پورا ہونے کی جانچ کے لیے `assert` بیان استعمال کرتا ہے۔

[یہاں مکمل فائل ملاحظہ کریں](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

مندرجہ بالا فائل کے ذریعے، آپ اپنے سرور کی جانچ کر سکتے ہیں تاکہ صلاحیتیں ویسی ہی بنائی گئی ہیں جیسا کہ ہونی چاہیے۔

تمام بڑے SDKs میں اسی طرح کا ٹیسٹنگ سیکشن ہوتا ہے تاکہ آپ اسے اپنے منتخب کردہ رن ٹائم کے مطابق ایڈجسٹ کر سکیں۔

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھن کیلکولیٹر](../../../../03-GettingStarted/samples/python)

## اضافی وسائل

- [پائتھن SDK](https://github.com/modelcontextprotocol/python-sdk)

## آگے کیا ہے

- اگلا: [تعمیرات](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی اعلان**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم صحت ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جائے۔ حساس معلومات کے لیے پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->