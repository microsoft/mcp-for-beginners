# Sử dụng một server từ tiện ích AI Toolkit cho Visual Studio Code

Khi bạn xây dựng một tác nhân AI, không chỉ là tạo ra các phản hồi thông minh; mà còn là cung cấp cho tác nhân khả năng thực hiện hành động. Đó chính là lúc Giao thức Ngữ cảnh Mô hình (Model Context Protocol - MCP) phát huy tác dụng. MCP giúp các tác nhân truy cập các công cụ và dịch vụ bên ngoài một cách đồng nhất. Hãy tưởng tượng nó như việc bạn cắm tác nhân của mình vào một hộp công cụ mà nó có thể *thực sự* sử dụng.

Giả sử bạn kết nối một tác nhân với server MCP máy tính của bạn. Bất ngờ, tác nhân có thể thực hiện các phép toán chỉ bằng cách nhận một lời nhắc như "47 nhân 89 bằng bao nhiêu?" — không cần phải lập trình cứng logic hay xây dựng API tùy chỉnh.

## Tổng quan

Bài học này đề cập đến cách kết nối một server MCP máy tính với tác nhân bằng tiện ích [AI Toolkit](https://aka.ms/AIToolkit) trong Visual Studio Code, cho phép tác nhân của bạn thực hiện các phép toán như cộng, trừ, nhân, chia qua ngôn ngữ tự nhiên.

AI Toolkit là một tiện ích mạnh mẽ cho Visual Studio Code giúp đơn giản hóa việc phát triển tác nhân. Kỹ sư AI dễ dàng xây dựng ứng dụng AI bằng cách phát triển và thử nghiệm các mô hình AI tạo sinh—cả trên máy cục bộ hoặc trên đám mây. Tiện ích hỗ trợ hầu hết các mô hình tạo sinh lớn hiện nay.

*Lưu ý*: AI Toolkit hiện hỗ trợ Python và TypeScript.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có khả năng:

- Sử dụng một server MCP qua AI Toolkit.
- Cấu hình tác nhân để nó có thể khám phá và sử dụng các công cụ do server MCP cung cấp.
- Sử dụng các công cụ MCP qua ngôn ngữ tự nhiên.

## Cách tiếp cận

Đây là cách chúng ta cần tiếp cận ở mức độ tổng quan:

- Tạo một tác nhân và định nghĩa lời nhắc hệ thống của nó.
- Tạo một server MCP với các công cụ máy tính.
- Kết nối Trình xây dựng tác nhân với server MCP.
- Thử nghiệm việc gọi công cụ của tác nhân qua ngôn ngữ tự nhiên.

Tuyệt vời, bây giờ khi đã hiểu quy trình, hãy cấu hình một tác nhân AI để tận dụng công cụ bên ngoài qua MCP, nâng cao khả năng của nó!

## Yêu cầu trước

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit cho Visual Studio Code](https://aka.ms/AIToolkit)

## Bài tập: Sử dụng một server

> [!WARNING]
> Lưu ý dành cho người dùng macOS. Chúng tôi hiện đang điều tra một lỗi ảnh hưởng đến việc cài đặt phụ thuộc trên macOS. Do đó, người dùng macOS sẽ không thể hoàn thành hướng dẫn này vào lúc này. Chúng tôi sẽ cập nhật hướng dẫn ngay khi có bản sửa lỗi. Cảm ơn bạn đã kiên nhẫn và thông cảm!

Trong bài tập này, bạn sẽ xây dựng, chạy và nâng cấp một tác nhân AI với các công cụ từ server MCP bên trong Visual Studio Code bằng AI Toolkit.

### -0- Bước đầu, thêm mô hình OpenAI GPT-4o vào My Models

Bài tập sử dụng mô hình **GPT-4o**. Mô hình nên được thêm vào **My Models** trước khi tạo tác nhân.

![Ảnh chụp màn hình giao diện chọn mô hình trong tiện ích AI Toolkit của Visual Studio Code. Tiêu đề ghi "Tìm mô hình phù hợp cho giải pháp AI của bạn" kèm phụ đề khuyến khích người dùng khám phá, thử nghiệm và triển khai mô hình AI. Dưới "Popular Models," có sáu thẻ mô hình: DeepSeek-R1 (được lưu trữ trên GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Nhỏ, Nhanh), và DeepSeek-R1 (được lưu trữ trên Ollama). Mỗi thẻ có tùy chọn “Add” và “Try in Playground”.](../../../../translated_images/vi/aitk-model-catalog.2acd38953bb9c119.webp)

1. Mở tiện ích **AI Toolkit** từ **Activity Bar**.
1. Trong phần **Catalog**, chọn **Models** để mở **Model Catalog**. Việc chọn **Models** sẽ mở **Model Catalog** trong tab trình soạn thảo mới.
1. Trong thanh tìm kiếm của **Model Catalog**, nhập **OpenAI GPT-4o**.
1. Bấm **+ Add** để thêm mô hình vào danh sách **My Models**. Đảm bảo bạn chọn mô hình **Hosted by GitHub**.
1. Ở **Activity Bar**, xác nhận mô hình **OpenAI GPT-4o** xuất hiện trong danh sách.

### -1- Tạo một tác nhân

**Agent (Prompt) Builder** cho phép bạn tạo và tùy chỉnh các tác nhân AI của riêng bạn. Trong phần này, bạn sẽ tạo tác nhân mới và gán mô hình để điều khiển cuộc hội thoại.

![Ảnh chụp màn hình giao diện "Calculator Agent" trong tiện ích AI Toolkit của Visual Studio Code. Bảng bên trái chọn mô hình "OpenAI GPT-4o (qua GitHub)." Lời nhắc hệ thống ghi "Bạn là một giáo sư đại học dạy toán," và lời nhắc người dùng là "Giải thích cho tôi phương trình Fourier theo cách đơn giản." Các tùy chọn khác gồm nút thêm công cụ, bật MCP Server, và chọn kết quả có cấu trúc. Nút “Run” màu xanh phía dưới. Bảng bên phải, dưới "Get Started with Examples," liệt kê ba tác nhân mẫu: Web Developer (với MCP Server, Bộ đơn giản hóa cấp hai, và Trình giải mã giấc mơ, kèm mô tả ngắn về chức năng).](../../../../translated_images/vi/aitk-agent-builder.901e3a2960c3e477.webp)

1. Mở tiện ích **AI Toolkit** từ **Activity Bar**.
1. Trong phần **Tools**, chọn **Agent (Prompt) Builder**. Việc chọn **Agent (Prompt) Builder** sẽ mở tab trình soạn thảo mới.
1. Bấm nút **+ New Agent**. Tiện ích sẽ khởi động trình hướng dẫn cấu hình qua **Command Palette**.
1. Nhập tên **Calculator Agent** và nhấn **Enter**.
1. Trong **Agent (Prompt) Builder**, tại trường **Model**, chọn mô hình **OpenAI GPT-4o (via GitHub)**.

### -2- Tạo lời nhắc hệ thống cho tác nhân

Khi tác nhân đã được tạo, đã đến lúc định hình cá tính và mục đích của nó. Trong phần này, bạn sẽ sử dụng tính năng **Generate system prompt** để mô tả hành vi dự kiến của tác nhân—ở đây, là tác nhân máy tính—và để mô hình giúp bạn viết lời nhắc hệ thống.

![Ảnh chụp màn hình giao diện "Calculator Agent" trong AI Toolkit cho Visual Studio Code với cửa sổ modal mở tiêu đề "Generate a prompt." Modal giải thích có thể tạo mẫu lời nhắc bằng cách cung cấp thông tin cơ bản và có hộp văn bản với mẫu lời nhắc: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Dưới hộp văn bản có các nút "Close" và "Generate." Phía sau modal, phần cấu hình tác nhân hiển thị mô hình "OpenAI GPT-4o (via GitHub)" đã chọn và các trường lời nhắc hệ thống và người dùng.](../../../../translated_images/vi/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Trong phần **Prompts**, bấm nút **Generate system prompt**. Nút này mở trình tạo lời nhắc sử dụng AI để tạo lời nhắc hệ thống cho tác nhân.
1. Trong cửa sổ **Generate a prompt**, nhập: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Bấm nút **Generate**. Một thông báo sẽ hiện ở góc dưới bên phải xác nhận lời nhắc đang được tạo. Khi hoàn thành, lời nhắc sẽ xuất hiện trong trường **System prompt** của **Agent (Prompt) Builder**.
1. Xem lại lời nhắc **System prompt** và chỉnh sửa nếu cần.

### -3- Tạo một server MCP

Giờ bạn đã định nghĩa lời nhắc hệ thống cho tác nhân—hướng dẫn hành vi và phản hồi của nó—đã đến lúc trang bị cho tác nhân những khả năng thực tế. Trong phần này, bạn sẽ tạo một server MCP máy tính với các công cụ thực hiện các phép tính cộng, trừ, nhân, chia. Server này cho phép tác nhân thực hiện phép toán thời gian thực dựa trên lời nhắc ngôn ngữ tự nhiên.

![Ảnh chụp màn hình phần dưới của giao diện Calculator Agent trong AI Toolkit cho Visual Studio Code. Hiển thị thực đơn có thể mở rộng cho “Tools” và “Structure output,” cùng với menu thả xuống “Choose output format” đặt thành “text.” Bên phải có nút “+ MCP Server” để thêm một server Model Context Protocol. Có biểu tượng hình ảnh giả lập trên phần Tools.](../../../../translated_images/vi/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit được trang bị các mẫu để dễ dàng tạo server MCP của riêng bạn. Chúng ta sẽ dùng mẫu Python để tạo server MCP máy tính.

*Lưu ý*: AI Toolkit hiện hỗ trợ Python và TypeScript.

1. Trong phần **Tools** của **Agent (Prompt) Builder**, bấm nút **+ MCP Server**. Tiện ích sẽ khởi động trình hướng dẫn cấu hình qua **Command Palette**.
1. Chọn **+ Add Server**.
1. Chọn **Create a New MCP Server**.
1. Chọn mẫu **python-weather**.
1. Chọn **Default folder** để lưu mẫu server MCP.
1. Nhập tên server: **Calculator**
1. Một cửa sổ Visual Studio Code mới sẽ mở. Chọn **Yes, I trust the authors**.
1. Sử dụng terminal (**Terminal** > **New Terminal**), tạo môi trường ảo: `python -m venv .venv`
1. Kích hoạt môi trường ảo qua terminal:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Cài đặt các phụ thuộc qua terminal: `pip install -e .[dev]`
1. Trong giao diện **Explorer** của **Activity Bar**, mở rộng thư mục **src** và chọn **server.py** để mở file trong trình soạn thảo.
1. Thay thế mã trong file **server.py** bằng đoạn mã sau và lưu lại:

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

### -4- Chạy tác nhân với server MCP máy tính

Giờ tác nhân của bạn đã có công cụ, đã đến lúc sử dụng chúng! Trong phần này, bạn sẽ gửi lời nhắc đến tác nhân để kiểm tra và xác thực xem tác nhân có sử dụng công cụ phù hợp từ server MCP máy tính hay không.

![Ảnh chụp màn hình giao diện Calculator Agent trong AI Toolkit cho Visual Studio Code. Bên trái, dưới “Tools,” server MCP tên local-server-calculator_server được thêm vào với bốn công cụ khả dụng: add, subtract, multiply và divide. Một huy hiệu cho biết có bốn công cụ hoạt động. Phần “Structure output” đang thu gọn và nút "Run" màu xanh. Bên phải, dưới “Model Response,” tác nhân gọi các công cụ multiply và subtract với đầu vào lần lượt {"a": 3, "b": 25} và {"a": 75, "b": 20}. Phản hồi cuối cùng "Tool Response" hiển thị 75.0. Có nút “View Code” ở dưới.](../../../../translated_images/vi/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Bạn sẽ chạy server MCP máy tính trên máy phát triển cục bộ qua **Agent Builder** với vai trò là client MCP.

1. Nhấn `F5` để bắt đầu gỡ lỗi server MCP. **Agent (Prompt) Builder** sẽ mở trong tab trình soạn thảo mới. Trạng thái server hiển thị ở terminal.
1. Ở trường **User prompt** của **Agent (Prompt) Builder**, nhập lời nhắc: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Bấm nút **Run** để tạo phản hồi cho tác nhân.
1. Xem lại đầu ra của tác nhân. Mô hình nên kết luận rằng bạn đã trả **$55**.
1. Đây là các bước xảy ra:
    - Tác nhân chọn công cụ **multiply** và **subtract** để hỗ trợ tính toán.
    - Các giá trị `a` và `b` được gán tương ứng cho công cụ **multiply**.
    - Các giá trị `a` và `b` được gán tương ứng cho công cụ **subtract**.
    - Phản hồi từ mỗi công cụ được cung cấp trong phần **Tool Response** tương ứng.
    - Kết quả cuối cùng được mô hình cung cấp ở phần **Model Response**.
1. Gửi thêm các lời nhắc khác để thử nghiệm thêm tác nhân. Bạn có thể chỉnh sửa lời nhắc hiện tại trong trường **User prompt** bằng cách bấm vào trường và thay thế lời nhắc.
1. Khi kết thúc thử nghiệm, bạn có thể dừng server qua **terminal** bằng cách nhấn **CTRL/CMD+C** để thoát.

## Bài tập về nhà

Thử thêm một công cụ mới vào file **server.py** của bạn (ví dụ: trả về căn bậc hai của một số). Gửi các lời nhắc mới đòi hỏi tác nhân sử dụng công cụ mới (hoặc các công cụ hiện có). Nhớ khởi động lại server để tải các công cụ mới thêm.

## Giải pháp

[Giải pháp](./solution/README.md)

## Những điều cần ghi nhớ

Những điểm chính trong chương này là:

- Tiện ích AI Toolkit là một client tuyệt vời cho phép bạn sử dụng các server MCP và công cụ của chúng.
- Bạn có thể thêm công cụ mới vào các server MCP, mở rộng khả năng của tác nhân đáp ứng các yêu cầu thay đổi.
- AI Toolkit bao gồm các mẫu (ví dụ: mẫu server MCP Python) giúp đơn giản hóa việc tạo công cụ tùy chỉnh.

## Tài nguyên bổ sung

- [Tài liệu AI Toolkit](https://aka.ms/AIToolkit/doc)

## Tiếp theo
- Tiếp theo: [Kiểm tra & Gỡ lỗi](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->