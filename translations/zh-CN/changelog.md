# 更新日志：MCP 初学者课程

本文档记录了模型上下文协议（MCP）初学者课程的重要变更。变更按时间倒序记录（最新变更优先）。

## 2026年7月29日

### 新模块08伴随课程：可靠性 Sidecars 与安全重试

新增一个供应商无关的伴随课程，针对创建现实世界
影响的 MCP 工具，符合最终的 `2026-07-28` 规范。

- <strong>新增</strong>: [可靠性 Sidecar 伴随课程][reliability-sidecar]
  通过一个支持票故事、两个 Mermaid 图表和一个重试决策
  流程，解释稳定运行关键、原子重复接纳、
  协调、证据及 Tasks 扩展边界。
- <strong>新增</strong>: 一个标准库 Python 与 SQLite 故障注入练习
  使用独立的操作和票据存储演示外部效应提交后响应丢失的情况。
  六个确定性测试覆盖简单重复、
  受守护的重启恢复、负载冲突、缓存结果、
  活跃声明和并发重复接纳。
- <strong>更新</strong>: 模块08现在链接伴随课程，标识
  最终 `2026-07-28` 无状态请求模型，区分 OpenTelemetry
  可观测性与已弃用的 MCP 日志功能，且将其
  通用重试示例限定为只读操作。
- <strong>可选</strong>: 课程将其便携概念映射到一个带标记的社区
  实现，而不将托管服务或网络调用作为
  练习内容。

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2026年7月2日

### 新课程：2026-07-28 MCP 规范候选发布版

新增关于即将发布的 `2026-07-28` MCP 规范候选版本的介绍（2026年5月21日宣布；正式发布计划于7月28日），内容摘自[官方公告博客文章](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)。课程的基线仍为<strong>MCP 规范 2025-11-25</strong>，直到新版本发布，因此此内容作为前瞻指导，而非现有课程的重写。

- <strong>新增</strong>: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — 详细介绍无状态协议核心（移除 `initialize` 握手和 `Mcp-Session-Id`）、新的 `Mcp-Method`/`Mcp-Name` 路由头、`ttlMs`/`cacheScope` 缓存元数据、_meta 中的 W3C Trace Context、正式的扩展框架（MCP 应用和新的 Tasks 扩展）、六个授权强化 SEP、Roots/Sampling/Logging 的弃用，以及工具模式转向完整 JSON Schema 2020-12。
- <strong>更新</strong> 并提供面向未来的提醒，链接至新课程：
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): 协议版本注释、Sampling/Roots/Logging/Tasks 部分，以及“下一步是什么”

  - [02-Security/README.md](./02-Security/README.md): 授权强化提示
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): 无状态传输提示
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): 采样弃用提示
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): 日志弃用和任务扩展提示
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): 无状态/会话路由提示
  - [README.md](./README.md): 规范部分中的“展望未来”注释和课程模块表中新添加的 `1.1` 条目
  - [study_guide.md](./study_guide.md): 核心概念概览中的前瞻性要点和带日期的附录说明
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): 关于 `mcp-session-id` 传输映射的提示，位于无状态请求模型之前
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): 关于根上下文/采样弃用和任务扩展的模块概览提示
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): 授权强化提示

## 2026年6月24日

### 新课程：在 Copilot 应用中使用 MCP

- [工具部分](./12-tooling/README.md) 添加了工具部分。
- [Copilot 应用中的 MCP](./12-tooling/01-copilot-app/README.md)

## 2026年6月16日

### MCP 规范对齐与样例验证

已基于当前<strong>MCP 规范 2025-11-25</strong>及最新官方 SDK 验证课程，然后修正了剩余的陈旧规范引用，并确认核心样例仍可构建和运行。

#### 规范版本修正（2025-06-18 / 2025-03-26 → 2025-11-25）

更新了仍声称旧规范版本为<em>当前/最新</em>标准的英文内容，并将链接指向权威的 `modelcontextprotocol.io` 规范路径：
- **05-AdvancedTopics/mcp-security/README.md**：更新了“当前标准”横幅、介绍、核心安全原则标题、强制要求标题、Microsoft Entra ID 部分、参考与资源链接及结束安全通知（共8处引用）至 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**：更新了额外资源规范链接和“当前标准”横幅至 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**：用当前的 2025-11-25 安全最佳实践页面替换了过时的 `2025-03-26` 安全与信任链接

- **03-GettingStarted/14-sampling/README.md**: 更新了官方采样文档链接至2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**：将现在时态的“当前 MCP 规范”引用和附加资源规范链接更新至 2025-11-25（保留历史 SSE 弃用说明以确保准确性）

#### 针对当前 SDK 的示例验证

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**：`npm install` 安装了解决方案中 `@modelcontextprotocol/sdk@1.29.0`；`tsc --noEmit` 编译无类型错误 — 现有的 `McpServer`/`StdioServerTransport` API 依然有效
- **Python (03-GettingStarted/01-first-server/solution/python)**：在隔离的 `.venv` 中使用 `mcp[cli]` (1.27.2) 验证；`py_compile` 通过，`FastMCP.list_tools()` 正确返回了 `add` 和 `subtract` 工具
- 确认所有示例中 `@modelcontextprotocol/sdk` 版本范围 (`>=1.26.0` / `^1.26.0` / `^1.27.0`) 均能干净解析至当前的 `1.29.0`，且无破坏性 API 变更

#### 依赖固定版本对齐（消除版本差异）

