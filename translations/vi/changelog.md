# Changelog: MCP cho Khóa học Người mới bắt đầu

Tài liệu này ghi lại tất cả các thay đổi quan trọng được thực hiện đối với chương trình giảng dạy Model Context Protocol (MCP) cho Người mới bắt đầu. Các thay đổi được ghi lại theo thứ tự thời gian ngược (thay đổi mới nhất trước).

## 18 tháng 12, 2025

### Cập nhật Tài liệu Bảo mật - Đặc tả MCP 2025-11-25

#### Thực hành Bảo mật MCP Tốt nhất (02-Security/mcp-best-practices.md) - Cập nhật Phiên bản Đặc tả
- **Cập nhật Phiên bản Giao thức**: Cập nhật tham chiếu đến Đặc tả MCP mới nhất 2025-11-25 (phát hành ngày 25 tháng 11 năm 2025)
  - Cập nhật tất cả các tham chiếu phiên bản đặc tả từ 2025-06-18 thành 2025-11-25
  - Cập nhật các tham chiếu ngày tài liệu từ ngày 18 tháng 8 năm 2025 thành ngày 18 tháng 12 năm 2025
  - Xác minh tất cả các URL đặc tả trỏ đến tài liệu hiện tại
- **Xác thực Nội dung**: Kiểm tra toàn diện các thực hành bảo mật tốt nhất theo tiêu chuẩn mới nhất
  - **Giải pháp Bảo mật Microsoft**: Xác minh thuật ngữ và liên kết hiện tại cho Prompt Shields (trước đây là "Phát hiện rủi ro Jailbreak"), Azure Content Safety, Microsoft Entra ID và Azure Key Vault
  - **Bảo mật OAuth 2.1**: Xác nhận phù hợp với các thực hành bảo mật OAuth mới nhất
  - **Tiêu chuẩn OWASP**: Xác thực các tham chiếu OWASP Top 10 cho LLMs vẫn còn hợp lệ
  - **Dịch vụ Azure**: Xác minh tất cả các liên kết tài liệu Microsoft Azure và thực hành tốt nhất
- **Phù hợp Tiêu chuẩn**: Tất cả các tiêu chuẩn bảo mật được tham chiếu đều được xác nhận là hiện hành
  - Khung Quản lý Rủi ro AI của NIST
  - ISO 27001:2022
  - Thực hành Bảo mật OAuth 2.1 Tốt nhất
  - Khung bảo mật và tuân thủ Azure
- **Tài nguyên Triển khai**: Xác minh tất cả các liên kết hướng dẫn và tài nguyên triển khai
  - Mẫu xác thực Azure API Management
  - Hướng dẫn tích hợp Microsoft Entra ID
  - Quản lý bí mật Azure Key Vault
  - Các pipeline DevSecOps và giải pháp giám sát

### Đảm bảo Chất lượng Tài liệu
- **Tuân thủ Đặc tả**: Đảm bảo tất cả các yêu cầu bảo mật MCP bắt buộc (PHẢI/PHẢI KHÔNG) phù hợp với đặc tả mới nhất
- **Tính Cập nhật của Tài nguyên**: Xác minh tất cả các liên kết bên ngoài đến tài liệu Microsoft, tiêu chuẩn bảo mật và hướng dẫn triển khai
- **Phủ sóng Thực hành Tốt nhất**: Xác nhận bao phủ toàn diện các chủ đề xác thực, ủy quyền, mối đe dọa AI đặc thù, bảo mật chuỗi cung ứng và mẫu doanh nghiệp

## 6 tháng 10, 2025

### Mở rộng Phần Bắt đầu – Sử dụng Máy chủ Nâng cao & Xác thực Đơn giản

#### Sử dụng Máy chủ Nâng cao (03-GettingStarted/10-advanced)
- **Thêm Chương Mới**: Giới thiệu hướng dẫn toàn diện về sử dụng máy chủ MCP nâng cao, bao gồm cả kiến trúc máy chủ thông thường và cấp thấp.
  - **Máy chủ Thông thường vs. Cấp thấp**: So sánh chi tiết và ví dụ mã Python và TypeScript cho cả hai phương pháp.
  - **Thiết kế Dựa trên Handler**: Giải thích quản lý công cụ/tài nguyên/prompt dựa trên handler cho các triển khai máy chủ có thể mở rộng và linh hoạt.
  - **Mẫu Thực tiễn**: Các kịch bản thực tế nơi các mẫu máy chủ cấp thấp có lợi cho các tính năng và kiến trúc nâng cao.

