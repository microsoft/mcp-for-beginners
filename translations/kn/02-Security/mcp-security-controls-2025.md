<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c243c6189393ed7468e470ef2090049",
  "translation_date": "2025-12-11T11:36:44+00:00",
  "source_file": "02-Security/mcp-security-controls-2025.md",
  "language_code": "kn"
}
-->
# MCP ಭದ್ರತಾ ನಿಯಂತ್ರಣಗಳು - ಆಗಸ್ಟ್ 2025 ನವೀಕರಣ

> **ಪ್ರಸ್ತುತ ಮಾನದಂಡ**: ಈ ದಾಖಲೆ [MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/) ಭದ್ರತಾ ಅಗತ್ಯಗಳು ಮತ್ತು ಅಧಿಕೃತ [MCP ಭದ್ರತಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) ಅನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ.

ಮಾದರಿ ಸನ್ನಿವೇಶ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಪರಂಪರাগত ಸಾಫ್ಟ್‌ವೇರ್ ಭದ್ರತೆ ಮತ್ತು AI-ನಿರ್ದಿಷ್ಟ ಬೆದರಿಕೆಗಳನ್ನು ಪರಿಹರಿಸುವ ಸುಧಾರಿತ ಭದ್ರತಾ ನಿಯಂತ್ರಣಗಳೊಂದಿಗೆ ಗಮನಾರ್ಹವಾಗಿ ವೃದ್ಧಿಯಾಗಿದೆ. ಈ ದಾಖಲೆ ಆಗಸ್ಟ್ 2025 ರ ವೇಳೆಗೆ ಸುರಕ್ಷಿತ MCP ಅನುಷ್ಠಾನಗಳಿಗೆ ಸಮಗ್ರ ಭದ್ರತಾ ನಿಯಂತ್ರಣಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

## **ಅನಿವಾರ್ಯ ಭದ್ರತಾ ಅಗತ್ಯಗಳು**

### **MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್‌ನಿಂದ ಪ್ರಮುಖ ನಿಷೇಧಗಳು:**

> **ನಿಷಿದ್ಧ**: MCP ಸರ್ವರ್‌ಗಳು MCP ಸರ್ವರ್‌ಗೆ ಸ್ಪಷ್ಟವಾಗಿ ನೀಡದ ಯಾವುದೇ ಟೋಕನ್‌ಗಳನ್ನು ಸ್ವೀಕರಿಸಬಾರದು  
>
> **ನಿಷೇಧಿಸಲಾಗಿದೆ**: MCP ಸರ್ವರ್‌ಗಳು ಪ್ರಮಾಣೀಕರಣಕ್ಕಾಗಿ ಸೆಷನ್‌ಗಳನ್ನು ಬಳಸಬಾರದು  
>
> **ಅಗತ್ಯವಿದೆ**: MCP ಸರ್ವರ್‌ಗಳು ಪ್ರಾಧಿಕಾರ ಅನುಷ್ಠಾನಗೊಳಿಸುವಾಗ ಎಲ್ಲಾ ಒಳಬರುವ ವಿನಂತಿಗಳನ್ನು ಪರಿಶೀಲಿಸಬೇಕು  
>
> **ಅನಿವಾರ್ಯ**: ಸ್ಥಿರ ಕ್ಲೈಂಟ್ ಐಡಿಗಳನ್ನು ಬಳಸುವ MCP ಪ್ರಾಕ್ಸಿ ಸರ್ವರ್‌ಗಳು ಪ್ರತಿ ಡೈನಾಮಿಕ್ ನೋಂದಾಯಿತ ಕ್ಲೈಂಟ್‌ಗೆ ಬಳಕೆದಾರ ಅನುಮತಿಯನ್ನು ಪಡೆಯಬೇಕು

---

## 1. **ಪ್ರಮಾಣೀಕರಣ ಮತ್ತು ಪ್ರಾಧಿಕಾರ ನಿಯಂತ್ರಣಗಳು**

### **ಬಾಹ್ಯ ಗುರುತಿನ ಒದಗಿಸುವವರ ಏಕೀಕರಣ**

**ಪ್ರಸ್ತುತ MCP ಮಾನದಂಡ (2025-06-18)** MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಬಾಹ್ಯ ಗುರುತಿನ ಒದಗಿಸುವವರಿಗೆ ಪ್ರಮಾಣೀಕರಣವನ್ನು ನಿಯೋಜಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ, ಇದು ಪ್ರಮುಖ ಭದ್ರತಾ ಸುಧಾರಣೆಯಾಗಿದೆ:

### **ಬಾಹ್ಯ ಗುರುತಿನ ಒದಗಿಸುವವರ ಏಕೀಕರಣ**

