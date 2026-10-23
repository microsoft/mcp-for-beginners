# Jalankan contoh ini

> [!NOTE]
> Terapkan model aktif seperti `gpt-5.1` di Microsoft Foundry dan konfigurasikan
> endpoint, kunci API, dan nama penerapannya.
>
> ```bash
> # zsh/bash
> export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
> export AZURE_OPENAI_API_KEY="<api-key>"
> export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
> ```
>
> ```powershell
> # PowerShell
> $env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
> $env:AZURE_OPENAI_API_KEY = "<api-key>"
> $env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
> ```

## Instal perpustakaan

```sh
dotnet restore
```

Ini menginstal klien OpenAI .NET dan SDK Model Context Protocol.

## Jalankan

```sh 
dotnet run
```

Anda seharusnya melihat output yang mirip dengan:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: OpenAI.Chat.ChatTool
MCP Tools def: 0: OpenAI.Chat.ChatTool
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

Banyak output hanyalah debugging tapi yang penting adalah bahwa Anda sedang mendaftarkan alat dari MCP Server, mengubahnya menjadi alat LLM dan akhirnya mendapatkan respons klien MCP "Sum 6".

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->