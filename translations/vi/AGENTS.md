# AGENTS.md

## Tổng quan về dự án

**MCP dành cho người mới bắt đầu** là một chương trình học mở nguồn về giao thức Model Context Protocol (MCP) - một khuôn khổ tiêu chuẩn hóa cho sự tương tác giữa các mô hình AI và các ứng dụng khách. Kho lưu trữ này cung cấp tài liệu học tập toàn diện với các ví dụ mã thực hành trên nhiều ngôn ngữ lập trình.

### Công nghệ chính

- **Ngôn ngữ lập trình**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework & SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Cơ sở dữ liệu**: PostgreSQL với phần mở rộng pgvector
- **Nền tảng đám mây**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Công cụ xây dựng**: npm, Maven, pip, Cargo
- **Tài liệu**: Markdown với dịch tự động đa ngôn ngữ (hơn 48 ngôn ngữ)

### Kiến trúc

- **11 mô-đun lõi (00-11)**: Lộ trình học tuần tự từ cơ bản đến nâng cao
- **Phòng thí nghiệm thực hành**: Bài tập thực tế với mã giải pháp hoàn chỉnh trên nhiều ngôn ngữ
- **Dự án mẫu**: Các triển khai máy chủ và ứng dụng khách MCP hoạt động được
- **Hệ thống dịch thuật**: Quy trình làm việc Github Actions tự động hỗ trợ đa ngôn ngữ
- **Tài sản hình ảnh**: Thư mục tập trung hình ảnh với các phiên bản đã dịch

## Lệnh thiết lập

Đây là kho tài liệu tập trung. Hầu hết việc thiết lập diễn ra trong các dự án mẫu và phòng thí nghiệm riêng biệt.

### Thiết lập kho lưu trữ

```bash
# Sao chép kho lưu trữ
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Làm việc với dự án mẫu

Các dự án mẫu nằm ở:
- `03-GettingStarted/samples/` - Ví dụ theo từng ngôn ngữ
- `03-GettingStarted/01-first-server/solution/` - Các triển khai máy chủ đầu tiên
- `03-GettingStarted/02-client/solution/` - Các triển khai ứng dụng khách
- `11-MCPServerHandsOnLabs/` - Phòng thí nghiệm tích hợp cơ sở dữ liệu toàn diện

Mỗi dự án mẫu có hướng dẫn thiết lập riêng:

#### Dự án TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Dự án Python
```bash
cd <project-directory>
pip install -r requirements.txt
# hoặc
pip install -e .
python main.py
```

#### Dự án Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Quy trình phát triển

### Sẵn sàng MCP 7-28

#### Danh sách kiểm tra sẵn sàng repo

- [x] **Rõ ràng cho người đóng góp mới**: Tệp này định nghĩa mục đích kho,
  cấu trúc, quy tắc đóng góp và đường dẫn thiết lập mẫu.
- [x] **Lệnh xây dựng/kiểm tra/lint với cờ chính xác**:
  - Kiểm tra lint tài liệu kho lưu trữ:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Kiểm tra mẫu đường dẫn liên kết tài liệu kho:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Xác thực mẫu TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Xác thực mẫu Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Xác thực mẫu Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Một quy trình công việc thực tế có thể trở thành công cụ MCP**:
  `validate_curriculum_change`
- [x] **Đầu vào/đầu ra rõ ràng** (xem đặc tả bên dưới).
- [x] **Quyền và các chế độ lỗi được ghi chép** (xem đặc tả bên dưới).
- [x] **Khả năng kiểm thử CI rõ ràng** (lệnh xác định, mã thoát rõ ràng,
  và đầu ra có thể đọc bằng máy).

#### Quy trình công cụ MCP ứng viên: `validate_curriculum_change`

##### Mục tiêu

Xác thực các thay đổi tài liệu chương trình và mã mẫu đại diện
trước khi hợp nhất.

##### Đầu vào

- `changed_paths: string[]` (bắt buộc) - đường dẫn tương đối thay đổi trong PR.
- `run_docs_lint: boolean` (mặc định `true`)
- `run_links_audit: boolean` (mặc định `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (mặc định tất cả `false`)

