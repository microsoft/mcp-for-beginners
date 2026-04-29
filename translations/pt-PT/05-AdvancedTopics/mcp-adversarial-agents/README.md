# Raciocínio Multi-Agente Adversarial com MCP

Os padrões de debate multi-agente utilizam dois ou mais agentes com posições opostas para produzir saídas mais fiáveis e bem calibradas do que um único agente poderia alcançar sozinho.

## Introdução

Nesta lição, exploramos o **padrão multi-agente adversarial** — uma técnica onde dois agentes de IA são atribuídos a posições opostas sobre um tema e devem raciocinar, chamar ferramentas MCP e desafiar as conclusões um do outro. Um terceiro agente (ou um revisor humano) avalia então os argumentos e determina o melhor resultado.

Este padrão é especialmente útil para:

- **Detecção de alucinações**: Um segundo agente desafia afirmações não fundamentadas feitas pelo primeiro agente.
- **Modelagem de ameaças e revisões de segurança**: Um agente argumenta que um sistema é seguro; o outro procura vulnerabilidades.
- **Desenho de API ou requisitos**: Um agente defende um design proposto; o outro levanta objeções.
- **Verificação factual**: Ambos os agentes consultam independentemente as mesmas ferramentas MCP e cruzam as conclusões um do outro.

Ao partilharem o mesmo conjunto de ferramentas MCP, ambos os agentes operam no mesmo ambiente de informação — o que significa que qualquer desacordo reflete diferenças genuínas de raciocínio e não uma assimetria de informações.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Explicar por que os padrões multi-agente adversariais detetam erros que pipelines de um único agente não captam.
- Projetar uma arquitetura de debate onde dois agentes partilham um conjunto comum de ferramentas MCP.
- Implementar prompts de sistema "a favor" e "contra" que orientem cada agente a defender a sua posição atribuída.
- Adicionar um agente juiz (ou etapa de revisão humana) que sintetize o debate num veredicto final.
- Compreender como a partilha de ferramentas MCP funciona entre agentes concorrentes.

## Visão Geral da Arquitetura

O padrão adversarial segue este fluxo de alto nível:

```mermaid
flowchart TD
    Topic([Tema do Debate / Afirmação]) --> ForAgent
    Topic --> AgainstAgent

    subgraph SharedMCPServer["Servidor da Ferramenta MCP Partilhada"]
        WebSearch[Ferramenta de Pesquisa Web]
        CodeExec[Ferramenta de Execução de Código]
        DocReader[Opcional: Ferramenta de Leitura de Documentos]
    end

    ForAgent["Agente A\n(Argumenta A FAVOR)"] -->|Chamadas de ferramenta| SharedMCPServer
    AgainstAgent["Agente B\n(Argumenta CONTRA)"] -->|Chamadas de ferramenta| SharedMCPServer

    SharedMCPServer -->|Resultados| ForAgent
    SharedMCPServer -->|Resultados| AgainstAgent

    ForAgent -->|Argumento de abertura| Debate[(Transcrição do Debate)]
    AgainstAgent -->|Refutação| Debate

    ForAgent -->|Contra-refutação| Debate
    AgainstAgent -->|Contra-refutação| Debate

    Debate --> JudgeAgent["Agente Juiz\n(Avalia os argumentos)"]
    JudgeAgent --> Verdict([Veredicto Final & Fundamentação])

    style ForAgent fill:#c2f0c2,stroke:#333
    style AgainstAgent fill:#f9d5e5,stroke:#333
    style JudgeAgent fill:#d5e8f9,stroke:#333
    style SharedMCPServer fill:#fff9c4,stroke:#333
```
### Decisões chave de design

| Decisão | Justificação |
|----------|--------------|
| Ambos os agentes partilham um servidor MCP | Elimina a assimetria de informação — os desacordos refletem raciocínio, não acesso a dados |
| Agentes têm prompts de sistema opostos | Obriga cada agente a colocar à prova a posição do lado oposto |
| Um agente juiz sintetiza o debate | Produz uma saída única acionável sem gargalo humano |
| Múltiplas rondas de debate | Permite que cada agente responda às evidências suportadas por ferramentas do outro |

## Implementação

### Passo 1 — Servidor de Ferramentas MCP Partilhado

Comece por expor as ferramentas que ambos os agentes irão utilizar. Neste exemplo, usamos um servidor MCP Python minimalista construído com FastMCP.

