# تشغيل هذا المثال

يُوصى بتثبيت `uv` ولكنه ليس إلزاميًا، راجع [التعليمات](https://docs.astral.sh/uv/#highlights)

## -0- إنشاء بيئة افتراضية

```bash
python -m venv venv
```

## -1- تفعيل البيئة الافتراضية

```bash
venv\Scripts\activate
```

## -2- تثبيت التبعيات

```bash
pip install "mcp[cli]"
```

## -3- تشغيل المثال

```bash
mcp run server.py
```

## -4- اختبار المثال

مع تشغيل الخادم في نافذة طرفية واحدة، افتح نافذة طرفية أخرى وقم بتشغيل الأمر التالي:

```bash
mcp dev server.py
```

يجب أن يبدأ هذا تشغيل خادم ويب بواجهة مرئية تتيح لك اختبار المثال.

بمجرد اتصال الخادم:

- حاول عرض الأدوات وتشغيل `add`، مع الوسيطين 2 و4، يجب أن ترى النتيجة 6.

- انتقل إلى الموارد وقالب الموارد وقم باستدعاء `get_greeting`، اكتب اسمًا وسترى تحية بالاسم الذي أدخلته.

### الاختبار في وضع CLI

المفتش الذي قمت بتشغيله هو في الواقع تطبيق Node.js و`mcp dev` هو غلاف حوله.

يمكنك تشغيله مباشرة في وضع CLI عن طريق تشغيل الأمر التالي:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

سيعرض هذا جميع الأدوات المتاحة في الخادم. يجب أن ترى المخرجات التالية:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

لإجراء استدعاء لأداة، اكتب:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

يجب أن ترى المخرجات التالية:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> عادةً ما يكون تشغيل المفتش في وضع CLI أسرع بكثير من تشغيله في المتصفح.
> اقرأ المزيد عن المفتش [هنا](https://github.com/modelcontextprotocol/inspector).

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.