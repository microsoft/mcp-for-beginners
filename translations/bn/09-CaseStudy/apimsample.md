# কেস স্টাডি: API ম্যানেজমেন্টে REST API MCP সার্ভার হিসেবে প্রকাশ করুন

Azure API Management একটি সেবা যা আপনার API এন্ডপয়েন্টগুলির শীর্ষে একটি গেটওয়ে প্রদান করে। এটি কীভাবে কাজ করে তা হলো Azure API Management আপনার API এর সামনে একটি প্রক্সি হিসেবে কাজ করে এবং ইনকামিং রিকোয়েস্ট নিয়ে কী করতে হবে তা নির্ধারণ করতে পারে।

এটি ব্যবহার করে, আপনি অনেক ফিচার যুক্ত করেন যেমন:

- **সুরক্ষা**, আপনি API কী, JWT থেকে শুরু করে managed identity পর্যন্ত সবকিছু ব্যবহার করতে পারেন।
- **রেট লিমিটিং**, একটি চমৎকার ফিচার হল নির্ধারণ করতে পারা কতগুলি কল একটি নির্দিষ্ট সময়ে পার হতে পারবে। এটি নিশ্চিত করে যে সব ব্যবহারকারীর একটি চমৎকার অভিজ্ঞতা হয় এবং আপনার সেবা রিকোয়েস্টে ভরাট হয় না।
- **স্কেলিং এবং লোড ব্যালান্সিং**। আপনি বেশ কিছু এন্ডপয়েন্ট সেটআপ করতে পারেন ভার সমান করার জন্য এবং “লোড ব্যালান্সিং” কীভাবে করবেন তাও নির্ধারণ করতে পারেন।
- **AI ফিচার যেমন সেম্যান্টিক ক্যাশিং**, টোকেন সীমা এবং টোকেন মনিটরিং ইত্যাদি। এগুলো চমৎকার ফিচার যা প্রতিক্রিয়া ক্ষমতা বৃদ্ধি করে এবং আপনার টোকেন খরচের উপর নিয়ন্ত্রণ রাখতে সাহায্য করে। [অধিক পড়ুন এখানে](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)। 

## কেন MCP + Azure API Management?

Model Context Protocol দ্রুত এজেন্টিক AI অ্যাপের জন্য একটি স্ট্যান্ডার্ড হয়ে উঠছে এবং কীভাবে consistent পদ্ধতিতে টুল ও ডেটা প্রকাশ করবেন তা নির্দেশ দেয়। Azure API Management হলো প্রাকৃতিক পছন্দ যখন আপনাকে API গুলো “ম্যানেজ” করতে হয়। MCP সার্ভারগুলো প্রায়ই অন্যান্য API এর সাথে ইন্টিগ্রেট করে টুলের জন্য রিকোয়েস্ট রেজলভ করে, তাই Azure API Management এবং MCP একসাথে ব্যবহার করা অনেক অর্থবহ।

## ওভারভিউ

এই নির্দিষ্ট ব্যবহারে আমরা শিখব কীভাবে API এন্ডপয়েন্টগুলো MCP সার্ভার হিসেবে প্রকাশ করবেন। এর মাধ্যমে, আমরা সহজেই এই এন্ডপয়েন্টগুলোকে এজেন্টিক অ্যাপের অংশ করে তুলতে পারব এবং Azure API Management এর ফিচারও উপভোগ করতে পারব।

## প্রধান ফিচারগুলি

- আপনি যেসব এন্ডপয়েন্ট মেথড প্রকাশ করতে চান সেগুলো নির্বাচন করবেন।
- অতিরিক্ত ফিচার আপনি পাবেন যা নির্ভর করবে আপনি কোন পলিসি অংশে আপনার API জন্য কী কনফিগার করেছেন তার ওপর। কিন্তু এখানে আমরা দেখাব কীভাবে আপনি রেট লিমিটিং অ্যাড করতে পারবেন।

## পূর্ববর্তী ধাপ: একটি API ইমপোর্ট করুন

