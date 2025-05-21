# Consuming a Server from GitHub Copilot Agent Mode

Visual Studio Code and GitHub Copilot can act as a client and consume an MCP Server. Why would we want to do that, you might ask? Well, that means whatever features the MCP Server has can now be used from within your IDE. Imagine adding, for example, GitHub's MCP server—this would allow you to control GitHub via prompts instead of typing specific commands in the terminal. Or imagine anything in general that could improve your developer experience, all controlled by natural language. Now you start to see the benefit, right?

## Overview

This lesson covers how to use Visual Studio Code and GitHub Copilot's Agent mode as a client for your MCP Server.

## Learning Objectives

By the end of this lesson, you will be able to:

- Consume an MCP Server via Visual Studio Code.
- Run capabilities like tools via GitHub Copilot.
- Configure Visual Studio Code to find and manage your MCP Server.

## Usage

You can control your MCP server in two different ways:

- User interface: You will see how this is done later in this chapter.
- Terminal: It's possible to control things from the terminal using the `code` executable.

  To add an MCP server to your user profile, use the `--add-mcp` command line option, and provide the JSON server configuration in the form `{"name":"server-name","command":...}`.

  ```sh
  code --add-mcp "{\"name\":\"my-server\",\"command\": \"uvx\",\"args\": [\"mcp-server-fetch\"]}"
  ```

<details>
<summary>Screenshots</summary>

![Guided MCP server configuration in Visual Studio Code](../images/03-GettingStarted/chat-mode-agent.png)
![Tool selection per agent session](../images/03-GettingStarted/agent-mode-select-tools.png)
![Easily debug errors during MCP development](../images/03-GettingStarted/mcp-list-servers.png)
</details>

Let's talk more about how we use the visual interface in the next sections.

## Approach

Here's how we need to approach this at a high level:

- Configure a file to find our MCP Server.
- Start up/connect to said server to have it list its capabilities.
- Use those capabilities through GitHub Copilot's chat interface.

Great, now that we understand the flow, let's try using an MCP Server through Visual Studio Code with an exercise.

## Exercise: Consuming a Server

In this exercise, we will configure Visual Studio Code to find your MCP server so that it can be used from GitHub Copilot's chat interface.

### -0- Prestep: Enable MCP Server Discovery

You may need to enable discovery of MCP Servers.

1. Go to `File -> Preferences -> Settings` in Visual Studio Code.
2. Search for "MCP" and enable `chat.mcp.discovery.enabled` in the settings.json file.

### -1- Create Config File

Start by creating a config file in your project root. You will need a file called `mcp.json` and to place it in a folder called `.vscode`. It should look like so:

```text
.vscode
|-- mcp.json
```

Next, let's see how we can add a server entry.

### -2- Configure a Server

Add the following content to *mcp.json*:

```json
{
    "inputs": [],
    "servers": {
       "hello-mcp": {
           "command": "cmd",
           "args": [
               "/c", "node", "<absolute path>\\build\\index.js"
           ]
       }
    }
}
```

Here's a simple example above for how to start a server written in Node.js. For other runtimes, specify the proper command for starting the server using `command` and `args`.

### -3- Start the Server

Now that you've added an entry, let's start the server:

1. Locate your entry in *mcp.json* and make sure you find the "play" icon:

   ![Starting server in Visual Studio Code](./assets/vscode-start-server.png)  

2. Click the "play" icon. You should see the tools icon in the GitHub Copilot chat increase the number of available tools. If you click the tools icon, you will see a list of registered tools. You can check or uncheck each tool depending on whether you want GitHub Copilot to use them as context:

   ![Starting server in Visual Studio Code](./assets/vscode-tool.png)

3. To run a tool, type a prompt that you know will match the description of one of your tools, for example, a prompt like "add 22 to 1":

   ![Running a tool from GitHub Copilot](./assets/vscode-agent.png)

   You should see a response saying 23.

## Assignment

Try adding a server entry to your *mcp.json* file and make sure you can start/stop the server. Make sure you can also communicate with the tools on your server via GitHub Copilot's chat interface.

## Solution

[Solution](./solution/README.md)

## Key Takeaways

The takeaways from this chapter are the following:

- Visual Studio Code is a great client that lets you consume several MCP Servers and their tools.
- GitHub Copilot's chat interface is how you interact with the servers.
- You can prompt the user for inputs like API keys that can be passed to the MCP Server when configuring the server entry in the *mcp.json* file.

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../samples/csharp/)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../samples/python/) 

## Additional Resources

- [Visual Studio docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## What's Next

Next: [Creating an SSE Server](/03-GettingStarted/05-sse-server/README.md)


