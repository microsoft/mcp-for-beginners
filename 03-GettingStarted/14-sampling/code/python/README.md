# Run the sample

> [!WARNING]
> `server.py` uses Sampling (`sampling/createMessage`), which is deprecated as
> of MCP `2026-07-28`. The official
> [Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
> registry recommends integrating directly with an LLM provider API instead,
> which is what `server_direct_llm.py` does. `server.py` is kept because
> existing clients still use Sampling over `2025-11-25` connections. It works
> only for clients that use the `2025-11-25` `initialize` handshake; on a
> `2026-07-28` connection the tool call fails with `NoBackChannelError`.

## Create virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Install dependencies

```sh
pip install "mcp[cli]>=2.3.0,<3"
```

## Run the server

The server uses the Streamable HTTP transport and listens on `http://localhost:8000/mcp`:

```sh
python server.py
```

## Test the server out with GitHub Copilot and VS Code

Add the entry to mcp.json like so:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8000/mcp",
        "type": "http"
    }
}
```

Make sure you click "start" on the server.

In GitHub Copilot paste the following prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

The first time you will be asked whether to accept a Sampling action, then you will be asked to accept the tool to run "create_blog". You should see a response similar to:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

The server terminal also shows an `MCPDeprecationWarning` for the
`create_message` call. That's expected.

## Run the recommended replacement (no Sampling)

`server_direct_llm.py` exposes the same `create_blog` tool, but calls Azure
OpenAI itself instead of asking the client's LLM. It works with any client and
protocol version.

```sh
pip install "openai>=3.44.0,<4"
export AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<your-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"  # optional
python server_direct_llm.py
```

It also listens on `http://localhost:8000/mcp`, so stop `server.py` first. Use
the same `mcp.json` entry and prompt as above. This time there is no Sampling
dialog, only the normal dialog asking you to run the tool.
