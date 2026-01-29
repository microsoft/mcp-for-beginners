# এই নমুনা চালানো

কিভাবে ক্লাসিক HTTP স্ট্রিমিং সার্ভার এবং ক্লায়েন্ট চালাতে হয়, সেইসাথে Python ব্যবহার করে MCP স্ট্রিমিং সার্ভার এবং ক্লায়েন্ট চালানোর নির্দেশিকা এখানে দেওয়া হলো।

### ওভারভিউ

- আপনি একটি MCP সার্ভার সেটআপ করবেন, যা আইটেম প্রক্রিয়াকরণের সময় ক্লায়েন্টে প্রগ্রেস নোটিফিকেশন স্ট্রিম করবে।
- ক্লায়েন্ট রিয়েল টাইমে প্রতিটি নোটিফিকেশন প্রদর্শন করবে।
- এই গাইডে প্রয়োজনীয়তা, সেটআপ, চালানো এবং সমস্যা সমাধানের বিষয়গুলো অন্তর্ভুক্ত রয়েছে।

### প্রয়োজনীয়তা

- Python 3.9 বা তার নতুন সংস্করণ
- `mcp` প্যাকেজ (ইনস্টল করতে `pip install mcp` ব্যবহার করুন)

### ইনস্টলেশন ও সেটআপ

1. রিপোজিটরি ক্লোন করুন অথবা সলিউশন ফাইলগুলো ডাউনলোড করুন।

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং সক্রিয় করুন (প্রস্তাবিত):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **প্রয়োজনীয় ডিপেন্ডেন্সি ইনস্টল করুন:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ফাইলসমূহ

- **সার্ভার:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **ক্লায়েন্ট:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### ক্লাসিক HTTP স্ট্রিমিং সার্ভার চালানো

1. সলিউশন ডিরেক্টরিতে যান:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. ক্লাসিক HTTP স্ট্রিমিং সার্ভার চালান:

   ```pwsh
   python server.py
   ```

3. সার্ভার শুরু হবে এবং নিচের মতো আউটপুট দেখাবে:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### ক্লাসিক HTTP স্ট্রিমিং ক্লায়েন্ট চালানো

1. একটি নতুন টার্মিনাল খুলুন (একই ভার্চুয়াল এনভায়রনমেন্ট এবং ডিরেক্টরি সক্রিয় করুন):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. আপনি ক্রমান্বয়ে স্ট্রিম করা মেসেজ দেখতে পাবেন:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP স্ট্রিমিং সার্ভার চালানো

1. সলিউশন ডিরেক্টরিতে যান:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. স্ট্রিমেবল-HTTP ট্রান্সপোর্ট সহ MCP সার্ভার চালান:
   ```pwsh
   python server.py mcp
   ```
3. সার্ভার শুরু হবে এবং নিচের মতো আউটপুট দেখাবে:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP স্ট্রিমিং ক্লায়েন্ট চালানো

1. একটি নতুন টার্মিনাল খুলুন (একই ভার্চুয়াল এনভায়রনমেন্ট এবং ডিরেক্টরি সক্রিয় করুন):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. সার্ভার প্রতিটি আইটেম প্রক্রিয়াকরণের সময় রিয়েল টাইমে নোটিফিকেশন প্রিন্ট হবে:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### মূল ইমপ্লিমেন্টেশন ধাপসমূহ

1. **FastMCP ব্যবহার করে MCP সার্ভার তৈরি করুন।**
2. **একটি টুল ডিফাইন করুন, যা একটি তালিকা প্রক্রিয়াকরণ করে এবং `ctx.info()` বা `ctx.log()` ব্যবহার করে নোটিফিকেশন পাঠায়।**
3. **`transport="streamable-http"` দিয়ে সার্ভার চালান।**
4. **একটি ক্লায়েন্ট ইমপ্লিমেন্ট করুন, যা নোটিফিকেশন প্রদর্শনের জন্য একটি মেসেজ হ্যান্ডলার ব্যবহার করে।**

### কোড ওয়াকথ্রু
- সার্ভার অ্যাসিঙ্ক ফাংশন এবং MCP কন্টেক্সট ব্যবহার করে প্রগ্রেস আপডেট পাঠায়।
- ক্লায়েন্ট একটি অ্যাসিঙ্ক মেসেজ হ্যান্ডলার ইমপ্লিমেন্ট করে, যা নোটিফিকেশন এবং চূড়ান্ত ফলাফল প্রিন্ট করে।

### টিপস ও সমস্যা সমাধান

- নন-ব্লকিং অপারেশনের জন্য `async/await` ব্যবহার করুন।
- সার্ভার এবং ক্লায়েন্ট উভয় ক্ষেত্রেই এক্সেপশন হ্যান্ডেল করুন, যাতে সিস্টেম মজবুত হয়।
- একাধিক ক্লায়েন্ট দিয়ে পরীক্ষা করুন, যাতে রিয়েল টাইম আপডেট পর্যবেক্ষণ করা যায়।
- যদি কোনো ত্রুটি হয়, আপনার Python সংস্করণ চেক করুন এবং নিশ্চিত করুন যে সব ডিপেন্ডেন্সি ইনস্টল করা আছে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা তার জন্য দায়ী থাকব না।