# Giới thiệu về Tích hợp Cơ sở Dữ liệu MCP

> [!NOTE]
> Các sơ đồ hoặc mã trong con đường học tập này sử dụng HTTP/SSE hoặc các tùy chọn khởi tạo
> phản ánh các phụ thuộc MCP mẫu `2025-11-25`. Đối với các triển khai mới,
> hãy sử dụng các yêu cầu không trạng thái `2026-07-28` và HTTP Có thể truyền.

## 🎯 Nội dung của Lab này

Lab giới thiệu này cung cấp cái nhìn tổng quan toàn diện về cách xây dựng máy chủ Model Context Protocol (MCP) với tích hợp cơ sở dữ liệu. Bạn sẽ hiểu về mục đích kinh doanh, kiến trúc kỹ thuật và các ứng dụng thực tế thông qua trường hợp phân tích bán lẻ Zava tại https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Tổng quan

**Model Context Protocol (MCP)** cho phép trợ lý AI truy cập an toàn và tương tác với các nguồn dữ liệu bên ngoài theo thời gian thực. Khi kết hợp với tích hợp cơ sở dữ liệu, MCP mở ra các khả năng mạnh mẽ cho các ứng dụng AI dựa trên dữ liệu.

Con đường học tập này dạy bạn cách xây dựng máy chủ MCP sẵn sàng sản xuất kết nối trợ lý AI với dữ liệu bán lẻ qua PostgreSQL, thực hiện các mẫu doanh nghiệp như Bảo mật Cấp độ Hàng, tìm kiếm ngữ nghĩa, và truy cập dữ liệu đa người thuê.

## Mục tiêu học tập

Sau khi hoàn thành lab này, bạn sẽ có thể:

- **Định nghĩa** Model Context Protocol và các lợi ích cốt lõi cho tích hợp cơ sở dữ liệu
- **Nhận diện** các thành phần chính của kiến trúc máy chủ MCP với cơ sở dữ liệu
- **Hiểu** trường hợp sử dụng Zava Retail và các yêu cầu kinh doanh
- **Nhận biết** các mẫu doanh nghiệp cho truy cập cơ sở dữ liệu an toàn, có thể mở rộng
- **Liệt kê** các công cụ và công nghệ sử dụng xuyên suốt con đường học tập

## 🧭 Thách thức: AI gặp dữ liệu thực tế

### Hạn chế truyền thống của AI

Trợ lý AI hiện đại rất mạnh mẽ nhưng gặp nhiều hạn chế khi làm việc với dữ liệu kinh doanh thực tế:

| **Thách thức** | **Mô tả** | **Ảnh hưởng kinh doanh** |
|---------------|-----------------|-------------------|
| **Kiến thức tĩnh** | Các mô hình AI huấn luyện trên bộ dữ liệu cố định không thể truy cập dữ liệu kinh doanh hiện tại | Thông tin lỗi thời, bỏ lỡ cơ hội |
| **Dữ liệu bị phân mảnh** | Thông tin bị khóa trong cơ sở dữ liệu, API và hệ thống mà AI không thể tiếp cận | Phân tích không đầy đủ, quy trình làm việc rời rạc |
| **Hạn chế bảo mật** | Truy cập trực tiếp cơ sở dữ liệu gây lo ngại về bảo mật và tuân thủ | Triển khai hạn chế, chuẩn bị dữ liệu thủ công |
| **Truy vấn phức tạp** | Người dùng kinh doanh cần kiến thức kỹ thuật để trích xuất thông tin dữ liệu | Giảm sự chấp nhận, quy trình kém hiệu quả |

### Giải pháp MCP

Model Context Protocol giải quyết các thách thức này bằng cách cung cấp:

- **Truy cập dữ liệu theo thời gian thực**: Trợ lý AI truy vấn cơ sở dữ liệu và API trực tiếp
- **Tích hợp an toàn**: Kiểm soát truy cập với xác thực và quyền hạn
- **Giao diện ngôn ngữ tự nhiên**: Người dùng kinh doanh đặt câu hỏi bằng tiếng Anh đơn giản
- **Giao thức chuẩn hóa**: Hoạt động trên nhiều nền tảng và công cụ AI khác nhau

