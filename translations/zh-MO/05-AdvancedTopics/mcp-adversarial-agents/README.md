# 對抗式多智能體推理與 MCP

多智能體辯論模式使用兩個或以上持對立立場的智能體，產生比單一智能體更可靠且校準良好的輸出結果。

## 介紹

在本課程中，我們探討 <strong>對抗式多智能體模式</strong> — 這種技術會指定兩個 AI 智能體在一個主題上持相反立場，並且必須推理、調用 MCP 工具，並互相挑戰對方的結論。第三個智能體（或人類審閱者）隨後評估論點並決定最佳結果。

此模式特別適用於：

- <strong>幻覺偵測</strong>：第二個智能體挑戰第一個智能體未經證實的聲稱。
- <strong>威脅建模與安全審查</strong>：一方主張系統安全；另一方尋找漏洞。
- **API 或需求設計**：一方為提出的設計辯護；另一方提出異議。
- <strong>事實驗證</strong>：雙方智能體獨立查詢相同 MCP 工具，交叉檢驗彼此的結論。

透過共享相同的 MCP 工具集，雙方智能體在相同的資訊環境中運作 — 因此任何分歧反映的是真實的推理差異，而非資訊不對稱。

## 學習目標

完成本課程後，你將能夠：

- 解釋為何對抗式多智能體模式能比單一智能體管線更有效捕捉錯誤。
- 設計兩個智能體共享共同 MCP 工具集的辯論架構。
- 實作「支持」與「反對」的系統提示，引導各智能體堅持其分配的立場。
- 增加評判智能體（或人類審閱步驟）綜合辯論成最終裁決。
- 了解 MCP 工具共享如何在多智能體並行運行中生效。

## 架構概述

對抗模式遵循此高階流程：

```mermaid
flowchart TD
    Topic([辯論主題 / 主張]) --> ForAgent
    Topic --> AgainstAgent

    subgraph SharedMCPServer["共享 MCP 工具伺服器"]
        WebSearch[網絡搜尋工具]
        CodeExec[代碼執行工具]
        DocReader[選擇性：文件閱讀工具]
    end

    ForAgent["代理人 A\n(支持主張)"] -->|工具調用| SharedMCPServer
    AgainstAgent["代理人 B\n(反對主張)"] -->|工具調用| SharedMCPServer

    SharedMCPServer -->|結果| ForAgent
    SharedMCPServer -->|結果| AgainstAgent

    ForAgent -->|開場辯論| Debate[(辯論記錄)]
    AgainstAgent -->|反駁| Debate

    ForAgent -->|反反駁| Debate
    AgainstAgent -->|反反駁| Debate

    Debate --> JudgeAgent["裁判代理人\n(評估論點)"]
    JudgeAgent --> Verdict([最終裁決及理由])

    style ForAgent fill:#c2f0c2,stroke:#333
    style AgainstAgent fill:#f9d5e5,stroke:#333
    style JudgeAgent fill:#d5e8f9,stroke:#333
    style SharedMCPServer fill:#fff9c4,stroke:#333
```
### 主要設計決策

| 決策 | 原因 |
|----------|-----------|
| 雙方智能體共享一台 MCP 伺服器 | 消除資訊不對稱 — 分歧反映推理差異，非資料取得差異 |
| 智能體擁有對立的系統提示 | 強迫各智能體嚴格檢驗對方的立場 |
| 評判智能體綜合辯論結果 | 產出單一可行動的結論，避免人為瓶頸 |
| 多輪辯論 | 允許智能體回應對手基於工具的證據 |

## 實作

### 步驟 1 — 共享 MCP 工具伺服器

