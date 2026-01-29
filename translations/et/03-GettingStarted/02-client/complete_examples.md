# Täielikud MCP kliendi näited

See kataloog sisaldab täielikult töötavaid MCP klientide näiteid erinevates programmeerimiskeeltes. Iga klient demonstreerib kogu funktsionaalsust, mida on kirjeldatud peamises README.md juhendis.

## Saadaval olevad kliendid

### 1. Java klient (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) üle HTTP
- **Sihtserver**: `http://localhost:8080`
- **Funktsioonid**:
  - Ühenduse loomine ja pingimine
  - Tööriistade loetelu
  - Kalkulaatori operatsioonid (liitmine, lahutamine, korrutamine, jagamine, abi)
  - Vigade käsitlemine ja tulemuste eraldamine

**Käivitamiseks:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# klient (`client_example_csharp.cs`)

- **Transport**: Stdio (Standard Input/Output)
- **Sihtserver**: Kohalik .NET MCP server läbi dotnet run
- **Funktsioonid**:
  - Automaatne serveri käivitamine stdio transpordi kaudu
  - Tööriistade ja ressursside loetelu
  - Kalkulaatori operatsioonid
  - JSON tulemuste parsimine
  - Põhjalik vigade käsitlemine

**Käivitamiseks:**

```bash
dotnet run
```

### 3. TypeScript klient (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Input/Output)
- **Sihtserver**: Kohalik Node.js MCP server
- **Funktsioonid**:
  - Täielik MCP protokolli tugi
  - Tööriistade, ressursside ja käskude operatsioonid
  - Kalkulaatori operatsioonid
  - Ressursside lugemine ja käskude täitmine
  - Tugev vigade käsitlemine

**Käivitamiseks:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python klient (`client_example_python.py`)

- **Transport**: Stdio (Standard Input/Output)  
- **Sihtserver**: Kohalik Python MCP server
- **Funktsioonid**:
  - Async/await mustri kasutamine operatsioonide jaoks
  - Tööriistade ja ressursside avastamine
  - Kalkulaatori operatsioonide testimine
  - Ressursside sisu lugemine
  - Klassipõhine organiseerimine

**Käivitamiseks:**

```bash
python client_example_python.py
```

## Ühised funktsioonid kõigis klientides

Iga kliendi implementatsioon demonstreerib:

1. **Ühenduse haldamine**
   - Ühenduse loomine MCP serveriga
   - Ühenduse vigade käsitlemine
   - Korralik ressursihaldus ja puhastamine

2. **Serveri avastamine**
   - Saadaval olevate tööriistade loetelu
   - Saadaval olevate ressursside loetelu (kui toetatud)
   - Saadaval olevate käskude loetelu (kui toetatud)

3. **Tööriistade kasutamine**
   - Põhilised kalkulaatori operatsioonid (liitmine, lahutamine, korrutamine, jagamine)
   - Abi käsk serveri info jaoks
   - Korralik argumentide edastamine ja tulemuste käsitlemine

4. **Vigade käsitlemine**
   - Ühenduse vead
   - Tööriistade täitmise vead
   - Sujuv ebaõnnestumine ja kasutajale tagasiside andmine

5. **Tulemuste töötlemine**
   - Teksti sisu eraldamine vastustest
   - Väljundi vormindamine loetavuse jaoks
   - Erinevate vastusevormingute käsitlemine

## Eeltingimused

Enne nende klientide käivitamist veenduge, et teil on:

1. **Vastav MCP server käimas** (kataloogist `../01-first-server/`)
2. **Nõutavad sõltuvused paigaldatud** valitud keele jaoks
3. **Õige võrguühendus** (HTTP-põhiste transportide jaoks)

## Peamised erinevused implementatsioonide vahel

| Keel       | Transport | Serveri käivitamine | Async mudel | Põhilised teegid       |
|------------|-----------|---------------------|-------------|------------------------|
| Java       | SSE/HTTP  | Väline              | Sünkroonne  | WebFlux, MCP SDK       |
| C#         | Stdio     | Automaatne          | Async/Await | .NET MCP SDK           |
| TypeScript | Stdio     | Automaatne          | Async/Await | Node MCP SDK           |
| Python     | Stdio     | Automaatne          | AsyncIO     | Python MCP SDK         |
| Rust       | Stdio     | Automaatne          | Async/Await | Rust MCP SDK, Tokio    |

## Järgmised sammud

Pärast nende kliendinäidete uurimist:

1. **Muuda kliente**, et lisada uusi funktsioone või operatsioone
2. **Loo oma server** ja testi seda nende klientidega
3. **Katseta erinevaid transporte** (SSE vs. Stdio)
4. **Ehita keerukam rakendus**, mis integreerib MCP funktsionaalsust

## Tõrkeotsing

### Levinud probleemid

1. **Ühendus keelatud**: Veenduge, et MCP server töötab oodatud pordi/tee peal
2. **Moodulit ei leitud**: Paigaldage nõutav MCP SDK oma keele jaoks
3. **Luba keelatud**: Kontrollige stdio transpordi faililubasid
4. **Tööriista ei leitud**: Veenduge, et server rakendab oodatud tööriistu

### Veaotsingu näpunäited

1. **Luba üksikasjalik logimine** oma MCP SDK-s
2. **Kontrollige serveri logisid** veateadete jaoks
3. **Veenduge, et tööriistade nimed ja signatuurid** ühtivad kliendi ja serveri vahel
4. **Testige MCP Inspectoriga**, et kinnitada serveri funktsionaalsust

## Seotud dokumentatsioon

- [Peamine kliendi juhend](./README.md)
- [MCP serveri näited](../../../../03-GettingStarted/01-first-server)
- [MCP koos LLM integratsiooniga](../../../../03-GettingStarted/03-llm-client)
- [Ametlik MCP dokumentatsioon](https://modelcontextprotocol.io/)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.