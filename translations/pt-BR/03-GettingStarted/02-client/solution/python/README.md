# Executando este exemplo

É recomendado instalar o `uv`, mas não é obrigatório, veja as [instruções](https://docs.astral.sh/uv/#highlights)

## -0- Crie um ambiente virtual

```bash
python -m venv venv
```

## -1- Ative o ambiente virtual

```bash
venv\Scrips\activate
```

## -2- Instale as dependências

```bash
pip install "mcp[cli]"
```

## -3- Execute o exemplo


```bash
python client.py
```

Você deve ver uma saída semelhante a:

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

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.