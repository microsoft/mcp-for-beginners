# Nghiên cứu trường hợp: Công khai REST API trong API Management dưới dạng máy chủ MCP

Azure API Management là một dịch vụ cung cấp một Gateway trên các API Endpoint của bạn. Cách hoạt động của nó là Azure API Management hoạt động như một proxy trước các API của bạn và có thể quyết định cách xử lý các yêu cầu đến.

Khi sử dụng dịch vụ này, bạn có thể thêm rất nhiều tính năng như:

- **Bảo mật**, bạn có thể sử dụng mọi thứ từ API keys, JWT đến managed identity.
- **Giới hạn tốc độ**, một tính năng tuyệt vời là khả năng quyết định số lượng cuộc gọi được phép trong một đơn vị thời gian nhất định. Điều này giúp đảm bảo tất cả người dùng có trải nghiệm tốt và dịch vụ của bạn không bị quá tải bởi các yêu cầu.
- **Khả năng mở rộng & Cân bằng tải**. Bạn có thể thiết lập một số endpoint để cân bằng tải và cũng có thể quyết định cách "cân bằng tải".
- **Các tính năng AI như caching ngữ nghĩa**, giới hạn token và giám sát token và nhiều hơn nữa. Đây là những tính năng tuyệt vời giúp cải thiện khả năng phản hồi cũng như giúp bạn kiểm soát việc sử dụng token. [Đọc thêm tại đây](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Tại sao nên kết hợp MCP + Azure API Management?

Model Context Protocol đang nhanh chóng trở thành tiêu chuẩn cho các ứng dụng AI mang tính tác nhân và cách công khai các công cụ và dữ liệu một cách nhất quán. Azure API Management là một lựa chọn tự nhiên khi bạn cần "quản lý" các API. Các máy chủ MCP thường tích hợp với các API khác để xử lý các yêu cầu đến một công cụ chẳng hạn. Do đó, việc kết hợp Azure API Management và MCP là một ý tưởng hợp lý.

## Tổng quan

Trong trường hợp sử dụng cụ thể này, chúng ta sẽ học cách công khai các API endpoint dưới dạng một máy chủ MCP. Bằng cách này, chúng ta có thể dễ dàng biến các endpoint này thành một phần của ứng dụng mang tính tác nhân đồng thời tận dụng các tính năng từ Azure API Management.

## Các tính năng chính

- Bạn có thể chọn các phương thức endpoint mà bạn muốn công khai dưới dạng công cụ.
- Các tính năng bổ sung bạn nhận được phụ thuộc vào những gì bạn cấu hình trong phần chính sách cho API của mình. Nhưng ở đây chúng ta sẽ chỉ cách thêm giới hạn tốc độ.

## Bước chuẩn bị: nhập một API

Nếu bạn đã có một API trong Azure API Management thì rất tốt, bạn có thể bỏ qua bước này. Nếu không, hãy xem liên kết này, [nhập một API vào Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Công khai API dưới dạng máy chủ MCP

Để công khai các API endpoint, hãy làm theo các bước sau:

1. Truy cập Azure Portal tại địa chỉ sau <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
   Điều hướng đến instance API Management của bạn.

1. Trong menu bên trái, chọn **APIs > MCP Servers > + Create new MCP Server**.

1. Trong API, chọn một REST API để công khai dưới dạng máy chủ MCP.

1. Chọn một hoặc nhiều API Operations để công khai dưới dạng công cụ. Bạn có thể chọn tất cả các operations hoặc chỉ các operations cụ thể.

    ![Chọn phương thức để công khai](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Chọn **Create**.

1. Điều hướng đến tùy chọn menu **APIs** và **MCP Servers**, bạn sẽ thấy như sau:

    ![Xem máy chủ MCP trong bảng chính](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Máy chủ MCP đã được tạo và các API operations được công khai dưới dạng công cụ. Máy chủ MCP được liệt kê trong bảng MCP Servers. Cột URL hiển thị endpoint của máy chủ MCP mà bạn có thể gọi để kiểm tra hoặc sử dụng trong ứng dụng khách.

## Tùy chọn: Cấu hình chính sách

Azure API Management có khái niệm cốt lõi là các chính sách, nơi bạn thiết lập các quy tắc khác nhau cho các endpoint của mình, ví dụ như giới hạn tốc độ hoặc caching ngữ nghĩa. Các chính sách này được viết bằng XML.

Dưới đây là cách bạn có thể thiết lập một chính sách để giới hạn tốc độ máy chủ MCP của mình:

1. Trong portal, dưới **APIs**, chọn **MCP Servers**.

1. Chọn máy chủ MCP mà bạn đã tạo.

1. Trong menu bên trái, dưới MCP, chọn **Policies**.

1. Trong trình chỉnh sửa chính sách, thêm hoặc chỉnh sửa các chính sách bạn muốn áp dụng cho các công cụ của máy chủ MCP. Các chính sách được định nghĩa bằng định dạng XML. Ví dụ, bạn có thể thêm một chính sách để giới hạn số cuộc gọi đến các công cụ của máy chủ MCP (trong ví dụ này, 5 cuộc gọi mỗi 30 giây cho mỗi địa chỉ IP của khách hàng). Đây là XML sẽ gây ra giới hạn tốc độ:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Đây là hình ảnh của trình chỉnh sửa chính sách:

    ![Trình chỉnh sửa chính sách](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Thử nghiệm

Hãy đảm bảo rằng máy chủ MCP của chúng ta hoạt động như mong đợi.

Để làm điều này, chúng ta sẽ sử dụng Visual Studio Code và GitHub Copilot với chế độ Agent. Chúng ta sẽ thêm máy chủ MCP vào một tệp *mcp.json*. Bằng cách làm như vậy, Visual Studio Code sẽ hoạt động như một ứng dụng khách với khả năng tác nhân và người dùng cuối sẽ có thể nhập một prompt và tương tác với máy chủ đó.

Hãy xem cách thực hiện, để thêm máy chủ MCP trong Visual Studio Code:

1. Sử dụng lệnh MCP: **Add Server từ Command Palette**.

1. Khi được nhắc, chọn loại máy chủ: **HTTP (HTTP hoặc Server Sent Events)**.

1. Nhập URL của máy chủ MCP trong API Management. Ví dụ: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (cho endpoint SSE) hoặc **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (cho endpoint MCP), lưu ý sự khác biệt giữa các giao thức là `/sse` hoặc `/mcp`.

1. Nhập một server ID theo ý bạn. Giá trị này không quan trọng nhưng sẽ giúp bạn nhớ máy chủ này là gì.

1. Chọn lưu cấu hình vào cài đặt workspace hoặc cài đặt người dùng.

  - **Cài đặt workspace** - Cấu hình máy chủ được lưu vào tệp .vscode/mcp.json chỉ có sẵn trong workspace hiện tại.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    hoặc nếu bạn chọn HTTP streaming làm giao thức, nó sẽ hơi khác:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Cài đặt người dùng** - Cấu hình máy chủ được thêm vào tệp *settings.json* toàn cục của bạn và có sẵn trong tất cả các workspace. Cấu hình trông giống như sau:

    ![Cài đặt người dùng](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Bạn cũng cần thêm cấu hình, một header để đảm bảo xác thực đúng cách với Azure API Management. Nó sử dụng một header gọi là **Ocp-Apim-Subscription-Key**.

    - Đây là cách bạn có thể thêm nó vào cài đặt:

    ![Thêm header để xác thực](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), điều này sẽ hiển thị một prompt yêu cầu bạn nhập giá trị API key mà bạn có thể tìm thấy trong Azure Portal cho instance Azure API Management của bạn.

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

Bây giờ chúng ta đã thiết lập xong trong cài đặt hoặc trong *.vscode/mcp.json*. Hãy thử nghiệm.

Sẽ có một biểu tượng Tools như sau, nơi các công cụ được công khai từ máy chủ của bạn được liệt kê:

![Công cụ từ máy chủ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Nhấp vào biểu tượng công cụ và bạn sẽ thấy danh sách các công cụ như sau:

    ![Công cụ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Nhập một prompt trong chat để gọi công cụ. Ví dụ, nếu bạn đã chọn một công cụ để lấy thông tin về một đơn hàng, bạn có thể yêu cầu agent về đơn hàng đó. Đây là một ví dụ prompt:

    ```text
    get information from order 2
    ```

    Bạn sẽ thấy một biểu tượng công cụ yêu cầu bạn tiếp tục gọi công cụ. Chọn tiếp tục chạy công cụ, bạn sẽ thấy một kết quả như sau:

    ![Kết quả từ prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Những gì bạn thấy ở trên phụ thuộc vào các công cụ bạn đã thiết lập, nhưng ý tưởng là bạn nhận được một phản hồi dạng văn bản như trên.**

## Tham khảo

Dưới đây là cách bạn có thể tìm hiểu thêm:

- [Hướng dẫn về Azure API Management và MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Ví dụ Python: Bảo mật máy chủ MCP từ xa bằng Azure API Management (thử nghiệm)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Phòng thí nghiệm ủy quyền khách hàng MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Sử dụng tiện ích mở rộng Azure API Management cho VS Code để nhập và quản lý API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Đăng ký và khám phá máy chủ MCP từ xa trong Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Kho lưu trữ tuyệt vời hiển thị nhiều khả năng AI với Azure API Management
- [Hội thảo AI Gateway](https://azure-samples.github.io/AI-Gateway/) Chứa các hội thảo sử dụng Azure Portal, đây là cách tuyệt vời để bắt đầu đánh giá các khả năng AI.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.