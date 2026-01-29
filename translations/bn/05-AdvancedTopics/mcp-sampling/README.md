# মডেল কনটেক্সট প্রোটোকলে স্যাম্পলিং

স্যাম্পলিং একটি শক্তিশালী MCP ফিচার যা সার্ভারকে ক্লায়েন্টের মাধ্যমে LLM কমপ্লিশন অনুরোধ করার সুযোগ দেয়, যা উন্নত এজেন্টিক আচরণ সক্ষম করে এবং নিরাপত্তা ও গোপনীয়তা বজায় রাখে। সঠিক স্যাম্পলিং কনফিগারেশন রেসপন্সের গুণগত মান এবং পারফরম্যান্স উল্লেখযোগ্যভাবে উন্নত করতে পারে। MCP একটি স্ট্যান্ডার্ডাইজড পদ্ধতি প্রদান করে যা মডেল কীভাবে টেক্সট তৈরি করে তা নিয়ন্ত্রণ করে, যেখানে নির্দিষ্ট প্যারামিটারগুলো র‍্যান্ডমনেস, সৃজনশীলতা এবং সামঞ্জস্য প্রভাবিত করে।

## পরিচিতি

এই পাঠে, আমরা MCP অনুরোধে স্যাম্পলিং প্যারামিটার কনফিগার করা এবং স্যাম্পলিংয়ের অন্তর্নিহিত প্রোটোকল মেকানিজম বুঝব।

## শেখার উদ্দেশ্য

এই পাঠের শেষে আপনি সক্ষম হবেন:

- MCP-তে উপলব্ধ মূল স্যাম্পলিং প্যারামিটারগুলো বুঝতে।
- বিভিন্ন ব্যবহারের ক্ষেত্রে স্যাম্পলিং প্যারামিটার কনফিগার করতে।
- পুনরুত্পাদনযোগ্য ফলাফলের জন্য ডিটারমিনিস্টিক স্যাম্পলিং বাস্তবায়ন করতে।
- প্রসঙ্গ এবং ব্যবহারকারীর পছন্দ অনুযায়ী স্যাম্পলিং প্যারামিটার ডায়নামিক্যালি সামঞ্জস্য করতে।
- বিভিন্ন পরিস্থিতিতে মডেল পারফরম্যান্স উন্নত করার জন্য স্যাম্পলিং কৌশল প্রয়োগ করতে।
- MCP-এর ক্লায়েন্ট-সার্ভার ফ্লোতে স্যাম্পলিং কীভাবে কাজ করে তা বুঝতে।

## MCP-তে স্যাম্পলিং কীভাবে কাজ করে

MCP-তে স্যাম্পলিং ফ্লো নিম্নলিখিত ধাপ অনুসরণ করে:

1. সার্ভার `sampling/createMessage` অনুরোধ ক্লায়েন্টকে পাঠায়
2. ক্লায়েন্ট অনুরোধ পর্যালোচনা করে এবং প্রয়োজনে পরিবর্তন করতে পারে
3. ক্লায়েন্ট LLM থেকে স্যাম্পল করে
4. ক্লায়েন্ট কমপ্লিশন পর্যালোচনা করে
5. ক্লায়েন্ট ফলাফল সার্ভারে ফেরত দেয়

এই মানব-ইন-দ্য-লুপ ডিজাইন নিশ্চিত করে যে ব্যবহারকারীরা নিয়ন্ত্রণ রাখে LLM কী দেখে এবং কী তৈরি করে।

## স্যাম্পলিং প্যারামিটার ওভারভিউ

MCP নিম্নলিখিত স্যাম্পলিং প্যারামিটারগুলো সংজ্ঞায়িত করে যা ক্লায়েন্ট অনুরোধে কনফিগার করা যায়:

| প্যারামিটার | বর্ণনা | সাধারণ রেঞ্জ |
|------------|---------|--------------|
| `temperature` | টোকেন নির্বাচনে র‍্যান্ডমনেস নিয়ন্ত্রণ করে | 0.0 - 1.0 |
| `maxTokens` | সর্বোচ্চ টোকেন সংখ্যা যা তৈরি করা হবে | পূর্ণসংখ্যা মান |
| `stopSequences` | কাস্টম সিকোয়েন্স যা পাওয়া গেলে জেনারেশন বন্ধ করে | স্ট্রিং এর অ্যারে |
| `metadata` | অতিরিক্ত প্রোভাইডার-নির্দিষ্ট প্যারামিটার | JSON অবজেক্ট |

