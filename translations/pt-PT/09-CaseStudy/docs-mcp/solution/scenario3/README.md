# Cenário 3: Documentação no Editor com o Servidor MCP no VS Code

## Visão Geral

Neste cenário, vai aprender como trazer a documentação Microsoft Learn diretamente para o seu ambiente Visual Studio Code usando o servidor MCP. Em vez de estar sempre a alternar entre separadores do navegador para procurar documentação, pode aceder, pesquisar e consultar documentação oficial diretamente no seu editor. Esta abordagem simplifica o seu fluxo de trabalho, mantém-no focado e permite uma integração perfeita com ferramentas como o GitHub Copilot.

- Pesquise e leia documentação dentro do VS Code sem sair do seu ambiente de programação.
- Consulte documentação e insira links diretamente nos seus ficheiros README ou de curso.
- Use o GitHub Copilot e o MCP em conjunto para um fluxo de trabalho integrado e potenciado por IA.

## Objetivos de Aprendizagem

No final deste capítulo, vai saber como configurar e usar o servidor MCP dentro do VS Code para melhorar o seu fluxo de trabalho de documentação e desenvolvimento. Será capaz de:

- Configurar o seu ambiente de trabalho para usar o servidor MCP na pesquisa de documentação.
- Pesquisar e inserir documentação diretamente a partir do VS Code.
- Combinar o poder do GitHub Copilot e do MCP para um fluxo de trabalho mais produtivo e potenciado por IA.

Estas competências vão ajudá-lo a manter o foco, melhorar a qualidade da documentação e aumentar a sua produtividade como programador ou redator técnico.

## Solução

Para conseguir acesso à documentação dentro do editor, vai seguir uma série de passos que integram o servidor MCP com o VS Code e o GitHub Copilot. Esta solução é ideal para autores de cursos, redatores de documentação e programadores que querem manter o foco no editor enquanto trabalham com documentação e o Copilot.

- Adicione rapidamente links de referência a um README enquanto escreve documentação de um curso ou projeto.
- Use o Copilot para gerar código e o MCP para encontrar e citar instantaneamente documentação relevante.
- Mantenha o foco no seu editor e aumente a produtividade.

### Guia Passo a Passo

Para começar, siga estes passos. Para cada passo, pode adicionar uma captura de ecrã da pasta de assets para ilustrar visualmente o processo.

1. **Adicione a configuração MCP:**
   Na raiz do seu projeto, crie um ficheiro `.vscode/mcp.json` e adicione a seguinte configuração:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Esta configuração indica ao VS Code como ligar-se ao [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp).
   
   ![Passo 1: Adicionar mcp.json à pasta .vscode](../../../../../../translated_images/pt-PT/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.png)
    
2. **Abra o painel GitHub Copilot Chat:**
   Se ainda não tiver a extensão GitHub Copilot instalada, vá à vista de Extensões no VS Code e instale-a. Pode descarregá-la diretamente do [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Depois, abra o painel Copilot Chat na barra lateral.

   ![Passo 2: Abrir painel Copilot Chat](../../../../../../translated_images/pt-PT/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.png)

3. **Ative o modo agente e verifique as ferramentas:**
   No painel Copilot Chat, ative o modo agente.

   ![Passo 3: Ativar modo agente e verificar ferramentas](../../../../../../translated_images/pt-PT/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.png)

   Depois de ativar o modo agente, verifique se o servidor MCP está listado como uma das ferramentas disponíveis. Isto garante que o agente Copilot pode aceder ao servidor de documentação para obter informação relevante.
   
   ![Passo 3: Verificar ferramenta do servidor MCP](../../../../../../translated_images/pt-PT/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.png)
4. **Inicie uma nova conversa e faça perguntas ao agente:**
   Abra uma nova conversa no painel Copilot Chat. Agora pode fazer perguntas ao agente sobre documentação. O agente usará o servidor MCP para obter e mostrar documentação relevante do Microsoft Learn diretamente no seu editor.

   - *"Estou a tentar escrever um plano de estudo para o tópico X. Vou estudá-lo durante 8 semanas, para cada semana, sugira o conteúdo que devo abordar."*

   ![Passo 4: Fazer perguntas ao agente no chat](../../../../../../translated_images/pt-PT/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.png)

5. **Consulta em tempo real:**

   > Vamos ver uma consulta em tempo real da secção [#get-help](https://discord.gg/D6cRhjHWSC) no Discord Azure AI Foundry ([ver mensagem original](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *"Estou à procura de respostas sobre como implementar uma solução multi-agente com agentes de IA desenvolvidos no Azure AI Foundry. Vejo que não existe um método direto de implementação, como canais do Copilot Studio. Então, quais são as diferentes formas de fazer esta implementação para que utilizadores empresariais possam interagir e realizar o trabalho?
Existem vários artigos/blogs que dizem que podemos usar o serviço Azure Bot para fazer este trabalho, que pode atuar como uma ponte entre o MS Teams e os Agentes do Azure AI Foundry. Será que isto funciona se configurar um bot Azure que se ligue ao Orchestrator Agent no Azure AI Foundry via Azure Function para realizar a orquestração, ou preciso criar uma Azure Function para cada um dos agentes de IA que fazem parte da solução multi-agente para fazer a orquestração no Bot Framework? Qualquer outra sugestão é muito bem-vinda."*

   ![Passo 5: Consultas em tempo real](../../../../../../translated_images/pt-PT/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.png)

   O agente responderá com links e resumos de documentação relevantes, que pode inserir diretamente nos seus ficheiros markdown ou usar como referência no seu código.
   
### Consultas de Exemplo

Aqui estão algumas consultas de exemplo que pode experimentar. Estas consultas demonstram como o servidor MCP e o Copilot podem trabalhar juntos para fornecer documentação instantânea, contextualizada e referências sem sair do VS Code:

- "Mostra-me como usar triggers do Azure Functions."
- "Insere um link para a documentação oficial do Azure Key Vault."
- "Quais são as melhores práticas para proteger recursos Azure?"
- "Encontra um quickstart para serviços Azure AI."

Estas consultas demonstram como o servidor MCP e o Copilot podem trabalhar juntos para fornecer documentação instantânea, contextualizada e referências sem sair do VS Code.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.