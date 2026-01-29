# AGENTS.md

## Visão Geral do Projeto

**MCP para Iniciantes** é um currículo educacional de código aberto para aprender o Model Context Protocol (MCP) - uma estrutura padronizada para interações entre modelos de IA e aplicações cliente. Este repositório fornece materiais de aprendizagem abrangentes com exemplos de código práticos em várias linguagens de programação.

### Tecnologias Principais

- **Linguagens de Programação**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bases de Dados**: PostgreSQL com extensão pgvector
- **Plataformas na Nuvem**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Ferramentas de Build**: npm, Maven, pip, Cargo
- **Documentação**: Markdown com tradução automática para múltiplos idiomas (48+ idiomas)

### Arquitetura

- **11 Módulos Centrais (00-11)**: Caminho de aprendizagem sequencial desde os fundamentos até tópicos avançados
- **Laboratórios Práticos**: Exercícios práticos com código de solução completo em várias linguagens
- **Projetos de Exemplo**: Implementações funcionais de servidor e cliente MCP
- **Sistema de Tradução**: Workflow automatizado do GitHub Actions para suporte multilíngue
- **Recursos de Imagem**: Diretório centralizado de imagens com versões traduzidas

## Comandos de Configuração

Este é um repositório focado em documentação. A maior parte da configuração ocorre dentro dos projetos de exemplo e laboratórios individuais.

### Configuração do Repositório

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Trabalhar com Projetos de Exemplo

Os projetos de exemplo estão localizados em:
- `03-GettingStarted/samples/` - Exemplos específicos de linguagem
- `03-GettingStarted/01-first-server/solution/` - Implementações do primeiro servidor
- `03-GettingStarted/02-client/solution/` - Implementações de cliente
- `11-MCPServerHandsOnLabs/` - Laboratórios abrangentes de integração de bases de dados

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
# or
pip install -e .
python main.py
```

#### Projetos Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Fluxo de Trabalho de Desenvolvimento

### Estrutura da Documentação

- **Módulos 00-11**: Conteúdo curricular principal em ordem sequencial
- **translations/**: Versões específicas de idioma (geradas automaticamente, não editar diretamente)
- **translated_images/**: Versões localizadas de imagens (geradas automaticamente)
- **images/**: Imagens e diagramas de origem

### Fazer Alterações na Documentação

1. Edite apenas os ficheiros markdown em inglês nos diretórios principais dos módulos (00-11)
2. Atualize imagens no diretório `images/` se necessário
3. O GitHub Action co-op-translator gerará automaticamente as traduções
4. As traduções são regeneradas ao fazer push para a branch principal

### Trabalhar com Traduções

- **Tradução Automática**: O workflow do GitHub Actions lida com todas as traduções
- **NÃO edite manualmente** os ficheiros no diretório `translations/`
- Metadados de tradução estão incorporados em cada ficheiro traduzido
- Idiomas suportados: 48+ idiomas, incluindo Árabe, Chinês, Francês, Alemão, Hindi, Japonês, Coreano, Português, Russo, Espanhol e muitos mais

## Instruções de Teste

### Validação da Documentação

Como este é principalmente um repositório de documentação, os testes concentram-se em:

1. **Validação de Links**: Certifique-se de que todos os links internos funcionam
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validação de Exemplos de Código**: Teste se os exemplos de código compilam/executam
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting de Markdown**: Verifique a consistência da formatação
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Teste de Projetos de Exemplo

Cada exemplo específico de linguagem inclui sua própria abordagem de teste:

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

- Use linguagem clara e acessível para iniciantes
- Inclua exemplos de código em várias linguagens, quando aplicável
- Siga as melhores práticas de markdown:
  - Use cabeçalhos no estilo ATX (`#` sintaxe)
  - Use blocos de código delimitados com identificadores de linguagem
  - Inclua texto alternativo descritivo para imagens
  - Mantenha comprimentos de linha razoáveis (sem limite rígido, mas seja sensato)

### Estilo de Exemplos de Código

#### TypeScript/JavaScript
- Use módulos ES (`import`/`export`)
- Siga as convenções de modo estrito do TypeScript
- Inclua anotações de tipo
- Alvo ES2022

#### Python
- Siga as diretrizes de estilo PEP 8
- Use dicas de tipo quando apropriado
- Inclua docstrings para funções e classes
- Use recursos modernos do Python (3.8+)

#### Java
- Siga as convenções do Spring Boot
- Use recursos do Java 21
- Siga a estrutura padrão de projetos Maven
- Inclua comentários Javadoc

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

## Build e Implementação

### Implementação da Documentação

O repositório utiliza GitHub Pages ou similar para hospedagem de documentação (se aplicável). Alterações na branch principal acionam:

