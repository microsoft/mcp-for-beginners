# Máy chủ MCP Thời tiết

Đây là một máy chủ MCP mẫu viết bằng Python, triển khai các công cụ thời tiết với phản hồi giả lập. Nó có thể được sử dụng làm khung mẫu cho máy chủ MCP của bạn. Các tính năng bao gồm:

- **Công cụ Thời tiết**: Một công cụ cung cấp thông tin thời tiết giả lập dựa trên vị trí được cung cấp.
- **Công cụ Clone Git**: Một công cụ để sao chép một kho lưu trữ git vào thư mục được chỉ định.
- **Công cụ Mở VS Code**: Một công cụ mở thư mục trong VS Code hoặc VS Code Insiders.
- **Kết nối với Agent Builder**: Một tính năng cho phép bạn kết nối máy chủ MCP với Agent Builder để kiểm tra và gỡ lỗi.
- **Gỡ lỗi trong [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Một tính năng cho phép bạn gỡ lỗi máy chủ MCP bằng MCP Inspector.

## Bắt đầu với mẫu Máy chủ MCP Thời tiết

> **Yêu cầu trước**
>
> Để chạy máy chủ MCP trên máy phát triển cục bộ của bạn, bạn cần:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Cần thiết cho công cụ git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) hoặc [VS Code Insiders](https://code.visualstudio.com/insiders/) (Cần thiết cho công cụ open_in_vscode)
> - (*Tùy chọn - nếu bạn thích uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Chuẩn bị môi trường

Có hai cách để thiết lập môi trường cho dự án này. Bạn có thể chọn một trong hai tùy theo sở thích.

> Lưu ý: Tải lại VSCode hoặc terminal để đảm bảo Python của môi trường ảo được sử dụng sau khi tạo môi trường ảo.

| Cách tiếp cận | Các bước |
| ------------- | -------- |
| Sử dụng `uv` | 1. Tạo môi trường ảo: `uv venv` <br>2. Chạy lệnh VSCode "***Python: Select Interpreter***" và chọn Python từ môi trường ảo đã tạo <br>3. Cài đặt các phụ thuộc (bao gồm phụ thuộc phát triển): `uv pip install -r pyproject.toml --extra dev` |
| Sử dụng `pip` | 1. Tạo môi trường ảo: `python -m venv .venv` <br>2. Chạy lệnh VSCode "***Python: Select Interpreter***" và chọn Python từ môi trường ảo đã tạo <br>3. Cài đặt các phụ thuộc (bao gồm phụ thuộc phát triển): `pip install -e .[dev]` | 

Sau khi thiết lập môi trường, bạn có thể chạy máy chủ trên máy phát triển cục bộ của mình thông qua Agent Builder làm MCP Client để bắt đầu:
1. Mở bảng điều khiển Debug của VS Code. Chọn `Debug in Agent Builder` hoặc nhấn `F5` để bắt đầu gỡ lỗi máy chủ MCP.
2. Sử dụng AI Toolkit Agent Builder để kiểm tra máy chủ với [lời nhắc này](../../../../../../../../../../../open_prompt_builder). Máy chủ sẽ tự động kết nối với Agent Builder.
3. Nhấn `Run` để kiểm tra máy chủ với lời nhắc.

**Chúc mừng**! Bạn đã chạy thành công Máy chủ MCP Thời tiết trên máy phát triển cục bộ của mình thông qua Agent Builder làm MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Những gì có trong mẫu

| Thư mục / Tệp | Nội dung                                     |
| ------------- | -------------------------------------------- |
| `.vscode`     | Các tệp VSCode để gỡ lỗi                    |
| `.aitk`       | Cấu hình cho AI Toolkit                     |
| `src`         | Mã nguồn cho máy chủ MCP thời tiết           |

## Cách gỡ lỗi Máy chủ MCP Thời tiết

> Lưu ý:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) là một công cụ phát triển trực quan để kiểm tra và gỡ lỗi các máy chủ MCP.
> - Tất cả các chế độ gỡ lỗi đều hỗ trợ điểm dừng, vì vậy bạn có thể thêm điểm dừng vào mã triển khai công cụ.

## Các công cụ có sẵn

### Công cụ Thời tiết
Công cụ `get_weather` cung cấp thông tin thời tiết giả lập cho một vị trí được chỉ định.

| Tham số | Loại | Mô tả |
| ------- | ---- | ----- |
| `location` | string | Vị trí để lấy thông tin thời tiết (ví dụ: tên thành phố, tiểu bang hoặc tọa độ) |

### Công cụ Clone Git
Công cụ `git_clone_repo` sao chép một kho lưu trữ git vào thư mục được chỉ định.

| Tham số | Loại | Mô tả |
| ------- | ---- | ----- |
| `repo_url` | string | URL của kho lưu trữ git để sao chép |
| `target_folder` | string | Đường dẫn đến thư mục nơi kho lưu trữ sẽ được sao chép |

Công cụ trả về một đối tượng JSON với:
- `success`: Boolean cho biết liệu thao tác có thành công hay không
- `target_folder` hoặc `error`: Đường dẫn của kho lưu trữ đã sao chép hoặc thông báo lỗi

### Công cụ Mở VS Code
Công cụ `open_in_vscode` mở một thư mục trong ứng dụng VS Code hoặc VS Code Insiders.

| Tham số | Loại | Mô tả |
| ------- | ---- | ----- |
| `folder_path` | string | Đường dẫn đến thư mục để mở |
| `use_insiders` | boolean (tùy chọn) | Có sử dụng VS Code Insiders thay vì VS Code thông thường hay không |

Công cụ trả về một đối tượng JSON với:
- `success`: Boolean cho biết liệu thao tác có thành công hay không
- `message` hoặc `error`: Một thông báo xác nhận hoặc thông báo lỗi

| Chế độ gỡ lỗi | Mô tả | Các bước gỡ lỗi |
| ------------- | ----- | --------------- |
| Agent Builder | Gỡ lỗi máy chủ MCP trong Agent Builder thông qua AI Toolkit. | 1. Mở bảng điều khiển Debug của VS Code. Chọn `Debug in Agent Builder` và nhấn `F5` để bắt đầu gỡ lỗi máy chủ MCP.<br>2. Sử dụng AI Toolkit Agent Builder để kiểm tra máy chủ với [lời nhắc này](../../../../../../../../../../../open_prompt_builder). Máy chủ sẽ tự động kết nối với Agent Builder.<br>3. Nhấn `Run` để kiểm tra máy chủ với lời nhắc. |
| MCP Inspector | Gỡ lỗi máy chủ MCP bằng MCP Inspector. | 1. Cài đặt [Node.js](https://nodejs.org/)<br> 2. Thiết lập Inspector: `cd inspector` && `npm install` <br> 3. Mở bảng điều khiển Debug của VS Code. Chọn `Debug SSE in Inspector (Edge)` hoặc `Debug SSE in Inspector (Chrome)`. Nhấn F5 để bắt đầu gỡ lỗi.<br> 4. Khi MCP Inspector khởi chạy trong trình duyệt, nhấn nút `Connect` để kết nối máy chủ MCP này.<br> 5. Sau đó bạn có thể `List Tools`, chọn một công cụ, nhập tham số, và `Run Tool` để gỡ lỗi mã máy chủ của bạn.<br> |

## Cổng mặc định và tùy chỉnh

| Chế độ gỡ lỗi | Cổng | Định nghĩa | Tùy chỉnh | Lưu ý |
| ------------- | ---- | ---------- | --------- | ----- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) để thay đổi các cổng trên. | N/A |
| MCP Inspector | 3001 (Máy chủ); 5173 và 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Chỉnh sửa [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) để thay đổi các cổng trên. | N/A |

## Phản hồi

Nếu bạn có bất kỳ phản hồi hoặc đề xuất nào cho mẫu này, vui lòng mở một vấn đề trên [kho lưu trữ GitHub của AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.