# 對抗式多智能體推理與 MCP

多智能體辯論模式使用兩個或以上持相反立場的智能體，產生比單一智能體更可靠且校準良好的輸出。

## 簡介

在本課程中，我們將探討<strong>對抗式多智能體模式</strong>——一種由兩個 AI 智能體被指派持有相反主張，需進行推理、調用 MCP 工具，並相互挑戰彼此結論的技術。隨後第三方智能體（或人類審核者）評估論點並決定最佳結果。

此模式尤其適用於：

- <strong>幻覺檢測</strong>：第二個智能體質疑第一個智能體做出的無根據主張。
- <strong>威脅建模與安全審查</strong>：一方主張系統安全；另一方尋找漏洞。
- **API 或需求設計**：一方為提案設計辯護；另一方提出異議。
- <strong>事實驗證</strong>：雙方智能體獨立使用相同 MCP 工具並交叉核對對方結論。

共用相同的 MCP 工具集，讓雙方智能體都在同一資訊環境下運作——這代表任何分歧都是推理差異，而非資訊不對稱。

## 學習目標

完成本課程後，你將能：

- 解釋為何對抗式多智能體模式能發現單一智能體流程遺漏的錯誤。
- 設計一個兩個智能體共用 MCP 工具集的辯論架構。
- 實作支持「贊成」與「反對」立場的系統提示，引導每個智能體論證其指定立場。
- 新增一個裁判智能體（或人工審查步驟），將辯論匯總為最終裁決。
- 理解 MCP 工具共享於並行智能體的運作方式。

## 架構總覽

對抗式模式遵循以下高階流程：

```mermaid
flowchart TD
    Topic([辯論主題 / 主張]) --> ForAgent
    Topic --> AgainstAgent

    subgraph SharedMCPServer["共享 MCP 工具服務器"]
        WebSearch[網絡搜索工具]
        CodeExec[代碼執行工具]
        DocReader[可選：文檔閱讀工具]
    end

    ForAgent["代理 A\n(支持主張)"] -->|工具調用| SharedMCPServer
    AgainstAgent["代理 B\n(反對主張)"] -->|工具調用| SharedMCPServer

    SharedMCPServer -->|結果| ForAgent
    SharedMCPServer -->|結果| AgainstAgent

    ForAgent -->|開場陳詞| Debate[(辯論記錄)]
    AgainstAgent -->|反駁| Debate

    ForAgent -->|反駁回應| Debate
    AgainstAgent -->|反駁回應| Debate

    Debate --> JudgeAgent["裁判代理\n(評估論點)"]
    JudgeAgent --> Verdict([最終裁決及理由])

    style ForAgent fill:#c2f0c2,stroke:#333
    style AgainstAgent fill:#f9d5e5,stroke:#333
    style JudgeAgent fill:#d5e8f9,stroke:#333
    style SharedMCPServer fill:#fff9c4,stroke:#333
```
### 主要設計決策

| 決策 | 理由 |
|----------|-----------|
| 雙方智能體共用 MCP 伺服器 | 消除資訊不對稱——分歧反映推理，而非資料存取差異 |
| 智能體持相反系統提示 | 促使雙方嚴格檢驗對方立場 |
| 由裁判智能體綜合辯論結果 | 生成單一可執行輸出，無需人力瓶頸 |
| 多輪辯論 | 允許雙方針對對方工具支持證據回應 |

## 實作

### 步驟 1 — 共享 MCP 工具伺服器

先開放雙方智能體皆可調用的工具。本例使用以 FastMCP 建構的簡易 Python MCP 伺服器。

<details>
<summary>Python – 共享工具伺服器</summary>

