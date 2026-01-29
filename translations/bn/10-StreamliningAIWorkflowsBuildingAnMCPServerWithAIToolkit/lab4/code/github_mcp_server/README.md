# Weather MCP Server

এটি একটি নমুনা MCP সার্ভার যা Python-এ আবহাওয়া টুলস সহ মক রেসপন্স ব্যবহার করে তৈরি করা হয়েছে। এটি আপনার নিজস্ব MCP সার্ভারের জন্য একটি কাঠামো হিসেবে ব্যবহার করা যেতে পারে। এতে নিম্নলিখিত বৈশিষ্ট্যগুলি অন্তর্ভুক্ত রয়েছে:

- **Weather Tool**: একটি টুল যা প্রদত্ত অবস্থানের উপর ভিত্তি করে মক আবহাওয়ার তথ্য সরবরাহ করে।
- **Git Clone Tool**: একটি টুল যা একটি গিট রিপোজিটরি নির্দিষ্ট ফোল্ডারে ক্লোন করে।
- **VS Code Open Tool**: একটি টুল যা VS Code বা VS Code Insiders-এ একটি ফোল্ডার খুলে।
- **Agent Builder-এর সাথে সংযোগ করুন**: একটি বৈশিষ্ট্য যা MCP সার্ভারকে Agent Builder-এর সাথে সংযোগ করতে দেয় পরীক্ষার এবং ডিবাগিংয়ের জন্য।
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)-এ ডিবাগ করুন**: একটি বৈশিষ্ট্য যা MCP Inspector ব্যবহার করে MCP সার্ভার ডিবাগ করতে দেয়।

## Weather MCP Server টেমপ্লেট দিয়ে শুরু করুন

