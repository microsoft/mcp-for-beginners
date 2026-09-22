# Tworzenie klienta

Klienci to niestandardowe aplikacje lub skrypty, które komunikują się bezpośrednio z serwerem MCP, aby żądać zasobów, narzędzi i podpowiedzi. W przeciwieństwie do korzystania z narzędzia inspektora, które zapewnia graficzny interfejs do interakcji z serwerem, napisanie własnego klienta umożliwia programowe i automatyczne interakcje. Pozwala to programistom na integrację możliwości MCP w ich własnych przepływach pracy, automatyzację zadań oraz budowanie niestandardowych rozwiązań dostosowanych do konkretnych potrzeb.

## Przegląd

Ta lekcja wprowadza pojęcie klientów w ekosystemie Model Context Protocol (MCP). Nauczysz się, jak napisać własnego klienta i połączyć go z serwerem MCP.

## Cele nauki

Pod koniec tej lekcji będziesz potrafił:

- Zrozumieć, do czego może służyć klient.
- Napisać własnego klienta.
- Połączyć i przetestować klienta z serwerem MCP, aby upewnić się, że działa zgodnie z oczekiwaniami.

## Co trzeba zrobić, aby napisać klienta?

Aby napisać klienta, musisz zrobić następujące rzeczy:

- **Zaimportować odpowiednie biblioteki**. Będziesz używać tej samej biblioteki co wcześniej, tylko innych konstrukcji.
- **Utworzyć klienta**. Obejmuje to utworzenie instancji klienta i połączenie go z wybraną metodą transportu.
- **Zdecydować, które zasoby wyświetlić**. Twój serwer MCP posiada zasoby, narzędzia i podpowiedzi, musisz zdecydować, które wyświetlić.
- **Zintegrować klienta z aplikacją hosta**. Gdy już znasz możliwości serwera, musisz zintegrować go z aplikacją hosta tak, aby po wpisaniu podpowiedzi lub innej komendy uruchamiana była odpowiednia funkcja serwera.

Teraz, gdy rozumiemy na wysokim poziomie, co mamy zrobić, spójrzmy na przykład.

### Przykładowy klient

Spójrzmy na ten przykładowy klient:

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// Lista promptów
const prompts = await client.listPrompts();

// Pobierz prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Lista zasobów
const resources = await client.listResources();

// Odczytaj zasób
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Wywołaj narzędzie
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

W powyższym kodzie:

- Importujemy biblioteki
- Tworzymy instancję klienta i łączymy ją za pomocą stdio jako transportu.
- Wyświetlamy listę podpowiedzi, zasobów i narzędzi oraz wywołujemy je wszystkie.

I oto masz — klient, który może rozmawiać z serwerem MCP.

Poświęćmy trochę czasu w następnej sekcji ćwiczeń, aby rozłożyć każdy fragment kodu i wyjaśnić, co się dzieje.

## Ćwiczenie: Pisanie klienta

Jak wspomniano powyżej, poświęćmy czas na wyjaśnienie kodu, i oczywiście możesz kodować razem z nami, jeśli chcesz.

### -1- Importowanie bibliotek

Zaimportujmy potrzebne biblioteki, będziemy potrzebować odniesień do klienta oraz do wybranego protokołu transportowego, stdio. stdio to protokół do rzeczy, które mają działać na twojej lokalnej maszynie. SSE to inny protokół transportowy, który pokażemy w kolejnych rozdziałach, ale na razie używajmy stdio.

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

W Javie stworzysz klienta, który łączy się z serwerem MCP z poprzedniego ćwiczenia. Korzystając z tej samej struktury projektu Java Spring Boot z [Wprowadzenia do serwera MCP](../../../../03-GettingStarted/01-first-server/solution/java), utwórz nową klasę Java o nazwie `SDKClient` w folderze `src/main/java/com/microsoft/mcp/sample/client/` i dodaj następujące importy:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

Musisz dodać następujące zależności do pliku `Cargo.toml`.

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

Następnie możesz zaimportować potrzebne biblioteki w kodzie klienta.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Przejdźmy do tworzenia instancji.

### -2- Tworzenie instancji klienta i transportu

Musimy utworzyć instancję transportu oraz instancję klienta:

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

W powyższym kodzie:

- Utworzono instancję transportu stdio. Zwróć uwagę, że określa polecenie i argumenty do znalezienia i uruchomienia serwera, ponieważ będziemy to musieli zrobić podczas tworzenia klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Utworzono instancję klienta, nadając mu nazwę i wersję.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Połączono klienta z wybranym transportem.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Utwórz parametry serwera dla połączenia stdio
server_params = StdioServerParameters(
    command="mcp",  # Wykonywalny
    args=["run", "server.py"],  # Opcjonalne argumenty wiersza poleceń
    env=None,  # Opcjonalne zmienne środowiskowe
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Zainicjuj połączenie
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

W powyższym kodzie:

- Zaimportowano potrzebne biblioteki
- Utworzono obiekt parametrów serwera, który użyjemy do uruchomienia serwera, aby móc połączyć się z nim za pomocą klienta.
- Zdefiniowano metodę `run`, która wywołuje `stdio_client`, rozpoczynającą sesję klienta.
- Utworzono punkt wejścia, gdzie przekazujemy metodę `run` do `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

W powyższym kodzie:

- Zaimportowano potrzebne biblioteki.
- Utworzono transport stdio i klienta `mcpClient`. Ten ostatni jest używany do wyświetlania i wywoływania funkcji na serwerze MCP.

Zwróć uwagę, że w „Argumentach” możesz wskazać albo plik *.csproj*, albo plik wykonywalny.

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // Twoja logika klienta idzie tutaj
    }
}
```

W powyższym kodzie:

- Utworzono metodę main, która ustawia transport SSE wskazujący na `http://localhost:8080`, gdzie będzie działać nasz serwer MCP.
- Utworzono klasę klienta, która przyjmuje transport jako parametr konstruktora.
- W metodzie `run` tworzymy synchronicznego klienta MCP używając transportu i inicjalizujemy połączenie.
- Użyto transportu SSE (Server-Sent Events), odpowiedniego do komunikacji HTTP z serwerami MCP Java Spring Boot.

#### Rust

Zauważ, że ten klient Rust zakłada, że serwer jest projektem rodzeństwem o nazwie „calculator-server” w tym samym katalogu. Poniższy kod uruchomi serwer i połączy się z nim.

```rust
async fn main() -> Result<(), RmcpError> {
    // Załóż, że serwer to projekt równorzędny o nazwie "calculator-server" w tym samym katalogu
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // DO ZROBIENIA: Inicjalizacja

    // DO ZROBIENIA: Wypisz narzędzia

    // DO ZROBIENIA: Wywołaj narzędzie add z argumentami = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Wyświetlanie funkcji serwera

Mamy teraz klienta, który może się połączyć po uruchomieniu programu. Jednak nie wyświetla on jeszcze dostępnych funkcji, zróbmy to teraz:

#### TypeScript

```typescript
// Lista podpowiedzi
const prompts = await client.listPrompts();

// Lista zasobów
const resources = await client.listResources();

// lista narzędzi
const tools = await client.listTools();
```

#### Python

```python
# Wyświetl dostępne zasoby
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Wyświetl dostępne narzędzia
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Tutaj wyświetlamy dostępne zasoby, `list_resources()` i narzędzia, `list_tools` oraz je drukujemy.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Powyżej przykładowo wyświetlamy narzędzia na serwerze. Dla każdego narzędzia drukujemy jego nazwę.

#### Java

```java
// Wypisz i pokaż narzędzia
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Możesz również pingować serwer, aby zweryfikować połączenie
client.ping();
```

W powyższym kodzie:

- Wywołano `listTools()`, aby uzyskać dostępne narzędzia z serwera MCP.
- Użyto `ping()`, aby zweryfikować, że połączenie z serwerem działa.
- `ListToolsResult` zawiera informacje o wszystkich narzędziach, w tym ich nazwy, opisy i schematy wejściowe.

Świetnie, uchwyciliśmy wszystkie funkcje. Pytanie tylko, kiedy ich używać? Ten klient jest prosty, co oznacza, że musimy jawnie wywołać funkcje, gdy ich potrzebujemy. W następnym rozdziale stworzymy bardziej zaawansowanego klienta, który posiada własny model językowy (LLM). Na razie zobaczmy, jak wywołać funkcje na serwerze:

#### Rust

W funkcji main, po zainicjalizowaniu klienta, możemy zainicjalizować serwer i wyświetlić niektóre jego funkcje.

```rust
// Inicjalizuj
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Lista narzędzi
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Wywoływanie funkcji

Aby wywołać funkcje, musimy zadbać o podanie właściwych argumentów, a w niektórych przypadkach nazwy tego, co chcemy wywołać.

#### TypeScript

```typescript

// Odczytaj zasób
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Wywołaj narzędzie
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// wywołaj podpowiedź
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

W powyższym kodzie:

- Odczytujemy zasób, wywołujemy `readResource()` podając `uri`. Oto jak to prawdopodobnie wygląda po stronie serwera:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    Nasza wartość `uri` `file://example.txt` odpowiada `file://{name}` na serwerze. `example.txt` zostanie przypisane do `name`.

- Wywołujemy narzędzie, podając jego `name` i `arguments` w ten sposób:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Pobieramy podpowiedź, aby ją uzyskać, wywołujemy `getPrompt()` z `name` i `arguments`. Kod serwera wygląda tak:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    Twoj kod klienta wygląda więc tak, aby pasował do deklaracji na serwerze:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# Odczytaj zasób
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Wywołaj narzędzie
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

W powyższym kodzie:

- Wywołaliśmy zasób o nazwie `greeting` za pomocą `read_resource`.
- Wywołaliśmy narzędzie o nazwie `add` za pomocą `call_tool`.

#### .NET

1. Dodajmy kod do wywołania narzędzia:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Aby wyświetlić wynik, oto kod obsługujący to zadanie:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Wywołaj różne narzędzia kalkulatora
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

W powyższym kodzie:

- Wywołano wiele narzędzi kalkulatora za pomocą metody `callTool()` i obiektów `CallToolRequest`.
- Każde wywołanie narzędzia określa nazwę narzędzia i mapę argumentów wymaganych przez to narzędzie.
- Narzędzia serwera oczekują specyficznych nazw parametrów (np. „a”, „b” dla operacji matematycznych).
- Wyniki zwracane są jako obiekty `CallToolResult`, zawierające odpowiedź z serwera.

#### Rust

```rust
// Wywołaj narzędzie add z argumentami = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- Uruchomienie klienta

Aby uruchomić klienta, wpisz następujące polecenie w terminalu:

#### TypeScript

Dodaj następujący wpis do sekcji "scripts" w *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Uruchom klienta następującym poleceniem:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Najpierw upewnij się, że serwer MCP działa pod adresem `http://localhost:8080`. Następnie uruchom klienta:

```bash
# Zbuduj swój projekt
./mvnw clean compile

# Uruchom klienta
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatywnie, możesz uruchomić kompletny projekt klienta dostępny w folderze rozwiązania `03-GettingStarted\02-client\solution\java`:

```bash
# Przejdź do katalogu rozwiązania
cd 03-GettingStarted/02-client/solution/java

# Zbuduj i uruchom plik JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Zadanie

W tym zadaniu wykorzystasz zdobytą wiedzę do stworzenia własnego klienta.

Oto serwer, którego możesz użyć i do którego musisz zadzwonić za pomocą kodu klienta — zobacz, czy potrafisz dodać więcej funkcji, aby był ciekawszy.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Utwórz serwer MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Dodaj narzędzie do dodawania
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dodaj dynamiczny zasób powitania
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Zacznij odbierać wiadomości na stdin i wysyłać wiadomości na stdout

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Utwórz serwer MCP
mcp = FastMCP("Demo")


# Dodaj narzędzie do dodawania
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dodaj dynamiczny zasób powitania
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

Sprawdź ten projekt, aby zobaczyć, jak możesz [dodać podpowiedzi i zasoby](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Zobacz także ten link, aby dowiedzieć się, jak wywołać [podpowiedzi i zasoby](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

W [poprzedniej sekcji](../../../../03-GettingStarted/01-first-server) nauczyłeś się tworzyć prosty serwer MCP w Rust. Możesz na tym dalej budować lub sprawdzić ten link z przykładami serwerów MCP w Rust: [Przykłady serwerów MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rozwiązanie

**Folder z rozwiązaniem** zawiera kompletne, gotowe do uruchomienia implementacje klienta, które demonstrują wszystkie pojęcia omówione w tym samouczku. Każde rozwiązanie zawiera zarówno kod klienta, jak i serwera zorganizowany w oddzielne, samodzielne projekty.

### 📁 Struktura rozwiązania

Katalog rozwiązania jest zorganizowany według języka programowania:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 Co zawiera każde rozwiązanie

Każde rozwiązanie specyficzne dla języka oferuje:

- **Kompletną implementację klienta** ze wszystkimi funkcjami z samouczka
- **Działającą strukturę projektu** z odpowiednimi zależnościami i konfiguracją
- **Skrypty budowania i uruchamiania** dla łatwej konfiguracji i wykonania
- **Szczegółowy README** z instrukcjami specyficznymi dla języka
- **Przykłady obsługi błędów** i przetwarzania wyników

### 📖 Korzystanie z rozwiązań

1. **Przejdź do folderu dla preferowanego języka**:

   ```bash
   cd solution/typescript/    # Dla TypeScript
   cd solution/java/          # Dla Java
   cd solution/python/        # Dla Pythona
   cd solution/dotnet/        # Dla .NET
   ```

2. **Postępuj zgodnie z instrukcjami w README** w każdym folderze, aby:
   - Zainstalować zależności
   - Zbudować projekt
   - Uruchomić klienta

3. **Przykładowe wyjście**, które powinieneś zobaczyć:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pełna dokumentacja i instrukcje krok po kroku dostępne są pod: **[📖 Dokumentacja rozwiązania](./solution/README.md)**

## 🎯 Kompleksowe przykłady

Udostępniliśmy kompletne, działające implementacje klientów dla wszystkich języków programowania omawianych w tym samouczku. Te przykłady demonstrują pełną funkcjonalność opisaną powyżej i mogą być używane jako wzorcowe implementacje lub punkt startowy do własnych projektów.

### Dostępne kompletne przykłady

| Język | Plik | Opis |
|-------|------|-------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kompletny klient Java używający transportu SSE z pełną obsługą błędów |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kompletny klient C# używający transportu stdio z automatycznym uruchamianiem serwera |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletny klient TypeScript z pełnym wsparciem protokołu MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kompletny klient Python używający wzorców async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Kompletny klient Rust używający Tokio do operacji asynchronicznych |

Każdy kompletny przykład zawiera:

- ✅ **Nawiązywanie połączenia** i obsługę błędów
- ✅ **Odkrywanie serwera** (narzędzia, zasoby, podpowiedzi tam gdzie dotyczy)
- ✅ **Operacje na kalkulatorze** (dodawanie, odejmowanie, mnożenie, dzielenie, pomoc)
- ✅ **Przetwarzanie wyników** i formatowane wyjście
- ✅ **Szczegółową obsługę błędów**

- ✅ **Czysty, udokumentowany kod** z komentarzami krok po kroku

### Pierwsze kroki z kompletnymi przykładami

1. **Wybierz preferowany język** z powyższej tabeli
2. **Przejrzyj kompletny plik z przykładem**, aby zrozumieć pełną implementację
3. **Uruchom przykład** zgodnie z instrukcjami w [`complete_examples.md`](./complete_examples.md)
4. **Zmodyfikuj i rozbuduj** przykład dla swojego konkretnego zastosowania

Szczegółową dokumentację dotyczącą uruchamiania i dostosowywania tych przykładów znajdziesz w: **[📖 Dokumentacja kompletnych przykładów](./complete_examples.md)**

### 💡 Rozwiązanie vs. Kompletny przykład

| **Folder rozwiązania** | **Kompletne przykłady** |
|--------------------|--------------------- |
| Pełna struktura projektu z plikami build | Implementacje pojedynczych plików |
| Gotowe do uruchomienia z zależnościami | Skoncentrowane przykłady kodu |
| Konfiguracja produkcyjna | Materiał edukacyjny |
| Narzędzia specyficzne dla języka | Porównanie międzyjęzykowe |

Oba podejścia są wartościowe - używaj **folderu rozwiązania** do kompletnych projektów, a **kompletnych przykładów** do nauki i odniesienia.

## Najważniejsze wnioski

Najważniejsze wnioski z tego rozdziału dotyczące klientów:

- Mogą być używane zarówno do odkrywania, jak i wywoływania funkcji na serwerze.
- Mogą uruchomić serwer, podczas gdy sam się uruchamia (jak w tym rozdziale), ale klienci mogą również łączyć się z działającymi serwerami.
- To świetny sposób na testowanie możliwości serwera obok alternatyw, takich jak Inspector, opisanych w poprzednim rozdziale.

## Dodatkowe zasoby

- [Tworzenie klientów w MCP](https://modelcontextprotocol.io/quickstart/client)

## Przykłady

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .NET](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)
- [Kalkulator Rust](../../../../03-GettingStarted/samples/rust)

## Co dalej

- Następny: [Tworzenie klienta z LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->