```python
# shared_tools_server.py
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("debate-tools")

@mcp.tool()
async def web_search(query: str) -> str:
    """Search the web and return a short summary of the top results."""
    # 換成你偏好的搜尋 API（例如 SerpAPI，Brave Search）。
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

執行方式：

```bash
python shared_tools_server.py
```

</details>

<details>
<summary>TypeScript – 共享工具伺服器</summary>

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
    // 換成你偏好的搜尋 API。
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
    // 警告：這會直接在主機程序上執行由 LLM 控制的程式碼。
    // 在生產環境中，請務必在隔離的沙盒內運行（例如容器
    // 不允許網絡訪問並有嚴格的資源限制）。
    // 詳情請參閱安全性考量部分。
    try {
      // 以直接參數形式傳遞程式碼給 python3 — 不啟動 shell，
      // 不使用字串插值，沒有命令注入風險。
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

執行方式：

```bash
npx ts-node shared-tools-server.ts
```

</details>

---

### 步驟 2 — 智能體系統提示

每個智能體收到鎖定其指定立場的系統提示。關鍵是雙方都知道自己正在辯論，且<strong>必須</strong>利用工具支持其主張。

<details>
<summary>Python – 系統提示</summary>

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

### 步驟 3 — 辯論協調器

協調器建立雙方智能體，管理辯論回合，最後將完整對話傳給裁判。

<details>
<summary>Python – 辯論協調器</summary>

```python
# debate_orchestrator.py
import asyncio
from anthropic import AsyncAnthropic
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from prompts import FOR_SYSTEM_PROMPT, AGAINST_SYSTEM_PROMPT, JUDGE_SYSTEM_PROMPT

client = AsyncAnthropic()

NUM_ROUNDS = 3  # 來回交流輪數


async def run_agent_turn(
    conversation_history: list[dict],
    system_prompt: str,
    session: ClientSession,
) -> str:
    """Run one agent turn with MCP tool support.

    Lists tools from the shared MCP session, passes them to the LLM, and
    handles tool_use blocks in a loop until the model returns a final text reply.
    """
    # 從共享 MCP 伺服器取得當前工具清單。
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

        # 收集模型產生的任何文本。
        text_blocks = [b for b in response.content if b.type == "text"]

        # 如果模型結束（無工具調用），回傳其文本回覆。
        tool_uses = [b for b in response.content if b.type == "tool_use"]
        if not tool_uses:
            return text_blocks[0].text if text_blocks else ""

        # 記錄助理回合（可能混合文本 + 工具使用區塊）。
        messages.append({"role": "assistant", "content": response.content})

        # 執行每個工具調用並收集結果。
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

        # 將工具結果回饋給模型。
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

            # 以命題作為辯論種子。
            opening_message = {"role": "user", "content": f"Proposition: {proposition}"}

            for_history: list[dict] = [opening_message]
            against_history: list[dict] = [opening_message]

            for round_num in range(1, NUM_ROUNDS + 1):
                print(f"\n--- Round {round_num} ---")

                # 代理 A 支持論點。
                for_response = await run_agent_turn(for_history, FOR_SYSTEM_PROMPT, session)
                print(f"Agent A (FOR): {for_response}")
                transcript.append({"round": round_num, "agent": "FOR", "text": for_response})

                # 將代理 A 的論點分享給代理 B。
                for_history.append({"role": "assistant", "content": for_response})
                against_history.append({"role": "user", "content": f"Opponent argued: {for_response}"})

                # 代理 B 反對論點。
                against_response = await run_agent_turn(
                    against_history, AGAINST_SYSTEM_PROMPT, session
                )
                print(f"Agent B (AGAINST): {against_response}")
                transcript.append({"round": round_num, "agent": "AGAINST", "text": against_response})

                # 將代理 B 的論點分享給代理 A 進入下一輪。
                against_history.append({"role": "assistant", "content": against_response})
                for_history.append({"role": "user", "content": f"Opponent argued: {against_response}"})

            # 建立法官用的記錄摘要。
            transcript_text = "\n\n".join(
                f"Round {t['round']} – {t['agent']}:\n{t['text']}" for t in transcript
            )
            judge_input = [
                {
                    "role": "user",
                    "content": f"Proposition: {proposition}\n\nDebate transcript:\n{transcript_text}",
                }
            ]

            # 法官評價辯論。
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
<summary>TypeScript – 辯論協調器</summary>

```typescript
// 辯論統籌者.ts
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

    // 代理人 A（支持）
    const forResponse = await runAgentTurn(forHistory, FOR_SYSTEM_PROMPT);
    console.log(`Agent A (FOR): ${forResponse}`);
    transcript.push({ round, agent: "FOR", text: forResponse });
    forHistory.push({ role: "assistant", content: forResponse });
    againstHistory.push({ role: "user", content: `Opponent argued: ${forResponse}` });

    // 代理人 B（反對）
    const againstResponse = await runAgentTurn(againstHistory, AGAINST_SYSTEM_PROMPT);
    console.log(`Agent B (AGAINST): ${againstResponse}`);
    transcript.push({ round, agent: "AGAINST", text: againstResponse });
    againstHistory.push({ role: "assistant", content: againstResponse });
    forHistory.push({ role: "user", content: `Opponent argued: ${againstResponse}` });
  }

  // 法官
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

// 執行
const proposition =
  "Large language models will eliminate the need for junior software developers within five years.";
runDebate(proposition).catch(console.error);
```

