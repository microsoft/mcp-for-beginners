# Kompletni Primjeri MCP Klijenata

Ovaj direktorij sadrži kompletne, funkcionalne primjere MCP klijenata u različitim programskim jezicima. Svaki klijent demonstrira punu funkcionalnost opisanu u glavnom README.md vodiču.

## Dostupni Klijenti

### 1. Java Klijent (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) preko HTTP-a
- **Ciljani Server**: `http://localhost:8080`
- **Značajke**:
  - Uspostavljanje veze i ping
  - Popis alata
  - Operacije kalkulatora (zbrajanje, oduzimanje, množenje, dijeljenje, pomoć)
  - Rukovanje greškama i izdvajanje rezultata

**Za pokretanje:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Klijent (`client_example_csharp.cs`)

- **Transport**: Stdio (Standardni Ulaz/Izlaz)
- **Ciljani Server**: Lokalni .NET MCP server putem dotnet run
- **Značajke**:
  - Automatsko pokretanje servera putem stdio transporta
  - Popis alata i resursa
  - Operacije kalkulatora
  - Parsiranje JSON rezultata
  - Sveobuhvatno rukovanje greškama

**Za pokretanje:**

```bash
dotnet run
```

### 3. TypeScript Klijent (`client_example_typescript.ts`)

- **Transport**: Stdio (Standardni Ulaz/Izlaz)
- **Ciljani Server**: Lokalni Node.js MCP server
- **Značajke**:
  - Potpuna podrška za MCP protokol
  - Operacije alata, resursa i upita
  - Operacije kalkulatora
  - Čitanje resursa i izvršavanje upita
  - Robusno rukovanje greškama

**Za pokretanje:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Klijent (`client_example_python.py`)

- **Transport**: Stdio (Standardni Ulaz/Izlaz)  
- **Ciljani Server**: Lokalni Python MCP server
- **Značajke**:
  - Async/await obrazac za operacije
  - Otkrivanje alata i resursa
  - Testiranje operacija kalkulatora
  - Čitanje sadržaja resursa
  - Organizacija temeljena na klasama

**Za pokretanje:**

```bash
python client_example_python.py
```

## Zajedničke Značajke Svih Klijenata

Svaka implementacija klijenta demonstrira:

1. **Upravljanje Vezi**
   - Uspostavljanje veze s MCP serverom
   - Rukovanje greškama veze
   - Pravilno čišćenje i upravljanje resursima

2. **Otkrivanje Servera**
   - Popis dostupnih alata
   - Popis dostupnih resursa (gdje je podržano)
   - Popis dostupnih upita (gdje je podržano)

3. **Pozivanje Alata**
   - Osnovne operacije kalkulatora (zbrajanje, oduzimanje, množenje, dijeljenje)
   - Pomoćna naredba za informacije o serveru
   - Pravilno prosljeđivanje argumenata i rukovanje rezultatima

4. **Rukovanje Greškama**
   - Greške veze
   - Greške pri izvršavanju alata
   - Graciozni neuspjeh i povratne informacije korisniku

5. **Obrada Rezultata**
   - Izdvajanje tekstualnog sadržaja iz odgovora
   - Formatiranje izlaza za čitljivost
   - Rukovanje različitim formatima odgovora

## Preduvjeti

Prije pokretanja ovih klijenata, osigurajte:

1. **Da odgovarajući MCP server radi** (iz `../01-first-server/`)
2. **Da su instalirane potrebne ovisnosti** za odabrani jezik
3. **Pravilnu mrežnu povezanost** (za transporte temeljene na HTTP-u)

## Ključne Razlike Između Implementacija

| Jezik      | Transport | Pokretanje Servera | Async Model | Ključne Biblioteke  |
|------------|-----------|--------------------|-------------|---------------------|
| Java       | SSE/HTTP  | Eksterno           | Sinkrono    | WebFlux, MCP SDK    |
| C#         | Stdio     | Automatski         | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Automatski         | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Automatski         | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Automatski         | Async/Await | Rust MCP SDK, Tokio |

## Sljedeći Koraci

Nakon istraživanja ovih primjera klijenata:

1. **Prilagodite klijente** kako biste dodali nove značajke ili operacije
2. **Kreirajte vlastiti server** i testirajte ga s ovim klijentima
3. **Eksperimentirajte s različitim transportima** (SSE vs. Stdio)
4. **Izgradite složeniju aplikaciju** koja integrira MCP funkcionalnost

## Rješavanje Problema

### Uobičajeni Problemi

1. **Veza odbijena**: Provjerite radi li MCP server na očekivanom portu/putanji
2. **Modul nije pronađen**: Instalirajte potrebni MCP SDK za vaš jezik
3. **Dopuštenje odbijeno**: Provjerite dozvole datoteka za stdio transport
4. **Alat nije pronađen**: Provjerite implementira li server očekivane alate

### Savjeti za Debugging

1. **Omogućite detaljno logiranje** u vašem MCP SDK-u
2. **Provjerite logove servera** za poruke o greškama
3. **Provjerite nazive i potpise alata** između klijenta i servera
4. **Testirajte s MCP Inspectorom** kako biste prvo validirali funkcionalnost servera

## Povezana Dokumentacija

- [Glavni Vodič za Klijente](./README.md)
- [Primjeri MCP Servera](../../../../03-GettingStarted/01-first-server)
- [MCP s LLM Integracijom](../../../../03-GettingStarted/03-llm-client)
- [Službena MCP Dokumentacija](https://modelcontextprotocol.io/)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.