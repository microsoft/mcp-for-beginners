using System.ComponentModel;
using System.Text.Json;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

namespace server;

[McpServerToolType]
public sealed class Tools
{
    private readonly ILogger<Tools> _logger;

    public Tools(ILogger<Tools> logger)
    {
        _logger = logger;
    }

    [McpServerTool, Description("Add two numbers together")]
    public async Task<string> AddNumbers(
        [Description("The first number")] int a,
        [Description("The second number")] int b)
    {
        var result = a + b;
        _logger.LogInformation("Adding {A} + {B} = {Result}", a, b, result);
        return await Task.FromResult($"{a} + {b} = {result}");
    }

    [McpServerTool, Description("Multiply two numbers together")]
    public async Task<string> MultiplyNumbers(
        [Description("The first number")] int a,
        [Description("The second number")] int b)
    {
        var result = a * b;
        _logger.LogInformation("Multiplying {A} × {B} = {Result}", a, b, result);
        return await Task.FromResult($"{a} × {b} = {result}");
    }

    [McpServerTool, Description("Generate a personalized greeting")]
    public async Task<string> GetGreeting(
        [Description("Name of the person to greet")] string name)
    {
        var greeting = $"Hello, {name}! Welcome to the MCP stdio server.";
        _logger.LogInformation("Generated greeting for {Name}", name);
        return await Task.FromResult(greeting);
    }

    [McpServerTool, Description("Get information about this MCP server")]
    public async Task<string> GetServerInfo()
    {
        var serverInfo = new
        {
            server_name = "example-stdio-server",
            version = "1.0.0",
            transport = "stdio",
            capabilities = new[] { "tools" },
            description = "Example MCP server using stdio transport (MCP 2025-06-18 specification)"
        };

        var json = JsonSerializer.Serialize(serverInfo, new JsonSerializerOptions 
        { 
            WriteIndented = true 
        });

        _logger.LogInformation("Providing server information");
        return await Task.FromResult(json);
    }
}