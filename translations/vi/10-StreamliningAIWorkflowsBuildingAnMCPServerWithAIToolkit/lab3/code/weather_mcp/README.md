# Máy chủ MCP Thời tiết

Đây là một mẫu Máy chủ MCP bằng Python thực hiện các công cụ thời tiết với các phản hồi mô phỏng. Nó có thể được dùng làm khung cho Máy chủ MCP của riêng bạn. Nó bao gồm các tính năng sau:

- **Công cụ Thời tiết**: Một công cụ cung cấp thông tin thời tiết mô phỏng dựa trên vị trí đã cho.
- **Kết nối với Agent Builder**: Tính năng cho phép bạn kết nối máy chủ MCP với Agent Builder để thử nghiệm và gỡ lỗi.
- **Gỡ lỗi với [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Tính năng cho phép bạn gỡ lỗi Máy chủ MCP bằng MCP Inspector.

## Bắt đầu với mẫu Máy chủ MCP Thời tiết

> **Yêu cầu**
>
> Để chạy Máy chủ MCP trên máy phát triển cục bộ của bạn, bạn sẽ cần:
>
> - [Python](https://www.python.org/)
> - (*Tùy chọn - nếu bạn thích uv*) [uv](https://github.com/astral-sh/uv)
> - [Tiện ích mở rộng Gỡ lỗi Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Chuẩn bị môi trường

Có hai cách tiếp cận để thiết lập môi trường cho dự án này. Bạn có thể chọn một trong hai tùy theo sở thích.

> Lưu ý: Tải lại VSCode hoặc terminal để chắc chắn python của môi trường ảo được sử dụng sau khi tạo môi trường ảo.

| Cách tiếp cận | Các bước |
| -------- | ----- |
| Sử dụng `uv` | 1. Tạo môi trường ảo: `uv venv` <br>2. Chạy lệnh VSCode "***Python: Select Interpreter***" và chọn python từ môi trường ảo vừa tạo <br>3. Cài đặt các phụ thuộc (bao gồm cả phụ thuộc phát triển): `uv pip install -r pyproject.toml --extra dev` |
| Sử dụng `pip` | 1. Tạo môi trường ảo: `python -m venv .venv` <br>2. Chạy lệnh VSCode "***Python: Select Interpreter***" và chọn python từ môi trường ảo vừa tạo<br>3. Cài đặt các phụ thuộc (bao gồm cả phụ thuộc phát triển): `pip install -e .[dev]` | 

Sau khi thiết lập môi trường, bạn có thể chạy máy chủ trên máy phát triển cục bộ thông qua Agent Builder như MCP Client để bắt đầu:
1. Mở bảng Debug của VS Code. Chọn `Debug in Agent Builder` hoặc nhấn `F5` để bắt đầu gỡ lỗi máy chủ MCP.
2. Trong Microsoft Foundry Toolkit Agent Builder, chọn một triển khai Foundry đang hoạt động như `gpt-5.1`, sau đó nhập: `What is the weather in Shanghai?` Máy chủ sẽ tự động kết nối.
3. Nhấn `Run` để kiểm tra máy chủ với lời nhắc.

**Chúc mừng**! Bạn đã chạy thành công Máy chủ MCP Thời tiết trên máy phát triển cục bộ thông qua Agent Builder như MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Những gì có trong mẫu

| Thư mục / Tệp | Nội dung                                   |
| ------------ | -------------------------------------------- |
| `.vscode`    | Các tệp VSCode để gỡ lỗi                       |
| `.aitk`      | Cấu hình cho Microsoft Foundry Toolkit                |
| `src`        | Mã nguồn cho máy chủ mcp thời tiết               |

## Cách gỡ lỗi Máy chủ MCP Thời tiết

> Lưu ý:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) là công cụ phát triển trực quan để thử nghiệm và gỡ lỗi máy chủ MCP.
> - Tất cả các chế độ gỡ lỗi đều hỗ trợ điểm dừng, do đó bạn có thể thêm điểm dừng vào mã triển khai công cụ.

| Chế độ gỡ lỗi | Mô tả | Các bước gỡ lỗi |
| ---------- | ----------- | --------------- |
| Agent Builder | Gỡ lỗi máy chủ MCP trong Agent Builder qua Microsoft Foundry Toolkit. | 1. Mở bảng Debug của VS Code. Chọn `Debug in Agent Builder` và nhấn `F5` để bắt đầu gỡ lỗi máy chủ MCP.<br>2. Chọn một triển khai Foundry đang hoạt động như `gpt-5.1`, sau đó nhập `What is the weather in Shanghai?`. Máy chủ sẽ tự động kết nối.<br>3. Nhấn `Run` để kiểm tra máy chủ với lời nhắc. |
| MCP Inspector | Gỡ lỗi máy chủ MCP bằng MCP Inspector. | 1. Cài đặt [Node.js](https://nodejs.org/)<br> 2. Thiết lập Inspector: `cd inspector` && `npm install` <br> 3. Mở bảng Debug của VS Code. Chọn `Debug SSE in Inspector (Edge)` hoặc `Debug SSE in Inspector (Chrome)`. Nhấn F5 để bắt đầu gỡ lỗi.<br> 4. Khi MCP Inspector khởi chạy trong trình duyệt, nhấn nút `Connect` để kết nối với máy chủ MCP này.<br> 5. Sau đó bạn có thể `List Tools`, chọn một công cụ, nhập tham số, và `Run Tool` để gỡ lỗi mã máy chủ của bạn.<br> |

## Các cổng mặc định và tùy chỉnh

| Chế độ gỡ lỗi | Các cổng | Định nghĩa | Tùy chỉnh | Ghi chú |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) để thay đổi các cổng trên. | N/A |
| MCP Inspector | 3001 (Máy chủ); 5173 và 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) để thay đổi các cổng trên.| N/A |

## Phản hồi

Nếu bạn có bất kỳ phản hồi hoặc đề xuất nào cho mẫu này, vui lòng mở một issue trên [kho lưu trữ Microsoft Foundry Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->