**ಪ್ರಸ್ತುತ MCP ಮಾನದಂಡ (2025-06-18)** MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಬಾಹ್ಯ ಗುರುತಿನ ಒದಗಿಸುವವರಿಗೆ ಪ್ರಮಾಣೀಕರಣವನ್ನು ನಿಯೋಜಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ, ಇದು ಪ್ರಮುಖ ಭದ್ರತಾ ಸುಧಾರಣೆಯಾಗಿದೆ:

**ಭದ್ರತಾ ಲಾಭಗಳು:**  
1. **ಕಸ್ಟಮ್ ಪ್ರಮಾಣೀಕರಣದ ಅಪಾಯಗಳನ್ನು ನಿವಾರಣೆ ಮಾಡುತ್ತದೆ**: ಕಸ್ಟಮ್ ಪ್ರಮಾಣೀಕರಣ ಅನುಷ್ಠಾನಗಳನ್ನು ತಪ್ಪಿಸುವ ಮೂಲಕ ಭದ್ರತಾ ದುರ್ಬಲತೆಗಳನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ  
2. **ಎಂಟರ್‌ಪ್ರೈಸ್-ಗ್ರೇಡ್ ಭದ್ರತೆ**: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಎಂಟ್ರಾ ID ಮುಂತಾದ ಸ್ಥಾಪಿತ ಗುರುತಿನ ಒದಗಿಸುವವರನ್ನು ಬಳಸುತ್ತದೆ  
3. **ಕೇಂದ್ರಿತ ಗುರುತು ನಿರ್ವಹಣೆ**: ಬಳಕೆದಾರ ಜೀವನಚಕ್ರ ನಿರ್ವಹಣೆ, ಪ್ರವೇಶ ನಿಯಂತ್ರಣ ಮತ್ತು ಅನುಕೂಲತೆ ಪರಿಶೀಲನೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತದೆ  
4. **ಬಹು-ಘಟಕ ಪ್ರಮಾಣೀಕರಣ**: ಎಂಟರ್‌ಪ್ರೈಸ್ ಗುರುತಿನ ಒದಗಿಸುವವರಿಂದ MFA ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಡೆದಿದೆ  
5. **ಶರತಾಧಾರಿತ ಪ್ರವೇಶ ನೀತಿಗಳು**: ಅಪಾಯ ಆಧಾರಿತ ಪ್ರವೇಶ ನಿಯಂತ್ರಣಗಳು ಮತ್ತು ಹೊಂದಾಣಿಕೆಯ ಪ್ರಮಾಣೀಕರಣದಿಂದ ಲಾಭ ಪಡೆಯುತ್ತದೆ

**ಅನುಷ್ಠಾನ ಅಗತ್ಯಗಳು:**  
- **ಟೋಕನ್ ಪ್ರೇಕ್ಷಕ ಪರಿಶೀಲನೆ**: ಎಲ್ಲಾ ಟೋಕನ್‌ಗಳು MCP ಸರ್ವರ್‌ಗೆ ಸ್ಪಷ್ಟವಾಗಿ ನೀಡಲ್ಪಟ್ಟಿರುವುದನ್ನು ಪರಿಶೀಲಿಸಿ  
- **ಜಾರಿಗಾರರ ಪರಿಶೀಲನೆ**: ಟೋಕನ್ ಜಾರಿಗಾರರು ನಿರೀಕ್ಷಿತ ಗುರುತಿನ ಒದಗಿಸುವವರಾಗಿರುವುದನ್ನು ಪರಿಶೀಲಿಸಿ  
- **ಸಹಿ ಪರಿಶೀಲನೆ**: ಟೋಕನ್ ಅಖಂಡತೆಯ ಕ್ರಿಪ್ಟೋಗ್ರಾಫಿಕ್ ಪರಿಶೀಲನೆ  
- **ಕಾಲಹರಣ ಜಾರಿಗೊಳಿಸುವಿಕೆ**: ಟೋಕನ್ ಜೀವನಾವಧಿ ಮಿತಿಗಳನ್ನು ಕಟ್ಟುನಿಟ್ಟಾಗಿ ಜಾರಿಗೊಳಿಸುವಿಕೆ  
- **ವ್ಯಾಪ್ತಿಯ ಪರಿಶೀಲನೆ**: ಟೋಕನ್‌ಗಳು ವಿನಂತಿಸಿದ ಕಾರ್ಯಗಳಿಗೆ ಸೂಕ್ತ ಅನುಮತಿಗಳನ್ನು ಹೊಂದಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ

### **ಪ್ರಾಧಿಕಾರ ತರ್ಕ ಭದ್ರತೆ**