#### Xác thực Đơn giản (03-GettingStarted/11-simple-auth)
- **Thêm Chương Mới**: Hướng dẫn từng bước triển khai xác thực đơn giản trong máy chủ MCP.
  - **Khái niệm Xác thực**: Giải thích rõ ràng về xác thực so với ủy quyền, và xử lý thông tin đăng nhập.
  - **Triển khai Xác thực Cơ bản**: Mẫu xác thực dựa trên middleware trong Python (Starlette) và TypeScript (Express), kèm ví dụ mã.
  - **Tiến tới Bảo mật Nâng cao**: Hướng dẫn bắt đầu với xác thực đơn giản và tiến tới OAuth 2.1 và RBAC, kèm tham chiếu đến các mô-đun bảo mật nâng cao.

Các bổ sung này cung cấp hướng dẫn thực tiễn, trực tiếp để xây dựng các triển khai máy chủ MCP mạnh mẽ, an toàn và linh hoạt hơn, kết nối các khái niệm nền tảng với các mẫu sản xuất nâng cao.

## 29 tháng 9, 2025

### MCP Server Database Integration Labs - Lộ trình Học Tập Thực hành Toàn diện

#### 11-MCPServerHandsOnLabs - Khóa học Tích hợp Cơ sở dữ liệu Hoàn chỉnh Mới
- **Lộ trình Học 13 Lab Hoàn chỉnh**: Thêm khóa học thực hành toàn diện để xây dựng máy chủ MCP sẵn sàng sản xuất với tích hợp cơ sở dữ liệu PostgreSQL
  - **Triển khai Thực tế**: Trường hợp sử dụng phân tích bán lẻ Zava minh họa các mẫu doanh nghiệp cấp cao
  - **Tiến trình Học có Cấu trúc**:
    - **Lab 00-03: Nền tảng** - Giới thiệu, Kiến trúc Cốt lõi, Bảo mật & Đa người thuê, Thiết lập Môi trường
    - **Lab 04-06: Xây dựng Máy chủ MCP** - Thiết kế & Sơ đồ Cơ sở dữ liệu, Triển khai Máy chủ MCP, Phát triển Công cụ  
    - **Lab 07-09: Tính năng Nâng cao** - Tích hợp Tìm kiếm Ngữ nghĩa, Kiểm thử & Gỡ lỗi, Tích hợp VS Code
    - **Lab 10-12: Sản xuất & Thực hành Tốt nhất** - Chiến lược Triển khai, Giám sát & Quan sát, Thực hành Tốt nhất & Tối ưu hóa
  - **Công nghệ Doanh nghiệp**: Framework FastMCP, PostgreSQL với pgvector, nhúng Azure OpenAI, Azure Container Apps, Application Insights
  - **Tính năng Nâng cao**: Bảo mật Cấp độ Hàng (RLS), tìm kiếm ngữ nghĩa, truy cập dữ liệu đa người thuê, nhúng vector, giám sát thời gian thực

#### Chuẩn hóa Thuật ngữ - Chuyển đổi Module thành Lab
- **Cập nhật Tài liệu Toàn diện**: Cập nhật hệ thống tất cả các file README trong 11-MCPServerHandsOnLabs để sử dụng thuật ngữ "Lab" thay vì "Module"
  - **Tiêu đề Phần**: Cập nhật "What This Module Covers" thành "What This Lab Covers" trên tất cả 13 lab
  - **Mô tả Nội dung**: Thay đổi "This module provides..." thành "This lab provides..." trong toàn bộ tài liệu
  - **Mục tiêu Học tập**: Cập nhật "By the end of this module..." thành "By the end of this lab..."
  - **Liên kết Điều hướng**: Chuyển đổi tất cả tham chiếu "Module XX:" thành "Lab XX:" trong các liên kết chéo và điều hướng
  - **Theo dõi Hoàn thành**: Cập nhật "After completing this module..." thành "After completing this lab..."
  - **Giữ Nguyên Tham chiếu Kỹ thuật**: Giữ nguyên các tham chiếu module Python trong file cấu hình (ví dụ, `"module": "mcp_server.main"`)

