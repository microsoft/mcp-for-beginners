# MCP Apps

MCP Apps é um novo paradigma no MCP. A ideia é que você não apenas responda com dados de uma chamada de ferramenta, mas também forneça informações sobre como essa informação deve ser interagida. Isso significa que os resultados da ferramenta agora podem conter informações de interface do usuário. Por que queremos isso? Bem, considere como você faz as coisas hoje. Você provavelmente consome os resultados de um MCP Server colocando algum tipo de frontend na frente dele, esse é um código que você precisa escrever e manter. Às vezes é isso que você quer, mas às vezes seria ótimo se você pudesse simplesmente trazer um trecho de informação que seja autocontido, que tenha tudo, desde os dados até a interface do usuário.

## Visão Geral

Esta lição fornece orientações práticas sobre MCP Apps, como começar com eles e como integrá-los em seus aplicativos Web existentes. MCP Apps é uma adição muito nova ao Padrão MCP.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Explicar o que são MCP Apps.
- Quando usar MCP Apps.
- Construir e integrar seus próprios MCP Apps.

## MCP Apps - como funciona

A ideia dos MCP Apps é fornecer uma resposta que essencialmente é um componente a ser renderizado. Tal componente pode ter tanto visuais quanto interatividade, por exemplo cliques em botões, entrada do usuário e mais. Vamos começar com o lado do servidor e nosso MCP Server. Para criar um componente MCP App você precisa criar uma ferramenta, mas também o recurso da aplicação. Essas duas partes são conectadas por um resourceUri.

Aqui está um exemplo. Vamos tentar visualizar o que está envolvido e quais partes fazem o que:

```text
server.ts -- responsible for registering tools and the component as a UI component
src/
  mcp-app.ts -- wiring up event handlers
mcp-app.html -- the user interface
```

Este visual descreve a arquitetura para criar um componente e sua lógica.

```mermaid
flowchart LR
  subgraph Backend[Backend: Servidor MCP]
    T["Registrar ferramentas: registerAppTool()"]
    C["Registrar recurso do componente: registerAppResource()"]
    U[resourceUri]
    T --- U
    C --- U
  end

  subgraph Parent[Página Web Pai]
    H[Aplicação hospedeira]
    IFRAME[Contêiner IFrame]
    H -->|Injetar UI do App MCP| IFRAME
  end

  subgraph Frontend[Frontend: App MCP dentro do IFrame]
    UI["Interface do usuário: mcp-app.html"]
    EH["Manipuladores de eventos: src/mcp-app.ts"]
    UI --> EH
  end

  IFRAME --> UI
  EH -->|Clique dispara chamada de ferramenta no servidor| T
  T -->|Dados do resultado da ferramenta| EH
  EH -->|Enviar mensagem para a página pai| H
```
Vamos tentar descrever as responsabilidades para backend e frontend respectivamente.

### O backend

Há duas coisas que precisamos realizar aqui:

- Registrar as ferramentas com as quais queremos interagir.
- Definir o componente.

**Registrando a ferramenta**

```typescript
registerAppTool(
    server,
    "get-time",
    {
      title: "Get Time",
      description: "Returns the current server time.",
      inputSchema: {},
      _meta: { ui: { resourceUri } }, // Vincula esta ferramenta ao seu recurso de interface do usuário
    },
    async () => {
      const time = new Date().toISOString();
      return { content: [{ type: "text", text: time }] };
    },
  );

```

O código acima descreve o comportamento, onde ele expõe uma ferramenta chamada `get-time`. Ela não recebe entradas, mas acaba produzindo a hora atual. Temos a capacidade de definir um `inputSchema` para ferramentas em que precisamos aceitar entrada do usuário.

**Registrando o componente**

No mesmo arquivo, também precisamos registrar o componente:

```typescript
const resourceUri = "ui://get-time/mcp-app.html";

// Registra o recurso, que retorna o HTML/JavaScript empacotado para a interface do usuário.
registerAppResource(
  server,
  resourceUri,
  resourceUri,
  { mimeType: RESOURCE_MIME_TYPE },
  async () => {
    const html = await fs.readFile(path.join(DIST_DIR, "mcp-app.html"), "utf-8");

    return {
    contents: [
        { uri: resourceUri, mimeType: RESOURCE_MIME_TYPE, text: html },
    ],
    };
  },
);
```

