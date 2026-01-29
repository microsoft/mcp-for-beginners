# MCP Security Controls - Cập nhật Tháng 12 Năm 2025

> **Tiêu Chuẩn Hiện Tại**: Tài liệu này phản ánh các yêu cầu bảo mật của [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) và [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) chính thức.

Model Context Protocol (MCP) đã phát triển đáng kể với các kiểm soát bảo mật nâng cao, giải quyết cả bảo mật phần mềm truyền thống và các mối đe dọa đặc thù AI. Tài liệu này cung cấp các kiểm soát bảo mật toàn diện cho các triển khai MCP an toàn tính đến tháng 12 năm 2025.

## **Yêu Cầu Bảo Mật BẮT BUỘC**

### **Các Cấm KỴ Quan Trọng từ MCP Specification:**

> **CẤM**: Máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận bất kỳ token nào không được cấp rõ ràng cho máy chủ MCP  
>
> **CẤM**: Máy chủ MCP **KHÔNG ĐƯỢC** sử dụng phiên làm phương thức xác thực  
>
> **BẮT BUỘC**: Máy chủ MCP triển khai ủy quyền **PHẢI** xác minh TẤT CẢ các yêu cầu đến  
>
> **BẮT BUỘC**: Máy chủ proxy MCP sử dụng client ID tĩnh **PHẢI** lấy sự đồng ý của người dùng cho mỗi client đăng ký động

---

## 1. **Kiểm Soát Xác Thực & Ủy Quyền**

### **Tích Hợp Nhà Cung Cấp Danh Tính Bên Ngoài**

**Tiêu Chuẩn MCP Hiện Tại (2025-06-18)** cho phép máy chủ MCP ủy quyền xác thực cho các nhà cung cấp danh tính bên ngoài, đại diện cho một cải tiến bảo mật đáng kể:

### **Tích Hợp Nhà Cung Cấp Danh Tính Bên Ngoài**

**Tiêu Chuẩn MCP Hiện Tại (2025-11-25)** cho phép máy chủ MCP ủy quyền xác thực cho các nhà cung cấp danh tính bên ngoài, đại diện cho một cải tiến bảo mật đáng kể:

**Lợi Ích Bảo Mật:**
1. **Loại Bỏ Rủi Ro Xác Thực Tùy Chỉnh**: Giảm bề mặt lỗ hổng bằng cách tránh triển khai xác thực tùy chỉnh
2. **Bảo Mật Cấp Doanh Nghiệp**: Tận dụng các nhà cung cấp danh tính đã được thiết lập như Microsoft Entra ID với các tính năng bảo mật nâng cao
3. **Quản Lý Danh Tính Tập Trung**: Đơn giản hóa quản lý vòng đời người dùng, kiểm soát truy cập và kiểm toán tuân thủ
4. **Xác Thực Đa Yếu Tố**: Kế thừa khả năng MFA từ các nhà cung cấp danh tính doanh nghiệp
5. **Chính Sách Truy Cập Có Điều Kiện**: Lợi ích từ kiểm soát truy cập dựa trên rủi ro và xác thực thích ứng

**Yêu Cầu Triển Khai:**
- **Xác Thực Đối Tượng Token**: Xác minh tất cả token được cấp rõ ràng cho máy chủ MCP
- **Xác Thực Nhà Phát Hành**: Xác nhận nhà phát hành token khớp với nhà cung cấp danh tính mong đợi
- **Xác Thực Chữ Ký**: Xác minh mật mã tính toàn vẹn token
- **Thực Thi Hạn Sử Dụng**: Thực thi nghiêm ngặt giới hạn thời gian sống của token
- **Xác Thực Phạm Vi**: Đảm bảo token chứa quyền phù hợp cho các thao tác yêu cầu

### **Bảo Mật Logic Ủy Quyền**

