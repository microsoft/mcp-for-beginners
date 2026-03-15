# Triển khai các Máy chủ MCP

Triển khai máy chủ MCP của bạn cho phép người khác truy cập các công cụ và tài nguyên của nó vượt ra ngoài môi trường cục bộ của bạn. Có nhiều chiến lược triển khai khác nhau để xem xét, tùy thuộc vào yêu cầu của bạn về khả năng mở rộng, độ tin cậy và sự dễ dàng quản lý. Dưới đây bạn sẽ tìm thấy hướng dẫn triển khai máy chủ MCP tại chỗ, trong container và lên đám mây.

## Tổng quan

Bài học này bao gồm cách triển khai ứng dụng Máy chủ MCP của bạn.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Đánh giá các phương pháp triển khai khác nhau.
- Triển khai ứng dụng của bạn.

## Phát triển và triển khai tại chỗ

Nếu máy chủ của bạn được sử dụng bằng cách chạy trên máy của người dùng, bạn có thể làm theo các bước sau:

1. **Tải xuống máy chủ**. Nếu bạn không tự viết máy chủ, hãy tải nó về máy của bạn trước.  
1. **Khởi động tiến trình máy chủ**: Chạy ứng dụng máy chủ MCP của bạn.  

Đối với SSE (không cần thiết cho máy chủ kiểu stdio)

1. **Cấu hình mạng**: Đảm bảo máy chủ có thể truy cập được trên cổng mong muốn  
1. **Kết nối các client**: Sử dụng các URL kết nối cục bộ như `http://localhost:3000`  

## Triển khai trên đám mây

Máy chủ MCP có thể được triển khai trên nhiều nền tảng đám mây khác nhau:

- **Hàm Không Máy chủ (Serverless Functions)**: Triển khai các máy chủ MCP nhẹ dưới dạng hàm không máy chủ  
- **Dịch vụ Container**: Sử dụng các dịch vụ như Azure Container Apps, AWS ECS hoặc Google Cloud Run  
- **Kubernetes**: Triển khai và quản lý các máy chủ MCP trong các cụm Kubernetes để đảm bảo tính khả dụng cao  

### Ví dụ: Azure Container Apps

Azure Container Apps hỗ trợ triển khai các Máy chủ MCP. Đây vẫn là một dự án đang trong quá trình phát triển và hiện đang hỗ trợ các máy chủ SSE.

Dưới đây là cách bạn có thể thực hiện:

1. Clone một repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Chạy nó tại chỗ để kiểm tra:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Để thử chạy tại chỗ, tạo một tập tin *mcp.json* trong thư mục *.vscode* và thêm nội dung sau:

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

  Khi máy chủ SSE được khởi động, bạn có thể nhấn vào biểu tượng phát trong tập tin JSON, bạn sẽ thấy các công cụ trên máy chủ được GitHub Copilot nhận diện, xem biểu tượng Công cụ.  

1. Để triển khai, chạy lệnh sau:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Vậy là xong, triển khai tại chỗ, triển khai lên Azure thông qua các bước này.

## Tài nguyên bổ sung

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Bài viết về Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repo MCP Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Tiếp theo

- Tiếp theo: [Các chủ đề máy chủ nâng cao](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->