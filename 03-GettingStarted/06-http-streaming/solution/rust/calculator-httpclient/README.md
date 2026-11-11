# Running this sample

## -1- Run the Streamable HTTP server

Open a terminal from the root of this project and run the following commands:

```bash
cd ../calculator-httpserver
cargo run
```

Keep this terminal open as it will run the HTTP server that the client will connect to. Open a new terminal for the next steps.

## -2- Install the dependencies and build the project

```bash
cargo build
```

## -3- Run the sample

```bash
cargo run
```

You should see output similar to:

```text
🔗 Connected to server:
   Name: rmcp
   Version: 2.2.0
   Protocol: ProtocolVersion("2025-11-25")
   Instructions: A simple calculator tool
   Capabilities:
   • Tools support enabled
📋 Available tools: 1
   • add - Adds a and b

🧮 Calculating 3 + 2...
✅ Result: 5
```