<details>
<summary>Python – Servidor de Ferramentas Partilhado</summary>

```python
# shared_tools_server.py
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("debate-tools")

@mcp.tool()
async def web_search(query: str) -> str:
    """Search the web and return a short summary of the top results."""
    # Substitua pela sua API de pesquisa preferida (por exemplo, SerpAPI, Brave Search).
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.search.example.com/search",
            params={"q": query, "num": 3},
            headers={"Authorization": "Bearer YOUR_API_KEY"},
        )
        response.raise_for_status()
        results = response.json().get("results", [])
    snippets = "\n".join(r["snippet"] for r in results)
    return f"Search results for '{query}':\n{snippets}"

@mcp.tool()
async def run_python(code: str) -> str:
    """Execute a Python snippet and return stdout + stderr.

    WARNING: This is an unsafe placeholder that runs code directly on the host.
    In production, replace with a sandboxed execution environment (e.g., a container
    with no network access, strict resource limits, and no access to the host filesystem).
    """
    import subprocess, sys, textwrap
    result = subprocess.run(
        [sys.executable, "-c", textwrap.dedent(code)],
        capture_output=True, text=True, timeout=10
    )
    return result.stdout + result.stderr

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

Execute com:

```bash
python shared_tools_server.py
```

</details>

<details>
<summary>TypeScript – Servidor de Ferramentas Partilhado</summary>

```typescript
// shared-tools-server.ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { execFile } from "child_process";
import { promisify } from "util";

const execFileAsync = promisify(execFile);

const server = new McpServer({ name: "debate-tools", version: "1.0.0" });

server.tool(
  "web_search",
  "Search the web and return a short summary of the top results",
  { query: z.string() },
  async ({ query }) => {
    // Substitua pela sua API de pesquisa preferida.
    const url = `https://api.search.example.com/search?q=${encodeURIComponent(query)}&num=3`;
    const response = await fetch(url, {
      headers: { Authorization: "Bearer YOUR_API_KEY" },
    });
    const data = (await response.json()) as { results: { snippet: string }[] };
    const snippets = data.results.map((r) => r.snippet).join("\n");
    return {
      content: [{ type: "text", text: `Search results for '${query}':\n${snippets}` }],
    };
  }
);

