# Exemplo

O exemplo anterior mostra como usar um projeto .NET local com o tipo `stdio`. E como executar o servidor localmente num contentor. Esta é uma boa solução em muitas situações. No entanto, pode ser útil ter o servidor a correr remotamente, como num ambiente na cloud. É aqui que entra o tipo `http`.

Ao observar a solução na pasta `04-PracticalImplementation`, pode parecer muito mais complexa do que a anterior. Mas, na realidade, não é. Se olhar atentamente para o projeto `src/Calculator`, verá que é essencialmente o mesmo código do exemplo anterior. A única diferença é que estamos a usar uma biblioteca diferente, `ModelContextProtocol.AspNetCore`, para tratar as requisições HTTP. E alterámos o método `IsPrime` para o tornar privado, apenas para mostrar que pode ter métodos privados no seu código. O resto do código é igual ao anterior.

Os outros projetos são da [Aspire](https://aspire.dev/get-started/what-is-aspire/). Ter Aspire na solução melhora a experiência do programador durante o desenvolvimento e teste e ajuda na observabilidade. Não é obrigatório para correr o servidor, mas é uma boa prática tê-lo na sua solução.

## Iniciar o servidor localmente

1. No VS Code (com a extensão C# DevKit), navegue até ao diretório `04-PracticalImplementation/samples/csharp`.
1. Execute o seguinte comando para iniciar o servidor:

   ```bash
    dotnet watch run --project ./src/AppHost
   ```

1. Quando um navegador abrir o painel da Aspire, note o URL `http`. Deve ser algo como `http://localhost:5058/`.

   ![Painel Aspire](../../../../../translated_images/pt-PT/dotnet-aspire-dashboard.0a7095710e9301e9.webp)

## Testar Streamable HTTP com o MCP Inspector

Se tiver Node.js 22.7.5 ou superior, pode usar o MCP Inspector para testar o seu servidor.

Inicie o servidor e execute o seguinte comando num terminal:

```bash
npx @modelcontextprotocol/inspector http://localhost:5058
```

![MCP Inspector](../../../../../translated_images/pt-PT/mcp-inspector.c223422b9b494fb4.webp)

- Selecione `Streamable HTTP` como o tipo de transporte.
- No campo URL, insira o URL do servidor anotado anteriormente e acrescente `/mcp`. Deve ser `http` (não `https`), algo como `http://localhost:5058/mcp`.
- selecione o botão Conectar.

Uma coisa boa do Inspector é que fornece uma boa visibilidade sobre o que está a acontecer.

- Experimente listar as ferramentas disponíveis
- Experimente algumas delas, deve funcionar como antes.

## Testar MCP Server com o GitHub Copilot Chat no VS Code

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

- Pergunte por "3 números primos depois de 6780". Note como o Copilot usará as novas ferramentas `NextFivePrimeNumbers` e apenas retornará os 3 primeiros números primos.
- Pergunte por "7 números primos depois de 111", para ver o que acontece.
- Pergunte por "O João tem 24 rebuçados e quer distribuí-los pelos seus 3 filhos. Quantos rebuçados tem cada filho?", para ver o que acontece.

## Fazer o deploy do servidor para Azure

Vamos fazer o deploy do servidor para o Azure para que mais pessoas possam usá-lo.

Num terminal, navegue até à pasta `04-PracticalImplementation/samples/csharp` e execute o seguinte comando:

```bash
azd up
```

Quando o deploy terminar, deverá ver uma mensagem como esta:

![Deploy azd com sucesso](../../../../../translated_images/pt-PT/azd-deployment-success.bd42940493f1b834.webp)

Copie o URL e use-o no MCP Inspector e no GitHub Copilot Chat.

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

## O que vem a seguir?

Experimentámos diferentes tipos de transporte e ferramentas de teste. Também fizemos o deploy do seu servidor MCP para o Azure. Mas e se o nosso servidor precisar de aceder a recursos privados? Por exemplo, uma base de dados ou uma API privada? No próximo capítulo, veremos como podemos melhorar a segurança do nosso servidor.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->