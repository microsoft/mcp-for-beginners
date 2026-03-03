using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Protocol;
using System.Diagnostics;
using System.Net;
using System.Text;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration 
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = $"{Path.Combine(AppContext.BaseDirectory, "../../../../", "server/bin/Debug/net9.0/server")}",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

Console.WriteLine("Listing tools");

var tools = await mcpClient.ListToolsAsync();

foreach (var tool in tools)
{
    Console.WriteLine($"Connected to server with tools: {tool.Name}");
}

var result = await mcpClient.CallToolAsync(
    "add",
    new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
    cancellationToken:CancellationToken.None);

Console.WriteLine("Result: " + ((TextContentBlock)result.Content[0]).Text);



