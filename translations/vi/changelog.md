# Nhật ký thay đổi: MCP cho Khóa học Người mới bắt đầu

Tài liệu này dùng để ghi lại tất cả các thay đổi quan trọng được thực hiện trong khóa học Model Context Protocol (MCP) cho Người mới bắt đầu. Các thay đổi được ghi lại theo thứ tự thời gian ngược (những thay đổi mới nhất trước).

## Ngày 9 tháng 9 năm 2026

### Cập nhật Thống nhất Đặc tả MCP 2026-07-28

Cập nhật khóa học tiếng Anh từ bản phát hành ứng cử viên và hướng dẫn cơ bản `2025-11-25`
lên đặc tả MCP cuối cùng `2026-07-28`.

- **Cập nhật**: Tham chiếu phiên bản hiện tại, liên kết đặc tả, hướng dẫn yêu cầu không trạng thái,
  `server/discover`, tiêu đề HTTP có thể truyền trực tiếp, và vòng đời phần mở rộng Nhiệm vụ
  trên 38 tệp tài liệu tiếng Anh.
- **Sửa lỗi**: Elicitation giờ sử dụng `elicitation/create`, Sampling sử dụng
  `sampling/createMessage`, và `InputRequiredResult.resultType` dùng
  `"input_required"`.
- **Thay thế**: Bài học trạng thái hội thoại Root Context không chính xác được thay bằng bài
  học Roots chính xác với giao thức, bao gồm gợi ý hệ thống tập tin thông tin,
  luồng với nhiều lần đi lại hiện tại, ranh giới bảo mật, và các tùy chọn di chuyển.
- **Làm rõ**: Roots, Sampling, Logging, và Đăng ký Khách hàng Động đều
  bị ngừng sử dụng trong `2026-07-28`, với các thay thế được đề xuất và ngày
  xóa sớm nhất được ghi lại.
- **Gắn nhãn**: Các mẫu vẫn phụ thuộc MCP `2025-11-25`, HTTP+SSE,
  bắt tay khởi tạo, hoặc phiên giao thức được giữ lại như ví dụ tương thích kế thừa
  thay vì trình bày như các hiện thực hiện tại.
- **Hướng dẫn bảo mật**: Cập nhật các hướng dẫn bảo mật độc lập để sử dụng
  ủy quyền theo yêu cầu và tay cầm trạng thái ứng dụng rõ ràng thay vì
  ID phiên giao thức đã bị loại bỏ. Tài liệu Metadata Client ID bây giờ là
  con đường đăng ký ưu tiên, với DCR được ghi nhận chỉ để tương thích.
- **Tài liệu hỗ trợ**: Cập nhật hướng dẫn học tập, danh sách kiểm tra cộng tác viên,
  nghiên cứu trường hợp Publora, và nghiên cứu trường hợp APIM. Hướng dẫn APIM giờ đề xuất
  điểm cuối HTTP `/mcp` có thể truyền trực tiếp hiện tại thay vì `/sse` đã hết hạn.
- **Liên kết chính thức**: Thay thế các URL đặc tả đã nghỉ và bản nháp trong nguồn
  Markdown tiếng Anh bằng liên kết có phiên bản `2026-07-28`, đồng thời giữ liên kết
  rõ ràng tới các phiên bản kế thừa khi mẫu vẫn gắn với công cụ cũ hơn.
- **Tên tệp ổn định**: Đổi tên hướng dẫn đặc tả cuối cùng và hai hướng dẫn bảo mật
  để loại bỏ hậu tố ứng cử viên phát hành và năm, sau đó cập nhật tất cả liên kết tiếng Anh
  đến các đường dẫn ổn định của chúng.
- **Mẫu ủy quyền mới**: Thêm một
  [máy chủ tài nguyên MCP TypeScript `2026-07-28`](./02-Security/samples/cimd-dcr-auth/README.md)
  đã được thử nghiệm so sánh Tài liệu Metadata Client ID ưu tiên với phương án dự phòng
  Đăng ký Khách hàng Động lỗi thời. Mẫu bao gồm khám phá RFC 9728, xác thực JWKS,
  phạm vi công cụ, mười hai bài kiểm tra, và hướng dẫn thiết lập Auth0.
- **Phạm vi dịch**: Chỉ các tệp nguồn tiếng Anh được chỉnh sửa; các bản dịch được tạo tự động
  và hình ảnh dịch vẫn không đổi vì chúng được dịch tự động.

## Ngày 29 tháng 7 năm 2026

### Bổ sung Bài học 08: Sidecar Độ tin cậy và Thử lại An toàn

Thêm một bài học đi kèm trung lập nhà cung cấp cho các công cụ MCP tạo hiệu ứng thế giới thực,
phù hợp với đặc tả cuối cùng `2026-07-28`.


- **Mới**: Bài học đồng hành [hộp phụ độ tin cậy][reliability-sidecar]
  sử dụng một câu chuyện phiếu hỗ trợ, hai sơ đồ Mermaid, và luồng quyết định thử lại
  để giải thích các chìa khóa vận hành ổn định, tiếp nhận sao chép nguyên tử,
  hòa giải, bằng chứng, và ranh giới phần mở rộng Tasks.
- **Mới**: Một bài tập tiêm lỗi Python và SQLite chuẩn-thư viện
  sử dụng kho lưu trữ vận hành và phiếu riêng biệt để minh họa phản hồi mất
  sau khi một hiệu ứng ngoài cam kết. Sáu bài kiểm tra xác định bao gồm sao chép
  ngây thơ, phục hồi khởi động lại có bảo vệ, xung đột payload, kết quả
  được lưu trong bộ nhớ đệm, tuyên bố đang hoạt động, và tiếp nhận sao chép đồng thời.
- **Cập nhật**: Mô-đun 08 hiện liên kết bài học đồng hành, xác định
  mô hình yêu cầu không trạng thái cuối cùng `2026-07-28`, phân biệt khả năng quan sát
  OpenTelemetry với tính năng ghi nhật ký MCP bị loại bỏ, và giới hạn
  ví dụ thử lại chung của nó cho các thao tác chỉ đọc.
- **Tùy chọn**: Bài học ánh xạ các khái niệm di động của nó đến một triển khai cộng đồng được gắn thẻ
  mà không biến dịch vụ lưu trữ hoặc cuộc gọi mạng thành một phần bài tập.


[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## Ngày 2 tháng 7, 2026

### Bài học mới: Ứng viên phát hành Đặc tả MCP 2026-07-28

Thêm nội dung về ứng viên phát hành đặc tả MCP sắp tới `2026-07-28` (được công bố ngày 21 tháng 5 năm 2026; dự kiến phát hành cuối cùng ngày 28 tháng 7 năm 2026), được tóm tắt từ [bài viết thông báo chính thức](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Nền tảng chương trình học vẫn giữ **Đặc tả MCP 2025-11-25** cho đến khi phiên bản mới được phát hành, nên đây được trình bày như hướng dẫn nhìn về tương lai thay vì viết lại các bài học hiện có.

- **Mới**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — một bài học đầy đủ bao gồm lõi giao thức không trạng thái (loại bỏ bắt tay `initialize` và `Mcp-Session-Id`), các header định tuyến mới `Mcp-Method`/`Mcp-Name`, metadata cache `ttlMs`/`cacheScope`, W3C Trace Context trong `_meta`, khuôn khổ Mở rộng chính thức (MCP Apps và phần mở rộng Tasks mới), sáu SEP tăng cường ủy quyền, ngừng dùng Roots/Sampling/Logging, và chuyển sang JSON Schema 2020-12 hoàn chỉnh cho các lược đồ công cụ.
- **Cập nhật** với các lời dẫn hướng về phía trước liên kết đến bài học mới:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): ghi chú phiên bản giao thức, các phần Sampling/Roots/Logging/Tasks, và "Tiếp theo là gì"
  - [02-Security/README.md](./02-Security/README.md): lời dẫn tăng cường ủy quyền
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): lời dẫn vận tải không trạng thái
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): lời dẫn ngừng dùng Sampling

  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Ghi chú việc ngừng hỗ trợ logging và mở rộng lời gọi Tasks

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): ghi chú về chuyển tiếp không trạng thái/phiên
  - [README.md](./README.md): ghi chú "Nhìn về phía trước" trong phần đặc tả và mục mới `1.1` trong bảng mô-đun chương trình học
  - [study_guide.md](./study_guide.md): đầu mục hướng về tương lai dưới phần Tổng quan Khái niệm Cốt lõi và ghi chú phụ lục có ngày tháng
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): ghi chú về bản đồ vận chuyển `mcp-session-id` trước mô hình yêu cầu không trạng thái
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): ghi chú tổng quan mô-đun về việc loại bỏ các Ngữ cảnh Gốc / Lấy mẫu và phần mở rộng Nhiệm vụ
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): ghi chú tăng cường ủy quyền

