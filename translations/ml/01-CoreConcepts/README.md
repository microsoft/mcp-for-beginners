Translation for chunk 1 of 'README.md' skipped due to timeout.
- **ലൈഫ്‌സൈക്കിൾ മാനേജ്മെന്റ്**: ക്ലയന്റുകളും സർവറുകളും തമ്മിലുള്ള കണക്ഷൻ ആരംഭിക്കൽ, കഴിവ് ചർച്ച, സെഷൻ അവസാനിപ്പിക്കൽ എന്നിവ കൈകാര്യം ചെയ്യുന്നു  
- **സർവർ പ്രിമിറ്റീവുകൾ**: ടൂളുകൾ, വിഭവങ്ങൾ, പ്രോംപ്റ്റുകൾ എന്നിവ വഴി സർവറുകൾക്ക് മുൽ പ്രവർത്തനങ്ങൾ നൽകാൻ സാധിക്കുന്നു  
- **ക്ലയന്റ് പ്രിമിറ്റീവുകൾ**: സർവറുകൾക്ക് LLM-കളിൽ നിന്ന് സാമ്പിളിംഗ് അഭ്യർത്ഥിക്കാനും, ഉപയോക്തൃ ഇൻപുട്ട് എlicit ചെയ്യാനും, ലോഗ് സന്ദേശങ്ങൾ അയയ്ക്കാനും സാധിക്കുന്നു  
- **റിയൽ-ടൈം അറിയിപ്പുകൾ**: പോളിംഗ് ഇല്ലാതെ ഡൈനാമിക് അപ്ഡേറ്റുകൾക്കായി അസിങ്ക്രോണസ് അറിയിപ്പുകൾ പിന്തുണയ്ക്കുന്നു  

#### പ്രധാന സവിശേഷതകൾ:

- **പ്രോട്ടോക്കോൾ പതിപ്പ് ചർച്ച**: അനുയോജ്യത ഉറപ്പാക്കാൻ തീയതി അടിസ്ഥാനമാക്കിയ പതിപ്പുകൾ (YYYY-MM-DD) ഉപയോഗിക്കുന്നു  
- **കഴിവ് കണ്ടെത്തൽ**: ക്ലയന്റുകളും സർവറുകളും ആരംഭിക്കുമ്പോൾ പിന്തുണയുള്ള സവിശേഷത വിവരങ്ങൾ കൈമാറുന്നു  
- **സ്റ്റേറ്റ്‌ഫുൾ സെഷനുകൾ**: പല ഇടപെടലുകളിലൂടെയും കണക്ഷൻ നില നിലനിർത്തുന്നു, കോൺടെക്സ്റ്റ് തുടർച്ചയ്ക്ക്  

### ട്രാൻസ്പോർട്ട് ലെയർ

**ട്രാൻസ്പോർട്ട് ലെയർ** MCP പങ്കാളികൾക്കിടയിലെ ആശയവിനിമയ ചാനലുകൾ, സന്ദേശ ഫ്രെയിമിംഗ്, പ്രാമാണീകരണം എന്നിവ കൈകാര്യം ചെയ്യുന്നു:

#### പിന്തുണയുള്ള ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾ:

1. **STDIO ട്രാൻസ്പോർട്ട്**:  
   - നേരിട്ടുള്ള പ്രോസസ് ആശയവിനിമയത്തിന് സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്/ഔട്ട്പുട്ട് സ്ട്രീമുകൾ ഉപയോഗിക്കുന്നു  
   - ഒരേ യന്ത്രത്തിലെ പ്രാദേശിക പ്രോസസുകൾക്കായി മികച്ചത്, നെറ്റ്‌വർക്ക് ഓവർഹെഡ് ഇല്ലാതെ  
   - പ്രാദേശിക MCP സർവർ നടപ്പാക്കലുകൾക്കായി സാധാരണയായി ഉപയോഗിക്കുന്നു  