##### Đầu ra

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Quyền hạn

- Chỉ đọc file không gian làm việc và ghi tác phẩm do công cụ tạo ra (ví dụ, báo cáo lint,
  nhật ký kiểm thử); không ghi `translations/` hoặc
  `translated_images/`.
- Thực thi các lệnh shell cục bộ.
- Truy cập mạng tùy chọn chỉ được dùng để phục hồi gói (`npm ci`,
  `python -m pip install`, `mvn` phân giải phụ thuộc).
- Không có quyền đẩy, gộp hoặc sửa đổi `translations/` hoặc
  `translated_images/`.

##### Chế độ lỗi

- `E_NO_INPUT_PATHS`: `changed_paths` trống.
- `E_INVALID_PATH`: đường dẫn đầu vào thoát khỏi gốc kho lưu trữ.
- `E_LINT_FAILED`: lint markdown thoát không bằng 0.
- `E_LINK_AUDIT_FAILED`: lệnh kiểm tra liên kết thoát không bằng 0.
- `E_SAMPLE_TEST_FAILED`: kiểm thử/máy xây mẫu thoát không bằng 0.
- `E_TIMEOUT`: lệnh vượt quá thời gian cấu hình.

##### Hợp đồng CI được đề xuất

Để tự động xác thực, cấu hình một công việc CI mà:

- Kích hoạt khi có yêu cầu kéo ảnh hưởng `*.md`, mã mẫu hoặc tệp này.
- Chạy các lệnh chính xác đã liệt kê ở trên.
- Lưu trữ nhật ký dưới dạng tác phẩm.
- Công việc thất bại khi có mã thoát khác 0.

#### Nếu bạn phát hành một máy chủ MCP từ kho này

- [ ] Đọc nhật ký thay đổi MCP cuối cùng `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Xác minh bản phát hành SDK được chọn hỗ trợ MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Loại bỏ giả định phiên và bắt tay; xem mỗi yêu cầu như
  một thực thể độc lập:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Gửi tiêu đề `Mcp-Method` và `Mcp-Name` cho các yêu cầu HTTP thô:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Kiểm toán mã lỗi cứng (`missing resource` chuyển từ `-32002` sang `-32602`).

- [ ] Di cư các Roots, Sampling, Logging và Dynamic Client đã lỗi thời
  Đăng ký:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Di cư khỏi API Nhiệm vụ thử nghiệm `2025-11-25`:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Rà soát ủy quyền để củng cố OAuth và OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Cấu trúc Tài liệu

- **Modules 00-11**: Nội dung chương trình cốt lõi theo thứ tự tuần tự
- **translations/**: Phiên bản ngôn ngữ cụ thể (tự động tạo, không chỉnh sửa trực tiếp)
- **translated_images/**: Phiên bản hình ảnh địa phương hóa (tự động tạo)
- **images/**: Hình ảnh và sơ đồ nguồn

### Thực hiện Thay đổi Tài liệu

1. Chỉ chỉnh sửa các tệp markdown tiếng Anh trong các thư mục module gốc (00-11)
2. Cập nhật hình ảnh trong thư mục `images/` nếu cần
3. Hành động GitHub co-op-translator sẽ tự động tạo bản dịch
4. Bản dịch được tạo lại khi đẩy lên nhánh chính

### Làm việc với Các Bản dịch

- **Dịch tự động**: Quy trình làm việc GitHub Actions xử lý tất cả các bản dịch
- **KHÔNG chỉnh sửa thủ công** các tệp trong thư mục `translations/`
- Metadữ liệu bản dịch được nhúng trong mỗi tệp dịch
- Các ngôn ngữ được hỗ trợ: hơn 48 ngôn ngữ bao gồm Ả Rập, Trung Quốc, Pháp, Đức, Hindi, Nhật, Hàn, Bồ Đào Nha, Nga, Tây Ban Nha và nhiều hơn nữa

## Hướng dẫn Kiểm thử

### Xác thực Tài liệu

Vì đây chủ yếu là kho tài liệu, kiểm thử tập trung vào:

1. **Kiểm tra Mẫu Liên kết**: Liệt kê các liên kết Markdown để rà soát

   ```bash
   # Liệt kê các liên kết Markdown (kiểm tra mẫu)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Xác thực Ví dụ Mã**: Kiểm tra ví dụ mã có thể biên dịch/chạy được

   ```bash
   # Điều hướng đến mẫu cụ thể và chạy các bài kiểm tra của nó
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Kiểm tra Lint Markdown**: Kiểm tra độ nhất quán định dạng

   ```bash
   # Sử dụng markdownlint nếu cần thiết
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Kiểm thử Dự án Mẫu