#### Cải tiến Hướng dẫn Học tập (study_guide.md)
- **Bản đồ Chương trình Trực quan**: Thêm phần mới "11. Database Integration Labs" với hình ảnh cấu trúc lab toàn diện
- **Cấu trúc Kho Lưu trữ**: Cập nhật từ mười lên mười một phần chính với mô tả chi tiết 11-MCPServerHandsOnLabs
- **Hướng dẫn Lộ trình Học**: Cải thiện chỉ dẫn điều hướng bao phủ các phần 00-11
- **Phủ sóng Công nghệ**: Thêm chi tiết tích hợp FastMCP, PostgreSQL, dịch vụ Azure
- **Kết quả Học tập**: Nhấn mạnh phát triển máy chủ sẵn sàng sản xuất, mẫu tích hợp cơ sở dữ liệu và bảo mật doanh nghiệp

#### Cải tiến Cấu trúc README Chính
- **Thuật ngữ Dựa trên Lab**: Cập nhật README.md chính trong 11-MCPServerHandsOnLabs để nhất quán sử dụng cấu trúc "Lab"
- **Tổ chức Lộ trình Học**: Tiến trình rõ ràng từ khái niệm nền tảng đến triển khai nâng cao và sản xuất
- **Tập trung Thực tế**: Nhấn mạnh học tập thực hành với các mẫu và công nghệ doanh nghiệp cấp cao

### Cải tiến Chất lượng & Tính nhất quán Tài liệu
- **Nhấn mạnh Học tập Thực hành**: Tăng cường phương pháp dựa trên lab trong toàn bộ tài liệu
- **Tập trung Mẫu Doanh nghiệp**: Nêu bật các triển khai sẵn sàng sản xuất và cân nhắc bảo mật doanh nghiệp
- **Tích hợp Công nghệ**: Bao phủ toàn diện các dịch vụ Azure hiện đại và mẫu tích hợp AI
- **Tiến trình Học**: Lộ trình rõ ràng, có cấu trúc từ khái niệm cơ bản đến triển khai sản xuất

## 26 tháng 9, 2025

### Cải tiến Nghiên cứu Tình huống - Tích hợp GitHub MCP Registry

#### Nghiên cứu Tình huống (09-CaseStudy/) - Tập trung Phát triển Hệ sinh thái
- **README.md**: Mở rộng lớn với nghiên cứu tình huống toàn diện về GitHub MCP Registry
  - **Nghiên cứu Tình huống GitHub MCP Registry**: Nghiên cứu toàn diện mới xem xét việc ra mắt GitHub MCP Registry vào tháng 9 năm 2025
    - **Phân tích Vấn đề**: Xem xét chi tiết các thách thức trong phát hiện và triển khai máy chủ MCP phân mảnh
    - **Kiến trúc Giải pháp**: Phương pháp registry tập trung của GitHub với cài đặt VS Code một cú nhấp chuột
    - **Tác động Kinh doanh**: Cải thiện đo lường được trong việc onboard và năng suất nhà phát triển
    - **Giá trị Chiến lược**: Tập trung vào triển khai agent mô-đun và khả năng tương tác công cụ chéo
    - **Phát triển Hệ sinh thái**: Định vị như nền tảng cơ sở cho tích hợp agentic
  - **Cấu trúc Nghiên cứu Tình huống Nâng cao**: Cập nhật tất cả bảy nghiên cứu tình huống với định dạng nhất quán và mô tả toàn diện
    - Azure AI Travel Agents: Nhấn mạnh điều phối đa agent
    - Tích hợp Azure DevOps: Tập trung tự động hóa quy trình làm việc
    - Truy xuất Tài liệu Thời gian Thực: Triển khai client console Python
    - Trình tạo Kế hoạch Học Tương tác: Ứng dụng web hội thoại Chainlit
    - Tài liệu Trong Trình soạn thảo: Tích hợp VS Code và GitHub Copilot
    - Azure API Management: Mẫu tích hợp API doanh nghiệp
    - GitHub MCP Registry: Phát triển hệ sinh thái và nền tảng cộng đồng
  - **Kết luận Toàn diện**: Viết lại phần kết luận nhấn mạnh bảy nghiên cứu tình huống trải dài nhiều khía cạnh triển khai MCP
    - Tích hợp Doanh nghiệp, Điều phối Đa Agent, Năng suất Nhà phát triển
    - Phát triển Hệ sinh thái, Ứng dụng Giáo dục phân loại
    - Cải thiện hiểu biết về mẫu kiến trúc, chiến lược triển khai và thực hành tốt nhất
    - Nhấn mạnh MCP như giao thức trưởng thành, sẵn sàng sản xuất

