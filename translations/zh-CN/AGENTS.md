# AGENTS.md

## 项目概览

**MCP入门指南** 是一个开源的教育课程，用于学习模型上下文协议（MCP）——一种用于 AI 模型与客户端应用之间交互的标准化框架。本仓库提供了涵盖多种编程语言的详尽学习资料和实操代码示例。

### 关键技术

- <strong>编程语言</strong>：C#、Java、JavaScript、TypeScript、Python、Rust
- **框架与 SDK**：
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- <strong>数据库</strong>：带 pgvector 扩展的 PostgreSQL
- <strong>云平台</strong>：Azure（容器应用、OpenAI、安全内容、应用分析）
- <strong>构建工具</strong>：npm、Maven、pip、Cargo
- <strong>文档</strong>：使用 Markdown 并支持 48+ 种语言的自动多语言翻译

### 架构

- **11 个核心模块（00-11）**：从基础到高级的顺序学习路径
- <strong>实操实验</strong>：多语言完整解决方案代码的实践练习
- <strong>示例项目</strong>：完整运行的 MCP 服务器和客户端实现
- <strong>翻译系统</strong>：自动化 GitHub Actions 工作流支持多语言
- <strong>图片资源</strong>：集中管理并附带翻译版本的图片目录

## 设置命令

这是一个以文档为主的仓库。大多数环境配置均在各个示例项目和实验中进行。

### 仓库设置

```bash
# 克隆仓库
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### 使用示例项目

示例项目位于：
- `03-GettingStarted/samples/` - 语言特定示例
- `03-GettingStarted/01-first-server/solution/` - 第一个服务器实现
- `03-GettingStarted/02-client/solution/` - 客户端实现
- `11-MCPServerHandsOnLabs/` - 综合数据库集成实验

每个示例项目内均包含其独立的设置说明：

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
# 或者
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

### MCP 7-28 准备情况

#### 仓库准备检查清单

- [x] <strong>新贡献者指导清晰</strong>：该文件定义了仓库目的、
  结构、贡献规则及示例设置路径。
- [x] **构建/测试/代码风格检查命令及精确参数**：
  - 仓库文档代码风格检查：
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - 仓库文档链接模式审计：
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript 示例验证：
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python 示例验证：
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java 示例验证：
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`

- [x] **一个可以成为MCP工具的现实工作流**：
  `validate_curriculum_change`
- [x] **输入/输出是明确的**（见下面的规范）。
- [x] <strong>权限和失败模式有文档说明</strong>（见下面的规范）。
- [x] **CI的可测试性是明确的**（确定性命令，明确的
  退出代码和机器可读的输出）。

#### 候选MCP工具工作流：`validate_curriculum_change`

##### 目标

验证课程文档更改和代表性示例代码
在合并前的健康状况。

##### 输入

- `changed_paths: string[]`（必需）- PR中更改的相对路径。
- `run_docs_lint: boolean`（默认 `true`）
- `run_links_audit: boolean`（默认 `true`）
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  （默认全部为 `false`）

##### 输出

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### 权限

- 只读取工作区文件并写入工具生成的工件（例如，lint
  报告，测试日志）；不写入 `translations/` 或
  `translated_images/`。
- 执行本地shell命令。
- 仅在恢复包时允许网络访问（`npm ci`，
  `python -m pip install`，`mvn`依赖解析）。
- 无权限推送、合并或修改 `translations/` 或
  `translated_images/`。

##### 失败模式

- `E_NO_INPUT_PATHS`：`changed_paths` 为空。
- `E_INVALID_PATH`：输入路径越出仓库根目录。
- `E_LINT_FAILED`：Markdown lint命令返回非零。
- `E_LINK_AUDIT_FAILED`：链接审核命令返回非零。
- `E_SAMPLE_TEST_FAILED`：示例测试/构建返回非零。
- `E_TIMEOUT`：命令超出配置的超时。

##### 推荐的CI契约

为实现自动验证，配置一个CI任务，该任务：

- 在触及 `*.md`，示例代码或者本文件的拉取请求时触发。
- 运行上面列出的确切命令。
- 将日志持久化为工件。
- 任何非零退出码都使任务失败。

#### 如果你从此仓库发布MCP服务器

- [ ] 阅读MCP 7-28的草案变更日志：
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] 针对SDK测试版运行你的服务器：
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] 移除会话和握手假设；将每个请求视为
  独立完整：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] 对原始HTTP请求发送 `Mcp-Method` 和 `Mcp-Name` 头：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] 审核硬编码错误代码（`missing resource` 从 `-32002` 移至 `-32602`）。

- [ ] 标记和规划弃用的根、采样和
  日志迁移：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] 迁移实验性的 `2025-11-25` Tasks API：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] 审查OAuth和OpenID Connect强化的授权：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### 文档结构

