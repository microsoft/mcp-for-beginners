# Running the sample

Here we assume you already have a working server code. Please locate a server from one of the earlier chapters.

## Set up mcp.json

Here's a file you use for reference, [mcp.json](./mcp.json). Copy it to a `.vscode` folder in the workspace you open in VS Code.

Change the server entry as needed to point to your server, including the full command to run it. Use an absolute path or `${workspaceFolder}`: a relative path such as `build/index.js` only works when the workspace you opened is the server's own folder.

In the example file referred above the server entry looks like so. It assumes you opened this repository as the workspace and starts the TypeScript server from [01-first-server](../../01-first-server/solution/typescript/), so build that server first:

```bash
cd 03-GettingStarted/01-first-server/solution/typescript
npm install
npm run build
```

<details>
<summary>node.js</summary>

```json
"hello-mcp": {
    "type": "stdio",
    "command": "node",
    "args": [
        "${workspaceFolder}/03-GettingStarted/01-first-server/solution/typescript/build/index.js"
    ]
}
```

</details>

<details>
<summary>.NET</summary>

You might have to enter the GitHub repository root, which can be fetched from the command, `git rev-parse --show-toplevel`.

```jsonc
{
  "inputs": [
    {
      "type": "promptString",
      "id": "repository-root",
      "description": "The absolute path to the repository root"
    }
  ],
  "servers": {
    "calculator-mcp-dotnet": {
      "type": "stdio",
      "command": "dotnet",
      "args": [
        "run",
        "--project",
        "${input:repository-root}/03-GettingStarted/02-client/solution/server/server.csproj"
      ]
    }
  }
}
```

</details>

The node.js entry corresponds to running `node <repository-root>/03-GettingStarted/01-first-server/solution/typescript/build/index.js`. The .NET entry also works with `${workspaceFolder}` in place of `${input:repository-root}` when you opened the repository as the workspace.

- Change this server entry to fit where your server file is located or to what's needed to startup your server depending on your chosen runtime and server location.

## Consume the features in the server

- Click the `play` icon, once you've added *mcp.json* to the *.vscode* folder,

    Observe the tooling icon change to increase the number of available tools. Tooling icon is located right above the chat field in GitHub Copilot.

## Run a tool

- Type a prompt in your chat window that matches the description of your tool. For example to trigger the tool `add` type something like "add 3 to 20".

    You should see a tool being presented above the chat text box indicating for you to select to run the tool like in this visual:

    ![VS Code indicating it wanting to run a tool](../assets/vscode-agent.png)

    Selecting the tool should produce a numeric result saying "23" if your prompt was like we mentioned previously.
