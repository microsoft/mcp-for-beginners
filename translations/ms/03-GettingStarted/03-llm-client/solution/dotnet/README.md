# Jalankan sampel ini

> [!NOTE]
> Sebarkan model aktif seperti `gpt-5.1` dalam Microsoft Foundry dan konfigurasikan
> endpoint, kunci API, dan nama penyebarannya.
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

## Pasang pustaka

```sh
dotnet restore
```

Ini memasang klien OpenAI .NET dan SDK Protokol Konteks Model.

## Jalankan

```sh 
dotnet run
```

Anda harus melihat keluaran yang serupa dengan:

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

Kebanyakan keluaran hanyalah untuk penyahpepijatan tetapi yang penting adalah anda disenaraikan alat dari MCP Server, tukarkan itu menjadi alat LLM dan anda akan mendapat tindak balas klien MCP "Jumlah 6".

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->