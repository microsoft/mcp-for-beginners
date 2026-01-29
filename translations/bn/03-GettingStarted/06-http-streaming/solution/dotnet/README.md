# এই নমুনা চালানো

## -1- নির্ভরশীলতা ইনস্টল করুন

```bash
dotnet restore
```

## -2- নমুনা চালান

```bash
dotnet run
```

## -3- নমুনা পরীক্ষা করুন

নিচের কমান্ড চালানোর আগে একটি আলাদা টার্মিনাল শুরু করুন (নিশ্চিত করুন যে সার্ভার এখনও চালু আছে)।

একটি টার্মিনালে সার্ভার চালু থাকা অবস্থায়, আরেকটি টার্মিনাল খুলুন এবং নিচের কমান্ড চালান:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

এটি একটি ওয়েব সার্ভার শুরু করবে যা একটি ভিজ্যুয়াল ইন্টারফেস প্রদান করবে, যা আপনাকে নমুনাটি পরীক্ষা করতে সাহায্য করবে।

> নিশ্চিত করুন যে **Streamable HTTP** পরিবহন প্রকার হিসেবে নির্বাচিত হয়েছে এবং URL `http://localhost:3001/mcp`।

সার্ভার সংযুক্ত হওয়ার পরে:

- টুলগুলির তালিকা দেখুন এবং `add` চালান, যেখানে আর্গুমেন্ট ২ এবং ৪, ফলাফলে আপনি ৬ দেখতে পাবেন।
- রিসোর্স এবং রিসোর্স টেমপ্লেটে যান এবং "greeting" কল করুন, একটি নাম টাইপ করুন এবং আপনি প্রদত্ত নাম সহ একটি অভিবাদন দেখতে পাবেন।

### CLI মোডে পরীক্ষা করা

আপনি সরাসরি CLI মোডে এটি চালু করতে পারেন নিচের কমান্ড চালিয়ে:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

এটি সার্ভারে উপলব্ধ সমস্ত টুলের তালিকা দেখাবে। আপনি নিম্নলিখিত আউটপুট দেখতে পাবেন:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

কোনো টুল চালানোর জন্য টাইপ করুন:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

আপনি নিম্নলিখিত আউটপুট দেখতে পাবেন:

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

> [!TIP]
> সাধারণত ব্রাউজারের তুলনায় CLI মোডে ইন্সপেক্টর চালানো অনেক দ্রুত হয়।
> ইন্সপেক্টর সম্পর্কে আরও পড়ুন [এখানে](https://github.com/modelcontextprotocol/inspector)।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়ী থাকব না।