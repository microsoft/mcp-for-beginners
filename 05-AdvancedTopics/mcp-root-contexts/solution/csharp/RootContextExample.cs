// .NET Example: Root Context Management Setup
using Microsoft.Mcp.Client;
using System;
using System.Threading.Tasks;
using System.Collections.Generic;

public class RootContextExample
{
    private readonly IMcpClient _client;
    private readonly IRootContextManager _contextManager;
    
    public RootContextExample(IMcpClient client, IRootContextManager contextManager)
    {
        _client = client;
        _contextManager = contextManager;
    }

    public async Task<string> CreateSupportContextAsync()
    {
        // Create a new root context for customer support
        var contextResult = await _contextManager.CreateRootContextAsync(new RootContextCreateOptions
        {
            Name = "Customer Support Session",
            Metadata = new Dictionary<string, string>
            {
                ["CustomerName"] = "Acme Corporation",
                ["PriorityLevel"] = "High",
                ["Domain"] = "Cloud Services"
            }
        });
        
        string contextId = contextResult.ContextId;
        Console.WriteLine($"✅ Created root context with ID: {contextId}");
        return contextId;
    }

    public async Task ConductConversationAsync(string contextId)
    {
        // First interaction using the context
        var response1 = await _client.SendPromptAsync(
            "I'm having issues scaling my web service deployment in the cloud.", 
            new SendPromptOptions { RootContextId = contextId }
        );
        Console.WriteLine($"🤖 AI Response: {response1.GeneratedText}");
        
        // Second interaction - AI remembers the previous conversation
        var response2 = await _client.SendPromptAsync(
            "Yes, we're using containerized deployments with Kubernetes.", 
            new SendPromptOptions { RootContextId = contextId }
        );
        Console.WriteLine($"🤖 AI Response: {response2.GeneratedText}");
    }

    public async Task UpdateContextInfoAsync(string contextId)
    {
        // Add metadata based on what we learned from the conversation
        await _contextManager.UpdateContextMetadataAsync(contextId, new Dictionary<string, string>
        {
            ["TechnicalEnvironment"] = "Kubernetes",
            ["IssueType"] = "Scaling",
            ["Status"] = "In Progress"
        });
        
        Console.WriteLine("📝 Updated context metadata with conversation insights");
    }

    public async Task DisplayContextInfoAsync(string contextId)
    {
        var contextInfo = await _contextManager.GetRootContextInfoAsync(contextId);
        
        Console.WriteLine("📊 Context Information:");
        Console.WriteLine($"   • Name: {contextInfo.Name}");
        Console.WriteLine($"   • Created: {contextInfo.CreatedAt}");
        Console.WriteLine($"   • Messages: {contextInfo.MessageCount}");
    }

    public async Task ArchiveContextAsync(string contextId)
    {
        // When the conversation is complete, archive the context
        await _contextManager.ArchiveRootContextAsync(contextId);
        Console.WriteLine($"🗄️ Archived context {contextId}");
    }

    public async Task DemonstrateRootContextAsync()
    {
        var contextId = await CreateSupportContextAsync();
        await ConductConversationAsync(contextId);
        await UpdateContextInfoAsync(contextId);
        await DisplayContextInfoAsync(contextId);
        await ArchiveContextAsync(contextId);
    }
}

// Program entry point
public class Program
{
    public static async Task Main(string[] args)
    {
        // Initialize MCP client and context manager
        var client = new McpClient("https://mcp-server-example.com");
        var contextManager = new RootContextManager(client);
        
        // Run the demonstration
        var example = new RootContextExample(client, contextManager);
        await example.DemonstrateRootContextAsync();
        
        Console.WriteLine("✅ Root context demonstration completed!");
    }
}