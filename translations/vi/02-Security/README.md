# Bảo mật MCP: Bảo vệ Toàn diện cho Hệ thống AI

[![Các Thực hành Tốt nhất về Bảo mật MCP](../../../translated_images/vi/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Nhấn vào hình ảnh phía trên để xem video bài học này)_

Bảo mật là yếu tố nền tảng trong thiết kế hệ thống AI, đó là lý do tại sao chúng tôi ưu tiên nó là phần thứ hai. Điều này phù hợp với nguyên tắc **Bảo mật theo Thiết kế** của Microsoft từ [Sáng kiến Tương lai An toàn](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Giao thức Ngữ cảnh Mô hình (MCP) mang lại khả năng mạnh mẽ mới cho các ứng dụng điều khiển bởi AI trong khi giới thiệu các thách thức bảo mật đặc thù vượt ra ngoài các rủi ro phần mềm truyền thống. Hệ thống MCP đối mặt với các mối lo ngại bảo mật đã được xác lập (mã hóa an toàn, đặc quyền tối thiểu, bảo mật chuỗi cung ứng) cùng các mối đe dọa riêng biệt với AI bao gồm chèn lệnh (prompt injection), đầu độc công cụ, chiếm quyền phiên làm việc, tấn công confused deputy, lỗ hổng truyền token, và chỉnh sửa năng lực động.

Bài học này khám phá những rủi ro bảo mật quan trọng nhất trong các triển khai MCP—bao gồm xác thực, ủy quyền, cấp phép quá mức, chèn lệnh gián tiếp, bảo mật phiên làm việc, vấn đề confused deputy, quản lý token và lỗ hổng chuỗi cung ứng. Bạn sẽ học các biện pháp kiểm soát và thực hành tốt nhất có thể áp dụng để giảm thiểu các rủi ro này đồng thời tận dụng các giải pháp của Microsoft như Prompt Shields, Azure Content Safety, và GitHub Advanced Security để tăng cường bảo vệ triển khai MCP của bạn.

## Mục tiêu học tập

Đến cuối bài học này, bạn sẽ có khả năng:

- **Xác định các Mối đe dọa Đặc thù MCP**: Nhận dạng các rủi ro bảo mật độc nhất trong hệ thống MCP bao gồm chèn lệnh, đầu độc công cụ, cấp phép quá mức, chiếm quyền phiên, vấn đề confused deputy, lỗ hổng truyền token, và các rủi ro chuỗi cung ứng
- **Áp dụng Kiểm soát Bảo mật**: Triển khai các biện pháp giảm thiểu hiệu quả bao gồm xác thực mạnh mẽ, truy cập theo đặc quyền tối thiểu, quản lý token an toàn, kiểm soát bảo mật phiên làm việc và xác thực chuỗi cung ứng
- **Tận dụng Giải pháp Bảo mật Microsoft**: Hiểu và triển khai Microsoft Prompt Shields, Azure Content Safety và GitHub Advanced Security để bảo vệ khối lượng công việc MCP
- **Xác thực An toàn Công cụ**: Nhận thức tầm quan trọng của xác thực siêu dữ liệu công cụ, giám sát thay đổi động và phòng thủ trước các tấn công chèn lệnh gián tiếp
- **Kết hợp Thực hành Tốt nhất**: Kết hợp các nguyên tắc bảo mật căn bản đã được xác lập (mã an toàn, tăng cường máy chủ, zero trust) với các kiểm soát riêng biệt MCP để bảo vệ toàn diện

# Kiến trúc & Kiểm soát Bảo mật MCP

Các triển khai MCP hiện đại yêu cầu các giải pháp bảo mật nhiều lớp vừa giải quyết các mối đe dọa phần mềm truyền thống, vừa các mối đe dọa đặc thù AI. Đặc tả MCP đang phát triển nhanh chóng và dần hoàn thiện các kiểm soát bảo mật, đồng thời cho phép tích hợp tốt hơn với kiến trúc bảo mật doanh nghiệp và các thực hành tốt nhất đã được xác nhận.

Nghiên cứu từ [Báo cáo Phòng thủ Kỹ thuật số Microsoft](https://aka.ms/mddr) cho thấy **98% các vụ vi phạm được báo cáo có thể được ngăn chặn bằng vệ sinh bảo mật mạnh mẽ**. Chiến lược bảo vệ hiệu quả nhất kết hợp các thực hành bảo mật nền tảng với các kiểm soát riêng biệt MCP—các biện pháp bảo mật cơ bản vẫn đóng vai trò quyết định trong việc giảm thiểu tổng thể rủi ro bảo mật.

## Bối cảnh Bảo mật Hiện tại

> **Ghi chú:** Chương này kết hợp các kiểm soát bảo mật MCP đã được xác lập cùng với
> hướng dẫn ủy quyền **MCP Specification 2026-07-28** hiện hành. Luôn tham khảo
> [Đặc tả MCP](https://modelcontextprotocol.io/specification/2026-07-28/), 
> [kho GitHub MCP](https://github.com/modelcontextprotocol), và 
> [tài liệu thực hành tốt nhất bảo mật](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) 
> khi triển khai mã có yêu cầu bảo mật cao.

> **Cập nhật ủy quyền:** MCP `2026-07-28` yêu cầu các client xác thực
> tham số `iss` trong phản hồi ủy quyền (RFC 9207) và liên kết các
> chứng thực đã đăng ký với máy chủ ủy quyền phát hành. Đăng ký Client động
> bị loại bỏ; các triển khai mới nên sử dụng Tài liệu Metadata Client ID.
> Xem [Những thay đổi trong MCP: Đặc tả 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> để biết danh sách đầy đủ các thay đổi ủy quyền.

## 🏔️ Hội nghị Bảo mật MCP (Sherpa)

Đối với **đào tạo bảo mật thực hành**, chúng tôi khuyên bạn tham gia **Hội nghị Bảo mật MCP (Sherpa)** - một hành trình hướng dẫn toàn diện để bảo vệ các máy chủ MCP trên Microsoft Azure.

### Tổng quan Hội nghị

[Hội nghị Bảo mật MCP](https://azure-samples.github.io/sherpa/) cung cấp đào tạo bảo mật thiết thực, triển khai theo phương pháp "lỗ hổng → khai thác → sửa chữa → xác thực" đã được chứng minh. Bạn sẽ:

- **Học qua Việc Phá hủy**: Trải nghiệm các lỗ hổng trực tiếp bằng cách khai thác các máy chủ cố tình không an toàn
- **Sử dụng Bảo mật bản địa Azure**: Tận dụng Azure Entra ID, Key Vault, API Management, và AI Content Safety
- **Theo Phòng thủ nhiều lớp**: Tiến qua các trại xây dựng nhiều lớp bảo mật toàn diện
- **Áp dụng Tiêu chuẩn OWASP**: Mỗi kỹ thuật liên kết với [Hướng dẫn Bảo mật MCP Azure của OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Nhận mã Sản xuất**: Kết thúc với các triển khai hoạt động và được kiểm thử

### Lộ trình Hành trình

| Trại | Trọng tâm | Rủi ro OWASP được Bao phủ |
|------|-------|---------------------|
| **Trại Cơ bản** | Những điều cơ bản MCP & lỗ hổng xác thực | MCP01, MCP07 |
| **Trại 1: Danh tính** | OAuth 2.1, Danh tính Quản lý Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Trại 2: Cổng giao tiếp** | Quản lý API, điểm cuối riêng tư, quản trị | MCP02, MCP06, MCP07, MCP09 |
| **Trại 3: An ninh I/O** | Chèn lệnh, bảo vệ PII, an toàn nội dung | MCP03, MCP05, MCP06, MCP10 |
| **Trại 4: Giám sát** | Phân tích nhật ký, bảng điều khiển, phát hiện mối đe dọa | MCP04, MCP08 |
| **Đỉnh Hội nghị** | Kiểm tra tích hợp Đội Đỏ / Đội Xanh | Tất cả |

**Bắt đầu tại**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Top 10 Rủi ro Bảo mật OWASP MCP

[Hướng dẫn Bảo mật MCP Azure của OWASP](https://microsoft.github.io/mcp-azure-security-guide/) trình bày mười rủi ro bảo mật quan trọng nhất cho các triển khai MCP:

| Rủi ro | Mô tả | Giải pháp Azure |
|------|-------------|------------------|
| **MCP01** | Quản lý Token sai & Lộ Thông tin Bí mật | Azure Key Vault, Danh tính Quản lý |
| **MCP02** | Leo thang đặc quyền qua Scope Creep | RBAC, Truy cập Có điều kiện |
| **MCP03** | Đầu độc Công cụ | Xác thực công cụ, xác minh tính toàn vẹn |
| **MCP04** | Tấn công Chuỗi cung ứng phần mềm & Chỉnh sửa phụ thuộc | GitHub Advanced Security, quét phụ thuộc |
| **MCP05** | Chèn & Thực thi lệnh | Xác thực đầu vào, sandboxing |
| **MCP06** | Đảo ngược luồng ý định | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Xác thực & Ủy quyền không đủ | Azure Entra ID, OAuth 2.1 với PKCE |
| **MCP08** | Thiếu kiểm toán và giám sát | Azure Monitor, Application Insights |
| **MCP09** | Máy chủ MCP bóng tối | Quản trị API Center, cô lập mạng |
| **MCP10** | Chèn ngữ cảnh & Chia sẻ quá mức | Phân loại dữ liệu, lộ mức độ tối thiểu |

### Sự tiến hóa của Xác thực MCP

Đặc tả MCP đã phát triển đáng kể trong phương pháp xác thực và ủy quyền:

- **Phương pháp ban đầu**: Các đặc tả đầu yêu cầu nhà phát triển triển khai máy chủ xác thực tùy chỉnh, máy chủ MCP hoạt động như OAuth 2.0 Authorization Server quản lý xác thực người dùng trực tiếp
- **Tiêu chuẩn hiện tại (`2026-07-28`)**: Máy chủ MCP có thể ủy quyền xác thực
  cho các nhà cung cấp danh tính bên ngoài như Microsoft Entra ID. Client cũng phải
  áp dụng các yêu cầu xác thực nhà phát hành và liên kết chứng thực hiện hành.
- **Bảo mật lớp truyền tải**: Hỗ trợ nâng cao cho các cơ chế truyền tải an toàn với các mẫu xác thực phù hợp cho kết nối cục bộ (STDIO) và từ xa (Streamable HTTP)

## An ninh Xác thực & Ủy quyền

### Thách thức Bảo mật Hiện tại

Các triển khai MCP hiện đại đối mặt với nhiều thách thức xác thực và ủy quyền:

### Rủi ro & Các vectơ tấn công

- **Logic Ủy quyền cấu hình sai**: Việc triển khai ủy quyền lỗi trong máy chủ MCP có thể làm lộ dữ liệu nhạy cảm và áp dụng sai kiểm soát truy cập
- **Xâm phạm Token OAuth**: Trộm token máy chủ MCP cục bộ cho phép tấn công giả danh máy chủ và truy cập dịch vụ hạ nguồn
- **Lỗ hổng Token Passthrough**: Xử lý token không đúng cách gây bỏ qua kiểm soát bảo mật và mất trách nhiệm
- **Cấp phép Quá mức**: Máy chủ MCP có đặc quyền quá mức vi phạm nguyên tắc đặc quyền thấp nhất và mở rộng bề mặt tấn công

#### Token Passthrough: Một Mô hình chống chỉ định quan trọng

**Token passthrough bị nghiêm cấm rõ ràng** trong đặc tả ủy quyền MCP hiện tại do các hậu quả bảo mật nghiêm trọng:

##### Vượt qua Kiểm soát Bảo mật
- Máy chủ MCP và API hạ nguồn triển khai các kiểm soát bảo mật quan trọng (giới hạn tần suất, xác thực yêu cầu, giám sát lưu lượng) phụ thuộc vào việc xác thực token đúng cách
- Việc client trực tiếp sử dụng token cho API bỏ qua các biện pháp bảo vệ thiết yếu này, làm suy yếu kiến trúc bảo mật

##### Khó khăn trong Trách nhiệm & Kiểm toán  
- Máy chủ MCP không thể phân biệt các client dùng token cấp bởi upstream, làm đứt gãy truy vết kiểm toán
- Nhật ký máy chủ tài nguyên hạ nguồn hiển thị nguồn yêu cầu sai lệch thay vì trung gian máy chủ MCP thực tế
- Việc điều tra sự cố và kiểm toán tuân thủ trở nên phức tạp hơn nhiều

##### Rủi ro Rò rỉ Dữ liệu
- Các yêu cầu token không được xác thực cho phép kẻ tấn công có token bị đánh cắp lợi dụng máy chủ MCP làm proxy để exfiltrate dữ liệu
- Vi phạm ranh giới tin cậy tạo điều kiện truy cập trái phép vượt qua các kiểm soát bảo mật dự kiến

##### Vectơ Tấn công Đa dịch vụ
- Token bị xâm phạm được chấp nhận bởi nhiều dịch vụ kích hoạt di chuyển bên trong các hệ thống kết nối
- Các giả định tin cậy giữa dịch vụ có thể bị vi phạm khi nguồn token không thể xác thực

### Kiểm soát & Biện pháp Giảm thiểu Bảo mật

**Yêu cầu Bảo mật Quan trọng:**

> **BẮT BUỘC**: Máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận bất kỳ token nào không được cấp riêng cho máy chủ MCP đó

#### Kiểm soát Xác thực & Ủy quyền

- **Đánh giá Ủy quyền nghiêm ngặt**: Thực hiện kiểm toán toàn diện logic ủy quyền máy chủ MCP để đảm bảo chỉ người dùng và client dự định mới có thể truy cập tài nguyên nhạy cảm
  - **Hướng dẫn triển khai**: [Azure API Management làm Cổng xác thực cho Máy chủ MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Tích hợp danh tính**: [Sử dụng Microsoft Entra ID cho Xác thực Máy chủ MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Quản lý Token An toàn**: Triển khai [thực hành tốt nhất về xác thực và vòng đời token của Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Xác thực các yêu cầu audience token khớp với danh tính máy chủ MCP
  - Thực thi chính sách xoay vòng và hết hạn token hợp lý
  - Ngăn chặn tấn công phát lại token và sử dụng trái phép

- **Lưu trữ Token được Bảo vệ**: Lưu trữ token an toàn với mã hóa cả khi nghỉ và truyền
  - **Thực hành tốt nhất**: [Hướng dẫn Lưu trữ và Mã hóa Token An toàn](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Triển khai Kiểm soát Truy cập

- **Nguyên tắc Đặc quyền Tối thiểu**: Cấp cho máy chủ MCP chỉ các quyền tối thiểu cần thiết cho chức năng dự kiến
  - Xem xét và cập nhật định kỳ để ngăn chặn leo thang đặc quyền
  - **Tài liệu Microsoft**: [Truy cập An toàn theo Đặc quyền Tối thiểu](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kiểm soát Truy cập theo Vai trò (RBAC)**: Triển khai phân quyền vai trò chi tiết
  - Giới hạn vai trò chặt chẽ theo tài nguyên và hành động cụ thể
  - Tránh cấp phép rộng rãi hoặc không cần thiết làm mở rộng bề mặt tấn công

- **Giám sát Cấp phép Liên tục**: Thực hiện kiểm toán và giám sát truy cập liên tục
  - Giám sát các mẫu sử dụng quyền để phát hiện bất thường
  - Khắc phục kịp thời các quyền quá mức hoặc không sử dụng

## Các Mối đe dọa An ninh Đặc thù AI

### Tấn công Chèn lệnh & Thao tác Công cụ

Các triển khai MCP hiện đại đối mặt với các vectơ tấn công AI tinh vi mà các biện pháp bảo mật truyền thống không thể giải quyết đầy đủ:

#### **Chèn lệnh gián tiếp (Chèn lệnh chéo miền)**

**Chèn lệnh gián tiếp** là một trong những lỗ hổng nghiêm trọng nhất trong các hệ thống AI được MCP hỗ trợ. Kẻ tấn công nhúng các hướng dẫn độc hại bên trong nội dung ngoài—tài liệu, trang web, email hoặc nguồn dữ liệu—mà hệ thống AI xử lý sau đó như các lệnh hợp lệ.

**Kịch bản tấn công:**
- **Chèn vào tài liệu**: Lệnh độc hại ẩn trong các tài liệu được xử lý kích hoạt hành động AI không mong muốn
- **Khai thác nội dung web**: Trang web bị xâm nhập chứa lệnh nhúng thao túng hành vi AI khi được thu thập dữ liệu
- **Tấn công qua email**: Lệnh độc hại trong email khiến trợ lý AI rò rỉ thông tin hoặc thực hiện hành động trái phép
- **Nhiễm nguồn dữ liệu**: Cơ sở dữ liệu hoặc API bị xâm nhập cung cấp nội dung bị nhiễm cho AI

**Tác động thực tế**: Các tấn công này có thể dẫn đến rò rỉ dữ liệu, vi phạm quyền riêng tư, tạo nội dung độc hại và thao túng tương tác người dùng. Để biết phân tích chi tiết, xem [Chèn lệnh trong MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Sơ đồ Tấn công Chèn lệnh](../../../translated_images/vi/prompt-injection.ed9fbfde297ca877.webp)

#### **Tấn công Đầu độc Công cụ**

**Đầu độc Công cụ** nhắm vào metadata định nghĩa công cụ MCP, khai thác cách các mô hình ngôn ngữ lớn (LLMs) diễn giải mô tả và tham số công cụ để đưa ra quyết định thực thi.

**Cơ chế tấn công:**
- **Chèn Metadata**: Kẻ tấn công tiêm các hướng dẫn độc hại vào mô tả công cụ, định nghĩa tham số hoặc ví dụ sử dụng
- **Lệnh vô hình**: Lệnh ẩn trong metadata công cụ được xử lý bởi mô hình AI nhưng không thấy được bởi người dùng
- **Sửa đổi Công cụ Động ("Rug Pulls")**: Công cụ được người dùng phê duyệt sau đó bị sửa đổi để thực hiện hành động độc hại mà người dùng không hay biết
- **Chèn tham số**: Nội dung độc hại nhúng trong sơ đồ tham số công cụ ảnh hưởng đến hành vi mô hình


**Rủi ro Máy chủ lưu trữ**: Các máy chủ MCP từ xa có rủi ro cao do định nghĩa công cụ có thể được cập nhật sau khi người dùng ban đầu phê duyệt, tạo nên các tình huống công cụ trước đây an toàn trở nên độc hại. Để phân tích toàn diện, xem [Các Cuộc tấn công Đầu độc Công cụ (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/vi/tool-injection.3b0b4a6b24de6bef.webp)

#### **Các Vectơ Tấn công AI Bổ sung**

- **Chèn Lời nhắc Chéo Miền (XPIA)**: Các cuộc tấn công tinh vi lợi dụng nội dung từ nhiều miền để vượt qua các kiểm soát bảo mật
- **Thay đổi Năng lực Động**: Thay đổi theo thời gian thực các khả năng công cụ để thoát khỏi đánh giá bảo mật ban đầu
- **Đầu độc Cửa sổ Ngữ cảnh**: Các cuộc tấn công thao túng cửa sổ ngữ cảnh lớn để che giấu các chỉ dẫn độc hại
- **Tấn công Lẫn lộn Mẫu**: Khai thác hạn chế của mô hình để tạo ra hành vi không thể đoán trước hoặc không an toàn


### Tác động Rủi ro Bảo mật AI

**Hậu quả Tác động Cao:**
- **Rò rỉ Dữ liệu**: Truy cập và đánh cắp dữ liệu doanh nghiệp hoặc cá nhân nhạy cảm trái phép
- **Vi phạm Quyền riêng tư**: Tiết lộ thông tin cá nhân nhận dạng (PII) và dữ liệu kinh doanh mật
- **Can thiệp Hệ thống**: Thay đổi không mong muốn đối với các hệ thống và quy trình quan trọng
- **Đánh cắp Thông tin Đăng nhập**: Xâm phạm token xác thực và thông tin đăng nhập dịch vụ
- **Di chuyển Ngang hàng**: Sử dụng các hệ thống AI bị xâm phạm như điểm trung gian cho các cuộc tấn công mạng rộng lớn hơn

### Giải pháp Bảo mật AI của Microsoft

#### **AI Prompt Shields: Bảo vệ Nâng cao Chống Tấn công Chèn Lời nhắc**

Microsoft **AI Prompt Shields** cung cấp phòng thủ toàn diện chống lại cả tấn công chèn lời nhắc trực tiếp và gián tiếp thông qua nhiều lớp bảo mật:

##### **Cơ chế Bảo vệ Cốt lõi:**

1. **Phát hiện & Lọc Nâng cao**
   - Thuật toán học máy và kỹ thuật NLP phát hiện chỉ dẫn độc hại trong nội dung bên ngoài
   - Phân tích thời gian thực các tài liệu, trang web, email và nguồn dữ liệu để phát hiện mối đe dọa ẩn giấu
   - Hiểu biết về ngữ cảnh giữa mẫu lời nhắc hợp pháp và độc hại

2. **Kỹ thuật Phân loại Nổi bật**  
   - Phân biệt giữa chỉ dẫn hệ thống đáng tin cậy và dữ liệu đầu vào bên ngoài có thể bị xâm phạm
   - Phương pháp biến đổi văn bản nâng cao tính liên quan mô hình đồng thời cô lập nội dung độc hại
   - Giúp hệ thống AI duy trì cấp bậc chỉ dẫn thích hợp và bỏ qua các lệnh bị chèn

3. **Hệ thống Phân cách & Đánh dấu Dữ liệu**
   - Định nghĩa rõ ràng ranh giới giữa các thông điệp hệ thống đáng tin cậy và văn bản đầu vào bên ngoài
   - Các dấu hiệu đặc biệt làm nổi bật ranh giới giữa nguồn dữ liệu tin cậy và không tin cậy
   - Phân tách rõ ràng tránh nhầm lẫn chỉ dẫn và thực thi lệnh trái phép

4. **Tình báo Mối đe dọa Liên tục**
   - Microsoft liên tục giám sát các mẫu tấn công mới và cập nhật các biện pháp phòng thủ
   - Săn tìm mối đe dọa chủ động cho kỹ thuật chèn và vectơ tấn công mới
   - Cập nhật định kỳ mô hình bảo mật để duy trì hiệu quả chống lại các mối đe dọa phát triển

5. **Tích hợp Azure Content Safety**
   - Một phần của bộ công cụ Azure AI Content Safety toàn diện
   - Phát hiện bổ sung các nỗ lực jailbreak, nội dung độc hại và vi phạm chính sách bảo mật
   - Kiểm soát bảo mật thống nhất trên các thành phần ứng dụng AI

**Tài nguyên triển khai**: [Tài liệu Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/vi/prompt-shield.ff5b95be76e9c78c.webp)


## Các Mối đe dọa Bảo mật MCP Nâng cao

### Lỗ hổng Chiếm đoạt Phiên làm việc (Session Hijacking)

**Chiếm đoạt phiên làm việc** là vectơ tấn công nghiêm trọng trong các triển khai MCP có trạng thái, nơi các bên trái phép lấy được và lạm dụng các định danh phiên hợp pháp để giả mạo khách hàng và thực hiện các hành động trái phép.

#### **Tình huống & Rủi ro Tấn công**

- **Chèn Lời nhắc Chiếm đoạt Phiên**: Kẻ tấn công với ID phiên đánh cắp chèn sự kiện độc hại vào các máy chủ chia sẻ trạng thái phiên, có thể kích hoạt hành động gây hại hoặc truy cập dữ liệu nhạy cảm
- **Giả mạo Trực tiếp**: ID phiên đánh cắp cho phép gọi máy chủ MCP trực tiếp bỏ qua xác thực, coi kẻ tấn công là người dùng hợp pháp
- **Luồng Dữ liệu Có thể Tái Tạo Bị Xâm phạm**: Kẻ tấn công có thể kết thúc các yêu cầu trước thời hạn, khiến khách hàng hợp pháp tiếp tục với nội dung tiềm ẩn độc hại

#### **Kiểm soát Bảo mật Quản lý Phiên**

**Yêu cầu Quan trọng:**
- **Xác minh Ủy quyền**: Máy chủ MCP triển khai ủy quyền **PHẢI** xác minh TẤT CẢ yêu cầu đầu vào và **KHÔNG ĐƯỢC** dựa vào phiên để xác thực
- **Tạo Phiên An toàn**: Sử dụng ID phiên ngẫu nhiên, không định trước, được tạo bằng bộ sinh số ngẫu nhiên bảo mật
- **Ràng buộc theo Người dùng**: Ràng buộc ID phiên với thông tin người dùng cụ thể theo định dạng như `<user_id>:<session_id>` để ngăn chặn lạm dụng phiên giữa người dùng
- **Quản lý Vòng đời Phiên**: Triển khai hết hạn, xoay vòng, và hủy bỏ thích hợp để giới hạn cửa sổ lỗ hổng
- **Bảo mật Giao tiếp**: Yêu cầu HTTPS cho tất cả truyền thông để ngăn chặn đánh cắp ID phiên

### Vấn đề Đại lý Bối rối (Confused Deputy)

Vấn đề **đại lý bối rối** xảy ra khi các máy chủ MCP đóng vai trò proxy xác thực giữa khách hàng và dịch vụ bên thứ ba, tạo cơ hội vượt qua ủy quyền thông qua khai thác ID khách hàng tĩnh.

#### **Cơ chế & Rủi ro Tấn công**

- **Vượt qua Chấp thuận dựa trên Cookie**: Xác thực người dùng trước đó tạo cookie chấp thuận mà kẻ tấn công lợi dụng qua các yêu cầu ủy quyền độc hại với URI chuyển hướng giả mạo
- **Đánh cắp Mã ủy quyền**: Cookie chấp thuận tồn tại có thể khiến máy chủ ủy quyền bỏ qua màn hình chấp thuận, chuyển mã đến điểm cuối do kẻ tấn công kiểm soát  
- **Truy cập API Không được phép**: Mã ủy quyền đánh cắp cho phép trao đổi token và giả mạo người dùng mà không cần phê duyệt rõ ràng

#### **Chiến lược Giảm thiểu**

**Kiểm soát Bắt buộc:**
- **Yêu cầu Chấp thuận Rõ ràng**: Proxy MCP sử dụng ID khách hàng tĩnh **PHẢI** lấy sự đồng ý người dùng cho mỗi khách hàng đăng ký động
- **Triển khai Bảo mật OAuth 2.1**: Tuân theo các thực tiễn tốt nhất bảo mật OAuth hiện tại bao gồm PKCE (Proof Key for Code Exchange) cho mọi yêu cầu ủy quyền
- **Xác thực Khách hàng Nghiêm ngặt**: Thực hiện xác thực chặt chẽ URI chuyển hướng và định danh khách hàng để ngăn chặn khai thác

### Lỗ hổng Chuyển Tiếp Token  

**Chuyển tiếp token** là một mẫu không nên áp dụng, nơi máy chủ MCP chấp nhận token của khách hàng mà không xác thực đầy đủ và chuyển tiếp chúng đến API hạ nguồn, vi phạm các đặc tả ủy quyền MCP.

#### **Hệ quả Bảo mật**

- **Vượt qua Kiểm soát**: Sử dụng token trực tiếp từ khách hàng đến API bỏ qua các kiểm soát giới hạn tỷ lệ, xác thực, và giám sát quan trọng
- **Hủy hoại Dấu vết Kiểm toán**: Token cấp trên làm không thể xác định khách hàng, phá vỡ khả năng điều tra sự cố
- **Rò rỉ Dữ liệu qua Proxy**: Token không xác thực cho phép kẻ ác sử dụng máy chủ làm proxy truy cập dữ liệu trái phép
- **Vi phạm Ranh giới Tin cậy**: Dịch vụ hạ nguồn dựa trên giả định tin cậy có thể bị vi phạm khi không xác thực được nguồn token
- **Mở rộng Tấn công Đa dịch vụ**: Token bị xâm phạm chấp nhận trên nhiều dịch vụ cho phép di chuyển ngang

#### **Kiểm soát Bảo mật Bắt buộc**

**Yêu cầu Không thể Thỏa hiệp:**
- **Xác thực Token**: Máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận token không do máy chủ MCP cấp rõ ràng
- **Xác minh Đối tượng Token**: Luôn xác thực đối tượng token khớp với định danh máy chủ MCP
- **Vòng đời Token Thích hợp**: Triển khai token truy cập thời gian ngắn với chính sách xoay vòng bảo mật


## Bảo mật Chuỗi Cung ứng cho Hệ thống AI

Bảo mật chuỗi cung ứng đã phát triển vượt qua các phụ thuộc phần mềm truyền thống để bao gồm toàn bộ hệ sinh thái AI. Các triển khai MCP hiện đại phải xác thực và giám sát nghiêm ngặt tất cả thành phần liên quan AI, vì mỗi thành phần tiềm ẩn các điểm yếu có thể làm suy yếu tính toàn vẹn hệ thống.

### Các Thành phần Chuỗi Cung ứng AI Mở rộng

**Phụ thuộc Phần mềm Truyền thống:**
- Thư viện và khung mã nguồn mở
- Hình ảnh container và hệ thống cơ sở  
- Công cụ phát triển và dây chuyền xây dựng
- Thành phần và dịch vụ cơ sở hạ tầng

**Yếu tố Chuỗi Cung ứng AI Cụ thể:**
- **Mô hình Nền tảng**: Mô hình tiền huấn luyện từ nhiều nhà cung cấp cần xác thực nguồn gốc
- **Dịch vụ Nhúng (Embedding Services)**: Dịch vụ vector hóa và tìm kiếm ngữ nghĩa bên ngoài
- **Nhà cung cấp Ngữ cảnh**: Nguồn dữ liệu, cơ sở tri thức, và kho tài liệu  
- **API Bên thứ ba**: Dịch vụ AI bên ngoài, pipeline ML, và điểm xử lý dữ liệu
- **Sản phẩm Mô hình**: Trọng số, cấu hình, và các biến thể mô hình được tinh chỉnh
- **Nguồn Dữ liệu Huấn luyện**: Bộ dữ liệu để huấn luyện và tinh chỉnh mô hình

### Chiến lược Bảo mật Chuỗi Cung ứng Toàn diện

#### **Xác thực & Tin cậy Thành phần**
- **Xác minh Nguồn gốc**: Xác minh nguồn gốc, bản quyền, và tính toàn vẹn của tất cả thành phần AI trước khi tích hợp
- **Đánh giá Bảo mật**: Thực hiện quét lỗ hổng và đánh giá bảo mật cho mô hình, nguồn dữ liệu, và dịch vụ AI
- **Phân tích Danh tiếng**: Đánh giá hồ sơ bảo mật và thực tiễn của nhà cung cấp dịch vụ AI
- **Xác minh Tuân thủ**: Đảm bảo tất cả thành phần đáp ứng yêu cầu bảo mật và quy định của tổ chức

#### **Dây chuyền Triển khai An toàn**  
- **Bảo mật CI/CD Tự động**: Tích hợp quét bảo mật xuyên suốt dây chuyền triển khai tự động
- **Tính Toàn vẹn Sản phẩm**: Triển khai xác thực mật mã cho tất cả sản phẩm triển khai (mã, mô hình, cấu hình)
- **Triển khai Giai đoạn**: Sử dụng chiến lược triển khai tiến triển với đánh giá bảo mật tại mỗi giai đoạn
- **Kho Lưu trữ Sản phẩm Tin cậy**: Triển khai chỉ từ các kho lưu trữ sản phẩm đã được xác minh và an toàn

#### **Giám sát & Phản ứng Liên tục**
- **Quét Phụ thuộc**: Giám sát liên tục lỗ hổng cho tất cả phụ thuộc phần mềm và thành phần AI
- **Giám sát Mô hình**: Đánh giá liên tục hành vi mô hình, trôi hiệu năng, và bất thường bảo mật
- **Theo dõi Tình trạng Dịch vụ**: Giám sát dịch vụ AI bên ngoài về khả dụng, sự cố bảo mật, và thay đổi chính sách
- **Tích hợp Tình báo Mối đe dọa**: Kết hợp nguồn dữ liệu tình báo mối đe dọa đặc thù cho AI và ML

#### **Kiểm soát Truy cập & Quyền Tối thiểu**
- **Quyền Cấp theo Thành phần**: Giới hạn truy cập mô hình, dữ liệu và dịch vụ dựa trên nhu cầu kinh doanh
- **Quản lý Tài khoản Dịch vụ**: Triển khai tài khoản dịch vụ riêng biệt với quyền tối thiểu cần thiết
- **Phân đoạn Mạng**: Cách ly các thành phần AI và giới hạn truy cập mạng giữa các dịch vụ
- **Kiểm soát Cổng API**: Sử dụng cổng API tập trung để kiểm soát và giám sát truy cập dịch vụ AI bên ngoài

#### **Phản ứng & Khôi phục Sự cố**
- **Quy trình Phản ứng Nhanh**: Quy trình có sẵn để vá hoặc thay thế thành phần AI bị xâm phạm
- **Xoay vòng Thông tin Đăng nhập**: Hệ thống tự động xoay vòng bí mật, khóa API và thông tin đăng nhập dịch vụ
- **Khả năng Khôi phục**: Khả năng nhanh chóng quay lại phiên bản AI đã biết là an toàn trước đó
- **Phục hồi Vi phạm Chuỗi Cung ứng**: Quy trình cụ thể đáp ứng sự cố xâm phạm dịch vụ AI cấp trên

### Công cụ & Tích hợp Bảo mật Microsoft

**GitHub Advanced Security** cung cấp bảo vệ chuỗi cung ứng toàn diện bao gồm:
- **Quét Bí mật**: Phát hiện tự động thông tin đăng nhập, khóa API, và token trong kho mã 
- **Quét Phụ thuộc**: Đánh giá lỗ hổng cho phụ thuộc và thư viện mã nguồn mở
- **Phân tích CodeQL**: Phân tích mã tĩnh nhằm phát hiện lỗ hổng bảo mật và lỗi mã hóa
- **Cái nhìn Chuỗi Cung ứng**: Hiển thị trạng thái sức khỏe và bảo mật phụ thuộc

**Tích hợp Azure DevOps & Azure Repos:**
- Tích hợp quét bảo mật liền mạch trên các nền tảng phát triển Microsoft
- Kiểm tra bảo mật tự động trong Azure Pipelines cho khối lượng công việc AI
- Thực thi chính sách triển khai thành phần AI an toàn

**Thực tiễn Nội bộ Microsoft:**
Microsoft áp dụng thực tiễn bảo mật chuỗi cung ứng rộng rãi trên tất cả sản phẩm. Tìm hiểu về các cách tiếp cận đã được chứng minh tại [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Thực hành Bảo mật Nền tảng Tốt nhất

Các triển khai MCP kế thừa và phát triển dựa trên vị thế bảo mật hiện có của tổ chức bạn. Tăng cường các thực hành bảo mật nền tảng sẽ nâng cao đáng kể an toàn tổng thể của hệ thống AI và các triển khai MCP.

### Các Nguyên tắc Bảo mật Cốt lõi

#### **Thực hành Phát triển An toàn**
- **Tuân thủ OWASP**: Bảo vệ chống lại [10 Lỗ hổng Hàng đầu OWASP](https://owasp.org/www-project-top-ten/) của ứng dụng web
- **Bảo vệ Cụ thể cho AI**: Triển khai kiểm soát cho [10 Lỗ hổng Hàng đầu OWASP cho LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Quản lý Bí mật An toàn**: Sử dụng kho chuyên dụng cho token, khóa API, và dữ liệu cấu hình nhạy cảm
- **Mã hóa Toàn bộ**: Triển khai giao tiếp an toàn trên tất cả thành phần ứng dụng và luồng dữ liệu
- **Xác thực Đầu vào**: Kiểm tra nghiêm ngặt mọi đầu vào người dùng, tham số API, và nguồn dữ liệu

#### **Tăng cường Hạ tầng**
- **Xác thực Đa yếu tố (MFA)**: Bắt buộc MFA cho tất cả tài khoản quản trị và dịch vụ
- **Quản lý Vá lỗi**: Vá lỗi tự động và kịp thời cho hệ điều hành, khung công tác và phụ thuộc  
- **Tích hợp Nhà cung cấp Danh tính**: Quản lý danh tính tập trung qua nhà cung cấp danh tính doanh nghiệp (Microsoft Entra ID, Active Directory)
- **Phân đoạn Mạng**: Cách ly hợp lý các thành phần MCP để hạn chế khả năng di chuyển ngang
- **Nguyên tắc Quyền Tối thiểu**: Phân quyền tối thiểu cần thiết cho mọi thành phần và tài khoản hệ thống

#### **Giám sát & Phát hiện Bảo mật**
- **Ghi nhật ký Toàn diện**: Ghi chi tiết hoạt động ứng dụng AI, bao gồm tương tác client-server MCP
- **Tích hợp SIEM**: Trung tâm quản lý thông tin và sự kiện bảo mật để phát hiện bất thường
- **Phân tích Hành vi**: Giám sát bằng AI để phát hiện mẫu hành vi bất thường của hệ thống và người dùng
- **Tình báo Mối đe dọa**: Kết hợp nguồn dữ liệu mối đe dọa bên ngoài và chỉ số xâm phạm (IOC)
- **Phản ứng Sự cố**: Quy trình xác định, phản ứng và phục hồi sự cố bảo mật rõ ràng

#### **Kiến trúc Zero Trust**
- **Không bao giờ tin, luôn xác minh**: Xác minh liên tục người dùng, thiết bị, và kết nối mạng
- **Phân đoạn vi mô**: Kiểm soát mạng chi tiết cô lập từng khối lượng công việc và dịch vụ
- **Bảo mật Tập trung danh tính**: Chính sách bảo mật dựa trên danh tính xác thực thay vì vị trí mạng
- **Đánh giá Rủi ro Liên tục**: Đánh giá vị thế bảo mật động dựa trên ngữ cảnh và hành vi hiện tại
- **Truy cập Có điều kiện**: Kiểm soát truy cập điều chỉnh dựa trên yếu tố rủi ro, vị trí và độ tin cậy thiết bị

### Mẫu Tích hợp Doanh nghiệp

#### **Tích hợp Hệ sinh thái Bảo mật Microsoft**
- **Microsoft Defender for Cloud**: Quản lý vị thế bảo mật đám mây toàn diện
- **Azure Sentinel**: SIEM và SOAR bản địa đám mây để bảo vệ khối lượng công việc AI
- **Microsoft Entra ID**: Quản lý danh tính và truy cập doanh nghiệp với chính sách truy cập có điều kiện
- **Azure Key Vault**: Quản lý bí mật tập trung với sự hỗ trợ của mô-đun bảo mật phần cứng (HSM)
- **Microsoft Purview**: Quản trị dữ liệu và tuân thủ cho nguồn dữ liệu và quy trình AI

#### **Tuân thủ & Quản trị**
- **Đảm bảo Tuân thủ**: Đảm bảo các triển khai MCP đáp ứng yêu cầu tuân thủ đặc thù ngành (GDPR, HIPAA, SOC 2)

- **Phân loại Dữ liệu**: Phân loại và xử lý đúng cách dữ liệu nhạy cảm được xử lý bởi các hệ thống AI
- **Dấu vết Kiểm toán**: Ghi nhật ký toàn diện để tuân thủ quy định và điều tra pháp y
- **Kiểm soát Quyền riêng tư**: Triển khai các nguyên tắc bảo mật theo thiết kế trong kiến trúc hệ thống AI
- **Quản lý Thay đổi**: Quy trình chính thức để đánh giá bảo mật các sửa đổi hệ thống AI

Các thực tiễn nền tảng này tạo ra một cơ sở bảo mật vững chắc giúp tăng hiệu quả kiểm soát bảo mật đặc thù MCP và cung cấp bảo vệ toàn diện cho các ứng dụng điều khiển bởi AI.

## Những điểm chính về Bảo mật

- **Phương pháp Bảo mật Tầng lớp**: Kết hợp các thực tiễn bảo mật nền tảng (mã hóa an toàn, quyền tối thiểu, xác minh chuỗi cung ứng, giám sát liên tục) với các kiểm soát đặc thù AI để bảo vệ toàn diện

- **Cảnh quan Mối đe dọa Riêng cho AI**: Hệ thống MCP đối mặt với các rủi ro đặc thù bao gồm tiêm chủng prompt, đầu độc công cụ, chiếm quyền phiên làm việc, vấn đề confused deputy, các lỗ hổng truyền token, và quyền hạn quá mức đòi hỏi các biện pháp giảm thiểu chuyên biệt

- **Xuất sắc về Xác thực & Ủy quyền**: Triển khai xác thực mạnh mẽ bằng nhà cung cấp danh tính bên ngoài (Microsoft Entra ID), thực thi xác thực token đúng cách, và không bao giờ chấp nhận token không được cấp rõ ràng cho máy chủ MCP của bạn

- **Phòng chống Tấn công AI**: Triển khai Microsoft Prompt Shields và Azure Content Safety để phòng thủ trước các cuộc tấn công tiêm chủng prompt gián tiếp và đầu độc công cụ, trong khi xác thực siêu dữ liệu công cụ và giám sát thay đổi động

- **Bảo mật Phiên & Giao thức**: Sử dụng ID phiên bảo mật mật mã không xác định ràng buộc với danh tính người dùng, triển khai quản lý vòng đời phiên đúng cách, và không bao giờ dùng phiên cho xác thực

- **Thực hành Tốt nhất về Bảo mật OAuth**: Ngăn ngừa tấn công confused deputy thông qua sự đồng ý rõ ràng của người dùng cho khách hàng đăng ký động, triển khai OAuth 2.1 đúng với PKCE, và kiểm tra nghiêm ngặt URI chuyển hướng  

- **Nguyên tắc Bảo mật Token**: Tránh các mẫu chống truyền token sai, xác thực các claim đối tượng token, triển khai token thời gian sống ngắn với xoay vòng an toàn, và duy trì ranh giới tin cậy rõ ràng

- **Bảo mật Chuỗi Cung Ứng Toàn diện**: Đối xử với tất cả các thành phần hệ sinh thái AI (mô hình, embeddings, nhà cung cấp ngữ cảnh, API bên ngoài) với mức độ nghiêm ngặt bảo mật như các phụ thuộc phần mềm truyền thống

- **Tiến hóa Liên tục**: Luôn cập nhật theo các đặc tả MCP phát triển nhanh, đóng góp vào các tiêu chuẩn cộng đồng bảo mật, và duy trì tư thế bảo mật thích ứng khi giao thức trưởng thành

- **Tích hợp Bảo mật Microsoft**: Tận dụng hệ sinh thái bảo mật toàn diện của Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) để tăng cường bảo vệ triển khai MCP

## Tài nguyên Toàn diện

### **Tài liệu Bảo mật Chính thức của MCP**
- [Đặc tả MCP (Hiện tại: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Thực hành Bảo mật Tốt nhất MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Đặc tả Ủy quyền MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Kho mã MCP GitHub](https://github.com/modelcontextprotocol)

### **Tài nguyên Bảo mật OWASP MCP**
- [Hướng dẫn Bảo mật OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 toàn diện với hướng dẫn triển khai Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Rủi ro bảo mật MCP chính thức OWASP
- [Hội thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Đào tạo bảo mật thực hành cho MCP trên Azure

### **Tiêu chuẩn & Thực hành Bảo mật Tốt nhất**
- [Thực hành Bảo mật Tốt nhất OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 An toàn Ứng dụng Web](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 cho Mô hình Ngôn ngữ Lớn](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Báo cáo Phòng thủ Kỹ thuật số Microsoft](https://aka.ms/mddr)

### **Nghiên cứu & Phân tích Bảo mật AI**
- [Tiêm chủng Prompt trong MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tấn công Đầu độc Công cụ (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Thông tin Nghiên cứu Bảo mật MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Giải pháp Bảo mật Microsoft**
- [Tài liệu Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Dịch vụ Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Bảo mật Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Thực hành Tốt nhất Quản lý Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Hướng dẫn Triển khai & Học tập**
- [Azure API Management làm Cổng Xác thực MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Xác thực Microsoft Entra ID với Máy chủ MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Lưu trữ Token An toàn và Mã hóa (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Bảo mật DevOps & Chuỗi Cung Ứng**
- [Bảo mật Azure DevOps](https://azure.microsoft.com/products/devops)
- [Bảo mật Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Hành trình Bảo mật Chuỗi Cung Ứng Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Tài liệu Bảo mật Bổ sung**

Để có hướng dẫn bảo mật toàn diện, tham khảo các tài liệu chuyên biệt trong phần này:

- **[Mẫu Ủy quyền CIMD và DCR](./samples/cimd-dcr-auth/README.md)** - Máy chủ tài nguyên MCP TypeScript `2026-07-28` có thể chạy ví dụ so sánh Tài liệu Metadata Client ID ưu tiên với đăng ký khách hàng động bị loại bỏ làm phương án dự phòng
- **[Thực hành Bảo mật Tốt nhất MCP](./mcp-security-best-practices.md)** - Thực hành bảo mật toàn diện cho triển khai MCP
- **[Triển khai Azure Content Safety](./azure-content-safety-implementation.md)** - Ví dụ triển khai thực tiễn cho tích hợp Azure Content Safety  
- **[Kiểm soát Bảo mật MCP](./mcp-security-controls.md)** - Kiểm soát và kỹ thuật bảo mật mới nhất cho triển khai MCP
- **[Tổng quan Thực hành Tốt nhất MCP](./mcp-best-practices.md)** - Hướng dẫn tham khảo nhanh các thực hành bảo mật MCP thiết yếu
- **[BlueHat 2026: Bảo mật tương lai AI: Bảo mật MCP với mô hình phòng thủ đa lớp](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Mô hình phòng thủ đa lớp từ Trung tâm Phản ứng An ninh Microsoft (MSRC)

### **Đào tạo Bảo mật Thực hành**

- **[Hội thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Hội thảo thực hành toàn diện để bảo mật máy chủ MCP trên Azure với các cấp độ tập dần từ Base Camp đến Summit
- **[Hướng dẫn Bảo mật OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Kiến trúc tham khảo và hướng dẫn triển khai cho tất cả rủi ro OWASP MCP Top 10

---

## Tiếp theo

Tiếp theo: [Chương 3: Bắt đầu](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->