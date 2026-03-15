# MCP 서버 배포

MCP 서버를 배포하면 로컬 환경을 넘어서 다른 사람들이 해당 도구와 리소스에 접근할 수 있습니다. 확장성, 신뢰성, 관리 용이성에 대한 요구 사항에 따라 고려할 수 있는 여러 배포 전략이 있습니다. 아래에는 MCP 서버를 로컬, 컨테이너, 클라우드에 배포하는 방법에 대한 안내가 나와 있습니다.

## 개요

이 레슨에서는 MCP 서버 앱을 배포하는 방법을 다룹니다.

## 학습 목표

이 레슨을 마치면 다음을 할 수 있습니다:

- 다양한 배포 접근 방식을 평가할 수 있습니다.
- 앱을 배포할 수 있습니다.

## 로컬 개발 및 배포

서버가 사용자 머신에서 실행되어 소비되는 경우 다음 단계를 따르십시오:

1. **서버 다운로드**. 서버를 직접 작성하지 않았다면 먼저 서버를 머신에 다운로드하십시오.
1. **서버 프로세스 시작**: MCP 서버 애플리케이션을 실행합니다.

SSE의 경우 (stdio 유형 서버에는 필요하지 않음)

1. **네트워킹 구성**: 서버가 예상된 포트에서 접근 가능하도록 설정합니다.
1. **클라이언트 연결**: `http://localhost:3000` 같은 로컬 연결 URL을 사용합니다.

## 클라우드 배포

MCP 서버는 여러 클라우드 플랫폼에 배포할 수 있습니다:

- **서버리스 함수**: 경량 MCP 서버를 서버리스 함수로 배포
- **컨테이너 서비스**: Azure Container Apps, AWS ECS, Google Cloud Run 등의 서비스를 사용
- **쿠버네티스**: 고가용성을 위해 쿠버네티스 클러스터에서 MCP 서버를 배포 및 관리

### 예시: Azure Container Apps

Azure Container Apps는 MCP 서버 배포를 지원합니다. 아직 개발 중이며 현재는 SSE 서버를 지원합니다.

방법은 다음과 같습니다:

1. 리포지토리를 클론합니다:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. 로컬에서 실행하여 테스트합니다:

  ```sh
  uv venv
  uv sync

  # 리눅스/macOS
  export API_KEYS=<AN_API_KEY>
  # 윈도우
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. 로컬에서 시도하려면 *.vscode* 디렉터리에 *mcp.json* 파일을 생성하고 다음 내용을 추가합니다:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  SSE 서버가 시작되면 JSON 파일의 재생 아이콘을 클릭할 수 있습니다. 이제 GitHub Copilot에서 서버의 도구를 인식하는 것을 확인할 수 있으며, 도구 아이콘을 참조하세요.

1. 배포하려면 다음 명령을 실행합니다:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

이렇게 하면 로컬에 배포하고, 이 단계들을 통해 Azure에 배포할 수 있습니다.

## 추가 자료

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 기사](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP 리포지토리](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## 다음 단계

- 다음: [고급 서버 주제](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다했지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원본 문서는 해당 언어로 작성된 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 모든 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->