# 🚀 10 Máy chủ Microsoft MCP Đang Thay Đổi Năng Suất Lập Trình Viên

## 🎯 Bạn Sẽ Học Gì Trong Hướng Dẫn Này

Hướng dẫn thực tế này giới thiệu mười máy chủ Microsoft MCP đang tích cực thay đổi cách các lập trình viên làm việc với trợ lý AI. Thay vì chỉ giải thích những gì máy chủ MCP *có thể* làm, chúng tôi sẽ chỉ cho bạn những máy chủ đã tạo ra sự khác biệt thực sự trong quy trình làm việc phát triển hàng ngày tại Microsoft và ngoài ra.

Mỗi máy chủ trong hướng dẫn này được chọn dựa trên việc sử dụng thực tế và phản hồi từ các lập trình viên. Bạn sẽ khám phá không chỉ chức năng của từng máy chủ mà còn lý do nó quan trọng và cách tận dụng tối đa trong dự án của bạn. Dù bạn hoàn toàn mới với MCP hay muốn mở rộng thiết lập hiện có, những máy chủ này đại diện cho một số công cụ thiết thực và có tác động lớn trong hệ sinh thái Microsoft.

> **💡 Mẹo Bắt Đầu Nhanh**
> 
> Mới với MCP? Đừng lo! Hướng dẫn này được thiết kế thân thiện với người mới. Chúng tôi sẽ giải thích các khái niệm trong quá trình đi, và bạn luôn có thể tham khảo lại các mô-đun [Giới thiệu về MCP](../00-Introduction/README.md) và [Khái niệm Cốt lõi](../01-CoreConcepts/README.md) để hiểu sâu hơn.

## Tổng Quan

Hướng dẫn toàn diện này khám phá mười máy chủ Microsoft MCP đang cách mạng hóa cách lập trình viên tương tác với trợ lý AI và công cụ bên ngoài. Từ quản lý tài nguyên Azure đến xử lý tài liệu, những máy chủ này chứng minh sức mạnh của Giao thức Ngữ cảnh Mô hình trong việc tạo ra quy trình phát triển trơn tru và hiệu quả.

## Mục Tiêu Học Tập

Cuối hướng dẫn này, bạn sẽ:
- Hiểu cách các máy chủ MCP nâng cao năng suất lập trình viên
- Tìm hiểu về các triển khai máy chủ MCP có tác động lớn nhất của Microsoft
- Khám phá các trường hợp sử dụng thực tế cho từng máy chủ
- Biết cách thiết lập và cấu hình các máy chủ này trong VS Code và Visual Studio
- Khám phá hệ sinh thái MCP rộng lớn hơn và các hướng phát triển tương lai

## 🔧 Hiểu Về Các Máy Chủ MCP: Hướng Dẫn Cho Người Mới Bắt Đầu

### Máy Chủ MCP Là Gì?

Là người mới với Giao thức Ngữ cảnh Mô hình (MCP), bạn có thể thắc mắc: "Máy chủ MCP chính xác là gì và tại sao tôi nên quan tâm?" Hãy bắt đầu với một phép so sánh đơn giản.

Hãy coi các máy chủ MCP như những trợ lý chuyên biệt giúp bạn đồng hành lập trình AI (như GitHub Copilot) kết nối với các công cụ và dịch vụ bên ngoài. Giống như bạn sử dụng các ứng dụng khác nhau trên điện thoại cho các tác vụ khác nhau—một ứng dụng cho dự báo thời tiết, một cho điều hướng, một cho ngân hàng—máy chủ MCP mang đến cho trợ lý AI của bạn khả năng tương tác với các công cụ và dịch vụ phát triển khác nhau.

### Vấn Đề Các Máy Chủ MCP Giải Quyết

Trước khi có các máy chủ MCP, nếu bạn muốn:
- Kiểm tra tài nguyên Azure của bạn
- Tạo một issue trên GitHub
- Truy vấn cơ sở dữ liệu của bạn
- Tìm kiếm qua tài liệu

Bạn phải dừng việc lập trình, mở trình duyệt, điều hướng đến trang web phù hợp và thực hiện các nhiệm vụ này thủ công. Việc chuyển đổi ngữ cảnh liên tục này làm gián đoạn dòng làm việc và giảm năng suất.

### Cách Các Máy Chủ MCP Thay Đổi Trải Nghiệm Phát Triển Của Bạn

Với các máy chủ MCP, bạn có thể ở lại trong môi trường phát triển (VS Code, Visual Studio, v.v.) và đơn giản là yêu cầu trợ lý AI của bạn xử lý các tác vụ này. Ví dụ:

**Thay vì quy trình truyền thống này:**
1. Dừng lập trình
2. Mở trình duyệt
3. Điều hướng đến cổng Azure
4. Tra cứu chi tiết tài khoản lưu trữ
5. Quay lại VS Code
6. Tiếp tục lập trình

**Bạn có thể làm như sau:**
1. Hỏi AI: "Tình trạng các tài khoản lưu trữ Azure của tôi như thế nào?"
2. Tiếp tục lập trình với thông tin được cung cấp

### Lợi Ích Chính Cho Người Mới

#### 1. 🔄 **Giữ Trạng Thái Dòng Làm Việc**
- Không phải chuyển đổi giữa nhiều ứng dụng
- Giữ tập trung vào mã bạn đang viết
- Giảm gánh nặng tinh thần khi quản lý các công cụ khác nhau

#### 2. 🤖 **Sử Dụng Ngôn Ngữ Tự Nhiên Thay Vì Các Lệnh Phức Tạp**
- Thay vì ghi nhớ cú pháp SQL, hãy mô tả dữ liệu bạn cần
- Thay vì nhớ các lệnh Azure CLI, hãy giải thích mục tiêu của bạn
- Để AI xử lý các chi tiết kỹ thuật trong khi bạn tập trung vào logic

#### 3. 🔗 **Kết Nối Nhiều Công Cụ Với Nhau**
- Tạo quy trình mạnh mẽ bằng cách kết hợp các dịch vụ khác nhau
- Ví dụ: "Lấy tất cả các issue GitHub gần đây và tạo các công việc tương ứng trong Azure DevOps"
- Xây dựng tự động hóa mà không cần viết kịch bản phức tạp

