# Model Context Protocol (MCP) Python Implementation

Kho lưu trữ này chứa một bản triển khai Python của Model Context Protocol (MCP), minh họa cách tạo cả ứng dụng server và client giao tiếp theo chuẩn MCP.

## Tổng quan

Bản triển khai MCP bao gồm hai thành phần chính:

1. **MCP Server (`server.py`)** - Một server cung cấp:
   - **Tools**: Các hàm có thể được gọi từ xa
   - **Resources**: Dữ liệu có thể truy xuất
   - **Prompts**: Mẫu để tạo prompt cho các mô hình ngôn ngữ

2. **MCP Client (`client.py`)** - Ứng dụng client kết nối với server và sử dụng các tính năng của nó

## Tính năng

Bản triển khai này minh họa một số tính năng chính của MCP:

### Tools
- `completion` - Tạo văn bản hoàn chỉnh từ các mô hình AI (giả lập)
- `add` - Máy tính đơn giản cộng hai số

### Resources
- `models://` - Trả về thông tin về các mô hình AI có sẵn
- `greeting://{name}` - Trả về lời chào cá nhân hóa cho tên được cung cấp

### Prompts
- `review_code` - Tạo prompt để đánh giá mã nguồn

## Cài đặt

Để sử dụng bản triển khai MCP này, cài đặt các gói cần thiết:

```powershell
pip install mcp-server mcp-client
```

## Chạy Server và Client

### Khởi động Server

Chạy server trong một cửa sổ terminal:

```powershell
python server.py
```

Server cũng có thể chạy ở chế độ phát triển bằng cách sử dụng MCP CLI:

```powershell
mcp dev server.py
```

Hoặc cài đặt trong Claude Desktop (nếu có):

```powershell
mcp install server.py
```

### Chạy Client

Chạy client trong một cửa sổ terminal khác:

```powershell
python client.py
```

Điều này sẽ kết nối với server và trình diễn tất cả các tính năng có sẵn.

### Cách sử dụng Client

Client (`client.py`) minh họa tất cả các khả năng của MCP:

```powershell
python client.py
```

Điều này sẽ kết nối với server và sử dụng tất cả các tính năng bao gồm tools, resources và prompts. Kết quả sẽ hiển thị:

1. Kết quả công cụ máy tính (5 + 7 = 12)
2. Phản hồi của công cụ completion cho câu hỏi "What is the meaning of life?"
3. Danh sách các mô hình AI có sẵn
4. Lời chào cá nhân hóa cho "MCP Explorer"
5. Mẫu prompt đánh giá mã nguồn

## Chi tiết triển khai

Server được triển khai sử dụng API `FastMCP`, cung cấp các trừu tượng cấp cao để định nghĩa dịch vụ MCP. Dưới đây là ví dụ đơn giản về cách định nghĩa các tools:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Client sử dụng thư viện MCP client để kết nối và gọi server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Tìm hiểu thêm

Để biết thêm thông tin về MCP, truy cập: https://modelcontextprotocol.io/

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.