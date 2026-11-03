# Sampling in Model Context Protocol

> [!WARNING]
> **Sampling is deprecated as of MCP `2026-07-28`**
> ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577)).
>
> - **What is deprecated:** the Sampling client feature, meaning the
>   `sampling` client capability and the `sampling/createMessage` request a
>   server sends to borrow the client's LLM. The `includeContext` values
>   `"thisServer"` and `"allServers"` were already deprecated in `2025-11-25`.
> - **What to use instead:** integrate your server directly with an LLM
>   provider API, as listed in the official
>   [Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
>   registry. The generation parameters in this lesson (temperature, top-p,
>   seed, and so on) carry over unchanged; see
>   [Recommended replacement: tune the LLM call directly](#recommended-replacement-tune-the-llm-call-directly).
> - **Why this lesson is kept:** existing servers and clients still use
>   Sampling over `2025-11-25` connections, and you may need to maintain or
>   migrate them. The feature stays in the specification for compatibility
>   and is eligible for removal in the first revision released on or after
>   July 28, 2027.
> - **What the SDK does today:** with MCP Python SDK 2.3.0,
>   `ctx.session.create_message(...)` works only on connections that used the
>   `2025-11-25` `initialize` handshake. On a `2026-07-28` connection it raises
>   `NoBackChannelError`, and every call emits an `MCPDeprecationWarning`.
>
> See [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)
> for the full picture.

In legacy MCP implementations, Sampling allows servers to request LLM
completions through the client. This lesson explains that deprecated protocol
flow for compatibility and migration work, and shows how to tune the same
generation parameters when your server calls an LLM directly.

## Introduction

In this lesson, we will explore how to configure sampling parameters in MCP requests and understand the underlying protocol mechanics of sampling.

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand the key sampling parameters available in MCP.
- Configure sampling parameters for different use cases.
- Implement deterministic sampling for reproducible results.
- Dynamically adjust sampling parameters based on context and user preferences.
- Understand how sampling works in the client-server flow of MCP.
- Move the same parameter choices to a direct LLM provider call, the
  replacement recommended for new servers.

## How Sampling Works in MCP

The sampling flow in MCP follows these steps:

1. Server sends a `sampling/createMessage` request to the client
2. Client reviews the request and can modify it
3. Client samples from an LLM
4. Client reviews the completion
5. Client returns the result to the server

This human-in-the-loop design ensures users maintain control over what the LLM sees and generates.

Note the direction: the **server** asks and the **client** answers. The server
can only *request* parameters such as `temperature`; the client decides which
model to use and which parameters to honor.

## Sampling Parameters Overview

A `sampling/createMessage` request can carry the following parameters:

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `messages` | The conversation to send to the LLM (required) | Array of messages |
| `maxTokens` | Maximum number of tokens to generate (required) | Integer value |
| `systemPrompt` | System prompt the server asks the client to use | String |
| `temperature` | Controls randomness in token selection | 0.0 - 1.0 |
| `stopSequences` | Custom sequences that stop generation when encountered | Array of strings |
| `modelPreferences` | Model name hints and cost, speed, and intelligence priorities | Priorities 0.0 - 1.0 |
| `includeContext` | Whether to include MCP context; only `"none"` is not deprecated | `"none"` |
| `metadata` | Additional provider-specific parameters | JSON object |

Many LLM providers support additional parameters. A server can pass them in the
`metadata` field, but the client is free to ignore them:

| Common Extension Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - limits tokens to top cumulative probability | 0.0 - 1.0 |
| `top_k` | Limits token selection to top K options | 1 - 100 |
| `presence_penalty` | Penalizes tokens based on their presence in the text so far | -2.0 - 2.0 |
| `frequency_penalty` | Penalizes tokens based on their frequency in the text so far | -2.0 - 2.0 |
| `seed` | Specific random seed for reproducible results | Integer value |

## Example Request Format

Here's an example of a server requesting sampling from a client in MCP:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "none",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## Response Format

The client returns a completion result:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "The current directory contains README.md and server.py."
    },
    "model": "gpt-5.1",
    "stopReason": "endTurn"
  }
}
```

`model` is the name of the model the client actually used. `stopReason` is
usually `"endTurn"`, `"stopSequence"`, or `"maxTokens"`, but clients may return
other values.

## Human in the Loop Controls

MCP sampling is designed with human oversight in mind:

- **For prompts**:
  - Clients should show users the proposed prompt
  - Users should be able to modify or reject prompts
  - System prompts can be filtered or modified
  - Context inclusion is controlled by the client

- **For completions**:
  - Clients should show users the completion
  - Users should be able to modify or reject completions
  - Clients can filter or modify completions
  - Users control which model is used

## Security Considerations

When implementing sampling in MCP, consider these security best practices:

- **Validate all message content** before sending it to the client
- **Sanitize sensitive information** from prompts and completions
- **Implement rate limits** to prevent abuse
- **Monitor sampling usage** for unusual patterns
- **Encrypt data in transit** using secure protocols
- **Handle user data privacy** according to relevant regulations
- **Audit sampling requests** for compliance and security
- **Control cost exposure** with appropriate limits
- **Implement timeouts** for sampling requests
- **Handle model errors gracefully** with appropriate fallbacks

These practices still apply when you replace Sampling with a direct LLM call.
The difference is that your server, not the client, is now responsible for
them.

## Configuring Sampling Parameters (Legacy)

Sampling parameters allow fine-tuning the behavior of language models to achieve the desired balance between deterministic and creative outputs.

The examples below use the MCP Python SDK (`mcp>=2.3.0,<3`). They only work
when the client connects with the `2025-11-25` `initialize` handshake.

> [!NOTE]
> Earlier versions of this lesson showed .NET, JavaScript, and Java snippets
> built on classes such as `McpClient`, `SamplingParameters`, and an
> `@mcp/client` package. Those APIs don't exist in the official MCP SDKs, and
> the snippets had the client sending sampling parameters to the server, which
> is the reverse of how Sampling works. They have been replaced with the
> runnable Python examples below.

### Server: request specific parameters

The server picks the parameters when it calls `create_message`. Here a
brainstorming tool asks for a creative (high temperature) completion:

```python
from mcp.server.mcpserver import Context, MCPServer
from mcp.types import ModelHint, ModelPreferences, SamplingMessage, TextContent