## 🏪 Gặp gỡ Zava Retail: Trường hợp nghiên cứu học tập của chúng ta https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Trong suốt con đường học tập này, chúng ta sẽ xây dựng một máy chủ MCP cho **Zava Retail**, một chuỗi bán lẻ DIY giả định với nhiều cửa hàng. Kịch bản thực tế này minh hoạ việc triển khai MCP cấp doanh nghiệp.

### Bối cảnh kinh doanh

**Zava Retail** hoạt động:
- **8 cửa hàng vật lý** trên toàn bang Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 cửa hàng trực tuyến** cho bán hàng thương mại điện tử
- **Danh mục sản phẩm đa dạng** bao gồm dụng cụ, phần cứng, vật tư làm vườn, và vật liệu xây dựng
- **Quản lý đa cấp** với quản lý cửa hàng, quản lý khu vực, và ban điều hành

### Yêu cầu kinh doanh

Quản lý cửa hàng và ban điều hành cần phân tích dựa trên AI để:

1. **Phân tích hiệu suất bán hàng** qua các cửa hàng và khoảng thời gian
2. **Theo dõi mức tồn kho** và xác định nhu cầu bổ sung
3. **Hiểu hành vi khách hàng** và các mẫu mua hàng
4. **Khám phá thông tin sản phẩm** qua tìm kiếm ngữ nghĩa
5. **Tạo báo cáo** với các truy vấn bằng ngôn ngữ tự nhiên
6. **Duy trì bảo mật dữ liệu** với kiểm soát truy cập theo vai trò

### Yêu cầu kỹ thuật

Máy chủ MCP phải cung cấp:

- **Truy cập dữ liệu đa người thuê** nơi quản lý cửa hàng chỉ xem dữ liệu cửa hàng của mình
- **Truy vấn linh hoạt** hỗ trợ các phép toán SQL phức tạp
- **Tìm kiếm ngữ nghĩa** để khám phá sản phẩm và đề xuất
- **Dữ liệu theo thời gian thực** phản ánh trạng thái kinh doanh hiện tại
- **Xác thực an toàn** với bảo mật cấp hàng
- **Kiến trúc có thể mở rộng** hỗ trợ nhiều người dùng đồng thời

## 🏗️ Tổng quan kiến trúc máy chủ MCP

Máy chủ MCP của chúng ta sử dụng kiến trúc phân lớp tối ưu cho tích hợp cơ sở dữ liệu:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Các thành phần chính

#### **1. Lớp Máy chủ MCP**
- **FastMCP Framework**: Triển khai máy chủ MCP hiện đại bằng Python
- **Đăng ký Công cụ**: Định nghĩa công cụ khai báo với an toàn kiểu
- **Ngữ cảnh Yêu cầu**: Quản lý nhận dạng người dùng và phiên làm việc
- **Xử lý Lỗi**: Quản lý lỗi ổn định và ghi nhật ký

#### **2. Lớp Tích hợp Cơ sở Dữ liệu**
- **Kết nối Pooling**: Quản lý kết nối asyncpg hiệu quả
- **Nhà cung cấp Schema**: Khám phá schema bảng động
- **Thực thi Truy vấn**: Thực thi SQL an toàn với ngữ cảnh RLS
- **Quản lý Giao dịch**: Tuân thủ ACID và xử lý rollback

#### **3. Lớp Bảo mật**
- **Bảo mật Cấp hàng (Row Level Security)**: PostgreSQL RLS cho cách ly dữ liệu đa người thuê
- **Nhận dạng Người dùng**: Xác thực và ủy quyền quản lý cửa hàng
- **Kiểm soát Truy cập**: Quyền hạn chi tiết và theo dõi kiểm toán
- **Kiểm tra Đầu vào**: Phòng chống SQL injection và xác thực truy vấn

#### **4. Lớp Nâng cao AI**
- **Tìm kiếm Ngữ nghĩa**: Vector embeddings để khám phá sản phẩm
- **Tích hợp Azure OpenAI**: Tạo embedding văn bản
- **Thuật toán Tương đồng**: Tìm kiếm tương đồng cosine với pgvector
- **Tối ưu Tìm kiếm**: Chỉ mục và tinh chỉnh hiệu suất

