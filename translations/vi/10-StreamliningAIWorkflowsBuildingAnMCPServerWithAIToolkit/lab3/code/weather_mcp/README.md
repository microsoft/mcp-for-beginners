# Weather MCP Server

Đây là một ví dụ về MCP Server viết bằng Python, triển khai các công cụ thời tiết với các phản hồi giả lập. Nó có thể được sử dụng làm khung để bạn phát triển MCP Server riêng của mình. Bao gồm các tính năng sau:

- **Weather Tool**: Công cụ cung cấp thông tin thời tiết giả lập dựa trên vị trí được cung cấp.
- **Kết nối với Agent Builder**: Tính năng cho phép bạn kết nối MCP server với Agent Builder để thử nghiệm và gỡ lỗi.
- **Gỡ lỗi trong [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Tính năng cho phép bạn gỡ lỗi MCP Server bằng MCP Inspector.

## Bắt đầu với mẫu Weather MCP Server

> **Yêu cầu trước**
>
> Để chạy MCP Server trên máy phát triển cục bộ, bạn cần:
>
> - [Python](https://www.python.org/)
> - (*Tùy chọn - nếu bạn thích uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Chuẩn bị môi trường

Có hai cách để thiết lập môi trường cho dự án này. Bạn có thể chọn một trong hai tùy theo sở thích.

> Lưu ý: Tải lại VSCode hoặc terminal để đảm bảo python trong môi trường ảo được sử dụng sau khi tạo môi trường ảo.

| Cách làm | Các bước |
| -------- | -------- |
| Sử dụng `uv` | 1. Tạo môi trường ảo: `uv venv` <br>2. Chạy lệnh trong VSCode "***Python: Select Interpreter***" và chọn python từ môi trường ảo vừa tạo <br>3. Cài đặt các phụ thuộc (bao gồm cả phụ thuộc phát triển): `uv pip install -r pyproject.toml --extra dev` |
| Sử dụng `pip` | 1. Tạo môi trường ảo: `python -m venv .venv` <br>2. Chạy lệnh trong VSCode "***Python: Select Interpreter***" và chọn python từ môi trường ảo vừa tạo<br>3. Cài đặt các phụ thuộc (bao gồm cả phụ thuộc phát triển): `pip install -e .[dev]` |

Sau khi thiết lập môi trường, bạn có thể chạy server trên máy phát triển cục bộ thông qua Agent Builder như MCP Client để bắt đầu:
1. Mở bảng Debug của VS Code. Chọn `Debug in Agent Builder` hoặc nhấn `F5` để bắt đầu gỡ lỗi MCP server.
2. Sử dụng AI Toolkit Agent Builder để thử nghiệm server với [prompt này](../../../../../../../../../../open_prompt_builder). Server sẽ tự động kết nối với Agent Builder.
3. Nhấn `Run` để thử nghiệm server với prompt.

**Chúc mừng**! Bạn đã chạy thành công Weather MCP Server trên máy phát triển cục bộ thông qua Agent Builder như MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Những gì có trong mẫu

| Thư mục / Tệp | Nội dung                                     |
| ------------- | -------------------------------------------- |
| `.vscode`     | Các tệp VSCode dùng để gỡ lỗi                 |
| `.aitk`       | Cấu hình cho AI Toolkit                       |
| `src`         | Mã nguồn cho weather mcp server               |

## Cách gỡ lỗi Weather MCP Server

> Lưu ý:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) là công cụ phát triển trực quan để thử nghiệm và gỡ lỗi MCP server.
> - Tất cả các chế độ gỡ lỗi đều hỗ trợ breakpoint, bạn có thể thêm breakpoint vào mã triển khai công cụ.

| Chế độ gỡ lỗi | Mô tả | Các bước gỡ lỗi |
| ------------ | ------ | --------------- |
| Agent Builder | Gỡ lỗi MCP server trong Agent Builder qua AI Toolkit. | 1. Mở bảng Debug của VS Code. Chọn `Debug in Agent Builder` và nhấn `F5` để bắt đầu gỡ lỗi MCP server.<br>2. Sử dụng AI Toolkit Agent Builder để thử nghiệm server với [prompt này](../../../../../../../../../../open_prompt_builder). Server sẽ tự động kết nối với Agent Builder.<br>3. Nhấn `Run` để thử nghiệm server với prompt. |
| MCP Inspector | Gỡ lỗi MCP server bằng MCP Inspector. | 1. Cài đặt [Node.js](https://nodejs.org/)<br> 2. Thiết lập Inspector: `cd inspector` && `npm install` <br> 3. Mở bảng Debug của VS Code. Chọn `Debug SSE in Inspector (Edge)` hoặc `Debug SSE in Inspector (Chrome)`. Nhấn F5 để bắt đầu gỡ lỗi.<br> 4. Khi MCP Inspector mở trong trình duyệt, nhấn nút `Connect` để kết nối MCP server này.<br> 5. Sau đó bạn có thể `List Tools`, chọn công cụ, nhập tham số và `Run Tool` để gỡ lỗi mã server.<br> |

## Cổng mặc định và tùy chỉnh

| Chế độ gỡ lỗi | Cổng | Định nghĩa | Tùy chỉnh | Ghi chú |
| ------------ | ----- | ----------- | --------- | ------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) để thay đổi các cổng trên. | Không áp dụng |
| MCP Inspector | 3001 (Server); 5173 và 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) để thay đổi các cổng trên.| Không áp dụng |

## Phản hồi

Nếu bạn có bất kỳ phản hồi hoặc đề xuất nào cho mẫu này, vui lòng mở issue trên [kho AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.