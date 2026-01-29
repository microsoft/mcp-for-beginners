# Gerador de Plano de Estudos com Chainlit & Microsoft Learn Docs MCP

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Acesso à internet para conectar ao servidor Microsoft Learn Docs MCP

## Instalação

1. Clone este repositório ou baixe os arquivos do projeto.
2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Cenário 1: Consulta Simples ao Docs MCP
Um cliente de linha de comando que se conecta ao servidor Docs MCP, envia uma consulta e imprime o resultado.

1. Execute o script:
   ```bash
   python scenario1.py
   ```
2. Insira sua pergunta sobre a documentação no prompt.

### Cenário 2: Gerador de Plano de Estudos (Aplicativo Web Chainlit)
Uma interface baseada na web (usando Chainlit) que permite aos usuários gerar um plano de estudos personalizado, semana a semana, para qualquer tópico técnico.

1. Inicie o aplicativo Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Abra o URL local fornecido no terminal (por exemplo, http://localhost:8000) no seu navegador.
3. Na janela de chat, insira o tópico de estudo e o número de semanas que deseja estudar (por exemplo, "Certificação AI-900, 8 semanas").
4. O aplicativo responderá com um plano de estudos semana a semana, incluindo links para a documentação relevante do Microsoft Learn.

**Variáveis de Ambiente Necessárias:**

Para usar o Cenário 2 (o aplicativo web Chainlit com Azure OpenAI), você deve definir as seguintes variáveis de ambiente em um arquivo `.env` no diretório `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Preencha esses valores com os detalhes do seu recurso Azure OpenAI antes de executar o aplicativo.

> [!TIP]
> Você pode facilmente implantar seus próprios modelos usando [Azure AI Foundry](https://ai.azure.com/).

### Cenário 3: Documentação no Editor com o Servidor MCP no VS Code

Em vez de alternar entre abas do navegador para buscar documentação, você pode trazer o Microsoft Learn Docs diretamente para o seu VS Code usando o servidor MCP. Isso permite que você:
- Pesquise e leia a documentação dentro do VS Code sem sair do ambiente de codificação.
- Referencie a documentação e insira links diretamente no seu README ou arquivos de curso.
- Use o GitHub Copilot e o MCP juntos para um fluxo de trabalho integrado e impulsionado por IA.

**Exemplos de Casos de Uso:**
- Adicione rapidamente links de referência a um README enquanto escreve a documentação de um curso ou projeto.
- Use o Copilot para gerar código e o MCP para encontrar e citar instantaneamente a documentação relevante.
- Mantenha o foco no editor e aumente a produtividade.

> [!IMPORTANT]
> Certifique-se de ter uma configuração válida [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) no seu espaço de trabalho (localização: `.vscode/mcp.json`).

## Por que usar Chainlit no Cenário 2?

Chainlit é um framework moderno e de código aberto para construir aplicativos web conversacionais. Ele facilita a criação de interfaces de usuário baseadas em chat que se conectam a serviços de backend, como o servidor Microsoft Learn Docs MCP. Este projeto utiliza Chainlit para fornecer uma maneira simples e interativa de gerar planos de estudo personalizados em tempo real. Ao aproveitar o Chainlit, você pode criar e implantar rapidamente ferramentas baseadas em chat que aumentam a produtividade e o aprendizado.

## O que Este Aplicativo Faz

Este aplicativo permite que os usuários criem um plano de estudos personalizado simplesmente inserindo um tópico e uma duração. O aplicativo interpreta sua entrada, consulta o servidor Microsoft Learn Docs MCP para obter conteúdo relevante e organiza os resultados em um plano estruturado semana a semana. As recomendações de cada semana são exibidas no chat, tornando fácil seguir e acompanhar seu progresso. A integração garante que você sempre receba os recursos de aprendizado mais recentes e relevantes.

## Consultas de Exemplo

Experimente estas consultas na janela de chat para ver como o aplicativo responde:

- `Certificação AI-900, 8 semanas`
- `Aprender Azure Functions, 4 semanas`
- `Azure DevOps, 6 semanas`
- `Engenharia de dados no Azure, 10 semanas`
- `Fundamentos de segurança da Microsoft, 5 semanas`
- `Power Platform, 7 semanas`
- `Serviços de IA do Azure, 12 semanas`
- `Arquitetura de nuvem, 9 semanas`

Esses exemplos demonstram a flexibilidade do aplicativo para diferentes objetivos de aprendizado e prazos.

## Referências

- [Documentação do Chainlit](https://docs.chainlit.io/)
- [Documentação do MCP](https://github.com/MicrosoftDocs/mcp)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.