# Dịch vụ Máy tính Cơ bản MCP

Dịch vụ này cung cấp các phép toán cơ bản thông qua Model Context Protocol (MCP). Nó được thiết kế như một ví dụ đơn giản dành cho người mới bắt đầu tìm hiểu về triển khai MCP.

Để biết thêm thông tin, xem [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Tính năng

Dịch vụ máy tính này cung cấp các khả năng sau:

1. **Các phép toán số học cơ bản**:
   - Cộng hai số
   - Trừ một số cho số khác
   - Nhân hai số
   - Chia một số cho số khác (có kiểm tra chia cho 0)

## Sử dụng loại `stdio`
  
## Cấu hình

1. **Cấu hình MCP Servers**:
   - Mở workspace của bạn trong VS Code.
   - Tạo file `.vscode/mcp.json` trong thư mục workspace để cấu hình MCP servers. Ví dụ cấu hình:

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

   - Bạn sẽ được yêu cầu nhập thư mục gốc của kho GitHub, có thể lấy bằng lệnh `git rev-parse --show-toplevel`.

## Sử dụng Dịch vụ

Dịch vụ cung cấp các API endpoint sau thông qua giao thức MCP:

- `add(a, b)`: Cộng hai số
- `subtract(a, b)`: Trừ số thứ hai cho số thứ nhất
- `multiply(a, b)`: Nhân hai số
- `divide(a, b)`: Chia số thứ nhất cho số thứ hai (có kiểm tra chia cho 0)
- isPrime(n): Kiểm tra một số có phải là số nguyên tố không

## Thử nghiệm với Github Copilot Chat trong VS Code

1. Thử gửi yêu cầu đến dịch vụ sử dụng giao thức MCP. Ví dụ, bạn có thể hỏi:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Để chắc chắn đang sử dụng công cụ, thêm #MyCalculator vào câu hỏi. Ví dụ:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Phiên bản Container

Giải pháp trước rất tốt khi bạn đã cài đặt .NET SDK và tất cả các phụ thuộc đã sẵn sàng. Tuy nhiên, nếu bạn muốn chia sẻ giải pháp hoặc chạy nó trong môi trường khác, bạn có thể sử dụng phiên bản container.

1. Khởi động Docker và đảm bảo nó đang chạy.
1. Từ terminal, điều hướng đến thư mục `03-GettingStarted\samples\csharp\src`
1. Để xây dựng image Docker cho dịch vụ máy tính, thực thi lệnh sau (thay `<YOUR-DOCKER-USERNAME>` bằng tên người dùng Docker Hub của bạn):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Sau khi image được xây dựng, hãy tải nó lên Docker Hub bằng lệnh sau:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Sử dụng Phiên bản Docker

1. Trong file `.vscode/mcp.json`, thay thế cấu hình server bằng đoạn sau:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Nhìn vào cấu hình, bạn sẽ thấy lệnh là `docker` và các tham số là `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Cờ `--rm` đảm bảo container sẽ bị xóa sau khi dừng, và cờ `-i` cho phép bạn tương tác với đầu vào chuẩn của container. Tham số cuối cùng là tên image mà chúng ta vừa xây dựng và đẩy lên Docker Hub.

## Thử nghiệm Phiên bản Docker

Khởi động MCP Server bằng cách nhấn nút Start nhỏ phía trên `"mcp-calc": {`, và giống như trước, bạn có thể yêu cầu dịch vụ máy tính thực hiện các phép toán cho bạn.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.