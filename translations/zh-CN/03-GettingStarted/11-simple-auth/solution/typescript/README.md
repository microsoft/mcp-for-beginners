# 运行示例

## 安装依赖

```sh
npm install
```

## 构建

```sh
npm run build
```

## 生成令牌

```sh
npm run generate
```

这会在文件 *.env* 中创建一个令牌。客户端将从该文件中读取。

## 运行代码

启动服务器：

```sh
npm start
```

在另一个终端中运行客户端：

```sh
npm run client
```

在服务器的终端中，你应该看到类似以下的输出：

```text
User exists
User has required scopes
Middleware executed
```

而在客户端终端中，你应该看到类似以下的输出：

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### 修改内容

让我们确保理解权限范围。找到文件 *server.ts* 和以下代码：

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

这表示传递的令牌需要具有 "User.Read" 权限，我们将其更改为 "User.Write"。然后运行 `npm run build` 并重新启动服务器 `npm start`。你现在应该看到认证失败，因为我们没有这个权限范围（我们有 User.Read 和 Admin.Write）：

客户端现在显示

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

你可以在服务器终端中看到它显示：

```text
User exists
```

并且它不会继续执行。

可以选择添加权限范围 "User.Write"，然后运行 `npm run generate` 并重新运行客户端，或者将服务器代码改回原样。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。