# Изпълнение на този пример

Ето как да стартирате класическия HTTP стрийминг сървър и клиент, както и MCP стрийминг сървър и клиент с помощта на Python.

### Общ преглед

- Ще настроите MCP сървър, който изпраща известия за напредък към клиента, докато обработва елементи.
- Клиентът ще показва всяко известие в реално време.
- Това ръководство обхваща предварителни изисквания, настройка, стартиране и отстраняване на проблеми.

### Предварителни изисквания

- Python 3.9 или по-нова версия
- Python пакетът `mcp` (инсталирайте с `pip install mcp`)

### Инсталация и настройка

1. Клонирайте хранилището или изтеглете файловете на решението.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Създайте и активирайте виртуална среда (препоръчително):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Инсталирайте необходимите зависимости:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Файлове

- **Сървър:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Клиент:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Стартиране на класическия HTTP стрийминг сървър

1. Навигирайте до директорията на решението:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Стартирайте класическия HTTP стрийминг сървър:

   ```pwsh
   python server.py
   ```

3. Сървърът ще се стартира и ще покаже:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Стартиране на класическия HTTP стрийминг клиент

1. Отворете нов терминал (активирайте същата виртуална среда и директория):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Трябва да видите последователно отпечатани съобщения:

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

### Стартиране на MCP стрийминг сървър

1. Навигирайте до директорията на решението:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Стартирайте MCP сървъра с транспорт streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Сървърът ще се стартира и ще покаже:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Стартиране на MCP стрийминг клиент

1. Отворете нов терминал (активирайте същата виртуална среда и директория):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Трябва да видите известия, отпечатани в реално време, докато сървърът обработва всеки елемент:
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

### Основни стъпки за имплементация

1. **Създайте MCP сървър с помощта на FastMCP.**
2. **Дефинирайте инструмент, който обработва списък и изпраща известия с помощта на `ctx.info()` или `ctx.log()`.**
3. **Стартирайте сървъра с `transport="streamable-http"`.**
4. **Имплементирайте клиент с обработчик на съобщения, който показва известията при пристигането им.**

### Преглед на кода
- Сървърът използва асинхронни функции и MCP контекст за изпращане на актуализации за напредък.
- Клиентът имплементира асинхронен обработчик на съобщения за отпечатване на известия и крайния резултат.

### Съвети и отстраняване на проблеми

- Използвайте `async/await` за неблокиращи операции.
- Винаги обработвайте изключения както в сървъра, така и в клиента за по-голяма надеждност.
- Тествайте с множество клиенти, за да наблюдавате актуализации в реално време.
- Ако срещнете грешки, проверете версията на Python и се уверете, че всички зависимости са инсталирани.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.