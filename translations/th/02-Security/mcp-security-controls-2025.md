# MCP Security Controls - อัปเดต ธันวาคม 2025

> **มาตรฐานปัจจุบัน**: เอกสารนี้สะท้อนข้อกำหนดความปลอดภัยของ [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) และ [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) อย่างเป็นทางการ

Model Context Protocol (MCP) ได้พัฒนาอย่างมากด้วยการควบคุมความปลอดภัยที่เพิ่มขึ้นซึ่งครอบคลุมทั้งความปลอดภัยซอฟต์แวร์แบบดั้งเดิมและภัยคุกคามเฉพาะ AI เอกสารนี้ให้การควบคุมความปลอดภัยอย่างครบถ้วนสำหรับการใช้งาน MCP อย่างปลอดภัย ณ เดือนธันวาคม 2025

## **ข้อกำหนดความปลอดภัยที่บังคับใช้**

### **ข้อห้ามสำคัญจาก MCP Specification:**

> **ห้าม**: เซิร์ฟเวอร์ MCP **ต้องไม่** รับโทเค็นใด ๆ ที่ไม่ได้ออกโดยชัดเจนสำหรับเซิร์ฟเวอร์ MCP
>
> **ห้าม**: เซิร์ฟเวอร์ MCP **ต้องไม่** ใช้เซสชันสำหรับการพิสูจน์ตัวตน  
>
> **ต้อง**: เซิร์ฟเวอร์ MCP ที่ใช้งานการอนุญาต **ต้อง** ตรวจสอบคำขอขาเข้าทั้งหมด
>
> **บังคับ**: เซิร์ฟเวอร์พร็อกซี MCP ที่ใช้รหัสไคลเอนต์แบบคงที่ **ต้อง** ได้รับความยินยอมจากผู้ใช้สำหรับไคลเอนต์ที่ลงทะเบียนแบบไดนามิกแต่ละครั้ง

---

## 1. **การควบคุมการพิสูจน์ตัวตนและการอนุญาต**

### **การรวมผู้ให้บริการตัวตนภายนอก**

**มาตรฐาน MCP ปัจจุบัน (2025-06-18)** อนุญาตให้เซิร์ฟเวอร์ MCP มอบหมายการพิสูจน์ตัวตนให้กับผู้ให้บริการตัวตนภายนอก ซึ่งเป็นการปรับปรุงความปลอดภัยที่สำคัญ:

### **การรวมผู้ให้บริการตัวตนภายนอก**

**มาตรฐาน MCP ปัจจุบัน (2025-11-25)** อนุญาตให้เซิร์ฟเวอร์ MCP มอบหมายการพิสูจน์ตัวตนให้กับผู้ให้บริการตัวตนภายนอก ซึ่งเป็นการปรับปรุงความปลอดภัยที่สำคัญ:

**ประโยชน์ด้านความปลอดภัย:**
1. **ขจัดความเสี่ยงจากการพิสูจน์ตัวตนแบบกำหนดเอง**: ลดพื้นผิวความเสี่ยงโดยหลีกเลี่ยงการใช้งานการพิสูจน์ตัวตนแบบกำหนดเอง
2. **ความปลอดภัยระดับองค์กร**: ใช้ประโยชน์จากผู้ให้บริการตัวตนที่มีชื่อเสียงเช่น Microsoft Entra ID ที่มีฟีเจอร์ความปลอดภัยขั้นสูง
3. **การจัดการตัวตนแบบรวมศูนย์**: ทำให้ง่ายต่อการจัดการวงจรชีวิตผู้ใช้ การควบคุมการเข้าถึง และการตรวจสอบการปฏิบัติตามข้อกำหนด
4. **การพิสูจน์ตัวตนหลายปัจจัย**: รับความสามารถ MFA จากผู้ให้บริการตัวตนระดับองค์กร
5. **นโยบายการเข้าถึงตามเงื่อนไข**: ได้รับประโยชน์จากการควบคุมการเข้าถึงตามความเสี่ยงและการพิสูจน์ตัวตนแบบปรับตัว

