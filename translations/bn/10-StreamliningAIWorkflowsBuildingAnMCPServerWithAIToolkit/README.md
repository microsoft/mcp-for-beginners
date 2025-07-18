<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "787440926586cd064b0899fd1c514f52",
  "translation_date": "2025-07-14T07:03:41+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md",
  "language_code": "bn"
}
-->
# AI ওয়ার্কফ্লো সহজতর করা: AI Toolkit দিয়ে MCP সার্ভার তৈরি

[![MCP Version](https://img.shields.io/badge/MCP-1.9.3-blue.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://python.org)
[![VS Code](https://img.shields.io/badge/VS%20Code-Latest-orange.svg)](https://code.visualstudio.com/)

![logo](../../../translated_images/logo.ec93918ec338dadde1715c8aaf118079e0ed0502e9efdfcc84d6a0f4a9a70ae8.bn.png)

## 🎯 পরিচিতি

স্বাগতম **Model Context Protocol (MCP) ওয়ার্কশপে**! এই ব্যাপক হ্যান্ডস-অন ওয়ার্কশপে দুটি আধুনিক প্রযুক্তি একত্রিত হয়েছে যা AI অ্যাপ্লিকেশন ডেভেলপমেন্টে বিপ্লব ঘটাবে:

- **🔗 Model Context Protocol (MCP)**: AI-টুল ইন্টিগ্রেশনের জন্য একটি ওপেন স্ট্যান্ডার্ড
- **🛠️ AI Toolkit for Visual Studio Code (AITK)**: মাইক্রোসফটের শক্তিশালী AI ডেভেলপমেন্ট এক্সটেনশন

### 🎓 আপনি কী শিখবেন

এই ওয়ার্কশপ শেষে, আপনি এমন বুদ্ধিমান অ্যাপ্লিকেশন তৈরি করতে সক্ষম হবেন যা AI মডেলকে বাস্তব জগতের টুল ও সার্ভিসের সাথে সংযুক্ত করে। স্বয়ংক্রিয় টেস্টিং থেকে শুরু করে কাস্টম API ইন্টিগ্রেশন পর্যন্ত, আপনি জটিল ব্যবসায়িক সমস্যার সমাধানে ব্যবহারিক দক্ষতা অর্জন করবেন।

## 🏗️ প্রযুক্তি স্ট্যাক

### 🔌 Model Context Protocol (MCP)

MCP হলো AI-এর জন্য **"USB-C"** — একটি সার্বজনীন স্ট্যান্ডার্ড যা AI মডেলকে বাহ্যিক টুল ও ডেটা সোর্সের সাথে সংযুক্ত করে।

**✨ প্রধান বৈশিষ্ট্য:**
- 🔄 **স্ট্যান্ডার্ডাইজড ইন্টিগ্রেশন**: AI-টুল সংযোগের জন্য সার্বজনীন ইন্টারফেস
- 🏛️ **ফ্লেক্সিবল আর্কিটেকচার**: লোকাল ও রিমোট সার্ভার stdio/SSE ট্রান্সপোর্টের মাধ্যমে
- 🧰 **সমৃদ্ধ ইকোসিস্টেম**: এক প্রোটোকলে টুল, প্রম্পট ও রিসোর্স
- 🔒 **এন্টারপ্রাইজ-রেডি**: বিল্ট-ইন সিকিউরিটি ও নির্ভরযোগ্যতা

**🎯 MCP কেন গুরুত্বপূর্ণ:**
যেমন USB-C তারের জটিলতা দূর করেছে, MCP AI ইন্টিগ্রেশনের জটিলতা দূর করে। এক প্রোটোকল, অসীম সম্ভাবনা।

### 🤖 AI Toolkit for Visual Studio Code (AITK)

মাইক্রোসফটের প্রধান AI ডেভেলপমেন্ট এক্সটেনশন যা VS Code কে AI শক্তিধর প্ল্যাটফর্মে রূপান্তর করে।

**🚀 মূল ক্ষমতা:**
- 📦 **মডেল ক্যাটালগ**: Azure AI, GitHub, Hugging Face, Ollama থেকে মডেল অ্যাক্সেস
- ⚡ **লোকাল ইনফারেন্স**: ONNX-অপ্টিমাইজড CPU/GPU/NPU এক্সিকিউশন
- 🏗️ **এজেন্ট বিল্ডার**: MCP ইন্টিগ্রেশনসহ ভিজ্যুয়াল AI এজেন্ট ডেভেলপমেন্ট
- 🎭 **মাল্টি-মোডাল**: টেক্সট, ভিশন, ও স্ট্রাকচার্ড আউটপুট সাপোর্ট

**💡 ডেভেলপমেন্ট সুবিধা:**
- জিরো-কনফিগ মডেল ডিপ্লয়মেন্ট
- ভিজ্যুয়াল প্রম্পট ইঞ্জিনিয়ারিং
- রিয়েল-টাইম টেস্টিং প্লেগ্রাউন্ড
- নির্বিঘ্ন MCP সার্ভার ইন্টিগ্রেশন

## 📚 শেখার যাত্রা

### [🚀 মডিউল ১: AI Toolkit এর মূল বিষয়াবলী](./lab1/README.md)
**সময়কাল**: ১৫ মিনিট
- 🛠️ VS Code এর জন্য AI Toolkit ইনস্টল ও কনফিগার করা
- 🗂️ মডেল ক্যাটালগ অন্বেষণ (GitHub, ONNX, OpenAI, Anthropic, Google থেকে ১০০+ মডেল)
- 🎮 রিয়েল-টাইম মডেল টেস্টিং এর জন্য ইন্টারেক্টিভ প্লেগ্রাউন্ডে দক্ষতা অর্জন
- 🤖 Agent Builder দিয়ে প্রথম AI এজেন্ট তৈরি
- 📊 বিল্ট-ইন মেট্রিক্স (F1, প্রাসঙ্গিকতা, সাদৃশ্য, সামঞ্জস্য) দিয়ে মডেল পারফরম্যান্স মূল্যায়ন
- ⚡ ব্যাচ প্রসেসিং ও মাল্টি-মোডাল সাপোর্ট শেখা

**🎯 শেখার ফলাফল**: AITK এর ক্ষমতা নিয়ে সম্পূর্ণ বোঝাপড়া সহ কার্যকর AI এজেন্ট তৈরি করা

### [🌐 মডিউল ২: MCP ও AI Toolkit এর মূল বিষয়াবলী](./lab2/README.md)
**সময়কাল**: ২০ মিনিট
- 🧠 Model Context Protocol (MCP) আর্কিটেকচার ও ধারণা আয়ত্ত করা
- 🌐 মাইক্রোসফটের MCP সার্ভার ইকোসিস্টেম অন্বেষণ
- 🤖 Playwright MCP সার্ভার ব্যবহার করে ব্রাউজার অটোমেশন এজেন্ট তৈরি
- 🔧 MCP সার্ভারগুলো AI Toolkit Agent Builder এর সাথে ইন্টিগ্রেট করা
- 📊 এজেন্টের মধ্যে MCP টুল কনফিগার ও টেস্ট করা
- 🚀 MCP-চালিত এজেন্ট প্রোডাকশনে রপ্তানি ও ডিপ্লয় করা

**🎯 শেখার ফলাফল**: MCP এর মাধ্যমে বাহ্যিক টুলস দিয়ে সুপারচার্জড AI এজেন্ট ডিপ্লয় করা

### [🔧 মডিউল ৩: AI Toolkit দিয়ে উন্নত MCP ডেভেলপমেন্ট](./lab3/README.md)
**সময়কাল**: ২০ মিনিট
- 💻 AI Toolkit ব্যবহার করে কাস্টম MCP সার্ভার তৈরি
- 🐍 সর্বশেষ MCP Python SDK (v1.9.3) কনফিগার ও ব্যবহার
- 🔍 MCP Inspector দিয়ে ডিবাগিং সেটআপ ও ব্যবহার
- 🛠️ প্রফেশনাল ডিবাগিং ওয়ার্কফ্লো সহ Weather MCP Server তৈরি
- 🧪 Agent Builder ও Inspector উভয় পরিবেশে MCP সার্ভার ডিবাগ করা

**🎯 শেখার ফলাফল**: আধুনিক টুলিং দিয়ে কাস্টম MCP সার্ভার ডেভেলপ ও ডিবাগ করা

### [🐙 মডিউল ৪: বাস্তব MCP ডেভেলপমেন্ট - কাস্টম GitHub ক্লোন সার্ভার](./lab4/README.md)
**সময়কাল**: ৩০ মিনিট
- 🏗️ ডেভেলপমেন্ট ওয়ার্কফ্লোর জন্য বাস্তব GitHub Clone MCP Server তৈরি
- 🔄 স্মার্ট রিপোজিটরি ক্লোনিং বাস্তবায়ন, ভ্যালিডেশন ও এরর হ্যান্ডলিং সহ
- 📁 বুদ্ধিমান ডিরেক্টরি ম্যানেজমেন্ট ও VS Code ইন্টিগ্রেশন তৈরি
- 🤖 কাস্টম MCP টুলস সহ GitHub Copilot Agent Mode ব্যবহার
- 🛡️ প্রোডাকশন-রেডি নির্ভরযোগ্যতা ও ক্রস-প্ল্যাটফর্ম সামঞ্জস্য প্রয়োগ

**🎯 শেখার ফলাফল**: বাস্তব ডেভেলপমেন্ট ওয়ার্কফ্লো সহজতর করার জন্য প্রোডাকশন-রেডি MCP সার্ভার ডিপ্লয় করা

## 💡 বাস্তব জীবনের অ্যাপ্লিকেশন ও প্রভাব

### 🏢 এন্টারপ্রাইজ ব্যবহারের ক্ষেত্র

#### 🔄 DevOps অটোমেশন
আপনার ডেভেলপমেন্ট ওয়ার্কফ্লোকে বুদ্ধিমান অটোমেশনের মাধ্যমে রূপান্তর করুন:
- **স্মার্ট রিপোজিটরি ম্যানেজমেন্ট**: AI-চালিত কোড রিভিউ ও মার্জ সিদ্ধান্ত
- **ইন্টেলিজেন্ট CI/CD**: কোড পরিবর্তনের ভিত্তিতে স্বয়ংক্রিয় পাইপলাইন অপ্টিমাইজেশন
- **ইস্যু ট্রায়াজ**: স্বয়ংক্রিয় বাগ শ্রেণীবিভাগ ও অ্যাসাইনমেন্ট

#### 🧪 কোয়ালিটি অ্যাসিউরেন্স বিপ্লব
AI-চালিত অটোমেশনের মাধ্যমে টেস্টিং উন্নত করুন:
- **ইন্টেলিজেন্ট টেস্ট জেনারেশন**: স্বয়ংক্রিয়ভাবে বিস্তৃত টেস্ট স্যুট তৈরি
- **ভিজ্যুয়াল রিগ্রেশন টেস্টিং**: AI-চালিত UI পরিবর্তন সনাক্তকরণ
- **পারফরম্যান্স মনিটরিং**: সক্রিয় সমস্যা সনাক্তকরণ ও সমাধান

#### 📊 ডেটা পাইপলাইন ইন্টেলিজেন্স
স্মার্ট ডেটা প্রসেসিং ওয়ার্কফ্লো তৈরি করুন:
- **অ্যাডাপটিভ ETL প্রসেস**: স্ব-অপ্টিমাইজিং ডেটা ট্রান্সফরমেশন
- **অ্যানোমালি ডিটেকশন**: রিয়েল-টাইম ডেটা কোয়ালিটি মনিটরিং
- **ইন্টেলিজেন্ট রাউটিং**: স্মার্ট ডেটা ফ্লো ম্যানেজমেন্ট

#### 🎧 কাস্টমার এক্সপেরিয়েন্স উন্নয়ন
অসাধারণ গ্রাহক যোগাযোগ তৈরি করুন:
- **কনটেক্সট-অ্যাওয়ার সাপোর্ট**: গ্রাহকের ইতিহাস অ্যাক্সেস সহ AI এজেন্ট
- **প্রোঅ্যাকটিভ ইস্যু রেজলিউশন**: পূর্বাভাসভিত্তিক গ্রাহক সেবা
- **মাল্টি-চ্যানেল ইন্টিগ্রেশন**: প্ল্যাটফর্ম জুড়ে একক AI অভিজ্ঞতা

## 🛠️ প্রয়োজনীয়তা ও সেটআপ

### 💻 সিস্টেমের চাহিদা

| উপাদান | প্রয়োজনীয়তা | মন্তব্য |
|---------|---------------|---------|
| **অপারেটিং সিস্টেম** | Windows 10+, macOS 10.15+, Linux | যেকোন আধুনিক OS |
| **Visual Studio Code** | সর্বশেষ স্থিতিশীল সংস্করণ | AITK এর জন্য প্রয়োজনীয় |
| **Node.js** | v18.0+ এবং npm | MCP সার্ভার ডেভেলপমেন্টের জন্য |
| **Python** | 3.10+ | Python MCP সার্ভারের জন্য ঐচ্ছিক |
| **মেমোরি** | ন্যূনতম ৮GB RAM | লোকাল মডেলের জন্য ১৬GB সুপারিশকৃত |

### 🔧 ডেভেলপমেন্ট পরিবেশ

#### সুপারিশকৃত VS Code এক্সটেনশনসমূহ
- **AI Toolkit** (ms-windows-ai-studio.windows-ai-studio)
- **Python** (ms-python.python)
- **Python Debugger** (ms-python.debugpy)
- **GitHub Copilot** (GitHub.copilot) - ঐচ্ছিক কিন্তু সহায়ক

#### ঐচ্ছিক টুলস
- **uv**: আধুনিক Python প্যাকেজ ম্যানেজার
- **MCP Inspector**: MCP সার্ভারের জন্য ভিজ্যুয়াল ডিবাগিং টুল
- **Playwright**: ওয়েব অটোমেশন উদাহরণের জন্য

## 🎖️ শেখার ফলাফল ও সার্টিফিকেশন পথ

### 🏆 দক্ষতা অর্জনের তালিকা

এই ওয়ার্কশপ সম্পন্ন করে আপনি নিম্নলিখিত দক্ষতায় পারদর্শী হবেন:

#### 🎯 মূল দক্ষতা
- [ ] **MCP প্রোটোকল আয়ত্ত**: আর্কিটেকচার ও ইমপ্লিমেন্টেশন প্যাটার্ন গভীরভাবে বোঝা
- [ ] **AITK দক্ষতা**: দ্রুত ডেভেলপমেন্টের জন্য AI Toolkit এর উচ্চতর ব্যবহার
- [ ] **কাস্টম সার্ভার ডেভেলপমেন্ট**: MCP সার্ভার তৈরি, ডিপ্লয় ও রক্ষণাবেক্ষণ
- [ ] **টুল ইন্টিগ্রেশন উৎকর্ষ**: বিদ্যমান ডেভেলপমেন্ট ওয়ার্কফ্লোর সাথে AI নির্বিঘ্ন সংযোগ
- [ ] **সমস্যা সমাধানে প্রয়োগ**: শেখা দক্ষতা বাস্তব ব্যবসায়িক সমস্যায় প্রয়োগ

#### 🔧 প্রযুক্তিগত দক্ষতা
- [ ] VS Code এ AI Toolkit সেটআপ ও কনফিগার করা
- [ ] কাস্টম MCP সার্ভার ডিজাইন ও ইমপ্লিমেন্ট করা
- [ ] MCP আর্কিটেকচারের সাথে GitHub মডেল ইন্টিগ্রেট করা
- [ ] Playwright দিয়ে স্বয়ংক্রিয় টেস্টিং ওয়ার্কফ্লো তৈরি
- [ ] প্রোডাকশনে AI এজেন্ট ডিপ্লয় করা
- [ ] MCP সার্ভার পারফরম্যান্স ডিবাগ ও অপ্টিমাইজ করা

#### 🚀 উন্নত ক্ষমতা
- [ ] এন্টারপ্রাইজ-স্কেল AI ইন্টিগ্রেশন আর্কিটেকচার ডিজাইন করা
- [ ] AI অ্যাপ্লিকেশনের জন্য সিকিউরিটি সেরা অনুশীলন বাস্তবায়ন
- [ ] স্কেলেবল MCP সার্ভার আর্কিটেকচার ডিজাইন করা
- [ ] নির্দিষ্ট ডোমেইনের জন্য কাস্টম টুল চেইন তৈরি করা
- [ ] AI-নেটিভ ডেভেলপমেন্টে অন্যদের মেন্টরিং করা

## 📖 অতিরিক্ত রিসোর্স
- [MCP স্পেসিফিকেশন](https://modelcontextprotocol.io/docs)
- [AI Toolkit GitHub রিপোজিটরি](https://github.com/microsoft/vscode-ai-toolkit)
- [সাম্পল MCP সার্ভার কালেকশন](https://github.com/modelcontextprotocol/servers)
- [সেরা অনুশীলন গাইড](https://modelcontextprotocol.io/docs/best-practices)

---

**🚀 আপনার AI ডেভেলপমেন্ট ওয়ার্কফ্লোতে বিপ্লব ঘটাতে প্রস্তুত?**

চলুন MCP ও AI Toolkit দিয়ে বুদ্ধিমান অ্যাপ্লিকেশনের ভবিষ্যত একসাথে গড়ি!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।