**ಪ್ರಮುಖ ನಿಯಂತ್ರಣಗಳು:**  
- **ಸಮಗ್ರ ಪ್ರಾಧಿಕಾರ ಪರಿಶೀಲನೆಗಳು**: ಎಲ್ಲಾ ಪ್ರಾಧಿಕಾರ ನಿರ್ಣಯ ಬಿಂದುಗಳ ನಿಯಮಿತ ಭದ್ರತಾ ವಿಮರ್ಶೆಗಳು  
- **ಫೇಲ್-ಸೆಫ್ಫ್ ಡೀಫಾಲ್ಟ್‌ಗಳು**: ಪ್ರಾಧಿಕಾರ ತರ್ಕ ಸ್ಪಷ್ಟ ನಿರ್ಣಯ ನೀಡದಿದ್ದಾಗ ಪ್ರವೇಶ ನಿರಾಕರಿಸಿ  
- **ಅನುಮತಿ ಗಡಿಗಳು**: ವಿಭಿನ್ನ привಿಲೇಜ್ ಮಟ್ಟಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲ ಪ್ರವೇಶಗಳ ಸ್ಪಷ್ಟ ವಿಭಜನೆ  
- **ಪರಿಶೀಲನಾ ಲಾಗಿಂಗ್**: ಭದ್ರತಾ ಮೇಲ್ವಿಚಾರಣೆಗೆ ಎಲ್ಲಾ ಪ್ರಾಧಿಕಾರ ನಿರ್ಣಯಗಳ ಸಂಪೂರ್ಣ ಲಾಗಿಂಗ್  
- **ನಿಯಮಿತ ಪ್ರವೇಶ ವಿಮರ್ಶೆಗಳು**: ಬಳಕೆದಾರ ಅನುಮತಿಗಳು ಮತ್ತು привಿಲೇಜ್ ನಿಯೋಜನೆಗಳ ನಿಯಮಿತ ಪರಿಶೀಲನೆ

## 2. **ಟೋಕನ್ ಭದ್ರತೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆ ತಡೆ ನಿಯಂತ್ರಣಗಳು**

### **ಟೋಕನ್ ಪ್ರತಿಕ್ರಿಯೆ ತಡೆ**

**MCP ಪ್ರಾಧಿಕಾರ ಸ್ಪೆಸಿಫಿಕೇಶನ್‌ನಲ್ಲಿ ಟೋಕನ್ ಪ್ರತಿಕ್ರಿಯೆ ಸ್ಪಷ್ಟವಾಗಿ ನಿಷೇಧಿಸಲಾಗಿದೆ** ಕಾರಣವು ಪ್ರಮುಖ ಭದ್ರತಾ ಅಪಾಯಗಳು:

**ನಿರ್ವಹಿಸಲಾದ ಭದ್ರತಾ ಅಪಾಯಗಳು:**  
- **ನಿಯಂತ್ರಣ ತಿರಸ್ಕರಣೆ**: ದರ ಮಿತಿ, ವಿನಂತಿ ಪರಿಶೀಲನೆ ಮತ್ತು ಟ್ರಾಫಿಕ್ ಮೇಲ್ವಿಚಾರಣೆ ಮುಂತಾದ ಅಗತ್ಯ ಭದ್ರತಾ ನಿಯಂತ್ರಣಗಳನ್ನು ಬಿಟ್ಟುಹೋಗುತ್ತದೆ  
- **ಹೆಚ್ಚುವರಿ ಹೊಣೆಗಾರಿಕೆ ನಾಶ**: ಕ್ಲೈಂಟ್ ಗುರುತಿಸುವಿಕೆ ಅಸಾಧ್ಯವಾಗುತ್ತದೆ, ಪರಿಶೀಲನಾ ಟ್ರೇಲ್ಗಳು ಮತ್ತು ಘಟನೆ ತನಿಖೆ ಹಾಳಾಗುತ್ತದೆ  
- **ಪ್ರಾಕ್ಸಿ ಆಧಾರಿತ ಡೇಟಾ ಕಳವು**: ದುಷ್ಟ ವ್ಯಕ್ತಿಗಳು ಸರ್ವರ್‌ಗಳನ್ನು ಅನಧಿಕೃತ ಡೇಟಾ ಪ್ರವೇಶಕ್ಕಾಗಿ ಪ್ರಾಕ್ಸಿಗಳಾಗಿ ಬಳಸಬಹುದು  
- **ನಂಬಿಕೆ ಗಡಿಬಿಡಿ ಉಲ್ಲಂಘನೆಗಳು**: ಟೋಕನ್ ಮೂಲಗಳ ಬಗ್ಗೆ ಕೆಳಗಿನ ಸೇವೆಗಳ ನಂಬಿಕೆ ಊಹೆಗಳನ್ನು ಮುರಿಯುತ್ತದೆ  
- **ಪಾರ್ಶ್ವ ಚಲನೆ**: ಹಲವಾರು ಸೇವೆಗಳ ನಡುವೆ ಹಾಳಾದ ಟೋಕನ್‌ಗಳು ವ್ಯಾಪಕ ದಾಳಿಗೆ ಅವಕಾಶ ನೀಡುತ್ತವೆ

