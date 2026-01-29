# 运行示例

## 安装依赖

```sh
npm install
```

## 运行代码

```sh
npm run build
```

```sh
npm start
```

你应该会看到类似以下的输出：

```text
JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlVzZXIgdXNlcnNzb24iLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNzU5MTY4NzIyLCJleHAiOjE3NTkxNzIzMjJ9.JAMGCX_sHdqHzsKqqg6jHFUGk6zYZB7N77mWDqcRMcY
Decoded Payload: {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: 1759168722,
  exp: 1759172322
```

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。