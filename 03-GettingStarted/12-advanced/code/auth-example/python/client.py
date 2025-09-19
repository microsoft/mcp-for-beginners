import base64
import hashlib
import secrets
import threading
import time
import urllib.parse
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

# Config
AUTH_SERVER = "http://localhost:8001"            # auth server base URL (dev)
CALLBACK_PORT = 8003
REDIRECT_URI = f"http://localhost:{CALLBACK_PORT}/callback"
CLIENT_ID = "client123"                          # public client id for demo
AUTHORIZE_PATH = "/authorize"
TOKEN_PATH = "/token"
USERINFO_PATH = "/userinfo"
REVOKE_PATH = "/revoke"

# PKCE helpers
def generate_code_verifier(length=64):
    return secrets.token_urlsafe(length)[:128]

def code_challenge_from_verifier(verifier: str) -> str:
    digest = hashlib.sha256(verifier.encode("ascii")).digest()
    return base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")

# Simple local callback server to catch redirect with ?code=...
class CallbackHandler(BaseHTTPRequestHandler):
    server_version = "CallbackHTTP/1.0"
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/callback":
            self.send_response(404)
            self.end_headers()
            return
        qs = urllib.parse.parse_qs(parsed.query)
        # store values in server.shared
        self.server.shared["code"] = qs.get("code", [None])[0]
        self.server.shared["state"] = qs.get("state", [None])[0]
        # respond to browser
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h2>Authorization received. You can close this window.</h2></body></html>")
        # politely shutdown the server after handling request
        def shutdown_later(srv=self.server):
            time.sleep(0.1)
            srv.shutdown()
        threading.Thread(target=shutdown_later, daemon=True).start()

def run_callback_server(shared, port=CALLBACK_PORT):
    httpd = HTTPServer(("localhost", port), CallbackHandler)
    httpd.shared = shared
    httpd.allow_reuse_address = True
    httpd.serve_forever()

def main():
    # 1) Build PKCE and state
    code_verifier = generate_code_verifier()
    code_challenge = code_challenge_from_verifier(code_verifier)
    state = secrets.token_urlsafe(16)

    # 2) Start callback server
    shared = {}
    srv_thread = threading.Thread(target=run_callback_server, args=(shared,), daemon=True)
    srv_thread.start()

    # 3) Build authorization URL and open browser
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "openid profile",
        "state": state,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }
    auth_url = f"{AUTH_SERVER}{AUTHORIZE_PATH}?{urllib.parse.urlencode(params)}"
    print("Open this URL in a browser to authorize the client:")
    print(auth_url)
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass

    # 4) Wait for callback with code
    for _ in range(120):  # wait up to ~60s
        if "code" in shared:
            break
        time.sleep(0.5)
    code = shared.get("code")
    returned_state = shared.get("state")
    if not code or returned_state != state:
        print("Authorization failed or timed out.")
        return
    print("Authorization code received:", code)

    # 5) Exchange code for tokens (public client uses client_id + PKCE)
    token_url = f"{AUTH_SERVER}{TOKEN_PATH}"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "code_verifier": code_verifier,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(token_url, data=data, headers=headers, timeout=10)
    resp.raise_for_status()
    tokens = resp.json()
    print("Token response:", tokens)

    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")

    # 6) Call a protected resource / userinfo
    if access_token:
        ui_resp = requests.get(f"{AUTH_SERVER}{USERINFO_PATH}", headers={"Authorization": f"Bearer {access_token}"}, timeout=10)
        print("Userinfo status:", ui_resp.status_code, "body:", ui_resp.text)

    # 7) (Optional) Use refresh token to get new access token
    if refresh_token:
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": CLIENT_ID,
        }
        r = requests.post(token_url, data=data, headers=headers, timeout=10)
        print("Refresh token response:", r.status_code, r.text)

    # 8) (Optional) Revoke tokens
    if access_token:
        revoke_url = f"{AUTH_SERVER}{REVOKE_PATH}"
        revoke_data = {"token": access_token, "token_type_hint": "access_token", "client_id": CLIENT_ID}
        r = requests.post(revoke_url, data=revoke_data, headers=headers, timeout=10)
        print("Revocation response:", r.status_code)

if __name__ == "__main__":
    main()