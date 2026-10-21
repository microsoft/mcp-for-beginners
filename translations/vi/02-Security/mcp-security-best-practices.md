# Các Thực Hành Bảo Mật MCP Tốt Nhất - Cập Nhật Tháng 9 năm 2026

> **Quan trọng:** Tài liệu này phản ánh
> [Đặc Tả MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> và
> [Các Thực Hành Bảo Mật MCP Tốt Nhất](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) chính thức.

## 🏔️ Đào Tạo Bảo Mật Thực Hành

Để có kinh nghiệm triển khai thực tế, chúng tôi khuyến nghị **[Hội Thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - một chuyến thám hiểm có hướng dẫn toàn diện về bảo mật máy chủ MCP trên Azure. Hội thảo bao gồm tất cả 10 rủi ro OWASP MCP thông qua phương pháp "dễ bị tấn công → lợi dụng → sửa lỗi → xác nhận".

Tất cả các thực hành trong tài liệu này phù hợp với **[Hướng Dẫn Bảo Mật MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)** cho hướng dẫn triển khai riêng cho Azure.

## Các Thực Hành Bảo Mật Cần Thiết Cho Triển Khai MCP

Giao Thức Ngữ Cảnh Mô Hình giới thiệu các thách thức bảo mật riêng biệt vượt ra khỏi bảo mật phần mềm truyền thống. Những thực hành này giải quyết các yêu cầu nền tảng và các mối đe dọa đặc thù MCP bao gồm chèn prompt, đầu độc công cụ, chiếm đoạt state-handle, lỗi confused deputy, và lỗ hổng truyền token.





### **Yêu Cầu Bảo Mật BẮT BUỘC**

**Yêu Cầu Quan Trọng theo Đặc Tả MCP:**

> **KHÔNG ĐƯỢC**: Máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận bất kỳ token nào không được cấp rõ ràng cho máy chủ MCP
> 
> **PHẢI**: Máy chủ MCP triển khai phân quyền **PHẢI** xác thực TẤT CẢ các yêu cầu inbound
>  
> **KHÔNG ĐƯỢC**: Máy chủ MCP **KHÔNG ĐƯỢC** sử dụng session để xác thực
>
> **PHẢI**: Máy chủ proxy MCP sử dụng client ID bên thứ ba tĩnh **PHẢI**
> lấy sự đồng ý cho mỗi client MCP trước khi chuyển tiếp phân quyền

---

## 1. **Bảo Mật Token & Xác Thực**

**Kiểm Soát Xác Thực & Phân Quyền:**
   - **Đánh Giá Phân Quyền Nghiêm Ngặt**: Thực hiện đánh giá toàn diện logic phân quyền máy chủ MCP để đảm bảo chỉ người dùng và client dự định mới có thể truy cập tài nguyên
   - **Tích Hợp Nhà Cung Cấp Danh Tính Bên Ngoài**: Sử dụng các nhà cung cấp danh tính đã thiết lập như Microsoft Entra ID thay vì triển khai xác thực tùy chỉnh
   - **Xác Thực Đối Tượng Token**: Luôn xác thực token được cấp rõ ràng cho máy chủ MCP của bạn - tuyệt đối không chấp nhận token upstream
   - **Quản Lý Vòng Đời Token Đúng Cách**: Triển khai xoay vòng token bảo mật, chính sách hết hạn và ngăn chặn tấn công phát lại token

**Lưu Trữ Token An Toàn:**
   - Sử dụng Azure Key Vault hoặc kho lưu trữ bí mật tương tự cho tất cả các bí mật
   - Mã hóa token khi lưu trữ và trong quá trình truyền
   - Thường xuyên xoay vòng chứng chỉ và giám sát truy cập trái phép

## 2. **Bảo Mật State Handle & Truyền Tải**

**Thực Hành Bảo Mật Trạng Thái Ứng Dụng:**

- **Handles Trạng Thái Mờ Đục**: Sử dụng handles an toàn, không xác định trước cho trạng thái ứng dụng phân tán qua các yêu cầu
- **Ràng Buộc Theo Người Dùng**: Ràng buộc handles ở phía máy chủ với chủ thể đã xác thực và từ chối tái sử dụng chéo người dùng
- **Quản Lý Vòng Đời**: Hết hạn và thu hồi handles để giới hạn cửa sổ lỗ hổng
- **Phân Quyền Theo Yêu Cầu**: Không bao giờ coi handle trạng thái là xác thực; phân quyền từng yêu cầu sử dụng nó

**Bảo Mật Lớp Truyền Tải:**

- Yêu cầu HTTPS cho truyền HTTP từ xa trong môi trường sản xuất

- Cấu hình TLS hiện đại với xoay vòng và xác thực chứng chỉ đúng cách

## 3. **Bảo Vệ Trước Các Mối Đe Dọa Đặc Thù AI** 🤖

**Phòng Thủ Chèn Prompt:**

   - **Xác Thực Đầu Vào**: Kiểm tra và lọc sạch tất cả đầu vào để ngăn chặn tấn công chèn và lỗi confused deputy


**Phòng Ngừa Đầu Độc Công Cụ:**
   - **Xác Thực Metadata Công Cụ**: Thực hiện kiểm tra tính toàn vẹn cho định nghĩa công cụ và giám sát thay đổi bất thường
   - **Giám Sát Công Cụ Động**: Giám sát hành vi runtime và thiết lập cảnh báo cho các mẫu thực thi bất thường


## 4. **Kiểm Soát Truy Cập & Quyền Hạn**

**Nguyên Tắc Quyền Ít Nhất:**

   - Triển khai kiểm soát truy cập theo vai trò (RBAC) với quyền hạn chi tiết


**Kiểm Soát Quyền Trong Thời Gian Chạy:**
   - Áp dụng giới hạn tài nguyên để ngăn chặn tấn công làm cạn kiệt tài nguyên
   - Sử dụng cách ly container cho môi trường thực thi công cụ  


## 5. **An Toàn Nội Dung & Giám Sát**

**Triển Khai An Toàn Nội Dung:**

   - **Phân Tích Hành Vi**: Triển khai giám sát hành vi runtime để phát hiện bất thường trong thực thi máy chủ MCP và công cụ


**Giám Sát Liên Tục:**
   - Cảnh báo thời gian thực cho các mẫu bất thường và cố gắng truy cập trái phép  
   - Tích hợp với hệ thống SIEM cho quản lý sự kiện bảo mật tập trung


## 6. **Bảo Mật Chuỗi Cung Ứng**

**Xác Thực Thành Phần:**

   - **Xác Minh Nguồn Gốc**: Kiểm tra nguồn gốc, cấp phép và tính toàn vẹn của mô hình, nguồn dữ liệu và dịch vụ bên ngoài


**Dòng Phát Triển An Toàn:**
   - **Bảo Mật Nâng Cao GitHub**: Triển khai quét bí mật, phân tích phụ thuộc, và phân tích CodeQL tĩnh
   - **Bảo Mật CI/CD**: Tích hợp xác thực bảo mật trong toàn bộ quy trình triển khai tự động


## 7. **Bảo Mật OAuth & Ngăn Ngừa Confused Deputy**

**Triển Khai OAuth 2.1:**

    - **Đăng Ký Client**: Ưu tiên Tài liệu Metadata Client ID hoặc đăng ký trước; chỉ dùng Đăng Ký Client Động lỗi thời như lựa chọn tương thích

   - **Xác Thực Redirect URI**: Triển khai xác thực nghiêm ngặt URI chuyển hướng và định danh client

**Bảo Mật Proxy:**
   - Ngăn chặn bỏ qua phân quyền qua khai thác client ID tĩnh
   - Triển khai quy trình đồng ý phù hợp cho truy cập API bên thứ ba
   - Giám sát đánh cắp mã phân quyền và truy cập API trái phép

## 8. **Ứng Phó Sự Cố & Khôi Phục**

**Khả Năng Ứng Phó Nhanh:**
   - **Phản Ứng Tự Động**: Triển khai hệ thống tự động xoay vòng chứng chỉ và kiểm soát mối đe dọa
   - **Quy Trình Rollback**: Có khả năng nhanh chóng khôi phục cấu hình và thành phần đã biết là an toàn
   - **Khả Năng Pháp Y**: Lưu trữ chi tiết theo dấu audit và log để điều tra sự cố

**Giao Tiếp & Phối Hợp:**

   - Tích hợp với đội ứng phó sự cố của tổ chức
   - Thực hành mô phỏng và bài tập bảng định kỳ về sự cố bảo mật

## 9. **Tuân Thủ & Quản Trị**

**Tuân Thủ Quy Định:**
   - Đảm bảo triển khai MCP đáp ứng yêu cầu ngành nghề cụ thể (GDPR, HIPAA, SOC 2)
   - Triển khai phân loại dữ liệu và kiểm soát riêng tư cho xử lý dữ liệu AI
   - Duy trì tài liệu đầy đủ phục vụ kiểm tra tuân thủ

**Quản Lý Thay Đổi:**

   - Kiểm soát phiên bản và quy trình phê duyệt cho thay đổi cấu hình
   - Đánh giá tuân thủ định kỳ và phân tích khoảng cách

## 10. **Kiểm Soát Bảo Mật Nâng Cao**

**Kiến Trúc Zero Trust:**
   - **Không Bao Giờ Tin Tưởng, Luôn Xác Thực**: Xác thực liên tục người dùng, thiết bị và kết nối
   - **Phân Vùng Vi Mạng**: Kiểm soát mạng chi tiết cô lập từng thành phần MCP
   - **Truy Cập Có Điều Kiện**: Kiểm soát truy cập dựa trên rủi ro thích ứng với bối cảnh và hành vi hiện tại

**Bảo Vệ Ứng Dụng Thời Gian Chạy:**

   - **Giám Sát Hiệu Suất Ứng Dụng**: Giám sát bất thường về hiệu suất có thể cho thấy tấn công
   - **Chính Sách Bảo Mật Động**: Triển khai chính sách bảo mật thích ứng theo cảnh quan mối đe dọa hiện tại

## 11. **Tích Hợp Hệ Sinh Thái Bảo Mật Microsoft**

**Bảo Mật Microsoft Toàn Diện:**
   - **Microsoft Defender for Cloud**: Quản lý tư thế an ninh đám mây cho khối lượng công việc MCP
   - **Azure Sentinel**: SIEM và SOAR bản địa đám mây cho phát hiện mối đe dọa nâng cao
   - **Microsoft Purview**: Quản trị dữ liệu và tuân thủ cho luồng công việc AI và nguồn dữ liệu

**Quản Lý Danh Tính & Truy Cập:**

   - **Quản Lý Danh Tính Đặc Quyền (PIM)**: Truy cập đúng lúc và quy trình phê duyệt cho chức năng quản trị
   - **Bảo Vệ Danh Tính**: Truy cập có điều kiện dựa trên rủi ro và phản ứng tự động với mối đe dọa

## 12. **Tiến Hóa Bảo Mật Liên Tục**

**Luôn Cập Nhật:**
   - **Theo Dõi Đặc Tả**: Xem xét định kỳ các cập nhật đặc tả MCP và thay đổi hướng dẫn bảo mật
   - **Tình Báo Mối Đe Dọa**: Tích hợp nguồn mối đe dọa đặc thù AI và chỉ số xâm phạm
   - **Tham Gia Cộng Đồng Bảo Mật**: Tham gia tích cực vào cộng đồng bảo mật MCP và chương trình công bố lỗ hổng

**Bảo Mật Thích Nghi:**

   - **Phân Tích Bảo Mật Dự Đoán**: Triển khai mô hình dự báo để xác định mối đe dọa chủ động
   - **Tự Động Hóa Bảo Mật**: Cập nhật chính sách bảo mật tự động dựa trên tình báo mối đe dọa và thay đổi đặc tả

---

## **Tài Nguyên Bảo Mật Quan Trọng**

### **Tài Liệu Chính Thức MCP**
   - **Tự động hóa Bảo mật**: Cập nhật chính sách bảo mật tự động dựa trên tình báo mối đe dọa và thay đổi đặc tả

---

## **Nguồn lực Bảo mật Quan trọng**

### **Tài liệu chính thức MCP**
- [Đặc tả MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Thực hành Bảo mật MCP Tốt nhất](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Đặc tả Ủy quyền MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Tài nguyên Bảo mật OWASP MCP**
- [Hướng dẫn Bảo mật OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Tổng hợp OWASP MCP Top 10 với triển khai Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Các rủi ro bảo mật MCP chính thức của OWASP
- [Hội thảo Bảo mật MCP Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Đào tạo thực hành bảo mật MCP trên Azure

### **Giải pháp Bảo mật Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Tiêu chuẩn Bảo mật**
- [Thực hành Bảo mật OAuth 2.0 Tốt nhất (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 cho Mô hình Ngôn ngữ Lớn](https://genai.owasp.org/)
- [Khung Quản lý Rủi ro AI NIST](https://www.nist.gov/itl/ai-risk-management-framework)

### **Hướng dẫn Triển khai**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID với các Máy chủ MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Thông báo bảo mật:** Các thực hành bảo mật MCP phát triển nhanh chóng. Luôn kiểm tra
> với [đặc tả MCP](https://modelcontextprotocol.io/specification/2026-07-28/) hiện hành
> và [tài liệu bảo mật chính thức](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> trước khi triển khai.

## Tiếp theo là gì

- Đọc: [Các Biện pháp Kiểm soát Bảo mật MCP](./mcp-security-controls.md)
- Quay lại: [Tổng quan Module Bảo mật](./README.md)
- Tiếp tục tới: [Module 3: Bắt đầu](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->