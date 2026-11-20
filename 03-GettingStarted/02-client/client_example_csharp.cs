using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

/**
 * Complete C# MCP Client Example
 *
 * This client demonstrates how to:
 * 1. Connect to an MCP server using stdio transport
 * 2. List available tools
 * 3. Call the calculator tool
 * 4. Handle responses from the server
 *
 * It starts the .NET server from 01-first-server/solution/dotnet.
 * See complete_examples.md for how to run it.
 */

Console.WriteLine("🚀 Starting MCP C# Client...");

try
{
    // Create stdio transport to start and connect to the MCP server
    var clientTransport = new StdioClientTransport(new()
    {
        Name = "Calculator Server",
        Command = "dotnet",
        Arguments = ["run", "--project", "../../01-first-server/solution/dotnet/dotnet.csproj"],
    });

    Console.WriteLine("📡 Connecting to MCP server...");

    // Create and connect the MCP client
    await using var mcpClient = await McpClient.CreateAsync(clientTransport);

    Console.WriteLine("✅ Connected to MCP server successfully!");

    // List available tools
    Console.WriteLine("\n📋 Listing available tools:");
    var tools = await mcpClient.ListToolsAsync();
    foreach (var tool in tools)
    {
        Console.WriteLine($"  - {tool.Name}: {tool.Description}");
    }

    // Call the add tool. The C# SDK publishes the C# method `Add` as `add`.
    Console.WriteLine("\n🧮 Testing Calculator Operations:");
    var addResult = await mcpClient.CallToolAsync(
        "add",
        new Dictionary<string, object?>() { ["a"] = 5, ["b"] = 3 },
        cancellationToken: CancellationToken.None
    );
    Console.WriteLine($"Add 5 + 3 = {ExtractTextResult(addResult)}");

    Console.WriteLine("\n✨ Client operations completed successfully!");
}
catch (Exception ex)
{
    Console.WriteLine($"❌ Error running MCP client: {ex.Message}");
}

/// <summary>
/// Extracts the text content from a tool call result.
/// </summary>
static string ExtractTextResult(CallToolResult result)
{
    var text = result.Content.OfType<TextContentBlock>().FirstOrDefault()?.Text;
    return text ?? "No text content";
}
