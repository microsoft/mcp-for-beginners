# Estudo de Caso: Publicando em Redes Sociais a partir de um Agente com um Servidor MCP Remoto

> **Aviso:** Vários serviços e projetos open-source podem publicar em redes sociais, e uma equipe também poderia integrar diretamente a API de cada rede. O cenário abaixo é fornecido como um exemplo prático de como um **servidor MCP remoto com capacidade de escrita** pode ser projetado e utilizado. Publora é um serviço comercial com uma camada gratuita; os padrões descritos aqui se aplicam a qualquer servidor MCP que execute ações irreversíveis em nome do usuário.

## Visão Geral

Agentes são bons em redigir conteúdo e ruins em entregá-lo. Um modelo pode escrever um anúncio de lançamento em segundos, e então o trabalho para: publicar significa uma API por rede, um app OAuth por rede, e um conjunto diferente de regras de mídia para cada uma. A maioria das equipes resolve isso copiando o texto no navegador manualmente.

Este estudo de caso analisa como essa última etapa é concluída com um único servidor MCP remoto e — mais útil para quem constrói um — as decisões de design que um servidor **com capacidade de escrita** deve acertar. Ler dados é tolerante. Publicar não é: uma chamada de ferramenta errada é visível para uma audiência e não pode ser desfeita.

## Cenário

Uma pequena equipe de relações com desenvolvedores redige postagens dentro de um agente (Claude, VS Code, Cursor — o cliente não importa). Eles querem que o agente:

- veja quais contas sociais a equipe conectou,
- redija um post e o mantenha como rascunho para aprovação humana,
- anexe uma imagem,
- agende para várias redes em um horário escolhido,
- e depois reporte como ele performou.

Crucialmente, eles querem que o agente seja *incapaz* de publicar acidentalmente enquanto ainda estão experimentando.

## Ferramentas Usadas

