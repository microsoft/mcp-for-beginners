# AGENTS.md

## 项目概述

**MCP for Beginners** 是一个开源教育课程，用于学习模型上下文协议（MCP）——一个标准化框架，用于 AI 模型与客户端应用之间的交互。本仓库提供全面的学习材料，包括多种编程语言的实践代码示例。

### 核心技术

- **编程语言**：C#、Java、JavaScript、TypeScript、Python、Rust
- **框架与 SDK**：
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **数据库**：PostgreSQL（带 pgvector 扩展）
- **云平台**：Azure（容器应用、OpenAI、内容安全、应用洞察）
- **构建工具**：npm、Maven、pip、Cargo
- **文档**：Markdown，支持自动多语言翻译（48+ 种语言）

### 架构

- **11 个核心模块（00-11）**：从基础到高级主题的循序渐进学习路径
- **实践实验室**：提供多语言完整解决方案代码的实践练习
- **示例项目**：包含 MCP 服务器和客户端的工作实现
- **翻译系统**：通过 GitHub Actions 自动化工作流支持多语言
- **图片资源**：集中管理的图片目录，包含翻译版本

## 设置命令

这是一个以文档为主的仓库。大部分设置在各个示例项目和实验室中完成。

### 仓库设置

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### 使用示例项目

示例项目位于：
- `03-GettingStarted/samples/` - 特定语言的示例
- `03-GettingStarted/01-first-server/solution/` - 第一个服务器实现
- `03-GettingStarted/02-client/solution/` - 客户端实现
- `11-MCPServerHandsOnLabs/` - 综合数据库集成实验室

每个示例项目都包含自己的设置说明：

#### TypeScript/JavaScript 项目
```bash
cd <project-directory>
npm install
npm start
```

#### Python 项目
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java 项目
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## 开发工作流程

### 文档结构

