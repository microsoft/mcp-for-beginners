using Aspire.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

builder.AddProject<Projects.calculatorMCPServer>("calculatorMCPServer");

builder.Build().Run();
