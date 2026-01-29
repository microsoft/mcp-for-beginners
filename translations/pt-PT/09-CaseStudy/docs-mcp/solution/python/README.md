# Gerador de Plano de Estudos com Chainlit e Microsoft Learn Docs MCP

## Pré-requisitos

- Python 3.8 ou superior
- pip (gestor de pacotes Python)
- Acesso à internet para conectar ao servidor Microsoft Learn Docs MCP

## Instalação

1. Clone este repositório ou descarregue os ficheiros do projeto.
2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Utilização

### Cenário 1: Consulta Simples ao Docs MCP
Um cliente de linha de comandos que se conecta ao servidor Docs MCP, envia uma consulta e imprime o resultado.

1. Execute o script:
   ```bash
   python scenario1.py
   ```
2. Insira a sua pergunta sobre a documentação no prompt.

### Cenário 2: Gerador de Plano de Estudos (Aplicação Web Chainlit)
Uma interface web (usando Chainlit) que permite aos utilizadores gerar um plano de estudos personalizado, semana a semana, para qualquer tópico técnico.

1. Inicie a aplicação Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Abra o URL local fornecido no seu terminal (por exemplo, http://localhost:8000) no seu navegador.
3. Na janela de chat, insira o tópico de estudo e o número de semanas que pretende estudar (por exemplo, "Certificação AI-900, 8 semanas").
4. A aplicação responderá com um plano de estudos semana a semana, incluindo links para a documentação relevante do Microsoft Learn.

**Variáveis de Ambiente Necessárias:**

Para utilizar o Cenário 2 (a aplicação web Chainlit com Azure OpenAI), deve definir as seguintes variáveis de ambiente num ficheiro `.env` no diretório `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Preencha estes valores com os detalhes do seu recurso Azure OpenAI antes de executar a aplicação.

> [!TIP]
> Pode facilmente implementar os seus próprios modelos utilizando o [Azure AI Foundry](https://ai.azure.com/).

### Cenário 3: Documentação no Editor com o Servidor MCP no VS Code

Em vez de alternar entre abas do navegador para procurar documentação, pode trazer o Microsoft Learn Docs diretamente para o seu VS Code utilizando o servidor MCP. Isto permite-lhe:
- Pesquisar e ler documentação dentro do VS Code sem sair do ambiente de codificação.
- Referenciar documentação e inserir links diretamente no seu README ou ficheiros de curso.
- Usar o GitHub Copilot e o MCP em conjunto para um fluxo de trabalho de documentação com suporte de IA.

**Exemplos de Casos de Uso:**
- Adicionar rapidamente links de referência a um README enquanto escreve a documentação de um curso ou projeto.
- Usar o Copilot para gerar código e o MCP para encontrar e citar documentação relevante instantaneamente.
- Manter o foco no editor e aumentar a produtividade.

> [!IMPORTANT]
> Certifique-se de que tem uma configuração válida [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) no seu espaço de trabalho (localização: `.vscode/mcp.json`).

## Por Que Usar Chainlit no Cenário 2?

O Chainlit é uma estrutura moderna e open-source para criar aplicações web conversacionais. Facilita a criação de interfaces de utilizador baseadas em chat que se conectam a serviços de backend, como o servidor Microsoft Learn Docs MCP. Este projeto utiliza o Chainlit para fornecer uma forma simples e interativa de gerar planos de estudo personalizados em tempo real. Ao aproveitar o Chainlit, pode criar e implementar rapidamente ferramentas baseadas em chat que aumentam a produtividade e o aprendizado.

## O Que Esta Aplicação Faz

Esta aplicação permite aos utilizadores criar um plano de estudos personalizado, bastando inserir um tópico e uma duração. A aplicação analisa a sua entrada, consulta o servidor Microsoft Learn Docs MCP para obter conteúdo relevante e organiza os resultados num plano estruturado, semana a semana. As recomendações de cada semana são apresentadas no chat, tornando fácil seguir e acompanhar o progresso. A integração garante que terá sempre acesso aos recursos de aprendizagem mais recentes e relevantes.

## Exemplos de Consultas

Experimente estas consultas na janela de chat para ver como a aplicação responde:

- `Certificação AI-900, 8 semanas`
- `Aprender Azure Functions, 4 semanas`
- `Azure DevOps, 6 semanas`
- `Engenharia de dados no Azure, 10 semanas`
- `Fundamentos de segurança da Microsoft, 5 semanas`
- `Power Platform, 7 semanas`
- `Serviços de IA do Azure, 12 semanas`
- `Arquitetura de cloud, 9 semanas`

Estes exemplos demonstram a flexibilidade da aplicação para diferentes objetivos de aprendizagem e prazos.

## Referências

- [Documentação do Chainlit](https://docs.chainlit.io/)
- [Documentação do MCP](https://github.com/MicrosoftDocs/mcp)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.