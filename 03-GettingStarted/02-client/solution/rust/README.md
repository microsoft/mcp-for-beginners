# Running this sample

> [!NOTE]
> This Rust client starts the .NET sample MCP server in the [server](../server/) directory (a sibling of this project) with `dotnet run`, so you need the [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) as well as a recent Rust toolchain (edition 2024, Rust 1.85 or later).

## -1- Install the dependencies and build the project

```bash
cargo build
```

## -2- Run the sample

```bash
cargo run
```

You don't need to start the server yourself. You should see output similar to the following (the server's log messages on stderr are printed as well):

```text
🔗 Connected to server:
   Name: server
   Version: 1.0.0.0
   Protocol: ProtocolVersion("2025-11-25")
   Capabilities:
   • Tools support enabled
   • Logging support enabled
📋 Available tools: 1
   • add - Adds two numbers

🧮 Calculating 3 + 2...
✅ Result: Sum 5
```