**Kiểm Soát Quan Trọng:**
- **Kiểm Toán Ủy Quyền Toàn Diện**: Đánh giá bảo mật định kỳ tất cả các điểm quyết định ủy quyền
- **Mặc Định An Toàn**: Từ chối truy cập khi logic ủy quyền không thể đưa ra quyết định rõ ràng
- **Ranh Giới Quyền Hạn**: Phân tách rõ ràng giữa các cấp độ đặc quyền và truy cập tài nguyên
- **Ghi Nhật Ký Kiểm Toán**: Ghi lại đầy đủ tất cả các quyết định ủy quyền để giám sát bảo mật
- **Đánh Giá Truy Cập Định Kỳ**: Xác nhận định kỳ quyền và phân quyền người dùng

## 2. **Bảo Mật Token & Kiểm Soát Chống Chuyển Tiếp Token**

### **Ngăn Chặn Chuyển Tiếp Token**

**Chuyển tiếp token bị cấm rõ ràng** trong MCP Authorization Specification do các rủi ro bảo mật nghiêm trọng:

**Rủi Ro Bảo Mật Được Giải Quyết:**
- **Vượt Qua Kiểm Soát**: Bỏ qua các kiểm soát bảo mật thiết yếu như giới hạn tốc độ, xác thực yêu cầu và giám sát lưu lượng
- **Phá Vỡ Trách Nhiệm**: Không thể xác định client, làm hỏng dấu vết kiểm toán và điều tra sự cố
- **Rút Trộm Qua Proxy**: Cho phép kẻ xấu sử dụng máy chủ làm proxy truy cập dữ liệu trái phép
- **Vi Phạm Ranh Giới Tin Cậy**: Phá vỡ giả định tin cậy của dịch vụ hạ nguồn về nguồn gốc token
- **Di Chuyển Ngang**: Token bị xâm phạm trên nhiều dịch vụ cho phép mở rộng tấn công

**Kiểm Soát Triển Khai:**
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

### **Mẫu Quản Lý Token An Toàn**

**Thực Tiễn Tốt Nhất:**
- **Token Ngắn Hạn**: Giảm thời gian phơi nhiễm bằng cách xoay token thường xuyên
- **Cấp Phát Kịp Thời**: Cấp token chỉ khi cần cho các thao tác cụ thể
- **Lưu Trữ An Toàn**: Sử dụng mô-đun bảo mật phần cứng (HSM) hoặc kho khóa an toàn
- **Ràng Buộc Token**: Ràng buộc token với client, phiên hoặc thao tác cụ thể nếu có thể
- **Giám Sát & Cảnh Báo**: Phát hiện thời gian thực các hành vi sử dụng token sai hoặc truy cập trái phép

## 3. **Kiểm Soát Bảo Mật Phiên**

### **Ngăn Chặn Chiếm Đoạt Phiên**

**Các Vector Tấn Công Được Giải Quyết:**
- **Tiêm Prompt Chiếm Đoạt Phiên**: Các sự kiện độc hại được tiêm vào trạng thái phiên chia sẻ
- **Mạo Danh Phiên**: Sử dụng trái phép ID phiên bị đánh cắp để vượt qua xác thực
- **Tấn Công Tiếp Tục Luồng**: Khai thác sự tiếp tục sự kiện gửi từ máy chủ để tiêm nội dung độc hại

**Kiểm Soát Phiên Bắt Buộc:**
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

**Bảo Mật Vận Chuyển:**
- **Thực Thi HTTPS**: Tất cả giao tiếp phiên qua TLS 1.3
- **Thuộc Tính Cookie An Toàn**: HttpOnly, Secure, SameSite=Strict
- **Ghim Chứng Chỉ**: Cho các kết nối quan trọng để ngăn tấn công MITM

### **Xem Xét Stateful vs Stateless**

**Đối Với Triển Khai Stateful:**
- Trạng thái phiên chia sẻ cần bảo vệ bổ sung chống tiêm độc hại
- Quản lý phiên dựa trên hàng đợi cần xác minh tính toàn vẹn
- Nhiều phiên bản máy chủ cần đồng bộ trạng thái phiên an toàn

