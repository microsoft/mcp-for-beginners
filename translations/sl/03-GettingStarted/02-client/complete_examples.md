# Popolni primeri MCP odjemalcev

Ta mapa vsebuje popolne, delujoče primere MCP odjemalcev v različnih programskih jezikih. Vsak odjemalec prikazuje celotno funkcionalnost, opisano v glavnem vodiču README.md.

## Razpoložljivi odjemalci

### 1. Java odjemalec (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) prek HTTP
- **Ciljni strežnik**: `http://localhost:8080`
- **Funkcionalnosti**:
  - Vzpostavitev povezave in ping
  - Seznam orodij
  - Operacije kalkulatorja (seštevanje, odštevanje, množenje, deljenje, pomoč)
  - Obdelava napak in pridobivanje rezultatov

**Za zagon:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# odjemalec (`client_example_csharp.cs`)

- **Transport**: Stdio (Standardni vhod/izhod)
- **Ciljni strežnik**: Lokalni .NET MCP strežnik prek ukaza `dotnet run`
- **Funkcionalnosti**:
  - Samodejni zagon strežnika prek stdio transporta
  - Seznam orodij in virov
  - Operacije kalkulatorja
  - Parsiranje rezultatov v JSON formatu
  - Celovita obdelava napak

**Za zagon:**

```bash
dotnet run
```

### 3. TypeScript odjemalec (`client_example_typescript.ts`)

- **Transport**: Stdio (Standardni vhod/izhod)
- **Ciljni strežnik**: Lokalni Node.js MCP strežnik
- **Funkcionalnosti**:
  - Popolna podpora MCP protokolu
  - Operacije z orodji, viri in pozivi
  - Operacije kalkulatorja
  - Branje virov in izvajanje pozivov
  - Zanesljiva obdelava napak

**Za zagon:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python odjemalec (`client_example_python.py`)

- **Transport**: Stdio (Standardni vhod/izhod)  
- **Ciljni strežnik**: Lokalni Python MCP strežnik
- **Funkcionalnosti**:
  - Vzorec async/await za operacije
  - Odkritje orodij in virov
  - Testiranje operacij kalkulatorja
  - Branje vsebine virov
  - Organizacija na osnovi razredov

**Za zagon:**

```bash
python client_example_python.py
```

## Skupne funkcionalnosti vseh odjemalcev

Vsaka implementacija odjemalca prikazuje:

1. **Upravljanje povezave**
   - Vzpostavitev povezave z MCP strežnikom
   - Obdelava napak pri povezavi
   - Pravilno čiščenje in upravljanje virov

2. **Odkritje strežnika**
   - Seznam razpoložljivih orodij
   - Seznam razpoložljivih virov (kjer je podprto)
   - Seznam razpoložljivih pozivov (kjer je podprto)

3. **Izvajanje orodij**
   - Osnovne operacije kalkulatorja (seštevanje, odštevanje, množenje, deljenje)
   - Ukaz za pomoč za informacije o strežniku
   - Pravilno posredovanje argumentov in obdelava rezultatov

4. **Obdelava napak**
   - Napake pri povezavi
   - Napake pri izvajanju orodij
   - Prijazno obveščanje uporabnika ob napakah

5. **Obdelava rezultatov**
   - Pridobivanje besedilne vsebine iz odgovorov
   - Oblikovanje izhodnih podatkov za boljšo berljivost
   - Obdelava različnih formatov odgovorov

## Predpogoji

Pred zagonom teh odjemalcev poskrbite za:

1. **Zagon ustreznega MCP strežnika** (iz `../01-first-server/`)
2. **Namestitev potrebnih odvisnosti** za izbrani programski jezik
3. **Ustrezno omrežno povezljivost** (za transporte na osnovi HTTP)

## Ključne razlike med implementacijami

| Jezik      | Transport | Zagon strežnika | Async model | Ključne knjižnice   |
|------------|-----------|-----------------|-------------|---------------------|
| Java       | SSE/HTTP  | Zunanji         | Sinhrono    | WebFlux, MCP SDK    |
| C#         | Stdio     | Samodejno       | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Samodejno       | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Samodejno       | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Samodejno       | Async/Await | Rust MCP SDK, Tokio |

## Naslednji koraki

Po raziskovanju teh primerov odjemalcev:

1. **Prilagodite odjemalce**, da dodate nove funkcionalnosti ali operacije
2. **Ustvarite svoj strežnik** in ga preizkusite s temi odjemalci
3. **Eksperimentirajte z različnimi transporti** (SSE proti Stdio)
4. **Zgradite bolj zapleteno aplikacijo**, ki vključuje MCP funkcionalnosti

## Odpravljanje težav

### Pogoste težave

1. **Povezava zavrnjena**: Prepričajte se, da MCP strežnik deluje na pričakovanem portu/poti
2. **Modul ni najden**: Namestite zahtevani MCP SDK za vaš jezik
3. **Dostop zavrnjen**: Preverite dovoljenja za datoteke pri stdio transportu
4. **Orodje ni najdeno**: Preverite, ali strežnik podpira pričakovana orodja

### Nasveti za odpravljanje napak

1. **Omogočite podrobno beleženje** v vašem MCP SDK
2. **Preverite dnevnike strežnika** za sporočila o napakah
3. **Preverite imena in podpise orodij**, da se ujemajo med odjemalcem in strežnikom
4. **Najprej preizkusite z MCP Inspectorjem**, da preverite funkcionalnost strežnika

## Povezana dokumentacija

- [Glavni vodič za odjemalce](./README.md)
- [Primeri MCP strežnikov](../../../../03-GettingStarted/01-first-server)
- [MCP z integracijo LLM](../../../../03-GettingStarted/03-llm-client)
- [Uradna dokumentacija MCP](https://modelcontextprotocol.io/)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.