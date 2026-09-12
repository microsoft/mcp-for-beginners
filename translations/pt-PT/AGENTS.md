# AGENTS.md

## Visão Geral do Projeto

**MCP para Iniciantes** é um currículo educativo open-source para aprender o Model Context Protocol (MCP) - uma estrutura padronizada para interações entre modelos de IA e aplicações clientes. Este repositório fornece materiais de aprendizagem abrangentes com exemplos práticos de código em várias linguagens de programação.

### Tecnologias Principais

- **Linguagens de Programação**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bases de Dados**: PostgreSQL com extensão pgvector
- **Plataformas Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Ferramentas de Build**: npm, Maven, pip, Cargo
- **Documentação**: Markdown com tradução automática multilíngue (48+ línguas)

### Arquitetura

- **11 Módulos Centrais (00-11)**: Caminho de aprendizagem sequencial desde fundamentos até tópicos avançados
- **Hands-on Labs**: Exercícios práticos com código solução completo em várias linguagens
- **Projetos Exemplares**: Implementações funcionais de servidores e clientes MCP
- **Sistema de Tradução**: Workflow automatizado GitHub Actions para suporte multilíngue
- **Imagens**: Diretório centralizado de imagens com versões traduzidas

## Comandos de Configuração

Este é um repositório focado em documentação. A maior parte da configuração ocorre dentro dos projetos exemplares e labs individuais.

### Configuração do Repositório

```bash
# Clone o repositório
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Trabalhar com Projetos Exemplares

Os projetos exemplares estão localizados em:
- `03-GettingStarted/samples/` - Exemplos específicos por linguagem
- `03-GettingStarted/01-first-server/solution/` - Primeiras implementações de servidores
- `03-GettingStarted/02-client/solution/` - Implementações de clientes
- `11-MCPServerHandsOnLabs/` - Labs abrangentes de integração de base de dados

Cada projeto exemplar contém suas próprias instruções de configuração:

#### Projetos TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Projetos Python
```bash
cd <project-directory>
pip install -r requirements.txt
# ou
pip install -e .
python main.py
```

#### Projetos Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Fluxo de Desenvolvimento

### Preparação MCP 7-28

#### Lista de verificação de prontidão do Repo

- [x] **Clareza para novos contribuintes**: Este ficheiro define o propósito do repositório,
  estrutura, regras de contribuição e caminhos de configuração exemplares.
- [x] **Comandos de build/test/lint com flags exatas**:
  - Lint da documentação do repositório:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Auditoria do padrão de links da documentação:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validação do exemplo TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validação do exemplo Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validação do exemplo Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Um fluxo de trabalho realista que pode tornar-se uma ferramenta MCP**:
  `validate_curriculum_change`
- [x] **Entradas/saídas são explícitas** (ver especificação abaixo).
- [x] **Permissões e modos de falha estão documentados** (ver especificação abaixo).
- [x] **Testabilidade CI é explícita** (comandos determinísticos, códigos de saída explícitos,
  e saídas legíveis por máquinas).

#### Fluxo de trabalho candidato a ferramenta MCP: `validate_curriculum_change`

##### Objetivo

Validar alterações na documentação do currículo e saúde do código exemplo representativo
antes do merge.

##### Entradas

- `changed_paths: string[]` (obrigatório) - caminhos relativos alterados no PR.
- `run_docs_lint: boolean` (padrão `true`)
- `run_links_audit: boolean` (padrão `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (padrão todos `false`)

##### Saídas

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permissões

- Ler ficheiros do workspace e escrever artefactos gerados pela ferramenta (ex.: relatórios
  lint, logs de teste) apenas; sem escrita em `translations/` ou
  `translated_images/`.
- Executar comandos shell locais.
- Acesso opcional à rede somente para restauração de pacotes (`npm ci`,
  `python -m pip install`, resolução de dependências `mvn`).
- Sem permissão para push, merge ou modificação de `translations/` ou
  `translated_images/`.

##### Modos de falha

- `E_NO_INPUT_PATHS`: `changed_paths` vazio.
- `E_INVALID_PATH`: caminho de entrada que escapa a raiz do repositório.
- `E_LINT_FAILED`: lint markdown termina com código diferente de zero.
- `E_LINK_AUDIT_FAILED`: comando de auditoria de links termina com código diferente de zero.
- `E_SAMPLE_TEST_FAILED`: teste/build do exemplo termina com código diferente de zero.
- `E_TIMEOUT`: comando excedeu o timeout configurado.