## 24 tháng 6, 2026

### Bài học mới: Sử dụng MCP trong ứng dụng Copilot

- [Phần Công cụ](./12-tooling/README.md) Thêm phần công cụ.
- [MCP trong ứng dụng Copilot](./12-tooling/01-copilot-app/README.md)

## 16 tháng 6, 2026

### Căn chỉnh Đặc tả MCP & Xác thực Mẫu

Đã xác thực chương trình học dựa trên **Đặc tả MCP 2025-11-25** hiện tại và các SDK chính thức mới nhất, sau đó chỉnh sửa các tham chiếu đặc tả cũ còn sót lại và xác nhận các mẫu cốt lõi vẫn xây dựng và chạy được.

#### Sửa Phiên bản Đặc tả (2025-06-18 / 2025-03-26 → 2025-11-25)

Cập nhật nội dung tiếng Anh nơi vẫn cho rằng bản sửa đổi đặc tả cũ hơn là tiêu chuẩn *hiện tại/mới nhất*, và điều hướng lại các liên kết đến đường dẫn đặc tả chính thức `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Cập nhật biểu ngữ "Tiêu chuẩn Hiện tại", phần giới thiệu, tiêu đề nguyên tắc bảo mật cốt lõi, tiêu đề yêu cầu bắt buộc, phần Microsoft Entra ID, các liên kết Tham khảo & Tài nguyên, và thông báo bảo mật kết thúc (8 tham chiếu) thành 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Cập nhật liên kết tài nguyên bổ sung đặc tả và biểu ngữ "Tiêu chuẩn Hiện tại" thành 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Thay thế liên kết bảo mật và tin cậy `2025-03-26` lỗi thời bằng trang thực hành bảo mật tốt nhất 2025-11-25 hiện tại
- **03-GettingStarted/14-sampling/README.md**: Cập nhật liên kết tài liệu chính thức về lấy mẫu thành 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Cập nhật tham chiếu "đặc tả MCP hiện tại" ở thì hiện tại và liên kết tài nguyên bổ sung đặc tả thành 2025-11-25 (ghi chú lịch sử ngừng hỗ trợ SSE vẫn giữ nguyên để đảm bảo chính xác)

#### Xác thực Mẫu Với SDK Hiện Tại

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` đã giải quyết `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` đã qua mà không lỗi kiểu — các API `McpServer`/`StdioServerTransport` hiện có vẫn hợp lệ
- **Python (03-GettingStarted/01-first-server/solution/python)**: Đã kiểm tra trong môi trường `.venv` biệt lập với `mcp[cli]` (1.27.2); `py_compile` thành công và `FastMCP.list_tools()` trả về đúng công cụ `add` và `subtract`
- Xác nhận tất cả phạm vi phiên bản mẫu `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) đều giải quyết sạch sẽ đến phiên bản hiện tại `1.29.0` mà không có thay đổi API phá vỡ

#### Căn chỉnh Ghim Phụ thuộc (đóng khoảng cách phiên bản)

Nâng các ghim SDK lỗi thời để mọi mẫu đều theo dõi bản phát hành MCP hiện tại, phù hợp với quy ước toàn repo:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Nâng `@modelcontextprotocol/sdk` từ `^1.8.0` → `>=1.26.0` và cập nhật mô tả gói cũ `"updated for MCP 2025-06-18"` thành `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** và **lab4/code/github_mcp_server/pyproject.toml**: Nâng ghim chính xác `mcp==1.23.0` → `mcp>=1.26.0`; tạo lại cả hai tập tin `uv.lock` (`uv lock`) để các tập tin khóa giải quyết đến `mcp 1.27.2` hiện tại và giữ đồng bộ với các bản khai báo

#### Phân tích Khoảng trống Chương trình Học — Phủ sóng Tính năng Đặc tả Mới nhất

Xác nhận chương trình học đã bao phủ mọi nguyên thủy được giới thiệu/mở rộng trong MCP 2025-11-25, nên không còn khoảng trống nội dung:
- **Lấy mẫu**: Bài học 03-GettingStarted/14-sampling cộng với 05-AdvancedTopics/mcp-sampling
- **Khơi gợi (bao gồm chế độ URL)**: Được tài liệu trong 01-CoreConcepts và 05-AdvancedTopics/mcp-protocol-features
- **Nguồn gốc**: Được tài liệu trong 00-Introduction, 01-CoreConcepts, và 05-AdvancedTopics/mcp-root-contexts
- **Nhiệm vụ (thí nghiệm, thao tác chạy dài)**: Được tài liệu trong 01-CoreConcepts và 05-AdvancedTopics/mcp-protocol-features
- **Chú thích Công cụ** (`readOnlyHint` / `destructiveHint`): Được tài liệu trong 01-CoreConcepts và 05-AdvancedTopics/mcp-protocol-features

### Tăng cường Bảo mật & Sửa chữa Lỗ hổng Phụ thuộc

Thực hiện một lần quét bảo mật đầy đủ trên mọi bản khai phụ thuộc và mã nguồn mẫu, sau đó khắc phục hết mọi cảnh báo npm đã báo và một phát hiện ở cấp độ mã. Sau khắc phục, `npm audit` báo **0 lỗ hổng** trong mọi thư mục được kiểm tra.

#### Lỗ hổng Phụ thuộc npm (gián tiếp) — Đã Sửa

Kiểm tra tất cả 15 tập tin `package-lock.json` đã cam kết. Các lỗ hổng giới hạn ở các phụ thuộc gián tiếp do công cụ phát triển MCP Inspector, client OpenAI và SDK MCP kéo vào; tất cả hiện đã được giải quyết mà không phá vỡ các mẫu:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** và **lab3/code/weather_mcp/inspector**: Nâng cấp `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), đã xóa bỏ các cảnh báo liên quan đến `ajv`, `brace-expansion`, `diff`, `path-to-regexp` và `ws` trong gói. Thêm mục `overrides` trong npm ép buộc dùng `shell-quote@1.8.4` đã vá lỗi để loại bỏ cảnh báo nghiêm trọng còn lại do `concurrently` gây ra; tạo lại cả hai lockfile (hiện không còn lỗ hổng)
- **03-GettingStarted/samples/typescript**: `npm audit fix` đã cập nhật thư viện phụ thuộc `qs` (mức độ trung bình) lên phiên bản đã vá lỗi
- **03-GettingStarted/samples/javascript**: `npm audit fix` đã cập nhật thư viện phụ thuộc `hono` (mức độ trung bình) lên phiên bản đã vá lỗi
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` đã cập nhật thư viện phụ thuộc `form-data` (mức độ cao) lên phiên bản đã vá lỗi
- **03-GettingStarted/11-simple-auth/solution/typescript**: Tạo mới `package-lock.json` bị thiếu nhằm giúp dự án có thể tái lập và kiểm tra (không còn lỗ hổng)

#### Sửa lỗi bảo mật mức độ mã (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Loại bỏ `shell=True` khỏi công cụ `open_in_vscode`. Trước đó, lệnh `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` cho phép các ký tự đặc biệt của shell trong đường dẫn thư mục được `cmd.exe` giải thích (kênh tiêm lệnh). Bây giờ lệnh khởi chạy trực tiếp tệp lệnh `Code.exe` đã được phân giải với đối số là thư mục — không qua shell — tương đương về mặt chức năng và an toàn

#### Kiểm tra Phụ thuộc Python

- Kiểm tra tất cả bộ yêu cầu Python với `pip-audit`. `05-AdvancedTopics` và `03-GettingStarted/samples/python` báo cáo **không có lỗ hổng đã biết** (các phạm vi `mcp` / `httpx` / `pydantic` / `python-dotenv` được giải quyết về các phiên bản đã vá hiện tại)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` phát hiện thư viện phụ thuộc gián tiếp **`werkzeug` 3.1.1** với ba cảnh báo DoS liên quan đến tên thiết bị Windows `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, và `CVE-2026-27199` (tất cả được khắc phục trong 3.1.6). Thêm cố định bảo mật rõ ràng `werkzeug>=3.1.6` để giải quyết phiên bản đã vá; xác minh rằng giới hạn này được giải quyết hợp lệ với ngăn xếp `chainlit` / `mcp` / `semantic-kernel`

### Đổi Tên Thương Hiệu Sản Phẩm

