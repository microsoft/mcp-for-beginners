# تشغيل المثال

## إنشاء البيئة

```sh
python -m venv venv
source ./venv/bin/activate
```

## تثبيت التبعيات

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## إنشاء رمز مميز

ستحتاج إلى إنشاء رمز مميز يستخدمه العميل للتواصل مع الخادم.

قم بالاستدعاء:

```sh
python util.py
```

## تشغيل الكود

قم بتشغيل الكود باستخدام:

```sh
python server.py
```

في نافذة طرفية منفصلة، اكتب:

```sh
python client.py
```

في نافذة طرفية الخادم، يجب أن ترى شيئًا مثل:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

في نافذة العميل، يجب أن ترى نصًا مشابهًا لـ:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

هذا يعني أن كل شيء يعمل بشكل صحيح.

### تغيير المعلومات لرؤية الفشل

حدد هذا الكود في *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

قم بتغييره ليقول "User.Write". الرمز المميز الحالي الخاص بك لا يحتوي على مستوى الأذونات هذا، لذا إذا قمت بإعادة تشغيل الخادم وحاولت تشغيل العميل مرة أخرى، يجب أن ترى خطأ مشابهًا لما يلي في نافذة طرفية الخادم:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

يمكنك إما إعادة الكود الخاص بالخادم إلى حالته الأصلية أو إنشاء رمز مميز جديد يحتوي على هذا النطاق الإضافي، الخيار لك.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.