2. **സ്റ്റ്രീമബിൾ HTTP ട്രാൻസ്പോർട്ട്**:  
   - ക്ലയന്റ്-ടു-സർവർ സന്ദേശങ്ങൾക്ക് HTTP POST ഉപയോഗിക്കുന്നു  
   - ഓപ്ഷണൽ സർവർ-സെന്റ് ഇവന്റുകൾ (SSE) സർവർ-ടു-ക്ലയന്റ് സ്റ്റ്രീമിംഗിന്  
   - നെറ്റ്‌വർക്ക് വഴി ദൂരസർവർ ആശയവിനിമയം സാധ്യമാക്കുന്നു  
   - സ്റ്റാൻഡേർഡ് HTTP പ്രാമാണീകരണം (ബിയറർ ടോക്കണുകൾ, API കീകൾ, കസ്റ്റം ഹെഡറുകൾ) പിന്തുണയ്ക്കുന്നു  
   - സുരക്ഷിത ടോക്കൺ അടിസ്ഥാന പ്രാമാണീകരണത്തിന് MCP OAuth ശുപാർശ ചെയ്യുന്നു  

#### ട്രാൻസ്പോർട്ട് അബ്സ്ട്രാക്ഷൻ:

ട്രാൻസ്പോർട്ട് ലെയർ ഡാറ്റ ലെയറിൽ നിന്നുള്ള ആശയവിനിമയ വിശദാംശങ്ങൾ അബ്സ്ട്രാക്റ്റ് ചെയ്യുന്നു, എല്ലാ ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾക്കും ഒരേ JSON-RPC 2.0 സന്ദേശ ഫോർമാറ്റ് അനുവദിക്കുന്നു. ഈ അബ്സ്ട്രാക്ഷൻ പ്രാദേശികവും ദൂരസർവറുകളും തമ്മിൽ ആപ്ലിക്കേഷനുകൾ എളുപ്പത്തിൽ മാറാൻ സഹായിക്കുന്നു.

### സുരക്ഷാ പരിഗണനകൾ

MCP നടപ്പാക്കലുകൾ എല്ലാ പ്രോട്ടോക്കോൾ പ്രവർത്തനങ്ങളിലും സുരക്ഷിതവും വിശ്വസനീയവുമായ ഇടപെടലുകൾ ഉറപ്പാക്കാൻ നിരവധി പ്രധാന സുരക്ഷാ സിദ്ധാന്തങ്ങൾ പാലിക്കണം:

- **ഉപയോക്തൃ സമ്മതവും നിയന്ത്രണവും**: ഡാറ്റ ആക്സസ് ചെയ്യുന്നതിന് മുമ്പ് ഉപയോക്താക്കൾ വ്യക്തമായ സമ്മതം നൽകണം. പങ്കുവെക്കേണ്ട ഡാറ്റയും അംഗീകരിക്കേണ്ട പ്രവർത്തനങ്ങളും വ്യക്തമായി നിയന്ത്രിക്കാൻ ഉപയോക്താക്കൾക്ക് സാധിക്കണം, പ്രവർത്തനങ്ങൾ പരിശോധിച്ച് അംഗീകരിക്കാൻ സുഗമമായ ഉപയോക്തൃ ഇന്റർഫേസുകൾ പിന്തുണയ്ക്കണം.  

- **ഡാറ്റ സ്വകാര്യത**: ഉപയോക്തൃ ഡാറ്റ വ്യക്തമായ സമ്മതത്തോടെ മാത്രമേ പുറത്തുവിടാവൂ, അനുയോജ്യമായ ആക്സസ് നിയന്ത്രണങ്ങൾ ഉപയോഗിച്ച് സംരക്ഷിക്കണം. അനധികൃത ഡാറ്റ സംപ്രേഷണം തടയുകയും എല്ലാ ഇടപെടലുകളിലും സ്വകാര്യത ഉറപ്പാക്കുകയും MCP നടപ്പാക്കലുകൾ നിർബന്ധമാണ്.  

- **ടൂൾ സുരക്ഷ**: ഏതെങ്കിലും ടൂൾ വിളിക്കുന്നതിന് മുമ്പ് വ്യക്തമായ ഉപയോക്തൃ സമ്മതം ആവശ്യമാണ്. ഓരോ ടൂളിന്റെയും പ്രവർത്തനം ഉപയോക്താക്കൾക്ക് വ്യക്തമായി മനസ്സിലാകണം, അനാവശ്യമായ അല്ലെങ്കിൽ അപകടകാരിയായ ടൂൾ പ്രവർത്തനം തടയാൻ ശക്തമായ സുരക്ഷാ പരിധികൾ നടപ്പിലാക്കണം.  

