# AGENTS.md

## Visão Geral do Projeto

**MCP para Iniciantes** é um currículo educativo open-source para aprender o Model Context Protocol (MCP) - um framework padronizado para interações entre modelos de IA e aplicações clientes. Este repositório disponibiliza materiais de aprendizagem completos com exemplos de código práticos em várias linguagens de programação.

### Tecnologias-Chave

- **Linguagens de Programação**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks e SDKs**:
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bases de Dados**: PostgreSQL com extensão pgvector
- **Plataformas Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Ferramentas de Build**: npm, Maven, pip, Cargo
- **Documentação**: Markdown com tradução automática em múltiplas línguas (48+ línguas)

### Arquitetura

- **11 Módulos Principais (00-11)**: Caminho de aprendizagem sequencial desde os fundamentos até tópicos avançados
- **Labs Práticos**: Exercícios práticos com código completo de solução em várias linguagens
- **Projetos de Exemplo**: Implementações funcionais de servidor e cliente MCP
- **Sistema de Tradução**: Workflow automatizado GitHub Actions para suporte multilíngue
- **Recursos de Imagem**: Diretório centralizado de imagens com versões traduzidas

## Comandos de Configuração

Este é um repositório focado em documentação. A maior parte da configuração ocorre dentro de projetos de exemplo e labs individuais.

### Configuração do Repositório

```bash
# Clonar o repositório
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Trabalhar com Projetos de Exemplo

Os projetos de exemplo encontram-se em:
- `03-GettingStarted/samples/` - Exemplos por linguagem
- `03-GettingStarted/01-first-server/solution/` - Primeiras implementações de servidores
- `03-GettingStarted/02-client/solution/` - Implementações de clientes
- `11-MCPServerHandsOnLabs/` - Labs abrangentes de integração com base de dados

Cada projeto de exemplo contém as suas próprias instruções de configuração:

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

## Workflow de Desenvolvimento

### Preparação para MCP 7-28

#### Lista de verificação de prontidão do repositório

- [x] **Clareza para novos contribuidores**: Este ficheiro define propósito,
  estrutura, regras de contribuição e caminhos de configuração de exemplo.
- [x] **Comandos de build/test/lint com flags exatas**:
  - Lint da documentação do repositório:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Auditoria de padrão de links da documentação:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validação do exemplo TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validação do exemplo Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validação do exemplo Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Um workflow realista que pode tornar-se numa ferramenta MCP**:
  `validate_curriculum_change`
- [x] **Entradas/saídas são explícitas** (ver especificação abaixo).
- [x] **Permissões e modos de falha estão documentados** (ver especificação abaixo).
- [x] **Testabilidade em CI é explícita** (comandos determinísticos, códigos de saída explícitos e
  outputs legíveis por máquina).

#### Workflow candidato para ferramenta MCP: `validate_curriculum_change`

##### Objetivo

Validar alterações da documentação do currículo e integridade do código de exemplo representativo
antes da fusão.

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

- Apenas ler ficheiros da workspace e escrever artefactos gerados pela ferramenta (ex.: relatórios de lint,
  logs de teste); sem escrever em `translations/` ou
  `translated_images/`.
- Executar comandos shell locais.
- Acesso de rede opcional somente para restauração de pacotes (`npm ci`,
  `python -m pip install`, resolução de dependências `mvn`).
- Sem permissão para fazer push, merge, ou modificar `translations/` ou
  `translated_images/`.

##### Modos de falha

- `E_NO_INPUT_PATHS`: `changed_paths` vazio.
- `E_INVALID_PATH`: caminho de entrada fora do root do repositório.
- `E_LINT_FAILED`: lint markdown terminou com código diferente de zero.
- `E_LINK_AUDIT_FAILED`: comando de auditoria de links terminou com erro.
- `E_SAMPLE_TEST_FAILED`: teste/build do exemplo terminou com erro.
- `E_TIMEOUT`: comando ultrapassou tempo limite configurado.

##### Contrato recomendado para CI

Para automatizar a validação, configurar um job CI que:

- Seja acionado por pull requests que afetem `*.md`, código de exemplo ou este ficheiro.
- Execute os comandos exatos listados acima.
- Persista logs como artefactos.
- Falhe o job se houver qualquer código de saída não-zero.

#### Se publicar um servidor MCP deste repositório

- [ ] Leia o changelog preliminar para MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Teste o seu servidor contra SDK betas:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Remova pressupostos de sessão e handshake; trate cada pedido como
  autónomo:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Envie cabeçalhos `Mcp-Method` e `Mcp-Name` para pedidos HTTP brutos:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Audite códigos de erro hard-coded (`missing resource` mudou de `-32002` para `-32602`).
- [ ] Identifique e planeie migração para as raízes, amostragem e
  logging obsoletos:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migre da API experimental de Tasks `2025-11-25`:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Reveja autorização para fortificação OAuth e OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Estrutura da Documentação

- **Módulos 00-11**: Conteúdo principal do currículo em ordem sequencial
- **translations/**: Versões específicas de idioma (geradas automaticamente, não editar diretamente)
- **translated_images/**: Versões localizadas de imagens (geradas automaticamente)
- **images/**: Imagens-fonte e diagramas

### Efetuando Alterações na Documentação

1. Edite apenas os ficheiros markdown em inglês nos diretórios principais dos módulos (00-11)
2. Atualize as imagens na diretoria `images/` se necessário
3. A ação GitHub co-op-translator gerará as traduções automaticamente
4. As traduções são regeneradas ao fazer push na branch main

### Trabalhar com Traduções

- **Tradução Automática**: workflow GitHub Actions trata todas as traduções
- **Não edite manualmente** ficheiros na diretoria `translations/`
- A metainformação da tradução está embutida em cada ficheiro traduzido
- Línguas suportadas: mais de 48, incluindo Árabe, Chinês, Francês, Alemão, Hindi, Japonês, Coreano, Português, Russo, Espanhol e muitas outras

## Instruções de Testes

### Validação da Documentação

Uma vez que este é principalmente um repositório de documentação, os testes focam-se em:

1. **Auditoria de Padrão de Links**: Listar links Markdown para revisão

   ```bash
   # Listar ligações Markdown (auditoria de padrão)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validação de Exemplos de Código**: Testar que exemplos de código compilam/executam

   ```bash
   # Navegar para uma amostra específica e executar os seus testes
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown**: Verificar consistência de formatação

   ```bash
   # Utilize markdownlint se necessário
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testes de Projetos de Exemplo

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

