# Executar este exemplo

Recomenda-se instalar `uv`, mas não é obrigatório. Veja [instruções](https://docs.astral.sh/uv/#highlights)

## -1- Instalar as dependências

```bash
npm install
```

## -3- Executar o exemplo

```bash
npm run build
```

## -4- Testar o exemplo

Com o servidor a correr num terminal, abra outro terminal e execute o seguinte comando:

```bash
npm run inspector
```

Isto deverá iniciar um servidor web com uma interface visual que lhe permitirá testar o exemplo.

Depois de o servidor estar conectado:

- Experimente listar ferramentas e executar `add`, com os argumentos 2 e 4. Deverá ver 6 no resultado.
- Vá a recursos e ao modelo de recurso e chame "greeting". Escreva um nome e deverá ver uma saudação com o nome que forneceu.

### Testar no modo CLI

O inspetor que executou é, na verdade, uma aplicação Node.js e `mcp dev` é um wrapper em torno dela.

Pode iniciá-lo diretamente no modo CLI executando o seguinte comando:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Isto irá listar todas as ferramentas disponíveis no servidor. Deverá ver o seguinte output:

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

Para invocar uma ferramenta, escreva:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Deverá ver o seguinte output:

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
> Normalmente é muito mais rápido executar o inspetor no modo CLI do que no navegador.
> Leia mais sobre o inspetor [aqui](https://github.com/modelcontextprotocol/inspector).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.