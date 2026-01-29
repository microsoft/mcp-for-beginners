# 🐙 Module 4: Phát Triển MCP Thực Tiễn - Máy Chủ GitHub Clone Tùy Chỉnh

![Duration](https://img.shields.io/badge/Duration-30_minutes-blue?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-Custom%20Server-purple?style=flat-square&logo=github)
![VS Code](https://img.shields.io/badge/VS%20Code-Integration-blue?style=flat-square&logo=visualstudiocode)
![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Agent%20Mode-green?style=flat-square&logo=github)

> **⚡ Bắt Đầu Nhanh:** Xây dựng một máy chủ MCP sẵn sàng cho môi trường sản xuất, tự động hóa việc clone repository GitHub và tích hợp với VS Code chỉ trong 30 phút!

## 🎯 Mục Tiêu Học Tập

Sau khi hoàn thành bài lab này, bạn sẽ có khả năng:

- ✅ Tạo máy chủ MCP tùy chỉnh cho quy trình phát triển thực tế
- ✅ Triển khai chức năng clone repository GitHub qua MCP
- ✅ Tích hợp máy chủ MCP tùy chỉnh với VS Code và Agent Builder
- ✅ Sử dụng GitHub Copilot Agent Mode với các công cụ MCP tùy chỉnh
- ✅ Kiểm thử và triển khai máy chủ MCP tùy chỉnh trong môi trường sản xuất

## 📋 Yêu Cầu Tiên Quyết

- Hoàn thành Labs 1-3 (cơ bản và phát triển nâng cao MCP)
- Đăng ký GitHub Copilot ([đăng ký miễn phí có sẵn](https://github.com/github-copilot/signup))
- VS Code đã cài đặt AI Toolkit và tiện ích mở rộng GitHub Copilot
- Git CLI đã được cài đặt và cấu hình

## 🏗️ Tổng Quan Dự Án

### **Thách Thức Phát Triển Thực Tế**
Là nhà phát triển, chúng ta thường xuyên sử dụng GitHub để clone repository và mở chúng trong VS Code hoặc VS Code Insiders. Quy trình thủ công này bao gồm:
1. Mở terminal/command prompt
2. Điều hướng đến thư mục mong muốn
3. Chạy lệnh `git clone`
4. Mở VS Code trong thư mục vừa clone

**Giải pháp MCP của chúng ta sẽ hợp nhất tất cả thành một lệnh thông minh duy nhất!**

### **Bạn Sẽ Xây Dựng Gì**
Một **GitHub Clone MCP Server** (`git_mcp_server`) cung cấp:

| Tính Năng | Mô Tả | Lợi Ích |
|---------|-------------|---------|
| 🔄 **Clone Repository Thông Minh** | Clone repo GitHub kèm kiểm tra hợp lệ | Tự động kiểm tra lỗi |
| 📁 **Quản Lý Thư Mục Thông Minh** | Kiểm tra và tạo thư mục an toàn | Ngăn chặn ghi đè dữ liệu |
| 🚀 **Tích Hợp VS Code Đa Nền Tảng** | Mở dự án trong VS Code/Insiders | Chuyển đổi quy trình làm việc mượt mà |
| 🛡️ **Xử Lý Lỗi Mạnh Mẽ** | Xử lý lỗi mạng, quyền truy cập, và đường dẫn | Đảm bảo độ tin cậy trong môi trường sản xuất |

---

## 📖 Hướng Dẫn Triển Khai Từng Bước

### Bước 1: Tạo GitHub Agent trong Agent Builder

1. **Khởi chạy Agent Builder** qua tiện ích AI Toolkit
2. **Tạo agent mới** với cấu hình sau:
   ```
   Agent Name: GitHubAgent
   ```

3. **Khởi tạo máy chủ MCP tùy chỉnh:**
   - Vào **Tools** → **Add Tool** → **MCP Server**
   - Chọn **"Create A new MCP Server"**
   - Chọn **mẫu Python** để linh hoạt tối đa
   - **Tên máy chủ:** `git_mcp_server`

### Bước 2: Cấu Hình GitHub Copilot Agent Mode

1. **Mở GitHub Copilot** trong VS Code (Ctrl/Cmd + Shift + P → "GitHub Copilot: Open")
2. **Chọn Agent Model** trong giao diện Copilot
3. **Chọn mô hình Claude 3.7** để nâng cao khả năng suy luận
4. **Bật tích hợp MCP** để truy cập công cụ

> **💡 Mẹo chuyên nghiệp:** Claude 3.7 cung cấp khả năng hiểu sâu về quy trình phát triển và mẫu xử lý lỗi.

### Bước 3: Triển Khai Chức Năng Chính của MCP Server

**Sử dụng prompt chi tiết sau với GitHub Copilot Agent Mode:**

```
Create two MCP tools with the following comprehensive requirements:

🔧 TOOL A: clone_repository
Requirements:
- Clone any GitHub repository to a specified local folder
- Return the absolute path of the successfully cloned project
- Implement comprehensive validation:
  ✓ Check if target directory already exists (return error if exists)
  ✓ Validate GitHub URL format (https://github.com/user/repo)
  ✓ Verify git command availability (prompt installation if missing)
  ✓ Handle network connectivity issues
  ✓ Provide clear error messages for all failure scenarios

🚀 TOOL B: open_in_vscode
Requirements:
- Open specified folder in VS Code or VS Code Insiders
- Cross-platform compatibility (Windows/Linux/macOS)
- Use direct application launch (not terminal commands)
- Auto-detect available VS Code installations
- Handle cases where VS Code is not installed
- Provide user-friendly error messages

Additional Requirements:
- Follow MCP 1.9.3 best practices
- Include proper type hints and documentation
- Implement logging for debugging purposes
- Add input validation for all parameters
- Include comprehensive error handling
```

### Bước 4: Kiểm Thử Máy Chủ MCP

#### 4a. Kiểm thử trong Agent Builder

1. **Khởi chạy cấu hình debug** cho Agent Builder
2. **Cấu hình agent với prompt hệ thống sau:**

```
SYSTEM_PROMPT:
You are my intelligent coding repository assistant. You help developers efficiently clone GitHub repositories and set up their development environment. Always provide clear feedback about operations and handle errors gracefully.
```

3. **Kiểm thử với các kịch bản người dùng thực tế:**

```
USER_PROMPT EXAMPLES:

Scenario : Basic Clone and Open
"Clone {Your GitHub Repo link such as https://github.com/kinfey/GHCAgentWorkshop
 } and save to {The global path you specify}, then open it with VS Code Insiders"
```

![Agent Builder Testing](../../../../translated_images/vi/DebugAgent.81d152370c503241b3b39a251b8966f7f739286df19dd57f9147f6402214a012.png)

**Kết quả mong đợi:**
- ✅ Clone thành công với xác nhận đường dẫn
- ✅ Tự động mở VS Code
- ✅ Thông báo lỗi rõ ràng cho các trường hợp không hợp lệ
- ✅ Xử lý đúng các trường hợp đặc biệt

#### 4b. Kiểm thử trong MCP Inspector

![MCP Inspector Testing](../../../../translated_images/vi/DebugInspector.eb5c95f94c69a8ba36944941b9a3588309a3a2fae101ace470ee09bde41d1667.png)

---

**🎉 Chúc mừng!** Bạn đã tạo thành công một máy chủ MCP thực tiễn, sẵn sàng cho môi trường sản xuất, giải quyết các thách thức trong quy trình phát triển thực tế. Máy chủ clone GitHub tùy chỉnh của bạn thể hiện sức mạnh của MCP trong việc tự động hóa và nâng cao hiệu suất làm việc của nhà phát triển.

### 🏆 Thành Tựu Đạt Được:
- ✅ **Nhà Phát Triển MCP** - Tạo máy chủ MCP tùy chỉnh
- ✅ **Chuyên Gia Tự Động Hóa Quy Trình** - Tinh giản quy trình phát triển  
- ✅ **Chuyên Gia Tích Hợp** - Kết nối nhiều công cụ phát triển
- ✅ **Sẵn Sàng Sản Xuất** - Xây dựng giải pháp có thể triển khai

---

## 🎓 Hoàn Thành Workshop: Hành Trình Với Model Context Protocol

**Tham Gia Viên Workshop thân mến,**

Chúc mừng bạn đã hoàn thành tất cả bốn module của workshop Model Context Protocol! Bạn đã đi một chặng đường dài từ việc hiểu các khái niệm cơ bản của AI Toolkit đến xây dựng các máy chủ MCP sẵn sàng cho môi trường sản xuất, giải quyết các thách thức phát triển thực tế.

### 🚀 Tóm Tắt Lộ Trình Học Tập:

**[Module 1](../lab1/README.md)**: Bạn bắt đầu với việc khám phá các kiến thức cơ bản về AI Toolkit, thử nghiệm mô hình và tạo agent AI đầu tiên.

**[Module 2](../lab2/README.md)**: Bạn học về kiến trúc MCP, tích hợp Playwright MCP và xây dựng agent tự động trình duyệt đầu tiên.

**[Module 3](../lab3/README.md)**: Bạn nâng cao kỹ năng phát triển máy chủ MCP tùy chỉnh với Weather MCP server và làm chủ công cụ gỡ lỗi.

**[Module 4](../lab4/README.md)**: Bạn áp dụng tất cả để tạo công cụ tự động hóa quy trình làm việc với repository GitHub thực tế.

### 🌟 Những Điều Bạn Đã Thành Thạo:

- ✅ **Hệ Sinh Thái AI Toolkit**: Mô hình, agent và các mẫu tích hợp
- ✅ **Kiến Trúc MCP**: Thiết kế client-server, giao thức truyền tải và bảo mật
- ✅ **Công Cụ Phát Triển**: Từ Playground đến Inspector và triển khai sản xuất
- ✅ **Phát Triển Tùy Chỉnh**: Xây dựng, kiểm thử và triển khai máy chủ MCP của riêng bạn
- ✅ **Ứng Dụng Thực Tiễn**: Giải quyết các thách thức quy trình làm việc thực tế bằng AI

### 🔮 Bước Tiếp Theo Của Bạn:

1. **Xây Dựng Máy Chủ MCP Riêng**: Áp dụng kỹ năng để tự động hóa quy trình làm việc độc đáo của bạn
2. **Tham Gia Cộng Đồng MCP**: Chia sẻ sản phẩm và học hỏi từ người khác
3. **Khám Phá Tích Hợp Nâng Cao**: Kết nối máy chủ MCP với hệ thống doanh nghiệp
4. **Đóng Góp Mã Nguồn Mở**: Góp phần cải thiện công cụ và tài liệu MCP

Hãy nhớ rằng, workshop này chỉ là khởi đầu. Hệ sinh thái Model Context Protocol đang phát triển nhanh chóng, và bạn đã sẵn sàng để dẫn đầu trong việc phát triển công cụ AI hỗ trợ.

**Cảm ơn bạn đã tham gia và nỗ lực học tập!**

Chúng tôi hy vọng workshop này đã truyền cảm hứng để bạn thay đổi cách xây dựng và tương tác với công cụ AI trong hành trình phát triển của mình.

**Chúc bạn lập trình vui vẻ!**

---

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.