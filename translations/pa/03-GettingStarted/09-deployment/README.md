# MCP ਸਰਵਰਾਂ ਦੀ ਤਾਇਨਾਤੀ

ਆਪਣੇ MCP ਸਰਵਰ ਨੂੰ ਤਾਇਨਾਤ ਕਰਨ ਨਾਲ ਹੋਰ ਲੋਕ ਇਸਦੇ ਟੂਲ ਅਤੇ ਸਰੋਤਾਂ ਤੱਕ ਤੁਹਾਡੇ ਸਥਾਨਕ ਵਾਤਾਵਰਣ ਤੋਂ ਬਾਹਰ ਵੀ ਪਹੁੰਚ ਸਕਦੇ ਹਨ। ਤੁਹਾਡੇ ਸਕੇਲਬਿਲਟੀ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਪ੍ਰਬੰਧਨ ਦੀ ਸੌਖਿਆ ਦੇ ਅਧਾਰ 'ਤੇ ਕਈ ਤਾਇਨਾਤੀ ਰਣਨੀਤੀਆਂ ਹਨ। ਹੇਠਾਂ ਤੁਹਾਨੂੰ MCP ਸਰਵਰਾਂ ਨੂੰ ਸਥਾਨਕ, ਕੰਟੇਨਰਾਂ ਵਿੱਚ ਅਤੇ ਕਲਾਉਡ 'ਤੇ ਤਾਇਨਾਤ ਕਰਨ ਲਈ ਮਦਦ ਮਿਲੇਗੀ।

## ਝਲਕ

ਇਸ ਪਾਠ ਵਿੱਚ ਤੁਹਾਨੂੰ ਸਿਖਾਇਆ ਜਾਵੇਗਾ ਕਿ MCP ਸਰਵਰ ਐਪ ਨੂੰ ਕਿਵੇਂ ਤਾਇਨਾਤ ਕਰਨਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕੜੀ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਵੱਖ-ਵੱਖ ਤਾਇਨਾਤੀ ਤਰੀਕਿਆਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ।
- ਆਪਣੀ ਐਪ ਨੂੰ ਤਾਇਨਾਤ ਕਰਨ ਲਈ।

## ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਤਾਇਨਾਤੀ

ਜੇ ਤੁਹਾਡਾ ਸਰਵਰ ਉਪਭੋਗਤਾਵਾਂ ਦੀ ਮਸ਼ੀਨ 'ਤੇ ਚੱਲਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ:

1. **ਸਰਵਰ ਡਾਊਨਲੋਡ ਕਰੋ**। ਜੇ ਤੁਸੀਂ ਸਰਵਰ ਨਹੀਂ ਲਿਖਿਆ, ਤਾਂ ਪਹਿਲਾਂ ਇਸਨੂੰ ਆਪਣੀ ਮਸ਼ੀਨ 'ਤੇ ਡਾਊਨਲੋਡ ਕਰੋ।  
1. **ਸਰਵਰ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰੋ**: ਆਪਣੀ MCP ਸਰਵਰ ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ।

SSE ਲਈ (stdio ਕਿਸਮ ਦੇ ਸਰਵਰ ਲਈ ਲੋੜ ਨਹੀਂ)

1. **ਨੈੱਟਵਰਕਿੰਗ ਸੈਟ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਰ ਉਮੀਦ ਕੀਤੇ ਪੋਰਟ 'ਤੇ ਪਹੁੰਚਯੋਗ ਹੈ।  
1. **ਕਲਾਇੰਟਾਂ ਨੂੰ ਜੁੜੋ**: ਸਥਾਨਕ ਕਨੈਕਸ਼ਨ URLs ਵਰਗੇ `http://localhost:3000` ਦੀ ਵਰਤੋਂ ਕਰੋ।

## ਕਲਾਉਡ ਤਾਇਨਾਤੀ

MCP ਸਰਵਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਕਲਾਉਡ ਪਲੇਟਫਾਰਮਾਂ 'ਤੇ ਤਾਇਨਾਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:

- **ਸਰਵਰਲੈੱਸ ਫੰਕਸ਼ਨਜ਼**: ਹਲਕੇ MCP ਸਰਵਰਾਂ ਨੂੰ ਸਰਵਰਲੈੱਸ ਫੰਕਸ਼ਨਜ਼ ਵਜੋਂ ਤਾਇਨਾਤ ਕਰੋ।  
- **ਕੰਟੇਨਰ ਸੇਵਾਵਾਂ**: Azure Container Apps, AWS ECS ਜਾਂ Google Cloud Run ਵਰਗੀਆਂ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।  
- **ਕੁਬਰਨੇਟਿਸ**: MCP ਸਰਵਰਾਂ ਨੂੰ ਕੁਬਰਨੇਟਿਸ ਕਲੱਸਟਰਾਂ ਵਿੱਚ ਉੱਚ ਉਪਲਬਧਤਾ ਲਈ ਤਾਇਨਾਤ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰੋ।

### ਉਦਾਹਰਨ: Azure Container Apps

Azure Container Apps MCP ਸਰਵਰਾਂ ਦੀ ਤਾਇਨਾਤ ਨੂੰ ਸਹਾਇਤਾ ਦਿੰਦੇ ਹਨ। ਇਹ ਅਜੇ ਵੀ ਵਿਕਾਸ ਵਿੱਚ ਹੈ ਅਤੇ ਇਸ ਸਮੇਂ SSE ਸਰਵਰਾਂ ਨੂੰ ਸਹਾਇਤਾ ਦਿੰਦਾ ਹੈ।

ਇਸ ਤਰ੍ਹਾਂ ਤੁਸੀਂ ਇਸਨੂੰ ਕਰ ਸਕਦੇ ਹੋ:

1. ਇੱਕ ਰਿਪੋ ਕਲੋਨ ਕਰੋ:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. ਟੈਸਟ ਕਰਨ ਲਈ ਇਸਨੂੰ ਸਥਾਨਕ ਚਲਾਓ:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. ਇਸਨੂੰ ਸਥਾਨਕ ਟੈਸਟ ਕਰਨ ਲਈ, *.vscode* ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ *mcp.json* ਫਾਇਲ ਬਣਾਓ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਸ਼ਾਮਲ ਕਰੋ:

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

  ਜਦੋਂ SSE ਸਰਵਰ ਸ਼ੁਰੂ ਹੋ ਜਾਵੇ, ਤਾਂ ਤੁਸੀਂ JSON ਫਾਇਲ ਵਿੱਚ ਪਲੇ ਆਈਕਨ 'ਤੇ ਕਲਿੱਕ ਕਰ ਸਕਦੇ ਹੋ, ਹੁਣ ਤੁਸੀਂ ਸਰਵਰ 'ਤੇ ਟੂਲ GitHub Copilot ਦੁਆਰਾ ਪਛਾਣੇ ਜਾਣਗੇ, ਟੂਲ ਆਈਕਨ ਵੇਖੋ।

1. ਤਾਇਨਾਤ ਕਰਨ ਲਈ, ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

ਇਸ ਤਰ੍ਹਾਂ, ਇਸਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਜਾਂ Azure 'ਤੇ ਤਾਇਨਾਤ ਕਰੋ।

## ਵਾਧੂ ਸਰੋਤ

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps ਲੇਖ](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP ਰਿਪੋ](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [ਵਿਆਵਹਾਰਿਕ ਲਾਗੂ ਕਰਨ](../../04-PracticalImplementation/README.md)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।