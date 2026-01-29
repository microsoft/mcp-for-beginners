# MCP stdio 서버 - .NET 솔루션

> **⚠️ 중요**: 이 솔루션은 MCP 사양 2025-06-18에서 권장하는 **stdio 전송**을 사용하도록 업데이트되었습니다. 기존 SSE 전송은 더 이상 사용되지 않습니다.

## 개요

이 .NET 솔루션은 현재 stdio 전송을 사용하여 MCP 서버를 구축하는 방법을 보여줍니다. stdio 전송은 더 간단하고, 더 안전하며, 사용이 중단된 SSE 방식보다 성능이 뛰어납니다.

## 사전 요구 사항

- .NET 9.0 SDK 이상
- .NET 종속성 주입에 대한 기본적인 이해

## 설정 지침

### 1단계: 종속성 복원

```bash
dotnet restore
```

### 2단계: 프로젝트 빌드

```bash
dotnet build
```

## 서버 실행

stdio 서버는 이전 HTTP 기반 서버와 다르게 실행됩니다. 웹 서버를 시작하는 대신 stdin/stdout을 통해 통신합니다:

```bash
dotnet run
```

**중요**: 서버가 멈춘 것처럼 보일 수 있습니다 - 정상입니다! 서버는 stdin에서 JSON-RPC 메시지를 기다리고 있습니다.

## 서버 테스트

### 방법 1: MCP Inspector 사용 (권장)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

이 작업은 다음을 수행합니다:
1. 서버를 하위 프로세스로 실행
2. 테스트를 위한 웹 인터페이스 열기
3. 모든 서버 도구를 대화형으로 테스트 가능

### 방법 2: 명령줄을 통한 직접 테스트

Inspector를 직접 실행하여 테스트할 수도 있습니다:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### 사용 가능한 도구

서버는 다음 도구를 제공합니다:

- **AddNumbers(a, b)**: 두 숫자를 더합니다
- **MultiplyNumbers(a, b)**: 두 숫자를 곱합니다  
- **GetGreeting(name)**: 개인화된 인사말을 생성합니다
- **GetServerInfo()**: 서버 정보를 가져옵니다

### Claude Desktop으로 테스트하기

Claude Desktop에서 이 서버를 사용하려면 `claude_desktop_config.json`에 다음 구성을 추가하세요:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## 프로젝트 구조

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE와의 주요 차이점

**stdio 전송 (현재):**
- ✅ 간단한 설정 - 웹 서버 불필요
- ✅ 더 나은 보안 - HTTP 엔드포인트 없음
- ✅ `Host.CreateApplicationBuilder()` 사용, `WebApplication.CreateBuilder()` 대신
- ✅ `WithStdioTransport()` 사용, `WithHttpTransport()` 대신
- ✅ 콘솔 애플리케이션, 웹 애플리케이션 대신
- ✅ 더 나은 성능

**HTTP/SSE 전송 (사용 중단됨):**
- ❌ ASP.NET Core 웹 서버 필요
- ❌ `app.MapMcp()` 라우팅 설정 필요
- ❌ 더 복잡한 구성 및 종속성
- ❌ 추가적인 보안 고려 사항
- ❌ MCP 2025-06-18에서 사용 중단됨

## 개발 기능

- **종속성 주입**: 서비스 및 로깅을 위한 완전한 DI 지원
- **구조화된 로깅**: `ILogger<T>`를 사용하여 stderr에 적절히 로깅
- **도구 속성**: `[McpServerTool]` 속성을 사용하여 깔끔한 도구 정의
- **비동기 지원**: 모든 도구는 비동기 작업을 지원
- **오류 처리**: 우아한 오류 처리 및 로깅

## 개발 팁

- 로깅에는 `ILogger`를 사용하세요 (stdout에 직접 쓰지 마세요)
- 테스트 전에 `dotnet build`로 빌드하세요
- Inspector를 사용하여 시각적 디버깅을 수행하세요
- 모든 로깅은 자동으로 stderr로 이동합니다
- 서버는 종료 신호를 우아하게 처리합니다

이 솔루션은 현재 MCP 사양을 따르며 .NET을 사용한 stdio 전송 구현의 모범 사례를 보여줍니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.