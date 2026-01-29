# Executando este exemplo

Recomenda-se instalar `uv`, mas não é obrigatório. Veja [instruções](https://docs.astral.sh/uv/#highlights)

## -1- Instale as dependências

```bash
npm install
```

## -3- Execute o exemplo

```bash
npm run build
```

## -4- Teste o exemplo

Com o servidor rodando em um terminal, abra outro terminal e execute o seguinte comando:

```bash
npm run inspector
```

Isso deve iniciar um servidor web com uma interface visual que permite testar o exemplo.

Uma vez que o servidor esteja conectado:

- tente listar as ferramentas e executar `add`, com os argumentos 2 e 4. Você deve ver 6 no resultado.
- vá para recursos e modelo de recurso e chame "greeting", digite um nome e você deve ver uma saudação com o nome que você forneceu.

### Testando no modo CLI

O inspetor que você executou é, na verdade, um aplicativo Node.js, e `mcp dev` é um wrapper em torno dele.

Você pode iniciá-lo diretamente no modo CLI executando o seguinte comando:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
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
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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