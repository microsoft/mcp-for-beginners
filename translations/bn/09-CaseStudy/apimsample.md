# কেস স্টাডি: API Management-এ REST API-কে MCP সার্ভার হিসেবে উন্মুক্ত করা

Azure API Management একটি সেবা যা আপনার API এন্ডপয়েন্টগুলোর উপরে একটি গেটওয়ে প্রদান করে। এটি কাজ করে এভাবে যে Azure API Management আপনার API-গুলোর সামনে একটি প্রক্সি হিসেবে কাজ করে এবং আগত অনুরোধগুলোর সাথে কী করা হবে তা নির্ধারণ করে।

এটি ব্যবহার করে আপনি অনেকগুলো বৈশিষ্ট্য যোগ করতে পারেন, যেমন:

- **নিরাপত্তা**, আপনি API কী, JWT থেকে শুরু করে ম্যানেজড আইডেন্টিটি পর্যন্ত সবকিছু ব্যবহার করতে পারেন।
- **রেট লিমিটিং**, একটি চমৎকার বৈশিষ্ট্য হলো নির্ধারণ করতে পারা যে একটি নির্দিষ্ট সময়ে কতগুলো কল অনুমোদিত হবে। এটি নিশ্চিত করে যে সকল ব্যবহারকারী একটি ভালো অভিজ্ঞতা পান এবং আপনার সেবা অতিরিক্ত অনুরোধে অভিভূত হয় না।
- **স্কেলিং এবং লোড ব্যালেন্সিং**, আপনি একাধিক এন্ডপয়েন্ট সেটআপ করতে পারেন লোড ব্যালেন্স করার জন্য এবং কীভাবে "লোড ব্যালেন্স" করবেন তা নির্ধারণ করতে পারেন।
- **AI বৈশিষ্ট্য যেমন সেমান্টিক ক্যাশিং**, টোকেন লিমিট এবং টোকেন মনিটরিং ইত্যাদি। এই বৈশিষ্ট্যগুলো প্রতিক্রিয়াশীলতা উন্নত করে এবং টোকেন ব্যবহারের উপর নজর রাখতে সাহায্য করে। [এখানে আরও পড়ুন](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## কেন MCP + Azure API Management?

মডেল কনটেক্সট প্রোটোকল দ্রুত এজেন্টিক AI অ্যাপ্লিকেশন এবং একটি সঙ্গতিপূর্ণ উপায়ে টুল এবং ডেটা উন্মুক্ত করার জন্য একটি মানদণ্ড হয়ে উঠছে। যখন API-গুলো "ম্যানেজ" করতে হয়, তখন Azure API Management একটি স্বাভাবিক পছন্দ। MCP সার্ভার প্রায়শই অন্যান্য API-এর সাথে ইন্টিগ্রেট হয় একটি টুলের জন্য অনুরোধ সমাধান করতে। তাই Azure API Management এবং MCP একত্রিত করা একটি যৌক্তিক সিদ্ধান্ত।

## ওভারভিউ

এই নির্দিষ্ট ব্যবহারের ক্ষেত্রে আমরা শিখব কীভাবে API এন্ডপয়েন্টগুলোকে MCP সার্ভার হিসেবে উন্মুক্ত করা যায়। এটি করে আমরা সহজেই এই এন্ডপয়েন্টগুলোকে একটি এজেন্টিক অ্যাপের অংশ করতে পারি এবং একই সাথে Azure API Management-এর বৈশিষ্ট্যগুলো ব্যবহার করতে পারি।

## মূল বৈশিষ্ট্য

- আপনি কোন এন্ডপয়েন্ট মেথডগুলো টুল হিসেবে উন্মুক্ত করবেন তা নির্বাচন করতে পারেন।
- আপনি যে অতিরিক্ত বৈশিষ্ট্যগুলো পাবেন তা নির্ভর করবে আপনার API-এর জন্য পলিসি সেকশনে কী কনফিগার করেছেন তার উপর। এখানে আমরা দেখাব কীভাবে রেট লিমিটিং যোগ করা যায়।

## প্রাক-ধাপ: একটি API ইম্পোর্ট করা

যদি আপনার Azure API Management-এ ইতোমধ্যে একটি API থাকে, তাহলে আপনি এই ধাপটি এড়িয়ে যেতে পারেন। যদি না থাকে, তাহলে এই লিঙ্কটি দেখুন: [Azure API Management-এ একটি API ইম্পোর্ট এবং পাবলিশ করা](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API-কে MCP সার্ভার হিসেবে উন্মুক্ত করা

API এন্ডপয়েন্টগুলো উন্মুক্ত করতে, নিচের ধাপগুলো অনুসরণ করুন:

1. Azure পোর্টালে যান এবং এই ঠিকানায় যান <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>। 
   আপনার API Management ইনস্ট্যান্সে নেভিগেট করুন।

1. বাম মেনুতে, **APIs > MCP Servers > + Create new MCP Server** নির্বাচন করুন।

1. API-তে, একটি REST API নির্বাচন করুন যা MCP সার্ভার হিসেবে উন্মুক্ত হবে।

1. এক বা একাধিক API অপারেশন নির্বাচন করুন যা টুল হিসেবে উন্মুক্ত হবে। আপনি সব অপারেশন বা নির্দিষ্ট অপারেশনগুলো নির্বাচন করতে পারেন।

    ![উন্মুক্ত করার জন্য মেথড নির্বাচন করুন](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** নির্বাচন করুন।

1. মেনু অপশনে **APIs** এবং **MCP Servers**-এ নেভিগেট করুন, আপনি নিচের মতো দেখতে পাবেন:

    ![মূল প্যানেলে MCP সার্ভার দেখুন](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP সার্ভার তৈরি হয়েছে এবং API অপারেশনগুলো টুল হিসেবে উন্মুক্ত হয়েছে। MCP সার্ভার MCP Servers প্যানেলে তালিকাভুক্ত। URL কলামটি MCP সার্ভারের এন্ডপয়েন্ট দেখায় যা আপনি টেস্টিং বা ক্লায়েন্ট অ্যাপ্লিকেশনের মধ্যে কল করতে পারেন।

## ঐচ্ছিক: পলিসি কনফিগার করা

Azure API Management-এর একটি মূল ধারণা হলো পলিসি, যেখানে আপনি আপনার এন্ডপয়েন্টগুলোর জন্য বিভিন্ন নিয়ম সেটআপ করতে পারেন, যেমন রেট লিমিটিং বা সেমান্টিক ক্যাশিং। এই পলিসিগুলো XML-এ লেখা হয়।

এখানে দেখানো হলো কীভাবে MCP সার্ভারের জন্য একটি রেট লিমিট পলিসি সেটআপ করবেন:

1. পোর্টালে, **APIs**-এর অধীনে **MCP Servers** নির্বাচন করুন।

1. আপনি যে MCP সার্ভার তৈরি করেছেন তা নির্বাচন করুন।

1. বাম মেনুতে, MCP-এর অধীনে **Policies** নির্বাচন করুন।

1. পলিসি এডিটরে, MCP সার্ভারের টুলগুলোর জন্য প্রয়োগ করতে চান এমন পলিসিগুলো যোগ করুন বা সম্পাদনা করুন। পলিসিগুলো XML ফরম্যাটে সংজ্ঞায়িত। উদাহরণস্বরূপ, আপনি একটি পলিসি যোগ করতে পারেন যা MCP সার্ভারের টুলগুলোর কল সীমিত করে (এই উদাহরণে, প্রতি ক্লায়েন্ট IP ঠিকানার জন্য প্রতি ৩০ সেকেন্ডে ৫টি কল)। নিচে XML দেওয়া হলো যা রেট লিমিট করবে:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    পলিসি এডিটরের একটি চিত্র এখানে:

    ![পলিসি এডিটার](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## চেষ্টা করে দেখুন

চলুন নিশ্চিত করি যে আমাদের MCP সার্ভার সঠিকভাবে কাজ করছে।

এটির জন্য, আমরা Visual Studio Code এবং GitHub Copilot এবং এর এজেন্ট মোড ব্যবহার করব। আমরা MCP সার্ভারটিকে একটি *mcp.json* ফাইলে যোগ করব। এটি করে, Visual Studio Code একটি ক্লায়েন্ট হিসেবে কাজ করবে এজেন্টিক ক্ষমতা নিয়ে এবং শেষ ব্যবহারকারীরা একটি প্রম্পট টাইপ করে সার্ভারের সাথে ইন্টারঅ্যাক্ট করতে পারবেন।

এখানে দেখানো হলো কীভাবে Visual Studio Code-এ MCP সার্ভার যোগ করবেন:

1. **Command Palette** থেকে MCP: **Add Server কমান্ড** ব্যবহার করুন।

1. যখন প্রম্পট করা হবে, সার্ভার টাইপ নির্বাচন করুন: **HTTP (HTTP বা Server Sent Events)**।

1. API Management-এ MCP সার্ভারের URL প্রবেশ করান। উদাহরণ: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE এন্ডপয়েন্টের জন্য) অথবা **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP এন্ডপয়েন্টের জন্য), লক্ষ্য করুন যে ট্রান্সপোর্টের মধ্যে পার্থক্য হলো `/sse` বা `/mcp`।

1. আপনার পছন্দমতো একটি সার্ভার ID প্রবেশ করান। এটি একটি গুরুত্বপূর্ণ মান নয় তবে এটি আপনাকে মনে রাখতে সাহায্য করবে যে এটি কোন সার্ভার ইনস্ট্যান্স।

1. কনফিগারেশনটি আপনার ওয়ার্কস্পেস সেটিংসে বা ব্যবহারকারী সেটিংসে সংরক্ষণ করবেন কিনা তা নির্বাচন করুন।

  - **ওয়ার্কস্পেস সেটিংস** - সার্ভার কনফিগারেশনটি একটি .vscode/mcp.json ফাইলে সংরক্ষণ করা হয় যা কেবলমাত্র বর্তমান ওয়ার্কস্পেসে উপলব্ধ।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    অথবা যদি আপনি স্ট্রিমিং HTTP ট্রান্সপোর্ট হিসেবে নির্বাচন করেন তবে এটি সামান্য ভিন্ন হবে:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ব্যবহারকারী সেটিংস** - সার্ভার কনফিগারেশনটি আপনার গ্লোবাল *settings.json* ফাইলে যোগ করা হয় এবং এটি সব ওয়ার্কস্পেসে উপলব্ধ। কনফিগারেশনটি নিম্নরূপ দেখাবে:

    ![ব্যবহারকারী সেটিং](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. আপনাকে আরও একটি কনফিগারেশন যোগ করতে হবে, একটি হেডার যা নিশ্চিত করবে এটি Azure API Management-এর সাথে সঠিকভাবে প্রমাণীকৃত হচ্ছে। এটি **Ocp-Apim-Subscription-Key** নামক একটি হেডার ব্যবহার করে।

    - এখানে দেখানো হলো কীভাবে এটি সেটিংসে যোগ করবেন:

    ![প্রমাণীকরণের জন্য হেডার যোগ করা](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), এটি একটি প্রম্পট দেখাবে যেখানে আপনাকে API কী মান প্রবেশ করতে বলা হবে যা আপনি Azure পোর্টালে আপনার Azure API Management ইনস্ট্যান্সের জন্য খুঁজে পাবেন।

   - এটি *mcp.json*-এ যোগ করতে চাইলে, আপনি এটি এভাবে যোগ করতে পারেন:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### এজেন্ট মোড ব্যবহার করুন

এখন আমরা হয় সেটিংসে বা *.vscode/mcp.json*-এ সবকিছু সেটআপ করেছি। চলুন এটি চেষ্টা করে দেখি।

আপনার একটি টুলস আইকন দেখতে পাওয়া উচিত, যেখানে আপনার সার্ভার থেকে উন্মুক্ত টুলগুলো তালিকাভুক্ত থাকবে:

![সার্ভার থেকে টুলস](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. টুলস আইকনে ক্লিক করুন এবং আপনি নিচের মতো একটি টুলস তালিকা দেখতে পাবেন:

    ![টুলস](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. চ্যাটে একটি প্রম্পট প্রবেশ করান টুলটি চালানোর জন্য। উদাহরণস্বরূপ, যদি আপনি একটি টুল নির্বাচন করেন যা একটি অর্ডারের তথ্য পেতে সাহায্য করে, আপনি এজেন্টকে অর্ডার সম্পর্কে জিজ্ঞাসা করতে পারেন। এখানে একটি উদাহরণ প্রম্পট:

    ```text
    get information from order 2
    ```

    এখন আপনি একটি টুলস আইকন দেখতে পাবেন যা আপনাকে টুল চালানোর জন্য এগিয়ে যেতে বলবে। টুল চালানো চালিয়ে যেতে নির্বাচন করুন, আপনি এখন নিচের মতো একটি আউটপুট দেখতে পাবেন:

    ![প্রম্পট থেকে ফলাফল](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **উপরেরটি আপনি কী টুল সেটআপ করেছেন তার উপর নির্ভর করে, তবে ধারণাটি হলো আপনি উপরের মতো একটি টেক্সট আউটপুট পাবেন।**

## রেফারেন্স

এখানে আরও জানার উপায়:

- [Azure API Management এবং MCP-এর উপর টিউটোরিয়াল](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [পাইথন নমুনা: Azure API Management ব্যবহার করে রিমোট MCP সার্ভার সুরক্ষিত করা (পরীক্ষামূলক)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP ক্লায়েন্ট অথরাইজেশন ল্যাব](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Visual Studio Code-এর জন্য Azure API Management এক্সটেনশন ব্যবহার করে API ইম্পোর্ট এবং ম্যানেজ করা](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center-এ রিমোট MCP সার্ভার রেজিস্টার এবং আবিষ্কার করা](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) একটি চমৎকার রিপোজিটরি যা Azure API Management-এর সাথে অনেক AI ক্ষমতা দেখায়
- [AI Gateway ওয়ার্কশপ](https://azure-samples.github.io/AI-Gateway/) Azure পোর্টাল ব্যবহার করে ওয়ার্কশপ অন্তর্ভুক্ত, যা AI ক্ষমতা মূল্যায়ন শুরু করার একটি চমৎকার উপায়।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।