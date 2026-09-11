# Raízes MCP (Recurso Legado)

> [!WARNING]
> Raízes estão obsoletas a partir do MCP `2026-07-28`. Elas permanecem nesta revisão para
> compatibilidade e são elegíveis para remoção na primeira revisão da especificação
> lançada em ou após 28 de julho de 2027. Novas implementações devem passar
> diretórios ou arquivos por meio de parâmetros de ferramenta, URIs de recursos ou configuração do servidor.


## Visão Geral

Raízes permitem que um cliente MCP informe a um servidor quais locais no sistema de arquivos são relevantes
para a requisição atual. Uma raiz contém um URI `file://` obrigatório e um nome legível por humanos opcional.


sessões de protocolo ou um mecanismo de controle de acesso. O protocolo não
exige que um servidor permaneça dentro das raízes listadas.


## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Explicar o que as Raízes MCP representam e o que elas não representam.
- Reconhecer o fluxo atual de múltiplas viagens `roots/list`.
- Aplicar controles de segurança independentemente das Raízes.
- Migrar novas implementações para alternativas suportadas.

## Dados da Raiz

Um cliente retorna cada raiz como um URI `file://` com um nome opcional para exibição:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Clientes devem expor apenas locais aprovados pelo usuário. Servidores devem tratar
o resultado como uma orientação sobre arquivos relevantes, não como prova de autorização.

## Fluxo MCP 2026-07-28

Um cliente que suporta Raízes declara a capacidade em cada requisição:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Enquanto processa uma requisição do cliente, um servidor pode retornar um
`InputRequiredResult` contendo uma requisição de entrada `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

O cliente coleta as raízes aprovadas e tenta novamente a requisição original com as
`inputResponses` correspondentes e o `requestState` inalterado. Esse padrão de múltiplas viagens
mantém o protocolo sem estado; não há handshake `initialize` nem
sessão ao nível de protocolo.

## Comportamento Legado 2025-11-25

No MCP `2025-11-25`, clientes anunciavam Raízes durante a inicialização. Um servidor
poderia emitir uma requisição direta `roots/list`, e um cliente poderia enviar
`notifications/roots/list_changed` quando suas raízes mudavam.

Esse ciclo de vida é um comportamento legado. Não combine seus exemplos de inicialização ou
notificação com uma implementação `2026-07-28`.

## Substituições Recomendadas

### Parâmetros de Ferramenta

Torne o diretório ou arquivo requerido explícito no esquema da ferramenta:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URIs de Recursos

Use Recursos MCP quando o servidor puder expor os arquivos relevantes por meio de URIs estáveis.
Isso mantém a descoberta e recuperação explícitas.

### Configuração do Servidor

Para implantações fixas, configure os diretórios permitidos quando o servidor iniciar.
Isso é frequentemente mais claro do que descobri-los durante uma chamada de ferramenta.

## Requisitos de Segurança

Qualquer que seja a substituição escolhida:

- Obtenha consentimento do usuário antes de expor locais do sistema de arquivos.
- Canonicalize e valide caminhos para evitar traversal.
- Aplique autorização e sandboxing independentemente dos valores das raízes.
- Reavalie permissões quando um arquivo for acessado, não apenas quando for listado.
- Evite retornar caminhos sensíveis em logs ou mensagens de erro.

## Pontos Principais

- Raízes descrevem locais relevantes do sistema de arquivos; elas não armazenam estado de conversa.

- Raízes são uma orientação, não uma barreira de controle de acesso.
- MCP `2026-07-28` transporta a capacidade por requisição e usa
  `InputRequiredResult` para `roots/list`.
- Novas implementações devem usar parâmetros de ferramentas, URIs de recursos ou
  configuração do servidor em vez disso.

## Recursos Adicionais

- [Raízes no MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Registro de recursos descontinuados](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [O que mudou no MCP: A especificação 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->