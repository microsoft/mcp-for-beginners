# client.py
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio
import mcp.types as types
from mcp.shared.session import RequestResponder
import requests
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")
if not token:
    print("TOKEN not found in .env file, run util.py to generate one.")
    raise ValueError("TOKEN not found in .env file")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('mcp_client')

class LoggingCollector:
    def __init__(self):
        self.log_messages: list[types.LoggingMessageNotificationParams] = []
    async def __call__(self, params: types.LoggingMessageNotificationParams) -> None:
        self.log_messages.append(params)
        logger.info("MCP Log: %s - %s", params.level, params.data)

logging_collector = LoggingCollector()
port = 8000

async def message_handler(
    message: RequestResponder[types.ServerRequest, types.ClientResult]
    | types.ServerNotification
    | Exception,
) -> None:
    logger.info("Received message: %s", message)
    if isinstance(message, Exception):
        logger.error("Exception received!")
        raise message
    elif isinstance(message, types.ServerNotification):
        logger.info("NOTIFICATION: %s", message)
    elif isinstance(message, RequestResponder):
        logger.info("REQUEST_RESPONDER: %s", message)
    else:
        logger.info("SERVER_MESSAGE: %s", message)

async def main():
    logger.info("Starting client...")
    async with streamablehttp_client(
        url = f"http://localhost:{port}/mcp",
        headers = {"Authorization": f"Bearer {token}"}
    ) as (
        read_stream,
        write_stream,
        session_callback,
    ):
        async with ClientSession(
            read_stream,
            write_stream,
            logging_callback=logging_collector,
            message_handler=message_handler
        ) as session:
            id_before = session_callback()
            logger.info("Session ID before init: %s", id_before)
            await session.initialize()
            id_after = session_callback()
            logger.info("Session ID after init: %s", id_after)
            logger.info("Session initialized, ready to call tools.")
            tool_result = await session.call_tool("get_time", {})
            logger.info("Tool result: %s", tool_result)
            if logging_collector.log_messages:
                logger.info("Collected log messages:")
                for log in logging_collector.log_messages:
                    logger.info("Log: %s", log)

def stream_progress(message="hello", url="http://localhost:8000/stream"):
    params = {"message": message}
    logger.info("Connecting to %s with message: %s", url, message)
    try:
        with requests.get(url, params=params, stream=True, timeout=10) as r:
            r.raise_for_status()
            logger.info("--- Streaming Progress ---")
            for line in r.iter_lines():
                if line:
                    # Still print the streamed content to stdout for visibility
                    decoded_line = line.decode().strip()
                    print(decoded_line)
                    logger.debug("Stream content: %s", decoded_line)
            logger.info("--- Stream Ended ---")
    except requests.RequestException as e:
        logger.error("Error during streaming: %s", e)

if __name__ == "__main__":
    import sys

    logger.info("Running MCP client...")
    asyncio.run(main())

        
    # Don't run both by default, let the user choose the mode