অনেক LLM প্রোভাইডার `metadata` ফিল্ডের মাধ্যমে অতিরিক্ত প্যারামিটার সাপোর্ট করে, যেমন:

| সাধারণ এক্সটেনশন প্যারামিটার | বর্ণনা | সাধারণ রেঞ্জ |
|-------------------------------|---------|--------------|
| `top_p` | নিউক্লিয়াস স্যাম্পলিং - টোকেন সীমাবদ্ধ করে শীর্ষ সামষ্টিক সম্ভাবনায় | 0.0 - 1.0 |
| `top_k` | টোকেন নির্বাচন সীমাবদ্ধ করে শীর্ষ K অপশনে | 1 - 100 |
| `presence_penalty` | টেক্সটে পূর্বে উপস্থিত টোকেনের জন্য পেনাল্টি দেয় | -2.0 - 2.0 |
| `frequency_penalty` | টেক্সটে টোকেনের পুনরাবৃত্তির জন্য পেনাল্টি দেয় | -2.0 - 2.0 |
| `seed` | পুনরুত্পাদনযোগ্য ফলাফলের জন্য নির্দিষ্ট র‍্যান্ডম সিড | পূর্ণসংখ্যা মান |

## উদাহরণ অনুরোধ ফরম্যাট

এখানে MCP-তে ক্লায়েন্ট থেকে স্যাম্পলিং অনুরোধের একটি উদাহরণ:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## রেসপন্স ফরম্যাট

ক্লায়েন্ট একটি কমপ্লিশন ফলাফল ফেরত দেয়:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## মানব-ইন-দ্য-লুপ নিয়ন্ত্রণ

MCP স্যাম্পলিং মানব তত্ত্বাবধানে ডিজাইন করা হয়েছে:

- **প্রম্পটের জন্য**:
  - ক্লায়েন্ট ব্যবহারকারীদের প্রস্তাবিত প্রম্পট দেখানো উচিত
  - ব্যবহারকারীরা প্রম্পট পরিবর্তন বা প্রত্যাখ্যান করতে সক্ষম হওয়া উচিত
  - সিস্টেম প্রম্পট ফিল্টার বা পরিবর্তন করা যেতে পারে
  - প্রসঙ্গ অন্তর্ভুক্তি ক্লায়েন্ট দ্বারা নিয়ন্ত্রিত হয়

- **কমপ্লিশনের জন্য**:
  - ক্লায়েন্ট ব্যবহারকারীদের কমপ্লিশন দেখানো উচিত
  - ব্যবহারকারীরা কমপ্লিশন পরিবর্তন বা প্রত্যাখ্যান করতে সক্ষম হওয়া উচিত
  - ক্লায়েন্ট কমপ্লিশন ফিল্টার বা পরিবর্তন করতে পারে
  - ব্যবহারকারীরা কোন মডেল ব্যবহার হবে তা নিয়ন্ত্রণ করে

এই নীতিমালা মাথায় রেখে, চলুন দেখি কীভাবে বিভিন্ন প্রোগ্রামিং ভাষায় স্যাম্পলিং বাস্তবায়ন করা যায়, বিশেষ করে যেসব প্যারামিটার সাধারণত LLM প্রোভাইডারদের মধ্যে সমর্থিত।

## নিরাপত্তা বিবেচনা

MCP-তে স্যাম্পলিং বাস্তবায়নের সময় নিম্নলিখিত নিরাপত্তা সেরা অনুশীলনগুলো বিবেচনা করুন:

