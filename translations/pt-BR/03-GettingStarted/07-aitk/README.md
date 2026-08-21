# Consumindo um servidor da extensão AI Toolkit para Visual Studio Code

Quando você está construindo um agente de IA, não se trata apenas de gerar respostas inteligentes; trata-se também de dar ao seu agente a capacidade de agir. É aí que entra o Model Context Protocol (MCP). O MCP facilita o acesso dos agentes a ferramentas e serviços externos de maneira consistente. Pense nisso como conectar seu agente a uma caixa de ferramentas que ele pode *realmente* usar.

Suponha que você conecte um agente ao seu servidor MCP de calculadora. De repente, seu agente pode realizar operações matemáticas apenas recebendo um prompt como “Quanto é 47 vezes 89?”—sem necessidade de codificar lógica fixa ou construir APIs personalizadas.

## Visão Geral

Esta lição cobre como conectar um servidor MCP de calculadora a um agente com a extensão [AI Toolkit](https://aka.ms/AIToolkit) no Visual Studio Code, permitindo que seu agente realize operações matemáticas como adição, subtração, multiplicação e divisão por meio da linguagem natural.

AI Toolkit é uma extensão poderosa para o Visual Studio Code que simplifica o desenvolvimento de agentes. Engenheiros de IA podem facilmente construir aplicações de IA desenvolvendo e testando modelos generativos—localmente ou na nuvem. A extensão suporta a maioria dos principais modelos generativos disponíveis atualmente.

*Nota*: O AI Toolkit atualmente suporta Python e TypeScript.

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Consumir um servidor MCP via AI Toolkit.
- Configurar uma configuração de agente para habilitar a descoberta e utilização de ferramentas fornecidas pelo servidor MCP.
- Utilizar ferramentas MCP por meio da linguagem natural.

## Abordagem

Aqui está como precisamos abordar isso em alto nível:

- Criar um agente e definir seu prompt de sistema.
- Criar um servidor MCP com ferramentas de calculadora.
- Conectar o Agent Builder ao servidor MCP.
- Testar a invocação das ferramentas do agente via linguagem natural.

Ótimo, agora que entendemos o fluxo, vamos configurar um agente de IA para aproveitar ferramentas externas através do MCP, aumentando suas capacidades!

## Pré-requisitos

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit para Visual Studio Code](https://aka.ms/AIToolkit)

## Exercício: Consumindo um servidor

> [!WARNING]
> Nota para usuários macOS. Atualmente estamos investigando um problema que afeta a instalação de dependências no macOS. Como resultado, usuários macOS não poderão completar este tutorial no momento. Atualizaremos as instruções assim que uma correção estiver disponível. Obrigado pela paciência e compreensão!

Neste exercício, você irá construir, executar e aprimorar um agente de IA com ferramentas de um servidor MCP dentro do Visual Studio Code usando o AI Toolkit.

### -0- Passo preliminar, adicionar o modelo OpenAI GPT-4o aos Meus Modelos

O exercício utiliza o modelo **GPT-4o**. O modelo deve ser adicionado aos **Meus Modelos** antes de criar o agente.

![Captura de tela da interface de seleção de modelo na extensão AI Toolkit do Visual Studio Code. O título diz "Encontre o modelo certo para sua solução de IA" com um subtítulo incentivando a descoberta, teste e implantação de modelos de IA. Abaixo, em “Modelos Populares,” seis cartões de modelo são mostrados: DeepSeek-R1 (hospedado pelo GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Pequeno, Rápido), e DeepSeek-R1 (hospedado pelo Ollama). Cada cartão inclui opções para “Adicionar” o modelo ou “Testar na Playground”.](../../../../translated_images/pt-BR/aitk-model-catalog.2acd38953bb9c119.webp)

1. Abra a extensão **AI Toolkit** na **Barra de Atividades**.
1. Na seção **Catálogo**, selecione **Modelos** para abrir o **Catálogo de Modelos**. Selecionar **Modelos** abre o **Catálogo de Modelos** em uma nova aba do editor.
1. Na barra de busca do **Catálogo de Modelos**, digite **OpenAI GPT-4o**.
1. Clique em **+ Adicionar** para adicionar o modelo à sua lista **Meus Modelos**. Certifique-se de ter selecionado o modelo que está **Hospedado pelo GitHub**.
1. Na **Barra de Atividades**, confirme que o modelo **OpenAI GPT-4o** aparece na lista.

### -1- Criar um agente

O **Agent (Prompt) Builder** permite criar e personalizar seus próprios agentes movidos a IA. Nesta seção, você criará um novo agente e atribuirá um modelo para impulsionar a conversa.

![Captura de tela da interface do construtor "Agente Calculadora" na extensão AI Toolkit para Visual Studio Code. No painel esquerdo, o modelo selecionado é "OpenAI GPT-4o (via GitHub)." Um prompt de sistema diz "Você é um professor universitário ensinando matemática," e o prompt do usuário diz "Explique para mim a equação de Fourier em termos simples." Opções adicionais incluem botões para adicionar ferramentas, habilitar o MCP Server e selecionar saída estruturada. Um botão azul “Executar” está na parte inferior. No painel direito, sob "Comece com Exemplos," três agentes de exemplo são listados: Desenvolvedor Web (com MCP Server, Simplificador para segundo grau, e Interpretador de Sonhos, cada um com descrições breves de suas funções).](../../../../translated_images/pt-BR/aitk-agent-builder.901e3a2960c3e477.webp)

1. Abra a extensão **AI Toolkit** na **Barra de Atividades**.
1. Na seção **Ferramentas**, selecione **Agent (Prompt) Builder**. Selecionar **Agent (Prompt) Builder** abre o **Agent (Prompt) Builder** em uma nova aba do editor.
1. Clique no botão **+ Novo Agente**. A extensão abrirá um assistente via **Paleta de Comandos**.
1. Digite o nome **Agente Calculadora** e pressione **Enter**.
1. No **Agent (Prompt) Builder**, para o campo **Modelo**, selecione o modelo **OpenAI GPT-4o (via GitHub)**.

### -2- Criar um prompt de sistema para o agente

Com o agente estruturado, é hora de definir sua personalidade e propósito. Nesta seção, você usará o recurso **Gerar prompt de sistema** para descrever o comportamento pretendido do agente—neste caso, um agente calculadora—e fazer o modelo gerar o prompt para você.

![Captura de tela da interface do "Agente Calculadora" na extensão AI Toolkit para Visual Studio Code com uma janela modal aberta intitulada "Gerar um prompt." A modal explica que um template de prompt pode ser gerado compartilhando detalhes básicos e inclui uma caixa de texto com o prompt de sistema exemplo: "Você é um assistente de matemática útil e eficiente. Quando recebe um problema envolvendo aritmética básica, responde com o resultado correto." Abaixo da caixa de texto estão os botões "Fechar" e "Gerar." Ao fundo, parte da configuração do agente é visível, incluindo o modelo selecionado "OpenAI GPT-4o (via GitHub)" e campos para prompts do sistema e do usuário.](../../../../translated_images/pt-BR/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Para a seção **Prompts**, clique no botão **Gerar prompt de sistema**. Esse botão abre o construtor de prompts que utiliza IA para gerar um prompt de sistema para o agente.
1. Na janela **Gerar um prompt**, digite o seguinte: `Você é um assistente de matemática útil e eficiente. Quando recebe um problema envolvendo aritmética básica, responde com o resultado correto.`
1. Clique no botão **Gerar**. Uma notificação aparecerá no canto inferior direito confirmando que o prompt de sistema está sendo gerado. Quando a geração do prompt for concluída, o prompt aparecerá no campo **Prompt de sistema** do **Agent (Prompt) Builder**.
1. Reveja o **Prompt de sistema** e modifique se necessário.

### -3- Criar um servidor MCP

Agora que você definiu o prompt de sistema do seu agente—guiando seu comportamento e respostas—é hora de equipar o agente com capacidades práticas. Nesta seção, você criará um servidor MCP de calculadora com ferramentas para executar cálculos de adição, subtração, multiplicação e divisão. Esse servidor permitirá que seu agente realize operações matemáticas em tempo real em resposta a prompts em linguagem natural.

!["Captura de tela da seção inferior da interface do Agente Calculadora na extensão AI Toolkit para Visual Studio Code. Mostra menus expansíveis para “Ferramentas” e “Saída estruturada,” junto de um menu suspenso rotulado “Escolha o formato de saída” definido como “texto.” À direita, há um botão chamado “+ MCP Server” para adicionar um servidor Model Context Protocol. Um espaço reservado de ícone de imagem é mostrado acima da seção Ferramentas.](../../../../translated_images/pt-BR/aitk-add-mcp-server.9742cfddfe808353.webp)

O AI Toolkit está equipado com templates para facilitar a criação do seu próprio servidor MCP. Usaremos o template Python para criar o servidor MCP de calculadora.

*Nota*: O AI Toolkit atualmente suporta Python e TypeScript.

1. Na seção **Ferramentas** do **Agent (Prompt) Builder**, clique no botão **+ MCP Server**. A extensão abrirá um assistente via **Paleta de Comandos**.
1. Selecione **+ Adicionar Servidor**.
1. Selecione **Criar um Novo Servidor MCP**.
1. Selecione **python-weather** como o template.
1. Selecione **Pasta padrão** para salvar o template do servidor MCP.
1. Digite o seguinte nome para o servidor: **Calculadora**
1. Uma nova janela do Visual Studio Code abrirá. Selecione **Sim, confio nos autores**.
1. Usando o terminal (**Terminal** > **Novo Terminal**), crie um ambiente virtual: `python -m venv .venv`
1. Usando o terminal, ative o ambiente virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
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

### -4- Execute o agente com o servidor MCP de calculadora

Agora que seu agente tem ferramentas, é hora de usá-las! Nesta seção, você enviará prompts para o agente para testar e validar se o agente utiliza a ferramenta apropriada do servidor MCP de calculadora.

![Captura de tela da interface do Agente Calculadora na extensão AI Toolkit para Visual Studio Code. No painel esquerdo, sob “Ferramentas,” um servidor MCP chamado local-server-calculator_server está adicionado, mostrando quatro ferramentas disponíveis: adicionar, subtrair, multiplicar e dividir. Um distintivo mostra que quatro ferramentas estão ativas. Abaixo está uma seção de “Saída estruturada” colapsada e um botão azul “Executar.” No painel direito, sob “Resposta do Modelo,” o agente invoca as ferramentas multiplicar e subtrair com entradas {"a": 3, "b": 25} e {"a": 75, "b": 20} respectivamente. A “Resposta da ferramenta” final é mostrada como 75.0. Um botão “Ver Código” aparece na parte inferior.](../../../../translated_images/pt-BR/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Você executará o servidor MCP de calculadora em sua máquina local de desenvolvimento via o **Agent Builder** como cliente MCP.

1. Pressione `F5` para iniciar a depuração do servidor MCP. O **Agent (Prompt) Builder** abrirá em uma nova aba do editor. O status do servidor é visível no terminal.
1. No campo **Prompt do usuário** do **Agent (Prompt) Builder**, digite o seguinte prompt: `Comprei 3 itens custando $25 cada, e depois usei um desconto de $20. Quanto paguei?`
1. Clique no botão **Executar** para gerar a resposta do agente.
1. Revise a saída do agente. O modelo deve concluir que você pagou **$55**.
1. Aqui está uma descrição do que deve ocorrer:
    - O agente seleciona as ferramentas **multiplicar** e **subtrair** para ajudar no cálculo.
    - Os valores respectivos `a` e `b` são atribuídos para a ferramenta **multiplicar**.
    - Os valores respectivos `a` e `b` são atribuídos para a ferramenta **subtrair**.
    - As respostas de cada ferramenta são fornecidas na respectiva **Resposta da Ferramenta**.
    - A saída final do modelo é fornecida na **Resposta do Modelo** final.
1. Envie prompts adicionais para testar mais o agente. Você pode modificar o prompt existente no campo **Prompt do usuário** clicando no campo e substituindo o prompt atual.
1. Quando terminar de testar o agente, você pode parar o servidor pelo **terminal** pressionando **CTRL/CMD+C** para sair.

## Tarefa

Tente adicionar uma entrada de ferramenta adicional ao seu arquivo **server.py** (ex: retorne a raiz quadrada de um número). Envie prompts adicionais que exijam que o agente utilize sua nova ferramenta (ou ferramentas existentes). Certifique-se de reiniciar o servidor para carregar as ferramentas recém-adicionadas.

## Solução

[Solução](./solution/README.md)

## Principais Conclusões

As principais conclusões deste capítulo são as seguintes:

- A extensão AI Toolkit é um ótimo cliente que permite consumir servidores MCP e suas ferramentas.
- Você pode adicionar novas ferramentas aos servidores MCP, expandindo as capacidades do agente para atender a requisitos em evolução.
- O AI Toolkit inclui templates (ex: templates de servidor MCP em Python) para simplificar a criação de ferramentas personalizadas.

## Recursos Adicionais

- [Documentação do AI Toolkit](https://aka.ms/AIToolkit/doc)

## Próximos Passos
- Próximo: [Testes e Depuração](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->