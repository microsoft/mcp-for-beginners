# Executar este exemplo

## -1- Instalar as dependências

```bash
dotnet restore
```

## -2- Executar o exemplo

```bash
dotnet run
```

## -3- Testar o exemplo

Inicie um terminal separado antes de executar o comando abaixo (certifique-se de que o servidor ainda está em execução).

Com o servidor a funcionar num terminal, abra outro terminal e execute o seguinte comando:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Isto deverá iniciar um servidor web com uma interface visual que permite testar o exemplo.

> Certifique-se de que o **HTTP Streamable** está selecionado como tipo de transporte e que o URL é `http://localhost:3001/mcp`.

Depois de o servidor estar conectado:

- experimente listar ferramentas e executar `add`, com os argumentos 2 e 4, deverá ver 6 no resultado.
- vá a recursos e ao modelo de recurso e chame "greeting", insira um nome e deverá ver uma saudação com o nome que forneceu.

### Testar no modo CLI

Pode iniciar diretamente no modo CLI executando o seguinte comando:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Isto irá listar todas as ferramentas disponíveis no servidor. Deverá ver o seguinte resultado:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Para invocar uma ferramenta, digite:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Deverá ver o seguinte resultado:

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
> Normalmente é muito mais rápido executar o inspector no modo CLI do que no navegador.
> Leia mais sobre o inspector [aqui](https://github.com/modelcontextprotocol/inspector).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.