**ข้อกำหนดการใช้งาน:**
- **การตรวจสอบกลุ่มเป้าหมายของโทเค็น**: ตรวจสอบว่าโทเค็นทั้งหมดออกโดยชัดเจนสำหรับเซิร์ฟเวอร์ MCP
- **การตรวจสอบผู้ออกโทเค็น**: ตรวจสอบว่าผู้ที่ออกโทเค็นตรงกับผู้ให้บริการตัวตนที่คาดหวัง
- **การตรวจสอบลายเซ็น**: การตรวจสอบทางคริปโตกราฟีของความสมบูรณ์ของโทเค็น
- **การบังคับใช้วันหมดอายุ**: บังคับใช้อย่างเข้มงวดเกี่ยวกับระยะเวลาของโทเค็น
- **การตรวจสอบขอบเขต**: ตรวจสอบว่าโทเค็นมีสิทธิ์ที่เหมาะสมสำหรับการดำเนินการที่ร้องขอ

### **ความปลอดภัยของตรรกะการอนุญาต**

**การควบคุมสำคัญ:**
- **การตรวจสอบการอนุญาตอย่างครบถ้วน**: ทบทวนความปลอดภัยอย่างสม่ำเสมอในทุกจุดตัดสินใจการอนุญาต
- **ค่าเริ่มต้นที่ปลอดภัย**: ปฏิเสธการเข้าถึงเมื่อไม่สามารถตัดสินใจการอนุญาตได้อย่างชัดเจน
- **ขอบเขตสิทธิ์**: การแยกสิทธิ์และการเข้าถึงทรัพยากรอย่างชัดเจน
- **การบันทึกการตรวจสอบ**: บันทึกการตัดสินใจการอนุญาตทั้งหมดเพื่อการตรวจสอบความปลอดภัย
- **การทบทวนการเข้าถึงเป็นประจำ**: ตรวจสอบสิทธิ์และการมอบหมายสิทธิ์ของผู้ใช้อย่างสม่ำเสมอ

## 2. **ความปลอดภัยของโทเค็น & การควบคุมป้องกันการส่งผ่านโทเค็น**

### **การป้องกันการส่งผ่านโทเค็น**

**การส่งผ่านโทเค็นถูกห้ามอย่างชัดเจน** ใน MCP Authorization Specification เนื่องจากความเสี่ยงด้านความปลอดภัยที่สำคัญ:

**ความเสี่ยงด้านความปลอดภัยที่แก้ไข:**
- **การหลีกเลี่ยงการควบคุม**: ข้ามการควบคุมความปลอดภัยที่จำเป็น เช่น การจำกัดอัตรา การตรวจสอบคำขอ และการตรวจสอบการจราจร
- **การขาดความรับผิดชอบ**: ทำให้ไม่สามารถระบุไคลเอนต์ได้ ส่งผลให้การตรวจสอบและการสืบสวนเหตุการณ์เสียหาย
- **การขโมยข้อมูลผ่านพร็อกซี**: เปิดโอกาสให้ผู้ประสงค์ร้ายใช้เซิร์ฟเวอร์เป็นพร็อกซีเพื่อเข้าถึงข้อมูลโดยไม่ได้รับอนุญาต
- **การละเมิดขอบเขตความเชื่อถือ**: ทำลายสมมติฐานความเชื่อถือของบริการปลายทางเกี่ยวกับแหล่งที่มาของโทเค็น
- **การเคลื่อนที่ในแนวราบ**: โทเค็นที่ถูกโจมตีในหลายบริการช่วยให้การโจมตีขยายวงกว้างขึ้น

**การควบคุมการใช้งาน:**
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

### **รูปแบบการจัดการโทเค็นอย่างปลอดภัย**