#### Cập nhật Hướng dẫn Học tập (study_guide.md)
- **Bản đồ Chương trình Trực quan**: Cập nhật sơ đồ tư duy để bao gồm GitHub MCP Registry trong phần Nghiên cứu Tình huống
- **Mô tả Nghiên cứu Tình huống**: Nâng cao từ mô tả chung sang phân tích chi tiết bảy nghiên cứu tình huống toàn diện
- **Cấu trúc Kho Lưu trữ**: Cập nhật phần 10 để phản ánh phạm vi nghiên cứu tình huống toàn diện với chi tiết triển khai cụ thể
- **Tích hợp Changelog**: Thêm mục ngày 26 tháng 9 năm 2025 ghi lại việc bổ sung GitHub MCP Registry và cải tiến nghiên cứu tình huống
- **Cập nhật Ngày tháng**: Cập nhật dấu thời gian chân trang để phản ánh phiên bản mới nhất (26 tháng 9, 2025)

### Cải tiến Chất lượng Tài liệu
- **Nâng cao Tính nhất quán**: Chuẩn hóa định dạng và cấu trúc nghiên cứu tình huống trên tất cả bảy ví dụ
- **Phủ sóng Toàn diện**: Nghiên cứu tình huống bao phủ doanh nghiệp, năng suất nhà phát triển và phát triển hệ sinh thái
- **Định vị Chiến lược**: Tăng cường tập trung MCP như nền tảng cơ sở cho triển khai hệ thống agentic
- **Tích hợp Tài nguyên**: Cập nhật tài nguyên bổ sung bao gồm liên kết GitHub MCP Registry

## 15 tháng 9, 2025

### Mở rộng Chủ đề Nâng cao - Giao thức Tùy chỉnh & Kỹ thuật Ngữ cảnh

#### Giao thức Tùy chỉnh MCP (05-AdvancedTopics/mcp-transport/) - Hướng dẫn Triển khai Nâng cao Mới
- **README.md**: Hướng dẫn triển khai đầy đủ cho các cơ chế giao thức MCP tùy chỉnh
  - **Giao thức Azure Event Grid**: Triển khai giao thức sự kiện không máy chủ toàn diện
    - Ví dụ C#, TypeScript và Python tích hợp Azure Functions
    - Mẫu kiến trúc sự kiện cho giải pháp MCP có thể mở rộng
    - Bộ nhận webhook và xử lý tin nhắn đẩy
  - **Giao thức Azure Event Hubs**: Triển khai giao thức streaming hiệu suất cao
    - Khả năng streaming thời gian thực cho các kịch bản độ trễ thấp
    - Chiến lược phân vùng và quản lý điểm kiểm tra
    - Gom nhóm tin nhắn và tối ưu hiệu suất
  - **Mẫu Tích hợp Doanh nghiệp**: Ví dụ kiến trúc sẵn sàng sản xuất
    - Xử lý MCP phân tán trên nhiều Azure Functions
    - Kiến trúc giao thức lai kết hợp nhiều loại giao thức
    - Chiến lược độ bền, độ tin cậy và xử lý lỗi tin nhắn
  - **Bảo mật & Giám sát**: Tích hợp Azure Key Vault và mẫu quan sát
    - Xác thực danh tính quản lý và truy cập quyền tối thiểu
    - Telemetry Application Insights và giám sát hiệu suất
    - Bộ ngắt mạch và mẫu chịu lỗi
  - **Khung Kiểm thử**: Chiến lược kiểm thử toàn diện cho giao thức tùy chỉnh
    - Kiểm thử đơn vị với test doubles và framework giả lập
    - Kiểm thử tích hợp với Azure Test Containers
    - Cân nhắc kiểm thử hiệu suất và tải

#### Kỹ thuật Ngữ cảnh (05-AdvancedTopics/mcp-contextengineering/) - Lĩnh vực AI Mới Nổi
- **README.md**: Khám phá toàn diện kỹ thuật ngữ cảnh như một lĩnh vực mới nổi
  - **Nguyên tắc Cốt lõi**: Chia sẻ ngữ cảnh đầy đủ, nhận thức quyết định hành động, và quản lý cửa sổ ngữ cảnh
  - **Phù hợp Giao thức MCP**: Cách thiết kế MCP giải quyết các thách thức kỹ thuật ngữ cảnh
    - Giới hạn cửa sổ ngữ cảnh và chiến lược tải dần
    - Xác định mức độ liên quan và truy xuất ngữ cảnh động
    - Xử lý ngữ cảnh đa phương thức và cân nhắc bảo mật
  - **Phương pháp Triển khai**: Kiến trúc đơn luồng so với đa agent
    - Kỹ thuật phân đoạn và ưu tiên ngữ cảnh
    - Tải dần ngữ cảnh và chiến lược nén
    - Phương pháp ngữ cảnh phân lớp và tối ưu truy xuất
  - **Khung Đo lường**: Các chỉ số mới nổi để đánh giá hiệu quả ngữ cảnh
    - Hiệu quả đầu vào, hiệu suất, chất lượng và trải nghiệm người dùng
    - Phương pháp thử nghiệm tối ưu hóa ngữ cảnh
    - Phân tích lỗi và phương pháp cải tiến

