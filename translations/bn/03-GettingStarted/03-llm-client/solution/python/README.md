# এই স্যাম্পল চালানো

আপনাকে `uv` ইনস্টল করার পরামর্শ দেওয়া হচ্ছে, তবে এটি বাধ্যতামূলক নয়, বিস্তারিত দেখুন [instructions](https://docs.astral.sh/uv/#highlights)

## -0- একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন

```bash
python -m venv venv
```

## -1- ভার্চুয়াল এনভায়রনমেন্ট সক্রিয় করুন

```bash
venv\Scrips\activate
```

## -2- নির্ভরশীলতাগুলো ইনস্টল করুন

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- স্যাম্পলটি চালান

```bash
python client.py
```

আপনি নিচের মতো একটি আউটপুট দেখতে পাবেন:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।