- **সকল মেসেজ কনটেন্ট যাচাই করুন** ক্লায়েন্টে পাঠানোর আগে
- **সংবেদনশীল তথ্য স্যানিটাইজ করুন** প্রম্পট এবং কমপ্লিশন থেকে
- **অপব্যবহার রোধে রেট লিমিট প্রয়োগ করুন**
- **অস্বাভাবিক প্যাটার্নের জন্য স্যাম্পলিং ব্যবহার মনিটর করুন**
- **ডেটা ট্রানজিটে এনক্রিপ্ট করুন** নিরাপদ প্রোটোকল ব্যবহার করে
- **ব্যবহারকারীর ডেটা গোপনীয়তা রক্ষা করুন** প্রাসঙ্গিক নিয়মাবলী অনুযায়ী
- **স্যাম্পলিং অনুরোধের অডিট করুন** সম্মতি ও নিরাপত্তার জন্য
- **খরচ নিয়ন্ত্রণ করুন** উপযুক্ত সীমা দিয়ে
- **স্যাম্পলিং অনুরোধের জন্য টাইমআউট প্রয়োগ করুন**
- **মডেল ত্রুটি সুষ্ঠুভাবে হ্যান্ডেল করুন** উপযুক্ত বিকল্প সহ

স্যাম্পলিং প্যারামিটার ভাষার মডেলের আচরণ সূক্ষ্মভাবে নিয়ন্ত্রণ করতে দেয়, যাতে ডিটারমিনিস্টিক এবং সৃজনশীল আউটপুটের মধ্যে কাঙ্ক্ষিত ভারসাম্য বজায় থাকে।

চলুন দেখি কীভাবে বিভিন্ন প্রোগ্রামিং ভাষায় এই প্যারামিটারগুলো কনফিগার করা যায়।

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

উপরের কোডে আমরা:

- একটি নির্দিষ্ট সার্ভার URL সহ MCP ক্লায়েন্ট তৈরি করেছি।
- `temperature`, `top_p`, এবং `top_k` এর মতো স্যাম্পলিং প্যারামিটার সহ একটি অনুরোধ কনফিগার করেছি।
- অনুরোধ পাঠিয়েছি এবং তৈরি হওয়া টেক্সট প্রিন্ট করেছি।
- ব্যবহার করেছি:
    - `allowedTools` মডেলকে নির্দিষ্ট টুল ব্যবহার করার অনুমতি দেয়। এখানে, আমরা `ideaGenerator` এবং `marketAnalyzer` টুলগুলো অনুমোদন করেছি যাতে সৃজনশীল অ্যাপ আইডিয়া তৈরি করতে সাহায্য করে।
    - `frequencyPenalty` এবং `presencePenalty` আউটপুটে পুনরাবৃত্তি এবং বৈচিত্র্য নিয়ন্ত্রণ করতে।
    - `temperature` আউটপুটের র‍্যান্ডমনেস নিয়ন্ত্রণ করতে, যেখানে উচ্চ মান বেশি সৃজনশীল রেসপন্স দেয়।
    - `top_p` টোকেন নির্বাচন সীমাবদ্ধ করে শীর্ষ সামষ্টিক সম্ভাবনায়, যা তৈরি হওয়া টেক্সটের গুণগত মান উন্নত করে।
    - `top_k` মডেলকে শীর্ষ K সম্ভাব্য টোকেনের মধ্যে সীমাবদ্ধ করে, যা আরও সামঞ্জস্যপূর্ণ রেসপন্স তৈরি করতে সাহায্য করে।
    - `frequencyPenalty` এবং `presencePenalty` পুনরাবৃত্তি কমাতে এবং বৈচিত্র্য উৎসাহিত করতে ব্যবহৃত হয়েছে।

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

উপরের কোডে আমরা:

