# Giới thiệu về Tích hợp Cơ sở Dữ liệu MCP

## 🎯 Nội dung của bài thực hành này

Bài thực hành giới thiệu này cung cấp một cái nhìn tổng quan toàn diện về việc xây dựng các máy chủ Model Context Protocol (MCP) với tích hợp cơ sở dữ liệu. Bạn sẽ hiểu rõ về trường hợp kinh doanh, kiến trúc kỹ thuật và các ứng dụng thực tế thông qua trường hợp sử dụng phân tích bán lẻ Zava tại https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Tổng quan

**Model Context Protocol (MCP)** cho phép các trợ lý AI truy cập và tương tác an toàn với các nguồn dữ liệu bên ngoài trong thời gian thực. Khi kết hợp với tích hợp cơ sở dữ liệu, MCP mở ra những khả năng mạnh mẽ cho các ứng dụng AI dựa trên dữ liệu.

Lộ trình học này hướng dẫn bạn xây dựng các máy chủ MCP sẵn sàng cho sản xuất, kết nối các trợ lý AI với dữ liệu bán hàng thông qua PostgreSQL, triển khai các mẫu doanh nghiệp như Bảo mật Cấp Dòng (Row Level Security), tìm kiếm ngữ nghĩa và truy cập dữ liệu đa người dùng.

## Mục tiêu học tập

Kết thúc bài thực hành này, bạn sẽ có thể:

- **Định nghĩa** Model Context Protocol và các lợi ích cốt lõi của nó đối với tích hợp cơ sở dữ liệu
- **Xác định** các thành phần chính của kiến trúc máy chủ MCP với cơ sở dữ liệu
- **Hiểu** trường hợp sử dụng Zava Retail và các yêu cầu kinh doanh của nó
- **Nhận biết** các mẫu doanh nghiệp để truy cập cơ sở dữ liệu an toàn và mở rộng
- **Liệt kê** các công cụ và công nghệ được sử dụng trong lộ trình học này

## 🧭 Thách thức: AI và Dữ liệu Thực tế

### Hạn chế của AI truyền thống

Các trợ lý AI hiện đại rất mạnh mẽ nhưng gặp phải những hạn chế đáng kể khi làm việc với dữ liệu kinh doanh thực tế:

| **Thách thức** | **Mô tả** | **Tác động kinh doanh** |
|----------------|-----------|-------------------------|
| **Kiến thức tĩnh** | Các mô hình AI được huấn luyện trên tập dữ liệu cố định không thể truy cập dữ liệu kinh doanh hiện tại | Thông tin lỗi thời, cơ hội bị bỏ lỡ |
| **Ngăn cách dữ liệu** | Thông tin bị khóa trong cơ sở dữ liệu, API và hệ thống mà AI không thể truy cập | Phân tích không đầy đủ, quy trình làm việc rời rạc |
| **Hạn chế bảo mật** | Truy cập trực tiếp vào cơ sở dữ liệu gây ra các vấn đề về bảo mật và tuân thủ | Triển khai hạn chế, chuẩn bị dữ liệu thủ công |
| **Truy vấn phức tạp** | Người dùng kinh doanh cần kiến thức kỹ thuật để trích xuất thông tin từ dữ liệu | Giảm sự chấp nhận, quy trình không hiệu quả |

### Giải pháp MCP

Model Context Protocol giải quyết những thách thức này bằng cách cung cấp:

- **Truy cập dữ liệu thời gian thực**: Các trợ lý AI truy vấn cơ sở dữ liệu và API trực tiếp
- **Tích hợp an toàn**: Truy cập được kiểm soát với xác thực và quyền hạn
- **Giao diện ngôn ngữ tự nhiên**: Người dùng kinh doanh đặt câu hỏi bằng tiếng Anh đơn giản
- **Giao thức chuẩn hóa**: Hoạt động trên các nền tảng và công cụ AI khác nhau

