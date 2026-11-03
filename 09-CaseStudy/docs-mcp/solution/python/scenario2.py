# Scenario 2: Integrate Docs MCP into a web development project
# This script demonstrates how to use Chainlit to build a conversational web app
# that queries the Microsoft Learn Docs MCP server.

import chainlit as cl
import logging
import json
from mcp.client.streamable_http import streamable_http_client
from mcp import ClientSession

from semantic_kernel.kernel import Kernel
from azure.core.credentials import AzureKeyCredential
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions import kernel_function
from semantic_kernel.agents import ChatCompletionAgent


MCP_SERVER_URL = "https://learn.microsoft.com/api/mcp"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('mcp_client')

# MCP Docs Plugin as a Semantic Kernel plugin
class MCPDocsPlugin:
    def __init__(self, mcp_server_url):
        self.mcp_server_url = mcp_server_url

    @kernel_function(name="search_docs", description="Search Microsoft Docs using MCP")
    async def search_docs(self, question: str) -> str:
        async with streamable_http_client(self.mcp_server_url) as (read_stream, write_stream, _):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                result = await session.call_tool("microsoft_docs_search", {"query": question})
                output = []
                if hasattr(result, 'content'):
                    for item in result.content:
                        try:
                            data = json.loads(item.text)
                            # The Docs MCP server returns {"results": [...]}
                            my_list = data.get("results", []) if isinstance(data, dict) else data
                            for doc in my_list:
                                title = doc.get('title', 'No title')
                                content = doc.get('content', 'No content')
                                output.append(f"**{title}**\n{content}")
                        except Exception:
                            output.append(item.text)
                    return "\n".join(output)
                else:
                    return "No content returned from the search."

# Register the MCP Docs search as a function
async def mcp_docs_search(question: str):
    async with streamable_http_client(MCP_SERVER_URL) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("microsoft_docs_search", {"query": question})
            output = []
            if hasattr(result, 'content'):
                for item in result.content:
                    try:
                        data = json.loads(item.text)
                        # The Docs MCP server returns {"results": [...]}
                        my_list = data.get("results", []) if isinstance(data, dict) else data
                        for doc in my_list:
                            title = doc.get('title', 'No title')
                            content = doc.get('content', 'No content')
                            output.append(f"**{title}**\n{content}")
                    except Exception:
                        output.append(item.text)
                return "\n".join(output)
            else:
                return "No content returned from the search."

@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome! Enter your Microsoft Docs search query below.").send()
    kernel = Kernel()
    service_id = "agent"
    kernel.add_service(AzureChatCompletion(service_id=service_id))
    from semantic_kernel.connectors.ai import FunctionChoiceBehavior
    settings = kernel.get_prompt_execution_settings_from_service_id(service_id=service_id)
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
    # Register the MCPDocsPlugin
    mcp_plugin = MCPDocsPlugin(MCP_SERVER_URL)
    kernel.add_plugin(mcp_plugin, plugin_name="MCPDocs")
    # Create the agent
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="DocsAgent",
        instructions="You are a helpful assistant that uses the MCPDocs plugin to answer Microsoft Docs questions. Format your answers clearly.",
        plugins=[mcp_plugin]
    )
    cl.user_session.set("kernel", kernel)
    cl.user_session.set("agent", agent)
    cl.user_session.set("settings", settings)

@cl.on_message
async def handle_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    user_query = message.content.strip()
    if not user_query:
        await cl.Message(content="Query cannot be empty. Please try again.").send()
        return
    answer = cl.Message(content="Processing your request...")
    await answer.send()
    try:
        response_printed = False
        async for content in agent.invoke(user_query):
            msg = content.content
            if hasattr(msg, "content"):
                msg = msg.content
            if msg:
                await answer.stream_token(str(msg))
                response_printed = True
        if not response_printed:
            await answer.stream_token("No response generated by the agent.\n")
        await answer.update()
    except Exception as e:
        await answer.stream_token(f"\n\n❌ Error: {str(e)}\n\n")
        await answer.update()