**Đối Với Triển Khai Stateless:**
- Quản lý phiên dựa trên JWT hoặc token tương tự
- Xác minh mật mã tính toàn vẹn trạng thái phiên
- Giảm bề mặt tấn công nhưng yêu cầu xác thực token mạnh mẽ

## 4. **Kiểm Soát Bảo Mật Đặc Thù AI**

### **Phòng Thủ Tiêm Prompt**

**Tích Hợp Microsoft Prompt Shields:**
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

**Kiểm Soát Triển Khai:**
- **Làm Sạch Đầu Vào**: Xác thực và lọc toàn diện tất cả đầu vào người dùng
- **Định Nghĩa Ranh Giới Nội Dung**: Phân tách rõ ràng giữa hướng dẫn hệ thống và nội dung người dùng
- **Thứ Tự Ưu Tiên Hướng Dẫn**: Quy tắc ưu tiên hợp lý cho các hướng dẫn mâu thuẫn
- **Giám Sát Đầu Ra**: Phát hiện các đầu ra có thể gây hại hoặc bị thao túng

### **Ngăn Chặn Độc Hại Công Cụ**

**Khung Bảo Mật Công Cụ:**
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

**Quản Lý Công Cụ Động:**
- **Quy Trình Phê Duyệt**: Lấy sự đồng ý rõ ràng của người dùng cho các thay đổi công cụ
- **Khả Năng Quay Lại**: Khả năng phục hồi về phiên bản công cụ trước đó
- **Kiểm Toán Thay Đổi**: Lịch sử đầy đủ các sửa đổi định nghĩa công cụ
- **Đánh Giá Rủi Ro**: Đánh giá tự động về tư thế bảo mật công cụ

## 5. **Ngăn Chặn Tấn Công Confused Deputy**

### **Bảo Mật Proxy OAuth**

**Kiểm Soát Ngăn Chặn Tấn Công:**
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

**Yêu Cầu Triển Khai:**
- **Xác Minh Sự Đồng Ý Người Dùng**: Không bao giờ bỏ qua màn hình đồng ý cho đăng ký client động
- **Xác Thực URI Chuyển Hướng**: Xác thực nghiêm ngặt dựa trên danh sách trắng các đích chuyển hướng
- **Bảo Vệ Mã Ủy Quyền**: Mã ngắn hạn với thực thi một lần
- **Xác Thực Danh Tính Client**: Xác minh mạnh mẽ thông tin xác thực và metadata client

## 6. **Bảo Mật Thực Thi Công Cụ**

### **Cách Ly & Sandboxing**

**Cách Ly Dựa Trên Container:**
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

**Cách Ly Quy Trình:**
- **Ngữ Cảnh Quy Trình Riêng Biệt**: Mỗi thực thi công cụ trong không gian quy trình cách ly
- **Giao Tiếp Liên Quy Trình**: Cơ chế IPC an toàn với xác thực
- **Giám Sát Quy Trình**: Phân tích hành vi thời gian chạy và phát hiện bất thường
- **Thực Thi Tài Nguyên**: Giới hạn cứng CPU, bộ nhớ và I/O

### **Triển Khai Quyền Ít Nhất**

**Quản Lý Quyền Hạn:**
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

## 7. **Kiểm Soát Bảo Mật Chuỗi Cung Ứng**

### **Xác Minh Phụ Thuộc**

**Bảo Mật Thành Phần Toàn Diện:**
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

### **Giám Sát Liên Tục**

