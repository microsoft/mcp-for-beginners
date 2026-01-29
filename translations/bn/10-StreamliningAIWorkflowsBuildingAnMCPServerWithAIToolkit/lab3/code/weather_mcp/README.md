# Weather MCP Server

এটি একটি নমুনা MCP Server যা Python-এ তৈরি এবং আবহাওয়া টুলসের জন্য মক রেসপন্স প্রদান করে। এটি আপনার নিজস্ব MCP Server তৈরির জন্য একটি ভিত্তি হিসেবে ব্যবহার করা যেতে পারে। এতে নিম্নলিখিত ফিচারগুলো অন্তর্ভুক্ত রয়েছে:

- **Weather Tool**: একটি টুল যা প্রদত্ত অবস্থানের উপর ভিত্তি করে মক করা আবহাওয়ার তথ্য প্রদান করে।
- **Connect to Agent Builder**: একটি ফিচার যা MCP সার্ভারকে Agent Builder-এর সাথে সংযুক্ত করে পরীক্ষণ ও ডিবাগিংয়ের জন্য।
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: MCP Inspector ব্যবহার করে MCP Server ডিবাগ করার সুবিধা।

## Weather MCP Server টেমপ্লেট দিয়ে শুরু করুন

> **প্রয়োজনীয়তা**
>
> আপনার লোকাল ডেভ মেশিনে MCP Server চালানোর জন্য আপনার প্রয়োজন হবে:
>
> - [Python](https://www.python.org/)
> - (*ঐচ্ছিক - যদি আপনি uv পছন্দ করেন*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## পরিবেশ প্রস্তুত করুন

এই প্রকল্পের জন্য পরিবেশ সেটআপ করার দুটি পদ্ধতি আছে। আপনার পছন্দ অনুযায়ী যেকোনো একটি বেছে নিতে পারেন।

> Note: ভার্চুয়াল এনভায়রনমেন্ট তৈরি করার পর VSCode বা টার্মিনাল রিলোড করুন যাতে ভার্চুয়াল এনভায়রনমেন্টের পাইথন ব্যবহার হয়।

| পদ্ধতি | ধাপসমূহ |
| -------- | ----- |
| `uv` ব্যবহার করে | 1. ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন: `uv venv` <br>2. VSCode কমান্ড "***Python: Select Interpreter***" চালিয়ে তৈরি ভার্চুয়াল এনভায়রনমেন্টের পাইথন নির্বাচন করুন <br>3. ডিপেন্ডেন্সি ইনস্টল করুন (ডেভ ডিপেন্ডেন্সিসহ): `uv pip install -r pyproject.toml --extra dev` |
| `pip` ব্যবহার করে | 1. ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন: `python -m venv .venv` <br>2. VSCode কমান্ড "***Python: Select Interpreter***" চালিয়ে তৈরি ভার্চুয়াল এনভায়রনমেন্টের পাইথন নির্বাচন করুন<br>3. ডিপেন্ডেন্সি ইনস্টল করুন (ডেভ ডিপেন্ডেন্সিসহ): `pip install -e .[dev]` |

পরিবেশ সেটআপ করার পর, Agent Builder কে MCP Client হিসেবে ব্যবহার করে আপনার লোকাল ডেভ মেশিনে সার্ভার চালাতে পারেন:
1. VS Code এর Debug প্যানেল খুলুন। `Debug in Agent Builder` নির্বাচন করুন অথবা MCP সার্ভার ডিবাগ শুরু করতে `F5` চাপুন।
2. AI Toolkit Agent Builder ব্যবহার করে [এই প্রম্পট](../../../../../../../../../../open_prompt_builder) দিয়ে সার্ভার পরীক্ষা করুন। সার্ভার স্বয়ংক্রিয়ভাবে Agent Builder-এ সংযুক্ত হবে।
3. প্রম্পট দিয়ে সার্ভার পরীক্ষা করতে `Run` ক্লিক করুন।

**অভিনন্দন**! আপনি সফলভাবে Agent Builder কে MCP Client হিসেবে ব্যবহার করে আপনার লোকাল ডেভ মেশিনে Weather MCP Server চালিয়েছেন।
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## টেমপ্লেটে কি কি অন্তর্ভুক্ত আছে

| ফোল্ডার / ফাইল | বিষয়বস্তু                                  |
| --------------- | ------------------------------------------ |
| `.vscode`       | ডিবাগিংয়ের জন্য VSCode ফাইলসমূহ           |
| `.aitk`         | AI Toolkit এর কনফিগারেশনসমূহ              |
| `src`           | weather mcp server এর সোর্স কোড             |

## Weather MCP Server কীভাবে ডিবাগ করবেন

> Notes:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) MCP সার্ভার টেস্ট ও ডিবাগ করার জন্য একটি ভিজ্যুয়াল ডেভেলপার টুল।
> - সব ডিবাগ মোডে ব্রেকপয়েন্ট সাপোর্ট করে, তাই আপনি টুল ইমপ্লিমেন্টেশন কোডে ব্রেকপয়েন্ট যোগ করতে পারবেন।

| ডিবাগ মোড | বর্ণনা | ডিবাগ করার ধাপসমূহ |
| ---------- | ----------- | ------------------ |
| Agent Builder | AI Toolkit এর মাধ্যমে Agent Builder-এ MCP সার্ভার ডিবাগ করুন। | 1. VS Code এর Debug প্যানেল খুলুন। `Debug in Agent Builder` নির্বাচন করে `F5` চাপুন MCP সার্ভার ডিবাগ শুরু করতে।<br>2. AI Toolkit Agent Builder ব্যবহার করে [এই প্রম্পট](../../../../../../../../../../open_prompt_builder) দিয়ে সার্ভার পরীক্ষা করুন। সার্ভার স্বয়ংক্রিয়ভাবে Agent Builder-এ সংযুক্ত হবে।<br>3. প্রম্পট দিয়ে সার্ভার পরীক্ষা করতে `Run` ক্লিক করুন। |
| MCP Inspector | MCP Inspector ব্যবহার করে MCP সার্ভার ডিবাগ করুন। | 1. [Node.js](https://nodejs.org/) ইনস্টল করুন।<br>2. Inspector সেটআপ করুন: `cd inspector` && `npm install` <br>3. VS Code এর Debug প্যানেল খুলুন। `Debug SSE in Inspector (Edge)` অথবা `Debug SSE in Inspector (Chrome)` নির্বাচন করুন। ডিবাগ শুরু করতে `F5` চাপুন।<br>4. MCP Inspector ব্রাউজারে চালু হলে, `Connect` বাটনে ক্লিক করে MCP সার্ভারের সাথে সংযুক্ত করুন।<br>5. এরপর আপনি `List Tools` থেকে একটি টুল নির্বাচন করে প্যারামিটার ইনপুট দিয়ে `Run Tool` ক্লিক করে সার্ভার কোড ডিবাগ করতে পারবেন।<br> |

## ডিফল্ট পোর্ট এবং কাস্টমাইজেশন

| ডিবাগ মোড | পোর্টসমূহ | সংজ্ঞাসমূহ | কাস্টমাইজেশন | নোট |
| ---------- | --------- | ----------- | ------------- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | উপরের পোর্ট পরিবর্তনের জন্য [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [__init__.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) সম্পাদনা করুন। | প্রযোজ্য নয় |
| MCP Inspector | 3001 (সার্ভার); 5173 এবং 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | উপরের পোর্ট পরিবর্তনের জন্য [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [__init__.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) সম্পাদনা করুন। | প্রযোজ্য নয় |

## প্রতিক্রিয়া

যদি আপনার এই টেমপ্লেট সম্পর্কে কোনো প্রতিক্রিয়া বা পরামর্শ থাকে, অনুগ্রহ করে [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)-এ একটি ইস্যু খুলুন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।