## 🏪 Zava Retail: Trường hợp học tập của chúng ta https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Trong suốt lộ trình học này, chúng ta sẽ xây dựng một máy chủ MCP cho **Zava Retail**, một chuỗi bán lẻ DIY hư cấu với nhiều địa điểm cửa hàng. Kịch bản thực tế này minh họa việc triển khai MCP cấp doanh nghiệp.

### Bối cảnh kinh doanh

**Zava Retail** vận hành:
- **8 cửa hàng vật lý** tại bang Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 cửa hàng trực tuyến** cho bán hàng thương mại điện tử
- **Danh mục sản phẩm đa dạng** bao gồm dụng cụ, phần cứng, vật liệu làm vườn và xây dựng
- **Quản lý nhiều cấp** với quản lý cửa hàng, quản lý khu vực và lãnh đạo cấp cao

### Yêu cầu kinh doanh

Các quản lý cửa hàng và lãnh đạo cần phân tích hỗ trợ AI để:

1. **Phân tích hiệu suất bán hàng** theo cửa hàng và thời gian
2. **Theo dõi mức tồn kho** và xác định nhu cầu bổ sung hàng
3. **Hiểu hành vi khách hàng** và xu hướng mua sắm
4. **Khám phá thông tin sản phẩm** thông qua tìm kiếm ngữ nghĩa
5. **Tạo báo cáo** bằng các truy vấn ngôn ngữ tự nhiên
6. **Duy trì bảo mật dữ liệu** với kiểm soát truy cập dựa trên vai trò

### Yêu cầu kỹ thuật

Máy chủ MCP phải cung cấp:

- **Truy cập dữ liệu đa người dùng** nơi quản lý cửa hàng chỉ thấy dữ liệu của cửa hàng mình
- **Truy vấn linh hoạt** hỗ trợ các thao tác SQL phức tạp
- **Tìm kiếm ngữ nghĩa** để khám phá và gợi ý sản phẩm
- **Dữ liệu thời gian thực** phản ánh trạng thái kinh doanh hiện tại
- **Xác thực an toàn** với bảo mật cấp dòng
- **Kiến trúc mở rộng** hỗ trợ nhiều người dùng đồng thời

## 🏗️ Tổng quan Kiến trúc Máy chủ MCP

Máy chủ MCP của chúng ta triển khai một kiến trúc phân lớp được tối ưu hóa cho tích hợp cơ sở dữ liệu:

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
- **Đăng ký công cụ**: Định nghĩa công cụ khai báo với độ an toàn kiểu dữ liệu
- **Ngữ cảnh yêu cầu**: Quản lý danh tính người dùng và phiên làm việc
- **Xử lý lỗi**: Quản lý lỗi mạnh mẽ và ghi nhật ký

#### **2. Lớp Tích hợp Cơ sở Dữ liệu**
- **Quản lý kết nối**: Quản lý kết nối asyncpg hiệu quả
- **Nhà cung cấp lược đồ**: Khám phá lược đồ bảng động
- **Trình thực thi truy vấn**: Thực thi SQL an toàn với ngữ cảnh RLS
- **Quản lý giao dịch**: Tuân thủ ACID và xử lý hoàn tác

#### **3. Lớp Bảo mật**
- **Bảo mật Cấp Dòng**: PostgreSQL RLS để cô lập dữ liệu đa người dùng
- **Danh tính người dùng**: Xác thực và ủy quyền quản lý cửa hàng
- **Kiểm soát truy cập**: Quyền hạn chi tiết và dấu vết kiểm toán
- **Xác thực đầu vào**: Ngăn chặn SQL injection và xác thực truy vấn

#### **4. Lớp Tăng cường AI**
- **Tìm kiếm ngữ nghĩa**: Vector embeddings để khám phá sản phẩm
- **Tích hợp Azure OpenAI**: Tạo embeddings văn bản
- **Thuật toán tương tự**: Tìm kiếm tương tự cosine pgvector
- **Tối ưu hóa tìm kiếm**: Lập chỉ mục và điều chỉnh hiệu suất

## 🔧 Công nghệ sử dụng

### Công nghệ cốt lõi

