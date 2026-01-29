# Triển khai MCP Servers

Triển khai server MCP của bạn cho phép người khác truy cập các công cụ và tài nguyên của nó ngoài môi trường cục bộ của bạn. Có nhiều chiến lược triển khai khác nhau để cân nhắc, tùy thuộc vào yêu cầu về khả năng mở rộng, độ tin cậy và sự dễ dàng trong quản lý. Dưới đây bạn sẽ tìm thấy hướng dẫn triển khai MCP servers tại chỗ, trong container và trên đám mây.

## Tổng quan

Bài học này hướng dẫn cách triển khai ứng dụng MCP Server của bạn.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Đánh giá các phương pháp triển khai khác nhau.
- Triển khai ứng dụng của bạn.

## Phát triển và triển khai cục bộ

Nếu server của bạn được thiết kế để chạy trên máy người dùng, bạn có thể làm theo các bước sau:

1. **Tải server về**. Nếu bạn không tự viết server, hãy tải nó về máy của bạn trước.  
1. **Khởi động tiến trình server**: Chạy ứng dụng MCP server của bạn.

Đối với SSE (không cần thiết với server loại stdio)

1. **Cấu hình mạng**: Đảm bảo server có thể truy cập được trên cổng dự kiến.  
1. **Kết nối client**: Sử dụng URL kết nối cục bộ như `http://localhost:3000`.

## Triển khai trên đám mây

MCP servers có thể được triển khai trên nhiều nền tảng đám mây khác nhau:

- **Serverless Functions**: Triển khai MCP servers nhẹ dưới dạng các hàm serverless.  
- **Container Services**: Sử dụng các dịch vụ như Azure Container Apps, AWS ECS hoặc Google Cloud Run.  
- **Kubernetes**: Triển khai và quản lý MCP servers trong các cụm Kubernetes để đảm bảo tính sẵn sàng cao.

### Ví dụ: Azure Container Apps

Azure Container Apps hỗ trợ triển khai MCP Servers. Đây vẫn là một dự án đang phát triển và hiện tại chỉ hỗ trợ các server SSE.

Dưới đây là cách bạn có thể thực hiện:

1. Clone một repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Chạy nó cục bộ để thử nghiệm:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Để thử nghiệm cục bộ, tạo một file *mcp.json* trong thư mục *.vscode* và thêm nội dung sau:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Khi server SSE được khởi động, bạn có thể nhấn biểu tượng play trong file JSON, lúc này các công cụ trên server sẽ được GitHub Copilot nhận diện, bạn sẽ thấy biểu tượng Tool.

1. Để triển khai, chạy lệnh sau:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Vậy là xong, bạn có thể triển khai cục bộ hoặc triển khai lên Azure theo các bước này.

## Tài nguyên bổ sung

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Bài viết về Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Repo Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)  

## Tiếp theo

- Tiếp theo: [Thực thi thực tế](../../04-PracticalImplementation/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.