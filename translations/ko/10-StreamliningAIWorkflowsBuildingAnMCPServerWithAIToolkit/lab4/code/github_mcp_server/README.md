# Weather MCP Server

이 문서는 Python으로 구현된 샘플 MCP 서버로, 날씨 도구를 모의 응답으로 제공하며, 여러분의 MCP 서버를 위한 기본 구조로 사용할 수 있습니다. 다음과 같은 기능을 포함하고 있습니다:

- **Weather Tool**: 주어진 위치를 기반으로 모의 날씨 정보를 제공하는 도구.
- **Git Clone Tool**: Git 저장소를 지정된 폴더에 복제하는 도구.
- **VS Code Open Tool**: VS Code 또는 VS Code Insiders에서 폴더를 여는 도구.
- **Connect to Agent Builder**: MCP 서버를 Agent Builder에 연결하여 테스트 및 디버깅할 수 있는 기능.
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)에서 디버깅**: MCP Inspector를 사용하여 MCP 서버를 디버깅할 수 있는 기능.

## Weather MCP Server 템플릿 시작하기

> **필수 조건**
>
> 로컬 개발 환경에서 MCP 서버를 실행하려면 다음이 필요합니다:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo 도구에 필요)
> - [VS Code](https://code.visualstudio.com/) 또는 [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode 도구에 필요)
> - (*선택 사항 - uv를 선호하는 경우*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 환경 준비

이 프로젝트의 환경을 설정하는 두 가지 방법이 있습니다. 선호하는 방법을 선택하세요.

> 참고: 가상 환경을 생성한 후, VSCode 또는 터미널을 다시 로드하여 가상 환경의 Python이 사용되도록 하세요.

| 방법 | 단계 |
| ---- | ---- |
| `uv` 사용 | 1. 가상 환경 생성: `uv venv` <br>2. VSCode 명령 "***Python: Select Interpreter***" 실행 후 생성된 가상 환경의 Python 선택 <br>3. 종속성 설치 (개발 종속성 포함): `uv pip install -r pyproject.toml --extra dev` |
| `pip` 사용 | 1. 가상 환경 생성: `python -m venv .venv` <br>2. VSCode 명령 "***Python: Select Interpreter***" 실행 후 생성된 가상 환경의 Python 선택 <br>3. 종속성 설치 (개발 종속성 포함): `pip install -e .[dev]` |

환경 설정 후, MCP Client로서 Agent Builder를 통해 로컬 개발 환경에서 서버를 실행할 수 있습니다:
1. VS Code 디버그 패널을 열고 `Debug in Agent Builder`를 선택하거나 `F5`를 눌러 MCP 서버 디버깅을 시작합니다.
2. AI Toolkit Agent Builder를 사용하여 [이 프롬프트](../../../../../../../../../../../open_prompt_builder)를 통해 서버를 테스트합니다. 서버는 자동으로 Agent Builder에 연결됩니다.
3. `Run`을 클릭하여 프롬프트로 서버를 테스트합니다.

**축하합니다**! MCP Client로서 Agent Builder를 통해 로컬 개발 환경에서 Weather MCP Server를 성공적으로 실행했습니다.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## 템플릿에 포함된 내용

| 폴더 / 파일 | 내용                                     |
| ----------- | ---------------------------------------- |
| `.vscode`   | 디버깅을 위한 VSCode 파일               |
| `.aitk`     | AI Toolkit 설정 파일                    |
| `src`       | Weather MCP Server의 소스 코드          |

## Weather MCP Server 디버깅 방법

> 참고:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector)는 MCP 서버를 테스트하고 디버깅하기 위한 시각적 개발 도구입니다.
> - 모든 디버깅 모드는 중단점을 지원하므로, 도구 구현 코드에 중단점을 추가할 수 있습니다.

## 사용 가능한 도구

### Weather Tool
`get_weather` 도구는 지정된 위치에 대한 모의 날씨 정보를 제공합니다.

| 매개변수 | 유형 | 설명 |
| -------- | ---- | ---- |
| `location` | string | 날씨 정보를 얻고자 하는 위치 (예: 도시 이름, 주, 또는 좌표) |

### Git Clone Tool
`git_clone_repo` 도구는 Git 저장소를 지정된 폴더에 복제합니다.

| 매개변수 | 유형 | 설명 |
| -------- | ---- | ---- |
| `repo_url` | string | 복제할 Git 저장소의 URL |
| `target_folder` | string | 저장소를 복제할 폴더 경로 |

도구는 다음을 포함하는 JSON 객체를 반환합니다:
- `success`: 작업 성공 여부를 나타내는 Boolean 값
- `target_folder` 또는 `error`: 복제된 저장소의 경로 또는 오류 메시지

### VS Code Open Tool
`open_in_vscode` 도구는 VS Code 또는 VS Code Insiders 애플리케이션에서 폴더를 엽니다.

| 매개변수 | 유형 | 설명 |
| -------- | ---- | ---- |
| `folder_path` | string | 열고자 하는 폴더 경로 |
| `use_insiders` | boolean (선택 사항) | 일반 VS Code 대신 VS Code Insiders를 사용할지 여부 |

도구는 다음을 포함하는 JSON 객체를 반환합니다:
- `success`: 작업 성공 여부를 나타내는 Boolean 값
- `message` 또는 `error`: 확인 메시지 또는 오류 메시지

| 디버그 모드 | 설명 | 디버깅 단계 |
| ----------- | ---- | ----------- |
| Agent Builder | AI Toolkit을 통해 Agent Builder에서 MCP 서버 디버깅. | 1. VS Code 디버그 패널을 열고 `Debug in Agent Builder`를 선택한 후 `F5`를 눌러 MCP 서버 디버깅 시작.<br>2. AI Toolkit Agent Builder를 사용하여 [이 프롬프트](../../../../../../../../../../../open_prompt_builder)를 통해 서버를 테스트합니다. 서버는 자동으로 Agent Builder에 연결됩니다.<br>3. `Run`을 클릭하여 프롬프트로 서버를 테스트합니다. |
| MCP Inspector | MCP Inspector를 사용하여 MCP 서버 디버깅. | 1. [Node.js](https://nodejs.org/) 설치<br> 2. Inspector 설정: `cd inspector` && `npm install` <br> 3. VS Code 디버그 패널을 열고 `Debug SSE in Inspector (Edge)` 또는 `Debug SSE in Inspector (Chrome)`을 선택한 후 F5를 눌러 디버깅 시작.<br> 4. MCP Inspector가 브라우저에서 실행되면 `Connect` 버튼을 클릭하여 MCP 서버를 연결합니다.<br> 5. 이후 `List Tools`를 선택하고, 도구를 선택한 후 매개변수를 입력하고 `Run Tool`을 클릭하여 서버 코드를 디버깅합니다.<br> |

## 기본 포트 및 사용자 정의

| 디버그 모드 | 포트 | 정의 | 사용자 정의 | 참고 |
| ----------- | ---- | ---- | ---------- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json)을 편집하여 위 포트를 변경할 수 있습니다. | N/A |
| MCP Inspector | 3001 (서버); 5173 및 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json)을 편집하여 위 포트를 변경할 수 있습니다. | N/A |

## 피드백

이 템플릿에 대한 피드백이나 제안이 있다면 [AI Toolkit GitHub 저장소](https://github.com/microsoft/vscode-ai-toolkit/issues)에 이슈를 열어주세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.