Cập nhật toàn bộ nội dung giáo trình để phản ánh việc đổi tên thương hiệu sản phẩm của Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Cập nhật liên kết cộng đồng Discord
- **AGENTS.md**: Cập nhật tham chiếu máy chủ Discord
- **README.md**: Cập nhật tham chiếu hệ sinh thái công nghệ
- **study_guide.md**: Cập nhật tham chiếu nghiên cứu tình huống
- **05-AdvancedTopics/README.md**: Cập nhật tiêu đề và mô tả Module 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Cập nhật tiêu đề phần và mô tả
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Cập nhật toàn bộ tiêu đề và nội dung module
- **05-AdvancedTopics/mcp-security-entra/README.md**: Cập nhật liên kết tham chiếu chéo
- **07-LessonsfromEarlyAdoption/README.md**: Cập nhật tham chiếu nghiên cứu tình huống
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Cập nhật tiêu đề Mục 9, huy hiệu và năng lực
- **08-BestPractices/README.md**: Cập nhật liên kết cộng đồng Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Cập nhật tham chiếu kênh Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Cập nhật tham chiếu triển khai mô hình
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Cập nhật bảng dịch vụ AI
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Cập nhật các tham chiếu tài nguyên

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Cập nhật các tham chiếu chính trong giáo trình
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Cập nhật tiêu đề module, tổng quan và tất cả tiêu đề phần trong module
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Cập nhật tiêu đề, mục tiêu học tập, hướng dẫn thiết lập và tài nguyên
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Cập nhật tiêu đề, mục tiêu học tập, bảng máy chủ MCP và các liên kết tham chiếu chéo
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Cập nhật tiêu đề, huy hiệu, yêu cầu trước và tài nguyên
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Cập nhật các tham chiếu Agent Builder và liên kết phản hồi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Cập nhật yêu cầu trước và các tham chiếu tiện ích mở rộng

---

## Ngày 11 tháng 4, 2026

### Bài học mới, Sửa tài liệu và Cập nhật phụ thuộc

#### Thêm nội dung giáo trình mới

**Module 05 - Chủ đề nâng cao**
- **Bài 5.17: Lý luận đa tác nhân đối kháng với MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Hướng dẫn toàn diện mới về mô hình tranh luận đối kháng cho hệ thống đa tác nhân
  - Sơ đồ kiến trúc Mermaid: hai tác nhân → MCP server dùng chung → bản ghi tranh luận → trọng tài → phán quyết
  - Máy chủ công cụ MCP dùng chung (`web_search` + `run_python`) được triển khai bằng Python và TypeScript
  - Các lời nhắc đối kháng hệ thống (CHO / CHỐNG / Trọng tài) với yêu cầu sử dụng công cụ rõ ràng
  - Điều phối viên tranh luận bằng Python, TypeScript, và C# quản lý vòng và điều phối luận điểm
  - MCP `ClientSession` kết nối cho điều phối viên gọi các công cụ thực tế
  - Bảng các trường hợp sử dụng (phát hiện ảo tưởng, mô hình hóa mối đe dọa, đánh giá thiết kế API, xác thực thực tế, lựa chọn công nghệ)
  - Các lưu ý bảo mật: thực thi trong vùng cách ly, xác thực gọi công cụ, giới hạn tần suất, ghi nhật ký kiểm tra
  - Bài tập có cấu trúc với ba kịch bản thực hành (đánh giá mã, quyết định kiến trúc, kiểm duyệt nội dung)

#### Sửa lỗi Tài liệu

**Module 03 - Bắt đầu**
- **05-stdio-server/README.md**: Sửa lỗi ví dụ máy chủ stdio TypeScript chưa hoàn chỉnh — bổ sung khởi tạo phương thức vận chuyển (`new StdioServerTransport()`) và gọi `server.connect(transport)` để phù hợp các ví dụ Python và .NET cùng phần
- **14-sampling/README.md**: Sửa lỗi chính tả — sửa `"Sampling is an davanced features"` thành `"Sampling is an advanced feature"`

#### Cập nhật Giáo trình

**README.md chính**
- Thêm mục 5.17 (Lý luận đa tác nhân đối kháng với MCP) vào bảng giáo trình với liên kết trực tiếp tới bài học mới

**05-AdvancedTopics/README.md**
- Thêm hàng bài học 5.17 vào bảng bài học

**study_guide.md**
- Thêm chủ đề Lý luận đa tác nhân đối kháng vào sơ đồ tư duy và mô tả bằng văn bản các Chủ đề nâng cao

#### Sửa lỗi mã và Bảo mật

**Module 05 - Agents đối kháng (`mcp-adversarial-agents`)**
- **Sửa bảo mật — tiêm lệnh**: Thay thế nội suy shell `execSync` bằng `execFile` + `promisify` trong công cụ TypeScript `run_python`, loại bỏ lỗ hổng tiêm lệnh (code do LLM kiểm soát giờ được truyền như một phần tử argv nguyên thủy, không qua shell)
- **Sửa đường dây công cụ MCP**: Cập nhật điều phối viên tranh luận Python sử dụng client `AsyncAnthropic` (thay vì `Anthropic` đồng bộ chặn), truyền `ClientSession` trực tiếp tới mỗi lượt tác nhân, lấy khai báo công cụ qua `session.list_tools()` mỗi lượt, và gửi các khối `tool_use` qua `session.call_tool()` trong vòng lặp cho tới khi mô hình trả về phản hồi văn bản cuối cùng

#### Cập nhật Phụ thuộc

- Nâng cấp `hono` lên 4.12.12 trên nhiều gói (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Nâng cấp `@hono/node-server` từ 1.19.11 lên 1.19.13 trong các gói TypeScript
- Nâng cấp `cryptography` từ 46.0.5 lên 46.0.7 trong các gói Python (các phòng thí nghiệm 3 và 4 của 10-StreamliningAIWorkflows)
- Nâng cấp `lodash` từ 4.17.23 lên 4.18.1 trong inspector của 10-StreamliningAIWorkflows

#### Dịch thuật

- Đồng bộ hóa bản dịch cho trên 48 ngôn ngữ với những thay đổi nguồn mới nhất (cập nhật i18n)

---

## Ngày 5 tháng 2, 2026

### Cải tiến Xác thực và Điều hướng Trên Toàn Bộ Kho Lưu Trữ

#### Thêm Nội dung Giáo trình Mới

**Module 03 - Bắt đầu**
- **12-mcp-hosts/README.md**: Hướng dẫn toàn diện mới thiết lập máy chủ MCP
  - Ví dụ cấu hình Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Mẫu cấu hình JSON cho tất cả máy chủ phổ biến
  - Bảng so sánh các loại phương thức vận chuyển (stdio, SSE/HTTP, WebSocket)
  - Hỗ trợ xử lý sự cố kết nối thường gặp
  - Thực hành bảo mật tốt nhất cho cấu hình máy chủ

- **13-mcp-inspector/README.md**: Hướng dẫn gỡ lỗi mới cho MCP Inspector
  - Các phương pháp cài đặt (npx, npm global, từ nguồn)
  - Kết nối tới máy chủ qua stdio và HTTP/SSE
  - Công cụ kiểm thử, tài nguyên và luồng công việc sử dụng lời nhắc
  - Tích hợp vào VS Code với MCP Inspector
  - Các tình huống gỡ lỗi phổ biến kèm giải pháp

**Module 04 - Triển khai Thực tế**
- **pagination/README.md**: Hướng dẫn cài đặt phân trang mới
  - Mẫu phân trang dựa trên con trỏ trong Python, TypeScript, Java
  - Xử lý phân trang phía khách hàng
  - Chiến lược thiết kế con trỏ (mờ đục vs có cấu trúc)
  - Khuyến nghị tối ưu hiệu suất

**Module 05 - Chủ đề Nâng cao**
- **mcp-protocol-features/README.md**: Phân tích sâu các tính năng giao thức mới
  - Triển khai thông báo tiến trình
  - Mẫu hủy yêu cầu
  - Mẫu tài nguyên với mẫu URI
  - Quản lý vòng đời máy chủ
  - Kiểm soát mức độ ghi nhật ký
  - Mẫu xử lý lỗi với mã JSON-RPC

#### Sửa lỗi Điều hướng (cập nhật trên 24 tệp)

**README các Module chính**
 Bây giờ liên kết tới cả bài học đầu tiên VÀ module tiếp theo

**Các tệp Phụ Lục Bảo mật 02-Security**
- Tất cả 5 tài liệu bảo mật bổ sung hiện có điều hướng "Tiếp theo là gì":

**Tệp Nghiên cứu Tình huống 09-CaseStudy**
- Tất cả tệp nghiên cứu tình huống hiện có điều hướng tuần tự:

**Phòng thí nghiệm 10-StreamliningAI**
Thêm phần "Tiếp theo là gì" vào tổng quan Module 10 và Module 11

#### Sửa lỗi Mã và Nội dung

**Cập nhật SDK và Phụ thuộc**
Sửa phiên bản openai trống thành `^4.95.0`
Cập nhật SDK từ `^1.8.0` lên `>=1.26.0`
Cập nhật các cố định phiên bản mcp lên `>=1.26.0`

**Sửa lỗi Mã**
Sửa mẫu mô hình không hợp lệ `gpt-4o-mini` thành `gpt-4.1-mini`

**Sửa lỗi Nội dung**
Sửa liên kết hỏng `READMEmd` thành `README.md`, sửa tiêu đề giáo trình `Module 1-3` thành `Module 0-3`, sửa đường dẫn phân biệt chữ hoa/thường
Xóa nội dung bị trùng lỗi của Nghiên cứu Tình huống 5

**Cải thiện Hướng dẫn cho Người mới**
Thêm phần giới thiệu phù hợp, mục tiêu học tập và yêu cầu trước dành cho người mới

#### Cập nhật Giáo trình

**README.md chính**
- Thêm các mục 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Phân trang), 5.16 (Tính năng Giao thức) vào bảng giáo trình

