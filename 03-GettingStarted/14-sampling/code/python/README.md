# Run the sample

> [!WARNING]
> This sample uses deprecated Sampling. It is retained for MCP `2025-11-25`
> compatibility. New implementations should call an LLM provider directly.

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