**ಅನುಷ್ಠಾನ ನಿಯಂತ್ರಣಗಳು:**  
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

### **ಭದ್ರ ಟೋಕನ್ ನಿರ್ವಹಣಾ ಮಾದರಿಗಳು**

**ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು:**  
- **ಕಿರು ಅವಧಿಯ ಟೋಕನ್‌ಗಳು**: ಟೋಕನ್ ಬದಲಾವಣೆಯೊಂದಿಗೆ ಬಹುಮಾನಿತ ಪ್ರದರ್ಶನ ವಿಂಡೋವನ್ನು ಕಡಿಮೆ ಮಾಡಿ  
- **ತಕ್ಷಣ ನೀಡುವಿಕೆ**: ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಗಳಿಗೆ ಮಾತ್ರ ಟೋಕನ್‌ಗಳನ್ನು ನೀಡುವುದು  
- **ಭದ್ರ ಸಂಗ್ರಹಣೆ**: ಹಾರ್ಡ್‌ವೇರ್ ಭದ್ರತಾ ಘಟಕಗಳು (HSM) ಅಥವಾ ಭದ್ರ ಕೀ ವಾಲ್ಟ್‌ಗಳನ್ನು ಬಳಸಿ  
- **ಟೋಕನ್ ಬಾಂಧನ**: ಸಾಧ್ಯವಾದರೆ ಟೋಕನ್‌ಗಳನ್ನು ನಿರ್ದಿಷ್ಟ ಕ್ಲೈಂಟ್‌ಗಳು, ಸೆಷನ್‌ಗಳು ಅಥವಾ ಕಾರ್ಯಗಳಿಗೆ ಬಾಂಧಿಸಿ  
- **ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಎಚ್ಚರಿಕೆ**: ಟೋಕನ್ ದುರುಪಯೋಗ ಅಥವಾ ಅನಧಿಕೃತ ಪ್ರವೇಶ ಮಾದರಿಗಳ实时 ಪತ್ತೆ

## 3. **ಸೆಷನ್ ಭದ್ರತಾ ನಿಯಂತ್ರಣಗಳು**

### **ಸೆಷನ್ ಹೈಜ್ಯಾಕಿಂಗ್ ತಡೆ**

**ದಾಳಿಯ ಮಾರ್ಗಗಳು:**  
- **ಸೆಷನ್ ಹೈಜ್ಯಾಕ್ ಪ್ರಾಂಪ್ಟ್ ಇಂಜೆಕ್ಷನ್**: ಹಂಚಿಕೊಂಡ ಸೆಷನ್ ಸ್ಥಿತಿಯಲ್ಲಿ ದುಷ್ಟ ಘಟನೆಗಳನ್ನು ಇಂಜೆಕ್ಟ್ ಮಾಡುವುದು  
- **ಸೆಷನ್ ನಕಲಿ**: ಕಳ್ಳತನಗೊಂಡ ಸೆಷನ್ ID ಗಳನ್ನು ಅನಧಿಕೃತವಾಗಿ ಬಳಸಿಕೊಂಡು ಪ್ರಮಾಣೀಕರಣವನ್ನು ತಪ್ಪಿಸುವುದು  
- **ಮರುಪ್ರಾರಂಭಿಸಬಹುದಾದ ಸ್ಟ್ರೀಮ್ ದಾಳಿಗಳು**: ದುಷ್ಟ ವಿಷಯ ಇಂಜೆಕ್ಷನ್‌ಗಾಗಿ ಸರ್ವರ್-ಕಳುಹಿಸಿದ ಘಟನೆ ಮರುಪ್ರಾರಂಭದ ದುರುಪಯೋಗ

**ಅನಿವಾರ್ಯ ಸೆಷನ್ ನಿಯಂತ್ರಣಗಳು:**  
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

**ಸಂವಹನ ಭದ್ರತೆ:**  
- **HTTPS ಜಾರಿಗೊಳಿಸುವಿಕೆ**: ಎಲ್ಲಾ ಸೆಷನ್ ಸಂವಹನ TLS 1.3 ಮೂಲಕ  
- **ಭದ್ರ ಕುಕೀ ಗುಣಲಕ್ಷಣಗಳು**: HttpOnly, Secure, SameSite=Strict  
- **ಪ್ರಮಾಣಪತ್ರ ಪಿನ್ನಿಂಗ್**: MITM ದಾಳಿಗಳನ್ನು ತಡೆಯಲು ಪ್ರಮುಖ ಸಂಪರ್ಕಗಳಿಗೆ

