# AGENTS.md

## Tổng quan dự án

**MCP cho người mới bắt đầu** là một khóa học giáo dục mã nguồn mở để học Giao thức Ngữ cảnh Mô hình (MCP) - một khuôn khổ chuẩn hóa cho các tương tác giữa các mô hình AI và ứng dụng khách. Kho lưu trữ này cung cấp tài liệu học tập toàn diện với các ví dụ mã thực hành trên nhiều ngôn ngữ lập trình.

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

- **11 mô-đun chính (00-11)**: Lộ trình học tuần tự từ cơ bản tới nâng cao
- **Phòng thí nghiệm thực hành**: Bài tập thực tế với mã giải pháp hoàn chỉnh trên nhiều ngôn ngữ
- **Dự án mẫu**: Các triển khai máy chủ và khách MCP hoạt động
- **Hệ thống dịch**: Quy trình làm việc GitHub Actions tự động cho đa ngôn ngữ
- **Tập tin hình ảnh**: Thư mục hình ảnh tập trung với các phiên bản đã dịch

## Lệnh thiết lập

Đây là kho tài liệu tập trung. Hầu hết việc thiết lập diễn ra trong các dự án mẫu và phòng thí nghiệm riêng biệt.

### Thiết lập kho lưu trữ

```bash
# Sao chép kho lưu trữ
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Làm việc với dự án mẫu

Các dự án mẫu nằm trong:
- `03-GettingStarted/samples/` - Ví dụ theo ngôn ngữ
- `03-GettingStarted/01-first-server/solution/` - Các triển khai máy chủ đầu tiên
- `03-GettingStarted/02-client/solution/` - Các triển khai phía khách
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

### Chuẩn bị MCP 7-28

#### Danh sách kiểm tra chuẩn bị kho lưu trữ

- [x] **Sự rõ ràng cho cộng tác viên mới**: Tệp này định nghĩa mục đích kho lưu trữ,
  cấu trúc, quy tắc đóng góp và các đường dẫn thiết lập mẫu.
- [x] **Lệnh build/test/lint với cờ chính xác**:
  - Lint tài liệu kho lưu trữ:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Kiểm tra mẫu liên kết tài liệu kho lưu trữ:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Xác nhận mẫu TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Xác nhận mẫu Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Xác nhận mẫu Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`

- [x] **Một quy trình làm việc thực tế có thể trở thành công cụ MCP**:
  `validate_curriculum_change`
- [x] **Đầu vào/đầu ra rõ ràng** (xem đặc tả bên dưới).
- [x] **Quyền hạn và các chế độ thất bại được ghi nhận** (xem đặc tả bên dưới).
- [x] **Khả năng kiểm thử CI rõ ràng** (lệnh xác định, mã thoát rõ ràng và đầu ra có thể đọc bởi máy).
  exit codes, and machine-readable outputs).

#### Quy trình công cụ MCP ứng viên: `validate_curriculum_change`

##### Mục tiêu

Xác thực các thay đổi tài liệu chương trình giảng dạy và sức khỏe mã mẫu đại diện
trước khi hợp nhất.

##### Đầu vào

