# Running this sample

You need a recent Rust toolchain (edition 2024, Rust 1.85 or later), see [rustup](https://rustup.rs/). To test the server you also need [Node.js](https://nodejs.org/) for `npx`.

## -1- Install the dependencies and build the project

```bash
cargo build
```

## -2- Run the sample

```bash
cargo run
```

The server uses the stdio transport, so it prints nothing and waits for a client on stdin. Press `Ctrl+C` to stop it.

## -3- Test the sample

The inspector starts its own copy of the server, so you don't need to keep the one from step 2 running.

To list the tools run:

```bash
npx @modelcontextprotocol/inspector --cli cargo run --method tools/list
```

You should see the `add` tool with its `a` and `b` number parameters.

To invoke the tool run:

```bash
npx @modelcontextprotocol/inspector --cli cargo run --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

You should see the following output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

To use the visual interface instead, run `npx @modelcontextprotocol/inspector cargo run`, connect, then list tools and run `add`.