### Estilo da Documentação

- Use linguagem clara e amigável para iniciantes
- Inclua exemplos de código em várias linguagens, sempre que aplicável
- Siga as melhores práticas de markdown:
  - Use cabeçalhos estilo ATX (sintaxe `#`)
  - Use blocos de código cercados com identificadores de linguagem
  - Inclua texto alt descritivo para imagens
  - Mantenha comprimentos de linha razoáveis (sem limite rígido, mas seja sensato)

### Estilo dos Exemplos de Código

#### TypeScript/JavaScript
- Use módulos ES (`import`/`export`)
- Siga as convenções do modo estrito TypeScript
- Inclua anotações de tipo
- Alvo ES2022

#### Python
- Siga as diretrizes do estilo PEP 8
- Use type hints onde apropriado
- Inclua docstrings para funções e classes
- Use funcionalidades modernas do Python (3.8+)

#### Java
- Siga convenções do Spring Boot
- Use funcionalidades do Java 21
- Siga estrutura padrão de projetos Maven
- Inclua comentários Javadoc

### Organização dos Ficheiros

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

## Compilação e Deploy

### Deploy da Documentação

O repositório usa GitHub Pages ou similar para alojamento da documentação (se aplicável). Alterações na branch main desencadeiam:

1. Workflow de tradução (`.github/workflows/co-op-translator.yml`)
2. Tradução automatizada de todos os ficheiros markdown em inglês
3. Localização de imagens conforme necessário

### Sem Processo de Build Necessário

Este repositório contém principalmente documentação em markdown. Não é necessário passo de compilação para o conteúdo principal do currículo.

### Deploy de Projetos de Exemplo

Projetos de exemplo individuais podem conter instruções de deploy:
- Veja `03-GettingStarted/09-deployment/` para orientação de deploy do servidor MCP
- Exemplos de deploy para Azure Container Apps em `11-MCPServerHandsOnLabs/`

