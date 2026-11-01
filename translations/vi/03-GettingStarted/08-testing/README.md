## Kiểm thử và Gỡ lỗi

Trước khi bạn bắt đầu kiểm thử server MCP của mình, điều quan trọng là phải hiểu các công cụ có sẵn và các phương pháp tốt nhất để gỡ lỗi. Kiểm thử hiệu quả đảm bảo server của bạn hoạt động như mong đợi và giúp bạn nhanh chóng xác định cũng như giải quyết các sự cố. Phần sau đây trình bày các phương pháp được khuyến nghị để xác thực việc triển khai MCP của bạn.

## Tổng quan

Bài học này bao gồm cách chọn phương pháp kiểm thử phù hợp và công cụ kiểm thử hiệu quả nhất.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Mô tả các phương pháp kiểm thử khác nhau.
- Sử dụng các công cụ khác nhau để kiểm thử mã của bạn một cách hiệu quả.


## Kiểm thử Server MCP

MCP cung cấp các công cụ giúp bạn kiểm thử và gỡ lỗi các server của mình:

- **MCP Inspector**: Một công cụ dòng lệnh có thể chạy cả ở chế độ CLI và chế độ trực quan.
- **Kiểm thử thủ công**: Bạn có thể sử dụng công cụ như curl để chạy các yêu cầu web, nhưng bất kỳ công cụ nào có khả năng thực thi HTTP cũng được.
- **Kiểm thử đơn vị**: Có thể sử dụng framework kiểm thử ưa thích của bạn để kiểm thử các tính năng của cả server và client.

### Sử dụng MCP Inspector

Chúng tôi đã mô tả cách dùng công cụ này ở các bài học trước nhưng hãy cùng tìm hiểu ở mức độ tổng quát. Đây là một công cụ phát triển bằng Node.js và bạn có thể sử dụng nó bằng cách gọi thực thi `npx`, công cụ này sẽ tải xuống và cài đặt tạm thời, sau đó tự dọn dẹp khi hoàn thành thực thi yêu cầu của bạn.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) giúp bạn:

- **Khám phá Khả năng Server**: Tự động phát hiện các tài nguyên, công cụ và lời nhắc có sẵn
- **Kiểm thử Thực thi Công cụ**: Thử các tham số khác nhau và xem phản hồi theo thời gian thực
- **Xem Metadata Server**: Kiểm tra thông tin server, sơ đồ, và cấu hình

Một lần chạy điển hình của công cụ như sau:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Lệnh trên khởi động MCP và giao diện trực quan, đồng thời mở một giao diện web cục bộ trên trình duyệt của bạn. Bạn có thể mong đợi thấy một bảng điều khiển hiển thị các server MCP đã đăng ký, các công cụ, tài nguyên và lời nhắc có sẵn. Giao diện này cho phép bạn kiểm thử tương tác việc thực thi công cụ, xem xét metadata server và xem phản hồi thời gian thực, giúp việc xác thực và gỡ lỗi việc triển khai server MCP của bạn trở nên dễ dàng hơn.

Đây là giao diện có thể trông như thế nào: ![Inspector](../../../../translated_images/vi/connect.141db0b2bd05f096.webp)

Bạn cũng có thể chạy công cụ này ở chế độ CLI, khi đó bạn thêm thuộc tính `--cli`. Dưới đây là ví dụ chạy công cụ ở chế độ "CLI" liệt kê tất cả các công cụ trên server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Kiểm thử Thủ công

Ngoài việc chạy công cụ inspector để kiểm thử khả năng của server, một phương pháp tương tự khác là chạy một client có thể sử dụng HTTP, ví dụ như curl.

Với curl, bạn có thể kiểm thử các server MCP trực tiếp bằng các yêu cầu HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Như bạn thấy trong ví dụ sử dụng curl ở trên, bạn dùng yêu cầu POST để gọi một công cụ với payload bao gồm tên công cụ và các tham số của nó. Hãy sử dụng phương pháp phù hợp nhất với bạn. Công cụ dòng lệnh nói chung cho tốc độ sử dụng nhanh hơn và dễ dàng để viết kịch bản tự động, điều này hữu ích trong môi trường CI/CD.

### Kiểm thử Đơn vị

Tạo các bài kiểm thử đơn vị cho công cụ và tài nguyên của bạn để đảm bảo chúng hoạt động như mong đợi. Dưới đây là ví dụ mã kiểm thử.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Đoạn mã trên thực hiện những việc sau:

- Sử dụng framework pytest cho phép bạn tạo các bài kiểm thử dưới dạng hàm và dùng các câu lệnh assert.
- Tạo một MCP Server với hai công cụ khác nhau.
- Dùng câu lệnh `assert` để kiểm tra những điều kiện nhất định được thỏa mãn.

Hãy xem [toàn bộ file tại đây](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dựa trên file trên, bạn có thể kiểm thử server của mình để đảm bảo các khả năng được tạo ra như dự kiến.

Tất cả các SDK lớn đều có phần kiểm thử tương tự nên bạn có thể điều chỉnh cho runtime mà bạn chọn.

## Mẫu

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .NET](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python)

## Tài nguyên Bổ sung

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Tiếp theo

- Tiếp theo: [Triển khai](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->