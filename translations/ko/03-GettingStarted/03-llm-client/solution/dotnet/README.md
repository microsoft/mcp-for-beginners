# 이 샘플 실행하기

> [!NOTE]
> 이 샘플은 GitHub Codespaces 인스턴스를 사용한다고 가정합니다. 로컬에서 실행하려면 GitHub에서 개인 액세스 토큰(PAT)을 설정해야 합니다.
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

## 라이브러리 설치

```sh
dotnet restore
```

다음 라이브러리가 설치되어야 합니다: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## 실행

```sh 
dotnet run
```

다음과 유사한 출력이 보여야 합니다:

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

출력의 대부분은 디버깅용이지만 중요한 점은 MCP 서버에서 도구를 나열하고, 이를 LLM 도구로 변환하여 MCP 클라이언트 응답 "Sum 6"을 얻는 것입니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.