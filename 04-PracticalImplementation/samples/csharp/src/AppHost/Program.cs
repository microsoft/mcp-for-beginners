using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

builder.AddProject<Projects.calculatorMCPServer>("calc-mcp")
				.WithExternalHttpEndpoints();

builder.Build().Run();