| **Thành phần** | **Công nghệ** | **Mục đích** |
|----------------|---------------|--------------|
| **MCP Framework** | FastMCP (Python) | Triển khai máy chủ MCP hiện đại |
| **Cơ sở dữ liệu** | PostgreSQL 17 + pgvector | Dữ liệu quan hệ với tìm kiếm vector |
| **Dịch vụ AI** | Azure OpenAI | Embeddings văn bản và mô hình ngôn ngữ |
| **Container hóa** | Docker + Docker Compose | Môi trường phát triển |
| **Nền tảng đám mây** | Microsoft Azure | Triển khai sản xuất |
| **Tích hợp IDE** | VS Code | Chat AI và quy trình phát triển |

### Công cụ phát triển

| **Công cụ** | **Mục đích** |
|-------------|--------------|
| **asyncpg** | Driver PostgreSQL hiệu suất cao |
| **Pydantic** | Xác thực và tuần tự hóa dữ liệu |
| **Azure SDK** | Tích hợp dịch vụ đám mây |
| **pytest** | Framework kiểm thử |
| **Docker** | Container hóa và triển khai |

### Ngăn xếp sản xuất

| **Dịch vụ** | **Tài nguyên Azure** | **Mục đích** |
|-------------|-----------------------|--------------|
| **Cơ sở dữ liệu** | Azure Database for PostgreSQL | Dịch vụ cơ sở dữ liệu được quản lý |
| **Container** | Azure Container Apps | Lưu trữ container không máy chủ |
| **Dịch vụ AI** | Azure AI Foundry | Mô hình OpenAI và điểm cuối |
| **Giám sát** | Application Insights | Quan sát và chẩn đoán |
| **Bảo mật** | Azure Key Vault | Quản lý bí mật và cấu hình |

## 🎬 Các kịch bản sử dụng thực tế

Hãy khám phá cách các người dùng khác nhau tương tác với máy chủ MCP của chúng ta:

### Kịch bản 1: Đánh giá hiệu suất của quản lý cửa hàng

**Người dùng**: Sarah, Quản lý cửa hàng Seattle  
**Mục tiêu**: Phân tích hiệu suất bán hàng quý trước

**Truy vấn ngôn ngữ tự nhiên**:
> "Hiển thị 10 sản phẩm hàng đầu theo doanh thu cho cửa hàng của tôi trong Q4 2024"

**Điều gì xảy ra**:
1. VS Code AI Chat gửi truy vấn đến máy chủ MCP
2. Máy chủ MCP xác định ngữ cảnh cửa hàng của Sarah (Seattle)
3. Chính sách RLS lọc dữ liệu chỉ cho cửa hàng Seattle
4. Truy vấn SQL được tạo và thực thi
5. Kết quả được định dạng và trả về cho AI Chat
6. AI cung cấp phân tích và thông tin chi tiết

### Kịch bản 2: Khám phá sản phẩm với tìm kiếm ngữ nghĩa

**Người dùng**: Mike, Quản lý tồn kho  
**Mục tiêu**: Tìm sản phẩm tương tự với yêu cầu của khách hàng

**Truy vấn ngôn ngữ tự nhiên**:
> "Chúng tôi bán những sản phẩm nào tương tự như 'đầu nối điện chống nước cho sử dụng ngoài trời'?"

**Điều gì xảy ra**:
1. Truy vấn được xử lý bởi công cụ tìm kiếm ngữ nghĩa
2. Azure OpenAI tạo vector embedding
3. pgvector thực hiện tìm kiếm tương tự
4. Các sản phẩm liên quan được xếp hạng theo mức độ phù hợp
5. Kết quả bao gồm chi tiết sản phẩm và tình trạng sẵn có
6. AI gợi ý các lựa chọn thay thế và cơ hội gói sản phẩm

### Kịch bản 3: Phân tích chéo cửa hàng

**Người dùng**: Jennifer, Quản lý khu vực  
**Mục tiêu**: So sánh hiệu suất giữa các cửa hàng