server.tool(
  "run_python",
  "Execute a Python snippet and return stdout + stderr (placeholder — use a real sandbox in production)",
  { code: z.string() },
  async ({ code }) => {
    // AVISO: Isto executa código controlado por LLM diretamente no processo anfitrião.
    // Em produção, execute sempre dentro de uma sandbox isolada (por exemplo, um contentor
    // sem acesso à rede e com limites rigorosos de recursos).
    // Consulte a secção Considerações de Segurança para mais detalhes.
    try {
      // Passe o código como argumento direto para python3 — sem invocação de shell,
      // sem interpolação de strings, sem risco de injeção de comandos.
      const { stdout, stderr } = await execFileAsync("python3", ["-c", code], {
        timeout: 10000,
      });
      return { content: [{ type: "text", text: stdout + stderr }] };
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : String(err);
      return { content: [{ type: "text", text: `Error: ${message}` }] };
    }
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
```

Execute com:

```bash
npx ts-node shared-tools-server.ts
```

</details>

---

### Passo 2 — Prompts de Sistema para os Agentes

Cada agente recebe um prompt de sistema que o mantém na sua posição atribuída. O importante é que ambos saibam que estão num debate e que *devem* usar ferramentas para fundamentar as suas afirmações.

<details>
<summary>Python – Prompts de Sistema</summary>

```python
# prompts.py

FOR_SYSTEM_PROMPT = """You are Agent A in a structured debate.
Your role is to argue *in favour* of the proposition given to you.
Rules:
- Support your position with evidence gathered from the available MCP tools.
- Call the web_search tool to find real supporting data.
- Call the run_python tool to verify quantitative claims with code.
- When your opponent makes a claim, challenge it specifically and with evidence.
- Do not concede your position unless your opponent provides irrefutable evidence.
- Keep each turn concise (≤ 200 words)."""

AGAINST_SYSTEM_PROMPT = """You are Agent B in a structured debate.
Your role is to argue *against* the proposition given to you.
Rules:
- Challenge the opposing agent's arguments with evidence from the available MCP tools.
- Call the web_search tool to find counter-evidence.
- Call the run_python tool to verify or disprove quantitative claims with code.
- Point out logical fallacies, missing context, or unsupported assertions.
- Do not concede your position unless the evidence is irrefutable.
- Keep each turn concise (≤ 200 words)."""

JUDGE_SYSTEM_PROMPT = """You are an impartial judge evaluating a structured debate.
Your task:
1. Read the full debate transcript.
2. Identify the strongest evidence-backed arguments on each side.
3. Note any claims that were left unchallenged.
4. Deliver a balanced verdict that states:
   - Which side presented the more compelling case and why.
   - Key caveats or nuances that neither side addressed adequately.
   - A confidence score (0–100) for the winning position."""
```

</details>

---

### Passo 3 — Orquestrador do Debate

O orquestrador cria ambos os agentes, gere as turnos do debate e depois envia a transcrição completa ao juiz.

<details>
<summary>Python – Orquestrador do Debate</summary>

```python
# debate_orchestrator.py
import asyncio
from anthropic import AsyncAnthropic
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from prompts import FOR_SYSTEM_PROMPT, AGAINST_SYSTEM_PROMPT, JUDGE_SYSTEM_PROMPT

client = AsyncAnthropic()

NUM_ROUNDS = 3  # Número de rondas de troca de ideias


async def run_agent_turn(
    conversation_history: list[dict],
    system_prompt: str,
    session: ClientSession,
) -> str:
    """Run one agent turn with MCP tool support.

    Lists tools from the shared MCP session, passes them to the LLM, and
    handles tool_use blocks in a loop until the model returns a final text reply.
    """
    # Obter a lista atual de ferramentas do servidor MCP partilhado.
    tools_result = await session.list_tools()
    tools = [
        {
            "name": t.name,
            "description": t.description or "",
            "input_schema": t.inputSchema,
        }
        for t in tools_result.tools
    ]

    messages = list(conversation_history)
    while True:
        response = await client.messages.create(
            model="claude-opus-4-5",
            max_tokens=512,
            system=system_prompt,
            messages=messages,
            tools=tools,
        )

        # Recolher qualquer texto produzido pelo modelo.
        text_blocks = [b for b in response.content if b.type == "text"]

        # Se o modelo tiver terminado (sem chamadas a ferramentas), retornar a sua resposta em texto.
        tool_uses = [b for b in response.content if b.type == "tool_use"]
        if not tool_uses:
            return text_blocks[0].text if text_blocks else ""

        # Registar a vez do assistente (pode misturar blocos de texto + utilização de ferramenta).
        messages.append({"role": "assistant", "content": response.content})

        # Executar cada chamada de ferramenta e recolher os resultados.
        tool_results = []
        for tool_use in tool_uses:
            result = await session.call_tool(tool_use.name, tool_use.input)
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": result.content[0].text if result.content else "",
                }
            )

        # Alimentar os resultados das ferramentas de volta para o modelo.
        messages.append({"role": "user", "content": tool_results})