ഈ സുരക്ഷാ സിദ്ധാന്തങ്ങൾ പാലിച്ച് MCP എല്ലാ പ്രോട്ടോക്കോൾ ഇടപെടലുകളിലും ഉപയോക്തൃ വിശ്വാസം, സ്വകാര്യത, സുരക്ഷ എന്നിവ ഉറപ്പാക്കുന്നു, ശക്തമായ AI സംയോജനങ്ങൾ സാധ്യമാക്കുന്നു.

## കോഡ് ഉദാഹരണങ്ങൾ: പ്രധാന ഘടകങ്ങൾ

താഴെ ചില ജനപ്രിയ പ്രോഗ്രാമിംഗ് ഭാഷകളിൽ MCP സർവർ ഘടകങ്ങളും ടൂളുകളും എങ്ങനെ നടപ്പിലാക്കാമെന്ന് കാണിക്കുന്ന കോഡ് ഉദാഹരണങ്ങൾ നൽകിയിരിക്കുന്നു.

### .NET ഉദാഹരണം: ടൂളുകളുള്ള ലളിതമായ MCP സർവർ സൃഷ്ടിക്കൽ

ഇവിടെ ഒരു ലളിതമായ MCP സർവർ ടൂളുകൾ ഉപയോഗിച്ച് എങ്ങനെ നടപ്പിലാക്കാമെന്ന് പ്രായോഗിക .NET കോഡ് ഉദാഹരണം കാണിക്കുന്നു. ടൂളുകൾ നിർവചിച്ച് രജിസ്റ്റർ ചെയ്യുന്നതും അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യുന്നതും Model Context Protocol ഉപയോഗിച്ച് സർവർ ബന്ധിപ്പിക്കുന്നതും ഇതിൽ ഉൾപ്പെടുന്നു.

```csharp
using System;
using System.Threading.Tasks;
using ModelContextProtocol.Server;
using ModelContextProtocol.Server.Transport;
using ModelContextProtocol.Server.Tools;

public class WeatherServer
{
    public static async Task Main(string[] args)
    {
        // Create an MCP server
        var server = new McpServer(
            name: "Weather MCP Server",
            version: "1.0.0"
        );
        
        // Register our custom weather tool
        server.AddTool<string, WeatherData>("weatherTool", 
            description: "Gets current weather for a location",
            execute: async (location) => {
                // Call weather API (simplified)
                var weatherData = await GetWeatherDataAsync(location);
                return weatherData;
            });
        
        // Connect the server using stdio transport
        var transport = new StdioServerTransport();
        await server.ConnectAsync(transport);
        
        Console.WriteLine("Weather MCP Server started");
        
        // Keep the server running until process is terminated
        await Task.Delay(-1);
    }
    
    private static async Task<WeatherData> GetWeatherDataAsync(string location)
    {
        // This would normally call a weather API
        // Simplified for demonstration
        await Task.Delay(100); // Simulate API call
        return new WeatherData { 
            Temperature = 72.5,
            Conditions = "Sunny",
            Location = location
        };
    }
}

public class WeatherData
{
    public double Temperature { get; set; }
    public string Conditions { get; set; }
    public string Location { get; set; }
}
```

### ജാവ ഉദാഹരണം: MCP സർവർ ഘടകങ്ങൾ

.NET ഉദാഹരണത്തിൽ കാണിച്ച MCP സർവർ, ടൂൾ രജിസ്ട്രേഷൻ എന്നിവ ജാവയിൽ എങ്ങനെ നടപ്പിലാക്കാമെന്ന് ഈ ഉദാഹരണം കാണിക്കുന്നു.

