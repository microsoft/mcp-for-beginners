from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint

import uvicorn

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"-> Received {request.method} {request.url}")
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response

class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(f"Hello, world!")

routes = [
    Route("/", Homepage),
]

middleware = [
    Middleware(CustomHeaderMiddleware)
]

app = Starlette(routes=routes, middleware=[])
app.add_middleware(CustomHeaderMiddleware)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000
    )