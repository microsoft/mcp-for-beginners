# AGENTS.md

## Tổng quan dự án

**MCP for Beginners** là một chương trình giáo dục mã nguồn mở dành cho việc học giao thức Model Context Protocol (MCP) - một khung chuẩn hóa cho các tương tác giữa các mô hình AI và ứng dụng khách. Kho lưu trữ này cung cấp tài liệu học tập toàn diện với các ví dụ mã thực hành trên nhiều ngôn ngữ lập trình.

### Công nghệ chính

- **Ngôn ngữ lập trình**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Cơ sở dữ liệu**: PostgreSQL với tiện ích mở rộng pgvector
- **Nền tảng đám mây**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Công cụ xây dựng**: npm, Maven, pip, Cargo
- **Tài liệu**: Markdown với hệ thống dịch tự động đa ngôn ngữ (hơn 48 ngôn ngữ)

### Kiến trúc

- **11 Module cốt lõi (00-11)**: Lộ trình học tuần tự từ cơ bản đến nâng cao
- **Phòng thực hành**: Bài tập thực hành với mã giải pháp hoàn chỉnh bằng nhiều ngôn ngữ
- **Dự án mẫu**: Các triển khai máy chủ và ứng dụng khách MCP hoạt động
- **Hệ thống dịch thuật**: Quy trình GitHub Actions tự động hỗ trợ đa ngôn ngữ
- **Tài nguyên hình ảnh**: Thư mục hình ảnh tập trung với các phiên bản đã dịch

## Lệnh thiết lập

Đây là kho lưu trữ tập trung vào tài liệu. Hầu hết các thiết lập diễn ra trong các dự án mẫu và phòng thực hành riêng lẻ.

### Thiết lập kho lưu trữ

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Làm việc với các dự án mẫu

Các dự án mẫu nằm tại:
- `03-GettingStarted/samples/` - Các ví dụ theo ngôn ngữ
- `03-GettingStarted/01-first-server/solution/` - Các triển khai máy chủ đầu tiên
- `03-GettingStarted/02-client/solution/` - Các triển khai ứng dụng khách
- `11-MCPServerHandsOnLabs/` - Phòng thực hành tích hợp cơ sở dữ liệu toàn diện

Mỗi dự án mẫu đều có hướng dẫn thiết lập riêng:

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
# or
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

### Cấu trúc tài liệu

