<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac67652abc453e2a7e2c75cd7a8897ae",
  "translation_date": "2025-07-13T18:04:30+00:00",
  "source_file": "03-GettingStarted/01-first-server/solution/typescript/README.md",
  "language_code": "bn"
}
-->
# এই স্যাম্পল চালানো

আপনাকে `uv` ইনস্টল করার পরামর্শ দেওয়া হচ্ছে, তবে এটি বাধ্যতামূলক নয়, বিস্তারিত দেখুন [নির্দেশনা](https://docs.astral.sh/uv/#highlights)

## -1- নির্ভরশীলতা ইনস্টল করুন

```bash
npm install
```

## -3- স্যাম্পল চালান

```bash
npm run build
```

## -4- স্যাম্পল পরীক্ষা করুন

একটি টার্মিনালে সার্ভার চালু থাকাকালীন, অন্য একটি টার্মিনাল খুলুন এবং নিচের কমান্ডটি চালান:

```bash
npm run inspector
```

এটি একটি ভিজ্যুয়াল ইন্টারফেস সহ একটি ওয়েব সার্ভার শুরু করবে যা আপনাকে স্যাম্পল পরীক্ষা করার সুযোগ দেবে।

সার্ভার সংযুক্ত হলে:

- টুলস তালিকা দেখার চেষ্টা করুন এবং `add` রান করুন, আর্গুমেন্ট হিসেবে ২ এবং ৪ দিন, ফলাফল হিসেবে ৬ দেখতে পাবেন।
- resources এবং resource template এ যান এবং "greeting" কল করুন, একটি নাম টাইপ করুন এবং আপনি প্রদত্ত নামসহ একটি শুভেচ্ছা দেখতে পাবেন।

### CLI মোডে পরীক্ষা

আপনি যে inspector চালিয়েছেন তা আসলে একটি Node.js অ্যাপ এবং `mcp dev` এর একটি র‍্যাপার।

আপনি সরাসরি CLI মোডে এটি চালাতে পারেন নিচের কমান্ডটি দিয়ে:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

এটি সার্ভারে উপলব্ধ সব টুলসের তালিকা দেখাবে। আপনি নিচের আউটপুট দেখতে পাবেন:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

কোনো টুল কল করতে টাইপ করুন:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

আপনি নিচের আউটপুট দেখতে পাবেন:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> ![!TIP]
> সাধারণত ব্রাউজারের তুলনায় CLI মোডে inspector চালানো অনেক দ্রুত হয়।
> inspector সম্পর্কে আরও পড়ুন [এখানে](https://github.com/modelcontextprotocol/inspector)।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।