**README các Module**
Thêm bài học 12 và 13 vào danh sách bài học
Thêm phần Hướng dẫn Thực hành với liên kết phân trang
Thêm bài học 5.15 (Phương thức vận chuyển Tùy chỉnh) và 5.16 (Tính năng Giao thức)

**study_guide.md**
- Cập nhật sơ đồ tư duy với tất cả chủ đề mới: Cài đặt MCP Hosts, MCP Inspector, Chiến lược Phân trang, Phân tích sâu Tính năng Giao thức

## Ngày 28 tháng 1, 2026

### Đánh giá Tuân thủ Tiêu chuẩn MCP 2025-11-25

#### Nâng cao Khái niệm Cốt lõi (01-CoreConcepts/)
- **Nguyên thủy Client Mới - Roots**: Thêm tài liệu toàn diện về nguyên thủy Roots của client, giúp máy chủ hiểu được ranh giới hệ thống tập tin và quyền truy cập
- **Chú thích Công cụ**: Thêm tài liệu hướng dẫn về các chú thích hành vi công cụ (`readOnlyHint`, `destructiveHint`) giúp quyết định thực thi công cụ tốt hơn
- **Gọi Công cụ trong Phân mẫu**: Cập nhật tài liệu Phân mẫu bao gồm các tham số `tools` và `toolChoice` để mô hình có thể gọi công cụ trong yêu cầu phân mẫu
- **Gây Dựng Chế độ URL**: Thêm tài liệu về cơ chế gây dựng dựa trên URL cho các tương tác web ngoài do máy chủ khởi xướng
- **Tasks (Thử nghiệm)**: Thêm mục mới tài liệu về tính năng Tasks thử nghiệm cho bao bọc thực thi bền bỉ và truy xuất kết quả hoãn lại

- **Hỗ trợ Biểu tượng**: Ghi nhận rằng công cụ, tài nguyên, mẫu tài nguyên và lời nhắc giờ đây có thể bao gồm biểu tượng như siêu dữ liệu bổ sung

#### Cập nhật Tài liệu
- **README.md**: Thêm tham chiếu phiên bản MCP Specification 2025-11-25 và giải thích phiên bản dựa trên ngày
- **study_guide.md**: Cập nhật bản đồ chương trình học để bao gồm Các Nhiệm vụ và Ghi chú Công cụ trong phần Khái niệm Cốt lõi; cập nhật dấu thời gian tài liệu

#### Xác minh Tuân thủ Đặc tả
- **Phiên bản Giao thức**: Xác minh tất cả tài liệu tham chiếu MCP Specification 2025-11-25 hiện tại
- **Phù hợp Kiến trúc**: Xác nhận tài liệu kiến trúc hai lớp (Lớp Dữ liệu + Lớp Giao Thức) chính xác
- **Tài liệu Nguyên thủy**: Xác thực nguyên thủy máy chủ (Tài nguyên, Lời nhắc, Công cụ) và nguyên thủy máy khách (Lấy mẫu, Gợi ý, Ghi nhật ký, Roots)
- **Cơ chế Vận chuyển**: Xác minh tài liệu vận chuyển STDIO và HTTP có thể Stream chính xác
- **Hướng dẫn Bảo mật**: Xác nhận phù hợp với tài liệu Thực tiễn Tốt nhất Bảo mật MCP hiện tại

#### Tính năng chính MCP 2025-11-25 được tài liệu hóa
- **Khám phá OpenID Connect**: Khám phá máy chủ xác thực qua OIDC
- **Tài liệu Metadata OAuth Client ID**: Cơ chế đăng ký máy khách được đề xuất
- **JSON Schema 2020-12**: Ngôn ngữ mặc định cho định nghĩa schema MCP
- **Hệ thống Phân cấp SDK**: Yêu cầu chính thức hóa cho hỗ trợ và bảo trì tính năng SDK
- **Cấu trúc Quản trị**: Chính thức hóa Nhóm công tác và Nhóm quan tâm trong quản trị MCP

### Cập nhật lớn về Tài liệu Bảo mật (02-Security/)

#### Tích hợp MCP Security Summit Workshop (Sherpa)
- **Tài nguyên Đào tạo Thực hành Mới**: Thêm tích hợp toàn diện với [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) trong suốt tài liệu bảo mật
- **Bao phủ Lộ trình Hành trình**: Tài liệu hóa toàn bộ tiến trình từ trại Cơ sở đến Đỉnh núi
- **Phù hợp OWASP**: Tất cả hướng dẫn bảo mật hiện ánh xạ đến rủi ro trong OWASP MCP Azure Security Guide

#### Tích hợp OWASP MCP Top 10
- **Phần Mới**: Thêm bảng rủi ro bảo mật OWASP MCP Top 10 với các biện pháp giảm thiểu Azure vào README chính
- **Tài liệu Căn cứ trên Rủi ro**: Cập nhật mcp-security-controls-2025.md với tham chiếu rủi ro OWASP MCP cho mỗi lĩnh vực bảo mật
- **Kiến trúc Tham khảo**: Liên kết đến kiến trúc tham khảo và mẫu triển khai trong OWASP MCP Azure Security Guide

#### Tập tin Bảo mật Cập nhật
- **README.md**: Thêm tổng quan Sherpa Workshop, bảng lộ trình thám hiểm, tóm tắt rủi ro OWASP MCP Top 10 và phần đào tạo thực hành
- **mcp-security-controls-2025.md**: Cập nhật tiêu đề thành tháng 2 năm 2026, thêm tham chiếu rủi ro OWASP (MCP01-MCP08), sửa lỗi không nhất quán phiên bản đặc tả
- **mcp-security-best-practices-2025.md**: Thêm phần tài nguyên Sherpa và OWASP, cập nhật dấu thời gian
- **mcp-best-practices.md**: Thêm phần đào tạo thực hành với liên kết Sherpa và OWASP
- **azure-content-safety-implementation.md**: Thêm tham chiếu OWASP MCP06, phù hợp với Sherpa Camp 3 và phần tài nguyên bổ sung

#### Thêm Liên kết Tài nguyên Mới
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Trang rủi ro OWASP MCP cá nhân (MCP01-MCP10)

### Đồng bộ Toàn chương trình với MCP Specification 2025-11-25

#### Module 03 - Bắt đầu
- **Tài liệu SDK**: Thêm Go SDK vào danh sách SDK chính thức; cập nhật tất cả tham chiếu SDK để phù hợp với MCP Specification 2025-11-25
- **Làm rõ Vận chuyển**: Cập nhật mô tả vận chuyển STDIO và HTTP Streaming với tham chiếu đặc tả rõ ràng

#### Module 04 - Triển khai Thực tế
- **Cập nhật SDK**: Thêm Go SDK; cập nhật danh sách SDK với tham chiếu phiên bản đặc tả
- **Đặc tả Ủy quyền**: Cập nhật liên kết đặc tả MCP Authorization đến phiên bản hiện tại 2025-11-25

#### Module 05 - Chủ đề Nâng cao
- **Tính năng Mới**: Thêm chú thích về tính năng mới MCP Specification 2025-11-25 (Nhiệm vụ, Ghi chú Công cụ, URL Mode Elicitation, Roots)
- **Tài nguyên Bảo mật**: Thêm liên kết OWASP MCP Top 10 và Sherpa workshop vào tham khảo bổ sung

#### Module 06 - Đóng góp Cộng đồng
- **Danh sách SDK**: Thêm Swift và Rust SDKs; cập nhật liên kết đặc tả đến 2025-11-25
- **Tham chiếu Đặc tả**: Cập nhật liên kết MCP Specification đến URL đặc tả trực tiếp

#### Module 07 - Bài học Từ Áp dụng Sớm
- **Cập nhật Tài nguyên**: Thêm liên kết MCP Specification 2025-11-25 và OWASP MCP Top 10 vào tài nguyên bổ sung

#### Module 08 - Thực hành Tốt nhất
- **Phiên bản Đặc tả**: Cập nhật tham chiếu MCP Specification thành 2025-11-25
- **Tài nguyên Bảo mật**: Thêm OWASP MCP Top 10 và Sherpa workshop vào tham khảo bổ sung

