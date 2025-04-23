using Calculator.Tools;

var builder = WebApplication.CreateBuilder(args);       
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
	.AddMcpServer()
	.WithStdioServerTransport()
	.WithToolsFromAssembly()
	.WithHttpTransport();

builder.AddServiceDefaults();

var app = builder.Build();

app.MapMcp();

app.Run();