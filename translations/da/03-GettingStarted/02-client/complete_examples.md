# Komplette MCP-klienteksempler

Denne mappe indeholder komplette, fungerende eksempler på MCP-klienter i forskellige programmeringssprog. Hver klient demonstrerer den fulde funktionalitet, der er beskrevet i hovedvejledningen README.md.

## Tilgængelige klienter

### 1. Java-klient (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) over HTTP
- **Målserver**: `http://localhost:8080`
- **Funktioner**:
  - Oprettelse af forbindelse og ping
  - Liste over værktøjer
  - Regnefunktioner (plus, minus, gange, dividere, hjælp)
  - Fejlhåndtering og resultatudtrækning

**Sådan køres:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C#-klient (`client_example_csharp.cs`)

- **Transport**: Stdio (Standard Input/Output)
- **Målserver**: Lokal .NET MCP-server via dotnet run
- **Funktioner**:
  - Automatisk serverstart via stdio-transport
  - Liste over værktøjer og ressourcer
  - Regnefunktioner
  - JSON-resultatparsing
  - Omfattende fejlhåndtering

**Sådan køres:**

```bash
dotnet run
```

### 3. TypeScript-klient (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Input/Output)
- **Målserver**: Lokal Node.js MCP-server
- **Funktioner**:
  - Fuld MCP-protokolunderstøttelse
  - Værktøjs-, ressource- og promptoperationer
  - Regnefunktioner
  - Læsning af ressourcer og udførelse af prompts
  - Robust fejlhåndtering

**Sådan køres:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python-klient (`client_example_python.py`)

- **Transport**: Stdio (Standard Input/Output)  
- **Målserver**: Lokal Python MCP-server
- **Funktioner**:
  - Async/await-mønster til operationer
  - Opdagelse af værktøjer og ressourcer
  - Test af regnefunktioner
  - Læsning af ressourceindhold
  - Klassebaseret organisering

**Sådan køres:**

```bash
python client_example_python.py
```

## Fælles funktioner på tværs af alle klienter

Hver klientimplementering demonstrerer:

1. **Forbindelseshåndtering**
   - Oprettelse af forbindelse til MCP-serveren
   - Håndtering af forbindelsesfejl
   - Korrekt oprydning og ressourcehåndtering

2. **Serveropdagelse**
   - Liste over tilgængelige værktøjer
   - Liste over tilgængelige ressourcer (hvor understøttet)
   - Liste over tilgængelige prompts (hvor understøttet)

3. **Værktøjsanvendelse**
   - Grundlæggende regnefunktioner (plus, minus, gange, dividere)
   - Hjælpekommando for serverinformation
   - Korrekt argumentoverførsel og resultathåndtering

4. **Fejlhåndtering**
   - Forbindelsesfejl
   - Fejl ved værktøjsudførelse
   - Graciøs fejlhåndtering og brugerfeedback

5. **Resultatbehandling**
   - Udtrækning af tekstindhold fra svar
   - Formatering af output for læsbarhed
   - Håndtering af forskellige svarformater

## Forudsætninger

Før du kører disse klienter, skal du sikre dig:

1. **Den tilsvarende MCP-server kører** (fra `../01-first-server/`)
2. **Nødvendige afhængigheder er installeret** for det valgte sprog
3. **Korrekt netværksforbindelse** (for HTTP-baserede transporter)

## Vigtige forskelle mellem implementeringer

| Sprog      | Transport | Serverstart    | Async-model | Nøglebiblioteker    |
|------------|-----------|----------------|-------------|---------------------|
| Java       | SSE/HTTP  | Ekstern        | Synkron     | WebFlux, MCP SDK    |
| C#         | Stdio     | Automatisk     | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Automatisk     | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Automatisk     | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Automatisk     | Async/Await | Rust MCP SDK, Tokio |

## Næste skridt

Efter at have udforsket disse klienteksempler:

1. **Tilpas klienterne** for at tilføje nye funktioner eller operationer
2. **Opret din egen server** og test den med disse klienter
3. **Eksperimentér med forskellige transporter** (SSE vs. Stdio)
4. **Byg en mere kompleks applikation** der integrerer MCP-funktionalitet

## Fejlfinding

### Almindelige problemer

1. **Forbindelse nægtet**: Sørg for, at MCP-serveren kører på den forventede port/sti
2. **Modul ikke fundet**: Installer det nødvendige MCP SDK for dit sprog
3. **Adgang nægtet**: Tjek filrettigheder for stdio-transport
4. **Værktøj ikke fundet**: Bekræft, at serveren implementerer de forventede værktøjer

### Debug-tips

1. **Aktivér detaljeret logning** i dit MCP SDK
2. **Tjek serverlogfiler** for fejlmeddelelser
3. **Bekræft værktøjsnavne og signaturer** stemmer overens mellem klient og server
4. **Test med MCP Inspector** først for at validere serverfunktionalitet

## Relateret dokumentation

- [Hovedvejledning til klienter](./README.md)
- [MCP-servereksempler](../../../../03-GettingStarted/01-first-server)
- [MCP med LLM-integration](../../../../03-GettingStarted/03-llm-client)
- [Officiel MCP-dokumentation](https://modelcontextprotocol.io/)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.