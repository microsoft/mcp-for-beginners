# 🚀 10 Máy chủ Microsoft MCP Đang Thay Đổi Năng Suất Phát Triển Phần Mềm

## 🎯 Những Gì Bạn Sẽ Học Trong Hướng Dẫn Này

Hướng dẫn thực tiễn này giới thiệu mười máy chủ Microsoft MCP đang tích cực thay đổi cách các nhà phát triển làm việc với trợ lý AI. Thay vì chỉ giải thích những gì máy chủ MCP *có thể* làm, chúng tôi sẽ cho bạn thấy những máy chủ đã tạo ra sự khác biệt thực sự trong quy trình phát triển hàng ngày tại Microsoft và hơn thế nữa.

Mỗi máy chủ trong hướng dẫn này được chọn dựa trên việc sử dụng thực tế và phản hồi từ nhà phát triển. Bạn sẽ khám phá không chỉ những gì mỗi máy chủ làm, mà còn vì sao nó quan trọng và cách tận dụng tối đa trong các dự án của bạn. Cho dù bạn hoàn toàn mới với MCP hay muốn mở rộng thiết lập hiện tại, các máy chủ này đại diện cho một số công cụ thực tiễn và có tác động mạnh mẽ nhất trong hệ sinh thái Microsoft.

> **💡 Mẹo Bắt Đầu Nhanh**
> 
> Mới với MCP? Đừng lo! Hướng dẫn này được thiết kế thân thiện cho người mới bắt đầu. Chúng tôi sẽ giải thích khái niệm khi đi, và bạn luôn có thể tham khảo lại các mô-đun [Giới thiệu về MCP](../00-Introduction/README.md) và [Các Khái Niệm Cốt Lõi](../01-CoreConcepts/README.md) để có nền tảng sâu hơn.

## Tổng Quan

Hướng dẫn toàn diện này khám phá mười máy chủ Microsoft MCP đang cách mạng hóa cách các nhà phát triển tương tác với trợ lý AI và các công cụ bên ngoài. Từ quản lý tài nguyên Azure đến xử lý tài liệu, những máy chủ này cho thấy sức mạnh của Giao thức Ngữ cảnh Mô hình trong việc tạo ra các quy trình phát triển liền mạch và hiệu quả.

## Mục Tiêu Học Tập

Đến cuối hướng dẫn này, bạn sẽ:
- Hiểu cách các máy chủ MCP nâng cao năng suất nhà phát triển
- Tìm hiểu về những triển khai máy chủ MCP tác động nhất của Microsoft
- Khám phá các kịch bản sử dụng thực tiễn cho mỗi máy chủ
- Biết cách thiết lập và cấu hình các máy chủ này trong VS Code và Visual Studio
- Khám phá hệ sinh thái MCP rộng lớn hơn và các hướng đi tương lai

## 🔧 Hiểu Về Máy Chủ MCP: Hướng Dẫn Cho Người Mới Bắt Đầu

### Máy Chủ MCP Là Gì?

Là người mới với Giao thức Ngữ cảnh Mô hình (MCP), bạn có thể tự hỏi: "Máy chủ MCP chính xác là gì, và tại sao tôi nên quan tâm?" Hãy bắt đầu với một phép ẩn dụ đơn giản.

Hãy nghĩ về các máy chủ MCP như những trợ lý chuyên biệt giúp người bạn đồng hành AI viết code (như GitHub Copilot) kết nối với các công cụ và dịch vụ bên ngoài. Giống như bạn sử dụng các ứng dụng khác nhau trên điện thoại cho các tác vụ khác nhau—một ứng dụng cho thời tiết, một cho điều hướng, một cho ngân hàng—máy chủ MCP cho phép trợ lý AI giao tiếp với nhiều công cụ và dịch vụ phát triển khác nhau.

### Vấn Đề Máy Chủ MCP Giải Quyết

Trước máy chủ MCP, nếu bạn muốn:
- Kiểm tra tài nguyên Azure của bạn
- Tạo một issue trên GitHub
- Truy vấn cơ sở dữ liệu của bạn
- Tìm kiếm trong tài liệu

Bạn phải dừng lập trình, mở trình duyệt, truy cập vào trang web phù hợp và thực hiện thủ công các tác vụ này. Việc chuyển đổi ngữ cảnh liên tục này làm gián đoạn dòng làm việc của bạn và giảm năng suất.

### Cách Máy Chủ MCP Thay Đổi Trải Nghiệm Phát Triển Của Bạn

Với các máy chủ MCP, bạn có thể ở lại môi trường phát triển của mình (VS Code, Visual Studio, v.v.) và đơn giản yêu cầu trợ lý AI xử lý các việc này. Ví dụ:

**Thay vì quy trình truyền thống này:**
1. Dừng viết code
2. Mở trình duyệt
3. Truy cập cổng Azure
4. Tra cứu chi tiết tài khoản lưu trữ
5. Trở lại VS Code
6. Tiếp tục viết code

**Bây giờ bạn có thể làm điều này:**
1. Hỏi AI: "Tình trạng các tài khoản lưu trữ Azure của tôi thế nào?"
2. Tiếp tục viết code với thông tin được cung cấp

### Lợi Ích Chính Cho Người Mới Bắt Đầu

#### 1. 🔄 **Giữ Ở Trạng Thái Tập Trung**
- Không phải chuyển đổi giữa nhiều ứng dụng
- Giữ sự tập trung vào mã bạn đang viết
- Giảm gánh nặng tư duy khi quản lý nhiều công cụ khác nhau

#### 2. 🤖 **Sử Dụng Ngôn Ngữ Tự Nhiên Thay Vì Lệnh Phức Tạp**
- Thay vì ghi nhớ cú pháp SQL, hãy mô tả dữ liệu bạn cần
- Thay vì nhớ các lệnh Azure CLI, hãy giải thích bạn muốn hoàn thành gì
- Để AI xử lý các chi tiết kỹ thuật trong khi bạn tập trung vào logic

