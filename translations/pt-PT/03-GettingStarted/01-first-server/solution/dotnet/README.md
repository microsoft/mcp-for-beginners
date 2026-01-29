# Executar este exemplo

## -1- Instalar as dependências

```bash
dotnet restore
```

## -3- Executar o exemplo

```bash
dotnet run
```

## -4- Testar o exemplo

Com o servidor a funcionar num terminal, abra outro terminal e execute o seguinte comando:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Isto deverá iniciar um servidor web com uma interface visual que permite testar o exemplo.

Depois de o servidor estar conectado:

- Experimente listar as ferramentas e executar `add`, com os argumentos 2 e 4. Deverá ver 6 como resultado.
- Vá a recursos e ao modelo de recurso e chame "greeting". Insira um nome e deverá ver uma saudação com o nome que forneceu.

### Testar no modo CLI

Pode iniciá-lo diretamente no modo CLI executando o seguinte comando:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Isto irá listar todas as ferramentas disponíveis no servidor. Deverá ver o seguinte output:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Deverá ver o seguinte output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.