- **模块 00-11**：按顺序排列的核心课程内容
- **translations/**：特定语言版本（自动生成，请勿直接编辑）
- **translated_images/**：本地化图片版本（自动生成）
- **images/**：源图片和图表

### 修改文档

1. 仅编辑根模块目录（00-11）中的英文 Markdown 文件
2. 如有需要，更新 `images/` 目录中的图片
3. co-op-translator GitHub Action 会自动生成翻译
4. 推送到主分支时会重新生成翻译

### 使用翻译

- **自动翻译**：GitHub Actions 工作流处理所有翻译
- **请勿手动编辑** `translations/` 目录中的文件
- 翻译元数据嵌入在每个翻译文件中
- 支持的语言：48+ 种语言，包括阿拉伯语、中文、法语、德语、印地语、日语、韩语、葡萄牙语、俄语、西班牙语等

## 测试说明

### 文档验证

由于这是一个以文档为主的仓库，测试重点包括：

1. **链接验证**：确保所有内部链接有效
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **代码示例验证**：测试代码示例是否可以编译/运行
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown 格式检查**：确保格式一致性
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### 示例项目测试

每个特定语言的示例都包含自己的测试方法：

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## 代码风格指南

### 文档风格

- 使用清晰、适合初学者的语言
- 在适用的情况下提供多语言代码示例
- 遵循 Markdown 最佳实践：
  - 使用 ATX 风格标题（`#` 语法）
  - 使用带语言标识的围栏代码块
  - 为图片提供描述性替代文本
  - 保持合理的行长度（没有硬性限制，但要合理）

### 代码示例风格

#### TypeScript/JavaScript
- 使用 ES 模块（`import`/`export`）
- 遵循 TypeScript 严格模式约定
- 包含类型注解
- 目标为 ES2022

#### Python
- 遵循 PEP 8 风格指南
- 在适当的地方使用类型提示
- 为函数和类添加文档字符串
- 使用现代 Python 特性（3.8+）

#### Java
- 遵循 Spring Boot 约定
- 使用 Java 21 特性
- 遵循标准 Maven 项目结构
- 添加 Javadoc 注释

### 文件组织

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## 构建与部署

### 文档部署

仓库使用 GitHub Pages 或类似工具进行文档托管（如适用）。对主分支的更改会触发：

1. 翻译工作流（`.github/workflows/co-op-translator.yml`）
2. 自动翻译所有英文 Markdown 文件
3. 根据需要进行图片本地化

### 无需构建过程

本仓库主要包含 Markdown 文档。核心课程内容无需编译或构建步骤。

### 示例项目部署

各个示例项目可能有自己的部署说明：
- 请参阅 `03-GettingStarted/09-deployment/` 获取 MCP 服务器部署指南
- Azure 容器应用部署示例位于 `11-MCPServerHandsOnLabs/`

## 贡献指南

### 拉取请求流程

1. **Fork 和克隆**：Fork 仓库并在本地克隆你的 Fork
2. **创建分支**：使用描述性分支名称（例如 `fix/typo-module-3`，`add/python-example`）
3. **进行修改**：仅编辑英文 Markdown 文件（不要编辑翻译文件）
4. **本地测试**：验证 Markdown 渲染是否正确
5. **提交 PR**：使用清晰的 PR 标题和描述
6. **CLA**：按提示签署 Microsoft 贡献者许可协议

### PR 标题格式

使用清晰、描述性的标题：
- `[Module XX] 简要描述` 用于模块特定的更改
- `[Samples] 描述` 用于示例代码更改
- `[Docs] 描述` 用于一般文档更新

### 可以贡献的内容

- 修复文档或代码示例中的错误
- 添加其他语言的新代码示例
- 对现有内容进行澄清和改进
- 添加新的案例研究或实践示例
- 报告不清楚或错误的内容

### 不要做的事情

- 不要直接编辑 `translations/` 目录中的文件
- 不要编辑 `translated_images/` 目录
- 未讨论的情况下不要添加大型二进制文件
- 未协调的情况下不要更改翻译工作流文件

## 附加说明

### 仓库维护

- **更新日志**：所有重要更改记录在 `changelog.md` 中
- **学习指南**：使用 `study_guide.md` 导航课程概览
- **问题模板**：使用 GitHub 问题模板报告错误或提出功能请求
- **行为准则**：所有贡献者必须遵守 Microsoft 开源行为准则

### 学习路径

按顺序学习模块（00-11）以获得最佳学习效果：
1. **00-02**：基础知识（介绍、核心概念、安全性）
2. **03**：通过实践实现入门
3. **04-05**：实践实现和高级主题
4. **06-10**：社区、最佳实践和实际应用
5. **11**：综合数据库集成实验室（13 个连续实验）

### 支持资源

- **文档**：https://modelcontextprotocol.io/
- **规范**：https://spec.modelcontextprotocol.io/
- **社区**：https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**：Microsoft Azure AI Foundry Discord 服务器
- **相关课程**：请参阅 README.md 获取其他 Microsoft 学习路径

### 常见问题排查

**问：我的 PR 未通过翻译检查**
答：确保你只编辑了根模块目录中的英文 Markdown 文件，而不是翻译版本。

**问：如何添加新语言？**
答：语言支持通过 co-op-translator 工作流管理。请打开问题讨论添加新语言。

**问：代码示例无法运行**
答：确保你已按照特定示例的 README 中的设置说明操作。检查是否安装了正确版本的依赖项。

**问：图片无法显示**
答：验证图片路径是否为相对路径并使用正斜杠。图片应位于 `images/` 目录或 `translated_images/` 中的本地化版本。

### 性能注意事项

- 翻译工作流可能需要几分钟完成
- 提交前应优化大型图片
- 保持单个 Markdown 文件内容集中且大小合理
- 使用相对链接以提高可移植性

### 项目治理

本项目遵循 Microsoft 开源实践：
- 代码和文档使用 MIT 许可证
- Microsoft 开源行为准则
- 贡献需要签署 CLA
- 安全问题：遵循 SECURITY.md 指南
- 支持：参阅 SUPPORT.md 获取帮助资源

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。