- `changed_paths: string[]` (bắt buộc) - các đường dẫn tương đối đã thay đổi trong PR.
- `run_docs_lint: boolean` (mặc định `true`)
- `run_links_audit: boolean` (mặc định `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (mặc định tất cả `false`)

##### Đầu ra

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,`
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Quyền hạn

- Đọc các tệp trong workspace và ghi các tài liệu được tạo bởi công cụ (ví dụ, báo cáo lint,
  nhật ký kiểm thử) chỉ; không ghi vào `translations/` hoặc
  `translated_images/`.
- Thực thi các lệnh shell cục bộ.
- Truy cập mạng tùy chọn chỉ để phục hồi gói (`npm ci`,
  `python -m pip install`, giải quyết phụ thuộc `mvn`).
- Không có quyền đẩy, hợp nhất hoặc chỉnh sửa `translations/` hoặc
  `translated_images/`.

##### Chế độ thất bại

- `E_NO_INPUT_PATHS`: `changed_paths` rỗng.
- `E_INVALID_PATH`: đường dẫn đầu vào thoát ra khỏi gốc kho lưu trữ.
- `E_LINT_FAILED`: lệnh lint markdown thoát với mã khác không.
- `E_LINK_AUDIT_FAILED`: lệnh kiểm tra liên kết thoát với mã khác không.
- `E_SAMPLE_TEST_FAILED`: thử nghiệm/mô hình mẫu thoát với mã khác không.
- `E_TIMEOUT`: lệnh vượt quá thời gian cấu hình.

##### Hợp đồng CI được khuyến nghị

Để tự động hóa xác thực, cấu hình một công việc CI mà:

- Kích hoạt trên các pull request chạm tới `*.md`, mã mẫu hoặc tệp này.
- Chạy chính xác các lệnh liệt kê ở trên.
- Lưu lại nhật ký làm tài liệu.
- Không thành công công việc nếu có bất kỳ mã thoát nào khác không.

#### Nếu bạn triển khai một máy chủ MCP từ kho này

- [ ] Đọc bản nháp nhật ký thay đổi cho MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Chạy máy chủ của bạn với các bản beta SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Loại bỏ các giả định phiên và bắt tay; xử lý mỗi yêu cầu như
  tự chứa:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Gửi các tiêu đề `Mcp-Method` và `Mcp-Name` cho các yêu cầu HTTP thô:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Kiểm tra các mã lỗi cứng (`missing resource` đã chuyển từ `-32002` sang `-32602`).

- [ ] Đánh dấu và lập kế hoạch di chuyển cho các root, sampling, và
  ghi nhật ký bị ngừng sử dụng:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Di chuyển khỏi API Tasks thử nghiệm `2025-11-25`:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Xem xét quyền xác thực cho OAuth và OpenID Connect cứng hóa:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Cấu trúc Tài liệu

- **Modules 00-11**: Nội dung chương trình chính theo thứ tự tuần tự
- **translations/**: Phiên bản theo ngôn ngữ (tự động tạo, không chỉnh sửa trực tiếp)
- **translated_images/**: Phiên bản hình ảnh đã địa phương hóa (tự động tạo)
- **images/**: Hình ảnh nguồn và sơ đồ

### Thực hiện Thay đổi Tài liệu

1. Chỉ chỉnh sửa các tệp markdown tiếng Anh trong thư mục mô-đun gốc (00-11)
2. Cập nhật hình ảnh trong thư mục `images/` nếu cần
3. Hành động GitHub co-op-translator sẽ tự động tạo bản dịch
4. Bản dịch được tái tạo lại khi đẩy lên nhánh chính

### Làm việc với Bản dịch

- **Dịch tự động**: Quy trình GitHub Actions xử lý tất cả bản dịch
- **KHÔNG chỉnh sửa thủ công** các tệp trong thư mục `translations/`
- Metadata bản dịch được nhúng trong mỗi tệp đã dịch
- Ngôn ngữ được hỗ trợ: hơn 48 ngôn ngữ bao gồm Ả Rập, Trung, Pháp, Đức, Hindi, Nhật, Hàn, Bồ Đào Nha, Nga, Tây Ban Nha, và nhiều hơn nữa

## Hướng Dẫn Kiểm Thử

### Xác thực Tài liệu

Vì đây chủ yếu là kho lưu trữ tài liệu, việc kiểm thử tập trung vào:

1. **Kiểm tra Mẫu Liên kết**: Liệt kê các liên kết Markdown để xem xét

   ```bash
   # Liệt kê các liên kết Markdown (kiểm tra mẫu)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Xác thực Mẫu Mã**: Kiểm tra các ví dụ mã biên dịch/chạy được

   ```bash
   # Điều hướng đến mẫu cụ thể và chạy các bài kiểm tra của nó
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown**: Kiểm tra tính nhất quán định dạng

   ```bash
   # Sử dụng markdownlint nếu cần thiết
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Kiểm Thử Dự Án Mẫu

Mỗi ví dụ mẫu theo ngôn ngữ đều bao gồm cách tiếp cận kiểm thử riêng:

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

## Hướng Dẫn Phong Cách Mã

### Phong Cách Tài liệu

- Sử dụng ngôn ngữ rõ ràng, thân thiện với người mới bắt đầu
- Bao gồm ví dụ mã trong nhiều ngôn ngữ khi thích hợp
- Tuân theo các thực hành tốt nhất của markdown:
  - Sử dụng tiêu đề kiểu ATX (`#` syntax)
  - Sử dụng khối mã có rào chắn với định danh ngôn ngữ
  - Bao gồm văn bản thay thế mô tả cho hình ảnh
  - Giữ độ dài dòng hợp lý (không giới hạn cứng, nhưng hợp lý)

### Phong Cách Ví dụ Mã

#### TypeScript/JavaScript
- Sử dụng mô-đun ES (`import`/`export`)
- Tuân theo quy ước chế độ nghiêm ngặt của TypeScript
- Bao gồm chú thích kiểu
- Hướng đến ES2022

#### Python
- Tuân theo hướng dẫn phong cách PEP 8
- Sử dụng gợi ý kiểu khi thích hợp
- Bao gồm docstring cho hàm và lớp
- Sử dụng các tính năng Python hiện đại (3.8+)

#### Java
- Tuân theo quy ước Spring Boot
- Sử dụng các tính năng Java 21
- Tuân theo cấu trúc dự án Maven tiêu chuẩn
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

Kho lưu trữ sử dụng GitHub Pages hoặc tương tự để lưu trữ tài liệu (nếu áp dụng). Thay đổi trên nhánh chính kích hoạt:

1. Quy trình dịch (`.github/workflows/co-op-translator.yml`)
2. Dịch tự động tất cả các tệp markdown tiếng Anh
3. Địa phương hóa hình ảnh khi cần

### Không Cần Quá Trình Xây Dựng

Kho lưu trữ này chủ yếu chứa tài liệu markdown. Không cần bước biên dịch hay xây dựng cho nội dung chương trình chính.

### Triển khai Dự án Mẫu

Các dự án mẫu riêng lẻ có thể có hướng dẫn triển khai:
- Xem thư mục `03-GettingStarted/09-deployment/` cho hướng dẫn triển khai máy chủ MCP
- Ví dụ triển khai Azure Container Apps trong `11-MCPServerHandsOnLabs/`

## Hướng Dẫn Đóng Góp

### Quy Trình Pull Request

1. **Fork và Clone**: Fork kho lưu trữ và clone bản fork về máy cục bộ của bạn
2. **Tạo Nhánh**: Sử dụng tên nhánh mô tả (ví dụ: `fix/typo-module-3`, `add/python-example`)
3. **Thực hiện thay đổi**: Chỉ chỉnh sửa các tệp markdown tiếng Anh (không phải bản dịch)
4. **Kiểm thử cục bộ**: Xác minh markdown hiển thị đúng
5. **Gửi PR**: Dùng tiêu đề và mô tả PR rõ ràng
6. **CLA**: Ký Thỏa thuận Cộng tác viên Microsoft khi được yêu cầu

### Định Dạng Tiêu Đề PR

Sử dụng tiêu đề rõ ràng, mô tả:
- `[Module XX] Mô tả ngắn` cho các thay đổi cụ thể mô-đun
- `[Samples] Mô tả` cho các thay đổi mã mẫu
- `[Docs] Mô tả` cho các cập nhật tài liệu chung

### Những Gì Nên Đóng Góp

- Sửa lỗi trong tài liệu hoặc ví dụ mã
- Ví dụ mã mới bằng các ngôn ngữ bổ sung
- Làm rõ và cải tiến nội dung hiện có
- Nghiên cứu trường hợp hoặc ví dụ thực tế mới
- Báo cáo lỗi về nội dung không rõ ràng hoặc không chính xác

### Những Gì Không Nên Làm

- Không chỉnh sửa trực tiếp các tệp trong thư mục `translations/`
- Không chỉnh sửa thư mục `translated_images/`
- Không thêm các tệp nhị phân lớn mà chưa thảo luận
- Không thay đổi các tệp quy trình dịch mà không phối hợp

## Ghi Chú Bổ Sung

### Bảo trì Kho Lưu trữ

- **Nhật ký thay đổi**: Tất cả thay đổi quan trọng được ghi lại trong `changelog.md`
- **Hướng dẫn học tập**: Sử dụng `study_guide.md` để tổng quan điều hướng chương trình
- **Mẫu Issue**: Sử dụng mẫu issue GitHub để báo lỗi và yêu cầu tính năng
- **Bộ Quy Tắc Ứng Xử**: Tất cả cộng tác viên phải tuân theo Bộ Quy Tắc Ứng Xử mã nguồn mở của Microsoft

### Lộ trình Học tập

Theo các mô-đun theo thứ tự tuần tự (00-11) để học hiệu quả:
1. **00-02**: Cơ bản (Giới thiệu, Khái niệm cốt lõi, An ninh)
2. **03**: Bắt đầu với triển khai thực hành
3. **04-05**: Triển khai thực tế và chủ đề nâng cao
4. **06-10**: Cộng đồng, thực hành tốt nhất, và ứng dụng thực tế
5. **11**: Phòng thí nghiệm tích hợp cơ sở dữ liệu toàn diện (13 phòng thí nghiệm tuần tự)

### Tài Nguyên Hỗ Trợ

- **Tài liệu**: https://modelcontextprotocol.io/
- **Thông số kỹ thuật**: https://spec.modelcontextprotocol.io/
- **Cộng đồng**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: máy chủ Discord Microsoft Foundry
- **Khóa học liên quan**: Xem README.md cho các lộ trình học Microsoft khác

### Hướng Dẫn Khắc Phục Thường Gặp

**Q: PR của tôi bị lỗi kiểm tra dịch**
A: Đảm bảo bạn chỉ chỉnh sửa các tệp markdown tiếng Anh trong thư mục mô-đun gốc, không phải các phiên bản đã dịch.

**Q: Làm sao để thêm ngôn ngữ mới?**
A: Hỗ trợ ngôn ngữ được quản lý qua quy trình co-op-translator. Mở issue để thảo luận thêm ngôn ngữ mới.

**Q: Ví dụ mã không hoạt động**

A: Đảm bảo bạn đã làm theo hướng dẫn cài đặt trong README của mẫu cụ thể. Kiểm tra xem bạn đã cài đặt đúng phiên bản các phụ thuộc.

**Q: Hình ảnh không hiển thị**
A: Xác minh rằng đường dẫn hình ảnh là tương đối và sử dụng dấu gạch chéo xuôi. Hình ảnh nên nằm trong thư mục `images/` hoặc `translated_images/` cho các phiên bản đã được dịch.

### Cân nhắc về Hiệu suất

- Quy trình dịch có thể mất vài phút để hoàn thành
- Những hình ảnh lớn nên được tối ưu trước khi cam kết
- Giữ các tập tin markdown riêng biệt có mức độ tập trung và kích thước hợp lý
- Sử dụng liên kết tương đối để dễ di chuyển hơn

### Quản trị Dự án

Dự án này tuân theo thực hành mã nguồn mở của Microsoft:
- Giấy phép MIT cho mã và tài liệu
- Bộ Quy tắc Ứng xử Mã Nguồn Mở của Microsoft
- Yêu cầu CLA cho các đóng góp
- Các vấn đề bảo mật: Tuân theo hướng dẫn trong SECURITY.md
- Hỗ trợ: Xem SUPPORT.md để biết tài nguyên trợ giúp

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->