#### Module 10 - Tinh giản Quy trình AI
- **Cập nhật Huy hiệu**: Thay đổi huy hiệu phiên bản MCP từ phiên bản SDK (1.9.3) sang phiên bản đặc tả (2025-11-25)
- **Liên kết Tài nguyên**: Cập nhật liên kết MCP Specification; thêm OWASP MCP Top 10

#### Module 11 - MCP Server Thực hành
- **Tham chiếu Đặc tả**: Cập nhật liên kết MCP Specification sang phiên bản 2025-11-25
- **Tài nguyên Bảo mật**: Thêm OWASP MCP Top 10 vào tài nguyên chính thức

## 18 tháng 12, 2025

### Cập nhật Tài liệu Bảo mật - MCP Specification 2025-11-25

#### Thực tiễn Tốt nhất Bảo mật MCP (02-Security/mcp-best-practices.md) - Cập nhật Phiên bản Đặc tả
- **Cập nhật Phiên bản Giao thức**: Cập nhật để tham chiếu MCP Specification 2025-11-25 mới nhất (phát hành ngày 25 tháng 11, 2025)
  - Cập nhật tất cả tham chiếu phiên bản đặc tả từ 2025-06-18 sang 2025-11-25
  - Cập nhật tham chiếu ngày tài liệu từ ngày 18 tháng 8, 2025 sang ngày 18 tháng 12, 2025
  - Xác minh tất cả URL đặc tả đều trỏ đến tài liệu hiện tại
- **Xác thực Nội dung**: Xác thực toàn diện các thực tiễn tốt nhất bảo mật so với tiêu chuẩn mới nhất
  - **Giải pháp Bảo mật Microsoft**: Xác minh thuật ngữ và liên kết hiện tại cho Prompt Shields (trước đây là "phát hiện rủi ro Jailbreak"), Azure Content Safety, Microsoft Entra ID và Azure Key Vault
  - **Bảo mật OAuth 2.1**: Xác nhận phù hợp với thực tiễn bảo mật OAuth mới nhất
  - **Tiêu chuẩn OWASP**: Xác nhận tham chiếu OWASP Top 10 cho LLM vẫn hiện hành
  - **Dịch vụ Azure**: Xác minh tất cả liên kết tài liệu Microsoft Azure và thực tiễn tốt nhất
- **Phù hợp Tiêu chuẩn**: Tất cả tiêu chuẩn bảo mật được tham chiếu xác nhận hiện hành
  - Khung Quản lý Rủi ro AI NIST
  - ISO 27001:2022
  - Thực tiễn Bảo mật OAuth 2.1
  - Các khung bảo mật và tuân thủ Azure
- **Tài nguyên Triển khai**: Xác minh tất cả liên kết hướng dẫn và tài nguyên triển khai
  - Mẫu xác thực Azure API Management
  - Hướng dẫn tích hợp Microsoft Entra ID
  - Quản lý bí mật Azure Key Vault
  - Các giải pháp pipeline DevSecOps và giám sát

### Đảm bảo Chất lượng Tài liệu
- **Tuân thủ Đặc tả**: Đảm bảo tất cả yêu cầu bảo mật MCP bắt buộc (MUST/MUST NOT) phù hợp với đặc tả mới nhất
- **Tính cập nhật của Tài nguyên**: Xác minh tất cả liên kết ngoài đến tài liệu Microsoft, tiêu chuẩn bảo mật và hướng dẫn triển khai
- **Phủ sóng Thực tiễn Tốt nhất**: Xác nhận bao phủ toàn diện các lĩnh vực xác thực, ủy quyền, mối đe dọa AI đặc thù, bảo mật chuỗi cung ứng và mẫu doanh nghiệp

## 6 tháng 10, 2025

### Mở rộng Phần Bắt đầu – Sử dụng Server Nâng cao & Xác thực Đơn giản

#### Sử dụng Server Nâng cao (03-GettingStarted/10-advanced)
- **Thêm Chương Mới**: Giới thiệu hướng dẫn đầy đủ về sử dụng server MCP nâng cao, bao gồm kiến trúc server thường và cấp thấp.
  - **Server Thường vs. Cấp thấp**: So sánh chi tiết và ví dụ mã Python và TypeScript cho cả hai cách tiếp cận.
  - **Thiết kế Dựa trên Handler**: Giải thích quản lý công cụ/tài nguyên/lời nhắc dựa trên handler cho các triển khai server có thể mở rộng và linh hoạt.
  - **Mẫu Thực tiễn**: Các kịch bản thực tế nơi mẫu server cấp thấp có lợi cho tính năng và kiến trúc nâng cao.

#### Xác thực Đơn giản (03-GettingStarted/11-simple-auth)
- **Thêm Chương Mới**: Hướng dẫn từng bước triển khai xác thực đơn giản trong server MCP.
  - **Khái niệm Xác thực**: Giải thích rõ ràng về xác thực và ủy quyền, cũng như xử lý thông tin đăng nhập.
  - **Triển khai Xác thực Cơ bản**: Mẫu xác thực dựa trên middleware trong Python (Starlette) và TypeScript (Express), kèm ví dụ mã.
  - **Tiến tới Bảo mật Nâng cao**: Hướng dẫn bắt đầu với xác thực đơn giản và tiến tới OAuth 2.1 và RBAC, kèm tham khảo các module bảo mật nâng cao.

Những bổ sung này cung cấp hướng dẫn thực hành, giúp xây dựng các triển khai server MCP vững chắc, an toàn và linh hoạt hơn, kết nối khái niệm nền tảng với mẫu sản xuất nâng cao.

## 29 tháng 9, 2025

### MCP Server Labs tích hợp Cơ sở dữ liệu - Lộ trình Học Tập Thực hành Toàn diện

#### 11-MCPServerHandsOnLabs - Chương trình học tích hợp cơ sở dữ liệu hoàn chỉnh
- **Lộ trình Học 13 Lab Toàn diện**: Thêm chương trình thực hành toàn diện để xây dựng server MCP sẵn sàng sản xuất với tích hợp cơ sở dữ liệu PostgreSQL
  - **Triển khai Thực tế**: Trường hợp phân tích Zava Retail minh họa mẫu doanh nghiệp
  - **Tiến trình Học Cấu trúc**:
    - **Labs 00-03: Nền tảng** - Giới thiệu, Kiến trúc Cốt lõi, Bảo mật & Đa thuê, Thiết lập Môi trường
    - **Labs 04-06: Xây dựng MCP Server** - Thiết kế & Lược đồ Cơ sở dữ liệu, Triển khai MCP Server, Phát triển Công cụ  
    - **Labs 07-09: Tính năng Nâng cao** - Tích hợp Tìm kiếm Ngữ nghĩa, Kiểm thử & Gỡ lỗi, Tích hợp VS Code
    - **Labs 10-12: Sản xuất & Thực hành Tốt nhất** - Chiến lược Triển khai, Giám sát & Quan sát, Thực hành tốt nhất & Tối ưu hóa
  - **Công nghệ Doanh nghiệp**: Khung FastMCP, PostgreSQL với pgvector, nhúng Azure OpenAI, Azure Container Apps, Application Insights
  - **Tính năng Nâng cao**: Bảo mật cấp dòng (Row Level Security - RLS), tìm kiếm ngữ nghĩa, truy cập dữ liệu đa thuê, nhúng vector, giám sát thời gian thực

#### Chuẩn hóa Thuật ngữ - Chuyển đổi Module thành Lab
- **Cập nhật Tài liệu Toàn diện**: Cập nhật hệ thống tất cả các file README trong 11-MCPServerHandsOnLabs sang thuật ngữ "Lab" thay cho "Module"
  - **Tiêu đề Mục**: Cập nhật "What This Module Covers" thành "What This Lab Covers" ở tất cả 13 lab
  - **Mô tả Nội dung**: Thay đổi "This module provides..." thành "This lab provides..." trong toàn bộ tài liệu
  - **Mục Tiêu Học Tập**: Cập nhật "By the end of this module..." thành "By the end of this lab..."
  - **Liên kết Điều hướng**: Chuyển đổi tất cả tham chiếu "Module XX:" sang "Lab XX:" trong tham chiếu chéo và điều hướng
  - **Theo dõi Hoàn thành**: Cập nhật "After completing this module..." thành "After completing this lab..."
  - **Giữ Nguyên Tham chiếu Kỹ thuật**: Bảo lưu tham chiếu module Python trong các file cấu hình (ví dụ, `"module": "mcp_server.main"`)