- একটি সার্ভার URL এবং API কী সহ MCP ক্লায়েন্ট ইনিশিয়ালাইজ করেছি।
- দুটি সেট স্যাম্পলিং প্যারামিটার কনফিগার করেছি: একটি সৃজনশীল কাজের জন্য এবং অন্যটি তথ্যভিত্তিক কাজের জন্য।
- এই কনফিগারেশন সহ অনুরোধ পাঠিয়েছি, মডেলকে প্রতিটি কাজের জন্য নির্দিষ্ট টুল ব্যবহার করার অনুমতি দিয়ে।
- তৈরি হওয়া রেসপন্স প্রিন্ট করেছি যাতে বিভিন্ন স্যাম্পলিং প্যারামিটারের প্রভাব প্রদর্শিত হয়।
- ব্যবহার করেছি `allowedTools` মডেলকে নির্দিষ্ট টুল ব্যবহার করার অনুমতি দিতে। এখানে, সৃজনশীল কাজের জন্য `ideaGenerator` এবং `environmentalImpactTool` অনুমোদিত, এবং তথ্যভিত্তিক কাজের জন্য `factChecker` এবং `dataAnalysisTool` অনুমোদিত।
- `temperature` আউটপুটের র‍্যান্ডমনেস নিয়ন্ত্রণ করতে, যেখানে উচ্চ মান বেশি সৃজনশীল রেসপন্স দেয়।
- `top_p` টোকেন নির্বাচন সীমাবদ্ধ করে শীর্ষ সামষ্টিক সম্ভাবনায়, যা তৈরি হওয়া টেক্সটের গুণগত মান উন্নত করে।
- `frequencyPenalty` এবং `presencePenalty` পুনরাবৃত্তি কমাতে এবং বৈচিত্র্য উৎসাহিত করতে ব্যবহৃত হয়েছে।
- `top_k` মডেলকে শীর্ষ K সম্ভাব্য টোকেনের মধ্যে সীমাবদ্ধ করে, যা আরও সামঞ্জস্যপূর্ণ রেসপন্স তৈরি করতে সাহায্য করে।

---

## ডিটারমিনিস্টিক স্যাম্পলিং

যেসব অ্যাপ্লিকেশন ধারাবাহিক আউটপুট প্রয়োজন, সেখানে ডিটারমিনিস্টিক স্যাম্পলিং পুনরুত্পাদনযোগ্য ফলাফল নিশ্চিত করে। এটি করে একটি নির্দিষ্ট র‍্যান্ডম সিড ব্যবহার করে এবং `temperature` শূন্যে সেট করে।

নিম্নলিখিত উদাহরণে বিভিন্ন প্রোগ্রামিং ভাষায় ডিটারমিনিস্টিক স্যাম্পলিং প্রদর্শন করা হয়েছে।

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

উপরের কোডে আমরা:

- একটি নির্দিষ্ট সার্ভার URL সহ MCP ক্লায়েন্ট তৈরি করেছি।
- একই প্রম্পট, নির্দিষ্ট সিড এবং শূন্য `temperature` সহ দুটি অনুরোধ কনফিগার করেছি।
- উভয় অনুরোধ পাঠিয়েছি এবং তৈরি হওয়া টেক্সট প্রিন্ট করেছি।
- দেখিয়েছি যে রেসপন্সগুলো একই কারণ স্যাম্পলিং কনফিগারেশন ডিটারমিনিস্টিক (একই সিড এবং `temperature`)।
- `setSeed` ব্যবহার করে একটি নির্দিষ্ট র‍্যান্ডম সিড নির্ধারণ করেছি, যা নিশ্চিত করে মডেল একই ইনপুটের জন্য প্রতিবার একই আউটপুট তৈরি করে।
- `temperature` শূন্যে সেট করেছি যাতে সর্বোচ্চ ডিটারমিনিজম নিশ্চিত হয়, অর্থাৎ মডেল সর্বদা সবচেয়ে সম্ভাব্য পরবর্তী টোকেন নির্বাচন করবে, র‍্যান্ডমনেস ছাড়া।

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

উপরের কোডে আমরা:

- একটি সার্ভার URL সহ MCP ক্লায়েন্ট ইনিশিয়ালাইজ করেছি।
- একই প্রম্পট, নির্দিষ্ট সিড এবং শূন্য `temperature` সহ দুটি অনুরোধ কনফিগার করেছি।
- উভয় অনুরোধ পাঠিয়েছি এবং তৈরি হওয়া টেক্সট প্রিন্ট করেছি।
- দেখিয়েছি যে রেসপন্সগুলো একই কারণ স্যাম্পলিং কনফিগারেশন ডিটারমিনিস্টিক (একই সিড এবং `temperature`)।
- `seed` ব্যবহার করে একটি নির্দিষ্ট র‍্যান্ডম সিড নির্ধারণ করেছি, যা নিশ্চিত করে মডেল একই ইনপুটের জন্য প্রতিবার একই আউটপুট তৈরি করে।
- `temperature` শূন্যে সেট করেছি যাতে সর্বোচ্চ ডিটারমিনিজম নিশ্চিত হয়।
- তৃতীয় অনুরোধের জন্য ভিন্ন সিড ব্যবহার করেছি, যা দেখায় যে সিড পরিবর্তন করলে একই প্রম্পট এবং `temperature` থাকলেও আউটপুট ভিন্ন হয়।

