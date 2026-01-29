# Bài học: Xây dựng MCP Server Tìm kiếm Web

Chương này hướng dẫn cách xây dựng một agent AI thực tế tích hợp với các API bên ngoài, xử lý nhiều loại dữ liệu khác nhau, quản lý lỗi và điều phối nhiều công cụ—tất cả trong một định dạng sẵn sàng cho môi trường sản xuất. Bạn sẽ thấy:

- **Tích hợp với các API bên ngoài yêu cầu xác thực**
- **Xử lý đa dạng loại dữ liệu từ nhiều điểm cuối**
- **Chiến lược xử lý lỗi và ghi nhật ký vững chắc**
- **Điều phối nhiều công cụ trong một server duy nhất**

Kết thúc bài học, bạn sẽ có kinh nghiệm thực tiễn với các mẫu thiết kế và thực hành tốt nhất cần thiết cho các ứng dụng AI và LLM nâng cao.

## Giới thiệu

Trong bài học này, bạn sẽ học cách xây dựng một MCP server và client nâng cao, mở rộng khả năng của LLM với dữ liệu web thời gian thực sử dụng SerpAPI. Đây là kỹ năng quan trọng để phát triển các agent AI động có thể truy cập thông tin cập nhật từ web.

## Mục tiêu học tập

Kết thúc bài học, bạn sẽ có thể:

- Tích hợp các API bên ngoài (như SerpAPI) một cách an toàn vào MCP server
- Triển khai nhiều công cụ cho tìm kiếm web, tin tức, sản phẩm và hỏi đáp
- Phân tích và định dạng dữ liệu có cấu trúc để LLM sử dụng
- Xử lý lỗi và quản lý giới hạn tốc độ API hiệu quả
- Xây dựng và kiểm thử cả client tự động và tương tác

## MCP Server Tìm kiếm Web

Phần này giới thiệu kiến trúc và các tính năng của MCP Server Tìm kiếm Web. Bạn sẽ thấy cách FastMCP và SerpAPI được sử dụng cùng nhau để mở rộng khả năng LLM với dữ liệu web thời gian thực.

### Tổng quan

Triển khai này có bốn công cụ thể hiện khả năng của MCP trong việc xử lý các tác vụ đa dạng dựa trên API bên ngoài một cách an toàn và hiệu quả:

- **general_search**: Tìm kiếm web tổng quát
- **news_search**: Tìm kiếm các tiêu đề tin tức mới nhất
- **product_search**: Tìm kiếm dữ liệu thương mại điện tử
- **qna**: Trích xuất câu hỏi và trả lời

### Tính năng
- **Ví dụ mã nguồn**: Bao gồm các đoạn mã theo ngôn ngữ cụ thể cho Python (và dễ dàng mở rộng sang các ngôn ngữ khác) sử dụng code pivots để rõ ràng

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Trước khi chạy client, bạn nên hiểu server làm gì. File [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) triển khai MCP server, cung cấp các công cụ tìm kiếm web, tin tức, sản phẩm và hỏi đáp bằng cách tích hợp với SerpAPI. Server xử lý các yêu cầu đến, quản lý các cuộc gọi API, phân tích phản hồi và trả về kết quả có cấu trúc cho client.

