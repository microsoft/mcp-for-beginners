/**
 * MCP stdio server example - Updated for MCP Specification 2025-06-18
 * 
 * This server demonstrates the recommended stdio transport instead of the 
 * deprecated SSE transport. The stdio transport is simpler, more secure,
 * and provides better performance.
 */

using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using server;

// Create host builder for stdio transport
var builder = Host.CreateApplicationBuilder(args);

// Configure services
builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

// Configure logging to stderr (never stdout for MCP servers)
builder.Services.AddLogging(logging =>
{
    logging.ClearProviders();
    logging.AddConsole();
    logging.SetMinimumLevel(LogLevel.Information);
});

// Build and run the application
var app = builder.Build();

// Log startup information to stderr
var logger = app.Services.GetRequiredService<ILogger<Program>>();
logger.LogInformation("Starting MCP stdio server...");
logger.LogInformation("Server configured for stdio transport (MCP 2025-06-18)");

try
{
    await app.RunAsync();
}
catch (Exception ex)
{
    logger.LogError(ex, "Server encountered an error");
    throw;
}