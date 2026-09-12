# এই নমুনাটি চালানো

আপনাকে `uv` ইনস্টল করার পরামর্শ দেওয়া হচ্ছে তবে এটি বাধ্যতামূলক নয়, দেখুন [নির্দেশাবলী](https://docs.astral.sh/uv/#highlights)

## -0- একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

```bash
python -m venv venv
```

## -1- ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করুন

```bash
venv\Scripts\activate
```

## -2- নির্ভরশীলতাসমূহ ইনস্টল করুন

```bash
pip install "mcp[cli]"
```

## -3- নমুনাটি চালান

```bash
python client.py
```

আপনি এরকম একটি আউটপুট দেখতে পাবেন:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->