Note como mencionamos `resourceUri` para conectar o componente com suas ferramentas. É interessante também o callback onde carregamos o arquivo UI e retornamos o componente.

### O frontend do componente

Assim como no backend, há duas partes aqui:

- Um frontend escrito em HTML puro.
- Código que lida com eventos e o que fazer, por exemplo, chamar ferramentas ou enviar mensagens para a janela pai.

**Interface do usuário**

Vamos dar uma olhada na interface do usuário.

```html
<!-- mcp-app.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Get Time App</title>
  </head>
  <body>
    <p>
      <strong>Server Time:</strong> <code id="server-time">Loading...</code>
    </p>
    <button id="get-time-btn">Get Server Time</button>
    <script type="module" src="/src/mcp-app.ts"></script>
  </body>
</html>
```

**Conexão dos eventos**

A última parte é a conexão dos eventos. Isso significa identificar qual parte da nossa UI precisa de handlers de evento e o que fazer se eventos forem disparados:

```typescript
// mcp-app.ts

import { App } from "@modelcontextprotocol/ext-apps";

// Obter referências dos elementos
const serverTimeEl = document.getElementById("server-time")!;
const getTimeBtn = document.getElementById("get-time-btn")!;

// Criar instância do aplicativo
const app = new App({ name: "Get Time App", version: "1.0.0" });

// Manipular resultados da ferramenta do servidor. Defina antes de `app.connect()` para evitar
// perder o resultado inicial da ferramenta.
app.ontoolresult = (result) => {
  const time = result.content?.find((c) => c.type === "text")?.text;
  serverTimeEl.textContent = time ?? "[ERROR]";
};

// Conectar clique do botão
getTimeBtn.addEventListener("click", async () => {
  // `app.callServerTool()` permite que a interface solicite dados atualizados do servidor
  const result = await app.callServerTool({ name: "get-time", arguments: {} });
  const time = result.content?.find((c) => c.type === "text")?.text;
  serverTimeEl.textContent = time ?? "[ERROR]";
});

// Conectar ao host
app.connect();
```

Como você pode ver acima, este é um código normal para conectar elementos do DOM a eventos. Vale destacar a chamada para `callServerTool` que acaba chamando uma ferramenta no backend.

## Lidando com entrada do usuário

Até agora, vimos um componente que tem um botão que, quando clicado, chama uma ferramenta. Vamos ver se podemos adicionar mais elementos de UI como um campo de entrada e ver se podemos enviar argumentos para uma ferramenta. Vamos implementar uma funcionalidade de FAQ. Veja como deve funcionar:

- Deve haver um botão e um elemento de entrada onde o usuário digita uma palavra-chave para procurar, por exemplo "Shipping" (Envio). Isso deve chamar uma ferramenta no backend que faz uma busca nos dados de FAQ.
- Uma ferramenta que suporta a busca FAQ mencionada.

Vamos adicionar o suporte necessário ao backend primeiro:

```typescript
const faq: { [key: string]: string } = {
    "shipping": "Our standard shipping time is 3-5 business days.",
    "return policy": "You can return any item within 30 days of purchase.",
    "warranty": "All products come with a 1-year warranty covering manufacturing defects.",
  }

registerAppTool(
    server,
    "get-faq",
    {
      title: "Search FAQ",
      description: "Searches the FAQ for relevant answers.",
      inputSchema: zod.object({
        query: zod.string().default("shipping"),
      }),
      _meta: { ui: { resourceUri: faqResourceUri } }, // Vincula esta ferramenta ao seu recurso de interface do usuário
    },
    async ({ query }) => {
      const answer: string = faq[query.toLowerCase()] || "Sorry, I don't have an answer for that.";
      return { content: [{ type: "text", text: answer }] };
    },
  );
```

O que estamos vendo aqui é como preenchemos `inputSchema` e damos um esquema `zod` assim:

```typescript
inputSchema: zod.object({
  query: zod.string().default("shipping"),
})
```