**แนวทางปฏิบัติที่ดีที่สุด:**
- **โทเค็นอายุสั้น**: ลดช่วงเวลาที่โทเค็นเปิดเผยด้วยการหมุนเวียนโทเค็นบ่อยครั้ง
- **การออกโทเค็นแบบ Just-in-Time**: ออกโทเค็นเฉพาะเมื่อจำเป็นสำหรับการดำเนินการเฉพาะ
- **การจัดเก็บอย่างปลอดภัย**: ใช้ฮาร์ดแวร์โมดูลความปลอดภัย (HSM) หรือคลังเก็บกุญแจที่ปลอดภัย
- **การผูกโทเค็น**: ผูกโทเค็นกับไคลเอนต์ เซสชัน หรือการดำเนินการเฉพาะเมื่อเป็นไปได้
- **การตรวจสอบและแจ้งเตือน**: ตรวจจับการใช้งานโทเค็นผิดปกติหรือการเข้าถึงโดยไม่ได้รับอนุญาตแบบเรียลไทม์

## 3. **การควบคุมความปลอดภัยของเซสชัน**

### **การป้องกันการแฮ็กเซสชัน**

**ช่องทางการโจมตีที่แก้ไข:**
- **การฉีดคำสั่งแฮ็กเซสชัน**: เหตุการณ์ที่เป็นอันตรายถูกฉีดเข้าไปในสถานะเซสชันที่ใช้ร่วมกัน
- **การแอบอ้างเซสชัน**: การใช้ ID เซสชันที่ถูกขโมยโดยไม่ได้รับอนุญาตเพื่อข้ามการพิสูจน์ตัวตน
- **การโจมตีสตรีมที่สามารถต่อเนื่องได้**: การใช้ประโยชน์จากการส่งเหตุการณ์ที่เซิร์ฟเวอร์ส่งต่อเนื่องเพื่อฉีดเนื้อหาที่เป็นอันตราย

**การควบคุมเซสชันที่บังคับใช้:**
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

**ความปลอดภัยของการส่งข้อมูล:**
- **บังคับใช้ HTTPS**: การสื่อสารเซสชันทั้งหมดผ่าน TLS 1.3
- **คุณสมบัติของคุกกี้ที่ปลอดภัย**: HttpOnly, Secure, SameSite=Strict
- **การตรึงใบรับรอง**: สำหรับการเชื่อมต่อที่สำคัญเพื่อป้องกันการโจมตี MITM

### **ข้อพิจารณา Stateful กับ Stateless**

**สำหรับการใช้งานแบบ Stateful:**
- สถานะเซสชันที่ใช้ร่วมกันต้องการการป้องกันเพิ่มเติมจากการโจมตีแบบฉีด
- การจัดการเซสชันแบบคิวต้องมีการตรวจสอบความสมบูรณ์
- เซิร์ฟเวอร์หลายตัวต้องมีการซิงโครไนซ์สถานะเซสชันอย่างปลอดภัย

**สำหรับการใช้งานแบบ Stateless:**
- การจัดการเซสชันโดยใช้ JWT หรือโทเค็นที่คล้ายกัน
- การตรวจสอบความสมบูรณ์ของสถานะเซสชันด้วยคริปโตกราฟี
- ลดพื้นผิวการโจมตีแต่ต้องการการตรวจสอบโทเค็นที่เข้มงวด

## 4. **การควบคุมความปลอดภัยเฉพาะ AI**

### **การป้องกันการฉีดคำสั่ง**

**การรวม Microsoft Prompt Shields:**
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

**การควบคุมการใช้งาน:**
- **การกรองข้อมูลนำเข้า**: การตรวจสอบและกรองข้อมูลนำเข้าของผู้ใช้อย่างครอบคลุม
- **การกำหนดขอบเขตเนื้อหา**: การแยกชัดเจนระหว่างคำสั่งระบบและเนื้อหาผู้ใช้
- **ลำดับชั้นคำสั่ง**: กฎลำดับความสำคัญที่เหมาะสมสำหรับคำสั่งที่ขัดแย้งกัน
- **การตรวจสอบผลลัพธ์**: การตรวจจับผลลัพธ์ที่อาจเป็นอันตรายหรือถูกปรับแต่ง

### **การป้องกันการวางยาพิษเครื่องมือ**

**กรอบความปลอดภัยของเครื่องมือ:**
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