> **প্রয়োজনীয়তা**
>
> আপনার লোকাল ডেভ মেশিনে MCP সার্ভার চালানোর জন্য আপনার প্রয়োজন হবে:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo টুলের জন্য প্রয়োজনীয়)
> - [VS Code](https://code.visualstudio.com/) বা [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode টুলের জন্য প্রয়োজনীয়)
> - (*ঐচ্ছিক - যদি আপনি uv পছন্দ করেন*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## পরিবেশ প্রস্তুত করুন

এই প্রকল্পের পরিবেশ সেটআপ করার দুটি পদ্ধতি রয়েছে। আপনি আপনার পছন্দ অনুযায়ী যেকোনো একটি বেছে নিতে পারেন।

> নোট: ভার্চুয়াল পরিবেশ তৈরি করার পরে নিশ্চিত করুন যে ভার্চুয়াল পরিবেশের Python ব্যবহার করা হচ্ছে, এর জন্য VSCode বা টার্মিনাল রিলোড করুন।

| পদ্ধতি | ধাপসমূহ |
| -------- | ----- |
| `uv` ব্যবহার করে | 1. ভার্চুয়াল পরিবেশ তৈরি করুন: `uv venv` <br>2. VSCode কমান্ড "***Python: Select Interpreter***" চালান এবং তৈরি করা ভার্চুয়াল পরিবেশ থেকে Python নির্বাচন করুন <br>3. ডিপেনডেন্সি ইনস্টল করুন (ডেভ ডিপেনডেন্সি সহ): `uv pip install -r pyproject.toml --extra dev` |
| `pip` ব্যবহার করে | 1. ভার্চুয়াল পরিবেশ তৈরি করুন: `python -m venv .venv` <br>2. VSCode কমান্ড "***Python: Select Interpreter***" চালান এবং তৈরি করা ভার্চুয়াল পরিবেশ থেকে Python নির্বাচন করুন<br>3. ডিপেনডেন্সি ইনস্টল করুন (ডেভ ডিপেনডেন্সি সহ): `pip install -e .[dev]` | 

পরিবেশ সেটআপ করার পরে, আপনি MCP ক্লায়েন্ট হিসেবে Agent Builder ব্যবহার করে আপনার লোকাল ডেভ মেশিনে সার্ভার চালাতে পারেন:
1. VS Code ডিবাগ প্যানেল খুলুন। `Debug in Agent Builder` নির্বাচন করুন অথবা `F5` চাপুন MCP সার্ভার ডিবাগিং শুরু করতে।
2. AI Toolkit Agent Builder ব্যবহার করে [এই প্রম্পট](../../../../../../../../../../../open_prompt_builder) দিয়ে সার্ভার পরীক্ষা করুন। সার্ভার স্বয়ংক্রিয়ভাবে Agent Builder-এর সাথে সংযুক্ত হবে।
3. `Run` ক্লিক করুন প্রম্পট দিয়ে সার্ভার পরীক্ষা করতে।

**অভিনন্দন**! আপনি সফলভাবে Agent Builder ব্যবহার করে MCP ক্লায়েন্ট হিসেবে আপনার লোকাল ডেভ মেশিনে Weather MCP Server চালিয়েছেন।
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## টেমপ্লেটে কী অন্তর্ভুক্ত রয়েছে

| ফোল্ডার / ফাইল| বিষয়বস্তু                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | ডিবাগিংয়ের জন্য VSCode ফাইল                 |
| `.aitk`      | AI Toolkit-এর জন্য কনফিগারেশন               |
| `src`        | Weather MCP Server-এর সোর্স কোড             |

## Weather MCP Server কীভাবে ডিবাগ করবেন

> নোট:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) হল MCP সার্ভার পরীক্ষা এবং ডিবাগ করার জন্য একটি ভিজ্যুয়াল ডেভেলপার টুল।
> - সমস্ত ডিবাগিং মোড ব্রেকপয়েন্ট সমর্থন করে, তাই আপনি টুল ইমপ্লিমেন্টেশনের কোডে ব্রেকপয়েন্ট যোগ করতে পারেন।

## উপলব্ধ টুলস

### Weather Tool
`get_weather` টুলটি নির্দিষ্ট অবস্থানের জন্য মক আবহাওয়ার তথ্য সরবরাহ করে।

| প্যারামিটার | টাইপ | বিবরণ |
| --------- | ---- | ----------- |
| `location` | string | অবস্থান যার জন্য আবহাওয়া তথ্য প্রয়োজন (যেমন, শহরের নাম, রাজ্য, বা কোঅর্ডিনেটস) |

### Git Clone Tool
`git_clone_repo` টুলটি একটি গিট রিপোজিটরি নির্দিষ্ট ফোল্ডারে ক্লোন করে।

| প্যারামিটার | টাইপ | বিবরণ |
| --------- | ---- | ----------- |
| `repo_url` | string | ক্লোন করার জন্য গিট রিপোজিটরির URL |
| `target_folder` | string | ফোল্ডারের পথ যেখানে রিপোজিটরি ক্লোন করা হবে |

টুলটি একটি JSON অবজেক্ট প্রদান করে:
- `success`: অপারেশন সফল হয়েছে কিনা তা নির্দেশ করে এমন একটি বুলিয়ান
- `target_folder` বা `error`: ক্লোন করা রিপোজিটরির পথ বা একটি ত্রুটি বার্তা

### VS Code Open Tool
`open_in_vscode` টুলটি VS Code বা VS Code Insiders অ্যাপ্লিকেশনে একটি ফোল্ডার খুলে।

| প্যারামিটার | টাইপ | বিবরণ |
| --------- | ---- | ----------- |
| `folder_path` | string | ফোল্ডারের পথ যা খুলতে হবে |
| `use_insiders` | boolean (ঐচ্ছিক) | নিয়মিত VS Code-এর পরিবর্তে VS Code Insiders ব্যবহার করা হবে কিনা |

টুলটি একটি JSON অবজেক্ট প্রদান করে:
- `success`: অপারেশন সফল হয়েছে কিনা তা নির্দেশ করে এমন একটি বুলিয়ান
- `message` বা `error`: একটি নিশ্চিতকরণ বার্তা বা একটি ত্রুটি বার্তা

| ডিবাগ মোড | বিবরণ | ডিবাগ করার ধাপসমূহ |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit-এর মাধ্যমে Agent Builder-এ MCP সার্ভার ডিবাগ করুন। | 1. VS Code ডিবাগ প্যানেল খুলুন। `Debug in Agent Builder` নির্বাচন করুন এবং `F5` চাপুন MCP সার্ভার ডিবাগিং শুরু করতে।<br>2. AI Toolkit Agent Builder ব্যবহার করে [এই প্রম্পট](../../../../../../../../../../../open_prompt_builder) দিয়ে সার্ভার পরীক্ষা করুন। সার্ভার স্বয়ংক্রিয়ভাবে Agent Builder-এর সাথে সংযুক্ত হবে।<br>3. `Run` ক্লিক করুন প্রম্পট দিয়ে সার্ভার পরীক্ষা করতে। |
| MCP Inspector | MCP Inspector ব্যবহার করে MCP সার্ভার ডিবাগ করুন। | 1. [Node.js](https://nodejs.org/) ইনস্টল করুন<br> 2. Inspector সেটআপ করুন: `cd inspector` && `npm install` <br> 3. VS Code ডিবাগ প্যানেল খুলুন। `Debug SSE in Inspector (Edge)` বা `Debug SSE in Inspector (Chrome)` নির্বাচন করুন। `F5` চাপুন ডিবাগিং শুরু করতে।<br> 4. MCP Inspector ব্রাউজারে চালু হলে, `Connect` বোতাম ক্লিক করুন এই MCP সার্ভারের সাথে সংযোগ করতে।<br> 5. এরপর আপনি `List Tools` করতে পারেন, একটি টুল নির্বাচন করতে পারেন, প্যারামিটার ইনপুট করতে পারেন এবং `Run Tool` ক্লিক করে আপনার সার্ভার কোড ডিবাগ করতে পারেন।<br> |

## ডিফল্ট পোর্ট এবং কাস্টমাইজেশন

| ডিবাগ মোড | পোর্ট | সংজ্ঞা | কাস্টমাইজেশন | নোট |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) সম্পাদনা করে উপরের পোর্ট পরিবর্তন করুন। | N/A |
| MCP Inspector | 3001 (Server); 5173 এবং 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) সম্পাদনা করে উপরের পোর্ট পরিবর্তন করুন।| N/A |

## মতামত

যদি এই টেমপ্লেটের জন্য আপনার কোনো মতামত বা পরামর্শ থাকে, তাহলে [AI Toolkit GitHub রিপোজিটরি](https://github.com/microsoft/vscode-ai-toolkit/issues)-তে একটি ইস্যু খুলুন।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।