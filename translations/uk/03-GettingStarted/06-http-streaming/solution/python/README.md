# Запуск цього прикладу

Ось як запустити класичний HTTP сервер і клієнт для потокової передачі, а також MCP сервер і клієнт для потокової передачі за допомогою Python.

### Огляд

- Ви налаштуєте MCP сервер, який передає клієнту сповіщення про прогрес у процесі обробки елементів.
- Клієнт буде відображати кожне сповіщення в реальному часі.
- Цей посібник охоплює вимоги, налаштування, запуск і усунення несправностей.

### Вимоги

- Python 3.9 або новіший
- Python-пакет `mcp` (встановіть за допомогою `pip install mcp`)

### Встановлення та налаштування

1. Клонуйте репозиторій або завантажте файли рішення.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Створіть і активуйте віртуальне середовище (рекомендується):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Встановіть необхідні залежності:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Файли

- **Сервер:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Клієнт:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Запуск класичного HTTP сервера для потокової передачі

1. Перейдіть до каталогу рішення:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Запустіть класичний HTTP сервер для потокової передачі:

   ```pwsh
   python server.py
   ```

3. Сервер запуститься і відобразить:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Запуск класичного HTTP клієнта для потокової передачі

1. Відкрийте новий термінал (активуйте те саме віртуальне середовище і каталог):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Ви побачите, як повідомлення передаються послідовно:

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

### Запуск MCP сервера для потокової передачі

1. Перейдіть до каталогу рішення:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Запустіть MCP сервер із транспортом streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Сервер запуститься і відобразить:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Запуск MCP клієнта для потокової передачі

1. Відкрийте новий термінал (активуйте те саме віртуальне середовище і каталог):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Ви побачите сповіщення, які відображаються в реальному часі, коли сервер обробляє кожен елемент:
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

### Основні етапи реалізації

1. **Створіть MCP сервер за допомогою FastMCP.**
2. **Визначте інструмент, який обробляє список і надсилає сповіщення за допомогою `ctx.info()` або `ctx.log()`.**
3. **Запустіть сервер із `transport="streamable-http"`.**
4. **Реалізуйте клієнт із обробником повідомлень для відображення сповіщень у реальному часі.**

### Огляд коду
- Сервер використовує асинхронні функції та MCP контекст для надсилання оновлень про прогрес.
- Клієнт реалізує асинхронний обробник повідомлень для друку сповіщень і кінцевого результату.

### Поради та усунення несправностей

- Використовуйте `async/await` для неблокуючих операцій.
- Завжди обробляйте виключення як на сервері, так і на клієнті для забезпечення надійності.
- Тестуйте з кількома клієнтами, щоб спостерігати оновлення в реальному часі.
- Якщо виникають помилки, перевірте версію Python і переконайтеся, що всі залежності встановлені.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.