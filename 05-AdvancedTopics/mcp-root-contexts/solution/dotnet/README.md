````markdown
# .NET Root Context Example

This example demonstrates how to implement MCP root contexts in a .NET application for customer support scenarios.

## Prerequisites

- .NET 8.0 SDK or later
- MCP .NET Client package
- Visual Studio 2022 or VS Code with C# extension

## Setup

1. **Create a new console application:**
   ```bash
   dotnet new console -n RootContextExample
   cd RootContextExample
   ```

2. **Add the MCP Client package:**
   ```bash
   dotnet add package Microsoft.Mcp.Client
   ```

3. **Copy the example code:**
   - Replace the contents of `Program.cs` with `RootContextExample.cs`

4. **Update the project file (`RootContextExample.csproj`):**
   ```xml
   <Project Sdk="Microsoft.NET.Sdk">
     <PropertyGroup>
       <OutputType>Exe</OutputType>
       <TargetFramework>net8.0</TargetFramework>
       <ImplicitUsings>enable</ImplicitUsings>
       <Nullable>enable</Nullable>
     </PropertyGroup>
     
     <ItemGroup>
       <PackageReference Include="Microsoft.Mcp.Client" Version="1.0.0" />
     </ItemGroup>
   </Project>
   ```

## Configuration

Update the MCP server URL in the `Main` method:
```csharp
var client = new McpClient("YOUR_MCP_SERVER_URL");
```

## Running the Example

1. **Build the project:**
   ```bash
   dotnet build
   ```

2. **Run the application:**
   ```bash
   dotnet run
   ```

## What the Example Demonstrates

- ✅ **Context Creation**: Creating a new root context with metadata
- 💬 **Multi-turn Conversations**: Sending multiple messages that reference previous context
- 📝 **Metadata Updates**: Adding information discovered during conversations
- 📊 **Context Monitoring**: Retrieving context information and statistics
- 🗄️ **Context Archival**: Properly cleaning up completed conversations

## Expected Output

```
✅ Created root context with ID: [context-id]
🤖 AI Response: [AI response about scaling issues]
🤖 AI Response: [AI response referencing Kubernetes]
📝 Updated context metadata with conversation insights
📊 Context Information:
   • Name: Customer Support Session
   • Created: [timestamp]
   • Messages: 2
🗄️ Archived context [context-id]
✅ Root context demonstration completed!
```

## Key Features

- **Enterprise-grade patterns**: Uses dependency injection and async/await
- **Type safety**: Strongly-typed objects with compile-time validation
- **Error handling**: Robust exception handling for production use
- **Metadata management**: Flexible metadata storage and retrieval

## Next Steps

- Integrate with your existing .NET application
- Add error handling and logging
- Implement user authentication
- Scale for production workloads
````