#### Cải thiện Hướng dẫn Học Tập (study_guide.md)
- **Bản đồ Chương trình Học Trực quan**: Thêm phần mới "11. Database Integration Labs" với trực quan hóa cấu trúc lab toàn diện
- **Cấu trúc Kho Lưu trữ**: Cập nhật từ mười thành mười một phần chính với mô tả chi tiết về 11-MCPServerHandsOnLabs
- **Hướng dẫn Lộ trình Học Tập**: Nâng cao chỉ dẫn điều hướng cho các phần 00-11
- **Bao phủ Công nghệ**: Thêm chi tiết công nghệ FastMCP, PostgreSQL, tích hợp dịch vụ Azure
- **Kết quả Học Tập**: Nhấn mạnh phát triển server sẵn sàng sản xuất, mẫu tích hợp cơ sở dữ liệu và bảo mật doanh nghiệp

#### Cải thiện Cấu trúc README Chính
- **Thuật ngữ Dựa trên Lab**: Cập nhật README.md chính trong 11-MCPServerHandsOnLabs sử dụng nhất quán cấu trúc "Lab"
- **Tổ chức Lộ trình Học Tập**: Tiến trình rõ ràng từ kiến thức cơ bản qua triển khai nâng cao đến triển khai sản xuất
- **Tập trung Thực tiễn Thế giới Thực**: Nhấn mạnh học tập thực hành với mẫu và công nghệ doanh nghiệp cấp sản xuất

### Cải thiện Chất lượng & Tính nhất quán Tài liệu
- **Nhấn mạnh Học tập Thực hành**: Tăng cường phương pháp tiếp cận dựa trên lab trong toàn bộ tài liệu
- **Tập trung Mẫu Doanh nghiệp**: Nêu bật triển khai sẵn sàng sản xuất và xem xét bảo mật doanh nghiệp
- **Tích hợp Công nghệ**: Bao phủ toàn diện các dịch vụ Azure hiện đại và mẫu tích hợp AI
- **Tiến trình Học Tập**: Lộ trình rõ ràng, có cấu trúc từ khái niệm cơ bản đến triển khai sản xuất

## 26 tháng 9, 2025

### Cải thiện Nghiên cứu Tình huống - Tích hợp MCP Registry trên GitHub

#### Nghiên cứu Tình huống (09-CaseStudy/) - Tập trung Phát triển Hệ sinh thái
- **README.md**: Mở rộng lớn với nghiên cứu tình huống toàn diện về MCP Registry GitHub
  - **Nghiên cứu MCP Registry GitHub**: Nghiên cứu đa chiều về ra mắt MCP Registry của GitHub vào tháng 9 năm 2025
    - **Phân tích Vấn đề**: Xem xét chi tiết các thách thức phân mảnh trong khám phá và triển khai server MCP
    - **Kiến trúc Giải pháp**: Cách tiếp cận registry tập trung của GitHub với cài đặt một cú nhấp chuột trong VS Code
    - **Tác động Kinh doanh**: Cải thiện đo lường được trong đưa nhà phát triển vào và năng suất
    - **Giá trị Chiến lược**: Tập trung vào triển khai agent mô-đun và tương tác đa công cụ
    - **Phát triển Hệ sinh thái**: Định vị là nền tảng cơ sở cho tích hợp agentic
  - **Cấu trúc Nghiên cứu Tăng cường**: Cập nhật bảy nghiên cứu tình huống với định dạng nhất quán và mô tả đầy đủ
    - Azure AI Travel Agents: Tập trung điều phối đa agent
    - Azure DevOps Integration: Tập trung tự động hóa quy trình công việc
    - Truy xuất Tài liệu Thời gian Thực: Triển khai client bảng điều khiển Python
    - Trình tạo Kế hoạch Học Tương tác: Ứng dụng web hội thoại Chainlit

    - Tài liệu trong trình soạn thảo: Tích hợp VS Code và GitHub Copilot
    - Quản lý API Azure: Các mẫu tích hợp API doanh nghiệp
    - GitHub MCP Registry: Phát triển hệ sinh thái và nền tảng cộng đồng
  - **Kết luận Toàn diện**: Viết lại phần kết luận nhấn mạnh bảy nghiên cứu điển hình trải dài nhiều khía cạnh triển khai MCP
    - Tích hợp Doanh nghiệp, Điều phối đa tác nhân, Năng suất nhà phát triển
    - Phát triển Hệ sinh thái, Phân loại Ứng dụng Giáo dục
    - Cải thiện hiểu biết về các mẫu kiến trúc, chiến lược triển khai và thực tiễn tốt nhất
    - Nhấn mạnh MCP như một giao thức trưởng thành, sẵn sàng cho sản xuất

#### Cập nhật Hướng dẫn Học tập (study_guide.md)
- **Bản đồ Chương trình Trực quan**: Cập nhật sơ đồ tư duy gồm GitHub MCP Registry trong phần Nghiên cứu điển hình
- **Mô tả Nghiên cứu điển hình**: Nâng cấp từ mô tả chung sang phân tích chi tiết bảy nghiên cứu điển hình toàn diện
- **Cấu trúc Kho lưu trữ**: Cập nhật mục 10 phản ánh phạm vi nghiên cứu điển hình toàn diện với các chi tiết triển khai cụ thể
- **Tích hợp Nhật ký Thay đổi**: Thêm mục ngày 26 tháng 9 năm 2025 ghi lại việc bổ sung GitHub MCP Registry và nâng cấp nghiên cứu điển hình
- **Cập nhật Ngày tháng**: Cập nhật dấu thời gian ở chân trang nhằm phản ánh sửa đổi mới nhất (26 tháng 9 năm 2025)

### Cải tiến Chất lượng Tài liệu
- **Tăng cường Tính nhất quán**: Chuẩn hóa định dạng và cấu trúc nghiên cứu điển hình trên tất cả bảy ví dụ
- **Phạm vi Toàn diện**: Nghiên cứu điển hình hiện bao phủ các kịch bản doanh nghiệp, năng suất nhà phát triển và phát triển hệ sinh thái
- **Định vị Chiến lược**: Tăng cường nhấn mạnh MCP như nền tảng cơ sở triển khai hệ thống tác nhân
- **Tích hợp Tài nguyên**: Cập nhật các tài nguyên bổ sung bao gồm liên kết GitHub MCP Registry

## 15 tháng 9, 2025

### Mở rộng Chủ đề Nâng cao - Giao Thông Tùy Chỉnh & Kỹ thuật Ngữ cảnh

#### Giao Thông Tùy Chỉnh MCP (05-AdvancedTopics/mcp-transport/) - Hướng dẫn Triển khai Nâng cao Mới
- **README.md**: Hướng dẫn triển khai đầy đủ cho các cơ chế giao thông MCP tùy chỉnh
  - **Giao Thông Azure Event Grid**: Triển khai giao thông sự kiện serverless toàn diện
    - Ví dụ C#, TypeScript, và Python tích hợp Azure Functions
    - Mẫu kiến trúc sự kiện cho các giải pháp MCP có khả năng mở rộng
    - Bộ nhận webhook và xử lý tin nhắn dựa trên push
  - **Giao Thông Azure Event Hubs**: Triển khai giao thông streaming hiệu suất cao
    - Khả năng streaming thời gian thực cho các kịch bản độ trễ thấp
    - Chiến lược phân vùng và quản lý điểm kiểm tra
    - Gộp tin nhắn và tối ưu hiệu năng
  - **Mẫu Tích hợp Doanh nghiệp**: Ví dụ kiến trúc sẵn sàng cho sản xuất
    - Xử lý MCP phân tán trên nhiều Azure Functions
    - Kiến trúc giao thông lai kết hợp nhiều loại giao thông
    - Chiến lược bền vững, độ tin cậy và xử lý lỗi tin nhắn
  - **Bảo mật & Giám sát**: Tích hợp Azure Key Vault và mẫu quan sát
    - Xác thực danh tính quản lý và quyền truy cập tối thiểu
    - Telemetry Application Insights và giám sát hiệu năng
    - Cầu dao mạch và mẫu chịu lỗi
  - **Khung Kiểm thử**: Chiến lược kiểm thử toàn diện cho giao thông tùy chỉnh
    - Kiểm thử đơn vị với test doubles và khung giả lập
    - Kiểm thử tích hợp với Azure Test Containers
    - Cân nhắc kiểm thử hiệu năng và tải

#### Kỹ thuật Ngữ cảnh (05-AdvancedTopics/mcp-contextengineering/) - Lĩnh vực AI Mới Nổi
- **README.md**: Khám phá toàn diện kỹ thuật ngữ cảnh như lĩnh vực mới nổi
  - **Nguyên tắc Cốt lõi**: Chia sẻ ngữ cảnh đầy đủ, nhận biết quyết định hành động, và quản lý cửa sổ ngữ cảnh
  - **Tương thích Giao thức MCP**: Cách thiết kế MCP giải quyết các thách thức kỹ thuật ngữ cảnh
    - Hạn chế cửa sổ ngữ cảnh và chiến lược tải dần
    - Xác định liên quan và truy xuất ngữ cảnh động
    - Xử lý ngữ cảnh đa mô-đun và cân nhắc bảo mật
  - **Phương pháp Triển khai**: Kiến trúc đa sợi đơn và đa tác nhân
    - Kỹ thuật phân đoạn và ưu tiên ngữ cảnh
    - Chiến lược tải dần và nén ngữ cảnh
    - Phương pháp ngữ cảnh phân lớp và tối ưu truy xuất
  - **Khung Đo lường**: Các chỉ số mới nổi đánh giá hiệu quả ngữ cảnh
    - Hiệu suất đầu vào, hiệu năng, chất lượng, và trải nghiệm người dùng
    - Phương pháp thử nghiệm tối ưu ngữ cảnh
    - Phân tích thất bại và phương pháp cải tiến

