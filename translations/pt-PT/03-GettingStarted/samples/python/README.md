# Servidor MCP Calculator (Python)

Uma implementação simples de servidor Model Context Protocol (MCP) em Python que oferece funcionalidades básicas de calculadora.

## Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```
  
Ou instale diretamente o SDK MCP Python:

```bash
pip install mcp>=1.18.0
```
  

## Utilização

### Executar o Servidor

O servidor foi projetado para ser utilizado por clientes MCP (como o Claude Desktop). Para iniciar o servidor:

```bash
python mcp_calculator_server.py
```
  
**Nota**: Quando executado diretamente num terminal, verá erros de validação JSON-RPC. Este é um comportamento normal - o servidor está à espera de mensagens formatadas corretamente de clientes MCP.

### Testar as Funções

Para testar se as funções da calculadora funcionam corretamente:

```bash
python test_calculator.py
```
  

## Resolução de Problemas

### Erros de Importação

Se aparecer `ModuleNotFoundError: No module named 'mcp'`, instale o SDK MCP Python:

```bash
pip install mcp>=1.18.0
```
  

### Erros JSON-RPC ao Executar Diretamente

Erros como "Invalid JSON: EOF while parsing a value" ao executar o servidor diretamente são esperados. O servidor necessita de mensagens de clientes MCP, e não de entradas diretas no terminal.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.