```java
import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpToolDefinition;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.server.tool.ToolExecutionContext;
import io.modelcontextprotocol.server.tool.ToolResponse;

public class WeatherMcpServer {
    public static void main(String[] args) throws Exception {
        // ഒരു MCP സെർവർ സൃഷ്ടിക്കുക
        McpServer server = McpServer.builder()
            .name("Weather MCP Server")
            .version("1.0.0")
            .build();
            
        // ഒരു കാലാവസ്ഥാ ഉപകരണം രജിസ്റ്റർ ചെയ്യുക
        server.registerTool(McpToolDefinition.builder("weatherTool")
            .description("Gets current weather for a location")
            .parameter("location", String.class)
            .execute((ToolExecutionContext ctx) -> {
                String location = ctx.getParameter("location", String.class);
                
                // കാലാവസ്ഥാ ഡാറ്റ നേടുക (സരളീകരിച്ചത്)
                WeatherData data = getWeatherData(location);
                
                // ഫോർമാറ്റ് ചെയ്ത പ്രതികരണം തിരികെ നൽകുക
                return ToolResponse.content(
                    String.format("Temperature: %.1f°F, Conditions: %s, Location: %s", 
                    data.getTemperature(), 
                    data.getConditions(), 
                    data.getLocation())
                );
            })
            .build());
        
        // stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് സെർവർ കണക്ട് ചെയ്യുക
        try (StdioServerTransport transport = new StdioServerTransport()) {
            server.connect(transport);
            System.out.println("Weather MCP Server started");
            // പ്രോസസ് അവസാനിപ്പിക്കപ്പെടുന്നത് വരെ സെർവർ പ്രവർത്തനക്ഷമമാക്കുക
            Thread.currentThread().join();
        }
    }
    
    private static WeatherData getWeatherData(String location) {
        // നടപ്പാക്കൽ ഒരു കാലാവസ്ഥാ API വിളിക്കും
        // ഉദാഹരണ ആവശ്യങ്ങൾക്കായി സരളീകരിച്ചത്
        return new WeatherData(72.5, "Sunny", location);
    }
}

class WeatherData {
    private double temperature;
    private String conditions;
    private String location;
    
    public WeatherData(double temperature, String conditions, String location) {
        this.temperature = temperature;
        this.conditions = conditions;
        this.location = location;
    }
    
    public double getTemperature() {
        return temperature;
    }
    
    public String getConditions() {
        return conditions;
    }
    
    public String getLocation() {
        return location;
    }
}
```

### പൈത്തൺ ഉദാഹരണം: MCP സർവർ നിർമ്മാണം

ഈ ഉദാഹരണം fastmcp ഉപയോഗിക്കുന്നു, അതിനാൽ ആദ്യം അത് ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:

```python
pip install fastmcp
```
കോഡ് സാമ്പിൾ:

```python
#!/usr/bin/env python3
import asyncio
from fastmcp import FastMCP
from fastmcp.transports.stdio import serve_stdio

# ഒരു ഫാസ്റ്റ്‌എംസിപി സെർവർ സൃഷ്ടിക്കുക
mcp = FastMCP(
    name="Weather MCP Server",
    version="1.0.0"
)

@mcp.tool()
def get_weather(location: str) -> dict:
    """Gets current weather for a location."""
    return {
        "temperature": 72.5,
        "conditions": "Sunny",
        "location": location
    }

# ഒരു ക്ലാസ് ഉപയോഗിച്ച് ബദൽ സമീപനം
class WeatherTools:
    @mcp.tool()
    def forecast(self, location: str, days: int = 1) -> dict:
        """Gets weather forecast for a location for the specified number of days."""
        return {
            "location": location,
            "forecast": [
                {"day": i+1, "temperature": 70 + i, "conditions": "Partly Cloudy"}
                for i in range(days)
            ]
        }

# ക്ലാസ് ടൂളുകൾ രജിസ്റ്റർ ചെയ്യുക
weather_tools = WeatherTools()

# സെർവർ ആരംഭിക്കുക
if __name__ == "__main__":
    asyncio.run(serve_stdio(mcp))
```

### ജാവാസ്ക്രിപ്റ്റ് ഉദാഹരണം: MCP സർവർ സൃഷ്ടിക്കൽ

ജാവാസ്ക്രിപ്റ്റിൽ MCP സർവർ സൃഷ്ടിക്കുകയും രണ്ട് കാലാവസ്ഥ സംബന്ധമായ ടൂളുകൾ രജിസ്റ്റർ ചെയ്യുകയും ചെയ്യുന്ന ഉദാഹരണം.