## 🔧 Ngăn xếp Công nghệ

### Công nghệ Cốt lõi

| **Thành phần** | **Công nghệ** | **Mục đích** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Triển khai máy chủ MCP hiện đại |
| **Cơ sở Dữ liệu** | PostgreSQL 17 + pgvector | Dữ liệu quan hệ với tìm kiếm vector |
| **Dịch vụ AI** | Azure OpenAI | Embeddings văn bản và mô hình ngôn ngữ |
| **Đóng gói Container** | Docker + Docker Compose | Môi trường phát triển |
| **Nền tảng đám mây** | Microsoft Azure | Triển khai sản xuất |
| **Tích hợp IDE** | VS Code | Chat AI và quy trình phát triển |

### Công cụ Phát triển

| **Công cụ** | **Mục đích** |
|----------|-------------|
| **asyncpg** | Trình điều khiển PostgreSQL hiệu năng cao |
| **Pydantic** | Xác thực và tuần tự hóa dữ liệu |
| **Azure SDK** | Tích hợp dịch vụ đám mây |
| **pytest** | Khung kiểm thử |
| **Docker** | Đóng gói container và triển khai |

### Ngăn xếp Sản xuất

| **Dịch vụ** | **Tài nguyên Azure** | **Mục đích** |
|-------------|-------------------|-------------|
| **Cơ sở dữ liệu** | Azure Database for PostgreSQL | Dịch vụ cơ sở dữ liệu được quản lý |
| **Container** | Azure Container Apps | Hosting container không máy chủ |
| **Dịch vụ AI** | Microsoft Foundry | Mô hình OpenAI và các điểm cuối |
| **Giám sát** | Application Insights | Quan sát và chẩn đoán |
| **Bảo mật** | Azure Key Vault | Quản lý bí mật và cấu hình |

## 🎬 Các kịch bản sử dụng thực tế

Hãy khám phá cách các người dùng khác nhau tương tác với máy chủ MCP của chúng ta:

### Kịch bản 1: Đánh giá Hiệu suất Quản lý Cửa hàng

**Người dùng**: Sarah, Quản lý cửa hàng Seattle  
**Mục tiêu**: Phân tích hiệu suất bán hàng quý trước

**Truy vấn Ngôn ngữ Tự nhiên**:
> "Hiển thị 10 sản phẩm hàng đầu theo doanh thu cho cửa hàng tôi trong quý 4 năm 2024"

**Chuyện gì xảy ra**:
1. VS Code AI Chat gửi truy vấn đến máy chủ MCP
2. Máy chủ MCP xác định ngữ cảnh cửa hàng của Sarah (Seattle)
3. Chính sách RLS lọc dữ liệu chỉ cho cửa hàng Seattle
4. Truy vấn SQL được sinh ra và thực thi
5. Kết quả được định dạng và trả về AI Chat
6. AI cung cấp phân tích và những hiểu biết

### Kịch bản 2: Khám phá Sản phẩm với Tìm kiếm Ngữ nghĩa

**Người dùng**: Mike, Quản lý Tồn kho  
**Mục tiêu**: Tìm sản phẩm tương tự với yêu cầu khách hàng

**Truy vấn Ngôn ngữ Tự nhiên**:
> "Chúng ta bán những sản phẩm nào tương tự 'đầu nối điện chống nước cho sử dụng ngoài trời'?"

**Chuyện gì xảy ra**:
1. Truy vấn được xử lý bởi công cụ tìm kiếm ngữ nghĩa
2. Azure OpenAI tạo vector embedding
3. pgvector thực hiện tìm kiếm tương đồng
4. Sản phẩm liên quan được xếp hạng theo mức độ liên quan
5. Kết quả bao gồm chi tiết sản phẩm và tình trạng tồn kho
6. AI gợi ý các lựa chọn thay thế và cơ hội gói sản phẩm

### Kịch bản 3: Phân tích Liên cửa hàng

**Người dùng**: Jennifer, Quản lý Khu vực  
**Mục tiêu**: So sánh hiệu suất tại tất cả các cửa hàng

**Truy vấn Ngôn ngữ Tự nhiên**:
> "So sánh doanh thu theo danh mục cho tất cả cửa hàng trong 6 tháng qua"

