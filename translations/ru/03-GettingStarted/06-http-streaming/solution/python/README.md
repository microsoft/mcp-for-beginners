# Запуск этого примера

Вот как запустить классический HTTP сервер и клиент потоковой передачи, а также MCP сервер и клиент потоковой передачи с использованием Python.

### Обзор

- Вы настроите MCP сервер, который будет отправлять уведомления о прогрессе клиенту по мере обработки элементов.
- Клиент будет отображать каждое уведомление в реальном времени.
- В этом руководстве описаны предварительные требования, настройка, запуск и устранение неполадок.

### Предварительные требования

- Python 3.9 или новее
- Python пакет `mcp` (установите с помощью `pip install mcp`)

### Установка и настройка

1. Клонируйте репозиторий или загрузите файлы решения.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Создайте и активируйте виртуальное окружение (рекомендуется):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Установите необходимые зависимости:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Файлы

- **Сервер:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Клиент:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Запуск классического HTTP сервера потоковой передачи

1. Перейдите в директорию с решением:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Запустите классический HTTP сервер потоковой передачи:

   ```pwsh
   python server.py
   ```

3. Сервер запустится и отобразит:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Запуск классического HTTP клиента потоковой передачи

1. Откройте новый терминал (активируйте то же виртуальное окружение и директорию):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Вы должны увидеть последовательный вывод потоковых сообщений:

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

### Запуск MCP сервера потоковой передачи

1. Перейдите в директорию с решением:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Запустите MCP сервер с транспортом streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Сервер запустится и отобразит:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Запуск MCP клиента потоковой передачи

1. Откройте новый терминал (активируйте то же виртуальное окружение и директорию):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Вы должны увидеть уведомления, отображаемые в реальном времени, по мере обработки сервером каждого элемента:
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

### Основные этапы реализации

1. **Создайте MCP сервер с использованием FastMCP.**
2. **Определите инструмент, который обрабатывает список и отправляет уведомления с помощью `ctx.info()` или `ctx.log()`.**
3. **Запустите сервер с `transport="streamable-http"`.**
4. **Реализуйте клиент с обработчиком сообщений для отображения уведомлений по мере их поступления.**

### Обзор кода
- Сервер использует асинхронные функции и MCP контекст для отправки обновлений о прогрессе.
- Клиент реализует асинхронный обработчик сообщений для вывода уведомлений и конечного результата.

### Советы и устранение неполадок

- Используйте `async/await` для неблокирующих операций.
- Всегда обрабатывайте исключения как на сервере, так и на клиенте для повышения надежности.
- Тестируйте с несколькими клиентами, чтобы наблюдать обновления в реальном времени.
- Если возникают ошибки, проверьте версию Python и убедитесь, что все зависимости установлены.

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.