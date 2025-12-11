<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62150e27d4b7b5797ee41146d176e6b",
  "translation_date": "2025-12-11T10:49:27+00:00",
  "source_file": "08-BestPractices/README.md",
  "language_code": "ml"
}
-->
# MCP വികസന മികച്ച പ്രാക്ടീസുകൾ

[![MCP Development Best Practices](../../../translated_images/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.ml.png)](https://youtu.be/W56H9W7x-ao)

_(ഈ പാഠത്തിന്റെ വീഡിയോ കാണാൻ മുകളിൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്യുക)_

## അവലോകനം

ഈ പാഠം MCP സെർവറുകളും ഫീച്ചറുകളും പ്രൊഡക്ഷൻ പരിസ്ഥിതികളിൽ വികസിപ്പിക്കൽ, ടെസ്റ്റിംഗ്, ഡിപ്ലോയ്മെന്റ് എന്നിവയ്ക്കുള്ള ആധുനിക മികച്ച പ്രാക്ടീസുകളെക്കുറിച്ചാണ്. MCP ഇക്കോസിസ്റ്റങ്ങൾ സങ്കീർണ്ണതയും പ്രാധാന്യവും വർദ്ധിക്കുന്നതിനാൽ, സ്ഥാപിത മാതൃകകൾ പാലിക്കുന്നത് വിശ്വാസ്യത, പരിപാലനക്ഷമത, ഇന്റർഓപ്പറബിലിറ്റി എന്നിവ ഉറപ്പാക്കുന്നു. ഈ പാഠം യഥാർത്ഥ MCP നടപ്പാക്കലുകളിൽ നിന്നുള്ള പ്രായോഗിക ജ്ഞാനം സംഗ്രഹിച്ച്, ഫലപ്രദമായ റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ, ടൂളുകൾ എന്നിവയോടുകൂടിയ ശക്തമായ, കാര്യക്ഷമമായ സെർവറുകൾ സൃഷ്ടിക്കാൻ നിങ്ങളെ മാർഗ്ഗനിർദ്ദേശം ചെയ്യുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിക്കുമ്പോൾ, നിങ്ങൾക്ക് കഴിയും:

- MCP സെർവർ, ഫീച്ചർ ഡിസൈനിൽ വ്യവസായത്തിലെ മികച്ച പ്രാക്ടീസുകൾ പ്രയോഗിക്കുക
- MCP സെർവറുകൾക്കായി സമഗ്രമായ ടെസ്റ്റിംഗ് തന്ത്രങ്ങൾ സൃഷ്ടിക്കുക
- സങ്കീർണ്ണ MCP ആപ്ലിക്കേഷനുകൾക്കായി കാര്യക്ഷമവും പുനരുപയോഗയോഗ്യവുമായ വർക്ക്‌ഫ്ലോ മാതൃകകൾ രൂപകൽപ്പന ചെയ്യുക
- MCP സെർവറുകളിൽ ശരിയായ പിശക് കൈകാര്യം ചെയ്യൽ, ലോഗിംഗ്, നിരീക്ഷണക്ഷമത നടപ്പിലാക്കുക
- പ്രകടനം, സുരക്ഷ, പരിപാലനക്ഷമത എന്നിവയ്ക്ക് MCP നടപ്പാക്കലുകൾ മെച്ചപ്പെടുത്തുക

## MCP കോർ സിദ്ധാന്തങ്ങൾ

നിർദ്ദിഷ്ട നടപ്പാക്കൽ പ്രാക്ടീസുകളിൽ പ്രവേശിക്കുന്നതിന് മുമ്പ്, ഫലപ്രദമായ MCP വികസനത്തിന് മാർഗ്ഗനിർദ്ദേശം ചെയ്യുന്ന കോർ സിദ്ധാന്തങ്ങൾ മനസ്സിലാക്കുന്നത് പ്രധാനമാണ്:

1. **സ്റ്റാൻഡേർഡൈസ്ഡ് കമ്മ്യൂണിക്കേഷൻ**: MCP JSON-RPC 2.0 അടിസ്ഥാനമാക്കി ഉപയോഗിക്കുന്നു, എല്ലാ നടപ്പാക്കലുകളിലും അഭ്യർത്ഥനകൾ, പ്രതികരണങ്ങൾ, പിശക് കൈകാര്യം ചെയ്യൽ എന്നിവയ്ക്ക് ഏകീകൃത ഫോർമാറ്റ് നൽകുന്നു.

2. **ഉപയോക്തൃകേന്ദ്രിത ഡിസൈൻ**: നിങ്ങളുടെ MCP നടപ്പാക്കലുകളിൽ എപ്പോഴും ഉപയോക്തൃ സമ്മതം, നിയന്ത്രണം, പാരദർശിത്വം മുൻഗണന നൽകുക.

3. **സുരക്ഷ ആദ്യം**: പ്രാമാണീകരണം, അധികാരനിർണ്ണയം, സാധുത പരിശോധന, നിരക്ക് നിയന്ത്രണം എന്നിവ ഉൾപ്പെടെയുള്ള ശക്തമായ സുരക്ഷാ നടപടികൾ നടപ്പിലാക്കുക.

4. **മൊഡുലാർ ആർക്കിടെക്ചർ**: ഓരോ ടൂളിനും റിസോഴ്‌സിനും വ്യക്തമായ, കേന്ദ്രീകൃത ലക്ഷ്യം ഉള്ള മൊഡുലാർ സമീപനം ഉപയോഗിച്ച് MCP സെർവറുകൾ രൂപകൽപ്പന ചെയ്യുക.

5. **സ്റ്റേറ്റ്‌ഫുൾ കണക്ഷനുകൾ**: കൂടുതൽ സുസ്ഥിരവും സാന്ദർഭ്യബോധമുള്ള ഇടപെടലുകൾക്കായി MCP-യുടെ സ്റ്റേറ്റ് നിലനിർത്താനുള്ള കഴിവ് ഉപയോഗിക്കുക.

## ഔദ്യോഗിക MCP മികച്ച പ്രാക്ടീസുകൾ

താഴെപ്പറയുന്ന മികച്ച പ്രാക്ടീസുകൾ ഔദ്യോഗിക മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ ഡോക്യുമെന്റേഷനിൽ നിന്നാണ് എടുത്തത്:

### സുരക്ഷാ മികച്ച പ്രാക്ടീസുകൾ

1. **ഉപയോക്തൃ സമ്മതവും നിയന്ത്രണവും**: ഡാറ്റ ആക്‌സസ് ചെയ്യുന്നതിന് മുമ്പും പ്രവർത്തനങ്ങൾ നടത്തുന്നതിന് മുമ്പും എപ്പോഴും വ്യക്തമായ ഉപയോക്തൃ സമ്മതം ആവശ്യമാണ്. പങ്കുവെക്കുന്ന ഡാറ്റയും അംഗീകൃത പ്രവർത്തനങ്ങളും വ്യക്തമായി നിയന്ത്രിക്കാൻ അവസരം നൽകുക.

2. **ഡാറ്റാ സ്വകാര്യത**: വ്യക്തമായ സമ്മതം ഉള്ള ഉപയോക്തൃ ഡാറ്റ മാത്രമേ പുറത്തുവിടാവൂ, അനുയോജ്യമായ ആക്‌സസ് നിയന്ത്രണങ്ങളാൽ സംരക്ഷിക്കുക. അനധികൃത ഡാറ്റ സംപ്രേഷണത്തിനെതിരെ സംരക്ഷണം ഉറപ്പാക്കുക.

3. **ടൂൾ സുരക്ഷ**: ഏതെങ്കിലും ടൂൾ വിളിക്കുമ്പോഴും വ്യക്തമായ ഉപയോക്തൃ സമ്മതം ആവശ്യമാണ്. ഓരോ ടൂളിന്റെയും പ്രവർത്തനം ഉപയോക്താക്കൾക്ക് മനസ്സിലാകുന്ന വിധം ഉറപ്പാക്കുകയും ശക്തമായ സുരക്ഷാ പരിധികൾ നടപ്പിലാക്കുകയും ചെയ്യുക.

4. **ടൂൾ അനുമതി നിയന്ത്രണം**: സെഷനിൽ മോഡലിന് ഉപയോഗിക്കാൻ അനുവദിച്ചിരിക്കുന്ന ടൂളുകൾ ക്രമീകരിക്കുക, വ്യക്തമായി അംഗീകൃത ടൂളുകൾക്ക് മാത്രമേ ആക്‌സസ് ലഭിക്കൂ.

5. **പ്രാമാണീകരണം**: API കീകൾ, OAuth ടോക്കണുകൾ, മറ്റ് സുരക്ഷിത പ്രാമാണീകരണ മാർഗങ്ങൾ ഉപയോഗിച്ച് ടൂളുകൾ, റിസോഴ്‌സുകൾ, സങ്കീർണ്ണ പ്രവർത്തനങ്ങൾ എന്നിവയ്ക്ക് ആക്‌സസ് നൽകുന്നതിന് മുമ്പ് ശരിയായ പ്രാമാണീകരണം ആവശ്യമാണ്.

6. **പാരാമീറ്റർ സാധുത പരിശോധന**: എല്ലാ ടൂൾ വിളിപ്പുകൾക്കും സാധുത പരിശോധന നിർബന്ധമാക്കി, തെറ്റായ അല്ലെങ്കിൽ ദുഷ്പ്രവർത്തനപരമായ ഇൻപുട്ടുകൾ ടൂൾ നടപ്പാക്കലിലേക്ക് എത്തുന്നത് തടയുക.

7. **നിരക്ക് നിയന്ത്രണം**: ദുരുപയോഗം തടയാനും സെർവർ റിസോഴ്‌സുകളുടെ നീതിപൂർവ്വമായ ഉപയോഗം ഉറപ്പാക്കാനും നിരക്ക് നിയന്ത്രണം നടപ്പിലാക്കുക.

### നടപ്പാക്കൽ മികച്ച പ്രാക്ടീസുകൾ

1. **ക്ഷമതാ ചർച്ച**: കണക്ഷൻ സജ്ജീകരണ സമയത്ത് പിന്തുണയുള്ള ഫീച്ചറുകൾ, പ്രോട്ടോക്കോൾ പതിപ്പുകൾ, ലഭ്യമായ ടൂളുകൾ, റിസോഴ്‌സുകൾ എന്നിവയെക്കുറിച്ച് വിവരങ്ങൾ കൈമാറുക.

2. **ടൂൾ ഡിസൈൻ**: ഒന്നുകിൽ നല്ല രീതിയിൽ ചെയ്യാൻ കഴിയുന്ന കേന്ദ്രീകൃത ടൂളുകൾ സൃഷ്ടിക്കുക, ബഹുമുഖ പ്രശ്നങ്ങൾ കൈകാര്യം ചെയ്യുന്ന വലിയ ടൂളുകൾ ഒഴിവാക്കുക.

3. **പിശക് കൈകാര്യം ചെയ്യൽ**: പ്രശ്നങ്ങൾ തിരിച്ചറിയാനും പരാജയങ്ങൾ സുഖപ്രദമായി കൈകാര്യം ചെയ്യാനും പ്രവർത്തനയോഗ്യമായ പ്രതികരണം നൽകാനും സഹായിക്കുന്ന സ്റ്റാൻഡേർഡൈസ്ഡ് പിശക് സന്ദേശങ്ങളും കോഡുകളും നടപ്പിലാക്കുക.

4. **ലോഗിംഗ്**: പ്രോട്ടോക്കോൾ ഇടപെടലുകൾ ഓഡിറ്റ് ചെയ്യാനും ഡീബഗ് ചെയ്യാനും നിരീക്ഷിക്കാനും ഘടനാപരമായ ലോഗുകൾ ക്രമീകരിക്കുക.

5. **പ്രോഗ്രസ് ട്രാക്കിംഗ്**: ദീർഘകാല പ്രവർത്തനങ്ങൾക്ക് പ്രോഗ്രസ് അപ്ഡേറ്റുകൾ റിപ്പോർട്ട് ചെയ്ത് പ്രതികരണശീലമുള്ള ഉപയോക്തൃ ഇന്റർഫേസുകൾ സജ്ജമാക്കുക.

6. **അഭ്യർത്ഥന റദ്ദാക്കൽ**: ഇനി ആവശ്യമില്ലാത്ത അല്ലെങ്കിൽ വളരെ സമയം എടുക്കുന്ന ഫ്ലൈറ്റ് അഭ്യർത്ഥനകൾ ക്ലയന്റുകൾ റദ്ദാക്കാൻ അനുവദിക്കുക.

## അധിക റഫറൻസുകൾ

MCP മികച്ച പ്രാക്ടീസുകളെക്കുറിച്ചുള്ള ഏറ്റവും പുതിയ വിവരങ്ങൾക്ക്, കാണുക:

- [MCP ഡോക്യുമെന്റേഷൻ](https://modelcontextprotocol.io/)
- [MCP സ്പെസിഫിക്കേഷൻ](https://spec.modelcontextprotocol.io/)
- [GitHub റിപോസിറ്ററി](https://github.com/modelcontextprotocol)
- [സുരക്ഷാ മികച്ച പ്രാക്ടീസുകൾ](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## പ്രായോഗിക നടപ്പാക്കൽ ഉദാഹരണങ്ങൾ

### ടൂൾ ഡിസൈൻ മികച്ച പ്രാക്ടീസുകൾ

#### 1. ഏകദൗത്യം സിദ്ധാന്തം

ഓരോ MCP ടൂളിനും വ്യക്തമായ, കേന്ദ്രീകൃത ലക്ഷ്യം ഉണ്ടായിരിക്കണം. ബഹുമുഖ പ്രശ്നങ്ങൾ കൈകാര്യം ചെയ്യാൻ ശ്രമിക്കുന്ന വലിയ ടൂളുകൾ സൃഷ്ടിക്കുന്നതിനുപകരം, പ്രത്യേക ജോലികളിൽ മികച്ച പ്രത്യേക ടൂളുകൾ വികസിപ്പിക്കുക.

```csharp
// A focused tool that does one thing well
public class WeatherForecastTool : ITool
{
    private readonly IWeatherService _weatherService;
    
    public WeatherForecastTool(IWeatherService weatherService)
    {
        _weatherService = weatherService;
    }
    
    public string Name => "weatherForecast";
    public string Description => "Gets weather forecast for a specific location";
    
    public ToolDefinition GetDefinition()
    {
        return new ToolDefinition
        {
            Name = Name,
            Description = Description,
            Parameters = new Dictionary<string, ParameterDefinition>
            {
                ["location"] = new ParameterDefinition
                {
                    Type = ParameterType.String,
                    Description = "City or location name"
                },
                ["days"] = new ParameterDefinition
                {
                    Type = ParameterType.Integer,
                    Description = "Number of forecast days",
                    Default = 3
                }
            },
            Required = new[] { "location" }
        };
    }
    
    public async Task<ToolResponse> ExecuteAsync(IDictionary<string, object> parameters)
    {
        var location = parameters["location"].ToString();
        var days = parameters.ContainsKey("days") 
            ? Convert.ToInt32(parameters["days"]) 
            : 3;
            
        var forecast = await _weatherService.GetForecastAsync(location, days);
        
        return new ToolResponse
        {
            Content = new List<ContentItem>
            {
                new TextContent(JsonSerializer.Serialize(forecast))
            }
        };
    }
}
```

#### 2. സ്ഥിരതയുള്ള പിശക് കൈകാര്യം ചെയ്യൽ

വിവരപ്രദമായ പിശക് സന്ദേശങ്ങളോടും അനുയോജ്യമായ പുനരുദ്ധാരണ സംവിധാനങ്ങളോടും കൂടിയ ശക്തമായ പിശക് കൈകാര്യം ചെയ്യൽ നടപ്പിലാക്കുക.

```python
# സമഗ്രമായ പിശക് കൈകാര്യം ചെയ്യലോടെയുള്ള പൈതൺ ഉദാഹരണം
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # പാരാമീറ്റർ പരിശോധന
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # സുരക്ഷാ പരിശോധന
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # ടൈംഔട്ടോടെയുള്ള ഡാറ്റാബേസ് പ്രവർത്തനം
                async with timeout(10):  # 10 സെക്കൻഡ് ടൈംഔട്ട്
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # കണക്ഷൻ പിശകുകൾ താൽക്കാലികമായിരിക്കാം
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # ക്വറി പിശകുകൾ സാധാരണയായി ക്ലയന്റ് പിശകുകളാണ്
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # ടൂൾ-നിർദ്ദിഷ്ട പിശകുകൾ കടക്കാൻ അനുവദിക്കുക
            raise
        except Exception as e:
            # അപ്രതീക്ഷിത പിശകുകൾക്കുള്ള കാച്ച്-ഓൾ
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL ഇൻജക്ഷൻ കണ്ടെത്തലിന്റെ നടപ്പാക്കൽ
        pass
        
    def _log_error(self, message, error):
        # പിശക് ലോഗിംഗ് നടപ്പാക്കൽ
        pass
```

#### 3. പാരാമീറ്റർ സാധുത പരിശോധന

തെറ്റായ അല്ലെങ്കിൽ ദുഷ്പ്രവർത്തനപരമായ ഇൻപുട്ടുകൾ തടയാൻ പാരാമീറ്ററുകൾ എപ്പോഴും പൂർണ്ണമായും പരിശോധിക്കുക.

```javascript
// വിശദമായ പാരാമീറ്റർ പരിശോധനയോടെയുള്ള ജാവാസ്ക്രിപ്റ്റ്/ടൈപ്പ്സ്ക്രിപ്റ്റ് ഉദാഹരണം
class FileOperationTool {
  getName() {
    return "fileOperation";
  }
  
  getDescription() {
    return "Performs file operations like read, write, and delete";
  }
  
  getDefinition() {
    return {
      name: this.getName(),
      description: this.getDescription(),
      parameters: {
        operation: {
          type: "string",
          description: "Operation to perform",
          enum: ["read", "write", "delete"]
        },
        path: {
          type: "string",
          description: "File path (must be within allowed directories)"
        },
        content: {
          type: "string",
          description: "Content to write (only for write operation)",
          optional: true
        }
      },
      required: ["operation", "path"]
    };
  }
  
  async execute(parameters) {
    // 1. പാരാമീറ്റർ സാന്നിധ്യം പരിശോധിക്കുക
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. പാരാമീറ്ററുകളുടെ തരം പരിശോധിക്കുക
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. പാരാമീറ്റർ മൂല്യങ്ങൾ പരിശോധിക്കുക
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. എഴുതൽ പ്രവർത്തനത്തിനായി ഉള്ളടക്ക സാന്നിധ്യം പരിശോധിക്കുക
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. പാതയുടെ സുരക്ഷാ പരിശോധന
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // പരിശോധനയുള്ള പാരാമീറ്ററുകളുടെ അടിസ്ഥാനത്തിൽ നടപ്പാക്കൽ
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // പാതയുടെ സുരക്ഷാ പരിശോധനയുടെ നടപ്പാക്കൽ
    // ...
  }
}
```

### സുരക്ഷാ നടപ്പാക്കൽ ഉദാഹരണങ്ങൾ

#### 1. പ്രാമാണീകരണവും അധികാരനിർണ്ണയവും

```java
// ഓതന്റിക്കേഷൻ ആൻഡ് ഓതറൈസേഷൻ ഉള്ള ജാവ ഉദാഹരണം
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // ഡിപ്പൻഡൻസി ഇൻജക്ഷൻ
    public SecureDataAccessTool(
            AuthenticationService authService,
            AuthorizationService authzService,
            DataService dataService) {
        this.authService = authService;
        this.authzService = authzService;
        this.dataService = dataService;
    }
    
    @Override
    public String getName() {
        return "secureDataAccess";
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        // 1. ഓതന്റിക്കേഷൻ കോൺടെക്സ്റ്റ് എക്സ്ട്രാക്റ്റ് ചെയ്യുക
        String authToken = request.getContext().getAuthToken();
        
        // 2. ഉപയോക്താവിനെ ഓതന്റിക്കേറ്റ് ചെയ്യുക
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. പ്രത്യേക പ്രവർത്തനത്തിന് ഓതറൈസേഷൻ പരിശോധിക്കുക
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. ഓതറൈസ്ഡ് പ്രവർത്തനത്തോടെ മുന്നോട്ട് പോവുക
        try {
            switch (operation) {
                case "read":
                    Object data = dataService.getData(dataId, user.getId());
                    return ToolResponse.success(data);
                case "update":
                    JsonNode newData = request.getParameters().get("newData");
                    dataService.updateData(dataId, newData, user.getId());
                    return ToolResponse.success("Data updated successfully");
                default:
                    return ToolResponse.error("Unsupported operation: " + operation);
            }
        } catch (Exception e) {
            return ToolResponse.error("Operation failed: " + e.getMessage());
        }
    }
}
```

#### 2. നിരക്ക് നിയന്ത്രണം

```csharp
// C# rate limiting implementation
public class RateLimitingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly IMemoryCache _cache;
    private readonly ILogger<RateLimitingMiddleware> _logger;
    
    // Configuration options
    private readonly int _maxRequestsPerMinute;
    
    public RateLimitingMiddleware(
        RequestDelegate next,
        IMemoryCache cache,
        ILogger<RateLimitingMiddleware> logger,
        IConfiguration config)
    {
        _next = next;
        _cache = cache;
        _logger = logger;
        _maxRequestsPerMinute = config.GetValue<int>("RateLimit:MaxRequestsPerMinute", 60);
    }
    
    public async Task InvokeAsync(HttpContext context)
    {
        // 1. Get client identifier (API key or user ID)
        string clientId = GetClientIdentifier(context);
        
        // 2. Get rate limiting key for this minute
        string cacheKey = $"rate_limit:{clientId}:{DateTime.UtcNow:yyyyMMddHHmm}";
        
        // 3. Check current request count
        if (!_cache.TryGetValue(cacheKey, out int requestCount))
        {
            requestCount = 0;
        }
        
        // 4. Enforce rate limit
        if (requestCount >= _maxRequestsPerMinute)
        {
            _logger.LogWarning("Rate limit exceeded for client {ClientId}", clientId);
            
            context.Response.StatusCode = StatusCodes.Status429TooManyRequests;
            context.Response.Headers.Add("Retry-After", "60");
            
            await context.Response.WriteAsJsonAsync(new
            {
                error = "Rate limit exceeded",
                message = "Too many requests. Please try again later.",
                retryAfterSeconds = 60
            });
            
            return;
        }
        
        // 5. Increment request count
        _cache.Set(cacheKey, requestCount + 1, TimeSpan.FromMinutes(2));
        
        // 6. Add rate limit headers
        context.Response.Headers.Add("X-RateLimit-Limit", _maxRequestsPerMinute.ToString());
        context.Response.Headers.Add("X-RateLimit-Remaining", (_maxRequestsPerMinute - requestCount - 1).ToString());
        
        // 7. Continue with the request
        await _next(context);
    }
    
    private string GetClientIdentifier(HttpContext context)
    {
        // Implementation to extract API key or user ID
        // ...
    }
}
```

## ടെസ്റ്റിംഗ് മികച്ച പ്രാക്ടീസുകൾ

### 1. MCP ടൂളുകളുടെ യൂണിറ്റ് ടെസ്റ്റിംഗ്

എല്ലാ ടൂളുകളും സ്വതന്ത്രമായി ടെസ്റ്റ് ചെയ്യുക, ബാഹ്യ ആശ്രിതങ്ങൾ മോക് ചെയ്യുക:

```typescript
// ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ് ടൂൾ യൂണിറ്റ് ടെസ്റ്റിന്റെ ഉദാഹരണം
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // ഒരു മോക് കാലാവസ്ഥ സേവനം സൃഷ്ടിക്കുക
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // മോക് ആശ്രിതത്വത്തോടെ ടൂൾ സൃഷ്ടിക്കുക
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // ക്രമീകരിക്കുക
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // പ്രവർത്തിക്കുക
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // ഉറപ്പാക്കുക
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // ക്രമീകരിക്കുക
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // പ്രവർത്തിക്കുകയും ഉറപ്പാക്കുകയും ചെയ്യുക
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. ഇന്റഗ്രേഷൻ ടെസ്റ്റിംഗ്

ക്ലയന്റ് അഭ്യർത്ഥനകളിൽ നിന്ന് സെർവർ പ്രതികരണങ്ങളിലേക്കുള്ള പൂർണ്ണ പ്രവാഹം ടെസ്റ്റ് ചെയ്യുക:

```python
# പൈതൺ ഇന്റഗ്രേഷൻ ടെസ്റ്റ് ഉദാഹരണം
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # ഒരു ടെസ്റ്റ് സെർവർ ആരംഭിക്കുക
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # ഒരു ക്ലയന്റ് സൃഷ്ടിക്കുക
        client = McpClient("http://localhost:5000")
        
        # ടൂൾ കണ്ടെത്തൽ പരിശോധിക്കുക
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # ടൂൾ പ്രവർത്തനം പരിശോധിക്കുക
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # പ്രതികരണം സ്ഥിരീകരിക്കുക
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # ശുചീകരണം നടത്തുക
        await server.stop()
```

## പ്രകടന മെച്ചപ്പെടുത്തൽ

### 1. കാഷിംഗ് തന്ത്രങ്ങൾ

വിലംബവും റിസോഴ്‌സ് ഉപയോഗവും കുറയ്ക്കാൻ അനുയോജ്യമായ കാഷിംഗ് നടപ്പിലാക്കുക:

```csharp
// C# example with caching
public class CachedWeatherTool : ITool
{
    private readonly IWeatherService _weatherService;
    private readonly IDistributedCache _cache;
    private readonly ILogger<CachedWeatherTool> _logger;
    
    public CachedWeatherTool(
        IWeatherService weatherService,
        IDistributedCache cache,
        ILogger<CachedWeatherTool> logger)
    {
        _weatherService = weatherService;
        _cache = cache;
        _logger = logger;
    }
    
    public string Name => "weatherForecast";
    
    public async Task<ToolResponse> ExecuteAsync(IDictionary<string, object> parameters)
    {
        var location = parameters["location"].ToString();
        var days = Convert.ToInt32(parameters.GetValueOrDefault("days", 3));
        
        // Create cache key
        string cacheKey = $"weather:{location}:{days}";
        
        // Try to get from cache
        string cachedForecast = await _cache.GetStringAsync(cacheKey);
        if (!string.IsNullOrEmpty(cachedForecast))
        {
            _logger.LogInformation("Cache hit for weather forecast: {Location}", location);
            return new ToolResponse
            {
                Content = new List<ContentItem>
                {
                    new TextContent(cachedForecast)
                }
            };
        }
        
        // Cache miss - get from service
        _logger.LogInformation("Cache miss for weather forecast: {Location}", location);
        var forecast = await _weatherService.GetForecastAsync(location, days);
        string forecastJson = JsonSerializer.Serialize(forecast);
        
        // Store in cache (weather forecasts valid for 1 hour)
        await _cache.SetStringAsync(
            cacheKey,
            forecastJson,
            new DistributedCacheEntryOptions
            {
                AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(1)
            });
        
        return new ToolResponse
        {
            Content = new List<ContentItem>
            {
                new TextContent(forecastJson)
            }
        };
    }
}
```

#### 2. ആശ്രിത ഇൻജക്ഷനും ടെസ്റ്റബിലിറ്റിയും

ടൂളുകൾ അവരുടെ ആശ്രിതങ്ങൾ കൺസ്ട്രക്ടർ ഇൻജക്ഷൻ വഴി സ്വീകരിക്കുന്ന വിധം രൂപകൽപ്പന ചെയ്യുക, ഇത് അവയെ ടെസ്റ്റബിളും ക്രമീകരണയോഗ്യവുമാക്കുന്നു:

```java
// ഡിപ്പൻഡൻസി ഇൻജക്ഷനോടുള്ള ജാവ ഉദാഹരണം
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // കൺസ്ട്രക്ടറിലൂടെ ഡിപ്പൻഡൻസികൾ ഇൻജക്ട് ചെയ്യുന്നു
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // ടൂൾ നടപ്പാക്കൽ
    // ...
}
```

#### 3. സംയോജ്യമായ ടൂളുകൾ

കൂടുതൽ സങ്കീർണ്ണ വർക്ക്‌ഫ്ലോകൾ സൃഷ്ടിക്കാൻ സംയോജ്യമായ ടൂളുകൾ രൂപകൽപ്പന ചെയ്യുക:

```python
# സംയോജ്യമായ ഉപകരണങ്ങൾ കാണിക്കുന്ന പൈത്തൺ ഉദാഹരണം
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # നടപ്പാക്കൽ...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # ഈ ഉപകരണം dataFetch ഉപകരണത്തിൽ നിന്നുള്ള ഫലങ്ങൾ ഉപയോഗിക്കാം
    async def execute_async(self, request):
        # നടപ്പാക്കൽ...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # ഈ ഉപകരണം dataAnalysis ഉപകരണത്തിൽ നിന്നുള്ള ഫലങ്ങൾ ഉപയോഗിക്കാം
    async def execute_async(self, request):
        # നടപ്പാക്കൽ...
        pass

# ഈ ഉപകരണങ്ങൾ സ്വതന്ത്രമായി അല്ലെങ്കിൽ ഒരു പ്രവൃത്തി പ്രവാഹത്തിന്റെ ഭാഗമായും ഉപയോഗിക്കാം
```

### സ്കീമ ഡിസൈൻ മികച്ച പ്രാക്ടീസുകൾ

സ്കീമ മോഡലിനും നിങ്ങളുടെ ടൂളിനും ഇടയിലുള്ള കരാറാണ്. നന്നായി രൂപകൽപ്പന ചെയ്ത സ്കീമകൾ മികച്ച ടൂൾ ഉപയോഗയോഗ്യതയ്ക്ക് വഴിയൊരുക്കുന്നു.

#### 1. വ്യക്തമായ പാരാമീറ്റർ വിവരണങ്ങൾ

ഓരോ പാരാമീറ്ററിനും വിവരണാത്മക വിവരങ്ങൾ എപ്പോഴും ഉൾപ്പെടുത്തുക:

```csharp
public object GetSchema()
{
    return new {
        type = "object",
        properties = new {
            query = new { 
                type = "string", 
                description = "Search query text. Use precise keywords for better results." 
            },
            filters = new {
                type = "object",
                description = "Optional filters to narrow down search results",
                properties = new {
                    dateRange = new { 
                        type = "string", 
                        description = "Date range in format YYYY-MM-DD:YYYY-MM-DD" 
                    },
                    category = new { 
                        type = "string", 
                        description = "Category name to filter by" 
                    }
                }
            },
            limit = new { 
                type = "integer", 
                description = "Maximum number of results to return (1-50)",
                default = 10
            }
        },
        required = new[] { "query" }
    };
}
```

#### 2. സാധുത പരിശോധന നിയന്ത്രണങ്ങൾ

അസാധുവായ ഇൻപുട്ടുകൾ തടയാൻ സാധുത പരിശോധന നിയന്ത്രണങ്ങൾ ഉൾപ്പെടുത്തുക:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // ഫോർമാറ്റ് സാധുതയുള്ള ഇമെയിൽ പ്രോപ്പർട്ടി
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // സംഖ്യാത്മക നിയന്ത്രണങ്ങളുള്ള പ്രായം പ്രോപ്പർട്ടി
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // എൻയുമറേറ്റഡ് പ്രോപ്പർട്ടി
    Map<String, Object> subscription = new HashMap<>();
    subscription.put("type", "string");
    subscription.put("enum", Arrays.asList("free", "basic", "premium"));
    subscription.put("default", "free");
    subscription.put("description", "Subscription tier");
    
    properties.put("email", email);
    properties.put("age", age);
    properties.put("subscription", subscription);
    
    schema.put("properties", properties);
    schema.put("required", Arrays.asList("email"));
    
    return schema;
}
```

#### 3. സ്ഥിരതയുള്ള പ്രതികരണ ഘടനകൾ

ഫലങ്ങൾ മോഡലുകൾക്ക് എളുപ്പത്തിൽ വ്യാഖ്യാനിക്കാൻ നിങ്ങളുടെ പ്രതികരണ ഘടനകളിൽ സ്ഥിരത പാലിക്കുക:

```python
async def execute_async(self, request):
    try:
        # അഭ്യർത്ഥന പ്രോസസ്സ് ചെയ്യുക
        results = await self._search_database(request.parameters["query"])
        
        # എപ്പോഴും സ്ഥിരമായ ഘടന മടക്കുക
        return ToolResponse(
            result={
                "matches": [self._format_item(item) for item in results],
                "totalCount": len(results),
                "queryTime": calculation_time_ms,
                "status": "success"
            }
        )
    except Exception as e:
        return ToolResponse(
            result={
                "matches": [],
                "totalCount": 0,
                "queryTime": 0,
                "status": "error",
                "error": str(e)
            }
        )
    
def _format_item(self, item):
    """Ensures each item has a consistent structure"""
    return {
        "id": item.id,
        "title": item.title,
        "summary": item.summary[:100] + "..." if len(item.summary) > 100 else item.summary,
        "url": item.url,
        "relevance": item.score
    }
```

### പിശക് കൈകാര്യം ചെയ്യൽ

MCP ടൂളുകൾ വിശ്വാസ്യത നിലനിർത്താൻ ശക്തമായ പിശക് കൈകാര്യം ചെയ്യൽ അനിവാര്യമാണ്.

#### 1. സുഖപ്രദമായ പിശക് കൈകാര്യം ചെയ്യൽ

ശരിയായ തലങ്ങളിൽ പിശകുകൾ കൈകാര്യം ചെയ്ത് വിവരപ്രദമായ സന്ദേശങ്ങൾ നൽകുക:

```csharp
public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
{
    try
    {
        string fileId = request.Parameters.GetProperty("fileId").GetString();
        
        try
        {
            var fileData = await _fileService.GetFileAsync(fileId);
            return new ToolResponse { 
                Result = JsonSerializer.SerializeToElement(fileData) 
            };
        }
        catch (FileNotFoundException)
        {
            throw new ToolExecutionException($"File not found: {fileId}");
        }
        catch (UnauthorizedAccessException)
        {
            throw new ToolExecutionException("You don't have permission to access this file");
        }
        catch (Exception ex) when (ex is IOException || ex is TimeoutException)
        {
            _logger.LogError(ex, "Error accessing file {FileId}", fileId);
            throw new ToolExecutionException("Error accessing file: The service is temporarily unavailable");
        }
    }
    catch (JsonException)
    {
        throw new ToolExecutionException("Invalid file ID format");
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Unexpected error in FileAccessTool");
        throw new ToolExecutionException("An unexpected error occurred");
    }
}
```

#### 2. ഘടനാപരമായ പിശക് പ്രതികരണങ്ങൾ

സാധ്യമായപ്പോൾ ഘടനാപരമായ പിശക് വിവരങ്ങൾ തിരിച്ചയക്കുക:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // നടപ്പാക്കല്‍
    } catch (Exception ex) {
        Map<String, Object> errorResult = new HashMap<>();
        
        errorResult.put("success", false);
        
        if (ex instanceof ValidationException) {
            ValidationException validationEx = (ValidationException) ex;
            
            errorResult.put("errorType", "validation");
            errorResult.put("errorMessage", validationEx.getMessage());
            errorResult.put("validationErrors", validationEx.getErrors());
            
            return new ToolResponse.Builder()
                .setResult(errorResult)
                .build();
        }
        
        // മറ്റ് ഒഴിവാക്കലുകള്‍ ToolExecutionException ആയി വീണ്ടും എറിഞ്ഞു
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. പുനരുദ്ധാരണ തന്ത്രം

താൽക്കാലിക പരാജയങ്ങൾക്ക് അനുയോജ്യമായ പുനരുദ്ധാരണ തന്ത്രങ്ങൾ നടപ്പിലാക്കുക:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # സെക്കൻഡുകൾ
    
    while retry_count < max_retries:
        try:
            # ബാഹ്യ API വിളിക്കുക
            return await self._call_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # ഘാതക തിരിച്ചടി
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # താൽക്കാലികമല്ലാത്ത പിശക്, വീണ്ടും ശ്രമിക്കരുത്
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### പ്രകടന മെച്ചപ്പെടുത്തൽ

#### 1. കാഷിംഗ്

വിലപ്പെട്ട പ്രവർത്തനങ്ങൾക്ക് കാഷിംഗ് നടപ്പിലാക്കുക:

```csharp
public class CachedDataTool : IMcpTool
{
    private readonly IDatabase _database;
    private readonly IMemoryCache _cache;
    
    public CachedDataTool(IDatabase database, IMemoryCache cache)
    {
        _database = database;
        _cache = cache;
    }
    
    public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
    {
        var query = request.Parameters.GetProperty("query").GetString();
        
        // Create cache key based on parameters
        var cacheKey = $"data_query_{ComputeHash(query)}";
        
        // Try to get from cache first
        if (_cache.TryGetValue(cacheKey, out var cachedResult))
        {
            return new ToolResponse { Result = cachedResult };
        }
        
        // Cache miss - perform actual query
        var result = await _database.QueryAsync(query);
        
        // Store in cache with expiration
        var cacheOptions = new MemoryCacheEntryOptions()
            .SetAbsoluteExpiration(TimeSpan.FromMinutes(15));
            
        _cache.Set(cacheKey, JsonSerializer.SerializeToElement(result), cacheOptions);
        
        return new ToolResponse { Result = JsonSerializer.SerializeToElement(result) };
    }
    
    private string ComputeHash(string input)
    {
        // Implementation to generate stable hash for cache key
    }
}
```

#### 2. അസിങ്ക്രണസ് പ്രോസസ്സിംഗ്

I/O-ബന്ധിത പ്രവർത്തനങ്ങൾക്ക് അസിങ്ക്രണസ് പ്രോഗ്രാമിംഗ് മാതൃകകൾ ഉപയോഗിക്കുക:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // ദൈർഘ്യമേറിയ പ്രവർത്തനങ്ങൾക്ക്, പ്രോസസ്സിംഗ് ഐഡി ഉടൻ തിരിച്ചുകിട്ടുക
        String processId = UUID.randomUUID().toString();
        
        // അസിങ്ക്രൺ പ്രോസസ്സിംഗ് ആരംഭിക്കുക
        CompletableFuture.runAsync(() -> {
            try {
                // ദൈർഘ്യമേറിയ പ്രവർത്തനം നടത്തുക
                documentService.processDocument(documentId);
                
                // നില അപ്ഡേറ്റ് ചെയ്യുക (സാധാരണയായി ഡാറ്റാബേസിൽ സൂക്ഷിക്കും)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // പ്രോസസ് ഐഡിയോടുകൂടിയ ഉടൻ പ്രതികരണം നൽകുക
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // കൂട്ടുകാരൻ നില പരിശോധിക്കൽ ഉപകരണം
    public class ProcessStatusTool implements Tool {
        @Override
        public ToolResponse execute(ToolRequest request) {
            String processId = request.getParameters().get("processId").asText();
            ProcessStatus status = processStatusRepository.getStatus(processId);
            
            return new ToolResponse.Builder().setResult(status).build();
        }
    }
}
```

#### 3. റിസോഴ്‌സ് ത്രോട്ട്ലിംഗ്

ഓവർലോഡ് തടയാൻ റിസോഴ്‌സ് ത്രോട്ട്ലിംഗ് നടപ്പിലാക്കുക:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # സെക്കൻഡിൽ 5 അഭ്യർത്ഥനകൾ അനുവദിക്കുക
            bucket_size=10        # 10 അഭ്യർത്ഥനകളിലേക്കുള്ള ബർസ്റ്റ് അനുവദിക്കുക
        )
    
    async def execute_async(self, request):
        # നാം മുന്നോട്ട് പോകാമോ അല്ലെങ്കിൽ കാത്തിരിക്കേണ്ടതുണ്ടോ എന്ന് പരിശോധിക്കുക
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # കാത്തിരിപ്പ് വളരെ നീണ്ടുനിൽക്കുകയാണെങ്കിൽ
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # അനുയോജ്യമായ വൈകിപ്പിക്കൽ സമയം കാത്തിരിക്കുക
                await asyncio.sleep(delay)
        
        # ഒരു ടോക്കൺ ഉപയോഗിച്ച് അഭ്യർത്ഥന മുന്നോട്ട് കൊണ്ടുപോകുക
        self.rate_limiter.consume()
        
        # API വിളിക്കുക
        result = await self._call_api(request.parameters)
        return ToolResponse(result=result)

class TokenBucketRateLimiter:
    def __init__(self, tokens_per_second, bucket_size):
        self.tokens_per_second = tokens_per_second
        self.bucket_size = bucket_size
        self.tokens = bucket_size
        self.last_refill = time.time()
        self.lock = asyncio.Lock()
    
    async def get_delay_time(self):
        async with self.lock:
            self._refill()
            if self.tokens >= 1:
                return 0
            
            # അടുത്ത ടോക്കൺ ലഭ്യമാകുന്നതുവരെ സമയം കണക്കാക്കുക
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # കഴിഞ്ഞ സമയത്തിന്റെ അടിസ്ഥാനത്തിൽ പുതിയ ടോക്കണുകൾ ചേർക്കുക
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### സുരക്ഷാ മികച്ച പ്രാക്ടീസുകൾ

#### 1. ഇൻപുട്ട് സാധുത പരിശോധന

എപ്പോഴും ഇൻപുട്ട് പാരാമീറ്ററുകൾ പൂർണ്ണമായും പരിശോധിക്കുക:

```csharp
public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
{
    // Validate parameters exist
    if (!request.Parameters.TryGetProperty("query", out var queryProp))
    {
        throw new ToolExecutionException("Missing required parameter: query");
    }
    
    // Validate correct type
    if (queryProp.ValueKind != JsonValueKind.String)
    {
        throw new ToolExecutionException("Query parameter must be a string");
    }
    
    var query = queryProp.GetString();
    
    // Validate string content
    if (string.IsNullOrWhiteSpace(query))
    {
        throw new ToolExecutionException("Query parameter cannot be empty");
    }
    
    if (query.Length > 500)
    {
        throw new ToolExecutionException("Query parameter exceeds maximum length of 500 characters");
    }
    
    // Check for SQL injection attacks if applicable
    if (ContainsSqlInjection(query))
    {
        throw new ToolExecutionException("Invalid query: contains potentially unsafe SQL");
    }
    
    // Proceed with execution
    // ...
}
```

#### 2. അധികാര പരിശോധനകൾ

ശരിയായ അധികാര പരിശോധനകൾ നടപ്പിലാക്കുക:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // അഭ്യർത്ഥനയിൽ നിന്ന് ഉപയോക്തൃ സാന്ദർഭ്യം നേടുക
    UserContext user = request.getContext().getUserContext();
    
    // ഉപയോക്താവിന് ആവശ്യമായ അനുമതികൾ ഉണ്ടോ എന്ന് പരിശോധിക്കുക
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // പ്രത്യേക വിഭവങ്ങൾക്കായി, ആ വിഭവത്തിലേക്കുള്ള പ്രവേശനം പരിശോധിക്കുക
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // ഉപകരണം പ്രവർത്തനത്തിലേക്ക് മുന്നോട്ട് പോവുക
    // ...
}
```

#### 3. സങ്കീർണ്ണ ഡാറ്റ കൈകാര്യം ചെയ്യൽ

സങ്കീർണ്ണ ഡാറ്റ ശ്രദ്ധാപൂർവ്വം കൈകാര്യം ചെയ്യുക:

```python
class SecureDataTool(Tool):
    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "userId": {"type": "string"},
                "includeSensitiveData": {"type": "boolean", "default": False}
            },
            "required": ["userId"]
        }
    
    async def execute_async(self, request):
        user_id = request.parameters["userId"]
        include_sensitive = request.parameters.get("includeSensitiveData", False)
        
        # ഉപയോക്തൃ ഡാറ്റ നേടുക
        user_data = await self.user_service.get_user_data(user_id)
        
        # വ്യക്തമായി അഭ്യർത്ഥിക്കപ്പെട്ടും അനുമതിയുള്ളതുമായില്ലെങ്കിൽ സങ്കീർണ്ണമായ ഫീൽഡുകൾ ഫിൽട്ടർ ചെയ്യുക
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # അഭ്യർത്ഥനാ സാന്ദർഭ്യത്തിൽ അനുമതി നില പരിശോധിക്കുക
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # യഥാർത്ഥം മാറ്റം വരുത്താതിരിക്കാൻ ഒരു പകർപ്പ് സൃഷ്ടിക്കുക
        redacted = user_data.copy()
        
        # പ്രത്യേക സങ്കീർണ്ണ ഫീൽഡുകൾ മറയ്ക്കുക
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # നസ്റ്റ് ചെയ്ത സങ്കീർണ്ണ ഡാറ്റ മറയ്ക്കുക
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP ടൂളുകൾക്കുള്ള ടെസ്റ്റിംഗ് മികച്ച പ്രാക്ടീസുകൾ

സമഗ്രമായ ടെസ്റ്റിംഗ് MCP ടൂളുകൾ ശരിയായി പ്രവർത്തിക്കുന്നുവെന്ന്, അതിരുകൾ കൈകാര്യം ചെയ്യുന്നതും, സിസ്റ്റത്തിന്റെ ബാക്കി ഭാഗങ്ങളുമായി ശരിയായി സംയോജിപ്പിക്കുന്നതും ഉറപ്പാക്കുന്നു.

### യൂണിറ്റ് ടെസ്റ്റിംഗ്

#### 1. ഓരോ ടൂളും സ്വതന്ത്രമായി ടെസ്റ്റ് ചെയ്യുക

ഓരോ ടൂളിന്റെയും പ്രവർത്തനക്ഷമതയ്ക്ക് കേന്ദ്രീകൃതമായ ടെസ്റ്റുകൾ സൃഷ്ടിക്കുക:

```csharp
[Fact]
public async Task WeatherTool_ValidLocation_ReturnsCorrectForecast()
{
    // Arrange
    var mockWeatherService = new Mock<IWeatherService>();
    mockWeatherService
        .Setup(s => s.GetForecastAsync("Seattle", 3))
        .ReturnsAsync(new WeatherForecast(/* test data */));
    
    var tool = new WeatherForecastTool(mockWeatherService.Object);
    
    var request = new ToolRequest(
        toolName: "weatherForecast",
        parameters: JsonSerializer.SerializeToElement(new { 
            location = "Seattle", 
            days = 3 
        })
    );
    
    // Act
    var response = await tool.ExecuteAsync(request);
    
    // Assert
    Assert.NotNull(response);
    var result = JsonSerializer.Deserialize<WeatherForecast>(response.Result);
    Assert.Equal("Seattle", result.Location);
    Assert.Equal(3, result.DailyForecasts.Count);
}

[Fact]
public async Task WeatherTool_InvalidLocation_ThrowsToolExecutionException()
{
    // Arrange
    var mockWeatherService = new Mock<IWeatherService>();
    mockWeatherService
        .Setup(s => s.GetForecastAsync("InvalidLocation", It.IsAny<int>()))
        .ThrowsAsync(new LocationNotFoundException("Location not found"));
    
    var tool = new WeatherForecastTool(mockWeatherService.Object);
    
    var request = new ToolRequest(
        toolName: "weatherForecast",
        parameters: JsonSerializer.SerializeToElement(new { 
            location = "InvalidLocation", 
            days = 3 
        })
    );
    
    // Act & Assert
    var exception = await Assert.ThrowsAsync<ToolExecutionException>(
        () => tool.ExecuteAsync(request)
    );
    
    Assert.Contains("Location not found", exception.Message);
}
```

#### 2. സ്കീമ സാധുത പരിശോധന ടെസ്റ്റിംഗ്

സ്കീമകൾ സാധുവാണെന്നും നിയന്ത്രണങ്ങൾ ശരിയായി നടപ്പിലാക്കുന്നുവെന്നും ടെസ്റ്റ് ചെയ്യുക:

```java
@Test
public void testSchemaValidation() {
    // ടൂൾ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
    SearchTool searchTool = new SearchTool();
    
    // സ്കീമ നേടുക
    Object schema = searchTool.getSchema();
    
    // സാധൂകരിക്കലിനായി സ്കീമ JSON ആയി മാറ്റുക
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // സ്കീമ സാധുവായ JSONSchema ആണെന്ന് പരിശോധിക്കുക
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // സാധുവായ പാരാമീറ്ററുകൾ പരിശോധിക്കുക
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // ആവശ്യമായ പാരാമീറ്റർ കാണാതായത് പരിശോധിക്കുക
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // അസാധുവായ പാരാമീറ്റർ തരം പരിശോധിക്കുക
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. പിശക് കൈകാര്യം ചെയ്യൽ ടെസ്റ്റുകൾ

പിശക് സാഹചര്യങ്ങൾക്ക് പ്രത്യേക ടെസ്റ്റുകൾ സൃഷ്ടിക്കുക:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # ക്രമീകരിക്കുക
    tool = ApiTool(timeout=0.1)  # വളരെ ചെറു ടൈംഔട്ട്
    
    # ടൈംഔട്ട് സംഭവിക്കുന്ന ഒരു അഭ്യർത്ഥന മോക് ചെയ്യുക
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # ടൈംഔട്ടിനേക്കാൾ നീളം
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # പ്രവർത്തിക്കുക & സ്ഥിരീകരിക്കുക
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # എക്സെപ്ഷൻ സന്ദേശം സ്ഥിരീകരിക്കുക
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # ക്രമീകരിക്കുക
    tool = ApiTool()
    
    # നിരക്ക്-പരിമിതമായ പ്രതികരണം മോക് ചെയ്യുക
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            status=429,
            headers={"Retry-After": "2"},
            body=json.dumps({"error": "Rate limit exceeded"})
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # പ്രവർത്തിക്കുക & സ്ഥിരീകരിക്കുക
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # എക്സെപ്ഷൻ നിരക്ക് പരിധി വിവരങ്ങൾ ഉൾക്കൊള്ളുന്നതായി സ്ഥിരീകരിക്കുക
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### ഇന്റഗ്രേഷൻ ടെസ്റ്റിംഗ്

#### 1. ടൂൾ ചെയിൻ ടെസ്റ്റിംഗ്

പ്രതീക്ഷിക്കുന്ന സംയോജനങ്ങളിൽ ടൂളുകൾ ചേർന്ന് പ്രവർത്തിക്കുന്നുണ്ടോ എന്ന് ടെസ്റ്റ് ചെയ്യുക:

```csharp
[Fact]
public async Task DataProcessingWorkflow_CompletesSuccessfully()
{
    // Arrange
    var dataFetchTool = new DataFetchTool(mockDataService.Object);
    var analysisTools = new DataAnalysisTool(mockAnalysisService.Object);
    var visualizationTool = new DataVisualizationTool(mockVisualizationService.Object);
    
    var toolRegistry = new ToolRegistry();
    toolRegistry.RegisterTool(dataFetchTool);
    toolRegistry.RegisterTool(analysisTools);
    toolRegistry.RegisterTool(visualizationTool);
    
    var workflowExecutor = new WorkflowExecutor(toolRegistry);
    
    // Act
    var result = await workflowExecutor.ExecuteWorkflowAsync(new[] {
        new ToolCall("dataFetch", new { source = "sales2023" }),
        new ToolCall("dataAnalysis", ctx => new { 
            data = ctx.GetResult("dataFetch"),
            analysis = "trend" 
        }),
        new ToolCall("dataVisualize", ctx => new {
            analysisResult = ctx.GetResult("dataAnalysis"),
            type = "line-chart"
        })
    });
    
    // Assert
    Assert.NotNull(result);
    Assert.True(result.Success);
    Assert.NotNull(result.GetResult("dataVisualize"));
    Assert.Contains("chartUrl", result.GetResult("dataVisualize").ToString());
}
```

#### 2. MCP സെർവർ ടെസ്റ്റിംഗ്

പൂർണ്ണ ടൂൾ രജിസ്ട്രേഷൻ, നിർവഹണത്തോടെ MCP സെർവർ ടെസ്റ്റ് ചെയ്യുക:

```java
@SpringBootTest
@AutoConfigureMockMvc
public class McpServerIntegrationTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @Autowired
    private ObjectMapper objectMapper;
    
    @Test
    public void testToolDiscovery() throws Exception {
        // ഡിസ്കവറി എന്റ്പോയിന്റ് പരിശോധന ചെയ്യുക
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // ടൂൾ അഭ്യർത്ഥന സൃഷ്ടിക്കുക
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // അഭ്യർത്ഥന അയച്ച് പ്രതികരണം സ്ഥിരീകരിക്കുക
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // അസാധുവായ ടൂൾ അഭ്യർത്ഥന സൃഷ്ടിക്കുക
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // "b" എന്ന പാരാമീറ്റർ കാണുന്നില്ല
        request.put("parameters", parameters);
        
        // അഭ്യർത്ഥന അയച്ച് പിശക് പ്രതികരണം സ്ഥിരീകരിക്കുക
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. എന്റ്-ടു-എന്റ് ടെസ്റ്റിംഗ്

മോഡൽ പ്രോംപ്റ്റിൽ നിന്ന് ടൂൾ നിർവഹണത്തിലേക്കുള്ള പൂർണ്ണ വർക്ക്‌ഫ്ലോകൾ ടെസ്റ്റ് ചെയ്യുക:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # ക്രമീകരിക്കുക - MCP ക്ലയന്റ് സജ്ജമാക്കുക, മോക്ക് മോഡൽ സജ്ജീകരിക്കുക
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # മോക്ക് മോഡൽ പ്രതികരണങ്ങൾ
    mock_model = MockLanguageModel([
        MockResponse(
            "What's the weather in Seattle?",
            tool_calls=[{
                "tool_name": "weatherForecast",
                "parameters": {"location": "Seattle", "days": 3}
            }]
        ),
        MockResponse(
            "Here's the weather forecast for Seattle:\n- Today: 65°F, Partly Cloudy\n- Tomorrow: 68°F, Sunny\n- Day after: 62°F, Rain",
            tool_calls=[]
        )
    ])
    
    # മോക്ക് കാലാവസ്ഥ ഉപകരണ പ്രതികരണം
    with aioresponses() as mocked:
        mocked.post(
            "http://localhost:5000/mcp/execute",
            payload={
                "result": {
                    "location": "Seattle",
                    "forecast": [
                        {"date": "2023-06-01", "temperature": 65, "conditions": "Partly Cloudy"},
                        {"date": "2023-06-02", "temperature": 68, "conditions": "Sunny"},
                        {"date": "2023-06-03", "temperature": 62, "conditions": "Rain"}
                    ]
                }
            }
        )
        
        # പ്രവർത്തിക്കുക
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # ഉറപ്പാക്കുക
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### പ്രകടന ടെസ്റ്റിംഗ്

#### 1. ലോഡ് ടെസ്റ്റിംഗ്

നിങ്ങളുടെ MCP സെർവർ എത്ര സമകാലിക അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാൻ കഴിയും എന്ന് ടെസ്റ്റ് ചെയ്യുക:

```csharp
[Fact]
public async Task McpServer_HandlesHighConcurrency()
{
    // Arrange
    var server = new McpServer(
        name: "TestServer",
        version: "1.0",
        maxConcurrentRequests: 100
    );
    
    server.RegisterTool(new FastExecutingTool());
    await server.StartAsync();
    
    var client = new McpClient("http://localhost:5000");
    
    // Act
    var tasks = new List<Task<McpResponse>>();
    for (int i = 0; i < 1000; i++)
    {
        tasks.Add(client.ExecuteToolAsync("fastTool", new { iteration = i }));
    }
    
    var results = await Task.WhenAll(tasks);
    
    // Assert
    Assert.Equal(1000, results.Length);
    Assert.All(results, r => Assert.NotNull(r));
}
```

#### 2. സ്ട്രെസ് ടെസ്റ്റിംഗ്

അത്യധികം ലോഡിൽ സിസ്റ്റം എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് ടെസ്റ്റ് ചെയ്യുക:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // സ്ട്രെസ് ടെസ്റ്റിംഗിനായി JMeter സജ്ജമാക്കുക
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // JMeter ടെസ്റ്റ് പ്ലാൻ കോൺഫിഗർ ചെയ്യുക
    HashTree testPlanTree = new HashTree();
    
    // ടെസ്റ്റ് പ്ലാൻ, ത്രെഡ് ഗ്രൂപ്പ്, സാമ്പ്ലറുകൾ എന്നിവ സൃഷ്ടിക്കുക
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // ടൂൾ എക്സിക്യൂഷനിനായി HTTP സാമ്പ്ലർ ചേർക്കുക
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // ലിസണറുകൾ ചേർക്കുക
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // ടെസ്റ്റ് നടത്തുക
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // ഫലങ്ങൾ സാധൂകരിക്കുക
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // ശരാശരി പ്രതികരണ സമയം < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90-ാം ശതമാനം < 500ms
}
```

#### 3. നിരീക്ഷണവും പ്രൊഫൈലിംഗും

ദീർഘകാല പ്രകടന വിശകലനത്തിനായി നിരീക്ഷണം സജ്ജമാക്കുക:

```python
# ഒരു MCP സെർവറിനായി നിരീക്ഷണം ക്രമീകരിക്കുക
def configure_monitoring(server):
    # പ്രോമീഥിയസ് മെട്രിക്‌സുകൾ സജ്ജമാക്കുക
    prometheus_metrics = {
        "request_count": Counter("mcp_requests_total", "Total MCP requests"),
        "request_latency": Histogram(
            "mcp_request_duration_seconds", 
            "Request duration in seconds",
            buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
        ),
        "tool_execution_count": Counter(
            "mcp_tool_executions_total", 
            "Tool execution count",
            labelnames=["tool_name"]
        ),
        "tool_execution_latency": Histogram(
            "mcp_tool_duration_seconds", 
            "Tool execution duration in seconds",
            labelnames=["tool_name"],
            buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
        ),
        "tool_errors": Counter(
            "mcp_tool_errors_total",
            "Tool execution errors",
            labelnames=["tool_name", "error_type"]
        )
    }
    
    # സമയമെടുക്കലിനും മെട്രിക്‌സ് രേഖപ്പെടുത്തലിനും മിഡിൽവെയർ ചേർക്കുക
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # മെട്രിക്‌സ് എന്റ്പോയിന്റ് പ്രദർശിപ്പിക്കുക
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP വർക്ക്‌ഫ്ലോ ഡിസൈൻ മാതൃകകൾ

നന്നായി രൂപകൽപ്പന ചെയ്ത MCP വർക്ക്‌ഫ്ലോകൾ കാര്യക്ഷമത, വിശ്വാസ്യത, പരിപാലനക്ഷമത മെച്ചപ്പെടുത്തുന്നു. പാലിക്കേണ്ട പ്രധാന മാതൃകകൾ:

### 1. ടൂളുകളുടെ ചെയിൻ മാതൃക

ഒരൊറ്റ ടൂളിന്റെ ഔട്ട്പുട്ട് അടുത്ത ടൂളിന്റെ ഇൻപുട്ടായി മാറുന്ന വിധം നിരവധി ടൂളുകൾ പരമ്പരയായി ബന്ധിപ്പിക്കുക:

```python
# പൈത്തൺ ചെയിൻ ഓഫ് ടൂൾസ് നടപ്പാക്കൽ
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # ക്രമത്തിൽ പ്രവർത്തിപ്പിക്കാൻ ടൂൾ നാമങ്ങളുടെ പട്ടിക
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # ചെയിനിലുള്ള ഓരോ ടൂളും മുൻഫലങ്ങൾ പാസ്സാക്കി പ്രവർത്തിപ്പിക്കുക
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # ഫലം സൂക്ഷിച്ച് അടുത്ത ടൂളിന്റെ ഇൻപുട്ടായി ഉപയോഗിക്കുക
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# ഉദാഹരണ ഉപയോഗം
data_processing_chain = ChainWorkflow([
    "dataFetch",
    "dataCleaner",
    "dataAnalyzer",
    "dataVisualizer"
])

result = await data_processing_chain.execute(
    mcp_client,
    {"source": "sales_database", "table": "transactions"}
)
```

### 2. ഡിസ്പാച്ചർ മാതൃക

ഇൻപുട്ട് അടിസ്ഥാനമാക്കി പ്രത്യേക ടൂളുകളിലേക്ക് ഡിസ്പാച്ച് ചെയ്യുന്ന കേന്ദ്ര ടൂൾ ഉപയോഗിക്കുക:

```csharp
public class ContentDispatcherTool : IMcpTool
{
    private readonly IMcpClient _mcpClient;
    
    public ContentDispatcherTool(IMcpClient mcpClient)
    {
        _mcpClient = mcpClient;
    }
    
    public string Name => "contentProcessor";
    public string Description => "Processes content of various types";
    
    public object GetSchema()
    {
        return new {
            type = "object",
            properties = new {
                content = new { type = "string" },
                contentType = new { 
                    type = "string",
                    enum = new[] { "text", "html", "markdown", "csv", "code" }
                },
                operation = new { 
                    type = "string",
                    enum = new[] { "summarize", "analyze", "extract", "convert" }
                }
            },
            required = new[] { "content", "contentType", "operation" }
        };
    }
    
    public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
    {
        var content = request.Parameters.GetProperty("content").GetString();
        var contentType = request.Parameters.GetProperty("contentType").GetString();
        var operation = request.Parameters.GetProperty("operation").GetString();
        
        // Determine which specialized tool to use
        string targetTool = DetermineTargetTool(contentType, operation);
        
        // Forward to the specialized tool
        var specializedResponse = await _mcpClient.ExecuteToolAsync(
            targetTool,
            new { content, options = GetOptionsForTool(targetTool, operation) }
        );
        
        return new ToolResponse { Result = specializedResponse.Result };
    }
    
    private string DetermineTargetTool(string contentType, string operation)
    {
        return (contentType, operation) switch
        {
            ("text", "summarize") => "textSummarizer",
            ("text", "analyze") => "textAnalyzer",
            ("html", _) => "htmlProcessor",
            ("markdown", _) => "markdownProcessor",
            ("csv", _) => "csvProcessor",
            ("code", _) => "codeAnalyzer",
            _ => throw new ToolExecutionException($"No tool available for {contentType}/{operation}")
        };
    }
    
    private object GetOptionsForTool(string toolName, string operation)
    {
        // Return appropriate options for each specialized tool
        return toolName switch
        {
            "textSummarizer" => new { length = "medium" },
            "htmlProcessor" => new { cleanUp = true, operation },
            // Options for other tools...
            _ => new { }
        };
    }
}
```

### 3. സമാന്തര പ്രോസസ്സിംഗ് മാതൃക

കാര്യക്ഷമതയ്ക്കായി ഒരേസമയം നിരവധി ടൂളുകൾ പ്രവർത്തിപ്പിക്കുക:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // ഘട്ടം 1: ഡാറ്റാസെറ്റ് മെറ്റാഡേറ്റാ (സിങ്ക്രോണസ്) എടുക്കുക
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // ഘട്ടം 2: ഒരേ സമയം പല വിശകലനങ്ങളും ആരംഭിക്കുക
        CompletableFuture<ToolResponse> statisticalAnalysis = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("statisticalAnalysis", Map.of(
                "datasetId", datasetId,
                "type", "comprehensive"
            ))
        );
        
        CompletableFuture<ToolResponse> correlationAnalysis = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("correlationAnalysis", Map.of(
                "datasetId", datasetId,
                "method", "pearson"
            ))
        );
        
        CompletableFuture<ToolResponse> outlierDetection = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("outlierDetection", Map.of(
                "datasetId", datasetId,
                "sensitivity", "medium"
            ))
        );
        
        // എല്ലാ സമാന്തര ടാസ്കുകളും പൂർത്തിയാകുന്നത് വരെ കാത്തിരിക്കുക
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // പൂർത്തീകരണം വരെ കാത്തിരിക്കുക
        
        // ഘട്ടം 3: ഫലങ്ങൾ സംയോജിപ്പിക്കുക
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // ഘട്ടം 4: സംക്ഷിപ്ത റിപ്പോർട്ട് സൃഷ്ടിക്കുക
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // പൂർണ്ണ വർക്ക്‌ഫ്ലോ ഫലം തിരികെ നൽകുക
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. പിശക് പുനരുദ്ധാരണ മാതൃക

ടൂൾ പരാജയങ്ങൾക്ക് സുഖപ്രദമായ ഫാൾബാക്കുകൾ നടപ്പിലാക്കുക:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # ആദ്യം പ്രാഥമിക ഉപകരണം പരീക്ഷിക്കുക
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # പരാജയം ലോഗ് ചെയ്യുക
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # ദ്വിതീയ ഉപകരണത്തിലേക്ക് മടങ്ങുക
            try:
                # മടങ്ങിവരുന്ന ഉപകരണത്തിന് പാരാമീറ്ററുകൾ മാറ്റേണ്ടതുണ്ടാകാം
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # ഇരുവരും പരാജയപ്പെട്ടു
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # ഈ നടപ്പാക്കൽ പ്രത്യേക ഉപകരണങ്ങളിലേതായി ആശ്രയിക്കും
        # ഈ ഉദാഹരണത്തിന്, നാം മൗലിക പാരാമീറ്ററുകൾ മടങ്ങി നൽകും
        return params

# ഉദാഹരണ ഉപയോഗം
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # പ്രാഥമിക (പണം നൽകുന്ന) കാലാവസ്ഥ API
        "basicWeatherService",    # മടങ്ങിവരുന്ന (സൗജന്യ) കാലാവസ്ഥ API
        {"location": location}
    )
```

### 5. വർക്ക്‌ഫ്ലോ സംയോജനം മാതൃക

സരളമായ വർക്ക്‌ഫ്ലോകൾ സംയോജിപ്പിച്ച് സങ്കീർണ്ണ വർക്ക്‌ഫ്ലോകൾ നിർമ്മിക്കുക:

```csharp
public class CompositeWorkflow : IWorkflow
{
    private readonly List<IWorkflow> _workflows;
    
    public CompositeWorkflow(IEnumerable<IWorkflow> workflows)
    {
        _workflows = new List<IWorkflow>(workflows);
    }
    
    public async Task<WorkflowResult> ExecuteAsync(WorkflowContext context)
    {
        var results = new Dictionary<string, object>();
        
        foreach (var workflow in _workflows)
        {
            var workflowResult = await workflow.ExecuteAsync(context);
            
            // Store each workflow's result
            results[workflow.Name] = workflowResult;
            
            // Update context with the result for the next workflow
            context = context.WithResult(workflow.Name, workflowResult);
        }
        
        return new WorkflowResult(results);
    }
    
    public string Name => "CompositeWorkflow";
    public string Description => "Executes multiple workflows in sequence";
}

// Example usage
var documentWorkflow = new CompositeWorkflow(new IWorkflow[] {
    new DocumentFetchWorkflow(),
    new DocumentProcessingWorkflow(),
    new InsightGenerationWorkflow(),
    new ReportGenerationWorkflow()
});

var result = await documentWorkflow.ExecuteAsync(new WorkflowContext {
    Parameters = new { documentId = "12345" }
});
```

# MCP സെർവറുകളുടെ ടെസ്റ്റിംഗ്: മികച്ച പ്രാക്ടീസുകളും പ്രധാന ടിപ്പുകളും

## അവലോകനം

വിശ്വാസയോഗ്യവും ഉയർന്ന ഗുണമേന്മയുള്ള MCP സെർവറുകൾ വികസിപ്പിക്കുന്നതിൽ ടെസ്റ്റിംഗ് നിർണായകമാണ്. യൂണിറ്റ് ടെസ്റ്റുകളിൽ നിന്ന് ഇന്റഗ്രേഷൻ ടെസ്റ്റുകൾ, എന്റ്-ടു-എന്റ് പരിശോധന വരെ വികസന ജീവിതചക്രത്തിൽ MCP സെർവറുകൾ ടെസ്റ്റ് ചെയ്യുന്നതിനുള്ള സമഗ്രമായ മികച്ച പ്രാക്ടീസുകളും ടിപ്പുകളും ഈ ഗൈഡ് നൽകുന്നു.

## MCP സെർവറുകൾക്കുള്ള ടെസ്റ്റിംഗ് എന്തുകൊണ്ട് പ്രധാനമാണ്

MCP സെർവറുകൾ AI മോഡലുകളുടെയും ക്ലയന്റ് ആപ്ലിക്കേഷനുകളുടെയും ഇടയിലെ നിർണായക മിഡിൽവെയർ ആയി പ്രവർത്തിക്കുന്നു. സമഗ്രമായ ടെസ്റ്റിംഗ് ഉറപ്പാക്കുന്നു:

- പ്രൊഡക്ഷൻ പരിസ്ഥിതികളിൽ വിശ്വാസ്യത
- അഭ്യർത്ഥനകളും പ്രതികരണങ്ങളും ശരിയായി കൈകാര്യം ചെയ്യൽ
- MCP സ്പെസിഫിക്കേഷനുകളുടെ ശരിയായ നടപ്പാക്കൽ
- പരാജയങ്ങളും അതിരുകളും നേരിടാനുള്ള പ്രതിരോധശേഷി
- വ്യത്യസ്ത ലോഡുകളിൽ സ്ഥിരതയുള്ള പ്രകടനം

## MCP സെർവറ
```yaml
name: MCP Server Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Runtime
      uses: actions/setup-dotnet@v1
      with:
        dotnet-version: '8.0.x'
    
    - name: Restore dependencies
      run: dotnet restore
    
    - name: Build
      run: dotnet build --no-restore
    
    - name: Unit Tests
      run: dotnet test --no-build --filter Category=Unit
    
    - name: Integration Tests
      run: dotnet test --no-build --filter Category=Integration
      
    - name: Performance Tests
      run: dotnet run --project tests/PerformanceTests/PerformanceTests.csproj
```

## MCP സ്പെസിഫിക്കേഷനുമായി അനുസൃതിയുള്ളതായുള്ള പരിശോധന

നിങ്ങളുടെ സെർവർ MCP സ്പെസിഫിക്കേഷൻ ശരിയായി നടപ്പിലാക്കുന്നുണ്ടോ എന്ന് സ്ഥിരീകരിക്കുക.

### പ്രധാന അനുസരണ മേഖലകൾ

1. **API എന്റ്പോയിന്റുകൾ**: ആവശ്യമായ എന്റ്പോയിന്റുകൾ (/resources, /tools, മുതലായവ) പരിശോധിക്കുക
2. **റിക്വസ്റ്റ്/റസ്പോൺസ് ഫോർമാറ്റ്**: സ്കീമ അനുസരണ പരിശോധന നടത്തുക
3. **എറർ കോഡുകൾ**: വിവിധ സാഹചര്യങ്ങൾക്ക് ശരിയായ സ്റ്റാറ്റസ് കോഡുകൾ പരിശോധിക്കുക
4. **കണ്ടന്റ് ടൈപ്പുകൾ**: വ്യത്യസ്ത കണ്ടന്റ് ടൈപ്പുകൾ കൈകാര്യം ചെയ്യുന്നത് പരിശോധിക്കുക
5. **ഓതന്റിക്കേഷൻ ഫ്ലോ**: സ്പെക് അനുസൃതമായ ഓത mechanisms പരിശോധിക്കുക

### അനുസരണ പരിശോധന സ്യൂട്ട്

```csharp
[Fact]
public async Task Server_ResourceEndpoint_ReturnsCorrectSchema()
{
    // Arrange
    var client = new HttpClient();
    client.DefaultRequestHeaders.Add("Authorization", "Bearer test-token");
    
    // Act
    var response = await client.GetAsync("http://localhost:5000/api/resources");
    var content = await response.Content.ReadAsStringAsync();
    var resources = JsonSerializer.Deserialize<ResourceList>(content);
    
    // Assert
    Assert.Equal(HttpStatusCode.OK, response.StatusCode);
    Assert.NotNull(resources);
    Assert.All(resources.Resources, resource => 
    {
        Assert.NotNull(resource.Id);
        Assert.NotNull(resource.Type);
        // Additional schema validation
    });
}
```

## ഫലപ്രദമായ MCP സെർവർ പരിശോധനയ്ക്കുള്ള ടോപ്പ് 10 ടിപ്പുകൾ

1. **ടൂൾ നിർവചനങ്ങൾ വേർതിരിച്ച് പരിശോധിക്കുക**: ടൂൾ ലജിക് മുതൽ സ്വതന്ത്രമായി സ്കീമ നിർവചനങ്ങൾ പരിശോധിക്കുക
2. **പാരാമീറ്ററൈസ്ഡ് ടെസ്റ്റുകൾ ഉപയോഗിക്കുക**: വിവിധ ഇൻപുട്ടുകളോടെ, അതിൽ എഡ്ജ് കേസുകളും ഉൾപ്പെടെ, ടൂളുകൾ പരിശോധിക്കുക
3. **എറർ റസ്പോൺസുകൾ പരിശോധിക്കുക**: എല്ലാ സാധ്യതയുള്ള എറർ സാഹചര്യങ്ങൾക്കും ശരിയായ എറർ കൈകാര്യം ചെയ്യൽ ഉറപ്പാക്കുക
4. **അധികാര പരിശോധനാ ലജിക് പരിശോധിക്കുക**: വ്യത്യസ്ത ഉപയോക്തൃ റോളുകൾക്കുള്ള ശരിയായ ആക്സസ് നിയന്ത്രണം ഉറപ്പാക്കുക
5. **ടെസ്റ്റ് കവറേജ് നിരീക്ഷിക്കുക**: പ്രധാന പാത കോഡിന്റെ ഉയർന്ന കവറേജ് ലക്ഷ്യമിടുക
6. **സ്റ്റ്രീമിംഗ് റസ്പോൺസുകൾ പരിശോധിക്കുക**: സ്റ്റ്രീമിംഗ് കണ്ടന്റ് ശരിയായി കൈകാര്യം ചെയ്യുന്നത് പരിശോധിക്കുക
7. **നെറ്റ്‌വർക്ക് പ്രശ്നങ്ങൾ സിമുലേറ്റ് ചെയ്യുക**: മോശം നെറ്റ്‌വർക്ക് സാഹചര്യങ്ങളിൽ പെരുമാറ്റം പരിശോധിക്കുക
8. **റിസോഴ്‌സ് പരിധികൾ പരിശോധിക്കുക**: ക്വോട്ടകൾ അല്ലെങ്കിൽ റേറ്റ് ലിമിറ്റുകൾ എത്തുമ്പോൾ പെരുമാറ്റം പരിശോധിക്കുക
9. **റിഗ്രഷൻ ടെസ്റ്റുകൾ ഓട്ടോമേറ്റ് ചെയ്യുക**: ഓരോ കോഡ് മാറ്റത്തിനും ഓടുന്ന ഒരു സ്യൂട്ട് നിർമ്മിക്കുക
10. **ടെസ്റ്റ് കേസുകൾ രേഖപ്പെടുത്തുക**: ടെസ്റ്റ് സീനാരിയോകളുടെ വ്യക്തമായ രേഖകൾ സൂക്ഷിക്കുക

## സാധാരണ പരിശോധന പിഴവുകൾ

- **സന്തോഷകരമായ പാത പരിശോധനയിൽ അധികം ആശ്രയം**: എറർ കേസുകൾ പൂർണ്ണമായി പരിശോധിക്കുക
- **പ്രകടന പരിശോധന അവഗണിക്കൽ**: പ്രൊഡക്ഷനിൽ ബാധിക്കുന്ന മുൻപ് ബോട്ടിൽനെക്കുകൾ കണ്ടെത്തുക
- **ഒറ്റയ്ക്ക് മാത്രം പരിശോധന**: യൂണിറ്റ്, ഇന്റഗ്രേഷൻ, E2E ടെസ്റ്റുകൾ സംയോജിപ്പിക്കുക
- **അപൂർണ്ണ API കവറേജ്**: എല്ലാ എന്റ്പോയിന്റുകളും ഫീച്ചറുകളും പരിശോധിക്കുക
- **അസമതുല്യമായ ടെസ്റ്റ് പരിസ്ഥിതികൾ**: സ്ഥിരതയുള്ള ടെസ്റ്റ് പരിസ്ഥിതികൾ ഉറപ്പാക്കാൻ കണ്ടെയ്‌നറുകൾ ഉപയോഗിക്കുക

## നിഗമനം

വിശ്വാസയോഗ്യവും ഉയർന്ന ഗുണമേന്മയുള്ള MCP സെർവർ വികസനത്തിന് സമഗ്രമായ പരിശോധന തന്ത്രം അനിവാര്യമാണ്. ഈ ഗൈഡിൽ വിശദീകരിച്ച മികച്ച പ്രാക്ടീസുകളും ടിപ്പുകളും നടപ്പിലാക്കുന്നതിലൂടെ, നിങ്ങളുടെ MCP നടപ്പാക്കലുകൾ ഉയർന്ന നിലവാരവും വിശ്വാസ്യതയും പ്രകടനവും ഉറപ്പാക്കും.

## പ്രധാന പഠനങ്ങൾ

1. **ടൂൾ ഡിസൈൻ**: ഏക ഉത്തരവാദിത്വ സിദ്ധാന്തം പാലിക്കുക, ഡിപ്പൻഡൻസി ഇൻജക്ഷൻ ഉപയോഗിക്കുക, കോംപോസബിലിറ്റിക്ക് രൂപകൽപ്പന ചെയ്യുക
2. **സ്കീമ ഡിസൈൻ**: വ്യക്തമായ, നന്നായി രേഖപ്പെടുത്തിയ സ്കീമകൾ ശരിയായ പരിശോധനാ നിയന്ത്രണങ്ങളോടെ സൃഷ്ടിക്കുക
3. **എറർ കൈകാര്യം ചെയ്യൽ**: സുന്ദരമായ എറർ കൈകാര്യം ചെയ്യൽ, ഘടനാപരമായ എറർ റസ്പോൺസുകൾ, റിട്രൈ ലജിക് നടപ്പിലാക്കുക
4. **പ്രകടനം**: കാഷിംഗ്, അസിങ്ക്രണസ് പ്രോസസ്സിംഗ്, റിസോഴ്‌സ് ത്രോട്ട്ലിംഗ് ഉപയോഗിക്കുക
5. **സുരക്ഷ**: സമഗ്രമായ ഇൻപുട്ട് പരിശോധന, അധികാര പരിശോധനകൾ, സენსിറ്റീവ് ഡാറ്റ കൈകാര്യം ചെയ്യൽ പ്രയോഗിക്കുക
6. **പരിശോധന**: സമഗ്രമായ യൂണിറ്റ്, ഇന്റഗ്രേഷൻ, എന്റ്-ടു-എന്റ് ടെസ്റ്റുകൾ സൃഷ്ടിക്കുക
7. **വർക്ക്‌ഫ്ലോ പാറ്റേണുകൾ**: ചെയിൻസ്, ഡിസ്പാച്ചേഴ്സ്, പാരലൽ പ്രോസസ്സിംഗ് പോലുള്ള സ്ഥാപിത പാറ്റേണുകൾ പ്രയോഗിക്കുക

## അഭ്യാസം

ഒരു ഡോക്യുമെന്റ് പ്രോസസ്സിംഗ് സിസ്റ്റത്തിനായി MCP ടൂൾയും വർക്ക്‌ഫ്ലോയും രൂപകൽപ്പന ചെയ്യുക, അത്:

1. വിവിധ ഫോർമാറ്റുകളിൽ (PDF, DOCX, TXT) ഡോക്യുമെന്റുകൾ സ്വീകരിക്കുന്നു
2. ഡോക്യുമെന്റുകളിൽ നിന്ന് ടെക്സ്റ്റും പ്രധാന വിവരങ്ങളും എടുക്കുന്നു
3. ഡോക്യുമെന്റുകൾ തരം, ഉള്ളടക്കം അനുസരിച്ച് വർഗ്ഗീകരിക്കുന്നു
4. ഓരോ ഡോക്യുമെന്റിന്റെയും സംക്ഷേപം സൃഷ്ടിക്കുന്നു

ടൂൾ സ്കീമകൾ, എറർ കൈകാര്യം ചെയ്യൽ, ഈ സീനാരിയോയുമായി ഏറ്റവും അനുയോജ്യമായ വർക്ക്‌ഫ്ലോ പാറ്റേൺ നടപ്പിലാക്കുക. ഈ നടപ്പാക്കൽ എങ്ങനെ പരിശോധിക്കാമെന്ന് പരിഗണിക്കുക.

## വിഭവങ്ങൾ

1. ഏറ്റവും പുതിയ വികസനങ്ങളെക്കുറിച്ച് അറിയാൻ [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) എന്ന MCP കമ്മ്യൂണിറ്റിയിൽ ചേരുക
2. ഓപ്പൺ-സോഴ്‌സ് [MCP പ്രോജക്ടുകൾ](https://github.com/modelcontextprotocol) ൽ സംഭാവന നൽകുക
3. നിങ്ങളുടെ സ്ഥാപനത്തിന്റെ AI സംരംഭങ്ങളിൽ MCP സിദ്ധാന്തങ്ങൾ പ്രയോഗിക്കുക
4. നിങ്ങളുടെ വ്യവസായത്തിനായി പ്രത്യേക MCP നടപ്പാക്കലുകൾ അന്വേഷിക്കുക
5. മൾട്ടി-മോഡൽ ഇന്റഗ്രേഷൻ അല്ലെങ്കിൽ എന്റർപ്രൈസ് ആപ്ലിക്കേഷൻ ഇന്റഗ്രേഷൻ പോലുള്ള പ്രത്യേക MCP വിഷയങ്ങളിൽ ഉയർന്ന തല കോഴ്സുകൾ പരിഗണിക്കുക
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) വഴി പഠിച്ച സിദ്ധാന്തങ്ങൾ ഉപയോഗിച്ച് നിങ്ങളുടെ സ്വന്തം MCP ടൂളുകളും വർക്ക്‌ഫ്ലോകളും നിർമ്മിച്ച് പരീക്ഷിക്കുക

അടുത്തത്: മികച്ച പ്രാക്ടീസുകൾ [കേസ് സ്റ്റഡികൾ](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->