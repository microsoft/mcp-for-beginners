# Thực Tiễn Bảo Mật MCP - Cập Nhật Tháng 9 Năm 2026

Hướng dẫn toàn diện này trình bày các thực tiễn bảo mật thiết yếu cho
việc triển khai hệ thống Model Context Protocol (MCP) dựa trên
**Đặc Tả MCP 2026-07-28** và các tiêu chuẩn ngành hiện hành. Những
thực tiễn này giải quyết cả các mối quan ngại bảo mật truyền thống và các mối đe dọa 
đặc thù AI duy nhất cho các triển khai MCP.

## Yêu Cầu Bảo Mật Quan Trọng

### Các Kiểm Soát Bảo Mật Bắt Buộc (Yêu Cầu MUST)

1. **Xác Thực Token**: Máy chủ MCP **KHÔNG ĐƯỢC** chấp nhận bất kỳ token nào không được cấp rõ ràng cho máy chủ MCP đó
2. **Xác Minh Ủy Quyền**: Các máy chủ MCP thực thi ủy quyền **PHẢI** xác minh TẤT CẢ các yêu cầu đến và **KHÔNG ĐƯỢC** sử dụng phiên để xác thực  
3. **Sự Đồng Ý của Người Dùng**: Các máy chủ proxy MCP sử dụng ID khách hàng bên thứ ba tĩnh **PHẢI** có được sự đồng ý rõ ràng từ mỗi khách hàng MCP trước khi chuyển tiếp luồng ủy quyền
4. **Bảo Mật Trạng Thái Handle**: Máy chủ MCP **KHÔNG ĐƯỢC** coi việc sở hữu
	handle trạng thái ứng dụng là xác thực và **PHẢI** ủy quyền cho mọi
	yêu cầu sử dụng nó

## Thực Tiễn Bảo Mật Cốt Lõi

### 1. Xác Thực & Làm Sạch Đầu Vào
- **Xác Thực Đầu Vào Toàn Diện**: Xác thực và làm sạch tất cả các đầu vào để ngăn chặn các tấn công tiêm nhiễm, vấn đề đại diện nhầm lẫn và lỗ hổng tiêm nhiễm prompt
- **Thực Thi Lược Đồ Tham Số**: Triển khai xác thực lược đồ JSON nghiêm ngặt cho tất cả tham số công cụ và đầu vào API
- **Lọc Nội Dung**: Sử dụng Microsoft Prompt Shields và Azure Content Safety để lọc nội dung độc hại trong prompt và phản hồi
- **Làm Sạch Đầu Ra**: Xác thực và làm sạch tất cả các đầu ra mô hình trước khi trình bày cho người dùng hoặc hệ thống hạ nguồn

### 2. Xuất Sắc trong Xác Thực & Ủy Quyền  
- **Nhà Cung Cấp Danh Tính Bên Ngoài**: Ủy quyền xác thực cho các nhà cung cấp danh tính đã thiết lập (Microsoft Entra ID, các nhà cung cấp OAuth 2.1) thay vì tự triển khai xác thực riêng
- **Đăng Ký Khách Hàng**: Ưu tiên Tài liệu Siêu dữ liệu ID Khách hàng hoặc đăng ký trước; chỉ dùng Đăng ký Khách hàng Động đã lỗi thời để tương thích
- **Quyền Hạn Chi Tiết**: Triển khai các quyền hạn chi tiết, riêng theo công cụ theo nguyên tắc quyền tối thiểu
- **Quản Lý Vòng Đời Token**: Sử dụng token truy cập ngắn hạn với xoay vòng bảo mật và xác thực đối tượng đúng cách
- **Xác Thực Đa Yếu Tố**: Yêu cầu MFA cho mọi truy cập quản trị và các thao tác nhạy cảm

### 3. Giao Thức Truyền Thông An Toàn
- **Bảo Mật Lớp Vận Chuyển**: Sử dụng HTTPS với xác thực chứng chỉ đúng cách
	cho truyền thông HTTP MCP từ xa; sử dụng cô lập quy trình và
	đăng nhập môi trường cho các máy chủ stdio cục bộ