先公開雙方智能體將調用的工具。在此示範中，我們使用 FastMCP 建立的最小 Python MCP 伺服器。

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
    # 請替換成您首選的搜尋 API（例如 SerpAPI、Brave Search）。
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
    // 請替換為您偏好的搜尋 API。
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
    // 警告：此操作會直接在主機程序上執行由 LLM 控制的代碼。
    // 在生產環境中，務必在隔離沙盒內運行（例如，一個沒有網絡訪問且資源限制嚴格的容器）。
    // 具有無網絡訪問和嚴格資源限制的容器）。
    // 詳情請參閱安全考量部分。
    try {
      // 將代碼作為直接參數傳給 python3 — 不通過 shell 調用，
      // 不進行字串插值，不存在指令注入風險。
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

每個智能體接收系統提示，將其鎖定在分配的立場。重點是雙方智能體知道自己在辯論，必須使用工具來支持其主張。

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

協調器建立雙方智能體，管理辯論回合，然後將完整對話文本傳給評判。

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

NUM_ROUNDS = 3  # 反覆交鋒的回合數量


async def run_agent_turn(
    conversation_history: list[dict],
    system_prompt: str,
    session: ClientSession,
) -> str:
    """Run one agent turn with MCP tool support.

    Lists tools from the shared MCP session, passes them to the LLM, and
    handles tool_use blocks in a loop until the model returns a final text reply.
    """
    # 從共享的 MCP 伺服器擷取目前的工具清單。
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

        # 收集模型產生的任何文字。
        text_blocks = [b for b in response.content if b.type == "text"]

        # 如果模型完成（無工具呼叫），回傳其文字回覆。
        tool_uses = [b for b in response.content if b.type == "tool_use"]
        if not tool_uses:
            return text_blocks[0].text if text_blocks else ""

        # 紀錄助理回合（可能混合文字 + 工具使用區塊）。
        messages.append({"role": "assistant", "content": response.content})

        # 執行每個工具呼叫並收集結果。
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

            # 以命題作為辯論的開端。
            opening_message = {"role": "user", "content": f"Proposition: {proposition}"}

            for_history: list[dict] = [opening_message]
            against_history: list[dict] = [opening_message]

            for round_num in range(1, NUM_ROUNDS + 1):
                print(f"\n--- Round {round_num} ---")

                # 代理人 A 支持論點。
                for_response = await run_agent_turn(for_history, FOR_SYSTEM_PROMPT, session)
                print(f"Agent A (FOR): {for_response}")
                transcript.append({"round": round_num, "agent": "FOR", "text": for_response})

                # 將代理人 A 的論點分享給代理人 B。
                for_history.append({"role": "assistant", "content": for_response})
                against_history.append({"role": "user", "content": f"Opponent argued: {for_response}"})

                # 代理人 B 反對論點。
                against_response = await run_agent_turn(
                    against_history, AGAINST_SYSTEM_PROMPT, session
                )
                print(f"Agent B (AGAINST): {against_response}")
                transcript.append({"round": round_num, "agent": "AGAINST", "text": against_response})

                # 將代理人 B 的論點分享給代理人 A 以進入下一回合。
                against_history.append({"role": "assistant", "content": against_response})
                for_history.append({"role": "user", "content": f"Opponent argued: {against_response}"})

            # 為評判構建文字紀錄摘要。
            transcript_text = "\n\n".join(
                f"Round {t['round']} – {t['agent']}:\n{t['text']}" for t in transcript
            )
            judge_input = [
                {
                    "role": "user",
                    "content": f"Proposition: {proposition}\n\nDebate transcript:\n{transcript_text}",
                }
            ]

            # 評判評估辯論。
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
// 辯論指揮者.ts
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

    // 代理人A（支持）
    const forResponse = await runAgentTurn(forHistory, FOR_SYSTEM_PROMPT);
    console.log(`Agent A (FOR): ${forResponse}`);
    transcript.push({ round, agent: "FOR", text: forResponse });
    forHistory.push({ role: "assistant", content: forResponse });
    againstHistory.push({ role: "user", content: `Opponent argued: ${forResponse}` });

    // 代理人B（反對）
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

### 步驟 4 — 通過 MCP 工具連接智能體

上方 Python 協調器示例展示完整的 MCP 連接實作。關鍵模式是：

- <strong>共享單一會話</strong>：`run_debate` 開啟一個 `ClientSession` 並傳入每個 `run_agent_turn` 呼叫，讓雙方智能體以及評判在相同工具環境運行。
- <strong>每回合工具列表</strong>：`run_agent_turn` 調用 `session.list_tools()` 取得目前工具定義，並作為 `tools` 參數提供給 LLM。
- <strong>工具使用迴圈</strong>：當模型回傳 `tool_use` 區塊時，`run_agent_turn` 調用 `session.call_tool()` 執行每項工具，並將結果回餵給模型，持續這樣直到模型產生最終文字回應。

請參考 [03-GettingStarted/02-client](../../../../03-GettingStarted/02-client/solution) 獲得各語言完整 MCP 用戶端範例。

---

## 實際應用案例

| 案例 | 支持方智能體 | 反對方智能體 | 評判輸出 |
|----------|-----------|---------------|--------------|
| <strong>威脅建模</strong> |「此 API 端點安全」 |「這裡有五種攻擊路徑」 | 風險優先列表 |
| **API 設計審查** |「此設計最佳」 |「這些取捨有問題」 | 建議設計方案與留意事項 |
| <strong>事實驗證</strong> |「主張 X 有證據支持」 |「證據 Y 與主張 X 矛盾」 | 信心評等的裁決 |
| <strong>技術選擇</strong> |「選擇框架 A」 |「框架 B 因為這些理由更佳」 | 附建議的決策矩陣 |

---

## 安全考量

在生產環境執行對抗式智能體時，請注意：

- <strong>沙箱代碼執行</strong>：`run_python` 工具必須在隔離環境中執行（例如無網絡訪問且有限資源的容器）。切勿直接在主機上執行不受信任的 LLM 生成代碼。
- <strong>工具調用驗證</strong>：執行前驗證所有工具輸入。雙方智能體共用同一工具伺服器，惡意提示注入可能試圖濫用工具。
- <strong>速率限制</strong>：對每個智能體的工具調用實施速率限制，防止無限循環爆增資源消耗。
- <strong>審計日誌</strong>：記錄每次工具調用及結果，方便回溯各智能體用哪些證據推理結論。
- <strong>人類介入</strong>：對於高風險決策，評判裁決應先經過人類審核再執行。

詳見 [02-Security](../../../../02-Security)，了解 MCP 安全最佳實務完整指南。

---

## 練習

為以下情境設計一個對抗式 MCP 管線：

1. <strong>程式碼審查</strong>：智能體 A 為拉取請求辯護；智能體 B 尋找錯誤、安全問題及風格問題。判官彙總主要問題。
2. <strong>架構決策</strong>：智能體 A 提倡微服務；智能體 B 支持單體架構。判官產出決策矩陣。
3. <strong>內容審核</strong>：智能體 A 主張內容安全發布；智能體 B 找出政策違規。判官給予風險評分。

針對每個情境：

- 定義雙方智能體與判官的系統提示。
- 指定各智能體所需 MCP 工具。
- 繪製訊息流程（開場論述 → 反駁 → 反反駁 → 裁決）。
- 描述如何驗證判官裁決後再執行。

---

## 重要重點

- 對抗式多智能體模式透過對立系統提示，強迫智能體嚴格檢驗彼此推理。
- 共享單一 MCP 工具伺服器，確保雙方基於同一資訊，分歧反映推理而非資料差異。
- 評判智能體整合辯論結果，產出可行結論，無需人為瓶頸決策。
- 此模式對幻覺偵測、威脅建模、事實驗證及設計審查特別有力。
- 執行工具須安全並具健全日誌紀錄，生產環境下不可或缺。

---

## 接下來的學習

- [5.1 MCP 整合](../mcp-integration/README.md)
- [5.8 安全](../mcp-security/README.md)
- [5.5 路由](../mcp-routing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，機器翻譯可能包含錯誤或不准確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->