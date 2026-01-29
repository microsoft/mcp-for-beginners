# Pilni MCP Klientų Pavyzdžiai

Šiame kataloge pateikiami pilni, veikiantys MCP klientų pavyzdžiai įvairiomis programavimo kalbomis. Kiekvienas klientas demonstruoja visą funkcionalumą, aprašytą pagrindiniame README.md vadove.

## Galimi Klientai

### 1. Java Klientas (`client_example_java.java`)

- **Transportas**: SSE (Server-Sent Events) per HTTP
- **Tikslinis serveris**: `http://localhost:8080`
- **Funkcijos**:
  - Ryšio užmezgimas ir ping
  - Įrankių sąrašas
  - Skaičiuotuvo operacijos (sudėtis, atimtis, daugyba, dalyba, pagalba)
  - Klaidų tvarkymas ir rezultatų išgavimas

**Kaip paleisti:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Klientas (`client_example_csharp.cs`)

- **Transportas**: Stdio (Standartinis įvestis/išvestis)
- **Tikslinis serveris**: Vietinis .NET MCP serveris per dotnet run
- **Funkcijos**:
  - Automatinis serverio paleidimas per stdio transportą
  - Įrankių ir resursų sąrašas
  - Skaičiuotuvo operacijos
  - JSON rezultatų analizė
  - Išsamus klaidų tvarkymas

**Kaip paleisti:**

```bash
dotnet run
```

### 3. TypeScript Klientas (`client_example_typescript.ts`)

- **Transportas**: Stdio (Standartinis įvestis/išvestis)
- **Tikslinis serveris**: Vietinis Node.js MCP serveris
- **Funkcijos**:
  - Pilnas MCP protokolo palaikymas
  - Įrankių, resursų ir užklausų operacijos
  - Skaičiuotuvo operacijos
  - Resursų skaitymas ir užklausų vykdymas
  - Patikimas klaidų tvarkymas

**Kaip paleisti:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Klientas (`client_example_python.py`)

- **Transportas**: Stdio (Standartinis įvestis/išvestis)  
- **Tikslinis serveris**: Vietinis Python MCP serveris
- **Funkcijos**:
  - Async/await modelis operacijoms
  - Įrankių ir resursų atradimas
  - Skaičiuotuvo operacijų testavimas
  - Resursų turinio skaitymas
  - Klasėmis pagrįsta organizacija

**Kaip paleisti:**

```bash
python client_example_python.py
```

## Bendros Funkcijos Visuose Klientuose

Kiekvienas klientas demonstruoja:

1. **Ryšio Valdymą**
   - Ryšio užmezgimą su MCP serveriu
   - Klaidų tvarkymą ryšio metu
   - Tinkamą resursų valymą ir uždarymą

2. **Serverio Atradimą**
   - Galimų įrankių sąrašą
   - Galimų resursų sąrašą (jei palaikoma)
   - Galimų užklausų sąrašą (jei palaikoma)

3. **Įrankių Naudojimą**
   - Pagrindines skaičiuotuvo operacijas (sudėtis, atimtis, daugyba, dalyba)
   - Pagalbos komandą serverio informacijai
   - Tinkamą argumentų perdavimą ir rezultatų tvarkymą

4. **Klaidų Tvarkymą**
   - Ryšio klaidas
   - Įrankių vykdymo klaidas
   - Sklandų gedimų valdymą ir naudotojo informavimą

5. **Rezultatų Apdorojimą**
   - Teksto turinio išgavimą iš atsakymų
   - Rezultatų formatavimą patogiam skaitymui
   - Skirtingų atsakymų formatų tvarkymą

## Būtinos Sąlygos

Prieš paleidžiant šiuos klientus, įsitikinkite, kad:

1. **Atitinkamas MCP serveris veikia** (iš `../01-first-server/`)
2. **Įdiegti reikalingi priklausomybės** jūsų pasirinktai kalbai
3. **Tinkamas tinklo ryšys** (HTTP pagrindu veikiančiam transportui)

## Pagrindiniai Skirtumai Tarp Įgyvendinimų

| Kalba      | Transportas | Serverio Paleidimas | Async Modelis | Pagrindinės Bibliotekos |
|------------|-------------|---------------------|---------------|-------------------------|
| Java       | SSE/HTTP    | Išorinis           | Sinchroninis  | WebFlux, MCP SDK        |
| C#         | Stdio       | Automatinis        | Async/Await   | .NET MCP SDK            |
| TypeScript | Stdio       | Automatinis        | Async/Await   | Node MCP SDK            |
| Python     | Stdio       | Automatinis        | AsyncIO       | Python MCP SDK          |
| Rust       | Stdio       | Automatinis        | Async/Await   | Rust MCP SDK, Tokio     |

## Kiti Žingsniai

Išnagrinėję šiuos klientų pavyzdžius:

1. **Modifikuokite klientus**, kad pridėtumėte naujų funkcijų ar operacijų
2. **Sukurkite savo serverį** ir išbandykite jį su šiais klientais
3. **Eksperimentuokite su skirtingais transportais** (SSE vs. Stdio)
4. **Sukurkite sudėtingesnę aplikaciją**, integruojančią MCP funkcionalumą

## Trikčių Šalinimas

### Dažnos Problemos

1. **Ryšys atmestas**: Įsitikinkite, kad MCP serveris veikia numatytu portu/keliu
2. **Modulis nerastas**: Įdiekite reikalingą MCP SDK jūsų kalbai
3. **Prieiga uždrausta**: Patikrinkite failų leidimus stdio transportui
4. **Įrankis nerastas**: Patikrinkite, ar serveris įgyvendina tikėtinus įrankius

### Patarimai Derinimui

1. **Įjunkite išsamų logavimą** savo MCP SDK
2. **Patikrinkite serverio logus** dėl klaidų pranešimų
3. **Patikrinkite įrankių pavadinimus ir parašus**, kad jie sutaptų tarp kliento ir serverio
4. **Išbandykite su MCP Inspector**, kad patvirtintumėte serverio funkcionalumą

## Susijusi Dokumentacija

- [Pagrindinis Klientų Vadovas](./README.md)
- [MCP Serverio Pavyzdžiai](../../../../03-GettingStarted/01-first-server)
- [MCP su LLM Integracija](../../../../03-GettingStarted/03-llm-client)
- [Oficiali MCP Dokumentacija](https://modelcontextprotocol.io/)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.