# Executar este exemplo

Recomenda-se instalar `uv`, mas não é obrigatório, veja as [instruções](https://docs.astral.sh/uv/#highlights)

## -0- Criar um ambiente virtual

```bash
python -m venv venv
```

## -1- Ativar o ambiente virtual

```bash
venv\Scrips\activate
```

## -2- Instalar as dependências

```bash
pip install "mcp[cli]"
```

## -3- Executar o exemplo

```bash
python client.py
```

Deverá ver uma saída semelhante a:

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
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.