**Chuyện gì xảy ra**:
1. Ngữ cảnh RLS được đặt cho quyền truy cập quản lý khu vực
2. Truy vấn phức tạp đa cửa hàng được tạo ra
3. Dữ liệu được tổng hợp qua các vị trí cửa hàng
4. Kết quả bao gồm xu hướng và so sánh
5. AI xác định các hiểu biết và đề xuất

## 🔒 Tìm hiểu sâu về Bảo mật và Đa người thuê

Triển khai của chúng ta ưu tiên bảo mật cấp doanh nghiệp:

### Bảo mật Cấp độ Hàng (Row Level Security - RLS)

PostgreSQL RLS bảo đảm cách ly dữ liệu:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Quản lý Nhận dạng Người dùng

Mỗi kết nối MCP bao gồm:
- **ID Quản lý cửa hàng**: Định danh duy nhất cho ngữ cảnh RLS
- **Phân công Vai trò**: Quyền hạn và mức độ truy cập
- **Quản lý Phiên**: Mã xác thực an toàn
- **Ghi nhật ký Kiểm toán**: Lịch sử truy cập đầy đủ

### Bảo vệ Dữ liệu

Nhiều lớp bảo mật:
- **Mã hóa Kết nối**: TLS cho tất cả kết nối cơ sở dữ liệu
- **Phòng chống SQL Injection**: Chỉ sử dụng truy vấn tham số hóa
- **Xác thực Đầu vào**: Xác thực yêu cầu toàn diện
- **Xử lý Lỗi**: Không có dữ liệu nhạy cảm trong thông báo lỗi

## 🎯 Các điểm cần ghi nhớ

Sau khi hoàn thành phần giới thiệu này, bạn sẽ hiểu:

✅ **Giá trị MCP**: Cách MCP kết nối trợ lý AI với dữ liệu thực tế  
✅ **Bối cảnh Kinh doanh**: Yêu cầu và thách thức của Zava Retail  
✅ **Tổng quan Kiến trúc**: Các thành phần chính và cách chúng tương tác  
✅ **Ngăn xếp Công nghệ**: Công cụ và khung làm việc sử dụng xuyên suốt  
✅ **Mô hình Bảo mật**: Truy cập và bảo vệ dữ liệu đa người thuê  
✅ **Mẫu Sử dụng**: Các kịch bản truy vấn thực tế và quy trình làm việc  

## 🚀 Tiếp theo là gì

Sẵn sàng đi sâu hơn? Tiếp tục với:

**[Lab 01: Các Khái niệm Kiến trúc Cốt lõi](../01-Architecture/README.md)**

Tìm hiểu các mẫu kiến trúc máy chủ MCP, nguyên tắc thiết kế cơ sở dữ liệu, và triển khai kỹ thuật chi tiết hỗ trợ giải pháp phân tích bán lẻ của chúng ta.

## 📚 Tài nguyên bổ sung

### Tài liệu MCP
- [Đặc tả MCP](https://modelcontextprotocol.io/docs/) - Tài liệu chính thức về giao thức
- [MCP cho Người mới bắt đầu](https://aka.ms/mcp-for-beginners) - Hướng dẫn học tập toàn diện về MCP
- [Tài liệu FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Tài liệu SDK Python

### Tích hợp Cơ sở Dữ liệu
- [Tài liệu PostgreSQL](https://www.postgresql.org/docs/) - Tài liệu tham khảo PostgreSQL đầy đủ
- [Hướng dẫn pgvector](https://github.com/pgvector/pgvector) - Tài liệu mở rộng vector
- [Bảo mật Cấp Hàng](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Hướng dẫn PostgreSQL RLS

### Dịch vụ Azure
- [Tài liệu Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Tích hợp dịch vụ AI
- [Azure Database cho PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Dịch vụ cơ sở dữ liệu được quản lý
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Container không máy chủ

---

**Tuyên bố từ chối trách nhiệm**: Đây là bài tập học tập sử dụng dữ liệu bán lẻ giả định. Luôn tuân thủ chính sách quản trị dữ liệu và bảo mật của tổ chức khi triển khai các giải pháp tương tự trong môi trường sản xuất.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->