যদি আপনার Azure API Management এ আগেই একটি API থাকে, তাহলে দুর্দান্ত, আপনি এই ধাপটি বাদ দিতে পারেন। যদি না থাকে, তাহলে এই লিংক দেখুন, [Azure API Management এ API ইমপোর্ট ও প্রকাশ করা](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API কে MCP সার্ভার হিসেবে প্রকাশ করুন

API এন্ডপয়েন্টগুলো প্রকাশ করতে, নিম্নলিখিত ধাপগুলো অনুসরণ করুন:

1. Azure Portal এ যান এবং এই ঠিকানায় যান <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
আপনার API Management ইনস্ট্যান্সে যান।

1. বাম মেনু থেকে APIs > MCP Servers > + Create new MCP Server নির্বাচন করুন।

1. API থেকে একটি REST API নির্বাচন করুন যাকে MCP সার্ভার হিসেবে প্রকাশ করবেন।

1. একটি বা একাধিক API অপারেশন নির্বাচন করুন যেগুলো টুল হিসেবে প্রকাশ করবেন। আপনি সব অপারেশন বা নির্দিষ্ট অপারেশনই নির্বাচন করতে পারেন।

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** নির্বাচন করুন।

1. মেনু অপশন **APIs** এবং **MCP Servers** এ যান, আপনি নিম্নলিখিতটি দেখতে পাবেন:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP সার্ভার তৈরি হয়েছে এবং API অপারেশনগুলো টুল হিসেবে প্রকাশিত হয়েছে। MCP সার্ভারটি MCP Servers পাতায় তালিকাভুক্ত থাকবে। URL কলাম MCP সার্ভারের এন্ডপয়েন্ট দেখায় যা আপনি টেস্টিং বা ক্লায়েন্ট অ্যাপ্লিকেশন থেকে কল করতে পারেন।

## ঐচ্ছিক: পলিসি কনফিগার করুন

Azure API Management এর মূল ধারণা হল পলিসি, যেখানে আপনি আপনার এন্ডপয়েন্টগুলোর জন্য বিভিন্ন নিয়ম সেটআপ করেন যেমন রেট লিমিটিং বা সেম্যান্টিক ক্যাশিং। এগুলো XML এ লেখা হয়।

নিচে দেখানো হলো কিভাবে MCP সার্ভারের জন্য রেট লিমিটিং পলিসি সেটআপ করবেন:

1. পোর্টালে APIs এর অধীনে **MCP Servers** নির্বাচন করুন।

1. আপনি যেই MCP সার্ভার তৈরি করেছেন সেটা নির্বাচন করুন।

1. বাম মেনু থেকে MCP এর অধীনে **Policies** নির্বাচন করুন।

1. পলিসি এডিটরে MCP সার্ভারের টুলগুলোর জন্য আপনি যেই পলিসি প্রয়োগ করতে চান তা যোগ বা সম্পাদনা করুন। পলিসিগুলো XML ফরম্যাটে নির্ধারণ করা হয়। উদাহরণস্বরূপ, আপনি একটি পলিসি যোগ করতে পারেন যা MCP সার্ভারের টুলগুলোতে কলের সংখ্যা সীমিত করবে (এখানে, প্রতি ক্লায়েন্ট IP ঠিকানায় প্রতি ৩০ সেকেন্ডে ৫ কল)। নিচে XML দেয়া হলো যা রেট লিমিটিং করবে:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    এখানে পলিসি এডিটরের একটি ছবি:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## এটি পরীক্ষা করুন

চলুন নিশ্চিত করি যে আমাদের MCP সার্ভার প্রত্যাশামতো কাজ করছে।

> [!NOTE]
> Azure API Management বর্তমানে এই সার্ভারটি Streamable
> HTTP `/mcp` এন্ডপয়েন্টের মাধ্যমে প্রকাশ করে। পুরনো HTTP+SSE `/sse` পরিবহন অবলুপ্ত এবং
> শুধুমাত্র লিগ্যাসি ক্লায়েন্টের সাথে ব্যবহার করা উচিত।

এ জন্য, আমরা Visual Studio Code এবং GitHub Copilot এর Agent মোড ব্যবহার করব। আমরা একটি *mcp.json* ফাইলে MCP সার্ভার যোগ করব। এর ফলে Visual Studio Code একটি এজেন্টিক ক্ষমতাসম্পন্ন ক্লায়েন্ট হিসেবে কাজ করবে এবং শেষ ব্যবহারকারীরা একটি প্রম্পট টাইপ করে সেই সার্ভারের সাথে ইন্টারঅ্যাক্ট করতে পারবেন।

চলুন দেখি, Visual Studio Code এ MCP সার্ভার কীভাবে যোগ করবেন:

1. Command Palette থেকে MCP: **Add Server command** ব্যবহার করুন।

1. প্রম্পট এ, সার্ভার টাইপ নির্বাচন করুন: **HTTP (HTTP or Server Sent Events)**।

1. API Management এ MCP সার্ভারের জন্য প্রদর্শিত Streamable HTTP URL প্রবেশ করান।
    উদাহরণস্বরূপ:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`।

1. আপনার পছন্দমতো একটি সার্ভার আইডি প্রবেশ করান। এটি গুরুত্বপূর্ণ নয় কিন্তু এটি আপনাকে মনে রাখতে সাহায্য করবে যে এই সার্ভার ইনস্ট্যান্সটি কী।

1. সংরক্ষণ করার জন্য নির্বাচন করুন আপনার কাজের স্থানের সেটিংসে অথবা ব্যবহারকারীর সেটিংসে।

  - **ওয়ার্কস্পেস সেটিংস** - সার্ভার কনফিগারেশন শুধুমাত্র বর্তমান ওয়ার্কস্পেসের .vscode/mcp.json ফাইলে সংরক্ষিত হবে।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ব্যবহারকারী সেটিংস** - সার্ভার কনফিগারেশন আপনার গ্লোবাল *settings.json* ফাইলে যোগ হবে এবং সব ওয়ার্কস্পেসে উপলব্ধ থাকবে। কনফিগারেশন এর মত দেখাবে:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. এছাড়াও আপনাকে একটি হেডার যোগ করতে হবে যাতে এটি সঠিকভাবে Azure API Management এর দিকে প্রমাণীকরণ (authentication) করে। এটি একটি হেডার ব্যবহার করে যার নাম **Ocp-Apim-Subscription-Key**।

    - সেটিংসে এটি কীভাবে যোগ করবেন:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), এর ফলে একটি প্রম্পট প্রদর্শিত হবে যা আপনার API কী মান চাইবে যা আপনি Azure Portal থেকে আপনার Azure API Management ইনস্ট্যান্সের জন্য পেতে পারেন।

   - বিকল্পভাবে *mcp.json* তে যোগ করতে, আপনি এরকমভাবে যোগ করতে পারেন:

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

### Agent মোড ব্যবহার করুন

এখন আমরা সেটিংস বা *.vscode/mcp.json* এ সব কনফিগারেশন সন্নিবেশ করেছি। চলুন পরীক্ষা করি।

সেখানে একটি Tools আইকন থাকা উচিত, যেখানে আপনার সার্ভার থেকে প্রকাশিত টুলগুলো তালিকাভুক্ত থাকবে:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. টুলস আইকনে ক্লিক করুন এবং আপনি এই রকম টুলগুলোর তালিকা দেখতে পাবেন:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. টুলটি চালাতে চ্যাটে একটি প্রম্পট লিখুন। উদাহরণস্বরূপ, আপনি যদি একটি টুল নির্বাচন করে থাকেন যা কোনো অর্ডারের তথ্য দেয়, তাহলে আপনি এজেন্টকে অর্ডারের সম্পর্কে জানতে বলতে পারেন। নিচে একটি উদাহরণ প্রম্পট দেওয়া হলো:

    ```text
    get information from order 2
    ```

    এখন আপনাকে একটি টুলস আইকন দেখানো হবে যা আপনাকে টুল চালাতে অনুমতি চাইবে। চালিয়ে যেতে নির্বাচন করুন, আপনি নিচের মত ফলাফল দেখতে পাবেন:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **উপরের ফলাফল আপনি কেমন টুল সেটআপ করেছেন তার ওপর নির্ভর করবে, তবে ধারণা হলো আপনি উপরের মত একটি টেক্সট রেসপন্স পাবেন**


## রেফারেন্সসমূহ

এখানে আপনি আরো শিখতে পারেন:

- [Azure API Management এবং MCP এর উপর টিউটোরিয়াল](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python স্যাম্পল: Azure API Management ব্যবহার করে রিমোট MCP সার্ভার সিকিউর করা (এক্সপেরিমেন্টাল)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP ক্লায়েন্ট অথরাইজেশন ল্যাব](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code এর জন্য Azure API Management এক্সটেনশন ব্যবহার করে API ইমপোর্ট ও ম্যানেজমেন্ট](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center এ রিমোট MCP সার্ভার নিবন্ধন ও আবিষ্কারকরণ](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) একটি চমৎকার রিপোজিটোরি যা Azure API Management সহ অনেক AI ক্ষমতা প্রদর্শন করে
- [AI Gateway ওয়ার্কশপসমূহ](https://azure-samples.github.io/AI-Gateway/) Azure Portal ব্যবহার করে ওয়ার্কশপ রয়েছে, যা AI ক্ষমতা মূল্যায়নের একটি চমৎকার উপায়।

## পরবর্তী ধাপ কী

- ফিরে যান: [Case Studies Overview](./README.md)
- পরবর্তী: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->