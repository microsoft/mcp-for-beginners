# Consumir um servidor a partir da extensão AI Toolkit para Visual Studio Code

Quando está a construir um agente de IA, não se trata apenas de gerar respostas inteligentes; trata-se também de dar ao seu agente a capacidade de agir. É aqui que entra o Protocolo de Contexto de Modelo (MCP). O MCP facilita o acesso dos agentes a ferramentas e serviços externos de forma consistente. Pense nisso como ligar o seu agente a uma caixa de ferramentas que ele pode *realmente* usar.

Suponha que liga um agente ao seu servidor MCP de calculadora. De repente, o seu agente consegue executar operações matemáticas apenas recebendo um comando como “Quanto é 47 vezes 89?” — sem necessidade de codificar lógica rígida ou construir APIs personalizadas.

## Visão Geral

Esta lição aborda como ligar um servidor MCP de calculadora a um agente com a extensão [AI Toolkit](https://aka.ms/AIToolkit) no Visual Studio Code, permitindo que o seu agente realize operações matemáticas como adição, subtração, multiplicação e divisão através da linguagem natural.

A AI Toolkit é uma extensão poderosa para o Visual Studio Code que simplifica o desenvolvimento de agentes. Os engenheiros de IA podem facilmente construir aplicações de IA desenvolvendo e testando modelos generativos de IA—localmente ou na cloud. A extensão suporta a maioria dos grandes modelos generativos disponíveis hoje.

*Nota*: Atualmente, a AI Toolkit suporta Python e TypeScript.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Consumir um servidor MCP via AI Toolkit.
- Configurar uma configuração de agente para permitir descobrir e utilizar ferramentas fornecidas pelo servidor MCP.
- Utilizar ferramentas MCP através da linguagem natural.

## Abordagem

Eis como devemos abordar isto a alto nível:

- Criar um agente e definir o seu prompt de sistema.
- Criar um servidor MCP com ferramentas de calculadora.
- Ligar o construtor de agentes ao servidor MCP.
- Testar a invocação das ferramentas do agente via linguagem natural.

Ótimo, agora que entendemos o fluxo, vamos configurar um agente de IA para aproveitar ferramentas externas através do MCP, melhorando as suas capacidades!

## Pré-requisitos

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit para Visual Studio Code](https://aka.ms/AIToolkit)

## Exercício: Consumir um servidor

> [!WARNING]
> Nota para utilizadores de macOS. Estamos atualmente a investigar um problema que afeta a instalação de dependências no macOS. Como resultado, os utilizadores de macOS não conseguirão completar este tutorial neste momento. Vamos atualizar as instruções assim que uma correção estiver disponível. Obrigado pela sua paciência e compreensão!

Neste exercício, irá construir, executar e melhorar um agente de IA com ferramentas de um servidor MCP dentro do Visual Studio Code usando a AI Toolkit.

### -0- Passo prévio, adicionar o modelo OpenAI GPT-4o aos Meus Modelos

O exercício utiliza o modelo **GPT-4o**. O modelo deve ser adicionado a **Meus Modelos** antes de criar o agente.

![Captura de ecrã de uma interface de seleção de modelos na extensão AI Toolkit do Visual Studio Code. O título lê "Encontre o modelo certo para a sua solução de IA" com uma legenda a incentivar os utilizadores a descobrir, testar e implementar modelos de IA. Abaixo, sob “Modelos Populares,” estão exibidos seis cartões de modelos: DeepSeek-R1 (hospedado no GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Pequeno, Rápido) e DeepSeek-R1 (hospedado pela Ollama). Cada cartão inclui opções para “Adicionar” o modelo ou “Testar no Playground”.](../../../../translated_images/pt-PT/aitk-model-catalog.2acd38953bb9c119.webp)

1. Abra a extensão **AI Toolkit** a partir da **Barra de Atividades**.
1. Na secção **Catálogo**, selecione **Modelos** para abrir o **Catálogo de Modelos**. Selecionar **Modelos** abre o **Catálogo de Modelos** numa nova aba do editor.
1. Na barra de pesquisa do **Catálogo de Modelos**, escreva **OpenAI GPT-4o**.
1. Clique em **+ Adicionar** para adicionar o modelo à sua lista de **Meus Modelos**. Certifique-se de que selecionou o modelo que está **Hospedado no GitHub**.
1. Na **Barra de Atividades**, confirme que o modelo **OpenAI GPT-4o** aparece na lista.

### -1- Criar um agente

O **Construtor de Agentes (Prompt)** permite criar e personalizar os seus próprios agentes alimentados por IA. Nesta secção, irá criar um novo agente e atribuir um modelo para alimentar a conversa.

![Captura de ecrã da interface do construtor "Agente Calculadora" na extensão AI Toolkit para Visual Studio Code. No painel esquerdo, o modelo selecionado é "OpenAI GPT-4o (via GitHub)." Um prompt de sistema diz "Você é um professor universitário a ensinar matemática," e o prompt do utilizador diz, "Explique a equação de Fourier em termos simples." Opções adicionais incluem botões para adicionar ferramentas, ativar Servidor MCP e selecionar saída estruturada. Um botão azul “Executar” está na parte inferior. No painel direito, sob "Começar com Exemplos," são listados três agentes de exemplo: Desenvolvedor Web (com Servidor MCP, Simplificador do 2º ano, e Intérprete de Sonhos, cada um com descrições breves das suas funções.](../../../../translated_images/pt-PT/aitk-agent-builder.901e3a2960c3e477.webp)

1. Abra a extensão **AI Toolkit** a partir da **Barra de Atividades**.
1. Na secção **Ferramentas**, selecione **Construtor de Agentes (Prompt)**. Selecionar **Construtor de Agentes (Prompt)** abre o **Construtor de Agentes (Prompt)** numa nova aba do editor.
1. Clique no botão **+ Novo Agente**. A extensão iniciará um assistente de configuração via a **Paleta de Comandos**.
1. Introduza o nome **Agente Calculadora** e pressione **Enter**.
1. No **Construtor de Agentes (Prompt)**, no campo **Modelo**, selecione o modelo **OpenAI GPT-4o (via GitHub)**.

### -2- Criar um prompt de sistema para o agente

Com o agente criado, é tempo de definir a sua personalidade e propósito. Nesta secção, utilizará a funcionalidade **Gerar prompt de sistema** para descrever o comportamento pretendido do agente—neste caso, um agente calculadora—e deixar o modelo escrever o prompt de sistema por si.

![Captura de ecrã da interface "Agente Calculadora" na AI Toolkit para Visual Studio Code com uma janela modal aberta intitulada "Gerar um prompt." A modal explica que um modelo de prompt pode ser gerado ao partilhar detalhes básicos e inclui uma caixa de texto com o prompt de sistema exemplo: "Você é um assistente de matemática prestável e eficiente. Quando confrontado com um problema envolvendo aritmética básica, responde com o resultado correto." Abaixo da caixa de texto estão os botões "Fechar" e "Gerar". Em segundo plano, parte da configuração do agente está visível, incluindo o modelo selecionado "OpenAI GPT-4o (via GitHub)" e campos para prompts de sistema e utilizador.](../../../../translated_images/pt-PT/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Para a secção **Prompts**, clique no botão **Gerar prompt de sistema**. Este botão abre o construtor de prompts que utiliza IA para gerar um prompt de sistema para o agente.
1. Na janela **Gerar um prompt**, introduza o seguinte: `Você é um assistente de matemática prestável e eficiente. Quando confrontado com um problema envolvendo aritmética básica, responde com o resultado correto.`
1. Clique no botão **Gerar**. Uma notificação aparecerá no canto inferior direito confirmando que o prompt de sistema está a ser gerado. Quando a geração do prompt estiver completa, o prompt aparecerá no campo **Prompt de sistema** do **Construtor de Agentes (Prompt)**.
1. Reveja o **Prompt de sistema** e modifique se necessário.

### -3- Criar um servidor MCP

Agora que definiu o prompt do sistema do seu agente — orientando o seu comportamento e respostas — é tempo de equipar o agente com capacidades práticas. Nesta secção, irá criar um servidor MCP de calculadora com ferramentas para executar cálculos de adição, subtração, multiplicação e divisão. Este servidor permitirá que o seu agente realize operações matemáticas em tempo real em resposta a comandos em linguagem natural.

![Captura de ecrã da parte inferior da interface do Agente Calculadora na extensão AI Toolkit para Visual Studio Code. Mostra menus expansíveis para “Ferramentas” e “Saída estruturada,” juntamente com um menu suspenso rotulado “Escolher formato de saída” definido para “texto.” À direita, há um botão rotulado “+ Servidor MCP” para adicionar um servidor Protocolo de Contexto de Modelo. Um marcador de espaço para ícone de imagem é mostrado acima da secção Ferramentas.](../../../../translated_images/pt-PT/aitk-add-mcp-server.9742cfddfe808353.webp)

A AI Toolkit está equipada com modelos para facilitar a criação do seu próprio servidor MCP. Usaremos o modelo Python para criar o servidor MCP da calculadora.

*Nota*: Atualmente, a AI Toolkit suporta Python e TypeScript.

1. Na secção **Ferramentas** do **Construtor de Agentes (Prompt)**, clique no botão **+ Servidor MCP**. A extensão iniciará um assistente via a **Paleta de Comandos**.
1. Selecione **+ Adicionar Servidor**.
1. Selecione **Criar um Novo Servidor MCP**.
1. Selecione o modelo **python-weather**.
1. Selecione **Pasta padrão** para guardar o modelo do servidor MCP.
1. Introduza o seguinte nome para o servidor: **Calculadora**
1. Abrirá uma nova janela do Visual Studio Code. Selecione **Sim, confio nos autores**.
1. Usando o terminal (**Terminal** > **Novo Terminal**), crie um ambiente virtual: `python -m venv .venv`
1. Usando o terminal, ative o ambiente virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Usando o terminal, instale as dependências: `pip install -e .[dev]`
1. Na vista **Explorer** da **Barra de Atividades**, expanda o diretório **src** e selecione **server.py** para abrir o ficheiro no editor.
1. Substitua o código no arquivo **server.py** pelo seguinte e guarde:

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

Agora que o seu agente tem ferramentas, é tempo de usá-las! Nesta secção, irá submeter prompts ao agente para testar e validar se o agente usa a ferramenta adequada do servidor MCP da calculadora.

![Captura de ecrã da interface do Agente Calculadora na extensão AI Toolkit para Visual Studio Code. No painel esquerdo, sob “Ferramentas,” um servidor MCP chamado local-server-calculator_server é adicionado, mostrando quatro ferramentas disponíveis: adicionar, subtrair, multiplicar e dividir. Um distintivo mostra que quatro ferramentas estão ativas. Abaixo está uma secção “Saída estruturada” recolhida e um botão azul “Executar.” No painel direito, sob “Resposta do Modelo,” o agente invoca as ferramentas multiplicar e subtrair com entradas {"a": 3, "b": 25} e {"a": 75, "b": 20} respetivamente. A resposta final da “Resposta da Ferramenta” está mostrada como 75.0. Um botão “Ver Código” aparece na parte inferior.](../../../../translated_images/pt-PT/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Irá executar o servidor MCP da calculadora na sua máquina local de desenvolvimento via o **Construtor de Agentes** como cliente MCP.

1. Pressione `F5` para começar a depuração do servidor MCP. O **Construtor de Agentes (Prompt)** será aberto numa nova aba do editor. O estado do servidor é visível no terminal.
1. No campo **Prompt do utilizador** do **Construtor de Agentes (Prompt)**, introduza o seguinte prompt: `Comprei 3 itens com preço de 25 dólares cada, e depois usei um desconto de 20 dólares. Quanto paguei?`
1. Clique no botão **Executar** para gerar a resposta do agente.
1. Reveja a saída do agente. O modelo deverá concluir que pagou **55 dólares**.
1. Eis uma decomposição do que deve acontecer:
    - O agente seleciona as ferramentas **multiplicar** e **subtrair** para ajudar no cálculo.
    - Os valores `a` e `b` respetivos são atribuídos para a ferramenta **multiplicar**.
    - Os valores `a` e `b` respetivos são atribuídos para a ferramenta **subtrair**.
    - A resposta de cada ferramenta é fornecida em **Resposta da Ferramenta** respetiva.
    - A saída final do modelo é fornecida na **Resposta do Modelo** final.
1. Submeta prompts adicionais para testar mais o agente. Pode modificar o prompt existente no campo **Prompt do utilizador** clicando no campo e substituindo o prompt existente.
1. Quando terminar de testar o agente, pode parar o servidor via o **terminal**, pressionando **CTRL/CMD+C** para sair.

## Tarefa

Tente adicionar uma ferramenta adicional ao seu ficheiro **server.py** (ex: devolver a raiz quadrada de um número). Submeta prompts adicionais que exijam que o agente utilize essa nova ferramenta (ou ferramentas existentes). Certifique-se de reiniciar o servidor para carregar as ferramentas recém-adicionadas.

## Solução

[Solução](./solution/README.md)

## Principais Conclusões

As conclusões deste capítulo são as seguintes:

- A extensão AI Toolkit é um excelente cliente que permite consumir Servidores MCP e as suas ferramentas.
- Pode adicionar novas ferramentas a servidores MCP, expandindo as capacidades do agente para atender a requisitos em evolução.
- A AI Toolkit inclui modelos (ex: modelos de servidor MCP Python) para simplificar a criação de ferramentas personalizadas.

## Recursos Adicionais

- [Documentação do AI Toolkit](https://aka.ms/AIToolkit/doc)

## Próximos Passos
- A seguir: [Testes e Depuração](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->