# Деплојовање MCP сервера

Деплојовање вашег MCP сервера омогућава другима да приступе његовим алатима и ресурсима ван вашег локалног окружења. Постоји неколико стратегија за деплојовање које треба размотрити, у зависности од ваших захтева за скалабилношћу, поузданошћу и лакоћом управљања. Испод ћете пронаћи упутства за деплојовање MCP сервера локално, у контејнерима и у облаку.

## Преглед

Ова лекција обухвата како да деплојујете вашу MCP Server апликацију.

## Циљеви учења

До краја ове лекције, моћи ћете да:

- Процените различите приступе деплојовању.
- Деплојујете вашу апликацију.

## Локални развој и деплојовање

Ако је ваш сервер намењен да се користи тако што ће радити на корисничком рачунару, можете пратити следеће кораке:

1. **Преузмите сервер**. Ако нисте ви написали сервер, прво га преузмите на свој рачунар.  
1. **Покрените серверски процес**: Покрените вашу MCP сервер апликацију.

За SSE (није потребно за stdio тип сервера)

1. **Конфигуришите мрежу**: Осигурајте да је сервер доступан на очекиваном порту.  
1. **Повежите клијенте**: Користите локалне URL адресе као што је `http://localhost:3000`.

## Деплојовање у облак

MCP сервери могу бити деплојовани на различите облачне платформе:

- **Serverless Functions**: Деплојујте лагане MCP сервере као serverless функције  
- **Container Services**: Користите сервисе као што су Azure Container Apps, AWS ECS или Google Cloud Run  
- **Kubernetes**: Деплојујте и управљајте MCP серверима у Kubernetes кластерима ради високе доступности

### Пример: Azure Container Apps

Azure Container Apps подржава деплојовање MCP сервера. Ово је још увек у развоју и тренутно подржава SSE сервере.

Ево како то можете урадити:

1. Клонирајте репозиторијум:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Покрените га локално да тестирате:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Да бисте га пробали локално, направите *mcp.json* фајл у *.vscode* директоријуму и додајте следећи садржај:

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

  Када се SSE сервер покрене, можете кликнути на иконицу за покретање у JSON фајлу, сада би требало да видите да GitHub Copilot препознаје алате на серверу, погледајте икону алата.

1. За деплојовање, покрените следећу команду:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ето, деплојујте га локално или у Azure пратећи ове кораке.

## Додатни ресурси

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Чланак о Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP репо](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Шта следи

- Следеће: [Практична имплементација](../../04-PracticalImplementation/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.