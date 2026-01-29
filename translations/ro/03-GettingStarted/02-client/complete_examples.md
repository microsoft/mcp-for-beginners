# Exemple Complete de Clienți MCP

Acest director conține exemple complete și funcționale de clienți MCP în diferite limbaje de programare. Fiecare client demonstrează întreaga funcționalitate descrisă în tutorialul principal din README.md.

## Clienți Disponibili

### 1. Client Java (`client_example_java.java`)

- **Transport**: SSE (Evenimente Trimise de Server) prin HTTP
- **Server Țintă**: `http://localhost:8080`
- **Funcționalități**:
  - Stabilirea conexiunii și ping
  - Listarea uneltelor
  - Operații ale calculatorului (adunare, scădere, înmulțire, împărțire, ajutor)
  - Gestionarea erorilor și extragerea rezultatelor

**Pentru a rula:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. Client C# (`client_example_csharp.cs`)

- **Transport**: Stdio (Intrare/Ieșire Standard)
- **Server Țintă**: Server MCP local .NET prin dotnet run
- **Funcționalități**:
  - Pornirea automată a serverului prin transport stdio
  - Listarea uneltelor și resurselor
  - Operații ale calculatorului
  - Parsarea rezultatelor JSON
  - Gestionare completă a erorilor

**Pentru a rula:**

```bash
dotnet run
```

### 3. Client TypeScript (`client_example_typescript.ts`)

- **Transport**: Stdio (Intrare/Ieșire Standard)
- **Server Țintă**: Server MCP local Node.js
- **Funcționalități**:
  - Suport complet pentru protocolul MCP
  - Operații cu unelte, resurse și prompturi
  - Operații ale calculatorului
  - Citirea resurselor și executarea prompturilor
  - Gestionare robustă a erorilor

**Pentru a rula:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Client Python (`client_example_python.py`)

- **Transport**: Stdio (Intrare/Ieșire Standard)  
- **Server Țintă**: Server MCP local Python
- **Funcționalități**:
  - Model async/await pentru operații
  - Descoperirea uneltelor și resurselor
  - Testarea operațiilor calculatorului
  - Citirea conținutului resurselor
  - Organizare bazată pe clase

**Pentru a rula:**

```bash
python client_example_python.py
```

## Funcționalități Comune Tuturor Clienților

Fiecare implementare de client demonstrează:

1. **Gestionarea Conexiunii**
   - Stabilirea conexiunii cu serverul MCP
   - Gestionarea erorilor de conexiune
   - Curățare corespunzătoare și gestionarea resurselor

2. **Descoperirea Serverului**
   - Listarea uneltelor disponibile
   - Listarea resurselor disponibile (unde este suportat)
   - Listarea prompturilor disponibile (unde este suportat)

3. **Invocarea Uneltelor**
   - Operații de bază ale calculatorului (adunare, scădere, înmulțire, împărțire)
   - Comanda de ajutor pentru informații despre server
   - Transmiterea corectă a argumentelor și gestionarea rezultatelor

4. **Gestionarea Erorilor**
   - Erori de conexiune
   - Erori de execuție a uneltelor
   - Eșecuri gestionate elegant și feedback pentru utilizator

5. **Procesarea Rezultatelor**
   - Extragerea conținutului text din răspunsuri
   - Formatarea ieșirii pentru lizibilitate
   - Gestionarea diferitelor formate de răspuns

## Cerințe Prealabile

Înainte de a rula acești clienți, asigurați-vă că aveți:

1. **Serverul MCP corespunzător pornit** (din `../01-first-server/`)
2. **Dependențele necesare instalate** pentru limbajul ales
3. **Conectivitate de rețea corespunzătoare** (pentru transporturile bazate pe HTTP)

## Diferențe Cheie Între Implementări

| Limbaj     | Transport | Pornirea Serverului | Model Async | Biblioteci Cheie    |
|------------|-----------|---------------------|-------------|---------------------|
| Java       | SSE/HTTP  | Extern              | Sincron     | WebFlux, MCP SDK    |
| C#         | Stdio     | Automat             | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Automat             | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Automat             | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Automat             | Async/Await | Rust MCP SDK, Tokio |

## Pași Următori

După ce explorați aceste exemple de clienți:

1. **Modificați clienții** pentru a adăuga funcționalități sau operații noi
2. **Creați propriul server** și testați-l cu acești clienți
3. **Experimentați cu diferite transporturi** (SSE vs. Stdio)
4. **Construiți o aplicație mai complexă** care integrează funcționalitatea MCP

## Depanare

### Probleme Comune

1. **Conexiune refuzată**: Asigurați-vă că serverul MCP rulează pe portul/calea așteptată
2. **Modulul nu a fost găsit**: Instalați SDK-ul MCP necesar pentru limbajul dvs.
3. **Permisiune refuzată**: Verificați permisiunile fișierelor pentru transportul stdio
4. **Unealta nu a fost găsită**: Verificați dacă serverul implementează uneltele așteptate

### Sfaturi pentru Debugging

1. **Activați jurnalizarea detaliată** în SDK-ul MCP
2. **Verificați jurnalele serverului** pentru mesaje de eroare
3. **Asigurați-vă că numele și semnăturile uneltelor** se potrivesc între client și server
4. **Testați mai întâi cu MCP Inspector** pentru a valida funcționalitatea serverului

## Documentație Aferentă

- [Tutorial Principal pentru Clienți](./README.md)
- [Exemple de Server MCP](../../../../03-GettingStarted/01-first-server)
- [MCP cu Integrare LLM](../../../../03-GettingStarted/03-llm-client)
- [Documentația Oficială MCP](https://modelcontextprotocol.io/)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.