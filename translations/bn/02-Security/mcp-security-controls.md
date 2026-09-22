# MCP সিকিউরিটি কন্ট্রোলস - সেপ্টেম্বর ২০২৬ আপডেট

> **বর্তমান স্ট্যান্ডার্ড:** এই ডকুমেন্টটি প্রতিফলিত করে
> [MCP স্পেসিফিকেশন ২০২৬-০৭-২৮](https://modelcontextprotocol.io/specification/2026-07-28/)
> এবং অফিসিয়াল
> [MCP সিকিউরিটি বেস্ট প্র্যাকটিসেস](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)।

মডেল কনটেক্সট প্রোটোকল (MCP) উল্লেখযোগ্যভাবে পরিপক্ক হয়েছে উন্নত সিকিউরিটি কন্ট্রোল নিয়ে যা ঐতিহ্যগত সফটওয়্যার সিকিউরিটি এবং AI-নির্দিষ্ট হুমকি উভয়ই মোকাবেলা করে। এই ডকুমেন্টটি নিরাপদ MCP ইমপ্লিমেন্টেশনের জন্য ব্যাপক সিকিউরিটি কন্ট্রোল সরবরাহ করে যা OWASP MCP Top 10 ফ্রেমওয়ার্কের সাথে সঙ্গতিপূর্ণ।

## 🏔️ হ্যান্ডস-অন সিকিউরিটি প্রশিক্ষণ

ব্যবহারিক, হাতে-কলমে সিকিউরিটি ইমপ্লিমেন্টেশন অভিজ্ঞতার জন্য, আমরা সুপারিশ করি **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Azure-এ MCP সার্ভার সুরক্ষিত করার জন্য একটি ব্যাপক নির্দেশিত অভিযাত্রা যা "ভালনারেবল → এক্সপ্লয়াইট → ফিক্স → ভ্যালিডেট" পদ্ধতি অনুসরণ করে।

এই ডকুমেন্টের সমস্ত সিকিউরিটি কন্ট্রোল মিলিত হয় **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** এর সাথে, যা OWASP MCP Top 10 ঝুঁকি জন্য রেফারেন্স আর্কিটেকচার এবং Azure-নির্দিষ্ট ইমপ্লিমেন্টেশন নির্দেশিকা প্রদান করে।

## **আবশ্যকীয় সিকিউরিটি চাহিদাসমূহ**

### **MCP স্পেসিফিকেশন থেকে গুরুত্বপূর্ণ নিষেধাজ্ঞা:**

> **নিষিদ্ধ**: MCP সার্ভারগুলি **অবশ্যই গ্রহণ করবে না** কোন টোকেন যা স্পষ্টভাবে MCP সার্ভারের জন্য ইস্যু করা হয়নি
>
> **নিষিদ্ধ**: MCP সার্ভারগুলি **অবশ্যই ব্যবহার করবে না** সেশন ভিত্তিক প্রমাণীকরণ  
>
> **প্রয়োজনীয়**: MCP সার্ভারগুলি যা অথরাইজেশন ইমপ্লিমেন্ট করে **সমস্ত** ইনবাউন্ড অনুরোধ যাচাই করবে
>
> **আবশ্যকীয়**: MCP প্রক্সি সার্ভার যা একটি স্থির তৃতীয়-পক্ষ ক্লায়েন্ট আইডি ব্যবহার করে
> **প্রত্যেক MCP ক্লায়েন্টের সম্মতি নিতে হবে** অথরাইজেশন ফরওয়ার্ড করার আগে

---

## ১. **প্রমাণীকরণ ও অনুমোদন নিয়ন্ত্রণ**

### **বাহ্যিক পরিচয় প্রদানকারী ইন্টিগ্রেশন**

**MCP স্পেসিফিকেশন `2026-07-28`** MCP সার্ভারগুলোকে অনুমতি দেয় তাদের প্রমাণীকরণ বহিরাগত পরিচয় প্রদানকারীদের কাছে দায়িত্বভার দিতে। HTTP পরিবহনের জন্য অনুমোদন প্রতি অনুরোধে মূল্যায়ন করা হয়; স্থানীয় stdio সার্ভার পরিবেশ থেকে শংসাপত্র পায়।




**OWASP MCP ঝুঁকি মোকাবেলা**: [MCP07 - অপর্যাপ্ত প্রমাণীকরণ ও অনুমোদন](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**সিকিউরিটি সুবিধাসমূহ:**
১. **কাস্টম প্রমাণীকরণ ঝুঁকি নির্মূল**: কাস্টম প্রমাণীকরণ ইমপ্লিমেন্টেশন এড়িয়ে ভিন্নতর ঝুঁকি কমানো
২. **এন্টারপ্রাইজ-গ্রেড সিকিউরিটি**: Microsoft Entra ID মত প্রতিষ্ঠিত পরিচয় প্রদানকারীদের উন্নত সিকিউরিটি ফিচার ব্যবহার
৩. **কেন্দ্রীকৃত পরিচয় পরিচালনা**: ব্যবহারকারীর জীবনচক্র ব্যবস্থাপনা, প্রবেশ নিয়ন্ত্রণ, এবং সম্মতি নিরীক্ষা সহজীকরণ
৪. **মাল্টি-ফ্যাক্টর প্রমাণীকরণ**: এন্টারপ্রাইজ পরিচয় প্রদানকারীদের MFA ক্ষমতা উত্তরাধিকারসূত্রে গ্রহণ
৫. **শর্তাধীন অ্যাক্সেস নীতি**: ঝুঁকি-ভিত্তিক প্রবেশ নিয়ন্ত্রণ এবং অভিযোজিত প্রমাণীকরণের সুবিধা

**ইমপ্লিমেন্টেশন চাহিদাসমূহ:**
- **ক্লায়েন্ট রেজিস্ট্রেশন**: ক্লায়েন্ট আইডি মেটাডেটা ডকুমেন্ট পছন্দ করুন অথবা প্রি-রেজিস্ট্রেশন; পুরাতন ডায়নামিক ক্লায়েন্ট রেজিস্ট্রেশন কেবল সামঞ্জস্য জন্য ব্যবহার করুন
 

- **টোকেন অডিয়েন্স যাচাইকরণ**: নিশ্চিত করুন টোকেনগুলি স্পষ্টভাবে MCP সার্ভারের জন্য ইস্যু করা হয়েছে
- **ইস্যুকার যাচাইকরণ**: টোকেন ইস্যুকার প্রত্যাশিত পরিচয় প্রদানকারী মিলেছে কিনা যাচাই করুন
- **স্বাক্ষর যাচাইকরণ**: টোকেনের অখণ্ডতা ক্রিপ্টোগ্রাফিকভাবে যাচাই করুন
- **মেয়াদ উত্তীর্ণ প্রয়োগ**: টোকেনের সময়সীমা কঠোরভাবে প্রয়োগ করুন
- **স্কোপ যাচাইকরণ**: টোকেনের যথাযথ অনুমতিসমূহ নিশ্চিত করুন যা অনুরোধকৃত অপারেশনগুলোর জন্য প্রয়োজনীয়

### **অনুমোদন লজিক সিকিউরিটি**

**গুরুত্বপূর্ণ নিয়ন্ত্রণসমূহ:**
- **ব্যাপক অনুমোদন নিরীক্ষা**: সমস্ত অনুমোদন সিদ্ধান্ত বিন্দুর নিয়মিত সিকিউরিটি পর্যালোচনা
- **ফেইল-সেফ ডিফল্টস**: অনুমোদন লজিক স্পষ্ট সিদ্ধান্ত না পারলে প্রবেশ অস্বীকার করুন
- **অনুমতি সীমারেখা**: বিভিন্ন মর্যাদা স্তর এবং রিসোর্স প্রবেশের মধ্যে পরিষ্কার পৃথকীকরণ
- **নিরীক্ষা লগিং**: নিরাপত্তা পর্যবেক্ষণের জন্য সমস্ত অনুমোদন সিদ্ধান্তের পূর্ণ লগিং
- **নিয়মিত প্রবেশ পর্যালোচনা**: ব্যবহারকারীর অনুমতি ও মর্যাদা নিয়মিত যাচাইকরণ

## ২. **টোকেন সিকিউরিটি ও অ্যান্টি-পাসথ্রু নিয়ন্ত্রণ**

**OWASP MCP ঝুঁকি মোকাবেলা**: [MCP01 - টোকেন অপব্যবস্থাপনা ও গোপনীয়তা ফাঁস](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **টোকেন পাসথ্রু প্রতিরোধ**

**টোকেন পাসথ্রু স্পষ্টভাবে নিষিদ্ধ** MCP অথরাইজেশন স্পেসিফিকেশনে কারণ তা গুরুতর সিকিউরিটি ঝুঁকি সৃষ্টি করে:

**নিরাপত্তা ঝুঁকি মোকাবেলা:**
- **কন্ট্রোল পরিহার**: অত্যাবশ্যক সিকিউরিটি কন্ট্রোল যেমন রেট সীমাবদ্ধতা, অনুরোধ যাচাই, ও ট্রাফিক মনিটরিং এড়িয়ে যাওয়া
- **জবাবদিহিতা ভঙ্গ**: ক্লায়েন্ট সনাক্তকরণ অসম্ভব, যা নিরীক্ষা ট্রেল এবং ঘটনা তদন্ত নষ্ট করে
- **প্রক্সি-ভিত্তিক এক্সফিলট্রেশন**: দূষিত অভিনেতাদের সার্ভারগুলোকে অননুমোদিত তথ্য প্রবেশের প্রক্সি হিসেবে ব্যবহার করার সুযোগ দেয়
- **বিশ্বাস সীমা লঙ্ঘন**: টোকেন উৎস সম্বন্ধে নিচের সেবা বিশ্বাস অনুমান ভেঙে দেয়
- **পার্শ্বগামী চলাচল**: একাধিক সেবায় অপরাধী টোকেন দিয়ে বড় আক্রমণ বিস্তার সম্ভব হয়

**ইমপ্লিমেন্টেশন নিয়ন্ত্রণ:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **নিরাপদ টোকেন ব্যবস্থাপনা প্যাটার্নস**

**সেরা চর্চাসমূহ:**
- **স্বল্পায়ু টোকেন**: ঘন ঘন টোকেন রোটেশনের মাধ্যমে ঝুঁকি কমান
- **প্রয়োজন সময়ে ইস্যু**: নির্দিষ্ট অপারেশনের জন্য দরকার হওয়ার সময়েই টোকেন ইস্যু করুন
- **নিরাপদ সংরক্ষণ**: হার্ডওয়্যার সিকিউরিটি মডিউল (HSM) বা নিরাপদ কী ভল্ট ব্যবহার করুন
- **টোকেন বাইন্ডিং**: টোকেনের লক্ষ্য অডিয়েন্স ও ইস্যুকার যাচাই করুন MCP সংস্থান, ক্লায়েন্ট ও অপারেশনের জন্য
  
- **মনিটরিং ও সতর্কতা**: টোকেনের অপব্যবহার বা অননুমোদিত প্রবেশ প্যাটার্নের রিয়েল-টাইম সনাক্তকরণ

## ৩. **অ্যাপ্লিকেশন স্টেট সিকিউরিটি কন্ট্রোলস**

### **স্টেট হ্যান্ডেল হাইজ্যাকিং প্রতিরোধ**

**আক্রমণ পথসমূহ মোকাবেলা:**
- **হ্যান্ডেল অনুমান**: পূর্বানুমানযোগ্য শনাক্তকারী অন্য কলারের স্টেট প্রকাশ করে
- **ক্রসব্-ইউজার পুনঃব্যবহার**: চুরি করা হ্যান্ডেল ভিন্ন পরিচয়ের সাথে ব্যবহার করা হয়
- **অজ্ঞাত অনুমোদন**: হ্যান্ডেল থাকার অর্থ ভুলভাবে প্রবেশের প্রমাণ মনে করা হয়
  

**স্টেট হ্যান্ডেল কন্ট্রোলস:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**পরিবহন সিকিউরিটি:**
- **HTTPS প্রয়োগ**: দূরবর্তী HTTP পরিবহনে HTTPS বাধ্যতামূলক করুন
- **শংসাপত্র হ্যান্ডলিং**: প্রতিটি HTTP অনুরোধে অথরাইজেশন পাঠান ও যাচাই করুন
- **stdio আইসোলেশন**: প্রক্রিয়া বিচ্ছিন্নতা ও পরিবেশগত শংসাপত্র নিয়ন্ত্রণের মাধ্যমে স্থানীয় stdio সার্ভার সুরক্ষা করুন
  

### **স্টেটফুল বনাম স্ট্যাটলেস বিবেচনা**

MCP `2026-07-28` প্রোটোকল স্তরে স্ট্যাটলেস। অ্যাপ্লিকেশনগুলো এখনও একটি টুল কল থেকে স্পষ্ট হ্যান্ডেল ফেরত দিয়ে এবং পরবর্তী কলগুলোতে সেটা সাধারণ আর্গুমেন্ট হিসেবে গ্রহণ করে স্টেট বজায় রাখতে পারে।

 

- স্টেট আলাদা সংরক্ষণ করুণ যেকোন একটি পরিবহন সংযোগ থেকে স্বাধীনভাবে।
- স্টেট হ্যান্ডেলগুলো প্রমাণীকৃত মূল সার্ভার-পাশের সাথে সংযোজন করুন।
- একটি হ্যান্ডেলকে নাম হিসেবে বিবেচনা করুন, বহনকারী শংসাপত্র হিসেবে নয়।
- স্টাল হ্যান্ডেলগুলোর মেয়াদোত্তীর্ণতা ও পুনরুদ্ধার আচরণ নির্ধারণ করুন।

## ৪. **AI-নির্দিষ্ট সিকিউরিটি কন্ট্রোলস**

**OWASP MCP ঝুঁকি মোকাবেলা**:

- [MCP06 - ইরাদা প্রবাহ সাবভার্শন](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - টুল বিষক্রিয়া](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - কমান্ড ইনজেকশন ও কার্যকরীতা](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **প্রম্পট ইনজেকশন প্রতিরক্ষা**

**মাইক্রোসফট প্রম্পট শিল্ডস ইন্টিগ্রেশন:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**বাস্তবায়ন নিয়ন্ত্রণ:**
- **ইনপুট স্যানিটাইজেশন**: সকল ব্যবহারকারী ইনপুট এর পূর্ণাঙ্গ যাচাই ও ফিল্টারিং
- **বিষয়বস্তু সীমানা সংজ্ঞা**: সিস্টেম নির্দেশনা ও ব্যবহারকারী বিষয়বস্তু মাঝে স্পষ্ট বিভাজন
- **নির্দেশনা শ্রেণিবিন্যাস**: বিরোধপূর্ণ নির্দেশনাগুলোর সঠিক প্রাধান্য বিধান
- **আউটপুট পর্যবেক্ষণ**: সম্ভাব্য ক্ষতিকর বা প্রভাবিত আউটপুট সনাক্তকরণ

### **টুল বিষক্রিয়া প্রতিরোধ**

**টুল সুরক্ষা ফ্রেমওয়ার্ক:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**ডায়নামিক টুল ব্যবস্থাপনা:**
- **অনুমোদন কার্যপ্রবাহ**: টুল পরিবর্তনের জন্য স্পষ্ট ব্যবহারকারী সম্মতি
- **রোলব্যাক সক্ষমতা**: পূর্ববর্তী টুল সংস্করণে প্রত্যাবর্তনের ক্ষমতা
- **পরিবর্তন নিরীক্ষণ**: টুল সংজ্ঞা পরিবর্তনের সম্পূর্ণ ইতিহাস
- **ঝুঁকি মূল্যায়ন**: টুল সুরক্ষা অবস্থার স্বয়ংক্রিয় মূল্যায়ন

## ৫. **কনফিউজড ডেপুটি আক্রমণ প্রতিরোধ**

### **OAuth প্রক্সি সুরক্ষা**

**আক্রমণ প্রতিরোধ নিয়ন্ত্রণ:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**বাস্তবায়ন প্রয়োজনীয়তা:**
- **ক্লায়েন্ট নিবন্ধন**: পূর্ব-নিবন্ধন বা ক্লায়েন্ট আইডি মেটাডেটা ডকুমেন্টস অগ্রাধিকার; ডায়নামিক ক্লায়েন্ট নিবন্ধনকে সামঞ্জস্যপূর্ণ ফ্যালব্যাক হিসেবে বিবেচনা করা হয়

- **ব্যবহারকারী সম্মতি যাচাই**: MCP প্রক্সিগুলো যেগুলো একটি স্থির তৃতীয় পক্ষ ক্লায়েন্ট আইডি ব্যবহার করে, তাদের প্রতিটি ক্লায়েন্টের সম্মতি গ্রহণ করা আবশ্যক পাচারের আগে

- **রিডাইরেক্ট URI যাচাই**: রিডাইরেক্ট গন্তব্যের কঠোর হোয়াইটলিস্ট ভিত্তিক যাচাই
- **অনুমোদন কোড সুরক্ষা**: স্বল্পস্থায়ী কোড, একবার ব্যবহারের জন্য বাধ্যতামূলক
- **ক্লায়েন্ট পরিচয় যাচাই**: ক্লায়েন্ট সনদ ও মেটাডেটার মজবুত যাচাই

## ৬. **টুল কার্যকরীতা সুরক্ষা**

### **স্যান্ডবক্সিং ও পৃথকীকরণ**

**কন্টেইনার-ভিত্তিক পৃথকীকরণ:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**প্রক্রিয়া পৃথকীকরণ:**
- **পৃথক প্রক্রিয়া প্রসঙ্গ**: প্রতিটি টুল কার্যকরীতা পৃথকপ্রক্রিয়া স্পেসে
- **ইন্টার-প্রসেস যোগাযোগ**: যাচাইসহ নিরাপদ আইপিসি ব্যবস্থা
- **প্রক্রিয়া পর্যবেক্ষণ**: রানটাইম আচরণ বিশ্লেষণ ও অস্বাভাবিকতা সনাক্তকরণ
- **সম্পদ প্রয়োগ**: CPU, মেমোরি, এবং I/O অপারেশনগুলিতে কঠোর সীমা আরোপ

### **সর্বনিম্ন প্রিভিলিজ বাস্তবায়ন**

**অনুমতি পরিচালনা:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## ৭. **সরবরাহ চেইন সুরক্ষা নিয়ন্ত্রণ**

**OWASP MCP ঝুঁকি সমাধান**: [MCP04 - সফটওয়্যার সরবরাহ চেইন আক্রমণ ও নির্ভরতা ছলনা](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **নির্ভরতা যাচাই**

**সম্পূর্ণ উপাদান সুরক্ষা:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **অবিচ্ছিন্ন পর্যবেক্ষণ**

**সরবরাহ চেইন হুমকি সনাক্তকরণ:**
- **নির্ভরতা স্বাস্থ্য পর্যবেক্ষণ**: নিরাপত্তা সমস্যা নিরূপণের জন্য সকল নির্ভরতার ধারাবাহিক মূল্যায়ন
- **হুমকি বুদ্ধিমত্তা ইন্টিগ্রেশন**: উদীয়মান সরবরাহ চেইন হুমকির রিয়েল-টাইম আপডেট
- **আচরণ বিশ্লেষণ**: বাহ্যিক উপাদানগুলিতে অস্বাভাবিক আচরণ সনাক্তকরণ
- **স্বয়ংক্রিয় প্রতিক্রিয়া**: ক্ষতিগ্রস্ত উপাদানগুলির তাৎক্ষণিক নিয়ন্ত্রণ

## ৮. **পর্যবেক্ষণ ও সনাক্তকরণ নিয়ন্ত্রণ**

**OWASP MCP ঝুঁকি সমাধান**: [MCP08 - নিরীক্ষণ ও টেলিমেট্রির অভাব](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **নিরাপত্তা তথ্য ও ইভেন্ট ব্যবস্থাপনা (SIEM)**

**সম্পূর্ণ লগিং কৌশল:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **রিয়েল-টাইম হুমকি সনাক্তকরণ**

**আচরণ বিশ্লেষণ:**
- **ব্যবহারকারীর আচরণ বিশ্লেষণ (UBA)**: অস্বাভাবিক ব্যবহারকারীর প্রবেশ প্যাটার্ন সনাক্তকরণ
- **সত্তার আচরণ বিশ্লেষণ (EBA)**: MCP সার্ভার ও টুল আচরণ পর্যবেক্ষণ
- **মেশিন লার্নিং অ্যানোমালি সনাক্তকরণ**: এআই-শক্তিকৃত নিরাপত্তা হুমকি শনাক্তকরণ
- **হুমকি বুদ্ধিমত্তা সম্পর্কিতকরণ**: পর্যবেক্ষিত কর্মকাণ্ডের সাথে পরিচিত আক্রমণ প্যাটার্ন মিলানো

## ৯. **ঘটনা প্রতিক্রিয়া ও পুনরুদ্ধার**

### **স্বয়ংক্রিয় প্রতিক্রিয়া সক্ষমতা**

**তাৎক্ষণিক প্রতিক্রিয়া কর্মসূচি:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **ফরেনসিক ক্ষমতা**

**তদন্ত সহায়তা:**
- **নিরীক্ষা ট্রেইল সংরক্ষণ**: ক্রিপ্টোগ্রাফিক ইন্টিগ্রিটি সুত্রযুক্ত অপরিবর্তনীয় লগিং
- **প্রমাণ সংগ্রহ**: প্রাসঙ্গিক নিরাপত্তা উপকরণের স্বয়ংক্রিয় সংগ্রহ
- **টাইমলাইন পুনর্গঠন**: নিরাপত্তা ঘটনার পূর্ববর্তী বিস্তারিত সিকোয়েন্স
- **প্রভাব মূল্যায়ন**: সংকটের পরিসর ও তথ্য সুরক্ষা মূল্যায়ন

## **মুখ্য নিরাপত্তা স্থাপত্য নীতি**

### **গভীর স্তরে প্রতিরক্ষা**
- **বহু নিরাপত্তা স্তর**: নিরাপত্তা স্থাপত্যে কোনো একক ব্যর্থতা বিন্দু নেই
- **অতিরিক্ত নিয়ন্ত্রণ**: গুরুত্বপূর্ণ ফাংশনের জন্য ওভারল্যাপিং নিরাপত্তা ব্যবস্থা
- **ফেল-সেফ মেকানিজম**: ত্রুটি বা আক্রমণের সময় সুরক্ষিত ডিফল্ট ব্যবস্থা

### **জিরো ট্রাস্ট বাস্তবায়ন**
- **কখনো বিশ্বাস করবেন না, সর্বদা যাচাই করুন**: সকল সত্তা ও অনুরোধের ধারাবাহিক যাচাই
- **সর্বনিম্ন প্রিভিলিজ নীতি**: সকল উপাদানের জন্য সর্বনিম্ন প্রবেশাধিকারের ন্যূনতমতা
- **মাইক্রো-সেগমেন্টেশন**: সূক্ষ্ম নেটওয়ার্ক ও প্রবেশ নিয়ন্ত্রণ

### **অবিচ্ছিন্ন নিরাপত্তা উন্নয়ন**
- **হুমকি দৃশ্যপট অভিযোজন**: উদীয়মান হুমকি মোকাবিলায় নিয়মিত আপডেট
- **নিরাপত্তা নিয়ন্ত্রণ কার্যকরীতা**: নিয়ন্ত্রণের ধারাবাহিক মূল্যায়ন ও উন্নয়ন
- **বৈশিষ্ট্য সামঞ্জস্যতা**: ক্রমবর্ধমান MCP নিরাপত্তা মানদণ্ডের সাথে সামঞ্জস্যতা

---

## **বাস্তবায়ন সম্পদসমূহ**

### **আধিকারিক MCP ডকুমেন্টেশন**
- [MCP স্পেসিফিকেশন (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP নিরাপত্তা সেরা প্র্যাকটিস](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP অনুমোদন স্পেসিফিকেশন](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP নিরাপত্তা সম্পদ**
- [OWASP MCP Azure নিরাপত্তা গাইড](https://microsoft.github.io/mcp-azure-security-guide/) - ব্যাপক OWASP MCP শীর্ষ ১০ Azure বাস্তবায়নসহ
- [OWASP MCP শীর্ষ ১০](https://owasp.org/www-project-mcp-top-10/) - অফিসিয়াল OWASP MCP নিরাপত্তা ঝুঁকি
- [MCP নিরাপত্তা সম্মেলন কর্মশালা (শেরপা)](https://azure-samples.github.io/sherpa/) - Azure এ MCP এর জন্য হাতে কলমে নিরাপত্তা প্রশিক্ষণ

### **মাইক্রোসফট নিরাপত্তা সমাধানসমূহ**
- [মাইক্রোসফট প্রম্পট শিল্ডস](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure কনটেন্ট সেফটি](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub উন্নত নিরাপত্তা](https://github.com/security/advanced-security)
- [Azure কী ভল্ট](https://learn.microsoft.com/azure/key-vault/)

### **নিরাপত্তা মানদণ্ড**
- [OAuth 2.0 নিরাপত্তা সেরা প্র্যাকটিস (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [বড় ভাষা মডেলগুলির জন্য OWASP টপ ১০](https://genai.owasp.org/)

- [NIST সাইবারসিকিউরিটি ফ্রেমওয়ার্ক](https://www.nist.gov/cyberframework)

---

> **গুরুত্বপূর্ণ:** এই নিরাপত্তা নিয়ন্ত্রণগুলি MCP স্পেসিফিকেশন
> `2026-07-28` প্রতিফলিত করে। সবসময় যাচাই করুন
> [বর্তমান আনুষ্ঠানিক ডকুমেন্টেশন](https://modelcontextprotocol.io/specification/2026-07-28/)
> কারণ মানগুলি অবিরত উন্নীত হচ্ছে।

## পরবর্তী কী

- ফেরত যান: [সিকিউরিটি মডিউল ওভারভিউ](./README.md)
- চালিয়ে যান: [মডিউল ৩: শুরু করা](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->