#### 4. 🌐 **Truy Cập Hệ Sinh Thái Đang Phát Triển**
- Tận hưởng các máy chủ do Microsoft, GitHub và các công ty khác xây dựng
- Kết hợp công cụ từ các nhà cung cấp khác nhau một cách liền mạch
- Tham gia hệ sinh thái chuẩn hóa hoạt động trên nhiều trợ lý AI khác nhau

#### 5. 🛠️ **Học Qua Thực Hành**
- Bắt đầu với các máy chủ có sẵn để hiểu các khái niệm
- Dần dần xây dựng máy chủ của riêng bạn khi bạn quen hơn
- Sử dụng SDK và tài liệu có sẵn để hướng dẫn việc học của bạn

### Ví Dụ Thực Tế Cho Người Mới

Giả sử bạn mới bắt đầu phát triển web và đang làm dự án đầu tiên. Dưới đây là cách máy chủ MCP có thể giúp bạn:

**Phương pháp truyền thống:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**Với các máy chủ MCP:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Lợi Thế Chuẩn Doanh Nghiệp

MCP đang trở thành tiêu chuẩn trên toàn ngành, có nghĩa là:
- **Tính nhất quán**: Trải nghiệm tương tự trên nhiều công cụ và công ty
- **Tính tương tác**: Các máy chủ từ các nhà cung cấp khác nhau hoạt động cùng nhau
- **Bảo vệ tương lai**: Kỹ năng và thiết lập chuyển giao giữa các trợ lý AI khác nhau
- **Cộng đồng**: Hệ sinh thái lớn với kiến thức và nguồn lực chia sẻ

### Bắt Đầu: Bạn Sẽ Học Gì

Trong hướng dẫn này, chúng tôi sẽ khám phá 10 máy chủ Microsoft MCP đặc biệt hữu ích cho các lập trình viên ở mọi trình độ. Mỗi máy chủ được thiết kế để:
- Giải quyết các thách thức phát triển phổ biến
- Giảm tác vụ lặp đi lặp lại
- Cải thiện chất lượng mã nguồn
- Tăng cơ hội học tập

