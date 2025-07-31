<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-07-31T01:12:58+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "zh"
}
-->
# 使用 Visual Studio Code 的 AI Toolkit 扩展连接服务器

在构建 AI 代理时，不仅仅是生成智能的响应，还需要赋予代理执行操作的能力。这就是 Model Context Protocol (MCP) 的用武之地。MCP 使代理能够以一致的方式访问外部工具和服务。可以把它想象成给你的代理接入了一个它真正能用的工具箱。

假设你将一个代理连接到你的计算器 MCP 服务器。这样一来，代理只需接收到类似“47 乘以 89 等于多少？”的提示，就能执行数学运算，而无需硬编码逻辑或构建自定义 API。

## 概述

本课程将介绍如何通过 Visual Studio Code 的 [AI Toolkit](https://aka.ms/AIToolkit) 扩展，将计算器 MCP 服务器连接到代理，使其能够通过自然语言执行加法、减法、乘法和除法等数学运算。

AI Toolkit 是 Visual Studio Code 的一个强大扩展，能够简化代理的开发过程。AI 工程师可以轻松地开发和测试生成式 AI 模型，无论是在本地还是云端。该扩展支持目前大多数主流的生成式模型。

*注意*：AI Toolkit 当前支持 Python 和 TypeScript。

## 学习目标

完成本课程后，你将能够：

- 使用 AI Toolkit 消费 MCP 服务器。
- 配置代理，使其能够发现并使用 MCP 服务器提供的工具。
- 通过自然语言使用 MCP 工具。

## 方法

以下是我们需要采取的高层次步骤：

- 创建一个代理并定义其系统提示。
- 创建一个带有计算器工具的 MCP 服务器。
- 将 Agent Builder 连接到 MCP 服务器。
- 通过自然语言测试代理调用工具的能力。

很好，现在我们了解了流程，接下来让我们配置一个 AI 代理，通过 MCP 利用外部工具，增强其能力！

## 前置条件

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code 的 AI Toolkit](https://aka.ms/AIToolkit)

## 练习：连接服务器

> [!WARNING]
> macOS 用户注意：我们目前正在调查一个影响 macOS 上依赖项安装的问题。因此，macOS 用户暂时无法完成本教程。我们会在修复后更新说明。感谢你的耐心和理解！

在本练习中，你将使用 Visual Studio Code 的 AI Toolkit 构建、运行并增强一个带有 MCP 服务器工具的 AI 代理。

### -0- 预备步骤：将 OpenAI GPT-4o 模型添加到“我的模型”

本练习使用 **GPT-4o** 模型。在创建代理之前，应将该模型添加到 **我的模型**。

![Visual Studio Code 的 AI Toolkit 扩展中模型选择界面的截图。标题为“为你的 AI 解决方案找到合适的模型”，副标题鼓励用户发现、测试和部署 AI 模型。下方“热门模型”部分显示了六个模型卡片：DeepSeek-R1（GitHub 托管）、OpenAI GPT-4o、OpenAI GPT-4.1、OpenAI o1、Phi 4 Mini（CPU - 小型、快速）和 DeepSeek-R1（Ollama 托管）。每个卡片都包含“添加”或“在 Playground 中试用”的选项。](../../../../translated_images/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.zh.png)

1. 从 **活动栏** 打开 **AI Toolkit** 扩展。
2. 在 **目录** 部分，选择 **模型** 打开 **模型目录**。选择 **模型** 会在新的编辑器标签页中打开 **模型目录**。
3. 在 **模型目录** 的搜索栏中输入 **OpenAI GPT-4o**。
4. 点击 **+ 添加** 将模型添加到你的 **我的模型** 列表中。确保选择的是 **GitHub 托管** 的模型。
5. 在 **活动栏** 中确认 **OpenAI GPT-4o** 模型已出现在列表中。

### -1- 创建一个代理

**Agent (Prompt) Builder** 允许你创建并自定义自己的 AI 驱动代理。在本节中，你将创建一个新代理并分配一个模型来驱动对话。

![Visual Studio Code 的 AI Toolkit 扩展中“计算器代理”构建界面的截图。左侧面板中选择的模型是“OpenAI GPT-4o（通过 GitHub）”。系统提示为“你是一名大学教授，教授数学”，用户提示为“用简单的术语向我解释傅里叶方程”。其他选项包括添加工具、启用 MCP 服务器和选择结构化输出的按钮。底部有一个蓝色的“运行”按钮。右侧面板中，“从示例开始”下列出了三个示例代理：Web 开发者（带 MCP 服务器）、二年级简化器和梦境解释器，每个都有简短的功能描述。](../../../../translated_images/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.zh.png)

1. 从 **活动栏** 打开 **AI Toolkit** 扩展。
2. 在 **工具** 部分，选择 **Agent (Prompt) Builder**。选择 **Agent (Prompt) Builder** 会在新的编辑器标签页中打开 **Agent (Prompt) Builder**。
3. 点击 **+ 新建代理** 按钮。扩展会通过 **命令面板** 启动一个设置向导。
4. 输入名称 **Calculator Agent** 并按下 **Enter**。
5. 在 **Agent (Prompt) Builder** 中，为 **模型** 字段选择 **OpenAI GPT-4o（通过 GitHub）** 模型。

### -2- 为代理创建系统提示

在代理框架搭建完成后，是时候定义它的个性和用途了。在本节中，你将使用 **生成系统提示** 功能来描述代理的预期行为（例如一个计算器代理），并让模型为你生成系统提示。

![Visual Studio Code 的 AI Toolkit 中“计算器代理”界面的截图，显示了一个标题为“生成提示”的模态窗口。模态窗口解释了可以通过分享基本细节生成提示模板，并包含一个文本框，示例系统提示为：“你是一个乐于助人且高效的数学助手。当遇到涉及基本算术的问题时，你会给出正确的结果。”文本框下方有“关闭”和“生成”按钮。背景中可见部分代理配置，包括选定的模型“OpenAI GPT-4o（通过 GitHub）”以及系统和用户提示字段。](../../../../translated_images/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.zh.png)

1. 在 **提示** 部分，点击 **生成系统提示** 按钮。此按钮会打开提示生成器，利用 AI 为代理生成系统提示。
2. 在 **生成提示** 窗口中，输入以下内容：`你是一个乐于助人且高效的数学助手。当遇到涉及基本算术的问题时，你会给出正确的结果。`
3. 点击 **生成** 按钮。右下角会出现通知，确认系统提示正在生成。生成完成后，提示会出现在 **Agent (Prompt) Builder** 的 **系统提示** 字段中。
4. 审核 **系统提示** 并根据需要进行修改。

### -3- 创建 MCP 服务器

现在你已经定义了代理的系统提示（指导其行为和响应），接下来是为代理配备实际功能。在本节中，你将创建一个带有加法、减法、乘法和除法工具的计算器 MCP 服务器。这个服务器将使你的代理能够根据自然语言提示执行实时数学运算。

![Visual Studio Code 的 AI Toolkit 扩展中“计算器代理”界面下部的截图，显示了“工具”和“结构化输出”的可展开菜单，以及一个设置为“文本”的“选择输出格式”下拉菜单。在右侧，有一个标记为“+ MCP 服务器”的按钮，用于添加 Model Context Protocol 服务器。工具部分上方显示了一个图像图标占位符。](../../../../translated_images/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.zh.png)

AI Toolkit 提供了模板，方便你创建自己的 MCP 服务器。我们将使用 Python 模板来创建计算器 MCP 服务器。

*注意*：AI Toolkit 当前支持 Python 和 TypeScript。

1. 在 **Agent (Prompt) Builder** 的 **工具** 部分，点击 **+ MCP 服务器** 按钮。扩展会通过 **命令面板** 启动一个设置向导。
2. 选择 **+ 添加服务器**。
3. 选择 **创建一个新的 MCP 服务器**。
4. 选择 **python-weather** 作为模板。
5. 选择 **默认文件夹** 保存 MCP 服务器模板。
6. 输入以下服务器名称：**Calculator**
7. 一个新的 Visual Studio Code 窗口将打开。选择 **是，我信任作者**。
8. 使用终端（**终端** > **新终端**），创建一个虚拟环境：`python -m venv .venv`
9. 使用终端激活虚拟环境：
    - Windows - `.venv\Scripts\activate`
    - macOS/Linux - `source venv/bin/activate`
10. 使用终端安装依赖项：`pip install -e .[dev]`
11. 在 **活动栏** 的 **资源管理器** 视图中，展开 **src** 目录并选择 **server.py**，在编辑器中打开文件。
12. 将 **server.py** 文件中的代码替换为以下内容并保存：

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

### -4- 使用计算器 MCP 服务器运行代理

现在你的代理已经有了工具，是时候使用它们了！在本节中，你将向代理提交提示，以测试并验证代理是否正确调用了计算器 MCP 服务器中的工具。

![Visual Studio Code 的 AI Toolkit 扩展中“计算器代理”界面的截图。左侧面板中，“工具”下添加了一个名为 local-server-calculator_server 的 MCP 服务器，显示了四个可用工具：add、subtract、multiply 和 divide。一个徽章显示有四个工具处于活动状态。下方是一个折叠的“结构化输出”部分和一个蓝色的“运行”按钮。右侧面板中，“模型响应”下代理调用了 multiply 和 subtract 工具，输入分别为 {"a": 3, "b": 25} 和 {"a": 75, "b": 20}。最终的“工具响应”显示为 75.0。底部有一个“查看代码”按钮。](../../../../translated_images/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.zh.png)

你将在本地开发机器上通过 **Agent Builder** 运行计算器 MCP 服务器作为 MCP 客户端。

1. 按下 `F5` 启动 MCP 服务器的调试。**Agent (Prompt) Builder** 将在新的编辑器标签页中打开。服务器的状态可在终端中查看。
2. 在 **Agent (Prompt) Builder** 的 **用户提示** 字段中，输入以下提示：`我买了 3 件每件 25 美元的商品，然后用了 20 美元的折扣。我花了多少钱？`
3. 点击 **运行** 按钮生成代理的响应。
4. 查看代理输出。模型应得出你花了 **55 美元**。
5. 以下是应发生的过程：
    - 代理选择 **multiply** 和 **subtract** 工具来协助计算。
    - 为 **multiply** 工具分配相应的 `a` 和 `b` 值。
    - 为 **subtract** 工具分配相应的 `a` 和 `b` 值。
    - 每个工具的响应显示在各自的 **工具响应** 中。
    - 模型的最终输出显示在 **模型响应** 中。
6. 提交其他提示以进一步测试代理。你可以通过点击 **用户提示** 字段并替换现有提示来修改提示。
7. 测试完成后，可以通过 **终端** 输入 **CTRL/CMD+C** 停止服务器。

## 作业

尝试向你的 **server.py** 文件添加一个额外的工具条目（例如：返回一个数字的平方根）。提交需要代理使用新工具（或现有工具）的额外提示。确保重新启动服务器以加载新添加的工具。

## 解决方案

[解决方案](./solution/README.md)

## 关键要点

本章的关键要点如下：

- AI Toolkit 扩展是一个很棒的客户端，可以消费 MCP 服务器及其工具。
- 你可以向 MCP 服务器添加新工具，扩展代理的能力以满足不断变化的需求。
- AI Toolkit 包含模板（例如 Python MCP 服务器模板），简化了自定义工具的创建。

## 其他资源

- [AI Toolkit 文档](https://aka.ms/AIToolkit/doc)

## 下一步
- 下一步：[测试与调试](../08-testing/README.md)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。