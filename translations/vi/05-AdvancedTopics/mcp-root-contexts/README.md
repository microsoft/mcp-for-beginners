# Gốc MCP (Tính năng kế thừa)

> [!WARNING]
> Gốc đã bị ngưng dùng kể từ MCP `2026-07-28`. Chúng vẫn còn trong phiên bản này để
> tương thích và có thể bị loại bỏ trong lần chỉnh sửa đặc tả đầu tiên
> phát hành vào hoặc sau ngày 28 tháng 7 năm 2027. Các triển khai mới nên truyền
> thư mục hoặc tập tin thông qua tham số công cụ, URI tài nguyên, hoặc cấu hình máy chủ.


## Tổng quan

Gốc cho phép một khách hàng MCP thông báo cho máy chủ những vị trí trên hệ thống tập tin có liên quan
đến yêu cầu hiện tại. Một gốc chứa một URI `file://` bắt buộc và một tên hiển thị có thể có.


các phiên giao thức, hoặc một cơ chế kiểm soát truy cập. Giao thức không
bắt buộc máy chủ phải giới hạn trong các gốc đã liệt kê.


## Mục tiêu học tập

Đến cuối bài học này, bạn sẽ có thể:

- Giải thích Gốc MCP đại diện cho điều gì và điều gì không đại diện.
- Nhận biết luồng đa lượt `roots/list` hiện tại.
- Áp dụng các kiểm soát bảo mật độc lập với Gốc.
- Di chuyển các triển khai mới sang các giải pháp thay thế được hỗ trợ.

## Dữ liệu Gốc

Một khách hàng trả về mỗi gốc dưới dạng một URI `file://` với tên hiển thị tùy chọn:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Khách hàng nên chỉ cung cấp các vị trí được người dùng chấp thuận. Máy chủ nên xem
kết quả như hướng dẫn về các tập tin có liên quan, không phải là bằng chứng ủy quyền.

## Luồng MCP 2026-07-28

Một khách hàng hỗ trợ Gốc tuyên bố khả năng này trong mọi yêu cầu:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Trong khi xử lý yêu cầu khách hàng, máy chủ có thể trả về một
`InputRequiredResult` chứa một yêu cầu nhập `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Khách hàng tập hợp các gốc được phê duyệt và thử lại yêu cầu gốc với
các `inputResponses` phù hợp và `requestState` không đổi. Mô hình đa lượt này
giữ cho giao thức không trạng thái; không có bắt tay `initialize` hoặc
phiên cấp giao thức.

## Hành vi kế thừa 2025-11-25

Trong MCP `2025-11-25`, khách hàng quảng bá Gốc trong quá trình khởi tạo. Một máy chủ
có thể phát hành yêu cầu trực tiếp `roots/list`, và khách hàng có thể gửi
`notifications/roots/list_changed` khi gốc của nó thay đổi.

Vòng đời đó là hành vi kế thừa. Không kết hợp ví dụ khởi tạo hoặc
thông báo đó với một triển khai `2026-07-28`.

## Giải pháp thay thế được khuyên dùng

### Tham số công cụ

Xác định rõ thư mục hoặc tập tin yêu cầu trong sơ đồ công cụ:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URI tài nguyên

Sử dụng Tài nguyên MCP khi máy chủ có thể cung cấp các tập tin liên quan thông qua các
URI ổn định. Điều này làm cho việc khám phá và truy xuất rõ ràng hơn.

### Cấu hình máy chủ

Trong triển khai cố định, cấu hình các thư mục được phép khi máy chủ khởi động.
Điều này thường rõ ràng hơn là khám phá chúng trong khi gọi công cụ.

## Yêu cầu bảo mật

Dù chọn giải pháp thay thế nào:

- Lấy sự đồng ý của người dùng trước khi cung cấp vị trí hệ thống tập tin.
- Chuẩn hóa và xác thực đường dẫn để tránh truy cập vượt rào.
- Thực thi ủy quyền và phân vùng độc lập với giá trị gốc.
- Kiểm tra lại quyền khi truy cập tập tin, không chỉ khi liệt kê.
- Tránh trả về các đường dẫn nhạy cảm trong nhật ký hoặc thông báo lỗi.

## Những điểm chính

- Gốc mô tả các vị trí hệ thống tập tin có liên quan; chúng không lưu trạng thái hội thoại.

- Gốc là hướng dẫn, không phải ranh giới kiểm soát truy cập.
- MCP `2026-07-28` truyền khả năng theo từng yêu cầu và sử dụng
  `InputRequiredResult` cho `roots/list`.
- Các triển khai mới nên sử dụng tham số công cụ, URI tài nguyên, hoặc cấu hình máy chủ thay thế.


## Tài nguyên bổ sung

- [Gốc trong MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Đăng ký các tính năng ngưng dùng](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Những thay đổi trong MCP: Đặc tả 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->