#### 3. 🔗 **Kết Nối Nhiều Công Cụ Với Nhau**
- Tạo quy trình làm việc mạnh mẽ bằng cách kết hợp các dịch vụ khác nhau
- Ví dụ: "Lấy tất cả các issue GitHub gần đây và tạo các work item tương ứng trong Azure DevOps"
- Xây dựng tự động hoá mà không cần viết script phức tạp

#### 4. 🌐 **Truy Cập Hệ Sinh Thái Đang Phát Triển**
- Hưởng lợi từ các máy chủ do Microsoft, GitHub, và các công ty khác xây dựng
- Kết hợp và phối hợp các công cụ từ các nhà cung cấp khác nhau một cách liền mạch
- Tham gia hệ sinh thái chuẩn hóa hoạt động trên nhiều trợ lý AI khác nhau

#### 5. 🛠️ **Học Qua Thực Hành**
- Bắt đầu với các máy chủ có sẵn để hiểu các khái niệm
- Dần dần xây dựng máy chủ riêng khi bạn quen tay hơn
- Sử dụng SDK và tài liệu sẵn có để hướng dẫn quá trình học

### Ví Dụ Thực Tế Cho Người Mới Bắt Đầu

Giả sử bạn mới bắt đầu phát triển web và đang làm dự án đầu tiên. Đây là cách các máy chủ MCP có thể giúp bạn:

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

### Lợi Thế Chuẩn Mực Doanh Nghiệp

MCP đang trở thành chuẩn mực toàn ngành, điều đó có nghĩa:
- **Tính nhất quán**: Trải nghiệm tương tự qua nhiều công cụ và công ty khác nhau
- **Tính tương tác**: Máy chủ từ các nhà cung cấp khác nhau có thể làm việc cùng nhau
- **Bảo đảm tương lai**: Kỹ năng và thiết lập chuyển giao giữa nhiều trợ lý AI khác nhau
- **Cộng đồng**: Hệ sinh thái lớn với kiến thức và nguồn lực chia sẻ

### Bắt Đầu: Những Gì Bạn Sẽ Học

Trong hướng dẫn này, chúng ta sẽ khám phá 10 máy chủ Microsoft MCP cực kỳ hữu ích cho các nhà phát triển ở mọi trình độ. Mỗi máy chủ được thiết kế để:
- Giải quyết các thách thức phổ biến khi phát triển
- Giảm những công việc lặp đi lặp lại
- Cải thiện chất lượng mã
- Tăng cơ hội học tập

