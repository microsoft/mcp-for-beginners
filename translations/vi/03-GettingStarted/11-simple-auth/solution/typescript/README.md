# Chạy mẫu

## Cài đặt các phụ thuộc

```sh
npm install
```

## Xây dựng

```sh
npm run build
```

## Tạo token

```sh
npm run generate
```

Điều này sẽ tạo một token trong tệp *.env*. Client sẽ đọc từ tệp này.

## Chạy mã

Khởi động server với:

```sh
npm start
```

Chạy client trong một terminal riêng với:

```sh
npm run client
```

Trong terminal của server, bạn sẽ thấy đầu ra tương tự như:

```text
User exists
User has required scopes
Middleware executed
```

và từ terminal của client, bạn sẽ thấy đầu ra tương tự như:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Thay đổi các thiết lập

Hãy đảm bảo rằng chúng ta hiểu các phạm vi. Tìm tệp *server.ts* và đoạn mã này:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Điều này nói rằng token được truyền vào cần có "User.Read", hãy thay đổi thành "User.Write". Bây giờ chạy `npm run build` và khởi động lại server bằng `npm start`. Bạn sẽ thấy xác thực thất bại vì chúng ta không có phạm vi này (chúng ta có User.Read và Admin.Write):

Client bây giờ sẽ hiển thị

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

và bạn có thể thấy trong terminal của server rằng nó hiển thị:

```text
User exists
```

và không tiến xa hơn điểm này.

Hoặc thêm phạm vi "User.Write" và chạy `npm run generate` rồi chạy lại client, HOẶC thay đổi lại mã của server.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.