mcp = MCPServer("Sampling parameters demo")


@mcp.tool()
async def brainstorm(topic: str, ctx: Context) -> str:
    """Brainstorm ideas about a topic with the client's LLM (legacy Sampling)."""
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=f"List three ideas about {topic}."),
            )
        ],
        system_prompt="You are a creative assistant.",
        max_tokens=200,                 # required
        temperature=0.9,                # higher = more creative
        stop_sequences=["\n\n\n"],      # stop at a long blank gap
        include_context="none",         # "thisServer"/"allServers" are deprecated
        model_preferences=ModelPreferences(
            hints=[ModelHint(name="gpt-5.1")],
            intelligence_priority=0.6,
            speed_priority=0.4,
        ),
        metadata={"top_p": 0.95, "frequency_penalty": 0.5},  # provider-specific extras
    )
    return result.content.text


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

In the preceding code we've:

- Used `temperature=0.9` to ask for more varied, creative output.
- Used `stop_sequences` to end generation early at a long blank gap.
- Set `include_context="none"`, the only value that isn't deprecated.
- Used `model_preferences` to hint at a model and say that quality matters a
  bit more than speed. These are hints; the client chooses the model.
- Put `top_p` and `frequency_penalty` in `metadata`, because they aren't
  standard Sampling fields.

### Client: honor the parameters

The client receives these values in its sampling callback and decides which
ones to pass to its LLM. This client uses Azure OpenAI through the OpenAI SDK:

```python
import asyncio
import os

from openai import AsyncOpenAI

from mcp import ClientSession, types
from mcp.client.context import ClientRequestContext
from mcp.client.streamable_http import streamable_http_client

llm = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1")


async def handle_sampling(
    context: ClientRequestContext, params: types.CreateMessageRequestParams
) -> types.CreateMessageResult:
    # A real host would show the request to the user for approval here.
    messages = [{"role": m.role, "content": m.content.text} for m in params.messages]
    if params.system_prompt:
        messages.insert(0, {"role": "system", "content": params.system_prompt})

    # The server's values are requests, not orders: only pass what your model supports.
    options = {"max_completion_tokens": params.max_tokens}
    if params.temperature is not None:
        options["temperature"] = params.temperature
    if params.stop_sequences:
        options["stop"] = params.stop_sequences
    extras = params.metadata or {}
    for key in ("top_p", "frequency_penalty", "presence_penalty", "seed"):
        if key in extras:
            options[key] = extras[key]

    response = await llm.chat.completions.create(model=DEPLOYMENT, messages=messages, **options)

    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(type="text", text=response.choices[0].message.content),
        model=DEPLOYMENT,
        stop_reason="endTurn",
    )


async def main():
    async with streamable_http_client("http://localhost:8000/mcp") as (read, write):
        async with ClientSession(read, write, sampling_callback=handle_sampling) as session:
            await session.initialize()  # Sampling needs the 2025-11-25 handshake
            result = await session.call_tool("brainstorm", arguments={"topic": "city transport"})
            print(result.content[0].text)


asyncio.run(main())
```