> **💡 Mẹo Học Tập**
> 
> Nếu bạn hoàn toàn mới với MCP, hãy bắt đầu với các mô-đun [Giới thiệu về MCP](../00-Introduction/README.md) và [Các Khái Niệm Cốt Lõi](../01-CoreConcepts/README.md) trước. Sau đó quay lại đây để xem các khái niệm đó áp dụng ra sao với các công cụ thực tế của Microsoft.
>
> Để có thêm bối cảnh về tầm quan trọng của MCP, hãy xem bài viết của Maria Naggaga: [Kết Nối Một Lần, Tích Hợp Ở Mọi Nơi với MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Bắt Đầu Với MCP Trong VS Code và Visual Studio 🚀

Việc thiết lập các máy chủ MCP này rất đơn giản nếu bạn sử dụng Visual Studio Code hoặc Visual Studio 2022 với GitHub Copilot.

### Thiết Lập VS Code

Đây là quy trình cơ bản cho VS Code:

1. **Bật Chế Độ Agent**: Trong VS Code, chuyển sang chế độ Agent trong cửa sổ Copilot Chat
2. **Cấu Hình Máy Chủ MCP**: Thêm cấu hình máy chủ vào file settings.json của VS Code
3. **Khởi Động Máy Chủ**: Nhấn nút "Start" cho mỗi máy chủ bạn muốn sử dụng
4. **Chọn Công Cụ**: Chọn máy chủ MCP nào để bật trong phiên làm việc hiện tại

Để biết hướng dẫn chi tiết, xem tài liệu [MCP VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Mẹo Chuyên Nghiệp: Quản lý máy chủ MCP như dân chuyên!**
> 
> Giao diện Extensions của VS Code nay có [giao diện mới tiện dụng để quản lý các máy chủ MCP đã cài](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Bạn sẽ có quyền truy cập nhanh để khởi động, dừng, và quản lý mọi máy chủ MCP đã cài với giao diện rõ ràng và đơn giản. Hãy thử ngay!

### Thiết Lập Visual Studio 2022

Với Visual Studio 2022 (phiên bản 17.14 trở lên):

1. **Bật Chế Độ Agent**: Nhấn dropdown "Ask" trong cửa sổ GitHub Copilot Chat và chọn "Agent"
2. **Tạo File Cấu Hình**: Tạo file `.mcp.json` trong thư mục giải pháp của bạn (vị trí đề xuất: `<SOLUTIONDIR>\.mcp.json`)
3. **Cấu Hình Máy Chủ**: Thêm cấu hình máy chủ MCP theo định dạng MCP chuẩn
4. **Phê Duyệt Công Cụ**: Khi được yêu cầu, phê duyệt các công cụ bạn muốn dùng với quyền truy cập phù hợp

Để xem hướng dẫn chi tiết cho Visual Studio, xem tài liệu [MCP Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Mỗi máy chủ MCP có yêu cầu cấu hình riêng (chuỗi kết nối, xác thực, v.v.), nhưng mẫu thiết lập nhất quán trên cả hai IDE.

## Bài Học Rút Ra Từ Máy Chủ Microsoft MCP 🛠️

### 1. 📚 Máy Chủ MCP Microsoft Learn Docs

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Nó làm gì**: Máy Chủ MCP Microsoft Learn Docs là dịch vụ được lưu trữ trên đám mây cung cấp trợ lý AI truy cập theo thời gian thực đến tài liệu chính thức của Microsoft qua Giao thức Ngữ cảnh Mô hình. Nó kết nối với `https://learn.microsoft.com/api/mcp` và cho phép tìm kiếm ngữ nghĩa trên Microsoft Learn, tài liệu Azure, tài liệu Microsoft 365 và các nguồn chính thức khác của Microsoft.

**Tại sao nó hữu ích**: Mặc dù có vẻ chỉ là "tài liệu," máy chủ này thực sự quan trọng đối với mỗi nhà phát triển sử dụng công nghệ Microsoft. Một trong những phàn nàn lớn nhất của các nhà phát triển .NET về trợ lý viết code AI là chúng không cập nhật các phiên bản .NET và C# mới nhất. Máy Chủ MCP Microsoft Learn Docs giải quyết điều này bằng cách cung cấp truy cập theo thời gian thực đến tài liệu mới nhất, tài liệu API và các thực tiễn tốt nhất. Dù bạn đang làm việc với SDK Azure mới nhất, khám phá các tính năng C# 13 mới, hay triển khai các mẫu Aspire tiên tiến, máy chủ này đảm bảo trợ lý AI của bạn có thông tin chính xác, cập nhật để tạo mã hiện đại và đúng.

**Sử dụng thực tế**: "Các lệnh az cli để tạo ứng dụng container Azure theo tài liệu chính thức Microsoft Learn là gì?" hoặc "Làm sao tôi cấu hình Entity Framework với dependency injection trong ASP.NET Core?" Hay "Xem xét đoạn mã này để đảm bảo nó phù hợp với các khuyến nghị về hiệu năng trong tài liệu Microsoft Learn." Máy chủ cung cấp phạm vi bao phủ toàn diện trên Microsoft Learn, tài liệu Azure, và Microsoft 365 dùng tìm kiếm ngữ nghĩa tiên tiến để tìm thông tin phù hợp nhất theo ngữ cảnh. Nó trả về tối đa 10 đoạn nội dung chất lượng cao kèm tiêu đề bài viết và URL, luôn truy cập tài liệu Microsoft mới nhất khi được xuất bản.

**Ví dụ nổi bật**: Máy chủ cung cấp công cụ `microsoft_docs_search` thực hiện tìm kiếm ngữ nghĩa trên tài liệu kỹ thuật chính thức của Microsoft. Khi cấu hình xong, bạn có thể hỏi "Làm thế nào để triển khai xác thực JWT trong ASP.NET Core?" và nhận được câu trả lời chi tiết, chính thức kèm link nguồn. Chất lượng tìm kiếm tuyệt vời vì nó hiểu ngữ cảnh – hỏi về "containers" trong bối cảnh Azure sẽ trả về tài liệu Azure Container Instances, trong khi cùng thuật ngữ trong bối cảnh .NET trả về thông tin về bộ sưu tập C# tương ứng.

Điều này đặc biệt hữu ích cho thư viện và trường hợp sử dụng thay đổi nhanh hoặc mới được cập nhật. Ví dụ, trong một số dự án mới đây tôi muốn tận dụng tính năng trong các bản phát hành mới nhất của Aspire và Microsoft.Extensions.AI. Bằng cách bổ sung Máy Chủ MCP Microsoft Learn Docs, tôi có thể tận dụng không chỉ tài liệu API mà còn các hướng dẫn và bài viết mới được phát hành.

> **💡 Mẹo Chuyên Nghiệp**
> 
> Ngay cả các mô hình thân thiện với công cụ cũng cần được khuyến khích sử dụng các công cụ MCP! Hãy xem xét thêm một prompt hệ thống hoặc [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) kiểu như: "Bạn có quyền truy cập `microsoft.docs.mcp` – hãy sử dụng công cụ này để tìm kiếm tài liệu chính thức mới nhất của Microsoft khi xử lý các câu hỏi về công nghệ Microsoft như C#, Azure, ASP.NET Core, hoặc Entity Framework."
>
> Để thấy ví dụ tuyệt vời về điều này trong thực tế, hãy xem chế độ chat [C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) từ kho Awesome GitHub Copilot. Chế độ này đặc biệt tận dụng Máy Chủ MCP Microsoft Learn Docs để giúp làm sạch và hiện đại hóa mã C# sử dụng các mẫu và thực tiễn tốt nhất mới nhất.
### 2. ☁️ Máy Chủ Azure MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Nó làm gì**: Máy Chủ Azure MCP là bộ đầy đủ hơn 15 bộ kết nối dịch vụ Azure chuyên biệt mang toàn bộ hệ sinh thái Azure vào quy trình làm việc AI của bạn. Đây không chỉ là một máy chủ đơn lẻ – mà là một tập hợp mạnh mẽ bao gồm quản lý tài nguyên, kết nối cơ sở dữ liệu (PostgreSQL, SQL Server), phân tích log Azure Monitor với KQL, tích hợp Cosmos DB, và còn nhiều hơn nữa.

**Tại sao nó hữu ích**: Ngoài việc quản lý tài nguyên Azure, máy chủ này cải thiện đáng kể chất lượng mã khi làm việc với SDK Azure. Khi bạn dùng Azure MCP ở chế độ Agent, nó không chỉ giúp bạn viết code – mà còn giúp bạn viết *mã Azure tốt hơn* theo những mẫu xác thực hiện hành, thực tiễn xử lý lỗi, và tận dụng các tính năng SDK mới nhất. Thay vì nhận mã chung chung có thể chạy được, bạn nhận mã theo chuẩn Azure đề xuất cho tải công việc sản xuất.

**Các mô-đun chính gồm**:
- **🗄️ Bộ Kết Nối Cơ Sở Dữ Liệu**: Truy cập ngôn ngữ tự nhiên trực tiếp đến Azure Database cho PostgreSQL và SQL Server
- **📊 Azure Monitor**: Phân tích log và thông tin vận hành dùng KQL
- **🌐 Quản Lý Tài Nguyên**: Quản lý vòng đời tài nguyên Azure đầy đủ
- **🔐 Xác Thực**: Các mẫu DefaultAzureCredential và danh tính được quản lý
- **📦 Dịch Vụ Lưu Trữ**: Thao tác Blob Storage, Queue Storage, và Table Storage
- **🚀 Dịch Vụ Container**: Quản lý Azure Container Apps, Container Instances, và AKS
- **Và nhiều bộ kết nối chuyên biệt khác**

**Sử dụng thực tế**: "Liệt kê các tài khoản lưu trữ Azure của tôi", "Truy vấn không gian làm việc Log Analytics để tìm lỗi giờ vừa qua", hoặc "Giúp tôi xây dựng ứng dụng Azure dùng Node.js với xác thực đúng chuẩn"

**Kịch bản demo đầy đủ**: Đây là hướng dẫn chi tiết cho thấy sức mạnh của việc kết hợp Azure MCP với tiện ích GitHub Copilot for Azure trong VS Code. Khi bạn có cả hai cài đặt và nhập lệnh:

> "Tạo một script Python tải lên một tệp tin lên Azure Blob Storage bằng cách sử dụng xác thực DefaultAzureCredential. Script cần kết nối đến tài khoản lưu trữ Azure của tôi có tên là 'mycompanystorage', tải lên một container có tên 'documents', tạo một tệp thử nghiệm với dấu thời gian hiện tại để tải lên, xử lý lỗi một cách nhẹ nhàng và cung cấp đầu ra thông tin, tuân thủ các thực hành tốt nhất của Azure cho xác thực và xử lý lỗi, bao gồm các chú thích giải thích cách hoạt động của xác thực DefaultAzureCredential, và làm cho script được cấu trúc tốt với các hàm và tài liệu phù hợp."

Máy chủ Azure MCP sẽ tạo ra một script Python hoàn chỉnh, sẵn sàng cho sản xuất, với các đặc điểm:
- Sử dụng SDK Azure Blob Storage mới nhất với các mẫu async thích hợp
- Triển khai DefaultAzureCredential với giải thích đầy đủ về chuỗi dự phòng
- Bao gồm xử lý lỗi mạnh mẽ với các loại ngoại lệ đặc thù của Azure
- Tuân thủ các thực hành tốt nhất của SDK Azure về quản lý tài nguyên và xử lý kết nối
- Cung cấp ghi nhận chi tiết và đầu ra thông tin ra console
- Tạo một script có cấu trúc đúng với hàm, tài liệu, và chú thích kiểu dữ liệu

Điều làm cho điều này đặc biệt là nếu không có Azure MCP, bạn có thể chỉ nhận được mã lưu trữ blob chung chung hoạt động nhưng không theo các mẫu Azure hiện tại. Với Azure MCP, bạn nhận mã tận dụng các phương pháp xác thực mới nhất, xử lý các tình huống lỗi đặc thù Azure, và theo các thực hành được Microsoft khuyến nghị cho các ứng dụng sản xuất.

**Ví dụ nổi bật**: Tôi đã từng khó khăn khi nhớ các lệnh cụ thể cho CLI `az` và `azd` để sử dụng tùy ý. Thường thì tôi phải làm hai bước: đầu tiên tìm cú pháp, sau đó chạy lệnh. Tôi thường vào portal và click một cách thủ công để hoàn thành công việc vì không muốn thừa nhận mình không nhớ cú pháp CLI. Có thể chỉ cần mô tả những gì tôi muốn làm thật tuyệt vời, và còn tuyệt hơn khi làm được việc đó mà không cần rời khỏi IDE!

Có một danh sách tuyệt vời các trường hợp sử dụng trong [kho Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) để bạn bắt đầu. Để xem các hướng dẫn thiết lập toàn diện và tùy chọn cấu hình nâng cao, hãy xem [tài liệu chính thức Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 Máy chủ GitHub MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Nó làm gì**: Máy chủ GitHub MCP chính thức cung cấp tích hợp liền mạch với toàn bộ hệ sinh thái GitHub, bao gồm cả truy cập từ xa được lưu trữ và tùy chọn triển khai Docker tại chỗ. Đây không chỉ là các thao tác cơ bản với kho mã – nó là một bộ công cụ toàn diện bao gồm quản lý GitHub Actions, quy trình làm việc pull request, theo dõi vấn đề, quét bảo mật, thông báo, và các khả năng tự động hóa nâng cao.

**Tại sao nó hữu ích**: Máy chủ này thay đổi cách bạn tương tác với GitHub bằng cách đưa toàn bộ trải nghiệm nền tảng trực tiếp vào môi trường phát triển của bạn. Thay vì liên tục chuyển đổi giữa VS Code và GitHub.com để quản lý dự án, xem xét mã, và giám sát CI/CD, bạn có thể xử lý tất cả qua các lệnh ngôn ngữ tự nhiên trong khi vẫn tập trung vào mã của mình.

> **ℹ️ Lưu ý: Các loại 'Agent' khác nhau**
> 
> Đừng nhầm lẫn máy chủ GitHub MCP này với Coding Agent của GitHub (agent AI mà bạn có thể giao vấn đề để thực hiện các tác vụ mã hóa tự động). Máy chủ GitHub MCP hoạt động trong chế độ Agent của VS Code để cung cấp tích hợp API GitHub, trong khi Coding Agent của GitHub là một tính năng riêng biệt tạo pull request khi được giao các vấn đề GitHub.

**Các khả năng chính bao gồm**:
- **⚙️ GitHub Actions**: Quản lý hoàn chỉnh pipeline CI/CD, giám sát workflow, và xử lý artifact
- **🔀 Pull Requests**: Tạo, xem xét, hợp nhất, và quản lý PR với theo dõi trạng thái toàn diện
- **🐛 Issues**: Quản lý vòng đời vấn đề đầy đủ, bình luận, gắn nhãn, và phân công
- **🔒 Bảo mật**: Cảnh báo quét mã, phát hiện bí mật, và tích hợp Dependabot
- **🔔 Thông báo**: Quản lý thông báo thông minh và kiểm soát đăng ký kho
- **📁 Quản lý kho mã**: Các thao tác tập tin, quản lý nhánh, và quản trị kho
- **👥 Hợp tác**: Tìm kiếm người dùng và tổ chức, quản lý đội nhóm, và kiểm soát truy cập

**Sử dụng thực tế**: "Tạo pull request từ nhánh tính năng của tôi", "Hiển thị tất cả các lần chạy CI thất bại trong tuần này", "Liệt kê các cảnh báo bảo mật mở cho các kho của tôi", hoặc "Tìm tất cả các vấn đề được giao cho tôi trong các tổ chức của tôi"

**Kịch bản demo đầy đủ**: Đây là một workflow mạnh mẽ minh họa các khả năng của máy chủ GitHub MCP:

> "Tôi cần chuẩn bị cho buổi xem xét sprint của chúng tôi. Hiển thị tất cả pull request tôi đã tạo trong tuần này, kiểm tra trạng thái các pipeline CI/CD, tạo tóm tắt các cảnh báo bảo mật cần xử lý, và giúp tôi soạn ghi chú phát hành dựa trên các PR đã được merge với nhãn 'feature'."

Máy chủ GitHub MCP sẽ:
- Truy vấn các pull request gần đây của bạn với thông tin trạng thái chi tiết
- Phân tích các lần chạy workflow và làm nổi bật các lỗi hoặc vấn đề hiệu suất
- Tổng hợp kết quả quét bảo mật và ưu tiên các cảnh báo nghiêm trọng
- Tạo ghi chú phát hành toàn diện bằng cách trích xuất thông tin từ các PR đã merge
- Cung cấp các bước hành động tiếp theo cho lập kế hoạch sprint và chuẩn bị phát hành

**Ví dụ nổi bật**: Tôi rất thích dùng cái này cho công việc review mã. Thay vì chuyển đổi qua lại giữa VS Code, thông báo GitHub, và trang pull request, tôi chỉ cần nói "Hiển thị tất cả PR đang chờ tôi review" rồi sau đó "Thêm bình luận vào PR #123 hỏi về cách xử lý lỗi trong phương thức xác thực." Máy chủ xử lý các cuộc gọi API GitHub, giữ ngữ cảnh thảo luận, và thậm chí giúp tôi soạn bình luận review xây dựng hơn.

**Tùy chọn xác thực**: Máy chủ hỗ trợ cả OAuth (liền mạch trong VS Code) và Personal Access Tokens, với bộ công cụ cấu hình cho phép chỉ bật các chức năng GitHub bạn cần. Bạn có thể chạy nó như một dịch vụ lưu trữ từ xa để thiết lập nhanh hoặc tại chỗ qua Docker để kiểm soát toàn diện.

> **💡 Mẹo chuyên nghiệp**
> 
> Chỉ bật các bộ công cụ bạn cần bằng cách cấu hình tham số `--toolsets` trong cài đặt máy chủ MCP để giảm kích thước ngữ cảnh và cải thiện chọn lựa công cụ AI. Ví dụ, thêm `"--toolsets", "repos,issues,pull_requests,actions"` vào tham số cấu hình MCP cho các workflow phát triển cốt lõi, hoặc dùng `"--toolsets", "notifications, security"` nếu bạn chủ yếu muốn khả năng giám sát GitHub.
### 4. 🔄 Máy chủ Azure DevOps MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Nó làm gì**: Kết nối với các dịch vụ Azure DevOps để quản lý dự án toàn diện, theo dõi công việc, quản lý pipeline xây dựng, và thao tác kho mã.

**Tại sao nó hữu ích**: Đối với các nhóm dùng Azure DevOps làm nền tảng DevOps chính, máy chủ MCP này loại bỏ việc chuyển đổi liên tục giữa môi trường phát triển và giao diện web Azure DevOps. Bạn có thể quản lý công việc, kiểm tra trạng thái xây dựng, truy vấn kho mã, và xử lý các tác vụ quản lý dự án trực tiếp từ trợ lý AI của mình.

**Sử dụng thực tế**: "Hiển thị tất cả các công việc đang hoạt động trong sprint hiện tại cho dự án WebApp", "Tạo báo cáo lỗi cho sự cố đăng nhập tôi vừa phát hiện", hoặc "Kiểm tra trạng thái các pipeline xây dựng và hiển thị bất kỳ lỗi gần đây nào"

**Ví dụ nổi bật**: Bạn có thể dễ dàng kiểm tra trạng thái sprint của nhóm mình bằng truy vấn đơn giản như "Hiển thị tất cả các công việc đang hoạt động trong sprint hiện tại cho dự án WebApp" hoặc "Tạo báo cáo lỗi cho sự cố đăng nhập tôi vừa phát hiện" mà không cần rời khỏi môi trường phát triển.

### 5. 📝 Máy chủ MarkItDown MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Nó làm gì**: MarkItDown là một máy chủ chuyển đổi tài liệu toàn diện biến đổi nhiều định dạng tệp thành Markdown chất lượng cao, tối ưu cho việc tiêu thụ bởi mô hình ngôn ngữ lớn (LLM) và các workflow phân tích văn bản.

**Tại sao nó hữu ích**: Thiết yếu cho các workflow tài liệu hiện đại! MarkItDown hỗ trợ một phạm vi ấn tượng các định dạng tệp trong khi vẫn giữ nguyên cấu trúc tài liệu quan trọng như tiêu đề, danh sách, bảng biểu, và liên kết. Không giống các công cụ trích xuất văn bản đơn giản, nó tập trung duy trì ý nghĩa ngữ nghĩa và định dạng có giá trị cho cả xử lý AI và dễ đọc của con người.

**Các định dạng tệp được hỗ trợ**:
- **Tài liệu Office**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Tệp phương tiện**: Hình ảnh (có metadata EXIF và nhận dạng OCR), Âm thanh (có metadata EXIF và chuyển văn bản giọng nói)
- **Nội dung web**: HTML, RSS feeds, URL YouTube, trang Wikipedia
- **Định dạng dữ liệu**: CSV, JSON, XML, tệp ZIP (xử lý nội dung đệ quy)
- **Định dạng xuất bản**: EPub, sổ ghi chép Jupyter (.ipynb)
- **Email**: Tin nhắn Outlook (.msg)
- **Nâng cao**: Tích hợp Azure Document Intelligence để xử lý PDF nâng cao

**Khả năng nâng cao**: MarkItDown hỗ trợ mô tả hình ảnh qua LLM (khi được cung cấp client OpenAI), Azure Document Intelligence cho xử lý PDF tốt hơn, chuyển văn bản thoại thành chữ, và hệ thống plugin để mở rộng thêm các định dạng tệp khác.

**Sử dụng thực tế**: "Chuyển bản trình bày PowerPoint này sang Markdown cho trang tài liệu của chúng tôi", "Trích xuất văn bản từ PDF này với cấu trúc tiêu đề đúng", hoặc "Biến bảng tính Excel này thành định dạng bảng dễ đọc"

**Ví dụ nổi bật (tóm tắt)**: Các
[tài liệu MarkItDown](https://github.com/microsoft/markitdown#why-markdown) giải thích
rằng Markdown giữ nguyên cấu trúc tài liệu với chi phí định dạng thấp.
Các mô hình ngôn ngữ thường sản xuất Markdown, làm cho nó trở thành định dạng hữu ích, tiết kiệm token
cho các workflow xử lý tài liệu.

MarkItDown thực sự tốt trong việc giữ cấu trúc tài liệu, điều quan trọng cho các workflow AI. Ví dụ, khi chuyển đổi bản trình bày PowerPoint, nó giữ tổ chức các slide với các tiêu đề phù hợp, trích xuất bảng dưới dạng bảng Markdown, bao gồm văn bản thay thế cho hình ảnh, và thậm chí xử lý ghi chú diễn giả. Biểu đồ được chuyển thành bảng dữ liệu dễ đọc, và Markdown kết quả giữ được luồng logic của bản trình bày gốc. Điều này làm cho nó hoàn hảo để đưa nội dung trình bày vào các hệ thống AI hoặc tạo tài liệu từ các slide có sẵn.
### 6. 🗃️ Máy chủ SQL Server MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Nó làm gì**: Cung cấp truy cập hội thoại đến cơ sở dữ liệu SQL Server (tại chỗ, Azure SQL, hoặc Fabric)

**Tại sao nó hữu ích**: Tương tự máy chủ PostgreSQL nhưng dành cho hệ sinh thái Microsoft SQL. Kết nối qua chuỗi kết nối đơn giản và bắt đầu truy vấn bằng ngôn ngữ tự nhiên – không còn phải chuyển đổi ngữ cảnh nữa!

**Sử dụng thực tế**: "Tìm tất cả đơn hàng chưa hoàn thành trong 30 ngày qua" được chuyển thành các truy vấn SQL phù hợp và trả về kết quả đã định dạng

**Ví dụ nổi bật**: Khi bạn thiết lập kết nối cơ sở dữ liệu, bạn có thể bắt đầu trò chuyện với dữ liệu ngay lập tức. Bài blog giới thiệu tính năng này với câu hỏi đơn giản: "Bạn đang kết nối với cơ sở dữ liệu nào?" Máy chủ MCP trả lời bằng cách gọi công cụ cơ sở dữ liệu phù hợp, kết nối tới phiên bản SQL Server của bạn, và trả về chi tiết kết nối cơ sở dữ liệu hiện tại – tất cả mà không phải viết một dòng SQL nào. Máy chủ hỗ trợ các thao tác cơ sở dữ liệu toàn diện từ quản lý schema đến thao tác dữ liệu, tất cả thông qua lời nhắc ngôn ngữ tự nhiên. Để có hướng dẫn thiết lập đầy đủ và ví dụ cấu hình với VS Code và Claude Desktop, xem: [Giới thiệu máy chủ MSSQL MCP (Phiên bản thử nghiệm)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Máy chủ Playwright MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Nó làm gì**: Cho phép các agent AI tương tác với các trang web để kiểm thử và tự động hóa

> **ℹ️ Cung cấp sức mạnh cho GitHub Copilot**
> 
> Máy chủ Playwright MCP cung cấp sức mạnh cho Coding Agent của GitHub Copilot, mang đến khả năng duyệt web! [Tìm hiểu thêm về tính năng này](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Tại sao nó hữu ích**: Hoàn hảo cho kiểm thử tự động được điều khiển bằng mô tả ngôn ngữ tự nhiên. AI có thể điều hướng website, điền biểu mẫu, và trích xuất dữ liệu qua các snapshot truy cập có cấu trúc – đây là công nghệ cực kỳ mạnh mẽ!

**Sử dụng thực tế**: "Kiểm thử luồng đăng nhập và xác minh rằng bảng điều khiển tải đúng" hoặc "Tạo một bài kiểm thử tìm kiếm sản phẩm và xác nhận trang kết quả" – tất cả đều không cần mã nguồn của ứng dụng

**Ví dụ nổi bật**: Đồng nghiệp của tôi, Debbie O'Brien, gần đây làm rất tốt với máy chủ Playwright MCP! Ví dụ, cô ấy mới đây đã trình diễn cách bạn có thể tạo các bài kiểm thử Playwright hoàn chỉnh ngay cả khi không có mã nguồn ứng dụng. Trong kịch bản của cô ấy, cô yêu cầu Copilot tạo một bài kiểm thử cho app tìm kiếm phim: điều hướng đến trang web, tìm "Garfield," và xác minh phim xuất hiện trong kết quả. MCP đã mở một phiên trình duyệt, khám phá cấu trúc trang qua các snapshot DOM, xác định bộ chọn đúng, và tạo ra bài kiểm thử TypeScript hoàn chỉnh chạy thành công ngay lần đầu.

Điều làm cho điều này thực sự mạnh mẽ là nó nối liền khoảng cách giữa các hướng dẫn ngôn ngữ tự nhiên và mã kiểm thử có thể thực thi được. Các phương pháp truyền thống yêu cầu hoặc là viết kiểm thử thủ công hoặc truy cập vào cơ sở mã để có ngữ cảnh. Nhưng với Playwright MCP, bạn có thể kiểm thử các trang web bên ngoài, ứng dụng khách, hoặc làm việc trong các kịch bản kiểm thử hộp đen nơi không có quyền truy cập mã nguồn.


### 8. 💻 Máy chủ Dev Box MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Công việc của nó**: Quản lý các môi trường Microsoft Dev Box thông qua ngôn ngữ tự nhiên

**Tại sao nó hữu ích**: Đơn giản hóa việc quản lý môi trường phát triển một cách đáng kể! Tạo, cấu hình và quản lý môi trường phát triển mà không cần nhớ các lệnh cụ thể.

**Sử dụng thực tế**: "Cài đặt một Dev Box mới với SDK .NET mới nhất và cấu hình nó cho dự án của chúng ta", "Kiểm tra trạng thái tất cả các môi trường phát triển của tôi", hoặc "Tạo môi trường demo tiêu chuẩn cho các bài trình bày nhóm của chúng ta"

**Ví dụ nổi bật**: Tôi là người rất yêu thích sử dụng Dev Box cho phát triển cá nhân. Khoảnh khắc sáng suốt của tôi ở đây là khi James Montemagno giải thích Dev Box tuyệt vời thế nào cho các bản demo hội nghị, vì nó có kết nối ethernet siêu nhanh bất kể wifi của hội nghị / khách sạn / máy bay tôi đang dùng lúc đó ra sao. Thực tế, tôi mới đây đã luyện tập demo hội nghị khi laptop tôi kết nối hotspot điện thoại trong lúc đi xe buýt từ Bruges đến Antwerp! Nhưng bước tiếp theo của tôi là khám phá quản lý nhiều môi trường phát triển và các môi trường demo tiêu chuẩn cho nhóm. Và một trường hợp sử dụng lớn khác mà tôi nghe được từ khách hàng và đồng nghiệp, tất nhiên, là sử dụng Dev Box cho các môi trường phát triển được cấu hình sẵn. Trong cả hai trường hợp, sử dụng một MCP để cấu hình và quản lý Dev Box cho phép bạn tương tác bằng ngôn ngữ tự nhiên, trong khi vẫn làm việc trong môi trường phát triển của bạn.

### 9. 🤖 Máy chủ Microsoft Foundry MCP

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Công việc của nó**: Máy chủ Microsoft Foundry MCP cung cấp cho nhà phát triển quyền truy cập toàn diện đến hệ sinh thái AI của Azure, bao gồm danh mục mô hình, quản lý triển khai, lập chỉ mục kiến thức với Azure AI Search, và công cụ đánh giá. Máy chủ thử nghiệm này kết nối khoảng cách giữa phát triển AI và hạ tầng AI mạnh mẽ của Azure, làm cho việc xây dựng, triển khai, và đánh giá ứng dụng AI trở nên dễ dàng hơn.

**Tại sao nó hữu ích**: Máy chủ này thay đổi cách bạn làm việc với các dịch vụ AI của Azure bằng cách mang các khả năng AI cấp doanh nghiệp trực tiếp vào quy trình phát triển của bạn. Thay vì phải chuyển đổi qua lại giữa cổng Azure, tài liệu, và IDE, bạn có thể khám phá mô hình, triển khai dịch vụ, quản lý cơ sở kiến thức, và đánh giá hiệu suất AI thông qua các lệnh ngôn ngữ tự nhiên. Nó đặc biệt mạnh mẽ cho các nhà phát triển xây dựng ứng dụng RAG (Tạo truy hồi tăng cường), quản lý triển khai đa mô hình, hoặc triển khai các pipeline đánh giá AI toàn diện.

**Khả năng chính cho nhà phát triển**:
- **🔍 Khám phá & Triển khai Mô hình**: Khám phá danh mục mô hình của Microsoft Foundry, nhận thông tin chi tiết về mô hình kèm ví dụ mã, và triển khai mô hình vào dịch vụ Azure AI
- **📚 Quản lý Kiến thức**: Tạo và quản lý các chỉ mục Azure AI Search, thêm tài liệu, cấu hình bộ lập chỉ mục, và xây dựng các hệ thống RAG tinh vi
- **⚡ Tích hợp tác tác AI**: Kết nối với các tác tác Azure AI, truy vấn các tác tác hiện có, và đánh giá hiệu suất tác tác trong các kịch bản sản xuất
- **📊 Khung Đánh giá**: Thực hiện các đánh giá toàn diện về văn bản và tác tác, tạo báo cáo markdown, và triển khai đảm bảo chất lượng cho ứng dụng AI
- **🚀 Công cụ Phác thảo**: Nhận hướng dẫn cài đặt cho phác thảo dựa trên GitHub và truy cập Microsoft Foundry Labs cho các mô hình nghiên cứu tiên tiến

**Sử dụng thực tế của nhà phát triển**: "Triển khai mô hình Phi-4 lên dịch vụ Azure AI cho ứng dụng của tôi", "Tạo chỉ mục tìm kiếm mới cho hệ thống RAG tài liệu của tôi", "Đánh giá phản hồi của tác tác với các chỉ số chất lượng", hoặc "Tìm mô hình lý luận tốt nhất cho các tác vụ phân tích phức tạp của tôi"

**Kịch bản demo toàn diện**: Đây là một quy trình phát triển AI mạnh mẽ:

> "Tôi đang xây dựng một tác tác hỗ trợ khách hàng. Giúp tôi tìm một mô hình lý luận tốt từ danh mục, triển khai nó lên dịch vụ Azure AI, tạo cơ sở kiến thức từ tài liệu của chúng tôi, thiết lập khung đánh giá để kiểm tra chất lượng phản hồi, rồi giúp tôi phác thảo tích hợp với token GitHub để thử nghiệm."

Máy chủ Microsoft Foundry MCP sẽ:
- Truy vấn danh mục mô hình để đề xuất mô hình lý luận tối ưu dựa trên yêu cầu của bạn
- Cung cấp lệnh triển khai và thông tin quota cho khu vực Azure bạn chọn
- Thiết lập chỉ mục tìm kiếm Azure AI với sơ đồ phù hợp cho tài liệu của bạn
- Cấu hình pipeline đánh giá với các chỉ số chất lượng và kiểm tra an toàn
- Tạo mã phác thảo với xác thực GitHub để thử nghiệm ngay lập tức
- Cung cấp hướng dẫn thiết lập toàn diện phù hợp với ngăn xếp công nghệ cụ thể của bạn

**Ví dụ nổi bật**: Với tư cách là nhà phát triển, tôi đã vật lộn để theo kịp các mô hình LLM khác nhau có sẵn. Tôi biết một vài mô hình chính, nhưng cảm thấy như mình bỏ lỡ một số cải tiến về năng suất và hiệu quả. Và tokens cùng quota thật sự căng thẳng và khó quản lý – tôi không bao giờ biết mình có chọn đúng mô hình cho nhiệm vụ hay lãng phí ngân sách không hiệu quả. Tôi vừa nghe về MCP Server này từ James Montemagno khi hỏi đồng đội về đề xuất MCP Server cho bài viết này, và tôi rất phấn khích để sử dụng nó! Khả năng khám phá mô hình trông đặc biệt ấn tượng cho người như tôi muốn khám phá ngoài các lựa chọn thông thường và tìm mô hình tối ưu cho nhiệm vụ cụ thể. Khung đánh giá sẽ giúp tôi xác nhận rằng mình thực sự nhận được kết quả tốt hơn, không chỉ thử cái mới vì muốn thử.

> **ℹ️ Tình trạng Thử nghiệm**
> 
> Máy chủ MCP này đang trong giai đoạn thử nghiệm và phát triển tích cực. Các tính năng và API có thể thay đổi. Hoàn hảo để khám phá khả năng AI Azure và xây dựng nguyên mẫu, nhưng cần xác thực yêu cầu ổn định cho sử dụng sản xuất.
### 10. 🏢 Bộ công cụ Microsoft 365 Agents MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Công việc của nó**: Cung cấp cho nhà phát triển các công cụ thiết yếu để xây dựng tác tác AI và ứng dụng tích hợp với Microsoft 365 và Microsoft 365 Copilot, bao gồm xác nhận cấu trúc, lấy mẫu mã, và hỗ trợ xử lý sự cố.

**Tại sao nó hữu ích**: Xây dựng cho Microsoft 365 và Copilot liên quan đến các cấu trúc manifest phức tạp và các mẫu phát triển cụ thể. Máy chủ MCP này đưa các nguồn tài nguyên phát triển thiết yếu trực tiếp vào môi trường mã của bạn, giúp bạn xác nhận cấu trúc, tìm mẫu mã, và xử lý các sự cố phổ biến mà không cần thường xuyên tham khảo tài liệu.

**Sử dụng thực tế**: "Xác nhận manifest tác tác khai báo của tôi và sửa lỗi cấu trúc nếu có", "Hiển thị mẫu mã cho việc triển khai plugin Microsoft Graph API", hoặc "Giúp tôi xử lý sự cố xác thực ứng dụng Teams"

**Ví dụ nổi bật**: Tôi đã liên hệ với bạn tôi John Miller sau khi nói chuyện với anh ấy tại Build về M365 Agents, và anh ấy giới thiệu MCP này. Điều này có thể rất tuyệt cho các nhà phát triển mới với M365 Agents vì nó cung cấp mẫu, ví dụ mã, và khung để bắt đầu mà không bị ngợp trong tài liệu. Các tính năng xác nhận cấu trúc trông rất hữu ích để tránh lỗi cấu trúc manifest gây mất hàng giờ gỡ lỗi.

> **💡 Mẹo chuyên nghiệp**
> 
> Sử dụng máy chủ này cùng với Microsoft Learn Docs MCP Server để hỗ trợ phát triển M365 toàn diện – một bên cung cấp tài liệu chính thức trong khi bên này cung cấp công cụ phát triển thực tiễn và hỗ trợ xử lý sự cố.


## Tiếp theo là gì? 🔮

## 📋 Kết luận

Model Context Protocol (MCP) đang làm thay đổi cách các nhà phát triển tương tác với trợ lý AI và công cụ bên ngoài. 10 máy chủ Microsoft MCP này chứng tỏ sức mạnh của việc tích hợp AI chuẩn hóa, cho phép quy trình làm việc liền mạch giữ cho nhà phát triển luôn tập trung trong khi truy cập các khả năng bên ngoài mạnh mẽ.

Từ tích hợp toàn diện hệ sinh thái Azure đến các công cụ chuyên biệt như Playwright cho tự động hóa trình duyệt và MarkItDown cho xử lý tài liệu, các máy chủ này trình bày cách MCP có thể nâng cao năng suất trong đa dạng kịch bản phát triển. Giao thức chuẩn hóa đảm bảo các công cụ này hoạt động cùng nhau suôn sẻ, tạo ra trải nghiệm phát triển liền mạch.

Khi hệ sinh thái MCP tiếp tục phát triển, việc tham gia cộng đồng, khám phá máy chủ mới, và xây dựng giải pháp tùy chỉnh sẽ là chìa khóa để tối đa hóa năng suất phát triển của bạn. Tính chất mở chuẩn của MCP nghĩa là bạn có thể phối hợp các công cụ từ nhà cung cấp khác nhau để tạo ra quy trình làm việc hoàn hảo cho nhu cầu cụ thể của mình.

## 🔗 Tài nguyên bổ sung

- [Kho lưu trữ Microsoft MCP chính thức](https://github.com/microsoft/mcp)
- [Cộng đồng & Tài liệu MCP](https://modelcontextprotocol.io/introduction)
- [Tài liệu VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Tài liệu Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Tài liệu Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Học cùng – Sự kiện MCP](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Tùy chỉnh GitHub Copilot tuyệt vời](https://github.com/awesome-copilot)
- [Bộ phát triển SDK C# MCP](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days trực tiếp 29/30 tháng 7 hoặc xem theo yêu cầu](https://aka.ms/mcpdevdays)

## 🎯 Bài tập

1. **Cài đặt và Cấu hình**: Thiết lập một trong các máy chủ MCP trong môi trường VS Code của bạn và kiểm tra chức năng cơ bản.
2. **Tích hợp Quy trình làm việc**: Thiết kế một quy trình phát triển kết hợp ít nhất ba máy chủ MCP khác nhau.
3. **Lập kế hoạch Máy chủ Tùy chỉnh**: Xác định một nhiệm vụ trong thói quen phát triển hàng ngày của bạn có thể hưởng lợi từ một máy chủ MCP tùy chỉnh và tạo một đặc tả cho nó.
4. **Phân tích Hiệu suất**: So sánh hiệu quả của việc sử dụng máy chủ MCP so với các phương pháp truyền thống đối với các nhiệm vụ phát triển phổ biến.
5. **Đánh giá An ninh**: Đánh giá các tác động bảo mật khi sử dụng máy chủ MCP trong môi trường phát triển của bạn và đề xuất các thực hành tốt nhất.


Tiếp theo:[Thực hành Tốt nhất](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->