#### Cập nhật Điều hướng Chương trình (README.md)
- **Cấu trúc Module Nâng cao**: Cập nhật bảng chương trình để bao gồm các chủ đề nâng cao mới
  - Thêm Kỹ thuật Ngữ cảnh (5.14) và Giao thức Tùy chỉnh (5.15)
  - Định dạng và liên kết điều hướng nhất quán trên tất cả các module
  - Cập nhật mô tả phản ánh phạm vi nội dung hiện tại

### Cải tiến Cấu trúc Thư mục
- **Chuẩn hóa Đặt tên**: Đổi tên "mcp transport" thành "mcp-transport" để nhất quán với các thư mục chủ đề nâng cao khác
- **Tổ chức Nội dung**: Tất cả thư mục 05-AdvancedTopics hiện theo mẫu đặt tên nhất quán (mcp-[topic])

### Cải tiến Chất lượng Tài liệu
- **Phù hợp Đặc tả MCP**: Tất cả nội dung mới tham chiếu Đặc tả MCP 2025-06-18 hiện hành
- **Ví dụ Đa ngôn ngữ**: Ví dụ mã đầy đủ bằng C#, TypeScript và Python
- **Tập trung Doanh nghiệp**: Mẫu sẵn sàng sản xuất và tích hợp đám mây Azure xuyên suốt
- **Tài liệu Trực quan**: Biểu đồ Mermaid cho kiến trúc và trực quan luồng

## 18 tháng 8, 2025

### Cập nhật Toàn diện Tài liệu - Tiêu chuẩn MCP 2025-06-18

#### Thực hành Bảo mật MCP Tốt nhất (02-Security/) - Hiện đại hóa Toàn diện
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Viết lại hoàn toàn phù hợp với Đặc tả MCP 2025-06-18
  - **Yêu cầu bắt buộc**: Thêm các yêu cầu MUST/MUST NOT rõ ràng từ đặc tả chính thức với các chỉ báo trực quan rõ ràng  
  - **12 Thực hành An ninh Cốt lõi**: Tái cấu trúc từ danh sách 15 mục thành các lĩnh vực an ninh toàn diện  
    - Bảo mật Token & Xác thực với tích hợp nhà cung cấp danh tính bên ngoài  
    - Quản lý Phiên & Bảo mật Vận chuyển với các yêu cầu mật mã  
    - Bảo vệ Mối đe dọa Đặc thù AI với tích hợp Microsoft Prompt Shields  
    - Kiểm soát Truy cập & Quyền hạn với nguyên tắc đặc quyền tối thiểu  
    - An toàn Nội dung & Giám sát với tích hợp Azure Content Safety  
    - An ninh Chuỗi Cung ứng với xác minh thành phần toàn diện  
    - Bảo mật OAuth & Ngăn ngừa Confused Deputy với triển khai PKCE  
    - Ứng phó Sự cố & Phục hồi với khả năng tự động hóa  
    - Tuân thủ & Quản trị với sự phù hợp quy định  
    - Kiểm soát An ninh Nâng cao với kiến trúc zero trust  
    - Tích hợp Hệ sinh thái An ninh Microsoft với các giải pháp toàn diện  
    - Tiến hóa An ninh Liên tục với các thực hành thích ứng  
  - **Giải pháp An ninh Microsoft**: Hướng dẫn tích hợp nâng cao cho Prompt Shields, Azure Content Safety, Entra ID và GitHub Advanced Security  
  - **Tài nguyên Triển khai**: Phân loại các liên kết tài nguyên toàn diện theo Tài liệu MCP Chính thức, Giải pháp An ninh Microsoft, Tiêu chuẩn An ninh và Hướng dẫn Triển khai  

