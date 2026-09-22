# Запуск этого примера

Рекомендуется установить `uv`, но это не обязательно, см. [инструкции](https://docs.astral.sh/uv/#highlights)

## -0- Создайте виртуальное окружение

```bash
python -m venv venv
```

## -1- Активируйте виртуальное окружение

```bash
venv\Scripts\activate
```

## -2- Установите зависимости

```bash
pip install "mcp[cli]"
```

## -3- Запустите пример

```bash
python client.py
```

Вы должны увидеть вывод, похожий на:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->