> **💡 Mẹo Học Tập**
> 
> Nếu bạn hoàn toàn mới với MCP, hãy bắt đầu với các mô-đun [Giới thiệu về MCP](../00-Introduction/README.md) và [Khái niệm Cốt lõi](../01-CoreConcepts/README.md). Sau đó quay lại đây để xem các khái niệm này được ứng dụng với các công cụ Microsoft thực tế.
>
> Để hiểu thêm về tầm quan trọng của MCP, hãy xem bài viết của Maria Naggaga: [Kết Nối Một Lần, Tích Hợp Mọi Nơi Với MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Bắt Đầu Với MCP trong VS Code và Visual Studio 🚀

Việc thiết lập các máy chủ MCP này khá đơn giản nếu bạn sử dụng Visual Studio Code hoặc Visual Studio 2022 với GitHub Copilot.

### Thiết Lập VS Code

Dưới đây là quy trình cơ bản cho VS Code:

1. **Bật Chế Độ Agent**: Trong VS Code, chuyển sang chế độ Agent trong cửa sổ Copilot Chat
2. **Cấu Hình Máy Chủ MCP**: Thêm cấu hình máy chủ vào tệp settings.json của VS Code
3. **Khởi Động Máy Chủ**: Nhấn nút "Start" cho từng máy chủ bạn muốn sử dụng
4. **Chọn Công Cụ**: Chọn các máy chủ MCP để kích hoạt trong phiên hiện tại

Để biết hướng dẫn thiết lập chi tiết, xem tài liệu [VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Mẹo Chuyên Nghiệp: Quản Lý Máy Chủ MCP như một chuyên gia!**
> 
> Giao diện Extensions của VS Code giờ đây bao gồm [giao diện mới tiện lợi để quản lý các Máy Chủ MCP đã cài đặt](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Bạn có thể nhanh chóng khởi động, dừng và quản lý bất kỳ Máy Chủ MCP nào bằng giao diện rõ ràng và đơn giản. Hãy thử ngay!

### Thiết Lập Visual Studio 2022

Đối với Visual Studio 2022 (phiên bản 17.14 trở lên):

1. **Bật Chế Độ Agent**: Nhấn dropdown "Ask" trong cửa sổ GitHub Copilot Chat và chọn "Agent"
2. **Tạo Tệp Cấu Hình**: Tạo tệp `.mcp.json` trong thư mục giải pháp của bạn (vị trí đề xuất: `<SOLUTIONDIR>\.mcp.json`)
3. **Cấu Hình Máy Chủ**: Thêm cấu hình máy chủ MCP của bạn bằng định dạng MCP tiêu chuẩn
4. **Phê Duyệt Công Cụ**: Khi được yêu cầu, phê duyệt các công cụ bạn muốn dùng với quyền truy cập phạm vi thích hợp

Để biết hướng dẫn thiết lập chi tiết cho Visual Studio, xem tài liệu [Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Mỗi máy chủ MCP có yêu cầu cấu hình riêng (chuỗi kết nối, xác thực, v.v.), nhưng mẫu thiết lập đều nhất quán trên cả hai IDE.

## Bài Học Rút Ra Từ Các Máy Chủ Microsoft MCP 🛠️

### 1. 📚 Máy Chủ Microsoft Learn Docs MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Chức năng**: Máy chủ Microsoft Learn Docs MCP là dịch vụ lưu trữ trên đám mây cung cấp cho trợ lý AI quyền truy cập thời gian thực vào tài liệu chính thức của Microsoft thông qua Giao thức Ngữ cảnh Mô hình. Nó kết nối đến `https://learn.microsoft.com/api/mcp` và cho phép tìm kiếm ngữ nghĩa trên Microsoft Learn, tài liệu Azure, tài liệu Microsoft 365 và các nguồn chính thức khác của Microsoft.

**Tại sao nó hữu ích**: Dù có vẻ chỉ là "tài liệu," máy chủ này thực sự rất quan trọng với mọi lập trình viên sử dụng công nghệ Microsoft. Một trong những phàn nàn lớn nhất từ các lập trình viên .NET về trợ lý lập trình AI là chúng không cập nhật kịp các phiên bản .NET và C# mới nhất. Máy chủ Microsoft Learn Docs MCP giải quyết điều này bằng cách cung cấp quyền truy cập thời gian thực vào tài liệu, tham khảo API và các thực tiễn tốt nhất mới nhất. Dù bạn làm việc với các SDK Azure mới nhất, khám phá tính năng mới của C# 13, hay áp dụng các mẫu Aspire tiên tiến, máy chủ này đảm bảo trợ lý AI của bạn có thông tin chính thống và cập nhật để tạo ra mã chính xác và hiện đại.

**Sử dụng thực tế**: "Các lệnh az cli để tạo một ứng dụng container Azure theo tài liệu chính thức Microsoft Learn là gì?" hoặc "Làm thế nào để cấu hình Entity Framework với dependency injection trong ASP.NET Core?" Hay "Xem xét mã này để đảm bảo nó phù hợp với các khuyến nghị về hiệu năng trong Tài liệu Microsoft Learn." Máy chủ cung cấp phạm vi bao phủ toàn diện trên Microsoft Learn, tài liệu Azure và Microsoft 365, sử dụng tìm kiếm ngữ nghĩa nâng cao để tìm thông tin phù hợp nhất với ngữ cảnh. Nó trả về tới 10 đoạn nội dung chất lượng cao với tiêu đề bài viết và URL, luôn truy cập tài liệu Microsoft mới nhất khi được xuất bản.

**Ví dụ nổi bật**: Máy chủ cung cấp công cụ `microsoft_docs_search` thực hiện tìm kiếm ngữ nghĩa đối với tài liệu kỹ thuật chính thức của Microsoft. Khi được cấu hình, bạn có thể hỏi các câu như "Làm thế nào để thực hiện xác thực JWT trong ASP.NET Core?" và nhận câu trả lời chi tiết, chính thức với liên kết nguồn. Chất lượng tìm kiếm xuất sắc vì nó hiểu ngữ cảnh – hỏi về "containers" trong ngữ cảnh Azure sẽ trả về tài liệu về Azure Container Instances, trong khi cùng thuật ngữ trong ngữ cảnh .NET trả về thông tin tập hợp C# liên quan.

Điều này đặc biệt hữu ích đối với thư viện và trường hợp sử dụng thay đổi nhanh hoặc mới cập nhật. Ví dụ, trong một số dự án lập trình gần đây tôi muốn khai thác các tính năng trong các bản phát hành mới nhất của Aspire và Microsoft.Extensions.AI. Bằng cách thêm máy chủ Microsoft Learn Docs MCP, tôi không chỉ tận dụng được tài liệu API mà còn các bài hướng dẫn và chỉ dẫn vừa được công bố.

> **💡 Mẹo Chuyên Nghiệp**
> 
> Ngay cả các mô hình thân thiện với công cụ cũng cần được khuyến khích sử dụng công cụ MCP! Hãy cân nhắc thêm một lời nhắc hệ thống hoặc [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) như: "Bạn có quyền truy cập `microsoft.docs.mcp` – sử dụng công cụ này để tìm kiếm tài liệu chính thức mới nhất của Microsoft khi xử lý các câu hỏi về công nghệ Microsoft như C#, Azure, ASP.NET Core hoặc Entity Framework."
>
> Để xem một ví dụ xuất sắc về điều này, hãy xem chế độ chat [C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) từ kho Awesome GitHub Copilot. Chế độ này đặc biệt tận dụng máy chủ Microsoft Learn Docs MCP để giúp làm sạch và hiện đại hóa mã C# bằng các mẫu và thực tiễn tốt nhất mới nhất.
### 2. ☁️ Máy Chủ Azure MCP


[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Nó làm gì**: Azure MCP Server là một bộ đầy đủ gồm hơn 15 bộ kết nối dịch vụ Azure chuyên biệt mang toàn bộ hệ sinh thái Azure vào quy trình làm việc AI của bạn. Đây không chỉ là một máy chủ đơn lẻ – mà là một tập hợp mạnh mẽ bao gồm quản lý tài nguyên, kết nối cơ sở dữ liệu (PostgreSQL, SQL Server), phân tích nhật ký Azure Monitor với KQL, tích hợp Cosmos DB, và rất nhiều thứ khác nữa.

**Tại sao nó hữu ích**: Ngoài việc quản lý tài nguyên Azure, máy chủ này cải thiện đáng kể chất lượng mã khi làm việc với Azure SDK. Khi bạn sử dụng Azure MCP ở chế độ Agent, nó không chỉ giúp bạn viết mã – mà còn giúp bạn viết *mã Azure tốt hơn* theo các mẫu chứng thực hiện tại, thực hành xử lý lỗi tốt nhất, và tận dụng các tính năng SDK mới nhất. Thay vì nhận được mã chung chung có thể hoạt động, bạn sẽ nhận được mã theo các mẫu được Azure khuyến nghị cho các khối lượng công việc sản xuất.

**Các module chính bao gồm**:
- **🗄️ Bộ kết nối cơ sở dữ liệu**: Truy cập ngôn ngữ tự nhiên trực tiếp vào Azure Database cho PostgreSQL và SQL Server
- **📊 Azure Monitor**: Phân tích nhật ký dựa trên KQL và thông tin vận hành
- **🌐 Quản lý tài nguyên**: Quản lý vòng đời tài nguyên Azure đầy đủ
- **🔐 Xác thực**: Các mẫu DefaultAzureCredential và managed identity
- **📦 Dịch vụ lưu trữ**: Thao tác Blob Storage, Queue Storage và Table Storage
- **🚀 Dịch vụ container**: Quản lý Azure Container Apps, Container Instances và AKS
- **Và nhiều bộ kết nối chuyên biệt khác**

**Sử dụng thực tế**: "Liệt kê các tài khoản lưu trữ Azure của tôi", "Truy vấn workspace Log Analytics của tôi để tìm lỗi trong giờ qua", hoặc "Giúp tôi xây dựng ứng dụng Azure dùng Node.js với xác thực đúng"

**Kịch bản demo đầy đủ**: Dưới đây là hướng dẫn hoàn chỉnh cho thấy sức mạnh của việc kết hợp Azure MCP với tiện ích mở rộng GitHub Copilot for Azure trong VS Code. Khi bạn cài cả hai và yêu cầu:

> "Tạo một script Python tải lên file lên Azure Blob Storage dùng xác thực DefaultAzureCredential. Script phải kết nối với tài khoản lưu trữ Azure của tôi tên 'mycompanystorage', tải lên container tên 'documents', tạo tệp thử nghiệm với dấu thời gian hiện tại để tải lên, xử lý lỗi nhẹ nhàng và cung cấp thông tin hữu ích, tuân theo các thực hành tốt nhất của Azure về xác thực và xử lý lỗi, bao gồm chú thích giải thích cách hoạt động của xác thực DefaultAzureCredential, và làm script có cấu trúc tốt với các hàm và tài liệu đầy đủ."

Azure MCP Server sẽ tạo một script Python hoàn chỉnh sẵn sàng cho sản xuất mà:
- Sử dụng SDK Azure Blob Storage mới nhất với các mẫu async đúng chuẩn
- Triển khai DefaultAzureCredential với giải thích đầy đủ về chuỗi fallback
- Bao gồm xử lý lỗi mạnh mẽ với các loại ngoại lệ Azure cụ thể
- Tuân theo thực hành tốt nhất của SDK Azure về quản lý tài nguyên và kết nối
- Cung cấp ghi nhật ký chi tiết và hiển thị thông tin hữu ích trên console
- Tạo script có cấu trúc đúng với các hàm, tài liệu và gợi ý kiểu

Điều làm nên sự khác biệt là nếu không có Azure MCP, bạn có thể nhận được mã blob storage chung chung hoạt động nhưng không theo các mẫu Azure hiện tại. Với Azure MCP, bạn nhận mã tận dụng phương pháp xác thực mới nhất, xử lý các kịch bản lỗi đặc thù Azure, và tuân theo các thực hành được Microsoft khuyến nghị cho ứng dụng sản xuất.

**Ví dụ nổi bật**: Tôi từng gặp khó khăn khi nhớ chính xác các lệnh `az` và `azd` CLI dùng ad-hoc. Luôn là quy trình hai bước với tôi: đầu tiên tra cú pháp, rồi chạy lệnh. Tôi thường vào portal và click quanh để làm việc vì không muốn thừa nhận mình không nhớ cú pháp CLI. Khả năng chỉ cần mô tả điều tôi muốn thật tuyệt, và tuyệt hơn nữa là làm việc đó ngay trong IDE của tôi!

Có một danh sách sử dụng rất tốt trong [kho Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) để bạn bắt đầu. Để có hướng dẫn thiết lập chi tiết và tùy chọn cấu hình nâng cao, tham khảo [tài liệu chính thức Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Nó làm gì**: GitHub MCP Server chính thức cung cấp tích hợp liền mạch với toàn bộ hệ sinh thái GitHub, bao gồm lựa chọn truy cập từ xa được host và triển khai Docker cục bộ. Đây không chỉ về các thao tác cơ bản trên kho chứa – mà là bộ công cụ toàn diện bao gồm quản lý GitHub Actions, quy trình pull request, theo dõi issue, quét bảo mật, thông báo, và khả năng tự động hóa nâng cao.

**Tại sao nó hữu ích**: Máy chủ này thay đổi cách bạn tương tác với GitHub bằng cách đưa trải nghiệm toàn bộ nền tảng trực tiếp vào môi trường phát triển của bạn. Thay vì liên tục chuyển đổi giữa VS Code và GitHub.com để quản lý dự án, đánh giá mã, và giám sát CI/CD, bạn có thể xử lý mọi thứ qua các lệnh ngôn ngữ tự nhiên trong khi vẫn tập trung vào mã của mình.

> **ℹ️ Lưu ý: Các loại 'Agent' khác nhau**
> 
> Đừng nhầm lẫn GitHub MCP Server này với GitHub's Coding Agent (agent AI bạn có thể giao issue để tự động hóa nhiệm vụ mã hóa). GitHub MCP Server làm việc trong chế độ Agent của VS Code để cung cấp tích hợp API GitHub, trong khi Coding Agent của GitHub là một tính năng riêng biệt tạo pull request khi được giao issue GitHub.

**Các khả năng chính bao gồm**:
- **⚙️ GitHub Actions**: Quản lý toàn bộ pipeline CI/CD, giám sát workflow, và xử lý artifact
- **🔀 Pull Requests**: Tạo, xem xét, hợp nhất, và quản lý PR với theo dõi trạng thái toàn diện
- **🐛 Issues**: Quản lý toàn bộ vòng đời issue, bình luận, gán nhãn, và phân công
- **🔒 Bảo mật**: Cảnh báo quét mã, phát hiện bí mật, và tích hợp Dependabot
- **🔔 Thông báo**: Quản lý thông báo thông minh và kiểm soát đăng ký kho chứa
- **📁 Quản lý kho chứa**: Thao tác tệp, quản lý nhánh, và quản trị kho chứa
- **👥 Hợp tác**: Tìm kiếm người dùng và tổ chức, quản lý nhóm, và kiểm soát truy cập

**Sử dụng thực tế**: "Tạo pull request từ nhánh tính năng của tôi", "Hiển thị tất cả các lần chạy CI thất bại trong tuần này", "Liệt kê cảnh báo bảo mật mở cho các kho chứa của tôi", hoặc "Tìm tất cả issue được giao cho tôi trong các tổ chức của tôi"

**Kịch bản demo đầy đủ**: Dưới đây là quy trình trình diễn mạnh mẽ thể hiện khả năng của GitHub MCP Server:

> "Tôi cần chuẩn bị cho buổi review sprint. Hiển thị tất cả pull request tôi đã tạo trong tuần này, kiểm tra trạng thái pipeline CI/CD của chúng ta, tạo tóm tắt các cảnh báo bảo mật cần xử lý, và giúp tôi soạn ghi chú phát hành dựa trên các PR đã hợp nhất với nhãn 'feature'."

GitHub MCP Server sẽ:
- Truy vấn pull request gần đây của bạn với thông tin trạng thái chi tiết
- Phân tích các lần chạy workflow và làm nổi bật bất kỳ lỗi hoặc vấn đề hiệu năng
- Tổng hợp kết quả quét bảo mật và ưu tiên cảnh báo quan trọng
- Tạo ghi chú phát hành toàn diện bằng cách trích xuất thông tin từ các PR đã hợp nhất
- Cung cấp các bước tiếp theo có thể hành động cho việc lập kế hoạch sprint và chuẩn bị phát hành

**Ví dụ nổi bật**: Tôi thích dùng cái này cho quy trình đánh giá mã. Thay vì nhảy giữa VS Code, thông báo GitHub và trang pull request, tôi có thể nói "Hiển thị tất cả PR đang chờ tôi đánh giá" rồi nói tiếp "Thêm bình luận vào PR #123 hỏi về xử lý lỗi trong phương thức xác thực." Máy chủ sẽ xử lý API GitHub, giữ ngữ cảnh cuộc thảo luận, và thậm chí giúp tôi tạo bình luận đánh giá hiệu quả hơn.

**Tùy chọn xác thực**: Máy chủ hỗ trợ cả OAuth (liền mạch trong VS Code) và Personal Access Tokens, với bộ công cụ cấu hình để kích hoạt chỉ chức năng GitHub bạn cần. Bạn có thể chạy nó như dịch vụ host từ xa để thiết lập nhanh hoặc chạy cục bộ qua Docker để kiểm soát hoàn toàn.

> **💡 Mẹo chuyên nghiệp**
> 
> Chỉ kích hoạt các bộ công cụ bạn cần bằng cách cấu hình tham số `--toolsets` trong cài đặt MCP server của bạn để giảm kích thước ngữ cảnh và cải thiện lựa chọn công cụ AI. Ví dụ, thêm `"--toolsets", "repos,issues,pull_requests,actions"` vào các args cấu hình MCP cho các quy trình phát triển cốt lõi, hoặc dùng `"--toolsets", "notifications, security"` nếu bạn chủ yếu muốn khả năng giám sát GitHub.
### 4. 🔄 Azure DevOps MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Nó làm gì**: Kết nối với dịch vụ Azure DevOps cho quản lý dự án toàn diện, theo dõi work item, quản lý pipeline xây dựng, và thao tác kho chứa.

**Tại sao nó hữu ích**: Đối với các nhóm sử dụng Azure DevOps làm nền tảng DevOps chính, MCP server này loại bỏ việc chuyển đổi liên tục giữa môi trường phát triển và giao diện web Azure DevOps. Bạn có thể quản lý work item, kiểm tra trạng thái build, truy vấn kho chứa và xử lý các nhiệm vụ quản lý dự án trực tiếp từ trợ lý AI.

**Sử dụng thực tế**: "Hiển thị tất cả work item đang hoạt động trong sprint hiện tại của dự án WebApp", "Tạo báo cáo lỗi cho vấn đề đăng nhập tôi vừa phát hiện", hoặc "Kiểm tra trạng thái pipeline build của chúng ta và hiển thị các lần thất bại gần đây"

**Ví dụ nổi bật**: Bạn có thể dễ dàng kiểm tra trạng thái sprint hiện tại của nhóm bạn với truy vấn đơn giản như "Hiển thị tất cả work item đang hoạt động trong sprint hiện tại của dự án WebApp" hoặc "Tạo báo cáo lỗi cho vấn đề đăng nhập tôi vừa phát hiện" mà không rời môi trường phát triển.

### 5. 📝 MarkItDown MCP Server


[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Nó làm gì**: MarkItDown là một máy chủ chuyển đổi tài liệu toàn diện, biến đổi nhiều định dạng tập tin khác nhau thành Markdown chất lượng cao, tối ưu hóa cho việc sử dụng LLM và các luồng công việc phân tích văn bản.

**Tại sao nó hữu ích**: Thiết yếu cho các luồng công việc tài liệu hiện đại! MarkItDown xử lý đa dạng các định dạng tập tin trong khi vẫn giữ nguyên cấu trúc tài liệu quan trọng như tiêu đề, danh sách, bảng và liên kết. Khác với các công cụ trích xuất văn bản đơn giản, nó tập trung duy trì ý nghĩa ngữ nghĩa và định dạng có giá trị cho cả xử lý AI và khả năng đọc của con người.

**Các định dạng tập tin được hỗ trợ**:
- **Tài liệu Office**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Tập tin phương tiện**: Hình ảnh (có siêu dữ liệu EXIF và OCR), Âm thanh (có siêu dữ liệu EXIF và phiên âm giọng nói)
- **Nội dung Web**: HTML, nguồn cấp RSS, URL YouTube, trang Wikipedia
- **Định dạng dữ liệu**: CSV, JSON, XML, tập tin ZIP (xử lý đệ quy nội dung)
- **Định dạng xuất bản**: EPub, notebook Jupyter (.ipynb)
- **Email**: tin nhắn Outlook (.msg)
- **Nâng cao**: tích hợp Azure Document Intelligence để xử lý PDF nâng cao

**Khả năng nâng cao**: MarkItDown hỗ trợ mô tả hình ảnh sử dụng LLM (khi cung cấp client OpenAI), Azure Document Intelligence cho xử lý PDF nâng cao, phiên âm âm thanh cho nội dung giọng nói, và hệ thống plugin để mở rộng sang nhiều định dạng tập tin hơn.

**Sử dụng thực tế**: "Chuyển đổi bài thuyết trình PowerPoint này thành Markdown cho trang tài liệu của chúng tôi", "Trích xuất văn bản từ PDF này với cấu trúc tiêu đề phù hợp", hoặc "Chuyển đổi bảng tính Excel này thành định dạng bảng dễ đọc"

**Ví dụ nổi bật**: Trích dẫn từ [tài liệu MarkItDown](https://github.com/microsoft/markitdown#why-markdown):

> Markdown rất gần với văn bản thuần, với ký hiệu hoặc định dạng tối giản, nhưng vẫn cung cấp cách thể hiện cấu trúc tài liệu quan trọng. Các LLM phổ biến, như GPT-4o của OpenAI, bản địa "nói" Markdown, và thường tích hợp Markdown vào phản hồi của mình một cách tự nhiên. Điều này cho thấy chúng đã được huấn luyện trên lượng lớn văn bản định dạng Markdown, và hiểu nó rất tốt. Thêm vào đó, quy ước Markdown còn rất tiết kiệm token.

MarkItDown rất giỏi trong việc giữ nguyên cấu trúc tài liệu, điều quan trọng với các luồng công việc AI. Ví dụ, khi chuyển đổi một bài thuyết trình PowerPoint, nó giữ nguyên tổ chức các slide với tiêu đề đúng, trích xuất bảng dưới dạng bảng Markdown, bao gồm văn bản alt cho hình ảnh và thậm chí xử lý ghi chú người trình bày. Biểu đồ được chuyển thành bảng dữ liệu dễ đọc, và Markdown kết quả giữ được luồng logic của bài thuyết trình gốc. Điều này làm cho nó hoàn hảo để đưa nội dung trình bày vào hệ thống AI hoặc tạo tài liệu từ các slide đã có.
### 6. 🗃️ SQL Server MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Nó làm gì**: Cung cấp truy cập đàm thoại tới cơ sở dữ liệu SQL Server (tại chỗ, Azure SQL hoặc Fabric)

**Tại sao nó hữu ích**: Tương tự như máy chủ PostgreSQL nhưng dành cho hệ sinh thái Microsoft SQL. Kết nối bằng chuỗi kết nối đơn giản và bắt đầu truy vấn bằng ngôn ngữ tự nhiên – không cần đổi ngữ cảnh nữa!

**Sử dụng thực tế**: “Tìm tất cả đơn hàng chưa được thực hiện trong 30 ngày qua” được chuyển thành truy vấn SQL phù hợp và trả về kết quả đã định dạng

**Ví dụ nổi bật**: Khi bạn thiết lập kết nối cơ sở dữ liệu, bạn có thể bắt đầu trò chuyện với dữ liệu ngay lập tức. Bài blog giới thiệu điều này với câu hỏi đơn giản: “bạn đang kết nối với cơ sở dữ liệu nào?” Máy chủ MCP phản hồi bằng cách gọi công cụ cơ sở dữ liệu tương ứng, kết nối tới phiên bản SQL Server của bạn, và trả về thông tin về kết nối cơ sở dữ liệu hiện tại – tất cả mà không cần viết một dòng SQL nào. Máy chủ hỗ trợ đầy đủ các thao tác cơ sở dữ liệu từ quản lý lược đồ đến thao tác dữ liệu, tất cả qua các câu lệnh ngôn ngữ tự nhiên. Để biết hướng dẫn cài đặt đầy đủ và ví dụ cấu hình với VS Code và Claude Desktop, xem: [Giới thiệu MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Nó làm gì**: Cho phép các tác nhân AI tương tác với trang web để kiểm thử và tự động hóa

> **ℹ️ Cung cấp sức mạnh cho GitHub Copilot**
> 
> Máy chủ Playwright MCP cung cấp sức mạnh cho Đặc vụ Lập trình của GitHub Copilot, đem đến khả năng duyệt web! [Tìm hiểu thêm về tính năng này](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Tại sao nó hữu ích**: Hoàn hảo cho kiểm thử tự động dựa trên mô tả ngôn ngữ tự nhiên. AI có thể điều hướng website, điền mẫu, và trích xuất dữ liệu thông qua các ảnh chụp truy cập có cấu trúc – đây là thứ cực kỳ mạnh mẽ!

**Sử dụng thực tế**: "Kiểm thử luồng đăng nhập và xác minh bảng điều khiển tải đúng" hoặc "Tạo bài kiểm thử tìm sản phẩm và xác nhận trang kết quả" – tất cả mà không cần mã nguồn ứng dụng

**Ví dụ nổi bật**: Đồng nghiệp tôi là Debbie O'Brien gần đây đã làm việc rất xuất sắc với máy chủ Playwright MCP! Ví dụ, cô ấy mới đây cho thấy bạn có thể tạo các bài kiểm thử Playwright hoàn chỉnh mà không cần truy cập mã nguồn ứng dụng. Trong trường hợp của cô, cô yêu cầu Copilot tạo một bài kiểm thử cho ứng dụng tìm kiếm phim: điều hướng đến trang, tìm "Garfield", và xác minh phim xuất hiện trong kết quả. MCP đã khởi động phiên trình duyệt, khám phá cấu trúc trang qua ảnh chụp DOM, tìm bộ chọn chính xác, và tạo một bài kiểm thử TypeScript đầy đủ hoạt động ngay lần chạy đầu tiên.

Điều làm cho điều này thực sự mạnh mẽ là nó kết nối khoảng cách giữa hướng dẫn bằng ngôn ngữ tự nhiên và mã kiểm thử có thể thi hành. Phương pháp truyền thống yêu cầu hoặc viết kiểm thử thủ công hoặc truy cập code để có ngữ cảnh. Nhưng với Playwright MCP, bạn có thể kiểm thử trang bên ngoài, ứng dụng khách, hoặc làm kiểm thử hộp đen khi không có quyền truy cập mã.


### 8. 💻 Dev Box MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Nó làm gì**: Quản lý môi trường Microsoft Dev Box qua ngôn ngữ tự nhiên

**Tại sao nó hữu ích**: Đơn giản hóa rất nhiều việc quản lý môi trường phát triển! Tạo, cấu hình và quản lý môi trường phát triển mà không cần nhớ các lệnh cụ thể.

**Sử dụng thực tế**: "Thiết lập một Dev Box mới với bộ SDK .NET mới nhất và cấu hình cho dự án của chúng tôi", "Kiểm tra trạng thái tất cả môi trường phát triển của tôi", hoặc "Tạo môi trường demo chuẩn hóa cho các buổi thuyết trình nhóm"

**Ví dụ nổi bật**: Tôi là người rất thích dùng Dev Box cho phát triển cá nhân. Khoảnh khắc khai sáng của tôi là khi James Montemagno giải thích Dev Box tuyệt vời thế nào cho các buổi demo hội nghị, vì nó có kết nối ethernet siêu nhanh bất kể wifi hội nghị / khách sạn / máy bay mà tôi đang dùng. Thực tế, gần đây tôi đã luyện tập demo hội nghị khi laptop tôi kết nối qua điểm truy cập điện thoại khi đi xe buýt từ Bruges đến Antwerp! Nhưng bước tiếp theo của tôi là nghiên cứu kỹ hơn quản lý nhiều môi trường phát triển cho nhóm và môi trường demo chuẩn hóa. Một trường hợp sử dụng lớn nữa mà tôi nghe từ khách hàng và đồng nghiệp, tất nhiên, là dùng Dev Box cho môi trường phát triển được cấu hình sẵn. Trong cả hai trường hợp, dùng MCP để cấu hình và quản lý Dev Box cho phép bạn tương tác bằng ngôn ngữ tự nhiên, tất cả trong môi trường phát triển của bạn.

### 9. 🤖 Microsoft Foundry MCP Server


[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Nó làm gì**: Máy chủ Microsoft Foundry MCP cung cấp cho các nhà phát triển quyền truy cập toàn diện vào hệ sinh thái AI của Azure, bao gồm danh mục mô hình, quản lý triển khai, lập chỉ mục kiến thức với Azure AI Search, và các công cụ đánh giá. Máy chủ thử nghiệm này kết nối khoảng cách giữa phát triển AI và hạ tầng AI mạnh mẽ của Azure, giúp việc xây dựng, triển khai và đánh giá các ứng dụng AI trở nên dễ dàng hơn.

**Tại sao nó hữu ích**: Máy chủ này thay đổi cách bạn làm việc với các dịch vụ AI của Azure bằng cách mang các khả năng AI cấp doanh nghiệp trực tiếp vào quy trình phát triển của bạn. Thay vì phải chuyển đổi giữa cổng Azure, tài liệu và môi trường phát triển tích hợp (IDE), bạn có thể khám phá mô hình, triển khai dịch vụ, quản lý cơ sở kiến thức và đánh giá hiệu suất AI qua các lệnh ngôn ngữ tự nhiên. Nó đặc biệt mạnh mẽ cho các nhà phát triển xây dựng ứng dụng RAG (Retrieval-Augmented Generation), quản lý triển khai đa mô hình hoặc thực hiện các quy trình đánh giá AI toàn diện.

**Các khả năng chính dành cho nhà phát triển**:
- **🔍 Khám phá & Triển khai Mô hình**: Khám phá danh mục mô hình của Microsoft Foundry, nhận thông tin chi tiết về mô hình kèm mẫu mã, và triển khai mô hình tới các dịch vụ AI của Azure
- **📚 Quản lý Kiến thức**: Tạo và quản lý các chỉ mục Azure AI Search, thêm tài liệu, cấu hình bộ lập chỉ mục, và xây dựng các hệ thống RAG phức tạp
- **⚡ Tích hợp Đại lý AI**: Kết nối với các Đại lý AI Azure, truy vấn các đại lý hiện có, và đánh giá hiệu suất đại lý trong các kịch bản sản xuất
- **📊 Khung Đánh giá**: Thực hiện đánh giá toàn diện về văn bản và đại lý, tạo báo cáo markdown, và triển khai đảm bảo chất lượng cho các ứng dụng AI
- **🚀 Công cụ Phác thảo**: Nhận hướng dẫn thiết lập để tạo mẫu trên nền tảng GitHub và truy cập Microsoft Foundry Labs cho các mô hình nghiên cứu tiên tiến

**Sử dụng thực tiễn của nhà phát triển**: "Triển khai một mô hình Phi-4 lên các dịch vụ AI của Azure cho ứng dụng của tôi", "Tạo một chỉ mục tìm kiếm mới cho hệ thống RAG tài liệu của tôi", "Đánh giá phản hồi của đại lý dựa trên các chỉ số chất lượng", hoặc "Tìm mô hình lý luận tốt nhất cho các tác vụ phân tích phức tạp của tôi"

**Kịch bản demo đầy đủ**: Đây là một quy trình phát triển AI mạnh mẽ:

> "Tôi đang xây dựng một đại lý hỗ trợ khách hàng. Giúp tôi tìm một mô hình lý luận tốt trong danh mục, triển khai nó tới các dịch vụ AI của Azure, tạo cơ sở kiến thức từ tài liệu của chúng tôi, thiết lập khung đánh giá để kiểm tra chất lượng phản hồi, rồi giúp tôi phác thảo tích hợp với token GitHub để thử nghiệm."

Máy chủ Microsoft Foundry MCP sẽ:
- Truy vấn danh mục mô hình để đề xuất các mô hình lý luận tối ưu dựa trên yêu cầu của bạn
- Cung cấp lệnh triển khai và thông tin hạn mức cho vùng Azure bạn ưu tiên
- Thiết lập các chỉ mục Azure AI Search với sơ đồ chính xác cho tài liệu của bạn
- Cấu hình các quy trình đánh giá với các chỉ số chất lượng và kiểm tra an toàn
- Tạo mã phác thảo với xác thực GitHub để thử nghiệm ngay lập tức
- Cung cấp hướng dẫn thiết lập toàn diện phù hợp với ngăn xếp công nghệ cụ thể của bạn

**Ví dụ nổi bật**: Là một nhà phát triển, tôi đã gặp khó khăn trong việc bắt kịp các mô hình LLM khác nhau hiện có. Tôi biết vài mô hình chính, nhưng cảm thấy như đang bỏ lỡ một số cải tiến về năng suất và hiệu quả. Và việc quản lý token cùng hạn mức làm tôi căng thẳng – tôi không bao giờ biết liệu mình có chọn đúng mô hình cho nhiệm vụ đúng không hay đang tiêu phí ngân sách không hiệu quả. Tôi vừa nghe về MCP Server này từ James Montemagno khi tìm hiểu với đồng đội về các đề xuất MCP Server cho bài viết này, và tôi rất hào hứng sử dụng nó! Khả năng khám phá mô hình dường như rất ấn tượng với người như tôi, muốn khám phá ngoài số mô hình thường gặp và tìm các mô hình được tối ưu cho các tác vụ cụ thể. Khung đánh giá sẽ giúp tôi xác nhận rằng mình thực sự đang có kết quả tốt hơn, không chỉ là thử thứ gì đó mới cho có.

> **ℹ️ Tình trạng thử nghiệm**
> 
> Máy chủ MCP này đang trong giai đoạn thử nghiệm và phát triển tích cực. Các tính năng và API có thể thay đổi. Phù hợp để khám phá các khả năng AI của Azure và xây dựng nguyên mẫu, nhưng cần xác thực yêu cầu về độ ổn định cho môi trường sản xuất.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Nó làm gì**: Cung cấp các công cụ thiết yếu cho nhà phát triển để xây dựng đại lý AI và ứng dụng tích hợp với Microsoft 365 và Microsoft 365 Copilot, bao gồm xác thực sơ đồ, truy xuất mã mẫu, và hỗ trợ khắc phục sự cố.

**Tại sao nó hữu ích**: Phát triển cho Microsoft 365 và Copilot liên quan đến các sơ đồ manifest phức tạp và các mẫu phát triển đặc thù. Máy chủ MCP này mang tài nguyên phát triển thiết yếu trực tiếp vào môi trường mã hóa của bạn, giúp bạn xác thực sơ đồ, tìm mã mẫu và khắc phục lỗi phổ biến mà không phải liên tục tham khảo tài liệu.

**Sử dụng thực tế**: "Xác thực manifest đại lý khai báo của tôi và sửa bất kỳ lỗi sơ đồ nào", "Hiển thị mẫu mã cho plugin Microsoft Graph API", hoặc "Giúp tôi khắc phục sự cố xác thực ứng dụng Teams"

**Ví dụ nổi bật**: Tôi đã liên hệ với bạn tôi John Miller sau khi trò chuyện với anh ấy tại Build về M365 Agents, và anh ấy đề nghị MCP này. Đây có thể rất hữu ích cho các nhà phát triển mới với M365 Agents vì nó cung cấp các mẫu, mã mẫu và khung để bắt đầu mà không bị ngập trong tài liệu. Các tính năng xác thực sơ đồ có vẻ đặc biệt hữu ích để tránh lỗi cấu trúc manifest có thể gây ra hàng giờ sửa lỗi.

> **💡 Mẹo chuyên nghiệp**
> 
> Sử dụng máy chủ này cùng với Microsoft Learn Docs MCP Server để hỗ trợ phát triển M365 toàn diện – một bên cung cấp tài liệu chính thức trong khi máy chủ này cung cấp công cụ phát triển thực tế và hỗ trợ khắc phục sự cố.


## Tiếp theo là gì? 🔮

## 📋 Kết luận

Giao thức Ngữ cảnh Mô hình (MCP) đang biến đổi cách các nhà phát triển tương tác với trợ lý AI và công cụ bên ngoài. 10 máy chủ MCP của Microsoft này thể hiện sức mạnh của tích hợp AI chuẩn hóa, cho phép quy trình làm việc liền mạch giữ cho nhà phát triển tập trung trong luồng công việc khi truy cập các khả năng bên ngoài mạnh mẽ.

Từ tích hợp hệ sinh thái Azure toàn diện đến các công cụ chuyên biệt như Playwright cho tự động hóa trình duyệt và MarkItDown cho xử lý tài liệu, các máy chủ này trình bày cách MCP có thể nâng cao năng suất qua các kịch bản phát triển đa dạng. Giao thức chuẩn hóa đảm bảo các công cụ này hoạt động cùng nhau trơn tru, tạo ra trải nghiệm phát triển thống nhất.

Khi hệ sinh thái MCP tiếp tục phát triển, việc duy trì gắn kết với cộng đồng, khám phá các máy chủ mới và xây dựng giải pháp tùy chỉnh sẽ là chìa khóa để tối đa hóa năng suất phát triển của bạn. Tính chất chuẩn mở của MCP nghĩa là bạn có thể phối hợp các công cụ từ các nhà cung cấp khác nhau để tạo ra quy trình làm việc hoàn hảo cho nhu cầu cụ thể của mình.

## 🔗 Tài nguyên Bổ sung

- [Kho Microsoft MCP chính thức](https://github.com/microsoft/mcp)
- [Cộng đồng & Tài liệu MCP](https://modelcontextprotocol.io/introduction)
- [Tài liệu MCP cho VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Tài liệu MCP cho Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Tài liệu MCP cho Azure](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Học cùng nhau – Sự kiện MCP](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Tuyển tập tùy chỉnh GitHub Copilot xuất sắc](https://github.com/awesome-copilot)
- [Bộ phát triển phần mềm MCP cho C#](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days trực tiếp ngày 29/30 tháng 7 hoặc xem theo yêu cầu](https://aka.ms/mcpdevdays)

## 🎯 Bài tập

1. **Cài đặt và Cấu hình**: Thiết lập một trong các máy chủ MCP trong môi trường VS Code của bạn và thử nghiệm chức năng cơ bản.
2. **Tích hợp Quy trình làm việc**: Thiết kế một quy trình phát triển kết hợp ít nhất ba máy chủ MCP khác nhau.
3. **Lập kế hoạch Máy chủ Tùy chỉnh**: Xác định một nhiệm vụ trong thói quen phát triển hàng ngày của bạn có thể hưởng lợi từ một máy chủ MCP tùy chỉnh và tạo một đặc tả cho nó.
4. **Phân tích Hiệu suất**: So sánh hiệu quả sử dụng máy chủ MCP so với các phương pháp truyền thống cho các nhiệm vụ phát triển phổ biến.
5. **Đánh giá An ninh**: Đánh giá các tác động về bảo mật khi sử dụng máy chủ MCP trong môi trường phát triển của bạn và đề xuất các thực hành tốt nhất.


Tiếp theo: [Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->