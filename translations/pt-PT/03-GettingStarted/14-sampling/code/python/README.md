# Executar o exemplo

> [!WARNING]
> Este exemplo utiliza Sampling obsoleto e um endpoint legado HTTP+SSE. É
> mantido para compatibilidade com MCP `2025-11-25`. Novas implementações devem chamar
> um fornecedor LLM diretamente e usar HTTP Streamable para tráfego remoto MCP.

## Criar ambiente virtual

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instalar dependências

```sh
pip install "mcp[cli]"
```

## Executar o servidor

```sh
uvicorn server:app --port 8000
```

## Testar o servidor com GitHub Copilot e VS Code

Adicione a entrada ao ficheiro mcp.json assim:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Certifique-se de clicar em "start" no servidor.

No GitHub Copilot cole o seguinte prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Na primeira vez será questionado se aceita uma ação Sampling, depois será pedido para aceitar a ferramenta para executar "create_blog". Deve ver uma resposta semelhante a:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->