```javascript
// ഔദ്യോഗിക മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ SDK ഉപയോഗിക്കുന്നു
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod"; // പാരാമീറ്റർ പരിശോധനയ്ക്കായി

// ഒരു MCP സെർവർ സൃഷ്ടിക്കുക
const server = new McpServer({
  name: "Weather MCP Server",
  version: "1.0.0"
});

// ഒരു കാലാവസ്ഥാ ഉപകരണം നിർവചിക്കുക
server.tool(
  "weatherTool",
  {
    location: z.string().describe("The location to get weather for")
  },
  async ({ location }) => {
    // സാധാരണയായി ഇത് ഒരു കാലാവസ്ഥ API വിളിക്കും
    // പ്രദർശനത്തിനായി ലളിതമാക്കിയിരിക്കുന്നു
    const weatherData = await getWeatherData(location);
    
    return {
      content: [
        { 
          type: "text", 
          text: `Temperature: ${weatherData.temperature}°F, Conditions: ${weatherData.conditions}, Location: ${weatherData.location}` 
        }
      ]
    };
  }
);

// ഒരു പ്രവചന ഉപകരണം നിർവചിക്കുക
server.tool(
  "forecastTool",
  {
    location: z.string(),
    days: z.number().default(3).describe("Number of days for forecast")
  },
  async ({ location, days }) => {
    // സാധാരണയായി ഇത് ഒരു കാലാവസ്ഥ API വിളിക്കും
    // പ്രദർശനത്തിനായി ലളിതമാക്കിയിരിക്കുന്നു
    const forecast = await getForecastData(location, days);
    
    return {
      content: [
        { 
          type: "text", 
          text: `${days}-day forecast for ${location}: ${JSON.stringify(forecast)}` 
        }
      ]
    };
  }
);

// സഹായക ഫംഗ്ഷനുകൾ
async function getWeatherData(location) {
  // API വിളി അനുകരിക്കുക
  return {
    temperature: 72.5,
    conditions: "Sunny",
    location: location
  };
}

async function getForecastData(location, days) {
  // API വിളി അനുകരിക്കുക
  return Array.from({ length: days }, (_, i) => ({
    day: i + 1,
    temperature: 70 + Math.floor(Math.random() * 10),
    conditions: i % 2 === 0 ? "Sunny" : "Partly Cloudy"
  }));
}

// stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് സെർവർ ബന്ധിപ്പിക്കുക
const transport = new StdioServerTransport();
server.connect(transport).catch(console.error);

console.log("Weather MCP Server started");
```
  
ഈ ജാവാസ്ക്രിപ്റ്റ് ഉദാഹരണം MCP ക്ലയന്റ് സൃഷ്ടിച്ച് സർവറുമായി ബന്ധിപ്പിക്കുകയും പ്രോംപ്റ്റ് അയയ്ക്കുകയും, ടൂൾ കോളുകൾ ഉൾപ്പെടെയുള്ള പ്രതികരണങ്ങൾ പ്രോസസ് ചെയ്യുകയും ചെയ്യുന്നത് കാണിക്കുന്നു.

## സുരക്ഷയും അനുമതിയും

MCP പ്രോട്ടോക്കോളിൽ സുരക്ഷയും അനുമതിയും കൈകാര്യം ചെയ്യാൻ നിരവധി ഉൾക്കൊള്ളിച്ച ആശയങ്ങളും മെക്കാനിസങ്ങളും ഉണ്ട്:

1. **ടൂൾ അനുമതി നിയന്ത്രണം**:  
   സെഷനിൽ മോഡലിന് ഉപയോഗിക്കാൻ അനുവദിച്ചിരിക്കുന്ന ടൂളുകൾ ക്ലയന്റുകൾ നിർദ്ദേശിക്കാം. ഇത് വ്യക്തമായി അംഗീകൃത ടൂളുകൾക്ക് മാത്രമേ ആക്സസ് ലഭിക്കുകയുള്ളൂ എന്ന് ഉറപ്പാക്കുന്നു, അനാവശ്യമായ അല്ലെങ്കിൽ അപകടകാരിയായ പ്രവർത്തനങ്ങൾ കുറയ്ക്കുന്നു. ഉപയോക്തൃ ഇഷ്ടാനുസരണം, സംഘടനാ നയങ്ങൾ, ഇടപെടൽ കോൺടെക്സ്റ്റ് എന്നിവ അടിസ്ഥാനമാക്കി അനുമതികൾ ഡൈനാമിക്കായി ക്രമീകരിക്കാം.  

