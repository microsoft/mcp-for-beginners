# Basic Calculator MCP Service

이 서비스는 Model Context Protocol(MCP)을 통해 기본 계산기 연산을 제공합니다. MCP 구현을 배우는 초보자를 위한 간단한 예제로 설계되었습니다.

자세한 내용은 [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)를 참고하세요.

## 기능

이 계산기 서비스는 다음과 같은 기능을 제공합니다:

1. **기본 산술 연산**:
   - 두 수의 덧셈
   - 한 수에서 다른 수를 뺌
   - 두 수의 곱셈
   - 한 수를 다른 수로 나눔 (제로 나누기 검사 포함)

## `stdio` 타입 사용하기

## 구성

1. **MCP 서버 구성하기**:
   - VS Code에서 작업 공간을 엽니다.
   - 작업 공간 폴더에 `.vscode/mcp.json` 파일을 만들어 MCP 서버를 구성합니다. 예시 구성:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - GitHub 저장소 루트를 입력하라는 요청이 나오며, 이는 `git rev-parse --show-toplevel` 명령어로 확인할 수 있습니다.

## 서비스 사용법

이 서비스는 MCP 프로토콜을 통해 다음 API 엔드포인트를 제공합니다:

- `add(a, b)`: 두 수를 더합니다
- `subtract(a, b)`: 첫 번째 수에서 두 번째 수를 뺍니다
- `multiply(a, b)`: 두 수를 곱합니다
- `divide(a, b)`: 첫 번째 수를 두 번째 수로 나눕니다 (제로 검사 포함)
- isPrime(n): 숫자가 소수인지 확인합니다

## VS Code에서 Github Copilot Chat으로 테스트하기

1. MCP 프로토콜을 사용해 서비스에 요청을 시도해보세요. 예를 들어 다음과 같이 물어볼 수 있습니다:
   - "5와 3을 더해줘"
   - "4에서 10을 빼줘"
   - "6과 7을 곱해줘"
   - "8을 2로 나눠줘"
   - "37854는 소수인가?"
   - "4242 전후의 소수 3개를 알려줘"
2. 도구를 사용하고 있는지 확인하려면 프롬프트에 #MyCalculator를 추가하세요. 예를 들어:
   - "5와 3을 더해줘 #MyCalculator"
   - "4에서 10을 빼줘 #MyCalculator"

## 컨테이너 버전

이전 솔루션은 .NET SDK가 설치되어 있고 모든 종속성이 갖춰져 있을 때 훌륭합니다. 하지만 솔루션을 공유하거나 다른 환경에서 실행하려면 컨테이너 버전을 사용할 수 있습니다.

1. Docker를 시작하고 실행 중인지 확인하세요.
1. 터미널에서 `03-GettingStarted\samples\csharp\src` 폴더로 이동하세요.
1. 계산기 서비스용 Docker 이미지를 빌드하려면 다음 명령어를 실행하세요 (`<YOUR-DOCKER-USERNAME>`를 Docker Hub 사용자 이름으로 바꾸세요):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. 이미지가 빌드되면 Docker Hub에 업로드합니다. 다음 명령어를 실행하세요:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Dockerized 버전 사용하기

1. `.vscode/mcp.json` 파일에서 서버 구성을 다음과 같이 바꾸세요:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   구성 내용을 보면 명령어는 `docker`이고 인자는 `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`입니다. `--rm` 플래그는 컨테이너가 중지된 후 삭제되도록 하며, `-i` 플래그는 컨테이너의 표준 입력과 상호작용할 수 있게 합니다. 마지막 인자는 우리가 방금 빌드하고 Docker Hub에 푸시한 이미지 이름입니다.

## Dockerized 버전 테스트하기

`"mcp-calc": {` 위에 있는 작은 시작 버튼을 클릭해 MCP 서버를 시작하세요. 이전과 마찬가지로 계산기 서비스에 수학 문제를 요청할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.