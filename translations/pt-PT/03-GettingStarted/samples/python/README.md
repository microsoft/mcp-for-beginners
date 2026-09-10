# Servidor Calculadora MCP (Python)



Uma implementação simples de servidor do Protocolo de Contexto de Modelo (MCP) em Python que fornece funcionalidade básica de calculadora.


## Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

Ou instale o SDK MCP Python diretamente:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Utilização

### Executar o Servidor

O servidor foi concebido para ser usado por clientes MCP (como o Claude Desktop). Para iniciar o servidor:

```bash
python mcp_calculator_server.py
```

**Nota**: Quando executado diretamente num terminal, verá erros de validação JSON-RPC. Este é um comportamento normal - o servidor está à espera de mensagens de clientes MCP devidamente formatadas.

### Testar as Funções

Para testar se as funções da calculadora funcionam corretamente:

```bash
python test_calculator.py
```

## Resolução de Problemas

### Erros de Importação

Se vir `ModuleNotFoundError: No module named 'mcp'`, instale o SDK MCP Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Erros JSON-RPC ao Executar Diretamente

Erros como "Invalid JSON: EOF while parsing a value" ao executar o servidor diretamente são esperados. O servidor necessita de mensagens de clientes MCP, não de input direto do terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->