## Diretrizes para Contribuição

### Processo de Pull Request

1. **Fork e Clone**: Faça fork do repositório e clone o seu fork localmente
2. **Crie uma Branch**: Use nomes descritivos para branches (ex.: `fix/typo-module-3`, `add/python-example`)
3. **Faça Alterações**: Edite apenas ficheiros markdown em inglês (não traduções)
4. **Teste Localmente**: Verifique se o markdown é renderizado corretamente
5. **Submeta o PR**: Use títulos e descrições claras para o PR
6. **CLA**: Assine o Contrato de Licença para Contribuidores Microsoft quando solicitado

### Formato do Título do PR

Use títulos claros e descritivos:
- `[Módulo XX] Descrição breve` para alterações específicas de módulo
- `[Samples] Descrição` para alterações em código de exemplo
- `[Docs] Descrição` para atualizações gerais de documentação

### O que Contribuir

- Correções de bugs na documentação ou exemplos de código
- Novos exemplos de código em linguagens adicionais
- Esclarecimentos e melhorias em conteúdo existente
- Novos estudos de caso ou exemplos práticos
- Relatórios de problemas sobre conteúdo incorreto ou pouco claro

### O que NÃO fazer

- Não edite diretamente ficheiros na diretoria `translations/`
- Não edite a diretoria `translated_images/`
- Não adicione ficheiros binários grandes sem discussão prévia
- Não modifique ficheiros do workflow de tradução sem coordenação

## Notas Adicionais

### Manutenção do Repositório

- **Changelog**: Todas as alterações significativas estão documentadas em `changelog.md`
- **Guia de Estudo**: Use `study_guide.md` para visão geral da navegação do currículo
- **Templates de Issue**: Use modelos de issues do GitHub para reportar bugs e pedir funcionalidades
- **Código de Conduta**: Todos os contribuidores devem seguir o Código de Conduta Open Source da Microsoft

### Trajeto de Aprendizagem

Siga os módulos em ordem sequencial (00-11) para aprendizagem ideal:
1. **00-02**: Fundamentos (Introdução, Conceitos Principais, Segurança)
2. **03**: Começando com implementação prática
3. **04-05**: Implementação prática e tópicos avançados
4. **06-10**: Comunidade, melhores práticas e aplicações reais
5. **11**: Labs abrangentes de integração com base de dados (13 labs sequenciais)

### Recursos de Suporte

- **Documentação**: https://modelcontextprotocol.io/
- **Especificação**: https://spec.modelcontextprotocol.io/
- **Comunidade**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: servidor Discord Microsoft Foundry
- **Cursos Relacionados**: Veja README.md para outros percursos de aprendizagem Microsoft

### Problemas Comuns e Soluções

**P: O meu PR está a falhar na verificação de tradução**
R: Assegure-se de que editou apenas os ficheiros markdown em inglês nas diretorias principais dos módulos, não as versões traduzidas.

**P: Como acrescentar um novo idioma?**
R: O suporte a idiomas é gerido pelo workflow co-op-translator. Abra um issue para discutir a adição de novos idiomas.

**P: Os exemplos de código não estão a funcionar**

R: Certifique-se de que seguiu as instruções de configuração no README do exemplo específico. Verifique se tem as versões corretas das dependências instaladas.

**P: As imagens não estão a ser exibidas**
R: Verifique se os caminhos das imagens são relativos e usam barras normais. As imagens devem estar na diretoria `images/` ou `translated_images/` para versões localizadas.

### Considerações de Performance

- O fluxo de trabalho de tradução pode levar vários minutos a completar
- As imagens grandes devem ser otimizadas antes de serem submetidas
- Mantenha os ficheiros markdown individuais focados e de tamanho razoável
- Utilize links relativos para melhor portabilidade

### Governação do Projeto

Este projeto segue as práticas open source da Microsoft:
- Licença MIT para código e documentação
- Código de Conduta Open Source da Microsoft
- CLA obrigatória para contribuições
- Questões de segurança: Siga as diretrizes do SECURITY.md
- Suporte: Veja o SUPPORT.md para recursos de ajuda

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->