#### Kiểm soát An ninh Nâng cao (02-Security/) - Triển khai Doanh nghiệp  
- **MCP-SECURITY-CONTROLS-2025.md**: Cải tổ hoàn toàn với khung an ninh cấp doanh nghiệp  
  - **9 Lĩnh vực An ninh Toàn diện**: Mở rộng từ các kiểm soát cơ bản thành khung doanh nghiệp chi tiết  
    - Xác thực & Ủy quyền Nâng cao với tích hợp Microsoft Entra ID  
    - Bảo mật Token & Kiểm soát Chống Passthrough với xác thực toàn diện  
    - Kiểm soát Bảo mật Phiên với ngăn chặn chiếm đoạt  
    - Kiểm soát An ninh Đặc thù AI với ngăn chặn tiêm prompt và đầu độc công cụ  
    - Ngăn ngừa Tấn công Confused Deputy với bảo mật proxy OAuth  
    - Bảo mật Thực thi Công cụ với sandboxing và cô lập  
    - Kiểm soát An ninh Chuỗi Cung ứng với xác minh phụ thuộc  
    - Kiểm soát Giám sát & Phát hiện với tích hợp SIEM  
    - Ứng phó Sự cố & Phục hồi với khả năng tự động hóa  
  - **Ví dụ Triển khai**: Thêm các khối cấu hình YAML chi tiết và ví dụ mã  
  - **Tích hợp Giải pháp Microsoft**: Bao phủ toàn diện các dịch vụ bảo mật Azure, GitHub Advanced Security và quản lý danh tính doanh nghiệp  

#### An ninh Chủ đề Nâng cao (05-AdvancedTopics/mcp-security/) - Triển khai Sẵn sàng Sản xuất  
- **README.md**: Viết lại hoàn toàn cho triển khai an ninh doanh nghiệp  
  - **Phù hợp Đặc tả Hiện tại**: Cập nhật theo Đặc tả MCP 2025-06-18 với các yêu cầu an ninh bắt buộc  
  - **Xác thực Nâng cao**: Tích hợp Microsoft Entra ID với các ví dụ toàn diện .NET và Java Spring Security  
  - **Tích hợp An ninh AI**: Triển khai Microsoft Prompt Shields và Azure Content Safety với ví dụ Python chi tiết  
  - **Giảm thiểu Mối đe dọa Nâng cao**: Ví dụ triển khai toàn diện cho  
    - Ngăn ngừa Tấn công Confused Deputy với PKCE và xác thực sự đồng ý của người dùng  
    - Ngăn chặn Token Passthrough với xác thực audience và quản lý token an toàn  
    - Ngăn chặn Chiếm đoạt Phiên với ràng buộc mật mã và phân tích hành vi  
  - **Tích hợp An ninh Doanh nghiệp**: Giám sát Azure Application Insights, pipeline phát hiện mối đe dọa và an ninh chuỗi cung ứng  
  - **Danh sách Kiểm tra Triển khai**: Kiểm soát an ninh bắt buộc so với khuyến nghị rõ ràng với lợi ích hệ sinh thái an ninh Microsoft  

### Chất lượng Tài liệu & Phù hợp Tiêu chuẩn  
- **Tham chiếu Đặc tả**: Cập nhật tất cả tham chiếu theo Đặc tả MCP 2025-06-18 hiện tại  
- **Hệ sinh thái An ninh Microsoft**: Hướng dẫn tích hợp nâng cao xuyên suốt tài liệu an ninh  
- **Triển khai Thực tiễn**: Thêm ví dụ mã chi tiết trong .NET, Java và Python với các mẫu doanh nghiệp  
- **Tổ chức Tài nguyên**: Phân loại toàn diện tài liệu chính thức, tiêu chuẩn an ninh và hướng dẫn triển khai  
- **Chỉ báo Trực quan**: Đánh dấu rõ ràng các yêu cầu bắt buộc so với thực hành khuyến nghị  

#### Khái niệm Cốt lõi (01-CoreConcepts/) - Hiện đại hóa Toàn diện  
- **Cập nhật Phiên bản Giao thức**: Tham chiếu Đặc tả MCP 2025-06-18 hiện tại với định dạng ngày (YYYY-MM-DD)  
- **Tinh chỉnh Kiến trúc**: Mô tả nâng cao về Hosts, Clients và Servers phản ánh mẫu kiến trúc MCP hiện tại  
  - Hosts được định nghĩa rõ ràng là các ứng dụng AI điều phối nhiều kết nối client MCP  
  - Clients mô tả là các kết nối giao thức duy trì quan hệ một-một với server  
  - Servers được nâng cấp với các kịch bản triển khai cục bộ và từ xa  
