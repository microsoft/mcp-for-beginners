# server.py
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from mcp.server.fastmcp import FastMCP, Context 
from mcp.types import (
    TextContent
)
import asyncio
import uvicorn
import os

# Create an MCP server
mcp = FastMCP("Streamable DEMO")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    html_path = os.path.join(os.path.dirname(__file__), "welcome.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

async def event_stream(message: str):
    for i in range(1, 4):
        yield f"Processing file {i}/3...\n"
        await asyncio.sleep(1)
    yield f"Here's the file content: {message}\n"

@app.get("/stream")
async def stream(message: str = "hello"):
    return StreamingResponse(event_stream(message), media_type="text/plain")

@mcp.tool(description="A tool that simulates file processing and sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    files = [f"file_{i}.txt" for i in range(1, 4)]
    for idx, file in enumerate(files, 1):
        await ctx.info(f"Processing {file} ({idx}/{len(files)})...")
        await asyncio.sleep(1)  
    await ctx.info("All files processed!")
    return TextContent(type="text", text=f"Processed files: {', '.join(files)} | Message: {message}")

if __name__ == "__main__":
    import sys
    if "mcp" in sys.argv:
        # Configure MCP server with streamable-http transport
        print("Starting MCP server with streamable-http transport...")
        # MCP server will create its own FastAPI app with the /mcp endpoint
        mcp.run(transport="streamable-http")
    else:
        # Start FastAPI app for classic HTTP streaming
        print("Starting FastAPI server for classic HTTP streaming...")
        uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
