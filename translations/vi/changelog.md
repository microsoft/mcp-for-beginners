# Nhật ký thay đổi: Giáo trình MCP cho Người mới bắt đầu

Tài liệu này là hồ sơ ghi lại tất cả các thay đổi quan trọng được thực hiện đối với giáo trình Model Context Protocol (MCP) cho người mới bắt đầu. Các thay đổi được ghi lại theo thứ tự ngược thời gian (thay đổi mới nhất trước).

## Ngày 29 tháng 7 năm 2026

### Bài học bổ trợ Mô-đun 08 mới: Reliability Sidecars và Các lần thử lại an toàn

Thêm một bài học bổ trợ trung lập nhà cung cấp cho các công cụ MCP tạo ra các
hiệu ứng thực tế, phù hợp với đặc tả cuối cùng `2026-07-28`.

- **Mới**: [bài học bổ trợ reliability sidecar][reliability-sidecar]
  sử dụng một câu chuyện về vé hỗ trợ, hai sơ đồ Mermaid, và luồng quyết định thử lại
  để giải thích các khóa vận hành ổn định, chấp nhận bản sao nguyên tử,
  hòa giải, bằng chứng, và ranh giới mở rộng Tasks.
- **Mới**: Một bài tập tiêm lỗi Python và SQLite thư viện chuẩn
  sử dụng kho lưu trữ vận hành và vé riêng biệt để mô phỏng phản hồi bị mất
  sau khi một hiệu ứng ngoài cam kết. Sáu bài kiểm tra định sẵn bao gồm sao chép
  ngây thơ, phục hồi khởi động lại có bảo vệ, xung đột payload, kết quả được lưu
  trong bộ nhớ đệm, các tuyên bố đang hoạt động và chấp nhận bản sao đồng thời.
- **Cập nhật**: Mô-đun 08 hiện liên kết đến bài học bổ trợ, xác định
  mô hình yêu cầu không trạng thái cuối cùng `2026-07-28`, phân biệt OpenTelemetry
  observability với tính năng ghi nhật ký MCP đã bị loại bỏ, và giới hạn
  ví dụ thử lại tổng quát cho các thao tác chỉ đọc.
- **Tùy chọn**: Bài học ánh xạ các khái niệm có thể mang theo sang một bản
  triển khai cộng đồng được gắn thẻ mà không làm cho dịch vụ được lưu trữ hoặc
  cuộc gọi mạng trở thành một phần của bài tập.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## Ngày 2 tháng 7 năm 2026

### Bài học mới: Ứng viên phát hành đặc tả MCP 2026-07-28

Thêm phần bao quát về ứng viên phát hành đặc tả MCP `2026-07-28` sắp tới (được công bố ngày 21 tháng 5 năm 2026; dự kiến phát hành cuối cùng ngày 28 tháng 7 năm 2026), tóm tắt từ [bài đăng blog công bố chính thức](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Cơ sở giáo trình vẫn là **Đặc tả MCP 2025-11-25** cho đến khi phiên bản mới được phát hành, vì vậy đây được coi là hướng dẫn nhìn về phía trước thay vì viết lại các bài học hiện có.

- **Mới**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — một bài học đầy đủ bao gồm cốt lõi giao thức không trạng thái (loại bỏ bắt tay `initialize` và `Mcp-Session-Id`), các tiêu đề định tuyến mới `Mcp-Method`/`Mcp-Name`, siêu dữ liệu bộ nhớ đệm `ttlMs`/`cacheScope`, W3C Trace Context trong `_meta`, khuôn khổ Extensions chính thức (ứng dụng MCP và phần mở rộng Tasks mới), sáu SEP tăng cường bảo mật ủy quyền, việc loại bỏ Roots/Sampling/Logging, và chuyển sang JSON Schema 2020-12 đầy đủ cho các lược đồ công cụ.
- **Cập nhật** với các chú ý hướng tới tương lai liên kết đến bài học mới:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): ghi chú phiên bản giao thức, các phần Sampling/Roots/Logging/Tasks, và "Điều gì tiếp theo"
  - [02-Security/README.md](./02-Security/README.md): chú ý tăng cường ủy quyền
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): chú ý vận chuyển không trạng thái
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): chú ý việc loại bỏ Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): chú ý việc loại bỏ Logging và phần mở rộng Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): chú ý định tuyến không trạng thái/phiên
  - [README.md](./README.md): ghi chú "Nhìn về phía trước" trong phần đặc tả và mục nhập `1.1` mới trong bảng mô-đun giáo trình
  - [study_guide.md](./study_guide.md): điểm nhấn hướng tới tương lai dưới phần tổng quan Khái niệm Cốt lõi và ghi chú phụ đề ngày tháng
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): chú ý về bản đồ vận chuyển `mcp-session-id` trước mô hình yêu cầu không trạng thái
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): chú ý tổng quan mô-đun về việc loại bỏ Root Contexts/Sampling và phần mở rộng Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): chú ý tăng cường ủy quyền

## Ngày 24 tháng 6 năm 2026

### Bài học mới: Sử dụng MCP trong ứng dụng Copilot

- [Phần công cụ](./12-tooling/README.md) Thêm phần công cụ.
- [MCP trong ứng dụng Copilot](./12-tooling/01-copilot-app/README.md)

## Ngày 16 tháng 6 năm 2026

### Căn chỉnh đặc tả MCP & Xác thực mẫu

Đã xác thực giáo trình theo **Đặc tả MCP 2025-11-25** hiện tại và các SDK chính thức mới nhất, sau đó sửa các tham chiếu đặc tả lỗi thời còn lại và xác nhận các mẫu cốt lõi vẫn có thể xây dựng và chạy.

#### Sửa đổi phiên bản đặc tả (2025-06-18 / 2025-03-26 → 2025-11-25)

Cập nhật nội dung tiếng Anh nơi vẫn cho rằng một phiên bản đặc tả cũ hơn là tiêu chuẩn *hiện tại/mới nhất*, và chuyển hướng các liên kết tới các đường dẫn đặc tả chuẩn `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Cập nhật biểu ngữ "Tiêu Chuẩn Hiện Tại", phần giới thiệu, tiêu đề nguyên tắc bảo mật cốt lõi, tiêu đề yêu cầu bắt buộc, phần Microsoft Entra ID, các liên kết Tài liệu Tham khảo & Tài nguyên, và thông báo bảo mật cuối bài (8 tài liệu tham khảo) sang 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Cập nhật liên kết đặc tả Tài nguyên thêm và biểu ngữ "Tiêu Chuẩn Hiện Tại" sang 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Thay thế liên kết cũ `2025-03-26` về bảo mật và tin cậy bằng trang thực hành tốt nhất bảo mật 2025-11-25 hiện tại
- **03-GettingStarted/14-sampling/README.md**: Cập nhật liên kết tài liệu chính thức về sampling thành 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Đã cập nhật tham chiếu "đặc tả MCP hiện tại" ở thì hiện tại và liên kết Đặc tả Tài nguyên Bổ sung đến ngày 2025-11-25 (ghi chú lịch sử về việc ngưng dùng SSE được giữ nguyên để đảm bảo chính xác)

#### Kiểm tra mẫu với SDK Hiện tại

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` cài đặt được `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` không có lỗi kiểu — các API `McpServer`/`StdioServerTransport` hiện có vẫn hợp lệ
- **Python (03-GettingStarted/01-first-server/solution/python)**: Đã kiểm nghiệm trong môi trường `.venv` riêng biệt với `mcp[cli]` (1.27.2); `py_compile` thành công và `FastMCP.list_tools()` trả về chính xác các công cụ `add` và `subtract`
- Xác nhận tất cả các phiên bản phụ thuộc mẫu của `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) đều được phân giải chính xác thành `1.29.0` hiện tại mà không có thay đổi API phá vỡ

#### Canh Chỉnh Phiên Bản Phụ Thuộc (đóng các khoảng cách phiên bản)

Đã nâng các khóa SDK lỗi thời để mọi mẫu đều theo dõi phiên bản MCP hiện tại, phù hợp với quy ước chung trong repo:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Nâng `@modelcontextprotocol/sdk` từ `^1.8.0` → `>=1.26.0` và cập nhật mô tả gói lỗi thời `"updated for MCP 2025-06-18"` thành `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** và **lab4/code/github_mcp_server/pyproject.toml**: Nâng khóa chính xác `mcp==1.23.0` → `mcp>=1.26.0`; tái tạo lại cả hai file `uv.lock` (`uv lock`) để các file khóa được phân giải thành `mcp 1.27.2` hiện tại và đồng bộ với manifest

