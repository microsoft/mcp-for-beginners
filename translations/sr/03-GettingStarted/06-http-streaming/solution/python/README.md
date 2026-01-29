# Покретање овог примера

Ево како да покренете класични HTTP стриминг сервер и клијента, као и MCP стриминг сервер и клијента користећи Python.

### Преглед

- Поставићете MCP сервер који шаље обавештења о напретку клијенту док обрађује ставке.
- Клијент ће приказивати свако обавештење у реалном времену.
- Овај водич покрива предуслове, постављање, покретање и решавање проблема.

### Предуслови

- Python 3.9 или новији
- Python пакет `mcp` (инсталирајте помоћу `pip install mcp`)

### Инсталација и постављање

1. Клонирајте репозиторијум или преузмите датотеке решења.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Креирајте и активирајте виртуелно окружење (препоручено):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Инсталирајте потребне зависности:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Датотеке

- **Сервер:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Клијент:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Покретање класичног HTTP стриминг сервера

1. Пређите у директоријум решења:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Покрените класични HTTP стриминг сервер:

   ```pwsh
   python server.py
   ```

3. Сервер ће се покренути и приказати:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Покретање класичног HTTP стриминг клијента

1. Отворите нови терминал (активирајте исто виртуелно окружење и директоријум):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Требало би да видите стримоване поруке које се секвенцијално приказују:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Покретање MCP стриминг сервера

1. Пређите у директоријум решења:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Покрените MCP сервер са транспортом streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Сервер ће се покренути и приказати:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Покретање MCP стриминг клијента

1. Отворите нови терминал (активирајте исто виртуелно окружење и директоријум):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Требало би да видите обавештења која се приказују у реалном времену док сервер обрађује сваку ставку:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Кључни кораци имплементације

1. **Креирајте MCP сервер користећи FastMCP.**
2. **Дефинишите алат који обрађује листу и шаље обавештења користећи `ctx.info()` или `ctx.log()`.**
3. **Покрените сервер са `transport="streamable-http"`.**
4. **Имплементирајте клијента са обрађивачем порука за приказивање обавештења како стижу.**

### Преглед кода
- Сервер користи асинхроне функције и MCP контекст за слање ажурирања напретка.
- Клијент имплементира асинхрони обрађивач порука за штампање обавештења и коначног резултата.

### Савети и решавање проблема

- Користите `async/await` за неблокирајуће операције.
- Увек обрађујте изузетке и на серверу и на клијенту ради робусности.
- Тестирајте са више клијената да бисте посматрали ажурирања у реалном времену.
- Ако наиђете на грешке, проверите верзију Python-а и уверите се да су све зависности инсталиране.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.