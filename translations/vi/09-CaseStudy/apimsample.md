# Nghiên cứu trường hợp: Phơi bày REST API trong Quản lý API dưới dạng MCP server

Azure API Management là một dịch vụ cung cấp Gateway trên các API Endpoints của bạn. Cách hoạt động là Azure API Management đóng vai trò như một proxy phía trước các API của bạn và có thể quyết định làm gì với các yêu cầu đến.

Bằng cách sử dụng nó, bạn thêm rất nhiều tính năng như:

- **Bảo mật**, bạn có thể sử dụng mọi thứ từ khóa API, JWT đến định danh quản lý.
- **Giới hạn tần suất**, một tính năng tuyệt vời là có thể quyết định bao nhiêu cuộc gọi được phép qua trong một đơn vị thời gian nhất định. Điều này giúp đảm bảo tất cả người dùng có trải nghiệm tốt và cũng giúp dịch vụ của bạn không bị quá tải với các yêu cầu.
- **Mở rộng & Cân bằng tải**. Bạn có thể thiết lập nhiều endpoint để cân bằng tải và cũng có thể quyết định cách "cân bằng tải".
- **Tính năng AI như semantic caching**, giới hạn token và giám sát token và hơn thế nữa. Đây là những tính năng tuyệt vời cải thiện độ phản hồi cũng như giúp bạn quản lý chi phí token. [Đọc thêm tại đây](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Tại sao MCP + Azure API Management?

Model Context Protocol đang nhanh chóng trở thành tiêu chuẩn cho các ứng dụng AI agentic và cách phơi bày công cụ và dữ liệu một cách nhất quán. Azure API Management là lựa chọn tự nhiên khi bạn cần "quản lý" các API. Các MCP Servers thường tích hợp với các API khác để xử lý yêu cầu tới một công cụ ví dụ. Vì vậy việc kết hợp Azure API Management và MCP là rất hợp lý.

## Tổng quan

Trong trường hợp cụ thể này, chúng ta sẽ học cách phơi bày các API endpoint dưới dạng MCP Server. Bằng cách này, chúng ta có thể dễ dàng tích hợp các endpoint này làm một phần của ứng dụng agentic đồng thời khai thác các tính năng của Azure API Management.

## Các tính năng chính

- Bạn chọn các phương thức endpoint bạn muốn phơi bày như công cụ.
- Các tính năng bổ sung bạn nhận được phụ thuộc vào cấu hình trong phần policy cho API của bạn. Nhưng ở đây chúng tôi sẽ chỉ bạn cách thêm giới hạn tần suất.

## Bước chuẩn bị: nhập một API

Nếu bạn đã có một API trong Azure API Management thì tốt, bạn có thể bỏ qua bước này. Nếu không, xem liên kết này, [nhập API vào Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Phơi bày API như MCP Server

Để phơi bày API endpoints, hãy làm theo các bước sau:

1. Điều hướng tới Azure Portal và địa chỉ sau <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Điều hướng tới instance API Management của bạn.

1. Ở menu bên trái, chọn APIs > MCP Servers > + Tạo MCP Server mới.

1. Trong phần API, chọn một REST API để phơi bày dưới dạng MCP server.

1. Chọn một hoặc nhiều thao tác API để phơi bày làm công cụ. Bạn có thể chọn tất cả hoặc chỉ các thao tác cụ thể.

    ![Chọn các phương pháp để phơi bày](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Chọn **Create**.

1. Điều hướng tới tùy chọn menu **APIs** và **MCP Servers**, bạn sẽ thấy như sau:

    ![Xem MCP Server ở khung chính](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server đã được tạo và các thao tác API được phơi bày làm công cụ. MCP server được liệt kê trong khung MCP Servers. Cột URL hiển thị endpoint của MCP server mà bạn có thể gọi để thử hoặc trong ứng dụng khách.

## Tùy chọn: Cấu hình chính sách

Azure API Management có khái niệm cốt lõi là các chính sách, nơi bạn thiết lập các quy tắc khác nhau cho endpoints của bạn như giới hạn tần suất hay semantic caching. Các chính sách này được viết bằng XML.

Đây là cách bạn có thể thiết lập một chính sách để giới hạn tần suất cho MCP Server:

1. Trong portal, dưới phần APIs, chọn **MCP Servers**.

1. Chọn MCP server bạn đã tạo.

1. Ở menu bên trái, dưới MCP, chọn **Policies**.

1. Trong trình chỉnh sửa chính sách, thêm hoặc sửa các chính sách bạn muốn áp dụng cho các công cụ của MCP server. Các chính sách được định nghĩa bằng định dạng XML. Ví dụ, bạn có thể thêm chính sách giới hạn cuộc gọi tới các công cụ của MCP server (trong ví dụ này, 5 cuộc gọi mỗi 30 giây cho mỗi địa chỉ IP client). Đây là XML sẽ thực hiện việc giới hạn tần suất:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Đây là hình ảnh trình chỉnh sửa chính sách:

    ![Trình chỉnh sửa chính sách](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Thử nghiệm

Hãy đảm bảo MCP Server của bạn hoạt động như mong muốn.

> [!NOTE]
> Hiện tại Azure API Management phơi bày server này qua Streamable
> HTTP `/mcp` endpoint. Phương thức truyền HTTP+SSE `/sse` trước đây đã bị loại bỏ
> và chỉ nên dùng với các client cũ.

Để làm việc này, chúng ta sẽ dùng Visual Studio Code và GitHub Copilot cùng chế độ Agent. Chúng ta sẽ thêm MCP server vào file *mcp.json*. Bằng cách này, Visual Studio Code sẽ hoạt động như một client có khả năng agentic và người dùng cuối có thể gõ prompt và tương tác với server đó.

Hãy xem cách thêm MCP server trong Visual Studio Code:

1. Dùng lệnh MCP: **Add Server từ Command Palette**.

1. Khi được yêu cầu, chọn loại server: **HTTP (HTTP hoặc Server Sent Events)**.

1. Nhập URL Streamable HTTP được hiển thị cho MCP server trong API Management.
    Ví dụ:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Nhập một ID server bạn chọn. Đây không phải giá trị quan trọng nhưng giúp bạn nhớ server instance này là gì.

1. Chọn lưu cấu hình vào cài đặt workspace hay cài đặt người dùng.

    - **Workspace settings** - Cấu hình server được lưu vào file `.vscode/mcp.json`, chỉ có trong workspace hiện tại.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **User settings** - Cấu hình server được thêm vào file *settings.json* toàn cục và có trong tất cả workspace. Cấu hình trông giống như sau:

      ![Cài đặt người dùng](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Bạn cũng cần thêm một header cấu hình để đảm bảo xác thực đúng với Azure API Management. Nó sử dụng header gọi là **Ocp-Apim-Subscription-Key**.

    - Đây là cách thêm vào settings:


    ![Thêm header để xác thực](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), điều này sẽ hiện ra một prompt yêu cầu bạn nhập giá trị khóa API bạn có thể tìm trong Azure Portal của instance Azure API Management.

   - Để thêm vào *mcp.json* thay vào đó, bạn có thể thêm như sau:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Sử dụng chế độ Agent

Bây giờ chúng ta đã thiết lập xong ở cả cấu hình người dùng hoặc trong *.vscode/mcp.json*. Hãy thử nghiệm.

Sẽ có biểu tượng Công cụ như bên dưới, nơi liệt kê các công cụ được phơi bày từ server của bạn:

![Công cụ từ server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Nhấp vào biểu tượng công cụ và bạn sẽ thấy danh sách các công cụ như sau:

    ![Công cụ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Nhập prompt trong chat để gọi công cụ. Ví dụ, nếu bạn chọn công cụ lấy thông tin về đơn hàng, bạn có thể hỏi agent về đơn hàng đó. Đây là ví dụ prompt:

    ```text
    get information from order 2
    ```

    Bây giờ bạn sẽ thấy biểu tượng công cụ yêu cầu xác nhận gọi công cụ. Chọn tiếp tục chạy công cụ, bạn sẽ thấy kết quả xuất ra như sau:

    ![Kết quả từ prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Những gì bạn thấy ở trên phụ thuộc vào các công cụ bạn đã thiết lập, nhưng ý tưởng là bạn nhận được một phản hồi văn bản như trên**


## Tài liệu tham khảo

Đây là cách bạn có thể tìm hiểu thêm:

- [Hướng dẫn về Azure API Management và MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Mẫu Python: Bảo mật các MCP server từ xa sử dụng Azure API Management (thử nghiệm)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Phòng thí nghiệm ủy quyền client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Sử dụng extension Azure API Management cho VS Code để nhập và quản lý APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Đăng ký và khám phá MCP server từ xa trong Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repo tuyệt vời thể hiện nhiều khả năng AI với Azure API Management
- [Workshop AI Gateway](https://azure-samples.github.io/AI-Gateway/) Chứa các workshop dùng Azure Portal, cách tuyệt vời để bắt đầu đánh giá khả năng AI.

## Tiếp theo

- Quay lại: [Tổng quan nghiên cứu trường hợp](./README.md)
- Tiếp theo: [Các đại lý du lịch AI của Azure](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->