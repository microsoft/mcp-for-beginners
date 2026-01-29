# Executando este exemplo

Recomenda-se instalar `uv`, mas não é obrigatório. Veja [instruções](https://docs.astral.sh/uv/#highlights)

## -0- Crie um ambiente virtual

```bash
python -m venv venv
```

## -1- Ative o ambiente virtual

```bash
venv\Scripts\activate
```

## -2- Instale as dependências

```bash
pip install "mcp[cli]"
```

## -3- Execute o exemplo

```bash
mcp run server.py
```

## -4- Teste o exemplo

Com o servidor rodando em um terminal, abra outro terminal e execute o seguinte comando:

```bash
mcp dev server.py
```

Isso deve iniciar um servidor web com uma interface visual que permite testar o exemplo.

Uma vez que o servidor esteja conectado:

- tente listar as ferramentas e executar `add`, com os argumentos 2 e 4. Você deve ver 6 como resultado.

- vá para recursos e modelo de recurso e chame `get_greeting`, digite um nome e você deve ver uma saudação com o nome que forneceu.

### Testando no modo CLI

O inspetor que você executou é, na verdade, um aplicativo Node.js, e `mcp dev` é um wrapper em torno dele.

Você pode iniciá-lo diretamente no modo CLI executando o seguinte comando:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Isso listará todas as ferramentas disponíveis no servidor. Você deve ver a seguinte saída:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Para invocar uma ferramenta, digite:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Você deve ver a seguinte saída:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Geralmente é muito mais rápido executar o inspetor no modo CLI do que no navegador.
> Leia mais sobre o inspetor [aqui](https://github.com/modelcontextprotocol/inspector).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.