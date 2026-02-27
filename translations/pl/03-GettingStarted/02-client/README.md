# Tworzenie klienta

Klienci to niestandardowe aplikacje lub skrypty, które komunikują się bezpośrednio z serwerem MCP, aby żądać zasobów, narzędzi i promptów. W przeciwieństwie do korzystania z narzędzia inspektora, które zapewnia graficzny interfejs do interakcji z serwerem, napisanie własnego klienta pozwala na programistyczne i automatyczne interakcje. Umożliwia to programistom integrację możliwości MCP z własnymi procesami pracy, automatyzację zadań oraz budowę niestandardowych rozwiązań dopasowanych do konkretnych potrzeb.

## Przegląd

Ta lekcja wprowadza pojęcie klientów w ekosystemie Model Context Protocol (MCP). Nauczysz się, jak napisać własnego klienta i połączyć go z serwerem MCP.

## Cele nauki

Na koniec tej lekcji będziesz umiał:

- Zrozumieć, co klient może robić.
- Napisać własnego klienta.
- Połączyć i przetestować klienta z serwerem MCP, aby upewnić się, że działa zgodnie z oczekiwaniami.

## Co wymaga napisanie klienta?

Aby napisać klienta, musisz wykonać następujące kroki:

- **Zaimportować odpowiednie biblioteki**. Będziesz używać tej samej biblioteki co wcześniej, ale innych konstrukcji.
- **Utworzyć instancję klienta**. To będzie polegać na stworzeniu instancji klienta i podłączeniu jej za pomocą wybranej metody transportu.
- **Zdecydować, jakie zasoby wyświetlać**. Twój serwer MCP oferuje zasoby, narzędzia i prompty; musisz zdecydować, które z nich wyświetlić.
- **Zintegrować klienta z aplikacją hosta**. Gdy już poznasz możliwości serwera, musisz zintegrować klienta z aplikacją hosta tak, aby jeśli użytkownik wpisze prompt lub inne polecenie, wywołana została odpowiednia funkcja serwera.

Teraz, gdy rozumiemy ogólnie, co będziemy robić, przyjrzyjmy się kolejnemu przykładowi.

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

// Lista podpowiedzi
const prompts = await client.listPrompts();

// Pobierz podpowiedź
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
- Tworzymy instancję klienta i łączymy ją używając stdio jako transportu
- Wyświetlamy listę promptów, zasobów i narzędzi, a następnie je wywołujemy

Oto masz klienta, który może komunikować się z serwerem MCP.

Poświęćmy czas w następnej części ćwiczenia, by przeanalizować każdy fragment kodu i wyjaśnić, co się dzieje.

## Ćwiczenie: Pisanie klienta

Jak powiedziano powyżej, poświęćmy czas na tłumaczenie kodu, a jeśli chcesz, programuj razem z nami.

### -1- Import bibliotek

Zaimportujmy potrzebne biblioteki; potrzebujemy odniesień do klienta i do wybranego protokołu transportowego, czyli stdio. stdio to protokół do rzeczy uruchamianych lokalnie. SSE to inny protokół transportowy, który pokażemy w przyszłych rozdziałach, ale to jest twoja druga opcja. Na razie jednak kontynuujemy ze stdio.

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

Dla Javy stworzysz klienta łączącego się z serwerem MCP z poprzedniego ćwiczenia. Używając tej samej struktury projektu Java Spring Boot z [Wprowadzenie do serwera MCP](../../../../03-GettingStarted/01-first-server/solution/java), utwórz nową klasę Java o nazwie `SDKClient` w folderze `src/main/java/com/microsoft/mcp/sample/client/` i dodaj następujące importy:

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

Będziesz musiał dodać następujące zależności do pliku `Cargo.toml`.

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

Przejdźmy teraz do tworzenia instancji.

### -2- Tworzenie instancji klienta i transportu

Musimy utworzyć instancję transportu oraz klienta:

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