将过时的 SDK 固定版本升级，使每个示例跟踪当前 MCP 版本，符合整个仓库的一致约定：
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**：将 `@modelcontextprotocol/sdk` 从 `^1.8.0` 升级为 `>=1.26.0`，并将陈旧的 `"updated for MCP 2025-06-18"` 包描述更新为 `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** 和 **lab4/code/github_mcp_server/pyproject.toml**：将精确固定版本 `mcp==1.23.0` 升级为 `mcp>=1.26.0`；重新生成了两个 `uv.lock` 文件（使用 `uv lock`），锁文件解析当前为 `mcp 1.27.2`，与清单保持同步

#### 教程内容空白分析 — 最新规范功能覆盖

验证教程已覆盖 MCP 2025-11-25 中引入/扩展的所有基础元素，内容无遗漏：
- <strong>采样</strong>：课程 03-GettingStarted/14-sampling 以及 05-AdvancedTopics/mcp-sampling
- **引导（包括 URL 模式）**：文档覆盖在 01-CoreConcepts 和 05-AdvancedTopics/mcp-protocol-features
- <strong>根上下文</strong>：文档覆盖在 00-Introduction、01-CoreConcepts 和 05-AdvancedTopics/mcp-root-contexts
- **任务（实验性，长时间运行操作）**：文档覆盖在 01-CoreConcepts 和 05-AdvancedTopics/mcp-protocol-features
- <strong>工具注解</strong>（`readOnlyHint` / `destructiveHint`）：文档覆盖在 01-CoreConcepts 和 05-AdvancedTopics/mcp-protocol-features

### 安全加固与依赖漏洞修复

对每个依赖清单和示例代码进行了全面安全检查，修复了所有报告的 npm 安全告警和一处代码级漏洞。修复后，`npm audit` 在所有审计目录中报告 **0 个漏洞**。

#### npm 依赖漏洞（传递依赖）— 已修复

审计了所有 15 个提交的 `package-lock.json` 文件。漏洞限于由 MCP Inspector 开发工具、OpenAI 客户端和 MCP SDK 引入的传递依赖；均已解决且未破坏示例：
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** 和 **lab3/code/weather_mcp/inspector**：升级了 `@modelcontextprotocol/inspector`（从 `0.16.6` / `0.14.1` 到 `0.22.0`），清除了内置的 `ajv`, `brace-expansion`, `diff`, `path-to-regexp` 和 `ws` 漏洞。添加 npm `overrides` 条目，强制使用补丁版本 `shell-quote@1.8.4`，消除了 `concurrently` 相关的关键漏洞；重新生成锁文件（现 0 漏洞）
- **03-GettingStarted/samples/typescript**：通过 `npm audit fix` 升级了传递依赖 `qs`（中危）到补丁版本
- **03-GettingStarted/samples/javascript**：通过 `npm audit fix` 升级了传递依赖 `hono`（中危）到补丁版本
- **03-GettingStarted/03-llm-client/solution/typescript**：通过 `npm audit fix` 升级了传递依赖 `form-data`（高危）到补丁版本
- **03-GettingStarted/11-simple-auth/solution/typescript**：生成缺失的 `package-lock.json`，确保项目可复现且可审计（0 漏洞）

#### 代码级安全修复（OWASP A03：注入）

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**：移除了 `open_in_vscode` 工具中的 `shell=True`。先前的 `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` 允许文件夹路径中的 shell 元字符被 `cmd.exe` 解释（命令注入风险）。现改为直接启动解析后的 `Code.exe`，将文件夹作为参数传入 — 无 shell 调用 — 功能等效且安全。

#### Python 依赖审计

- 使用 `pip-audit` 审计了所有 Python 依赖集。`05-AdvancedTopics` 和 `03-GettingStarted/samples/python` 的依赖无已知漏洞（包含的 `mcp` / `httpx` / `pydantic` / `python-dotenv` 版本均解析到当前补丁版本）
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**：`pip-audit` 报告传递依赖 **`werkzeug` 3.1.1** 存在三个 `safe_join` Windows 设备名拒绝服务漏洞 — `CVE-2025-66221`、`CVE-2026-21860` 和 `CVE-2026-27199`（均已在 3.1.6 修复）。添加显式安全固定版本 `werkzeug>=3.1.6`，确保解析为补丁版本；验证此约束与 `chainlit` / `mcp` / `semantic-kernel` 版本栈兼容无碍

### 产品名称重塑

更新了所有课程内容以反映微软的产品名称重塑：


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**：更新了 Discord 社区链接

- **AGENTS.md**：更新 Discord 服务器引用
- **README.md**：更新技术生态系统引用
- **study_guide.md**：更新案例研究引用
- **05-AdvancedTopics/README.md**：更新模块 5.13 标题和描述
- **05-AdvancedTopics/mcp-integration/README.md**：更新章节标题和描述
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**：完整模块标题和内容更新
- **05-AdvancedTopics/mcp-security-entra/README.md**：更新交叉引用链接
- **07-LessonsfromEarlyAdoption/README.md**：更新案例研究引用
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**：更新第 9 节标题、徽章和功能
- **08-BestPractices/README.md**：更新 Discord 社区链接
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**：更新 Discord 频道引用
- **09-CaseStudy/docs-mcp/solution/python/README.md**：更新模型部署引用
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**：更新 AI 服务表
- **11-MCPServerHandsOnLabs/03-Setup/README.md**：更新资源引用

#### AI 工具包 / AITK → Microsoft Foundry Toolkit 扩展插件，用于 VS Code
- **README.md**：更新主课程引用
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**：更新模块标题、概述及所有模块标题
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**：更新标题、学习目标、设置说明和资源
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**：更新标题、学习目标、MCP 主机表和交叉引用
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**：更新标题、徽章、先决条件和资源
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**：更新 Agent Builder 参考和反馈链接
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**：更新先决条件和扩展引用

---

## 2026 年 4 月 11 日

### 新课程、文档修复及依赖更新

#### 添加新课程内容

**模块 05 - 高级主题**
- **课程 5.17：带 MCP 的对抗性多智能体推理**（`05-AdvancedTopics/mcp-adversarial-agents/README.md`）：新增全面指南，涵盖多智能体系统中的对抗性辩论模式
  - Mermaid 架构图：两个智能体 → 共享 MCP 服务器 → 辩论记录 → 裁判 → 判决
  - Python 和 TypeScript 实现的共享 MCP 工具服务器（`web_search` + `run_python`）
  - 对立系统提示（支持 / 反对 / 裁判）含明确工具使用需求
  - 用 Python、TypeScript 和 C# 编写的辩论协调器，管理轮次并路由论点
  - 为协调器连接真实工具调用的 MCP `ClientSession` 绑定
  - 用例表（幻觉检测、威胁建模、API 设计评审、事实验证、技术选型）
  - 安全考量：沙箱执行、工具调用验证、速率限制、审计日志
  - 结构化练习，包含三个实际方案（代码审查、架构决策、内容审核）

#### 文档修复

**模块 03 - 入门指导**
- **05-stdio-server/README.md**：修复不完整的 TypeScript stdio 服务器示例 —— 补充缺失的传输实例化（`new StdioServerTransport()`）和 `server.connect(transport)` 调用，以匹配同章节 Python 和 .NET 示例
- **14-sampling/README.md**：修正拼写错误 — 将 `"Sampling is an davanced features"` 改为 `"Sampling is an advanced feature"`

#### 课程更新

**主 README.md**
- 在课程表中添加条目 5.17（带 MCP 的对抗性多智能体推理），并提供直达新课程的链接

**05-AdvancedTopics/README.md**
- 在课程表中添加课程 5.17 行

**study_guide.md**
- 在高级主题的思维导图和文字描述中添加对抗性多智能体推理主题

#### 代码与安全修复

**模块 05 - 对抗性智能体（`mcp-adversarial-agents`）**
- **安全修复 — 命令注入**：用 `execFile` + `promisify` 替代 TypeScript `run_python` 工具中的 `execSync` Shell 插值，消除了命令注入风险（LLM 控制的代码现以字面 argv 元素传递，无 Shell 参与）
- **MCP 工具循环绑定**：更新 Python 辩论协调器，使用异步 `AsyncAnthropic` 客户端（替代阻塞同步 `Anthropic`），每轮直接传递活动 `ClientSession`，通过 `session.list_tools()` 获取工具定义，循环调用 `session.call_tool()` 直到模型输出最终文本响应

#### 依赖更新

- 多个包（03-GettingStarted、04-PracticalImplementation、10-StreamliningAIWorkflows）中将 `hono` 升级至 4.12.12
- TypeScript 包中将 `@hono/node-server` 从 1.19.11 升级至 1.19.13
- Python 包（10-StreamliningAIWorkflows 实验室 3 和 4）中将 `cryptography` 从 46.0.5 升级至 46.0.7
- 10-StreamliningAIWorkflows 检查器中将 `lodash` 从 4.17.23 升级至 4.18.1

#### 翻译

- 同步 48+ 语言翻译，包含最新源代码更改（i18n 更新）

---

## 2026 年 2 月 5 日

### 库存范围验证和导航改进

#### 新增课程内容

**模块 03 - 入门指导**
- **12-mcp-hosts/README.md**：新增设置 MCP 主机的全面指南
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf 配置示例
  - 所有主流主机的 JSON 配置模板
  - 传输类型比较表（stdio、SSE/HTTP、WebSocket）
  - 常见连接问题排查
  - 主机配置安全最佳实践

- **13-mcp-inspector/README.md**：新增 MCP Inspector 调试指南
  - 安装方式（npx、npm 全局安装、源码安装）
  - 通过 stdio 和 HTTP/SSE 连接服务器
  - 测试工具、资源和提示流程
  - VS Code 与 MCP Inspector 集成
  - 常见调试场景及解决方案

**模块 04 - 实践实现**
- **pagination/README.md**：新增分页实现指南
  - Python、TypeScript、Java 中的基于光标的分页模式
  - 客户端分页处理
  - 光标设计策略（不透明 vs 结构化）
  - 性能优化建议

**模块 05 - 高级主题**
- **mcp-protocol-features/README.md**：新增协议功能深度解析
  - 进度通知实现
  - 请求取消模式
  - 资源模板及 URI 模式
  - 服务器生命周期管理
  - 日志级别控制
  - 使用 JSON-RPC 代码的错误处理模式

#### 导航修复（更新 24+ 文件）

**主模块 README 文件**
现链接至首个课程及下一个模块

**02-安全 子文件**
- 所有 5 个安全补充文件现含“下一步”导航：

**09-案例研究文件**
- 所有案例研究文件现具备顺序导航：

**10-StreamliningAI 实验室**
在模块 10 概览和模块 11 添加“下一步”部分

#### 代码与内容修复

**SDK 及依赖更新**
修复空白 openai 版本为 `^4.95.0`
SDK 版本从 `^1.8.0` 更新为 `>=1.26.0`
MCP 版本锁定更新为 `>=1.26.0`

<strong>代码修复</strong>
修正无效模型 `gpt-4o-mini` 为 `gpt-4.1-mini`

<strong>内容修复</strong>
修复断链 `READMEmd` → `README.md`，修正课程表头 `Module 1-3` → `Module 0-3`，修正大小写路径
删除损坏重复的案例研究 5 内容

<strong>初学者指导改进</strong>
为初学者添加了适当的介绍、学习目标和先决条件

#### 课程更新

**主 README.md**
- 在课程表中添加条目 3.12（MCP 主机）、3.13（MCP Inspector）、4.1（分页）、5.16（协议功能）

**模块 README 文件**
添加课程 12 和 13 至课程列表
添加了实践指南部分及分页链接
添加课程 5.15（自定义传输）和 5.16（协议功能）

**study_guide.md**
- 更新思维导图，包含所有新主题：MCP 主机设置、MCP Inspector、分页策略、协议功能深度解析

## 2026 年 1 月 28 日

### MCP 规范 2025-11-25 合规审查

#### 核心概念增强（01-CoreConcepts/）
- **新增客户端原语 - Roots**：新增全面文档，介绍 Roots 客户端原语，支持服务器理解文件系统边界及访问权限
- <strong>工具注解</strong>：新增工具行为注解文档（`readOnlyHint`、`destructiveHint`），以改善工具执行决策
- <strong>采样中的工具调用</strong>：更新采样文档，新增模型驱动工具调用时的 `tools` 和 `toolChoice` 参数说明
- **URL 模式引导**：新增 URL 方式引导文档，支持服务器发起外部网页交互
- **任务（实验性）**：新增实验性任务功能文档，支持持久执行包装和延迟结果检索
- <strong>图标支持</strong>：指出工具、资源、资源模板和提示均可包含图标作为附加元数据

#### 文档更新
- **README.md**：添加 MCP 规范 2025-11-25 版本引用及基于日期的版本说明
- **study_guide.md**：更新课程地图，包含核心概念部分的任务和工具注解；更新文档时间戳

#### 规范合规验证
- <strong>协议版本</strong>：验证所有文档均引用当前 MCP 规范 2025-11-25
- <strong>架构对齐</strong>：确认文档准确描述双层架构（数据层 + 传输层）
- <strong>原语文档</strong>：验证服务器原语（资源、提示、工具）及客户端原语（采样、引导、日志、Roots）
- <strong>传输机制</strong>：核实 STDIO 和可流 HTTP 传输文档准确
- <strong>安全指导</strong>：确认与当前 MCP 安全最佳实践文档一致

#### 关键 MCP 2025-11-25 功能文档
- **OpenID Connect 发现**：认证服务器通过 OIDC 进行发现
- **OAuth 客户端 ID 元数据文档**：推荐客户端注册机制
- **JSON Schema 2020-12**：MCP 架构定义默认语法
- **SDK 分层系统**：正式定义 SDK 功能支持与维护要求
- <strong>治理结构</strong>：正式定义 MCP 治理中的工作组和兴趣组

### 安全文档重大更新（02-Security/）

#### MCP 安全峰会研讨会（Sherpa）集成
- <strong>新增实操培训资源</strong>：在所有安全文档中全面集成了 [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- <strong>远征路线覆盖</strong>：文档涵盖从大本营至峰顶的完整营地进展
- **OWASP 对齐**：所有安全指导映射到 OWASP MCP Azure 安全指南风险

#### OWASP MCP 前 10 风险集成
- <strong>新章节</strong>：在主安全 README 中添加 OWASP MCP 前 10 安全风险表及 Azure 缓解措施
- <strong>基于风险的文档</strong>：更新 mcp-security-controls-2025.md，添加 OWASP MCP 风险引用（MCP01-MCP08）对应安全域
- <strong>参考架构</strong>：链接到 OWASP MCP Azure 安全指南参考架构和实施模式

#### 更新安全文件
- **README.md**：添加 Sherpa 研讨会概述、远征路线表、OWASP MCP 前 10 风险总结和实操培训部分
- **mcp-security-controls-2025.md**：更新头部为 2026 年 2 月，添加 OWASP 风险引用（MCP01-MCP08），修正规范版本不一致
- **mcp-security-best-practices-2025.md**：新增 Sherpa 和 OWASP 资源部分，更新时间戳
- **mcp-best-practices.md**：新增实操培训部分，包含 Sherpa 和 OWASP 链接
- **azure-content-safety-implementation.md**：添加 OWASP MCP06 引用，Sherpa 第 3 营对齐及额外资源部分

#### 新增资源链接
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure 安全指南](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP 前十](https://owasp.org/www-project-mcp-top-10/)
- 个人 OWASP MCP 风险页面 (MCP01-MCP10)

### 全课程 MCP 规范 2025-11-25 对齐

#### 模块 03 - 入门
- **SDK 文档**：将 Go SDK 添加至官方 SDK 列表；更新所有 SDK 引用以符合 MCP 规范 2025-11-25
- <strong>传输说明</strong>：更新 STDIO 和 HTTP 流式传输描述，增加明确规范引用

#### 模块 04 - 实际实现
- **SDK 更新**：新增 Go SDK；并在 SDK 列表中添加规范版本引用
- <strong>授权规范</strong>：更新 MCP 授权规范链接至当前 2025-11-25 版本

#### 模块 05 - 高级主题
- <strong>新功能</strong>：新增 MCP 规范 2025-11-25 特性说明（任务、工具注释、URL 模式引导、根节点）
- <strong>安全资源</strong>：新增 OWASP MCP 前十和 Sherpa 研讨会链接作为附加参考

#### 模块 06 - 社区贡献
- **SDK 列表**：新增 Swift 和 Rust SDK；更新规范链接至 2025-11-25
- <strong>规范引用</strong>：更新 MCP 规范链接至直接规范 URL

#### 模块 07 - 早期采纳经验
- <strong>资源更新</strong>：新增 MCP 规范 2025-11-25 链接和 OWASP MCP 前十至附加资源

#### 模块 08 - 最佳实践
- <strong>规范版本</strong>：更新 MCP 规范引用至 2025-11-25
- <strong>安全资源</strong>：新增 OWASP MCP 前十和 Sherpa 研讨会至附加参考

#### 模块 10 - 简化 AI 工作流
- <strong>徽章更新</strong>：将 MCP 版本徽章从 SDK 版本 (1.9.3) 改为规范版本 (2025-11-25)
- <strong>资源链接</strong>：更新 MCP 规范链接；新增 OWASP MCP 前十

#### 模块 11 - MCP 服务器实操实验
- <strong>规范引用</strong>：更新 MCP 规范链接至 2025-11-25 版本
- <strong>安全资源</strong>：新增 OWASP MCP 前十至官方资源

## 2025 年 12 月 18 日

### 安全文档更新 - MCP 规范 2025-11-25

#### MCP 安全最佳实践 (02-Security/mcp-best-practices.md) - 规范版本更新
- <strong>协议版本更新</strong>：更新引用至最新 MCP 规范 2025-11-25（发布于 2025 年 11 月 25 日）
  - 将所有规范版本引用从 2025-06-18 更新至 2025-11-25
  - 更新文档日期引用从 2025 年 8 月 18 日至 2025 年 12 月 18 日
  - 核实所有规范 URL 指向最新文档
- <strong>内容验证</strong>：全面验证安全最佳实践符合最新标准
  - <strong>微软安全方案</strong>：核实当前术语及链接，涉及 Prompt Shields（原“越狱风险检测”）、Azure 内容安全、Microsoft Entra ID 和 Azure Key Vault
  - **OAuth 2.1 安全**：确认符合最新 OAuth 安全最佳实践
  - **OWASP 标准**：验证 LLMs 相关 OWASP 前十引用依然有效
  - **Azure 服务**：核实所有微软 Azure 文档链接及最佳实践
- <strong>标准对齐</strong>：所有被引用的安全标准确认最新有效
  - NIST 人工智能风险管理框架
  - ISO 27001:2022
  - OAuth 2.1 安全最佳实践
  - Azure 安全与合规框架
- <strong>实施资源</strong>：核实所有实现指南链接及资源
  - Azure API 管理认证模式
  - Microsoft Entra ID 集成指南
  - Azure Key Vault 秘密管理
  - DevSecOps 流水线及监控方案

### 文档质量保证
- <strong>规范合规性</strong>：确保所有强制 MCP 安全要求（必须/禁止）与最新规范一致
- <strong>资源时效性</strong>：核实所有外部链接到 Microsoft 文档、安全标准及实施指南
- <strong>最佳实践覆盖</strong>：确认全面涵盖认证、授权、针对 AI 的威胁、供应链安全及企业模式

## 2025 年 10 月 6 日

### 入门章节扩展 – 高级服务器使用和简单认证

#### 高级服务器用法 (03-GettingStarted/10-advanced)
- <strong>新增章节</strong>：提供全面的高级 MCP 服务器使用指南，涵盖常规及低层服务器架构。
  - <strong>常规与低层服务器对比</strong>：详细对比并提供 Python 和 TypeScript 代码示例。
  - <strong>基于处理器的设计</strong>：解释基于处理器的工具/资源/提示管理，实现可扩展且灵活的服务器。
  - <strong>实用模式</strong>：实际案例说明低层服务器模式在高级功能和架构中的应用价值。

#### 简单认证 (03-GettingStarted/11-simple-auth)
- <strong>新增章节</strong>：逐步指导如何在 MCP 服务器实现简单认证。
  - <strong>认证概念</strong>：清晰说明认证与授权及凭据管理。
  - <strong>基础认证实现</strong>：Python (Starlette) 和 TypeScript (Express) 中基于中间件的认证模式及代码示例。
  - <strong>迈向高级安全</strong>：引导从简单认证过渡到 OAuth 2.1 和基于角色访问控制（RBAC），并引用高级安全模块。

这些新增内容为构建更健壮、安全且灵活的 MCP 服务器实现提供了实用的操作指南，连接基础概念与高级生产模式。

## 2025 年 9 月 29 日

### MCP 服务器数据库集成实验 - 全面动手学习路径

#### 11-MCPServerHandsOnLabs - 新增完整数据库集成课程
- **完整的 13 个实验学习路径**：增添用于构建具备 PostgreSQL 数据库集成的生产级 MCP 服务器综合动手机制
  - <strong>真实案例实现</strong>：Zava 零售分析案例展示企业级模式
  - <strong>结构化学习进程</strong>：
    - **实验 00-03：基础** - 介绍、核心架构、安全性和多租户、环境搭建
    - **实验 04-06：构建 MCP 服务器** - 数据库设计与模式、MCP 服务器实现、工具开发  
    - **实验 07-09：高级功能** - 语义搜索集成、测试与调试、VS Code 集成
    - **实验 10-12：生产部署与最佳实践** - 部署策略、监控与可观察性、最佳实践与优化
  - <strong>企业技术</strong>：FastMCP 框架、采用 pgvector 的 PostgreSQL、Azure OpenAI 嵌入、Azure 容器应用、Application Insights
  - <strong>高级功能</strong>：行级安全 (RLS)、语义搜索、多租户数据访问、向量嵌入、实时监控

#### 术语标准化 - 模块转换为实验
- <strong>全面文档更新</strong>：系统性将 11-MCPServerHandsOnLabs 中所有 README 文件的“模块”术语更新为“实验”
  - <strong>章节标题</strong>：将所有 13 个实验中的“本模块涵盖内容”更新为“本实验涵盖内容”
  - <strong>内容描述</strong>：文档内“本模块提供...”更改为“本实验提供...”
  - <strong>学习目标</strong>：更新“完成本模块后...”为“完成本实验后...”
  - <strong>导航链接</strong>：所有“模块 XX:”引用更新为“实验 XX:”以统一交叉引用和导航
  - <strong>完成跟踪</strong>：将“完成本模块后...”更新为“完成本实验后...”
  - <strong>保留技术引用</strong>：保持配置文件中的 Python 模块引用不变（例如 `"module": "mcp_server.main"`）

#### 学习指南增强 (study_guide.md)
- <strong>视觉课程地图</strong>：新增“11. 数据库集成实验”章节及其综合实验结构可视化
- <strong>仓库结构</strong>：从十个主要部分更新为十一部分，详细描述 11-MCPServerHandsOnLabs
- <strong>学习路径指导</strong>：增强导航说明，涵盖 00-11 章节
- <strong>技术覆盖</strong>：添加 FastMCP、PostgreSQL、Azure 服务集成细节
- <strong>学习成果</strong>：强调生产就绪服务器开发、数据库集成模式及企业安全

#### 主 README 结构增强
- <strong>实验术语</strong>：在 11-MCPServerHandsOnLabs 主 README.md 中统一使用“实验”结构
- <strong>学习路径组织</strong>：从基础概念到高级实现再到生产部署的清晰进阶
- <strong>真实案例聚焦</strong>：强调实践动手学习及企业级模式与技术

### 文档质量与一致性改进
- <strong>动手学习重点</strong>：强化文档中动手实验方法
- <strong>企业模式聚焦</strong>：突出生产就绪实现及企业安全考量
- <strong>技术集成</strong>：全面覆盖现代 Azure 服务及 AI 集成模式
- <strong>学习进阶</strong>：从基础概念到生产部署的清晰有序路径

## 2025 年 9 月 26 日

### 案例研究增强 - GitHub MCP 注册表集成

#### 案例研究 (09-CaseStudy/) - 生态系统发展聚焦
- **README.md**：重大扩展，包含全面 GitHub MCP 注册表案例研究
  - **GitHub MCP 注册表案例研究**：2025 年 9 月 GitHub MCP 注册表发布详尽分析
    - <strong>问题分析</strong>：详细审视 MCP 服务器发现和部署的碎片化挑战
    - <strong>解决方案架构</strong>：GitHub 集中式注册表模式与一键 VS Code 安装
    - <strong>业务影响</strong>：明显提升开发者入门和生产效率
    - <strong>战略价值</strong>：专注于模块化代理部署及跨工具互操作性
    - <strong>生态系统发展</strong>：作为代理系统集成的基础平台定位
  - <strong>增强案例研究结构</strong>：更新全部七个案例研究，统一格式并增加详细描述
    - Azure AI 旅行代理：多代理协同重点
    - Azure DevOps 集成：工作流自动化聚焦
    - 实时文档检索：Python 控制台客户端实现
    - 互动学习计划生成器：Chainlit 对话式 Web 应用
    - 编辑器内文档：VS Code 和 GitHub Copilot 集成
    - Azure API 管理：企业 API 集成模式
    - GitHub MCP 注册表：生态系统发展与社区平台
  - <strong>全面结论</strong>：重写结论部分，涵盖七个案例研究，涉及多个 MCP 实现维度
    - 企业集成、多代理编排、开发者生产力
    - 生态系统发展、教育应用分类
    - 加强对架构模式、实现策略和最佳实践的见解
    - 强调 MCP 作为成熟的生产就绪协议

#### 学习指南更新 (study_guide.md)
- <strong>视觉课程地图</strong>：更新思维导图，纳入 GitHub MCP 注册表到案例研究部分
- <strong>案例研究描述</strong>：由通用描述提升为七个详尽案例的细分讲解
- <strong>仓库结构</strong>：更新第 10 部分，反映全面案例研究覆盖与具体实现细节
- <strong>变更日志整合</strong>：新增 2025 年 9 月 26 日条目，记录 GitHub MCP 注册表添加及案例研究增强
- <strong>日期更新</strong>：更新页脚时间戳以反映最新修订（2025 年 9 月 26 日）

### 文档质量改进
- <strong>一致性增强</strong>：统一所有七个案例的格式与结构
- <strong>全面覆盖</strong>：案例研究涵盖企业、开发者生产力及生态系统发展场景
- <strong>战略定位</strong>：增强 MCP 作为代理系统部署基础平台的关注
- <strong>资源整合</strong>：更新附加资源以包含 GitHub MCP 注册表链接

## 2025 年 9 月 15 日

### 高级主题扩展 - 自定义传输与上下文工程

#### MCP 自定义传输 (05-AdvancedTopics/mcp-transport/) - 新高级实现指南
- **README.md**：自定义 MCP 传输机制完整实现指南
  - **Azure 事件网格传输**：全面的无服务器事件驱动传输实现
    - 提供 C#、TypeScript 和 Python 示例，集成 Azure Functions
    - 事件驱动架构模式，实现可扩展 MCP 解决方案
    - Webhook 接收器及基于推送的消息处理
  - **Azure 事件中心传输**：高吞吐量流式传输实现
    - 适合低延迟场景的实时流处理能力
    - 分区策略及检查点管理
    - 消息批处理及性能优化
  - <strong>企业集成模式</strong>：生产就绪架构示例
    - 跨多个 Azure Functions 的分布式 MCP 处理
    - 结合多种传输类型的混合传输架构
    - 消息持久性、可靠性及错误处理策略
  - <strong>安全与监控</strong>：Azure Key Vault 集成及可观察性模式
    - 托管身份认证与最小权限访问
    - Application Insights 远程遥测和性能监控
    - 熔断器与容错模式
  - <strong>测试框架</strong>：自定义传输的全面测试策略
    - 使用测试替身和模拟框架的单元测试
    - 结合 Azure 测试容器的集成测试
    - 性能和负载测试考量

#### 上下文工程 (05-AdvancedTopics/mcp-contextengineering/) - 新兴的 AI 领域
- **README.md**：全面探讨上下文工程作为新兴领域
  - <strong>核心原则</strong>：完整上下文共享、动作决策知晓与上下文窗口管理

  - **MCP 协议对齐**：MCP 设计如何应对上下文工程挑战
    - 上下文窗口限制和渐进式加载策略
    - 相关性判断和动态上下文检索
    - 多模态上下文处理和安全考虑
  - <strong>实现方法</strong>：单线程与多代理架构
    - 上下文切片和优先级技术
    - 渐进式上下文加载和压缩策略
    - 分层上下文方法和检索优化
  - <strong>测量框架</strong>：评估上下文有效性的最新指标
    - 输入效率、性能、质量和用户体验考量
    - 上下文优化的实验方法
    - 失败分析和改进方法论

#### 课程导航更新 (README.md)
- <strong>模块结构增强</strong>：更新课程表以包含新的高级主题
  - 添加了上下文工程（5.14）和自定义传输（5.15）条目
  - 所有模块保持一致的格式和导航链接
  - 更新描述以反映当前内容范围

### 目录结构改进
- <strong>命名标准化</strong>：将“mcp transport”重命名为“mcp-transport”，与其他高级主题文件夹保持一致
- <strong>内容组织</strong>：所有 05-AdvancedTopics 文件夹遵循一致的命名模式（mcp-[topic]）

### 文档质量提升
- **MCP 规范对齐**：所有新内容均参考当前 MCP 规范 2025-06-18
- <strong>多语言示例</strong>：包含 C#、TypeScript 和 Python 的全面代码示例
- <strong>企业聚焦</strong>：贯穿生产就绪模式和 Azure 云集成
- <strong>可视化文档</strong>：使用 Mermaid 图表进行架构和流程可视化

## 2025年8月18日

### 文档全面更新 - MCP 2025-06-18 标准

#### MCP 安全最佳实践 (02-Security/) - 完全现代化
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：基于 MCP 规范 2025-06-18 完全重写
  - <strong>强制性要求</strong>：添加来自官方规范的明确 MUST/MUST NOT 要求，附带清晰视觉指示
  - **12 个核心安全实践**：从 15 条列表调整为全面安全领域
    - 令牌安全与认证，集成外部身份提供商
    - 会话管理与传输安全，包括加密要求
    - AI 特定威胁防护，集成 Microsoft Prompt Shields
    - 访问控制与权限，遵循最小权限原则
    - 内容安全与监控，集成 Azure 内容安全
    - 供应链安全，全面组件验证
    - OAuth 安全与“代理困惑”防范，采用 PKCE 实现
    - 事件响应与恢复，支持自动化能力
    - 合规与治理，符合监管要求
    - 高级安全控制，采用零信任架构
    - Microsoft 安全生态系统集成，提供综合解决方案
    - 持续安全演进，采用自适应实践
  - **Microsoft 安全解决方案**：加强对 Prompt Shields、Azure 内容安全、Entra ID 和 GitHub 高级安全的集成指导
  - <strong>实施资源</strong>：根据官方 MCP 文档、Microsoft 安全解决方案、安全标准和实施指南分类综合资源链接

#### 高级安全控制 (02-Security/) - 企业实施
- **MCP-SECURITY-CONTROLS-2025.md**：采用企业级安全框架全面重构
  - **9 大安全领域**：从基础控制扩展至详细企业框架
    - 高级身份验证与授权，集成 Microsoft Entra ID
    - 令牌安全与反透传控制，全面验证机制
    - 会话安全控制，防止劫持
    - AI 特定安全控制，防止提示注入与工具污染
    - 代理困惑攻击防范，使用 OAuth 代理安全机制
    - 工具执行安全，采用沙箱和隔离技术
    - 供应链安全控制，依赖关系验证
    - 监控与检测控制，集成 SIEM
    - 事件响应与恢复，具备自动化能力
  - <strong>实施示例</strong>：添加详细 YAML 配置块和代码示例
  - **Microsoft 解决方案集成**：覆盖 Azure 安全服务、GitHub 高级安全和企业身份管理

#### 高级主题安全 (05-AdvancedTopics/mcp-security/) - 生产就绪实现
- **README.md**：为企业安全实施完全重写
  - <strong>当前规范对齐</strong>：更新至 MCP 规范 2025-06-18，包含强制安全要求
  - <strong>增强身份验证</strong>：集成 Microsoft Entra ID，附带全面 .NET 和 Java Spring Security 示例
  - **AI 安全集成**：实现 Microsoft Prompt Shields 和 Azure 内容安全，包含详细 Python 示例
  - <strong>高级威胁缓解</strong>：提供全面实现示例，涵盖
    - 代理困惑攻击防范，使用 PKCE 和用户同意验证
    - 令牌透传防护，采用受众验证和安全令牌管理
    - 会话劫持防护，结合密码学绑定与行为分析
  - <strong>企业安全集成</strong>：Azure 应用洞察监控、威胁检测管线和供应链安全
  - <strong>实施清单</strong>：明确标识强制与推荐安全控制及 Microsoft 安全生态优势

### 文档质量与标准对齐
- <strong>规范引用</strong>：更新所有引用为当前 MCP 规范 2025-06-18
- **Microsoft 安全生态系统**：贯穿所有安全文档的集成指导增强
- <strong>实践实施</strong>：添加 .NET、Java 和 Python 的详细代码示例及企业模式
- <strong>资源组织</strong>：对官方文档、安全标准和实施指南进行全面分类
- <strong>视觉指示</strong>：清晰标明强制性要求与推荐实践


#### 核心概念 (01-CoreConcepts/) - 完全现代化
- <strong>协议版本更新</strong>：引用当前 MCP 规范 2025-06-18，采用基于日期的版本格式（YYYY-MM-DD）
- <strong>架构细化</strong>：增强 Hosts、Clients 和 Servers 描述，反映当前 MCP 架构模式
  - Hosts 现明确定义为协调多个 MCP 客户端连接的 AI 应用
  - Clients 描述为维持一对一服务器关系的协议连接器
  - Servers 增加本地与远程部署场景说明
- <strong>原语重构</strong>：对服务器与客户端原语进行全面重构
  - 服务器原语：资源（数据源）、提示（模板）、工具（可执行函数），附详细解释和示例
  - 客户端原语：采样（LLM 补全）、引导（用户输入）、日志（调试/监控）
  - 更新采用当前的发现（`*/list`）、检索（`*/get`）和执行（`*/call`）方法模式
- <strong>协议架构</strong>：引入两层架构模型
  - 数据层：基于 JSON-RPC 2.0，包含生命周期管理和原语
  - 传输层：本地 STDIO 与远程支持 SSE 的流式 HTTP 传输机制
- <strong>安全框架</strong>：全面安全原则，包括明确用户同意、数据隐私保护、工具执行安全和传输层安全
- <strong>通信模式</strong>：更新协议消息，展示初始化、发现、执行和通知流程
- <strong>代码示例</strong>：刷新多语言示例（.NET、Java、Python、JavaScript）以反映当前 MCP SDK 模式

#### 安全 (02-Security/) - 全面安全大修  
- <strong>标准对齐</strong>：完全符合 MCP 规范 2025-06-18 安全要求
- <strong>身份验证演进</strong>：记录从定制 OAuth 服务器到外部身份提供商委托的演变（Microsoft Entra ID）
- **AI 特定威胁分析**：增强现代 AI 攻击向量的覆盖
  - 详细提示注入攻击场景及真实示例
  - 工具污染机制和“割韭菜”攻击模式
  - 上下文窗口污染与模型混淆攻击
- **Microsoft AI 安全解决方案**：全面涵盖微软安全生态系统
  - AI Prompt Shields，具备高级检测、聚焦和定界技术
  - Azure 内容安全集成模式
  - GitHub 高级安全保护供应链
- <strong>高级威胁缓解</strong>：详细安全控制
  - 会话劫持，含 MCP 具体攻击场景和密码学会话 ID 要求
  - MCP 代理场景中的代理困惑问题，要求明确同意
  - 令牌透传漏洞，含强制验证控制
- <strong>供应链安全</strong>：扩展 AI 供应链覆盖，包括基础模型、嵌入服务、上下文提供者和第三方 API
- <strong>基础安全</strong>：增强企业安全模式集成，包括零信任架构和微软安全生态系统
- <strong>资源组织</strong>：根据类型分类综合资源链接（官方文档、标准、研究、微软解决方案、实施指南）

### 文档质量提升
- <strong>结构化学习目标</strong>：增强学习目标，确立具体可执行成果
- <strong>交叉引用</strong>：添加相关安全与核心概念主题间链接
- <strong>最新信息</strong>：更新所有日期引用和规范链接到当前标准
- <strong>实施指导</strong>：贯穿两部分添加具体可操作的实施指引

## 2025年7月16日

### README 和导航改进
- 彻底重新设计 README.md 中的课程导航
- 用更易访问的基于表格格式替代 `<details>` 标签
- 在新“alternative_layouts”文件夹中创建替代布局选项
- 添加卡片式、标签式和手风琴式导航示例
- 更新仓库结构章节，包含所有最新文件
- 增强“如何使用本课程”章节，提供清晰建议
- 更新 MCP 规范链接，指向正确的 URL
- 添加上下文工程部分（5.14）到课程结构

### 学习指南更新
- 完全修订学习指南以匹配当前仓库结构
- 新增 MCP 客户端与工具及流行 MCP 服务器章节
- 更新可视课程地图，准确反映所有主题
- 增强高级主题描述，涵盖所有专业领域
- 更新案例研究章节，反映实际示例
- 添加本综合变更日志

### 社区贡献 (06-CommunityContributions/)
- 添加有关 MCP 图像生成服务器的详细信息
- 增加全面的 Claude 在 VSCode 中使用章节
- 添加 Cline 终端客户端安装与使用说明
- 更新 MCP 客户端章节，包含所有流行客户端选项
- 增强贡献示例，提供更准确的代码样例

### 高级主题 (05-AdvancedTopics/)
- 组织所有专业主题文件夹，保持命名一致
- 添加上下文工程材料与示例
- 添加 Foundry 代理集成文档
- 增强 Entra ID 安全集成文档

## 2025年6月11日

### 初始创建
- 发布 MCP 初学者课程的第一个版本
- 创建全部 10 个主要部分的基础结构
- 实现可视课程地图用于导航
- 添加多种编程语言的初始示例项目

### 入门 (03-GettingStarted/)
- 创建第一个服务器实现示例
- 添加客户端开发指导
- 包含 LLM 客户端集成说明
- 添加 VS Code 集成文档
- 实现服务器推送事件（SSE）示例

### 核心概念 (01-CoreConcepts/)
- 添加客户端-服务器架构详细说明
- 创建关键协议组件文档
- 记录 MCP 中的消息模式

## 2025年5月23日

### 仓库结构
- 使用基础文件夹结构初始化仓库
- 为每个主要部分创建 README 文件
- 建立翻译基础设施
- 添加图像资源和图表

### 文档
- 创建初始 README.md，包含课程总览
- 添加行为守则 (CODE_OF_CONDUCT.md) 和安全 (SECURITY.md)
- 建立支持文档 (SUPPORT.md)，提供求助指南
- 创建初步学习指南结构

## 2025年4月15日

### 规划与框架
- MCP 初学者课程的初步规划
- 定义学习目标和目标受众
- 概述课程的 10 个章节结构
- 制定示例和案例研究的概念框架
- 创建关键概念的初始原型示例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->