</details>

<details>
<summary>C# – 辯論協調器</summary>

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

### 步驟 4 — 將 MCP 工具連接至智能體

上述 Python 協調器已展示完整的 MCP 連線實作。關鍵模式為：

- <strong>共用一個會話</strong>：`run_debate` 開啟單一 `ClientSession`，並將其傳給各個 `run_agent_turn`，使雙方智能體與裁判都在同一工具環境中操作。
- <strong>每回合取得工具清單</strong>：`run_agent_turn` 呼叫 `session.list_tools()` 取得目前的工具定義，並作為 `tools` 參數傳給 LLM。
- <strong>工具使用迴圈</strong>：模型回傳 `tool_use` 區塊時，`run_agent_turn` 依序呼叫 `session.call_tool()`，並將結果回饋給模型，如此重複直到模型輸出最終文字回應。

各語言完整 MCP 用戶端範例請參考 [03-GettingStarted/02-client](../../../../03-GettingStarted/02-client/solution)。

---

## 實務應用場景

| 場景 | 贊成智能體 | 反對智能體 | 裁判輸出 |
|----------|-----------|---------------|--------------|
| <strong>威脅建模</strong> | 「此 API 端點安全」 | 「這裡有五種攻擊向量」 | 風險優先排序清單 |
| **API 設計審查** | 「此設計最佳」 | 「這些取捨有問題」 | 帶附註的推薦設計 |
| <strong>事實驗證</strong> | 「主張 X 有證據支持」 | 「證據 Y 與主張 X 矛盾」 | 信心水準裁決 |
| <strong>技術選擇</strong> | 「選擇框架 A」 | 「框架 B 有此優勢」 | 含建議的決策矩陣 |

---

## 安全考量

在生產環境運行對抗式智能體時，請注意：

- <strong>沙盒代碼執行</strong>：`run_python` 工具必須在隔離環境執行（例如無網路且有限資源的容器）。切勿直接在主機執行不受信任的 LLM 生成代碼。
- <strong>工具調用驗證</strong>：所有工具輸入需先驗證。雙方智能體共用工具伺服器，惡意提示可能嘗試濫用工具。
- <strong>速率限制</strong>：對每個智能體的工具呼叫實施速率限制，避免無限循環。
- <strong>審計紀錄</strong>：記錄每次工具呼叫與結果，方便回溯每個智能體的證據來源。
- <strong>人機介入流程</strong>：高風險決策時，經裁判輸出結果需經人工審查後方行動。

詳情參見 [02-Security](../../../../02-Security) 中的全面 MCP 安全實務指南。

---

## 練習題

為下列情境設計對抗式 MCP 流程：

1. <strong>程式碼審查</strong>：智能體 A 持護拉取請求；智能體 B 尋找錯誤、安全與風格問題。裁判總結主要問題。
2. <strong>架構決策</strong>：智能體 A 提議微服務；智能體 B 擁護單體架構。裁判輸出決策矩陣。
3. <strong>內容審核</strong>：智能體 A 主張內容安全可發布；智能體 B 發現政策違規。裁判賦予風險評分。

每項情境請：

- 定義雙方智能體及裁判的系統提示。
- 指明各智能體需用的 MCP 工具。
- 擬定訊息流程（開場論點 → 反駁 → 二度反駁 → 裁決）。
- 描述如何在採取行動前驗證裁判裁決。

---

## 重要重點

- 對抗式多智能體模式透過相反系統提示，逼使智能體嚴格檢驗彼此推理。
- 共用單一 MCP 工具伺服器確保雙方基於相同資訊，分歧即為推理差異，而非資料不對稱。
- 裁判智能體綜合辯論，生成可執行裁決，避免每次決策皆需人工介入瓶頸。
- 此模式對幻覺檢測、威脅建模、事實驗證與設計審核尤其有力。
- 安全執行工具與完整日誌記錄為生產環境運行對抗式智能體的關鍵。

---

## 接下來的內容

- [5.1 MCP Integration](../mcp-integration/README.md)
- [5.8 Security](../mcp-security/README.md)
- [5.5 Routing](../mcp-routing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。如需關鍵資訊，建議採用專業人工翻譯。我們對因使用本翻譯引起的任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->