2. **പ്രാമാണീകരണം**:  
   ടൂളുകൾ, വിഭവങ്ങൾ, സങ്കീർണ്ണ പ്രവർത്തനങ്ങൾ എന്നിവയ്ക്ക് ആക്സസ് നൽകുന്നതിന് മുമ്പ് സർവറുകൾ പ്രാമാണീകരണം ആവശ്യപ്പെടാം. API കീകൾ, OAuth ടോക്കണുകൾ, മറ്റ് പ്രാമാണീകരണ സ്കീമുകൾ എന്നിവ ഇതിൽ ഉൾപ്പെടാം. ശരിയായ പ്രാമാണീകരണം വിശ്വസനീയമായ ക്ലയന്റുകൾക്കും ഉപയോക്താക്കൾക്കും മാത്രമേ സർവർ-സൈഡ് കഴിവുകൾ ഉപയോഗിക്കാൻ അനുവദിക്കുകയുള്ളൂ എന്ന് ഉറപ്പാക്കുന്നു.  

3. **വാലിഡേഷൻ**:  
   എല്ലാ ടൂൾ വിളിപ്പുകൾക്കും പാരാമീറ്റർ വാലിഡേഷൻ നിർബന്ധമാണ്. ഓരോ ടൂളും അതിന്റെ പാരാമീറ്ററുകളുടെ പ്രതീക്ഷിക്കുന്ന തരം, ഫോർമാറ്റ്, നിയന്ത്രണങ്ങൾ നിർവചിക്കുന്നു, സർവർ വരവേൽക്കുന്ന അഭ്യർത്ഥനകൾ അവ അനുസരിച്ച് പരിശോധിക്കുന്നു. ഇത് തെറ്റായ അല്ലെങ്കിൽ ദുഷ്പ്രവർത്തന ഇൻപുട്ട് ടൂൾ നടപ്പാക്കലിലേക്ക് എത്തുന്നത് തടയുകയും പ്രവർത്തനങ്ങളുടെ അഖണ്ഡത നിലനിർത്തുകയും ചെയ്യുന്നു.  

4. **റേറ്റ് ലിമിറ്റിംഗ്**:  
   ദുരുപയോഗം തടയാനും സർവർ വിഭവങ്ങളുടെ നീതിയായ ഉപയോഗം ഉറപ്പാക്കാനും MCP സർവർ ടൂൾ കോളുകൾക്കും വിഭവ ആക്സസിനും റേറ്റ് ലിമിറ്റിംഗ് നടപ്പിലാക്കാം. ഉപയോക്തൃ, സെഷൻ, ആഗോള തലങ്ങളിൽ റേറ്റ് ലിമിറ്റുകൾ പ്രയോഗിക്കാം, ഡിനയൽ-ഓഫ്-സർവീസ് ആക്രമണങ്ങൾക്കും അധിക വിഭവ ഉപഭോഗത്തിനും പ്രതിരോധം നൽകുന്നു.  

ഈ മെക്കാനിസങ്ങൾ സംയോജിപ്പിച്ച് MCP ഭാഷാ മോഡലുകളെ ബാഹ്യ ടൂളുകളുമായി, ഡാറ്റ സ്രോതസ്സുകളുമായി സുരക്ഷിതമായി സംയോജിപ്പിക്കാൻ ഒരു ഉറച്ച അടിസ്ഥാനമൊരുക്കുന്നു, ഉപയോക്താക്കളും ഡെവലപ്പർമാരും ആക്സസ് നിയന്ത്രണവും ഉപയോഗ നിയന്ത്രണവും സൂക്ഷ്മമായി കൈകാര്യം ചെയ്യാൻ സാധിക്കുന്നു.

## പ്രോട്ടോക്കോൾ സന്ദേശങ്ങളും ആശയവിനിമയ പ്രവാഹവും

MCP ആശയവിനിമയം ഹോസ്റ്റുകൾ, ക്ലയന്റുകൾ, സർവറുകൾ തമ്മിലുള്ള വ്യക്തവും വിശ്വസനീയവുമായ ഇടപെടലുകൾക്ക് ഘടനാപരമായ **JSON-RPC 2.0** സന്ദേശങ്ങൾ ഉപയോഗിക്കുന്നു. വ്യത്യസ്ത പ്രവർത്തനങ്ങൾക്ക് പ്രത്യേക സന്ദേശ മാതൃകകൾ പ്രോട്ടോക്കോൾ നിർവചിക്കുന്നു:

### കോർ സന്ദേശ തരം:

#### **ആരംഭിക്കൽ സന്ദേശങ്ങൾ**  
- **`initialize` അഭ്യർത്ഥന**: കണക്ഷൻ സ്ഥാപിക്കുകയും പ്രോട്ടോക്കോൾ പതിപ്പും കഴിവുകളും ചർച്ച ചെയ്യുകയും ചെയ്യുന്നു  
- **`initialize` പ്രതികരണം**: പിന്തുണയുള്ള സവിശേഷതകളും സർവർ വിവരങ്ങളും സ്ഥിരീകരിക്കുന്നു  
- **`notifications/initialized`**: ആരംഭിക്കൽ പൂർത്തിയായി സെഷൻ തയ്യാറാണെന്ന് സൂചിപ്പിക്കുന്നു  

#### **കണ്ടെത്തൽ സന്ദേശങ്ങൾ**  
- **`tools/list` അഭ്യർത്ഥന**: സർവറിൽ ലഭ്യമായ ടൂളുകൾ കണ്ടെത്തുന്നു  
- **`resources/list` അഭ്യർത്ഥന**: ലഭ്യമായ വിഭവങ്ങൾ (ഡാറ്റ സ്രോതസ്സുകൾ) പട്ടികപ്പെടുത്തുന്നു  
- **`prompts/list` അഭ്യർത്ഥന**: ലഭ്യമായ പ്രോംപ്റ്റ് ടെംപ്ലേറ്റുകൾ നേടുന്നു  

#### **നടപ്പാക്കൽ സന്ദേശങ്ങൾ**  
- **`tools/call` അഭ്യർത്ഥന**: നൽകിയ പാരാമീറ്ററുകളോടെ ഒരു പ്രത്യേക ടൂൾ പ്രവർത്തിപ്പിക്കുന്നു  
- **`resources/read` അഭ്യർത്ഥന**: ഒരു പ്രത്യേക വിഭവത്തിൽ നിന്നുള്ള ഉള്ളടക്കം നേടുന്നു  
- **`prompts/get` അഭ്യർത്ഥന**: ഓപ്ഷണൽ പാരാമീറ്ററുകളോടെ പ്രോംപ്റ്റ് ടെംപ്ലേറ്റ് ലഭിക്കുന്നു  

#### **ക്ലയന്റ്-സൈഡ് സന്ദേശങ്ങൾ**  
- **`sampling/complete` അഭ്യർത്ഥന**: ക്ലയന്റിൽ നിന്ന് LLM പൂർത്തീകരണം സർവർ അഭ്യർത്ഥിക്കുന്നു  
- **`elicitation/request`**: ഉപയോക്തൃ ഇൻപുട്ട് ക്ലയന്റ് ഇന്റർഫേസിലൂടെ അഭ്യർത്ഥിക്കുന്നു  
- **ലോഗിംഗ് സന്ദേശങ്ങൾ**: ക്ലയന്റിലേക്ക് ഘടനാപരമായ ലോഗ് സന്ദേശങ്ങൾ സർവർ അയയ്ക്കുന്നു  

#### **അറിയിപ്പ് സന്ദേശങ്ങൾ**  
- **`notifications/tools/list_changed`**: ടൂൾ മാറ്റങ്ങൾക്കായി ക്ലയന്റിനെ അറിയിക്കുന്നു  
- **`notifications/resources/list_changed`**: വിഭവ മാറ്റങ്ങൾക്കായി ക്ലയന്റിനെ അറിയിക്കുന്നു  
- **`notifications/prompts/list_changed`**: പ്രോംപ്റ്റ് മാറ്റങ്ങൾക്കായി ക്ലയന്റിനെ അറിയിക്കുന്നു  

### സന്ദേശ ഘടന:

എല്ലാ MCP സന്ദേശങ്ങളും JSON-RPC 2.0 ഫോർമാറ്റ് പാലിക്കുന്നു:  
- **അഭ്യർത്ഥന സന്ദേശങ്ങൾ**: `id`, `method`, ഓപ്ഷണൽ `params` ഉൾക്കൊള്ളുന്നു  
- **പ്രതികരണ സന്ദേശങ്ങൾ**: `id` കൂടാതെ `result` അല്ലെങ്കിൽ `error` ഉൾക്കൊള്ളുന്നു  
- **അറിയിപ്പ് സന്ദേശങ്ങൾ**: `method` കൂടാതെ ഓപ്ഷണൽ `params` (id ഇല്ല, പ്രതികരണം പ്രതീക്ഷിക്കില്ല)  

