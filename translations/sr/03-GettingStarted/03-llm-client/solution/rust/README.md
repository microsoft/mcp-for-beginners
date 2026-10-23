# Покретање овог примера

Ово је Rust решење за пример LLM клијента. Потребно је да имате инсталиран Rust тулчејн; погледајте [официјални приручник за инсталацију](https://www.rust-lang.org/tools/install).

Клијент позива постављени Microsoft Foundry модел преко Azure OpenAI
v1 крајње тачке.

> [!NOTE]
> Вредност која се прослеђује као `model` је име ваше Foundry имплементације, не нужно
> име основног модела.

## -0- Конфигурација Microsoft Foundry

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
$env:AZURE_OPENAI_API_KEY = "<api-key>"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
```

## -1- Изградња примера

```bash
cargo build
```

## -2- Покретање примера

```bash
cargo run
```

Клијент покреће MCP сервер калкулатора, преузима листу алата и користи
постављени модел за позив алата `add`. Требало би да видите излаз који указује
на позив алата (на пример, "Позив алата: add") и резултат тог позива.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->