- **Mã Hóa Đầu Cuối**: Triển khai các lớp mã hóa bổ sung cho dữ liệu cực kỳ nhạy cảm khi truyền và lưu trữ
- **Quản Lý Chứng Chỉ**: Duy trì quản lý vòng đời chứng chỉ đúng cách với các quy trình tự động gia hạn
- **Thực Thi Phiên Bản Giao Thức**: Sử dụng phiên bản MCP `2026-07-28`, bao gồm siêu dữ liệu phiên bản bắt buộc trên mỗi yêu cầu và từ chối các phiên bản không hỗ trợ


### 4. Giới Hạn Tốc Độ và Bảo Vệ Tài Nguyên Nâng Cao
- **Giới Hạn Tốc Độ Đa Lớp**: Triển khai giới hạn tốc độ theo người dùng, thông tin đăng nhập,
  hoạt động, công cụ, và tài nguyên để ngăn chặn lạm dụng
- **Giới Hạn Tốc Độ Thích Ứng**: Sử dụng giới hạn tốc độ dựa trên máy học thích ứng theo mẫu sử dụng và chỉ báo mối đe dọa
- **Quản Lý Hạn Ngạch Tài Nguyên**: Đặt giới hạn phù hợp cho tài nguyên tính toán, sử dụng bộ nhớ, và thời gian thực thi
- **Bảo Vệ DDoS**: Triển khai hệ thống bảo vệ DDoS toàn diện và phân tích lưu lượng

### 5. Ghi Log và Giám Sát Toàn Diện
- **Ghi Log Kiểm Tra Có Cấu Trúc**: Triển khai các bản ghi chi tiết, có thể tìm kiếm cho tất cả các hoạt động MCP, thực thi công cụ, và sự kiện bảo mật

- **Giám sát An ninh Thời gian Thực**: Triển khai hệ thống SIEM với khả năng phát hiện bất thường dựa trên AI cho các workload MCP
- **Ghi nhật ký tuân thủ Quyền riêng tư**: Ghi lại các sự kiện an ninh đồng thời tuân thủ các yêu cầu và quy định về bảo mật dữ liệu
- **Tích hợp Phản ứng Sự cố**: Kết nối hệ thống ghi nhật ký với các quy trình phản ứng sự cố tự động

### 6. Thực tiễn Lưu trữ An toàn Nâng cao
- **Mô-đun Bảo mật Phần cứng**: Sử dụng lưu trữ khóa được hỗ trợ bởi HSM (Azure Key Vault, AWS CloudHSM) cho các hoạt động mật mã quan trọng
- **Quản lý Khóa Mã hóa**: Triển khai xoay vòng khóa đúng cách, phân tách và kiểm soát truy cập cho các khóa mã hóa
- **Quản lý Bí mật**: Lưu trữ tất cả các khóa API, token và thông tin xác thực trong các hệ thống quản lý bí mật chuyên dụng
- **Phân loại Dữ liệu**: Phân loại dữ liệu dựa trên mức độ nhạy cảm và áp dụng các biện pháp bảo vệ phù hợp

### 7. Quản lý Token Nâng cao
- **Ngăn ngừa Chuyển tiếp Token**: Rõ ràng cấm các mẫu chuyển tiếp token vượt qua các kiểm soát an ninh
- **Xác thực Đối tượng Token**: Luôn xác minh các yêu cầu đối tượng token khớp với danh tính MCP server dự kiến
- **Ủy quyền dựa trên Claims**: Triển khai ủy quyền chi tiết dựa trên các claim token và thuộc tính người dùng
- **Ràng buộc Token**: Xác thực rằng token nhắm tới tài nguyên MCP dự kiến và
	ràng buộc các handle trạng thái ứng dụng phía máy chủ với chủ thể đã xác thực

### 8. Trạng thái Ứng dụng An toàn

