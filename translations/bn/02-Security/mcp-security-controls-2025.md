# MCP সিকিউরিটি কন্ট্রোলস - ডিসেম্বর ২০২৫ আপডেট

> **বর্তমান স্ট্যান্ডার্ড**: এই ডকুমেন্টটি [MCP স্পেসিফিকেশন ২০২৫-১১-২৫](https://spec.modelcontextprotocol.io/specification/2025-11-25/) সিকিউরিটি প্রয়োজনীয়তা এবং অফিসিয়াল [MCP সিকিউরিটি বেস্ট প্র্যাকটিসেস](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) প্রতিফলিত করে।

মডেল কনটেক্সট প্রোটোকল (MCP) উল্লেখযোগ্যভাবে পরিণত হয়েছে উন্নত সিকিউরিটি কন্ট্রোলস সহ যা ঐতিহ্যবাহী সফটওয়্যার সিকিউরিটি এবং AI-নির্দিষ্ট হুমকির উভয়কেই মোকাবেলা করে। এই ডকুমেন্টটি ডিসেম্বর ২০২৫ পর্যন্ত নিরাপদ MCP বাস্তবায়নের জন্য বিস্তৃত সিকিউরিটি কন্ট্রোলস প্রদান করে।

## **আবশ্যকীয় সিকিউরিটি প্রয়োজনীয়তা**

### **MCP স্পেসিফিকেশন থেকে গুরুত্বপূর্ণ নিষেধাজ্ঞা:**

> **নিষিদ্ধ**: MCP সার্ভারগুলি **অবশ্যই গ্রহণ করবে না** এমন কোনো টোকেন যা স্পষ্টভাবে MCP সার্ভারের জন্য ইস্যু করা হয়নি  
>
> **নিষিদ্ধ**: MCP সার্ভারগুলি **অবশ্যই ব্যবহার করবে না** সেশনগুলি প্রমাণীকরণের জন্য  
>
> **প্রয়োজনীয়**: MCP সার্ভারগুলি অনুমোদন বাস্তবায়ন করলে **অবশ্যই** সমস্ত ইনবাউন্ড অনুরোধ যাচাই করবে  
>
> **আবশ্যকীয়**: MCP প্রক্সি সার্ভারগুলি যা স্ট্যাটিক ক্লায়েন্ট আইডি ব্যবহার করে **অবশ্যই** প্রতিটি ডায়নামিকভাবে নিবন্ধিত ক্লায়েন্টের জন্য ব্যবহারকারীর সম্মতি গ্রহণ করবে

---

## ১. **প্রমাণীকরণ ও অনুমোদন কন্ট্রোলস**

### **বাহ্যিক পরিচয় প্রদানকারী ইন্টিগ্রেশন**

**বর্তমান MCP স্ট্যান্ডার্ড (২০২৫-০৬-১৮)** MCP সার্ভারগুলিকে বাহ্যিক পরিচয় প্রদানকারীদের কাছে প্রমাণীকরণ ডেলিগেট করার অনুমতি দেয়, যা একটি উল্লেখযোগ্য সিকিউরিটি উন্নতি প্রতিনিধিত্ব করে:

### **বাহ্যিক পরিচয় প্রদানকারী ইন্টিগ্রেশন**

**বর্তমান MCP স্ট্যান্ডার্ড (২০২৫-১১-২৫)** MCP সার্ভারগুলিকে বাহ্যিক পরিচয় প্রদানকারীদের কাছে প্রমাণীকরণ ডেলিগেট করার অনুমতি দেয়, যা একটি উল্লেখযোগ্য সিকিউরিটি উন্নতি প্রতিনিধিত্ব করে:

**সিকিউরিটি সুবিধাসমূহ:**
1. **কাস্টম প্রমাণীকরণ ঝুঁকি নির্মূল করে**: কাস্টম প্রমাণীকরণ বাস্তবায়ন এড়িয়ে ঝুঁকির পৃষ্ঠ কমায়  
2. **এন্টারপ্রাইজ-গ্রেড সিকিউরিটি**: Microsoft Entra ID-এর মতো প্রতিষ্ঠিত পরিচয় প্রদানকারীদের উন্নত সিকিউরিটি বৈশিষ্ট্য ব্যবহার করে  
3. **কেন্দ্রীভূত পরিচয় ব্যবস্থাপনা**: ব্যবহারকারীর জীবনচক্র ব্যবস্থাপনা, অ্যাক্সেস নিয়ন্ত্রণ এবং সম্মতি নিরীক্ষণ সহজ করে  
4. **মাল্টি-ফ্যাক্টর প্রমাণীকরণ**: এন্টারপ্রাইজ পরিচয় প্রদানকারীদের থেকে MFA ক্ষমতা উত্তরাধিকারসূত্রে পায়  
5. **শর্তাধীন অ্যাক্সেস নীতি**: ঝুঁকি-ভিত্তিক অ্যাক্সেস নিয়ন্ত্রণ এবং অভিযোজিত প্রমাণীকরণের সুবিধা

**বাস্তবায়ন প্রয়োজনীয়তা:**
- **টোকেন অডিয়েন্স যাচাই**: নিশ্চিত করুন সব টোকেন স্পষ্টভাবে MCP সার্ভারের জন্য ইস্যু করা হয়েছে  
- **ইস্যুকারী যাচাই**: টোকেন ইস্যুকারী প্রত্যাশিত পরিচয় প্রদানকারীর সাথে মেলে কিনা যাচাই করুন  
- **স্বাক্ষর যাচাই**: টোকেনের অখণ্ডতার ক্রিপ্টোগ্রাফিক যাচাই  
- **মেয়াদ উত্তীর্ণ প্রয়োগ**: টোকেনের জীবনকাল সীমা কঠোরভাবে প্রয়োগ করুন  
- **স্কোপ যাচাই**: নিশ্চিত করুন টোকেনগুলিতে অনুরোধকৃত অপারেশনের জন্য উপযুক্ত অনুমতি রয়েছে

### **অনুমোদন লজিক সিকিউরিটি**

**গুরুত্বপূর্ণ কন্ট্রোলস:**
- **ব্যাপক অনুমোদন নিরীক্ষা**: সমস্ত অনুমোদন সিদ্ধান্ত পয়েন্টের নিয়মিত সিকিউরিটি পর্যালোচনা  
- **ফেইল-সেফ ডিফল্টস**: অনুমোদন লজিক স্পষ্ট সিদ্ধান্ত নিতে না পারলে অ্যাক্সেস অস্বীকার করুন  
- **অনুমতি সীমানা**: বিভিন্ন বিশেষাধিকার স্তর এবং সম্পদ অ্যাক্সেসের মধ্যে স্পষ্ট বিভাজন  
- **নিরীক্ষা লগিং**: সিকিউরিটি পর্যবেক্ষণের জন্য সমস্ত অনুমোদন সিদ্ধান্তের সম্পূর্ণ লগিং  
- **নিয়মিত অ্যাক্সেস পর্যালোচনা**: ব্যবহারকারীর অনুমতি এবং বিশেষাধিকার নিয়মিত যাচাই

## ২. **টোকেন সিকিউরিটি ও অ্যান্টি-পাসথ্রু কন্ট্রোলস**

### **টোকেন পাসথ্রু প্রতিরোধ**

**টোকেন পাসথ্রু MCP অনুমোদন স্পেসিফিকেশনে স্পষ্টভাবে নিষিদ্ধ কারণ তা গুরুতর সিকিউরিটি ঝুঁকি সৃষ্টি করে:**

**সিকিউরিটি ঝুঁকি মোকাবেলা:**
- **নিয়ন্ত্রণ এড়ানো**: রেট লিমিটিং, অনুরোধ যাচাই, এবং ট্রাফিক পর্যবেক্ষণের মতো অপরিহার্য সিকিউরিটি কন্ট্রোলস বাইপাস করে  
- **দায়িত্বহীনতা ভঙ্গ**: ক্লায়েন্ট সনাক্তকরণ অসম্ভব করে, যা নিরীক্ষা ট্রেইল এবং ঘটনা তদন্তকে দুর্নীতিগ্রস্ত করে  
- **প্রক্সি-ভিত্তিক তথ্য চুরি**: অননুমোদিত ডেটা অ্যাক্সেসের জন্য সার্ভারকে প্রক্সি হিসেবে ব্যবহার করার সুযোগ দেয়  
- **বিশ্বাস সীমানা লঙ্ঘন**: টোকেন উৎস সম্পর্কে ডাউনস্ট্রিম সার্ভিসের বিশ্বাস ভঙ্গ করে  
- **পার্শ্ববর্তী গতিবিধি**: একাধিক সার্ভিসে ক্ষতিগ্রস্ত টোকেন ব্যবহার করে বিস্তৃত আক্রমণ সম্প্রসারণ সম্ভব করে

**বাস্তবায়ন কন্ট্রোলস:**
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

**সেরা অনুশীলন:**
- **স্বল্পমেয়াদী টোকেন**: ঘন ঘন টোকেন রোটেশনের মাধ্যমে এক্সপোজার উইন্ডো কমান  
- **যথাসময়ে ইস্যু**: নির্দিষ্ট অপারেশনের জন্য প্রয়োজন হলে টোকেন ইস্যু করুন  
- **নিরাপদ সংরক্ষণ**: হার্ডওয়্যার সিকিউরিটি মডিউল (HSM) বা নিরাপদ কী ভল্ট ব্যবহার করুন  
- **টোকেন বাইনডিং**: সম্ভব হলে টোকেনকে নির্দিষ্ট ক্লায়েন্ট, সেশন বা অপারেশনের সাথে বেঁধে দিন  
- **পর্যবেক্ষণ ও সতর্কতা**: টোকেন অপব্যবহার বা অননুমোদিত অ্যাক্সেস প্যাটার্নের রিয়েল-টাইম সনাক্তকরণ

## ৩. **সেশন সিকিউরিটি কন্ট্রোলস**

### **সেশন হাইজ্যাকিং প্রতিরোধ**

**আক্রমণ ভেক্টরসমূহ:**
- **সেশন হাইজ্যাক প্রম্পট ইনজেকশন**: শেয়ার করা সেশন স্টেটে ক্ষতিকর ইভেন্ট ইনজেকশন  
- **সেশন ছদ্মবেশ**: চুরি হওয়া সেশন আইডি ব্যবহার করে প্রমাণীকরণ বাইপাস  
- **রিসিউমেবল স্ট্রিম আক্রমণ**: সার্ভার-সেন্ট ইভেন্ট রিসাম্পশনের মাধ্যমে ক্ষতিকর কন্টেন্ট ইনজেকশন

**আবশ্যকীয় সেশন কন্ট্রোলস:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**ট্রান্সপোর্ট সিকিউরিটি:**
- **HTTPS প্রয়োগ**: সমস্ত সেশন যোগাযোগ TLS 1.3 এর মাধ্যমে  
- **নিরাপদ কুকি অ্যাট্রিবিউটস**: HttpOnly, Secure, SameSite=Strict  
- **সার্টিফিকেট পিনিং**: MITM আক্রমণ প্রতিরোধে গুরুত্বপূর্ণ সংযোগের জন্য

### **স্টেটফুল বনাম স্টেটলেস বিবেচনা**

**স্টেটফুল বাস্তবায়নের জন্য:**
- শেয়ার করা সেশন স্টেট ইনজেকশন আক্রমণের বিরুদ্ধে অতিরিক্ত সুরক্ষা প্রয়োজন  
- কিউ-ভিত্তিক সেশন ব্যবস্থাপনায় অখণ্ডতা যাচাই প্রয়োজন  
- একাধিক সার্ভার ইনস্ট্যান্সের জন্য নিরাপদ সেশন স্টেট সিঙ্ক্রোনাইজেশন প্রয়োজন

**স্টেটলেস বাস্তবায়নের জন্য:**
- JWT বা অনুরূপ টোকেন-ভিত্তিক সেশন ব্যবস্থাপনা  
- সেশন স্টেট অখণ্ডতার ক্রিপ্টোগ্রাফিক যাচাই  
- আক্রমণ পৃষ্ঠ কম কিন্তু শক্তিশালী টোকেন যাচাই প্রয়োজন

## ৪. **AI-নির্দিষ্ট সিকিউরিটি কন্ট্রোলস**

### **প্রম্পট ইনজেকশন প্রতিরোধ**

**Microsoft Prompt Shields ইন্টিগ্রেশন:**
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

**বাস্তবায়ন কন্ট্রোলস:**
- **ইনপুট স্যানিটাইজেশন**: সমস্ত ব্যবহারকারী ইনপুটের ব্যাপক যাচাই ও ফিল্টারিং  
- **কন্টেন্ট সীমানা সংজ্ঞায়ন**: সিস্টেম নির্দেশনা এবং ব্যবহারকারী কন্টেন্টের মধ্যে স্পষ্ট বিভাজন  
- **নির্দেশনা শ্রেণিবিন্যাস**: বিরোধপূর্ণ নির্দেশনার জন্য সঠিক অগ্রাধিকার নিয়ম  
- **আউটপুট পর্যবেক্ষণ**: সম্ভাব্য ক্ষতিকর বা পরিবর্তিত আউটপুট সনাক্তকরণ

### **টুল পয়জনিং প্রতিরোধ**

**টুল সিকিউরিটি ফ্রেমওয়ার্ক:**
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

**ডায়নামিক টুল ব্যবস্থাপনা:**
- **অনুমোদন ওয়ার্কফ্লো**: টুল পরিবর্তনের জন্য স্পষ্ট ব্যবহারকারী সম্মতি  
- **রোলব্যাক ক্ষমতা**: পূর্ববর্তী টুল সংস্করণে ফিরে যাওয়ার সক্ষমতা  
- **পরিবর্তন নিরীক্ষণ**: টুল সংজ্ঞার পরিবর্তনের সম্পূর্ণ ইতিহাস  
- **ঝুঁকি মূল্যায়ন**: টুল সিকিউরিটি অবস্থার স্বয়ংক্রিয় মূল্যায়ন

## ৫. **কনফিউজড ডেপুটি আক্রমণ প্রতিরোধ**

### **OAuth প্রক্সি সিকিউরিটি**

**আক্রমণ প্রতিরোধ কন্ট্রোলস:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**বাস্তবায়ন প্রয়োজনীয়তা:**
- **ব্যবহারকারী সম্মতি যাচাই**: ডায়নামিক ক্লায়েন্ট নিবন্ধনের জন্য কখনো সম্মতি স্ক্রিন এড়াবেন না  
- **রিডাইরেক্ট URI যাচাই**: রিডাইরেক্ট গন্তব্যের কঠোর হোয়াইটলিস্ট ভিত্তিক যাচাই  
- **অনুমোদন কোড সুরক্ষা**: স্বল্পমেয়াদী কোড এবং একবার ব্যবহার প্রয়োগ  
- **ক্লায়েন্ট পরিচয় যাচাই**: ক্লায়েন্ট ক্রেডেনশিয়াল এবং মেটাডেটার শক্তিশালী যাচাই

## ৬. **টুল এক্সিকিউশন সিকিউরিটি**

### **স্যান্ডবক্সিং ও আইসোলেশন**

**কন্টেইনার-ভিত্তিক আইসোলেশন:**
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

**প্রসেস আইসোলেশন:**
- **বিভিন্ন প্রসেস কনটেক্সট**: প্রতিটি টুল এক্সিকিউশন আলাদা প্রসেস স্পেসে  
- **ইন্টার-প্রসেস কমিউনিকেশন**: যাচাইসহ নিরাপদ IPC মেকানিজম  
- **প্রসেস মনিটরিং**: রানটাইম আচরণ বিশ্লেষণ ও অস্বাভাবিকতা সনাক্তকরণ  
- **রিসোর্স প্রয়োগ**: CPU, মেমরি, এবং I/O অপারেশনের কঠোর সীমা

### **সর্বনিম্ন বিশেষাধিকার বাস্তবায়ন**

**অনুমতি ব্যবস্থাপনা:**
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

## ৭. **সাপ্লাই চেইন সিকিউরিটি কন্ট্রোলস**

### **ডিপেনডেন্সি যাচাই**

**ব্যাপক উপাদান সিকিউরিটি:**
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

### **নিরবিচ্ছিন্ন পর্যবেক্ষণ**

**সাপ্লাই চেইন হুমকি সনাক্তকরণ:**
- **ডিপেনডেন্সি স্বাস্থ্য পর্যবেক্ষণ**: সমস্ত ডিপেনডেন্সির সিকিউরিটি সমস্যা নিয়মিত মূল্যায়ন  
- **হুমকি বুদ্ধিমত্তা ইন্টিগ্রেশন**: উদীয়মান সাপ্লাই চেইন হুমকির রিয়েল-টাইম আপডেট  
- **আচরণ বিশ্লেষণ**: বাহ্যিক উপাদানের অস্বাভাবিক আচরণ সনাক্তকরণ  
- **স্বয়ংক্রিয় প্রতিক্রিয়া**: ক্ষতিগ্রস্ত উপাদানগুলির তাৎক্ষণিক নিয়ন্ত্রণ

## ৮. **পর্যবেক্ষণ ও সনাক্তকরণ কন্ট্রোলস**

### **সিকিউরিটি ইনফরমেশন ও ইভেন্ট ম্যানেজমেন্ট (SIEM)**

**ব্যাপক লগিং কৌশল:**
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

### **রিয়েল-টাইম হুমকি সনাক্তকরণ**

**আচরণ বিশ্লেষণ:**
- **ব্যবহারকারী আচরণ বিশ্লেষণ (UBA)**: অস্বাভাবিক ব্যবহারকারী অ্যাক্সেস প্যাটার্ন সনাক্তকরণ  
- **এন্টিটি আচরণ বিশ্লেষণ (EBA)**: MCP সার্ভার এবং টুল আচরণ পর্যবেক্ষণ  
- **মেশিন লার্নিং অ্যানোমালি সনাক্তকরণ**: AI-চালিত সিকিউরিটি হুমকি সনাক্তকরণ  
- **হুমকি বুদ্ধিমত্তা সম্পর্ক**: পরিচিত আক্রমণ প্যাটার্নের সাথে পর্যবেক্ষিত কার্যকলাপ মিলানো

## ৯. **ঘটনা প্রতিক্রিয়া ও পুনরুদ্ধার**

### **স্বয়ংক্রিয় প্রতিক্রিয়া ক্ষমতা**

**তাৎক্ষণিক প্রতিক্রিয়া কর্মসূচি:**
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

**তদন্ত সহায়তা:**
- **নিরীক্ষা ট্রেইল সংরক্ষণ**: অপরিবর্তনীয় লগিং ক্রিপ্টোগ্রাফিক অখণ্ডতা সহ  
- **প্রমাণ সংগ্রহ**: প্রাসঙ্গিক সিকিউরিটি আর্টিফ্যাক্ট স্বয়ংক্রিয় সংগ্রহ  
- **টাইমলাইন পুনর্গঠন**: সিকিউরিটি ঘটনার বিস্তারিত ক্রম  
- **প্রভাব মূল্যায়ন**: আপসের পরিধি এবং ডেটা এক্সপোজার মূল্যায়ন

## **মূল সিকিউরিটি আর্কিটেকচার নীতিমালা**

### **ডিফেন্স ইন ডেপথ**
- **একাধিক সিকিউরিটি স্তর**: সিকিউরিটি আর্কিটেকচারে কোনো একক ব্যর্থতা বিন্দু নেই  
- **অতিরিক্ত কন্ট্রোলস**: গুরুত্বপূর্ণ ফাংশনের জন্য ওভারল্যাপিং সিকিউরিটি ব্যবস্থা  
- **ফেইল-সেফ মেকানিজম**: সিস্টেম ত্রুটি বা আক্রমণের সময় নিরাপদ ডিফল্টস

### **জিরো ট্রাস্ট বাস্তবায়ন**
- **কখনো বিশ্বাস করবেন না, সর্বদা যাচাই করুন**: সমস্ত সত্তা এবং অনুরোধের ধারাবাহিক যাচাই  
- **সর্বনিম্ন বিশেষাধিকার নীতি**: সমস্ত উপাদানের জন্য সর্বনিম্ন অ্যাক্সেস অধিকার  
- **মাইক্রো-সেগমেন্টেশন**: সূক্ষ্ম নেটওয়ার্ক এবং অ্যাক্সেস নিয়ন্ত্রণ

### **নিরবিচ্ছিন্ন সিকিউরিটি বিবর্তন**
- **হুমকি ল্যান্ডস্কেপ অভিযোজন**: উদীয়মান হুমকি মোকাবেলায় নিয়মিত আপডেট  
- **সিকিউরিটি কন্ট্রোল কার্যকারিতা**: কন্ট্রোলের চলমান মূল্যায়ন ও উন্নতি  
- **স্পেসিফিকেশন সম্মতি**: পরিবর্তনশীল MCP সিকিউরিটি স্ট্যান্ডার্ডের সাথে সামঞ্জস্য

---

## **বাস্তবায়ন সম্পদ**

### **অফিসিয়াল MCP ডকুমেন্টেশন**
- [MCP স্পেসিফিকেশন (২০২৫-১১-২৫)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP সিকিউরিটি বেস্ট প্র্যাকটিসেস](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP অনুমোদন স্পেসিফিকেশন](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft সিকিউরিটি সলিউশনস**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **সিকিউরিটি স্ট্যান্ডার্ডস**
- [OAuth 2.0 সিকিউরিটি বেস্ট প্র্যাকটিসেস (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP টপ ১০ ফর লার্জ ল্যাঙ্গুয়েজ মডেলস](https://genai.owasp.org/)
- [NIST সাইবারসিকিউরিটি ফ্রেমওয়ার্ক](https://www.nist.gov/cyberframework)

---

> **গুরুত্বপূর্ণ**: এই সিকিউরিটি কন্ট্রোলস বর্তমান MCP স্পেসিফিকেশন (২০২৫-০৬-১৮) প্রতিফলিত করে। সর্বদা সর্বশেষ [অফিসিয়াল ডকুমেন্টেশন](https://spec.modelcontextprotocol.io/) এর সাথে যাচাই করুন কারণ স্ট্যান্ডার্ডগুলি দ্রুত পরিবর্তিত হচ্ছে।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->