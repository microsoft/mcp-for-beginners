# নমুনা চালান

এই নমুনাটি একটি MCP সার্ভার শুরু করে যা একটি middleware ব্যবহার করে যা একটি বৈধ Authorization হেডার পরীক্ষা করে।

## নির্ভরতা ইনস্টল করুন

```bash
pip install "mcp[cli]" 
```

## সার্ভার শুরু করুন

```bash
python server.py
```

অন্য একটি টার্মিনালে ক্লায়েন্ট শুরু করুন

```bash
python client.py
```

আপনার একটি ফলাফল দেখতে পাওয়া উচিত যা এরকম:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

এর মানে হচ্ছে প্রেরিত credential অনুমোদিত হয়েছে।

`client.py`-এ credential "secret-token2" এ পরিবর্তন করার চেষ্টা করুন, তারপর আপনি এই টেক্সটটি প্রতিক্রিয়ার অংশ হিসেবে দেখতে পাবেন:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

এর মানে আপনি প্রমাণীকৃত হয়েছেন (আপনার একটি credential ছিল), কিন্তু এটি অবৈধ ছিল।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।