- **Handle Trạng thái Mật mã**: Tạo các handle mờ đục, không xác định trước
	cho trạng thái trải dài qua các yêu cầu
- **Ràng buộc theo Người dùng**: Ràng buộc mỗi handle phía máy chủ với chủ thể đã xác thực; không tin vào bất kỳ ID người dùng nào do client cung cấp
										
- **Kiểm soát Vòng đời**: Hết hạn và thu hồi các handle, và định nghĩa cách các caller phục hồi từ trạng thái lỗi thời
											
- **Ủy quyền theo Yêu cầu**: Kiểm tra lại ủy quyền mỗi khi handle được trình bày; handle là một tên gọi, không phải chứng chỉ
											

### 9. Kiểm soát An ninh Đặc thù cho AI
- **Phòng chống Tiêm chủng Prompt**: Triển khai Microsoft Prompt Shields với spotlighting, dấu phân cách và kỹ thuật đánh dấu dữ liệu
- **Ngăn ngừa Độc Tố Công cụ**: Xác minh metadata công cụ, giám sát các thay đổi động, và kiểm tra tính toàn vẹn của công cụ
- **Xác thực Đầu ra Mô hình**: Quét đầu ra mô hình để phát hiện rò rỉ dữ liệu tiềm ẩn, nội dung độc hại hoặc vi phạm chính sách an ninh
- **Bảo vệ Cửa sổ Ngữ cảnh**: Triển khai các kiểm soát để ngăn ngừa đầu độc cửa sổ ngữ cảnh và các tấn công thao túng

### 10. An ninh Thực thi Công cụ
- **Sandbox thực thi**: Chạy thực thi công cụ trong môi trường cô lập container hóa với giới hạn tài nguyên
- **Phân tách Đặc quyền**: Thực thi công cụ với đặc quyền tối thiểu cần thiết và phân tách các tài khoản dịch vụ
- **Cách ly Mạng**: Triển khai phân đoạn mạng cho môi trường thực thi công cụ
- **Giám sát Thực thi**: Giám sát thực thi công cụ để phát hiện hành vi khác thường, sử dụng tài nguyên và vi phạm an ninh

### 11. Xác thực An ninh Liên tục
- **Kiểm thử An ninh Tự động**: Tích hợp kiểm thử an ninh vào pipeline CI/CD với các công cụ như GitHub Advanced Security
- **Quản lý Lỗ hổng**: Quét thường xuyên tất cả các phụ thuộc, bao gồm mô hình AI và dịch vụ bên ngoài
- **Kiểm thử Xâm nhập**: Thực hiện đánh giá an ninh định kỳ hướng trực tiếp vào triển khai MCP
- **Đánh giá Mã An ninh**: Thực hiện bắt buộc đánh giá an ninh cho tất cả các thay đổi mã liên quan MCP

### 12. An ninh Chuỗi Cung ứng cho AI
- **Xác minh Thành phần**: Xác minh nguồn gốc, tính toàn vẹn và an ninh của tất cả các thành phần AI (mô hình, embeddings, API)
- **Quản lý Phụ thuộc**: Duy trì danh mục cập nhật tất cả phần mềm và phụ thuộc AI với theo dõi lỗ hổng
- **Kho Lưu trữ Tin cậy**: Sử dụng nguồn tin cậy đã xác minh cho tất cả mô hình AI, thư viện và công cụ

- **Giám sát Chuỗi Cung ứng**: Liên tục giám sát các nhà cung cấp dịch vụ AI và kho lưu trữ mô hình để phát hiện các sự cố an ninh


## Mô Hình Bảo Mật Nâng Cao

### Kiến Trúc Zero Trust cho MCP
- **Không Bao Giờ Tin Tưởng, Luôn Kiểm Tra**: Triển khai xác minh liên tục cho tất cả người tham gia MCP
- **Phân đoạn vi mô**: Cô lập các thành phần MCP với kiểm soát mạng và nhận dạng chi tiết
- **Truy cập Có Điều Kiện**: Triển khai kiểm soát truy cập dựa trên rủi ro thích ứng theo ngữ cảnh và hành vi
- **Đánh giá Rủi ro Liên tục**: Đánh giá năng động trạng thái bảo mật dựa trên các chỉ báo mối đe dọa hiện tại

