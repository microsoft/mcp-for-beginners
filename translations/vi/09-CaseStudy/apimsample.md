# Nghiên cứu trường hợp: Phơi bày REST API trong API Management như một máy chủ MCP

Azure API Management là một dịch vụ cung cấp một Gateway trên đỉnh các Điểm cuối API của bạn. Cách hoạt động là Azure API Management hoạt động như một proxy trước các API của bạn và có thể quyết định làm gì với các yêu cầu đến.

Bằng cách sử dụng nó, bạn thêm một loạt các tính năng như:

- **Bảo mật**, bạn có thể sử dụng mọi thứ từ khóa API, JWT đến định danh được quản lý.
- **Giới hạn tần suất**, một tính năng tuyệt vời là có thể quyết định bao nhiêu cuộc gọi được phép qua trong một đơn vị thời gian nhất định. Điều này giúp đảm bảo tất cả người dùng có trải nghiệm tốt và cũng tránh dịch vụ của bạn bị quá tải với các yêu cầu.
- **Mở rộng & Cân bằng tải**. Bạn có thể thiết lập một số điểm cuối để cân bằng tải và bạn cũng có thể quyết định cách "cân bằng tải".
- **Các tính năng AI như caching ngữ nghĩa**, giới hạn token và giám sát token và nhiều hơn nữa. Đây là các tính năng tuyệt vời giúp cải thiện khả năng phản hồi cũng như giúp bạn kiểm soát việc tiêu thụ token của mình. [Đọc thêm tại đây](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Tại sao chọn MCP + Azure API Management?

Model Context Protocol đang nhanh chóng trở thành tiêu chuẩn cho các ứng dụng AI có tính chủ động và cách phơi bày công cụ cũng như dữ liệu theo một cách nhất quán. Azure API Management là lựa chọn tự nhiên khi bạn cần "quản lý" các API. Các Máy chủ MCP thường tích hợp với các API khác để giải quyết các yêu cầu đến một công cụ ví dụ. Vì vậy, kết hợp Azure API Management và MCP rất hợp lý.

## Tổng quan

Trong trường hợp sử dụng cụ thể này, chúng ta sẽ học cách phơi bày các điểm cuối API như một Máy chủ MCP. Bằng cách này, chúng ta có thể dễ dàng biến các điểm cuối này thành một phần của ứng dụng có tính chủ động đồng thời tận dụng các tính năng từ Azure API Management.

## Các tính năng chính

- Bạn chọn các phương thức điểm cuối bạn muốn phơi bày như công cụ.
- Các tính năng bổ sung bạn nhận được phụ thuộc vào những gì bạn cấu hình trong phần chính sách cho API của bạn. Nhưng ở đây chúng tôi sẽ chỉ bạn cách thêm giới hạn tần suất.

## Bước chuẩn bị: nhập một API

Nếu bạn đã có API trong Azure API Management rồi thì tuyệt vời, bạn có thể bỏ qua bước này. Nếu chưa, xem liên kết sau, [nhập API vào Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Phơi bày API như Máy chủ MCP

Để phơi bày các điểm cuối API, hãy làm theo các bước sau:

1. Điều hướng đến Azure Portal và địa chỉ sau <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Điều hướng đến thể hiện API Management của bạn.

1. Trong menu bên trái, chọn APIs > MCP Servers > + Tạo mới MCP Server.

1. Trong API, chọn một REST API để phơi bày như một máy chủ MCP.

1. Chọn một hoặc nhiều Hoạt động API để phơi bày như công cụ. Bạn có thể chọn tất cả các hoạt động hoặc chỉ những hoạt động cụ thể.

    ![Chọn các phương thức để phơi bày](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Chọn **Tạo**.

1. Điều hướng đến tùy chọn menu **APIs** và **MCP Servers**, bạn sẽ thấy như sau:

    ![Xem MCP Server trong vùng chính](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Máy chủ MCP đã được tạo và các hoạt động API được phơi bày như công cụ. Máy chủ MCP được liệt kê trong bảng MCP Servers. Cột URL hiển thị điểm cuối của máy chủ MCP mà bạn có thể gọi để thử nghiệm hoặc trong ứng dụng khách.

## Tùy chọn: Cấu hình chính sách

Azure API Management có khái niệm cốt lõi về các chính sách nơi bạn thiết lập các quy tắc khác nhau cho các điểm cuối như ví dụ giới hạn tần suất hoặc caching ngữ nghĩa. Các chính sách này được viết bằng XML.

Đây là cách bạn có thể thiết lập một chính sách để giới hạn tần suất cho Máy chủ MCP của bạn:

1. Trong portal, dưới APIs, chọn **MCP Servers**.

1. Chọn máy chủ MCP bạn đã tạo.

1. Trong menu bên trái, dưới MCP, chọn **Policies**.

1. Trong trình soạn thảo chính sách, thêm hoặc chỉnh sửa các chính sách bạn muốn áp dụng cho các công cụ của máy chủ MCP. Các chính sách được định nghĩa ở định dạng XML. Ví dụ, bạn có thể thêm chính sách giới hạn cuộc gọi đến các công cụ của máy chủ MCP (trong ví dụ này, 5 cuộc gọi mỗi 30 giây cho mỗi địa chỉ IP khách). Đây là XML sẽ thực hiện giới hạn tần suất:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Đây là hình ảnh của trình soạn thảo chính sách:

    ![Trình soạn thảo chính sách](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Thử nghiệm

Chúng ta hãy đảm bảo Máy chủ MCP của mình hoạt động như ý muốn.

> [!NOTE]
> Azure API Management hiện tại phơi bày máy chủ này thông qua endpoint HTTP Streamable `/mcp`. 
> Giao thức cũ HTTP+SSE `/sse` đã bị ngừng dùng và 
> chỉ nên sử dụng với các client cũ kỹ.

Để làm điều này, chúng ta sẽ sử dụng Visual Studio Code và GitHub Copilot với chế độ Agent của nó. Chúng ta sẽ thêm máy chủ MCP vào một *mcp.json*. Bằng cách này, Visual Studio Code sẽ hoạt động như một client có khả năng chủ động và người dùng cuối có thể nhập prompt và tương tác với máy chủ đó.

Hãy xem cách thêm máy chủ MCP trong Visual Studio Code:

1. Sử dụng lệnh MCP: **Add Server từ Command Palette**.

1. Khi được yêu cầu, chọn loại máy chủ: **HTTP (HTTP hoặc Server Sent Events)**.

1. Nhập URL HTTP Streamable hiển thị cho máy chủ MCP trong API Management.
    Ví dụ:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Nhập một ID máy chủ tùy chọn. Đây không phải là giá trị quan trọng nhưng sẽ giúp bạn nhớ đây là instance máy chủ nào.

1. Chọn lưu cấu hình vào cài đặt workspace hay cài đặt người dùng.

  - **Cài đặt workspace** - Cấu hình máy chủ sẽ được lưu trong tập tin .vscode/mcp.json chỉ có trong workspace hiện tại.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Cài đặt người dùng** - Cấu hình máy chủ sẽ được thêm vào tập tin *settings.json* toàn cục và có sẵn trong tất cả các workspace. Cấu hình trông như sau:

    ![Cài đặt người dùng](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Bạn cũng cần thêm cấu hình, một header để đảm bảo xác thực đúng đến Azure API Management. Nó sử dụng một header có tên **Ocp-Apim-Subscription-Key**.

    - Đây là cách bạn có thể thêm nó vào cài đặt:

    ![Thêm header để xác thực](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), điều này sẽ khiến một prompt hiển thị yêu cầu bạn nhập giá trị khóa API mà bạn có thể tìm thấy trong Azure Portal cho thể hiện Azure API Management của bạn.

   - Để thêm nó vào *mcp.json*, bạn có thể thêm như sau:

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

Bây giờ ta đã thiết lập xong trong cài đặt hay trong *.vscode/mcp.json*. Hãy thử nghiệm.

Sẽ có một biểu tượng Công cụ như sau, nơi các công cụ được phơi bày từ máy chủ của bạn được liệt kê:

![Công cụ từ máy chủ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Nhấn biểu tượng công cụ và bạn sẽ thấy danh sách các công cụ như sau:

    ![Công cụ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Nhập một prompt trong hộp chat để gọi công cụ. Ví dụ, nếu bạn đã chọn một công cụ để lấy thông tin về một đơn hàng, bạn có thể hỏi đại lý về đơn hàng đó. Đây là ví dụ prompt:

    ```text
    get information from order 2
    ```

    Bạn sẽ được hiển thị một biểu tượng công cụ hỏi bạn có muốn tiếp tục gọi công cụ không. Chọn tiếp tục chạy công cụ, bạn sẽ thấy kết quả như sau:

    ![Kết quả từ prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Những gì bạn thấy ở trên phụ thuộc vào các công cụ bạn đã thiết lập, nhưng ý tưởng là bạn nhận được phản hồi bằng văn bản như trên**


## Tài liệu tham khảo

Đây là cách bạn có thể tìm hiểu thêm:

- [Hướng dẫn về Azure API Management và MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Ví dụ Python: Bảo vệ các máy chủ MCP từ xa bằng Azure API Management (thử nghiệm)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Phòng thí nghiệm ủy quyền client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Sử dụng tiện ích mở rộng Azure API Management cho VS Code để nhập và quản lý API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Đăng ký và khám phá các máy chủ MCP từ xa trong Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Kho lưu trữ tuyệt vời thể hiện nhiều khả năng AI với Azure API Management
- [Hội thảo AI Gateway](https://azure-samples.github.io/AI-Gateway/) Chứa các buổi hội thảo sử dụng Azure Portal, là cách tuyệt vời để bắt đầu đánh giá các khả năng AI.

## Tiếp theo là gì

- Quay lại: [Tổng quan các nghiên cứu trường hợp](./README.md)
- Tiếp theo: [Đại lý du lịch AI Azure](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->