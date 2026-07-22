# Consuming a server from GitHub Copilot Agent mode

Visual Studio Code and GitHub Copilot can act as a client and consume an MCP Server. Why would we want to do that you might ask? Well, that means whatever features the MCP Server has can now be used from within your IDE. Imagine you adding for example GitHub's MCP server, this would allow for controlling GitHub via prompts over typing specific commands in the terminal. Or imagine anything in general that could improve your developer experience all controlled by natural language. Now you start to see the win right?

## Overview

This lesson covers how to use Visual Studio Code and GitHub Copilot's Agent mode as a client for your MCP Server.

## Learning Objectives

By the end of this lesson, you will be able to:

- Consume an MCP Server via Visual Studio Code.
- Run capabilities like tools via GitHub Copilot.
- Configure Visual Studio Code to find and manage your MCP Server.

## Usage

You can control your MCP server in two different ways:

- User interface, you will see how this is done later in this chapter.
- Terminal, it's possible to control things from the terminal using the `code` executable:

  To add an MCP server to your user profile, use the --add-mcp command line option, and provide the JSON server configuration in the form {\"name\":\"server-name\",\"command\":...}.

  ```
  code --add-mcp "{\"name\":\"my-server\",\"command\": \"uvx\",\"args\": [\"mcp-server-fetch\"]}"
  ```

### Screenshots

![Guided MCP server configuration in Visual Studio Code](../../images/03-GettingStarted/chat-mode-agent.png)
![Tool selection per agent session](../../images/03-GettingStarted/agent-mode-select-tools.png)
![Easily debug errors during MCP development](../../images/03-GettingStarted/mcp-list-servers.png)

Let's talk more about how we use the visual interface in the next sections.

## Approach

Here's how we need to approach this at high level:

- Configure a file to find our MCP Server.
- Start up/Connect to said server to have it list its capabilities.
- Use said capabilities through GitHub Copilot Chat interface.

Great, now that we understand the flow, let's try use an MCP Server through Visual Studio Code through an exercise.

## Exercise: Consuming a server

In this exercise, we will configure Visual Studio Code to find your MCP server so that it can be used from GitHub Copilot Chat interface.

### -0- Prestep, enable MCP Server discovery

You may need to enable discovery of MCP Servers.

1. Go to `File -> Preferences -> Settings` in Visual Studio Code.

1. Search for "MCP" and enable `chat.mcp.discovery.enabled` in the settings.json file.

### -1- Create config file

Start by creating a config file in your project root, you will need a file called MCP.json and to place it in a folder called .vscode. It should look like so:

```text
.vscode
|-- mcp.json
```

Next, let's see how we can add a server entry.

### -2- Configure a server

Add the following content to *mcp.json*:

```json
{
    "inputs": [],
    "servers": {
       "hello-mcp": {
           "command": "node",
           "args": [
               "build/index.js"
           ]
       }
    }
}
```

Here's a simple example above how to start a server written in Node.js, for other runtimes point out the proper command for starting the server using `command` and `args`.

### -3- Start the server

Now that you've added an entry, let's start the server:

1. Locate your entry in *mcp.json* and make sure you find the "play" icon:

  ![Starting server in Visual Studio Code](./assets/vscode-start-server.png)  

1. Click the "play" icon, you should see the tools icon in the GitHub Copilot Chat increase the number of available tools. If you click said tools icon, you will see a list of registered tools. You can check/uncheck each tool depending if you want GitHub Copilot to use them as context:

  ![Starting server in Visual Studio Code](./assets/vscode-tool.png)

1. To run a tool, type a prompt that you know will match the description of one of your tools, for example a prompt like so "add 22 to 1":

  ![Running a tool from GitHub Copilot](./assets/vscode-agent.png)

  You should see a response saying 23.

## Assignment

Try adding a server entry to your *mcp.json* file and make sure you can start/stop the server. Make sure you can also communicate with the tools on your server via GitHub Copilot Chat interface.

## Solution

[Solution](./solution/README.md)

## Key Takeaways

The takeaways from this chapter is the following:

- Visual Studio Code is a great client that lets you consume several MCP Servers and their tools.
- GitHub Copilot Chat interface is how you interact with the servers.
- You can prompt the user for inputs like API keys that can be passed to the MCP Server when configuring the server entry in *mcp.json* file.

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../samples/csharp/)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../samples/python/)

## Additional Resources

- [Visual Studio docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## What's Next

- Next: [Creating a stdio Server](../05-stdio-server/README.md)
