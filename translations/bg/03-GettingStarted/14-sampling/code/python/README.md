# Стартирайте примера

> [!WARNING]
> Този пример използва остарял Sampling и наследствен HTTP+SSE крайна точка. Той е
> запазен за съвместимост с MCP `2025-11-25`. Новите реализации трябва да извикват
> доставчик на LLM директно и да използват Streamable HTTP за отдалечен MCP трафик.

## Създаване на виртуална среда

```sh
python -m venv venv
source ./venv/bin/activate
```

## Инсталиране на зависимости

```sh
pip install "mcp[cli]"
```

## Стартиране на сървъра

```sh
uvicorn server:app --port 8000
```

## Изпробвайте сървъра с GitHub Copilot и VS Code

Добавете записа в mcp.json по следния начин:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Уверете се, че сте натиснали "start" на сървъра.

В GitHub Copilot поставете следния prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Първия път ще бъдете попитани дали приемате Sampling действие, след което ще бъдете помолени да приемете инструмента да изпълни "create_blog". Трябва да видите отговор, подобен на:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->