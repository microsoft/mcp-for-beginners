# Sample

This is a JavaScript sample for an MCP Server

Here's an example of a tool registration where we register a tool:

```csharp
[McpTool("getCurrentWeather", "Gets the current weather for a location")]
public async Task<WeatherResult> GetCurrentWeatherAsync(
    [McpParameter(Description = "The location to get weather for")] string location)
{
    _logger.LogInformation($"Getting weather for {location}");

    // Simulate API call delay
    await Task.Delay(500);
    
    // Return mock weather data
    return new WeatherResult
    {
        Location = location,
        Temperature = new Random().Next(0, 35),
        Condition = GetRandomWeatherCondition(),
        Timestamp = DateTime.UtcNow
    };
}
```

## Install

Run the following command:

```bash
dotnet restore
```

## Run

```bash
dotnet run
```