Mỗi mẫu ngôn ngữ có phương pháp kiểm thử riêng:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Hướng dẫn Phong cách Mã

### Phong cách Tài liệu

- Sử dụng ngôn ngữ rõ ràng, thân thiện với người mới bắt đầu
- Bao gồm ví dụ mã trong nhiều ngôn ngữ khi có thể
- Tuân theo các thực tiễn tốt nhất về markdown:
  - Sử dụng tiêu đề kiểu ATX (cú pháp `#`)
  - Sử dụng các khối mã có hàng rào với định danh ngôn ngữ
  - Bao gồm văn bản alt mô tả cho hình ảnh
  - Giữ độ dài dòng hợp lý (không giới hạn cứng, nhưng cần hợp lý)

### Phong cách Ví dụ Mã

#### TypeScript/JavaScript
- Sử dụng các module ES (`import`/`export`)
- Tuân theo quy ước chế độ nghiêm ngặt TypeScript
- Bao gồm chú thích kiểu
- Mục tiêu ES2022

#### Python
- Tuân theo hướng dẫn phong cách PEP 8
- Sử dụng gợi ý kiểu khi phù hợp
- Bao gồm docstring cho hàm và lớp
- Sử dụng các tính năng Python hiện đại (3.8+)

#### Java
- Tuân theo quy ước Spring Boot
- Sử dụng các tính năng Java 21
- Tuân theo cấu trúc dự án Maven chuẩn
- Bao gồm chú thích Javadoc

### Tổ chức Tệp

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Xây dựng và Triển khai

### Triển khai Tài liệu

Kho lưu trữ sử dụng GitHub Pages hoặc tương tự để lưu trữ tài liệu (nếu có). Thay đổi lên nhánh chính sẽ kích hoạt:

1. Quy trình làm việc bản dịch (`.github/workflows/co-op-translator.yml`)
2. Dịch tự động tất cả các tệp markdown tiếng Anh

3. Định vị hình ảnh khi cần thiết

### Không cần quy trình xây dựng

Kho lưu trữ này chủ yếu chứa tài liệu markdown. Không cần biên dịch hoặc bước xây dựng cho nội dung chương trình học cốt lõi.

### Triển khai dự án mẫu

Các dự án mẫu riêng lẻ có thể có hướng dẫn triển khai:
- Xem `03-GettingStarted/09-deployment/` để hướng dẫn triển khai máy chủ MCP
- Ví dụ triển khai Azure Container Apps trong `11-MCPServerHandsOnLabs/`

## Hướng dẫn đóng góp

### Quy trình Pull Request

1. **Fork và Clone**: Fork kho lưu trữ và clone bản fork của bạn về máy
2. **Tạo nhánh**: Sử dụng tên nhánh mô tả (ví dụ: `fix/typo-module-3`, `add/python-example`)
3. **Thực hiện thay đổi**: Chỉ chỉnh sửa các tệp markdown tiếng Anh (không chỉnh sửa bản dịch)
4. **Kiểm tra cục bộ**: Xác nhận markdown hiển thị đúng
5. **Gửi PR**: Sử dụng tiêu đề và mô tả PR rõ ràng
6. **CLA**: Ký Thỏa thuận Giấy phép Đóng góp của Microsoft khi được yêu cầu

### Định dạng tiêu đề PR

Sử dụng tiêu đề rõ ràng, mô tả:
- `[Module XX] Mô tả ngắn` cho thay đổi riêng từng module
- `[Samples] Mô tả` cho thay đổi mẫu mã nguồn
- `[Docs] Mô tả` cho cập nhật tài liệu chung