- **Tái cấu trúc Primitive**: Cải tổ hoàn toàn các primitive server và client  
  - Primitive Server: Tài nguyên (nguồn dữ liệu), Prompts (mẫu), Công cụ (hàm thực thi) với giải thích và ví dụ chi tiết  
  - Primitive Client: Sampling (hoàn thành LLM), Elicitation (đầu vào người dùng), Logging (gỡ lỗi/giám sát)  
  - Cập nhật theo mẫu phương thức khám phá (`*/list`), truy xuất (`*/get`), và thực thi (`*/call`) hiện tại  
- **Kiến trúc Giao thức**: Giới thiệu mô hình kiến trúc hai lớp  
  - Lớp Dữ liệu: Nền tảng JSON-RPC 2.0 với quản lý vòng đời và primitives  
  - Lớp Vận chuyển: STDIO (cục bộ) và HTTP có thể stream với SSE (vận chuyển từ xa)  
- **Khung An ninh**: Nguyên tắc an ninh toàn diện bao gồm sự đồng ý rõ ràng của người dùng, bảo vệ quyền riêng tư dữ liệu, an toàn thực thi công cụ và bảo mật lớp vận chuyển  
- **Mẫu Giao tiếp**: Cập nhật các thông điệp giao thức thể hiện luồng khởi tạo, khám phá, thực thi và thông báo  
- **Ví dụ Mã**: Làm mới ví dụ đa ngôn ngữ (.NET, Java, Python, JavaScript) phản ánh mẫu SDK MCP hiện tại  

#### An ninh (02-Security/) - Cải tổ An ninh Toàn diện  
- **Phù hợp Tiêu chuẩn**: Hoàn toàn phù hợp với yêu cầu an ninh Đặc tả MCP 2025-06-18  
- **Tiến hóa Xác thực**: Tài liệu tiến hóa từ server OAuth tùy chỉnh sang ủy quyền nhà cung cấp danh tính bên ngoài (Microsoft Entra ID)  
- **Phân tích Mối đe dọa Đặc thù AI**: Mở rộng bao phủ các vectơ tấn công AI hiện đại  
  - Kịch bản tấn công tiêm prompt chi tiết với ví dụ thực tế  
  - Cơ chế đầu độc công cụ và mẫu tấn công "rug pull"  
  - Đầu độc cửa sổ ngữ cảnh và tấn công gây nhầm lẫn mô hình  
- **Giải pháp An ninh AI Microsoft**: Bao phủ toàn diện hệ sinh thái an ninh Microsoft  
  - AI Prompt Shields với phát hiện nâng cao, spotlighting và kỹ thuật delimiter  
  - Mẫu tích hợp Azure Content Safety  
  - GitHub Advanced Security cho bảo vệ chuỗi cung ứng  
- **Giảm thiểu Mối đe dọa Nâng cao**: Kiểm soát an ninh chi tiết cho  
  - Chiếm đoạt phiên với kịch bản tấn công MCP cụ thể và yêu cầu ID phiên mật mã  
  - Vấn đề confused deputy trong kịch bản proxy MCP với yêu cầu đồng ý rõ ràng  
  - Lỗ hổng token passthrough với kiểm soát xác thực bắt buộc  
- **An ninh Chuỗi Cung ứng**: Mở rộng bao phủ chuỗi cung ứng AI bao gồm mô hình nền tảng, dịch vụ embeddings, nhà cung cấp ngữ cảnh và API bên thứ ba  
- **An ninh Nền tảng**: Tăng cường tích hợp với mẫu an ninh doanh nghiệp bao gồm kiến trúc zero trust và hệ sinh thái an ninh Microsoft  
- **Tổ chức Tài nguyên**: Phân loại các liên kết tài nguyên toàn diện theo loại (Tài liệu Chính thức, Tiêu chuẩn, Nghiên cứu, Giải pháp Microsoft, Hướng dẫn Triển khai)  

### Cải tiến Chất lượng Tài liệu  
- **Mục tiêu Học tập Cấu trúc**: Nâng cao mục tiêu học tập với kết quả cụ thể, có thể hành động  
- **Tham chiếu Chéo**: Thêm liên kết giữa các chủ đề an ninh và khái niệm cốt lõi liên quan  
- **Thông tin Hiện tại**: Cập nhật tất cả tham chiếu ngày tháng và liên kết đặc tả theo tiêu chuẩn hiện tại  
- **Hướng dẫn Triển khai**: Thêm hướng dẫn triển khai cụ thể, có thể hành động xuyên suốt cả hai phần  

## 16 tháng 7, 2025  

