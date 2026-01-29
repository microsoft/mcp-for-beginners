# Servidor MCP Calculator (Python)

Uma implementação simples de servidor Model Context Protocol (MCP) em Python que oferece funcionalidades básicas de calculadora.

## Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

Ou instale diretamente o SDK Python do MCP:

```bash
pip install mcp>=1.18.0
```

## Uso

### Executando o Servidor

O servidor foi projetado para ser usado por clientes MCP (como o Claude Desktop). Para iniciar o servidor:

```bash
python mcp_calculator_server.py
```

**Nota**: Quando executado diretamente em um terminal, você verá erros de validação JSON-RPC. Isso é um comportamento normal - o servidor está aguardando mensagens formatadas corretamente de clientes MCP.

### Testando as Funções

Para testar se as funções da calculadora estão funcionando corretamente:

```bash
python test_calculator.py
```

## Solução de Problemas

### Erros de Importação

Se você vir `ModuleNotFoundError: No module named 'mcp'`, instale o SDK Python do MCP:

```bash
pip install mcp>=1.18.0
```

### Erros JSON-RPC ao Executar Diretamente

Erros como "Invalid JSON: EOF while parsing a value" ao executar o servidor diretamente são esperados. O servidor precisa de mensagens de clientes MCP, e não de entradas diretas no terminal.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.