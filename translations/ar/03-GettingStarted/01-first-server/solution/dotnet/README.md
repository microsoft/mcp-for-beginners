# تشغيل هذا المثال

## -1- تثبيت التبعيات

```bash
dotnet restore
```

## -3- تشغيل المثال

```bash
dotnet run
```

## -4- اختبار المثال

مع تشغيل الخادم في نافذة طرفية واحدة، افتح نافذة طرفية أخرى وقم بتشغيل الأمر التالي:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

يجب أن يبدأ هذا تشغيل خادم ويب بواجهة مرئية تتيح لك اختبار المثال.

بمجرد اتصال الخادم:

- حاول عرض الأدوات وتشغيل `add`، مع الوسيطات 2 و4، يجب أن ترى النتيجة 6.
- انتقل إلى الموارد وقالب الموارد وقم باستدعاء "greeting"، اكتب اسمًا وسترى تحية بالاسم الذي قدمته.

### الاختبار في وضع CLI

يمكنك تشغيله مباشرة في وضع CLI عن طريق تشغيل الأمر التالي:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

سيعرض هذا جميع الأدوات المتاحة في الخادم. يجب أن ترى الإخراج التالي:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

لإطلاق أداة، اكتب:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

يجب أن ترى الإخراج التالي:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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