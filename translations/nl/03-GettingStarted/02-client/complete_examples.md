# Volledige MCP Client Voorbeelden

Deze map bevat complete, werkende voorbeelden van MCP-clients in verschillende programmeertalen. Elke client demonstreert de volledige functionaliteit zoals beschreven in de hoofdhandleiding README.md.

## Beschikbare Clients

### 1. Java Client (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) via HTTP
- **Doelserver**: `http://localhost:8080`
- **Functies**:
  - Verbinding maken en ping
  - Lijst van tools ophalen
  - Rekenmachinebewerkingen (optellen, aftrekken, vermenigvuldigen, delen, help)
  - Foutafhandeling en resultaatverwerking

**Uitvoeren:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Client (`client_example_csharp.cs`)

- **Transport**: Stdio (Standaard Invoer/Uitvoer)
- **Doelserver**: Lokale .NET MCP-server via dotnet run
- **Functies**:
  - Automatisch opstarten van de server via stdio-transport
  - Lijst van tools en bronnen ophalen
  - Rekenmachinebewerkingen
  - JSON-resultaat parsing
  - Uitgebreide foutafhandeling

**Uitvoeren:**

```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)

- **Transport**: Stdio (Standaard Invoer/Uitvoer)
- **Doelserver**: Lokale Node.js MCP-server
- **Functies**:
  - Volledige ondersteuning van het MCP-protocol
  - Tool-, bron- en promptbewerkingen
  - Rekenmachinebewerkingen
  - Bronnen lezen en prompts uitvoeren
  - Robuuste foutafhandeling

**Uitvoeren:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Client (`client_example_python.py`)

- **Transport**: Stdio (Standaard Invoer/Uitvoer)  
- **Doelserver**: Lokale Python MCP-server
- **Functies**:
  - Async/await patroon voor bewerkingen
  - Ontdekking van tools en bronnen
  - Testen van rekenmachinebewerkingen
  - Inhoud van bronnen lezen
  - Class-gebaseerde organisatie

**Uitvoeren:**

```bash
python client_example_python.py
```

## Gemeenschappelijke Functies van Alle Clients

Elke clientimplementatie demonstreert:

1. **Verbindingsbeheer**
   - Verbinding maken met de MCP-server
   - Afhandelen van verbindingsfouten
   - Correct opruimen en beheren van bronnen

2. **Serverontdekking**
   - Beschikbare tools weergeven
   - Beschikbare bronnen weergeven (indien ondersteund)
   - Beschikbare prompts weergeven (indien ondersteund)

3. **Toolaanroepen**
   - Basisbewerkingen van de rekenmachine (optellen, aftrekken, vermenigvuldigen, delen)
   - Help-opdracht voor serverinformatie
   - Correct doorgeven van argumenten en verwerken van resultaten

4. **Foutafhandeling**
   - Verbindingsfouten
   - Fouten bij het uitvoeren van tools
   - Gracieus falen en feedback aan de gebruiker

5. **Resultaatverwerking**
   - Tekstinhoud uit reacties halen
   - Uitvoer formatteren voor leesbaarheid
   - Verschillende antwoordformaten afhandelen

## Vereisten

Voordat je deze clients uitvoert, zorg ervoor dat je:

1. **De bijbehorende MCP-server hebt draaien** (uit `../01-first-server/`)
2. **De vereiste afhankelijkheden hebt geïnstalleerd** voor de gekozen taal
3. **Correcte netwerkverbinding hebt** (voor HTTP-gebaseerde transports)

## Belangrijke Verschillen Tussen Implementaties

| Taal       | Transport | Server Starten | Async Model | Belangrijke Bibliotheken |
|------------|-----------|----------------|-------------|--------------------------|
| Java       | SSE/HTTP  | Extern         | Sync        | WebFlux, MCP SDK         |
| C#         | Stdio     | Automatisch    | Async/Await | .NET MCP SDK             |
| TypeScript | Stdio     | Automatisch    | Async/Await | Node MCP SDK             |
| Python     | Stdio     | Automatisch    | AsyncIO     | Python MCP SDK           |
| Rust       | Stdio     | Automatisch    | Async/Await | Rust MCP SDK, Tokio      |

## Volgende Stappen

Na het verkennen van deze clientvoorbeelden:

1. **Pas de clients aan** om nieuwe functies of bewerkingen toe te voegen
2. **Maak je eigen server** en test deze met deze clients
3. **Experimenteer met verschillende transports** (SSE versus Stdio)
4. **Bouw een complexere applicatie** die MCP-functionaliteit integreert

## Problemen Oplossen

### Veelvoorkomende Problemen

1. **Verbinding geweigerd**: Zorg ervoor dat de MCP-server draait op de verwachte poort/pad
2. **Module niet gevonden**: Installeer de vereiste MCP SDK voor je taal
3. **Toegang geweigerd**: Controleer bestandsrechten voor stdio-transport
4. **Tool niet gevonden**: Controleer of de server de verwachte tools implementeert

### Debug Tips

1. **Schakel uitgebreide logging in** in je MCP SDK
2. **Controleer serverlogs** op foutmeldingen
3. **Controleer toolnamen en handtekeningen** of deze overeenkomen tussen client en server
4. **Test eerst met MCP Inspector** om de serverfunctionaliteit te valideren

## Gerelateerde Documentatie

- [Hoofdhandleiding voor Clients](./README.md)
- [MCP Server Voorbeelden](../../../../03-GettingStarted/01-first-server)
- [MCP met LLM-integratie](../../../../03-GettingStarted/03-llm-client)
- [Officiële MCP Documentatie](https://modelcontextprotocol.io/)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.