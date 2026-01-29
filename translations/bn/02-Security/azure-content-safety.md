# Azure Content Safety সহ উন্নত MCP সিকিউরিটি

Azure Content Safety আপনার MCP বাস্তবায়নগুলোর সুরক্ষা বাড়ানোর জন্য বেশ কিছু শক্তিশালী টুল সরবরাহ করে:

## Prompt Shields

Microsoft-এর AI Prompt Shields সরাসরি এবং পরোক্ষ উভয় ধরনের prompt injection আক্রমণ থেকে শক্তিশালী সুরক্ষা দেয়, যা করে:

1. **উন্নত সনাক্তকরণ**: মেশিন লার্নিং ব্যবহার করে কনটেন্টে লুকানো ক্ষতিকর নির্দেশনা চিহ্নিত করে।
2. **স্পটলাইটিং**: ইনপুট টেক্সটকে এমনভাবে রূপান্তর করে যাতে AI সিস্টেম সঠিক নির্দেশনা এবং বাইরের ইনপুট আলাদা করতে পারে।
3. **ডেলিমিটার এবং ডেটামার্কিং**: বিশ্বাসযোগ্য এবং অবিশ্বাসযোগ্য ডেটার মধ্যে সীমানা চিহ্নিত করে।
4. **Content Safety ইন্টিগ্রেশন**: Azure AI Content Safety-এর সাথে কাজ করে jailbreak চেষ্টা এবং ক্ষতিকর কনটেন্ট সনাক্ত করে।
5. **নিরবচ্ছিন্ন আপডেট**: Microsoft নিয়মিত নতুন হুমকির বিরুদ্ধে সুরক্ষা ব্যবস্থা আপডেট করে।

## MCP-র সাথে Azure Content Safety বাস্তবায়ন

এই পদ্ধতিটি বহুমাত্রিক সুরক্ষা প্রদান করে:
- প্রক্রিয়াকরণের আগে ইনপুট স্ক্যান করা
- আউটপুট ফেরত দেওয়ার আগে যাচাই করা
- পরিচিত ক্ষতিকর প্যাটার্নের জন্য ব্লকলিস্ট ব্যবহার করা
- Azure-এর নিয়মিত আপডেট হওয়া Content Safety মডেলগুলো ব্যবহার করা

## Azure Content Safety রিসোর্সসমূহ

আপনার MCP সার্ভারের সাথে Azure Content Safety বাস্তবায়ন সম্পর্কে আরও জানতে, এই অফিসিয়াল রিসোর্সগুলো দেখুন:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety-এর অফিসিয়াল ডকুমেন্টেশন।
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Prompt injection আক্রমণ প্রতিরোধের পদ্ধতি শিখুন।
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety বাস্তবায়নের জন্য বিস্তারিত API রেফারেন্স।
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# ব্যবহার করে দ্রুত বাস্তবায়নের গাইড।
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - বিভিন্ন প্রোগ্রামিং ভাষার জন্য ক্লায়েন্ট লাইব্রেরি।
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - jailbreak চেষ্টা সনাক্তকরণ এবং প্রতিরোধের জন্য নির্দিষ্ট নির্দেশনা।
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - কার্যকরভাবে Content Safety বাস্তবায়নের সেরা পদ্ধতি।

আরও গভীর বাস্তবায়নের জন্য, আমাদের [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) দেখুন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।