**Phát Hiện Mối Đe Dọa Chuỗi Cung Ứng:**
- **Giám Sát Sức Khỏe Phụ Thuộc**: Đánh giá liên tục tất cả phụ thuộc về các vấn đề bảo mật
- **Tích Hợp Tình Báo Mối Đe Dọa**: Cập nhật thời gian thực về các mối đe dọa chuỗi cung ứng mới nổi
- **Phân Tích Hành Vi**: Phát hiện hành vi bất thường trong các thành phần bên ngoài
- **Phản Ứng Tự Động**: Ngăn chặn ngay lập tức các thành phần bị xâm phạm

## 8. **Kiểm Soát Giám Sát & Phát Hiện**

### **Quản Lý Thông Tin & Sự Kiện Bảo Mật (SIEM)**

**Chiến Lược Ghi Nhật Ký Toàn Diện:**
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

### **Phát Hiện Mối Đe Dọa Thời Gian Thực**

**Phân Tích Hành Vi:**
- **Phân Tích Hành Vi Người Dùng (UBA)**: Phát hiện các mẫu truy cập người dùng bất thường
- **Phân Tích Hành Vi Thực Thể (EBA)**: Giám sát hành vi máy chủ MCP và công cụ
- **Phát Hiện Bất Thường Bằng Máy Học**: Nhận diện mối đe dọa bảo mật bằng AI
- **Tương Quan Tình Báo Mối Đe Dọa**: So khớp hoạt động quan sát với các mẫu tấn công đã biết

## 9. **Ứng Phó Sự Cố & Phục Hồi**

### **Khả Năng Ứng Phó Tự Động**

**Hành Động Ứng Phó Ngay Lập Tức:**
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

### **Khả Năng Pháp Y**

**Hỗ Trợ Điều Tra:**
- **Bảo Tồn Dấu Vết Kiểm Toán**: Ghi nhật ký không thể thay đổi với tính toàn vẹn mật mã
- **Thu Thập Bằng Chứng**: Tự động thu thập các hiện vật bảo mật liên quan
- **Tái Tạo Dòng Thời Gian**: Chuỗi sự kiện chi tiết dẫn đến sự cố bảo mật
- **Đánh Giá Tác Động**: Đánh giá phạm vi xâm phạm và mức độ lộ dữ liệu

## **Nguyên Tắc Kiến Trúc Bảo Mật Chính**

### **Phòng Thủ Nhiều Lớp**
- **Nhiều Lớp Bảo Mật**: Không có điểm thất bại đơn lẻ trong kiến trúc bảo mật
- **Kiểm Soát Dự Phòng**: Các biện pháp bảo mật chồng chéo cho các chức năng quan trọng
- **Cơ Chế An Toàn**: Mặc định an toàn khi hệ thống gặp lỗi hoặc tấn công

### **Triển Khai Zero Trust**
- **Không Bao Giờ Tin, Luôn Xác Minh**: Xác thực liên tục tất cả thực thể và yêu cầu
- **Nguyên Tắc Quyền Ít Nhất**: Quyền truy cập tối thiểu cho tất cả thành phần
- **Phân Đoạn Vi Mạng**: Kiểm soát mạng và truy cập chi tiết

### **Tiến Hóa Bảo Mật Liên Tục**
- **Thích Ứng Với Cảnh Quan Mối Đe Dọa**: Cập nhật định kỳ để giải quyết các mối đe dọa mới nổi
- **Hiệu Quả Kiểm Soát Bảo Mật**: Đánh giá và cải tiến liên tục các kiểm soát
- **Tuân Thủ Tiêu Chuẩn**: Phù hợp với các tiêu chuẩn bảo mật MCP đang phát triển

---

## **Tài Nguyên Triển Khai**

### **Tài Liệu MCP Chính Thức**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Giải Pháp Bảo Mật Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Tiêu Chuẩn Bảo Mật**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Quan Trọng**: Các kiểm soát bảo mật này phản ánh tiêu chuẩn MCP hiện tại (2025-06-18). Luôn xác minh với [tài liệu chính thức](https://spec.modelcontextprotocol.io/) mới nhất vì các tiêu chuẩn tiếp tục phát triển nhanh chóng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->