- **模块00-11**：核心课程内容，按顺序排列
- **translations/**：特定语言版本（自动生成，不要直接编辑）
- **translated_images/**：本地化的图片版本（自动生成）
- **images/**：源图片和图表

### 进行文档更改

1. 仅编辑根模块目录（00-11）中的英文markdown文件
2. 如有需要，更新 `images/` 目录中的图片
3. co-op-translator GitHub Action 会自动生成翻译
4. 向主分支推送时会重新生成翻译

### 处理翻译

- <strong>自动翻译</strong>：GitHub Actions工作流管理所有翻译
- <strong>不要手动编辑</strong> `translations/` 目录中的文件
- 翻译元数据嵌入每个翻译文件中
- 支持语言：48种以上，包括阿拉伯语、中文、法语、德语、印地语、日语、韩语、葡萄牙语、俄语、西班牙语等

## 测试说明

### 文档验证

因为这是主要的文档库，测试重点包括：

1. <strong>链接模式审核</strong>：列出Markdown链接供审核

   ```bash
   # 列出 Markdown 链接（模式审核）
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. <strong>代码示例验证</strong>：测试代码示例能否编译/运行

   ```bash
   # 导航到特定样本并运行其测试
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown 代码风格检查**：检查格式一致性

   ```bash
   # 如有需要，请使用 markdownlint
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
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
- 在适用时包含多语言的代码示例
- 遵循markdown最佳实践：
  - 使用ATX风格标题（`#` 语法）
  - 使用带语言标识的围栏代码块
  - 为图片包含描述性alt文本
  - 保持行长度合理（没有硬限制，但要合适）

### 代码示例风格

#### TypeScript/JavaScript
- 使用ES模块（`import`/`export`）
- 遵循TypeScript严格模式规范
- 包含类型注解
- 目标ES2022

#### Python
- 遵循PEP 8风格指南
- 适当使用类型提示
- 为函数和类添加文档字符串
- 使用现代Python特性（3.8及以上）

#### Java
- 遵循Spring Boot惯例
- 使用Java 21特性
- 遵循标准Maven项目结构
- 添加Javadoc注释

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

## 构建和部署

### 文档部署

仓库使用GitHub Pages或类似服务进行文档托管（如果适用）。对主分支的更改会触发：

1. 翻译工作流 (`.github/workflows/co-op-translator.yml`)
2. 自动翻译所有英文markdown文件
3. 根据需要的图片本地化

### 无需构建过程

本仓库主要包含markdown文档。核心课程内容不需要编译或构建步骤。

### 示例项目部署

各个示例项目可能有其部署说明：
- 参见 `03-GettingStarted/09-deployment/` 获得MCP服务器部署指南
- `11-MCPServerHandsOnLabs/` 中的Azure容器应用部署示例

## 贡献指南

### Pull Request 流程

1. **Fork和克隆**：Fork仓库，并在本地克隆你的Fork
2. <strong>创建分支</strong>：使用描述性分支名称（例如 `fix/typo-module-3`，`add/python-example`）
3. <strong>进行更改</strong>：只编辑英文markdown文件（不编辑翻译）
4. <strong>本地测试</strong>：验证markdown渲染正确
5. **提交PR**：使用清晰的PR标题和描述
6. **签署CLA**：按提示签署微软贡献者许可协议

### PR标题格式

使用清晰、描述性的标题：
- `[Module XX] 简要说明` 用于模块特定更改
- `[Samples] 说明` 用于示例代码更改
- `[Docs] 说明` 用于一般文档更新

### 可以贡献的内容

- 文档或代码示例中的错误修复
- 新增其他语言的代码示例
- 现有内容的澄清和改进
- 新的案例研究或实际示例
- 不明确或错误内容的问题报告

### 不要做的事项

- 不要直接编辑 `translations/` 目录中的文件
- 不要编辑 `translated_images/` 目录
- 未经讨论不要添加大型二进制文件
- 未经协调不要更改翻译工作流文件

## 其他说明

### 仓库维护

- <strong>变更日志</strong>：所有重要更改都记录在 `changelog.md`
- <strong>学习指南</strong>：使用 `study_guide.md` 进行课程导航概览
- <strong>问题模板</strong>：使用GitHub问题模板报告错误和功能请求
- <strong>行为守则</strong>：所有贡献者必须遵守微软开源行为守则

### 学习路径

按顺序学习模块（00-11）以获得最佳学习效果：
1. **00-02**：基础（介绍、核心概念、安全）
2. **03**：动手入门实践
3. **04-05**：实操与高级主题
4. **06-10**：社区、最佳实践和实际应用
5. **11**：综合数据库集成实验（13个连续实验）

### 支持资源

- <strong>文档</strong>：https://modelcontextprotocol.io/
- <strong>规范</strong>：https://spec.modelcontextprotocol.io/
- <strong>社区</strong>：https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**：Microsoft Foundry Discord服务器
- <strong>相关课程</strong>：请参见 README.md 中的其他微软学习路径

### 常见故障排查

**问：我的PR未通过翻译检查怎么办？**
答：确保只编辑了根模块目录中的英文markdown文件，而非翻译版本。

**问：如何添加新语言？**
答：语言支持通过co-op-translator工作流管理。需要添加新语言时请先开issues讨论。

**问：代码示例无法运行**

A: 确保您已按照特定示例的 README 中的设置说明操作。检查是否安装了正确版本的依赖项。

**Q: 图片无法显示**
A: 验证图片路径是否为相对路径并使用正斜杠。图片应位于 `images/` 目录下，或者针对本地化版本位于 `translated_images/`。

### 性能注意事项

- 翻译工作流程可能需要几分钟才能完成
- 大图应在提交前进行优化
- 让单个 Markdown 文件保持专注且大小合理
- 使用相对链接以提高可移植性

### 项目管理

本项目遵循微软开源实践：
- 代码和文档采用 MIT 许可证
- 微软开源行为规范
- 贡献者需签署 CLA
- 安全问题：遵循 SECURITY.md 指南
- 支持：请参阅 SUPPORT.md 获取帮助资源

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->