In the preceding code we've:

- Registered `handle_sampling` as the `sampling_callback`, which also tells the
  server that this client supports Sampling.
- Called `session.initialize()`, because Sampling only works over the
  `2025-11-25` handshake.
- Translated the MCP parameters into OpenAI parameters, copying only the
  values that were actually sent.
- Returned the completion, including the name of the model that was used.

Run the server with `python server.py`, then run the client in a second
terminal. The server prints an `MCPDeprecationWarning` when it calls
`create_message`; that's expected.

---

## Deterministic Sampling

For applications requiring consistent outputs, deterministic sampling makes
results as reproducible as possible. You get there by setting the temperature
to zero and, where the provider supports it, using a fixed random seed. Even
then, most providers only promise *mostly* reproducible results.

With Sampling, the server can only ask for this. It sets `temperature=0` and
passes a seed in `metadata`, and the client may ignore both:

```python
result = await ctx.session.create_message(
    messages=[SamplingMessage(role="user", content=TextContent(type="text", text=prompt))],
    max_tokens=100,
    temperature=0.0,
    metadata={"seed": 12345},
)
```

When the server calls the LLM itself, it controls these values directly. See
the `"deterministic"` preset in the next sections.

---

## Dynamic Sampling Configuration

Intelligent sampling adapts parameters based on the context and requirements of each request. That means dynamically adjusting parameters like temperature, top_p, and penalties based on the task type, user preferences, or historical performance.

The selection logic is plain Python and works the same with Sampling or with a
direct LLM call:

```python
PRESETS = {
    "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
    "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
    "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
    "deterministic": {"temperature": 0.0, "seed": 12345},
}


def choose_sampling_params(task_type: str, creativity: int | None = None) -> dict:
    """Pick generation parameters for a task; creativity is 1-10."""
    params = dict(PRESETS.get(task_type, PRESETS["factual"]))
    if creativity is not None:
        creativity = min(max(creativity, 1), 10) / 10
        params["temperature"] = round(0.1 + 0.9 * creativity, 2)
    return params
```

In the preceding code we've:

- Defined presets for different task types (creative, factual, code,
  deterministic).
- Fallen back to the `factual` preset for unknown task types.
- Scaled the temperature from a 1-10 `creativity` preference, clamped with
  `min` and `max` so invalid values can't produce an invalid configuration.

With legacy Sampling, you would pass `temperature` to `create_message` and put
the other values in `metadata`. The next section shows the recommended way:
passing them straight to the LLM provider.

---

## Recommended replacement: tune the LLM call directly

For new servers, the specification recommends integrating directly with an LLM
provider API instead of using Sampling. Everything you learned about generation
parameters still applies; you just pass them to the provider yourself.

This server combines the presets above with a direct call to Azure OpenAI:

```python
import os

from openai import AsyncOpenAI

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Writing assistant")

llm = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1")

# PRESETS and choose_sampling_params from the previous section go here


@mcp.tool()
async def write(prompt: str, task_type: str = "factual", creativity: int | None = None) -> str:
    """Generate text, tuning the LLM's parameters to the kind of task."""
    params = choose_sampling_params(task_type, creativity)
    response = await llm.chat.completions.create(
        model=DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=300,
        **params,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

In the preceding code we've:

- Created the LLM client once, when the server starts.
- Picked the parameters with `choose_sampling_params`, including the
  `deterministic` preset (`temperature=0`, fixed `seed`).
- Passed the parameters directly to `chat.completions.create`, so they are
  always applied instead of being a request the client may ignore.
- Kept the tool free of any `ctx` usage, so it works for every client and
  every protocol version, including `2026-07-28`.

Before you migrate, check which parameters your chosen model supports. Some
models, especially reasoning models, reject or ignore `temperature`, `top_p`,
or penalty values.

For a beginner-level walkthrough of the same migration, see
[Lesson 3.14 Sampling](../../03-GettingStarted/14-sampling/README.md#recommended-replacement-call-the-llm-provider-directly).

## Key Takeaways

- Sampling lets a server ask the client's LLM for a completion and request
  parameters such as `temperature`, `stopSequences`, and `modelPreferences`.
  The client decides what to honor.
- Sampling is deprecated as of MCP `2026-07-28`. Keep it only for existing
  `2025-11-25` servers and clients.
- New servers should call an LLM provider directly. The same parameter
  choices (temperature, top-p, seed, penalties) carry over unchanged.

## What's next

- [5.7 Scaling](../mcp-scaling/README.md)
