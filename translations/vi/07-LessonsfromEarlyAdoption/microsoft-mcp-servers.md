# 🚀 10 Máy chủ Microsoft MCP Đang Thay Đổi Năng Suất Phát Triển Phần Mềm

## 🎯 Những Gì Bạn Sẽ Học Trong Hướng Dẫn Này

Hướng dẫn thực tiễn này giới thiệu mười máy chủ Microsoft MCP đang tích cực thay đổi cách các nhà phát triển làm việc với trợ lý AI. Thay vì chỉ giải thích những gì máy chủ MCP *có thể* làm, chúng tôi sẽ cho bạn thấy những máy chủ đã và đang tạo ra sự khác biệt thực sự trong quy trình phát triển hàng ngày tại Microsoft và các nơi khác.

Mỗi máy chủ trong hướng dẫn này được chọn dựa trên việc sử dụng thực tế và phản hồi từ các nhà phát triển. Bạn sẽ khám phá không chỉ chức năng của từng máy chủ mà còn hiểu tại sao nó quan trọng và cách tận dụng tối đa trong dự án của bạn. Dù bạn hoàn toàn mới với MCP hay muốn mở rộng thiết lập hiện có, những máy chủ này đại diện cho một số công cụ thiết thực và có ảnh hưởng nhất trong hệ sinh thái Microsoft.

> **💡 Mẹo Bắt Đầu Nhanh**
> 
> Mới với MCP? Đừng lo! Hướng dẫn này được thiết kế thân thiện với người mới bắt đầu. Chúng tôi sẽ giải thích các khái niệm khi đi, và bạn luôn có thể tham khảo lại các module [Giới thiệu về MCP](../00-Introduction/README.md) và [Khái niệm Cốt lõi](../01-CoreConcepts/README.md) để hiểu sâu hơn.

## Tổng Quan

Hướng dẫn toàn diện này khám phá mười máy chủ Microsoft MCP đang cách mạng hóa cách các nhà phát triển tương tác với trợ lý AI và các công cụ bên ngoài. Từ quản lý tài nguyên Azure đến xử lý tài liệu, những máy chủ này thể hiện sức mạnh của Model Context Protocol trong việc tạo ra quy trình phát triển liền mạch và hiệu quả.

## Mục Tiêu Học Tập

Kết thúc hướng dẫn này, bạn sẽ:
- Hiểu cách các máy chủ MCP nâng cao năng suất của nhà phát triển
- Tìm hiểu về các triển khai máy chủ MCP có ảnh hưởng nhất của Microsoft
- Khám phá các trường hợp sử dụng thực tế cho từng máy chủ
- Biết cách thiết lập và cấu hình các máy chủ này trong VS Code và Visual Studio
- Khám phá hệ sinh thái MCP rộng lớn hơn và các hướng phát triển trong tương lai

## 🔧 Hiểu Về Máy Chủ MCP: Hướng Dẫn Cho Người Mới Bắt Đầu

### Máy Chủ MCP Là Gì?

Nếu bạn mới với Model Context Protocol (MCP), bạn có thể thắc mắc: "Máy chủ MCP chính xác là gì và tại sao tôi nên quan tâm?" Hãy bắt đầu với một phép so sánh đơn giản.

Hãy tưởng tượng máy chủ MCP như những trợ lý chuyên biệt giúp trợ lý AI lập trình của bạn (như GitHub Copilot) kết nối với các công cụ và dịch vụ bên ngoài. Giống như bạn sử dụng các ứng dụng khác nhau trên điện thoại cho các nhiệm vụ khác nhau—một ứng dụng xem thời tiết, một ứng dụng dẫn đường, một ứng dụng ngân hàng—máy chủ MCP cho phép trợ lý AI của bạn tương tác với các công cụ và dịch vụ phát triển khác nhau.

### Vấn Đề Máy Chủ MCP Giải Quyết

Trước khi có máy chủ MCP, nếu bạn muốn:
- Kiểm tra tài nguyên Azure của mình
- Tạo một issue trên GitHub
- Truy vấn cơ sở dữ liệu
- Tìm kiếm trong tài liệu

Bạn phải dừng việc lập trình, mở trình duyệt, truy cập trang web phù hợp và thực hiện các tác vụ đó thủ công. Việc chuyển đổi ngữ cảnh liên tục này làm gián đoạn dòng chảy công việc và giảm năng suất.

### Cách Máy Chủ MCP Thay Đổi Trải Nghiệm Phát Triển Của Bạn

Với máy chủ MCP, bạn có thể ở lại trong môi trường phát triển (VS Code, Visual Studio, v.v.) và chỉ cần yêu cầu trợ lý AI xử lý các tác vụ này. Ví dụ:

**Thay vì quy trình truyền thống này:**
1. Dừng lập trình
2. Mở trình duyệt
3. Truy cập cổng Azure
4. Tra cứu chi tiết tài khoản lưu trữ
5. Quay lại VS Code
6. Tiếp tục lập trình

**Bạn có thể làm như sau:**
1. Hỏi AI: "Tình trạng các tài khoản lưu trữ Azure của tôi thế nào?"
2. Tiếp tục lập trình với thông tin được cung cấp

### Lợi Ích Chính Cho Người Mới Bắt Đầu

#### 1. 🔄 **Giữ Vững Trạng Thái Tập Trung**
- Không còn phải chuyển đổi giữa nhiều ứng dụng
- Giữ sự tập trung vào mã bạn đang viết
- Giảm bớt gánh nặng tinh thần khi quản lý nhiều công cụ

#### 2. 🤖 **Sử Dụng Ngôn Ngữ Tự Nhiên Thay Vì Lệnh Phức Tạp**
- Thay vì nhớ cú pháp SQL, bạn chỉ cần mô tả dữ liệu cần lấy
- Thay vì nhớ lệnh Azure CLI, bạn giải thích mục tiêu muốn đạt được
- Để AI xử lý các chi tiết kỹ thuật, bạn tập trung vào logic