**การจัดการเครื่องมือแบบไดนามิก:**
- **เวิร์กโฟลว์การอนุมัติ**: ได้รับความยินยอมจากผู้ใช้อย่างชัดเจนสำหรับการแก้ไขเครื่องมือ
- **ความสามารถในการย้อนกลับ**: สามารถย้อนกลับไปยังเวอร์ชันเครื่องมือก่อนหน้าได้
- **การตรวจสอบการเปลี่ยนแปลง**: บันทึกประวัติการแก้ไขนิยามเครื่องมืออย่างครบถ้วน
- **การประเมินความเสี่ยง**: การประเมินสถานะความปลอดภัยของเครื่องมือโดยอัตโนมัติ

## 5. **การป้องกันการโจมตี Confused Deputy**

### **ความปลอดภัยพร็อกซี OAuth**

**การควบคุมป้องกันการโจมตี:**
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

**ข้อกำหนดการใช้งาน:**
- **การตรวจสอบความยินยอมของผู้ใช้**: ห้ามข้ามหน้าจอความยินยอมสำหรับการลงทะเบียนไคลเอนต์แบบไดนามิก
- **การตรวจสอบ URI การเปลี่ยนเส้นทาง**: ตรวจสอบอย่างเข้มงวดโดยใช้รายการขาวของปลายทางการเปลี่ยนเส้นทาง
- **การป้องกันรหัสอนุญาต**: รหัสที่มีอายุสั้นและบังคับใช้การใช้ครั้งเดียว
- **การตรวจสอบตัวตนไคลเอนต์**: การตรวจสอบข้อมูลประจำตัวและเมตาดาต้าไคลเอนต์อย่างเข้มงวด

## 6. **ความปลอดภัยในการดำเนินการเครื่องมือ**

### **การแยกและแซนด์บ็อกซ์**

**การแยกด้วยคอนเทนเนอร์:**
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

**การแยกกระบวนการ:**
- **บริบทกระบวนการแยกต่างหาก**: การดำเนินการเครื่องมือแต่ละรายการในพื้นที่กระบวนการที่แยกจากกัน
- **การสื่อสารระหว่างกระบวนการ**: กลไก IPC ที่ปลอดภัยพร้อมการตรวจสอบ
- **การตรวจสอบกระบวนการ**: การวิเคราะห์พฤติกรรมขณะรันไทม์และการตรวจจับความผิดปกติ
- **การบังคับใช้ทรัพยากร**: จำกัดการใช้ CPU, หน่วยความจำ และ I/O อย่างเข้มงวด

### **การใช้งานสิทธิ์น้อยที่สุด**

**การจัดการสิทธิ์:**
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

## 7. **การควบคุมความปลอดภัยห่วงโซ่อุปทาน**

### **การตรวจสอบความถูกต้องของการพึ่งพา**

**ความปลอดภัยของส่วนประกอบอย่างครบถ้วน:**
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

### **การตรวจสอบอย่างต่อเนื่อง**

**การตรวจจับภัยคุกคามห่วงโซ่อุปทาน:**
- **การตรวจสอบสุขภาพของการพึ่งพา**: การประเมินอย่างต่อเนื่องของการพึ่งพาทั้งหมดเพื่อหาปัญหาด้านความปลอดภัย
- **การรวมข่าวกรองภัยคุกคาม**: อัปเดตแบบเรียลไทม์เกี่ยวกับภัยคุกคามห่วงโซ่อุปทานที่เกิดขึ้นใหม่
- **การวิเคราะห์พฤติกรรม**: ตรวจจับพฤติกรรมผิดปกติในส่วนประกอบภายนอก
- **การตอบสนองอัตโนมัติ**: การกักกันส่วนประกอบที่ถูกโจมตีทันที

## 8. **การควบคุมการตรวจสอบและการตรวจจับ**

### **ระบบจัดการข้อมูลและเหตุการณ์ความปลอดภัย (SIEM)**

**กลยุทธ์การบันทึกอย่างครบถ้วน:**
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

### **การตรวจจับภัยคุกคามแบบเรียลไทม์**

