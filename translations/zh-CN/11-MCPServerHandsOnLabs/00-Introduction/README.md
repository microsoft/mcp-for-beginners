# MCP 数据库集成简介

> [!NOTE]
> 本学习路径中的图表或代码使用 HTTP/SSE 或初始化选项反映了示例的 MCP `2025-11-25` 依赖关系。对于新实现，请使用 `2026-07-28` 无状态请求和可流式 HTTP。
> 
> 

## 🎯 本实验涵盖内容

本简介实验全面概述了构建带有数据库集成的模型上下文协议（MCP）服务器。您将通过 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 中的 Zava Retail 零售分析用例，了解业务背景、技术架构及实际应用。

## 概述

**模型上下文协议（MCP）** 使 AI 助手能够安全地实时访问并与外部数据源交互。结合数据库集成，MCP 激发了数据驱动 AI 应用的强大能力。

本学习路径教您构建面向生产的 MCP 服务器，通过 PostgreSQL 连接 AI 助手和零售销售数据，实施企业级方案如行级安全、语义搜索和多租户数据访问。

## 学习目标

完成本实验后，您将能够：

- <strong>定义</strong> 模型上下文协议及其数据库集成的核心优势
- <strong>识别</strong> 具有数据库的 MCP 服务器架构关键组件
- <strong>理解</strong> Zava Retail 用例及其业务需求
- <strong>认识</strong> 用于安全、可扩展数据库访问的企业模式
- <strong>列举</strong> 本学习路径中使用的工具和技术

## 🧭 挑战：AI 遇见真实世界数据

### 传统 AI 的局限

现代 AI 助手极为强大，但在处理现实业务数据时面临显著限制：

| <strong>挑战</strong> | <strong>描述</strong> | <strong>业务影响</strong> |
|---------------|-----------------|-------------------|
| <strong>静态知识</strong> | AI 模型基于固定数据集训练，无法访问当前业务数据 | 洞察过时，错失机会 |
| <strong>数据孤岛</strong> | 信息被锁定在数据库、API 和系统中，AI 无法触及 | 分析不全，工作流程碎片化 |
| <strong>安全约束</strong> | 直接数据库访问带来安全和合规风险 | 部署受限，需手动准备数据 |
| <strong>复杂查询</strong> | 业务用户需技术知识来挖掘数据洞察 | 采用度降低，流程低效 |

### MCP 解决方案

模型上下文协议通过提供下列功能解决这些挑战：

- <strong>实时数据访问</strong>：AI 助手查询实时数据库和 API
- <strong>安全集成</strong>：受控访问，带认证和权限
- <strong>自然语言接口</strong>：业务用户用普通英语提问
- <strong>标准化协议</strong>：跨不同 AI 平台和工具通用

## 🏪 认识 Zava Retail：我们的学习案例 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

在本学习路径中，我们将为 **Zava Retail** 构建 MCP 服务器，这是一家拥有多门店的虚构 DIY 零售连锁。此现实场景演示了企业级 MCP 实现。

### 业务背景

**Zava Retail** 运营：
- **华盛顿州 8 家实体店**（西雅图、贝尔维尤、塔科马、斯波坎、埃弗雷特、雷德蒙德、柯克兰）
- **1 家在线商店**，支持电商销售
- <strong>丰富产品目录</strong>，包括工具、五金、园艺用品和建筑材料
- <strong>多层级管理</strong>，有店长、区域经理及高管

### 业务需求

店长和高管需要 AI 驱动的分析以：

1. <strong>分析各店及时间段销售表现</strong>
2. **跟踪库存水平，识别补货需求**
3. <strong>理解客户行为和购买模式</strong>
4. <strong>通过语义搜索发现产品洞察</strong>
5. <strong>使用自然语言查询生成报表</strong>
6. <strong>通过基于角色的访问控制维护数据安全</strong>

### 技术需求

MCP 服务器必须提供：

- <strong>多租户数据访问</strong>，店长只能看到所属门店数据
- <strong>灵活查询</strong>，支持复杂 SQL 操作
- <strong>语义搜索</strong>，用于产品发现和推荐
- <strong>实时数据</strong>，反映业务最新状态
- <strong>安全认证</strong>，实现行级安全
- <strong>可扩展架构</strong>，支持多用户并发访问

## 🏗️ MCP 服务器架构概述

我们的 MCP 服务器实现了针对数据库集成优化的分层架构：

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### 关键组件

#### **1. MCP 服务器层**
- **FastMCP 框架**：现代 Python MCP 服务器实现
- <strong>工具注册</strong>：声明式工具定义及类型安全
- <strong>请求上下文</strong>：用户身份及会话管理
- <strong>错误处理</strong>：健壮的错误管理与日志记录

#### **2. 数据库集成层**
- <strong>连接池</strong>：高效的 asyncpg 连接管理
- <strong>架构提供者</strong>：动态表结构发现
- <strong>查询执行器</strong>：带 RLS 上下文的安全 SQL 执行
- <strong>事务管理</strong>：ACID 合规与回滚处理

#### **3. 安全层**
- <strong>行级安全</strong>：PostgreSQL RLS 实现多租户数据隔离
- <strong>用户身份</strong>：店长身份认证与授权
- <strong>访问控制</strong>：细粒度权限和审计追踪
- <strong>输入验证</strong>：防止 SQL 注入及查询验证

#### **4. AI 增强层**
- <strong>语义搜索</strong>：基于向量嵌入的产品发现
- **Azure OpenAI 集成**：文本嵌入生成
- <strong>相似度算法</strong>：pgvector 余弦相似度搜索
- <strong>搜索优化</strong>：索引和性能调优

## 🔧 技术栈

### 核心技术