#### 3. 🔗 **Kết Nối Nhiều Công Cụ Với Nhau**
- Tạo quy trình làm việc mạnh mẽ bằng cách kết hợp các dịch vụ khác nhau
- Ví dụ: "Lấy tất cả các issue GitHub gần đây và tạo các work item tương ứng trên Azure DevOps"
- Xây dựng tự động hóa mà không cần viết script phức tạp

#### 4. 🌐 **Truy Cập Hệ Sinh Thái Ngày Càng Mở Rộng**
- Hưởng lợi từ các máy chủ do Microsoft, GitHub và các công ty khác phát triển
- Kết hợp công cụ từ nhiều nhà cung cấp một cách liền mạch
- Tham gia hệ sinh thái chuẩn hóa hoạt động trên nhiều trợ lý AI khác nhau

#### 5. 🛠️ **Học Qua Thực Hành**
- Bắt đầu với các máy chủ có sẵn để hiểu các khái niệm
- Dần dần xây dựng máy chủ riêng khi bạn quen hơn
- Sử dụng SDK và tài liệu có sẵn để hướng dẫn quá trình học

### Ví Dụ Thực Tế Cho Người Mới Bắt Đầu

Giả sử bạn mới bắt đầu phát triển web và đang làm dự án đầu tiên. Đây là cách máy chủ MCP có thể giúp bạn:

**Cách làm truyền thống:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**Với máy chủ MCP:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Lợi Thế Chuẩn Doanh Nghiệp

MCP đang trở thành tiêu chuẩn ngành, điều này có nghĩa:
- **Tính nhất quán**: Trải nghiệm tương tự trên nhiều công cụ và công ty khác nhau
- **Tính tương tác**: Máy chủ từ các nhà cung cấp khác nhau có thể làm việc cùng nhau
- **Bảo vệ tương lai**: Kỹ năng và thiết lập có thể chuyển đổi giữa các trợ lý AI khác nhau
- **Cộng đồng**: Hệ sinh thái lớn với kiến thức và tài nguyên chia sẻ

### Bắt Đầu: Những Gì Bạn Sẽ Học

Trong hướng dẫn này, chúng ta sẽ khám phá 10 máy chủ Microsoft MCP đặc biệt hữu ích cho các nhà phát triển ở mọi trình độ. Mỗi máy chủ được thiết kế để:
- Giải quyết các thách thức phát triển phổ biến
- Giảm các tác vụ lặp đi lặp lại
- Cải thiện chất lượng mã
- Tăng cơ hội học tập

> **💡 Mẹo Học Tập**
> 
> Nếu bạn hoàn toàn mới với MCP, hãy bắt đầu với các module [Giới thiệu về MCP](../00-Introduction/README.md) và [Khái niệm Cốt lõi](../01-CoreConcepts/README.md). Sau đó quay lại đây để xem các khái niệm này được áp dụng trong các công cụ thực tế của Microsoft.
>
> Để hiểu thêm về tầm quan trọng của MCP, hãy xem bài viết của Maria Naggaga: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Bắt Đầu Với MCP Trong VS Code Và Visual Studio 🚀

Việc thiết lập các máy chủ MCP này khá đơn giản nếu bạn sử dụng Visual Studio Code hoặc Visual Studio 2022 với GitHub Copilot.

### Thiết Lập VS Code

Quy trình cơ bản cho VS Code như sau:

1. **Bật Chế Độ Agent**: Trong VS Code, chuyển sang chế độ Agent trong cửa sổ Copilot Chat
2. **Cấu Hình Máy Chủ MCP**: Thêm cấu hình máy chủ vào file settings.json của VS Code
3. **Khởi Động Máy Chủ**: Nhấn nút "Start" cho từng máy chủ bạn muốn sử dụng
4. **Chọn Công Cụ**: Chọn máy chủ MCP nào sẽ được bật trong phiên làm việc hiện tại

