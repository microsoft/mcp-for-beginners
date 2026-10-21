# Dịch vụ Máy tính Cơ bản MCP

Dịch vụ này cung cấp các phép tính cơ bản thông qua Giao thức Ngữ cảnh Mô hình (MCP). Nó được thiết kế như một ví dụ đơn giản dành cho những người mới bắt đầu tìm hiểu về triển khai MCP.

Để biết thêm thông tin, xem [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Tính năng

Dịch vụ máy tính này cung cấp các khả năng sau:

1. **Các phép toán số học cơ bản**:
   - Cộng hai số
   - Trừ một số cho số còn lại
   - Nhân hai số
   - Chia một số cho số khác (có kiểm tra chia cho 0)

## Sử dụng `stdio` Type
  
## Cấu hình

1. **Cấu hình MCP Servers**:
   - Mở workspace của bạn trong VS Code.
   - Tạo một tập tin `.vscode/mcp.json` trong thư mục workspace để cấu hình các MCP server. Ví dụ cấu hình:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Bạn sẽ được yêu cầu nhập thư mục gốc của kho GitHub, có thể lấy được từ lệnh `git rev-parse --show-toplevel`.

## Sử dụng Dịch vụ

Dịch vụ cung cấp các điểm cuối API sau qua giao thức MCP:

- `add(a, b)`: Cộng hai số
- `subtract(a, b)`: Trừ số thứ hai khỏi số thứ nhất
- `multiply(a, b)`: Nhân hai số
- `divide(a, b)`: Chia số thứ nhất cho số thứ hai (có kiểm tra chia cho 0)
- isPrime(n): Kiểm tra một số có phải là số nguyên tố không

## Thử nghiệm với Github Copilot Chat trong VS Code

1. Thử gửi yêu cầu đến dịch vụ sử dụng giao thức MCP. Ví dụ, bạn có thể hỏi:
   - "Cộng 5 và 3"
   - "Trừ 10 từ 4"
   - "Nhân 6 và 7"
   - "Chia 8 cho 2"
   - "Số 37854 có phải là số nguyên tố không?"
   - "Ba số nguyên tố trước và sau 4242 là gì?"
2. Để chắc chắn nó sử dụng công cụ, thêm #MyCalculator vào câu lệnh. Ví dụ:
   - "Cộng 5 và 3 #MyCalculator"
   - "Trừ 10 từ 4 #MyCalculator"


## Phiên bản Đóng container

Giải pháp trước đó rất tốt khi bạn đã cài đặt .NET SDK và các phụ thuộc đã có sẵn. Tuy nhiên, nếu bạn muốn chia sẻ giải pháp hoặc chạy nó trong môi trường khác, bạn có thể sử dụng phiên bản đóng container.

1. Khởi động Docker và đảm bảo nó đang chạy.
1. Từ terminal, di chuyển đến thư mục `03-GettingStarted\samples\csharp\src` 
1. Để build hình ảnh Docker cho dịch vụ máy tính, thực thi lệnh sau (thay `<YOUR-DOCKER-USERNAME>` bằng tên người dùng Docker Hub của bạn):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Sau khi hình ảnh được build, hãy upload nó lên Docker Hub. Chạy lệnh sau:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Sử dụng Phiên bản Dockerized

1. Trong tập tin `.vscode/mcp.json`, thay thế cấu hình server bằng đoạn sau:
   ```json
    "mcp-calculator": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calculator"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Khi xem cấu hình, bạn có thể thấy lệnh là `docker` và các tham số là `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Cờ `--rm` đảm bảo container được xóa sau khi dừng, và cờ `-i` cho phép bạn tương tác với input chuẩn của container. Tham số cuối cùng là tên hình ảnh chúng ta vừa build và đẩy lên Docker Hub.

## Thử nghiệm Phiên bản Dockerized

Khởi động MCP Server bằng cách nhấn nút Start nhỏ phía trên `"mcp-calculator": {`, và giống như trước bạn có thể yêu cầu dịch vụ máy tính thực hiện một số phép tính cho bạn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->