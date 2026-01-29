# Sử dụng một máy chủ từ tiện ích mở rộng AI Toolkit cho Visual Studio Code

Khi bạn xây dựng một tác nhân AI, không chỉ là tạo ra các phản hồi thông minh; mà còn là cung cấp cho tác nhân khả năng thực hiện hành động. Đó là lúc giao thức Model Context Protocol (MCP) xuất hiện. MCP giúp các tác nhân dễ dàng truy cập các công cụ và dịch vụ bên ngoài một cách nhất quán. Hãy tưởng tượng như bạn đang kết nối tác nhân của mình với một hộp công cụ mà nó có thể *thực sự* sử dụng.

Ví dụ, bạn kết nối một tác nhân với máy chủ MCP của máy tính. Đột nhiên, tác nhân của bạn có thể thực hiện các phép toán chỉ bằng cách nhận một yêu cầu như “47 nhân 89 là bao nhiêu?”—không cần phải mã hóa logic hay xây dựng API tùy chỉnh.

## Tổng quan

Bài học này hướng dẫn cách kết nối một máy chủ MCP của máy tính với một tác nhân bằng tiện ích mở rộng [AI Toolkit](https://aka.ms/AIToolkit) trong Visual Studio Code, cho phép tác nhân thực hiện các phép toán như cộng, trừ, nhân, và chia thông qua ngôn ngữ tự nhiên.

AI Toolkit là một tiện ích mạnh mẽ cho Visual Studio Code, giúp đơn giản hóa việc phát triển tác nhân AI. Các kỹ sư AI có thể dễ dàng xây dựng ứng dụng AI bằng cách phát triển và kiểm thử các mô hình AI sinh—cả cục bộ và trên đám mây. Tiện ích này hỗ trợ hầu hết các mô hình sinh lớn hiện nay.

*Lưu ý*: AI Toolkit hiện hỗ trợ Python và TypeScript.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Sử dụng một máy chủ MCP thông qua AI Toolkit.
- Cấu hình một tác nhân để cho phép nó khám phá và sử dụng các công cụ được cung cấp bởi máy chủ MCP.
- Sử dụng các công cụ MCP thông qua ngôn ngữ tự nhiên.

## Phương pháp tiếp cận

Dưới đây là cách tiếp cận ở mức độ cao:

- Tạo một tác nhân và định nghĩa yêu cầu hệ thống của nó.
- Tạo một máy chủ MCP với các công cụ máy tính.
- Kết nối Agent Builder với máy chủ MCP.
- Kiểm tra việc gọi công cụ của tác nhân thông qua ngôn ngữ tự nhiên.

Tuyệt vời, giờ chúng ta đã hiểu quy trình, hãy cấu hình một tác nhân AI để tận dụng các công cụ bên ngoài thông qua MCP, nâng cao khả năng của nó!

## Yêu cầu trước

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit cho Visual Studio Code](https://aka.ms/AIToolkit)

## Bài tập: Sử dụng một máy chủ

> [!WARNING]
> Lưu ý cho người dùng macOS. Chúng tôi hiện đang điều tra một vấn đề ảnh hưởng đến việc cài đặt các phụ thuộc trên macOS. Do đó, người dùng macOS sẽ không thể hoàn thành hướng dẫn này vào thời điểm hiện tại. Chúng tôi sẽ cập nhật hướng dẫn ngay khi có bản sửa lỗi. Cảm ơn bạn đã kiên nhẫn và thông cảm!

Trong bài tập này, bạn sẽ xây dựng, chạy, và cải thiện một tác nhân AI với các công cụ từ một máy chủ MCP bên trong Visual Studio Code sử dụng AI Toolkit.

### -0- Bước chuẩn bị, thêm mô hình OpenAI GPT-4o vào My Models

Bài tập này sử dụng mô hình **GPT-4o**. Mô hình này cần được thêm vào **My Models** trước khi tạo tác nhân.

1. Mở tiện ích mở rộng **AI Toolkit** từ **Activity Bar**.
1. Trong phần **Catalog**, chọn **Models** để mở **Model Catalog**. Việc chọn **Models** sẽ mở **Model Catalog** trong một tab trình chỉnh sửa mới.
1. Trong thanh tìm kiếm của **Model Catalog**, nhập **OpenAI GPT-4o**.
1. Nhấp vào **+ Add** để thêm mô hình vào danh sách **My Models** của bạn. Đảm bảo rằng bạn đã chọn mô hình được **Hosted by GitHub**.
1. Trong **Activity Bar**, xác nhận rằng mô hình **OpenAI GPT-4o** xuất hiện trong danh sách.

### -1- Tạo một tác nhân

**Agent (Prompt) Builder** cho phép bạn tạo và tùy chỉnh các tác nhân AI của riêng mình. Trong phần này, bạn sẽ tạo một tác nhân mới và gán một mô hình để hỗ trợ cuộc trò chuyện.

1. Mở tiện ích mở rộng **AI Toolkit** từ **Activity Bar**.
1. Trong phần **Tools**, chọn **Agent (Prompt) Builder**. Việc chọn **Agent (Prompt) Builder** sẽ mở **Agent (Prompt) Builder** trong một tab trình chỉnh sửa mới.
1. Nhấp vào nút **+ New Agent**. Tiện ích mở rộng sẽ khởi chạy một trình hướng dẫn thiết lập thông qua **Command Palette**.
1. Nhập tên **Calculator Agent** và nhấn **Enter**.
1. Trong **Agent (Prompt) Builder**, ở trường **Model**, chọn mô hình **OpenAI GPT-4o (via GitHub)**.

### -2- Tạo yêu cầu hệ thống cho tác nhân

Sau khi tạo khung cho tác nhân, đã đến lúc định nghĩa tính cách và mục đích của nó. Trong phần này, bạn sẽ sử dụng tính năng **Generate system prompt** để mô tả hành vi dự định của tác nhân—trong trường hợp này là một tác nhân máy tính—và để mô hình viết yêu cầu hệ thống cho bạn.

1. Trong phần **Prompts**, nhấp vào nút **Generate system prompt**. Nút này mở trình tạo yêu cầu, sử dụng AI để tạo yêu cầu hệ thống cho tác nhân.
1. Trong cửa sổ **Generate a prompt**, nhập nội dung sau: `Bạn là một trợ lý toán học hữu ích và hiệu quả. Khi được đưa ra một bài toán liên quan đến số học cơ bản, bạn trả lời với kết quả chính xác.`
1. Nhấp vào nút **Generate**. Một thông báo sẽ xuất hiện ở góc dưới bên phải xác nhận rằng yêu cầu hệ thống đang được tạo. Sau khi hoàn tất, yêu cầu sẽ xuất hiện trong trường **System prompt** của **Agent (Prompt) Builder**.
1. Xem lại **System prompt** và chỉnh sửa nếu cần.

### -3- Tạo một máy chủ MCP

Bây giờ bạn đã định nghĩa yêu cầu hệ thống của tác nhân—hướng dẫn hành vi và phản hồi của nó—đã đến lúc trang bị cho tác nhân các khả năng thực tế. Trong phần này, bạn sẽ tạo một máy chủ MCP máy tính với các công cụ để thực hiện các phép toán cộng, trừ, nhân, và chia. Máy chủ này sẽ cho phép tác nhân thực hiện các phép toán thời gian thực để đáp ứng các yêu cầu ngôn ngữ tự nhiên.

AI Toolkit được trang bị các mẫu để dễ dàng tạo máy chủ MCP của riêng bạn. Chúng ta sẽ sử dụng mẫu Python để tạo máy chủ MCP máy tính.

*Lưu ý*: AI Toolkit hiện hỗ trợ Python và TypeScript.

1. Trong phần **Tools** của **Agent (Prompt) Builder**, nhấp vào nút **+ MCP Server**. Tiện ích mở rộng sẽ khởi chạy một trình hướng dẫn thiết lập thông qua **Command Palette**.
1. Chọn **+ Add Server**.
1. Chọn **Create a New MCP Server**.
1. Chọn **python-weather** làm mẫu.
1. Chọn **Default folder** để lưu mẫu máy chủ MCP.
1. Nhập tên sau cho máy chủ: **Calculator**
1. Một cửa sổ Visual Studio Code mới sẽ mở ra. Chọn **Yes, I trust the authors**.
1. Sử dụng terminal (**Terminal** > **New Terminal**), tạo một môi trường ảo: `python -m venv .venv`
1. Sử dụng terminal, kích hoạt môi trường ảo:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Sử dụng terminal, cài đặt các phụ thuộc: `pip install -e .[dev]`
1. Trong chế độ xem **Explorer** của **Activity Bar**, mở rộng thư mục **src** và chọn **server.py** để mở tệp trong trình chỉnh sửa.
1. Thay thế mã trong tệp **server.py** bằng nội dung sau và lưu:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
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
    ```

### -4- Chạy tác nhân với máy chủ MCP máy tính

Bây giờ tác nhân của bạn đã có công cụ, đã đến lúc sử dụng chúng! Trong phần này, bạn sẽ gửi các yêu cầu đến tác nhân để kiểm tra và xác nhận liệu tác nhân có sử dụng công cụ phù hợp từ máy chủ MCP máy tính hay không.

Bạn sẽ chạy máy chủ MCP máy tính trên máy phát triển cục bộ của mình thông qua **Agent Builder** như một MCP client.

1. Nhấn `F5` để bắt đầu gỡ lỗi máy chủ MCP. **Agent (Prompt) Builder** sẽ mở trong một tab trình chỉnh sửa mới. Trạng thái của máy chủ hiển thị trong terminal.
1. Trong trường **User prompt** của **Agent (Prompt) Builder**, nhập yêu cầu sau: `Tôi đã mua 3 món hàng giá $25 mỗi món, và sau đó sử dụng một phiếu giảm giá $20. Tôi đã trả bao nhiêu tiền?`
1. Nhấp vào nút **Run** để tạo phản hồi của tác nhân.
1. Xem lại đầu ra của tác nhân. Mô hình nên kết luận rằng bạn đã trả **$55**.
1. Dưới đây là phân tích những gì sẽ xảy ra:
    - Tác nhân chọn các công cụ **multiply** và **subtract** để hỗ trợ tính toán.
    - Các giá trị `a` và `b` tương ứng được gán cho công cụ **multiply**.
    - Các giá trị `a` và `b` tương ứng được gán cho công cụ **subtract**.
    - Phản hồi từ mỗi công cụ được cung cấp trong **Tool Response** tương ứng.
    - Đầu ra cuối cùng từ mô hình được cung cấp trong **Model Response** cuối cùng.
1. Gửi thêm các yêu cầu để kiểm tra thêm tác nhân. Bạn có thể chỉnh sửa yêu cầu hiện tại trong trường **User prompt** bằng cách nhấp vào trường và thay thế yêu cầu hiện tại.
1. Khi bạn hoàn tất việc kiểm tra tác nhân, bạn có thể dừng máy chủ thông qua **terminal** bằng cách nhập **CTRL/CMD+C** để thoát.

## Bài tập

Hãy thử thêm một mục công cụ mới vào tệp **server.py** của bạn (ví dụ: trả về căn bậc hai của một số). Gửi thêm các yêu cầu yêu cầu tác nhân sử dụng công cụ mới của bạn (hoặc các công cụ hiện có). Đảm bảo khởi động lại máy chủ để tải các công cụ mới được thêm vào.

## Giải pháp

[Solution](./solution/README.md)

## Những điểm chính

Những điểm chính từ chương này bao gồm:

- Tiện ích mở rộng AI Toolkit là một client tuyệt vời cho phép bạn sử dụng các máy chủ MCP và các công cụ của chúng.
- Bạn có thể thêm các công cụ mới vào máy chủ MCP, mở rộng khả năng của tác nhân để đáp ứng các yêu cầu ngày càng tăng.
- AI Toolkit bao gồm các mẫu (ví dụ: mẫu máy chủ MCP Python) để đơn giản hóa việc tạo các công cụ tùy chỉnh.

## Tài nguyên bổ sung

- [Tài liệu AI Toolkit](https://aka.ms/AIToolkit/doc)

## Tiếp theo
- Tiếp theo: [Kiểm tra & Gỡ lỗi](../08-testing/README.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.