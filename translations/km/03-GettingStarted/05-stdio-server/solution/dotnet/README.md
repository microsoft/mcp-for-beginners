# MCP stdio Server - ដំណោះស្រាយ .NET

> **⚠️ សំខាន់**: ដំណោះស្រាយនេះត្រូវបានធ្វើបច្ចុប្បន្នភាពឱ្យប្រើ **stdio transport** ដូចបានផ្តល់អនុសាសន៍ដោយ MCP Specification 2025-06-18។ របៀប SSE ដើមត្រូវបានផ្អាក។

## ទិដ្ឋភាពទូទៅ

ដំណោះស្រាយ .NET នេះបង្ហាញរបៀបបង្កើតម៉ាស៊ីនបម្រើ MCP ដោយប្រើ stdio transport បច្ចុប្បន្ន។ stdio transport ងាយស្រួលជាង មានសុវត្ថិភាពខ្ពស់ជាង ហើយផ្តល់នូវសមត្ថភាពល្អជាងរបៀប SSE ដែលបានផ្អាក។

## ការត្រូវមានមុន

- .NET 9.0 SDK ឬកំណែចុងក្រោយជាងនេះ
- ការយល់ដឹងមូលដ្ឋានអំពីការ dependency injection ក្នុង .NET

## សេចក្ដីណែនាំការតំឡើង

### ជំហានទី 1: ត្រឡប់ dependencies

```bash
dotnet restore
```

### ជំហានទី 2: សង់គម្រោង

```bash
dotnet build
```

## រត់ម៉ាស៊ីនបម្រើ

ម៉ាស៊ីនបម្រើ stdio រត់ខុសពីម៉ាស៊ីនបម្រើ HTTP ជាមុន។ វាមិនចាប់ផ្តើមម៉ាស៊ីនបម្រើវេបទេ ប៉ុន្តែទំនាក់ទំនងតាមរយៈ stdin/stdout៖

```bash
dotnet run
```

**សំខាន់**: ម៉ាស៊ីនបម្រើនឹងមើលទៅដូចជាអ្នករំពឹងរង់ចាំ - នេះគឺស្របតាមធម្មតា! វាកំពុងរង់ចាំសារ JSON-RPC មកពី stdin ។

## សាកល្បងម៉ាស៊ីនបម្រើ

### វិធីសាស្ត្រ ១៖ ប្រើ MCP Inspector (ផ្តល់អនុសាសន៍)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

នេះនឹង:
1. ចាប់ផ្តើមម៉ាស៊ីនបម្រើរបស់អ្នកជាដំណើរការជាគន្លងក្រោម
2. បើកផ្ទាំងបង្ហាញវេបសម្រាប់សាកល្បង
3. អនុញ្ញាតឱ្យអ្នកសាកល្បងឧបករណ៍ម៉ាស៊ីនបម្រើទាំងអស់ដោយអន្តរកម្ម

### វិធីសាស្ត្រ ២៖ សាកល្បងតាមបញ្ជារបញ្ជាโดยផ្ទាល់

អ្នកអាចសាកល្បងដោយចាប់ផ្តើម Inspector ដោយផ្ទាល់:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### ឧបករណ៍ដែលមាន

ម៉ាស៊ីនបម្រើផ្តល់ឧបករណ៍ដូចខាងក្រោម៖

- **AddNumbers(a, b)**: បូកលេខពីរជាមួយគ្នា
- **MultiplyNumbers(a, b)**: គុណលេខពីរជាមួយគ្នា  
- **GetGreeting(name)**: បង្កើតសូរសើមផ្ទាល់ខ្លួន
- **GetServerInfo()**: ទទួលព័ត៌មានអំពីម៉ាស៊ីនបម្រើ

### សាកល្បងជាមួយ Claude Desktop

ដើម្បីប្រើម៉ាស៊ីនបម្រើនេះជាមួយ Claude Desktop សូមបញ្ចូលការកំណត់នេះក្នុង `claude_desktop_config.json` របស់អ្នក៖

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## រចនាសម្ព័ន្ធគម្រោង

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## ផ្សេងគ្នាសំខាន់ៗពី HTTP/SSE

**stdio transport (បច្ចុប្បន្ន):**
- ✅ ការតំឡើងងាយស្រួល - មិនចាំបាច់មានម៉ាស៊ីនបម្រើវេប
- ✅ សុវត្ថិភាពខ្ពស់ជាង - គ្មានច្រក HTTP
- ✅ ប្រើ `Host.CreateApplicationBuilder()` ជំនួស `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` ជំនួស `WithHttpTransport()`
- ✅ កម្មវិធី console ជំនួសកម្មវិធីវេប
- ✅ មានសមត្ថភាពល្អជាង

**HTTP/SSE transport (បានផ្អាក):**
- ❌ តម្រូវម៉ាស៊ីនបម្រើ ASP.NET Core វេប
- ❌ តម្រូវការកំណត់ផ្លូវ `app.MapMcp()`
- ❌ ការកំណត់ស្មុគស្មាញ និងការពឹងផ្អែកច្រើន
- ❌ ការពិចារណាសុវត្ថិភាពបន្ថែម
- ❌ ឥឡូវនេះបានផ្អាកក្នុង MCP 2025-06-18

## លក្ខណៈពិសេសក្នុងការអភិវឌ្ឍន៍

- **Dependency Injection**: គាំទ្រពេញលេញចំពោះសេវាកម្ម និងការចុះបញ្ជីlogger
- **Structured Logging**: ការចុះបញ្ជីloggerហើយទៅ stderr ដោយប្រើ `ILogger<T>`
- **Tool Attributes**: ការកំណត់ឧបករណ៍ស្អាតដោយប្រើ attribute `[McpServerTool]`
- **Async Support**: ឧបករណ៍ទាំងអស់គាំទ្រការធ្វើការជាអសង្ខេប (async)
- **Error Handling**: ការដោះស្រាយកំហុសយ៉ាងមានអានុភាព និងការចុះបញ្ជីlogger

## គន្លឹះអភិវឌ្ឍន៍

- ប្រើ `ILogger` សម្រាប់ចុះបញ្ជីlogger (កុំសរសេរទៅ stdout តាមផ្ទាល់)
- សង់បង្កើតជាមួយ `dotnet build` មុនសាកល្បង
- សាកល្បងជាមួយ Inspector សម្រាប់រៀបរាប់កំហុសដោយម្ដង់ផ្លូវ
- ការចុះបញ្ជីloggerទាំងអស់ទៅ stderr ដោយស្វ័យប្រវត្តិ
- ម៉ាស៊ីនបម្រើគ្រប់គ្រងសញ្ញាដើម្បីបិទយ៉ាងប្រកបដោយអានុភាព

ដំណោះស្រាយនេះតាមដានការបញ្ជាក់ MCP បច្ចុប្បន្ន ហើយបង្ហាញជំនាញល្អបំផុតសម្រាប់ការអនុវត្ត stdio transport ដោយប្រើ .NET ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រព័ន្ធបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារមូលដ្ឋានក្នុងភាសាដើមគួរត្រូវបានគេរាប់អានថាជាភាសារដ្ឋបាលដែលត្រឹមត្រូវ។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->