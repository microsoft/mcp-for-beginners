# 🐙 模块 4：实用 MCP 开发 - 自定义 GitHub 克隆服务器

![Duration](https://img.shields.io/badge/Duration-30_minutes-blue?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-Custom%20Server-purple?style=flat-square&logo=github)
![VS Code](https://img.shields.io/badge/VS%20Code-Integration-blue?style=flat-square&logo=visualstudiocode)
![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Agent%20Mode-green?style=flat-square&logo=github)

> **⚡ 快速开始：** 只需30分钟，构建一个生产级的 MCP 服务器，实现 GitHub 仓库克隆和 VS Code 集成的自动化！

## 🎯 学习目标

完成本实验后，您将能够：

- ✅ 创建适用于真实开发流程的自定义 MCP 服务器
- ✅ 通过 MCP 实现 GitHub 仓库克隆功能
- ✅ 将自定义 MCP 服务器与 VS Code 和 Agent Builder 集成
- ✅ 使用 GitHub Copilot Agent 模式配合自定义 MCP 工具
- ✅ 在生产环境中测试和部署自定义 MCP 服务器

## 📋 先决条件

- 完成实验 1-3（MCP 基础和高级开发）
- 拥有 GitHub Copilot 订阅（[免费注册](https://github.com/github-copilot/signup)）
- 安装了带有 AI Toolkit 和 GitHub Copilot 扩展的 VS Code
- 安装并配置好 Git CLI

## 🏗️ 项目概述

### **真实开发挑战**
作为开发者，我们经常使用 GitHub 克隆仓库并在 VS Code 或 VS Code Insiders 中打开。这个手动流程包括：
1. 打开终端/命令提示符
2. 切换到目标目录
3. 执行 `git clone` 命令
4. 在克隆的目录中打开 VS Code

**我们的 MCP 解决方案将这一流程简化为一个智能命令！**

### **你将构建的内容**
一个 **GitHub 克隆 MCP 服务器**（`git_mcp_server`），具备以下功能：

| 功能 | 描述 | 优势 |
|---------|-------------|---------|
| 🔄 **智能仓库克隆** | 验证后克隆 GitHub 仓库 | 自动错误检查 |
| 📁 **智能目录管理** | 安全检查并创建目录 | 防止覆盖已有内容 |
| 🚀 **跨平台 VS Code 集成** | 在 VS Code/Insiders 中打开项目 | 流程无缝衔接 |
| 🛡️ **强健的错误处理** | 处理网络、权限和路径问题 | 生产环境级别的可靠性 |

---

## 📖 逐步实现

### 第 1 步：在 Agent Builder 中创建 GitHub Agent

1. 通过 AI Toolkit 扩展启动 Agent Builder
2. 使用以下配置创建新 agent：
   ```
   Agent Name: GitHubAgent
   ```

3. 初始化自定义 MCP 服务器：
   - 进入 **工具** → **添加工具** → **MCP 服务器**
   - 选择 **“创建新的 MCP 服务器”**
   - 选择 **Python 模板** 以获得最大灵活性
   - **服务器名称：** `git_mcp_server`

### 第 2 步：配置 GitHub Copilot Agent 模式

1. 在 VS Code 中打开 GitHub Copilot（Ctrl/Cmd + Shift + P → “GitHub Copilot: Open”）
2. 在 Copilot 界面选择 Agent 模型
3. 选择 **Claude 3.7 模型**，以增强推理能力
4. 启用 MCP 集成以访问工具

> **💡 专业提示：** Claude 3.7 对开发流程和错误处理模式有更深刻的理解。

### 第 3 步：实现核心 MCP 服务器功能

**使用以下详细提示配合 GitHub Copilot Agent 模式：**

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

### 第 4 步：测试你的 MCP 服务器

#### 4a. 在 Agent Builder 中测试

1. 启动 Agent Builder 的调试配置
2. 使用以下系统提示配置你的 agent：

```
SYSTEM_PROMPT:
You are my intelligent coding repository assistant. You help developers efficiently clone GitHub repositories and set up their development environment. Always provide clear feedback about operations and handle errors gracefully.
```

3. 使用真实用户场景进行测试：

```
USER_PROMPT EXAMPLES:

Scenario : Basic Clone and Open
"Clone {Your GitHub Repo link such as https://github.com/kinfey/GHCAgentWorkshop
 } and save to {The global path you specify}, then open it with VS Code Insiders"
```

![Agent Builder Testing](../../../../translated_images/zh-CN/DebugAgent.81d152370c503241b3b39a251b8966f7f739286df19dd57f9147f6402214a012.png)

**预期结果：**
- ✅ 成功克隆并确认路径
- ✅ 自动启动 VS Code
- ✅ 对无效场景给出清晰错误信息
- ✅ 正确处理边缘情况

#### 4b. 在 MCP Inspector 中测试

![MCP Inspector Testing](../../../../translated_images/zh-CN/DebugInspector.eb5c95f94c69a8ba36944941b9a3588309a3a2fae101ace470ee09bde41d1667.png)

---

**🎉 恭喜！** 你已成功创建了一个实用且生产级的 MCP 服务器，解决了真实开发流程中的难题。你的自定义 GitHub 克隆服务器展示了 MCP 在自动化和提升开发者效率方面的强大能力。

### 🏆 成就解锁：
- ✅ **MCP 开发者** - 创建了自定义 MCP 服务器
- ✅ **流程自动化专家** - 优化了开发流程  
- ✅ **集成专家** - 连接了多种开发工具
- ✅ **生产就绪** - 构建了可部署的解决方案

---

## 🎓 研讨会完成：你的 Model Context Protocol 之旅

**亲爱的研讨会参与者，**

恭喜你完成了 Model Context Protocol 研讨会的全部四个模块！你已经从理解 AI Toolkit 基础知识，成长为能够构建生产级 MCP 服务器，解决真实开发挑战的开发者。

### 🚀 你的学习路径回顾：

**[模块 1](../lab1/README.md)**：你从探索 AI Toolkit 基础、模型测试和创建第一个 AI agent 开始。

**[模块 2](../lab2/README.md)**：你学习了 MCP 架构，集成了 Playwright MCP，并构建了第一个浏览器自动化 agent。

**[模块 3](../lab3/README.md)**：你进阶到自定义 MCP 服务器开发，完成了天气 MCP 服务器，并掌握了调试工具。

**[模块 4](../lab4/README.md)**：你将所学应用于创建实用的 GitHub 仓库工作流自动化工具。

### 🌟 你已掌握：

- ✅ **AI Toolkit 生态系统**：模型、agent 和集成模式
- ✅ **MCP 架构**：客户端-服务器设计、传输协议和安全性
- ✅ **开发者工具**：从 Playground 到 Inspector 再到生产部署
- ✅ **自定义开发**：构建、测试和部署自有 MCP 服务器
- ✅ **实用应用**：用 AI 解决真实工作流难题

### 🔮 你的下一步：

1. **构建你自己的 MCP 服务器**：运用所学自动化你的专属工作流
2. **加入 MCP 社区**：分享你的作品，向他人学习
3. **探索高级集成**：将 MCP 服务器连接到企业系统
4. **贡献开源**：帮助改进 MCP 工具和文档

请记住，这个研讨会只是开始。Model Context Protocol 生态系统正在快速发展，你已具备站在 AI 驱动开发工具前沿的能力。

**感谢你的参与和学习热情！**

希望本次研讨会激发了你改变开发方式、与 AI 工具互动的新思路。

**祝编码愉快！**

---

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。