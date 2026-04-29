## الاختبار وتصحيح الأخطاء

قبل أن تبدأ في اختبار خادم MCP الخاص بك، من المهم فهم الأدوات المتاحة وأفضل الممارسات لتصحيح الأخطاء. يضمن الاختبار الفعال أن يتصرف الخادم كما هو متوقع ويساعدك على تحديد المشكلات وحلها بسرعة. يوضح القسم التالي الطرق الموصى بها للتحقق من تنفيذ MCP الخاص بك.

## نظرة عامة

تغطي هذه الدرس كيفية اختيار النهج الصحيح للاختبار وأداة الاختبار الأكثر فاعلية.

## أهداف التعلم

بنهاية هذا الدرس، ستتمكن من:

- وصف الأساليب المختلفة للاختبار.
- استخدام أدوات مختلفة لاختبار كودك بشكل فعال.

## اختبار خوادم MCP

يوفر MCP أدوات لمساعدتك في اختبار وتصحيح خوادمك:

- **MCP Inspector**: أداة سطر أوامر يمكن تشغيلها كأداة CLI وأيضًا كأداة بواجهة بصرية.
- **الاختبار اليدوي**: يمكنك استخدام أداة مثل curl لتشغيل طلبات الويب، ولكن أي أداة تدعم تشغيل HTTP ستفي بالغرض.
- **اختبار الوحدة**: يمكن استخدام إطار الاختبار المفضل لديك لاختبار ميزات الخادم والعميل على حد سواء.

### استخدام MCP Inspector

لقد وصفنا استخدام هذه الأداة في الدروس السابقة ولكن دعنا نتحدث عنها بشكل مبسط. إنها أداة مبنية على Node.js ويمكنك استخدامها من خلال استدعاء التنفيذي `npx` الذي سيقوم بتنزيل الأداة وتثبيتها مؤقتًا ثم تنظيف نفسه بمجرد الانتهاء من تشغيل طلبك.

تساعدك [MCP Inspector](https://github.com/modelcontextprotocol/inspector) على:

- **اكتشاف قدرات الخادم**: اكتشاف الموارد والأدوات والمطالبات المتاحة تلقائيًا
- **اختبار تنفيذ الأدوات**: تجربة معلمات مختلفة ورؤية الاستجابات في الوقت الفعلي
- **عرض بيانات تعريف الخادم**: فحص معلومات الخادم والمخططات والتكوينات

يبدو تشغيل الأداة النموذجي كما يلي:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

الأمر أعلاه يبدأ MCP وواجهته البصرية ويطلق واجهة ويب محلية في متصفحك. يمكنك توقع رؤية لوحة تعرض خوادم MCP المسجلة، والأدوات المتاحة لديهم، والموارد، والمطالبات. تتيح لك الواجهة اختبار تنفيذ الأدوات بشكل تفاعلي، وفحص بيانات تعريف الخادم، ومشاهدة الاستجابات في الوقت الحقيقي، مما يسهل التحقق وتصحيح تنفيذ MCP الخاص بك.

إليك شكله: ![Inspector](../../../../translated_images/ar/connect.141db0b2bd05f096.webp)

يمكنك أيضًا تشغيل هذه الأداة بوضع CLI حيث تضيف الخاصية `--cli`. هنا مثال لتشغيل الأداة بوضع "CLI" والذي يعرض جميع الأدوات على الخادم:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### الاختبار اليدوي

بجانب تشغيل أداة المفتش لاختبار قدرات الخادم، هناك نهج مشابه وهو تشغيل عميل قادر على استخدام HTTP مثل curl على سبيل المثال.

باستخدام curl، يمكنك اختبار خوادم MCP مباشرة باستخدام طلبات HTTP:

```bash
# مثال: بيانات وصفية لخادم الاختبار
curl http://localhost:3000/v1/metadata

# مثال: تنفيذ أداة
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

كما ترى من استخدام curl أعلاه، تستخدم طلب POST لاستدعاء أداة باستخدام تحميل مكون من اسم الأداة ومعلماتها. استخدم النهج الذي يناسبك أفضل. أدوات CLI بشكل عام أسرع في الاستخدام وتميل إلى أن تكون قابلة للبرمجة النصية مما يمكن أن يكون مفيدًا في بيئة CI/CD.

### اختبار الوحدة

قم بإنشاء اختبارات وحدة لأدواتك ومواردك للتأكد من أنها تعمل كما هو متوقع. إليك بعض كود الاختبار كمثال.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# وضع علامة على الوحدة بأكملها لاختبارات غير متزامنة
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # إنشاء بعض أدوات الاختبار
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # اختبار بدون معلمة المؤشر (تم الحذف)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # اختبار مع المؤشر = None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # اختبار مع المؤشر كسلسلة نصية
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # اختبار مع مؤشر فارغ (نص فارغ)
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

الكود السابق يقوم بما يلي:

- يستفيد من إطار عمل pytest الذي يتيح لك إنشاء اختبارات كدوال واستخدام عبارات assert.
- ينشئ خادم MCP مع أداتين مختلفتين.
- يستخدم عبارة `assert` للتحقق من تحقق شروط معينة.

اطلع على [الملف الكامل هنا](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

بناءً على الملف أعلاه، يمكنك اختبار خادمك الخاص لضمان أن القدرات تم إنشاؤها كما ينبغي.

جميع حزم SDK الرئيسية تحتوي على أقسام اختبار مماثلة بحيث يمكنك التكيف مع بيئة التشغيل التي تختارها.

## عينات

- [آلة حاسبة جافا](../samples/java/calculator/README.md)
- [آلة حاسبة .Net](../../../../03-GettingStarted/samples/csharp)
- [آلة حاسبة جافا سكريبت](../samples/javascript/README.md)
- [آلة حاسبة تايب سكريبت](../samples/typescript/README.md)
- [آلة حاسبة بايثون](../../../../03-GettingStarted/samples/python)

## موارد إضافية

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## ما هو التالي

- التالي: [النشر](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حرجة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير نابع من استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->