### **ಸ್ಥಿತಿಗತ ಮತ್ತು ಸ್ಥಿತಿರಹಿತ ಪರಿಗಣನೆಗಳು**

**ಸ್ಥಿತಿಗತ ಅನುಷ್ಠಾನಗಳಿಗೆ:**  
- ಹಂಚಿಕೊಂಡ ಸೆಷನ್ ಸ್ಥಿತಿಗೆ ಇಂಜೆಕ್ಷನ್ ದಾಳಿಗಳ ವಿರುದ್ಧ ಹೆಚ್ಚುವರಿ ರಕ್ಷಣೆ ಅಗತ್ಯ  
- ಕ್ಯೂ ಆಧಾರಿತ ಸೆಷನ್ ನಿರ್ವಹಣೆಗೆ ಅಖಂಡತೆ ಪರಿಶೀಲನೆ ಅಗತ್ಯ  
- ಬಹು ಸರ್ವರ್ ಉದಾಹರಣೆಗಳಿಗೆ ಸುರಕ್ಷಿತ ಸೆಷನ್ ಸ್ಥಿತಿ ಸಮನ್ವಯ ಅಗತ್ಯ

**ಸ್ಥಿತಿರಹಿತ ಅನುಷ್ಠಾನಗಳಿಗೆ:**  
- JWT ಅಥವಾ ಸಮಾನ ಟೋಕನ್ ಆಧಾರಿತ ಸೆಷನ್ ನಿರ್ವಹಣೆ  
- ಸೆಷನ್ ಸ್ಥಿತಿ ಅಖಂಡತೆಯ ಕ್ರಿಪ್ಟೋಗ್ರಾಫಿಕ್ ಪರಿಶೀಲನೆ  
- ಕಡಿಮೆ ದಾಳಿ ವಲಯ ಆದರೆ ಬಲವಾದ ಟೋಕನ್ ಪರಿಶೀಲನೆ ಅಗತ್ಯ

## 4. **AI-ನಿರ್ದಿಷ್ಟ ಭದ್ರತಾ ನಿಯಂತ್ರಣಗಳು**

### **ಪ್ರಾಂಪ್ಟ್ ಇಂಜೆಕ್ಷನ್ ರಕ್ಷಣಾ ಕ್ರಮಗಳು**

**Microsoft ಪ್ರಾಂಪ್ಟ್ ಶೀಲ್ಡ್‌ಗಳ ಏಕೀಕರಣ:**  
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

**ಅನುಷ್ಠಾನ ನಿಯಂತ್ರಣಗಳು:**  
- **ಇನ್ಪುಟ್ ಶುದ್ಧೀಕರಣ**: ಎಲ್ಲಾ ಬಳಕೆದಾರ ಇನ್ಪುಟ್‌ಗಳ ಸಮಗ್ರ ಪರಿಶೀಲನೆ ಮತ್ತು ಫಿಲ್ಟರಿಂಗ್  
- **ವಿಷಯ ಗಡಿಬಿಡಿ ವ್ಯಾಖ್ಯಾನ**: ವ್ಯವಸ್ಥೆ ಸೂಚನೆಗಳು ಮತ್ತು ಬಳಕೆದಾರ ವಿಷಯದ ಸ್ಪಷ್ಟ ವಿಭಜನೆ  
- **ಸೂಚನೆ ಹಿರಾರ್ಕಿ**: ವಿರೋಧಾಭಾಸ ಸೂಚನೆಗಳಿಗೆ ಸರಿಯಾದ ಆದ್ಯತೆ ನಿಯಮಗಳು  
- **ಔಟ್‌ಪುಟ್ ಮೇಲ್ವಿಚಾರಣೆ**: ಹಾನಿಕಾರಕ ಅಥವಾ ಮ್ಯಾನಿಪ್ಯುಲೇಟ್ ಮಾಡಿದ ಔಟ್‌ಪುಟ್‌ಗಳ ಪತ್ತೆ

### **ಟೂಲ್ ವಿಷಕಾರಕ ತಡೆ**

**ಟೂಲ್ ಭದ್ರತಾ ಚಟುವಟಿಕೆ:**  
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

