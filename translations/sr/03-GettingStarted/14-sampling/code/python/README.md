# Покрени пример

> [!WARNING]
> Овај пример користи застарели Sampling и стари HTTP+SSE крајњи терминал. Он је
> задржан за MCP `2025-11-25` компатибилност. Нове имплементације треба директно да позивају
> LLM провајдера и користе Streamable HTTP за удаљени MCP саобраћај.

## Направи виртуелно окружење

```sh
python -m venv venv
source ./venv/bin/activate
```

## Инсталирај зависности

```sh
pip install "mcp[cli]"
```

## Покрени сервер

```sh
uvicorn server:app --port 8000
```

## Тестирај сервер са GitHub Copilot и VS Code

Додај унос у mcp.json на следећи начин:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Увери се да си кликнуо на „start“ на серверу.

У GitHub Copilot налепи следећи захтев:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Први пут ће те питати да прихватиш Sampling акцију, затим ће те питати да прихватиш алат да покрене „create_blog“. Требало би да видиш сличан одговор:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->