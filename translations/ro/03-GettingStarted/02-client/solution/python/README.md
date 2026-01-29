# Rularea acestui exemplu

Se recomandă să instalezi `uv`, dar nu este obligatoriu, vezi [instrucțiunile](https://docs.astral.sh/uv/#highlights)

## -0- Creează un mediu virtual

```bash
python -m venv venv
```

## -1- Activează mediul virtual

```bash
venv\Scrips\activate
```

## -2- Instalează dependențele

```bash
pip install "mcp[cli]"
```

## -3- Rulează exemplul


```bash
python client.py
```

Ar trebui să vezi o ieșire similară cu:

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

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.