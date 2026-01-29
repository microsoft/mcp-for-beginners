# Chạy mẫu

## Tạo môi trường

```sh
python -m venv venv
source ./venv/bin/activate
```

## Cài đặt các phụ thuộc

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Tạo token

Bạn sẽ cần tạo một token để client sử dụng khi giao tiếp với server.

Gọi:

```sh
python util.py
```

## Chạy mã

Chạy mã với:

```sh
python server.py
```

Trong một terminal khác, nhập:

```sh
python client.py
```

Trong terminal của server, bạn sẽ thấy một cái gì đó giống như:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Trong cửa sổ client, bạn sẽ thấy văn bản tương tự như:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Điều này có nghĩa là mọi thứ đang hoạt động.

### Thay đổi thông tin để kiểm tra lỗi

Tìm đoạn mã này trong *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Thay đổi nó để hiển thị "User.Write". Token hiện tại của bạn không có mức quyền này, vì vậy nếu bạn khởi động lại server và thử chạy client một lần nữa, bạn sẽ thấy một lỗi tương tự như sau trong terminal của server:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Bạn có thể thay đổi lại mã server của mình hoặc tạo một token mới chứa phạm vi bổ sung này, tùy thuộc vào bạn.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.