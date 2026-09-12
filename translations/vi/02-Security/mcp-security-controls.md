# Kiểm Soát An Ninh MCP - Cập Nhật Tháng 9 Năm 2026

> **Tiêu chuẩn hiện tại:** Tài liệu này phản ánh
> [Đặc tả MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> và
> [Thực hành Bảo mật Tốt nhất MCP chính thức](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Giao thức Ngữ cảnh Mô hình (MCP) đã trưởng thành đáng kể với các kiểm soát an ninh nâng cao, giải quyết cả bảo mật phần mềm truyền thống và các mối đe dọa đặc thù AI. Tài liệu này cung cấp các kiểm soát an ninh toàn diện cho các triển khai MCP an toàn phù hợp với khung OWASP MCP Top 10.

## 🏔️ Đào Tạo An Ninh Thực Hành

Để có kinh nghiệm thực tế về triển khai an ninh, chúng tôi khuyến nghị **[Hội thảo Thượng đỉnh An ninh MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** – một chuyến thám hiểm có hướng dẫn toàn diện nhằm bảo vệ các máy chủ MCP trên Azure bằng phương pháp "dễ bị tấn công → khai thác → sửa → xác nhận".

Tất cả các kiểm soát an ninh trong tài liệu này đều phù hợp với **[Hướng dẫn An ninh Azure MCP OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, cung cấp các kiến trúc tham khảo và hướng dẫn triển khai cụ thể trên Azure cho các rủi ro trong OWASP MCP Top 10.

## **Yêu Cầu An Ninh Bắt Buộc**

### **Các Lệnh Cấm Quan Trọng từ Đặc tả MCP:**

> **CẤM:** Máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận bất kỳ mã thông báo nào không được cấp rõ ràng cho máy chủ MCP
>
> **CẤM:** Máy chủ MCP **KHÔNG ĐƯỢC** sử dụng phiên cho xác thực  
>
> **YÊU CẦU:** Máy chủ MCP thực thi ủy quyền **PHẢI** xác minh TẤT CẢ các yêu cầu đến
>
> **BẮT BUỘC:** Các máy chủ proxy MCP sử dụng client ID tĩnh của bên thứ ba
> **PHẢI** nhận được sự đồng ý cho mỗi khách hàng MCP trước khi chuyển tiếp ủy quyền

---

## 1. **Kiểm Soát Xác Thực & Ủy Quyền**

### **Tích Hợp Nhà Cung Cấp Danh Tính Bên Ngoài**

**Đặc tả MCP `2026-07-28`** cho phép các máy chủ MCP ủy quyền
xác thực cho các nhà cung cấp danh tính bên ngoài. Ủy quyền cho các phương thức HTTP
được đánh giá theo từng yêu cầu; các máy chủ stdio cục bộ thay vào đó lấy thông tin xác thực
từ môi trường của chúng.

**Rủi ro MCP OWASP được giải quyết**: [MCP07 - Xác thực & ủy quyền không đầy đủ](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Lợi ích về An ninh:**
1. **Loại bỏ Rủi ro Xác thực Tùy chỉnh**: Giảm bề mặt lỗ hổng bằng cách tránh các triển khai xác thực tùy chỉnh
2. **An ninh Cấp Doanh nghiệp**: Tận dụng các nhà cung cấp danh tính đã được thiết lập như Microsoft Entra ID với các tính năng an ninh nâng cao
3. **Quản lý Danh tính Tập trung**: Đơn giản hóa quản lý vòng đời người dùng, kiểm soát truy cập và kiểm toán tuân thủ
4. **Xác thực Đa Yếu tố**: Kế thừa khả năng MFA từ các nhà cung cấp danh tính doanh nghiệp
5. **Chính sách Truy cập Có điều kiện**: Hưởng lợi từ các kiểm soát truy cập dựa trên rủi ro và xác thực thích ứng

**Yêu cầu Triển khai:**
- **Đăng ký Khách hàng**: Ưu tiên Tài liệu Metadata Client ID hoặc
  đăng ký trước; chỉ sử dụng Đăng ký Client Động đã lỗi thời để
  tương thích
- **Xác minh Đối tượng Token**: Xác minh tất cả các mã thông báo được cấp rõ ràng cho máy chủ MCP
- **Xác minh Người cấp**: Xác nhận người phát token khớp với nhà cung cấp danh tính mong đợi
- **Xác minh Chữ ký**: Xác thực mã hóa tính toàn vẹn của token
- **Thi hành Hết hạn**: Thi hành nghiêm ngặt giới hạn thời gian sống của token
- **Xác minh Phạm vi**: Đảm bảo mã thông báo chứa quyền hạn phù hợp cho các thao tác được yêu cầu

### **Bảo mật Logic Ủy quyền**


**Kiểm soát quan trọng:**
- **Kiểm toán ủy quyền toàn diện**: Đánh giá bảo mật định kỳ tất cả các điểm quyết định ủy quyền
- **Mặc định an toàn**: Từ chối truy cập khi logic ủy quyền không thể đưa ra quyết định rõ ràng
- **Ranh giới quyền hạn**: Phân tách rõ ràng giữa các cấp độ đặc quyền và truy cập tài nguyên
- **Ghi nhật ký kiểm toán**: Ghi lại đầy đủ tất cả các quyết định ủy quyền để theo dõi bảo mật
- **Kiểm tra truy cập định kỳ**: Xác nhận định kỳ các quyền và phân bổ đặc quyền của người dùng

## 2. **Bảo mật Token & Kiểm soát chống truyền token**

**Rủi ro OWASP MCP được giải quyết**: [MCP01 - Quản lý token sai và lộ thông tin bí mật](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Ngăn chặn truyền token**

**Việc truyền token bị cấm rõ ràng** trong Đặc tả Ủy quyền MCP do các rủi ro bảo mật nghiêm trọng:

**Các rủi ro bảo mật đã được giải quyết:**
- **Vượt qua kiểm soát**: Bỏ qua các kiểm soát quan trọng như giới hạn tốc độ, xác minh yêu cầu và giám sát lưu lượng
- **Phá vỡ trách nhiệm**: Làm cho việc xác định khách hàng trở nên không thể, làm hỏng dấu vết kiểm toán và điều tra sự cố
- **Rút trộm thông qua proxy**: Cho phép tác nhân xấu sử dụng máy chủ làm proxy để truy cập dữ liệu trái phép
- **Vi phạm ranh giới tin cậy**: Phá vỡ giả định tin cậy của dịch vụ hạ nguồn về nguồn gốc token
- **Di chuyển ngang**: Token bị lộ trên nhiều dịch vụ cho phép mở rộng tấn công rộng hơn

**Kiểm soát triển khai:**
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

### **Mẫu quản lý token an toàn**

**Thực hành tốt nhất:**
- **Token thời gian sống ngắn**: Giảm thiểu thời gian phơi nhiễm bằng cách xoay token thường xuyên
- **Cấp phát kịp thời**: Cấp token chỉ khi cần thiết cho các thao tác cụ thể
- **Lưu trữ an toàn**: Sử dụng mô-đun bảo mật phần cứng (HSM) hoặc kho khóa an toàn
- **Ràng buộc token**: Xác thực đối tượng và nhà phát hành token cho MCP
  tài nguyên, khách hàng và thao tác phù hợp
- **Giám sát & cảnh báo**: Phát hiện theo thời gian thực việc sử dụng sai token hoặc các mẫu truy cập trái phép

## 3. **Kiểm soát bảo mật trạng thái ứng dụng**

### **Ngăn chặn chiếm đoạt State Handle**

**Các vectơ tấn công được giải quyết:**
- **Dự đoán handle**: Định danh có thể đoán được làm lộ trạng thái của bên gọi khác
- **Tái sử dụng giữa người dùng**: Handle bị đánh cắp được sử dụng với danh tính khác
- **Ủy quyền ngầm định**: Sở hữu handle bị nhầm là
  bằng chứng truy cập

**Kiểm soát State Handle:**

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

**Bảo mật vận chuyển:**
- **Yêu cầu HTTPS**: Bắt buộc HTTPS cho các vận chuyển HTTP từ xa
- **Xử lý thông tin đăng nhập**: Gửi và xác thực ủy quyền trên mọi yêu cầu HTTP
- **Cách ly stdio**: Bảo vệ máy chủ stdio cục bộ thông qua cách ly tiến trình và
  kiểm soát thông tin đăng nhập môi trường

### **Cân nhắc trạng thái có trạng thái và không trạng thái**

MCP `2026-07-28` là không trạng thái ở lớp giao thức. Các ứng dụng vẫn có thể
duy trì trạng thái bằng cách trả về một handle rõ ràng từ một lần gọi công cụ và chấp nhận
nó như một đối số thông thường trong các lần gọi sau.

- Lưu trữ trạng thái độc lập với bất kỳ kết nối vận chuyển nào.
- Ràng buộc state handle với máy chủ chính xác xác thực.
- Xử lý một handle như một tên, không phải như chứng chỉ người mang.
- Định nghĩa hành vi hết hạn và phục hồi cho các handle lỗi thời.

## 4. **Kiểm soát bảo mật dành riêng cho AI**

**Rủi ro OWASP MCP được giải quyết**:

- [MCP06 - Phá hoại Dòng Ý định](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Đầu độc Công cụ](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Tiêm Lệnh & Thực thi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Phòng thủ Tiêm Lệnh**

**Tích hợp Microsoft Prompt Shields:**
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

**Kiểm soát Triển khai:**
- **Làm sạch đầu vào**: Xác thực và lọc toàn diện tất cả các đầu vào của người dùng
- **Định nghĩa Ranh giới Nội dung**: Phân tách rõ ràng giữa lệnh hệ thống và nội dung người dùng
- **Cấp bậc Hướng dẫn**: Quy tắc ưu tiên phù hợp cho các lệnh mâu thuẫn
- **Giám sát Đầu ra**: Phát hiện các đầu ra có thể gây hại hoặc bị thao túng

### **Phòng ngừa Đầu độc Công cụ**

**Khung Bảo mật Công cụ:**
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

**Quản lý Công cụ Động:**
- **Quy trình Phê duyệt**: Sự đồng thuận rõ ràng của người dùng cho các sửa đổi công cụ
- **Khả năng Hoàn tác**: Khả năng trở lại các phiên bản công cụ trước đó
- **Kiểm toán Thay đổi**: Lịch sử đầy đủ các sửa đổi định nghĩa công cụ
- **Đánh giá Rủi ro**: Đánh giá tự động về tư thế bảo mật của công cụ

## 5. **Phòng ngừa Tấn công Confused Deputy**

### **Bảo mật OAuth Proxy**

**Kiểm soát Phòng ngừa Tấn công:**
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

**Yêu cầu Triển khai:**
- **Đăng ký Khách hàng**: Ưu tiên đăng ký trước hoặc Tài liệu Metadata ID Khách hàng
  ; coi Đăng ký Khách hàng Động là phương án dự phòng tương thích
- **Xác nhận Sự đồng ý Người dùng**: MCP proxy sử dụng ID khách hàng bên thứ ba tĩnh
  phải lấy sự đồng ý từng khách hàng trước khi chuyển tiếp ủy quyền
- **Xác thực URI Chuyển hướng**: Xác thực nghiêm ngặt dựa trên danh sách trắng các điểm đến chuyển hướng
- **Bảo vệ Mã ủy quyền**: Mã ngắn hạn với việc thi hành sử dụng một lần
- **Xác minh Danh tính Khách hàng**: Xác thực mạnh mẽ thông tin và metadata của khách hàng

## 6. **Bảo mật Thực thi Công cụ**

### **Tách vùng và Cách ly**

**Cách ly Dựa trên Container:**
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

**Cách ly Quy trình:**
- **Ngữ cảnh Quy trình Riêng biệt**: Mỗi lần thực thi công cụ trong không gian quy trình cách ly
- **Giao tiếp liên Quy trình**: Cơ chế IPC an toàn với xác thực
- **Giám sát Quy trình**: Phân tích hành vi thời gian chạy và phát hiện bất thường
- **Áp dụng Tài nguyên**: Giới hạn cứng về CPU, bộ nhớ và các hoạt động I/O

### **Triển khai Quyền Đặc quyền Tối thiểu**

**Quản lý Quyền:** 
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

## 7. **Kiểm soát An ninh Chuỗi Cung ứng**

**Rủi ro OWASP MCP Giải quyết**: [MCP04 - Tấn công Chuỗi Cung ứng Phần mềm & Can thiệp Phụ thuộc](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Xác thực Phụ thuộc**

**Bảo mật Thành phần Toàn diện:**
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

### **Giám sát Liên tục**

**Phát hiện Mối đe dọa Chuỗi Cung ứng:**
- **Giám sát Sức khỏe Phụ thuộc**: Đánh giá liên tục tất cả các phụ thuộc về các vấn đề bảo mật
- **Tích hợp Thông tin Mối đe dọa**: Cập nhật thời gian thực về các mối đe dọa chuỗi cung ứng mới nổi
- **Phân tích Hành vi**: Phát hiện hành vi bất thường trong các thành phần bên ngoài
- **Phản hồi Tự động**: Hạn chế ngay lập tức các thành phần bị xâm phạm

## 8. **Kiểm soát Giám sát & Phát hiện**

**Rủi ro OWASP MCP Giải quyết**: [MCP08 - Thiếu Kiểm toán và Truyền dẫn dữ liệu](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Quản lý Thông tin và Sự kiện An ninh (SIEM)**

**Chiến lược Ghi nhật ký Toàn diện:**
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

### **Phát hiện Mối đe dọa Thời gian thực**

**Phân tích Hành vi:**
- **Phân tích Hành vi Người dùng (UBA)**: Phát hiện các mẫu truy cập người dùng bất thường
- **Phân tích Hành vi Thực thể (EBA)**: Giám sát hành vi máy chủ MCP và công cụ
- **Phát hiện Bất thường bằng Học máy**: Xác định các mối đe dọa bảo mật bằng AI
- **Phối hợp Thông tin Mối đe dọa**: Đối chiếu hoạt động quan sát với các mẫu tấn công đã biết

## 9. **Ứng phó Sự cố & Khôi phục**

### **Khả năng Phản hồi Tự động**

**Hành động Phản hồi Ngay lập tức:**
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

### **Khả năng Pháp y**

**Hỗ trợ Điều tra:**
- **Bảo tồn Dấu vết Kiểm toán**: Ghi nhật ký không thể thay đổi với tính toàn vẹn mật mã
- **Thu thập Bằng chứng**: Tự động thu thập các tài liệu an ninh liên quan
- **Tái tạo Dòng Thời gian**: Trình tự chi tiết các sự kiện dẫn đến sự cố bảo mật
- **Đánh giá Tác động**: Đánh giá phạm vi xâm phạm và lộ dữ liệu

## **Nguyên tắc Kiến trúc An ninh Chính**

### **Phòng thủ theo Chiều sâu**
- **Nhiều Lớp An ninh**: Không có điểm lỗi đơn lẻ trong kiến trúc an ninh
- **Kiểm soát Dự phòng**: Các biện pháp bảo mật chồng chéo cho các chức năng quan trọng
- **Cơ chế An toàn Dự phòng**: Mặc định an toàn khi hệ thống gặp lỗi hoặc tấn công

### **Triển khai Zero Trust**
- **Không Bao giờ Tin, Luôn Xác minh**: Xác thực liên tục tất cả thực thể và yêu cầu
- **Nguyên tắc Đặc quyền Tối thiểu**: Quyền truy cập tối thiểu cho tất cả thành phần
- **Phân đoạn Vi mô**: Kiểm soát mạng và truy cập chi tiết

### **Tiến hóa An ninh Liên tục**
- **Thích ứng Cảnh quan Mối đe dọa**: Cập nhật thường xuyên để giải quyết các mối đe dọa mới nổi
- **Hiệu quả Kiểm soát An ninh**: Đánh giá và cải tiến liên tục các biện pháp kiểm soát
- **Tuân thủ Quy định**: Phù hợp với các tiêu chuẩn an ninh MCP đang phát triển

---

## **Tài nguyên Triển khai**

### **Tài liệu MCP Chính thức**
- [Đặc tả MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Thực hành Tốt nhất về An ninh MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Đặc tả Ủy quyền MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Tài nguyên Bảo mật OWASP MCP**
- [Hướng dẫn Bảo mật OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 toàn diện với triển khai Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Những rủi ro bảo mật MCP chính thức của OWASP
- [Hội thảo Đỉnh cao MCP Bảo mật (Sherpa)](https://azure-samples.github.io/sherpa/) - Đào tạo bảo mật thực hành cho MCP trên Azure

### **Giải pháp Bảo mật Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Tiêu chuẩn An ninh**
- [Thực hành Tốt nhất OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 cho Mô Hình Ngôn Ngữ Lớn](https://genai.owasp.org/)

- [Khung An ninh mạng NIST](https://www.nist.gov/cyberframework)

---

> **Quan trọng:** Các kiểm soát bảo mật này phản ánh Đặc tả MCP
> `2026-07-28`. Luôn kiểm tra đối chiếu với
> [tài liệu chính thức hiện hành](https://modelcontextprotocol.io/specification/2026-07-28/)
> vì các tiêu chuẩn tiếp tục phát triển.

## Tiếp theo là gì

- Quay lại: [Tổng quan Mô-đun An ninh](./README.md)
- Tiếp tục tới: [Mô-đun 3: Bắt đầu](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->