**ಡೈನಾಮಿಕ್ ಟೂಲ್ ನಿರ್ವಹಣೆ:**  
- **ಅನುಮೋದನೆ ಕಾರ್ಯಪ್ರವಾಹಗಳು**: ಟೂಲ್ ಬದಲಾವಣೆಗಳಿಗೆ ಸ್ಪಷ್ಟ ಬಳಕೆದಾರ ಅನುಮತಿ  
- **ರೋಲ್ಬ್ಯಾಕ್ ಸಾಮರ್ಥ್ಯಗಳು**: ಹಿಂದಿನ ಟೂಲ್ ಆವೃತ್ತಿಗಳಿಗೆ ಮರಳುವ ಸಾಮರ್ಥ್ಯ  
- **ಬದಲಾವಣೆ ಪರಿಶೀಲನೆ**: ಟೂಲ್ ವ್ಯಾಖ್ಯಾನ ಬದಲಾವಣೆಗಳ ಸಂಪೂರ್ಣ ಇತಿಹಾಸ  
- **ಅಪಾಯ ಮೌಲ್ಯಮಾಪನ**: ಟೂಲ್ ಭದ್ರತಾ ಸ್ಥಿತಿಗತಿಯ ಸ್ವಯಂಚಾಲಿತ ಮೌಲ್ಯಮಾಪನ

## 5. **ಕನ್ಫ್ಯೂಸ್‌ಡ್ ಡೆಪ್ಯೂ ದಾಳಿ ತಡೆ**

### **OAuth ಪ್ರಾಕ್ಸಿ ಭದ್ರತೆ**

**ದಾಳಿ ತಡೆ ನಿಯಂತ್ರಣಗಳು:**  
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

**ಅನುಷ್ಠಾನ ಅಗತ್ಯಗಳು:**  
- **ಬಳಕೆದಾರ ಅನುಮತಿ ಪರಿಶೀಲನೆ**: ಡೈನಾಮಿಕ್ ಕ್ಲೈಂಟ್ ನೋಂದಣಿಗೆ ಅನುಮತಿ ಪರದೆಗಳನ್ನು ಎಂದಿಗೂ ತಪ್ಪಿಸಬಾರದು  
- **ರೀಡೈರೆಕ್ಟ್ URI ಪರಿಶೀಲನೆ**: ರೀಡೈರೆಕ್ಟ್ ಗಮ್ಯಸ್ಥಾನಗಳ ಕಟ್ಟುನಿಟ್ಟಿನ ಶ್ವೇತಪಟ್ಟಿ ಆಧಾರಿತ ಪರಿಶೀಲನೆ  
- **ಪ್ರಾಧಿಕಾರ ಕೋಡ್ ರಕ್ಷಣಾ ಕ್ರಮಗಳು**: ಸಣ್ಣ ಅವಧಿಯ ಕೋಡ್‌ಗಳು ಮತ್ತು ಏಕಬಾರಿಯ ಜಾರಿಗೊಳಿಸುವಿಕೆ  
- **ಕ್ಲೈಂಟ್ ಗುರುತು ಪರಿಶೀಲನೆ**: ಕ್ಲೈಂಟ್ ಪ್ರಮಾಣಪತ್ರಗಳು ಮತ್ತು ಮೆಟಾಡೇಟಾದ ಬಲವಾದ ಪರಿಶೀಲನೆ

## 6. **ಟೂಲ್ ಕಾರ್ಯಾಚರಣೆ ಭದ್ರತೆ**

### **ಸ್ಯಾಂಡ್‌ಬಾಕ್ಸಿಂಗ್ ಮತ್ತು ವಿಭಜನೆ**

**ಕಂಟೈನರ್ ಆಧಾರಿತ ವಿಭಜನೆ:**  
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

**ಪ್ರಕ್ರಿಯೆ ವಿಭಜನೆ:**  
- **ವಿಭಿನ್ನ ಪ್ರಕ್ರಿಯೆ ಸನ್ನಿವೇಶಗಳು**: ಪ್ರತಿ ಟೂಲ್ ಕಾರ್ಯಾಚರಣೆ ವಿಭಜಿತ ಪ್ರಕ್ರಿಯೆ ವಲಯದಲ್ಲಿ  
- **ಇಂಟರ್-ಪ್ರೊಸೆಸ್ ಸಂವಹನ**: ಪರಿಶೀಲನೆಯೊಂದಿಗೆ ಭದ್ರ IPC ಯಂತ್ರಗಳು  
- **ಪ್ರಕ್ರಿಯೆ ಮೇಲ್ವಿಚಾರಣೆ**: ರನ್‌ಟೈಮ್ ವರ್ತನೆ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ಅನೋಮಲಿ ಪತ್ತೆ  
- **ಸಂಪನ್ಮೂಲ ಜಾರಿಗೊಳಿಸುವಿಕೆ**: CPU, ಮೆಮೊರಿ ಮತ್ತು I/O ಕಾರ್ಯಾಚರಣೆಗಳ ಮೇಲೆ ಕಠಿಣ ಮಿತಿ

### **ಕನಿಷ್ಠ привಿಲೇಜ್ ಅನುಷ್ಠಾನ**