No esquema acima declaramos que temos um parâmetro de entrada chamado `query` e que ele é opcional com um valor padrão de "shipping".

Ok, vamos para *mcp-app.html* ver qual UI precisamos criar para isso:

```html
<div class="faq">
    <h1>FAQ response</h1>
    <p>FAQ Response: <code id="faq-response">Loading...</code></p>
    <input type="text" id="faq-query" placeholder="Enter FAQ query" />
    <button id="get-faq-btn">Get FAQ Response</button>
  </div>
```

Ótimo, agora temos um elemento de entrada e um botão. Vamos para *mcp-app.ts* a seguir para conectar esses eventos:

```typescript
const getFaqBtn = document.getElementById("get-faq-btn")!;
const faqQueryInput = document.getElementById("faq-query") as HTMLInputElement;

getFaqBtn.addEventListener("click", async () => {
  const query = faqQueryInput.value;
  const result = await app.callServerTool({ name: "get-faq", arguments: { query } });
  const faq = result.content?.find((c) => c.type === "text")?.text;
  faqResponseEl.textContent = faq ?? "[ERROR]";
});
```

No código acima nós:

- Criamos referências para os elementos interessantes da UI.
- Lidamos com o clique do botão para extrair o valor do elemento de entrada e também chamamos `app.callServerTool()` com `name` e `arguments` onde este último está passando `query` como valor.

O que realmente acontece quando você chama `callServerTool` é que ele envia uma mensagem para a janela pai e essa janela acaba chamando o MCP Server.

### Experimente

Ao tentar isso, devemos agora ver o seguinte:

![](../../../../translated_images/pt-BR/faq.f78abe6b2cc68c83.webp)

e aqui onde tentamos com entrada como "warranty" (garantia)

![](../../../../translated_images/pt-BR/faq-input.3e276f1c3d7e061e.webp)

Para executar este código, vá para a [Seção de Código](./code/README.md)

## Testando no Visual Studio Code

O Visual Studio Code tem ótimo suporte para MVP Apps e provavelmente é uma das maneiras mais fáceis de testar seus MCP Apps. Para usar o Visual Studio Code, adicione uma entrada de servidor no *mcp.json* assim:

```json
"my-mcp-server-7178eca7": {
    "url": "http://localhost:3001/mcp",
    "type": "http"
  }
```

Então inicie o servidor, você deve conseguir se comunicar com seu MVP App através da Janela de Chat, desde que tenha o GitHub Copilot instalado.

disparando via prompt, por exemplo "#get-faq":

![Prompt de execução no Visual Studio](../../../../translated_images/pt-BR/vscode-run.16cbab9436499f32.webp)

e assim como quando você executou pelo navegador, ele renderiza do mesmo jeito assim:

![UI Visual Studio Code](../../../../translated_images/pt-BR/vscode-ui.f2771dcfce25ca0f.webp)

## Tarefa

Crie um jogo de pedra, papel e tesoura. Deve consistir no seguinte:

UI:

- um menu suspenso com opções
- um botão para enviar uma escolha
- um rótulo mostrando quem escolheu o que e quem ganhou

Servidor:

- deve ter uma ferramenta pedra, papel e tesoura que recebe "choice" como entrada. Também deve renderizar uma escolha do computador e determinar o vencedor

## Solução

[Soluição](./assignment/README.md)

## Resumo

Aprendemos sobre esse novo paradigma MCP Apps. É um novo paradigma que permite que MCP Servers tenham uma opinião não apenas sobre os dados, mas também sobre como esses dados devem ser apresentados.

Além disso, aprendemos que esses MCP Apps são hospedados dentro de um IFrame e para se comunicarem com os MCP Servers eles precisam enviar mensagens para o app web pai. Existem várias bibliotecas para JavaScript puro, React e mais, que facilitam essa comunicação.

## Principais Conclusões

Aqui está o que você aprendeu:

- MCP Apps é um novo padrão que pode ser útil quando você quer entregar tanto dados quanto recursos de UI.
- Esses tipos de apps rodam em um IFrame por razões de segurança.

## O que vem a seguir

- [Capítulo 4](../../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos empenhemos em garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas resultantes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->