### Triển Khai AI Bảo Vệ Quyền Riêng Tư
- **Giảm Thiểu Dữ Liệu**: Chỉ tiết lộ dữ liệu tối thiểu cần thiết cho mỗi hoạt động MCP
- **Bảo Mật Quyền Riêng Tư Vi Phân**: Triển khai các kỹ thuật bảo vệ quyền riêng tư cho xử lý dữ liệu nhạy cảm
- **Mã Hóa Đồng Thuận**: Sử dụng kỹ thuật mã hóa nâng cao cho tính toán an toàn trên dữ liệu được mã hóa
- **Học Liên Kết**: Triển khai phương pháp học phân tán bảo vệ tính địa phương và quyền riêng tư của dữ liệu

### Ứng Phó Sự Cố cho Hệ Thống AI
- **Quy Trình Sự Cố Riêng cho AI**: Phát triển quy trình ứng phó sự cố phù hợp với các mối đe dọa AI và MCP cụ thể
- **Phản Hồi Tự Động**: Triển khai cách ly và khắc phục tự động cho các sự cố bảo mật AI phổ biến  
- **Khả Năng Pháp Y**: Duy trì sẵn sàng pháp y cho các sự cố xâm phạm hệ thống AI và rò rỉ dữ liệu
- **Quy Trình Phục Hồi**: Thiết lập quy trình phục hồi từ đầu độc mô hình AI, tấn công tiêm mã lệnh và xâm phạm dịch vụ

## Tài Nguyên & Tiêu Chuẩn Triển Khai

