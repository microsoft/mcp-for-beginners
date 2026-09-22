# 🚀 带 PostgreSQL 的 MCP 服务器 - 完整学习指南

## 🧠 MCP 数据库集成学习路径概述

本综合学习指南通过实际零售分析实现，教您如何构建可投入生产的<strong>模型上下文协议（MCP）服务器</strong>，并与数据库集成。您将学习企业级模式，包括<strong>行级安全（RLS）</strong>、<strong>语义搜索</strong>、<strong>Azure AI 集成</strong>以及<strong>多租户数据访问</strong>。

无论您是后端开发人员、AI 工程师还是数据架构师，本指南均提供结构化学习和真实示例及动手练习，带您逐步了解以下 MCP 服务器 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail。

## 🔗 官方 MCP 资源

- 📘 [MCP 文档](https://modelcontextprotocol.io/) – 详细教程和用户指南
- 📜 [MCP 规范（2026-07-28）](https://modelcontextprotocol.io/specification/2026-07-28/) – 协议架构和技术参考
- 🧑‍💻 [MCP GitHub 仓库](https://github.com/modelcontextprotocol) – 开源 SDK、工具和代码示例
- 🌐 [MCP 社区](https://github.com/orgs/modelcontextprotocol/discussions) – 加入讨论并贡献社区
- 🔒 [OWASP MCP 前十](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – 安全最佳实践和风险缓解


## 🧭 MCP 数据库集成学习路径

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 完整学习结构

| 实验室 | 主题 | 描述 | 链接 |
|--------|-------|-------------|------|
| **实验室 1-3：基础** | | | |
| 00 | [MCP 数据库集成介绍](./00-Introduction/README.md) | MCP 与数据库集成及零售分析用例概述 | [开始这里](./00-Introduction/README.md) |
| 01 | [核心架构概念](./01-Architecture/README.md) | 理解 MCP 服务器架构、数据库层及安全模式 | [学习](./01-Architecture/README.md) |
| 02 | [安全及多租户](./02-Security/README.md) | 行级安全、认证及多租户数据访问 | [学习](./02-Security/README.md) |
| 03 | [环境设置](./03-Setup/README.md) | 搭建开发环境，Docker，Azure 资源 | [设置](./03-Setup/README.md) |
| **实验室 4-6：构建 MCP 服务器** | | | |
| 04 | [数据库设计与模式](./04-Database/README.md) | PostgreSQL 设置，零售模式设计及示例数据 | [构建](./04-Database/README.md) |
| 05 | [MCP 服务器实现](./05-MCP-Server/README.md) | 构建带数据库集成的 FastMCP 服务器 | [构建](./05-MCP-Server/README.md) |
| 06 | [工具开发](./06-Tools/README.md) | 创建数据库查询工具和模式检测 | [构建](./06-Tools/README.md) |
| **实验室 7-9：高级功能** | | | |
| 07 | [语义搜索集成](./07-Semantic-Search/README.md) | 使用 Azure OpenAI 和 pgvector 实现向量嵌入 | [进阶](./07-Semantic-Search/README.md) |
| 08 | [测试与调试](./08-Testing/README.md) | 测试策略、调试工具和验证方法 | [测试](./08-Testing/README.md) |
| 09 | [VS Code 集成](./09-VS-Code/README.md) | 配置 VS Code MCP 集成及 AI 聊天用法 | [集成](./09-VS-Code/README.md) |
| **实验室 10-12：生产及最佳实践** | | | |
| 10 | [部署策略](./10-Deployment/README.md) | Docker 部署、Azure 容器应用及扩展考量 | [部署](./10-Deployment/README.md) |
| 11 | [监控与可观测性](./11-Monitoring/README.md) | Application Insights、日志和性能监控 | [监控](./11-Monitoring/README.md) |
| 12 | [最佳实践与优化](./12-Best-Practices/README.md) | 性能优化、安全加固及生产环境建议 | [优化](./12-Best-Practices/README.md) |

### 💻 您将构建的内容

完成本学习路径后，您将构建完整的 **Zava 零售分析 MCP 服务器**，功能包括：

- <strong>多表零售数据库</strong>，含客户订单、产品和库存
- 基于门店的 <strong>行级安全</strong> 实现数据隔离
- 使用 Azure OpenAI 嵌入实现的 <strong>语义产品搜索</strong>
- 集成 **VS Code AI 聊天**，支持自然语言查询
- 支持 <strong>生产部署</strong>，通过 Docker 和 Azure
- 使用 Application Insights 实现 <strong>全面监控</strong>

## 🎯 学习前提

为了最大化学习效果，您应具备：

- <strong>编程经验</strong>：熟悉 Python（优先）或类似语言
- <strong>数据库知识</strong>：了解 SQL 和关系型数据库基础
- **API 概念**：理解 REST API 和 HTTP 原理
- <strong>开发工具</strong>：熟练使用命令行、Git 和代码编辑器
- <strong>云基础</strong>：（可选）了解 Azure 或类似云平台基础知识
- **Docker 熟悉度**：（可选）理解容器化相关概念

### 必备工具

- **Docker Desktop** - 用于运行 PostgreSQL 和 MCP 服务器
- **Azure CLI** - 用于云资源部署
- **VS Code** - 用于开发和 MCP 集成
- **Git** - 用于版本控制
- **Python 3.8+** - 用于 MCP 服务器开发

## 📚 学习指南与资源

本学习路径提供丰富资源，帮助您高效学习：

### 学习指南

每个实验室包含：
- <strong>明确学习目标</strong> - 您将达成的成果
- <strong>分步骤指导</strong> - 详细实施教程
- <strong>代码示例</strong> - 可运行示范及解析
- <strong>练习题</strong> - 动手实践机会
- <strong>故障排查指南</strong> - 常见问题及解决方案
- <strong>附加资源</strong> - 拓展阅读和探索

### 前提检查

每个实验室开始前，包含：
- <strong>所需知识</strong> - 需要预先了解的内容
- <strong>环境验证</strong> - 如何确认环境搭建正确
- <strong>时间估计</strong> - 预计完成时长
- <strong>学习成果</strong> - 完成后掌握的技能

### 推荐学习路线

根据经验水平选择您的路径：

#### 🟢 <strong>初学者路径</strong>（MCP 新手）
1. 确保先完成 [MCP 初学者](https://aka.ms/mcp-for-beginners) 的 0-10 课程
2. 完成实验室 00-03，强化基础理解
3. 按照实验室 04-06 进行动手构建
4. 试试实验室 07-09，学习实际应用

#### 🟡 <strong>中级路径</strong>（有 MCP 经验）
1. 回顾实验室 00-01，数据库相关概念
2. 聚焦实验室 02-06，进行实现
3. 深入实验室 07-12，掌握高级功能

#### 🔴 <strong>高级路径</strong>（MCP 经验丰富）
1. 浏览实验室 00-03 获取背景信息
2. 聚焦实验室 04-09，数据库集成
3. 专注实验室 10-12，生产部署

## 🛠️ 如何高效使用本学习路径

### 顺序学习（推荐）

按顺序完成实验室，全面掌握：

1. <strong>阅读概览</strong> - 了解学习内容
2. <strong>检查前提</strong> - 确认基础知识
3. <strong>跟随步骤指导</strong> - 边学边做
4. <strong>完成练习</strong> - 加深理解
5. <strong>回顾重点</strong> - 巩固成果

### 目标学习

如果您需要特定技能：

- <strong>数据库集成</strong>：重点实验室 04-06
- <strong>安全实现</strong>：关注实验室 02、08、12
- **AI/语义搜索**：深入实验室 07
- <strong>生产部署</strong>：学习实验室 10-12

### 动手实践

每个实验室包含：
- <strong>操作代码示例</strong> - 复制、修改和试验
- <strong>真实场景</strong> - 实际零售分析用例
- <strong>逐步递进难度</strong> - 由浅入深构建项目
- <strong>验证步骤</strong> - 确认实现有效

## 🌟 社区与支持

### 获取帮助

- **Azure AI Discord**：[加入专家支持](https://discord.com/invite/ByRwuEEgH4)
- **GitHub 仓库和示例**：[部署示例和资源](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP 社区**：[加入更广泛的 MCP 讨论](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 准备好开始了吗？

立即开始您的旅程，点击 **[实验室 00：MCP 数据库集成介绍](./00-Introduction/README.md)**

---

*通过本综合且动手的学习体验，掌握构建具备数据库集成的生产级 MCP 服务器的技能。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->