### Những gì cần đóng góp

- Sửa lỗi trong tài liệu hoặc mẫu mã
- Ví dụ mã nguồn mới bằng các ngôn ngữ bổ sung
- Làm rõ và cải thiện nội dung hiện có
- Nghiên cứu trường hợp hoặc ví dụ thực tiễn mới
- Báo cáo lỗi cho nội dung không rõ hoặc sai

### Những gì KHÔNG nên làm

- Không chỉnh sửa trực tiếp các tệp trong thư mục `translations/`
- Không chỉnh sửa thư mục `translated_images/`
- Không thêm tệp nhị phân lớn nếu chưa thảo luận
- Không thay đổi các tệp quy trình dịch thuật nếu chưa phối hợp

## Ghi chú bổ sung

### Bảo trì kho lưu trữ

- **Changelog**: Tất cả thay đổi quan trọng được ghi lại trong `changelog.md`
- **Hướng dẫn học tập**: Sử dụng `study_guide.md` để tổng quan định hướng chương trình học
- **Mẫu báo cáo lỗi**: Sử dụng mẫu báo cáo lỗi trên GitHub để báo lỗi và đề xuất tính năng
- **Quy tắc ứng xử**: Tất cả người đóng góp phải tuân thủ Quy tắc Ứng xử mã nguồn mở của Microsoft

### Lộ trình học

Theo các module theo thứ tự tuần tự (00-11) để học hiệu quả:
1. **00-02**: Những kiến thức nền tảng (Giới thiệu, Khái niệm cốt lõi, An ninh)
2. **03**: Bắt đầu với thực hành làm việc trực tiếp
3. **04-05**: Thực hành và các chủ đề nâng cao
4. **06-10**: Cộng đồng, thực hành tốt nhất, và ứng dụng thực tế
5. **11**: Các bài lab tích hợp cơ sở dữ liệu toàn diện (13 bài liên tiếp)

### Tài nguyên hỗ trợ

- **Tài liệu**: https://modelcontextprotocol.io/
- **Đặc tả**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Cộng đồng**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Máy chủ Discord Microsoft Foundry
- **Khóa học liên quan**: Xem README.md để biết các lộ trình học khác của Microsoft

### Xử lý sự cố phổ biến

**Q: PR của tôi bị lỗi kiểm tra bản dịch**
A: Đảm bảo bạn chỉ chỉnh sửa các tệp markdown tiếng Anh trong thư mục module gốc, không chỉnh sửa các bản dịch.

**Q: Làm thế nào để tôi thêm ngôn ngữ mới?**
A: Hỗ trợ ngôn ngữ được quản lý thông qua quy trình làm việc co-op-translator. Mở một issue để thảo luận về việc thêm ngôn ngữ mới.

**Q: Mẫu mã không hoạt động**

A: Đảm bảo bạn đã làm theo hướng dẫn cài đặt trong README của mẫu cụ thể đó. Kiểm tra xem bạn đã cài đặt đúng phiên bản các phụ thuộc chưa.


**Hỏi: Hình ảnh không hiển thị**

A: Xác minh rằng các đường dẫn hình ảnh là đường dẫn tương đối và sử dụng dấu gạch chéo xuôi. Hình ảnh nên nằm trong thư mục `images/` hoặc `translated_images/` cho các phiên bản đã được dịch thuật.

### Các cân nhắc về hiệu suất

- Quy trình dịch có thể mất vài phút để hoàn thành
- Hình ảnh lớn nên được tối ưu hóa trước khi cam kết
- Giữ các file markdown riêng lẻ tập trung và có kích thước hợp lý
- Sử dụng liên kết tương đối để tăng khả năng di động

### Quản trị dự án

Dự án này tuân theo các thực hành mã nguồn mở của Microsoft:
- Giấy phép MIT cho mã và tài liệu
- Bộ Quy tắc ứng xử Mã nguồn mở của Microsoft
- Yêu cầu CLA cho các đóng góp
- Vấn đề bảo mật: Tuân theo hướng dẫn trong SECURITY.md
- Hỗ trợ: Xem SUPPORT.md để biết tài nguyên trợ giúp

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->