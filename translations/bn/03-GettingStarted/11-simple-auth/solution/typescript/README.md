# নমুনা চালান

## নির্ভরতা ইনস্টল করুন

```sh
npm install
```

## বিল্ড করুন

```sh
npm run build
```

## টোকেন তৈরি করুন

```sh
npm run generate
```

এটি একটি *.env* ফাইলে একটি টোকেন তৈরি করে। ক্লায়েন্ট এই ফাইল থেকে পড়বে।

## কোড চালান

সার্ভার শুরু করুন:

```sh
npm start
```

ক্লায়েন্ট চালান, একটি আলাদা টার্মিনালে:

```sh
npm run client
```

সার্ভারের টার্মিনালে, আপনি নিম্নলিখিত আউটপুট দেখতে পাবেন:

```text
User exists
User has required scopes
Middleware executed
```

এবং ক্লায়েন্টের টার্মিনালে, আপনি নিম্নলিখিত আউটপুট দেখতে পাবেন:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### পরিবর্তন করা

চলুন নিশ্চিত করি যে আমরা স্কোপগুলি বুঝি। *server.ts* ফাইলটি খুঁজুন এবং এই কোডটি দেখুন:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

এটি বলে যে পাস করা টোকেনের "User.Read" থাকা প্রয়োজন, চলুন এটি "User.Write"-এ পরিবর্তন করি। এখন `npm run build` চালান এবং সার্ভার পুনরায় চালু করুন `npm start`। এখন আপনি দেখতে পাবেন যে প্রমাণীকরণ ব্যর্থ হয়েছে কারণ আমাদের এই স্কোপ নেই (আমাদের কাছে আছে User.Read এবং Admin.Write):

ক্লায়েন্ট এখন বলে

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

এবং আপনি সার্ভারের টার্মিনালে দেখতে পাবেন যে এটি বলে:

```text
User exists
```

এবং এটি এই পয়েন্টের বাইরে যায় না।

অথবা এই স্কোপ "User.Write" যোগ করুন এবং `npm run generate` চালান এবং ক্লায়েন্ট পুনরায় চালান অথবা সার্ভারের কোডটি পূর্বাবস্থায় ফিরিয়ে দিন।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।