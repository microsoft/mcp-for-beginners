# Triển khai Máy chủ MCP

> [!NOTE]
> Ví dụ cấu hình sử dụng điểm cuối `/sse` nhắm mục tiêu giao thức HTTP+SSE cũ.
> Máy chủ từ xa MCP `2026-07-28` sử dụng HTTP có thể truyền luồng (Streamable HTTP), thường ở
> một điểm cuối do máy chủ định nghĩa như `/mcp`.

Triển khai máy chủ MCP của bạn cho phép người khác truy cập các công cụ và tài nguyên vượt ra ngoài môi trường cục bộ của bạn. Có một số chiến lược triển khai cần xem xét, tùy theo yêu cầu về khả năng mở rộng, độ tin cậy và dễ quản lý. Dưới đây bạn sẽ tìm thấy hướng dẫn để triển khai máy chủ MCP cục bộ, trong container và lên đám mây.

## Tổng quan

Bài học này hướng dẫn cách triển khai ứng dụng Máy chủ MCP của bạn.

## Mục tiêu học tập

Đến cuối bài học này, bạn sẽ có thể:

- Đánh giá các cách tiếp cận triển khai khác nhau.
- Triển khai ứng dụng của bạn.

## Phát triển và triển khai cục bộ

Nếu máy chủ của bạn được thiết kế để chạy trên máy người dùng, bạn có thể làm theo các bước sau:

1. **Tải máy chủ về**. Nếu bạn không viết máy chủ, hãy tải nó về máy của bạn trước.
1. **Khởi động tiến trình máy chủ**: Chạy ứng dụng máy chủ MCP của bạn

Đối với SSE (không cần cho máy chủ loại stdio)

1. **Cấu hình mạng**: Đảm bảo máy chủ có thể truy cập được trên cổng dự kiến
1. **Kết nối các client**: Dùng URL kết nối cục bộ như `http://localhost:3000`

## Triển khai lên đám mây

Máy chủ MCP có thể được triển khai lên nhiều nền tảng đám mây khác nhau:

- **Hàm Serverless**: Triển khai máy chủ MCP nhẹ dưới dạng hàm serverless
- **Dịch vụ Container**: Sử dụng các dịch vụ như Azure Container Apps, AWS ECS hoặc Google Cloud Run
- **Kubernetes**: Triển khai và quản lý máy chủ MCP trên các cụm Kubernetes để có độ sẵn sàng cao

### Ví dụ: Azure Container Apps

Azure Container Apps hỗ trợ triển khai Máy chủ MCP. Đây vẫn là một dự án đang phát triển và hiện hỗ trợ máy chủ SSE.

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

1. Để thử nghiệm cục bộ, tạo một tệp *mcp.json* trong thư mục *.vscode* và thêm nội dung sau:

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

  Khi máy chủ SSE đã khởi động, bạn có thể nhấn biểu tượng chạy trong tệp JSON, bạn sẽ thấy các công cụ trên máy chủ được GitHub Copilot nhận diện, xem biểu tượng Công cụ.

1. Để triển khai, chạy lệnh sau:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Vậy là bạn đã có, triển khai cục bộ, triển khai lên Azure thông qua các bước này.

## Tài nguyên bổ sung

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Bài viết Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repo Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Tiếp theo là gì

- Tiếp theo: [Chủ đề Máy chủ nâng cao](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->