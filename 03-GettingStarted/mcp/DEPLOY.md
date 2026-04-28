# Deploying the MCP Server to Kubernetes

The server exposes read-only Oracle database tools and Aria Knowledge Central search over the [MCP streamable-HTTP transport](https://modelcontextprotocol.io/docs/concepts/transports). Once deployed, any developer can point their MCP client at the cluster endpoint and supply their own Oracle credentials per tool call — no shared credentials live in the cluster.

---

## Prerequisites

- Docker (with access to the Aria Artifactory registry)
- `kubectl` configured for the target cluster (VPN required for dev0/dev1)

---

## 1. Build and Push the Docker Image

The Dockerfile downloads Oracle Instant Client 23.6 (Linux x86_64) directly during the build — no manual download needed.

```bash
cd /Users/ansingh/repo/mcp-for-beginners/03-GettingStarted/mcp/app

IMAGE=harbor.dev0.us-east-1.devk8s.ariasystems.net/library/mcp-server:latest

docker build -t $IMAGE .
docker push $IMAGE
```

### Using a different Instant Client version

If you need a specific version, pass both build args together. Find the download URL and extracted directory name for your version at:
https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html

```bash
docker build \
  --build-arg IC_URL=https://download.oracle.com/otn_software/linux/instantclient/2340000/instantclient-basic-linux.x64-23.4.0.24.05.zip \
  --build-arg IC_DIR=instantclient_23_4 \
  -t $IMAGE .
```

> **Note:** Your local copy at `/Users/ansingh/apps/instantclient_23_26` contains macOS `.dylib` files and cannot be used inside a Linux container. The Dockerfile downloads the Linux `.so` build automatically.

---

## 2. Deploy to Kubernetes

```bash
cd /Users/ansingh/repo/mcp-for-beginners/03-GettingStarted/mcp/k8s

bash create-namespace.sh

kubectl apply -f service.yaml
kubectl apply -f deployment.yaml
kubectl apply -f ingress.yaml
```

The MCP endpoint is publicly reachable inside the corporate network at:
```
http://mcp-server.ansingh-apps.dev0.us-east-1.devk8s.ariasystems.net/mcp
```

No port-forward needed. Teams point their `claude_desktop_config.json` directly at this URL.

Verify the pod comes up:

```bash
kubectl get pods -n ansingh-apps -l app=mcp-server
kubectl logs -n ansingh-apps -l app=mcp-server --tail=20
```
Troubleshoot:
```bash
kubectl get pods -n ansingh-apps -l app=mcp-server -o wide
kubectl describe pod -n ansingh-apps -l app=mcp-server
kubectl logs -n ansingh-apps -l app=mcp-server --previous --tail=200
kubectl logs -n ansingh-apps -l app=mcp-server --tail=200
kubectl get events -n ansingh-apps --sort-by=.lastTimestamp | tail -n 30

kubectl rollout restart deployment/mcp-server -n ansingh-apps
kubectl rollout status deployment/mcp-server -n ansingh-apps
kubectl get pods -n ansingh-apps -l app=mcp-server
kubectl get endpoints -n ansingh-apps mcp-server
kubectl logs -n ansingh-apps -l app=mcp-server --tail=80
```

The MCP endpoint is now reachable inside the cluster at:
```
http://mcp-server.ansingh-apps.svc.cluster.local:8000/mcp
```

---

## 3. (Optional) Server-Level Default Oracle Connection

By default the server has **no** hardcoded Oracle credentials — each caller passes their own. If you want a fallback (e.g. a shared read-only service account), uncomment and fill in `k8s/secret.yaml`, then apply it and uncomment the env-var block in `k8s/deployment.yaml`:

```bash
# Edit k8s/secret.yaml — fill in ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN
kubectl apply -n ansingh-apps -f k8s/secret.yaml

# Then uncomment the ORACLE_* env vars in k8s/deployment.yaml and re-apply:
kubectl apply -n ansingh-apps -f k8s/deployment.yaml
```

---

## 4. Developer Setup (connecting your MCP client)

### Claude Desktop

Add the server to `~/Library/Application Support/Claude/claude_desktop_config.json`.

Each team supplies their own Oracle credentials via `--header` flags — credentials never touch the shared server config:

```json
{
  "mcpServers": {
    "aria-oracle-kb": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://mcp-server.ansingh-apps.dev0.us-east-1.devk8s.ariasystems.net/mcp",
        "--header", "x-oracle-user:YOUR_DB_USER",
        "--header", "x-oracle-password:YOUR_DB_PASSWORD",
        "--header", "x-oracle-dsn:YOUR_HOST:1521/YOUR_SERVICE"
      ]
    }
  }
}
```

> **Note:** You must be on the Aria VPN for the cluster hostname to resolve. No port-forward required.

Restart Claude Desktop. The five tools (`list_tables`, `describe_table`, `run_select`, `kb_fetch`, `kb_search`) will appear automatically — no `connection` parameter needed on each call.

### VS Code (GitHub Copilot / MCP extension)

Add to `.vscode/mcp.json` in your workspace (or user settings):

```json
{
  "servers": {
    "aria-oracle-kb": {
      "type": "http",
      "url": "http://mcp-server.ansingh-apps.dev0.us-east-1.devk8s.ariasystems.net/mcp"
    }
  }
}
```

---

## 5. Using the Tools

Once your `claude_desktop_config.json` is configured with `--header` flags, credentials are injected automatically — just ask Claude naturally:

### List your tables
```
list_tables()
list_tables(owner="ARIACORE")
```

### Describe a table
```
describe_table(table_name="ACCT_", owner="ARIACORE")
```

### Run a SELECT
```
run_select(
  sql="SELECT acct_no, status_cd FROM ariacore.acct_ WHERE status_cd = :s",
  binds={"s": 1},
  max_rows=50
)
```

### Override with a different database (optional)
Any tool still accepts an explicit `connection` dict to target a different DB than the one in your headers:
```
run_select(
  sql="SELECT * FROM other_schema.some_table FETCH FIRST 10 ROWS ONLY",
  connection={"user": "other_user", "password": "other_pass", "dsn": "other_host:1521/svc"}
)
```

### Search Knowledge Central (no DB needed)

```
kb_search(query="Aria Billing release 70 notes", max_pages=12)
kb_fetch(url="https://knowledge.ariasystems.net/")
```

---

## 6. Local Development (stdio transport)

Run the server locally without Docker — useful for iterating on tools:

```bash
cd 03-GettingStarted/mcp/app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export ORACLE_DRIVER_MODE=thick
export ORACLE_CLIENT_LIB_DIR=/Users/ansingh/apps/instantclient_23_26
export ORACLE_USER=devdba
export ORACLE_PASSWORD=password123
export ORACLE_DSN=db.data-extract.devfarm.ariasystems.net:1521/ec01dub

python server.py   # stdio transport — connect via MCP Inspector or Claude Desktop
```

Test with MCP Inspector:

```bash
npx @modelcontextprotocol/inspector python server.py
```

---

## 7. Running Tests

```bash
cd 03-GettingStarted/mcp/app
source .venv/bin/activate
pip install pytest

# Unit tests (no DB required)
pytest tests/test_server.py tests/test_kb.py -q

# Integration tests (requires Oracle env vars set as above)
pytest tests/test_integration_oracle.py -q
```

---

## Environment Variable Reference

| Variable | Where set | Description |
|---|---|---|
| `MCP_TRANSPORT` | Dockerfile | `streamable-http` (K8s) or `stdio` (local) |
| `MCP_HOST` | Dockerfile | Bind address (`0.0.0.0` in container) |
| `MCP_PORT` | Dockerfile | HTTP port (default `8000`) |
| `ORACLE_DRIVER_MODE` | Dockerfile | `thick` (required for NNE) |
| `ORACLE_CLIENT_LIB_DIR` | Dockerfile | Path to Instant Client inside the container |
| `ORACLE_USER` | Optional secret / local shell | Default DB user (omit on shared cluster) |
| `ORACLE_PASSWORD` | Optional secret / local shell | Default DB password |
| `ORACLE_DSN` | Optional secret / local shell | Default DSN, e.g. `host:1521/service` |
| `ORACLE_POOL_MIN/MAX/INCREMENT` | Optional | Connection pool sizing (defaults: 1 / 5 / 1) |
| `ORACLE_MCP_DEBUG` | Optional | Set to any value to include tracebacks in tool errors |
