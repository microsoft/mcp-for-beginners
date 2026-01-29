# MCP ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ - ਦਸੰਬਰ 2025 ਅੱਪਡੇਟ

> **ਮੌਜੂਦਾ ਮਿਆਰ**: ਇਹ ਦਸਤਾਵੇਜ਼ [MCP ਵਿਸ਼ੇਸ਼ਤਾ 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਅਤੇ ਅਧਿਕਾਰਕ [MCP ਸੁਰੱਖਿਆ ਸਰਵੋਤਮ ਅਭਿਆਸ](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।

ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਨੇ ਪਰੰਪਰਾਗਤ ਸਾਫਟਵੇਅਰ ਸੁਰੱਖਿਆ ਅਤੇ AI-ਵਿਸ਼ੇਸ਼ ਖ਼ਤਰਿਆਂ ਨੂੰ ਸੰਬੋਧਨ ਕਰਦੇ ਹੋਏ ਬਹੁਤ ਵਿਕਸਤ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਪ੍ਰਦਾਨ ਕੀਤੇ ਹਨ। ਇਹ ਦਸਤਾਵੇਜ਼ ਦਸੰਬਰ 2025 ਤੱਕ ਸੁਰੱਖਿਅਤ MCP ਲਾਗੂ ਕਰਨ ਲਈ ਵਿਸਤ੍ਰਿਤ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## **ਲਾਜ਼ਮੀ ਸੁਰੱਖਿਆ ਲੋੜਾਂ**

### **MCP ਵਿਸ਼ੇਸ਼ਤਾ ਤੋਂ ਅਹਿਮ ਮਨਾਹੀਆਂ:**

> **ਮਨਾਹੀ ਹੈ**: MCP ਸਰਵਰਾਂ ਨੂੰ ਕੋਈ ਵੀ ਟੋਕਨ ਸਵੀਕਾਰ ਨਹੀਂ ਕਰਨੇ ਚਾਹੀਦੇ ਜੋ ਖਾਸ ਤੌਰ 'ਤੇ MCP ਸਰਵਰ ਲਈ ਜਾਰੀ ਨਹੀਂ ਕੀਤੇ ਗਏ  
>
> **ਪਾਬੰਦੀ ਹੈ**: MCP ਸਰਵਰਾਂ ਨੂੰ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਸੈਸ਼ਨ ਵਰਤਣ ਦੀ ਆਗਿਆ ਨਹੀਂ ਹੈ  
>
> **ਲਾਜ਼ਮੀ ਹੈ**: MCP ਸਰਵਰ ਜੋ ਅਧਿਕਾਰ ਲਾਗੂ ਕਰਦੇ ਹਨ ਉਹ ਸਾਰੇ ਆਉਣ ਵਾਲੇ ਬੇਨਤੀਆਂ ਦੀ ਜਾਂਚ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ  
>
> **ਲਾਜ਼ਮੀ ਹੈ**: MCP ਪ੍ਰਾਕਸੀ ਸਰਵਰ ਜੋ ਸਥਿਰ ਕਲਾਇੰਟ ID ਵਰਤਦੇ ਹਨ ਉਹ ਹਰ ਗਤੀਸ਼ੀਲ ਰਜਿਸਟਰਡ ਕਲਾਇੰਟ ਲਈ ਉਪਭੋਗਤਾ ਦੀ ਸਹਿਮਤੀ ਲੈਣੇ ਚਾਹੀਦੇ ਹਨ

---

## 1. **ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਅਧਿਕਾਰ ਨਿਯੰਤਰਣ**

### **ਬਾਹਰੀ ਪਹਚਾਣ ਪ੍ਰਦਾਤਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**

**ਮੌਜੂਦਾ MCP ਮਿਆਰ (2025-06-18)** MCP ਸਰਵਰਾਂ ਨੂੰ ਬਾਹਰੀ ਪਹਚਾਣ ਪ੍ਰਦਾਤਿਆਂ ਨੂੰ ਪ੍ਰਮਾਣਿਕਤਾ ਸੌਂਪਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜੋ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਸੁਰੱਖਿਆ ਸੁਧਾਰ ਹੈ:

### **ਬਾਹਰੀ ਪਹਚਾਣ ਪ੍ਰਦਾਤਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**

**ਮੌਜੂਦਾ MCP ਮਿਆਰ (2025-11-25)** MCP ਸਰਵਰਾਂ ਨੂੰ ਬਾਹਰੀ ਪਹਚਾਣ ਪ੍ਰਦਾਤਿਆਂ ਨੂੰ ਪ੍ਰਮਾਣਿਕਤਾ ਸੌਂਪਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜੋ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਸੁਰੱਖਿਆ ਸੁਧਾਰ ਹੈ:

**ਸੁਰੱਖਿਆ ਲਾਭ:**
1. **ਕਸਟਮ ਪ੍ਰਮਾਣਿਕਤਾ ਖ਼ਤਰਿਆਂ ਨੂੰ ਖਤਮ ਕਰਦਾ ਹੈ**: ਕਸਟਮ ਪ੍ਰਮਾਣਿਕਤਾ ਲਾਗੂ ਕਰਨ ਤੋਂ ਬਚ ਕੇ ਜੋਖਮ ਘਟਾਉਂਦਾ ਹੈ  
2. **ਐਂਟਰਪ੍ਰਾਈਜ਼-ਗਰੇਡ ਸੁਰੱਖਿਆ**: ਮਾਈਕ੍ਰੋਸਾਫਟ ਐਂਟਰਾ ID ਵਰਗੇ ਸਥਾਪਿਤ ਪਹਚਾਣ ਪ੍ਰਦਾਤਿਆਂ ਦੀਆਂ ਉੱਚ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਾ ਲਾਭ  
3. **ਕੇਂਦਰੀਕ੍ਰਿਤ ਪਹਚਾਣ ਪ੍ਰਬੰਧਨ**: ਉਪਭੋਗਤਾ ਜੀਵਨਚੱਕਰ ਪ੍ਰਬੰਧਨ, ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਅਤੇ ਅਨੁਕੂਲਤਾ ਆਡੀਟਿੰਗ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦਾ ਹੈ  
4. **ਮਲਟੀ-ਫੈਕਟਰ ਪ੍ਰਮਾਣਿਕਤਾ**: ਐਂਟਰਪ੍ਰਾਈਜ਼ ਪਹਚਾਣ ਪ੍ਰਦਾਤਿਆਂ ਤੋਂ MFA ਸਮਰੱਥਾਵਾਂ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ  
5. **ਸ਼ਰਤੀ ਪਹੁੰਚ ਨੀਤੀਆਂ**: ਜੋਖਮ-ਆਧਾਰਿਤ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਅਤੇ ਅਨੁਕੂਲ ਪ੍ਰਮਾਣਿਕਤਾ ਦਾ ਲਾਭ

**ਲਾਗੂ ਕਰਨ ਦੀਆਂ ਲੋੜਾਂ:**
- **ਟੋਕਨ ਦਰਸ਼ਕ ਪ੍ਰਮਾਣਿਕਤਾ**: ਸਾਰੇ ਟੋਕਨ ਖਾਸ ਤੌਰ 'ਤੇ MCP ਸਰਵਰ ਲਈ ਜਾਰੀ ਕੀਤੇ ਗਏ ਹਨ ਜਾਂ ਨਹੀਂ ਦੀ ਜਾਂਚ ਕਰੋ  
- **ਜਾਰੀ ਕਰਨ ਵਾਲੇ ਦੀ ਜਾਂਚ**: ਟੋਕਨ ਜਾਰੀ ਕਰਨ ਵਾਲਾ ਉਮੀਦ ਕੀਤੇ ਗਏ ਪਹਚਾਣ ਪ੍ਰਦਾਤਾ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਜਾਂ ਨਹੀਂ  
- **ਦਸਤਖਤ ਦੀ ਜਾਂਚ**: ਟੋਕਨ ਦੀ ਅਖੰਡਤਾ ਦੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫਿਕ ਜਾਂਚ  
- **ਮਿਆਦ ਦੀ ਪਾਬੰਦੀ**: ਟੋਕਨ ਦੀ ਮਿਆਦ ਦੀ ਸਖਤ ਪਾਲਣਾ  
- **ਸਕੋਪ ਦੀ ਜਾਂਚ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਟੋਕਨਾਂ ਵਿੱਚ ਮੰਗੇ ਗਏ ਕਾਰਜਾਂ ਲਈ ਉਚਿਤ ਅਧਿਕਾਰ ਹਨ

### **ਅਧਿਕਾਰ ਤਰਕ ਸੁਰੱਖਿਆ**

**ਅਹਿਮ ਨਿਯੰਤਰਣ:**
- **ਵਿਆਪਕ ਅਧਿਕਾਰ ਆਡੀਟ**: ਸਾਰੇ ਅਧਿਕਾਰ ਫੈਸਲੇ ਬਿੰਦੂਆਂ ਦੀ ਨਿਯਮਤ ਸੁਰੱਖਿਆ ਸਮੀਖਿਆ  
- **ਫੇਲ-ਸੇਫ ਡਿਫਾਲਟ**: ਜਦੋਂ ਅਧਿਕਾਰ ਤਰਕ ਸਪਸ਼ਟ ਫੈਸਲਾ ਨਹੀਂ ਕਰ ਸਕਦਾ ਤਾਂ ਪਹੁੰਚ ਨੂੰ ਮਨਾਹੀ ਕਰੋ  
- **ਅਧਿਕਾਰ ਸੀਮਾਵਾਂ**: ਵੱਖ-ਵੱਖ ਅਧਿਕਾਰ ਪੱਧਰਾਂ ਅਤੇ ਸਰੋਤ ਪਹੁੰਚ ਵਿਚ ਸਾਫ਼ ਵੰਡ  
- **ਆਡੀਟ ਲੌਗਿੰਗ**: ਸੁਰੱਖਿਆ ਨਿਗਰਾਨੀ ਲਈ ਸਾਰੇ ਅਧਿਕਾਰ ਫੈਸਲਿਆਂ ਦੀ ਪੂਰੀ ਲੌਗਿੰਗ  
- **ਨਿਯਮਤ ਪਹੁੰਚ ਸਮੀਖਿਆ**: ਉਪਭੋਗਤਾ ਅਧਿਕਾਰਾਂ ਅਤੇ ਅਧਿਕਾਰ ਸੌਂਪਣ ਦੀ ਨਿਯਮਤ ਜਾਂਚ

## 2. **ਟੋਕਨ ਸੁਰੱਖਿਆ ਅਤੇ ਐਂਟੀ-ਪਾਸਥਰੂ ਨਿਯੰਤਰਣ**

### **ਟੋਕਨ ਪਾਸਥਰੂ ਰੋਕਥਾਮ**

**MCP ਅਧਿਕਾਰ ਵਿਸ਼ੇਸ਼ਤਾ ਵਿੱਚ ਟੋਕਨ ਪਾਸਥਰੂ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਮਨਾਹੀ ਹੈ** ਕਿਉਂਕਿ ਇਹ ਗੰਭੀਰ ਸੁਰੱਖਿਆ ਖ਼ਤਰਿਆਂ ਨਾਲ ਜੁੜਿਆ ਹੈ:

**ਸੁਰੱਖਿਆ ਖ਼ਤਰਿਆਂ ਦਾ ਸੰਬੋਧਨ:**
- **ਨਿਯੰਤਰਣ ਚਾਲਾਕੀ**: ਜ਼ਰੂਰੀ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਜਿਵੇਂ ਕਿ ਦਰ ਸੀਮਾ, ਬੇਨਤੀ ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਟ੍ਰੈਫਿਕ ਨਿਗਰਾਨੀ ਨੂੰ ਬਾਈਪਾਸ ਕਰਦਾ ਹੈ  
- **ਜਵਾਬਦੇਹੀ ਟੁੱਟਣਾ**: ਕਲਾਇੰਟ ਪਛਾਣ ਅਸੰਭਵ ਬਣਾਉਂਦਾ ਹੈ, ਆਡੀਟ ਟਰੇਲ ਅਤੇ ਘਟਨਾ ਜਾਂਚ ਨੂੰ ਖਰਾਬ ਕਰਦਾ ਹੈ  
- **ਪ੍ਰਾਕਸੀ-ਆਧਾਰਿਤ ਡਾਟਾ ਚੋਰੀ**: ਮਾਲਿਸ਼ੀਅਸ ਪੱਖੀ ਸਰਵਰਾਂ ਨੂੰ ਅਣਅਧਿਕ੍ਰਿਤ ਡਾਟਾ ਪਹੁੰਚ ਲਈ ਪ੍ਰਾਕਸੀ ਵਜੋਂ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ  
- **ਭਰੋਸਾ ਸੀਮਾ ਉਲੰਘਣਾ**: ਟੋਕਨ ਮੂਲਾਂ ਬਾਰੇ ਡਾਊਨਸਟਰੀਮ ਸੇਵਾ ਭਰੋਸਾ ਅਨੁਮਾਨਾਂ ਨੂੰ ਤੋੜਦਾ ਹੈ  
- **ਲੈਟਰਲ ਮੂਵਮੈਂਟ**: ਕਈ ਸੇਵਾਵਾਂ ਵਿੱਚ ਸਮਝੌਤਾ ਕੀਤੇ ਟੋਕਨ ਵਿਆਪਕ ਹਮਲੇ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ

**ਲਾਗੂ ਕਰਨ ਵਾਲੇ ਨਿਯੰਤਰਣ:**
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

### **ਸੁਰੱਖਿਅਤ ਟੋਕਨ ਪ੍ਰਬੰਧਨ ਪੈਟਰਨ**

**ਸਰਵੋਤਮ ਅਭਿਆਸ:**
- **ਛੋਟੇ ਸਮੇਂ ਵਾਲੇ ਟੋਕਨ**: ਟੋਕਨ ਘੁਮਾਅ ਨਾਲ ਖੁਲਾਸਾ ਸਮਾਂ ਘਟਾਓ  
- **ਜਸਟ-ਇਨ-ਟਾਈਮ ਜਾਰੀਕਰਨ**: ਟੋਕਨ ਸਿਰਫ਼ ਜ਼ਰੂਰਤ ਅਨੁਸਾਰ ਜਾਰੀ ਕਰੋ  
- **ਸੁਰੱਖਿਅਤ ਸਟੋਰੇਜ**: ਹਾਰਡਵੇਅਰ ਸੁਰੱਖਿਆ ਮਾਡਿਊਲ (HSM) ਜਾਂ ਸੁਰੱਖਿਅਤ ਕੀ ਵੌਲਟ ਵਰਤੋ  
- **ਟੋਕਨ ਬਾਈਂਡਿੰਗ**: ਸੰਭਵ ਹੋਵੇ ਤਾਂ ਟੋਕਨਾਂ ਨੂੰ ਖਾਸ ਕਲਾਇੰਟ, ਸੈਸ਼ਨ ਜਾਂ ਕਾਰਜਾਂ ਨਾਲ ਬੰਨ੍ਹੋ  
- **ਨਿਗਰਾਨੀ ਅਤੇ ਚੇਤਾਵਨੀ**: ਟੋਕਨ ਦੀ ਗਲਤ ਵਰਤੋਂ ਜਾਂ ਅਣਅਧਿਕ੍ਰਿਤ ਪਹੁੰਚ ਦੇ ਪੈਟਰਨ ਦੀ ਤੁਰੰਤ ਪਹਿਚਾਣ

## 3. **ਸੈਸ਼ਨ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ**

### **ਸੈਸ਼ਨ ਹਾਈਜੈਕਿੰਗ ਰੋਕਥਾਮ**

**ਹਮਲੇ ਦੇ ਰਸਤੇ:**
- **ਸੈਸ਼ਨ ਹਾਈਜੈਕ ਪ੍ਰਾਂਪਟ ਇੰਜੈਕਸ਼ਨ**: ਸਾਂਝੇ ਸੈਸ਼ਨ ਸਥਿਤੀ ਵਿੱਚ ਮਾਲਿਸ਼ੀਅਸ ਘਟਨਾਵਾਂ ਦਾ ਇੰਜੈਕਸ਼ਨ  
- **ਸੈਸ਼ਨ ਨਕਲਬਾਜ਼ੀ**: ਚੋਰੀ ਹੋਏ ਸੈਸ਼ਨ ID ਦੀ ਬਿਨਾਂ ਅਧਿਕਾਰ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਵਰਤੋਂ  
- **ਰੀਜ਼ਿਊਮੇਬਲ ਸਟ੍ਰੀਮ ਹਮਲੇ**: ਸਰਵਰ-ਭੇਜੇ ਗਏ ਇਵੈਂਟ ਰੀਜ਼ਿਊਮਪਸ਼ਨ ਦੀ ਮਾਲਿਸ਼ੀਅਸ ਸਮੱਗਰੀ ਇੰਜੈਕਸ਼ਨ ਲਈ ਸ਼ੋਸ਼ਣ

**ਲਾਜ਼ਮੀ ਸੈਸ਼ਨ ਨਿਯੰਤਰਣ:**
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

**ਟ੍ਰਾਂਸਪੋਰਟ ਸੁਰੱਖਿਆ:**
- **HTTPS ਲਾਗੂ ਕਰਨਾ**: ਸਾਰੇ ਸੈਸ਼ਨ ਸੰਚਾਰ TLS 1.3 'ਤੇ  
- **ਸੁਰੱਖਿਅਤ ਕੁਕੀ ਗੁਣ**: HttpOnly, Secure, SameSite=Strict  
- **ਸਰਟੀਫਿਕੇਟ ਪਿਨਿੰਗ**: MITM ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਅਹਿਮ ਕਨੈਕਸ਼ਨਾਂ ਲਈ

### **ਸਟੇਟਫੁਲ ਵਿਰੁੱਧ ਸਟੇਟਲੈੱਸ ਵਿਚਾਰ**

**ਸਟੇਟਫੁਲ ਲਾਗੂ ਕਰਨ ਲਈ:**
- ਸਾਂਝਾ ਸੈਸ਼ਨ ਸਥਿਤੀ ਨੂੰ ਇੰਜੈਕਸ਼ਨ ਹਮਲਿਆਂ ਤੋਂ ਵਾਧੂ ਸੁਰੱਖਿਆ ਦੀ ਲੋੜ  
- ਕਿਊ-ਆਧਾਰਿਤ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ ਲਈ ਅਖੰਡਤਾ ਦੀ ਜਾਂਚ  
- ਕਈ ਸਰਵਰ ਇੰਸਟੈਂਸਾਂ ਲਈ ਸੁਰੱਖਿਅਤ ਸੈਸ਼ਨ ਸਥਿਤੀ ਸਿੰਕ੍ਰੋਨਾਈਜ਼ੇਸ਼ਨ

**ਸਟੇਟਲੈੱਸ ਲਾਗੂ ਕਰਨ ਲਈ:**
- JWT ਜਾਂ ਸਮਾਨ ਟੋਕਨ-ਆਧਾਰਿਤ ਸੈਸ਼ਨ ਪ੍ਰਬੰਧਨ  
- ਸੈਸ਼ਨ ਸਥਿਤੀ ਦੀ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫਿਕ ਜਾਂਚ  
- ਘਟਾਇਆ ਹਮਲਾ ਸਤਹ ਪਰ ਮਜ਼ਬੂਤ ਟੋਕਨ ਪ੍ਰਮਾਣਿਕਤਾ ਦੀ ਲੋੜ

## 4. **AI-ਵਿਸ਼ੇਸ਼ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ**

### **ਪ੍ਰਾਂਪਟ ਇੰਜੈਕਸ਼ਨ ਰੋਕਥਾਮ**

**ਮਾਈਕ੍ਰੋਸਾਫਟ ਪ੍ਰਾਂਪਟ ਸ਼ੀਲਡਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ:**
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

**ਲਾਗੂ ਕਰਨ ਵਾਲੇ ਨਿਯੰਤਰਣ:**
- **ਇਨਪੁੱਟ ਸੈਨੀਟਾਈਜ਼ੇਸ਼ਨ**: ਸਾਰੇ ਉਪਭੋਗਤਾ ਇਨਪੁੱਟ ਦੀ ਵਿਸਤ੍ਰਿਤ ਜਾਂਚ ਅਤੇ ਛਾਣ-ਬੀਨ  
- **ਸਮੱਗਰੀ ਸੀਮਾ ਪਰਿਭਾਸ਼ਾ**: ਸਿਸਟਮ ਨਿਰਦੇਸ਼ਾਂ ਅਤੇ ਉਪਭੋਗਤਾ ਸਮੱਗਰੀ ਵਿਚ ਸਾਫ਼ ਵੰਡ  
- **ਨਿਰਦੇਸ਼ ਹਾਇਰਾਰਕੀ**: ਟਕਰਾਅ ਵਾਲੇ ਨਿਰਦੇਸ਼ਾਂ ਲਈ ਠੀਕ ਪ੍ਰਾਥਮਿਕਤਾ ਨਿਯਮ  
- **ਆਉਟਪੁੱਟ ਨਿਗਰਾਨੀ**: ਸੰਭਾਵਿਤ ਹਾਨਿਕਾਰਕ ਜਾਂ ਤਬਦੀਲ ਕੀਤੇ ਗਏ ਨਤੀਜਿਆਂ ਦੀ ਪਹਿਚਾਣ

### **ਟੂਲ ਜਹਿਰਲਾਪਣ ਰੋਕਥਾਮ**

**ਟੂਲ ਸੁਰੱਖਿਆ ਫਰੇਮਵਰਕ:**
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

**ਗਤੀਸ਼ੀਲ ਟੂਲ ਪ੍ਰਬੰਧਨ:**
- **ਮਨਜ਼ੂਰੀ ਕਾਰਜ ਪ੍ਰਵਾਹ**: ਟੂਲ ਬਦਲਾਅ ਲਈ ਖਾਸ ਉਪਭੋਗਤਾ ਸਹਿਮਤੀ  
- **ਰੋਲਬੈਕ ਸਮਰੱਥਾਵਾਂ**: ਪਿਛਲੇ ਟੂਲ ਵਰਜਨਾਂ 'ਤੇ ਵਾਪਸੀ ਦੀ ਸਮਰੱਥਾ  
- **ਬਦਲਾਅ ਆਡੀਟਿੰਗ**: ਟੂਲ ਪਰਿਭਾਸ਼ਾ ਬਦਲਾਅ ਦਾ ਪੂਰਾ ਇਤਿਹਾਸ  
- **ਜੋਖਮ ਮੁਲਾਂਕਣ**: ਟੂਲ ਸੁਰੱਖਿਆ ਅਵਸਥਾ ਦੀ ਸਵੈਚਾਲਿਤ ਮੁਲਾਂਕਣ

## 5. **ਕੰਫਿਊਜ਼ਡ ਡੈਪਟੀ ਹਮਲਾ ਰੋਕਥਾਮ**

### **OAuth ਪ੍ਰਾਕਸੀ ਸੁਰੱਖਿਆ**

**ਹਮਲਾ ਰੋਕਥਾਮ ਨਿਯੰਤਰਣ:**
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

**ਲਾਗੂ ਕਰਨ ਦੀਆਂ ਲੋੜਾਂ:**
- **ਉਪਭੋਗਤਾ ਸਹਿਮਤੀ ਦੀ ਜਾਂਚ**: ਗਤੀਸ਼ੀਲ ਕਲਾਇੰਟ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਲਈ ਕਦੇ ਵੀ ਸਹਿਮਤੀ ਸਕਰੀਨਾਂ ਨੂੰ ਛੱਡੋ ਨਾ  
- **ਰੀਡਾਇਰੈਕਟ URI ਪ੍ਰਮਾਣਿਕਤਾ**: ਰੀਡਾਇਰੈਕਟ ਮੰਜ਼ਿਲਾਂ ਦੀ ਸਖਤ ਵ੍ਹਾਈਟਲਿਸਟ-ਆਧਾਰਿਤ ਜਾਂਚ  
- **ਅਧਿਕਾਰ ਕੋਡ ਸੁਰੱਖਿਆ**: ਛੋਟੇ ਸਮੇਂ ਵਾਲੇ ਕੋਡ ਅਤੇ ਇਕ-ਵਾਰ ਵਰਤੋਂ ਦੀ ਪਾਬੰਦੀ  
- **ਕਲਾਇੰਟ ਪਹਚਾਣ ਪ੍ਰਮਾਣਿਕਤਾ**: ਕਲਾਇੰਟ ਪ੍ਰਮਾਣਪੱਤਰ ਅਤੇ ਮੈਟਾਡੇਟਾ ਦੀ ਮਜ਼ਬੂਤ ਜਾਂਚ

## 6. **ਟੂਲ ਕਾਰਜ ਸੁਰੱਖਿਆ**

### **ਸੈਂਡਬਾਕਸਿੰਗ ਅਤੇ ਅਲੱਗਾਵ**

**ਕੰਟੇਨਰ-ਆਧਾਰਿਤ ਅਲੱਗਾਵ:**
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

**ਪ੍ਰਕਿਰਿਆ ਅਲੱਗਾਵ:**
- **ਵੱਖ-ਵੱਖ ਪ੍ਰਕਿਰਿਆ ਸੰਦਰਭ**: ਹਰ ਟੂਲ ਕਾਰਜ ਨੂੰ ਅਲੱਗ ਪ੍ਰਕਿਰਿਆ ਖੇਤਰ ਵਿੱਚ ਚਲਾਉਣਾ  
- **ਇੰਟਰ-ਪ੍ਰੋਸੈਸ ਕਮਿਊਨੀਕੇਸ਼ਨ**: ਪ੍ਰਮਾਣਿਕਤਾ ਨਾਲ ਸੁਰੱਖਿਅਤ IPC ਮਕੈਨਿਜ਼ਮ  
- **ਪ੍ਰਕਿਰਿਆ ਨਿਗਰਾਨੀ**: ਰਨਟਾਈਮ ਵਿਹਾਰ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਅਸਧਾਰਣਤਾ ਪਹਿਚਾਣ  
- **ਸੰਸਾਧਨ ਲਾਗੂ ਕਰਨਾ**: CPU, ਮੈਮੋਰੀ ਅਤੇ I/O ਕਾਰਜਾਂ 'ਤੇ ਕਠੋਰ ਸੀਮਾਵਾਂ

### **ਘੱਟੋ-ਘੱਟ ਅਧਿਕਾਰ ਲਾਗੂ ਕਰਨਾ**

**ਅਧਿਕਾਰ ਪ੍ਰਬੰਧਨ:**
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

## 7. **ਸਪਲਾਈ ਚੇਨ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ**

### **ਨਿਰਭਰਤਾ ਪ੍ਰਮਾਣਿਕਤਾ**

**ਵਿਆਪਕ ਘਟਕ ਸੁਰੱਖਿਆ:**
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

### **ਲਗਾਤਾਰ ਨਿਗਰਾਨੀ**

**ਸਪਲਾਈ ਚੇਨ ਖ਼ਤਰਾ ਪਹਿਚਾਣ:**
- **ਨਿਰਭਰਤਾ ਸਿਹਤ ਨਿਗਰਾਨੀ**: ਸਾਰੇ ਨਿਰਭਰਤਾਵਾਂ ਦੀ ਸੁਰੱਖਿਆ ਸਮੱਸਿਆਵਾਂ ਲਈ ਲਗਾਤਾਰ ਮੁਲਾਂਕਣ  
- **ਖ਼ਤਰਾ ਬੁੱਧੀ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਉਭਰ ਰਹੇ ਸਪਲਾਈ ਚੇਨ ਖ਼ਤਰਿਆਂ 'ਤੇ ਤੁਰੰਤ ਅੱਪਡੇਟ  
- **ਵਿਹਾਰਕ ਵਿਸ਼ਲੇਸ਼ਣ**: ਬਾਹਰੀ ਘਟਕਾਂ ਵਿੱਚ ਅਸਧਾਰਣ ਵਿਹਾਰ ਦੀ ਪਹਿਚਾਣ  
- **ਸਵੈਚਾਲਿਤ ਪ੍ਰਤੀਕਿਰਿਆ**: ਸਮਝੌਤਾ ਕੀਤੇ ਘਟਕਾਂ ਦੀ ਤੁਰੰਤ ਰੋਕਥਾਮ

## 8. **ਨਿਗਰਾਨੀ ਅਤੇ ਪਹਿਚਾਣ ਨਿਯੰਤਰਣ**

### **ਸੁਰੱਖਿਆ ਜਾਣਕਾਰੀ ਅਤੇ ਘਟਨਾ ਪ੍ਰਬੰਧਨ (SIEM)**

**ਵਿਆਪਕ ਲੌਗਿੰਗ ਰਣਨੀਤੀ:**
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

### **ਤੁਰੰਤ ਖ਼ਤਰਾ ਪਹਿਚਾਣ**

**ਵਿਹਾਰਕ ਵਿਸ਼ਲੇਸ਼ਣ:**
- **ਉਪਭੋਗਤਾ ਵਿਹਾਰ ਵਿਸ਼ਲੇਸ਼ਣ (UBA)**: ਅਸਧਾਰਣ ਉਪਭੋਗਤਾ ਪਹੁੰਚ ਪੈਟਰਨ ਦੀ ਪਹਿਚਾਣ  
- **ਇਕਾਈ ਵਿਹਾਰ ਵਿਸ਼ਲੇਸ਼ਣ (EBA)**: MCP ਸਰਵਰ ਅਤੇ ਟੂਲ ਵਿਹਾਰ ਦੀ ਨਿਗਰਾਨੀ  
- **ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਅਸਧਾਰਣਤਾ ਪਹਿਚਾਣ**: AI-ਚਾਲਿਤ ਸੁਰੱਖਿਆ ਖ਼ਤਰਿਆਂ ਦੀ ਪਹਿਚਾਣ  
- **ਖ਼ਤਰਾ ਬੁੱਧੀ ਸਹਿਯੋਗ**: ਜਾਣੇ-ਪਹਿਚਾਣੇ ਹਮਲੇ ਦੇ ਪੈਟਰਨਾਂ ਨਾਲ ਦੇਖੀਆਂ ਗਈਆਂ ਗਤਿਵਿਧੀਆਂ ਦਾ ਮੇਲ

## 9. **ਘਟਨਾ ਪ੍ਰਤੀਕਿਰਿਆ ਅਤੇ ਪੁਨਰ ਪ੍ਰਾਪਤੀ**

### **ਸਵੈਚਾਲਿਤ ਪ੍ਰਤੀਕਿਰਿਆ ਸਮਰੱਥਾਵਾਂ**

**ਤੁਰੰਤ ਪ੍ਰਤੀਕਿਰਿਆ ਕਾਰਵਾਈਆਂ:**
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

### **ਫੋਰੈਂਸਿਕ ਸਮਰੱਥਾਵਾਂ**

**ਜਾਂਚ ਸਹਾਇਤਾ:**
- **ਆਡੀਟ ਟਰੇਲ ਸੰਰੱਖਣ**: ਅਟੱਲ ਲੌਗਿੰਗ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫਿਕ ਅਖੰਡਤਾ ਨਾਲ  
- **ਸਬੂਤ ਇਕੱਠਾ ਕਰਨਾ**: ਸਬੰਧਤ ਸੁਰੱਖਿਆ ਸਬੂਤਾਂ ਦੀ ਸਵੈਚਾਲਿਤ ਇਕੱਠ  
- **ਟਾਈਮਲਾਈਨ ਪੁਨਰਰਚਨਾ**: ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ ਤੱਕ ਲੈ ਜਾਂਦੇ ਵਿਸਥਾਰਿਤ ਘਟਨਾ ਕ੍ਰਮ  
- **ਪ੍ਰਭਾਵ ਮੁਲਾਂਕਣ**: ਸਮਝੌਤੇ ਦੇ ਪੈਮਾਨੇ ਅਤੇ ਡਾਟਾ ਖੁਲਾਸੇ ਦਾ ਮੁਲਾਂਕਣ

## **ਮੁੱਖ ਸੁਰੱਖਿਆ ਆਰਕੀਟੈਕਚਰ ਸਿਧਾਂਤ**

### **ਗਹਿਰਾਈ ਵਿੱਚ ਰੱਖਿਆ**
- **ਕਈ ਸੁਰੱਖਿਆ ਪਰਤਾਂ**: ਸੁਰੱਖਿਆ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਕੋਈ ਇਕੱਲਾ ਨੁਕਸਾਨ ਬਿੰਦੂ ਨਹੀਂ  
- **ਦੁਹਰਾਏ ਨਿਯੰਤਰਣ**: ਅਹਿਮ ਕਾਰਜਾਂ ਲਈ ਓਵਰਲੈਪਿੰਗ ਸੁਰੱਖਿਆ ਉਪਾਅ  
- **ਫੇਲ-ਸੇਫ ਮਕੈਨਿਜ਼ਮ**: ਜਦੋਂ ਸਿਸਟਮ ਗਲਤੀਆਂ ਜਾਂ ਹਮਲਿਆਂ ਦਾ ਸਾਹਮਣਾ ਕਰਦੇ ਹਨ ਤਾਂ ਸੁਰੱਖਿਅਤ ਡਿਫਾਲਟ

### **ਜ਼ੀਰੋ ਟਰੱਸਟ ਲਾਗੂ ਕਰਨਾ**
- **ਕਦੇ ਭਰੋਸਾ ਨਾ ਕਰੋ, ਹਮੇਸ਼ਾ ਜਾਂਚੋ**: ਸਾਰੇ ਇਕਾਈਆਂ ਅਤੇ ਬੇਨਤੀਆਂ ਦੀ ਲਗਾਤਾਰ ਜਾਂਚ  
- **ਘੱਟੋ-ਘੱਟ ਅਧਿਕਾਰ ਦਾ ਸਿਧਾਂਤ**: ਸਾਰੇ ਘਟਕਾਂ ਲਈ ਘੱਟੋ-ਘੱਟ ਪਹੁੰਚ ਅਧਿਕਾਰ  
- **ਮਾਈਕ੍ਰੋ-ਸੈਗਮੈਂਟੇਸ਼ਨ**: ਨੈੱਟਵਰਕ ਅਤੇ ਪਹੁੰਚ ਨਿਯੰਤਰਣ ਵਿੱਚ ਬਾਰੀਕੀ

### **ਲਗਾਤਾਰ ਸੁਰੱਖਿਆ ਵਿਕਾਸ**
- **ਖ਼ਤਰਾ ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਅਨੁਕੂਲਤਾ**: ਉਭਰ ਰਹੇ ਖ਼ਤਰਿਆਂ ਨੂੰ ਸੰਬੋਧਨ ਕਰਨ ਲਈ ਨਿਯਮਤ ਅੱਪਡੇਟ  
- **ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ**: ਨਿਯੰਤਰਣਾਂ ਦੀ ਲਗਾਤਾਰ ਮੁਲਾਂਕਣ ਅਤੇ ਸੁਧਾਰ  
- **ਵਿਸ਼ੇਸ਼ਤਾ ਅਨੁਕੂਲਤਾ**: ਵਿਕਸਤ ਹੋ ਰਹੇ MCP ਸੁਰੱਖਿਆ ਮਿਆਰਾਂ ਨਾਲ ਸੰਗਤ

---

## **ਲਾਗੂ ਕਰਨ ਵਾਲੇ ਸਰੋਤ**

### **ਅਧਿਕਾਰਕ MCP ਦਸਤਾਵੇਜ਼**
- [MCP ਵਿਸ਼ੇਸ਼ਤਾ (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP ਸੁਰੱਖਿਆ ਸਰਵੋਤਮ ਅਭਿਆਸ](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP ਅਧਿਕਾਰ ਵਿਸ਼ੇਸ਼ਤਾ](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **ਮਾਈਕ੍ਰੋਸਾਫਟ ਸੁਰੱਖਿਆ ਹੱਲ**
- [ਮਾਈਕ੍ਰੋਸਾਫਟ ਪ੍ਰਾਂਪਟ ਸ਼ੀਲਡਸ](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [ਅਜ਼ੂਰ ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub ਐਡਵਾਂਸਡ ਸੁਰੱਖਿਆ](https://github.com/security/advanced-security)
- [ਅਜ਼ੂਰ ਕੀ ਵੌਲਟ](https://learn.microsoft.com/azure/key-vault/)

### **ਸੁਰੱਖਿਆ ਮਿਆਰ**
- [OAuth 2.0 ਸੁਰੱਖਿਆ ਸਰਵੋਤਮ ਅਭਿਆਸ (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਲਈ OWASP ਟੌਪ 10](https://genai.owasp.org/)
- [NIST ਸਾਇਬਰਸੁਰੱਖਿਆ ਫਰੇਮਵਰਕ](https://www.nist.gov/cyberframework)

---

> **ਮਹੱਤਵਪੂਰਨ**: ਇਹ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣ ਮੌਜੂਦਾ MCP ਵਿਸ਼ੇਸ਼ਤਾ (2025-06-18) ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਹਮੇਸ਼ਾ ਨਵੀਨਤਮ [ਅਧਿਕਾਰਕ ਦਸਤਾਵੇਜ਼](https://spec.modelcontextprotocol.io/) ਨਾਲ ਜਾਂਚ ਕਰੋ ਕਿਉਂਕਿ ਮਿਆਰ ਤੇਜ਼ੀ ਨਾਲ ਵਿਕਸਤ ਹੋ ਰਹੇ ਹਨ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->