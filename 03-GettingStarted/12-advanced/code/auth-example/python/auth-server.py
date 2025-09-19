from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from typing import Optional
from urllib.parse import urlencode
import uvicorn

# /workspaces/mcp-for-beginners/03-GettingStarted/12-advanced/code/auth-example/python/auth-server.py

app = FastAPI(title="Minimal Auth Example")

@app.post("/introspect")
async def introspect(token: str):
    """
    Very small /introspect endpoint.
    Accepts a token query parameter and returns a minimal introspection response.
    """
    print(f"Introspection request received for token: {token}")

    if token == "access-token-xyz":
        return {
            "active": True,
            "scope": "mcp:read",
            "client_id": "client-123",
            "username": "user-456",
            "token_type": "Bearer",
            "exp": 9999999999,
            "iat": 1111111111,
            "nbf": 1111111111,
            "sub": "user-456",
            "aud": "http://localhost:8000",
            "iss": "http://localhost:8001",
            "jti": "unique-token-id-789"
        }

@app.get("/authorize")
async def authorize(response_type: Optional[str] = None,
                    client_id: Optional[str] = None,
                    redirect_uri: Optional[str] = None,
                    state: Optional[str] = None):
    """
    Very small /authorize endpoint.
    If redirect_uri is provided it redirects back with a dummy code and optional state.
    Otherwise it returns a tiny JSON payload.
    """
    print("Authorize request received")

    code = "authcode-123"
    if redirect_uri:
        params = {"code": code}
        if state:
            params["state"] = state
        url = f"{redirect_uri}?{urlencode(params)}"
        return RedirectResponse(url=url)
    return JSONResponse({"code": code, "state": state})


@app.post("/token")
async def token(grant_type: str = Form(...),
                code: Optional[str] = Form(None),
                redirect_uri: Optional[str] = Form(None),
                client_id: Optional[str] = Form(None),
                client_secret: Optional[str] = Form(None)):
    """
    Very small /token endpoint.
    Accepts form-encoded params and returns a minimal access token response.
    """
    print("Token request received")

    if grant_type != "authorization_code":
        raise HTTPException(status_code=400, detail="unsupported_grant_type")
    if not code:
        raise HTTPException(status_code=400, detail="invalid_request")
    # In a real server you would validate the code, client_id, client_secret, etc.
    return JSONResponse({
        "access_token": "access-token-xyz",
        "token_type": "Bearer",
        "expires_in": 3600
    })

port = 8001

if __name__ == "__main__":
    print(f"Starting Auth server on http://localhost:{port}")
    uvicorn.run("auth-server:app", host="0.0.0.0", port=port, log_level="info")