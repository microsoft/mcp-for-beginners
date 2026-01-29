# MCP stdio Server - Soluție .NET

> **⚠️ Important**: Această soluție a fost actualizată pentru a utiliza **transportul stdio**, conform recomandărilor din Specificația MCP 2025-06-18. Transportul SSE original a fost depreciat.

## Prezentare generală

Această soluție .NET demonstrează cum să construiești un server MCP folosind transportul stdio actual. Transportul stdio este mai simplu, mai sigur și oferă performanțe mai bune decât abordarea SSE depreciată.

## Cerințe preliminare

- SDK .NET 9.0 sau o versiune mai recentă
- Înțelegere de bază a injecției de dependențe în .NET

## Instrucțiuni de configurare

### Pasul 1: Restaurează dependențele

```bash
dotnet restore
```

### Pasul 2: Construiește proiectul

```bash
dotnet build
```

## Rularea serverului

Serverul stdio funcționează diferit față de vechiul server bazat pe HTTP. În loc să pornească un server web, acesta comunică prin stdin/stdout:

```bash
dotnet run
```

**Important**: Serverul va părea că s-a blocat - acest lucru este normal! Așteaptă mesaje JSON-RPC de la stdin.

## Testarea serverului

### Metoda 1: Utilizarea MCP Inspector (Recomandată)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Aceasta va:
1. Lansa serverul tău ca un subproces
2. Deschide o interfață web pentru testare
3. Permite testarea interactivă a tuturor uneltelor serverului

### Metoda 2: Testare directă din linia de comandă

Poți testa și lansând Inspectorul direct:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Unelte disponibile

Serverul oferă următoarele unelte:

- **AddNumbers(a, b)**: Adună două numere
- **MultiplyNumbers(a, b)**: Înmulțește două numere  
- **GetGreeting(name)**: Generează un mesaj de salut personalizat
- **GetServerInfo()**: Oferă informații despre server

### Testarea cu Claude Desktop

Pentru a utiliza acest server cu Claude Desktop, adaugă această configurație în fișierul `claude_desktop_config.json`:

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

## Structura proiectului

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Diferențe cheie față de HTTP/SSE

**Transport stdio (Actual):**
- ✅ Configurare mai simplă - nu este necesar un server web
- ✅ Securitate mai bună - fără endpoint-uri HTTP
- ✅ Utilizează `Host.CreateApplicationBuilder()` în loc de `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` în loc de `WithHttpTransport()`
- ✅ Aplicație de consolă în loc de aplicație web
- ✅ Performanță mai bună

**Transport HTTP/SSE (Depreciat):**
- ❌ Necesita un server web ASP.NET Core
- ❌ Necesita configurarea rutării `app.MapMcp()`
- ❌ Configurare și dependențe mai complexe
- ❌ Considerații suplimentare de securitate
- ❌ Acum depreciat în MCP 2025-06-18

## Funcționalități pentru dezvoltare

- **Injecție de dependențe**: Suport complet pentru servicii și logare
- **Logare structurată**: Logare corectă către stderr folosind `ILogger<T>`
- **Atribute pentru unelte**: Definire curată a uneltelor folosind atributele `[McpServerTool]`
- **Suport pentru operații asincrone**: Toate uneltele suportă operații asincrone
- **Gestionarea erorilor**: Gestionare grațioasă a erorilor și logare

## Sfaturi pentru dezvoltare

- Utilizează `ILogger` pentru logare (nu scrie direct în stdout)
- Construiește proiectul cu `dotnet build` înainte de testare
- Testează cu Inspector pentru depanare vizuală
- Toată logarea este direcționată automat către stderr
- Serverul gestionează semnalele de închidere grațioasă

Această soluție urmează specificația actuală MCP și demonstrează cele mai bune practici pentru implementarea transportului stdio folosind .NET.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.