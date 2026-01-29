# Executando este exemplo

## -1- Instale as dependências

```bash
dotnet restore
```

## -3- Execute o exemplo

```bash
dotnet run
```

## -4- Teste o exemplo

Com o servidor rodando em um terminal, abra outro terminal e execute o seguinte comando:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Isso deve iniciar um servidor web com uma interface visual que permite testar o exemplo.

Uma vez que o servidor esteja conectado:

- Experimente listar as ferramentas e executar `add`, com os argumentos 2 e 4. Você deve ver 6 como resultado.
- Vá para recursos e modelo de recurso e chame "greeting". Digite um nome e você deve ver uma saudação com o nome que forneceu.

### Testando no modo CLI

Você pode iniciá-lo diretamente no modo CLI executando o seguinte comando:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Isso listará todas as ferramentas disponíveis no servidor. Você deve ver a seguinte saída:

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

Você deve ver a seguinte saída:

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
> Geralmente é muito mais rápido executar o inspetor no modo CLI do que no navegador.
> Leia mais sobre o inspetor [aqui](https://github.com/modelcontextprotocol/inspector).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.