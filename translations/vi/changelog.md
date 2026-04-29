# Changelog: Giáo trình MCP cho Người mới bắt đầu

Tài liệu này lưu giữ tất cả các thay đổi quan trọng đã thực hiện đối với giáo trình Model Context Protocol (MCP) cho Người mới bắt đầu. Các thay đổi được ghi lại theo thứ tự đảo ngược thời gian (thay đổi mới nhất trước).

## 11 tháng 4, 2026

### Bài học mới, sửa lỗi tài liệu và cập nhật phụ thuộc

#### Nội dung giáo trình mới được thêm vào

**Module 05 - Chủ đề nâng cao**
- **Bài học 5.17: Lập luận đa tác nhân đối kháng với MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Hướng dẫn toàn diện mới bao gồm mẫu tranh luận đối kháng cho hệ thống đa tác nhân
  - Sơ đồ kiến trúc Mermaid: hai tác nhân → máy chủ MCP chung → bản ghi cuộc tranh luận → thẩm phán → phán quyết
  - Máy chủ công cụ MCP chung (`web_search` + `run_python`) được triển khai bằng Python và TypeScript
  - Các lời nhắc hệ thống đối lập (CHỐNG / ỦNG HỘ / Thẩm phán) với yêu cầu sử dụng công cụ rõ ràng
  - Bộ điều phối tranh luận bằng Python, TypeScript và C# quản lý vòng và tuyến lập luận
  - Kết nối `ClientSession` của MCP cho bộ điều phối gọi công cụ thực tế
  - Bảng các trường hợp sử dụng (phát hiện ảo giác, mô hình hóa mối đe dọa, xem xét thiết kế API, xác minh sự thật, lựa chọn công nghệ)
  - Các cân nhắc bảo mật: thực thi trong vùng an toàn, xác thực cuộc gọi công cụ, giới hạn tốc độ, ghi nhật ký kiểm toán
  - Bài tập có cấu trúc với ba kịch bản thực tế (đánh giá code, quyết định kiến trúc, quản lý nội dung)

#### Sửa lỗi tài liệu

