# Servidor MCP Calculator (Python)



Uma implementação simples de servidor do Model Context Protocol (MCP) em Python que oferece funcionalidades básicas de calculadora.


## Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

Ou instale diretamente o SDK Python do MCP:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Uso

### Executando o Servidor

O servidor foi projetado para ser usado por clientes MCP (como Claude Desktop). Para iniciar o servidor:

```bash
python mcp_calculator_server.py
```

**Nota**: Quando executado diretamente em um terminal, você verá erros de validação JSON-RPC. Este é um comportamento normal — o servidor está aguardando mensagens de cliente MCP devidamente formatadas.

### Testando as Funções

Para testar se as funções da calculadora funcionam corretamente:

```bash
python test_calculator.py
```

## Resolução de Problemas

### Erros de Importação

Se você vir `ModuleNotFoundError: No module named 'mcp'`, instale o SDK Python do MCP:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Erros JSON-RPC ao Executar Diretamente

Erros como "JSON Inválido: EOF enquanto analisava um valor" ao executar o servidor diretamente são esperados. O servidor precisa de mensagens de clientes MCP, não de entrada direta do terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->