1. Workflow de tradução (`.github/workflows/co-op-translator.yml`)
2. Tradução automática de todos os ficheiros markdown em inglês
3. Localização de imagens conforme necessário

### Nenhum Processo de Build Necessário

Este repositório contém principalmente documentação em markdown. Não é necessário compilação ou etapa de build para o conteúdo curricular principal.

### Implementação de Projetos de Exemplo

Projetos de exemplo individuais podem ter instruções de implementação:
- Veja `03-GettingStarted/09-deployment/` para orientações de implementação de servidor MCP
- Exemplos de implementação no Azure Container Apps em `11-MCPServerHandsOnLabs/`

## Diretrizes de Contribuição

### Processo de Pull Request

1. **Fork e Clone**: Faça fork do repositório e clone o seu fork localmente
2. **Crie uma Branch**: Use nomes de branch descritivos (ex.: `fix/typo-module-3`, `add/python-example`)
3. **Faça Alterações**: Edite apenas os ficheiros markdown em inglês (não traduções)
4. **Teste Localmente**: Verifique se o markdown é renderizado corretamente
5. **Submeta o PR**: Use títulos e descrições claros para o PR
6. **CLA**: Assine o Microsoft Contributor License Agreement quando solicitado

### Formato de Título de PR

Use títulos claros e descritivos:
- `[Module XX] Breve descrição` para alterações específicas de módulo
- `[Samples] Descrição` para alterações em exemplos de código
- `[Docs] Descrição` para atualizações gerais de documentação

### O Que Contribuir

- Correções de bugs na documentação ou exemplos de código
- Novos exemplos de código em idiomas adicionais
- Esclarecimentos e melhorias no conteúdo existente
- Novos estudos de caso ou exemplos práticos
- Relatórios de problemas para conteúdo pouco claro ou incorreto

### O Que NÃO Fazer

- Não edite diretamente ficheiros no diretório `translations/`
- Não edite o diretório `translated_images/`
- Não adicione ficheiros binários grandes sem discussão
- Não altere ficheiros de workflow de tradução sem coordenação

## Notas Adicionais

### Manutenção do Repositório

- **Changelog**: Todas as alterações significativas são documentadas em `changelog.md`
- **Guia de Estudo**: Use `study_guide.md` para visão geral de navegação no currículo
- **Templates de Issues**: Use templates de issues do GitHub para relatórios de bugs e pedidos de funcionalidades
- **Código de Conduta**: Todos os contribuidores devem seguir o Código de Conduta de Código Aberto da Microsoft

### Caminho de Aprendizagem

Siga os módulos em ordem sequencial (00-11) para uma aprendizagem otimizada:
1. **00-02**: Fundamentos (Introdução, Conceitos Centrais, Segurança)
2. **03**: Introdução com implementação prática
3. **04-05**: Implementação prática e tópicos avançados
4. **06-10**: Comunidade, melhores práticas e aplicações no mundo real
5. **11**: Laboratórios abrangentes de integração de bases de dados (13 laboratórios sequenciais)

### Recursos de Suporte

- **Documentação**: https://modelcontextprotocol.io/
- **Especificação**: https://spec.modelcontextprotocol.io/
- **Comunidade**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Servidor Discord Microsoft Azure AI Foundry
- **Cursos Relacionados**: Veja README.md para outros caminhos de aprendizagem da Microsoft

### Resolução Comum de Problemas

**P: Meu PR está falhando na verificação de tradução**
R: Certifique-se de que editou apenas ficheiros markdown em inglês nos diretórios principais dos módulos, não versões traduzidas.

**P: Como adiciono um novo idioma?**
R: O suporte a idiomas é gerido através do workflow co-op-translator. Abra uma issue para discutir a adição de novos idiomas.

**P: Os exemplos de código não estão funcionando**
R: Certifique-se de que seguiu as instruções de configuração no README específico do exemplo. Verifique se tem as versões corretas das dependências instaladas.

**P: As imagens não estão a ser exibidas**
R: Verifique se os caminhos das imagens são relativos e utilizam barras para frente. As imagens devem estar no diretório `images/` ou `translated_images/` para versões localizadas.

### Considerações de Desempenho

- O workflow de tradução pode levar vários minutos para ser concluído
- Imagens grandes devem ser otimizadas antes de serem commitadas
- Mantenha os ficheiros markdown individuais focados e de tamanho razoável
- Use links relativos para melhor portabilidade

### Governança do Projeto

Este projeto segue as práticas de código aberto da Microsoft:
- Licença MIT para código e documentação
- Código de Conduta de Código Aberto da Microsoft
- CLA necessário para contribuições
- Questões de segurança: Siga as diretrizes do SECURITY.md
- Suporte: Veja SUPPORT.md para recursos de ajuda

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.