# Chạy mẫu này

Đây là giải pháp Rust cho mẫu client LLM. Bạn cần cài đặt toolchain Rust; xem [hướng dẫn cài đặt chính thức](https://www.rust-lang.org/tools/install).

Client gọi một mô hình Microsoft Foundry đã triển khai thông qua endpoint Azure OpenAI
v1.

> [!NOTE]
> Giá trị được truyền dưới dạng `model` là tên triển khai Foundry của bạn, không nhất thiết
> là tên mô hình cơ bản.

## -0- Cấu hình Microsoft Foundry

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
$env:AZURE_OPENAI_API_KEY = "<api-key>"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
```

## -1- Xây dựng mẫu

```bash
cargo build
```

## -2- Chạy mẫu

```bash
cargo run
```

Client khởi động server MCP máy tính, lấy danh sách công cụ của nó, và sử dụng
mô hình đã triển khai để gọi công cụ `add`. Bạn sẽ thấy kết quả hiển thị cho biết
thao tác gọi công cụ (ví dụ, "Calling tool: add") và kết quả của thao tác đó.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->