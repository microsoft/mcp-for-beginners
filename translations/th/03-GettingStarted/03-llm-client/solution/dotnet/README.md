# รันตัวอย่างนี้

> [!NOTE]
> ตัวอย่างนี้สมมติว่าคุณกำลังใช้ GitHub Codespaces หากต้องการรันแบบโลคอล คุณต้องตั้งค่า personal access token (PAT) บน GitHub
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## ติดตั้งไลบรารี

```sh
dotnet restore
```

ควรติดตั้งไลบรารีดังต่อไปนี้: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## รัน

```sh 
dotnet run
```

คุณควรเห็นผลลัพธ์ประมาณนี้:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

ผลลัพธ์ส่วนใหญ่เป็นการดีบัก แต่สิ่งสำคัญคือคุณกำลังแสดงรายการเครื่องมือจาก MCP Server แล้วเปลี่ยนเป็นเครื่องมือ LLM และสุดท้ายจะได้การตอบกลับจาก MCP client ว่า "Sum 6"

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้