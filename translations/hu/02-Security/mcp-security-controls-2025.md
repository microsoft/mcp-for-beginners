# MCP Biztonsági Intézkedések - 2025 Decemberi Frissítés

> **Jelenlegi Szabvány**: Ez a dokumentum tükrözi a [MCP Specifikáció 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) biztonsági követelményeit és a hivatalos [MCP Biztonsági Legjobb Gyakorlatokat](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

A Model Context Protocol (MCP) jelentősen érett, fejlett biztonsági intézkedésekkel, amelyek mind a hagyományos szoftverbiztonsági, mind az AI-specifikus fenyegetéseket kezelik. Ez a dokumentum átfogó biztonsági intézkedéseket nyújt a biztonságos MCP megvalósításokhoz 2025 decemberétől.

## **KÖTELEZŐ Biztonsági Követelmények**

### **Kritikus Tiltások az MCP Specifikációból:**

> **TILOS**: Az MCP szerverek **NEM FOGADHATNAK EL** olyan tokeneket, amelyeket nem kifejezetten az MCP szerver számára bocsátottak ki  
>
> **TILOS**: Az MCP szerverek **NEM HASZNÁLHATNAK** munkameneteket hitelesítésre  
>
> **KÖTELEZŐ**: Az MCP szerverek, amelyek jogosultságkezelést valósítanak meg, **MINDEN** bejövő kérést ellenőrizniük kell  
>
> **KÖTELEZŐ**: Az MCP proxy szerverek, amelyek statikus kliensazonosítókat használnak, **MINDEN** dinamikusan regisztrált kliens esetén kötelesek felhasználói hozzájárulást kérni

---

## 1. **Hitelesítés és Jogosultságkezelés Intézkedések**

### **Külső Identitásszolgáltató Integráció**

**Jelenlegi MCP Szabvány (2025-06-18)** lehetővé teszi, hogy az MCP szerverek a hitelesítést külső identitásszolgáltatókra bízzák, ami jelentős biztonsági előrelépést jelent:

### **Külső Identitásszolgáltató Integráció**

**Jelenlegi MCP Szabvány (2025-11-25)** lehetővé teszi, hogy az MCP szerverek a hitelesítést külső identitásszolgáltatókra bízzák, ami jelentős biztonsági előrelépést jelent:

**Biztonsági Előnyök:**
1. **Egyedi Hitelesítési Kockázatok Kiküszöbölése**: Csökkenti a sebezhetőségi felületet az egyedi hitelesítési megvalósítások elkerülésével  
2. **Vállalati Szintű Biztonság**: Kihasználja az olyan bevált identitásszolgáltatókat, mint a Microsoft Entra ID fejlett biztonsági funkciókkal  
3. **Központosított Identitáskezelés**: Egyszerűsíti a felhasználói életciklus-kezelést, hozzáférés-ellenőrzést és megfelelőségi auditokat  
4. **Többlépcsős Hitelesítés**: Örökli a vállalati identitásszolgáltatók MFA képességeit  
5. **Feltételes Hozzáférési Szabályok**: Használja a kockázatalapú hozzáférés-ellenőrzést és adaptív hitelesítést

**Megvalósítási Követelmények:**
- **Token Célközönség Ellenőrzése**: Ellenőrizni kell, hogy minden token kifejezetten az MCP szerver számára lett kiadva  
- **Kibocsátó Ellenőrzése**: Érvényesíteni kell, hogy a token kibocsátója megfelel az elvárt identitásszolgáltatónak  
- **Aláírás Ellenőrzése**: Kriptográfiai ellenőrzés a token integritására  
- **Lejárat Betartása**: Szigorú betartása a token élettartamának  
- **Jogosultság Ellenőrzése**: Biztosítani kell, hogy a tokenek megfelelő jogosultságokat tartalmazzanak a kért műveletekhez

### **Jogosultságkezelési Logika Biztonsága**

**Kritikus Intézkedések:**
- **Átfogó Jogosultság Auditok**: Rendszeres biztonsági felülvizsgálatok minden jogosultság döntési ponton  
- **Biztonságos Alapértelmezések**: Hozzáférés megtagadása, ha a jogosultság logika nem tud egyértelmű döntést hozni  
- **Jogosultsági Határok**: Egyértelmű elkülönítés a különböző jogosultsági szintek és erőforrás-hozzáférések között  
- **Audit Naplózás**: Minden jogosultsági döntés teljes körű naplózása a biztonsági megfigyeléshez  
- **Rendszeres Hozzáférés Felülvizsgálatok**: Időszakos felülvizsgálat a felhasználói jogosultságokról és privilégiumokról

## 2. **Token Biztonság és Anti-Passthrough Intézkedések**

### **Token Passthrough Megelőzése**

**A token passthrough kifejezetten tilos** az MCP Jogosultságkezelési Specifikációban kritikus biztonsági kockázatok miatt:

**Kezelt Biztonsági Kockázatok:**
- **Ellenőrzés Megkerülése**: Megkerüli az alapvető biztonsági intézkedéseket, mint a sebességkorlátozás, kérés-ellenőrzés és forgalomfigyelés  
- **Felelősség Megszűnése**: Megakadályozza az ügyfél azonosítását, rontva az audit nyomvonalakat és eseményvizsgálatot  
- **Proxy-alapú Kiszivárogtatás**: Lehetővé teszi rosszindulatú szereplők számára, hogy szervereket használjanak jogosulatlan adat-hozzáféréshez  
- **Bizalmi Határ Áthágása**: Megsérti az alárendelt szolgáltatások token eredetére vonatkozó bizalmi feltételezéseit  
- **Oldalirányú Mozgás**: Több szolgáltatás között kompromittált tokenek szélesebb körű támadási teret biztosítanak

**Megvalósítási Intézkedések:**
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

### **Biztonságos Token Kezelési Minták**

**Legjobb Gyakorlatok:**
- **Rövid Élettartamú Tokenek**: Minimalizálja a kitettségi időt gyakori token forgatással  
- **Just-in-Time Kiadás**: Csak a szükséges műveletekhez ad ki tokeneket  
- **Biztonságos Tárolás**: Hardveres biztonsági modulok (HSM) vagy biztonságos kulcstárolók használata  
- **Token Kötés**: Lehetőség szerint köti a tokeneket adott klienshez, munkamenethez vagy művelethez  
- **Figyelés és Riasztás**: Valós idejű észlelés a token visszaélések vagy jogosulatlan hozzáférési minták esetén

## 3. **Munkamenet Biztonsági Intézkedések**

### **Munkamenet Átirányítás Megelőzése**

**Kezelt Támadási Vektorok:**
- **Munkamenet Átirányítás Prompt Befecskendezés**: Rosszindulatú események befecskendezése megosztott munkamenet állapotba  
- **Munkamenet Személyesítés**: Jogosulatlan lopott munkamenet azonosítók használata hitelesítés megkerülésére  
- **Folytatható Stream Támadások**: Szerver által küldött események folytatásának kihasználása rosszindulatú tartalom befecskendezésére

**Kötelező Munkamenet Intézkedések:**
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

**Átvitel Biztonság:**
- **HTTPS Kötelező Használata**: Minden munkamenet kommunikáció TLS 1.3-on keresztül  
- **Biztonságos Süti Attribútumok**: HttpOnly, Secure, SameSite=Strict  
- **Tanúsítvány Rögzítés**: Kritikus kapcsolatok esetén a MITM támadások megelőzésére

### **Állapotfüggő vs Állapotmentes Megfontolások**

**Állapotfüggő Megvalósításokhoz:**
- Megosztott munkamenet állapot további védelemre szorul befecskendezés elleni támadásokkal szemben  
- Sor alapú munkamenet-kezelés integritás ellenőrzést igényel  
- Több szerver példány esetén biztonságos munkamenet állapot szinkronizáció szükséges

**Állapotmentes Megvalósításokhoz:**
- JWT vagy hasonló token alapú munkamenet-kezelés  
- Kriptográfiai ellenőrzés a munkamenet állapot integritására  
- Csökkentett támadási felület, de robusztus token érvényesítést igényel

## 4. **AI-Specifikus Biztonsági Intézkedések**

### **Prompt Befecskendezés Védelem**

**Microsoft Prompt Shields Integráció:**
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

**Megvalósítási Intézkedések:**
- **Bemenet Tisztítás**: Minden felhasználói bemenet átfogó ellenőrzése és szűrése  
- **Tartalom Határ Meghatározása**: Egyértelmű elkülönítés a rendszer utasítások és a felhasználói tartalom között  
- **Utasítás Hierarchia**: Megfelelő elsőbbségi szabályok az ellentmondó utasítások esetén  
- **Kimenet Figyelés**: Potenciálisan káros vagy manipulált kimenetek észlelése

### **Eszköz Mérgezés Megelőzése**

**Eszköz Biztonsági Keretrendszer:**
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

**Dinamikus Eszközkezelés:**
- **Jóváhagyási Munkafolyamatok**: Kifejezett felhasználói hozzájárulás az eszköz módosításokhoz  
- **Visszaállítási Képességek**: Lehetőség korábbi eszközverziókra való visszatérésre  
- **Változás Auditálás**: Az eszközdefiníció módosításainak teljes története  
- **Kockázatértékelés**: Automatikus eszközbiztonsági állapot értékelés

## 5. **Confused Deputy Támadás Megelőzése**

### **OAuth Proxy Biztonság**

**Támadás Megelőzési Intézkedések:**
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

**Megvalósítási Követelmények:**
- **Felhasználói Hozzájárulás Ellenőrzése**: Soha ne hagyja ki a hozzájárulási képernyőket dinamikus kliens regisztrációnál  
- **Redirect URI Ellenőrzés**: Szigorú fehérlista alapú átirányítási célok ellenőrzése  
- **Engedélyezési Kód Védelem**: Rövid élettartamú, egyszer használatos kódok  
- **Kliensazonosító Ellenőrzés**: Robusztus klienskredenciális és metaadat érvényesítés

## 6. **Eszköz Végrehajtási Biztonság**

### **Sandboxing és Izoláció**

**Konténer-alapú Izoláció:**
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

**Folyamat Izoláció:**
- **Külön Folyamat Kontextusok**: Minden eszköz végrehajtása izolált folyamat térben  
- **Folyamatok Közötti Kommunikáció**: Biztonságos IPC mechanizmusok ellenőrzéssel  
- **Folyamat Megfigyelés**: Futásidejű viselkedéselemzés és anomália észlelés  
- **Erőforrás Korlátozás**: Kemény korlátok CPU, memória és I/O műveletekre

### **Legkisebb Jogosultság Elve**

**Jogosultságkezelés:**
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

## 7. **Ellátási Lánc Biztonsági Intézkedések**

### **Függőség Ellenőrzés**

**Átfogó Komponens Biztonság:**
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

### **Folyamatos Megfigyelés**

**Ellátási Lánc Fenyegetés Észlelés:**
- **Függőség Egészség Monitorozás**: Minden függőség folyamatos értékelése biztonsági problémák szempontjából  
- **Fenyegetés Intelligencia Integráció**: Valós idejű frissítések az újonnan felmerülő ellátási lánc fenyegetésekről  
- **Viselkedéselemzés**: Szokatlan viselkedés észlelése külső komponensekben  
- **Automatizált Válasz**: Azonnali intézkedés a kompromittált komponensek elszigetelésére

## 8. **Megfigyelés és Észlelés Intézkedések**

### **Biztonsági Információ és Eseménykezelés (SIEM)**

**Átfogó Naplózási Stratégia:**
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

### **Valós Idejű Fenyegetés Észlelés**

**Viselkedéselemzés:**
- **Felhasználói Viselkedés Elemzés (UBA)**: Szokatlan felhasználói hozzáférési minták észlelése  
- **Entitás Viselkedés Elemzés (EBA)**: MCP szerver és eszköz viselkedésének monitorozása  
- **Gépi Tanulás Anomália Észlelés**: AI-alapú biztonsági fenyegetések azonosítása  
- **Fenyegetés Intelligencia Korreláció**: Megfigyelt tevékenységek összevetése ismert támadási mintákkal

## 9. **Eseménykezelés és Helyreállítás**

### **Automatizált Válasz Képességek**

**Azonnali Válasz Intézkedések:**
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

### **Forenzikus Képességek**

**Vizsgálati Támogatás:**
- **Audit Nyomvonal Megőrzése**: Megmásíthatatlan naplózás kriptográfiai integritással  
- **Bizonyítékgyűjtés**: Automatikus releváns biztonsági anyagok gyűjtése  
- **Idővonal Újjáépítés**: Részletes eseménysorozat a biztonsági incidensekhez  
- **Hatásértékelés**: A kompromittálás mértékének és adatkitettségnek értékelése

## **Kulcsfontosságú Biztonsági Architektúra Elvek**

### **Mélységi Védelem**
- **Többszörös Biztonsági Rétegek**: Nincs egyetlen hibapont a biztonsági architektúrában  
- **Tartalék Intézkedések**: Átfedő biztonsági megoldások kritikus funkciókhoz  
- **Biztonságos Alapértelmezések**: Biztonságos alapbeállítások hibák vagy támadások esetén

### **Zero Trust Megvalósítás**
- **Sose Bízz Meg, Mindig Ellenőrizz**: Folyamatos érvényesítés minden entitás és kérés esetén  
- **Legkisebb Jogosultság Elve**: Minimális hozzáférési jogok minden komponens számára  
- **Mikro-szegmentáció**: Részletes hálózati és hozzáférés-ellenőrzések

### **Folyamatos Biztonsági Fejlődés**
- **Fenyegetési Környezethez Alkalmazkodás**: Rendszeres frissítések az új fenyegetések kezelésére  
- **Biztonsági Intézkedések Hatékonysága**: Folyamatos értékelés és fejlesztés  
- **Specifikáció Megfelelés**: Az MCP biztonsági szabványok folyamatos követése

---

## **Megvalósítási Források**

### **Hivatalos MCP Dokumentáció**
- [MCP Specifikáció (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Biztonsági Legjobb Gyakorlatok](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Jogosultságkezelési Specifikáció](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Biztonsági Megoldások**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Biztonsági Szabványok**
- [OAuth 2.0 Biztonsági Legjobb Gyakorlatok (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Nagy Nyelvi Modellekhez](https://genai.owasp.org/)
- [NIST Kiberbiztonsági Keretrendszer](https://www.nist.gov/cyberframework)

---

> **Fontos**: Ezek a biztonsági intézkedések a jelenlegi MCP specifikációt tükrözik (2025-06-18). Mindig ellenőrizze a legfrissebb [hivatalos dokumentációt](https://spec.modelcontextprotocol.io/), mivel a szabványok gyorsan fejlődnek.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->