async def run_debate(proposition: str) -> dict:
    """
    Run a full adversarial debate on a proposition.

    Both agents share a single MCP session so they operate in the same
    tool environment. Returns a dictionary with the transcript and verdict.
    """
    server_params = StdioServerParameters(
        command="python", args=["shared_tools_server.py"]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            transcript: list[dict] = []

            # Iniciar o debate com a proposta.
            opening_message = {"role": "user", "content": f"Proposition: {proposition}"}

            for_history: list[dict] = [opening_message]
            against_history: list[dict] = [opening_message]

            for round_num in range(1, NUM_ROUNDS + 1):
                print(f"\n--- Round {round_num} ---")

                # O Agente A argumenta A FAVOR.
                for_response = await run_agent_turn(for_history, FOR_SYSTEM_PROMPT, session)
                print(f"Agent A (FOR): {for_response}")
                transcript.append({"round": round_num, "agent": "FOR", "text": for_response})

                # Partilhar o argumento do Agente A com o Agente B.
                for_history.append({"role": "assistant", "content": for_response})
                against_history.append({"role": "user", "content": f"Opponent argued: {for_response}"})

                # O Agente B argumenta CONTRA.
                against_response = await run_agent_turn(
                    against_history, AGAINST_SYSTEM_PROMPT, session
                )
                print(f"Agent B (AGAINST): {against_response}")
                transcript.append({"round": round_num, "agent": "AGAINST", "text": against_response})

                # Partilhar o argumento do Agente B com o Agente A para a ronda seguinte.
                against_history.append({"role": "assistant", "content": against_response})
                for_history.append({"role": "user", "content": f"Opponent argued: {against_response}"})

            # Construir o resumo da transcrição para o juiz.
            transcript_text = "\n\n".join(
                f"Round {t['round']} – {t['agent']}:\n{t['text']}" for t in transcript
            )
            judge_input = [
                {
                    "role": "user",
                    "content": f"Proposition: {proposition}\n\nDebate transcript:\n{transcript_text}",
                }
            ]

            # O juiz avalia o debate.
            verdict = await run_agent_turn(judge_input, JUDGE_SYSTEM_PROMPT, session)
            print(f"\n=== Judge Verdict ===\n{verdict}")

            return {"transcript": transcript, "verdict": verdict}


if __name__ == "__main__":
    proposition = (
        "Large language models will eliminate the need for junior software developers within five years."
    )
    result = asyncio.run(run_debate(proposition))
```

</details>

<details>
<summary>TypeScript – Orquestrador do Debate</summary>

```typescript
// debate-orchestrator.ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const FOR_SYSTEM_PROMPT = `You are Agent A in a structured debate.
Your role is to argue *in favour* of the proposition given to you.
Rules:
- Support your position with evidence gathered from the available MCP tools.
- Call the web_search tool to find real supporting data.
- When your opponent makes a claim, challenge it specifically and with evidence.
- Keep each turn concise (≤ 200 words).`;

const AGAINST_SYSTEM_PROMPT = `You are Agent B in a structured debate.
Your role is to argue *against* the proposition given to you.
Rules:
- Challenge the opposing agent's arguments with evidence from the available MCP tools.
- Call the web_search tool to find counter-evidence.
- Point out logical fallacies, missing context, or unsupported assertions.
- Keep each turn concise (≤ 200 words).`;

const JUDGE_SYSTEM_PROMPT = `You are an impartial judge evaluating a structured debate.
Deliver a verdict with:
1. Which side presented the more compelling case and why.
2. Key caveats or nuances that neither side addressed.
3. A confidence score (0–100) for the winning position.`;

type Message = { role: "user" | "assistant"; content: string };

type DebateTurn = { round: number; agent: "FOR" | "AGAINST"; text: string };

async function runAgentTurn(history: Message[], systemPrompt: string): Promise<string> {
  const response = await client.messages.create({
    model: "claude-opus-4-5",
    max_tokens: 512,
    system: systemPrompt,
    messages: history,
  });

  const text = response.content
    .filter((block) => block.type === "text")
    .map((block) => block.text)
    .join("\n")
    .trim();

  if (!text) {
    const blockTypes = response.content.map((block) => block.type).join(", ");
    throw new Error(
      `Expected at least one text response block, but received: ${blockTypes || "none"}`
    );
  }

  return text;
}

async function runDebate(
  proposition: string,
  numRounds = 3
): Promise<{ transcript: DebateTurn[]; verdict: string }> {
  const transcript: DebateTurn[] = [];
  const openingMessage: Message = { role: "user", content: `Proposition: ${proposition}` };
  const forHistory: Message[] = [openingMessage];
  const againstHistory: Message[] = [openingMessage];

  for (let round = 1; round <= numRounds; round++) {
    console.log(`\n--- Round ${round} ---`);

    // Agente A (A FAVOR)
    const forResponse = await runAgentTurn(forHistory, FOR_SYSTEM_PROMPT);
    console.log(`Agent A (FOR): ${forResponse}`);
    transcript.push({ round, agent: "FOR", text: forResponse });
    forHistory.push({ role: "assistant", content: forResponse });
    againstHistory.push({ role: "user", content: `Opponent argued: ${forResponse}` });

    // Agente B (CONTRA)
    const againstResponse = await runAgentTurn(againstHistory, AGAINST_SYSTEM_PROMPT);
    console.log(`Agent B (AGAINST): ${againstResponse}`);
    transcript.push({ round, agent: "AGAINST", text: againstResponse });
    againstHistory.push({ role: "assistant", content: againstResponse });
    forHistory.push({ role: "user", content: `Opponent argued: ${againstResponse}` });
  }

  // Juiz
  const transcriptText = transcript
    .map((t) => `Round ${t.round} – ${t.agent}:\n${t.text}`)
    .join("\n\n");
  const judgeHistory: Message[] = [
    {
      role: "user",
      content: `Proposition: ${proposition}\n\nDebate transcript:\n${transcriptText}`,
    },
  ];
  const verdict = await runAgentTurn(judgeHistory, JUDGE_SYSTEM_PROMPT);
  console.log(`\n=== Judge Verdict ===\n${verdict}`);

  return { transcript, verdict };
}

// Executar
const proposition =
  "Large language models will eliminate the need for junior software developers within five years.";
runDebate(proposition).catch(console.error);
```

</details>

<details>
<summary>C# – Orquestrador do Debate</summary>

```csharp
// DebateOrchestrator.cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Anthropic.SDK;
using Anthropic.SDK.Messaging;

public class DebateOrchestrator
{
    private const string Model = "claude-opus-4-5";
    private readonly AnthropicClient _client = new();

    private const string ForSystemPrompt = @"You are Agent A in a structured debate.
Your role is to argue *in favour* of the proposition given to you.
Rules:
- Support your position with evidence.
- Challenge your opponent's claims specifically.
- Keep each turn concise (≤ 200 words).";

    private const string AgainstSystemPrompt = @"You are Agent B in a structured debate.
Your role is to argue *against* the proposition given to you.
Rules:
- Challenge the opposing agent's arguments with evidence.
- Point out logical fallacies or unsupported assertions.
- Keep each turn concise (≤ 200 words).";

    private const string JudgeSystemPrompt = @"You are an impartial judge evaluating a structured debate.
Deliver a verdict with:
1. Which side presented the more compelling case and why.
2. Key caveats neither side addressed.
3. A confidence score (0–100) for the winning position.";

    private record DebateTurn(int Round, string Agent, string Text);

    private async Task<string> RunAgentTurnAsync(
        List<Message> history,
        string systemPrompt)
    {
        var request = new MessageParameters
        {
            Model = Model,
            MaxTokens = 512,
            System = [new SystemMessage(systemPrompt)],
            Messages = history
        };
        var response = await _client.Messages.GetClaudeMessageAsync(request);
        return response.Content.OfType<TextContent>().FirstOrDefault()?.Text ?? string.Empty;
    }

    public async Task<(List<DebateTurn> Transcript, string Verdict)> RunDebateAsync(
        string proposition,
        int numRounds = 3)
    {
        var transcript = new List<DebateTurn>();
        var opening = new Message { Role = RoleType.User, Content = $"Proposition: {proposition}" };

        var forHistory = new List<Message> { opening };
        var againstHistory = new List<Message> { opening };

        for (int round = 1; round <= numRounds; round++)
        {
            Console.WriteLine($"\n--- Round {round} ---");

            // Agent A (FOR)
            var forResponse = await RunAgentTurnAsync(forHistory, ForSystemPrompt);
            Console.WriteLine($"Agent A (FOR): {forResponse}");
            transcript.Add(new DebateTurn(round, "FOR", forResponse));
            forHistory.Add(new Message { Role = RoleType.Assistant, Content = forResponse });
            againstHistory.Add(new Message { Role = RoleType.User, Content = $"Opponent argued: {forResponse}" });

            // Agent B (AGAINST)
            var againstResponse = await RunAgentTurnAsync(againstHistory, AgainstSystemPrompt);
            Console.WriteLine($"Agent B (AGAINST): {againstResponse}");
            transcript.Add(new DebateTurn(round, "AGAINST", againstResponse));
            againstHistory.Add(new Message { Role = RoleType.Assistant, Content = againstResponse });
            forHistory.Add(new Message { Role = RoleType.User, Content = $"Opponent argued: {againstResponse}" });
        }

        // Judge
        var transcriptText = string.Join("\n\n",
            transcript.Select(t => $"Round {t.Round} – {t.Agent}:\n{t.Text}"));
        var judgeHistory = new List<Message>
        {
            new() { Role = RoleType.User, Content = $"Proposition: {proposition}\n\nDebate transcript:\n{transcriptText}" }
        };
        var verdict = await RunAgentTurnAsync(judgeHistory, JudgeSystemPrompt);
        Console.WriteLine($"\n=== Judge Verdict ===\n{verdict}");

        return (transcript, verdict);
    }

    public static async Task Main()
    {
        var orchestrator = new DebateOrchestrator();
        const string proposition =
            "Large language models will eliminate the need for junior software developers within five years.";
        await orchestrator.RunDebateAsync(proposition);
    }
}
```

</details>

---

### Passo 4 — Ligação das Ferramentas MCP aos Agentes

O orquestrador Python acima já mostra a implementação completa ligada ao MCP. O padrão chave é:

- **Uma sessão partilhada**: `run_debate` abre uma única `ClientSession` que é passada para cada chamada de `run_agent_turn`, para que ambos os agentes e o juiz operem no mesmo ambiente de ferramentas.
- **Listagem de ferramentas por turno**: `run_agent_turn` chama `session.list_tools()` para obter as definições atuais de ferramentas e encaminha-as para o LLM como o parâmetro `tools`.
- **Loop de uso de ferramentas**: Quando o modelo retorna blocos `tool_use`, `run_agent_turn` chama `session.call_tool()` para cada um e alimenta os resultados ao modelo, repetindo até o modelo produzir uma resposta final em texto.

Consulte [03-GettingStarted/02-client](../../../../03-GettingStarted/02-client/solution) para exemplos completos de cliente MCP em cada linguagem.

---

## Casos Práticos de Utilização

| Caso de Uso | Agente A FAVOR | Agente CONTRA | Saída do Juiz |
|-------------|----------------|---------------|---------------|
| **Modelagem de ameaças** | "Este endpoint API é seguro" | "Aqui estão cinco vetores de ataque" | Lista priorizada de riscos |
| **Revisão de desenho de API** | "Este desenho é ótimo" | "Estas compensações são problemáticas" | Desenho recomendado com ressalvas |
| **Verificação factual** | "A afirmação X é suportada por evidências" | "A evidência Y contradiz a afirmação X" | Veredicto com classificação de confiança |
| **Seleção tecnológica** | "Escolha o framework A" | "O framework B é melhor por estas razões" | Matriz de decisão com recomendação |

---

## Considerações de Segurança

Ao executar agentes adversariais em produção, tenha em conta:

- **Execução isolada de código**: A ferramenta `run_python` deve executar num ambiente isolado (p.e., um contentor sem acesso à rede e com limites de recursos). Nunca execute código gerado pelo LLM diretamente no e hospedeiro.
- **Validação de chamadas de ferramenta**: Valide todas as entradas para as ferramentas antes da execução. Ambos os agentes partilham o mesmo servidor de ferramentas, de modo que um prompt malicioso injetado no debate pode tentar utilizar indevidamente as ferramentas.
- **Limitação de taxa**: Implemente limites de chamada de ferramentas por agente para evitar loops descontrolados.
- **Registo de auditoria**: Registe todas as chamadas e resultados das ferramentas para que possa rever que evidências cada agente usou para chegar às suas conclusões.
- **Intervenção humana**: Para decisões de alto risco, encaminhe o veredicto do juiz para um revisor humano antes de executar ações.

Consulte [02-Security](../../../../02-Security) para um guia abrangente das melhores práticas de segurança MCP.

---

## Exercício

Projete um pipeline MCP adversarial para um dos seguintes cenários:

1. **Revisão de código**: O Agente A defende um pull request; o Agente B procura bugs, problemas de segurança e de estilo. O juiz resume as principais questões.
2. **Decisão arquitetónica**: O Agente A propõe microserviços; o Agente B defende um monólito. O juiz produz uma matriz de decisão.
3. **Moderação de conteúdo**: O Agente A argumenta que um conteúdo é seguro para publicação; o Agente B encontra violações de política. O juiz atribui uma pontuação de risco.

Para cada cenário:

- Defina os prompts de sistema para ambos os agentes e para o juiz.
- Identifique que ferramentas MCP cada agente necessita.
- Esboce o fluxo de mensagens (argumento inicial → réplica → contraréplica → veredicto).
- Descreva como validaria o veredicto do juiz antes de agir sobre ele.

---

## Pontos-chave

- Padrões multi-agente adversariais usam prompts de sistema opostos para forçar os agentes a testar o raciocínio um do outro.
- Partilhar um único servidor de ferramentas MCP assegura que ambos os agentes trabalham com a mesma informação, pelo que os desacordos são sobre raciocínio, não acesso a dados.
- Um agente juiz sintetiza o debate num veredicto acionável sem exigir um gargalo humano para cada decisão.
- Este padrão é especialmente poderoso para deteção de alucinações, modelagem de ameaças, verificação factual e revisões de design.
- Execução segura das ferramentas e registos robustos são essenciais ao executar agentes adversariais em produção.

---

## Próximos passos

- [5.1 Integração MCP](../mcp-integration/README.md)
- [5.8 Segurança](../mcp-security/README.md)
- [5.5 Routing](../mcp-routing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informação crítica, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->