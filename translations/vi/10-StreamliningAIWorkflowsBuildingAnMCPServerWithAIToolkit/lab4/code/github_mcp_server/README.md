# Máy chủ MCP Thời tiết

Đây là một mẫu Máy chủ MCP bằng Python triển khai các công cụ thời tiết với phản hồi giả lập. Nó có thể được sử dụng như một khung cho Máy chủ MCP của riêng bạn. Nó bao gồm các tính năng sau:

- **Công cụ Thời tiết**: Một công cụ cung cấp thông tin thời tiết giả lập dựa trên vị trí được cung cấp.
- **Công cụ Sao chép Git**: Một công cụ sao chép kho git vào thư mục được chỉ định.
- **Công cụ Mở VS Code**: Một công cụ mở thư mục trong VS Code hoặc VS Code Insiders.
- **Kết nối với Agent Builder**: Một tính năng cho phép bạn kết nối máy chủ MCP với Agent Builder để kiểm tra và gỡ lỗi.
- **Gỡ lỗi trong [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Một tính năng cho phép bạn gỡ lỗi Máy chủ MCP bằng MCP Inspector.

## Bắt đầu với mẫu Máy chủ MCP Thời tiết

> **Yêu cầu trước**
>
> Để chạy Máy chủ MCP trên máy phát triển cục bộ của bạn, bạn sẽ cần:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Cần thiết cho công cụ git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) hoặc [VS Code Insiders](https://code.visualstudio.com/insiders/) (Cần thiết cho công cụ open_in_vscode)
> - (*Tùy chọn - nếu bạn thích uv*) [uv](https://github.com/astral-sh/uv)
> - [Tiện ích mở rộng Gỡ lỗi Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Chuẩn bị môi trường

Có hai cách để thiết lập môi trường cho dự án này. Bạn có thể chọn một trong hai dựa trên sở thích của bạn.

> Lưu ý: Tải lại VSCode hoặc terminal để đảm bảo sử dụng python của môi trường ảo sau khi tạo môi trường ảo.

| Cách tiếp cận | Các bước |
| -------- | ----- |
| Sử dụng `uv` | 1. Tạo môi trường ảo: `uv venv` <br>2. Chạy lệnh VSCode "***Python: Chọn Bộ thông dịch***" và chọn python từ môi trường ảo đã tạo <br>3. Cài đặt các phụ thuộc (bao gồm phụ thuộc phát triển): `uv pip install -r pyproject.toml --extra dev` |
| Sử dụng `pip` | 1. Tạo môi trường ảo: `python -m venv .venv` <br>2. Chạy lệnh VSCode "***Python: Chọn Bộ thông dịch***" và chọn python từ môi trường ảo đã tạo<br>3. Cài đặt các phụ thuộc (bao gồm phụ thuộc phát triển): `pip install -e .[dev]` | 

Sau khi thiết lập môi trường, bạn có thể chạy máy chủ trên máy phát triển cục bộ qua Agent Builder với vai trò khách hàng MCP để bắt đầu:
1. Mở bảng Gỡ lỗi VS Code. Chọn `Debug in Agent Builder` hoặc nhấn `F5` để bắt đầu gỡ lỗi máy chủ MCP.
2. Trong Microsoft Foundry Toolkit for Visual Studio Code Agent Builder, chọn một triển khai Foundry đang hoạt động như `gpt-5.1`, sau đó nhập: `What is the weather in Shanghai?` Máy chủ sẽ tự động kết nối.
3. Nhấp `Run` để kiểm tra máy chủ với lời nhắc.

**Chúc mừng**! Bạn đã chạy thành công Máy chủ MCP Thời tiết trên máy phát triển cục bộ qua Agent Builder với vai trò khách hàng MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Những gì có trong mẫu

| Thư mục / Tệp | Nội dung                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Tệp VSCode để gỡ lỗi                         |
| `.aitk`      | Cấu hình Microsoft Foundry Toolkit           |
| `src`        | Mã nguồn cho máy chủ mcp thời tiết             |

## Cách gỡ lỗi Máy chủ MCP Thời tiết

> Ghi chú:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) là công cụ phát triển trực quan để kiểm tra và gỡ lỗi các máy chủ MCP.
> - Tất cả các chế độ gỡ lỗi đều hỗ trợ điểm ngắt, bạn có thể thêm điểm ngắt vào mã triển khai công cụ.

## Các công cụ có sẵn

### Công cụ Thời tiết
Công cụ `get_weather` cung cấp thông tin thời tiết giả lập cho vị trí được chỉ định.

| Tham số | Loại | Mô tả |
| --------- | ---- | ----------- |
| `location` | chuỗi | Vị trí lấy thông tin thời tiết (ví dụ: tên thành phố, bang, hoặc tọa độ) |

### Công cụ Sao chép Git
Công cụ `git_clone_repo` sao chép kho git vào thư mục được chỉ định.

| Tham số | Loại | Mô tả |
| --------- | ---- | ----------- |
| `repo_url` | chuỗi | URL kho git cần sao chép |
| `target_folder` | chuỗi | Đường dẫn đến thư mục nơi kho sẽ được sao chép |

Công cụ trả về đối tượng JSON với:
- `success`: Boolean cho biết nếu thao tác thành công
- `target_folder` hoặc `error`: Đường dẫn của kho đã sao chép hoặc thông báo lỗi

### Công cụ Mở VS Code 
Công cụ `open_in_vscode` mở thư mục trong ứng dụng VS Code hoặc VS Code Insiders.

| Tham số | Loại | Mô tả |
| --------- | ---- | ----------- |
| `folder_path` | chuỗi | Đường dẫn đến thư mục cần mở |
| `use_insiders` | boolean (tùy chọn) | Có dùng VS Code Insiders thay vì VS Code thường không |

Công cụ trả về đối tượng JSON với:
- `success`: Boolean cho biết nếu thao tác thành công
- `message` hoặc `error`: Tin nhắn xác nhận hoặc tin nhắn lỗi

| Chế độ Gỡ lỗi | Mô tả | Các bước gỡ lỗi |
| ---------- | ----------- | --------------- |
| Agent Builder | Gỡ lỗi máy chủ MCP trong Agent Builder qua Microsoft Foundry Toolkit cho Visual Studio Code. | 1. Mở bảng Gỡ lỗi VS Code. Chọn `Debug in Agent Builder` và nhấn `F5` để bắt đầu gỡ lỗi máy chủ MCP.<br>2. Chọn một triển khai Foundry đang hoạt động như `gpt-5.1`, sau đó nhập `What is the weather in Shanghai?`. Máy chủ sẽ tự động kết nối.<br>3. Nhấp `Run` để kiểm tra máy chủ với lời nhắc. |
| MCP Inspector | Gỡ lỗi máy chủ MCP bằng MCP Inspector. | 1. Cài đặt [Node.js](https://nodejs.org/)<br> 2. Thiết lập Inspector: `cd inspector` && `npm install` <br> 3. Mở bảng Gỡ lỗi VS Code. Chọn `Debug SSE in Inspector (Edge)` hoặc `Debug SSE in Inspector (Chrome)`. Nhấn F5 để bắt đầu gỡ lỗi.<br> 4. Khi MCP Inspector mở trong trình duyệt, nhấp nút `Connect` để kết nối máy chủ MCP này.<br> 5. Sau đó bạn có thể `List Tools`, chọn công cụ, nhập tham số, và `Run Tool` để gỡ lỗi mã máy chủ.<br> |

## Cổng Mặc định và tùy chỉnh

| Chế độ Gỡ lỗi | Cổng | Định nghĩa | Tùy chỉnh | Ghi chú |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) để thay đổi các cổng trên. | N/A |
| MCP Inspector | 3001 (Máy chủ); 5173 và 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) để thay đổi các cổng trên. | N/A |

## Phản hồi

Nếu bạn có phản hồi hoặc đề xuất cho mẫu này, vui lòng mở một issue trên [kho Microsoft Foundry Toolkit cho Visual Studio Code GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->