### README và Cải tiến Điều hướng  
- Thiết kế lại hoàn toàn điều hướng chương trình học trong README.md  
- Thay thế thẻ `<details>` bằng định dạng bảng dễ tiếp cận hơn  
- Tạo các tùy chọn bố cục thay thế trong thư mục "alternative_layouts" mới  
- Thêm ví dụ điều hướng dạng thẻ, dạng tab và dạng accordion  
- Cập nhật phần cấu trúc kho lưu trữ để bao gồm tất cả các tệp mới nhất  
- Nâng cao phần "Cách Sử dụng Chương trình học" với các khuyến nghị rõ ràng  
- Cập nhật liên kết đặc tả MCP để trỏ đến URL chính xác  
- Thêm phần Kỹ thuật Ngữ cảnh (5.14) vào cấu trúc chương trình học  

### Cập nhật Hướng dẫn Học tập  
- Viết lại hoàn toàn hướng dẫn học tập để phù hợp với cấu trúc kho lưu trữ hiện tại  
- Thêm các phần mới cho MCP Clients và Tools, và MCP Servers phổ biến  
- Cập nhật Bản đồ Chương trình học Trực quan để phản ánh chính xác tất cả các chủ đề  
- Nâng cao mô tả các Chủ đề Nâng cao để bao phủ tất cả các lĩnh vực chuyên biệt  
- Cập nhật phần Nghiên cứu Tình huống để phản ánh các ví dụ thực tế  
- Thêm nhật ký thay đổi toàn diện này  

### Đóng góp Cộng đồng (06-CommunityContributions/)  
- Thêm thông tin chi tiết về các server MCP cho tạo hình ảnh  
- Thêm phần toàn diện về sử dụng Claude trong VSCode  
- Thêm hướng dẫn thiết lập và sử dụng client terminal Cline  
- Cập nhật phần client MCP để bao gồm tất cả các tùy chọn client phổ biến  
- Nâng cao ví dụ đóng góp với các mẫu mã chính xác hơn  

### Chủ đề Nâng cao (05-AdvancedTopics/)  
- Tổ chức tất cả thư mục chủ đề chuyên biệt với tên gọi nhất quán  
- Thêm tài liệu và ví dụ kỹ thuật ngữ cảnh  
- Thêm tài liệu tích hợp agent Foundry  
- Nâng cao tài liệu tích hợp an ninh Entra ID  

## 11 tháng 6, 2025  

### Tạo Mới Ban đầu  
- Phát hành phiên bản đầu tiên của chương trình MCP cho Người mới bắt đầu  
- Tạo cấu trúc cơ bản cho tất cả 10 phần chính  
- Triển khai Bản đồ Chương trình học Trực quan để điều hướng  
- Thêm các dự án mẫu ban đầu bằng nhiều ngôn ngữ lập trình  

### Bắt đầu (03-GettingStarted/)  
- Tạo ví dụ triển khai server đầu tiên  
- Thêm hướng dẫn phát triển client  
- Bao gồm hướng dẫn tích hợp client LLM  
- Thêm tài liệu tích hợp VS Code  
- Triển khai ví dụ server Server-Sent Events (SSE)  

### Khái niệm Cốt lõi (01-CoreConcepts/)  
- Thêm giải thích chi tiết về kiến trúc client-server  
- Tạo tài liệu về các thành phần giao thức chính  
- Tài liệu hóa các mẫu thông điệp trong MCP  

## 23 tháng 5, 2025  

### Cấu trúc Kho lưu trữ  
- Khởi tạo kho lưu trữ với cấu trúc thư mục cơ bản  
- Tạo các tệp README cho mỗi phần chính  
- Thiết lập hạ tầng dịch thuật  
- Thêm tài sản hình ảnh và sơ đồ  

### Tài liệu  
- Tạo README.md ban đầu với tổng quan chương trình học  
- Thêm CODE_OF_CONDUCT.md và SECURITY.md  
- Thiết lập SUPPORT.md với hướng dẫn nhận trợ giúp  
- Tạo cấu trúc hướng dẫn học tập sơ bộ  

## 15 tháng 4, 2025  

### Lập kế hoạch và Khung  
- Lập kế hoạch ban đầu cho chương trình MCP cho Người mới bắt đầu  
- Xác định mục tiêu học tập và đối tượng mục tiêu  
- Phác thảo cấu trúc 10 phần của chương trình học  
- Phát triển khung khái niệm cho ví dụ và nghiên cứu tình huống  
- Tạo các ví dụ nguyên mẫu ban đầu cho các khái niệm chính  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->