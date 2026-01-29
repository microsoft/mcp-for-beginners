# Ejecutando este ejemplo

Se recomienda instalar `uv` pero no es obligatorio, consulta las [instrucciones](https://docs.astral.sh/uv/#highlights)

## -0- Crear un entorno virtual

```bash
python -m venv venv
```

## -1- Activar el entorno virtual

```bash
venv\Scrips\activate
```

## -2- Instalar las dependencias

```bash
pip install "mcp[cli]"
```

## -3- Ejecutar el ejemplo

```bash
python client.py
```

Deberías ver una salida similar a:

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

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.