- Utworzono instancję transportu stdio. Zwróć uwagę, jak określa polecenie i argumenty do znalezienia i uruchomienia serwera, ponieważ będziemy to musieli zrobić pisząc klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Utworzono klienta, nadając mu nazwę i wersję.

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
- Utworzono obiekt parametrów serwera, ponieważ użyjemy go do uruchomienia serwera, abyśmy mogli się z nim połączyć klientem.
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
- Utworzono transport stdio oraz klienta o nazwie `mcpClient`. Ten ostatni będzie używany do listowania i wywoływania funkcji na serwerze MCP.

Uwaga: w polu "Arguments" możesz wskazać albo plik *.csproj*, albo plik wykonywalny.

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

- Utworzono metodę main, która ustawia transport SSE wskazujący na `http://localhost:8080`, gdzie będzie działał nasz serwer MCP.
- Utworzono klasę klienta, która przyjmuje transport jako parametr konstruktora.
- W metodzie `run` tworzymy synchronicznego klienta MCP, korzystając z transportu, i inicjalizujemy połączenie.
- Użyto transportu SSE (Server-Sent Events), odpowiedniego dla komunikacji HTTP z serwerami MCP opartymi na Java Spring Boot.

#### Rust

Ten klient Rust zakłada, że serwer jest projektem rodzeństwem o nazwie "calculator-server" w tym samym katalogu. Poniższy kod uruchomi serwer i połączy się z nim.

```rust
async fn main() -> Result<(), RmcpError> {
    // Załóżmy, że serwer to projekt rodzeństwa o nazwie "calculator-server" w tym samym katalogu
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

    // DO ZROBIENIA: Wyświetl listę narzędzi

    // DO ZROBIENIA: Wywołaj narzędzie add z argumentami = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Wyświetlanie funkcji serwera

Mamy teraz klienta, który może połączyć się z serwerem po uruchomieniu programu. Jednak nie wyświetla on jeszcze funkcji, więc zróbmy to teraz:

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
# Wymień dostępne zasoby
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Wymień dostępne narzędzia
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Tutaj wyświetlamy dostępne zasoby, `list_resources()`, i narzędzia, `list_tools`, i wypisujemy je.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Powyżej przykład, jak wyświetlić narzędzia na serwerze. Dla każdego narzędzia wypisujemy jego nazwę.

#### Java

```java
// Wymień i zademonstruj narzędzia
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Możesz także pingować serwer, aby zweryfikować połączenie
client.ping();
```

W powyższym kodzie:

- Wywołano `listTools()`, aby pobrać wszystkie dostępne narzędzia z serwera MCP.
- Użyto `ping()`, aby zweryfikować, że połączenie z serwerem działa.
- `ListToolsResult` zawiera informacje o wszystkich narzędziach, łącznie z ich nazwami, opisami i schematami wejściowymi.

Świetnie, mamy teraz wszystkie funkcje. Ale kiedy je wykorzystać? Ten klient jest dość prosty, co oznacza, że będziemy musieli wywoływać funkcje explicite, gdy będziemy ich chcieli. W następnym rozdziale stworzymy bardziej zaawansowanego klienta mającego dostęp do własnego dużego modelu językowego (LLM). Na razie jednak zobaczmy, jak wywołać funkcje na serwerze:

#### Rust

W funkcji main, po inicjalizacji klienta, możemy zainicjalizować serwer i wyświetlić niektóre jego funkcje.

```rust
// Inicjalizuj
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Wyświetl narzędzia
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Wywoływanie funkcji

Aby wywołać funkcje, musimy zapewnić podanie właściwych argumentów, a w niektórych przypadkach nazwy tego, co wywołujemy.

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

- Odczytujemy zasób, wywołujemy go przez `readResource()`, podając `uri`. Oto jak to prawdopodobnie wygląda na serwerze:

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

    Wartość `uri` `file://example.txt` odpowiada wzorcowi `file://{name}` na serwerze. `example.txt` zostanie przypisane do `name`.