**การวิเคราะห์พฤติกรรม:**
- **การวิเคราะห์พฤติกรรมผู้ใช้ (UBA)**: ตรวจจับรูปแบบการเข้าถึงผู้ใช้ที่ผิดปกติ
- **การวิเคราะห์พฤติกรรมหน่วยงาน (EBA)**: ตรวจสอบพฤติกรรมของเซิร์ฟเวอร์ MCP และเครื่องมือ
- **การตรวจจับความผิดปกติด้วยแมชชีนเลิร์นนิง**: การระบุภัยคุกคามความปลอดภัยด้วย AI
- **การเชื่อมโยงข่าวกรองภัยคุกคาม**: การจับคู่กิจกรรมที่สังเกตได้กับรูปแบบการโจมตีที่รู้จัก

## 9. **การตอบสนองและการกู้คืนเหตุการณ์**

### **ความสามารถในการตอบสนองอัตโนมัติ**

**การดำเนินการตอบสนองทันที:**
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

### **ความสามารถด้านนิติเวช**

**การสนับสนุนการสืบสวน:**
- **การเก็บรักษาเส้นทางตรวจสอบ**: การบันทึกที่ไม่เปลี่ยนแปลงพร้อมความสมบูรณ์ทางคริปโตกราฟี
- **การเก็บรวบรวมหลักฐาน**: การรวบรวมอัตโนมัติของหลักฐานความปลอดภัยที่เกี่ยวข้อง
- **การสร้างลำดับเหตุการณ์**: ลำดับเหตุการณ์อย่างละเอียดที่นำไปสู่เหตุการณ์ความปลอดภัย
- **การประเมินผลกระทบ**: การประเมินขอบเขตการถูกโจมตีและการเปิดเผยข้อมูล

## **หลักการสำคัญของสถาปัตยกรรมความปลอดภัย**

### **การป้องกันเชิงลึก**
- **หลายชั้นของความปลอดภัย**: ไม่มีจุดล้มเหลวเดียวในสถาปัตยกรรมความปลอดภัย
- **การควบคุมซ้ำซ้อน**: มาตรการความปลอดภัยที่ทับซ้อนสำหรับฟังก์ชันที่สำคัญ
- **กลไกความปลอดภัยเริ่มต้น**: ค่าเริ่มต้นที่ปลอดภัยเมื่อระบบพบข้อผิดพลาดหรือการโจมตี

### **การใช้งาน Zero Trust**
- **ไม่เชื่อใจใคร ตรวจสอบตลอดเวลา**: การตรวจสอบอย่างต่อเนื่องของทุกหน่วยงานและคำขอ
- **หลักการสิทธิ์น้อยที่สุด**: สิทธิ์การเข้าถึงขั้นต่ำสำหรับทุกส่วนประกอบ
- **การแบ่งส่วนเครือข่ายอย่างละเอียด**: การควบคุมเครือข่ายและการเข้าถึงอย่างละเอียด

### **วิวัฒนาการความปลอดภัยอย่างต่อเนื่อง**
- **การปรับตัวต่อภูมิทัศน์ภัยคุกคาม**: การอัปเดตเป็นประจำเพื่อจัดการกับภัยคุกคามที่เกิดขึ้นใหม่
- **ประสิทธิภาพของการควบคุมความปลอดภัย**: การประเมินและปรับปรุงการควบคุมอย่างต่อเนื่อง
- **การปฏิบัติตามข้อกำหนด**: การสอดคล้องกับมาตรฐานความปลอดภัย MCP ที่พัฒนาอย่างต่อเนื่อง

---

## **ทรัพยากรสำหรับการใช้งาน**

### **เอกสาร MCP อย่างเป็นทางการ**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **โซลูชันความปลอดภัยของ Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **มาตรฐานความปลอดภัย**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **สำคัญ**: การควบคุมความปลอดภัยเหล่านี้สะท้อนข้อกำหนด MCP ปัจจุบัน (2025-06-18) โปรดตรวจสอบกับ [เอกสารอย่างเป็นทางการ](https://spec.modelcontextprotocol.io/) ล่าสุดเสมอเนื่องจากมาตรฐานมีการพัฒนาอย่างรวดเร็ว

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->