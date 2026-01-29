# Calculator LLM Client

একটি Java অ্যাপ্লিকেশন যা LangChain4j ব্যবহার করে MCP (Model Context Protocol) ক্যালকুলেটর সার্ভিসের সাথে GitHub Models ইন্টিগ্রেশন কিভাবে করা যায় তা প্রদর্শন করে।

## প্রয়োজনীয়তা

- Java 21 বা তার উপরে
- Maven 3.6+ (অথবা অন্তর্ভুক্ত Maven wrapper ব্যবহার করুন)
- GitHub Models অ্যাক্সেস সহ একটি GitHub অ্যাকাউন্ট
- `http://localhost:8080` এ চলমান MCP ক্যালকুলেটর সার্ভিস

## GitHub Token পাওয়ার পদ্ধতি

এই অ্যাপ্লিকেশন GitHub Models ব্যবহার করে, যার জন্য একটি GitHub personal access token প্রয়োজন। আপনার token পাওয়ার জন্য নিচের ধাপগুলো অনুসরণ করুন:

### 1. GitHub Models অ্যাক্সেস করুন
1. যান [GitHub Models](https://github.com/marketplace/models)
2. আপনার GitHub অ্যাকাউন্ট দিয়ে সাইন ইন করুন
3. যদি আগে না করে থাকেন, GitHub Models অ্যাক্সেসের জন্য অনুরোধ করুন

### 2. Personal Access Token তৈরি করুন
1. যান [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. "Generate new token" → "Generate new token (classic)" ক্লিক করুন
3. আপনার token এর জন্য একটি বর্ণনামূলক নাম দিন (যেমন, "MCP Calculator Client")
4. প্রয়োজন অনুযায়ী মেয়াদ নির্ধারণ করুন
5. নিচের স্কোপগুলো নির্বাচন করুন:
   - `repo` (যদি প্রাইভেট রিপোজিটরি অ্যাক্সেস করতে হয়)
   - `user:email`
6. "Generate token" ক্লিক করুন
7. **গুরুত্বপূর্ণ**: token তৈরি হওয়ার পর তা অবিলম্বে কপি করে রাখুন - পরে আর দেখতে পারবেন না!

### 3. Environment Variable সেট করুন

#### Windows (Command Prompt) এ:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) এ:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux এ:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## সেটআপ এবং ইনস্টলেশন

1. **প্রজেক্ট ডিরেক্টরিতে ক্লোন করুন বা যান**

2. **ডিপেন্ডেন্সি ইনস্টল করুন**:
   ```cmd
   mvnw clean install
   ```
   অথবা যদি আপনার সিস্টেমে Maven গ্লোবালি ইনস্টল থাকে:
   ```cmd
   mvn clean install
   ```

3. **Environment variable সেট করুন** (উপরের "Getting the GitHub Token" অংশ দেখুন)

4. **MCP Calculator Service চালু করুন**:
   নিশ্চিত করুন chapter 1 এর MCP calculator সার্ভিস `http://localhost:8080/sse` এ চলছে। ক্লায়েন্ট চালানোর আগে এটি চালু থাকতে হবে।

## অ্যাপ্লিকেশন চালানো

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## অ্যাপ্লিকেশন কী করে

অ্যাপ্লিকেশনটি ক্যালকুলেটর সার্ভিসের সাথে তিনটি প্রধান ইন্টারঅ্যাকশন প্রদর্শন করে:

1. **যোগ**: 24.5 এবং 17.3 এর যোগফল হিসাব করে
2. **বর্গমূল**: 144 এর বর্গমূল হিসাব করে
3. **সাহায্য**: উপলব্ধ ক্যালকুলেটর ফাংশনগুলো দেখায়

## প্রত্যাশিত আউটপুট

সফলভাবে চালানোর সময়, আপনি নিচের মতো আউটপুট দেখতে পাবেন:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## সমস্যা সমাধান

### সাধারণ সমস্যা

1. **"GITHUB_TOKEN environment variable not set"**
   - নিশ্চিত করুন `GITHUB_TOKEN` environment variable সেট করেছেন
   - সেট করার পর টার্মিনাল/কমান্ড প্রম্পট রিস্টার্ট করুন

2. **"Connection refused to localhost:8080"**
   - MCP calculator সার্ভিস 8080 পোর্টে চলছে কিনা নিশ্চিত করুন
   - অন্য কোনো সার্ভিস 8080 পোর্ট ব্যবহার করছে কিনা চেক করুন

3. **"Authentication failed"**
   - আপনার GitHub token বৈধ এবং সঠিক অনুমতি আছে কিনা যাচাই করুন
   - GitHub Models অ্যাক্সেস আছে কিনা নিশ্চিত করুন

4. **Maven build ত্রুটি**
   - Java 21 বা তার উপরে ব্যবহার করছেন কিনা দেখুন: `java -version`
   - বিল্ড ক্লিন করুন: `mvnw clean`

### ডিবাগিং

ডিবাগ লগিং চালু করতে, অ্যাপ্লিকেশন চালানোর সময় নিচের JVM আর্গুমেন্ট যোগ করুন:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## কনফিগারেশন

অ্যাপ্লিকেশনটি কনফিগার করা হয়েছে:
- GitHub Models `gpt-4.1-nano` মডেল ব্যবহার করতে
- MCP সার্ভিসের সাথে `http://localhost:8080/sse` এ সংযোগ করতে
- অনুরোধের জন্য ৬০ সেকেন্ড টাইমআউট ব্যবহার করতে
- ডিবাগিংয়ের জন্য রিকোয়েস্ট/রেসপন্স লগিং চালু রাখতে

## ডিপেন্ডেন্সি

এই প্রজেক্টে ব্যবহৃত প্রধান ডিপেন্ডেন্সি:
- **LangChain4j**: AI ইন্টিগ্রেশন এবং টুল ম্যানেজমেন্টের জন্য
- **LangChain4j MCP**: Model Context Protocol সাপোর্টের জন্য
- **LangChain4j GitHub Models**: GitHub Models ইন্টিগ্রেশনের জন্য
- **Spring Boot**: অ্যাপ্লিকেশন ফ্রেমওয়ার্ক এবং ডিপেন্ডেন্সি ইনজেকশনের জন্য

## লাইসেন্স

এই প্রজেক্ট Apache License 2.0 এর অধীনে লাইসেন্সকৃত - বিস্তারিত জানতে [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ফাইল দেখুন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।