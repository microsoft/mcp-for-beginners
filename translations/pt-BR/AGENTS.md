# AGENTS.md

## Visão Geral do Projeto

**MCP para Iniciantes** é um currículo educacional open-source para aprender o Model Context Protocol (MCP) - uma estrutura padronizada para interações entre modelos de IA e aplicações clientes. Este repositório oferece materiais de aprendizado abrangentes com exemplos práticos de código em várias linguagens de programação.

### Tecnologias Principais

- **Linguagens de Programação**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bancos de Dados**: PostgreSQL com extensão pgvector
- **Plataformas em Nuvem**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Ferramentas de Build**: npm, Maven, pip, Cargo
- **Documentação**: Markdown com tradução automática para múltiplos idiomas (mais de 48 línguas)

### Arquitetura

- **11 Módulos Centrais (00-11)**: Caminho sequencial de aprendizado desde fundamentos até tópicos avançados
- **Laboratórios Práticos**: Exercícios práticos com código solução completo em várias linguagens
- **Projetos de Exemplo**: Implementações funcionais de servidor e cliente MCP
- **Sistema de Tradução**: Workflow automatizado no GitHub Actions para suporte multilíngue
- **Ativos de Imagem**: Diretório centralizado de imagens com versões traduzidas

## Comandos de Configuração

Este é um repositório focado em documentação. A maior parte da configuração ocorre dentro dos projetos e laboratórios de exemplo individuais.

### Configuração do Repositório

```bash
# Clone o repositório
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Trabalhando com Projetos de Exemplo

Projetos de exemplo estão localizados em:
- `03-GettingStarted/samples/` - Exemplos específicos por linguagem
- `03-GettingStarted/01-first-server/solution/` - Primeiras implementações de servidor
- `03-GettingStarted/02-client/solution/` - Implementações de cliente
- `11-MCPServerHandsOnLabs/` - Laboratórios completos de integração com banco de dados

Cada projeto de exemplo contém suas próprias instruções de configuração:

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

#### Checklist de prontidão do repositório

- [x] **Clareza para novos colaboradores**: Este arquivo define o propósito do repositório,
  estrutura, regras de contribuição e caminhos de configuração para exemplos.
- [x] **Comandos de build/teste/lint com flags exatas**:
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
- [x] **Um fluxo de trabalho realista que pode se tornar uma ferramenta MCP**:
  `validate_curriculum_change`
- [x] **Entradas/saídas são explícitas** (ver especificação abaixo).
- [x] **Permissões e modos de falha são documentados** (ver especificação abaixo).
- [x] **Testabilidade CI é explícita** (comandos determinísticos, códigos de saída explícitos,
  e saídas legíveis por máquina).

#### Fluxo de trabalho candidato para ferramenta MCP: `validate_curriculum_change`

##### Objetivo

Validar mudanças na documentação do currículo e saúde do código de exemplo representativo
antes da mesclagem.

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

- Ler arquivos do workspace e escrever artefatos gerados pela ferramenta (ex.: relatórios de lint,
  logs de teste) somente; não escrever em `translations/` ou
  `translated_images/`.
- Executar comandos shell locais.
- Acesso opcional à rede apenas para restauração de pacotes (`npm ci`,
  `python -m pip install`, resolução de dependências `mvn`).
- Sem permissão para push, merge ou modificação em `translations/` ou
  `translated_images/`.

##### Modos de falha

- `E_NO_INPUT_PATHS`: `changed_paths` vazio.
- `E_INVALID_PATH`: caminho de entrada escapa a raiz do repositório.
- `E_LINT_FAILED`: lint markdown saiu com código diferente de zero.
- `E_LINK_AUDIT_FAILED`: comando de auditoria de links saiu com código diferente de zero.
- `E_SAMPLE_TEST_FAILED`: teste/build do exemplo saiu com código diferente de zero.
- `E_TIMEOUT`: comando excedeu tempo limite configurado.

##### Contrato CI recomendado

Para automatizar a validação, configure um job CI que:

- Execute em pull requests que alterem arquivos `*.md`, código de exemplo ou este arquivo.
- Execute os comandos exatos listados acima.
- Persista logs como artefatos.
- Falhe o job ao ocorrer qualquer código de saída diferente de zero.

#### Se você lançar um servidor MCP a partir deste repositório

- [ ] Leia o changelog rascunho para MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Teste seu servidor com SDKs beta:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Remova suposições de sessão e handshake; trate cada requisição como
  independente:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Envie cabeçalhos `Mcp-Method` e `Mcp-Name` para requisições HTTP brutas:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Audite códigos de erro codificados (ex.: `missing resource` mudou de `-32002` para `-32602`).
- [ ] Marque e planeje a migração para raízes, amostragem e
  logging depreciados:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migre da API experimental `2025-11-25` de Tasks:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Revise autenticação para endurecimento OAuth e OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Estrutura da Documentação

- **Módulos 00-11**: Conteúdo principal do currículo em ordem sequencial
- **translations/**: Versões específicas por língua (auto-geradas, não editar diretamente)
- **translated_images/**: Versões localizadas de imagens (auto-geradas)
- **images/**: Imagens e diagramas fonte

### Fazendo Mudanças na Documentação

1. Edite apenas os arquivos markdown em inglês nos diretórios raiz dos módulos (00-11)
2. Atualize imagens na pasta `images/` se necessário
3. A GitHub Action co-op-translator irá gerar as traduções automaticamente
4. Traduções são regeneradas ao fazer push para o branch principal

### Trabalhando com Traduções

- **Tradução Automatizada**: Workflow GitHub Actions cuida de todas as traduções
- **NÃO edite manualmente** arquivos na pasta `translations/`
- Metadados de tradução estão embutidos em cada arquivo traduzido
- Línguas suportadas: mais de 48, incluindo Árabe, Chinês, Francês, Alemão, Hindi, Japonês, Coreano, Português, Russo, Espanhol e muitas outras

## Instruções de Teste

### Validação da Documentação

Como este é principalmente um repositório de documentação, o foco dos testes é:

1. **Auditoria de Padrão de Links**: Listar links Markdown para revisão

   ```bash
   # Listar links Markdown (auditoria de padrão)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validação dos Exemplos de Código**: Testar se os exemplos compilam/executam

   ```bash
   # Navegue para a amostra específica e execute seus testes
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting do Markdown**: Verificar consistência na formatação

   ```bash
   # Use markdownlint se necessário
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Teste dos Projetos de Exemplo