#### Cập nhật Điều hướng Chương trình (README.md)
- **Cấu trúc Mô-đun Nâng cao**: Cập nhật bảng chương trình để gồm các chủ đề nâng cao mới
  - Thêm mục Kỹ thuật Ngữ cảnh (5.14) và Giao Thông Tùy Chỉnh (5.15)
  - Định dạng và liên kết điều hướng đồng nhất trên các mô-đun
  - Cập nhật mô tả phản ánh phạm vi nội dung hiện tại

### Cải tiến Cấu trúc Thư mục
- **Chuẩn hóa Đặt tên**: Đổi tên "mcp transport" thành "mcp-transport" để đồng bộ với các thư mục chủ đề nâng cao khác
- **Tổ chức Nội dung**: Tất cả thư mục 05-AdvancedTopics hiện tuân theo mẫu đặt tên đồng nhất (mcp-[topic])

### Nâng cao Chất lượng Tài liệu
- **Tương thích Tiêu chuẩn MCP**: Tất cả nội dung mới tham chiếu MCP Specification 2025-06-18 hiện hành
- **Ví dụ Đa ngôn ngữ**: Ví dụ mã nguồn toàn diện bằng C#, TypeScript, và Python
- **Tập trung Doanh nghiệp**: Mẫu sẵn sàng sản xuất và tích hợp đám mây Azure xuyên suốt
- **Tài liệu Trực quan**: Biểu đồ Mermaid cho trực quan kiến trúc và luồng

## 18 tháng 8, 2025

### Cập nhật Toàn diện Tài liệu - Tiêu chuẩn MCP 2025-06-18

#### Thực hành Bảo mật MCP Tốt nhất (02-Security/) - Hiện đại hóa Toàn diện
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Viết lại hoàn toàn phù hợp với MCP Specification 2025-06-18
  - **Yêu cầu Bắt buộc**: Thêm yêu cầu phải/tuyệt đối không từ đặc tả chính thức với chỉ báo trực quan rõ ràng
  - **12 Thực hành Bảo mật Cốt lõi**: Tái cấu trúc từ danh sách 15 mục thành các miền bảo mật toàn diện
    - Bảo mật Token & Xác thực với tích hợp nhà cung cấp danh tính bên ngoài
    - Quản lý Phiên & Bảo mật Giao thông với yêu cầu mật mã
    - Bảo vệ Mối đe dọa AI đặc thù với tích hợp Microsoft Prompt Shields
    - Kiểm soát Truy cập & Quyền với nguyên tắc quyền tối thiểu
    - An toàn Nội dung & Giám sát với tích hợp Azure Content Safety
    - Bảo mật Chuỗi Cung ứng với xác minh thành phần toàn diện
    - Bảo mật OAuth & Ngăn ngừa Confused Deputy với triển khai PKCE
    - Ứng phó Sự cố & Khôi phục với khả năng tự động hóa
    - Tuân thủ & Quản trị với sự phù hợp quy định
    - Kiểm soát Bảo mật Nâng cao với kiến trúc zero trust
    - Tích hợp Hệ sinh thái Bảo mật Microsoft với các giải pháp toàn diện
    - Tiến hóa Bảo mật Liên tục với thực tiễn thích ứng
  - **Giải pháp Bảo mật Microsoft**: Hướng dẫn tích hợp tăng cường cho Prompt Shields, Azure Content Safety, Entra ID và GitHub Advanced Security
  - **Tài nguyên Triển khai**: Phân loại liên kết tài nguyên toàn diện theo Tài liệu MCP Chính thức, Giải pháp Bảo mật Microsoft, Tiêu chuẩn Bảo mật và Hướng dẫn Triển khai

#### Kiểm soát Bảo mật Nâng cao (02-Security/) - Triển khai Doanh nghiệp
- **MCP-SECURITY-CONTROLS-2025.md**: Cải tổ hoàn toàn với khung bảo mật cấp doanh nghiệp
  - **9 Miền Bảo mật Toàn diện**: Mở rộng từ các kiểm soát cơ bản thành khung doanh nghiệp chi tiết
    - Xác thực & Ủy quyền Nâng cao với tích hợp Microsoft Entra ID
    - Bảo mật Token & Kiểm soát Chống Passthrough với xác thực toàn diện
    - Kiểm soát Bảo mật Phiên với ngăn chặn chiếm quyền
    - Kiểm soát Bảo mật AI đặc thù với ngăn chặn prompt injection và tool poisoning
    - Ngăn ngừa tấn công Confused Deputy với bảo mật proxy OAuth
    - Bảo mật Thực thi Công cụ với sandboxing và cô lập
    - Kiểm soát Bảo mật Chuỗi Cung ứng với xác minh phụ thuộc
    - Kiểm soát Giám sát & Phát hiện với tích hợp SIEM
    - Ứng phó & Khôi phục Sự cố với khả năng tự động hóa
  - **Ví dụ Triển khai**: Thêm khối cấu hình YAML chi tiết và ví dụ mã nguồn
  - **Tích hợp Giải pháp Microsoft**: Bao phủ toàn diện dịch vụ bảo mật Azure, GitHub Advanced Security và quản lý danh tính doanh nghiệp

#### Bảo mật Chủ đề Nâng cao (05-AdvancedTopics/mcp-security/) - Triển khai Sẵn sàng Sản xuất
- **README.md**: Viết lại hoàn toàn cho triển khai bảo mật doanh nghiệp
  - **Phù hợp với Đặc tả Hiện hành**: Cập nhật đến MCP Specification 2025-06-18 với yêu cầu bảo mật bắt buộc
  - **Nâng cao Xác thực**: Tích hợp Microsoft Entra ID kèm ví dụ toàn diện .NET và Java Spring Security
  - **Tích hợp Bảo mật AI**: Triển khai Microsoft Prompt Shields và Azure Content Safety với ví dụ Python chi tiết
  - **Giảm thiểu Mối đe dọa Nâng cao**: Ví dụ hoàn chỉnh cho
    - Ngăn ngừa tấn công Confused Deputy với PKCE và xác thực đồng thuận người dùng
    - Ngăn Passthrough Token với xác thực đối tượng và quản lý token an toàn
    - Ngăn chặn chiếm quyền phiên với ràng buộc mật mã và phân tích hành vi
  - **Tích hợp Bảo mật Doanh nghiệp**: Giám sát Azure Application Insights, đường ống phát hiện mối đe dọa, và bảo mật chuỗi cung ứng
  - **Danh sách Kiểm tra Triển khai**: Kiểm soát bảo mật bắt buộc và đề xuất rõ ràng với lợi ích hệ sinh thái bảo mật Microsoft

### Chất lượng Tài liệu & Phù hợp Tiêu chuẩn
- **Tham chiếu Đặc tả**: Cập nhật tất cả tham chiếu đến MCP Specification 2025-06-18
- **Hệ sinh thái Bảo mật Microsoft**: Hướng dẫn tích hợp nâng cao xuyên suốt tài liệu bảo mật
- **Triển khai Thực tiễn**: Thêm ví dụ mã chi tiết trong .NET, Java và Python theo mẫu doanh nghiệp
- **Tổ chức Tài nguyên**: Phân loại toàn diện tài liệu chính thức, tiêu chuẩn bảo mật và hướng dẫn triển khai
- **Chỉ báo Trực quan**: Đánh dấu rõ ràng yêu cầu bắt buộc so với thực hành đề xuất


#### Khái niệm Cốt lõi (01-CoreConcepts/) - Hiện đại hóa Toàn diện
- **Cập nhật Phiên bản Giao thức**: Cập nhật tham chiếu MCP Specification 2025-06-18 với phiên bản dựa trên ngày (định dạng YYYY-MM-DD)
- **Tinh chỉnh Kiến trúc**: Mô tả nâng cao về Hosts, Clients, và Servers phản ánh mẫu kiến trúc MCP hiện tại
  - Hosts hiện được định nghĩa rõ ràng là ứng dụng AI điều phối nhiều kết nối client MCP
  - Clients được mô tả như kết nối giao thức duy trì quan hệ một-một với server
  - Servers được nâng cấp với các kịch bản triển khai cục bộ và từ xa
