# Uruchamianie tego przykładu

Zaleca się zainstalowanie `uv`, ale nie jest to konieczne, zobacz [instrukcje](https://docs.astral.sh/uv/#highlights)

## -0- Utwórz środowisko wirtualne

```bash
python -m venv venv
```

## -1- Aktywuj środowisko wirtualne

```bash
venv\Scrips\activate
```

## -2- Zainstaluj zależności

```bash
pip install "mcp[cli]"
```

## -3- Uruchom przykład


```bash
python client.py
```

Powinieneś zobaczyć wynik podobny do:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.