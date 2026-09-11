> [!WARNING]
> A amostragem está obsoleta no MCP `2026-07-28`. Esta lição é mantida para
> implementações legadas. Novos servidores devem se integrar diretamente com uma API
> de provedor de LLM.

# Amostragem - delegar funcionalidades para o Cliente

> A amostragem permanece na especificação `2026-07-28` para compatibilidade e está
> elegível para remoção na primeira revisão lançada em ou após 28 de julho de
> 2027. Exemplos nesta lição podem usar APIs do SDK que implementam `2025-11-25`.
> Veja [O que mudou no MCP: A Especificação 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Em implementações legadas, a Amostragem permite que um servidor MCP solicite ajuda de um LLM
gerenciado pelo cliente. Para novas implementações, chame o provedor de LLM escolhido
diretamente.

Vamos explorar alguns casos de uso e como construir uma solução envolvendo amostragem.

## Visão Geral

Nesta lição, focamos em explicar quando e onde usar a Amostragem e como configurá-la.

## Objetivos de Aprendizagem

Neste capítulo, iremos:

- Explicar o que é a Amostragem e quando usá-la.
- Mostrar como configurar Amostragem no MCP.
- Fornecer exemplos da Amostragem em ação.

## O que é Amostragem e por que usá-la?

A Amostragem é um recurso avançado que funciona da seguinte forma:

```mermaid
sequenceDiagram
    participant User
    participant MCP Client
    participant LLM
    participant MCP Server

    User->>MCP Client: Postagem do autor no blog
    MCP Client->>MCP Server: Chamada da ferramenta (rascunho da postagem no blog)
    MCP Server->>MCP Client: Solicitação de amostragem (criar resumo)
    MCP Client->>LLM: Gerar resumo da postagem no blog
    LLM->>MCP Client: Resultado do resumo
    MCP Client->>MCP Server: Resposta da amostragem (resumo)
    MCP Server->>MCP Client: Postagem completa no blog (rascunho + resumo)
    MCP Client->>User: Postagem do blog pronta
```

### Solicitação de Amostragem

Ok, agora que temos uma visão geral de um cenário crível, vamos falar sobre a solicitação de amostragem que o servidor envia de volta para o cliente. Eis como essa solicitação pode ser no formato JSON-RPC:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "Create a blog post summary of the following blog post: <BLOG POST>"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ],
      "intelligencePriority": 0.8,
      "speedPriority": 0.5
    },
    "systemPrompt": "You are a helpful assistant.",
    "maxTokens": 100
  }
}
```

Algumas coisas aqui valem ser destacadas:

- Prompt, dentro de content -> text, é nosso prompt que é uma instrução para o LLM resumir o conteúdo do post do blog.

- **modelPreferences**. Esta seção é exatamente isso, uma preferência, uma recomendação de qual configuração usar com o LLM. O usuário pode escolher seguir essas recomendações ou alterá-las. Neste caso há recomendações sobre modelo a usar e prioridade entre velocidade e inteligência.
- **systemPrompt**, este é o seu prompt padrão de sistema que dá uma personalidade ao seu LLM e contém instruções de orientação.
- **maxTokens**, esta é outra propriedade usada para indicar quantos tokens são recomendados para essa tarefa.

### Resposta de Amostragem

Esta resposta é o que o Cliente MCP acaba enviando de volta ao Servidor MCP e é o resultado do cliente chamar o LLM, esperar por essa resposta e então construir esta mensagem. Eis como pode parecer em JSON-RPC:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "role": "assistant",
    "content": {
      "type": "text",
      "text": "Here's your abstract <ABSTRACT>"
    },
    "model": "gpt-5",
    "stopReason": "endTurn"
  }
}
```

Note como a resposta é um resumo do post do blog exatamente como pedimos. Também note como o `model` usado não é o que pedimos, mas "gpt-5" em vez de "claude-3-sonnet". Isso é para ilustrar que o usuário pode mudar de ideia sobre o que usar e que sua solicitação de amostragem é uma recomendação.

Ok, agora que entendemos o fluxo principal e a tarefa útil para usá-lo "criação de post de blog + resumo", vamos ver o que precisamos fazer para fazê-lo funcionar.

### Tipos de mensagem

Mensagens de amostragem não se limitam apenas a texto, mas você também pode enviar imagens e áudio. Veja como o JSON-RPC fica diferente:

**Texto**

```json
{
  "type": "text",
  "text": "The message content"
}
```

**Conteúdo de imagem**

```json
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/jpeg"
}
```

**Conteúdo de áudio**

```json
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

> NOTE: Para status atual e orientações de migração, veja a
> [documentação obsoleta de Amostragem](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling).

## Como Configurar Amostragem no Cliente

> Nota: se você está apenas construindo um servidor, não precisa fazer muito aqui.

Em um cliente, você precisa especificar a seguinte funcionalidade assim:

```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