- Wywołujemy narzędzie, podając jego `name` i `arguments` w ten sposób:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Pobieramy prompt, wywołując `getPrompt()` z `name` i `arguments`. Kod serwera wygląda tak:

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

    a więc wynikowy kod klienta wygląda tak, aby pasować do tego, co jest zadeklarowane na serwerze:

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

- Wywołaliśmy zasób `greeting` używając `read_resource`.
- Wywołaliśmy narzędzie `add` używając `call_tool`.

#### .NET

1. Dodajmy kod do wywołania narzędzia:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. Aby wypisać wynik, oto kod to obsługujący:

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

- Wywołano wiele narzędzi kalkulatora używając metody `callTool()` z obiektami `CallToolRequest`.
- Każde wywołanie narzędzia określa nazwę narzędzia i mapę argumentów wymaganych przez to narzędzie.
- Narzędzia serwera oczekują określonych nazw parametrów (np. "a", "b" dla operacji matematycznych).
- Wyniki zwracane są jako obiekty `CallToolResult`, zawierające odpowiedź z serwera.

#### Rust

```rust
// Wywołaj narzędzie dodawania z argumentami = {"a": 3, "b": 2}
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

Wywołaj klienta następującym poleceniem:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Najpierw upewnij się, że twój serwer MCP działa pod adresem `http://localhost:8080`. Następnie uruchom klienta:

```bash
# Zbuduj swój projekt
./mvnw clean compile

# Uruchom klienta
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatywnie możesz uruchomić kompletny projekt klienta dostępny w folderze `03-GettingStarted\02-client\solution\java`:

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

W tym zadaniu wykorzystasz wiedzę zdobytą przy tworzeniu klienta, ale stworzysz własnego klienta.

Oto serwer, którego możesz użyć i wywołać go za pomocą swojego kodu klienta; sprawdź, czy potrafisz dodać więcej funkcji do serwera, by uczynić go bardziej interesującym.

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

// Dodaj dynamiczne zasoby powitalne
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

// Rozpocznij odbieranie wiadomości na stdin i wysyłanie wiadomości na stdout

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

Zobacz ten projekt, aby dowiedzieć się, jak [dodawać prompty i zasoby](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Sprawdź też ten link, aby dowiedzieć się, jak wywoływać [prompty i zasoby](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

W [poprzedniej sekcji](../../../../03-GettingStarted/01-first-server) nauczyłeś się, jak stworzyć prosty serwer MCP z Rustem. Możesz dalej go rozwijać lub sprawdzić ten link, aby zobaczyć więcej przykładów serwerów MCP opartych na Rust: [Przykłady serwerów MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rozwiązanie

**Folder z rozwiązaniami** zawiera kompletne, gotowe do uruchomienia implementacje klientów demonstrujące wszystkie koncepcje omówione w tym samouczku. Każde rozwiązanie zawiera kod klienta i serwera zorganizowany w oddzielnych, niezależnych projektach.

### 📁 Struktura rozwiązania

Katalog rozwiązania jest zorganizowany według języków programowania:

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

Każde rozwiązanie specyficzne dla danego języka zawiera:

- **Kompletną implementację klienta** ze wszystkimi funkcjami z tutorialu
- **Działającą strukturę projektu** z odpowiednimi zależnościami i konfiguracją
- **Skrypty budowania i uruchamiania** dla łatwej konfiguracji i wykonania
- **Szczegółowy plik README** z instrukcjami specyficznymi dla języka
- **Obsługę błędów** i przykłady przetwarzania wyników

### 📖 Korzystanie z rozwiązań

1. **Przejdź do wybranego folderu języka**:

   ```bash
   cd solution/typescript/    # Dla TypeScript
   cd solution/java/          # Dla Java
   cd solution/python/        # Dla Pythona
   cd solution/dotnet/        # Dla .NET
   ```

2. **Postępuj zgodnie z instrukcjami README** w każdym folderze dotyczącymi:
   - Instalacji zależności
   - Budowania projektu
   - Uruchamiania klienta

3. **Przykładowy wynik**, który powinieneś zobaczyć:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pełna dokumentacja oraz instrukcje krok po kroku dostępne są pod adresem: **[📖 Dokumentacja rozwiązania](./solution/README.md)**

## 🎯 Kompleksowe przykłady

Udostępniliśmy kompletne, działające implementacje klientów dla wszystkich języków programowania omawianych w tym tutorialu. Te przykłady demonstrują pełną opisaną powyżej funkcjonalność i mogą służyć jako odniesienia lub punkty startowe do własnych projektów.

### Dostępne kompletne przykłady

| Język    | Plik                            | Opis                                                        |
|----------|--------------------------------|-------------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)         | Kompletny klient Java używający transportu SSE z pełną obsługą błędów |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)         | Kompletny klient C# używający transportu stdio z automatycznym uruchamianiem serwera |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletny klient TypeScript z pełnym wsparciem protokołu MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)         | Kompletny klient Python używający wzorców async/await         |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)             | Kompletny klient Rust używający Tokio do operacji asynchronicznych |

Każdy kompletny przykład zawiera:
- ✅ **Nawiązywanie połączenia** i obsługa błędów  
- ✅ **Odnajdywanie serwera** (narzędzia, zasoby, podpowiedzi tam, gdzie to możliwe)  
- ✅ **Operacje kalkulatora** (dodawanie, odejmowanie, mnożenie, dzielenie, pomoc)  
- ✅ **Przetwarzanie wyników** i formatowany output  
- ✅ **Kompleksowa obsługa błędów**  
- ✅ **Czysty, udokumentowany kod** z komentarzami krok po kroku  

### Rozpoczęcie pracy z kompletnymi przykładami

1. **Wybierz preferowany język** z powyższej tabeli  
2. **Przejrzyj kompletny plik przykładowy**, aby zrozumieć pełną implementację  
3. **Uruchom przykład** zgodnie z instrukcjami w [`complete_examples.md`](./complete_examples.md)  
4. **Modyfikuj i rozszerzaj** przykład, dostosowując go do własnych zastosowań  

Po szczegółową dokumentację dotyczącą uruchamiania i dostosowywania tych przykładów zajrzyj do: **[📖 Dokumentacja Kompletnych Przykładów](./complete_examples.md)**  

### 💡 Rozwiązanie vs. Kompletnie Przykłady

| **Folder z rozwiązaniem** | **Kompletne przykłady**               |
|---------------------------|-------------------------------------|
| Pełna struktura projektu z plikami build | Implementacje w pojedynczych plikach        |
| Gotowe do uruchomienia z zależnościami  | Skupione przykłady kodu                       |
| Środowisko produkcyjne                   | Materiał edukacyjny, punkt odniesienia        |
| Narzędzia specyficzne dla języka         | Porównanie międzyjęzykowe                      |

Oba podejścia są wartościowe – używaj **folderu z rozwiązaniem** dla pełnych projektów, a **kompletnych przykładów** do nauki i odniesienia.  

## Kluczowe Wnioski

Kluczowe wnioski z tego rozdziału dotyczące klientów to:  

- Mogą być używane zarówno do odnajdowania, jak i wywoływania funkcji na serwerze.  
- Klient może uruchomić serwer wraz z samym sobą (jak w tym rozdziale), ale klienci mogą też łączyć się z już działającymi serwerami.  
- To świetny sposób na testowanie możliwości serwera, obok innych narzędzi takich jak Inspector, opisanych w poprzednim rozdziale.  

## Dodatkowe Zasoby

- [Budowanie klientów w MCP](https://modelcontextprotocol.io/quickstart/client)  

## Przykłady

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## Co dalej

- Następny: [Tworzenie klienta z LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku należy traktować jako źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->