Bạn có thể xem toàn bộ triển khai trong [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Dưới đây là ví dụ ngắn về cách server định nghĩa và đăng ký một công cụ:

### Python Server

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Tích hợp API bên ngoài**: Minh họa cách xử lý an toàn khóa API và các yêu cầu bên ngoài
- **Phân tích dữ liệu có cấu trúc**: Cho thấy cách chuyển đổi phản hồi API thành định dạng thân thiện với LLM
- **Xử lý lỗi**: Xử lý lỗi vững chắc kèm ghi nhật ký phù hợp
- **Client tương tác**: Bao gồm cả kiểm thử tự động và chế độ tương tác để thử nghiệm
- **Quản lý ngữ cảnh**: Sử dụng MCP Context để ghi nhật ký và theo dõi các yêu cầu

## Yêu cầu trước

Trước khi bắt đầu, hãy đảm bảo môi trường của bạn được thiết lập đúng bằng cách làm theo các bước sau. Điều này đảm bảo tất cả các phụ thuộc được cài đặt và khóa API của bạn được cấu hình chính xác để phát triển và kiểm thử mượt mà.

- Python 3.8 trở lên
- Khóa API SerpAPI (Đăng ký tại [SerpAPI](https://serpapi.com/) - có gói miễn phí)

## Cài đặt

Để bắt đầu, làm theo các bước sau để thiết lập môi trường:

1. Cài đặt các phụ thuộc bằng uv (khuyến nghị) hoặc pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Tạo file `.env` trong thư mục gốc dự án với khóa SerpAPI của bạn:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Cách sử dụng

MCP Server Tìm kiếm Web là thành phần cốt lõi cung cấp các công cụ tìm kiếm web, tin tức, sản phẩm và hỏi đáp bằng cách tích hợp với SerpAPI. Server xử lý các yêu cầu đến, quản lý các cuộc gọi API, phân tích phản hồi và trả về kết quả có cấu trúc cho client.

Bạn có thể xem toàn bộ triển khai trong [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Khởi động Server

Để khởi động MCP server, sử dụng lệnh sau:

```bash
python server.py
```

Server sẽ chạy dưới dạng MCP server dựa trên stdio mà client có thể kết nối trực tiếp.

### Chế độ Client

Client (`client.py`) hỗ trợ hai chế độ để tương tác với MCP server:

- **Chế độ bình thường**: Chạy các kiểm thử tự động để kiểm tra tất cả các công cụ và xác minh phản hồi của chúng. Điều này hữu ích để nhanh chóng kiểm tra server và các công cụ hoạt động như mong đợi.
- **Chế độ tương tác**: Khởi động giao diện menu cho phép bạn chọn và gọi công cụ thủ công, nhập truy vấn tùy chỉnh và xem kết quả theo thời gian thực. Đây là cách lý tưởng để khám phá khả năng của server và thử nghiệm với các đầu vào khác nhau.

Bạn có thể xem toàn bộ triển khai trong [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Chạy Client

Để chạy kiểm thử tự động (lệnh này sẽ tự động khởi động server):

```bash
python client.py
```

Hoặc chạy ở chế độ tương tác:

```bash
python client.py --interactive
```

### Kiểm thử với các phương pháp khác nhau

Có nhiều cách để kiểm thử và tương tác với các công cụ do server cung cấp, tùy thuộc vào nhu cầu và quy trình làm việc của bạn.

#### Viết script kiểm thử tùy chỉnh với MCP Python SDK
Bạn cũng có thể xây dựng các script kiểm thử riêng bằng MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Trong ngữ cảnh này, "script kiểm thử" nghĩa là một chương trình Python tùy chỉnh bạn viết để làm client cho MCP server. Thay vì là một unit test chính thức, script này cho phép bạn kết nối lập trình với server, gọi bất kỳ công cụ nào với tham số bạn chọn, và kiểm tra kết quả. Cách làm này hữu ích cho:
- Phát triển mẫu và thử nghiệm các cuộc gọi công cụ
- Xác thực phản hồi của server với các đầu vào khác nhau
- Tự động hóa các lần gọi công cụ lặp lại
- Xây dựng quy trình làm việc hoặc tích hợp riêng trên MCP server

Bạn có thể dùng script kiểm thử để nhanh chóng thử các truy vấn mới, gỡ lỗi hành vi công cụ, hoặc làm điểm khởi đầu cho tự động hóa nâng cao hơn. Dưới đây là ví dụ cách dùng MCP Python SDK để tạo script như vậy:

## Mô tả các công cụ

Bạn có thể sử dụng các công cụ sau do server cung cấp để thực hiện các loại tìm kiếm và truy vấn khác nhau. Mỗi công cụ được mô tả dưới đây với các tham số và ví dụ sử dụng.

Phần này cung cấp chi tiết về từng công cụ có sẵn và các tham số của chúng.

### general_search

Thực hiện tìm kiếm web tổng quát và trả về kết quả đã được định dạng.

**Cách gọi công cụ này:**

Bạn có thể gọi `general_search` từ script của bạn sử dụng MCP Python SDK, hoặc tương tác qua Inspector hoặc chế độ client tương tác. Dưới đây là ví dụ mã dùng SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Ngoài ra, trong chế độ tương tác, chọn `general_search` từ menu và nhập truy vấn khi được yêu cầu.

**Tham số:**
- `query` (chuỗi): Truy vấn tìm kiếm

**Ví dụ yêu cầu:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Tìm kiếm các bài báo tin tức gần đây liên quan đến truy vấn.

**Cách gọi công cụ này:**

Bạn có thể gọi `news_search` từ script của bạn sử dụng MCP Python SDK, hoặc tương tác qua Inspector hoặc chế độ client tương tác. Dưới đây là ví dụ mã dùng SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Ngoài ra, trong chế độ tương tác, chọn `news_search` từ menu và nhập truy vấn khi được yêu cầu.

**Tham số:**
- `query` (chuỗi): Truy vấn tìm kiếm

**Ví dụ yêu cầu:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Tìm kiếm các sản phẩm phù hợp với truy vấn.

**Cách gọi công cụ này:**

Bạn có thể gọi `product_search` từ script của bạn sử dụng MCP Python SDK, hoặc tương tác qua Inspector hoặc chế độ client tương tác. Dưới đây là ví dụ mã dùng SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Ngoài ra, trong chế độ tương tác, chọn `product_search` từ menu và nhập truy vấn khi được yêu cầu.

**Tham số:**
- `query` (chuỗi): Truy vấn tìm kiếm sản phẩm

**Ví dụ yêu cầu:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Lấy câu trả lời trực tiếp cho các câu hỏi từ các công cụ tìm kiếm.

**Cách gọi công cụ này:**

Bạn có thể gọi `qna` từ script của bạn sử dụng MCP Python SDK, hoặc tương tác qua Inspector hoặc chế độ client tương tác. Dưới đây là ví dụ mã dùng SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Ngoài ra, trong chế độ tương tác, chọn `qna` từ menu và nhập câu hỏi khi được yêu cầu.

**Tham số:**
- `question` (chuỗi): Câu hỏi cần tìm câu trả lời

**Ví dụ yêu cầu:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Chi tiết mã nguồn

Phần này cung cấp các đoạn mã và tham chiếu cho triển khai server và client.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Xem [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) và [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) để biết chi tiết triển khai đầy đủ.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Các khái niệm nâng cao trong bài học này

Trước khi bắt đầu xây dựng, đây là một số khái niệm nâng cao quan trọng sẽ xuất hiện xuyên suốt chương này. Hiểu những điều này sẽ giúp bạn theo kịp nội dung, ngay cả khi bạn mới làm quen:

- **Điều phối nhiều công cụ**: Nghĩa là chạy nhiều công cụ khác nhau (như tìm kiếm web, tin tức, sản phẩm và hỏi đáp) trong một MCP server duy nhất. Điều này cho phép server xử lý đa dạng các tác vụ, không chỉ một loại.
- **Xử lý giới hạn tốc độ API**: Nhiều API bên ngoài (như SerpAPI) giới hạn số lượng yêu cầu bạn có thể gửi trong một khoảng thời gian nhất định. Mã tốt sẽ kiểm tra các giới hạn này và xử lý chúng một cách khéo léo, để ứng dụng không bị lỗi khi vượt quá giới hạn.
- **Phân tích dữ liệu có cấu trúc**: Phản hồi API thường phức tạp và lồng nhau. Khái niệm này liên quan đến việc chuyển đổi các phản hồi đó thành định dạng sạch, dễ sử dụng, thân thiện với LLM hoặc các chương trình khác.
- **Phục hồi lỗi**: Đôi khi có sự cố xảy ra—có thể mạng bị lỗi, hoặc API không trả về dữ liệu như mong đợi. Phục hồi lỗi nghĩa là mã của bạn có thể xử lý các vấn đề này và vẫn cung cấp phản hồi hữu ích, thay vì bị sập.
- **Xác thực tham số**: Đây là việc kiểm tra tất cả các đầu vào cho công cụ của bạn có đúng và an toàn để sử dụng không. Bao gồm việc đặt giá trị mặc định và đảm bảo kiểu dữ liệu chính xác, giúp ngăn ngừa lỗi và nhầm lẫn.

Phần này sẽ giúp bạn chẩn đoán và giải quyết các vấn đề phổ biến có thể gặp khi làm việc với MCP Server Tìm kiếm Web. Nếu bạn gặp lỗi hoặc hành vi không mong muốn khi làm việc với MCP Server Tìm kiếm Web, phần khắc phục sự cố này cung cấp các giải pháp cho những vấn đề thường gặp nhất. Hãy xem qua các mẹo này trước khi tìm kiếm sự trợ giúp thêm—chúng thường giúp bạn giải quyết vấn đề nhanh chóng.

## Khắc phục sự cố

Khi làm việc với MCP Server Tìm kiếm Web, đôi khi bạn có thể gặp sự cố—điều này là bình thường khi phát triển với các API bên ngoài và công cụ mới. Phần này cung cấp các giải pháp thực tế cho những vấn đề phổ biến nhất, giúp bạn nhanh chóng trở lại làm việc. Nếu bạn gặp lỗi, hãy bắt đầu từ đây: các mẹo dưới đây giải quyết các vấn đề mà hầu hết người dùng gặp phải và thường có thể khắc phục mà không cần trợ giúp thêm.

### Các vấn đề thường gặp

Dưới đây là một số vấn đề phổ biến nhất mà người dùng gặp phải, kèm theo giải thích rõ ràng và các bước để khắc phục:

1. **Thiếu SERPAPI_KEY trong file .env**
   - Nếu bạn thấy lỗi `SERPAPI_KEY environment variable not found`, nghĩa là ứng dụng của bạn không tìm thấy khóa API cần thiết để truy cập SerpAPI. Để sửa lỗi này, hãy tạo file `.env` trong thư mục gốc dự án (nếu chưa có) và thêm dòng `SERPAPI_KEY=your_serpapi_key_here`. Hãy chắc chắn thay `your_serpapi_key_here` bằng khóa thực tế của bạn lấy từ trang SerpAPI.

2. **Lỗi không tìm thấy module**
   - Các lỗi như `ModuleNotFoundError: No module named 'httpx'` cho thấy một gói Python cần thiết bị thiếu. Thường xảy ra khi bạn chưa cài đặt đầy đủ các phụ thuộc. Để khắc phục, chạy lệnh `pip install -r requirements.txt` trong terminal để cài đặt tất cả các gói cần thiết cho dự án.

3. **Sự cố kết nối**
   - Nếu bạn nhận lỗi như `Error during client execution`, thường có nghĩa client không thể kết nối với server hoặc server không chạy như mong đợi. Hãy kiểm tra lại phiên bản client và server có tương thích, và file `server.py` có tồn tại và đang chạy trong thư mục đúng không. Khởi động lại cả server và client cũng có thể giúp.

4. **Lỗi SerpAPI**
   - Khi thấy `Search API returned error status: 401` nghĩa là khóa SerpAPI của bạn bị thiếu, sai hoặc đã hết hạn. Hãy vào bảng điều khiển SerpAPI, kiểm tra lại khóa, và cập nhật file `.env` nếu cần. Nếu khóa đúng mà vẫn lỗi, kiểm tra xem gói miễn phí của bạn có hết hạn mức sử dụng không.

### Chế độ Debug

Mặc định, ứng dụng chỉ ghi lại thông tin quan trọng. Nếu bạn muốn xem chi tiết hơn về những gì đang diễn ra (ví dụ để chẩn đoán các vấn đề khó), bạn có thể bật chế độ DEBUG. Chế độ này sẽ hiển thị nhiều thông tin hơn về từng bước ứng dụng thực hiện.

**Ví dụ: Kết quả bình thường**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Ví dụ: Kết quả DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Bạn sẽ thấy chế độ DEBUG bao gồm thêm các dòng về yêu cầu HTTP, phản hồi và các chi tiết nội bộ khác. Điều này rất hữu ích cho việc khắc phục sự cố.
Để bật chế độ DEBUG, hãy đặt mức logging thành DEBUG ở đầu file `client.py` hoặc `server.py` của bạn:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Tiếp theo là gì

- [5.10 Phát trực tiếp thời gian thực](../mcp-realtimestreaming/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.