Isso será então reconhecido quando seu cliente escolhido se inicializar com o servidor.

## Exemplo da Amostragem em Ação - Criar um Post de Blog

Vamos codificar um servidor de amostragem juntos, precisamos fazer o seguinte:

1. Criar uma ferramenta no Servidor.
1. Dita ferramenta deve criar uma solicitação de amostragem
1. A ferramenta deve esperar pela resposta da solicitação de amostragem do cliente.
1. Então o resultado da ferramenta deve ser produzido.

Vamos ver o código passo a passo:

### -1- Criar a ferramenta

**python**

```python
@mcp.tool()
async def create_blog(title: str, content: str, ctx: Context[ServerSession, None]) -> str:
    """Create a blog post and generate a summary"""

```

### -2- Criar uma solicitação de amostragem

Estenda sua ferramenta com o seguinte código:

**python**

```python
post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=""
    )

prompt = f"Create an abstract of the following blog post: title: {title} and draft: {content} "

result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
)

```

### -3- Espere pela resposta e retorne a resposta

**python**

```python
post.abstract = result.content.text

posts.append(post)

# retorne o produto completo
return json.dumps({
    "id": post.title,
    "abstract": post.abstract
})
```

### -4- Código completo

**python**

```python
from starlette.applications import Starlette
from starlette.routing import Mount, Host

from mcp.server.fastmcp import Context, FastMCP

from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

import json


from uuid import uuid4
from typing import List
from pydantic import BaseModel


mcp = FastMCP("Blog post generator")

# app = FastAPI()

posts = []

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    abstract: str

posts: List[BlogPost] = []

@mcp.tool()
async def create_blog(title: str, content: str, ctx: Context[ServerSession, None]) -> str:
    """Create a blog post and generate a summary"""

    post = BlogPost(
        id=len(posts) + 1,
        title=title,
        content=content,
        abstract=""
    )

    prompt = f"Create an abstract of the following blog post: title: {title} and draft: {content} "

    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt),
            )
        ],
        max_tokens=100,
    )

    post.abstract = result.content.text

    posts.append(post)

    # retorna o post completo do blog
    return json.dumps({
        "id": post.title,
        "abstract": post.abstract
    })

if __name__ == "__main__":
    print("Starting server...")
    # mcp.run()
    mcp.run(transport="streamable-http")

# execute o app com: python server.py
```

### -5- Testando no Visual Studio Code

Para testar isso no Visual Studio Code, faça o seguinte:

1. Inicie o servidor no terminal
1. Adicione ao *mcp.json* (e certifique-se de que está iniciado) algo parecido com isso:

   ```json
   "servers": {
      "blog-server": {
        "type": "http",
        "url": "http://localhost:8000/mcp"
      }
   }
   ```

1. Digite um prompt:

   ```text
   create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
   ```

1. Permita que a amostragem ocorra. Na primeira vez que testar isso, será apresentado um diálogo adicional que precisará ser aceito, depois verá o diálogo normal perguntando para executar uma ferramenta

1. Inspecione os resultados. Você verá os resultados renderizados de forma agradável no GitHub Copilot Chat, mas também pode inspecionar a resposta JSON bruta.

**Bônus**. As ferramentas do Visual Studio Code têm ótimo suporte para amostragem. Você pode configurar o acesso à Amostragem no seu servidor instalado navegando nele assim:

1. Navegue até a seção de extensões.
1. Selecione o ícone de engrenagem para seu servidor instalado na seção "MCP SERVERS - INSTALLED".
1 Selecione "Configure Model Access" (Configurar Acesso ao Modelo), aqui você pode selecionar quais Modelos o GitHub Copilot pode usar ao realizar amostragem. Você também pode ver todas as solicitações de amostragem que aconteceram recentemente selecionando "Show Sampling requests" (Mostrar solicitações de amostragem).

## Tarefa

Nesta tarefa, você construirá uma amostragem um pouco diferente, nomeadamente uma integração de amostragem que suporte gerar uma descrição de produto. Aqui está seu cenário:

**Cenário**: O colaborador do back office em um e-commerce precisa de ajuda, leva muito tempo para gerar descrições de produtos. Portanto, você deve construir uma solução onde possa chamar uma ferramenta "create_product" com "title" e "keywords" como argumentos e ela deve produzir um produto completo incluindo um campo "description" que deve ser preenchido pelo LLM de um cliente.

DICA: use o que aprendeu antes para construir este servidor e sua ferramenta usando uma solicitação de amostragem.

## Solução

[Solução](./solution/README.md)

## Principais Conclusões

A Amostragem é um recurso poderoso que permite ao servidor delegar tarefas ao cliente quando precisa da ajuda de um LLM.

## O que vem a seguir

- [Capítulo 4 - Implementação prática](../../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->