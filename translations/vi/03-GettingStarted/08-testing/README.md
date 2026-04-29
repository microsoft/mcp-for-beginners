## Testing and Debugging

Trước khi bạn bắt đầu kiểm thử máy chủ MCP của mình, điều quan trọng là phải hiểu các công cụ có sẵn và các phương pháp hay nhất để gỡ lỗi. Kiểm thử hiệu quả đảm bảo máy chủ của bạn hoạt động như mong đợi và giúp bạn nhanh chóng xác định và giải quyết các sự cố. Phần sau đây trình bày các phương pháp được khuyến nghị để xác thực triển khai MCP của bạn.

## Overview

Bài học này bao gồm cách chọn phương pháp kiểm thử phù hợp và công cụ kiểm thử hiệu quả nhất.

## Learning Objectives

Sau khi kết thúc bài học này, bạn sẽ có thể:

- Mô tả các phương pháp khác nhau để kiểm thử.
- Sử dụng các công cụ khác nhau để kiểm thử mã của bạn một cách hiệu quả.


## Testing MCP Servers

MCP cung cấp các công cụ để giúp bạn kiểm thử và gỡ lỗi các máy chủ:

- **MCP Inspector**: Một công cụ dòng lệnh có thể chạy cả dưới dạng CLI và giao diện trực quan.
- **Kiểm thử thủ công**: Bạn có thể dùng công cụ như curl để thực hiện các yêu cầu web, nhưng bất kỳ công cụ nào có thể chạy HTTP đều được.
- **Kiểm thử đơn vị**: Có thể sử dụng framework kiểm thử ưa thích để kiểm thử các tính năng của cả máy chủ và khách hàng.

### Using MCP Inspector

Chúng tôi đã mô tả cách sử dụng công cụ này trong các bài học trước nhưng hãy nói qua về nó ở cấp độ cao. Đây là một công cụ được xây dựng bằng Node.js và bạn có thể sử dụng nó bằng cách gọi thực thi `npx` sẽ tải xuống và cài đặt công cụ tạm thời và sẽ tự động dọn dẹp sau khi hoàn tất chạy yêu cầu của bạn.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) giúp bạn:

- **Khám phá Khả năng Máy chủ**: Tự động phát hiện các tài nguyên, công cụ và các lời nhắc có sẵn
- **Kiểm thử Thực thi Công cụ**: Thử các tham số khác nhau và xem phản hồi theo thời gian thực
- **Xem Thông tin Metadata Máy chủ**: Kiểm tra thông tin máy chủ, schema và cấu hình

Một ví dụ chạy công cụ như sau:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Lệnh trên khởi chạy một MCP và giao diện trực quan của nó đồng thời mở giao diện web cục bộ trên trình duyệt của bạn. Bạn sẽ thấy một bảng điều khiển hiển thị các máy chủ MCP đã đăng ký, các công cụ, tài nguyên và lời nhắc có sẵn. Giao diện cho phép bạn tương tác kiểm thử thực thi công cụ, kiểm tra metadata máy chủ và xem phản hồi thời gian thực, giúp việc xác thực và gỡ lỗi các triển khai MCP của bạn dễ dàng hơn.

Nó trông như thế này: ![Inspector](../../../../translated_images/vi/connect.141db0b2bd05f096.webp)

Bạn cũng có thể chạy công cụ ở chế độ CLI, trong trường hợp đó bạn thêm thuộc tính `--cli`. Đây là ví dụ khi chạy công cụ ở chế độ "CLI" liệt kê tất cả các công cụ trên máy chủ:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manual Testing

Ngoài việc chạy công cụ inspector để kiểm thử khả năng máy chủ, một cách tiếp cận tương tự là chạy một client có thể sử dụng HTTP như ví dụ curl.

Với curl, bạn có thể kiểm thử các máy chủ MCP trực tiếp bằng các yêu cầu HTTP:

```bash
# Ví dụ: Kiểm tra siêu dữ liệu máy chủ
curl http://localhost:3000/v1/metadata

# Ví dụ: Thực thi một công cụ
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Như bạn thấy trong ví dụ sử dụng curl ở trên, bạn sử dụng yêu cầu POST để gọi một công cụ kèm theo payload gồm tên công cụ và các tham số của nó. Hãy chọn cách phù hợp nhất với bạn. Các công cụ CLI nói chung thường nhanh hơn để sử dụng và dễ dàng lập trình kịch bản, điều này có thể hữu ích trong môi trường CI/CD.

### Unit Testing

Tạo các bài kiểm thử đơn vị cho công cụ và tài nguyên của bạn để đảm bảo chúng hoạt động như mong đợi. Dưới đây là ví dụ mã kiểm thử.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Đánh dấu toàn bộ module để kiểm tra bất đồng bộ
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Tạo một vài công cụ kiểm tra
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Kiểm tra không có tham số con trỏ (bị bỏ qua)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Kiểm tra với con trỏ=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Kiểm tra với con trỏ là chuỗi
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Kiểm tra với con trỏ chuỗi rỗng
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Mã trên thực hiện các hành động sau:

- Sử dụng framework pytest cho phép bạn tạo các bài kiểm thử dưới dạng hàm và dùng câu lệnh assert.
- Tạo một Máy chủ MCP với hai công cụ khác nhau.
- Sử dụng câu lệnh `assert` để kiểm tra các điều kiện nhất định được thỏa mãn.

Bạn có thể xem [file đầy đủ ở đây](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dựa vào file trên, bạn có thể kiểm thử máy chủ của mình để đảm bảo các khả năng được tạo đúng như cần.

Tất cả các SDK lớn đều có phần kiểm thử tương tự nên bạn có thể điều chỉnh theo runtime bạn chọn.

## Samples 

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .Net](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python) 

## Additional Resources

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## What's Next

- Tiếp theo: [Triển khai](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo tính chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản của nó được coi là nguồn chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->