| <strong>组件</strong> | <strong>技术</strong> | <strong>用途</strong> |
|---------------|----------------|-------------|
| **MCP 框架** | FastMCP（Python） | 现代 MCP 服务器实现 |
| <strong>数据库</strong> | PostgreSQL 17 + pgvector | 关系数据与向量搜索 |
| **AI 服务** | Azure OpenAI | 文本嵌入和语言模型 |
| <strong>容器化</strong> | Docker + Docker Compose | 开发环境 |
| <strong>云平台</strong> | Microsoft Azure | 生产环境部署 |
| **IDE 集成** | VS Code | AI 聊天与开发工作流 |

### 开发工具

| <strong>工具</strong> | <strong>用途</strong> |
|----------|-------------|
| **asyncpg** | 高性能 PostgreSQL 驱动 |
| **Pydantic** | 数据验证与序列化 |
| **Azure SDK** | 云服务集成 |
| **pytest** | 测试框架 |
| **Docker** | 容器化与部署 |

### 生产环境栈

| <strong>服务</strong> | **Azure 资源** | <strong>用途</strong> |
|-------------|-------------------|-------------|
| <strong>数据库</strong> | Azure Database for PostgreSQL | 托管数据库服务 |
| <strong>容器</strong> | Azure Container Apps | 无服务器容器托管 |
| **AI 服务** | Microsoft Foundry | OpenAI 模型与端点 |
| <strong>监控</strong> | Application Insights | 可观察性与诊断 |
| <strong>安全</strong> | Azure Key Vault | 密钥和配置管理 |

## 🎬 真实使用场景

让我们看看不同用户如何与 MCP 服务器交互：

### 场景 1：店长业绩回顾

<strong>用户</strong>：Sarah，西雅图店店长  
<strong>目标</strong>：分析上季度销售业绩

<strong>自然语言查询</strong>：
> “展示我店 2024 年第四季度按收入排行前 10 的产品”

<strong>发生了什么</strong>：
1. VS Code AI 聊天将查询发送至 MCP 服务器
2. MCP 服务器识别 Sarah 的门店上下文（西雅图）
3. RLS 策略筛选仅西雅图门店数据
4. 生成并执行 SQL 查询
5. 结果格式化后返回 AI 聊天
6. AI 提供分析与洞察

### 场景 2：语义搜索产品发现

<strong>用户</strong>：Mike，库存经理  
<strong>目标</strong>：查找与客户需求相似的产品

<strong>自然语言查询</strong>：
> “我们销售哪些产品类似于‘户外用防水电连接器’？”

<strong>发生了什么</strong>：
1. 查询由语义搜索工具处理
2. Azure OpenAI 生成嵌入向量
3. pgvector 进行相似度搜索
4. 相关产品按相关度排序
5. 结果包含产品详情及库存状况
6. AI 推荐替代品和组合购买方案

### 场景 3：跨门店分析

<strong>用户</strong>：Jennifer，区域经理  
<strong>目标</strong>：比较所有门店绩效

<strong>自然语言查询</strong>：
> “比较所有门店过去 6 个月的分类销售额”

<strong>发生了什么</strong>：
1. RLS 上下文设置为区域经理访问权限
2. 生成复杂跨门店查询
3. 汇总各门店数据
4. 结果包含趋势和对比
5. AI 识别洞察并给出建议

## 🔒 安全与多租户深度解析

我们的实现优先满足企业级安全要求：

### 行级安全（RLS）

PostgreSQL RLS 确保数据隔离：

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### 用户身份管理

每个 MCP 连接包含：
- **店长 ID**：RLS 上下文唯一标识符
- <strong>角色分配</strong>：权限和访问级别
- <strong>会话管理</strong>：安全认证令牌
- <strong>审计日志</strong>：完整访问历史

### 数据保护

多层安全措施：
- <strong>连接加密</strong>：所有数据库连接使用 TLS
- **防止 SQL 注入**：仅参数化查询
- <strong>输入验证</strong>：全面请求验证
- <strong>错误处理</strong>：错误信息不泄露敏感数据

## 🎯 关键要点总结

完成本介绍后，您应理解：

✅ **MCP 价值主张**：MCP 如何桥接 AI 助手与真实世界数据  
✅ <strong>业务背景</strong>：Zava Retail 的需求和挑战  
✅ <strong>架构概述</strong>：关键组件及其交互  
✅ <strong>技术栈</strong>：贯穿全过程的工具和框架  
✅ <strong>安全模型</strong>：多租户数据访问和保护  
✅ <strong>使用模式</strong>：真实查询场景和工作流程  

## 🚀 接下来做什么

准备深入了解？请继续学习：

**[实验 01：核心架构概念](../01-Architecture/README.md)**

学习 MCP 服务器架构模式、数据库设计原则，以及驱动我们零售分析解决方案的详细技术实现。

## 📚 附加资源

### MCP 文档
- [MCP 规范](https://modelcontextprotocol.io/docs/) - 官方协议文档
- [MCP 入门](https://aka.ms/mcp-for-beginners) - 全面 MCP 学习指南
- [FastMCP 文档](https://github.com/modelcontextprotocol/python-sdk) - Python SDK 文档

### 数据库集成
- [PostgreSQL 文档](https://www.postgresql.org/docs/) - 完整 PostgreSQL 参考资料
- [pgvector 指南](https://github.com/pgvector/pgvector) - 向量扩展文档
- [行级安全](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS 指南

### Azure 服务
- [Azure OpenAI 文档](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 服务集成
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - 托管数据库服务
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - 无服务器容器

---

<strong>免责声明</strong>：本示例使用虚构零售数据作为学习练习。实际生产环境中请务必遵循贵组织的数据治理和安全政策。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->