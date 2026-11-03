# Running this sample

> [!WARNING]
> This solution uses Sampling (`sampling/createMessage`), which is deprecated
> as of MCP `2026-07-28`. New servers should integrate directly with an LLM
> provider API instead; see the
> [Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
> registry and the
> [recommended replacement](../../README.md#recommended-replacement-call-the-llm-provider-directly)
> in this lesson. The sample is kept because existing servers and clients still
> use Sampling over `2025-11-25` connections. That's why `client.py` calls
> `session.initialize()`: on a `2026-07-28` connection the server can't send
> sampling requests and the tool call fails with `NoBackChannelError`.

The sample has two parts:

- `server.py` is an MCP server that uses the Streamable HTTP transport on
  `http://localhost:8000/mcp`. Its `create_product` tool asks the client's LLM
  for a product description.
- `client.py` connects to the server, handles the sampling request by calling
  Azure OpenAI, and prints the result.

You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

## -1- Activate the virtual environment

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]>=2.3.0,<3" "openai>=3.44.0,<4"
```

## -3- Start the server

In one terminal, with the virtual environment activated:

```bash
python server.py
```

## -4- Run the client

In a second terminal, activate the virtual environment, set your Azure OpenAI
settings, and run the client:

```bash
export AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<your-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"  # optional

python client.py
```

On Windows PowerShell, set the variables with `$env:AZURE_OPENAI_ENDPOINT = "..."`.

The client prints the sampling request it received, then the tool results:

```text
Sampling request: [SamplingMessage(role='user', content=TextContent(type='text', text='Create a product description about paprika described by as red, juicy, vegetable', annotations=None, meta=None), meta=None)]
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. ..."}
result: [{"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\n..."}]
```

The server terminal shows an `MCPDeprecationWarning` for the `create_message`
call. That's expected, because Sampling is deprecated.
