# تشغيل هذا المثال

## -1- تثبيت التبعيات

```bash
dotnet restore
```

## -2- تشغيل المثال

```bash
dotnet run
```

## -3- اختبار المثال

ابدأ تشغيل نافذة طرفية منفصلة قبل تنفيذ الأوامر أدناه (تأكد من أن الخادم لا يزال يعمل).

مع تشغيل الخادم في نافذة طرفية واحدة، افتح نافذة طرفية أخرى وقم بتنفيذ الأمر التالي:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

يجب أن يبدأ هذا خادم ويب بواجهة مرئية تتيح لك اختبار المثال.

> تأكد من أن **HTTP القابل للبث** تم اختياره كنوع النقل، وأن عنوان URL هو `http://localhost:3001/mcp`.

بمجرد اتصال الخادم:

- حاول عرض الأدوات وتشغيل `add`، مع الوسيطات 2 و4، يجب أن ترى النتيجة 6.
- انتقل إلى الموارد وقالب الموارد وقم باستدعاء "greeting"، اكتب اسمًا وسترى تحية بالاسم الذي قدمته.

### الاختبار في وضع CLI

يمكنك تشغيله مباشرة في وضع CLI عن طريق تنفيذ الأمر التالي:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

سيعرض هذا قائمة بجميع الأدوات المتاحة في الخادم. يجب أن ترى المخرجات التالية:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

لإجراء استدعاء لأداة، اكتب:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.