- [Servidor MCP Publora](https://github.com/publora/mcp-server) — um servidor MCP remoto (`streamable-http`) que expõe ferramentas de publicação, agendamento, mídia e análise do LinkedIn. Registrado no registro oficial MCP como `com.publora/mcp-server`.

## Workflow Passo a Passo

1. **Conectar o servidor.** Clientes que usam OAuth completam o fluxo de código de autorização com PKCE contra a própria tela de consentimento do servidor; clientes que não usam, como CLIs headless, usam uma chave API Publora em um cabeçalho. Ambos os caminhos são suportados, e qual você obtém depende do cliente, não do servidor.
2. **Listar conexões.** O agente chama `list_connections` e recebe as contas conectadas com seus identificadores.
3. **Redigir.** O agente chama `create_post` *sem* hora agendada. O post é guardado como rascunho — nada é publicado.
4. **Anexar mídia.** URLs públicos de imagem são passados na mesma chamada; o servidor os baixa e valida.
5. **Agendar.** Após aprovação humana, `update_post` define o status como agendado com um horário ISO 8601.
6. **Medir.** Para o LinkedIn, `linkedin_post_stats` retorna engajamento uma vez que o post está ao vivo.

## Exemplo de Prompt

```text
Which social accounts do I have connected?
Draft a post announcing our new changelog page, attach the screenshot at
https://example.com/changelog.png, and keep it as a draft — do not publish it.
Once I approve, schedule it to LinkedIn and Bluesky for tomorrow at 09:00 UTC.
```

## Diagrama Mermaid

```mermaid
flowchart TD
    A[Prompt do usuário em um cliente MCP] --> B[Cliente realiza OAuth com o servidor]
    B --> C[listar_conexões]
    C --> D{Redes alvo conectadas?}
    D -- No --> E[Agente informa quais estão faltando]
    D -- Yes --> F[criar_post sem scheduledTime -> rascunho]
    F --> G[Humano revisa o rascunho]
    G -- Approved --> H[update_post: status=agendado]
    G -- Rejected --> I[deletar_post]
    H --> J[Servidor publica no horário agendado]
    J --> K[linkedin_post_stats para engajamento]
```

## Implementação Técnica

As lições abaixo são a parte transferível deste estudo de caso.

### Descoberta aberta, execução autenticada

`tools/list` é servido sem credenciais; toda `tools/call` requer um token
e caso contrário retorna `401` com um cabeçalho `WWW-Authenticate` apontando para os
metadados do recurso protegido. O endpoint legado do servidor também responde a uma
`initialize` não autenticada para clientes em versões de protocolo anteriores a
`2026-07-28`; clientes atuais não usam essa negociação.

Essa divisão específica do servidor permite que registros, catálogos e clientes inspecionem nomes,
esquemas e anotações das ferramentas sem um segredo, enquanto previne execução anônima.
Descoberta aberta é uma escolha de implantação, não um requisito MCP; uma
implantação protegida pode também exigir autorização para `tools/list`.

### Registro: registro dinâmico de clientes, e o que o substitui

O servidor anuncia `/.well-known/oauth-protected-resource` e `/.well-known/oauth-authorization-server` e suporta o fluxo de código de autorização com PKCE (`S256`), tokens de atualização e **registro dinâmico de clientes**.

O registro dinâmico removeu a etapa manual para clientes legados: sem ele,
cada cliente precisava de um `client_id` pré-emitido pelo fornecedor.

Trate isso como comportamento de compatibilidade e não como o design a ser copiado. A revisão da especificação de `2026-07-28` deprecia registro dinâmico de clientes em favor dos Documentos de Metadados de ID do Cliente (CIMD), onde o cliente hospeda um documento de metadados em uma URL HTTPS estável e essa URL *é* o `client_id`. O DCR continua funcionando por ora, mas um servidor sendo construído hoje deve planejar para CIMD e manter DCR apenas para clientes mais antigos.

### Anotações de ferramenta não são decoração

Cada ferramenta carrega um `title` e os avisos aplicáveis: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

Dois motivos para investir neles. Primeiro, clientes usam os avisos para decidir o que confirmar com o usuário — um cliente pode executar automaticamente uma consulta somente leitura e parar para aprovação antes de uma exclusão. A especificação é explícita ao dizer que as anotações são avisos não confiáveis, não um mecanismo de autorização: elas moldam o que um cliente oferece fazer, não impedem nada no servidor, e um servidor ainda deve impor suas próprias regras. Segundo, os principais diretórios de conectores agora *exigem* elas para revisão; um servidor cujas ferramentas faltam títulos e avisos será rejeitado independentemente de quão bem funcione.

### Faça identificadores impossível de inventar

Identificadores da plataforma são strings opacas retornadas por `list_connections`, e a descrição do esquema diz explicitamente que devem ser copiados literalmente e nunca adivinhados. O servidor rejeita qualquer outro valor.

Modelos são adivinhadores fluentes. Qualquer servidor com capacidade de escrita deve assumir que um identificador será eventualmente imaginado e fazer esse caminho falhar de forma evidente e precoce, ao invés de agir baseado em um valor aparentemente plausível.

### Falhe antes de publicar, com uma mensagem acionável

Algumas redes rejeitam posts somente texto e requerem imagem ou vídeo. Isso é validado quando o post é agendado, e o erro nomeia a plataforma e o requisito ausente.

Um agente pode se recuperar de "Instagram requer mídia — anexe uma imagem ou vídeo" sem outra volta. Ele não pode se recuperar de um `400` genérico.

### Torne as tentativas seguras

As duas ferramentas que criam conteúdo, `create_post` e `update_post`, aceitam uma chave de idempotência: reusá-la com uma requisição idêntica reproduz a resposta original ao invés de criar um segundo post. Runtimes de agentes tentam novamente em timeouts; sem idempotência, uma resposta lenta vira publicação duplicada. As outras ferramentas de escrita — exclusões, passos de mídia, reações e comentários no LinkedIn — não aceitam uma, então uma nova tentativa ali não é automaticamente segura. Vale a pena saber quais das suas mutações estão protegidas e quais não.

### Forneça uma forma de testar que não publica nada


O servidor aceita um destino reservado, `publora-playground`, que é validado e reconhecido como um destino real e então descartado — nada chega a uma conta ativa. Isso está descrito no próprio esquema da ferramenta, que qualquer cliente pode ler sem credenciais: o campo `platforms` de `create_post` documenta-o como "um destino de teste de conexão que não requer conexão real — a postagem é reconhecida e descartada, nada é publicado". Invoque-o passando-o como a única entrada: `platforms: ["publora-playground"]`.

Isso acabou se tornando um dos detalhes mais úteis de toda a superfície. Avaliadores de diretórios de conectores, contribuintes e CI podem exercitar todo o caminho de escrita de ponta a ponta sem risco para uma audiência real. Qualquer servidor MCP com ações irreversíveis se beneficia de um destino no-op documentado.

## Resultados e Impacto

- A etapa de publicação mudou de um navegador para a mesma conversa onde o conteúdo é escrito, e um hábito de rascunho primeiro mantém um humano no loop. Seja preciso sobre o que isso é: um rascunho é uma convenção, não uma barreira. A mesma credencial pode agendar ou publicar, então quem precisar de um portão real de aprovação deve aplicá-lo fora da superfície da ferramenta — credenciais separadas, ou uma camada de política na frente do servidor.
- Diferenças por rede — requisitos de mídia, encadeamento, controles de resposta — são tratadas uma vez no servidor ao invés de em cada agente que fala com ele.
- O mesmo servidor suporta vários clientes MCP sem credenciais pré-emitiadas.
    Clientes atuais podem usar Documentos de Metadados de ID do Cliente; DCR continua sendo uma alternativa
    para clientes mais antigos.
- As restrições de design acima foram moldadas tanto por revisões de diretórios de conectores quanto por usuários: anotações, OAuth e um destino de teste seguro foram cada um requerido por pelo menos um deles.

## Referências

- [Servidor MCP Publora (fonte)](https://github.com/publora/mcp-server)
- [Documentação da API e MCP Publora](https://docs.publora.com)
- [Entrada do Registro MCP: `com.publora/mcp-server`](https://registry.modelcontextprotocol.io/v0/servers?search=com.publora/mcp-server)
- [Especificação MCP — Autorização](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Especificação MCP — Anotações em ferramentas](https://modelcontextprotocol.io/docs/concepts/tools)

## O que vem a seguir

- Pegue um servidor MCP que você está construindo e verifique as três vitórias mais econômicas aqui: anotações em cada ferramenta, uma chave de idempotência em cada escrita, e um destino no-op documentado.
- Experimente a divisão de descoberta aberta: chame `tools/list` contra um servidor remoto público sem credenciais, então chame uma ferramenta e inspecione o desafio `401`.
- Considere o que "desfazer" significa para o seu domínio. A publicação tem rascunhos e exclusão; se suas ações não têm equivalente, a confirmação pertence ao design da ferramenta, não ao prompt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->