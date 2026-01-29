# 📘 Giải pháp Bài tập: Mở rộng Máy chủ MCP Máy tính của bạn với Công cụ Căn bậc hai

## Tổng quan
Trong bài tập này, bạn đã nâng cấp máy chủ MCP máy tính của mình bằng cách thêm một công cụ mới để tính căn bậc hai của một số. Sự bổ sung này giúp cho AI agent của bạn có thể xử lý các truy vấn toán học phức tạp hơn, như "Căn bậc hai của 16 là bao nhiêu?" hoặc "Tính √49," sử dụng các câu lệnh ngôn ngữ tự nhiên.

## 🛠️ Triển khai Công cụ Căn bậc hai
Để thêm chức năng này, bạn đã định nghĩa một hàm công cụ mới trong file server.py. Dưới đây là phần cài đặt:

```python
"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools
that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from mcp.server.fastmcp import FastMCP
import math

server = FastMCP("calculator")

@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@server.tool()
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@server.tool()
def sqrt(a: float) -> float:
    """
    Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(a)
```

## 🔍 Cách hoạt động

- **Nhập module `math`**: Để thực hiện các phép toán vượt ra ngoài các phép tính cơ bản, Python cung cấp module tích hợp `math`. Module này bao gồm nhiều hàm và hằng số toán học. Bằng cách nhập `import math`, bạn có thể sử dụng các hàm như `math.sqrt()`, dùng để tính căn bậc hai của một số.
- **Định nghĩa hàm**: Bộ trang trí `@server.tool()` đăng ký hàm `sqrt` như một công cụ mà AI agent có thể truy cập.
- **Tham số đầu vào**: Hàm nhận một đối số duy nhất `a` kiểu `float`.
- **Xử lý lỗi**: Nếu `a` là số âm, hàm sẽ ném ra lỗi `ValueError` để ngăn việc tính căn bậc hai của số âm, điều mà hàm `math.sqrt()` không hỗ trợ.
- **Giá trị trả về**: Với các giá trị không âm, hàm trả về căn bậc hai của `a` bằng phương thức `math.sqrt()` có sẵn trong Python.

## 🔄 Khởi động lại Máy chủ
Sau khi thêm công cụ `sqrt` mới, bạn cần khởi động lại máy chủ MCP để đảm bảo agent nhận diện và sử dụng được chức năng vừa thêm.

## 💬 Ví dụ Câu lệnh để Kiểm tra Công cụ Mới
Dưới đây là một số câu lệnh ngôn ngữ tự nhiên bạn có thể dùng để kiểm tra chức năng căn bậc hai:

- "Căn bậc hai của 25 là bao nhiêu?"
- "Tính căn bậc hai của 81."
- "Tìm căn bậc hai của 0."
- "Căn bậc hai của 2.25 là bao nhiêu?"

Những câu lệnh này sẽ kích hoạt agent gọi công cụ `sqrt` và trả về kết quả chính xác.

## ✅ Tóm tắt
Qua bài tập này, bạn đã:

- Mở rộng máy chủ MCP máy tính của mình với công cụ `sqrt` mới.
- Giúp AI agent có thể thực hiện các phép tính căn bậc hai thông qua các câu lệnh ngôn ngữ tự nhiên.
- Thực hành thêm công cụ mới và khởi động lại máy chủ để tích hợp các chức năng bổ sung.

Hãy tiếp tục thử nghiệm bằng cách thêm các công cụ toán học khác, như phép lũy thừa hoặc hàm logarit, để nâng cao khả năng của agent nhé!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.