# 🚀 Máy chủ MCP với PostgreSQL - Hướng dẫn học tập hoàn chỉnh

## 🧠 Tổng quan về Lộ trình học Tích hợp Cơ sở dữ liệu MCP

Hướng dẫn học tập toàn diện này sẽ chỉ bạn cách xây dựng các **máy chủ Model Context Protocol (MCP)** sẵn sàng cho môi trường sản xuất tích hợp với cơ sở dữ liệu thông qua một ứng dụng phân tích bán lẻ thực tế. Bạn sẽ học các mẫu thiết kế cấp doanh nghiệp bao gồm **Bảo mật cấp dòng (RLS)**, **tìm kiếm ngữ nghĩa**, **tích hợp Azure AI**, và **truy cập dữ liệu đa người thuê**.

Cho dù bạn là nhà phát triển backend, kỹ sư AI hay kiến trúc sư dữ liệu, hướng dẫn này cung cấp lộ trình học có cấu trúc với các ví dụ thực tế và bài tập thực hành giúp bạn đi qua máy chủ MCP https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Tài nguyên chính thức của MCP

- 📘 [Tài liệu MCP](https://modelcontextprotocol.io/) – Hướng dẫn chi tiết và tài liệu người dùng
- 📜 [Đặc tả MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Kiến trúc giao thức và tham chiếu kỹ thuật
- 🧑‍💻 [Kho lưu trữ MCP trên GitHub](https://github.com/modelcontextprotocol) – SDK mã nguồn mở, công cụ và ví dụ mã
- 🌐 [Cộng đồng MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Tham gia thảo luận và đóng góp cho cộng đồng
- 🔒 [10 Lỗi MCP Hàng đầu OWASP](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Thực hành an ninh tốt nhất và giảm thiểu rủi ro


## 🧭 Lộ trình học Tích hợp Cơ sở dữ liệu MCP

### 📚 Cấu trúc học tập hoàn chỉnh cho https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Phòng thí nghiệm | Chủ đề | Mô tả | Liên kết |
|--------|-------|-------------|------|
| **Phòng thí nghiệm 1-3: Nền tảng** | | | |
| 00 | [Giới thiệu về Tích hợp Cơ sở dữ liệu MCP](./00-Introduction/README.md) | Tổng quan về MCP kết hợp cơ sở dữ liệu và trường hợp phân tích bán lẻ | [Bắt đầu tại đây](./00-Introduction/README.md) |
| 01 | [Khái niệm Kiến trúc Cốt lõi](./01-Architecture/README.md) | Hiểu kiến trúc máy chủ MCP, các lớp cơ sở dữ liệu và mẫu bảo mật | [Học](./01-Architecture/README.md) |
| 02 | [Bảo mật và Đa người thuê](./02-Security/README.md) | Bảo mật cấp dòng, xác thực, và truy cập dữ liệu đa người thuê | [Học](./02-Security/README.md) |
| 03 | [Thiết lập Môi trường](./03-Setup/README.md) | Cài đặt môi trường phát triển, Docker, tài nguyên Azure | [Thiết lập](./03-Setup/README.md) |
| **Phòng thí nghiệm 4-6: Xây dựng Máy chủ MCP** | | | |
| 04 | [Thiết kế Cơ sở dữ liệu và Lược đồ](./04-Database/README.md) | Cài đặt PostgreSQL, thiết kế lược đồ bán lẻ, và dữ liệu mẫu | [Xây dựng](./04-Database/README.md) |
| 05 | [Triển khai Máy chủ MCP](./05-MCP-Server/README.md) | Xây dựng máy chủ FastMCP với tích hợp cơ sở dữ liệu | [Xây dựng](./05-MCP-Server/README.md) |
| 06 | [Phát triển Công cụ](./06-Tools/README.md) | Tạo công cụ truy vấn cơ sở dữ liệu và khảo sát lược đồ | [Xây dựng](./06-Tools/README.md) |
| **Phòng thí nghiệm 7-9: Tính năng Nâng cao** | | | |
| 07 | [Tích hợp Tìm kiếm Ngữ nghĩa](./07-Semantic-Search/README.md) | Triển khai vector embeddings với Azure OpenAI và pgvector | [Nâng cao](./07-Semantic-Search/README.md) |
| 08 | [Kiểm thử và Gỡ lỗi](./08-Testing/README.md) | Chiến lược kiểm thử, công cụ gỡ lỗi và phương pháp xác thực | [Kiểm thử](./08-Testing/README.md) |
| 09 | [Tích hợp VS Code](./09-VS-Code/README.md) | Cấu hình tích hợp MCP trên VS Code và sử dụng AI Chat | [Tích hợp](./09-VS-Code/README.md) |
| **Phòng thí nghiệm 10-12: Sản xuất và Thực hành tốt nhất** | | | |
| 10 | [Chiến lược Triển khai](./10-Deployment/README.md) | Triển khai Docker, Azure Container Apps, và các cân nhắc mở rộng | [Triển khai](./10-Deployment/README.md) |
| 11 | [Giám sát và Quan sát](./11-Monitoring/README.md) | Application Insights, ghi log, giám sát hiệu suất | [Giám sát](./11-Monitoring/README.md) |
| 12 | [Thực hành Tốt nhất và Tối ưu hóa](./12-Best-Practices/README.md) | Tối ưu hiệu suất, gia cố bảo mật, và mẹo sản xuất | [Tối ưu](./12-Best-Practices/README.md) |

### 💻 Những gì bạn sẽ xây dựng

Vào cuối lộ trình học này, bạn sẽ xây dựng được một **Máy chủ MCP Phân tích Bán lẻ Zava** hoàn chỉnh với các tính năng:

- **Cơ sở dữ liệu bán lẻ đa bảng** với các đơn hàng khách hàng, sản phẩm và tồn kho
- **Bảo mật cấp dòng** để tách biệt dữ liệu theo cửa hàng
- **Tìm kiếm sản phẩm ngữ nghĩa** sử dụng vector embeddings của Azure OpenAI
- **Tích hợp AI Chat trên VS Code** cho truy vấn ngôn ngữ tự nhiên
- **Triển khai sẵn sàng cho sản xuất** với Docker và Azure
- **Giám sát toàn diện** bằng Application Insights

## 🎯 Yêu cầu tiên quyết để học

Để tận dụng tốt nhất lộ trình học này, bạn nên có:

- **Kinh nghiệm lập trình**: Quen thuộc với Python (ưu tiên) hoặc các ngôn ngữ tương tự
- **Kiến thức cơ sở dữ liệu**: Hiểu biết cơ bản về SQL và cơ sở dữ liệu quan hệ
- **Khái niệm API**: Hiểu REST API và các khái niệm HTTP
- **Công cụ phát triển**: Kinh nghiệm sử dụng dòng lệnh, Git, và trình soạn thảo mã nguồn
- **Kiến thức cơ bản về đám mây**: (Tùy chọn) Hiểu biết cơ bản về Azure hoặc các nền tảng đám mây tương tự
- **Quen thuộc Docker**: (Tùy chọn) Hiểu các khái niệm về container hóa

### Công cụ cần thiết

- **Docker Desktop** - Để chạy PostgreSQL và máy chủ MCP
- **Azure CLI** - Để triển khai tài nguyên đám mây
- **VS Code** - Để phát triển và tích hợp MCP
- **Git** - Để kiểm soát phiên bản
- **Python 3.8+** - Để phát triển máy chủ MCP

## 📚 Hướng dẫn học & Tài nguyên

Lộ trình học này bao gồm các tài nguyên toàn diện giúp bạn điều hướng hiệu quả:

### Hướng dẫn học

Mỗi phòng thí nghiệm bao gồm:
- **Mục tiêu học tập rõ ràng** - Những gì bạn sẽ đạt được
- **Hướng dẫn chi tiết theo bước** - Hướng dẫn triển khai cụ thể
- **Ví dụ mã** - Mẫu mã hoạt động với giải thích
- **Bài tập** - Cơ hội thực hành thực tế
- **Hướng dẫn khắc phục sự cố** - Các vấn đề phổ biến và giải pháp
- **Tài nguyên bổ sung** - Đọc thêm và khám phá sâu hơn

### Kiểm tra Yêu cầu Tiên quyết

Trước khi bắt đầu mỗi phòng thí nghiệm, bạn sẽ thấy:
- **Kiến thức yêu cầu** - Những gì bạn nên biết trước
- **Xác thực thiết lập** - Cách kiểm tra môi trường của bạn
- **Ước tính thời gian** - Thời gian dự kiến hoàn thành
- **Kết quả học tập** - Những gì bạn sẽ biết sau khi hoàn thành

### Lộ trình học khuyến nghị

Chọn lộ trình dựa trên trình độ của bạn:

#### 🟢 **Lộ trình Người mới** (Mới với MCP)
1. Đảm bảo đã hoàn thành 0-10 trong [MCP cho Người mới](https://aka.ms/mcp-for-beginners) trước
2. Hoàn thành các phòng thí nghiệm 00-03 để củng cố nền tảng
3. Theo dõi các phòng thí nghiệm 04-06 để thực hành xây dựng
4. Thử các phòng thí nghiệm 07-09 để sử dụng thực tế

#### 🟡 **Lộ trình Trung cấp** (Có kinh nghiệm MCP)
1. Xem lại các phòng thí nghiệm 00-01 về các khái niệm cơ sở dữ liệu
2. Tập trung vào các phòng thí nghiệm 02-06 để triển khai
3. Đi sâu vào các phòng thí nghiệm 07-12 cho các tính năng nâng cao

#### 🔴 **Lộ trình Nâng cao** (Có kinh nghiệm với MCP)
1. Lướt nhanh các phòng thí nghiệm 00-03 để nắm bối cảnh
2. Tập trung các phòng thí nghiệm 04-09 để tích hợp cơ sở dữ liệu
3. Tập trung vào các phòng thí nghiệm 10-12 cho triển khai sản xuất

## 🛠️ Cách sử dụng lộ trình học này hiệu quả

### Học theo thứ tự (Khuyến nghị)

Làm qua các phòng thí nghiệm theo thứ tự để hiểu sâu:

1. **Đọc tổng quan** - Hiểu bạn sẽ học gì
2. **Kiểm tra yêu cầu tiên quyết** - Đảm bảo bạn có kiến thức cần thiết
3. **Theo hướng dẫn từng bước** - Triển khai khi học
4. **Hoàn thành bài tập** - Củng cố hiểu biết
5. **Xem lại các điểm chính** - Củng cố kết quả học tập

### Học tập có mục tiêu

Nếu bạn cần kỹ năng cụ thể:

- **Tích hợp cơ sở dữ liệu**: Tập trung các phòng thí nghiệm 04-06
- **Triển khai bảo mật**: Tập trung phòng thí nghiệm 02, 08, 12
- **Tìm kiếm AI/Ngữ nghĩa**: Đào sâu phòng thí nghiệm 07
- **Triển khai sản xuất**: Học các phòng thí nghiệm 10-12

### Thực hành thực tế

Mỗi phòng thí nghiệm bao gồm:
- **Ví dụ mã hoạt động** - Sao chép, chỉnh sửa và thử nghiệm
- **Kịch bản thực tế** - Các trường hợp sử dụng phân tích bán lẻ thực tiễn
- **Độ phức tạp tăng dần** - Xây dựng từ đơn giản đến nâng cao
- **Bước xác thực** - Kiểm tra triển khai của bạn hoạt động

## 🌟 Cộng đồng và Hỗ trợ

### Nhận sự giúp đỡ

- **Azure AI Discord**: [Tham gia để được hỗ trợ chuyên gia](https://discord.com/invite/ByRwuEEgH4)
- **Kho GitHub và Mẫu Triển khai**: [Mẫu triển khai và tài nguyên](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Cộng đồng MCP**: [Tham gia thảo luận rộng hơn về MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Sẵn sàng bắt đầu?

Bắt đầu hành trình của bạn với **[Phòng thí nghiệm 00: Giới thiệu về Tích hợp Cơ sở dữ liệu MCP](./00-Introduction/README.md)**

---

*Thành thạo xây dựng máy chủ MCP sẵn sàng sản xuất tích hợp cơ sở dữ liệu thông qua trải nghiệm học thực hành toàn diện này.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->