**Module 03 - Bắt đầu**
- **05-stdio-server/README.md**: Sửa ví dụ máy chủ stdio TypeScript chưa hoàn chỉnh — thêm khởi tạo transport thiếu (`new StdioServerTransport()`) và gọi `server.connect(transport)` để khớp với ví dụ Python và .NET trong cùng phần
- **14-sampling/README.md**: Sửa lỗi chính tả — chỉnh `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Cập nhật giáo trình

**README chính**
- Thêm mục 5.17 (Lập luận đa tác nhân đối kháng với MCP) vào bảng giáo trình với liên kết trực tiếp đến bài học mới

**05-AdvancedTopics/README.md**
- Thêm hàng bài học 5.17 vào bảng bài học

**study_guide.md**
- Thêm chủ đề Lập luận đa tác nhân đối kháng vào bản đồ tư duy và mô tả văn bản của Chủ đề nâng cao

#### Sửa lỗi code và bảo mật

**Module 05 - Tác nhân đối kháng (`mcp-adversarial-agents`)**
- **Sửa lỗi bảo mật — lệnh chèn**: Thay thế nội suy shell `execSync` bằng `execFile` + `promisify` trong công cụ `run_python` TypeScript, loại bỏ bề mặt lỗ hổng thực thi lệnh (mã do LLM điều khiển giờ được truyền dưới dạng phần tử argv dạng literal, không qua shell)
- **Kết nối vòng gọi công cụ MCP**: Cập nhật bộ điều phối tranh luận Python dùng client `AsyncAnthropic` không chặn (thay cho `Anthropic` đồng bộ), truyền trực tiếp `ClientSession` sống tới mỗi lượt tác nhân, lấy danh sách công cụ qua `session.list_tools()` mỗi lượt, và gửi các khối `tool_use` qua `session.call_tool()` trong vòng lặp cho tới khi mô hình phát ra phản hồi văn bản cuối cùng

#### Cập nhật phụ thuộc

- Nâng cấp `hono` lên 4.12.12 trong nhiều gói (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Nâng cấp `@hono/node-server` từ 1.19.11 lên 1.19.13 trong các gói TypeScript
- Nâng cấp `cryptography` từ 46.0.5 lên 46.0.7 trong các gói Python (10-StreamliningAIWorkflows lab 3 và 4)
- Nâng cấp `lodash` từ 4.17.23 lên 4.18.1 trong trình kiểm tra 10-StreamliningAIWorkflows

#### Dịch thuật

- Đồng bộ các bản dịch cho hơn 48 ngôn ngữ với các thay đổi nguồn mới nhất (cập nhật i18n)

---

## 5 tháng 2, 2026

### Cải tiến xác thực và điều hướng toàn kho

#### Nội dung giáo trình mới được thêm vào

**Module 03 - Bắt đầu**
- **12-mcp-hosts/README.md**: Hướng dẫn toàn diện mới để thiết lập các máy chủ MCP
  - Ví dụ cấu hình Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Mẫu cấu hình JSON cho tất cả các máy chủ chính
  - Bảng so sánh các loại transport (stdio, SSE/HTTP, WebSocket)
  - Khắc phục sự cố kết nối phổ biến
  - Thực hành tốt về bảo mật khi cấu hình máy chủ

- **13-mcp-inspector/README.md**: Hướng dẫn mới để gỡ lỗi MCP Inspector
  - Phương pháp cài đặt (npx, npm toàn cục, từ mã nguồn)
  - Kết nối với máy chủ qua stdio và HTTP/SSE
  - Công cụ, tài nguyên và trình tự làm việc với lời nhắc kiểm thử
  - Tích hợp MCP Inspector với VS Code
  - Các kịch bản gỡ lỗi thường gặp và cách giải quyết

**Module 04 - Triển khai thực tế**
- **pagination/README.md**: Hướng dẫn mới về triển khai phân trang
  - Các mẫu phân trang dựa trên con trỏ trong Python, TypeScript, Java
  - Xử lý phân trang phía khách
  - Chiến lược thiết kế con trỏ (mờ vs cấu trúc)
  - Khuyến nghị tối ưu hóa hiệu suất

**Module 05 - Chủ đề nâng cao**
- **mcp-protocol-features/README.md**: Phân tích sâu các tính năng giao thức mới
  - Triển khai thông báo tiến độ
  - Mẫu hủy bỏ yêu cầu
  - Mẫu tài nguyên với mẫu URI
  - Quản lý vòng đời máy chủ
  - Kiểm soát mức độ ghi nhật ký
  - Mẫu xử lý lỗi với mã JSON-RPC

#### Sửa lỗi điều hướng (cập nhật 24+ tệp)

**README Module chính**
 Liên kết bây giờ đến cả bài học đầu tiên VÀ module tiếp theo

**Các tệp phụ 02-Security**
- Tất cả 5 tài liệu hỗ trợ bảo mật giờ có điều hướng "Tiếp theo là gì":

**Tệp nghiên cứu tình huống 09-CaseStudy**
- Tất cả các tệp nghiên cứu tình huống giờ có điều hướng tuần tự:

**Lab 10-StreamliningAI**
Thêm phần "Tiếp theo là gì" vào tổng quan Module 10 và Module 11

#### Sửa lỗi code và nội dung

**Cập nhật SDK và phụ thuộc**
Sửa phiên bản openai trống thành `^4.95.0`
Cập nhật SDK từ `^1.8.0` lên `>=1.26.0`
Cập nhật phiên bản mcp thành `>=1.26.0`

**Sửa lỗi code**
Sửa model không hợp lệ `gpt-4o-mini` thành `gpt-4.1-mini`

**Sửa lỗi nội dung**
Sửa liên kết hỏng `READMEmd` → `README.md`, sửa tiêu đề giáo trình `Module 1-3` → `Module 0-3`, sửa đường dẫn phân biệt chữ hoa chữ thường
Xóa nội dung trùng lặp bị hỏng của Nghiên cứu tình huống 5

**Cải tiến hướng dẫn dành cho người mới**
Thêm lời giới thiệu đúng đắn, mục tiêu học tập và điều kiện tiên quyết cho người mới bắt đầu

#### Cập nhật giáo trình

**README chính**
- Thêm các mục 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Phân trang), 5.16 (Tính năng giao thức) vào bảng giáo trình

**README các Module**
Thêm bài học 12 và 13 vào danh sách bài học
Thêm phần Hướng dẫn thực tế với liên kết phân trang
Thêm bài học 5.15 (Transport tùy chỉnh) và 5.16 (Tính năng giao thức)

**study_guide.md**
- Cập nhật sơ đồ tư duy với tất cả chủ đề mới: Thiết lập MCP Hosts, MCP Inspector, Chiến lược phân trang, Phân tích sâu Tính năng giao thức

## 28 tháng 1, 2026

### Đánh giá tuân thủ đặc tả MCP 2025-11-25

#### Nâng cao Khái niệm cốt lõi (01-CoreConcepts/)
- **Primitive Client Mới - Roots**: Thêm tài liệu toàn diện về primitive Roots client, cho phép máy chủ hiểu ranh giới hệ thống tập tin và quyền truy cập
- **Chú thích Công cụ**: Thêm tài liệu về các chú thích hành vi công cụ (`readOnlyHint`, `destructiveHint`) để quyết định thực thi công cụ tốt hơn
- **Gọi công cụ trong Sampling**: Cập nhật tài liệu Sampling để bao gồm các tham số `tools` và `toolChoice` cho việc gọi công cụ điều khiển bởi mô hình khi yêu cầu sampling
- **Kích thích chế độ URL**: Thêm tài liệu về kích thích dựa trên URL cho các tương tác web bên ngoài do máy chủ khởi tạo
- **Tasks (Thử nghiệm)**: Thêm phần mới tài liệu tính năng Tasks thử nghiệm cho wrapper thực thi bền và truy xuất kết quả hoãn
- **Hỗ trợ Icon**: Ghi chú rằng công cụ, tài nguyên, mẫu tài nguyên và lời nhắc bây giờ có thể bao gồm icon làm metadata phụ

#### Cập nhật tài liệu
- **README.md**: Thêm tham chiếu phiên bản MCP Specification 2025-11-25 và giải thích phiên bản theo ngày
- **study_guide.md**: Cập nhật bản đồ giáo trình để bao gồm Tasks và Chú thích Công cụ trong phần Khái niệm cốt lõi; cập nhật dấu thời gian tài liệu

#### Kiểm tra tuân thủ đặc tả
- **Phiên bản giao thức**: Xác nhận tất cả tài liệu tham chiếu MCP Specification 2025-11-25 hiện hành
- **Đồng bộ kiến trúc**: Xác nhận tài liệu kiến trúc hai lớp (Lớp Dữ liệu + Lớp Giao vận) chính xác
- **Tài liệu primitives**: Xác nhận primitives máy chủ (Resources, Prompts, Tools) và primitives client (Sampling, Elicitation, Logging, Roots)
- **Cơ chế Transport**: Xác minh tài liệu transport STDIO và Streamable HTTP chính xác
- **Hướng dẫn Bảo mật**: Xác nhận phù hợp với tài liệu Thực hành tốt về Bảo mật MCP hiện hành

#### Các tính năng chính MCP 2025-11-25 được tài liệu hóa
- **OpenID Connect Discovery**: Phát hiện máy chủ xác thực qua OIDC
- **Tài liệu siêu dữ liệu Client ID OAuth**: Cơ chế đăng ký client được khuyến nghị
- **JSON Schema 2020-12**: Bộ quy tắc mặc định cho định nghĩa schema MCP
- **Hệ thống phân tầng SDK**: Các yêu cầu chính thức cho hỗ trợ và bảo trì tính năng SDK
- **Cơ cấu quản trị**: Chính thức hóa các Nhóm làm việc và Nhóm quan tâm trong quản trị MCP

### Cập nhật lớn tài liệu bảo mật (02-Security/)

#### Tích hợp Hội thảo MCP Security Summit Workshop (Sherpa)
- **Tài nguyên đào tạo thực hành mới**: Thêm tích hợp toàn diện với [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) xuyên suốt các tài liệu bảo mật
- **Phủ sóng tuyến đường thám hiểm**: Tài liệu tiến trình từng trại từ Base Camp đến Summit đầy đủ
- **Đồng bộ với OWASP**: Tất cả hướng dẫn bảo mật hiện ánh xạ rủi ro theo OWASP MCP Azure Security Guide

#### Tích hợp OWASP MCP Top 10
- **Mục mới**: Thêm bảng rủi ro bảo mật OWASP MCP Top 10 với các biện pháp Azure vào README bảo mật chính
- **Tài liệu dựa trên rủi ro**: Cập nhật mcp-security-controls-2025.md với tham chiếu rủi ro OWASP MCP cho từng lĩnh vực bảo mật
- **Kiến trúc tham khảo**: Liên kết đến kiến trúc tham khảo và mẫu triển khai OWASP MCP Azure Security Guide

#### Các tệp bảo mật cập nhật
- **README.md**: Thêm tổng quan Hội thảo Sherpa, bảng tuyến đường thám hiểm, tóm tắt rủi ro OWASP MCP Top 10 và phần đào tạo thực hành
- **mcp-security-controls-2025.md**: Cập nhật tiêu đề tháng 2 năm 2026, thêm tham chiếu rủi ro OWASP (MCP01-MCP08), sửa lỗi không nhất quán phiên bản đặc tả
- **mcp-security-best-practices-2025.md**: Thêm phần tài nguyên Sherpa và OWASP, cập nhật dấu thời gian
- **mcp-best-practices.md**: Thêm phần đào tạo thực hành với liên kết Sherpa và OWASP
- **azure-content-safety-implementation.md**: Thêm tham chiếu OWASP MCP06, đồng bộ trại 3 Sherpa, và phần tài nguyên bổ sung

#### Thêm liên kết tài nguyên mới
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Trang rủi ro OWASP MCP từng mục (MCP01-MCP10)

### Đồng bộ toàn giáo trình với MCP Specification 2025-11-25

#### Module 03 - Bắt đầu
- **Tài liệu SDK**: Thêm Go SDK vào danh sách SDK chính thức; cập nhật tất cả tham chiếu SDK phù hợp MCP Specification 2025-11-25
- **Làm rõ Transport**: Cập nhật mô tả transport STDIO và HTTP Streaming với tham chiếu đặc tả rõ ràng

#### Module 04 - Triển khai thực tế
- **Cập nhật SDK**: Thêm Go SDK; cập nhật danh sách SDK với tham chiếu phiên bản đặc tả
- **Đặc tả Ủy quyền**: Cập nhật liên kết đặc tả MCP Authorization lên phiên bản 2025-11-25 hiện tại

#### Module 05 - Chủ đề nâng cao
- **Tính năng mới**: Thêm ghi chú về các tính năng MCP Specification 2025-11-25 mới (Tasks, Chú thích Công cụ, Kích thích chế độ URL, Roots)
- **Tài nguyên bảo mật**: Thêm liên kết OWASP MCP Top 10 và hội thảo Sherpa vào phần tài liệu bổ sung

#### Module 06 - Đóng góp Cộng đồng
- **Danh sách SDK**: Thêm Swift và Rust SDK; cập nhật liên kết đặc tả lên 2025-11-25
- **Tham chiếu đặc tả**: Cập nhật liên kết MCP Specification lên URL đặc tả trực tiếp

#### Module 07 - Bài học từ Áp dụng sớm
- **Cập nhật Tài nguyên**: Thêm liên kết MCP Specification 2025-11-25 và OWASP MCP Top 10 vào tài nguyên bổ sung

#### Module 08 - Thực hành tốt nhất
- **Phiên bản đặc tả**: Cập nhật tham chiếu MCP Specification lên 2025-11-25
- **Tài nguyên bảo mật**: Thêm OWASP MCP Top 10 và hội thảo Sherpa vào tài liệu bổ sung

#### Module 10 - Tinh giản Quy trình AI
- **Cập nhật huy hiệu**: Thay đổi huy hiệu phiên bản MCP từ phiên bản SDK (1.9.3) sang phiên bản đặc tả (2025-11-25)
- **Liên kết tài nguyên**: Cập nhật liên kết MCP Specification; thêm OWASP MCP Top 10

#### Module 11 - Lab MCP Server Thực hành
- **Tham chiếu đặc tả**: Cập nhật liên kết MCP Specification lên phiên bản 2025-11-25
- **Tài nguyên bảo mật**: Thêm OWASP MCP Top 10 vào tài nguyên chính thức

## 18 tháng 12, 2025
### Cập Nhật Tài Liệu Bảo Mật - Đặc Tả MCP 2025-11-25

#### Thực Tiễn Bảo Mật MCP Tốt Nhất (02-Security/mcp-best-practices.md) - Cập Nhật Phiên Bản Đặc Tả
- **Cập Nhật Phiên Bản Giao Thức**: Cập nhật để tham chiếu Đặc Tả MCP mới nhất 2025-11-25 (phát hành ngày 25 tháng 11 năm 2025)
  - Cập nhật tất cả tham chiếu phiên bản đặc tả từ 2025-06-18 thành 2025-11-25
  - Cập nhật ngày tài liệu từ ngày 18 tháng 8 năm 2025 thành 18 tháng 12 năm 2025
  - Xác minh tất cả đường dẫn đặc tả trỏ đến tài liệu hiện hành
- **Kiểm Tra Nội Dung**: Kiểm tra toàn diện các thực tiễn bảo mật tốt nhất theo tiêu chuẩn mới nhất
  - **Giải Pháp Bảo Mật Microsoft**: Xác minh thuật ngữ và liên kết hiện tại cho Prompt Shields (trước đây gọi là "Phát hiện rủi ro Jailbreak"), Azure Content Safety, Microsoft Entra ID, và Azure Key Vault
  - **Bảo Mật OAuth 2.1**: Xác nhận phù hợp với các thực tiễn bảo mật OAuth mới nhất
  - **Tiêu Chuẩn OWASP**: Kiểm tra các tham chiếu Top 10 OWASP cho LLMs vẫn còn hiện hành
  - **Dịch Vụ Azure**: Xác minh tất cả các liên kết tài liệu Microsoft Azure và thực tiễn tốt nhất
- **Đồng Bộ Tiêu Chuẩn**: Tất cả tiêu chuẩn bảo mật được tham chiếu đều hiện hành
  - Khung Quản Lý Rủi Ro AI của NIST
  - ISO 27001:2022
  - Thực Tiễn Bảo Mật OAuth 2.1
  - Khung bảo mật và tuân thủ Azure
- **Tài Nguyên Triển Khai**: Xác minh tất cả liên kết hướng dẫn và tài nguyên triển khai
  - Các mẫu xác thực Azure API Management
  - Hướng dẫn tích hợp Microsoft Entra ID
  - Quản lý bí mật Azure Key Vault
  - Các pipeline DevSecOps và giải pháp giám sát

### Đảm Bảo Chất Lượng Tài Liệu
- **Tuân Thủ Đặc Tả**: Đảm bảo tất cả yêu cầu bảo mật MCP bắt buộc (MUST/MUST NOT) phù hợp với phiên bản đặc tả mới nhất
- **Tính Cập Nhật Tài Nguyên**: Xác minh tất cả liên kết bên ngoài tới tài liệu Microsoft, tiêu chuẩn bảo mật và hướng dẫn triển khai
- **Phủ Sóng Thực Tiễn Tốt Nhất**: Xác nhận sự bao phủ toàn diện về xác thực, ủy quyền, mối đe dọa AI cụ thể, bảo mật chuỗi cung ứng và mẫu doanh nghiệp

## Ngày 6 Tháng 10, 2025

### Mở Rộng Phần Bắt Đầu – Sử Dụng Máy Chủ Nâng Cao & Xác Thực Đơn Giản

#### Sử Dụng Máy Chủ Nâng Cao (03-GettingStarted/10-advanced)
- **Thêm Chương Mới**: Giới thiệu hướng dẫn toàn diện về sử dụng máy chủ MCP nâng cao, bao gồm cả kiến trúc máy chủ thường và cấp thấp.
  - **So Sánh Máy Chủ Thường và Máy Chủ Cấp Thấp**: So sánh chi tiết và ví dụ mã Python và TypeScript cho cả hai cách tiếp cận.
  - **Thiết Kế Dựa Trên Handler**: Giải thích quản lý công cụ/tài nguyên/prompt dựa trên handler cho triển khai máy chủ linh hoạt và mở rộng.
  - **Mẫu Thực Tiễn**: Các tình huống thực tế cho thấy mẫu máy chủ cấp thấp có lợi ích với tính năng và kiến trúc nâng cao.

#### Xác Thực Đơn Giản (03-GettingStarted/11-simple-auth)
- **Thêm Chương Mới**: Hướng dẫn từng bước triển khai xác thực đơn giản trong các máy chủ MCP.
  - **Khái Niệm Xác Thực**: Giải thích rõ ràng về xác thực và ủy quyền, cùng cách xử lý thông tin đăng nhập.
  - **Triển Khai Xác Thực Cơ Bản**: Mẫu xác thực dựa trên middleware trong Python (Starlette) và TypeScript (Express), kèm ví dụ mã.
  - **Tiến Đến Bảo Mật Nâng Cao**: Hướng dẫn bắt đầu với xác thực đơn giản và tiến tới OAuth 2.1 và RBAC, kèm tham chiếu tới các module bảo mật nâng cao.

Các bổ sung này cung cấp hướng dẫn thực tiễn, thao tác để xây dựng các triển khai máy chủ MCP mạnh mẽ, an toàn và linh hoạt, kết nối các khái niệm cơ bản với mẫu triển khai sản xuất nâng cao.

## Ngày 29 Tháng 9, 2025

### MCP Server Database Integration Labs - Lộ Trình Học Tập Thực Hành Toàn Diện

#### 11-MCPServerHandsOnLabs - Chương Trình Học Kết Nối Cơ Sở Dữ Liệu Đầy Đủ
- **Lộ Trình Học 13 Lab Toàn Diện**: Thêm chương trình học thực hành toàn diện để xây dựng máy chủ MCP sẵn sàng sản xuất với tích hợp cơ sở dữ liệu PostgreSQL
  - **Triển Khai Thực Tế**: Trường hợp sử dụng phân tích Zava Retail minh họa mẫu chuẩn doanh nghiệp
  - **Lộ Trình Học Có Cấu Trúc**:
    - **Lab 00-03: Nền Tảng** - Giới thiệu, Kiến trúc cốt lõi, Bảo mật & đa người dùng, Cài đặt môi trường
    - **Lab 04-06: Xây Dựng Máy Chủ MCP** - Thiết kế & lược đồ cơ sở dữ liệu, Triển khai máy chủ MCP, Phát triển công cụ
    - **Lab 07-09: Tính Năng Nâng Cao** - Tích hợp tìm kiếm ngữ nghĩa, Kiểm thử & gỡ lỗi, Tích hợp VS Code
    - **Lab 10-12: Sản Xuất & Thực Tiễn Tốt Nhất** - Chiến lược triển khai, Giám sát & quan sát, Thực tiễn tốt nhất & tối ưu hóa
  - **Công Nghệ Doanh Nghiệp**: Framework FastMCP, PostgreSQL với pgvector, nhúng Azure OpenAI, Azure Container Apps, Application Insights
  - **Tính Năng Nâng Cao**: Bảo mật cấp hàng (Row Level Security - RLS), tìm kiếm ngữ nghĩa, truy cập dữ liệu đa người thuê, vector embeddings, giám sát thời gian thực

#### Chuẩn Hóa Thuật Ngữ - Chuyển Đổi Module Thành Lab
- **Cập Nhật Tài Liệu Toàn Diện**: Cập nhật có hệ thống tất cả các tệp README trong 11-MCPServerHandsOnLabs sử dụng thuật ngữ "Lab" thay vì "Module"
  - **Tiêu Đề Phần**: Cập nhật "Phần này trình bày" thành "Lab này trình bày" trên toàn bộ 13 lab
  - **Mô Tả Nội Dung**: Thay "Module này cung cấp..." thành "Lab này cung cấp..."
  - **Mục Tiêu Học Tập**: Cập nhật "Kết thúc module này..." thành "Kết thúc lab này..."
  - **Liên Kết Điều Hướng**: Chuyển đổi tất cả tham chiếu "Module XX:" thành "Lab XX:" trong cross-reference và điều hướng
  - **Theo Dõi Hoàn Thành**: Cập nhật "Sau khi hoàn thành module này..." thành "Sau khi hoàn thành lab này..."
  - **Giữ Nguyên Tham Chiếu Kỹ Thuật**: Giữ tham chiếu module Python trong file cấu hình (ví dụ `"module": "mcp_server.main"`)

#### Nâng Cao Hướng Dẫn Học Tập (study_guide.md)
- **Bản Đồ Chương Trình Trực Quan**: Thêm phần mới "11. Database Integration Labs" với cấu trúc lab đầy đủ
- **Cấu Trúc Kho Lưu Trữ**: Cập nhật từ mười thành mười một phần chính với mô tả chi tiết về 11-MCPServerHandsOnLabs
- **Hướng Dẫn Lộ Trình Học**: Nâng cao hướng dẫn điều hướng để phủ toàn bộ phần 00-11
- **Phủ Sóng Công Nghệ**: Thêm chi tiết tích hợp FastMCP, PostgreSQL và dịch vụ Azure
- **Kết Quả Học Tập**: Nhấn mạnh phát triển máy chủ sẵn sàng sản xuất, mẫu tích hợp cơ sở dữ liệu và bảo mật doanh nghiệp

#### Nâng Cao Cấu Trúc README Chính
- **Thuật Ngữ Dựa Trên Lab**: Cập nhật README.md chính trong 11-MCPServerHandsOnLabs sử dụng nhất quán cấu trúc "Lab"
- **Tổ Chức Lộ Trình Học**: Tiến trình rõ ràng từ khái niệm nền tảng tới triển khai nâng cao và sản xuất
- **Tập Trung Thực Tế**: Nhấn mạnh học tập thực hành với mẫu chuẩn doanh nghiệp và công nghệ

### Cải Tiến Chất Lượng & Tính Nhất Quán Tài Liệu
- **Nhấn Mạnh Học Tập Thực Hành**: Gia cố phương pháp học tập dựa trên lab trong toàn bộ tài liệu
- **Tập Trung Mẫu Doanh Nghiệp**: Nêu bật các triển khai sẵn sàng sản xuất và xem xét bảo mật doanh nghiệp
- **Tích Hợp Công Nghệ**: Bao phủ toàn diện dịch vụ Azure hiện đại và mẫu tích hợp AI
- **Lộ Trình Học**: Lộ trình rõ ràng, có cấu trúc từ khái niệm cơ bản tới triển khai sản xuất

## Ngày 26 Tháng 9, 2025

### Nâng Cấp Case Studies - Tích Hợp GitHub MCP Registry

#### Case Studies (09-CaseStudy/) - Tập Trung Phát Triển Hệ Sinh Thái
- **README.md**: Mở rộng lớn với Case Study toàn diện về GitHub MCP Registry
  - **Case Study GitHub MCP Registry**: Case study toàn diện mới đánh giá việc ra mắt MCP Registry của GitHub vào tháng 9 năm 2025
    - **Phân Tích Vấn Đề**: Xem xét chi tiết các khó khăn trong phát hiện và triển khai MCP server phân tán
    - **Kiến Trúc Giải Pháp**: Cách tiếp cận registry tập trung với cài đặt VS Code chỉ một cú nhấp
    - **Ảnh Hưởng Kinh Doanh**: Cải thiện rõ ràng trong tiếp nhận và hiệu suất phát triển
    - **Giá Trị Chiến Lược**: Tập trung triển khai tác nhân mô-đun và khả năng liên vận công cụ chéo
    - **Phát Triển Hệ Sinh Thái**: Định vị như nền tảng cơ bản cho tích hợp hệ thống tác nhân
  - **Cải Tiến Cấu Trúc Case Study**: Cập nhật bảy case study với định dạng nhất quán và mô tả toàn diện
    - Đại lý AI du lịch Azure: Tập trung phối hợp đa đại lý
    - Tích hợp Azure DevOps: Tự động hóa quy trình làm việc
    - Truy xuất tài liệu thời gian thực: Triển khai client console Python
    - Bộ tạo kế hoạch học tương tác: Ứng dụng web đàm thoại Chainlit
    - Tài liệu trong trình soạn thảo: Tích hợp VS Code và GitHub Copilot
    - Quản lý API Azure: Mẫu tích hợp API doanh nghiệp
    - GitHub MCP Registry: Phát triển hệ sinh thái và nền tảng cộng đồng
  - **Kết Luận Toàn Diện**: Viết lại phần kết luận nhấn mạnh bảy case study bao phủ nhiều chiều triển khai MCP
    - Tích hợp doanh nghiệp, phối hợp đa đại lý, năng suất phát triển
    - Phát triển hệ sinh thái, phân loại ứng dụng giáo dục
    - Góc nhìn sâu sắc mẫu kiến trúc, chiến lược triển khai và thực tiễn tốt nhất
    - Nhấn mạnh MCP là giao thức trưởng thành, sẵn sàng sản xuất

#### Cập Nhật Hướng Dẫn Học (study_guide.md)
- **Bản Đồ Chương Trình Trực Quan**: Cập nhật mindmap để bao gồm GitHub MCP Registry trong phần Case Studies
- **Mô Tả Case Studies**: Nâng cấp từ mô tả chung thành phân tách chi tiết bảy case study toàn diện
- **Cấu Trúc Kho Lưu Trữ**: Cập nhật phần 10 để phản ánh bao phủ case study toàn diện với chi tiết triển khai cụ thể
- **Tích Hợp Changelog**: Thêm mục ngày 26 tháng 9 năm 2025 ghi nhận bổ sung GitHub MCP Registry và cải tiến case study
- **Cập Nhật Ngày**: Cập nhật dấu thời gian footer phản ánh bản sửa đổi mới nhất (26 tháng 9 năm 2025)

### Cải Thiện Chất Lượng Tài Liệu
- **Nâng Cao Tính Nhất Quán**: Chuẩn hóa định dạng và cấu trúc case study trên bảy ví dụ
- **Phủ Sóng Toàn Diện**: Case study bao phủ các kịch bản doanh nghiệp, năng suất phát triển và phát triển hệ sinh thái
- **Định Vị Chiến Lược**: Nhấn mạnh vai trò MCP là nền tảng cơ bản cho triển khai hệ thống tác nhân
- **Tích Hợp Tài Nguyên**: Cập nhật tài nguyên bổ sung để bao gồm liên kết GitHub MCP Registry

## Ngày 15 Tháng 9, 2025

### Mở Rộng Chủ Đề Nâng Cao - Custom Transports & Kỹ Thuật Context

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Hướng Dẫn Triển Khai Nâng Cao Mới
- **README.md**: Hướng dẫn triển khai đầy đủ cho các cơ chế truyền tải MCP tùy chỉnh
  - **Azure Event Grid Transport**: Triển khai truyền tải dựa trên sự kiện serverless toàn diện
    - Ví dụ C#, TypeScript và Python tích hợp Azure Functions
    - Mẫu kiến trúc hướng sự kiện cho giải pháp MCP quy mô
    - Bộ nhận webhook và xử lý tin nhắn đẩy
  - **Azure Event Hubs Transport**: Triển khai truyền tải streaming hiệu suất cao
    - Khả năng streaming thời gian thực cho các kịch bản độ trễ thấp
    - Chiến lược phân vùng và quản lý điểm kiểm tra
    - Gộp tin nhắn và tối ưu hiệu suất
  - **Mẫu Tích Hợp Doanh Nghiệp**: Ví dụ kiến trúc sẵn sàng sản xuất
    - Xử lý MCP phân tán qua nhiều Azure Functions
    - Kiến trúc truyền tải lai kết hợp nhiều loại truyền tải
    - Chiến lược độ bền, độ tin cậy và xử lý lỗi tin nhắn
  - **Bảo Mật & Giám Sát**: Tích hợp Azure Key Vault và mẫu quan sát
    - Xác thực managed identity và truy cập theo quyền tối thiểu
    - Telemetry Application Insights và giám sát hiệu suất
    - Circuit breakers và mẫu chịu lỗi
  - **Khung Kiểm Thử**: Chiến lược kiểm thử toàn diện cho truyền tải tùy chỉnh
    - Kiểm thử đơn vị với test doubles và mocking
    - Kiểm thử tích hợp với Azure Test Containers
    - Xem xét kiểm thử hiệu suất và tải

#### Kỹ Thuật Context (05-AdvancedTopics/mcp-contextengineering/) - Lĩnh Vực AI Mới Nổi
- **README.md**: Khám phá toàn diện kỹ thuật context là lĩnh vực emergent
  - **Nguyên Tắc Cốt Lõi**: Chia sẻ context đầy đủ, nhận thức quyết định hành động, quản lý cửa sổ context
  - **Phù Hợp Với MCP Protocol**: Cách thiết kế MCP xử lý thách thức kỹ thuật context
    - Giới hạn cửa sổ context và chiến lược tải dần
    - Xác định mức độ liên quan và truy xuất context động
    - Xử lý đa phương thức context và xem xét bảo mật
  - **Cách Tiếp Cận Triển Khai**: Kiến trúc đơn luồng và đa đại lý
    - Kỹ thuật chia nhỏ chunk context và ưu tiên
    - Tải dần và nén context
    - Cách tiếp cận phân lớp context và tối ưu truy xuất
  - **Khung Đo Lường**: Các chỉ số mới để đánh giá hiệu quả context
    - Hiệu quả đầu vào, hiệu năng, chất lượng và trải nghiệm người dùng
    - Phương pháp thử nghiệm tối ưu context
    - Phân tích lỗi và phương pháp cải tiến

#### Cập Nhật Điều Hướng Chương Trình Học (README.md)
- **Nâng Cao Cấu Trúc Module**: Cập nhật bảng chương trình bao gồm chủ đề nâng cao mới
  - Thêm mục Context Engineering (5.14) và Custom Transport (5.15)
  - Định dạng nhất quán và liên kết điều hướng trên tất cả các module
  - Cập nhật mô tả phù hợp phạm vi nội dung hiện tại

### Cải Tiến Cấu Trúc Thư Mục
- **Chuẩn Hóa Tên**: Đổi tên "mcp transport" thành "mcp-transport" để nhất quán với các thư mục chủ đề nâng cao khác
- **Tổ Chức Nội Dung**: Tất cả thư mục 05-AdvancedTopics hiện theo mẫu đặt tên thống nhất (mcp-[topic])

### Nâng Cao Chất Lượng Tài Liệu
- **Phù Hợp Đặc Tả MCP**: Tất cả nội dung mới tham chiếu Đặc Tả MCP hiện hành 2025-06-18
- **Ví Dụ Đa Ngôn Ngữ**: Ví dụ mã đầy đủ bằng C#, TypeScript, và Python
- **Tập Trung Doanh Nghiệp**: Mẫu sẵn sàng sản xuất và tích hợp đám mây Azure xuyên suốt
- **Tài Liệu Trực Quan**: Biểu đồ Mermaid minh họa kiến trúc và luồng xử lý

## Ngày 18 Tháng 8, 2025

### Cập Nhật Toàn Diện Tài Liệu - Tiêu Chuẩn MCP 2025-06-18

#### Thực Tiễn Bảo Mật MCP (02-Security/) - Hiện Đại Hóa Toàn Bộ
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Viết lại hoàn toàn phù hợp với Đặc tả MCP 2025-06-18  
  - **Yêu cầu Bắt buộc**: Thêm các yêu cầu PHẢI/PHẢI KHÔNG rõ ràng từ đặc tả chính thức với chỉ báo trực quan rõ nét  
  - **12 Thực hành Bảo mật Cốt lõi**: Cấu trúc lại từ danh sách 15 mục thành các miền bảo mật tổng thể  
    - Bảo mật Token & Xác thực với tích hợp nhà cung cấp danh tính bên ngoài  
    - Quản lý Phiên & Bảo mật Vận chuyển với các yêu cầu mật mã  
    - Bảo vệ Đe dọa Đặc thù AI với tích hợp Microsoft Prompt Shields  
    - Kiểm soát Truy cập & Quyền hạn với nguyên tắc quyền ít nhất  
    - An toàn Nội dung & Giám sát với tích hợp Azure Content Safety  
    - Bảo mật Chuỗi Cung ứng với xác minh thành phần toàn diện  
    - Bảo mật OAuth & Ngăn ngừa Confused Deputy với triển khai PKCE  
    - Ứng phó Sự cố & Phục hồi với khả năng tự động hóa  
    - Tuân thủ & Quản trị với sự phù hợp quy định  
    - Điều khiển Bảo mật Nâng cao với kiến trúc zero trust  
    - Tích hợp Hệ sinh thái Bảo mật Microsoft với các giải pháp toàn diện  
    - Tiến hóa Bảo mật Liên tục với các thực hành thích ứng  
  - **Giải pháp Bảo mật Microsoft**: Hướng dẫn tích hợp nâng cao cho Prompt Shields, Azure Content Safety, Entra ID và GitHub Advanced Security  
  - **Tài nguyên Triển khai**: Phân loại các liên kết tài nguyên toàn diện theo Tài liệu MCP chính thức, Giải pháp Bảo mật Microsoft, Tiêu chuẩn Bảo mật và Hướng dẫn Triển khai  

#### Điều khiển Bảo mật Nâng cao (02-Security/) - Triển khai Doanh nghiệp  
- **MCP-SECURITY-CONTROLS-2025.md**: Cải tổ hoàn toàn với khung bảo mật cấp doanh nghiệp  
  - **9 Miền Bảo mật Toàn diện**: Mở rộng từ điều khiển cơ bản thành khung doanh nghiệp chi tiết  
    - Xác thực & Phân quyền Nâng cao với tích hợp Microsoft Entra ID  
    - Bảo mật Token & Điều khiển Chống Truyền qua với xác thực toàn diện  
    - Điều khiển Bảo mật Phiên với phòng chống chiếm đoạt  
    - Điều khiển Bảo mật Đặc thù AI với ngăn chặn tiêm nhúng prompt và đầu độc công cụ  
    - Ngăn chặn Tấn công Confused Deputy với bảo mật proxy OAuth  
    - Bảo mật Thực thi Công cụ với sandboxing và cô lập  
    - Điều khiển Bảo mật Chuỗi Cung ứng với xác minh phụ thuộc  
    - Điều khiển Giám sát & Phát hiện với tích hợp SIEM  
    - Ứng phó Sự cố & Phục hồi với khả năng tự động hóa  
  - **Ví dụ Triển khai**: Thêm các khối cấu hình YAML chi tiết và ví dụ mã  
  - **Tích hợp Giải pháp Microsoft**: Bao phủ toàn diện các dịch vụ bảo mật Azure, GitHub Advanced Security và quản lý danh tính doanh nghiệp  

#### An ninh Chủ đề Nâng cao (05-AdvancedTopics/mcp-security/) - Triển khai Sẵn sàng Sản xuất  
- **README.md**: Viết lại hoàn toàn cho triển khai bảo mật doanh nghiệp  
  - **Phù hợp Đặc tả Hiện tại**: Cập nhật theo Đặc tả MCP 2025-06-18 với yêu cầu bảo mật bắt buộc  
  - **Xác thực Nâng cao**: Tích hợp Microsoft Entra ID với ví dụ toàn diện .NET và Java Spring Security  
  - **Tích hợp Bảo mật AI**: Thực thi Microsoft Prompt Shields và Azure Content Safety với ví dụ Python chi tiết  
  - **Giảm thiểu Mối đe dọa Nâng cao**: Ví dụ triển khai toàn diện cho  
    - Ngăn chặn Tấn công Confused Deputy với PKCE và xác thực sự đồng ý của người dùng  
    - Ngăn chặn Truyền Token với xác thực audience và quản lý token an toàn  
    - Ngăn chặn Chiếm đoạt Phiên với ràng buộc mật mã và phân tích hành vi  
  - **Tích hợp Bảo mật Doanh nghiệp**: Giám sát Azure Application Insights, các pipeline phát hiện mối đe dọa và bảo mật chuỗi cung ứng  
  - **Checklist Triển khai**: Phân biệt rõ ràng điều khiển bảo mật bắt buộc và đề xuất với lợi ích hệ sinh thái bảo mật Microsoft  

### Chất lượng Tài liệu & Phù hợp Tiêu chuẩn  
- **Tham chiếu Đặc tả**: Cập nhật tất cả tham chiếu theo Đặc tả MCP 2025-06-18 hiện hành  
- **Hệ sinh thái Bảo mật Microsoft**: Tăng cường hướng dẫn tích hợp xuyên suốt tài liệu bảo mật  
- **Triển khai Thực tế**: Thêm ví dụ mã chi tiết trong .NET, Java và Python với các mẫu doanh nghiệp  
- **Tổ chức Tài nguyên**: Phân loại toàn diện tài liệu chính thức, tiêu chuẩn bảo mật, và hướng dẫn triển khai  
- **Chỉ báo Trực quan**: Đánh dấu rõ ràng yêu cầu bắt buộc so với thực hành được khuyến nghị  

#### Khái niệm Cốt lõi (01-CoreConcepts/) - Hiện đại hóa Toàn diện  
- **Cập nhật Phiên bản Giao thức**: Tham chiếu theo Đặc tả MCP 2025-06-18 với định dạng phiên bản theo ngày (YYYY-MM-DD)  
- **Tinh chỉnh Kiến trúc**: Mô tả chi tiết hơn về Hosts, Clients và Servers phản ánh mẫu kiến trúc MCP hiện tại  
  - Hosts định nghĩa rõ là ứng dụng AI điều phối nhiều kết nối client MCP  
  - Clients mô tả là kết nối giao thức giữ quan hệ một-một với server  
  - Servers bổ sung các kịch bản triển khai cục bộ và từ xa  
- **Tái cấu trúc Nguyên thủy**: Cải tổ hoàn toàn nguyên thủy server và client  
  - Nguyên thủy Server: Resources (nguồn dữ liệu), Prompts (mẫu), Tools (hàm thực thi) với giải thích và ví dụ chi tiết  
  - Nguyên thủy Client: Sampling (hoàn thành LLM), Elicitation (đầu vào người dùng), Logging (gỡ lỗi/giám sát)  
  - Cập nhật theo mẫu phương thức hiện tại cho discovery (`*/list`), retrieval (`*/get`), và execution (`*/call`)  
- **Kiến trúc Giao thức**: Giới thiệu mô hình hai lớp kiến trúc  
  - Lớp Dữ liệu: Nền tảng JSON-RPC 2.0 với quản lý vòng đời và nguyên thủy  
  - Lớp Vận chuyển: STDIO (cục bộ) và HTTP có thể stream kèm SSE (vận chuyển từ xa)  
- **Khung Bảo mật**: Nguyên tắc bảo mật toàn diện bao gồm đồng ý người dùng rõ ràng, bảo vệ dữ liệu riêng tư, an toàn thực thi công cụ, và bảo mật lớp vận chuyển  
- **Mẫu Giao tiếp**: Cập nhật các tin nhắn giao thức thể hiện luồng khởi tạo, khám phá, thực thi và thông báo  
- **Ví dụ Mã**: Làm mới ví dụ đa ngôn ngữ (.NET, Java, Python, JavaScript) phản ánh mẫu SDK MCP hiện tại  

#### Bảo mật (02-Security/) - Cải tổ Toàn diện Bảo mật  
- **Phù hợp Tiêu chuẩn**: Đầy đủ theo các yêu cầu bảo mật Đặc tả MCP 2025-06-18  
- **Tiến hóa Xác thực**: Ghi lại sự tiến hóa từ server OAuth tùy chỉnh sang ủy quyền nhà cung cấp danh tính bên ngoài (Microsoft Entra ID)  
- **Phân tích Đe dọa AI Đặc thù**: Mở rộng bao phủ các vectơ tấn công AI hiện đại  
  - Kịch bản tấn công tiêm nhúng prompt chi tiết với ví dụ thực tế  
  - Cơ chế đầu độc công cụ và mẫu tấn công "kéo tấm thảm rug pull"  
  - Đầu độc cửa sổ ngữ cảnh và tấn công làm nhầm lẫn mô hình  
- **Giải pháp Bảo mật AI Microsoft**: Toàn diện hệ sinh thái bảo mật Microsoft  
  - AI Prompt Shields với phát hiện nâng cao, chiếu sáng và kỹ thuật phân cách  
  - Mẫu tích hợp Azure Content Safety  
  - GitHub Advanced Security cho bảo vệ chuỗi cung ứng  
- **Giảm thiểu Mối đe dọa Nâng cao**: Điều khiển bảo mật chi tiết cho  
  - Hiểm họa chiếm đoạt phiên với kịch bản tấn công MCP và yêu cầu session ID mật mã  
  - Vấn đề confused deputy trong kịch bản proxy MCP với yêu cầu đồng ý rõ ràng  
  - Lỗ hổng truyền token với điều khiển xác thực bắt buộc  
- **Bảo mật Chuỗi Cung ứng**: Mở rộng bảo mật chuỗi cung ứng AI gồm mô hình nền tảng, dịch vụ nhúng, nhà cung cấp ngữ cảnh, và API bên thứ ba  
- **Bảo mật Nền tảng**: Tăng cường tích hợp với mô hình bảo mật doanh nghiệp bao gồm kiến trúc zero trust và hệ sinh thái bảo mật Microsoft  
- **Tổ chức Tài nguyên**: Phân loại các liên kết tài nguyên toàn diện theo loại (Tài liệu Chính thức, Tiêu chuẩn, Nghiên cứu, Giải pháp Microsoft, Hướng dẫn Triển khai)  

### Cải tiến Chất lượng Tài liệu  
- **Mục tiêu Học tập Cấu trúc**: Tăng cường mục tiêu học tập cụ thể, có thể hành động  
- **Tham chiếu Chéo**: Thêm liên kết giữa các chủ đề bảo mật và khái niệm cốt lõi liên quan  
- **Thông tin Hiện hành**: Cập nhật tất cả tham chiếu ngày tháng và liên kết đặc tả theo tiêu chuẩn mới nhất  
- **Hướng dẫn Triển khai**: Thêm hướng dẫn triển khai cụ thể, có thể áp dụng xuyên suốt hai phần  

## 16 tháng 7, 2025

### Cải tiến README và Điều hướng  
- Thiết kế lại hoàn toàn điều hướng chương trình học trong README.md  
- Thay thế thẻ `<details>` bằng định dạng bảng dễ truy cập hơn  
- Tạo các tùy chọn bố cục thay thế trong thư mục "alternative_layouts" mới  
- Thêm ví dụ điều hướng dạng thẻ, tab và accordion  
- Cập nhật phần cấu trúc kho lưu trữ để bao gồm tất cả tệp mới nhất  
- Nâng cao phần "Cách Sử dụng Chương trình học" với khuyến nghị rõ ràng  
- Cập nhật liên kết đặc tả MCP đến các URL chính xác  
- Thêm phần Kỹ thuật Ngữ cảnh (5.14) vào cấu trúc chương trình học  

### Cập nhật Hướng dẫn Học tập  
- Viết lại hoàn toàn hướng dẫn học tập cho phù hợp cấu trúc kho lưu trữ hiện tại  
- Thêm các phần mới cho MCP Clients và Tools, cùng MCP Servers phổ biến  
- Cập nhật Bản đồ Chương trình Học Trực quan phản ánh chính xác tất cả chủ đề  
- Nâng cao mô tả về Chủ đề Nâng cao để bao phủ đầy đủ các lĩnh vực chuyên biệt  
- Cập nhật phần Nghiên cứu trường hợp với ví dụ thực tế  
- Thêm nhật ký thay đổi toàn diện này  

### Đóng góp Cộng đồng (06-CommunityContributions/)  
- Thêm thông tin chi tiết về MCP servers tạo hình ảnh  
- Thêm phần toàn diện về sử dụng Claude trong VSCode  
- Thêm hướng dẫn cấu hình và sử dụng client terminal Cline  
- Cập nhật phần MCP client để bao gồm tất cả lựa chọn client phổ biến  
- Tăng cường ví dụ đóng góp với mẫu mã chính xác hơn  

### Chủ đề Nâng cao (05-AdvancedTopics/)  
- Tổ chức tất cả thư mục chủ đề chuyên biệt với tên gọi nhất quán  
- Thêm tài liệu và ví dụ kỹ thuật ngữ cảnh  
- Thêm tài liệu tích hợp agent Foundry  
- Nâng cao tài liệu tích hợp bảo mật Entra ID  

## 11 tháng 6, 2025

### Tạo Ban đầu  
- Phát hành phiên bản đầu tiên của chương trình MCP cho Người mới bắt đầu  
- Tạo cấu trúc cơ bản cho tất cả 10 phần chính  
- Triển khai Bản đồ chương trình học trực quan để điều hướng  
- Thêm các dự án mẫu ban đầu bằng nhiều ngôn ngữ lập trình  

### Bắt đầu (03-GettingStarted/)  
- Tạo ví dụ triển khai server đầu tiên  
- Thêm hướng dẫn phát triển client  
- Bao gồm hướng dẫn tích hợp client LLM  
- Thêm tài liệu tích hợp VS Code  
- Triển khai ví dụ Server-Sent Events (SSE) server  

### Khái niệm Cốt lõi (01-CoreConcepts/)  
- Thêm giải thích chi tiết kiến trúc client-server  
- Tạo tài liệu về thành phần chủ đạo giao thức  
- Tài liệu hóa mẫu tin nhắn trong MCP  

## 23 tháng 5, 2025

### Cấu trúc Kho lưu trữ  
- Khởi tạo kho lưu trữ với cấu trúc thư mục cơ bản  
- Tạo các file README cho từng phần chính  
- Thiết lập cơ sở hạ tầng dịch thuật  
- Thêm tài sản hình ảnh và sơ đồ  

### Tài liệu  
- Tạo README.md ban đầu với tổng quan chương trình học  
- Thêm CODE_OF_CONDUCT.md và SECURITY.md  
- Thiết lập SUPPORT.md với hướng dẫn nhận trợ giúp  
- Tạo cấu trúc hướng dẫn học tập sơ bộ  

## 15 tháng 4, 2025

### Lập kế hoạch và Khung  
- Lập kế hoạch ban đầu cho chương trình MCP cho Người mới bắt đầu  
- Định nghĩa mục tiêu học tập và đối tượng mục tiêu  
- Phác thảo cấu trúc 10 phần của chương trình học  
- Phát triển khung khái niệm cho ví dụ và nghiên cứu trường hợp  
- Tạo các mẫu ví dụ đầu tiên cho các khái niệm chính

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa của nó nên được coi là nguồn tham khảo chính xác nhất. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->