# Example: Basic Host

একটি রেফারেন্স ইমপ্লিমেন্টেশন যা দেখায় কিভাবে MCP সার্ভারগুলিতে সংযুক্ত একটি MCP হোস্ট অ্যাপ্লিকেশন তৈরি করতে হয় এবং একটি সুরক্ষিত স্যান্ডবক্সে টুল ইউআই রেন্ডার করতে হয়।

এই বেসিক হোস্টটি স্থানীয় ডেভেলপমেন্টের সময় MCP অ্যাপ্লিকেশন পরীক্ষার জন্যও ব্যবহার করা যেতে পারে।

## Key Files

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - টুল নির্বাচন, প্যারামিটার ইনপুট, এবং iframe ব্যবস্থাপনার সাথে রিয়্যাক্ট ইউআই হোস্ট
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - সিকিউরিটি ভ্যালিডেশন এবং দ্বিমুখী মেসেজ রিলে সহ বাইরের iframe প্রক্সি
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - মূল লজিক: সার্ভার সংযোগ, টুল কলিং, এবং AppBridge সেটআপ

## Getting Started

```bash
npm install
npm run start
# খুলুন http://localhost:8080
```

ডিফল্টভাবে, হোস্ট অ্যাপ্লিকেশনটি `http://localhost:3001/mcp` ঠিকানায় একটি MCP সার্ভারের সাথে সংযোগ করার চেষ্টা করবে। আপনি সার্ভার URL এর JSON অ্যারে সহ `SERVERS` এনভায়রনমেন্ট ভেরিয়েবলটি সেট করে এই আচরণ কনফিগার করতে পারেন:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

এই উদাহরণটি সুরক্ষিত UI আলাদা করার জন্য একটি ডাবল-iframe sandbox প্যাটার্ন ব্যবহার করে:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**কেন দুইটি iframe?**

- বাইরের iframe একটি আলাদা উৎস (port 8081) এ চলে যা সরাসরি হোস্ট অ্যাক্সেস প্রতিরোধ করে
- ভিতরের iframe `srcdoc` এর মাধ্যমে HTML গ্রহণ করে এবং স্যান্ডবক্স অ্যাট্রিবিউট দ্বারা সীমাবদ্ধ
- মেসেজগুলি বাইরের iframe এর মাধ্যমে প্রবাহিত হয় যা এগুলি যাচাই করে এবং দ্বিমুখীভাবে রিলে করে

এই আর্কিটেকচার নিশ্চিত করে যে, যদি টুল UI কোড ম্যালিশিয়াসও হয়, তবুও এটি হোস্ট অ্যাপ্লিকেশনের DOM, কুকিজ, বা জাভাস্ক্রিপ্ট প্রসঙ্গ অ্যাক্সেস করতে পারে না।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করলেও, স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজভাষায়ই কর্তৃত্বসূচক উৎস বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের কারণে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->