- **Modules 00-11**: Nội dung chương trình học cốt lõi theo thứ tự tuần tự
- **translations/**: Các phiên bản theo ngôn ngữ (tự động tạo, không chỉnh sửa trực tiếp)
- **translated_images/**: Các phiên bản hình ảnh đã được bản địa hóa (tự động tạo)
- **images/**: Hình ảnh và sơ đồ nguồn

### Thay đổi tài liệu

1. Chỉ chỉnh sửa các tệp markdown tiếng Anh trong các thư mục module gốc (00-11)
2. Cập nhật hình ảnh trong thư mục `images/` nếu cần
3. GitHub Action co-op-translator sẽ tự động tạo các bản dịch
4. Các bản dịch được tạo lại khi đẩy lên nhánh chính

### Làm việc với bản dịch

- **Dịch tự động**: Quy trình GitHub Actions xử lý tất cả các bản dịch
- **KHÔNG chỉnh sửa thủ công** các tệp trong thư mục `translations/`
- Metadata dịch thuật được nhúng trong mỗi tệp đã dịch
- Ngôn ngữ hỗ trợ: Hơn 48 ngôn ngữ bao gồm tiếng Ả Rập, Trung Quốc, Pháp, Đức, Hindi, Nhật Bản, Hàn Quốc, Bồ Đào Nha, Nga, Tây Ban Nha và nhiều ngôn ngữ khác

## Hướng dẫn kiểm tra

### Xác thực tài liệu

Vì đây chủ yếu là kho lưu trữ tài liệu, việc kiểm tra tập trung vào:

1. **Xác thực liên kết**: Đảm bảo tất cả các liên kết nội bộ hoạt động
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Xác thực mẫu mã**: Kiểm tra rằng các ví dụ mã có thể biên dịch/chạy
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Kiểm tra Markdown**: Kiểm tra tính nhất quán định dạng
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Kiểm tra dự án mẫu

Mỗi mẫu theo ngôn ngữ đều có cách kiểm tra riêng:

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

## Nguyên tắc phong cách mã

### Phong cách tài liệu

- Sử dụng ngôn ngữ rõ ràng, dễ hiểu cho người mới bắt đầu
- Bao gồm các ví dụ mã bằng nhiều ngôn ngữ khi có thể
- Tuân theo các thực hành tốt nhất của markdown:
  - Sử dụng tiêu đề kiểu ATX (`#` syntax)
  - Sử dụng khối mã có rào chắn với định danh ngôn ngữ
  - Bao gồm văn bản thay thế mô tả cho hình ảnh
  - Giữ độ dài dòng hợp lý (không giới hạn cứng, nhưng cần hợp lý)

### Phong cách mẫu mã

#### TypeScript/JavaScript
- Sử dụng ES modules (`import`/`export`)
- Tuân theo các quy ước chế độ nghiêm ngặt của TypeScript
- Bao gồm chú thích kiểu
- Nhắm mục tiêu ES2022

#### Python
- Tuân theo hướng dẫn phong cách PEP 8
- Sử dụng gợi ý kiểu khi phù hợp
- Bao gồm docstrings cho các hàm và lớp
- Sử dụng các tính năng hiện đại của Python (3.8+)

#### Java
- Tuân theo các quy ước của Spring Boot
- Sử dụng các tính năng của Java 21
- Tuân theo cấu trúc dự án Maven tiêu chuẩn
- Bao gồm các nhận xét Javadoc

### Tổ chức tệp

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

## Xây dựng và triển khai

### Triển khai tài liệu

Kho lưu trữ sử dụng GitHub Pages hoặc tương tự để lưu trữ tài liệu (nếu áp dụng). Các thay đổi trên nhánh chính sẽ kích hoạt:

1. Quy trình dịch thuật (`.github/workflows/co-op-translator.yml`)
2. Dịch tự động tất cả các tệp markdown tiếng Anh
3. Bản địa hóa hình ảnh khi cần

### Không yêu cầu quy trình xây dựng

Kho lưu trữ này chủ yếu chứa tài liệu markdown. Không cần bước biên dịch hoặc xây dựng cho nội dung chương trình học cốt lõi.

### Triển khai dự án mẫu

Các dự án mẫu riêng lẻ có thể có hướng dẫn triển khai:
- Xem `03-GettingStarted/09-deployment/` để biết hướng dẫn triển khai máy chủ MCP
- Ví dụ triển khai Azure Container Apps trong `11-MCPServerHandsOnLabs/`

## Hướng dẫn đóng góp

### Quy trình Pull Request

1. **Fork và Clone**: Fork kho lưu trữ và clone fork của bạn về máy cục bộ
2. **Tạo nhánh**: Sử dụng tên nhánh mô tả (ví dụ: `fix/typo-module-3`, `add/python-example`)
3. **Thực hiện thay đổi**: Chỉ chỉnh sửa các tệp markdown tiếng Anh (không phải bản dịch)
4. **Kiểm tra cục bộ**: Xác minh rằng markdown hiển thị đúng
5. **Gửi PR**: Sử dụng tiêu đề và mô tả PR rõ ràng
6. **CLA**: Ký Thỏa thuận Cấp phép Người đóng góp của Microsoft khi được yêu cầu

### Định dạng tiêu đề PR

Sử dụng tiêu đề rõ ràng, mô tả:
- `[Module XX] Mô tả ngắn gọn` cho các thay đổi cụ thể của module
- `[Samples] Mô tả` cho các thay đổi mã mẫu
- `[Docs] Mô tả` cho các cập nhật tài liệu chung

### Những gì cần đóng góp

- Sửa lỗi trong tài liệu hoặc mẫu mã
- Ví dụ mã mới bằng các ngôn ngữ bổ sung
- Làm rõ và cải thiện nội dung hiện có
- Nghiên cứu trường hợp mới hoặc ví dụ thực tế
- Báo cáo vấn đề về nội dung không rõ ràng hoặc không chính xác

### Những gì KHÔNG nên làm

- Không chỉnh sửa trực tiếp các tệp trong thư mục `translations/`
- Không chỉnh sửa thư mục `translated_images/`
- Không thêm các tệp nhị phân lớn mà không thảo luận trước
- Không thay đổi các tệp quy trình dịch thuật mà không có sự phối hợp

## Ghi chú bổ sung

### Bảo trì kho lưu trữ

- **Changelog**: Tất cả các thay đổi quan trọng được ghi lại trong `changelog.md`
- **Hướng dẫn học tập**: Sử dụng `study_guide.md` để có cái nhìn tổng quan về lộ trình học tập
- **Mẫu vấn đề**: Sử dụng mẫu vấn đề GitHub để báo cáo lỗi và yêu cầu tính năng
- **Quy tắc ứng xử**: Tất cả người đóng góp phải tuân theo Quy tắc Ứng xử Mã nguồn Mở của Microsoft

### Lộ trình học tập

Tuân theo các module theo thứ tự tuần tự (00-11) để học tập hiệu quả:
1. **00-02**: Kiến thức cơ bản (Giới thiệu, Khái niệm cốt lõi, Bảo mật)
2. **03**: Bắt đầu với triển khai thực hành
3. **04-05**: Triển khai thực tế và các chủ đề nâng cao
4. **06-10**: Cộng đồng, thực hành tốt nhất, và ứng dụng thực tế
5. **11**: Phòng thực hành tích hợp cơ sở dữ liệu toàn diện (13 phòng thực hành tuần tự)

### Tài nguyên hỗ trợ

- **Tài liệu**: https://modelcontextprotocol.io/
- **Đặc tả**: https://spec.modelcontextprotocol.io/
- **Cộng đồng**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Máy chủ Discord Microsoft Azure AI Foundry
- **Khóa học liên quan**: Xem README.md để biết các lộ trình học tập khác của Microsoft

### Các vấn đề thường gặp

**Q: PR của tôi không vượt qua kiểm tra dịch thuật**
A: Đảm bảo bạn chỉ chỉnh sửa các tệp markdown tiếng Anh trong các thư mục module gốc, không phải các phiên bản đã dịch.

**Q: Làm thế nào để thêm ngôn ngữ mới?**
A: Hỗ trợ ngôn ngữ được quản lý thông qua quy trình co-op-translator. Mở một vấn đề để thảo luận về việc thêm ngôn ngữ mới.

**Q: Các mẫu mã không hoạt động**
A: Đảm bảo bạn đã làm theo hướng dẫn thiết lập trong README của mẫu cụ thể. Kiểm tra rằng bạn đã cài đặt đúng phiên bản của các phụ thuộc.

**Q: Hình ảnh không hiển thị**
A: Xác minh rằng các đường dẫn hình ảnh là tương đối và sử dụng dấu gạch chéo. Hình ảnh nên nằm trong thư mục `images/` hoặc `translated_images/` cho các phiên bản đã bản địa hóa.

### Cân nhắc hiệu suất

- Quy trình dịch thuật có thể mất vài phút để hoàn thành
- Hình ảnh lớn nên được tối ưu hóa trước khi commit
- Giữ các tệp markdown riêng lẻ tập trung và có kích thước hợp lý
- Sử dụng liên kết tương đối để tăng tính di động

### Quản trị dự án

Dự án này tuân theo các thực hành mã nguồn mở của Microsoft:
- Giấy phép MIT cho mã và tài liệu
- Quy tắc Ứng xử Mã nguồn Mở của Microsoft
- Yêu cầu CLA cho các đóng góp
- Vấn đề bảo mật: Tuân theo hướng dẫn trong SECURITY.md
- Hỗ trợ: Xem SUPPORT.md để biết các tài nguyên hỗ trợ

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.