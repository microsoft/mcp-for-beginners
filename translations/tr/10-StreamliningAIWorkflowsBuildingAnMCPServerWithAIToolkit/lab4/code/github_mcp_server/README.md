# Hava Durumu MCP Sunucusu

Bu, Python'da hava durumu araçlarını sahte yanıtlarla uygulayan örnek bir MCP Sunucusudur. Kendi MCP Sunucunuz için bir temel olarak kullanılabilir. Şu özellikleri içerir:

- **Hava Durumu Aracı**: Belirtilen konuma göre sahte hava durumu bilgileri sağlayan bir araç.
- **Git Klonlama Aracı**: Bir git deposunu belirtilen bir klasöre klonlayan bir araç.
- **VS Code Açma Aracı**: Bir klasörü VS Code veya VS Code Insiders'da açan bir araç.
- **Agent Builder'a Bağlanma**: MCP sunucusunu test ve hata ayıklama için Agent Builder'a bağlamanızı sağlayan bir özellik.
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ile Hata Ayıklama**: MCP Sunucusunu MCP Inspector kullanarak hata ayıklamanızı sağlayan bir özellik.

## Hava Durumu MCP Sunucusu şablonuyla başlama

> **Ön Koşullar**
>
> MCP Sunucusunu yerel geliştirme makinenizde çalıştırmak için ihtiyacınız olanlar:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo aracı için gereklidir)
> - [VS Code](https://code.visualstudio.com/) veya [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode aracı için gereklidir)
> - (*Opsiyonel - uv tercih ediyorsanız*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Ortamı Hazırlama

Bu proje için ortamı kurmanın iki yaklaşımı vardır. Tercihinize göre birini seçebilirsiniz.

> Not: Sanal ortam oluşturduktan sonra sanal ortam Python'unun kullanıldığından emin olmak için VSCode veya terminali yeniden yükleyin.

| Yaklaşım | Adımlar |
| -------- | ----- |
| `uv` kullanarak | 1. Sanal ortam oluşturun: `uv venv` <br>2. VSCode Komutunu çalıştırın "***Python: Select Interpreter***" ve oluşturulan sanal ortamdan Python'u seçin <br>3. Bağımlılıkları yükleyin (geliştirme bağımlılıkları dahil): `uv pip install -r pyproject.toml --extra dev` |
| `pip` kullanarak | 1. Sanal ortam oluşturun: `python -m venv .venv` <br>2. VSCode Komutunu çalıştırın "***Python: Select Interpreter***" ve oluşturulan sanal ortamdan Python'u seçin <br>3. Bağımlılıkları yükleyin (geliştirme bağımlılıkları dahil): `pip install -e .[dev]` |

Ortamı kurduktan sonra, MCP Client olarak Agent Builder üzerinden yerel geliştirme makinenizde sunucuyu çalıştırabilirsiniz:
1. VS Code Hata Ayıklama panelini açın. `Debug in Agent Builder` seçeneğini seçin veya MCP sunucusunu başlatmak için `F5` tuşuna basın.
2. AI Toolkit Agent Builder'ı kullanarak [bu istemi](../../../../../../../../../../../open_prompt_builder) test etmek için sunucuyu kullanın. Sunucu otomatik olarak Agent Builder'a bağlanacaktır.
3. İstemi test etmek için `Run` düğmesine tıklayın.

**Tebrikler**! MCP Client olarak Agent Builder üzerinden yerel geliştirme makinenizde Hava Durumu MCP Sunucusunu başarıyla çalıştırdınız.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Şablonda neler var?

| Klasör / Dosya | İçerik                                     |
| -------------- | ------------------------------------------ |
| `.vscode`      | Hata ayıklama için VSCode dosyaları        |
| `.aitk`        | AI Toolkit için yapılandırmalar            |
| `src`          | Hava durumu MCP sunucusunun kaynak kodu    |

## Hava Durumu MCP Sunucusunu nasıl hata ayıklarsınız?

> Notlar:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector), MCP sunucularını test etmek ve hata ayıklamak için görsel bir geliştirici aracıdır.
> - Tüm hata ayıklama modları kesme noktalarını destekler, böylece araç uygulama koduna kesme noktaları ekleyebilirsiniz.

## Kullanılabilir Araçlar

### Hava Durumu Aracı
`get_weather` aracı, belirtilen bir konum için sahte hava durumu bilgileri sağlar.

| Parametre | Tür | Açıklama |
| --------- | --- | -------- |
| `location` | string | Hava durumu alınacak konum (örneğin, şehir adı, eyalet veya koordinatlar) |

### Git Klonlama Aracı
`git_clone_repo` aracı, bir git deposunu belirtilen bir klasöre klonlar.

| Parametre | Tür | Açıklama |
| --------- | --- | -------- |
| `repo_url` | string | Klonlanacak git deposunun URL'si |
| `target_folder` | string | Depo klonlanacak klasörün yolu |

Araç bir JSON nesnesi döndürür:
- `success`: İşlemin başarılı olup olmadığını belirten bir boolean
- `target_folder` veya `error`: Klonlanan depo yolu veya hata mesajı

### VS Code Açma Aracı
`open_in_vscode` aracı, bir klasörü VS Code veya VS Code Insiders uygulamasında açar.

| Parametre | Tür | Açıklama |
| --------- | --- | -------- |
| `folder_path` | string | Açılacak klasörün yolu |
| `use_insiders` | boolean (opsiyonel) | Normal VS Code yerine VS Code Insiders kullanılıp kullanılmayacağı |

Araç bir JSON nesnesi döndürür:
- `success`: İşlemin başarılı olup olmadığını belirten bir boolean
- `message` veya `error`: Onay mesajı veya hata mesajı

| Hata Ayıklama Modu | Açıklama | Hata Ayıklama Adımları |
| ------------------ | -------- | ---------------------- |
| Agent Builder | MCP sunucusunu AI Toolkit üzerinden Agent Builder'da hata ayıklayın. | 1. VS Code Hata Ayıklama panelini açın. `Debug in Agent Builder` seçeneğini seçin ve `F5` tuşuna basarak MCP sunucusunu başlatın.<br>2. AI Toolkit Agent Builder'ı kullanarak [bu istemi](../../../../../../../../../../../open_prompt_builder) test etmek için sunucuyu kullanın. Sunucu otomatik olarak Agent Builder'a bağlanacaktır.<br>3. İstemi test etmek için `Run` düğmesine tıklayın. |
| MCP Inspector | MCP sunucusunu MCP Inspector kullanarak hata ayıklayın. | 1. [Node.js](https://nodejs.org/) yükleyin<br> 2. Inspector'ı kurun: `cd inspector` && `npm install` <br> 3. VS Code Hata Ayıklama panelini açın. `Debug SSE in Inspector (Edge)` veya `Debug SSE in Inspector (Chrome)` seçeneğini seçin. `F5` tuşuna basarak hata ayıklamayı başlatın.<br> 4. MCP Inspector tarayıcıda açıldığında, bu MCP sunucusuna bağlanmak için `Connect` düğmesine tıklayın.<br> 5. Ardından `List Tools` seçeneğini kullanabilir, bir araç seçebilir, parametreleri girebilir ve sunucu kodunuzu hata ayıklamak için `Run Tool` seçeneğini kullanabilirsiniz.<br> |

## Varsayılan Portlar ve Özelleştirmeler

| Hata Ayıklama Modu | Portlar | Tanımlar | Özelleştirmeler | Not |
| ------------------ | ------ | -------- | --------------- | --- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) dosyalarını düzenleyerek yukarıdaki portları değiştirebilirsiniz. | N/A |
| MCP Inspector | 3001 (Sunucu); 5173 ve 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) dosyalarını düzenleyerek yukarıdaki portları değiştirebilirsiniz. | N/A |

## Geri Bildirim

Bu şablonla ilgili herhangi bir geri bildiriminiz veya öneriniz varsa, lütfen [AI Toolkit GitHub deposunda](https://github.com/microsoft/vscode-ai-toolkit/issues) bir sorun açın.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.