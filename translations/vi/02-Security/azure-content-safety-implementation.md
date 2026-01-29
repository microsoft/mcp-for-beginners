# Triển khai Azure Content Safety với MCP

Để tăng cường bảo mật MCP chống lại các cuộc tấn công chèn lệnh, đầu độc công cụ và các lỗ hổng đặc thù của AI, việc tích hợp Azure Content Safety được khuyến nghị mạnh mẽ.

## Tích hợp với MCP Server

Để tích hợp Azure Content Safety vào server MCP của bạn, thêm bộ lọc content safety làm middleware trong quy trình xử lý yêu cầu:

1. Khởi tạo bộ lọc khi server khởi động
2. Xác thực tất cả các yêu cầu công cụ đến trước khi xử lý
3. Kiểm tra tất cả phản hồi gửi ra trước khi trả về cho client
4. Ghi lại và cảnh báo khi phát hiện vi phạm an toàn
5. Thực hiện xử lý lỗi phù hợp khi kiểm tra content safety không thành công

Điều này cung cấp một lớp phòng thủ vững chắc chống lại:
- Các cuộc tấn công chèn lệnh (prompt injection)
- Các nỗ lực đầu độc công cụ
- Rò rỉ dữ liệu qua các đầu vào độc hại
- Việc tạo ra nội dung có hại

## Các thực hành tốt nhất khi tích hợp Azure Content Safety

1. **Danh sách chặn tùy chỉnh**: Tạo các danh sách chặn riêng biệt dành cho các mẫu chèn lệnh MCP
2. **Điều chỉnh mức độ nghiêm trọng**: Tùy chỉnh ngưỡng mức độ nghiêm trọng dựa trên trường hợp sử dụng và mức độ chấp nhận rủi ro của bạn
3. **Phủ sóng toàn diện**: Áp dụng kiểm tra content safety cho tất cả đầu vào và đầu ra
4. **Tối ưu hiệu năng**: Cân nhắc triển khai bộ nhớ đệm cho các lần kiểm tra content safety lặp lại
5. **Cơ chế dự phòng**: Xác định rõ hành vi dự phòng khi dịch vụ content safety không khả dụng
6. **Phản hồi người dùng**: Cung cấp phản hồi rõ ràng cho người dùng khi nội dung bị chặn do lý do an toàn
7. **Cải tiến liên tục**: Thường xuyên cập nhật danh sách chặn và các mẫu dựa trên các mối đe dọa mới xuất hiện

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.