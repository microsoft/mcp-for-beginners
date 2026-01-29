# Bu örneği çalıştır

> [!NOTE]
> Bu örnek, bir GitHub Codespaces örneği kullandığınızı varsayar. Bunu yerel olarak çalıştırmak istiyorsanız, GitHub üzerinde kişisel erişim belirteci (PAT) oluşturmanız gerekir.
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

## Kütüphaneleri yükle

```sh
dotnet restore
```

Aşağıdaki kütüphaneler yüklenmelidir: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## Çalıştır

```sh 
dotnet run
```

Aşağıdakine benzer bir çıktı görmelisiniz:

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

Çıktının çoğu sadece hata ayıklama amaçlıdır ancak önemli olan, MCP Sunucusundan araçları listelemeniz, bunları LLM araçlarına dönüştürmeniz ve sonunda MCP istemcisinden "Sum 6" yanıtını almanızdır.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.