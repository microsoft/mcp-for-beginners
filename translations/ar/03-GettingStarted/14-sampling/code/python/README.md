# تشغيل العينة

> [!WARNING]
> تستخدم هذه العينة طريقة أخذ العينات (Sampling) المنتهية الصلاحية ونقطة نهاية HTTP+SSE قديمة.
> يتم الاحتفاظ بها لتوافق MCP `2025-11-25`. ينبغي على التنفيذات الجديدة استدعاء
> موفر LLM مباشرة واستخدام HTTP قابل للتدفق (Streamable) لحركة MCP البعيدة.

## إنشاء بيئة افتراضية

```sh
python -m venv venv
source ./venv/bin/activate
```

## تثبيت التبعيات

```sh
pip install "mcp[cli]"
```

## تشغيل الخادم

```sh
uvicorn server:app --port 8000
```

## اختبار الخادم باستخدام GitHub Copilot و VS Code

أضف الإدخال إلى mcp.json كما يلي:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

تأكد من النقر على "start" على الخادم.

في GitHub Copilot الصق الطلب التالي:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

في المرة الأولى سيُطلب منك قبول إجراء أخذ العينات (Sampling)، ثم سيتعين عليك قبول الأداة لتشغيل "create_blog". يجب أن ترى استجابة مشابهة لـ:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->