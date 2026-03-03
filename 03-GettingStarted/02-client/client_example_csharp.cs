using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using System.Text.Json;

/**
 * Complete C# MCP Client Example
 * 
 * This client demonstrates how to:
 * 1. Connect to an MCP server using stdio transport
 * 2. List available tools and resources
 * 3. Call calculator tools
 * 4. Handle responses from the server
 */

Console.WriteLine("🚀 Starting MCP C# Client...");

try
{
    // Create configuration builder
    var builder = Host.CreateApplicationBuilder(args);

    builder.Configuration
        .AddEnvironmentVariables()
        .AddUserSecrets<Program>();

    // Create stdio transport to connect to the MCP server
    var clientTransport = new StdioClientTransport(new()
    {
        Name = "Calculator Server",
        Command = "dotnet",
        Arguments = ["run", "--project", "../01-first-server/solution/csharp/calculator-server.csproj"],
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

    // Test calculator operations
    Console.WriteLine("\n🧮 Testing Calculator Operations:");

    // Addition
    var addResult = await mcpClient.CallToolAsync(
        "Add",
        new Dictionary<string, object?>() { ["a"] = 5, ["b"] = 3 },
        cancellationToken: CancellationToken.None
    );
    Console.WriteLine($"Add 5 + 3 = {ExtractTextResult(addResult)}");

    // Subtraction
    var subtractResult = await mcpClient.CallToolAsync(
        "Subtract",
        new Dictionary<string, object?>() { ["a"] = 10, ["b"] = 4 },
        cancellationToken: CancellationToken.None
    );
    Console.WriteLine($"Subtract 10 - 4 = {ExtractTextResult(subtractResult)}");

    // Multiplication
    var multiplyResult = await mcpClient.CallToolAsync(
        "Multiply",
        new Dictionary<string, object?>() { ["a"] = 6, ["b"] = 7 },
        cancellationToken: CancellationToken.None
    );
    Console.WriteLine($"Multiply 6 × 7 = {ExtractTextResult(multiplyResult)}");

    // Division
    var divideResult = await mcpClient.CallToolAsync(
        "Divide",
        new Dictionary<string, object?>() { ["a"] = 20, ["b"] = 4 },
        cancellationToken: CancellationToken.None
    );
    Console.WriteLine($"Divide 20 ÷ 4 = {ExtractTextResult(divideResult)}");

    // Help
    var helpResult = await mcpClient.CallToolAsync(
        "Help",
        new Dictionary<string, object?>(),
        cancellationToken: CancellationToken.None
    );
    Console.WriteLine($"\n📖 Help Information:");
    Console.WriteLine(ExtractTextResult(helpResult));

    // List resources if available
    try
    {
        Console.WriteLine("\n📄 Listing available resources:");
        var resources = await mcpClient.ListResourcesAsync();
        foreach (var resource in resources)
        {
            Console.WriteLine($"  - {resource.Name}: {resource.Description}");
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine("  No resources available or error listing resources: " + ex.Message);
    }

    Console.WriteLine("\n✨ Client operations completed successfully!");
}
catch (Exception ex)
{
    Console.WriteLine($"❌ Error running MCP client: {ex.Message}");
    Console.WriteLine($"Stack trace: {ex.StackTrace}");
}

/// <summary>
/// Extracts the text result from a tool call response object.
/// </summary>
/// <param name="result">The result object, which may contain text content or other data.</param>
/// <returns>
/// A string containing the extracted text if found, a serialized representation of the result if no text is found, 
/// or a fallback string if serialization fails.
/// </returns>
static string ExtractTextResult(object result)
{
    try
    {
        if (result is IEnumerable<object> contentList)
        {
            foreach (var content in contentList)
            {
                if (content is IDictionary<string, object> contentDict &&
                    contentDict.TryGetValue("text", out var text))
                {
                    return text?.ToString() ?? "No text content";
                }
            }
        }
        
        // Fallback: try to serialize the entire result
        return JsonSerializer.Serialize(result, new JsonSerializerOptions { WriteIndented = true });
    }
    catch
    {
        return result?.ToString() ?? "No result";
    }
}