**ಅನುಮತಿ ನಿರ್ವಹಣೆ:**  
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

## 7. **ಸರಬರಾಜು ಸರಪಳಿ ಭದ್ರತಾ ನಿಯಂತ್ರಣಗಳು**

### **ಆಧಾರ ಪರಿಶೀಲನೆ**

**ಸಮಗ್ರ ಘಟಕ ಭದ್ರತೆ:**  
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

### **ನಿರಂತರ ಮೇಲ್ವಿಚಾರಣೆ**

**ಸರಬರಾಜು ಸರಪಳಿ ಬೆದರಿಕೆ ಪತ್ತೆ:**  
- **ಆಧಾರ ಆರೋಗ್ಯ ಮೇಲ್ವಿಚಾರಣೆ**: ಎಲ್ಲಾ ಆಧಾರಗಳ ಭದ್ರತಾ ಸಮಸ್ಯೆಗಳ ನಿರಂತರ ಮೌಲ್ಯಮಾಪನ  
- **ಬೆದರಿಕೆ ಬುದ್ಧಿವಂತಿಕೆ ಏಕೀಕರಣ**: ಉದಯೋನ್ಮುಖ ಸರಬರಾಜು ಸರಪಳಿ ಬೆದರಿಕೆಗಳ实时 ನವೀಕರಣಗಳು  
- **ವರ್ತನೆ ವಿಶ್ಲೇಷಣೆ**: ಬಾಹ್ಯ ಘಟಕಗಳಲ್ಲಿ ಅಸಾಮಾನ್ಯ ವರ್ತನೆ ಪತ್ತೆ  
- **ಸ್ವಯಂಚಾಲಿತ ಪ್ರತಿಕ್ರಿಯೆ**: ಹಾಳಾದ ಘಟಕಗಳ ತಕ್ಷಣದ ನಿಯಂತ್ರಣ

## 8. **ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಪತ್ತೆ ನಿಯಂತ್ರಣಗಳು**

### **ಭದ್ರತಾ ಮಾಹಿತಿ ಮತ್ತು ಘಟನೆ ನಿರ್ವಹಣೆ (SIEM)**

**ಸಮಗ್ರ ಲಾಗಿಂಗ್ ತಂತ್ರ:**  
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

### **实时 ಬೆದರಿಕೆ ಪತ್ತೆ**

**ವರ್ತನೆ ವಿಶ್ಲೇಷಣೆ:**  
- **ಬಳಕೆದಾರ ವರ್ತನೆ ವಿಶ್ಲೇಷಣೆ (UBA)**: ಅಸಾಮಾನ್ಯ ಬಳಕೆದಾರ ಪ್ರವೇಶ ಮಾದರಿಗಳ ಪತ್ತೆ  
- **ಘಟಕ ವರ್ತನೆ ವಿಶ್ಲೇಷಣೆ (EBA)**: MCP ಸರ್ವರ್ ಮತ್ತು ಟೂಲ್ ವರ್ತನೆ ಮೇಲ್ವಿಚಾರಣೆ  
- **ಯಂತ್ರ ಅಧ್ಯಯನ ಅನೋಮಲಿ ಪತ್ತೆ**: AI-ಚಾಲಿತ ಭದ್ರತಾ ಬೆದರಿಕೆ ಗುರುತಿಸುವಿಕೆ  
- **ಬೆದರಿಕೆ ಬುದ್ಧಿವಂತಿಕೆ ಹೊಂದಾಣಿಕೆ**: ತಿಳಿದಿರುವ ದಾಳಿ ಮಾದರಿಗಳ ವಿರುದ್ಧ ಗಮನಿಸಿದ ಚಟುವಟಿಕೆಗಳನ್ನು ಹೊಂದಾಣಿಕೆ

## 9. **ಘಟನೆ ಪ್ರತಿಕ್ರಿಯೆ ಮತ್ತು ಪುನರುತ್ಥಾನ**

### **ಸ್ವಯಂಚಾಲಿತ ಪ್ರತಿಕ್ರಿಯೆ ಸಾಮರ್ಥ್ಯಗಳು**

**ತಕ್ಷಣದ ಪ್ರತಿಕ್ರಿಯೆ ಕ್ರಮಗಳು:**  
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

### **ಫೋರೇನ್ಸಿಕ್ ಸಾಮರ್ಥ್ಯಗಳು**

