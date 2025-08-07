<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-08-07T08:28:47+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "pt"
}
-->
# Consumir um servidor com a extensão AI Toolkit para Visual Studio Code

Ao criar um agente de IA, não se trata apenas de gerar respostas inteligentes; é também sobre dar ao seu agente a capacidade de agir. É aqui que entra o Model Context Protocol (MCP). O MCP facilita o acesso dos agentes a ferramentas e serviços externos de forma consistente. Pense nisso como conectar o seu agente a uma caixa de ferramentas que ele pode *realmente* usar.

Imagine que você conecta um agente ao seu servidor MCP de calculadora. De repente, o seu agente pode realizar operações matemáticas apenas recebendo um comando como “Quanto é 47 vezes 89?”—sem necessidade de codificar lógica ou criar APIs personalizadas.

## Visão Geral

Esta lição aborda como conectar um servidor MCP de calculadora a um agente usando a extensão [AI Toolkit](https://aka.ms/AIToolkit) no Visual Studio Code, permitindo que o seu agente realize operações matemáticas como adição, subtração, multiplicação e divisão através de linguagem natural.

O AI Toolkit é uma extensão poderosa para o Visual Studio Code que simplifica o desenvolvimento de agentes. Engenheiros de IA podem facilmente criar aplicações de IA desenvolvendo e testando modelos generativos de IA—localmente ou na nuvem. A extensão suporta a maioria dos principais modelos generativos disponíveis atualmente.

*Nota*: O AI Toolkit atualmente suporta Python e TypeScript.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Consumir um servidor MCP através do AI Toolkit.
- Configurar um agente para descobrir e utilizar ferramentas fornecidas pelo servidor MCP.
- Utilizar ferramentas MCP através de linguagem natural.

## Abordagem

Aqui está como devemos abordar isso em um nível geral:

- Criar um agente e definir o seu prompt do sistema.
- Criar um servidor MCP com ferramentas de calculadora.
- Conectar o Agent Builder ao servidor MCP.
- Testar a invocação de ferramentas do agente através de linguagem natural.

Ótimo, agora que entendemos o fluxo, vamos configurar um agente de IA para aproveitar ferramentas externas através do MCP, ampliando suas capacidades!

## Pré-requisitos

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit para Visual Studio Code](https://aka.ms/AIToolkit)

## Exercício: Consumir um servidor

> [!WARNING]
> Nota para utilizadores de macOS. Estamos atualmente a investigar um problema que afeta a instalação de dependências no macOS. Como resultado, os utilizadores de macOS não poderão concluir este tutorial neste momento. Atualizaremos as instruções assim que uma correção estiver disponível. Obrigado pela sua paciência e compreensão!

Neste exercício, você irá criar, executar e aprimorar um agente de IA com ferramentas de um servidor MCP dentro do Visual Studio Code usando o AI Toolkit.

### -0- Passo prévio, adicionar o modelo OpenAI GPT-4o aos Meus Modelos

O exercício utiliza o modelo **GPT-4o**. O modelo deve ser adicionado aos **Meus Modelos** antes de criar o agente.

![Captura de ecrã de uma interface de seleção de modelos na extensão AI Toolkit do Visual Studio Code. O título diz "Encontre o modelo certo para a sua solução de IA" com um subtítulo incentivando os utilizadores a descobrir, testar e implementar modelos de IA. Abaixo, sob “Modelos Populares,” são exibidos seis cartões de modelos: DeepSeek-R1 (hospedado no GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Pequeno, Rápido) e DeepSeek-R1 (hospedado no Ollama). Cada cartão inclui opções para “Adicionar” o modelo ou “Experimentar no Playground](../../../../translated_images/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.pt.png)

1. Abra a extensão **AI Toolkit** na **Barra de Atividades**.
1. Na seção **Catálogo**, selecione **Modelos** para abrir o **Catálogo de Modelos**. Selecionar **Modelos** abre o **Catálogo de Modelos** numa nova aba do editor.
1. Na barra de pesquisa do **Catálogo de Modelos**, insira **OpenAI GPT-4o**.
1. Clique em **+ Adicionar** para adicionar o modelo à sua lista de **Meus Modelos**. Certifique-se de que selecionou o modelo **Hospedado no GitHub**.
1. Na **Barra de Atividades**, confirme que o modelo **OpenAI GPT-4o** aparece na lista.

### -1- Criar um agente

O **Agent (Prompt) Builder** permite que você crie e personalize os seus próprios agentes com IA. Nesta seção, você criará um novo agente e atribuirá um modelo para alimentar a conversa.

![Captura de ecrã da interface "Calculator Agent" no AI Toolkit para Visual Studio Code. No painel esquerdo, o modelo selecionado é "OpenAI GPT-4o (via GitHub)." Um prompt do sistema diz "Você é um professor universitário que ensina matemática," e o prompt do utilizador diz, "Explique-me a equação de Fourier em termos simples." Opções adicionais incluem botões para adicionar ferramentas, ativar o servidor MCP e selecionar saída estruturada. Um botão azul “Executar” está na parte inferior. No painel direito, sob "Comece com Exemplos," três agentes de exemplo estão listados: Desenvolvedor Web (com Servidor MCP, Simplificador de Segunda Classe e Intérprete de Sonhos, cada um com descrições breves das suas funções).](../../../../translated_images/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.pt.png)

1. Abra a extensão **AI Toolkit** na **Barra de Atividades**.
1. Na seção **Ferramentas**, selecione **Agent (Prompt) Builder**. Selecionar **Agent (Prompt) Builder** abre o **Agent (Prompt) Builder** numa nova aba do editor.
1. Clique no botão **+ Novo Agente**. A extensão iniciará um assistente de configuração através do **Command Palette**.
1. Insira o nome **Calculator Agent** e pressione **Enter**.
1. No **Agent (Prompt) Builder**, para o campo **Modelo**, selecione o modelo **OpenAI GPT-4o (via GitHub)**.

### -2- Criar um prompt do sistema para o agente

Com o agente estruturado, é hora de definir sua personalidade e propósito. Nesta seção, você usará o recurso **Gerar prompt do sistema** para descrever o comportamento pretendido do agente—neste caso, um agente de calculadora—e deixar o modelo escrever o prompt do sistema para você.

![Captura de ecrã da interface "Calculator Agent" no AI Toolkit para Visual Studio Code com uma janela modal aberta intitulada "Gerar um prompt." A modal explica que um modelo de prompt pode ser gerado compartilhando detalhes básicos e inclui uma caixa de texto com o prompt do sistema de exemplo: "Você é um assistente de matemática útil e eficiente. Quando recebe um problema envolvendo aritmética básica, responde com o resultado correto." Abaixo da caixa de texto estão os botões "Fechar" e "Gerar." Ao fundo, parte da configuração do agente é visível, incluindo o modelo selecionado "OpenAI GPT-4o (via GitHub)" e campos para prompts do sistema e do utilizador.](../../../../translated_images/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.pt.png)

1. Na seção **Prompts**, clique no botão **Gerar prompt do sistema**. Este botão abre o construtor de prompts, que utiliza IA para gerar um prompt do sistema para o agente.
1. Na janela **Gerar um prompt**, insira o seguinte: `Você é um assistente de matemática útil e eficiente. Quando recebe um problema envolvendo aritmética básica, responde com o resultado correto.`
1. Clique no botão **Gerar**. Uma notificação aparecerá no canto inferior direito confirmando que o prompt do sistema está sendo gerado. Assim que a geração do prompt for concluída, o prompt aparecerá no campo **Prompt do sistema** do **Agent (Prompt) Builder**.
1. Revise o **Prompt do sistema** e modifique, se necessário.

### -3- Criar um servidor MCP

Agora que você definiu o prompt do sistema do seu agente—orientando seu comportamento e respostas—é hora de equipar o agente com capacidades práticas. Nesta seção, você criará um servidor MCP de calculadora com ferramentas para executar cálculos de adição, subtração, multiplicação e divisão. Este servidor permitirá que o seu agente realize operações matemáticas em tempo real em resposta a comandos de linguagem natural.

!["Captura de ecrã da seção inferior da interface Calculator Agent na extensão AI Toolkit para Visual Studio Code. Mostra menus expansíveis para “Ferramentas” e “Saída estruturada,” juntamente com um menu suspenso rotulado “Escolher formato de saída” definido como “texto.” À direita, há um botão rotulado “+ Servidor MCP” para adicionar um servidor Model Context Protocol. Um ícone de espaço reservado para imagem é mostrado acima da seção Ferramentas.](../../../../translated_images/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.pt.png)

O AI Toolkit está equipado com templates para facilitar a criação do seu próprio servidor MCP. Usaremos o template Python para criar o servidor MCP de calculadora.

*Nota*: O AI Toolkit atualmente suporta Python e TypeScript.

1. Na seção **Ferramentas** do **Agent (Prompt) Builder**, clique no botão **+ Servidor MCP**. A extensão iniciará um assistente de configuração através do **Command Palette**.
1. Selecione **+ Adicionar Servidor**.
1. Selecione **Criar um Novo Servidor MCP**.
1. Selecione **python-weather** como o template.
1. Selecione **Pasta padrão** para salvar o template do servidor MCP.
1. Insira o seguinte nome para o servidor: **Calculator**
1. Uma nova janela do Visual Studio Code será aberta. Selecione **Sim, confio nos autores**.
1. Usando o terminal (**Terminal** > **Novo Terminal**), crie um ambiente virtual: `python -m venv .venv`
1. Usando o terminal, ative o ambiente virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source venv/bin/activate`
1. Usando o terminal, instale as dependências: `pip install -e .[dev]`
1. Na visualização **Explorer** da **Barra de Atividades**, expanda o diretório **src** e selecione **server.py** para abrir o arquivo no editor.
1. Substitua o código no arquivo **server.py** pelo seguinte e salve:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Executar o agente com o servidor MCP de calculadora

Agora que o seu agente tem ferramentas, é hora de usá-las! Nesta seção, você enviará comandos ao agente para testar e validar se ele utiliza a ferramenta apropriada do servidor MCP de calculadora.

![Captura de ecrã da interface Calculator Agent na extensão AI Toolkit para Visual Studio Code. No painel esquerdo, sob “Ferramentas,” um servidor MCP chamado local-server-calculator_server é adicionado, mostrando quatro ferramentas disponíveis: add, subtract, multiply e divide. Um indicador mostra que quatro ferramentas estão ativas. Abaixo está uma seção “Saída estruturada” recolhida e um botão azul “Executar.” No painel direito, sob “Resposta do Modelo,” o agente invoca as ferramentas multiply e subtract com entradas {"a": 3, "b": 25} e {"a": 75, "b": 20} respectivamente. A “Resposta da Ferramenta” final é mostrada como 75.0. Um botão “Ver Código” aparece na parte inferior.](../../../../translated_images/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.pt.png)

Você executará o servidor MCP de calculadora na sua máquina de desenvolvimento local através do **Agent Builder** como cliente MCP.

1. Pressione `F5` para iniciar a depuração do servidor MCP. O **Agent (Prompt) Builder** será aberto numa nova aba do editor. O status do servidor é visível no terminal.
1. No campo **Prompt do utilizador** do **Agent (Prompt) Builder**, insira o seguinte comando: `Comprei 3 itens a $25 cada, e depois usei um desconto de $20. Quanto paguei?`
1. Clique no botão **Executar** para gerar a resposta do agente.
1. Revise a saída do agente. O modelo deve concluir que você pagou **$55**.
1. Aqui está um resumo do que deve ocorrer:
    - O agente seleciona as ferramentas **multiply** e **subtract** para auxiliar no cálculo.
    - Os valores `a` e `b` são atribuídos para a ferramenta **multiply**.
    - Os valores `a` e `b` são atribuídos para a ferramenta **subtract**.
    - A resposta de cada ferramenta é fornecida na respectiva **Resposta da Ferramenta**.
    - A saída final do modelo é fornecida na **Resposta do Modelo**.
1. Envie comandos adicionais para testar ainda mais o agente. Você pode modificar o comando existente no campo **Prompt do utilizador** clicando no campo e substituindo o comando existente.
1. Quando terminar de testar o agente, você pode parar o servidor através do **terminal** inserindo **CTRL/CMD+C** para sair.

## Tarefa

Tente adicionar uma entrada de ferramenta adicional ao seu arquivo **server.py** (ex: retornar a raiz quadrada de um número). Envie comandos adicionais que exijam que o agente utilize a sua nova ferramenta (ou ferramentas existentes). Certifique-se de reiniciar o servidor para carregar as ferramentas recém-adicionadas.

## Solução

[Solução](./solution/README.md)

## Principais Conclusões

As principais conclusões deste capítulo são as seguintes:

- A extensão AI Toolkit é um ótimo cliente que permite consumir Servidores MCP e suas ferramentas.
- Você pode adicionar novas ferramentas aos servidores MCP, expandindo as capacidades do agente para atender a requisitos em evolução.
- O AI Toolkit inclui templates (ex: templates de servidor MCP em Python) para simplificar a criação de ferramentas personalizadas.

## Recursos Adicionais

- [Documentação do AI Toolkit](https://aka.ms/AIToolkit/doc)

## O que vem a seguir
- Próximo: [Testar e Depurar](../08-testing/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.