Cada exemplo por linguagem inclui sua própria abordagem de teste:

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
- Inclua exemplos de código em múltiplas linguagens quando aplicável
- Siga boas práticas de markdown:
  - Use cabeçalhos no estilo ATX (sintaxe `#`)
  - Use blocos de código delimitados com identificadores de linguagem
  - Inclua texto alternativo descritivo para imagens
  - Mantenha comprimentos de linha razoáveis (sem limite rígido, mas sensato)

### Estilo dos Exemplos de Código

#### TypeScript/JavaScript
- Use módulos ES (`import`/`export`)
- Siga as convenções do modo estrito do TypeScript
- Inclua anotações de tipo
- Alvo ES2022

#### Python
- Siga as diretrizes de estilo PEP 8
- Use anotações de tipo onde apropriado
- Inclua docstrings para funções e classes
- Use recursos modernos do Python (3.8+)

#### Java
- Siga as convenções do Spring Boot
- Use recursos do Java 21
- Siga a estrutura padrão de projeto Maven
- Inclua comentários Javadoc

### Organização de Arquivos

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

## Build e Implantação

### Implantação da Documentação

O repositório usa GitHub Pages ou similar para hospedagem da documentação (se aplicável). Mudanças no branch principal acionam:

1. Workflow de tradução (`.github/workflows/co-op-translator.yml`)
2. Tradução automática de todos os arquivos markdown em inglês
3. Localização de imagens conforme necessário

### Nenhum Processo de Build Necessário

Este repositório contém principalmente documentação em markdown. Nenhuma etapa de compilação ou build é necessária para o conteúdo principal do currículo.

### Implantação dos Projetos de Exemplo

Projetos de exemplo individuais podem ter instruções de implantação:
- Veja `03-GettingStarted/09-deployment/` para orientações de implantação do servidor MCP
- Exemplos de implantação no Azure Container Apps em `11-MCPServerHandsOnLabs/`