ഈ ഘടനാപരമായ ആശയവിനിമയം വിശ്വസനീയവും ട്രേസബിളുമായ ഇടപെടലുകൾ ഉറപ്പാക്കുന്നു, റിയൽ-ടൈം അപ്ഡേറ്റുകൾ, ടൂൾ ചെയിനിംഗ്, ശക്തമായ പിശക് കൈകാര്യം എന്നിവ പോലുള്ള പുരോഗമന സന്നിവേശങ്ങൾ പിന്തുണയ്ക്കുന്നു.

## പ്രധാനപ്പെട്ട കാര്യങ്ങൾ

- **ആർക്കിടെക്ചർ**: MCP ഹോസ്റ്റുകൾക്ക് നിരവധി ക്ലയന്റ് കണക്ഷനുകൾ സർവറുകളിലേക്ക് കൈകാര്യം ചെയ്യുന്ന ക്ലയന്റ്-സർവർ ആർക്കിടെക്ചർ ഉപയോഗിക്കുന്നു  
- **പങ്കാളികൾ**: ഈ പരിസ്ഥിതിയിൽ ഹോസ്റ്റുകൾ (AI ആപ്ലിക്കേഷനുകൾ), ക്ലയന്റുകൾ (പ്രോട്ടോക്കോൾ കണക്ടറുകൾ), സർവറുകൾ (കഴിവ് ദാതാക്കൾ) ഉൾപ്പെടുന്നു  
- **ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾ**: STDIO (പ്രാദേശിക)യും ഓപ്ഷണൽ SSE ഉള്ള സ്റ്റ്രീമബിൾ HTTP (ദൂര)യും ആശയവിനിമയം പിന്തുണയ്ക്കുന്നു  
- **കോർ പ്രിമിറ്റീവുകൾ**: സർവറുകൾ ടൂളുകൾ (നടപ്പിലാക്കാവുന്ന ഫംഗ്ഷനുകൾ), വിഭവങ്ങൾ (ഡാറ്റ സ്രോതസ്സുകൾ), പ്രോംപ്റ്റുകൾ (ടെംപ്ലേറ്റുകൾ) പുറത്തുവിടുന്നു  
- **ക്ലയന്റ് പ്രിമിറ്റീവുകൾ**: സർവറുകൾ sampling (LLM പൂർത്തീകരണങ്ങൾ), elicitation (ഉപയോക്തൃ ഇൻപുട്ട്), ലോഗിംഗ് ക്ലയന്റുകളിൽ നിന്ന് അഭ്യർത്ഥിക്കാം  
- **പ്രോട്ടോക്കോൾ അടിസ്ഥാനമാക്കൽ**: JSON-RPC 2.0-ൽ നിർമ്മിച്ചിരിക്കുന്നു, തീയതി അടിസ്ഥാന പതിപ്പുമായി (നിലവിൽ: 2025-11-25)  
- **റിയൽ-ടൈം കഴിവുകൾ**: ഡൈനാമിക് അപ്ഡേറ്റുകൾക്കും റിയൽ-ടൈം സിങ്ക്രോണൈസേഷനും അറിയിപ്പുകൾ പിന്തുണയ്ക്കുന്നു  
- **സുരക്ഷ മുൻഗണന**: വ്യക്തമായ ഉപയോക്തൃ സമ്മതം, ഡാറ്റ സ്വകാര്യത സംരക്ഷണം, സുരക്ഷിത ട്രാൻസ്പോർട്ട് എന്നിവ പ്രധാന ആവശ്യകതകൾ  

## അഭ്യാസം

നിങ്ങളുടെ മേഖലയിലെ ഉപകാരപ്രദമായ ലളിതമായ MCP ടൂൾ രൂപകൽപ്പന ചെയ്യുക. നിർവചിക്കുക:  
1. ടൂളിന്റെ പേര് എന്താകും  
2. സ്വീകരിക്കുന്ന പാരാമീറ്ററുകൾ എന്തെല്ലാം ആയിരിക്കും  
3. പുറപ്പെടുന്ന ഔട്ട്പുട്ട് എന്താകും  
4. ഉപയോക്തൃ പ്രശ്നങ്ങൾ പരിഹരിക്കാൻ മോഡൽ ഈ ടൂൾ എങ്ങനെ ഉപയോഗിക്കാം  

---

## അടുത്തത്

അടുത്തത്: [അധ്യായം 2: സുരക്ഷ](../02-Security/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->