---

## ডায়নামিক স্যাম্পলিং কনফিগারেশন

বুদ্ধিমান স্যাম্পলিং প্রতিটি অনুরোধের প্রসঙ্গ এবং প্রয়োজন অনুযায়ী প্যারামিটার সামঞ্জস্য করে। অর্থাৎ, কাজের ধরন, ব্যবহারকারীর পছন্দ বা পূর্বের পারফরম্যান্সের ভিত্তিতে `temperature`, `top_p` এবং পেনাল্টি গুলো ডায়নামিক্যালি পরিবর্তন করা হয়।

নিম্নলিখিত উদাহরণে বিভিন্ন প্রোগ্রামিং ভাষায় ডায়নামিক স্যাম্পলিং বাস্তবায়ন দেখানো হয়েছে।

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

উপরের কোডে আমরা:

- একটি `DynamicSamplingService` ক্লাস তৈরি করেছি যা অভিযোজিত স্যাম্পলিং পরিচালনা করে।
- বিভিন্ন কাজের ধরনের জন্য (সৃজনশীল, তথ্যভিত্তিক, কোড, বিশ্লেষণাত্মক) স্যাম্পলিং প্রিসেট সংজ্ঞায়িত করেছি।
- কাজের ধরন অনুযায়ী একটি বেস স্যাম্পলিং প্রিসেট নির্বাচন করেছি।
- ব্যবহারকারীর পছন্দ যেমন সৃজনশীলতা এবং বৈচিত্র্যের ভিত্তিতে স্যাম্পলিং প্যারামিটার সামঞ্জস্য করেছি।
- কনফিগার করা স্যাম্পলিং প্যারামিটার সহ অনুরোধ পাঠিয়েছি।
- তৈরি হওয়া টেক্সট এবং প্রয়োগকৃত স্যাম্পলিং প্যারামিটার ও কাজের ধরন সহ ফলাফল ফেরত দিয়েছি।
- `temperature` ব্যবহার করেছি আউটপুটের র‍্যান্ডমনেস নিয়ন্ত্রণে, যেখানে উচ্চ মান বেশি সৃজনশীল রেসপন্স দেয়।
- `top_p` ব্যবহার করেছি টোকেন নির্বাচন সীমাবদ্ধ করতে শীর্ষ সামষ্টিক সম্ভাবনায়, যা তৈরি হওয়া টেক্সটের গুণগত মান উন্নত করে।
- `frequency_penalty` ব্যবহার করেছি পুনরাবৃত্তি কমাতে এবং বৈচিত্র্য উৎসাহিত করতে।
- `user_preferences` ব্যবহার করেছি ব্যবহারকারীর সংজ্ঞায়িত সৃজনশীলতা এবং বৈচিত্র্য স্তরের ভিত্তিতে স্যাম্পলিং প্যারামিটার কাস্টমাইজেশনের জন্য।
- `task_type` ব্যবহার করেছি অনুরোধের জন্য উপযুক্ত স্যাম্পলিং কৌশল নির্ধারণে, কাজের প্রকৃতির উপর ভিত্তি করে আরও উপযোগী রেসপন্সের জন্য।
- `send_request` পদ্ধতি ব্যবহার করেছি কনফিগার করা স্যাম্পলিং প্যারামিটার সহ প্রম্পট পাঠাতে, নিশ্চিত করতে যে মডেল নির্দিষ্ট চাহিদা অনুযায়ী টেক্সট তৈরি করে।
- `generated_text` ব্যবহার করেছি মডেলের রেসপন্স পেতে, যা পরে স্যাম্পলিং প্যারামিটার এবং কাজের ধরন সহ ফেরত দেওয়া হয়।
- `min` এবং `max` ফাংশন ব্যবহার করেছি ব্যবহারকারীর পছন্দ বৈধ সীমার মধ্যে সীমাবদ্ধ রাখতে, অবৈধ স্যাম্পলিং কনফিগারেশন প্রতিরোধে।

