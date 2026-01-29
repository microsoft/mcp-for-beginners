# اجرای این نمونه

توصیه می‌شود `uv` را نصب کنید اما اجباری نیست، برای جزئیات به [دستورالعمل‌ها](https://docs.astral.sh/uv/#highlights) مراجعه کنید

## -0- ایجاد یک محیط مجازی

```bash
python -m venv venv
```

## -1- فعال‌سازی محیط مجازی

```bash
venv\Scrips\activate
```

## -2- نصب وابستگی‌ها

```bash
pip install "mcp[cli]"
```

## -3- اجرای نمونه

```bash
python client.py
```

باید خروجی مشابه زیر را ببینید:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.