# Запустіть приклад

> [!WARNING]
> Цей приклад використовує застаріле Sampling і спадковий HTTP+SSE ендпоінт. Він
> збережений для сумісності MCP `2025-11-25`. Нові реалізації повинні викликати
> провайдера LLM безпосередньо та використовувати Streamable HTTP для віддаленого трафіку MCP.

## Створіть віртуальне оточення

```sh
python -m venv venv
source ./venv/bin/activate
```

## Встановіть залежності

```sh
pip install "mcp[cli]"
```

## Запустіть сервер

```sh
uvicorn server:app --port 8000
```

## Перевірте сервер за допомогою GitHub Copilot та VS Code

Додайте запис до mcp.json ось так:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Переконайтесь, що ви натиснули «start» на сервері.

У GitHub Copilot вставте наступний запит:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Вперше у вас запитають, чи прийняти дію Sampling, потім буде запит про дозвіл виконання інструменту "create_blog". Ви повинні побачити відповідь подібну до:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->