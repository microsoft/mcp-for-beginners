# Running this sample

## -1- Install the dependencies and build the project

```bash
cargo build
```

## -2- Run the sample

```bash
cargo run
```

The server listens on `http://127.0.0.1:8000` and serves MCP over Streamable HTTP at `/mcp`. You can test it with the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:8000/mcp --method tools/call --tool-name add --tool-arg a=2 --tool-arg b=4
```
