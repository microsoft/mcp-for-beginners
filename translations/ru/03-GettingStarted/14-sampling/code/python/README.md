# Запустите пример

> [!WARNING]
> Этот пример использует устаревший Sampling и устаревший HTTP+SSE эндпоинт. Он
> сохранён для совместимости с MCP `2025-11-25`. В новых реализациях следует обращаться
> напрямую к LLM-провайдеру и использовать Streamable HTTP для удалённого трафика MCP.

## Создайте виртуальное окружение

```sh
python -m venv venv
source ./venv/bin/activate
```

## Установите зависимости

```sh
pip install "mcp[cli]"
```

## Запустите сервер

```sh
uvicorn server:app --port 8000
```

## Проверьте работу сервера с GitHub Copilot и VS Code

Добавьте запись в mcp.json следующим образом:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Убедитесь, что вы нажали "start" на сервере.

В GitHub Copilot вставьте следующий запрос:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

В первый раз вас попросят принять действие Sampling, затем будет запрос на разрешение запуска инструмента "create_blog". Вы должны увидеть ответ, похожий на:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->