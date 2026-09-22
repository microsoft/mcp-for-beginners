# MCP ਸਰਵਰ ਤੈਅਰ ਕਰਨਾ

> [!NOTE]
> ਕਨਫਿਗਰੇਸ਼ਨ ਉਦਾਹਰਣਾਂ ਜੋ `/sse` ਐਂਡਪੋਇੰਟ ਨੂੰ ਵਰਤਦੀਆਂ ਹਨ ਉਹ ਲੈਗਸੀ HTTP+SSE ਟ੍ਰਾਂਸਪੋਰਟ ਨੂੰ ਨਿਸ਼ਾਨਾ ਬਨਾਉਂਦੀਆਂ ਹਨ। MCP `2026-07-28` ਰਿਮੋਟ ਸਰਵਰ ਸਟ੍ਰੀਮੇਬਲ HTTP ਵਰਤਦੇ ਹਨ, ਆਮ ਤੌਰ 'ਤੇ ਸੇਰਵਰ-ਨਿਰਧਾਰਿਤ ਐਂਡਪੋਇੰਟ ਵਿੱਚ ਜਿਵੇਂ `/mcp`।
> 




## ਸਰਵੇਖਣ

ਇਹ ਪਾਠ MCP ਸਰਵਰ ਐਪ ਨੂੰ ਕਿਵੇਂ ਤੈਅਰ ਕਰਨਾ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਵੱਖ-ਵੱਖ ਤੈਅਰੀ ਢੰਗਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ।
- ਆਪਣੀ ਐਪ ਨੂੰ ਤੈਅਰ ਕਰੋ।

## ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਤੈਅਰੀ

ਜੇ ਤੁਹਾਡਾ ਸਰਵਰ ਉਪਭੋਗਤਾ ਦੀ ਮਸ਼ੀਨ 'ਤੇ ਚੱਲ ਕੇ ਉਪਭੋਗਤਾ ਲਈ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ:

1. **ਸਰਵਰ ਡਾਉਨਲੋਡ ਕਰੋ**। ਜੇ ਤੁਸੀਂ ਸਰਵਰ ਨਹੀਂ ਲਿਖਿਆ, ਤਾਂ ਪਹਿਲਾਂ ਇਸਨੂੰ ਆਪਣੇ ਮਸ਼ੀਨ 'ਤੇ ਡਾਉਨਲੋਡ ਕਰੋ।
1. **ਸਰਵਰ ਪ੍ਰੋਸੈਸ ਸ਼ੁਰੂ ਕਰੋ**: ਆਪਣੀ MCP ਸਰਵਰ ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ

SSE ਲਈ (stdio ਟਾਈਪ ਸਰਵਰ ਲਈ ਜ਼ਰੂਰੀ ਨਹੀਂ)

1. **ਨੈੱਟਵਰਕਿੰਗ ਸੈਟ ਅਪ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਰ ਉਮੀਦ ਕੀਤੇ ਪੋਰਟ 'ਤੇ ਪਹੁੰਚਯੋਗ ਹੈ
1. **ਕਲਾਇੰਟ ਕਨੈਕਟ ਕਰੋ**: ਸਥਾਨਕ ਕਨੈਕਸ਼ਨ URLs ਵਰਤੋ ਜਿਵੇਂ `http://localhost:3000`

## ਕਲਾਉਡ ਤੈਅਰੀ

MCP ਸਰਵਰ ਕਈ ਕਲਾਉਡ ਪਲੇਟਫਾਰਮਾਂ 'ਤੇ ਤੈਅਰ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ:

- **ਸਰਵਰਲੈਸ ਫੰਕਸ਼ਨਸ**: ਹਲਕੇ MCP ਸਰਵਰਾਂ ਨੂੰ ਸਰਵਰਲੈਸ ਫੰਕਸ਼ਨ ਵਜੋਂ ਤੈਅਰ ਕਰੋ
- **ਕੰਟੇਨਰ ਸੇਵਾਵਾਂ**: ਜਿਵੇਂ Azure Container Apps, AWS ECS, ਜਾਂ Google Cloud Run ਵਰਤੋ
- **ਕੁਬਰਨੇਟਿਸ**: MCP ਸਰਵਰਾਂ ਨੂੰ ਕੁਬਰਨੇਟਿਸ ਕਲੱਸਟਰਾਂ ਵਿੱਚ ਤੈਅਰ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰੋ ਦਿੱਲੋਂ ਉੱਚ ਉਪਲੱਬਧਤਾ ਲਈ

### ਉਦਾਹਰਣ: Azure Container Apps

Azure Container Apps MCP ਸਰਵਰਾਂ ਦੀ ਤੈਅਰੀ ਨੂੰ ਸਮਰਥਨ ਕਰਦੇ ਹਨ। ਇਹ ਅਜੇ ਵੀ ਵਿਕਾਸ ਅਧੀਨ ਹੈ ਅਤੇ ਇਸ ਵਾਰਤੇ SSE ਸਰਵਰਾਂ ਨੂੰ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।

ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹੋ:

1. ਇੱਕ ਰੇਪੋ ਕਲੋਨ ਕਰੋ:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. ਲੋਕਲ ਤੌਰ 'ਤੇ ਟੈਸਟ ਕਰਨ ਲਈ ਚਲਾਓ:

  ```sh
  uv venv
  uv sync

  # ਲਿਨਕਸ/ਮੈਕਓਐਸ
  export API_KEYS=<AN_API_KEY>
  # ਵਿਂਡੋਜ਼
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. ਇਸਨੂੰ ਲੋਕਲ ਲਈ ਟ੍ਰਾਈ ਕਰਨ ਲਈ, ਇੱਕ *mcp.json* ਫਾਈਲ ਬਣਾਓ *.vscode* ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਸ਼ਾਮਲ ਕਰੋ:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

ਇੱਕ ਵਾਰੀ SSE ਸਰਵਰ ਸ਼ੁਰੂ ਹੋ ਜਾਂਦਾ ਹੈ, ਤੁਸੀਂ ਜੇਐਸਓਐਨ ਫਾਈਲ ਵਿੱਚ ਪਲੇਅ ਆਇਕਨ 'ਤੇ ਕਲਿੱਕ ਕਰ ਸਕਦੇ ਹੋ, ਹੁਣ ਤੁਸੀਂ GitHub Copilot ਵੱਲੋਂ ਸਰਵਰ 'ਤੇ ਟੂਲਾਂ ਨੂੰ ਚੁਣਿਆ ਜਾ ਰਿਹਾ ਦੇਖ ਸਕਦੇ ਹੋ, ਟੂਲ ਆਇਕਨ ਵੇਖੋ।

1. ਤੈਅਰੀ ਲਈ, ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

ਤੁਹਾਨੂੰ ਇਹ ਮਿਲਿਆ, ਇਸਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਤੈਅਰ ਕਰੋ, Azure 'ਤੇ ਇਸ ਤਰ੍ਹਾਂ ਤੈਅਰ ਕਰੋ।

## ਵਾਧੂ ਸਰੋਤ

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps ਲੇਖ](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP ਰੇਪੋ](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## ਅੱਗੇ ਕੀ ਹੈ

- ਅੱਗੇ: [ਉੱਚ-ਪੱਧਰੀ ਸਰਵਰ ਵਿਸ਼ੇ](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->