#### Phân Tích Khoảng Trống Chương Trình — Bao Phủ Tính Năng Đặc Tả Mới Nhất

Xác nhận chương trình đào tạo đã bao phủ tất cả các kiểu nguyên thủy được giới thiệu/mở rộng trong MCP 2025-11-25, do đó không còn khoảng trống nội dung:
- **Sampling**: Bài 03-GettingStarted/14-sampling và 05-AdvancedTopics/mcp-sampling
- **Elicitation (bao gồm chế độ URL)**: Được ghi lại trong 01-CoreConcepts và 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Được ghi lại trong 00-Introduction, 01-CoreConcepts, và 05-AdvancedTopics/mcp-root-contexts
- **Tasks (thử nghiệm, các thao tác chạy lâu dài)**: Được ghi lại trong 01-CoreConcepts và 05-AdvancedTopics/mcp-protocol-features
- **Chú Thích Công Cụ** (`readOnlyHint` / `destructiveHint`): Được ghi trong 01-CoreConcepts và 05-AdvancedTopics/mcp-protocol-features

### Tăng Cường Bảo Mật & Xử Lý Lỗ Hổng Phụ Thuộc

Đã quét bảo mật toàn bộ các tệp khai báo phụ thuộc và mã nguồn mẫu, sau đó xử lý tất cả cảnh báo npm được báo cáo và một lỗ hổng cấp mã. Sau khi xử lý, `npm audit` báo cáo **0 lỗ hổng** trong mọi thư mục được kiểm tra.

#### Lỗ Hổng Phụ Thuộc npm (gián tiếp) — Đã Sửa

Kiểm tra tất cả 15 tệp `package-lock.json` đã cam kết. Lỗ hổng chỉ giới hạn ở các phụ thuộc gián tiếp được kéo vào bởi công cụ phát triển MCP Inspector, client OpenAI, và MCP SDK; tất cả hiện đã được xử lý mà không làm hỏng các mẫu:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** và **lab3/code/weather_mcp/inspector**: Nâng `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), đã xử lý các cảnh báo `ajv`, `brace-expansion`, `diff`, `path-to-regexp` và `ws` có trong gói. Thêm mục `overrides` npm ép dùng bản vá `shell-quote@1.8.4` để loại bỏ cảnh báo nghiêm trọng còn lại do `concurrently` mang lại; tái tạo lại cả hai tệp khóa (hiện không còn lỗ hổng)
- **03-GettingStarted/samples/typescript**: `npm audit fix` cập nhật `qs` gián tiếp (mức độ trung bình) lên bản vá
- **03-GettingStarted/samples/javascript**: `npm audit fix` cập nhật `hono` gián tiếp (mức độ trung bình) lên bản vá
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` cập nhật `form-data` gián tiếp (mức độ cao) lên bản vá
- **03-GettingStarted/11-simple-auth/solution/typescript**: Đã tạo `package-lock.json` bị thiếu nên dự án có thể tái tạo và kiểm tra bảo mật (0 lỗ hổng)

#### Sửa Bảo Mật ở Cấp Mã (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Đã loại bỏ `shell=True` khỏi công cụ `open_in_vscode`. Trước đó `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` cho phép các ký tự điều khiển shell trong đường dẫn thư mục được `cmd.exe` hiểu nhầm (vấn đề tiêm lệnh). Hiện tại nó khởi chạy trực tiếp `Code.exe` đã được phân giải với thư mục làm đối số — không qua shell — chức năng tương đương và an toàn

#### Kiểm Tra Phụ Thuộc Python

- Kiểm tra tất cả bộ yêu cầu Python với `pip-audit`. `05-AdvancedTopics` và `03-GettingStarted/samples/python` báo cáo **không có lỗ hổng đã biết** (các phiên bản `mcp` / `httpx` / `pydantic` / `python-dotenv` của họ được phân giải thành các bản vá hiện tại)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` phát hiện phụ thuộc gián tiếp **`werkzeug` 3.1.1** với ba cảnh báo DoS tên thiết bị Windows trong hàm `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, và `CVE-2026-27199` (tất cả đã được sửa trong 3.1.6). Đã thêm khóa bảo mật rõ ràng `werkzeug>=3.1.6` để lấy phiên bản có bản vá; xác nhận ràng buộc phân giải sạch với stack `chainlit` / `mcp` / `semantic-kernel`

### Đổi Tên Thương Hiệu Sản Phẩm

Cập nhật toàn bộ nội dung chương trình phản ánh việc đổi tên thương hiệu sản phẩm của Microsoft:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Cập nhật liên kết cộng đồng Discord

- **AGENTS.md**: Cập nhật tham chiếu máy chủ Discord
- **README.md**: Cập nhật tham chiếu hệ sinh thái công nghệ
- **study_guide.md**: Cập nhật tham chiếu nghiên cứu tình huống
- **05-AdvancedTopics/README.md**: Cập nhật tiêu đề và mô tả Mô-đun 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Cập nhật tiêu đề phần và mô tả
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Cập nhật đầy đủ tiêu đề và nội dung mô-đun
- **05-AdvancedTopics/mcp-security-entra/README.md**: Cập nhật liên kết tham chiếu chéo
- **07-LessonsfromEarlyAdoption/README.md**: Cập nhật tham chiếu nghiên cứu tình huống
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Cập nhật tiêu đề Phần 9, huy hiệu và năng lực
- **08-BestPractices/README.md**: Cập nhật liên kết cộng đồng Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Cập nhật tham chiếu kênh Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Cập nhật tham chiếu triển khai mô hình
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Cập nhật bảng Dịch vụ AI
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Cập nhật tham chiếu tài nguyên

#### Bộ công cụ AI / AITK → Mở rộng Bộ công cụ Foundry của Microsoft cho VS Code
- **README.md**: Cập nhật tham chiếu chương trình học chính
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Cập nhật tiêu đề mô-đun, tổng quan và tất cả tiêu đề mô-đun
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Cập nhật tiêu đề, mục tiêu học tập, hướng dẫn thiết lập và tài nguyên
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Cập nhật tiêu đề, mục tiêu học tập, bảng máy chủ MCP và tham chiếu chéo
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Cập nhật tiêu đề, huy hiệu, điều kiện tiên quyết và tài nguyên
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Cập nhật tham chiếu Trình xây dựng Agent và liên kết phản hồi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Cập nhật điều kiện tiên quyết và tham chiếu tiện ích mở rộng

---

## Ngày 11 tháng 4, 2026

### Bài học mới, Sửa lỗi tài liệu và Cập nhật phụ thuộc

#### Thêm Nội dung Chương trình Mới

**Mô-đun 05 - Chủ đề Nâng cao**
- **Bài học 5.17: Lập luận Đối kháng đa tác nhân với MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Hướng dẫn toàn diện mới bao gồm mô hình tranh luận đối kháng cho hệ thống đa tác nhân
  - Sơ đồ kiến trúc Mermaid: hai tác nhân → máy chủ MCP chia sẻ → bản ghi tranh luận → trọng tài → phán quyết
  - Máy chủ công cụ MCP chia sẻ (`web_search` + `run_python`) được triển khai bằng Python và TypeScript
  - Các đề bài hệ thống đối lập (CHO / CHỐNG / Trọng tài) với yêu cầu sử dụng công cụ rõ ràng
  - Bộ điều phối tranh luận bằng Python, TypeScript và C# quản lý vòng và phân phối luận điểm
  - Kết nối MCP `ClientSession` cho bộ điều phối gọi các công cụ thực tế
  - Bảng trường hợp sử dụng (phát hiện ảo giác, mô hình nguy cơ, rà soát thiết kế API, xác minh sự thật, lựa chọn công nghệ)
  - Cân nhắc bảo mật: thực thi trong sandbox, xác thực gọi công cụ, giới hạn tần suất, ghi nhật ký kiểm toán
  - Bài tập có cấu trúc với ba kịch bản thực tế (đánh giá mã, quyết định kiến trúc, kiểm duyệt nội dung)

#### Sửa lỗi Tài liệu