# [JavaScript Dynamic](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Dynamic sampling configuration based on user context
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Define base sampling profiles
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Track historical performance
    this.performanceHistory = [];
  }
  
  // Detect task type from prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simple heuristic detection - could be enhanced with ML classification
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // Default to conversational if no clear type is detected
    return 'conversational';
  }
  
  // Calculate sampling parameters based on context and user preferences
  getSamplingParameters(prompt, context = {}) {
    // Detect the type of task
    const taskType = this.detectTaskType(prompt, context);
    
    // Get base profile
    let params = {...this.samplingProfiles[taskType]};
    
    // Adjust based on user preferences
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Scale from 1-10 to appropriate temperature range
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Higher precision means lower topP (more focused selection)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Higher consistency means lower penalties
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Apply learned adjustments from performance history
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simple adaptive logic - could be enhanced with more sophisticated algorithms
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Only consider recent history
    
    if (relevantHistory.length > 0) {
      // Calculate average performance scores
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // If performance is below threshold, adjust parameters
      if (avgScore < 0.7) {
        // Slight adjustment toward safer values
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Record performance for future adjustments
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 rating of response quality
    });
    
    // Limit history size
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Get optimized sampling parameters
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Send request with optimized parameters
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // If user provides feedback, record it for future optimization
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// Example usage
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creative task with custom user preferences
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // High creativity (1-10)
          consistency: 3  // Low consistency (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Code generation task
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Low creativity
          precision: 8,   // High precision
          consistency: 9  // High consistency
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

উপরের কোডে আমরা:

- একটি `AdaptiveSamplingManager` ক্লাস তৈরি করেছি যা কাজের ধরন এবং ব্যবহারকারীর পছন্দ অনুযায়ী ডায়নামিক স্যাম্পলিং পরিচালনা করে।
- বিভিন্ন কাজের ধরনের জন্য (সৃজনশীল, তথ্যভিত্তিক, কোড, কথোপকথন) স্যাম্পলিং প্রোফাইল সংজ্ঞায়িত করেছি।
- প্রম্পট থেকে কাজের ধরন সনাক্ত করার জন্য সহজ হিউরিস্টিক্স প্রয়োগ করেছি।
- সনাক্তকৃত কাজের ধরন এবং ব্যবহারকারীর পছন্দ অনুযায়ী স্যাম্পলিং প্যারামিটার হিসাব করেছি।
- পূর্বের পারফরম্যান্সের ভিত্তিতে শেখা সামঞ্জস্য প্রয়োগ করে স্যাম্পলিং প্যারামিটার অপ্টিমাইজ করেছি।
- ভবিষ্যতের সামঞ্জস্যের জন্য পারফরম্যান্স রেকর্ড করেছি, যাতে সিস্টেম অতীতের ইন্টারঅ্যাকশন থেকে শিখতে পারে।
- ডায়নামিক কনফিগার করা স্যাম্পলিং প্যারামিটার সহ অনুরোধ পাঠিয়েছি এবং তৈরি হওয়া টেক্সট, প্রয়োগকৃত প্যারামিটার এবং সনাক্তকৃত কাজের ধরন ফেরত দিয়েছি।
- ব্যবহার করেছি:
    - `userPreferences` ব্যবহারকারীর সংজ্ঞায়িত সৃজনশীলতা, নির্ভুলতা এবং ধারাবাহিকতার স্তরের ভিত্তিতে স্যাম্পলিং প্যারামিটার কাস্টমাইজেশনের জন্য।
    - `detectTaskType` প্রম্পট থেকে কাজের প্রকৃতি নির্ধারণে, যাতে বিভিন্ন ধরনের অনুরোধের জন্য উপযুক্ত স্যাম্পলিং কৌশল প্রয়োগ করা যায়।
    - `recordPerformance` তৈরি

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।