# Запуск цього прикладу

Рекомендується встановити `uv`, але це необов’язково, дивіться [інструкції](https://docs.astral.sh/uv/#highlights)

## -0- Створіть віртуальне оточення

```bash
python -m venv venv
```

## -1- Активуйте віртуальне оточення

```bash
venv\Scripts\activate
```

## -2- Встановіть залежності

```bash
pip install "mcp[cli]"
```

## -3- Запустіть приклад

```bash
python client.py
```

Ви повинні побачити вивід, подібний до:

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
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->