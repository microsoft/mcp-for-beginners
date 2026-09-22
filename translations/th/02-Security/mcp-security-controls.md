# การควบคุมความปลอดภัย MCP - อัปเดตเดือนกันยายน 2026

> **มาตรฐานปัจจุบัน:** เอกสารนี้สะท้อน
> [ข้อกำหนด MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> และอย่างเป็นทางการ
> [แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

โปรโตคอลบริบทแบบจำลอง (MCP) ได้เจริญเติบโตอย่างมากพร้อมกับการควบคุมความปลอดภัยที่เพิ่มขึ้นซึ่งครอบคลุมทั้งความปลอดภัยซอฟต์แวร์แบบดั้งเดิมและภัยคุกคามเฉพาะด้าน AI เอกสารนี้ให้การควบคุมความปลอดภัยแบบครบถ้วนสำหรับการใช้งาน MCP อย่างปลอดภัยโดยสอดคล้องกับกรอบ OWASP MCP Top 10

## 🏔️ การฝึกอบรมความปลอดภัยแบบปฏิบัติจริง

สำหรับประสบการณ์การใช้งานความปลอดภัยแบบปฏิบัติจริง เราขอแนะนำ **[เวิร์กช็อป MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - การเดินทางนำทางอย่างครบถ้วนเพื่อความมั่นคงของเซิร์ฟเวอร์ MCP ใน Azure โดยใช้วิธีการ "ช่องโหว่ → เจาะ → แก้ไข → ตรวจสอบ"

คำควบคุมความปลอดภัยทั้งหมดในเอกสารนี้สอดคล้องกับ **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** ซึ่งให้สถาปัตยกรรมอ้างอิงและคำแนะนำการใช้งานเฉพาะ Azure สำหรับความเสี่ยง OWASP MCP Top 10

## **ข้อกำหนดความปลอดภัยบังคับ**

### **ข้อห้ามสำคัญจากข้อกำหนด MCP:**

> **ห้าม:** เซิร์ฟเวอร์ MCP **ต้องไม่** ยอมรับโทเค็นใดๆ ที่ไม่ได้ออกอย่างชัดเจนสำหรับเซิร์ฟเวอร์ MCP
>
> **ห้ามใช้:** เซิร์ฟเวอร์ MCP **ต้องไม่** ใช้เซสชันสำหรับการตรวจสอบสิทธิ์  
>
> **ต้องการ:** เซิร์ฟเวอร์ MCP ที่ใช้การอนุญาต **ต้อง** ตรวจสอบคำขอขาเข้าทั้งหมด
>
> **ข้อบังคับ:** เซิร์ฟเวอร์พร็อกซี MCP ที่ใช้ไคลเอนต์ ID ภายนอกแบบคงที่
> **ต้อง** ขอความยินยอมจากแต่ละไคลเอนต์ MCP ก่อนส่งต่อการอนุญาต

---

## 1. **การควบคุมการตรวจสอบสิทธิ์และการอนุญาต**

### **การรวมผู้ให้บริการตัวตนภายนอก**

**ข้อกำหนด MCP `2026-07-28`** อนุญาตให้เซิร์ฟเวอร์ MCP มอบหมาย
การตรวจสอบสิทธิ์ให้กับผู้ให้บริการตัวตนภายนอก การอนุญาตสำหรับการขนส่ง HTTP
จะประเมินต่อคำขอ ส่วนเซิร์ฟเวอร์ stdio ภายในเครื่องจะรับข้อมูลรับรอง
จากสภาพแวดล้อมแทน

**ความเสี่ยง OWASP MCP ที่แก้ไข:** [MCP07 - การตรวจสอบสิทธิ์และการอนุญาตไม่เพียงพอ](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**ประโยชน์ด้านความปลอดภัย:**
1. **ลดความเสี่ยงจากการตรวจสอบสิทธิ์แบบกำหนดเอง:** ลดพื้นผิวช่องโหว่โดยหลีกเลี่ยงการใช้การตรวจสอบสิทธิ์แบบกำหนดเอง
2. **ความปลอดภัยระดับองค์กร:** ใช้ผู้ให้บริการตัวตนที่ได้รับการยอมรับเช่น Microsoft Entra ID ที่มีคุณสมบัติความปลอดภัยขั้นสูง
3. **การจัดการตัวตนแบบรวมศูนย์:** ทำให้การจัดการวงจรชีวิตผู้ใช้ การควบคุมการเข้าถึง และการตรวจสอบความสอดคล้องง่ายขึ้น
4. **การตรวจสอบสิทธิ์หลายปัจจัย:** รับคุณสมบัติ MFA จากผู้ให้บริการตัวตนองค์กร
5. **นโยบายการเข้าถึงตามเงื่อนไข:** ได้ประโยชน์จากการควบคุมการเข้าถึงตามความเสี่ยงและการตรวจสอบสิทธิ์แบบปรับตัว

**ข้อกำหนดการนำไปใช้:**
- **การลงทะเบียนไคลเอนต์:** ควรใช้เอกสารข้อมูลเมตาของ Client ID หรือการลงทะเบียนล่วงหน้า; ใช้ Dynamic Client Registration ที่เลิกใช้แล้วเฉพาะเพื่อความเข้ากันได้เท่านั้น
  

- **การตรวจสอบผู้รับโทเค็น:** ตรวจสอบว่าโทเค็นทั้งหมดออกอย่างชัดเจนสำหรับเซิร์ฟเวอร์ MCP
- **การตรวจสอบผู้ออกโทเค็น:** ตรวจสอบให้แน่ใจว่าผู้ออกโทเค็นตรงกับผู้ให้บริการตัวตนที่คาดไว้
- **การตรวจสอบลายเซ็น:** การตรวจสอบทางคริปโตกราฟีเพื่อความสมบูรณ์ของโทเค็น
- **การบังคับใช้วันหมดอายุ:** บังคับใช้อย่างเคร่งครัดเกี่ยวกับระยะเวลาของโทเค็น
- **การตรวจสอบขอบเขต:** ตรวจสอบให้แน่ใจว่าโทเค็นมีสิทธิ์ที่เหมาะสมสำหรับการดำเนินการที่ร้องขอ

### **ความปลอดภัยของตรรกะการอนุญาต**

**การควบคุมสำคัญ:**
- **การตรวจสอบการอนุญาตอย่างครอบคลุม:** ทบทวนความปลอดภัยอย่างสม่ำเสมอของจุดตัดสินใจทั้งหมดที่เกี่ยวกับการอนุญาต
- **ค่าเริ่มต้นที่ปลอดภัย:** ปฏิเสธการเข้าถึงเมื่อไม่สามารถตัดสินใจการอนุญาตได้อย่างชัดเจน
- **ขอบเขตสิทธิ์:** แยกสิทธิ์และการเข้าถึงทรัพยากรอย่างชัดเจน
- **การบันทึกการตรวจสอบ:** บันทึกอย่างครบถ้วนของการตัดสินใจการอนุญาตทั้งหมดเพื่อการตรวจสอบความปลอดภัย
- **การทบทวนสิทธิ์อย่างสม่ำเสมอ:** ตรวจสอบความถูกต้องของสิทธิ์ผู้ใช้และการมอบสิทธิ์อย่างเป็นระยะ

## 2. **การรักษาความปลอดภัยโทเค็นและการควบคุมป้องกันการส่งผ่าน**

**ความเสี่ยง OWASP MCP ที่แก้ไข:** [MCP01 - การจัดการโทเค็นผิดพลาดและการเปิดเผยความลับ](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **การป้องกันการส่งผ่านโทเค็น**

**การส่งผ่านโทเค็นถูกห้ามอย่างชัดเจน** ในข้อกำหนด MCP Authorization เนื่องจากความเสี่ยงด้านความปลอดภัยร้ายแรง:

**ความเสี่ยงที่แก้ไข:**
- **การลัดเลาะควบคุม:** ข้ามการควบคุมความปลอดภัยที่จำเป็น เช่น การจำกัดจำนวนคำขอ การตรวจสอบคำขอ และการตรวจตราการรับส่งข้อมูล
- **การขาดความรับผิดชอบ:** ทำให้ไม่สามารถระบุไคลเอนต์ได้ ส่งผลให้การตรวจสอบและสืบสวนเหตุการณ์ผิดพลาด
- **การส่งข้อมูลออกโดยใช้พร็อกซี:** ทำให้แฮกเกอร์ใช้เซิร์ฟเวอร์เป็นพร็อกซีเพื่อเข้าถึงข้อมูลโดยไม่ได้รับอนุญาต
- **การละเมิดขอบเขตความไว้วางใจ:** ทำลายสมมติฐานความไว้วางใจของบริการปลายน้ำเกี่ยวกับแหล่งที่มาโทเค็น
- **การเคลื่อนที่ข้างเคียง:** โทเค็นที่ถูกโจมตีในหลายบริการช่วยให้การขยายการโจมตีเป็นวงกว้างขึ้น

**การควบคุมการนำไปใช้:**
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
- **โทเค็นอายุสั้น:** ลดระยะเวลาที่โทเค็นเปิดเผยด้วยการหมุนเวียนโทเค็นบ่อยๆ
- **ออกโทเค็นตามเวลาที่ต้องการ:** ออกโทเค็นเฉพาะเมื่อจำเป็นสำหรับการดำเนินงานเฉพาะ
- **การจัดเก็บอย่างปลอดภัย:** ใช้โมดูลรักษาความปลอดภัยฮาร์ดแวร์ (HSMs) หรือคลังเก็บกุญแจที่ปลอดภัย
- **การผูกโทเค็น:** ตรวจสอบผู้รับโทเค็นและผู้ออกสำหรับทรัพยากร MCP เป้าหมาย ไคลเอนต์ และการดำเนินงาน

- **การเฝ้าระวังและแจ้งเตือน:** ตรวจจับเวลาจริงของการใช้งานโทเค็นผิดหรือรูปแบบการเข้าถึงไม่ได้รับอนุญาต

## 3. **การควบคุมความปลอดภัยสถานะแอปพลิเคชัน**

### **การป้องกันการยึดกลุ่ม handle สถานะ**

**ช่องทางการโจมตีที่แก้ไข:**
- **การเดากลุ่ม handle:** ตัวระบุที่สามารถทำนายได้เปิดเผยสถานะของผู้เรียกคนอื่น
- **การใช้ซ้ำข้ามผู้ใช้:** กลุ่ม handle ที่ถูกขโมยถูกใช้กับตัวตนอื่น
- **การอนุญาตโดยปริยาย:** การครอบครองกลุ่ม handle ถูกเข้าใจผิดว่าเป็น
  หลักฐานของการเข้าถึง

**การควบคุมกลุ่ม handle สถานะ:**

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

**ความปลอดภัยการขนส่ง:**
- **การบังคับใช้ HTTPS:** ต้องใช้ HTTPS สำหรับการขนส่ง HTTP ระยะไกล
- **การจัดการข้อมูลรับรอง:** ส่งและตรวจสอบการอนุญาตในทุกคำขอ HTTP
- **การแยก stdio:** ปกป้องเซิร์ฟเวอร์ stdio ภายในเครื่องผ่านการแยกกระบวนการและ
  การควบคุมข้อมูลรับรองในสภาพแวดล้อม

### **ข้อพิจารณาระหว่าง Stateful กับ Stateless**

MCP `2026-07-28` ไม่มีสถานะที่ชั้นโปรโตคอล แอปพลิเคชันอาจยังคง
เก็บสถานะโดยส่งกลับกลุ่ม handle อย่างชัดเจนจากการเรียกเครื่องมือหนึ่งและรับ
เป็นอาร์กิวเมนต์ปกติในคำเรียกล่าช้า

- เก็บสถานะแยกจากการเชื่อมต่อขนส่งใดๆ
- ผูกกลุ่ม handle สถานะกับตัวเซิร์ฟเวอร์หลักที่ผ่านการตรวจสอบสิทธิ์ฝั่งเซิร์ฟเวอร์
- ปฏิบัติกับกลุ่ม handle เป็นเหมือนชื่อ ไม่ใช่ข้อมูลรับรองผู้ถือ
- กำหนดพฤติกรรมหมดอายุและการกู้คืนสำหรับกลุ่ม handle ที่ล้าสมัย

## 4. **การควบคุมความปลอดภัยเฉพาะ AI**

**ความเสี่ยง OWASP MCP ที่แก้ไข:**

- [MCP06 - การลักลอบเปลี่ยนเจตนาในโฟลว์](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - การปลอมแปลงเครื่องมือ](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - การแทรกคำสั่งและการดำเนินการ](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **การป้องกันการแทรกคำสั่ง Prompt**

**การผสานรวม Microsoft Prompt Shields:**
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

**การควบคุมการดำเนินงาน:**
- **การล้างข้อมูลนำเข้า**: การตรวจสอบและกรองข้อมูลจากผู้ใช้ทั้งหมดอย่างละเอียด
- **การกำหนดขอบเขตเนื้อหา**: การแยกคำสั่งระบบและเนื้อหาผู้ใช้อย่างชัดเจน
- **ลำดับความสำคัญคำสั่ง**: กฎลำดับความสำคัญที่เหมาะสมสำหรับคำสั่งที่ขัดแย้งกัน
- **การตรวจสอบผลลัพธ์**: การตรวจจับผลลัพธ์ที่อาจเป็นอันตรายหรือถูกดัดแปลง

### **การป้องกันการปลอมแปลงเครื่องมือ**

**โครงสร้างความปลอดภัยเครื่องมือ:**
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
- **เวิร์กโฟลว์การอนุมัติ**: การขอความยินยอมจากผู้ใช้ชัดเจนสำหรับการแก้ไขเครื่องมือ
- **ความสามารถในการย้อนกลับ**: ความสามารถในการกลับไปยังเวอร์ชันเครื่องมือก่อนหน้าได้
- **การตรวจสอบการเปลี่ยนแปลง**: ประวัติการแก้ไขคำจำกัดความเครื่องมืออย่างครบถ้วน
- **การประเมินความเสี่ยง**: การประเมินสถานะความปลอดภัยของเครื่องมือโดยอัตโนมัติ

## 5. **การป้องกันการโจมตี Confused Deputy**

### **ความปลอดภัยของ OAuth Proxy**

**การควบคุมเพื่อป้องกันการโจมตี:**
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

**ข้อกำหนดการดำเนินงาน:**
- **การลงทะเบียนลูกค้า**: ควรใช้การลงทะเบียนล่วงหน้าหรือเอกสาร Client ID Metadata
  พิจารณาการลงทะเบียนลูกค้าแบบไดนามิกเป็นการสำรองความเข้ากันได้
- **การยืนยันความยินยอมของผู้ใช้**: MCP proxy ที่ใช้ client รายบุคคลของบุคคลที่สามคงที่
  ต้องได้รับความยินยอมแยกตามลูกค้าก่อนส่งต่อการอนุญาต
- **การตรวจสอบ URI การเปลี่ยนเส้นทาง**: การตรวจสอบบนรายการอนุญาตอย่างเข้มงวดของจุดหมายปลายทางเปลี่ยนเส้นทาง
- **การปกป้องรหัสอนุญาต**: รหัสที่มีอายุสั้นและบังคับใช้การใช้ครั้งเดียว
- **การยืนยันตัวตนของลูกค้า**: การตรวจสอบข้อมูลประจำตัวและ metadata ของลูกค้าอย่างเข้มงวด

## 6. **ความปลอดภัยในการดำเนินการเครื่องมือ**

### **การแยกและการแซนด์บ็อกซ์**

**การแยกโดยใช้คอนเทนเนอร์:**
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

**การแยกระบบประมวลผล:**
- **บริบทกระบวนการแยกต่างหาก**: การดำเนินการเครื่องมือแต่ละเครื่องในพื้นที่กระบวนการแยก
- **การสื่อสารระหว่างกระบวนการ (IPC)**: กลไก IPC ที่ปลอดภัยและมีการตรวจสอบ
- **การตรวจสอบกระบวนการ**: การวิเคราะห์พฤติกรรมการทำงานและการตรวจจับความผิดปกติ
- **การบังคับใช้ทรัพยากร**: จำกัดอย่างเข้มงวดใน CPU หน่วยความจำ และการดำเนินการ I/O

### **การใช้สิทธิ์น้อยที่สุด**

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

## 7. **การควบคุมความปลอดภัยซัพพลายเชน**

**OWASP MCP ความเสี่ยงที่แก้ไข**: [MCP04 - การโจมตีซัพพลายเชนซอฟต์แวร์และการดัดแปลงการพึ่งพา](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **การตรวจสอบการพึ่งพา**

**ความปลอดภัยส่วนประกอบอย่างรอบด้าน:**
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

**การตรวจจับภัยคุกคามซัพพลายเชน:**
- **การติดตามสุขภาพของการพึ่งพา**: การประเมินอย่างต่อเนื่องของการพึ่งพาทั้งหมดเพื่อหาปัญหาด้านความปลอดภัย
- **การผสานข่าวกรองภัยคุกคาม**: การอัปเดตแบบเรียลไทม์เกี่ยวกับภัยคุกคามซัพพลายเชนที่เกิดขึ้นใหม่
- **การวิเคราะห์พฤติกรรม**: การตรวจจับพฤติกรรมผิดปกติในส่วนประกอบภายนอก
- **การตอบสนองอัตโนมัติ**: การกักกันส่วนประกอบที่ถูกแทรกแซงทันที

## 8. **การควบคุมการตรวจสอบและการตรวจจับ**

**OWASP MCP ความเสี่ยงที่แก้ไข**: [MCP08 - ขาดการตรวจสอบและโทรเมทรี](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **การจัดการข้อมูลความปลอดภัยและเหตุการณ์ (SIEM)**

**กลยุทธ์การบันทึกข้อมูลอย่างครบถ้วน:**
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
- **การวิเคราะห์พฤติกรรมผู้ใช้ (UBA)**: การตรวจจับรูปแบบการเข้าถึงผู้ใช้ที่ผิดปกติ
- **การวิเคราะห์พฤติกรรมหน่วยงาน (EBA)**: การเฝ้าระวังพฤติกรรมของเซิร์ฟเวอร์ MCP และเครื่องมือ
- **การตรวจจับความผิดปกติด้วยการเรียนรู้ของเครื่อง**: การระบุภัยคุกคามทางความปลอดภัยด้วย AI
- **การเชื่อมโยงข่าวกรองภัยคุกคาม**: การจับคู่กิจกรรมที่สังเกตกับรูปแบบการโจมตีที่รู้จัก

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

### **ความสามารถในการตรวจสอบทางนิติวิทยาศาสตร์**

**การสนับสนุนการสอบสวน:**
- **การรักษาบันทึกตรวจสอบ**: การบันทึกที่ไม่สามารถแก้ไขได้พร้อมความสมบูรณ์ด้วยรหัสคริปโตกราฟฟี
- **การรวบรวมหลักฐาน**: การรวบรวมอัตโนมัติของสิ่งของด้านความปลอดภัยที่เกี่ยวข้อง
- **การสร้างลำดับเวลาทางเหตุการณ์**: ลำดับเหตุการณ์อย่างละเอียดที่นำไปสู่เหตุการณ์ความปลอดภัย
- **การประเมินผลกระทบ**: การประเมินขอบเขตของการถูกเจาะและการเปิดเผยข้อมูล

## **หลักการออกแบบความปลอดภัยสำคัญ**

### **การป้องกันเชิงลึก**
- **ชั้นความปลอดภัยหลายชั้น**: ไม่มีจุดล้มเหลวเดียวในสถาปัตยกรรมความปลอดภัย
- **การควบคุมซ้ำซ้อน**: มาตรการความปลอดภัยซ้อนทับสำหรับฟังก์ชันที่สำคัญ
- **กลไกการป้องกันเมื่อเกิดข้อผิดพลาด**: ค่าปริยายที่ปลอดภัยเมื่อตรวจพบข้อผิดพลาดหรือการโจมตี

### **การใช้งานแนวคิด Zero Trust**
- **ไม่เชื่อถือโดยอัตโนมัติ ตรวจสอบตลอดเวลา**: การตรวจสอบอย่างต่อเนื่องของหน่วยงานและคำขอทั้งหมด
- **หลักการใช้สิทธิ์น้อยที่สุด**: สิทธิ์เข้าถึงขั้นต่ำสุดสำหรับทุกส่วนประกอบ
- **การแบ่งส่วนเครือข่ายอย่างละเอียด**: การควบคุมเครือข่ายและการเข้าถึงอย่างละเอียด

### **วิวัฒนาการความปลอดภัยอย่างต่อเนื่อง**
- **การปรับตัวต่อภูมิทัศน์ภัยคุกคาม**: การอัปเดตเป็นประจำเพื่อตอบสนองภัยคุกคามที่เกิดขึ้นใหม่
- **ประสิทธิภาพการควบคุมความปลอดภัย**: การประเมินและปรับปรุงมาตรการอย่างต่อเนื่อง
- **การปฏิบัติตามข้อกำหนด**: ความสอดคล้องกับมาตรฐานความปลอดภัย MCP ที่พัฒนาไปตามลำดับ

---

## **แหล่งข้อมูลสำหรับการดำเนินงาน**

### **เอกสาร MCP อย่างเป็นทางการ**
- [ข้อกำหนด MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [แนวปฏิบัติความปลอดภัยที่ดีที่สุดของ MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [ข้อกำหนดการอนุญาต MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **แหล่งข้อมูลความปลอดภัย OWASP MCP**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - รายการ 10 อันดับสูงสุดของ OWASP MCP พร้อมการใช้งานบน Azure อย่างครบถ้วน
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - ความเสี่ยงความปลอดภัยอย่างเป็นทางการของ OWASP MCP
- [การประชุมเชิงปฏิบัติการ MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - การฝึกอบรมความปลอดภัยเชิงปฏิบัติสำหรับ MCP บน Azure

### **โซลูชันความปลอดภัยของ Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **มาตรฐานความปลอดภัย**
- [แนวปฏิบัติความปลอดภัย OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP 10 อันดับแรกสำหรับโมเดลภาษาใหญ่](https://genai.owasp.org/)

- [กรอบงานความปลอดภัยทางไซเบอร์ของ NIST](https://www.nist.gov/cyberframework)

---

> **สำคัญ:** การควบคุมความปลอดภัยเหล่านี้สะท้อนถึงข้อกำหนด MCP
> `2026-07-28` โปรดยืนยันเสมอโดยเปรียบเทียบกับ
> [เอกสารอย่างเป็นทางการปัจจุบัน](https://modelcontextprotocol.io/specification/2026-07-28/)
> เนื่องจากมาตรฐานยังคงมีการพัฒนาอย่างต่อเนื่อง

## ต่อไป

- กลับไปที่: [ภาพรวมโมดูลความปลอดภัย](./README.md)
- ไปต่อที่: [โมดูล 3: เริ่มต้นใช้งาน](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->