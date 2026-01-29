# Komplette MCP-klienteksempler

Denne katalogen inneholder komplette, fungerende eksempler på MCP-klienter i forskjellige programmeringsspråk. Hver klient demonstrerer hele funksjonaliteten som er beskrevet i hovedveiledningen README.md.

## Tilgjengelige klienter

### 1. Java-klient (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) over HTTP
- **Målserver**: `http://localhost:8080`
- **Funksjoner**:
  - Opprettelse av tilkobling og ping
  - Verktøyliste
  - Kalkulatoroperasjoner (add, subtract, multiply, divide, help)
  - Feilhåndtering og resultatuttrekk

**For å kjøre:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C#-klient (`client_example_csharp.cs`)

- **Transport**: Stdio (Standard Input/Output)
- **Målserver**: Lokal .NET MCP-server via dotnet run
- **Funksjoner**:
  - Automatisk serveroppstart via stdio-transport
  - Liste over verktøy og ressurser
  - Kalkulatoroperasjoner
  - JSON-resultatparsing
  - Omfattende feilhåndtering

**For å kjøre:**

```bash
dotnet run
```

### 3. TypeScript-klient (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Input/Output)
- **Målserver**: Lokal Node.js MCP-server
- **Funksjoner**:
  - Full støtte for MCP-protokollen
  - Verktøy-, ressurs- og promptoperasjoner
  - Kalkulatoroperasjoner
  - Ressurslesing og promptutførelse
  - Robust feilhåndtering

**For å kjøre:**

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
- **Funksjoner**:
  - Async/await-mønster for operasjoner
  - Oppdagelse av verktøy og ressurser
  - Testing av kalkulatoroperasjoner
  - Lesing av ressursinnhold
  - Klassebasert organisering

**For å kjøre:**

```bash
python client_example_python.py
```

## Felles funksjoner for alle klienter

Hver klientimplementasjon demonstrerer:

1. **Tilkoblingshåndtering**
   - Opprette tilkobling til MCP-serveren
   - Håndtere tilkoblingsfeil
   - Ryddig opprydding og ressursstyring

2. **Serveroppdagelse**
   - Liste over tilgjengelige verktøy
   - Liste over tilgjengelige ressurser (hvor støttet)
   - Liste over tilgjengelige prompts (hvor støttet)

3. **Verktøyutførelse**
   - Grunnleggende kalkulatoroperasjoner (add, subtract, multiply, divide)
   - Help-kommando for serverinformasjon
   - Korrekt argumentoverføring og resultathåndtering

4. **Feilhåndtering**
   - Tilkoblingsfeil
   - Feil ved verktøyutførelse
   - Grasiøs feilhåndtering og tilbakemelding til brukeren

5. **Resultatbehandling**
   - Trekke ut tekstinnhold fra svar
   - Formatere utdata for lesbarhet
   - Håndtere ulike svarformater

## Forutsetninger

Før du kjører disse klientene, sørg for at du har:

1. **Den tilsvarende MCP-serveren kjørende** (fra `../01-first-server/`)
2. **Nødvendige avhengigheter installert** for det valgte språket
3. **Korrekt nettverkstilkobling** (for HTTP-baserte transporter)

## Viktige forskjeller mellom implementasjoner

| Språk      | Transport | Serveroppstart | Async-modell | Nøkkelbiblioteker   |
|------------|-----------|----------------|--------------|---------------------|
| Java       | SSE/HTTP  | Ekstern        | Synkron      | WebFlux, MCP SDK    |
| C#         | Stdio     | Automatisk     | Async/Await  | .NET MCP SDK        |
| TypeScript | Stdio     | Automatisk     | Async/Await  | Node MCP SDK        |
| Python     | Stdio     | Automatisk     | AsyncIO      | Python MCP SDK      |
| Rust       | Stdio     | Automatisk     | Async/Await  | Rust MCP SDK, Tokio |

## Neste steg

Etter å ha utforsket disse klienteksemplene:

1. **Modifiser klientene** for å legge til nye funksjoner eller operasjoner
2. **Lag din egen server** og test den med disse klientene
3. **Eksperimenter med ulike transporter** (SSE vs. Stdio)
4. **Bygg en mer kompleks applikasjon** som integrerer MCP-funksjonalitet

## Feilsøking

### Vanlige problemer

1. **Tilkobling nektet**: Sørg for at MCP-serveren kjører på forventet port/sti
2. **Modul ikke funnet**: Installer nødvendig MCP SDK for ditt språk
3. **Ingen tilgang**: Sjekk filrettigheter for stdio-transport
4. **Verktøy ikke funnet**: Verifiser at serveren implementerer de forventede verktøyene

### Feiltips

1. **Aktiver detaljert logging** i MCP SDK-en din
2. **Sjekk serverlogger** for feilmeldinger
3. **Bekreft verktøynavn og signaturer** samsvarer mellom klient og server
4. **Test med MCP Inspector** først for å validere serverfunksjonalitet

## Relatert dokumentasjon

- [Hovedveiledning for klienter](./README.md)
- [Eksempler på MCP-servere](../../../../03-GettingStarted/01-first-server)
- [MCP med LLM-integrasjon](../../../../03-GettingStarted/03-llm-client)
- [Offisiell MCP-dokumentasjon](https://modelcontextprotocol.io/)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.