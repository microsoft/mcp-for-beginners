# Basic Calculator MCP Service

该服务通过 Model Context Protocol (MCP) 提供基本的计算器操作。它设计为一个简单的示例，适合初学者了解 MCP 的实现。

更多信息，请参见 [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## 功能

该计算器服务提供以下功能：

1. **基本算术运算**：
   - 两数相加
   - 一个数减去另一个数
   - 两数相乘
   - 一个数除以另一个数（带零除检查）

## 使用 `stdio` 类型

## 配置

1. **配置 MCP 服务器**：
   - 在 VS Code 中打开你的工作区。
   - 在工作区文件夹中创建 `.vscode/mcp.json` 文件以配置 MCP 服务器。示例配置：

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - 系统会要求你输入 GitHub 仓库根目录，可以通过命令 `git rev-parse --show-toplevel` 获取。

## 使用该服务

该服务通过 MCP 协议暴露以下 API 端点：

- `add(a, b)`：将两个数字相加
- `subtract(a, b)`：用第一个数字减去第二个数字
- `multiply(a, b)`：将两个数字相乘
- `divide(a, b)`：用第一个数字除以第二个数字（带零检查）
- isPrime(n)：检查一个数字是否为质数

## 在 VS Code 中使用 Github Copilot Chat 测试

1. 尝试使用 MCP 协议向服务发起请求。例如，你可以问：
   - “Add 5 and 3”
   - “Subtract 10 from 4”
   - “Multiply 6 and 7”
   - “Divide 8 by 2”
   - “Does 37854 prime?”
   - “What are the 3 prime numbers before after 4242?”
2. 为确保使用了工具，在提示中添加 #MyCalculator。例如：
   - “Add 5 and 3 #MyCalculator”
   - “Subtract 10 from 4 #MyCalculator”

## 容器化版本

当你安装了 .NET SDK 并且所有依赖都已就绪时，之前的方案非常适用。但如果你想分享该方案或在不同环境中运行，可以使用容器化版本。

1. 启动 Docker 并确保其正在运行。
1. 在终端中，切换到文件夹 `03-GettingStarted\samples\csharp\src`
1. 构建计算器服务的 Docker 镜像，执行以下命令（将 `<YOUR-DOCKER-USERNAME>` 替换为你的 Docker Hub 用户名）：
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. 镜像构建完成后，上传到 Docker Hub。运行以下命令：
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## 使用 Docker 版本

1. 在 `.vscode/mcp.json` 文件中，将服务器配置替换为以下内容：
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   从配置中可以看到，命令是 `docker`，参数是 `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`。`--rm` 标志确保容器停止后被删除，`-i` 标志允许你与容器的标准输入交互。最后一个参数是我们刚刚构建并推送到 Docker Hub 的镜像名称。

## 测试 Docker 版本

点击 `"mcp-calc": {` 上方的小启动按钮启动 MCP 服务器，和之前一样，你可以让计算器服务帮你做一些数学运算。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。