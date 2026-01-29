# اجرای نمونه

## ایجاد محیط

```sh
python -m venv venv
source ./venv/bin/activate
```

## نصب وابستگی‌ها

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## تولید توکن

شما باید یک توکن تولید کنید که کلاینت از آن برای ارتباط با سرور استفاده کند.

فراخوانی کنید:

```sh
python util.py
```

## اجرای کد

کد را با دستور زیر اجرا کنید:

```sh
python server.py
```

در یک ترمینال جداگانه، تایپ کنید:

```sh
python client.py
```

در ترمینال سرور، باید چیزی مشابه زیر را مشاهده کنید:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

در پنجره کلاینت، باید متنی مشابه زیر را ببینید:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

این به این معناست که همه چیز درست کار می‌کند.

### تغییر اطلاعات برای مشاهده خطا

این کد را در فایل *server.py* پیدا کنید:

```python
 if not has_scope(has_header, "Admin.Write"):
```

آن را تغییر دهید تا "User.Write" را نشان دهد. توکن فعلی شما این سطح دسترسی را ندارد، بنابراین اگر سرور را مجدداً راه‌اندازی کنید و دوباره سعی کنید کلاینت را اجرا کنید، باید خطایی مشابه زیر را در ترمینال سرور مشاهده کنید:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

شما می‌توانید یا کد سرور خود را به حالت قبلی برگردانید یا یک توکن جدید تولید کنید که این سطح دسترسی اضافی را شامل شود، انتخاب با شماست.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.