Để biết hướng dẫn chi tiết, xem tài liệu [VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Mẹo Chuyên Nghiệp: Quản Lý Máy Chủ MCP Như Một Pro!**
> 
> Giao diện Extensions của VS Code giờ đây có [giao diện mới tiện lợi để quản lý các máy chủ MCP đã cài đặt](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Bạn có thể nhanh chóng khởi động, dừng và quản lý bất kỳ máy chủ MCP nào qua giao diện rõ ràng, đơn giản. Hãy thử ngay!

### Thiết Lập Visual Studio 2022

Đối với Visual Studio 2022 (phiên bản 17.14 trở lên):

1. **Bật Chế Độ Agent**: Nhấn dropdown "Ask" trong cửa sổ GitHub Copilot Chat và chọn "Agent"
2. **Tạo File Cấu Hình**: Tạo file `.mcp.json` trong thư mục solution của bạn (vị trí khuyến nghị: `<SOLUTIONDIR>\.mcp.json`)
3. **Cấu Hình Máy Chủ**: Thêm cấu hình máy chủ MCP theo định dạng chuẩn MCP
4. **Phê Duyệt Công Cụ**: Khi được yêu cầu, phê duyệt các công cụ bạn muốn sử dụng với quyền truy cập phù hợp

Để biết hướng dẫn chi tiết cho Visual Studio, xem tài liệu [Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Mỗi máy chủ MCP có yêu cầu cấu hình riêng (chuỗi kết nối, xác thực, v.v.), nhưng mẫu thiết lập đều nhất quán trên cả hai IDE.

## Bài Học Rút Ra Từ Máy Chủ Microsoft MCP 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Cài đặt trong VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Cài đặt trong VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Chức năng**: Microsoft Learn Docs MCP Server là dịch vụ đám mây cung cấp cho trợ lý AI quyền truy cập thời gian thực vào tài liệu chính thức của Microsoft thông qua Model Context Protocol. Nó kết nối với `https://learn.microsoft.com/api/mcp` và cho phép tìm kiếm ngữ nghĩa trên Microsoft Learn, tài liệu Azure, tài liệu Microsoft 365 và các nguồn chính thức khác của Microsoft.

**Tại sao hữu ích**: Dù có vẻ chỉ là "tài liệu," máy chủ này thực sự rất quan trọng với mọi nhà phát triển sử dụng công nghệ Microsoft. Một trong những phàn nàn lớn nhất của các nhà phát triển .NET về trợ lý AI lập trình là chúng không cập nhật kịp các phiên bản .NET và C# mới nhất. Microsoft Learn Docs MCP Server giải quyết vấn đề này bằng cách cung cấp quyền truy cập thời gian thực vào tài liệu mới nhất, tham chiếu API và các thực hành tốt nhất. Dù bạn đang làm việc với SDK Azure mới nhất, khám phá tính năng mới của C# 13, hay triển khai các mẫu .NET Aspire tiên tiến, máy chủ này đảm bảo trợ lý AI của bạn có thông tin chính xác, cập nhật để tạo ra mã hiện đại.

**Ứng dụng thực tế**: "Các lệnh az cli để tạo một Azure container app theo tài liệu chính thức của Microsoft Learn là gì?" hoặc "Làm thế nào để cấu hình Entity Framework với dependency injection trong ASP.NET Core?" Hay "Xem lại đoạn mã này để đảm bảo nó phù hợp với các khuyến nghị về hiệu suất trong tài liệu Microsoft Learn." Máy chủ cung cấp phạm vi bao phủ toàn diện trên Microsoft Learn, tài liệu Azure và Microsoft 365 bằng cách sử dụng tìm kiếm ngữ nghĩa nâng cao để tìm thông tin phù hợp nhất theo ngữ cảnh. Nó trả về tối đa 10 đoạn nội dung chất lượng cao kèm tiêu đề bài viết và URL, luôn truy cập tài liệu Microsoft mới nhất khi được xuất bản.

**Ví dụ nổi bật**: Máy chủ cung cấp công cụ `microsoft_docs_search` thực hiện tìm kiếm ngữ nghĩa trên tài liệu kỹ thuật chính thức của Microsoft. Khi được cấu hình, bạn có thể hỏi các câu như "Làm thế nào để triển khai xác thực JWT trong ASP.NET Core?" và nhận được câu trả lời chi tiết, chính thức kèm liên kết nguồn. Chất lượng tìm kiếm rất xuất sắc vì nó hiểu ngữ cảnh – hỏi về "containers" trong bối cảnh Azure sẽ trả về tài liệu Azure Container Instances, trong khi cùng thuật ngữ trong bối cảnh .NET sẽ trả về thông tin về collection trong C#.

Điều này đặc biệt hữu ích với các thư viện và trường hợp sử dụng thay đổi nhanh hoặc mới được cập nhật. Ví dụ, trong một số dự án lập trình gần đây, tôi muốn tận dụng các tính năng trong các phiên bản mới nhất của .NET Aspire và Microsoft.Extensions.AI. Bằng cách thêm Microsoft Learn Docs MCP server, tôi không chỉ sử dụng được tài liệu API mà còn có các hướng dẫn và walkthrough mới được phát hành.
> **💡 Mẹo chuyên nghiệp**
> 
> Ngay cả các mô hình thân thiện với công cụ cũng cần được khuyến khích sử dụng các công cụ MCP! Hãy cân nhắc thêm một lời nhắc hệ thống hoặc [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) như: "Bạn có quyền truy cập vào `microsoft.docs.mcp` – sử dụng công cụ này để tìm kiếm tài liệu chính thức mới nhất của Microsoft khi xử lý các câu hỏi về công nghệ Microsoft như C#, Azure, ASP.NET Core hoặc Entity Framework."
>
> Để xem một ví dụ tuyệt vời về cách áp dụng, hãy tham khảo [chế độ trò chuyện C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) từ kho Awesome GitHub Copilot. Chế độ này tận dụng máy chủ Microsoft Learn Docs MCP để giúp làm sạch và hiện đại hóa mã C# bằng cách sử dụng các mẫu và thực tiễn tốt nhất mới nhất.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Nó làm gì**: Azure MCP Server là một bộ công cụ toàn diện với hơn 15 kết nối dịch vụ Azure chuyên biệt, giúp đưa toàn bộ hệ sinh thái Azure vào quy trình làm việc AI của bạn. Đây không chỉ là một server đơn lẻ – mà là một tập hợp mạnh mẽ bao gồm quản lý tài nguyên, kết nối cơ sở dữ liệu (PostgreSQL, SQL Server), phân tích log Azure Monitor với KQL, tích hợp Cosmos DB, và nhiều hơn nữa.

**Tại sao nó hữu ích**: Ngoài việc quản lý tài nguyên Azure, server này còn cải thiện đáng kể chất lượng mã khi làm việc với Azure SDKs. Khi bạn sử dụng Azure MCP ở chế độ Agent, nó không chỉ giúp bạn viết code – mà còn giúp bạn viết *mã Azure tốt hơn* theo các mẫu xác thực hiện hành, thực hành xử lý lỗi tốt nhất, và tận dụng các tính năng SDK mới nhất. Thay vì nhận được mã chung chung có thể chạy được, bạn sẽ có mã tuân theo các mẫu được Azure khuyến nghị cho các workload sản xuất.

**Các module chính bao gồm**:
- **🗄️ Kết nối Cơ sở dữ liệu**: Truy cập ngôn ngữ tự nhiên trực tiếp đến Azure Database cho PostgreSQL và SQL Server
- **📊 Azure Monitor**: Phân tích log và thông tin vận hành dựa trên KQL
- **🌐 Quản lý Tài nguyên**: Quản lý vòng đời tài nguyên Azure đầy đủ
- **🔐 Xác thực**: Các mẫu DefaultAzureCredential và managed identity
- **📦 Dịch vụ Lưu trữ**: Các thao tác Blob Storage, Queue Storage và Table Storage
- **🚀 Dịch vụ Container**: Quản lý Azure Container Apps, Container Instances và AKS
- **Và nhiều kết nối chuyên biệt khác**

**Ứng dụng thực tế**: "Liệt kê các tài khoản lưu trữ Azure của tôi", "Truy vấn workspace Log Analytics để tìm lỗi trong giờ vừa qua", hoặc "Giúp tôi xây dựng ứng dụng Azure dùng Node.js với xác thực đúng chuẩn"

**Kịch bản demo đầy đủ**: Đây là một hướng dẫn chi tiết thể hiện sức mạnh khi kết hợp Azure MCP với GitHub Copilot for Azure extension trong VS Code. Khi bạn đã cài cả hai và nhập lệnh:

> "Tạo một script Python tải file lên Azure Blob Storage sử dụng xác thực DefaultAzureCredential. Script cần kết nối đến tài khoản lưu trữ Azure của tôi tên 'mycompanystorage', tải lên container 'documents', tạo file test với timestamp hiện tại để tải lên, xử lý lỗi một cách mượt mà và cung cấp thông tin đầu ra rõ ràng, tuân theo các best practice của Azure về xác thực và xử lý lỗi, có chú thích giải thích cách hoạt động của DefaultAzureCredential, và cấu trúc script rõ ràng với các hàm và tài liệu."

Azure MCP Server sẽ tạo ra một script Python hoàn chỉnh, sẵn sàng cho môi trường sản xuất với các điểm sau:
- Sử dụng SDK Azure Blob Storage mới nhất với các mẫu async chuẩn
- Triển khai DefaultAzureCredential với giải thích đầy đủ về chuỗi fallback
- Xử lý lỗi mạnh mẽ với các loại ngoại lệ Azure cụ thể
- Tuân theo best practice của Azure SDK về quản lý tài nguyên và kết nối
- Cung cấp logging chi tiết và đầu ra console rõ ràng
- Tạo script có cấu trúc tốt với hàm, tài liệu và chú thích kiểu dữ liệu

Điều làm nên sự khác biệt là nếu không có Azure MCP, bạn có thể chỉ nhận được mã blob storage chung chung có thể chạy nhưng không theo mẫu Azure hiện hành. Với Azure MCP, bạn có mã tận dụng các phương pháp xác thực mới nhất, xử lý các tình huống lỗi đặc thù của Azure, và tuân theo các thực hành được Microsoft khuyến nghị cho ứng dụng sản xuất.

**Ví dụ nổi bật**: Tôi từng gặp khó khăn khi nhớ các lệnh cụ thể cho CLI `az` và `azd` khi dùng tạm thời. Luôn là quá trình hai bước với tôi: tìm cú pháp rồi chạy lệnh. Tôi thường phải vào portal và click để làm việc vì không muốn thừa nhận mình quên cú pháp CLI. Việc chỉ cần mô tả điều mình muốn thật tuyệt vời, và còn tuyệt hơn khi làm được điều đó ngay trong IDE!

Có một danh sách các trường hợp sử dụng rất hay trong [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) để bạn bắt đầu. Để có hướng dẫn thiết lập chi tiết và tùy chọn cấu hình nâng cao, hãy xem [tài liệu chính thức của Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Nó làm gì**: GitHub MCP Server chính thức cung cấp tích hợp liền mạch với toàn bộ hệ sinh thái GitHub, bao gồm cả truy cập từ xa được host và tùy chọn triển khai Docker cục bộ. Đây không chỉ là các thao tác cơ bản với repository – mà là bộ công cụ toàn diện bao gồm quản lý GitHub Actions, quy trình pull request, theo dõi issue, quét bảo mật, thông báo và các khả năng tự động hóa nâng cao.

**Tại sao nó hữu ích**: Server này thay đổi cách bạn tương tác với GitHub bằng cách đưa toàn bộ trải nghiệm nền tảng trực tiếp vào môi trường phát triển của bạn. Thay vì liên tục chuyển đổi giữa VS Code và GitHub.com để quản lý dự án, review code và theo dõi CI/CD, bạn có thể xử lý mọi thứ qua các lệnh ngôn ngữ tự nhiên trong khi vẫn tập trung vào code.

> **ℹ️ Lưu ý: Các loại 'Agent' khác nhau**
> 
> Đừng nhầm lẫn GitHub MCP Server này với GitHub's Coding Agent (agent AI bạn có thể gán issue để tự động hóa coding). GitHub MCP Server hoạt động trong chế độ Agent của VS Code để cung cấp tích hợp API GitHub, trong khi Coding Agent là tính năng riêng biệt tạo pull request khi được gán issue trên GitHub.

**Các khả năng chính bao gồm**:
- **⚙️ GitHub Actions**: Quản lý pipeline CI/CD đầy đủ, giám sát workflow và xử lý artifact
- **🔀 Pull Requests**: Tạo, review, merge và quản lý PR với theo dõi trạng thái chi tiết
- **🐛 Issues**: Quản lý vòng đời issue, bình luận, gán nhãn và phân công
- **🔒 Bảo mật**: Cảnh báo quét mã, phát hiện secret và tích hợp Dependabot
- **🔔 Thông báo**: Quản lý thông báo thông minh và điều khiển đăng ký repository
- **📁 Quản lý Repository**: Thao tác file, quản lý nhánh và quản trị repository
- **👥 Hợp tác**: Tìm kiếm người dùng và tổ chức, quản lý nhóm và kiểm soát truy cập

**Ứng dụng thực tế**: "Tạo pull request từ nhánh tính năng của tôi", "Hiển thị tất cả các lần chạy CI thất bại trong tuần này", "Liệt kê các cảnh báo bảo mật mở cho các repository của tôi", hoặc "Tìm tất cả issue được giao cho tôi trong các tổ chức của tôi"

**Kịch bản demo đầy đủ**: Đây là một quy trình làm việc mạnh mẽ thể hiện khả năng của GitHub MCP Server:

> "Tôi cần chuẩn bị cho sprint review. Hiển thị tất cả pull request tôi đã tạo trong tuần này, kiểm tra trạng thái các pipeline CI/CD, tạo bản tóm tắt các cảnh báo bảo mật cần xử lý, và giúp tôi soạn thảo ghi chú phát hành dựa trên các PR đã merge có nhãn 'feature'."

GitHub MCP Server sẽ:
- Truy vấn các pull request gần đây với thông tin trạng thái chi tiết
- Phân tích các lần chạy workflow và làm nổi bật các lỗi hoặc vấn đề hiệu suất
- Tổng hợp kết quả quét bảo mật và ưu tiên các cảnh báo quan trọng
- Tạo ghi chú phát hành toàn diện bằng cách trích xuất thông tin từ các PR đã merge
- Cung cấp các bước hành động tiếp theo cho kế hoạch sprint và chuẩn bị phát hành

**Ví dụ nổi bật**: Tôi rất thích dùng nó cho quy trình review code. Thay vì nhảy qua lại giữa VS Code, thông báo GitHub và trang pull request, tôi chỉ cần nói "Hiển thị tất cả PR đang chờ tôi review" rồi "Thêm bình luận vào PR #123 hỏi về cách xử lý lỗi trong phương thức xác thực." Server sẽ xử lý các gọi API GitHub, giữ ngữ cảnh cuộc thảo luận, và thậm chí giúp tôi soạn bình luận review mang tính xây dựng hơn.

**Tùy chọn xác thực**: Server hỗ trợ cả OAuth (liền mạch trong VS Code) và Personal Access Tokens, với bộ công cụ có thể cấu hình để chỉ bật các chức năng GitHub bạn cần. Bạn có thể chạy nó như dịch vụ host từ xa để thiết lập nhanh hoặc cục bộ qua Docker để kiểm soát hoàn toàn.

> **💡 Mẹo chuyên nghiệp**
> 
> Chỉ bật các bộ công cụ bạn cần bằng cách cấu hình tham số `--toolsets` trong cài đặt MCP server để giảm kích thước ngữ cảnh và cải thiện lựa chọn công cụ AI. Ví dụ, thêm `"--toolsets", "repos,issues,pull_requests,actions"` vào args cấu hình MCP cho các workflow phát triển cốt lõi, hoặc dùng `"--toolsets", "notifications, security"` nếu bạn chủ yếu muốn theo dõi GitHub.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Nó làm gì**: Kết nối với các dịch vụ Azure DevOps để quản lý dự án toàn diện, theo dõi work item, quản lý pipeline build và thao tác repository.

**Tại sao nó hữu ích**: Với các nhóm sử dụng Azure DevOps làm nền tảng DevOps chính, MCP server này giúp loại bỏ việc phải chuyển đổi liên tục giữa môi trường phát triển và giao diện web Azure DevOps. Bạn có thể quản lý work item, kiểm tra trạng thái build, truy vấn repository và xử lý các tác vụ quản lý dự án ngay từ trợ lý AI của mình.

**Ứng dụng thực tế**: "Hiển thị tất cả work item đang hoạt động trong sprint hiện tại cho dự án WebApp", "Tạo báo cáo lỗi cho vấn đề đăng nhập tôi vừa phát hiện", hoặc "Kiểm tra trạng thái các pipeline build và hiển thị các lỗi gần đây"

**Ví dụ nổi bật**: Bạn có thể dễ dàng kiểm tra trạng thái sprint hiện tại của nhóm với câu lệnh đơn giản như "Hiển thị tất cả work item đang hoạt động trong sprint hiện tại cho dự án WebApp" hoặc "Tạo báo cáo lỗi cho vấn đề đăng nhập tôi vừa phát hiện" mà không cần rời khỏi môi trường phát triển.

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Nó làm gì**: MarkItDown là một máy chủ chuyển đổi tài liệu toàn diện, biến đổi nhiều định dạng tệp khác nhau thành Markdown chất lượng cao, tối ưu cho việc sử dụng LLM và các quy trình phân tích văn bản.

**Tại sao nó hữu ích**: Thiết yếu cho quy trình tài liệu hiện đại! MarkItDown xử lý đa dạng các định dạng tệp trong khi vẫn giữ nguyên cấu trúc quan trọng của tài liệu như tiêu đề, danh sách, bảng và liên kết. Khác với các công cụ trích xuất văn bản đơn giản, nó tập trung vào việc duy trì ý nghĩa ngữ nghĩa và định dạng có giá trị cho cả xử lý AI và khả năng đọc của con người.

**Các định dạng tệp được hỗ trợ**:
- **Tài liệu Office**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Tệp phương tiện**: Hình ảnh (có metadata EXIF và OCR), Âm thanh (có metadata EXIF và chuyển đổi giọng nói thành văn bản)
- **Nội dung web**: HTML, nguồn cấp RSS, URL YouTube, trang Wikipedia
- **Định dạng dữ liệu**: CSV, JSON, XML, tệp ZIP (xử lý nội dung đệ quy)
- **Định dạng xuất bản**: EPub, sổ tay Jupyter (.ipynb)
- **Email**: Tin nhắn Outlook (.msg)
- **Nâng cao**: Tích hợp Azure Document Intelligence để xử lý PDF nâng cao

**Khả năng nâng cao**: MarkItDown hỗ trợ mô tả hình ảnh dựa trên LLM (khi có OpenAI client), Azure Document Intelligence để xử lý PDF nâng cao, chuyển đổi âm thanh thành văn bản cho nội dung giọng nói, và hệ thống plugin để mở rộng hỗ trợ thêm các định dạng tệp khác.

**Ứng dụng thực tế**: "Chuyển bài thuyết trình PowerPoint này sang Markdown cho trang tài liệu của chúng ta", "Trích xuất văn bản từ PDF này với cấu trúc tiêu đề đúng", hoặc "Chuyển bảng tính Excel này thành định dạng bảng dễ đọc"

**Ví dụ nổi bật**: Trích dẫn từ [tài liệu MarkItDown](https://github.com/microsoft/markitdown#why-markdown):

> Markdown gần như là văn bản thuần túy, với rất ít đánh dấu hoặc định dạng, nhưng vẫn cung cấp cách thể hiện cấu trúc tài liệu quan trọng. Các LLM phổ biến, như GPT-4o của OpenAI, bản thân chúng "nói" Markdown, và thường tích hợp Markdown vào câu trả lời mà không cần yêu cầu. Điều này cho thấy chúng đã được huấn luyện trên lượng lớn văn bản định dạng Markdown và hiểu rất rõ. Một lợi ích phụ nữa là quy ước Markdown cũng rất tiết kiệm token.

MarkItDown thực sự giỏi trong việc giữ nguyên cấu trúc tài liệu, điều quan trọng cho các quy trình AI. Ví dụ, khi chuyển đổi bài thuyết trình PowerPoint, nó giữ nguyên tổ chức slide với các tiêu đề phù hợp, trích xuất bảng dưới dạng bảng Markdown, bao gồm văn bản thay thế cho hình ảnh, và thậm chí xử lý ghi chú người thuyết trình. Biểu đồ được chuyển thành bảng dữ liệu dễ đọc, và Markdown kết quả giữ được luồng logic của bài thuyết trình gốc. Điều này làm cho nó hoàn hảo để đưa nội dung bài thuyết trình vào hệ thống AI hoặc tạo tài liệu từ các slide có sẵn.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Nó làm gì**: Cung cấp truy cập đàm thoại đến cơ sở dữ liệu SQL Server (tại chỗ, Azure SQL hoặc Fabric)

**Tại sao nó hữu ích**: Tương tự như máy chủ PostgreSQL nhưng dành cho hệ sinh thái Microsoft SQL. Kết nối bằng chuỗi kết nối đơn giản và bắt đầu truy vấn bằng ngôn ngữ tự nhiên – không còn phải chuyển đổi ngữ cảnh nữa!

**Ứng dụng thực tế**: "Tìm tất cả đơn hàng chưa được hoàn thành trong 30 ngày qua" được chuyển thành các truy vấn SQL phù hợp và trả về kết quả đã định dạng

**Ví dụ nổi bật**: Khi bạn thiết lập kết nối cơ sở dữ liệu, bạn có thể bắt đầu trò chuyện với dữ liệu ngay lập tức. Bài viết blog minh họa điều này với câu hỏi đơn giản: "Bạn đang kết nối với cơ sở dữ liệu nào?" Máy chủ MCP trả lời bằng cách gọi công cụ cơ sở dữ liệu thích hợp, kết nối với phiên bản SQL Server của bạn và trả về thông tin về kết nối cơ sở dữ liệu hiện tại – tất cả mà không cần viết một dòng SQL nào. Máy chủ hỗ trợ các thao tác cơ sở dữ liệu toàn diện từ quản lý lược đồ đến thao tác dữ liệu, tất cả qua các lệnh bằng ngôn ngữ tự nhiên. Để biết hướng dẫn thiết lập đầy đủ và ví dụ cấu hình với VS Code và Claude Desktop, xem: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Nó làm gì**: Cho phép các tác nhân AI tương tác với các trang web để kiểm thử và tự động hóa

> **ℹ️ Hỗ trợ GitHub Copilot**
> 
> Playwright MCP Server cung cấp sức mạnh cho Coding Agent của GitHub Copilot, giúp nó có khả năng duyệt web! [Tìm hiểu thêm về tính năng này](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Tại sao nó hữu ích**: Hoàn hảo cho kiểm thử tự động dựa trên mô tả bằng ngôn ngữ tự nhiên. AI có thể điều hướng website, điền biểu mẫu và trích xuất dữ liệu qua các ảnh chụp truy cập có cấu trúc – đây là một công cụ cực kỳ mạnh mẽ!

**Ứng dụng thực tế**: "Kiểm thử quy trình đăng nhập và xác nhận rằng bảng điều khiển tải đúng" hoặc "Tạo một bài kiểm thử tìm kiếm sản phẩm và xác thực trang kết quả" – tất cả đều không cần mã nguồn ứng dụng

**Ví dụ nổi bật**: Đồng nghiệp của tôi, Debbie O'Brien, gần đây đã làm việc xuất sắc với Playwright MCP Server! Ví dụ, cô ấy đã trình diễn cách tạo các bài kiểm thử Playwright hoàn chỉnh mà không cần truy cập mã nguồn ứng dụng. Trong kịch bản của cô, cô yêu cầu Copilot tạo bài kiểm thử cho một ứng dụng tìm kiếm phim: truy cập trang web, tìm kiếm "Garfield," và xác nhận phim xuất hiện trong kết quả. MCP đã khởi chạy phiên trình duyệt, khám phá cấu trúc trang qua ảnh chụp DOM, xác định bộ chọn phù hợp, và tạo ra bài kiểm thử TypeScript hoàn chỉnh chạy thành công ngay lần đầu.

Điều làm cho công cụ này thực sự mạnh mẽ là nó kết nối được hướng dẫn bằng ngôn ngữ tự nhiên với mã kiểm thử có thể chạy được. Các phương pháp truyền thống yêu cầu viết kiểm thử thủ công hoặc truy cập mã nguồn để có ngữ cảnh. Nhưng với Playwright MCP, bạn có thể kiểm thử các trang web bên ngoài, ứng dụng khách, hoặc làm việc trong các kịch bản kiểm thử hộp đen khi không có quyền truy cập mã.

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Nó làm gì**: Quản lý môi trường Microsoft Dev Box thông qua ngôn ngữ tự nhiên

**Tại sao nó hữu ích**: Đơn giản hóa việc quản lý môi trường phát triển một cách đáng kể! Tạo, cấu hình và quản lý môi trường phát triển mà không cần nhớ các lệnh cụ thể.

**Ứng dụng thực tế**: "Thiết lập một Dev Box mới với .NET SDK mới nhất và cấu hình cho dự án của chúng ta", "Kiểm tra trạng thái tất cả các môi trường phát triển của tôi", hoặc "Tạo môi trường demo chuẩn hóa cho các buổi thuyết trình nhóm"

**Ví dụ nổi bật**: Tôi rất thích dùng Dev Box cho phát triển cá nhân. Khoảnh khắc “đèn sáng” của tôi là khi James Montemagno giải thích Dev Box tuyệt vời thế nào cho các buổi demo hội nghị, vì nó có kết nối ethernet siêu nhanh bất kể wifi hội nghị / khách sạn / máy bay tôi đang dùng. Thực tế, tôi vừa luyện tập demo hội nghị trong khi laptop tôi kết nối qua hotspot điện thoại trên chuyến xe buýt từ Bruges đến Antwerp! Bước tiếp theo của tôi là tìm hiểu thêm về quản lý nhóm nhiều môi trường phát triển và môi trường demo chuẩn hóa. Một trường hợp sử dụng lớn khác mà tôi nghe từ khách hàng và đồng nghiệp là dùng Dev Box cho các môi trường phát triển được cấu hình sẵn. Trong cả hai trường hợp, dùng MCP để cấu hình và quản lý Dev Box cho phép bạn tương tác bằng ngôn ngữ tự nhiên, đồng thời vẫn làm việc trong môi trường phát triển của mình.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Nó làm gì**: Azure AI Foundry MCP Server cung cấp cho các nhà phát triển quyền truy cập toàn diện vào hệ sinh thái AI của Azure, bao gồm danh mục mô hình, quản lý triển khai, lập chỉ mục kiến thức với Azure AI Search và các công cụ đánh giá. Máy chủ thử nghiệm này kết nối khoảng cách giữa phát triển AI và hạ tầng AI mạnh mẽ của Azure, giúp việc xây dựng, triển khai và đánh giá các ứng dụng AI trở nên dễ dàng hơn.

**Tại sao nó hữu ích**: Máy chủ này thay đổi cách bạn làm việc với các dịch vụ AI của Azure bằng cách đưa các khả năng AI cấp doanh nghiệp trực tiếp vào quy trình phát triển của bạn. Thay vì phải chuyển đổi giữa cổng Azure, tài liệu và IDE, bạn có thể khám phá mô hình, triển khai dịch vụ, quản lý cơ sở kiến thức và đánh giá hiệu suất AI thông qua các lệnh ngôn ngữ tự nhiên. Nó đặc biệt hữu ích cho các nhà phát triển xây dựng ứng dụng RAG (Retrieval-Augmented Generation), quản lý triển khai đa mô hình hoặc triển khai các pipeline đánh giá AI toàn diện.

**Các khả năng chính dành cho nhà phát triển**:
- **🔍 Khám phá & Triển khai Mô hình**: Duyệt danh mục mô hình của Azure AI Foundry, xem thông tin chi tiết kèm ví dụ mã, và triển khai mô hình lên Azure AI Services
- **📚 Quản lý Kiến thức**: Tạo và quản lý các chỉ mục Azure AI Search, thêm tài liệu, cấu hình bộ lập chỉ mục, và xây dựng các hệ thống RAG phức tạp
- **⚡ Tích hợp AI Agent**: Kết nối với Azure AI Agents, truy vấn các agent hiện có, và đánh giá hiệu suất agent trong các kịch bản sản xuất
- **📊 Khung Đánh giá**: Thực hiện đánh giá toàn diện về văn bản và agent, tạo báo cáo markdown, và triển khai đảm bảo chất lượng cho các ứng dụng AI
- **🚀 Công cụ Phát triển Nhanh**: Hướng dẫn thiết lập cho prototyping dựa trên GitHub và truy cập Azure AI Foundry Labs cho các mô hình nghiên cứu tiên tiến

**Sử dụng thực tế của nhà phát triển**: "Triển khai mô hình Phi-4 lên Azure AI Services cho ứng dụng của tôi", "Tạo chỉ mục tìm kiếm mới cho hệ thống RAG tài liệu của tôi", "Đánh giá phản hồi của agent dựa trên các chỉ số chất lượng", hoặc "Tìm mô hình suy luận tốt nhất cho các tác vụ phân tích phức tạp của tôi"

**Kịch bản demo đầy đủ**: Đây là một quy trình phát triển AI mạnh mẽ:

> "Tôi đang xây dựng một agent hỗ trợ khách hàng. Giúp tôi tìm một mô hình suy luận tốt trong danh mục, triển khai nó lên Azure AI Services, tạo cơ sở kiến thức từ tài liệu của chúng tôi, thiết lập khung đánh giá để kiểm tra chất lượng phản hồi, rồi giúp tôi tạo prototype tích hợp với token GitHub để thử nghiệm."

Azure AI Foundry MCP Server sẽ:
- Truy vấn danh mục mô hình để đề xuất các mô hình suy luận tối ưu dựa trên yêu cầu của bạn
- Cung cấp lệnh triển khai và thông tin hạn mức cho khu vực Azure bạn chọn
- Thiết lập các chỉ mục Azure AI Search với cấu trúc phù hợp cho tài liệu của bạn
- Cấu hình pipeline đánh giá với các chỉ số chất lượng và kiểm tra an toàn
- Tạo mã prototyping với xác thực GitHub để thử nghiệm ngay lập tức
- Cung cấp hướng dẫn thiết lập chi tiết phù hợp với ngăn xếp công nghệ của bạn

**Ví dụ nổi bật**: Là một nhà phát triển, tôi đã gặp khó khăn trong việc theo kịp các mô hình LLM khác nhau hiện có. Tôi biết một vài mô hình chính, nhưng cảm thấy mình đang bỏ lỡ nhiều cơ hội tăng năng suất và hiệu quả. Việc quản lý token và hạn mức cũng gây áp lực và khó khăn – tôi không bao giờ chắc mình chọn đúng mô hình cho nhiệm vụ hay đang tiêu tốn ngân sách một cách không hiệu quả. Tôi vừa nghe về MCP Server này từ James Montemagno khi trao đổi với đồng nghiệp về các đề xuất MCP Server cho bài viết này, và tôi rất hào hứng để sử dụng nó! Khả năng khám phá mô hình trông rất ấn tượng với những người như tôi muốn khám phá ngoài những mô hình phổ biến và tìm các mô hình được tối ưu cho các nhiệm vụ cụ thể. Khung đánh giá sẽ giúp tôi xác nhận rằng mình thực sự có kết quả tốt hơn, chứ không chỉ thử nghiệm cho có.

> **ℹ️ Tình trạng Thử nghiệm**
> 
> MCP server này đang trong giai đoạn thử nghiệm và phát triển tích cực. Các tính năng và API có thể thay đổi. Phù hợp để khám phá khả năng Azure AI và xây dựng prototype, nhưng cần kiểm tra kỹ yêu cầu ổn định khi sử dụng trong môi trường sản xuất.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Nó làm gì**: Cung cấp cho các nhà phát triển các công cụ cần thiết để xây dựng các AI agent và ứng dụng tích hợp với Microsoft 365 và Microsoft 365 Copilot, bao gồm xác thực schema, truy xuất mã mẫu và hỗ trợ khắc phục sự cố.

**Tại sao nó hữu ích**: Phát triển cho Microsoft 365 và Copilot đòi hỏi các schema manifest phức tạp và các mẫu phát triển đặc thù. MCP server này đưa các tài nguyên phát triển thiết yếu trực tiếp vào môi trường lập trình của bạn, giúp bạn xác thực schema, tìm mã mẫu và xử lý các vấn đề phổ biến mà không phải liên tục tra cứu tài liệu.

**Sử dụng thực tế**: "Xác thực manifest agent khai báo của tôi và sửa lỗi schema nếu có", "Hiển thị mã mẫu để triển khai plugin Microsoft Graph API", hoặc "Giúp tôi khắc phục sự cố xác thực ứng dụng Teams"

**Ví dụ nổi bật**: Tôi đã liên hệ với bạn tôi John Miller sau khi trò chuyện với anh ấy tại Build về M365 Agents, và anh ấy đã giới thiệu MCP này. Đây có thể là công cụ tuyệt vời cho các nhà phát triển mới với M365 Agents vì nó cung cấp mẫu, mã ví dụ và khung sườn để bắt đầu mà không bị ngập trong tài liệu. Tính năng xác thực schema trông rất hữu ích để tránh các lỗi cấu trúc manifest gây mất nhiều giờ gỡ lỗi.

> **💡 Mẹo chuyên nghiệp**
> 
> Sử dụng server này cùng với Microsoft Learn Docs MCP Server để có hỗ trợ phát triển M365 toàn diện – một bên cung cấp tài liệu chính thức, bên kia cung cấp công cụ phát triển thực tiễn và hỗ trợ khắc phục sự cố.

## Tiếp theo là gì? 🔮

## 📋 Kết luận

Model Context Protocol (MCP) đang thay đổi cách các nhà phát triển tương tác với trợ lý AI và các công cụ bên ngoài. 10 MCP server của Microsoft này thể hiện sức mạnh của việc tích hợp AI theo chuẩn hóa, cho phép các quy trình làm việc liền mạch giúp nhà phát triển duy trì trạng thái tập trung trong khi truy cập các khả năng bên ngoài mạnh mẽ.

Từ việc tích hợp toàn diện hệ sinh thái Azure đến các công cụ chuyên biệt như Playwright cho tự động hóa trình duyệt và MarkItDown cho xử lý tài liệu, các server này cho thấy MCP có thể nâng cao năng suất trong nhiều kịch bản phát triển đa dạng. Giao thức chuẩn hóa đảm bảo các công cụ này hoạt động cùng nhau một cách mượt mà, tạo nên trải nghiệm phát triển thống nhất.

Khi hệ sinh thái MCP tiếp tục phát triển, việc tham gia cộng đồng, khám phá các server mới và xây dựng các giải pháp tùy chỉnh sẽ là chìa khóa để tối đa hóa năng suất phát triển của bạn. Tính mở của MCP cho phép bạn kết hợp các công cụ từ nhiều nhà cung cấp khác nhau để tạo ra quy trình làm việc hoàn hảo phù hợp với nhu cầu riêng.

## 🔗 Tài nguyên bổ sung

- [Official Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Events](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29th/30th July or watch on Demand ](https://aka.ms/mcpdevdays)

## 🎯 Bài tập

1. **Cài đặt và Cấu hình**: Thiết lập một trong các MCP server trong môi trường VS Code của bạn và thử nghiệm các chức năng cơ bản.
2. **Tích hợp Quy trình làm việc**: Thiết kế một quy trình phát triển kết hợp ít nhất ba MCP server khác nhau.
3. **Lập kế hoạch Server Tùy chỉnh**: Xác định một nhiệm vụ trong thói quen phát triển hàng ngày của bạn có thể được cải thiện bằng một MCP server tùy chỉnh và tạo đặc tả cho nó.
4. **Phân tích Hiệu suất**: So sánh hiệu quả khi sử dụng MCP server với các phương pháp truyền thống cho các tác vụ phát triển phổ biến.
5. **Đánh giá An ninh**: Đánh giá các tác động về bảo mật khi sử dụng MCP server trong môi trường phát triển của bạn và đề xuất các thực hành tốt nhất.

Tiếp theo: [Best Practices](../08-BestPractices/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.