**ತಪಾಸಣಾ ಬೆಂಬಲ:**  
- **ಪರಿಶೀಲನಾ ಟ್ರೇಲ್ ಸಂರಕ್ಷಣೆ**: ಕ್ರಿಪ್ಟೋಗ್ರಾಫಿಕ್ ಅಖಂಡತೆಯೊಂದಿಗೆ ಅಚಲ ಲಾಗಿಂಗ್  
- **ಸಾಕ್ಷ್ಯ ಸಂಗ್ರಹಣೆ**: ಸಂಬಂಧಿತ ಭದ್ರತಾ ವಸ್ತುಗಳ ಸ್ವಯಂಚಾಲಿತ ಸಂಗ್ರಹಣೆ  
- **ಕಾಲರೇಖೆ ಪುನರ್ ನಿರ್ಮಾಣ**: ಭದ್ರತಾ ಘಟನೆಗಳಿಗೆ ಕಾರಣವಾದ ಘಟನೆಗಳ ವಿವರವಾದ ಕ್ರಮ  
- **ಪ್ರಭಾವ ಮೌಲ್ಯಮಾಪನ**: ಒಪ್ಪಿಗೆಯ ವ್ಯಾಪ್ತಿ ಮತ್ತು ಡೇಟಾ ಬಹಿರ್ಗಮನದ ಮೌಲ್ಯಮಾಪನ

## **ಪ್ರಮುಖ ಭದ್ರತಾ ವಾಸ್ತುಶಿಲ್ಪ ತತ್ವಗಳು**

### **ಆಳವಾದ ರಕ್ಷಣಾ ಕ್ರಮಗಳು**  
- **ಬಹುಭಾಗ ಭದ್ರತಾ ಪದರಗಳು**: ಭದ್ರತಾ ವಾಸ್ತುಶಿಲ್ಪದಲ್ಲಿ ಏಕೈಕ ವೈಫಲ್ಯ ಬಿಂದುವಿಲ್ಲ  
- **ಪುನರಾವರ್ತಿತ ನಿಯಂತ್ರಣಗಳು**: ಪ್ರಮುಖ ಕಾರ್ಯಗಳಿಗೆ ಅತಿರೇಕ ಭದ್ರತಾ ಕ್ರಮಗಳು  
- **ಫೇಲ್-ಸೆಫ್ಫ್ ಯಂತ್ರಗಳು**: ವ್ಯವಸ್ಥೆಗಳು ದೋಷಗಳು ಅಥವಾ ದಾಳಿಗಳನ್ನು ಎದುರಿಸುವಾಗ ಭದ್ರ ಡೀಫಾಲ್ಟ್‌ಗಳು

### **ಶೂನ್ಯ ನಂಬಿಕೆ ಅನುಷ್ಠಾನ**  
- **ಯಾವಾಗಲೂ ನಂಬಬೇಡಿ, ಸದಾ ಪರಿಶೀಲಿಸಿ**: ಎಲ್ಲಾ ಘಟಕಗಳು ಮತ್ತು ವಿನಂತಿಗಳ ನಿರಂತರ ಪರಿಶೀಲನೆ  
- **ಕನಿಷ್ಠ привಿಲೇಜ್ ತತ್ವ**: ಎಲ್ಲಾ ಘಟಕಗಳಿಗೆ ಕನಿಷ್ಠ ಪ್ರವೇಶ ಹಕ್ಕುಗಳು  
- **ಮೈಕ್ರೋ-ವಿಭಾಗೀಕರಣ**: ಸೂಕ್ಷ್ಮ ಜಾಲ ಮತ್ತು ಪ್ರವೇಶ ನಿಯಂತ್ರಣಗಳು

### **ನಿರಂತರ ಭದ್ರತಾ ಅಭಿವೃದ್ಧಿ**  
- **ಬೆದರಿಕೆ ಪರಿಸರಕ್ಕೆ ಹೊಂದಿಕೊಳ್ಳುವುದು**: ಉದಯೋನ್ಮುಖ ಬೆದರಿಕೆಗಳನ್ನು ಪರಿಹರಿಸಲು ನಿಯಮಿತ ನವೀಕರಣಗಳು  
- **ಭದ್ರತಾ ನಿಯಂತ್ರಣ ಪರಿಣಾಮಕಾರಿತ್ವ**: ನಿಯಂತ್ರಣಗಳ ನಿರಂತರ ಮೌಲ್ಯಮಾಪನ ಮತ್ತು ಸುಧಾರಣೆ  
- **ಸ್ಪೆಸಿಫಿಕೇಶನ್ ಅನುಕೂಲತೆ**: ಅಭಿವೃದ್ಧಿಯಾಗುತ್ತಿರುವ MCP ಭದ್ರತಾ ಮಾನದಂಡಗಳಿಗೆ ಹೊಂದಾಣಿಕೆ

---

## **ಅನುಷ್ಠಾನ ಸಂಪನ್ಮೂಲಗಳು**

### **ಅಧಿಕೃತ MCP ಡಾಕ್ಯುಮೆಂಟೇಶನ್**  
- [MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ (2025-

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->