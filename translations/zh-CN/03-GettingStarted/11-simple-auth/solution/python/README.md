# 运行示例

## 创建环境

```sh
python -m venv venv
source ./venv/bin/activate
```

## 安装依赖

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## 生成令牌

您需要生成一个令牌，供客户端与服务器通信使用。

调用：

```sh
python util.py
```

## 运行代码

运行代码：

```sh
python server.py
```

在另一个终端中输入：

```sh
python client.py
```

在服务器终端中，您应该会看到类似以下内容：

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

在客户端窗口中，您应该会看到类似以下的文本：

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

这表示一切正常运行。

### 修改信息以查看失败情况

在 *server.py* 文件中找到以下代码：

```python
 if not has_scope(has_header, "Admin.Write"):
```

将其修改为 "User.Write"。当前令牌没有该权限级别，因此如果您重新启动服务器并再次尝试运行客户端，您应该会在服务器终端中看到类似以下的错误：

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

您可以选择将服务器代码改回原样，或者生成一个包含额外权限范围的新令牌，取决于您的需求。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。