**Truy vấn ngôn ngữ tự nhiên**:
> "So sánh doanh số theo danh mục cho tất cả các cửa hàng trong 6 tháng qua"

**Điều gì xảy ra**:
1. Ngữ cảnh RLS được thiết lập cho quyền truy cập của quản lý khu vực
2. Truy vấn phức tạp đa cửa hàng được tạo
3. Dữ liệu được tổng hợp giữa các địa điểm cửa hàng
4. Kết quả bao gồm xu hướng và so sánh
5. AI xác định thông tin chi tiết và gợi ý

## 🔒 Phân tích sâu về Bảo mật và Đa người dùng

Triển khai của chúng ta ưu tiên bảo mật cấp doanh nghiệp:

### Bảo mật Cấp Dòng (RLS)

PostgreSQL RLS đảm bảo cô lập dữ liệu:

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

### Quản lý danh tính người dùng

Mỗi kết nối MCP bao gồm:
- **ID Quản lý cửa hàng**: Định danh duy nhất cho ngữ cảnh RLS
- **Phân công vai trò**: Quyền hạn và mức độ truy cập
- **Quản lý phiên làm việc**: Token xác thực an toàn
- **Ghi nhật ký kiểm toán**: Lịch sử truy cập đầy đủ

### Bảo vệ dữ liệu

Nhiều lớp bảo mật:
- **Mã hóa kết nối**: TLS cho tất cả các kết nối cơ sở dữ liệu
- **Ngăn chặn SQL Injection**: Chỉ sử dụng truy vấn có tham số
- **Xác thực đầu vào**: Xác thực yêu cầu toàn diện
- **Xử lý lỗi**: Không có dữ liệu nhạy cảm trong thông báo lỗi

## 🎯 Những điểm chính cần nhớ

Sau khi hoàn thành phần giới thiệu này, bạn sẽ hiểu:

✅ **Giá trị của MCP**: Cách MCP kết nối trợ lý AI và dữ liệu thực tế  
✅ **Bối cảnh kinh doanh**: Các yêu cầu và thách thức của Zava Retail  
✅ **Tổng quan kiến trúc**: Các thành phần chính và cách chúng tương tác  
✅ **Công nghệ sử dụng**: Các công cụ và framework được sử dụng  
✅ **Mô hình bảo mật**: Truy cập dữ liệu đa người dùng và bảo vệ  
✅ **Mẫu sử dụng**: Các kịch bản truy vấn thực tế và quy trình làm việc  

## 🚀 Tiếp theo

Sẵn sàng đi sâu hơn? Tiếp tục với:

**[Lab 01: Các khái niệm kiến trúc cốt lõi](../01-Architecture/README.md)**

Tìm hiểu về các mẫu kiến trúc máy chủ MCP, nguyên tắc thiết kế cơ sở dữ liệu và triển khai kỹ thuật chi tiết hỗ trợ giải pháp phân tích bán lẻ của chúng ta.

## 📚 Tài liệu bổ sung

### Tài liệu MCP
- [MCP Specification](https://modelcontextprotocol.io/docs/) - Tài liệu chính thức về giao thức
- [MCP for Beginners](https://aka.ms/mcp-for-beginners) - Hướng dẫn học MCP toàn diện
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk) - Tài liệu SDK Python

### Tích hợp cơ sở dữ liệu
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - Tài liệu tham khảo PostgreSQL đầy đủ
- [pgvector Guide](https://github.com/pgvector/pgvector) - Tài liệu hướng dẫn mở rộng vector
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Hướng dẫn RLS PostgreSQL

### Dịch vụ Azure
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - Tích hợp dịch vụ AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Dịch vụ cơ sở dữ liệu được quản lý
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Container không máy chủ

---

**Lưu ý**: Đây là một bài tập học tập sử dụng dữ liệu bán lẻ hư cấu. Luôn tuân thủ các chính sách quản trị và bảo mật dữ liệu của tổ chức bạn khi triển khai các giải pháp tương tự trong môi trường sản xuất.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.