##### Contrato CI recomendado

Para automatizar a validação, configure um job CI que:

- Seja acionado por pull requests que alterem `*.md`, código exemplo ou este ficheiro.
- Execute os comandos exactos acima listados.
- Persista logs como artefactos.
- Falhe no job em qualquer código de saída diferente de zero.

#### Se publicar um servidor MCP deste repositório

- [ ] Leia o changelog final do MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verifique que a versão do SDK selecionada suporta o MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Remova as suposições de sessão e handshake; trate cada pedido como
  autónomo:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Envie os cabeçalhos `Mcp-Method` e `Mcp-Name` para pedidos HTTP crus:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Audite códigos de erro codificados diretamente (`missing resource` mudou de `-32002` para `-32602`).

- [ ] Migrar Roots, Sampling, Logging e Dynamic Client depreciados
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrar da API experimental `2025-11-25` Tasks:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Rever autorização para o reforço de OAuth e OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Estrutura da Documentação

- **Módulos 00-11**: Conteúdo curricular principal em ordem sequencial
- **translations/**: Versões específicas de idioma (geradas automaticamente, não editar diretamente)
- **translated_images/**: Versões localizadas das imagens (geradas automaticamente)
- **images/**: Imagens e diagramas originais

### Como Efetuar Alterações na Documentação

1. Editar apenas os ficheiros markdown em inglês nas diretórias principais dos módulos (00-11)
2. Atualizar imagens na diretoria `images/` se necessário
3. A ação co-op-translator do GitHub Action gera automaticamente as traduções
4. As traduções são regeneradas ao fazer push para a branch main

### Trabalhar com Traduções

- **Tradução automatizada**: O fluxo de trabalho do GitHub Actions gere todas as traduções
- **Não editar manualmente** ficheiros na diretoria `translations/`
- Os metadados da tradução estão incluídos em cada ficheiro traduzido
- Idiomas suportados: mais de 48 idiomas incluindo Árabe, Chinês, Francês, Alemão, Hindi, Japonês, Coreano, Português, Russo, Espanhol, e muitos mais

## Instruções de Teste

### Validação da Documentação

Como esta é principalmente uma repositório de documentação, os testes focam-se em:

1. **Auditoria de Padrões de Links**: Listar os links em markdown para revisão

   ```bash
   # Listar links Markdown (auditoria de padrão)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validação de Exemplos de Código**: Testar se os exemplos de código compilam/correm

   ```bash
   # Navegar para uma amostra específica e executar os seus testes
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting de Markdown**: Verificar consistência de formatação

   ```bash
   # Use markdownlint se necessário
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Teste de Projeto Exemplo

Cada exemplo específico de linguagem inclui a sua própria abordagem de teste:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Diretrizes de Estilo de Código

### Estilo de Documentação

- Usar linguagem clara e acessível para iniciantes
- Incluir exemplos de código em múltiplas linguagens quando aplicável
- Seguir as melhores práticas do markdown:
  - Usar cabeçalhos no estilo ATX (`#` sintaxe)
  - Usar blocos de código delimitados com identificadores de linguagem
  - Incluir texto alternativo descritivo para as imagens
  - Manter linhas com comprimentos razoáveis (sem limite rígido, mas ser sensato)

### Estilo dos Exemplos de Código

#### TypeScript/JavaScript
- Usar módulos ES (`import`/`export`)
- Seguir as convenções do modo estrito do TypeScript
- Incluir anotações de tipo
- Destinar-se a ES2022

#### Python
- Seguir as diretrizes de estilo PEP 8
- Usar "type hints" onde apropriado
- Incluir docstrings para funções e classes
- Usar funcionalidades modernas do Python (3.8+)

#### Java
- Seguir as convenções do Spring Boot
- Usar funcionalidades do Java 21
- Seguir a estrutura padrão de projetos Maven
- Incluir comentários Javadoc

### Organização de Ficheiros

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Construção e Implantação

### Implantação da Documentação

O repositório usa GitHub Pages ou similar para alojamento da documentação (se aplicável). Alterações na branch main desencadeiam:

1. Fluxo de trabalho de tradução (`.github/workflows/co-op-translator.yml`)
2. Tradução automatizada de todos os ficheiros markdown em inglês
3. Localização de imagens conforme necessário

### Nenhum Processo de Build Necessário

Este repositório contém principalmente documentação markdown. Não é necessário nenhum passo de compilação ou construção para o conteúdo curricular principal.

### Implantação dos Projetos de Exemplo

Projetos de exemplo individuais podem ter instruções de implantação:
- Ver `03-GettingStarted/09-deployment/` para orientação de implantação do servidor MCP
- Exemplos de implantação do Azure Container Apps em `11-MCPServerHandsOnLabs/`

## Diretrizes de Contribuição

### Processo de Pull Request

1. **Fork e Clone**: Fazer fork do repositório e clonar localmente
2. **Criar uma Branch**: Usar nomes descritivos para a branch (ex.: `fix/typo-module-3`, `add/python-example`)
3. **Fazer Alterações**: Editar apenas os ficheiros markdown em inglês (não traduções)
4. **Testar Localmente**: Verificar se o markdown é renderizado corretamente
5. **Submeter PR**: Usar títulos e descrições claras para o PR
6. **CLA**: Assinar o Acordo de Licença de Contribuidor Microsoft quando solicitado

### Formato do Título do PR

Usar títulos claros e descritivos:
- `[Module XX] Breve descrição` para alterações específicas de módulo
- `[Samples] Descrição` para alterações em código exemplo
- `[Docs] Descrição` para atualizações gerais na documentação

### O Que Contribuir

- Correções de bugs na documentação ou exemplos de código
- Novos exemplos de código em linguagens adicionais
- Esclarecimentos e melhorias no conteúdo existente
- Novos estudos de caso ou exemplos práticos
- Relatórios de problemas para conteúdos pouco claros ou incorretos

### O Que NÃO Fazer

- Não editar diretamente ficheiros na diretoria `translations/`
- Não editar a diretoria `translated_images/`
- Não adicionar ficheiros binários grandes sem discussão prévia
- Não alterar ficheiros do fluxo de trabalho de tradução sem coordenação

## Notas Adicionais

### Manutenção do Repositório

- **Changelog**: Todas as alterações significativas estão documentadas em `changelog.md`
- **Guia de Estudo**: Usar `study_guide.md` para visão geral da navegação curricular
- **Modelos de Issue**: Usar modelos de issues no GitHub para relatórios de bugs e pedidos de funcionalidades
- **Código de Conduta**: Todos os contribuintes devem seguir o Código de Conduta de Código Aberto da Microsoft

### Caminho de Aprendizagem

Seguir os módulos em ordem sequencial (00-11) para melhor aprendizagem:
1. **00-02**: Fundamentos (Introdução, Conceitos Básicos, Segurança)
2. **03**: Introdução com implementação prática
3. **04-05**: Implementação prática e tópicos avançados
4. **06-10**: Comunidade, melhores práticas e aplicações reais
5. **11**: Laboratórios completos de integração de bases de dados (13 laboratórios sequenciais)

### Recursos de Apoio

- **Documentação**: https://modelcontextprotocol.io/
- **Especificação**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Comunidade**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Servidor Discord Microsoft Foundry
- **Cursos Relacionados**: Ver README.md para outros caminhos de aprendizagem da Microsoft

### Problemas Comuns

**P: O meu PR está a falhar na verificação de tradução**
R: Assegure-se de que editou apenas ficheiros markdown em inglês nas diretórias principais dos módulos, não versões traduzidas.

**P: Como adiciono um novo idioma?**
R: O suporte a idiomas é gerido pelo fluxo de trabalho do co-op-translator. Abra uma issue para discutir a adição de novos idiomas.

**P: Os exemplos de código não estão a funcionar**
R: Assegure-se de que seguiu as instruções de configuração no README do exemplo específico. Verifique se têm as versões corretas das dependências instaladas.


**P: As imagens não estão a ser exibidas**

A: Verifique se os caminhos das imagens são relativos e utilizam barras normais. As imagens devem estar no diretório `images/` ou `translated_images/` para versões localizadas.

### Considerações de Desempenho

- O fluxo de trabalho da tradução pode demorar vários minutos a concluir
- Imagens grandes devem ser otimizadas antes de serem enviadas
- Mantenha os ficheiros markdown individuais focados e com tamanho razoável
- Use links relativos para melhor portabilidade

### Governança do Projeto

Este projeto segue as práticas de código aberto da Microsoft:
- Licença MIT para código e documentação
- Código de Conduta de Código Aberto da Microsoft
- CLA obrigatória para contribuições
- Questões de segurança: Siga as diretrizes do SECURITY.md
- Suporte: Veja o SUPPORT.md para recursos de ajuda

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->