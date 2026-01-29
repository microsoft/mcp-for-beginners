# Jalankan contoh ini

> [!NOTE]
> Contoh ini mengasumsikan Anda menggunakan instance GitHub Codespaces. Jika ingin menjalankannya secara lokal, Anda perlu membuat personal access token (PAT) di GitHub.
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

## Instal pustaka

```sh
dotnet restore
```

Harus menginstal pustaka berikut: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## Jalankan

```sh 
dotnet run
```

Anda akan melihat output yang mirip dengan:

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

Sebagian besar output hanya untuk debugging, tapi yang penting adalah Anda sedang mendaftar alat dari MCP Server, mengubahnya menjadi alat LLM, dan akhirnya mendapatkan respons klien MCP "Sum 6".

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.