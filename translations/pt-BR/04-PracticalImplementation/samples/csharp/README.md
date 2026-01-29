# Exemplo

O exemplo anterior mostra como usar um projeto .NET local com o tipo `stdio`. E como executar o servidor localmente em um contêiner. Essa é uma boa solução em muitas situações. No entanto, pode ser útil ter o servidor rodando remotamente, como em um ambiente de nuvem. É aí que o tipo `http` entra em cena.

Olhando para a solução na pasta `04-PracticalImplementation`, ela pode parecer muito mais complexa do que a anterior. Mas, na verdade, não é. Se você olhar de perto o projeto `src/Calculator`, verá que é basicamente o mesmo código do exemplo anterior. A única diferença é que estamos usando uma biblioteca diferente, `ModelContextProtocol.AspNetCore`, para lidar com as requisições HTTP. E alteramos o método `IsPrime` para torná-lo privado, só para mostrar que você pode ter métodos privados no seu código. O resto do código é igual ao anterior.

Os outros projetos são do [.NET Aspire](https://learn.microsoft.com/dotnet/aspire/get-started/aspire-overview). Ter o .NET Aspire na solução melhora a experiência do desenvolvedor durante o desenvolvimento e testes, além de ajudar na observabilidade. Não é obrigatório para rodar o servidor, mas é uma boa prática tê-lo na sua solução.

## Iniciar o servidor localmente

1. No VS Code (com a extensão C# DevKit), navegue até o diretório `04-PracticalImplementation/samples/csharp`.
1. Execute o seguinte comando para iniciar o servidor:

   ```bash
    dotnet watch run --project ./src/AppHost
   ```

1. Quando um navegador abrir o dashboard do .NET Aspire, anote a URL `http`. Deve ser algo como `http://localhost:5058/`.

   ![.NET Aspire Dashboard](../../../../../translated_images/pt-BR/dotnet-aspire-dashboard.0a7095710e9301e90df2efd867e1b675b3b9bc2ccd7feb1ebddc0751522bc37c.png)

## Testar Streamable HTTP com o MCP Inspector

Se você tem Node.js 22.7.5 ou superior, pode usar o MCP Inspector para testar seu servidor.

Inicie o servidor e execute o seguinte comando em um terminal:

```bash
npx @modelcontextprotocol/inspector http://localhost:5058
```

![MCP Inspector](../../../../../translated_images/pt-BR/mcp-inspector.c223422b9b494fb4a518a3b3911b3e708e6a5715069470f9163ee2ee8d5f1ba9.png)

- Selecione `Streamable HTTP` como tipo de transporte.
- No campo Url, insira a URL do servidor anotada anteriormente e acrescente `/mcp`. Deve ser `http` (não `https`), algo como `http://localhost:5058/mcp`.
- Clique no botão Connect.

Uma coisa legal do Inspector é que ele oferece uma boa visibilidade do que está acontecendo.

- Tente listar as ferramentas disponíveis
- Experimente algumas delas, deve funcionar como antes.

## Testar MCP Server com GitHub Copilot Chat no VS Code

Para usar o transporte Streamable HTTP com o GitHub Copilot Chat, altere a configuração do servidor `calc-mcp` criado anteriormente para ficar assim:

```jsonc
// .vscode/mcp.json
{
  "servers": {
    "calc-mcp": {
      "type": "http",
      "url": "http://localhost:5058/mcp"
    }
  }
}
```

Faça alguns testes:

- Peça "3 números primos após 6780". Note como o Copilot usará as novas ferramentas `NextFivePrimeNumbers` e retornará apenas os 3 primeiros números primos.
- Peça "7 números primos após 111", para ver o que acontece.
- Pergunte "John tem 24 pirulitos e quer distribuir todos para seus 3 filhos. Quantos pirulitos cada filho recebe?", para ver o que acontece.

## Fazer o deploy do servidor no Azure

Vamos fazer o deploy do servidor no Azure para que mais pessoas possam usá-lo.

No terminal, navegue até a pasta `04-PracticalImplementation/samples/csharp` e execute o seguinte comando:

```bash
azd up
```

Quando o deploy terminar, você deverá ver uma mensagem assim:

![Azd deployment success](../../../../../translated_images/pt-BR/azd-deployment-success.bd42940493f1b834a5ce6251a6f88966546009b350df59d0cc4a8caabe94a4f1.png)

Pegue a URL e use-a no MCP Inspector e no GitHub Copilot Chat.

```jsonc
// .vscode/mcp.json
{
  "servers": {
    "calc-mcp": {
      "type": "http",
      "url": "https://calc-mcp.gentleriver-3977fbcf.australiaeast.azurecontainerapps.io/mcp"
    }
  }
}
```

## E agora?

Testamos diferentes tipos de transporte e ferramentas de teste. Também fizemos o deploy do seu servidor MCP no Azure. Mas e se nosso servidor precisar acessar recursos privados? Por exemplo, um banco de dados ou uma API privada? No próximo capítulo, veremos como podemos melhorar a segurança do nosso servidor.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.