- **Tái cấu trúc Primitive**: Cải tổ hoàn toàn primitive của server và client
  - Primitive Server: Tài nguyên (nguồn dữ liệu), Prompts (mẫu), Công cụ (hàm thực thi) với giải thích và ví dụ chi tiết
  - Primitive Client: Sampling (hoàn thành LLM), Elicitation (đầu vào người dùng), Logging (gỡ lỗi/giám sát)
  - Cập nhật theo mẫu phương thức hiện tại phát hiện (`*/list`), truy xuất (`*/get`), và thực thi (`*/call`)
- **Kiến trúc Giao thức**: Giới thiệu mô hình kiến trúc hai lớp
  - Lớp Dữ liệu: Nền tảng JSON-RPC 2.0 với quản lý vòng đời và primitives
  - Lớp Giao thông: STDIO (cục bộ) và HTTP có khả năng stream với SSE (từ xa)
- **Khung Bảo mật**: Nguyên tắc bảo mật toàn diện bao gồm đồng thuận người dùng rõ ràng, bảo vệ dữ liệu riêng tư, an toàn thực thi công cụ, và bảo mật lớp giao thông
- **Mẫu Giao tiếp**: Cập nhật thông điệp giao thức hiển thị khởi tạo, phát hiện, thực thi, và luồng thông báo
- **Ví dụ Mã**: Làm mới ví dụ đa ngôn ngữ (.NET, Java, Python, JavaScript) phản ánh mẫu SDK MCP hiện tại

#### Bảo mật (02-Security/) - Cải tổ Bảo mật Toàn diện  
- **Phù hợp Tiêu chuẩn**: Toàn bộ phù hợp yêu cầu bảo mật MCP Specification 2025-06-18
- **Tiến hóa Xác thực**: Tài liệu tiến trình từ server OAuth tùy chỉnh sang ủy quyền nhà cung cấp danh tính bên ngoài (Microsoft Entra ID)
- **Phân tích Mối đe dọa Đặc thù AI**: Mở rộng bao phủ các vectơ tấn công AI hiện đại
  - Kịch bản tấn công prompt injection chi tiết với ví dụ thực tế
  - Cơ chế đầu độc công cụ và mẫu tấn công "kéo thảm" (rug pull)
  - Đầu độc cửa sổ ngữ cảnh và các tấn công gây nhầm lẫn mô hình
- **Giải pháp Bảo mật AI Microsoft**: Bao phủ toàn diện hệ sinh thái bảo mật Microsoft
  - AI Prompt Shields với phát hiện nâng cao, làm nổi bật, và kỹ thuật phân tách
  - Mẫu tích hợp Azure Content Safety
  - GitHub Advanced Security cho bảo vệ chuỗi cung ứng
- **Giảm thiểu Mối đe dọa Nâng cao**: Kiểm soát bảo mật chi tiết cho
  - Chiếm quyền phiên với kịch bản tấn công MCP và yêu cầu ID phiên mật mã
  - Vấn đề confused deputy trong kịch bản proxy MCP với yêu cầu đồng thuận rõ ràng
  - Lỗ hổng passthrough token với kiểm soát xác thực bắt buộc
- **Bảo mật Chuỗi Cung ứng**: Mở rộng bảo vệ chuỗi cung ứng AI bao gồm mô hình nền tảng, dịch vụ embeddings, nhà cung cấp ngữ cảnh, và API bên thứ ba
- **Bảo mật Nền tảng**: Tăng cường tích hợp với mẫu bảo mật doanh nghiệp bao gồm kiến trúc zero trust và hệ sinh thái bảo mật Microsoft
- **Tổ chức Tài nguyên**: Phân loại liên kết tài nguyên toàn diện theo loại (Tài liệu Chính thức, Tiêu chuẩn, Nghiên cứu, Giải pháp Microsoft, Hướng dẫn Triển khai)

### Cải tiến Chất lượng Tài liệu
- **Mục tiêu Học tập Cấu trúc**: Nâng cao mục tiêu học tập với kết quả cụ thể, khả thi 
- **Tham chiếu Chéo**: Thêm liên kết giữa các chủ đề bảo mật và khái niệm cốt lõi liên quan
- **Thông tin Hiện hành**: Cập nhật tất cả tham chiếu ngày tháng và liên kết đặc tả theo tiêu chuẩn hiện hành
- **Hướng dẫn Triển khai**: Thêm hướng dẫn triển khai cụ thể và khả thi trong cả hai phần

## 16 tháng 7, 2025

### Cải tiến README và Điều hướng
- Thiết kế lại hoàn toàn điều hướng chương trình trong README.md
- Thay thế thẻ `<details>` bằng định dạng bảng dễ tiếp cận hơn
- Tạo các tùy chọn bố cục thay thế trong thư mục "alternative_layouts" mới
- Thêm ví dụ điều hướng kiểu thẻ, kiểu tab, và kiểu accordion
- Cập nhật phần cấu trúc kho lưu trữ để bao gồm tất cả tập tin mới nhất
- Nâng cao phần "Cách sử dụng Chương trình này" với khuyến nghị rõ ràng
- Cập nhật liên kết đặc tả MCP để trỏ đến URL đúng
- Thêm phần Kỹ thuật Ngữ cảnh (5.14) vào cấu trúc chương trình

### Cập nhật Hướng dẫn Học tập
- Viết lại hoàn toàn hướng dẫn học tập để phù hợp với cấu trúc kho lưu trữ hiện tại
- Thêm các phần mới cho MCP Clients và Tools, cùng các MCP Servers phổ biến
- Cập nhật Bản đồ Chương trình Trực quan để phản ánh chính xác tất cả chủ đề
- Nâng cấp mô tả các Chủ đề Nâng cao để bao phủ toàn diện tất cả lĩnh vực chuyên biệt
- Cập nhật phần Nghiên cứu điển hình để phản ánh các ví dụ thực tế
- Thêm nhật ký thay đổi toàn diện này

### Đóng góp Cộng đồng (06-CommunityContributions/)
- Thêm thông tin chi tiết về MCP servers cho tạo ảnh
- Thêm phần toàn diện về sử dụng Claude trong VSCode
- Thêm hướng dẫn thiết lập và sử dụng terminal client Cline
- Cập nhật phần MCP client để bao gồm tất cả lựa chọn client phổ biến
- Nâng cao ví dụ đóng góp với mẫu mã chính xác hơn

### Chủ đề Nâng cao (05-AdvancedTopics/)
- Tổ chức tất cả thư mục chủ đề chuyên biệt với cách đặt tên nhất quán
- Thêm tài liệu và ví dụ kỹ thuật ngữ cảnh
- Thêm tài liệu tích hợp tác nhân Foundry
- Nâng cao tài liệu tích hợp bảo mật Entra ID

## 11 tháng 6, 2025

### Tạo Lập Ban đầu
- Phát hành phiên bản đầu tiên của chương trình MCP dành cho Người mới bắt đầu

- Tạo cấu trúc cơ bản cho tất cả 10 phần chính
- Triển khai Bản đồ Chương trình học trực quan cho điều hướng
- Thêm các dự án mẫu ban đầu bằng nhiều ngôn ngữ lập trình

### Bắt đầu (03-GettingStarted/)
- Tạo ví dụ triển khai máy chủ đầu tiên
- Thêm hướng dẫn phát triển client
- Bao gồm hướng dẫn tích hợp client LLM
- Thêm tài liệu tích hợp VS Code
- Triển khai ví dụ máy chủ Server-Sent Events (SSE)

### Khái niệm cốt lõi (01-CoreConcepts/)
- Thêm giải thích chi tiết về kiến trúc client-server
- Tạo tài liệu về các thành phần giao thức chính
- Tài liệu các mô hình nhắn tin trong MCP

## 23 tháng 5, 2025

### Cấu trúc Kho lưu trữ
- Khởi tạo kho với cấu trúc thư mục cơ bản
- Tạo các file README cho mỗi phần chính
- Thiết lập hạ tầng dịch thuật
- Thêm tài nguyên hình ảnh và sơ đồ

### Tài liệu
- Tạo README.md ban đầu với tổng quan chương trình học
- Thêm CODE_OF_CONDUCT.md và SECURITY.md
- Thiết lập SUPPORT.md với hướng dẫn nhận hỗ trợ
- Tạo cấu trúc hướng dẫn học tập sơ bộ

## 15 tháng 4, 2025

### Lập kế hoạch và Khung
- Lập kế hoạch ban đầu cho chương trình MCP dành cho Người mới bắt đầu
- Xác định mục tiêu học tập và đối tượng mục tiêu
- Phác thảo cấu trúc 10 phần của chương trình học
- Phát triển khung khái niệm cho ví dụ và nghiên cứu tình huống
- Tạo ví dụ nguyên mẫu ban đầu cho các khái niệm chính

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->