### 🏔️ Đào Tạo Bảo Mật Thực Hành
- **[Hội Thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Hội thảo thực hành toàn diện để bảo vệ máy chủ MCP trên Azure
- **[Hướng Dẫn Bảo Mật MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)** - Kiến trúc tham khảo và hướng dẫn triển khai OWASP MCP Top 10

### Tài Liệu Chính Thức MCP
- [Đặc Tả MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Đặc tả giao thức MCP hiện tại
- [Thực Tiễn Bảo Mật MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Hướng dẫn bảo mật chính thức
- [Đặc Tả Ủy Quyền MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Mô hình ủy quyền HTTP
- [Giao Thức Vận Chuyển MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Yêu cầu về giao thức vận chuyển

### Giải Pháp Bảo Mật Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Bảo vệ nâng cao chống tiêm prompt
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Lọc nội dung AI toàn diện
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Quản lý nhận dạng và truy cập doanh nghiệp
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Quản lý bí mật và chứng thực an toàn
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Quét bảo mật chuỗi cung ứng và mã nguồn

### Tiêu Chuẩn & Khung Bảo Mật
- [Thực Tiễn Bảo Mật OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Hướng dẫn bảo mật OAuth hiện tại
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Rủi ro bảo mật ứng dụng web
- [OWASP Top 10 cho LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Rủi ro bảo mật riêng cho AI
- [Khung Quản Lý Rủi Ro AI NIST](https://www.nist.gov/itl/ai-risk-management-framework) - Quản lý rủi ro AI toàn diện
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Hệ thống quản lý an ninh thông tin

### Hướng Dẫn & Bài Học Triển Khai
- [Quản Lý API Azure làm Cổng Xác Thực MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Mô hình xác thực doanh nghiệp
- [Microsoft Entra ID với Máy Chủ MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Tích hợp nhà cung cấp nhận dạng
- [Triển Khai Lưu Trữ Token An Toàn](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Thực tiễn quản lý token tốt nhất
- [Mã Hóa Đầu Cuối cho AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Mô hình mã hóa nâng cao

### Tài Nguyên Bảo Mật Nâng Cao
- [Vòng Đời Phát Triển Bảo Mật Microsoft](https://www.microsoft.com/sdl) - Thực hành phát triển an toàn
- [Hướng Dẫn Đội Đỏ AI](https://learn.microsoft.com/security/ai-red-team/) - Kiểm thử bảo mật riêng cho AI
- [Mô Hình Đe Dọa cho Hệ Thống AI](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Phương pháp mô hình đe dọa AI
- [Kỹ Thuật Bảo Vệ Quyền Riêng Tư cho AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Kỹ thuật AI bảo vệ quyền riêng tư

### Tuân Thủ & Quản Trị
- [Tuân Thủ GDPR cho AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Tuân thủ về quyền riêng tư trong hệ thống AI
- [Khung Quản Trị AI](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Triển khai AI có trách nhiệm
- [SOC 2 cho Dịch Vụ AI](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Kiểm soát bảo mật dành cho nhà cung cấp dịch vụ AI
- [Tuân Thủ HIPAA cho AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Yêu cầu tuân thủ AI trong chăm sóc sức khỏe

### DevSecOps & Tự Động Hóa
- [Dây Chuyền DevSecOps cho AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Dây chuyền phát triển AI an toàn
- [Kiểm Thử Bảo Mật Tự Động](https://learn.microsoft.com/security/engineering/devsecops) - Xác thực bảo mật liên tục
- [Bảo Mật Hạ Tầng Như Mã](https://learn.microsoft.com/security/engineering/infrastructure-security) - Triển khai hạ tầng an toàn
- [Bảo Mật Container cho AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - An ninh container hóa khối lượng công việc AI

### Giám sát & Ứng Phó Sự Cố  
- [Azure Monitor cho Khối Lượng Công Việc AI](https://learn.microsoft.com/azure/azure-monitor/overview) - Giải pháp giám sát toàn diện
- [Ứng Phó Sự Cố Bảo Mật AI](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Quy trình ứng phó sự cố riêng cho AI
- [SIEM cho Hệ Thống AI](https://learn.microsoft.com/azure/sentinel/overview) - Quản lý thông tin và sự kiện bảo mật

- [Tình báo Đe dọa cho AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Nguồn tin tình báo đe dọa AI

## 🔄 Cải tiến Liên tục

### Luôn Cập nhật Các Chuẩn Mực Mới
- **Cập nhật Đặc tả MCP**: Theo dõi các thay đổi chính thức về đặc tả MCP và các cảnh báo bảo mật
- **Tình báo Đe dọa**: Đăng ký các nguồn cấp dữ liệu đe dọa bảo mật AI và cơ sở dữ liệu lỗ hổng  
- **Tham gia Cộng đồng**: Tham gia thảo luận cộng đồng bảo mật MCP và các nhóm công tác
- **Đánh giá Định kỳ**: Thực hiện đánh giá tình trạng bảo mật hàng quý và cập nhật các thực hành phù hợp

### Góp phần vào Bảo mật MCP
- **Nghiên cứu Bảo mật**: Đóng góp cho nghiên cứu bảo mật MCP và các chương trình công bố lỗ hổng
- **Chia sẻ Thực hành Tốt nhất**: Chia sẻ các triển khai bảo mật và bài học rút ra với cộng đồng
- **Phát triển Chuẩn mực**: Tham gia phát triển đặc tả MCP và tạo lập các tiêu chuẩn bảo mật
- **Phát triển Công cụ**: Phát triển và chia sẻ các công cụ và thư viện bảo mật cho hệ sinh thái MCP

---

*Tài liệu này phản ánh các thực hành bảo mật tốt nhất MCP tính đến ngày 9 tháng 9 năm 2026,
dựa trên Đặc tả MCP `2026-07-28`. Các thực hành bảo mật nên được xem xét định kỳ
khi giao thức và bối cảnh đe dọa phát triển.*

## Tiếp theo là gì

- Đọc thêm: [Các Thực hành Bảo mật MCP](./mcp-security-best-practices.md)
- Quay lại: [Tổng quan Mô-đun Bảo mật](./README.md)
- Tiếp tục tới: [Mô-đun 3: Bắt đầu](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->