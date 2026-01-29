# نمونہ چلائیں

## ماحول بنائیں

```sh
python -m venv venv
source ./venv/bin/activate
```

## ضروریات انسٹال کریں

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## ٹوکن بنائیں

آپ کو ایک ٹوکن بنانا ہوگا جسے کلائنٹ سرور سے بات کرنے کے لیے استعمال کرے گا۔

کال کریں:

```sh
python util.py
```

## کوڈ چلائیں

کوڈ کو چلانے کے لیے:

```sh
python server.py
```

ایک الگ ٹرمینل میں، درج کریں:

```sh
python client.py
```

سرور کے ٹرمینل میں، آپ کو کچھ اس طرح نظر آنا چاہیے:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

کلائنٹ ونڈو میں، آپ کو اس طرح کا متن نظر آنا چاہیے:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

اس کا مطلب ہے کہ سب کچھ ٹھیک کام کر رہا ہے۔

### معلومات تبدیل کریں، تاکہ ناکامی نظر آئے

*server.py* میں یہ کوڈ تلاش کریں:

```python
 if not has_scope(has_header, "Admin.Write"):
```

اسے تبدیل کریں تاکہ یہ "User.Write" کہے۔ آپ کے موجودہ ٹوکن میں یہ اجازت سطح نہیں ہے، لہذا اگر آپ سرور کو دوبارہ شروع کریں اور کلائنٹ کو دوبارہ چلانے کی کوشش کریں تو آپ کو سرور کے ٹرمینل میں درج ذیل جیسی غلطی نظر آئے گی:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

آپ یا تو اپنے سرور کوڈ کو واپس تبدیل کر سکتے ہیں یا ایک نیا ٹوکن بنا سکتے ہیں جس میں یہ اضافی اسکوپ شامل ہو، یہ آپ پر منحصر ہے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