## Diretrizes para Contribuição

### Processo de Pull Request

1. **Fork e Clone**: Faça fork do repositório e clone seu fork localmente
2. **Crie um Branch**: Use nomes descritivos para branches (ex.: `fix/typo-module-3`, `add/python-example`)
3. **Faça as Mudanças**: Edite apenas arquivos markdown em inglês (não traduções)
4. **Teste Localmente**: Verifique se o markdown renderiza corretamente
5. **Submeta PR**: Use títulos e descrições claras para o PR
6. **CLA**: Assine o Contrato de Licença de Contribuidor Microsoft quando solicitado

### Formato do Título do PR

Use títulos claros e descritivos:
- `[Módulo XX] Breve descrição` para mudanças específicas do módulo
- `[Exemplos] Descrição` para mudanças em código de exemplo
- `[Docs] Descrição` para atualizações gerais da documentação

### O que Contribuir

- Correções de bugs na documentação ou exemplos de código
- Novos exemplos de código em outras linguagens
- Esclarecimentos e melhorias no conteúdo existente
- Novos estudos de caso ou exemplos práticos
- Relatórios de problemas para conteúdos confusos ou incorretos

### O que NÃO fazer

- Não edite diretamente arquivos na pasta `translations/`
- Não edite a pasta `translated_images/`
- Não adicione arquivos binários grandes sem discussão prévia
- Não altere arquivos do workflow de tradução sem coordenação

## Notas Adicionais

### Manutenção do Repositório

- **Changelog**: Todas as alterações significativas estão documentadas em `changelog.md`
- **Guia de Estudo**: Use `study_guide.md` para visão geral da navegação do currículo
- **Templates de Issues**: Use templates do GitHub para relatórios de bugs e solicitações de recursos
- **Código de Conduta**: Todos os colaboradores devem seguir o Código de Conduta Open Source da Microsoft

### Caminho de Aprendizado

Siga os módulos em ordem sequencial (00-11) para aprendizado otimizado:
1. **00-02**: Fundamentos (Introdução, Conceitos Centrais, Segurança)
2. **03**: Primeiros passos com implementação prática
3. **04-05**: Implementação prática e tópicos avançados
4. **06-10**: Comunidade, boas práticas e aplicações no mundo real
5. **11**: Laboratórios completos de integração com banco de dados (13 laboratórios sequenciais)

### Recursos de Suporte

- **Documentação**: https://modelcontextprotocol.io/
- **Especificação**: https://spec.modelcontextprotocol.io/
- **Comunidade**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Servidor Discord Microsoft Foundry
- **Cursos Relacionados**: Veja README.md para outros caminhos de aprendizado Microsoft

### Resolução de Problemas Comuns

**P: Meu PR está falhando na checagem de tradução**
R: Certifique-se de que editou apenas arquivos markdown em inglês nos diretórios raiz dos módulos, não versões traduzidas.

**P: Como adiciono uma nova língua?**
R: O suporte a idiomas é gerenciado pelo workflow co-op-translator. Abra uma issue para discutir a adição de novas línguas.

**P: Exemplos de código não estão funcionando**

R: Certifique-se de que você seguiu as instruções de configuração no README da amostra específica. Verifique se você tem as versões corretas das dependências instaladas.

**P: As imagens não estão sendo exibidas**
R: Verifique se os caminhos das imagens são relativos e usam barras normais. As imagens devem estar no diretório `images/` ou em `translated_images/` para versões localizadas.

### Considerações sobre desempenho

- O fluxo de trabalho de tradução pode levar vários minutos para ser concluído
- Imagens grandes devem ser otimizadas antes do commit
- Mantenha arquivos markdown individuais focados e de tamanho razoável
- Use links relativos para melhor portabilidade

### Governança do projeto

Este projeto segue as práticas de código aberto da Microsoft:
- Licença MIT para código e documentação
- Código de Conduta de Código Aberto da Microsoft
- CLA necessária para contribuições
- Problemas de segurança: Siga as diretrizes do SECURITY.md
- Suporte: Veja SUPPORT.md para recursos de ajuda

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->