**Mô-đun 03 - Bắt đầu**
- **05-stdio-server/README.md**: Sửa ví dụ máy chủ stdio TypeScript chưa hoàn chỉnh — thêm thiếu khởi tạo transport (`new StdioServerTransport()`) và gọi `server.connect(transport)` để khớp với các ví dụ Python và .NET cùng phần
- **14-sampling/README.md**: Sửa lỗi chính tả — sửa `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Cập nhật Chương trình học

**README.md chính**
- Thêm mục 5.17 (Lập luận Đối kháng đa tác nhân với MCP) vào bảng chương trình với liên kết trực tiếp đến bài học mới

**05-AdvancedTopics/README.md**
- Thêm dòng bài học 5.17 vào bảng bài học

**study_guide.md**
- Thêm chủ đề Lập luận Đối kháng đa tác nhân vào bản đồ tư duy và mô tả văn bản Chủ đề Nâng cao

#### Sửa lỗi Mã và Bảo mật

**Mô-đun 05 - Tác nhân Đối kháng (`mcp-adversarial-agents`)**
- **Sửa lỗi bảo mật — tiêm lệnh**: Thay thế nội suy shell `execSync` bằng `execFile` + `promisify` trong công cụ `run_python` TypeScript, loại bỏ bề mặt tiêm lệnh (mã do LLM kiểm soát giờ được truyền làm phần tử argv chữ ký, không qua shell)
- **Kết nối vòng lặp công cụ MCP**: Cập nhật bộ điều phối tranh luận Python sử dụng client `AsyncAnthropic` (thay cho `Anthropic` đồng bộ chặn), truyền trực tiếp `ClientSession` cho mỗi lượt tác nhân, lấy định nghĩa công cụ qua `session.list_tools()` mỗi lượt, và phân phối các khối `tool_use` qua `session.call_tool()` trong vòng lặp đến khi mô hình phát ra phản hồi văn bản cuối cùng

#### Cập nhật Phụ thuộc

- Nâng cấp `hono` lên 4.12.12 cho nhiều gói (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Nâng cấp `@hono/node-server` từ 1.19.11 lên 1.19.13 trong các gói TypeScript
- Nâng cấp `cryptography` từ 46.0.5 lên 46.0.7 trong các gói Python (phòng lab 3 và 4 của 10-StreamliningAIWorkflows)
- Nâng cấp `lodash` từ 4.17.23 lên 4.18.1 trong trình kiểm tra 10-StreamliningAIWorkflows

#### Bản Dịch

- Đồng bộ hóa bản dịch cho hơn 48 ngôn ngữ với các thay đổi nguồn mới nhất (cập nhật i18n)

---

## Ngày 5 tháng 2, 2026

### Cải tiến Xác thực và Dẫn hướng trên Toàn bộ Kho lưu trữ

#### Thêm Nội dung Chương trình Mới

**Mô-đun 03 - Bắt đầu**
- **12-mcp-hosts/README.md**: Hướng dẫn toàn diện mới thiết lập máy chủ MCP
  - Ví dụ cấu hình Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Mẫu cấu hình JSON cho tất cả máy chủ chính
  - Bảng so sánh loại transport (stdio, SSE/HTTP, WebSocket)
  - Khắc phục sự cố kết nối phổ biến
  - Thực hành bảo mật tốt nhất cho cấu hình máy chủ

- **13-mcp-inspector/README.md**: Hướng dẫn gỡ lỗi MCP Inspector mới
  - Các phương pháp cài đặt (npx, npm global, từ mã nguồn)
  - Kết nối với máy chủ qua stdio và HTTP/SSE
  - Công cụ thử nghiệm, tài nguyên và quy trình nhắc nhở
  - Tích hợp VS Code với MCP Inspector
  - Kịch bản gỡ lỗi phổ biến với giải pháp

**Mô-đun 04 - Triển khai Thực tiễn**
- **pagination/README.md**: Hướng dẫn triển khai phân trang mới
  - Các mẫu phân trang dựa trên con trỏ trong Python, TypeScript, Java
  - Xử lý phân trang phía khách
  - Chiến lược thiết kế con trỏ (đặc, cấu trúc)
  - Khuyến nghị tối ưu hiệu năng

**Mô-đun 05 - Chủ đề Nâng cao**
- **mcp-protocol-features/README.md**: Phân tích sâu về tính năng giao thức mới
  - Triển khai thông báo tiến trình
  - Các mẫu hủy yêu cầu
  - Mẫu tài nguyên với URI
  - Quản lý vòng đời máy chủ
  - Kiểm soát mức độ ghi log
  - Mẫu xử lý lỗi với mã JSON-RPC

#### Sửa Dẫn hướng (cập nhật hơn 24 tệp)

**README chính của các Mô-đun**
 Hiện liên kết đến bài học đầu tiên VÀ mô-đun kế tiếp

**Tệp Phụ bảo mật 02-Security**
- Tất cả 5 tài liệu bổ trợ bảo mật hiện có phần "Tiếp theo là gì" để dẫn hướng:

**09-CaseStudy Các Tệp**
- Tất cả tệp nghiên cứu tình huống hiện có dẫn hướng tuần tự:

**Phòng Thí nghiệm 10-StreamliningAI**
Thêm phần Tiếp theo là gì cho Tổng quan Mô-đun 10 và Mô-đun 11

#### Sửa Mã và Nội dung

**Cập Nhật SDK và Phụ Thuộc**
Sửa phiên bản openai trống thành `^4.95.0`
Cập nhật SDK từ `^1.8.0` lên `>=1.26.0`
Cập nhật phiên bản mcp được ghim thành `>=1.26.0`

**Sửa Mã**
Sửa mẫu mô hình không hợp lệ `gpt-4o-mini` thành `gpt-4.1-mini`

**Sửa Nội dung**
Sửa liên kết hỏng `READMEmd` → `README.md`, sửa tiêu đề chương trình `Module 1-3` → `Module 0-3`, sửa đường dẫn phân biệt chữ hoa chữ thường
Xóa nội dung trùng lặp bị hỏng của Nghiên cứu Tình huống 5

**Cải thiện Hướng dẫn cho Người mới**
Thêm phần giới thiệu thích hợp, mục tiêu học tập và điều kiện tiên quyết cho người mới

#### Cập nhật Chương trình học

**README.md chính**
- Thêm các mục 3.12 (Máy chủ MCP), 3.13 (MCP Inspector), 4.1 (Phân trang), 5.16 (Tính năng Giao thức) vào bảng chương trình học

**README các Mô-đun**
Thêm bài 12 và 13 vào danh sách bài học
Thêm phần Hướng dẫn Thực hành với liên kết phân trang
Thêm bài 5.15 (Điều khiển Transport Tuỳ chỉnh) và 5.16 (Tính năng Giao thức)

**study_guide.md**
- Cập nhật bản đồ tư duy với tất cả các chủ đề mới: Thiết lập Máy chủ MCP, MCP Inspector, Chiến lược Phân trang, Phân tích sâu Tính năng Giao thức

## Ngày 28 tháng 1, 2026

### Đánh giá Tuân thủ Đặc tả MCP 2025-11-25

#### Nâng cao Khái niệm Cốt lõi (01-CoreConcepts/)
- **Đơn vị khách hàng mới - Roots**: Thêm tài liệu toàn diện về đơn vị khách hàng Roots, cho phép máy chủ hiểu ranh giới hệ thống tệp và quyền truy cập
- **Chú thích Công cụ**: Thêm tài liệu về chú thích hành vi công cụ (`readOnlyHint`, `destructiveHint`) để quyết định chạy công cụ tốt hơn
- **Gọi công cụ trong Sampling**: Cập nhật tài liệu Sampling bao gồm tham số `tools` và `toolChoice` cho việc gọi công cụ theo mô hình khi yêu cầu sampling
- **Kích hoạt Chế độ URL**: Thêm tài liệu về kích hoạt tương tác web bên ngoài do máy chủ khởi tạo qua URL
- **Nhiệm vụ (thử nghiệm)**: Thêm phần mới tài liệu về tính năng Nhiệm vụ thử nghiệm cho bao bọc thực thi bền và truy xuất kết quả trì hoãn
- **Hỗ trợ Biểu tượng**: Ghi chú rằng công cụ, tài nguyên, mẫu tài nguyên và nhắc giờ có thể bao gồm biểu tượng như siêu dữ liệu thêm

#### Cập nhật Tài liệu
- **README.md**: Thêm tham chiếu phiên bản Đặc tả MCP 2025-11-25 và giải thích phiên bản dựa trên ngày
- **study_guide.md**: Cập nhật sơ đồ chương trình bao gồm Nhiệm vụ và Chú thích Công cụ trong phần Khái niệm Cốt lõi; cập nhật dấu thời gian tài liệu

#### Xác minh Tuân thủ Đặc tả
- **Phiên bản Giao thức**: Xác nhận tất cả tài liệu tham chiếu Đặc tả MCP 2025-11-25 hiện hành
- **Căn chỉnh Kiến trúc**: Xác nhận chính xác tài liệu kiến trúc hai lớp (Lớp Dữ liệu + Lớp Vận chuyển)
- **Tài liệu Đơn vị**: Xác minh đơn vị máy chủ (Tài nguyên, Nhắc, Công cụ) và đơn vị khách (Sampling, Elicitation, Ghi nhật ký, Roots)
- **Cơ chế Vận chuyển**: Xác nhận chính xác tài liệu giao thức STDIO và HTTP có thể truyền
- **Hướng dẫn Bảo mật**: Xác nhận phù hợp với Tài liệu Thực hành Bảo mật Tốt nhất MCP hiện hành

#### Tính năng MCP 2025-11-25 Chính được Ghi lại
- **Khám phá OpenID Connect**: Khám phá máy chủ xác thực qua OIDC
- **Tài liệu Metadata ID Khách OAuth**: Cơ chế đăng ký khách được đề xuất
- **JSON Schema 2020-12**: Ngôn ngữ chuẩn mặc định cho định nghĩa schema MCP
- **Hệ Thống Tầng SDK**: Quy định chính thức yêu cầu hỗ trợ và duy trì tính năng SDK
- **Cấu trúc Quản trị**: Quy định chính thức Nhóm Công tác và Nhóm Quan tâm trong quản trị MCP

### Cập nhật Lớn Tài liệu Bảo mật (02-Security/)

#### Tích hợp Hội thảo MCP Security Summit (Sherpa)
- **Tài nguyên đào tạo thực hành mới**: Thêm tích hợp toàn diện với [Hội thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) trên tất cả tài liệu bảo mật
- **Theo dõi tuyến đường hành trình**: Tài liệu chi tiết tiến trình từ Trại Cơ sở đến Đỉnh Hội nghị
- **Căn chỉnh OWASP**: Tất cả hướng dẫn bảo mật hiện phù hợp với rủi ro Hướng dẫn bảo mật MCP Azure OWASP

#### Tích hợp OWASP MCP Top 10
- **Mục mới**: Thêm bảng Rủi ro bảo mật OWASP MCP Top 10 với biện pháp Azure vào README Bảo mật chính
- **Tài liệu dựa trên rủi ro**: Cập nhật mcp-security-controls-2025.md với tham chiếu rủi ro OWASP MCP cho từng lĩnh vực bảo mật
- **Kiến trúc Tham khảo**: Liên kết tới kiến trúc tham khảo và mẫu triển khai trong Hướng dẫn Bảo mật MCP Azure OWASP

#### Cập nhật Tệp Bảo mật
- **README.md**: Thêm tổng quan Hội thảo Sherpa, bảng tuyến đường hành trình, tóm tắt rủi ro OWASP MCP Top 10 và phần đào tạo thực hành
- **mcp-security-controls-2025.md**: Cập nhật tiêu đề tháng 2 năm 2026, thêm tham chiếu rủi ro OWASP (MCP01-MCP08), sửa lỗi không nhất quán phiên bản đặc tả
- **mcp-security-best-practices-2025.md**: Thêm phần tài nguyên Sherpa và OWASP, cập nhật dấu thời gian
- **mcp-best-practices.md**: Thêm phần đào tạo thực hành với liên kết Sherpa và OWASP
- **azure-content-safety-implementation.md**: Thêm tham chiếu OWASP MCP06, căn chỉnh Camp 3 Sherpa và phần tài nguyên thêm

#### Thêm Liên kết Tài nguyên Mới
- [Hội thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)

- [Hướng dẫn bảo mật OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Các trang rủi ro OWASP MCP cá nhân (MCP01-MCP10)

### Căn chỉnh Khung Chương Trình MCP Toàn diện 2025-11-25

#### Module 03 - Bắt đầu
- **Tài liệu SDK**: Thêm Go SDK vào danh sách SDK chính thức; cập nhật tất cả tham chiếu SDK để đồng bộ với MCP Specification 2025-11-25
- **Làm rõ Giao thức Truyền tải**: Cập nhật mô tả giao thức STDIO và HTTP Streaming với tham chiếu rõ ràng đến đặc tả

#### Module 04 - Triển khai Thực tiễn
- **Cập nhật SDK**: Thêm Go SDK; cập nhật danh sách SDK kèm tham chiếu phiên bản đặc tả
- **Đặc tả Ủy quyền**: Cập nhật liên kết đặc tả MCP Authorization thành phiên bản 2025-11-25 hiện tại

#### Module 05 - Chủ đề Nâng cao
- **Tính năng Mới**: Thêm ghi chú về các tính năng mới trong MCP Specification 2025-11-25 (Tác vụ, Chú thích công cụ, Phương thức Gợi ý URL, Gốc)
- **Tài nguyên Bảo mật**: Thêm liên kết OWASP MCP Top 10 và hội thảo Sherpa vào tài liệu tham khảo bổ sung

#### Module 06 - Đóng góp Cộng đồng
- **Danh sách SDK**: Thêm Swift và Rust SDK; cập nhật liên kết đặc tả lên 2025-11-25
- **Tham chiếu Đặc tả**: Cập nhật liên kết MCP Specification thành URL đặc tả trực tiếp

#### Module 07 - Bài học từ việc áp dụng sớm
- **Cập nhật Tài nguyên**: Thêm liên kết MCP Specification 2025-11-25 và OWASP MCP Top 10 vào tài nguyên bổ sung

#### Module 08 - Thực hành Tốt nhất
- **Phiên bản Đặc tả**: Cập nhật tham chiếu MCP Specification đến 2025-11-25
- **Tài nguyên Bảo mật**: Thêm OWASP MCP Top 10 và hội thảo Sherpa vào tài liệu tham khảo bổ sung

#### Module 10 - Tinh giản Quy trình AI
- **Cập nhật Huy hiệu**: Thay đổi huy hiệu phiên bản MCP từ phiên bản SDK (1.9.3) sang phiên bản đặc tả (2025-11-25)
- **Liên kết Tài nguyên**: Cập nhật liên kết MCP Specification; thêm OWASP MCP Top 10

#### Module 11 - MCP Server Thực hành tại chỗ
- **Tham chiếu Đặc tả**: Cập nhật liên kết MCP Specification thành phiên bản 2025-11-25
- **Tài nguyên Bảo mật**: Thêm OWASP MCP Top 10 vào tài nguyên chính thức

## 18 tháng 12, 2025

### Cập nhật Tài liệu Bảo mật - MCP Specification 2025-11-25

#### Thực hành Bảo mật MCP tốt nhất (02-Security/mcp-best-practices.md) - Cập nhật Phiên bản Đặc tả
- **Cập nhật Phiên bản Giao thức**: Chỉ định đến MCP Specification mới nhất 2025-11-25 (phát hành ngày 25 tháng 11 năm 2025)
  - Cập nhật tất cả tham chiếu phiên bản đặc tả từ 2025-06-18 sang 2025-11-25
  - Cập nhật ngày tài liệu từ 18 tháng 8 năm 2025 thành 18 tháng 12 năm 2025
  - Đảm bảo tất cả URL đặc tả trỏ đến tài liệu hiện tại
- **Xác thực Nội dung**: Kiểm tra toàn diện các thực hành bảo mật tốt nhất so với tiêu chuẩn mới nhất
  - **Giải pháp Bảo mật Microsoft**: Xác nhận thuật ngữ và liên kết hiện tại cho Prompt Shields (trước đây "phát hiện rủi ro jailbreak"), Azure Content Safety, Microsoft Entra ID và Azure Key Vault
  - **Bảo mật OAuth 2.1**: Xác nhận phù hợp với thực hành bảo mật OAuth mới nhất
  - **Tiêu chuẩn OWASP**: Đảm bảo tham chiếu OWASP Top 10 cho LLMs vẫn còn hiệu lực
  - **Dịch vụ Azure**: Xác minh tất cả liên kết tài liệu Microsoft Azure và thực hành tốt nhất
- **Phù hợp Tiêu chuẩn**: Xác nhận tất cả tiêu chuẩn bảo mật được tham chiếu là hiện tại
  - Khung Quản lý Rủi ro AI của NIST
  - ISO 27001:2022
  - Thực hành Bảo mật OAuth 2.1
  - Khung bảo mật và tuân thủ Azure
- **Tài nguyên Triển khai**: Kiểm tra tất cả liên kết hướng dẫn và tài nguyên triển khai
  - Mẫu chứng thực Azure API Management
  - Hướng dẫn tích hợp Microsoft Entra ID
  - Quản lý bí mật Azure Key Vault
  - Pipeline và giải pháp giám sát DevSecOps

### Đảm bảo Chất lượng Tài liệu
- **Tuân thủ Đặc tả**: Đảm bảo tất cả yêu cầu bảo mật MCP bắt buộc (MUST/MUST NOT) phù hợp với đặc tả mới nhất
- **Tính Cập nhật Tài nguyên**: Xác minh tất cả liên kết bên ngoài với tài liệu Microsoft, tiêu chuẩn bảo mật và hướng dẫn triển khai
- **Phủ rộng Thực hành Tốt nhất**: Xác nhận bao phủ toàn diện các chủ đề xác thực, ủy quyền, mối đe dọa AI đặc thù, bảo mật chuỗi cung ứng và mẫu doanh nghiệp

## 6 tháng 10, 2025

### Mở rộng phần Bắt đầu – Sử dụng Server Nâng cao & Xác thực Đơn giản

#### Sử dụng Server Nâng cao (03-GettingStarted/10-advanced)
- **Thêm Chương Mới**: Giới thiệu hướng dẫn toàn diện về sử dụng server MCP nâng cao, khai thác cả kiến trúc server thông thường và cấp thấp.
  - **Server Thông thường vs. Cấp thấp**: So sánh chi tiết và ví dụ mã Python và TypeScript cho cả hai phương pháp.
  - **Thiết kế Dựa trên Handler**: Giải thích quản lý công cụ/tài nguyên/prompt dựa trên handler cho triển khai server có thể mở rộng, linh hoạt.
  - **Mẫu Thực tiễn**: Kịch bản thực tế nơi các mẫu server cấp thấp có lợi cho các tính năng và kiến trúc nâng cao.

#### Xác thực Đơn giản (03-GettingStarted/11-simple-auth)
- **Thêm Chương Mới**: Hướng dẫn từng bước thực hiện xác thực đơn giản trong các server MCP.
  - **Khái niệm Xác thực**: Giải thích rõ ràng về xác thực so với ủy quyền, và xử lý thông tin đăng nhập.
  - **Triển khai Xác thực Cơ bản**: Mẫu xác thực dựa trên middleware trong Python (Starlette) và TypeScript (Express), kèm ví dụ mã.
  - **Tiến tới Bảo mật Nâng cao**: Hướng dẫn bắt đầu với xác thực đơn giản và tiến tới OAuth 2.1 và RBAC, kèm tham chiếu đến các module bảo mật nâng cao.

Các bổ sung này cung cấp hướng dẫn thực tiễn, thực tế để xây dựng các triển khai server MCP mạnh mẽ, bảo mật và linh hoạt hơn, kết nối các khái niệm nền tảng với các mẫu sản xuất nâng cao.

## 29 tháng 9, 2025

### Labs Tích hợp Cơ sở dữ liệu MCP Server - Lộ trình học thực hành toàn diện

#### 11-MCPServerHandsOnLabs - Khung chương trình tích hợp cơ sở dữ liệu hoàn chỉnh mới
- **Lộ trình Học 13 Lab Hoàn chỉnh**: Thêm khung chương trình thực hành toàn diện để xây dựng các server MCP sẵn sàng sản xuất tích hợp cơ sở dữ liệu PostgreSQL
  - **Triển khai Thực tế**: Trường hợp sử dụng phân tích bán lẻ Zava minh họa mẫu lực doanh nghiệp
  - **Trình tự Học Cấu trúc**:
    - **Lab 00-03: Nền tảng** - Giới thiệu, Kiến trúc Cốt lõi, Bảo mật & Đa người thuê, Thiết lập Môi trường
    - **Lab 04-06: Xây dựng MCP Server** - Thiết kế Cơ sở dữ liệu & Lược đồ, Triển khai MCP Server, Phát triển Công cụ  
    - **Lab 07-09: Tính năng Nâng cao** - Tích hợp Tìm kiếm Ngữ nghĩa, Kiểm thử & Gỡ lỗi, Tích hợp VS Code
    - **Lab 10-12: Sản xuất & Thực hành Tốt nhất** - Chiến lược Triển khai, Giám sát & Quan sát, Thực hành tốt & Tối ưu hóa
  - **Công nghệ Doanh nghiệp**: Khung FastMCP, PostgreSQL với pgvector, nhúng Azure OpenAI, Azure Container Apps, Application Insights
  - **Tính năng Nâng cao**: Bảo mật Cấp hàng (RLS), tìm kiếm ngữ nghĩa, truy cập dữ liệu đa thuê, nhúng vector, giám sát thời gian thực

#### Chuẩn hóa Thuật ngữ - Chuyển đổi Module sang Lab
- **Cập nhật Tài liệu Toàn diện**: Hệ thống cập nhật tất cả các file README trong 11-MCPServerHandsOnLabs sử dụng thuật ngữ "Lab" thay cho "Module"
  - **Tiêu đề Phần**: Cập nhật "Nội dung Module này" thành "Nội dung Lab này" trên tất cả 13 lab
  - **Mô tả Nội dung**: Thay đổi câu "Module này cung cấp..." thành "Lab này cung cấp..." xuyên suốt tài liệu
  - **Mục tiêu Học tập**: Cập nhật "Vào cuối module này..." thành "Vào cuối lab này..."
  - **Liên kết Điều hướng**: Chuyển đổi tất cả tham chiếu "Module XX:" thành "Lab XX:" trong tham chiếu chéo và điều hướng
  - **Theo dõi Hoàn thành**: Cập nhật "Sau khi hoàn thành module này..." thành "Sau khi hoàn thành lab này..."
  - **Giữ nguyên Tham chiếu Kỹ thuật**: Duy trì tham chiếu module Python trong các file cấu hình (ví dụ, `"module": "mcp_server.main"`)

#### Cải tiến Hướng dẫn Học tập (study_guide.md)
- **Bản đồ Khung Chương Trình Hình ảnh**: Thêm phần mới "11. Labs Tích hợp Cơ sở dữ liệu" với hình dung cấu trúc lab toàn diện
- **Cấu trúc Kho Lưu trữ**: Cập nhật từ mười lên mười một phần chính với mô tả chi tiết cho 11-MCPServerHandsOnLabs
- **Hướng dẫn Lộ trình Học tập**: Nâng cấp hướng dẫn điều hướng phủ các phần 00-11
- **Phủ Công nghệ**: Thêm chi tiết về FastMCP, PostgreSQL, tích hợp dịch vụ Azure
- **Kết quả Học tập**: Nhấn mạnh phát triển server sản xuất, mẫu tích hợp cơ sở dữ liệu và bảo mật doanh nghiệp

#### Cải thiện cấu trúc README Chính
- **Thuật ngữ dựa trên Lab**: Cập nhật README.md chính trong 11-MCPServerHandsOnLabs sử dụng nhất quán cấu trúc "Lab"
- **Tổ chức Lộ trình Học**: Trình tự rõ ràng từ khái niệm nền tảng đến triển khai nâng cao và sản xuất
- **Tập trung Thực tế**: Nhấn mạnh học tập thực hành, với các mẫu và công nghệ doanh nghiệp

### Cải tiến Chất lượng và Tính nhất quán Tài liệu
- **Nhấn mạnh Học tập Thực hành**: Tăng cường phương pháp học dựa trên lab xuyên suốt tài liệu
- **Tập trung Mẫu Doanh nghiệp**: Nổi bật các triển khai sẵn sàng sản xuất và cân nhắc bảo mật doanh nghiệp
- **Tích hợp Công nghệ**: Phủ sóng toàn diện về dịch vụ Azure hiện đại và mẫu tích hợp AI
- **Trình tự Học**: Lộ trình rõ ràng, có cấu trúc từ khái niệm cơ bản đến triển khai sản xuất

## 26 tháng 9, 2025

### Cải tiến Nghiên cứu Trường hợp - Tích hợp GitHub MCP Registry

#### Nghiên cứu Trường hợp (09-CaseStudy/) - Tập trung Phát triển Hệ sinh thái
- **README.md**: Mở rộng lớn với nghiên cứu trường hợp toàn diện về GitHub MCP Registry
  - **Nghiên cứu trường hợp GitHub MCP Registry**: Nghiên cứu chi tiết về việc khởi động MCP Registry của GitHub vào tháng 9 năm 2025
    - **Phân tích Vấn đề**: Khảo sát chi tiết các thách thức phân mảnh trong khám phá và triển khai server MCP
    - **Kiến trúc Giải pháp**: Phương pháp registry tập trung của GitHub với cài đặt VS Code chỉ bằng một cú nhấp
    - **Tác động Kinh doanh**: Cải thiện đo lường hiệu quả onboarding và năng suất nhà phát triển
    - **Giá trị Chiến lược**: Tập trung vào triển khai agent mô-đun và khả năng tương tác công cụ chéo
    - **Phát triển Hệ sinh thái**: Định vị như nền tảng nền tảng cho tích hợp agentic
  - **Cấu trúc Nghiên cứu Trường hợp Nâng cao**: Cập nhật bảy nghiên cứu trường hợp với định dạng nhất quán và mô tả toàn diện
    - Azure AI Travel Agents: Tập trung điều phối đa agent
    - Tích hợp Azure DevOps: Tập trung tự động hóa quy trình làm việc
    - Truy xuất Tài liệu Thời gian Thực: Triển khai client console Python
    - Trình tạo Kế hoạch Học Tương tác: Ứng dụng web trò chuyện Chainlit
    - Tài liệu Trong Trình soạn thảo: Tích hợp VS Code và GitHub Copilot
    - Quản lý API Azure: Mẫu tích hợp API doanh nghiệp
    - GitHub MCP Registry: Phát triển hệ sinh thái và nền tảng cộng đồng
  - **Kết luận Toàn diện**: Viết lại phần kết luận nhấn mạnh bảy nghiên cứu trường hợp trải rộng nhiều khía cạnh triển khai MCP
    - Tích hợp Doanh nghiệp, Điều phối Đa-Agent, Năng suất Nhà phát triển
    - Phát triển Hệ sinh thái, Phân loại Ứng dụng Giáo dục
    - Nâng cao hiểu biết về các mẫu kiến trúc, chiến lược triển khai và thực hành tốt nhất
    - Nhấn mạnh MCP như giao thức trưởng thành, sẵn sàng sản xuất

#### Cập nhật Hướng dẫn Học tập (study_guide.md)
- **Bản đồ Khung Chương Trình Hình ảnh**: Cập nhật sơ đồ tư duy để bao gồm GitHub MCP Registry trong phần Nghiên cứu trường hợp
- **Mô tả Nghiên cứu Trường hợp**: Nâng cao từ mô tả chung chung sang phân tích chi tiết bảy nghiên cứu trường hợp toàn diện
- **Cấu trúc Kho Lưu trữ**: Cập nhật phần 10 phản ánh phạm vi nghiên cứu trường hợp toàn diện với chi tiết triển khai cụ thể
- **Tích hợp Nhật ký Thay đổi**: Thêm mục ngày 26 tháng 9 năm 2025 ghi nhận bổ sung GitHub MCP Registry và cải thiện nghiên cứu trường hợp
- **Cập nhật Ngày**: Cập nhật dấu thời gian chân trang phản ánh bản sửa đổi mới nhất (26 tháng 9, 2025)

### Cải thiện Chất lượng Tài liệu
- **Tăng cường Tính nhất quán**: Chuẩn hóa định dạng và cấu trúc nghiên cứu trường hợp trên tất cả bảy ví dụ
- **Phủ sóng Toàn diện**: Nghiên cứu trường hợp bây giờ bao phủ doanh nghiệp, năng suất nhà phát triển và các kịch bản phát triển hệ sinh thái
- **Định vị Chiến lược**: Tập trung nâng cao về MCP như nền tảng nền tảng cho triển khai hệ thống agentic
- **Tích hợp Tài nguyên**: Cập nhật tài nguyên bổ sung bao gồm liên kết GitHub MCP Registry

## 15 tháng 9, 2025

### Mở rộng Chủ đề Nâng cao - Giao thức Tùy chỉnh & Kỹ thuật Ngữ cảnh

#### MCP Giao thức Tùy chỉnh (05-AdvancedTopics/mcp-transport/) - Hướng dẫn Triển khai Nâng cao Mới
- **README.md**: Hướng dẫn triển khai đầy đủ cho các cơ chế giao thức MCP tùy chỉnh
  - **Giao thức Azure Event Grid**: Triển khai giao thức không máy chủ dựa trên sự kiện toàn diện
    - Ví dụ C#, TypeScript và Python tích hợp Azure Functions
    - Các mẫu kiến trúc hướng sự kiện cho giải pháp MCP có thể mở rộng
    - Bộ nhận webhook và xử lý tin nhắn đẩy
  - **Giao thức Azure Event Hubs**: Triển khai giao thức luồng truyền tải hiệu suất cao
    - Khả năng streaming thời gian thực cho kịch bản độ trễ thấp
    - Chiến lược phân vùng và quản lý checkpoint
    - Tổng hợp tin nhắn và tối ưu hiệu suất
  - **Mẫu Tích hợp Doanh nghiệp**: Ví dụ kiến trúc sẵn sàng sản xuất
    - Xử lý MCP phân tán qua nhiều Azure Functions
    - Kiến trúc giao thức lai kết hợp nhiều loại giao thức
    - Chiến lược độ bền, độ tin cậy và xử lý lỗi tin nhắn
  - **Bảo mật & Giám sát**: Tích hợp Azure Key Vault và mẫu quan sát
    - Xác thực danh tính quản lý và quyền truy cập tối thiểu
    - Telemetry Application Insights và giám sát hiệu suất
    - Bộ ngắt mạch và mẫu chịu lỗi
  - **Khung Kiểm thử**: Chiến lược kiểm thử toàn diện cho giao thức tùy chỉnh
    - Kiểm thử đơn vị với test doubles và khung giả lập
    - Kiểm thử tích hợp với Azure Test Containers
    - Xem xét kiểm thử hiệu suất và tải

#### Kỹ thuật Ngữ cảnh (05-AdvancedTopics/mcp-contextengineering/) - Lĩnh vực AI Mới Nổi
- **README.md**: Khám phá toàn diện kỹ thuật ngữ cảnh như một lĩnh vực mới nổi
  - **Nguyên lý Cốt lõi**: Chia sẻ ngữ cảnh đầy đủ, nhận thức quyết định hành động và quản lý cửa sổ ngữ cảnh

  - **Căn chỉnh Giao thức MCP**: Cách thiết kế MCP giải quyết các thách thức trong kỹ thuật ngữ cảnh
    - Giới hạn cửa sổ ngữ cảnh và chiến lược tải dần
    - Xác định tính liên quan và truy xuất ngữ cảnh động
    - Xử lý ngữ cảnh đa phương thức và cân nhắc về bảo mật
  - **Phương pháp Triển khai**: Kiến trúc đơn luồng so với đa tác nhân
    - Kỹ thuật phân đoạn và ưu tiên ngữ cảnh
    - Chiến lược tải và nén ngữ cảnh dần dần
    - Phương pháp ngữ cảnh phân lớp và tối ưu hóa truy xuất
  - **Khung Đo lường**: Các chỉ số mới nổi để đánh giá hiệu quả ngữ cảnh
    - Hiệu quả đầu vào, hiệu suất, chất lượng và trải nghiệm người dùng
    - Phương pháp thử nghiệm để tối ưu hóa ngữ cảnh
    - Phân tích lỗi và phương pháp cải thiện

#### Cập nhật Điều hướng Chương trình Học (README.md)
- **Cấu trúc Mô-đun Nâng cao**: Bảng chương trình học được cập nhật bao gồm các chủ đề nâng cao mới
  - Thêm mục Kỹ thuật Ngữ cảnh (5.14) và Vận chuyển Tùy chỉnh (5.15)
  - Định dạng nhất quán và liên kết điều hướng trên tất cả các mô-đun
  - Cập nhật mô tả phản ánh phạm vi nội dung hiện tại

### Cải tiến Cấu trúc Thư mục
- **Tiêu chuẩn hóa Tên**: Đổi tên "mcp transport" thành "mcp-transport" để đồng bộ với các thư mục chủ đề nâng cao khác
- **Tổ chức Nội dung**: Tất cả các thư mục 05-AdvancedTopics hiện tuân theo mẫu đặt tên nhất quán (mcp-[chủ đề])

### Nâng cao Chất lượng Tài liệu
- **Căn chỉnh Đặc tả MCP**: Tất cả nội dung mới tham chiếu Đặc tả MCP hiện tại 2025-06-18
- **Ví dụ Đa ngôn ngữ**: Các ví dụ mã hóa đầy đủ bằng C#, TypeScript, và Python
- **Tập trung Doanh nghiệp**: Các mẫu sẵn sàng sản xuất và tích hợp đám mây Azure xuyên suốt
- **Tài liệu Hình ảnh**: Biểu đồ Mermaid cho kiến trúc và trực quan luồng hoạt động

## Ngày 18 tháng 8, 2025

### Cập nhật Toàn diện Tài liệu - Chuẩn MCP 2025-06-18

#### Thực hành Bảo mật MCP Tốt nhất (02-Security/) - Hiện đại hóa Toàn diện
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Viết lại hoàn toàn căn chỉnh với Đặc tả MCP 2025-06-18
  - **Yêu cầu Bắt buộc**: Thêm các yêu cầu PHẢI / KHÔNG PHẢI rõ ràng từ đặc tả chính thức với chỉ báo trực quan rõ ràng
  - **12 Thực hành Bảo mật Cốt lõi**: Tái cấu trúc từ danh sách 15 mục thành các lĩnh vực bảo mật toàn diện
    - Bảo mật Token & Xác thực với tích hợp nhà cung cấp danh tính bên ngoài
    - Quản lý Phiên & Bảo mật Vận chuyển với yêu cầu mật mã học
    - Bảo vệ Mối đe dọa Đặc thù AI với tích hợp Microsoft Prompt Shields
    - Kiểm soát Truy cập & Quyền với nguyên tắc đặc quyền tối thiểu
    - An toàn Nội dung & Giám sát với tích hợp Azure Content Safety
    - Bảo mật Chuỗi Cung ứng với xác thực thành phần toàn diện
    - Bảo mật OAuth & Ngăn ngừa Confused Deputy với triển khai PKCE
    - Ứng phó Sự cố & Phục hồi với năng lực tự động
    - Tuân thủ & Quản trị với căn chỉnh quy định
    - Kiểm soát Bảo mật Nâng cao với kiến trúc zero trust
    - Tích hợp Hệ sinh thái Bảo mật Microsoft với các giải pháp toàn diện
    - Tiến hóa Bảo mật Liên tục với các thực hành thích ứng
  - **Giải pháp Bảo mật Microsoft**: Hướng dẫn tích hợp nâng cao cho Prompt Shields, Azure Content Safety, Entra ID, và GitHub Advanced Security
  - **Tài nguyên Triển khai**: Liên kết tài nguyên toàn diện được phân loại theo Tài liệu MCP Chính thức, Giải pháp Bảo mật Microsoft, Tiêu chuẩn Bảo mật, và Hướng dẫn Triển khai

#### Kiểm soát Bảo mật Nâng cao (02-Security/) - Triển khai Doanh nghiệp
- **MCP-SECURITY-CONTROLS-2025.md**: Cải tổ hoàn toàn với khung bảo mật cấp doanh nghiệp
  - **9 Lĩnh vực Bảo mật Toàn diện**: Mở rộng từ các kiểm soát cơ bản thành khung doanh nghiệp chi tiết
    - Xác thực & Ủy quyền Nâng cao với tích hợp Microsoft Entra ID
    - Bảo mật Token & Kiểm soát Chống Qua Lại với xác thực toàn diện
    - Kiểm soát Bảo mật Phiên với ngăn chặn chiếm quyền
    - Kiểm soát Bảo mật Đặc thù AI với ngăn ngừa tiêm lệnh và đầu độc công cụ
    - Ngăn ngừa Tấn công Confused Deputy với bảo mật proxy OAuth
    - Bảo mật Thực thi Công cụ với môi trường cách ly và sandbox
    - Kiểm soát Bảo mật Chuỗi Cung ứng với xác minh phụ thuộc
    - Kiểm soát Giám sát & Phát hiện với tích hợp SIEM
    - Ứng phó Sự cố & Phục hồi với năng lực tự động
  - **Ví dụ Triển khai**: Thêm các khối cấu hình YAML chi tiết và ví dụ mã
  - **Tích hợp Giải pháp Microsoft**: Bao phủ toàn diện dịch vụ bảo mật Azure, GitHub Advanced Security, và quản lý danh tính doanh nghiệp

#### Bảo mật Chủ đề Nâng cao (05-AdvancedTopics/mcp-security/) - Triển khai Sẵn sàng Sản xuất
- **README.md**: Viết lại hoàn toàn cho triển khai bảo mật doanh nghiệp
  - **Căn chỉnh Đặc tả Hiện tại**: Cập nhật theo Đặc tả MCP 2025-06-18 với các yêu cầu bảo mật bắt buộc
  - **Xác thực Nâng cao**: Tích hợp Microsoft Entra ID với ví dụ toàn diện .NET và Java Spring Security
  - **Tích hợp Bảo mật AI**: Triển khai Microsoft Prompt Shields và Azure Content Safety với ví dụ Python chi tiết
  - **Giảm thiểu Mối đe dọa Nâng cao**: Ví dụ triển khai toàn diện cho
    - Ngăn ngừa Tấn công Confused Deputy với PKCE và xác thực sự đồng ý của người dùng
    - Ngăn ngừa Qua Lại Token với xác thực khán giả và quản lý token an toàn
    - Ngăn ngừa Chiếm quyền Phiên với liên kết mật mã và phân tích hành vi
  - **Tích hợp Bảo mật Doanh nghiệp**: Giám sát Azure Application Insights, đường ống phát hiện mối đe dọa, và bảo mật chuỗi cung ứng
  - **Bảng Kiểm Tra Triển khai**: Kiểm soát bảo mật bắt buộc so với khuyến nghị rõ ràng cùng lợi ích của hệ sinh thái bảo mật Microsoft

### Chất lượng Tài liệu & Căn chỉnh Tiêu chuẩn
- **Tham chiếu Đặc tả**: Cập nhật tất cả tham chiếu tới Đặc tả MCP 2025-06-18 hiện tại
- **Hệ sinh thái Bảo mật Microsoft**: Hướng dẫn tích hợp nâng cao xuyên suốt tài liệu bảo mật
- **Triển khai Thực tế**: Thêm ví dụ mã chi tiết trong .NET, Java, và Python với các mẫu doanh nghiệp
- **Tổ chức Tài nguyên**: Phân loại toàn diện tài liệu chính thức, tiêu chuẩn bảo mật, và hướng dẫn triển khai
- **Chỉ báo Trực quan**: Đánh dấu rõ ràng yêu cầu bắt buộc và các thực hành khuyến nghị


#### Khái niệm Cốt lõi (01-CoreConcepts/) - Hiện đại hóa Toàn diện
- **Cập nhật Phiên bản Giao thức**: Cập nhật để tham chiếu Đặc tả MCP 2025-06-18 hiện tại với định dạng phiên bản theo ngày (YYYY-MM-DD)
- **Tinh chỉnh Kiến trúc**: Nâng cao mô tả về Host, Client, và Server để phản ánh các mẫu kiến trúc MCP hiện tại
  - Host bây giờ được định nghĩa rõ ràng là các ứng dụng AI điều phối nhiều kết nối client MCP
  - Client được mô tả là kết nối giao thức duy trì quan hệ một-một với server
  - Server được nâng cao với kịch bản triển khai cục bộ so với từ xa
- **Tái cấu trúc Nguyên thủy**: Cải tổ hoàn toàn các kiểu nguyên thủy server và client
  - Nguyên thủy Server: Tài nguyên (nguồn dữ liệu), Prompt (mẫu), Công cụ (hàm thực thi) với giải thích và ví dụ chi tiết
  - Nguyên thủy Client: Lấy mẫu (hoàn thiện LLM), Gợi ý (đầu vào người dùng), Ghi nhật ký (gỡ lỗi/giám sát)
  - Cập nhật với các mẫu phương thức khám phá (`*/list`), truy xuất (`*/get`), và thực thi (`*/call`) hiện tại
- **Kiến trúc Giao thức**: Giới thiệu mô hình kiến trúc hai lớp
  - Lớp Dữ liệu: nền tảng JSON-RPC 2.0 với quản lý vòng đời và nguyên thủy
  - Lớp Vận chuyển: STDIO (cục bộ) và HTTP Streamable với SSE (vận chuyển từ xa)
- **Khung Bảo mật**: Nguyên tắc bảo mật toàn diện bao gồm sự đồng ý rõ ràng của người dùng, bảo vệ quyền riêng tư dữ liệu, an toàn thực thi công cụ, và bảo mật lớp vận chuyển
- **Mẫu Giao tiếp**: Cập nhật thông điệp giao thức thể hiện luồng khởi tạo, khám phá, thực thi, và thông báo
- **Ví dụ Mã**: Làm mới ví dụ đa ngôn ngữ (.NET, Java, Python, JavaScript) để phản ánh các mẫu MCP SDK hiện tại

#### Bảo mật (02-Security/) - Cải tổ Toàn diện Bảo mật  
- **Căn chỉnh Tiêu chuẩn**: Căn chỉnh hoàn toàn với các yêu cầu bảo mật Đặc tả MCP 2025-06-18
- **Tiến hóa Xác thực**: Tài liệu tiến trình từ các server OAuth tùy chỉnh đến ủy quyền nhà cung cấp danh tính bên ngoài (Microsoft Entra ID)
- **Phân tích Mối đe dọa Đặc thù AI**: Mở rộng bao phủ các vectơ tấn công AI hiện đại
  - Kịch bản tấn công tiêm prompt chi tiết với ví dụ thực tế
  - Cơ chế đầu độc công cụ và mẫu tấn công "rug pull"
  - Đầu độc cửa sổ ngữ cảnh và các tấn công gây nhầm lẫn mô hình
- **Giải pháp Bảo mật AI Microsoft**: Bao phủ toàn diện hệ sinh thái bảo mật Microsoft
  - AI Prompt Shields với phát hiện nâng cao, làm nổi bật, và kỹ thuật phân tách
  - Mẫu tích hợp Azure Content Safety
  - GitHub Advanced Security cho bảo vệ chuỗi cung ứng
- **Giảm thiểu Mối đe dọa Nâng cao**: Kiểm soát bảo mật chi tiết cho
  - Chiếm quyền phiên với các kịch bản tấn công đặc thù MCP và yêu cầu ID phiên mật mã
  - Vấn đề Confused Deputy trong kịch bản proxy MCP với yêu cầu sự đồng ý rõ ràng
  - Lỗ hổng qua lại token với kiểm soát xác nhận bắt buộc
- **Bảo mật Chuỗi Cung ứng**: Mở rộng bao phủ chuỗi cung ứng AI bao gồm mô hình nền tảng, dịch vụ nhúng, nhà cung cấp ngữ cảnh, và API bên thứ ba
- **Bảo mật Nền tảng**: Tăng cường tích hợp với các mẫu bảo mật doanh nghiệp bao gồm kiến trúc zero trust và hệ sinh thái bảo mật Microsoft
- **Tổ chức Tài nguyên**: Phân loại toàn diện các liên kết tài nguyên theo loại (Tài liệu Chính thức, Tiêu chuẩn, Nghiên cứu, Giải pháp Microsoft, Hướng dẫn Triển khai)

### Cải thiện Chất lượng Tài liệu
- **Mục tiêu Học tập Có cấu trúc**: Nâng cao mục tiêu học tập với kết quả cụ thể và khả thi
- **Tham chiếu Chéo**: Thêm liên kết giữa các chủ đề liên quan về bảo mật và khái niệm cốt lõi
- **Thông tin Hiện tại**: Cập nhật tất cả tham chiếu ngày tháng và liên kết đặc tả theo tiêu chuẩn hiện hành
- **Hướng dẫn Triển khai**: Thêm hướng dẫn triển khai cụ thể và khả thi trong cả hai phần

## Ngày 16 tháng 7, 2025

### Cải tiến README và Điều hướng
- Thiết kế lại toàn bộ điều hướng chương trình học trong README.md
- Thay thế thẻ `<details>` bằng định dạng bảng dễ tiếp cận hơn
- Tạo các tùy chọn bố cục thay thế trong thư mục "alternative_layouts" mới
- Thêm ví dụ điều hướng dạng thẻ, dạng tab, và dạng gập
- Cập nhật phần cấu trúc kho lưu trữ bao gồm tất cả các tệp mới nhất
- Tăng cường phần "Cách sử dụng Chương trình Học" với các khuyến nghị rõ ràng
- Cập nhật liên kết đặc tả MCP trỏ đến URL chính xác
- Thêm phần Kỹ thuật Ngữ cảnh (5.14) vào cấu trúc chương trình học

### Cập nhật Hướng dẫn Học tập
- Xem xét lại hoàn toàn hướng dẫn học tập để phù hợp với cấu trúc kho lưu trữ hiện tại
- Thêm các phần mới về MCP Clients và Tools, và MCP Servers Phổ biến
- Cập nhật Bản đồ Chương trình Trực quan để phản ánh chính xác tất cả chủ đề
- Tăng cường mô tả các Chủ đề Nâng cao bao phủ tất cả các lĩnh vực chuyên biệt
- Cập nhật phần Nghiên cứu Tình huống phản ánh các ví dụ thực tế
- Thêm nhật ký thay đổi toàn diện này

### Đóng góp Cộng đồng (06-CommunityContributions/)
- Thêm thông tin chi tiết về các server MCP cho tạo hình ảnh
- Thêm phần toàn diện về sử dụng Claude trong VSCode
- Thêm hướng dẫn cài đặt và sử dụng client terminal Cline
- Cập nhật phần client MCP để bao gồm tất cả các tùy chọn client phổ biến
- Cải tiến ví dụ đóng góp với các mẫu mã chính xác hơn

### Chủ đề Nâng cao (05-AdvancedTopics/)
- Tổ chức tất cả các thư mục chủ đề chuyên biệt với tên gọi nhất quán
- Thêm tài liệu và ví dụ kỹ thuật ngữ cảnh
- Thêm tài liệu tích hợp agent Foundry
- Cải tiến tài liệu tích hợp bảo mật Entra ID

## Ngày 11 tháng 6, 2025

### Tạo Ban đầu
- Phát hành phiên bản đầu tiên của chương trình MCP cho Người mới bắt đầu
- Tạo cấu trúc cơ bản cho tất cả 10 phần chính
- Triển khai Bản đồ Chương trình Trực quan để điều hướng
- Thêm các dự án mẫu ban đầu bằng nhiều ngôn ngữ lập trình

### Bắt đầu (03-GettingStarted/)
- Tạo ví dụ triển khai server đầu tiên
- Thêm hướng dẫn phát triển client
- Bao gồm hướng dẫn tích hợp client LLM
- Thêm tài liệu tích hợp VS Code
- Triển khai các ví dụ server Server-Sent Events (SSE)

### Khái niệm Cốt lõi (01-CoreConcepts/)
- Thêm giải thích chi tiết về kiến trúc client-server
- Tạo tài liệu về các thành phần giao thức chính
- Tài liệu các mẫu thông điệp trong MCP

## Ngày 23 tháng 5, 2025

### Cấu trúc Kho lưu trữ
- Khởi tạo kho lưu trữ với cấu trúc thư mục cơ bản
- Tạo tệp README cho mỗi phần chính
- Thiết lập hạ tầng dịch thuật
- Thêm tài sản hình ảnh và biểu đồ

### Tài liệu
- Tạo README.md ban đầu với tổng quan chương trình học
- Thêm CODE_OF_CONDUCT.md và SECURITY.md
- Thiết lập SUPPORT.md với hướng dẫn nhận trợ giúp
- Tạo cấu trúc hướng dẫn học tập sơ bộ

## Ngày 15 tháng 4, 2025

### Lập Kế hoạch và Khung
- Lập kế hoạch ban đầu cho chương trình MCP cho Người mới bắt đầu
- Xác định mục tiêu học tập và đối tượng mục tiêu
- Phác thảo cấu trúc 10 phần của chương trình học
- Phát triển khung khái niệm cho ví dụ và nghiên cứu tình huống
- Tạo các ví dụ nguyên mẫu ban đầu cho các khái niệm chính

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->