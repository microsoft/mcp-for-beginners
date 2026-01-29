# MCP Security: Bảo vệ Toàn diện cho Hệ thống AI

[![MCP Security Best Practices](../../../translated_images/vi/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Nhấp vào hình ảnh trên để xem video bài học này)_

Bảo mật là nền tảng trong thiết kế hệ thống AI, đó là lý do tại sao chúng tôi ưu tiên nó là phần thứ hai. Điều này phù hợp với nguyên tắc **Secure by Design** của Microsoft từ [Sáng kiến Tương lai An toàn](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Giao thức Ngữ cảnh Mô hình (MCP) mang lại các khả năng mạnh mẽ mới cho các ứng dụng điều khiển bởi AI đồng thời giới thiệu các thách thức bảo mật độc đáo vượt ra ngoài các rủi ro phần mềm truyền thống. Hệ thống MCP đối mặt với cả các mối quan tâm bảo mật đã được thiết lập (lập trình an toàn, quyền tối thiểu, bảo mật chuỗi cung ứng) và các mối đe dọa đặc thù AI mới bao gồm tiêm lệnh (prompt injection), đầu độc công cụ, chiếm đoạt phiên làm việc, tấn công confused deputy, lỗ hổng truyền token, và sửa đổi năng lực động.

Bài học này khám phá các rủi ro bảo mật quan trọng nhất trong triển khai MCP — bao gồm xác thực, ủy quyền, quyền hạn quá mức, tiêm lệnh gián tiếp, bảo mật phiên làm việc, vấn đề confused deputy, quản lý token, và lỗ hổng chuỗi cung ứng. Bạn sẽ học các biện pháp kiểm soát và thực hành tốt nhất có thể áp dụng để giảm thiểu các rủi ro này đồng thời tận dụng các giải pháp Microsoft như Prompt Shields, Azure Content Safety, và GitHub Advanced Security để củng cố triển khai MCP của bạn.

## Mục tiêu học tập

Kết thúc bài học này, bạn sẽ có thể:

- **Nhận diện các mối đe dọa đặc thù MCP**: Nhận biết các rủi ro bảo mật độc đáo trong hệ thống MCP bao gồm tiêm lệnh, đầu độc công cụ, quyền hạn quá mức, chiếm đoạt phiên làm việc, vấn đề confused deputy, lỗ hổng truyền token, và rủi ro chuỗi cung ứng
- **Áp dụng các biện pháp kiểm soát bảo mật**: Triển khai các biện pháp giảm thiểu hiệu quả bao gồm xác thực mạnh mẽ, truy cập theo nguyên tắc quyền tối thiểu, quản lý token an toàn, kiểm soát bảo mật phiên làm việc, và xác minh chuỗi cung ứng
- **Tận dụng giải pháp bảo mật Microsoft**: Hiểu và triển khai Microsoft Prompt Shields, Azure Content Safety, và GitHub Advanced Security để bảo vệ khối lượng công việc MCP
- **Xác thực bảo mật công cụ**: Nhận biết tầm quan trọng của việc xác thực metadata công cụ, giám sát các thay đổi động, và phòng chống các cuộc tấn công tiêm lệnh gián tiếp
- **Tích hợp các thực hành tốt nhất**: Kết hợp các nguyên tắc bảo mật nền tảng (lập trình an toàn, tăng cường máy chủ, zero trust) với các biện pháp kiểm soát đặc thù MCP để bảo vệ toàn diện

# Kiến trúc & Biện pháp kiểm soát Bảo mật MCP

Các triển khai MCP hiện đại đòi hỏi các phương pháp bảo mật nhiều lớp nhằm giải quyết cả bảo mật phần mềm truyền thống và các mối đe dọa đặc thù AI. Đặc tả MCP đang phát triển nhanh chóng và tiếp tục hoàn thiện các biện pháp kiểm soát bảo mật, cho phép tích hợp tốt hơn với kiến trúc bảo mật doanh nghiệp và các thực hành tốt nhất đã được thiết lập.

Nghiên cứu từ [Báo cáo Phòng thủ Kỹ thuật số Microsoft](https://aka.ms/mddr) cho thấy **98% các vi phạm được báo cáo có thể được ngăn chặn bằng vệ sinh bảo mật nghiêm ngặt**. Chiến lược bảo vệ hiệu quả nhất kết hợp các thực hành bảo mật nền tảng với các biện pháp kiểm soát đặc thù MCP — các biện pháp bảo mật cơ bản đã được chứng minh vẫn là yếu tố tác động lớn nhất trong việc giảm thiểu rủi ro bảo mật tổng thể.

## Bối cảnh Bảo mật Hiện tại

> **Lưu ý:** Thông tin này phản ánh các tiêu chuẩn bảo mật MCP tính đến **ngày 18 tháng 12 năm 2025**. Giao thức MCP tiếp tục phát triển nhanh chóng, và các triển khai trong tương lai có thể giới thiệu các mẫu xác thực mới và các biện pháp kiểm soát nâng cao. Luôn tham khảo [Đặc tả MCP](https://spec.modelcontextprotocol.io/), [kho lưu trữ MCP trên GitHub](https://github.com/modelcontextprotocol), và [tài liệu thực hành bảo mật tốt nhất](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) hiện hành để có hướng dẫn mới nhất.

### Sự phát triển của Xác thực MCP

Đặc tả MCP đã tiến triển đáng kể trong cách tiếp cận xác thực và ủy quyền:

- **Cách tiếp cận ban đầu**: Các đặc tả đầu tiên yêu cầu nhà phát triển triển khai máy chủ xác thực tùy chỉnh, với các máy chủ MCP hoạt động như Máy chủ Ủy quyền OAuth 2.0 quản lý xác thực người dùng trực tiếp
- **Tiêu chuẩn hiện tại (2025-11-25)**: Đặc tả cập nhật cho phép máy chủ MCP ủy quyền xác thực cho các nhà cung cấp danh tính bên ngoài (như Microsoft Entra ID), cải thiện tư thế bảo mật và giảm độ phức tạp triển khai
- **Bảo mật lớp vận chuyển**: Hỗ trợ nâng cao cho các cơ chế vận chuyển an toàn với các mẫu xác thực phù hợp cho cả kết nối cục bộ (STDIO) và từ xa (Streamable HTTP)

## Bảo mật Xác thực & Ủy quyền

### Thách thức Bảo mật Hiện tại

Các triển khai MCP hiện đại đối mặt với một số thách thức về xác thực và ủy quyền:

### Rủi ro & Vectơ tấn công

- **Logic ủy quyền cấu hình sai**: Việc triển khai ủy quyền lỗi trong máy chủ MCP có thể làm lộ dữ liệu nhạy cảm và áp dụng sai các kiểm soát truy cập
- **Xâm phạm token OAuth**: Việc đánh cắp token máy chủ MCP cục bộ cho phép kẻ tấn công giả mạo máy chủ và truy cập dịch vụ hạ nguồn
- **Lỗ hổng truyền token**: Xử lý token không đúng cách tạo ra các lỗ hổng bỏ qua kiểm soát bảo mật và khoảng trống trách nhiệm
- **Quyền hạn quá mức**: Máy chủ MCP có quyền quá cao vi phạm nguyên tắc quyền tối thiểu và mở rộng bề mặt tấn công

#### Truyền token: Một mẫu chống quan trọng

**Truyền token bị cấm rõ ràng** trong đặc tả ủy quyền MCP hiện tại do các tác động bảo mật nghiêm trọng:

##### Vượt qua kiểm soát bảo mật  
- Máy chủ MCP và API hạ nguồn thực thi các kiểm soát bảo mật quan trọng (giới hạn tốc độ, xác thực yêu cầu, giám sát lưu lượng) phụ thuộc vào việc xác thực token đúng cách  
- Việc sử dụng token trực tiếp từ client đến API bỏ qua các biện pháp bảo vệ thiết yếu này, làm suy yếu kiến trúc bảo mật

##### Thách thức về trách nhiệm & kiểm toán  
- Máy chủ MCP không thể phân biệt giữa các client sử dụng token do upstream cấp, làm đứt đoạn các dấu vết kiểm toán  
- Nhật ký máy chủ tài nguyên hạ nguồn hiển thị nguồn yêu cầu sai lệch thay vì trung gian máy chủ MCP thực tế  
- Việc điều tra sự cố và kiểm toán tuân thủ trở nên khó khăn hơn nhiều

##### Rủi ro rò rỉ dữ liệu  
- Các tuyên bố token không được xác thực cho phép kẻ xấu với token bị đánh cắp sử dụng máy chủ MCP làm proxy để rò rỉ dữ liệu  
- Vi phạm ranh giới tin cậy cho phép các mẫu truy cập trái phép bỏ qua các kiểm soát bảo mật dự kiến

##### Vectơ tấn công đa dịch vụ  
- Token bị xâm phạm được chấp nhận bởi nhiều dịch vụ cho phép di chuyển ngang qua các hệ thống kết nối  
- Các giả định tin cậy giữa các dịch vụ có thể bị vi phạm khi nguồn token không thể xác minh

### Biện pháp kiểm soát & Giảm thiểu

**Yêu cầu bảo mật quan trọng:**

> **BẮT BUỘC**: Máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận bất kỳ token nào không được cấp rõ ràng cho máy chủ MCP đó

#### Kiểm soát Xác thực & Ủy quyền

- **Đánh giá ủy quyền nghiêm ngặt**: Thực hiện kiểm toán toàn diện logic ủy quyền máy chủ MCP để đảm bảo chỉ người dùng và client dự kiến mới có thể truy cập tài nguyên nhạy cảm  
  - **Hướng dẫn triển khai**: [Azure API Management làm cổng xác thực cho máy chủ MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
  - **Tích hợp danh tính**: [Sử dụng Microsoft Entra ID cho xác thực máy chủ MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Quản lý token an toàn**: Triển khai [thực hành tốt nhất về xác thực và vòng đời token của Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)  
  - Xác thực các tuyên bố audience token phù hợp với danh tính máy chủ MCP  
  - Thực hiện chính sách xoay vòng và hết hạn token đúng cách  
  - Ngăn chặn các cuộc tấn công phát lại token và sử dụng trái phép

- **Lưu trữ token được bảo vệ**: Lưu trữ token an toàn với mã hóa cả khi lưu trữ và truyền tải  
  - **Thực hành tốt nhất**: [Hướng dẫn lưu trữ và mã hóa token an toàn](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Triển khai Kiểm soát Truy cập

- **Nguyên tắc Quyền Tối thiểu**: Cấp cho máy chủ MCP chỉ các quyền tối thiểu cần thiết cho chức năng dự kiến  
  - Đánh giá và cập nhật quyền định kỳ để ngăn chặn quyền hạn leo thang  
  - **Tài liệu Microsoft**: [Truy cập an toàn theo quyền tối thiểu](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kiểm soát truy cập dựa trên vai trò (RBAC)**: Triển khai phân quyền vai trò chi tiết  
  - Giới hạn vai trò chặt chẽ với tài nguyên và hành động cụ thể  
  - Tránh cấp quyền rộng hoặc không cần thiết làm mở rộng bề mặt tấn công

- **Giám sát quyền liên tục**: Thực hiện kiểm toán và giám sát truy cập liên tục  
  - Giám sát các mẫu sử dụng quyền để phát hiện bất thường  
  - Sửa chữa kịp thời các quyền quá mức hoặc không sử dụng

## Các Mối đe dọa Bảo mật Đặc thù AI

### Tấn công Tiêm Lệnh & Thao Túng Công Cụ

Các triển khai MCP hiện đại đối mặt với các vectơ tấn công AI tinh vi mà các biện pháp bảo mật truyền thống không thể xử lý hoàn toàn:

#### **Tiêm Lệnh Gián Tiếp (Tiêm Lệnh Liên Miền)**

**Tiêm Lệnh Gián Tiếp** là một trong những lỗ hổng nghiêm trọng nhất trong các hệ thống AI được kích hoạt MCP. Kẻ tấn công nhúng các chỉ dẫn độc hại trong nội dung bên ngoài — tài liệu, trang web, email hoặc nguồn dữ liệu — mà hệ thống AI sau đó xử lý như các lệnh hợp lệ.

**Kịch bản tấn công:**  
- **Tiêm lệnh dựa trên tài liệu**: Chỉ dẫn độc hại ẩn trong tài liệu được xử lý kích hoạt các hành động AI không mong muốn  
- **Khai thác nội dung web**: Trang web bị xâm phạm chứa các prompt nhúng thao túng hành vi AI khi được thu thập dữ liệu  
- **Tấn công qua email**: Prompt độc hại trong email khiến trợ lý AI rò rỉ thông tin hoặc thực hiện hành động trái phép  
- **Ô nhiễm nguồn dữ liệu**: Cơ sở dữ liệu hoặc API bị xâm phạm cung cấp nội dung bị nhiễm cho hệ thống AI

**Tác động thực tế**: Các cuộc tấn công này có thể dẫn đến rò rỉ dữ liệu, vi phạm quyền riêng tư, tạo nội dung có hại, và thao túng tương tác người dùng. Để phân tích chi tiết, xem [Tiêm Lệnh trong MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/vi/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Tấn công Đầu độc Công Cụ**

**Đầu độc Công Cụ** nhắm vào metadata định nghĩa các công cụ MCP, khai thác cách các mô hình ngôn ngữ lớn (LLM) diễn giải mô tả và tham số công cụ để quyết định thực thi.

**Cơ chế tấn công:**  
- **Thao túng metadata**: Kẻ tấn công chèn các chỉ dẫn độc hại vào mô tả công cụ, định nghĩa tham số, hoặc ví dụ sử dụng  
- **Chỉ dẫn vô hình**: Prompt ẩn trong metadata công cụ được mô hình AI xử lý nhưng không hiển thị với người dùng  
- **Sửa đổi công cụ động ("Rug Pulls")**: Công cụ được người dùng phê duyệt sau đó bị thay đổi để thực hiện hành động độc hại mà người dùng không biết  
- **Tiêm tham số**: Nội dung độc hại nhúng trong schema tham số công cụ ảnh hưởng đến hành vi mô hình

**Rủi ro máy chủ lưu trữ**: Máy chủ MCP từ xa có rủi ro cao hơn vì định nghĩa công cụ có thể được cập nhật sau khi người dùng phê duyệt ban đầu, tạo ra các kịch bản công cụ trước an toàn trở nên độc hại. Để phân tích toàn diện, xem [Tấn công Đầu độc Công Cụ (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/vi/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Các Vectơ Tấn công AI Bổ sung**

- **Tiêm Lệnh Liên Miền (XPIA)**: Các cuộc tấn công tinh vi sử dụng nội dung từ nhiều miền để vượt qua kiểm soát bảo mật  
- **Sửa đổi Năng lực Động**: Thay đổi năng lực công cụ theo thời gian thực thoát khỏi đánh giá bảo mật ban đầu  
- **Đầu độc Cửa sổ Ngữ cảnh**: Tấn công thao túng cửa sổ ngữ cảnh lớn để ẩn chỉ dẫn độc hại  
- **Tấn công Gây nhầm lẫn Mô hình**: Khai thác giới hạn mô hình để tạo hành vi không thể đoán trước hoặc không an toàn

### Tác động Rủi ro Bảo mật AI

**Hậu quả tác động cao:**  
- **Rò rỉ dữ liệu**: Truy cập và đánh cắp dữ liệu doanh nghiệp hoặc cá nhân nhạy cảm trái phép  
- **Vi phạm quyền riêng tư**: Lộ thông tin cá nhân nhận dạng (PII) và dữ liệu kinh doanh bí mật  
- **Thao túng hệ thống**: Sửa đổi không mong muốn các hệ thống và quy trình quan trọng  
- **Đánh cắp thông tin xác thực**: Xâm phạm token xác thực và thông tin đăng nhập dịch vụ  
- **Di chuyển ngang**: Sử dụng hệ thống AI bị xâm phạm làm điểm trung chuyển cho các cuộc tấn công mạng rộng hơn

### Giải pháp Bảo mật AI của Microsoft

#### **AI Prompt Shields: Bảo vệ Nâng cao Chống Tấn công Tiêm Lệnh**

Microsoft **AI Prompt Shields** cung cấp phòng thủ toàn diện chống lại cả tấn công tiêm lệnh trực tiếp và gián tiếp thông qua nhiều lớp bảo mật:

##### **Cơ chế bảo vệ cốt lõi:**

1. **Phát hiện & Lọc nâng cao**  
   - Thuật toán học máy và kỹ thuật xử lý ngôn ngữ tự nhiên phát hiện chỉ dẫn độc hại trong nội dung bên ngoài  
   - Phân tích thời gian thực tài liệu, trang web, email, và nguồn dữ liệu để phát hiện mối đe dọa nhúng  
   - Hiểu ngữ cảnh phân biệt mẫu prompt hợp lệ và độc hại

2. **Kỹ thuật Spotlighting**  
   - Phân biệt giữa chỉ dẫn hệ thống tin cậy và đầu vào bên ngoài có thể bị xâm phạm  
   - Phương pháp biến đổi văn bản tăng cường tính liên quan của mô hình đồng thời cô lập nội dung độc hại  
   - Giúp hệ thống AI duy trì thứ tự chỉ dẫn đúng và bỏ qua lệnh tiêm

3. **Hệ thống phân định & đánh dấu dữ liệu**  
   - Định nghĩa ranh giới rõ ràng giữa tin nhắn hệ thống tin cậy và văn bản đầu vào bên ngoài  
   - Các dấu hiệu đặc biệt làm nổi bật ranh giới giữa nguồn dữ liệu tin cậy và không tin cậy  
   - Phân tách rõ ràng ngăn ngừa nhầm lẫn chỉ dẫn và thực thi lệnh trái phép

4. **Tình báo mối đe dọa liên tục**  
   - Microsoft liên tục giám sát các mẫu tấn công mới và cập nhật biện pháp phòng thủ  
   - Tìm kiếm mối đe dọa chủ động cho các kỹ thuật tiêm lệnh và vectơ tấn công mới  
   - Cập nhật mô hình bảo mật định kỳ để duy trì hiệu quả trước các mối đe dọa phát triển

5. **Tích hợp Azure Content Safety**  
   - Là một phần của bộ công cụ Azure AI Content Safety toàn diện  
   - Phát hiện bổ sung các nỗ lực jailbreak, nội dung có hại, và vi phạm chính sách bảo mật  
   - Kiểm soát bảo mật thống nhất trên các thành phần ứng dụng AI

**Tài nguyên triển khai**: [Tài liệu Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/vi/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Các Mối đe dọa Bảo mật MCP Nâng cao

### Lỗ hổng Chiếm đoạt Phiên làm việc

**Chiếm đoạt phiên làm việc** là vectơ tấn công nghiêm trọng trong các triển khai MCP có trạng thái, nơi các bên không được phép lấy và lạm dụng các định danh phiên hợp pháp để giả mạo client và thực hiện hành động trái phép.

#### **Kịch bản tấn công & Rủi ro**

- **Tiêm lệnh chiếm đoạt phiên**: Kẻ tấn công với ID phiên bị đánh cắp tiêm các sự kiện độc hại vào máy chủ chia sẻ trạng thái phiên, có thể kích hoạt hành động gây hại hoặc truy cập dữ liệu nhạy cảm  
- **Giả mạo trực tiếp**: ID phiên bị đánh cắp cho phép gọi máy chủ MCP trực tiếp bỏ qua xác thực, coi kẻ tấn công như người dùng hợp pháp  
- **Luồng có thể tiếp tục bị xâm phạm**: Kẻ tấn công có thể kết thúc yêu cầu sớm, khiến client hợp pháp tiếp tục với nội dung có thể độc hại

#### **Biện pháp kiểm soát cho Quản lý Phiên làm việc**

**Yêu cầu quan trọng:**
- **Xác thực ủy quyền**: Các máy chủ MCP triển khai ủy quyền **PHẢI** xác minh TẤT CẢ các yêu cầu đến và **KHÔNG ĐƯỢC** dựa vào phiên làm việc để xác thực
- **Tạo phiên làm việc an toàn**: Sử dụng ID phiên làm việc không xác định, an toàn về mặt mật mã được tạo bằng bộ sinh số ngẫu nhiên an toàn
- **Ràng buộc theo người dùng**: Ràng buộc ID phiên làm việc với thông tin người dùng cụ thể bằng các định dạng như `<user_id>:<session_id>` để ngăn chặn việc lạm dụng phiên làm việc giữa các người dùng
- **Quản lý vòng đời phiên làm việc**: Triển khai hết hạn, xoay vòng và vô hiệu hóa đúng cách để giới hạn cửa sổ lỗ hổng
- **Bảo mật truyền tải**: Bắt buộc HTTPS cho tất cả các giao tiếp để ngăn chặn việc chặn bắt ID phiên làm việc

### Vấn đề đại diện nhầm lẫn

**Vấn đề đại diện nhầm lẫn** xảy ra khi các máy chủ MCP đóng vai trò như proxy xác thực giữa khách hàng và các dịch vụ bên thứ ba, tạo cơ hội cho việc vượt qua ủy quyền thông qua khai thác ID khách hàng tĩnh.

#### **Cơ chế tấn công & Rủi ro**

- **Vượt qua sự đồng ý dựa trên cookie**: Xác thực người dùng trước đó tạo cookie đồng ý mà kẻ tấn công khai thác thông qua các yêu cầu ủy quyền độc hại với URI chuyển hướng được tạo thủ công
- **Trộm mã ủy quyền**: Cookie đồng ý hiện có có thể khiến máy chủ ủy quyền bỏ qua màn hình đồng ý, chuyển mã đến các điểm cuối do kẻ tấn công kiểm soát  
- **Truy cập API trái phép**: Mã ủy quyền bị đánh cắp cho phép trao đổi token và giả mạo người dùng mà không có sự chấp thuận rõ ràng

#### **Chiến lược giảm thiểu**

**Kiểm soát bắt buộc:**
- **Yêu cầu đồng ý rõ ràng**: Các máy chủ proxy MCP sử dụng ID khách hàng tĩnh **PHẢI** lấy sự đồng ý của người dùng cho mỗi khách hàng được đăng ký động
- **Triển khai bảo mật OAuth 2.1**: Tuân theo các thực hành bảo mật OAuth hiện hành bao gồm PKCE (Proof Key for Code Exchange) cho tất cả các yêu cầu ủy quyền
- **Xác thực khách hàng nghiêm ngặt**: Triển khai xác thực chặt chẽ các URI chuyển hướng và định danh khách hàng để ngăn chặn khai thác

### Lỗ hổng chuyển tiếp token  

**Chuyển tiếp token** là một mẫu chống rõ ràng khi các máy chủ MCP chấp nhận token của khách hàng mà không xác thực đúng cách và chuyển tiếp chúng đến các API hạ nguồn, vi phạm các đặc tả ủy quyền MCP.

#### **Hệ quả bảo mật**

- **Vượt qua kiểm soát**: Việc sử dụng token trực tiếp từ khách hàng đến API bỏ qua các kiểm soát giới hạn tốc độ, xác thực và giám sát quan trọng
- **Hỏng dấu vết kiểm toán**: Token phát hành từ phía trên làm cho việc xác định khách hàng không thể thực hiện, phá vỡ khả năng điều tra sự cố
- **Rò rỉ dữ liệu qua proxy**: Token không được xác thực cho phép kẻ xấu sử dụng máy chủ như proxy để truy cập dữ liệu trái phép
- **Vi phạm ranh giới tin cậy**: Các dịch vụ hạ nguồn có thể bị vi phạm giả định tin cậy khi nguồn gốc token không thể xác minh
- **Mở rộng tấn công đa dịch vụ**: Token bị xâm phạm được chấp nhận trên nhiều dịch vụ cho phép di chuyển ngang

#### **Kiểm soát bảo mật bắt buộc**

**Yêu cầu không thể thương lượng:**
- **Xác thực token**: Các máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận token không được phát hành rõ ràng cho máy chủ MCP
- **Xác minh đối tượng token**: Luôn xác thực các tuyên bố đối tượng token khớp với danh tính máy chủ MCP
- **Vòng đời token đúng cách**: Triển khai token truy cập thời gian sống ngắn với các thực hành xoay vòng an toàn


## Bảo mật chuỗi cung ứng cho hệ thống AI

Bảo mật chuỗi cung ứng đã phát triển vượt ra ngoài các phụ thuộc phần mềm truyền thống để bao quát toàn bộ hệ sinh thái AI. Các triển khai MCP hiện đại phải kiểm tra và giám sát nghiêm ngặt tất cả các thành phần liên quan đến AI, vì mỗi thành phần đều có thể mang lại các lỗ hổng tiềm ẩn có thể làm tổn hại tính toàn vẹn hệ thống.

### Các thành phần chuỗi cung ứng AI mở rộng

**Phụ thuộc phần mềm truyền thống:**
- Thư viện và khung mã nguồn mở
- Ảnh container và hệ thống cơ sở  
- Công cụ phát triển và quy trình xây dựng
- Thành phần và dịch vụ hạ tầng

**Các yếu tố chuỗi cung ứng AI cụ thể:**
- **Mô hình nền tảng**: Mô hình được huấn luyện sẵn từ nhiều nhà cung cấp khác nhau cần xác minh nguồn gốc
- **Dịch vụ nhúng**: Dịch vụ vector hóa và tìm kiếm ngữ nghĩa bên ngoài
- **Nhà cung cấp ngữ cảnh**: Nguồn dữ liệu, cơ sở tri thức và kho tài liệu  
- **API bên thứ ba**: Dịch vụ AI bên ngoài, pipeline ML và điểm xử lý dữ liệu
- **Tài sản mô hình**: Trọng số, cấu hình và các biến thể mô hình tinh chỉnh
- **Nguồn dữ liệu huấn luyện**: Bộ dữ liệu dùng để huấn luyện và tinh chỉnh mô hình

### Chiến lược bảo mật chuỗi cung ứng toàn diện

#### **Xác minh thành phần & Tin cậy**
- **Xác thực nguồn gốc**: Xác minh xuất xứ, giấy phép và tính toàn vẹn của tất cả các thành phần AI trước khi tích hợp
- **Đánh giá bảo mật**: Thực hiện quét lỗ hổng và đánh giá bảo mật cho mô hình, nguồn dữ liệu và dịch vụ AI
- **Phân tích uy tín**: Đánh giá hồ sơ bảo mật và thực hành của nhà cung cấp dịch vụ AI
- **Xác minh tuân thủ**: Đảm bảo tất cả thành phần đáp ứng yêu cầu bảo mật và quy định của tổ chức

#### **Quy trình triển khai an toàn**  
- **Bảo mật CI/CD tự động**: Tích hợp quét bảo mật trong toàn bộ quy trình triển khai tự động
- **Toàn vẹn tài sản**: Triển khai xác minh mật mã cho tất cả tài sản được triển khai (mã, mô hình, cấu hình)
- **Triển khai theo giai đoạn**: Sử dụng chiến lược triển khai tiến tiến với xác thực bảo mật ở mỗi giai đoạn
- **Kho lưu trữ tài sản tin cậy**: Chỉ triển khai từ các kho lưu trữ tài sản đã được xác minh và an toàn

#### **Giám sát & Phản ứng liên tục**
- **Quét phụ thuộc**: Giám sát lỗ hổng liên tục cho tất cả phụ thuộc phần mềm và thành phần AI
- **Giám sát mô hình**: Đánh giá liên tục hành vi mô hình, sự trôi dạt hiệu năng và bất thường bảo mật
- **Theo dõi sức khỏe dịch vụ**: Giám sát dịch vụ AI bên ngoài về tính khả dụng, sự cố bảo mật và thay đổi chính sách
- **Tích hợp tình báo mối đe dọa**: Kết hợp nguồn dữ liệu mối đe dọa đặc thù cho bảo mật AI và ML

#### **Kiểm soát truy cập & Nguyên tắc tối thiểu**
- **Quyền hạn cấp thành phần**: Hạn chế truy cập mô hình, dữ liệu và dịch vụ dựa trên nhu cầu kinh doanh
- **Quản lý tài khoản dịch vụ**: Triển khai tài khoản dịch vụ riêng biệt với quyền hạn tối thiểu cần thiết
- **Phân đoạn mạng**: Cô lập các thành phần AI và giới hạn truy cập mạng giữa các dịch vụ
- **Kiểm soát cổng API**: Sử dụng cổng API tập trung để kiểm soát và giám sát truy cập dịch vụ AI bên ngoài

#### **Phản ứng sự cố & Khôi phục**
- **Quy trình phản ứng nhanh**: Các quy trình thiết lập để vá hoặc thay thế các thành phần AI bị xâm phạm
- **Xoay vòng thông tin xác thực**: Hệ thống tự động xoay vòng bí mật, khóa API và thông tin xác thực dịch vụ
- **Khả năng phục hồi**: Khả năng nhanh chóng quay lại các phiên bản AI đã biết là an toàn trước đó
- **Phục hồi sau vi phạm chuỗi cung ứng**: Quy trình cụ thể để ứng phó với các sự cố xâm phạm dịch vụ AI phía trên

### Công cụ & Tích hợp bảo mật Microsoft

**GitHub Advanced Security** cung cấp bảo vệ chuỗi cung ứng toàn diện bao gồm:
- **Quét bí mật**: Phát hiện tự động thông tin xác thực, khóa API và token trong kho mã
- **Quét phụ thuộc**: Đánh giá lỗ hổng cho các phụ thuộc và thư viện mã nguồn mở
- **Phân tích CodeQL**: Phân tích mã tĩnh để phát hiện lỗ hổng bảo mật và lỗi lập trình
- **Thông tin chuỗi cung ứng**: Hiển thị tình trạng sức khỏe và bảo mật phụ thuộc

**Tích hợp Azure DevOps & Azure Repos:**
- Tích hợp quét bảo mật liền mạch trên các nền tảng phát triển Microsoft
- Kiểm tra bảo mật tự động trong Azure Pipelines cho khối lượng công việc AI
- Thực thi chính sách triển khai thành phần AI an toàn

**Thực hành nội bộ Microsoft:**
Microsoft triển khai các thực hành bảo mật chuỗi cung ứng rộng khắp trên tất cả sản phẩm. Tìm hiểu các phương pháp đã được chứng minh tại [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Thực hành bảo mật nền tảng tốt nhất

Các triển khai MCP kế thừa và xây dựng dựa trên tư thế bảo mật hiện có của tổ chức bạn. Tăng cường các thực hành bảo mật nền tảng sẽ nâng cao đáng kể bảo mật tổng thể của hệ thống AI và triển khai MCP.

### Các nguyên tắc bảo mật cốt lõi

#### **Thực hành phát triển an toàn**
- **Tuân thủ OWASP**: Bảo vệ chống lại các lỗ hổng ứng dụng web [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Bảo vệ đặc thù AI**: Triển khai kiểm soát cho [OWASP Top 10 cho LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Quản lý bí mật an toàn**: Sử dụng kho bí mật chuyên dụng cho token, khóa API và dữ liệu cấu hình nhạy cảm
- **Mã hóa đầu cuối**: Triển khai giao tiếp an toàn trên tất cả thành phần ứng dụng và luồng dữ liệu
- **Xác thực đầu vào**: Kiểm tra nghiêm ngặt tất cả đầu vào người dùng, tham số API và nguồn dữ liệu

#### **Củng cố hạ tầng**
- **Xác thực đa yếu tố**: Bắt buộc MFA cho tất cả tài khoản quản trị và dịch vụ
- **Quản lý bản vá**: Tự động và kịp thời vá lỗi cho hệ điều hành, khung và phụ thuộc  
- **Tích hợp nhà cung cấp danh tính**: Quản lý danh tính tập trung qua nhà cung cấp danh tính doanh nghiệp (Microsoft Entra ID, Active Directory)
- **Phân đoạn mạng**: Cô lập logic các thành phần MCP để hạn chế khả năng di chuyển ngang
- **Nguyên tắc tối thiểu quyền hạn**: Cấp quyền tối thiểu cần thiết cho tất cả thành phần và tài khoản hệ thống

#### **Giám sát & phát hiện bảo mật**
- **Ghi nhật ký toàn diện**: Ghi lại chi tiết hoạt động ứng dụng AI, bao gồm tương tác máy khách-máy chủ MCP
- **Tích hợp SIEM**: Quản lý thông tin và sự kiện bảo mật tập trung để phát hiện bất thường
- **Phân tích hành vi**: Giám sát dựa trên AI để phát hiện các mẫu hành vi bất thường của hệ thống và người dùng
- **Tình báo mối đe dọa**: Kết hợp nguồn dữ liệu mối đe dọa bên ngoài và chỉ số xâm phạm (IOC)
- **Phản ứng sự cố**: Quy trình rõ ràng cho phát hiện, phản ứng và khôi phục sự cố bảo mật

#### **Kiến trúc Zero Trust**
- **Không bao giờ tin tưởng, luôn xác minh**: Xác minh liên tục người dùng, thiết bị và kết nối mạng
- **Phân đoạn vi mô**: Kiểm soát mạng chi tiết để cô lập từng khối lượng công việc và dịch vụ
- **Bảo mật tập trung danh tính**: Chính sách bảo mật dựa trên danh tính đã xác minh thay vì vị trí mạng
- **Đánh giá rủi ro liên tục**: Đánh giá tư thế bảo mật động dựa trên ngữ cảnh và hành vi hiện tại
- **Truy cập có điều kiện**: Kiểm soát truy cập thích ứng dựa trên yếu tố rủi ro, vị trí và độ tin cậy thiết bị

### Mẫu tích hợp doanh nghiệp

#### **Tích hợp hệ sinh thái bảo mật Microsoft**
- **Microsoft Defender for Cloud**: Quản lý tư thế bảo mật đám mây toàn diện
- **Azure Sentinel**: SIEM và SOAR bản địa đám mây cho bảo vệ khối lượng công việc AI
- **Microsoft Entra ID**: Quản lý danh tính và truy cập doanh nghiệp với chính sách truy cập có điều kiện
- **Azure Key Vault**: Quản lý bí mật tập trung với mô-đun bảo mật phần cứng (HSM) hỗ trợ
- **Microsoft Purview**: Quản trị dữ liệu và tuân thủ cho nguồn dữ liệu và quy trình AI

#### **Tuân thủ & Quản trị**
- **Phù hợp quy định**: Đảm bảo triển khai MCP đáp ứng yêu cầu tuân thủ ngành (GDPR, HIPAA, SOC 2)
- **Phân loại dữ liệu**: Phân loại và xử lý đúng cách dữ liệu nhạy cảm do hệ thống AI xử lý
- **Dấu vết kiểm toán**: Ghi nhật ký toàn diện cho tuân thủ quy định và điều tra pháp y
- **Kiểm soát quyền riêng tư**: Triển khai nguyên tắc bảo mật theo thiết kế trong kiến trúc hệ thống AI
- **Quản lý thay đổi**: Quy trình chính thức cho đánh giá bảo mật các sửa đổi hệ thống AI

Các thực hành nền tảng này tạo ra một cơ sở bảo mật vững chắc nâng cao hiệu quả các kiểm soát bảo mật đặc thù MCP và cung cấp bảo vệ toàn diện cho các ứng dụng AI.

## Những điểm chính về bảo mật

- **Phương pháp bảo mật nhiều lớp**: Kết hợp các thực hành bảo mật nền tảng (lập trình an toàn, tối thiểu quyền hạn, xác minh chuỗi cung ứng, giám sát liên tục) với các kiểm soát đặc thù AI để bảo vệ toàn diện

- **Cảnh quan mối đe dọa đặc thù AI**: Hệ thống MCP đối mặt với các rủi ro độc đáo bao gồm tiêm lệnh nhắc, đầu độc công cụ, chiếm đoạt phiên, vấn đề đại diện nhầm lẫn, lỗ hổng chuyển tiếp token và quyền hạn quá mức cần các biện pháp giảm thiểu chuyên biệt

- **Xuất sắc trong xác thực & ủy quyền**: Triển khai xác thực mạnh mẽ sử dụng nhà cung cấp danh tính bên ngoài (Microsoft Entra ID), thực thi xác thực token đúng cách và không bao giờ chấp nhận token không được phát hành rõ ràng cho máy chủ MCP của bạn

- **Phòng chống tấn công AI**: Triển khai Microsoft Prompt Shields và Azure Content Safety để phòng chống tiêm lệnh nhắc gián tiếp và tấn công đầu độc công cụ, đồng thời xác thực siêu dữ liệu công cụ và giám sát thay đổi động

- **Bảo mật phiên & truyền tải**: Sử dụng ID phiên làm việc không xác định, an toàn về mặt mật mã, ràng buộc với danh tính người dùng, triển khai quản lý vòng đời phiên đúng cách và không bao giờ dùng phiên làm việc để xác thực

- **Thực hành bảo mật OAuth tốt nhất**: Ngăn chặn tấn công đại diện nhầm lẫn thông qua đồng ý người dùng rõ ràng cho khách hàng đăng ký động, triển khai OAuth 2.1 đúng cách với PKCE và xác thực URI chuyển hướng nghiêm ngặt  

- **Nguyên tắc bảo mật token**: Tránh mẫu chống chuyển tiếp token, xác thực tuyên bố đối tượng token, triển khai token thời gian sống ngắn với xoay vòng an toàn và duy trì ranh giới tin cậy rõ ràng

- **Bảo mật chuỗi cung ứng toàn diện**: Đối xử tất cả thành phần hệ sinh thái AI (mô hình, nhúng, nhà cung cấp ngữ cảnh, API bên ngoài) với mức độ nghiêm ngặt bảo mật tương đương phụ thuộc phần mềm truyền thống

- **Tiến hóa liên tục**: Cập nhật các đặc tả MCP đang phát triển nhanh, đóng góp vào tiêu chuẩn cộng đồng bảo mật và duy trì tư thế bảo mật thích ứng khi giao thức trưởng thành

- **Tích hợp bảo mật Microsoft**: Tận dụng hệ sinh thái bảo mật toàn diện của Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) để tăng cường bảo vệ triển khai MCP

## Tài nguyên toàn diện

### **Tài liệu bảo mật MCP chính thức**
- [Đặc tả MCP (Hiện tại: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Thực hành bảo mật MCP tốt nhất](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Đặc tả ủy quyền MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Kho mã MCP GitHub](https://github.com/modelcontextprotocol)

### **Tiêu chuẩn & Thực hành bảo mật**
- [Thực hành bảo mật OAuth 2.0 tốt nhất (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 bảo mật ứng dụng web](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 cho mô hình ngôn ngữ lớn](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Báo cáo phòng thủ số Microsoft](https://aka.ms/mddr)

### **Nghiên cứu & Phân tích bảo mật AI**
- [Tiêm lệnh nhắc trong MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tấn công đầu độc công cụ (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Báo cáo Nghiên cứu Bảo mật MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Giải pháp Bảo mật Microsoft**
- [Tài liệu Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Dịch vụ Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Bảo mật Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Thực hành tốt nhất Quản lý Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Bảo mật Nâng cao GitHub](https://github.com/security/advanced-security)

### **Hướng dẫn & Bài học Triển khai**
- [Quản lý API Azure làm Cổng xác thực MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Xác thực Microsoft Entra ID với Máy chủ MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Lưu trữ Token An toàn và Mã hóa (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Bảo mật Chuỗi Cung ứng**
- [Bảo mật Azure DevOps](https://azure.microsoft.com/products/devops)
- [Bảo mật Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Hành trình Bảo mật Chuỗi Cung ứng Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Tài liệu Bảo mật Bổ sung**

Để có hướng dẫn bảo mật toàn diện, tham khảo các tài liệu chuyên biệt trong phần này:

- **[Thực hành Bảo mật MCP Tốt nhất 2025](./mcp-security-best-practices-2025.md)** - Thực hành bảo mật tốt nhất đầy đủ cho triển khai MCP
- **[Triển khai Azure Content Safety](./azure-content-safety-implementation.md)** - Ví dụ triển khai thực tế cho tích hợp Azure Content Safety  
- **[Kiểm soát Bảo mật MCP 2025](./mcp-security-controls-2025.md)** - Các kiểm soát và kỹ thuật bảo mật mới nhất cho triển khai MCP
- **[Tham khảo Nhanh Thực hành Tốt nhất MCP](./mcp-best-practices.md)** - Hướng dẫn tham khảo nhanh các thực hành bảo mật MCP thiết yếu

---

## Tiếp theo

Tiếp theo: [Chương 3: Bắt đầu](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->