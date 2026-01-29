# এই স্যাম্পলটি চালান

> [!NOTE]
> এই স্যাম্পলটি ধরে নিচ্ছে আপনি GitHub Codespaces ব্যবহার করছেন। যদি আপনি এটি লোকালি চালাতে চান, তাহলে GitHub-এ একটি personal access token (PAT) সেটআপ করতে হবে।
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## লাইব্রেরি ইনস্টল করুন

```sh
dotnet restore
```

নিম্নলিখিত লাইব্রেরিগুলো ইনস্টল করা উচিত: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## চালান

```sh 
dotnet run
```

আপনি নিম্নলিখিত ধরনের আউটপুট দেখতে পাবেন:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

আউটপুটের অনেক অংশ ডিবাগিং সংক্রান্ত, কিন্তু গুরুত্বপূর্ণ হলো আপনি MCP Server থেকে টুলগুলো তালিকাভুক্ত করছেন, সেগুলোকে LLM টুলে রূপান্তর করছেন এবং শেষ পর্যন্ত MCP ক্লায়েন্ট থেকে "Sum 6" রেসপন্স পাচ্ছেন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।